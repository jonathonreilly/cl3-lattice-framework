#!/usr/bin/env python3
"""Exact checks for the note that lifts the finite-alphabet abundance no-go.

Every stage is exact: rational `fractions.Fraction` linear algebra for the lattice
law, its covariance sweeps and the polynomial rank certificates, and exact symbolic
`sympy` integration for the continuum-density stage.  No floating point enters any
load-bearing computation.  No seeds are used: the Bloch directions come from a
declared stereographic table, the great circles from declared integer quaternions,
and every swept condition from declared index arithmetic.  The largest dense object
is 2470 by 21.  The dimension-three frame-function theorem is named as context and
is not recomputed.  Recorded arguments are printed with an `ARG:` prefix and are
excluded from the PASS/FAIL total, so no prose claim is counted as a verification.
"""

import time
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "A_CONTINUUM_RECORD_ALPHABET_LIFTS_THE_ABUNDANCE_NO_GO_A_FIBRED_BORN_THEOREM_"
    "AND_A_FACTOR_OF_TWO_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-09-04.md"
)
PARENT_NOTE = ROOT / "docs" / (
    "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_"
    "NOTE_2026-08-09.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/A_CONTINUUM_RECORD_ALPHABET_LIFTS_THE_ABUNDANCE_NO_GO_A_FIBRED_BORN_"
    "THEOREM_AND_A_FACTOR_OF_TWO_OBSTRUCTION_BOUNDED_THEOREM_NOTE_2026-09-04.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM"
    "_NOTE_2026-08-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text):
    return " ".join(text.split())


class Checks:
    """Machine verifications count; recorded arguments are printed, never counted."""

    def __init__(self):
        self.passed = 0
        self.failed = 0
        self.arguments = 0

    def check(self, label, statement, condition):
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} {statement}")

    def note(self, label, statement):
        self.arguments += 1
        print(f"ARG: {label} {statement}")

    def finish(self):
        print(f"recorded_arguments: {self.arguments} printed, none counted as verified")
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


# ------------------------------------------------------------------ exact linear algebra
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def smul(s, a):
    return tuple(s * x for x in a)


def neg(a):
    return tuple(-x for x in a)


def matvec(m, v):
    return tuple(dot(r, v) for r in m)


def _reduce(rows, ncols):
    m = [list(r) for r in rows]
    pivots, rank = [], 0
    for col in range(ncols):
        sel = None
        for i in range(rank, len(m)):
            if m[i][col] != 0:
                sel = i
                break
        if sel is None:
            continue
        m[rank], m[sel] = m[sel], m[rank]
        piv = m[rank][col]
        m[rank] = [x / piv for x in m[rank]]
        for i in range(len(m)):
            if i != rank and m[i][col] != 0:
                f = m[i][col]
                m[i] = [a - f * b for a, b in zip(m[i], m[rank])]
        pivots.append(col)
        rank += 1
        if rank == len(m):
            break
    return m, pivots


def exact_rank(rows, ncols):
    return len(_reduce(rows, ncols)[1])


def kernel_basis(rows, ncols):
    m, pivots = _reduce(rows, ncols)
    basis = []
    for free in [c for c in range(ncols) if c not in pivots]:
        v = [F(0)] * ncols
        v[free] = F(1)
        for r, pc in enumerate(pivots):
            v[pc] = -m[r][free]
        basis.append(tuple(v))
    return basis


def solve_exact(a_rows, b_vec):
    """Unique exact solution of an overdetermined rational system, else None."""
    n = len(a_rows[0])
    m, pivots = _reduce([list(r) + [b] for r, b in zip(a_rows, b_vec)], n)
    for i in range(len(pivots), len(m)):
        if m[i][n] != 0:
            return None
    if len(pivots) < n:
        return None
    x = [F(0)] * n
    for r, pc in enumerate(pivots):
        x[pc] = m[r][n]
    return tuple(x)


def proper_cubic_rotations():
    out = []
    for perm in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for signs in product([1, -1], repeat=3):
            rows = [[F(0)] * 3 for _ in range(3)]
            for i in range(3):
                rows[i][perm[i]] = F(signs[i])
            det = (rows[0][0] * (rows[1][1] * rows[2][2] - rows[1][2] * rows[2][1])
                   - rows[0][1] * (rows[1][0] * rows[2][2] - rows[1][2] * rows[2][0])
                   + rows[0][2] * (rows[1][0] * rows[2][1] - rows[1][1] * rows[2][0]))
            if det == 1:
                out.append(tuple(tuple(r) for r in rows))
    return out


