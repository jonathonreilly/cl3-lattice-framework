#!/usr/bin/env python3
"""Independent endpoint-path and axis-count control for Eta Block-05."""
from __future__ import annotations

from collections import Counter
import hashlib
from pathlib import Path
import re
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
PRIMARY = ROOT / "scripts/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py"
PRIMARY_CACHE = ROOT / "logs/runner-cache/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.txt"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.txt",
)
ACTIVE = {5, 6, 9, 10, 17, 18, 20, 23, 24, 27, 29, 30,
          33, 34, 36, 39, 40, 43, 45, 46, 53, 54, 57, 58}
INVERSE = (1, 0, 3, 2, 5, 4)


def insert(exterior: int, bit: int, value: int) -> int:
    answer = value << bit
    source = 0
    for target in range(6):
        if target != bit:
            answer |= ((exterior >> source) & 1) << target
            source += 1
    return answer


def cache_bound() -> bool:
    text = PRIMARY_CACHE.read_text(encoding="utf-8")
    digest = hashlib.sha256(PRIMARY.read_bytes()).hexdigest()
    match = re.search(r"^runner_sha256:\s*([0-9a-f]{64})$", text, re.M)
    return bool(match and match.group(1) == digest and "status: ok" in text
                and "TOTAL: PASS=5 FAIL=0" in text)


def main() -> int:
    histogram: Counter[int] = Counter()
    directions = set()
    for d in range(6):
        reverse = INVERSE[d]
        for left in range(32):
            for right in range(32):
                values = (insert(left, d, 0), insert(left, d, 1),
                          insert(right, reverse, 0), insert(right, reverse, 1))
                delta = int(values[0] in ACTIVE) + int(values[3] in ACTIVE) \
                    - int(values[2] in ACTIVE) - int(values[1] in ACTIVE)
                histogram[delta] += 1
                if delta:
                    directions.add(d)

    triples = sorted({tuple(((m >> b) & 1) + ((m >> INVERSE[b]) & 1)
                             for b in (0, 2, 4)) for m in ACTIVE})
    differences = sp.Matrix([[x - y for x, y in zip(row, triples[0])]
                             for row in triples[1:]])
    checks = (
        ("A_primary_identity", cache_bound(), "primary cache matches current source"),
        ("B_independent_path_census", dict(histogram) == {0: 2112, 1: 1152,
             -1: 1152, -2: 864, 2: 864} and directions == set(range(6)),
         f"independent endpoint insertion reproduces histogram {dict(histogram)}"),
        ("C_nonneutral_condition", all((sp.Rational(2)**d != 1) == (d != 0)
                                         for d in histogram),
         "an explicit positive nonneutral odds value fails exactly the nonzero-exponent squares"),
        ("D_axis_slope_elimination", len(triples) == 6 and differences.rank() == 3,
         f"six active axis-count triples have difference rank {differences.rank()}"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print(f"INDEPENDENT_CURL: histogram={dict(histogram)}; active_axis_classes={len(triples)}.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
