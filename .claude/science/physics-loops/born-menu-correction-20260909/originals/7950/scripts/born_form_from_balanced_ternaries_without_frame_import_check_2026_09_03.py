#!/usr/bin/env python3
"""Exact rational checks for the balanced-ternary Born note without the frame import.

Class A throughout: every printed check is an algebraic identity or an exact rank and
kernel certificate computed over `Q` from declared inputs; nothing is compared against
an external number and nothing is sampled.  No floating point, no seed, no numpy and
no sympy.  Two blocks are copied from the source computation `b5_exact.py` of the
probe this note lands:

  * `rref_nullspace` reproduces the source's exact elimination over `Q`
    (`b5_exact.py:23-52`, the block cited as `rref_nullspace :23`): reduced row
    echelon form with rational pivots and an explicit nullspace basis.
  * `mode_rows` reproduces the source's angle-mode row builder (`b5_exact.py:192-219`,
    the block cited as `mode_rows :192`): per perimeter-2 grid triangle the real and
    imaginary parts of `sum_i h_k(c_i) e^{i k alpha_i} = 0` in Chebyshev form, plus
    the collinear-ternary and mixed-coin rows that separate `M_all` from `M_CONT`.

The helpers `pyth_pairs`, `balanced_weights2`, `cs_k`, `cheb_T` and `cheb_U`
reproduce the source's rational-grid and trigonometric blocks (`b5_exact.py:54-79`
and `:181-190`).  The dimension-three frame-function theorem is neither used nor
recomputed here: the parent note's import is read as text only, to quote it.
Recorded arguments print with an `ARG:` prefix and are excluded from the total.
"""

import re
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "THE_BORN_FORM_FROM_BALANCED_TERNARY_MENUS_WITHOUT_THE_FRAME_IMPORT_EXACT_FOR_"
    "HOMOGENEOUS_GRADINGS_AND_A_COUNTING_ROGUE_ON_THE_REALISED_FAMILY_BOUNDED_"
    "THEOREM_NOTE_2026-09-03.md"
)
PARENT_PATH = ROOT / "docs" / (
    "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_"
    "NOTE_2026-08-09.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THE_BORN_FORM_FROM_BALANCED_TERNARY_MENUS_WITHOUT_THE_FRAME_IMPORT_EXACT"
    "_FOR_HOMOGENEOUS_GRADINGS_AND_A_COUNTING_ROGUE_ON_THE_REALISED_FAMILY_BOUNDED"
    "_THEOREM_NOTE_2026-09-03.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM"
    "_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text):
    """Whitespace-collapse; markdown blockquote markers are stripped first, so a
    sentence quoted across wrapped `>` lines matches its source verbatim."""
    unquoted = "\n".join(re.sub(r"^\s*>\s?", "", ln) for ln in text.split("\n"))
    return " ".join(unquoted.split())


class Checks:
    """Machine verifications count; recorded arguments print and never count."""

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.arguments = 0

    def check(self, label, statement, condition):
        ok = bool(condition)
        if ok:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if ok else 'FAIL'}: {label} {statement}")

    def note(self, label, statement):
        self.arguments += 1
        print(f"ARG: {label} {statement}")

    def finish(self):
        print(f"recorded_arguments: {self.arguments} printed, none counted")
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


# ------------------------------------------------------- exact elimination over Q
# copy of b5_exact.py:23-52 (`rref_nullspace :23`)
def rref_nullspace(rows, ncols):
    """rows: list of lists of Fractions. Returns (rank, nullspace basis)."""
    piv_rows = []
    piv_cols = []
    for r in rows:
        r = [F(x) for x in r]
        for pr, pc in zip(piv_rows, piv_cols):
            if r[pc] != 0:
                f = r[pc]
                r = [a - f * b for a, b in zip(r, pr)]
        pc = next((j for j in range(ncols) if r[j] != 0), None)
        if pc is None:
            continue
        f = r[pc]
        r = [a / f for a in r]
        for i in range(len(piv_rows)):
            if piv_rows[i][pc] != 0:
                g = piv_rows[i][pc]
                piv_rows[i] = [a - g * b for a, b in zip(piv_rows[i], r)]
        piv_rows.append(r)
        piv_cols.append(pc)
        if len(piv_rows) == ncols:
            break
    rank = len(piv_rows)
    free = [j for j in range(ncols) if j not in piv_cols]
    basis = []
    for fcol in free:
        v = [F(0)] * ncols
        v[fcol] = F(1)
        for pr, pc in zip(piv_rows, piv_cols):
            v[pc] = -pr[fcol]
        basis.append(v)
    return rank, basis


