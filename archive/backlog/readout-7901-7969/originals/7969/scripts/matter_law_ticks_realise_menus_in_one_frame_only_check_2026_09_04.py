#!/usr/bin/env python3
"""Exact checks for the note on the menus the designed matter law's own ticks realise.

Class A throughout: every printed check is an exact identity, an exact complete
census over a declared condition family, or an exact rank certificate over `Q`.
No seed is used anywhere and no condition family is sampled: each is either a
complete enumeration or a list written out in this file.  The only floating
point is the two labelled cross-checks against the many-body sea and against the
numerical spectral projector; no support and no odds value is ever read from a
float.

The runner is self-contained.  Every computational block is copied from the
source computation of the probe this note lands, and each copy names its source:

  * `QF`, `qf_det`                      -- `b6_common.py:14-60`, exact `Q(sqrt m)`
    arithmetic on `fractions.Fraction` pairs and the Gaussian determinant.
  * `cluster`, `face_flux`              -- `b6_common.py:62-115`, the T2 geometry
    conventions (vertex `(x,y,z) -> (x*Ly+y)*Lz+z`, edges sorted by `(i,j)`,
    Kawamoto-Smit signs, flux `-1` on every face).
  * `exact_kernel`, `kernel_checks`     -- `b6_common.py:117-160`, the exact
    one-particle kernel `K = P_W` of the half-filled sea and its identities.
  * `corner_law`                        -- `b6_common.py:163-181`, the exact
    determinantal corner law `p(n) = det(diag(n) K + diag(1-n)(I-K))`.
  * `f2_rank`, `f2_basis`, `f2_reduce`, `f2_span`, `wht`, `all_corner_patterns`,
    `common_denominator`, `qf_to_int_arrays`, `popcount_parity_table`
                                        -- `b6_common.py:183-273`, the `F2` and
    Walsh-Hadamard layer behind the record law `P(w) = 2^-g p(A w)`.
  * `Law`, `unit_patterns`, `canonical_odds`, `census`, `explicit_odds`
                                        -- `b6_census.py:12-140`, the coset-class
    census engine and the exact canonicalisation of odds vectors in `Z[sqrt m]`.
  * `sea_cube`                          -- the BKSF sea builder of `b6_law.py`'s
    read-only cross-check import, `L3/l3_core.py:27-116` (`P`, `pact`, the
    route-B `A`, `B`, `loop`, `record`, `hop_pauli`, `hop_amp`, `code_space`)
    and `L3j/l3j_core.py:34-108` (staggered signs, `H`, the code space, the sea).
  * `torus_family`, `torus_family_sub`  -- `b6_torus.py:38-120`, the closure
    marginal with the Schur-complement kernel on the `4^3` torus, with the
    inversion removed: on every declared family the formed corners `T` lie in one
    sublattice, where `K_TT = I/2` makes `M_TT = I/2` exactly, so
    `K' = K_RR - 2 K_RT D K_TR`.  The runner checks `M_TT = I/2` before using it.
  * `int_rank`                          -- `b6_born.py:13-28` (`rref`), the exact
    elimination over `Q`, run fraction-free on integer rows.
  * `structural`                        -- `b6_extra.py:20-93`, particle-hole
    symmetry, matching invariance, the even-sublattice marginal, and closure
    against uniformity along the class tick.

Reductions, declared.  Three of the source's complete censuses run over millions
of conditions and are reduced here to declared sub-families; their complete
counts are quoted in the note and not recomputed:
  * the slab column pair over all `3^14` conditions (`11405` menus, `95631` odds
    vectors) -> the class tick's own conditions, complete;
  * the slab degree-4 star over all `3^16` conditions (`1093` menus, `358125`
    odds vectors) -> the class tick's own conditions, complete;
  * the `4^3` torus family T6 over `2097152` condition classes (float64 census,
    `21656` menus) -> the exact declared sub-family, complete.
"""

import itertools
import math
import re
from fractions import Fraction as Fr
from functools import reduce
from pathlib import Path

import numpy as np

AUDIT_TIMEOUT_SEC = 300

ROOT = Path(__file__).resolve().parents[1]
NOTE_NAME = (
    "THE_MATTER_LAWS_OWN_TICKS_REALISE_MENUS_IN_ONE_FRAME_ONLY_THE_GLOBAL_CLAUSE_IS_"
    "REFUTED_BY_THE_SUPPORTS_THE_FIBRED_CLAUSE_IS_AN_IDENTITY_AND_ABUNDANCE_IS_"
    "UNPAID_BOUNDED_NOTE_2026-09-04.md"
)
NOTE_PATH = ROOT / "docs" / NOTE_NAME
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/THE_MATTER_LAWS_OWN_TICKS_REALISE_MENUS_IN_ONE_FRAME_ONLY_THE_GLOBAL_CLAUSE_IS_"
    "REFUTED_BY_THE_SUPPORTS_THE_FIBRED_CLAUSE_IS_AN_IDENTITY_AND_ABUNDANCE_IS_UNPAID_"
    "BOUNDED_NOTE_2026-09-04.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


def normalize(text):
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


# ------------------------------------------------- b6_common.py:14-60, Q(sqrt m)
class QF:
    """a + b*sqrt(m), a and b Fractions; m squarefree (1 allowed: plain rationals)."""

    __slots__ = ("a", "b", "m")

    def __init__(self, a, b=0, m=2):
        self.a = Fr(a)
        self.b = Fr(b)
        self.m = m

    def _c(self, o):
        return o if isinstance(o, QF) else QF(o, 0, self.m)

    def __add__(s, o):
        o = s._c(o)
        return QF(s.a + o.a, s.b + o.b, s.m)

    __radd__ = __add__

    def __sub__(s, o):
        o = s._c(o)
        return QF(s.a - o.a, s.b - o.b, s.m)

    def __rsub__(s, o):
        o = s._c(o)
        return QF(o.a - s.a, o.b - s.b, s.m)

    def __neg__(s):
        return QF(-s.a, -s.b, s.m)

    def __mul__(s, o):
        o = s._c(o)
        return QF(s.a * o.a + s.m * s.b * o.b, s.a * o.b + s.b * o.a, s.m)

    __rmul__ = __mul__

    def inv(s):
        d = s.a * s.a - s.m * s.b * s.b
        if d == 0:
            raise ZeroDivisionError("QF inverse of zero")
        return QF(s.a / d, -s.b / d, s.m)

    def __eq__(s, o):
        o = s._c(o)
        return s.a == o.a and s.b == o.b

    def __hash__(s):
        return hash((s.a, s.b, s.m))

    def iszero(s):
        return s.a == 0 and s.b == 0

    def __float__(s):
        return float(s.a) + float(s.b) * math.sqrt(s.m)


def qf_det(M, m):
    """exact determinant of a square list-of-lists of QF (Gaussian elimination)."""
    n = len(M)
    A = [row[:] for row in M]
    det = QF(1, 0, m)
    for c in range(n):
        piv = next((r for r in range(c, n) if not A[r][c].iszero()), None)
        if piv is None:
            return QF(0, 0, m)
        if piv != c:
            A[c], A[piv] = A[piv], A[c]
            det = -det
        det = det * A[c][c]
        inv = A[c][c].inv()
        for r in range(c + 1, n):
            if A[r][c].iszero():
                continue
            f = A[r][c] * inv
            Ar = A[r]
            Ac = A[c]
            for k in range(c, n):
                Ar[k] = Ar[k] - f * Ac[k]
    return det


# ------------------------------------------- b6_common.py:62-115, T2's geometry
def cluster(Lx, Ly, Lz, periodic=(False, False, False), twist=(0, 0, 0)):
    L = (Lx, Ly, Lz)
    idx = {}
    for x in range(Lx):
        for y in range(Ly):
            for z in range(Lz):
                idx[(x, y, z)] = (x * Ly + y) * Lz + z
    V = Lx * Ly * Lz
    E = []
    for (x, y, z) in idx:
        p = (x, y, z)
        for a in range(3):
            q = list(p)
            q[a] += 1
            wrap = False
            if q[a] == L[a]:
                if periodic[a] and L[a] > 2:
                    q[a] = 0
                    wrap = True
                else:
                    continue
            q = tuple(q)
            eta = 1 if a == 0 else ((-1) ** x if a == 1 else (-1) ** (x + y))
            if wrap and twist[a]:
                eta = -eta
            i, j = idx[p], idx[q]
            E.append((min(i, j), max(i, j), a, eta))
    E.sort(key=lambda t: (t[0], t[1]))
    EDGES = [(i, j) for (i, j, a, s) in E]
    eta = [s for (i, j, a, s) in E]
    coords = {v: k for k, v in idx.items()}

    def nxt(c, a):
        v = list(c)
        v[a] += 1
        if v[a] == L[a]:
            if periodic[a] and L[a] > 2:
                v[a] = 0
            else:
                return None
        return tuple(v)

    FACES = set()
    for c in idx:
        for a, b in itertools.combinations(range(3), 2):
            p1 = nxt(c, a)
            p2 = nxt(c, b)
            if p1 is None or p2 is None:
                continue
            p3 = nxt(p1, b)
            if p3 is None or p3 != nxt(p2, a):
                continue
            cyc = (idx[c], idx[p1], idx[p3], idx[p2])
            if len(set(cyc)) == 4:
                FACES.add(cyc)
    FACES = sorted(FACES)
    h = [[0] * V for _ in range(V)]
    for q, (i, j) in enumerate(EDGES):
        h[i][j] = h[j][i] = -eta[q]
    sub = [sum(coords[v]) % 2 for v in range(V)]
    cls = [
        (coords[v][0] % 2) * 4 + (coords[v][1] % 2) * 2 + (coords[v][2] % 2)
        for v in range(V)
    ]
    STAR = {v: [q for q, (i, j) in enumerate(EDGES) if v in (i, j)] for v in range(V)}
    EIDX = {}
    for q, (i, j) in enumerate(EDGES):
        EIDX[(i, j)] = EIDX[(j, i)] = q
    COL = [(1 << i) | (1 << j) for (i, j) in EDGES]
    return dict(
        L=L, V=V, E=len(EDGES), EDGES=EDGES, eta=eta, FACES=FACES, h=h, coords=coords,
        idx=idx, sub=sub, cls=cls, STAR=STAR, EIDX=EIDX, COL=COL,
    )


