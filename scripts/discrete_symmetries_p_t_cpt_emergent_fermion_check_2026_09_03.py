#!/usr/bin/env python3
"""Discrete symmetries P, T and CPT of the emergent fermion.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3, one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding
written on it, with the Kawamoto-Smit link signs
    eta_1 = 1,  eta_2(v) = (-1)^{v_1},  eta_3(v) = (-1)^{v_1+v_2}.
The declared Hamiltonian is
    H(t, m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v,
    A_ij = X(edge) x Z-tails, direction order -x < -y < -z < +x < +y < +z,
    A_ji = -A_ij,  B_v = prod of the six Z's at a corner = I - 2 n_v,
    S_f = the ordered four-A face loop,  T_ij = (i/2) A_ij (B_i - B_j),
    n_v = (I - B_v)/2,  eps_v = (-1)^{v_1+v_2+v_3},
    J_ij = eta_ij (t/2) A_ij (I - B_i B_j),  Q = -(1/2) sum_v B_v.

CONDITIONAL ON IMPROPER ELEMENTS.  The Lattice axiom of
docs/MINIMAL_AXIOMS_2026-06-29.md names "nearest-neighbor adjacency, standard
translations, and proper cubic rotations about each site" -- no improper
element.  Every P-statement below is of the form "if the improper map is
applied, the encoded algebra does this"; nothing here licenses adding an
improper element to the axiom.  That is an axiom-level question for the owner.

  A  T1  PARITY NEEDS A CZ NETWORK.  Inversion shifts the direction order by
     three, so the bare relabelling V_P leaves a pure-Z discrepancy per bond
     that no Z-Pauli can absorb; it defines a symmetric loop-free adjacency,
     hence U_P = G_g D_CZ V_P with U_P A_ij U_P^-1 = sigma_ij A_{P(i)P(j)},
     sigma_ij = eta_ij eta_{P(i)P(j)}; face stabilizers carry no sign.
  B  T2  THE SHIFT-PARITY RULE.  Inversion about a corner: sigma = +1 on every
     bond, eta invariant bond by bond, H(t,m) exactly P-symmetric at every t
     and m.  Cube-centre inversion and the mid-plane reflections send m -> -m.
     eps_{P(v)} = (-1)^{sum c} eps_v depends only on the shift parity.
  C  T3  TIME REVERSAL.  T = Z_E K with Z_E = prod_e Z_e = prod_{v: eps_v = -1}
     B_v, the unique pure-Z choice; the full transformation table; H(t,m)
     invariant for every t and m; T^2 = +1 exactly.
  D  T4  THE DIRAC POINT.  Eight zero modes, gap 2|m|; specified spectral BDI at m=0; corner
     inversion is represented by exactly the staggered-mass matrix
     eps = Z1 Z2 Z3, the emergent gamma^0, anticommuting with the chirality;
     spectral CPT from corner inversion is +I; negative product squares persist
     at nonzero m. Commuting PT and anticommuting C_spec P have distinct domains.
     Many-body unitary C and its CPT table are separate representations.
  E  T5  THE FULL TABLE and fixed-Z diagonal classification; no physical readout.

Groups A, B, C and E are exact: Gaussian-rational coefficients on symplectic
Pauli monomials (F2 supports, Z4 phases), with no floating-point step.  Group D
and the tagged items are floating-point at the stated tolerance.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
import hashlib
from pathlib import Path
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sp

AUDIT_TIMEOUT_SEC = 90

# Actual mutable publication/premise inputs, not scientific substitutes.
AUDIT_INPUT_PATHS = ('docs/DISCRETE_SYMMETRIES_P_T_AND_CPT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
INPUT_SHA256 = {'docs/DISCRETE_SYMMETRIES_P_T_AND_CPT_OF_THE_EMERGENT_FERMION_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c7d3e52300ec4bacb9b241f38cdddb7573cc02bac8c4c48be878d8c7d66955d5', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(INPUT_SHA256):
        raise RuntimeError("input declaration/pin mismatch")
    for rel in AUDIT_INPUT_PATHS:
        body = (root / rel).read_bytes()
        if hashlib.sha256(body).hexdigest() != INPUT_SHA256[rel]:
            raise RuntimeError("changed publication/premise input: " + rel)

verify_inputs()

T0 = time.time()
PASS = 0
FAIL = 0
TOL = 1e-12


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ===================================================== coarse lattice, KS signs

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
DIRS = [(-1, 0, 0), (0, -1, 0), (0, 0, -1), (1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


def wrap(v, dims):
    return tuple(v[i] % dims[i] for i in range(3))


def pcnt(n):
    return bin(n).count("1")


def bits(n):
    out = []
    i = 0
    while n:
        if n & 1:
            out.append(i)
        n >>= 1
        i += 1
    return out


def eps_of(v):
    return -1 if (sum(v) & 1) else 1


# ============================================ symplectic Pauli monomials / sums

class Q:
    """i^k X^x Z^z on a register of qubits indexed by bit position."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k & 3
        self.x = x
        self.z = z

    def __mul__(a, b):
        return Q(a.k + b.k + 2 * pcnt(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def neg(s):
        return Q(s.k + 2, s.x, s.z)

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0


def qprod(seq):
    o = Q(0, 0, 0)
    for p in seq:
        o = o * p
    return o


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


ONE = (Fr(1), Fr(0))
IMU = (Fr(0), Fr(1))
HALF = (Fr(1, 2), Fr(0))
HALFI = (Fr(0), Fr(1, 2))
PHASE = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1))]


