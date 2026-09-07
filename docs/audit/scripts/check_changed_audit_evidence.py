#!/usr/bin/env python3
"""Review-time evidence-readiness gate for changed scientific surfaces.

Run after the audit pipeline.  It maps the branch diff to ledger rows and
fails when a changed source/runner/helper is mechanically incapable of
supplying the forensic packet expected after merge.  This is not an audit and
never grants a verdict: the audit lane re-executes the runner live.
"""
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path

import forensic_evidence_readiness
import ledger_io


REPO_ROOT = Path(__file__).resolve().parents[3]
LEDGER_PATH = REPO_ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
LEGACY_EPOCH_BASELINE_PATH = (
    "docs/audit/data/legacy_science_epoch_baseline.json"
)


def _git(*args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=REPO_ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip())
    return proc.stdout


def merge_base_commit(base: str) -> str:
    merge_base = _git("merge-base", base, "HEAD").strip()
    if not merge_base:
        raise RuntimeError(f"cannot resolve merge-base against {base}")
    return merge_base


def changed_paths(base: str, *, include_worktree: bool = False) -> set[str]:
    merge_base = merge_base_commit(base)
    commands = [("diff", "--no-renames", "--name-only", "-z", f"{merge_base}...HEAD")]
    if include_worktree:
        # Review includes the index and working copy separately: an unstaged
        # reversal must not hide a staged change from the evidence gate.
        commands.extend([
            ("diff", "--cached", "--no-renames", "--name-only", "-z", "HEAD"),
            ("diff", "--no-renames", "--name-only", "-z"),
            ("ls-files", "--others", "--exclude-standard", "-z"),
        ])
    return {path for command in commands for path in _git(*command).split("\0") if path}


def immutable_control_failures(base: str, paths: set[str]) -> list[dict]:
    """Reject edits to a deployed one-time baseline, while allowing bootstrap."""
    if LEGACY_EPOCH_BASELINE_PATH not in paths:
        return []
    merge_base = merge_base_commit(base)
    existed_at_base = LEGACY_EPOCH_BASELINE_PATH in {
        line.strip()
        for line in _git(
            "ls-tree",
            "--name-only",
            merge_base,
            "--",
            LEGACY_EPOCH_BASELINE_PATH,
        ).splitlines()
        if line.strip()
    }
    if not existed_at_base:
        return []
    return [{
        "control": "immutable_legacy_science_epoch_baseline",
        "changed_surfaces": [LEGACY_EPOCH_BASELINE_PATH],
        "issue": (
            "legacy_science_epoch_baseline_is_immutable_after_deployment; "
            "do not refresh it to absorb premise or dependency-policy drift"
        ),
    }]


def candidate_version_conflicts() -> list[dict]:
    """Do not certify index bytes using a different working-copy version."""
    staged = set(filter(None, _git(
        "diff", "--cached", "--no-renames", "--name-only", "-z", "HEAD"
    ).split("\0")))
    unstaged = set(filter(None, _git(
        "diff", "--no-renames", "--name-only", "-z"
    ).split("\0")))
    # A staged deletion followed by file recreation is untracked, not an
    # index-to-worktree diff. Those bytes also cannot certify the index.
    unstaged.update(filter(None, _git(
        "ls-files", "--others", "--exclude-standard", "-z"
    ).split("\0")))
    for path in filter(None, _git(
        "diff", "--cached", "--no-renames", "--diff-filter=D", "--name-only", "-z", "HEAD"
    ).split("\0")):
        # Recreated ignored files are absent even from ls-files --others.
        target = REPO_ROOT / path
        if target.exists() or target.is_symlink():
            unstaged.add(path)
    ambiguous = sorted(staged & unstaged)
    if not ambiguous:
        return []
    return [{
        "control": "mixed_candidate_versions",
        "changed_surfaces": ambiguous,
        "issue": (
            "paths_have_conflicting_staged_and_working_versions; readiness reads working-copy "
            "bytes, not a different index version. Stage the intended bytes or unstage "
            "these paths for working-copy review, then rerun the gate"
        ),
    }]


def affected_rows(
    rows: dict[str, dict],
    paths: set[str],
) -> list[tuple[str, dict, list[str]]]:
    affected: list[tuple[str, dict, list[str]]] = []
    for claim_id, row in rows.items():
        surfaces = {
            str(row.get("note_path") or ""),
            str(row.get("runner_path") or ""),
            *(str(path) for path in row.get("helper_runner_paths") or []),
        }
        overlap = sorted((surfaces - {""}) & paths)
        if not overlap:
            continue
        claim_type = row.get("claim_type") or row.get("claim_type_author_hint")
        if claim_type in {"meta", "open_gate", "decoration"}:
            continue
        affected.append((claim_id, row, overlap))
    return affected


def build_report(base: str, *, include_worktree: bool = False) -> dict:
    ledger_io.ensure_cache()
    ledger = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    rows = ledger.get("rows") or {}
    paths = changed_paths(base, include_worktree=include_worktree)
    control_failures = immutable_control_failures(base, paths)
    if include_worktree:
        control_failures.extend(candidate_version_conflicts())
    checked: list[dict] = []
    failures: list[dict] = []
    for claim_id, row, overlap in affected_rows(rows, paths):
        issue = forensic_evidence_readiness.cached_row_readiness_issue(
            {**row, "claim_id": claim_id},
            rows,
            REPO_ROOT,
        )
        record = {
            "claim_id": claim_id,
            "changed_surfaces": overlap,
            "runner_path": row.get("runner_path"),
            "helper_runner_paths": list(row.get("helper_runner_paths") or []),
            "forensic_evidence_ready": issue is None,
            "issue": issue,
        }
        checked.append(record)
        if issue is not None:
            failures.append(record)
    return {
        "schema": "changed_audit_evidence_readiness_v1",
        "base": base,
        "diff_scope": "committed_and_worktree" if include_worktree else "committed",
        "changed_path_count": len(paths),
        "checked": checked,
        "failures": failures,
        "control_failures": control_failures,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="origin/main")
    parser.add_argument(
        "--include-worktree", action="store_true",
        help="Also inspect staged, unstaged, and untracked candidate changes (use before committing or with --no-commit review).",
    )
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = build_report(args.base, include_worktree=args.include_worktree)
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"changed-audit-evidence: ERROR: {exc}")
        return 2
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
    else:
        print(
            "changed-audit-evidence: "
            f"checked={len(report['checked'])} "
            f"failures={len(report['failures'])} "
            f"control_failures={len(report['control_failures'])}"
        )
        for failure in report["failures"]:
            print(f"  {failure['claim_id']}: {failure['issue']}")
        for failure in report["control_failures"]:
            print(f"  {failure['control']}: {failure['issue']}")
    return 1 if report["failures"] or report["control_failures"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
