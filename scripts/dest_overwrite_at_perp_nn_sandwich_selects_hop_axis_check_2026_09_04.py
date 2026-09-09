#!/usr/bin/env python3
"""Finite fresh two-seed census, not overwrite-and-continuation.

Each candidate starts independently from {origin:+e1,+e2:d} for one of six
signed-axis destinations. The one-seed baseline is a separate run. FIFO seed
insertion order and STEPS order are supplied, with first-arrival assignment.
At scored radii 4,6,8 and grow radius r+4, only d=±e2 fills the geometric y=0
sandwich; both successful candidates occupy +e1, unlike the baseline. Their
occupancy sets agree. At r=6 each omits 413 completed-baseline sites.
No physical Record overwrite, formation law or rule uniqueness is claimed.
All arithmetic is integer and all science functions are inline.
"""
from __future__ import annotations

from collections import deque
from itertools import product
import sys

from pathlib import Path
import hashlib

AUDIT_INPUT_PATHS = ('docs/DEST_OVERWRITE_AT_PERP_NN_SANDWICH_SELECTS_HOP_AXIS_BOUNDED_THEOREM_NOTE_2026-09-04.md',)
EXPECTED_INPUT_SHA256 = {'docs/DEST_OVERWRITE_AT_PERP_NN_SANDWICH_SELECTS_HOP_AXIS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '1c413267e6c6ea627ba42a9bab56b205b4b92e53d0f81bf33941dba886f939b9'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    for rel, expected in EXPECTED_INPUT_SHA256.items():
        if hashlib.sha256((root / rel).read_bytes()).hexdigest() != expected:
            raise RuntimeError(f"scientific input changed: {rel}")
    print("INPUT_BINDING: exact companion note verified")

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
    verify_inputs()
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
                f"r={r} fresh second dest={d} n8={len(cubes)} fills_y0={int(fills)}"
            )
            if d in (E2, (0, -1, 0)):
                check(f"r={r} fresh second dest={d} fills geometric y=0 sandwich", fills)
            else:
                check(f"r={r} fresh second dest={d} fills no 8/8 cube", cubes == set())
        occ_plus = by_dest[E2]
        occ_minus = by_dest[(0, -1, 0)]
        check(
            f"r={r} fresh +hop and -hop occupancy sets equal",
            set(occ_plus) == set(occ_minus),
        )
        check(f"r={r} fresh +hop candidate occupies +e1 with dest -e1", occ_plus.get(E1) == (-1, 0, 0))
        check(f"r={r} fresh -hop candidate occupies +e1 with dest +e1", occ_minus.get(E1) == E1)
        if r == 6:
            lost_plus = len(set(one) - set(occ_plus))
            lost_minus = len(set(one) - set(occ_minus))
            pr(f"r=6 completed-baseline sites omitted by fresh candidates: plus={lost_plus} minus={lost_minus}")
            check("r=6 each fresh candidate omits 413 baseline sites, incompatible with no-erasure continuation",
                  lost_plus == 413 and lost_minus == 413)
        extra = set(occ_plus) - set(one)
        check(f"r={r} +e2 belongs to both fresh candidate and separate baseline", E2 not in extra)

    pr(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
