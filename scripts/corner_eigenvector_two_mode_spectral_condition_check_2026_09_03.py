#!/usr/bin/env python3
"""The corner eigenvector property is a two-mode spectral condition: exact on flat
bands, not general.

Class-A finite-cluster runner, self-contained. Qubits sit on the EDGE sites of two
finite subgraphs of the cubic lattice: the 2x2x2 cube (8 corners, 12 edge sites, 6
faces) and the 2x2x3 slab -- two stacked cubes -- open in z (12 corners, 20 edge
sites, 11 faces, corner degrees 3 and 4), with the 2x2x3 slab periodic in z (24
edge sites, every corner degree 4) and the 2x2x4 slabs carried at the one-particle
level only. The sites compose ordinarily. A record at an edge site REGISTERS a
Z-value there; the corner parity dictionary n_v = (1 - B_v)/2 registers occupancy
from those records. The slab's record space is 2^20 = 1048576-dimensional and is
touched by SPARSE Pauli-string application and Lanczos only: the many-body operator
is held on the conserved half-filling index set J (473088 of 2^20) as a sparse
matrix, state vectors are ~16 MB, and no dense object above 4096 x 4096 is formed.

THE LAW. eta = the Kawamoto-Smit staggered link signs (eta_x = 1, eta_y = (-1)^x,
eta_z = (-1)^(x+y)), whose product round every face of BOTH clusters is -1: the
all-minus (pi-flux) sector. H = -t sum_e eta_e T_e with T_ij = (i/2) A_ij (B_i -
B_j), t = 1. THE SEA is the ground state of H in the code space at half filling.
H_R is H restricted to a record subspace = the sum of the hop terms on the
UNRECORDED edges, since every hop's Pauli X-part is exactly one edge qubit.

THE QUESTION. PR #7900 found, on the cube, that after a corner's own record set
star(v) forms jointly the conditioned sea is an exact H_R eigenvector at 8 of 8
outcomes, and offered as a candidate wording "Records form together on a corner's
record set; between formations the law runs on." This runner asks WHY that holds
and WHETHER it generalises, and answers both. It narrows a result of the same day:
the narrowing is the point, and it is a narrowing to an exact condition. No
unit, rule or neighbourhood tick is foreclosed anywhere below.

  A  THE SETTING.   Both clusters, the encoding relations R0-R4, the flux sector,
     the seas, and the plain arithmetic of the 2x2xL family.
  B  T1  THE RECORD LAYER FACTORS OUT, exactly on the checked cube/slab incidence.
  C  T2  THE ONE-PARTICLE CRITERION, and why the cube satisfies it.
  D  T3  THE 2x2x3 SLAB: where it holds, where it fails, and by how much.
  E  T4  ROBUSTNESS under declared perturbations.
  F  T5  THE TWO-CORNER MARGINAL IS BLIND; the full record law discriminates.

NO SEEDS ANYWHERE. Nothing is sampled and no random number generator is used. The
Lanczos start vector is the fixed deterministic vector cos(0.7i + 0.3) + i
cos(1.3i + 1.1) projected into the code space, written out below; every
"perturbation" is an EXPLICIT FIXED TABLE written out in this file (SIGN_FLIPS,
ONSITE), not a draw.

Line tags. `[exact]` = integer, F2 or symplectic Pauli arithmetic with no floating
point in the statement. `[numerical, tol]` = a deterministic double-precision
evaluation of an exactly specified quantity at the stated threshold.

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
AUDIT_INPUT_PATHS = ('docs/THE_CORNER_EIGENVECTOR_PROPERTY_IS_A_TWO_MODE_SPECTRAL_CONDITION_EXACT_ON_FLAT_BANDS_NOT_GENERAL_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md')
_EXPECTED_INPUT_SHA256 = {'docs/THE_CORNER_EIGENVECTOR_PROPERTY_IS_A_TWO_MODE_SPECTRAL_CONDITION_EXACT_ON_FLAT_BANDS_NOT_GENERAL_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'b6c32e83e4818adf1511dfa05a345435a5d59597199fbf0fe374bd125e3186f0', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753'}

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

AUDIT_TIMEOUT_SEC = 150

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


# ==========================================================================
# Pauli algebra in the symplectic representation, phases mod 4
# ==========================================================================
def pc(n):
    return bin(n).count("1")


PH = [1 + 0j, 1j, -1 + 0j, -1j]


class P:
    """i^k * prod_q X_q^{x_q} Z_q^{z_q}  (X before Z on every qubit)."""

    __slots__ = ("k", "x", "z")

    def __init__(s, k, x, z):
        s.k = k % 4
        s.x = x
        s.z = z

    def __mul__(a, b):
        return P(a.k + b.k + 2 * pc(a.z & b.x), a.x ^ b.x, a.z ^ b.z)

    def neg(s):
        return P(s.k + 2, s.x, s.z)

    def __eq__(a, b):
        return a.k == b.k and a.x == b.x and a.z == b.z

    def is_herm(s):
        return s.k % 2 == pc(s.x & s.z) % 2

    def is_id(s):
        return s.x == 0 and s.z == 0 and s.k == 0

    def is_mid(s):
        return s.x == 0 and s.z == 0 and s.k == 2


ID = P(0, 0, 0)


def comm(a, b):
    return (pc(a.x & b.z) + pc(a.z & b.x)) % 2 == 0


def parity(x):
    x = x.astype(np.int64)
    for s in (32, 16, 8, 4, 2, 1):
        x = x ^ (x >> s)
    return (x & 1).astype(np.int64)


# ==========================================================================
# Geometry: the 2x2xLz slab, open or periodic in z
# ==========================================================================
def slab(Lx=2, Ly=2, Lz=2, pz=False):
    idx = {(x, y, z): (x * Ly + y) * Lz + z
           for x in range(Lx) for y in range(Ly) for z in range(Lz)}
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
        elif pz and Lz > 2:
            add((x, y, z), (x, y, 0), 2)
    raw.sort(key=lambda t: (t[0], t[1]))
    EDGES = [(i, j) for (i, j, a, p) in raw]
    ETA = {}
    for (i, j, a, p) in raw:
        x, y, z = p
        ETA[(i, j)] = 1 if a == 0 else (-1 if (a == 1 and x & 1) else
                                        (-1 if (a == 2 and (x + y) & 1) else 1))

    def nxt(c, a):
        L = (Lx, Ly, Lz)[a]
        v = list(c)
        if v[a] + 1 < L:
            v[a] += 1
        elif a == 2 and pz and Lz > 2:
            v[a] = 0
        else:
            return None
        return tuple(v)

    FACES = []
    for c in idx:
        for a, b in itertools.combinations(range(3), 2):
            p1, p2 = nxt(c, a), nxt(c, b)
            if p1 is None or p2 is None:
                continue
            p3 = nxt(p1, b)
            if p3 is None or p3 != nxt(p2, a):
                continue
            cyc = (idx[c], idx[p1], idx[p3], idx[p2])
            if len(set(cyc)) == 4:
                FACES.append(cyc)
    return V, EDGES, sorted(set(FACES)), np.array([ETA[e] for e in EDGES], dtype=np.int64)


def hmat(V, EDGES, eta):
    h = np.zeros((V, V))
    for q, (i, j) in enumerate(EDGES):
        h[i, j] = h[j, i] = -float(eta[q])
    return h


def degrees(V, EDGES):
    d = np.zeros(V, dtype=int)
    for (i, j) in EDGES:
        d[i] += 1
        d[j] += 1
    return d


def face_flux(FACES, EDGES, eta):
    EI = {}
    for q, (i, j) in enumerate(EDGES):
        EI[(i, j)] = EI[(j, i)] = q
    return [int(np.prod([eta[EI[(c[t], c[(t + 1) % len(c)])]] for t in range(len(c))]))
            for c in FACES]


# ==========================================================================
# The one-particle layer and THE CRITERION
# ==========================================================================
def sea_proj(h, N):
    w, U = np.linalg.eigh(h)
    W = U[:, :N]
    return w, W @ W.T, W


def criterion(h, N):
    """h e_v in span(e_v, P_W e_v): e_v is a superposition of two spectral directions of h in distinct occupied and empty eigenspaces,
    assuming [h,P_W]=0 and 0<P_vv<1.  Per-site residual, 0 = HOLD."""
    V = h.shape[0]
    w, Pw, _ = sea_proj(h, N)
    Q = np.eye(V) - Pw
    out = []
    for v in range(V):
        e = np.zeros(V)
        e[v] = 1.0
        he = h @ e
        r = 0.0
        for Pr in (Pw, Q):
            a, b = Pr @ he, Pr @ e
            nb = float(b @ b)
            if nb < 1e-24:
                continue
            r = max(r, float(np.linalg.norm(a - (float(b @ a) / nb) * b) /
                             max(np.linalg.norm(he), 1e-30)))
        out.append(r)
    return w, float(w[N] - w[N - 1]), np.array(out)


def trace_pred(h, N, v):
    """The one-particle trace prediction of <H_R> in both branches, with the
    invariance residual ||h_R B - B M|| of the deleted-site subspace."""
    V = h.shape[0]
    _, _, W = sea_proj(h, N)
    e = np.zeros(V)
    e[v] = 1.0
    Rv = np.delete(np.eye(V), v, axis=0)
    hR = Rv @ h @ Rv.T
    a = W.T @ e
    Qn = np.linalg.qr(np.column_stack([a, np.eye(N)]))[0][:, :N]
    W0 = W @ Qn[:, 1:]                       # occupied modes with zero amplitude at v
    out = []
    for B in (Rv @ W0, Rv @ W):
        M = np.linalg.solve(B.T @ B, B.T @ (hR @ B))
        out.append((float(np.trace(M)), float(np.linalg.norm(hR @ B - B @ M))))
    return out


# ==========================================================================
# The encoding, its R0-R4 audit, and the sparse many-body model
# ==========================================================================
class Enc:
    def __init__(self, V, EDGES, FACES):
        self.V, self.EDGES, self.FACES = V, list(EDGES), list(FACES)
        self.NQ = len(EDGES)
        self.EIDX = {}
        for q, (i, j) in enumerate(self.EDGES):
            self.EIDX[(i, j)] = self.EIDX[(j, i)] = q
        self.NBR = {i: sorted(j for (a, b) in self.EDGES
                              for j in ((b,) if a == i else ((a,) if b == i else ())))
                    for i in range(V)}
        self.STAR = {i: [self.EIDX[(i, k)] for k in self.NBR[i]] for i in range(V)}
        self.SMASK = {i: reduce(lambda a, b: a | (1 << b), self.STAR[i], 0) for i in range(V)}
        self.FMASK = [reduce(lambda m, t: m | (1 << self.EIDX[(c[t], c[(t + 1) % len(c)])]),
                             range(len(c)), 0) for c in self.FACES]

    def A_uns(self, i, j):
        x, z = 1 << self.EIDX[(i, j)], 0
        for k in self.NBR[i]:
            if k != j and k < j:
                z ^= 1 << self.EIDX[(i, k)]
        for l in self.NBR[j]:
            if l != i and l < i:
                z ^= 1 << self.EIDX[(j, l)]
        return P(pc(x & z) % 2, x, z)

    def A(self, i, j):
        p = self.A_uns(i, j)
        return p if i < j else p.neg()

    def B(self, i):
        return P(0, 0, self.SMASK[i])

    def loop(self, c):
        return reduce(lambda o, t: o * self.A(c[t], c[(t + 1) % len(c)]), range(len(c)), ID)

    def hop(self, i, j):
        A = self.A(i, j)
        return A * self.B(i), A * self.B(j)


def audit(E):
    R = {}
    A = {e: E.A(*e) for e in E.EDGES}
    Bv = {i: E.B(i) for i in range(E.V)}
    R["R0"] = (all(E.A_uns(i, j) == E.A_uns(j, i) for (i, j) in E.EDGES)
               and all(E.A(j, i) == E.A(i, j).neg() for (i, j) in E.EDGES))
    R["R1"] = (all(A[e].is_herm() and (A[e] * A[e]).is_id() for e in E.EDGES)
               and all(Bv[i].is_herm() and (Bv[i] * Bv[i]).is_id() for i in range(E.V)))
    r2 = all(comm(Bv[i], Bv[j]) for i, j in itertools.combinations(range(E.V), 2))
    r2 &= all(comm(A[e], Bv[v]) != (v in e) for e in E.EDGES for v in range(E.V))
    R["R2"] = bool(r2)
    R["R3"] = all(comm(A[e], A[f]) != (len(set(e) & set(f)) == 1)
                  for e, f in itertools.combinations(E.EDGES, 2))
    S = [E.loop(f) for f in E.FACES]
    r4 = all(s.is_herm() and (s * s).is_id() for s in S)
    r4 &= all(comm(s, A[e]) for s in S for e in E.EDGES)
    r4 &= all(comm(s, Bv[v]) for s in S for v in range(E.V))
    r4 &= all(comm(a, b) for a, b in itertools.combinations(S, 2))
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
    R["k"], R["gens"] = len(gens), gens
    grp = []
    for m in range(1 << len(gens)):
        p = ID
        for t in range(len(gens)):
            if (m >> t) & 1:
                p = p * gens[t]
        grp.append(p)
    R["grp_ok"] = (not any(g.is_mid() for g in grp)) and sum(1 for g in grp if g.x == 0) == 1
    R["code_dim"] = (1 << E.NQ) >> len(gens)
    return R


class Model:
    """H = -t sum_e eta_e T_e on the half-filling sector J, sparse only."""

    def __init__(self, V, EDGES, FACES, eta):
        self.V, self.NQ, self.D = V, len(EDGES), 1 << len(EDGES)
        self.En = Enc(V, EDGES, FACES)
        self.AUD = audit(self.En)
        self.k, self.code_dim = self.AUD["k"], self.AUD["code_dim"]
        Z = np.arange(self.D, dtype=np.int64)
        NV = np.zeros(self.D, dtype=np.int8)
        for v in range(V):
            NV += parity(Z & self.En.SMASK[v]).astype(np.int8)
        self.nfill = V // 2
        self.J = np.flatnonzero(NV == self.nfill).astype(np.int64)
        self.n = len(self.J)
        self.loc = -np.ones(self.D, dtype=np.int64)
        self.loc[self.J] = np.arange(self.n)
        self.xpart_ok = True
        self.AMP = []
        for q, e in enumerate(EDGES):
            P1, P2 = self.En.hop(*e)
            self.xpart_ok &= (P1.x == P2.x == (1 << q))
            s1 = 1 - 2 * parity(self.J & P1.z)
            s2 = 1 - 2 * parity(self.J & P2.z)
            a = 0.5j * (PH[P1.k] * s1 - PH[P2.k] * s2)
            ai = np.round(a.imag).astype(np.int8)
            assert np.max(np.abs(a.real)) < 1e-12 and np.max(np.abs(a.imag - ai)) < 1e-12
            self.AMP.append((-int(eta[q])) * ai)
        self.H = self.sparse(range(self.NQ))

    def sparse(self, qs):
        rows, cols, dat = [], [], []
        for q in qs:
            a = self.AMP[q]
            m = a != 0
            if not m.any():
                continue
            src = np.flatnonzero(m)
            rows.append(self.loc[self.J[src] ^ (1 << q)])
            cols.append(src)
            dat.append(1j * a[src].astype(np.float64))
        if not rows:
            return sp.csr_matrix((self.n, self.n), dtype=complex)
        return sp.coo_matrix((np.concatenate(dat), (np.concatenate(rows), np.concatenate(cols))),
                             shape=(self.n, self.n)).tocsr()

    def H_R(self, Rmask):
        """P_S H P_S = H_R: the hops on the UNRECORDED edges."""
        return self.sparse([q for q in range(self.NQ) if not (Rmask >> q) & 1])

    def apply(self, p, v):
        out = np.zeros_like(v)
        out[self.loc[self.J ^ p.x]] = (1 - 2 * parity(self.J & p.z)) * PH[p.k] * v
        return out

    def proj(self, v):
        for g in self.AUD["gens"]:
            v = 0.5 * (v + self.apply(g, v))
        return v

    def sea(self, diag=None, npolish=250):
        """Lanczos from a DECLARED deterministic start vector (no seed), then shifted
        power steps inside the code space."""
        H = self.H if diag is None else (self.H + sp.diags(diag))
        t = np.arange(self.n, dtype=np.float64)
        v0 = self.proj(np.cos(0.7 * t + 0.3) + 1j * np.cos(1.3 * t + 1.1))
        v0 /= np.linalg.norm(v0)
        w, U = spla.eigsh(H, k=3, which="SA", v0=v0, tol=0, maxiter=20000)
        psi = self.proj(U[:, 0])
        psi /= np.linalg.norm(psi)
        sh = float(np.abs(w).max()) + (0.0 if diag is None else float(np.abs(diag).max())) + 6.0
        for _ in range(npolish):
            psi = self.proj(sh * psi - (H @ psi))
            psi /= np.linalg.norm(psi)
        ev = float(np.real(psi.conj() @ (H @ psi)))
        return ev, psi, float(np.linalg.norm(H @ psi - ev * psi)), H

    def key(self, mask):
        bits = [q for q in range(self.NQ) if (mask >> q) & 1]
        k = np.zeros(self.n, dtype=np.int64)
        for a, q in enumerate(bits):
            k |= ((self.J >> q) & 1) << a
        return k, len(bits)

    def cstar(self, v):
        S = set([v]) | set(self.En.NBR[v])
        return reduce(lambda m, t: m | ((1 << t[0]) if (t[1][0] in S or t[1][1] in S) else 0),
                      enumerate(self.En.EDGES), 0)


def group_resid(key, nk, psi, g):
    """Per-record-sector residual ||g_w - <H_R>_w psi_w|| / ||psi_w||, computed DIRECTLY
    (the difference taken elementwise before summing), and, for contrast, the
    variance form sqrt(<H_R^2> - <H_R>^2) which suffers catastrophic cancellation."""
    nn = np.bincount(key, weights=psi.real ** 2 + psi.imag ** 2, minlength=nk)
    ip = np.bincount(key, weights=psi.real * g.real + psi.imag * g.imag, minlength=nk)
    gg = np.bincount(key, weights=g.real ** 2 + g.imag ** 2, minlength=nk)
    live = nn > 1e-13
    ev = np.zeros(nk)
    ev[live] = ip[live] / nn[live]
    d = g - ev[key] * psi
    r2 = np.bincount(key, weights=d.real ** 2 + d.imag ** 2, minlength=nk)
    res = np.zeros(nk)
    res[live] = np.sqrt(np.maximum(r2[live], 0.0) / nn[live])
    raw = np.zeros(nk)
    raw[live] = (gg[live] - ip[live] ** 2 / nn[live]) / nn[live]
    return live, nn, ev, res, raw


def unit_report(M, psi, mask):
    key, m = M.key(mask)
    g = M.H_R(mask) @ psi
    live, nn, ev, res, raw = group_resid(key, 1 << m, psi, g)
    return (m, int(live.sum()), float(res[live].max()), float(res[live].min()),
            sorted(set(np.round(ev[live], 9).tolist())),
            float(np.sqrt(np.abs(raw[live])).max()), float(raw[live].min()), res)


# ==========================================================================
# A -- the setting: two finite clusters of the physical lattice
# ==========================================================================
CUBE = slab(2, 2, 2)
SLAB = slab(2, 2, 3)
SLABP = slab(2, 2, 3, pz=True)

MC = Model(*CUBE)
MS = Model(*SLAB)

EC, seaC, rC, _ = MC.sea()
ES, seaS, rS, _ = MS.sea()
hC = hmat(CUBE[0], CUBE[1], CUBE[3])
hS = hmat(SLAB[0], SLAB[1], SLAB[3])
hP = hmat(SLABP[0], SLABP[1], SLABP[3])
wC, gapC, crC = criterion(hC, 4)
wS, gapS, crS = criterion(hS, 6)
wP, gapP, crP = criterion(hP, 6)
degC, degS, degP = degrees(CUBE[0], CUBE[1]), degrees(SLAB[0], SLAB[1]), degrees(SLABP[0], SLABP[1])

check(
    "A1 [exact] SETTING. R0-R4 hold pair by pair on both clusters, no -I in the face group, k = %d/%d, code dim "
    "%d/%d; every hop's Pauli X-part is exactly one edge qubit, so P_S H P_S = H_R, the hops on UNRECORDED sites. "
    "Flux -1 on all %d/%d faces (pi flux)."
    % (MC.k, MS.k, MC.code_dim, MS.code_dim, len(CUBE[2]), len(SLAB[2])),
    all(MC.AUD[t] and MS.AUD[t] for t in ("R0", "R1", "R2", "R3", "R4", "grp_ok"))
    and MC.xpart_ok and MS.xpart_ok and (MC.k, MS.k) == (5, 9) and (MC.code_dim, MS.code_dim) == (128, 2048)
    and set(face_flux(CUBE[2], CUBE[1], CUBE[3])) == {-1}
    and set(face_flux(SLAB[2], SLAB[1], SLAB[3])) == {-1}
    and set(face_flux(SLABP[2], SLABP[1], SLABP[3])) == {-1},
)
E24o, E24p = len(slab(2, 2, 4)[1]), len(slab(2, 2, 4, pz=True)[1])
check(
    "A2 [exact] the objects. Cube: 8 corners, 12 edges, 6 faces, all degree 3. The 2x2x3 slab open in z -- two stacked "
    "cubes -- 12 corners, 20 edges, 11 faces, dim 2^20, degree 4 exactly at the middle layer %s and 3 at the other "
    "eight; periodic in z, 24 edges, all degree 4. (2x2x4 has %d/%d edges, so the 20-edge object here is the slab.)"
    % ([int(v) for v in np.flatnonzero(degS == 4)], E24o, E24p),
    (CUBE[0], len(CUBE[1]), len(CUBE[2])) == (8, 12, 6) and set(degC.tolist()) == {3}
    and (SLAB[0], len(SLAB[1]), len(SLAB[2])) == (12, 20, 11) and MS.D == 1 << 20
    and sorted(np.flatnonzero(degS == 4).tolist()) == [1, 4, 7, 10]
    and sorted(set(degS.tolist())) == [3, 4] and len(SLABP[1]) == 24 and set(degP.tolist()) == {4}
    and (E24o, E24p) == (28, 32),
)
check(
    "A3 [numerical, 1e-11] the seas, Lanczos on the sparse half-filling sector (|J| = %d of 2^20, nnz %d) from a "
    "declared deterministic start: E_sea = %.12f = -4 sqrt 3 (cube), %.12f = -(8 + 2 sqrt 2) (slab), each the sum of "
    "the N lowest one-particle levels to %.1e/%.1e; eigen-residuals %.1e/%.1e; Fermi gaps %.6f/%.6f."
    % (MS.n, MS.H.nnz, EC, ES, abs(EC - wC[:4].sum()), abs(ES - wS[:6].sum()), rC, rS, gapC, gapS),
    abs(EC + 4 * np.sqrt(3)) < 1e-9 and abs(ES + (8 + 2 * np.sqrt(2))) < 1e-9
    and abs(EC - wC[:4].sum()) < 1e-11 and abs(ES - wS[:6].sum()) < 1e-11
    and rC < 1e-9 and rS < 1e-9 and MS.n == 473088,
)

# ==========================================================================
# B -- T1: the record layer factors out, exactly
# ==========================================================================
def logical_count(M, v):
    """Subsets T of star(v) whose Z_T commutes with every face stabiliser, and the
    number of syndrome classes they fall into."""
    star = sorted(M.En.STAR[v])
    d = len(star)
    cls, log = {}, []
    for bits in range(1 << d):
        T = reduce(lambda m, a: m | ((1 << star[a]) if (bits >> a) & 1 else 0), range(d), 0)
        syn = tuple(pc(T & fm) % 2 for fm in M.En.FMASK)
        cls.setdefault(syn, []).append((bits, T))
        if not any(syn):
            log.append(T)
    return d, cls, log


CUTS = [(MC, "cube", v) for v in range(8)] + [(MS, "slab", v) for v in range(12)]
LOGOK = all(len(logical_count(M, v)[2]) == 2 and len(logical_count(M, v)[1]) == 1 << (len(M.En.STAR[v]) - 1)
            for (M, _, v) in CUTS)
FACE2 = all(pc(fm & M.En.SMASK[v]) == 2
            for (M, _, v) in CUTS for fm in M.En.FMASK if pc(fm & M.En.SMASK[v]))
check(
    "B1 [exact] T1. A face through v holds exactly TWO of star(v)'s edges, and the actual incidence verifies that of the 2^d subsets T the only LOGICAL "
    "Z_T are T = empty and T = star(v) (= B_v) -- at all %d corners of both clusters, degree 3 and 4 alike -- and the "
    "subsets fall into 2^(d-1) syndrome classes in mutually orthogonal sectors."
    % (len(CUTS),),
    LOGOK and FACE2,
)


def identity_resid(M, psi, v):
    """max | P_w|sea> - 2^-(d-1) (sum_T eps_T Z_T) Pi_{n_v}|sea> | over all outcomes."""
    d, cls, _ = logical_count(M, v)
    star = sorted(M.En.STAR[v])
    reps = [vals[0] for vals in cls.values()]
    zs = [(bits, (1 - 2 * parity(M.J & T)).astype(np.float64)) for (bits, T) in reps]
    Bv = (1 - 2 * parity(M.J & M.En.SMASK[v])).astype(np.float64)
    worst = 0.0
    for w in range(1 << d):
        s = [1 - 2 * ((w >> a) & 1) for a in range(d)]
        sel = np.ones(M.n, dtype=bool)
        for a, q in enumerate(star):
            sel &= (((M.J >> q) & 1) == ((w >> a) & 1))
        phi = 0.5 * (psi + int(np.prod(s)) * Bv * psi)
        rhs = np.zeros_like(psi)
        for (bits, zt) in zs:
            eps = int(np.prod([s[a] for a in range(d) if (bits >> a) & 1])) if bits else 1
            rhs = rhs + eps * zt * phi
        worst = max(worst, float(np.max(np.abs(np.where(sel, psi, 0.0) - 2.0 ** -(d - 1) * rhs))))
    return worst


ID_C0 = identity_resid(MC, seaC, 0)
ID_S1 = identity_resid(MS, seaS, 1)
ID_S0 = identity_resid(MS, seaS, 0)
check(
    "B2 [numerical, 1e-15] T1, the identity, verified directly and not inferred: P_w|sea> = 2^-(d-1) (sum_T eps_T Z_T) "
    "Pi_{n_v}|sea>, Pi_{n_v} = (1 + b_v B_v)/2, at max |LHS - RHS| = %.1e/%.1e/%.1e (cube v=0 d=3; slab v=1 d=4; slab "
    "v=0 d=3) over every outcome -- where the property fails as well as where it holds: an identity about the code."
    % (ID_C0, ID_S1, ID_S0),
    max(ID_C0, ID_S1, ID_S0) < 1e-15,
)
ZT_COMM = all(comm(P(0, 0, T), MC.En.hop(*e)[t]) for v in range(8) for T in logical_count(MC, v)[2]
              for e in MC.En.EDGES if not (MC.En.SMASK[v] >> MC.En.EIDX[e]) & 1 for t in (0, 1))
kC0, mC0 = MC.key(MC.En.SMASK[0])
pC0 = np.bincount(kC0, weights=np.abs(seaC) ** 2, minlength=1 << mC0)
kS1, mS1 = MS.key(MS.En.SMASK[1])
pS1 = np.bincount(kS1, weights=np.abs(seaS) ** 2, minlength=1 << mS1)
check(
    "B3 [numerical, 1e-9] T1, the consequence. Every Z_T commutes with H_R (checked term by term), so P_w|sea> is an "
    "H_R eigenvector iff Pi_{n_v}|sea> is: THE RECORD LAYER IS INERT AND THE QUESTION IS PURELY FERMIONIC. Each "
    "outcome's weight is exactly 2^-d (max |p - 2^-d| = %.1e/%.1e) because <B_v> = 0 at half filling."
    % (float(np.abs(pC0 - 0.125).max()), float(np.abs(pS1 - 0.0625).max())),
    ZT_COMM and float(np.abs(pC0 - 0.125).max()) < 1e-9 and float(np.abs(pS1 - 0.0625).max()) < 1e-9,
)

# ==========================================================================
# C -- T2: the one-particle criterion, and the cube
# ==========================================================================
h2C = hC @ hC
flatC = np.abs(h2C - np.diag(np.diag(h2C))).max() < 1e-12 and float(np.ptp(np.diag(h2C))) < 1e-12
check(
    "C1 [numerical, 1e-12] T2, THE CRITERION: BOTH nonzero occupied and empty conditioned branches are H_R eigenvectors iff h e_v lies in span(e_v, "
    "P_W e_v) -- e_v a superposition of two spectral directions in distinct occupied and empty eigenspaces (both branches). Flat bands "
    "suffice: pi flux cancels the two 2-step paths in each cube face, so h^2 = %.1f I and the criterion residual is "
    "%.1e at every corner."
    % (np.diag(h2C)[0], float(crC.max())),
    flatC and abs(np.diag(h2C)[0] - 3.0) < 1e-12 and float(crC.max()) < 1e-12,
)
HRC = MC.H_R(MC.En.SMASK[0])
gC = HRC @ seaC
liveC, nnC, evC, resC, rawC = group_resid(kC0, 1 << mC0, seaC, gC)
allc = [unit_report(MC, seaC, MC.En.SMASK[v]) for v in range(8)]
EPRED = -3 * np.sqrt(3)
subs = [np.flatnonzero(kC0 == w) for w in range(8)]
ovl, degs = [], []
for s_ in subs:
    blk = HRC[s_][:, s_].toarray()
    ww, UU = np.linalg.eigh(blk)
    degs.append(int(np.sum(ww < ww[0] + 1e-9)))
    v_ = seaC[s_] / np.linalg.norm(seaC[s_])
    ovl.append(float(abs(np.vdot(UU[:, 0], v_)) ** 2))
check(
    "C2 [numerical, 1e-12] T2 on the cube, many-body. All 8 corners x 8 outcomes pass H_R eigenvector residual tests: max "
    "residual %.1e over the 64, at the predicted -(N-1) sqrt 3 = %.9f in BOTH branches; in its own record sector the "
    "conditioned sea is the non-degenerate H_R ground state (deg %d, overlap %.9f)."
    % (max(a[2] for a in allc), EPRED, max(degs), min(ovl)),
    max(a[2] for a in allc) < 1e-12 and all(a[1] == 8 for a in allc)
    and all(abs(x - EPRED) < 1e-9 for a in allc for x in a[4])
    and max(degs) == 1 and min(ovl) > 1 - 1e-9,
)
edgeC = unit_report(MC, seaC, 1 << 0)
faceC = unit_report(MC, seaC, MC.En.FMASK[0])
cstC = unit_report(MC, seaC, MC.cstar(0))
check(
    "C3 [numerical, 1e-12] and the criterion sorts the cube's other units: a single edge is an eigenvector at 0 of %d "
    "(%.4f = 1/sqrt 3), a face at 0 of %d (%.4f), the 9-edge closed corner star at %d of %d (%.1e, <H_R> = %.9f)."
    % (edgeC[1], edgeC[2], faceC[1], faceC[2], cstC[1], cstC[1], cstC[2], cstC[4][0]),
    edgeC[2] > 0.5 and faceC[2] > 0.8 and cstC[2] < 1e-12 and cstC[1] == 448
    and abs(edgeC[2] - 1 / np.sqrt(3)) < 1e-6,
)

# ==========================================================================
# D -- T3: the 2x2x3 slab
# ==========================================================================
h2S = np.diag(hS @ hS)
check(
    "D1 [numerical, 1e-10] T3, PREDICTED IN ADVANCE by a V x V eigendecomposition: HOLD at the four degree-4 middle "
    "corners %s (<= %.1e), FAIL at the other eight (%.3e). The slab's bands are NOT flat (diag(h^2) = %s), so flat "
    "bands are sufficient and not necessary; the two-mode condition is the real statement."
    % ([int(v) for v in np.flatnonzero(crS < 1e-10)], float(crS[crS < 1e-10].max()),
       float(crS[crS > 1e-10].min()), sorted(set(np.round(h2S, 9).tolist()))),
    sorted(np.flatnonzero(crS < 1e-10).tolist()) == [1, 4, 7, 10]
    and float(crS[crS > 1e-10].min()) > 1e-2 and len(set(np.round(h2S, 9).tolist())) == 2,
)
S_v1 = unit_report(MS, seaS, MS.En.SMASK[1])
S_v10 = unit_report(MS, seaS, MS.En.SMASK[10])
S_v0 = unit_report(MS, seaS, MS.En.SMASK[0])
check(
    "D2 [numerical, 1e-12] T3 many-body, sparse on 2^20. The degree-4 corners hold EXACTLY: v=1 and v=10 are H_R "
    "eigenvectors at %d/%d and %d/%d outcomes, max residual %.1e, <H_R> = %.9f = -(6 + 2 sqrt 2). The degree-3 corner "
    "v=0 FAILS at all %d, residual %.6f = (sqrt 2 - 1)/2 -- tenths of the norm, not 1e-6."
    % (S_v1[1], S_v1[1], S_v10[1], S_v10[1], max(S_v1[2], S_v10[2]), S_v1[4][0], S_v0[1], S_v0[2]),
    S_v1[1] == 16 and S_v10[1] == 16 and max(S_v1[2], S_v10[2]) < 1e-12
    and abs(S_v1[4][0] + 6 + 2 * np.sqrt(2)) < 1e-9 and abs(S_v10[4][0] - S_v1[4][0]) < 1e-9
    and S_v0[1] == 8 and abs(S_v0[2] - (np.sqrt(2) - 1) / 2) < 1e-6 and S_v0[3] > 0.2,
)
S_e = unit_report(MS, seaS, 1 << 0)
S_f = unit_report(MS, seaS, MS.En.FMASK[0])
S_c0 = unit_report(MS, seaS, MS.cstar(0))
S_c1 = unit_report(MS, seaS, MS.cstar(1))
check(
    "D3 [numerical, 1e-12] T3, other units on the slab: the 14-edge closed star of v=1 holds at all %d live outcomes "
    "(%.1e, <H_R> = %.9f = -(2 + sqrt 2)); a single edge fails at %.4f = sqrt(3/8), a face at %.4f, and the closed star "
    "of degree-3 v=0 at all %d of %d, up to %.4f -- worse there, not better."
    % (S_c1[1], S_c1[2], S_c1[4][0], S_e[2], S_f[2], S_c0[1], S_c0[1], S_c0[2]),
    S_c1[1] == 15360 and S_c1[2] < 1e-12 and abs(S_c1[4][0] + 2 + np.sqrt(2)) < 1e-9
    and abs(S_e[2] - np.sqrt(3 / 8)) < 1e-6 and S_f[2] > 0.9 and S_c0[2] > S_v0[2] and S_c0[1] == 1024,
)
TP0 = trace_pred(hS, 6, 0)
TP1 = trace_pred(hS, 6, 1)
TPC = trace_pred(hC, 4, 0)
check(
    "D4 [numerical, 1e-9] T3, the one-particle layer predicts the SIZE of the failure. tr h_R on the deleted-site "
    "subspace gives every many-body <H_R> (%.9f cube, %.9f slab v=1, %.9f slab v=0, both branches), and its invariance "
    "residual ||h_R B - B M|| is %.1e/%.1e at the holding corners and %.3e at slab v=0 -- the many-body %.3e to three "
    "digits."
    % (TPC[0][0], TP1[0][0], TP0[0][0], TPC[0][1], TP1[0][1], TP0[0][1], S_v0[2]),
    abs(TPC[0][0] - EPRED) < 1e-9 and abs(TPC[1][0] - EPRED) < 1e-9
    and abs(TP1[0][0] - S_v1[4][0]) < 1e-9 and abs(TP1[1][0] - S_v1[4][0]) < 1e-9
    and abs(TP0[0][0] - S_v0[4][0]) < 1e-9 and max(TPC[0][1], TP1[0][1]) < 1e-12
    and abs(TP0[0][1] - S_v0[2]) < 2e-3,
)
h24o = hmat(*slab(2, 2, 4)[:2], slab(2, 2, 4)[3])
h24p = hmat(*slab(2, 2, 4, pz=True)[:2], slab(2, 2, 4, pz=True)[3])
c24o = criterion(h24o, 8)[2].max()
c24p = criterion(h24p, 8)[2].max()
check(
    "D5 [numerical, 1e-10] T3, SO THE CONDITION IS SPECTRAL, NOT A MATTER OF DEGREE: the PERIODIC 2x2x3 slab is degree "
    "4 at every corner and fails at every corner (%.3e .. %.3e), and both 2x2x4 slabs fail (%.3e open, %.3e periodic), "
    "while the cube is degree 3 throughout and holds."
    % (float(crP.min()), float(crP.max()), c24o, c24p),
    float(crP.min()) > 1e-10 and float(crC.max()) < 1e-12 and c24o > 1e-10 and c24p > 1e-10,
)

# ==========================================================================
# E -- T4: robustness under DECLARED perturbations (explicit fixed tables)
# ==========================================================================
STAG = np.array([(-1.0) ** pc(v) for v in range(8)])          # index popcount = x+y+z parity
SIGN_FLIPS = ((0,), (0, 3, 7))                                 # DECLARED fixed tables
ONSITE = np.array([0.31, -0.17, 0.44, -0.28, 0.05, 0.36, -0.49, 0.22])   # DECLARED fixed table
NC = 4
CUBE_EDGES, CUBE_ETA = CUBE[1], CUBE[3]


def mass_diag(M, coef):
    d = np.zeros(M.n)
    for v in range(M.V):
        d += coef[v] * 0.5 * (1 - (1 - 2 * parity(M.J & M.En.SMASK[v])))
    return d


def perturb(eta, coef):
    """One-particle criterion + many-body residual at cube corner v=0, all 8 outcomes."""
    h = hmat(8, CUBE_EDGES, eta) + (np.diag(coef) if coef is not None else 0.0)
    _, _, cr = criterion(h, NC)
    M = Model(8, CUBE_EDGES, CUBE[2], eta)
    dg = None if coef is None else mass_diag(M, coef)
    E, psi, r, H = M.sea(diag=dg, npolish=800)
    key, m = M.key(M.En.SMASK[0])
    HR = M.H_R(M.En.SMASK[0]) + (sp.diags(dg) if dg is not None else 0)
    live, nn, ev, res, raw = group_resid(key, 1 << m, psi, HR @ psi)
    w1 = np.linalg.eigvalsh(h)
    return float(cr.max()), float(res[live].max()), E, float(w1[:NC].sum()), r


P_UNP = perturb(CUBE_ETA, None)
P_ST3 = perturb(CUBE_ETA, 0.3 * STAG)
P_ST1 = perturb(CUBE_ETA, 1.0 * STAG)
P_UNI = perturb(CUBE_ETA, 0.5 * np.ones(8))
hm3 = hmat(8, CUBE_EDGES, CUBE_ETA) + 0.3 * np.diag(STAG)
h2m = hm3 @ hm3
check(
    "E1 [numerical, 1e-9] T4. A staggered mass preserves the property EXACTLY: it anticommutes with the bipartite h, "
    "so h^2 = (3 + m^2) I stays flat (%.2f I at m = 0.3), criterion %.1e/%.1e and many-body residual at cube v=0 over "
    "all 8 outcomes %.1e/%.1e at m = 0.3/1.0, against %.1e unperturbed; a uniform mass is a trivial shift at fixed N "
    "and also holds (%.1e)."
    % (np.diag(h2m)[0], P_ST3[0], P_ST1[0], P_ST3[1], P_ST1[1], P_UNP[1], P_UNI[1]),
    np.abs(h2m - np.diag(np.diag(h2m))).max() < 1e-12 and abs(np.diag(h2m)[0] - 3.09) < 1e-9
    and max(P_ST3[1], P_ST1[1], P_UNI[1], P_UNP[1]) < 1e-9
    and max(P_ST3[0], P_ST1[0], P_UNI[0], P_UNP[0]) < 1e-9,
)
BRK = []
for tbl in SIGN_FLIPS:
    e2 = CUBE_ETA.copy()
    for q in tbl:
        e2[q] = -e2[q]
    BRK.append(("hop signs %s" % (tbl,), perturb(e2, None)))
for sc in (0.25, 1.0):
    BRK.append(("on-site %.2f x table" % sc, perturb(CUBE_ETA, sc * ONSITE)))
BRK.append(("zero flux", perturb(np.ones(12, dtype=np.int64), None)))
check(
    "E2 [numerical, 1e-9] T4, and it BREAKS for the following fixed perturbation tables -- declared fixed tables, no seeds: hop-sign "
    "flips %s, an on-site table at 0.25 and 1.0, the zero-flux sector. Criterion/many-body pairs: %s. Every "
    "one-particle verdict is reproduced many-body and the residual TRACKS the criterion; each perturbed sea matches "
    "its own one-particle sum to %.1e and its own eigen-equation to %.1e."
    % (SIGN_FLIPS, ", ".join("%s %.3f/%.3f" % (n, r[0], r[1]) for n, r in BRK),
       max(abs(r[2] - r[3]) for _, r in BRK), max(r[4] for _, r in BRK)),
    all(r[0] > 1e-3 and r[1] > 1e-3 for _, r in BRK)
    and all(r[1] > 0.3 * r[0] for _, r in BRK)
    and all(abs(r[2] - r[3]) < 1e-9 and r[4] < 1e-9 for _, r in BRK),
)

# ==========================================================================
# F -- T5: the two-corner marginal is blind
# ==========================================================================
PS = np.abs(seaS) ** 2
SEASUP = int((PS > 1e-14).sum())


def two_corner(va, vb, taus):
    """Form star(va) jointly, run exp(-i tau H_R), form star(vb); then record every
    remaining edge with nothing in between, so the final law is each branch's Born law."""
    kA, mA = MS.key(MS.En.SMASK[va])
    kAB, mAB = MS.key(MS.En.SMASK[va] | MS.En.SMASK[vb])
    HRA = MS.H_R(MS.En.SMASK[va])
    ref8 = np.bincount(kAB, weights=PS, minlength=1 << mAB)
    out = []
    for tau in taus:
        full = np.zeros(MS.n)
        for wa in range(1 << mA):
            sub = np.flatnonzero(kA == wa)
            ps = seaS[sub]
            pa = float(np.vdot(ps, ps).real)
            if pa < 1e-13:
                continue
            ps = ps / np.sqrt(pa)
            e1 = ps if tau == 0.0 else spla.expm_multiply(-1j * tau * HRA[sub][:, sub].tocsc(), ps)
            full[sub] += pa * np.abs(e1) ** 2
        j8 = np.bincount(kAB, weights=full, minlength=1 << mAB)
        out.append((tau, 0.5 * float(np.abs(j8 - ref8).sum()), 0.5 * float(np.abs(full - PS).sum()),
                    int((full > 1e-14).sum())))
    return out, mAB, ref8


