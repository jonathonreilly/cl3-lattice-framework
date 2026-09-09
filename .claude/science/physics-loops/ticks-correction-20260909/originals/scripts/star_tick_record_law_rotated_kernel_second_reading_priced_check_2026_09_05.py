#!/usr/bin/env python3
"""The star tick's record law is exactly determinantal with a rotated kernel; the second
reading keeps the ruler, the Born structure and the TT reading, and costs the sea as vacuum.

Class-A finite-dimensional runner, self-contained: nothing is imported from any worktree and
every object below is rebuilt from its definition. Qubits sit on the EDGE sites of finite
subgraphs of the cubic lattice (the 2x2x2 cube, the 2x2x3 slab, the 4^3 and 6^3 tori in their
declared twist sectors), BKSF superfast encoding (A_ij, B_v = product of Z on star(v), face
stabilisers S_f), corner parity dictionary n_v = (1 - B_v)/2, Kawamoto-Smit staggered signs
eta_x = 1, eta_y = (-1)^x, eta_z = (-1)^(x+y) -- flux -1 on every face, the wrap-around faces
of the tori included. H = -sum_e eta_e T_e with t = 1, one-particle matrix h_ij = -eta_ij; the
SEA is the code-space ground state at half filling = the Slater determinant of the N = V/2
lowest h-modes, W their span. A record at an edge site REGISTERS Z_e. The TICK is PR #7876
Model A (Lueders formation with the Born odds of the pre-record state; exp(-i tau H_R) between
formations, H_R the hop terms on the UNRECORDED edges). The STAR TICK is G4's sum sharing rule
S1: every corner's star ticks, a ticking star registers jointly all of its still-unrecorded
edge sites, and a site therefore forms at the first tick of either of its two stars.

DECLARED here, supplied by no axiom and by no parent: the corner order in which the stars tick
(the physical object is the uniform-order average -- all 8! orders on the cube, a declared
28-order family on the slab, declared symmetric families on the tori -- and single orders are
its members); and the NULL-EVENT convention, that a star tick whose edges are all already
recorded forms nothing and is followed by no evolution (the alternative is reported as a
sensitivity). tau in {0.1, 0.5, 2.0} with declared scans.

THE STRUCTURAL IDENTITY certified here. For any Model-A schedule with formation steps
i = 1..k recording edge sets U_i (R_i = U_1 u ... u U_i) and evolution U_i = exp(-i tau H_{R_i})
after each, the final record law is P(w) = || P_w U_{k-1} ... U_1 |sea> ||^2: every P_{w_j} is a
function of Z_e, e in R_j, and H_{R_i} commutes with every such Z_e for i >= j, so the
projectors move to the left and their product is P_w. Since H_{R_i} preserves the code space,
U_{k-1}...U_1|sea> = Slater(G W) with G = prod_i exp(-i tau h_{R_i}) (later factors left), so
the law of every fixed schedule is EXACTLY determinantal, P(w) = 2^-g p_K(A w) with
p_K(n) = det(diag(n) K + diag(1-n)(I-K)), K = G P G^+ a rank-N projector, A the corner-edge
incidence and 2^-g the sea's own uniform gauge factor (g = |E| - rank_F2 A = 5 on the cube,
9 on the slab). The disturbance is a unitary rotation of the sea's projector by the tick's own
restricted propagators.

Source blocks reproduced (scratch T3 of 2026-09-05, read-only; nothing imported):
  * T3/t3_core.py          Pauli algebra P/pc/comm/pact/parity, cube_cluster, cube_faces,
                           eta_ks, face_flux, cluster (boxes and tori with twists), Enc, audit,
                           code_space, Space (sparse record space with H_free), cheb_evolve,
                           tv, build_cube_mb, mb_schedule_law, sea_W, det_law,
                           corner_index_of_edges, gauge_dim, edge_mask, h_free, schedule_G,
                           star_masks, edge_masks, kernel, law_from_kernel, slab_T1,
                           build_slab_mb  (its own (T1)/(T2) tags name the tick-lane parents)
  * T3/t3_validate.py      the cube's many-body-versus-one-particle certification V1-V5
  * T3/t3_task1_cube.py    corner_law4, census4, the 8!-order census, cube_syms, the tau scans
  * T3/t3_task1_slab.py    corner_law6, census6, the declared 28-order family, prefix_residual
  * T3/t3_task2_gravity.py Torus, tensor/coords, tt_basis, cubic_group, G_dG (the
                           divided-difference Frechet derivative of every exp(-i tau h_R)),
                           stats_and_resp, numerical_rank, the assemble response matrix
  * T3/t3_task2_energy.py  E_pi = tr(h K_pi), the kernel distance and the pair statistics
  * T3/t3_task3_born.py    branch_process (every branch of the Model-A tree walked),
                           nn_odds_spread, site_menus -- the last two recast as exact
                           marginal reductions (one bincount per record subset) instead of the
                           scratch's per-condition boolean masks; the values are identical
  * T3/t3_task4_structure.py eigen_residual, the mixture marginal tests and the 64-parameter
                           best-single-Slater search from five declared starts

TWO EXACT REDUCTIONS used to bring the declared torus families inside the runner budget, and
certified here rather than assumed. For a family member whose order is the base order
translated by t, K^{(t)} = T_t K^{(0)} T_{-t}; the ruler's dressing at momentum k satisfies
T_{-t} dh T_t = e^{i k.t} dh, so the complex response field obeys
dS^{(t)}(v) = e^{i k.t} dS^{(0)}(v - t) and its Fourier component at q = k + G picks up
e^{-i G.t}. (R1) On the 4^3 torus the average over all 64 translations therefore annihilates
every G != 0 row exactly and leaves every G = 0 row unchanged, so the 3072-order O_h x T family
average is computed from the 48 rotation orders alone; the reduction is certified by running
all 64 translations of the base order explicitly. (R2) On the 6^3 torus the 27 even
translations have e^{-i G.t} = 1 for every shift G in {0, 3}^3, so the 27-translation family
average of the response matrix equals the base order's exactly; certified against explicitly
translated orders. The baseline statistic fields become their own site means under either
average, which is what the family's site/pair figures report.

Nothing is sampled and there is NO SEED anywhere: every cluster, order, pattern and schedule is
enumerated or written out, and the slab's Lanczos start is the fixed vector
cos(0.7 i + 0.3) + i cos(1.3 i + 1.1) projected into the code space. The propagator on the
2^20 record space is the Chebyshev (Jacobi-Anger) series of exp(-i tau H_R) under the rigorous
bound ||H_R|| <= the number of free edges. No dense object above 4096 x 4096 is formed (the
2^20 slab space is held sparse on the half-filling index set |J| = 473088), peak memory stays
under 1 GB, one process, no network.

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
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla
from scipy.optimize import minimize
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
# Pauli algebra in the symplectic representation, phases mod 4   (T3/t3_core.py)
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
# clusters   (T3/t3_core.py)
def cube_cluster():
    B = [(s, s ^ bit) for s in range(8) for bit in (4, 2, 1) if s ^ bit > s]
    return 8, sorted(B)


def cube_faces():
    out = []
    for ax in range(3):
        bits = [4, 2, 1]
        fb = bits[ax]
        ob = [b for b in bits if b != fb]
        for val in (0, fb):
            out.append((val, val | ob[1], val | ob[0] | ob[1], val | ob[0]))
    return out


def corner_xyz(s):
    return ((s >> 2) & 1, (s >> 1) & 1, s & 1)


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def face_flux(FACES, EDGES, eta):
    EIDX = {}
    for q, (i, j) in enumerate(EDGES):
        EIDX[(i, j)] = EIDX[(j, i)] = q
    out = []
    for cyc in FACES:
        f = 1
        for t in range(len(cyc)):
            f *= int(eta[EIDX[(cyc[t], cyc[(t + 1) % len(cyc)])]])
        out.append(f)
    return out


def cluster(Lx, Ly, Lz, periodic=(False, False, False), twist=(0, 0, 0)):
    """corner (x,y,z) -> (x*Ly + y)*Lz + z; Kawamoto-Smit staggered signs; h_ij = -eta_ij."""
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
    return dict(L=L, periodic=periodic, twist=twist, V=V, E=len(EDGES), EDGES=EDGES, eta=eta,
                FACES=FACES, h=h, coords=coords, idx=idx, sub=sub, STAR=STAR, EIDX=EIDX,
                NBR=NBR, name="%dx%dx%d" % L)


# ==========================================================================
# the superfast encoding and the record space   (T3/t3_core.py)
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
        n = len(cyc)
        for a in range(n):
            out = out * self.A(cyc[a], cyc[(a + 1) % n])
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
    r2 = True
    for i, j in itertools.combinations(range(E.V), 2):
        r2 &= comm(Bv[i], Bv[j])
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


class Space:
    """a record space held on an index set Z with locator loc; H[z^bq, z] = 1j * amp_q(z)."""

    def __init__(self, En, eta, Z, loc, name):
        self.En, self.name = En, name
        self.NQ, self.EDGES, self.V = En.NQ, En.EDGES, En.V
        self.Z, self.loc, self.n = Z, loc, len(Z)
        n, NQ = self.n, self.NQ
        self.BIT = [((Z >> q) & 1).astype(bool) for q in range(NQ)]
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
        self.edge_of = np.zeros(len(H.data), dtype=np.int64)
        flip = (Z[self.rows] ^ Z[self.cols])
        for q in range(NQ):
            self.edge_of[flip == (1 << q)] = q

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

    def H_free(self, recmask):
        """H_R: the hops on the UNRECORDED edges, written by an edge mask."""
        keep = ((recmask >> self.edge_of) & 1) == 0
        return sp.csr_matrix((self.H.data * keep, self.cols, self.H.indptr), shape=(self.n, self.n))

    def set_sea(self, sea):
        self.SEA = sea
        self.P_SEA = np.abs(sea) ** 2


def cheb_evolve(Hl, v, tau, lam):
    """exp(-i tau Hl) v by the Jacobi-Anger expansion on [-lam, lam], lam >= ||Hl||."""
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


# ==========================================================================
# many-body objects   (T3/t3_core.py)
def build_cube_mb():
    _, EDG = cube_cluster()
    FAC = cube_faces()
    En = Enc(8, sorted(EDG), FAC)
    AUD = audit(En)
    ok = all(AUD[k] for k in ("R0_welldef", "R0_antisym", "R1", "R2", "R3", "R4", "grp_ok"))
    ETA = []
    for (i, j) in En.EDGES:
        ETA.append(eta_ks(corner_xyz(min(i, j)), {4: 0, 2: 1, 1: 2}[min(i, j) ^ max(i, j)]))
    FLUX = face_flux(FAC, En.EDGES, ETA)
    Z = np.arange(4096, dtype=np.int64)
    S = Space(En, ETA, Z, Z, "cube")
    CID, PHI, REPS = code_space(En, AUD)
    W = np.zeros((4096, 128), dtype=np.complex128)
    W[Z, CID] = PHI / np.sqrt(32.0)
    HC = W.conj().T @ (S.H @ W)
    EV, VC = np.linalg.eigh(HC)
    sea = W @ VC[:, 0]
    S.set_sea(sea)
    S.set_gens(AUD["gens"])
    Hs = S.H @ sea
    E = math.fsum((np.conj(sea) * Hs).real)
    res = float(np.linalg.norm(Hs - E * sea))
    NVAL = np.zeros(4096, dtype=np.int64)
    for v in range(8):
        NVAL += parity(Z & En.STARMASK[v])
    return dict(En=En, S=S, ETA=ETA, FLUX=FLUX, ok=ok, AUD=AUD, E=E, res=res,
                gap=float(EV[1] - EV[0]), NVAL=NVAL, code_dim=AUD["code_dim"])


def mb_schedule_law(S, masks, tau, evolve_null=False):
    """The final record law of a Model-A schedule: at each step the edges in `mask` not yet
    recorded form jointly (Lueders with the Born odds -- the identity on the level vector),
    then exp(-i tau H_R).  Returns |Psi|^2, Psi = U_{k-1}...U_1|sea>.  A step whose mask is
    already fully recorded is a null event: no evolution unless evolve_null."""
    Phi = S.SEA.astype(np.complex128).copy()
    rec = 0
    NQ = S.NQ
    for mask in masks:
        new = mask & ~rec
        rec |= mask
        nrec = pc(rec)
        if new == 0 and not evolve_null:
            continue
        if tau > 0 and nrec < NQ:
            Phi = cheb_evolve(S.H_free(rec), Phi, tau, float(NQ - nrec))
    return np.abs(Phi) ** 2


def slab_T1(Lx=2, Ly=2, Lz=3):
    idx = {}
    for x in range(Lx):
        for y in range(Ly):
            for z in range(Lz):
                idx[(x, y, z)] = (x * Ly + y) * Lz + z
    V = Lx * Ly * Lz
    E = []

    def add(p, q, a):
        i, j = idx[p], idx[q]
        E.append((min(i, j), max(i, j), a, p))

    for (x, y, z) in idx:
        if x + 1 < Lx:
            add((x, y, z), (x + 1, y, z), 0)
        if y + 1 < Ly:
            add((x, y, z), (x, y + 1, z), 1)
        if z + 1 < Lz:
            add((x, y, z), (x, y, z + 1), 2)
    E.sort(key=lambda t: (t[0], t[1]))
    EDGES = [(i, j) for (i, j, a, p) in E]
    ETA = {}
    for (i, j, a, p) in E:
        x, y, z = p
        ETA[(i, j)] = 1 if a == 0 else (-1 if (a == 1 and x & 1) else
                                        (-1 if (a == 2 and (x + y) & 1) else 1))
    FACES = []

    def nxt(c, a):
        v = list(c)
        if v[a] + 1 < (Lx, Ly, Lz)[a]:
            v[a] += 1
            return tuple(v)
        return None

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
                FACES.append(cyc)
    return V, EDGES, sorted(set(FACES)), [ETA[e] for e in EDGES]


def build_slab_mb():
    VS, EDGES_S, FACES_S, ETA_S = slab_T1(2, 2, 3)
    En = Enc(VS, EDGES_S, FACES_S)
    AUD = audit(En)
    ok = all(AUD[k] for k in ("R0_welldef", "R0_antisym", "R1", "R2", "R3", "R4", "grp_ok"))
    FLUX = face_flux(FACES_S, EDGES_S, ETA_S)
    ZS = np.arange(1 << 20, dtype=np.int64)
    NVS = np.zeros(1 << 20, dtype=np.int8)
    for v in range(VS):
        NVS += parity(ZS & En.STARMASK[v])
    J = np.flatnonzero(NVS == 6).astype(np.int64)
    locS = -np.ones(1 << 20, dtype=np.int64)
    locS[J] = np.arange(len(J))
    del ZS, NVS
    S = Space(En, ETA_S, J, locS, "slab")
    S.set_gens(AUD["gens"])
    tt = np.arange(S.n, dtype=np.float64)
    v0 = S.project_code(np.cos(0.7 * tt + 0.3) + 1j * np.cos(1.3 * tt + 1.1))
    v0 /= np.linalg.norm(v0)
    wS, US = spla.eigsh(S.H, k=3, which="SA", v0=v0, tol=0, maxiter=20000)
    sea = S.project_code(US[:, 0])
    sea /= np.linalg.norm(sea)
    sh = float(np.abs(wS).max()) + 6.0
    for it in range(120):
        sea = S.project_code(sh * sea - S.H @ sea)
        sea /= np.linalg.norm(sea)
        if it % 20 == 19:
            Hs = S.H @ sea
            ev = math.fsum((np.conj(sea) * Hs).real) / math.fsum(np.abs(sea) ** 2)
            if np.linalg.norm(Hs - ev * sea) < 1e-13:
                break
    Hs = S.H @ sea
    E = math.fsum((np.conj(sea) * Hs).real) / math.fsum(np.abs(sea) ** 2)
    res = float(np.linalg.norm(Hs - E * sea))
    del Hs, US, v0
    S.set_sea(sea)
    return dict(En=En, S=S, J=J, ok=ok, AUD=AUD, E=E, res=res, FLUX=FLUX,
                code_dim=AUD["code_dim"])


# ==========================================================================
# the one-particle layer   (T3/t3_core.py)
def sea_W(h, N=None):
    V = h.shape[0]
    N = V // 2 if N is None else N
    w, U = np.linalg.eigh(h)
    return U[:, :N], float(w[N] - w[N - 1]), float(w[:N].sum()), w


def det_law(K):
    V = K.shape[0]
    out = np.zeros(1 << V)
    I = np.eye(V, dtype=K.dtype)
    for n in range(1 << V):
        bits = (n >> np.arange(V)) & 1
        M = np.where(bits[:, None] == 1, K, I - K)
        out[n] = np.linalg.det(M).real
    return out


def corner_index_of_edges(C):
    NQ = C["E"]
    Z = np.arange(1 << NQ, dtype=np.int64)
    out = np.zeros(1 << NQ, dtype=np.int64)
    for v in range(C["V"]):
        m = 0
        for q in C["STAR"][v]:
            m |= 1 << q
        out |= parity(Z & m).astype(np.int64) << v
    return out


def gauge_dim(C):
    """g = |E| - rank_F2(A); the record law is P(w) = 2^-g p(A w)."""
    rows = []
    for v in range(C["V"]):
        m = 0
        for q in C["STAR"][v]:
            m |= 1 << q
        rows.append(m)
    basis = []
    for r in rows:
        for b in basis:
            r = min(r, r ^ b)
        if r:
            basis.append(r)
            basis.sort(reverse=True)
    return C["E"] - len(basis)


def edge_mask(C, edges):
    m = 0
    for q in edges:
        m |= 1 << q
    return m


def h_free(C, recmask, h=None):
    h = C["h"] if h is None else h
    hR = h.copy()
    for q, (i, j) in enumerate(C["EDGES"]):
        if (recmask >> q) & 1:
            hR[i, j] = hR[j, i] = 0.0
    return hR


def schedule_G(C, masks, tau, evolve_null=False, return_steps=False):
    """G = prod_i exp(-i tau h_{R_i}), later steps on the left; null events skip the evolution."""
    V = C["V"]
    NQ = C["E"]
    G = np.eye(V, dtype=np.complex128)
    rec = 0
    steps = []
    for mask in masks:
        new = mask & ~rec
        rec |= mask
        steps.append((pc(new), pc(rec)))
        if new == 0 and not evolve_null:
            continue
        if tau > 0 and pc(rec) < NQ:
            G = sla.expm(-1j * tau * h_free(C, rec)) @ G
    return (G, steps) if return_steps else G


def star_masks(C, order):
    return [edge_mask(C, C["STAR"][v]) for v in order]


def edge_masks(order):
    return [1 << q for q in order]


def kernel(G, W):
    GW = G @ W
    return GW @ GW.conj().T


# ==========================================================================
# A1 -- Theorem 1 on the cube: the structural identity, many-body against one-particle
#      (T3/t3_validate.py V1-V5)
tA = time.time()
MB = build_cube_mb()
S, En, NVAL = MB["S"], MB["En"], MB["NVAL"]
C = cluster(2, 2, 2)
assert C["EDGES"] == En.EDGES and [int(e) for e in C["eta"]] == MB["ETA"]
W8, gap1, E1p, w1 = sea_W(C["h"])
Pk = W8 @ W8.T
Aw = corner_index_of_edges(C)
g8 = gauge_dim(C)
p_sea_full = det_law(Pk)
law_sea_1p = (2.0 ** -g8) * p_sea_full[Aw]

IDENT12 = list(range(12))
EDGE_ORDERS = [IDENT12[s:] + IDENT12[:s] for s in range(12)]
REV12 = IDENT12[::-1]
EDGE_ORDERS += [REV12[s:] + REV12[:s] for s in range(12)]
tvs_mb, tvs_1p, gaps = [], [], []
acc_mb = np.zeros(4096)
acc_1p = np.zeros(4096)
for o in EDGE_ORDERS:
    law_mb = mb_schedule_law(S, edge_masks(o), 0.5)
    K = kernel(schedule_G(C, edge_masks(o), 0.5), W8)
    law_1p = (2.0 ** -g8) * det_law(K)[Aw]
    tvs_mb.append(tv(law_mb, S.P_SEA))
    tvs_1p.append(tv(law_1p, S.P_SEA))
    gaps.append(float(np.max(np.abs(law_mb - law_1p))))
    acc_mb += law_mb / 24
    acc_1p += law_1p / 24

CORD = {"identity": list(range(8)), "reverse": list(range(8))[::-1],
        "even-first": [0, 3, 5, 6, 1, 2, 4, 7], "antipodal": [0, 7, 1, 6, 2, 5, 3, 4],
        "closed-star-first": [1, 2, 4, 0, 3, 5, 6, 7]}
star_gap = 0.0
star_tv = {}
for name, o in CORD.items():
    for evn in (False, True):
        law_mb = mb_schedule_law(S, star_masks(C, o), 0.5, evolve_null=evn)
        K = kernel(schedule_G(C, star_masks(C, o), 0.5, evolve_null=evn), W8)
        law_1p = (2.0 ** -g8) * det_law(K)[Aw]
        star_gap = max(star_gap, float(np.max(np.abs(law_mb - law_1p))))
        star_tv[(name, evn)] = (tv(law_mb, S.P_SEA), tv(law_1p, S.P_SEA))
Kid = kernel(schedule_G(C, star_masks(C, list(range(8))), 0.5), W8)
p_mb = np.zeros(256)
np.add.at(p_mb, Aw, mb_schedule_law(S, star_masks(C, list(range(8))), 0.5))
p_det = det_law(Kid)
proj = float(np.max(np.abs(Kid @ Kid - Kid)))
trK = float(np.trace(Kid).real)
diagK = float(np.max(np.abs(np.diag(Kid).real - 0.5)))
detgap = float(np.max(np.abs(p_mb - p_det)))
fibre = float(np.max(np.abs(mb_schedule_law(S, star_masks(C, list(range(8))), 0.5)
                           - (2.0 ** -g8) * p_det[Aw])))
sea_gap = float(np.max(np.abs(law_sea_1p - S.P_SEA)))
check("A1 [exact; numerical, 1e-15] T1 STRUCTURAL IDENTITY, cube 2x2x2 on its whole 2^12 record "
      "space: R0-R4 %s, code %d, flux %s, g=%d; sea E=-6.928203230276=-4sqrt3, resid %.0e, gap "
      "%.4f, support 1984, 1856 charge + 256 cancellation zeros; one-particle law vs |sea|^2 "
      "%.2e. Every Model-A schedule's law IS 2^-g det-law(G P G^+)(Aw): T1's A4 24 edge orders "
      "at tau=0.5 reproduce to nine digits (identity %.9f, reverse %.9f, min/max/mean %.9f/%.9f/"
      "%.9f, average law %.9f -- T1: 0.324925161, 0.289380397, 0.289380397/0.456208220/"
      "0.379401338, 0.239288631) with max|law_mb-law_1p| %.2e over 24x4096 patterns; five star-"
      "tick orders under BOTH null conventions %.1e; K^2=K %.1e, tr K %.12f, max|K_vv-1/2| %.1e, "
      "corner law vs det(K) %.2e, fibre uniformity %.1e. [%.0fs]"
      % (MB["ok"], MB["code_dim"], sorted(set(MB["FLUX"])), g8, MB["res"], MB["gap"], sea_gap,
         tvs_1p[0], tvs_1p[12], min(tvs_1p), max(tvs_1p), float(np.mean(tvs_1p)),
         tv(acc_1p, S.P_SEA), max(gaps), star_gap, proj, trK, diagK, detgap, fibre,
         time.time() - tA),
      MB["ok"] and MB["code_dim"] == 128 and set(MB["FLUX"]) == {-1} and g8 == 5
      and sea_gap < 1e-16 and max(gaps) < 1.1e-17 and star_gap < 1e-17
      and abs(tvs_1p[0] - 0.324925161) < 5e-10 and abs(tvs_mb[0] - tvs_1p[0]) < 1e-12
      and abs(tvs_1p[12] - 0.289380397) < 5e-10 and abs(min(tvs_1p) - 0.289380397) < 5e-10
      and abs(max(tvs_1p) - 0.456208220) < 5e-10
      and abs(float(np.mean(tvs_1p)) - 0.379401338) < 5e-10
      and abs(tv(acc_1p, S.P_SEA) - 0.239288631) < 5e-10
      and abs(tv(acc_mb, S.P_SEA) - tv(acc_1p, S.P_SEA)) < 1e-12
      and proj < 1e-15 and abs(trK - 4.0) < 1e-12 and diagK < 1e-15 and detgap < 1e-15
      and fibre < 1e-17)

# ==========================================================================
# the cube's one-particle machinery on the 70 half-filled corner patterns  (T3/t3_task1_cube.py)
NV8 = np.array([bin(n).count("1") for n in range(256)])
PATS4 = np.flatnonzero(NV8 == 4)
BITS4 = ((PATS4[:, None] >> np.arange(8)[None, :]) & 1).astype(bool)
I8 = np.eye(8)
p_sea4 = p_sea_full[PATS4]
zero4 = np.flatnonzero(p_sea4 < 1e-13)
closed_star_of = {}
for v in range(8):
    pat = sum(1 << u for u in ({v} | C["NBR"][v]))
    closed_star_of[int(np.flatnonzero(PATS4 == pat)[0])] = v


def corner_law4(K):
    M = np.where(BITS4[:, :, None], K[None, :, :], (I8 - K)[None, :, :])
    return np.linalg.det(M).real


def corner_tv4(p4):
    return 0.5 * float(np.abs(p4 - p_sea4).sum())


def census4(p4):
    nz = (p4 * 2.0 ** -g8) > 1e-14
    return dict(support=32 * int(nz.sum()),
                canc=32 * int(np.sum(~nz[zero4])), tv=corner_tv4(p4))


def star_G(order, tau, evolve_null=False):
    return schedule_G(C, star_masks(C, order), tau, evolve_null=evolve_null)


DECL8 = {"identity": list(range(8))}
for s in range(1, 8):
    DECL8["shift%d" % s] = list(range(8))[s:] + list(range(8))[:s]
DECL8["reverse"] = list(range(8))[::-1]
for s in range(1, 8):
    DECL8["rshift%d" % s] = list(range(8))[::-1][s:] + list(range(8))[::-1][:s]
DECL8["even-first"] = [0, 3, 5, 6, 1, 2, 4, 7]
DECL8["odd-first"] = [1, 2, 4, 7, 0, 3, 5, 6]
DECL8["antipodal"] = [0, 7, 1, 6, 2, 5, 3, 4]
DECL8["closed-star-first"] = [1, 2, 4, 0, 3, 5, 6, 7]

# ==========================================================================
# B1 -- Theorem 2 on the cube, COMPLETE over all 8! = 40320 corner orders
tB = time.time()
ALL8 = list(itertools.permutations(range(8)))
NORD = len(ALL8)
res = {}
for tau in (0.1, 0.5, 2.0):
    tvs = np.zeros(NORD)
    supp = np.zeros(NORD, dtype=np.int64)
    canc = np.zeros(NORD, dtype=np.int64)
    acc = np.zeros(70)
    nz8 = np.zeros(9, dtype=np.int64)
    Es = np.zeros(NORD)
    for oi, o in enumerate(ALL8):
        K = kernel(star_G(o, tau), W8)
        p4 = corner_law4(K)
        c = census4(p4)
        tvs[oi], supp[oi], canc[oi] = c["tv"], c["support"], c["canc"]
        acc += p4
        nz8[int(np.sum(p4[zero4] < 1e-13))] += 1
        if tau == 0.5:
            Es[oi] = float(np.trace(C["h"] @ K).real)
    acc /= NORD
    res[tau] = dict(tvs=tvs, avg=acc, hist=nz8, cen=census4(acc), supp=supp, E=Es)

tv5 = res[0.5]["tvs"]
EVENS = {0, 3, 5, 6}
kinds = [0, 0, 0]
for i in np.flatnonzero(tv5 < 1e-12):
    o = ALL8[i]
    kinds[0 if set(o[:4]) == EVENS else (1 if set(o[:4]) == {1, 2, 4, 7} else 2)] += 1


def cube_syms():
    out = []
    for perm in itertools.permutations(range(3)):
        for flips in itertools.product((0, 1), repeat=3):
            m = {}
            for s in range(8):
                x = corner_xyz(s)
                y = [x[perm[a]] ^ flips[a] for a in range(3)]
                m[s] = (y[0] << 2) | (y[1] << 1) | y[2]
            out.append(m)
    return out


idx_of = {o: i for i, o in enumerate(ALL8)}
symdev = 0.0
for o in [tuple(v) for v in DECL8.values()]:
    for m in cube_syms():
        symdev = max(symdev, abs(tv5[idx_of[o]] - tv5[idx_of[tuple(m[v] for v in o)]]))
nex = int(np.sum(tv5 < 1e-12))
check("B1 [numerical, 1e-12] T2 the star tick on the cube, COMPLETE over all 8! = 40320 corner "
      "orders at tau = 0.1/0.5/2.0. TV to the sea min 0/0/0, max %.9f/%.9f/%.9f, mean %.6f/%.6f/"
      "%.6f; EXACT orders %d at every tau -- %d even-first, %d odd-first, %d others (every "
      "prefix closure an eigen-set); support values %s; a fixed order keeps 8, 4, 2 or 0 of the "
      "eight closed-star zeros, histogram over j=0..8 %s; the UNIFORM-ORDER AVERAGE sits at TV "
      "%.9f/%.9f/%.9f with support %d and %d of 256 cancellation zeros kept at every tau. TV is "
      "invariant under the 48 cube symmetries to %.1e. [%.0fs]"
      % (res[0.1]["tvs"].max(), res[0.5]["tvs"].max(), res[2.0]["tvs"].max(),
         res[0.1]["tvs"].mean(), res[0.5]["tvs"].mean(), res[2.0]["tvs"].mean(),
         nex, kinds[0], kinds[1], kinds[2], sorted(set(res[0.5]["supp"].tolist())),
         res[0.5]["hist"].tolist(), res[0.1]["cen"]["tv"], res[0.5]["cen"]["tv"],
         res[2.0]["cen"]["tv"], res[0.5]["cen"]["support"], res[0.5]["cen"]["canc"],
         symdev, time.time() - tB),
      nex == 1440 and all(int(np.sum(res[t]["tvs"] < 1e-12)) == 1440 for t in (0.1, 2.0))
      and kinds == [576, 576, 288]
      and abs(res[0.5]["tvs"].max() - 0.342363972) < 5e-9
      and abs(res[0.1]["cen"]["tv"] - 0.009854703) < 5e-9
      and abs(res[0.5]["cen"]["tv"] - 0.145430031) < 5e-9
      and abs(res[2.0]["cen"]["tv"] - 0.237998278) < 5e-9
      and res[0.5]["cen"]["support"] == 2240 and res[0.5]["cen"]["canc"] == 0
      and res[0.5]["hist"].tolist() == [25536, 0, 9792, 0, 2976, 0, 0, 0, 2016]
      and sorted(set(res[0.5]["supp"].tolist())) == [1984, 2112, 2176, 2240]
      and symdev < 1e-15)

# ==========================================================================
# B2 -- the tau dependence and the null-event convention on the cube
tB2 = time.time()
small = [1e-3, 3e-3, 1e-2, 3e-2, 0.1, 0.3]
tv_id, tv_an = [], []
for t in small:
    tv_id.append(corner_tv4(corner_law4(kernel(star_G(DECL8["identity"], t), W8))))
    tv_an.append(corner_tv4(corner_law4(kernel(star_G(DECL8["antipodal"], t), W8))))
exp_id = [math.log(tv_id[i + 1] / tv_id[i]) / math.log(small[i + 1] / small[i]) for i in range(3)]
exp_an = [math.log(tv_an[i + 1] / tv_an[i]) / math.log(small[i + 1] / small[i]) for i in range(3)]
supp_small = census4(corner_law4(kernel(star_G(DECL8["antipodal"], 1e-3), W8)))["support"]
avg_small = []
for t in (0.01, 0.03):
    acc = np.zeros(70)
    for o in ALL8:
        acc += corner_law4(kernel(star_G(o, t), W8))
    avg_small.append(corner_tv4(acc / NORD))
exp_avg = math.log(avg_small[1] / avg_small[0]) / math.log(3.0)
grid = 0.5 + 0.25 * np.arange(400)
acc_id = np.zeros(70)
acc_an = np.zeros(70)
gid, gan = [], []
for t in grid:
    p_i = corner_law4(kernel(star_G(DECL8["identity"], t), W8))
    p_a = corner_law4(kernel(star_G(DECL8["antipodal"], t), W8))
    acc_id += p_i
    acc_an += p_a
    gid.append(corner_tv4(p_i))
    gan.append(corner_tv4(p_a))
gid = np.array(gid)
acc_id /= len(grid)
acc_an /= len(grid)
tvs_alt = np.zeros(NORD)
acc_alt = np.zeros(70)
nnull = 0
for oi, o in enumerate(ALL8):
    p4 = corner_law4(kernel(star_G(o, 0.5, evolve_null=True), W8))
    tvs_alt[oi] = corner_tv4(p4)
    acc_alt += p4
    rec = 0
    for v in o:
        m = edge_mask(C, C["STAR"][v])
        if (m & ~rec) == 0 and pc(rec) < 12:
            nnull += 1
            break
        rec |= m
acc_alt /= NORD
dnull = float(np.max(np.abs(tvs_alt - tv5)))
check("B2 [numerical, 1e-12] T2's tau dependence and the declared null-event convention, cube. "
      "tau -> 0: TV = c tau^2 -- the identity order runs %.3e -> %.3e over tau = 1e-3 -> 3e-2 "
      "with local exponents %s, the antipodal order %.3e -> %.3e with %s, and the uniform-order "
      "average over all 40320 orders %.4e at 0.01 and %.4e at 0.03 (exponent %.2f); the support "
      "is already %d at tau = 1e-3, so the cancellation zeros go at any tau > 0 and only their "
      "weight is small. tau -> infinity: NO limit -- over the declared grid tau = 0.5 + 0.25j, "
      "j < 400, the identity order's TV ranges %.4f - %.4f (mean %.4f, last-100 spread %.4f), "
      "quasi-periodic; its tau-averaged (Cesaro) law sits at TV %.6f, support %d, the antipodal "
      "order's at %.6f. Null-event sensitivity: 'evolve after every tick' moves a single order "
      "by at most %.1e and the uniform average from %.6f to %.6f; a null event before full "
      "coverage occurs in %d of the 40320 orders. [%.0fs]"
      % (tv_id[0], tv_id[3], ["%.2f" % x for x in exp_id], tv_an[0], tv_an[3],
         ["%.2f" % x for x in exp_an], avg_small[0], avg_small[1], exp_avg, supp_small,
         gid.min(), gid.max(), gid.mean(), gid[-100:].max() - gid[-100:].min(),
         corner_tv4(acc_id), census4(acc_id)["support"], corner_tv4(acc_an),
         dnull, res[0.5]["cen"]["tv"], corner_tv4(acc_alt), nnull, time.time() - tB2),
      max(abs(x - 2.0) for x in exp_id) < 0.01 and max(abs(x - 2.0) for x in exp_an) < 0.01
      and abs(exp_avg - 2.0) < 0.01 and supp_small == 2240
      and abs(avg_small[0] - 1.0077e-4) < 1e-8 and abs(avg_small[1] - 9.0531e-4) < 1e-8
      and gid[-100:].max() - gid[-100:].min() > 0.3 and abs(gid.mean() - 0.2246) < 5e-4
      and abs(corner_tv4(acc_id) - 0.199223) < 5e-6
      and abs(corner_tv4(acc_an) - 0.214374) < 5e-6
      and abs(dnull - 0.13) < 0.01 and abs(corner_tv4(acc_alt) - 0.154022) < 5e-6
      and nnull == 10368)

# ==========================================================================
# B3 -- Theorem 3, the 2x2x3 slab: 28 declared orders, no exact one, many-body on |J| = 473088
tB3 = time.time()
CS = cluster(2, 2, 3)
VS, NQS = CS["V"], CS["E"]
WS, gapS, EseaS, wS = sea_W(CS["h"])
gS = gauge_dim(CS)
NV12 = np.array([bin(n).count("1") for n in range(1 << VS)])
PATS6 = np.flatnonzero(NV12 == 6)
BITS6 = ((PATS6[:, None] >> np.arange(VS)[None, :]) & 1).astype(bool)
I12 = np.eye(VS)


def corner_law6(K):
    M = np.where(BITS6[:, :, None], K[None, :, :], (I12 - K)[None, :, :])
    return np.linalg.det(M).real


p_sea6 = corner_law6(WS @ WS.T)
sea_zero6 = np.flatnonzero(p_sea6 * 2.0 ** -gS < 1e-14)


def corner_tv6(p6):
    return 0.5 * float(np.abs(p6 - p_sea6).sum())


def census6(p6):
    nz = (p6 * 2.0 ** -gS) > 1e-14
    return dict(support=512 * int(nz.sum()), canc=512 * int(np.sum(~nz[sea_zero6])),
                tv=corner_tv6(p6))


ID12 = list(range(12))
DECL12 = {"identity": ID12}
for s in range(1, 12):
    DECL12["shift%d" % s] = ID12[s:] + ID12[:s]
DECL12["reverse"] = ID12[::-1]
for s in range(1, 12):
    DECL12["rshift%d" % s] = ID12[::-1][s:] + ID12[::-1][:s]
EVEN12 = [v for v in range(12) if CS["sub"][v] == 0]
ODD12 = [v for v in range(12) if CS["sub"][v] == 1]
DECL12["even-first"] = EVEN12 + ODD12
DECL12["odd-first"] = ODD12 + EVEN12
DECL12["deg4-first"] = [4, 7, 0, 2, 9, 11] + ODD12
DECL12["classes-in-order"] = [4, 7, 0, 2, 9, 11, 1, 10, 3, 5, 6, 8]
slab_tv = {}
slab_row = {}
for tau in (0.1, 0.5, 2.0):
    acc = np.zeros(len(PATS6))
    rows = []
    for name, o in DECL12.items():
        p6 = corner_law6(kernel(schedule_G(CS, star_masks(CS, o), tau), WS))
        slab_tv[(name, tau)] = p6
        acc += p6
        rows.append((name, census6(p6)["tv"], census6(p6)["support"], census6(p6)["canc"]))
    slab_row[tau] = (rows, census6(acc / len(DECL12)))


def prefix_residual(order):
    """the one-particle eigen-set criterion (T2 Theorem 1) of each prefix closure, on the SEA."""
    out = []
    rec = 0
    for v in order:
        rec |= edge_mask(CS, CS["STAR"][v])
        Sp = [u for u in range(VS) if all((rec >> q) & 1 for q in CS["STAR"][u])]
        if len(Sp) == VS:
            break
        Sc = [u for u in range(VS) if u not in Sp]
        hR = CS["h"][np.ix_(Sc, Sc)]
        worst = 0.0
        for n in itertools.product((0, 1), repeat=len(Sp)):
            S1 = [Sp[a] for a in range(len(Sp)) if n[a]]
            Zn = (np.eye(WS.shape[1]) if not S1
                  else np.linalg.svd(WS[S1, :], full_matrices=True)[2][len(S1):].T)
            U0 = (WS @ Zn)[Sc, :]
            u, s, vt = np.linalg.svd(U0, full_matrices=False)
            r = int(np.sum(s > 1e-10))
            if r != WS.shape[1] - len(S1):
                continue
            U = u[:, :r]
            hU = hR @ U
            worst = max(worst, float(np.linalg.norm(hU - U @ (U.conj().T @ hU))))
        out.append((v, len(Sp), worst))
    return out


pr_id = prefix_residual(DECL12["identity"])
pr_d4 = prefix_residual(DECL12["deg4-first"])
b2 = {}
for tau in (0.5, 2.0):
    b2[tau] = [corner_tv6(corner_law6(kernel(schedule_G(CS, edge_masks(list(range(k))), tau), WS)))
               for k in (1, 6)]
MBS = build_slab_mb()
SS, EnS = MBS["S"], MBS["En"]
assert EnS.EDGES == CS["EDGES"]
Aw_J = np.zeros(SS.n, dtype=np.int64)
for v in range(VS):
    Aw_J |= parity(SS.Z & edge_mask(CS, CS["STAR"][v])).astype(np.int64) << v
pos6 = -np.ones(1 << VS, dtype=np.int64)
pos6[PATS6] = np.arange(len(PATS6))
sea_gapS = float(np.max(np.abs((2.0 ** -gS) * p_sea6[pos6[Aw_J]] - SS.P_SEA)))
mbgap = 0.0
mbtv = {}
for name in ("identity", "deg4-first", "even-first", "reverse"):
    law_mb = mb_schedule_law(SS, star_masks(CS, DECL12[name]), 0.5)
    law_1p = (2.0 ** -gS) * slab_tv[(name, 0.5)][pos6[Aw_J]]
    mbgap = max(mbgap, float(np.max(np.abs(law_mb - law_1p))))
    mbtv[name] = (tv(law_mb, SS.P_SEA), corner_tv6(slab_tv[(name, 0.5)]))
law_mb = mb_schedule_law(SS, edge_masks(list(range(6))), 0.5)
law_1p = (2.0 ** -gS) * corner_law6(kernel(schedule_G(CS, edge_masks(list(range(6))), 0.5), WS))[pos6[Aw_J]]
ruleC = (tv(law_mb, SS.P_SEA), float(np.max(np.abs(law_mb - law_1p))))
r5, c5 = slab_row[0.5]
tvs5 = [r[1] for r in r5]
check("B3 [exact; numerical, 1e-12] T3 the star tick on the 2x2x3 slab (12 corners, 20 edges, "
      "g=%d), 28 DECLARED corner orders, one-particle exact and many-body certified on the 2^20 "
      "record space held on |J| = %d: R0-R4 %s, code %d, flux %s, sea E=%.12f=-(8+2sqrt2), resid "
      "%.0e, support 411648, one-particle law vs |sea|^2 %.1e. NO star-tick order is exact at any "
      "declared tau (%d of 28 at each): the only single-corner eigen-sets are the degree-4 "
      "corners, and the third event is a degree-3 corner whose prefix closure fails -- identity "
      "residuals %s, deg4-first %s. At tau=0.5 the 28 orders span TV %.6f (even-first, odd-first, "
      "deg4-first, classes-in-order: support 411648, all 61440 cancellation zeros kept) to %.6f "
      "(rshift3), declared-family average %.6f with support %d and %d of 61440 zeros kept; at "
      "tau=0.1 %.6f-%.6f, average %.6f; at tau=2.0 %.6f-%.6f, average %.6f. Many-body vs "
      "one-particle on J for four star orders %.1e (TV %.9f identity, %.9f even-first, both "
      "routes) and for T1's rule-C six-record law %.1e; T1's B2 figures reproduce: %.4f/%.4f at "
      "tau=0.5 and %.4f/%.4f at tau=2.0 (T1: 0.1148/0.3156, 0.0268/0.347). [%.0fs]"
      % (gS, SS.n, MBS["ok"], MBS["code_dim"], sorted(set(MBS["FLUX"])), MBS["E"], MBS["res"],
         sea_gapS, sum(1 for t in tvs5 if t < 1e-12), ["%.4f" % t[2] for t in pr_id[:3]],
         ["%.4f" % t[2] for t in pr_d4[:4]], min(tvs5), max(tvs5), c5["tv"], c5["support"],
         c5["canc"], min(r[1] for r in slab_row[0.1][0]), max(r[1] for r in slab_row[0.1][0]),
         slab_row[0.1][1]["tv"], min(r[1] for r in slab_row[2.0][0]),
         max(r[1] for r in slab_row[2.0][0]), slab_row[2.0][1]["tv"], mbgap,
         mbtv["identity"][0], mbtv["even-first"][0], ruleC[1], b2[0.5][0], b2[0.5][1],
         b2[2.0][0], b2[2.0][1], time.time() - tB3),
      MBS["ok"] and MBS["code_dim"] == 2048 and set(MBS["FLUX"]) == {-1} and gS == 9
      and SS.n == 473088 and abs(MBS["E"] + 8 + 2 * math.sqrt(2)) < 1e-12 and sea_gapS < 1e-16
      and all(sum(1 for r in slab_row[t][0] if r[1] < 1e-12) == 0 for t in (0.1, 0.5, 2.0))
      and abs(pr_id[0][2] - 0.2071) < 5e-4 and abs(pr_d4[2][2] - 0.2071) < 5e-4
      and abs(min(tvs5) - 0.032625) < 5e-6 and abs(max(tvs5) - 0.486099) < 5e-6
      and abs(c5["tv"] - 0.345484) < 5e-6 and c5["support"] == 473088 and c5["canc"] == 0
      and abs(slab_row[0.1][1]["tv"] - 0.081326) < 5e-6
      and abs(slab_row[2.0][1]["tv"] - 0.408083) < 5e-6
      and mbgap < 4e-18 and abs(mbtv["identity"][0] - 0.468995964) < 5e-9
      and abs(mbtv["identity"][0] - mbtv["identity"][1]) < 1e-12
      and abs(mbtv["even-first"][0] - 0.032625043) < 5e-9 and ruleC[1] < 4e-18
      and abs(b2[0.5][0] - 0.1148) < 5e-5 and abs(b2[0.5][1] - 0.3156) < 5e-5
      and abs(b2[2.0][0] - 0.0268) < 5e-5 and abs(b2[2.0][1] - 0.3472) < 5e-5)

# ==========================================================================
# C1 -- Theorem 4, the Born odds per fixed order (T3/t3_task3_born.py), cube many-body
tC = time.time()


def branch_process(order, tau):
    """walk the star tick as a tree of unnormalised branch states, recording every event's
    Born odds; a branch below PMIN is dropped."""
    Phi = S.SEA.astype(np.complex128).copy()
    rec = 0
    events = []
    nodes = {0: Phi}
    for step, v in enumerate(order):
        mask = En.STARMASK[v]
        new = mask & ~rec
        if new == 0:
            continue
        qs = [q for q in range(12) if (new >> q) & 1]
        newnodes = {}
        for w0, psi in nodes.items():
            p0 = float(np.sum(np.abs(psi) ** 2))
            if p0 < PMIN:
                continue
            odds = {}
            for bits in itertools.product((0, 1), repeat=len(qs)):
                m = np.ones(4096, dtype=bool)
                wv = w0
                for q, b in zip(qs, bits):
                    m &= (S.BIT[q] if b else ~S.BIT[q])
                    wv |= (b << q)
                ps = np.where(m, psi, 0)
                pw = float(np.sum(np.abs(ps) ** 2))
                odds[bits] = pw / p0
                if pw / p0 >= PMIN:
                    newnodes[wv] = ps
            events.append((v, rec, w0, qs, odds))
        rec |= new
        nrec = pc(rec)
        if tau > 0 and nrec < 12:
            Hl = S.H_free(rec)
            for wv in newnodes:
                newnodes[wv] = cheb_evolve(Hl, newnodes[wv], tau, float(12 - nrec))
        nodes = newnodes
    return events


BORN = {"identity": list(range(8)), "antipodal": [0, 7, 1, 6, 2, 5, 3, 4],
        "even-first": [0, 3, 5, 6, 1, 2, 4, 7], "closed-star-first": [1, 2, 4, 0, 3, 5, 6, 7]}
born = {}
for name, order in BORN.items():
    events = branch_process(order, 0.5)
    law = mb_schedule_law(S, star_masks(C, order), 0.5)
    worst = 0.0
    menus, sizes = set(), []
    for (v, rec0, w0, qs, odds) in events:
        m0 = np.ones(4096, dtype=bool)
        for q in range(12):
            if (rec0 >> q) & 1:
                m0 &= (S.BIT[q] if (w0 >> q) & 1 else ~S.BIT[q])
        p0 = float(law[m0].sum())
        vec = []
        for bits, pr in odds.items():
            m = m0.copy()
            for q, b in zip(qs, bits):
                m &= (S.BIT[q] if b else ~S.BIT[q])
            worst = max(worst, abs(pr - float(law[m].sum()) / p0))
            vec.append(pr)
        vec = np.array(vec)
        supp = tuple(int(x) for x in np.flatnonzero(vec > 1e-13))
        menus.add((len(qs), supp))
        sizes.append(len(supp))
    lines = []
    incon = 0
    for size in sorted(set(s for s, _ in menus)):
        M = [supp for s, supp in menus if s == size]
        A = np.zeros((len(M), 1 << size))
        for r, supp in enumerate(M):
            A[r, list(supp)] = 1.0
        rA = np.linalg.matrix_rank(A, tol=1e-9)
        rAb = np.linalg.matrix_rank(np.hstack([A, np.ones((len(M), 1))]), tol=1e-9)
        if len(M) > 1:
            incon += int(rAb > rA)
        lines.append("%de:%d menus %s rank %d|%d"
                     % (size, len(M), sorted(set(len(s) for s in M)), rA, rAb))
    born[name] = dict(nev=len(events), worst=worst, menus=len(menus),
                      sizes=sorted(set(sizes)), lines=lines, incon=incon)
check("C1 [numerical, 1e-15] T4 the BORN structure per fixed order, cube many-body at tau=0.5, "
      "every branch of the tree walked. At every one of the %d / %d / %d / %d formation events "
      "of the identity, antipodal, even-first and closed-star-first orders the Born odds of the "
      "branch state EQUAL the record-basis diagonal of the ONE conditioned final level vector "
      "Psi = U_{k-1}...U_1|sea> = Slater(G_pi W), to %.1e / %.1e / %.1e / %.1e: B6's one-frame "
      "structure transfers verbatim with the sea replaced by the order's rotated Slater state. "
      "Menus: identity %d of sizes %s (%s), antipodal %d of sizes %s (%s) -- a THREE-outcome "
      "menu on a 2-edge unit, absent on the sea's star -- even-first %d of sizes %s, "
      "closed-star-first %d of sizes %s. The global clause stays REFUTED by the supports "
      "(rank(A|1) = rank(A) + 1) at every unit size with more than one menu, in every order "
      "(%d/%d/%d/%d), while the fibred clause holds as the same identity. [%.0fs]"
      % (born["identity"]["nev"], born["antipodal"]["nev"], born["even-first"]["nev"],
         born["closed-star-first"]["nev"], born["identity"]["worst"], born["antipodal"]["worst"],
         born["even-first"]["worst"], born["closed-star-first"]["worst"],
         born["identity"]["menus"], born["identity"]["sizes"], "; ".join(born["identity"]["lines"]),
         born["antipodal"]["menus"], born["antipodal"]["sizes"],
         "; ".join(born["antipodal"]["lines"]), born["even-first"]["menus"],
         born["even-first"]["sizes"], born["closed-star-first"]["menus"],
         born["closed-star-first"]["sizes"], born["identity"]["incon"],
         born["antipodal"]["incon"], born["even-first"]["incon"],
         born["closed-star-first"]["incon"], time.time() - tC),
      all(born[n]["worst"] < 5e-16 for n in BORN)
      and born["identity"]["nev"] == 2793 and born["antipodal"]["nev"] == 2889
      and born["even-first"]["nev"] == 521 and born["closed-star-first"]["nev"] == 2953
      and born["identity"]["sizes"] == [1, 2, 4, 8]
      and born["antipodal"]["sizes"] == [1, 2, 3, 4, 8]
      and born["even-first"]["sizes"] == [4, 5, 6, 8]
      and born["closed-star-first"]["sizes"] == [1, 2, 6, 8]
      and born["identity"]["menus"] == 7 and born["antipodal"]["menus"] == 9
      and born["even-first"]["menus"] == 37 and born["closed-star-first"]["menus"] == 8
      and min(born[n]["incon"] for n in BORN) >= 1)

# ==========================================================================
# C2 -- the Markov statement and the single-site menus (T3/t3_task3_born.py B2-B3), by exact
#       marginal reduction: one bincount per record subset gives every condition at once
tC2 = time.time()
BITZ = ((np.arange(4096, dtype=np.int64)[:, None] >> np.arange(12)[None, :]) & 1)


def marg(law, T):
    """the exact joint marginal of `law` on the record subset T, as an array whose axis a is
    the value of edge T[a]: one bincount replaces every per-condition boolean mask."""
    m = len(T)
    idx = np.zeros(4096, dtype=np.int64)
    for a, r in enumerate(T):
        idx += BITZ[:, r] << (m - 1 - a)
    return np.bincount(idx, weights=law, minlength=1 << m).reshape([2] * m)


def nn_spread(law):
    worst = 0.0
    for q in range(12):
        i, j = En.EDGES[q]
        nn = [r for r in range(12) if r != q and len(set(En.EDGES[r]) & {i, j}) == 1]
        M = marg(law, [q] + nn)
        p1 = np.take(M, 1, axis=0).ravel()
        p0 = np.take(M, 0, axis=0).ravel()
        p = p0 + p1
        live = p > 1e-13
        worst = max(worst, float(np.max(np.abs(p1[live] / p[live] - 0.5))) if live.any() else 0.0)
    return worst


def site_menus(law, kmax=9):
    menus = set()
    first = None
    for m in range(1, kmax + 2):
        for T in itertools.combinations(range(12), m):
            M = marg(law, T)
            for j in range(m):
                p1 = np.take(M, 1, axis=j).ravel()
                p0 = np.take(M, 0, axis=j).ravel()
                p = p0 + p1
                live = p > 1e-13
                if not live.any():
                    continue
                r1 = p1[live] / p[live]
                codes = np.unique(((r1 > 1e-13).astype(np.int64) << 1)
                                  | ((1 - r1) > 1e-13).astype(np.int64))
                for c in codes:
                    menus.add((bool(c >> 1), bool(c & 1)))
                if first is None and int(codes.min()) != 3:
                    first = m - 1
    return sorted(menus), first


law_id = mb_schedule_law(S, star_masks(C, BORN["identity"]), 0.5)
law_an = mb_schedule_law(S, star_masks(C, BORN["antipodal"]), 0.5)
nn = (nn_spread(S.P_SEA), nn_spread(law_id), nn_spread(law_an))
m0, f0 = site_menus(S.P_SEA)
m1, f1 = site_menus(law_id)
m2, f2 = site_menus(law_an)
check("C2 [numerical, 1e-15] T4's nearest-neighbour and single-site menu statements survive the "
      "disturbance. Records on the four edges sharing a corner with a site never move its odds "
      "off 1/2: max|odds - 1/2| is %.1e on the sea, %.1e on the identity-order law and %.1e on "
      "the antipodal-order law. Over ALL conditions with k <= 9 prior records the single-site "
      "menus are the same three -- {P0,P1}, {P0}, {P1} -- on the sea (%s, first forcing k=%s, "
      "B6: 3 menus at k=8), on the identity-order law (%s, k=%s) and on the antipodal-order law "
      "(%s, k=%s), so the abundance item stays unpaid: every menu is still a subset of the "
      "record frame. [%.0fs]"
      % (nn[0], nn[1], nn[2], len(m0), f0, len(m1), f1, len(m2), f2, time.time() - tC2),
      max(nn) < 5e-16 and m0 == m1 == m2 == [(False, True), (True, False), (True, True)]
      and f0 == 8 and f1 == 8 and f2 == 9)

# ==========================================================================
# D1 -- Theorem 5, the determinantal structure per order and on the mixture
#       (T3/t3_task4_structure.py D1-D5)
tD = time.time()
DSTR = {"identity": DECL8["identity"], "shift1": DECL8["shift1"], "shift2": DECL8["shift2"],
        "shift3": DECL8["shift3"], "antipodal": DECL8["antipodal"],
        "closed-star-first": DECL8["closed-star-first"], "even-first": DECL8["even-first"]}
d1 = {}
for name, o in DSTR.items():
    K = kernel(star_G(o, 0.5), W8)
    p4 = corner_law4(K)
    d1[name] = dict(proj=float(np.max(np.abs(K @ K - K))), tr=float(np.trace(K).real),
                    rank=int(np.linalg.matrix_rank(K, tol=1e-9)),
                    supp=int((p4 > 1e-13).sum()),
                    surv=sorted(closed_star_of[i] for i in zero4 if p4[i] < 1e-13),
                    small=float(p4[p4 > 1e-13].min()), tv=corner_tv4(p4))


def eigen_residual(h, Wx, Sset):
    N = Wx.shape[1]
    Sc = [v for v in range(8) if v not in Sset]
    hR = h[np.ix_(Sc, Sc)]
    worst = 0.0
    for n in itertools.product((0, 1), repeat=len(Sset)):
        S1 = [Sset[a] for a in range(len(Sset)) if n[a]]
        if S1:
            u, s, vt = np.linalg.svd(Wx[S1, :], full_matrices=True)
            Zn = vt[int(np.sum(s > 1e-10)):].conj().T
        else:
            Zn = np.eye(N)
        if Zn.shape[1] != N - len(S1):
            continue
        u, s, vt = np.linalg.svd((Wx @ Zn)[Sc, :], full_matrices=False)
        r = int(np.sum(s > 1e-10))
        if r != N - len(S1):
            continue
        U = u[:, :r]
        hU = hR @ U
        worst = max(worst, float(np.linalg.norm(hU - U @ (U.conj().T @ hU))))
    return worst


SETS = {"corner {0}": [0], "adjacent {0,1}": [0, 1], "antipodal {0,7}": [0, 7],
        "even class {0,3,5,6}": [0, 3, 5, 6], "closed star {0,1,2,4}": [0, 1, 2, 4]}
d3 = {}
for name in ("identity", "antipodal"):
    Wx = star_G(DSTR[name], 0.5) @ W8
    d3[name] = dict(E=float(np.trace(Wx.conj().T @ C["h"] @ Wx).real),
                    res=float(np.linalg.norm(C["h"] @ Wx - Wx @ (Wx.conj().T @ C["h"] @ Wx))),
                    sets=[eigen_residual(C["h"], Wx, s) for s in SETS.values()])
    masks2 = [edge_mask(C, C["STAR"][0] + C["STAR"][3]), edge_mask(C, C["STAR"][5] + C["STAR"][6])]
    G2 = schedule_G(C, masks2, 0.5)
    p_before = corner_law4(Wx @ Wx.conj().T)
    p_after = corner_law4((G2 @ Wx) @ (G2 @ Wx).conj().T)
    d3[name]["round2"] = 0.5 * float(np.abs(p_after - p_before).sum())
sea_sets = [eigen_residual(C["h"], W8, s) for s in SETS.values()]
G2 = schedule_G(C, [edge_mask(C, C["STAR"][0] + C["STAR"][3]),
                    edge_mask(C, C["STAR"][5] + C["STAR"][6])], 0.5)
sea_round2 = 0.5 * float(np.abs(corner_law4((G2 @ W8) @ (G2 @ W8).conj().T) - p_sea4).sum())
kry = [int(np.linalg.matrix_rank(np.stack([np.eye(8)[v], C["h"] @ np.eye(8)[v],
                                           C["h"] @ C["h"] @ np.eye(8)[v]], 1), tol=1e-9))
       for v in range(8)]
check("D1 [numerical, 1e-13] T5 the determinantal structure per fixed order, and what the sea's "
      "structure loses. Every fixed order's law is EXACTLY the determinantal law of the rank-4 "
      "projector K = G_pi P G_pi^+: over seven declared orders max|K^2-K| %.1e, tr K = 4 to "
      "%.1e, rank 4, and the ZERO CRITERION survives (zero iff det = 0) while the sea's own "
      "zeros do not -- identity keeps all 8 closed-star zeros at TV %.6f (support 62/70), shift1 "
      "keeps {0,7} and shift3 {3,4} (68/70), shift2 and antipodal none (70/70, TV %.6f / %.6f), "
      "even-first is exact. The disturbed state is NOT an h-eigenstate: <h> = %.6f / %.6f "
      "against the sea's %.6f, eigen-residual %.4f / %.4f (sea 0); T2's eigen-set criterion on "
      "W_pi gives %s and %s against the sea's %s, its zero on the even class being the cube "
      "accident that the class records every edge, and the sea's corner Krylov dimensions are %s "
      "(the two-mode condition). NO unit holds the disturbed law still: a second round -- even "
      "pairs {0,3} then {5,6} with evolution between -- moves it by TV %.6f / %.6f where the "
      "same schedule leaves the sea at %.1e. [%.0fs]"
      % (max(d1[n]["proj"] for n in DSTR), max(abs(d1[n]["tr"] - 4) for n in DSTR),
         d1["identity"]["tv"], d1["shift2"]["tv"], d1["antipodal"]["tv"], d3["identity"]["E"],
         d3["antipodal"]["E"], E1p, d3["identity"]["res"], d3["antipodal"]["res"],
         ["%.4f" % x for x in d3["identity"]["sets"]],
         ["%.4f" % x for x in d3["antipodal"]["sets"]], ["%.4f" % x for x in sea_sets], kry,
         d3["identity"]["round2"], d3["antipodal"]["round2"], sea_round2, time.time() - tD),
      max(d1[n]["proj"] for n in DSTR) < 1e-14
      and max(abs(d1[n]["tr"] - 4) for n in DSTR) < 1e-12
      and all(d1[n]["rank"] == 4 for n in DSTR)
      and d1["identity"]["surv"] == list(range(8)) and d1["shift1"]["surv"] == [0, 7]
      and d1["shift3"]["surv"] == [3, 4] and d1["shift2"]["surv"] == []
      and d1["antipodal"]["surv"] == [] and d1["even-first"]["surv"] == list(range(8))
      and d1["even-first"]["tv"] < 1e-12 and abs(d1["identity"]["tv"] - 0.246607) < 5e-6
      and abs(d3["identity"]["E"] + 3.878820) < 5e-6
      and abs(d3["antipodal"]["E"] + 4.652201) < 5e-6
      and abs(d3["identity"]["res"] - 2.8140) < 5e-4
      and abs(d3["antipodal"]["res"] - 2.4781) < 5e-4
      and max(sea_sets) < 0.5001 and sea_sets[0] < 1e-12 and kry == [2] * 8
      and abs(d3["identity"]["round2"] - 0.295792) < 5e-6
      and abs(d3["antipodal"]["round2"] - 0.340817) < 5e-6 and sea_round2 < 1e-14)

# ==========================================================================
# D2 -- the order-averaged law: a mixture of determinantal laws, and the best single Slater state
tD2 = time.time()


def mixture_probe(p4, label):
    mg = {}
    for k in (1, 2, 3, 4):
        for T in itertools.combinations(range(8), k):
            mg[T] = float(p4[np.all(BITS4[:, list(T)], axis=1)].sum())
    Kd = np.array([mg[(v,)] for v in range(8)])
    K2 = np.zeros((8, 8))
    for u, v in itertools.combinations(range(8), 2):
        K2[u, v] = K2[v, u] = Kd[u] * Kd[v] - mg[(u, v)]
    worst_ratio = 0.0
    viol = 0
    for u, v, w in itertools.combinations(range(8), 3):
        c = 0.5 * (mg[(u, v, w)] - Kd[u] * Kd[v] * Kd[w] + Kd[u] * K2[v, w]
                   + Kd[v] * K2[u, w] + Kd[w] * K2[u, v])
        b = math.sqrt(max(K2[u, v] * K2[v, w] * K2[u, w], 0.0))
        r = abs(c) / b if b > 1e-14 else 0.0
        worst_ratio = max(worst_ratio, r)
        viol += int(r > 1 + 1e-9)

    def kern(x):
        A = np.zeros((8, 8), dtype=complex)
        k = 0
        for i in range(8):
            A[i, i] = x[k]
            k += 1
        for i in range(8):
            for j in range(i + 1, 8):
                A[i, j] = x[k] + 1j * x[k + 1]
                A[j, i] = x[k] - 1j * x[k + 1]
                k += 2
        return kernel(sla.expm(1j * A), W8)

    def objtv(x):
        return 0.5 * float(np.abs(p4 - corner_law4(kern(x))).sum())

    def objl2(x):
        d = p4 - corner_law4(kern(x))
        return float(d @ d)

    starts = {"sea (G=I)": np.zeros(64)}
    for nm in ("identity", "antipodal", "shift1", "closed-star-first"):
        A0 = -1j * sla.logm(star_G(DECL8[nm], 0.5))
        A0 = 0.5 * (A0 + A0.conj().T)
        x = [A0[i, i].real for i in range(8)]
        for i in range(8):
            for j in range(i + 1, 8):
                x += [A0[i, j].real, A0[i, j].imag]
        starts[nm] = np.array(x)
    best = None
    for nm, x0 in starts.items():
        r = minimize(objl2, x0, method="L-BFGS-B",
                     options=dict(maxiter=3000, maxfun=200000, ftol=1e-15, gtol=1e-12))
        r2 = minimize(objtv, r.x, method="Nelder-Mead",
                      options=dict(maxiter=3000, maxfev=6000, xatol=1e-8, fatol=1e-12))
        val = min(objtv(r.x), r2.fun)
        xb = r2.x if r2.fun <= objtv(r.x) else r.x
        if best is None or val < best[0]:
            best = (val, nm, xb)
    Kb = kern(best[2])
    minors = [max(abs(mg[T] - float(np.linalg.det(Kb[np.ix_(T, T)]).real))
                  for T in itertools.combinations(range(8), k)) for k in (2, 3, 4)]
    return dict(one=float(np.max(np.abs(Kd - 0.5))), tr=float(Kd.sum()),
                frob=float(np.sum(Kd ** 2) + K2.sum()), ratio=worst_ratio, viol=viol,
                fit=best[0], start=best[1], minors=minors, tvsea=corner_tv4(p4), label=label)


acc16 = np.zeros(70)
o16 = ([list(range(8))[s:] + list(range(8))[:s] for s in range(8)]
       + [list(range(8))[::-1][s:] + list(range(8))[::-1][:s] for s in range(8)])
for o in o16:
    acc16 += corner_law4(kernel(star_G(o, 0.5), W8))
mx = [mixture_probe(res[0.5]["avg"], "mixture tau=0.5"),
      mixture_probe(res[2.0]["avg"], "mixture tau=2.0"),
      mixture_probe(corner_law4(kernel(star_G(DECL8["identity"], 0.5), W8)), "control"),
      mixture_probe(acc16 / 16, "16 cyclic/reverse")]
check("D2 [numerical, 1e-13] T5 the PHYSICAL order-averaged law is a mixture of determinantal "
      "laws and no single one. Its 1-point marginals are 1/2 to %.1e, its 2-point-derived "
      "sum|K_uv|^2 is %.6f (= 4 for any rank-4 projector, so the projector test cannot "
      "discriminate) and its 3-point marginals are fixed by the 1- and 2-point ones -- the phase "
      "ratio |Re(K_uv K_vw K_wu)|/(|K_uv||K_vw||K_wu|) is %.4f with %d violations of 56, because "
      "same-sublattice entries of K are imaginary and cross-sublattice real for every law in the "
      "family, mixtures included. The best single Slater state (rank-4 projector, 64-parameter "
      "search over G = expm(iA) from five declared starts, L-BFGS then Nelder-Mead) reaches TV "
      "%.6f at tau=0.5 (from start '%s') and %.6f at tau=2.0, against TV %.6f / %.6f from the "
      "sea, with 2-/3-/4-point minors off the mixture's marginals by %.1e/%.1e/%.1e; the "
      "CONTROL, a single order's law, is fitted to TV %.6f and minors %.1e, and the 16-order "
      "cyclic mixture to %.6f. The fit is an upper bound on the best fit, not a lower-bound "
      "certificate. [%.0fs]"
      % (max(m["one"] for m in mx), mx[0]["frob"], mx[0]["ratio"], mx[0]["viol"], mx[0]["fit"],
         mx[0]["start"], mx[1]["fit"], mx[0]["tvsea"], mx[1]["tvsea"], mx[0]["minors"][0],
         mx[0]["minors"][1], mx[0]["minors"][2], mx[2]["fit"], max(mx[2]["minors"]),
         mx[3]["fit"], time.time() - tD2),
      max(m["one"] for m in mx) < 1e-13 and abs(mx[0]["frob"] - 4.0) < 1e-9
      and max(m["ratio"] for m in mx) < 1e-5 and sum(m["viol"] for m in mx) == 0
      and abs(mx[0]["fit"] - 0.068765) < 5e-6 and abs(mx[1]["fit"] - 0.090499) < 5e-6
      and mx[2]["fit"] < 1e-9 and max(mx[2]["minors"]) < 1e-14
      and abs(mx[3]["fit"] - 0.047305) < 5e-6
      and abs(mx[0]["tvsea"] - 0.145430) < 5e-6 and abs(mx[1]["tvsea"] - 0.237998) < 5e-6)

# ==========================================================================
# the gravity lane's machinery on the tori   (T3/t3_task2_gravity.py)
TW = {4: (1, 1, 1), 6: (0, 0, 0)}
TAU = 0.5
FD = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
POL_PAIRS = [(0, 0), (1, 1), (2, 2), (0, 1), (1, 2), (2, 0)]
STAT_NAMES = ['site'] + ['ax' + s for s in 'xyz'] + ['fd%d' % d for d in range(6)]


def tensor_from_coords(c):
    ht = np.zeros((3, 3))
    for p, (a, b) in enumerate(POL_PAIRS):
        if a == b:
            ht[a, a] = c[p]
        else:
            ht[a, b] = ht[b, a] = c[p] / np.sqrt(2)
    return ht


def coords_from_tensor(ht):
    c = np.zeros(6)
    for p, (a, b) in enumerate(POL_PAIRS):
        c[p] = ht[a, a] if a == b else np.sqrt(2) * ht[a, b]
    return c


def tt_basis(k):
    n = np.asarray(k, float) / np.linalg.norm(k)
    trial = np.array([1.0, 0.0, 0.0]) if abs(n[0]) < 0.9 else np.array([0.0, 1.0, 0.0])
    u1 = trial - n * (trial @ n)
    u1 /= np.linalg.norm(u1)
    u2 = np.cross(n, u1)
    plus = (np.outer(u1, u1) - np.outer(u2, u2)) / np.sqrt(2)
    cross = (np.outer(u1, u2) + np.outer(u2, u1)) / np.sqrt(2)
    return np.stack([coords_from_tensor(plus), coords_from_tensor(cross)], axis=1)


def cubic_group():
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            Rm = np.zeros((3, 3), int)
            for i in range(3):
                Rm[i, perm[i]] = signs[i]
            if int(round(np.linalg.det(Rm))) == 1:
                mats.append(Rm)
    return mats


class Torus:
    def __init__(self, L):
        self.L = L
        self.C = cluster(L, L, L, periodic=(True, True, True), twist=TW[L])
        Ct = self.C
        self.V = Ct["V"]
        self.N = self.V // 2
        self.coords = np.array([Ct["coords"][v] for v in range(self.V)])
        self.h = Ct["h"]
        w, U = np.linalg.eigh(self.h)
        self.Uo = np.ascontiguousarray(U[:, :self.N])
        self.Ue = np.ascontiguousarray(U[:, self.N:])
        self.P = self.Uo @ self.Uo.T
        self.gap = float(w[self.N] - w[self.N - 1])
        self.E = float(w[:self.N].sum())
        self.D = 1.0 / (w[:self.N, None] - w[None, self.N:])
        self.J = [self.idx((self.coords + np.eye(3, dtype=int)[a]) % L) for a in range(3)]
        self.JD = [self.idx((self.coords + np.array(d)) % L) for d in FD]

    def idx(self, wv):
        wv = np.asarray(wv)
        return (wv[:, 0] * self.L + wv[:, 1]) * self.L + wv[:, 2]

    def phase(self, nq):
        return np.exp(2j * np.pi * (self.coords @ np.asarray(nq, float)) / self.L)

    def fourier(self, field, nq):
        return (np.conj(self.phase(nq)) @ field) / self.V

    def dP(self, dh):
        A = self.Uo.T @ dh @ self.Ue
        Y = self.Uo @ (A * self.D) @ self.Ue.T
        return Y + Y.T

    def directions(self, nk):
        """the 12 real symmetric directions: Re and Im of the endpoint-mean bond field for each
        of the six polarisations, applied as the relative dressing dh_ij = h_ij f_b(v)."""
        ph = self.phase(nk)
        out = []
        for p in range(6):
            c = np.zeros(6)
            c[p] = 1.0
            ht = tensor_from_coords(c)
            f = [-ht[b, b] * (ph + ph[self.J[b]]) / 4.0 for b in range(3)]
            for part in (np.real, np.imag):
                dh = np.zeros((self.V, self.V))
                for b in range(3):
                    fb = part(f[b])
                    for v in range(self.V):
                        j = int(self.J[b][v])
                        dh[v, j] += self.h[v, j] * fb[v]
                        dh[j, v] += self.h[j, v] * fb[v]
                out.append(dh)
        return out

    def order(self, Rm, t):
        return [int(i) for i in self.idx((self.coords @ np.asarray(Rm).T + np.array(t)) % self.L)]


def G_dG(T, order, tau, dhs, sea=False):
    """G = prod exp(-i tau h_R) over the star tick in `order`, and its Frechet derivatives along
    dhs by the divided-difference formula, accumulated along the schedule."""
    Ct, V = T.C, T.V
    G = np.eye(V, dtype=np.complex128)
    dG = [np.zeros((V, V), dtype=np.complex128) for _ in dhs]
    if sea:
        return G, dG
    rec = np.zeros(Ct["E"], dtype=bool)
    closed = np.zeros(V, dtype=bool)
    for v in order:
        st = Ct["STAR"][v]
        new = [q for q in st if not rec[q]]
        rec[st] = True
        if not new or rec.all():
            continue
        for u in {v} | Ct["NBR"][v]:
            if all(rec[q] for q in Ct["STAR"][u]):
                closed[u] = True
        act = np.flatnonzero(~closed)
        hR = T.h[np.ix_(act, act)].copy()
        live = [q for q in np.flatnonzero(rec)
                if not closed[Ct["EDGES"][q][0]] and not closed[Ct["EDGES"][q][1]]]
        pos = {int(a): i for i, a in enumerate(act)}
        for q in live:
            i, j = Ct["EDGES"][q]
            hR[pos[i], pos[j]] = hR[pos[j], pos[i]] = 0.0
        w, Q = np.linalg.eigh(hR)
        e = np.exp(-1j * tau * w)
        dw = w[:, None] - w[None, :]
        with np.errstate(divide="ignore", invalid="ignore"):
            Phi = (e[:, None] - e[None, :]) / dw
        same = np.abs(dw) < 1e-10
        Phi[same] = (-1j * tau * e[:, None] * np.ones_like(Phi))[same]
        Gi = (Q * e[None, :]) @ Q.T
        Gact = G[act, :]
        for d, dh in enumerate(dhs):
            E = dh[np.ix_(act, act)].copy()
            for q in live:
                i, j = Ct["EDGES"][q]
                E[pos[i], pos[j]] = E[pos[j], pos[i]] = 0.0
            dGi = Q @ ((Q.T @ E @ Q) * Phi) @ Q.T
            dG[d][act, :] = Gi @ dG[d][act, :] + dGi @ Gact
        G[act, :] = Gi @ Gact
    return G, dG


def stats_and_resp(T, K, dKs):
    st = np.zeros((10, T.V))
    st[0] = np.diag(K).real
    for a in range(3):
        st[1 + a] = -np.abs(K[np.arange(T.V), T.J[a]]) ** 2
    for d in range(6):
        st[4 + d] = -np.abs(K[np.arange(T.V), T.JD[d]]) ** 2
    rs = np.zeros((len(dKs), 10, T.V))
    for m, dK in enumerate(dKs):
        rs[m, 0] = np.diag(dK).real
        for a in range(3):
            i, j = np.arange(T.V), T.J[a]
            rs[m, 1 + a] = -2 * (np.conj(K[i, j]) * dK[i, j]).real
        for d in range(6):
            i, j = np.arange(T.V), T.JD[d]
            rs[m, 4 + d] = -2 * (np.conj(K[i, j]) * dK[i, j]).real
    return st, rs


def numerical_rank(A, rel=1e-9):
    s = np.linalg.svd(A, compute_uv=False)
    return (0, s) if s.size == 0 or s[0] == 0 else (int(np.sum(s > rel * s[0])), s)


def family_stats(T, orders, nk, sea=False):
    dhs = T.directions(nk)
    dPs = [T.dP(dh) for dh in dhs]
    Ssum = np.zeros((10, T.V))
    Rsum = np.zeros((12, 10, T.V))
    per = []
    for o in orders:
        G, dG = G_dG(T, o, TAU, dhs, sea=sea)
        GP = G @ T.P
        K = GP @ G.conj().T
        dKs = [dG[d] @ GP.conj().T + G @ dPs[d] @ G.conj().T + GP @ dG[d].conj().T
               for d in range(12)]
        st, rs = stats_and_resp(T, K, dKs)
        Ssum += st
        Rsum += rs
        per.append((st, rs))
    return Ssum / len(orders), Rsum / len(orders), per


def trans_average(T, S, step):
    """the family's baseline statistic field: the exact average of S over the translations
    (step Z)^3, S^{(t)}(v) = S^{(0)}(v - t), evaluated as a convolution of the base order's own
    field -- no extra orders are run."""
    out = np.zeros_like(S)
    ts = list(itertools.product(range(0, T.L, step), repeat=3))
    for t in ts:
        perm = T.idx((T.coords - np.array(t)) % T.L)
        out += S[:, perm]
    return out / len(ts)


def resp_matrix(T, R, nk, zero_offshift=False):
    L = T.L
    shifts = [tuple((L // 2) * gg[i] for i in range(3)) for gg in itertools.product((0, 1), repeat=3)]
    keys = [(nm, Gs) for Gs in shifts for nm in STAT_NAMES]
    Rm = np.zeros((len(keys), 6), complex)
    for p in range(6):
        resp = R[2 * p] + 1j * R[2 * p + 1]
        col = []
        for Gs in shifts:
            nq = tuple((nk[i] + Gs[i]) % L for i in range(3))
            for si in range(10):
                col.append(T.fourier(resp[si], nq))
        Rm[:, p] = col
    if zero_offshift:
        for i, (nm, Gs) in enumerate(keys):
            if Gs != (0, 0, 0):
                Rm[i, :] = 0.0
    return Rm, keys


def read_row(T, Rm, keys, nk):
    TT = tt_basis(2 * np.pi * np.asarray(nk, float) / T.L)
    r, s = numerical_rank(Rm @ TT)
    site = float(np.max(np.abs(Rm[[i for i, k in enumerate(keys) if k[0] == "site"]])))
    off = float(np.max(np.abs(Rm[[i for i, k in enumerate(keys)
                                  if k[0].startswith("ax") and k[1] != (0, 0, 0)]])))
    shear = float(np.max(np.abs(Rm[:, 3:6])))
    fd = float(np.max(np.abs(Rm[[i for i, k in enumerate(keys) if k[0].startswith("fd")]])))
    return dict(rank=r, sv=s, site=site, off=off, shear=shear, fd=fd)


# ==========================================================================
# E1 -- Theorem 6 on the 4^3 torus: the declared O_h x T family of 3072 orders
tE = time.time()
T4 = Torus(4)
ROT48 = [T4.order(Rm, (0, 0, 0)) for Rm in cubic_group() + [-Rm for Rm in cubic_group()]]
MOM4 = [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 1, 2), (1, 2, 3)]
sea4, mix48, mix24 = {}, {}, {}
S48 = None
for nk in MOM4:
    Ss, Rs, _ = family_stats(T4, [list(range(64))], nk, sea=True)
    sea4[nk] = read_row(T4, *resp_matrix(T4, Rs, nk), nk)
    sea4[nk]["fdstat"] = float(np.max(np.abs(Ss[4:10])))
    Sm, Rm_, per = family_stats(T4, ROT48, nk)
    S48 = trans_average(T4, Sm, 1)
    mix48[nk] = read_row(T4, *resp_matrix(T4, Rm_, nk, zero_offshift=True), nk)
    R24 = sum(p[1] for p in per[:24]) / 24
    mix24[nk] = read_row(T4, *resp_matrix(T4, R24, nk, zero_offshift=True), nk)
# certification of reduction (R1): all 64 translations of the base order, explicitly
TRANS64 = [T4.order(np.eye(3, dtype=int), t) for t in itertools.product(range(4), repeat=3)]
_, Rtr, _ = family_stats(T4, TRANS64, (1, 1, 1))
Rm_tr, keys4 = resp_matrix(T4, Rtr, (1, 1, 1))
_, Rb, _ = family_stats(T4, [list(range(64))], (1, 1, 1))
Rm_b, _ = resp_matrix(T4, Rb, (1, 1, 1))
off_tr = float(np.max(np.abs(Rm_tr[[i for i, k in enumerate(keys4) if k[1] != (0, 0, 0)]])))
g0_tr = float(np.max(np.abs(Rm_tr[[i for i, k in enumerate(keys4) if k[1] == (0, 0, 0)]]
                            - Rm_b[[i for i, k in enumerate(keys4) if k[1] == (0, 0, 0)]])))
site48 = float(np.max(np.abs(S48[0] - 0.5)))
ax48 = S48[1:4].mean(axis=1)
fd48 = float(np.max(np.abs(S48[4:10])))
check("E1 [numerical, 1e-15] T6 gravity, 4^3 torus, ground sector (1,1,1), E_sea %.6f, gap %.6f, "
      "tau=0.5, declared O_h x T family of 3072 orders (48 rotations + the exact 64-translation "
      "average, certified against all 64 run explicitly: G != 0 rows %.1e, G = 0 rows unchanged "
      "%.1e). STATIC HALF, stronger than on the sea: site statistic 1/2 to %.1e, its response "
      "zero at every momentum, polarisation and shift (<= %.1e; sea %.1e) -- the bipartite "
      "grading survives every edge deletion, so the cancellation is exact order by order and the "
      "rate ruler stands. PROPAGATING HALF: TT rank %s at n = (1,0,0)/(1,1,0)/(1,1,1)/(1,1,2)/"
      "(1,2,3) against the sea's %s -- the pattern survives -- but the calibration does not: TT "
      "sv %s against %s, so amplitudes halve (%.6f vs %.6f axis, %.6f vs %.6f body diagonal) and "
      "the sea's endpoint-mean silences at k_a = pi break (second value %.1e / %.1e). Shear "
      "columns exactly %.1e on every law; the face-diagonal statistics, zero on the sea (%.1e), "
      "come alive at %.1e and respond at %.1e. Rotation covariance needs the FULL 48-element "
      "group: body-diagonal s_min/s_max %.4f for O_h, %.4f for the 24 proper rotations. [%.0fs]"
      % (T4.E, T4.gap, off_tr, g0_tr, site48, max(mix48[n]["site"] for n in MOM4),
         max(sea4[n]["site"] for n in MOM4), [mix48[n]["rank"] for n in MOM4],
         [sea4[n]["rank"] for n in MOM4],
         ["%.6f" % mix48[n]["sv"][0] for n in MOM4], ["%.6f" % sea4[n]["sv"][0] for n in MOM4],
         mix48[(1, 0, 0)]["sv"][0], sea4[(1, 0, 0)]["sv"][0],
         mix48[(1, 1, 1)]["sv"][0], sea4[(1, 1, 1)]["sv"][0],
         mix48[(1, 1, 2)]["sv"][1], mix48[(1, 2, 3)]["sv"][1],
         max(mix48[n]["shear"] for n in MOM4), max(sea4[n]["fdstat"] for n in MOM4), fd48,
         max(mix48[n]["fd"] for n in MOM4),
         mix48[(1, 1, 1)]["sv"][1] / mix48[(1, 1, 1)]["sv"][0],
         mix24[(1, 1, 1)]["sv"][1] / mix24[(1, 1, 1)]["sv"][0], time.time() - tE),
      abs(T4.E + 78.383672) < 5e-6 and abs(T4.gap - 4.898979) < 5e-6
      and off_tr < 1e-15 and g0_tr < 1e-14 and site48 < 1e-15
      and max(mix48[n]["site"] for n in MOM4) < 1e-15
      and max(sea4[n]["site"] for n in MOM4) < 1e-17
      and [mix48[n]["rank"] for n in MOM4] == [1, 1, 2, 2, 2]
      and [sea4[n]["rank"] for n in MOM4] == [1, 1, 2, 1, 1]
      and abs(mix48[(1, 0, 0)]["sv"][0] - 0.016586) < 5e-6
      and abs(sea4[(1, 0, 0)]["sv"][0] - 0.034722) < 5e-6
      and abs(sea4[(1, 1, 0)]["sv"][0] - 0.020833) < 5e-6
      and abs(mix48[(1, 1, 1)]["sv"][0] - 0.003867) < 5e-6
      and abs(sea4[(1, 1, 1)]["sv"][0] - 0.008505) < 5e-6
      and abs(sea4[(1, 1, 2)]["sv"][0] - 0.008019) < 5e-6
      and abs(sea4[(1, 2, 3)]["sv"][0] - 0.005952) < 5e-6
      and abs(mix48[(1, 1, 2)]["sv"][0] - 0.004437) < 5e-6
      and abs(mix48[(1, 2, 3)]["sv"][0] - 0.003329) < 5e-6
      and sea4[(1, 1, 2)]["sv"][1] < 1e-15 and sea4[(1, 2, 3)]["sv"][1] < 1e-15
      and 1e-4 < mix48[(1, 1, 2)]["sv"][1] < 1e-3
      and max(mix48[n]["shear"] for n in MOM4) == 0.0
      and max(sea4[n]["fdstat"] for n in MOM4) < 1e-30 and abs(fd48 - 7.1e-3) < 5e-5
      and abs(float(np.max(np.abs(ax48 + 0.015886))) ) < 5e-7
      and abs(mix48[(1, 1, 1)]["sv"][1] / mix48[(1, 1, 1)]["sv"][0] - 1.0) < 1e-4
      and abs(mix24[(1, 1, 1)]["sv"][1] / mix24[(1, 1, 1)]["sv"][0] - 0.9292) < 5e-4)

# ==========================================================================
# E2 -- Theorem 6 on the 6^3 torus: the sea baseline and the declared 27-translation family
tE2 = time.time()
T6 = Torus(6)
MOM6 = [(1, 0, 0), (1, 1, 0), (1, 2, 0), (1, 1, 1), (1, 1, 2), (1, 2, 3)]
BASE6 = list(range(216))
sea6, mix6 = {}, {}
S6 = None
for nk in MOM6:
    Ss, Rs, _ = family_stats(T6, [BASE6], nk, sea=True)
    sea6[nk] = read_row(T6, *resp_matrix(T6, Rs, nk), nk)
    sea6[nk]["fdstat"] = float(np.max(np.abs(Ss[4:10])))
    Sm, Rm_, _ = family_stats(T6, [BASE6], nk)
    S6 = trans_average(T6, Sm, 2)
    mix6[nk] = read_row(T6, *resp_matrix(T6, Rm_, nk), nk)
# certification of reduction (R2): two declared even translations give the same response matrix
Rm_base, _ = resp_matrix(T6, family_stats(T6, [BASE6], (1, 1, 2))[1], (1, 1, 2))
tr_dev = 0.0
for t in ((2, 0, 0), (2, 4, 2)):
    Rm_t, _ = resp_matrix(T6, family_stats(T6, [T6.order(np.eye(3, dtype=int), t)], (1, 1, 2))[1],
                          (1, 1, 2))
    tr_dev = max(tr_dev, float(np.max(np.abs(Rm_t - Rm_base))))
ax6 = S6[1:4].mean(axis=1)
check("E2 [numerical, 1e-14] T6 gravity, 6^3 torus (the non-flat check), ground sector (0,0,0), "
      "E_sea %.6f, gap %.6f, tau=0.5, declared 27-even-translation family (reduction R2: every "
      "shift G in {0,3}^3 has e^{-iG.t} = 1 on (2Z)^3, so the family's response matrix is the "
      "base order's; certified against two declared translated orders to %.1e). Sea baseline = "
      "the TT note: TT rank %s, first sv %s at n = (1,0,0)/(1,1,0)/(1,2,0)/(1,1,1)/(1,1,2)/"
      "(1,2,3), site response <= %.1e, shear %.1e, face-diagonal %.1e. Disturbed law: site 1/2 "
      "to %.1e, response <= %.1e, TT rank unchanged (%s), amplitudes fall to %s; the axis pair "
      "statistic goes from %.6f to %.6f/%.6f/%.6f (mean %.6f), the face-diagonal statistics come "
      "alive at %.1e and the shear columns stay exactly %.1e, while the axis-pair response at "
      "G != 0 runs %.1e - %.1e -- the reduced family's period-2 artefact, not physics. The "
      "rotation-averaged O_h x (2Z)^3 family (1296 orders) is above this runner's budget and is "
      "QUOTED, not recomputed, from out_grav_L6_even48.txt:A1-A2 -- site 1/2 to 2.7e-15, "
      "response <= 1.4e-16, TT rank 2, sv 0.004079 / 0.001423, s_min/s_max 0.3488 at n = (1,1,2) "
      "against the sea's 0.015679 / 0.004882 and 0.3114: a fall by 3.8 / 3.4 with the "
      "conditioning at its kinematic value. [%.0fs]"
      % (T6.E, T6.gap, tr_dev, [sea6[n]["rank"] for n in MOM6],
         ["%.6f" % sea6[n]["sv"][0] for n in MOM6], max(sea6[n]["site"] for n in MOM6),
         max(sea6[n]["shear"] for n in MOM6), max(sea6[n]["fdstat"] for n in MOM6),
         float(np.max(np.abs(S6[0] - 0.5))), max(mix6[n]["site"] for n in MOM6),
         [mix6[n]["rank"] for n in MOM6], ["%.6f" % mix6[n]["sv"][0] for n in MOM6],
         float(np.mean(-np.abs(T6.P[np.arange(T6.V), T6.J[0]]) ** 2)), ax6[0], ax6[1], ax6[2],
         float(ax6.mean()), float(np.max(np.abs(S6[4:10]))),
         max(mix6[n]["shear"] for n in MOM6), min(mix6[n]["off"] for n in MOM6),
         max(mix6[n]["off"] for n in MOM6), time.time() - tE2),
      abs(T6.E + 258.857540) < 5e-6 and abs(T6.gap - 3.464102) < 5e-6 and tr_dev < 1e-14
      and [sea6[n]["rank"] for n in MOM6] == [1, 1, 1, 2, 2, 2]
      and [mix6[n]["rank"] for n in MOM6] == [1, 1, 1, 2, 2, 2]
      and abs(sea6[(1, 0, 0)]["sv"][0] - 0.030359) < 5e-6
      and abs(sea6[(1, 1, 0)]["sv"][0] - 0.023311) < 5e-6
      and abs(sea6[(1, 2, 0)]["sv"][0] - 0.020249) < 5e-6
      and abs(sea6[(1, 1, 1)]["sv"][0] - 0.013664) < 5e-6
      and abs(sea6[(1, 1, 1)]["sv"][1] - 0.013664) < 5e-6
      and abs(sea6[(1, 1, 2)]["sv"][0] - 0.015679) < 5e-6
      and abs(sea6[(1, 1, 2)]["sv"][1] - 0.004882) < 5e-6
      and abs(sea6[(1, 2, 3)]["sv"][0] - 0.009180) < 5e-6
      and max(sea6[n]["site"] for n in MOM6) < 1e-17
      and max(sea6[n]["fdstat"] for n in MOM6) < 1e-30
      and abs(mix6[(1, 0, 0)]["sv"][0] - 0.019545) < 5e-6
      and abs(mix6[(1, 1, 0)]["sv"][0] - 0.016647) < 5e-6
      and abs(mix6[(1, 2, 0)]["sv"][0] - 0.013441) < 5e-6
      and abs(mix6[(1, 1, 1)]["sv"][0] - 0.009104) < 5e-6
      and abs(mix6[(1, 1, 2)]["sv"][0] - 0.003763) < 5e-6
      and abs(mix6[(1, 2, 3)]["sv"][0] - 0.003910) < 5e-6
      and float(np.max(np.abs(S6[0] - 0.5))) < 1e-14
      and max(mix6[n]["site"] for n in MOM6) < 1e-14
      and abs(ax6[0] + 0.001009) < 5e-6 and abs(ax6[2] + 0.031317) < 5e-6
      and max(mix6[n]["shear"] for n in MOM6) == 0.0)

# ==========================================================================
# E3 -- how disturbed the vacuum is: the binding energy and the kernel distance
tE3 = time.time()
en = {}
for T, orders, name in ((T4, ROT48, "4^3"),
                        (T6, [BASE6, T6.order(np.eye(3, dtype=int), (2, 0, 0)),
                              T6.order(np.eye(3, dtype=int), (2, 4, 2))], "6^3")):
    Es, dists, fds = [], [], []
    Pf = np.linalg.norm(T.P)
    for o in orders:
        K = kernel(schedule_G(T.C, star_masks(T.C, o), TAU), T.Uo)
        Es.append(float(np.trace(T.h @ K).real))
        dists.append(float(np.linalg.norm(K - T.P)) / Pf)
        fds.append(float(np.max(np.abs(K[np.arange(T.V), T.JD[0]]) ** 2)))
    en[name] = (float(np.mean(Es)), float(np.mean(Es)) / T.E, float(np.mean(dists)),
                max(dists) - min(dists), max(fds), T.E)
Ecube = res[0.5]["E"]
check("E3 [numerical, 1e-12] T6's price on the vacuum itself, tau=0.5. On the 4^3 torus every "
      "order of the declared family gives tr(h K_pi) = %.6f against the sea's %.6f, so the tick "
      "keeps %.4f of the sea's binding energy at kernel distance ||K_pi - P||_F/||P||_F = %.4f "
      "(spread over the family %.1e); on the 6^3 torus %.6f against %.6f, %.4f kept at distance "
      "%.4f. The face-diagonal |K|^2, exactly zero on the sea, reaches %.2e / %.2e per order. "
      "For scale, the cube's 40320 orders keep %.4f of its binding energy (%.6f against %.6f, "
      "min %.6f max %.6f). On the tori the tick is an order-one rotation of the vacuum's kernel, "
      "not a perturbation of it. [%.0fs]"
      % (en["4^3"][0], en["4^3"][5], en["4^3"][1], en["4^3"][2], en["4^3"][3], en["6^3"][0],
         en["6^3"][5], en["6^3"][1], en["6^3"][2], en["4^3"][4], en["6^3"][4],
         float(np.mean(Ecube)) / E1p, float(np.mean(Ecube)), E1p, float(Ecube.min()),
         float(Ecube.max()), time.time() - tE3),
      abs(en["4^3"][1] - 0.2423) < 5e-5 and abs(en["4^3"][2] - 0.8705) < 5e-5
      and en["4^3"][3] < 1e-12 and abs(en["6^3"][1] - 0.2346) < 5e-5
      and abs(en["6^3"][2] - 0.8724) < 5e-5 and abs(en["4^3"][4] - 3.43e-2) < 5e-4
      and abs(float(np.mean(Ecube)) / E1p - 0.7645) < 5e-5
      and abs(float(Ecube.min()) - E1p) < 1e-12)

t_end = time.time() - T0
check("F1 [timing] cube structural identity + 40320-order censuses + tau scans %.0f s, slab "
      "many-body on |J| = 473088 %.0f s, Born trees and menus %.0f s, determinantal structure "
      "and the Slater fits %.0f s, the two tori %.0f s; total %.0f s < AUDIT_TIMEOUT_SEC = %d. "
      "One process, no network, no dense object above 4096 x 4096 (the 2^20 slab space is held "
      "sparse on its half-filling index set), peak memory under 1 GB, NO SEED anywhere."
      % (tB3 - tA, tC - tB3, tD - tC, tE - tD, time.time() - tE, t_end, AUDIT_TIMEOUT_SEC),
      t_end < AUDIT_TIMEOUT_SEC)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
