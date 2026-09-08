#!/usr/bin/env python3
"""The fermion's U(1) coupled to quantum links: Gauss's law as a support condition among records.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3 carrying one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding, with
the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1},
eta_3(v) = (-1)^{v_1+v_2}, and a SECOND designed role per coarse edge -- a
spin-1/2 "link" site -- carrying

    E_e = (1/2) Z^L_e   (eigenvalues +-1/2),   U_e = (X^L_e + i Y^L_e)/2,

with the coarse edge (v, e_a) oriented i = v -> j = v + e_a and s_{v,e} = +1
when e leaves v, -1 when it enters.  The declared coupled law is

    H_hop^g = -t sum_<ij> eta_ij (T_ij X^L_ij + K_ij Y^L_ij) / 2,
    H_full^g = H_hop^g + lambda sum_f P_f + (g^2/2) sum_e E_e^2,

with T_ij = (i/2) A_ij (B_i - B_j), K_ij = -(1/2) A_ij (I - B_i B_j),
B_v = the product of the Z's at corner v = I - 2 n_v, S_f the ordered four-A
face loop, P_f = W_f + W_f^dag the oriented four-link ring exchange, and
G_v = (div E)_v - rho_v with rho_v^{sea} = n_v - 1/2 or
rho_v^{stag} = n_v - (1 - eps_v)/2. t,lambda,g are real and supplied.
The class method Hg builds hopping only; numerical full-H assembly adds the specified terms.

  A  THE GAUGE-INVARIANT HOP.  a_i^dag U_ij a_j + h.c. = (T X^L + K Y^L)/2 on
     every bond, K_ij two monomials, K = -i[T, n_i], {T, K} = 0,
     [T, K] = -2i(n_i - n_j), and J_ij (PR #7892) = -eta_ij t K_ij.
  B  GAUSS'S LAW AS A SUPPORT CONDITION.  G_v pure Z at one corner,
     [G_v, G_w] = [G_v, H^g] = 0, sum_v G_v = -Q, the coordination-parity
     condition, and the exact joint record-pattern counts.
  C  HOPPING-ONLY AMPERE AND CONTINUITY.  dE_e/dt = -J^g_e, dn_v/dt = -sum J^g,
     d(div E)_v/dt = dn_v/dt, E_e^2 = I/4, and the link-orientation reversal.
  D  THE RING EXCHANGE.  P_f Hermitian, eight monomials on four links,
     [P_f, G_v] = 0, [P_f, H_hop^g] != 0.
  E  THE COUPLED SEA.  The 256-dimensional plaquette and the cube's sparse
     14400-state Gauss sector.
  F  ONE-CORNER CONDITIONAL PROJECTIONS of the supplied Gauss relation.
     Only occurring prefixes are considered; no global gluing, fine-site
     locality, law-level probabilities or Record formation is derived.

Groups A-D and F are exact: Gaussian-rational coefficients on symplectic Pauli
monomials (F2 supports, Z4 phases) and integer record arithmetic, with no
floating-point step anywhere.  Group E is numerical at the stated tolerance.

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
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 120

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


def pcnt(n):
    return bin(n).count("1")


def eps_of(v):
    return -1 if (sum(v) & 1) else 1


def bits(n):
    out = set()
    i = 0
    while n:
        if n & 1:
            out.add(i)
        n >>= 1
        i += 1
    return out


# ============================================ symplectic Pauli monomials / sums

class Q:
    """i^k X^x Z^z on a register of sites indexed by bit position."""

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


def qprod(seq):
    o = Q(0, 0, 0)
    for p in seq:
        o = o * p
    return o


def cmul(a, b):
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


ONE = (Fr(1), Fr(0))
IMU = (Fr(0), Fr(1))
MONE = (Fr(-1), Fr(0))
H2 = (Fr(1, 2), Fr(0))
HI = (Fr(0), Fr(1, 2))
MH = (Fr(-1, 2), Fr(0))
MI = (Fr(0), Fr(-1))


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
        return a + b.smul(MONE)

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

    def isdiag(a):
        return all(x == 0 for (x, z) in a)

    def supp(a):
        s = set()
        for (x, z) in a:
            s |= bits(x | z)
        return s


def mono(q, c=ONE):
    ph = [(Fr(1), Fr(0)), (Fr(0), Fr(1)), (Fr(-1), Fr(0)), (Fr(0), Fr(-1))][q.k & 3]
    return PS({(q.x, q.z): cmul(c, ph)})


def zop(z, c=ONE):
    return PS({(0, z): c})


IDP = PS({(0, 0): ONE})


def comm(a, b):
    return a * b - b * a


def acomm(a, b):
    return a * b + b * a


class Lat:
    """Coarse cubic block with the BK superfast encoding on its edges."""

    def __init__(self, dims):
        self.dims = tuple(dims)
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


# ============================== the second designed role: one spin-1/2 link site

class G:
    """Fermion edge sites on bits 0..nq-1; link sites on bits nq..2nq-1."""

    def __init__(self, dims):
        self.L = L = Lat(dims)
        self.nq = L.nq
        self.bonds = []
        for (v, ax) in L.E:
            self.bonds.append((v, L.step(v, EX[ax]), eta_ks(v, ax), ax, L.ei[(v, ax)]))
        self.incs = {v: [] for v in L.V}
        for (i, j, e, ax, q) in self.bonds:
            self.incs[i].append((q, +1, j))
            self.incs[j].append((q, -1, i))
        self.eps = {v: eps_of(v) for v in L.V}

    # ---- fermion sector
    def Bv(self, v):
        return zop(self.L.star[v])

    def nv(self, v):
        return (IDP - self.Bv(v)).smul(H2)

    def Aij(self, i, j):
        return mono(self.L.Aij(i, j))

    def Tij(self, i, j):
        return (self.Aij(i, j) * (self.Bv(i) - self.Bv(j))).smul(HI)

    def Kij(self, i, j):
        return (self.Aij(i, j) * (IDP - self.Bv(i) * self.Bv(j))).smul(MH)

    def Jij(self, i, j, eta, t=1):
        """PR #7892's bond current J_ij = eta (t/2) A_ij (I - B_i B_j), no links."""
        return (self.Aij(i, j) * (IDP - self.Bv(i) * self.Bv(j))).smul((Fr(eta * t, 2), Fr(0)))

    # ---- link sector
    def m(self, q):
        return 1 << (self.nq + q)

    def XL(self, q):
        return PS({(self.m(q), 0): ONE})

    def YL(self, q):
        return PS({(self.m(q), self.m(q)): IMU})

    def ZL(self, q):
        return PS({(0, self.m(q)): ONE})

    def Ee(self, q):
        return self.ZL(q).smul(H2)

    def Up(self, q):
        m = self.m(q)
        return PS({(m, 0): H2, (m, m): MH})

    def Um(self, q):
        m = self.m(q)
        return PS({(m, 0): H2, (m, m): H2})

    # ---- the coupled law
    def hop(self, i, j, q):
        return (self.Tij(i, j) * self.XL(q) + self.Kij(i, j) * self.YL(q)).smul(H2)

    def Hg(self, t=1):
        H = PS()
        for (i, j, e, ax, q) in self.bonds:
            H = H + self.hop(i, j, q).smul((Fr(-t * e), Fr(0)))
        return H

    def Jg(self, i, j, eta, q, t=1):
        return (self.Kij(i, j) * self.XL(q)
                - self.Tij(i, j) * self.YL(q)).smul((Fr(-t * eta, 2), Fr(0)))

    # ---- Gauss
    def rho(self, v, kind):
        if kind == "sea":
            return self.nv(v) - IDP.smul(H2)
        return self.nv(v) - IDP.smul((Fr(1 - self.eps[v], 2), Fr(0)))

    def divE(self, v):
        o = PS()
        for (q, s, w) in self.incs[v]:
            o = o + self.Ee(q).smul((Fr(s), Fr(0)))
        return o

    def Gv(self, v, kind):
        return self.divE(v) - self.rho(v, kind)

    # ---- the ring exchange
    def face_links(self, f):
        L = self.L
        out = []
        n = len(f)
        for a in range(n):
            p, r = f[a], f[(a + 1) % n]
            for ax in range(3):
                if L.step(p, EX[ax]) == r and (p, ax) in L.ei:
                    out.append((L.ei[(p, ax)], +1))
                    break
                if L.step(r, EX[ax]) == p and (r, ax) in L.ei:
                    out.append((L.ei[(r, ax)], -1))
                    break
            else:
                raise KeyError((p, r))
        return out

    def Wf(self, f):
        o = IDP
        for (q, d) in self.face_links(f):
            o = o * (self.Up(q) if d > 0 else self.Um(q))
        return o

    def Pf(self, f):
        W = self.Wf(f)
        return W + W.dag()