class PS(dict):
    """sum_j c_j X^{x_j} Z^{z_j} with c_j a pair of Fractions: exact."""

    def __add__(a, b):
        o = PS(a)
        for k, v in b.items():
            w = o.get(k)
            if w is None:
                o[k] = v
            else:
                s = (w[0] + v[0], w[1] + v[1])
                if s[0] == 0 and s[1] == 0:
                    del o[k]
                else:
                    o[k] = s
        return o

    def __sub__(a, b):
        return a + b.smul((Fr(-1), Fr(0)))

    def smul(a, s):
        o = PS()
        for k, v in a.items():
            c = cmul(v, s)
            if c[0] or c[1]:
                o[k] = c
        return o

    def __mul__(a, b):
        o = PS()
        for (x1, z1), c1 in a.items():
            for (x2, z2), c2 in b.items():
                c = cmul(c1, c2)
                if pcnt(z1 & x2) & 1:
                    c = (-c[0], -c[1])
                k = (x1 ^ x2, z1 ^ z2)
                w = o.get(k)
                if w is None:
                    o[k] = c
                else:
                    s = (w[0] + c[0], w[1] + c[1])
                    if s[0] == 0 and s[1] == 0:
                        del o[k]
                    else:
                        o[k] = s
        return o

    def iszero(a):
        return len(a) == 0

    def xsupp(a):
        s = 0
        for (x, z) in a:
            s |= x
        return s

    def has_diag(a):
        return any(x == 0 for (x, z) in a)

    def is_pure_z(a):
        return all(x == 0 for (x, z) in a)


def mono(q, c=ONE):
    return PS({(q.x, q.z): cmul(c, PHASE[q.k & 3])})


def zop(z, c=ONE):
    return PS({(0, z): c})


IDP = PS({(0, 0): ONE})


def comm(a, b):
    return a * b - b * a


def conj_mono(c):
    """O -> c O c^{-1} for a Pauli MONOMIAL c: a sign per key."""
    def f(P):
        o = PS()
        for (x, z), co in P.items():
            if (pcnt(c.x & z) + pcnt(c.z & x)) & 1:
                o[(x, z)] = (-co[0], -co[1])
            else:
                o[(x, z)] = co
        return o
    return f


def antiK(P):
    """K P K for a Pauli sum: conjugate the coefficient of every (x, z) key."""
    o = PS()
    for k, c in P.items():
        o[k] = (c[0], -c[1])
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

    def bonds(self):
        return [(v, self.step(v, EX[a]), eta_ks(v, a), a) for (v, a) in self.E]


def Bop(L, v):
    return zop(L.star[v])


def nop(L, v):
    return (IDP - Bop(L, v)).smul(HALF)


def Aop(L, i, j):
    return mono(L.Aij(i, j))


def Top(L, i, j):
    return (Aop(L, i, j) * (Bop(L, i) - Bop(L, j))).smul(HALFI)


def Jop(L, i, j, w):
    return (Aop(L, i, j) * (IDP - Bop(L, i) * Bop(L, j))).smul((Fr(w) / 2, Fr(0)))


def Hhop(L):
    H = PS()
    for (i, j, e, a) in L.bonds():
        H = H + Top(L, i, j).smul((-Fr(e), Fr(0)))
    return H


def Hmass(L):
    H = PS()
    for v in L.V:
        H = H + zop(L.star[v], (Fr(-eps_of(v), 2), Fr(0)))
    return H


def Qop(L):
    o = PS()
    for v in L.V:
        o = o + (nop(L, v) - IDP.smul(HALF))
    return o


# ======================================== point maps and the induced relabelling

class Map:
    """v -> M v + c on the coarse lattice; (M v)_i = s_i v[j_i]."""

    def __init__(self, name, M, c, det):
        self.name = name
        self.M = M
        self.c = tuple(c)
        self.det = det

    def pt(self, L, v):
        w = tuple(self.M[i][1] * v[self.M[i][0]] + self.c[i] for i in range(3))
        if L.per:
            return wrap(w, L.dims)
        return w if all(0 <= w[i] < L.dims[i] for i in range(3)) else None

    def dirimg(self, a):
        for i in range(3):
            if self.M[i][0] == a:
                return i, self.M[i][1]
        raise KeyError


NEG = [(0, -1), (1, -1), (2, -1)]
POS = [(0, 1), (1, 1), (2, 1)]
IDMAP = Map("identity", POS, (0, 0, 0), +1)
INV0 = Map("inversion about a corner", NEG, (0, 0, 0), -1)
INVC = Map("inversion about a cube centre", NEG, (1, 1, 1), -1)
REF0X = Map("reflection x=0", [(0, -1), (1, 1), (2, 1)], (0, 0, 0), -1)
REFHX = Map("reflection x=1/2", [(0, -1), (1, 1), (2, 1)], (1, 0, 0), -1)
REF0Y = Map("reflection y=0", [(0, 1), (1, -1), (2, 1)], (0, 0, 0), -1)
REFHY = Map("reflection y=1/2", [(0, 1), (1, -1), (2, 1)], (0, 1, 0), -1)
REF0Z = Map("reflection z=0", [(0, 1), (1, 1), (2, -1)], (0, 0, 0), -1)
REFHZ = Map("reflection z=1/2", [(0, 1), (1, 1), (2, -1)], (0, 0, 1), -1)
ROTZ = Map("C4 about z (proper)", [(1, -1), (0, 1), (2, 1)], (0, 0, 0), +1)
TRX = Map("translation +x (proper)", POS, (1, 0, 0), +1)

IMPROPER = [INV0, INVC, REF0X, REFHX, REF0Y, REFHY, REF0Z, REFHZ]
MAPS = IMPROPER + [ROTZ, TRX]


def edge_perm(L, mp):
    """Induced permutation of the code qubits, or (None, None)."""
    vm = {}
    for v in L.V:
        w = mp.pt(L, v)
        if w is None:
            return None, None
        vm[v] = w
    if len(set(vm.values())) != L.nv:
        return None, None
    ep = {}
    for (v, a) in L.E:
        b, s = mp.dirimg(a)
        u = vm[v]
        e2 = (u, b) if s > 0 else (L.step(u, tuple(-x for x in EX[b])), b)
        if e2[0] is None or e2 not in L.ei:
            return None, None
        ep[L.ei[(v, a)]] = L.ei[e2]
    if len(set(ep.values())) != L.nq:
        return None, None
    return vm, ep


def permmask(ep, msk):
    o = 0
    for q in bits(msk):
        o |= 1 << ep[q]
    return o


def vperm(ep, q):
    return Q(q.k, permmask(ep, q.x), permmask(ep, q.z))


def cz_conj(N, q):
    """D Q D^-1 for D = prod_{{e,f}: f in N[e]} CZ_{ef}, N symmetric, loop-free."""
    S = bits(q.x)
    zn = 0
    for e in S:
        zn ^= N[e]
    sg = 0
    for a in range(len(S)):
        for b in range(a + 1, len(S)):
            if (N[S[a]] >> S[b]) & 1:
                sg ^= 1
    return Q(q.k + 2 * sg, q.x, q.z ^ zn)


