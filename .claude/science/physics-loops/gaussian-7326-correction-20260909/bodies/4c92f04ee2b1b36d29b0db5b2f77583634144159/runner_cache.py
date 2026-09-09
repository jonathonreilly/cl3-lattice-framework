"""Content-pinned runner output cache for the audit lane.

Each runner under `scripts/` has one canonical cache file at:

    logs/runner-cache/<runner-stem>.txt

The header always pins the cache to the runner's content SHA-256. A runner
that reads mutable repository inputs may additionally declare a top-level
``AUDIT_INPUT_PATHS`` tuple. For such a runner the header also pins a
deterministic fingerprint of those files, and cache consumption rejects any
input drift. The optional pre-commit hook and diff-scoped CLI can select
changed runners and declared inputs for an operator or external automation.

Format (no timestamps anywhere — gate-clean):

    ===== runner cache v1 =====
    runner: scripts/<name>.py
    runner_sha256: <hex>
    input_fingerprint_sha256: <hex>  # only with AUDIT_INPUT_PATHS
    timeout_sec: 120
    exit_code: 0
    elapsed_sec: 12.34
    status: ok
    ----- stdout -----
    <stdout, capped at 200KB tail>
    ----- stderr -----
    <stderr, capped at 50KB tail>

The audit runner uses this cache for readiness and non-authoritative
diagnostics; authority-bearing prompts re-execute the runner. The pre-commit
hook and diff-scoped CLI can select a cache when either its runner or one of
its declared inputs changes. Refresh binds the output to identities captured
before execution and refuses to write if the runner or any declared input
moves during execution.
"""
from __future__ import annotations

import ast
import hashlib
import os
import re
import stat
import subprocess
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "logs" / "runner-cache"
LIVE_LOG_DIR = CACHE_DIR / ".in-progress"

CACHE_HEADER_PREFIX = "===== runner cache v1 ====="
SHA_RE = re.compile(r"^runner_sha256:\s*([0-9a-f]{64})\s*$", re.MULTILINE)
INPUT_FINGERPRINT_RE = re.compile(
    r"^input_fingerprint_sha256:\s*([0-9a-f]{64})\s*$",
    re.MULTILINE,
)
RUNNER_PATH_RE = re.compile(r"^runner:\s*(.+)$", re.MULTILINE)
STATUS_RE = re.compile(r"^status:\s*(\S+)\s*$", re.MULTILINE)
EXIT_CODE_RE = re.compile(r"^exit_code:\s*(\S+)\s*$", re.MULTILINE)

# Per-runner declared timeout. Authors who know their runner is slow
# add `AUDIT_TIMEOUT_SEC = N` near the top of the runner module. The
# precompute orchestrator and the audit runner both honor this value
# in preference to the legacy substring overrides and the default.
TIMEOUT_HEADER_RE = re.compile(
    r"^AUDIT_TIMEOUT_SEC\s*=\s*(\d+)\s*(?:#.*)?$",
    re.MULTILINE,
)
TIMEOUT_DEFAULT_SEC = 120

# Legacy substring map. Kept as a fallback only for runners that have
# not yet declared `AUDIT_TIMEOUT_SEC` in their source. New runners
# should declare directly; over time this list shrinks to zero.
TIMEOUT_LEGACY_OVERRIDES: list[tuple[str, int]] = [
    ("frontier_alpha_s", 900),
    ("frontier_confinement", 900),
    ("frontier_gauge_vacuum_plaquette_perron", 900),
    ("frontier_gauge_vacuum_plaquette_reduction", 900),
    ("frontier_gauge_vacuum_plaquette_spectral", 900),
    ("frontier_gauge_vacuum_plaquette_susceptibility", 900),
    ("frontier_yt_uv_to_ir", 900),
    ("frontier_yt_p1_delta_r_master", 900),
    ("frontier_higgs_mass_full", 900),
    ("frontier_dm_neutrino_source_surface", 600),
    ("frontier_ckm_atlas", 600),
    ("frontier_self_consistent_field", 600),
    ("frontier_emergent_lorentz", 600),
]