ROTS = proper_cubic_rotations()
SLOTS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def quat_rot(a, b, c, d):
    n = F(a * a + b * b + c * c + d * d)
    rows = [[F(a * a + b * b - c * c - d * d), F(2 * (b * c - a * d)), F(2 * (b * d + a * c))],
            [F(2 * (b * c + a * d)), F(a * a - b * b + c * c - d * d), F(2 * (c * d - a * b))],
            [F(2 * (b * d - a * c)), F(2 * (c * d + a * b)), F(a * a - b * b - c * c + d * d)]]
    return tuple(tuple(x / n for x in row) for row in rows)


def unit_from_stereo(p, q):
    d = p * p + q * q + 1
    return (2 * p / d, 2 * q / d, (p * p + q * q - 1) / d)


# ------------------------------------------------------------------ declared families
STEREO_P = [F(0), F(1), F(-1), F(1, 2), F(2), F(-1, 3), F(3, 2), F(1, 4), F(-2, 3), F(5, 2)]
STEREO_Q = [F(0), F(1), F(-1), F(1, 3), F(2), F(-3, 2), F(1, 5), F(4, 3)]
QUATS = [(1, 0, 0, 0), (1, 1, 0, 0), (2, 1, 0, 0), (1, 0, 1, 0), (2, 0, 1, 1), (3, 1, 2, 0),
         (1, 1, 1, 1), (2, 2, 1, 0), (3, 0, 1, 2), (4, 1, 1, 2), (2, 1, 3, 1), (5, 1, 0, 2),
         (1, 2, 2, 3), (3, 3, 1, 1)]
TPARAMS = [F(0), F(1), F(-1), F(1, 2), F(-1, 2), F(2), F(-2), F(1, 3), F(3), F(-1, 3), F(-3),
           F(2, 3), F(3, 2), F(1, 5), F(5), F(4, 3), F(-4, 3), F(5, 2), F(-5, 2), F(1, 4), F(-1, 4)]
SEEDS = [(F(1), F(0), F(0)), (F(3, 5), F(4, 5), F(0)),
         unit_from_stereo(F(1, 2), F(1, 3)), unit_from_stereo(F(2), F(-1))]

SAMPLE_DIRS = []
for _p in STEREO_P:
    for _q in STEREO_Q:
        _u = unit_from_stereo(_p, _q)
        if _u not in SAMPLE_DIRS:
            SAMPLE_DIRS.append(_u)


def plane_frame(q):
    r = quat_rot(*q)
    return (r[0][0], r[1][0], r[2][0]), (r[0][1], r[1][1], r[2][1])


PLANES = [plane_frame(q) for q in QUATS]


def circ(t):
    d = 1 + t * t
    return ((1 - t * t) / d, 2 * t / d)


def in_plane(e, f, t):
    co, si = circ(t)
    return add(smul(co, e), smul(si, f))


def ternary_weights(n1, n2, n3):
    """The unique c with sum c_k n_k = 0 and sum c_k = 2, when it is positive."""
    a_rows = [[n1[0], n2[0], n3[0]], [n1[1], n2[1], n3[1]],
              [n1[2], n2[2], n3[2]], [F(1), F(1), F(1)]]
    c = solve_exact(a_rows, [F(0), F(0), F(0), F(2)])
    if c is None or any(x <= 0 for x in c):
        return None
    return c


def build_ternaries(planes, tparams, cap):
    out = []
    for e, f in planes:
        pts = [in_plane(e, f, t) for t in tparams]
        pts += [neg(p) for p in pts]
        for i, j, k in combinations(range(len(pts)), 3):
            n1, n2, n3 = pts[i], pts[j], pts[k]
            if n1 == n2 or n2 == n3 or n1 == n3:
                continue
            c = ternary_weights(n1, n2, n3)
            if c is None:
                continue
            out.append(((c[0], n1), (c[1], n2), (c[2], n3)))
            if len(out) >= cap:
                return out
    return out


def resolves_identity(menu):
    total = sum(c for c, _ in menu)
    v = (sum(c * n[0] for c, n in menu), sum(c * n[1] for c, n in menu),
         sum(c * n[2] for c, n in menu))
    return total == 2 and v == (F(0), F(0), F(0))


def det3(a, b, c):
    return (a[0] * (b[1] * c[2] - b[2] * c[1]) - a[1] * (b[0] * c[2] - b[2] * c[0])
            + a[2] * (b[0] * c[1] - b[1] * c[0]))


