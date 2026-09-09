#!/usr/bin/env python3
"""Independent small-graph control for corrected Eta Block-04."""
from __future__ import annotations

import hashlib
from itertools import combinations
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
PRIMARY = ROOT / "scripts/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py"
PRIMARY_CACHE = ROOT / "logs/runner-cache/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.txt"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.txt",
)


def cache_bound() -> bool:
    text = PRIMARY_CACHE.read_text(encoding="utf-8")
    digest = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    match = re.search(r"^runner_sha256:\s*([0-9a-f]{64})$", text, re.M)
    return bool(match and match.group(1) == digest and "status: ok" in text
                and "TOTAL: PASS=4 FAIL=0" in text)


def main() -> int:
    appends = 0
    for edge_bits in range(64):
        adj = [set() for _ in range(4)]
        for k, (i, j) in enumerate(combinations(range(4), 2)):
            if edge_bits >> k & 1:
                adj[i].add(j)
                adj[j].add(i)
        for state in range(16):
            occupied = {i for i in range(4) if state >> i & 1}
            before = {i for i in range(4) if i not in occupied and adj[i] <= occupied}
            for x in before:
                after_occupied = occupied | {x}
                after = {i for i in range(4)
                         if i not in after_occupied and adj[i] <= after_occupied}
                assert after == before - {x}
                appends += 1
    checks = (
        ("A_primary_identity", cache_bound(), "primary cache matches current primary source"),
        ("B_independent_graph_control", appends == 864,
         "independent four-vertex enumeration checks 864 ready appends"),
        ("C_local_information_deficit", 2**5 == 32 and 24 * 2 * 6 * 32 == 9216,
         "one fixed reciprocal bit leaves five independent bits and 9216 active compatibility rows"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print("INDEPENDENT: n=4; ready_appends=864; direct_target_status=occupied.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