@dataclass(frozen=True)
class RunnerIdentity:
    """Immutable source identities to which one execution result is bound."""

    runner_sha256: str
    input_fingerprint_sha256: str | None


@dataclass(frozen=True)
class ExecutionIdentity:
    """Content identity plus filesystem-generation observations.

    Cache freshness stays content-addressed.  The extra stat tokens are used
    only across one execution so an edit/read/restore (ABA) cycle cannot make
    changed bytes look continuously immutable merely because final content
    equals initial content.
    """

    content: RunnerIdentity
    source_stat_tokens: tuple[tuple[str, int, int, int, int, int, int], ...]


class RunnerIdentityChangedError(RuntimeError):
    """The runner or a declared input changed while the runner executed."""


def declared_timeout_for(runner_path: str | Path) -> int | None:
    """Return the runner-declared `AUDIT_TIMEOUT_SEC`, else None.

    The declaration is a top-level Python assignment somewhere in the
    file body (not inside a function). Parsing is regex-based for speed
    — the runner does not need to be importable for us to read its
    declared timeout.
    """
    p = runner_path if isinstance(runner_path, Path) and runner_path.is_absolute() \
        else REPO_ROOT / runner_path
    try:
        text = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return None
    m = TIMEOUT_HEADER_RE.search(text)
    if not m:
        return None
    try:
        val = int(m.group(1))
    except ValueError:
        return None
    return val if val > 0 else None


def runner_timeout_for(runner_path: str | Path,
                       default_sec: int = TIMEOUT_DEFAULT_SEC) -> int:
    """Resolve effective timeout for a runner.

    Priority:
      1. `AUDIT_TIMEOUT_SEC = N` declared at module top of the runner
      2. Legacy substring overrides (`frontier_*` patterns)
      3. `default_sec` (default 120)
    """
    declared = declared_timeout_for(runner_path)
    if declared is not None:
        return declared
    bn = Path(runner_path).name
    for needle, override in TIMEOUT_LEGACY_OVERRIDES:
        if needle in bn:
            return override
    return default_sec


def runner_sha256(runner_path: str | Path) -> str | None:
    """SHA-256 of the runner's source bytes; None if missing on disk."""
    p = runner_path if isinstance(runner_path, Path) and runner_path.is_absolute() \
        else REPO_ROOT / runner_path
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return None


def declared_input_paths(runner_path: str | Path) -> tuple[str, ...] | None:
    """Return a runner's literal ``AUDIT_INPUT_PATHS`` declaration.

    ``None`` means the runner makes no declaration. An empty tuple means a
    declaration exists but is invalid; callers must reject it rather than
    silently treating the runner as input-free. Only non-empty tuples/lists of
    unique, normalized repo-relative paths are accepted. The runner is parsed,
    never imported or executed.
    """
    p = runner_path if isinstance(runner_path, Path) and runner_path.is_absolute() \
        else REPO_ROOT / runner_path
    try:
        tree = ast.parse(p.read_text(encoding="utf-8", errors="replace"))
    except (OSError, SyntaxError):
        return None
    for node in tree.body:
        if not isinstance(node, (ast.Assign, ast.AnnAssign)):
            continue
        targets = node.targets if isinstance(node, ast.Assign) else [node.target]
        if not any(isinstance(t, ast.Name) and t.id == "AUDIT_INPUT_PATHS"
                   for t in targets):
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            return ()
        if not isinstance(value, (tuple, list)) or not value:
            return ()
        out: list[str] = []
        for raw in value:
            if not isinstance(raw, str):
                return ()
            rel = Path(raw)
            if (rel.is_absolute() or not rel.parts or ".." in rel.parts
                    or rel.as_posix() != raw or raw in out):
                return ()
            out.append(raw)
        return tuple(out)
    return None


