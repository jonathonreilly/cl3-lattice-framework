#!/usr/bin/env python3
"""Dest=hop face plant occupies the HOLDING sandwich 3-cells.

Class-A finite integer check. No floats. No external solver.

Declared objects (all defined here):

  * Sites are Z^3. A unit cube is named by its min-corner (i,j,k) and has
    the eight vertices {i,i+1} x {j,j+1} x {k,k+1}.
  * L2 ball B_r = {p : p·p <= r^2}.
  * Geometric y=0 sandwich cubes in B_r: those unit cubes whose eight
    vertices lie in B_r and whose min-corner has y=0.
  * Curl grow: first-arrival BFS. From occupied p with dest L, a 6-NN step
    s is allowed when L x s is a signed axis; the new dest is L x s.
  * Inherit+perp grow: first-arrival BFS. A 6-NN step s is allowed when
    L · s = 0; the new dest is L (copied).
  * HOLDING seeds: four sites on the y=0 and y=1 planes with dests
    +e1, -e1, +e2, -e2 as written below.
  * dest=hop plant +e2: two seeds {(0,0,0): +e1, (0,1,0): +e2} grown by curl.

Checks, for r in {4,6,8} with grow radius r+4 (margin against ball cutoff):

  [A] dest=hop plant +e2 occupies exactly the geometric y=0 sandwich cubes
  [B] HOLDING inherit+perp occupies exactly those same cubes
  [C] dest=hop plant -e2 occupies exactly the geometric y=-1 sandwich
  [D] those two sandwiches are disjoint; face ±e2 is their union
  [E] dest=perpL plant +e1 dest=+e2 occupies exactly the geometric x=0 slab

At r=6 additionally:

  [F] occupancy *sets* of dest=hop +e2 and HOLDING inherit differ
  [G] every sandwich-cube vertex is occupied in both
  [H] dests on those vertices are not identical
  [I] 1-seed curl and dest=copy plant +e2 occupy no 8/8 cube in B_6

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
HOLDING = {
    (0, 0, 0): (1, 0, 0),
    (0, 1, 0): (-1, 0, 0),
    (0, 0, 1): (0, 1, 0),
    (0, 1, 1): (0, -1, 0),
}

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


def neg(a):
    return (-a[0], -a[1], -a[2])


def dot(a, b):
    return a[0] * b[0] + a[1] * b[1] + a[2] * b[2]


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


def grow_inherit_perp(seeds, r):
    formed = dict(seeds)
    q = deque(seeds.keys())
    while q:
        p = q.popleft()
        L = formed[p]
        for s in STEPS:
            if dot(L, s) != 0:
                continue
            v = add(p, s)
            if not in_ball(v, r):
                continue
            if v not in formed:
                formed[v] = L
                q.append(v)
    return formed


def cube_vertices(corner):
    i, j, k = corner
    return tuple(product((i, i + 1), (j, j + 1), (k, k + 1)))


def geometric_slab_cubes(r, axis, lo):
    """Unit cubes in B_r whose min-corner has coordinate `axis` equal to `lo`."""
    out = set()
    R = r + 1
    for corner in product(range(-R, R), repeat=3):
        if corner[axis] != lo:
            continue
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


def cube_vertex_set(corners):
    verts = set()
    for c in corners:
        verts.update(cube_vertices(c))
    return verts


def main() -> None:
    radii = (4, 6, 8)
    for r in radii:
        grow_r = r + 4
        geom_y0 = geometric_slab_cubes(r, 1, 0)
        geom_ym1 = geometric_slab_cubes(r, 1, -1)
        geom_x0 = geometric_slab_cubes(r, 0, 0)
        inh = grow_inherit_perp(HOLDING, grow_r)
        hop = grow_curl({ORIGIN: E1, E2: E2}, grow_r)
        hopm = grow_curl({ORIGIN: E1, neg(E2): neg(E2)}, grow_r)
        face = grow_curl({ORIGIN: E1, E2: E2, neg(E2): neg(E2)}, grow_r)
        perp = grow_curl({ORIGIN: E1, E1: E2}, grow_r)
        ci = occupied_cubes(inh, r)
        cp = occupied_cubes(hop, r)
        cm = occupied_cubes(hopm, r)
        cf = occupied_cubes(face, r)
        cx = occupied_cubes(perp, r)
        pr(
            f"r={r} |geom_y0|={len(geom_y0)} inherit={len(ci)} hop+e2={len(cp)} "
            f"hop-e2={len(cm)} face={len(cf)} perpL={len(cx)} geom_x0={len(geom_x0)}"
        )
        check(f"r={r} dest=hop +e2 cubes == geometric y=0 sandwich", cp == geom_y0)
        check(f"r={r} HOLDING inherit cubes == geometric y=0 sandwich", ci == geom_y0)
        check(f"r={r} dest=hop -e2 cubes == geometric y=-1 sandwich", cm == geom_ym1)
        check(f"r={r} y=0 and y=-1 sandwiches disjoint", not (geom_y0 & geom_ym1))
        check(f"r={r} face ±e2 cubes == disjoint union of ±e2 sandwiches", cf == geom_y0 | geom_ym1)
        check(f"r={r} dest=perpL cubes == geometric x=0 slab", cx == geom_x0)

    r = 6
    grow_r = r + 4
    inh = grow_inherit_perp(HOLDING, grow_r)
    hop = grow_curl({ORIGIN: E1, E2: E2}, grow_r)
    one = grow_curl({ORIGIN: E1}, grow_r)
    copy = grow_curl({ORIGIN: E1, E2: E1}, grow_r)
    geom_y0 = geometric_slab_cubes(r, 1, 0)
    verts = cube_vertex_set(geom_y0)
    check("r=6 dest=hop occupancy set != HOLDING inherit occupancy set", set(hop) != set(inh))
    check("r=6 every y=0 sandwich vertex occupied by dest=hop", all(v in hop for v in verts))
    check("r=6 every y=0 sandwich vertex occupied by HOLDING inherit", all(v in inh for v in verts))
    n_agree = sum(1 for v in verts if hop[v] == inh[v])
    pr(f"r=6 dest agree on sandwich vertices {n_agree}/{len(verts)}")
    check("r=6 dests on sandwich vertices are not identical", n_agree < len(verts))
    check("r=6 dests on sandwich vertices agree somewhere", n_agree > 0)
    check("r=6 1-seed curl occupies no 8/8 cube", occupied_cubes(one, r) == set())
    check("r=6 dest=copy plant +e2 occupies no 8/8 cube", occupied_cubes(copy, r) == set())

    pr(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
