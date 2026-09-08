#!/usr/bin/env python3
"""The sea's cancellation zeros are a determinant criterion; finite minimum stars and nonstar minimal supports.

Class-A finite-cluster runner, self-contained: it imports nothing from this
repository and rebuilds every object from the hopping signs up. The supplied
vacuum is the sea of the designed free-hopping law at N = V/2 with
Kawamoto-Smit link signs; the supplied readout maps incident edge-record bits to coarse occupancy,
and the update clause upstream is Lueders conditioning, stipulated there and
untouched here. Writing h for the one-particle matrix and P for the projector
onto the N lowest modes, the runner establishes:

  A  CUBE CONTROL.  On the open 2x2x2 cube the sea's Born distribution over all
     2^12 records has support 1984, 1856 charge zeros and 256 cancellation
     zeros = 8 corner patterns x 32, the 8 being exactly the closed corner
     stars; the distribution is constant on cycle-space cosets and its
     histogram is bimodal with a 28-decade empty span, so the declared 1e-20
     relative threshold is clean.
  B  THE SLAB, 2^20.  On the open 2x2x3 slab the same census gives support
     411648, charge zeros 575488 and cancellation zeros 61440 = 120 x 512, with
     a 26-decade empty span. The 120 is reached from the many-body vector, not
     from the determinant, and reproduces the "120 of 924" of the determinantal
     note.
  C  THE CLOSED-STAR RULE FAILS ONE CUBE TALLER.  On the slab the closed-star
     rule predicts 324 patterns against 120 actual: 204 false positives, 0 false
     negatives. The eight degree-3 closed stars are NOT singular
     (det P_star = 1.340413e-03); the four degree-4 ones are. The minimal
     zero-carrying corner sets are 12 five-corner sets and 36 six-corner sets,
     only 4 of them stars, and most kernel directions mix the +sqrt2 and +2
     bands.
  D  THE CRITERION.  P(S occupied) = det P_S = det (I-P)_{S^c} on all 70 cube
     and all 924 slab patterns; det P_T = 0 iff the empty band carries a state
     supported inside T; on a flat band h^2 = cI this collapses to
     lambda_max(h_T) = sqrt c, which includes the closed stars of
     degree-c corners, realised by (sqrt c + h) e_v. The cube has h^2 = 3I as a
     zero-residual integer identity; the slab's h^2 acquires four unordered pairs, hence eight
     ordered off-diagonal entries, two per open z-column.
  E  THE ANTIPERIODIC 4^3 TORUS.  h^2 = 6I exactly, the sector is gapped, all
     64 closed stars are singular, and a complete enumeration of all 1391280
     connected corner sets of size <= 7 finds that the attainers of sqrt 6 are
     exactly the 64 closed stars. The periodic 4^3 has 8 zero modes and no
     unique sea.
  F  6^3 AND 8^3.  The gapped sectors are twist (0,0,0) at 6^3 and (1,1,1) at
     8^3, reproducing the determinantal note's optimal twists. There h^2 is not
     proportional to I, closed-star minors exceed the old cutoff, and that determinant cutoff plus a separate
     numerical eigenvalue-margin diagnostic are reported for: all connected sets of size <= 5 (6^3) and <= 4 (8^3)
     plus two declared fixed families of larger sets.

Exact lines are integer or rational arithmetic at zero tolerance; numerical
lines are double precision on integer-derived data, each printing the residual
it is judged against. Every line is tagged [exact] or [numerical]. There is no
random draw anywhere: every scan is a complete enumeration or a declared fixed
family, and the Lanczos start vector is a declared deterministic vector.

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
AUDIT_INPUT_PATHS = ('docs/THE_SEAS_CANCELLATION_ZEROS_ARE_A_DETERMINANT_CRITERION_CLOSED_STARS_ONLY_ON_FLAT_BANDS_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
_EXPECTED_INPUT_SHA256 = {'docs/THE_SEAS_CANCELLATION_ZEROS_ARE_A_DETERMINANT_CRITERION_CLOSED_STARS_ONLY_ON_FLAT_BANDS_BOUNDED_THEOREM_NOTE_2026-09-03.md': '9dfa7f9d86b88a1626a51de237386b33faa56554bce7731a972c3747b909a733', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

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
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 240

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


# ===================================================== Pauli algebra, symplectic

def pc(n):
    return bin(n).count("1")


class Pauli:
    """i^k prod_q X_q^{x_q} Z_q^{z_q}, with X before Z on every qubit."""

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


PID = Pauli(0, 0, 0)
PH = [1 + 0j, 1j, -1 + 0j, -1j]


def commutes(a, b):
    return (pc(a.x & b.z) + pc(a.z & b.x)) % 2 == 0


# ============================================ geometry: open 2 x 2 x Lz clusters

def open_block(Lx, Ly, Lz):
    """Vertices (x, y, z) indexed (x*Ly + y)*Lz + z; nearest-neighbour edges, no wrap.

    Kawamoto-Smit link signs: eta_1 = 1, eta_2 = (-1)^{v_1}, eta_3 = (-1)^{v_1 + v_2}.
    """
    idx = {}
    for x in range(Lx):
        for y in range(Ly):
            for z in range(Lz):
                idx[(x, y, z)] = (x * Ly + y) * Lz + z
    V = Lx * Ly * Lz
    raw = []

    def add(p, q, a):
        raw.append((min(idx[p], idx[q]), max(idx[p], idx[q]), a, p))

    for (x, y, z) in idx:
        if x + 1 < Lx:
            add((x, y, z), (x + 1, y, z), 0)
        if y + 1 < Ly:
            add((x, y, z), (x, y + 1, z), 1)
        if z + 1 < Lz:
            add((x, y, z), (x, y, z + 1), 2)
    raw.sort(key=lambda t: (t[0], t[1]))
    EDGES = [(i, j) for (i, j, a, p) in raw]
    eta = []
    for (i, j, a, p) in raw:
        x, y, z = p
        if a == 0:
            eta.append(1)
        elif a == 1:
            eta.append(-1 if x & 1 else 1)
        else:
            eta.append(-1 if (x + y) & 1 else 1)
    FACES = []

    def nxt(c, a):
        v = list(c)
        if v[a] + 1 < (Lx, Ly, Lz)[a]:
            v[a] += 1
            return tuple(v)
        return None

    for c in idx:
        for a, b in itertools.combinations(range(3), 2):
            p1, p2 = nxt(c, a), nxt(c, b)
            if p1 is None or p2 is None:
                continue
            p3 = nxt(p1, b)
            if p3 is None or p3 != nxt(p2, a):
                continue
            FACES.append((idx[c], idx[p1], idx[p3], idx[p2]))
    return V, EDGES, sorted(set(FACES)), np.array(eta, dtype=np.int64)


def hmat(V, EDGES, eta):
    """H = -t sum_e eta_e T_e at t = 1, so h_ij = -eta_ij."""
    h = np.zeros((V, V))
    for q, (i, j) in enumerate(EDGES):
        h[i, j] = h[j, i] = -float(eta[q])
    return h


def face_fluxes(FACES, EDGES, eta):
    ei = {}
    for q, (i, j) in enumerate(EDGES):
        ei[(i, j)] = ei[(j, i)] = q
    out = []
    for cyc in FACES:
        f = 1
        for t in range(len(cyc)):
            f *= int(eta[ei[(cyc[t], cyc[(t + 1) % len(cyc)])]])
        out.append(f)
    return out


# ============================================ the superfast encoding on the edges

class Enc:
    """Edge qubits; A on edges with the Z tail on lower-indexed incident edges at
    both ends; B_v the product of the Z's on the edges incident to v; the face
    loops as stabilizers. n_v = parity of the record bits on star(v)."""

    def __init__(self, V, EDGES, FACES):
        self.V = V
        self.EDGES = list(EDGES)
        self.FACES = list(FACES)
        self.NQ = len(EDGES)
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = self.EIDX[(j, i)] = q
        self.NBR = {i: sorted(j for (a, b) in self.EDGES
                              for j in ((b,) if a == i else ((a,) if b == i else ())))
                    for i in range(V)}
        self.STAR = {i: [self.EIDX[(i, k)] for k in self.NBR[i]] for i in range(V)}
        self.STARMASK = {i: reduce(lambda a, b: a | (1 << b), self.STAR[i], 0)
                         for i in range(V)}

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
        out = PID
        for a in range(len(cyc)):
            out = out * self.A(cyc[a], cyc[(a + 1) % len(cyc)])
        return out

    def hop_pauli(self, i, j):
        A = self.A(i, j)
        return A * self.B(i), A * self.B(j)


def encoding_audit(E):
    """R0-R4 of the encoding, and an independent stabilizer generating set."""
    A = {e: E.A(*e) for e in E.EDGES}
    Bv = {i: E.B(i) for i in range(E.V)}
    R = {}
    R["R0"] = (all(E.A_unsigned(i, j) == E.A_unsigned(j, i) for (i, j) in E.EDGES)
               and all(E.A(j, i) == E.A(i, j).neg() for (i, j) in E.EDGES))
    R["R1"] = (all(A[e].is_herm() and (A[e] * A[e]).is_id() for e in E.EDGES)
               and all(Bv[i].is_herm() and (Bv[i] * Bv[i]).is_id() for i in range(E.V)))
    r2 = all(commutes(Bv[i], Bv[j]) for i, j in itertools.combinations(range(E.V), 2))
    for e in E.EDGES:
        for v in range(E.V):
            r2 &= (commutes(A[e], Bv[v]) != (v in e))
    R["R2"] = bool(r2)
    R["R3"] = all(commutes(A[e], A[f]) != (len(set(e) & set(f)) == 1)
                  for e, f in itertools.combinations(E.EDGES, 2))
    S = [E.loop(f) for f in E.FACES]
    r4 = True
    for s in S:
        r4 &= s.is_herm() and (s * s).is_id()
        for e in E.EDGES:
            r4 &= commutes(s, A[e])
        for v in range(E.V):
            r4 &= commutes(s, Bv[v])
    for a, b in itertools.combinations(S, 2):
        r4 &= commutes(a, b)
    R["R4"] = bool(r4)
    gens, basis = [], []
    for s in S:
        v = s.x
        for b in basis:
            v = min(v, v ^ b)
        if v:
            basis.append(v)
            basis.sort(reverse=True)
            gens.append(s)
    R["gens"] = gens
    R["k"] = len(gens)
    grp = []
    for m in range(1 << len(gens)):
        p = PID
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        grp.append(p)
    R["grp_ok"] = (not any(g.is_mid() for g in grp)) and sum(1 for g in grp if g.x == 0) == 1
    return R


def parity_np(x):
    x = np.asarray(x, dtype=np.int64)
    for s in (32, 16, 8, 4, 2, 1):
        x = x ^ (x >> s)
    return x & 1


class Model:
    """H = -t sum_e eta_e T_e on the record sector N(z) = nfill, sparse only."""

    def __init__(self, V, EDGES, FACES, eta, nfill):
        self.V = V
        self.NQ = len(EDGES)
        self.D = 1 << self.NQ
        self.En = Enc(V, EDGES, FACES)
        self.AUD = encoding_audit(self.En)
        self.k = self.AUD["k"]
        self.gens = self.AUD["gens"]
        Z = np.arange(self.D, dtype=np.int64)
        NVAL = np.zeros(self.D, dtype=np.int8)
        for v in range(V):
            NVAL += parity_np(Z & self.En.STARMASK[v]).astype(np.int8)
        del Z
        self.nfill = nfill
        self.J = np.flatnonzero(NVAL == nfill).astype(np.int64)
        self.n = len(self.J)
        del NVAL
        self.loc = -np.ones(self.D, dtype=np.int64)
        self.loc[self.J] = np.arange(self.n)
        rows, cols, dat = [], [], []
        for q, e in enumerate(EDGES):
            P1, P2 = self.En.hop_pauli(*e)
            assert P1.x == P2.x == (1 << q)
            s1 = 1 - 2 * parity_np(self.J & P1.z)
            s2 = 1 - 2 * parity_np(self.J & P2.z)
            a = 0.5j * (PH[P1.k] * s1 - PH[P2.k] * s2)
            assert np.max(np.abs(a.real)) < 1e-12
            ai = np.round(a.imag).astype(np.int8)
            assert np.max(np.abs(a.imag - ai)) < 1e-12
            amp = (-int(eta[q])) * ai
            m = amp != 0
            src = np.flatnonzero(m)
            tgt = self.loc[self.J[src] ^ (1 << q)]
            assert np.all(tgt >= 0)
            rows.append(tgt)
            cols.append(src)
            dat.append(1j * amp[src].astype(np.float64))
        self.H = sp.coo_matrix(
            (np.concatenate(dat), (np.concatenate(rows), np.concatenate(cols))),
            shape=(self.n, self.n)).tocsr()

    def apply_pauli(self, p, v):
        s = (1 - 2 * parity_np(self.J & p.z)) * PH[p.k]
        out = np.zeros_like(v)
        tgt = self.loc[self.J ^ p.x]
        assert np.all(tgt >= 0)
        out[tgt] = s * v
        return out

    def project_code(self, v):
        for g in self.gens:
            v = 0.5 * (v + self.apply_pauli(g, v))
        return v

    def sea(self):
        """Ground vector in the record sector. DECLARED start vector, no random draw:
        v0_j = cos(j) + i cos(0.7 j + 1), code-projected and normalised."""
        t = np.arange(self.n, dtype=np.float64)
        v0 = self.project_code(np.cos(t) + 1j * np.cos(0.7 * t + 1.0))
        v0 /= np.linalg.norm(v0)
        w, U = spla.eigsh(self.H, k=3, which="SA", v0=v0, tol=0, maxiter=20000)
        psi = self.project_code(U[:, 0])
        psi /= np.linalg.norm(psi)
        res = float(np.linalg.norm(self.H @ psi - (psi.conj() @ (self.H @ psi)) * psi))
        return float(w[0]), psi, res


# ==================================================================== the tori

def torus(L, tw):
    """L^3 torus with Kawamoto-Smit signs; tw_a = 1 negates the links crossing the
    a-boundary (v_a = L-1 -> 0), i.e. antiperiodic on axis a."""
    V = L ** 3

    def idx(x, y, z):
        return (x % L) * L * L + (y % L) * L + (z % L)

    h = np.zeros((V, V))
    for x in range(L):
        for y in range(L):
            for z in range(L):
                v = (x, y, z)
                for a in range(3):
                    w = list(v)
                    w[a] = (v[a] + 1) % L
                    e = -(1 if a == 0 else ((-1) ** x if a == 1 else (-1) ** (x + y)))
                    if tw[a] and v[a] == L - 1:
                        e = -e
                    i, j = idx(*v), idx(*w)
                    h[i, j] += e
                    h[j, i] += e
    NBR = {v: sorted(np.flatnonzero(np.abs(h[v]) > 0.5).tolist()) for v in range(V)}
    fl = []
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for a, b in itertools.combinations(range(3), 2):
                    v = [x, y, z]
                    va = v[:]; va[a] = (va[a] + 1) % L
                    vb = v[:]; vb[b] = (vb[b] + 1) % L
                    vab = va[:]; vab[b] = (vab[b] + 1) % L
                    fl.append(round(float(h[idx(*v), idx(*va)] * h[idx(*va), idx(*vab)]
                                          * h[idx(*vab), idx(*vb)] * h[idx(*vb), idx(*v)])))
    pol = []
    for a in range(3):
        v = [0, 0, 0]
        pr = 1.0
        for _ in range(L):
            w = v[:]; w[a] = (v[a] + 1) % L
            pr *= h[idx(*v), idx(*w)]
            v = w
        pol.append(round(float(pr)))
    return V, h, NBR, fl, pol


def connected_sets(NBR, V, kmax):
    """Every connected corner set of size 2..kmax, each generated exactly once.

    Standard exclusive-neighbourhood enumeration: a set is grown from its least
    element v0, and a corner is offered only if it is not already in the closed
    neighbourhood of the set, so no set is reached twice. Returned as int16
    arrays of shape (count, k)."""
    NB = {v: frozenset(NBR[v]) for v in range(V)}
    chunks = {k: [] for k in range(2, kmax + 1)}
    for v0 in range(V):
        buf = {k: [] for k in range(2, kmax + 1)}
        stack = [((v0,), tuple(sorted(u for u in NB[v0] if u > v0)),
                  frozenset([v0]) | NB[v0])]
        while stack:
            S, ext, excl = stack.pop()
            for i, u in enumerate(ext):
                S2 = S + (u,)
                ext2 = ext[i + 1:] + tuple(w for w in sorted(NB[u])
                                           if w > v0 and w not in excl)
                buf[len(S2)].append(S2)
                if len(S2) < kmax:
                    stack.append((S2, ext2, excl | NB[u]))
        for k in buf:
            if buf[k]:
                chunks[k].append(np.array(buf[k], dtype=np.int16))
    return {k: (np.concatenate(v) if v else np.zeros((0, k), np.int16))
            for k, v in chunks.items()}


def census_keys_valid(NBR, sets):
    """Validate the ACTUAL rows later diagonalized: distinct connected vertex sets.

    Completeness also uses the exclusive-neighbourhood proof and declared count,
    with an independent brute-force cube comparison below. No printed count
    stands in for distinct executed keys.
    """
    V=len(NBR);adj=np.zeros((V,V),dtype=bool)
    for v,nb in NBR.items():adj[v,list(nb)]=True
    report=[]
    for k,rows in sorted(sets.items()):
        canon=np.sort(rows.astype(np.int64),axis=1)
        valid=bool(np.all((canon>=0)&(canon<V)) and np.all(np.diff(canon,axis=1)>0))
        if not valid:return False,report+[(k,len(rows),False)]
        unique=len(np.unique(canon,axis=0))==len(rows)
        conn=True
        for lo in range(0,len(rows),40000):
            rr=canon[lo:lo+40000];edges=adj[rr[:,:,None],rr[:,None,:]]
            reach=np.zeros((len(rr),k),bool);reach[:,0]=True
            for _ in range(k-1):reach |= np.any(reach[:,:,None]&edges,axis=1)
            conn &= bool(np.all(reach))
        report.append((k,len(rows),unique,conn))
    return all(r[2] and r[3] for r in report),report


def small_census_control():
    nb={i:[j for j in range(8) if (i^j).bit_count()==1] for i in range(8)}
    rows=connected_sets(nb,8,6)
    for k,arr in rows.items():
        want=set()
        for T in itertools.combinations(range(8),k):
            seen={T[0]}
            for _ in range(k):seen |= {j for i in tuple(seen) for j in nb[i] if j in T}
            if len(seen)==k:want.add(T)
        got=[tuple(sorted(map(int,row))) for row in arr]
        if len(got)!=len(set(got)) or set(got)!=want:return False
    return sum(map(len,rows.values()))==150


def batch_top_eig(h, sets, chunk=40000):
    """lambda_max of h restricted to each row of `sets`."""
    out = np.empty(len(sets))
    for a in range(0, len(sets), chunk):
        ix = sets[a:a + chunk].astype(np.intp)
        sub = h[ix[:, :, None], ix[:, None, :]]
        out[a:a + chunk] = np.linalg.eigvalsh(sub)[:, -1]
    return out


def batch_absdet(P, sets, chunk=40000):
    out = np.empty(len(sets))
    for a in range(0, len(sets), chunk):
        ix = sets[a:a + chunk].astype(np.intp)
        sub = P[ix[:, :, None], ix[:, None, :]]
        out[a:a + chunk] = np.abs(np.linalg.det(sub))
    return out


def projector(h, N):
    w, U = np.linalg.eigh(h)
    return w, U, U[:, :N] @ U[:, :N].conj().T


# ======================================================== the many-body census

REL_TOL = 1e-20          # declared before the run: p < REL_TOL * p_max is a zero
DET_TOL = 1e-12          # declared before the run: |det P_T| < DET_TOL is singular
GEO_TOL = 0.20           # preserved historical geometric-mean diagnostic; NOT an exact-zero test
MARGIN_TOL = 1e-8        # NEW post-review finite eigenvalue-margin diagnostic, not DET_TOL replacement


def census(V, EDGES, FACES, eta, name):
    """Full Born distribution over all 2^E records, and the zero census."""
    N = V // 2
    NE = len(EDGES)
    M = Model(V, EDGES, FACES, eta, N)
    fl = face_fluxes(FACES, EDGES, eta)
    E0, sea, res = M.sea()
    h = hmat(V, EDGES, eta)
    w, U, P = projector(h, N)
    stab = max(float(np.max(np.abs(M.apply_pauli(g, sea) - sea))) for g in M.gens)
    born = np.zeros(1 << NE)
    born[M.J] = np.abs(sea) ** 2
    pmax = born.max()
    nz = born[born > 0.0]
    rel = nz / pmax
    lo = int(np.sum(rel < 1e-30))
    mid26 = int(np.sum((rel >= 1e-30) & (rel < 1e-4)))
    band = int(np.sum((rel >= 1e-4) & (rel < 1e-2)))
    hi = int(np.sum(rel >= 1e-2))
    tol = REL_TOL * pmax
    Zi = np.arange(1 << NE, dtype=np.int64)
    CP = np.zeros(1 << NE, dtype=np.int32)
    NV = np.zeros(1 << NE, dtype=np.int8)
    for v in range(V):
        b = parity_np(Zi & M.En.STARMASK[v])
        CP |= (b << v).astype(np.int32)
        NV += b.astype(np.int8)
    del Zi
    ncp = 1 << V
    pcp = np.bincount(CP, weights=born, minlength=ncp)
    cnt = np.bincount(CP, minlength=ncp)
    occ = cnt > 0
    mx = np.zeros(ncp)
    mn = np.full(ncp, np.inf)
    np.maximum.at(mx, CP, born)
    np.minimum.at(mn, CP, born)
    spread = float(np.max((mx[occ] - mn[occ]) / np.maximum(mx[occ], 1e-300)))
    supp = int(np.sum(born >= tol))
    charge = int(np.sum(NV != N))
    canc = (1 << NE) - supp - charge
    nb = np.array([bin(c).count("1") for c in range(ncp)])
    vanish = np.flatnonzero((nb == N) & occ & (pcp < tol))
    del CP, NV, born, pcp
    return dict(name=name, V=V, NE=NE, N=N, k=M.k, coset=int(cnt[occ][0]), n=M.n,
                E0=E0, res=res, w=w, U=U, P=P, h=h, stab=stab, spread=spread,
                supp=supp, charge=charge, canc=canc, vanish=vanish,
                lo=lo, mid26=mid26, band=band, hi=hi, minrel=float(rel.min()),
                npos=int(nz.size), nfaces=len(fl), allflux=(set(fl) == {-1}),
                NBR=M.En.NBR, tol=tol, pmax=pmax)


def stars_of(NBR, V):
    return {v: tuple(sorted([v] + list(NBR[v]))) for v in range(V)}


def group_A_cube(C):
    """The cube control."""
    V, N = C["V"], C["N"]
    check("A1 [exact] cube 2x2x2: V=%d, E=%d, cycle dim E-V+1=%d so each corner pattern carries "
          "a coset of %d records, all %d face fluxes -1, |J|=%d"
          % (V, C["NE"], C["NE"] - V + 1, C["coset"], C["nfaces"], C["n"]),
          V == 8 and C["NE"] == 12 and C["k"] == 5 and C["coset"] == 32 and C["n"] == 2240
          and C["nfaces"] == 6 and C["allflux"])
    w = C["w"]
    check("A2 [numerical, 1e-11] cube sea E_sea=%.12f=-4 sqrt3 (one-particle sum to %.1e, "
          "H-residual %.1e), Fermi gap %.9f=2 sqrt3 so unique, stabilised by all %d generators "
          "to %.1e"
          % (C["E0"], abs(C["E0"] - w[:N].sum()), C["res"], w[N] - w[N - 1], C["k"], C["stab"]),
          abs(C["E0"] + 4 * np.sqrt(3)) < 1e-10 and abs(C["E0"] - w[:N].sum()) < 1e-11
          and C["res"] < 1e-11 and abs(w[N] - w[N - 1] - 2 * np.sqrt(3)) < 1e-10
          and C["stab"] < 1e-8)
    check("A3 [numerical, exact] the odds are constant on cycle-space cosets: max relative spread "
          "within a coset %.3e, so every zero is a whole coset of %d records"
          % (C["spread"], C["coset"]),
          C["spread"] == 0.0)
    check("A4 [numerical, 1e-20 relative] cube p/p_max over %d positive entries is bimodal: %d "
          "below 1e-30 (smallest %.2e), %d at or above 1e-2, %d in the 28 decades between"
          % (C["npos"], C["lo"], C["minrel"], C["hi"], C["mid26"] + C["band"]),
          C["npos"] == 2240 and C["lo"] == 256 and C["hi"] == 1984
          and C["mid26"] == 0 and C["band"] == 0 and C["minrel"] < 1e-30)
    check("A5 [numerical, 1e-20 relative] cube census over all 2^12 records: support %d, charge "
          "zeros %d (every N != 4), cancellation zeros %d"
          % (C["supp"], C["charge"], C["canc"]),
          C["supp"] == 1984 and C["charge"] == 1856 and C["canc"] == 256)
    check("A6 [exact] the %d cancellation zeros are %d corner patterns x %d records"
          % (C["canc"], len(C["vanish"]), C["coset"]),
          len(C["vanish"]) == 8 and len(C["vanish"]) * C["coset"] == C["canc"])
    st = stars_of(C["NBR"], V)
    got = set()
    for m in C["vanish"]:
        got.add(tuple(v for v in range(V) if (int(m) >> v) & 1))
    want = set()
    for v in range(V):
        want.add(tuple(sorted(st[v])))
    check("A7 [exact] those %d patterns are exactly the %d closed corner stars {v} u N(v), each "
          "labelled twice: star(v) all-occupied and star(v-bar) all-empty"
          % (len(got), len(want)), got == want and len(want) == 8)


def group_B_slab(S):
    """The 2x2x3 slab, open in z: the full 2^20 census."""
    V, N, w = S["V"], S["N"], S["w"]
    deg = {v: len(S["NBR"][v]) for v in range(V)}
    ndeg3 = sum(1 for v in range(V) if deg[v] == 3)
    check("B1 [exact] slab 2x2x3 open in z: V=%d (%d of degree 3 at the z-boundaries, %d of "
          "degree 4 in the middle), E=%d, cycle dim %d, coset %d records, all %d face fluxes -1, "
          "|J|=%d"
          % (V, ndeg3, V - ndeg3, S["NE"], S["NE"] - V + 1, S["coset"], S["nfaces"], S["n"]),
          V == 12 and S["NE"] == 20 and S["k"] == 9 and S["coset"] == 512
          and ndeg3 == 8 and S["n"] == 473088 and S["nfaces"] == 11 and S["allflux"])
    check("B2 [numerical, 1e-10] slab sea E_sea=%.12f=-(8+2 sqrt2) (sum to %.1e, residual %.1e), "
          "spectrum (-2)^4 (-sqrt2)^2 | (+sqrt2)^2 (+2)^4, gap %.9f=2 sqrt2 so unique, stabilised "
          "by all %d generators to %.1e"
          % (S["E0"], abs(S["E0"] - w[:N].sum()), S["res"], w[N] - w[N - 1], S["k"], S["stab"]),
          abs(S["E0"] + (8 + 2 * np.sqrt(2))) < 1e-9 and abs(S["E0"] - w[:N].sum()) < 1e-10
          and S["res"] < 1e-9 and abs(w[N] - w[N - 1] - 2 * np.sqrt(2)) < 1e-9
          and S["stab"] < 1e-7
          and np.allclose(np.sort(np.round(w, 9)),
                          np.sort(np.array([-2.0] * 4 + [-np.sqrt(2)] * 2 + [np.sqrt(2)] * 2
                                           + [2.0] * 4)), atol=1e-8))
    check("B3 [numerical, exact] the odds are constant on cosets here too: max relative spread "
          "%.3e over cosets of %d" % (S["spread"], S["coset"]), S["spread"] == 0.0)
    check("B4 [numerical, 1e-20 relative] slab p/p_max over %d positive entries: %d below 1e-30 "
          "(smallest %.2e), %d in the 26 decades to 1e-4, %d in [1e-4,1e-2), %d above"
          % (S["npos"], S["lo"], S["minrel"], S["mid26"], S["band"], S["hi"]),
          S["npos"] == 473088 and S["lo"] == 61440 and S["mid26"] == 0
          and S["band"] == 96256 and S["hi"] == 315392 and S["minrel"] < 1e-30)
    check("B5 [numerical, 1e-20 relative] slab census over all 2^20 records: support %d, charge "
          "zeros %d (every N != 6), cancellation zeros %d"
          % (S["supp"], S["charge"], S["canc"]),
          S["supp"] == 411648 and S["charge"] == 575488 and S["canc"] == 61440)
    check("B6 [exact] %d cancellation zeros = %d corner patterns x %d; those %d of the 924 at "
          "N=6 reproduce the determinantal note's \"120 of 924\", from the many-body vector and "
          "not from the determinant"
          % (S["canc"], len(S["vanish"]), S["coset"], len(S["vanish"])),
          len(S["vanish"]) == 120 and len(S["vanish"]) * S["coset"] == S["canc"])


def group_C_star_rule(C, S):
    """The closed-star rule one cube taller."""
    V, N, P, NBR = S["V"], S["N"], S["P"], S["NBR"]
    st = stars_of(NBR, V)
    vanish = set()
    for m in S["vanish"]:
        vanish.add(frozenset(v for v in range(V) if (int(m) >> v) & 1))
    rule = set()
    for Sset in itertools.combinations(range(V), N):
        A = set(Sset)
        B = set(range(V)) - A
        if any(set(st[v]) <= A or set(st[v]) <= B for v in range(V)):
            rule.add(frozenset(A))
    fp = rule - vanish
    fn = vanish - rule
    check("C1 [exact] the closed-star rule (a pattern vanishes when it holds some closed star "
          "all-occupied or all-empty) predicts %d slab patterns against the %d that vanish: %d "
          "false positives, %d false negatives, over-predicting by %.1f"
          % (len(rule), len(vanish), len(fp), len(fn), len(rule) / len(vanish)),
          len(rule) == 324 and len(vanish) == 120 and len(fp) == 204 and len(fn) == 0)
    d3 = sorted(set(round(abs(float(np.linalg.det(P[np.ix_(list(st[v]), list(st[v]))]))), 9)
                    for v in range(V) if len(NBR[v]) == 3))
    d4 = max(abs(float(np.linalg.det(P[np.ix_(list(st[v]), list(st[v]))])))
             for v in range(V) if len(NBR[v]) == 4)
    check("C2 [numerical, 1e-12] the slab's eight degree-3 closed stars are NOT singular: "
          "det P_star=%.6e at every one, well above the declared 1e-12 cutoff; the four "
          "degree-4 stars are singular, max %.1e" % (d3[0], d4),
          len(d3) == 1 and abs(d3[0] - 1.340413e-03) < 1e-8 and d4 < DET_TOL)
    sing = {}
    for k in range(1, N + 1):
        got = [T for T in itertools.combinations(range(V), k)
               if abs(float(np.linalg.det(P[np.ix_(list(T), list(T))]))) < DET_TOL]
        sing[k] = got
    minimal = []
    for k in sorted(sing):
        for T in sing[k]:
            if not any(set(M0) < set(T) for kk in sorted(sing) if kk < k for M0 in sing[kk]):
                minimal.append(T)
    m5 = [T for T in minimal if len(T) == 5]
    m6 = [T for T in minimal if len(T) == 6]
    check("C3 [numerical, 1e-12] no slab corner set of size <= 4 is singular (0 of 12, 66, 220, "
          "495); the minimal zero-carrying sets among sizes <= N=6 are %d of size 5 and %d of size 6, %d in all"
          % (len(m5), len(m6), len(minimal)),
          all(len(sing[k]) == 0 for k in (1, 2, 3, 4)) and len(m5) == 12 and len(m6) == 36
          and len(minimal) == 48)
    cols = [tuple(range(3 * c, 3 * c + 3)) for c in range(4)]
    ok5 = 0
    for T in m5:
        Ts = set(T)
        for col in cols:
            if set(col) <= Ts:
                rest = Ts - set(col)
                if len(rest) == 2 and any(rest <= set(NBR[v]) for v in col):
                    ok5 += 1
                    break
    star5 = [T for T in m5 if any(tuple(sorted(T)) == st[v] for v in range(V))]
    check("C4 [exact] each of the %d minimal five-corner sets is a full z-column plus the two "
          "in-plane neighbours of one of its three sites (4 columns x 3 heights); only the %d "
          "middle-height ones are closed stars, the other %d are stars of nothing"
          % (len(m5), len(star5), len(m5) - len(star5)),
          ok5 == 12 and len(star5) == 4)
    sig = set()
    for T in m6:
        hits = tuple(sorted(len(set(T) & set(col)) for col in cols))
        sig.add(hits)
    check("C5 [exact] each of the %d minimal six-corner sets meets exactly 3 of the 4 z-columns, "
          "each in exactly 2 of its 3 heights: 9 signatures x 4 column triples" % len(m6),
          len(m6) == 36 and sig == {(0, 2, 2, 2)})
    w, U = S["w"], S["U"]
    pure, mixed = 0, 0
    for T in minimal:
        A = P[np.ix_(list(T), list(T))]
        ww, vv = np.linalg.eigh(A)
        c = np.zeros(V)
        c[list(T)] = vv[:, 0]
        coef = U.conj().T @ c
        bands = sorted(set(np.round(w[np.abs(coef) > 1e-9], 6).tolist()))
        if len(bands) == 1:
            pure += 1
        else:
            mixed += 1
    check("C6 [numerical, 1e-9] of the %d minimal sets only %d have a single-band kernel "
          "direction (4 pure +2, 4 pure +sqrt2) and %d mix the +sqrt2 and +2 bands"
          % (len(minimal), pure, mixed),
          pure + mixed == 48 and pure == 8 and mixed == 40)


def born_by_pattern(S):
    """P(corner set S occupied, complement empty) read off the many-body census."""
    V, N = S["V"], S["N"]
    return set(frozenset(v for v in range(V) if (int(m) >> v) & 1) for m in S["vanish"])


def group_D_criterion(C, S):
    """The criterion, and its flat-band collapse."""
    worst = []
    for cl in (C, S):
        V, N, P = cl["V"], cl["N"], cl["P"]
        Q = np.eye(V) - P
        vz = born_by_pattern(cl)
        mm = 0.0
        agree = True
        for T in itertools.combinations(range(V), N):
            Tc = tuple(v for v in range(V) if v not in T)
            dP = float(np.linalg.det(P[np.ix_(list(T), list(T))]).real)
            dQ = float(np.linalg.det(Q[np.ix_(list(Tc), list(Tc))]).real)
            mm = max(mm, abs(dP - dQ))
            agree &= ((abs(dP) < DET_TOL) == (frozenset(T) in vz))
        worst.append((mm, agree, len(list(itertools.combinations(range(V), N)))))
    check("D1 [numerical, 1e-13] det P_S = det (I-P)_{S^c} on all %d cube and %d slab patterns "
          "(max difference %.1e, %.1e), and the singular patterns equal the Born zeros of A and B "
          "as sets, no tolerance slack: %s, %s"
          % (worst[0][2], worst[1][2], worst[0][0], worst[1][0], worst[0][1], worst[1][1]),
          worst[0][2] == 70 and worst[1][2] == 924 and worst[0][0] < 1e-13
          and worst[1][0] < 1e-13 and worst[0][1] and worst[1][1])
    # the mechanism: det P_T = 0 iff the empty band carries a state supported inside T
    resid = 0.0
    nsets = 0
    for cl in (C, S):
        V, N, P = cl["V"], cl["N"], cl["P"]
        sing = {}
        for k in range(1, N + 1):
            sing[k] = [T for T in itertools.combinations(range(V), k)
                       if abs(float(np.linalg.det(P[np.ix_(list(T), list(T))]))) < DET_TOL]
        for k in sorted(sing):
            for T in sing[k]:
                if any(set(M0) < set(T) for kk in sorted(sing) if kk < k for M0 in sing[kk]):
                    continue
                A = P[np.ix_(list(T), list(T))]
                _, vv = np.linalg.eigh(A)
                c = np.zeros(V)
                c[list(T)] = vv[:, 0]
                resid = max(resid, float(np.linalg.norm(P @ c)))
                assert set(v for v in range(V) if abs(c[v]) > 1e-9) == set(T)
                nsets += 1
    check("D2 [exact + numerical, 1e-13] det P_T = det(W_T W_T^dag) vanishes iff the rows of W on "
          "T are dependent, i.e. iff some c supported on T has Pc = 0: on all %d minimal singular "
          "sets of the two clusters supp(c) = T exactly and ||Pc|| <= %.1e"
          % (nsets, resid), nsets == 56 and resid < 1e-13)
    hc = C["h"]
    r_cube = float(np.linalg.norm(hc @ hc - 3 * np.eye(C["V"])))
    check("D3 [exact] the cube's band is flat: ||h^2 - 3I|| = %.1e, each face's two 2-paths "
          "cancelling under flux -1" % r_cube, r_cube == 0.0)
    hs = S["h"]
    h2 = hs @ hs
    V = S["V"]
    off = sorted((i, j) for i in range(V) for j in range(V) if i != j and abs(h2[i, j]) > 1e-9)
    diag = sorted(set(np.round(np.diag(h2), 9).tolist()))
    col = np.array([[3.0, 0.0, 1.0], [0.0, 4.0, 0.0], [1.0, 0.0, 3.0]])
    ev = sorted(np.round(np.linalg.eigvalsh(col), 9).tolist())
    check("D4 [exact] the slab's band is not flat: h^2 has diagonal deg(v) in %s and exactly %d "
          "off-diagonal entries, all 1, at %s -- the two ends of each open z-column joined by one "
          "uncancelled 2-path; the column block [[3,0,1],[0,4,0],[1,0,3]] has eigenvalues %s so "
          "spec(h^2) = 2^4 4^8"
          % (diag, len(off), [(i, j) for (i, j) in off if i < j], ev),
          diag == [3.0, 4.0] and len(off) == 8
          and [(i, j) for (i, j) in off if i < j] == [(0, 2), (3, 5), (6, 8), (9, 11)]
          and all(abs(h2[i, j] - 1.0) < 1e-12 for (i, j) in off)
          and ev == [2.0, 4.0, 4.0]
          and sorted(np.round(np.linalg.eigvalsh(h2), 6).tolist()) == [2.0] * 4 + [4.0] * 8)
    # flat-band corollary on the cube: det P_T = 0 <=> lambda_max(h_T) = sqrt 3
    V, N, P = C["V"], C["N"], C["P"]
    lam = np.sqrt(3.0)
    bad = 0
    for k in range(1, N + 1):
        for T in itertools.combinations(range(V), k):
            d = abs(float(np.linalg.det(P[np.ix_(list(T), list(T))])))
            l = float(np.linalg.eigvalsh(hc[np.ix_(list(T), list(T))])[-1])
            if (d < DET_TOL) != (l > lam - 1e-9):
                bad += 1
    check("D5 [exact + numerical, 1e-9] flat-band corollary: h^2 = cI makes the empty band the "
          "+sqrt c eigenspace, so det P_T = 0 <=> lambda_max(h_T) = sqrt c (forward by "
          "restriction, back because the padded top eigenvector of h_T is a global maximiser of "
          "the Rayleigh quotient). The two sides agree on all %d cube sets of size <= N, %d "
          "mismatches"
          % (sum(1 for k in range(1, N + 1) for _ in itertools.combinations(range(V), k)), bad),
          bad == 0)
    cls = []
    for v in range(V):
        c = hc[:, v].copy()
        c[v] += lam
        r = float(np.linalg.norm(hc @ c - lam * c) / np.linalg.norm(c))
        supp = tuple(u for u in range(V) if abs(c[u]) > 1e-9)
        star = tuple(sorted([v] + list(C["NBR"][v])))
        cls.append((r, supp == star, abs(float(np.linalg.det(P[np.ix_(list(supp), list(supp))])))))
    check("D6 [numerical, 1e-13] and the minimal solutions are realised: (sqrt c + h) e_v is an "
          "h-eigenvector at +sqrt c supported exactly on star(v), since h^2 e_v = c e_v. All %d "
          "cube corners: max relative residual %.1e, support = the star every time (%s), max "
          "|det P_star| %.1e"
          % (V, max(r for r, _, _ in cls), all(s for _, s, _ in cls),
             max(d for _, _, d in cls)),
          max(r for r, _, _ in cls) < 1e-13 and all(s for _, s, _ in cls)
          and max(d for _, _, d in cls) < DET_TOL)


def group_E_torus4():
    """The antiperiodic 4^3 torus: the flat band survives, and the stars are all minimum-cardinality solutions."""
    L = 4
    V, h, NBR, fl, pol = torus(L, (1, 1, 1))
    N = V // 2
    r = float(np.linalg.norm(h @ h - 6 * np.eye(V)))
    w, U, P = projector(h, N)
    gap = float(w[N] - w[N - 1])
    check("E1 [exact] antiperiodic 4^3 (twist (1,1,1), links crossing each boundary negated): all "
          "%d fluxes -1, Polyakov loops %s, ||h^2 - 6I|| = %.1e. At L=4, v+2e_a and v-2e_a are one "
          "vertex, so the two 2-paths to it multiply to the a-Polyakov loop, -1: they cancel"
          % (len(fl), pol, r),
          set(fl) == {-1} and pol == [-1, -1, -1] and r == 0.0)
    check("E2 [numerical, 1e-9] gapped: spectrum +-sqrt6, 32 each, Fermi gap %.9f = 2 sqrt6, so "
          "the sea is a unique Slater determinant and the criterion has one P" % gap,
          abs(gap - 2 * np.sqrt(6)) < 1e-9
          and sorted(set(np.round(w, 6).tolist())) == [-2.449490, 2.449490])
    st = sorted(set(tuple(sorted([v] + list(NBR[v]))) for v in range(V)))
    dmax = max(abs(float(np.linalg.det(P[np.ix_(list(T), list(T))]))) for T in st)
    check("E3 [numerical, 1e-12] all %d closed corner stars (7 corners each) are singular, max "
          "|det P_star| = %.3e" % (len(st), dmax),
          len(st) == 64 and dmax < DET_TOL)
    lam = float(w[-1])
    CS = connected_sets(NBR, V, 7)
    key_ok,key_report=census_keys_valid(NBR,CS)
    counts = {k: len(CS[k]) for k in sorted(CS)}
    tot = sum(counts.values())
    tops = {}
    hits = {}
    for k in sorted(CS):
        lm = batch_top_eig(h, CS[k])
        tops[k] = float(lm.max())
        hits[k] = np.flatnonzero(lm > lam - 1e-9)
    ok_small = all(abs(tops[k] - np.sqrt(k - 1)) < 1e-9 for k in range(2, 8))
    got7 = set(tuple(sorted(row.tolist())) for row in CS[7][hits[7]])
    check("E4 [numerical, complete enumeration, 1e-9] all %d connected corner sets of size 2..7 "
          "(%s): max lambda_max(h_T) = sqrt(k-1) at every size k, so nothing of size <= 6 attains "
          "sqrt6 and the minimum singular support is 7"
          % (tot, counts),
          tot == 1391280
          and counts == {2: 192, 3: 960, 4: 5360, 5: 31680, 6: 191104, 7: 1161984}
          and ok_small and all(len(hits[k]) == 0 for k in range(2, 7))
          and key_ok and small_census_control())
    print("EXECUTED_CENSUS_KEYS",key_report)
    check("E5 [exact set equality] at size 7 exactly %d of the %d connected sets attain sqrt6 and "
          "they are precisely the %d closed corner stars: %s"
          % (len(hits[7]), counts[7], len(st), got7 == set(st)),
          len(hits[7]) == 64 and got7 == set(st))
    Vp, hp, _, flp, polp = torus(L, (0, 0, 0))
    wp = np.linalg.eigvalsh(hp)
    nz = int(np.sum(np.abs(wp) < 1e-9))
    check("E6 [numerical, 1e-9] the periodic 4^3 sector has no unique sea to ask about: Polyakov "
          "loops %s, %d exact zero modes at q = (pi,pi,pi), Fermi gap %.1e, so no single P"
          % (polp, nz, float(wp[Vp // 2] - wp[Vp // 2 - 1])),
          set(flp) == {-1} and polp == [1, 1, 1] and nz == 8
          and abs(wp[Vp // 2] - wp[Vp // 2 - 1]) < 1e-9)
    T,d,mins,nostar=exact_nonstar_certificate(h)
    check("E7 [exact] minimum cardinality is not all inclusion-minimal supports: eleven-site T=%s, "
          "det=%s, positive deletion minors=%s, no contained star=%s" % (T,d,{v:str(x) for v,x in mins.items()},nostar),
          d==0 and all(x>0 for x in mins.values()) and nostar)
    return None



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


def declared_families(L, NBR):
    """Two declared fixed families of larger corner sets. No random draw anywhere.

    BALLS(m): for every corner v, the m corners nearest v in the order
      (L1 distance on the torus, then index), for m in 7, 10, 15, 20.
    COLUMN+: for every corner v, the whole z-column through v (L corners) together
      with the two in-plane neighbours of v -- the shape of the slab's minimal
      five-corner sets, transplanted to the torus.
    """
    V = L ** 3

    def coord(v):
        return (v // (L * L), (v // L) % L, v % L)

    def d1(a, b):
        return sum(min((x - y) % L, (y - x) % L) for x, y in zip(coord(a), coord(b)))

    fam = {}
    for m in (7, 10, 15, 20):
        rows = []
        for v in range(V):
            order = sorted(range(V), key=lambda u: (d1(v, u), u))
            rows.append(sorted(order[:m]))
        fam["ball%d" % m] = rows
    rows = []
    for v in range(V):
        x, y, z = coord(v)
        colset = [(x * L + y) * L + zz for zz in range(L)]
        inpl = [u for u in NBR[v] if coord(u)[2] == z]
        rows.append(sorted(set(colset) | set(inpl[:2])))
    fam["column+"] = rows
    return fam


def group_F_L6_L8():
    """6^3 and 8^3: the closed-star family is not found, with historical cutoff failures and separately reported numerical margins."""
    res = {}
    for L, tw_gapped, tw_other in ((6, (0, 0, 0), (1, 1, 1)), (8, (1, 1, 1), (0, 0, 0))):
        V, h, NBR, fl, pol = torus(L, tw_gapped)
        N = V // 2
        w, U, P = projector(h, N)
        h2 = h @ h
        off = float(np.linalg.norm(h2 - np.diag(np.diag(h2))))
        Vo, ho, _, flo, polo = torus(L, tw_other)
        wo = np.linalg.eigvalsh(ho)
        res[L] = dict(V=V, h=h, P=P, NBR=NBR, w=w, off=off, fl=fl, pol=pol,
                      gap=float(w[N] - w[N - 1]),
                      nz_other=int(np.sum(np.abs(wo) < 1e-9)), pol_other=polo,
                      gap_other=float(wo[Vo // 2] - wo[Vo // 2 - 1]), tw=tw_gapped,
                      tw_other=tw_other)
    check("F1 [numerical, 1e-9] the gapped sector is twist %s at 6^3 (gap %.9f) and %s at 8^3 "
          "(gap %.9f), the other twist giving %d and %d zero modes at gap 0 -- an independent "
          "reproduction of the determinantal note's optimal twists (1,1,1),(0,0,0),(1,1,1)"
          % (res[6]["tw"], res[6]["gap"], res[8]["tw"], res[8]["gap"],
             res[6]["nz_other"], res[8]["nz_other"]),
          res[6]["tw"] == (0, 0, 0) and res[8]["tw"] == (1, 1, 1)
          and res[6]["gap"] > 3.4 and res[8]["gap"] > 2.6
          and res[6]["nz_other"] == 8 and res[8]["nz_other"] == 8
          and res[6]["gap_other"] < 1e-9 and res[8]["gap_other"] < 1e-9)
    check("F2 [numerical, 1e-9] neither gapped sector is flat: ||offdiag(h^2)|| = %.3e on 6^3 and "
          "%.3e on 8^3. For L >= 6, v+2e_a and v-2e_a differ and each is reached by one 2-path, so "
          "nothing cancels" % (res[6]["off"], res[8]["off"]),
          res[6]["off"] > 1.0 and res[8]["off"] > 1.0)
    lines = []
    for L in (6, 8):
        d = res[L]
        st = sorted(set(tuple(sorted([v] + list(d["NBR"][v]))) for v in range(d["V"])))
        dets = [abs(float(np.linalg.det(d["P"][np.ix_(list(T), list(T))]))) for T in st]
        c = np.zeros(d["V"])
        lam = float(d["w"][-1])
        c[:] = d["h"][:, 0]
        c[0] += lam
        cres = float(np.linalg.norm(d["h"] @ c - lam * c) / np.linalg.norm(c))
        lines.append((len(st), min(dets), max(dets), sum(1 for x in dets if x < DET_TOL), cres))
    check("F3 [numerical, 1e-12] all closed corner star minors exceed the declared cutoff in either gapped sector: "
          "det P_star is uniformly %.3e over all %d stars of 6^3 and %.3e over all %d of 8^3, and "
          "(lambda_max + h) e_v fails with relative residual %.3f and %.3f"
          % (lines[0][1], lines[0][0], lines[1][1], lines[1][0], lines[0][4], lines[1][4]),
          lines[0][0] == 216 and lines[1][0] == 512
          and abs(lines[0][1] - 3.323e-04) < 1e-6 and lines[0][2] - lines[0][1] < 1e-9
          and abs(lines[1][1] - 3.756e-04) < 1e-6 and lines[1][2] - lines[1][1] < 1e-9
          and lines[0][3] == 0 and lines[1][3] == 0
          and lines[0][4] > 1.0 and lines[1][4] > 1.0)
    scan = {}
    scan_keys = {}
    for L, kmax in ((6, 5), (8, 4)):
        d = res[L]
        CS = connected_sets(d["NBR"], d["V"], kmax)
        scan_keys[L]=census_keys_valid(d["NBR"],CS)
        scan[L] = [(k, len(CS[k]), float(batch_absdet(d["P"], CS[k]).min()))
                   for k in sorted(CS)]
    check("F4 [numerical, complete enumeration] every connected corner set of size <= 5 on 6^3 "
          "(%s) and <= 4 on 8^3 (%s): min |det P_T| = %s and %s, per-corner geometric mean "
          "|det P_T|^(1/|T|) never below %.3f -- preserved finite determinant data; "
          "historical geometric-mean diagnostic only; not exact-zero exclusion"
          % ([n for _, n, _ in scan[6]], [n for _, n, _ in scan[8]],
             ["%.3e" % m for _, _, m in scan[6]], ["%.3e" % m for _, _, m in scan[8]],
             min(m ** (1.0 / k) for L in (6, 8) for k, _, m in scan[L])),
          [n for _, n, _ in scan[6]] == [648, 3240, 18576, 115344]
          and [n for _, n, _ in scan[8]] == [1536, 7680, 44032]
          and all(m ** (1.0 / k) > GEO_TOL for k, _, m in scan[6])
          and all(m ** (1.0 / k) > GEO_TOL for k, _, m in scan[8])
          and all(scan_keys[L][0] for L in (6,8)))
    fam = {}
    margin_rows = []
    for L in (6, 8):
        d = res[L]
        F = declared_families(L, d["NBR"])
        fam[L] = []
        for nm in ("ball7", "ball10", "ball15", "ball20", "column+"):
            rows = F[nm]
            mn = min(abs(float(np.linalg.det(d["P"][np.ix_(T, T)]))) for T in rows)
            fam[L].append((nm, len(rows), len(rows[0]), mn))
            vals=np.array([np.linalg.det(d["P"][np.ix_(T,T)]) for T in rows])
            smallest=[]; residual=orth=0.0
            for T in rows:
                A=d["P"][np.ix_(T,T)];ev,Z=np.linalg.eigh(A)
                smallest.append(float(ev[0]))
                residual=max(residual,float(np.linalg.norm(A@Z-Z*ev,ord="fro")))
                orth=max(orth,float(np.linalg.norm(Z.T@Z-np.eye(len(T)),ord="fro")))
            # Conservative numerical diagnostics, not directed-rounding interval proof.
            projres=float(np.linalg.norm(d["h"]@d["P"]-d["P"]@d["h"],ord="fro"))
            idem=float(np.linalg.norm(d["P"]@d["P"]-d["P"],ord="fro"))
            margin_rows.append((L,nm,len(rows),len(rows[0]),int(np.sum(np.abs(vals)<DET_TOL)),
                                min(smallest),residual,orth,projres,idem))
    check("F5 [numerical, declared fixed family, no random draw] BALLS(m) = the m corners nearest "
          "a corner in the order (L1 distance, then index), m = 7,10,15,20, and COLUMN+ = a whole "
          "z-column plus the two in-plane neighbours of one of its sites, one set per corner: min "
          "|det P_T| = %s on 6^3 and %s on 8^3, per-corner geometric mean never below %.3f -- "
          "historical geometric-mean diagnostic only; not exact-zero exclusion"
          % (["%.2e" % m for _, _, _, m in fam[6]], ["%.2e" % m for _, _, _, m in fam[8]],
             min(m ** (1.0 / sz) for L in (6, 8) for _, _, sz, m in fam[L])),
          all(m ** (1.0 / sz) > GEO_TOL for _, _, sz, m in fam[6])
          and all(m ** (1.0 / sz) > GEO_TOL for _, _, sz, m in fam[8])
          and all(n == 216 for _, n, _, _ in fam[6]) and all(n == 512 for _, n, _, _ in fam[8]))


    check("F6 [numerical, historical cutoff retained] actual BALLS20 minors below DET_TOL=1e-12: "
          "%s; these contradict the old universal cutoff claim, despite positive geometric means"
          % [(r[0],r[4]) for r in margin_rows if r[1]=="ball20"],
          [(r[0],r[4]) for r in margin_rows if r[1]=="ball20"]==[(6,36),(8,56)])
    check("F7 [numerical, NEW post-review margin diagnostic] every declared larger-family "
          "principal eigenvalue exceeds 1e-8; all eigensystem/projector residual diagnostics <1e-10; "
          "no directed-rounding or exact nonsingularity certificate is claimed",
          len(margin_rows)==10 and all(r[5]>MARGIN_TOL and max(r[6:])<1e-10 for r in margin_rows))
    print("PRINCIPAL_MARGIN_ROWS",margin_rows)



def main():
    Vc, Ec, Fc, etac = open_block(2, 2, 2)
    C = census(Vc, Ec, Fc, etac, "cube")
    group_A_cube(C)
    Vs, Es, Fs, etas = open_block(2, 2, 3)
    S = census(Vs, Es, Fs, etas, "slab")
    group_B_slab(S)
    group_C_star_rule(C, S)
    group_D_criterion(C, S)
    group_E_torus4()
    group_F_L6_L8()
    print("SUMMARY: a corner set has zero odds for the all-occupied pattern exactly when "
          "det P_T = 0, flatness supplies stars but not all minimal supports. The old determinant cutoff flags BALLS20; the separate margin diagnostic is numerical only.")
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 1 if FAIL else 0


if __name__ == "__main__":
    sys.exit(main())