def face_flux(C):
    out = []
    for cyc in C["FACES"]:
        f = 1
        for t in range(4):
            f *= C["eta"][C["EIDX"][(cyc[t], cyc[(t + 1) % 4])]]
        out.append(f)
    return out


# ------------------------------------ b6_common.py:117-160, the exact kernel
def matmul_int(A, B):
    n = len(A)
    k = len(B)
    mm = len(B[0])
    return [[sum(A[i][t] * B[t][j] for t in range(k)) for j in range(mm)] for i in range(n)]


def exact_kernel(C):
    """K = P_W exactly: flat case h^2 = d I, and spec(h^2) = {2,4} for the slab."""
    V = C["V"]
    h = C["h"]
    h2 = matmul_int(h, h)
    diag = [h2[i][i] for i in range(V)]
    off = [(i, j) for i in range(V) for j in range(V) if i != j and h2[i][j] != 0]
    if not off and len(set(diag)) == 1:
        d = diag[0]
        sq = 1
        rest = d
        for p in (2, 3, 5, 7, 11, 13):
            while rest % (p * p) == 0:
                rest //= p * p
                sq *= p
        m = rest
        inv_sqrt_d = QF(0, Fr(1, sq * m), m)
        K = [
            [
                QF(Fr(1, 2) if i == j else 0, 0, m) - inv_sqrt_d * QF(Fr(h[i][j], 2), 0, m)
                for j in range(V)
            ]
            for i in range(V)
        ]
        return K, m, "flat h^2 = %dI" % d
    h4 = matmul_int(h2, h2)
    ok = all(
        (h4[i][j] - 6 * h2[i][j] + (8 if i == j else 0)) == 0
        for i in range(V)
        for j in range(V)
    )
    assert ok, "h^2 does not satisfy (x-2)(x-4) = 0"
    m = 2
    S = [
        [
            QF(
                Fr(h2[i][j] - (2 if i == j else 0), 4),
                Fr((4 if i == j else 0) - h2[i][j], 4),
                2,
            )
            for j in range(V)
        ]
        for i in range(V)
    ]
    hS = [
        [sum((S[t][j] * h[i][t] for t in range(V)), QF(0, 0, 2)) for j in range(V)]
        for i in range(V)
    ]
    K = [
        [(QF(1 if i == j else 0, 0, 2) - hS[i][j]) * QF(Fr(1, 2), 0, 2) for j in range(V)]
        for i in range(V)
    ]
    return K, m, "spec(h^2) = {2,4}"


def kernel_checks(C, K, m):
    """exact: K = K^T, K^2 = K, tr K = V/2, [h, K] = 0, K_AA = K_BB = I/2."""
    V = C["V"]
    sub = C["sub"]
    h = C["h"]
    sym = all(K[i][j] == K[j][i] for i in range(V) for j in range(V))
    K2 = [
        [sum((K[i][t] * K[t][j] for t in range(V)), QF(0, 0, m)) for j in range(V)]
        for i in range(V)
    ]
    idem = all(K2[i][j] == K[i][j] for i in range(V) for j in range(V))
    tr = sum((K[i][i] for i in range(V)), QF(0, 0, m))
    hK = [
        [sum((K[t][j] * h[i][t] for t in range(V)), QF(0, 0, m)) for j in range(V)]
        for i in range(V)
    ]
    Kh = [
        [sum((K[i][t] * h[t][j] for t in range(V)), QF(0, 0, m)) for j in range(V)]
        for i in range(V)
    ]
    comm = all(hK[i][j] == Kh[i][j] for i in range(V) for j in range(V))
    half = all(
        K[i][j] == (QF(Fr(1, 2), 0, m) if i == j else QF(0, 0, m))
        for i in range(V)
        for j in range(V)
        if sub[i] == sub[j]
    )
    return dict(sym=sym, idem=idem, trace=tr, comm=comm, half=half)


# --------------------------- b6_common.py:163-273, corner law, F2, Walsh-Hadamard
def corner_law(K, m, S=None):
    V = len(K)
    S = list(range(V)) if S is None else list(S)
    k = len(S)
    out = {}
    for n in range(1 << k):
        M = []
        for a in range(k):
            i = S[a]
            occ = (n >> a) & 1
            row = []
            for b in range(k):
                j = S[b]
                if occ:
                    row.append(K[i][j])
                else:
                    row.append((QF(1, 0, m) if i == j else QF(0, 0, m)) - K[i][j])
            M.append(row)
        out[n] = qf_det(M, m)
    return out


def f2_rank(cols):
    basis = []
    for v in cols:
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
    return len(basis)


def f2_basis(vectors):
    basis = []
    for v in vectors:
        for pb, b in basis:
            if (v >> pb) & 1:
                v ^= b
        if v:
            pb = v.bit_length() - 1
            basis = [(p, (b ^ v) if (b >> pb) & 1 else b) for p, b in basis]
            basis.append((pb, v))
            basis.sort(reverse=True)
    return basis


def f2_reduce(v, basis):
    for pb, b in basis:
        if (v >> pb) & 1:
            v ^= b
    return v


def f2_span(basis):
    vals = np.zeros(1, dtype=np.int64)
    for pb, b in basis:
        vals = np.concatenate([vals, vals ^ np.int64(b)])
    return vals


def all_corner_patterns(C):
    out = np.zeros(1, dtype=np.int64)
    for q in range(C["E"]):
        out = np.concatenate([out, out ^ np.int64(C["COL"][q])])
    return out


def wht(x):
    y = np.array(x, copy=True)
    n = y.shape[0]
    hh = 1
    while hh < n:
        y = y.reshape(-1, 2, hh)
        a = y[:, 0, :].copy()
        b = y[:, 1, :].copy()
        y[:, 0, :] = a + b
        y[:, 1, :] = a - b
        y = y.reshape(n)
        hh *= 2
    return y


def common_denominator(vals):
    D = 1
    for v in vals:
        D = D * v.a.denominator // math.gcd(D, v.a.denominator)
        D = D * v.b.denominator // math.gcd(D, v.b.denominator)
    return D


def qf_to_int_arrays(law, nbits, D):
    a = np.zeros(1 << nbits, dtype=np.int64)
    b = np.zeros(1 << nbits, dtype=np.int64)
    for n, v in law.items():
        na = v.a * D
        nb = v.b * D
        assert na.denominator == 1 and nb.denominator == 1
        a[n] = int(na.numerator)
        b[n] = int(nb.numerator)
    return a, b


def popcount_parity_table(nbits):
    t = np.zeros(1 << nbits, dtype=np.int64)
    for i in range(1, 1 << nbits):
        t[i] = t[i >> 1] ^ (i & 1)
    return t


# ------------------------------------ b6_census.py:12-140, the census engine
class Law:
    def __init__(self, C, m, D, g, pa, pb, law=None):
        self.C = C
        self.V = C["V"]
        self.E = C["E"]
        self.m = m
        self.D = D
        self.g = g
        self.pa = pa
        self.pb = pb
        self.law = law
        self.WA = wht(pa)
        self.WB = wht(pb)
        self.PT = popcount_parity_table(self.V)
        self.chi = np.arange(1 << self.V, dtype=np.int64)
        self.COL = C["COL"]
        self._qcache = {}

    def qF(self, F_mask):
        """exact q_F on all 2^V corner patterns for the free edge set F."""
        if F_mask in self._qcache:
            return self._qcache[F_mask]
        cols = [self.COL[e] for e in range(self.E) if (F_mask >> e) & 1]
        basis = f2_basis(cols)
        rF = len(basis)
        mask = np.ones(1 << self.V, dtype=bool)
        for pb, b in basis:
            mask &= self.PT[self.chi & np.int64(b)] == 0
        den = 1 << (self.V - rF)
        qa = wht(self.WA * mask)
        qb = wht(self.WB * mask)
        assert np.all(qa % den == 0) and np.all(qb % den == 0)
        qa //= den
        qb //= den
        res = (qa, qb, basis, rF)
        if len(self._qcache) < 4096:
            self._qcache[F_mask] = res
        return res