GC = G((2, 2, 2))
GP = G((2, 2, 1))
GB = G((3, 3, 3))
BLOCKS = ((GC, "cube 2x2x2"), (GB, "open 3x3x3"))

print("H^g = -t sum eta (T X^L + K Y^L)/2; E_e = Z^L_e/2; U_e = (X^L + iY^L)/2; G_v = (div E)_v - rho_v")

# ============== A -- the gauge-invariant hop and the two-monomial K_ij [exact]

hop_ok = kk_ok = comm_ok = cur_ok = True
hmono = set()
kmono = set()
ksupp = set()
for g, tag in BLOCKS:
    for (i, j, e, ax, q) in g.bonds:
        T, K = g.Tij(i, j), g.Kij(i, j)
        aij = (T - K.smul(IMU)).smul(H2)          # a_i^dag a_j
        aji = (T + K.smul(IMU)).smul(H2)          # a_j^dag a_i
        lhs = aij * g.Up(q) + aji * g.Um(q)
        hop_ok = hop_ok and (lhs - g.hop(i, j, q)).iszero() and lhs.isherm()
        hmono.add(len(lhs))
        kk_ok = kk_ok and K.isherm() and (g.Kij(j, i) + K).iszero() \
            and (K - comm(T, g.nv(i)).smul(MI)).iszero() and K.supp() == T.supp()
        kmono.add(len(K))
        ksupp.add(len(K.supp()))
        comm_ok = comm_ok and acomm(T, K).iszero() \
            and (comm(T, K) + (g.nv(i) - g.nv(j)).smul((Fr(0), Fr(2)))).iszero() \
            and (comm(T, K) - (g.Bv(i) - g.Bv(j)).smul(IMU)).iszero()
        cur_ok = cur_ok and (g.Jij(i, j, e) + K.smul((Fr(e), Fr(0)))).iszero() \
            and not (g.Jij(i, j, e) - K.smul((Fr(e, 2), Fr(0)))).iszero()