# ------------------------------------------------------- rational grids (b5_exact.py:54-79)
def pyth_pairs(maxmn):
    pts = set()
    for m in range(1, maxmn + 1):
        for n in range(0, m):
            d = m * m + n * n
            c, s = F(m * m - n * n, d), F(2 * m * n, d)
            for (a, b) in [(c, s), (s, c)]:
                for sa in (1, -1):
                    for sb in (1, -1):
                        pts.add((sa * a, sb * b))
    return sorted(pts)


def cross2(u, v):
    return u[0] * v[1] - u[1] * v[0]


def dot(u, v):
    return sum(a * b for a, b in zip(u, v))


def balanced_weights2(n1, n2, n3):
    p = [cross2(n2, n3), cross2(n3, n1), cross2(n1, n2)]
    if all(x > 0 for x in p) or all(x < 0 for x in p):
        s = sum(p)
        return [x / s for x in p]
    return None


def cs_k(c, s, k):
    re, im = F(1), F(0)
    for _ in range(k):
        re, im = re * c - im * s, re * s + im * c
    return re, im


def cheb_T(k, x):
    a, b = F(1), x
    if k == 0:
        return a
    for _ in range(k - 1):
        a, b = b, 2 * x * b - a
    return b


def cheb_U(k, x):
    a, b = F(1), 2 * x
    if k == 0:
        return a
    for _ in range(k - 1):
        a, b = b, 2 * x * b - a
    return b


# ------------------------------------------------------- copy of b5_exact.py:192-219 (`mode_rows :192`)
def mode_rows(k, grid, with_all):
    idx = {c: i for i, c in enumerate(grid)}
    n = len(grid)
    rows = []
    ntri = 0
    interior = [c for c in grid if c < 1]
    for s1, s2 in combinations(interior, 2):
        s3 = 2 - s1 - s2
        if s3 not in idx or not (0 < s3 < 1) or s3 < s2:
            continue
        ntri += 1
        cosA3 = (s1 * s1 + s2 * s2 - s3 * s3) / (2 * s1 * s2)
        cosA2 = (s1 * s1 + s3 * s3 - s2 * s2) / (2 * s1 * s3)
        sA3, sA2 = 2 / (s1 * s2), 2 / (s1 * s3)
        if k == 0:
            r = [F(0)] * n
            r[idx[s1]] += 1
            r[idx[s2]] += 1
            r[idx[s3]] += 1
            rows.append(r)
        else:
            re = [F(0)] * n
            im = [F(0)] * n
            re[idx[s1]] += 1
            re[idx[s2]] += -cheb_T(k, cosA3)
            re[idx[s3]] += -cheb_T(k, cosA2)
            im[idx[s2]] += sA3 * cheb_U(k - 1, cosA3)
            im[idx[s3]] += -sA2 * cheb_U(k - 1, cosA2)
            rows.append(re)
            rows.append(im)
    if with_all:
        for a in grid:
            if a < 1 and (1 - a) in idx:
                r = [F(0)] * n
                r[idx[a]] += 1
                r[idx[1 - a]] += 1
                r[idx[F(1)]] += -1
                rows.append(r)
        if k % 2 == 0:
            for c in grid:
                r = [F(0)] * n
                r[idx[c]] += 2
                rows.append(r)
    return rows, ntri


# ------------------------------------------------------- shared declared data
PTS5 = pyth_pairs(5)
PTS6 = pyth_pairs(6)
PTS4 = pyth_pairs(4)
FRAMES = [
    [(F(1), F(0), F(0)), (F(0), F(1), F(0)), (F(0), F(0), F(1))],
    [(F(2, 3), F(2, 3), F(-1, 3)), (F(2, 3), F(-1, 3), F(2, 3)), (F(-1, 3), F(2, 3), F(2, 3))],
    [(F(2, 7), F(3, 7), F(6, 7)), (F(3, 7), F(-6, 7), F(2, 7)), (F(6, 7), F(2, 7), F(-3, 7))],
    [(F(1, 9), F(4, 9), F(8, 9)), (F(4, 9), F(7, 9), F(-4, 9)), (F(8, 9), F(-4, 9), F(1, 9))],
]
GRID = [F(j, 24) for j in range(1, 25)]


