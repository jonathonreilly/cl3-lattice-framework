#!/usr/bin/env python3
"""Execute corrected #7359-C Blocks 184--188 once under reviewed bounds."""

from __future__ import annotations

import ast
import hashlib
import json
import os
from pathlib import Path
import signal
import subprocess
import sys
import time
import traceback


WORKTREE = Path(
    "/Users/jonreilly/Projects/Physics-worktrees/fix-released7359-c-20260911"
)
sys.path.insert(0, str(WORKTREE / "scripts"))
import runner_cache as rc


HANDOFF = Path(__file__).resolve().parent
OUTPUT = HANDOFF.parent / "producer-01"
EXPECTED_HEAD = "08986aee8ae358cc05c8424d4e048aa7019f1231"
SOURCE_MAP_PATH = HANDOFF / "EXECUTION_SOURCE_INPUT_MAPS.json"
SOURCE_MAP_SHA256 = "660368c5b4e1704f1437fa9e5d687bc3fce88534a74e1dcfe9327feccf253490"
RUNS = ({'name': 'block184',
  'runner': 'scripts/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.py',
  'cache': 'logs/runner-cache/admissibility_dirac_kahler_temporal_link_extraction_2026_08_24.txt',
  'total': 'TOTAL: PASS=8 FAIL=0',
  'child': 120,
  'outer': 150,
  'identity': {'runner_sha256': '8d959d9b9e63c29ee020372ead5d035724f502e1bce413f38cc0c554f2d70618',
               'input_fingerprint_sha256': '06313f977c7c58f21c11e180f7d172db5dcaf910ef6cc9c7c4f6bce27f1c8c3d'}},
 {'name': 'block185',
  'runner': 'scripts/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.py',
  'cache': 'logs/runner-cache/admissibility_dirac_kahler_curved_os_seam_glued_gram_2026_08_24.txt',
  'total': 'TOTAL: PASS=8 FAIL=0',
  'child': 120,
  'outer': 150,
  'identity': {'runner_sha256': '635bbb6659c3f1ddde03c89d4f9fd564e0f1747dbb3bbaa2f97fe0b338511a60',
               'input_fingerprint_sha256': 'b98e42802fc687601347af6c9fc0acbcc6c81261a5f00b00efe6ee38f2d41952'}},
 {'name': 'block186',
  'runner': 'scripts/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.py',
  'cache': 'logs/runner-cache/admissibility_dirac_kahler_section_frame_inertia_wall_2026_08_24.txt',
  'total': 'TOTAL: PASS=8 FAIL=0',
  'child': 180,
  'outer': 220,
  'identity': {'runner_sha256': '693bd57dfe0c89ceaa4352165406584e3f1af0ae2bf4b22bc67951ed2fd8e3b4',
               'input_fingerprint_sha256': '50a7e1ccb6f93323d05eda627e69189675909aff0fb88591ffb17633ee587b86'}},
 {'name': 'block187',
  'runner': 'scripts/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.py',
  'cache': 'logs/runner-cache/admissibility_dirac_kahler_positivity_window_characterization_2026_08_24.txt',
  'total': 'TOTAL: PASS=8 FAIL=0',
  'child': 240,
  'outer': 300,
  'identity': {'runner_sha256': '27f497b89039f8ab9193e6744788417a84461114996c85ea62456984da2cd79b',
               'input_fingerprint_sha256': '7101bd5b351d4475db157a062d12b0463aa9457978be6701e8ba92db0cbdb16e'}},
 {'name': 'block188',
  'runner': 'scripts/admissibility_dirac_kahler_site_os_positivity_2026_08_24.py',
  'cache': 'logs/runner-cache/admissibility_dirac_kahler_site_os_positivity_2026_08_24.txt',
  'total': 'TOTAL: PASS=8 FAIL=0',
  'child': 180,
  'outer': 220,
  'identity': {'runner_sha256': '6bf440037e108bf7c0a7209d8344462f4838aff5d9d6efaac0939c06da91f5a4',
               'input_fingerprint_sha256': 'f5f8244cfc1e7c3517e93c20220f7bcae7aae4f004c17f3880f46ce02a1f099e'}})