nb = len(GC.bonds) + len(GB.bonds)
check("A1 [exact] a_i^dag U_ij a_j + a_j^dag U_ij^dag a_i = (T_ij X^L_ij + K_ij Y^L_ij)/2 exactly, "
      "Hermitian, %s Pauli monomials, on all %d bonds of the 2x2x2 cube and the open 3x3x3 block"
      % (sorted(hmono), nb), hop_ok and hmono == {4})
check("A2 [exact] K_ij = -(1/2) A_ij (I - B_i B_j): Hermitian, K_ji = -K_ij, exactly %s Pauli "
      "monomials on %s sites, the same support as T_ij" % (sorted(kmono), sorted(ksupp)),
      kk_ok and kmono == {2})
check("A3 [exact] K_ij = -i [T_ij, n_i] on every bond: given the hop, K is fixed by the fermion "
      "algebra, not chosen", kk_ok)
check("A4 [exact] {T_ij, K_ij} = 0 and [T_ij, K_ij] = -2i (n_i - n_j) = i (B_i - B_j) on every "
      "bond: T, K and n_i - n_j close an su(2) per bond", comm_ok)
check("A5 [exact] J_ij of PR #7892 = -eta_ij t K_ij on every bond -- one factor of t, sign MINUS, "
      "and NOT eta (t/2) K_ij: the coupled hop's Y^L partner is the uncoupled current", cur_ok)

# ================= B -- Gauss's law as a support condition among records [exact]

gz_ok = gg_ok = gh_ok = gq_ok = True
gmono = {}
gsupp = {}
for g, tag in BLOCKS:
    Hg = g.Hg()
    for kind in ("sea", "stag"):
        Gs = {v: g.Gv(v, kind) for v in g.L.V}
        gz_ok = gz_ok and all(x.isdiag() for x in Gs.values())
        gg_ok = gg_ok and all(comm(Gs[v], Gs[w]).iszero() for v in g.L.V for w in g.L.V)
        gh_ok = gh_ok and all(comm(Gs[v], Hg).iszero() for v in g.L.V)
        S = PS()
        R = PS()
        for v in g.L.V:
            S = S + Gs[v]
            R = R + g.rho(v, kind)
        gq_ok = gq_ok and (S + R).iszero()
        if tag == "cube 2x2x2":
            gmono[kind] = sorted({len(x) for x in Gs.values()})
            gsupp[kind] = sorted({len(x.supp()) for x in Gs.values()})
gsupp_b = sorted({len(GB.Gv(v, "sea").supp()) for v in GB.L.V})

check("B1 [exact] every G_v is pure Z -- record-diagonal -- with %s monomials on %s records at the "
      "one corner (sea/stag), and %s in the 3x3x3 block: 2 z_v records, 12 at a bulk corner"
      % (gmono["sea"], gsupp["sea"], gsupp_b), gz_ok and gsupp["sea"] == [6] and gsupp_b == [6, 8, 10, 12])
check("B2 [exact] [G_v, G_w] = 0 for all %d + %d corner pairs, both rho conventions: the corner "
      "operators are simultaneously diagonal; a nonempty joint zero set is separate"
      % (GC.L.nv ** 2, GB.L.nv ** 2), gg_ok)
check("B3 [exact] [G_v, H^g] = 0 at every corner of both blocks, both rho conventions: the coupled "
      "law preserves the corner condition exactly", gh_ok)
check("B4 [exact] sum_v G_v = -sum_v rho_v on both blocks, every link cancelling in the sum; in the "
      "sea convention that reads sum_v G_v = -Q with Q the PR #7892 charge", gq_ok)


def popc(a):
    a = np.array(a, dtype=np.int64)
    c = np.zeros_like(a)
    while a.any():
        c += a & 1
        a >>= 1
    return c


def enumerate_records(g):
    """Exact joint record-pattern census of G_v = 0, by vectorised bit arithmetic."""
    L = g.L
    nq = g.nq
    V = L.V
    NF = 1 << nq
    f = np.arange(NF, dtype=np.int64)
    nvals = np.stack([popc(f & L.star[v]) & 1 for v in V], axis=1)
    Nf = nvals.sum(1)
    sgn = np.zeros((len(V), nq), dtype=np.int64)
    for a, v in enumerate(V):
        for (q, s, w) in g.incs[v]:
            sgn[a, q] = s
    lb = np.stack([((f >> q) & 1) for q in range(nq)], axis=1)
    dv = (1 - 2 * lb) @ sgn.T
    eps = np.array([g.eps[v] for v in V], dtype=np.int64)
    out = {}
    for kind in ("sea", "stag"):
        r = 2 * nvals - 1 if kind == "sea" else 2 * nvals - (1 - eps)[None, :]
        lo = min(dv.min(), r.min())
        base = max(dv.max(), r.max()) - lo + 1
        pw = base ** np.arange(len(V), dtype=object)
        kd = ((dv - lo) * pw).sum(1)
        kr = ((r - lo) * pw).sum(1)
        uk, cnt = np.unique(kd, return_counts=True)
        idx = np.clip(np.searchsorted(uk, kr), 0, len(uk) - 1)
        per = np.where(uk[idx] == kr, cnt[idx], 0).astype(np.int64)
        out[kind] = (int(per.sum()), int((per > 0).sum()), per, Nf)
    return out


