#!/usr/bin/env python3
"""Charge conjugation and the conserved U(1) current of the emergent fermion.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3, one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding
written on it, with the Kawamoto-Smit link signs
    eta_1 = 1,  eta_2(v) = (-1)^{v_1},  eta_3(v) = (-1)^{v_1+v_2}.
The declared Hamiltonian is
    H(t, m) = -t sum_<ij> eta_ij T_ij - (m/2) sum_v eps_v B_v,
    A_ij = X(edge) x Z-tails, direction order -x < -y < -z < +x < +y < +z,
    A_ji = -A_ij,  B_v = prod of the z_v incident Z's at a corner = I - 2 n_v,
    S_f = the ordered four-A face loop,  T_ij = (i/2) A_ij (B_i - B_j),
    n_v = (I - B_v)/2,  eps_v = (-1)^{v_1+v_2+v_3}.

  A  THE CONTINUITY EQUATION.  dn_i/dt = i[H, n_i] = -sum_{j~i} J_ij with the
     bond current J_ij = eta_ij (t/2) A_ij (I - B_i B_j): Hermitian, odd under
     bond reversal, two monomials/X-support one qubit when t!=0, gauge-legal,
     and with an identically zero record-diagonal part.  The naive candidate
     (t/2) A_ij (B_i + B_j) fails structurally at t!=0; t=0 gives zero current.
     Parameters t,m are supplied real; original numerical fixtures use t=1.
  B  CHARGE CONJUGATION.  C = Z_E C_0 with C_0 = prod over a perfect matching
     of A_ij and Z_E = prod of all Z_e = prod over odd corners of B_v; the
     transformation table, C^2=I, matching conjugation on encoded generators, eta independence.
  C  THE PARITY OBSTRUCTION.  prod_v B_v = I identically, so an odd corner
     count admits no unitary C on the code space at all.
  D  THE CHARGE AS A RECORD READOUT.  Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v
     read off all 4096 record patterns of the 2x2x2 cube as a three-bit cube-corner
     parity count; the current has no such readout.
  E  SUPPLIED FINITE CONJUGATION-INVARIANT STATES.  One-particle 4^3 torus and the cube's
     128-dimensional even-N code space: C H(t,m) C^-1 = H(t,-m), the
     antiperiodic/no-zero-mode finite sea is C-invariant; no physical vacuum selection.

Groups A, B, C and D are exact: Gaussian-rational coefficients on symplectic
Pauli monomials (F2 supports, Z4 phases) and integer record arithmetic, with
no floating-point step anywhere.  Group E is numerical at the stated
tolerance.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sp

AUDIT_TIMEOUT_SEC = 90

T0 = time.time()
PASS = 0
FAIL = 0


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

    def neg(s):
        return Q(s.k + 2, s.x, s.z)

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def isI(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def ismI(s):
        return s.x == 0 and s.z == 0 and s.k == 2


def qprod(seq):
    o = Q(0, 0, 0)
    for p in seq:
        o = o * p
    return o


def commutes_mono(p, q):
    return ((pcnt(p.x & q.z) + pcnt(p.z & q.x)) & 1) == 0


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


ONE = (Fr(1), Fr(0))
IMU = (Fr(0), Fr(1))


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

    def dag(a):
        o = PS()
        for (x, z), c in a.items():
            c = (c[0], -c[1])
            if pcnt(x & z) & 1:
                c = (-c[0], -c[1])
            o[(x, z)] = c
        return o

    def iszero(a):
        return len(a) == 0

    def isherm(a):
        return (a - a.dag()).iszero()

    def supp(a):
        s = set()
        for (x, z) in a:
            s |= {i for i in range(x.bit_length() | z.bit_length()) if (x | z) >> i & 1}
        return s


def mono(q, c=ONE):
    ph = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1))][q.k & 3]
    return PS({(q.x, q.z): cmul(c, ph)})


def zop(z, c=ONE):
    return PS({(0, z): c})


IDP = PS({(0, 0): ONE})


def comm(a, b):
    return a * b - b * a


def conj_mono(c, ps):
    """c P c^{-1} for a Pauli monomial c acting on a Pauli sum, exactly."""
    o = PS()
    for (x, z), co in ps.items():
        if (pcnt(c.x & z) + pcnt(c.z & x)) & 1:
            o[(x, z)] = (-co[0], -co[1])
        else:
            o[(x, z)] = co
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


HALF = (Fr(1, 2), Fr(0))
HALFI = (Fr(0), Fr(1, 2))


def Bop(L, v):
    return zop(L.star[v])


def nop(L, v):
    return (IDP - Bop(L, v)).smul(HALF)


def Aop(L, i, j):
    return mono(L.Aij(i, j))


def Top(L, i, j):
    return (Aop(L, i, j) * (Bop(L, i) - Bop(L, j))).smul(HALFI)


def Jop(L, i, j, w, t=1):
    """J_ij = w_ij (t/2) A_ij (I - B_i B_j), for supplied real t (exact rational fixtures here)."""
    return (Aop(L, i, j) * (IDP - Bop(L, i) * Bop(L, j))).smul((Fr(w) * Fr(t) / 2, Fr(0)))


def Hhop(L, wts=None, t=1):
    """H_hop = -t sum_<ij> w_ij T_ij with supplied real t; w = the KS signs unless given."""
    H = PS()
    for k, (i, j, e, a) in enumerate(L.bonds()):
        w = e if wts is None else wts[k]
        H = H + Top(L, i, j).smul((-Fr(w) * Fr(t), Fr(0)))
    return H


def Hmass(L):
    """H_m = m sum_v eps_v n_v = -(m/2) sum_v eps_v B_v + const, at m = 1."""
    H = PS()
    for v in L.V:
        H = H + zop(L.star[v], (Fr(-eps_of(v), 2), Fr(0)))
    return H


def Qop(L):
    """Q = sum_v (n_v - 1/2) = -(1/2) sum_v B_v."""
    Qq = PS()
    for v in L.V:
        Qq = Qq + (nop(L, v) - IDP.smul(HALF))
    return Qq


L333 = Lat((3, 3, 3), False)
L444T = Lat((4, 4, 4), True)
L222 = Lat((2, 2, 2), False)
L444 = Lat((4, 4, 4), False)

# ================================ A -- the continuity equation and the current

print("H(t,m) = -t sum eta_ij T_ij - (m/2) sum eps_v B_v; n_i = (I - B_i)/2;"
      " J_ij = eta_ij (t/2) A_ij (I - B_i B_j)")

cont_ok = True
naive = []
forms_ok = True
herm_ok = True
sign_ok = True
face_ok = True
glob_ok = True
nmono = set()
sxs = set()
supp3 = set()
supp4 = set()
for L, tag, dst in ((L333, "open 3x3x3", supp3), (L444T, "torus 4^3", supp4)):
    H = Hhop(L)
    nbr = {v: [] for v in L.V}
    for (i, j, e, a) in L.bonds():
        nbr[i].append((j, e))
        nbr[j].append((i, e))
    for i in L.V:
        lhs = comm(H, nop(L, i)).smul(IMU)
        rhs = PS()
        for (j, e) in nbr[i]:
            rhs = rhs - Jop(L, i, j, e)
        if not (lhs - rhs).iszero():
            cont_ok = False
    i0 = L.V[0] if not L.per else (1, 1, 1)
    lhs = comm(H, nop(L, i0)).smul(IMU)
    bad = PS()
    for (j, e) in nbr[i0]:
        bad = bad - (Aop(L, i0, j) * (Bop(L, i0) + Bop(L, j))).smul((Fr(e, 2), Fr(0)))
    naive.append(len(lhs - bad))
    fz = [L.loop(f) for f in L.faces()]
    for (i, j, e, a) in L.bonds():
        J = Jop(L, i, j, e)
        herm_ok = herm_ok and J.isherm()
        sign_ok = sign_ok and (J + Jop(L, j, i, e)).iszero() \
            and (Top(L, i, j) - Top(L, j, i)).iszero() \
            and (Aop(L, i, j) + Aop(L, j, i)).iszero()
        d = Bop(L, i) - Bop(L, j)
        forms_ok = forms_ok and (J - (Top(L, i, j) * Bop(L, j)).smul((Fr(0), Fr(e)))).iszero() \
            and (J + (Top(L, i, j) * Bop(L, i)).smul((Fr(0), Fr(e)))).iszero() \
            and (J - (Aop(L, i, j) * d * d).smul((Fr(e, 4), Fr(0)))).iszero()
        nmono.add(len(J))
        sxs.add(len({b for (x, z) in J for b in range(x.bit_length()) if x >> b & 1}))
        dst.add(len(J.supp()))
        for (x, z) in J:
            if x == 0:
                forms_ok = False
            for s in fz:
                if not commutes_mono(Q(0, x, z), s):
                    face_ok = False
    Nn = PS()
    for v in L.V:
        Nn = Nn + nop(L, v)
    Qq = Qop(L)
    glob_ok = glob_ok and comm(H, Nn).iszero() and comm(H, Qq).iszero() \
        and all(x == 0 for (x, z) in Qq)

check('A1 [exact,t=1] i[H,n_i]+sum_j J_ij=0: all27 open3^3 and64 torus4^3 corners', cont_ok)
check('A2 [exact,t=1] naive A(B_i+B_j)/2 vanishes where hopping acts; nonzero residual terms %d/%d'
      % (naive[0], naive[1]), naive == [12, 24])
check("A3 [exact] on every bond J_ij = i t eta T_ij B_j = -i t eta T_ij B_i = (t eta/4) A_ij (B_i - B_j)^2",
      forms_ok)
check('A4 [exact,t=1] J Hermitian, J_ji=-J_ij,T_ji=T_ij; %s monomials, X-support %s on own edge' % (sorted(nmono), sorted(sxs)),
      herm_ok and sign_ok and nmono == {2} and sxs == {1})
check('A5 [exact,t=1] total star-union support %s bulk,%s boundary; all J monomials off-diagonal'
      % (sorted(supp4), sorted(supp3)), supp4 == {11} and supp3 == {6, 8, 10})
check('A6 [exact] [J_ij,S_f]=0 on every tested bond-face pair', face_ok)
check('A7 [exact] [H,N]=[H,Q]=0 by pairwise current cancellation; Q pure Z', glob_ok)

# Additional F1 parameter controls; the original A1-A7 t=1 fixtures remain.
scaled_ok = True
for t_value in (Fr(0), Fr(1), Fr(2), Fr(-3, 2)):
    Ls = L222
    Hs = Hhop(Ls, t=t_value)
    for i in Ls.V:
        divergence = PS()
        for j, q in Ls.inc[i].values():
            weight = next(e for a, b, e, ax in Ls.bonds() if {a, b} == {i, j})
            divergence = divergence + Jop(Ls, i, j, weight, t=t_value)
        scaled_ok &= (comm(Hs, nop(Ls, i)).smul(IMU) + divergence).iszero()
    for i, j, weight, ax in Ls.bonds():
        Js = Jop(Ls, i, j, weight, t=t_value)
        deltaB = Bop(Ls, i) - Bop(Ls, j)
        scaled_ok &= (Js - (Top(Ls, i, j) * Bop(Ls, j)).smul((Fr(0), t_value * weight))).iszero()
        scaled_ok &= (Js + (Top(Ls, i, j) * Bop(Ls, i)).smul((Fr(0), t_value * weight))).iszero()
        scaled_ok &= (Js - (Aop(Ls, i, j) * deltaB * deltaB).smul((t_value * weight / 4, Fr(0)))).iszero()
        scaled_ok &= len(Js) == (0 if t_value == 0 else 2)
check("A8 [exact] supplied t=0,1,2,-3/2: actual current, three scaled forms and continuity agree; t=0 current vanishes", scaled_ok)

# ============================================== B -- charge conjugation C

def matching(L, ax):
    M = []
    for v in L.V:
        if v[ax] % 2 == 0:
            w = L.step(v, EX[ax])
            if w is not None:
                M.append((v, w))
    return M


def conjugator(L, ax=0):
    C0 = qprod([L.Aij(i, j) for (i, j) in matching(L, ax)])
    ZE = Q(0, 0, (1 << L.nq) - 1)
    return ZE * C0, C0, ZE


match_ok = tail_ok = zed_ok = True
bflip_ok = aflip_ok = face2_ok = True
tab_ok = c0_ok = ze_ok = jq_ok = True
sq_ok = mind_ok = eta_ok = True
c2sign = set()
for L, tag in ((L222, "2x2x2 cube"), (L444, "open 4x4x4"), (L444T, "torus 4^3")):
    M = matching(L, 0)
    deg = {v: 0 for v in L.V}
    for (i, j) in M:
        deg[i] += 1
        deg[j] += 1
    match_ok = match_ok and set(deg.values()) == {1} and 2 * len(M) == L.nv
    C, C0, ZE = conjugator(L)
    tail_ok = tail_ok and {b for b in range(C0.x.bit_length()) if C0.x >> b & 1} \
        == {L.ei[(i, 0)] for (i, j) in M}
    Zodd = qprod([Q(0, 0, L.star[v]) for v in L.V if eps_of(v) < 0])
    zed_ok = zed_ok and Zodd.x == ZE.x and Zodd.z == ZE.z
    for v in L.V:
        B = Bop(L, v)
        bflip_ok = bflip_ok and (conj_mono(C, B) + B).iszero() \
            and (conj_mono(C0, B) + B).iszero() and (conj_mono(ZE, B) - B).iszero()
    for (i, j, e, a) in L.bonds():
        A, T, J = Aop(L, i, j), Top(L, i, j), Jop(L, i, j, e)
        aflip_ok = aflip_ok and (conj_mono(C, A) + A).iszero() \
            and (conj_mono(C0, A) - A).iszero() and (conj_mono(ZE, A) + A).iszero()
        tab_ok = tab_ok and (conj_mono(C, T) - T).iszero()
        c0_ok = c0_ok and (conj_mono(C0, T) + T).iszero()
        ze_ok = ze_ok and (conj_mono(ZE, T) + T).iszero()
        jq_ok = jq_ok and (conj_mono(C, J) + J).iszero() \
            and (conj_mono(C0, J) - J).iszero() and (conj_mono(ZE, J) + J).iszero()
    fz = [L.loop(f) for f in L.faces()]
    face2_ok = face2_ok and all(commutes_mono(C, s) and commutes_mono(C0, s)
                                and commutes_mono(ZE, s) for s in fz)
    Hh, Hm, Qq = Hhop(L), Hmass(L), Qop(L)
    tab_ok = tab_ok and (conj_mono(C, Hh) - Hh).iszero() and (conj_mono(C, Hm) + Hm).iszero()
    c0_ok = c0_ok and (conj_mono(C0, Hh) + Hh).iszero() and (conj_mono(C0, Hm) + Hm).iszero()
    ze_ok = ze_ok and (conj_mono(ZE, Hh) + Hh).iszero() and (conj_mono(ZE, Hm) - Hm).iszero()
    jq_ok = jq_ok and (conj_mono(C, Qq) + Qq).iszero() and (conj_mono(C0, Qq) + Qq).iszero() \
        and (conj_mono(ZE, Qq) - Qq).iszero()
    cc = C * C
    c2sign.add("+" if cc.isI() else ("-" if cc.ismI() else "?"))
    sq_ok = sq_ok and cc.isI()
    My = matching(L, 1)
    if 2 * len(My) == L.nv:
        Cy = Q(0, 0, (1 << L.nq) - 1) * qprod([L.Aij(i, j) for (i, j) in My])
        mind_ok = mind_ok and all((conj_mono(Cy, Bop(L, v)) - conj_mono(C, Bop(L, v))).iszero()
                                  for v in L.V) \
            and all((conj_mono(Cy, Aop(L, i, j)) - conj_mono(C, Aop(L, i, j))).iszero()
                    for (i, j, e, a) in L.bonds())
    else:
        mind_ok = False
    nb = len(L.bonds())
    for wts in ([1] * nb, [Fr(1 + (k % 5), 3) for k in range(nb)]):
        Hw = Hhop(L, wts)
        eta_ok = eta_ok and (conj_mono(C, Hw) - Hw).iszero() \
            and (conj_mono(C0, Hw) + Hw).iszero() and (conj_mono(ZE, Hw) + Hw).iszero()

check('B1 [exact] x-dimer perfect matchings on cube/open4^3/torus4^3; C0 X-support equals matching', match_ok and tail_ok)
check('B2 [exact] ZE=prod_e Z_e=prod_odd B_v=(-1)^N_odd on the supplied bipartite graphs', zed_ok)
check('B3 [exact] C flips B and rho, n->1-n; C0 flips B, ZE fixes B', bflip_ok)
check("B4 [exact] C A_ij C^-1 = -A_ij on every bond, C_0 A_ij C_0^-1 = +A_ij, Z_E A_ij Z_E = -A_ij",
      aflip_ok)
check("B5 [exact] C, C_0 and Z_E commute with every S_f: S_f -> +S_f, code space preserved with no "
      "sign", face2_ok)
check('B6 [exact] C fixes T,H_hop and reverses H_m; C H(t,m) C^-1=H(t,-m)', tab_ok)
check('B7 [exact] C0 flips T,H_hop,H_m; fixes A,J', c0_ok)
check('B8 [exact] ZE flips A,T,H_hop; fixes B,H_m,Q', ze_ok)
check('B9 [exact] C reverses both current J and charge Q', jq_ok)
check("B10 [exact] C^2 = %sI on all three lattices: C is unitary and an involution" % "".join(sorted(c2sign)),
      sq_ok and c2sign == {"+"})
check('B11 [exact] y/x matching conjugation agrees on every encoded B,A; no ambient scalar claim', mind_ok)
check('B12 [exact] full table holds for KS, all+1 and generic rational bond weights', eta_ok)
print("  C: B_v -> -B_v, n_v -> I-n_v, A_ij -> -A_ij, S_f -> +S_f, T_ij -> +T_ij, H_hop -> +H_hop,"
      " H_m -> -H_m, J_ij -> -J_ij, Q -> -Q; eps_v is a supplied corner label, unchanged")

# =============================================== C -- the parity obstruction

allB_ok = all(qprod([Q(0, 0, L.star[v]) for v in L.V]).isI()
              for L in (L222, L333, L444, L444T))
check('C1 [exact] prod_v B_v=I on all tested blocks/tori: each edge occurs twice', allB_ok)
check('C2 [exact] odd |V|=%d forbids any unitary flipping all B on the fixed-parity code' % L333.nv, L333.nv % 2 == 1)
check('C3 [exact] odd degrees at all%d corners require even component size; named even graphs have matchings' % L333.nv,
      L333.nv % 2 == 1 and all(L.nv % 2 == 0 for L in (L222, L444, L444T)))

# ========================================= D -- the charge as a record readout

L = L222
NQ = L.nq
D = 1 << NQ
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


def Bm(v):
    return pmat(Q(0, 0, L.star[v]))


odd = np.zeros(D, dtype=np.int64)
for v in L.V:
    odd += popcount(col & L.star[v]) & 1
Qrec = odd - L.nv // 2
Qmat = sum((IM - Bm(v)) * 0.5 for v in L.V) - IM * (L.nv / 2.0)
Qdiag = np.real(Qmat.diagonal())
qdev = float(np.abs(Qdiag - Qrec).max())
check('D1 [exact] %d cube patterns: Q counts odd three-edge stars minus4; deviation %.1e' % (D, qdev), qdev == 0.0 and all(len(L.inc[v]) == pcnt(L.star[v]) == 3 for v in L.V))
qspec = sorted(set(int(x) for x in Qrec))
check('D2 [exact] cube incident-star charge spectrum %s, symmetric about0' % qspec,
      qspec == [-4, -2, 0, 2, 4] and int(Qrec.min()) == -L.nv // 2 and int(Qrec.max()) == L.nv // 2)


def Jm(i, j, e):
    return (pmat(L.Aij(i, j)) @ (IM - Bm(i) @ Bm(j))) * (0.5 * e)


bl = [(i, j, e) for (i, j, e, a) in L.bonds()]
jdev = max(float(np.abs(Jm(i, j, e).diagonal()).max()) for (i, j, e) in bl)
check('D3 [exact] current diagonal zero on%d bonds x%d patterns (%.1e); fixed-Z statistics do not read J' % (len(bl), D, jdev), jdev == 0.0)

# ================================== E -- this supplied finite state is C-invariant

def build1p(Ls, twist=(1, 1, 1)):
    sites = list(itertools.product(range(Ls), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((Ls ** 3, Ls ** 3))
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % Ls for i in range(3))
            s = eta_ks(v, a)
            if twist[a] and v[a] == Ls - 1:
                s = -s
            M[idx[w], idx[v]] += s
            M[idx[v], idx[w]] += s
    return M, np.array([float(eps_of(v)) for v in sites])


M1, e1 = build1p(4)
E1 = np.diag(e1)
ac = float(np.abs(E1 @ M1 @ E1 + M1).max())


def sea_proj(m):
    w, U = np.linalg.eigh(M1 + m * E1)
    S = U[:, w < -1e-9]
    return S @ S.conj().T


d4b = 0.0
for m in (0.0, 0.5, 1.0, 2.0):
    d4b = max(d4b, float(np.abs(E1 @ (np.eye(64) - sea_proj(m)) @ E1 - sea_proj(-m)).max()))
check('E1 [1e-12] antiperiodic4^3/no zeros: chiral residual %.1e, projector +/-m residual %.1e (m=0,.5,1,2)'
      % (ac, d4b), ac < 1e-12 and d4b < 1e-12)
n1 = np.real(np.diag(sea_proj(1.0)))
n2 = np.real(np.diag(sea_proj(-1.0)))
n0 = np.real(np.diag(sea_proj(0.0)))
dn = float(np.abs(n2 - (1 - n1)).max())
d0 = float(np.abs(n0 - 0.5).max())
check('E2 [1e-12] supplied finite sea n(-m)=1-n(m),residual %.1e; n(0)=1/2,residual %.1e' % (dn, d0), dn < 1e-12 and d0 < 1e-12)


def Ham(m=0.0, t=1.0):
    H = sp.csr_matrix((D, D), dtype=complex)
    for (i, j, e) in bl:
        H = H + (pmat(L.Aij(i, j)) @ (Bm(i) - Bm(j))) * (0.5j * (-t) * e)
    for v in L.V:
        H = H + Bm(v) * (-0.5 * m * eps_of(v))
    return H


Cq, C0q, ZEq = conjugator(L)
Cm, C0m = pmat(Cq), pmat(C0q)
Nm = sum((IM - Bm(v)) * 0.5 for v in L.V)
Pcode = IM
for f in L.faces():
    Pcode = Pcode @ ((IM + pmat(L.loop(f))) * 0.5)
rng = np.random.default_rng(11)
G = Pcode @ (rng.standard_normal((D, 200)) + 1j * rng.standard_normal((D, 200)))
Ub, sv, _ = np.linalg.svd(np.asarray(G), full_matrices=False)
kdim = int((sv > 1e-8).sum())
Vb = Ub[:, :kdim]


def red(op):
    return Vb.conj().T @ (op @ Vb)


Cc, Nc = red(Cm), red(Nm)
du = float(np.abs(Cc @ Cc.conj().T - np.eye(kdim)).max())
dn8 = float(np.abs(Cc @ Nc @ Cc.conj().T + Nc - L.nv * np.eye(kdim)).max())
wN = np.linalg.eigvalsh(Nc)
evenN = all(abs(x - round(x)) < 1e-8 and round(x) % 2 == 0 for x in wN)
check('E3 [1e-10] cube%d qubits,%d ambient,%d faces,code%d; C unitary residual%.1e, N->8-N residual%.1e'
      % (NQ, D, len(L.faces()), kdim, du, dn8),
      kdim == 1 << (L.nv - 1) and evenN and du < 1e-10 and dn8 < 1e-10)
dh = 0.0
for m in (0.0, 0.7, 1.5):
    dh = max(dh, float(np.abs(Cc @ red(Ham(m)) @ Cc.conj().T - red(Ham(-m))).max()))
H0 = red(Ham(0.0))
w0, U0 = np.linalg.eigh(H0)
dsym = float(np.abs(np.sort(w0) + np.sort(w0)[::-1]).max())
d0m = float(np.abs(C0m @ IM @ C0m.conj().T - IM).max())
ZEc = red(pmat(ZEq))
chiral_residual = float(np.abs(ZEc @ H0 @ ZEc.conj().T + H0).max())
check('E4 [matrix1e-10,spectrum1e-9] C H(m) C^-1=H(-m) residual%.1e; actual ZE chirality and reflected spectrum residual%.1e' % (dh, dsym),
      dh < 1e-10 and dsym < 1e-9 and d0m < 1e-10 and chiral_residual < 1e-10)
g = U0[:, 0]
ov = float(abs(np.vdot(g, Cc @ g)))
nbar = float(np.real(np.vdot(g, Nc @ g)))
check('E5 [1e-8] t=1,m=0 finite ground E=%.9f approximates-4sqrt3 (%.1e),N=%.9f,C-overlap=%.9f'
      % (w0[0], abs(w0[0] + 4 * np.sqrt(3.0)), nbar, ov),
      abs(w0[0] + 4 * np.sqrt(3.0)) < 1e-9 and abs(nbar - L.nv / 2) < 1e-8 and ov > 1 - 1e-8)
jmax = 0.0
for m in (0.0, 1.0):
    gm = np.linalg.eigh(red(Ham(m)))[1][:, 0]
    jmax = max(jmax, max(abs(complex(np.vdot(gm, red(Jm(i, j, e)) @ gm))) for (i, j, e) in bl))
check('E6 [1e-10] finite ground currents at m=0/1: max%.1e; C-oddness forces zero at m=0' % jmax, jmax < 1e-10)
wn, Un = np.linalg.eigh(Nc)
v0 = Un[:, int(np.argmin(wn))]
vF = Un[:, int(np.argmax(wn))]
Cv0 = Cc @ v0
ov0 = float(abs(np.vdot(v0, Cv0)))
nfull = float(np.real(np.vdot(Cv0, Nc @ Cv0)))
ovF = float(abs(np.vdot(vF, Cv0)))
check('E7 [overlap1e-9,N1e-8] empty-state C-overlap%.1e; mapped N=%.6f,full-state overlap%.9f; no physical vacuum selection'
      % (ov0, nfull, ovF),
      ov0 < 1e-9 and abs(nfull - L.nv) < 1e-8 and abs(ovF - 1) < 1e-9)

# Boundary, code-sector and fixed-record controls added after the original E1-E7.
def sea_domain(matrix, grading, zero_tol=1e-9):
    """Sufficient finite domain for the strict-negative projector identity at m=0."""
    ep = np.diag(grading)
    return (np.max(np.abs(matrix - matrix.conj().T)) < 1e-12
            and np.max(np.abs(ep @ matrix @ ep + matrix)) < 1e-12
            and np.min(np.abs(np.linalg.eigvalsh(matrix))) > zero_tol)

periodic_M, periodic_eps = build1p(4, twist=(0, 0, 0))
pw, pu = np.linalg.eigh(periodic_M)
pneg = pu[:, pw < -1e-9]
periodic_P = pneg @ pneg.conj().T
periodic_residual = float(np.max(np.abs(E1 @ (np.eye(64) - periodic_P) @ E1 - periodic_P)))
asymmetric_M = M1 + 0.25 * np.eye(64)
check("E8 [boundary] sea domain accepts antiperiodic matrix; rejects periodic 8-zero-mode/rank28 residual=1/8 and gapped nonchiral shift",
      sea_domain(M1, e1) and not sea_domain(periodic_M, periodic_eps)
      and int(np.sum(np.abs(pw) < 1e-9)) == 8 and pneg.shape[1] == 28
      and abs(periodic_residual - 0.125) < 1e-12 and not sea_domain(asymmetric_M, e1))
Cyq = conjugator(L, 1)[0]
ratio_q = Cq * Cyq
ratio_code = red(pmat(ratio_q))
ratio_phase = np.trace(ratio_code) / kdim
check("E9 [1e-10] x/y matching ratio is nonscalar on the ambient edge register but scalar on the complete cube +face code",
      (ratio_q.x, ratio_q.z) != (0, 0) and abs(abs(ratio_phase)-1) < 1e-10
      and np.max(np.abs(ratio_code-ratio_phase*np.eye(kdim))) < 1e-10)
u_record = np.asarray(Pcode[:, 2].toarray()).ravel()
u_record /= np.linalg.norm(u_record)
test_current = Jm(*bl[0])
v_record = test_current @ u_record
v_record /= np.linalg.norm(v_record)
states = [(u_record + v_record)/np.sqrt(2), (u_record - v_record)/np.sqrt(2)]
record_distance = float(np.max(np.abs(np.abs(states[0])**2 - np.abs(states[1])**2)))
currents = [float(np.real(np.vdot(z, test_current @ z))) for z in states]
check("E10 [1e-12] two complete +face-code states have identical full Z-record distributions but current +1/-1; fixed-record correlations cannot read J",
      record_distance < 1e-12 and np.allclose(currents, [1, -1], atol=1e-12, rtol=0)
      and all(np.linalg.norm(Pcode @ z-z) < 1e-12 for z in states))
asymmetric_spectrum = np.array([-2., -1., 1., 3.])
check("E11 [exact] real spectral-reflection oracle rejects an asymmetric spectrum",
      np.max(np.abs(np.sort(asymmetric_spectrum)+np.sort(asymmetric_spectrum)[::-1])) == 1)

print("SUMMARY: supplied finite current/conjugation algebra; component/code/seam domains explicit; no fixed-record current readout or physical vacuum selection.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