# ------------------------------------------------------------------ the laws
def rot_slot(r, d):
    return tuple(int(x) for x in matvec(r, tuple(F(v) for v in d)))


def rot_dir(r, u):
    return matvec(r, u)


def rot_cond(r, cond):
    return {rot_slot(r, d): rot_dir(r, u) for d, u in cond.items()}


def rot_item(r, item):
    return item if item[0] == "I" else (item[0], item[1], rot_dir(r, item[2]))


def pair_mean(ms):
    """The invariant mean of the pairwise record inner products."""
    pairs = list(combinations(range(len(ms)), 2))
    return sum(dot(ms[i], ms[j]) for i, j in pairs) / F(len(pairs))


def L_CONT(cond):
    """The record-echo law: one record echoes as its binary resolution, three coplanar
    records as their ternary resolution, two records as the coin a = (1 + m_1.m_2)/2."""
    ms = list(cond.values())
    if len(ms) == 1:
        return (("P", F(1), ms[0]), ("P", F(1), neg(ms[0])))
    if len(ms) == 3:
        c = ternary_weights(*ms)
        if c is not None:
            return tuple(("P", c[k], ms[k]) for k in range(3))
        return (("I", F(1)),)
    if len(ms) == 2:
        a = (1 + pair_mean(ms)) / 2
        if 0 < a < 1:
            return (("I", a), ("I", 1 - a))
        return (("I", F(1)),)
    return (("I", F(1)),)


def L_COIN(cond):
    """Covariant, continuum alphabet, coin supports only: no rank-one support at all."""
    ms = list(cond.values())
    if len(ms) < 2:
        return (("I", F(1)),)
    a = (1 + pair_mean(ms)) / 2
    return (("I", a), ("I", 1 - a)) if 0 < a < 1 else (("I", F(1)),)


def L_BIN_dir(cond):
    """The equivariant record sum whose direction L_BIN echoes."""
    v = (F(0), F(0), F(0))
    for m in cond.values():
        v = add(v, m)
    return v


def L_BIN(cond):
    """Covariant, continuum alphabet, binary rank-one supports only: {P(vhat), P(-vhat)}."""
    v = L_BIN_dir(cond)
    if v == (F(0), F(0), F(0)):
        return (("I", F(1)),)
    return (("Phat", F(1), v), ("Phat", F(1), neg(v)))


def lam(cond):
    """The lattice dipole: the sum of the recorded slot directions."""
    v = (0, 0, 0)
    for d in cond:
        v = tuple(a + b for a, b in zip(v, d))
    return v


def support_resolves(support):
    trace = sum(2 * it[1] if it[0] == "I" else it[1] for it in support)
    v = (F(0), F(0), F(0))
    for it in support:
        if it[0] == "P":
            v = add(v, smul(it[1], it[2]))
    return trace == 2 and v == (F(0), F(0), F(0))


def as_set(support):
    return set(map(str, support))


def born(r, item):
    if item[0] == "I":
        return item[1]
    return item[1] * (1 + dot(r, item[2])) / 2


T_PARAM = F(2, 3)
UNIT_SLOTS = [tuple(s) for s in SLOTS]


def rho_of_label(l):
    if l in UNIT_SLOTS:
        return tuple(T_PARAM * F(x) for x in l)
    return (F(0), F(0), F(0))


# ------------------------------------------------------------------ polynomial sector
A_MONS = [(i, j) for i in range(6) for j in range(6) if i + j <= 5]
B_MONS = [(i, j) for i in range(5) for j in range(5) if i + j <= 4]
A_ODD = [(i, j) for (i, j) in A_MONS if (i + j) % 2 == 1]
B_EVEN = [(i, j) for (i, j) in B_MONS if (i + j) % 2 == 0]
NCOL_ODD = len(A_ODD) + len(B_EVEN)


def f_row(n, a_mons, b_mons):
    x, y, z = n
    return [x ** i * y ** j for (i, j) in a_mons] + [z * x ** i * y ** j for (i, j) in b_mons]


def menu_row(menu, a_mons, b_mons):
    row = [F(0)] * (len(a_mons) + len(b_mons))
    for c, n in menu:
        row = [r + c * v for r, v in zip(row, f_row(n, a_mons, b_mons))]
    return row


def is_born_kernel(basis):
    if len(basis) != 3:
        return False
    idx = (A_ODD.index((1, 0)), A_ODD.index((0, 1)), len(A_ODD) + B_EVEN.index((0, 0)))
    rows = [list(b) for b in basis]
    for i in idx:
        e = [F(0)] * NCOL_ODD
        e[i] = F(1)
        if exact_rank(rows + [e], NCOL_ODD) != 3:
            return False
    return True