def declared_input_fingerprint(runner_path: str | Path) -> str | None:
    """Return the v1 fingerprint for declared inputs.

    ``None`` means no declaration. The empty string means the declaration is
    invalid or a declared input is unreadable, which callers must reject.
    """
    paths = declared_input_paths(runner_path)
    if paths is None:
        return None
    if not paths:
        return ""
    digest = hashlib.sha256()
    digest.update(b"runner-cache-input-fingerprint-v1\0")
    for rel in paths:
        try:
            _lexical_path_stat_tokens(rel, REPO_ROOT / rel)
            body = (REPO_ROOT / rel).read_bytes()
        except (OSError, ValueError):
            return ""
        rel_bytes = rel.encode("utf-8")
        digest.update(len(rel_bytes).to_bytes(8, "big"))
        digest.update(rel_bytes)
        digest.update(len(body).to_bytes(8, "big"))
        digest.update(body)
    return digest.hexdigest()


def capture_runner_identity(runner_path: str | Path) -> RunnerIdentity | None:
    """Capture the runner SHA and declared-input fingerprint atomically enough
    for pre/post execution comparison.

    ``None`` means the runner is absent. Invalid declarations and unreadable
    declared inputs fail loudly rather than being treated as input-free.
    """
    runner_sha = runner_sha256(runner_path)
    if runner_sha is None:
        return None
    input_fp = declared_input_fingerprint(runner_path)
    if input_fp == "":
        raise ValueError(
            f"invalid or unreadable AUDIT_INPUT_PATHS declaration: {runner_path}"
        )
    return RunnerIdentity(runner_sha, input_fp)


def _execution_source_paths(runner_path: str | Path) -> tuple[tuple[str, Path], ...]:
    runner = (
        runner_path
        if isinstance(runner_path, Path) and runner_path.is_absolute()
        else REPO_ROOT / runner_path
    )
    try:
        runner_label = runner.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        runner_label = str(runner)
    declared = declared_input_paths(runner_path)
    if declared == ():
        raise ValueError(
            f"invalid or unreadable AUDIT_INPUT_PATHS declaration: {runner_path}"
        )
    paths = [(runner_label, runner)]
    if declared is not None:
        paths.extend((rel, REPO_ROOT / rel) for rel in declared)
    return tuple(paths)


def _lexical_path_stat_tokens(
    label: str, path: Path
) -> tuple[tuple[str, int, int, int, int, int, int], ...]:
    """Observe each repo-relative path component without following links."""
    try:
        relative = path.relative_to(REPO_ROOT)
    except ValueError as exc:
        raise ValueError(f"execution source escapes repository: {label}") from exc
    component = REPO_ROOT
    tokens: list[tuple[str, int, int, int, int, int, int]] = []
    for part in relative.parts:
        component /= part
        component_label = component.relative_to(REPO_ROOT).as_posix()
        try:
            observed = component.lstat()
        except OSError as exc:
            raise ValueError(
                f"execution source is unreadable: {component_label}"
            ) from exc
        if stat.S_ISLNK(observed.st_mode):
            raise ValueError(
                f"execution source path may not contain symlinks: {component_label}"
            )
        tokens.append(
            (
                component_label,
                int(observed.st_mode),
                int(observed.st_dev),
                int(observed.st_ino),
                int(observed.st_size),
                int(observed.st_mtime_ns),
                int(observed.st_ctime_ns),
            )
        )
    return tuple(tokens)


def _source_stat_tokens(
    runner_path: str | Path,
) -> tuple[tuple[str, int, int, int, int, int, int], ...]:
    tokens: list[tuple[str, int, int, int, int, int, int]] = []
    for label, path in _execution_source_paths(runner_path):
        tokens.extend(_lexical_path_stat_tokens(label, path))
    return tuple(tokens)


