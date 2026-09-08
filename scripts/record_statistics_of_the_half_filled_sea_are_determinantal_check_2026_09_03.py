#!/usr/bin/env python3
"""Record statistics of the half-filled sea are determinantal.

Class-A finite-cluster runner, self-contained. The vacuum is the half-filled
staggered sea of the designed free-hopping law: one coarse mode per site,
Kawamoto-Smit link signs, half filling, optimal twist on the tori. A record at
a coarse site registers occupancy there; the update clause throughout is
Lueders conditioning on the value a forming record locks, STIPULATED here and
not derived. Writing P for the sea's one-particle projector, the runner
establishes:

  A  DETERMINANTAL.  On the open 2x2x2 cube (8 modes, N = 4) and the open
     2x2x3 block (12 modes, N = 6) the many-body ground state built in the
     Jordan-Wigner Fock sector -- not from a Slater form -- carries
     |<S|psi>|^2 = |det phi_i(s_j)|^2 = det P_S on every pattern, and every
     k-point marginal is det P_S. Exactly, over Q(sqrt3) and Q(sqrt2):
     P = P^2 = P^T, tr P = N, P_vv = 1/2 at every site, sum det P_S = 1, the
     marginal identity holds with 0 mismatches, and the value multiset and the
     zero census are read off.
  B  THE FORBIDDEN PAIRS.  PR #7858's 12 forbidden corner pairs of the plain
     N = 2, E = -4 cube state are determinantal zeros:
     det P_uv = P_uu P_vv - P_uv^2 in {0, 1/16}, reproducing the 16 allowed
     cosets at 1/512 and the 384 cancellation zeros; the rank-4 one-particle union
     projector has no zero pair inclusion minors, and is not the N=2 manifold.
  C  CONDITIONING IS THE SCHUR COMPLEMENT.  Explicit Lueders conditioning of
     the exact state equals the Schur complement of P (P for an occupied
     record, I - P for an empty one), with the joint formula
     P(A occ, B empty) = (-1)^|B| det (P - 1_B)_{A u B}; each conditional
     kernel is an exact projector of rank N - |O|. Edge records push forward
     through the parity dictionary, and the finished set is order-blind.
  D  THE REACH.  On the tori 4^3, 6^3, 8^3 one record in the UNCONDITIONED sea shifts odds by
     exactly 2 P_vu^2. The parity rule applies before conditioning; the power
     fits are finite-grid diagnostics, with no limit or arbitrary-history claim.
  E  ADDITIVITY AND FORCING.  The six neighbours enter additively; a record set
     need not force a value when it covers a row, and can force without covering
     it (explicit exact eleven-site counterexample); records beyond the star
     still shift the odds.

Groups A (exact half) and B are exact: integer matrices, `Fraction`
arithmetic, and exact arithmetic in Q(sqrt3) and Q(sqrt2). Groups C, D, E and
the Fock half of A are finite floating-point computations on integer data,
each reporting its residual against a tolerance declared before the run. Every
line is tagged [exact] or [numerical].

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys
from fractions import Fraction as Fr
from functools import reduce


# Mutable scientific prose and live interpretation boundary; no parent campaign import.
from pathlib import Path
import hashlib
AUDIT_INPUT_PATHS = ('docs/RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
_EXPECTED_INPUT_SHA256 = {'docs/RECORD_STATISTICS_OF_THE_HALF_FILLED_SEA_ARE_DETERMINANTAL_CONDITIONAL_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'fe618bf5815ead9df4195aa8e9e55a8734b01b32340ec52e3f3350cb1d56f25c', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

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

AUDIT_TIMEOUT_SEC = 120

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


# ==================================================== lattices and the sea

EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def eta_ks(v, a):
    """Kawamoto-Smit link sign of the coarse bond (v, v + e_a)."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


def build_open(dims):
    """Open block with KS staggered signs and no wrap."""
    sites = list(itertools.product(*[range(d) for d in dims]))
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((len(sites), len(sites)))
    for v in sites:
        for a in range(3):
            w = tuple(v[i] + EX[a][i] for i in range(3))
            if w not in idx:
                continue
            s = eta_ks(v, a)
            M[idx[w], idx[v]] += s
            M[idx[v], idx[w]] += s
    return M, sites, idx


def build_torus(L, twist):
    """L^3 torus, KS signs, twist[a] = 1 flips the bonds crossing v_a = L-1 -> 0."""
    sites = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((len(sites), len(sites)))
    for v in sites:
        for a in range(3):
            w = tuple((v[i] + EX[a][i]) % L for i in range(3))
            if w == v:
                continue
            s = eta_ks(v, a)
            if twist[a] and v[a] == L - 1:
                s = -s
            M[idx[w], idx[v]] += s
            M[idx[v], idx[w]] += s
    return M, sites, idx


def sea_projector(M, N=None):
    w, U = np.linalg.eigh(M)
    if N is None:
        N = M.shape[0] // 2
    Phi = U[:, :N]
    return Phi @ Phi.T, Phi, w


def fock_H(M, N):
    """Many-body H = sum_ij M_ij c^dag_i c_j in the N-particle JW-ordered sector."""
    V = M.shape[0]
    basis = list(itertools.combinations(range(V), N))
    pos = {s: i for i, s in enumerate(basis)}
    H = np.zeros((len(basis), len(basis)))
    for bi, S in enumerate(basis):
        Sset = set(S)
        for j in S:
            for i in range(V):
                if M[i, j] == 0 or (i != j and i in Sset):
                    continue
                jl = S.index(j)
                sgn = (-1) ** jl
                rest = S[:jl] + S[jl + 1:]
                k = 0
                while k < len(rest) and rest[k] < i:
                    k += 1
                H[pos[rest[:k] + (i,) + rest[k:]], bi] += M[i, j] * sgn * ((-1) ** k)
    return H, basis, pos


def det_minor(K, S):
    if len(S) == 0:
        return 1.0
    ix = np.array(S)
    return float(np.linalg.det(K[np.ix_(ix, ix)]))


def joint_prob(P, A, B):
    """P(all of A occupied, all of B empty) = (-1)^|B| det (P - 1_B)_{A u B}."""
    U = sorted(set(A) | set(B))
    if not U:
        return 1.0
    ix = np.array(U)
    K = P[np.ix_(ix, ix)].copy()
    Bs = set(B)
    for a, u in enumerate(U):
        if u in Bs:
            K[a, a] -= 1.0
    return ((-1) ** len(B)) * float(np.linalg.det(K))


def schur_condition(P, O, E):
    """Conditional kernel on the complement of O u E: Schur complement of P on the
    occupied records, then of the hole kernel I - K on the empty ones."""
    V = P.shape[0]
    rest = [i for i in range(V) if i not in set(O) | set(E)]
    if O:
        Oi = np.array(sorted(O))
        keep = np.array(sorted(set(range(V)) - set(O)))
        A = P[np.ix_(Oi, Oi)]
        K1 = P[np.ix_(keep, keep)] - P[np.ix_(keep, Oi)] @ np.linalg.solve(A, P[np.ix_(Oi, keep)])
        kmap = {v: a for a, v in enumerate(keep)}
    else:
        K1 = P.copy()
        kmap = {v: v for v in range(V)}
    keep2 = np.array([kmap[v] for v in rest])
    if E:
        Ei = np.array([kmap[v] for v in sorted(E)])
        Q = np.eye(K1.shape[0]) - K1
        A = Q[np.ix_(Ei, Ei)]
        Q2 = Q[np.ix_(keep2, keep2)] - Q[np.ix_(keep2, Ei)] @ np.linalg.solve(A, Q[np.ix_(Ei, keep2)])
        K2 = np.eye(len(rest)) - Q2
    else:
        K2 = K1[np.ix_(keep2, keep2)]
    return K2, rest