TAUS = (0.0, 0.5, 2.0)
HOLD, mAB4, ref4 = two_corner(1, 10, TAUS)
FAILP, mAB3, ref3 = two_corner(0, 11, TAUS)
check(
    "F1 [numerical, 1e-13] T5, THE TWO DECLARED TWO-CORNER MARGINAL TESTS ARE BLIND. Form star(v), run exp(-i tau H_R), form a "
    "disjoint star(w), compare the 8-edge (1,10) or 6-edge (0,11) record law with the sea's: TV = %s at the degree-4 pair (1,10) where the "
    "property holds, %s at the degree-3 pair (0,11) where it fails by 0.207, at tau = %s. Passing it is not evidence."
    % ("/".join("%.1e" % r[1] for r in HOLD), "/".join("%.1e" % r[1] for r in FAILP), list(TAUS)),
    all(r[1] < 1e-13 for r in HOLD) and all(r[1] < 1e-13 for r in FAILP),
)
UNI = []
for (a, b) in ((1, 10), (0, 11), (0, 2)):
    kk, mm = MS.key(MS.En.SMASK[a] | MS.En.SMASK[b])
    pp = np.bincount(kk, weights=PS, minlength=1 << mm)
    UNI.append(float(np.abs(pp - 2.0 ** -mm).max()))


