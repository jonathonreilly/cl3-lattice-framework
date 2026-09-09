#!/usr/bin/env python3
"""Independent exact check for the Block51 support-typed target repair."""

from __future__ import annotations

import hashlib
import json
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TARGET_ROW = ROOT / "docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json"
EXPECTED_OBLIGATION_HASH = "bd91c0496a51334fa7f7b4ab7a84f87b1575103b1398873d77fe260ffd6aef63"
AUDIT_INPUT_PATHS = (
    "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md",
    "docs/audit/data/ledger/ac/ac_orbit_occupancy_statistical_grain_derivation_obligation.json",
)
GaussianInteger = tuple[int, int]
Matrix2 = tuple[
    tuple[GaussianInteger, GaussianInteger],
    tuple[GaussianInteger, GaussianInteger],
]


def cmul(a: GaussianInteger, b: GaussianInteger) -> GaussianInteger:
    return a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def csub(a: GaussianInteger, b: GaussianInteger) -> GaussianInteger:
    return a[0] - b[0], a[1] - b[1]


def det2(a: Matrix2) -> GaussianInteger:
    return csub(cmul(a[0][0], a[1][1]), cmul(a[0][1], a[1][0]))


def det4(m: list[list[int]]) -> int:
    total = 0
    for p in ((0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1),
              (0, 3, 1, 2), (0, 3, 2, 1), (1, 0, 2, 3), (1, 0, 3, 2),
              (1, 2, 0, 3), (1, 2, 3, 0), (1, 3, 0, 2), (1, 3, 2, 0),
              (2, 0, 1, 3), (2, 0, 3, 1), (2, 1, 0, 3), (2, 1, 3, 0),
              (2, 3, 0, 1), (2, 3, 1, 0), (3, 0, 1, 2), (3, 0, 2, 1),
              (3, 1, 0, 2), (3, 1, 2, 0), (3, 2, 0, 1), (3, 2, 1, 0)):
        inv = sum(p[i] > p[j] for i in range(4) for j in range(i + 1, 4))
        prod = 1
        for i, j in enumerate(p):
            prod *= m[i][j]
        total += (-1 if inv % 2 else 1) * prod
    return total


def realification(k: Matrix2) -> list[list[int]]:
    x = [[z[0] for z in row] for row in k]
    y = [[z[1] for z in row] for row in k]
    return [x[0] + [-v for v in y[0]], x[1] + [-v for v in y[1]],
            y[0] + x[0], y[1] + x[1]]


def main() -> int:
    tests: list[tuple[str, bool]] = []
    add = lambda name, value: tests.append((name, bool(value)))

    # Burnside/orbit computation by direct closure.
    action = {0: 0, 1: 2, 2: 1}
    orbits = {frozenset((x, action[x])) for x in action}
    add("orbit census", len(orbits) == 2 and sum(action[x] == x for x in action) == 1)

    def projective(v: tuple[int, int]) -> F:
        return F(v[1], v[0])

    add("global power neutral", projective((1, 2)) == projective((2, 4)))
    add("sector-local copy active", projective((1, 1)) != projective((1, 2)))
    for nu, q in (((1, 1), (1, 1)), ((2, 3), (4, 6)), ((1, 1), (0, 1))):
        lhs = F(nu[1] + q[1], 2 * (nu[0] + q[0])) - F(nu[1], 2 * nu[0])
        rhs = F(nu[0] * q[1] - nu[1] * q[0], 2 * nu[0] * (nu[0] + q[0]))
        add(f"increment identity {nu} {q}", lhs == rhs)

    fixtures: tuple[Matrix2, ...] = (
        (((1, 2), (3, -1)), ((2, 0), (4, 1))),
        (((2, 0), (0, 1)), ((1, -1), (3, 0))),
    )
    for k in fixtures:
        dc_re, dc_im = det2(k)
        add("exact Gaussian-integer realification",
            det4(realification(k)) == dc_re * dc_re + dc_im * dc_im)

    def odds(power: int, x: F) -> F:
        p = x ** power / (1 + x ** power)
        return p / (1 - p)

    add("odds exponent one", odds(1, F(4)) / odds(1, F(2)) == 2)
    add("odds exponent two", odds(2, F(4)) / odds(2, F(2)) == 4)

    obligation = ROOT / "docs/AC_ORBIT_OCCUPANCY_STATISTICAL_GRAIN_DERIVATION_OBLIGATION.md"
    add("obligation source pinned", hashlib.sha256(obligation.read_bytes()).hexdigest() == EXPECTED_OBLIGATION_HASH)
    row = json.loads(TARGET_ROW.read_text())
    add("live gate open", row["claim_type"] == "open_gate" and row["chain_closes"] is None)
    add("blast radius", row["direct_in_degree"] == 16 and row["transitive_descendants"] == 108)

    failed = [(n, ok) for n, ok in tests if not ok]
    for name, _ in failed:
        print(f"FAIL {name}")
    print(f"TOTAL: PASS={len(tests)-len(failed)} FAIL={len(failed)}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
