#!/usr/bin/env python3
"""The continuum record alphabet keeps the winding phase as record content, the
record-echo law does not support it as a field, and the fibred Born odds
register its sign as a fair coin.

Self-contained class-A runner.  Every object is declared here; nothing is
derived from any axiom.  There is no random number and no seed anywhere: every
field, pattern and formation order is declared arithmetic, and the
"quasi-random" flip patterns are the deterministic frac(x*golden + y*sqrt2).

SOURCE BLOCKS COPIED.  Each helper below reproduces a named block of the H3
scratch campaign (scratchpad/H3/), and is copied so this runner stands alone:

  dot/add/neg/cross/solve_exact/ternary_weights/dirs_of/L_CONT/mean_dir/
  L_HYB/in_support/phase_of/_rots/matvec/rot_rec/SLOTS/circle_dir
        <- h3_common.py, blocks "exact vector helpers" and the exact record
           rules (L_CONT is PR #7926's law verbatim in its branch structure,
           re-implemented there from continuum_abundance_check.py:252-272;
           L_HYB is the H3 probe's variant, not landed anywhere)
  P3/G/XI/EPS/M2S/CHI/Plane/build_H/ingap_modes
        <- h3_common.py, block "cell algebra (H2 conventions)"
  relax_xy_fast/support_residual/winding_number/loop_sites
        <- h3_common.py, block "XY relaxation (L_HYB fixed points)"
  cell_density/analytic_field/torus_pair_field/relaxed_field/
  dilute_dimer_field/check_dimer_support/supercell_gap
        <- h3_b_vortex3d.py, blocks B0-B5
  A1..A4/B4/chain_ops/square_ops/D4/grid/chi_density4/interior_mask/
  analytic_dirs/relax2d/support_check2d/rt_profile
        <- h3_c_recordtime.py, block "H1's operator, verbatim" and C1-C6
  build_table/census/degree_stats  <- h3_a_register.py, block A5
  form_all                         <- h3_a_register.py, block A4
  rho_of_label/born/lam            <- h3_a_register.py, block A6
  flip_step                        <- h3_d_formation.py, block D2

DECLARED REDUCTIONS relative to the source campaign.  (1) H1's record-time
operator D4 is assembled sparse and solved by shift-invert about E = 0 instead
of dense LAPACK; group F1 certifies the two solvers agree on a small square.
(2) The transverse-plane eigenproblems use sparse shift-invert exactly as the
source does.  (3) The largest dense matrix built anywhere is 1152 x 1152 (the
24 x 24 transverse plane of group E); every other dense object is at most
24 x 24.  Sizes are stated in every check label.

GROUPS
  A  T1  the register: the phase readout is record content; the H2 mass couples
         to it covariantly; the node gap is M_0 for every uniform phase; the
         Dirac mass is the cell average of the record-read mass.
  B  T2  the complete support census of L_CONT over all 8^6 neighbourhood
         conditions; the echo lemma; the Gibbs census; formation from no seed
         and from seeds.
  C  T3  the dilute (dimer-superlattice) winding is gapless in the staggered 3D
         matter law and gapped, index-carrying, in H1's record-time operator.
  D  T4  the variant law L_HYB supports the smooth vortex as its own fixed
         point; 2n co-moving modes; the bulk net handedness; the torus pair;
         H1's geometry; the core.
  E  T5  the fibred Born odds register the phase's sign as a fair coin; flip
         patterns; the tilted class map.
  F      solver certificate.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
"""
from __future__ import annotations

import math
import sys
import time
from fractions import Fraction as F
from itertools import combinations, permutations, product

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 300

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


# ===================================================================== h3_common.py
# --- exact vector helpers ------------------------------------------------------
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def smul(s, a):
    return tuple(s * x for x in a)


def cross(a, b):
    return (a[1] * b[2] - a[2] * b[1], a[2] * b[0] - a[0] * b[2], a[0] * b[1] - a[1] * b[0])


def solve_exact(A, b):
    """Exact Gaussian elimination on the augmented matrix; None if not unique."""
    m, n = len(A), len(A[0])
    M = [list(row) + [bb] for row, bb in zip(A, b)]
    piv_cols = []
    r = 0
    for c in range(n):
        p = None
        for i in range(r, m):
            if M[i][c] != 0:
                p = i
                break
        if p is None:
            continue
        M[r], M[p] = M[p], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        piv_cols.append(c)
        r += 1
        if r == m:
            break
    for i in range(r, m):
        if M[i][n] != 0:
            return None
    if len(piv_cols) < n:
        return None
    x = [F(0)] * n
    for i, c in enumerate(piv_cols):
        x[c] = M[i][n]
    return x


def ternary_weights(n1, n2, n3):
    A = [[n1[0], n2[0], n3[0]], [n1[1], n2[1], n3[1]], [n1[2], n2[2], n3[2]], [F(1), F(1), F(1)]]
    c = solve_exact(A, [F(0), F(0), F(0), F(2)])
    if c is None or any(x <= 0 for x in c):
        return None
    return c


def dirs_of(cond):
    """Multiset of recorded Bloch directions (reading R1: a cI record has none)."""
    return [rec[2] for rec in cond if rec[0] == "P"]


def L_CONT(cond):
    """PR #7926's record-echo law, verbatim in its branch structure (list count)."""
    ms = dirs_of(cond)
    if len(ms) == 1:
        m = ms[0]
        return (("P", F(1), m), ("P", F(1), neg(m)))
    if len(ms) == 3:
        c = ternary_weights(*ms)
        if c is not None:
            return tuple(("P", c[k], ms[k]) for k in range(3))
        return (("I", F(1)),)
    if len(ms) == 2:
        a = (1 + dot(ms[0], ms[1])) / 2
        if 0 < a < 1:
            return (("I", a), ("I", 1 - a))
        return (("I", F(1)),)
    return (("I", F(1)),)


def mean_dir(ms):
    v = (F(0), F(0), F(0))
    for m in ms:
        v = add(v, m)
    return v, dot(v, v)


def L_HYB(cond):
    """The H3 probe's variant: L_CONT on 1-3 recorded directions, otherwise the
    binary resolution {P(vhat), P(-vhat)} of the neighbour mean v (v = 0 -> {I}).
    Returned symbolically as ("PDIR", v).  Not landed anywhere."""
    ms = dirs_of(cond)
    if 1 <= len(ms) <= 3:
        return L_CONT(cond)
    v, v2 = mean_dir(ms)
    if v2 == 0:
        return (("I", F(1)),)
    return (("PDIR", v),)


def in_support(rec, S):
    for it in S:
        if it[0] == "PDIR":
            if rec[0] != "P" or rec[1] != 1:
                continue
            if cross(rec[2], it[1]) == (0, 0, 0):
                return True
            continue
        if it[0] == rec[0] and it[1] == rec[1] and (it[0] == "I" or it[2] == rec[2]):
            return True
    return False


def phase_of(rec, e1=(F(1), F(0), F(0)), e2=(F(0), F(1), F(0))):
    """The phase readout (cos phi, sin phi) = (n.e1, n.e2) on the declared circle."""
    if rec[0] != "P":
        return None
    n = rec[2]
    return (dot(n, e1), dot(n, e2))


def _rots():
    out = []
    for perm in [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]:
        for signs in product([1, -1], repeat=3):
            R = [[F(0)] * 3 for _ in range(3)]
            for i in range(3):
                R[i][perm[i]] = F(signs[i])
            det = (R[0][0] * (R[1][1] * R[2][2] - R[1][2] * R[2][1])
                   - R[0][1] * (R[1][0] * R[2][2] - R[1][2] * R[2][0])
                   + R[0][2] * (R[1][0] * R[2][1] - R[1][1] * R[2][0]))
            if det == 1:
                out.append(R)
    return out


ROTS = _rots()


def matvec(R, v):
    return tuple(sum(R[i][j] * v[j] for j in range(3)) for i in range(3))


def rot_rec(R, rec):
    if rec[0] == "P":
        return ("P", rec[1], matvec(R, rec[2]))
    if rec[0] == "PDIR":
        return ("PDIR", matvec(R, rec[1]))
    return rec


SLOTS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def circle_dir(t):
    """Exact rational unit vector on the x-y great circle; t = tan(phi/2)."""
    d = 1 + t * t
    return ((1 - t * t) / d, 2 * t / d, F(0))