def capture_runner_execution_identity(
    runner_path: str | Path,
) -> ExecutionIdentity | None:
    """Capture content plus filesystem generations for one execution.

    A stable before/content/after observation is required so a source edit
    racing the capture itself is rejected.  ``ctime_ns`` is deliberately part
    of the token: ordinary write-then-restore cycles retain the same content
    hash but advance the file's metadata generation. Every lexical path
    component is observed with ``lstat`` and symlinks are rejected, so swapping
    a parent or leaf link cannot redirect the runner between the two captures.
    """

    for _attempt in range(3):
        try:
            stats_before = _source_stat_tokens(runner_path)
        except ValueError:
            if runner_sha256(runner_path) is None:
                return None
            raise
        content = capture_runner_identity(runner_path)
        if content is None:
            return None
        stats_after = _source_stat_tokens(runner_path)
        if stats_before == stats_after:
            return ExecutionIdentity(content, stats_before)
    raise RunnerIdentityChangedError(
        f"runner or declared input changed while identity was captured: {runner_path}"
    )


def cache_path_for(runner_path: str | Path) -> Path:
    """Canonical cache path for a runner. One file per runner stem."""
    return CACHE_DIR / f"{Path(runner_path).stem}.txt"


def parse_cache_header(text: str) -> dict | None:
    """Parse a cache file body. Returns dict with keys
    runner_path, runner_sha256, input_fingerprint_sha256, status, exit_code
    (str), or None on bad header.
    """
    if not text.startswith(CACHE_HEADER_PREFIX):
        return None
    head = text.split("----- stdout -----", 1)[0]
    sha_m = SHA_RE.search(head)
    rp_m = RUNNER_PATH_RE.search(head)
    if not (sha_m and rp_m):
        return None
    return {
        "runner_path": rp_m.group(1).strip(),
        "runner_sha256": sha_m.group(1),
        "input_fingerprint_sha256": (
            INPUT_FINGERPRINT_RE.search(head).group(1)
            if INPUT_FINGERPRINT_RE.search(head) else None
        ),
        "status": (STATUS_RE.search(head).group(1) if STATUS_RE.search(head) else None),
        "exit_code": (EXIT_CODE_RE.search(head).group(1) if EXIT_CODE_RE.search(head) else None),
    }


def load_cache(runner_path: str | Path) -> tuple[Path, dict | None, str | None]:
    """Return (cache_path, parsed_header_or_None, body_text_or_None)."""
    p = cache_path_for(runner_path)
    if not p.exists():
        return p, None, None
    try:
        body = p.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return p, None, None
    return p, parse_cache_header(body), body


def cache_identity_status(runner_path: str | Path) -> str:
    """Return a cache identity-freshness classification.

    Values are ``fresh``, ``missing``, ``corrupt``, ``sha_mismatch``, or
    ``input_mismatch``. ``fresh`` means the runner SHA matches and, when the
    runner declares mutable inputs, their fingerprint also matches.
    Caller is responsible for handling the missing-runner case (the runner
    file itself absent from disk — those runners shouldn't have caches).
    """
    p = REPO_ROOT / runner_path
    if not p.exists():
        return "fresh"  # nothing to check; runner is gone, ignore
    cache_p, header, _ = load_cache(runner_path)
    if not cache_p.exists():
        return "missing"
    if not header:
        return "corrupt"
    cur = runner_sha256(runner_path)
    if cur is None or header.get("runner_sha256") != cur:
        return "sha_mismatch"
    input_fp = declared_input_fingerprint(runner_path)
    if input_fp is not None and (
        not input_fp or header.get("input_fingerprint_sha256") != input_fp
    ):
        return "input_mismatch"
    return "fresh"


def cache_status(runner_path: str | Path) -> str:
    """Return whether a cache is both identity-fresh and execution-usable.

    Identity freshness and execution success are separate facts. Timeout,
    error, and nonzero-exit caches remain useful incident artifacts, but they
    must not satisfy audit readiness checks or be returned as evidence.
    """
    identity_status = cache_identity_status(runner_path)
    if identity_status != "fresh":
        return identity_status
    p = REPO_ROOT / runner_path
    if not p.exists():
        return "fresh"
    _cache_p, header, _body = load_cache(runner_path)
    if not header:
        return "corrupt"
    status = header.get("status")
    exit_code = header.get("exit_code")
    if status == "timeout":
        return "execution_timeout"
    if status != "ok":
        return "execution_error"
    if exit_code != "0":
        return "execution_nonzero_exit"
    return "fresh"