ec = enumerate_records(GC)
ep = enumerate_records(GP)
coord_c = sorted({len(GC.incs[v]) for v in GC.L.V})
coord_p = sorted({len(GP.incs[v]) for v in GP.L.V})
check("B5 [exact] coordination parity: 2 (div E)_v sums z_v terms +-1 so carries the parity of z_v, "
      "while 2 rho^sea = 2n - 1 is odd and 2 rho^stag = 2n - (1 - eps) even. Cube z = %s: %d joint "
      "patterns of 2^24 sea, %d stag; plaquette z = %s: %d and %d"
      % (coord_c, ec["sea"][0], ec["stag"][0], coord_p, ep["sea"][0], ep["stag"][0]),
      coord_c == [3] and coord_p == [2]
      and (ec["sea"][0], ec["stag"][0]) == (14400, 0)
      and (ep["sea"][0], ep["stag"][0]) == (0, 14))
per, Nf = ec["sea"][2], ec["sea"][3]
mult = sorted(zip(*[x.tolist() for x in np.unique(per[per > 0], return_counts=True)]))
Ns = sorted(set(Nf[per > 0].tolist()))
check("B6 [exact] on the cube exactly %d of the 4096 fermion record patterns admit a link pattern, "
      "and they are precisely the half-filled N = %s sector; link patterns each: %s" % (ec["sea"][1], Ns[0], ", ".join("%d x %d" % (b, a) for a, b in mult)),
      ec["sea"][1] == 2240 and Ns == [4]
      and mult == [(4, 192), (6, 1024), (7, 768), (8, 192), (9, 64)])