# --- cell algebra (H2 conventions) --------------------------------------------
I2 = np.eye(2)
Xp = np.array([[0, 1], [1, 0]], complex)
Yp = np.array([[0, -1j], [1j, 0]])
Zp = np.diag([1.0, -1.0]).astype(complex)
PAULI = {"I": I2, "X": Xp, "Y": Yp, "Z": Zp}


def P3(s):
    return np.kron(np.kron(PAULI[s[0]], PAULI[s[1]]), PAULI[s[2]])


G = [P3("YII"), P3("ZYI"), P3("ZZY")]
XI = [P3("XII"), P3("ZXI"), P3("ZZX")]
EPS = P3("ZZZ")
M2S = P3("XYX")
CHI = 1j * G[0] @ G[1] @ G[2]


class Plane:
    """Transverse (x, y) plane of coarse sites with the z cell bit b."""

    def __init__(self, Nx, Ny, periodic=False):
        assert Nx % 2 == 0 and Ny % 2 == 0
        self.Nx, self.Ny, self.periodic = Nx, Ny, periodic
        self.D = 2 * Nx * Ny
        xs, ys, bs = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(2), indexing="ij")
        self.x = xs.ravel()
        self.y = ys.ravel()
        self.b = bs.ravel()
        self.cells = [(X, Y) for X in range(Nx // 2) for Y in range(Ny // 2)]

    def idx(self, x, y, b):
        return (x * self.Ny + y) * 2 + b

    def cell_sites(self, X, Y):
        return [self.idx(2 * X + b1, 2 * Y + b2, b3)
                for b1 in range(2) for b2 in range(2) for b3 in range(2)]

    def hop_matrices(self):
        Nx, Ny, idx = self.Nx, self.Ny, self.idx
        rows, cols, vals = [], [], []
        zr, zc, zv = [], [], []
        for x in range(Nx):
            for y in range(Ny):
                for b in range(2):
                    i = idx(x, y, b)
                    if x + 1 < Nx or self.periodic:
                        j = idx((x + 1) % Nx, y, b)
                        rows += [j, i]
                        cols += [i, j]
                        vals += [1.0, 1.0]
                    if y + 1 < Ny or self.periodic:
                        amp = (-1.0) ** x
                        j = idx(x, (y + 1) % Ny, b)
                        rows += [j, i]
                        cols += [i, j]
                        vals += [amp, amp]
                eta3 = (-1.0) ** (x + y)
                i0, i1 = idx(x, y, 0), idx(x, y, 1)
                rows += [i1, i0]
                cols += [i0, i1]
                vals += [eta3, eta3]
                zr += [i0]
                zc += [i1]
                zv += [eta3]
        H0 = sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)
        Zi = sp.csr_matrix((zv, (zr, zc)), shape=(self.D, self.D), dtype=complex)
        return H0, Zi

    def cell_operator(self, O8):
        rows, cols, vals = [], [], []
        nz = np.argwhere(np.abs(O8) > 0)
        for (X, Y) in self.cells:
            s = self.cell_sites(X, Y)
            for i, j in nz:
                rows.append(s[i])
                cols.append(s[j])
                vals.append(O8[i, j])
        return sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)

    def m2_hop_operator(self, m2_site):
        """The body-diagonal hop M2 with each hop's amplitude the MEAN of the two
        endpoint records' m_2 (each hop reads its two records)."""
        rows, cols, vals = [], [], []
        nz = np.argwhere(np.abs(M2S) > 0)
        for (X, Y) in self.cells:
            s = self.cell_sites(X, Y)
            for i, j in nz:
                rows.append(s[i])
                cols.append(s[j])
                vals.append(0.5 * (m2_site[s[i]] + m2_site[s[j]]) * M2S[i, j])
        return sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)

    def neighbours_inplane(self, i):
        x, y, b = self.x[i], self.y[i], self.b[i]
        out = []
        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            xx, yy = x + dx, y + dy
            if self.periodic:
                xx %= self.Nx
                yy %= self.Ny
            elif not (0 <= xx < self.Nx and 0 <= yy < self.Ny):
                continue
            out.append(self.idx(xx, yy, b))
        return out


def build_H(pl, rvec, M0, H0, Zi, e1=(1, 0, 0), e2=(0, 1, 0)):
    """The dressed one-particle Hamiltonian read from the record Bloch vectors."""
    e1 = np.asarray(e1, float)
    e2 = np.asarray(e2, float)
    m1 = M0 * (rvec @ e1)
    m2 = M0 * (rvec @ e2)
    eps = (-1.0) ** (pl.x + pl.y + pl.b)
    Hstat = (H0 + sp.diags(eps * m1) + pl.m2_hop_operator(m2)).tocsr()

    def H(q):
        return (Hstat + Zi * np.exp(-1j * q) + Zi.conj().T * np.exp(1j * q)).tocsr()

    def V(q):
        return (-1j * Zi * np.exp(-1j * q) + 1j * Zi.conj().T * np.exp(1j * q)).tocsr()

    return H, V


def ingap_modes(Hq, k, window):
    E, U = spla.eigsh(Hq, k=k, sigma=0.0, which="LM", tol=1e-12)
    o = np.argsort(E)
    E, U = E[o], U[:, o]
    sel = np.abs(E) < window
    return E[sel], U[:, sel]


# --- XY relaxation (L_HYB fixed points) ---------------------------------------
def relax_xy_fast(pl, n0, pinned, zterm=2.0, tol=1e-14, maxit=200000):
    n = n0.copy()
    nbl = np.array([pl.neighbours_inplane(i) + [i] * (4 - len(pl.neighbours_inplane(i)))
                    for i in range(pl.D)])
    cnt = np.array([len(pl.neighbours_inplane(i)) for i in range(pl.D)])
    pad = 4 - cnt
    free = ~pinned
    for it in range(maxit):
        s = n[nbl].sum(1) - pad[:, None] * n + zterm * n
        norm = np.linalg.norm(s, axis=1)
        new = n.copy()
        m = free & (norm > 0)
        new[m] = s[m] / norm[m, None]
        delta = np.max(np.abs(new - n))
        n = new
        if delta < tol:
            return n, it + 1
    return n, maxit


def support_residual(pl, n, zterm=2.0):
    nbl = [pl.neighbours_inplane(i) for i in range(pl.D)]
    res = np.zeros(pl.D)
    dotp = np.zeros(pl.D)
    for i in range(pl.D):
        v = n[nbl[i]].sum(0) + zterm * n[i]
        vn = np.linalg.norm(v)
        if vn > 0:
            res[i] = np.linalg.norm(np.cross(n[i], v)) / vn
            dotp[i] = n[i] @ v / vn
    return res, dotp


def winding_number(phis):
    d = np.diff(np.append(phis, phis[0]))
    d = (d + np.pi) % (2 * np.pi) - np.pi
    return float(np.sum(d) / (2 * np.pi))


def loop_sites(pl, xc, yc, R, b=0):
    pts = []
    x0, x1 = int(round(xc - R)), int(round(xc + R))
    y0, y1 = int(round(yc - R)), int(round(yc + R))
    for x in range(x0, x1 + 1):
        pts.append((x, y0))
    for y in range(y0 + 1, y1 + 1):
        pts.append((x1, y))
    for x in range(x1 - 1, x0 - 1, -1):
        pts.append((x, y1))
    for y in range(y1 - 1, y0, -1):
        pts.append((x0, y))
    out = []
    for (x, y) in pts:
        if pl.periodic:
            x %= pl.Nx
            y %= pl.Ny
        elif not (0 <= x < pl.Nx and 0 <= y < pl.Ny):
            return None
        out.append(pl.idx(x, y, b))
    return out


# ===================================================================== h3_b_vortex3d.py
M0 = 0.7
WGAP = 0.98 * M0


def cell_density(pl, psi, O8):
    out = np.zeros(len(pl.cells))
    for ci, (X, Y) in enumerate(pl.cells):
        s = pl.cell_sites(X, Y)
        v = psi[s]
        out[ci] = np.real(v.conj() @ O8 @ v)
    return out


def analytic_field(pl, cores):
    r = np.zeros((pl.D, 3))
    for i in range(pl.D):
        ph = 0.0
        for (xc, yc, n) in cores:
            ph += n * np.arctan2(pl.y[i] - yc, pl.x[i] - xc)
        r[i] = [np.cos(ph), np.sin(ph), 0.0]
    return r


