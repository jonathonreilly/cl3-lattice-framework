#!/usr/bin/env python3
"""Joint corner formation: finite schedules that preserve or lose the sea's zeros.

Class-A finite-cluster runner, self-contained. Qubits sit on the 12 EDGE sites of
the 2x2x2 cube graph (8 corners, 6 faces); the sites compose ordinarily (tensor
product, operators on disjoint regions commute, no graded clause anywhere). A
record at an edge site registers a Z-value there, and the corner-parity
dictionary n_v = (1 - B_v)/2 registers occupancy from those records. The full
record space is 2^12 = 4096-dimensional; the code space (all six face
stabilizers S_f = +1) is 128-dimensional and, because prod_v B_v = I, is the
even-N space. No dense object above 4096 x 4096 is formed, and every matrix
actually diagonalized is a record block of dimension at most 2048, split further
by the conserved record number N.

THE LAW. eta = the Kawamoto-Smit staggered link signs (eta_x = 1,
eta_y = (-1)^x, eta_z = (-1)^(x+y)), whose product round every one of the six
faces is -1: the all-minus (pi-flux) sector. H = -sum_e eta_e T_e with the
encoded hop T_ij = (i/2) A_ij (B_i - B_j), t = 1. THE SEA is the ground state of
H in the code space: E = -4 sqrt 3, non-degenerate, gap 2 sqrt 3, sharp N = 4.

WHAT IS STIPULATED HERE, AND DERIVED FROM NOTHING. The site-wise parent note
(PR #7895) lets one edge site at a time register. This runner stipulates a UNIT
of record formation instead -- a set of edge sites whose records form together,
as one event -- and computes what follows. Five unit types are declared:

  U1  a single edge site                                   12 units, size 1
  U2  the three edges at one corner v, star(v)              8 units, size 3
      -- a corner's own record set
  U3  the four edges of one face                            6 units, size 4
  U4  the closed corner star of v: every edge incident to    8 units, size 9
      {v} u N(v), which on this cube is E \\ star(7 - v)
  U5  all twelve edge sites at once                          1 unit, size 12

A tick is: (i) take the next unit in a DECLARED order; (ii) the not-yet-recorded
sites of that unit register JOINTLY, as one event, with the Born odds of the
current pre-record object on the 2^m joint outcome patterns of those m sites;
(iii) between events apply one of three DECLARED rules --

  (a) M_R  relax to the ground state of H restricted to the record-consistent
           subspace, with the normalized projector Pi/deg where that ground
           space is degenerate (PR #7895's tick);
  (b) A    the unitary exp(-i tau H_R), tau = 0.5 (PR #7876's Model A);
  (c) L    nothing at all -- pure sequential Born, the control.

Declared conventions: a unit with no unrecorded sites is SKIPPED (no formation
event and no between-event rule); the between-event rule after the LAST event is
not applied, since it cannot change the final distribution; records are
permanent, so "together" is read at the level of FORMATION -- a formation event
registers a whole unit's worth of records at once. Sixteen orders are declared
for U1-U4, four per type, written out in ORDERS_U, plus U5's single order; a
further declared lexicographic sweep of the first LEX_N permutations of the unit
list is run for U2, U3 and U4.

The runner establishes:

  A  THE SETTING AND THE SEA'S ZEROS.  The encoding, the pi-flux sector, the sea,
     and PR #7895's census: support 1984 = 62 x 32 and 2112 zeros = 1856 charge
     zeros (N != 4) + 256 cancellation zeros = the 8 closed corner stars x 32.
  B  THE UNITS AND ORDERS, DECLARED IN FULL.  Their counts, sizes, schedules and
     event counts, and what a single unit's own joint Born marginal already
     forbids.
  C  THE CONTROL.  Rule (c) is order-independent and IS the sea, for every unit
     type: joint Z-basis conditioning commutes, so every deviation below is
     caused by the between-event rule and not by the joint conditioning.
  D  THE UNITARY TICK.  Joint formation on a corner's record set keeps all 256
     cancellation zeros at THREE of FOUR declared U2 orders; U2 antipodal loses them, and two schedules
     of disjoint corner sets match the sea to stated tolerances at every tau tested.
  E  THE MECHANISM.  After a corner's record set forms jointly the Born-
     conditioned sea passes the first-unit H_R eigenvector residual test.
     An exact eigenvector would change only by phase; the other tested units fail.
  F  RELAXATION.  Under rule (a) no tested proper-unit schedule keeps more
     than 64 of the 256, and the readable charge stays smeared in these menus.
  G  ORDER DEPENDENCE.  It is positive in every tested proper-unit menu,
     smaller at U4 than U1, and not monotone across the four unit types.

NO SEEDS ANYWHERE. Nothing is sampled: each distribution is a finite floating-point tree product
with branches of relative probability <=1e-12 omitted and their mass reported, and every order used is written out in this file.

Line tags. `[exact]` = integer, F2 or symplectic Pauli arithmetic with no
floating point in the statement. `[numerical, tol]` = a deterministic
double-precision evaluation of an exactly specified quantity at the stated
threshold, with no sampling and no seed.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""
from __future__ import annotations

import itertools
import sys
from functools import reduce


# Mutable scientific prose and live interpretation boundary; no parent campaign import.
from pathlib import Path
import hashlib
AUDIT_INPUT_PATHS = ('docs/JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
_EXPECTED_INPUT_SHA256 = {'docs/JOINT_FORMATION_ON_A_CORNERS_RECORD_SET_KEEPS_THE_SEAS_ZEROS_UNDER_THE_UNITARY_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md': '37f4d269abebae38a9613037df091b30e7d7c5ae629868587674959120683798', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

def _check_source_inputs():
    root = Path(__file__).resolve().parents[1]
    if set(AUDIT_INPUT_PATHS) != set(_EXPECTED_INPUT_SHA256):
        raise SystemExit("SOURCE_INPUTS: declaration/pin set mismatch")
    for rel in AUDIT_INPUT_PATHS:
        try:
            actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        except OSError as exc:
            raise SystemExit("SOURCE_INPUTS: missing/unreadable " + rel) from exc
        if actual != _EXPECTED_INPUT_SHA256[rel]:
            raise SystemExit("SOURCE_INPUTS: changed " + rel)
    print("SOURCE_INPUTS: exact own-note and current-memo pins verified; physical suppliers remain conditional")

_check_source_inputs()

import numpy as np

AUDIT_TIMEOUT_SEC = 150

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


def HR_apply(Rmask, w, psi):
    """H_R psi on the block. H = i M with M real skew, sector by sector."""
    out = np.zeros(D, dtype=np.complex128)
    for J, M in block_M(Rmask, w):
        out[J] = 1j * (M @ psi[J])
    return out


def tv(p, q):
    return 0.5 * float(np.abs(np.asarray(p) - np.asarray(q)).sum())


# ==========================================================================
# the stipulated formation units, the declared orders, and the joint tree
# ==========================================================================
FULL = D - 1
ZTOL = 1e-12
PTOL = 1e-12
LEX_N = 40  # the declared lexicographic sweep: first LEX_N permutations


def mk(qs):
    m = 0
    for q in qs:
        m |= 1 << q
    return m


def face_edges(cyc):
    return [EN.EIDX[(cyc[t], cyc[(t + 1) % 4])] for t in range(4)]


def cstar_edges(v):
    """Every edge incident to {v} u N(v): the closed corner star of v."""
    S = {v} | set(EN.NBR[v])
    return sorted(q for q in range(NQ) if EN.EDGES[q][0] in S or EN.EDGES[q][1] in S)


UNITS = {
    "U1": [("e%d" % q, 1 << q) for q in range(NQ)],
    "U2": [("corner%d" % v, mk(sorted(EN.STAR[v]))) for v in range(8)],
    "U3": [("face%d" % i, mk(face_edges(FAC[i]))) for i in range(6)],
    "U4": [("cstar%d" % v, mk(cstar_edges(v))) for v in range(8)],
    "U5": [("all12", FULL)],
}

ORDERS_U = {
    "U1": [
        ("identity", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),
        ("reverse", [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]),
        ("byaxis", [2, 4, 6, 7, 0, 3, 8, 11, 1, 5, 9, 10]),
        ("interleave", [0, 6, 1, 7, 2, 8, 3, 9, 4, 10, 5, 11]),
    ],
    "U2": [
        ("identity", [0, 1, 2, 3, 4, 5, 6, 7]),
        ("reverse", [7, 6, 5, 4, 3, 2, 1, 0]),
        ("evenfirst", [0, 3, 5, 6, 1, 2, 4, 7]),
        ("antipodal", [0, 7, 1, 6, 2, 5, 3, 4]),
    ],
    "U3": [
        ("identity", [0, 1, 2, 3, 4, 5]),
        ("reverse", [5, 4, 3, 2, 1, 0]),
        ("oneperaxis", [0, 2, 4, 1, 3, 5]),
        ("mixed", [3, 0, 5, 2, 1, 4]),
    ],
    "U4": [
        ("identity", [0, 1, 2, 3, 4, 5, 6, 7]),
        ("reverse", [7, 6, 5, 4, 3, 2, 1, 0]),
        ("antipodal", [0, 7, 1, 6, 2, 5, 3, 4]),
        ("gray", [0, 1, 3, 2, 6, 7, 5, 4]),
    ],
    "U5": [("identity", [0])],
}
UT4 = ("U1", "U2", "U3", "U4")
ONAME = {ut: [nm for nm, _ in ORDERS_U[ut]] for ut in ORDERS_U}


def schedule(ut, perm):
    """(unit name, newly recorded bits) per actual formation event."""
    sch, R = [], 0
    for i in perm:
        nm, m = UNITS[ut][i]
        nb = m & ~R
        if nb == 0:
            continue
        sch.append((nm, nb))
        R |= nb
        if R == FULL:
            break
    assert R == FULL, "declared order does not cover all 12 sites"
    return sch


SCHED = {(ut, nm): schedule(ut, p) for ut in ORDERS_U for nm, p in ORDERS_U[ut]}


RUN_RECEIPTS = []


def run(sch, mode, tau=0.5, eig=None, visit=None):
    """Finite deterministic tree; PTOL-pruned probability is explicitly accounted."""
    ne = len(sch)
    out = np.zeros(D)
    discarded = [0.0]

    def rec(k, Rmask, w, obj, prob):
        nm, nb = sch[k]
        dg = obj if mode == "MR" else np.abs(obj) ** 2
        grp = np.bincount(ARG & nb, weights=dg, minlength=nb + 1)
        tot = float(grp.sum())
        for val in np.flatnonzero(grp > 0.0):
            pb = float(grp[val]) / tot
            if pb <= PTOL:
                discarded[0] += prob * pb
                continue
            R2 = Rmask | nb
            w2 = w | int(val)
            if k + 1 == ne:
                out[w2] += prob * pb
                continue
            if mode == "MR":
                E0, deg, J2, v2 = relax(R2, w2)
                nx = np.zeros(D)
                nx[J2] = v2
            else:
                nx = obj.copy()
                nx[(ARG & nb) != val] = 0.0
                nx /= np.linalg.norm(nx)
                if visit is not None:
                    visit[np.abs(nx) > 1e-11] = True
                if eig is not None:
                    r = HR_apply(R2, w2, nx)
                    lam = float(np.vdot(nx, r).real)
                    e = float(np.max(np.abs(r - lam * nx))) < 1e-9
                    a = eig.setdefault(k + 1, [0.0, 0.0])
                    a[0] += prob * pb * (1.0 if e else 0.0)
                    a[1] += prob * pb
                if mode == "A":
                    nx = evolve_HR(R2, w2, nx, tau)
                    if visit is not None:
                        visit[np.abs(nx) > 1e-11] = True
            rec(k + 1, R2, w2, nx, prob * pb)

    st = P_SEA.copy() if mode == "MR" else SEA.copy()
    if visit is not None:
        visit[np.abs(st) > 1e-11] = True
    rec(0, 0, 0, st, 1.0)
    RUN_RECEIPTS.append((tuple(sch), mode, float(tau), float(out.sum()), discarded[0]))
    return out


# ------------------------------------------------- the sea's zeros, by class
SEAZ = P_SEA <= ZTOL
CHG0 = SEAZ & (NVAL != 4)
CAN0 = SEAZ & (NVAL == 4)
SEASUP = ~SEAZ
CSTAR_PAT = []
for v in range(8):
    p = [0] * 8
    p[v] = 1
    for u in EN.NBR[v]:
        p[u] = 1
    CSTAR_PAT.append(tuple(p))
RECT = [tuple(int(x) for x in RECZ[z]) for z in range(D)]
CANCEL_OF = -np.ones(D, dtype=np.int64)
for z in range(D):
    if CAN0[z]:
        CANCEL_OF[z] = CSTAR_PAT.index(RECT[z])
CANC_PATS = {RECT[z] for z in np.flatnonzero(CAN0)}
SUPP_PATS = {RECT[z] for z in np.flatnonzero(SEASUP)}
N_ZERO = int(SEAZ.sum())
N_CHG = int(CHG0.sum())
N_CAN = int(CAN0.sum())


def kept(p):
    """(cancellation zeros kept, charge zeros kept, support) of a distribution."""
    z = p <= ZTOL
    return int((z & CAN0).sum()), int((z & CHG0).sum()), int((p > ZTOL).sum())


def per_star(p):
    z = p <= ZTOL
    return [int(((CANCEL_OF == v) & z).sum()) for v in range(8)]


def pq0(p):
    return float(p[QVAL == 0].sum())


def varq(p):
    m = float((p * QVAL).sum())
    return float((p * QVAL ** 2).sum()) - m * m


# ==========================================================================
# A -- the setting and the sea's zeros (the census PR #7895 reports)
# ==========================================================================
check(
    "A1 [exact] cube 2x2x2, 8 corners / 12 edge sites / 6 faces: R0-R4 pair by pair, no -I in the face group, k = %d, code dim "
    "2^12/2^%d = %d; each hop term has X-part exactly one edge qubit, so P_S H P_S is the sum of the hops on UNRECORDED "
    "sites -- H_R" % (AUD["k"], AUD["k"], AUD["code_dim"]),
    AUD["R0"] and AUD["R1"] and AUD["R2"] and AUD["R3"] and AUD["R4"] and AUD["grp_ok"]
    and AUD["k"] == 5 and AUD["code_dim"] == 128 and D == 4096 and NQ == 12 and HOPX_OK,
)
check(
    "A2 [exact] the Kawamoto-Smit signs put flux %s on all six faces -- the pi-flux sector -- and H = -sum_e eta_e T_e is "
    "Hermitian on the 4096-dimensional record space" % (set(FACE_FLUX),),
    all(f == -1 for f in FACE_FLUX) and HERM_OK,
)
check(
    "A3 [numerical, 1e-11] the code space (six S_f = +1, dim 128 = the even-N space) is H-invariant to %.1e; the sea has "
    "E = %.12f = -4 sqrt 3, deg 1, gap %.12f = 2 sqrt 3, sharp N = 4 (mass off: %.1e)"
    % (CODE_INV, E_SEA, SEA_GAP, SEA_OFF_N4),
    WORTH < 1e-12 and CODE_INV < 1e-11 and abs(E_SEA + 4 * SQ3) < 1e-11
    and SEA_DEG == 1 and abs(SEA_GAP - 2 * SQ3) < 1e-11 and SEA_OFF_N4 < 1e-25,
)
check(
    "A4 [exact, 1e-12 zero read] the target, the sea's registration: support %d = 62 x 32, %d zeros = %d charge (N != 4) + %d "
    "cancellation, whose 8 corner patterns are EXACTLY the 8 closed corner stars {v} u N(v), 32 each (min nonzero sea "
    "probability %.2e)" % (D - N_ZERO, N_ZERO, N_CHG, N_CAN, float(P_SEA[SEASUP].min())),
    (D - N_ZERO) == 1984 and len(SUPP_PATS) == 62 and N_ZERO == 2112 and N_CHG == 1856 and N_CAN == 256
    and CANC_PATS == set(CSTAR_PAT) and len(CSTAR_PAT) == 8
    and all(int((CANCEL_OF == v).sum()) == 32 for v in range(8)),
)

# ==========================================================================
# B -- the units and the declared orders
# ==========================================================================
SIZES = {ut: sorted({bin(m).count("1") for _, m in UNITS[ut]}) for ut in UNITS}
CSTAR_COMPL = all(
    UNITS["U4"][v][1] == FULL ^ UNITS["U2"][7 - v][1] for v in range(8)
)
EV = {ut: [len(SCHED[(ut, nm)]) for nm in ONAME[ut]] for ut in UNITS}
MEANEV = {ut: sum(EV[ut]) / len(EV[ut]) for ut in UNITS}
NORD = sum(len(ORDERS_U[ut]) for ut in UT4)

check(
    "B1 [exact] the five stipulated units: U1 %d edge sites (size 1), U2 %d corner record sets star(v) (3), U3 %d faces (4), "
    "U4 %d closed corner stars (9), U5 the one 12-site unit; cstar(v) = E \\ star(7 - v)" % (len(UNITS["U1"]), len(UNITS["U2"]), len(UNITS["U3"]), len(UNITS["U4"])),
    [SIZES[u] for u in ("U1", "U2", "U3", "U4", "U5")] == [[1], [3], [4], [9], [12]]
    and [len(UNITS[u]) for u in ("U1", "U2", "U3", "U4", "U5")] == [12, 8, 6, 8, 1]
    and CSTAR_COMPL,
)
check(
    "B2 [exact] the %d declared orders for U1-U4 (four per type, written out; no seed) plus U5's cover all 12 sites; events "
    "U1 %s, U2 %s, U3 %s, U4 %s, U5 %s -- means %.2f, %.2f, %.2f, %.2f, %.2f"
    % (NORD, EV["U1"], EV["U2"], EV["U3"], EV["U4"], EV["U5"],
       MEANEV["U1"], MEANEV["U2"], MEANEV["U3"], MEANEV["U4"], MEANEV["U5"]),
    NORD == 16
    and all(sorted(p) == list(range(len(UNITS[ut]))) for ut in ORDERS_U for _, p in ORDERS_U[ut])
    and EV["U1"] == [12, 12, 12, 12] and EV["U2"] == [7, 7, 4, 6]
    and EV["U3"] == [4, 4, 5, 5] and EV["U4"] == [3, 3, 2, 3] and EV["U5"] == [1]
    and abs(MEANEV["U2"] - 6.0) < 1e-12 and abs(MEANEV["U3"] - 4.5) < 1e-12
    and abs(MEANEV["U4"] - 2.75) < 1e-12,
)

MARG = {}
for ut in UNITS:
    rows = []
    for nm, m in UNITS[ut]:
        g = np.bincount(ARG & m, weights=P_SEA, minlength=m + 1)
        alive = g > 1e-14
        blocked = ~alive[ARG & m]
        rows.append((int((blocked & CHG0).sum()), int((blocked & CAN0).sum())))
    MARG[ut] = rows

check(
    "B3 [numerical, 1e-12] what ONE unit's own joint Born marginal forbids: 0 charge and 0 cancellation at every U1, U2 and "
    "U3 unit -- an edge, a corner record set and a face each see none of the sea's zeros -- while every U4 closed star "
    "forbids %d + %d, and U5 all %d + %d"
    % (MARG["U4"][0][0], MARG["U4"][0][1], MARG["U5"][0][0], MARG["U5"][0][1]),
    all(r == (0, 0) for ut in ("U1", "U2", "U3") for r in MARG[ut])
    and all(r == (448, 64) for r in MARG["U4"])
    and MARG["U5"] == [(1856, 256)],
)

# ==========================================================================
# C -- the control: rule (c), pure sequential Born
# ==========================================================================
P_L = {(ut, nm): run(SCHED[(ut, nm)], "L") for ut in UNITS for nm in ONAME[ut]}
tvL = {k: tv(p, P_SEA) for k, p in P_L.items()}
suppL = {k: int((p > ZTOL).sum()) for k, p in P_L.items()}
ordL = {ut: max(tv(P_L[(ut, a)], P_L[(ut, b)]) for a in ONAME[ut] for b in ONAME[ut]) for ut in UT4}

check(
    "C1 [numerical, 1e-15] THE CONTROL: with no between-event rule, all %d declared schedules give support %d and ARE the "
    "sea's registration -- TV to the sea at most %.1e" % (len(P_L), 1984, max(tvL.values())),
    all(s == 1984 for s in suppL.values()) and max(tvL.values()) < 1e-15,
)
check(
    "C2 [numerical, 1e-15] and order-independent for every unit type -- max pairwise TV %.0e (U1), %.0e (U2), %.0e (U3), "
    "%.0e (U4): joint Z-basis conditioning commutes, so what follows is the between-event rule, not the conditioning" % (ordL["U1"], ordL["U2"], ordL["U3"], ordL["U4"]),
    max(ordL.values()) < 1e-15,
)

# ==========================================================================
# D -- the unitary tick (rule (b), Model A at tau = 0.5)
# ==========================================================================
TAU = 0.5
P_A = {(ut, nm): run(SCHED[(ut, nm)], "A", TAU) for ut in UNITS for nm in ONAME[ut]}
KA = {k: kept(p) for k, p in P_A.items()}
tvA = {k: tv(p, P_SEA) for k, p in P_A.items()}

check(
    "D1 [numerical, 1e-12] site-wise formation (U1) under the unitary tick: support %d, all %d charge zeros kept, %d of the "
    "256 cancellation zeros kept, TV to the sea %.12f at the identity order"
    % (KA[("U1", "identity")][2], KA[("U1", "identity")][1], KA[("U1", "identity")][0], tvA[("U1", "identity")]),
    KA[("U1", "identity")] == (0, 1856, 2240) and abs(tvA[("U1", "identity")] - 0.324925160534) < 1e-9
    and all(KA[("U1", nm)] == (0, 1856, 2240) for nm in ONAME["U1"]),
)
canA = {ut: [KA[(ut, nm)][0] for nm in ONAME[ut]] for ut in UNITS}
check(
    "D2 [numerical, 1e-12] joint formation on a corner's record set flips it: cancellation zeros kept over the four declared "
    "orders are U1 %s, U2 %s, U3 %s, U4 %s, U5 %s -- all 256 at 3 of 4 corner orders, none at any face order; charge "
    "zeros kept everywhere" % (canA["U1"], canA["U2"], canA["U3"], canA["U4"], canA["U5"]),
    canA["U1"] == [0, 0, 0, 0] and sorted(canA["U2"]) == [0, 256, 256, 256]
    and canA["U3"] == [0, 0, 0, 0] and sorted(canA["U4"]) == [128, 128, 128, 256]
    and canA["U5"] == [256] and all(v[1] == 1856 for v in KA.values()),
)
check(
    "D3 [numerical, 1e-12] and two schedules match the sea to the stated numerical tolerance: U2 evenfirst, the four disjoint corner sets star(0), "
    "star(3), star(5), star(6), at TV %.2e; U4 antipodal, cstar(0) then star(7), at TV %.2e; both on support %d" % (tvA[("U2", "evenfirst")], tvA[("U4", "antipodal")], KA[("U2", "evenfirst")][2]),
    tvA[("U2", "evenfirst")] < 1e-14 and tvA[("U4", "antipodal")] < 1e-14
    and KA[("U2", "evenfirst")] == (256, 1856, 1984) and KA[("U4", "antipodal")] == (256, 1856, 1984),
)
TAUS = (0.1, 0.5, 1.234567, 2.0)
tau_rows = {}
for ut, nm in (("U2", "evenfirst"), ("U4", "antipodal"), ("U1", "identity"), ("U3", "identity")):
    tau_rows[(ut, nm)] = [
        (tv(run(SCHED[(ut, nm)], "A", t), P_SEA), kept(run(SCHED[(ut, nm)], "A", t))[0]) for t in TAUS
    ]
check(
    "D4 [numerical, 1e-12] at every tau tested, %s: both stay at TV < 1e-14 with all 256 cancellation zeros, while U1 and U3 "
    "identity keep 0 of the 256 at every one of them" % (TAUS,),
    all(r[0] < 1e-14 and r[1] == 256 for k in (("U2", "evenfirst"), ("U4", "antipodal")) for r in tau_rows[k])
    and all(r[1] == 0 for k in (("U1", "identity"), ("U3", "identity")) for r in tau_rows[k]),
)

LEX = {ut: [list(p) for p in itertools.islice(itertools.permutations(range(len(UNITS[ut]))), LEX_N)]
       for ut in ("U2", "U3", "U4")}
lex_can = {}
lex_executed = []
for ut in ("U2", "U3", "U4"):
    for mode in ("A", "MR"):
        lex_can[(ut, mode)] = []
        for p in LEX[ut]:
            lex_executed.append((ut,mode,tuple(p)))
            lex_can[(ut, mode)].append(kept(run(schedule(ut,p),mode,TAU))[0])
lex_full = {k: sum(1 for c in v if c == 256) for k, v in lex_can.items()}

check(
    "D5 [numerical, 1e-12] a declared lexicographic sweep, the first %d permutations of each unit list (no seed): under the "
    "unitary tick %d of %d U2 orders keep all 256, U3 keeps 0 .. %d, U4 %d .. %d; under relaxation none over 64" % (LEX_N, lex_full[("U2", "A")], LEX_N, max(lex_can[("U3", "A")]),
       min(lex_can[("U4", "A")]), max(lex_can[("U4", "A")])),
    LEX_N == 40 and len(lex_executed) == 240 and len(set(lex_executed)) == 240
    and set(lex_executed) == {(ut,mode,p) for ut in ("U2","U3","U4")
        for mode in ("A","MR") for p in sorted(itertools.permutations(range(len(UNITS[ut]))))[:40]}
    and lex_full[("U2", "A")] == 4 and lex_full[("U3", "A")] == 0
    and set(lex_can[("U4","A")]) == {128}
    and all(len(v)==40 for v in lex_can.values())
    and max(lex_can[("U3", "A")]) == 0
    and all(max(lex_can[(ut, "MR")]) <= 64 for ut in ("U2", "U3", "U4")),
)

# ==========================================================================
# E -- the mechanism
# ==========================================================================
def first_unit_report(ut):
    """G, F, Fq, TV(|psi|^2, Pi/deg) and the eigenvector count after the first unit."""
    nm, nb = SCHED[(ut, "identity")][0]
    g = np.bincount(ARG & nb, weights=P_SEA, minlength=nb + 1)
    tot = float(g.sum())
    G = F = Fq = TVd = 0.0
    degs, ne, nt = [], 0, 0
    for val in np.flatnonzero(g > 1e-14):
        pb = float(g[val]) / tot
        sel = (ARG & nb) == val
        psi = SEA.copy()
        psi[~sel] = 0.0
        psi /= np.linalg.norm(psi)
        nt += 1
        if nb == FULL:
            G += pb
            F += pb
            Fq += pb
            degs.append(1)
            ne += 1
            continue
        E0, deg, secs = relax_full(nb, int(val))
        _, _, J2, v2 = relax(nb, int(val))
        dg = np.zeros(D)
        dg[J2] = v2
        fq = fidelity(secs, E0, deg, psi)
        degs.append(deg)
        G += pb * fq * deg
        Fq += pb * fq
        qq = np.abs(psi) ** 2
        F += pb * float(np.sum(np.sqrt(qq * dg))) ** 2
        TVd += pb * 0.5 * float(np.abs(qq - dg).sum())
        r = HR_apply(nb, int(val), psi)
        lam = float(np.vdot(psi, r).real)
        if float(np.max(np.abs(r - lam * psi))) < 1e-9:
            ne += 1
    return nm, G, F, Fq, TVd, (min(degs), max(degs)), ne, nt


FU = {ut: first_unit_report(ut) for ut in ("U1", "U2", "U3", "U4")}

check(
    "E1 [numerical, 1e-9] THE MECHANISM. After a corner's record set forms jointly the Born-conditioned sea lies in the "
    "restricted ground space (G = %.9f, deg %d), an H_R eigenvector residual test passed at %d of %d outcomes, TV(|psi|^2, Pi/deg) = %.9f: "
    "relaxation is the IDENTITY there, the unitary a global phase"
    % (FU["U2"][1], FU["U2"][5][1], FU["U2"][6], FU["U2"][7], FU["U2"][4]),
    abs(FU["U2"][1] - 1.0) < 1e-9 and FU["U2"][5] == (1, 1) and FU["U2"][6] == 8 and FU["U2"][7] == 8
    and FU["U2"][4] < 1e-9,
)
check(
    "E2 [numerical, 1e-9] the closed corner star too, G = %.9f at %d/%d, but its ground space is %d-fold degenerate, so "
    "Pi/deg gives a rank-2 mixture (F = %.9f, Fq = %.3f); an edge (%.9f, %d/%d) and a FACE (%.9f, %d/%d) are not "
    "eigenvectors, though the face is larger"
    % (FU["U4"][1], FU["U4"][6], FU["U4"][7], FU["U4"][5][1], FU["U4"][2], FU["U4"][3],
       FU["U1"][1], FU["U1"][6], FU["U1"][7], FU["U3"][1], FU["U3"][6], FU["U3"][7]),
    abs(FU["U4"][1] - 1.0) < 1e-9 and FU["U4"][6] == 448 and FU["U4"][7] == 448 and FU["U4"][5] == (2, 2)
    and abs(FU["U4"][2] - 0.636894534) < 1e-8 and abs(FU["U4"][3] - 0.5) < 1e-9
    and FU["U1"][6] == 0 and FU["U1"][7] == 2 and abs(FU["U1"][1] - 0.962606705806) < 1e-8
    and FU["U3"][6] == 0 and FU["U3"][7] == 16 and abs(FU["U3"][1] - 0.890431430) < 1e-8,
)

EIG = {}
for ut, nm in (("U2", "evenfirst"), ("U4", "antipodal"), ("U1", "identity"), ("U3", "identity")):
    d = {}
    run(SCHED[(ut, nm)], "A", TAU, eig=d)
    EIG[(ut, nm)] = [d[k][0] / d[k][1] for k in sorted(d)]

check(
    "E3 [numerical, 1e-9] along both exact-sea schedules the conditioned state passes the H_R eigenvector residual test at every retained node a "
    "between-event step follows: eigen-weight %s and %s, against %s (U1 identity, first seven) and %s (U3 identity)"
    % ("/".join("%.3f" % x for x in EIG[("U2", "evenfirst")]), "/".join("%.3f" % x for x in EIG[("U4", "antipodal")]),
       "/".join("%.3f" % x for x in EIG[("U1", "identity")][:7]),
       "/".join("%.3f" % x for x in EIG[("U3", "identity")])),
    all(abs(x - 1.0) < 1e-9 for x in EIG[("U2", "evenfirst")])
    and all(abs(x - 1.0) < 1e-9 for x in EIG[("U4", "antipodal")])
    and all(x < 1e-9 for x in EIG[("U1", "identity")][:7])
    and EIG[("U3", "identity")][0] < 1e-9,
)

LEAK = {}
for ut, nm in (("U1", "identity"), ("U2", "identity"), ("U2", "evenfirst"), ("U4", "antipodal")):
    vis = np.zeros(D, dtype=bool)
    run(SCHED[(ut, nm)], "A", TAU, visit=vis)
    LEAK[(ut, nm)] = (int(vis.sum()), int((vis & ~SEASUP & (NVAL != 4)).sum()), int((vis & CAN0).sum()))

check(
    "E4 [numerical, 1e-11] OPEN, not claimed: the rule-(b) node-support union never leaves N = 4 (%s outside) and, for the "
    "two exact-sea schedules, never leaves the sea's 1984 labels (unions %d, %d); yet U2 identity visits %d "
    "cancellation-coset labels en route and still finishes with all 256 zeros -- observed, not explained"
    % ({LEAK[k][1] for k in LEAK}, LEAK[("U2", "evenfirst")][0], LEAK[("U4", "antipodal")][0],
       LEAK[("U2", "identity")][2]),
    all(LEAK[k][1] == 0 for k in LEAK)
    and LEAK[("U2", "evenfirst")][0] == 1984 and LEAK[("U4", "antipodal")][0] == 1984
    and LEAK[("U2", "identity")][2] == 192 and LEAK[("U1", "identity")][2] == 256
    and KA[("U2", "identity")][0] == 256,
)

# ==========================================================================
# F -- relaxation (rule (a), M_R with the Pi/deg tie-break)
# ==========================================================================
P_M = {(ut, nm): run(SCHED[(ut, nm)], "MR") for ut in UNITS for nm in ONAME[ut]}
KM = {k: kept(p) for k, p in P_M.items()}
tvM = {k: tv(p, P_SEA) for k, p in P_M.items()}
canM = {ut: [KM[(ut, nm)][0] for nm in ONAME[ut]] for ut in UNITS}
best_prop = max(max(canM[ut]) for ut in UT4)
best_lex = max(max(lex_can[(ut, "MR")]) for ut in ("U2", "U3", "U4"))

check(
    "F1 [numerical, 1e-12] under RELAXATION no tested proper-unit schedule keeps more than %d of the 256: over the 16 "
    "declared orders U1 %s, U2 %s, U3 %s, U4 %s, over the sweep at most %d; U5 keeps all %d zeros"
    % (best_prop, canM["U1"], canM["U2"], canM["U3"], canM["U4"], best_lex,
       KM[("U5", "identity")][0] + KM[("U5", "identity")][1]),
    best_prop == 64 and best_lex <= 64 and canM["U1"] == [0, 0, 0, 0] and canM["U3"] == [0, 0, 0, 0]
    and canM["U4"] == [64, 64, 64, 64] and sorted(canM["U2"]) == [0, 0, 0, 64]
    and KM[("U5", "identity")] == (256, 1856, 1984) and tvM[("U5", "identity")] < 1e-14,
)
u4_first = {nm: int(SCHED[("U4", nm)][0][0][5:]) for nm in ONAME["U4"]}
u4_ok = all(
    sorted(v for v, c in enumerate(per_star(P_M[("U4", nm)])) if c == 32) == sorted([u4_first[nm], 7 - u4_first[nm]])
    for nm in ONAME["U4"]
)
check(
    "F2 [numerical, 1e-12] the 64 that survive under U4 are exactly the FIRST-formed star's coset and its antipode's at all "
    "four declared orders (%s): cstar(v)'s nine edges fix the parities on {v} u N(v), and in the sharp-N = 4 sea both "
    "all-occupied and all-empty are forced to zero; later stars go to the relaxation"
    % (sorted({tuple(sorted([u4_first[nm], 7 - u4_first[nm]])) for nm in ONAME["U4"]}),),
    u4_ok and all(sum(per_star(P_M[("U4", nm)])) == 64 for nm in ONAME["U4"]),
)
u2ef = [v for v, c in enumerate(per_star(P_M[("U2", "evenfirst")])) if c == 32]
check(
    "F3 [numerical, 1e-12] the 'formed first, therefore kept' reading does NOT transfer to the corner unit: under U2 "
    "evenfirst, whose first unit is corner0, the surviving cosets are %s, not 0 -- as B3 requires" % (u2ef,),
    u2ef == [1, 6] and MARG["U2"][0] == (0, 0),
)
pq_prop = {ut: [pq0(P_M[(ut, nm)]) for nm in ONAME[ut]] for ut in UT4}
best_pq = max(max(v) for v in pq_prop.values())
check(
    "F4 [numerical, 1e-12] and the readable charge stays smeared: P(Q = 0) is below 1 in the declared proper-unit cases -- best %.9f at U3, the "
    "4-site face, against U4's %.9f .. %.9f; U5 gives exactly %.9f. Bigger units do not sharpen Q monotonically"
    % (best_pq, min(pq_prop["U4"]), max(pq_prop["U4"]), pq0(P_M[("U5", "identity")])),
    abs(best_pq - 0.841145833333) < 1e-9 and best_pq < 1.0 - 1e-9
    and abs(pq0(P_M[("U5", "identity")]) - 1.0) < 1e-12
    and abs(varq(P_M[("U5", "identity")])) < 1e-12
    and max(pq_prop["U4"]) < max(pq_prop["U3"]),
)

# ==========================================================================
# G -- order dependence
# ==========================================================================
ordM = {ut: max(tv(P_M[(ut, a)], P_M[(ut, b)]) for a in ONAME[ut] for b in ONAME[ut]) for ut in UT4}
ordA = {ut: max(tv(P_A[(ut, a)], P_A[(ut, b)]) for a in ONAME[ut] for b in ONAME[ut]) for ut in UT4}

check(
    "G1 [numerical, 1e-12] order dependence is positive in each tested proper-unit menu and smaller at U4 than U1: max pairwise TV over the "
    "four declared orders, rules (a)/(b), is U1 %.12f/%.12f, U2 %.9f/%.9f, U3 %.9f/%.9f, U4 %.12f/%.12f -- a LOWER BOUND"
    % (ordM["U1"], ordA["U1"], ordM["U2"], ordA["U2"], ordM["U3"], ordA["U3"], ordM["U4"], ordA["U4"]),
    abs(ordM["U1"] - 0.602777777778) < 1e-9 and abs(ordA["U1"] - 0.619386368116) < 1e-9
    and abs(ordM["U4"] - 0.25) < 1e-9 and abs(ordA["U4"] - 0.076616282355) < 1e-9
    and all(ordM[ut] > 0 and ordA[ut] > 0 for ut in UT4),
)
check(
    "G2 [numerical, 1e-12] and not monotone in the unit size: the 4-site face U3 is MORE order-dependent than the 3-site "
    "corner set U2 under both rules (%.9f > %.9f, %.9f > %.9f) -- shape, not size, governs"
    % (ordM["U3"], ordM["U2"], ordA["U3"], ordA["U2"]),
    ordM["U3"] > ordM["U2"] and ordA["U3"] > ordA["U2"],
)

check("G3 [numerical, 1e-10 accounting] %d actual tree runs: max discarded relative-branch mass %.3e, "
      "max |retained+discarded-1| %.3e; omitted leaves are not an exact whole-tree certificate"
      % (len(RUN_RECEIPTS),max(r[4] for r in RUN_RECEIPTS),max(abs(r[3]+r[4]-1) for r in RUN_RECEIPTS)),
      len(RUN_RECEIPTS)>0 and all(np.isfinite(r[3]+r[4]) and r[4]>=0 and abs(r[3]+r[4]-1)<1e-10 for r in RUN_RECEIPTS))
print("TREE_RECEIPTS", RUN_RECEIPTS)
print("SUMMARY: U2 keeps all 256 zeros in three of four declared orders; the two named schedules "
      "match the sea at the four tested dwell times. Exact all-time equality requires the "
      "eigenvector premise at every reachable node. Proper-unit relaxation failures concern "
      "only the declared menus; pruned mass is reported.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
