#!/usr/bin/env python3
"""Sandwich 3-cells select dest ±hop at the already-occupied perp NN.

Class-A finite integer check. No floats.

One-seed curl from {(0,0,0): +e1} occupies +e2 with dest = e1 × e2 = +e3.
Overwrite dest at +e2 to each of the six signed axes, then continue curl
first-arrival grow. Score occupied 8-vertex cubes in B_r against the
geometric y=0 sandwich (min-corner y=0, all eight vertices in B_r).

Checks for r in {4,6,8}, grow radius r+4:

  [A] 1-seed occupies +e2; dest there is +e3; +e1 is vacant
  [B] overwrite dest=+e2 occupies exactly the y=0 sandwich cubes
  [C] overwrite dest=-e2 occupies exactly those same cubes
  [D] overwrite dest=±e1 or dest=±e3 occupies no 8/8 cube
  [E] +e2 and -e2 overwrite occupancy *sets* are equal
  [F] +e2 is not occupancy-extra vs 1-seed (dest overwrite, not a new site)

Prints one line per check; ends with TOTAL: PASS=N FAIL=0.
"""
from __future__ import annotations

from collections import deque
from itertools import product
import sys

AUDIT_TIMEOUT_SEC = 60

STEPS = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
ORIGIN = (0, 0, 0)
AXES = (E1, (-1, 0, 0), E2, (0, -1, 0), E3, (0, 0, -1))

PASS = 0
FAIL = 0


def pr(*a):
    sys.stdout.write(" ".join(str(x) for x in a) + "\n")
    sys.stdout.flush()


def check(label, ok):
    global PASS, FAIL
    if ok:
        PASS += 1
        pr(f"PASS {label}")
    else:
        FAIL += 1
        pr(f"FAIL {label}")


def add(a, b):
    return (a[0] + b[0], a[1] + b[1], a[2] + b[2])


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def is_axis(v):
    return sum(abs(x) for x in v) == 1


def in_ball(p, r):
    return p[0] * p[0] + p[1] * p[1] + p[2] * p[2] <= r * r


def grow_curl(seeds, r):
    formed = dict(seeds)
    q = deque(seeds.keys())
    while q:
        p = q.popleft()
        L = formed[p]
        for s in STEPS:
            Lp = cross(L, s)
            if not is_axis(Lp):
                continue
            v = add(p, s)
            if not in_ball(v, r):
                continue
            if v not in formed:
                formed[v] = Lp
                q.append(v)
    return formed


def cube_vertices(corner):
    i, j, k = corner
    return tuple(product((i, i + 1), (j, j + 1), (k, k + 1)))


def geometric_y0(r):
    out = set()
    R = r + 1
    for i, k in product(range(-R, R), repeat=2):
        corner = (i, 0, k)
        verts = cube_vertices(corner)
        if all(in_ball(v, r) for v in verts):
            out.add(corner)
    return out


def occupied_cubes(formed, r):
    out = set()
    R = r + 1
    for corner in product(range(-R, R), repeat=3):
        verts = cube_vertices(corner)
        if not all(in_ball(v, r) for v in verts):
            continue
        if all(v in formed for v in verts):
            out.add(corner)
    return out


def main() -> None:
    curl_at_e2 = cross(E1, E2)
    check("e1 × e2 is +e3", curl_at_e2 == E3)

    for r in (4, 6, 8):
        grow_r = r + 4
        one = grow_curl({ORIGIN: E1}, grow_r)
        check(f"r={r} 1-seed occupies +e2", E2 in one)
        check(f"r={r} 1-seed dest at +e2 is +e3", one.get(E2) == E3)
        check(f"r={r} 1-seed does not occupy +e1", E1 not in one)
        geom = geometric_y0(r)
        by_dest = {}
        for d in AXES:
            occ = grow_curl({ORIGIN: E1, E2: d}, grow_r)
            by_dest[d] = occ
            cubes = occupied_cubes(occ, r)
            fills = cubes == geom
            pr(
                f"r={r} overwrite dest={d} n8={len(cubes)} fills_y0={int(fills)}"
            )
            if d in (E2, (0, -1, 0)):
                check(f"r={r} overwrite dest={d} fills geometric y=0 sandwich", fills)
            else:
                check(f"r={r} overwrite dest={d} fills no 8/8 cube", cubes == set())
        occ_plus = by_dest[E2]
        occ_minus = by_dest[(0, -1, 0)]
        check(
            f"r={r} +hop and -hop overwrite occupancy sets equal",
            set(occ_plus) == set(occ_minus),
        )
        extra = set(occ_plus) - set(one)
        check(f"r={r} +e2 is not occupancy-extra vs 1-seed", E2 not in extra)

    pr(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