def balanced_triples(points):
    out = []
    for n1, n2, n3 in combinations(points, 3):
        p = balanced_weights2(n1, n2, n3)
        if p is not None:
            out.append(((n1, n2, n3), p))
    return out


# ------------------------------------------------------- T1 the dictionary
def t1(checks, trips):
    checks.check("T1-grid", "52 rational unit directions, each exactly on the circle",
                 len(PTS5) == 52 and all(a * a + b * b == 1 for a, b in PTS5))
    checks.check("T1-count", "5200 non-collinear balanced ternaries on that grid",
                 len(trips) == 5200)
    res = all(sum(2 * x for x in p) == 2
              and all(sum(2 * x * ni[j] for x, ni in zip(p, ns)) == 0 for j in (0, 1))
              for ns, p in trips)
    checks.check("T1-resolution", "each has sum c_i = 2 and sum c_i n_i = 0, so sum c_i P(n_i) = I",
                 res)
    per = all(sum(2 * x for x in p) == 2 for ns, p in trips)
    checks.check("T1-perimeter", "the sides v_i = c_i n_i close a triangle of perimeter 2",
                 per)
    cs = [2 * x for ns, p in trips for x in p]
    checks.check("T1-interior", "every weight is in (1/21, 696/697), so c_i <= 1 is automatic",
                 min(cs) == F(1, 21) and max(cs) == F(696, 697) and all(0 < c < 1 for c in cs))
    strict = all(dot(a, b) < 1 for a, b in combinations(PTS5, 2))
    checks.check("T1-strict", "|c2 n2 + c3 n3| < c2 + c3 unless n2 = n3, on all 1326 grid pairs",
                 strict and len(list(combinations(PTS5, 2))) == 1326)
    checks.check("T1-no-projector", "no non-collinear balanced ternary contains a projector",
                 all(c != 1 for c in cs))
    checks.note("T1-degenerate", "a side of length 1 forces the other two to sum to 1, hence n2 = n3")