def zw_conj(W, q):
    return Q(q.k + 2 * (pcnt(W & q.x) & 1), q.x, q.z)


class Conj:
    """U_P = G_g . D_CZ . V_P acting by conjugation on monomials and sums."""

    def __init__(self, ep, N, W):
        self.ep = ep
        self.N = N
        self.W = W

    def q(self, p):
        return zw_conj(self.W, cz_conj(self.N, vperm(self.ep, p)))

    def ps(self, P):
        o = PS()
        for (x, z), c in P.items():
            r = self.q(Q(0, x, z))
            cc = cmul(c, PHASE[r.k & 3])
            w = o.get((r.x, r.z))
            if w is None:
                o[(r.x, r.z)] = cc
            else:
                s = (w[0] + cc[0], w[1] + cc[1])
                if s[0] == 0 and s[1] == 0:
                    del o[(r.x, r.z)]
                else:
                    o[(r.x, r.z)] = s
        return o


class Act:
    """A possibly antiunitary symmetry acting by conjugation on Pauli sums."""

    def __init__(self, fn, anti):
        self.fn = fn
        self.anti = anti

    def __call__(self, O):
        return self.fn(O)


def comp(a, b):
    return Act(lambda O: a(b(O)), a.anti ^ b.anti)


def analyze(L, mp):
    """Build U_P = G_g D_CZ V_P and every derived sign, exactly."""
    vm, ep = edge_perm(L, mp)
    if vm is None:
        return None
    N = {q: 0 for q in range(L.nq)}
    s0 = {}
    orient = {}
    badk = 0
    for (v, a) in L.E:
        i, j, e = v, L.step(v, EX[a]), L.ei[(v, a)]
        R = vperm(ep, L.Aij(i, j)) * L.Aij(vm[i], vm[j])
        if R.x != 0 or (R.k & 1):
            badk += 1
        N[ep[e]] = R.z
        s0[e] = 1 if (R.k & 3) == 0 else -1
        orient[e] = 1 if (vm[i] == L.E[ep[e]][0]) else -1
    sym_ok = all(((N[e] >> f) & 1) == ((N[f] >> e) & 1)
                 for e in range(L.nq) for f in bits(N[e]))
    self_ok = all(not ((N[e] >> e) & 1) for e in range(L.nq))
    W = 0
    for (v, a) in L.E:
        e = L.ei[(v, a)]
        (u, c) = L.E[ep[e]]
        if s0[e] * eta_ks(v, a) != eta_ks(u, c):
            W |= 1 << ep[e]
    sigma = {e: s0[e] * (-1 if (W >> ep[e]) & 1 else 1) for e in s0}
    return dict(vm=vm, ep=ep, N=N, s0=s0, W=W, U=Conj(ep, N, W), sigma=sigma,
                orient=orient, sym_ok=sym_ok, self_ok=self_ok, badk=badk,
                nz=sum(1 for e in range(L.nq) if N[e] != 0))


def gauge_corners(L, W):
    """Solve XOR_{v in S} star[v] = W over F2; return S, or None."""
    piv = {}
    for idx, v in enumerate(L.V):
        r, prov = L.star[v], 1 << idx
        while r:
            h = r.bit_length() - 1
            if h in piv:
                r ^= piv[h][0]
                prov ^= piv[h][1]
            else:
                piv[h] = (r, prov)
                break
    w, prov = W, 0
    while w:
        h = w.bit_length() - 1
        if h not in piv:
            return None
        w ^= piv[h][0]
        prov ^= piv[h][1]
    return [L.V[i] for i in range(L.nv) if (prov >> i) & 1]


def cz_neighbourhood_of_inversion(L, q):
    """The three +direction edges at the image edge's upper endpoint together
    with the three -direction edges at its lower endpoint."""
    (u, c) = L.E[q]
    w = L.step(u, EX[c])
    msk = 0
    for a in range(3):
        if (w, a) in L.ei:
            msk |= 1 << L.ei[(w, a)]
        p = L.step(u, tuple(-x for x in EX[a]))
        if p is not None and (p, a) in L.ei:
            msk |= 1 << L.ei[(p, a)]
    return msk


CUBE = Lat((2, 2, 2), False)
TOR = Lat((4, 4, 4), True)

print("H(t,m) = -t sum eta_ij T_ij - (m/2) sum eps_v B_v, open 2x2x2 cube and 4^3 torus. The"
      " Lattice axiom names PROPER rotations only: every P-line is CONDITIONAL.")

# ============================ A -- T1: parity needs a CZ network on the encoding

perm_ok = pureZ_ok = sym_ok = img_ok = sigA_ok = etaeta_ok = True
cut_ok = rec_ok = face_ok = polar_ok = True
auto = {}
zfail = 0
degs = {}
cuts = {}
nrev = {}
nsig = {}
for L, tag in ((CUBE, "cube"), (TOR, "torus")):
    faces = L.faces()
    fidx = {frozenset(f): f for f in faces}
    Sf = {f: mono(L.loop(f)) for f in faces}
    Qch = Qop(L)
    for mp in MAPS:
        r = analyze(L, mp)
        auto[(tag, mp.name)] = r is not None
        if r is None:
            continue
        U, vm, ep = r["U"], r["vm"], r["ep"]
        perm_ok = perm_ok and len(set(ep.values())) == L.nq
        pureZ_ok = pureZ_ok and r["badk"] == 0
        sym_ok = sym_ok and r["sym_ok"] and r["self_ok"]
        if mp in (INV0, INVC) and tag == "torus" and r["nz"] != L.nq:
            zfail += 1
        degs[(tag, mp.name)] = sorted({pcnt(r["N"][e]) for e in range(L.nq)})
        if mp in (INV0, INVC):
            img_ok = img_ok and all(
                r["N"][q] == cz_neighbourhood_of_inversion(L, q) for q in range(L.nq))
        ns = 0
        for (v, a) in L.E:
            i, j, e = v, L.step(v, EX[a]), L.ei[(v, a)]
            tgt = L.Aij(vm[i], vm[j])
            s = r["sigma"][e]
            if not U.q(L.Aij(i, j)) == (tgt if s > 0 else tgt.neg()):
                sigA_ok = False
            if s != eta_ks(v, a) * eta_ks(*L.E[ep[e]]):
                etaeta_ok = False
            ns += (s < 0)
        nsig[(tag, mp.name)] = ns
        g = gauge_corners(L, r["W"])
        cut_ok = cut_ok and g is not None
        cuts[(tag, mp.name)] = len(g) if g is not None else -1
        rec_ok = rec_ok and all(U.ps(Bop(L, v)) == Bop(L, vm[v]) for v in L.V) \
            and (U.ps(Qch) - Qch).iszero()
        for f in faces:
            if not U.q(L.loop(f)) == L.loop(fidx[frozenset(tuple(vm[x] for x in f))]):
                face_ok = False
        nr = 0
        for (v, a) in L.E:
            i, j, e = v, L.step(v, EX[a]), L.ei[(v, a)]
            (u, c) = L.E[ep[e]]
            w = L.step(u, EX[c])
            tg = Jop(L, u, w, eta_ks(u, c)).smul((Fr(r["orient"][e]), Fr(0)))
            if not (U.ps(Jop(L, i, j, eta_ks(v, a))) - tg).iszero():
                polar_ok = False
            nr += (r["orient"][e] < 0)
        nrev[(tag, mp.name)] = nr