def Bexp(vs):
    s = np.ones(MS.n)
    for v in vs:
        s = s * (1 - 2 * parity(MS.J & MS.En.SMASK[v]))
    return float(np.sum(PS * s))


BV = max(abs(Bexp([v])) for v in range(12))
BVW = [Bexp([1, 10]), Bexp([0, 11]), Bexp([0, 2]), Bexp([0, 1])]
check(
    "F2 [numerical, 1e-12] T5, why: the sea's joint law is uniform on the THREE DECLARED disjoint-star pairs (max |p - "
    "2^-m| = %.1e/%.1e/%.1e at (1,10), (0,11), (0,2)), since the only logical Z_T there are I, B_v, B_w, B_v B_w while "
    "max_v |<B_v>| = %.1e and <B_v B_w> = %.1e/%.1e/%.1e on those non-adjacent pairs (against %.4f on adjacent (0,1)). "
    "Only a non-zero <B_v B_w> could fail that test, and this schedule makes none."
    % (UNI[0], UNI[1], UNI[2], BV, BVW[0], BVW[1], BVW[2], BVW[3]),
    max(UNI) < 1e-12 and BV < 1e-12 and max(abs(x) for x in BVW[:3]) < 1e-12
    and abs(BVW[3] + 0.25) < 1e-9,
)
check(
    "F3 [numerical, 1e-12] T5, what DOES discriminate: the FULL record law. Record every remaining edge and compare "
    "all 2^20 patterns with the sea's: TV = %s where the property holds, against %s at tau = %s where it fails, the "
    "state leaking out of the sea's Z-support by %d patterns (%d against %d)."
    % ("/".join("%.1e" % r[2] for r in HOLD), "/".join("%.3f" % r[2] for r in FAILP[1:]), list(TAUS[1:]),
       FAILP[1][3] - SEASUP, FAILP[1][3], SEASUP),
    all(r[2] < 1e-12 for r in HOLD) and all(r[3] == SEASUP for r in HOLD)
    and all(r[2] > 1e-2 for r in FAILP[1:]) and FAILP[2][2] > FAILP[1][2]
    and FAILP[1][3] == SEASUP + 16384 and SEASUP == 411648,
)
check(
    "F4 [numerical] T5, THE CANCELLATION TRAP, named. One matvec and a bincount give every outcome at once, but via "
    "the variance form <H_R^2> - <H_R>^2 they cancel catastrophically: at the holding corner v=1 that difference is "
    "NEGATIVE (%.1e, an impossible variance) of magnitude %.1e -- the ~1e-6 floor -- where the DIRECT form, differenced "
    "elementwise before summing, gives %.1e. They agree at the failing corner (%.4f vs %.4f)."
    % (S_v1[6], S_v1[5], S_v1[2], S_v0[5], S_v0[2]),
    S_v1[6] < 0 and S_v1[5] > 1e3 * S_v1[2] and S_v1[2] < 1e-12
    and abs(S_v0[5] - S_v0[2]) < 1e-6,
)

_, PS1, _ = sea_proj(hS,6)
key05,m05=MS.key(MS.En.SMASK[0] | MS.En.SMASK[5])
p05=np.bincount(key05,weights=PS,minlength=1<<m05)
expect05=-4*PS1[0,5]**2
check("F5 [numerical, 1e-11] nonadjacent (0,5) has disjoint incident edge sets but is NOT uniform: "
      "P05=%.12f, <B0B5>=%.12f, marginal deviation %.3e" % (PS1[0,5],Bexp([0,5]),np.max(np.abs(p05-2.0**-m05))),
      (MS.En.SMASK[0]&MS.En.SMASK[5])==0 and 5 not in MS.En.NBR[0]
      and abs(PS1[0,5]-(1-np.sqrt(2))/8)<1e-12
      and abs(Bexp([0,5])-expect05)<1e-11 and np.max(np.abs(p05-2.0**-m05))>1e-5
      and (mAB4,mAB3)==(8,6))
print("SUMMARY: the simultaneous two-branch eigenvector condition is a finite supplied-model "
      "spectral statement. Flatness suffices but is not necessary; the declared marginal "
      "tests are blind while another nonadjacent pair is nonuniform. No physical tick follows.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