def torus_pair_field(pl, cores):
    """Single-valued phase with vorticity 2 pi n at the core plaquettes and integer
    cycle windings: Poisson solve for the stream function, discrete curl, a uniform
    twist making the cycle circulations integers, integration on a spanning tree."""
    Nx, Ny = pl.Nx, pl.Ny
    q = np.zeros((Nx, Ny))
    for (xc, yc, n) in cores:
        q[int(round(xc - 0.5)), int(round(yc - 0.5))] += 2 * np.pi * n
    kx = 2 * np.pi * np.fft.fftfreq(Nx)
    ky = 2 * np.pi * np.fft.fftfreq(Ny)
    lap = 2 * np.cos(kx)[:, None] + 2 * np.cos(ky)[None, :] - 4
    qk = np.fft.fft2(q)
    psik = np.zeros_like(qk)
    m = np.abs(lap) > 1e-12
    psik[m] = qk[m] / lap[m]
    psi = np.real(np.fft.ifft2(psik))
    ux = psi - np.roll(psi, 1, axis=1)
    uy = np.roll(psi, 1, axis=0) - psi
    c0 = (int(round(cores[0][0] - 0.5)), int(round(cores[0][1] - 0.5)))
    if (ux + np.roll(uy, -1, axis=0) - np.roll(ux, -1, axis=1) - uy)[c0] * cores[0][2] < 0:
        ux, uy = -ux, -uy
    cx = ux.sum(0)
    cy = uy.sum(1)
    tx = (np.round(cx.mean() / (2 * np.pi)) * 2 * np.pi - cx.mean()) / Nx
    ty = -cy[0] / Ny
    ux = ux + tx
    uy = uy + ty
    phi = np.zeros((Nx, Ny))
    for x in range(1, Nx):
        phi[x, 0] = phi[x - 1, 0] + ux[x - 1, 0]
    for y in range(1, Ny):
        phi[:, y] = phi[:, y - 1] + uy[:, y - 1]
    circ = ux + np.roll(uy, -1, axis=0) - np.roll(ux, -1, axis=1) - uy
    r = np.zeros((pl.D, 3))
    for i in range(pl.D):
        r[i] = [np.cos(phi[pl.x[i], pl.y[i]]), np.sin(phi[pl.x[i], pl.y[i]]), 0.0]
    return r, circ, uy.sum(1)


def relaxed_field(pl, cores):
    """The L_HYB fixed point: XY relaxation from the analytic field (open plane) or
    from the exact torus pair field (torus), with the boundary ring and the four
    plaquette corners about each core pinned (the core position is supplied)."""
    if pl.periodic:
        n0, circ, cy = torus_pair_field(pl, cores)
        pinned = np.zeros(pl.D, bool)
    else:
        n0 = analytic_field(pl, cores)
        circ = cy = None
        pinned = np.minimum.reduce([pl.x, pl.y, pl.Nx - 1 - pl.x, pl.Ny - 1 - pl.y]) < 0.5
    for (xc, yc, _) in cores:
        pinned |= (np.abs(pl.x - xc) < 0.75) & (np.abs(pl.y - yc) < 0.75)
    n, _ = relax_xy_fast(pl, n0, pinned)
    res, dotp = support_residual(pl, n)
    free = ~pinned
    return n, float(res[free].max()), float(dotp[free].min()), int(free.sum()), circ, cy


def dilute_dimer_field(pl, cores, period=3):
    """The L_CONT-supported field: same-direction x-dimers, everything else
    unrecorded (r = 0)."""
    r = np.zeros((pl.D, 3))
    rec = np.zeros(pl.D, bool)
    for i in range(pl.D):
        x, y, b = pl.x[i], pl.y[i], pl.b[i]
        if b != 0 or y % 2 != 0 or x % period not in (0, 1):
            continue
        if x % period == 1 and x - 1 < 0:
            continue
        if x % period == 0 and x + 1 >= pl.Nx:
            continue
        xm = (x - (x % period)) + 0.5
        ph = sum(n * np.arctan2(y - yc, xm - xc) for (xc, yc, n) in cores)
        r[i] = [np.cos(ph), np.sin(ph), 0.0]
        rec[i] = True
    return r, rec


def check_dimer_support(pl, r, rec):
    """Exact L_CONT support check: every recorded site sees exactly its partner."""
    bad = 0
    nrec = 0
    for i in range(pl.D):
        if not rec[i]:
            continue
        nrec += 1
        recs = [j for j in pl.neighbours_inplane(i) if rec[j]]
        if len(recs) != 1 or not np.allclose(r[recs[0]], r[i]):
            bad += 1
    return nrec, bad


def supercell_gap(M0_, recfn, box, phi=0.0, nq=16):
    """Periodic-supercell Bloch scan of the staggered 3D matter law on a record
    pattern; returns the minimum |E| over the declared q grid."""
    Lx, Ly, Lz = box
    sites = [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]
    idx = {s_: i for i, s_ in enumerate(sites)}
    Dm = len(sites)
    gmin = 1e9
    qs = np.linspace(-np.pi, np.pi, nq, endpoint=False)
    for qx in qs:
        for qy in qs:
            for qz in qs:
                Hm = np.zeros((Dm, Dm), complex)
                for (x, y, z) in sites:
                    i = idx[(x, y, z)]
                    eta = [1.0, (-1) ** x, (-1) ** (x + y)]
                    for a, dv in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                        nx_, ny_, nz_ = x + dv[0], y + dv[1], z + dv[2]
                        ph = 1.0
                        if nx_ == Lx:
                            nx_ = 0
                            ph = np.exp(-1j * qx)
                        if ny_ == Ly:
                            ny_ = 0
                            ph = np.exp(-1j * qy)
                        if nz_ == Lz:
                            nz_ = 0
                            ph = np.exp(-1j * qz)
                        j = idx[(nx_, ny_, nz_)]
                        Hm[j, i] += eta[a] * ph
                        Hm[i, j] += eta[a] * np.conj(ph)
                    if recfn(x, y, z):
                        Hm[i, i] += M0_ * np.cos(phi) * (-1) ** (x + y + z)
                for X in range(Lx // 2):
                    for Y in range(Ly // 2):
                        for Z in range(Lz // 2):
                            for b1 in range(2):
                                for b2 in range(2):
                                    for b3 in range(2):
                                        bb = (1 - b1, 1 - b2, 1 - b3)
                                        si = (2 * X + b1, 2 * Y + b2, 2 * Z + b3)
                                        sj = (2 * X + bb[0], 2 * Y + bb[1], 2 * Z + bb[2])
                                        i, j = idx[si], idx[sj]
                                        m2i = M0_ * np.sin(phi) if recfn(*si) else 0.0
                                        m2j = M0_ * np.sin(phi) if recfn(*sj) else 0.0
                                        ii = b1 * 4 + b2 * 2 + b3
                                        jj = bb[0] * 4 + bb[1] * 2 + bb[2]
                                        Hm[i, j] += 0.5 * (m2i + m2j) * M2S[ii, jj]
                gmin = min(gmin, float(np.min(np.abs(np.linalg.eigvalsh(Hm)))))
    return gmin


# ===================================================================== h3_c_recordtime.py
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]])
S3 = np.diag([1, -1]).astype(complex)
A1 = np.kron(S1, S1)
A2 = np.kron(S1, S2)
A3 = np.kron(S1, S3)
A4 = np.kron(S2, np.eye(2, dtype=complex))
B4 = A1 @ A2 @ A3 @ A4
M_DEF = 0.8
R_S = 1.0


def chain_ops(n):
    """H1's hard-ended chain: K = -i/2 (shift - shift^dag), LAP the Wilson term."""
    k = sp.lil_matrix((n, n), dtype=complex)
    lap = sp.lil_matrix((n, n), dtype=complex)
    for s in range(n - 1):
        k[s, s + 1] += -0.5j
        k[s + 1, s] += 0.5j
        lap[s, s] += 0.5
        lap[s + 1, s + 1] += 0.5
        lap[s, s + 1] += -0.5
        lap[s + 1, s] += -0.5
    lap[0, 0] += 0.5
    lap[n - 1, n - 1] += 0.5
    return k.tocsr(), lap.tocsr()


def square_ops(n1, n2):
    k1, l1 = chain_ops(n1)
    k2, l2 = chain_ops(n2)
    E1 = sp.identity(n1, format="csr", dtype=complex)
    E2 = sp.identity(n2, format="csr", dtype=complex)
    return sp.kron(k1, E2), sp.kron(E1, k2), sp.kron(l1, E2) + sp.kron(E1, l2)


