#!/usr/bin/env python3
"""The fermion's charge coupling screens the spin-1/2 link field and supplies no
transverse electric stiffness, and the pi-flux sea selects the sign of the
plaquette coupling.

Self-contained runner.  Every object is rebuilt here from its own indexing and
every exact number is recomputed from scratch; no binary and no external datum
is trusted.  The two C engines are embedded verbatim below and compiled at run
time into a private temporary directory.

THE SETTING, redeclared.  One designed spin-1/2 role per coarse edge (PR #7893,
P2 = PR #7959): E_e = Z^L_e/2, U_e = sigma^+_e, P_f = W_f + W_f^dag, the pure
law H = -lambda sum_f P_f with lambda supplied and set to 1.  One fermion mode
per coarse vertex with the Kawamoto-Smit signs eta_1 = 1, eta_2 = (-1)^{v_1},
eta_3 = (-1)^{v_1+v_2}, the Peierls hop -t sum eta_d(v) [a_v^+ U_(v,d) a_{v+d}
+ h.c.] of PR #7893 at unit charge, and its staggered Gauss law
2 (div E)_v = 2 n_v - (1 - eps_v).  Records fixed = the joint Z basis.

  A  [exact, seed-free] THE ONE-LOOP POLARISATION of the half-filled pi-flux
     sea on the 6^3, 8^3 and 12^3 twisted tori, with the link phase read as a
     c-number background (supplied: the large-S / mean-field reading of U_e).
     The sea and its twists; the Ward identity, Pi_L = 0 and chi(0) = 0; the
     induced Lorentz-covariant Maxwell term kappa_E (d_tau A)^2 + kappa_B B^2
     with both couplings positive and running logarithmically and
     c^2 = kappa_B/kappa_E falling to v_F^2 = 4; and the screening arithmetic
     1/U_tot = 1/U_link + kappa_E.
     [reproduces the source blocks t1_sea.py, t1_vf.py, t1_polarisation.py]
  B  [exact, seed-free] THE COUPLED MODEL ON 2x2x2, complete and untruncated:
     303,721 states over all 70 charge patterns.  P2's three t = 0 anchors; the
     softening of the transverse-electric pole and the rise of S_T as the hop is
     turned on; the melting of the staggered sea; the mixing of the winding
     sectors; the record-basis sign structure and its severity in both lambda
     conventions; and the energetic selection of -lambda by the sea.
     [reproduces t2_coupled_222.py, t2_sign_structure.py, t2_extras.py]
  C  [C1 exact in Python; C2-C5 need a C compiler] THE SUPPLIED COLLINEAR
     STAND-IN Uc sum_{collinear pairs} E_b E_b' -- NOT what the fermion
     produces, a calibration term chosen for its symmetry.  The exact 2x2x2 ice
     component; the patched walker engine against it at declared seeds; the
     exact 4x2x2 rows at Uc = 0 (P2's T3 to every digit) and at Uc = 1; and one
     short L = 4 witness pair.
     [reproduces geo.py, t3_validate_222.py, t3_run.py, t3_parse_t422.py, and
      the engines gfmc_d.c and t422d.c produced by patch_engines.py]
  D  [declared] THE QUOTED L^3 ROWS.  The cross-lane comparison against the
     sister lane's Rokhsar-Kivelson dispersion and the Uc scan at L = 4, 6, 8
     cost about twelve minutes of core time and are NOT rerun here; their
     numbers are declared constants and this group checks only the arithmetic
     read off them.

Groups A and B are exact linear algebra and integer/bit arithmetic in Python.
Group C is exact and seed-free except C2 and C5, which are witnesses at
declared seeds; C2-C5 report SKIP with a stated reason where no C compiler is
available.  One process at a time; no dense matrix exceeds 1728 x 1728 and peak
memory stays under about 400 MB.

Output: one PASS/SKIP/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import math
import os
import shutil
import subprocess
import sys
import tempfile
import time
from collections import deque

import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as sla

AUDIT_TIMEOUT_SEC = 300

# The Lanczos start vector is fixed so that every "seed-free" row below is
# bit-reproducible: without this, ARPACK draws its start vector from the global
# generator and the roundoff floors printed at 1e-30 wander between runs.
np.random.seed(20260904)

T_HOP = 1.0                 # the Peierls hop scale used for the sea and v_F
LAM = 1.0                   # the supplied plaquette coupling |lambda|
SEED_VAL = (20260930, 20261201, 20261202, 20261203, 20261204)   # C2 witnesses
SEED_L4 = 20261401                                              # C5 witness

PASS = 0
FAIL = 0
SKIPPED = 0
T0 = time.time()


def check(label, cond):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
    else:
        FAIL += 1
    print(("PASS " if ok else "FAIL ") + label)
    return ok


def skip(label, reason):
    global SKIPPED
    SKIPPED += 1
    print("SKIP " + label + " -- " + reason)


def near(a, b, tol):
    return abs(float(a) - float(b)) <= tol


def allnear(a, b, tol):
    return all(near(x, y, tol) for x, y in zip(a, b))


# =====================================================================  A
# The half-filled Kawamoto-Smit (pi-flux) sea and its one-loop polarisation.
# Hopping M_{v,v+d} = -t eta_d(v) with eta_1 = 1, eta_2 = (-1)^{v_1},
# eta_3 = (-1)^{v_1+v_2} (PR #7893's definitions); a twist on axis a flips the
# bonds crossing v_a = L-1 -> 0 (PR #7883's convention); half filling
# N = L^3/2.  Minimal coupling M_b -> M_b e^{i A_b} on the bond b = (v,d):
#   H(A) = H_0 - sum_b A_b j_b - (1/2) sum_b K_b A_b^2 + O(A^3)
#   Pi_dd'(k)      = -<K_bond> delta_dd' - (2/N) sum_{ph} conj(J_d) J_d' / D
#   kappaE_dd'(k)  =  (2/N) sum_{ph} conj(J_d) J_d' / D^3      [w^2 coefficient]
#   chi(k)         =  (2/N) sum_{ph} |rho(k)_ph|^2 / D
# with D = e_p - e_h, lattice gradient K_d = 2 sin(k_d/2), transverse projector
# P_T = 1 - K K^T/|K|^2, kappa_B = Pi_T/(2|K|^2) and kappa_E = tr(P_T kappaE)/2
# per transverse polarisation.  Exact linear algebra, no seed.

def build_M(L, twist):
    N = L ** 3
    M = np.zeros((N, N))
    idx = lambda v: (v[0] % L) * L * L + (v[1] % L) * L + (v[2] % L)
    bonds = []
    for v in itertools.product(range(L), repeat=3):
        for d in range(3):
            w = list(v)
            w[d] += 1
            eta = [1, (-1) ** v[0], (-1) ** (v[0] + v[1])][d]
            s = -1.0 if (twist[d] and v[d] == L - 1) else 1.0
            i, j = idx(v), idx(tuple(w))
            M[i, j] += -eta * s * T_HOP
            M[j, i] += -eta * s * T_HOP
            bonds.append((i, j, d, -eta * s * T_HOP))
    return M, bonds


def bloch8(kx, ky, kz):
    """The 8-site-cell Bloch block of the same sign field (cell side 2)."""
    sub = list(itertools.product((0, 1), repeat=3))
    H = np.zeros((8, 8), complex)
    for a, v in enumerate(sub):
        for d in range(3):
            w = list(v)
            w[d] += 1
            eta = [1, (-1) ** v[0], (-1) ** (v[0] + v[1])][d]
            cell = [w[i] // 2 for i in range(3)]
            b = sub.index(tuple(x % 2 for x in w))
            ph = np.exp(1j * (kx * 2 * cell[0] + ky * 2 * cell[1] + kz * 2 * cell[2]))
            H[a, b] += -eta * ph * T_HOP
            H[b, a] += -eta * np.conj(ph) * T_HOP
    return np.linalg.eigvalsh(H)


def polarisation(L, twist, kpoints):
    N = L ** 3
    Nh = N // 2
    M, bonds = build_M(L, twist)
    e, U = np.linalg.eigh(M)
    Uh, Up = U[:, :Nh], U[:, Nh:]
    D = e[Nh:][None, :] - e[:Nh][:, None]
    P = Uh @ Uh.T
    Kvals = np.array([b[3] * 2 * P[b[0], b[1]] for b in bonds])
    pos = np.array([divmod(i, L * L)[0:1] + divmod(divmod(i, L * L)[1], L) for i in range(N)], float)
    out = {"E_sea": float(e[:Nh].sum()), "gap": float(e[Nh] - e[Nh - 1]),
           "Kbond": float(Kvals.mean()), "Kspread": float(Kvals.std()), "rows": {}}
    for kk in kpoints:
        k = 2 * np.pi * np.array(kk) / L
        Kd = 2 * np.sin(k / 2)
        J = []
        for d in range(3):
            Jd = np.zeros((N, N), complex)
            for (i, j, dd, m) in bonds:
                if dd != d:
                    continue
                r = pos[i].copy()
                r[d] += 0.5
                ph = np.exp(-1j * (k @ r))
                Jd[i, j] += -1j * m * ph
                Jd[j, i] += 1j * m * ph
            J.append(Uh.T @ Jd @ Up)
        Rph = Uh.T @ np.diag(np.exp(-1j * (pos @ k))) @ Up
        Pi = np.zeros((3, 3), complex)
        kE = np.zeros((3, 3), complex)
        for a in range(3):
            for b in range(3):
                Pi[a, b] = -out["Kbond"] * (a == b) - 2 * np.sum(np.conj(J[a]) * J[b] / D) / N
                kE[a, b] = 2 * np.sum(np.conj(J[a]) * J[b] / D ** 3) / N
        chi = float(np.real(2 * np.sum(np.abs(Rph) ** 2 / D) / N))
        herm = float(np.abs(Pi - Pi.conj().T).max())
        K2 = float(Kd @ Kd)
        row = {"K2": K2, "herm": herm, "chi": chi}
        if K2 > 1e-12:
            row["ward"] = float(np.abs(Pi @ Kd).max() / max(np.abs(Pi).max(), 1e-30))
            PT = np.eye(3) - np.outer(Kd, Kd) / K2
            PiT = float(np.real(np.trace(PT @ Pi)))
            row["PiT"] = PiT
            row["PiL"] = float(np.real(Kd @ Pi @ Kd) / K2)
            row["kappa_B"] = PiT / (2 * K2)
            row["kappa_E"] = float(np.real(np.trace(PT @ kE)) / 2)
            row["kE_L"] = float(np.real(Kd @ kE @ Kd) / K2)
            row["c2"] = row["kappa_B"] / row["kappa_E"]
            evT = np.sort(np.real(np.linalg.eigvalsh((PT @ Pi @ PT + (PT @ Pi @ PT).conj().T) / 2)))
            row["split"] = (float(evT[1]), float(evT[2]))
        else:
            row["Pi0"] = float(np.real(np.trace(Pi)) / 3)
            row["kappa_E"] = float(np.real(np.trace(kE)) / 3)
        out["rows"][tuple(kk)] = row
    return out


# --- A1: the sea, its twists, the chiral identity and the Dirac node ---------
SEA = {}
for L in (4, 6, 8, 12):
    best = None
    for tw in itertools.product((0, 1), repeat=3):
        M, _ = build_M(L, tw)
        ev = np.linalg.eigvalsh(M)
        Nh = L ** 3 // 2
        Es = float(ev[:Nh].sum())
        if best is None or Es < best[1] - 1e-9:
            best = (tw, Es, float(ev[Nh] - ev[Nh - 1]))
    SEA[L] = best
M8, _ = build_M(8, (1, 1, 1))
eps8 = np.array([(-1) ** (v[0] + v[1] + v[2]) for v in itertools.product(range(8), repeat=3)])
chiral = float(np.abs(eps8[:, None] * M8 * eps8[None, :] + M8).max())
node = float(np.abs(bloch8(np.pi / 2, np.pi / 2, np.pi / 2)).max())
vF = [min(abs(bloch8(np.pi / 2 + q, np.pi / 2, np.pi / 2))) / q for q in (0.01, 0.02, 0.05)]

check("A1 [exact] the pi-flux sea, L = 4, 6, 8, 12: twists %d%d%d, %d%d%d, %d%d%d, %d%d%d minimise E_sea = %.6f, "
      "%.6f, %.6f, %.6f (the first three PR #7883's), gaps %.6f, %.6f, %.6f, %.6f; chiral residual %.1f exactly; "
      "Bloch node at (pi/2,pi/2,pi/2) to %.0e, v_F = %.5f -> 2t"
      % (SEA[4][0] + SEA[6][0] + SEA[8][0] + SEA[12][0] + (SEA[4][1], SEA[6][1], SEA[8][1], SEA[12][1],
         SEA[4][2], SEA[6][2], SEA[8][2], SEA[12][2], chiral, node, vF[0])),
      SEA[4][0] == (1, 1, 1) and SEA[6][0] == (0, 0, 0) and SEA[8][0] == (1, 1, 1) and SEA[12][0] == (1, 1, 1)
      and allnear([SEA[L][1] for L in (4, 6, 8, 12)],
                  [-78.383672, -258.857540, -611.811768, -2063.196887], 5e-6)
      and allnear([SEA[L][2] for L in (4, 6, 8, 12)],
                  [4.898979, 3.464102, 2.651309, 1.793151], 5e-6)
      and chiral == 0.0 and node < 1e-12 and allnear(vF, [2.0, 2.0, 2.0], 1e-3))

POL = {}
for L, tw in ((6, (0, 0, 0)), (8, (1, 1, 1)), (12, (1, 1, 1))):
    kps = [(0, 0, 0)] + [(n, 0, 0) for n in range(1, L // 2 + 1)] \
        + [(n, n, 0) for n in range(1, L // 4 + 1)] + [(n, n, n) for n in range(1, L // 4 + 1)]
    POL[L] = polarisation(L, tw, kps)

ROWS = [(L, kk, r) for L in (6, 8, 12) for kk, r in POL[L]["rows"].items() if r["K2"] > 1e-12]
w_max = max(r["ward"] for _, _, r in ROWS)
piL_max = max(abs(r["PiL"]) for _, _, r in ROWS)
herm_max = max(r["herm"] for L in POL for r in POL[L]["rows"].values())
kspread = max(POL[L]["Kspread"] for L in POL)
chi0 = max(abs(POL[L]["rows"][(0, 0, 0)]["chi"]) for L in POL)
cont = max(abs(r["kE_L"] - r["chi"] / r["K2"]) for _, _, r in ROWS)

check("A2 [exact] on all three tori: <K_bond> uniform to %.0e, Pi Hermitian to %.0e, Ward "
      "|Pi K|/|Pi| <= %.1e at all %d non-zero k, Pi_L = 0 to %.0e, chi(0) = 0 to %.0e, kappaE_L = chi/|K|^2 to %.0e"
      " -- PURELY LONGITUDINAL density response, no transverse cost from Gauss's law" % (kspread, herm_max, w_max, len(ROWS), piL_max, chi0, cont),
      kspread <= 1e-15 and herm_max <= 1e-15 and w_max <= 1.5e-15 and piL_max <= 1e-15
      and chi0 <= 1e-29 and cont <= 1e-12)

tab = [(6, (1, 0, 0)), (6, (3, 0, 0)), (8, (1, 0, 0)), (8, (2, 0, 0)), (12, (1, 0, 0)),
       (12, (2, 0, 0)), (12, (3, 0, 0)), (12, (6, 0, 0)), (12, (3, 3, 3))]
ref = [(0.203096, 0.101548, 0.016076), (0.443751, 0.055469, 0.010735), (0.124677, 0.106418, 0.021123),
       (0.249630, 0.062407, 0.016426), (0.065981, 0.123123, 0.027706), (0.156141, 0.078070, 0.020356),
       (0.240055, 0.060014, 0.017619), (0.404008, 0.050501, 0.018081), (0.448930, 0.037411, 0.007718)]
got = [(POL[L]["rows"][k]["PiT"], POL[L]["rows"][k]["kappa_B"], POL[L]["rows"][k]["kappa_E"]) for L, k in tab]
split6 = POL[6]["rows"][(1, 1, 0)]["split"]

check("A3 [exact] a Maxwell term with BOTH couplings positive: Pi_T, kappa_B, kappa_E > 0 at all %d non-zero k "
      "(min %.6f), transverse eigenvalues equal on the axes, split off it (%.5f, %.5f at 2pi/6 (1,1,0)); "
      "the nine table rows reproduce, e.g. %.6f, %.6f, %.6f at 2pi/12 (1,0,0). kappa_E (d_tau A)^2 is INERTIA"
      % (len(ROWS), min(r["kappa_E"] for _, _, r in ROWS), split6[0], split6[1], got[4][0], got[4][1], got[4][2]),
      all(r["PiT"] > 0 and r["kappa_B"] > 0 and r["kappa_E"] > 0 for _, _, r in ROWS)
      and all(allnear(g, rr, 6e-6) for g, rr in zip(got, ref))
      and near(split6[0], 0.10996, 1e-5) and near(split6[1], 0.15107, 1e-5))

kBmin = [POL[L]["rows"][(1, 0, 0)]["kappa_B"] for L in (6, 8, 12)]
kEmin = [POL[L]["rows"][(1, 0, 0)]["kappa_E"] for L in (6, 8, 12)]
c2min = [POL[L]["rows"][(1, 0, 0)]["c2"] for L in (6, 8, 12)]
kBfix = [POL[8]["rows"][(2, 0, 0)]["kappa_B"], POL[12]["rows"][(3, 0, 0)]["kappa_B"]]
drude = [POL[L]["rows"][(0, 0, 0)]["Pi0"] * L ** 3 for L in (6, 8, 12)]

check("A4 [exact] both run logarithmically: at fixed k L, kappa_B = %.6f, %.6f, %.6f and kappa_E = %.6f, %.6f, "
      "%.6f at L = 6, 8, 12, while kappa_B(pi/2) = %.6f, %.6f at L = 8, 12 is L-independent; c^2 = %.3f, %.3f, %.3f "
      "falls to v_F^2 = 4 FROM ABOVE; Pi(0) L^3 = %.2f, %.2f, %.2f, no free-carrier term"
      % (kBmin[0], kBmin[1], kBmin[2], kEmin[0], kEmin[1], kEmin[2], kBfix[0], kBfix[1],
         c2min[0], c2min[1], c2min[2], drude[0], drude[1], drude[2]),
      kBmin[0] < kBmin[1] < kBmin[2] and kEmin[0] < kEmin[1] < kEmin[2]
      and allnear(kBmin, [0.101548, 0.106418, 0.123123], 6e-6)
      and allnear(kEmin, [0.016076, 0.021123, 0.027706], 6e-6)
      and allnear(kBfix, [0.062407, 0.060014], 6e-6)
      and allnear(c2min, [6.317, 5.038, 4.444], 1e-3) and c2min[0] > c2min[1] > c2min[2] > 4.0
      and allnear(drude, [9.56, 9.47, 10.39], 5e-2))

Ueff = [1.0 / k for k in kEmin]
u_p2 = 0.78 / (2 * 0.17)                 # P2's omega ~ 0.78 k^2 and S_T ~ 0.17 per polarisation
kstar = 1.0 / math.sqrt(kEmin[2] * u_p2)
small = [math.sqrt((0.065 + kBmin[2]) * u_p2 / (1 + kEmin[2] * u_p2 * kk ** 2)) * kk ** 2 for kk in (0.1, 0.2)]

check("A5 [exact] kappa_E enters the INVERSE stiffness 1/U_tot = 1/U_link + kappa_E, so the sea only lowers U: "
      "U_eff = 1/kappa_E = %.1f, %.1f, %.1f. Under P2's U(k) = u k^2, u = %.3f, "
      "omega^2 = (v + kappa_B) u k^4/(1 + kappa_E u k^2) stays QUADRATIC (omega/k^2 = %.3f, %.3f at k = 0.1, 0.2), "
      "linear only above k_* = %.2f > pi = %.2f: the anticipated crossover runs the other way"
      % (Ueff[0], Ueff[1], Ueff[2], u_p2, small[0] / 0.01, small[1] / 0.04, kstar, math.pi),
      allnear(Ueff, [62.2, 47.3, 36.1], 0.1) and kstar > math.pi and near(kstar, 3.97, 0.02)
      and abs(small[0] / 0.01 - small[1] / 0.04) < 0.02)


# =====================================================================  B
# The coupled fermion + spin-1/2 link model on the fully periodic 2x2x2 torus,
# exact and complete in the Gauss sector.  Links (v,d) run from v to v+e_d,
# E = +1/2 iff the bit is set; faces (v, d<d') have forward links (v,d),
# (v+d,d') and backward (v+d',d), (v,d'); P_f flips all four when applicable.
# One fermion mode per vertex, Jordan-Wigner order = vertex index.
#   H(t,lam) = -t sum_{(v,d)} eta_d(v) [a_v^+ U_(v,d) a_{v+d} + h.c.]
#              + s lam sum_f P_f ,  s = -1 (P2's law) or +1 (PR #7893's)
#   Gauss:  2 (div E)_v = 2 n_v - (1 - eps_v)      [PR #7893, T2 item 3]
# The sector is built from ALL 2^24 link states grouped by their 2 div E
# signature and intersected with the 70 half-filled fermion patterns.
# NO TRUNCATION.

BL, BNV, BNL = 2, 8, 24
bverts = list(itertools.product(range(BL), repeat=3))
bvidx = lambda v: ((v[0] % BL) * BL + (v[1] % BL)) * BL + (v[2] % BL)


def bshift(v, d):
    w = list(v)
    w[d] = (w[d] + 1) % BL
    return tuple(w)


blinks = [(v, d) for v in bverts for d in range(3)]
blidx = {lk: i for i, lk in enumerate(blinks)}
beps = np.array([(-1) ** (v[0] + v[1] + v[2]) for v in bverts])
BETA_KS = True


def beta(v, d):
    return [1, (-1) ** v[0], (-1) ** (v[0] + v[1])][d] if BETA_KS else 1


bfaces = []
for v in bverts:
    for d in range(3):
        for dp in range(d + 1, 3):
            bfaces.append((blidx[(v, d)], blidx[(bshift(v, d), dp)],
                           blidx[(bshift(v, dp), d)], blidx[(v, dp)]))
assert len(bfaces) == 24


def div2_of(states):
    d2 = np.zeros((len(states), BNV), np.int8)
    for (v, d), j in blidx.items():
        ee = (((states >> j) & 1).astype(np.int8) * 2 - 1)
        d2[:, bvidx(v)] += ee
        d2[:, bvidx(bshift(v, d))] -= ee
    return d2


sig_index = {}
for c0 in range(0, 1 << BNL, 1 << 20):
    st = np.arange(c0, min(c0 + (1 << 20), 1 << BNL), dtype=np.uint32)
    packed = (div2_of(st) + 6).astype(np.uint8).astype(np.uint64) @ (np.uint64(13) ** np.arange(BNV, dtype=np.uint64))
    order = np.argsort(packed, kind='stable')
    packed, st = packed[order], st[order]
    u, start = np.unique(packed, return_index=True)
    ends = list(start[1:]) + [len(packed)]
    for uu, s0, s1 in zip(u, start, ends):
        sig_index.setdefault(int(uu), []).append(st[s0:s1])
sig_index = {k: np.concatenate(v) for k, v in sig_index.items()}
NSIG = len(sig_index)
sig_of = lambda d2: int(sum((int(x) + 6) * 13 ** i for i, x in enumerate(d2)))
DIM_PURE = len(sig_index.get(sig_of([0] * BNV), []))

nvec = lambda f: np.array([(f >> i) & 1 for i in range(BNV)])
bstates, bblocks = [], []
for f in [f for f in range(1 << BNV) if bin(f).count('1') == BNV // 2]:
    s = sig_of(2 * nvec(f) - (1 - beps))
    if s in sig_index:
        lk = sig_index[s]
        bstates.append(lk.astype(np.uint64) | (np.uint64(f) << np.uint64(BNL)))
        bblocks.append((f, len(lk)))
bkeys = np.sort(np.concatenate(bstates))
BD = len(bkeys)
bvac = [f for f, _ in bblocks if all(nvec(f) == (1 - beps) // 2)][0]
BVACDIM = dict(bblocks)[bvac]
BCHARGED = sorted(set(d for f, d in bblocks if f != bvac))
lk_all = (bkeys & np.uint64((1 << BNL) - 1)).astype(np.int64)
fm_all = (bkeys >> np.uint64(BNL)).astype(np.int64)
Emat = np.array([((lk_all >> j) & 1) * 1.0 - 0.5 for j in range(BNL)]).T
nmat = np.array([(fm_all >> i) & 1 for i in range(BNV)]).T * 1.0


def blookup(k):
    i = np.searchsorted(bkeys, k)
    ok = (i < BD)
    ok[ok] &= (bkeys[i[ok]] == k[ok])
    return i, ok


def jw_sign(fm, a, b):
    lo, hi = min(a, b), max(a, b)
    m = ((1 << hi) - 1) & ~((1 << (lo + 1)) - 1)
    return 1 - 2 * (np.array([bin(int(x) & m).count('1') for x in fm]) & 1)


def bbuild(t, lam, s):
    rows, cols, vals = [], [], []
    for (p, q, u, w) in bfaces:
        bp, bq, bu, bw = (lk_all >> p) & 1, (lk_all >> q) & 1, (lk_all >> u) & 1, (lk_all >> w) & 1
        idx = np.nonzero((bp == bq) & (bu == bw) & (bp != bu))[0]
        mask = (1 << p) | (1 << q) | (1 << u) | (1 << w)
        j, ok = blookup((lk_all[idx] ^ mask).astype(np.uint64) | (fm_all[idx].astype(np.uint64) << np.uint64(BNL)))
        assert ok.all()
        rows.append(idx); cols.append(j); vals.append(np.full(len(idx), s * lam))
    for (v, d), jl in blidx.items():
        a, b = bvidx(v), bvidx(bshift(v, d))
        e = beta(v, d)
        bl = (lk_all >> jl) & 1
        for (src, dst, need) in ((b, a, 0), (a, b, 1)):
            idx = np.nonzero((((fm_all >> src) & 1) == 1) & (((fm_all >> dst) & 1) == 0) & (bl == need))[0]
            if len(idx) == 0:
                continue
            fm_new = fm_all[idx] ^ ((1 << src) | (1 << dst))
            lk_new = lk_all[idx] ^ (1 << jl)
            j, ok = blookup(lk_new.astype(np.uint64) | (fm_new.astype(np.uint64) << np.uint64(BNL)))
            assert ok.all(), "Gauss closure"
            rows.append(idx); cols.append(j); vals.append(-t * e * jw_sign(fm_all[idx], dst, src))
    return sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(BD, BD))


def bphase(kvec, pol):
    ph = np.zeros(BNL)
    for j, (v, d) in enumerate(blinks):
        ph[j] = pol[d] * np.prod([(-1) ** (v[i] * kvec[i]) for i in range(3)]) / np.sqrt(8.0)
    return ph


def bpole(H, psi, E0, kvec, pol, nlan=80):
    """The pole of the E_pol(k) spectral function carrying the largest weight."""
    v = (Emat @ bphase(kvec, pol)) * psi
    v -= psi * (psi @ v)
    nrm = np.linalg.norm(v)
    v /= nrm
    V = [v]; al = []; be = []
    wv = H @ v; a = v @ wv; al.append(a); wv = wv - a * v; wv -= psi * (psi @ wv)
    for _ in range(nlan - 1):
        b = np.linalg.norm(wv)
        if b < 1e-10:
            break
        be.append(b); vn = wv / b; V.append(vn)
        wv = H @ vn; a = vn @ wv; al.append(a); wv = wv - a * vn - b * V[-2]
        wv -= psi * (psi @ wv)
        for uu in V[:-2]:
            wv -= uu * (uu @ wv)
    T = np.diag(al) + np.diag(be, 1) + np.diag(be, -1)
    ev, evec = np.linalg.eigh(T)
    wts = evec[0, :] ** 2
    i = int(np.argmax(wts))
    return float(ev[i] - E0), float(wts[i]), float(nrm ** 2)


def bfrustrated(H):
    """Breadth-first sign gauge sigma_j = -sign(H_ij) sigma_i; count frustrated edges."""
    Hc = H.tocsr().copy()
    Hc.setdiag(0)
    Hc.eliminate_zeros()
    n = Hc.shape[0]
    sgn = np.zeros(n, np.int8)
    fr = 0
    ncomp = 0
    indptr, indices, data = Hc.indptr, Hc.indices, Hc.data
    for s in range(n):
        if sgn[s]:
            continue
        ncomp += 1
        sgn[s] = 1
        dq = deque([s])
        while dq:
            i = dq.popleft()
            for p in range(indptr[i], indptr[i + 1]):
                j = indices[p]
                want = -sgn[i] * (1 if data[p] > 0 else -1)
                if sgn[j] == 0:
                    sgn[j] = want
                    dq.append(j)
                elif sgn[j] != want:
                    fr += 1
    return fr // 2, Hc.nnz // 2, ncomp


def bosonic(H):
    Hb = H.copy()
    d = Hb.diagonal()
    Hb.setdiag(0)
    Hb = -abs(Hb)
    Hb.setdiag(d)
    return float(sla.eigsh(Hb, k=1, which='SA', tol=1e-10)[0][0])


TS = (0.0, 0.25, 0.5, 1.0, 2.0)
B = {}
for t in TS:
    Eb = None
    for s in ((-1,) if t == 0.0 else (-1, 1)):
        H = bbuild(t, LAM, s)
        ev, vec = sla.eigsh(H, k=2, which='SA', tol=1e-10)
        o = np.argsort(ev)
        ev = ev[o]
        psi = vec[:, o[0]]
        if Eb is None:
            Eb = bosonic(H)
        w = psi ** 2
        Wd = [float(w @ ((Emat @ np.array([1.0 if (lk[1] == d and lk[0][d] == 0) else 0.0
                                           for lk in blinks])) ** 2)) for d in range(3)]
        ST = float(w @ ((Emat @ bphase((1, 0, 0), (0, 1, 0))) ** 2))
        SZ = float(w @ ((Emat @ bphase((1, 0, 0), (0, 0, 1))) ** 2))
        SL = float(w @ ((Emat @ bphase((1, 0, 0), (1, 0, 0))) ** 2))
        pl = bpole(H, psi, ev[0], (1, 0, 0), (0, 1, 0))
        B[(t, s)] = dict(E0=float(ev[0]), gap=float(ev[1] - ev[0]), stag=float(w @ (nmat @ beps)) / BNV,
                         ST=ST, SZ=SZ, SL=SL, W2=Wd, pole=pl, sev=float(ev[0]) - Eb,
                         herm=float(abs(H - H.T).max()))

check("B1 [exact] the coupled sector, complete and UNTRUNCATED: %d 2 div E signatures over all 2^24 link states, "
      "the rho = 0 block %d (P2's); with the %d half-filled fermion patterns, %d states over ALL %d charge "
      "patterns -- vacuum block %d, the %d charged ones in {%d, ..., %d}; |H - H^T| = %.0f"
      % (NSIG, DIM_PURE, len(bblocks), BD, len(bblocks), BVACDIM, len(bblocks) - 1, BCHARGED[0], BCHARGED[-1],
         B[(0.0, -1)]["herm"]),
      NSIG == 130193 and DIM_PURE == 9600 and BD == 303721 and len(bblocks) == 70 and BVACDIM == 9600
      and BCHARGED[0] == 2896 and BCHARGED[-1] == 6000 and B[(0.0, -1)]["herm"] == 0.0)

z = B[(0.0, -1)]
check("B2 [exact] P2's three t = 0 anchors to every digit: E_0 = %.10f, S_yy = S_zz = %.8f at (pi,0,0) with "
      "S_L = %.0e, transverse-electric pole %.10f at weight %.3f; the sector's own first excitation is a static "
      "charge pair at %.6f, not P2's Delta_1 = 1.6276"
      % (z["E0"], z["ST"], z["SL"], z["pole"][0], z["pole"][1], z["gap"]),
      near(z["E0"], -9.0267209135, 1e-9) and near(z["ST"], 0.25303701, 1e-8) and near(z["SZ"], 0.25303701, 1e-8)
      and z["SL"] < 1e-29 and near(z["pole"][0], 2.5172790443, 1e-8) and near(z["pole"][1], 0.803010, 1e-5)
      and near(z["gap"], 0.884161, 1e-6))

U0 = z["pole"][0] / (2 * z["ST"])
Um = B[(1.0, -1)]["pole"][0] / (2 * B[(1.0, -1)]["ST"])
Up = B[(1.0, 1)]["pole"][0] / (2 * B[(1.0, 1)]["ST"])
check("B3 [exact] the hop SOFTENS the pole and RAISES S_T at (pi,0,0): main pole %.4f -> %.4f (t = 1, P2's "
      "-lambda) -> %.4f (+lambda), S_T per polarisation %.6f -> %.6f -> %.6f, so U = omega/(2 S_T) "
      "FALLS %.2f -> %.2f -> %.2f -- screening in the exact model too"
      % (z["pole"][0], B[(1.0, -1)]["pole"][0], B[(1.0, 1)]["pole"][0], z["ST"], B[(1.0, -1)]["ST"],
         B[(1.0, 1)]["ST"], U0, Um, Up),
      B[(1.0, -1)]["pole"][0] < z["pole"][0] and B[(1.0, -1)]["ST"] > z["ST"] and Um < U0 and Up < Um
      and near(U0, 4.97, 5e-3) and near(Um, 4.75, 5e-3) and near(Up, 3.52, 5e-3)
      and near(B[(1.0, -1)]["pole"][0], 2.4806, 1e-4) and near(B[(1.0, 1)]["pole"][0], 1.8711, 1e-4))

stag = [B[(t, -1)]["stag"] for t in TS]
w2 = [B[(t, -1)]["W2"][0] for t in TS]
check("B4 [exact] the staggered sea MELTS and the winding sectors MIX (at -lambda): <eps n>/8 = %.5f, %.5f, %.5f, "
      "%.5f, %+.5f and <W_d^2> = %.5f, %.5f, %.5f, %.5f, %.5f at t = 0, 0.25, 0.5, 1, 2, isotropic in d: P2's 125 "
      "winding classes stop being superselected"
      % (stag[0], stag[1], stag[2], stag[3], stag[4], w2[0], w2[1], w2[2], w2[3], w2[4]),
      allnear(stag, [-0.50000, -0.26463, -0.06635, -0.00980, 0.00812], 1e-5)
      and allnear(w2, [0.0, 0.08892, 0.16419, 0.24005, 0.35214], 1e-5)
      and all(max(abs(np.array(B[(t, -1)]["W2"]) - B[(t, -1)]["W2"][0])) < 1e-9 for t in TS))

sevm = [B[(t, -1)]["sev"] for t in TS[1:]]
sevp = [B[(t, 1)]["sev"] for t in TS[1:]]
rat = [p / m for p, m in zip(sevp, sevm)]
Hh = bbuild(1.0, 0.0, -1)
sev_hop = float(sla.eigsh(Hh, k=1, which='SA', tol=1e-10)[0][0]) - bosonic(Hh)
fr = {}
for lab, H in (("hopKS", Hh), ("hop1", None), ("fullm", bbuild(1.0, LAM, -1)), ("fullp", bbuild(1.0, LAM, 1))):
    if H is None:
        BETA_KS = False
        H = bbuild(1.0, 0.0, -1)
        BETA_KS = True
    fr[lab] = bfrustrated(H)

check("B5 [exact] a RECORD-BASIS SIGN PROBLEM IN EVERY VARIANT: E_0 - E_0^bos = %.6f, %.6f, %.6f, %.6f "
      "at -lambda and %.6f, %.6f, %.6f, %.6f at +lambda (t = 0.25, 0.5, 1, 2), a factor %.1f, %.1f, %.1f, %.1f "
      "worse; the hop alone (lambda = 0, t = 1) %.6f; frustrated edges %d of %d for the hops (KS and "
      "eta = 1 alike: %d), %d / %d of %d for the full model"
      % (sevm[0], sevm[1], sevm[2], sevm[3], sevp[0], sevp[1], sevp[2], sevp[3], rat[0], rat[1], rat[2], rat[3],
         sev_hop, fr["hopKS"][0], fr["hopKS"][1], fr["hop1"][0], fr["fullm"][0], fr["fullp"][0], fr["fullm"][1]),
      allnear(sevm, [0.008344, 0.064856, 0.227373, 0.587880], 1e-6)
      and allnear(sevp, [0.187319, 0.792138, 1.548007, 2.831711], 1e-6)
      and all(r > 4.5 for r in rat) and sev_hop > 0.2
      and fr["hopKS"] == (231542, 1352112, 1) and fr["hop1"] == (231542, 1352112, 1)
      and fr["fullm"][0] == 517703 and fr["fullp"][0] == 561717 and fr["fullm"][1] == 2079672)

dE = [B[(t, 1)]["E0"] - B[(t, -1)]["E0"] for t in TS[1:]]
check("B6 [exact] THE SIGN OF lambda IS PHYSICAL and the sea selects P2's -lambda: "
      "E_0(-lambda) < E_0(+lambda) at every t > 0, by %.4f, %.4f, %.4f, %.4f at t = 0.25, 0.5, 1, 2 -- %.4f at "
      "t = lambda = 1 (%.10f against %.10f); for the pure law the flip is a gauge symmetry"
      % (dE[0], dE[1], dE[2], dE[3], dE[2], B[(1.0, -1)]["E0"], B[(1.0, 1)]["E0"]),
      all(d > 0 for d in dE) and near(dE[2], 1.3206, 1e-4)
      and near(B[(1.0, -1)]["E0"], -15.4713732151, 1e-9) and near(B[(1.0, 1)]["E0"], -14.1507399853, 1e-9))


# =====================================================================  C
# The supplied collinear stand-in.  On spin-1/2 links E_e^2 = 1/4 is a c-number,
# and section A shows the fermion generates no term of the form U E^2 at all;
# what is added here is therefore a SUPPLIED calibration term, the simplest
# record-diagonal, gauge-invariant, cubic-covariant quadratic form with a
# non-zero transverse k = 0 component -- the site-averaged field squared
#   U_site sum_v |Ebar_v|^2 = const + (U_site/2) sum_{collinear pairs} E_b E_b'
# with Ebar_v = (1/2) sum_d (E_{v,d} + E_{v-d,d}) e_d.  The engines carry
# Uc = U_site/2 as the coefficient of sum_{collinear pairs} E_b E_b', plus the
# sister lane's Rokhsar-Kivelson detuning V n_app for cross-reference.
# IT IS NOT WHAT THE INTEGRATED-OUT FERMION PRODUCES.
# Geometry class, torus3d, ice_config and write_geo are P2's own indexing,
# rebuilt here so the .geo files fed to the C engines are P2's.

class Geo:
    def __init__(self, tag, NL, plaq, inc, rho2, pos=None, ldir=None, n=None, li=None):
        self.tag, self.NL, self.plaq, self.inc, self.rho2 = tag, NL, plaq, inc, rho2
        self.pos, self.ldir, self.n, self.li = pos, ldir, n, li
        self.NP, self.NV = len(plaq), len(inc)

    def flips(self, s):
        out = []
        for f, (p, q, u, w) in enumerate(self.plaq):
            bp, bq, bu, bw = (s >> p) & 1, (s >> q) & 1, (s >> u) & 1, (s >> w) & 1
            if bp == bq and bu == bw and bp != bu:
                out.append((f, s ^ (1 << p) ^ (1 << q) ^ (1 << u) ^ (1 << w)))
        return out

    def n_app(self, s):
        return len(self.flips(s))


def torus3d(Lx, Ly, Lz):
    n = (Lx, Ly, Lz)
    sites = [(x, y, z) for x in range(Lx) for y in range(Ly) for z in range(Lz)]
    step = lambda s, d: tuple(((s[i] + 1) % n[i]) if i == d else s[i] for i in range(3))
    li, links, pos, ldir = {}, [], [], []
    for s in sites:
        for d in range(3):
            li[(s, d)] = len(links)
            links.append((s, d)); pos.append(s); ldir.append(d)
    inc = {s: [] for s in sites}
    for (s, d), j in li.items():
        inc[s].append((j, +1)); inc[step(s, d)].append((j, -1))
    plaq = []
    for s in sites:
        for d1 in range(3):
            for d2 in range(d1 + 1, 3):
                a, b = step(s, d1), step(s, d2)
                plaq.append((li[(s, d1)], li[(a, d2)], li[(b, d1)], li[(s, d2)]))
    g = Geo("t%d%d%d" % (Lx, Ly, Lz), len(links), plaq, inc, {s: 0 for s in sites}, pos, ldir, n, li)
    g.sites, g.step = sites, step
    return g


def ice_config(g):
    bits = 0
    for (s, d), j in g.li.items():
        if sum(s[i] for i in range(3) if i != d) % 2 == 0:
            bits |= 1 << j
    return bits


def write_geo(g, path, init_bits):
    with open(path, "w") as fh:
        fh.write("%d %d %d\n" % (g.NL, g.NP, g.NV))
        for (p, q, u, w) in g.plaq:
            fh.write("%d %d %d %d\n" % (p, q, u, w))
        fh.write("".join('1' if (init_bits >> j) & 1 else '0' for j in range(g.NL)) + "\n")
        fh.write("%d %d %d\n" % g.n)
        for j in range(g.NL):
            x, y, z = g.pos[j]
            fh.write("%d %d %d %d\n" % (x, y, z, g.ldir[j]))
        for v, lst in g.inc.items():
            fh.write(str(len(lst)) + " " + " ".join("%d %d" % (j, sg) for j, sg in lst) + " %d\n" % g.rho2[v])


def cval_of(g, s):
    """sum over collinear pairs (v,d), (v+e_d,d) of (2E)(2E')"""
    c = 0
    for (v, d), j in g.li.items():
        m = g.li[(g.step(v, d), d)]
        c += (1 if (s >> j) & 1 else -1) * (1 if (s >> m) & 1 else -1)
    return c


# ----------------------------------------------------------------- the engines
# Embedded verbatim and compiled at run time into a private temporary
# directory, so no binary is trusted.  Each is P2's engine (PR #7959's
# C_GFMC and C_T422) with the single P3 patch that adds the supplied diagonal
# D(s) = V n_app(s) + Uc sum_{collinear pairs} E_b E_b' -- the walker weight
# rate becomes n_app - D - E_T, E_mix = <-n_app + D>_w, and the 4x2x2 power
# iteration uses B = I + dpow (A - (D - D_min)) with dpow = 1/(D_max - D_min),
# entrywise non-negative so the Perron vector is still the ground state.
# [reproduces the source blocks gfmc_d.c and t422d.c of patch_engines.py]

C_GFMC_D = r"""/* P3 (patched from P2) -- adds diagonal D(s) = V n_app + Uc sum_pairs E E' (argv[18], argv[19]); continuous-time Green's-function (projector) Monte Carlo for H = -sum_f P_f on a Gauss sector,
 * with fixed-population reconfiguration and forward-walking (ancestry) buffers.
 *
 * e^{tau A} (A = -H = flip-graph adjacency) is sampled by walkers: from state s a walker waits an
 * exponential time with rate n_app(s), then flips a uniformly chosen applicable face; the importance
 * weight grows as exp( int (n_app(s(t)) - E_T) dt ).  Every dtau the population is reconfigured to
 * exactly Nw walkers by systematic resampling with probabilities w_i / sum w (population-control
 * bias O(1/Nw), checked by varying Nw against exact anchors).  The weighted population is the
 * mixed distribution ~ psi_0(s); an ancestor Kp steps back of the present population is distributed
 * as psi_0(s)^2 (forward walking), so every walker carries a ring buffer of its ancestors' observables
 * (transverse E(k) at axis momenta) and periodic state snapshots (dumped for pure structure factors).
 *
 * Estimators (lambda = 1):  E_mix = -<n_app>_w ,  E_growth = E_T - ln(W/Nw)/dtau ,
 *   S_T(k) pure = <|E_c(k)|^2 at lag Kp>_w ,  C_c(k,m) = <E_c(k)[lag Kp+m] E_c(k)^*[lag Kp]>_w  (tau = m dtau).
 * usage: gfmc geo Nw tau_equil tau_prod dtau K Kp kmax snap_every nsnap dump_every dump_walkers nbins seed corr_every outprefix
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdint.h>
#include <complex.h>

static uint64_t rs[4];
static inline uint64_t rotl(const uint64_t x, int k) { return (x << k) | (x >> (64 - k)); }
static uint64_t next_u64(void) { const uint64_t r = rotl(rs[1] * 5, 7) * 9; const uint64_t t = rs[1] << 17; rs[2] ^= rs[0]; rs[3] ^= rs[1]; rs[1] ^= rs[2]; rs[0] ^= rs[3]; rs[2] ^= t; rs[3] = rotl(rs[3], 45); return r; }
static double urand(void) { return (next_u64() >> 11) * (1.0 / 9007199254740992.0); }
static void seed_rng(uint64_t seed) { uint64_t z = seed; for (int i = 0; i < 4; i++) { z += 0x9e3779b97f4a7c15ULL; uint64_t x = z; x = (x ^ (x >> 30)) * 0xbf58476d1ce4e5b9ULL; x = (x ^ (x >> 27)) * 0x94d049bb133111ebULL; rs[i] = x ^ (x >> 31); } }

static int NL, NP, NV, Lx, Ly, Lz, is3d;
static int (*plq)[4]; static int *nbf_cnt, (*nbf)[13];
static int *lpos_x, *lpos_y, *lpos_z, *ldir;
static int *inc_cnt, (*inc_link)[8], (*inc_sign)[8], *rho2;
static unsigned char *init_bits;
static double Vrk = 0.0, Uc = 0.0; static int *cpart, *bpart;   /* P3: diagonal term V n_app + Uc sum_pairs E E'; forward/backward collinear partners */
static int cmp_int(const void *a, const void *b) { return (*(int *)a) - (*(int *)b); }

static void read_geo(const char *fn) {
    FILE *fh = fopen(fn, "r"); if (!fh) { fprintf(stderr, "cannot open %s\n", fn); exit(1); }
    if (fscanf(fh, "%d %d %d", &NL, &NP, &NV) != 3) exit(2);
    plq = malloc(sizeof(int[4]) * NP);
    for (int f = 0; f < NP; f++) if (fscanf(fh, "%d %d %d %d", &plq[f][0], &plq[f][1], &plq[f][2], &plq[f][3]) != 4) exit(3);
    init_bits = malloc(NL); char *buf = malloc(NL + 16); if (fscanf(fh, "%s", buf) != 1) exit(4);
    for (int j = 0; j < NL; j++) init_bits[j] = (buf[j] == '1'); free(buf);
    if (fscanf(fh, "%d %d %d", &Lx, &Ly, &Lz) != 3) exit(5);
    is3d = (Lx > 0);
    lpos_x = malloc(sizeof(int) * NL); lpos_y = malloc(sizeof(int) * NL); lpos_z = malloc(sizeof(int) * NL); ldir = malloc(sizeof(int) * NL);
    if (is3d) for (int j = 0; j < NL; j++) if (fscanf(fh, "%d %d %d %d", &lpos_x[j], &lpos_y[j], &lpos_z[j], &ldir[j]) != 4) exit(6);
    inc_cnt = malloc(sizeof(int) * NV); inc_link = malloc(sizeof(int[8]) * NV); inc_sign = malloc(sizeof(int[8]) * NV); rho2 = malloc(sizeof(int) * NV);
    for (int v = 0; v < NV; v++) { if (fscanf(fh, "%d", &inc_cnt[v]) != 1) exit(7); for (int a = 0; a < inc_cnt[v]; a++) if (fscanf(fh, "%d %d", &inc_link[v][a], &inc_sign[v][a]) != 2) exit(8); if (fscanf(fh, "%d", &rho2[v]) != 1) exit(9); }
    fclose(fh);
    int *lf_cnt = calloc(NL, sizeof(int)); int (*lf)[8] = malloc(sizeof(int[8]) * NL);
    for (int f = 0; f < NP; f++) for (int a = 0; a < 4; a++) { int j = plq[f][a]; lf[j][lf_cnt[j]++] = f; }
    nbf_cnt = calloc(NP, sizeof(int)); nbf = malloc(sizeof(int[13]) * NP);
    for (int f = 0; f < NP; f++) { int tmp[40], n = 0; tmp[n++] = f; for (int a = 0; a < 4; a++) { int j = plq[f][a]; for (int b = 0; b < lf_cnt[j]; b++) tmp[n++] = lf[j][b]; }
        qsort(tmp, n, sizeof(int), cmp_int); int m = 0; for (int i = 0; i < n; i++) if (i == 0 || tmp[i] != tmp[i - 1]) nbf[f][m++] = tmp[i]; nbf_cnt[f] = m; }
    free(lf_cnt); free(lf);
    cpart = malloc(sizeof(int) * NL); bpart = malloc(sizeof(int) * NL); for (int j = 0; j < NL; j++) cpart[j] = bpart[j] = -1;
    if (is3d) { int Ld[3] = {Lx, Ly, Lz}; for (int j = 0; j < NL; j++) { int d = ldir[j]; int px = lpos_x[j], py = lpos_y[j], pz = lpos_z[j]; if (d == 0) px = (px + 1) % Ld[0]; else if (d == 1) py = (py + 1) % Ld[1]; else pz = (pz + 1) % Ld[2];
        for (int m = 0; m < NL; m++) if (ldir[m] == d && lpos_x[m] == px && lpos_y[m] == py && lpos_z[m] == pz) { cpart[j] = m; bpart[m] = j; break; } } }
}
static inline int pairval(const unsigned char *b, int j) { int m = cpart[j]; if (m < 0) return 0; return ((b[j] ? 1 : -1) * (b[m] ? 1 : -1)); }
static int cval_full(const unsigned char *b) { int c = 0; for (int j = 0; j < NL; j++) c += pairval(b, j); return c; }
static inline int applicable(const unsigned char *b, int f) { int bp = b[plq[f][0]], bq = b[plq[f][1]], bu = b[plq[f][2]], bw = b[plq[f][3]]; return (bp == bq) && (bu == bw) && (bp != bu); }
static int gauss_residual(const unsigned char *b) { int worst = 0; for (int v = 0; v < NV; v++) { int tot = 0; for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (b[inc_link[v][a]] ? 1 : -1); int r = abs(tot - rho2[v]); if (r > worst) worst = r; } return worst; }

/* walker layout: one contiguous block */
static int NK, NCOMP, K, NSNAP;
static size_t WSZ, off_bits, off_list, off_pos, off_Ek, off_buf, off_snap;
typedef struct { int n_app; int cval; double logw; } WHead;
static inline double diag_of(const WHead *h) { return Vrk * h->n_app + Uc * 0.25 * h->cval; }
static inline unsigned char *w_bits(char *w) { return (unsigned char *)(w + off_bits); }
static inline int *w_list(char *w) { return (int *)(w + off_list); }
static inline int *w_pos(char *w) { return (int *)(w + off_pos); }
static inline double complex *w_Ek(char *w) { return (double complex *)(w + off_Ek); }
static inline float complex *w_buf(char *w) { return (float complex *)(w + off_buf); }
static inline unsigned char *w_snap(char *w) { return (unsigned char *)(w + off_snap); }
static double complex *ph; static int *k_d, *k_n; static double Ns;

static void walker_init(char *w, const unsigned char *bits) {
    WHead *h = (WHead *)w; h->logw = 0; h->n_app = 0;
    memcpy(w_bits(w), bits, NL); h->cval = cval_full(w_bits(w));
    int *list = w_list(w), *pos = w_pos(w);
    for (int f = 0; f < NP; f++) { if (applicable(w_bits(w), f)) { pos[f] = h->n_app; list[h->n_app++] = f; } else pos[f] = -1; }
    double complex *Ek = w_Ek(w);
    for (int kk = 0; kk < NK; kk++) for (int mu = 0; mu < 3; mu++) { double complex z = 0; for (int j = 0; j < NL; j++) if (ldir[j] == mu) z += ph[kk * NL + j] * (w_bits(w)[j] ? 0.5 : -0.5); Ek[kk * 3 + mu] = z; }
    memset(w_buf(w), 0, sizeof(float complex) * (size_t)K * NK * NCOMP);
    for (int s = 0; s < NSNAP; s++) memcpy(w_snap(w) + (size_t)s * NL, bits, NL);
}
static inline void walker_flip(char *w, int f) {
    WHead *h = (WHead *)w; unsigned char *b = w_bits(w); int *list = w_list(w), *pos = w_pos(w);
    int aff[8], na = 0; for (int a = 0; a < 4; a++) { int jl = plq[f][a]; aff[na++] = jl; if (bpart[jl] >= 0) aff[na++] = bpart[jl]; }
    for (int a = 0; a < na; a++) for (int c = 0; c < a; c++) if (aff[c] == aff[a]) { aff[a] = -1; break; }
    int before = 0; for (int a = 0; a < na; a++) if (aff[a] >= 0) before += pairval(b, aff[a]);
    for (int a = 0; a < 4; a++) { int jl = plq[f][a]; b[jl] ^= 1; double dE = b[jl] ? 1.0 : -1.0; double complex *Ek = w_Ek(w); for (int kk = 0; kk < NK; kk++) Ek[kk * 3 + ldir[jl]] += ph[kk * NL + jl] * dE; }
    int after = 0; for (int a = 0; a < na; a++) if (aff[a] >= 0) after += pairval(b, aff[a]); h->cval += after - before;
    for (int i = 0; i < nbf_cnt[f]; i++) { int g = nbf[f][i]; int val = applicable(b, g); int p = pos[g];
        if (val && p < 0) { pos[g] = h->n_app; list[h->n_app++] = g; }
        else if (!val && p >= 0) { int last = list[--h->n_app]; list[p] = last; pos[last] = p; pos[g] = -1; } }
}

int main(int argc, char **argv) {
    if (argc < 17) { fprintf(stderr, "usage: gfmc geo Nw tau_equil tau_prod dtau K Kp kmax snap_every nsnap dump_every dump_walkers nbins seed corr_every outprefix [nsub]\n"); return 1; }
    int nsub = (argc > 17) ? atoi(argv[17]) : 1;
    Vrk = (argc > 18) ? atof(argv[18]) : 0.0; Uc = (argc > 19) ? atof(argv[19]) : 0.0;   /* reconfigurations per dtau (weight spread per reconfiguration ~ exp(sigma_n dtau/nsub)) */
    const char *geo = argv[1]; int Nw = atoi(argv[2]); double tau_equil = atof(argv[3]), tau_prod = atof(argv[4]), dtau = atof(argv[5]);
    K = atoi(argv[6]); int Kp = atoi(argv[7]); int kmax = atoi(argv[8]); int snap_every = atoi(argv[9]); NSNAP = atoi(argv[10]);
    int dump_every = atoi(argv[11]); int dump_walkers = atoi(argv[12]); int nbins = atoi(argv[13]); uint64_t seed = strtoull(argv[14], NULL, 10); int corr_every = atoi(argv[15]); const char *outp = argv[16];
    read_geo(geo); seed_rng(seed);
    NK = is3d ? 3 * kmax : 1; NCOMP = is3d ? 2 : 1; Ns = is3d ? (double)(Lx * Ly * Lz) : (double)(NL / 3);
    ph = malloc(sizeof(double complex) * NK * NL); k_d = malloc(sizeof(int) * NK); k_n = malloc(sizeof(int) * NK);
    if (is3d) { int Ld[3] = {Lx, Ly, Lz}; for (int d = 0; d < 3; d++) for (int n = 1; n <= kmax; n++) { int kk = d * kmax + n - 1; k_d[kk] = d; k_n[kk] = n; double kv = 2 * M_PI * n / Ld[d];
        for (int j = 0; j < NL; j++) { int c = (d == 0) ? lpos_x[j] : (d == 1) ? lpos_y[j] : lpos_z[j]; ph[kk * NL + j] = cexp(-I * kv * c) / sqrt(Ns); } } }
    else { k_d[0] = 0; k_n[0] = 1; for (int j = 0; j < NL; j++) ph[j] = (j % 3 == 0) ? (((j / 3) % 2) ? -1.0 : 1.0) / sqrt(Ns) : 0.0; }
    int MC = K - Kp;   /* number of correlator lags */
    off_bits = sizeof(WHead); off_list = off_bits + ((NL + 7) / 8) * 8; off_pos = off_list + sizeof(int) * NP; off_Ek = off_pos + sizeof(int) * NP; off_Ek = (off_Ek + 15) / 16 * 16;
    off_buf = off_Ek + sizeof(double complex) * NK * 3; off_snap = off_buf + sizeof(float complex) * (size_t)K * NK * NCOMP; WSZ = off_snap + (size_t)NSNAP * NL; WSZ = (WSZ + 15) / 16 * 16;
    printf("# gfmc: geo=%s NL=%d NP=%d NV=%d Nw=%d tau_equil=%g tau_prod=%g dtau=%g K=%d Kp=%d (tau_proj=%g, corr lags %d -> tau %g) kmax=%d snap_every=%d nsnap=%d (snapshot lag %g) dump_every=%d dump_walkers=%d nbins=%d seed=%llu corr_every=%d walker_bytes=%zu nsub=%d (reconfigure every %g)\n",
           geo, NL, NP, NV, Nw, tau_equil, tau_prod, dtau, K, Kp, Kp * dtau, MC, MC * dtau, kmax, snap_every, NSNAP, (NSNAP - 1) * snap_every * dtau, dump_every, dump_walkers, nbins, (unsigned long long)seed, corr_every, WSZ, nsub, dtau / nsub);
    char *pool = malloc(WSZ * (size_t)Nw); if (!pool) { fprintf(stderr, "oom\n"); return 2; }
    for (int i = 0; i < Nw; i++) walker_init(pool + WSZ * i, init_bits);
    printf("# init: gauss residual=%d n_app=%d cval=%d (check %d) V=%g Uc=%g diag=%g\n", gauss_residual(init_bits), ((WHead *)pool)->n_app, ((WHead *)pool)->cval, cval_full(init_bits), Vrk, Uc, diag_of((WHead *)pool));
    double ET = ((WHead *)pool)->n_app - diag_of((WHead *)pool);   /* trial energy (-E), adapted to the growth estimate */
    long nsteps_eq = (long)(tau_equil / dtau + 0.5), nsteps_pr = (long)(tau_prod / dtau + 0.5), per_bin = nsteps_pr / nbins;
    int rpos = 0, spos = 0;    /* ring positions (global) */
    /* accumulators */
    double a_Emix = 0, a_Egr = 0, a_cnt = 0, a_nappP = 0;
    double *a_Smix = calloc(NK * NCOMP, sizeof(double)), *a_Spure = calloc(NK * NCOMP, sizeof(double)), *a_SL = calloc(NK, sizeof(double));
    double *a_C = calloc((size_t)NK * NCOMP * MC, sizeof(double)); double a_Ccnt = 0;
    double *cum = malloc(sizeof(double) * Nw); int *copies = malloc(sizeof(int) * Nw);
    char fn[512]; snprintf(fn, sizeof fn, "%s.bins", outp); FILE *fb = fopen(fn, "w");
    FILE *fd = NULL; if (dump_every > 0) { snprintf(fn, sizeof fn, "%s.dump", outp); fd = fopen(fn, "wb"); }
    fprintf(fb, "# columns: bin E_mix E_growth cval_mix | S_mix(k,c) | S_pure(k,c) | S_L_pure(k) | C(k,c,m) m=0..%d | ncopies_max\n", MC - 1);
    fprintf(fb, "# NK=%d NCOMP=%d MC=%d dtau=%g Kp=%d k_d=", NK, NCOMP, MC, dtau, Kp);
    for (int kk = 0; kk < NK; kk++) fprintf(fb, "%d:%d ", k_d[kk], k_n[kk]); fprintf(fb, "\n");
    long total = nsteps_eq + nsteps_pr; int bin = 0; long gauss_err = 0, ndump = 0; double maxcopies_bin = 0; double Wmin = 1e300, Wmax = 0;
    for (long step = 0; step < total; step++) {
        /* evolve every walker for dtau in nsub sub-steps, reconfiguring after each sub-step but the last */
        double lnW_sum = 0;
        for (int sub = 0; sub < nsub; sub++) {
            double dts = dtau / nsub;
            for (int i = 0; i < Nw; i++) {
                char *w = pool + WSZ * i; WHead *h = (WHead *)w; double t = 0;
                while (1) {
                    double rate = h->n_app, dg = diag_of(h);
                    if (rate <= 0) { h->logw += (-dg - ET) * (dts - t); break; }
                    double dt = -log(1.0 - urand()) / rate;
                    if (t + dt >= dts) { h->logw += (rate - dg - ET) * (dts - t); break; }
                    h->logw += (rate - dg - ET) * dt; t += dt;
                    walker_flip(w, w_list(w)[(int)(urand() * h->n_app)]);
                }
            }
            if (sub < nsub - 1) {
                double lm = -1e300; for (int i = 0; i < Nw; i++) { double l = ((WHead *)(pool + WSZ * i))->logw; if (l > lm) lm = l; }
                double Ws = 0; for (int i = 0; i < Nw; i++) { double wi = exp(((WHead *)(pool + WSZ * i))->logw - lm); cum[i] = wi; Ws += wi; }
                lnW_sum += log(Ws / Nw) + lm;
                double u = urand() / Nw, acc = 0; int j = 0;
                for (int i = 0; i < Nw; i++) { acc += cum[i] / Ws; int c = 0; while (j < Nw && u + (double)j / Nw < acc) { c++; j++; } copies[i] = c; }
                int dead_i = 0;
                for (int i = 0; i < Nw; i++) { if (copies[i] <= 1) continue;
                    for (int c = 1; c < copies[i]; c++) { while (dead_i < Nw && copies[dead_i] != 0) dead_i++; if (dead_i >= Nw) break; memcpy(pool + WSZ * dead_i, pool + WSZ * i, WSZ); copies[dead_i] = 1; } }
                for (int i = 0; i < Nw; i++) ((WHead *)(pool + WSZ * i))->logw = 0;
            }
        }
        for (int i = 0; i < Nw; i++) {
            char *w = pool + WSZ * i;
            /* push observables into the ring */
            float complex *buf = w_buf(w) + (size_t)rpos * NK * NCOMP; double complex *Ek = w_Ek(w);
            for (int kk = 0; kk < NK; kk++) for (int c = 0; c < NCOMP; c++) { int mu = is3d ? ((k_d[kk] + 1 + c) % 3) : 0; buf[kk * NCOMP + c] = (float complex)Ek[kk * 3 + mu]; }
            if (step % snap_every == 0) memcpy(w_snap(w) + (size_t)spos * NL, w_bits(w), NL);
        }
        /* weights */
        double lmax = -1e300; for (int i = 0; i < Nw; i++) { double l = ((WHead *)(pool + WSZ * i))->logw; if (l > lmax) lmax = l; }
        double W = 0; for (int i = 0; i < Nw; i++) { double wi = exp(((WHead *)(pool + WSZ * i))->logw - lmax); cum[i] = wi; W += wi; }
        double a_growth = ET + (lnW_sum + log(W / Nw) + lmax) / dtau;   /* estimate of a0 = -E_0 over the whole step */
        double Egrowth = -a_growth;
        int measuring = (step >= nsteps_eq) && (step >= K);
        if (measuring) {
            double emix = 0, nappP = 0;
            for (int i = 0; i < Nw; i++) { char *w = pool + WSZ * i; double wi = cum[i] / W; emix += wi * (((WHead *)w)->n_app - diag_of((WHead *)w)); nappP += wi * ((WHead *)w)->cval;
                float complex *b0 = w_buf(w) + (size_t)rpos * NK * NCOMP;
                int lagpos = (rpos - Kp + K) % K; float complex *bp = w_buf(w) + (size_t)lagpos * NK * NCOMP;
                for (int q = 0; q < NK * NCOMP; q++) { a_Smix[q] += wi * crealf(b0[q] * conjf(b0[q])); a_Spure[q] += wi * crealf(bp[q] * conjf(bp[q])); }
                /* longitudinal: not buffered (zero by Gauss); computed from the current Ek for the record */
                double complex *Ek = w_Ek(w); for (int kk = 0; kk < NK; kk++) { double complex zl = Ek[kk * 3 + k_d[kk]]; a_SL[kk] += wi * creal(zl * conj(zl)); }
                if (step % corr_every == 0) {
                    for (int m = 0; m < MC; m++) { int lp2 = (rpos - Kp - m + 2 * K) % K; float complex *bm = w_buf(w) + (size_t)lp2 * NK * NCOMP;
                        for (int q = 0; q < NK * NCOMP; q++) a_C[q * MC + m] += wi * crealf(bm[q] * conjf(bp[q])); }
                }
            }
            a_Emix += -emix; a_Egr += Egrowth; a_nappP += nappP; a_cnt += 1; if (step % corr_every == 0) a_Ccnt += 1;
            if (W < Wmin) Wmin = W; if (W > Wmax) Wmax = W;
            if (fd && dump_every > 0 && ((step - nsteps_eq) % dump_every == 0)) {
                int oldest = (spos + 1) % NSNAP;   /* the slot about to be overwritten next = oldest */
                for (int i = 0; i < Nw; i += (Nw / dump_walkers > 0 ? Nw / dump_walkers : 1)) { unsigned char *s = w_snap(pool + WSZ * i) + (size_t)oldest * NL; if (gauss_residual(s)) gauss_err++; if (cval_full(w_bits(pool + WSZ * i)) != ((WHead *)(pool + WSZ * i))->cval) gauss_err += 1000000; fwrite(s, 1, NL, fd); ndump++; }
            }
        }
        /* reconfiguration: systematic resampling */
        double u = urand() / Nw, acc = 0; int j = 0, maxc = 0;
        for (int i = 0; i < Nw; i++) { acc += cum[i] / W; int c = 0; while (j < Nw && u + (double)j / Nw < acc) { c++; j++; } copies[i] = c; if (c > maxc) maxc = c; }
        if (maxc > maxcopies_bin) maxcopies_bin = maxc;
        /* survivors stay, dead slots receive copies */
        int dead_i = 0;
        for (int i = 0; i < Nw; i++) {
            if (copies[i] <= 1) continue;
            for (int c = 1; c < copies[i]; c++) { while (dead_i < Nw && copies[dead_i] != 0) dead_i++; if (dead_i >= Nw) break; memcpy(pool + WSZ * dead_i, pool + WSZ * i, WSZ); copies[dead_i] = 1; }
        }
        for (int i = 0; i < Nw; i++) ((WHead *)(pool + WSZ * i))->logw = 0;
        ET = 0.9 * ET + 0.1 * a_growth;
        rpos = (rpos + 1) % K; if (step % snap_every == 0) spos = (spos + 1) % NSNAP;
        if (measuring && ((step - nsteps_eq + 1) % per_bin == 0)) {
            fprintf(fb, "%d %.10f %.10f %.6f |", bin, a_Emix / a_cnt, a_Egr / a_cnt, a_nappP / a_cnt);
            for (int q = 0; q < NK * NCOMP; q++) fprintf(fb, " %.10f", a_Smix[q] / a_cnt); fprintf(fb, " |");
            for (int q = 0; q < NK * NCOMP; q++) fprintf(fb, " %.10f", a_Spure[q] / a_cnt); fprintf(fb, " |");
            for (int kk = 0; kk < NK; kk++) fprintf(fb, " %.3e", a_SL[kk] / a_cnt); fprintf(fb, " |");
            for (int q = 0; q < NK * NCOMP; q++) for (int m = 0; m < MC; m++) fprintf(fb, " %.10f", a_C[q * MC + m] / a_Ccnt); fprintf(fb, " | %g\n", maxcopies_bin);
            fflush(fb);
            a_Emix = a_Egr = a_cnt = a_Ccnt = a_nappP = 0; memset(a_Smix, 0, sizeof(double) * NK * NCOMP); memset(a_Spure, 0, sizeof(double) * NK * NCOMP); memset(a_SL, 0, sizeof(double) * NK); memset(a_C, 0, sizeof(double) * NK * NCOMP * MC); maxcopies_bin = 0; bin++;
        }
    }
    fclose(fb); if (fd) fclose(fd);
    printf("# final: ET=%.6f gauss_err(dumps)=%ld dumps=%ld W range per step [%.3g, %.3g] (relative to Nw=%d)\n", ET, gauss_err, ndump, Wmin, Wmax, Nw);
    return 0;
}
"""

C_T422D = r"""/* Exact, seed-free 4x2x2 engine: Gauss-sector enumeration, winding census, flip component,
 * Perron vector of B = I + A on the component, transverse structure factors and the exact
 * transverse-electric decay rates.  Reads the .geo written by the runner's own indexing.
 * usage: t422x geo mmax                                                                     */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <math.h>

static int NL, NP, NV, Lx, Ly, Lz;
static int (*plq)[4];
static int *lpx, *lpy, *lpz, *ldir;
static int *inc_cnt, (*inc_link)[8], (*inc_sign)[8], *rho2;
static unsigned char *initb;
static double Vrk = 0.0, Uc = 0.0; static int *cpart; static int8_t *cval; static double Dmin = 0, Dmax = 0;   /* P3 diagonal term */
static int (*newl)[8], *newl_cnt;
static uint64_t *St; static int64_t nst = 0; static int counting = 1; static int64_t ncount = 0;

static void read_geo(const char *fn) {
    FILE *fh = fopen(fn, "r"); if (!fh) { fprintf(stderr, "no geo\n"); exit(1); }
    if (fscanf(fh, "%d %d %d", &NL, &NP, &NV) != 3) exit(2);
    plq = malloc(sizeof(int[4]) * NP);
    for (int f = 0; f < NP; f++) if (fscanf(fh, "%d %d %d %d", &plq[f][0], &plq[f][1], &plq[f][2], &plq[f][3]) != 4) exit(3);
    char *buf = malloc(NL + 16); if (fscanf(fh, "%s", buf) != 1) exit(4);
    initb = malloc(NL); for (int j = 0; j < NL; j++) initb[j] = (buf[j] == '1');
    if (fscanf(fh, "%d %d %d", &Lx, &Ly, &Lz) != 3) exit(5);
    lpx = malloc(sizeof(int) * NL); lpy = malloc(sizeof(int) * NL); lpz = malloc(sizeof(int) * NL); ldir = malloc(sizeof(int) * NL);
    for (int j = 0; j < NL; j++) if (fscanf(fh, "%d %d %d %d", &lpx[j], &lpy[j], &lpz[j], &ldir[j]) != 4) exit(6);
    inc_cnt = malloc(sizeof(int) * NV); inc_link = malloc(sizeof(int[8]) * NV); inc_sign = malloc(sizeof(int[8]) * NV); rho2 = malloc(sizeof(int) * NV);
    for (int v = 0; v < NV; v++) {
        if (fscanf(fh, "%d", &inc_cnt[v]) != 1) exit(7);
        for (int a = 0; a < inc_cnt[v]; a++) if (fscanf(fh, "%d %d", &inc_link[v][a], &inc_sign[v][a]) != 2) exit(8);
        if (fscanf(fh, "%d", &rho2[v]) != 1) exit(9);
    }
    fclose(fh);
}

static void rec(int v, uint64_t bits) {
    if (v == NV) { if (counting) ncount++; else St[nst++] = bits; return; }
    int k = newl_cnt[v];
    for (int m = 0; m < (1 << k); m++) {
        uint64_t b = bits;
        for (int a = 0; a < k; a++) if ((m >> a) & 1) b |= 1ULL << newl[v][a];
        int tot = 0;
        for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (((b >> inc_link[v][a]) & 1) ? 1 : -1);
        if (tot == rho2[v]) rec(v + 1, b);
    }
}
static int cmp64(const void *a, const void *b) { uint64_t x = *(const uint64_t *)a, y = *(const uint64_t *)b; return (x < y) ? -1 : (x > y); }

static int64_t M; static uint64_t *S; static int64_t *rowptr; static int32_t *col; static int8_t *napp;
static int64_t bs(const uint64_t *arr, int64_t n, uint64_t x) {
    int64_t lo = 0, hi = n - 1;
    while (lo <= hi) { int64_t mid = (lo + hi) >> 1; if (arr[mid] == x) return mid; if (arr[mid] < x) lo = mid + 1; else hi = mid - 1; }
    return -1;
}
static void matvec_A(const double *x, double *y) {
    for (int64_t i = 0; i < M; i++) { double s = 0; for (int64_t p = rowptr[i]; p < rowptr[i + 1]; p++) s += x[col[p]]; y[i] = s; }
}
static inline double diag_i(int64_t i) { return Vrk * napp[i] + Uc * 0.25 * cval[i]; }
/* y = (A - (D - Dmin)) x  : minus the Hamiltonian, shifted so the diagonal is <= 0 */
static void matvec_H(const double *x, double *y) { matvec_A(x, y); for (int64_t i = 0; i < M; i++) y[i] -= (diag_i(i) - Dmin) * x[i]; }

int main(int argc, char **argv) {
    if (argc < 3) { fprintf(stderr, "usage: t422x geo mmax [V Uc]\n"); return 1; }
    if (argc > 4) { Vrk = atof(argv[3]); Uc = atof(argv[4]); }
    read_geo(argv[1]);
    int mmax = atoi(argv[2]);
    newl = malloc(sizeof(int[8]) * NV); newl_cnt = calloc(NV, sizeof(int));
    char *seen = calloc(NL, 1);
    for (int v = 0; v < NV; v++) for (int q = 0; q < inc_cnt[v]; q++) { int j = inc_link[v][q]; if (!seen[j]) { seen[j] = 1; newl[v][newl_cnt[v]++] = j; } }
    counting = 1; rec(0, 0);
    int64_t n = ncount;
    St = malloc(8 * (size_t)n); if (!St) { fprintf(stderr, "oom states\n"); return 2; }
    counting = 0; rec(0, 0);
    qsort(St, n, 8, cmp64);
    int64_t dup = 0; for (int64_t i = 1; i < n; i++) if (St[i] <= St[i - 1]) dup++;
    printf("dim_gauss=%lld sorted_unique=%d\n", (long long)n, dup == 0);
    /* re-derive Gauss on every state */
    int64_t bad = 0;
    for (int64_t i = 0; i < n; i++) {
        uint64_t b = St[i];
        for (int v = 0; v < NV; v++) { int tot = 0; for (int a = 0; a < inc_cnt[v]; a++) tot += inc_sign[v][a] * (((b >> inc_link[v][a]) & 1) ? 1 : -1); if (tot != rho2[v]) { bad++; break; } }
    }
    printf("gauss_violations=%lld\n", (long long)bad);
    /* winding class of every state; key = (Wx+8)*289 + (Wy+8)*17 + (Wz+8) */
    int nwl[3] = {0, 0, 0}; int wlink[3][16];
    for (int j = 0; j < NL; j++) { int d = ldir[j]; int c = (d == 0) ? lpx[j] : (d == 1 ? lpy[j] : lpz[j]); if (c == 0) wlink[d][nwl[d]++] = j; }
    int *wcount = calloc(4913, sizeof(int));
    int32_t *key = malloc(4 * (size_t)n);
    uint64_t fmask[64];
    for (int f = 0; f < NP; f++) fmask[f] = (1ULL << plq[f][0]) | (1ULL << plq[f][1]) | (1ULL << plq[f][2]) | (1ULL << plq[f][3]);
    int8_t *nap = malloc((size_t)n);
    int64_t frozen = 0, frozen0 = 0;
    for (int64_t i = 0; i < n; i++) {
        uint64_t b = St[i]; int W[3];
        for (int d = 0; d < 3; d++) { int t = 0; for (int q = 0; q < nwl[d]; q++) t += ((b >> wlink[d][q]) & 1) ? 1 : -1; W[d] = t / 2; }
        int32_t k = (W[0] + 8) * 289 + (W[1] + 8) * 17 + (W[2] + 8);
        key[i] = k; wcount[k]++;
        int na = 0;
        for (int f = 0; f < NP; f++) { int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1; if (bp == bq && bu == bw && bp != bu) na++; }
        nap[i] = (int8_t)na;
        if (na == 0) { frozen++; if (k == 8 * 289 + 8 * 17 + 8) frozen0++; }
    }
    int ndist = 0, wmax = 0;
    for (int i = 0; i < 4913; i++) { if (wcount[i]) ndist++; if (wcount[i] > wmax) wmax = wcount[i]; }
    int32_t k0 = 8 * 289 + 8 * 17 + 8;
    printf("winding_classes=%d zero_winding=%d w100=%d w010=%d w001=%d largest_class=%d\n",
           ndist, wcount[k0], wcount[k0 + 289], wcount[k0 + 17], wcount[k0 + 1], wmax);
    printf("frozen_total=%lld frozen_zero_winding=%lld\n", (long long)frozen, (long long)frozen0);
    /* BFS from the ice state */
    uint64_t ice = 0; for (int j = 0; j < NL; j++) if (initb[j]) ice |= 1ULL << j;
    int64_t i0 = bs(St, n, ice); if (i0 < 0) { fprintf(stderr, "ice not in sector\n"); return 3; }
    printf("ice_key_is_zero=%d ice_napp=%d\n", key[i0] == k0, (int)nap[i0]);
    unsigned char *vis = calloc((n + 7) / 8, 1);
    int64_t *queue = malloc(8 * 2000000); int64_t qcap = 2000000, qn = 0;
    vis[i0 >> 3] |= 1 << (i0 & 7); queue[qn++] = i0;
    int64_t lstart = 0, lend = 1; int depth = 0;
    while (lstart < lend) {
        for (int64_t p = lstart; p < lend; p++) {
            uint64_t b = St[queue[p]];
            for (int f = 0; f < NP; f++) {
                int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1;
                if (!(bp == bq && bu == bw && bp != bu)) continue;
                int64_t j = bs(St, n, b ^ fmask[f]);
                if (j < 0) { fprintf(stderr, "missing target in sector\n"); return 4; }
                if (!(vis[j >> 3] & (1 << (j & 7)))) {
                    vis[j >> 3] |= 1 << (j & 7);
                    if (qn == qcap) { qcap *= 2; queue = realloc(queue, 8 * qcap); }
                    queue[qn++] = j;
                }
            }
        }
        lstart = lend; lend = qn; depth++;
    }
    printf("component=%lld bfs_depth=%d zero_minus_comp_minus_frozen0=%lld\n", (long long)qn, depth, (long long)(wcount[k0] - qn - frozen0));
    /* extract the component, free the sector */
    M = qn;
    S = malloc(8 * (size_t)M);
    int64_t mm = 0; for (int64_t i = 0; i < n; i++) if (vis[i >> 3] & (1 << (i & 7))) S[mm++] = St[i];
    int allzero = 1; for (int64_t i = 0; i < n; i++) if ((vis[i >> 3] & (1 << (i & 7))) && key[i] != k0) { allzero = 0; break; }
    printf("component_all_zero_winding=%d\n", allzero);
    free(St); free(key); free(vis); free(queue); free(nap); St = NULL;
    /* CSR adjacency */
    rowptr = malloc(8 * (size_t)(M + 1)); napp = malloc((size_t)M);
    int64_t nnz = 0;
    for (int64_t i = 0; i < M; i++) {
        uint64_t b = S[i]; int na = 0;
        for (int f = 0; f < NP; f++) { int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1; if (bp == bq && bu == bw && bp != bu) na++; }
        napp[i] = (int8_t)na; rowptr[i] = nnz; nnz += na;
    }
    rowptr[M] = nnz;
    col = malloc(4 * (size_t)nnz);
    int64_t missing = 0;
    for (int64_t i = 0; i < M; i++) {
        uint64_t b = S[i]; int64_t p = rowptr[i];
        for (int f = 0; f < NP; f++) {
            int bp = (b >> plq[f][0]) & 1, bq = (b >> plq[f][1]) & 1, bu = (b >> plq[f][2]) & 1, bw = (b >> plq[f][3]) & 1;
            if (bp == bq && bu == bw && bp != bu) { int64_t j = bs(S, M, b ^ fmask[f]); if (j < 0) { missing++; j = i; } col[p++] = (int32_t)j; }
        }
    }
    printf("nnz=%lld missing_targets=%lld\n", (long long)nnz, (long long)missing);
    cpart = malloc(sizeof(int) * NL); { int Ld[3] = {Lx, Ly, Lz}; for (int j = 0; j < NL; j++) { int d = ldir[j]; int px = lpx[j], py = lpy[j], pz = lpz[j]; if (d == 0) px = (px + 1) % Ld[0]; else if (d == 1) py = (py + 1) % Ld[1]; else pz = (pz + 1) % Ld[2]; cpart[j] = -1;
        for (int m = 0; m < NL; m++) if (ldir[m] == d && lpx[m] == px && lpy[m] == py && lpz[m] == pz) { cpart[j] = m; break; } } }
    cval = malloc((size_t)M); Dmin = 1e300; Dmax = -1e300;
    for (int64_t i = 0; i < M; i++) { int c = 0; for (int j = 0; j < NL; j++) { int m = cpart[j]; if (m >= 0) c += (((S[i] >> j) & 1) ? 1 : -1) * (((S[i] >> m) & 1) ? 1 : -1); } cval[i] = (int8_t)c; double d = diag_i(i); if (d < Dmin) Dmin = d; if (d > Dmax) Dmax = d; }
    double dpow = (Dmax - Dmin > 1e-12) ? 1.0 / (Dmax - Dmin) : 1.0;   /* B = I + dpow (A - (D - Dmin)) is entrywise non-negative */
    printf("diag: V=%g Uc=%g Dmin=%.6f Dmax=%.6f dpow=%.6f\n", Vrk, Uc, Dmin, Dmax, dpow);
    /* Perron vector of B = I + A by power iteration */
    double *x = malloc(8 * (size_t)M), *y = malloc(8 * (size_t)M);
    for (int64_t i = 0; i < M; i++) x[i] = 1.0 / sqrt((double)M);
    double lam = 0, lam_old = -1; int it;
    for (it = 0; it < 5000; it++) {
        matvec_H(x, y);
        for (int64_t i = 0; i < M; i++) y[i] = x[i] + dpow * y[i];
        double nrm = 0, rq = 0;
        for (int64_t i = 0; i < M; i++) { nrm += y[i] * y[i]; rq += x[i] * y[i]; }
        nrm = sqrt(nrm); lam = rq;
        for (int64_t i = 0; i < M; i++) x[i] = y[i] / nrm;
        if (fabs(lam - lam_old) < 1e-14 && it > 40) break;
        if (it == 4999) fprintf(stderr, "power iteration did not converge\n");
        lam_old = lam;
    }
    matvec_H(x, y); double ray = 0, res = 0;
    for (int64_t i = 0; i < M; i++) ray += x[i] * y[i];
    for (int64_t i = 0; i < M; i++) { double d = y[i] - ray * x[i]; res += d * d; }
    double nap0 = 0, sx = 0, snx = 0, cv0 = 0;
    for (int64_t i = 0; i < M; i++) { nap0 += x[i] * x[i] * napp[i]; cv0 += x[i] * x[i] * cval[i]; sx += x[i]; snx += x[i] * (napp[i] - (diag_i(i) - Dmin)); }
    printf("power_it=%d E0=%.10f rayleigh_a0=%.10f residual=%.2e napp0=%.10f mixed=%.10f Pf=%.10f cval0=%.10f  [E0 = -ray + Dmin; Dmin=%.6f]\n",
           it, -ray + Dmin, ray, sqrt(res), nap0, -snx / sx + Dmin, nap0 / NP, cv0, Dmin);
    /* structure factors and exact decay rates at k = (2 pi q / Lx, 0, 0) */
    double Ns = (double)(Lx * Ly * Lz);
    double *orr = malloc(8 * (size_t)M), *oii = malloc(8 * (size_t)M);
    double *ar = malloc(8 * (size_t)M), *ai = malloc(8 * (size_t)M), *tr = malloc(8 * (size_t)M), *ti = malloc(8 * (size_t)M);
    double delta = 0.25; if (0.5 / (Dmax - Dmin + 1e-9) < delta) delta = 0.5 / (Dmax - Dmin + 1e-9); double lamd = 1.0 + delta * ray; printf("corr delta=%.6f lamd=%.6f\n", delta, lamd);
    for (int q = 1; q <= Lx / 2; q++) {
        double kv = 2 * M_PI * q / Lx;
        for (int mu = 0; mu < 3; mu++) {
            for (int64_t i = 0; i < M; i++) {
                double zr = 0, zi = 0;
                for (int j = 0; j < NL; j++) if (ldir[j] == mu) { double e = ((S[i] >> j) & 1) ? 0.5 : -0.5; zr += cos(kv * lpx[j]) * e; zi += -sin(kv * lpx[j]) * e; }
                orr[i] = zr / sqrt(Ns) * x[i]; oii[i] = zi / sqrt(Ns) * x[i];
            }
            double s = 0; for (int64_t i = 0; i < M; i++) s += orr[i] * orr[i] + oii[i] * oii[i];
            printf("S q=%d mu=%d val=%.10f\n", q, mu, s);
            if (mu == 0) continue;
            if (mu == 2) continue;       /* S_zz equals S_yy by the y<->z symmetry, checked at mu=2 above */
            memcpy(ar, orr, 8 * (size_t)M); memcpy(ai, oii, 8 * (size_t)M);
            double c0 = s, cprev = s;
            for (int m = 1; m <= mmax; m++) {
                matvec_H(ar, tr); matvec_H(ai, ti);
                for (int64_t i = 0; i < M; i++) { ar[i] = (ar[i] + delta * tr[i]) / lamd; ai[i] = (ai[i] + delta * ti[i]) / lamd; }   /* P3: normalise each step (no overflow at large m) */
                double cm = 0; for (int64_t i = 0; i < M; i++) cm += orr[i] * ar[i] + oii[i] * ai[i];
                if (m % 40 == 0 || m == mmax) printf("omega q=%d m=%d ratio=%.10f omega_eff=%.6f\n", q, m, cm / c0, lamd * (1.0 - cm / cprev) / delta);
                cprev = cm;
            }
        }
    }
    return 0;
}
"""


# --- C1: the exact 2x2x2 ice component with the stand-in (no compiler needed) -
g2 = torus3d(2, 2, 2)
ice2 = ice_config(g2)
comp = [ice2]
seen = {ice2: 0}
for s in comp:
    for f, s2 in g2.flips(s):
        if s2 not in seen:
            seen[s2] = len(comp)
            comp.append(s2)
MC2 = len(comp)
A2 = np.zeros((MC2, MC2))
for i, s in enumerate(comp):
    for f, s2 in g2.flips(s):
        A2[i, seen[s2]] += 1
napp2 = np.array([g2.n_app(s) for s in comp], float)
cv2 = np.array([cval_of(g2, s) for s in comp], float)
Ev2 = np.array([[0.5 if (s >> j) & 1 else -0.5 for j in range(g2.NL)] for s in comp])
ph2 = {mu: np.array([np.cos(np.pi * g2.pos[j][0]) if g2.ldir[j] == mu else 0.0
                     for j in range(g2.NL)]) / np.sqrt(8.0) for mu in range(3)}
VU = ((0.0, 0.0), (0.9, 0.0), (0.0, 0.5), (0.0, 1.0), (0.0, -0.5))
EX = {}
for (V, Uc) in VU:
    w, Uv = np.linalg.eigh(-A2 + np.diag(V * napp2 + Uc * 0.25 * cv2))
    psi = Uv[:, 0]
    p2 = psi ** 2
    EX[(V, Uc)] = dict(E0=float(w[0]), gap=float(w[1] - w[0]), napp=float(p2 @ napp2),
                       cval=float(p2 @ cv2), cmix=float((psi @ cv2) / psi.sum()),
                       S=[float(p2 @ ((Ev2 @ ph2[mu]) ** 2)) for mu in range(3)])

check("C1 [exact] the SUPPLIED stand-in, NOT what the fermion produces, on the complete %d-state 2x2x2 ice "
      "component: E_0 = %.6f, %.6f, %.6f, %.6f, %.6f and S_yy(pi,0,0) = %.6f, %.6f, %.6f, %.6f, %.6f at "
      "(V, Uc) = (0,0), (0.9,0), (0,0.5), (0,1), (0,-0.5); Uc > 0 lowers S_T, Uc < 0 raises it"
      % (MC2, EX[(0.0, 0.0)]["E0"], EX[(0.9, 0.0)]["E0"], EX[(0.0, 0.5)]["E0"], EX[(0.0, 1.0)]["E0"],
         EX[(0.0, -0.5)]["E0"], EX[(0.0, 0.0)]["S"][1], EX[(0.9, 0.0)]["S"][1], EX[(0.0, 0.5)]["S"][1],
         EX[(0.0, 1.0)]["S"][1], EX[(0.0, -0.5)]["S"][1]),
      MC2 == 864
      and allnear([EX[k]["E0"] for k in VU], [-9.026721, -0.810822, -9.037853, -9.388780, -9.584715], 5e-6)
      and allnear([EX[k]["S"][1] for k in VU], [0.253037, 0.395643, 0.228492, 0.208281, 0.280059], 5e-6)
      and near(EX[(0.0, 0.0)]["E0"], -9.0267209135, 1e-9)
      and EX[(0.0, 1.0)]["S"][1] < EX[(0.0, 0.5)]["S"][1] < EX[(0.0, 0.0)]["S"][1] < EX[(0.0, -0.5)]["S"][1])


# --- the compiler ------------------------------------------------------------
def find_compiler():
    for cc in (os.environ.get("CC"), "cc", "gcc", "clang"):
        if cc and shutil.which(cc):
            return cc
    return None


CC = find_compiler()
TMP = tempfile.mkdtemp(prefix="fermion_screens_link_")
EXE = {}
cc_reason = ""
if CC is None:
    cc_reason = "no C compiler on PATH (tried $CC, cc, gcc, clang)"
else:
    for name, src in (("gfmc_d", C_GFMC_D), ("t422d", C_T422D)):
        path = os.path.join(TMP, name + ".c")
        with open(path, "w") as fh:
            fh.write(src)
        cp = subprocess.run([CC, "-O2", "-o", os.path.join(TMP, name), path, "-lm"],
                            capture_output=True, text=True, timeout=180)
        if cp.returncode != 0:
            CC = None
            cc_reason = "the embedded %s.c did not compile: %s" % (name, cp.stderr.strip()[-160:])
            break
        EXE[name] = os.path.join(TMP, name)

if CC is not None:
    GEO2 = os.path.join(TMP, "t222.geo")
    write_geo(g2, GEO2, ice2)
    g4 = torus3d(4, 2, 2)
    GEO4 = os.path.join(TMP, "t422.geo")
    write_geo(g4, GEO4, ice_config(g4))
    gL4 = torus3d(4, 4, 4)
    GEOL4 = os.path.join(TMP, "t444.geo")
    write_geo(gL4, GEOL4, ice_config(gL4))


def bins_of(path):
    rows = []
    for line in open(path):
        if line.startswith("#") or not line.strip():
            continue
        rows.append([[float(x) for x in blk.split()] for blk in line.split("|")])
    return rows


def ms(v):
    v = np.asarray(v, float)
    return float(v.mean()), float(v.std(ddof=1) / math.sqrt(len(v)))


def run_gfmc(geo, Nw, teq, tpr, dtau, K, Kp, kmax, seed, tag, V, Uc, nbins=20):
    out = os.path.join(TMP, tag)
    r = subprocess.run([EXE["gfmc_d"], geo, str(Nw), str(teq), str(tpr), str(dtau), str(K), str(Kp),
                        str(kmax), "4", "4", "0", "0", str(nbins), str(seed), "1", out, "1", str(V), str(Uc)],
                       capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    d = bins_of(out + ".bins")
    npure = len(d[0][2])
    fin = [l for l in r.stdout.splitlines() if l.startswith("# final")][0]
    return dict(E=ms([x[0][1] for x in d]), Eg=ms([x[0][2] for x in d]), cv=ms([x[0][3] for x in d]),
                Sp=[ms([x[2][q] for x in d]) for q in range(npure)],
                Cor=[ms([x[4][q] for x in d]) for q in range(len(d[0][4]))],
                SL=max(abs(v) for x in d for v in x[3]), maxc=max(x[5][0] for x in d), nbin=len(d),
                gauss=int(fin.split("gauss_err(dumps)=")[1].split()[0]))


def sig(m, e, x):
    return (m - x) / e if e > 0 else float("inf")


def t422(mmax, V, Uc):
    r = subprocess.run([EXE["t422d"], GEO4, str(mmax), str(V), str(Uc)],
                       capture_output=True, text=True, timeout=AUDIT_TIMEOUT_SEC)
    if r.returncode != 0:
        raise RuntimeError(r.stderr[-300:])
    d = {}
    for line in r.stdout.splitlines():
        for tok in line.replace("dim_gauss=", "dim=").split():
            if "=" in tok:
                k, v = tok.split("=", 1)
                try:
                    d.setdefault(k, []).append(float(v))
                except ValueError:
                    pass
        p = dict(x.split("=", 1) for x in line.split() if "=" in x)
        if line.startswith("S q="):
            d["S%s_%s" % (p["q"], p["mu"])] = float(p["val"])
        if line.startswith("omega q="):
            d.setdefault("om%s" % p["q"], []).append((int(p["m"]), float(p["omega_eff"])))
    return d


# --- C2-C5 -------------------------------------------------------------------
if CC is None:
    for lab, txt in (("C2 [witness] the patched walker engine against the exact 2x2x2 rows", ""),
                     ("C3 [exact] the 4x2x2 regression at Uc = 0", ""),
                     ("C4 [exact] the 4x2x2 rows with the supplied stiffness at Uc = 1", ""),
                     ("C5 [witness] the short L = 4 pair", "")):
        skip(lab, cc_reason)
else:
    W = {}
    for (V, Uc), sd in zip(VU, SEED_VAL):
        W[(V, Uc)] = run_gfmc(GEO2, 1600, 20, 400, 0.05, 200, 120, 1, sd, "v%s_%s" % (V, Uc), V, Uc)
    sg = []
    for k in VU:
        a, x = W[k], EX[k]
        sg += [sig(a["E"][0], a["E"][1], x["E0"]), sig(a["Eg"][0], a["Eg"][1], x["E0"]),
               sig(a["Sp"][0][0], a["Sp"][0][1], x["S"][1]), sig(a["Sp"][1][0], a["Sp"][1][1], x["S"][2])]
    dcv = max(abs(W[k]["cv"][0] - EX[k]["cmix"]) for k in VU)
    check("C2 [witness, seeds %d, %d-%d] the patched engine on that component (N_w = 1600, tau = 20 + 400, "
          "dtau = 0.05, K = 200, K_p = 120, %d bins): E_mix, E_growth and the pure S_yy, S_zz sit within %.2f sigma "
          "of C1 over %d comparisons, Gauss residual %d, S_L <= %.0e; the mixed <cval> matches the exact mixed "
          "value to %.3f, certifying the incremental collinear tracking" % (SEED_VAL[0], SEED_VAL[1], SEED_VAL[4], W[VU[0]]["nbin"], max(abs(s) for s in sg),
                           len(sg), max(W[k]["gauss"] for k in VU), max(W[k]["SL"] for k in VU), dcv),
          max(abs(s) for s in sg) <= 1.6 and max(W[k]["gauss"] for k in VU) == 0 and dcv <= 0.05)

    R0 = t422(120, 0, 0)
    om0 = [o for m, o in R0["om1"] if m in (40, 80, 120)]
    check("C3 [exact] the 4x2x2 at Uc = 0 is P2's T3 to every digit: dim %d, %d violations, %d winding vectors, "
          "zero-winding class %d = ONE component of %d (depth %d) + %d frozen, %d adjacencies, %d missing; "
          "E_0 = %.10f, <n_app> = %.10f, S_L(pi/2) = %.0e, S_yy = %.10f (pi/2), %.10f (pi); omega_eff = %.6f, %.6f, "
          "%.6f at m = 40, 80, 120, from above"
          % (R0["dim"][0], R0["gauss_violations"][0], R0["winding_classes"][0], R0["zero_winding"][0],
             R0["component"][0], R0["bfs_depth"][0], R0["frozen_zero_winding"][0], R0["nnz"][0],
             R0["missing_targets"][0], R0["E0"][0], R0["napp0"][0], R0["S1_0"], R0["S1_1"], R0["S2_1"],
             om0[0], om0[1], om0[2]),
          R0["dim"][0] == 23063296 and R0["gauss_violations"][0] == 0 and R0["winding_classes"][0] == 405
          and R0["zero_winding"][0] == 1552024 and R0["component"][0] == 1551976 and R0["nnz"][0] == 21578752
          and R0["missing_targets"][0] == 0 and near(R0["E0"][0], -16.7037885782, 1e-9)
          and near(R0["napp0"][0], 19.0690013962, 1e-9) and R0["S1_0"] == 0.0
          and near(R0["S1_1"], 0.1044875978, 1e-9) and near(R0["S2_1"], 0.1815941329, 1e-9)
          and allnear(om0, [2.599424, 2.569058, 2.566168], 1e-5) and om0[0] > om0[1] > om0[2])

    R1 = t422(400, 0, 1)
    o1 = R1["om1"][-1][1]
    o0 = om0[-1]
    Ua, Ub = o0 / (2 * R0["S1_1"]), o1 / (2 * R1["S1_1"])
    Va, Vb = 2 * o0 * R0["S1_1"], 2 * o1 * R1["S1_1"]
    fall = 100 * (1 - R1["S1_1"] / R0["S1_1"])
    check("C4 [exact] the same component at Uc = 1: E_0 = %.10f, <cval> = %.6f, S_yy(pi/2) FALLS %.10f -> %.10f "
          "(%.1f per cent), omega(pi/2) RISES %.6f -> %.6f (m = %d, from above), so U(pi/2) = omega/(2 S_yy) rises "
          "%.2f -> %.2f while V(pi/2) holds at %.3f -> %.3f; the component is the same %d states"
          % (R1["E0"][0], R1["cval0"][0], R0["S1_1"], R1["S1_1"], fall, o0, o1, R1["om1"][-1][0], Ua, Ub, Va, Vb,
             R1["component"][0]),
          near(R1["E0"][0], -17.3923265594, 1e-8) and near(R1["S1_1"], 0.0844696486, 1e-9)
          and near(o1, 2.951, 1e-3) and o1 > o0 and near(fall, 19.2, 0.2) and Ub > Ua
          and R1["component"][0] == R0["component"][0])

    L4 = {}
    for Uc in (0.0, 1.0):
        L4[Uc] = run_gfmc(GEOL4, 1000, 15, 60, 0.05, 240, 120, 2, SEED_L4, "L4_%s" % Uc, 0.0, Uc, nbins=10)
    st = {}
    for Uc in L4:
        path = os.path.join(TMP, "L4_%s.bins" % Uc)
        hd = [l for l in open(path) if l.startswith("# NK=")][0]
        NC = int(hd.split("NCOMP=")[1].split()[0])
        kd = [tuple(int(x) for x in tok.split(":")) for tok in hd.split("k_d=")[1].split()]
        ks = [i for i, (d, nn) in enumerate(kd) if nn == 1]      # k = 2 pi/L along each of the three axes
        per = [sum(x[2][i * NC + c] for i in ks for c in range(NC)) / len(ks) for x in bins_of(path)]
        st[Uc] = ms(per)
    dd = st[0.0][0] - st[1.0][0]
    de = math.hypot(st[0.0][1], st[1.0][1])
    check("C5 [witness, seed %d] one short L = 4 pair (N_w = 1000, tau = 15 + 60, dtau = 0.05, K = 240, K_p = 120, "
          "%d bins, cubic-averaged): S_T(pi/2) = %.4f(%.0f) at Uc = 0 and %.4f(%.0f) at Uc = 1, a fall of %.1f per "
          "cent at %.1f sigma, matching C4's exact %.1f; S_L <= %.0e, Gauss residual %d"
          % (SEED_L4, L4[0.0]["nbin"], st[0.0][0], 1e4 * st[0.0][1], st[1.0][0], 1e4 * st[1.0][1],
             100 * dd / st[0.0][0], dd / de, fall, max(L4[u]["SL"] for u in L4), max(L4[u]["gauss"] for u in L4)),
          dd > 0 and dd / de > 2.0 and 12.0 < 100 * dd / st[0.0][0] < 28.0
          and max(L4[u]["gauss"] for u in L4) == 0)


# =====================================================================  D
# The L^3 rows of the source computation are stochastic WITNESSES at declared
# seeds and are NOT rerun here (about twelve minutes of core time); their
# numbers are declared constants and this group checks only the arithmetic read
# off them.  Runs: t3_run.py L 2000 30 200 0.05 240 120 <seed> V Uc <tag> 20,
# i.e. N_w = 2000, tau = 30 + 200, dtau = 0.05, forward-walk lag K_p = 120,
# 20 bins, k = 2 pi n / L along each axis cubic-averaged, both transverse
# polarisations summed; omega is the least-squares slope of -ln C(tau) over the
# declared window.  Seeds 20261401-4 (L = 4), 20261411-6 (L = 6), 20261421-6
# (L = 8).  S_L <= 5e-33 in every run.

RK = {6: (0.3025, 0.0009, 0.305382, 0.005596, 0.7500, 0.0008),
      8: (0.1778, 0.0004, 0.177396, 0.003236, 0.7479, 0.0011)}
pc = [100 * abs(RK[L][0] - RK[L][2]) / RK[L][2] for L in (6, 8)]
sg = [abs(RK[L][0] - RK[L][2]) / math.hypot(RK[L][1], RK[L][3]) for L in (6, 8)]
oq2 = [RK[L][0] / (2 * math.sin(math.pi / L)) ** 2 for L in (6, 8)]
check("D1 [declared, seeds 20261416, 20261426] cross-lane: at V = 1 this engine gives "
      "omega(k_min) = %.4f(%.0f) at L = 6, %.4f(%.0f) at L = 8 against the sister lane's %.6f(%.0f) and %.6f(%.0f) "
      "-- %.2f and %.2f per cent, %.2f and %.2f sigma -- with S_T(k_min) = %.4f, %.4f (the ice 3/4) and "
      "omega/q^2 = %.4f, %.4f, quadratic. The source's '0.5 per cent' at L = 6 is the sigma; the percentage "
      "is %.2f"
      % (RK[6][0], 1e4 * RK[6][1], RK[8][0], 1e4 * RK[8][1], RK[6][2], 1e6 * RK[6][3], RK[8][2], 1e6 * RK[8][3],
         pc[0], pc[1], sg[0], sg[1], RK[6][4], RK[8][4], oq2[0], oq2[1], pc[0]),
      sg[0] < 1.0 and sg[1] < 1.0 and near(pc[0], 0.94, 0.02) and near(pc[1], 0.23, 0.02)
      and abs(oq2[0] - oq2[1]) < 0.005 and near(RK[6][4], 0.75, 2e-3) and near(RK[8][4], 0.75, 3e-3))

S4 = ((0.354, 0.005), (0.325, 0.006), (0.298, 0.006), (0.285, 0.010))   # L = 4, k = pi/2, Uc = 0, .25, .5, 1
S8 = ((0.311, 0.010), (0.285, 0.012), (0.311, 0.012), (0.354, 0.016))   # L = 8, k = pi/4
MAXC8 = (20, 15, 20, 54)
fall4 = 100 * (1 - S4[3][0] / S4[0][0])
res8 = abs(S8[3][0] - S8[0][0]) / math.hypot(S8[3][1], S8[0][1])
u_c = 12.2784 / 2.0                       # U(pi/2) = u |K|^2 at Uc = 0, |K|^2 = 2  (C4's exact rows)
U0_c = 17.4680 - 12.2784
kst = math.sqrt(U0_c / u_c)
check("D2 [declared, seeds 20261401-4/11-4/21-4] the L^3 scan: at L = 4, S_T(pi/2) falls %.3f(%.0f) -> "
      "%.3f(%.0f) from Uc = 0 to 1, %.1f per cent, C4's fraction; at L = 8 nothing is resolved -- S_T(pi/4) = "
      "%.3f, %.3f, %.3f, %.3f moves by %.1f sigma, not monotonically, and the copy count %d, %d, %d, %d flags a "
      "population-control breakdown at Uc = 1; NO k^2 -> c|k| crossover at k >= pi/4 for Uc <= 1. "
      "Crude, on C4's rows: u = %.2f, U_0 = %.2f, k_* = %.2f = pi/%.1f"
      % (S4[0][0], 1e3 * S4[0][1], S4[3][0], 1e3 * S4[3][1], fall4, S8[0][0], S8[1][0], S8[2][0], S8[3][0],
         res8, MAXC8[0], MAXC8[1], MAXC8[2], MAXC8[3], u_c, U0_c, kst, math.pi / kst),
      near(fall4, 19.5, 0.2) and res8 < 2.5 and MAXC8[3] > 2 * max(MAXC8[:3])
      and near(kst, 0.92, 0.01) and near(math.pi / kst, 3.42, 0.02))


# ================================================================== the total
shutil.rmtree(TMP, ignore_errors=True)
print("runtime %.1f s (AUDIT_TIMEOUT_SEC = %d); skipped %d" % (time.time() - T0, AUDIT_TIMEOUT_SEC, SKIPPED))
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