free_ok = True
dims_gc = []
for g, gauss in ((GC, 14400), (GP, 14)):
    L = g.L
    rank = L.nq - L.nv + 1
    fz = [L.loop(f) for f in L.faces()]
    for r in range(1, 1 << len(fz)):
        p = qprod([fz[a] for a in range(len(fz)) if (r >> a) & 1])
        if p.x == 0 and (p.z != 0 or (p.k & 2) == 0):
            pass
        if p.x == 0 and p.z == 0:
            continue
        if p.x == 0:
            free_ok = False
    dims_gc.append((gauss, rank, gauss // (1 << rank)))
check("B7 [exact] the code acts freely on the Gauss sector -- every nontrivial face-loop product "
      "carries X, hence zero diagonal -- so dim(Gauss and code) = %d/2^%d = %d on the cube, "
      "%d/2^%d = %d on the plaquette"
      % (dims_gc[0][0], dims_gc[0][1], dims_gc[0][2], dims_gc[1][0], dims_gc[1][1], dims_gc[1][2]),
      free_ok and dims_gc[0][2] == 450 and dims_gc[1][2] == 7)

# ============================== C -- Ampere, continuity and bond reversal [exact]

cont_ok = amp_ok = joint_ok = herm_ok = split_ok = rev_ok = True
naive_fails = 0
naive_tot = 0
esq_ok = True
for g, tag in BLOCKS:
    Hg = g.Hg()
    nbr = {v: [] for v in g.L.V}
    for (i, j, e, ax, q) in g.bonds:
        nbr[i].append((j, e, q, +1))
        nbr[j].append((i, e, q, -1))
    for v in g.L.V:
        lhs = comm(Hg, g.nv(v)).smul(IMU)
        rhs = PS()
        for (w, e, q, s) in nbr[v]:
            Jg = g.Jg(v, w, e, q) if s > 0 else g.Jg(w, v, e, q).smul(MONE)
            rhs = rhs - Jg
        cont_ok = cont_ok and (lhs - rhs).iszero()
        joint_ok = joint_ok and (comm(Hg, g.divE(v)).smul(IMU) - lhs).iszero()
    for (i, j, e, ax, q) in g.bonds:
        Jg = g.Jg(i, j, e, q)
        amp_ok = amp_ok and (comm(Hg, g.Ee(q)).smul(IMU) + Jg).iszero()
        herm_ok = herm_ok and Jg.isherm()
        split_ok = split_ok and (Jg - (g.Jij(i, j, e) * g.XL(q)
                                      + g.Tij(i, j).smul((Fr(e), Fr(0))) * g.YL(q)).smul(H2)).iszero()
        naive_tot += 1
        if not (Jg + g.Jg(j, i, e, q)).iszero():
            naive_fails += 1
        X = g.XL(q)
        rev_ok = rev_ok and ((X * g.Jg(j, i, e, q) * X) + Jg).iszero()
        esq_ok = esq_ok and (g.Ee(q) * g.Ee(q) - IDP.smul((Fr(1, 4), Fr(0)))).iszero()

check("C1 [exact] coupled continuity dn_v/dt = i[H^g, n_v] = -sum_w J^g_vw at every corner of both "
      "blocks, with J^g_ij = -(t eta_ij/2)(K_ij X^L_ij - T_ij Y^L_ij)", cont_ok)
check("C2 [exact] Hopping-only Ampere i[H_hop^g, E_e] = -J^g_e on every one of the %d links, e oriented "
      "tail to head; full-H evolution additionally includes the magnetic curl" % naive_tot,
      amp_ok)
check("C3 [exact] joint continuity d(div E)_v/dt = dn_v/dt at every corner -- B3 written as a rate: "
      "the flux divergence and the corner parity cannot drift apart", joint_ok)
check("C4 [exact] every J^g_ij is Hermitian and J^g_ij = (1/2)(J_ij X^L_ij + eta_ij t T_ij Y^L_ij): "
      "the X^L coefficient is half the uncoupled PR #7892 current",
      herm_ok and split_ok)
check("C5 [exact] reversing a bond must reverse the link orientation too: X^L_e J^g_ji X^L_e = "
      "-J^g_ij on every bond, while J^g_ji = -J^g_ij alone fails on %d of %d bonds"
      % (naive_fails, naive_tot), rev_ok and naive_fails == naive_tot)
check("C6 [exact] E_e^2 = I/4 identically on every link, so (g^2/2) sum_e E_e^2 is a c-number: at "
      "spin 1/2 the electric term supplies no dynamics at all", esq_ok)

# F5: the actual full-H link equation includes a nonzero magnetic curl.
magnetic_sum = PS()
for face in GP.L.faces():
    magnetic_sum = magnetic_sum + GP.Pf(face)
full_h = GP.Hg() + magnetic_sum  # t=1, lambda=1; electric term is scalar here.
curl_ok = True
curl_sizes = []
for i, j, eta, axis, q in GP.bonds:
    curl = comm(magnetic_sum, GP.Ee(q)).smul(IMU)
    actual_rate = comm(full_h, GP.Ee(q)).smul(IMU)
    expected_rate = GP.Jg(i, j, eta, q).smul(MONE) + curl
    curl_ok &= (actual_rate - expected_rate).iszero()
    curl_sizes.append(len(curl))
check("C7 [exact] full-H lambda=1 plaquette: i[H,E]=-J+magnetic curl, eight nonzero curl terms on every link and zero divergence",
      curl_ok and curl_sizes == [8]*4
      and all(comm(magnetic_sum, GP.divE(v)).iszero() and comm(full_h, GP.Gv(v, 'stag')).iszero() for v in GP.L.V))

# ================================== D -- the four-link ring exchange P_f [exact]

pf_herm = pf_gauss = pf_code = pf_z2 = True
pf_mono = set()
pf_supp = set()
pf_bad = None
for g, tag in ((GC, "cube"), (GP, "plaquette")):
    Hg = g.Hg()
    for f in g.L.faces():
        Pf = g.Pf(f)
        pf_mono.add(len(Pf))
        pf_supp.add(len(Pf.supp()))
        pf_herm = pf_herm and Pf.isherm()
        pf_supp_links = all(b >= g.nq for b in Pf.supp())
        pf_herm = pf_herm and pf_supp_links
        for kind in ("sea", "stag"):
            for v in g.L.V:
                pf_gauss = pf_gauss and comm(Pf, g.Gv(v, kind)).iszero()
        pf_code = pf_code and comm(Pf, mono(g.L.loop(f))).iszero()
        zf = PS({(0, sum(1 << (g.nq + q) for (q, d) in g.face_links(f))): ONE})
        pf_z2 = pf_z2 and comm(Pf, zf).iszero()
        c = comm(Pf, Hg)
        if not c.iszero() and pf_bad is None:
            pf_bad = (f[0], len(c))

npairs = len(GC.L.faces()) * GC.L.nv
check("D1 [exact] P_f = W_f + W_f^dag, the oriented four-link ring exchange, is Hermitian with %s "
      "Pauli monomials on exactly %s sites -- the four link records of one coarse face, no fermion "
      "record" % (sorted(pf_mono), sorted(pf_supp)), pf_herm and pf_mono == {8} and pf_supp == {4})
check("D2 [exact] [P_f, G_v] = 0 for all %d face-corner pairs on the cube and %d on the plaquette, "
      "in both rho conventions: the ring exchange respects the corner condition"
      % (npairs, len(GP.L.faces()) * GP.L.nv), pf_gauss)
check("D3 [exact] [P_f, S_f] = 0 and [P_f, prod_{e in f} Z^L_e] = 0: the fermion code is untouched, "
      "and the Z2 face flux is a record-diagonal constant of the ring exchange",
      pf_code and pf_z2)
check("D4 [exact] [P_f, H_hop^g] != 0 -- on the cube face at %s the commutator carries %d nonzero Pauli "
      "monomials: the link sector's declared dynamics does not commute with the coupled hop"
      % (pf_bad[0], pf_bad[1]) if pf_bad else "D4 no nonzero commutator", pf_bad is not None and pf_bad[1] == 64)

# ============================= E -- the coupled sea, plaquette and cube [numerical]

def dense(ps, n):
    d = 1 << n
    M = np.zeros((d, d), dtype=complex)
    s = np.arange(d, dtype=np.int64)
    for (x, z), (re, im) in ps.items():
        ph = 1 - 2 * (popc(s & z) & 1)
        M[s ^ x, s] += complex(float(re), float(im)) * ph
    return M


g = GP
NQP = 2 * g.nq
DP = 1 << NQP
Hgp = dense(g.Hg(), NQP)
f0 = g.L.faces()[0]
Pfp = dense(g.Pf(f0), NQP)
Sfp = dense(mono(g.L.loop(f0)), NQP)
dims_p = {}
for kind in ("sea", "stag"):
    m = np.ones(DP, dtype=bool)
    for v in g.L.V:
        m &= np.abs(np.real(np.diag(dense(g.Gv(v, kind), NQP)))) < 1e-12
    dims_p[kind] = m
idx = np.where(dims_p["stag"])[0]
Pg = np.eye(DP)[:, idx]
Sg = Pg.conj().T @ Sfp @ Pg
wS, US = np.linalg.eigh(Sg)
codeP = US[:, np.abs(np.real(wS) - 1) < 1e-9]
Bs = Pg @ codeP
check("E1 [1e-12] plaquette 2x2x1, %d records = %d dimensions: the Gauss sector has dimension %d in "
      "the admissible staggered convention, %d in the sea convention (z = 2 is even), and %d "
      "intersected with the fermion code"
      % (NQP, DP, int(dims_p["stag"].sum()), int(dims_p["sea"].sum()), codeP.shape[1]),
      int(dims_p["stag"].sum()) == 14 and int(dims_p["sea"].sum()) == 0 and codeP.shape[1] == 7)
resP = {}
for lam in (0.0, 1.0):
    M = Bs.conj().T @ (Hgp + lam * Pfp) @ Bs
    ev, vec = np.linalg.eigh(M)
    psi = Bs @ vec[:, 0]
    ex = lambda O: float(np.real(psi.conj() @ O @ psi))
    resP[lam] = (float(ev[0]), ex(Pfp),
                 max(abs(ex(dense(g.rho(v, "stag"), NQP))) for v in g.L.V))
check('E2 [1e-12/1e-11] plaquette +code E0≈%.12f (-sqrt6,lambda0),%.12f (lambda1); Pf≈%.12f (1/6),%.12f' % (resP[0.0][0], resP[1.0][0], resP[0.0][1], resP[1.0][1]),
      abs(resP[0.0][0] + np.sqrt(6.0)) < 1e-12 and abs(resP[1.0][0] + 2.323404276086) < 1e-11
      and abs(resP[0.0][1] - 1.0 / 6.0) < 1e-12 and abs(resP[1.0][1] - 0.094209746012) < 1e-11)
check("E3 [1e-9] the plaquette's admissible convention is not locally neutral: max |<rho_v>| = %.10f "
      "at lambda = 0 and %.10f at lambda = 1, the total charge vanishing only in the sum"
      % (resP[0.0][2], resP[1.0][2]),
      abs(resP[0.0][2] - 0.5833333333) < 1e-9 and abs(resP[1.0][2] - 0.6456532164) < 1e-9)

g = GC
nq = g.nq
V = g.L.V
NFC = 1 << nq
fpat = np.arange(NFC, dtype=np.int64)
nvC = np.stack([popc(fpat & g.L.star[v]) & 1 for v in V], axis=1)
sgnC = np.zeros((len(V), nq), dtype=np.int64)
for a, v in enumerate(V):
    for (q, s, w) in g.incs[v]:
        sgnC[a, q] = s
lbC = np.stack([((fpat >> q) & 1) for q in range(nq)], axis=1)
dvC = (1 - 2 * lbC) @ sgnC.T
rC = 2 * nvC - 1
pw = 9 ** np.arange(len(V), dtype=object)
kdC = ((dvC + 3) * pw).sum(1)
krC = ((rC + 3) * pw).sum(1)
order = np.argsort(kdC)
kds = kdC[order]
pairs = []
for fi in range(NFC):
    lo = np.searchsorted(kds, krC[fi], "left")
    hi = np.searchsorted(kds, krC[fi], "right")
    for li in order[lo:hi]:
        pairs.append(fi | (int(li) << nq))
sec = np.array(sorted(pairs), dtype=np.int64)
DC = len(sec)


def spmat(ps):
    rows, cols, vals = [], [], []
    ar = np.arange(DC)
    for (x, z), (re, im) in ps.items():
        tgt = sec ^ x
        j = np.searchsorted(sec, tgt)
        jc = np.clip(j, 0, DC - 1)
        ok = (j < DC) & (sec[jc] == tgt)
        ph = 1 - 2 * (popc(sec & z) & 1)
        rows.append(jc[ok])
        cols.append(ar[ok])
        vals.append((complex(float(re), float(im)) * ph)[ok])
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))),
                         shape=(DC, DC))


