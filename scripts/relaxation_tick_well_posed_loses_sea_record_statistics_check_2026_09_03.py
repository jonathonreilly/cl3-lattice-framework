#!/usr/bin/env python3
"""A relaxation tick is well posed and loses the sea's record statistics.

Class-A finite-cluster runner, self-contained. Qubits sit on the 12 EDGE sites of
the 2x2x2 cube graph (8 corners, 6 faces); the sites compose ordinarily (tensor
product, operators on disjoint regions commute, no graded clause anywhere). A
record at an edge site registers a Z-value there, and the corner-parity
dictionary n_v = (1 - B_v)/2 registers occupancy from those records. The full
record space is 2^12 = 4096-dimensional; the code space (all six face
stabilizers S_f = +1) is 128-dimensional and realizes the even eight-mode Fock sector.
The identity prod_v B_v = I already holds on the full ambient carrier; it does
not define the face code. Local Z recording generally leaves that code. No dense object above 4096 x 4096 is formed, and every matrix
actually diagonalized is a record block of dimension at most 2048, split further
by the conserved record number N.

THE LAW. eta = the Kawamoto-Smit staggered link signs (eta_x = 1,
eta_y = (-1)^x, eta_z = (-1)^(x+y)), whose product round every one of the six
faces is -1: the all-minus (pi-flux) sector. H = -sum_e eta_e T_e with the
encoded hop T_ij = (i/2) A_ij (B_i - B_j), t = 1. THE SEA is the ground state of
H in the code space: E = -4 sqrt 3, non-degenerate, gap 2 sqrt 3, sharp N = 4.

THE TICK MODEL M_R IS STIPULATED HERE, NOT DERIVED. It is the vacuum panel's
candidate sentence -- "Between records, the lattice settles into its
lowest-energy arrangement" -- turned into a tick, with every free choice named:

  (i)   the state before any record is the sea;
  (ii)  each tick the next unrecorded edge site in a DECLARED order forms a
        record, which locks its value with the Born odds of the current
        pre-record state;
  (iii) the state is then REPLACED by the ground state of H restricted to the
        subspace consistent with all records so far. Unitarity is given up at
        this step. At fixed records R the reset is the linear CPTP map
        X -> Tr(X) Pi_R/deg_R; normalization of an outcome branch is nonlinear;
  (iv)  where that ground space is degenerate the state becomes the normalized
        projector Pi/deg onto it, and the next record's odds are its diagonal;
  (v)   records are permanent; the run continues to 12 records.
  The charge-superselected variant M_R^N, declared alongside, relaxes inside the
  conserved N = 4 sector of the block instead of the whole block.

Reference ticks computed against M_R: L, pure Lueders conditioning with no
dynamics at all (the p = 1 boundary, where the finished set is the sea's own
Born diagonal); and A, the tick of the parent note, identical to M_R except that
step (iii) is replaced by the unitary exp(-i tau H_R), run at tau = 0.5.

The runner establishes:

  A  THE RESTRICTION IDENTITY AND THE SETTING.  Every hop term flips exactly one
     edge qubit, so P_S H P_S = P_S (-sum over UNRECORDED e eta_e T_e) P_S:
     this is equality after compression to the actual ambient record block, and M_R is
     memoryless -- its state is a function of the record set alone.
  B  THE SEA'S OWN RECORD ODDS.  Flat 2^-k at every record block with k <= 3, and
     at p = 1 the Born support 1984 = 62 x 32 with 2112 zeros = 1856 charge zeros
     plus 256 cancellation zeros = the 8 closed corner stars x 32.
  C  SUPPORT.  Under M_R every one of the 4096 patterns carries positive odds and
     not one of the 2112 zeros survives, for every declared order.
  D  ORDER DEPENDENCE.  TV(identity, reverse) = 1/3, and the spread over the 32
     declared orders against exact order independence for pure Lueders.
  E  CHARGE.  <Q> = 0 and <N> = 4, but Q is no longer sharp; the spread sits
     exactly on the degenerate blocks; M_R^N restores sharp Q.
  F  RELAXATION AGAINST CONDITIONING.  Fidelities to the Lueders-conditioned sea
     at k = 1, 2, 3, the closed form -(12-k)/sqrt 3 for the Lueders-weighted mean,
     and the variational inequality at all 2048 blocks.
  G  THE POINTER-BASIS TABLE.  The corner-parity dictionary singles out the
     nontrivial Z_e measurement up to outcome labels under its supplied
     nondisturbance requirement; no physical basis is selected by this test.

NO SEEDS ANYWHERE. Nothing is sampled: MR enumerates all 4096 leaves. The
separate unitary/Lueders recursion omits relative branches at or below 1e-15.
Every order used is written out in this file. The 32 declared orders are the 12 cyclic shifts of the identity order,
their 12 reverses, and 8 further orders listed explicitly in ORDERS_EXTRA.

Line tags. `[exact]` = integer, F2 or symplectic Pauli arithmetic with no
floating point in the statement. `[numerical, tol]` = a deterministic
double-precision evaluation of an exactly specified quantity at the stated
threshold, with no sampling and no seed: the block ground spaces come from a
diagonalization, so numerical agreement alone is not an exact rational proof, and the tick
trees, though enumerated whole, are built from those diagonalizations.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import json
import sys
from functools import reduce

import hashlib
from pathlib import Path

AUDIT_INPUT_PATHS = ['docs/A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md']
_EXPECTED_INPUT_SHA256 = {'docs/A_RELAXATION_TICK_IS_WELL_POSED_AND_LOSES_THE_SEAS_RECORD_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-03.md': '906ca8ddfb18c960117242ae7222883a7f076474eb2007e3615e7ee457709aa3', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def _check_source_inputs():
    root = Path(__file__).resolve().parents[1]
    if len(AUDIT_INPUT_PATHS) != len(set(AUDIT_INPUT_PATHS)) or set(AUDIT_INPUT_PATHS) != set(_EXPECTED_INPUT_SHA256):
        raise SystemExit("SOURCE_INPUTS: declaration/pin mismatch")
    for rel in AUDIT_INPUT_PATHS:
        try:
            actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        except OSError as exc:
            raise SystemExit("SOURCE_INPUTS: missing/unreadable " + rel) from exc
        if actual != _EXPECTED_INPUT_SHA256[rel]:
            raise SystemExit("SOURCE_INPUTS: changed " + rel)
    print("SOURCE_INPUTS: exact declared note/memo/comparator inputs verified; physical suppliers remain conditional")

_check_source_inputs()

import numpy as np

AUDIT_TIMEOUT_SEC = 120

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


# --------------------------------------------------------------------------
# Pauli algebra in the symplectic representation, phases mod 4
# --------------------------------------------------------------------------
def pc(n):
    return bin(n).count("1")


PH = [1 + 0j, 1j, -1 + 0j, -1j]


class Pauli:
    """i^k * prod_q X_q^{x_q} Z_q^{z_q}, X before Z on every qubit."""

    __slots__ = ("k", "x", "z")

    def __init__(self, k, x, z):
        self.k = k % 4
        self.x = x
        self.z = z

    def __mul__(a, b):
        return Pauli(a.k + b.k + 2 * pc(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def neg(self):
        return Pauli(self.k + 2, self.x, self.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def is_herm(self):
        return self.k % 2 == pc(self.x & self.z) % 2

    def is_id(self):
        return self.x == 0 and self.z == 0 and self.k == 0

    def is_mid(self):
        return self.x == 0 and self.z == 0 and self.k == 2


IDP = Pauli(0, 0, 0)


def comm(a, b):
    return (pc(a.x & b.z) + pc(a.z & b.x)) % 2 == 0


def pact(p, b):
    """P|b> = amp |b ^ p.x>, amp a unit Gaussian integer."""
    return b ^ p.x, PH[p.k] * ((-1) ** (pc(p.z & b) % 2))


# --------------------------------------------------------------------------
# the cube and the superfast encoding (route B: Z tail on edges ordered BEFORE)
# --------------------------------------------------------------------------
def cube_cluster():
    return 8, sorted((min(s, s ^ bit), max(s, s ^ bit)) for s in range(8) for bit in (4, 2, 1) if s ^ bit > s)


def cube_faces():
    out = []
    for ax in range(3):
        bits = [4, 2, 1]
        fb = bits[ax]
        ob = [b for b in bits if b != fb]
        for val in (0, fb):
            out.append((val, val | ob[1], val | ob[0] | ob[1], val | ob[0]))
    return out


class Enc:
    def __init__(self, V, EDGES, FACES):
        self.V = V
        self.EDGES = list(EDGES)
        self.FACES = list(FACES)
        self.NQ = len(self.EDGES)
        self.DIM = 1 << self.NQ
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = q
            self.EIDX[(j, i)] = q
        self.NBR = {
            i: sorted(j for (a, b) in self.EDGES for j in ((b,) if a == i else ((a,) if b == i else ())))
            for i in range(V)
        }
        self.STAR = {i: [self.EIDX[(i, k)] for k in self.NBR[i]] for i in range(V)}
        self.STARMASK = {i: reduce(lambda a, b: a | (1 << b), self.STAR[i], 0) for i in range(V)}

    def A_unsigned(self, i, j):
        x = 1 << self.EIDX[(i, j)]
        z = 0
        for k in self.NBR[i]:
            if k != j and k < j:
                z ^= 1 << self.EIDX[(i, k)]
        for l in self.NBR[j]:
            if l != i and l < i:
                z ^= 1 << self.EIDX[(j, l)]
        return Pauli(pc(x & z) % 2, x, z)

    def A(self, i, j):
        p = self.A_unsigned(i, j)
        return p if i < j else p.neg()

    def B(self, i):
        return Pauli(0, 0, self.STARMASK[i])

    def loop(self, cyc):
        out = IDP
        for a in range(len(cyc)):
            out = out * self.A(cyc[a], cyc[(a + 1) % len(cyc)])
        return out

    def record(self, z):
        return tuple(pc(z & self.STARMASK[i]) % 2 for i in range(self.V))

    def hop_pauli(self, i, j):
        A = self.A(i, j)
        return A * self.B(i), A * self.B(j)

    def hop_amp(self, P1, P2, y):
        b1, a1 = pact(P1, y)
        b2, a2 = pact(P2, y)
        assert b1 == b2
        v = 0.5j * (a1 - a2)
        assert abs(v.real - round(v.real)) < 1e-12 and abs(v.imag - round(v.imag)) < 1e-12
        return b1, complex(round(v.real), round(v.imag))


def encoding_audit(E):
    """R0-R4 pair by pair, the face group, k, and the code dimension. All exact."""
    R = {}
    A = {e: E.A(*e) for e in E.EDGES}
    Bv = {i: E.B(i) for i in range(E.V)}
    R["R0"] = all(E.A_unsigned(i, j) == E.A_unsigned(j, i) for (i, j) in E.EDGES) and all(
        E.A(j, i) == E.A(i, j).neg() for (i, j) in E.EDGES
    )
    R["R1"] = all(A[e].is_herm() and (A[e] * A[e]).is_id() for e in E.EDGES) and all(
        Bv[i].is_herm() and (Bv[i] * Bv[i]).is_id() for i in range(E.V)
    )
    r2 = all(comm(Bv[i], Bv[j]) for i, j in itertools.combinations(range(E.V), 2))
    for e in E.EDGES:
        for v in range(E.V):
            r2 &= comm(A[e], Bv[v]) != (v in e)
    R["R2"] = bool(r2)
    R["R3"] = all(
        comm(A[e], A[f]) != (len(set(e) & set(f)) == 1) for e, f in itertools.combinations(E.EDGES, 2)
    )
    S = [E.loop(f) for f in E.FACES]
    r4 = True
    for s in S:
        r4 &= s.is_herm() and (s * s).is_id()
        for e in E.EDGES:
            r4 &= comm(s, A[e])
        for v in range(E.V):
            r4 &= comm(s, Bv[v])
    for a, b in itertools.combinations(S, 2):
        r4 &= comm(a, b)
    R["R4"] = bool(r4)
    R["S"] = S
    gens, basis = [], []
    for s in S:
        v = s.x
        for b in basis:
            v = min(v, v ^ b)
        if v != 0:
            basis.append(v)
            basis.sort(reverse=True)
            gens.append(s)
    R["k"] = len(gens)
    grp = []
    for m in range(1 << len(gens)):
        p = IDP
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        grp.append(p)
    R["grp"] = grp
    R["grp_ok"] = (not any(g.is_mid() for g in grp)) and sum(1 for g in grp if g.x == 0) == 1
    R["code_dim"] = E.DIM >> len(gens)
    return R


def code_space(E, R):
    """Cosets of the face group; phi[z] is the unit coefficient of |z> in its coset."""
    grp = R["grp"]
    phi = np.zeros(E.DIM, dtype=complex)
    cid = -np.ones(E.DIM, dtype=np.int64)
    reps = []
    for z0 in range(E.DIM):
        if cid[z0] >= 0:
            continue
        c = len(reps)
        reps.append(z0)
        for g in grp:
            b, a = pact(g, z0)
            assert cid[b] < 0
            cid[b] = c
            phi[b] = a
    assert (cid >= 0).all()
    return cid, phi, reps


VN, EDG = cube_cluster()
FAC = cube_faces()
EN = Enc(VN, EDG, FAC)
AUD = encoding_audit(EN)
CID, PHI, REPS = code_space(EN, AUD)
D = EN.DIM
NQ = EN.NQ

# ------------------------------------------------------- staggered link signs
def corner_xyz(s):
    return ((s >> 2) & 1, (s >> 1) & 1, s & 1)


def eta_ks(v, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


ETA = np.zeros(NQ, dtype=np.int64)
EDIR = np.zeros(NQ, dtype=np.int64)
for q, (i, j) in enumerate(EN.EDGES):
    a = {4: 0, 2: 1, 1: 2}[min(i, j) ^ max(i, j)]
    EDIR[q] = a
    ETA[q] = eta_ks(corner_xyz(min(i, j)), a)

FACE_FLUX = [
    int(np.prod([ETA[EN.EIDX[(cyc[t], cyc[(t + 1) % 4])]] for t in range(4)])) for cyc in FAC
]

# --------------------------------------------- H on the full 4096 record space
HOPX_OK = True
MI = np.zeros((NQ, D), dtype=np.int64)  # H[z ^ (1<<q), z] = 1j * MI[q, z]
for q, e in enumerate(EN.EDGES):
    P1, P2 = EN.hop_pauli(*e)
    HOPX_OK &= (P1.x == (1 << q)) and (P2.x == (1 << q))
    for z in range(D):
        zz, amp = EN.hop_amp(P1, P2, z)
        if amp == 0:
            continue
        assert zz == z ^ (1 << q) and abs(amp.real) < 1e-12
        MI[q, z] = -int(ETA[q]) * int(round(amp.imag))  # H = -sum_e eta_e T_e

HAMP = 1j * MI.astype(np.float64)
HERM_OK = True
for q in range(NQ):
    HERM_OK &= bool(np.all(MI[q, np.arange(D) ^ (1 << q)] == -MI[q]))

RECZ = np.array([EN.record(z) for z in range(D)], dtype=np.int8)
NVAL = RECZ.sum(1).astype(np.int64)
QVAL = NVAL - 4  # Q = -(1/2) sum_v B_v = N - 4


def Hmul(psi):
    out = np.zeros(D, dtype=np.complex128)
    idx = np.arange(D)
    for q in range(NQ):
        out[idx ^ (1 << q)] += HAMP[q] * psi
    return out


# ------------------------------------------------------------ code space + sea
NCOSET = len(REPS)
W = np.zeros((D, NCOSET), dtype=np.complex128)
W[np.arange(D), CID] = PHI / np.sqrt(float(1 << AUD["k"]))
WORTH = float(np.max(np.abs(W.conj().T @ W - np.eye(NCOSET))))
HW = np.zeros((D, NCOSET), dtype=np.complex128)
for c in range(NCOSET):
    HW[:, c] = Hmul(W[:, c])
HC = W.conj().T @ HW
CODE_INV = float(np.max(np.abs(HW - W @ HC)))
EVC, VCC = np.linalg.eigh(HC)
SEA = W @ VCC[:, 0]
E_SEA = float(EVC[0])
SEA_GAP = float(EVC[1] - EVC[0])
SEA_DEG = int(np.sum(EVC < EVC[0] + 1e-9))
P_SEA = np.abs(SEA) ** 2
SEA_OFF_N4 = float(P_SEA[NVAL != 4].sum())
SQ3 = float(np.sqrt(3.0))

# --------------------------------------------------------------- record blocks
ARG = np.arange(D)
LOC = -np.ones(D, dtype=np.int64)
TOL = 1e-9


def block_M(Rmask, w):
    """H on the block S(R,w) = {z : z & Rmask == w}, split by the conserved N.

    Every hop term flips exactly one edge qubit, so the terms surviving the
    restriction are exactly the hops on UNRECORDED sites: this is the parent
    note's H_R. Its matrix is purely imaginary, so H = i M with M real and
    skew-symmetric; the spectrum of H on each N sector is therefore symmetric
    about 0, its square is M M^T, and the ground level is -sqrt(lambda_max)."""
    I = ARG[(ARG & Rmask) == w]
    free = [q for q in range(NQ) if not (Rmask >> q) & 1]
    out = []
    for n in np.unique(NVAL[I]):
        J = I[NVAL[I] == n]
        d = len(J)
        LOC[J] = np.arange(d)
        M = np.zeros((d, d))
        cols = np.arange(d)
        for q in free:
            a = MI[q][J]
            m = a != 0
            if not m.any():
                continue
            assert np.all(NVAL[J[m] ^ (1 << q)] == n)
            M[LOC[J[m] ^ (1 << q)], cols[m]] += a[m]
        LOC[J] = -1
        out.append((J, M))
    return out


def sector_ground(M):
    """(E0, top eigenvectors of M M^T, their count) for one N sector."""
    if M.size == 0 or not M.any():
        return 0.0, None, M.shape[0]
    lam, V = np.linalg.eigh(M @ M.T)
    lmax = float(lam[-1])
    if lmax <= 1e-9:
        return 0.0, None, M.shape[0]
    sel = np.flatnonzero(lam > lmax - 1e-7 * max(1.0, lmax))
    assert len(sel) % 2 == 0
    return -float(np.sqrt(lmax)), V[:, sel], len(sel)


def relax(Rmask, w, nfix=None):
    """The relaxed state on block (R,w): the normalized projector Pi/deg onto the
    ground space of H restricted to the block (to the N = nfix sector if given).
    Returns (E0, deg, indices, diagonal), the diagonal summing to 1.

    Because H = i M with M real skew, the ground projector inside a sector is
    (1/2)(P - (i/mu) M P) with P the real spectral projector of M M^T at
    lambda_max; M P is skew, so the projector's DIAGONAL is exactly (1/2) diag P."""
    secs = []
    for J, M in block_M(Rmask, w):
        if nfix is not None and NVAL[J[0]] != nfix:
            continue
        e, V, d = sector_ground(M)
        secs.append((J, M, e, V, d))
    if not secs:
        return None, 0, None, None
    E0 = min(s[2] for s in secs)
    tot = 0
    Js, vs = [], []
    for J, M, e, V, d in secs:
        if e > E0 + TOL:
            continue
        if V is None:
            tot += d
            Js.append(J)
            vs.append(np.ones(len(J)))
        else:
            tot += d // 2
            Js.append(J)
            vs.append(0.5 * np.sum(V ** 2, axis=1))
    return E0, tot, np.concatenate(Js), np.concatenate(vs) / tot