RSS_LIMIT_BYTES = 2 * 1024**3


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def source_paths(runner: str) -> tuple[str, ...]:
    tree = ast.parse((WORKTREE / runner).read_text(encoding="utf-8"))
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        if any(
            isinstance(target, ast.Name) and target.id == "AUDIT_INPUT_PATHS"
            for target in node.targets
        ):
            inputs = ast.literal_eval(node.value)
            if not isinstance(inputs, tuple) or not all(
                isinstance(path, str) for path in inputs
            ):
                raise RuntimeError(
                    "AUDIT_INPUT_PATHS is not a literal tuple of strings"
                )
            return (runner, *inputs)
    raise RuntimeError(f"literal AUDIT_INPUT_PATHS absent: {runner}")


def hashes(paths: tuple[str, ...]) -> dict[str, str]:
    return {path: sha256(WORKTREE / path) for path in paths}


def process_group_rss_bytes(pgid: int) -> int:
    total = 0
    rows = subprocess.check_output(
        ["ps", "-axo", "pgid=,rss="], text=True
    ).splitlines()
    for row in rows:
        values = row.split()
        if len(values) == 2 and int(values[0]) == pgid:
            total += int(values[1]) * 1024
    return total


def execute(spec: dict, source_maps: dict) -> dict:
    result_dir = OUTPUT / spec["name"]
    result_dir.mkdir()
    runner = spec["runner"]
    paths = source_paths(runner)
    expected_map = source_maps[runner]
    if list(paths) != expected_map["paths"]:
        raise RuntimeError(f"literal input tuple changed: {runner}")
    before = hashes(paths)
    if before != expected_map["sha256"]:
        raise RuntimeError(f"source/input bytes differ from freeze: {runner}")
    (result_dir / "preexecution-inputs.json").write_text(
        json.dumps(before, indent=2) + "\n"
    )

    cache_path, old_header, old_text = rc.load_cache(runner)
    expected_cache_path = (WORKTREE / spec["cache"]).resolve()
    if cache_path.resolve() != expected_cache_path:
        raise RuntimeError(f"unexpected canonical cache path: {runner}")
    if cache_path.exists() or old_header is not None or old_text is not None:
        raise RuntimeError(f"canonical corrected cache already exists: {runner}")

    identity = rc.capture_runner_identity(runner)
    if identity is None or {
        "runner_sha256": identity.runner_sha256,
        "input_fingerprint_sha256": identity.input_fingerprint_sha256,
    } != spec["identity"]:
        raise RuntimeError(f"runner identity differs from freeze: {runner}")

    command = [
        "python3",
        "scripts/cached_runner_output.py",
        "--refresh",
        "--timeout-sec",
        str(spec["child"]),
        runner,
    ]
    environment = dict(
        os.environ,
        PYTHONDONTWRITEBYTECODE="1",
        OPENBLAS_NUM_THREADS="1",
        OMP_NUM_THREADS="1",
        MKL_NUM_THREADS="1",
    )
    started = time.monotonic()
    maximum_rss = 0
    resource_failure: str | None = None
    monitor_failure: str | None = None
    process: subprocess.Popen | None = None
    cli_exit_code: int | None = None
    with (result_dir / "execution.stdout").open("wb") as stdout, (
        result_dir / "execution.stderr"
    ).open("wb") as stderr:
        try:
            process = subprocess.Popen(
                command,
                cwd=WORKTREE,
                env=environment,
                stdout=stdout,
                stderr=stderr,
                start_new_session=True,
            )
            while process.poll() is None:
                try:
                    rss = process_group_rss_bytes(process.pid)
                except Exception as exc:
                    monitor_failure = f"{type(exc).__name__}: {exc}"
                    break
                maximum_rss = max(maximum_rss, rss)
                if time.monotonic() - started > spec["outer"]:
                    resource_failure = "wall_timeout"
                    break
                if rss > RSS_LIMIT_BYTES:
                    resource_failure = "process_group_rss_cap"
                    break
                time.sleep(0.1)
        finally:
            if process is not None and process.poll() is None:
                try:
                    os.killpg(process.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
            if process is not None:
                cli_exit_code = process.wait()

    after = hashes(paths)
    (result_dir / "postexecution-inputs.json").write_text(
        json.dumps(after, indent=2) + "\n"
    )
    cache_path, cache_header, cache_text = rc.load_cache(runner)
    cache_text = cache_text or ""
    post_identity = rc.capture_runner_identity(runner)
    cache_status = rc.cache_status(runner)
    cache_exists = cache_path.is_file()
    header_identity_matches = bool(
        cache_header
        and post_identity
        and cache_header.get("runner_path") == runner
        and cache_header.get("runner_sha256")
        == spec["identity"]["runner_sha256"]
        == post_identity.runner_sha256
        and cache_header.get("input_fingerprint_sha256")
        == spec["identity"]["input_fingerprint_sha256"]
        == post_identity.input_fingerprint_sha256
    )
    header_execution_ok = bool(
        cache_header
        and cache_header.get("status") == "ok"
        and cache_header.get("exit_code") == "0"
    )
    record = {
        "name": spec["name"],
        "command": command,
        "cwd": str(WORKTREE),
        "head": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=WORKTREE, text=True
        ).strip(),
        "elapsed_seconds": time.monotonic() - started,
        "wrapper_cli_exit_code": cli_exit_code,
        "resource_failure": resource_failure,
        "monitor_failure": monitor_failure,
        "max_process_group_rss_bytes": maximum_rss,
        "declared_runner_timeout_seconds": rc.runner_timeout_for(runner),
        "timeout_override_seconds": spec["child"],
        "outer_timeout_seconds": spec["outer"],
        "rss_limit_bytes": RSS_LIMIT_BYTES,
        "source_input_count": len(paths),
        "inputs_unchanged": before == after,
        "cache_path": spec["cache"],
        "cache_path_matches": cache_path.resolve() == expected_cache_path,
        "preexisting_cache": False,
        "forced_refresh": True,
        "cache_exists": cache_exists,
        "cache_sha256": sha256(cache_path) if cache_exists else None,
        "cache_header": cache_header,
        "expected_fresh_cache_identity": spec["identity"],
        "header_identity_matches": header_identity_matches,
        "header_execution_ok": header_execution_ok,
        "runner_cache_status": cache_status,
        "expected_total": spec["total"],
        "expected_total_present": spec["total"] in cache_text,
        "formal_audit": False,
        "automatic_retry": False,
    }
    (result_dir / "execution.json").write_text(
        json.dumps(record, indent=2) + "\n"
    )
    return record