nauto = sum(1 for k in auto if auto[k])
check("A1 [exact] %d of the %d point maps are automorphisms of the open cube and all %d of the "
      "torus; each PERMUTES the code qubits"
      % (sum(1 for k in auto if k[0] == "cube" and auto[k]), len(MAPS), len(MAPS)),
      perm_ok and nauto == 14)
check("A2 [exact] inversion shifts the direction order -x<-y<-z<+x<+y<+z by three, so V_P leaves a "
      "PURE Z factor on all %d torus bonds"
      % TOR.nq, pureZ_ok and zfail == 0 and degs[("torus", INV0.name)] == [6])
check("A3 [exact] a Z-Pauli only SIGNS A_e, so no Z product repairs it; the factor is the 3 +edges "
      "above and the 3 -edges below the image edge (degree %s)"
      % (degs[("torus", INV0.name)],), img_ok)
check("A4 [exact] that adjacency is SYMMETRIC and LOOP-FREE for every map, so the diagonal "
      "Clifford D_CZ = prod CZ_ef is legal", sym_ok)
check("A5 [exact] U_P = G_g D_CZ V_P gives U_P A_ij U_P^-1 = sigma_ij A_{P(i)P(j)} with "
      "sigma_ij = eta_ij eta_{P(i)P(j)} on every bond", sigA_ok and etaeta_ok)
check("A6 [exact] the Z-mask of G_g is a CUT, prod_{v in S} B_v with |S| = %d: a Z2 gauge factor, "
      "DIAGONAL in the record basis" % cuts[("torus", INV0.name)],
      cut_ok and cuts[("torus", INV0.name)] == 32 and cuts[("torus", INVC.name)] == 32)
check("A7 [exact] U_P B_v U_P^-1 = +B_{P(v)}, no sign ever (Q -> +Q), and U_P S_f U_P^-1 = "
      "+S_{P(f)}: legal in the pi-flux code space", rec_ok and face_ok)
check("A8 [exact] U_P J_ij U_P^-1 = o_ij J_{P(i)P(j)}: the inversions reverse all %d bonds, the "
      "x-mirrors only %d -- J is POLAR"
      % (nrev[("torus", INV0.name)], nrev[("torus", REFHX.name)]),
      polar_ok and nrev[("torus", INV0.name)] == 192 and nrev[("torus", INVC.name)] == 192
      and nrev[("torus", REFHX.name)] == 64 and nrev[("torus", TRX.name)] == 0)

# ================================ B -- T2: inversion about a corner, shift parity

etainv = {}
for mp in (INV0, INVC, REF0X, REFHX):
    bad = 0
    for (v, a) in TOR.E:
        vm, ep = edge_perm(TOR, mp)
        (u, c) = TOR.E[ep[TOR.ei[(v, a)]]]
        bad += (eta_ks(v, a) != eta_ks(u, c))
    etainv[mp.name] = bad

eps_ok = hh_ok = hm_ok = True
for L in (CUBE, TOR):
    Hh, Hm = Hhop(L), Hmass(L)
    for mp in MAPS:
        r = analyze(L, mp)
        if r is None:
            continue
        s = (-1) ** (sum(mp.c) & 1)
        eps_ok = eps_ok and all(eps_of(r["vm"][v]) == s * eps_of(v) for v in L.V)
        hh_ok = hh_ok and (r["U"].ps(Hh) - Hh).iszero()
        hm_ok = hm_ok and (r["U"].ps(Hm) - Hm.smul((Fr(s), Fr(0)))).iszero()

check("B1 [exact] CORNER inversion: sigma = +1 on all %d bonds; the cube centre -1 on %d and the "
      "x=1/2 mirror on %d"
      % (TOR.nq, nsig[("torus", INVC.name)], nsig[("torus", REFHX.name)]),
      nsig[("torus", INV0.name)] == 0 and nsig[("torus", INVC.name)] == 64
      and nsig[("torus", REFHX.name)] == 128)
check("B2 [exact] corner inversion carries eta to ITSELF bond by bond, %d of %d differing; the "
      "odd-shift maps differ on %d and %d"
      % (etainv[INV0.name], TOR.nq, etainv[INVC.name], etainv[REFHX.name]),
      etainv[INV0.name] == 0 and etainv[REF0X.name] == 0 and etainv[INVC.name] > 0
      and etainv[REFHX.name] > 0)
check("B3 [exact] U_P H_hop U_P^-1 = H_hop EXACTLY for every map on both geometries", hh_ok)
check("B4 [exact] eps_{P(v)} = (-1)^{sum c} eps_v at every corner: the rule depends only on the "
      "SHIFT parity", eps_ok)
check("B5 [exact] so H(t,m) is EXACTLY P-symmetric at every t and m about a corner, and only with "
      "m -> -m about a cube centre", hm_ok)

# ==================================================== C -- T3: time reversal

