#!/usr/bin/env python3
"""The record-readable gauge-invariant algebra is colour-blind, on one plaquette.

Self-contained finite-block runner.  The carrier is the SAME declared plaquette
as A_NON_ABELIAN_GAUSS_LAW_HAS_NO_RECORD_PATTERN_SOLUTIONS_..._2026-09-03 and
its construction code is reused unchanged; everything it builds is DECLARED
design, derived from no axiom:

  geometry  one coarse plaquette, corners v = 0,1,2,3 in a cycle, links
            e_k = (i = k, j = k+1 mod 4), k = 0..3;
  matter    a fermion DOUBLET per corner -- two encoded modes psi_{v,alpha} on
            two code layers, the layer index being the internal ("colour")
            label -- 8 modes, Jordan-Wigner encoded, mode index 2v + alpha;
  link      the minimal SU(2)/U(2) QUANTUM LINK: the one-rishon (N_e = 1)
            sector, a FOUR-dimensional link space span{|i,0>, |i,1>, |j,0>,
            |j,1>} = (orientation record) x (colour record), i.e. TWO DESIGNED
            RECORDS per link, with U_e^{ab} = c_{e,i,a} c^dag_{e,j,b} (U U = 0)
            and E^a_{e,v} = P_v (I x tau^a/2);
  law       H_hop = -t sum_e eta_e sum_{ab} [psi^dag_{i,a} psi_{j,b} U_e^{ab}
            + h.c.], eta = (1, 1, -1, -1), used only as an example element of I;
  Gauss     G_v^a = rho_v^a + sum_{e at v} E^a_{e,v}, Q_v = n^f_v + n^r_v.

  R  = operators diagonal in the declared record basis (record-readable).
  I  = the commutant of {G_v^a} (gauge-invariant).
  D  = the record map D(M) = sum_r P_r M P_r onto R.

  A  R, I AND THE EXACT REDUCTION.  The commutator identity, the record-mixing
     graph of G_v^{1,2}, and dim(R n I) = 1296 = 3^4 x 2^4.
  B  THE BASIS AND THE GENERATORS.  The components are the level sets of the
     abelian record data; {Q_v} u {E^2_{e,end}} generate all 1296; only 256 of
     the 65536 Pauli-Z strings lie in R n I; a single record value is not in I.
  C  THE RECORD MAP.  D(I) is NOT inside R n I (C_0 and P_0^{j=0}), so D and
     the Gauss projector do not commute; every rank >= 1 tensor has a zero
     Gauss-sector block; on the Gauss sector R n I is 82 rank-one projectors.
  D  COLOUR ROTATIONS.  An open-string state and its colour partner: the FINE
     record distributions have total-variation distance 1, the READABLE
     (R n I atom) distributions agree to 1e-16 over 3 axes x 4 angles.
  E  THE U(1) CONTROL, exact dim I, AND THE COLOUR FRAME.  For U(1) the Gauss
     generators are diagonal so R n I = R; exact-integer Haar characters give
     dim I = 356306; and R n I is unchanged by a gauge rotation of the frame.

Every matrix entry of the generators and the link operators is a dyadic
rational of magnitude <= 4, so all sparse sums and products are exact in IEEE
double and every zero test tagged [exact] is `== 0`, not a tolerance.  The
65536-dimensional space is carried sparsely throughout; apart from operator
diagonals read as vectors, the largest dense array formed anywhere is 544 x 544.
No random number is drawn: the colour rotations run on DECLARED angles by
Krylov exponentiation (expm_multiply), never a dense exponential.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import sys
import time
from itertools import product
from math import comb

import numpy as np
import scipy.sparse as sp
from scipy.sparse.csgraph import connected_components
from scipy.sparse.linalg import expm_multiply

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
ANGLES = (0.3, 0.7, 1.1, 2.0, np.pi)           # DECLARED rotation angles

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
TAU = [SX, SY, SZ]


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
    """Pi, Pj, T^a, U^{ab} on the 4-dim one-rishon link space."""
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
IOP = sp.identity(DIM, format="csr", dtype=complex)
ZERO = sp.csr_matrix((DIM, DIM), dtype=complex)


def nnz0(M):
    M = sp.csr_matrix(M).copy()
    M.eliminate_zeros()
    return int(M.nnz)


def offdiag_nnz(M):
    M = sp.coo_matrix(M)
    return int(np.count_nonzero(M.data[M.row != M.col]))


def comm(A, B):
    return (A @ B - B @ A).tocsr()


def in_I_exact(M):
    """[exact] is M in the commutant of all twelve G_v^a?  nnz == 0, no tolerance."""
    return all(nnz0(comm(M, G[(v, a)])) == 0 for v in range(NV) for a in range(3))


def dyadic(M, bound=4.0):
    """True when every entry is k/4 with |entry| <= bound -- exact in IEEE double."""
    d = sp.csr_matrix(M).data
    if d.size == 0:
        return True
    r, i = 4.0 * d.real, 4.0 * d.imag
    return bool(np.all(r == np.round(r)) and np.all(i == np.round(i))
                and np.abs(d).max() <= bound)


print("declared: 4 corners, a fermion doublet each (8 JW modes); 4 minimal u(2) quantum links "
      "(4-dim, 2 designed records each). R = record-diagonal; I = commutant of {G_v^a}; "
      "D(M) = sum_r P_r M P_r")

# ============================== A -- R, I, and the exact reduction to R n I

car_ok = True
for m in range(NMODE):
    for n in range(NMODE):
        d = 1.0 if m == n else 0.0
        ac = CM[m] @ CM[n].getH() + CM[n].getH() @ CM[m]
        car_ok = car_ok and nnz0(ac - d * sp.identity(DM, format="csr", dtype=complex)) == 0
        car_ok = car_ok and nnz0(CM[m] @ CM[n] + CM[n] @ CM[m]) == 0
allops = [H_HOP] + [G[(v, a)] for v in range(NV) for a in range(3)] + [Q[v] for v in range(NV)]
diag_ok = all(offdiag_nnz(G[(v, 2)]) == 0 and offdiag_nnz(Q[v]) == 0 for v in range(NV))
check("A1 [exact] the parent note's block reused unchanged: 8 JW modes with exact anticommutators, 4 "
      "minimal quantum links, dim R = dim H = 2^8 x 4^4 = %d; every generator entry a dyadic rational "
      "of magnitude <= 4, so every [exact] zero test below is exact; G_v^3 and Q_v pure Z, hence in R"
      % DIM,
      car_ok and DIM == 65536 and diag_ok and all(dyadic(M) for M in allops))

# the exact reduction:  for diagonal D,  [D, G]_{rs} = (d_r - d_s) G_{rs}
dtest = ((np.arange(DIM) % 5) - 2) / 4.0            # DECLARED dyadic diagonal, no seed
Dtest = sp.diags(dtest).tocsr()
red_ok = True
for v in range(NV):
    for a in range(3):
        lhs = sp.coo_matrix(comm(Dtest, G[(v, a)]))
        Gc = sp.coo_matrix(G[(v, a)])
        rhs = sp.coo_matrix(((dtest[Gc.row] - dtest[Gc.col]) * Gc.data, (Gc.row, Gc.col)),
                            shape=(DIM, DIM))
        red_ok = red_ok and nnz0(lhs - rhs) == 0
check("A2 [exact] the reduction: for diagonal D, [D, G]_{rs} = (d_r - d_s) G_{rs}, verified entrywise "
      "against sparse arithmetic on all twelve G_v^a. G_v^3 is diagonal so imposes nothing: D in R n I "
      "iff d_r = d_s wherever (G_v^1)_{rs} or (G_v^2)_{rs} is nonzero", red_ok)

rows, cols, tot_off = [], [], 0
for v in range(NV):
    for a in (0, 1):
        M = sp.coo_matrix(G[(v, a)])
        m = (M.row != M.col) & (M.data != 0)
        tot_off += int(m.sum())
        rows.append(M.row[m])
        cols.append(M.col[m])
rows = np.concatenate(rows)
cols = np.concatenate(cols)
ADJ = sp.coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(DIM, DIM)).tocsr()
NCOMP, LABELS = connected_components(ADJ, directed=False)
SIZES = np.bincount(LABELS)
check("A3 [exact] R n I = functions constant on the connected components of the graph cut by the "
      "off-diagonal support of G_v^{1,2} (%d edges): dim(R n I) = %d = 3^4 x 2^4 of dim R = %d, ratio "
      "%.6f; the component indicators are its minimal projections"
      % (tot_off, NCOMP, DIM, NCOMP / DIM),
      tot_off == 786432 and NCOMP == 1296 == 3 ** 4 * 2 ** 4
      and abs(NCOMP / DIM - 0.019775) < 1e-6)
check("A4 [exact] component sizes %s, summing to %d"
      % (sorted(set(SIZES.tolist())), SIZES.sum()),
      sorted(set(SIZES.tolist())) == [16, 32, 64, 128, 256] and int(SIZES.sum()) == DIM)

# ============================== B -- the basis, the generators, the monomials

nf = np.array([np.array(NF[v].diagonal()).real.astype(int) for v in range(NV)])
oe = np.array([np.array(NR_END[(e, 'j')].diagonal()).real.astype(int) for e in range(NE)])
qv = np.array([np.array(Q[v].diagonal()).real.astype(int) for v in range(NV)])
E2 = {}
for e in range(NE):
    for s in ('i', 'j'):
        acc = sum((EFIELD[(e, s, a)] @ EFIELD[(e, s, a)] for a in range(3)), ZERO).tocsr()
        E2[(e, s)] = acc
e2d = np.array([np.array(E2[(e, s)].diagonal()).real for e in range(NE) for s in ('i', 'j')])
casm = 0.75 * nf * (2 - nf)
par = qv % 2


def nlevels(arrs):
    """number of distinct joint values of a list of length-DIM dyadic arrays"""
    key = np.zeros(DIM, dtype=np.int64)
    for a in arrs:
        ai = np.rint(np.asarray(a) * 4).astype(np.int64)      # dyadic -> exact int
        key = key * (ai.max() - ai.min() + 1) + (ai - ai.min())
    return len(np.unique(key)), key


k_ab, key_ab = nlevels(list(nf) + list(oe))
pairs = np.unique(np.stack([LABELS, key_ab], axis=1), axis=0)
check("B1 [exact] the components are exactly the level sets of the abelian record data "
      "(n^f_v ; link orientation o_e): %d level sets, in bijection with the %d components"
      % (k_ab, NCOMP),
      k_ab == NCOMP == len(pairs) == 1296)

k_gen, _ = nlevels(list(qv) + list(e2d))
k_cas, _ = nlevels(list(casm))
k_par, _ = nlevels(list(par))
k_q, _ = nlevels(list(qv))
k_e2, _ = nlevels(list(e2d))
k_all, _ = nlevels(list(casm) + list(par) + list(qv) + list(e2d))
check("B2 [exact] {Q_v} u {E^2_{e,end}} have %d joint level sets: the abelian charges and the link-end "
      "electric Casimirs generate ALL of R n I. Alone: matter Casimirs (3/4)n_v(2-n_v) %d, centre "
      "parities (-1)^{Q_v} %d, link-end Casimirs %d, {Q_v} %d; all of it together %d. The singlet data "
      "are functions of the abelian data, not independent readable content"
      % (k_gen, k_cas, k_par, k_e2, k_q, k_all),
      k_gen == NCOMP and k_cas == 16 and k_par == 16 and k_e2 == 16 and k_q == 431
      and k_all == NCOMP)

PICKS = [0, 259, 518, 777, 1036, 1295]                        # DECLARED, no seed
six_ok = all(in_I_exact(sp.diags((LABELS == c).astype(float)).tocsr()) for c in PICKS)
gen_ok = (all(in_I_exact(sp.diags(qv[v].astype(float)).tocsr()) for v in range(NV))
          and all(in_I_exact(sp.diags(e2d[k]).tocsr()) for k in range(len(e2d)))
          and all(in_I_exact(sp.diags(casm[v]).tocsr()) for v in range(NV)))
check("B3 [exact] six declared component projectors P_c (c = %s) commute with all twelve G_v^a as "
      "sparse 65536-dim matrices, nnz = 0, no tolerance; so do every Q_v, E^2_{e,end} and matter "
      "Casimir" % PICKS, six_ok and gen_ok)


def local_ok(sets, subset):
    """is the Z-monomial on 'subset' of a 2-record factor constant on every set?"""
    def chi(bits):
        s = 1
        for q in subset:
            s *= (1 - 2 * bits[q])
        return s
    return all(len({chi(b) for b in S}) == 1 for S in sets)


MSETS = [[(0, 0)], [(1, 0), (0, 1)], [(1, 1)]]                # matter pair, by n_v
LSETS = [[(0, 0), (0, 1)], [(1, 0), (1, 1)]]                  # link (orient, colour), by o_e
SUBS = [(), (0,), (1,), (0, 1)]
mgood = [s for s in SUBS if local_ok(MSETS, s)]
lgood = [s for s in SUBS if local_ok(LSETS, s)]
nstr = len(mgood) ** NV * len(lgood) ** NE
check("B4 [exact] only %d of the %d Pauli-Z strings spanning R lie in R n I: per corner only "
      "{1, Z_1 Z_2} of 4 (Z_1 alone reads the colour), per link only {1, Z_orientation} of 4 (Z_colour "
      "reads the colour), 2^4 x 2^4. Since %d < %d, R n I is NOT spanned by record-value monomials; "
      "%d dimensions are carried by sums like Z_1 + Z_2 = 2 - 2 n_v"
      % (nstr, DIM, nstr, NCOMP, NCOMP - nstr),
      len(mgood) == 2 and len(lgood) == 2 and nstr == 256 and nstr < NCOMP)

big = int(np.where(SIZES > 1)[0][0])
r0 = int(np.where(LABELS == big)[0][0])
d1 = np.zeros(DIM)
d1[r0] = 1.0
check("B5 [exact] a single record value is not physical: the projector onto one record pattern (its "
      "component holds %d) does NOT commute with the twelve G_v^a, so R is not inside I"
      % SIZES[big], not in_I_exact(sp.diags(d1).tocsr()))

# ============================== C -- the record map D, and the Gauss sector

d3 = np.array([np.array(G[(v, 2)].diagonal()).real for v in range(NV)])
S3 = np.where(np.all(d3 == 0.0, axis=0))[0]
GP = [(G[(v, 0)] + 1j * G[(v, 1)]).tocsr() for v in range(NV)]
ARAISE = sum((g.getH() @ g for g in GP), ZERO).tocsr()
BG = ARAISE[S3][:, S3].toarray()
BG = 0.5 * (BG + BG.conj().T)
evg, evecg = np.linalg.eigh(BG)
NZ = int(np.sum(evg < 1e-9))
VG = evecg[:, :NZ]
check("C1 [numerical, 1e-9] the Gauss sector (joint kernel of the twelve G_v^a) is %d-dimensional "
      "inside the %d-pattern Cartan cut G_v^3 = 0, smallest nonzero raising-Gram eigenvalue %.4f"
      % (NZ, len(S3), float(evg[evg >= 1e-9].min())),
      NZ == 82 and len(S3) == 544 and abs(float(evg[evg >= 1e-9].min()) - 2.0) < 1e-9)


def pg_block(T):
    return VG.conj().T @ (T[S3][:, S3].toarray()) @ VG


def const_on_components(dvec):
    lo = np.full(NCOMP, np.inf)
    hi = np.full(NCOMP, -np.inf)
    np.minimum.at(lo, LABELS, dvec)
    np.maximum.at(hi, LABELS, dvec)
    return int(np.count_nonzero(hi - lo != 0.0)), float(np.nanmax(hi - lo))


CAS0 = sum((G[(0, a)] @ G[(0, a)] for a in range(3)), ZERO).tocsr()
P0 = IOP.copy()
for c in (0.75, 2.0, 3.75):
    P0 = (P0 @ (CAS0 - c * IOP)) / (0.0 - c)
P0 = P0.tocsr()
idem = float(np.abs((P0 @ P0 - P0).data).max()) if nnz0(P0 @ P0 - P0) else 0.0
nbad_c, spread_c = const_on_components(np.array(CAS0.diagonal()).real)
nbad_p, spread_p = const_on_components(np.array(P0.diagonal()).real)
dc_in_I = in_I_exact(sp.diags(np.array(CAS0.diagonal()).real).tocsr())
dp_in_I = in_I_exact(sp.diags(np.array(P0.diagonal()).real).tocsr())
check("C2 [exact] D(I) is NOT inside R n I: the corner Gauss Casimir C_0 = sum_a (G_0^a)^2 and the "
      "corner singlet projector P_0^{j=0} = prod_{c in {3/4,2,15/4}} (C_0-c)/(0-c) (exactly idempotent, "
      "max|P^2-P| = %.1f) are gauge-invariant, yet D(C_0) and D(P_0) are non-constant on %d and %d of "
      "the %d components, spreads %.1f and %.1f, and neither is in I"
      % (idem, nbad_c, nbad_p, NCOMP, spread_c, spread_p),
      idem == 0.0 and in_I_exact(CAS0) and in_I_exact(P0)
      and nbad_c == 540 and nbad_p == 432
      and abs(spread_c - 2.0) < 1e-12 and abs(spread_p - 0.5) < 1e-12
      and not dc_in_I and not dp_in_I)
check("C3 [exact] so the record map D and the Gauss projector do not commute: Pi(C_0) = C_0 gives "
      "D(Pi(C_0)) not in I, while Pi(D(C_0)) is in I always. There is no canonical 'readable part' of "
      "a gauge-invariant operator: R n I must be taken as the intersection, as in A3",
      (not dc_in_I) and in_I_exact(CAS0))

E1S = sum((EFIELD[(e, 'i', a)] @ EFIELD[(e, 'i', a)] for e in range(NE) for a in range(3)),
          ZERO).tocsr()
good = True
for M in (H_HOP, E1S, Q[0]):
    dv = np.array(M.diagonal()).real
    nb, _ = const_on_components(dv)
    good = good and in_I_exact(M) and nb == 0 and in_I_exact(sp.diags(dv).tocsr())
check("C4 [exact] contrast: for H_hop, sum_e sum_a (E^a_{e,i})^2 and Q_0 -- all gauge-invariant -- "
      "D(M) IS constant on all 1296 components and lands in R n I. C2's failure is a property of the "
      "operator, not of the method", good)

tests = []
for v in range(NV):
    for a in range(3):
        tests.append(RHO[(v, a)])
for e in range(NE):
    for a in range(3):
        tests.append(EFIELD[(e, 'i', a)])
tests.append(sum((RHO[(v, 0)] for v in range(NV)), ZERO).tocsr())
tests.append((RHO[(0, 2)] @ RHO[(0, 2)]
              - (1.0 / 3.0) * sum((RHO[(0, a)] @ RHO[(0, a)] for a in range(3)), ZERO)).tocsr())
tests.append(sp.diags(np.array((EFIELD[(0, 'i', 2)] * 2).diagonal()).real).tocsr())
tests.append((RHO[(0, 2)] * 2).tocsr())
worst = max(float(np.abs(pg_block(T)).max()) for T in tests)
check("C5 [numerical, 1e-12] every rank >= 1 tensor has a zero Gauss-sector block: over %d of them "
      "(twelve rho_v^a, twelve E^a_{e,i}, the global colour charge sum_v rho_v^1, a rank-2 quadrupole, "
      "and the single COLOUR RECORD VALUES 2 E^3_{0,i} and 2 rho_0^3) max |P_G T P_G| = %.3e"
      % (len(tests), worst),
      len(tests) == 28 and worst < 1e-12)

CASM0 = sum((RHO[(0, a)] @ RHO[(0, a)] for a in range(3)), ZERO).tocsr()
ranks = [int(np.linalg.matrix_rank(pg_block(M), tol=1e-9)) for M in (CASM0, Q[0], H_HOP)]
check("C6 [numerical, 1e-9] contrast in the same sector: the singlet operators C^m_0, Q_0 and H_hop "
      "have Gauss-sector blocks of rank %d, %d and %d of %d" % (*ranks, NZ),
      ranks == [26, 68, 42])

hull = S3[np.abs(np.einsum('ij,ij->i', VG, VG.conj())).real > 1e-9]
comps_hull = np.unique(LABELS[hull])
blk_tr, blk_idem = [], 0.0
for c in comps_hull:
    idx = np.isin(S3, np.where(LABELS == c)[0])
    Pc = VG.conj().T @ np.diag(idx.astype(float)) @ VG
    blk_tr.append(float(np.trace(Pc).real))
    blk_idem = max(blk_idem, float(np.abs(Pc @ Pc - Pc).max()))
check("C7 [numerical, 1e-9] on the Gauss sector R n I is a COMPLETE COMMUTING SET: the sector's record "
      "hull is exactly the %d-pattern Cartan cut and meets %d of the 1296 readable classes, each "
      "restricting to an orthogonal projector (max|P^2-P| = %.1e) of dimension exactly 1, summing to "
      "%d. Records resolve every physical state and still cannot see colour"
      % (len(hull), len(comps_hull), blk_idem, int(round(sum(blk_tr)))),
      len(hull) == 544 and len(comps_hull) == 82 and blk_idem < 1e-9
      and all(abs(t - 1.0) < 1e-9 for t in blk_tr) and abs(sum(blk_tr) - 82.0) < 1e-9)

# ============================== D -- colour-rotated open-string states

sel = (d3[0] == 0.5) & (d3[1] == 0.0) & (d3[2] == 0.0) & (d3[3] == 0.0)
SO = np.where(sel)[0]
BO = ARAISE[SO][:, SO].toarray()
BO = 0.5 * (BO + BO.conj().T)
evo, eveco = np.linalg.eigh(BO)
KO = int(np.sum(evo < 1e-9))
check("D1 [numerical, 1e-9] the open-string sector: the coordinate subspace G_0^3 = +1/2, G_v^3 = 0 "
      "(v = 1,2,3) holds %d record patterns and the joint kernel of sum_v (G_v^+)^dag G_v^+ inside it "
      "is %d-dimensional, smallest nonzero Gram eigenvalue %.4f: a singlet at corners 1,2,3 and the "
      "highest weight of a colour DOUBLET at corner 0"
      % (len(SO), KO, float(evo[evo >= 1e-9].min())),
      len(SO) == 424 and KO == 94 and abs(float(evo[evo >= 1e-9].min()) - 2.0) < 1e-9)

psi_p = np.zeros(DIM, dtype=complex)
psi_p[SO] = eveco[:, 0]
psi_p /= np.linalg.norm(psi_p)
psi_m = (G[(0, 0)] - 1j * G[(0, 1)]).tocsr() @ psi_p
psi_m /= np.linalg.norm(psi_m)


def ex(M, x):
    return float(np.vdot(x, M @ x).real)


sing_res = max(float(np.linalg.norm(G[(v, a)] @ psi_p)) for v in (1, 2, 3) for a in range(3))
c0p, c0m = ex(CAS0, psi_p), ex(CAS0, psi_m)
g3p, g3m = ex(G[(0, 2)], psi_p), ex(G[(0, 2)], psi_m)
q0p, q0m = ex(Q[0], psi_p), ex(Q[0], psi_m)
check("D2 [numerical, 1e-12] psi_+ is an exact singlet at corners 1,2,3 (max ||G_v^a psi|| = %.3e); "
      "it and its colour partner psi_- = G_0^- psi_+/||.|| carry <C_0> = %.12f = 3/4 (j = 1/2) and "
      "<G_0^3> = %+.1f / %+.1f, and the abelian charge <Q_0> = %.12f is IDENTICAL on the two"
      % (sing_res, c0p, g3p, g3m, q0p),
      sing_res < 1e-12 and abs(c0p - 0.75) < 1e-12 and abs(c0m - 0.75) < 1e-12
      and abs(g3p - 0.5) < 1e-12 and abs(g3m + 0.5) < 1e-12 and abs(q0p - q0m) < 1e-12)

KAX = [sum((G[(v, ax)] for v in range(NV)), ZERO).tocsr() for ax in range(3)]
theta = 0.7
psi_t = expm_multiply(-1j * theta * KAX[0], psi_p)
psi_t /= np.linalg.norm(psi_t)
c_p = np.vdot(psi_p, psi_t)
c_m = np.vdot(psi_m, psi_t)
resid = float(np.linalg.norm(psi_t - c_p * psi_p - c_m * psi_m))
check("D3 [numerical, 1e-12] the global colour rotation U(theta) = exp(-i theta sum_v G_v^1), by "
      "Krylov exponentiation on the DECLARED angle theta = %.1f and never a dense exponential, keeps "
      "the state in span{psi_+, psi_-} to %.3e with |c_+|^2 = %.12f = cos^2(theta/2) = %.12f: "
      "psi_theta is the colour-rotated state, not a different one"
      % (theta, resid, abs(c_p) ** 2, np.cos(theta / 2) ** 2),
      resid < 1e-12 and abs(abs(c_p) ** 2 - np.cos(theta / 2) ** 2) < 1e-12)

pp, pm, pt = np.abs(psi_p) ** 2, np.abs(psi_m) ** 2, np.abs(psi_t) ** 2
tv_pm = 0.5 * float(np.abs(pp - pm).sum())
tv_pt = 0.5 * float(np.abs(pp - pt).sum())
supp = (int((pp > 1e-14).sum()), int((pm > 1e-14).sum()), int((pt > 1e-14).sum()))
check("D4 [numerical, 1e-12] the RAW record pattern DOES distinguish the colour-rotated states, "
      "maximally: the FINE distributions of psi_+ and psi_- sit on %d and %d patterns at "
      "total-variation distance %.12f (disjoint supports); psi_theta gives %.12f on %d. Every "
      "colour-blindness statement here is about record-readable AND gauge-invariant observables"
      % (supp[0], supp[1], tv_pm, tv_pt, supp[2]),
      supp == (174, 174, 348) and abs(tv_pm - 1.0) < 1e-12 and abs(tv_pt - 0.117578906358) < 1e-9)


def coarse(p):
    return np.bincount(LABELS, weights=p, minlength=NCOMP)


cp, cm, ct = coarse(pp), coarse(pm), coarse(pt)
dev_pm = float(np.abs(cp - cm).max())
dev_pt = float(np.abs(cp - ct).max())
worst_scan = 0.0
for ax in range(3):
    for th in ANGLES[:1] + ANGLES[2:]:
        x = expm_multiply(-1j * th * KAX[ax], psi_p)
        x /= np.linalg.norm(x)
        worst_scan = max(worst_scan, float(np.abs(coarse(np.abs(x) ** 2) - cp).max()))
check("D5 [numerical, 1e-12] no record-readable AND gauge-invariant observable distinguishes them: "
      "over the %d atoms of R n I (%d carry nonzero probability) psi_+ and psi_- differ by at most "
      "%.3e and psi_theta by %.3e, and over the DECLARED scan of 3 axes x 4 angles (%s) the largest "
      "deviation anywhere is %.3e"
      % (NCOMP, int((cp > 1e-14).sum()), dev_pm, dev_pt, "0.3, 1.1, 2.0, pi", worst_scan),
      int((cp > 1e-14).sum()) == 23 and dev_pm < 1e-15 and dev_pt < 1e-15
      and worst_scan < 1e-15)

odd0 = ((qv[0].astype(int) % 2) == 1)
par_p, par_m, par_t = float(pp[odd0].sum()), float(pm[odd0].sum()), float(pt[odd0].sum())
sing = np.zeros(DIM, dtype=complex)
sing[S3] = VG[:, 0]
sing /= np.linalg.norm(sing)
par_s = float((np.abs(sing) ** 2)[odd0].sum())
check("D6 [numerical, 1e-12] what records DO register of an uncompensated colour source is the Z_2 "
      "centre charge: P[(-1)^{Q_0} = -1] = %.12f for psi_+, psi_- and psi_theta alike, against %.12f "
      "for a Gauss-sector (singlet) state" % (par_p, par_s),
      abs(par_p - 1.0) < 1e-12 and abs(par_m - 1.0) < 1e-12 and abs(par_t - 1.0) < 1e-12
      and abs(par_s) < 1e-12)

rf = (2 * ex(RHO[(0, 2)], psi_p), 2 * ex(RHO[(0, 2)], psi_m), 2 * ex(RHO[(0, 2)], psi_t))
check("D7 [numerical, 1e-9] the contrast that fixes the wording: the frame-dependent record "
      "observable 2 <rho_0^3> -- in R, NOT in I -- reports %+.9f / %+.9f / %+.9f on the three states. "
      "It separates them, which is why it is not a physical readout: it registers which colour frame "
      "was declared, and C5 gives it a zero Gauss-sector block" % rf,
      abs(rf[0] + rf[1]) < 1e-9 and abs(rf[0] - 0.793369885) < 1e-8
      and abs(rf[2] - 0.606802758) < 1e-8)

# ============================== E -- the U(1) control, dim I, and the frame

offd_u1 = sum(offdiag_nnz(Q[v]) for v in range(NV))
nq = len(np.unique(np.stack(list(qv), 1), axis=0))
check("E1 [exact] the U(1) control on the SAME carrier and record basis, gauge algebra reduced to the "
      "u(1) summand {Q_v}: %d off-diagonal entries, so R n I = R = %d, ratio 1.000000 against %.6f for "
      "SU(2), a suppression of %.4f. Charge IS readable: every record pattern is an exact joint Q_v "
      "eigenstate, %d distinct joint values. An abelian group stabilises the record basis up to phase; "
      "a non-abelian one mixes patterns, and only mixing-invariant functions survive"
      % (offd_u1, DIM, NCOMP / DIM, DIM / NCOMP, nq),
      offd_u1 == 0 and nq == 431 and abs(DIM / NCOMP - 50.5679) < 1e-3)

poly = {(0, 0, 0, 0): 1}


def mul_term(pol, terms):
    out = {}
    for mono, c in pol.items():
        for add, cc in terms:
            key = tuple(mono[k] + add[k] for k in range(4))
            out[key] = out.get(key, 0) + c * cc
    return out


for v in range(NV):
    ev_ = [0, 0, 0, 0]
    ev_[v] = 1
    poly = mul_term(poly, [((0, 0, 0, 0), 2), (tuple(ev_), 1)])
for (i, j) in LINKS:
    ei = [0, 0, 0, 0]
    ei[i] = 1
    ej = [0, 0, 0, 0]
    ej[j] = 1
    poly = mul_term(poly, [(tuple(ei), 1), (tuple(ej), 1)])


def Mint(p):
    return 0 if p % 2 else comb(p, p // 2) - comb(p, p // 2 + 1)


def cpj(p, twoj):
    if (p - twoj) % 2 or twoj > p:
        return 0
    a = (p - twoj) // 2
    return comb(p, a) - comb(p, a - 1) if a >= 1 else comb(p, 0)


dim_singlet = sum(c * int(np.prod([Mint(m[v]) for v in range(4)])) for m, c in poly.items())
mult = {}
for mono, c in poly.items():
    for tj in product(*[range(0, mono[v] + 1) for v in range(4)]):
        w = 1
        for v in range(4):
            w *= cpj(mono[v], tj[v])
            if w == 0:
                break
        if w:
            mult[tj] = mult.get(tj, 0) + c * w
mult = {k: v for k, v in mult.items() if v}
dimI = sum(v * v for v in mult.values())
tot = sum(v * int(np.prod([t + 1 for t in k])) for k, v in mult.items())
check("E2 [exact] exact-integer SU(2)^4 Haar characters on prod_v (2+chi_v) prod_e (chi_i+chi_j) (%d "
      "monomials): singlet multiplicity %d and open-string multiplicity m_(1/2,0,0,0) = %d, "
      "cross-checking C1 and D1 independently; %d irreps occur, dim I = sum m_lambda^2 = %d, "
      "sum m_lambda dim(lambda) = %d = dim H, and dim(R n I)/dim I = %.8f"
      % (len(poly), int(dim_singlet), mult.get((1, 0, 0, 0), 0), len(mult), int(dimI), int(tot),
         NCOMP / dimI),
      int(dim_singlet) == 82 and mult.get((1, 0, 0, 0), 0) == 94 and len(mult) == 193
      and int(dimI) == 356306 and int(tot) == DIM)

frame_ok = bool(np.all(LABELS[rows] == LABELS[cols]))
check("E3 [exact] R n I is unchanged under a gauge rotation of the colour frame: all %d component "
      "projectors commute with all twelve G_v^a, checked completely at once by LABELS[r] == LABELS[c] "
      "on every one of the %d off-diagonal entries of G_v^{1,2} (G_v^3 diagonal). So R n I sits inside "
      "I pointwise and U_g (R n I) U_g^dag = R n I for every g in the connected group: redeclaring the "
      "colour record frame changes R, not R n I" % (NCOMP, tot_off),
      frame_ok and tot_off == 786432)

g3_in_R = all(offdiag_nnz(G[(v, 2)]) == 0 for v in range(NV))
g3_in_I = any(in_I_exact(G[(v, 2)]) for v in range(NV))
g3_blk = max(float(np.abs(pg_block(G[(v, 2)])).max()) for v in range(NV))
check("E4 [exact] the frame-dependent Cartan readout G_v^3 is in R (0 off-diagonal entries) and NOT "
      "in I, and its Gauss-sector block vanishes identically -- max |P_G G_v^3 P_G| = %.1f, exactly "
      "zero because the sector sits inside the cut G_v^3 = 0. The intersection excludes precisely the "
      "frame-dependent readouts, retiring the frame-artefact worry of the parent note's section 4"
      % g3_blk, g3_in_R and not g3_in_I and g3_blk == 0.0)

print("SUMMARY: R n I is exactly the 1296-dim algebra of functions of the abelian charges Q_v and the "
      "link-end electric Casimirs -- colour-blind, and on the 82-dim Gauss sector a complete commuting "
      "set of 82 rank-one projectors. The raw record pattern separates colour-rotated states at "
      "total-variation distance 1; no record-readable AND gauge-invariant observable separates them "
      "at all (1.4e-16 over 3 axes x 4 angles). For U(1) on the same carrier R n I = R.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
if time.time() - T0 > AUDIT_TIMEOUT_SEC:
    print("WARNING: runtime %.1f s exceeded the declared %d s budget"
          % (time.time() - T0, AUDIT_TIMEOUT_SEC), file=sys.stderr)
sys.exit(0 if FAIL == 0 else 1)
