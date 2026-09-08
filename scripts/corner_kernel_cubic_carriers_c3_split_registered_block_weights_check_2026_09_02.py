#!/usr/bin/env python3
"""Finite corner representation, grading-selected copies and supplied coefficients.
The supplied 8-dimensional corner representation decomposes as 2 A1 + 2 T1.
Hamming eigengrading picks two copies inside a CP1 family of irreducible mixed
carriers; no physical generation or carrier selection follows. The original
20 IDs and twelve-by-two coefficient table are retained. Ratios require a != 0;
phases require b != 0. Symbolic Clifford/circulant and rational character results
are distinguished from original NumPy kernel, overlap and rank diagnostics.
No old Record/central-sector reading or physical weighting is a premise.
R1/R2 additionally test the actual mixed invariant carrier and ratio domains.
"""

from __future__ import annotations

import itertools
import sys
from collections import deque
from fractions import Fraction

import numpy as np
import sympy as sp

AUDIT_TIMEOUT_SEC = 120

# Current publication and interpretation inputs; no parent campaign is imported.
AUDIT_INPUT_PATHS = ['docs/CORNER_KERNEL_CUBIC_CARRIERS_C3_SPLIT_AND_REGISTERED_BLOCK_WEIGHTS_BOUNDED_THEOREM_NOTE_2026-09-02.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']
SOURCE_INPUT_SHA256 = {'docs/CORNER_KERNEL_CUBIC_CARRIERS_C3_SPLIT_AND_REGISTERED_BLOCK_WEIGHTS_BOUNDED_THEOREM_NOTE_2026-09-02.md': 'f862128e96893a2a417a7eab9dedf6686ebd56bf6fe2ad961d15a838295adde5', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def _source_input_guard():
    from pathlib import Path
    import hashlib
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(SOURCE_INPUT_SHA256):
        raise RuntimeError("source input declaration mismatch")
    for relative in AUDIT_INPUT_PATHS:
        path = root / relative
        if not path.is_file():
            raise RuntimeError("missing source input: " + relative)
        if hashlib.sha256(path.read_bytes()).hexdigest() != SOURCE_INPUT_SHA256[relative]:
            raise RuntimeError("source input drift: " + relative)
    print("SOURCE_INPUTS: " + " ".join(p+":"+SOURCE_INPUT_SHA256[p] for p in AUDIT_INPUT_PATHS))

_source_input_guard()


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


# ============================================== KS phases, coarse lattice, cell

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
L4 = 4


def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a); axes 0,1,2 = 1,2,3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def va(a, b):
    return tuple(a[i] + b[i] for i in range(3))


I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]], dtype=complex)
SZ = np.diag([1, -1]).astype(complex)


def kr(*ms):
    o = np.array([[1.0 + 0j]])
    for m in ms:
        o = np.kron(o, m)
    return o


XI = [kr(SX, I2, I2), kr(SZ, SX, I2), kr(SZ, SZ, SX)]
GAM = [kr(SY, I2, I2), kr(SZ, SY, I2), kr(SZ, SZ, SY)]
SIX = GAM + XI
EPS8 = kr(SZ, SZ, SZ)
HW = [bin(s).count("1") for s in range(8)]


def gint(M):
    """Round to the nearest Gaussian-integer matrix."""
    return np.rint(M.real) + 1j * np.rint(M.imag)


def is_gint(M):
    return np.array_equal(M, gint(M))


# ================================================ group A: the two cubic carriers

qs = sp.symbols("q1 q2 q3", real=True)
GS = [sp.Matrix(8, 8, lambda i, j: sp.nsimplify(G[i, j])) for G in GAM]
XS = [sp.Matrix(8, 8, lambda i, j: sp.nsimplify(X[i, j])) for X in XI]
HSYM = sp.zeros(8, 8)
for a in range(3):
    HSYM += (1 + sp.cos(qs[a])) * XS[a] + sp.sin(qs[a]) * GS[a]


def bloch_numeric(q):
    """8x8 Bloch block built from the KS hopping rules, no closed form used."""
    H = np.zeros((8, 8), dtype=complex)
    for s in range(8):
        sv = [(s >> (2 - a)) & 1 for a in range(3)]
        for a in range(3):
            e = eta_ks(sv, a)
            bit = 1 << (2 - a)
            if sv[a] == 0:
                t = s | bit
                H[t, s] += e
                H[s, t] += e
            else:
                t = s & ~bit
                H[t, s] += e * np.exp(-1j * q[a])
                H[s, t] += e * np.exp(1j * q[a])
    return H


HSYM_RULES = sp.zeros(8, 8)
for s in range(8):
    sv = [(s >> (2 - a)) & 1 for a in range(3)]
    for a in range(3):
        e = eta_ks(sv, a)
        bit = 1 << (2 - a)
        if sv[a] == 0:
            t = s | bit
            HSYM_RULES[t, s] += e
            HSYM_RULES[s, t] += e
        else:
            t = s & ~bit
            HSYM_RULES[t, s] += e * sp.exp(-sp.I * qs[a])
            HSYM_RULES[s, t] += e * sp.exp(sp.I * qs[a])