def w_cubic(n):
    return n[2] ** 3


def demoivre(co, si, m):
    c, s = F(1), F(0)
    for _ in range(m):
        c, s = c * co - s * si, c * si + s * co
    return c, s


def circle_row(menu):
    row = [F(0)] * 6
    for c, n in menu:
        co, si = n[0], n[1]
        for k, m in enumerate([1, 3, 5]):
            cm, sm = demoivre(co, si, m)
            row[2 * k] += c * cm
            row[2 * k + 1] += c * sm
    return row


# ------------------------------------------------------------------ T0 declared objects
def t0(checks):
    checks.check("T0-rotations", "24 proper cubic rotations, determinant one", len(ROTS) == 24)
    checks.check("T0-directions", f"{len(SAMPLE_DIRS)} declared rational unit Bloch directions",
                 len(SAMPLE_DIRS) == 80 and all(dot(u, u) == 1 for u in SAMPLE_DIRS))
    checks.check("T0-planes", f"{len(PLANES)} declared rational plane frames from quaternions",
                 len(PLANES) == 14 and all(dot(e, e) == 1 and dot(f, f) == 1 and dot(e, f) == 0
                                           for e, f in PLANES))
    ternaries = build_ternaries(PLANES, TPARAMS[:9], cap=4000)
    checks.check("T0-ternary-family", f"{len(ternaries)} exact rank-one ternary resolutions of I_2",
                 len(ternaries) == 1764 and all(resolves_identity(m) for m in ternaries))
    checks.check("T0-ternary-effects", "every weight has 0 < c_k <= 1, so each c_k P(n_k) is an effect",
                 all(all(0 < c <= 1 for c, _ in m) for m in ternaries))
    checks.check("T0-ternary-coplanar", "det[n_1 n_2 n_3] = 0 on all: the family is 5-dimensional",
                 all(det3(m[0][1], m[1][1], m[2][1]) == 0 for m in ternaries))
    return ternaries


# ------------------------------------------------------------------ declared conditions
def declared_conditions(ternaries, closed):
    """1740 conditions by declared index arithmetic, one block per branch of L_CONT."""
    conds = [{d: u} for d in SLOTS for u in closed[:40]]
    conds += [{SLOTS[0]: m[0][1], SLOTS[2]: m[1][1], SLOTS[4]: m[2][1]}
              for m in ternaries[:500]]
    coin = []
    i = 0
    while len(coin) < 500:
        u = closed[i % len(closed)]
        v = closed[(7 * i + 3) % len(closed)]
        a = (1 + dot(u, v)) / 2
        if 0 < a < 1:
            coin.append({SLOTS[i % 6]: u, SLOTS[(i + 1) % 6]: v})
        i += 1
    conds += coin
    default = []
    i = 0
    while len(default) < 500:
        vals = [closed[(3 * i + 5 * k) % len(closed)] for k in range(4)]
        default.append({SLOTS[(i + k) % 6]: vals[k] for k in range(4)})
        i += 1
    return conds + default


