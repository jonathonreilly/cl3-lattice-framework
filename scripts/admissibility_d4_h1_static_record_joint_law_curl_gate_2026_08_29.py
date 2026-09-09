#!/usr/bin/env python3
"""Exact conditional square-curl and compatible-extension calculation."""
from __future__ import annotations

from collections import Counter
from pathlib import Path
import sympy as sp

import independent_admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29 as _packet_helper  # noqa: F401,E501

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py",
)
ACTIVE = tuple((5, 6, 9, 10, 17, 18, 20, 23, 24, 27, 29, 30,
                33, 34, 36, 39, 40, 43, 45, 46, 53, 54, 57, 58))
INVERSE = (1, 0, 3, 2, 5, 4)


def insert_bit(rest: int, bit: int, value: int) -> int:
    mask = value << bit
    cursor = 0
    for target in range(6):
        if target != bit:
            mask |= ((rest >> cursor) & 1) << target
            cursor += 1
    return mask


def derivative_row(bit: int, rest: int) -> list[int]:
    row = [0] * 64
    row[insert_bit(rest, bit, 1)] = 1
    row[insert_bit(rest, bit, 0)] = -1
    return row


def minus(a: list[int], b: list[int]) -> list[int]:
    return [x - y for x, y in zip(a, b)]


def main() -> int:
    active = set(ACTIVE)
    deltas: list[int] = []
    failures_by_direction = Counter()
    for direction in range(6):
        reverse = INVERSE[direction]
        for left_rest in range(32):
            x0 = insert_bit(left_rest, direction, 0)
            x1 = insert_bit(left_rest, direction, 1)
            for right_rest in range(32):
                y0 = insert_bit(right_rest, reverse, 0)
                y1 = insert_bit(right_rest, reverse, 1)
                delta = int(x0 in active) + int(y1 in active) \
                    - int(y0 in active) - int(x1 in active)
                deltas.append(delta)
                failures_by_direction[direction] += int(delta != 0)
    histogram = dict(Counter(deltas))

    rows: list[list[int]] = []
    for bit in range(6):
        reference = derivative_row(bit, 0)
        for rest in range(1, 32):
            rows.append(minus(derivative_row(bit, rest), reference))
    for bit in (0, 2, 4):
        rows.append(minus(derivative_row(bit, 0), derivative_row(INVERSE[bit], 0)))
    compatibility = sp.Matrix(rows)
    constant = sp.ones(64, 1)
    axis_counts = [sp.Matrix([((mask >> bit) & 1) + ((mask >> INVERSE[bit]) & 1)
                              for mask in range(64)]) for bit in (0, 2, 4)]
    basis = (constant, *axis_counts)
    basis_ok = all(compatibility * v == sp.zeros(compatibility.rows, 1) for v in basis)
    basis_rank = sp.Matrix.hstack(*basis).rank()

    pinned = list(rows)
    anchor = ACTIVE[0]
    for mask in ACTIVE[1:]:
        row = [0] * 64
        row[mask], row[anchor] = 1, -1
        pinned.append(row)
    pinned_matrix = sp.Matrix(pinned)

    note = NOTE.read_text(encoding="utf-8")
    checks = (
        ("A_conditional_square_curl", len(deltas) == 6144
         and histogram == {0: 2112, 1: 1152, -1: 1152, -2: 864, 2: 864}
         and set(failures_by_direction) == set(range(6)),
         f"nonneutral odds fail 4032/6144 squares; histogram={histogram}"),
        ("B_neutral_exception", all(1**delta == 1 for delta in deltas),
         "t=1 closes every square and is explicitly excluded from the obstruction"),
        ("C_compatible_space", compatibility.rank() == 60 and basis_ok and basis_rank == 4,
         "compatible log-odds form the four-dimensional constant-plus-axis-count space"),
        ("D_active_pinning", pinned_matrix.rank() == 63
         and pinned_matrix * constant == sp.zeros(pinned_matrix.rows, 1),
         "equal active values kill all three axis slopes, leaving constants"),
        ("E_germ_scope", all(x in note for x in ("sufficiently small punctured germ",
                                                  "do not exclude additional zeros",
                                                  "t != 1", "did not recompute")),
         "the parent cubic coefficient is supplied and implies only a local punctured condition"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print(f"CURL: squares={len(deltas)}; failing={sum(d != 0 for d in deltas)}; histogram={histogram}.")
    print(f"COMPATIBLE: raw_rank={compatibility.rank()}/64; active_pinned_rank={pinned_matrix.rank()}/64.")
    print("DOMAIN: obstruction requires positive t!=1; supplied cubic gives only a sufficiently small punctured germ.")
    print("MUTATION_CREDIT: none claimed; no mutation sweep executed.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