# ------------------------------------------------------- T2 Theorem A
def t2(checks, trips):
    checks.check("T2-lemma1-pairs", "no two members of a balanced triple are antipodal",
                 all(cross2(ns[i], ns[j]) != 0 for ns, p in trips for i, j in ((0, 1), (0, 2), (1, 2))))
    idx = {n: i for i, n in enumerate(PTS5)}
    rows = []
    for ns, p in trips:
        r = [F(0)] * len(PTS5)
        for ni, pi in zip(ns, p):
            r[idx[ni]] += pi
        rows.append(r)
    rk, ker = rref_nullspace(rows, len(PTS5))
    checks.check("T2-circle-free", "52 free values, 5200 rows, rank 50, nullity 2: no truncation",
                 rk == 50 and len(ker) == 2)
    xs = [n[0] for n in PTS5]
    ys = [n[1] for n in PTS5]
    joint, _ = rref_nullspace([xs, ys] + [list(v) for v in ker], len(PTS5))
    checks.check("T2-circle-free-kernel", "that kernel is exactly the restriction of span{x, y}",
                 joint == 2)
    rows = []
    ntrip = 0
    for ns, p in balanced_triples(PTS6):
        row = [F(0)] * 17
        for ni, pi in zip(ns, p):
            row[0] += pi
            for k in range(1, 9):
                ck, sk = cs_k(ni[0], ni[1], k)
                row[2 * k - 1] += pi * ck
                row[2 * k] += pi * sk
        rows.append(row)
        ntrip += 1
        if ntrip >= 400:
            break
    rk, ker = rref_nullspace(rows, 17)
    checks.check("T2-circle-modes", "modes 0..8, 17 unknowns, 400 triples, rank 15, nullity 2",
                 ntrip == 400 and rk == 15 and len(ker) == 2)
    nz = sorted(i for v in ker for i in range(17) if v[i] != 0)
    checks.check("T2-circle-kernel", "that kernel is exactly {cos t, sin t}", nz == [1, 2])
    orth = all(dot(fr[i], fr[j]) == 0 and dot(fr[i], fr[i]) == 1
               for fr in FRAMES for i, j in combinations(range(3), 2))
    checks.check("T2-frames", "4 rational orthonormal frames give 12 exact great circles",
                 orth and len(FRAMES) * 3 == 12)
    mons = ([(a, b, 0) for a in range(7) for b in range(7 - a)]
            + [(a, b, 1) for a in range(6) for b in range(6 - a)])
    rows = []
    ntrip = 0
    for fr in FRAMES:
        for i, j in combinations(range(3), 2):
            ea, eb = fr[i], fr[j]
            circ = [tuple(c * ea[t] + s * eb[t] for t in range(3)) for (c, s) in PTS4]
            per = 0
            for k1, k2, k3 in combinations(range(len(PTS4)), 3):
                p = balanced_weights2(PTS4[k1], PTS4[k2], PTS4[k3])
                if p is None:
                    continue
                tri = (circ[k1], circ[k2], circ[k3])
                rows.append([sum(pi * (n[0] ** m[0]) * (n[1] ** m[1]) * (n[2] ** m[2])
                                 for pi, n in zip(p, tri)) for m in mons])
                ntrip += 1
                per += 1
                if per >= 14:
                    break
    rk, ker = rref_nullspace(rows, len(mons))
    checks.check("T2-sphere", "degree <= 6, 49 unknowns, 168 triples, rank 46, nullity 3",
                 len(mons) == 49 and ntrip == 168 and rk == 46 and len(ker) == 3)
    nz = sorted(mons[i] for v in ker for i in range(49) if v[i] != 0)
    checks.check("T2-sphere-kernel", "that kernel is exactly span{x, y, z}",
                 nz == [(0, 0, 1), (0, 1, 0), (1, 0, 0)])
    beta = (F(3, 10), F(2, 5))
    vals = [F(1, 2) + dot(beta, n) for n in PTS5]
    born = all(sum(2 * x * (F(1, 2) + dot(beta, ni)) for x, ni in zip(p, ns)) == 1
               for ns, p in trips)
    big = (F(3, 5), F(4, 5))
    checks.check("T2-range", "|beta| = 1/2 keeps 1/2 + beta.n in [0,1] and sums to 1; |beta| = 1 does not",
                 dot(beta, beta) == F(1, 4) and all(0 <= v <= 1 for v in vals) and born
                 and F(1, 2) + dot(big, big) > 1)
    checks.note("T2-lemma1", "chaining balanced pairs round the circle carries one beta to every point")
    checks.note("T2-lemma2", "a form linear on every great circle is linear on the sphere, by gluing")


# ------------------------------------------------------- T3 the counting rogue
def rogue(kind, c):
    if kind == "P":
        return F(1, 2) if c == 1 else F(1, 3)
    return F(1, 2)


def t3(checks, trips):
    nm = 0
    ok = True
    for ns, p in trips:
        ok &= sum(rogue("P", 2 * x) for x in p) == 1
        nm += 1
    for n in PTS5:
        ok &= rogue("P", 1) + rogue("P", 1) == 1
        nm += 1
    for a in [F(j, 20) for j in range(1, 20)]:
        ok &= rogue("I", a) + rogue("I", 1 - a) == 1
        nm += 1
    checks.check("T3-realised", "5271 menus M_CONT realises: 5200 ternaries, 52 binaries, 19 coins",
                 nm == 5271)
    checks.check("T3-rogue", "the counting rogue is normalised on every one of them", ok)
    checks.check("T3-not-born", "it is not Born: w(P)/1 = 1/2 against w(P/2)/(1/2) = 2/3",
                 rogue("P", 1) / 1 != rogue("P", F(1, 2)) / F(1, 2))
    fam = all(sum(2 * x for x in p) - 2 == 0
              and sum(2 * x * ni[0] for x, ni in zip(p, ns)) == 0
              and sum(2 * x * ni[1] for x, ni in zip(p, ns)) == 0
              and sum(2 * x for x in p) / 2 == 1
              for ns, p in trips)
    checks.check("T3-family", "(1/2+lam)|v| - 2lam/3 + beta.v sums to 1 on all 5200, in lam and beta",
                 fam)
    lo, hi = F(-3, 2), F(0)
    checks.check("T3-family-range", "its range is in [0,1] exactly for lam in [-3/2, 0]",
                 -2 * lo / 3 == 1 and -2 * hi / 3 == 0
                 and F(1, 2) + lo / 3 == 0 and F(1, 2) + hi / 3 == F(1, 2))
    a = F(1, 4)
    checks.check("T3-collinear", "the collinear ternary {aP(n),(1-a)P(n),P(-n)} at a = 1/4 sums to 7/6",
                 rogue("P", a) + rogue("P", 1 - a) + rogue("P", 1) == F(7, 6))
    checks.check("T3-mixed", "the mixed coin ternary {cP(n),cP(-n),(1-c)I} at c = 1/2 sums to 7/6",
                 2 * rogue("P", F(1, 2)) + F(1, 2) == F(7, 6))
    n = PTS5[0]
    checks.check("T3-unrealised", "neither is a coplanar positively spanning rank-one triple",
                 balanced_weights2(n, n, (-n[0], -n[1])) is None)
    checks.note("T3-arity", "on M_CONT arity is a function of the effect, so 1/arity is menu-independent")