# ------------------------------------------------------------------ T1 the law
def t1(checks, ternaries):
    closed = []
    for s in SEEDS:
        for r in ROTS:
            u = rot_dir(r, s)
            if u not in closed:
                closed.append(u)
    checks.check("T1-closed-alphabet", f"{len(closed)} record values closed under the 24 rotations",
                 all(rot_dir(r, u) in closed for r in ROTS for u in closed))
    conds = declared_conditions(ternaries, closed)
    checks.check("T1-declared-conditions",
                 f"{len(conds)} conditions by declared index arithmetic, no seed", len(conds) == 1740)

    mismatch = 0
    nchecks = 0
    bad_resolution = 0
    supports = set()
    for cond in conds:
        support = L_CONT(cond)
        supports.add(tuple(sorted(map(str, support))))
        if not support_resolves(support):
            bad_resolution += 1
        for r in ROTS:
            nchecks += 1
            if as_set(L_CONT(rot_cond(r, cond))) != {str(rot_item(r, it)) for it in support}:
                mismatch += 1
    checks.check("T1-covariance", f"S(g.n) = g.S(n) on {nchecks} exact checks, {mismatch} mismatches",
                 mismatch == 0 and nchecks == 41760)
    checks.check("T1-resolutions", f"all {len(supports)} distinct realised supports resolve I_2",
                 bad_resolution == 0)
    permuted = {SLOTS[5]: ternaries[0][2][1], SLOTS[3]: ternaries[0][0][1],
                SLOTS[1]: ternaries[0][1][1]}
    original = {SLOTS[0]: ternaries[0][0][1], SLOTS[2]: ternaries[0][1][1],
                SLOTS[4]: ternaries[0][2][1]}
    checks.check("T1-multiset-only", "the support reads the record values only, never the slots",
                 as_set(L_CONT(permuted)) == as_set(L_CONT(original)))
    checks.note("T1-nearest-neighbour",
                "the rule reads the six neighbour record values and nothing else")

    binaries = sum(1 for u in SAMPLE_DIRS
                   if L_CONT({SLOTS[0]: u}) == (("P", F(1), u), ("P", F(1), neg(u))))
    checks.check("T1-abundance-binary",
                 f"every binary resolution is a support: {binaries}/80 declared directions",
                 binaries == 80)
    ter_ok = 0
    for m in ternaries[:1200]:
        cond = {SLOTS[0]: m[0][1], SLOTS[2]: m[1][1], SLOTS[4]: m[2][1]}
        if as_set(L_CONT(cond)) == {str(("P", c, n)) for c, n in m}:
            ter_ok += 1
    checks.check("T1-abundance-ternary",
                 f"every non-collinear rank-one ternary is a support: {ter_ok}/1200", ter_ok == 1200)
    coin_vals = set()
    for u in SAMPLE_DIRS[:20]:
        for v in SAMPLE_DIRS[:20]:
            a = (1 + dot(u, v)) / 2
            if 0 < a < 1:
                coin_vals.add(min(a, 1 - a))
    checks.check("T1-abundance-coin",
                 f"coin supports at {len(coin_vals)} distinct exact a; a = (1+m_1.m_2)/2 sweeps (0,1)",
                 len(coin_vals) >= 50)
    checks.check("T1-abundance", "L_CONT has full menu abundance: the finite-alphabet no-go is lifted",
                 binaries == 80 and ter_ok == 1200 and len(coin_vals) >= 50 and mismatch == 0)
    return conds, closed