def D4(n1, n2, m1, m2):
    """H1's operator: K_1 a_1 + K_2 a_2 + [diag(m1) + r_s LAP] a_3 + diag(m2) a_4."""
    K1, K2, LAP = square_ops(n1, n2)
    mass1 = sp.diags(np.asarray(m1, dtype=float).ravel()) + R_S * LAP
    mass2 = sp.diags(np.asarray(m2, dtype=float).ravel())
    return (sp.kron(K1, A1) + sp.kron(K2, A2) + sp.kron(mass1, A3) + sp.kron(mass2, A4)).tocsc()


def grid(n1, n2):
    u = np.arange(n1)[:, None] - (n1 - 1) / 2.0
    v = np.arange(n2)[None, :] - (n2 - 1) / 2.0
    return np.broadcast_to(u, (n1, n2)).copy(), np.broadcast_to(v, (n1, n2)).copy()


def chi_density4(evec, idx, n1, n2):
    v = evec[:, idx].reshape(n1 * n2, 4, -1)
    return np.einsum("scm,cd,sdm->s", v.conj(), B4, v).real.reshape(n1, n2)


def interior_mask(n1, n2, pad):
    m = np.zeros((n1, n2), bool)
    m[pad:n1 - pad, pad:n2 - pad] = True
    return m


def analytic_dirs(N, cores):
    u, v = grid(N, N)
    ph = np.zeros((N, N))
    for (uc, vc, n) in cores:
        ph += n * np.arctan2(v - vc, u - uc)
    return np.stack([np.cos(ph), np.sin(ph)], -1)


def relax2d(N, n0, pinned, tol=1e-14, maxit=400000):
    n = n0.copy()
    for it in range(maxit):
        s = np.zeros_like(n)
        s[1:, :] += n[:-1, :]
        s[:-1, :] += n[1:, :]
        s[:, 1:] += n[:, :-1]
        s[:, :-1] += n[:, 1:]
        norm = np.linalg.norm(s, axis=-1)
        new = n.copy()
        m = (~pinned) & (norm > 1e-13)
        new[m] = s[m] / norm[m][:, None]
        delta = np.max(np.abs(new - n))
        n = new
        if delta < tol:
            break
    s = np.zeros_like(n)
    s[1:, :] += n[:-1, :]
    s[:-1, :] += n[1:, :]
    s[:, 1:] += n[:, :-1]
    s[:, :-1] += n[:, 1:]
    return n, np.linalg.norm(s, axis=-1), s


def support_check2d(n, s, pinned):
    norm = np.linalg.norm(s, axis=-1)
    res = np.zeros(norm.shape)
    m = norm > 1e-13
    res[m] = np.abs(n[m][:, 0] * s[m][:, 1] - n[m][:, 1] * s[m][:, 0]) / norm[m]
    return float(res[(~pinned) & m].max()), np.argwhere(~m)


def rt_profile(N, r, cut=0.30, pad=4, k=24):
    """H1's light-cut chirality census, sparse shift-invert about E = 0."""
    D = D4(N, N, M_DEF * r[..., 0], M_DEF * r[..., 1])
    ev, evec = spla.eigsh(D, k=k, sigma=0.0, which="LM", tol=1e-12)
    o = np.argsort(np.abs(ev))
    ev, evec = ev[o], evec[:, o]
    idx = np.where(np.abs(ev) < cut)[0]
    rest = np.abs(ev[np.abs(ev) >= cut])
    nxt = float(rest.min()) if rest.size else float("inf")
    chi = chi_density4(evec, idx, N, N)
    inter = interior_mask(N, N, pad)
    return (len(idx), float(np.max(np.abs(ev[idx]))) if len(idx) else 0.0, nxt,
            float(chi[inter].sum()), float(chi[~interior_mask(N, N, 2)].sum()), float(chi.sum()))


# ===================================================================== h3_a_register.py A4/A5/A6
CUBE = list(product(range(2), repeat=3))
CUBE_NB = {v: [u for u in CUBE if sum(abs(a - b) for a, b in zip(u, v)) == 1] for v in CUBE}


def form_all(seeds, sites):
    """Sequential formation: walk all orders of `sites` and all picks."""
    dirs_seen = set()
    finals = []
    for order in permutations(sites):
        stack = [(0, dict(seeds))]
        while stack:
            i, cfg = stack.pop()
            if i == len(order):
                finals.append(cfg)
                continue
            v = order[i]
            S = L_CONT([cfg[u] for u in CUBE_NB[v] if u in cfg])
            for it in S:
                if it[0] == "P":
                    dirs_seen.add(it[2])
                c2 = dict(cfg)
                c2[v] = it
                stack.append((i + 1, c2))
    return dirs_seen, finals


def build_table(LET, nnb):
    tab = np.zeros((7, 8 ** 7), dtype=bool)
    seen = set()
    for tup in product(range(7), repeat=nnb):
        key = sum(8 ** l for l in tup)
        if key in seen:
            continue
        seen.add(key)
        S = L_CONT([LET[l] for l in tup])
        for i, l in enumerate(LET):
            tab[i, key] = in_support(l, S)
    return tab


def census(nsites, nbr_lists, tab, chunk=1 << 21):
    total = 7 ** nsites
    pw = np.array([8 ** l for l in range(7)], dtype=np.int64)
    nsup = 0
    found = []
    for start in range(0, total, chunk):
        idx = np.arange(start, min(total, start + chunk), dtype=np.int64)
        digs = []
        r = idx.copy()
        for _ in range(nsites):
            digs.append(r % 7)
            r //= 7
        digs = np.array(digs)
        ok = np.ones(idx.shape[0], dtype=bool)
        for s in range(nsites):
            key = np.zeros(idx.shape[0], dtype=np.int64)
            for u in nbr_lists[s]:
                key += pw[digs[u]]
            ok &= tab[digs[s], key]
        nsup += int(ok.sum())
        found.extend(idx[ok].tolist())
    return nsup, found


def degree_stats(found, nsites, nbr_lists):
    degs = {}
    maxdir = 0
    for i in found:
        d = []
        for _ in range(nsites):
            d.append(i % 7)
            i //= 7
        isdir = [l < 6 for l in d]
        maxdir = max(maxdir, sum(isdir))
        for s in range(nsites):
            if isdir[s]:
                k = sum(1 for u in nbr_lists[s] if isdir[u])
                degs[k] = degs.get(k, 0) + 1
    return degs, maxdir


TILT = F(2, 3)


def rho_of_label(l):
    """L_FIB (PR #7926): rho_l = (I + t lhat.sigma)/2 for l a unit lattice direction,
    I/2 otherwise; t = 2/3."""
    if l in [tuple(s) for s in SLOTS]:
        return tuple(TILT * F(x) for x in l)
    return (F(0), F(0), F(0))


def born(r, it):
    if it[0] == "I":
        return it[1]
    return it[1] * (1 + dot(r, it[2])) / 2


def lam(slots):
    v = (0, 0, 0)
    for d in slots:
        v = tuple(a + b for a, b in zip(v, d))
    return v


def flip_step(rho, t):
    """h3_d_formation.py D2: one class tick of the tilted record-value class map."""
    Pk = [F(math.comb(6, k)) * rho ** k * (1 - rho) ** (6 - k) for k in range(7)]
    pplus = (1 + t) / 2
    return (sum(Pk[k] for k in (4, 5, 6)) * pplus
            + sum(Pk[k] for k in (0, 1, 2)) * (1 - pplus)), Pk[3]


# ===================================================================== A -- T1 the register
m1 = circle_dir(F(0))
m2 = circle_dir(F(2))
m3 = circle_dir(F(-2))
ez = (F(0), F(0), F(1))
Pr = lambda c, n: ("P", F(c), n)

