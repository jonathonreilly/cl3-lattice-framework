#!/usr/bin/env python3
"""Kill every preregistered Block52 mutation against the primary runner."""

from __future__ import annotations

import re
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMARY = ROOT / "scripts/reta_c3_source_response_spectral_identity_2026_09_02.py"
AUDIT_INPUT_PATHS = (
    "scripts/reta_c3_source_response_spectral_identity_2026_09_02.py",
    "docs/AC_RETA_C3_SOURCE_RESPONSE_SPECTRAL_IDENTITY_TYPE_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md",
)


def main() -> int:
    listed = subprocess.run(
        [sys.executable, str(PRIMARY), "--list-mutations"],
        cwd=ROOT, check=True, text=True, capture_output=True,
    ).stdout.splitlines()
    def execute(mutation: str) -> tuple[str, bool]:
        run = subprocess.run(
            [sys.executable, str(PRIMARY), "--mutation", mutation],
            cwd=ROOT, text=True, capture_output=True,
        )
        totals = re.findall(r"TOTAL: PASS=(\d+) FAIL=(\d+)", run.stdout)
        killed = run.returncode != 0 and len(totals) == 1 and int(totals[0][1]) >= 1
        return mutation, killed

    with ThreadPoolExecutor(max_workers=4) as pool:
        outcomes = list(pool.map(execute, listed))

    passed = 0
    failures: list[str] = []
    for mutation, killed in outcomes:
        print(f"{'PASS' if killed else 'FAIL'} mutation={mutation}")
        if killed:
            passed += 1
        else:
            failures.append(mutation)
    failed = len(listed) - passed
    if failures:
        print("SURVIVORS=" + ",".join(failures))
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