# ------------------------------------------------------------------ T2 the fibred theorem
def t2(checks, ternaries, conds):
    mismatch = 0
    nchecks = 0
    for cond in conds:
        for r in ROTS:
            nchecks += 1
            if lam(rot_cond(r, cond)) != rot_slot(r, lam(cond)):
                mismatch += 1
    checks.check("T2-dipole-equivariant",
                 f"lambda(g.n) = g lambda(n) on {nchecks} exact checks, {mismatch} mismatches",
                 mismatch == 0)
    checks.note("T2-dipole-decoupled",
                "lambda reads the slots, the menu the values: they are decoupled")

    ex = (1, 0, 0)
    fib_bin = all(lam({SLOTS[0]: u}) == ex
                  and L_CONT({SLOTS[0]: u}) == (("P", F(1), u), ("P", F(1), neg(u)))
                  for u in SAMPLE_DIRS)
    fib_ter = 0
    for m in ternaries[:1200]:
        cond = {SLOTS[0]: m[0][1], SLOTS[2]: m[1][1], SLOTS[3]: m[2][1]}
        if lam(cond) == ex and as_set(L_CONT(cond)) == {str(("P", c, n)) for c, n in m}:
            fib_ter += 1
    checks.check("T2-fibre-abundance",
                 f"the fibre lambda = e_x realises every binary and {fib_ter}/1200 ternaries",
                 fib_bin and fib_ter == 1200)

    normalised = True
    nonneg = True
    mismatch = 0
    npos = 0
    for cond in conds:
        support = L_CONT(cond)
        r_vec = rho_of_label(lam(cond))
        if sum(born(r_vec, it) for it in support) != 1:
            normalised = False
        if any(born(r_vec, it) < 0 for it in support):
            nonneg = False
        for rot in ROTS:
            r_img = rho_of_label(lam(rot_cond(rot, cond)))
            for it in support:
                npos += 1
                if born(r_vec, it) != born(r_img, rot_item(rot, it)):
                    mismatch += 1
    checks.check("T2-fibred-law-normalised",
                 "L_FIB at rho_l = (I + (2/3) l.sigma)/2 sums to 1 on every support",
                 normalised)
    checks.check("T2-fibred-law-positive", "and is non-negative on every realised support", nonneg)
    checks.check("T2-fibred-law-covariant",
                 f"p_(g.n)(g.v) = p_n(v) on {npos} per-possibility checks, {mismatch} mismatches",
                 mismatch == 0 and npos == 83520)

    m_a = ((F(8, 9), (F(0), F(0), F(1))), (F(5, 9), (F(3, 5), F(0), F(-4, 5))),
           (F(5, 9), (F(-3, 5), F(0), F(-4, 5))))
    m_b = ((F(8, 9), (F(0), F(0), F(1))), (F(5, 9), (F(0), F(3, 5), F(-4, 5))),
           (F(5, 9), (F(0), F(-3, 5), F(-4, 5))))
    c_a = {SLOTS[0]: m_a[0][1], SLOTS[2]: m_a[1][1], SLOTS[3]: m_a[2][1]}
    c_b = {SLOTS[0]: m_b[0][1], SLOTS[2]: m_b[1][1], SLOTS[3]: m_b[2][1]}
    checks.check("T2-non-vacuous", "one fibre holds two supports sharing the possibility (8/9)P(e_z)",
                 resolves_identity(m_a) and resolves_identity(m_b)
                 and lam(c_a) == ex and lam(c_b) == ex
                 and as_set(L_CONT(c_a)) == {str(("P", c, n)) for c, n in m_a}
                 and as_set(L_CONT(c_b)) == {str(("P", c, n)) for c, n in m_b}
                 and m_a[0] == m_b[0] and as_set(m_a) != as_set(m_b))

    checks.check("T2-normal-form",
                 f"degree-five sector: {len(A_MONS) + len(B_MONS)} monomials, {NCOL_ODD} when odd",
                 len(A_MONS) + len(B_MONS) == 36 and NCOL_ODD == 21)
    rows = [menu_row(m, A_ODD, B_EVEN) for m in ternaries]
    rank = exact_rank(rows, NCOL_ODD)
    kernel = kernel_basis(rows, NCOL_ODD)
    checks.check("T2-rank-certificate",
                 f"the law-realised family: {len(rows)} by {NCOL_ODD}, rank {rank}, nullity "
                 f"{NCOL_ODD - rank}, exact over Q",
                 rank == 18 and NCOL_ODD - rank == 3)
    checks.check("T2-kernel-is-born",
                 "the kernel is exactly span{x, y, z}, the Born family tr(rho, cP(u))",
                 is_born_kernel(kernel))
    rank36 = exact_rank([menu_row(m, A_MONS, B_MONS) for m in ternaries], 36)
    checks.check("T2-rank-certificate-36",
                 f"without oddness: 36 columns, rank {rank36}, nullity {36 - rank36}",
                 36 - rank36 == 3)
    checks.note("T2-fibred-theorem",
                "abundance in fibre and a grading shared there give p_n(E) = "
                "tr(rho_lambda(n) E) by the imported frame theorem")


# ------------------------------------------------------------------ T3 the factor of two
def t3(checks):
    th, ph = sp.symbols("theta phi", real=True)
    rx, ry, rz = sp.symbols("r_x r_y r_z", real=True)
    u = sp.Matrix([sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)])
    r_vec = sp.Matrix([rx, ry, rz])
    dmu = sp.sin(th) / (4 * sp.pi)

    def sphere(expr, top=sp.pi):
        return sp.simplify(sp.integrate(sp.integrate(expr, (ph, 0, 2 * sp.pi)), (th, 0, top)))

    total = sphere(dmu)
    moments = [sphere(u[i] * dmu) for i in range(3)]
    checks.check("T3-density-normalised",
                 "(1 + r.u) dOmega/4pi integrates to exactly 1, exact symbolic",
                 sp.simplify(sphere((1 + (r_vec.T * u)[0]) * dmu) - 1) == 0)
    checks.check("T3-continuum-resolution",
                 "int 2P(u) dmu = I exactly: the continuum family resolves the identity",
                 total == 1 and all(m == 0 for m in moments))
    hemi = sphere(sp.cos(th) * dmu, top=sp.pi / 2)
    checks.check("T3-hemisphere",
                 f"hemisphere A: mu(A) = 1/2 and int_A u dmu = ({hemi}) e_z, the maximiser",
                 sp.simplify(hemi - sp.Rational(1, 4)) == 0)
    checks.check("T3-factor-of-two",
                 "the Born value needs int_A u dmu = e_z/2, the maximum is 1/4: short by two",
                 sp.simplify(2 * hemi - sp.Rational(1, 2)) == 0)
    checks.note("T3-per-condition",
                "a support carries one menu, so abundance is across conditions")
    checks.note("T3-lueders",
                "Lueders conditioning on a locked pure state is defined off one antipode")
    checks.note("T3-zero-singleton",
                "reading note (3) is met: a singleton has zero measure while 1 + r.u "
                "stays positive")


