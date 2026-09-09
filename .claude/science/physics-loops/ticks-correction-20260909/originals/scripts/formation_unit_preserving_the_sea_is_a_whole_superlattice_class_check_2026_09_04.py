#!/usr/bin/env python3
"""The formation unit that preserves the sea is a whole class of the superlattice role
pattern; the eigen-set criterion is one-particle and its minimal sets are the parity classes.

Class-A finite-dimensional runner, self-contained: nothing is imported from any worktree and
every object below is rebuilt from its definition. Qubits sit on the EDGE sites of finite
subgraphs of the cubic lattice (open boxes and periodic tori with declared twists), BKSF
superfast encoding (A_ij, B_v = product of Z on star(v), face stabilisers S_f), corner parity
dictionary n_v = (1 - B_v)/2, Kawamoto-Smit staggered signs eta_x = 1, eta_y = (-1)^x,
eta_z = (-1)^(x+y) -- flux -1 on every face of every cluster, the wrap-around faces of the tori
included. H = -sum_e eta_e T_e with t = 1, one-particle matrix h_ij = -eta_ij, the SEA is the
code-space ground state at half filling = the Slater determinant of the N lowest h-modes,
W = span of those modes (N = V/2, rounded up to the even value the code space allows when V is
odd). A record at an edge site REGISTERS Z_e. For a corner set S, R(S) = union of star(v) over
v in S is the record set formed jointly and H_R = the hop terms on the unrecorded edges =
the hopping Hamiltonian of G[V \\ S] (P_S H P_S = H_R exactly). The tick is Lueders formation
with the Born odds of the pre-record state and exp(-i tau H_R) between formations.

THE ONE-PARTICLE CRITERION certified here. With closure S' = {u : star(u) subset R(S)} and a
corner-occupation pattern S' = S1 (occupied) u S0 (empty), put
    U_{S1} = R_{V \\ S'}( W ∩ e_{S1}^perp ),      h_R = h[V \\ S', V \\ S'].
For a regular set (the Z-strings inside R(S) commuting with every face stabiliser have F2 rank
|S'|, i.e. G[V \\ S'] is connected) the conditioned state P_w|sea> is an H_R eigenvector for
every outcome w of nonzero odds iff h_R U_{S1} is contained in U_{S1} for every live pattern;
the many-body eigen-residual of the outcome is exactly ||(I - P_U) h_R U||_F, its <H_R> is
Tr(U^+ h_R U), and its odds are 2^-(|R| - |S'|) times the determinantal law
p(n) = det( diag(n) K_{S'S'} + diag(1-n)(I - K_{S'S'}) ), K = P_W. A pattern is LIVE iff
dim U_{S1} = N - |S1|: liveness is the orbital-dimension test, never the determinantal odds,
which underflow (2^-64 on an 8^3 class) above about 43 corners. On irregular sets the
one-particle test is only sufficient, so every irregular verdict quoted is many-body.

Source blocks reproduced (scratch T2 of 2026-09-04, read-only; nothing imported):
  * T2/t2_common.py       cluster() geometry (boxes, tori, twists), face_flux, sea_space,
                          t2_graph (T2 = offdiag h^2), components, logical_rank, null_space,
                          det_odds, eigenset_test, krylov_dims, closure, comp_label,
                          summarize_cluster -- with the liveness fix (orbital dimension)
  * T2/t2_certify_cube.py mb_outcomes (per-outcome many-body residual / eigenvalue / odds by
                          one matvec and bincounts) and the declared cube tree schedules
  * T2/t2_certify_slab.py the same on the 2^20 record space held on the half-filling index set
  * T2/t2_slab_table.py   the structure post-analysis of the slab's eigen closures
  * T2/t2_classify.py     fast_closure, full_or_declared (the declared pattern family),
                          repair_units, the coverage and prefix-closure scans
  * L3/l3_core.py         Pauli algebra P/pact/comm, Enc (A_ij, B_v, S_f, hop_pauli), the
                          R0-R4 audit, code_space
  * L3j/l3j_core.py       the cube: the 128-dim code space and the sea by one 128 x 128 eigh
  * L3m/l3m_mb.py         the slab: the sparse H on the half-filled sector J, |J| = 473088;
                          the seeded Lanczos start is replaced by a declared deterministic one
  * T1/t1_cube.py         run_tree in the unnormalised-branch form, the census, joint_set

The Krylov screen rank[e_S, h e_S, h^2 e_S] <= 2|S| is evaluated here through the 3|S| x 3|S|
Gram matrix whose (a,b) block is h^(a+b)[S,S] (rank M = rank M^T M), batched over sets; it
agrees set by set with the direct rank of [e_S, h e_S, h^2 e_S] and makes the complete
enumerations affordable. Nothing is sampled and there is NO SEED anywhere: every cluster, set,
pattern, order and schedule is enumerated or written out, and the slab's Lanczos start is the
fixed vector cos(0.7 i + 0.3) + i cos(1.3 i + 1.1) projected into the code space. The
propagator is the Chebyshev (Jacobi-Anger) series of exp(-i tau H_R) under the rigorous bound
||H_R|| <= the number of free edges. No dense object above 4096 x 4096 is formed and peak
memory stays under 1 GB; one process, no network.

Line tags. `[exact]` = integer, F2 or symplectic Pauli arithmetic with no floating point in the
statement. `[numerical, tol]` = a deterministic double-precision evaluation of an exactly
specified quantity at the stated threshold.

Output: one PASS/FAIL line per check, then `TOTAL: PASS=N FAIL=M`. Exit 0 iff FAIL = 0.
"""
from __future__ import annotations

import itertools
import math
import sys
import time
from functools import reduce

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.special import jv

AUDIT_TIMEOUT_SEC = 300

T0 = time.time()
PASS = 0
FAIL = 0
PMIN = 1e-13


def check(label, cond):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ==========================================================================
# Pauli algebra in the symplectic representation, phases mod 4   (L3/l3_core.py)
def pc(n):
    return bin(n).count("1")