realA_ok = kanti_ok = ze_ok = uniq_ok = True
ta_ok = tb_ok = tt_ok = ts_ok = th_ok = tj_ok = tq_ok = True
for L in (CUBE, TOR):
    FULL = (1 << L.nq) - 1
    ZEc = Conj({q: q for q in range(L.nq)}, {q: 0 for q in range(L.nq)}, FULL)
    Tact = Act(lambda O, Z=ZEc: Z.ps(antiK(O)), True)
    Hh, Hm, Qch = Hhop(L), Hmass(L), Qop(L)
    Hf = Hh + Hm
    zm = 0
    for v in L.V:
        if eps_of(v) < 0:
            zm ^= L.star[v]
    ze_ok = ze_ok and zm == FULL
    xs = set()
    for (i, j, e, a) in L.bonds():
        A, Tb, J = Aop(L, i, j), Top(L, i, j), Jop(L, i, j, e)
        realA_ok = realA_ok and antiK(A) == A
        kanti_ok = kanti_ok and (antiK(Tb) + Tb).iszero()
        xs.add(A.xsupp())
        ta_ok = ta_ok and (Tact(A) + A).iszero()
        tt_ok = tt_ok and (Tact(Tb) - Tb).iszero()
        tj_ok = tj_ok and (Tact(J) + J).iszero()
    uniq_ok = uniq_ok and xs == {1 << q for q in range(L.nq)}
    kanti_ok = kanti_ok and (antiK(Hh) + Hh).iszero()
    tb_ok = tb_ok and all(Tact(Bop(L, v)) == Bop(L, v) for v in L.V)
    ts_ok = ts_ok and all(Tact(mono(L.loop(f))) == mono(L.loop(f)) for f in L.faces())
    th_ok = th_ok and (Tact(Hh) - Hh).iszero() and (Tact(Hm) - Hm).iszero() \
        and (Tact(Hf) - Hf).iszero()
    tq_ok = tq_ok and (Tact(Qch) - Qch).iszero()

check("C1 [exact] every A_ij is REAL, so K A_ij K = +A_ij and K H_hop K = -H_hop: bare conjugation "
      "is an ANTI-symmetry of the hop", realA_ok and kanti_ok)
check("C2 [exact] Z_E = prod_e Z_e = prod over the corners with eps_v = -1 of B_v: bipartite, so "
      "every edge is covered once", ze_ok)
check("C3 [exact] Z_E is the UNIQUE pure-Z choice: A_ij has X-support exactly its own edge and the "
      "bond-to-edge map is onto", uniq_ok)
check("C4 [exact] T = Z_E K: A_ij -> -A_ij, B_v -> +B_v (records T-EVEN), T_ij -> +T_ij, "
      "S_f -> +S_f -- the code space is T-invariant",
      ta_ok and tb_ok and tt_ok and ts_ok)
check("C5 [exact] T H(t,m) T^-1 = H(t,m) for EVERY t and EVERY m: time reversal is exact at every "
      "mass, with no m -> -m", th_ok)
check("C6 [exact] T J_ij T^-1 = -J_ij on every bond (the current is T-ODD) and T Q T^-1 = +Q",
      tj_ok and tq_ok)

# dense many-body confirmation on the 4096-dimensional cube space
L = CUBE
D = 1 << L.nq
col = np.arange(D, dtype=np.int64)


def popcount(a):
    a = a.copy()
    c = np.zeros_like(a)
    while a.any():
        c += a & 1
        a >>= 1
    return c


def pmat(q, coef=1.0):
    ph = [1, 1j, -1, -1j][q.k & 3]
    dat = ((-1.0) ** (popcount(col & q.z) & 1)).astype(complex) * (ph * coef)
    return sp.csr_matrix((dat, (col ^ q.x, col)), shape=(D, D))


IM = sp.identity(D, format="csr", dtype=complex)
ZEm = pmat(Q(0, 0, D - 1))
ZEd = np.real(ZEm.diagonal())
Pc = IM
for f in L.faces():
    Pc = Pc @ ((IM + pmat(L.loop(f))) * 0.5)
rank = float(np.real(Pc.diagonal().sum()))
imP = float(np.abs(Pc.data.imag).max())
cmP = abs(ZEm @ Pc - Pc @ ZEm)
dcm = float(cmP.data.max()) if cmP.nnz else 0.0
DZ = sp.diags(ZEd).tocsr()


def Ham(m):
    H = sp.csr_matrix((D, D), dtype=complex)
    for (i, j, e, a) in L.bonds():
        H = H + (pmat(L.Aij(i, j)) @ (pmat(Q(0, 0, L.star[i])) - pmat(Q(0, 0, L.star[j])))) \
            * (0.5j * (-1.0) * e)
    for v in L.V:
        H = H + pmat(Q(0, 0, L.star[v])) * (-0.5 * m * eps_of(v))
    return H


dh = 0.0
for m in (0.0, 0.7):
    Hs = Ham(m)
    R = DZ @ Hs.conj() @ DZ - Hs
    dh = max(dh, float(np.abs(R.data).max()) if R.nnz else 0.0)
check("C7 [1e-12] Z_E is a real diagonal involution (T^2 = +I); the %d-dim space's code projector "
      "is real of rank %d and commutes with it; T H T^-1 = H (%.0e)"
      % (D, int(round(rank)), dh),
      float(np.abs(ZEd * ZEd - 1).max()) == 0.0 and imP < TOL
      and abs(rank - 128) < 1e-8 and dcm < TOL and dh < TOL)

# ============================================= D -- T4: the Dirac point, 8 x 8

I2 = np.eye(2)
Xp = np.array([[0, 1], [1, 0]], complex)
Yp = np.array([[0, -1j], [1j, 0]])
Zp = np.diag([1, -1]).astype(complex)


def kr(*a):
    o = np.array([[1.0 + 0j]])
    for m in a:
        o = np.kron(o, m)
    return o


GAM = [kr(Yp, I2, I2), kr(Zp, Yp, I2), kr(Zp, Zp, Yp)]
XI = [kr(Xp, I2, I2), kr(Zp, Xp, I2), kr(Zp, Zp, Xp)]
EPSC = kr(Zp, Zp, Zp).real