def relax_full(Rmask, w):
    """As relax, but also returns the per-sector data needed for fidelities."""
    secs = []
    for J, M in block_M(Rmask, w):
        e, V, d = sector_ground(M)
        secs.append((J, M, e, V, d))
    E0 = min(s[2] for s in secs)
    tot = sum((d if V is None else d // 2) for J, M, e, V, d in secs if e <= E0 + TOL)
    return E0, tot, secs


def fidelity(secs, E0, deg, psi):
    """<psi| Pi/deg |psi> with Pi the ground projector of the block."""
    f = 0.0
    for J, M, e, V, d in secs:
        if e > E0 + TOL:
            continue
        v = psi[J]
        if V is None:
            f += float(np.vdot(v, v).real)
        else:
            c = V.T @ v
            f += 0.5 * float((np.vdot(c, c) - (1j / (-e)) * np.vdot(v, M @ (V @ c))).real)
    return f / deg


def expect_HR(Rmask, w, psi):
    """<psi| H_R |psi> on the block, without any diagonalization."""
    return sum(float((1j * np.vdot(psi[J], M @ psi[J])).real) for J, M in block_M(Rmask, w))


def evolve_HR(Rmask, w, psi, tau):
    """exp(-i tau H_R) psi = exp(tau M) psi, sector by sector."""
    out = np.zeros(D, dtype=np.complex128)
    for J, M in block_M(Rmask, w):
        v = psi[J]
        if not M.any():
            out[J] = v
            continue
        lam, V = np.linalg.eigh(M @ M.T)
        mu = np.sqrt(np.maximum(lam, 0.0))
        c = V.T @ v
        si = np.where(mu > 1e-9, np.sin(tau * mu) / np.where(mu > 1e-9, mu, 1.0), 0.0)
        out[J] = V @ (np.cos(tau * mu) * c) + M @ (V @ (si * c))
    return out


# --------------------------------------------------------------- the tick trees
BLOCK_CACHE = {}


def relaxed_node(Rmask, w):
    r = BLOCK_CACHE.get((Rmask, w))
    return r if r is not None else relax(Rmask, w)


def tree_MR(order, nfix=None, stats=None):
    """The exact M_R tree for one declared order: all 4096 leaves, nothing sampled."""
    out = np.zeros(D)
    order = list(order)

    def rec(k, Rmask, w, J, v, prob):
        if k == NQ:
            out[w] += prob
            return
        q = order[k]
        hi = ((J >> q) & 1).astype(bool)
        for b in (0, 1):
            m = hi if b else ~hi
            pb = float(v[m].sum())
            if pb <= 0.0:
                continue
            R2 = Rmask | (1 << q)
            w2 = w | (b << q)
            E0, deg, J2, v2 = relax(R2, w2, nfix) if nfix is not None else relaxed_node(R2, w2)
            if J2 is None:
                continue
            if stats is not None:
                stats.append((k + 1, prob * pb, E0, deg, float((v2 * NVAL[J2]).sum()), len(set(NVAL[J2].tolist()))))
            rec(k + 1, R2, w2, J2, v2, prob * pb)

    rec(0, 0, 0, ARG, P_SEA.copy(), 1.0)
    return out


def tree_unitary(order, tau, lueders=False, prof=None):
    """The Lueders tree (tau ignored) and the parent note's Model A tree."""
    out = np.zeros(D)
    order = list(order)

    def rec(k, Rmask, w, psi, prob):
        if k == NQ:
            out[w] += prob
            return
        q = order[k]
        d = np.abs(psi) ** 2
        for b in (0, 1):
            sel = ((ARG >> q) & 1) == b
            pb = float(d[sel].sum())
            if pb <= 1e-15:
                continue
            R2 = Rmask | (1 << q)
            w2 = w | (b << q)
            p2 = psi.copy()
            p2[~sel] = 0.0
            p2 /= np.linalg.norm(p2)
            if prof is not None:
                prof.setdefault(k + 1, []).append((prob * pb, expect_HR(R2, w2, p2)))
            if not lueders:
                p2 = evolve_HR(R2, w2, p2, tau)
            rec(k + 1, R2, w2, p2, prob * pb)

    rec(0, 0, 0, SEA.copy(), 1.0)
    return out


def tv(p, q):
    return 0.5 * float(np.abs(np.asarray(p) - np.asarray(q)).sum())


# ------------------------------------------------------------ declared orders
ORDER_ID = list(range(12))
ORDERS_SHIFT = [[(j + i) % 12 for i in range(12)] for j in range(12)]
ORDERS_REV = [list(reversed(o)) for o in ORDERS_SHIFT]
ORDERS_EXTRA = [
    [2, 4, 6, 7, 1, 3, 9, 10, 0, 5, 8, 11],   # x edges, then y, then z
    [0, 5, 8, 11, 1, 3, 9, 10, 2, 4, 6, 7],   # z edges, then y, then x
    [5, 8, 9, 10, 0, 1, 2, 3, 4, 6, 7, 11],   # the four eta = -1 sites first
    [0, 1, 2, 7, 10, 11, 3, 4, 5, 6, 8, 9],   # star of corner 0, star of corner 7, rest
    [0, 2, 4, 6, 8, 10, 1, 3, 5, 7, 9, 11],   # even indices, then odd
    [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10],   # odd indices, then even
    [0, 6, 3, 9, 1, 7, 4, 10, 2, 8, 5, 11],   # index bit-reversal
    [5, 11, 0, 8, 2, 9, 7, 1, 10, 4, 3, 6],   # outward from site 5
]
ORDERS = ORDERS_SHIFT + ORDERS_REV + ORDERS_EXTRA
assert len({tuple(o) for o in ORDERS}) == 32
assert all(sorted(o) == ORDER_ID for o in ORDERS)

# ==========================================================================
# A -- the restriction identity and the setting
# ==========================================================================
check(
    "A1 [exact] cube 2x2x2, 8 corners / 12 edge sites / 6 faces: the superfast relations R0-R4 hold pair by pair, the face "
    "group carries no -I, k = %d, code dimension 2^12/2^%d = %d" % (AUD["k"], AUD["k"], AUD["code_dim"]),
    AUD["R0"] and AUD["R1"] and AUD["R2"] and AUD["R3"] and AUD["R4"] and AUD["grp_ok"]
    and AUD["k"] == 5 and AUD["code_dim"] == 128 and D == 4096 and NQ == 12,
)
check(
    "A2 [exact] the Kawamoto-Smit staggered signs put flux %s on all six faces -- the all-minus (pi-flux) sector -- and "
    "H = -sum_e eta_e T_e is Hermitian on the 4096-dimensional record space" % (set(FACE_FLUX),),
    all(f == -1 for f in FACE_FLUX) and HERM_OK,
)
check(
    "A3 [exact] THE RESTRICTION IDENTITY: each of the 12 hop terms has Pauli X-part exactly one edge qubit, so P_S H P_S is the "
    "signed sum of hops on UNRECORDED sites, with P_S on both sides; M_R is memoryless on records",
    HOPX_OK,
)
check(
    "A4 [numerical, 1e-11] the code space (six S_f = +1, dim 128 realizes the even-Fock sector) is H-invariant to %.1e; the sea, its ground "
    "state, has E = %.12f = -4 sqrt 3, non-degenerate, gap %.12f = 2 sqrt 3, sharp N = 4 (mass off N = 4: %.1e)"
    % (CODE_INV, E_SEA, SEA_GAP, SEA_OFF_N4),
    WORTH < 1e-12 and CODE_INV < 1e-11 and abs(E_SEA + 4 * SQ3) < 1e-11
    and SEA_DEG == 1 and abs(SEA_GAP - 2 * SQ3) < 1e-11 and SEA_OFF_N4 < 1e-25,
)

# ==========================================================================
# B -- the sea's own record odds
# ==========================================================================
flat_dev = 0.0
fid = {}
viol = 0
nblocks = {}
for k in (1, 2, 3):
    F, EE, LL = [], [], []
    for S in itertools.combinations(range(NQ), k):
        Rmask = sum(1 << q for q in S)
        for vals in itertools.product((0, 1), repeat=k):
            w = sum(b << q for q, b in zip(S, vals))
            E0, deg, secs = relax_full(Rmask, w)
            BLOCK_CACHE[(Rmask, w)] = relax(Rmask, w)
            sel = (ARG & Rmask) == w
            psi = SEA.copy()
            psi[~sel] = 0.0
            wgt = float(np.vdot(psi, psi).real)
            flat_dev = max(flat_dev, abs(wgt - 2.0 ** -k))
            psi /= np.sqrt(wgt)
            F.append(fidelity(secs, E0, deg, psi))
            eL = expect_HR(Rmask, w, psi)
            LL.append(eL)
            EE.append(E0)
            if E0 > eL + 1e-9:
                viol += 1
    fid[k] = (np.array(F), np.array(LL))
    nblocks[k] = len(F)

zero_idx = np.flatnonzero(P_SEA < 1e-12)
n_zero = len(zero_idx)
n_charge = int((NVAL[zero_idx] != 4).sum())
canc = zero_idx[NVAL[zero_idx] == 4]
canc_pats = {tuple(RECZ[z]) for z in canc}
supp_pats = {tuple(RECZ[z]) for z in np.flatnonzero(P_SEA >= 1e-12)}
stars = set()
for v in range(8):
    s = [0] * 8
    s[v] = 1
    for u in EN.NBR[v]:
        s[u] = 1
    stars.add(tuple(s))

check(
    "B1 [numerical, 1e-12] the sea's own record odds are FLAT: each of the %d + %d + %d = %d record blocks with k <= 3 carries "
    "sea weight 2^-k to %.1e -- odds 1/2, nothing forced up to three records"
    % (nblocks[1], nblocks[2], nblocks[3], sum(nblocks.values()), flat_dev),
    flat_dev < 1e-12 and nblocks == {1: 24, 2: 264, 3: 1760},
)
check(
    "B2 [exact, 1e-12 zero read] at p = 1, where the finished set is the sea's own Born diagonal, the support is %d = 62 x 32 and the %d zeros "
    "split as %d charge zeros (N != 4) + %d cancellation zeros" % (4096 - n_zero, n_zero, n_charge, len(canc)),
    (4096 - n_zero) == 1984 and len(supp_pats) == 62 and n_zero == 2112 and n_charge == 1856 and len(canc) == 256,
)
check(
    "B3 [exact, 1e-12 zero read] the %d cancellation zeros are %d corner-occupation patterns x 32, and those are EXACTLY the 8 corner "
    "stars {v} u N(v) -- the cube's selection-rule zeros" % (len(canc), len(canc_pats)),
    canc_pats == stars and len(stars) == 8 and len(canc) == 8 * 32,
)

# ==========================================================================
# C -- support: every pattern becomes admissible
# ==========================================================================
P_ORD = [tree_MR(o) for o in ORDERS]
P_MR = P_ORD[0]
P_A = tree_unitary(ORDER_ID, 0.5)
supp_all = [int((p > 1e-13).sum()) for p in P_ORD]
kept_all = [int((p[zero_idx] < 1e-13).sum()) for p in P_ORD]
tv_mr = tv(P_MR, P_SEA)
tv_A = tv(P_A, P_SEA)

check(
    "C1 [numerical, 1e-12] under M_R at the identity order all 4096 patterns carry positive odds (support %d, smallest "
    "%.3e): not one of the sea's %d zeros survives" % (supp_all[0], float(P_MR.min()), n_zero),
    supp_all[0] == 4096 and kept_all[0] == 0 and P_MR.min() > 0,
)
check(
    "C2 [numerical, 1e-12] the same for all 32 declared orders: support 4096 in all 32, 0 of the 2112 zeros kept -- the charge "
    "zeros included, though N is conserved by H and by every record projection",
    all(s == 4096 for s in supp_all) and all(z == 0 for z in kept_all),
)
check(
    "C3 [numerical, 1e-12] TV(M_R identity order, sea Born) = %.12f = 1283/2880: this tick is not the sea's registration" % tv_mr,
    abs(tv_mr - 1283 / 2880) < 1e-12,
)
check(
    "C4 [numerical, 1e-12] the locally redeclared Model A at tau = 0.5 sits CLOSER to the sea -- TV %.12f against %.12f -- on "
    "support %d, keeping all %d charge zeros and losing the same 256 cancellation zeros"
    % (tv_A, tv_mr, int((P_A > 1e-13).sum()), int((P_A[zero_idx] < 1e-13).sum())),
    tv_A < tv_mr and abs(tv_A - 0.324925160534) < 1e-9 and int((P_A > 1e-13).sum()) == 2240
    and int((P_A[zero_idx] < 1e-13).sum()) == 1856,
)

# ==========================================================================
# D -- order dependence
# ==========================================================================
tv_rev = tv(P_ORD[0], P_ORD[12])
pairs = [(a, b) for a in range(32) for b in range(a + 1, 32)]
tvs = [tv(P_ORD[a], P_ORD[b]) for a, b in pairs]
tv_max, tv_min = max(tvs), min(tvs)
tv_sea = [tv(p, P_SEA) for p in P_ORD]
P_L = tree_unitary(ORDER_ID, 0.0, lueders=True)
P_LR = tree_unitary(list(reversed(ORDER_ID)), 0.0, lueders=True)

check(
    "D1 [numerical, 1e-12] the odds depend on the order in which the sites record: TV(identity, reverse) = %.12f = 1/3, for "
    "the same twelve sites and the same tick" % tv_rev,
    abs(tv_rev - 1.0 / 3.0) < 1e-12,
)
check(
    "D2 [numerical, 1e-12] over the 32 declared orders (12 cyclic shifts, their reverses, 8 more written out; no seed) the "
    "maximal pairwise TV is %.12f, the minimal %.12f, TV to the sea %.9f .. %.9f -- a LOWER BOUND over all 12! orders"
    % (tv_max, tv_min, min(tv_sea), max(tv_sea)),
    tv_max > 0.7 and tv_min > 0.1 and abs(min(tv_sea) - tv_mr) < 1e-12,
)
check(
    "D3 [numerical, 1e-14] twelve SEQUENTIAL commuting Lueders recordings reproduce the supplied sea Born diagonal "
    "to %.1e, identity and reverse agreeing to %.1e" % (tv(P_L, P_SEA), tv(P_L, P_LR)),
    tv(P_L, P_SEA) < 1e-14 and tv(P_L, P_LR) < 1e-14 and int((P_L > 1e-13).sum()) == 1984,
)

# ==========================================================================
# E -- charge
# ==========================================================================
stats = []
tree_MR(ORDER_ID, stats=stats)
law = np.array([float(P_MR[QVAL == v].sum()) for v in (-4, -2, 0, 2, 4)])
law_exact = np.array([1 / 384, 1 / 8, 143 / 192, 1 / 8, 1 / 384])
varQ = float((P_MR * QVAL ** 2).sum())
meanQ = [abs(float((p * QVAL).sum())) for p in P_ORD]
meanN = [abs(float((p * NVAL).sum()) - 4.0) for p in P_ORD]
pq0 = [float(p[QVAL == 0].sum()) for p in P_ORD]
vq = [float((p * QVAL ** 2).sum()) for p in P_ORD]
mixed = [r for r in stats if r[5] > 1]
degen = [r for r in stats if r[3] > 1]
mixed_ticks = sorted({r[0] for r in mixed})
nmean_tick = {k: sum(r[1] * r[4] for r in stats if r[0] == k) for k in range(1, 13)}
P_MRN = tree_MR(ORDER_ID, nfix=4)

check(
    "E1 [numerical, 1e-12] M_R keeps half filling on average at all 32 orders: max |<Q>| = %.1e, max |<N> - 4| = %.1e"
    % (max(meanQ), max(meanN)),
    max(meanQ) < 1e-12 and max(meanN) < 1e-12,
)
check(
    "E2 [numerical, 1e-12] but the readable charge is no longer sharp: at the identity order the law over Q = -4,-2,0,2,4 is "
    "%s = (1/384, 1/8, 143/192, 1/8, 1/384), var Q = %.12f = 13/12"
    % (", ".join("%.7f" % x for x in law), varQ),
    float(np.max(np.abs(law - law_exact))) < 1e-12 and abs(varQ - 13 / 12) < 1e-12,
)
check(
    "E3 [numerical, 1e-12] and the charge law depends on the order: over the 32 orders P(Q = 0) ranges %.12f .. %.12f, var Q "
    "%.12f .. %.12f" % (min(pq0), max(pq0), min(vq), max(vq)),
    max(pq0) - min(pq0) > 0.2 and max(vq) - min(vq) > 1.0,
)
check(
    "E4 [numerical, 1e-12] the spread sits on the Pi/deg tie-break: of the 8190 nodes of the identity tree the %d not N-sharp "
    "are EXACTLY the %d with a degenerate ground space, at ticks %s; per tick the weight-averaged <N> stays 4 (to %.1e)"
    % (len(mixed), len(degen), mixed_ticks, max(abs(v - 4.0) for v in nmean_tick.values())),
    len(mixed) == len(degen) and len(mixed) > 0
    and all((r[5] > 1) == (r[3] > 1) for r in stats)
    and mixed_ticks == [5, 6, 8, 9, 11]
    and max(abs(v - 4.0) for v in nmean_tick.values()) < 1e-12,
)
check(
    "E5 [numerical, 1e-12] the variant M_R^N -- relax inside the conserved N = 4 sector -- restores P(Q = 0) = %.12f and all %d "
    "charge zeros on support %d, but still loses all 256 cancellation zeros, as Model A does"
    % (float(P_MRN[QVAL == 0].sum()), int((P_MRN[zero_idx] < 1e-13).sum()), int((P_MRN > 1e-13).sum())),
    abs(float(P_MRN[QVAL == 0].sum()) - 1.0) < 1e-12 and int((P_MRN > 1e-13).sum()) == 2240
    and int((P_MRN[zero_idx] < 1e-13).sum()) == 1856,
)

# ==========================================================================
# F -- relaxation against conditioning
# ==========================================================================
prof = {}
tree_unitary(ORDER_ID, 0.0, lueders=True, prof=prof)
lue_col = {k: sum(a * b for a, b in prof[k]) / sum(a for a, _ in prof[k]) for k in prof}
lue_dev = max(abs(lue_col[k] + (12 - k) / SQ3) for k in lue_col)
relaxed_col = {
    k: sum(r[1] * r[2] for r in stats if r[0] == k) / sum(r[1] for r in stats if r[0] == k) for k in range(1, 13)
}
drops = {k: lue_col[k] - relaxed_col[k] for k in range(1, 13)}
kpeak = max(drops, key=lambda k: drops[k])
F1 = fid[1][0]
F3 = fid[3][0]

check(
    "F1 [numerical, 1e-12] relaxation parts from conditioning at the FIRST record: the relaxed state and the conditioned sea "
    "overlap by %.12f at all 24 (site, value) blocks, identically (spread %.1e)"
    % (float(F1.mean()), float(F1.max() - F1.min())),
    float(F1.max() - F1.min()) < 1e-12 and abs(float(F1.mean()) - 0.962606705806) < 1e-9,
)
check(
    "F2 [numerical, 1e-12] by three records the overlap is %.12f in the worst of the 1760 blocks, mean %.12f, while in %d of "
    "them the conditioned sea IS the block ground state (overlap 1)"
    % (float(F3.min()), float(F3.mean()), int((F3 > 1 - 1e-9).sum())),
    abs(float(F3.min()) - 0.448473881026) < 1e-9 and abs(float(F3.mean()) - 0.773546569701) < 1e-9
    and int((F3 > 1 - 1e-9).sum()) == 64,
)
check(
    "F3 [numerical, 1e-12] the Lueders-weighted conditional ENERGY MEAN is -(12-k)/sqrt 3 (to %.1e); "
    "individual positive-weight outcomes need not have that energy" % lue_dev,
    lue_dev < 1e-12,
)
check(
    "F4 [numerical, 1e-9] relaxation lowers the energy and never raises it: E_0(R,w) <= <sea_S|H_R|sea_S> at all %d blocks with "
    "k <= 3, %d violations" % (sum(nblocks.values()), viol),
    viol == 0,
)
check(
    "F5 [numerical, 1e-12] DIFFERENCE of Lueders-weighted and MR-weighted energy means peaks at k = %d (%.12f); "
    "zero at the common k=0 sea and one-dimensional k=12 block, and to %.1e at k=3; not a common-law mean gain"
    % (kpeak, drops[kpeak], abs(drops[3])),
    kpeak == 9 and abs(drops[kpeak] - 0.401011505139) < 1e-9 and abs(drops[12]) < 1e-12 and abs(drops[3]) < 1e-12,
)

# ==========================================================================
# G -- the pointer-basis table
# ==========================================================================
BV = [EN.B(i) for i in range(8)]
SF = [EN.loop(f) for f in FAC]


def one_site(q, kind):
    return Pauli(1 if kind == "Y" else 0, (1 << q) if kind in "XY" else 0, (1 << q) if kind in "ZY" else 0)


z_vs_B = [sum(1 for v in range(8) if not comm(one_site(q, "Z"), BV[v])) for q in range(12)]
xy_endpoints = all(
    sorted(v for v in range(8) if not comm(one_site(q, kind), BV[v])) == sorted(EN.EDGES[q])
    for q in range(12)
    for kind in ("X", "Y")
)
z_faces_ok = True
for q in range(12):
    anti = sorted(f for f in range(6) if not comm(one_site(q, "Z"), SF[f]))
    thru = sorted(
        f for f, cyc in enumerate(FAC) if q in [EN.EIDX[(cyc[t], cyc[(t + 1) % 4])] for t in range(4)]
    )
    z_faces_ok &= anti == thru and len(thru) == 2
no_basis_both = all(
    any(not comm(one_site(q, kind), BV[v]) for v in range(8))
    or any(not comm(one_site(q, kind), SF[f]) for f in range(6))
    for q in range(12)
    for kind in ("X", "Y", "Z")
)

check(
    "G1 [exact] GIVEN the corner-parity dictionary and its nondisturbance requirement: Z_e commutes with all 8 parities B_v at all 12 sites, "
    "while X_e and Y_e each anticommute with exactly the two endpoint parities of their site",
    all(c == 0 for c in z_vs_B) and xy_endpoints,
)
check(
    "G2 [exact] the face dictionary singles out none: Z_e anticommutes with exactly the two faces through e at all 12 sites, and "
    "no one-site basis commutes with the corner and face dictionaries at once",
    z_faces_ok and no_basis_both,
)

# The original ensemble columns are retained; individual conditional values differ.
energy_rows = []
for value in range(32):
    cond = SEA.copy()
    cond[(ARG & 31) != value] = 0
    probability = float(np.vdot(cond, cond).real)
    assert probability > 0
    cond /= np.sqrt(probability)
    energy = expect_HR(31, value, cond)
    energy_rows.append(dict(mask=31, value=value, probability=probability, energy=energy))
energy_mean = sum(r["probability"] * r["energy"] for r in energy_rows)
check("F6 [numerical, 1e-12] actual mask31 conditional counterexamples and all 32-outcome energy average; "
      "value 0 has probability 1/48, energy -2sqrt3; value 2 has probability 1/24, energy -(5/2)sqrt3",
      abs(energy_rows[0]["probability"]-1/48)<1e-12
      and abs(energy_rows[2]["probability"]-1/24)<1e-12
      and abs(energy_rows[0]["energy"]+2*SQ3)<1e-12
      and abs(energy_rows[2]["energy"]+2.5*SQ3)<1e-12
      and abs(sum(r["probability"] for r in energy_rows)-1)<1e-12
      and abs(energy_mean+7/SQ3)<1e-12)
print("CONDITIONAL_ENERGY_ROWS " + json.dumps(energy_rows, sort_keys=True))
print("ENSEMBLE_ENERGY_ROWS " + json.dumps([
    dict(k=k, lueders_mean=lue_col[k], MR_mean=relaxed_col[k], difference=drops[k])
    for k in range(1, 13)], sort_keys=True))

# Fixed-record reset: a finite Kraus check of the accompanying general proof.
sigma = np.diag([0.6, 0.4, 0.0])
kraus = []
for i, lam in enumerate(np.diag(sigma)):
    for j in range(3):
        z = np.zeros((3, 3), complex)
        z[i, j] = np.sqrt(lam)
        kraus.append(z)
rho = np.array([[.4, .1j, .05], [-.1j, .4, .02], [.05, .02, .2]], complex)
reset_rho = sum(k @ rho @ k.conj().T for k in kraus)
check("H1 [numerical, 1e-14] fixed-record reset has complete Kraus normalization and equals Tr(rho)sigma; "
      "normalized outcome conditioning is separate",
      np.max(abs(sum(k.conj().T@k for k in kraus)-np.eye(3)))<1e-14
      and np.max(abs(reset_rho-np.trace(rho)*sigma))<1e-14)
check("H2 [exact/numerical] even corner parity holds on all 4096 ambient words; the 128-dimensional face code "
      "is a distinct supplied sector, and local Z does not preserve it",
      bool((NVAL % 2 == 0).all()) and W.shape == (4096, 128)
      and len(AUD["grp"]) == 32 and z_faces_ok)

print(
    "SUMMARY: the stipulated relaxation tick is well posed and memoryless, its state a function of the records alone, and it does "
    "not give back the sea's odds: every pattern becomes admissible, the zeros go, the odds depend on the order."
)
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