HgC = spmat(g.Hg())
facesC = g.L.faces()
SfC = [spmat(mono(g.L.loop(f))) for f in facesC]
PfC = [spmat(g.Pf(f)) for f in facesC]
Pftot = sum(PfC)
STAB = sum(SfC)
nopsC = [spmat(g.nv(v)) for v in V]
ropsC = [spmat(g.rho(v, "sea")) for v in V]
EopsC = [spmat(g.Ee(q)) for (_, _, _, _, q) in g.bonds]
hdev = float(abs(HgC - HgC.getH()).max())
V0 = np.random.default_rng(20260903).standard_normal(DC)
resC = {}
for lam in (0.0, 1.0):
    M = (HgC + lam * Pftot - 5.0 * STAB).tocsc()
    ev, vec = spla.eigsh(M, k=2, which="SA", maxiter=40000, tol=0, v0=V0)
    o = np.argsort(ev)
    psi = vec[:, o[0]]
    ex = lambda O: float(np.real(psi.conj() @ (O @ psi)))
    resC[lam] = (float(ev[o[0]]) + 5.0 * len(facesC),
                 min(ex(S) for S in SfC),
                 sum(ex(o2) for o2 in nopsC),
                 max(abs(ex(o2) - 0.5) for o2 in nopsC),
                 max(abs(ex(o2)) for o2 in ropsC),
                 max(abs(ex(o2)) for o2 in EopsC))