cT = ternary_weights(m1, m2, m3)
branches = [
    (L_CONT([Pr(1, m1)]) == (Pr(1, m1), Pr(1, neg(m1)))),
    (L_CONT([Pr(1, m1), Pr(1, m2), Pr(1, m3)])
     == (("P", cT[0], m1), ("P", cT[1], m2), ("P", cT[2], m3))),
    (L_CONT([Pr(1, m1), Pr(1, m2)]) == (("I", F(1, 5)), ("I", F(4, 5)))),
    (L_CONT([Pr(1, m1), Pr(1, m1)]) == (("I", F(1)),)),
    (L_CONT([Pr(1, m1)] * 6) == (("I", F(1)),)),
    (L_CONT([]) == (("I", F(1)),)),
    (L_CONT([("I", F(1))] * 6) == (("I", F(1)),)),
]
check("A1 [exact] L_CONT rebuilt (PR #7926): {m}->binary; {m1,m2,m3}->ternary, weights (%s,%s,%s), "
      "sum 2, weighted sum 0; {m1,m2}->coin (1/5,4/5); {m,m}, 6 equal, empty, I-only -> {I}" % (cT[0], cT[1], cT[2]),
      all(branches) and sum(cT) == 2
      and add(add(smul(cT[0], m1), smul(cT[1], m2)), smul(cT[2], m3)) == (0, 0, 0))

D4dirs = [m1, m2, m3, ez]
nchk = 0
mism = 0
for kk in (1, 2, 3):
    for slots in combinations(range(6), kk):
        for ds in product(D4dirs, repeat=kk):
            cond = {SLOTS[s]: Pr(1, d) for s, d in zip(slots, ds)}
            S = L_CONT(list(cond.values()))
            for R in ROTS:
                condR = {tuple(int(x) for x in matvec(R, tuple(F(a) for a in sl))): rot_rec(R, rc)
                         for sl, rc in cond.items()}
                nchk += 1
                if set(L_CONT(list(condR.values()))) != set(rot_rec(R, it) for it in S):
                    mism += 1
check("A2 [exact] L_CONT covariance S(g.n) = g.S(n) on %d checks (24 rotations x every slot pattern "
      "with 1-3 records from 4 directions): %d mismatches" % (nchk, mism),
      mism == 0 and nchk == 37056)

readouts = []
for t in (F(0), F(1, 2), F(1), F(2), F(-1), F(-1, 2), F(-2)):
    n = circle_dir(t)
    cs = phase_of(Pr(1, n))
    readouts.append(cs == (n[0], n[1]) and cs[0] ** 2 + cs[1] ** 2 == 1)
Rz = [R for R in ROTS if matvec(R, (F(1), F(0), F(0))) == (F(0), F(1), F(0))
      and matvec(R, ez) == ez][0]
cs0 = phase_of(Pr(1, circle_dir(F(1, 2))))
cs1 = phase_of(rot_rec(Rz, Pr(1, circle_dir(F(1, 2)))))
check("A3 [exact] the register: (cos phi, sin phi) = (n.e_1, n.e_2) on the declared circle, exact "
      "at 7 rational points, same at c = 1 and c = 1/2, none for cI; the C_4 sends (3/5,4/5) to "
      "(-4/5,3/5), phi -> phi + pi/2",
      all(readouts)
      and all(phase_of(Pr(F(1, 2), circle_dir(t))) == phase_of(Pr(1, circle_dir(t)))
              for t in (F(0), F(2), F(-2)))
      and phase_of(("I", F(1))) is None and cs1 == (-cs0[1], cs0[0]))


def landed_bloch(q):
    return sum((1 + np.cos(q[a])) * XI[a] + np.sin(q[a]) * G[a] for a in range(3))


Hn = landed_bloch((np.pi, np.pi, np.pi))
gaps = []
for phi in (0.0, 0.7, 2.0):
    ev = np.linalg.eigvalsh(Hn + M0 * np.cos(phi) * EPS + M0 * np.sin(phi) * M2S)
    gaps.append(float(np.max(np.abs(np.abs(ev) - M0))))
check("A4 [1e-12] the H2 mass couples covariantly: for a uniform phase phi = 0, 0.7, 2.0 the node "
      "spectrum is +-M_0 = +-%.1f fourfold, max dev %.1e" % (M0, max(gaps)),
      max(gaps) < 1e-12)

mb = np.array([0.3, -0.1, 0.5, 0.2, 0.0, 0.9, -0.4, 0.6])
epsb = np.array([(-1.0) ** (b1 + b2 + b3) for b1 in range(2) for b2 in range(2) for b3 in range(2)])
coef = float(np.real(np.trace(EPS @ np.diag(epsb * mb))) / 8)
check("A5 [1e-14] the Dirac mass is the cell average of the record-read mass: tr(eps D)/8 = %.6f = "
      "the cell average %.6f, so density d gives Dirac mass d M_0" % (coef, mb.mean()),
      abs(coef - mb.mean()) < 1e-14)

# ===================================================================== B -- T2 the census
D6 = [m1, m2, m3, neg(m1), ez, neg(ez)]
STATES = [None, ("I", F(1))] + [Pr(1, d) for d in D6]
stats = {}
nonecho = 0
for states in product(range(8), repeat=6):
    cond = [STATES[s] for s in states if STATES[s] is not None]
    ms = dirs_of(cond)
    S = L_CONT(cond)
    hasP = any(it[0] == "P" for it in S)
    echo = all(it[2] in ms or neg(it[2]) in ms for it in S if it[0] == "P")
    nonecho += (not echo)
    st = stats.setdefault(len(ms), [0, 0, 0])
    st[0] += 1
    st[1] += hasP
    st[2] += (len(S) == 3)
tot_cond = sum(v[0] for v in stats.values())
check("B1 [exact] complete census over all 8^6 = %d conditions (slots blank, I or P(d), 6 "
      "directions): a rank-one effect is supported for %s of kP = 1 and %d of kP = 3 (the "
      "positively spanning triples), never for kP = 0, 2, 4, 5, 6"
      % (tot_cond, "%d/%d" % (stats[1][1], stats[1][0]), stats[3][1]),
      tot_cond == 262144 and stats[1][1] == stats[1][0] == 1152 and stats[3][1] == 960
      and stats[3][2] == 960 and all(stats[k][1] == 0 for k in (0, 2, 4, 5, 6)))
check("B2 [exact] ECHO LEMMA: every rank-one direction in a support is a neighbour's or its "
      "antipode, %d of %d; a fully recorded bulk site (kP = 6, %d) is an I record"
      % (tot_cond - nonecho, tot_cond, stats[6][0]),
      nonecho == 0 and stats[6][1] == 0 and stats[6][0] == 46656)

LET = [Pr(1, m1), Pr(1, m2), Pr(1, m3), Pr(cT[0], m1), Pr(cT[1], m2), Pr(cT[2], m3), ("I", F(1))]
sites9 = [(x, y) for x in range(3) for y in range(3)]
nb9 = [[sites9.index(((x + dx) % 3, (y + dy) % 3)) for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1))]
       for (x, y) in sites9]
n9, f9 = census(9, nb9, build_table(LET, 4))
degs9, maxdir9 = degree_stats(f9, 9, nb9)
check("B3 [exact] Gibbs census, 3x3 periodic plane, 7 letters: %d of 7^9 = %d supported everywhere, "
      "direction degrees %s, at most %d of 9 directional"
      % (n9, 7 ** 9, {k: degs9[k] for k in sorted(degs9)}, maxdir9),
      n9 == 64 and degs9 == {1: 108, 3: 216} and maxdir9 == 6)

nb8 = [[CUBE.index(u) for u in CUBE_NB[v]] for v in CUBE]
n8, f8 = census(8, nb8, build_table(LET, 3))
degs8, maxdir8 = degree_stats(f8, 8, nb8)
check("B4 [exact] 2x2x2 open cube: %d of 7^8 = %d, degrees %s, at most %d of 8 -- dimers only"
      % (n8, 7 ** 8, {k: degs8[k] for k in sorted(degs8)}, maxdir8),
      n8 == 19 and degs8 == {1: 72} and maxdir8 == 4)

d0, fin0 = form_all({}, CUBE)
check("B5 [exact] from NO seed, every order and pick on the 2x2x2 cube: all 8! = %d form only I "
      "records, %d directions ever offered" % (len(fin0), len(d0)),
      len(fin0) == 40320 and len(d0) == 0
      and all(all(rc[0] == "I" for rc in cfg.values()) for cfg in fin0))

d1, fin1 = form_all({(0, 0, 0): Pr(1, m1)}, [v for v in CUBE if v != (0, 0, 0)])
seed3 = {(0, 0, 0): Pr(1, m1), (1, 1, 0): Pr(1, m2), (1, 0, 1): Pr(1, m3)}
d3, fin3 = form_all(seed3, [v for v in CUBE if v not in seed3])
check("B6 [exact] from seeds it only echoes them: one seed -> %d leaves offering only {m_1, -m_1}; "
      "three seeds -> %d leaves, nothing beyond the seeds and antipodes" % (len(fin1), len(fin3)),
      len(fin1) == 57264 and d1 <= {m1, neg(m1)} and len(fin3) == 2880
      and d3 <= {m1, m2, m3, neg(m1), neg(m2), neg(m3)})