# ------------------------------------------------------- T4 Theorem B
def t4(checks, trips):
    idx = {c: i for i, c in enumerate(GRID)}
    one = idx[F(1)]
    rows = []
    for a in GRID:
        if a < 1 and (1 - a) in idx:
            r = [F(0)] * 24
            r[idx[a]] += 1
            r[idx[1 - a]] += 1
            r[one] -= 1
            rows.append(r)
    for a, b in combinations([c for c in GRID if c < 1], 2):
        c3 = 1 - a - b
        if c3 in idx and 0 < c3 < 1:
            r = [F(0)] * 24
            r[idx[a]] += 1
            r[idx[b]] += 1
            r[idx[c3]] += 1
            r[one] -= 1
            rows.append(r)
    rk, ker = rref_nullspace(rows, 24)
    coin_ok = (len(ker) == 1 and rk == 23
               and all(ker[0][i] / ker[0][one] == GRID[i] for i in range(24)))
    checks.check("T4-coin", "coin rows on the grid j/24: 144 rows, rank 23, nullity 1, kernel u(c) = c",
                 len(rows) == 144 and coin_ok)
    u = {GRID[i]: ker[0][i] / ker[0][one] for i in range(24)}
    checks.check("T4-odd", "the mixed coin menu then gives W(cn) + W(-cn) = 1 - u(1-c) = c: K is odd",
                 all(1 - u[1 - c] == c for c in GRID if c < 1 and (1 - c) in u))
    checks.check("T4-additive", "sum |v_i| = 2 on all 5200, so sum W = 1 is K(v1)+K(v2)+K(v3) = 0",
                 all(sum(2 * x for x in p) == 2 for ns, p in trips))
    sines = True
    ntri = 0
    for s1, s2 in combinations([c for c in GRID if c < 1], 2):
        s3 = 2 - s1 - s2
        if s3 not in idx or not (0 < s3 < 1) or s3 < s2:
            continue
        ntri += 1
        sines &= (2 / (s2 * s3)) / s1 == (2 / (s1 * s3)) / s2 == (2 / (s1 * s2)) / s3
    checks.check("T4-triangles", "44 perimeter-2 triangles have sides on the grid j/24", ntri == 44)
    checks.check("T4-sines", "sin A_i / c_i is one number per triangle, exactly: mode 1 is Born",
                 sines)
    expect = {0: 3, 1: 3, 3: 2, 5: 2, 7: 2}
    covered = {}
    kernels = {}
    good = True
    for k in (0, 1, 3, 5, 7):
        rows, nt = mode_rows(k, GRID, False)
        rk, ker = rref_nullspace(rows, 24)
        cov = [i for i in range(24) if GRID[i] < 1 and any(r[i] != 0 for r in rows)]
        unc = [str(GRID[i]) for i in range(24) if GRID[i] < 1 and i not in cov]
        good &= (nt == 44 and len(ker) == expect[k] and unc == ["1/24"])
        covered[k] = cov
        kernels[k] = ker
    checks.check("T4-cont-nullity",
                 "M_CONT: nullity 3 at k = 0 and 1, nullity 2 at k = 3, 5, 7; 1/24 uncovered", good)

    def prop(v, cov, shift):
        return all(v[i] * (GRID[j] - shift) == v[j] * (GRID[i] - shift) for i in cov for j in cov)

    k0 = kernels[0]
    cov0 = covered[0]
    checks.check("T4-cont-k0",
                 "at k = 0 the covered interior carries the rogue (c - 2/3) and h(1) is free",
                 any(prop(v, cov0, F(2, 3)) and not prop(v, cov0, F(0)) for v in k0)
                 and any(v[-1] == 1 and all(v[i] == 0 for i in cov0) for v in k0))
    k1 = kernels[1]
    cov1 = covered[1]
    checks.check("T4-cont-k1",
                 "at k = 1 the covered interior carries Born c and h(1) is free",
                 any(prop(v, cov1, F(0)) and not prop(v, cov1, F(2, 3)) for v in k1)
                 and any(v[-1] == 1 and all(v[i] == 0 for i in cov1) for v in k1))
    killed = all(all(v[i] == 0 for i in covered[k]) for k in (3, 5, 7) for v in kernels[k])
    checks.check("T4-cont-high",
                 "at k = 3, 5, 7 the interior is killed by the non-collinear ternaries alone", killed)
    good = True
    for k in (0, 3, 5, 7):
        rows, nt = mode_rows(k, GRID, True)
        rk, ker = rref_nullspace(rows, 24)
        good &= (nt == 44 and rk == 24 and len(ker) == 0)
    checks.check("T4-all-even", "M_all: rank 24 and nullity 0 at k = 0, 3, 5, 7", good)
    rows, nt = mode_rows(1, GRID, True)
    rk, ker = rref_nullspace(rows, 24)
    checks.check("T4-all-k1", "M_all: nullity 1 at k = 1, the vector h_1(c) = c with h_1(1) = 1",
                 len(rows) == 111 and rk == 23 and len(ker) == 1
                 and all(ker[0][i] / ker[0][-1] == GRID[i] for i in range(24)))
    checks.note("T4-modes", "sin kA_1 = 0 with sin kA_2 nonzero kills h_k on an interval, then everywhere")
    checks.note("T4-ae", "an integrable direction profile gives the Born form a.e. in direction per scale")


