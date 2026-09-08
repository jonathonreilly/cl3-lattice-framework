#!/usr/bin/env python3
"""Finite integer-flux coupling, local parity, code spectra and scalar Wilson comparison.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3 carrying one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding, with
the Kawamoto-Smit link signs eta_1 = 1, eta_2(v) = (-1)^{v_1},
eta_3(v) = (-1)^{v_1+v_2}.  The ONE change from the spin-1/2 link role of
PR #7893 is that each coarse edge carries a COMPACT U(1) link role instead:

    E_e |m> = m |m>,  m integer, truncated to m in {-S, ..., S};
    U_e |m> = |m+1>   (U|S> = 0),   so   [E_e, U_e] = U_e exactly;
    C_e = U_e + U_e^dag,   S_e = -i(U_e - U_e^dag),   both Hermitian.

The link role is a DESIGN element of exactly the kind PR #7834's period-(4,2,2)
superlattice role pattern is; it is derived from no axiom.  The declared law is

    H^g = -t sum_<ij> eta_ij (T_ij C_e + K_ij S_e) / 2      the coupled hop
    H_E = (g^2/2) sum_e E_e^2                                the electric term
    H_B = -(1/g^2) sum_f cos_f,  cos_f = (W_f + W_f^dag)/2   the magnetic term

with T_ij = (i/2) A_ij (B_i - B_j), K_ij = -(1/2) A_ij (I - B_i B_j),
B_v = the product of the Z's at corner v = I - 2 n_v, W_f the oriented four-link
loop product, and G_v = (div E)_v - rho_v with rho^sea_v = n_v - 1/2 or
rho^stag_v = n_v - (1 - eps_v)/2. t is real and g is nonzero real, both supplied.

  A  THE COUPLING.  a_i^dag U_ij a_j + h.c. = (T C + K S)/2 on every bond,
     what truncation preserves and what it breaks, and [G_v, H^g] = 0 at every
     corner of every coordination z = 2..6.
  B  LOCAL INTEGER PARITY, finite global censuses and a global code-parity
     obstruction. Background translation changes both carrier and energy.
  C  NONCONSTANT ELECTRIC ENERGY AND WILSON COMPRESSION preserving Gauss.
     The scalar positive-curvature comparison does not supply a Euclidean action.
  D  RAW26/50 SPECTRA AND +CODE13/25 FOCK EQUIVALENCE at g^2=1,S1/2.
     Raw zero gaps and degenerate cosine choices are not code-gap invariants.
  E  FINITE RING ENERGY COMPARISONS, both raw loop sectors retained;
     exact pure-electric energy, supplied-H screening, no thermodynamic claim.

Groups A, B, C and E2 are exact -- Gaussian-rational Pauli monomials (F2
supports, Z4 phases) tensored with exact integer link matrices, and exact
integer record arithmetic, with no floating-point step anywhere.  The items
tagged [numerical] are floating-point at the stated tolerance.  No dense object
above 4096 x 4096 is formed anywhere; the cube is counted, never diagonalised.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
import time
from fractions import Fraction as Fr

import numpy as np

AUDIT_TIMEOUT_SEC = 150

T0 = time.time()
PASS = 0
FAIL = 0


def check(label, cond):
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


def psmat(P, nq):
    """dense complex matrix of a PS on nq fermion record qubits."""
    N = 1 << nq
    M = np.zeros((N, N), dtype=np.complex128)
    b = np.arange(N)
    for (x, z), (re, im) in P.items():
        sgn = np.array([(-1) ** pcnt(int(k) & z) for k in b], dtype=np.float64)
        M[b ^ x, b] += complex(float(re), float(im)) * sgn
    return M


# ================================== the compact U(1) link role: exact integers

def linkops(S):
    """E, U, U^dag, C = U + U^dag, Sm = -i(U - U^dag) on E in {-S..S}."""
    d = 2 * S + 1
    Em = np.diag(np.arange(-S, S + 1)).astype(np.int64)
    U = np.zeros((d, d), dtype=np.int64)
    for a in range(d - 1):
        U[a + 1, a] = 1                       # U|m> = |m+1>
    Ud = U.T.copy()
    C = (U + Ud).astype(np.complex128)
    Sm = (-1j) * (U - Ud).astype(np.complex128)
    return d, Em, U, Ud, C, Sm


class PM:
    """d x d matrix of exact PS entries: the hybrid fermion x link algebra."""

    __slots__ = ("d", "e")

    def __init__(self, d, e=None):
        self.d = d
        self.e = dict(e or {})

    @staticmethod
    def eye(d, P=None):
        P = IDP if P is None else P
        return PM(d, {(a, a): P for a in range(d)})

    @staticmethod
    def kron(P, M):
        d = M.shape[0]
        e = {}
        for a in range(d):
            for b in range(d):
                z = complex(M[a, b])
                if z == 0:
                    continue
                t = P.smul((Fr(z.real).limit_denominator(10 ** 9),
                            Fr(z.imag).limit_denominator(10 ** 9)))
                if t:
                    e[(a, b)] = t
        return PM(d, e)

    def __add__(a, b):
        o = PM(a.d, a.e)
        for k, v in b.e.items():
            w = o.e.get(k)
            s = v if w is None else (w + v)
            if s:
                o.e[k] = s
            elif k in o.e:
                del o.e[k]
        return o

    def __sub__(a, b):
        return a + b.smul(MONE)

    def smul(a, s):
        o = PM(a.d)
        for k, v in a.e.items():
            t = v.smul(s)
            if t:
                o.e[k] = t
        return o

    def __mul__(a, b):
        o = PM(a.d)
        for (r, m), P in a.e.items():
            for (m2, c), R in b.e.items():
                if m2 != m:
                    continue
                t = P * R
                if not t:
                    continue
                w = o.e.get((r, c))
                s = t if w is None else (w + t)
                if s:
                    o.e[(r, c)] = s
                elif (r, c) in o.e:
                    del o.e[(r, c)]
        return o

    def dag(a):
        return PM(a.d, {(b, r): P.dag() for (r, b), P in a.e.items()})

    def iszero(a):
        return all(not v for v in a.e.values())

    def nterms(a):
        return sum(len(v) for v in a.e.values())


def pmcomm(a, b):
    return a * b - b * a


# ==================================== the coarse block and its superfast code

class Lat:
    def __init__(self, dims):
        self.dims = tuple(dims)
        self.V = [v for v in itertools.product(*(range(d) for d in dims))]
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


class Geo:
    """A coarse block: BK fermion edge records plus one compact link per edge."""

    def __init__(self, dims):
        self.L = L = Lat(dims)
        self.nq = L.nq
        self.V = L.V
        self.bonds = [(v, L.step(v, EX[ax]), eta_ks(v, ax), ax, L.ei[(v, ax)])
                      for (v, ax) in L.E]
        self.incs = {v: [] for v in L.V}
        for (i, j, e, ax, q) in self.bonds:
            self.incs[i].append((q, +1, j))
            self.incs[j].append((q, -1, i))
        self.eps = {v: eps_of(v) for v in L.V}
        self.star = L.star

    def Bv(self, v):
        return zop(self.star[v])

    def nv(self, v):
        return (IDP - self.Bv(v)).smul(H2)

    def Aij(self, i, j):
        return mono(self.L.Aij(i, j))

    def Tij(self, i, j):
        return (self.Aij(i, j) * (self.Bv(i) - self.Bv(j))).smul(HI)

    def Kij(self, i, j):
        return (self.Aij(i, j) * (IDP - self.Bv(i) * self.Bv(j))).smul(MH)

    def rho(self, v, kind):
        if kind == "sea":
            return self.nv(v) - IDP.smul(H2)
        return self.nv(v) - IDP.smul((Fr(1 - self.eps[v], 2), Fr(0)))

    def faces(self):
        return self.L.faces()

    def face_links(self, f):
        L = self.L
        out = []
        for a in range(len(f)):
            p, r = f[a], f[(a + 1) % len(f)]
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


class Ring:
    """Periodic 1D chain, Lv corners and Lv links, superfast encoding by hand:
       A_{v,v+1} = X_{q_v} Z_{q_{v-1}}, B_v = Z_{q_{v-1}} Z_{q_v}, eta = 1."""

    def __init__(self, Lv):
        self.Lv = Lv
        self.nq = Lv
        self.V = list(range(Lv))
        self.star = {v: (1 << ((v - 1) % Lv)) | (1 << v) for v in range(Lv)}
        self.bonds = [(v, (v + 1) % Lv, 1, 0, v) for v in range(Lv)]
        self.incs = {v: [] for v in range(Lv)}
        for (i, j, e, ax, q) in self.bonds:
            self.incs[i].append((q, +1, j))
            self.incs[j].append((q, -1, i))
        self.eps = {v: (1 if v % 2 == 0 else -1) for v in range(Lv)}

    def Bv(self, v):
        return zop(self.star[v])

    def nv(self, v):
        return (IDP - self.Bv(v)).smul(H2)

    def Aij(self, i, j):
        Lv = self.Lv
        if (i + 1) % Lv == j:
            return PS({((1 << i), (1 << ((i - 1) % Lv))): ONE})
        if (j + 1) % Lv == i:
            return PS({((1 << j), (1 << ((j - 1) % Lv))): MONE})
        raise KeyError((i, j))

    def Tij(self, i, j):
        return (self.Aij(i, j) * (self.Bv(i) - self.Bv(j))).smul(HI)

    def Kij(self, i, j):
        return (self.Aij(i, j) * (IDP - self.Bv(i) * self.Bv(j))).smul(MH)


GP = Geo((2, 2, 1))
GC = Geo((2, 2, 2))
GB = Geo((3, 3, 3))

print("H^g = -t sum eta (T C + K S)/2, C = U + U^dag, S = -i(U - U^dag); E|m> = m|m>, "
      "U|m> = |m+1>, |m| <= S; G_v = (div E)_v - rho_v")

# ============================ A -- the coupling on a compact U(1) link [exact]

LK = {S: linkops(S) for S in (1, 2)}

hop_ok = sign_ok = herm_ok = True
nmon = {}
nbond = 0
for g in (GP, GC, GB):
    for (i, j, e, ax, q) in g.bonds:
        T, K = g.Tij(i, j), g.Kij(i, j)
        aij = (T - K.smul(IMU)).smul(H2)              # a_i^dag a_j = (T - iK)/2
        aji = (T + K.smul(IMU)).smul(H2)              # a_j^dag a_i = (T + iK)/2
        for S in (1, 2):
            d, Em, U, Ud, C, Sm = LK[S]
            lhs = PM.kron(aij, U) + PM.kron(aji, Ud)  # a^dag U a + a^dag U^dag a
            rhs = (PM.kron(T, C) + PM.kron(K, Sm)).smul(H2)
            hop_ok = hop_ok and (lhs - rhs).iszero()
            herm_ok = herm_ok and (rhs - rhs.dag()).iszero()
            bad = (PM.kron(T, C)
                   + PM.kron(K, (1j * (U - Ud)).astype(np.complex128))).smul(H2)
            sign_ok = sign_ok and not (lhs - bad).iszero()
            nmon.setdefault(S, set()).add(rhs.nterms())
            nbond += 1

check("A1 [exact] a_i^dag U a_j + a_j^dag U^dag a_i = (T C + K S)/2, C = U + U^dag, "
      "S = -i(U - U^dag), Hermitian, %d and %d monomial entries: all %d bond checks -- every "
      "bond of the plaquette, the cube and the open 3x3x3 at S = 1 and 2"
      % (min(nmon[1]), min(nmon[2]), nbond),
      hop_ok and herm_ok and nmon[1] == {16} and nmon[2] == {32})

check("A2 [exact] the opposite-sign partner +i(U - U^dag) is not this hop on any of the %d: "
      "it is a_i^dag U^dag a_j + h.c., carrying flux the other way along the bond"
      % nbond, sign_ok)

# reduction to the landed spin-1/2 form: U = sigma^+ = (X + iY)/2
sx = np.array([[0, 1], [1, 0]], dtype=np.complex128)
sy = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
Up2 = (sx + 1j * sy) / 2
red = np.allclose(Up2 + Up2.conj().T, sx) and np.allclose(-1j * (Up2 - Up2.conj().T), sy)
check('A3 [exact] spin1/2 supplied #7893 identity: U=(X+iY)/2 gives C=X,S=Y and the same hop', red)

o1 = o2 = o3 = True
for (i, j, e, ax, q) in GC.bonds:
    T, K, ni, nj = GC.Tij(i, j), GC.Kij(i, j), GC.nv(i), GC.nv(j)
    o1 = o1 and (comm(ni, T) - K.smul(MI)).iszero() and (comm(ni, K) - T.smul(IMU)).iszero()
    o2 = o2 and (comm(nj, T) - K.smul(IMU)).iszero() and (comm(nj, K) - T.smul(MI)).iszero()
    for w in GC.V:
        if w in (i, j):
            continue
        o3 = o3 and comm(GC.nv(w), T).iszero() and comm(GC.nv(w), K).iszero()
check("A4 [exact] the relations behind gauge invariance, all 12 cube bonds: [n_i, T] = -iK, "
      "[n_i, K] = +iT, [n_j, T] = +iK, [n_j, K] = -iT, and [n_w, T] = [n_w, K] = 0 off the "
      "bond (96 pairs)", o1 and o2 and o3)

alg_ok = brk_ok = True
for S in (1, 2):
    d, Em, U, Ud, C, Sm = LK[S]
    I = np.eye(d, dtype=np.int64)
    Pp = np.diag([0] * (d - 1) + [1])
    Pm = np.diag([1] + [0] * (d - 1))
    alg_ok = alg_ok and np.array_equal(Em @ U - U @ Em, U) \
        and np.array_equal(Em @ Ud - Ud @ Em, -Ud) \
        and np.allclose(C, C.conj().T) and np.allclose(Sm, Sm.conj().T)
    brk_ok = brk_ok and np.array_equal(Ud @ U, I - Pp) and np.array_equal(U @ Ud, I - Pm) \
        and np.allclose(C @ Sm - Sm @ C, 2j * (Pp - Pm))
check('A5 [exact] [E,U]=U,[E,Udag]=-Udag and Hermitian C,S at S1/2; these commutators survive truncation', alg_ok)
check('A6 [exact] two listed defects: Udag U=I-P_+S,U Udag=I-P_-S and [C,S]=2i(P_+S-P_-S)!=0', brk_ok)

gauge_ok = True
npair = 0
zs = set()
for g, Ss in ((GP, (1, 2)), (GC, (1, 2)), (GB, (1, 2))):
    for v in g.V:
        zs.add(len(g.incs[v]))
    pre = {}
    for (i, j, e, ax, q) in g.bonds:
        pre[q] = (g.Tij(i, j), g.Kij(i, j), e)
    for S in Ss:
        d, Em, U, Ud, C, Sm = LK[S]
        hops = {q: (PM.kron(T, C) + PM.kron(K, Sm)).smul((Fr(-e, 2), Fr(0)))
                for q, (T, K, e) in pre.items()}
        for kind in ("sea", "stag"):
            for v in g.V:
                inc = {q: s for (q, s, w) in g.incs[v]}
                base = PM.eye(d, g.rho(v, kind)).smul(MONE)
                for q, hop in hops.items():
                    Gv = base
                    if q in inc:
                        Gv = Gv + PM.kron(IDP, (inc[q] * Em).astype(np.complex128))
                    gauge_ok = gauge_ok and pmcomm(Gv, hop).iszero()
                    if S == Ss[0] and kind == "sea":
                        npair += 1
check("A7 [exact] [G_v, H^g] = 0 at every corner of every coordination z = %s -- %d "
      "corner-bond pairs on the plaquette, the cube and the open 3x3x3, both rho conventions, "
      "S = 1 and 2" % (sorted(zs), npair), gauge_ok and sorted(zs) == [2, 3, 4, 5, 6] and npair == 1570)

# ================== B -- the integer flux selects the staggered convention

def nvec_table(g, nq, star, V):
    """n_v for every fermion record pattern, as an exact integer table."""
    N = 1 << nq
    f = np.arange(N, dtype=np.int64)
    out = np.zeros((N, len(V)), dtype=np.int64)
    for a, v in enumerate(V):
        m = star[v]
        p = np.zeros(N, dtype=np.int64)
        for k in range(nq):
            if m >> k & 1:
                p ^= ((f >> k) & 1)
        out[:, a] = p
    return out


def dp_census(nv, ends, vals, targets):
    """DP over links: count assignments of `vals` (DOUBLED link variables 2E_e)
       with prescribed doubled divergence.  Exact integer arithmetic."""
    rem = [0] * nv
    for (a, b) in ends:
        rem[a] += 1
        rem[b] += 1
    lo = [min(t[a] for t in targets) for a in range(nv)]
    hi = [max(t[a] for t in targets) for a in range(nv)]
    mx = max(abs(x) for x in vals)
    st = {tuple([0] * nv): 1}
    for (a, b) in ends:
        rem[a] -= 1
        rem[b] -= 1
        ns = {}
        for key, cnt in st.items():
            for m in vals:
                pa, pb = key[a] + m, key[b] - m
                if pa < lo[a] - rem[a] * mx or pa > hi[a] + rem[a] * mx:
                    continue
                if pb < lo[b] - rem[b] * mx or pb > hi[b] + rem[b] * mx:
                    continue
                nk = list(key)
                nk[a] = pa
                nk[b] = pb
                nk = tuple(nk)
                ns[nk] = ns.get(nk, 0) + cnt
        st = ns
    return {t: st.get(t, 0) for t in targets}


def full_census(nv, ends, vals, targets):
    """Complete vectorised enumeration of the whole link space."""
    nE = len(ends)
    d = len(vals)
    M = d ** nE
    conf = np.empty((M, nE), dtype=np.int64)
    t = np.arange(M, dtype=np.int64)
    va_ = np.array(vals, dtype=np.int64)
    for k in range(nE):
        conf[:, k] = va_[t % d]
        t //= d
    DIV = np.zeros((M, nv), dtype=np.int64)
    for k, (a, b) in enumerate(ends):
        DIV[:, a] += conf[:, k]
        DIV[:, b] -= conf[:, k]
    out = {}
    for tg in targets:
        out[tg] = int((DIV == np.array(tg)).all(axis=1).sum())
    return out


def keyed_census(nv, ends, vals, targets, half):
    """Complete vectorised enumeration of the whole link space, by histogram."""
    nE = len(ends)
    d = len(vals)
    M = d ** nE
    t = np.arange(M, dtype=np.int64)
    va_ = np.array(vals, dtype=np.int64)
    DIV = np.zeros((M, nv), dtype=np.int64)
    for k, (a, b) in enumerate(ends):
        col = va_[t % d]
        t //= d
        DIV[:, a] += col
        DIV[:, b] -= col
    W = 2 * half + 1
    key = np.zeros(M, dtype=np.int64)
    for a in range(nv):
        key = key * W + (DIV[:, a] + half)
    uq, ct = np.unique(key, return_counts=True)
    hist = dict(zip(uq.tolist(), ct.tolist()))
    out = {}
    for tg in targets:
        k = 0
        bad = False
        for x in tg:
            if abs(x) > half:
                bad = True
            k = k * W + (x + half)
        out[tg] = 0 if bad else int(hist.get(k, 0))
    return out


def cycle_census(nv, ends, vals, targets):
    """Complete enumeration over the cycle space: the spanning tree's link values
       are determined by the divergence, so only the nE - nv + 1 chords are free."""
    nE = len(ends)
    A = np.zeros((nv, nE), dtype=np.int64)
    for k, (a, b) in enumerate(ends):
        A[a, k] += 1
        A[b, k] -= 1
    adj = {a: [] for a in range(nv)}
    for k, (a, b) in enumerate(ends):
        adj[a].append((b, k))
        adj[b].append((a, k))
    seen = {0}
    tre = []
    stk = [0]
    while stk:
        a = stk.pop()
        for (b, k) in adj[a]:
            if b not in seen:
                seen.add(b)
                tre.append(k)
                stk.append(b)
    chords = [k for k in range(nE) if k not in set(tre)]
    # leaf-strip the tree to express x_tree = Mtree @ r exactly
    Mt = np.zeros((len(tre), nv), dtype=np.int64)
    R = np.eye(nv, dtype=np.int64)
    deg = {a: 0 for a in range(nv)}
    for k in tre:
        a, b = ends[k]
        deg[a] += 1
        deg[b] += 1
    live = set(tre)
    tix = {k: i for i, k in enumerate(tre)}
    while live:
        leaf = None
        for u in range(nv):
            if deg[u] == 1:
                leaf = u
                break
        k = next(k for k in live if leaf in ends[k])
        a, b = ends[k]
        w = b if a == leaf else a
        s = A[leaf, k]
        Mt[tix[k]] = s * R[leaf]
        R[w] = R[w] - A[w, k] * Mt[tix[k]]
        deg[leaf] -= 1
        deg[w] -= 1
        live.discard(k)
    Y = np.array(list(itertools.product(vals, repeat=len(chords))), dtype=np.int64)
    Ac = A[:, chords]
    Xy = Mt @ (Ac @ Y.T)                                  # (ntree, nY)
    B = np.array(targets, dtype=np.int64)
    Xb = Mt @ B.T                                         # (ntree, ntg)
    mx = max(abs(x) for x in vals)
    out = {}
    st = sorted(set(vals))
    for i, tg in enumerate(targets):
        if sum(tg) != 0:                       # any divergence sums to zero
            out[tg] = 0
            continue
        X = Xb[:, i][:, None] - Xy
        ok = (np.abs(X) <= mx)
        if len(st) != 2 * mx + 1:
            ok &= np.isin(X, st)
        out[tg] = int(ok.all(axis=0).sum())
    return out


def targets_of(g, kind, S=None):
    """doubled rho targets, one per fermion record pattern class."""
    V = list(g.V)
    NT = nvec_table(g, g.nq, g.star, V)
    if kind == "sea":
        RH = 2 * NT - 1
    else:
        RH = 2 * NT - np.array([1 - g.eps[v] for v in V])
    uq, inv, cts = np.unique(RH, axis=0, return_inverse=True, return_counts=True)
    return NT, [tuple(int(x) for x in r) for r in uq], inv, cts


def ends_of(g):
    vix = {v: a for a, v in enumerate(g.V)}
    return [(vix[i], vix[j]) for (i, j, e, ax, q) in g.bonds]


def sector(g, kind, S, method):
    NT, tg, inv, cts = targets_of(g, kind)
    vals = list(range(-2 * S, 2 * S + 1, 2))          # 2E for a compact link
    cnt = method(len(g.V), ends_of(g), vals, tg)
    per = np.array([cnt[t] for t in tg], dtype=np.int64)
    return NT, tg, inv, cts, per, int((per * cts).sum())

_, _, _, _, _, pl1 = sector(GP, "stag", 1, dp_census)
_, _, _, _, _, pl2 = sector(GP, "stag", 2, dp_census)
_, _, _, _, _, ps1 = sector(GP, "sea", 1, dp_census)
_, _, _, _, _, ps2 = sector(GP, "sea", 2, dp_census)
_, _, _, _, _, xl1 = sector(GP, "stag", 1, full_census)
_, _, _, _, _, xl2 = sector(GP, "stag", 2, full_census)
_, _, _, _, _, xs1 = sector(GP, "sea", 1, full_census)

check("B1 [exact] integer flux makes 2 (div E)_v EVEN at every corner of every coordination, "
      "while 2 rho^sea = 2n - 1 is ODD and 2 rho^stag = 2n - (1 - eps_v) is EVEN: z_v drops out "
      "of the condition, and staggered charge passes this LOCAL parity test; global solvability is separate",
      ps1 == 0 and ps2 == 0 and xs1 == 0 and pl1 > 0 and pl2 > 0)

check("B2 [exact] plaquette census, DP and complete enumeration agreeing: rho^sea 0 of "
      "16 x 81 and 0 of 16 x 625; rho^stag %d (S = 1) and %d (S = 2)" % (pl1, pl2),
      (pl1, pl2, xl1, xl2, ps1, xs1) == (26, 50, 26, 50, 0, 0))

NTc, tgc, invc, ctsc, perc1, cu1 = sector(GC, "stag", 1, dp_census)
_, _, _, _, perc2, cu2 = sector(GC, "stag", 2, dp_census)
_, _, _, _, _, cs1 = sector(GC, "sea", 1, dp_census)
_, _, _, _, _, cs2 = sector(GC, "sea", 2, dp_census)
_, _, _, _, _, yc1 = sector(GC, "stag", 1, cycle_census)
_, _, _, _, _, zc1 = sector(GC, "stag", 1,
                            lambda n, e, v, t: keyed_census(n, e, v, t, 6))
_, _, _, _, _, yc2 = sector(GC, "stag", 2, cycle_census)
_, _, _, _, _, ys1 = sector(GC, "sea", 1, cycle_census)

check("B3 [exact] cube census by DP and two complete enumerations (the whole 3^12 space at "
      "S = 1, the cycle space at both S), agreeing: rho^sea 0 and 0; rho^stag %d and %d. The "
      "cube is counted, never diagonalised" % (cu1, cu2),
      (cu1, cu2, yc1, yc2, zc1, cs1, cs2, ys1)
      == (102304, 1477920, 102304, 1477920, 102304, 0, 0, 0))

Ns = NTc.sum(axis=1)
adm1 = perc1[invc] > 0
adm2 = perc2[invc] > 0
h1, h2 = {}, {}
for a in range(len(tgc)):
    if perc1[a] > 0:
        h1[int(perc1[a])] = h1.get(int(perc1[a]), 0) + int(ctsc[a])
    if perc2[a] > 0:
        h2[int(perc2[a])] = h2.get(int(perc2[a]), 0) + int(ctsc[a])
cls1 = [h1[k] for k in sorted(h1)]
cls2 = [h2[k] for k in sorted(h2)]
check("B4 [exact] %d of the 4096 cube fermion patterns admit a link configuration -- exactly "
      "the half-filled N = 4 sector, all of it, at both S -- in EIGHT multiplicity classes of "
      "sizes %s, identical at S = 1 (counts %s) and S = 2 (%s): raising S re-weights the charge "
      "sectors, it does not re-partition them"
      % (int(adm1.sum()), cls1, sorted(h1), sorted(h2)),
      int(adm1.sum()) == 2240 and np.array_equal(adm1, adm2)
      and set(Ns[adm1]) == {4} and cls1 == cls2 == [128, 192, 416, 768, 128, 192, 384, 32]
      and sorted(h1) == [38, 39, 42, 44, 48, 50, 54, 69]
      and sorted(h2) == [616, 626, 642, 652, 672, 682, 702, 767])

# spin-1/2 links, by the same DP: 2E = +-1
def half_census(g, kind):
    NT, tg, inv, cts = targets_of(g, kind)
    cnt = dp_census(len(g.V), ends_of(g), [-1, 1], tg)
    per = np.array([cnt[t] for t in tg], dtype=np.int64)
    return int((per * cts).sum())

hcs, hcg = half_census(GC, "sea"), half_census(GC, "stag")
hps, hpg = half_census(GP, "sea"), half_census(GP, "stag")
check("B5 [exact] the same census on PR #7893's spin-1/2 link (2E = +-1) fixes which "
      "convention its original finite numbers belong to: the cube's %d is the SEA convention (staggered "
      "gives %d), the plaquette %d sea and %d staggered" % (hcs, hcg, hps, hpg), (hcs, hcg, hps, hpg) == (14400, 0, 0, 14))

def ring_census(Lv, S, kind):
    g = Ring(Lv)
    V = list(range(Lv))
    NT = nvec_table(g, Lv, g.star, V)
    RH = 2 * NT - (1 if kind == "sea" else np.array([1 - g.eps[v] for v in V]))
    uq, inv, cts = np.unique(RH, axis=0, return_inverse=True, return_counts=True)
    tg = [tuple(int(x) for x in r) for r in uq]
    ends = [(v, (v + 1) % Lv) for v in range(Lv)]
    a = dp_census(Lv, ends, list(range(-2 * S, 2 * S + 1, 2)), tg)
    b = full_census(Lv, ends, list(range(-2 * S, 2 * S + 1, 2)), tg)
    pa = np.array([a[t] for t in tg])
    pb = np.array([b[t] for t in tg])
    return int((pa * cts).sum()), int((pb * cts).sum())

rg8, rf8 = ring_census(8, 1, "stag")
rs8, _ = ring_census(8, 1, "sea")
check("B6 [exact] periodic ring L = 8, S = 1, DP and complete enumeration agreeing: rho^sea 0 "
      "of 256 x 3^8, rho^stag %d -- the same selection at coordination z = 2 with no face at "
      "all" % rg8, (rg8, rf8, rs8) == (234, 234, 0))

# the background link field that relates the two conventions
def bgfield(g):
    V = list(g.V)
    vix = {v: a for a, v in enumerate(V)}
    nv, nE = len(V), len(g.bonds)
    tgt = np.array([-g.eps[v] for v in V], dtype=np.int64)     # = 2 (div c)_v
    if tgt.sum() != 0:
        return None
    A = np.zeros((nv, nE), dtype=np.int64)
    for k, (i, j, e, ax, q) in enumerate(g.bonds):
        A[vix[i], k] = 1
        A[vix[j], k] = -1
    adj = {a: [] for a in range(nv)}
    for k in range(nE):
        a = int(np.nonzero(A[:, k] == 1)[0][0])
        b = int(np.nonzero(A[:, k] == -1)[0][0])
        adj[a].append((b, k))
        adj[b].append((a, k))
    seen = {0}
    order = [0]
    par = {}
    stk = [0]
    while stk:
        a = stk.pop()
        for (b, k) in adj[a]:
            if b not in seen:
                seen.add(b)
                par[b] = (a, k)
                order.append(b)
                stk.append(b)
    dvec = np.zeros(nE, dtype=np.int64)
    acc = tgt.copy()
    for b in reversed(order[1:]):
        a, k = par[b]
        val = acc[b] * A[b, k]
        dvec[k] = val
        acc[b] -= A[b, k] * val
        acc[a] -= A[a, k] * val
    return dvec if np.array_equal(A @ dvec, tgt) else None

bg = {}
for dims, nm in (((2, 2, 1), "plaquette"), ((2, 2, 2), "cube"),
                 ((2, 2, 3), "2x2x3"), ((3, 3, 3), "open 3x3x3")):
    g = Geo(dims)
    nev = sum(1 for v in g.V if g.eps[v] == 1)
    bg[nm] = (bgfield(g), nev, len(g.V) - nev)
mx = {nm: (None if d is None else int(np.abs(d).max())) for nm, (d, a, b) in bg.items()}
check("B7 [exact] rho^sea = rho^stag - eps_v/2, so the divergence equations agree in shifted "
      "variables when a background field c_e with (div c)_v = -eps_v/2 exists: it does "
      "on balanced blocks, c_e in {-1/2, 0, +1/2} (plaquette 2/2, cube 4/4, 2x2x3 6/6), and not "
      "on the open 3x3x3 (14/13, sum_v -eps_v = -1 while any divergence sums to 0)",
      mx["plaquette"] == mx["cube"] == mx["2x2x3"] == 1 and bg["open 3x3x3"][0] is None
      and bg["open 3x3x3"][1:] == (14, 13))

# Additional global-parity and changed-carrier boundaries; no large census needed.
odd_block = Geo((3, 3, 3))
all_stars = 0
for vertex in odd_block.V:
    all_stars ^= odd_block.star[vertex]
required_number = sum((1-odd_block.eps[v])//2 for v in odd_block.V)
check("B8 [exact boundary] open 3^3: product B_v=I permits even N, but zero total divergence demands N=13; staggered Gauss is empty for every integer window",
      all_stars == 0 and required_number == 13 and required_number % 2 == 1)
old_flux = [Fr(-1), Fr(0), Fr(1)]
shift = Fr(1,2)
shifted_flux = [e + shift for e in old_flux]
energy_change = [(e+shift)**2-e**2 for e in old_flux]
check("B9 [exact boundary] shift c=1/2 changes the S=1 carrier to {-1/2,1/2,3/2} and E^2 by {-3/4,1/4,5/4}; it is not the same integer-window Hamiltonian",
      shifted_flux == [Fr(-1,2), Fr(1,2), Fr(3,2)]
      and energy_change == [Fr(-3,4), Fr(1,4), Fr(5,4)]
      and all(de == 2*shift*e+shift**2 for e,de in zip(old_flux,energy_change)))

# ==================================== C -- the electric and magnetic terms

def gauss_basis(g, S, kind, qext=None):
    V = list(g.V)
    vix = {v: a for a, v in enumerate(V)}
    nv, nE = len(V), len(g.bonds)
    off = [(1 - g.eps[v]) // 2 for v in V]
    q0 = qext if qext is not None else [0] * nv
    bas = []
    for f in range(1 << g.nq):
        n = [pcnt(f & g.star[v]) & 1 for v in V]
        if kind == "sea":
            rr, sc = [2 * n[a] - 1 for a in range(nv)], 2
        else:
            rr, sc = [n[a] - off[a] + q0[a] for a in range(nv)], 1
        for m in itertools.product(range(-S, S + 1), repeat=nE):
            dv = [0] * nv
            for k, (i, j, e, ax, qq) in enumerate(g.bonds):
                dv[vix[i]] += m[k]
                dv[vix[j]] -= m[k]
            if all(sc * dv[a] == rr[a] for a in range(nv)):
                bas.append((f, m))
    return bas, {b: a for a, b in enumerate(bas)}


SPEC = {S: sorted(set(int(x) for x in np.diag(LK[S][1] @ LK[S][1]))) for S in (1, 2)}
check("C1 [exact] E_e^2 has spectrum %s at S = 1 and %s at S = 2, so H_E = (g^2/2) sum_e E_e^2 "
      "is a genuine operator -- contrast spin 1/2, where E_e^2 = I/4 and the electric term is a "
      "c-number that does nothing" % (SPEC[1], SPEC[2]), SPEC[1] == [0, 1] and SPEC[2] == [0, 1, 4])

pf_ok = True
compression_ok = True
npf = 0
nnz = {}
for g, nm in ((GP, "plaquette"), (GC, "cube")):
    for S in (1, 2):
        d = 2 * S + 1
        D = d ** 4
        for f in g.faces():
            fl = g.face_links(f)
            qs = [q for (q, s) in fl]
            ds = [s for (q, s) in fl]
            dec = np.empty((D, 4), dtype=np.int64)
            t = np.arange(D, dtype=np.int64)
            for k in range(4):
                dec[:, k] = (t % d) - S
                t //= d
            W = np.zeros((D, D), dtype=np.complex128)
            for a in range(D):
                nn = dec[a] + np.array(ds)
                if np.all(np.abs(nn) <= S):
                    b = 0
                    for k in range(3, -1, -1):
                        b = b * d + int(nn[k]) + S
                    W[b, a] = 1
            # Independent tensor compression of a shift on a larger flux window.
            # The one-step matrix elements coincide with P_S U_infinity P_S.
            larger_shift = np.eye(d + 2, k=-1, dtype=int)
            compressed = larger_shift[1:d+1, 1:d+1]
            tensor_W = np.array([[1]])
            for direction in reversed(ds):
                tensor_W = np.kron(tensor_W, compressed if direction == 1 else compressed.T)
            compression_ok &= np.array_equal(W, tensor_W)
            Pf = W + W.conj().T
            nnz.setdefault(S, set()).add(int((np.abs(Pf) > 0).sum()))
            for v in g.V:
                inc = {q: s for (q, s, w) in g.incs[v]}
                dg = dec @ np.array([inc.get(q, 0) for q in qs], dtype=np.int64)
                pf_ok = pf_ok and np.array_equal(Pf * dg[None, :], Pf * dg[:, None])
                if S == 1:
                    npf += 1
check("C2 [exact] the Wilson term commutes with Gauss's law: [P_f, (div E)_v] = 0 on all %d "
      "face-corner pairs (48 cube, 4 plaquette) at S = 1 and 2, nnz(P_f) = %d and %d; rho_v is "
      "fermion-only, so [P_f, rho_v] = 0 outright" % (npf, min(nnz[1]), min(nnz[2])),
      pf_ok and npf == 52 and nnz[1] == {32} and nnz[2] == {512})


def apply_H(g, S, f, m, t=1.0, g2=1.0, mag=True, elec=True):
    """H^g + H_E + H_B on one Gauss state, with destinations in the FULL space."""
    out = {}

    def add(k, c):
        out[k] = out.get(k, 0j) + c
    if elec:
        add((f, tuple(m)), (g2 / 2) * sum(x * x for x in m))
    for (i, j, e, ax, q) in g.bonds:
        for (Pop, sh) in ((g.Tij(i, j), {+1: 1.0 + 0j, -1: 1.0 + 0j}),
                          (g.Kij(i, j), {+1: -1j, -1: +1j})):
            for (x, z), (re, im) in Pop.items():
                c = complex(float(re), float(im)) * ((-1) ** pcnt(f & z))
                f2 = f ^ x
                for sgn, lc in sh.items():
                    m2 = list(m)
                    m2[q] += sgn
                    if -S <= m2[q] <= S:
                        add((f2, tuple(m2)), (-t * e / 2.0) * c * lc)
    if mag:
        for fc in g.faces():
            fl = g.face_links(fc)
            for dr in (+1, -1):
                m2 = list(m)
                ok = True
                for (q, s) in fl:
                    m2[q] += dr * s
                    if not (-S <= m2[q] <= S):
                        ok = False
                if ok:
                    add((f, tuple(m2)), -(1.0 / g2) * 0.5)
    return {k: v for k, v in out.items() if abs(v) > 1e-14}


leak_ok = True
leaks = 0
mxleak = 0.0
BAS = {}
for S in (1, 2):
    bas, ix = gauss_basis(GP, S, "stag")
    BAS[S] = (bas, ix)
    for (f, m) in bas:
        for k, v in apply_H(GP, S, f, m).items():
            if k not in ix:
                leaks += 1
                mxleak = max(mxleak, abs(v))
check("C3 [exact] the assembled H^g + H_E + H_B maps the plaquette Gauss sector into itself: "
      "on all %d states at S = 1 and %d at S = 2, destinations taken in the FULL space, %d "
      "out-of-sector amplitudes, max leaked %.1e -- the T C and K S terms leave the sector "
      "separately and cancel" % (len(BAS[1][0]), len(BAS[2][0]), leaks, mxleak), leaks == 0 and mxleak == 0.0)

# the Wilson potential's germ, exact Maclaurin coefficients of (1 - cos)/g^2
fact = [1]
for k in range(1, 12):
    fact.append(fact[-1] * k)
cos_c = [Fr((-1) ** (k // 2), fact[k]) if k % 2 == 0 else Fr(0) for k in range(9)]
Vc = [-c for c in cos_c]
Vc[0] = Fr(0)
germ_ok = (Vc[0] == 0 and Vc[1] == 0 and 2 * Vc[2] == 1
           and all(Vc[k] == 0 for k in (1, 3, 5, 7)))
check("C4 [exact] the separate untruncated scalar comparison V=(1-cos theta)/g^2, real g!=0, has a positive germ; no finite-matrix angle or photon derivation",
      germ_ok)

check("C5 [exact] each actual finite Wilson matrix equals the tensor compression of the untruncated shift; scalar-angle interpretation is a separate comparison", compression_ok)

# ============================= D -- the plaquette in its Gauss sector [numerical]

def build(g, S, bas, ix, t=1.0, g2=1.0, mag=True, elec=True):
    D = len(bas)
    H = np.zeros((D, D), dtype=np.complex128)
    for a, (f, m) in enumerate(bas):
        for k, v in apply_H(g, S, f, m, t=t, g2=g2, mag=mag, elec=elec).items():
            H[ix[k], a] += v
    return H


Vp = list(GP.V)
offp = [(1 - GP.eps[v]) // 2 for v in Vp]
rows = {}
herm = 0.0
for S in (1, 2):
    bas, ix = BAS[S]
    for g2 in (1.0, 2.0, 4.0):
        for mag in (False, True):
            H = build(GP, S, bas, ix, g2=g2, mag=mag)
            herm = max(herm, float(np.abs(H - H.conj().T).max()))
            w, vv = np.linalg.eigh(H)
            psi = vv[:, 0]
            pr = np.abs(psi) ** 2
            E2 = float(np.mean([sum(pr[a] * bas[a][1][q] ** 2 for a in range(len(bas)))
                                for q in range(len(GP.bonds))]))
            rv = np.array([sum(pr[a] * ((pcnt(bas[a][0] & GP.star[v]) & 1) - offp[b])
                               for a in range(len(bas))) for b, v in enumerate(Vp)])
            Ee = np.array([sum(pr[a] * bas[a][1][q] for a in range(len(bas)))
                           for q in range(len(GP.bonds))])
            Nv = sum(pr[a] * sum((pcnt(bas[a][0] & GP.star[v]) & 1) for v in Vp)
                     for a in range(len(bas)))
            Hb = build(GP, S, bas, ix, t=0.0, g2=1.0, mag=True, elec=False)
            cf = float(np.real(psi.conj() @ (-Hb) @ psi)) / len(GP.faces())
            rows[(S, g2, mag)] = (float(w[0]), float(w[1] - w[0]), E2, cf,
                                  rv, Ee, float(Nv))

TOL = 1e-9


def close(a, b, tol=TOL):
    return abs(a - b) < tol


e1 = [rows[(1, g2, m)][0] for g2 in (1.0, 2.0, 4.0) for m in (False, True)]
e2 = [rows[(2, g2, m)][0] for g2 in (1.0, 2.0, 4.0) for m in (False, True)]
tgt1 = [-2.152011641, -2.491847562, -1.807850741, -1.889262585,
        -1.352280241, -1.364473432]
tgt2 = [-2.153356887, -2.573395352, -1.807956223, -1.899005796,
        -1.352283081, -1.365185023]
check("D1 [numerical 1e-9] raw plaquette Gauss dimensions %d and %d before +code projection; E_0 at g^2 = 1, 2, 4 without/with H_B: S = 1 %s; S = 2 %s"
      % (len(BAS[1][0]), len(BAS[2][0]),
         " ".join("%.6f" % x for x in e1), " ".join("%.6f" % x for x in e2)),
      len(BAS[1][0]) == 26 and len(BAS[2][0]) == 50
      and all(close(a, b) for a, b in zip(e1, tgt1))
      and all(close(a, b) for a, b in zip(e2, tgt2)))

gapsF = [rows[(S, g2, False)][1] for S in (1, 2) for g2 in (1.0, 2.0, 4.0)]
cosF = [rows[(S, g2, False)][3] for S in (1, 2) for g2 in (1.0, 2.0, 4.0)]
gapsT = [rows[(S, g2, True)][1] for S in (1, 2) for g2 in (1.0, 2.0, 4.0)]
cosT = [rows[(S, g2, True)][3] for S in (1, 2) for g2 in (1.0, 2.0, 4.0)]
check("D2 [numerical 1e-9] raw-sector gaps and selected eigh ground-vector cosine are zero without H_B; "
      "with H_B gaps=%s, cosine=%s at the three tested couplings; no all-ground or limiting claim"
      % (" ".join("%.6f" % x for x in gapsT), " ".join("%.6f" % x for x in cosT)),
      all(abs(x) < TOL for x in gapsF) and all(abs(x) < TOL for x in cosF)
      and all(close(a, b) for a, b in zip(
          gapsT, [0.395359309, 0.110635103, 0.017047410,
                  0.411730513, 0.114075109, 0.017219995]))
      and all(close(a, b) for a, b in zip(
          cosT, [0.418514989, 0.210242684, 0.063343275,
                 0.541713235, 0.244706153, 0.068692838])))

E2T = [rows[(S, g2, True)][2] for S in (1, 2) for g2 in (1.0, 2.0, 4.0)]
E2F = [rows[(S, g2, False)][2] for S in (1, 2) for g2 in (1.0, 2.0, 4.0)]
sh = abs(rows[(2, 1.0, True)][0] - rows[(1, 1.0, True)][0]) / abs(rows[(1, 1.0, True)][0])
check("D3 [numerical 1e-6] <E_e^2> at S = 1 is %s without H_B and %s with it: the flux window "
      "is barely used, and the S = 1 to S = 2 shift in E_0 is %.2f%% at g^2 = 1 with H_B, so convergence in S has not been established for these g^2=1 data"
      % (" ".join("%.6f" % x for x in E2F[:3]), " ".join("%.6f" % x for x in E2T[:3]),
         100 * sh),
      all(close(a, b, 1e-6) for a, b in zip(E2F, [0.205293, 0.145868, 0.089108,
                                                  0.207299, 0.145984, 0.089111]))
      and all(close(a, b, 1e-6) for a, b in zip(E2T, [0.289139, 0.168525, 0.091811,
                                                      0.332564, 0.172734, 0.092001])))

rv4 = rows[(2, 4.0, True)][4]
mxr = [float(np.abs(rows[(1, g2, True)][4]).max()) for g2 in (1.0, 2.0, 4.0)]
epsp = np.array([GP.eps[v] for v in Vp], dtype=float)
check("D4 [numerical 1e-9] the coupled sea is NOT locally neutral: <rho_v> = %s at g^2 = 4 with "
      "H_B, S = 2. the computed pattern is +a -a -a +a with vanishing total; no bare C_4 symmetry proof; "
      "a decreases over the tested couplings (max |<rho_v>| = %s at g^2 = 1, 2, 4, S = 1); "
      "<N> = 2 and Hermiticity residual %.1e"
      % (" ".join("%+.9f" % x for x in rv4), " ".join("%.3f" % x for x in mxr), herm),
      close(abs(rv4[0]), 0.180762247) and abs(rv4.sum()) < TOL
      and np.allclose(rv4, abs(rv4[0]) * epsp, atol=TOL)
      and all(close(a, b, 1e-3) for a, b in zip(mxr, [0.426, 0.305, 0.181]))
      and close(rows[(2, 4.0, True)][6], 2.0) and herm == 0.0)

Sf = mono(GP.L.loop([Vp[0], GP.L.step(Vp[0], EX[0]),
                     GP.L.step(GP.L.step(Vp[0], EX[0]), EX[1]),
                     GP.L.step(Vp[0], EX[1])]))
Msf = psmat(Sf, GP.nq)
dcode = []
CODE = {}
for S in (1, 2):
    bas, ix = BAS[S]
    Pr = np.zeros((len(bas), len(bas)), dtype=np.complex128)
    for a, (f, m) in enumerate(bas):
        col = Msf[:, f]
        for f2 in np.nonzero(np.abs(col) > 1e-12)[0]:
            k = ix.get((int(f2), m))
            if k is not None:
                Pr[k, a] += col[f2]
    w, vectors = np.linalg.eigh((Pr + Pr.conj().T) / 2)
    CODE[S] = (Pr, vectors[:, w > 0.5], vectors[:, w < -0.5])
    dcode.append(int(round(sum(1 for x in w if x > 0.5))))
check("D5 [numerical 1e-9] the face stabiliser splits the plaquette Gauss sector in half, "
      "26 = 13 + 13 and 50 = 25 + 25, so dim(Gauss and code) = %d and %d (spin 1/2 gave "
      "14 = 7 + 7)" % (dcode[0], dcode[1]),
      dcode == [13, 25])

# Independent ordinary occupation/flux construction, without BK operators or masks.
def occupation_flux_plaquette(S, magnetic):
    vertices = list(itertools.product(range(2), repeat=2))
    vi = {v:k for k,v in enumerate(vertices)}
    edges = []
    for v in vertices:
        for axis in range(2):
            w = list(v); w[axis] += 1; w = tuple(w)
            if w in vi:
                edges.append((vi[v], vi[w], (-1)**sum(v[:axis])))
    ei = {(i,j):q for q,(i,j,eta) in enumerate(edges)}
    cycle = [vi[(0,0)], vi[(1,0)], vi[(1,1)], vi[(0,1)]]
    face = [(ei[(i,j)],1) if (i,j) in ei else (ei[(j,i)],-1)
            for i,j in zip(cycle,cycle[1:]+cycle[:1])]
    basis = []
    for occupation in range(16):
        if occupation.bit_count() % 2:
            continue
        charge = [((occupation>>i)&1)-sum(v)%2 for i,v in enumerate(vertices)]
        for flux in itertools.product(range(-S,S+1),repeat=4):
            divergence = [0]*4
            for q,(i,j,eta) in enumerate(edges):
                divergence[i] += flux[q]; divergence[j] -= flux[q]
            if divergence == charge:
                basis.append((occupation,flux))
    index = {b:a for a,b in enumerate(basis)}
    ham = np.zeros((len(basis),len(basis)),complex)
    cosine = np.zeros_like(ham)
    for a,(occupation,flux) in enumerate(basis):
        ham[a,a] = sum(e*e for e in flux)/2
        for q,(i,j,eta) in enumerate(edges):
            for dst,src,direction in ((i,j,1),(j,i,-1)):
                if (occupation>>src)&1 and not (occupation>>dst)&1:
                    sign = (-1)**((occupation&((1<<src)-1)).bit_count())
                    n = occupation ^ (1<<src)
                    sign *= (-1)**((n&((1<<dst)-1)).bit_count())
                    n ^= 1<<dst
                    m = list(flux); m[q] += direction
                    if abs(m[q]) <= S:
                        ham[index[(n,tuple(m))],a] -= eta*sign
        for direction in (-1,1):
            m = list(flux)
            for q,orientation in face:
                m[q] += direction*orientation
            if all(abs(e)<=S for e in m):
                cosine[index[(occupation,tuple(m))],a] += 0.5
    return basis, ham-cosine if magnetic else ham, cosine

code_equivalence = True
code_gap_ok = True
ground_boundary_ok = True
gap_reference = {(1,False):0.978328969369697, (1,True):1.787323468929332,
                 (2,False):0.956978271110297, (2,True):1.687818382305960}
for S in (1,2):
    bas, ix = BAS[S]
    stabilizer, plus, minus = CODE[S]
    # Pick one normalized +1 vector per ordinary occupation/flux basis state.
    columns = {}
    for a,(f,flux) in enumerate(bas):
        occupation = sum((pcnt(f&GP.star[v])&1)<<k for k,v in enumerate(Vp))
        key = (occupation,flux)
        if key not in columns:
            z = np.eye(len(bas),dtype=complex)[:,a] + stabilizer[:,a]
            columns[key] = z / np.linalg.norm(z)
    cosine = -build(GP,S,bas,ix,t=0,g2=1,mag=True,elec=False)
    for magnetic in (False,True):
        fock_basis, fock_H, fock_cosine = occupation_flux_plaquette(S,magnetic)
        embedding = np.column_stack([columns[b] for b in fock_basis])
        H = build(GP,S,bas,ix,g2=1,mag=magnetic)
        encoded_H = embedding.conj().T @ H @ embedding
        encoded_cosine = embedding.conj().T @ cosine @ embedding
        # Solve a diagonal basis-phase convention, then check EVERY matrix entry.
        phases = np.zeros(len(fock_basis),complex)
        for start in range(len(phases)):
            if phases[start] != 0:
                continue
            phases[start] = 1
            pending = [start]
            while pending:
                i = pending.pop()
                for j in np.flatnonzero(np.abs(encoded_H[i]) > 1e-12):
                    if i != j and phases[j] == 0:
                        phases[j] = phases[i]*fock_H[i,j]/encoded_H[i,j]
                        pending.append(int(j))
        phase_matrix = np.diag(phases)
        residual = max(float(np.max(np.abs(phase_matrix.conj().T@encoded_H@phase_matrix-fock_H))),
                       float(np.max(np.abs(phase_matrix.conj().T@encoded_cosine@phase_matrix-fock_cosine))))
        ew, ev = np.linalg.eigh(plus.conj().T@H@plus)
        minus_w = np.linalg.eigvalsh(minus.conj().T@H@minus)
        fock_w = np.linalg.eigvalsh(fock_H)
        code_equivalence &= (len(fock_basis)=={1:13,2:25}[S] and residual < 1e-10
            and np.max(np.abs(np.abs(phases)-1)) < 1e-10
            and np.max(np.abs(embedding.conj().T@embedding-np.eye(len(fock_basis)))) < 1e-10
            and np.max(np.abs(stabilizer@embedding-embedding)) < 1e-10
            and np.max(np.abs(H@stabilizer-stabilizer@H)) < 1e-10
            and np.max(np.abs(ew-fock_w)) < 1e-10
            and np.max(np.abs(np.sort(np.r_[ew,minus_w])-np.linalg.eigvalsh(H))) < 1e-10)
        code_gap_ok &= abs(ew[1]-ew[0]-gap_reference[(S,magnetic)]) < 1e-10
        psi = plus@ev[:,0]
        code_cosine = float(np.real(psi.conj()@cosine@psi))
        print("CODE S=%d magnetic=%s dim=%d E0=%.12f gap=%.12f cos=%.12f intertwiner=%.1e"
              % (S,magnetic,len(ew),ew[0],ew[1]-ew[0],code_cosine,residual))
        if not magnetic:
            raw_w,raw_v = np.linalg.eigh(H)
            ground = raw_v[:,np.abs(raw_w-raw_w[0])<1e-9]
            ground_cosine = ground.conj().T@cosine@ground
            cw,cv = np.linalg.eigh(ground_cosine)
            balanced = ground@(cv[:,0]+cv[:,-1])/np.sqrt(2)
            ground_boundary_ok &= (ground.shape[1]==2 and cw[0] < -0.2 and cw[-1]>0.2
                and abs(cw.sum())<1e-10 and abs(np.trace(ground_cosine)/2)<1e-10
                and abs(balanced.conj()@cosine@balanced)<1e-10)
            print("RAW GROUND S=%d cos range=[%.12f,%.12f]; uniform mixture and one balanced pure state give zero"%(S,cw[0],cw[-1]))
check("D6 [numerical 1e-10] actual +code matrices and cosine are unitarily equivalent to independent even-Fock/flux matrices; raw spectrum is the union of both loop sectors",code_equivalence)
check("D7 [numerical 1e-10] +code gaps at g^2=1 match the four predeclared references; raw zero gaps are not physical code gaps",code_gap_ok)
check("D8 [boundary] no-H_B degenerate raw ground space supports opposite nonzero cosine expectations; zero is not state-independent",ground_boundary_ok)

# ============================================== E -- the ring [exact + numerical]

def ring_parity(Lv):
    """which total fermion numbers the superfast ring encoding realises."""
    g = Ring(Lv)
    N = 1 << Lv
    f = np.arange(N, dtype=np.int64)
    tot = np.zeros(N, dtype=np.int64)
    for v in range(Lv):
        m = g.star[v]
        p = np.zeros(N, dtype=np.int64)
        for k in range(Lv):
            if m >> k & 1:
                p ^= ((f >> k) & 1)
        tot += p
    return sorted(set(int(x) % 2 for x in tot))


ring_alg = True
gr = Ring(8)
for (i, j, e, ax, q) in gr.bonds:
    A, T, K = gr.Aij(i, j), gr.Tij(i, j), gr.Kij(i, j)
    ring_alg = ring_alg and acomm(A, gr.Bv(i)).iszero() and acomm(A, gr.Bv(j)).iszero() \
        and (A * A - IDP).iszero() \
        and (comm(gr.nv(i), T) - K.smul(MI)).iszero() \
        and (comm(gr.nv(i), K) - T.smul(IMU)).iszero()
    for w in gr.V:
        if w in (i, j):
            continue
        ring_alg = ring_alg and comm(gr.nv(w), T).iszero() and comm(gr.nv(w), K).iszero()
par = {Lv: ring_parity(Lv) for Lv in (4, 6, 8)}
check("E1 [exact] the ring's hand-rolled superfast encoding satisfies the same relations "
      "({A, B_i} = 0, A^2 = I, [n_i, T] = -iK, [n_i, K] = +iT, [n_w, T] = 0 off the bond) and "
      "realises ONLY EVEN total fermion number at L = 4, 6, 8; half filling needs N = L/2, so "
      "L = 0 mod 4 and L = 6 has an empty Gauss sector",
      ring_alg and par[4] == par[6] == par[8] == [0])


def pure_electric(Lv, d, g2, S=1):
    best = None
    q = [0] * Lv
    if d > 0:
        q[0], q[d] = +1, -1
    for m in itertools.product(range(-S, S + 1), repeat=Lv):
        if [m[v] - m[(v - 1) % Lv] for v in range(Lv)] != q:
            continue
        E = Fr(g2, 2) * sum(x * x for x in m)
        best = E if best is None else min(best, E)
    return best


pe_ok = True
pev = {}
for g2 in (1, 4):
    b0 = pure_electric(8, 0, g2)
    for d in range(5):
        V = pure_electric(8, d, g2) - b0
        pev[(g2, d)] = V
        pe_ok = pe_ok and V == Fr(g2, 2) * d
check("E2 [exact] pure electric, no fermion, static +1 and -1 charges on the L = 8 ring at "
      "S = 1: V(d) = (g^2/2) d EXACTLY in rational arithmetic for d = 0..4 at g^2 = 1 and 4 -- "
      "a string whose energy grows linearly with the separation; S = 1 is already exact, the "
      "minimiser using only E in {0, 1}", pe_ok)


def ring_basis(g, S, qext):
    Lv = g.Lv
    off = [(1 - g.eps[v]) // 2 for v in range(Lv)]
    bas = []
    for f in range(1 << Lv):
        n = [pcnt(f & g.star[v]) & 1 for v in range(Lv)]
        rho = [n[v] - off[v] + qext[v] for v in range(Lv)]
        if sum(rho) != 0:
            continue
        ps_, acc = [0] * Lv, 0
        for v in range(Lv):
            acc += rho[v]
            ps_[v] = acc
        lo = max(-S - x for x in ps_)
        hi = min(S - x for x in ps_)
        for c in range(int(np.ceil(lo)), int(np.floor(hi)) + 1):
            bas.append((f, tuple(c + x for x in ps_)))
    return bas, {b: a for a, b in enumerate(bas)}


def ring_H(g, S, bas, ix, t, g2):
    D = len(bas)
    H = np.zeros((D, D), dtype=np.complex128)
    for a, (f, m) in enumerate(bas):
        H[a, a] += (g2 / 2) * sum(x * x for x in m)
    if t:
        for (i, j, e, ax, q) in g.bonds:
            for (Pop, sh) in ((g.Tij(i, j), {+1: 1.0 + 0j, -1: 1.0 + 0j}),
                              (g.Kij(i, j), {+1: -1j, -1: +1j})):
                for (x, z), (re, im) in Pop.items():
                    cc = complex(float(re), float(im))
                    for a, (f, m) in enumerate(bas):
                        c = cc * ((-1) ** pcnt(f & z))
                        f2 = f ^ x
                        for sgn, lc in sh.items():
                            m2 = list(m)
                            m2[q] += sgn
                            if not (-S <= m2[q] <= S):
                                continue
                            k = ix.get((f2, tuple(m2)))
                            if k is not None:
                                H[k, a] += (-t * e / 2.0) * c * lc
    return H


def ring_run(Lv, g2, ds, want=None):
    g = Ring(Lv)
    out = {}
    for d in ds:
        q = [0] * Lv
        if d > 0:
            q[0], q[d] = +1, -1
        bas, ix = ring_basis(g, 1, q)
        H = ring_H(g, 1, bas, ix, 1.0, g2)
        w, vv = np.linalg.eigh(H)
        psi = vv[:, 0]
        pr = np.abs(psi) ** 2
        Ee = np.array([sum(pr[a] * bas[a][1][q2] for a in range(len(bas)))
                       for q2 in range(Lv)])
        nvv = np.array([sum(pr[a] * (pcnt(bas[a][0] & g.star[v]) & 1)
                            for a in range(len(bas))) for v in range(Lv)])
        out[d] = (float(w[0]), len(bas), Ee, nvv, float(nvv.sum()),
                  float(np.abs(H - H.conj().T).max()))
    return out


r1 = ring_run(8, 1.0, range(5))
r4 = ring_run(8, 4.0, range(5))
V4 = [r4[d][0] - r4[0][0] for d in range(1, 5)]
V1 = [r1[d][0] - r1[0][0] for d in range(1, 5)]
dims8 = [r4[d][1] for d in range(5)]
check("E3 [numerical 1e-9] with the fermion hop at half filling (t = 1) the finite raw-sector potential screens relative to pure electric: at "
      "g^2 = 4 the potential is %s against the unbroken 2, 4, 6, 8, and it is not monotone -- "
      "V(4) < V(3) at g^2 = 1 too (%s against 0.5, 1.0, 1.5, 2.0); raw Gauss dimensions %s, <N> = 4 "
      "exactly at every separation" % (" ".join("%.6f" % x for x in V4),
                                       " ".join("%.6f" % x for x in V1), dims8),
      all(close(a, b) for a, b in zip(V4, [2.271563007, 2.383425096,
                                           4.295401559, 2.819090192]))
      and all(close(a, b) for a, b in zip(V1, [0.796888158, 0.796906164,
                                               1.277804351, 1.026768433]))
      and dims8 == [234, 150, 160, 132, 150]
      and all(close(r4[d][4], 4.0) for d in range(5)))

Ee4 = r4[4][2]
nv4 = r4[4][3]
check("E4 [numerical 1e-4] the mechanism, off the d = 4 ground state at g^2 = 4: the flux does "
      "not span the separation but localises on the sources, sum_e |<E_e>| = %.3f against 4 "
      "unbroken, dying to %.4f three links away; the screening charge shows as a HOLE "
      "<n> = %.3f at the +1 source and a fermion <n> = %.3f at the -1 source"
      % (float(np.abs(Ee4).sum()), abs(float(Ee4[3])), float(nv4[0]), float(nv4[4])),
      close(float(np.abs(Ee4).sum()), 1.6032, 1e-4)
      and close(float(nv4[0]), 0.1805, 1e-4) and close(float(nv4[4]), 0.9811, 1e-4)
      and abs(float(Ee4[3])) < 0.01)

s1 = ring_run(4, 1.0, range(3))
s4 = ring_run(4, 4.0, range(3))
W1 = [s1[d][0] - s1[0][0] for d in (1, 2)]
W4 = [s4[d][0] - s4[0][0] for d in (1, 2)]
check("E5 [numerical 1e-6] finite-size cross-check on the L = 4 ring: V = %s at g^2 = 1 and %s "
      "at g^2 = 4, against the pure-electric 0.5, 1.0 and 2.0, 4.0 -- saturated there too, so "
      "this finite comparison occurs at both lengths; the values are finite-size numbers and carry no "
      "infinite-volume statement"
      % (" ".join("%.6f" % x for x in W1), " ".join("%.6f" % x for x in W4)),
      all(close(a, b, 1e-6) for a, b in zip(W1, [0.762517, 0.594051]))
      and all(close(a, b, 1e-6) for a, b in zip(W4, [2.271118, 2.169659]))
      and s1[0][1] == 26)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(1 if FAIL else 0)