def stale_runners(runner_paths: Iterable[str]) -> list[tuple[str, str]]:
    """Return [(runner_path, reason)] for caches that need refreshing.
    Reason is one of 'missing' | 'corrupt' | 'sha_mismatch' |
    'input_mismatch' | 'execution_timeout' | 'execution_error' |
    'execution_nonzero_exit'.
    Runners absent from disk are excluded — orphan cache cleanup is a
    separate concern.
    """
    out: list[tuple[str, str]] = []
    for rp in runner_paths:
        s = cache_status(rp)
        if s != "fresh":
            out.append((rp, s))
    return out


def live_log_path_for(runner_path: str | Path) -> Path:
    """Path of the in-progress live log for a runner. Tail this during a
    precompute pass to watch a runner make progress mid-execution.
    """
    return LIVE_LOG_DIR / f"{Path(runner_path).stem}.txt"


def execute_runner(runner_path: str, timeout_sec: int) -> dict:
    """Run a single runner; return result dict with stdout/stderr/status.

    During execution the runner's stdout+stderr are streamed to a live
    log file at `logs/runner-cache/.in-progress/<stem>.txt` (gitignored)
    so an operator can `tail -f` any in-progress runner. The live log is
    cleaned up when the canonical cache file is written.
    """
    p = REPO_ROOT / runner_path
    if not p.exists():
        return {"runner": runner_path, "status": "missing", "exit_code": None,
                "stdout": "", "stderr": "", "elapsed_sec": 0.0,
                "timeout_sec": timeout_sec}
    LIVE_LOG_DIR.mkdir(parents=True, exist_ok=True)
    live_log = live_log_path_for(runner_path)
    t0 = time.time()
    status = "ok"
    exit_code: int | None = None

    # Write a header to the live log so a tail -F shows context.
    live_log.write_text(
        f"# in-progress live log for {runner_path}\n"
        f"# timeout_sec: {timeout_sec}\n"
        f"# started: {time.strftime('%Y-%m-%d %H:%M:%S %Z')}\n"
        f"# (this file is replaced by the canonical cache when the run completes)\n"
        f"\n",
        encoding="utf-8",
    )

    proc = None
    try:
        # Open the live log in append mode after the header so we can
        # see streaming output via tail -F. stderr is merged into stdout
        # to preserve interleaving.
        with live_log.open("a", encoding="utf-8") as live_fh:
            proc = subprocess.Popen(
                [sys.executable, "-u", str(p)],
                cwd=REPO_ROOT,
                stdout=live_fh,
                stderr=subprocess.STDOUT,
                env={**os.environ, "PYTHONPATH": str(REPO_ROOT / "scripts")},
            )
            try:
                exit_code = proc.wait(timeout=timeout_sec)
                if exit_code != 0:
                    status = "nonzero_exit"
            except subprocess.TimeoutExpired:
                status = "timeout"
                proc.kill()
                try:
                    proc.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    pass
                exit_code = proc.returncode
    except Exception as exc:
        status = "error"
        try:
            with live_log.open("a", encoding="utf-8") as live_fh:
                live_fh.write(f"\n[orchestrator caught: {exc!r}]\n")
        except OSError:
            pass

    elapsed = time.time() - t0
    # Read the live log tail back as the result body. The merged
    # stdout+stderr stream is what the audit prompt needs.
    try:
        body = live_log.read_text(encoding="utf-8", errors="replace")
    except OSError:
        body = ""
    # Strip our header (first 4 lines + blank) so the cache contains
    # only the runner's actual output.
    lines = body.split("\n", 5)
    stdout = lines[5] if len(lines) > 5 else ""

    return {
        "runner": runner_path,
        "status": status,
        "exit_code": exit_code,
        "stdout": stdout,
        "stderr": "",  # merged into stdout via STDOUT redirect
        "elapsed_sec": elapsed,
        "timeout_sec": timeout_sec,
        "live_log": str(live_log),
    }