cl6 = all(np.array_equal(A @ A, np.eye(8, dtype=complex)) for A in SIX) and all(
    np.array_equal(A @ B + B @ A, np.zeros((8, 8), dtype=complex))
    for i, A in enumerate(SIX)
    for B in SIX[i + 1:]
)
herm = all(np.array_equal(A, A.conj().T) for A in SIX)
DIFF = sp.Matrix(8, 8, lambda i, j: sp.simplify(sp.expand(
    (HSYM_RULES[i, j] - HSYM[i, j]).rewrite(sp.cos))))
form_ok = DIFF.is_zero_matrix
HSQ = sp.expand_trig(sp.simplify(sp.expand(HSYM * HSYM)))
sq_ok = sp.simplify(HSQ - (6 + 2 * sum(sp.cos(qs[a]) for a in range(3))) * sp.eye(8)).is_zero_matrix
corner_zero = sp.simplify(HSYM.subs({qs[a]: sp.pi for a in range(3)})).is_zero_matrix
check(
    "A1 [exact, sympy] Gamma = (Y1, Z1Y2, Z1Z2Y3), Xi = (X1, Z1X2, Z1Z2X3) are six anticommuting hermitian involutions, "
    "the 2x2x2-cell Bloch block of the KS hopping is sum_a [(1+cos q_a) Xi_a + sin q_a Gamma_a] identically in q, "
    "H(q)^2 = (6 + 2 sum_a cos q_a) I, and H(pi,pi,pi) = 0: the whole eight-dimensional cell is the corner kernel",
    cl6 and herm and form_ok and sq_ok and corner_zero,
)

S4 = [v for v in itertools.product(range(L4), repeat=3)]
IDX4 = {v: i for i, v in enumerate(S4)}
N4 = len(S4)
H4 = np.zeros((N4, N4))
for v in S4:
    for a in range(3):
        w = tuple((v[i] + EX[a][i]) % L4 for i in range(3))
        H4[IDX4[w], IDX4[v]] += eta_ks(v, a)
        H4[IDX4[v], IDX4[w]] += eta_ks(v, a)

ROTS = []
for perm in itertools.permutations(range(3)):
    for sg in itertools.product((1, -1), repeat=3):
        M = np.zeros((3, 3), dtype=int)
        for i in range(3):
            M[i, perm[i]] = sg[i]
        if round(np.linalg.det(M)) == 1:
            ROTS.append(M)
RKEY = {tuple(M.flatten()): i for i, M in enumerate(ROTS)}


def rot_act(M, v):
    return tuple(int(sum(M[i, j] * v[j] for j in range(3))) % L4 for i in range(3))


def class_of(M):
    tr = int(round(np.trace(M)))
    if tr == 3:
        return "E"
    if tr == 0:
        return "8C3"
    if tr == 1:
        return "6C4"
    return "3C2" if np.count_nonzero(M - np.diag(np.diag(M))) == 0 else "6C2p"


def gauge_to(target):
    g = {(0, 0, 0): 1}
    dq = deque([(0, 0, 0)])
    while dq:
        v = dq.popleft()
        for a in range(3):
            for sgn in (1, -1):
                w = list(v)
                w[a] += sgn
                w = tuple(x % L4 for x in w)
                src = v if sgn == 1 else w
                r = target(src, a) * eta_ks(src, a)
                if w in g:
                    if g[w] != g[v] * r:
                        return None
                else:
                    g[w] = g[v] * r
                    dq.append(w)
    return g


CS = []
lift_ok = True
for M in ROTS:
    def tgt(v, a, M=M):
        w = tuple((v[i] + EX[a][i]) % L4 for i in range(3))
        return H4[IDX4[rot_act(M, v)], IDX4[rot_act(M, w)]]

    g = gauge_to(tgt)
    if g is None:
        lift_ok = False
        continue
    C = np.zeros((N4, N4))
    for v in S4:
        C[IDX4[rot_act(M, v)], IDX4[v]] = g[v]
    CS.append(C)

KINT = np.zeros((N4, 8), dtype=int)
for s in range(8):
    sv = [(s >> (2 - a)) & 1 for a in range(3)]
    for R in itertools.product(range(2), repeat=3):
        KINT[IDX4[tuple(2 * R[a] + sv[a] for a in range(3))], s] = (-1) ** sum(R)