class P:
    __slots__ = ("k", "x", "z")

    def __init__(s, k, x, z):
        s.k = k % 4
        s.x = x
        s.z = z

    def __mul__(a, b):
        return P(a.k + b.k + 2 * pc(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def neg(s):
        return P(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def __hash__(s):
        return hash((s.k, s.x, s.z))

    def is_herm(s):
        return s.k % 2 == pc(s.x & s.z) % 2

    def is_id(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def is_mid(s):
        return s.x == 0 and s.z == 0 and s.k == 2


ID = P(0, 0, 0)
PH = [1 + 0j, 1j, -1 + 0j, -1j]


def comm(a, b):
    return (pc(a.x & b.z) + pc(a.z & b.x)) % 2 == 0


def pact(p, b):
    return b ^ p.x, PH[p.k] * ((-1) ** (pc(p.z & b) % 2))


def parity(x):
    x = x.astype(np.int64)
    for s in (32, 16, 8, 4, 2, 1):
        x = x ^ (x >> s)
    return (x & 1).astype(np.int8)


# ==========================================================================
# geometry: open boxes and tori with declared twists                (T2/t2_common.py)
def cluster(Lx, Ly, Lz, periodic=(False, False, False), twist=(0, 0, 0)):
    """corner (x,y,z) has index (x*Ly + y)*Lz + z; a periodic direction needs even length so
    the staggered signs close, and twist_a = 1 multiplies its wrap-around hops by -1."""
    L = (Lx, Ly, Lz)
    idx = {(x, y, z): (x * Ly + y) * Lz + z
           for x in range(Lx) for y in range(Ly) for z in range(Lz)}
    V = Lx * Ly * Lz
    raw = []
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
            raw.append((min(i, j), max(i, j), a, eta))
    raw.sort(key=lambda t: (t[0], t[1]))
    EDGES = [(i, j) for (i, j, a, s) in raw]
    eta = np.array([s for (i, j, a, s) in raw], dtype=np.int64)
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
            p1, p2 = nxt(c, a), nxt(c, b)
            if p1 is None or p2 is None:
                continue
            p3 = nxt(p1, b)
            if p3 is None or p3 != nxt(p2, a):
                continue
            cyc = (idx[c], idx[p1], idx[p3], idx[p2])
            if len(set(cyc)) == 4:
                FACES.add(cyc)
    FACES = sorted(FACES)
    h = np.zeros((V, V))
    for q, (i, j) in enumerate(EDGES):
        h[i, j] = h[j, i] = -float(eta[q])
    sub = np.array([sum(coords[v]) % 2 for v in range(V)])
    cls = np.array([(coords[v][0] % 2) * 4 + (coords[v][1] % 2) * 2 + (coords[v][2] % 2)
                    for v in range(V)])
    deg = np.array([int(np.sum(np.abs(h[v]) > 0)) for v in range(V)])
    EIDX = {}
    for q, (i, j) in enumerate(EDGES):
        EIDX[(i, j)] = EIDX[(j, i)] = q
    STAR = {v: [] for v in range(V)}
    for q, (i, j) in enumerate(EDGES):
        STAR[i].append(q)
        STAR[j].append(q)
    NBR = {v: set() for v in range(V)}
    for (i, j) in EDGES:
        NBR[i].add(j)
        NBR[j].add(i)
    return dict(L=L, periodic=periodic, twist=twist, V=V, EDGES=EDGES, eta=eta, FACES=FACES,
                h=h, coords=coords, idx=idx, sub=sub, cls=cls, deg=deg, STAR=STAR, EIDX=EIDX,
                NBR=NBR, name="%dx%dx%d" % L)


def face_flux(C):
    out = []
    for cyc in C["FACES"]:
        f = 1
        for t in range(4):
            f *= int(C["eta"][C["EIDX"][(cyc[t], cyc[(t + 1) % 4])]])
        out.append(f)
    return out


def straight_two_step(C):
    """the geometric prediction for T2: u ~ u +- 2 e_a (with wrap where periodic)."""
    V = C["V"]
    pred = np.zeros((V, V), dtype=bool)
    for u in range(V):
        x = C["coords"][u]
        for a in range(3):
            for sgn in (2, -2):
                y = list(x)
                y[a] += sgn
                if C["periodic"][a]:
                    y[a] %= C["L"][a]
                y = tuple(y)
                if y in C["idx"] and C["idx"][y] != u:
                    pred[u, C["idx"][y]] = True
    return pred


def components(A):
    V = A.shape[0]
    seen = -np.ones(V, dtype=np.int64)
    comps = []
    for s in range(V):
        if seen[s] >= 0:
            continue
        c = len(comps)
        stack = [s]
        seen[s] = c
        mem = []
        while stack:
            u = stack.pop()
            mem.append(u)
            for v in np.flatnonzero(A[u]):
                if seen[v] < 0:
                    seen[v] = c
                    stack.append(int(v))
        comps.append(sorted(int(v) for v in mem))
    return comps, seen


def closure(C, S):
    R = set(q for v in S for q in C["STAR"][v])
    return sorted(u for u in range(C["V"]) if set(C["STAR"][u]) <= R)


def fast_closure(C, S):
    Sset = set(S)
    cand = set()
    for v in S:
        cand |= C["NBR"][v]
    return sorted(Sset | {u for u in cand if u not in Sset and C["NBR"][u] <= Sset})


def star_mask(C, S):
    m = 0
    for v in S:
        for q in C["STAR"][v]:
            m |= 1 << q
    return m


def n_records(C, S):
    return len(set(q for v in S for q in C["STAR"][v]))


def logical_rank(C, S):
    """F2 dimension of {T subset R(S) : |T ∩ f| even for every face f}; |S'| for a regular set."""
    R = sorted(set(q for v in S for q in C["STAR"][v]))
    pos = {q: a for a, q in enumerate(R)}
    basis = []
    for cyc in C["FACES"]:
        r = 0
        for t in range(4):
            q = C["EIDX"][(cyc[t], cyc[(t + 1) % 4])]
            if q in pos:
                r ^= 1 << pos[q]
        for b in basis:
            r = min(r, r ^ b)
        if r:
            basis.append(r)
            basis.sort(reverse=True)
    return len(R) - len(basis), len(R)


def regular(C, S):
    Sp = closure(C, S)
    lr, nR = logical_rank(C, S)
    return (lr == len(Sp)) or (len(Sp) == C["V"] and lr == C["V"] - 1)


# ==========================================================================
# the one-particle layer and the criterion                          (T2/t2_common.py)
def sea_space(h, N):
    w, U = np.linalg.eigh(h)
    return w, U[:, :N], (float(w[N] - w[N - 1]) if N < len(w) else float("inf"))


def summarize(C, N=None):
    V = C["V"]
    N = V // 2 if N is None else N
    if N % 2:
        N += 1
    w, W, gap = sea_space(C["h"], N)
    h2 = C["h"] @ C["h"]
    A = (np.abs(h2) > 1e-12)
    np.fill_diagonal(A, False)
    comps, lab = components(A)
    return dict(N=N, w=w, W=W, gap=gap, T2=A, h2=h2, comps=comps, lab=lab,
                E_sea=float(np.sum(w[:N])), nzero=int(np.sum(np.abs(w) < 1e-9)))


def null_space(M, tol=1e-10):
    if M.shape[0] == 0:
        return np.eye(M.shape[1])
    u, s, vt = np.linalg.svd(M, full_matrices=True)
    r = int(np.sum(s > tol))
    return vt[r:].conj().T


def det_odds(K, S, n):
    KS = K[np.ix_(S, S)]
    m = len(S)
    M = np.zeros((m, m), dtype=KS.dtype)
    I = np.eye(m)
    for a in range(m):
        M[a] = KS[a] if n[a] else (I[a] - KS[a])
    return float(np.real(np.linalg.det(M)))


def eigenset_test(h, W, S, K=None, patterns=None, tol=1e-10):
    """per-pattern one-particle criterion; liveness is the orbital-dimension test."""
    V = h.shape[0]
    N = W.shape[1]
    S = list(S)
    Sset = set(S)
    Sc = [v for v in range(V) if v not in Sset]
    hR = h[np.ix_(Sc, Sc)]
    rows = []
    pats = patterns if patterns is not None else list(itertools.product((0, 1), repeat=len(S)))
    for n in pats:
        S1 = [S[a] for a in range(len(S)) if n[a]]
        prob = det_odds(K, S, n) if K is not None else float("nan")
        Z = null_space(W[S1, :]) if S1 else np.eye(N)
        if Z.shape[1] != N - len(S1):
            rows.append(dict(pattern=tuple(n), prob=prob, dimU=-1, resid=float("nan"),
                             ev=float("nan")))
            continue
        U0 = (W @ Z)[Sc, :]
        u, s, vt = np.linalg.svd(U0, full_matrices=False)
        r = int(np.sum(s > tol))
        if r != N - len(S1):
            rows.append(dict(pattern=tuple(n), prob=prob, dimU=r, resid=float("nan"),
                             ev=float("nan")))
            continue
        U = u[:, :r]
        hU = hR @ U
        M = U.conj().T @ hU
        rows.append(dict(pattern=tuple(n), prob=prob, dimU=r,
                         resid=float(np.linalg.norm(hU - U @ M)),
                         ev=float(np.real(np.trace(M)))))
    live = [r for r in rows if r["dimU"] == N - sum(r["pattern"])]
    return rows, max((r["resid"] for r in live), default=0.0), len(live)


def declared_patterns(m):
    """the declared pattern family for sets too large to enumerate: empty, full, every single
    corner occupied / empty, every pair among the first eight, and the two alternating ones."""
    pats = {tuple([0] * m), tuple([1] * m)}
    for a in range(m):
        p = [0] * m
        p[a] = 1
        pats.add(tuple(p))
        p = [1] * m
        p[a] = 0
        pats.add(tuple(p))
    for a, b in itertools.combinations(range(min(m, 8)), 2):
        p = [0] * m
        p[a] = p[b] = 1
        pats.add(tuple(p))
        p = [1] * m
        p[a] = p[b] = 0
        pats.add(tuple(p))
    pats.add(tuple(a % 2 for a in range(m)))
    pats.add(tuple((a + 1) % 2 for a in range(m)))
    return sorted(pats)


def small_patterns(m):
    """the declared eight-pattern family for the largest classes: empty, full, the first corner
    occupied / empty, the last corner occupied / empty, and the two alternating patterns."""
    pats = {tuple([0] * m), tuple([1] * m), tuple(a % 2 for a in range(m)),
            tuple((a + 1) % 2 for a in range(m))}
    for a in (0, m - 1):
        p = [0] * m
        p[a] = 1
        pats.add(tuple(p))
        p = [1] * m
        p[a] = 0
        pats.add(tuple(p))
    return sorted(pats)


def full_or_declared(h, W, K, S, maxbits=12, small=False):
    m = len(S)
    if m <= maxbits and not small:
        rows, mx, nl = eigenset_test(h, W, S, K=K)
        return mx, nl, "all %d patterns" % (1 << m)
    pats = small_patterns(m) if small else declared_patterns(m)
    rows, mx, nl = eigenset_test(h, W, S, K=K, patterns=pats)
    return mx, nl, "%s %d patterns" % ("declared small" if small else "declared", len(pats))


def krylov_dims(h, W, S, tol=1e-9):
    """dim of the Krylov closure of e_S under h, and dim M_1 = P_W e_S, dim M_0 = (I-P_W) e_S."""
    V = h.shape[0]
    S = list(S)
    m = len(S)
    E = np.zeros((V, m))
    E[S, np.arange(m)] = 1.0
    Q, _ = np.linalg.qr(E)
    basis = Q[:, :m]
    cur = basis
    while basis.shape[1] < V:
        nxt = h @ cur
        for _ in range(2):
            nxt = nxt - basis @ (basis.T @ nxt)
        u, sv, vt = np.linalg.svd(nxt, full_matrices=False)
        r = int(np.sum(sv > tol))
        if r == 0:
            break
        cur = u[:, :r]
        basis = np.column_stack([basis, cur])
    Pw = W @ W.conj().T
    d1 = int(np.linalg.matrix_rank(Pw @ E, tol=tol))
    d0 = int(np.linalg.matrix_rank(E - Pw @ E, tol=tol))
    return int(basis.shape[1]), d1, d0


def hpowers(h):
    hp = [np.eye(h.shape[0])]
    for _ in range(4):
        hp.append(hp[-1] @ h)
    return hp


def gram_ranks(hp, Sarr, tol=1e-9):
    """rank[e_S, h e_S, h^2 e_S] for a batch of equal-size sets, through the Gram matrix
    whose (a,b) block is h^(a+b)[S,S]."""
    nb, m = Sarr.shape
    G = np.empty((nb, 3 * m, 3 * m))
    for a in range(3):
        for b in range(3):
            G[:, a * m:(a + 1) * m, b * m:(b + 1) * m] = hp[a + b][Sarr[:, :, None],
                                                                   Sarr[:, None, :]]
    w = np.linalg.eigvalsh(G)
    return (w > (tol * w[:, -1])[:, None]).sum(1)


def screen_sets(hp, sets, chunk=4000):
    """which of the given (equal-size) corner sets pass rank <= 2|S|."""
    if not sets:
        return []
    A = np.array(sets, dtype=np.intp)
    m = A.shape[1]
    out = []
    for i in range(0, len(A), chunk):
        out.append(gram_ranks(hp, A[i:i + chunk]) <= 2 * m)
    return np.concatenate(out)


def enumerate_unions(C, hp, h, W, K, max_union=3, reduce_torus=False, full_max=12):
    """complete enumeration of the unions of up to `max_union` corner stars: closure, the
    Krylov screen, then the full per-pattern criterion on every set that passes."""
    V = C["V"]
    F = None
    if reduce_torus:
        F = set(C["idx"][(x, y, z)] for x in (0, 1) for y in (0, 1) for z in (0, 1))
    nsets = 0
    nscreen = 0
    found = []
    for m in range(1, max_union + 1):
        cl = []
        for S in itertools.combinations(range(V), m):
            if F is not None and not any(v in F for v in S):
                continue
            nsets += 1
            cl.append(tuple(fast_closure(C, list(S))))
        bysz = {}
        for Sp in cl:
            bysz.setdefault(len(Sp), []).append(Sp)
        for sz, group in bysz.items():
            ok = screen_sets(hp, group)
            for Sp, good in zip(group, ok):
                if not good:
                    continue
                nscreen += 1
                if len(Sp) > full_max:
                    continue
                rows, mx, nl = eigenset_test(h, W, list(Sp), K=K)
                if mx < 1e-9:
                    found.append(Sp)
    return nsets, nscreen, sorted(set(found))


# ==========================================================================
# the superfast encoding, its R0-R4 audit and the code-space cosets  (L3/l3_core.py)
class Enc:
    def __init__(self, V, EDGES, FACES):
        self.V = V
        self.EDGES = list(EDGES)
        self.FACES = list(FACES)
        self.NQ = len(EDGES)
        self.DIM = 1 << self.NQ
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = q
            self.EIDX[(j, i)] = q
        self.NBR = {i: sorted(j for (a, b) in self.EDGES
                              for j in ((b,) if a == i else ((a,) if b == i else ())))
                    for i in range(V)}
        self.STAR = {i: [self.EIDX[(i, k)] for k in self.NBR[i]] for i in range(V)}
        self.STARMASK = {i: reduce(lambda a, b: a | (1 << b), self.STAR[i], 0) for i in range(V)}

    def A_unsigned(self, i, j):
        x = 1 << self.EIDX[(i, j)]
        z = 0
        for k in self.NBR[i]:
            if k != j and k < j:
                z ^= 1 << self.EIDX[(i, k)]
        for l in self.NBR[j]:
            if l != i and l < i:
                z ^= 1 << self.EIDX[(j, l)]
        return P(pc(x & z) % 2, x, z)

    def A(self, i, j):
        p = self.A_unsigned(i, j)
        return p if i < j else p.neg()

    def B(self, i):
        return P(0, 0, self.STARMASK[i])

    def loop(self, cyc):
        out = ID
        for a in range(len(cyc)):
            out = out * self.A(cyc[a], cyc[(a + 1) % len(cyc)])
        return out

    def record(self, z):
        return tuple(pc(z & self.STARMASK[i]) % 2 for i in range(self.V))

    def hop_pauli(self, i, j):
        A = self.A(i, j)
        return A * self.B(i), A * self.B(j)


def audit(E):
    R = {}
    A = {e: E.A(*e) for e in E.EDGES}
    Bv = {i: E.B(i) for i in range(E.V)}
    R["R0_welldef"] = all(E.A_unsigned(i, j) == E.A_unsigned(j, i) for (i, j) in E.EDGES)
    R["R0_antisym"] = all(E.A(j, i) == E.A(i, j).neg() for (i, j) in E.EDGES)
    R["R1"] = (all(A[e].is_herm() and (A[e] * A[e]).is_id() for e in E.EDGES)
               and all(Bv[i].is_herm() and (Bv[i] * Bv[i]).is_id() for i in range(E.V)))
    r2 = all(comm(Bv[i], Bv[j]) for i, j in itertools.combinations(range(E.V), 2))
    for e in E.EDGES:
        for v in range(E.V):
            r2 &= (comm(A[e], Bv[v]) != (v in e))
    R["R2"] = bool(r2)
    r3 = True
    for e, f in itertools.combinations(E.EDGES, 2):
        r3 &= (comm(A[e], A[f]) != (len(set(e) & set(f)) == 1))
    R["R3"] = bool(r3)
    S = [E.loop(f) for f in E.FACES]
    r4 = True
    for s in S:
        r4 &= s.is_herm() and (s * s).is_id()
        for e in E.EDGES:
            r4 &= comm(s, A[e])
        for v in range(E.V):
            r4 &= comm(s, Bv[v])
    for a, b in itertools.combinations(S, 2):
        r4 &= comm(a, b)
    R["R4"] = bool(r4)
    gens, basis = [], []
    for s in S:
        v = s.x
        for b in basis:
            v = min(v, v ^ b)
        if v != 0:
            basis.append(v)
            basis.sort(reverse=True)
            gens.append(s)
    R["k"] = len(gens)
    R["gens"] = gens
    grp = []
    for m in range(1 << len(gens)):
        p = ID
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        grp.append(p)
    R["grp"] = grp
    R["grp_ok"] = (not any(g.is_mid() for g in grp)) and sum(1 for g in grp if g.x == 0) == 1
    R["code_dim"] = E.DIM >> len(gens)
    R["ok"] = all(R[k] for k in ("R0_welldef", "R0_antisym", "R1", "R2", "R3", "R4", "grp_ok"))
    return R


def code_space(E, R):
    grp = R["grp"]
    phi = np.zeros(E.DIM, dtype=complex)
    cid = -np.ones(E.DIM, dtype=np.int64)
    reps = []
    for z0 in range(E.DIM):
        if cid[z0] >= 0:
            continue
        c = len(reps)
        reps.append(z0)
        for g in grp:
            b, a = pact(g, z0)
            assert cid[b] < 0
            cid[b] = c
            phi[b] = a
    assert (cid >= 0).all()
    return cid, phi, reps


# ==========================================================================
# a record space held on an index set: the whole 2^12 (cube) or J (slab)
# (L3j/l3j_core.py HAMP and L3m/l3m_mb.py Model, unified: H[z^bq, z] = 1j * amp_q(z))
class Space:
    def __init__(self, En, eta, Z, loc, name):
        self.En, self.name = En, name
        self.NQ, self.EDGES, self.V = En.NQ, En.EDGES, En.V
        self.Z, self.loc, self.n = Z, loc, len(Z)
        n, NQ = self.n, self.NQ
        self.BIT = [((Z >> q) & 1).astype(bool) for q in range(NQ)]
        self.src, self.tgt, self.amp = [], [], []
        rows, cols, dat = [], [], []
        self.xpart_ok = True
        for q, e in enumerate(En.EDGES):
            P1, P2 = En.hop_pauli(*e)
            self.xpart_ok &= (P1.x == P2.x == (1 << q))
            s1 = 1 - 2 * parity(Z & P1.z).astype(np.int64)
            s2 = 1 - 2 * parity(Z & P2.z).astype(np.int64)
            a = 0.5j * (PH[P1.k] * s1 - PH[P2.k] * s2)
            ai = np.round(a.imag).astype(np.int8)
            assert np.max(np.abs(a.real)) < 1e-12 and np.max(np.abs(a.imag - ai)) < 1e-12
            amp = (-int(eta[q])) * ai
            m = np.flatnonzero(amp != 0)
            t = loc[Z[m] ^ (1 << q)]
            assert np.all(t >= 0)
            self.src.append(m.astype(np.int32))
            self.tgt.append(t.astype(np.int32))
            self.amp.append(amp[m])
            rows.append(t.astype(np.int32))
            cols.append(m.astype(np.int32))
            dat.append(1j * amp[m].astype(np.float64))
        H = sp.coo_matrix((np.concatenate(dat), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(n, n)).tocsr()
        H.sort_indices()
        self.H = H
        self.rows = np.repeat(np.arange(n, dtype=np.int32), np.diff(H.indptr))
        self.cols = H.indices
        self.gens = None

    def set_gens(self, gens):
        self.gens = []
        for g in gens:
            perm = self.loc[self.Z ^ g.x]
            assert np.all(perm >= 0)
            sign = (1 - 2 * parity(self.Z & g.z)).astype(np.int8)
            self.gens.append((perm.astype(np.int32), sign, PH[g.k]))

    def project_code(self, v):
        for perm, sign, ph in self.gens:
            out = np.zeros_like(v)
            out[perm] = (ph * sign) * v
            v = 0.5 * (v + out)
        return v

    def intra(self, nid):
        mask = nid[self.rows] == nid[self.cols]
        return sp.csr_matrix((self.H.data * mask, self.cols, self.H.indptr),
                             shape=(self.n, self.n))

    def set_sea(self, sea):
        self.SEA = sea
        self.P_SEA = np.abs(sea) ** 2
        self.SUPP = int((self.P_SEA > 1e-14).sum())
        self.HQSEA = []
        for q in range(self.NQ):
            v = np.zeros(self.n, dtype=np.complex128)
            v[self.tgt[q]] = (1j * self.amp[q]) * sea[self.src[q]]
            self.HQSEA.append(v)
        self.HSEA = sum(self.HQSEA)


def node_residual(S, Phi, nid, nn, p, Hl):
    G = Hl @ Phi
    prod = (np.conj(Phi) * G).real
    EV = np.bincount(nid, weights=prod, minlength=nn)
    ev = np.where(p > 0, EV / np.where(p > 0, p, 1.0), 0.0)
    diff = G - ev[nid] * Phi
    R2 = np.bincount(nid, weights=np.abs(diff) ** 2, minlength=nn)
    res = np.sqrt(np.where(p > 0, R2 / np.where(p > 0, p, 1.0), 0.0))
    if S.n > 100000:
        small = np.flatnonzero((res < 1e-8) & (p >= PMIN))
        if 0 < len(small) <= 512:
            d = np.abs(Phi) ** 2
            for i in small:
                m = nid == i
                pi = float(np.sum(d[m]))
                evi = float(np.sum(prod[m])) / pi
                di = G[m] - evi * Phi[m]
                res[i] = math.sqrt(float(np.sum(np.abs(di) ** 2)) / pi)
                ev[i] = evi
    return res, ev


def cheb_evolve(Hl, v, tau, lam):
    """exp(-i tau Hl) v by Jacobi-Anger on [-lam, lam], lam >= ||Hl||."""
    x = tau * lam
    n = int(math.ceil(x))
    while n < x or abs(jv(n, x)) > 1e-17:
        n += 1
    nmax = n + 2
    c = [(1.0 if k == 0 else 2.0) * ((-1j) ** k) * jv(k, x) for k in range(nmax + 1)]
    T0c = v.copy()
    T1c = (Hl @ v) / lam
    out = c[0] * T0c + c[1] * T1c
    for k in range(2, nmax + 1):
        T2c = (2.0 / lam) * (Hl @ T1c) - T0c
        out += c[k] * T2c
        T0c, T1c = T1c, T2c
    return out


def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())


def run_tree(S, masks, tau):
    """joint formation of the declared record masks in the declared order, exp(-i tau H_R)
    between formations; unnormalised-branch form (T1/t1_cube.py run_tree, rule D)."""
    n, NQ = S.n, S.NQ
    Phi = S.SEA.astype(np.complex128).copy()
    nid = np.zeros(n, dtype=np.int64)
    nn = 1
    Rm = 0
    levels = []
    for mask in masks:
        qs = [q for q in range(NQ) if (mask >> q) & 1]
        key = np.zeros(n, dtype=np.int64)
        for a, q in enumerate(qs):
            key |= S.BIT[q].astype(np.int64) << a
        new = nid * (1 << len(qs)) + key
        uniq, inv = np.unique(new, return_inverse=True)
        nid = inv.astype(np.int64)
        nn = len(uniq)
        Rm |= mask
        d = np.abs(Phi) ** 2
        p = np.bincount(nid, weights=d, minlength=nn)
        alive = p >= PMIN
        nrec = pc(Rm)
        Hl = S.intra(nid)
        res, ev = node_residual(S, Phi, nid, nn, p, Hl)
        if tau > 0 and nrec < NQ:
            Phi2 = cheb_evolve(Hl, Phi, tau, float(NQ - nrec))
            dtv = 0.5 * np.bincount(nid, weights=np.abs(d - np.abs(Phi2) ** 2), minlength=nn) \
                * np.where(p > 0, 1.0 / np.where(p > 0, p, 1.0), 0.0)
            Phi = Phi2
        else:
            dtv = np.zeros(nn)
        del Hl
        full = np.abs(Phi) ** 2
        levels.append(dict(nrec=nrec, nalive=int(alive.sum()),
                           res_max=float(res[alive].max()), dtv_max=float(dtv[alive].max()),
                           full_tv=tv(full, S.P_SEA), support=int((full > 1e-14).sum())))
    return dict(law=np.abs(Phi) ** 2, levels=levels)


def mb_outcomes(S, C, Sp):
    """many-body per-outcome odds / <H_R> / residual on R(S'), by one matvec combination and
    bincounts (T2/t2_certify_cube.py, t2_certify_slab.py)."""
    R = sorted(set(q for v in Sp for q in C["STAR"][v]))
    key = np.zeros(S.n, dtype=np.int64)
    for a, q in enumerate(R):
        key |= S.BIT[q].astype(np.int64) << a
    g = S.HSEA.copy()
    for q in R:
        g -= S.HQSEA[q]
    nb = 1 << len(R)
    p = np.bincount(key, weights=S.P_SEA, minlength=nb)
    e = np.bincount(key, weights=np.real(np.conj(S.SEA) * g), minlength=nb)
    live = p > 1e-13
    ev = np.where(live, e / np.where(live, p, 1.0), 0.0)
    r2 = np.bincount(key, weights=np.abs(g - ev[key] * S.SEA) ** 2, minlength=nb)
    resid = np.sqrt(np.where(live, r2 / np.where(live, p, 1.0), 0.0))
    pat = np.zeros((nb, len(Sp)), dtype=np.int64)
    ws = np.arange(nb)
    for a, v in enumerate(Sp):
        m = 0
        for q in C["STAR"][v]:
            m |= 1 << R.index(q)
        pat[:, a] = np.array([pc(int(x)) & 1 for x in (ws & m)])
    return R, p, ev, resid, live, pat


# ==========================================================================
# A. THE 2x2x2 CUBE -- setting, the criterion on all 255 vertex sets, the trees
CC = cluster(2, 2, 2)
EnC = Enc(CC["V"], CC["EDGES"], CC["FACES"])
AUDC = audit(EnC)
ZC = np.arange(1 << EnC.NQ, dtype=np.int64)
SC = Space(EnC, CC["eta"], ZC, ZC, "cube")
CIDC, PHIC, _ = code_space(EnC, AUDC)
WCODE = np.zeros((4096, 128), dtype=np.complex128)
WCODE[ZC, CIDC] = PHIC / np.sqrt(float(len(AUDC["grp"])))
HWC = SC.H @ WCODE
HCC = WCODE.conj().T @ HWC
herm_c = float(np.max(np.abs(HCC - HCC.conj().T)))
inv_c = float(np.max(np.abs(HWC - WCODE @ HCC)))
EVC, VCC = np.linalg.eigh(HCC)
SEA_C = WCODE @ VCC[:, 0]
SC.set_sea(SEA_C)
HsC = SC.H @ SEA_C
E_SEA_C = math.fsum((np.conj(SEA_C) * HsC).real) / math.fsum(np.abs(SEA_C) ** 2)
sea_res_c = float(np.linalg.norm(HsC - E_SEA_C * SEA_C))
NVAL_C = np.zeros(4096, dtype=np.int64)
for v in range(8):
    NVAL_C += parity(ZC & EnC.STARMASK[v])
ZERO_C = SC.P_SEA < 1e-14
CHARGE_C = ZERO_C & (NVAL_C != 4)
CANC_C = ZERO_C & (NVAL_C == 4)
SMC = summarize(CC)
hC, WC, KC = CC["h"], SMC["W"], SMC["W"] @ SMC["W"].conj().T
del HWC, HsC
check("A1 [exact; 1e-12] cube 2x2x2: R0-R4 %s, k=%d, code %d of 4096, flux %s x%d; sea "
      "E=%.12f=-4sqrt3 (%.0e), resid %.1e, gap %.4f = the one-particle sum %.6f and gap %.4f; "
      "support %d, zeros %d=%d charge+%d cancellation; h^2=3I (T2 empty, %.0e), 8 singleton classes."
      % (AUDC["ok"], AUDC["k"], AUDC["code_dim"], set(face_flux(CC)), len(CC["FACES"]),
         E_SEA_C, abs(E_SEA_C + 4 * np.sqrt(3)), sea_res_c, float(EVC[1] - EVC[0]),
         SMC["E_sea"], SMC["gap"], SC.SUPP, int(ZERO_C.sum()), int(CHARGE_C.sum()),
         int(CANC_C.sum()), float(np.max(np.abs(SMC["h2"] - 3 * np.eye(8)))),
         ),
      AUDC["ok"] and AUDC["k"] == 5 and AUDC["code_dim"] == 128 and SC.xpart_ok
      and set(face_flux(CC)) == {-1} and abs(E_SEA_C + 4 * np.sqrt(3)) < 1e-12
      and sea_res_c < 1e-12 and herm_c < 1e-11 and inv_c < 1e-11 and SC.SUPP == 1984
      and int(CHARGE_C.sum()) == 1856 and int(CANC_C.sum()) == 256
      and abs(SMC["E_sea"] - E_SEA_C) < 1e-12 and not SMC["T2"].any()
      and len(SMC["comps"]) == 8 and float(np.max(np.abs(SMC["h2"] - 3 * np.eye(8)))) < 1e-12)

tA = time.time()
w_res = w_ev = w_odds = 0.0
cube_eig = []
cube_irr = []
cube_irr_res = 0.0
nreg = 0
for m in range(1, 9):
    for S in itertools.combinations(range(8), m):
        S = list(S)
        Sp = closure(CC, S)
        R, p, ev, resid, live, pat = mb_outcomes(SC, CC, Sp)
        rows, mx1, nl = eigenset_test(hC, WC, Sp, K=KC)
        rmap = {r["pattern"]: r for r in rows}
        scale = 2.0 ** (-(len(R) - (len(Sp) if len(Sp) < 8 else 7)))
        reg = regular(CC, S)
        mbmax = float(resid[live].max())
        if reg:
            nreg += 1
            for w in np.flatnonzero(live):
                r1 = rmap[tuple(int(x) for x in pat[w])]
                w_res = max(w_res, abs(resid[w] - r1["resid"]))
                w_ev = max(w_ev, abs(ev[w] - r1["ev"]))
                w_odds = max(w_odds, abs(p[w] - scale * r1["prob"]))
        else:
            cube_irr.append(S)
            cube_irr_res = min(cube_irr_res, mbmax) if cube_irr_res else mbmax
        if mbmax < 1e-9:
            cube_eig.append(S)
t_cube_sets = time.time() - tA
check("A2 [numerical, 1e-13] T1 criterion, cube, COMPLETE -- all 255 vertex sets, every outcome of "
      "nonzero odds. On the %d regular sets the many-body residual IS the one-particle Frobenius "
      "residual: max|resid_mb-resid_1p| %.3e, max|<H_R>_mb-Tr(U+h_R U)| %.3e, max odds gap %.1e. "
      "%d eigen-sets; the %d irregular sets (disconnected unrecorded graph) are all many-body "
      "NON-eigen at %.4f. [%.0fs]"
      % (nreg, w_res, w_ev, w_odds, len(cube_eig), len(cube_irr), cube_irr_res, t_cube_sets),
      w_res < 1.5e-14 and w_ev < 2e-14 and w_odds < 1e-14 and len(cube_eig) == 75
      and nreg == 249 and len(cube_irr) == 6 and cube_irr_res > 0.7)

subC = CC["sub"]
same = [S for S in cube_eig if len(set(subC[v] for v in S)) == 1]
mixed = [S for S in cube_eig if len(set(subC[v] for v in S)) == 2]
nsame = sum(1 for m in range(1, 9) for S in itertools.combinations(range(8), m)
            if len(set(subC[v] for v in S)) == 1)
anti = [S for S in mixed if len(S) == 2 and hC[S[0], S[1]] == 0]
adj_fail = [(u, v) for (u, v) in itertools.combinations(range(8), 2)
            if hC[u, v] != 0 and [u, v] not in cube_eig]
stars4 = sorted(sorted(closure(CC, [u for u in range(8) if hC[v, u] != 0])) for v in range(8))
mix4 = sorted(S for S in mixed if len(S) == 4)
check("A3 T2 on the cube (flat, every corner its own class): all %d single-sublattice sets are "
      "eigen-sets (%d of %d), %d of %d mixed are; the size-2 mixed eigen-sets are exactly the %d "
      "antipodal pairs, all %d adjacent pairs fail, and the size-4 ones are exactly the %d closed "
      "stars {v} u N(v) = closures of N(v)."
      % (nsame, len(same), nsame, len(mixed), 255 - nsame, len(anti), len(adj_fail), len(mix4)),
      len(same) == nsame == 30 and len(mixed) == 45 and len(anti) == 4 and len(adj_fail) == 12
      and len(mix4) == 8 and mix4 == stars4)

EVEN_C = [0, 3, 5, 6]
ODD_C = [1, 2, 4, 7]


def cube_census(law):
    z = law < 1e-14
    return (tv(law, SC.P_SEA), int((~z).sum()), int((z & CANC_C).sum()), int((z & CHARGE_C).sum()))


tA = time.time()
tr_tv = []
tr_res = []
tr_dtv = []
tr_supp = set()
tr_canc = set()
ntree = 0
for tau in (0.5, 2.0):
    for part in (EVEN_C, ODD_C):
        for order in itertools.permutations(part):
            r = run_tree(SC, [star_mask(CC, [v]) for v in order], tau)
            t, supp, canc, charge = cube_census(r["law"])
            tr_tv.append(t)
            tr_supp.add(supp)
            tr_canc.add(canc)
            tr_res.append(max(L["res_max"] for L in r["levels"]))
            tr_dtv.append(max(L["dtv_max"] for L in r["levels"]))
            ntree += 1
pair_tv = []
for tau in (0.5, 2.0):
    for sets in ([[0, 3], [5, 6]], [[1, 2], [4, 7]]):
        r = run_tree(SC, [star_mask(CC, S) for S in sets], tau)
        pair_tv.append(cube_census(r["law"])[0])
check("A4 [numerical, 1e-13] T4 cube, whole classes formed jointly with evolution: %d trees (all "
      "24 orders of the four even and of the four odd classes, tau in {0.5,2.0}) -- TV to the sea's "
      "law <= %.1e, support %s, all %s of 256 cancellation and %s of 1856 charge zeros kept, node "
      "residual <= %.1e, diagonal displaced <= %.1e; the two pair schedules <= %.1e. [%.0fs]"
      % (ntree, max(tr_tv), sorted(tr_supp), sorted(tr_canc), 1856, max(tr_res), max(tr_dtv),
         max(pair_tv), time.time() - tA),
      ntree == 96 and max(tr_tv) < 3e-15 and tr_supp == {1984} and tr_canc == {256}
      and max(tr_res) < 1e-13 and max(tr_dtv) < 1e-13 and max(pair_tv) < 2e-15)

CTRL_C = [("antipodal pairs {0,7},{1,6},{2,5},{3,4}", [[0, 7], [1, 6], [2, 5], [3, 4]]),
          ("adjacent pairs {0,1},{2,3},{4,5},{6,7}", [[0, 1], [2, 3], [4, 5], [6, 7]]),
          ("faces {0,1,2,3},{4,5,6,7}", [[0, 1, 2, 3], [4, 5, 6, 7]]),
          ("one corner at a time 0..7", [[v] for v in range(8)]),
          ("closed star {0,1,2,4} then {7}", [[0, 1, 2, 4], [7]])]
ctrl = {}
for lab, sets in CTRL_C:
    row = []
    for tau in (0.5, 2.0):
        r = run_tree(SC, [star_mask(CC, S) for S in sets], tau)
        row.append(cube_census(r["law"]))
    pref = [eigenset_test(hC, WC, closure(CC, sorted(set(v for S in sets[:k + 1] for v in S))),
                          K=KC)[1] for k in range(len(sets))]
    ctrl[lab] = (row, pref)
c_anti, c_adj, c_face, c_one, c_star = [ctrl[l][0] for l, _ in CTRL_C]
p_anti, p_adj, p_face, p_one, p_star = [ctrl[l][1] for l, _ in CTRL_C]
check("A5 T4 cube controls fail exactly where a prefix closure fails the criterion (TV at "
      "tau=0.5/2.0, prefix residuals): antipodal pairs %.3f/%.3f (first pair eigen at %.0e, prefix "
      "{0,1,6,7} irregular at %.3f), adjacent pairs %.3f/%.3f (%.3f), the two faces %.3f/%.3f "
      "(%.3f), one corner at a time %.3f/%.3f (%.0e then %.3f); the closed star {0,1,2,4} then {7} "
      "is a sequence of eigen-sets (%.0e, %.0e) and exact, %.1e/%.1e on support %d."
      % (c_anti[0][0], c_anti[1][0], p_anti[0], p_anti[1], c_adj[0][0], c_adj[1][0], p_adj[0],
         c_face[0][0], c_face[1][0], p_face[0], c_one[0][0], c_one[1][0], p_one[0], p_one[1],
         p_star[0], p_star[1], c_star[0][0], c_star[1][0], c_star[0][1]),
      p_anti[0] < 1e-12 and p_anti[1] > 0.7 and p_adj[0] > 0.49 and p_face[0] > 0.6
      and p_one[0] < 1e-12 and p_one[1] > 0.49 and p_star[0] < 1e-12 and p_star[1] < 1e-12
      and min(c_anti[0][0], c_anti[1][0], c_adj[0][0], c_adj[1][0], c_face[0][0], c_face[1][0],
              c_one[0][0], c_one[1][0]) > 0.02
      and c_star[0][0] < 1e-14 and c_star[1][0] < 1e-14 and c_star[0][1] == 1984)
t_cube = time.time() - T0


# ==========================================================================
# B. THE 2x2x3 SLAB -- the criterion many-body on 2^20, and the complete one-particle
#    classification of all 4095 vertex sets
CS = cluster(2, 2, 3)
EnS = Enc(CS["V"], CS["EDGES"], CS["FACES"])
AUDS = audit(EnS)
ZS = np.arange(1 << EnS.NQ, dtype=np.int64)
NVS = np.zeros(1 << EnS.NQ, dtype=np.int8)
for v in range(CS["V"]):
    NVS += parity(ZS & EnS.STARMASK[v])
J = np.flatnonzero(NVS == 6).astype(np.int64)
locS = -np.ones(1 << EnS.NQ, dtype=np.int64)
locS[J] = np.arange(len(J))
del ZS, NVS
SS = Space(EnS, CS["eta"], J, locS, "slab")
SS.set_gens(AUDS["gens"])
tt = np.arange(SS.n, dtype=np.float64)
v0 = SS.project_code(np.cos(0.7 * tt + 0.3) + 1j * np.cos(1.3 * tt + 1.1))
v0 /= np.linalg.norm(v0)
wS, US = spla.eigsh(SS.H, k=3, which="SA", v0=v0, tol=0, maxiter=20000)
sea_s = SS.project_code(US[:, 0])
sea_s /= np.linalg.norm(sea_s)
sh = float(np.abs(wS).max()) + 6.0
for it in range(120):
    sea_s = SS.project_code(sh * sea_s - SS.H @ sea_s)
    sea_s /= np.linalg.norm(sea_s)
    if it % 20 == 19:
        Hs = SS.H @ sea_s
        evq = math.fsum((np.conj(sea_s) * Hs).real) / math.fsum(np.abs(sea_s) ** 2)
        if np.linalg.norm(Hs - evq * sea_s) < 1e-13:
            break
Hs = SS.H @ sea_s
E_SEA_S = math.fsum((np.conj(sea_s) * Hs).real) / math.fsum(np.abs(sea_s) ** 2)
sea_res_s = float(np.linalg.norm(Hs - E_SEA_S * sea_s))
del Hs, US, v0, tt
SS.set_sea(sea_s)
SMS = summarize(CS)
hS, WS, KS = CS["h"], SMS["W"], SMS["W"] @ SMS["W"].conj().T
COMPS_S = SMS["comps"]
EVEN_S = [c for c in COMPS_S if CS["sub"][c[0]] == 0]
ODD_S = [c for c in COMPS_S if CS["sub"][c[0]] == 1]
t_sea = time.time() - T0 - t_cube

IRREG_S = [S for S in (list(x) for x in itertools.combinations(range(12), 4))
           if not regular(CS, S)]
FAMILY = ([[v] for v in range(12)]
          + [list(S) for S in itertools.combinations(range(12), 2)]
          + IRREG_S
          + [[0, 2, 10], [1, 9, 11], [3, 5, 7], [4, 6, 8], [0, 2, 4, 7],
             [0, 3, 6, 9], [0, 1, 3, 4, 6, 7, 9, 10], [0, 2, 4, 7, 9, 11]])
tA = time.time()
sw_res = sw_ev = sw_odds = 0.0
s8_res = s8_ev = s8_odds = 0.0
fam_eig = []
fam_irr = 0.0
nfam_reg = 0
for S in FAMILY:
    Sp = closure(CS, S)
    R, p, ev, resid, live, pat = mb_outcomes(SS, CS, Sp)
    rows, mx1, nl = eigenset_test(hS, WS, Sp, K=KS)
    rmap = {r["pattern"]: r for r in rows}
    scale = 2.0 ** (-(len(R) - (len(Sp) if len(Sp) < 12 else 11)))
    mbmax = float(resid[live].max())
    if regular(CS, S):
        nfam_reg += 1
        for w in np.flatnonzero(live):
            r1 = rmap[tuple(int(x) for x in pat[w])]
            dr, de, do = (abs(resid[w] - r1["resid"]), abs(ev[w] - r1["ev"]),
                          abs(p[w] - scale * r1["prob"]))
            sw_res, sw_ev, sw_odds = max(sw_res, dr), max(sw_ev, de), max(sw_odds, do)
            if len(Sp) <= 8:
                s8_res, s8_ev, s8_odds = max(s8_res, dr), max(s8_ev, de), max(s8_odds, do)
    else:
        fam_irr = max(fam_irr, mbmax)
    if mbmax < 1e-9:
        fam_eig.append(tuple(Sp))
t_fam = time.time() - tA
check("B1 [exact; numerical, 1e-12] slab 2x2x3 open in z: R0-R4 %s, k=%d, code %d, flux %s x%d, "
      "2^20 record space on the half-filled |J|=%d; sea E=%.12f=-(8+2sqrt2) (%.0e), resid %.1e, "
      "support %d = the one-particle sum %.9f, gap %.4f. T1 criterion many-body vs one-particle on "
      "a declared family of %d sets (all singletons, all pairs, all %d irregular size-4 sets, eight "
      "declared larger ones): over the %d regular ones max|resid_mb-resid_1p| %.3e, max|<H_R>_mb-Tr| "
      "%.3e, max odds gap %.1e, each attained at |S\'|<=8 (%.3e/%.3e/%.1e), the floor of a "
      "473088-term reduction; %d eigen closures; every irregular set NON-eigen, >= %.3f. [%.0fs]"
      % (AUDS["ok"], AUDS["k"], AUDS["code_dim"], set(face_flux(CS)), len(CS["FACES"]), SS.n,
         E_SEA_S, abs(E_SEA_S + 8 + 2 * np.sqrt(2)), sea_res_s, SS.SUPP, SMS["E_sea"], SMS["gap"],
         len(FAMILY), len(IRREG_S), nfam_reg, sw_res, sw_ev, sw_odds, s8_res, s8_ev, s8_odds,
         len(set(fam_eig)), fam_irr, t_fam),
      AUDS["ok"] and AUDS["k"] == 9 and AUDS["code_dim"] == 2048 and set(face_flux(CS)) == {-1}
      and SS.n == 473088 and abs(E_SEA_S + 8 + 2 * np.sqrt(2)) < 1e-10 and sea_res_s < 1e-10
      and SS.SUPP == 411648 and abs(SMS["E_sea"] - E_SEA_S) < 1e-10 and SS.xpart_ok
      and len(IRREG_S) == 21 and fam_irr > 0.1
      and sw_res < 5e-13 and sw_ev < 5e-12 and sw_odds < 1e-13
      and s8_res == sw_res and s8_ev == sw_ev and s8_odds == sw_odds)

SS.HQSEA = None
SS.HSEA = None
SC.HQSEA = None
SC.HSEA = None
tA = time.time()
eigcl = set()
noncl = set()
nirr_s = 0
for m in range(1, 13):
    for S in itertools.combinations(range(12), m):
        S = list(S)
        if not regular(CS, S):
            nirr_s += 1
        Sp = tuple(closure(CS, S))
        if Sp in eigcl or Sp in noncl:
            continue
        rows, mx, nl = eigenset_test(hS, WS, Sp, K=KS)
        (eigcl if mx < 1e-9 else noncl).add(Sp)
labS = SMS["lab"]
subS = CS["sub"]


def comp_union(Sx):
    return all(set(COMPS_S[labS[v]]) <= set(Sx) for v in Sx)


def parts(Sp):
    return [v for v in Sp if subS[v] == 0], [v for v in Sp if subS[v] == 1]


def adjacent(SA, SB):
    return any(hS[a, b] != 0 for a in SA for b in SB)


allcl = eigcl | noncl
ss_cl = [s for s in allcl if len(set(subS[v] for v in s)) == 1]
ss_eig = [s for s in ss_cl if s in eigcl]
mixed_e = [s for s in eigcl if parts(s)[0] and parts(s)[1]]
cu_non = [s for s in noncl if comp_union(parts(s)[0]) and comp_union(parts(s)[1])]
clos_of_cu = set()
for r in range(1, 5):
    for pr in (0, 1):
        for cc in itertools.combinations([c for c in COMPS_S if subS[c[0]] == pr], r):
            clos_of_cu.add(tuple(closure(CS, sorted(v for c in cc for v in c))))
unexplained = [s for s in mixed_e if adjacent(*parts(s)) and s not in clos_of_cu]
minimal = sorted(s for s in eigcl if not any(set(t) < set(s) for t in eigcl))
check("B2 [numerical, 1e-13] T2 structure, slab, COMPLETE one-particle over all 4095 vertex sets "
      "(%d distinct closures, %d eigen): of the %d single-sublattice closures exactly %d are "
      "eigen-sets and exactly %d are class unions -- eigen <=> union of classes, set by set -- and "
      "the minimal eigen-sets are the %d T2 components %s. All %d eigen closures have both "
      "sublattice parts class unions; the %d mixed ones are %d non-adjacent cross unions and %d "
      "closures of a class union (%d unexplained); the %d non-eigen class-union closures are all "
      "adjacent; %d of the 4095 sets are irregular. [%.0fs]"
      % (len(allcl), len(eigcl), len(ss_cl), len(ss_eig), sum(comp_union(list(s)) for s in ss_cl),
         len(minimal), "".join(str(list(s)).replace(" ", "") for s in minimal), len(eigcl),
         len(mixed_e), sum(not adjacent(*parts(s)) for s in mixed_e),
         sum(adjacent(*parts(s)) for s in mixed_e), len(unexplained), len(cu_non), nirr_s,
         time.time() - tA),
      len(eigcl) == 33 and len(ss_cl) == 80 and len(ss_eig) == 20
      and all((s in eigcl) == comp_union(list(s)) for s in ss_cl) and len(minimal) == 8
      and sorted(minimal) == sorted(tuple(c) for c in COMPS_S)
      and all(comp_union(parts(s)[0]) and comp_union(parts(s)[1]) for s in eigcl)
      and len(mixed_e) == 13 and sum(not adjacent(*parts(s)) for s in mixed_e) == 4
      and not unexplained and len(cu_non) == 132 and all(adjacent(*parts(s)) for s in cu_non)
      and all(c in eigcl for c in clos_of_cu) and nirr_s == 547 and fam_irr > 0.1)

tA = time.time()
st_tv = []
st_supp = set()
st_res = []
st_dtv = []
ntree_s = 0
for part in (EVEN_S, ODD_S):
    for order in itertools.permutations(range(4)):
        r = run_tree(SS, [star_mask(CS, part[k]) for k in order], 0.5)
        st_tv.append(r["levels"][-1]["full_tv"])
        st_supp.add(r["levels"][-1]["support"])
        st_res.append(max(L["res_max"] for L in r["levels"]))
        st_dtv.append(max(L["dtv_max"] for L in r["levels"]))
        ntree_s += 1
st2_tv = [run_tree(SS, [star_mask(CS, c) for c in part], 2.0)["levels"][-1]["full_tv"]
          for part in (EVEN_S, ODD_S)]
CTRL_S = [("star(0) alone, then {2},{4},{7},{9,11}", [[0], [2], [4], [7], [9, 11]]),
          ("the z=0 plaquette {0,3,6,9}, then {1,4,7,10}, then {2,5,8,11}",
           [[0, 3, 6, 9], [1, 4, 7, 10], [2, 5, 8, 11]]),
          ("the coarse cell {0,1,3,4,6,7,9,10}, then the top plane {2,5,8,11}",
           [[0, 1, 3, 4, 6, 7, 9, 10], [2, 5, 8, 11]]),
          ("the adjacent pair {0,1}, then {2},{4},{7},{9,11}", [[0, 1], [2], [4], [7], [9, 11]]),
          ("all six even corners in one tick", [[0, 2, 4, 7, 9, 11]])]
ctrl_s = {}
for lab, sets in CTRL_S:
    r = run_tree(SS, [star_mask(CS, S) for S in sets], 0.5)
    lv = r["levels"]
    ctrl_s[lab] = (lv[-1]["full_tv"], lv[-1]["support"],
                   max(L["res_max"] for L in lv[:-1]) if len(lv) > 1 else lv[0]["res_max"])
cs = [ctrl_s[l][0] for l, _ in CTRL_S]
check("B3 [numerical, 1e-13] T4 slab, whole classes formed jointly with evolution on the 2^20 "
      "record space: all %d orders of the four even and of the four odd classes at tau=0.5 -- full "
      "20-edge law TV <= %.1e, support %s = the sea's, node residual <= %.1e, displacement <= %.1e; "
      "identity order at tau=2.0 <= %.1e. Controls (TV, tau=0.5): star(0) alone then the rest %.4f "
      "(support %d, own residual %.4f), the z=0 plaquette %.3f, the coarse cell %.3f, the adjacent "
      "pair {0,1} %.3f (support %d) -- each failing exactly at the levels whose prefix closure "
      "fails (%.2f-%.2f); all six even corners in ONE tick %.1e. [%.0fs]"
      % (ntree_s, max(st_tv), sorted(st_supp), max(st_res), max(st_dtv), max(st2_tv), cs[0],
         ctrl_s[CTRL_S[0][0]][1], ctrl_s[CTRL_S[0][0]][2], cs[1], cs[2], cs[3],
         ctrl_s[CTRL_S[3][0]][1], min(ctrl_s[l][2] for l, _ in CTRL_S[:4]),
         max(ctrl_s[l][2] for l, _ in CTRL_S[:4]), cs[4], time.time() - tA),
      ntree_s == 48 and max(st_tv) < 1.9e-15 and st_supp == {411648} and max(st_res) < 2.5e-13
      and max(st2_tv) < 1e-14 and 0.019 < cs[0] < 0.022 and ctrl_s[CTRL_S[0][0]][1] == 428032
      and 0.13 < cs[1] < 0.15 and 0.07 < cs[2] < 0.09 and 0.29 < cs[3] < 0.31
      and ctrl_s[CTRL_S[3][0]][1] == 455680 and cs[4] < 1e-14
      and min(ctrl_s[l][2] for l, _ in CTRL_S[:4]) > 0.2)
t_slab = time.time() - T0 - t_cube - t_sea


# ==========================================================================
# C. THE CLASSIFICATION ON GROWING CLUSTERS -- one-particle             (T2/t2_classify.py)
def repair_units(C, comps, lab):
    """the declared larger units: a plaquette of four stars, a coarse cell of eight, a coarse
    line, a coarse plane, the whole class of corner 0, that class minus one corner, two classes."""
    idx, L = C["idx"], C["L"]
    out = [("plaquette", [idx[(0, 0, 0)], idx[(1, 0, 0)], idx[(0, 1, 0)], idx[(1, 1, 0)]]),
           ("coarse cell", [idx[(x, y, z)] for x in (0, 1) for y in (0, 1) for z in (0, 1)])]
    cl = [v for v in range(C["V"]) if C["cls"][v] == C["cls"][0]]
    out.append(("coarse line", [v for v in cl if C["coords"][v][1] == 0 and C["coords"][v][2] == 0]))
    out.append(("coarse plane", [v for v in cl if C["coords"][v][2] == 0]))
    out.append(("whole class", cl))
    if len(cl) > 2:
        out.append(("class minus one", cl[1:]))
    two = [v for v in range(C["V"]) if C["cls"][v] in (C["cls"][0], C["cls"][idx[(1, 1, 0)]])]
    out.append(("two classes", two))
    return out


def classify(C, N=None, max_union=3, reduce_torus=False, minimal_max=8, small=False,
             prefix=True, repairs=False, modes=True, comp_subset=None, mode_corners=None):
    SM = summarize(C, N)
    V, h, W = C["V"], C["h"], SM["W"]
    K = W @ W.conj().T
    hp = hpowers(h)
    comps, lab = SM["comps"], SM["lab"]
    out = dict(V=V, N=SM["N"], gap=SM["gap"], nzero=SM["nzero"], E_sea=SM["E_sea"],
               ncomp=len(comps), sizes=sorted(set(len(c) for c in comps)),
               recs=sorted(set(n_records(C, c) for c in comps)),
               t2_exact=float(np.max(np.abs(SM["h2"] - np.diag(np.diag(SM["h2"]))
                                            - SM["T2"] * SM["h2"]))),
               t2_geom=bool(np.array_equal(SM["T2"], straight_two_step(C))),
               t2_ones=bool(np.all(np.abs(SM["h2"][SM["T2"]] - 1.0) < 1e-12)),
               t2_edges=int(SM["T2"].sum()) // 2, flux=set(face_flux(C)))
    if max_union:
        out["nsets"], out["nscreen"], out["eig"] = enumerate_unions(
            C, hp, h, W, K, max_union=max_union, reduce_torus=reduce_torus)
    cmax = 0.0
    cmin_sub = float("inf")
    npat = set()
    tested = comps if comp_subset is None else comps[:comp_subset]
    for c in tested:
        mx, nl, how = full_or_declared(h, W, K, c, small=small)
        cmax = max(cmax, mx)
        npat.add(nl)
        if len(c) <= minimal_max and len(c) > 1:
            for r in range(1, len(c)):
                for sub_ in itertools.combinations(c, r):
                    cmin_sub = min(cmin_sub, eigenset_test(h, W, list(sub_), K=K)[1])
        elif len(c) > minimal_max:
            subs = ([[v] for v in c] + [list(x) for x in itertools.combinations(c[:8], 2)]
                    + [[v for v in c if v != u] for u in c[:3]])
            for sub_ in subs:
                cmin_sub = min(cmin_sub, full_or_declared(h, W, K, sub_, small=small)[0])
    out["ncomp_tested"] = len(tested)
    out["class_resid"] = cmax
    out["class_pats"] = sorted(npat)
    out["sub_min"] = cmin_sub
    evenc = [c for c in comps if C["sub"][c[0]] == 0]
    oddc = [c for c in comps if C["sub"][c[0]] == 1]
    cov = True
    for cc in (evenc, oddc):
        cover = np.zeros(len(C["EDGES"]), dtype=int)
        for c in cc:
            for q in set(q for v in c for q in C["STAR"][v]):
                cover[q] += 1
        cov &= bool(np.all(cover == 1))
    out["coverage"] = cov and len(evenc) + len(oddc) == len(comps)
    if prefix and len(evenc) <= 4:
        pref = set()
        for order in itertools.permutations(range(len(evenc))):
            acc = []
            for k in order[:-1]:
                acc = sorted(set(acc) | set(evenc[k]))
                pref.add(tuple(fast_closure(C, acc)))
        out["npref"] = len(pref)
        out["pref_sizes"] = (min(len(p) for p in pref), max(len(p) for p in pref))
        out["pref_resid"] = max(full_or_declared(h, W, K, list(p), small=small)[0]
                                for p in pref)
    if modes:
        md = {}
        for v in (range(V) if mode_corners is None else mode_corners):
            dK, d1, d0 = krylov_dims(h, W, [v])
            mx = eigenset_test(h, W, [v], K=K)[1]
            md.setdefault((int(C["deg"][v]), len(comps[lab[v]]), dK), []).append(mx)
        out["modes"] = {k: (len(v), min(v), max(v)) for k, v in md.items()}
    if repairs:
        out["repair"] = {}
        for name, S in repair_units(C, comps, lab):
            Sp = fast_closure(C, S)
            out["repair"][name] = full_or_declared(h, W, K, Sp, small=small)[0]
    return out


tA = time.time()
BOXES = [(2, 2, L) for L in range(3, 9)] + [(2, 3, 3), (2, 3, 4), (2, 3, 5), (2, 3, 6),
                                            (3, 3, 3), (3, 3, 4), (4, 4, 4)]
RES = {}
for dims in BOXES:
    RES[dims] = classify(cluster(*dims), repairs=dims in ((2, 2, 8), (2, 3, 6), (3, 3, 3),
                                                          (4, 4, 4)))
t_box = time.time() - tA
r22 = [RES[(2, 2, L)] for L in range(3, 9)]
check("C1 [numerical, 1e-13] T3 on 2x2xL, L=3..8, complete enumeration of every union of up to "
      "three stars: sets %s, eigen-sets %s -- 22 on 2x2x3 (18 class unions, 4 non-adjacent cross "
      "unions), then exactly the z-columns, NONE on 2x2x8; the 8 classes are eigen-sets at <= %.1e "
      "over all their patterns, every proper subset fails (smallest %.3f); T2 = the straight-2-step "
      "graph, h^2-D-T2 = %.1e, entries +1. [%.0fs]"
      % ([r["nsets"] for r in r22], [len(r["eig"]) for r in r22],
         max(r["class_resid"] for r in r22), min(r["sub_min"] for r in r22),
         max(r["t2_exact"] for r in r22), t_box),
      [r["nsets"] for r in r22] == [298, 696, 1350, 2324, 3682, 5488]
      and [len(r["eig"]) for r in r22] == [22, 8, 8, 8, 4, 0]
      and max(r["class_resid"] for r in r22) < 1e-13
      and min(r["sub_min"] for r in r22) > 0.15
      and max(r["t2_exact"] for r in r22) == 0.0
      and all(r["t2_geom"] and r["t2_ones"] and r["flux"] == {-1} and r["ncomp"] == 8 for r in r22))

r23 = [RES[d] for d in ((2, 3, 3), (2, 3, 4), (2, 3, 5), (2, 3, 6), (3, 3, 3), (3, 3, 4))]
check("C2 [numerical, 1e-13] T3 on 2x3x3, 2x3x4, 2x3x5, 2x3x6, 3x3x3, 3x3x4, complete enumeration "
      "of every union of up to three stars: sets %s, eigen-sets %s -- each a class union or a "
      "non-adjacent cross union, none of any other shape; the 8 classes are eigen-sets at <= %.1e, "
      "every proper subset of a class of size <= 8 fails (smallest %.3f); N %s, gap %s, zero modes "
      "%s. [%.0fs]"
      % ([r["nsets"] for r in r23], [len(r["eig"]) for r in r23],
         max(r["class_resid"] for r in r23), min(r["sub_min"] for r in r23),
         [r["N"] for r in r23], ["%.2f" % r["gap"] for r in r23], [r["nzero"] for r in r23],
         time.time() - tA),
      [r["nsets"] for r in r23] == [987, 2324, 4525, 7806, 3303, 7806]
      and [len(r["eig"]) for r in r23] == [10, 4, 4, 4, 4, 2]
      and max(r["class_resid"] for r in r23) < 1e-13 and min(r["sub_min"] for r in r23) > 0.15
      and all(r["t2_exact"] == 0.0 and r["t2_geom"] and r["ncomp"] == 8 for r in r23))

r44 = RES[(4, 4, 4)]
rp = r44["repair"]
check("C3 [numerical, 1e-13] T3 on the 4x4x4 open box (V=64, N=32, gap %.3f): the 8 classes are "
      "2x2x2 coarse cubes of 8 corners; of all %d unions of up to three stars NOT ONE is an "
      "eigen-set (none passes the screen), while every class is one at <= %.1e over all 256 patterns "
      "and all 254 proper subsets fail (smallest %.3f); every corner sees 8 modes, %.2f-%.2f; "
      "plaquette %.3f, cell %.3f, line %.3f, plane %.3f, class minus one %.3f all fail, two classes "
      "exact at %.1e."
      % (r44["gap"], r44["nsets"], r44["class_resid"], r44["sub_min"],
         min(v[1] for v in r44["modes"].values()), max(v[2] for v in r44["modes"].values()),
         rp["plaquette"], rp["coarse cell"], rp["coarse line"], rp["coarse plane"],
         rp["class minus one"], rp["two classes"]),
      r44["nsets"] == 43744 and r44["nscreen"] == 0 and len(r44["eig"]) == 0
      and r44["class_resid"] < 1e-13 and r44["sub_min"] > 0.25 and rp["whole class"] < 1e-13
      and rp["two classes"] < 1e-13 and min(rp[k] for k in ("plaquette", "coarse cell",
                                                            "coarse line", "coarse plane",
                                                            "class minus one")) > 0.3
      and set(k[2] for k in r44["modes"]) == {8})

r_all = [RES[d] for d in BOXES]
check("C4 [numerical, 1e-12] T4 coverage and sequential exactness, one-particle, on all %d open "
      "boxes: the even classes (equally the odd) partition the record sites, and every proper prefix "
      "closure of all 24 orders of the four even classes is itself an eigen-set (%d distinct "
      "closures of sizes %d to %d, max residual %.1e), so the classes form in any order."
      % (len(BOXES), sum(r["npref"] for r in r_all), min(r["pref_sizes"][0] for r in r_all),
         max(r["pref_sizes"][1] for r in r_all), max(r["pref_resid"] for r in r_all)),
      all(r["coverage"] for r in r_all) and max(r["pref_resid"] for r in r_all) < 2.5e-13
      and sum(r["npref"] for r in r_all) > 100)


# ==========================================================================
# D. PERIODIC TORI -- the twist sectors and the classification in the ground sector
def twist_table(dims):
    rows = []
    for tw in itertools.product((0, 1), repeat=3):
        C = cluster(*dims, periodic=(True, True, True), twist=tw)
        assert set(face_flux(C)) == {-1}
        V = C["V"]
        N = V // 2
        w = np.linalg.eigvalsh(C["h"])
        rows.append((tw, float(np.sum(w[:N])), float(w[N] - w[N - 1]),
                     int(np.sum(np.abs(w) < 1e-9))))
    Emin = min(r[1] for r in rows)
    ground = [r for r in rows if abs(r[1] - Emin) < 1e-9]
    return rows, ground


t_tori = time.time()
tA = time.time()
TT = {d: twist_table(d) for d in ((4, 4, 4), (6, 6, 6), (4, 4, 6), (8, 8, 8))}
g4, g6, g46, g8 = [TT[d][1][0] for d in ((4, 4, 4), (6, 6, 6), (4, 4, 6), (8, 8, 8))]
per = {d: [r for r in TT[d][0] if r[0] == (0, 0, 0)][0] for d in TT}
check("D1 [numerical, 1e-9] T5 twist sectors of the tori, all 8 of each, N=V/2, flux -1 on every "
      "face including the wrap-around ones: 4^3 ground %s E %.3f=-32sqrt6 gap %.3f, its periodic "
      "sector gap %.1e with %d zero modes and no sea; 6^3 ground %s E %.3f gap %.3f (periodic AND "
      "gapped), all-antiperiodic %.1e with %d zero modes; 4x4x6 ground %s E %.3f gap %.3f; 8^3 "
      "ground %s E %.3f gap %.3f, periodic %.1e with %d zero modes and no sea. [%.0fs]"
      % (g4[0], g4[1], g4[2], per[(4, 4, 4)][2], per[(4, 4, 4)][3],
         g6[0], g6[1], g6[2],
         [r for r in TT[(6, 6, 6)][0] if r[0] == (1, 1, 1)][0][2],
         [r for r in TT[(6, 6, 6)][0] if r[0] == (1, 1, 1)][0][3],
         g46[0], g46[1], g46[2], g8[0], g8[1], g8[2], per[(8, 8, 8)][2], per[(8, 8, 8)][3],
         time.time() - tA),
      g4[0] == (1, 1, 1) and abs(g4[1] + 32 * np.sqrt(6)) < 1e-6 and g4[2] > 4.8
      and per[(4, 4, 4)][3] == 8 and per[(4, 4, 4)][2] < 1e-9
      and g6[0] == (0, 0, 0) and abs(g6[2] - 3.4641) < 1e-3 and g6[3] == 0
      and [r for r in TT[(6, 6, 6)][0] if r[0] == (1, 1, 1)][0][3] == 8
      and g46[0] == (1, 1, 0) and abs(g46[2] - 4.4721) < 1e-3
      and g8[0] == (1, 1, 1) and abs(g8[2] - 2.6513) < 1e-3
      and per[(8, 8, 8)][3] == 8 and per[(8, 8, 8)][2] < 1e-9)

tA = time.time()
C4 = cluster(4, 4, 4, periodic=(True, True, True), twist=(1, 1, 1))
SM4 = summarize(C4)
h4, W4 = C4["h"], SM4["W"]
K4 = W4 @ W4.conj().T
hp4 = hpowers(h4)
n4 = 0
eig4 = {1: 0, 2: 0}
adj_fail4 = 0
cross_ok4 = 0
same4 = 0
for m in (1, 2):
    sets = [list(S) for S in itertools.combinations(range(64), m)]
    n4 += len(sets)
    ok = screen_sets(hp4, sets)
    for S, good in zip(sets, ok):
        if not good:
            continue
        if eigenset_test(h4, W4, S, K=K4)[1] < 1e-9:
            eig4[m] += 1
            if m == 2:
                if C4["sub"][S[0]] == C4["sub"][S[1]]:
                    same4 += 1
                else:
                    cross_ok4 += 1
    if m == 2:
        adj_fail4 = sum(1 for S in sets if h4[S[0], S[1]] != 0
                        and eigenset_test(h4, W4, S, K=K4)[1] >= 1e-9)
R4T = classify(C4, max_union=0, prefix=False, repairs=True, modes=False)
rp4 = R4T["repair"]
check("D2 [numerical, 1e-13] T5 the 4^3 torus, ground sector (1,1,1): on a side of length 4 the two "
      "straight 2-paths u -> u +- 2 e_a hit the same corner with opposite signs and cancel, so T2=0 "
      "and h^2=6I exactly (%.0e) -- FLAT, %d singleton classes. Complete over every union of one or "
      "two stars (%d sets): all 64 single corners are eigen-sets, of the 2016 pairs exactly the %d "
      "same-sublattice and %d non-adjacent cross ones are, all %d adjacent pairs fail; line, plane, "
      "class, class minus one, two classes all eigen (<= %.1e), the adjacent plaquette %.2f and cell "
      "%.2f fail -- an L=4 cancellation (+2 = -2 mod 4), not a lattice property. [%.0fs]"
      % (float(np.max(np.abs(SM4["h2"] - 6 * np.eye(64)))), len(SM4["comps"]), n4, same4,
         cross_ok4, adj_fail4, max(rp4[k] for k in ("coarse line", "coarse plane", "whole class",
                                                    "class minus one", "two classes")),
         rp4["plaquette"], rp4["coarse cell"], time.time() - tA),
      float(np.max(np.abs(SM4["h2"] - 6 * np.eye(64)))) < 1e-12 and not SM4["T2"].any()
      and len(SM4["comps"]) == 64 and n4 == 2080 and eig4[1] == 64 and same4 == 992
      and cross_ok4 == 832 and adj_fail4 == 192
      and max(rp4[k] for k in ("coarse line", "coarse plane", "whole class", "class minus one",
                               "two classes")) < 1e-13
      and rp4["plaquette"] > 1.3 and rp4["coarse cell"] > 2.0)

tA = time.time()
C6 = cluster(6, 6, 6, periodic=(True, True, True), twist=(0, 0, 0))
R6 = classify(C6, max_union=3, reduce_torus=True, repairs=True, prefix=False,
              comp_subset=2, mode_corners=[0, 1, C6["idx"][(1, 1, 1)]])
check("D3 [numerical, 1e-13] T5 the 6^3 torus, ground sector the PERIODIC (0,0,0), gap %.3f, no "
      "zero modes: T2 is the straight-2-step graph (%d edges, h^2-D-T2 = %.1e, entries +1), its "
      "components the %d classes of 27 corners, %d records each. Of the %d unions of up to three "
      "stars -- every such set modulo the 27 even translations -- NOT ONE passes the screen; the "
      "classes are eigen-sets at <= %.1e over %s patterns and the declared proper subsets (27 "
      "singles, 28 pairs, three class-minus-one) fail at >= %.3f; a corner sees 8 modes, %.4f; "
      "plaquette %.3f, cell %.3f, line %.3f, plane %.3f, class minus one %.3f fail, two classes "
      "exact at %.1e. [%.0fs]"
      % (R6["gap"], R6["t2_edges"], R6["t2_exact"], R6["ncomp"], R6["recs"][0], R6["nsets"],
         R6["class_resid"], R6["class_pats"], R6["sub_min"],
         list(R6["modes"].values())[0][1], R6["repair"]["plaquette"], R6["repair"]["coarse cell"],
         R6["repair"]["coarse line"], R6["repair"]["coarse plane"],
         R6["repair"]["class minus one"], R6["repair"]["two classes"], time.time() - tA),
      abs(R6["gap"] - 3.4641) < 1e-3 and R6["nzero"] == 0 and R6["t2_exact"] == 0.0
      and R6["t2_geom"] and R6["t2_ones"] and R6["t2_edges"] == 648 and R6["ncomp"] == 8
      and R6["sizes"] == [27] and R6["recs"] == [162] and R6["nsets"] == 179804
      and R6["nscreen"] == 0 and len(R6["eig"]) == 0 and R6["class_resid"] < 1e-13
      and R6["sub_min"] > 0.35 and set(k[2] for k in R6["modes"]) == {8}
      and R6["repair"]["whole class"] < 1e-13 and R6["repair"]["two classes"] < 1e-13
      and min(R6["repair"][k] for k in ("plaquette", "coarse cell", "coarse line", "coarse plane",
                                        "class minus one")) > 0.35 and R6["coverage"])

tA = time.time()
C8 = cluster(8, 8, 8, periodic=(True, True, True), twist=(1, 1, 1))
R8 = classify(C8, max_union=1, small=True, repairs=False, prefix=False, comp_subset=1,
              minimal_max=0, mode_corners=[0])
C46 = cluster(4, 4, 6, periodic=(True, True, True), twist=(1, 1, 0))
R46 = classify(C46, max_union=3, repairs=True, prefix=False, mode_corners=[0, 1])
check("D4 [numerical, 1e-12] T5 the 8^3 torus, ground sector (1,1,1), gap %.3f: T2 is the "
      "straight-2-step graph (%d edges, %.1e), %d classes of 64 corners, %d records each; the class "
      "of corner 0 is an eigen-set at %.1e over a declared %d-pattern family, its declared proper "
      "subsets fail at >= %.3f, and of the %d single corners NOT ONE passes the screen (corner 0: 8 "
      "modes, %.4f). The 4x4x6 torus, ground (1,1,0), gap %.3f: the L=4 directions are antiperiodic "
      "so their 2-steps cancel and T2 keeps only z -- %d components, the z-columns of 3 corners (%d "
      "records) -- and of all %d unions of up to three stars exactly %d are eigen-sets, exactly "
      "those columns (<= %.1e); the class of 12 is one at %.1e over all 4096 patterns, class minus "
      "one %.4f; plaquette %.3f, cell %.3f, line %.3f, plane %.3f. [%.0fs]"
      % (R8["gap"], R8["t2_edges"], R8["t2_exact"], R8["ncomp"], R8["recs"][0],
         R8["class_resid"], R8["class_pats"][0], R8["sub_min"], R8["nsets"],
         list(R8["modes"].values())[0][1], R46["gap"], R46["ncomp"], R46["recs"][0],
         R46["nsets"], len(R46["eig"]), R46["class_resid"], R46["repair"]["whole class"],
         R46["repair"]["class minus one"], R46["repair"]["plaquette"],
         R46["repair"]["coarse cell"], R46["repair"]["coarse line"],
         R46["repair"]["coarse plane"], time.time() - tA),
      abs(R8["gap"] - 2.6513) < 1e-3 and R8["t2_exact"] == 0.0 and R8["t2_geom"]
      and R8["ncomp"] == 8 and R8["sizes"] == [64] and R8["recs"] == [384]
      and R8["class_resid"] < 1e-12 and R8["sub_min"] > 0.35 and R8["nsets"] == 512
      and R8["nscreen"] == 0 and set(k[2] for k in R8["modes"]) == {8}
      and abs(R46["gap"] - 4.4721) < 1e-3 and R46["ncomp"] == 32 and R46["sizes"] == [3]
      and R46["recs"] == [18] and R46["nsets"] == 147536 and len(R46["eig"]) == 32
      and R46["class_resid"] < 1e-13 and R46["repair"]["whole class"] < 1e-13
      and R46["repair"]["class minus one"] > 0.19
      and min(R46["repair"][k] for k in ("plaquette", "coarse cell", "coarse line",
                                         "coarse plane")) > 0.27)

t_end = time.time() - T0
check("E1 [timing] cube %.0f s, slab sea %.0f s, slab many-body family + all 4095 one-particle + "
      "50 trees %.0f s, 13 open boxes %.0f s, four tori %.0f s; total %.0f s < %d s. No dense object "
      "above 4096 x 4096, peak memory under 1 GB, one process, no network, NO SEED anywhere."
      % (t_cube, t_sea, t_slab, t_box, time.time() - t_tori, t_end, AUDIT_TIMEOUT_SEC),
      t_end < AUDIT_TIMEOUT_SEC)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
