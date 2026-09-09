#!/usr/bin/env python3
"""Records register colour only through triality and singlets: the SU(3) case.

Self-contained finite-block runner.  The carrier is the SU(3) analogue of the
plaquette of THE_RECORD_READABLE_GAUGE_INVARIANT_ALGEBRA_IS_COLOUR_BLIND_...
_2026-09-03 (PR #7914), whose construction code is reused generalised from
N = 2 to general N and reduced to the geometries that fit the memory rule.
Everything it builds is DECLARED design, derived from no axiom:

  geometry  the DIMER (corners v = 0,1; link e = (i=0, j=1)), the open
            3-CHAIN (corners 0,1,2; links (0,1),(1,2)) and the TRIANGLE
            (corners 0,1,2; links (0,1),(1,2),(2,0)).  The SU(3) plaquette is
            dimensioned and REJECTED, never built.
  matter    a fermion TRIPLET per corner -- N = 3 encoded modes psi_{v,alpha}
            on N code layers, the layer index being the internal ("colour")
            label -- Jordan-Wigner encoded, mode index N*v + alpha;
  link      the ONE-RISHON (N_e = 1) sector of the U(3) QUANTUM LINK.  Rishon
            modes are c_{e,end,a}, end in {i,j}, a = 1..N; the N_e = 1 sector
            is span{|i,a>, |j,a>} = (orientation record) x (colour record),
            TWO DESIGNED RECORDS per link, of dimension DL = 2N = 6, with
            U_e^{ab} = c_{e,i,a} c^dag_{e,j,b} (U U = 0) and
            E^a_{e,v} = P_v (I x lambda^a/2);
  law       H_hop = -t sum_e eta_e sum_{ab} [psi^dag_{i,a} psi_{j,b} U_e^{ab}
            + h.c.], eta = 1, used only as one example element of I;
  Gauss     G_v^a = rho_v^a + sum_{e at v} E^a_{e,v}, Q_v = n^f_v + n^r_v.

  R  = operators diagonal in the declared record basis (record-readable).
  I  = the commutant of {G_v^a} (gauge-invariant).
  D  = the record map D(M) = sum_r P_r M P_r onto R.

  A  T1 THE CONSTRUCTION.  Exact CAR, U U = 0, su(3) closure
     [G_v^a, G_w^b] = i f^{abc} delta_vw G_v^c with f read off the generators,
     [G_v^a, H_hop] = 0 exactly, the corner Casimir spectrum, and the carriers.
  B  T2 R n I EXACTLY.  dim(R n I) = (N+1)^V 2^E on nine non-abelian carriers;
     the level sets of the abelian record data; the generators; no colour
     record value in I; no record pattern solves the Gauss law; exact integer
     Haar characters for dim I and the Gauss dimension; R n I restricted to the
     Gauss sector is a complete commuting set; the colour frame.
  C  T3 TRIALITY.  omega^{Q_v} is record-diagonal and in the commutant; the
     Gauss sector sits at triality zero; colour-rotated triplets; the zero
     Gauss-sector block of every colour octet / triplet / anti-triplet; the
     epsilon_abc baryon in the 3-chain hull.
  D  T4 THE TWO FACTS THAT CORRECT THE EXPECTATION.  The readable fraction of
     I is NOT monotone in N while the readable fraction of R falls; and the
     Cartan generators are record-diagonal but not gauge-invariant.

Every matrix entry of the generators, the link operators and the RESCALED
Cartan generator T^8 = sqrt(3) lambda^8/2 = diag(1,1,-2)/2 is a dyadic rational
of magnitude <= 4, so all sums and products are exact in IEEE double and every
zero test tagged [exact] is `== 0`, not a tolerance.  T^8 spans the same Cartan
direction as lambda^8/2, so the commutant I is unchanged by the rescaling; the
true lambda^8/2 (entries 1/(2 sqrt 3)) is used only where the su(3)
normalisation matters -- closure and Casimirs -- and those checks are tagged
[numerical].  The dimer is carried densely; the 3-chain and the triangle are
carried sparsely.  The largest dense array formed anywhere is 384 x 384.  No
random number is drawn and no seed is set: the colour rotations run on
DECLARED axes and DECLARED angles.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import sys
import time
from itertools import combinations, product as iproduct

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components

AUDIT_TIMEOUT_SEC = 150

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


# ============================================================ declared objects

ANGLES = (0.3, 0.7, 1.1, 2.0, np.pi)           # DECLARED rotation angles
I2 = np.eye(2, dtype=complex)
SZ = np.diag([1, -1]).astype(complex)
ANN = np.array([[0, 1], [0, 0]], dtype=complex)


def gellmann():
    """lambda^a, a = 1..8, in the true normalisation."""
    return [np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
            np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
            np.diag([1, -1, 0]).astype(complex),
            np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
            np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
            np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
            np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
            np.diag([1, 1, -2]).astype(complex) / np.sqrt(3.0)]


def pauli():
    return [np.array([[0, 1], [1, 0]], dtype=complex),
            np.array([[0, -1j], [1j, 0]], dtype=complex),
            np.diag([1, -1]).astype(complex)]


def gens(N):
    """(T_true, T_dyadic): su(N) generators lambda^a/2 and the dyadic rescale."""
    if N == 1:
        return [], []
    if N == 2:
        T = [p / 2.0 for p in pauli()]
        return T, [t.copy() for t in T]
    L = gellmann()
    T = [x / 2.0 for x in L]
    D = [x / 2.0 for x in L[:7]] + [np.diag([1, 1, -2]).astype(complex) / 2.0]
    return T, D


def kron_dense(mats):
    out = np.ones((1, 1), dtype=complex)
    for m in mats:
        out = np.kron(out, m)
    return out


def kron_sparse(mats):
    out = sp.identity(1, format="csr", dtype=complex)
    for m in mats:
        out = sp.kron(out, m, format="csr")
    return out


class Carrier:
    """The whole declared block for gauge group SU(N), carried densely."""

    def __init__(self, N, NV, LINKS, eta=None):
        self.N, self.NV, self.LINKS = N, NV, LINKS
        self.NE = len(LINKS)
        self.NMODE = N * NV
        self.DM = 2 ** self.NMODE
        self.DL = 2 * N
        self.DLL = self.DL ** self.NE
        self.DIM = self.DM * self.DLL
        self.ETA = eta if eta is not None else [1.0] * self.NE
        self.TT, self.TD = gens(N)
        self.NA = len(self.TT)
        self._build()

    def _jw(self, m):
        return kron_dense([SZ if k < m else (ANN if k == m else I2)
                           for k in range(self.NMODE)])

    def _emb_matter(self, op):
        return np.kron(op, np.eye(self.DLL, dtype=complex))

    def _emb_link(self, e, op):
        return np.kron(np.eye(self.DM, dtype=complex),
                       kron_dense([op if k == e else np.eye(self.DL, dtype=complex)
                                   for k in range(self.NE)]))

    def ends_at(self, v):
        out = []
        for e, (i, j) in enumerate(self.LINKS):
            if i == v:
                out.append((e, 'i'))
            if j == v:
                out.append((e, 'j'))
        return out

    def _build(self):
        N, NV, NE, DL = self.N, self.NV, self.NE, self.DL
        CM = [self._jw(m) for m in range(self.NMODE)]
        self.CM = CM
        self.PSI = {(v, a): self._emb_matter(CM[N * v + a])
                    for v in range(NV) for a in range(N)}
        Pi = np.diag([1.0] * N + [0.0] * N).astype(complex)
        Pj = np.diag([0.0] * N + [1.0] * N).astype(complex)
        self.PI, self.PJ = Pi, Pj
        self.TL_true = [np.kron(I2, t) for t in self.TT]
        self.TL_dyad = [np.kron(I2, t) for t in self.TD]
        U = [[np.zeros((DL, DL), dtype=complex) for _ in range(N)] for _ in range(N)]
        for a in range(N):
            for b in range(N):
                U[a][b][N + b, a] = -1.0            # U^{ab} = -|j,b><i,a|
        self.U = U
        self.RHO_t, self.RHO_d = {}, {}
        for v in range(NV):
            for a in range(self.NA):
                for tab, store in ((self.TT, self.RHO_t), (self.TD, self.RHO_d)):
                    acc = np.zeros((self.DIM, self.DIM), dtype=complex)
                    for p in range(N):
                        for q in range(N):
                            c = tab[a][p, q]
                            if c != 0:
                                acc += c * (self.PSI[(v, p)].conj().T @ self.PSI[(v, q)])
                    store[(v, a)] = acc
        self.NF = {v: sum(self.PSI[(v, a)].conj().T @ self.PSI[(v, a)] for a in range(N))
                   for v in range(NV)}
        self.EF_t, self.EF_d, self.NR = {}, {}, {}
        for e in range(NE):
            for s, P in (('i', Pi), ('j', Pj)):
                for a in range(self.NA):
                    self.EF_t[(e, s, a)] = self._emb_link(e, P @ self.TL_true[a])
                    self.EF_d[(e, s, a)] = self._emb_link(e, P @ self.TL_dyad[a])
                self.NR[(e, s)] = self._emb_link(e, P)
        self.G_t, self.G_d, self.Q = {}, {}, {}
        for v in range(NV):
            for a in range(self.NA):
                self.G_t[(v, a)] = self.RHO_t[(v, a)] + sum(
                    self.EF_t[(e, s, a)] for (e, s) in self.ends_at(v))
                self.G_d[(v, a)] = self.RHO_d[(v, a)] + sum(
                    self.EF_d[(e, s, a)] for (e, s) in self.ends_at(v))
            self.Q[v] = self.NF[v] + sum(self.NR[(e, s)] for (e, s) in self.ends_at(v))
        H = np.zeros((self.DIM, self.DIM), dtype=complex)
        for e, (i, j) in enumerate(self.LINKS):
            term = np.zeros((self.DIM, self.DIM), dtype=complex)
            for a in range(N):
                for b in range(N):
                    term += (self.PSI[(i, a)].conj().T @ self.PSI[(j, b)]) \
                        @ self._emb_link(e, U[a][b])
            term = term + term.conj().T
            H -= self.ETA[e] * term
        self.H = H
        self.nf = np.array([np.real(np.diag(self.NF[v])) for v in range(NV)])
        self.oe = np.array([np.real(np.diag(self.NR[(e, 'j')])) for e in range(NE)])
        self.qv = np.array([np.real(np.diag(self.Q[v])) for v in range(NV)])


def nnz0(M):
    return int(np.count_nonzero(M))


def offdiag_nnz(M):
    A = M.copy()
    np.fill_diagonal(A, 0)
    return int(np.count_nonzero(A))


def comm(A, B):
    return A @ B - B @ A


def dyadic(M, bound=4.0):
    d = M[M != 0]
    if d.size == 0:
        return True
    r, i = 4.0 * d.real, 4.0 * d.imag
    return bool(np.all(r == np.round(r)) and np.all(i == np.round(i))
                and np.abs(d).max() <= bound)


def in_I_exact(C, M):
    """[exact] is M in the commutant of every dyadic G_v^a?  nnz == 0."""
    return all(nnz0(comm(M, C.G_d[(v, a)])) == 0
               for v in range(C.NV) for a in range(C.NA))


def components(C):
    """R n I = functions constant on the components cut by the OFF-DIAGONAL support
    of the su(N) Gauss generators (for diagonal D, [D,G]_rs = (d_r - d_s) G_rs)."""
    DIM = C.DIM
    parent = np.arange(DIM)

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    nedge = 0
    for v in range(C.NV):
        for a in range(C.NA):
            A = C.G_d[(v, a)].copy()
            np.fill_diagonal(A, 0)
            r, c = np.nonzero(A)
            nedge += len(r)
            for x, y in zip(r, c):
                rx, ry = find(x), find(y)
                if rx != ry:
                    parent[rx] = ry
    roots = np.array([find(x) for x in range(DIM)])
    _, labels = np.unique(roots, return_inverse=True)
    return int(labels.max()) + 1, labels, nedge


def nlevels(arrs):
    """number of distinct joint values of a list of length-DIM real arrays"""
    A = np.stack([np.rint(np.asarray(x) * 12.0) for x in arrs], axis=1)
    _, key = np.unique(A, axis=0, return_inverse=True)
    return int(key.max()) + 1, key


DIMER = (2, [(0, 1)])
print("declared: a fermion TRIPLET per corner and the one-rishon sector of the U(3) quantum "
      "link (DL = 2N = 6 = orientation x colour). R = record-diagonal; I = commutant of "
      "{G_v^a}. Carriers: dimer 384, 3-chain 18432, triangle 110592; no plaquette")

C3 = Carrier(3, *DIMER)
C2 = Carrier(2, *DIMER)
C1 = Carrier(1, *DIMER)

# ====================================== A -- T1, the construction

car_ok = True
for m in range(C3.NMODE):
    for n in range(C3.NMODE):
        d = 1.0 if m == n else 0.0
        ac = C3.CM[m] @ C3.CM[n].conj().T + C3.CM[n].conj().T @ C3.CM[m]
        car_ok = car_ok and nnz0(ac - d * np.eye(C3.DM)) == 0
        car_ok = car_ok and nnz0(C3.CM[m] @ C3.CM[n] + C3.CM[n] @ C3.CM[m]) == 0
uu_ok = all(nnz0(C3.U[a][b] @ C3.U[c][d]) == 0
            for a in range(3) for b in range(3) for c in range(3) for d in range(3))
allops = [C3.H] + [C3.G_d[(v, a)] for v in range(2) for a in range(8)] \
    + [C3.Q[v] for v in range(2)]
diag_ok = all(offdiag_nnz(C3.G_d[(v, a)]) == 0 for v in range(2) for a in (2, 7)) \
    and all(offdiag_nnz(C3.Q[v]) == 0 for v in range(2))
check("A1 [exact] the construction: %d JW matter modes, exact CAR, one one-rishon U(3) link "
      "DL = 2N = %d, U U = 0, dim R = dim H = 2^%d x %d = %d; every generator entry dyadic of "
      "magnitude <= 4 once T^8 = sqrt(3) lambda^8/2 = diag(1,1,-2)/2, so every [exact] test "
      "is nnz == 0; G_v^3, G_v^8, Q_v diagonal, hence in R"
      % (C3.NMODE, C3.DL, C3.NMODE, C3.DLL, C3.DIM),
      car_ok and uu_ok and C3.DIM == 384 and C3.DL == 6 and diag_ok
      and all(dyadic(M) for M in allops))

TT = C3.TT
f = np.zeros((8, 8, 8))
for a in range(8):
    for b in range(8):
        for c in range(8):
            f[a, b, c] = np.real(-2j * np.trace(comm(TT[a], TT[b]) @ TT[c]))
f_ok = (abs(f[0, 1, 2] - 1.0) < 1e-12 and abs(f[3, 4, 7] - np.sqrt(3) / 2) < 1e-12
        and abs(f[0, 3, 6] - 0.5) < 1e-12 and abs(f[0, 4, 5] + 0.5) < 1e-12)
worst_cl = 0.0
for v in range(2):
    for w in range(2):
        for a in range(8):
            for b in range(8):
                lhs = comm(C3.G_t[(v, a)], C3.G_t[(w, b)])
                rhs = np.zeros_like(lhs) if v != w else \
                    sum(1j * f[a, b, c] * C3.G_t[(v, c)] for c in range(8))
                worst_cl = max(worst_cl, float(np.abs(lhs - rhs).max()))
check("A2 [numerical, 1e-13] su(3) CLOSURE with f^{abc} = -2i tr([T^a,T^b]T^c) read off the "
      "generators (f_123 = %.1f, f_458 = %.6f = sqrt(3)/2, f_147 = %.1f, f_156 = %.1f): "
      "[G_v^a, G_w^b] = i f^{abc} delta_vw G_v^c for all 2 x 2 x 8 x 8 pairs to %.2e"
      % (f[0, 1, 2], f[3, 4, 7], f[0, 3, 6], f[0, 4, 5], worst_cl),
      f_ok and worst_cl < 1e-13)

hop_exact = all(nnz0(comm(C3.G_d[(v, a)], C3.H)) == 0 for v in range(2) for a in range(8))
hop_true = max(float(np.abs(comm(C3.G_t[(v, a)], C3.H)).max())
               for v in range(2) for a in range(8))
q_hop = all(nnz0(comm(C3.Q[v], C3.H)) == 0 for v in range(2))
check("A3 [exact] the covariant hop is gauge-invariant: [G_v^a, H_hop] = 0 for all 16 "
      "generators as dyadic matrices (nnz = 0, no tolerance) and %.1e with the true "
      "lambda^8/2; [Q_v, H_hop] = 0 too" % hop_true,
      hop_exact and hop_true < 1e-14 and q_hop)

CAS = {v: sum(C3.G_t[(v, a)] @ C3.G_t[(v, a)] for a in range(8)) for v in range(2)}
cas_ok = all(max(float(np.abs(comm(CAS[v], C3.G_t[(w, a)])).max())
                 for w in range(2) for a in range(8)) < 1e-13 for v in range(2))
casvals = sorted({round(x, 9) for x in np.real(np.linalg.eigvalsh(CAS[0]))})
check("A4 [numerical, 1e-13] the corner Casimir C_v = sum_a (G_v^a)^2 commutes with the gauge "
      "algebra, spectrum %s = {0, 4/3, 3, 10/3}: the 1, the 3/3bar, the 8, the 6/6bar -- the "
      "reps from tensoring the corner Fock space Lambda(C^3) = 1 + 3 + 3bar + 1 with its link "
      "end" % [float(round(x, 4)) for x in casvals],
      cas_ok and len(casvals) == 4 and abs(casvals[1] - 4.0 / 3.0) < 1e-9
      and abs(casvals[2] - 3.0) < 1e-9 and abs(casvals[3] - 10.0 / 3.0) < 1e-9)

PLQ = {N: (2 ** (N * 4) * (2 * N) ** 4, (N + 1) ** 4 * 2 ** 4) for N in (1, 2, 3)}
check("A5 [exact] carriers built: dimer 384 densely, 3-chain 18432 and triangle 110592 "
      "sparsely. The SU(3) PLAQUETTE, 2^12 x 6^4 = %d, is REJECTED under the memory rule and "
      "never built (12 JW modes need a 4096 x 4096 factor, ~2 x 10^8 graph edges); its "
      "dim(R n I) = 4^4 x 2^4 = %d is inferred by the law of B2, its dim I and Gauss "
      "dimension by the characters of B8" % (PLQ[3][0], PLQ[3][1]),
      PLQ[3] == (5308416, 4096) and PLQ[2] == (65536, 1296) and PLQ[1] == (256, 256))

# ====================================== B -- T2, R n I exactly

RES = {}
for name, C in (("U(1)", C1), ("SU(2)", C2), ("SU(3)", C3)):
    RES[name] = (C.DIM, np.arange(C.DIM), 0) if C.NA == 0 else components(C)
n3, lab3, ne3 = RES["SU(3)"]
n2, lab2, _ = RES["SU(2)"]
n1, lab1, _ = RES["U(1)"]
check("B1 [exact] the reduction: for diagonal D, [D, G]_{rs} = (d_r - d_s) G_{rs}, so R n I = "
      "functions constant on the components cut by the off-diagonal support of the six "
      "non-Cartan G_v^a (%d edges; G_v^3, G_v^8 diagonal, imposing nothing). dim(R n I) = %d "
      "= 4^2 x 2 of dim R = %d; SU(2) here gives %d of %d, U(1) %d of %d, all of R"
      % (ne3, n3, C3.DIM, n2, C2.DIM, n1, C1.DIM),
      n3 == 32 == 4 ** 2 * 2 and n2 == 18 == 3 ** 2 * 2 and n1 == C1.DIM == 8)


def carrier_components(N, NV, LINKS):
    """dim(R n I), dim R, and whether the components are the abelian level sets."""
    NE = len(LINKS)
    NMODE, DL = N * NV, 2 * N
    DM, DLL = 2 ** NMODE, DL ** NE
    DIM = DM * DLL
    T = gens(N)[1]

    def jw(m):
        return kron_sparse([sp.csr_matrix(SZ if k < m else (ANN if k == m else I2))
                            for k in range(NMODE)])

    CM = [jw(m) for m in range(NMODE)]
    IL = sp.identity(DLL, format="csr", dtype=complex)
    ID = sp.identity(DM, format="csr", dtype=complex)
    PSI = {(v, a): sp.kron(CM[N * v + a], IL, format="csr")
           for v in range(NV) for a in range(N)}

    def emb_link(e, op):
        return sp.kron(ID, kron_sparse([sp.csr_matrix(op) if k == e
                                        else sp.identity(DL, format="csr", dtype=complex)
                                        for k in range(NE)]), format="csr")

    Pi = np.diag([1.0] * N + [0.0] * N).astype(complex)
    Pj = np.diag([0.0] * N + [1.0] * N).astype(complex)
    NFd = np.zeros((NV, DIM))
    for v in range(NV):
        acc = sum((PSI[(v, a)].getH() @ PSI[(v, a)] for a in range(N)),
                  sp.csr_matrix((DIM, DIM), dtype=complex))
        NFd[v] = np.real(acc.diagonal())
    OEd = np.zeros((NE, DIM))
    NRd = np.zeros((NV, DIM))
    for e, (i, j) in enumerate(LINKS):
        OEd[e] = np.real(emb_link(e, Pj).diagonal())
        NRd[i] += np.real(emb_link(e, Pi).diagonal())
        NRd[j] += np.real(emb_link(e, Pj).diagonal())
    key = np.zeros(DIM, dtype=np.int64)
    for row in list(NFd) + list(OEd):
        key = key * (N + 2) + np.rint(row).astype(np.int64)
    nlev = len(np.unique(key))
    keyQ = np.zeros(DIM, dtype=np.int64)
    for row in list(NFd + NRd) + list(OEd):
        keyQ = keyQ * (2 * N + 3) + np.rint(row).astype(np.int64)
    nlevQ = len(np.unique(keyQ))
    if not T:                                    # U(1): no su(N) generators at all
        return DIM, DIM, nlev, nlevQ, 0, True
    rows, cols, nedge = [], [], 0
    for v in range(NV):
        for a in range(len(T)):
            acc = sp.csr_matrix((DIM, DIM), dtype=complex)
            for p in range(N):
                for q in range(N):
                    c = T[a][p, q]
                    if c != 0:
                        acc = acc + c * (PSI[(v, p)].getH() @ PSI[(v, q)])
            for (e, (i, j)) in enumerate(LINKS):
                if i == v:
                    acc = acc + emb_link(e, Pi @ np.kron(I2, T[a]))
                if j == v:
                    acc = acc + emb_link(e, Pj @ np.kron(I2, T[a]))
            M = sp.coo_matrix(acc)
            m = (M.row != M.col) & (M.data != 0)
            nedge += int(m.sum())
            rows.append(M.row[m])
            cols.append(M.col[m])
    rows = np.concatenate(rows)
    cols = np.concatenate(cols)
    inside = bool(np.all(key[rows] == key[cols]))     # every edge stays in a level set
    ADJ = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(DIM, DIM)).tocsr()
    ncomp, _ = connected_components(ADJ, directed=False)
    return DIM, ncomp, nlev, nlevQ, nedge, inside


GEOM = {"dimer": (2, [(0, 1)]),
        "3-chain": (3, [(0, 1), (1, 2)]),
        "triangle": (3, [(0, 1), (1, 2), (2, 0)])}
rowsout, ok_all = [], True
for gname, (NV, LINKS) in GEOM.items():
    for N in (1, 2, 3):
        DIM, nc, nlev, nlevQ, ne, inside = carrier_components(N, NV, LINKS)
        pred = (N + 1) ** NV * 2 ** len(LINKS)
        ok_all = ok_all and (nc == pred == nlev == nlevQ) and inside
        rowsout.append((gname, N, DIM, nc))
check("B2 [exact] dim(R n I) = (N+1)^V 2^E EXACTLY on all %d carriers (3 geometries x "
      "N = 1,2,3) by explicit components -- %s -- and equals every time both the number of "
      "joint level sets of the abelian record data (n^f_v ; o_e) and of {Q_v} u "
      "{E^2_{e,end}}; every off-diagonal entry of every non-Cartan G_v^a joins two patterns "
      "in the SAME level set, so no finer readable invariant exists. It reproduces the SU(2) "
      "plaquette's 1296 and gives 4096 for the SU(3) plaquette"
      % (len(rowsout), ", ".join("%d/%d" % (nc, D) for g, N, D, nc in rowsout)),
      ok_all and len(rowsout) == 9)

k_ab, _ = nlevels(list(C3.nf) + list(C3.oe))
E2, E2X, e2res = {}, {}, 0.0
for e in range(C3.NE):
    for s, P in (('i', C3.PI), ('j', C3.PJ)):
        E2[(e, s)] = sum(C3.EF_t[(e, s, a)] @ C3.EF_t[(e, s, a)] for a in range(8))
        E2X[(e, s)] = (4.0 / 3.0) * C3._emb_link(e, P)      # the EXACT link-end Casimir
        e2res = max(e2res, float(np.abs(E2[(e, s)] - E2X[(e, s)]).max()))
e2d = np.array([np.real(np.diag(E2X[(e, s)])) for e in range(C3.NE) for s in ('i', 'j')])
k_gen, _ = nlevels(list(C3.qv) + list(e2d))
k_q, _ = nlevels(list(C3.qv))
k_e2, _ = nlevels(list(e2d))
tri = C3.qv % 3
k_tri, _ = nlevels(list(tri))
picks = [0, 7, 15, 23, 31]
proj_ok = all(in_I_exact(C3, np.diag((lab3 == c).astype(float))) for c in picks)
gen_ok = (all(in_I_exact(C3, np.diag(C3.qv[v])) for v in range(2))
          and all(in_I_exact(C3, np.diag(e2d[k])) for k in range(len(e2d))))
check("B3 [exact] the generators: {Q_v} u {E^2_{e,end}} have %d joint level sets, so the "
      "abelian charges and the link-end electric Casimirs generate ALL of R n I; alone {Q_v} "
      "%d, {E^2} %d (E^2 = (4/3) P_end exactly, matched to %.1e, so on the one-rishon link "
      "the Casimir IS the orientation record), triality 9. Five declared component "
      "projectors, every Q_v and every E^2_{e,end} commute with all 16 G_v^a as 384-dim "
      "matrices, nnz = 0" % (k_gen, k_q, k_e2, e2res),
      k_ab == n3 == 32 and k_gen == n3 and k_q == 23 and k_e2 == 2 and k_tri == 9
      and proj_ok and gen_ok)


def local_ok(sets, subset):
    def chi(bits):
        s = 1
        for q in subset:
            s *= (1 - 2 * bits[q])
        return s
    return all(len({chi(b) for b in S}) == 1 for S in sets)


MSETS3 = [[b for b in iproduct((0, 1), repeat=3) if sum(b) == k] for k in range(4)]
SUB3 = [s for k in range(4) for s in combinations(range(3), k)]
mgood = [s for s in SUB3 if local_ok(MSETS3, s)]
nstr = len(mgood) ** 2 * 2
colour_vals = []
for a in range(3):
    colour_vals.append(np.real(np.diag(C3.PSI[(0, a)].conj().T @ C3.PSI[(0, a)])))
    colour_vals.append(np.real(np.diag(C3._emb_link(0, np.diag(
        [1.0 if k == a else 0.0 for k in range(3)] + [0.0] * 3)))))
cv_in_I = [in_I_exact(C3, np.diag(x)) for x in colour_vals]
r0 = int(np.where(np.bincount(lab3)[lab3] > 1)[0][0])
d1 = np.zeros(C3.DIM)
d1[r0] = 1.0
check("B4 [exact] R n I is COLOUR-BLIND: not one of the 6 single colour record values (three "
      "matter colour occupations n_{0,a}, three link colour records) is in I, all %s; nor is "
      "the projector onto one record pattern, so R is not inside I. Of the 8 Pauli-Z strings "
      "on a corner's colour records only %d survive, giving %d monomials against dim(R n I) "
      "= %d: R n I is not spanned by record-value monomials"
      % (set(bool(x) for x in cv_in_I), len(mgood), nstr, n3),
      not any(cv_in_I) and not in_I_exact(C3, np.diag(d1)) and len(mgood) == 2)

edge_ok = True
for v in range(2):
    for a in range(8):
        A = C3.G_d[(v, a)].copy()
        np.fill_diagonal(A, 0)
        r, c = np.nonzero(A)
        edge_ok = edge_ok and bool(np.all(lab3[r] == lab3[c]))
check("B5 [exact] R n I does not depend on the declared colour frame: all %d component "
      "projectors commute with all 16 G_v^a, checked at once by LABELS[r] == LABELS[c] on "
      "every one of the %d off-diagonal entries, so U_g (R n I) U_g^dag = R n I for every g "
      "in SU(3)^2" % (n3, ne3), edge_ok)

A3op = sum(C3.G_t[(v, a)] @ C3.G_t[(v, a)] for v in range(2) for a in range(8))
A3op = 0.5 * (A3op + A3op.conj().T)
ev, evec = np.linalg.eigh(A3op)
NZ = int(np.sum(ev < 1e-9))
VG = evec[:, :NZ]
npat_d = int(np.sum(np.abs(np.real(np.diag(A3op))) < 1e-12))


def pg(T):
    return VG.conj().T @ T @ VG


hull = np.where(np.abs(np.einsum('ij,ij->i', VG, VG.conj())).real > 1e-9)[0]
comps_hull = np.unique(lab3[hull])
blk_tr, blk_idem, blk_rk = [], 0.0, []
for c in comps_hull:
    Pc = pg(np.diag((lab3 == c).astype(float)))
    blk_tr.append(float(np.trace(Pc).real))
    blk_rk.append(int(np.linalg.matrix_rank(Pc, tol=1e-9)))
    blk_idem = max(blk_idem, float(np.abs(Pc @ Pc - Pc).max()))
check("B6 [numerical, 1e-9] the dimer Gauss sector (joint kernel of the 16 G_v^a) is "
      "%d-dimensional of %d, smallest nonzero eigenvalue %.4f, and %d record patterns solve "
      "the SU(3) Gauss law: the sector is nowhere in the record basis. R n I restricted to it "
      "is a COMPLETE COMMUTING SET -- hull %d patterns meeting %d of the %d readable classes, "
      "each an orthogonal projector (max|P^2-P| = %.1e) of rank one, traces summing to %d"
      % (NZ, C3.DIM, float(ev[ev >= 1e-9].min()), npat_d, len(hull), len(comps_hull), n3,
         blk_idem, int(round(sum(blk_tr)))),
      NZ == 4 and npat_d == 0 and blk_idem < 1e-9 and len(comps_hull) == 4
      and blk_rk == [1, 1, 1, 1] and len(hull) == 12 and abs(sum(blk_tr) - NZ) < 1e-9)


def ct_monomials(N):
    zk = []
    for k in range(N - 1):
        e = [0] * (N - 1)
        e[k] = 1
        zk.append(tuple(e))
    zk.append(tuple([-1] * (N - 1)))
    return zk


def pmul(A, B):
    out = {}
    for ka, va in A.items():
        for kb, vb in B.items():
            k = tuple(x + y for x, y in zip(ka, kb))
            out[k] = out.get(k, 0) + va * vb
    return {k: v for k, v in out.items() if v}


def Mtable(N, maxp):
    """M(p,q) = singlet multiplicity in N^(x)p (x) Nbar^(x)q, exact integers."""
    zk = ct_monomials(N)
    one = {tuple([0] * (N - 1)): 1}
    fund, anti = {}, {}
    for z in zk:
        fund[z] = fund.get(z, 0) + 1
        zi = tuple(-x for x in z)
        anti[zi] = anti.get(zi, 0) + 1
    W = dict(one)
    for k in range(N):
        for l in range(N):
            if k == l:
                continue
            r = tuple(x - y for x, y in zip(zk[k], zk[l]))
            W = pmul(W, {tuple([0] * (N - 1)): 1, r: -1})
    fac = 1
    for k in range(2, N + 1):
        fac *= k
    fp = [dict(one)]
    ap = [dict(one)]
    for _ in range(maxp):
        fp.append(pmul(fp[-1], fund))
        ap.append(pmul(ap[-1], anti))
    M = {}
    for p in range(maxp + 1):
        for q in range(maxp + 1):
            poly = pmul(pmul(fp[p], ap[q]), W)
            c = poly.get(tuple([0] * (N - 1)), 0)
            assert c % fac == 0, (N, p, q, c)
            M[(p, q)] = c // fac
    return M


def expand(N, NV, LINKS):
    """chi_H as {tuple over corners of (p_v,q_v): integer coefficient}."""
    matter = [((0, 0), 2), ((1, 0), 1)] if N == 2 else [((0, 0), 2), ((1, 0), 1), ((0, 1), 1)]
    terms = {tuple((0, 0) for _ in range(NV)): 1}
    for v in range(NV):
        nxt = {}
        for key, c in terms.items():
            for (dp, dq), cc in matter:
                k = list(key)
                k[v] = (k[v][0] + dp, k[v][1] + dq)
                k = tuple(k)
                nxt[k] = nxt.get(k, 0) + c * cc
        terms = nxt
    for (i, j) in LINKS:
        nxt = {}
        for key, c in terms.items():
            for v in (i, j):
                k = list(key)
                k[v] = (k[v][0] + 1, k[v][1])
                k = tuple(k)
                nxt[k] = nxt.get(k, 0) + c
        terms = nxt
    return terms


def haar(N, NV, LINKS):
    terms = expand(N, NV, LINKS)
    maxp = max(max(p + q for (p, q) in key) for key in terms) * 2 + 2
    M = Mtable(N, maxp)
    gauss = sum(c * int(np.prod([M[(p, q)] for (p, q) in key], dtype=object))
                for key, c in terms.items())
    items = list(terms.items())
    dimI = 0
    for k1, c1 in items:
        for k2, c2 in items:
            w = c1 * c2
            for v in range(NV):
                w *= M[(k1[v][0] + k2[v][1], k1[v][1] + k2[v][0])]
                if w == 0:
                    break
            dimI += w
    return int(gauss), int(dimI), len(terms)


m2, m3 = Mtable(2, 4), Mtable(3, 4)
g2p, i2p, nt2 = haar(2, 4, [(0, 1), (1, 2), (2, 3), (3, 0)])
check("B7 [exact, integer] the SU(N) Haar characters, a Weyl/Dyson constant term in integer "
      "arithmetic with no floating-point step, count singlets correctly (SU(3): M(0,0)=%d, "
      "M(1,0)=%d, M(1,1)=%d, M(3,0)=%d the epsilon_abc BARYON, M(2,2)=%d, M(3,3)=%d; SU(2): "
      "M(2,0)=%d, M(4,0)=%d) and CROSS-CHECK against PR #7914: on the SU(2) plaquette they "
      "reproduce the parent's Gauss dimension %d and dim I = %d by an independent route"
      % (m3[(0, 0)], m3[(1, 0)], m3[(1, 1)], m3[(3, 0)], m3[(2, 2)], m3[(3, 3)],
         m2[(2, 0)], m2[(4, 0)], g2p, i2p),
      m3[(0, 0)] == 1 and m3[(1, 0)] == 0 and m3[(1, 1)] == 1 and m3[(3, 0)] == 1
      and m3[(2, 2)] == 2 and m3[(3, 3)] == 6 and m2[(2, 0)] == 1 and m2[(4, 0)] == 2
      and g2p == 82 and i2p == 356306)

GEOM4 = dict(GEOM)
GEOM4["plaquette"] = (4, [(0, 1), (1, 2), (2, 3), (3, 0)])
TAB = {}
for gname, (NV, LINKS) in GEOM4.items():
    for N in (2, 3):
        g, di, nt = haar(N, NV, LINKS)
        TAB[(gname, N)] = (2 ** (N * NV) * (2 * N) ** len(LINKS),
                           (N + 1) ** NV * 2 ** len(LINKS), g, di)
check("B8 [exact, integer] exact dim(Gauss) / dim I for SU(3): dimer 4 / %d, 3-chain %d / %d, "
      "triangle %d / %d, PLAQUETTE %d / %d (inferred, not built). The dimer's 4 agrees with "
      "the eigen-decomposition of B6, the 3-chain's %d with the Cartan cut of C1; and "
      "dim(Gauss) <= dim(R n I) on every carrier"
      % (TAB[("dimer", 3)][3], TAB[("3-chain", 3)][2], TAB[("3-chain", 3)][3],
         TAB[("triangle", 3)][2], TAB[("triangle", 3)][3], TAB[("plaquette", 3)][2],
         TAB[("plaquette", 3)][3], TAB[("3-chain", 3)][2]),
      TAB[("dimer", 3)][2] == 4 and TAB[("3-chain", 3)][2] == 10
      and TAB[("triangle", 3)][2] == 14 and TAB[("plaquette", 3)][2] == 34
      and TAB[("plaquette", 3)][3] == 991584
      and all(g <= r for (_, r, g, _) in TAB.values()))

# ====================================== the SU(3) open 3-chain, carried sparsely

LAM = gellmann()
TT3 = [x / 2.0 for x in LAM]
TD3 = [x / 2.0 for x in LAM[:7]] + [np.diag([1, 1, -2]).astype(complex) / 2.0]
N, NV = 3, 3
CLINKS = [(0, 1), (1, 2)]
NE = len(CLINKS)
NMODE, DL = N * NV, 2 * N
DM, DLL = 2 ** NMODE, DL ** NE
CDIM = DM * DLL


def cjw(m):
    return kron_sparse([sp.csr_matrix(SZ if k < m else (ANN if k == m else I2))
                        for k in range(NMODE)])


IL = sp.identity(DLL, format="csr", dtype=complex)
ID = sp.identity(DM, format="csr", dtype=complex)
CPSI = {(v, a): sp.kron(cjw(N * v + a), IL, format="csr")
        for v in range(NV) for a in range(N)}


def cemb(e, op):
    return sp.kron(ID, kron_sparse([sp.csr_matrix(op) if k == e
                                    else sp.identity(DL, format="csr", dtype=complex)
                                    for k in range(NE)]), format="csr")


CPI = np.diag([1.0] * N + [0.0] * N).astype(complex)
CPJ = np.diag([0.0] * N + [1.0] * N).astype(complex)
Z0 = sp.csr_matrix((CDIM, CDIM), dtype=complex)


def cends(v):
    out = []
    for e, (i, j) in enumerate(CLINKS):
        if i == v:
            out.append((e, CPI))
        if j == v:
            out.append((e, CPJ))
    return out


def cbuild(TAB_):
    RHO, EF, G = {}, {}, {}
    for v in range(NV):
        for a in range(8):
            acc = Z0
            for p in range(3):
                for q in range(3):
                    c = TAB_[a][p, q]
                    if c != 0:
                        acc = acc + c * (CPSI[(v, p)].getH() @ CPSI[(v, q)])
            RHO[(v, a)] = acc.tocsr()
            g = acc
            for (e, P) in cends(v):
                EF[(e, v, a)] = cemb(e, P @ np.kron(I2, TAB_[a]))
                g = g + EF[(e, v, a)]
            G[(v, a)] = g.tocsr()
    return RHO, EF, G


cRHO, cEF, cG = cbuild(TT3)
cNF = {v: sum((CPSI[(v, a)].getH() @ CPSI[(v, a)] for a in range(3)), Z0).tocsr()
       for v in range(NV)}
cQ = {v: (cNF[v] + sum((cemb(e, P) for (e, P) in cends(v)), Z0)).tocsr() for v in range(NV)}
cqv = np.array([np.real(cQ[v].diagonal()) for v in range(NV)])
cnfv = np.array([np.real(cNF[v].diagonal()) for v in range(NV)])
coev = np.array([np.real(cemb(e, CPJ).diagonal()) for e in range(NE)])
keyk = np.zeros(CDIM, dtype=np.int64)
for row in list(cnfv) + list(coev):
    keyk = keyk * 5 + np.rint(row).astype(np.int64)
_, CLAB = np.unique(keyk, return_inverse=True)
CNCOMP = int(CLAB.max()) + 1

cd3 = np.array([np.real(cG[(v, 2)].diagonal()) for v in range(NV)])
cd8 = np.array([np.real(cG[(v, 7)].diagonal()) for v in range(NV)])
CUT = np.where(np.all(np.abs(cd3) < 1e-12, axis=0)
               & np.all(np.abs(cd8) < 1e-12, axis=0))[0]
cRA = [(cG[(v, 0)] + 1j * cG[(v, 1)]).tocsr() for v in range(NV)] \
    + [(cG[(v, 3)] + 1j * cG[(v, 4)]).tocsr() for v in range(NV)] \
    + [(cG[(v, 5)] + 1j * cG[(v, 6)]).tocsr() for v in range(NV)]
AR = sum((E.getH() @ E for E in cRA), Z0).tocsr()
Bcut = AR[CUT][:, CUT].toarray()
Bcut = 0.5 * (Bcut + Bcut.conj().T)
evb, vb = np.linalg.eigh(Bcut)
CNZ = int(np.sum(evb < 1e-9))
CVG = np.zeros((CDIM, CNZ), dtype=complex)
CVG[CUT] = vb[:, :CNZ]
cres = max(float(np.abs(cG[(v, a)] @ CVG).max()) for v in range(NV) for a in range(8))
ACAS = sum((cG[(v, a)] @ cG[(v, a)] for v in range(NV) for a in range(8)), Z0).tocsr()
npat_c = int(np.sum(np.abs(np.real(ACAS.diagonal())) < 1e-12))


def cpg(T):
    return CVG.conj().T @ (T @ CVG)


chull = np.where(np.abs(np.einsum('ij,ij->i', CVG, CVG.conj())).real > 1e-12)[0]
cch = np.unique(CLAB[chull])
ctr, crk, cidem = [], [], 0.0
for c in cch:
    idx = np.zeros(CDIM)
    idx[CLAB == c] = 1.0
    Pc = cpg(sp.diags(idx).tocsr())
    ctr.append(round(float(np.trace(Pc).real), 9))
    crk.append(int(np.linalg.matrix_rank(Pc, tol=1e-9)))
    cidem = max(cidem, float(np.abs(Pc @ Pc - Pc).max()))
check("C1 [numerical, 1e-9] the same on the open 3-CHAIN (dim H = %d, dim(R n I) = %d = 4^3 x "
      "2^2, sparse): the Cartan cut G_v^3 = G_v^8 = 0 holds %d record patterns and the joint "
      "kernel of sum (G^+)^dag G^+ inside it is %d-dimensional, annihilated by all 24 "
      "generators to %.2e, matching B8; %d record patterns solve the Gauss law; R n I on the "
      "sector is again COMPLETE -- hull %d patterns meeting %d of the %d classes, all rank "
      "one (max|P^2-P| = %.1e), traces summing to %d"
      % (CDIM, CNCOMP, len(CUT), CNZ, cres, npat_c, len(chull), len(cch), CNCOMP, cidem,
         int(round(sum(ctr)))),
      CNZ == 10 and cres < 1e-12 and npat_c == 0 and cidem < 1e-9 and crk == [1] * 10
      and abs(sum(ctr) - CNZ) < 1e-9 and CNCOMP == 256)

# ====================================== C -- T3, triality

tri_re = np.exp(2j * np.pi * C3.qv[0] / 3.0)
tri_ok = in_I_exact(C3, np.diag(tri_re)) and offdiag_nnz(np.diag(tri_re)) == 0
tri_hull = sorted({(int(round(C3.qv[0][r])) % 3, int(round(C3.qv[1][r])) % 3) for r in hull})
ctriset = sorted({tuple(int(round(cqv[v][r])) % 3 for v in range(NV)) for r in chull})
check("C2 [exact] TRIALITY REGISTERS: omega^{Q_v}, omega = e^{2 pi i/3}, is record-diagonal "
      "AND commutes with all 16 G_v^a (nnz = 0), so it is an element of R n I; and the Gauss "
      "sector sits entirely at TRIALITY ZERO -- over its record hull the triality tuple takes "
      "only %s on the dimer and only %s on the 3-chain" % (tri_hull, ctriset),
      tri_ok and tri_hull == [(0, 0)] and ctriset == [(0, 0, 0)])

K = [sum(C3.G_t[(v, a)] for v in range(2)) for a in range(8)]
A1c = sum(C3.G_t[(1, a)] @ C3.G_t[(1, a)] for a in range(8))
A1c = 0.5 * (A1c + A1c.conj().T)
e1, V1 = np.linalg.eigh(A1c)
S1 = V1[:, e1 < 1e-9]                     # exact singlet at corner 1
RA = [C3.G_t[(0, 0)] + 1j * C3.G_t[(0, 1)],
      C3.G_t[(0, 3)] + 1j * C3.G_t[(0, 4)],
      C3.G_t[(0, 5)] + 1j * C3.G_t[(0, 6)]]
Braise = sum(S1.conj().T @ (E.conj().T @ E) @ S1 for E in RA)
Braise = 0.5 * (Braise + Braise.conj().T)
w3 = S1.conj().T @ C3.G_t[(0, 2)] @ S1
w8 = S1.conj().T @ C3.G_t[(0, 7)] @ S1
Mhw = Braise + (w3 - 0.5 * np.eye(S1.shape[1])) @ (w3 - 0.5 * np.eye(S1.shape[1])) \
    + (w8 - (1.0 / (2 * np.sqrt(3))) * np.eye(S1.shape[1])) \
    @ (w8 - (1.0 / (2 * np.sqrt(3))) * np.eye(S1.shape[1]))
Mhw = 0.5 * (Mhw + Mhw.conj().T)
em, Vm = np.linalg.eigh(Mhw)
NHW = int(np.sum(em < 1e-9))
psi_p = S1 @ (Vm[:, :NHW] @ np.ones(NHW))    # DECLARED uniform combination, no seed
psi_p /= np.linalg.norm(psi_p)
psi_2 = (C3.G_t[(0, 0)] - 1j * C3.G_t[(0, 1)]) @ psi_p
psi_2 /= np.linalg.norm(psi_2)
psi_3 = (C3.G_t[(0, 3)] - 1j * C3.G_t[(0, 4)]) @ psi_p
psi_3 /= np.linalg.norm(psi_3)
TRIP = [psi_p, psi_2, psi_3]


def ex(Mx, x):
    return float(np.vdot(x, Mx @ x).real)


sres = max(float(np.linalg.norm(C3.G_t[(1, a)] @ x)) for a in range(8) for x in TRIP)
c0 = [ex(CAS[0], x) for x in TRIP]
wgt = [(ex(C3.G_t[(0, 2)], x), ex(C3.G_t[(0, 7)], x)) for x in TRIP]
q0 = [ex(C3.Q[0], x) for x in TRIP]
check("C3 [numerical, 1e-11] a colour TRIPLET at corner 0: %d highest-weight vectors at "
      "weight (1/2, 1/(2 sqrt 3)); psi_1 and its partners psi_2 = G_0^- psi_1, psi_3 = V_0^- "
      "psi_1 are exact singlets at corner 1 (max ||G_1^a psi|| = %.2e), all carry <C_0> = "
      "%.9f = 4/3, the fundamental 3, and the abelian charge <Q_0> = %.9f identically"
      % (NHW, sres, c0[0], q0[0]),
      sres < 1e-11 and all(abs(x - 4.0 / 3.0) < 1e-9 for x in c0)
      and max(abs(q0[i] - q0[0]) for i in range(3)) < 1e-9
      and abs(wgt[0][0] - 0.5) < 1e-9 and abs(wgt[1][0] + 0.5) < 1e-9 and abs(wgt[2][0]) < 1e-9)


def expm_apply(Aop, x, n=120):
    y, t = x.copy(), x.copy()
    for k in range(1, n + 1):
        t = (Aop @ t) / k
        y = y + t
        if np.abs(t).max() < 1e-18:
            break
    return y


theta = 0.7
psi_t = expm_apply(-1j * theta * K[0], psi_p)
psi_t /= np.linalg.norm(psi_t)
Pspan = sum(np.outer(x, x.conj()) for x in TRIP)
resid = float(np.linalg.norm(psi_t - Pspan @ psi_t))
pp = np.abs(psi_p) ** 2
tvs = [0.5 * float(np.abs(pp - np.abs(x) ** 2).sum()) for x in (psi_2, psi_3)]
tv1t = 0.5 * float(np.abs(pp - np.abs(psi_t) ** 2).sum())


def coarse(p):
    return np.bincount(lab3, weights=p, minlength=n3)


cp = coarse(pp)
dev = max(float(np.abs(coarse(np.abs(x) ** 2) - cp).max()) for x in (psi_2, psi_3, psi_t))
worst_scan = 0.0
for a in range(8):
    for th in ANGLES:
        x = expm_apply(-1j * th * K[a], psi_p)
        x /= np.linalg.norm(x)
        worst_scan = max(worst_scan, float(np.abs(coarse(np.abs(x) ** 2) - cp).max()))
check("C4 [numerical, 1e-14] colour-rotated states are MAXIMALLY DISTINCT in the raw records "
      "and IDENTICAL in every readable gauge-invariant statistic, on the dimer: U(theta) = "
      "exp(-i theta sum_v G_v^a) holds the state in span{psi_1,psi_2,psi_3} to %.2e with "
      "|<psi_1|psi_theta>|^2 = %.9f = cos^2(theta/2), declared theta = 0.7; the FINE record "
      "distributions are at total-variation distance %.12f and %.12f (disjoint supports), "
      "psi_theta at %.12f; over the %d atoms of R n I (%d carry weight) the deviation is at "
      "most %.3e, and over the DECLARED scan of ALL 8 su(3) axes x 5 angles (0.3, 0.7, 1.1, "
      "2.0, pi) at most %.3e"
      % (resid, abs(np.vdot(psi_p, psi_t)) ** 2, tvs[0], tvs[1], tv1t, n3,
         int((cp > 1e-14).sum()), dev, worst_scan),
      resid < 1e-12 and abs(abs(np.vdot(psi_p, psi_t)) ** 2 - np.cos(theta / 2) ** 2) < 1e-9
      and all(abs(t - 1.0) < 1e-12 for t in tvs) and dev < 1e-14 and worst_scan < 1e-14)

A12 = sum((cG[(v, a)].getH() @ cG[(v, a)] for v in (1, 2) for a in range(8)), Z0).tocsr()
SEL = np.where((np.abs(cd3[0] - 0.5) < 1e-12) & (np.abs(cd8[0] - 1.0 / (2 * np.sqrt(3))) < 1e-12)
               & np.all(np.abs(cd3[1:]) < 1e-12, axis=0)
               & np.all(np.abs(cd8[1:]) < 1e-12, axis=0))[0]
cRA0 = [(cG[(0, 0)] + 1j * cG[(0, 1)]).tocsr(), (cG[(0, 3)] + 1j * cG[(0, 4)]).tocsr(),
        (cG[(0, 5)] + 1j * cG[(0, 6)]).tocsr()]
Bc = (sum((E.getH() @ E for E in cRA0), Z0) + A12).tocsr()[SEL][:, SEL].toarray()
Bc = 0.5 * (Bc + Bc.conj().T)
eo, vo = np.linalg.eigh(Bc)
KO = int(np.sum(eo < 1e-9))
cpsi1 = np.zeros(CDIM, dtype=complex)
cpsi1[SEL] = vo[:, :KO] @ np.ones(KO)               # DECLARED uniform combination
cpsi1 /= np.linalg.norm(cpsi1)
cpsi2 = (cG[(0, 0)] - 1j * cG[(0, 1)]) @ cpsi1
cpsi2 /= np.linalg.norm(cpsi2)
cpsi3 = (cG[(0, 3)] - 1j * cG[(0, 4)]) @ cpsi1
cpsi3 /= np.linalg.norm(cpsi3)
CTRIP = [cpsi1, cpsi2, cpsi3]
csres = max(float(np.linalg.norm(cG[(v, a)] @ x))
            for v in (1, 2) for a in range(8) for x in CTRIP)
CCAS0 = sum((cG[(0, a)] @ cG[(0, a)] for a in range(8)), Z0).tocsr()
cc0 = [float(np.vdot(x, CCAS0 @ x).real) for x in CTRIP]
cK = [sum((cG[(v, a)] for v in range(NV)), Z0).tocsr() for a in range(8)]
cpp = np.abs(cpsi1) ** 2


def ccoarse(p):
    return np.bincount(CLAB, weights=p, minlength=CNCOMP)


ccp = ccoarse(cpp)
ctvs = [0.5 * float(np.abs(cpp - np.abs(x) ** 2).sum()) for x in (cpsi2, cpsi3)]
cdevs = [float(np.abs(ccoarse(np.abs(x) ** 2) - ccp).max()) for x in (cpsi2, cpsi3)]
cworst_scan, cworst_tv = 0.0, 0.0
for a in range(8):
    for th in ANGLES:
        x = expm_apply(-1j * th * cK[a], cpsi1)
        x /= np.linalg.norm(x)
        px = np.abs(x) ** 2
        cworst_scan = max(cworst_scan, float(np.abs(ccoarse(px) - ccp).max()))
        cworst_tv = max(cworst_tv, 0.5 * float(np.abs(px - cpp).sum()))
check("C5 [numerical, 1e-13] the same on the 3-chain: %d highest-weight vectors, corners 1 "
      "and 2 exact singlets (max ||G_v^a psi|| = %.2e), <C_0> = %.9f = 4/3; the FINE record "
      "distributions of psi_1 and its partners are at total-variation distance %s and the "
      "largest fine TV over the declared 8 axes x 5 angles is %.6f, while over the %d atoms "
      "of R n I (%d carry weight) the READABLE distributions differ by at most %.3e "
      "(partners) and %.3e (whole scan)"
      % (KO, csres, cc0[0], [float(round(t, 12)) for t in ctvs], cworst_tv, CNCOMP,
         int((ccp > 1e-14).sum()), max(cdevs), cworst_scan),
      KO > 0 and csres < 1e-11 and all(abs(x - 4.0 / 3.0) < 1e-9 for x in cc0)
      and all(abs(t - 1.0) < 1e-12 for t in ctvs) and max(cdevs) < 1e-13
      and cworst_scan < 1e-13 and cworst_tv > 0.1)

tests = []
for v in range(2):
    for a in range(8):
        tests.append(C3.RHO_t[(v, a)])          # colour OCTET (matter)
        tests.append(C3.EF_t[(0, 'i', a)])      # colour OCTET (link)
for a in range(3):
    tests.append(C3.PSI[(0, a)])                # colour TRIPLET
    tests.append(C3.PSI[(0, a)].conj().T)       # colour ANTI-TRIPLET
tests.append(sum(C3.RHO_t[(v, 0)] for v in range(2)))
tests.append(2 * C3.RHO_t[(0, 2)])              # a single colour RECORD VALUE
tests.append(2 * C3.EF_t[(0, 'i', 2)])
worst = max(float(np.abs(pg(T)).max()) for T in tests)
ctests = []
for v in range(NV):
    for a in range(8):
        ctests.append(cRHO[(v, a)])
for a in range(8):
    ctests.append(cEF[(0, 0, a)])
for a in range(3):
    ctests.append(CPSI[(0, a)])
    ctests.append(CPSI[(0, a)].getH())
ctests.append(sum((cRHO[(v, 0)] for v in range(NV)), Z0).tocsr())
ctests.append((2 * cRHO[(0, 2)]).tocsr())
ctests.append((2 * cG[(0, 2)]).tocsr())
ctests.append((2 * cG[(0, 7)]).tocsr())
cworst = max(float(np.abs(cpg(T)).max()) for T in ctests)
sing_ops = [C3.Q[0], C3.H, sum(E2[(0, s)] for s in ('i', 'j')), np.diag(tri_re)]
ranks = [int(np.linalg.matrix_rank(pg(M), tol=1e-9)) for M in sing_ops]
cE2X = sum((sp.csr_matrix((4.0 / 3.0) * cemb(e, P))
            for e in range(NE) for P in (CPI, CPJ)), Z0).tocsr()
ctri_op = sp.diags(np.exp(2j * np.pi * cqv[0] / 3.0)).tocsr()
cranks = [int(np.linalg.matrix_rank(cpg(M), tol=1e-9)) for M in (cQ[0], cE2X, ctri_op)]
check("C6 [numerical, 1e-12] every colour OCTET, TRIPLET and ANTI-TRIPLET tensor has a ZERO "
      "Gauss-sector block: over %d on the dimer (16 rho_v^a, 8 E^a_{e,i}, 3 psi_{0,a}, 3 "
      "psi^dag_{0,a}, the global colour charge, and the single colour record values 2 rho_0^3 "
      "and 2 E^3_{0,i}) max |P_G T P_G| = %.3e, and over %d on the 3-chain (24 rho_v^a, 8 "
      "E^a, 3 psi_{0,a}, 3 psi^dag_{0,a}, the global colour charge, 2 rho_0^3, 2 G_0^3, 2 "
      "G_0^8) %.3e. The SINGLET readouts Q_0, H_hop, sum E^2, omega^{Q_0} have blocks of rank "
      "%s of 4 and %s of 10" % (len(tests), worst, len(ctests), cworst, ranks, cranks),
      len(tests) == 41 and worst < 1e-12 and len(ctests) == 42 and cworst < 1e-12
      and all(r > 0 for r in ranks) and all(r > 0 for r in cranks))

tri_dist = []
for x in TRIP + [psi_t, VG[:, 0]]:
    p = np.abs(x) ** 2
    tri_dist.append(tuple(round(float(p[(np.rint(C3.qv[0]).astype(int) % 3) == k].sum()), 9)
                          for k in range(3)))
ctri_rows = []
for x in CTRIP + [CVG[:, 0]]:
    p = np.abs(x) ** 2
    ctri_rows.append(tuple(round(float(p[(np.rint(cqv[0]).astype(int) % 3) == k].sum()), 9)
                           for k in range(3)))
bary = [r for r in chull if int(round(cnfv[0][r])) == 3]
check("C7 [numerical, 1e-9] what records DO register of an uncompensated colour source is the "
      "Z_3 TRIALITY charge: P[Q_0 = k mod 3] reads %s for psi_1, psi_2, psi_3 and psi_theta "
      "alike -- triality 2 with certainty, identical across the triplet -- against %s for a "
      "Gauss-sector state, and the same on the 3-chain. That hull contains the epsilon_abc "
      "BARYON: %d of its %d patterns carry n^f_0 = 3, the SU(3) singlet channel with no SU(2) "
      "analogue" % (tri_dist[0], tri_dist[4], len(bary), len(chull)),
      all(t == tri_dist[0] for t in tri_dist[:4]) and max(tri_dist[0]) > 1 - 1e-9
      and abs(tri_dist[4][0] - 1.0) < 1e-9
      and ctri_rows[0] == ctri_rows[1] == ctri_rows[2]
      and abs(ctri_rows[3][0] - 1.0) < 1e-9 and len(bary) == 21)

# ====================================== D -- T4, the two corrections

fracR = []
for gname, (NV_, LINKS_) in GEOM4.items():
    row = []
    for Nx in (1, 2, 3):
        row.append(((Nx + 1) ** NV_ * 2 ** len(LINKS_))
                   / (2 ** (Nx * NV_) * (2 * Nx) ** len(LINKS_)))
    fracR.append((gname, row))
fracI = {}
for gname in GEOM4:
    for Nx in (2, 3):
        DIMx, RIx, gx, dix = TAB[(gname, Nx)]
        fracI[(gname, Nx)] = RIx / dix
mono_up = all(fracI[(g, 3)] > fracI[(g, 2)] for g in GEOM4)
mono_down = all(all(r[k] > r[k + 1] for k in range(2)) for _, r in fracR)
check("D1 [exact, integer] the readable fraction of I is NOT monotone in N, while the "
      "readable fraction of R is. dim(R n I)/dim I is LARGER for SU(3) than for SU(2) on "
      "EVERY geometry -- plaquette %.3e against %.3e, dimer %.3e/%.3e, 3-chain %.3e/%.3e, "
      "triangle %.3e/%.3e -- because (N+1)^V 2^E grows polynomially while dim I is throttled "
      "by the tightening singlet constraint (SU(3) needs p - q = 0 mod 3). dim(R n I)/dim R "
      "instead falls monotonically: on the plaquette 1, %.6f, %.6f. The qualitative cut is "
      "N-independent; the numerical fraction is not"
      % (fracI[("plaquette", 3)], fracI[("plaquette", 2)], fracI[("dimer", 3)],
         fracI[("dimer", 2)], fracI[("3-chain", 3)], fracI[("3-chain", 2)],
         fracI[("triangle", 3)], fracI[("triangle", 2)],
         fracR[3][1][1], fracR[3][1][2]),
      mono_up and mono_down and abs(fracI[("plaquette", 3)] - 4.131e-3) < 1e-6
      and abs(fracI[("plaquette", 2)] - 3.637e-3) < 1e-6)

g3_in_R = all(offdiag_nnz(C3.G_d[(v, 2)]) == 0 for v in range(2)) \
    and all(offdiag_nnz(C3.G_d[(v, 7)]) == 0 for v in range(2))
g3_in_I = any(in_I_exact(C3, C3.G_d[(v, a)]) for v in range(2) for a in (2, 7))
g3_blk = max(float(np.abs(pg(C3.G_t[(v, a)])).max()) for v in range(2) for a in (2, 7))
rf = tuple(round(2 * ex(C3.RHO_t[(0, 2)], x), 9) for x in TRIP + [psi_t])
check("D2 [exact] the pattern is CENTRE AND u(1)-CHARGE DATA, not centre and Cartan: both "
      "Cartan generators G_v^3, G_v^8 are record-diagonal (0 off-diagonal entries, so in R) "
      "and NOT in I, with identically vanishing Gauss-sector blocks, max = %.1e. The "
      "frame-dependent readout 2 <rho_0^3> -- in R, not in I -- reports %s on the four "
      "triplet states: it separates them, which is why it is not a physical readout"
      % (g3_blk, rf),
      g3_in_R and not g3_in_I and g3_blk < 1e-12 and len({rf[0], rf[1]}) == 2)

print("SUMMARY: for SU(3) as for SU(2), the record-readable AND gauge-invariant algebra is "
      "the abelian record data, dim (N+1)^V 2^E, generated by {Q_v} u {E^2_{e,end}}, "
      "colour-blind, and a complete commuting set of rank-one projectors on the Gauss sector. "
      "The Z_3 triality omega^{Q_v} registers, the Gauss sector sits at triality zero, colour "
      "octets and triplets have zero Gauss-sector blocks, and colour-rotated states are at "
      "total-variation distance 1 in the raw records and identical to 1e-16 in every readable "
      "gauge-invariant statistic. The readable gauge-invariant data are the centre and the "
      "u(1) charges, not the Cartan; the readable fraction of I does not shrink with N.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
if time.time() - T0 > AUDIT_TIMEOUT_SEC:
    print("WARNING: runtime %.1f s exceeded the declared %d s budget"
          % (time.time() - T0, AUDIT_TIMEOUT_SEC), file=sys.stderr)
sys.exit(0 if FAIL == 0 else 1)