# ===================================================================== C -- T3 the dilute field
PATTERNS = [
    ("uniform control", lambda x, y, z: True, (2, 2, 2)),
    ("x-dimers 1/6", lambda x, y, z: z == 0 and y == 0 and (x % 3) in (0, 1), (6, 2, 2)),
    ("z-dimers 1/3", lambda x, y, z: (x + y) % 2 == 0 and (z % 3) in (0, 1), (2, 2, 6)),
    ("x-dimers 1/8", lambda x, y, z: z == 0 and y == 0 and (x % 4) in (0, 1), (4, 2, 2)),
]
sc = {}
for (nm, fn, box) in PATTERNS:
    for M0_ in (0.7, 1.5):
        for phi in (0.0, np.pi / 2):
            sc[(nm, M0_, phi)] = supercell_gap(M0_, fn, box, phi)
dilute_gaps = [v for (nm, M0_, phi), v in sc.items() if nm != "uniform control"]
check("C1 [1e-9] supercell Bloch scan (16^3) of the 3D matter law: the uniform control is "
      "gapped at %.4f and %.4f, every dimer superlattice (densities 1/6, 1/3, 1/8, both M_0, "
      "phases 0 and pi/2) is GAPLESS, max %.1e over %d"
      % (sc[("uniform control", 0.7, 0.0)], sc[("uniform control", 1.5, 0.0)],
         max(dilute_gaps), len(dilute_gaps)),
      abs(sc[("uniform control", 0.7, 0.0)] - 0.7) < 1e-9
      and abs(sc[("uniform control", 1.5, 0.0)] - 1.5) < 1e-9
      and max(dilute_gaps) < 1e-9)

Nd = 48
pld = Plane(Nd, Nd)
H0d, Zid = pld.hop_matrices()
cd = ((Nd - 1) / 2, (Nd - 1) / 2)
rd, recd = dilute_dimer_field(pld, [(cd[0], cd[1], 1)])
nrecd, badd = check_dimer_support(pld, rd, recd)
Hd, _ = build_H(pld, rd, 1.5, H0d, Zid)
Ed = np.sort(np.abs(spla.eigsh(Hd(np.pi), k=60, sigma=0.0, which="LM", tol=1e-10)[0]))
ru = np.zeros((pld.D, 3))
ru[:, 0] = 1.0
Hu, _ = build_H(pld, ru, 1.5, H0d, Zid)
Eu = float(np.min(np.abs(spla.eigsh(Hu(np.pi), k=6, sigma=0.0, which="LM", tol=1e-10)[0])))
n01 = int(np.sum(Ed < 0.1))
check("C2 [numerical] the dilute winding, 48x48 plane (M_0 = 1.5, %d sites at density 1/6, %d "
      "violations): %d states below |E| = 0.1, smallest %.4f, uniform gap %.4f"
      % (nrecd, badd, n01, Ed[0], Eu),
      badd == 0 and nrecd == 768 and n01 == 7 and Ed[0] < 0.01 and abs(Eu - 1.5027) < 5e-3)

rt_gaps = {}
for Nc in (24, 32):
    rr = np.zeros((Nc, Nc, 2))
    recc = np.zeros((Nc, Nc), bool)
    uu, vv = grid(Nc, Nc)
    for s1 in range(Nc):
        for s2 in range(Nc):
            if s2 % 2 != 0 or s1 % 3 not in (0, 1):
                continue
            if s1 % 3 == 0 and s1 + 1 >= Nc:
                continue
            base = s1 - (s1 % 3)
            ph = np.arctan2(vv[base, s2], 0.5 * (uu[base, s2] + uu[base + 1, s2]))
            rr[s1, s2] = [np.cos(ph), np.sin(ph)]
            recc[s1, s2] = True
    bad = 0
    for s1 in range(Nc):
        for s2 in range(Nc):
            if not recc[s1, s2]:
                continue
            nb = [(s1 + d1, s2 + d2) for d1, d2 in ((1, 0), (-1, 0), (0, 1), (0, -1))
                  if 0 <= s1 + d1 < Nc and 0 <= s2 + d2 < Nc]
            rn = [p for p in nb if recc[p]]
            if len(rn) != 1 or not np.allclose(rr[rn[0]], rr[s1, s2]):
                bad += 1
    ruc = np.zeros((Nc, Nc, 2))
    ruc[recc] = [1.0, 0.0]
    gu = float(np.min(np.abs(spla.eigsh(D4(Nc, Nc, M_DEF * ruc[..., 0], M_DEF * ruc[..., 1]),
                                        k=4, sigma=0.0, which="LM", tol=1e-12)[0])))
    rt_gaps[Nc] = (bad, gu, rt_profile(Nc, rr, cut=0.12, pad=4, k=24))
check("C3 [numerical] the same field in H1's operator (M = 0.8, r_s = 1, hard ends, density 1/3, %d "
      "violations) is GAPPED at %.6f (N = 24), %.6f (N = 32); M/3 = %.4f"
      % (rt_gaps[24][0] + rt_gaps[32][0], rt_gaps[24][1], rt_gaps[32][1], M_DEF / 3),
      rt_gaps[24][0] == 0 and rt_gaps[32][0] == 0
      and abs(rt_gaps[24][1] - 0.267204) < 1e-5 and abs(rt_gaps[32][1] - 0.246455) < 1e-5)
c4 = rt_gaps[32][2]
check("C4 [numerical] and carries the index: N = 32, cut 0.12 -> %d light states, max|E| %.3e (next "
      "%.5f), interior %+.9f, edge %+.9f" % (c4[0], c4[1], c4[2], c4[3], c4[4]),
      c4[0] == 2 and abs(c4[3] - 0.951637) < 1e-4 and c4[4] < -0.8)

# ===================================================================== D -- T4 the variant law
Rl = [3, 5, 7, 9, 11, 14, 18, 22]
plane_res = {}
hR = {}
split = {}
core_E = {}
for N in (24, 32, 48):
    pl = Plane(N, N)
    H0, Zi = pl.hop_matrices()
    c = ((N - 1) / 2, (N - 1) / 2)
    cores = [(c[0], c[1], 1)]
    n, res, dp, nfree, _, _ = relaxed_field(pl, cores)
    wind = [winding_number(np.arctan2(n[L, 1], n[L, 0]))
            for R in (2, 4, 6) for L in [loop_sites(pl, c[0], c[1], R)] if L is not None]
    plane_res[N] = (res, dp, nfree, wind)
    H, V = build_H(pl, n, M0, H0, Zi)
    kk = {24: 40, 32: 60, 48: 110}[N]
    E, U = ingap_modes(H(np.pi + 0.1), kk, WGAP)
    Vq = V(np.pi + 0.1)
    cellpos = np.array([(2 * X + 0.5, 2 * Y + 0.5) for (X, Y) in pl.cells])
    cellr = np.hypot(cellpos[:, 0] - c[0], cellpos[:, 1] - c[1])
    dens = np.zeros(len(pl.cells))
    nL = 0
    for j in range(len(E)):
        if abs(E[j]) < 0.3:
            dens += cell_density(pl, U[:, j], -G[2])
            nL += 1
    hR[N] = ({R: float(dens[cellr < R].sum()) for R in Rl if R < N / 2}, float(dens.sum()), nL)
    core = np.hypot(pl.x - c[0], pl.y - c[1]) < 5
    sel = [j for j in range(len(E)) if (np.abs(U[:, j]) ** 2)[core].sum() > 0.6]
    core_E[N] = (sorted(float(E[j]) for j in sel),
                 [float(np.real(U[:, j].conj() @ (Vq @ U[:, j]))) for j in sel])
    E0, _ = ingap_modes(H(np.pi), 12, WGAP)
    split[N] = float(np.min(np.abs(E0)))
check("D1 [1e-13] L_HYB (this note's variant, not landed) supports the smooth vortex as its own "
      "fixed point: residual %.1e/%.1e/%.1e over %d/%d/%d unpinned sites (N = 24/32/48), "
      "min n.vhat %+.6f, winding +1 on loops 2, 4, 6"
      % (plane_res[24][0], plane_res[32][0], plane_res[48][0],
         plane_res[24][2], plane_res[32][2], plane_res[48][2], plane_res[48][1]),
      all(plane_res[N][0] < 1e-13 and abs(plane_res[N][1] - 1) < 1e-9
          and all(abs(w - 1) < 1e-6 for w in plane_res[N][3]) for N in (24, 32, 48)))