def run_succeeded(record: dict) -> bool:
    return bool(
        record["head"] == EXPECTED_HEAD
        and record["wrapper_cli_exit_code"] == 0
        and record["resource_failure"] is None
        and record["monitor_failure"] is None
        and record["inputs_unchanged"]
        and record["cache_exists"]
        and record["cache_path_matches"]
        and record["header_identity_matches"]
        and record["header_execution_ok"]
        and record["runner_cache_status"] == "fresh"
        and record["expected_total_present"]
    )


def main() -> int:
    if OUTPUT.exists():
        raise RuntimeError(
            f"refusing automatic retry: output already exists: {OUTPUT}"
        )
    OUTPUT.mkdir()
    summary = {
        "automatic_retry": False,
        "formal_audit": False,
        "runs": [],
        "failure": None,
    }
    try:
        if sha256(SOURCE_MAP_PATH) != SOURCE_MAP_SHA256:
            raise RuntimeError("frozen source map changed")
        source_maps = json.loads(SOURCE_MAP_PATH.read_text())
        (WORKTREE / "logs/runner-cache/.in-progress").mkdir(
            parents=True, exist_ok=True
        )
        head = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=WORKTREE, text=True
        ).strip()
        if head != EXPECTED_HEAD:
            raise RuntimeError(f"unexpected worktree HEAD: {head}")
        cache_absence = {}
        for spec in RUNS:
            path = WORKTREE / spec["cache"]
            cache_absence[spec["cache"]] = not path.exists()
        (OUTPUT / "preexecution-cache-absence.json").write_text(
            json.dumps(cache_absence, indent=2) + "\n"
        )
        if not all(cache_absence.values()):
            raise RuntimeError("one or more corrected caches already exist")
        for spec in RUNS:
            record = execute(spec, source_maps)
            summary["runs"].append(record)
            if not run_succeeded(record):
                raise RuntimeError(
                    f"{spec['name']} did not satisfy its frozen producer gate"
                )
    except Exception as exc:
        summary["failure"] = {
            "type": type(exc).__name__,
            "message": str(exc),
            "traceback": traceback.format_exc(),
        }
    (OUTPUT / "SUMMARY.json").write_text(
        json.dumps(summary, indent=2) + "\n"
    )
    print(json.dumps(summary, indent=2))
    if summary["failure"] is not None:
        return 1
    print(
        "PASS corrected #7359-C Blocks 184--188; fresh cache headers and source identities verified"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