# ------------------------------------------------------------------ T4 permitted, not supplied
def t4(checks, conds):
    coin_mismatch = 0
    bin_mismatch = 0
    ncoin = 0
    for cond in conds[:400]:
        for r in ROTS:
            ncoin += 1
            if as_set(L_COIN(rot_cond(r, cond))) != {str(rot_item(r, it)) for it in L_COIN(cond)}:
                coin_mismatch += 1
            if L_BIN_dir(rot_cond(r, cond)) != rot_dir(r, L_BIN_dir(cond)):
                bin_mismatch += 1
    checks.check("T4-coin-law-covariant",
                 f"L_COIN is covariant on {ncoin} exact checks, {coin_mismatch} mismatches",
                 coin_mismatch == 0 and ncoin == 9600)
    checks.check("T4-coin-law-no-rank-one", "and realises no rank-one support at all",
                 all(all(it[0] == "I" for it in L_COIN(c)) for c in conds))
    checks.check("T4-binary-law-covariant",
                 f"L_BIN is equivariant on {ncoin} exact checks, {bin_mismatch} mismatches",
                 bin_mismatch == 0)
    bin_supports = [L_BIN(c) for c in conds]
    checks.check("T4-binary-law-binary-only",
                 "and realises only antipodal binary supports, never a ternary",
                 all(len(s) <= 2 for s in bin_supports)
                 and all(s[1] == (s[0][0], s[0][1], neg(s[0][2]))
                         for s in bin_supports if len(s) == 2)
                 and any(len(s) == 2 for s in bin_supports))
    checks.check("T4-grading-odd", "f(u) = u_z^3 is odd: normalised on every binary and coin support",
                 all(w_cubic(u) + w_cubic(neg(u)) == 0 for u in SAMPLE_DIRS))
    checks.check("T4-grading-non-born",
                 "and non-Born: f(3/5,0,4/5) = 64/125 against 4/5, with |f| <= 1",
                 w_cubic((F(3, 5), F(0), F(4, 5))) == F(64, 125)
                 and all(abs(w_cubic(u)) <= 1 for u in SAMPLE_DIRS))


# ------------------------------------------------------------------ T5 covariance obstruction
def invariant_bloch(group):
    rows = []
    for r in group:
        for i in range(3):
            rows.append([r[i][j] - (F(1) if i == j else F(0)) for j in range(3)])
    return kernel_basis(rows, 3)


def t5(checks, conds):
    ex = (1, 0, 0)
    stab = [r for r in ROTS if rot_slot(r, ex) == ex]
    checks.check("T5-stabiliser", f"Stab(e_x) has order {len(stab)}, the C_4 about the x axis",
                 len(stab) == 4)
    inv_ex = invariant_bloch(stab)
    checks.check("T5-fibre-state-free",
                 "its invariant Bloch space is the x axis: rho = (I + t sigma_x)/2, t free",
                 len(inv_ex) == 1 and inv_ex[0][1] == 0 and inv_ex[0][2] == 0 and inv_ex[0][0] != 0)
    checks.check("T5-invariant-fibre-forced",
                 "the invariant Bloch space is {0}: an invariant class forces rho = I/2",
                 len(invariant_bloch(ROTS)) == 0)
    scalar_invariant = True
    for cond in conds[:400]:
        ms = list(cond.values())
        label = (len(ms), tuple(sorted(str(dot(ms[i], ms[j]))
                                       for i, j in combinations(range(len(ms)), 2))))
        for r in ROTS:
            image = list(rot_cond(r, cond).values())
            other = (len(image), tuple(sorted(str(dot(image[i], image[j]))
                                              for i, j in combinations(range(len(image)), 2))))
            if label != other:
                scalar_invariant = False
    checks.check("T5-scalar-labels-invariant",
                 "record count and pairwise record dots are rotation invariant",
                 scalar_invariant)


