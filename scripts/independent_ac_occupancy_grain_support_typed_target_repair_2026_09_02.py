#!/usr/bin/env python3
"""Independent exact check for the Block51 support-typed target repair."""

from __future__ import annotations

import hashlib
from fractions import Fraction as F
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 120
# Populated with current own-note/source identity before the final freeze.
AUDIT_INPUT_PATHS = ('scripts/independent_ac_occupancy_grain_support_typed_target_repair_2026_09_02.py', 'docs/AC_OCCUPANCY_GRAIN_SUPPORT_TYPED_FORMAL_TARGET_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md')
EXPECTED_HASHES = {'docs/AC_OCCUPANCY_GRAIN_SUPPORT_TYPED_FORMAL_TARGET_REPAIR_BOUNDED_THEOREM_NOTE_2026-09-02.md': '44a9d2154373d8b4f74ba4e66a5159d285471132200c558d3329dcd1ab4c2393'}
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


def algebra_checks() -> list[tuple[str, bool]]:
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

    # Independently represented actual sign corruption and Jacobian omission.
    k = fixtures[0]
    valid = realification(k)
    bad = [row[:] for row in valid]
    for i in range(2):
        for j in range(2, 4):
            bad[i][j] = -bad[i][j]
    add("realification sign mutation detected", det4(valid) == 137 and det4(bad) == -121)
    zero = (0, 0)
    a = [[zero for _ in range(4)] for _ in range(4)]
    for i in range(2):
        for j in range(2):
            a[i][j + 2] = k[i][j]
            a[j + 2][i] = (-k[i][j][0], -k[i][j][1])
    def pf4(m):
        left = csub(cmul(m[0][1], m[2][3]), cmul(m[0][2], m[1][3]))
        right = cmul(m[0][3], m[1][2])
        return left[0] + right[0], left[1] + right[1]
    scales = (2, 1, 1, 1)
    changed = [[tuple(scales[i] * scales[j] * x for x in a[i][j]) for j in range(4)] for i in range(4)]
    original_pf = pf4(a)
    transformed_pf = pf4(changed)
    add("nonunit Jacobian cancellation", transformed_pf == tuple(2 * x for x in original_pf))
    add("omitted Jacobian detected", csub(transformed_pf, original_pf) == (4, -11))
    for nu, q in (((2, 3), (0, 0)), ((2, 3), (1, 0)), ((2, 3), (0, 1))):
        diff = F(nu[1] + q[1], 2 * (nu[0] + q[0])) - F(nu[1], 2 * nu[0])
        add(f"support boundary {q}", (diff == 0) if q == (0, 0) else (diff < 0 if q[1] == 0 else diff > 0))
    return tests


def source_bound() -> bool:
    return all((ROOT / p).is_file() for p in AUDIT_INPUT_PATHS) and all(hashlib.sha256((ROOT / p).read_bytes()).hexdigest() == h for p, h in EXPECTED_HASHES.items())


def main() -> int:
    tests = [("current source/own-note binding", source_bound()), *algebra_checks()]
    for name, ok in tests:
        print(f"CHECK {name}: {'PASS' if ok else 'FAIL'}")
    failed = sum(not ok for _, ok in tests)
    print(f"TOTAL: PASS={len(tests)-failed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