v48 = core_E[48][0][0] / 0.1
check("D2 [numerical] the string carries 2n co-moving modes: %d core modes at E = %s, <V_z> = %s, "
      "v = %.3f; the cut keeps 4 states"
      % (len(core_E[48][0]), " ".join("%+.5f" % e for e in core_E[48][0]),
         " ".join("%+.3f" % v for v in core_E[48][1]), v48),
      len(core_E[48][0]) == 2 and all(abs(e - 0.09983) < 5e-5 for e in core_E[48][0])
      and all(v > 0.99 for v in core_E[48][1]) and hR[48][2] == 4 and hR[32][2] == 4)
check("D3 [numerical] bulk net handedness (cut 0.3): h = %+.4f at R = 14, %+.4f at R = 18 on 48x48, "
      "%+.4f at R = 11 on 32x32; whole plane %.1e, %.1e, %.1e -- the -2n is on the ring"
      % (hR[48][0][14], hR[48][0][18], hR[32][0][11], hR[24][1], hR[32][1], hR[48][1]),
      abs(hR[48][0][14] - 1.9983) < 2e-3 and abs(hR[48][0][18] - 1.9983) < 2e-3
      and abs(hR[32][0][11] - 1.9864) < 2e-3
      and max(abs(hR[N][1]) for N in (24, 32, 48)) < 1e-13)
check("D4 [numerical] the core pair decouples exponentially: p = 0 splitting %.3e, %.3e, %.3e at "
      "N = 24, 32, 48" % (split[24], split[32], split[48]),
      abs(split[24] - 3.125e-3) < 1e-4 and abs(split[32] - 3.991e-4) < 1e-5
      and abs(split[48] - 7.748e-6) < 1e-6 and split[24] > split[32] > split[48])

torus = {}
for (Nx, Ny) in ((48, 24), (64, 32)):
    plt_ = Plane(Nx, Ny, periodic=True)
    H0t, Zit = plt_.hop_matrices()
    cores = [(Nx / 4 - 0.5, Ny / 2 - 0.5, 1), (3 * Nx / 4 - 0.5, Ny / 2 - 0.5, -1)]
    n, res, dp, nfree, circ, cy = relaxed_field(plt_, cores)
    ycyc = sorted(set(np.round(cy / (2 * np.pi), 6).tolist()))
    nvort = 0
    for X in range(plt_.Nx):
        for Y in range(plt_.Ny):
            L = [plt_.idx(X, Y, 0), plt_.idx((X + 1) % plt_.Nx, Y, 0),
                 plt_.idx((X + 1) % plt_.Nx, (Y + 1) % plt_.Ny, 0),
                 plt_.idx(X, (Y + 1) % plt_.Ny, 0)]
            if abs(winding_number(np.arctan2(n[L, 1], n[L, 0]))) > 0.5:
                nvort += 1
    H, V = build_H(plt_, n, M0, H0t, Zit)
    E, U = ingap_modes(H(np.pi + 0.15), 16, WGAP)
    cellpos = np.array([(2 * X + 0.5, 2 * Y + 0.5) for (X, Y) in plt_.cells])
    dens = np.zeros(len(plt_.cells))
    nL = 0
    for j in range(len(E)):
        if abs(E[j]) < 0.3:
            dens += cell_density(plt_, U[:, j], -G[2])
            nL += 1
    hs = []
    for (xc, yc, _) in cores:
        d = np.hypot(cellpos[:, 0] - xc, cellpos[:, 1] - yc)
        hs.append(float(dens[d < 11].sum()))
    torus[(Nx, Ny)] = (res, ycyc, nvort, nL, hs, float(dens.sum()))
check("D5 [numerical] torus: the pair forces a 2 pi winding along the cycle between them -- relaxed "
      "at %.1e/%.1e, y-cycle windings %s, exactly %d/%d vortex plaquettes, 4 light states "
      "carrying %+.4f/%+.4f (48x24), %+.4f/%+.4f (64x32) at r < 11, torus %.1e"
      % (torus[(48, 24)][0], torus[(64, 32)][0], torus[(48, 24)][1], torus[(48, 24)][2],
         torus[(64, 32)][2], torus[(48, 24)][4][0], torus[(48, 24)][4][1],
         torus[(64, 32)][4][0], torus[(64, 32)][4][1], torus[(64, 32)][5]),
      all(torus[t][0] < 1e-13 and torus[t][1] == [0.0, 1.0] and torus[t][2] == 2
          and torus[t][3] == 4 and torus[t][4][0] > 1.97 and torus[t][4][1] < -1.97
          and abs(torus[t][5]) < 1e-13 for t in torus))

Nr = 32
n0r = analytic_dirs(Nr, [(0.0, 0.0, 1)])
pin = np.zeros((Nr, Nr), bool)
pin[0, :] = pin[-1, :] = pin[:, 0] = pin[:, -1] = True
uu, vv = grid(Nr, Nr)
pin |= (np.abs(uu) < 0.75) & (np.abs(vv) < 0.75)
nrel, vnr, srel = relax2d(Nr, n0r, pin)
res2d, zero2d = support_check2d(nrel, srel, pin)
rt32 = rt_profile(Nr, nrel, cut=0.30, pad=4, k=20)
check("D6 [numerical] H1's geometry: the relaxed field is an L_HYB fixed point (residual %.1e) "
      "giving interior %+.9f at N = 32, edge ring %+.9f, net %.1e over %d light states (max|E| "
      "%.1e, next %.5f)" % (res2d, rt32[3], rt32[4], rt32[5], rt32[0], rt32[1], rt32[2]),
      res2d < 1e-13 and abs(rt32[3] - 0.999991511) < 1e-6 and rt32[4] < -0.99
      and abs(rt32[5]) < 1e-9 and rt32[0] == 2)

core4 = [Pr(1, (F(1), F(0), F(0))), Pr(1, (F(0), F(1), F(0))),
         Pr(1, (F(-1), F(0), F(0))), Pr(1, (F(0), F(-1), F(0)))]
Nsc = 25
csc = Nsc // 2
usc, vsc = grid(Nsc, Nsc)
n0s = analytic_dirs(Nsc, [(usc[csc, csc], vsc[csc, csc], 1)])
n0s[csc, csc] = [0.0, 0.0]
pins = np.zeros((Nsc, Nsc), bool)
pins[0, :] = pins[-1, :] = pins[:, 0] = pins[:, -1] = True
pins[csc, csc] = True
nsc, vnsc, ssc = relax2d(Nsc, n0s, pins)
check("D7 [exact] a site-centred core is registered I by BOTH laws (neighbours at 0, 90, 180, 270 "
      "deg, |v_core| = %.1e, relaxed 25x25): the mass zero there is the law's"
      % float(vnsc[csc, csc]),
      L_CONT(core4) == (("I", F(1)),) and L_HYB(core4) == (("I", F(1)),)
      and float(vnsc[csc, csc]) < 1e-18)

# ===================================================================== E -- T5 the fair coin
rows = []
for R in ROTS:
    for i in range(3):
        rows.append([R[i][j] - (F(1) if i == j else F(0)) for j in range(3)])


def rank_exact(rws):
    M = [list(r) for r in rws]
    rk = 0
    for c in range(3):
        p = next((i for i in range(rk, len(M)) if M[i][c] != 0), None)
        if p is None:
            continue
        M[rk], M[p] = M[p], M[rk]
        pv = M[rk][c]
        M[rk] = [x / pv for x in M[rk]]
        for i in range(len(M)):
            if i != rk and M[i][c] != 0:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[rk])]
        rk += 1
    return rk


r6 = rho_of_label(lam(SLOTS))
Sb = L_HYB([Pr(1, m1)] * 6)
check("E1 [exact] the dipole class map sends a fully recorded condition to lambda = %s; the "
      "only Bloch vector fixed by all 24 rotations is 0 (rank %d), so rho = I/2 and the bulk menu "
      "has odds %s, %s -- a fair coin"
      % (str(lam(SLOTS)), rank_exact(rows),
         born(r6, Pr(1, m1)), born(r6, Pr(1, neg(m1)))),
      rank_exact(rows) == 3 and lam(SLOTS) == (0, 0, 0) and Sb[0][0] == "PDIR"
      and born(r6, Pr(1, m1)) == F(1, 2) and born(r6, Pr(1, neg(m1))) == F(1, 2))