def write_cache(
    runner_path: str,
    result: dict,
    runner_sha: str | None = None,
    *,
    identity: RunnerIdentity | None = None,
) -> Path:
    """Write the result of execute_runner to the canonical cache path.
    Pure function of captured runner/input identities plus execution result.

    Execution callers must pass the pre-run ``identity`` after comparing it to
    a post-run capture. Direct fixture/migration callers may omit it, in which
    case the current identity is captured at write time.
    """
    if identity is not None and runner_sha is not None:
        raise ValueError("pass identity or runner_sha, not both")
    if identity is None:
        captured = capture_runner_identity(runner_path)
        if captured is None:
            raise FileNotFoundError(f"runner missing on disk: {runner_path}")
        if runner_sha is not None:
            captured = RunnerIdentity(runner_sha, captured.input_fingerprint_sha256)
        identity = captured
    runner_sha = identity.runner_sha256
    input_fp = identity.input_fingerprint_sha256
    if not runner_sha:
        raise FileNotFoundError(f"runner missing on disk: {runner_path}")
    cache_p = cache_path_for(runner_path)
    cache_p.parent.mkdir(parents=True, exist_ok=True)

    stdout = result.get("stdout") or ""
    stderr = result.get("stderr") or ""
    stdout_tail = stdout[-200_000:]
    stderr_tail = stderr[-50_000:]
    elapsed = result.get("elapsed_sec") or 0.0
    body = (
        f"{CACHE_HEADER_PREFIX}\n"
        f"runner: {runner_path}\n"
        f"runner_sha256: {runner_sha}\n"
        + (f"input_fingerprint_sha256: {input_fp}\n" if input_fp else "")
        +
        f"timeout_sec: {result.get('timeout_sec')}\n"
        f"exit_code: {result.get('exit_code')}\n"
        f"elapsed_sec: {elapsed:.2f}\n"
        f"status: {result.get('status')}\n"
        f"----- stdout -----\n"
        f"{stdout_tail}\n"
        f"----- stderr -----\n"
        f"{stderr_tail}\n"
    )
    cache_p.write_text(body, encoding="utf-8")
    # Now that the canonical cache has the result, the in-progress live
    # log can go away. Best-effort cleanup; nothing depends on it.
    live = live_log_path_for(runner_path)
    try:
        if live.exists():
            live.unlink()
    except OSError:
        pass
    return cache_p


def execute_and_write_cache(
    runner_path: str, timeout_sec: int
) -> tuple[dict, Path | None]:
    """Execute once and cache only if pre/post execution identities agree.

    Content hashes bind the cache header. Filesystem-generation tokens close
    the ordinary ABA gap where a source is changed, read by the runner, and
    restored to its original bytes before the post-check. If a concurrent edit
    lands after the post-check but before the write, the pre-run content header
    is immediately stale; it cannot certify output against the new bytes.
    """
    before = capture_runner_execution_identity(runner_path)
    result = execute_runner(runner_path, timeout_sec=timeout_sec)
    if before is None or result.get("status") == "missing":
        return result, None
    after = capture_runner_execution_identity(runner_path)
    if after != before:
        live = live_log_path_for(runner_path)
        try:
            if live.exists():
                live.unlink()
        except OSError:
            pass
        raise RunnerIdentityChangedError(
            f"runner or declared input changed during execution: {runner_path}; "
            f"before={before!r}; after={after!r}"
        )
    return result, write_cache(runner_path, result, identity=before.content)


def cache_excerpt_for_audit(runner_path: str | Path,
                            tail_chars: int = 6000) -> str | None:
    """Return cache content suitable for the audit prompt's Section 3.
    Returns None if no cache exists or if the cache is stale.
    """
    p, header, body = load_cache(runner_path)
    if not (header and body):
        return None
    if cache_status(runner_path) != "fresh":
        return None
    clipped = len(body) > tail_chars
    excerpt = body[-tail_chars:] if clipped else body
    marker = (
        f"[runner cache excerpt clipped; {len(body)} chars total]\n"
        if clipped else ""
    )
    return (
        f"[runner cache hit: {p.name}, sha {header['runner_sha256'][:12]}]\n"
        f"{marker}{excerpt}"
    )
