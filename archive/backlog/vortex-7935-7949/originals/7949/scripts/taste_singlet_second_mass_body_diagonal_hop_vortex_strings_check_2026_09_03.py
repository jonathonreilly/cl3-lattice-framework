#!/usr/bin/env python3
"""The taste-singlet second mass is a body-diagonal imaginary hop, and its
vortex strings carry 2n co-moving modes.

Self-contained one-particle runner on the coarse lattice with one mode per
site and the Kawamoto-Smit signs eta_1 = 1, eta_2 = (-1)^x, eta_3 = (-1)^{x+y}.
The 2x2x2 cell carries bits (b_1, b_2, b_3) = (x, y, z) mod 2, Pauli-string
index 4 b_1 + 2 b_2 + b_3, and the declared cell algebra

    Gamma = (Y1, Z1Y2, Z1Z2Y3)   Xi = (X1, Z1X2, Z1Z2X3)   eps = Z1Z2Z3
    H(q)  = sum_a [(1 + cos q_a) Xi_a + sin q_a Gamma_a]

with the Dirac point at q = (pi, pi, pi), velocities -Gamma_a and chirality
X = i Gamma_1 Gamma_2 Gamma_3 = -Y1X2Y3.  The first mass is the record-native
staggered term m_1 eps_v, eps_v = (-1)^{x+y+z}.  The second mass examined here
is M2 = X1Y2X3 = i Xi_1 Xi_2 Xi_3, and the taste generators are
s = (Y2X3, Y1Z2X3, Y1X2).  Everything is SUPPLIED and declared here; nothing is
derived from any axiom.

Every helper is copied from the source campaign script h2_flux_string.py and
the block it reproduces is named:
  P3, G, XI, EPS, M2S, CHI, TASTE, acomm, comm, nrm, cell_bloch, landed_bloch
      <- "Pauli strings on 3 bits" (source lines 23-61)
  Plane, vortex_fields                       <- "real-space transverse lattice"
                                                (source lines 143-205)
  build_sparse                               <- `build` (source lines 207-217),
                                                kept sparse instead of dense
  string_modes, classify, census, proj_eigs  <- `analyse` (219-240),
                                                `taste_pair_eigs` (242-250) and
                                                `run_vortex` (252-282)
  peierls_flux_tube                          <- `stage_F` (source lines 351-395)
The eigenproblems on the transverse planes use the sparse shift-invert solver
scipy.sparse.linalg.eigsh about E = 0 with a fixed deterministic start vector
(no random numbers and no seed anywhere), followed by a Rayleigh-Ritz
re-diagonalisation of H on the returned span, which makes the vectors of a
near-degenerate pair orthonormal.  A window |E| < E_max is CERTIFIED complete
in two independent ways at every call: the k-th eigenvalue nearest zero lies
outside the window, and the number of states inside it equals a dense LAPACK
eigenvalue count.  The largest dense matrix is 2048 x 2048.

Groups:
  A  T1  the anticommutant of the Dirac-point Clifford set {Gamma, eps} in the
         8x8 cell algebra is exactly four Pauli strings: the taste triplet
         Xi_1, Xi_2, Xi_3 and the taste singlet M2 = X1Y2X3; on the node
         (X, M2, eps) = (tau_3, tau_1, tau_2); gap sqrt(m1^2 + m2^2) exact.
  B  T2  M2 is a body-diagonal hop of Manhattan length 3 with amplitude +-i,
         T-odd and P-odd; the singlet must flip all three cell bits; any
         even-length hop commutes with eps; {M1, M2} = 0 in real space.
  C  T3  the exact square with the taste-splitting cross term.
  D  T4/T5  string modes on open planes with Bloch q_z: 2n co-moving modes per
         winding, one per taste, handedness = eigenvalue of -Gamma_3, <X> = 0,
         the -2n on the outer ring decoupling exponentially with N.
  E  T6  the nearest-neighbour (taste-triplet) second mass gives net zero and
         gaps; the mixed mass obeys n [sgn(a+b) + sgn(a-b)].
  F  T7  string plus anti-string in one plane: +2 and -2 on the cores.
  G  T8  a 2 pi or 4 pi flux tube of the link field with a real mass carries
         no in-gap state.
  S      the solver certificate aggregated over every transverse window.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import sys
import time

import numpy as np
import scipy.linalg as sla
import scipy.sparse as sp
import scipy.sparse.linalg as spla

AUDIT_TIMEOUT_SEC = 150

PASS = 0
FAIL = 0
T0 = time.time()


def check(label, cond):
    """Record and print one check."""
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)


# ------------------------------------------- Pauli strings on 3 bits (source 23-61)
I2 = np.eye(2)
Xp = np.array([[0, 1], [1, 0]], complex)
Yp = np.array([[0, -1j], [1j, 0]])
Zp = np.diag([1., -1.]).astype(complex)
PAULI = {'I': I2, 'X': Xp, 'Y': Yp, 'Z': Zp}


def P3(s):
    """8x8 Pauli string; first letter on bit 1 (x), second on bit 2 (y), third on bit 3 (z)."""
    return np.kron(np.kron(PAULI[s[0]], PAULI[s[1]]), PAULI[s[2]])


G = [P3('YII'), P3('ZYI'), P3('ZZY')]           # Gamma_a
XI = [P3('XII'), P3('ZXI'), P3('ZZX')]          # Xi_a
EPS = P3('ZZZ')
M2S = P3('XYX')                                  # taste-singlet second mass
CHI = 1j * G[0] @ G[1] @ G[2]                    # chirality, = -Y1 X2 Y3
TASTE = [P3('IYX'), P3('YZX'), P3('YXI')]        # s_1, s_2, s_3
LABELS = [a + b + c for a in 'IXYZ' for b in 'IXYZ' for c in 'IXYZ']


def acomm(A, B):
    return A @ B + B @ A


def comm(A, B):
    return A @ B - B @ A


def nrm(A):
    return float(np.max(np.abs(A)))


def flips(s):
    return sum(1 for ch in s if ch in 'XY')


def cell_bloch(q):
    """8x8 Bloch matrix from the real-space hopping rules on a 2x2x2 cell."""
    H = np.zeros((8, 8), complex)
    for b1 in range(2):
        for b2 in range(2):
            for b3 in range(2):
                i = b1 * 4 + b2 * 2 + b3
                x, y = b1, b2
                eta = [1.0, (-1) ** x, (-1) ** (x + y)]
                for a, db in enumerate([(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                    nb = [b1 + db[0], b2 + db[1], b3 + db[2]]
                    if nb[a] == 2:
                        nb[a] = 0
                        ph = np.exp(-1j * q[a])
                    else:
                        ph = 1.0
                    j = nb[0] * 4 + nb[1] * 2 + nb[2]
                    H[j, i] += eta[a] * ph
                    H[i, j] += eta[a] * np.conj(ph)
    return H


def landed_bloch(q):
    return sum((1 + np.cos(q[a])) * XI[a] + np.sin(q[a]) * G[a] for a in range(3))


# ------------------------------------ real-space transverse lattice (source 144-207)
class Plane:
    def __init__(self, Nx, Ny):
        self.Nx, self.Ny = Nx, Ny
        self.D = 2 * Nx * Ny
        xs, ys, bs = np.meshgrid(np.arange(Nx), np.arange(Ny), np.arange(2), indexing='ij')
        self.x = xs.ravel()
        self.y = ys.ravel()
        self.b = bs.ravel()
        self.idx = lambda x, y, b: (x * Ny + y) * 2 + b
        self.cells = [(X, Y) for X in range(Nx // 2) for Y in range(Ny // 2)]

    def cell_sites(self, X, Y):
        return [self.idx(2 * X + b1, 2 * Y + b2, b3)
                for b1 in range(2) for b2 in range(2) for b3 in range(2)]

    def hop_matrices(self, phase=None):
        """(H0: q_z-independent sparse part, Zi: coefficient of e^{-iq} on <b=0|H|b=1>)."""
        Nx, Ny, idx = self.Nx, self.Ny, self.idx
        rows, cols, vals = [], [], []
        zr, zc, zv = [], [], []
        for x in range(Nx):
            for y in range(Ny):
                for b in range(2):
                    i = idx(x, y, b)
                    if x + 1 < Nx:
                        amp = 1.0 * (phase[('x', x, y)] if phase else 1.0)
                        j = idx(x + 1, y, b)
                        rows += [j, i]; cols += [i, j]; vals += [amp, np.conj(amp)]
                    if y + 1 < Ny:
                        amp = (-1) ** x * (phase[('y', x, y)] if phase else 1.0)
                        j = idx(x, y + 1, b)
                        rows += [j, i]; cols += [i, j]; vals += [amp, np.conj(amp)]
                eta3 = (-1) ** (x + y)
                i0, i1 = idx(x, y, 0), idx(x, y, 1)
                rows += [i1, i0]; cols += [i0, i1]; vals += [eta3, eta3]
                zr += [i0]; zc += [i1]; zv += [eta3]
        H0 = sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)
        Zi = sp.csr_matrix((zv, (zr, zc)), shape=(self.D, self.D), dtype=complex)
        return H0, Zi

    def cell_operator(self, O8, weights=None):
        """block-diagonal cell-local operator; weights: dict cell -> scalar (default 1)."""
        rows, cols, vals = [], [], []
        for (X, Y) in self.cells:
            s = self.cell_sites(X, Y)
            wgt = 1.0 if weights is None else weights[(X, Y)]
            for i in range(8):
                for j in range(8):
                    if O8[i, j] != 0:
                        rows.append(s[i]); cols.append(s[j]); vals.append(wgt * O8[i, j])
        return sp.csr_matrix((vals, (rows, cols)), shape=(self.D, self.D), dtype=complex)


def vortex_fields(pl, cores, M0, xi):
    """cores: list of (xc, yc, n).  m1 per site (array), m2 per cell (dict)."""
    def mass_phase(x, y):
        mag = M0
        ph = 0.0
        for (xc, yc, n) in cores:
            r = np.hypot(x - xc, y - yc)
            mag *= np.tanh(r / xi)
            ph += n * np.arctan2(y - yc, x - xc)
        return mag, ph
    m1 = np.zeros(pl.D)
    for i in range(pl.D):
        mag, ph = mass_phase(pl.x[i], pl.y[i])
        m1[i] = mag * np.cos(ph)
    m2 = {}
    for (X, Y) in pl.cells:
        mag, ph = mass_phase(2 * X + 0.5, 2 * Y + 0.5)
        m2[(X, Y)] = mag * np.sin(ph)
    return m1, m2


def build_sparse(pl, m1, m2, M2op, H0, Zi):
    """H(q) = H0 + Zi e^{-iq} + Zi^dag e^{iq} + diag(m1 eps_v) + sum_cells m2 M2op, sparse."""
    eps_diag = ((-1.0) ** (pl.x + pl.y + pl.b)) * m1
    Hstat = (H0 + sp.diags(eps_diag) + pl.cell_operator(M2op, m2)).tocsr()
    Zd = Zi.conj().T.tocsr()

    def H(q):
        return (Hstat + Zi * np.exp(-1j * q) + Zd * np.exp(1j * q)).tocsc()

    def V(q):
        return (-1j * Zi * np.exp(-1j * q) + 1j * Zd * np.exp(1j * q)).tocsr()
    return H, V


# ----------------------------------------------- sparse in-gap solver and observables
CERT = {"count_dev": 0, "dE": 0.0, "res": 0.0, "windows": 0}


def start_vector(D):
    i = np.arange(D)
    return np.cos(0.731 * i) + 0.5j * np.sin(0.277 * i + 0.3) + 0.25


def in_gap(Hq, Emax, k=48):
    """All eigenpairs with |E| < Emax: shift-invert about 0 (k doubled until the k-th
    eigenvalue nearest zero lies outside the window), Rayleigh-Ritz re-diagonalisation
    on the returned span, residuals, and a dense LAPACK count of the same window."""
    while True:
        E, U = spla.eigsh(Hq, k=k, sigma=0.0, which='LM', v0=start_vector(Hq.shape[0]),
                          tol=1e-12, maxiter=20000)
        if np.max(np.abs(E)) > Emax:
            break
        k *= 2
    Q, _ = np.linalg.qr(U)
    Hs = Q.conj().T @ (Hq @ Q)
    E, W = np.linalg.eigh((Hs + Hs.conj().T) / 2)
    U = Q @ W
    sel = np.abs(E) < Emax
    E, U = E[sel], U[:, sel]
    res = max((float(np.linalg.norm(Hq @ U[:, j] - E[j] * U[:, j])) for j in range(len(E))),
              default=0.0)
    Ed = sla.eigvalsh(Hq.toarray())
    Ed = Ed[np.abs(Ed) < Emax]
    CERT["windows"] += 1
    CERT["count_dev"] = max(CERT["count_dev"], abs(len(Ed) - len(E)))
    CERT["res"] = max(CERT["res"], res)
    if len(Ed) == len(E):
        CERT["dE"] = max(CERT["dE"], float(np.max(np.abs(Ed - E))) if len(E) else 0.0)
    return E, U


def string_modes(pl, H, V, ops, cores, Emax, p, Rc=5.0):
    """rows (E, core weights, ring weight, <V_z>, expectations, psi) for the in-gap states at p."""
    ring = np.minimum.reduce([pl.x, pl.y, pl.Nx - 1 - pl.x, pl.Ny - 1 - pl.y]) < 2.5
    masks = [np.hypot(pl.x - xc, pl.y - yc) < Rc for (xc, yc, n) in cores]
    q = np.pi + p
    E, U = in_gap(H(q), Emax)
    Vq = V(q)
    rows = []
    for k in range(len(E)):
        psi = U[:, k]
        dens = np.abs(psi) ** 2
        cw = [float(dens[m].sum()) for m in masks]
        rw = float(dens[ring].sum())
        vel = float(np.real(psi.conj() @ (Vq @ psi)))
        exps = {name: float(np.real(psi.conj() @ (O @ psi))) for name, O in ops.items()}
        rows.append((float(E[k]), cw, rw, vel, exps, psi))
    return rows


def classify(row):
    E, cw, rw, vel, exps, psi = row
    cls = ("core%d" % int(np.argmax(cw))) if max(cw) > 0.6 else ("ring" if rw > 0.6 else "mixed")
    return cls, ('+' if vel > 0 else '-')


def census(rows):
    out = {}
    for r in rows:
        key = classify(r)
        out[key] = out.get(key, 0) + 1
    return out


def net(cen, cls):
    return cen.get((cls, '+'), 0) - cen.get((cls, '-'), 0)


def core_rows(rows, ci=0):
    return sorted([r for r in rows if classify(r)[0] == "core%d" % ci], key=lambda r: r[0])


def proj_eigs(rows, O):
    """eigenvalues of the operator O projected on the span of the given (orthonormal) modes."""
    if not rows:
        return np.array([])
    Psi = np.array([r[5] for r in rows]).T
    M = Psi.conj().T @ (O @ Psi)
    return np.linalg.eigvalsh((M + M.conj().T) / 2)


def make_ops(pl):
    return {'X': pl.cell_operator(CHI), '-G3': pl.cell_operator(-G[2]), 'eps': pl.cell_operator(EPS),
            's1': pl.cell_operator(TASTE[0]), 's2': pl.cell_operator(TASTE[1]),
            's3': pl.cell_operator(TASTE[2])}


def vortex_plane(Nx, Ny, cores, M2op, M0=0.7, xi=2.0):
    pl = Plane(Nx, Ny)
    H0, Zi = pl.hop_matrices()
    m1, m2 = vortex_fields(pl, cores, M0, xi)
    H, V = build_sparse(pl, m1, m2, M2op, H0, Zi)
    return pl, H, V, make_ops(pl)


def fmt(vals, f="%+.5f"):
    return ",".join(f % v for v in vals)


M0, XI_CORE = 0.7, 2.0
EMAX = M0 * 0.98
N24 = 24
C24 = ((N24 - 1) / 2, (N24 - 1) / 2)
ONE = [(C24[0], C24[1], +1)]

# ============================================================== GROUP A -- T1
print("GROUPS A=T1 B=T2 C=T3 D=T4/T5 E=T6 F=T7 G=T8, S=solver; planes 24x24, 16/24/32, 40x24; "
      "M0 = 0.7, xi = 2, Bloch q_z = pi + p, window |E| < %.3f, R_c = 5" % EMAX)
gens = G + XI
cl6 = max(nrm(acomm(gens[i], gens[j]) - (2 * np.eye(8) if i == j else 0))
          for i in range(6) for j in range(6))
eps_ac = max(nrm(acomm(EPS, g)) for g in gens)
qs = [(0.3, 1.1, -2.0), (np.pi, np.pi, np.pi), (2.2, -0.7, 0.4)]
bloch_dev = max(nrm(cell_bloch(q) - landed_bloch(q)) for q in qs)
check("A1 [exact] Cl(6) %.1e; eps anticommutes with all six %.1e; real-space cell rules == landed "
      "H(q) at three momenta %.1e" % (cl6, eps_ac, bloch_dev),
      cl6 == 0.0 and eps_ac == 0.0 and bloch_dev == 0.0)

anti = [s for s in LABELS if all(nrm(acomm(P3(s), g)) < 1e-12 for g in G + [EPS])]
cols = [np.concatenate([acomm(P3(s), g).ravel() for g in G + [EPS]]) for s in LABELS]
nullity = 64 - np.linalg.matrix_rank(np.array(cols).T, tol=1e-9)
singlet = [s for s in anti if all(nrm(comm(P3(s), t)) < 1e-12 for t in TASTE)]
check("A2 [exact] over the complete set of 64 Pauli strings, those anticommuting with Gamma_1,2,3 "
      "and eps are %s (count %d, nullity %d); bit flips %s; the one commuting with all three "
      "tastes (the singlet) is %s"
      % (" ".join(anti), len(anti), nullity, ",".join(str(flips(s)) for s in anti), " ".join(singlet)),
      sorted(anti) == ['XII', 'XYX', 'ZXI', 'ZZX'] and nullity == 4
      and sorted(flips(s) for s in anti) == [1, 1, 1, 3] and singlet == ['XYX'])

m2_props = max(nrm(M2S - M2S.conj().T), nrm(M2S @ M2S - np.eye(8)),
               nrm(M2S - 1j * XI[0] @ XI[1] @ XI[2]))
m2_ac = max(nrm(acomm(M2S, EPS)), max(nrm(acomm(M2S, g)) for g in G), max(nrm(comm(M2S, x)) for x in XI))
chi_props = max(nrm(CHI + P3('YXY')), nrm(CHI @ CHI - np.eye(8)),
                max(nrm(comm(CHI, g)) for g in G), nrm(acomm(CHI, EPS)), nrm(acomm(CHI, M2S)))
tau = nrm(CHI @ M2S - 1j * EPS)
taste_ok = max(max(nrm(comm(s, O)) for s in TASTE for O in G + [EPS, CHI, M2S]),
               nrm(TASTE[0] @ TASTE[1] - 1j * TASTE[2]), nrm(TASTE[1] @ TASTE[2] - 1j * TASTE[0]),
               nrm(TASTE[2] @ TASTE[0] - 1j * TASTE[1]), max(nrm(s @ s - np.eye(8)) for s in TASTE))
trip = max(nrm(XI[0] - M2S @ TASTE[0]), nrm(XI[1] + M2S @ TASTE[1]), nrm(XI[2] - M2S @ TASTE[2]))
check("A3 [exact] M2 = X1Y2X3 = i Xi1Xi2Xi3, hermitian involution %.1e; {M2,eps} = {M2,Gamma_a} = "
      "[M2,Xi_a] = 0 at %.1e; X = -Y1X2Y3 commutes with Gamma_a, anticommutes with eps and M2 "
      "%.1e; X M2 = i eps %.1e -> (X,M2,eps) = (tau_3,tau_1,tau_2) at the node; taste s_b commute "
      "with all %.1e; Xi_b = M2 (s1,-s2,s3)_b %.1e"
      % (m2_props, m2_ac, chi_props, tau, taste_ok, trip),
      max(m2_props, m2_ac, chi_props, tau, taste_ok, trip) == 0.0)

gap_dev = 0.0
for (m1, m2) in [(0.3, 0.4), (0.7, 0.0), (0.0, 0.7), (0.5, -0.5)]:
    ev = np.linalg.eigvalsh(landed_bloch((np.pi, np.pi, np.pi)) + m1 * EPS + m2 * M2S)
    gap_dev = max(gap_dev, nrm(np.abs(ev) - np.hypot(m1, m2)), abs(np.sum(ev > 0) - 4))
check("A4 [1e-14] node spectrum +-sqrt(m1^2+m2^2), fourfold each, for (m1,m2) = (0.3,0.4), (0.7,0), "
      "(0,0.7), (0.5,-0.5): max dev %.1e" % gap_dev, gap_dev < 1e-14)

# ============================================================== GROUP B -- T2
ent = [(i, j) for i in range(8) for j in range(8) if M2S[i, j] != 0]
lengths = sorted(set(bin(i ^ j).count('1') for (i, j) in ent))
amp_dev = max(abs(M2S[j, i] - 1j * (-1) ** ((i >> 1) & 1)) for (j, i) in ent)
check("B1 [exact] M2: %d nonzero entries, each between a cell corner b and its complement (bit "
      "distance %s = Manhattan length 3, the body diagonal), amplitude i(-1)^{b_2} at %.1e, "
      "max|Re M2| %.1e" % (len(ent), lengths, amp_dev, nrm(M2S.real)),
      len(ent) == 8 and lengths == [3] and amp_dev == 0.0 and nrm(M2S.real) == 0.0)

even = [s for s in LABELS if flips(s) % 2 == 0]
odd = [s for s in LABELS if flips(s) % 2 == 1]
even_comm = max(nrm(comm(P3(s), EPS)) for s in even)
odd_ac = max(nrm(acomm(P3(s), EPS)) for s in odd)
short = [s for s in anti if flips(s) < 3]
check("B2 [exact] a hop of displacement d gives the strings flipping the bits where d is odd: all "
      "%d even-flip strings commute with eps (%.1e), all %d odd-flip strings anticommute (%.1e), "
      "so no even-length hop is a mass; the anticommutant elements with fewer than 3 flips are %s, "
      "the nearest-neighbour triplet: no nearest-neighbour or face-diagonal term gives the "
      "singlet" % (len(even), even_comm, len(odd), odd_ac, " ".join(short)),
      even_comm == 0.0 and odd_ac == 0.0 and sorted(short) == ['XII', 'ZXI', 'ZZX'])

t_odd = nrm(M2S.conj() + M2S)
p_odd = nrm(EPS @ M2S @ EPS + M2S)
t_even = max(nrm(EPS.conj() - EPS), nrm(cell_bloch((0.3, 1.1, -2.0)).conj() - cell_bloch((-0.3, -1.1, 2.0))))
check("B3 [exact] M2* = -M2 (T-odd) %.1e; eps M2 eps = -M2 (P-odd) %.1e; eps and the hop T-even "
      "%.1e: (m1, m2) is a scalar + pseudoscalar pair" % (t_odd, p_odd, t_even),
      t_odd == 0.0 and p_odd == 0.0 and t_even == 0.0)

plB = Plane(8, 8)
epsB = sp.diags(((-1.0) ** (plB.x + plB.y + plB.b)).astype(complex))
M2B = plB.cell_operator(M2S)
rr, cc, vv = [], [], []
for x in range(7):
    for y in range(7):
        for b in range(2):
            i, j = plB.idx(x, y, b), plB.idx(x + 1, y + 1, b)
            rr += [i, j]; cc += [j, i]; vv += [1.0, 1.0]
faceB = sp.csr_matrix((vv, (rr, cc)), shape=(plB.D, plB.D), dtype=complex)
ac_real = abs(epsB @ M2B + M2B @ epsB).max()
c_face = abs(epsB @ faceB - faceB @ epsB).max()
check("B4 [exact] real space, 8x8 plane: {diag(eps_v), M2} = %.1e (so {M1, M2} = 0 for any "
      "profiles), while a face-diagonal (1,1,0) hop commutes with diag(eps_v): %.1e"
      % (ac_real, c_face), ac_real == 0.0 and c_face == 0.0)

# ============================================================== GROUP C -- T3
sq_dev = 0.0
for (m1, m2) in ((0.3, 0.4), (0.0, 0.7)):
    for p in (np.array([0.05, -0.03, 0.02]), np.array([0.4, 0.1, -0.3]), np.array([1.0, -0.8, 0.5])):
        Hp = landed_bloch(np.pi + p) + m1 * EPS + m2 * M2S
        pred = ((np.sum(2 - 2 * np.cos(p)) + m1 ** 2 + m2 ** 2) * np.eye(8)
                + 2 * m2 * sum((1 - np.cos(p[a])) * (M2S @ XI[a]) for a in range(3)))
        sq_dev = max(sq_dev, nrm(Hp @ Hp - pred))
check("C1 [1e-14] H(pi+p)^2 = [sum_a(2-2cos p_a) + m1^2 + m2^2] 1 + 2 m2 sum_a (1-cos p_a) M2 Xi_a, "
      "M2 Xi_a = (s1,-s2,s3)_a: max residual %.1e over 3 momenta x 2 mass pairs -- the node gap is "
      "exact, the second mass splits the taste velocities at O(m2)" % sq_dev, sq_dev < 1e-14)

# ============================================================== GROUP D -- T4, T5
pl, H, V, ops = vortex_plane(N24, N24, ONE, M2S)
rows_p = string_modes(pl, H, V, ops, ONE, EMAX, +0.1)
cen = census(rows_p)
core = core_rows(rows_p)
cE = [r[0] for r in core]
cV = [r[3] for r in core]
cG = [r[4]['-G3'] for r in core]
cX = max(abs(r[4]['X']) for r in core)
cE8 = max(abs(r[4]['eps']) for r in core)
check("D1 [numerical] 24x24 (dim %d), n = +1, p = +0.1: %d in-gap states, %d core modes E = %s, "
      "core w >= %.3f, ring <= %.3f, <V_z> = %s, <-G3> = %s, |<X>| <= %.1e, |<eps>| <= %.1e; net "
      "core %+d, ring %+d, mixed %+d"
      % (pl.D, len(rows_p), len(core), fmt(cE), min(r[1][0] for r in core), max(r[2] for r in core),
         fmt(cV, "%+.3f"), fmt(cG, "%+.3f"), cX, cE8, net(cen, 'core0'), net(cen, 'ring'),
         net(cen, 'mixed')),
      len(core) == 2 and net(cen, 'core0') == 2 and net(cen, 'ring') == -2 and net(cen, 'mixed') == 0
      and all(abs(e - 0.0999) < 2e-3 for e in cE) and all(v > 0.98 for v in cV)
      and all(g > 0.99 for g in cG) and cX < 1e-2 and cE8 < 1e-2 and min(r[1][0] for r in core) > 0.8)
te = {name: proj_eigs(core, ops[name]) for name in ('s1', 's2', 's3')}
check("D2 [numerical] taste-projected eigenvalues on the n = +1 core pair: s1 %s; s2 %s; s3 %s -- "
      "one mode per taste, both right-movers" % tuple(fmt(te[k], "%+.3f") for k in ('s1', 's2', 's3')),
      all(len(te[k]) == 2 and te[k][0] < -0.9 and te[k][1] > 0.9 for k in te))

MINUS = [(C24[0], C24[1], -1)]
pl_m, H_m, V_m, ops_m = vortex_plane(N24, N24, MINUS, M2S)
rows_m = string_modes(pl_m, H_m, V_m, ops_m, MINUS, EMAX, +0.1)
cen_m = census(rows_m)
core_m = core_rows(rows_m)
te_m = proj_eigs(core_m, ops_m['s3'])
check("D3 [numerical] n = -1, p = +0.1: %d core modes, E = %s, <V_z> = %s, <-Gamma_3> = %s, "
      "s3-projected %s: two left-movers; net core %+d, ring %+d"
      % (len(core_m), fmt([r[0] for r in core_m]), fmt([r[3] for r in core_m], "%+.3f"),
         fmt([r[4]['-G3'] for r in core_m], "%+.3f"), fmt(te_m, "%+.3f"),
         net(cen_m, 'core0'), net(cen_m, 'ring')),
      len(core_m) == 2 and net(cen_m, 'core0') == -2 and net(cen_m, 'ring') == 2
      and all(abs(r[0] + 0.0999) < 2e-3 and r[3] < -0.98 for r in core_m)
      and te_m[0] < -0.9 and te_m[1] > 0.9)

TWO = [(C24[0], C24[1], +2)]
pl2, H2, V2, ops2 = vortex_plane(N24, N24, TWO, M2S)
rows2 = string_modes(pl2, H2, V2, ops2, TWO, EMAX, +0.1)
cen2 = census(rows2)
core2 = core_rows(rows2)
x2 = proj_eigs(core2, ops2['X'])
t2 = proj_eigs(core2, ops2['s3'])
check("D4 [numerical] n = +2, p = +0.1: %d core modes E = %s, core w >= %.3f, <V_z> >= %+.3f, "
      "<-G3> >= %+.3f; X on the core subspace %s (trace %.1e); s3 %s: four right-movers, two per "
      "taste; net core %+d, ring %+d"
      % (len(core2), fmt([r[0] for r in core2]), min(r[1][0] for r in core2),
         min(r[3] for r in core2), min(r[4]['-G3'] for r in core2), fmt(x2, "%+.3f"),
         float(np.sum(x2)), fmt(t2, "%+.3f"), net(cen2, 'core0'), net(cen2, 'ring')),
      len(core2) == 4 and net(cen2, 'core0') == 4 and net(cen2, 'ring') == -4
      and all(abs(r[0] - 0.1002) < 2e-3 and r[3] > 0.98 for r in core2)
      and abs(np.sum(x2)) < 1e-2 and np.sum(t2 > 0.9) == 2 and np.sum(t2 < -0.9) == 2)

vel_rows, split_rows = [], []
for N in (16, 24, 32):
    c = [((N - 1) / 2, (N - 1) / 2, +1)]
    plN, HN, VN, opsN = vortex_plane(N, N, c, M2S)
    Ep = [r[0] for r in core_rows(string_modes(plN, HN, VN, opsN, c, EMAX, +0.1))]
    Em = [r[0] for r in core_rows(string_modes(plN, HN, VN, opsN, c, EMAX, -0.1))]
    E0, _ = in_gap(HN(np.pi), EMAX)
    vel_rows.append((N, plN.D, [(a - b) / 0.2 for a, b in zip(Ep, Em)]))
    split_rows.append(float(np.min(np.abs(E0))))
vtxt = "; ".join("N=%d (dim %d) %.4f" % (N, D, v[0]) for (N, D, v) in vel_rows)
check("D5 [numerical] n = +1 core-pair velocity (E(+0.1) - E(-0.1))/0.2, both branches equal: %s; "
      "p = 0 core/ring splitting min|E| = %s, falling by %.1f then %.1f per Delta N = 8"
      % (vtxt, ", ".join("%.3e" % s for s in split_rows), split_rows[0] / split_rows[1],
         split_rows[1] / split_rows[2]),
      all(len(v) == 2 and all(abs(x - 1.0) < 0.05 for x in v) for (_, _, v) in vel_rows)
      and split_rows[0] > split_rows[1] > split_rows[2] and split_rows[2] < 1e-3)
allG = cG + [r[4]['-G3'] for r in core_m]
xmax = max(cX, max(abs(r[4]['X']) for r in core_m))
check("D6 [numerical] |<X>| <= %.1e on every n = +-1 string mode, X traceless on the n = 2 core "
      "subspace (%.1e), <-G3> = %s: handedness is the sharp eigenvalue of -Gamma_3 = sigma_3 x "
      "tau_3 (the Jackiw-Rossi index), not the 3+1D chirality"
      % (xmax, float(np.sum(x2)), fmt(allG, "%+.3f")),
      xmax < 1e-2 and abs(np.sum(x2)) < 1e-2 and all(abs(abs(g) - 1) < 5e-3 for g in allG))

# ============================================================== GROUP E -- T6
plT, HT, VT, opsT = vortex_plane(N24, N24, ONE, XI[2])
coreT = core_rows(string_modes(plT, HT, VT, opsT, ONE, EMAX, +0.1))
gapT = sorted(abs(r[0]) for r in core_rows(string_modes(plT, HT, VT, opsT, ONE, EMAX, 0.0)))
sT = proj_eigs(coreT, opsT['s3'])
netT = sum(1 if r[3] > 0 else -1 for r in coreT)
check("E1 [numerical] M2 -> Xi_3 = M2 s_3 (z-bond dimerisation), n = +1, p = +0.1: %d core modes "
      "(E,<V_z>,<s3>) = %s, s3 %s: one right- and one left-mover of opposite taste, net %+d; at "
      "p = 0 they hybridise into a gap 2 x %.5f"
      % (len(coreT), " ".join("(%+.5f,%+.3f,%+.3f)" % (r[0], r[3], r[4]['s3']) for r in coreT),
         fmt(sT, "%+.3f"), netT, gapT[0] if gapT else -1.0),
      len(coreT) == 2 and netT == 0 and coreT[0][3] < -0.7 and coreT[1][3] > 0.7
      and coreT[0][4]['s3'] * coreT[1][4]['s3'] < -0.4 and len(gapT) == 2 and abs(gapT[0] - 0.0846) < 2e-3)
mixed = []
for (a, b) in ((1.0, 0.5), (0.5, 1.0), (0.8, 0.8)):
    plX, HX, VX, opsX = vortex_plane(N24, N24, ONE, a * M2S + b * XI[2])
    rowsX = string_modes(plX, HX, VX, opsX, ONE, EMAX, +0.1)
    mixed.append((a, b, net(census(rowsX), 'core0'), len(core_rows(rowsX)),
                  int(np.sign(a + b) + np.sign(a - b))))
check("E2 [numerical] mixed a M2 + b Xi_3, n = +1, p = +0.1: (a, b, core net, core modes) = %s, "
      "against n [sgn(a+b) + sgn(a-b)] = %s"
      % (" ".join("(%g,%g,%+d,%d)" % m[:4] for m in mixed), ",".join("%+d" % m[4] for m in mixed)),
      all(m[2] == m[4] for m in mixed) and [m[2] for m in mixed] == [2, 0, 1])

# ============================================================== GROUP F -- T7
coresF = [(9.5, 11.5, +1), (29.5, 11.5, -1)]
plF, HF, VF, opsF = vortex_plane(40, 24, coresF, M2S)
rowsF = string_modes(plF, HF, VF, opsF, coresF, EMAX, +0.15)
rowsFm = string_modes(plF, HF, VF, opsF, coresF, EMAX, -0.15)
cenF, cenFm = census(rowsF), census(rowsFm)
c0, c1 = core_rows(rowsF, 0), core_rows(rowsF, 1)
vF = (c0[0][0] - core_rows(rowsFm, 0)[0][0]) / 0.3
check("F1 [numerical] 40x24 (dim %d), cores (9.5,11.5,+1) and (29.5,11.5,-1), p = +0.15: core0 %d "
      "modes E = %s <V_z> = %s; core1 %d modes E = %s <V_z> = %s (both modes equal per core); "
      "ring %d states, net %+d; at p = -0.15 net core0 %+d, core1 %+d, ring %+d; v = %.3f: +2 on "
      "the string, -2 on the anti-string, the ring vector-like"
      % (plF.D, len(c0), "%+.5f" % c0[0][0], "%+.3f" % c0[0][3], len(c1),
         "%+.5f" % c1[0][0], "%+.3f" % c1[0][3],
         cenF.get(('ring', '+'), 0) + cenF.get(('ring', '-'), 0), net(cenF, 'ring'),
         net(cenFm, 'core0'), net(cenFm, 'core1'), net(cenFm, 'ring'), vF),
      len(c0) == 2 and len(c1) == 2 and net(cenF, 'core0') == 2 and net(cenF, 'core1') == -2
      and net(cenF, 'ring') == 0 and net(cenFm, 'core0') == 2 and net(cenFm, 'core1') == -2
      and net(cenFm, 'ring') == 0 and abs(vF - 1.0) < 0.05)

# ============================================================== GROUP G -- T8


def peierls_flux_tube(N, c, nphi, sB=2.0):
    """Peierls phases for a Gaussian flux tube of total flux 2 pi nphi (source stage_F)."""
    def Aline(x0, y0, x1, y1):
        xm, ym = (x0 + x1) / 2 - c[0], (y0 + y1) / 2 - c[1]
        r2 = xm * xm + ym * ym
        Phi = 2 * np.pi * nphi * (1 - np.exp(-r2 / (2 * sB * sB)))
        Ax, Ay = -Phi * ym / (2 * np.pi * r2), Phi * xm / (2 * np.pi * r2)
        return Ax * (x1 - x0) + Ay * (y1 - y0)
    phase = {}
    for x in range(N):
        for y in range(N):
            phase[('x', x, y)] = np.exp(1j * Aline(x, y, x + 1, y))
            phase[('y', x, y)] = np.exp(1j * Aline(x, y, x, y + 1))
    tot = 0.0
    for x in range(N - 1):
        for y in range(N - 1):
            tot += np.angle(phase[('x', x, y)] * phase[('y', x + 1, y)]
                            * np.conj(phase[('x', x, y + 1)]) * np.conj(phase[('y', x, y)]))
    return phase, tot / (2 * np.pi)


plG = Plane(N24, N24)
ZERO2 = {cell: 0.0 for cell in plG.cells}
flux_rows, massless = [], None
for nphi in (1, 2):
    phase, tot = peierls_flux_tube(N24, C24, nphi)
    H0G, ZiG = plG.hop_matrices(phase=phase)
    HG, VG = build_sparse(plG, np.full(plG.D, M0), ZERO2, M2S, H0G, ZiG)
    counts, nearest = [], []
    for p in (-0.1, 0.0, 0.1):
        E, _ = in_gap(HG(np.pi + p), EMAX, k=8)
        counts.append(len(E))
        Eall = spla.eigsh(HG(np.pi + p), k=4, sigma=0.0, which='LM', v0=start_vector(plG.D),
                          return_eigenvectors=False)
        nearest.append(float(np.min(np.abs(Eall))))
    flux_rows.append((nphi, tot, counts, min(nearest)))
    if nphi == 1:
        HGm, VGm = build_sparse(plG, np.zeros(plG.D), ZERO2, M2S, H0G, ZiG)
        Em, Um = in_gap(HGm(np.pi + 0.1), 0.3, k=16)
        velm = [float(np.real(Um[:, k].conj() @ (VGm(np.pi + 0.1) @ Um[:, k]))) for k in range(len(Em))]
        order = np.argsort(np.abs(Em))
        massless = (Em, velm, [Em[order[0]], Em[order[1]]], [velm[order[0]], velm[order[1]]],
                    sum(1 if v > 0 else -1 for v in velm))
check("G1 [numerical] 24x24, Gaussian flux tube (sigma_B = 2) of the link field, real mass "
      "m1 = 0.7, no vortex: (n_phi, plaquette sum/2pi, in-gap count at p = -0.1,0,+0.1, nearest "
      "|E|) = %s: no in-gap state; massless control n_phi = 1, p = +0.1: %d states with |E| < 0.3 "
      "in +-E pairs, the two nearest zero E = %s, <V_z> = %s, net %+d: vector-like"
      % (" ".join("(%d, %.4f, %s, %.3f)" % (n, t, c, m) for (n, t, c, m) in flux_rows),
         len(massless[0]), fmt(massless[2], "%+.4f"), fmt(massless[3], "%+.3f"), massless[4]),
      all(c == [0, 0, 0] and m > EMAX and abs(t - n) < 1e-3 for (n, t, c, m) in flux_rows)
      and massless[4] == 0 and massless[3][0] * massless[3][1] < 0
      and abs(massless[2][0] + massless[2][1]) < 1e-6)

check("S1 [1e-9] solver certificate over all %d transverse windows: |dense LAPACK count - sparse "
      "count| max %d, max |dE| %.1e, max eigenpair residual %.1e; the k-th eigenvalue nearest zero "
      "lay outside every window" % (CERT["windows"], CERT["count_dev"], CERT["dE"], CERT["res"]),
      CERT["count_dev"] == 0 and CERT["dE"] < 1e-9 and CERT["res"] < 1e-8)

print("SUMMARY: the taste-singlet second mass is the body-diagonal imaginary hop X1Y2X3; its "
      "vortex strings carry exactly 2n co-moving modes, one per taste, handed by -Gamma_3 and not "
      "by X, paired with -2n on a ring or an anti-string.  [%.1f s]" % (time.time() - T0))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