# ==================================================== exact arithmetic in Q(sqrt d)

class QF:
    """a + b sqrt(d) with a, b rational."""

    __slots__ = ("a", "b", "d")

    def __init__(s, a, b, d):
        s.a = Fr(a)
        s.b = Fr(b)
        s.d = d

    def _c(x, y):
        return y if isinstance(y, QF) else QF(y, 0, x.d)

    def __add__(x, y):
        y = x._c(y)
        return QF(x.a + y.a, x.b + y.b, x.d)

    def __sub__(x, y):
        y = x._c(y)
        return QF(x.a - y.a, x.b - y.b, x.d)

    def __mul__(x, y):
        y = x._c(y)
        return QF(x.a * y.a + x.d * x.b * y.b, x.a * y.b + x.b * y.a, x.d)

    def inv(x):
        n = x.a * x.a - x.d * x.b * x.b
        if n == 0:
            raise ZeroDivisionError
        return QF(x.a / n, -x.b / n, x.d)

    def iszero(x):
        return x.a == 0 and x.b == 0

    def __eq__(x, y):
        y = x._c(y)
        return x.a == y.a and x.b == y.b

    def __hash__(x):
        return hash((x.a, x.b, x.d))

    def __repr__(x):
        if x.b == 0:
            return str(x.a)
        return "%s%s%s*sqrt%d" % (x.a, "+" if x.b > 0 else "-", abs(x.b), x.d)

    def val(x):
        return float(x.a) + float(x.b) * (x.d ** 0.5)


def qzero(d):
    return QF(0, 0, d)


def qone(d):
    return QF(1, 0, d)


def qmatmul(A, B, d):
    n, m, k = len(A), len(B[0]), len(B)
    return [[sum((A[i][t] * B[t][j] for t in range(k)), qzero(d)) for j in range(m)]
            for i in range(n)]


def qdet(Mx, d):
    """Exact Gaussian elimination over Q(sqrt d)."""
    n = len(Mx)
    if n == 0:
        return qone(d)
    A = [row[:] for row in Mx]
    sign = 1
    out = qone(d)
    for c in range(n):
        p = None
        for r in range(c, n):
            if not A[r][c].iszero():
                p = r
                break
        if p is None:
            return qzero(d)
        if p != c:
            A[c], A[p] = A[p], A[c]
            sign = -sign
        piv = A[c][c]
        out = out * piv
        inv = piv.inv()
        for r in range(c + 1, n):
            if A[r][c].iszero():
                continue
            f = A[r][c] * inv
            for cc in range(c, n):
                A[r][cc] = A[r][cc] - f * A[c][cc]
    return out if sign == 1 else QF(-out.a, -out.b, d)


def qeye(n, d):
    return [[qone(d) if i == j else qzero(d) for j in range(n)] for i in range(n)]


def qscal(A, c):
    return [[x * c for x in row] for row in A]


def qadd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


# ==================================================== Pauli algebra and BKSF

def pc(n):
    return bin(n).count("1")