check("E4 [Herm1e-12,code1e-8] cube 2x2x2, 24 records: the Gauss sector is %d states of 2^24, on which H^g is "
      "sparse with %d nonzeros, Hermitian at %.1e; the ground state lies in the code space at "
      "<S_f> = %.9f" % (DC, HgC.nnz, hdev, resC[0.0][1]),
      DC == 14400 and HgC.nnz == 79872 and hdev < 1e-12 and resC[0.0][1] > 1 - 1e-8)
check("E5 [energy1e-9,N1e-8] coupled cube ground state: E_0 = %.12f at lambda = 0 and %.12f at lambda = 1, both "
      "at <N> = %.9f, exactly half filling" % (resC[0.0][0], resC[1.0][0], resC[0.0][2]),
      abs(resC[0.0][0] + 5.466823694822) < 1e-9 and abs(resC[1.0][0] + 6.980814328073) < 1e-9
      and abs(resC[0.0][2] - 4.0) < 1e-8 and abs(resC[1.0][2] - 4.0) < 1e-8)
check("E6 [1e-12] the coupled sea is neutral with zero mean flux: <n_v> = 1/2 to %.1e, <rho_v> = 0 "
      "to %.1e at every one of the 8 corners, <E_e> = 0 to %.1e on every one of the 12 links, at "
      "lambda = 0 and lambda = 1 alike"
      % (max(resC[0.0][3], resC[1.0][3]), max(resC[0.0][4], resC[1.0][4]),
         max(resC[0.0][5], resC[1.0][5])),
      max(resC[0.0][3], resC[1.0][3]) < 1e-12 and max(resC[0.0][4], resC[1.0][4]) < 1e-12
      and max(resC[0.0][5], resC[1.0][5]) < 1e-12)


# ========== F -- supplied one-corner conditional-projection relation [exact]
# The table restricts only prefixes occurring in a supplied one-corner relation.
# It reconstructs that relation in every order; global extension and physical
# fine-site formation are separate, unproved obligations. n_v is a product/parity
# of fermion bits, so the relation is not linear in those individual bits.


def corner_table(g, v, kind):
    """Every assignment of the 2 z_v records at corner v with G_v = 0, plus the
    conditional support table. Bit r < z_v is the fermion edge record of the r-th incident
    edge and bit z_v + r its link record; a bit b carries the Z value 1 - 2b, so
    2 (div E)_v = sum_e s_{v,e} (1 - 2 b) and 2 rho_v = 2 n_v - c with n_v the
    corner parity of the fermion edge records.  A[(mask, val, r)] is the set of
    values of record r occurring in this relation conditional on the records in `mask`."""
    inc = sorted(g.incs[v])
    z = len(inc)
    n = 2 * z
    c = 1 if kind == "sea" else 1 - g.eps[v]
    pats = []
    for p in range(1 << n):
        nv = 0
        d = 0
        for r, (q, s, w) in enumerate(inc):
            nv ^= (p >> r) & 1
            d += s * (1 - 2 * ((p >> (z + r)) & 1))
        if d == 2 * nv - c:
            pats.append(p)
    A = {}
    for mask in range(1 << n):
        groups = {}
        for p in pats:
            groups.setdefault(p & mask, []).append(p)
        for val, gp in groups.items():
            for r in range(n):
                if not (mask >> r) & 1:
                    A[(mask, val, r)] = frozenset((p >> r) & 1 for p in gp)
    return pats, n, A


def formed_set(A, n, order):
    """Reconstruct the supplied one-corner relation through its occurring-prefix
    projections in `order`; this does not implement a global formation law."""
    frontier = {(0, 0)}
    for r in order:
        nxt = set()
        for (mask, val) in frontier:
            av = A.get((mask, val, r), frozenset())
            if not av:
                return None
            for b in av:
                nxt.add((mask | (1 << r), val | (b << r)))
        frontier = nxt
    return {val for (_, val) in frontier}


CORNERS = []
for g, kind, tag in ((GC, "sea", "cube"), (GP, "stag", "plaquette")):
    for v in g.L.V:
        CORNERS.append((tag, v) + corner_table(g, v, kind))