def unit_patterns(law, U):
    vals = np.zeros(1, dtype=np.int64)
    for e in U:
        vals = np.concatenate([vals, vals ^ np.int64(law.COL[e])])
    return vals


def canonical_odds(qa_row, qb_row, m):
    """exact canonical form of q/sum(q) in Q(sqrt m) as an integer tuple key."""
    A = int(sum(int(x) for x in qa_row))
    B = int(sum(int(x) for x in qb_row))
    N = A * A - m * B * B
    if N < 0:
        A, B, N = -A, -B, -N
    ap = []
    bp = []
    for a, b in zip(qa_row, qb_row):
        a = int(a)
        b = int(b)
        ap.append(a * A - m * b * B)
        bp.append(b * A - a * B)
    g = N
    for x in ap:
        g = math.gcd(g, x)
    for x in bp:
        g = math.gcd(g, x)
    return tuple(x // g for x in ap), tuple(x // g for x in bp), N // g


def census(law, U, cond_edges, kmax=None, kmin=0, tag_fn=None):
    """complete census over all R_0 subset cond_edges and all valid w_0, by cosets."""
    U = list(U)
    nU = unit_patterns(law, U)
    Umask = sum(1 << e for e in U)
    ALL = (1 << law.E) - 1
    cond_edges = [e for e in cond_edges if not (Umask >> e) & 1]
    kmax = len(cond_edges) if kmax is None else min(kmax, len(cond_edges))
    keys = {}
    perk = {}
    for k in range(kmin, kmax + 1):
        perk[k] = dict(conditions=0, classes=0, supports=set(), odds=set())
        for R0 in itertools.combinations(cond_edges, k):
            R0mask = sum(1 << e for e in R0)
            qa, qb, basisL, rF = law.qF(ALL & ~Umask & ~R0mask)
            reduced = [f2_reduce(law.COL[e], basisL) for e in R0]
            basisQ = f2_basis(reduced)
            reps = f2_span(basisQ)
            mult = 1 << (k - len(basisQ))
            idx = reps[:, None] ^ nU[None, :]
            QA = qa[idx]
            QB = qb[idx]
            nzero = (QA != 0) | (QB != 0)
            valid = np.any(nzero, axis=1)
            tag = tag_fn(R0mask) if tag_fn is not None else None
            for r in np.flatnonzero(valid):
                supp = 0
                for w in np.flatnonzero(nzero[r]):
                    supp |= 1 << int(w)
                key = (supp,) + canonical_odds(QA[r], QB[r], law.m)
                st = keys.get(key)
                if st is None:
                    st = dict(count=0, ks=set(), tags=set())
                    keys[key] = st
                st["count"] += mult
                st["ks"].add(k)
                if tag is not None:
                    st["tags"] |= tag
                perk[k]["conditions"] += mult
                perk[k]["classes"] += 1
                perk[k]["supports"].add(supp)
                perk[k]["odds"].add(key)
    return dict(U=U, keys=keys, perk=perk)


def explicit_odds(law, U, R0, w0):
    """exact odds for one explicit condition: records w0 on the edges R0."""
    U = list(U)
    nU = unit_patterns(law, U)
    Umask = sum(1 << e for e in U)
    R0mask = sum(1 << e for e in R0)
    ALL = (1 << law.E) - 1
    qa, qb, basisL, rF = law.qF(ALL & ~Umask & ~R0mask)
    n0 = 0
    for e, b in zip(R0, w0):
        if b:
            n0 ^= law.COL[e]
    idx = np.int64(n0) ^ nU
    QA = qa[idx]
    QB = qb[idx]
    if not np.any((QA != 0) | (QB != 0)):
        return None
    supp = 0
    for w in np.flatnonzero((QA != 0) | (QB != 0)):
        supp |= 1 << int(w)
    return (supp,) + canonical_odds(QA, QB, law.m)


def odds_str(key, m):
    ap, bp, N = key
    out = []
    for a, b in zip(ap, bp):
        if a == 0 and b == 0:
            out.append("0")
            continue
        fa = Fr(a, N)
        fb = Fr(b, N)
        if fb == 0:
            out.append(str(fa))
        elif fa == 0:
            out.append("%s*sqrt%d" % (fb, m))
        else:
            out.append("(%s + %s*sqrt%d)" % (fa, fb, m))
    return "[" + ", ".join(out) + "]"


def is_uniform(key):
    nz = set((a, b) for a, b in zip(key[1], key[2]) if (a, b) != (0, 0))
    return len(nz) == 1


def sizes_of(supports):
    d = {}
    for s in supports:
        d[bin(s).count("1")] = d.get(bin(s).count("1"), 0) + 1
    return dict(sorted(d.items()))


# --------- L3/l3_core.py:27-116 and L3j/l3j_core.py:34-108, the many-body sea
def pc(n):
    return bin(n).count("1")


class Pauli:
    """i^k * prod_q X_q^{x_q} Z_q^{z_q}  (X before Z on every qubit)."""

    __slots__ = ("k", "x", "z")

    def __init__(s, k, x, z):
        s.k = k % 4
        s.x = x
        s.z = z

    def __mul__(a, b):
        return Pauli(a.k + b.k + 2 * pc(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def neg(s):
        return Pauli(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def __hash__(s):
        return hash((s.k, s.x, s.z))


PHASE = [1 + 0j, 1j, -1 + 0j, -1j]


def pact(p, b):
    return b ^ p.x, PHASE[p.k] * ((-1) ** (pc(p.z & b) % 2))


def sea_cube(C):
    """the half-filled BKSF sea of the cube: returns (P_SEA, E_sea, gap, code_dim)."""
    V = C["V"]
    EDGES = C["EDGES"]
    NQ = len(EDGES)
    D = 1 << NQ
    EIDX = C["EIDX"]
    NBR = {i: sorted(set(j for (a, b) in EDGES for j in ((b,) if a == i else ((a,) if b == i else ())))) for i in range(V)}
    STARMASK = {i: reduce(lambda a, b: a | (1 << b), C["STAR"][i], 0) for i in range(V)}

    def A_unsigned(i, j):
        x = 1 << EIDX[(i, j)]
        z = 0
        for k in NBR[i]:
            if k != j and k < j:
                z ^= 1 << EIDX[(i, k)]
        for l in NBR[j]:
            if l != i and l < i:
                z ^= 1 << EIDX[(j, l)]
        return Pauli(pc(x & z) % 2, x, z)

    def Aop(i, j):
        p = A_unsigned(i, j)
        return p if i < j else p.neg()

    def Bop(i):
        return Pauli(0, 0, STARMASK[i])

    def loop(cyc):
        out = Pauli(0, 0, 0)
        for a in range(len(cyc)):
            out = out * Aop(cyc[a], cyc[(a + 1) % len(cyc)])
        return out

    grp = {Pauli(0, 0, 0)}
    gens = [loop(cyc) for cyc in C["FACES"]]
    changed = True
    while changed:
        changed = False
        for g in list(grp):
            for hgen in gens:
                p = g * hgen
                if p not in grp:
                    grp.add(p)
                    changed = True
    grp = list(grp)
    HAMP = np.zeros((NQ, D), dtype=np.complex128)
    for q, (i, j) in enumerate(EDGES):
        Aij = Aop(i, j)
        P1 = Aij * Bop(i)
        P2 = Aij * Bop(j)
        for z in range(D):
            b1, a1 = pact(P1, z)
            b2, a2 = pact(P2, z)
            v = 0.5j * (a1 - a2)
            HAMP[q, z] = -1.0 * C["eta"][q] * complex(round(v.real), round(v.imag))
    cid = -np.ones(D, dtype=np.int64)
    phi = np.zeros(D, dtype=complex)
    reps = []
    for z0 in range(D):
        if cid[z0] >= 0:
            continue
        c = len(reps)
        reps.append(z0)
        for g in grp:
            b, a = pact(g, z0)
            assert cid[b] < 0
            cid[b] = c
            phi[b] = a
    NC = len(reps)
    W = np.zeros((D, NC), dtype=np.complex128)
    W[np.arange(D), cid] = phi / np.sqrt(float(len(grp)))
    HW = np.zeros((D, NC), dtype=np.complex128)
    zz = np.arange(D)
    for c in range(NC):
        psi = W[:, c]
        out = np.zeros(D, dtype=np.complex128)
        for q in range(NQ):
            out[zz ^ (1 << q)] += HAMP[q] * psi
        HW[:, c] = out
    HC = W.conj().T @ HW
    EVC, VCC = np.linalg.eigh(HC)
    SEA = W @ VCC[:, 0]
    return SEA, float(EVC[0]), float(EVC[1] - EVC[0]), NC


# ------------------------- b6_torus.py:38-120, the closure marginal on the torus
def torus_family(C, K, m, v0, T, closed, star):
    """census of the star(v0) event over all n_T and all closure parities pi."""
    ZERO = QF(0, 0, m)
    ONE = QF(1, 0, m)
    HALF = QF(Fr(1, 2), 0, m)
    mtt_half = all(
        K[T[a]][T[b]] == (HALF if a == b else ZERO)
        for a in range(len(T))
        for b in range(len(T))
    )
    assert mtt_half, "M_TT = I/2 fails; the inversion-free Schur step does not apply"
    Rset = [v0] + closed
    k = len(Rset)
    c = len(closed)
    PA = [[[K[i][T[a]] * K[T[a]][j] for j in Rset] for i in Rset] for a in range(len(T))]
    ce = [C["EIDX"][(v0, u)] for u in closed]
    cpos = [star.index(q) for q in ce]
    Wp = np.arange(64)
    par = np.array([bin(w).count("1") & 1 for w in Wp])
    cbits = np.zeros(64, dtype=np.int64)
    for a, p in enumerate(cpos):
        cbits |= ((Wp >> p) & 1) << a
    keys = {}
    for nTint in range(1 << len(T)):
        Kp = [[K[i][j] for j in Rset] for i in Rset]
        for a in range(len(T)):
            plus = (nTint >> a) & 1
            for i in range(k):
                Pi = PA[a][i]
                oi = Kp[i]
                for j in range(k):
                    if Pi[j].iszero():
                        continue
                    oi[j] = oi[j] - Pi[j] - Pi[j] if plus else oi[j] + Pi[j] + Pi[j]
        lawR = []
        for n in range(1 << k):
            M = [
                [
                    (Kp[i][j] if (n >> i) & 1 else ((ONE - Kp[i][j]) if i == j else -Kp[i][j]))
                    for j in range(k)
                ]
                for i in range(k)
            ]
            lawR.append(qf_det(M, m))
        for pi in range(1 << c):
            vals = []
            for w in range(64):
                n = int(par[w])
                for a in range(c):
                    n |= (((pi >> a) & 1) ^ ((int(cbits[w]) >> a) & 1)) << (1 + a)
                vals.append(lawR[n])
            if all(x.iszero() for x in vals):
                continue
            Dd = common_denominator(vals)
            supp = sum(1 << w for w in range(64) if not vals[w].iszero())
            key = (supp,) + canonical_odds(
                [int(x.a * Dd) for x in vals], [int(x.b * Dd) for x in vals], m
            )
            keys[key] = keys.get(key, 0) + 1
    return keys


# ---------------------------------- b6_born.py:13-28 (rref), exact over Q
def int_rank(rows, ncols):
    """exact rank over Q of integer rows, fraction-free with gcd normalisation."""
    piv = []
    for r in rows:
        r = list(r)
        for pcol, prow in piv:
            if r[pcol]:
                a = prow[pcol]
                b = r[pcol]
                r = [a * x - b * y for x, y in zip(r, prow)]
                g = 0
                for x in r:
                    g = math.gcd(g, x)
                if g > 1:
                    r = [x // g for x in r]
        pcol = next((j for j in range(ncols) if r[j]), None)
        if pcol is not None:
            piv.append((pcol, r))
    return len(piv)


def global_clause(menus, n):
    """(G): rank of the incidence system sum_{w in M} g_w = 1 and of its augment."""
    rows = [[1 if (M >> w) & 1 else 0 for w in range(n)] for M in sorted(menus)]
    rA = int_rank(rows, n)
    rAug = int_rank([r + [1] for r in rows], n + 1)
    return rA, rAug, rAug > rA


def disjoint_witness(menus):
    """two disjoint realised menus, smallest first (the elementary refutation)."""
    Ms = sorted(menus, key=lambda M: bin(M).count("1"))
    for A, B in itertools.combinations(Ms, 2):
        if A & B == 0:
            return A, B
    return None


# ======================================================================= checks
def build(C, do_law=True):
    K, m, desc = exact_kernel(C)
    chk = kernel_checks(C, K, m)
    R = dict(C=C, K=K, m=m, desc=desc, chk=chk)
    if not do_law:
        return R
    law = corner_law(K, m)
    D = common_denominator(list(law.values()))
    pa, pb = qf_to_int_arrays(law, C["V"], D)
    g = C["E"] - f2_rank(C["COL"])
    npat = all_corner_patterns(C)
    R.update(
        law=law, D=D, pa=pa, pb=pb, g=g, npat=npat,
        support=int(np.sum((pa[npat] != 0) | (pb[npat] != 0))),
        nz=[n for n, v in law.items() if not v.iszero()],
    )
    return R


def t1(ck, cube, slab, torus):
    C = cube["C"]
    m = cube["m"]
    ck.check("T1-cube-geom", "cube 2x2x2: 8 corners, 12 sites, flux -1 on all 6 faces",
             C["V"] == 8 and C["E"] == 12 and set(face_flux(C)) == {-1} and len(C["FACES"]) == 6)
    ck.check("T1-cube-kernel", "h^2 = 3I and K = (I - h/sqrt3)/2 exact in Q(sqrt3)",
             cube["desc"] == "flat h^2 = 3I" and m == 3)
    chk = cube["chk"]
    ck.check("T1-cube-ident", "exactly K = K^T = K^2, tr K = 4, [h,K] = 0",
             chk["sym"] and chk["idem"] and chk["comm"] and chk["trace"] == QF(4, 0, m))
    ck.check("T1-cube-half", "K_AA = K_BB = I/2 exactly on the cube", chk["half"])
    law = cube["law"]
    tot = sum(law.values(), QF(0, 0, m))
    ck.check("T1-cube-corner", "corner law: 256 patterns, 62 nonzero, |n| = 4, sum 1, D = 144",
             len(law) == 256 and len(cube["nz"]) == 62 and cube["D"] == 144
             and all(bin(n).count("1") == 4 for n in cube["nz"]) and tot == QF(1, 0, m))
    vals = sorted(set(law[n] for n in cube["nz"]), key=float)
    ck.check("T1-cube-values", "rational: no sqrt3 part; values {1/144,1/48,1/36,1/16}",
             all(law[n].b == 0 for n in cube["nz"])
             and [v.a for v in vals] == [Fr(1, 144), Fr(1, 48), Fr(1, 36), Fr(1, 16)])
    canc = sorted(n for n in range(256) if bin(n).count("1") == 4 and law[n].iszero())
    closed = sorted(
        sum(1 << u for u in [v] + [j if i == v else i for (i, j) in C["EDGES"] if v in (i, j)])
        for v in range(8)
    )
    ck.check("T1-cube-zeros", "the 8 cancellation zeros are the closed corner stars",
             canc == closed)
    ck.check("T1-cube-record", "P(w) = 2^-5 p(Aw): support 1984 = 32 x 62 on 4096 labels",
             cube["g"] == 5 and cube["support"] == 1984)
    SEA, E, gap, ncode = sea_cube(C)
    P_SEA = np.abs(SEA) ** 2
    Pex = cube["pa"][cube["npat"]] / cube["D"] / 2 ** cube["g"]
    dev = float(np.max(np.abs(Pex - P_SEA)))
    ck.check("T1-cube-sea", "float: code dim 128, E = -4 sqrt3, max|P_ex - P_SEA| = %.1e < 4e-18" % dev,
             ncode == 128 and abs(E + 4 * math.sqrt(3)) < 1e-12 and dev < 4e-18)
    ck.check("T1-slab-kernel", "slab 2x2x3: spec(h^2) = {2,4}, K in Q(sqrt2), K_AA = K_BB = I/2",
             slab["desc"] == "spec(h^2) = {2,4}" and slab["m"] == 2 and slab["chk"]["half"]
             and slab["chk"]["sym"] and slab["chk"]["idem"] and slab["chk"]["comm"])
    ls = slab["law"]
    irr = sum(1 for n in slab["nz"] if ls[n].b != 0)
    ck.check("T1-slab-corner", "corner law: 4096 patterns, 804 nonzero, |n| = 6, D = 8192, 392 irrat.",
             len(ls) == 4096 and len(slab["nz"]) == 804 and slab["D"] == 8192 and irr == 392
             and all(bin(n).count("1") == 6 for n in slab["nz"])
             and sum(ls.values(), QF(0, 0, 2)) == QF(1, 0, 2)
             and len(set(ls[n] for n in slab["nz"])) == 23)
    ck.check("T1-slab-record", "P(w) = 2^-9 p(Aw): support 411648 = 512 x 804",
             slab["g"] == 9 and slab["support"] == 411648 and 512 * 804 == 411648)
    Ct = torus["C"]
    h2 = matmul_int(Ct["h"], Ct["h"])
    ck.check("T1-torus", "4^3 torus twist (1,1,1): 192 sites, flux -1, h^2 = 6I, K in Q(sqrt6)",
             Ct["E"] == 192 and set(face_flux(Ct)) == {-1} and torus["m"] == 6
             and all(h2[i][j] == (6 if i == j else 0) for i in range(64) for j in range(64)))
    ck.check("T1-torus-half", "K_AA = K_BB = I/2 exactly on the 4^3 torus, and tr K = 32",
             torus["chk"]["half"] and torus["chk"]["trace"] == QF(32, 0, 6)
             and torus["chk"]["sym"] and torus["chk"]["idem"])
    return SEA, P_SEA


def t2(ck, cube, slab, lawc, laws):
    C = cube["C"]

    def nn_edges(CC, q):
        i, j = CC["EDGES"][q]
        return sorted(set(CC["STAR"][i] + CC["STAR"][j]) - {q})

    perk = {}
    allkeys = {}
    nn_keys = set()
    for q in range(12):
        nn = nn_edges(C, q)
        nnmask = sum(1 << e for e in nn)
        res = census(lawc, [q], [e for e in range(12) if e != q], kmax=None,
                     tag_fn=lambda M, nm=nnmask: frozenset(["NN"]) if M & ~nm == 0 else frozenset())
        for k, d in res["perk"].items():
            a = perk.setdefault(k, dict(conditions=0, supports=set(), odds=set()))
            a["conditions"] += d["conditions"]
            a["supports"] |= d["supports"]
            a["odds"] |= d["odds"]
        for key, st in res["keys"].items():
            s = allkeys.setdefault(key, set())
            s |= st["ks"]
            if "NN" in st["tags"]:
                nn_keys.add(key)
    counts = [perk[k]["conditions"] for k in range(12)]
    ck.check("T2-cube-table", "all 3^11 conditions per site: 12/264/.../17664 by k, 2105028 total",
             counts == [12, 264, 2640, 15840, 63360, 177408, 354816, 506880, 506880,
                        336384, 122880, 17664] and sum(counts) == 2105028)
    supports = set(k[0] for k in allkeys)
    ck.check("T2-cube-menus", "3 menus over every site and condition: {P0,P1}, {P0}, {P1}; 129 odds",
             supports == {1, 2, 3} and len(allkeys) == 129)
    first = min(k for key, ks in allkeys.items() if key[0] in (1, 2) for k in ks)
    ck.check("T2-cube-forcing", "no singleton menu through k = 7; the first forcing is at k = 8",
             first == 8 and all(perk[k]["supports"] == {3} for k in range(8)))
    supp = np.flatnonzero(cube["pa"][cube["npat"]] != 0)
    blocks = []
    for k in range(4):
        b = 0
        for R0 in itertools.combinations(range(12), k):
            seen = set()
            for z in supp:
                seen.add(tuple((int(z) >> e) & 1 for e in R0))
            b += len(seen)
        blocks.append(b)
    ck.check("T2-control-blocks", "PR #7919's nonzero record blocks at k = 0..3: 1 / 24 / 264 / 1760",
             blocks == [1, 24, 264, 1760])
    v3 = sorted(set(Fr(key[1][0], key[3]) for key in perk[3]["odds"]))
    ck.check("T2-control-odds", "its five odds at k = 3: {5/18, 1/3, 1/2, 2/3, 13/18}",
             v3 == [Fr(5, 18), Fr(1, 3), Fr(1, 2), Fr(2, 3), Fr(13, 18)]
             and all(len(perk[k]["odds"]) == 1 for k in (0, 1, 2)))
    key = explicit_odds(lawc, [9], [0, 1, 2, 3, 4, 5, 6, 8], [0] * 8)
    ck.check("T2-control-witness", "its witness: records 0 on edges 0..6 and 8 lock edge 9 to [0,1]",
             key is not None and key[0] == 2 and odds_str(key[1:], 3) == "[0, 1]")
    ck.check("T2-cube-nn", "Lemma 5: NN-only conditions give one menu, one odds [1/2,1/2]",
             len(nn_keys) == 1 and next(iter(nn_keys))[0] == 3)
    ntot = 0
    nviol = 0
    worst = Fr(0)
    ALL = (1 << 12) - 1
    for q in range(12):
        nn = nn_edges(C, q)
        far = [e for e in range(12) if e != q and e not in nn]
        nU = unit_patterns(lawc, [q])
        byNN = {}
        for kf in range(len(far) + 1):
            for Rf in itertools.combinations(far, kf):
                R0 = list(nn) + list(Rf)
                qa, qb, bl, rF = lawc.qF(ALL & ~(1 << q) & ~sum(1 << e for e in R0))
                n0 = np.zeros(1, dtype=np.int64)
                for e in R0:
                    n0 = np.concatenate([n0, n0 ^ np.int64(lawc.COL[e])])
                idx = n0[:, None] ^ nU[None, :]
                QA = qa[idx]
                QB = qb[idx]
                nz = (QA != 0) | (QB != 0)
                for r in np.flatnonzero(np.any(nz, axis=1)):
                    supp2 = int(nz[r, 0]) | (int(nz[r, 1]) << 1)
                    byNN.setdefault(r & 0xF, set()).add(
                        (supp2,) + canonical_odds(QA[r], QB[r], lawc.m))
        for wnn, ks in byNN.items():
            ntot += 1
            if len(ks) > 1:
                nviol += 1
                fl = [Fr(k2[1][0], k2[3]) for k2 in ks]
                worst = max(worst, max(fl) - min(fl))
    ck.check("T2-cube-markov", "all 192 (site, NN pattern) pairs vary with far records, spread 1",
             ntot == 192 and nviol == 192 and worst == 1)
    skeys = set()
    for q in range(20):
        res = census(laws, [q], [e for e in range(20) if e != q], kmax=4)
        skeys |= set(res["keys"])
    k4 = len(skeys)
    for q in range(20):
        skeys |= set(census(laws, [q], nn_edges(slab["C"], q))["keys"])
    Cs = slab["C"]
    cls = {"even": [[4], [7], [0, 2], [9, 11]], "odd": [[1], [10], [3, 5], [6, 8]]}
    for cl in cls.values():
        for t in range(1, 4):
            for T in itertools.combinations(range(4), t):
                R0 = sorted(set(e for c in T for v in cl[c] for e in Cs["STAR"][v]))
                for q in [x for x in range(20) if x not in R0]:
                    r2 = census(laws, [q], R0, kmin=len(R0))
                    skeys |= r2["perk"][len(R0)]["odds"]
    ck.check("T2-slab-site", "slab sites (k <= 4, NN, whole-class): one menu, 73 odds, no forcing",
             k4 == 7 and len(skeys) == 73 and set(k[0] for k in skeys) == {3})
    return allkeys


def t3(ck, cube, slab, lawc, laws):
    C = cube["C"]
    agg = {}
    for v in range(8):
        U = C["STAR"][v]
        nn = sorted(set(e for q in U for i in C["EDGES"][q] for e in C["STAR"][i]) - set(U))
        nnmask = sum(1 << e for e in nn)
        res = census(lawc, U, [e for e in range(12) if e not in U], kmax=None,
                     tag_fn=lambda M, nm=nnmask: frozenset(["NN"]) if M & ~nm == 0 else frozenset())
        for key, st in res["keys"].items():
            a = agg.setdefault(key, set())
            a |= st["tags"]
    sup = set(k[0] for k in agg)
    per = {}
    for k in agg:
        per.setdefault(k[0], 0)
        per[k[0]] += 1
    ck.check("T3-cube-star", "cube star, 8 corners complete over 3^9 conditions: 69 menus, 1329 odds",
             len(sup) == 69 and len(agg) == 1329)
    ck.check("T3-star-sizes", "sizes {4:8, 5:24, 6:28, 7:8, 8:1}: no three-outcome menu, one full basis",
             sizes_of(sup) == {4: 8, 5: 24, 6: 28, 7: 8, 8: 1} and sum(1 for s in sup if s == 255) == 1)
    ck.check("T3-star-odds", "37 of the 69 menus carry several odds, 849 on the full basis",
             sum(1 for s in per.values() if s > 1) == 37 and max(per.values()) == 849
             and per[255] == 849)
    nnk = set(k for k, tg in agg.items() if "NN" in tg)
    ck.check("T3-star-nn", "NN-only star conditions: 5 menus of sizes {6:4, 8:1}, 27 odds",
             sizes_of(set(k[0] for k in nnk)) == {6: 4, 8: 1} and len(nnk) == 27)
    ctick = tick_steps(lawc, [C["STAR"][v] for v in range(8) if C["sub"][v] == 0])
    ck.check("T3-cube-tick", "cube tick, 24 orders: menus 1/1/13/32, odds 1/1/18/32, uniform 1/1/0/0",
             [len(ctick[t]["supports"]) for t in (1, 2, 3, 4)] == [1, 1, 13, 32]
             and [len(ctick[t]["odds"]) for t in (1, 2, 3, 4)] == [1, 1, 18, 32]
             and [ctick[t]["uniform"] for t in (1, 2, 3, 4)] == [1, 1, 0, 0])
    Cs = slab["C"]

    def star_edges(S):
        return sorted(set(e for v in S for e in Cs["STAR"][v]))

    even = [[4], [7], [0, 2], [9, 11]]
    subfam = {}
    for S in ([0, 2], [4]):
        U = star_edges(S)
        keys = {}
        for r in range(4):
            for T in itertools.combinations([c for c in even if c != S], r):
                R0 = sorted(set(itertools.chain.from_iterable(star_edges(c) for c in T)))
                d = census(laws, U, R0, kmin=len(R0))["perk"][len(R0)]
                for k in d["odds"]:
                    keys[k] = 1
        subfam[tuple(S)] = keys
    pk = subfam[(0, 2)]
    sk = subfam[(4,)]
    ck.check("T3-slab-pair", "slab pair, the class tick's conditions: 421 menus, 423 odds, 1 uniform",
             len(set(k[0] for k in pk)) == 421 and len(pk) == 423
             and sum(1 for k in pk if is_uniform(k)) == 1
             and sizes_of(set(k[0] for k in pk)) == {19: 32, 25: 32, 31: 192, 32: 96,
                                                     44: 16, 56: 36, 60: 16, 64: 1})
    ck.check("T3-slab-star", "slab degree-4 star, same: 285 menus (sizes 5..16), 501 odds, 1 uniform",
             len(set(k[0] for k in sk)) == 285 and len(sk) == 501
             and sum(1 for k in sk if is_uniform(k)) == 1
             and sizes_of(set(k[0] for k in sk)) == {5: 16, 7: 112, 8: 8, 9: 112, 10: 16,
                                                     12: 12, 14: 8, 16: 1})
    stick = tick_steps(laws, [star_edges(c) for c in even])
    ck.check("T3-slab-tick", "slab tick, 24 orders: menus 2/2/166/960, odds 2/2/192/1152, uniform 2/2/0/0",
             [len(stick[t]["supports"]) for t in (1, 2, 3, 4)] == [2, 2, 166, 960]
             and [len(stick[t]["odds"]) for t in (1, 2, 3, 4)] == [2, 2, 192, 1152]
             and [stick[t]["uniform"] for t in (1, 2, 3, 4)] == [2, 2, 0, 0])
    return pk, sk, agg


def tick_steps(law, units):
    """the class tick in every order; per step the menus and odds vectors realised."""
    n = len(units)
    perstep = {}
    seen = set()
    for order in itertools.permutations(range(n)):
        for t in range(n):
            key = (tuple(sorted(order[:t])), order[t])
            if key in seen:
                continue
            seen.add(key)
            U = units[order[t]]
            R0 = sorted(e for s in order[:t] for e in units[s])
            d = census(law, U, R0, kmin=len(R0))["perk"][len(R0)]
            st = perstep.setdefault(t + 1, dict(supports=set(), odds=set()))
            st["supports"] |= d["supports"]
            st["odds"] |= d["odds"]
    for t in perstep:
        perstep[t]["uniform"] = sum(1 for k in perstep[t]["odds"] if is_uniform(k))
    return perstep


def lemma4(ck, cube, slab, lawc, laws):
    """closure against uniformity along the class tick, and the wrong predictor."""
    ok = True
    incol_ever = False
    for R, law, classes in ((cube, lawc, [[0], [3], [5], [6]]),
                            (slab, laws, [[4], [7], [0, 2], [9, 11]])):
        C = R["C"]
        E = C["E"]
        units = [sorted(set(e for v in S for e in C["STAR"][v])) for S in classes]
        seen = set()
        for order in itertools.permutations(range(4)):
            for t in range(4):
                key = (tuple(sorted(order[:t])), order[t])
                if key in seen:
                    continue
                seen.add(key)
                U = units[order[t]]
                R0 = sorted(e for s in order[:t] for e in units[s])
                F = [e for e in range(E) if e not in U and e not in R0]
                basisL = f2_basis([C["COL"][e] for e in F])
                incol_ever |= all(f2_reduce(C["COL"][e], basisL) == 0 for e in U)
                rec = set(R0) | set(U)
                formed = set(itertools.chain.from_iterable(classes[s] for s in order[:t + 1]))
                closes = any(
                    v not in formed and all(e in rec for e in C["STAR"][v]) for v in range(C["V"])
                )
                d = census(law, U, R0, kmin=len(R0))["perk"][len(R0)]
                full = (1 << (1 << len(U))) - 1
                uni = all(is_uniform(k) and k[0] == full for k in d["odds"])
                ok &= uni == (not closes)
        ck.check("T3-closure-%d" % C["V"], "Lemma 4 on 32 %s tick steps: a full uniform menu iff no corner closes"
                 % ("cube" if C["V"] == 8 else "slab"), ok)
    ck.check("T3-columns", "the 'unit columns in L_F' criterion holds at no step; closure does",
             not incol_ever)
    counts = {}
    for Lt in (6, 8):
        C6 = cluster(Lt, Lt, Lt, periodic=(True, True, True),
                     twist=(0, 0, 0) if Lt == 6 else (1, 1, 1))
        clsd = {}
        for v in range(C6["V"]):
            if C6["sub"][v] == 0:
                clsd.setdefault(C6["cls"][v], []).append(v)
        classes = [clsd[k] for k in sorted(clsd)]
        units = [sorted(set(e for v in S for e in C6["STAR"][v])) for S in classes]
        seen = set()
        per = {}
        for order in itertools.permutations(range(4)):
            for t in range(4):
                key = (tuple(sorted(order[:t])), order[t])
                if key in seen:
                    continue
                seen.add(key)
                rec = set(e for s in order[:t + 1] for e in units[s])
                per.setdefault(t + 1, set()).add(sum(
                    1 for v in range(C6["V"])
                    if C6["sub"][v] == 1 and all(e in rec for e in C6["STAR"][v])))
        counts[Lt] = ([sorted(per[t]) for t in (1, 2, 3, 4)], len(units[0]))
    ck.check("T3-bigtori", "6^3 / 8^3: 162 / 384 records per class; closure 0,0,27,108 / 0,0,64,256",
             counts[6] == ([[0], [0], [27], [108]], 162)
             and counts[8] == ([[0], [0], [64], [256]], 384))


def structural(ck, cube, slab):
    """b6_extra.py:20-93: particle-hole, matchings, the even-sublattice marginal."""
    out = []
    for R in (cube, slab):
        C = R["C"]
        V = C["V"]
        law = R["law"]
        ph = all(law[n] == law[n ^ ((1 << V) - 1)] for n in range(1 << V))
        matchings = 0
        inv = True
        for a in range(3):
            M = [q for q, (i, j) in enumerate(C["EDGES"]) if C["coords"][j][a] != C["coords"][i][a]]
            deg = [sum(1 for q in M if v in C["EDGES"][q]) for v in range(V)]
            if all(d == 1 for d in deg):
                matchings += 1
                xM = sum(1 << q for q in M)
                Z = np.arange(1 << C["E"])
                inv &= bool(np.array_equal(R["pa"][R["npat"]], R["pa"][R["npat"][Z ^ xM]]))
        A = [v for v in range(V) if C["sub"][v] == 0]
        mar = corner_law(R["K"], R["m"], S=A)
        uni = all(mar[n] == QF(Fr(1, 1 << len(A)), 0, R["m"]) for n in mar)
        i, j = C["EDGES"][0]
        pair = corner_law(R["K"], R["m"], S=[i, j])
        out.append((ph, matchings, inv, uni, pair[0] == pair[3]))
    ck.check("T3-lemma5", "particle-hole p(n) = p(1-n); matching invariance, cube 3, slab 2",
             all(o[0] and o[2] for o in out) and out[0][1] == 3 and out[1][1] == 2)
    ck.check("T3-even-uniform", "K_AA = I/2 gives the even marginal 2^-|A| exactly; p(00) = p(11)",
             all(o[3] and o[4] for o in out))


def t4(ck, torus):
    C = torus["C"]
    K, m = torus["K"], torus["m"]
    L = 4

    def corner(x, y, z):
        return C["idx"][(x % L, y % L, z % L)]

    def nbrs(v):
        x, y, z = C["coords"][v]
        return [corner(x + 1, y, z), corner(x - 1, y, z), corner(x, y + 1, z),
                corner(x, y - 1, z), corner(x, y, z + 1), corner(x, y, z - 1)]

    v0 = corner(0, 0, 0)
    odd = nbrs(v0)
    star = C["STAR"][v0]

    def Nm(u):
        return [t for t in nbrs(u) if t != v0]

    T6 = sorted(set(sum((Nm(u) for u in odd), [])))
    HALF = QF(Fr(1, 2), 0, m)
    ZERO = QF(0, 0, m)
    ck.check("T4-schur", "every declared T is even, so K_TT = I/2 and M_TT = I/2 exactly",
             all(K[a][b] == (HALF if a == b else ZERO) for a in T6 for b in T6)
             and all(C["sub"][a] == 0 for a in T6) and len(T6) == 15)
    fam = {}
    fam["T0"] = torus_family(C, K, m, v0, [], [], star)
    fam["T1"] = torus_family(C, K, m, v0, Nm(odd[0]), [odd[0]], star)
    fam["T2o"] = torus_family(C, K, m, v0, sorted(set(Nm(odd[0]) + Nm(odd[1]))),
                              [odd[0], odd[1]], star)
    fam["T2a"] = torus_family(C, K, m, v0, sorted(set(Nm(odd[0]) + Nm(odd[2]))),
                              [odd[0], odd[2]], star)
    fam["T3"] = torus_family(C, K, m, v0,
                             sorted(set(Nm(odd[0]) + Nm(odd[2]) + Nm(odd[4]))),
                             [odd[0], odd[2], odd[4]], star)
    k0 = next(iter(fam["T0"]))
    ck.check("T4-T0T1", "T0: one menu, the full basis at 1/64; T1: 5 menus (48,64), 12 odds",
             len(fam["T0"]) == 1 and is_uniform(k0) and k0[0] == (1 << 64) - 1
             and len(set(k[0] for k in fam["T1"])) == 5 and len(fam["T1"]) == 12
             and sizes_of(set(k[0] for k in fam["T1"])) == {48: 4, 64: 1})
    ck.check("T4-T2", "T2 opposite and adjacent: 25 menus (32,48,56,64), 200 odds each",
             all(len(set(k[0] for k in fam[f])) == 25 and len(fam[f]) == 200
                 and sizes_of(set(k[0] for k in fam[f])) == {32: 8, 48: 8, 56: 8, 64: 1}
                 for f in ("T2o", "T2a")))
    s3 = set(k[0] for k in fam["T3"])
    ck.check("T4-T3", "T3 exact over 32768 classes: 141 menus, 4096 odds, 1 full basis, 0 uniform",
             len(s3) == 141 and len(fam["T3"]) == 4096 and sum(fam["T3"].values()) == 32768
             and sum(1 for s in s3 if s == (1 << 64) - 1) == 1
             and sum(1 for k in fam["T3"] if is_uniform(k)) == 0
             and sizes_of(s3) == {20: 16, 32: 24, 40: 48, 48: 12, 56: 24, 60: 16, 64: 1})
    special = [0, (1 << 15) - 1, sum(1 << a for a in range(0, 15, 2)),
               sum(1 << a for a in range(1, 15, 2))]
    sub = {n: [0] for n in range(1 << 15) if bin(n).count("1") <= 2}
    for n in special:
        sub[n] = list(range(64))
    fam["T6"] = torus_family_sub(C, K, m, v0, T6, odd, star, sub)
    s6 = set(k[0] for k in fam["T6"])
    ck.check("T4-T6", "T6 exact sub-family: 312 classes, 193 menus (7,20,23,63), 257 rational odds",
             sum(fam["T6"].values()) == 312 and len(s6) == 193 and len(fam["T6"]) == 257
             and sizes_of(s6) == {7: 64, 20: 20, 23: 45, 63: 64}
             and all(all(b == 0 for b in k[2]) for k in fam["T6"])
             and sum(1 for s in s6 if s == (1 << 64) - 1) == 0)
    return fam


def torus_family_sub(C, K, m, v0, T, closed, star, sub):
    """the T6 declared sub-family: the same engine over the listed (n_T, pi) classes."""
    ZERO = QF(0, 0, m)
    ONE = QF(1, 0, m)
    HALF = QF(Fr(1, 2), 0, m)
    assert all(K[T[a]][T[b]] == (HALF if a == b else ZERO)
               for a in range(len(T)) for b in range(len(T)))
    Rset = [v0] + closed
    k = len(Rset)
    c = len(closed)
    PA = [[[K[i][T[a]] * K[T[a]][j] for j in Rset] for i in Rset] for a in range(len(T))]
    cpos = [star.index(C["EIDX"][(v0, u)]) for u in closed]
    Wp = np.arange(64)
    par = np.array([bin(w).count("1") & 1 for w in Wp])
    cbits = np.zeros(64, dtype=np.int64)
    for a, p in enumerate(cpos):
        cbits |= ((Wp >> p) & 1) << a
    keys = {}
    for nTint, pis in sub.items():
        Kp = [[K[i][j] for j in Rset] for i in Rset]
        for a in range(len(T)):
            plus = (nTint >> a) & 1
            for i in range(k):
                Pi = PA[a][i]
                oi = Kp[i]
                for j in range(k):
                    if Pi[j].iszero():
                        continue
                    oi[j] = oi[j] - Pi[j] - Pi[j] if plus else oi[j] + Pi[j] + Pi[j]
        lawR = []
        for n in range(1 << k):
            M = [[(Kp[i][j] if (n >> i) & 1 else ((ONE - Kp[i][j]) if i == j else -Kp[i][j]))
                  for j in range(k)] for i in range(k)]
            lawR.append(qf_det(M, m))
        for pi in pis:
            vals = []
            for w in range(64):
                n = int(par[w])
                for a in range(c):
                    n |= (((pi >> a) & 1) ^ ((int(cbits[w]) >> a) & 1)) << (1 + a)
                vals.append(lawR[n])
            if all(x.iszero() for x in vals):
                continue
            Dd = common_denominator(vals)
            supp = sum(1 << w for w in range(64) if not vals[w].iszero())
            key = (supp,) + canonical_odds([int(x.a * Dd) for x in vals],
                                           [int(x.b * Dd) for x in vals], m)
            keys[key] = keys.get(key, 0) + 1
    return keys


def t5(ck, site_keys, star_keys, pair_keys, sstar_keys, fam, SEA, P_SEA):
    gs = global_clause(set(k[0] for k in site_keys), 2)
    gstar = global_clause(set(k[0] for k in star_keys), 8)
    ck.check("T5-global-cube", "cube: the global system is inconsistent at the site (rank 2), star (rank 8)",
             gs == (2, 3, True) and gstar == (8, 9, True))
    w = disjoint_witness(set(k[0] for k in star_keys))
    ck.check("T5-witness", "the supports refute it: two disjoint size-4 star menus union to the basis",
             w is not None and bin(w[0]).count("1") == 4 and w[0] | w[1] == 255
             and 255 in set(k[0] for k in star_keys))
    gp = global_clause(set(k[0] for k in pair_keys), 64)
    gss = global_clause(set(k[0] for k in sstar_keys), 16)
    ck.check("T5-global-slab", "slab tick: pair 421 menus rank 64, star 285 rank 16, both inconsistent",
             gp == (64, 65, True) and gss == (16, 17, True)
             and disjoint_witness(set(k[0] for k in pair_keys)) is not None
             and disjoint_witness(set(k[0] for k in sstar_keys)) is not None)
    gt = {f: global_clause(set(k[0] for k in fam[f]), 64) for f in ("T1", "T2o", "T3", "T6")}
    pooled = set()
    for f in ("T0", "T1", "T2o", "T2a", "T3", "T6"):
        pooled |= set(k[0] for k in fam[f])
    gpool = global_clause(pooled, 64)
    ck.check("T5-global-torus", "torus T1/T2/T3/T6 rank 4/8/16/64, 353 pooled rank 64: all inconsistent",
             [gt[f][0] for f in ("T1", "T2o", "T3", "T6")] == [4, 8, 16, 64]
             and all(gt[f][2] for f in gt) and len(pooled) == 353 and gpool == (64, 65, True))
    g0 = global_clause(set(k[0] for k in fam["T0"]), 64)
    g7 = global_clause({3}, 2)
    ck.check("T5-single-menu", "one-menu families (site k <= 7, torus T0) are consistent, sum pinned",
             g0 == (1, 1, False) and g7 == (1, 1, False))
    nu_site = sum(1 for k in site_keys if not is_uniform(k))
    nu_star = sum(1 for k in star_keys if not is_uniform(k))
    nu_pool = sum(1 for k in set(itertools.chain.from_iterable(
        fam[f] for f in ("T0", "T1", "T2o", "T2a", "T3", "T6"))) if not is_uniform(k))
    ck.check("T5-rogue", "the uniform rogue differs from Born on 126/129 site, 1324/1329 star fibres",
             nu_site == 126 and len(site_keys) == 129 and nu_star == 1324 and len(star_keys) == 1329
             and nu_pool == 4765)
    families = [(site_keys, 2), (star_keys, 8), (pair_keys, 64), (sstar_keys, 16)]
    families += [(fam[f], 64) for f in fam]
    ok = True
    for keys, n in families:
        union = 0
        for k in keys:
            ap, bp, N = k[1], k[2], k[3]
            ok &= sum(ap) == N and sum(bp) == 0
            ok &= all((ap[w], bp[w]) == (0, 0) for w in range(n) if not (k[0] >> w) & 1)
            ok &= all((ap[w], bp[w]) != (0, 0) for w in range(n) if (k[0] >> w) & 1)
            union |= k[0]
        ok &= union == (1 << n) - 1
    ck.check("T5-effects", "each menu's odds live on its support and sum to 1; menus cover the basis",
             ok)
    sizes = set()
    for keys, n in families:
        sizes |= set(bin(k[0]).count("1") for k in keys)
    star_sup = set(k[0] for k in star_keys)
    four = [s for s in star_sup if bin(s).count("1") == 4]
    ck.check("T5-arity", "no menu has three outcomes at any unit; minimum sizes 4 / 19 / 5 / 7",
             3 not in sizes
             and min(bin(k[0]).count("1") for k in star_keys) == 4
             and min(bin(k[0]).count("1") for k in pair_keys) == 19
             and min(bin(k[0]).count("1") for k in sstar_keys) == 5
             and min(bin(k[0]).count("1") for k in fam["T6"]) == 7)
    ck.check("T5-killing", "the site realises only {P0},{P1},{P0,P1}; the 8 four-outcome menus pair up",
             set(k[0] for k in site_keys) == {1, 2, 3} and len(four) == 8
             and all((255 ^ s) in star_sup for s in four)
             and sizes_of(set(k[0] for k in fam["T0"])) == {64: 1})
    fibre(ck, SEA, P_SEA)


def fibre(ck, SEA, P_SEA):
    """b6_fibre.py: the reduced record-conditioned sea, Lemma 2 and Lemma 3."""
    NQ = 12
    D = 4096
    PSI = SEA.reshape((2,) * NQ)
    ZL = np.arange(D)

    def reduced(cond_edges, cond_vals, U):
        sl = [slice(None)] * NQ
        for e, b in zip(cond_edges, cond_vals):
            sl[NQ - 1 - e] = b
        psi = PSI[tuple(sl)]
        rem = [q for q in range(NQ - 1, -1, -1) if q not in cond_edges]
        p = float(np.sum(np.abs(psi) ** 2))
        if p < 1e-14:
            return None
        psi = psi / np.sqrt(p)
        Uax = [rem.index(q) for q in U]
        oth = [a for a in range(len(rem)) if a not in Uax]
        psi = np.transpose(psi, Uax + oth).reshape(1 << len(U), -1)
        rho = psi @ psi.conj().T
        rows = np.zeros(1 << len(U), dtype=np.int64)
        for w in range(1 << len(U)):
            r = 0
            for a in range(len(U)):
                r = (r << 1) | ((w >> a) & 1)
            rows[w] = r
        return rho[np.ix_(rows, rows)]

    conds = 0
    pairs = 0
    inv_site = set()
    inv_pool = set()
    dev = 0.0
    for k in range(5):
        for R0 in itertools.combinations(range(NQ), k):
            for w0 in itertools.product((0, 1), repeat=k):
                ok = False
                msk = np.ones(D, dtype=bool)
                for e, b in zip(R0, w0):
                    msk &= ((ZL >> e) & 1) == b
                pw = P_SEA[msk]
                z = ZL[msk]
                tot = pw.sum()
                for q in range(NQ):
                    if q in R0:
                        continue
                    rho = reduced(list(R0), list(w0), [q])
                    if rho is None:
                        continue
                    ok = True
                    pairs += 1
                    key = (round(rho[0, 0].real, 9), round(rho[1, 1].real, 9),
                           round(abs(rho[0, 1]), 9))
                    inv_pool.add(key)
                    inv_site.add((q,) + key)
                    dev = max(dev, abs(pw[((z >> q) & 1) == 1].sum() / tot - rho[1, 1].real))
                conds += int(ok)
    ck.check("T5-fibre-172", "PR #7931: 9969 conditions, 82116 pairs, 164232 checks, 172 keyed fibres",
             conds == 9969 and pairs == 82116 and 2 * pairs == 164232
             and len(inv_site) == 172 and len(inv_pool) == 21)
    res = []
    for U in ([0], [0, 1, 2]):
        pool = [e for e in range(NQ) if e not in U]
        fib = {}
        menus = set()
        nc = 0
        bd = 0.0
        for k in range(len(pool) + 1):
            for R0 in itertools.combinations(pool, k):
                for w0 in itertools.product((0, 1), repeat=k):
                    rho = reduced(list(R0), list(w0), U)
                    if rho is None:
                        continue
                    nc += 1
                    d = np.real(np.diag(rho)).copy()
                    d[np.abs(d) < 1e-13] = 0.0
                    supp = tuple(int(x > 0) for x in d)
                    menus.add(supp)
                    fk = tuple(np.round(rho.real, 9).ravel()) + tuple(np.round(rho.imag, 9).ravel())
                    fib.setdefault(fk, set()).add(supp)
                    msk = np.ones(D, dtype=bool)
                    for e, b in zip(R0, w0):
                        msk &= ((ZL >> e) & 1) == b
                    pw = P_SEA[msk]
                    z = ZL[msk]
                    wi = np.zeros(len(z), dtype=np.int64)
                    for a, q in enumerate(U):
                        wi |= ((z >> q) & 1) << a
                    pu = np.bincount(wi, weights=pw, minlength=1 << len(U)) / pw.sum()
                    bd = max(bd, float(np.max(np.abs(pu - np.real(np.diag(rho))))))
        res.append((nc, len(fib), len(menus), sum(1 for s in fib.values() if len(s) > 1), bd))
    ck.check("T5-fibre-menu", "Lemma 2 on site 0 (175419 conditions) and star(0) (19619): no fibre has 2 menus",
             res[0][0] == 175419 and res[1][0] == 19619 and res[0][3] == 0 and res[1][3] == 0
             and res[0][2] == 3 and res[1][2] == 69 and res[0][1] == 635 and res[1][1] == 1499)
    worst = max(dev, res[0][4], res[1][4])
    ck.check("T5-fibre-born", "Lemma 3, float: p(w|n) = <w|sigma(n)|w> to %.1e: the fibred clause is an identity" % worst,
             worst < 8e-15)


def gates(ck):
    note = NOTE_PATH.read_text()
    nnorm = normalize(note)
    ax = normalize(AXIOM_PATH.read_text())
    q1 = ("There is one fixed nearest-neighbor admissibility rule, covariant under lattice "
          "translations and proper cubic rotations.")
    q2 = ("For each site, the probability distribution over the possibilities is determined by, "
          "and varies with, the nearest-neighbor conditions.")
    q3 = ("When present, a record locks exactly one admissible local possibility. A site never "
          "carries more than one record; records are permanent.")
    q4 = "Only records are readable. A readout value is determined by record content alone."
    ck.check("gate-axioms", "Admissibility and Record quoted verbatim from MINIMAL_AXIOMS_2026-06-29.md",
             all(q in ax and q in nnorm for q in (q1, q2, q3, q4)))
    ck.check("gate-title", "the note carries the honest title, no paid price, no refuted Born rule",
             "THE MATTER LAW'S OWN TICKS REALISE MENUS IN ONE FRAME ONLY" in note.upper()
             and "the tick pays the Born price" not in note
             and "the Born rule is refuted" not in note)
    ck.check("gate-quoted", "the note declares the three censuses reduced here and quoted",
             all(s in nnorm for s in ("11405", "95631", "358125", "21656")))
    ck.check("gate-surface", "the note keeps its conditional surface and its audit line",
             all(s in note for s in ("actual_current_surface_status: conditional-support",
                                     "audit_required_before_effective_retained: true",
                                     "Independent audit remains required")))


def main():
    print("arithmetic_boundary: exact in Q(sqrt m), m = 1, 2, 3, 6; no seed, no sampling")
    print("float_boundary: the sea cross-check and the reduced states only")
    print("census_boundary: cube complete; slab and torus T6 on sub-families")
    print("import_boundary: no Born form, no frame theorem, no axiom content")
    ck = Checks()
    cube = build(cluster(2, 2, 2))
    slab = build(cluster(2, 2, 3))
    torus = build(cluster(4, 4, 4, periodic=(True, True, True), twist=(1, 1, 1)), do_law=False)
    SEA, P_SEA = t1(ck, cube, slab, torus)
    lawc = Law(cube["C"], cube["m"], cube["D"], cube["g"], cube["pa"], cube["pb"])
    laws = Law(slab["C"], slab["m"], slab["D"], slab["g"], slab["pa"], slab["pb"])
    site_keys = t2(ck, cube, slab, lawc, laws)
    pair_keys, sstar_keys, star_keys = t3(ck, cube, slab, lawc, laws)
    lemma4(ck, cube, slab, lawc, laws)
    structural(ck, cube, slab)
    fam = t4(ck, torus)
    ck.note("corollary", "one frame at every unit: no abundance is supplied and nothing is forced")
    t5(ck, site_keys, star_keys, pair_keys, sstar_keys, fam, SEA, P_SEA)
    gates(ck)
    return ck.finish()


if __name__ == "__main__":
    raise SystemExit(main())