rz = rho_of_label(lam([(0, 0, 1)]))
Sd = L_CONT([Pr(1, m1)])
odds_d = [born(rz, it) for it in Sd]
mxz = (F(3, 5), F(0), F(4, 5))
odds_t = [born(rz, it) for it in L_CONT([Pr(1, mxz)])]
odds_ter = [born(r6, it) for it in L_CONT([Pr(1, m1), Pr(1, m2), Pr(1, m3)])]
check("E2 [exact] a dimer with its phase circle normal to the axis (lambda = e_z, t = 2/3) gives "
      "%s, %s; tilted onto the x-z circle %s, %s; ternary odds in the invariant fibre %s = c_k/2"
      % (odds_d[0], odds_d[1], odds_t[0], odds_t[1], ", ".join(str(o) for o in odds_ter)),
      odds_d == [F(1, 2), F(1, 2)] and odds_t == [F(23, 30), F(7, 30)]
      and odds_ter == [cT[0] / 2, cT[1] / 2, cT[2] / 2])

pw = {N: (N * N * math.log10(2), -N * N * math.log10(F(5) / 6)) for N in (24, 32, 48)}
check("E3 [exact] one class tick re-registers the vortex unflipped with odds 2^-N^2 = 10^-%.1f, "
      "10^-%.1f, 10^-%.1f (N = 24, 32, 48); with tilt 2/3, (5/6)^N^2 = 10^-%.1f, 10^-%.1f, 10^-%.1f" % (pw[24][0], pw[32][0], pw[48][0], pw[24][1], pw[32][1], pw[48][1]),
      abs(pw[24][0] - 173.4) < 0.1 and abs(pw[48][0] - 693.6) < 0.1
      and abs(pw[24][1] - 45.6) < 0.1)

Nf = 24
plf = Plane(Nf, Nf)
H0f, Zif = plf.hop_matrices()
cf = ((Nf - 1) / 2, (Nf - 1) / 2)
nf, _, _, _, _, _ = relaxed_field(plf, [(cf[0], cf[1], 1)])
golden = (1 + 5 ** 0.5) / 2
qr = (plf.x * golden + plf.y * 2 ** 0.5) % 1.0
FLIPS = [
    ("none", np.ones(plf.D)),
    ("isolated 1/9", np.where((plf.x % 3 == 0) & (plf.y % 3 == 0), -1.0, 1.0)),
    ("declared ~1/2", np.where(qr < 0.5, -1.0, 1.0)),
    ("declared ~1/6", np.where(qr < 1 / 6, -1.0, 1.0)),
]
flipres = {}
for nm, s in FLIPS:
    Hf, Vf = build_H(plf, nf * s[:, None], M0, H0f, Zif)
    Ef, Uf = ingap_modes(Hf(np.pi + 0.1), 60, WGAP)
    core = np.hypot(plf.x - cf[0], plf.y - cf[1]) < 5
    sel = [j for j in range(len(Ef)) if (np.abs(Uf[:, j]) ** 2)[core].sum() > 0.6]
    flipres[nm] = (float(np.mean(s)), len(sel), [float(Ef[j]) for j in sel])
check("E4a [numerical] a coin-signed field has no string mode: density 1/2 (mean sign %+.3f) leaves "
      "%d core modes on the 24x24 vortex; none (%+.3f) keeps %d at E = %s, 1/9 (%+.3f) keeps %d, "
      "~1/6 (%+.3f) keeps %d"
      % (flipres["declared ~1/2"][0], flipres["declared ~1/2"][1], flipres["none"][0],
         flipres["none"][1], " ".join("%+.5f" % e for e in flipres["none"][2]),
         flipres["isolated 1/9"][0], flipres["isolated 1/9"][1],
         flipres["declared ~1/6"][0], flipres["declared ~1/6"][1]),
      flipres["declared ~1/2"][1] == 0 and flipres["none"][1] == 2
      and flipres["isolated 1/9"][1] == 2 and flipres["declared ~1/6"][1] == 2)

Nq = 24
n0q = analytic_dirs(Nq, [(0.0, 0.0, 1)])
pinq = np.zeros((Nq, Nq), bool)
pinq[0, :] = pinq[-1, :] = pinq[:, 0] = pinq[:, -1] = True
uq, vq = grid(Nq, Nq)
pinq |= (np.abs(uq) < 0.75) & (np.abs(vq) < 0.75)
nq_, _, _ = relax2d(Nq, n0q, pinq)
Xg, Yg = np.meshgrid(np.arange(Nq), np.arange(Nq), indexing="ij")
qrt = (Xg * golden + Yg * 2 ** 0.5) % 1.0
rt_flip = {}
for nm, sg in (("none", np.ones((Nq, Nq))),
               ("isolated 1/9", np.where((Xg % 3 == 0) & (Yg % 3 == 0), -1.0, 1.0)),
               ("declared ~1/2", np.where(qrt < 0.5, -1.0, 1.0)),
               ("declared ~1/6", np.where(qrt < 1 / 6, -1.0, 1.0))):
    rt_flip[nm] = rt_profile(Nq, nq_ * sg[..., None], cut=0.30, pad=4, k=24)
check("E4b [numerical] the coin fills H1's gap: density 1/2 -> %d light states (max|E| %.3f, next "
      "%.3f), interior %+.3f; none -> %d, %+.9f; 1/9 -> %d, %+.9f; ~1/6 -> %d, %+.9f"
      % (rt_flip["declared ~1/2"][0], rt_flip["declared ~1/2"][1], rt_flip["declared ~1/2"][2],
         rt_flip["declared ~1/2"][3], rt_flip["none"][0], rt_flip["none"][3],
         rt_flip["isolated 1/9"][0], rt_flip["isolated 1/9"][3],
         rt_flip["declared ~1/6"][0], rt_flip["declared ~1/6"][3]),
      rt_flip["declared ~1/2"][0] >= 18 and abs(rt_flip["declared ~1/2"][3]) < 0.2
      and rt_flip["none"][0] == 2 and abs(rt_flip["none"][3] - 0.999951757) < 1e-6
      and rt_flip["isolated 1/9"][0] == 2 and rt_flip["isolated 1/9"][3] > 0.99
      and rt_flip["declared ~1/6"][0] == 2 and rt_flip["declared ~1/6"][3] > 0.99)

tilt_rows = []
for t in (F(0), F(1, 3), F(2, 3), F(9, 10)):
    rho = float((1 - t) / 2)
    io = 0.0
    for _ in range(400):
        rr_, io = flip_step(F(rho).limit_denominator(10 ** 9), t)
        rho = float(rr_)
    tilt_rows.append((t, rho, float(io), 1 - 2 * rho - float(io)))
check("E5 [1e-3] a record-value class map with a supplied tilt t: at t = 0 the flip density is "
      "%.4f, I-density %.4f, mean mass %+.4f (a director with a coin); t = 2/3 keeps %+.4f, "
      "t = 9/10 %+.4f"
      % (tilt_rows[0][1], tilt_rows[0][2], tilt_rows[0][3],
         tilt_rows[2][3], tilt_rows[3][3]),
      abs(tilt_rows[0][3]) < 1e-3 and abs(tilt_rows[2][3] - 0.6217) < 1e-3
      and abs(tilt_rows[3][3] - 0.8979) < 1e-3)

# ===================================================================== F -- solver certificate
Nz = 12
rz2 = analytic_dirs(Nz, [(0.0, 0.0, 1)])
Dz = D4(Nz, Nz, M_DEF * rz2[..., 0], M_DEF * rz2[..., 1])
ev_dense = np.linalg.eigvalsh(Dz.toarray())
ev_sp = np.sort(spla.eigsh(Dz, k=20, sigma=0.0, which="LM", tol=1e-12)[0])
near = np.sort(np.abs(ev_dense))[:20]
dev = float(np.max(np.abs(np.sort(np.abs(ev_sp)) - near)))
check("F1 [1e-9] solver certificate: sparse shift-invert agrees with dense LAPACK on a 12x12 "
      "record-time square to %.1e over the 20 nearest zero; largest dense 1152; no seed" % dev,
      dev < 1e-9)

print("SUMMARY: a register; no field under the landed law; a field under a variant; a fair-coin "
      "sign.  [%.1f s]" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
