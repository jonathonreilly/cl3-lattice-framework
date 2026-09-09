#!/usr/bin/env python3
"""Copied symplectic/encoding/gauge machinery from the landed runner
scripts/emergent_fermion_pi_flux_sector_staggered_kinetic_form_check_2026_09_02.py
(branch origin/physics-loop/staggered-kinetic-form-pi-flux-sector).
Repo untouched; this is a scratch copy with induced_eta generalised to an
arbitrary consistent flux sector."""

from __future__ import annotations
import itertools
from collections import deque
import numpy as np


EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a); axes 0,1,2 = 1,2,3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def wrap(v, dims):
    return tuple(v[i] % dims[i] for i in range(3))


# ================================================== one-cell 8-dimensional algebra

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)

def pcnt(n):
    return bin(n).count("1")


class Q:
    """i^k X^x Z^z on a register of qubits indexed by bit position."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k & 3
        self.x = x
        self.z = z

    def __mul__(a, b):
        return Q(a.k + b.k + 2 * pcnt(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def neg(s):
        return Q(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def herm(s):
        return (s.k & 1) == (pcnt(s.x & s.z) & 1)

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def ismI(s):
        return s.x == 0 and s.z == 0 and s.k == 2

    def vec(s, n):
        return s.x | (s.z << n)


IDQ = Q(0, 0, 0)


def qprod(seq):
    o = IDQ
    for p in seq:
        o = o * p
    return o


class Lat:
    """Coarse cubic block or torus with the BK superfast encoding on its edges."""

    def __init__(self, dims, periodic):
        self.dims = tuple(dims)
        self.per = periodic
        self.V = [v for v in itertools.product(*(range(d) for d in dims))]
        self.nv = len(self.V)
        self.E = []
        for v in self.V:
            for ax in range(3):
                if self.step(v, EX[ax]) is not None:
                    self.E.append((v, ax))
        self.ei = {e: i for i, e in enumerate(self.E)}
        self.nq = len(self.E)
        self.inc = {}
        for v in self.V:
            d = {}
            for r in range(6):
                w = self.step(v, DIRS[r])
                if w is None:
                    continue
                d[r] = (w, self.ei[(v, r - 3) if r >= 3 else (w, r)])
            self.inc[v] = d
        self.star = {v: sum(1 << q for (_, q) in self.inc[v].values()) for v in self.V}

    def step(self, v, d):
        w = va(v, d)
        if self.per:
            return wrap(w, self.dims)
        return w if all(0 <= w[i] < self.dims[i] for i in range(3)) else None

    def A(self, v, r):
        w, q = self.inc[v][r]
        x, z = 1 << q, 0
        for r2, (_, q2) in self.inc[v].items():
            if r2 < r:
                z ^= 1 << q2
        rb = (r + 3) % 6
        for r2, (_, q2) in self.inc[w].items():
            if r2 < rb:
                z ^= 1 << q2
        p = Q(pcnt(x & z) & 1, x, z)
        return p if r >= 3 else p.neg()

    def Aij(self, i, j):
        for r in range(6):
            if r in self.inc[i] and self.inc[i][r][0] == j:
                return self.A(i, r)
        raise KeyError("not adjacent")

    def B(self, v):
        return Q(0, 0, self.star[v])

    def faces(self):
        out = []
        for v in self.V:
            for d1 in range(3):
                for d2 in range(d1 + 1, 3):
                    a = self.step(v, EX[d1])
                    b = self.step(v, EX[d2])
                    if a is None or b is None:
                        continue
                    c = self.step(a, EX[d2])
                    if c is None:
                        continue
                    out.append((v, a, c, b))
        return out

    def loop(self, cyc):
        n = len(cyc)
        return qprod([self.Aij(cyc[a], cyc[(a + 1) % n]) for a in range(n)]).scal(n)


def transport(L, path):
    """Ordered product of the encoded hops T_{i_{k+1} i_k} = (i/2) A (B - B) along path.

    On any configuration where every step is legal -- source occupied, target
    empty -- each factor contributes (i/2)(+1 - (-1)) = i, hence the i^n.
    """
    n = len(path) - 1
    ops = [L.Aij(path[k + 1], path[k]) for k in range(n)]
    return qprod(ops[::-1]).scal(n)


def f2_pivots(gens):
    piv = {}
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
    return piv


def f2_express(target, piv):
    v, c = target, 0
    while v:
        p = v.bit_length() - 1
        if p not in piv:
            return None
        pv, pc = piv[p]
        v ^= pv
        c ^= pc
    return c


def f2_relations(gens):
    piv, rel = {}, []
    for j, g in enumerate(gens):
        v, c = g, 1 << j
        while v:
            p = v.bit_length() - 1
            if p in piv:
                pv, pc = piv[p]
                v ^= pv
                c ^= pc
            else:
                piv[p] = (v, c)
                break
        if v == 0:
            rel.append(c)
    return rel, len(piv)


def bits(m):
    out = []
    while m:
        b = m & -m
        out.append(b.bit_length() - 1)
        m ^= b
    return out


def solve_f2(rows, nunk):
    mask = (1 << nunk) - 1
    piv, R = [], []
    for r in rows:
        for i, p in enumerate(piv):
            if (r >> p) & 1:
                r ^= R[i]
        low = r & mask
        if low == 0:
            if r:
                return None
            continue
        p = low.bit_length() - 1
        for i in range(len(R)):
            if (R[i] >> p) & 1:
                R[i] ^= r
        R.append(r)
        piv.append(p)
    sol = 0
    for i, p in enumerate(piv):
        if (R[i] >> nunk) & 1:
            sol |= 1 << p

def holonomies(L, eta):
    out = set()
    for f in L.faces():
        v, a, c, b = f
        pr = 1
        for (p, q) in ((v, a), (a, c), (b, c), (v, b)):
            for ax in range(3):
                if L.step(p, EX[ax]) == q and (p, ax) in eta:
                    pr *= eta[(p, ax)]
                    break
                if L.step(q, EX[ax]) == p and (q, ax) in eta:
                    pr *= eta[(q, ax)]
                    break
        out.add(pr)
    return out


def gauge_witness(L, e1, e2):
    s = {L.V[0]: 1}
    dq = deque([L.V[0]])
    adj = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        adj.setdefault(v, []).append((w, v, ax))
        adj.setdefault(w, []).append((v, v, ax))
    while dq:
        v = dq.popleft()
        for (w, src, ax) in adj.get(v, []):
            r = e1[(src, ax)] * e2[(src, ax)]
            if w in s:
                if s[w] != s[v] * r:
                    return None
            else:
                s[w] = s[v] * r
                dq.append(w)
    return s if len(s) == L.nv else None


def one_particle(L, eta):
    idx = {v: i for i, v in enumerate(L.V)}
    M = np.zeros((L.nv, L.nv))
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        M[idx[w], idx[v]] += eta[(v, ax)]
        M[idx[v], idx[w]] += eta[(v, ax)]
    return M



# --------------------------------------------------------------------------
# generalisation of the runner's induced_eta: arbitrary consistent sector
# --------------------------------------------------------------------------

def sector_eta(L, face_vals, wilson=(1, 1, 1)):
    """Link sign field realising the flux sector S_f = face_vals[f] on Lat L.

    Identical to the runner's induced_eta (spanning-tree gauge fixing, then
    fundamental-cycle transport with the residual Z4 phase read off) except
    that the face eigenvalues are supplied instead of being fixed at -1.
    Returns (eta, consistent).  eta is None when the sector is inconsistent.
    """
    root = L.V[0]
    par = {root: None}
    dq = deque([root])
    while dq:
        v = dq.popleft()
        for r in range(6):
            if r not in L.inc[v]:
                continue
            w = L.inc[v][r][0]
            if w not in par:
                par[w] = v
                dq.append(w)
    tree = {frozenset((v, w)) for w, v in par.items() if v is not None}

    def tpath(v):
        p = [v]
        while par[p[-1]] is not None:
            p.append(par[p[-1]])
        return p[::-1]

    F = L.faces()
    gens = [L.loop(f) for f in F]
    vals = list(face_vals)
    assert len(vals) == len(F)
    if L.per:
        for ax in range(3):
            cyc = [wrap(tuple((k if i == ax else 0) for i in range(3)), L.dims)
                   for k in range(L.dims[ax])]
            gens.append(transport(L, cyc + [cyc[0]]))
        vals += list(wilson)
    gv = [g.vec(L.nq) for g in gens]
    piv = f2_pivots(gv)
    cons = True
    rels, _ = f2_relations(gv)
    for r in rels:
        idxs = bits(r)
        pr = qprod([gens[j] for j in idxs])
        eps = 1 if pr.isI() else (-1 if pr.ismI() else 0)
        pv = 1
        for j in idxs:
            pv *= vals[j]
        if eps == 0 or pv != eps:
            cons = False
    if not cons:
        return None, False
    eta = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        if frozenset((v, w)) in tree:
            eta[(v, ax)] = 1
            continue
        pv, pw = tpath(v), tpath(w)
        op = transport(L, pv + [w] + pw[::-1][1:])
        c = f2_express(op.vec(L.nq), piv)
        if c is None:
            return None, False
        idxs = bits(c)
        pr = qprod([gens[j] for j in idxs])
        resid = (op.k - pr.k) & 3
        if resid not in (0, 2):
            return None, False
        e = 1 if resid == 0 else -1
        for j in idxs:
            e *= vals[j]
        eta[(v, ax)] = e
    return eta, True


def face_holonomy_list(L, eta):
    """Plaquette holonomy of eta, one entry per face in L.faces() order."""
    out = []
    for (v, a, c, b) in L.faces():
        pr = 1
        for (p, q) in ((v, a), (a, c), (b, c), (v, b)):
            for ax in range(3):
                if L.step(p, EX[ax]) == q and (p, ax) in eta:
                    pr *= eta[(p, ax)]
                    break
                if L.step(q, EX[ax]) == p and (q, ax) in eta:
                    pr *= eta[(q, ax)]
                    break
        out.append(pr)
    return out


def levels(L, eta):
    """Sorted one-particle spectrum of the hopping sum_ij eta_ij c_i^dag c_j."""
    return np.sort(np.linalg.eigvalsh(one_particle(L, eta)))


def ladder(ev):
    """E_N = sum of the N lowest levels, N = 0..V, as a numpy array."""
    return np.concatenate(([0.0], np.cumsum(ev)))
