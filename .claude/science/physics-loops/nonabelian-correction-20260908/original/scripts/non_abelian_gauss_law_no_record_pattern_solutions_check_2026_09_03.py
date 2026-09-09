#!/usr/bin/env python3
"""A non-abelian Gauss law has no record-pattern solutions on one plaquette.

Self-contained finite-block runner.  Everything it builds is DECLARED design,
derived from no axiom:

  geometry  one coarse plaquette, corners v = 0,1,2,3 in a cycle, links
            e_k = (i = k, j = k+1 mod 4), k = 0..3;
  matter    a fermion DOUBLET per corner -- two encoded modes psi_{v,alpha} on
            two code layers, the layer index being the internal ("colour")
            label -- 8 modes, Jordan-Wigner encoded, mode index 2v + alpha;
  link      the minimal SU(2)/U(2) QUANTUM LINK: the one-rishon (N_e = 1)
            sector of the rishon construction, a FOUR-dimensional link space
            span{|i,0>, |i,1>, |j,0>, |j,1>} = (orientation record) x (colour
            record), i.e. TWO DESIGNED RECORDS per link and exactly the
            carrier of QUBIT_LINK_U2_CONNECTION_ALGEBRA_..._2026-06-04, with
                U_e^{ab} = c_{e,i,a} c^dag_{e,j,b} = -|j,b><i,a|   (U U = 0)
                E^a_{e,v} = P_v (I x tau^a/2)                (electric field);
  law       H_hop = -t sum_e eta_e sum_{ab} [psi^dag_{i,a} psi_{j,b} U_e^{ab}
            + h.c.], eta = (1, 1, -1, -1) declared Kawamoto-Smit-style signs;
  Gauss     G_v^a = rho_v^a + sum_{e at v} E^a_{e,v} with rho_v^a =
            psi^dag_v (tau^a/2) psi_v, and Q_v = n^f_v + n^r_v, the u(1)
            summand of the local u(2).

  A  THE CONSTRUCTION.  dim = 2^8 x 4^4 = 65536 = 2^16 record patterns, the
     link carrier and its truncation, and the non-scalar plaquette holonomy.
  B  THE GAUGE ALGEBRA.  [G_v^a, H_hop] = 0, u(2) closure, cross-corner
     commuting, u(1) central.
  C  WHAT IS RECORD-DIAGONAL.  G_v^3 and Q_v pure Z; G_v^{1,2} and the corner
     Gauss Casimir not; the matter-only Casimir and the centre parity yes.
  D  THE RECORD CENSUS.  The 544-pattern Cartan cut, the 82-dimensional
     singlet sector, ZERO Gauss-invariant record patterns, and the abelian
     control on the same carrier.
  E  THE BASIS-INDEPENDENT OBSTRUCTION.  One corner forces a Schmidt-rank-2
     pair of colour records, so no single-site product basis works.
  F  SPECTRA.  The symmetric electric term as a c-number, E_0 = -sqrt 34, and
     the declared one-sided variant.

Every matrix entry of the generators, the link operators and the law is a
dyadic rational of magnitude <= 4, so all sparse sums and products are exact in
IEEE double and every zero test tagged [exact] is `== 0`, not a tolerance.  The
65536-dimensional space is carried sparsely throughout; apart from operator
diagonals read as vectors, the largest dense array formed anywhere is 544 x 544.
No random number is drawn.

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

NV, NE = 4, 4
LINKS = [(0, 1), (1, 2), (2, 3), (3, 0)]      # (left end i, right end j)
NMODE = 2 * NV                                 # 8 fermion modes
DM = 2 ** NMODE                                # 256 matter states
DL = 4                                         # 4-dim quantum link
DIM = DM * DL ** NE                            # 65536
ETA = [1.0, 1.0, -1.0, -1.0]                   # declared link signs

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TAU = [SX, SY, SZ]
EPS = np.zeros((3, 3, 3))
for (a_, b_, c_), s_ in [((0, 1, 2), 1), ((1, 2, 0), 1), ((2, 0, 1), 1),
                         ((0, 2, 1), -1), ((2, 1, 0), -1), ((1, 0, 2), -1)]:
    EPS[a_, b_, c_] = s_


def kron_list(mats):
    out = sp.identity(1, format="csr", dtype=complex)
    for m in mats:
        out = sp.kron(out, m, format="csr")
    return out


def jw_annihilate(m):
    """psi_m on NMODE qubits in the Jordan-Wigner encoding, qubit 0 leftmost."""
    mats = []
    for k in range(NMODE):
        if k < m:
            mats.append(SZ)
        elif k == m:
            mats.append(np.array([[0, 1], [0, 0]], dtype=complex))
        else:
            mats.append(I2)
    return kron_list([sp.csr_matrix(x) for x in mats])


CM = [jw_annihilate(m) for m in range(NMODE)]


def link_ops():
    """Pi, Pj, T^a, U^{ab} on the 4-dim one-rishon link space.

    Basis order |i,0>, |i,1>, |j,0>, |j,1>."""
    Pi = np.diag([1., 1., 0., 0.]).astype(complex)
    Pj = np.diag([0., 0., 1., 1.]).astype(complex)
    Ta = [np.kron(I2, t / 2.0).astype(complex) for t in TAU]
    U = [[np.zeros((4, 4), dtype=complex) for _ in range(2)] for _ in range(2)]
    for a in range(2):
        for b in range(2):
            U[a][b][2 + b, a] = -1.0          # U^{ab} = -|j,b><i,a|
    return Pi, Pj, Ta, U


PI4, PJ4, TA4, U4 = link_ops()
DLL = DL ** NE                                 # 256, link sector alone


def emb_matter(op):
    return sp.kron(op, sp.identity(DLL, format="csr", dtype=complex), format="csr")


def link_only(e, op):
    mats = [sp.csr_matrix(op) if k == e else sp.identity(DL, format="csr", dtype=complex)
            for k in range(NE)]
    return kron_list(mats)


def emb_link(e, op):
    return sp.kron(sp.identity(DM, format="csr", dtype=complex), link_only(e, op), format="csr")


PSI = {(v, a): emb_matter(CM[2 * v + a]) for v in range(NV) for a in range(2)}

RHO = {}
for v in range(NV):
    for a in range(3):
        acc = sp.csr_matrix((DIM, DIM), dtype=complex)
        for p in range(2):
            for q in range(2):
                coef = TAU[a][p, q] / 2.0
                if coef != 0:
                    acc = acc + coef * (PSI[(v, p)].getH() @ PSI[(v, q)])
        RHO[(v, a)] = acc.tocsr()

NF = {v: (PSI[(v, 0)].getH() @ PSI[(v, 0)] + PSI[(v, 1)].getH() @ PSI[(v, 1)]).tocsr()
      for v in range(NV)}

EFIELD, NR_END = {}, {}
for e in range(NE):
    for a in range(3):
        EFIELD[(e, 'i', a)] = emb_link(e, PI4 @ TA4[a])
        EFIELD[(e, 'j', a)] = emb_link(e, PJ4 @ TA4[a])
    NR_END[(e, 'i')] = emb_link(e, PI4)
    NR_END[(e, 'j')] = emb_link(e, PJ4)


def ends_at(v):
    out = []
    for e, (i, j) in enumerate(LINKS):
        if i == v:
            out.append((e, 'i'))
        if j == v:
            out.append((e, 'j'))
    return out


G, Q = {}, {}
for v in range(NV):
    for a in range(3):
        acc = RHO[(v, a)]
        for (e, s) in ends_at(v):
            acc = acc + EFIELD[(e, s, a)]
        G[(v, a)] = acc.tocsr()
    accq = NF[v]
    for (e, s) in ends_at(v):
        accq = accq + NR_END[(e, s)]
    Q[v] = accq.tocsr()


def build_hop(t=1.0):
    H = sp.csr_matrix((DIM, DIM), dtype=complex)
    for e, (i, j) in enumerate(LINKS):
        term = sp.csr_matrix((DIM, DIM), dtype=complex)
        for a in range(2):
            for b in range(2):
                term = term + (PSI[(i, a)].getH() @ PSI[(j, b)]) @ emb_link(e, U4[a][b])
        term = term + term.getH()
        H = H - t * ETA[e] * term
    return H.tocsr()


H_HOP = build_hop(1.0)


def nnz0(M):
    M = sp.csr_matrix(M).copy()
    M.eliminate_zeros()
    return int(M.nnz)


def offdiag_nnz(M):
    M = sp.coo_matrix(M)
    return int(np.count_nonzero(M.data[M.row != M.col]))


def maxabs(M):
    M = sp.csr_matrix(M)
    return 0.0 if M.nnz == 0 else float(np.abs(M.data).max())


def comm(A, B):
    return (A @ B - B @ A).tocsr()


def dyadic(M, bound=4.0):
    """True when every entry is k/4 with |entry| <= bound -- exact in IEEE double."""
    d = sp.csr_matrix(M).data
    if d.size == 0:
        return True
    r, i = 4.0 * d.real, 4.0 * d.imag
    return bool(np.all(r == np.round(r)) and np.all(i == np.round(i))
                and np.abs(d).max() <= bound)


print("declared: 4 corners, a fermion doublet each (8 JW modes); 4 minimal u(2) quantum links, 4-dim = "
      "2 designed records each; G_v^a = rho_v^a + sum_{e at v} E^a_{e,v}")

# ================================================== A -- the declared construction

car_ok = True
for m in range(NMODE):
    for n in range(NMODE):
        d = 1.0 if m == n else 0.0
        ac = CM[m] @ CM[n].getH() + CM[n].getH() @ CM[m]
        car_ok = car_ok and nnz0(ac - d * sp.identity(DM, format="csr", dtype=complex)) == 0
        car_ok = car_ok and nnz0(CM[m] @ CM[n] + CM[n] @ CM[m]) == 0
allops = [H_HOP] + [G[(v, a)] for v in range(NV) for a in range(3)] + [Q[v] for v in range(NV)]
check("A1 [exact] the declared block: a fermion doublet at each of 4 corners (8 Jordan-Wigner modes, "
      "exact anticommutators) and 4 minimal quantum links; dim = 2^8 x 4^4 = %d = 2^16 record patterns; "
      "H_hop Hermitian with %d nonzeros; every entry of the law and the generators is a dyadic rational "
      "of magnitude <= 4, so every [exact] zero test below is exact" % (DIM, nnz0(H_HOP)),
      car_ok and DIM == 65536 and nnz0(H_HOP) == 131072
      and nnz0(H_HOP - H_HOP.getH()) == 0 and all(dyadic(M) for M in allops))

fac_ok = (np.all(PI4 == np.kron(np.diag([1., 0.]), I2))
          and np.all(PJ4 == np.kron(np.diag([0., 1.]), I2))
          and np.all(PI4 + PJ4 == np.eye(4))
          and all(np.all(TA4[a] == np.kron(I2, TAU[a] / 2.0)) for a in range(3)))
uu_ok = all(np.all(U4[a][b] @ U4[c][d] == 0) for a in range(2) for b in range(2)
            for c in range(2) for d in range(2))
resol = sum(U4[a][b].conj().T @ U4[a][b] + U4[a][b] @ U4[a][b].conj().T
            for a in range(2) for b in range(2))
end_ok = True
for a in range(3):
    for b in range(3):
        lhs = (PI4 @ TA4[a]) @ (PI4 @ TA4[b]) - (PI4 @ TA4[b]) @ (PI4 @ TA4[a])
        rhs = sum(1j * EPS[a, b, c] * (PI4 @ TA4[c]) for c in range(3))
        end_ok = end_ok and np.all(lhs == rhs)
        end_ok = end_ok and np.all((PI4 @ TA4[a]) @ (PJ4 @ TA4[b]) == 0)
check("A2 [exact] the designed link: P_i + P_j = I (one rishon per link), the 4-dim space factorises as "
      "(orientation record) x (colour record), U^{ab} = c_{i,a} c^dag_{j,b} is truncated with U U = 0 in "
      "all 16 colour pairings and sum_{ab} (U^dag U + U U^dag) = 2 I in place of unitarity, and the two "
      "ends carry commuting su(2)s",
      fac_ok and uu_ok and np.all(resol == 2.0 * np.eye(4)) and end_ok)

WP = [[sp.csr_matrix((DLL, DLL), dtype=complex) for _ in range(2)] for _ in range(2)]
for a in range(2):
    for d in range(2):
        acc = sp.csr_matrix((DLL, DLL), dtype=complex)
        for b in range(2):
            for c in range(2):
                for x in range(2):
                    acc = acc + (link_only(0, U4[a][b]) @ link_only(1, U4[b][c])
                                 @ link_only(2, U4[c][x]) @ link_only(3, U4[x][d]))
        WP[a][d] = acc.tocsr()
half_tr = 0.5 * (WP[0][0] + WP[1][1])
tl_nnz = 0
for a in range(2):
    for d in range(2):
        blk = WP[a][d] - (half_tr if a == d else sp.csr_matrix((DLL, DLL), dtype=complex))
        tl_nnz += nnz0(blk)
wp_nnz = sum(nnz0(WP[a][d]) for a in range(2) for d in range(2))
check("A3 [exact] the plaquette holonomy U_p^{ad} = sum U_{01}^{ab} U_{12}^{bc} U_{23}^{cx} U_{30}^{xd} "
      "has %d nonzero entries and its traceless su(2) colour part %d: the designed link carries a colour "
      "holonomy, which the native-hop scalar-holonomy result of 2026-05-23 does not cover"
      % (wp_nnz, tl_nnz),
      wp_nnz == 32 and tl_nnz == 48)

# ==================================================== B -- the exact gauge algebra

check("B1 [exact] [G_v^a, H_hop] = 0 for all 12 pairs (v, a): the covariant hop is exactly gauge "
      "invariant under the local su(2)",
      all(nnz0(comm(G[(v, a)], H_HOP)) == 0 for v in range(NV) for a in range(3)))
check("B2 [exact] [Q_v, H_hop] = 0 at all 4 corners: the u(1) summand is conserved by the same law",
      all(nnz0(comm(Q[v], H_HOP)) == 0 for v in range(NV)))

clos_ok, cross_ok = True, True
for v in range(NV):
    for w in range(NV):
        for a in range(3):
            for b in range(3):
                lhs = comm(G[(v, a)], G[(w, b)])
                if v == w:
                    rhs = sp.csr_matrix((DIM, DIM), dtype=complex)
                    for c in range(3):
                        if EPS[a, b, c] != 0:
                            rhs = rhs + 1j * EPS[a, b, c] * G[(v, c)]
                    clos_ok = clos_ok and nnz0(lhs - rhs) == 0
                else:
                    cross_ok = cross_ok and nnz0(lhs) == 0
check("B3 [exact] closure [G_v^a, G_v^b] = i eps^{abc} G_v^c on all 36 same-corner pairs: an exact "
      "su(2) at each corner", clos_ok)
check("B4 [exact] [G_v^a, G_w^b] = 0 on all 108 cross-corner pairs, the two ends of a shared link "
      "annihilating each other", cross_ok)
check("B5 [exact] [Q_v, G_w^a] = 0 on all 48 pairs: the u(1) is central, so each corner carries an exact "
      "u(2) = su(2) + u(1) -- the repository's own link algebra -- as a gauge algebra",
      all(nnz0(comm(Q[v], G[(w, a)])) == 0 for v in range(NV) for w in range(NV) for a in range(3)))
mx12 = max(maxabs(comm(G[(v, 0)], G[(v, 1)])) for v in range(NV))
check("B6 [exact] genuinely non-abelian: max |[G_v^1, G_v^2]| = %.1f over the corners, every G_v^3 "
      "nonzero as an operator" % mx12,
      mx12 == 1.5 and all(nnz0(G[(v, 2)]) > 0 for v in range(NV)))

# ============================================== C -- what is and is not record-diagonal

off1 = sum(offdiag_nnz(G[(v, 0)]) for v in range(NV))
off2 = sum(offdiag_nnz(G[(v, 1)]) for v in range(NV))
check("C1 [exact] the record basis is the joint Z eigenbasis of the 8 fermion records and the 4 x 2 link "
      "records; G_v^3 and Q_v are pure Z at every corner, so both are record-diagonal",
      all(offdiag_nnz(G[(v, 2)]) == 0 and offdiag_nnz(Q[v]) == 0 for v in range(NV)))
check("C2 [exact] G_v^1 and G_v^2 are not: %d off-diagonal entries each, summed over the corners. G_v^1 "
      "is the Cartan generator of the same su(2) in a rotated colour frame, so G_v^3's readability is an "
      "artefact of aligning the record basis with tau^3" % off1,
      off1 == 393216 and off2 == 393216
      and all(offdiag_nnz(G[(v, a)]) > 0 for v in range(NV) for a in (0, 1)))

CAS = {v: (G[(v, 0)] @ G[(v, 0)] + G[(v, 1)] @ G[(v, 1)] + G[(v, 2)] @ G[(v, 2)]).tocsr()
       for v in range(NV)}
cas_off = sum(offdiag_nnz(CAS[v]) for v in range(NV))
check("C3 [exact] the corner Gauss Casimir sum_a (G_v^a)^2 is NOT record-diagonal: %d off-diagonal "
      "entries summed. Gauge invariance and record-diagonality are independent here" % cas_off,
      cas_off == 98304 and all(offdiag_nnz(CAS[v]) > 0 for v in range(NV)))

CASM = {v: (RHO[(v, 0)] @ RHO[(v, 0)] + RHO[(v, 1)] @ RHO[(v, 1)] + RHO[(v, 2)] @ RHO[(v, 2)]).tocsr()
        for v in range(NV)}
nfd = {v: np.asarray(NF[v].diagonal()).real for v in range(NV)}
casm_ok = all(offdiag_nnz(CASM[v]) == 0
              and np.all(np.asarray(CASM[v].diagonal()).real == 0.75 * nfd[v] * (2.0 - nfd[v]))
              for v in range(NV))
check("C4 [exact] the matter-only Casimir sum_a (rho_v^a)^2 IS record-diagonal and equals "
      "(3/4) n_v (2 - n_v) exactly at all 65536 patterns and every corner: whether the matter at a corner "
      "is colourless registers, as whether n_v is even", casm_ok)

qd = np.array([np.asarray(Q[v].diagonal()).real for v in range(NV)])
qi = qd.astype(np.int64)
n_even = int(np.count_nonzero(np.all(qi % 2 == 0, axis=0)))
check("C5 [exact] the centre parity Q_v even is record-diagonal, integer-valued and colour-frame-free, "
      "holding on %d of the 65536 patterns: necessary for colour neutrality, and the only frame-free "
      "colour content that registers" % n_even,
      n_even == 4096 and np.all(qd == qi))

# ======================================================== D -- the record census

d3 = np.array([np.asarray(G[(v, 2)].diagonal()).real for v in range(NV)])
cartan = np.where(np.all(d3 == 0.0, axis=0))[0]
n_cartan = int(cartan.size)
check("D1 [exact] the abelian Cartan cut: exactly %d of the 65536 record patterns have G_v^3 = 0 at every "
      "corner, and all %d also have Q_v even" % (n_cartan, n_cartan),
      n_cartan == 544 and bool(np.all(qi[:, cartan] % 2 == 0)))

GP = [(G[(v, 0)] + 1j * G[(v, 1)]).tocsr() for v in range(NV)]
GRAM = sp.csr_matrix((DIM, DIM), dtype=complex)
for g in GP:
    GRAM = GRAM + g.getH() @ g
GRAM = GRAM.tocsr()
gram_diag = np.asarray(GRAM.diagonal()).real
inv_pat = np.where((np.all(d3 == 0.0, axis=0)) & (gram_diag == 0.0))[0]
check("D2 [exact] ZERO of the 65536 record patterns is Gauss-invariant: a pattern lies in the joint "
      "kernel exactly when G_v^3 x = 0 for all v and the Gram diagonal sum_v ||G_v^+ x||^2 vanishes; %d "
      "pass both, by exact equality on quarter-integer entries, no tolerance" % int(inv_pat.size),
      int(inv_pat.size) == 0 and dyadic(GRAM, 8.0))

B = GRAM[cartan][:, cartan].toarray()
B = 0.5 * (B + B.conj().T)
evals, evecs = np.linalg.eigh(B)
TOL = 1e-9
nsing = int(np.sum(evals < TOL))
gap = float(evals[evals >= TOL].min())
V = evecs[:, :nsing]
check("D3 [numerical, %g] the singlet sector -- the joint kernel of the twelve G_v^a -- is %d-dimensional "
      "inside the %d-dimensional Cartan cut, the smallest nonzero raising-Gram eigenvalue on that cut "
      "being %.4f" % (TOL, nsing, n_cartan, gap),
      nsing == 82 and gap > 1.99)


def m_singlet(p):
    """Number of SU(2) singlets in the p-fold tensor power of the doublet."""
    mult = {Fr(0): 1}
    for _ in range(p):
        nm = {}
        for j, m in mult.items():
            for jj in ([j + Fr(1, 2)] if j == 0 else [j + Fr(1, 2), j - Fr(1, 2)]):
                nm[jj] = nm.get(jj, 0) + m
        mult = nm
    return mult.get(Fr(0), 0)


CP = [2 * m_singlet(p) + m_singlet(p + 1) for p in range(6)]
char_dim = 0
for choice in itertools.product([0, 1], repeat=NE):
    pv = [0] * NV
    for k, ch in enumerate(choice):
        pv[LINKS[k][ch]] += 1
    prod = 1
    for v in range(NV):
        prod *= CP[pv[v]]
    char_dim += prod
check("D4 [exact] independent cross-check by the SU(2)^4 Haar character integral "
      "dim = int prod_v dg_v prod_v (2 + chi_v) prod_e (chi_i + chi_j), c(p) = 2 M(p) + M(p+1) = %s: "
      "exact integer arithmetic gives %d" % (CP, char_dim),
      char_dim == 82 and CP == [2, 1, 2, 2, 4, 5])

P = V @ V.conj().T
diagP = np.real(np.diag(P))
max_off = float(np.abs(P - np.diag(np.diag(P))).max())
n_hull = int(np.count_nonzero(diagP > 1e-9))
max_diag = float(diagP.max())
check("D5 [numerical, 1e-9] the singlet projector is not record-diagonal: largest off-diagonal %.2f, "
      "largest diagonal %.4f, record hull exactly the %d-pattern Cartan cut, so 82 <= %d <= %d and the "
      "step from %d to 82 registers only through correlations"
      % (max_off, max_diag, n_hull, n_hull, n_cartan, n_cartan),
      abs(max_off - 0.25) < 1e-9 and n_hull == 544 and max_diag < 1 - 1e-6)

counts = {q0: int(np.count_nonzero(np.all(qi == q0, axis=0))) for q0 in (0, 1, 2, 3, 4)}
check("D6 [exact] abelian control on the SAME carrier: the u(1) Gauss law Q_v = q0 at every corner has "
      "%d record-pattern solutions at q0 = 2, %d at q0 = 1 and 3, none at 0 and 4 -- a nonempty condition "
      "on record values on the very block where the non-abelian law has none: %d against 0"
      % (counts[2], counts[1], counts[2]),
      counts == {0: 0, 1: 32, 2: 1312, 3: 32, 4: 0})

# ============================== E -- the corner obstruction, independent of any basis

c1 = np.zeros((4, 4), dtype=complex)
c2 = np.zeros((4, 4), dtype=complex)
c1[0, 1] = 1
c1[2, 3] = 1
c2[0, 2] = 1
c2[1, 3] = -1
cmm = [c1, c2]
rho_c = [sum(TAU[a][p, q] / 2 * (cmm[p].conj().T @ cmm[q]) for p in range(2) for q in range(2))
         for a in range(3)]
R_c = [PI4 @ TA4[a] for a in range(3)]
GB = [np.kron(rho_c[a], np.eye(4)) + np.kron(np.eye(4), R_c[a]) for a in range(3)]
CB = sum(g @ g for g in GB)
wb, VB = np.linalg.eigh(CB)
ker = VB[:, wb < 1e-10]
occ = np.diag(np.kron(np.diag([0., 1., 1., 2.]), np.eye(4))).real
rish = np.diag(np.kron(np.eye(4), PI4)).real
sel = np.where((occ == 1) & (rish == 1))[0]
sub = (ker @ ker.conj().T)[np.ix_(sel, sel)]
ws, Vs = np.linalg.eigh(sub)
inside = Vs[:, ws > 1 - 1e-10]
check("E1 [numerical, 1e-10] one corner alone, the 16-dim block (matter doublet Fock space x one link "
      "end): the corner singlet space is %d-dimensional, and inside the %d record patterns with one "
      "matter quantum and the rishon at this end exactly %d singlet state survives"
      % (ker.shape[1], len(sel), inside.shape[1]),
      ker.shape[1] == 5 and len(sel) == 4 and inside.shape[1] == 1)

psi = inside[:, 0] / np.linalg.norm(inside[:, 0])
Mm = psi.reshape(2, 2)
sv = np.linalg.svd(Mm, compute_uv=False)
red = Mm @ Mm.conj().T
check("E2 [numerical, 1e-12] that forced state is (|1>_m |0>_L - |0>_m |1>_L)/sqrt 2: Schmidt spectrum "
      "(%.6f, %.6f) across the two colour records, rank 2, reduced state maximally mixed. Schmidt rank is "
      "basis-free, so the corner condition is a condition on values in NO single-site product basis"
      % (sv[0], sv[1]),
      abs(sv[0] - 2 ** -0.5) < 1e-12 and abs(sv[1] - 2 ** -0.5) < 1e-12
      and np.abs(red - 0.5 * np.eye(2)).max() < 1e-12)

# ================================================================= F -- spectra

EL2 = sp.csr_matrix((DIM, DIM), dtype=complex)
for e in range(NE):
    for s in ('i', 'j'):
        for a in range(3):
            EL2 = EL2 + EFIELD[(e, s, a)] @ EFIELD[(e, s, a)]
EL2 = EL2.tocsr()
eld = np.asarray(EL2.diagonal()).real
check("F1 [exact] the symmetric electric term sum_e sum_ends sum_a (E^a)^2 is the c-number %.1f on the "
      "one-rishon sector -- an occupied end holds a doublet (3/4), an empty end a singlet (0), one end of "
      "each link occupied -- so g is inert and E_0(g) = E_0 + (3/2) g^2" % eld[0],
      offdiag_nnz(EL2) == 0 and bool(np.all(eld == 3.0)))

Hs = H_HOP[cartan][:, cartan].toarray()
Hsing = V.conj().T @ Hs @ V
Hsing = 0.5 * (Hsing + Hsing.conj().T)
ev = np.linalg.eigvalsh(Hsing)
check("F2 [numerical, 1e-10] in the 82-dim singlet sector the hop ground energy at t = 1 is "
      "E_0 = %.12f = -sqrt 34, the spectrum symmetric about zero with a 40-fold zero" % float(ev[0]),
      abs(float(ev[0]) + np.sqrt(34.0)) < 1e-10
      and abs(float(ev[0]) + float(ev[-1])) < 1e-10
      and int(np.count_nonzero(np.abs(ev) < 1e-10)) == 40)

E1S = sp.csr_matrix((DIM, DIM), dtype=complex)
for e in range(NE):
    for a in range(3):
        E1S = E1S + EFIELD[(e, 'i', a)] @ EFIELD[(e, 'i', a)]
E1S = E1S.tocsr()
e1d = np.asarray(E1S.diagonal()).real
E1ss = V.conj().T @ (E1S[cartan][:, cartan].toarray()) @ V
Hg = Hsing + 0.5 * (0.5 * (E1ss + E1ss.conj().T))
e0g = float(np.linalg.eigvalsh(0.5 * (Hg + Hg.conj().T))[0])
check("F3 [numerical, 1e-10] the DECLARED one-sided variant sum_e sum_a (E^a_{e,i})^2, supplied only "
      "because the symmetric term is inert, is nonconstant and commutes with all twelve G_v^a exactly; it "
      "gives E_0 = %.12f at g^2 = 1. It breaks link-reversal symmetry: a supplied crutch, not a result"
      % e0g,
      offdiag_nnz(E1S) == 0 and len(set(np.round(e1d, 12))) > 1
      and all(nnz0(comm(E1S, G[(v, a)])) == 0 for v in range(NV) for a in range(3))
      and abs(e0g + 5.126268164739) < 1e-10)

print("SUMMARY: on one plaquette with a designed fermion doublet per corner and the minimal u(2) quantum "
      "link, the gauge algebra is exact and the holonomy carries a colour part, while the non-abelian "
      "Gauss law has no record-pattern solutions: 0 of 65536, against 1312 for the abelian law on the "
      "same carrier. What registers of colour is the centre and one frame-dependent Cartan component.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
