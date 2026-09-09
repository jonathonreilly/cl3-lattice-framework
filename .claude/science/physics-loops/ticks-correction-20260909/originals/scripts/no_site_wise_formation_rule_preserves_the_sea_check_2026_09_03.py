#!/usr/bin/env python3
"""No site-wise formation rule preserves the sea's registration under tick evolution;
the eigenvector condition is per step and set-wise.

Class-A finite-dimensional runner, self-contained. Qubits sit on the EDGE sites of two
finite subgraphs of the cubic lattice: the 2x2x2 cube (8 corners, 12 edge sites, 6
faces, record space 2^12 = 4096, held whole) and the 2x2x3 slab open in z (12 corners,
20 edge sites, 11 faces, record space 2^20, held only on the conserved half-filling index
set J, |J| = 473088, as a sparse matrix and 7.5 MB vectors; no dense object above
4096 x 4096 is formed anywhere and peak memory stays well under 1 GB). A record at an
edge site REGISTERS a Z-value there. The law is H = -sum_e eta_e T_e with the
Kawamoto-Smit staggered signs (flux -1 on every face, the pi-flux sector), t = 1; the
sea is the ground state of H in the code space at half filling. Between formations the
pre-record state runs by exp(-i tau H_R), H_R = the hop terms on the UNRECORDED edges
(PR #7876 Model A; P_S H P_S = H_R exactly). Formation = Lueders conditioning with the
Born odds of the current pre-record state.

THE RULES, declared in full (a rule is a map (state, record set) -> next site; greedy =
deterministic argmax with the lowest edge index on ties after rounding to 1e-9):
  A1  energy-above-sea   r_q = max(eps_q(psi) - eps_q(sea), 0), eps_q = <psi|h_q|psi>
  A1v corner form        eps_v = (1/2) sum_{e in star(v)} eps_e, r_e = mean endpoint excess
  A2  energy-scale       r_q = |eps_q(psi)|;   A2v its corner form
  B   least-entangled    argmax of the purity Tr rho_q^2 of the one-site reduced state
  C   declared orders    the identity 0..11 and its 11 cyclic shifts, the reverse and its
                         11 cyclic shifts (24 orders, cube); the identity 0..5 (slab)
  D   corner sets        joint formation of whole corner stars, evolving after each star
  E   eigenvector-first  argmin over free q of the Born-weighted H_{R+q} residual of the
                         two conditioned states; the rule "exists" iff that minimum is 0
For the stochastic A rules the greedy (max-rate) path is walked and the stochastic odds
along it are quantified: contrast = max odds x number of free sites (1 = uniform) and
p_chosen = the odds of the greedy site.

Every tree is an EXACT enumeration in the unnormalised-branch form: the branch vectors of
one level live in disjoint record sectors, so the whole level is one vector Phi with a
node label per basis state; Lueders conditioning with both outcomes is then the identity
on Phi, the per-node Born odds are bincounts of |Phi|^2, and the evolution of every branch
at once is exp(-i tau H_lev) Phi with H_lev = H with the hops on each node's OWN recorded
edges zeroed (a mask on the sparse data). The law after every record has formed is
|Phi|^2 exactly. The propagator is the Chebyshev (Jacobi-Anger) series of exp(-i tau H_lev)
with the rigorous spectral bound ||H_R|| <= number of free edges (each hop term T_e has
T_e^2 = (1 - B_i B_j)/2, so ||T_e|| = 1), truncated where the Bessel coefficients fall below
1e-17; it agrees with scipy's expm_multiply to 1e-16 and keeps three live vectors and no
matrix copy. Nothing is sampled and there is no seed anywhere: the Lanczos start on the
slab is the fixed vector cos(0.7 i + 0.3) + i cos(1.3 i + 1.1) projected into the code
space, and every order and set is declared above. Reductions over the 473088-entry slab
vectors are done by exact (fsum) or pairwise summation wherever a residual near zero is
reported, because a sequential Rayleigh quotient over that many terms carries a ~4e-12
floor (its variance form even comes out negative) -- the cancellation trap of PR #7902.

Source blocks reproduced (scratch T1 of 2026-09-03, read-only against the repository;
nothing is imported from any worktree):
  * L3/l3_core.py          Pauli algebra P/pact/comm, cube_cluster, cube_faces, Enc
                           (A_ij, B_v, S_f, hop_pauli), audit R0-R4, code_space
  * L3j/l3j_core.py        the cube: eta_ks, HAMP (here the per-edge hop pairs), NVAL,
                           the 128-dim code space, the sea by one 128 x 128 eigh
  * L3m/l3m_geom.py        slab(), face_flux
  * L3m/l3m_mb.py          the sparse half-filling Model (AMPJ, H, apply_pauli,
                           project_code); the seeded Lanczos start is replaced by the
                           declared deterministic start of PR #7902's runner
  * T1/t1_cube.py          rates A1/A1v/A2/A2v/B/E, select, the 24 orders, the corner
                           sets, cond_sea_marg (margerr), diag_tv, the census
  * T1/t1_slab.py          leaf-TV and full-law TV per level, the E-rule residual scan
  * T1/t1_scan.py          the per-node eigenvector-vs-diagonal-invariance scan and the
                           declared-set residuals on the sea

Line tags. `[exact]` = integer, F2 or symplectic Pauli arithmetic with no floating point
in the statement. `[numerical, tol]` = a deterministic double-precision evaluation of an
exactly specified quantity at the stated threshold.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`. Exit 0 iff FAIL = 0.
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

AUDIT_TIMEOUT_SEC = 180

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


def f3(x):
    return "%.3e" % x


# ==========================================================================
# Pauli algebra in the symplectic representation, phases mod 4  (L3/l3_core.py)
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
    x = x ^ (x >> 32)
    x = x ^ (x >> 16)
    x = x ^ (x >> 8)
    x = x ^ (x >> 4)
    x = x ^ (x >> 2)
    x = x ^ (x >> 1)
    return (x & 1).astype(np.int8)


# ==========================================================================
# the clusters  (L3/l3_core.py cube_cluster, cube_faces; L3m/l3m_geom.py slab, face_flux)
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


def slab(Lx=2, Ly=2, Lz=3):
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


def corner_xyz(s):
    return ((s >> 2) & 1, (s >> 1) & 1, s & 1)


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


# ==========================================================================
# the superfast encoding, its audit and the code-space cosets  (L3/l3_core.py)
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
    recs = [E.record(reps[c]) for c in range(len(reps))]
    for z in range(E.DIM):
        assert E.record(z) == recs[cid[z]]
    return cid, phi, reps, recs


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
        self.src, self.tgt, self.amp, self.p0src, self.p0tgt = [], [], [], [], []
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
            m0 = np.flatnonzero(~self.BIT[q])
            t0 = loc[Z[m0] ^ (1 << q)]
            ok = t0 >= 0
            self.p0src.append(m0[ok].astype(np.int32))
            self.p0tgt.append(t0[ok].astype(np.int32))
        H = sp.coo_matrix((np.concatenate(dat), (np.concatenate(rows), np.concatenate(cols))),
                          shape=(n, n)).tocsr()
        H.sort_indices()
        self.H = H
        self.rows = np.repeat(np.arange(n, dtype=np.int32), np.diff(H.indptr))
        self.cols = H.indices
        self.EI = np.array([i for (i, j) in En.EDGES])
        self.EJ = np.array([j for (i, j) in En.EDGES])
        self.MHALF = np.zeros((self.V, NQ))
        for q, (i, j) in enumerate(En.EDGES):
            self.MHALF[i, q] = self.MHALF[j, q] = 0.5
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
        return sp.csr_matrix((self.H.data * mask, self.cols, self.H.indptr), shape=(self.n, self.n))

    def set_sea(self, sea):
        self.SEA = sea
        self.P_SEA = np.abs(sea) ** 2
        self.SUPP = int((self.P_SEA > 1e-14).sum())
        z0 = np.zeros(self.n, dtype=np.int64)
        self.EPS_SEA = local_energies(self, sea, z0, 1)[0]
        self.EPSV_SEA = self.EPS_SEA @ self.MHALF.T


def local_energies(S, Phi, nid, nn):
    eps = np.zeros((nn, S.NQ))
    for q in range(S.NQ):
        s, t = S.src[q], S.tgt[q]
        ns = nid[s]
        same = ns == nid[t]
        val = -S.amp[q] * (np.conj(Phi[t]) * Phi[s]).imag
        eps[:, q] = np.bincount(ns[same], weights=val[same], minlength=nn)
    return eps


def purities(S, Phi, d, nid, nn, inv_p):
    out = np.zeros((nn, S.NQ))
    for q in range(S.NQ):
        b = S.BIT[q]
        p1 = np.bincount(nid[b], weights=d[b], minlength=nn) * inv_p
        s, t = S.p0src[q], S.p0tgt[q]
        prod = np.conj(Phi[s]) * Phi[t]
        cre = np.bincount(nid[s], weights=prod.real, minlength=nn)
        cim = np.bincount(nid[s], weights=prod.imag, minlength=nn)
        out[:, q] = (1 - p1) ** 2 + p1 ** 2 + 2 * (cre ** 2 + cim ** 2) * inv_p ** 2
    return out


def e_residuals(S, Phi, d, nid, nn, p, G):
    """Born-weighted H_{R+q} residual of the two conditioned states, per node and site
    (direct form, never the variance form)."""
    out = np.zeros((nn, S.NQ))
    nk = 2 * nn
    for q in range(S.NQ):
        s, t = S.src[q], S.tgt[q]
        hq = np.zeros(S.n, dtype=np.complex128)
        hq[t] = (1j * S.amp[q]) * Phi[s]
        Gq = G - hq
        key = nid * 2 + S.BIT[q]
        PB = np.bincount(key, weights=d, minlength=nk)
        EVk = np.bincount(key, weights=(np.conj(Phi) * Gq).real, minlength=nk)
        evk = np.where(PB > 0, EVk / np.where(PB > 0, PB, 1.0), 0.0)
        diff = Gq - evk[key] * Phi
        R2 = np.bincount(key, weights=np.abs(diff) ** 2, minlength=nk)
        resk = np.sqrt(np.where(PB > 0, R2 / np.where(PB > 0, PB, 1.0), 0.0)).reshape(nn, 2)
        pb = PB.reshape(nn, 2) / np.where(p > 0, p, 1.0)[:, None]
        out[:, q] = np.where(pb >= PMIN, pb * resk, 0.0).sum(1)
    return out


def node_residual(S, Phi, nid, nn, p, Hl):
    """per-node residual ||H_R psi - <H_R> psi|| of the normalised branch states, direct form;
    on the large object a node whose bincount residual is already below 1e-8 is re-evaluated
    with pairwise sums so the reported figure is not the sequential-reduction floor."""
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
    return res, ev, G


def cheb_evolve(Hl, v, tau, lam):
    """exp(-i tau Hl) v by the Jacobi-Anger expansion on [-lam, lam], lam >= ||Hl||:
    exp(-i x y) = J_0(x) + 2 sum_{n>=1} (-i)^n J_n(x) T_n(y), x = tau lam, truncated
    two terms past the first n > x with |J_n(x)| < 1e-17."""
    x = tau * lam
    n = int(math.ceil(x))
    while n < x or abs(jv(n, x)) > 1e-17:
        n += 1
    nmax = n + 2
    c = [(1.0 if k == 0 else 2.0) * ((-1j) ** k) * jv(k, x) for k in range(nmax + 1)]
    T0 = v.copy()
    T1 = (Hl @ v) / lam
    out = c[0] * T0 + c[1] * T1
    for k in range(2, nmax + 1):
        T2 = (2.0 / lam) * (Hl @ T1) - T0
        out += c[k] * T2
        T0, T1 = T1, T2
    return out


def tv(p, q):
    return 0.5 * float(np.abs(p - q).sum())


def run_tree(S, rule, tau, depth, order=None, sets=None, margerr=False):
    """Exact tree in the unnormalised-branch form; returns the final law and per-level stats."""
    n, NQ = S.n, S.NQ
    Phi = S.SEA.astype(np.complex128).copy()
    nid = np.zeros(n, dtype=np.int64)
    nn = 1
    Rm = np.zeros(1, dtype=np.int64)
    levels = []
    for k in range(depth):
        d = np.abs(Phi) ** 2
        p = np.bincount(nid, weights=d, minlength=nn)
        alive = p >= PMIN
        inv_p = np.where(p > 0, 1.0 / np.where(p > 0, p, 1.0), 0.0)
        lev = dict(k=k + 1)
        if rule == "D":
            Sset = sets[k]
            qs = [q for q in range(NQ) if (Sset >> q) & 1]
        else:
            if rule == "C":
                qsel = np.full(nn, order[k], dtype=np.int64)
            else:
                free = ((Rm[:, None] >> np.arange(NQ)[None, :]) & 1) == 0
                if rule in ("A1", "A1v", "A2", "A2v"):
                    eps = local_energies(S, Phi, nid, nn) * inv_p[:, None]
                    if rule == "A1":
                        r = np.maximum(eps - S.EPS_SEA[None, :], 0.0)
                    elif rule == "A2":
                        r = np.abs(eps)
                    else:
                        ev = eps @ S.MHALF.T
                        if rule == "A1v":
                            ex = ev - S.EPSV_SEA[None, :]
                            r = np.maximum(0.5 * (ex[:, S.EI] + ex[:, S.EJ]), 0.0)
                        else:
                            ea = np.abs(ev)
                            r = 0.5 * (ea[:, S.EI] + ea[:, S.EJ])
                elif rule == "B":
                    r = purities(S, Phi, d, nid, nn, inv_p)
                else:
                    G = S.intra(nid) @ Phi
                    r = -e_residuals(S, Phi, d, nid, nn, p, G)
                r = np.where(free, r, -np.inf)
                qsel = np.argmax(np.round(r, 9), axis=1)
                if rule[0] == "A":
                    rf = np.where(free, np.maximum(r, 0.0), 0.0)
                    tot = rf.sum(1)
                    nfree = free.sum(1)
                    odds = np.where(tot[:, None] > 1e-12, rf / np.where(tot > 1e-12, tot, 1.0)[:, None],
                                    free / np.maximum(nfree, 1)[:, None])
                    contrast = odds.max(1) * nfree
                    pch = odds[np.arange(nn), qsel]
                    lev["contrast"] = float(np.mean(contrast[alive]))
                    lev["pch"] = float(np.mean(pch[alive]))
                if rule == "E":
                    emin = -r[np.arange(nn), qsel]
                    lev["emin"] = float(emin[alive][0])
                    lev["emin_min"] = float(emin[alive].min())
                    lev["emin_spread"] = float(emin[alive].max() - emin[alive].min())
            lev["q_w"] = np.bincount(qsel[alive], weights=p[alive], minlength=NQ)
            if margerr:
                b = ((S.Z >> qsel[nid]) & 1).astype(bool)
                p1 = np.bincount(nid[b], weights=d[b], minlength=nn) * inv_p
                sm = np.bincount(nid, weights=S.P_SEA, minlength=nn)
                s1 = np.bincount(nid[b], weights=S.P_SEA[b], minlength=nn)
                okm = alive & (sm > 0)
                me = np.abs(p1 - s1 / np.where(sm > 0, sm, 1.0))
                lev["margerr"] = float((p[okm] * me[okm]).sum() / p[okm].sum())
            qs = None
        # --- split: Lueders conditioning with both outcomes is the identity on Phi
        if rule == "D":
            key = np.zeros(n, dtype=np.int64)
            for a, q in enumerate(qs):
                key |= S.BIT[q].astype(np.int64) << a
            new = nid * (1 << len(qs)) + key
        else:
            qz = qsel[nid]
            new = nid * 2 + ((S.Z >> qz) & 1)
        uniq, inv = np.unique(new, return_inverse=True)
        nid = inv.astype(np.int64)
        nn = len(uniq)
        if rule == "D":
            Rm = Rm[uniq >> len(qs)] | Sset
        else:
            par = uniq >> 1
            Rm = Rm[par] | (1 << qsel[par])
        d = np.abs(Phi) ** 2
        p = np.bincount(nid, weights=d, minlength=nn)
        alive = p >= PMIN
        nrec = int(bin(int(Rm[0])).count("1"))
        Hl = S.intra(nid)
        res, ev, _ = node_residual(S, Phi, nid, nn, p, Hl)
        if tau > 0 and nrec < NQ:
            Phi2 = cheb_evolve(Hl, Phi, tau, float(NQ - nrec))
            dtv = 0.5 * np.bincount(nid, weights=np.abs(d - np.abs(Phi2) ** 2), minlength=nn) \
                * np.where(p > 0, 1.0 / np.where(p > 0, p, 1.0), 0.0)
            Phi = Phi2
        else:
            dtv = np.zeros(nn)
        del Hl
        full = np.abs(Phi) ** 2
        psea = np.bincount(nid, weights=S.P_SEA, minlength=nn)
        lev.update(nrec=nrec, nalive=int(alive.sum()),
                   res_w=float((p[alive] * res[alive]).sum() / p[alive].sum()),
                   res_max=float(res[alive].max()),
                   dtv_w=float((p[alive] * dtv[alive]).sum() / p[alive].sum()),
                   dtv_max=float(dtv[alive].max()),
                   res_list=res[alive], dtv_list=dtv[alive],
                   leaf_tv=0.5 * float(np.abs(p - psea).sum()),
                   full_tv=tv(full, S.P_SEA), support=int((full > 1e-14).sum()))
        levels.append(lev)
    return dict(law=np.abs(Phi) ** 2, levels=levels)


def set_residual(S, bits, vals):
    """residual of the sea conditioned on the declared records (bits, vals) under H_R (t1_scan.py)."""
    m = np.ones(S.n, dtype=bool)
    R = 0
    for q, b in zip(bits, vals):
        m &= (S.BIT[q] if b else ~S.BIT[q])
        R |= 1 << q
    ph = np.where(m, S.SEA, 0)
    ph = ph / np.linalg.norm(ph)
    nid = np.zeros(S.n, dtype=np.int64)
    nid[~m] = 1
    Hl = S.intra(nid)
    Rm = np.zeros(2, dtype=np.int64)
    Rm[:] = R
    p = np.array([1.0, 0.0])
    res, ev, _ = node_residual(S, ph, nid, 2, p, Hl)
    return float(res[0]), float(ev[0])


def joint_set(S, mask, tau):
    """one joint formation of the whole set `mask` on the sea, then exp(-i tau H_R):
    per-outcome residuals, the diagonal moved, and the full law afterwards."""
    r = run_tree(S, "D", tau, 1, sets=[mask])
    L = r["levels"][0]
    return L, r["law"]


# ==========================================================================
# A. THE CUBE
V8, EDG = cube_cluster()
FAC = cube_faces()
EnC = Enc(8, sorted(EDG), FAC)
AUDC = audit(EnC)
ok_c = all(AUDC[k] for k in ("R0_welldef", "R0_antisym", "R1", "R2", "R3", "R4", "grp_ok"))
ETA_C = []
for (i, j) in EnC.EDGES:
    ETA_C.append(eta_ks(corner_xyz(min(i, j)), {4: 0, 2: 1, 1: 2}[min(i, j) ^ max(i, j)]))
FLUX_C = face_flux(FAC, EnC.EDGES, ETA_C)
ZC = np.arange(4096, dtype=np.int64)
SC = Space(EnC, ETA_C, ZC, ZC, "cube")
CID, PHI, REPS, RECS = code_space(EnC, AUDC)
W = np.zeros((4096, 128), dtype=np.complex128)
W[ZC, CID] = PHI / np.sqrt(32.0)
HW = SC.H @ W
HC = W.conj().T @ HW
herm_c = float(np.max(np.abs(HC - HC.conj().T)))
inv_c = float(np.max(np.abs(HW - W @ HC)))
EVC, VCC = np.linalg.eigh(HC)
SEA_C = W @ VCC[:, 0]
E_SEA_C = float(EVC[0])
GAP_C = float(EVC[1] - EVC[0])
SC.set_sea(SEA_C)
NVAL_C = np.zeros(4096, dtype=np.int64)
for v in range(8):
    NVAL_C += parity(ZC & EnC.STARMASK[v])
ZERO_C = SC.P_SEA < 1e-14
CHARGE_C = ZERO_C & (NVAL_C != 4)
CANC_C = ZERO_C & (NVAL_C == 4)
HsC = SC.H @ SEA_C
E_SEA_C = math.fsum((np.conj(SEA_C) * HsC).real) / math.fsum(np.abs(SEA_C) ** 2)
sea_res_c = float(np.linalg.norm(HsC - E_SEA_C * SEA_C))


def census(law):
    z = law < 1e-14
    return dict(support=int((~z).sum()), charge=int((z & CHARGE_C).sum()), canc=int((z & CANC_C).sum()),
                tv=tv(law, SC.P_SEA), off=float(law[ZERO_C].sum()))


r1 = [set_residual(SC, [q], [0])[0] for q in range(12)]
r_star0 = set_residual(SC, [0, 1, 2], [0, 0, 0])[0]
check("A1 [exact; 1e-12] cube: R0-R4 %s, k=%d, code %d, D=4096, flux %s x6; sea E=%.12f=-4sqrt3 (%.1e), resid %.1e, "
      "gap %.6f; support %d, zeros %d=%d charge+%d cancellation; eps_q(sea)=%.6f x12 (spread %.0e); residual one edge %.6f=1/sqrt3 x12 "
      "(spread %.0e), star(0) %.1e."
      % (ok_c, AUDC["k"], AUDC["code_dim"], set(FLUX_C), E_SEA_C, abs(E_SEA_C + 4 * np.sqrt(3)), sea_res_c, GAP_C,
         SC.SUPP, int(ZERO_C.sum()), int(CHARGE_C.sum()), int(CANC_C.sum()), SC.EPS_SEA.mean(), np.ptp(SC.EPS_SEA),
         np.mean(r1), np.ptp(r1), r_star0),
      ok_c and AUDC["k"] == 5 and AUDC["code_dim"] == 128 and SC.xpart_ok and set(FLUX_C) == {-1}
      and abs(E_SEA_C + 4 * np.sqrt(3)) < 1e-12 and sea_res_c < 1e-12 and herm_c < 1e-11 and inv_c < 1e-11
      and SC.SUPP == 1984 and int(CHARGE_C.sum()) == 1856 and int(CANC_C.sum()) == 256
      and np.ptp(SC.EPS_SEA) < 1e-12 and abs(SC.EPS_SEA.mean() + 1 / np.sqrt(3)) < 1e-12
      and np.ptp(r1) < 1e-12 and abs(np.mean(r1) - 1 / np.sqrt(3)) < 1e-12 and r_star0 < 1e-12)

SITE_RULES = ("A1", "A1v", "A2", "A2v", "B", "E")
IDENT = list(range(12))
ORDERS = [IDENT[s:] + IDENT[:s] for s in range(12)]
REV = IDENT[::-1]
ORDERS += [REV[s:] + REV[:s] for s in range(12)]
STARS_C = [EnC.STARMASK[v] for v in (0, 3, 5, 6)]
RES = {}
for tau in (0.0, 0.5, 2.0, 0.1):
    for rule in SITE_RULES:
        RES[(rule, tau)] = run_tree(SC, rule, tau, 12, margerr=True)
        RES[(rule, tau)]["c"] = census(RES[(rule, tau)]["law"])
    rD = run_tree(SC, "D", tau, 4, sets=STARS_C)
    rD["c"] = census(rD["law"])
    RES[("D", tau)] = rD
    acc = np.zeros(4096)
    tvs = []
    for oi, o in enumerate(ORDERS):
        rr = run_tree(SC, "C", tau, 12, order=o, margerr=(oi == 0))
        acc += rr["law"] / len(ORDERS)
        tvs.append(tv(rr["law"], SC.P_SEA))
        if oi == 0:
            RES[("Cid", tau)] = rr
    RES[("C", tau)] = dict(c=census(acc), tvs=tvs)
t_cube = time.time() - T0

c0 = [RES[(r, 0.0)]["c"] for r in SITE_RULES] + [RES[("D", 0.0)]["c"], RES[("C", 0.0)]["c"]]
a1_0 = RES[("A1", 0.0)]["levels"]
con0 = [a1_0[k]["contrast"] for k in range(5)]
me0 = max(max(L["margerr"] for L in a1_0), max(L["margerr"] for L in RES[("Cid", 0.0)]["levels"]))
check("A2 [1e-12] T1 tau=0: every rule (A1 A1v A2 A2v B E, D, all 24 orders) reproduces the sea: max TV %.1e / %.1e, support 1984, "
      "1856/1856 charge + 256/256 cancellation zeros kept; margerr <= %.1e at every node; A1 "
      "contrast at steps 1-5 = %s."
      % (max(c["tv"] for c in c0), max(RES[("C", 0.0)]["tvs"]), me0, "/".join("%.4f" % c for c in con0)),
      all(c["tv"] < 1e-12 and c["support"] == 1984 and c["charge"] == 1856 and c["canc"] == 256 for c in c0)
      and max(RES[("C", 0.0)]["tvs"]) < 1e-12 and me0 < 1e-12 and all(abs(c - 1) < 1e-9 for c in con0))

c5 = {r: RES[(r, 0.5)]["c"] for r in SITE_RULES}
cD5 = RES[("D", 0.5)]["c"]
dl = RES[("D", 0.5)]["levels"]
check("A3 [1e-12] T2 tau=0.5 TV(sea): A1 %.9f A1v %.9f A2 %.9f A2v %.9f B %.9f E %.9f; each support 2240, 1856/1856 charge, "
      "0/256 cancellation kept; D (stars 0,3,5,6) TV %.1e, 256/256, node "
      "residual <= %.1e, diagonal displaced <= %.1e."
      % tuple([c5[r]["tv"] for r in SITE_RULES] + [cD5["tv"],
                                                 max(L["res_max"] for L in dl), max(L["dtv_max"] for L in dl)]),
      all(0.30 < c5[r]["tv"] < 0.46 and c5[r]["support"] == 2240 and c5[r]["charge"] == 1856 and c5[r]["canc"] == 0 for r in SITE_RULES)
      and cD5["tv"] < 1e-12 and cD5["canc"] == 256 and cD5["support"] == 1984
      and max(L["res_max"] for L in dl) < 1e-12 and max(L["dtv_max"] for L in dl) < 1e-12)

tvs5 = RES[("C", 0.5)]["tvs"]
cC5 = RES[("C", 0.5)]["c"]
check("A4 T2 24 orders tau=0.5: per-order TV min %.9f (order %d%s) max %.9f mean %.9f, identity %.9f, each support 2240, 0/256 cancellation; "
      "their average law TV %.9f with support %d, not 1984."
      % (min(tvs5), int(np.argmin(tvs5)), " = reverse" if int(np.argmin(tvs5)) == 12 else "", max(tvs5), float(np.mean(tvs5)), tvs5[0],
         cC5["tv"], cC5["support"]),
      0.28 < min(tvs5) and max(tvs5) < 0.46 and 0.2 < cC5["tv"] < min(tvs5) and cC5["support"] == 2240 and cC5["canc"] == 0)

rows = []
okt = True
for tau in (0.1, 2.0):
    cc = [RES[(r, tau)]["c"] for r in SITE_RULES]
    tvo = RES[("C", tau)]["tvs"]
    cD = RES[("D", tau)]["c"]
    okt &= all(c["canc"] == 0 and c["support"] == 2240 and c["tv"] > 0.04 for c in cc) and all(t > 0.04 for t in tvo) \
        and cD["tv"] < 1e-12 and cD["canc"] == 256
    rows.append("tau %.1f: %s, orders %.4f-%.4f, D %.1e" % (
        tau, " ".join("%s %.4f" % (r, c["tv"]) for r, c in zip(SITE_RULES, cc)), min(tvo), max(tvo), cD["tv"]))
check("A5 T2 TV(sea) at %s; every site-wise law support 2240 with 0/256 cancellation at both; D 256/256 at both." % "; ".join(rows), okt)

a1 = RES[("A1", 0.5)]["levels"]
top = [int(np.argmax(L["q_w"])) for L in a1[:4]]
a1v = RES[("A1v", 0.5)]["levels"]
topv = [int(np.argmax(L["q_w"])) for L in a1v[:5]]
check("A6 [1e-12] T4 cube A1 tau=0.5 forms %s (the z-matching): contrast %s, greedy odds %s, margerr %s then %.3f at step 4; residual "
      "%s, diagonal displaced %s. A1v: star(0) then star(4) in 5 records (%s), residual %.3f after its 3rd."
      % ("".join("(%d,%d)" % EnC.EDGES[q] for q in top), "/".join("%.2f" % L["contrast"] for L in a1[:4]),
         "/".join("%.3f" % L["pch"] for L in a1[:4]), "/".join("%.0e" % L["margerr"] for L in a1[:3]), a1[3]["margerr"],
         "/".join("%.2f" % L["res_w"] for L in a1[:4]), "/".join("%.3f" % L["dtv_w"] for L in a1[:4]),
         "".join("(%d,%d)" % EnC.EDGES[q] for q in topv), a1v[2]["res_w"]),
      top == [0, 5, 8, 11] and abs(a1[0]["contrast"] - 1) < 1e-9 and all(L["pch"] >= 0.44 for L in a1[1:4])
      and all(L["margerr"] < 1e-12 for L in a1[:3]) and a1[3]["margerr"] > 0.1 and all(L["res_w"] > 0.4 for L in a1[:4])
      and all(L["dtv_w"] > 0.05 for L in a1[:4]) and set(topv) == set(EnC.STAR[0]) | set(EnC.STAR[4]) and a1v[2]["res_w"] > 0.5)

rs = dict(same_star=set_residual(SC, [0, 1], [0, 0])[0], parallel=set_residual(SC, [0, 5], [0, 0])[0],
          far=set_residual(SC, [0, 11], [0, 0])[0], not_star=set_residual(SC, [0, 5, 8], [0, 0, 0])[0],
          zmatch=set_residual(SC, [0, 5, 8, 11], [0, 0, 0, 0])[0])
scan = []
oks = True
for tau in (0.5, 0.1, 2.0):
    for key in ("A1", "Cid", "A1v", "B"):
        Ls = RES[(key, tau)]["levels"]
        res = np.concatenate([L["res_list"] for L in Ls])
        dtv = np.concatenate([L["dtv_list"] for L in Ls])
        non = res > 1e-6
        n_inv = int((dtv[non] < 1e-9).sum())
        n_mov = int((dtv[~non] > 1e-9).sum())
        scan.append((tau, key, len(res), int(non.sum()), n_inv, int((~non).sum()), n_mov, float(dtv[non].min())))
        oks &= n_inv == 0 and n_mov == 0 and float(dtv[non].min()) > 5e-5
check("A7 T5 sea conditioned on two edges of one star %.6f, two parallel z-edges %.6f, two far edges %.6f=sqrt(2/3), a whole "
      "star %.1e, three edges not a star %.6f, the z-matching %.6f. Scan of 12 trees (A1, identity, A1v, B x tau 0.5/0.1/2.0; %d-%d nodes): "
      "non-eigenvector nodes (res > 1e-6) with invariant diagonal (< 1e-9) %d of %d; eigenvector nodes displaced %d of %d; min displacement "
      "among non-eigenvector nodes %.1e/%.1e/%.1e at tau 0.1/0.5/2.0."
      % (rs["same_star"], rs["parallel"], rs["far"], r_star0, rs["not_star"], rs["zmatch"],
         min(s[2] for s in scan), max(s[2] for s in scan), sum(s[4] for s in scan), sum(s[3] for s in scan),
         sum(s[6] for s in scan), sum(s[5] for s in scan),
         min(s[7] for s in scan if s[0] == 0.1), min(s[7] for s in scan if s[0] == 0.5), min(s[7] for s in scan if s[0] == 2.0)),
      oks and abs(rs["same_star"] - 1 / np.sqrt(3)) < 1e-9 and abs(rs["parallel"] - 1.0) < 1e-9
      and abs(rs["far"] - np.sqrt(2 / 3)) < 1e-9 and rs["not_star"] > 1.2 and rs["zmatch"] > 1.3)

eL = RES[("E", 0.5)]["levels"]
e0c = RES[("E", 0.0)]["levels"]
emins = [L["emin_min"] for L in eL]
first0 = next((L["k"] for L in eL if L["emin_min"] < 1e-9), None)
check("A8 rule E on the cube, best-site residual (min over all branches): tau=0.5 %s at steps 1-7 (min %.3f), first eigenvector site at step "
      "%d (%d free edges left); tau=0 %s -- the third record completes star(0) exactly, but after one tau=0.5 tick that completion leaves "
      "%.3f; E's final law at tau=0.5: TV %.6f, 0/256 cancellation."
      % ("/".join("%.3f" % e for e in emins[:7]), min(emins[:7]), first0, 12 - first0 + 1,
         "/".join("%.3f" % L["emin_min"] for L in e0c[:4]), eL[2]["emin_min"], c5["E"]["tv"]),
      min(emins[:7]) > 0.45 and first0 is not None and first0 >= 8 and e0c[2]["emin_min"] < 1e-12 and e0c[0]["emin_min"] > 0.5
      and e0c[1]["emin_min"] > 0.5 and eL[2]["emin_min"] > 0.5 and c5["E"]["canc"] == 0)

# ==========================================================================
# B. THE 2x2x3 SLAB (sparse on J)
VS, EDGES_S, FACES_S, ETA_S = slab(2, 2, 3)
EnS = Enc(VS, EDGES_S, FACES_S)
AUDS = audit(EnS)
ok_s = all(AUDS[k] for k in ("R0_welldef", "R0_antisym", "R1", "R2", "R3", "R4", "grp_ok"))
FLUX_S = face_flux(FACES_S, EDGES_S, ETA_S)
DEG = np.zeros(VS, dtype=int)
for (i, j) in EDGES_S:
    DEG[i] += 1
    DEG[j] += 1
ZS = np.arange(1 << 20, dtype=np.int64)
NVS = np.zeros(1 << 20, dtype=np.int8)
for v in range(VS):
    NVS += parity(ZS & EnS.STARMASK[v])
J = np.flatnonzero(NVS == 6).astype(np.int64)
locS = -np.ones(1 << 20, dtype=np.int64)
locS[J] = np.arange(len(J))
del ZS, NVS
SS = Space(EnS, ETA_S, J, locS, "slab")
SS.set_gens(AUDS["gens"])
tt = np.arange(SS.n, dtype=np.float64)
v0 = SS.project_code(np.cos(0.7 * tt + 0.3) + 1j * np.cos(1.3 * tt + 1.1))
v0 /= np.linalg.norm(v0)
wS, US = spla.eigsh(SS.H, k=3, which="SA", v0=v0, tol=0, maxiter=20000)
sea_s = SS.project_code(US[:, 0])
sea_s /= np.linalg.norm(sea_s)
sh = float(np.abs(wS).max()) + 6.0
npol = 0
for it in range(120):
    sea_s = SS.project_code(sh * sea_s - SS.H @ sea_s)
    sea_s /= np.linalg.norm(sea_s)
    npol += 1
    if it % 20 == 19:
        Hs = SS.H @ sea_s
        ev = math.fsum((np.conj(sea_s) * Hs).real) / math.fsum(np.abs(sea_s) ** 2)
        if np.linalg.norm(Hs - ev * sea_s) < 1e-13:
            break
Hs = SS.H @ sea_s
E_SEA_S = math.fsum((np.conj(sea_s) * Hs).real) / math.fsum(np.abs(sea_s) ** 2)
sea_res_s = float(np.linalg.norm(Hs - E_SEA_S * sea_s))
E_SEA_S_SEQ = float(np.real(np.vdot(sea_s, Hs)))
del Hs, US, v0
SS.set_sea(sea_s)
t_sea = time.time() - T0
eps_s = SS.EPS_SEA
epsv_s = SS.EPSV_SEA
r1s = np.array([set_residual(SS, [q], [0])[0] for q in range(20)])
out_plane = [q for q, (i, j) in enumerate(EDGES_S) if DEG[i] == 3 and DEG[j] == 3]
mid = [q for q in range(20) if q not in out_plane]
E0S = -(8 + 2 * np.sqrt(2))
check("B1 [exact; 1e-10] slab 2x2x3 open in z: degrees %s, 20 edges, %d faces, R0-R4 %s, k=%d, code %d, flux %s x%d, |J|=%d; "
      "sea by Lanczos + %d polish steps: E=%.12f=-(8+2sqrt2) (%.1e; the sequential Rayleigh quotient is "
      "off by %.1e), resid %.1e, support %d; eps(sea) %.6f x%d / %.6f=-(1+sqrt2)/4 x%d; corner %.4f (deg 4) / %.4f (deg 3); one-edge residual "
      "%.6f=sqrt(3/8) / %.6f."
      % ("".join(str(d) for d in DEG), len(FACES_S), ok_s, AUDS["k"], AUDS["code_dim"], set(FLUX_S), len(FLUX_S), SS.n, npol,
         E_SEA_S, abs(E_SEA_S - E0S), abs(E_SEA_S_SEQ - E0S), sea_res_s, SS.SUPP, eps_s[mid].mean(), len(mid), eps_s[out_plane].mean(),
         len(out_plane), epsv_s[DEG == 4].mean(), epsv_s[DEG == 3].mean(), r1s[mid].mean(), r1s[out_plane].mean()),
      ok_s and AUDS["k"] == 9 and AUDS["code_dim"] == 2048 and set(FLUX_S) == {-1} and len(FLUX_S) == 11 and SS.n == 473088
      and abs(E_SEA_S - E0S) < 1e-10 and sea_res_s < 1e-10 and SS.SUPP == 411648 and SS.xpart_ok
      and np.ptp(eps_s[mid]) < 1e-8 and abs(eps_s[mid].mean() + 0.5) < 1e-8 and abs(eps_s[out_plane].mean() + (1 + np.sqrt(2)) / 4) < 1e-8
      and abs(r1s[mid].mean() - np.sqrt(3 / 8)) < 1e-8 and np.ptp(r1s[mid]) < 1e-8 and abs(r1s[out_plane].mean() - 0.5638) < 2e-4)

SLAB_RULES = ("A1", "A1v", "A2", "A2v", "B", "E", "C")
KMAX = 6
RS = {}
for rule in SLAB_RULES:
    RS[rule] = run_tree(SS, rule, 0.5, KMAX, order=list(range(KMAX)) if rule == "C" else None)
RS2 = {rule: run_tree(SS, rule, 2.0, KMAX, order=list(range(KMAX)) if rule == "C" else None) for rule in ("A1", "C")}
t_slab = time.time() - T0


def sites_of(levels):
    return "".join("(%d,%d)" % EDGES_S[int(np.argmax(L["q_w"]))] for L in levels)


ft = {r: [L["full_tv"] for L in RS[r]["levels"]] for r in SLAB_RULES}
lt = {r: [L["leaf_tv"] for L in RS[r]["levels"]] for r in SLAB_RULES}
sup = {r: [L["support"] for L in RS[r]["levels"]] for r in SLAB_RULES}
ft2 = {r: [L["full_tv"] for L in RS2[r]["levels"]] for r in RS2}
check("B2 [1e-10] T3 %d records, tau=0.5, full 20-edge law vs the sea (A1/A1v/A2/A2v/B/E/C): after one %s "
      "(support %d-%d > 411648), after six %s; order: A1 %s A1v %s A2v %s E %s. tau=2.0: A1/C %.4f/%.4f after one, %.3f/%.3f "
      "after six."
      % (KMAX, "/".join("%.4f" % ft[r][0] for r in SLAB_RULES), min(sup[r][0] for r in SLAB_RULES), max(sup[r][0] for r in SLAB_RULES),
         "/".join("%.4f" % ft[r][-1] for r in SLAB_RULES), sites_of(RS["A1"]["levels"]), sites_of(RS["A1v"]["levels"]),
         sites_of(RS["A2v"]["levels"]), sites_of(RS["E"]["levels"]),
         ft2["A1"][0], ft2["C"][0], ft2["A1"][-1], ft2["C"][-1]),
      all(ft[r][0] > 0.11 and sup[r][0] > 411648 for r in SLAB_RULES) and all(0.20 < ft[r][-1] < 0.42 for r in SLAB_RULES)
      and all(min(ft[r]) > 0.11 for r in SLAB_RULES) and all(ft2[r][0] > 0.02 and ft2[r][-1] > 0.3 for r in RS2))

blind3 = max(lt[r][2] for r in SLAB_RULES)
check("B3 [1e-10] T3 leaf-TV on the formed sites is blind: <= %.1e at three records for every rule while the full law is "
      "%.3f-%.3f away; A2/A2v stay at %.1e/%.1e through six (full law %.3f/%.3f); A1 %s at records 3-6, A1v %.3f at 5, B/E/C %.3f/%.3f/%.3f "
      "at 6 only."
      % (blind3, min(ft[r][2] for r in SLAB_RULES), max(ft[r][2] for r in SLAB_RULES), lt["A2"][5], lt["A2v"][5], ft["A2"][5], ft["A2v"][5],
         "/".join("%.3f" % x for x in lt["A1"][2:6]), lt["A1v"][4], lt["B"][5], lt["E"][5], lt["C"][5]),
      blind3 < 1e-10 and lt["A2"][5] < 1e-10 and lt["A2v"][5] < 1e-10 and lt["A1"][3] > 0.1 and lt["A1v"][4] > 0.1
      and all(lt[r][k] < 1e-10 for r in SLAB_RULES for k in range(3)) and all(lt[r][4] < 1e-10 for r in ("B", "E", "C")))

eS = RS["E"]["levels"]
emS = [L["emin_min"] for L in eS]
allres = [L["res_w"] for r in SLAB_RULES for L in RS[r]["levels"]]
alldtv = [L["dtv_w"] for r in SLAB_RULES for L in RS[r]["levels"]]
check("B4 [1e-9] rule E on the slab: best-site residual %s at records 1-6, identical across a level's branches (spread <= %.1e), never 0, "
      "ending above where it began; residual along every path %.2f-%.2f, diagonal displaced per tick %.3f-%.3f."
      % ("/".join("%.4f" % e for e in emS), max(L["emin_spread"] for L in eS), min(allres), max(allres), min(alldtv), max(alldtv)),
      min(emS) > 0.5 and emS[-1] > emS[0] and max(L["emin_spread"] for L in eS) < 1e-9 and min(allres) > 0.4 and min(alldtv) > 0.05)

a1s = RS["A1"]["levels"]
a2v = RS["A2v"]["levels"]
t1s = [int(np.argmax(L["q_w"])) for L in a1s[:4]]
t2v = [int(np.argmax(L["q_w"])) for L in a2v[:3]]
mid_edges = {q for q, (i, j) in enumerate(EDGES_S) if DEG[i] == 4 and DEG[j] == 4}
check("B5 T4 slab A1: contrast %.6f at step 1, then %s with greedy odds %s at steps 2-6, the parallel z-edges %s first (a matching); "
      "A2v forms the degree-4 corners' middle edges %s first and is worst at six records (%.4f = max of %s)."
      % (a1s[0]["contrast"], "/".join("%.1f" % L["contrast"] for L in a1s[1:6]), "/".join("%.3f" % L["pch"] for L in a1s[1:6]),
         "".join("(%d,%d)" % EDGES_S[q] for q in t1s), "".join("(%d,%d)" % EDGES_S[q] for q in t2v), ft["A2v"][5],
         "/".join("%.3f" % ft[r][5] for r in SLAB_RULES)),
      abs(a1s[0]["contrast"] - 1) < 1e-9 and all(0.43 <= L["pch"] <= 1.0 + 1e-12 for L in a1s[1:4])
      and all(EDGES_S[q][1] - EDGES_S[q][0] == 1 for q in t1s) and len(set(t1s)) == 4 and set(t2v) <= mid_edges
      and ft["A2v"][5] >= max(ft[r][5] for r in SLAB_RULES) - 1e-12)

RE0 = run_tree(SS, "E", 0.0, KMAX)
e0 = RE0["levels"]
s0 = [int(np.argmax(L["q_w"])) for L in e0]
star02 = EnS.STARMASK[0] | EnS.STARMASK[2]
L02, law02 = joint_set(SS, star02, 0.5)
L0, _ = joint_set(SS, EnS.STARMASK[0], 0.0)
L2, _ = joint_set(SS, EnS.STARMASK[2], 0.0)
RD = run_tree(SS, "D", 0.5, 2, sets=[EnS.STARMASK[4], EnS.STARMASK[7]])
dS = RD["levels"]
t_end = time.time() - T0
check("B6 [1e-11] T6 tau=0: rule E on the sea forms %s = star(0) then star(2), best residuals %s; each degree-3 star alone leaves "
      "%.6f=(sqrt2-1)/2 (%.6f/%.6f); the pair star(0) u star(2) restores the eigenvector property exactly: "
      "residual max %.1e over its %d outcomes; control full-law TV <= %.1e."
      % ("".join("(%d,%d)" % EDGES_S[q] for q in s0), "/".join("%.4f" % L["emin_min"] for L in e0), (np.sqrt(2) - 1) / 2, L0["res_max"],
         L2["res_max"], e0[5]["res_max"], e0[5]["nalive"], max(L["full_tv"] for L in e0)),
      set(s0[:3]) == set(EnS.STAR[0]) and set(s0[3:6]) == set(EnS.STAR[2]) and abs(e0[2]["emin_min"] - (np.sqrt(2) - 1) / 2) < 1e-6
      and abs(L0["res_max"] - (np.sqrt(2) - 1) / 2) < 1e-6 and abs(L2["res_max"] - (np.sqrt(2) - 1) / 2) < 1e-6
      and e0[5]["res_max"] < 1e-11 and e0[5]["nalive"] == 64 and max(L["full_tv"] for L in e0) < 1e-11)

check("B7 [1e-11] T6 the six-record JOINT tick on star(0) u star(2) at tau=0.5: residual max %.1e (%d outcomes), diagonal displaced max %.1e, "
      "full-law TV %.1e, support %d; the same six sites one at a time with tau=0.5 ticks (rule C): %.4f. D star(4) then star(7): "
      "full-law TV %.1e/%.1e at 4/8 records, residual max %.1e/%.1e, support %d."
      % (L02["res_max"], L02["nalive"], L02["dtv_max"], L02["full_tv"], L02["support"], ft["C"][5], dS[0]["full_tv"], dS[1]["full_tv"],
         dS[0]["res_max"], dS[1]["res_max"], dS[1]["support"]),
      L02["res_max"] < 1e-11 and L02["nalive"] == 64 and L02["dtv_max"] < 1e-11 and L02["full_tv"] < 1e-11 and L02["support"] == 411648
      and ft["C"][5] > 0.2 and dS[0]["full_tv"] < 1e-11 and dS[1]["full_tv"] < 1e-11 and dS[1]["support"] == 411648
      and dS[0]["res_max"] < 1e-10 and dS[1]["res_max"] < 1e-10 and dS[1]["nalive"] == 256)

check("B8 [timing] cube 124 trees %.0f s, slab sea %.0f s, nine slab trees to %d records %.0f s, total %.0f s < %d s; no dense object "
      "above 4096 x 4096, no seed."
      % (t_cube, t_sea - t_cube, KMAX, t_slab - t_sea, t_end, AUDIT_TIMEOUT_SEC), t_end < AUDIT_TIMEOUT_SEC)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
