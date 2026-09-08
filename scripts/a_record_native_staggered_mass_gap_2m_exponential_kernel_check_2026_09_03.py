#!/usr/bin/env python3
"""A supplied staggered mass in a finite Pauli/one-particle model.

Self-contained finite-cluster runner.  The coarse lattice is 2Z^3, one
fermionic mode per coarse vertex in the Bravyi-Kitaev superfast encoding
written on it, with the Kawamoto-Smit link signs
    eta_1 = 1,  eta_2(v) = (-1)^{v_1},  eta_3(v) = (-1)^{v_1+v_2}.
The object declared and tested here is the staggered mass term
    H_m = m sum_v eps_v n_v,   eps_v = (-1)^{v_1+v_2+v_3},  n_v = (1 - B_v)/2,
whose coefficient m the law does not fix.

  A  RECORD-NATIVE FORM.  H_m = -(m/2) sum_v eps_v B_v + (m/2)(sum_v eps_v) I:
     a pure Z-product on the six edge sites at each corner, diagonal in the
     code-qubit Z basis (no permanent Record instrument derived), commuting with every face stabilizer, every B_w and the
     Wilson lines, with the exact hop commutator [H_m, T_ij] = m (eps_j -
     eps_i) T_ij B_j on every bond.
  B  SYMMETRY.  Invariant under coarse translations of even coordinate sum and
     under all 24 proper corner rotations; odd translations send H_m -> -H_m.
  C  SPECTRUM.  {M, Eps} = 0, so (M + m Eps)^2 = M^2 + m^2 and the spectrum is
     +-sqrt(E_0^2 + m^2); balanced bipartite SVD pairs signs; a node gaps to 2|m|.
  D  TASTE.  U Eps U^dag = -+ I (x) Y_A (x) I: chirality-odd and taste-singlet.
  E  THE MASSIVE SEA.  <n_v> = 1/2 - (m/2) eps_v c(m) and the condensate
     C(m) = -m c(m)/2, exact on the antiperiodic 4^3.
  F  KERNEL DECAY.  Finite m=0 slope and m={.2,.5,1} exponential fits, compared with
     the branch-point scale xi = 2/arccosh(1 + m^2/2), not a limit theorem.
  G  SECTOR SELECTION.  Only KS versus plain sectors at the listed finite masses/twists/grids.
  H  CONJUGATION.  eps (M + m Eps) eps = -(M - m Eps): +-m are exchanged.

Groups A and B are exact symplectic Pauli algebra (F2 supports, Z4 phases);
C, G and H carry exact algebraic content with floating-point cross-checks at
the stated tolerance; D, E and F are numerical at the stated tolerance, the
decay lengths being fits.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import hashlib
from pathlib import Path
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md')
INPUT_SHA256 = {'docs/A_RECORD_NATIVE_STAGGERED_MASS_GAP_2M_EXPONENTIAL_KERNEL_AND_WHAT_IT_BREAKS_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'd77b18f545085aecba6ce4644c6913f0845682e7a3646fa5411330f63b8a2b68', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md': '67ad0284ca494a4fc82c37dae248a70eb5f84b59d4fad101b0e076122f066d90'}

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


def verify_inputs():
    """Bind final prose and exact quoted context; no parent science is executed."""
    root = Path(__file__).resolve().parents[1]
    for relative, expected in INPUT_SHA256.items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError("missing or changed declared input: " + relative)
    return True


check("Z1 [input identity] final own-note/current memo/quoted gate pinned; no parent campaign approval", verify_inputs())


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

    def scal(s, t):
        return Q(s.k + t, s.x, s.z)

    def neg(s):
        return Q(s.k + 2, s.x, s.z)


def qprod(seq):
    o = Q(0, 0, 0)
    for p in seq:
        o = o * p
    return o


def commutes_mono(p, q):
    return ((pcnt(p.x & q.z) + pcnt(p.z & q.x)) & 1) == 0


class PS(dict):
    """sum_j c_j P_j with P_j = X^x Z^z keyed (x, z); i-powers folded into c."""

    def __add__(a, b):
        o = PS(a)
        for k, v in b.items():
            o[k] = o.get(k, 0) + v
            if o[k] == 0:
                del o[k]
        return o

    def __sub__(a, b):
        return a + b.smul(-1)

    def smul(a, s):
        return PS({k: s * v for k, v in a.items() if s * v != 0})

    def __mul__(a, b):
        o = PS()
        for (x1, z1), c1 in a.items():
            for (x2, z2), c2 in b.items():
                k = (x1 ^ x2, z1 ^ z2)
                c = c1 * c2 * (1j) ** ((2 * pcnt(z1 & x2)) & 3)
                o[k] = o.get(k, 0) + c
                if o[k] == 0:
                    del o[k]
        return o

    def iszero(a):
        return len(a) == 0


def mono(q, c=1):
    return PS({(q.x, q.z): c * (1j) ** q.k})


def comm(a, b):
    return a * b - b * a


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


def massterm(L, m=1):
    """H_m = -(m/2) sum_v eps_v B_v, the record-native staggered mass."""
    H = PS()
    for v in L.V:
        H = H + PS({(0, L.star[v]): -0.5 * m * eps_of(v)})
    return H


def Tij(L, i, j):
    """T_ij = (i/2) A_ij (B_i - B_j)."""
    A = mono(L.Aij(i, j))
    Bi = PS({(0, L.star[i]): 1})
    Bj = PS({(0, L.star[j]): 1})
    return (A * (Bi - Bj)).smul(0.5j)


# ============================================ one-particle matrices, quadrature

def build(L, twist=(0, 0, 0), plain=False):
    """One-particle hopping M on the coarse L^3 torus, with Eps = diag(eps_v)."""
    idx = {}
    sites = []
    for v in itertools.product(range(L), repeat=3):
        idx[v] = len(sites)
        sites.append(v)
    M = np.zeros((L ** 3, L ** 3))
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % L for i in range(3))
            s = 1 if plain else eta_ks(v, a)
            if twist[a] and v[a] == L - 1:
                s = -s
            M[idx[w], idx[v]] += s
            M[idx[v], idx[w]] += s
    eps = np.array([eps_of(v) for v in sites], float)
    return M, sites, idx, eps


def Esea(lam, m):
    return -0.5 * float(np.sum(np.sqrt(lam * lam + m * m)))


def best_twist(L, m, plain=False):
    best = None
    for tw in itertools.product((0, 1), repeat=3):
        E = Esea(np.linalg.eigvalsh(build(L, tw, plain=plain)[0]), m)
        if best is None or E < best[1] - 1e-12:
            best = (tw, E)
    return best


def bloch_moments(m, N=200, plain=False):
    """<sqrt(E0^2+m^2)>, <(E0^2+m^2)^-1/2>, <E0^2>, <E0^4> on a midpoint grid."""
    q = 2 * np.pi * (np.arange(N) + 0.5) / N
    if plain:
        c = 2 * np.cos(q)
        x = (c[:, None, None] + c[None, :, None] + c[None, None, :]) ** 2
    else:
        c = np.cos(q)
        x = 6 + 2 * (c[:, None, None] + c[None, :, None] + c[None, None, :])
    s = np.sqrt(x + m * m)
    return float(s.mean()), float((1.0 / s).mean()), float(x.mean()), float((x * x).mean())


# ==================================================== A -- record-native form

for tag, L, per in (("torus 4^3", Lat((4, 4, 4), True), True),
                    ("open 3x3x3", Lat((3, 3, 3), False), False)):
    H = massterm(L)
    seps = sum(eps_of(v) for v in L.V)
    terms = [Q(0, 0, z) for (x, z) in H]
    diag = all(x == 0 for (x, z) in H)
    supp = sorted(set(pcnt(z) for (x, z) in H))
    fz = [L.loop(f) for f in L.faces()]
    Bw = [Q(0, 0, L.star[w]) for w in L.V]
    cf = all(commutes_mono(t, s) for t in terms for s in fz)
    cb = all(commutes_mono(t, b) for t in terms for b in Bw)
    if per:
        wl = [L.loop([tuple((k if a == ax else 0) for a in range(3))
                      for k in range(L.dims[ax])]) for ax in range(3)]
        cw = all(commutes_mono(t, w) for t in terms for w in wl)
        check("A1 [exact] 4^3: H_m = -(m/2) sum eps_v B_v + (m/2)(sum eps)I, diagonal, 6-edge "
              "corner stars; commutes with %d S_f (%d pairs), %d B_w, 3 lines; sum eps = %d"
              % (len(fz), len(terms) * len(fz), len(Bw), seps),
              diag and supp == [6] and cf and cb and cw and seps == 0)
    else:
        check("A2 [exact] open 3x3x3: same form, star-local (supports %s); commutes with %d S_f (%d "
              "pairs), %d B_w; sum eps = %+d, constant +m/2"
              % (supp, len(fz), len(terms) * len(fz), len(Bw), seps),
              diag and max(supp) == 6 and cf and cb and seps == 1)

L4 = Lat((4, 4, 4), True)
H4 = massterm(L4, 1)
ok_all = True
nz = 0
for i in L4.V:
    for ax in range(3):
        j = wrap(va(i, EX[ax]), L4.dims)
        T = Tij(L4, i, j)
        C = comm(H4, T)
        Bj = PS({(0, L4.star[j]): 1})
        ok_all = ok_all and (C - (T * Bj).smul(eps_of(j) - eps_of(i))).iszero()
        if not C.iszero():
            nz += 1
check("A3 [exact, m = 1, linear in m] all %d bonds of 4^3: [H_m, T_ij] = m (eps_j - eps_i) "
      "T_ij B_j, nonzero for m != 0" % (3 * L4.nv,), ok_all and nz == 3 * L4.nv)

i0, j0 = (0, 0, 0), (1, 0, 0)
T0h = Tij(L4, i0, j0)
Bi0 = PS({(0, L4.star[i0]): 1})
Bj0 = PS({(0, L4.star[j0]): 1})
check("A4 [exact, m=1] T_ij B_i=-T_ij B_j; ad(H_m)^2 T=4m^2 T, not a real nonzero "
      "ad eigenoperator; original nonzero anticommutator retained",
      ((T0h * Bi0) + (T0h * Bj0)).iszero() and not (H4 * T0h + T0h * H4).iszero()
      and (comm(H4,comm(H4,T0h))-T0h.smul(4)).iszero())
unit_ps=PS({(0,0):1})
oriented_ok=True
for mtest in (-.5,0,1):
    Htest=massterm(L4,mtest)
    for bsign in (-1,1):
        orient=T0h*(unit_ps+Bj0.smul(bsign)).smul(.5)
        eigenvalue=mtest*(eps_of(j0)-eps_of(i0))*bsign
        oriented_ok = oriented_ok and (comm(Htest,orient)-orient.smul(eigenvalue)).iszero()
check("A5 [exact oriented-hop control] T(I+bB_j)/2 has eigenvalue m(eps_j-eps_i)b at "
      "m=-1/2,0,1; the Hermitian T has neither eigenvalue +2 nor -2 at m=1",
      oriented_ok and comm(massterm(L4,0),T0h).iszero()
      and not (comm(H4,T0h)-T0h.smul(2)).iszero()
      and not (comm(H4,T0h)+T0h.smul(2)).iszero())
face=L4.loop(L4.faces()[0]); edgebit=face.x & -face.x
check("A6 [exact instrument boundary] one edge Z anticommutes with a face, while its corner "
      "parity commutes; diagonal parity alone does not provide an edge Record instrument",
      edgebit!=0 and not commutes_mono(Q(0,0,edgebit),face)
      and all(commutes_mono(Q(0,0,z),face) for z in L4.star.values()))

# ============================================================= B -- symmetries

def perm_qubits(L, f):
    pm = {}
    for (v, ax) in L.E:
        w = L.step(v, EX[ax])
        fv, fw = f(v), f(w)
        key = None
        for b in range(3):
            if L.step(fv, EX[b]) == fw:
                key = (fv, b)
                break
            if L.step(fw, EX[b]) == fv:
                key = (fw, b)
                break
        pm[L.ei[(v, ax)]] = L.ei[key]
    return pm


def apply_perm(H, pm, n):
    out = PS()
    for (x, z), c in H.items():
        nz2 = 0
        for q in range(n):
            if (z >> q) & 1:
                nz2 |= 1 << pm[q]
        out[(0, nz2)] = out.get((0, nz2), 0) + c
    return out


odd_ok = even_ok = True
ne = no = 0
for d in itertools.product(range(4), repeat=3):
    Ht = apply_perm(H4, perm_qubits(L4, lambda v, d=d: wrap(va(v, d), L4.dims)), L4.nq)
    if sum(d) & 1:
        no += 1
        odd_ok = odd_ok and (Ht - H4.smul(-1)).iszero()
    else:
        ne += 1
        even_ok = even_ok and (Ht - H4).iszero()
check("B1 [exact] the %d EVEN-sum coarse translations fix H_m: an index-2 sublattice generated by "
      "e_a + e_b" % ne, even_ok and ne == 32)
check("B2 [exact] the %d ODD-sum ones send H_m -> -H_m (Eps -> -Eps, m -> -m): the kinetic shift "
      "symmetry survives so" % no, odd_ok and no == 32)

ROTS = []
for p in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        Mx = [[0] * 3 for _ in range(3)]
        for a in range(3):
            Mx[a][p[a]] = sg[a]
        det = (Mx[0][0] * (Mx[1][1] * Mx[2][2] - Mx[1][2] * Mx[2][1])
               - Mx[0][1] * (Mx[1][0] * Mx[2][2] - Mx[1][2] * Mx[2][0])
               + Mx[0][2] * (Mx[1][0] * Mx[2][1] - Mx[1][1] * Mx[2][0]))
        if det == 1:
            ROTS.append(Mx)
rot_ok = all(
    (apply_perm(H4, perm_qubits(L4, lambda v, Mx=Mx: wrap(
        tuple(sum(Mx[a][b] * v[b] for b in range(3)) for a in range(3)), L4.dims)), L4.nq) - H4).iszero()
    for Mx in ROTS)
check("B3 [exact] all %d proper corner rotations fix H_m: a signed coordinate permutation keeps "
      "v1+v2+v3 mod 2" % len(ROTS), rot_ok and len(ROTS) == 24)

# ============================================================== C -- spectrum

anti = ok2 = okspec = 0.0
sp_ok = True
for L in (4, 6, 8):
    for tw in ((0, 0, 0), (1, 1, 1)):
        M, _, _, eps = build(L, tw)
        anti = max(anti, np.max(np.abs(eps[:, None] * M * eps[None, :] + M)))
        lam = np.linalg.eigvalsh(M)
        for m in (0.25, 0.5, 1.0, 2.0):
            Hm = M + m * np.diag(eps)
            ok2 = max(ok2, np.max(np.abs(Hm @ Hm - (M @ M + m * m * np.eye(L ** 3)))))
            w = np.linalg.eigvalsh(Hm)
            okspec = max(okspec, np.max(np.abs(np.sort(np.abs(w)) - np.sort(np.sqrt(lam ** 2 + m * m)))))
            sp_ok = sp_ok and int(np.sum(w > 0)) == L ** 3 // 2 and int(np.sum(w < 0)) == L ** 3 // 2
check("C1 [exact/1e-11] 4^3, 6^3, 8^3, both bcs, m = 0.25 to 2: {M,Eps} = 0 exactly "
      "(%.1e), (M+mEps)^2 = M^2+m^2 (%.1e), spectrum +-sqrt(E_0^2+m^2) half positive (%.1e)"
      % (anti, ok2, okspec), anti == 0.0 and ok2 < 1e-11 and okspec < 1e-11 and sp_ok)

M4, _, _, e4 = build(4, (1, 1, 1))
d6 = np.max(np.abs(M4 @ M4 - 6 * np.eye(64)))
fl = max(np.max(np.abs(np.abs(np.linalg.eigvalsh(M4 + m * np.diag(e4))) - np.sqrt(6 + m * m)))
         for m in (0.5, 1.0, 2.0))
check("C2 [exact/1e-12] antiperiodic 4^3: M^2 = 6I exactly (%.1e), so the spectrum is flat, "
      "+-sqrt(6+m^2) 32-fold, m = 0.5, 1, 2 (%.1e)" % (d6, fl), d6 == 0.0 and fl < 1e-12)

M8p, _, _, e8p = build(8, (0, 0, 0))
nz8 = int(np.sum(np.abs(np.linalg.eigvalsh(M8p)) < 1e-9))
gd = max(abs((lambda w: w[256] - w[255])(np.linalg.eigvalsh(M8p + m * np.diag(e8p))) - 2 * m)
         for m in (0.2, 0.5, 1.0))
check("C3 [1e-11] periodic 8^3 has %d zero modes (Dirac point on the grid); the mass gaps it to "
      "exactly 2m (%.1e)" % (nz8, gd),
      nz8 == 8 and gd < 1e-11)

bd = 0.0
for L in (4, 6, 8):
    M, _, _, eps = build(L, (1, 1, 1))
    for m in (0.0, 0.7):
        pred = []
        for n in itertools.product(range(L // 2), repeat=3):
            E = np.sqrt(6 + 2 * sum(np.cos(2 * np.pi * (2 * ni + 1) / L) for ni in n) + m * m)
            pred += [E] * 4 + [-E] * 4
        bd = max(bd, np.max(np.abs(np.sort(pred) - np.linalg.eigvalsh(M + m * np.diag(eps)))))
check("C4 [1e-13] Bloch E(q)^2 = 6 + 2 sum_a cos q_a + m^2, q_a = 2pi(2n_a+1)/L, fourfold: L = 4, 6, 8 "
      "antiperiodic, m = 0, 0.7 (%.1e)" % bd, bd < 1e-13)

# ============================================================ D -- taste class

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.diag([1, -1]).astype(complex)


def kr(*ms):
    o = np.array([[1.0 + 0j]])
    for mm in ms:
        o = np.kron(o, mm)
    return o


XI = [kr(SX, I2, I2), kr(SZ, SX, I2), kr(SZ, SZ, SX)]
GAM = [kr(SY, I2, I2), kr(SZ, SY, I2), kr(SZ, SZ, SY)]
SIX = GAM + XI
EPS8 = kr(SZ, SZ, SZ)
SIG = [SX, SY, SZ]
TT = np.diag([1, 1, -1, -1]).astype(complex)
BB = [kr(SX, SX), kr(SX, SY), kr(SX, SZ)]


def averaging_intertwiner(N):
    pg, pn = {}, {}
    for mm in range(64):
        g = np.eye(8, dtype=complex)
        n = np.eye(8, dtype=complex)
        for k in range(6):
            if (mm >> k) & 1:
                g = g @ SIX[k]
                n = n @ N[k]
        pg[mm] = g.conj().T
        pn[mm] = n
    for r in range(8):
        for c in range(8):
            Mx = np.zeros((8, 8), dtype=complex)
            Mx[r, c] = 1
            U = sum(pn[mm] @ Mx @ pg[mm] for mm in range(64))
            if abs(np.linalg.det(U)) > 1e-6:
                return U
    return None


G_ = [np.kron(SIG[a], TT) for a in range(3)]
W_ = [np.kron(I2, BB[a]) for a in range(3)]
F_ = [kr(I2, I2, SIG[b]) for b in range(3)]
Y_A = kr(I2, SY, I2)
res = {}
for sg in (1, -1):
    N = [sg * np.kron(SIG[a], TT) for a in range(3)] + [np.kron(I2, BB[a]) for a in range(3)]
    U = averaging_intertwiner(N)
    U = U / np.sqrt((U @ U.conj().T)[0, 0].real)
    im = U @ EPS8 @ U.conj().T
    res[sg] = dict(
        form=min(np.max(np.abs(im - s * Y_A)) for s in (1, -1)),
        anti_G=max(np.max(np.abs(im @ g + g @ im)) for g in G_),
        comm_F=max(np.max(np.abs(im @ f - f @ im)) for f in F_),
        anti_W=max(np.max(np.abs(im @ w + w @ im)) for w in W_))
GF = max(np.max(np.abs(g @ f - f @ g)) for g in G_ for f in F_)
WF = max(np.max(np.abs(w @ f - f @ w)) for w in W_ for f in F_)
r = res[-1]
check("D1 [1e-12] cell = spin (x) tA (x) tB: U Eps U^dag = -+ I (x) Y_A (x) I on BOTH branches "
      "(%.1e), identity on flavour" % r["form"],
      all(res[s]["form"] < 1e-12 for s in (1, -1)))
check("D2 [1e-12] it anticommutes with the three gamma_a = sigma_a (x) Z_A (x) I (%.1e): chirality-odd, "
      "not a chemical potential" % r["anti_G"],
      all(res[s]["anti_G"] < 1e-12 for s in (1, -1)))
check("D3 [1e-12] it commutes with the three flavour generators F_b = I (x) I (x) sigma_b (%.1e): "
      "taste-SINGLET" % r["comm_F"],
      all(res[s]["comm_F"] < 1e-12 for s in (1, -1)))
check("D4 [1e-12] the gamma_a commute with the F_b (%.1e); only the artefacts W_a = I (x) X_A (x) "
      "sigma_a fail (%.1e)" % (GF, WF),
      GF < 1e-12 and WF > 0.5)
check("D5 [1e-12] the mass anticommutes with the W_a too (%.1e), so with all six Clifford generators"
      % r["anti_W"],
      all(res[s]["anti_W"] < 1e-12 for s in (1, -1)))

# ========================================================== E -- the massive sea

MS = [0.0, 0.1, 0.25, 0.5, 1.0, 2.0, 4.0]
TW = {L: best_twist(L, 1.0)[0] for L in (4, 6, 8)}
M8, s8, i8, e8 = build(8, TW[8])
w80 = np.linalg.eigvalsh(M8)
gap0 = {L: (lambda w: w[L ** 3 // 2] - w[L ** 3 // 2 - 1])(
    np.linalg.eigvalsh(build(L, TW[L])[0])) for L in (4, 6, 8)}
TD = {m: bloch_moments(m, 200) for m in MS + [0.05]}
print("  massive sea, 8^3 at its best twist %s, and finite quadrature:" % str(TW[8]))
print("    m   <n>(+)     <n>(-)    C(8^3)   C(quad)  E/V(quad)   gap     2m")
idres = 0.0
gres = 0.0
for m in MS:
    w, Uv = np.linalg.eigh(M8 + m * np.diag(e8))
    P = Uv[:, :256] @ Uv[:, :256].T
    nv = np.diag(P)
    C8 = float(np.sum(e8 * nv)) / 512
    g = w[256] - w[255]
    gres = max(gres, abs(g - 2 * np.sqrt((gap0[8] / 2) ** 2 + m * m)))
    print("  %5.2f %.8f %.8f %+.6f %+.6f %+.6f %.6f %5.2f"
          % (m, nv[e8 > 0].mean(), nv[e8 < 0].mean(), C8, -0.5 * m * TD[m][1], -0.5 * TD[m][0], g, 2 * m))
dgz = 0.0
for L in (4, 6, 8):
    Mx, _, _, ex_ = build(L, TW[L])
    ev, EV = np.linalg.eigh(Mx)
    for m in (0.1, 0.5, 1.0, 2.0):
        cvec = np.einsum("ij,j,ij->i", EV, 1.0 / np.sqrt(ev * ev + m * m), EV)
        dgz = max(dgz, np.max(np.abs(np.einsum("ij,j,ij->i", EV, ev / np.sqrt(ev * ev + m * m), EV))))
        Uv = np.linalg.eigh(Mx + m * np.diag(ex_))[1]
        nvx = np.diag(Uv[:, :L ** 3 // 2] @ Uv[:, :L ** 3 // 2].T)
        idres = max(idres, np.max(np.abs(nvx - (0.5 - 0.5 * m * ex_ * cvec))))
check("E1 [1e-12] 4^3, 6^3, 8^3, m = 0.1 to 2: <n_v> = 1/2 - (m/2) eps_v c(m), c = [(M^2+m^2)^-1/2]_vv "
      "(%.1e), M f(M^2) diagonal-free (%.1e)"
      % (idres, dgz), idres < 1e-12 and dgz < 1e-12)

M4a, _, _, e4a = build(4, (1, 1, 1))
ex = 0.0
for m in (0.1, 0.25, 0.5, 1.0, 2.0, 4.0):
    w, Uv = np.linalg.eigh(M4a + m * np.diag(e4a))
    nv = np.diag(Uv[:, :32] @ Uv[:, :32].T)
    p = 0.5 - m / (2 * np.sqrt(6 + m * m))
    ex = max(ex, np.max(np.abs(nv[e4a > 0] - p)), np.max(np.abs(nv[e4a < 0] - (1 - p))),
             abs(float(np.sum(e4a * nv)) / 64 + m / (2 * np.sqrt(6 + m * m))))
check("E2 [exact form, 1e-12] antiperiodic 4^3, m = 0.1 to 4: <n_v> = 1/2 -+ m/(2 sqrt(6+m^2)) per "
      "sublattice, C = -m/(2 sqrt(6+m^2)) (%.1e)" % ex, ex < 1e-12)

c0 = [bloch_moments(0.0, N)[1] for N in (120, 200, 320)]
chi = c0[-1] / 2
sat = [(mm, -0.5 * mm * bloch_moments(mm, 160)[1]) for mm in (8.0, 100.0)]
check("E3 [numerical] C(0) = 0; slope chi = c(0)/2 = %.6f, measured %.6f at m = 0.05; saturation "
      "-1/2 + 3/(2 m^2) (m = 100: %+.6f vs %+.6f)"
      % (chi, 0.5 * TD[0.05][1], sat[-1][1], -0.5 + 1.5 / 1e4),
      abs(TD[0.0][1] * 0.0) < 1e-15 and abs(0.5 * TD[0.05][1] - chi) < 5e-3
      and abs(sat[-1][1] - (-0.5 + 1.5 / 1e4)) < 1e-5)
check("E4 [1e-11] the finite-torus gap is 2 sqrt((gap_0/2)^2 + m^2), gap_0 = %.6f on 8^3 (%.1e)"
      % (gap0[8], gres), gres < 1e-11)

# ========================================================= F -- kernel decay

def kernel_cols(Nc, m, off=0.0):
    q = 2 * np.pi * (np.arange(Nc) + off) / Nc
    co, si = np.cos(q), np.sin(q)
    C = [np.broadcast_to(co.reshape(sh), (Nc, Nc, Nc)) for sh in ((Nc, 1, 1), (1, Nc, 1), (1, 1, Nc))]
    S = [np.broadcast_to(si.reshape(sh), (Nc, Nc, Nc)) for sh in ((Nc, 1, 1), (1, Nc, 1), (1, 1, Nc))]
    E = np.sqrt(6 + 2 * (C[0] + C[1] + C[2]) + m * m)
    out = {}
    for s in range(8):
        col = np.zeros((Nc, Nc, Nc), dtype=complex)
        for a in range(3):
            col = col + (1 + C[a]) * XI[a][s, 0] + S[a] * GAM[a][s, 0]
        col = col + m * EPS8[s, 0]
        P = -0.5 * col / E
        if s == 0:
            P = P + 0.5
        out[s] = np.fft.ifftn(P)
    return out


Kv = kernel_cols(4, 0.5, 0.0)
Mr, sr, ir, er = build(8, (0, 0, 0))
Ur = np.linalg.eigh(Mr + 0.5 * np.diag(er))[1]
Pr = Ur[:, :256] @ Ur[:, :256].T
dev = 0.0
for v in sr:
    if (v[1] % 2) or (v[2] % 2):
        continue
    s = 4 * (v[0] % 2)
    dev = max(dev, abs(Kv[s][tuple(c // 2 for c in v)] - Pr[ir[v], ir[(0, 0, 0)]]))
Kw = kernel_cols(4, 0.5, 0.5)
Mw, _, iw, ew = build(8, (1, 1, 1))
Uw = np.linalg.eigh(Mw + 0.5 * np.diag(ew))[1]
Pw = Uw[:, :256] @ Uw[:, :256].T
devw = max(abs(abs(Kw[4 * (n % 2)][(n // 2, 0, 0)]) - abs(Pw[iw[(n, 0, 0)], iw[(0, 0, 0)]]))
           for n in range(1, 8))
check("F1 [1e-12] original selected-column validation: 128 periodic entries of 8^3, "
      "m = 0.5 (%.1e), seven antiperiodic axis magnitudes (%.1e)" % (dev, devw),
      dev < 1e-12 and devw < 1e-12)


# All eight cell components, including zero entries/contact, in one 8^3 source column.
full_per=full_ap=0.0
for v in sr:
    s=4*(v[0]%2)+2*(v[1]%2)+(v[2]%2)
    cell=tuple(c//2 for c in v)
    full_per=max(full_per,abs(Kv[s][cell]-Pr[ir[v],ir[(0,0,0)]]))
    # Half-shifted inverse FFT carries a known unit phase; magnitudes avoid that convention.
    full_ap=max(full_ap,abs(abs(Kw[s][cell])-abs(Pw[iw[v],iw[(0,0,0)]])))
check("F4 [complete declared-column control] all512 periodic complex entries and all512 "
      "antiperiodic magnitudes, m=.5, including off-axis and contact; not a full matrix test "
      "(%.1e, %.1e)" % (full_per,full_ap),full_per<1e-12 and full_ap<1e-12)


def axis_kernel(m, N1=2048, N2=192):
    """|P_{0u}| along u = (n,0,0); q2,q3 on an N2^2 midpoint grid, q1 on N1 points."""
    q1 = 2 * np.pi * (np.arange(N1) + 0.5) / N1
    c2 = np.cos(2 * np.pi * (np.arange(N2) + 0.5) / N2)
    X23 = c2[:, None] + c2[None, :]
    g = np.array([np.mean(1.0 / np.sqrt(6 + 2 * (np.cos(qq) + X23) + m * m)) for qq in q1])
    return (np.abs(np.fft.ifft(-0.5 * m * g)),
            np.abs(np.fft.ifft(-0.5 * (1 + np.exp(1j * q1)) * g)))


def fit(F, par, kap, lo, hi):
    R = np.arange(max(3, int(lo / kap)), int(hi / kap) + 1)
    R = R[(R < 1024) & (F[R] > 1e-14)]
    rr = 2.0 * R + par
    A = np.vstack([np.ones_like(rr), -rr, -np.log(rr)]).T
    sol = np.linalg.lstsq(A, np.log(F[R]), rcond=None)[0]
    return 1.0 / sol[1], sol[2]


print("  sea kernel along (n,0,0): |P(r)| = A e^{-r/xi} r^-b; branch-point comparison xi = 2/arccosh(1 + m^2/2)")
print("     m   even xi near/far  b      odd xi near/far  b     xi branch")
fok = True
for m in (0.2, 0.5, 1.0):
    fe, fo = axis_kernel(m)
    kap = np.arccosh(1 + m * m / 2)
    xp = 2.0 / kap
    (en, _), (ef, be) = fit(fe, 0, kap, 3, 7), fit(fe, 0, kap, 8, 20)
    (on, _), (of, bo) = fit(fo, 1, kap, 3, 7), fit(fo, 1, kap, 8, 20)
    print("   %5.2f   %7.3f %7.3f %5.3f  %7.3f %7.3f %5.3f  %8.4f"
          % (m, en, ef, be, on, of, bo, xp))
    fok = fok and abs(ef / xp - 1) < 0.02 and abs(of / xp - 1) < 0.02
check("F2 [finite fits, m=.2,.5,1] both far-window lengths within 2 per "
      "cent of branch-point comparison; fitted power prefactor, no all-m/image bound", fok)

fe0, fo0 = axis_kernel(0.0)
sl = [(2 * a + 1, 2 * b - 1, np.polyfit(np.log(2.0 * np.arange(a, b) + 1),
                                        np.log(fo0[np.arange(a, b)]), 1)[0]) for a, b in ((8, 20), (20, 60))]
check("F3 [numerical] m = 0: even noncontact kernel term zero (%.1e), contact P_vv=1/2 "
      "excluded; finite odd-branch log-log slope %.4f (%d <= n <= %d)"
      % (fe0.max(), sl[-1][2], sl[-1][0], sl[-1][1]),
      fe0.max() < 1e-15 and abs(sl[-1][2] + 3) < 0.04)

# ====================================================== G -- sector selection

ap = 0.0
for L in (4, 6):
    Mp, _, _, epp = build(L, (0, 0, 0), plain=True)
    ap = max(ap, np.max(np.abs(epp[:, None] * Mp * epp[None, :] + Mp)))
check("G1 [exact] Eps anticommutes with the PLAIN hopping too (%.1e), both graphs bipartite: "
      "E_{V/2} = -(1/2) tr sqrt(M^2 + m^2) in both sectors" % ap, ap == 0.0)

gok = True
worst = None
for L in (4, 6):
    for m in (0.0, 0.5, 1.0, 2.0, 4.0):
        ep = best_twist(L, m, plain=True)[1] / L ** 3
        es = best_twist(L, m, plain=False)[1] / L ** 3
        gok = gok and es < ep - 1e-9
        if worst is None or ep - es < worst[2]:
            worst = (L, m, ep - es)
check("G2 [1e-9] 4^3, 6^3, best twist per sector, m in {0,0.5,1,2,4}: KS is lower than plain among these two sectors, "
      "smallest margin %.6f (L=%d, m=%.1f)"
      % (worst[2], worst[0], worst[1]), gok)

print("  finite quadrature (200^3): m | plain E/V | staggered E/V | difference | -3/m^3")
lok = True
for m in (0.0, 0.5, 1.0, 2.0, 8.0, 50.0):
    sp = bloch_moments(m, 200, plain=True)[0]
    ss = bloch_moments(m, 200, plain=False)[0]
    d = -0.5 * (ss - sp)
    lok = lok and d < -1e-9
    print("   %6.2f  %+.9f  %+.9f  %+.9f  %s"
          % (m, -0.5 * sp, -0.5 * ss, d, ("%+.9f" % (-3.0 / m ** 3)) if m > 0 else "--"))
check("G3 [numerical] KS lower than plain at m={0,.5,1,2,8,50} on200^3; -3/m^3 only a comparison", lok)

_, _, x1s, x2s = bloch_moments(0.0, 200)
_, _, x1p, x2p = bloch_moments(0.0, 200, plain=True)
check("G4 [numerical moments, tolerance as stated] both sectors share <E_0^2> = %.6f/%.6f, the coordination 6, and differ at the "
      "fourth, %.4f vs %.4f"
      % (x1s, x1p, x2s, x2p),
      abs(x1s - 6) < 1e-6 and abs(x1p - 6) < 1e-6 and abs(x2s - 42) < 0.05 and abs(x2p - 90) < 0.2)

# ========================================================= H -- conjugation

D8 = np.diag(e8)
d1 = d2 = d3 = d4 = dc = 0.0
for m in (0.25, 0.5, 1.0):
    Hp, Hn = M8 + m * D8, M8 - m * D8
    wp, Up = np.linalg.eigh(Hp)
    wn, Un = np.linalg.eigh(Hn)
    Pp = Up[:, :256] @ Up[:, :256].T
    Pn = Un[:, :256] @ Un[:, :256].T
    d2 = max(d2, np.max(np.abs(D8 @ Hp @ D8 + Hn)))
    d1 = max(d1, np.max(np.abs(D8 @ (np.eye(512) - Pp) @ D8 - Pn)))
    d3 = max(d3, np.max(np.abs(np.sort(wp) - np.sort(wn))))
    d4 = max(d4, np.max(np.abs(np.diag(Pn) - (1 - np.diag(Pp)))))
    dc = max(dc, abs(float(np.sum(e8 * np.diag(Pn)) + np.sum(e8 * np.diag(Pp)))))
check("H1 [exact/1e-11] 8^3, m = 0.25, 0.5, 1: eps(M+mEps)eps = -(M-mEps) (%.1e), so P -> eps(I-P)eps "
      "maps the mass-m sea onto the mass-(-m) sea (%.1e), spectra equal, <n_v>(-m) = 1-<n_v>(m), "
      "C(-m) = -C(m) (%.1e)"
      % (d2, d1, dc), d2 == 0.0 and d1 < 1e-11 and d3 < 1e-11 and d4 < 1e-11 and dc < 1e-11)

# Corrected-scope controls reuse only small actual matrices.
Mb, vb, ib, eb=build(4,(1,1,1)); Db=np.diag(eb)
A=Mb[np.ix_(eb>0,eb<0)]; singular=np.linalg.svd(A,compute_uv=False)
svd_dev=0.0
for mm in (-.7,0,.7):
    energies=np.sqrt(singular**2+mm**2)
    svd_dev=max(svd_dev,float(np.max(abs(np.linalg.eigvalsh(Mb+mm*Db)
                                      -np.sort(np.r_[-energies,energies])))))
small_M=np.array([[0.,1,0],[1,0,1],[0,1,0]])
small_D=np.diag([1.,-1,1])
small_e=np.linalg.eigvalsh(small_M+.7*small_D)
check("C5 [balanced SVD control] full signed spectrum at m=-.7,0,.7; eps H(m) eps=-H(-m), "
      "not -H(m); an unbalanced three-site graph need not have equal sign multiplicities",
      svd_dev<1e-12 and np.max(abs(Db@(Mb+.7*Db)@Db+(Mb-.7*Db)))<1e-13
      and np.max(abs(Db@(Mb+.7*Db)@Db+(Mb+.7*Db)))>1
      and (np.sum(small_e>0),np.sum(small_e<0))==(2,1))
pcheck=np.array([.3,-.7,1.1])
Hcell=sum(np.sin(pcheck[a])*G_[a]+(1-np.cos(pcheck[a]))*W_[a] for a in range(3))+.7*Y_A
Ecell=np.sqrt(sum(2-2*np.cos(pcheck))+.7**2)
check("D6 [finite band control] noncommuting flavor artifacts mix the chosen basis while "
      "the full massive cell bands remain fourfold (spin2 x flavor2), not four tastes",
      np.max(abs(Hcell@Hcell-Ecell**2*np.eye(8)))<1e-12
      and np.max(abs(np.linalg.eigvalsh(Hcell)-np.r_[-Ecell*np.ones(4),Ecell*np.ones(4)]))<1e-12)
xa=np.array([0.,2.]); wa=np.array([.5,.5]); xb=np.array([.5,5.]); wb=np.array([8/9,1/9])
check("G5 [moment inference counterexample] equal mean, smaller second moment does not "
      "order E sqrt(X+m^2): m=1/4, XA={0,2}, XB={1/2,5}",
      abs(wa@xa-wb@xb)<1e-14 and wa@(xa*xa)<wb@(xb*xb)
      and wa@np.sqrt(xa+1/16)<wb@np.sqrt(xb+1/16))
wp,Up=np.linalg.eigh(Mb+.7*Db); wn,Un=np.linalg.eigh(Mb-.7*Db)
Ppos=Up[:,:32]@Up[:,:32].T; Pminus=Un[:,:32]@Un[:,:32].T
label_difference=float(np.max(abs(np.diag(Ppos)-np.diag(Pminus))))
check("H2 [fixed-label control] equal mass-sign spectra but site occupancies differ by %.6f; "
      "equivalence needs a simultaneous observable/state relabeling" % label_difference,
      np.max(abs(wp-wn))<1e-12 and label_difference>.25
      and np.max(abs(np.diag(Pminus)+np.diag(Ppos)-1))<1e-12)
print("SUMMARY: supplied diagonal parity model; balanced node gap2|m|, two flavors with "
      "fourfold bands, finite kernel fits and KS/plain comparisons; physical Record/time bridge unproved.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