V = TOR.V
iv = {v: k for k, v in enumerate(V)}
n1 = TOR.nv
h0 = np.zeros((n1, n1))
for (v, a) in TOR.E:
    w = TOR.step(v, EX[a])
    e = eta_ks(v, a)
    h0[iv[v], iv[w]] += -e
    h0[iv[w], iv[v]] += -e
Eps = np.diag([float(eps_of(v)) for v in V])
acom = float(np.abs(h0 @ Eps + Eps @ h0).max())
ev = np.linalg.eigvalsh(h0)
nz = int((np.abs(ev) < 1e-9).sum())
gaps = []
for m in (0.2, 0.5, 1.0):
    e2 = np.linalg.eigvalsh(h0 + m * Eps)
    gaps.append(abs(e2[e2 > 0].min() - e2[e2 < 0].max() - 2 * m))
check("D1 [1e-12] the 4^3 one-particle operator is real symmetric with {h_0, Eps} = 0 (%.1e) and "
      "EXACTLY %d zero modes gapped to exactly 2m (%.0e)"
      % (acom, nz, max(gaps)), acom < TOL and nz == 8 and max(gaps) < 1e-10)

Vb = np.zeros((n1, 8))
for v in V:
    s = tuple(c % 2 for c in v)
    Vb[iv[v], 4 * s[0] + 2 * s[1] + s[2]] = (-1.0) ** sum(c // 2 for c in v)
Vb /= np.sqrt(8.0)
dker = float(np.abs(h0 @ Vb).max())
dorth = float(np.abs(Vb.T @ Vb - np.eye(8)).max())
qD = (np.pi, np.pi, np.pi)
dbl = float(np.abs(sum((1 + np.cos(qD[a])) * XI[a] + np.sin(qD[a]) * GAM[a]
                       for a in range(3))).max())


def red(O):
    return Vb.T @ (O @ Vb)


CHI = np.real(-1j * (-GAM[0]) @ (-GAM[1]) @ (-GAM[2]))
Er = red(Eps)
check("D2 [1e-12] the cell basis psi_s(v) = (-1)^{sum(v div 2)} delta_{v mod 2, s} is an orthonormal "
      "REAL kernel basis and the q = (pi,pi,pi) block (%.0e)" % (dbl,),
      dker < TOL and dorth < TOL and dbl < TOL)
check("D3 [1e-12] the chirality X = -(Y x X x Y) has spectrum {+1 x4, -1 x4}: 2 right- and 2 "
      "left-handed doublets; the mass eps = Z1 Z2 Z3 ANTIcommutes (%.0e)"
      % float(np.abs(Er - EPSC).max()),
      float(np.abs(CHI @ CHI - np.eye(8)).max()) < TOL
      and sorted(np.round(np.linalg.eigvalsh(CHI), 9).tolist()) == [-1.0] * 4 + [1.0] * 4
      and float(np.abs(Er - EPSC).max()) < TOL
      and float(np.abs(Er @ CHI + CHI @ Er).max()) < TOL)


def one_particle_U(mp):
    vm = {v: mp.pt(TOR, v) for v in V}
    inv = {w: v for v, w in vm.items()}
    g = {V[0]: 1}
    stack = [V[0]]
    while stack:
        v = stack.pop()
        for r in range(6):
            w = TOR.inc[v][r][0]
            if w in g:
                continue
            rr = h0[iv[inv[v]], iv[inv[w]]] * h0[iv[v], iv[w]]
            g[w] = int(np.sign(rr) * g[v])
            stack.append(w)
    U = np.zeros((n1, n1))
    for w in V:
        U[iv[vm[w]], iv[w]] = g[vm[w]]
    return U, sum(1 for v in V if g[v] < 0)


DMAPS = [("corner inversion", INV0), ("cube-centre inversion", INVC),
         ("reflection x=0", REF0X), ("reflection x=1/2", REFHX), ("C4 about z", ROTZ)]
reps = {}
d1p = 0.0
gcnt = {}
for nm, mp in DMAPS:
    U, ng = one_particle_U(mp)
    s = (-1) ** (sum(mp.c) & 1)
    d1p = max(d1p, float(np.abs(U @ h0 @ U.T - h0).max()),
              float(np.abs(U @ Eps @ U.T - s * Eps).max()))
    reps[nm] = red(U)
    gcnt[nm] = ng
check("D4 [1e-12] one-particle: U h_0 U^T = h_0 and U Eps U^T = (-1)^{sum c} Eps (%.1e); %d "
      "flipped corners at a corner, %d at a cube centre"
      % (d1p, gcnt["corner inversion"], gcnt["cube-centre inversion"]),
      d1p < TOL and gcnt["corner inversion"] == 0 and gcnt["cube-centre inversion"] == 32)
Pc0 = reps["corner inversion"]
check("D5 [1e-12] CORNER inversion IS the staggered-mass matrix eps = Z1 Z2 Z3 (%.1e): the "
      "emergent gamma^0, ANTIcommuting with the chirality"
      % float(np.abs(Pc0 - EPSC).max()),
      float(np.abs(Pc0 - EPSC).max()) < TOL
      and float(np.abs(Pc0 @ CHI + CHI @ Pc0).max()) < TOL)

Cm, Tm = Er.copy(), np.eye(8)


def mulop(a, b):
    (A, aa), (B, ab) = a, b
    return (A @ (B.conj() if aa else B), aa ^ ab)


def sq(op):
    M, aa = op
    return M @ (M.conj() if aa else M)


sqs = {}
spectral_products = {}
for nm, _ in DMAPS:
    o = {"C": (Cm, True), "P": (reps[nm], False), "T": (Tm, True)}
    o["CP"] = mulop(o["C"], o["P"])
    o["PT"] = mulop(o["P"], o["T"])
    o["CPT"] = mulop(o["C"], o["PT"])
    spectral_products[nm] = o
    for k in ("C", "T", "P", "CP", "PT", "CPT"):
        M = sq(o[k])
        v = M[0, 0].real
        v = round(v) if abs(v - round(v)) < 1e-9 else v
        sqs[(nm, k)] = float(v) if np.abs(M - M[0, 0] * np.eye(8)).max() < 1e-10 else 0.0
    if nm == "corner inversion":
        cpt = o["CPT"]
mass_domains = []
for mu in (0.0, 0.7):
    hm = h0 + mu * Eps
    mass_domains.append((float(np.max(abs(Eps @ hm.conj() @ Eps + (h0 - mu * Eps)))),
                         float(np.max(abs(Eps @ hm @ Eps + hm - 2 * mu * Eps))),
                         float(np.max(abs(Eps @ hm @ Eps + hm)))))
check("D6 [1e-12] spectral BDI at m=0 only: T = K with T^2 = +1, C = Eps.K with C^2 = +1, chiral S = CT = Eps; no "
      "Kramers sign from T alone",
      float(np.abs(Tm - np.eye(8)).max()) < TOL
      and float(np.abs(Cm @ Cm.conj() - np.eye(8)).max()) < TOL
      and sqs[("corner inversion", "T")] == 1.0 and sqs[("corner inversion", "C")] == 1.0
      and all(a < TOL and b < TOL for a, b, _ in mass_domains)
      and mass_domains[0][2] < TOL and abs(mass_domains[1][2] - 1.4) < TOL)
Mc, ac = cpt
expected_improper = {"corner inversion", "cube-centre inversion", "reflection x=0", "reflection x=1/2"}
actual_improper = {nm for nm, mp in DMAPS if mp.det == -1}
scalar_products = []
scalar_flags_ok = True
for nm in actual_improper:
    product, anti = spectral_products[nm]["CPT"]
    scalar_flags_ok = scalar_flags_ok and not anti
    scalar = np.trace(product) / 8
    if np.max(abs(product - scalar * np.eye(8))) < 1e-10:
        scalar_products.append(nm)
check("D7 [1e-10] CPT from corner inversion is +1 times the IDENTITY on the Dirac point (%.1e); "
      "no other of the four listed improper restrictions gives a scalar" % float(np.abs(Mc - np.eye(8)).max()),
      not ac and float(np.abs(Mc - np.eye(8)).max()) < 1e-10
      and actual_improper == expected_improper and len(DMAPS) == 5
      and scalar_flags_ok and scalar_products == ["corner inversion"]
      and {nm for nm, mp in DMAPS if mp.det == 1} == {"C4 about z"})
check("D8 [1e-10] half-cell negative squares (all m), with Hamiltonian domains checked separately: "
      "(PT)^2 = %+.0f (cube centre), (CP)^2 = %+.0f (x=1/2), %+.0f/%+.0f at a corner"
      % (sqs[("cube-centre inversion", "PT")], sqs[("reflection x=1/2", "CP")],
         sqs[("corner inversion", "PT")], sqs[("corner inversion", "CP")]),
      sqs[("cube-centre inversion", "PT")] == -1.0 and sqs[("reflection x=1/2", "CP")] == -1.0
      and sqs[("corner inversion", "PT")] == 1.0 and sqs[("corner inversion", "CP")] == 1.0)

# ================================================= E -- T5: the full table

L = TOR
FULL = (1 << L.nq) - 1
ZEc = Conj({q: q for q in range(L.nq)}, {q: 0 for q in range(L.nq)}, FULL)
Tact = Act(lambda O: ZEc.ps(antiK(O)), True)
Mmatch = [(v, L.step(v, EX[0])) for v in L.V if v[0] % 2 == 0]
Cq = Q(0, 0, FULL) * qprod([L.Aij(i, j) for (i, j) in Mmatch])
Cact = Act(conj_mono(Cq), False)
rA, rB, rR = analyze(L, INV0), analyze(L, INVC), analyze(L, REFHX)
Pa, Pb, Pr = Act(rA["U"].ps, False), Act(rB["U"].ps, False), Act(rR["U"].ps, False)
COLS = [("C", Cact, IDMAP), ("Pcor", Pa, INV0), ("Pcen", Pb, INVC), ("Ref", Pr, REFHX),
        ("T", Tact, IDMAP), ("CP", comp(Cact, Pa), INV0), ("CT", comp(Cact, Tact), IDMAP),
        ("PT", comp(Pa, Tact), INV0), ("CPT", comp(Cact, comp(Pa, Tact)), INV0)]
Hh, Hm, Qch = Hhop(L), Hmass(L), Qop(L)
faces = L.faces()
fidx = {frozenset(f): f for f in faces}


def sgn(A, B):
    if (A - B).iszero():
        return 1
    if (A + B).iszero():
        return -1
    return 0


def uniq(s):
    return list(s)[0] if len(s) == 1 else 0


tab = {}
nozero_ok = True
mix_ok = True
for name, act, mp in COLS:
    vm = {v: mp.pt(L, v) for v in L.V}
    raw = {}
    raw["B_v"] = {sgn(act(Bop(L, v)), Bop(L, vm[v])) for v in L.V}
    raw["A_ij"] = {sgn(act(Aop(L, i, j)), Aop(L, vm[i], vm[j])) for (i, j, e, a) in L.bonds()}
    raw["S_f"] = {sgn(act(mono(L.loop(f))),
                      mono(L.loop(fidx[frozenset(tuple(vm[x] for x in f))]))) for f in faces}
    raw["T_ij"] = {sgn(act(Top(L, i, j)), Top(L, vm[i], vm[j])) for (i, j, e, a) in L.bonds()}
    raw["J_ij"] = {sgn(act(Jop(L, i, j, e)), Jop(L, vm[i], vm[j], e))
                   for (i, j, e, a) in L.bonds()}
    raw["eps_v"] = {eps_of(vm[v]) * eps_of(v) for v in L.V}
    nozero_ok = nozero_ok and all(0 not in st for st in raw.values())
    c = {k: uniq(st) for k, st in raw.items()}
    c["H_hop"] = sgn(act(Hh), Hh)
    c["H_m"] = sgn(act(Hm), Hm)
    c["Q"] = sgn(act(Qch), Qch)
    c["n_v"] = "n_P" if c["B_v"] == 1 else "1-nP"
    c["H(t,m)"] = "inv" if (c["H_hop"] == 1 and c["H_m"] == 1) else (
        "-m" if (c["H_hop"] == 1 and c["H_m"] == -1) else "??")
    tab[name] = c
for name in ("Pcen", "Ref"):
    vm = {v: (INVC if name == "Pcen" else REFHX).pt(L, v) for v in L.V}
    act = Pb if name == "Pcen" else Pr
    r = rB if name == "Pcen" else rR
    for (v, a) in L.E:
        i, j, e = v, L.step(v, EX[a]), L.ei[(v, a)]
        if sgn(act(Aop(L, i, j)), Aop(L, vm[i], vm[j])) != r["sigma"][e]:
            mix_ok = False

ORD = ["B_v", "n_v", "A_ij", "S_f", "T_ij", "H_hop", "H_m", "H(t,m)", "J_ij", "Q", "eps_v"]


def fmt(v):
    if isinstance(v, str):
        return v
    return "e.e'" if v == 0 else "%+d" % v


print("TABLE, 4^3 torus. Pcor/Pcen = corner/cube-centre inversion, Ref = the x=1/2 mid-plane;"
      " CP, PT, CPT use Pcor; e.e' = sigma_ij = eta_ij eta_{P(i)P(j)}; -m = m -> -m.")
print(("%-7s" % "" + "".join("%-5s" % n for n, _, _ in COLS)).rstrip())
for k in ORD:
    print(("%-7s" % k + "".join("%-5s" % fmt(tab[n][k]) for n, _, _ in COLS)).rstrip())

uni = all(isinstance(tab[n][k], int) and tab[n][k] != 0
          for n, _, _ in COLS for k in ("B_v", "S_f", "H_hop", "H_m", "Q", "eps_v"))
mixcols = [n for n, _, _ in COLS if tab[n]["A_ij"] == 0]
check("E1 [exact] every entry is a sign on the SAME operator at the image index; B_v, S_f, H_hop, "
      "H_m, Q and eps_v are uniform in every column", uni and nozero_ok)
check("E2 [exact] the odd-shift columns %s carry sigma_ij = eta_ij eta_{P(i)P(j)} on A_ij, T_ij "
      "and J_ij, at -1 on %d of %d bonds and on %d"
      % (", ".join(mixcols), nsig[("torus", INVC.name)], TOR.nq, nsig[("torus", REFHX.name)]),
      mixcols == ["Pcen", "Ref"] and mix_ok
      and all(tab[n][k] == 0 for n in mixcols for k in ("A_ij", "T_ij", "J_ij")))
check("E3 [exact] H(t,m) is INVARIANT under Pcor, T and PT and goes to H(t,-m) under C, Pcen, "
      "Ref, CP, CT and CPT; mass-flipping maps are not fixed-m symmetries",
      [tab[n]["H(t,m)"] for n, _, _ in COLS]
      == ["-m", "inv", "-m", "-m", "inv", "-m", "-m", "inv", "-m"])
check("E4 [exact] S_f -> +S_f in every column: each operation carries the code space to itself "
      "with no sign; the encoding obstructs none",
      all(tab[n]["S_f"] == 1 for n, _, _ in COLS))

recd_ok = corr_ok = True
for Lx in (CUBE, TOR):
    for O in (Qop(Lx), Hmass(Lx)) + tuple(Bop(Lx, v) for v in Lx.V):
        recd_ok = recd_ok and O.is_pure_z()
    for (i, j, e, a) in Lx.bonds():
        for O in (Aop(Lx, i, j), Top(Lx, i, j), Jop(Lx, i, j, e)):
            corr_ok = corr_ok and not O.has_diag()
    for f in Lx.faces():
        corr_ok = corr_ok and not mono(Lx.loop(f)).has_diag()
check("E5 [exact] B_v, Q and H_m are pure Z, so record-diagonal, carrying the table's signs; "
      "A_ij, S_f, T_ij, J_ij have zero fixed-Z diagonal; this supplies no off-diagonal measurement",
      recd_ok and corr_ok)

# Post-review controls leave every original numerical sequence and check ID intact.
negative_gaps = []
for mu in (-0.2, -0.5, -1.0):
    vals = np.linalg.eigvalsh(h0 + mu * Eps)
    negative_gaps.append(abs(vals[vals > 0].min() - vals[vals < 0].max() - 2 * abs(mu)))
check("R1 [1e-10] negative-m gaps are 2|m|; spectral particle-hole at fixed m fails by 2|m|",
      max(negative_gaps) < 1e-10 and abs(mass_domains[1][2] - 1.4) < TOL)
odd_rows = []
for nm, mp in (("cube-centre PT", INVC), ("x-half C_spec P", REFHX)):
    u, _ = one_particle_U(mp)
    a = u if mp is INVC else Eps @ u
    for mu in (0.0, 0.7):
        hm = h0 + mu * Eps
        out = a @ hm.conj() @ a.conj().T
        square_error = float(np.max(abs(a @ a.conj() + np.eye(n1))))
        commute_error = float(np.max(abs(out - hm)))
        anticommute_error = float(np.max(abs(out + hm)))
        odd_rows.append((nm, mu, square_error, commute_error, anticommute_error))
check("R2 [1e-12] cube-centre PT commutes only at m0; x-half C_spec P anticommutes all tested m; both square -I",
      all(r[2] < TOL for r in odd_rows)
      and odd_rows[0][3] < TOL and abs(odd_rows[1][3] - 1.4) < TOL
      and all(r[4] < TOL for r in odd_rows[2:]))
plus = np.array([1., 1.]) / np.sqrt(2)
minus = np.array([1., -1.]) / np.sqrt(2)
check("R3 [1e-12] identical complete Z laws have opposite X expectations; fixed-Z correlations do not determine X",
      np.max(abs(abs(plus)**2 - abs(minus)**2)) < TOL
      and abs(np.vdot(plus, Xp @ plus) - 1) < TOL
      and abs(np.vdot(minus, Xp @ minus) + 1) < TOL)
odd_many_body = [comp(Cact, Pb), comp(Cact, Pr)]
check("R4 [exact] unitary many-body C times either odd-shift parity preserves both hop and mass",
      all(not a.anti and (a(Hh)-Hh).iszero() and (a(Hm)-Hm).iszero() for a in odd_many_body))
print("DOMAIN_DATA:", mass_domains, odd_rows, "scalar choices", scalar_products)
print("SUMMARY: conditional finite corner P and encoded T preserve all masses; specified spectral BDI is massless; many-body CPT flips m. Fixed-Z diagonality does not supply physical Records.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