CSI = [np.rint(C).astype(int) for C in CS]
GRAM = KINT.T @ KINT
RAW = [KINT.T @ C @ KINT for C in CSI]
MS = [R // 8 for R in RAW]
exact_lift = (
    np.array_equal(GRAM, 8 * np.eye(8, dtype=int))
    and all(np.array_equal(M * 8, R) for M, R in zip(MS, RAW))
    and np.array_equal(np.rint(H4).astype(int) @ KINT, np.zeros((N4, 8), dtype=int))
)
KER = KINT / np.sqrt(8.0)
bad = sum(
    0 if np.array_equal(MS[i] @ MS[j], MS[RKEY[tuple((ROTS[i] @ ROTS[j]).flatten())]]) else 1
    for i in range(24)
    for j in range(24)
)
check(
    "A2 [integer representation; numerical kernel/overlap cross-check] the L=4 site-coordinate torus (2 cells per axis) has an 8-dimensional kernel spanned by the corner basis; all 24 proper cubic "
    "rotations lift to signed permutations with C_R H C_R^T = H, and all 576 products close on the nose as integer "
    "matrices on the corner kernel (%d failures) -- a genuine representation of O, not projective" % bad,
    lift_ok
    and len(CS) == 24
    and all(np.allclose(C @ H4 @ C.T, H4) for C in CS)
    and int(np.sum(np.abs(np.linalg.eigvalsh(H4)) < 1e-9)) == 8
    and exact_lift
    and bad == 0
    and all(set(np.unique(m)).issubset({-1, 0, 1}) and (abs(m).sum(0) == 1).all() for m in MS),
)

TAB = {
    "A1": [1, 1, 1, 1, 1],
    "A2": [1, 1, 1, -1, -1],
    "E": [2, -1, 2, 0, 0],
    "T1": [3, 0, -1, 1, -1],
    "T2": [3, 0, -1, -1, 1],
}
ORDER = ["E", "8C3", "3C2", "6C4", "6C2p"]
CIX = {c: i for i, c in enumerate(ORDER)}
SIZE = [1, 8, 3, 6, 6]
tab_ok = all(
    Fraction(sum(SIZE[i] * TAB[x][i] * TAB[y][i] for i in range(5)), 24) == (1 if x == y else 0)
    for x in TAB
    for y in TAB
)
CHI = [0] * 5
for i, M in enumerate(ROTS):
    CHI[CIX[class_of(M)]] = int(np.trace(MS[i]))
DEC = {k: Fraction(sum(SIZE[i] * TAB[k][i] * CHI[i] for i in range(5)), 24) for k in TAB}
check(
    "A3 [exact] characters on the corner kernel (E, 8C3, 3C2, 6C4, 6C2') = (%d, %d, %d, %d, %d) decompose in exact "
    "rational arithmetic, against a self-checked orthonormal character table of O, as 2 A1 + 2 T1" % tuple(CHI),
    tab_ok and DEC == {"A1": 2, "A2": 0, "E": 0, "T1": 2, "T2": 0},
)


def isoproj(irr):
    d = TAB[irr][0]
    A = sum(TAB[irr][CIX[class_of(ROTS[i])]] * MS[i] for i in range(24))
    return np.array([[Fraction(int(A[i, j]) * d, 24) for j in range(8)] for i in range(8)], dtype=object)


PI = {k: isoproj(k) for k in TAB}
PHW = {
    w: np.array(
        [[Fraction(1 if (i == j and HW[i] == w) else 0) for j in range(8)] for i in range(8)],
        dtype=object,
    )
    for w in range(4)
}
diagA1 = np.array(
    [[Fraction(1 if (i == j and HW[i] in (0, 3)) else 0) for j in range(8)] for i in range(8)],
    dtype=object,
)
diagT1 = np.array(
    [[Fraction(1 if (i == j and HW[i] in (1, 2)) else 0) for j in range(8)] for i in range(8)],
    dtype=object,
)
check(
    "A4 [exact] the isotypic projectors from the character formula in exact rational arithmetic are exactly "
    "P_A1 = diag(1,0,0,0,0,0,0,1) = P_hw0 + P_hw3 and P_T1 = diag(0,1,1,1,1,1,1,0) = P_hw1 + P_hw2, with "
    "P_A2 = P_E = P_T2 = 0: the two grading-selected Hamming triplets are copies within the multiplicity-two T1 isotypic",
    np.array_equal(PI["A1"], diagA1)
    and np.array_equal(PI["A1"], PHW[0] + PHW[3])
    and np.array_equal(PI["T1"], diagT1)
    and np.array_equal(PI["T1"], PHW[1] + PHW[2])
    and all(not PI[k].any() for k in ("A2", "E", "T2")),
)

blk_ok = True
blk_chi = {}
for w in range(4):
    Pw = np.array([[1.0 if (i == j and HW[i] == w) else 0.0 for j in range(8)] for i in range(8)])
    inv = all(np.array_equal(MS[i] @ Pw, Pw @ MS[i]) for i in range(24))
    ch = [0] * 5
    for i, M in enumerate(ROTS):
        ch[CIX[class_of(M)]] = int(round(float(np.trace(MS[i] @ Pw))))
    dec = {k: Fraction(sum(SIZE[i] * TAB[k][i] * ch[i] for i in range(5)), 24) for k in TAB}
    blk_chi[w] = tuple(ch)
    want = {"A1": 1} if w in (0, 3) else {"T1": 1}
    blk_ok = blk_ok and inv and {k: v for k, v in dec.items() if v} == want
check(
    "A5 [exact] each Hamming block is separately O-invariant: characters %s on hw = 0 and 3 (one A1 each) and %s on "
    "hw = 1 and 2 (one T1 each)" % (str(blk_chi[0]).replace(" ", ""), str(blk_chi[1]).replace(" ", "")),
    blk_ok and blk_chi[0] == blk_chi[3] == (1, 1, 1, 1, 1) and blk_chi[1] == blk_chi[2] == (3, 0, -1, 1, -1),
)

# ============================================ group B: grading, multiplicity, T

ZS = gint(1j * sum(GAM[a] @ XI[a] for a in range(3)))
TOP = gint(1j * GAM[0] @ GAM[1] @ GAM[2])
zs_ok = (
    is_gint(1j * sum(GAM[a] @ XI[a] for a in range(3)))
    and np.array_equal(ZS, kr(SZ, I2, I2) + kr(I2, SZ, I2) + kr(I2, I2, SZ))
    and np.array_equal(ZS, np.diag([3 - 2 * HW[s] for s in range(8)]).astype(complex))
    and all(np.array_equal(MS[i] @ ZS, ZS @ MS[i]) for i in range(24))
)
check(
    "B1 [exact] i sum_a Gamma_a Xi_a = Z_1 + Z_2 + Z_3 exactly, it is O-invariant, and its corner spectrum is 3 - 2 hw: "
    "the landed 1 + 3 + 3 + 1 grading is the eigen-grading of that one O-invariant Cl(6) bilinear",
    zs_ok,
)

comm_all = Fraction(sum(SIZE[i] * CHI[i] * CHI[i] for i in range(5)), 24)
chi_t1iso = [2 * TAB["T1"][i] for i in range(5)]
comm_t1 = Fraction(sum(SIZE[i] * chi_t1iso[i] * chi_t1iso[i] for i in range(5)), 24)
P1F = np.array([[1.0 if (i == j and HW[i] == 1) else 0.0 for j in range(8)] for i in range(8)])
P2F = np.array([[1.0 if (i == j and HW[i] == 2) else 0.0 for j in range(8)] for i in range(8)])
CMT = [P1F.astype(complex), P2F.astype(complex), P2F @ TOP @ P1F, P1F @ TOP @ P2F]
cmt_ok = all(np.array_equal(MS[i] @ Xm, Xm @ MS[i]) for Xm in CMT for i in range(24)) and (
    np.linalg.matrix_rank(np.array([Xm.ravel() for Xm in CMT])) == 4
)
check(
    "B2 [exact character dimensions; numerical exhibited rank] the T1 isotypic component is T1 (x) C^2: the commutant of the 24 lifts has dimension %s on the corner "
    "kernel and %s on the T1 isotypic by the exact rational formula (1/24) sum |chi|^2, and four independent commuting "
    "elements P_hw1, P_hw2, P_hw2 T P_hw1, P_hw1 T P_hw2 are exhibited -- the group alone does not split it"
    % (comm_all, comm_t1),
    comm_all == 8 and comm_t1 == 4 and cmt_ok,
)

t_ok = (
    is_gint(1j * GAM[0] @ GAM[1] @ GAM[2])
    and np.array_equal(TOP @ TOP.conj().T, np.eye(8, dtype=complex))
    and all(np.array_equal(MS[i] @ TOP, TOP @ MS[i]) for i in range(24))
    and np.array_equal(P1F @ TOP @ P1F, np.zeros((8, 8), dtype=complex))
    and np.array_equal(P2F @ TOP @ P2F, np.zeros((8, 8), dtype=complex))
    and np.linalg.matrix_rank(P2F @ TOP @ P1F) == 3
    and np.linalg.matrix_rank(P1F @ TOP @ P2F) == 3
    and np.array_equal(EPS8, np.diag([(-1) ** HW[s] for s in range(8)]).astype(complex))
    and np.array_equal(TOP @ EPS8 + EPS8 @ TOP, np.zeros((8, 8), dtype=complex))
    and not np.array_equal(TOP, EPS8)
)
check(
    "B3 [exact identities; numerical off-diagonal rank] T = i Gamma_1 Gamma_2 Gamma_3 is O-invariant and unitary, carries hw=1 onto hw=2 and back with rank 3, "
    "and anticommutes with epsilon = Z_1 Z_2 Z_3 = diag((-1)^hw), T != epsilon: the two T1 copies are O-equivariantly "
    "isomorphic and are distinguished by epsilon within the supplied Hamming pair",
    t_ok,
)

# ================================================== group C: the C3[111] split

IC = [i for i, M in enumerate(ROTS) if np.array_equal(M, np.array([[0, 1, 0], [0, 0, 1], [1, 0, 0]]))][0]
C8 = MS[IC]
BAS = {1: [4, 2, 1], 2: [3, 5, 6]}


def rst(O, idx):
    return sp.Matrix(3, 3, lambda i, j: sp.nsimplify(sp.Rational(int(round(O[idx[i], idx[j]].real)))
                                                     + sp.I * sp.Rational(int(round(O[idx[i], idx[j]].imag)))))


def rsti(O, idx):
    return sp.Matrix(3, 3, lambda i, j: sp.Integer(int(O[idx[i], idx[j]])))


UC = {w: rsti(C8, BAS[w]) for w in (1, 2)}
c1_ok = True
for w in (1, 2):
    U = UC[w]
    c1_ok = c1_ok and sp.trace(U) == 0 and (U ** 3 == sp.eye(3)) and set(
        sp.nsimplify(sp.expand(k)) for k in U.eigenvals()
    ) == set(sp.nsimplify(sp.exp(2 * sp.pi * sp.I * k / 3)) for k in range(3))
check(
    "C1 [exact] the C3[111] restriction U = C|_T1 on each triplet has tr U = 0 and U^3 = I, with eigenvalues "
    "{1, omega, omegabar}: each triplet is the regular representation of Z/3",
    c1_ok,
)

SING = {}
c2_ok = True
overlaps = {}
for w in (1, 2):
    U = UC[w]
    ns = (U - sp.eye(3)).nullspace()
    v = sp.simplify(ns[0] / max(abs(sp.Rational(x)) for x in ns[0]))
    v = v / sp.sqrt((v.T * v)[0, 0])
    SING[w] = v
    wt = [sp.simplify(sp.Abs(v[i]) ** 2) for i in range(3)]
    c2_ok = c2_ok and len(ns) == 1 and all(x == sp.Rational(1, 3) for x in wt)
    W = sp.Matrix([1, 1, 1]) / sp.sqrt(3)
    overlaps[w] = sp.simplify(sp.Abs((W.T * v)[0, 0]) ** 2)
sigma = sp.diag(*[sp.sign(SING[2][i]) for i in range(3)])
regauged = sp.simplify(sigma * UC[2] * sigma)
plain3 = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
c2_ok = (
    c2_ok
    and overlaps[1] == 1
    and overlaps[2] == sp.Rational(1, 9)
    and regauged == plain3
    and sp.simplify(sigma * SING[2]) == sp.Matrix([1, 1, 1]) / sp.sqrt(3)
)
check(
    "C2 [exact] the C-invariant vector of each triplet has corner weights exactly (1/3, 1/3, 1/3) -- gauge-invariant "
    "trimaximality; against the fixed democratic W = (1,1,1)/sqrt3 the overlaps are |<W|v>|^2 = %s and %s, a "
    "corner-sign gauge artefact removed by rephasing a single corner, which carries U to the plain 3-cycle and v to W"
    % (overlaps[1], overlaps[2]),
    c2_ok,
)

P0 = {}
c3_ok = True
for w in (1, 2):
    v = SING[w]
    P0[w] = sp.simplify(v * v.T)
    P1m = sp.eye(3) - P0[w]
    c3_ok = c3_ok and sp.simplify(P0[w] * P0[w] - P0[w]).is_zero_matrix
    c3_ok = c3_ok and sp.simplify(P0[w] * UC[w] - UC[w] * P0[w]).is_zero_matrix
    c3_ok = c3_ok and sp.simplify(P1m * UC[w] - UC[w] * P1m).is_zero_matrix
    c3_ok = c3_ok and all(sp.Abs(P0[w][i, j]) == sp.Rational(1, 3) for i in range(3) for j in range(3))
check(
    "C3 [exact] the C3 singlet projectors P_0 = |v><v| have every entry of modulus 1/3 (P_0 = J/3 in the gauge that "
    "carries v to W), are idempotent, and P_0 and P_1 = I - P_0 both commute with U",
    c3_ok,
)

# ============================================= group D: circulant restrictions

SG = gint(sum(GAM))
SXi = gint(sum(XI))
SG2 = gint(SG @ SG)
SX2 = gint(SXi @ SXi)
BG = gint(1j * sum(GAM[a] @ GAM[(a + 1) % 3] for a in range(3)))
BX = gint(1j * sum(XI[a] @ XI[(a + 1) % 3] for a in range(3)))
MG1 = gint(1j * sum(GAM[a] @ XI[(a + 1) % 3] for a in range(3)))
MG2 = gint(1j * sum(GAM[a] @ XI[(a + 2) % 3] for a in range(3)))

ps = sp.symbols("p1 p2 p3", real=True)
HSHIFT = HSYM.subs({qs[a]: sp.pi + ps[a] for a in range(3)}, simultaneous=True)
HSQ2 = sp.expand_trig(sp.expand(HSHIFT * HSHIFT))
LAPS = [
    sp.simplify(sp.diff(HSQ2, ps[a], 2).subs({ps[b]: 0 for b in range(3)}) / 2)
    for a in range(3)
]
lap_ok = all(Lm == sp.eye(8) for Lm in LAPS)
LAP = np.eye(8, dtype=complex)

OPS = [
    ("sum_a Gamma_a", SG),
    ("sum_a Xi_a", SXi),
    ("i sum_a Gamma_a Xi_a = Z_1+Z_2+Z_3", ZS),
    ("(sum_a Gamma_a)^2", SG2),
    ("(sum_a Xi_a)^2", SX2),
    ("T = i Gamma_1 Gamma_2 Gamma_3", TOP),
    ("epsilon = Z_1 Z_2 Z_3", EPS8),
    ("i(G_xG_y + G_yG_z + G_zG_x)", BG),
    ("i(X_xX_y + X_yX_z + X_zX_x)", BX),
    ("p_a^2 coeff of H(pi+p)^2", LAP),
    ("i sum_a Gamma_a Xi_{a+1}", MG1),
    ("i sum_a Gamma_a Xi_{a+2}", MG2),
]


def circ(M3, U):
    """Exact circulant decomposition M3 = a I + b U + c U^2 with U^3 = I, tr U = 0."""
    U2 = U * U
    a = sp.nsimplify(sp.trace(M3) / 3)
    b = sp.nsimplify(sp.trace(M3 * U2) / 3)
    c = sp.nsimplify(sp.trace(M3 * U) / 3)
    R = sp.expand(M3 - (a * sp.eye(3) + b * U + c * U2))
    return a, b, c, R


def rst_c(O, idx):
    return sp.Matrix(
        3, 3,
        lambda i, j: sp.Integer(int(round(O[idx[i], idx[j]].real)))
        + sp.I * sp.Integer(int(round(O[idx[i], idx[j]].imag))),
    )


TABLE = {}
PHASES = {}
d1_ok = (
    all(is_gint(O) for _, O in OPS)
    and all(np.array_equal(O, O.conj().T) for _, O in OPS)
    and lap_ok
)
print("  operator restrictions on each cubic carrier (a, |b|, delta/pi, r = |b|^2/a^2; exact):")
print("    %-38s %-3s %-6s %-6s %-9s %-8s %s" % ("operator", "hw", "a", "|b|", "delta/pi", "r", "dev"))
for nm, O in OPS:
    for w in (1, 2):
        M3 = rst_c(O, BAS[w])
        a, b, c, R = circ(M3, UC[w])
        ab = sp.simplify(sp.Abs(b))
        r = sp.nsimplify(ab ** 2 / a ** 2) if a != 0 else None
        TABLE[(nm, w)] = (a, b, c, ab, r, R)
        d1_ok = d1_ok and R.is_zero_matrix and sp.simplify(c - sp.conjugate(b)) == 0
        PHASES[(nm, w)] = None if b == 0 else sp.arg(b)
        dl = "--" if PHASES[(nm, w)] is None else "%+.3f" % float(PHASES[(nm, w)] / sp.pi)
        print(
            "    %-38s %-3d %-6s %-6s %-9s %-8s %s"
            % (nm[:38], w, a, ab, dl, "--" if r is None else r, 0 if R.is_zero_matrix else "NONZERO")
        )
EXPECT = {
    ("sum_a Gamma_a", 1): (0, 0), ("sum_a Gamma_a", 2): (0, 0),
    ("sum_a Xi_a", 1): (0, 0), ("sum_a Xi_a", 2): (0, 0),
    ("i sum_a Gamma_a Xi_a = Z_1+Z_2+Z_3", 1): (1, 0),
    ("i sum_a Gamma_a Xi_a = Z_1+Z_2+Z_3", 2): (-1, 0),
    ("(sum_a Gamma_a)^2", 1): (3, 0), ("(sum_a Gamma_a)^2", 2): (3, 0),
    ("(sum_a Xi_a)^2", 1): (3, 0), ("(sum_a Xi_a)^2", 2): (3, 0),
    ("T = i Gamma_1 Gamma_2 Gamma_3", 1): (0, 0), ("T = i Gamma_1 Gamma_2 Gamma_3", 2): (0, 0),
    ("epsilon = Z_1 Z_2 Z_3", 1): (-1, 0), ("epsilon = Z_1 Z_2 Z_3", 2): (1, 0),
    ("i(G_xG_y + G_yG_z + G_zG_x)", 1): (0, sp.I), ("i(G_xG_y + G_yG_z + G_zG_x)", 2): (0, sp.I),
    ("i(X_xX_y + X_yX_z + X_zX_x)", 1): (0, sp.I), ("i(X_xX_y + X_yX_z + X_zX_x)", 2): (0, sp.I),
    ("p_a^2 coeff of H(pi+p)^2", 1): (1, 0), ("p_a^2 coeff of H(pi+p)^2", 2): (1, 0),
    ("i sum_a Gamma_a Xi_{a+1}", 1): (0, -1), ("i sum_a Gamma_a Xi_{a+1}", 2): (0, 1),
    ("i sum_a Gamma_a Xi_{a+2}", 1): (0, -1), ("i sum_a Gamma_a Xi_{a+2}", 2): (0, 1),
}
d1_ok = d1_ok and all(
    TABLE[k][0] == EXPECT[k][0] and sp.simplify(TABLE[k][1] - EXPECT[k][1]) == 0 for k in EXPECT
)
zero_rest = all(
    rst_c(dict(OPS)[nm], BAS[w]).is_zero_matrix
    for nm in ("sum_a Gamma_a", "sum_a Xi_a", "T = i Gamma_1 Gamma_2 Gamma_3")
    for w in (1, 2)
)
check(
    "D1 [exact] every one of the twelve stipulated bilinears restricts to an exactly circulant operator on each "
    "carrier (residual 0, c = conj(b) throughout), with the tabulated (a, |b|, delta, r); the restrictions of "
    "sum Gamma_a, sum Xi_a and T are identically zero, and the p_a^2 coefficient of H(pi+p)^2 is the identity on both "
    "carriers -- the naive dispersion is hw-blind",
    d1_ok and zero_rest,
)

OINV = {}
CINV = {}
for nm, O in OPS:
    OINV[nm] = all(np.array_equal(MS[i] @ O, O @ MS[i]) for i in range(24))
    CINV[nm] = np.array_equal(C8 @ O, O @ C8)
mixed = [
    nm for nm, _ in OPS for w in (1, 2)
    if TABLE[(nm, w)][0] != 0 and TABLE[(nm, w)][1] != 0
]
schur_ok = all(TABLE[(nm, w)][1] == 0 for nm, _ in OPS if OINV[nm] for w in (1, 2))
avg_ok = True
for nm, O in OPS:
    SUMAVG = gint(sum(MS[i] @ O @ MS[i].T for i in range(24)))
    if OINV[nm]:
        avg_ok = avg_ok and np.array_equal(SUMAVG, 24 * O)
    else:
        avg_ok = avg_ok and np.array_equal(SUMAVG, np.zeros((8, 8), dtype=complex))
trace_ok = all(TABLE[(nm, w)][0] == 0 for nm, _ in OPS if CINV[nm] and not OINV[nm] for w in (1, 2))
allc3 = all(CINV[nm] for nm, _ in OPS)
r0 = [nm for nm, _ in OPS if TABLE[(nm, 1)][0] != 0]
check(
    "D2 [exact] all twelve commute with C3[111]; the %d that commute with all 24 lifts have b = 0 on both carriers "
    "(Schur on an irreducible T1), and the O-average of each of the other %d is exactly 0, so their a -- which depends "
    "on the O-average alone, the Hamming projectors being O-invariant -- vanishes; no listed operator has a != 0 and "
    "b != 0, hence each nonzero scalar restriction has r = 0; r is undefined at a = 0"
    % (sum(1 for nm, _ in OPS if OINV[nm]), sum(1 for nm, _ in OPS if CINV[nm] and not OINV[nm])),
    allc3 and schur_ok and avg_ok and trace_ok and not mixed
    and all(TABLE[(nm, w)][4] == 0 for nm in r0 for w in (1, 2)),
)

BASIS3 = [("sum Z_a", ZS), ("i sum_cyc Gamma_a Gamma_{a+1}", BG), ("i sum_a Gamma_a Xi_{a+1}", MG1)]
d3_ok = True
for w in (1, 2):
    rows = []
    for nm, O in BASIS3:
        a, b, c, R = circ(rst_c(O, BAS[w]), UC[w])
        rows.append([sp.re(a), sp.re(b), sp.im(b)])
    d3_ok = d3_ok and sp.Matrix(rows).rank() == 3
check(
    "D3 [exact] surjectivity: on each carrier the three real C3-invariant Hermitian quadratics "
    "alpha (sum Z_a) + beta i(sum_cyc Gamma_a Gamma_{a+1}) + gamma i(sum_a Gamma_a Xi_{a+1}) map onto (a, Re b, Im b) "
    "with real rank 3, so every (a, Re b, Im b), with delta only for b != 0 and r only for a != 0 -- hence every r in [0, inf) -- is realised by stipulated coefficients",
    d3_ok,
)

d4_ok = True
reg = []
for (al, be, ga), want in (((2, 1, 1), sp.Rational(1, 2)), ((2, 1, 0), sp.Rational(1, 4))):
    for w in (1, 2):
        O = gint(al * ZS + be * BG + ga * MG1)
        a, b, c, R = circ(rst_c(O, BAS[w]), UC[w])
        rr = sp.nsimplify(sp.Abs(b) ** 2 / a ** 2)
        d4_ok = d4_ok and R.is_zero_matrix and rr == want
    reg.append(((al, be, ga), want))
check(
    "D4 [exact] registered examples, stipulated and not derived: the coefficient triple (alpha, beta, gamma) = %s "
    "registers r = %s and %s registers r = %s, exactly and on both carriers -- r is a free function of stipulated "
    "coefficients, matched not delivered" % (reg[0][0], reg[0][1], reg[1][0], reg[1][1]),
    d4_ok,
)

# ================================================== group E: invariance census

e1_ok = True
for nm, O in OPS:
    for w in (1, 2):
        aR, bR, _, abR, _, _ = TABLE[(nm, w)]
        for perm in itertools.permutations(range(3)):
            idx = [BAS[w][k] for k in perm]
            Up = rsti(C8, idx)
            a, b, c, R = circ(rst_c(O, idx), Up)
            e1_ok = e1_ok and R.is_zero_matrix and a == aR and sp.simplify(sp.Abs(b) - abR) == 0
            if aR != 0:
                e1_ok = e1_ok and sp.nsimplify(sp.Abs(b) ** 2 / a ** 2) == sp.nsimplify(abR ** 2 / aR ** 2)
check(
    "E1 [exact] all 6 relabellings of each carrier's basis leave (a, |b|, r where defined) unchanged with circulant residual 0, for "
    "every one of the twelve operators: no quantity reported here depends on which member of a triplet is written first",
    e1_ok,
)

e2_ok = True
for nm, O in OPS:
    for w in (1, 2):
        aR, bR, _, abR, _, _ = TABLE[(nm, w)]
        for i in range(24):
            g = MS[i]
            gi = g.T
            Og = gint(g @ O @ gi)
            Cg = g @ C8 @ gi
            a, b, c, R = circ(rst_c(Og, BAS[w]), rsti(Cg, BAS[w]))
            e2_ok = e2_ok and R.is_zero_matrix and a == aR and sp.simplify(sp.Abs(b) - abR) == 0
check(
    "E2 [exact] all 24 cubic conjugations (O -> g O g^-1 with C -> g C g^-1, covering all eight C3 elements) leave "
    "(a, |b|, r where defined) unchanged with circulant residual 0, for every one of the twelve operators",
    e2_ok,
)

e3_ok = True
flip = []
for nm, O in OPS:
    for w in (1, 2):
        aR, bR, _, abR, _, _ = TABLE[(nm, w)]
        a, b, c, R = circ(rst_c(O, BAS[w]), UC[w] * UC[w])
        e3_ok = e3_ok and R.is_zero_matrix and a == aR and sp.simplify(b - sp.conjugate(bR)) == 0
        if bR != 0 and sp.simplify(b - bR) != 0:
            flip.append(nm)
check(
    "E3 [exact] naming C^2 rather than C the generator sends b -> conj(b), i.e. delta -> -delta when b != 0, and leaves "
    "(a, |b|, r where defined) fixed on both carriers: the orientation of the cyclic order is a supplied datum, not a computed one",
    e3_ok and flip,
)

# ==================================================== group F: the carrier locus

sep_a = [nm for nm, _ in OPS if TABLE[(nm, 1)][0] != TABLE[(nm, 2)][0]]
sep_b = [
    nm for nm, _ in OPS
    if sp.simplify(TABLE[(nm, 1)][1] - TABLE[(nm, 2)][1]) != 0
    and sp.simplify(TABLE[(nm, 1)][3] - TABLE[(nm, 2)][3]) == 0
]
same = [nm for nm, _ in OPS if nm not in sep_a and nm not in sep_b]
delta_pi = all(
    sp.simplify(sp.Abs(sp.arg(TABLE[(nm, 1)][1]) - sp.arg(TABLE[(nm, 2)][1])) - sp.pi) == 0 for nm in sep_b
)
check(
    "F1 [exact] exactly %d of the twelve separate the two carriers: sum Z_a and epsilon, by the sign of a -- the "
    "chirality grading's own sign convention -- and the two Gamma-Xi cross terms, with equal |b| and delta differing "
    "by exactly pi; the remaining %d restrict identically to both" % (len(sep_a) + len(sep_b), len(same)),
    set(sep_a) == {"i sum_a Gamma_a Xi_a = Z_1+Z_2+Z_3", "epsilon = Z_1 Z_2 Z_3"}
    and set(sep_b) == {"i sum_a Gamma_a Xi_{a+1}", "i sum_a Gamma_a Xi_{a+2}"}
    and delta_pi
    and len(same) == 8,
)

lopsided = [
    nm for nm, _ in OPS
    if CINV[nm] and ((TABLE[(nm, 1)][1] != 0) != (TABLE[(nm, 2)][1] != 0))
]
check(
    "F2 [exact] no listed operator is C3-invariant with b != 0 on exactly one carrier: the off-diagonal part is either "
    "absent on both or present on both, so nothing in this list singles out one triplet as the one carrying a weight",
    not lopsided,
)


# Exact finite countercontrols on the actual matrices, not a supplied verdict.
MIX_P = sp.diag(*[int(x == 1) for x in HW])
MIX_Q = sp.diag(*[int(x == 2) for x in HW])
MIX_T = sp.Matrix(TOP.tolist()).applyfunc(sp.nsimplify)
MIX_C = MIX_Q * MIX_T * MIX_P
MIX_R = (9*MIX_P + 16*MIX_Q + 12*(MIX_C + MIX_C.conjugate().T))/25
MIX_MS = [sp.Matrix(m.tolist()).applyfunc(sp.nsimplify) for m in MS]
MIX_CH = [sp.trace(MIX_R*m) for m in MIX_MS]
check("R1 [exact mixed carrier] actual rank3 rational projector commutes with all24 lifts, is irreducible and distinct from the Hamming pair",
      MIX_R*MIX_R == MIX_R and MIX_R.rank() == 3
      and all(MIX_R*m == m*MIX_R for m in MIX_MS)
      and sum(v*sp.conjugate(v) for v in MIX_CH)/24 == 1
      and MIX_R != MIX_P and MIX_R != MIX_Q
      and MIX_R*sp.Matrix(EPS8) != sp.Matrix(EPS8)*MIX_R)
DOMAIN_OK = all((row[4] is None) == (row[0] == 0)
                and (PHASES[key] is None) == (row[1] == 0) for key, row in TABLE.items())
check("R2 [exact domains] all24 actual table rows retain undefined r at a=0 and undefined phase at b=0, including zero/scalar/off-diagonal cases",
      DOMAIN_OK and any(v[0] == 0 and v[1] == 0 for v in TABLE.values())
      and any(v[0] != 0 and v[1] == 0 and v[4] == 0 for v in TABLE.values())
      and any(v[0] == 0 and v[1] != 0 for v in TABLE.values()))
print("SUMMARY: exact isotypic multiplicities permit mixed cubic carriers; the supplied Hamming grading selects two copies. The original finite coefficient table is retained, with ratios and phases only on their domains; no physical readout or carrier selection follows.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