class Pau:
    """i^k prod_q X_q^{x_q} Z_q^{z_q}, X written before Z on every qubit."""

    __slots__ = ("k", "x", "z")

    def __init__(s, k, x, z):
        s.k = k % 4
        s.x = x
        s.z = z

    def __mul__(a, b):
        return Pau(a.k + b.k + 2 * pc(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def neg(s):
        return Pau(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z


PID = Pau(0, 0, 0)
PH = [1 + 0j, 1j, -1 + 0j, -1j]


def pcomm(a, b):
    return (pc(a.x & b.z) + pc(a.z & b.x)) % 2 == 0


def pact(p, y):
    return y ^ p.x, PH[p.k] * ((-1) ** (pc(p.z & y) % 2))


class Enc:
    """Bravyi-Kitaev superfast encoding on the cube graph; qubits on the edge sites."""

    def __init__(self, V, EDGES, FACES):
        self.V = V
        self.EDGES = list(EDGES)
        self.FACES = list(FACES)
        self.NQ = len(EDGES)
        self.DIM = 1 << self.NQ
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = q
            self.EIDX[(j, i)] = q
        self.NBR = {i: sorted(j for (a, b) in self.EDGES
                              for j in ((b,) if a == i else ((a,) if b == i else ())))
                    for i in range(V)}
        self.STAR = {i: [self.EIDX[(i, k)] for k in self.NBR[i]] for i in range(V)}
        self.STARMASK = {i: reduce(lambda a, b: a | (1 << b), self.STAR[i], 0) for i in range(V)}

    def A(self, i, j):
        x = 1 << self.EIDX[(i, j)]
        z = 0
        for k in self.NBR[i]:
            if k != j and k < j:
                z ^= 1 << self.EIDX[(i, k)]
        for l in self.NBR[j]:
            if l != i and l < i:
                z ^= 1 << self.EIDX[(j, l)]
        p = Pau(pc(x & z) % 2, x, z)
        return p if i < j else p.neg()

    def B(self, i):
        return Pau(0, 0, self.STARMASK[i])

    def loop(self, cyc):
        out = PID
        for a in range(len(cyc)):
            out = out * self.A(cyc[a], cyc[(a + 1) % len(cyc)])
        return out

    def record(self, z):
        return tuple(pc(z & self.STARMASK[i]) % 2 for i in range(self.V))


def cube_cluster():
    return 8, sorted((s, s ^ bit) for s in range(8) for bit in (4, 2, 1) if s ^ bit > s)


def cube_faces():
    out = []
    for ax in range(3):
        bits = [4, 2, 1]
        fb = bits[ax]
        ob = [b for b in bits if b != fb]
        for val in (0, fb):
            out.append((val, val | ob[1], val | ob[0] | ob[1], val | ob[0]))
    return out


def stabilizer_group(En):
    """Independent face-loop generators (Gaussian elimination on X-parts) and their group."""
    S = [En.loop(f) for f in En.FACES]
    gens, basis = [], []
    for s in S:
        v = s.x
        for b in basis:
            v = min(v, v ^ b)
        if v != 0:
            basis.append(v)
            basis.sort(reverse=True)
            gens.append(s)
    grp = []
    for m in range(1 << len(gens)):
        p = PID
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        grp.append(p)
    return S, gens, grp


def code_space(En, grp):
    """Cosets of the cycle space; phi[z] is the unit coefficient of |z> in its coset."""
    phi = np.zeros(En.DIM, dtype=complex)
    cid = -np.ones(En.DIM, dtype=np.int64)
    reps = []
    for z0 in range(En.DIM):
        if cid[z0] >= 0:
            continue
        c = len(reps)
        reps.append(z0)
        for g in grp:
            b, a = pact(g, z0)
            cid[b] = c
            phi[b] = a
    recs = [En.record(reps[c]) for c in range(len(reps))]
    return cid, phi, reps, recs


# ==================================================== Bloch machinery

SUB = list(itertools.product((0, 1), repeat=3))
SI = {s: i for i, s in enumerate(SUB)}


def eta_s(s, a):
    if a == 0:
        return 1
    if a == 1:
        return -1 if (s[0] & 1) else 1
    return -1 if ((s[0] + s[1]) & 1) else 1


def bloch_batch(K):
    """K: (..., 3) cell momenta -> (..., 8, 8) Bloch matrix of the KS hopping."""
    sh = K.shape[:-1]
    H = np.zeros(sh + (8, 8), dtype=complex)
    for s in SUB:
        for a in range(3):
            t = list(s)
            t[a] ^= 1
            t = tuple(t)
            ph = np.exp(-1j * K[..., a]) if s[a] == 1 else np.ones(sh, dtype=complex)
            H[..., SI[t], SI[s]] += eta_s(s, a) * ph
            H[..., SI[s], SI[t]] += eta_s(s, a) * np.conj(ph)
    return H


def kernel_field(nc):
    """Finite Fourier-grid kernel P(R)_{s' s} from an nc^3 cell-momentum grid.
    Only 8 x 8 objects are formed per momentum."""
    kk = 2 * np.pi * (np.arange(nc) + 0.5) / nc
    K = np.stack(np.meshgrid(kk, kk, kk, indexing="ij"), axis=-1)
    w, U = np.linalg.eigh(bloch_batch(K))
    Um = U[..., :4]
    Pk = Um @ np.conj(np.swapaxes(Um, -1, -2))
    Pr = np.fft.ifftn(Pk, axes=(0, 1, 2))
    Rg = np.stack(np.meshgrid(*[np.arange(nc)] * 3, indexing="ij"), axis=-1)
    return Pr * np.exp(1j * np.pi * Rg.sum(-1) / nc)[..., None, None], w


# ==================================================== A: the law of records is determinantal

def exact_P_cube(Mq, V, d):
    """M^2 = 3I on the open cube, so P = (I - M/sqrt3)/2 exactly over Q(sqrt3)."""
    M2 = qmatmul(Mq, Mq, d)
    assert all(M2[i][j] == (QF(3, 0, d) if i == j else qzero(d))
               for i in range(V) for j in range(V)), "M^2 != 3I"
    B = qscal(Mq, QF(0, Fr(1, 3), d))            # M / sqrt3
    return qscal(qadd(qeye(V, d), qscal(B, QF(-1, 0, d))), QF(Fr(1, 2), 0, d))


def exact_P_block(Mq, V, d):
    """Spectrum {+-2, +-sqrt2} on the open 2x2x3 block; P = E_{-2} + E_{-sqrt2}
    by spectral idempotents over Q(sqrt2)."""
    M2 = qmatmul(Mq, Mq, d)
    I = qeye(V, d)
    A = qadd(M2, qscal(I, QF(-2, 0, d)))
    Em2 = qscal(qmatmul(A, qadd(Mq, qscal(I, QF(-2, 0, d))), d), QF(Fr(-1, 8), 0, d))
    B = qadd(M2, qscal(I, QF(-4, 0, d)))
    Es2 = qscal(qmatmul(B, qadd(Mq, qscal(I, QF(0, -1, d))), d), QF(0, Fr(1, 8), d))
    return qadd(Em2, Es2)


EXACT = {}


def exact_case(dims, d, builder, N):
    M, _, _ = build_open(dims)
    V = M.shape[0]
    Mi = M.astype(int)
    assert np.max(np.abs(M - Mi)) == 0
    Pq = builder([[QF(int(x), 0, d) for x in row] for row in Mi], V, d)
    PP = qmatmul(Pq, Pq, d)
    proj = all(PP[i][j] == Pq[i][j] and Pq[i][j] == Pq[j][i] for i in range(V) for j in range(V))
    tr = sum((Pq[i][i] for i in range(V)), qzero(d))
    half = all(Pq[i][i] == QF(Fr(1, 2), 0, d) for i in range(V))
    pats = [(S, qdet([[Pq[i][j] for j in S] for i in S], d))
            for S in itertools.combinations(range(V), N)]
    tot = sum((x for _, x in pats), qzero(d))
    zeros = sum(1 for _, x in pats if x.iszero())
    neg = sum(1 for _, x in pats if x.val() < -1e-30)
    marg = {}
    bad = 0
    for k in (1, 2, 3):
        for T in itertools.combinations(range(V), k):
            Ts = set(T)
            lhs = sum((x for S, x in pats if Ts <= set(S)), qzero(d))
            rhs = qdet([[Pq[i][j] for j in T] for i in T], d)
            if not lhs == rhs:
                bad += 1
            marg[T] = rhs
    pairzero = sum(1 for T, x in marg.items() if len(T) == 2 and x.iszero())
    offmax = max(abs(Pq[i][j].val()) for i in range(V) for j in range(V) if i != j)
    mult = {}
    for _, x in pats:
        mult[repr(x)] = mult.get(repr(x), 0) + 1
    EXACT[dims] = dict(P=Pq, pats=pats, proj=proj, tr=tr, half=half, tot=tot, zeros=zeros,
                       neg=neg, bad=bad, mult=mult, pairzero=pairzero, offmax=offmax,
                       V=V, N=N, d=d)
    return EXACT[dims]


def fock_case(dims):
    """The many-body ground state built in the JW Fock sector, not from a Slater form."""
    M, sites, idx = build_open(dims)
    V = M.shape[0]
    N = V // 2
    P, Phi, w = sea_projector(M, N)
    H, basis, pos = fock_H(M, N)
    ev, evec = np.linalg.eigh(H)
    psi = evec[:, 0]
    probs = psi ** 2
    e_slater = e_dpp = 0.0
    for bi, S in enumerate(basis):
        e_slater = max(e_slater, abs(probs[bi] - np.linalg.det(Phi[np.array(S), :]) ** 2))
        e_dpp = max(e_dpp, abs(probs[bi] - det_minor(P, S)))
    e_marg = 0.0
    for k in (1, 2, 3):
        for S in itertools.combinations(range(V), k):
            emp = sum(probs[bi] for bi, T in enumerate(basis) if set(S) <= set(T))
            e_marg = max(e_marg, abs(emp - det_minor(P, S)))
    return dict(M=M, P=P, basis=basis, probs=probs, V=V, N=N, ev=ev, w=w,
                deg=int(np.sum(ev < ev[0] + 1e-9)), e_slater=e_slater, e_dpp=e_dpp,
                e_marg=e_marg, half=float(np.max(np.abs(np.diag(P) - 0.5))),
                idx=idx, sites=sites)


FOCK = {}


def group_A():
    c = exact_case((2, 2, 2), 3, exact_P_cube, 4)
    b = exact_case((2, 2, 3), 2, exact_P_block, 6)
    FOCK[(2, 2, 2)] = fc = fock_case((2, 2, 2))
    FOCK[(2, 2, 3)] = fb = fock_case((2, 2, 3))

    check("A1 [exact] open 2x2x2 cube, KS signs: M^2 = 3I exactly, so P = (I - M/sqrt3)/2 over Q(sqrt3), "
          "with P = P^2 = P^T, tr P = %s = N and P_vv = 1/2 at EVERY site" % c["tr"], c["proj"] and c["tr"] == QF(4, 0, 3) and c["half"])
    check("A2 [exact] cube: sum of det P_S over all 70 patterns = %s, negatives %d, exact zeros %d; value "
          "multiset {1/144 x30, 1/48 x24, 0 x8, 1/36 x6, 1/16 x2}: %s"
          % (c["tot"], c["neg"], c["zeros"],
             c["mult"] == {"1/144": 30, "1/48": 24, "0": 8, "1/36": 6, "1/16": 2}),
          c["tot"] == qone(3) and c["neg"] == 0 and c["zeros"] == 8
          and c["mult"] == {"1/144": 30, "1/48": 24, "0": 8, "1/36": 6, "1/16": 2})
    check("A3 [exact] open 2x2x3 block, spectrum {+-2, +-sqrt2}: P by spectral idempotents over Q(sqrt2), "
          "P = P^2 = P^T, tr P = %s = N, P_vv = 1/2; sum over 924 = %s, negatives %d, zeros %d"
          % (b["tr"], b["tot"], b["neg"], b["zeros"]),
          b["proj"] and b["tr"] == QF(6, 0, 2) and b["half"] and b["tot"] == qone(2)
          and b["neg"] == 0 and b["zeros"] == 120)
    check("A4 [exact] the marginal identity sum_{S contains T} det P_S = det P_T on every 1-, 2-, 3-subset "
          "(8+28+56, 12+66+220): %d + %d mismatches, no minor vanishing for k <= 3"
          % (c["bad"], b["bad"]),
          c["bad"] == 0 and b["bad"] == 0)
    check("A5 [exact] FORBIDDEN PAIRS: det P_uv = 0 for %d pairs on the cube and %d on the block -- one needs "
          "|P_uv| = 1/2 and the largest off-diagonal is %.4f, %.4f"
          % (c["pairzero"], b["pairzero"], c["offmax"], b["offmax"]),
          c["pairzero"] == 0 and b["pairzero"] == 0
          and abs(c["offmax"] - 0.2887) < 5e-5 and abs(b["offmax"] - 0.3018) < 5e-5)
    check("A6 [numerical, 1e-15] the JW Fock ground state (dims 70, 924; degeneracy %d, %d) has "
          "|<S|psi>|^2 = |det phi_i(s_j)|^2 = det P_S on EVERY pattern (%.1e, %.1e) and every marginal "
          "= det P_S (%.1e)"
          % (fc["deg"], fb["deg"], fc["e_slater"], fb["e_slater"],
             max(fc["e_marg"], fb["e_marg"])),
          fc["deg"] == 1 and fb["deg"] == 1 and max(fc["e_slater"], fb["e_slater"]) < 1e-15
          and max(fc["e_dpp"], fb["e_dpp"]) < 1e-15 and max(fc["e_marg"], fb["e_marg"]) < 1e-15)


# ==================================================== B: PR #7858's forbidden pairs

def chi(S, x):
    return (-1) ** pc(S & x)


def rational_kernel(cols):
    """P = Phi Phi^T for Phi's columns the hypercube characters chi_S / sqrt8: exact over Q."""
    return [[sum(Fr(chi(S, u) * chi(S, v), 8) for S in cols) for v in range(8)]
            for u in range(8)]


def group_B():
    Mp = np.zeros((8, 8))
    for s in range(8):
        for b in (1, 2, 4):
            Mp[s, s ^ b] = 1.0
    Hp, basp, _ = fock_H(Mp, 2)
    evp = np.linalg.eigvalsh(Hp)
    deg = int(np.sum(evp < evp[0] + 1e-9))
    check("B1 [numerical, 1e-12] the PLAIN cube of PR #7858 (all-(+1) adjacency): N = 2 ground energy %.6f "
          "with degeneracy %d over the 28 cosets" % (evp[0], deg),
          abs(evp[0] + 4.0) < 1e-12 and deg == 3 and len(basp) == 28)

    zero_sets = []
    census_ok = True
    closed_ok = True
    for Sset in (3, 5, 6):
        P = rational_kernel((7, Sset))
        e = sum(chi(7, x) * Mp[x, y] * chi(7, y) + chi(Sset, x) * Mp[x, y] * chi(Sset, y)
                for x in range(8) for y in range(8)) / 8.0
        cnt = {}
        zs = []
        for u, v in itertools.combinations(range(8), 2):
            dm = P[u][u] * P[v][v] - P[u][v] * P[v][u]
            dm2 = P[u][u] * P[v][v] - P[u][v] ** 2
            if dm != dm2:
                closed_ok = False
            cnt[dm] = cnt.get(dm, 0) + 1
            if dm == 0:
                zs.append((u, v))
        zero_sets.append(zs)
        if cnt != {Fr(0): 12, Fr(1, 16): 16} or abs(e + 4.0) > 1e-12:
            census_ok = False
    xface = all((u >> 2) == (v >> 2) for u, v in zero_sets[0])
    check("B2 [exact] each of the three declared character-basis E = -4 Slaters has det P_uv = P_uu P_vv - P_uv^2 in {0 (12 pairs), 1/16 "
          "(16)}; the (chi_111, chi_011) zeros are the corner pairs sharing an x-face: %s"
          % xface, census_ok and closed_ok and xface and all(len(z) == 12 for z in zero_sets))

    P = rational_kernel((7, 3))
    pats = {S: P[S[0]][S[0]] * P[S[1]][S[1]] - P[S[0]][S[1]] ** 2
            for S in itertools.combinations(range(8), 2)}
    nz = [S for S, x in pats.items() if x != 0]
    V, EDGES = cube_cluster()
    En = Enc(V, EDGES, cube_faces())
    S_loops, gens, grp = stabilizer_group(En)
    k = len(gens)
    cid, phi, reps, recs = code_space(En, grp)
    fib = 1 << k
    even = {r for r in itertools.product((0, 1), repeat=8) if sum(r) % 2 == 0}
    inj = len(set(recs)) == len(reps) and set(recs) == even
    sup = len(nz) * fib
    canc = (len(pats) - len(nz)) * fib
    unif = {x / fib for x in pats.values() if x != 0}
    check("B3 [exact] through the parity dictionary (%d cosets, fibre %d, a bijection onto the even "
          "patterns: %s): the %d nonzero patterns give support %d at %s, the 12 zeros %d cancellation "
          "zeros"
          % (len(reps), fib, inj, len(nz), sup, sorted(str(x) for x in unif)[0], canc),
          inj and len(reps) == 128 and fib == 32 and len(nz) == 16 and sup == 512
          and canc == 384 and unif == {Fr(1, 512)})

    Pm = rational_kernel((7, 3, 5, 6))
    mins = [Pm[u][u] * Pm[v][v] - Pm[u][v] ** 2 for u, v in itertools.combinations(range(8), 2)]
    check("B4 [exact] the rank-4 one-particle union projector (filled N=4, E=-6) has %d vanishing pair minors of 28 (smallest %s): "
          "its pair inclusion minors sum to 6, not an N=2 probability law"
          % (sum(1 for x in mins if x == 0), min(mins)),
          sum(1 for x in mins if x == 0) == 0 and min(mins) == Fr(3, 16))

    # F2: the actual rank-three N=2 eigenspace and a different Slater in it.
    pairs=list(itertools.combinations(range(8),2))
    amps=[[Fr(chi(7,u)*chi(c,v)-chi(7,v)*chi(c,u),8) for c in (3,5,6)] for u,v in pairs]
    gram=[[sum(row[i]*row[j] for row in amps) for j in range(3)] for i in range(3)]
    manifold=[[sum(amps[i][c]*amps[j][c] for c in range(3)) for j in range(28)] for i in range(28)]
    weights=[manifold[i][i]/3 for i in range(28)]
    same_basis=list(basp)==pairs
    full_projector_ok=same_basis and all(
        sum(manifold[i][k]*manifold[k][j] for k in range(28))==manifold[i][j]
        for i in range(28) for j in range(28))
    full_projector_ok &= same_basis and all(
        sum(int(Hp[i,k])*manifold[k][j] for k in range(28))==-4*manifold[i][j]
        for i in range(28) for j in range(28))
    check("B5 [exact] normalized rank-3 N=2 E=-4 ground-manifold mixture: full pair weights "
          "sum to 1 and take values %s; the old rank-4 inclusion minors instead sum to %s"
          % (sorted(str(x) for x in set(weights)),sum(mins)),
          full_projector_ok and gram==[[Fr(int(i==j)) for j in range(3)] for i in range(3)]
          and sum(weights)==1 and set(weights)=={Fr(1,48),Fr(1,24),Fr(1,16)}
          and sum(mins)==6)
    phi=[chi(3,u)+2*chi(5,u)+4*chi(6,u) for u in range(8)]
    generic=[Fr((chi(7,u)*phi[v]-chi(7,v)*phi[u])**2,64*21) for u,v in pairs]
    # The unchanged plain-cube one-particle matrix acts as -3 on chi7 and -1 on phi.
    eigok=all(sum(int(Mp[u,v])*phi[v] for v in range(8))==-phi[u] for u in range(8))
    eigok &= all(sum(int(Mp[u,v])*chi(7,v) for v in range(8))==-3*chi(7,u) for u in range(8))
    check("B6 [exact] the normalized Slater (chi7, (chi3+2chi5+4chi6)/sqrt21) "
          "also has N=2 and E=-4 but has ZERO forbidden pairs; minimum probability %s" % min(generic),
          eigok and sum(generic)==1 and min(generic)>0)


# ==================================================== C: conditioning is the Schur complement

def conditioning_case(dims, nrecs):
    """Explicit Lueders conditioning of the exact state against the Schur complement of P."""
    F = FOCK[dims]
    P, basis, probs, V, N = F["P"], F["basis"], F["probs"], F["V"], F["N"]
    out = {}
    for nrec in nrecs:
        nbad = nbadd = ncase = 0
        worst = worstd = worstj = 0.0
        projdev = 0.0
        lo, hi = 1.0, 0.0
        nconds = 0
        for R in itertools.combinations(range(V), nrec):
            for vals in itertools.product((0, 1), repeat=nrec):
                cond = dict(zip(R, vals))
                O = [v for v, b in cond.items() if b == 1]
                E = [v for v, b in cond.items() if b == 0]
                nconds += 1
                keep = [bi for bi, S in enumerate(basis)
                        if all(((v in set(S)) == bool(b)) for v, b in cond.items())]
                tot = float(sum(probs[bi] for bi in keep))
                pj = joint_prob(P, O, E)
                worstj = max(worstj, abs(tot - pj))
                if tot < 1e-14:
                    continue
                odds = np.zeros(V)
                for bi in keep:
                    for v in basis[bi]:
                        odds[v] += probs[bi]
                odds /= tot
                K2, rest = schur_condition(P, O, E)
                projdev = max(projdev, float(np.max(np.abs(K2 @ K2 - K2))),
                              abs(float(np.trace(K2)) - (N - len(O))))
                for a, v in enumerate(rest):
                    ncase += 1
                    d1 = abs(odds[v] - K2[a, a])
                    worst = max(worst, d1)
                    nbad += d1 > 1e-12
                    d2 = abs(odds[v] - joint_prob(P, O + [v], E) / pj)
                    worstd = max(worstd, d2)
                    nbadd += d2 > 1e-12
                    lo, hi = min(lo, odds[v]), max(hi, odds[v])
        out[nrec] = dict(nconds=nconds, ncase=ncase, nbad=nbad, nbadd=nbadd, worst=worst,
                         worstd=worstd, worstj=worstj, projdev=projdev, lo=lo, hi=hi)
    return out


def group_C():
    cu = conditioning_case((2, 2, 2), (1, 2))
    bl = conditioning_case((2, 2, 3), (1, 2))
    check("C1 [numerical, 1e-12 odds/1e-10 determinant] cube: over %d one- and %d two-record conditions Lueders conditioning = the "
          "Schur complement of P on %d + %d odds, %d mismatches (%.1e); [1/3, 2/3], [1/6, 5/6]"
          % (cu[1]["nconds"], cu[2]["nconds"], cu[1]["ncase"], cu[2]["ncase"],
             cu[1]["nbad"] + cu[2]["nbad"], max(cu[1]["worst"], cu[2]["worst"])),
          cu[1]["nconds"] == 16 and cu[2]["nconds"] == 112 and cu[1]["ncase"] == 112
          and cu[2]["ncase"] == 672 and cu[1]["nbad"] + cu[2]["nbad"] == 0
          and abs(cu[1]["lo"] - 1 / 3) < 1e-12 and abs(cu[1]["hi"] - 2 / 3) < 1e-12
          and abs(cu[2]["lo"] - 1 / 6) < 1e-12 and abs(cu[2]["hi"] - 5 / 6) < 1e-12)
    check("C2 [numerical, 1e-12 odds/1e-10 determinant] block: the same over %d and %d conditions, %d mismatches (%.1e); odds "
          "ranges [%.4f, %.4f] and [%.4f, %.4f]"
          % (bl[1]["nconds"], bl[2]["nconds"], bl[1]["nbad"] + bl[2]["nbad"],
             max(bl[1]["worst"], bl[2]["worst"]), bl[1]["lo"], bl[1]["hi"], bl[2]["lo"], bl[2]["hi"]),
          bl[1]["nconds"] == 24 and bl[2]["nconds"] == 264 and bl[1]["nbad"] + bl[2]["nbad"] == 0
          and abs(bl[1]["lo"] - 0.3179) < 5e-5 and abs(bl[1]["hi"] - 0.6821) < 5e-5
          and abs(bl[2]["lo"] - 0.1357) < 5e-5 and abs(bl[2]["hi"] - 0.8643) < 5e-5)
    wj = max(cu[1]["worstj"], cu[2]["worstj"], bl[1]["worstj"], bl[2]["worstj"])
    wd = max(cu[1]["worstd"], cu[2]["worstd"], bl[1]["worstd"], bl[2]["worstd"])
    pd = max(cu[1]["projdev"], cu[2]["projdev"], bl[1]["projdev"], bl[2]["projdev"])
    check("C3 [numerical, 1e-14 joint/odds, 1e-10 projector] on every case P(A occ, B empty) = (-1)^|B| det (P - 1_B)_{A u B} (%.1e), "
          "the odds are P(A + v, B)/P(A, B) (%.1e), each kernel an exact projector of rank N - |O| (%.1e)"
          % (wj, wd, pd),
          wj < 1e-14 and wd < 1e-14 and pd < 1e-10)


def group_C_edges():
    """The vertex-level determinantal law pushed to the edge sites of the BKSF cube."""
    M, sites, idx = build_open((2, 2, 2))
    Psea, _, _ = sea_projector(M, 4)
    assert all(idx[v] == 4 * v[0] + 2 * v[1] + v[2] for v in sites)
    pat = {tuple(1 if v in S else 0 for v in range(8)): det_minor(Psea, S)
           for S in itertools.combinations(range(8), 4)}
    V, EDGES = cube_cluster()
    En = Enc(V, EDGES, cube_faces())
    S_loops, gens, grp = stabilizer_group(En)
    k = len(gens)
    cid, phi, reps, recs = code_space(En, grp)
    rec_of = {c: recs[c] for c in range(len(reps))}
    rng = np.random.default_rng(11)
    phase = {c: np.exp(2j * np.pi * rng.random()) for c in range(len(reps))}
    amp = np.zeros(En.DIM, dtype=complex)
    for z in range(En.DIM):
        c = cid[z]
        amp[z] = np.sqrt(max(pat.get(rec_of[c], 0.0), 0.0) / (1 << k)) * phi[z] * phase[c]
    q = np.abs(amp) ** 2
    dev = 0.0
    for c in range(len(reps)):
        mem = [z for z in range(En.DIM) if cid[z] == c]
        vals = q[mem]
        dev = max(dev, vals.max() - vals.min(), abs(vals.sum() - pat.get(rec_of[c], 0.0)))

    def vodds(cond):
        keep = [z for z in range(En.DIM) if all(((z >> e) & 1) == b for e, b in cond.items())]
        m = float(q[keep].sum())
        if m < 1e-14:
            return 0.0, None
        o = np.zeros(8)
        for z in keep:
            r = rec_of[cid[z]]
            for v in range(8):
                if r[v]:
                    o[v] += q[z]
        return m, o / m
    base = vodds({})[1]
    w1 = w2 = 0.0
    n1 = n2 = 0
    for e in range(En.NQ):
        for b in (0, 1):
            m, o = vodds({e: b})
            n1 += 1
            w1 = max(w1, abs(m - 0.5), float(np.max(np.abs(o - base))))
    for e, f in itertools.combinations(range(En.NQ), 2):
        for b1, b2 in itertools.product((0, 1), repeat=2):
            m, o = vodds({e: b1, f: b2})
            n2 += 1
            w2 = max(w2, abs(m - 0.25), float(np.max(np.abs(o - base))))
    check("C4 [numerical, 1e-16] BKSF cube, %d edge sites: %d cosets, every fibre 2^%d = %d patterns, the "
          "encoded state uniform WITHIN a fibre with fibre total det P_S (%.1e)"
          % (En.NQ, len(reps), k, 1 << k, dev),
          En.NQ == 12 and len(reps) == 128 and (1 << k) == 32 and dev < 1e-16
          and bool(np.allclose(base, 0.5, atol=1e-13)))
    check("C5 [numerical, 1e-14] ONE edge record (%d cases) leaves mass 1/2 and TWO (%d) mass 1/4, both with "
          "the vertex odds UNCHANGED at 1/2 (%.1e, %.1e): below a star, no vertex condition"
          % (n1, n2, w1, w2), n1 == 24 and n2 == 264 and w1 < 1e-14 and w2 < 1e-14)

    w3 = 0.0
    nstar = 0
    for v in range(8):
        star = En.STAR[v]
        for assign in itertools.product((0, 1), repeat=len(star)):
            m, o = vodds(dict(zip(star, assign)))
            if m < 1e-14:
                continue
            b = sum(assign) % 2
            K2, rest = schur_condition(Psea, [v] if b == 1 else [], [] if b == 1 else [v])
            pred = np.array(base)
            for a, u in enumerate(rest):
                pred[u] = K2[a, a]
            pred[v] = float(b)
            w3 = max(w3, float(np.max(np.abs(o - pred))))
            nstar += 1
    Zs = [Pau(0, 0, 1 << qq) for qq in range(En.NQ)]
    zcomm = all(pcomm(a, b) for a, b in itertools.combinations(Zs, 2))
    check("C6 [numerical, 1e-14] a full vertex STAR of edge records (%d assignments, all reachable) induces "
          "exactly the determinantal conditional on n_v = parity(star) (%.1e)"
          % (nstar, w3), nstar == 64 and w3 < 1e-14)

    bad = ncase = 0
    executed_orders = []
    worst = 0.0
    nsets = 0
    for T in itertools.combinations(range(8), 3):
        for vals in itertools.product((0, 1), repeat=3):
            nsets += 1
            ref = None
            for perm in itertools.permutations(range(3)):
                Ks = Psea.copy()
                labels = list(range(8))
                ok = True
                for t in perm:
                    site, b = T[t], vals[t]
                    j = labels.index(site)
                    A = Ks if b == 1 else (np.eye(len(labels)) - Ks)
                    if abs(A[j, j]) < 1e-13:
                        ok = False
                        break
                    keep = [a for a in range(len(labels)) if a != j]
                    An = A[np.ix_(keep, keep)] - np.outer(A[keep, j], A[j, keep]) / A[j, j]
                    Ks = An if b == 1 else (np.eye(len(keep)) - An)
                    labels = [labels[a] for a in keep]
                if not ok:
                    continue
                executed_orders.append((T, vals, perm))
                if ref is None:
                    ref = Ks.copy()
                else:
                    ncase += 1
                    d = float(np.max(np.abs(Ks - ref)))
                    worst = max(worst, d)
                    bad += d > 1e-11
    check("C7 [exact + numerical, 1e-14] ORDER INDEPENDENCE: all %d Z_e commute pairwise (%s), and Schur "
          "conditioning on %d three-record sets in 6 orders gives %d comparisons, %d mismatches (%.1e)"
          % (En.NQ, zcomm, nsets, ncase, bad, worst),
          zcomm and nsets == 448 and bad == 0 and worst < 1e-14
          and ncase == 2240 and len(executed_orders) == 2688
          and set(executed_orders) == {(T,vals,perm)
              for T in itertools.combinations(range(8),3)
              for vals in itertools.product((0,1),repeat=3)
              for perm in ((0,1,2),(0,2,1),(1,0,2),(1,2,0),(2,0,1),(2,1,0))})


# ==================================================== D: the reach of a record

SEA = {}
NBR6 = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def l1(u, L):
    return sum(min(u[a] % L, (-u[a]) % L) for a in range(3))


def build_seas():
    for L in (4, 6, 8):
        best = None
        for tw in itertools.product((0, 1), repeat=3):
            Mx, _, _ = build_torus(L, tw)
            E = float(np.sum(np.linalg.eigvalsh(Mx)[:L ** 3 // 2]))
            if best is None or E < best[1] - 1e-12:
                best = (tw, E)
        tw, E = best
        M, sites, idx = build_torus(L, tw)
        P, _, w = sea_projector(M)
        eps = np.array([(-1) ** sum(v) for v in sites])
        i0 = idx[(0, 0, 0)]
        same = np.where(eps == eps[i0])[0]
        SEA[L] = dict(M=M, P=P, sites=sites, idx=idx, tw=tw, E=E, w=w, i0=i0,
                      V=L ** 3, N=L ** 3 // 2,
                      m2=float(np.max(np.abs(M @ M - 6 * np.eye(L ** 3)))),
                      halfdev=float(np.max(np.abs(np.diag(P) - 0.5))),
                      samedev=float(np.max(np.abs(P[np.ix_(same, same)]
                                                  - 0.5 * np.eye(len(same))))))


def group_D():
    build_seas()
    ok = all(SEA[L]["halfdev"] < 1e-15 and SEA[L]["samedev"] < 1e-15 for L in (4, 6, 8))
    check("D1 [numerical, 1e-15] the vacuum on 4^3, 6^3, 8^3 at optimal twist %s, %s, %s: E_sea = "
          "%.6f, %.6f, %.6f; P_vv = 1/2 and P = I/2 on each sublattice (%.1e)"
          % (SEA[4]["tw"], SEA[6]["tw"], SEA[8]["tw"], SEA[4]["E"], SEA[6]["E"], SEA[8]["E"],
             max(max(SEA[L]["halfdev"], SEA[L]["samedev"]) for L in (4, 6, 8))),
          ok and abs(SEA[4]["E"] + 78.383672) < 1e-5 and abs(SEA[6]["E"] + 258.857540) < 1e-5
          and abs(SEA[8]["E"] + 611.811768) < 1e-5)

    worst = 0.0
    ns = []
    for L in (4, 6, 8):
        S = SEA[L]
        P, i0 = S["P"], S["i0"]
        n = 0
        for j in range(S["V"]):
            if j == i0:
                continue
            for b in (1, 0):
                K2, rest = schur_condition(P, [j] if b else [], [] if b else [j])
                pred = 0.5 - (1 if b else -1) * 2 * P[i0, j] ** 2
                worst = max(worst, abs(K2[rest.index(i0)][rest.index(i0)] - pred))
                n += 1
        ns.append(n)
    check("D2 [numerical, 1e-15] ONE record shifts the odds at every other site by exactly 2 P_vu^2 (down if "
          "occupied, up if empty), against Schur on %d, %d, %d cases (%.1e)"
          % (ns[0], ns[1], ns[2], worst),
          ns == [126, 430, 1022] and worst < 1e-15)

    axis = {}
    sums = []
    for L in (4, 6, 8):
        S = SEA[L]
        P, sites, i0 = S["P"], S["sites"], S["i0"]
        shell = {}
        for j, u in enumerate(sites):
            d = l1(u, L)
            if d:
                shell[d] = max(shell.get(d, 0.0), abs(P[i0, j]))
        axis[L] = [shell.get(d, 0.0) for d in (1, 3, 5, 7)]
        sums.append(float(np.sum(P[i0, :] ** 2) - P[i0, i0] ** 2))
    check("D3 [numerical, 1e-13] largest |P_vu| at d = 1, 3, 5, 7: %.6f then 0 on 4^3; %s on 6^3; %s "
          "on 8^3; sum_{u != v} P_vu^2 = 1/4 exactly (%.1e)"
          % (axis[4][0], " ".join("%.6f" % x for x in axis[6]),
             " ".join("%.6f" % x for x in axis[8]), max(abs(x - 0.25) for x in sums)),
          all(abs(x - 0.25) < 1e-13 for x in sums)
          and abs(axis[4][0] - 0.204124) < 5e-7 and max(axis[4][1:]) < 1e-13
          and abs(axis[6][1] - 0.037805) < 5e-7 and abs(axis[6][2] - 0.008097) < 5e-7
          and abs(axis[6][3] - 0.002368) < 5e-7 and abs(axis[8][1] - 0.023936) < 5e-7
          and abs(axis[8][2] - 0.007268) < 5e-7 and abs(axis[8][3] - 0.003154) < 5e-7)

    census = []
    for L in (4, 6, 8):
        S = SEA[L]
        P, i0, sites = S["P"], S["i0"], S["sites"]
        bad = nz = npred = 0
        for j, u in enumerate(sites):
            if j == i0:
                continue
            nodd = sum(1 for a in range(3) if u[a] % 2 == 1)
            halfs = sum(1 for a in range(3) if u[a] == L // 2 and u[a] % 2 == 0)
            pred = (nodd == 1) and (halfs == 0)
            big = abs(P[i0, j]) > 1e-12
            nz += big
            npred += pred
            bad += (big != pred)
        census.append((S["V"] - 1, npred, nz, bad))
    check("D4 [numerical, 1e-12] SELECTION RULE: P_vu != 0 iff the separation has one odd component and no "
          "even one equal to L/2 -- %d of %d, %d of %d, %d of %d, %d mismatches"
          % (census[0][2], census[0][0], census[1][2], census[1][0], census[2][2], census[2][0],
             sum(c[3] for c in census)),
          sum(c[3] for c in census) == 0
          and [c[2] for c in census] == [6, 81, 108] and [c[1] for c in census] == [6, 81, 108])


def group_D_decay():
    """The decay exponent from a Bloch-block momentum grid, validated against the exact 8^3."""
    S = SEA[8]
    nc = 4
    kk = 2 * np.pi * (np.arange(nc) + 0.5) / nc
    K = np.stack(np.meshgrid(kk, kk, kk, indexing="ij"), axis=-1)
    w8, U8 = np.linalg.eigh(bloch_batch(K))
    Um = U8[..., :4]
    Pk = Um @ np.conj(np.swapaxes(Um, -1, -2))
    Pr8 = np.fft.ifftn(Pk, axes=(0, 1, 2))
    Rg = np.stack(np.meshgrid(*[np.arange(nc)] * 3, indexing="ij"), axis=-1)
    Pr8 = Pr8 * np.exp(1j * np.pi * Rg.sum(-1) / nc)[..., None, None]
    espec = float(np.max(np.abs(np.sort(w8.reshape(-1)) - np.sort(S["w"]))))
    ek = 0.0
    for R in itertools.product(range(nc), repeat=3):
        for s in SUB:
            for sp in SUB:
                u = tuple((2 * R[a] + sp[a]) % 8 for a in range(3))
                ek = max(ek, abs(Pr8[R][SI[sp], SI[s]] - S["P"][S["idx"][u], S["idx"][tuple(s)]]))
    check("D5 [numerical, 1e-14] the Bloch-block machinery (8 x 8 per momentum) reproduces "
          "the exact 8^3 torus: spectra to %.1e, every kernel entry to %.1e" % (espec, ek),
          espec < 1e-14 and ek < 1e-14)

    nc = 48
    Pr, _ = kernel_field(nc)
    rs = list(range(1, nc, 2))
    vs = [abs(Pr[(n // 2, 0, 0)][SI[(n % 2, 0, 0)], SI[(0, 0, 0)]]) for n in rs]
    loc = [(rs[i], np.log(vs[i + 1] / vs[i]) / np.log(rs[i + 1] / rs[i]))
           for i in range(len(rs) - 1) if vs[i] > 0 and vs[i + 1] > 0]
    slope19 = [x for r, x in loc if r == 19][0]
    pts = []
    for R in itertools.product(range(nc // 2), repeat=3):
        for sp in SUB:
            r = np.array([2 * R[a] + sp[a] for a in range(3)], float)
            rn = float(np.linalg.norm(r))
            if rn < 1e-9:
                continue
            v = abs(Pr[R][SI[sp], SI[(0, 0, 0)]])
            if v > 1e-13:
                pts.append((rn, v))
    use = [(r, v) for r, v in pts if 10 <= r <= 30]
    sl, ic = np.polyfit(np.log([r for r, _ in use]), np.log([v for _, v in use]), 1)
    mean3 = float(np.mean([v * r ** 3 for r, v in use]))
    check("D6 [numerical, fitted slope, physical extent %d^3 from 48^3 cell momenta] finite diagnostic: local slope %.2f "
          "at n = 19; a fit on %d separations, 10 <= |r| <= 30, gives |P| ~ |r|^%.2f, mean "
          "|P| |r|^3 = %.2f"
          % (2 * nc, slope19, len(use), sl, mean3),
          abs(slope19 + 3.02) < 0.02 and abs(sl + 3.04) < 0.03 and abs(mean3 - 0.21) < 0.01)


# ==================================================== E: additivity, forcing, and reach beyond the star

def group_E():
    six = {}
    stardev = 0.0
    adddev = 0.0
    rng = {}
    forced = {}
    for L in (4, 6, 8):
        S = SEA[L]
        P, idx, i0 = S["P"], S["idx"], S["i0"]
        nb = [idx[tuple(o[a] % L for a in range(3))] for o in NBR6]
        stardev = max(stardev, float(np.max(np.abs(P[np.ix_(nb, nb)] - 0.5 * np.eye(6)))))
        vals = []
        for m in range(64):
            O = [nb[t] for t in range(6) if (m >> t) & 1]
            E = [nb[t] for t in range(6) if not (m >> t) & 1]
            K2, rest = schur_condition(P, O, E)
            o = float(K2[rest.index(i0)][rest.index(i0)])
            closed = 0.5 - 2 * sum(P[i0, u] ** 2 for u in O) + 2 * sum(P[i0, u] ** 2 for u in E)
            adddev = max(adddev, abs(o - closed))
            vals.append((o, m))
        vals.sort()
        six[L] = (nb, vals)
        rng[L] = (vals[0][0], vals[-1][0])
        forced[L] = sum(1 for o, _ in vals if o < 1e-12 or o > 1 - 1e-12)
    check("E1 [numerical, 1e-15] the six neighbours lie on the other sublattice, so P on them is exactly I/2 "
          "(%.1e) and the odds are ADDITIVE: 1/2 - 2 sum_occ P_vu^2 + 2 sum_empty P_vu^2 over 64 x 3 (%.1e)" % (stardev, adddev), stardev < 1e-15 and adddev < 1e-15)
    check("E2 [numerical, 1e-12] range over the 64: [%.6f, %.6f] on 4^3 with %d forcing; [%.6f, %.6f] on "
          "6^3, %d; [%.6f, %.6f] on 8^3, %d -- in this six-neighbour menu forcing occurs on the torus with M^2 = 6I exactly (%.1e)"
          % (rng[4][0], rng[4][1], forced[4], rng[6][0], rng[6][1], forced[6],
             rng[8][0], rng[8][1], forced[8], SEA[4]["m2"]),
          forced[4] == 2 and forced[6] == 0 and forced[8] == 0 and SEA[4]["m2"] == 0.0
          and abs(rng[6][0] - 0.021268) < 5e-7 and abs(rng[8][0] - 0.024036) < 5e-7
          and rng[4][0] < 1e-12 and rng[4][1] > 1 - 1e-12)

    supp_n = []
    supp_s = []
    whole = []
    minus = []
    for L in (4, 6, 8):
        S = SEA[L]
        P, i0 = S["P"], S["i0"]
        supp = [j for j in range(S["V"]) if j != i0 and abs(P[i0, j]) > 1e-12]
        supp_n.append(len(supp))
        supp_s.append(float(np.sum(P[i0, supp] ** 2)))
        K2, rest = schur_condition(P, supp, [])
        whole.append(float(K2[rest.index(i0)][rest.index(i0)]))
        drop = sorted(supp, key=lambda j: -abs(P[i0, j]))[:-1]
        K3, rest3 = schur_condition(P, drop, [])
        minus.append(float(K3[rest3.index(i0)][rest3.index(i0)]))
    check("E3 [numerical, 1e-12] FORCING: the row support sum of P_vu^2 = 1/4 exactly (%.1e), uniform occupied-support sufficiency: "
          "the tested whole row supports have %d, %d, %d sites, giving odds %.1e; one short leaves "
          "%.1e, %.1e, %.1e"
          % (max(abs(x - 0.25) for x in supp_s), supp_n[0], supp_n[1], supp_n[2],
             max(abs(x) for x in whole), minus[0], minus[1], minus[2]),
          all(abs(x - 0.25) < 1e-13 for x in supp_s) and supp_n == [6, 81, 108]
          and all(abs(x) < 1e-12 for x in whole) and minus[0] > 1e-3
          and abs(minus[1] - 1.12e-5) < 1e-6 and abs(minus[2] - 1.99e-5) < 1e-6)

    L = 8
    S = SEA[L]
    P, idx, sites, i0 = S["P"], S["idx"], S["sites"], S["i0"]
    nb, _ = six[L]
    rows = {}
    for lbl, m0 in (("occ", 63), ("alt", 0b010101)):
        O = [nb[t] for t in range(6) if (m0 >> t) & 1]
        E = [nb[t] for t in range(6) if not (m0 >> t) & 1]
        K2, rest = schur_condition(P, O, E)
        o0 = float(K2[rest.index(i0)][rest.index(i0)])
        per_d = {}
        for j, u in enumerate(sites):
            if j == i0 or j in nb:
                continue
            d = l1(u, L)
            best = 0.0
            for b in (1, 0):
                OO, EE = (O + [j], E) if b else (O, E + [j])
                if abs(joint_prob(P, OO, EE)) < 1e-14:
                    continue
                K3, r3 = schur_condition(P, OO, EE)
                best = max(best, abs(float(K3[r3.index(i0)][r3.index(i0)]) - o0))
            per_d[d] = max(per_d.get(d, 0.0), best)
        rows[lbl] = (o0, per_d)
    o_occ, pd_occ = rows["occ"]
    o_alt, pd_alt = rows["alt"]
    far = max(pd_occ[d] for d in pd_occ if d >= 8)
    check("E4 [numerical, stated finite bounds] BEYOND THE STAR, 8^3, six neighbours occupied (%.4f): one more record at "
          "d = 2..7 shifts at most %.1e, %.1e, %.1e, %.1e, %.1e, %.1e, and by %.1e at d >= 8"
          % (o_occ, pd_occ[2], pd_occ[3], pd_occ[4], pd_occ[5], pd_occ[6], pd_occ[7], far),
          abs(o_occ - 0.024036) < 5e-7 and far == 0.0 and pd_occ[2] > 4e-3 and pd_occ[7] < 1e-4)

    d2 = [idx[u] for u in sites if l1(u, L) == 2]
    maxP2 = max(abs(P[i0, j]) for j in d2)
    K4, r4 = schur_condition(P, [nb[t] for t in range(6) if (0b010101 >> t) & 1],
                             [nb[t] for t in range(6) if not (0b010101 >> t) & 1] + d2)
    shell = float(K4[r4.index(i0)][r4.index(i0)])
    check("E5 [numerical, stated mixed tolerances] with the neighbours ALTERNATING (%.4f) a d = 2 record reaches %.1e though "
          "P_vu = 0 there (%.1e): influence through the Schur complement alone; the d = 2 shell empty "
          "gives %.4f"
          % (o_alt, pd_alt[2], maxP2, shell),
          abs(o_alt - 0.5) < 1e-12 and pd_alt[2] > 5e-2 and maxP2 < 1e-15
          and abs(shell - 0.9704) < 5e-5)


def exact_flat_minor(h, T):
    """det[(I-h/sqrt(6))/2]_T by the bipartite Schur determinant.

    Only the actual integer, bipartite, h^2=6I torus is admitted. The two
    parity blocks of P_T are I/2, so the radical cancels: det =
    2^-|T| det(I-B B^T/6). All elimination below is rational.
    """
    from fractions import Fraction
    assert h.shape == (64, 64) and np.array_equal(h, h.T)
    assert np.array_equal(h @ h, 6 * np.eye(64))
    assert np.array_equal(h, np.rint(h))
    par = [(i // 16 + (i // 4) % 4 + i % 4) % 2 for i in range(64)]
    assert all(h[i, j] == 0 for i in range(64) for j in range(64) if par[i] == par[j])
    A = [i for i in T if par[i] == 0]
    B = [i for i in T if par[i] == 1]
    mat = [[Fraction(int(i == j)) - sum(Fraction(int(h[i,k]*h[j,k]),6) for k in B)
            for j in A] for i in A]
    det = Fraction(1)
    for i in range(len(A)):
        pivot = next((j for j in range(i,len(A)) if mat[j][i]), None)
        if pivot is None:return Fraction(0)
        if pivot != i:mat[i],mat[pivot]=mat[pivot],mat[i];det=-det
        p=mat[i][i];det*=p
        for j in range(i+1,len(A)):
            ratio=mat[j][i]/p
            for k in range(i+1,len(A)):mat[j][k]-=ratio*mat[i][k]
    return det / 2**len(T)


def exact_nonstar_certificate(h):
    """One inclusion-minimal eleven-site support; not a family classification."""
    T=(0,2,3,4,5,12,13,16,17,48,49)
    minors={v:exact_flat_minor(h,tuple(u for u in T if u!=v)) for v in T}
    stars=[{v}|set(np.flatnonzero(h[v]).tolist()) for v in range(64)]
    return T, exact_flat_minor(h,T), minors, not any(S <= set(T) for S in stars)


def group_forcing_corrections():
    M,sites,idx=build_torus(4,(1,1,1))
    h=-M
    P=(np.eye(64)-h/np.sqrt(6))/2
    nb=np.flatnonzero(h[0]).tolist()
    O,E=nb[:3],nb[3:]
    K,rest=schur_condition(P,O,E)
    pr=joint_prob(P,O,E)
    check("E6 [numerical, 1e-13] full row support with three occupied and three empty neighbours "
          "does NOT force n0: condition probability %.12f and conditional odds %.12f" % (pr,K[rest.index(0),rest.index(0)]),
          len(nb)==6 and abs(pr-1/64)<1e-13 and abs(K[rest.index(0),rest.index(0)]-.5)<1e-13)
    T,det,mins,nostar=exact_nonstar_certificate(h)
    from fractions import Fraction
    missing=set(nb)-set(T)
    check("E7 [exact] eleven-site nonstar T=%s has det P_T=%s, all deletion minors positive; "
          "T without 0 occupied forces n0=0 with probability %s despite missing row site %s"
          % (T,det,mins[0],sorted(missing)),
          det==0 and all(x>0 for x in mins.values()) and nostar
          and mins[0]==Fraction(3125,7962624) and missing=={1})


def main():
    group_A()
    group_B()
    group_C()
    group_C_edges()
    group_D()
    group_D_decay()
    group_E()
    group_forcing_corrections()
    print("SUMMARY: the finished set of records is determinantal with kernel P, conditioning is the "
          "Schur complement, and forcing means a conditional Schur diagonal is 0 or 1; neither arbitrary row-cover implication holds.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