# ------------------------------------------------------------------ T6 the great circle
def t6(checks, ternaries):
    plane0 = PLANES[0]
    checks.check("T6-plane", "the identity quaternion's plane is the great circle z = 0",
                 plane0[0] == (F(1), F(0), F(0)) and plane0[1] == (F(0), F(1), F(0)))
    circle_ternaries = build_ternaries([plane0], TPARAMS, cap=3000)
    rows = [menu_row(m, A_ODD, B_EVEN) for m in circle_ternaries]
    rank = exact_rank(rows, NCOL_ODD)
    checks.check("T6-circle-global-nullity",
                 f"all {len(rows)} in-circle ternaries leave global nullity {NCOL_ODD - rank}",
                 NCOL_ODD - rank == 17)
    crows = [circle_row(m) for m in circle_ternaries]
    crank = exact_rank(crows, 6)
    ckernel = kernel_basis(crows, 6)
    checks.check("T6-circle-on-circle",
                 f"on the circle at modes 1,3,5: rank {crank}, nullity {6 - crank}",
                 crank == 4 and len(ckernel) == 2)
    checks.check("T6-circle-kernel",
                 "modes 3 and 5 are annihilated, so f is a cos t + b sin t: Born odds there",
                 all(b[2] == 0 and b[3] == 0 and b[4] == 0 and b[5] == 0 for b in ckernel))
    checks.check("T6-grading-blind-in-plane",
                 f"u_z^3 has residual exactly zero on all {len(rows)} in-circle ternaries",
                 all(sum(c * w_cubic(n) for c, n in m) == 0 for m in circle_ternaries))
    nonzero = sum(1 for m in ternaries if sum(c * w_cubic(n) for c, n in m) != 0)
    checks.check("T6-grading-fails-out-of-plane",
                 f"but fails {nonzero} of {len(ternaries)} over 14 planes", nonzero > 0)
    checks.note("T6-two-circles",
                "two non-parallel circles agree at +-e_x, so one r covers their union")
    checks.note("T6-price",
                "the price stays three items: abundance moves from unpayable to payable")


# ------------------------------------------------------------------ main
def main():
    started = time.time()
    checks = Checks()
    note = normalize(NOTE_PATH.read_text(encoding="utf-8"))
    parent = normalize(PARENT_NOTE.read_text(encoding="utf-8"))
    axiom = normalize(AXIOM_PATH.read_text(encoding="utf-8"))

    print("external_scientific_inputs: the axiom file and the 2026-08-09 parent are read for "
          "source gates")
    print("package_local_integrity_reads: the source note is read for claim-surface consistency")
    print("standard_theorem_boundary: the dimension-three frame-function theorem is named, not "
          "recomputed")
    print("arithmetic_boundary: every stage is exact rational or exact symbolic, no floats")

    ternaries = t0(checks)
    conds, _closed = t1(checks, ternaries)
    t2(checks, ternaries, conds)
    t3(checks)
    t4(checks, conds)
    t5(checks, conds)
    t6(checks, ternaries)

    checks.check("source-qubit", "Qubit: the one-site possibility domain has presentation M_2(C)",
                 "The full one-site possibility domain has algebraic presentation `M_2(C)`" in axiom)
    checks.check("source-admissibility",
                 "Admissibility: the distribution is nearest-neighbor determined and varying",
                 "the probability distribution over the possibilities is determined by, and varies "
                 "with, the nearest-neighbor conditions" in axiom)
    checks.check("source-admissibility-continuum",
                 "reading note (3): a supported point may have zero singleton measure",
                 "On a continuous domain, a supported exact point may have zero singleton measure"
                 in axiom and '"available"/"admissible" denotes its support' in axiom)
    checks.check("source-record",
                 "Record: a record locks one admissible possibility; only records are readable",
                 "When present, a record locks exactly one admissible local possibility" in axiom
                 and "Only records are readable" in axiom)
    checks.check("source-parent-frame-import",
                 "the 2026-08-09 parent names the dimension-three frame theorem",
                 "Every nonnegative weight-one frame function on a complex Hilbert space of "
                 "dimension at least three is represented by a unique density operator" in parent)
    checks.check("surface-status",
                 "the note keeps its conditional surface and independent audit explicit",
                 all(s in note for s in ("actual_current_surface_status: conditional-support",
                                         "audit_required_before_effective_retained: true",
                                         "no canonical axiom edit",
                                         "Independent audit remains required")))

    print("per_element: every direction, plane, resolution, support and rank row is declared")
    print("per_site: one M_2(C) site under a Z^3 nearest-neighbour law; no wider carrier")
    print("per_mode: sphere polynomials through degree five and circle Fourier modes 1, 3 and 5")
    print("per_block: the law, the fibration, the fibred law, the certificates, the counterexamples")
    print("lattice_wide: one condition family for covariance only; no lattice-wide Born claim")
    print(f"runtime_seconds: {time.time() - started:.1f}")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