last_ok = True
last_cases = 0
open_cases = 0
never_empty = True
free_at_empty = True
first_forcing = {}
sizes = {}
for (tag, v, pats, n, A) in CORNERS:
    sizes.setdefault(tag, set()).add(len(pats))
    full = (1 << n) - 1
    for (mask, val, r), av in A.items():
        k = pcnt(mask)
        never_empty = never_empty and len(av) >= 1
        open_cases += 1
        if k == 0:
            free_at_empty = free_at_empty and len(av) == 2
        if len(av) == 1 and (tag not in first_forcing or k < first_forcing[tag]):
            first_forcing[tag] = k
        if mask == full ^ (1 << r):
            last_cases += 1
            last_ok = last_ok and len(av) == 1

check('F1 [exact] %d occurring all-but-one prefixes force the last value within the supplied one-corner relation' % last_cases, last_ok and last_cases == 1248)
check('F2 [exact] %d occurring prefix/missing-record pairs have nonempty local projections; first forcing after%d cube/%d plaquette records'
      % (open_cases, first_forcing["cube"], first_forcing["plaquette"]),
      never_empty and free_at_empty and first_forcing == {"cube": 2, "plaquette": 1})

order_ok = True
norders = {}
for (tag, v, pats, n, A) in CORNERS:
    target = set(pats)
    cnt = 0
    for order in itertools.permutations(range(n)):
        cnt += 1
        order_ok = order_ok and formed_set(A, n, order) == target
    norders[tag] = cnt
check('F3 [exact] %d cube/%d plaquette orders reconstruct each supplied relation (%s/%s patterns); no global formation'
      % (norders["cube"], norders["plaquette"], sorted(sizes["cube"])[0], sorted(sizes["plaquette"])[0]),
      order_ok and norders == {"cube": 720, "plaquette": 24}
      and sizes == {"cube": {24}, "plaquette": {6}})
# Bind every complete local table to the independently evaluated actual G_v.
table_bound = True
for model, kind in ((GC, 'sea'), (GP, 'stag')):
    for vertex in model.L.V:
        incident = sorted(model.incs[vertex]); z = len(incident)
        pats, nbits, supports = corner_table(model, vertex, kind)
        direct = []
        for local in range(1 << nbits):
            full = 0
            for r, (edge, sign, other) in enumerate(incident):
                full |= ((local >> r) & 1) << edge
                full |= ((local >> (z+r)) & 1) << (model.nq+edge)
            value = (Fr(0), Fr(0))
            for (xmask, zmask), coefficient in model.Gv(vertex, kind).items():
                assert xmask == 0
                phase = (-1)**pcnt(full & zmask)
                value = tuple(value[k]+phase*coefficient[k] for k in range(2))
            if value == (0, 0): direct.append(local)
        table_bound &= pats == direct
check("F4 [exact] all complete corner tables equal the zero set of the actual declared G_v, including staggered signs", table_bound)

# Exhaustive 256-state boundary witness; no global-completion oracle is added to the local rule.
local_valid = {v: [] for v in GP.L.V}; valid_global = []; corner_masks = {}
for v in GP.L.V:
    corner_masks[v] = sum((1 << q) | (1 << (GP.nq+q)) for q, sign, other in GP.incs[v])
for record in range(1 << (2*GP.nq)):
    good = True
    for v in GP.L.V:
        value = sum(coefficient[0]*((-1)**pcnt(record & zmask))
                    for (xmask, zmask), coefficient in GP.Gv(v, 'stag').items())
        if value == 0: local_valid[v].append(record)
        else: good = False
    if good: valid_global.append(record)
all_fermion_mask = (1 << GP.nq)-1
local_extension = all(any((r & all_fermion_mask) == 0 for r in pats) for pats in local_valid.values())
global_extension = any((r & all_fermion_mask) == 0 for r in valid_global)
frontier = [(0, 0, [])]; dead_end = None
while frontier and dead_end is None:
    mask, value, prefix = frontier.pop()
    for q in range(2*GP.nq):
        if mask >> q & 1: continue
        choices = []
        for bit in (0, 1):
            next_mask = mask | (1 << q); next_value = value | (bit << q)
            if all(any((r & next_mask & corner_masks[v]) == (next_value & corner_masks[v])
                       for r in pats) for v, pats in local_valid.items()): choices.append(bit)
        if not choices: dead_end = (mask, value, prefix, q); break
        if len(prefix) < 7:
            frontier.extend((mask | (1 << q), value | (bit << q), prefix+[(q,bit)]) for bit in choices)
check("F5 [exact] local/global boundary: all-four-fermion-zero prefix has local completions but no global Gauss completion; a locally permitted prefix gets stuck",
      len(valid_global)==14 and local_extension and not global_extension and dead_end is not None)

print("SUMMARY: an exactly gauge-invariant minimal coupling of the fermion's U(1) to a designed "
      "spin-1/2 link role; Gauss's law is a record-diagonal corner relation whose solution set on "
      "the cube projects onto the half-filled fermion patterns; global formation remains open; spin-1/2 links carry a coordination-parity "
      "condition; the coupled sea is neutral with zero mean flux. No photon is shown.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