# ------------------------------------------------------- source gates
def gates(checks):
    note = normalize(NOTE_PATH.read_text())
    parent = normalize(PARENT_PATH.read_text())
    axiom = normalize(AXIOM_PATH.read_text())
    family = ("**Low-arity eligibility.** Every two- or three-member menu is normalized: "
              "`sum_j w(E_j)=1`.")
    lift = ("`F` is a nonnegative normalized frame function on `C^3` with no continuity, "
            "measurability, differentiability, or countable additivity premise added.")
    gleason = ("By the named dimension-three frame theorem, there is a unique positive operator "
               "`R on C^3` with `Tr(R)=1`")
    checks.check("gate-parent-family", "the 2026-08-09 note's low-arity family M_all, verbatim",
                 family in parent and family in note)
    checks.check("gate-parent-lift", "its ancilla frame lift, verbatim", lift in parent and lift in note)
    checks.check("gate-parent-gleason", "its dimension-three frame step, verbatim",
                 gleason in parent and gleason in note)
    checks.check("gate-axiom-domain", "the axiom file's one-site M_2(C) presentation",
                 "The full one-site possibility domain has algebraic presentation `M_2(C)`" in axiom)
    checks.check("gate-correction", "the note records the homogeneous-ansatz correction, quoted",
                 "In the normal form `w(cP(u)) = c(1 + f(u))/2`" in note
                 and "Take the polynomial sector `w(c P(u)) = c(1 + f(u))/2`" in note
                 and "row = [r + c * v for r, v in zip(row, f_row(n, a_mons, b_mons))]" in note)
    checks.check("gate-surface", "the note keeps its conditional surface and its audit line",
                 all(s in note for s in ("actual_current_surface_status: conditional-support",
                                         "audit_required_before_effective_retained: true",
                                         "Independent audit remains required")))


def main():
    print("arithmetic_boundary: exact rational only, fractions.Fraction; no float, no seed")
    print("grid_boundary: 52 and 68 circle points, 12 rational great circles, radii j/24")
    print("truncation_boundary: circle modes 0..8, sphere degree <= 6; Lemmas 1-2 need neither")
    print("import_boundary: no frame theorem, no ancilla lift, no Gleason; the parent is read as text")
    checks = Checks()
    trips = balanced_triples(PTS5)
    t1(checks, trips)
    t2(checks, trips)
    t3(checks, trips)
    t4(checks, trips)
    gates(checks)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
