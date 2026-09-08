#!/usr/bin/env python3
"""Record walls in the staggered mass: what they carry.

Self-contained one-particle runner.  The coarse lattice is 2Z^3, one fermionic
mode per coarse vertex, with the Kawamoto-Smit link signs
    eta_1 = 1,  eta_2(v) = (-1)^{v_1},  eta_3(v) = (-1)^{v_1+v_2},
the hopping matrix H_{wv} = eta_a(v) on each coarse bond (the declared t = -1
convention), and the staggered mass H_m = m sum_v eps_v |v><v| with
eps_v = (-1)^{v_1+v_2+v_3}.  A RECORD WALL is a plane across which the SUPPLIED
sign of m changes: m(x) = +m for x < x_0 and -m for x >= x_0.  The value, the
sign and the profile of m are supplied data.

  A  THE WALL IS A STACKING FAULT.  eps_{v+e_x} = -eps_v, so flipping the sign
     of the mass on a half-space equals a one-site translation of the mass
     pattern there and no plane carries a vanishing mass; the cell algebra and
     the wall-chirality operator W = i Gamma_1 Eps = -(X x Z x Z), which
     anticommutes with the chirality X = -(Y x X x Y); the 1 x 2 x 2 transverse
     Bloch cell reproduces the direct real-space coarse torus and the bulk
     E(q)^2 = 6 + 2 sum_a cos q_a + m^2.
  B  Selected localized finite modes, sharp cutoff census and distinct fitted
     wall-energy / zero-energy kernel scales; velocity is in two-site cell units.
  C  Sharp finite gap fit and small nonzero resolved levels, not exact zeros.
  D  Direct projected-X and sharp taste-mass diagnostics; no wall-swap proof
     or physical parity anomaly is inferred from anticommutation.
  E  A massive DISPERSING line band, with opposite off-node velocities.

Group A carries exact integer and operator identities at residual 0.0; the
items tagged [numerical] are floating-point cross-checks at the stated
tolerance; the closed forms E_w = sqrt(1 + m^2) - 1 and <W> = 1/sqrt(1 + m^2),
the decay lengths and the velocities are FITS, labelled as such everywhere.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import hashlib
from pathlib import Path
import sys
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 120

# Semantic input identity: the model is self-contained; these are the current
# note and exact quoted ontology/comparison boundaries, not parent campaigns.
AUDIT_INPUT_PATHS = ('docs/RECORD_WALLS_IN_THE_STAGGERED_MASS_CARRY_LOCALIZED_2P1D_DIRAC_MATTER_VECTOR_LIKE_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md')
EXPECTED_INPUT_SHA256 = {'docs/RECORD_WALLS_IN_THE_STAGGERED_MASS_CARRY_LOCALIZED_2P1D_DIRAC_MATTER_VECTOR_LIKE_BOUNDED_THEOREM_NOTE_2026-09-03.md': '1b55dfb8e5744ba516a88c5270638deeec585a8a433ac82868cdfc0c3f900009', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md': '67ad0284ca494a4fc82c37dae248a70eb5f84b59d4fad101b0e076122f066d90'}

def current_input_guard():
    root = Path(__file__).resolve().parents[1]
    errors = []
    if set(AUDIT_INPUT_PATHS) != set(EXPECTED_INPUT_SHA256):
        errors.append("declared semantic input set differs from pinned set")
    for rel in AUDIT_INPUT_PATHS:
        try:
            actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        except OSError as exc:
            errors.append(rel + ": " + str(exc))
            continue
        print("INPUT_SHA " + rel + " " + actual)
        if actual != EXPECTED_INPUT_SHA256[rel]:
            errors.append(rel + ": current semantic input changed")
    if errors:
        print("FAIL G0 current source/input guard: " + "; ".join(errors))
        print("TOTAL: PASS=0 FAIL=1")
        raise SystemExit(1)
    print("SOURCE_INPUT_GUARD: exact current inputs; broader parent claims unaccepted")

current_input_guard()


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


# ============================================ the 2x2x2 cell algebra, verbatim

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0, 1], [1, 0]], dtype=complex)
Y2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
Z2 = np.array([[1, 0], [0, -1]], dtype=complex)
PAULI = {"I": I2, "X": X2, "Y": Y2, "Z": Z2}


def kr(*a):
    out = np.array([[1.0 + 0j]])
    for mat in a:
        out = np.kron(out, mat)
    return out


GAM = [kr(Y2, I2, I2), kr(Z2, Y2, I2), kr(Z2, Z2, Y2)]   # Gamma_1, Gamma_2, Gamma_3
EPSC = kr(Z2, Z2, Z2)                                    # Eps = Z1 Z2 Z3, the mass
XCHI = -kr(Y2, X2, Y2)                                   # X = -(Y x X x Y), the chirality
WWALL = 1j * GAM[0] @ EPSC                               # W = i Gamma_1 Eps
MASS2D = GAM[0] @ XCHI                                   # Gamma_1 X = i Gamma_2 Gamma_3


def acom(a, b):
    return float(np.abs(a @ b + b @ a).max())


def com(a, b):
    return float(np.abs(a @ b - b @ a).max())


# ====================================================== lattice / slab builders


def idx(x, a, b):
    return (x * 2 + a) * 2 + b


def build_slab(Lx, kY, kZ, mvec, periodic_x=True):
    """4 L_x x 4 L_x transverse-Bloch block at cell momenta (kY, kZ).

    x is explicit; the Bloch cell is 2 coarse sites in y and 2 in z -- the
    minimal cell on which both the KS sign field and the mass grading are
    cell-periodic.  mvec[x] is the supplied m(x) on the x-th coarse plane.
    """
    n = 4 * Lx
    A = np.zeros((n, n), dtype=complex)
    d = np.zeros(n)
    eY, eZ = np.exp(-1j * kY), np.exp(-1j * kZ)
    for x in range(Lx):
        sy = 1.0 if x % 2 == 0 else -1.0            # eta_2 = (-1)^{v_1}
        for a in (0, 1):
            sz = sy if a == 0 else -sy              # eta_3 = (-1)^{v_1+v_2}
            for b in (0, 1):
                if x + 1 < Lx:
                    A[idx(x + 1, a, b), idx(x, a, b)] += 1.0
                elif periodic_x:
                    A[idx(0, a, b), idx(x, a, b)] += 1.0
                if a == 0:
                    A[idx(x, 1, b), idx(x, 0, b)] += sy
                else:
                    A[idx(x, 0, b), idx(x, 1, b)] += sy * eY
                if b == 0:
                    A[idx(x, a, 1), idx(x, a, 0)] += sz
                else:
                    A[idx(x, a, 0), idx(x, a, 1)] += sz * eZ
                d[idx(x, a, b)] = mvec[x] * (-1.0) ** (x + a + b)
    return A + A.conj().T + np.diag(d.astype(complex))


def slab_diag(Lx, mvec):
    """The supplied mass diagonal of the slab, indexed as build_slab."""
    d = np.zeros(4 * Lx)
    for x in range(Lx):
        for a in (0, 1):
            for b in (0, 1):
                d[idx(x, a, b)] = mvec[x] * (-1.0) ** (x + a + b)
    return d


def build_torus_real(L, m):
    """Direct real-space L^3 coarse torus at uniform mass m."""
    n = L ** 3

    def s(x, y, z):
        return (x % L) * L * L + (y % L) * L + (z % L)

    A = np.zeros((n, n))
    d = np.zeros(n)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                v = s(x, y, z)
                A[s(x + 1, y, z), v] += 1.0
                A[s(x, y + 1, z), v] += (-1.0) ** x
                A[s(x, y, z + 1), v] += (-1.0) ** (x + y)
                d[v] = m * (-1.0) ** (x + y + z)
    return A + A.T + np.diag(d)


def build_line(L, kZ, mgrid):
    """x and y explicit on an L x L torus, 2-site Bloch cell in z; dim 2 L^2."""
    n = 2 * L * L

    def s(x, y, b):
        return ((x % L) * L + (y % L)) * 2 + b

    A = np.zeros((n, n), dtype=complex)
    d = np.zeros(n)
    eZ = np.exp(-1j * kZ)
    for x in range(L):
        for y in range(L):
            sy, sz = (-1.0) ** x, (-1.0) ** (x + y)
            for b in (0, 1):
                A[s(x + 1, y, b), s(x, y, b)] += 1.0
                A[s(x, y + 1, b), s(x, y, b)] += sy
                if b == 0:
                    A[s(x, y, 1), s(x, y, 0)] += sz
                else:
                    A[s(x, y, 0), s(x, y, 1)] += sz * eZ
                d[s(x, y, b)] = mgrid[x, y] * (-1.0) ** (x + y + b)
    return A + A.conj().T + np.diag(d.astype(complex))


# ------------------------------------------------- supplied mass sign profiles


def sharp(Lx, m):
    """Two walls on the x-torus: +m for x < Lx/2, -m for x >= Lx/2."""
    v = np.full(Lx, -float(m))
    v[: Lx // 2] = float(m)
    return v


def resolved(Lx, m, w):
    """The same two walls with m(x) ramped through zero over w coarse sites."""
    x = np.arange(Lx)
    return m * (np.tanh((Lx / 2.0 - 0.5 - x) / w) * np.tanh((x + 0.5) / w)
                * np.tanh((Lx - 0.5 - x) / w))


def sharp_open(Lx, m):
    """One wall at x = Lx/2 with open x ends."""
    v = np.full(Lx, -float(m))
    v[: Lx // 2] = float(m)
    return v


def lowest(Lx, mvec, nlow=8, kY=np.pi, kZ=np.pi, periodic_x=True):
    H = build_slab(Lx, kY, kZ, mvec, periodic_x)
    w, V = np.linalg.eigh(H)
    o = np.argsort(np.abs(w))[:nlow]
    o = o[np.argsort(w[o])]
    return H, w[o], V[:, o]


def wall_indicator(V, Lx, lo, hi):
    """Matrix of the indicator on lo <= x < hi in the span of the columns."""
    mask = np.zeros(Lx)
    mask[lo:hi] = 1.0
    A = V.reshape(Lx, 4, V.shape[1])
    return np.einsum("xan,x,xam->nm", A.conj(), mask, A)


def cell_matrix(V, Lx, Op8):
    """Matrix of a 2x2x2-cell-local operator in the span of the columns."""
    W = V.reshape(Lx, 2, 2, V.shape[1]).reshape(Lx // 2, 8, V.shape[1])
    return np.einsum("cin,ij,cjm->nm", W.conj(), Op8, W)


def herm_eigs(A):
    return np.linalg.eigvalsh((A + A.conj().T) / 2)


def split_walls(Lx, mvec, periodic_x=True):
    """The selected lowest 8 absolute-energy states, split by wall indicator.

    This is not the complete resolved-profile in-gap census.
    """
    H, e, V = lowest(Lx, mvec, 8, periodic_x=periodic_x)
    ind = np.linalg.eigh(wall_indicator(V, Lx, Lx // 4, 3 * Lx // 4))
    ev, U = ind
    return H, e, V @ U[:, ev < 0.5], V @ U[:, ev >= 0.5], ev


# ======================== A -- the sharp record wall is a stacking fault [exact]

LX = 32
M0 = 1.0
r_eps = max(abs((-1.0) ** (x + 1 + a + b) + (-1.0) ** (x + a + b))
            for x in range(4) for a in (0, 1) for b in (0, 1))
d_wall = slab_diag(LX, sharp(LX, M0))
d_shift = np.zeros(4 * LX)
for x in range(LX):
    sgn = (x + 1) if x >= LX // 2 else x           # a one-site translation of the pattern
    for a in (0, 1):
        for b in (0, 1):
            d_shift[idx(x, a, b)] = M0 * (-1.0) ** (sgn + a + b)
r_fault = float(np.abs(d_wall - d_shift).max())
check("A1 [exact] eps_{v+e_x} = -eps_v (%.1e), so a half-space sign flip IS a one-site "
      "translation of the mass pattern (%.1e): the wall is a STACKING FAULT, and min|m(x)| = %.3f "
      "-- no plane's mass vanishes"
      % (r_eps, r_fault, np.abs(d_wall).min()),
      r_eps == 0.0 and r_fault == 0.0 and np.abs(d_wall).min() == M0)

rg = max(acom(GAM[a], GAM[b]) for a in range(3) for b in range(3) if a != b)
re = max(acom(GAM[a], EPSC) for a in range(3))
rx = float(np.abs(XCHI - 1j * GAM[0] @ GAM[1] @ GAM[2]).max())
rxg = max(com(XCHI, GAM[a]) for a in range(3))
check("A2 [exact] cell algebra (a != b): {G_a, G_b} = %.1e, {G_a, Eps} = %.1e, X = i G1G2G3 = -(YxXxY) "
      "(%.1e), [X, G_a] = %.1e, {X, Eps} = %.1e"
      % (rg, re, rx, rxg, acom(XCHI, EPSC)),
      rg == 0.0 and re == 0.0 and rx == 0.0 and rxg == 0.0 and acom(XCHI, EPSC) == 0.0)

rw = float(np.abs(WWALL + kr(X2, Z2, Z2)).max())
rh = float(np.abs(WWALL - WWALL.conj().T).max())
r2 = float(np.abs(WWALL @ WWALL - np.eye(8)).max())
check("A3 [exact] W = i G1 Eps = -(XxZxZ) (%.1e), hermitian (%.1e), W^2 = I (%.1e); "
      "{W,G1} = {W,Eps} = %.1e, [W,G2] = [W,G3] = %.1e, {W, X} = %.1e: W ANTICOMMUTES WITH X"
      % (rw, rh, r2, max(acom(WWALL, GAM[0]), acom(WWALL, EPSC)),
         max(com(WWALL, GAM[1]), com(WWALL, GAM[2])), acom(WWALL, XCHI)),
      rw == 0.0 and rh == 0.0 and r2 == 0.0 and acom(WWALL, GAM[0]) == 0.0
      and acom(WWALL, EPSC) == 0.0 and com(WWALL, GAM[1]) == 0.0
      and com(WWALL, GAM[2]) == 0.0 and acom(WWALL, XCHI) == 0.0)

d_cell = 0.0
for L in (4, 6):
    for m in (0.0, 0.5, 1.0):
        er = np.sort(np.linalg.eigvalsh(build_torus_real(L, m)))
        nc = L // 2
        eb = np.sort(np.concatenate([
            np.linalg.eigvalsh(build_slab(L, 2 * np.pi * nY / nc, 2 * np.pi * nZ / nc,
                                          np.full(L, m)))
            for nY in range(nc) for nZ in range(nc)]))
        d_cell = max(d_cell, float(np.abs(er - eb).max()))
check("A4 [1e-13] the 1x2x2 transverse Bloch cell reproduces the DIRECT real-space coarse torus, "
      "L = 4, 6, m = 0, 0.5, 1 (%.1e)" % d_cell, d_cell < 1e-13)

d_disp = 0.0
for L in (4, 6, 8):
    for m in (0.0, 0.5, 2.0):
        er = np.sort(np.linalg.eigvalsh(build_torus_real(L, m)))
        pr = []
        for n in itertools.product(range(L // 2), repeat=3):
            q = 4 * np.pi * np.array(n) / L
            E = np.sqrt(max(6 + 2 * np.cos(q).sum() + m * m, 0.0))
            pr += [-E] * 4 + [E] * 4
        d_disp = max(d_disp, float(np.abs(er - np.sort(np.array(pr))).max()))
M8 = build_torus_real(8, 0.0)
e8 = np.array([(-1.0) ** ((v // 64) + (v // 8) % 8 + v % 8) for v in range(512)])
r_me = float(np.abs(M8 * e8[None, :] + e8[:, None] * M8).max())
d_gap = max(abs(2 * np.abs(np.linalg.eigvalsh(build_torus_real(8, m))).min() - 2 * m)
            for m in (0.2, 0.5, 1.0))
check("A5 [exact/1e-13] {M, Eps} = %.1e; bulk E(q)^2 = 6 + 2 sum_a cos q_a + m^2, each +-E "
      "fourfold, L = 4, 6, 8, m = 0, 0.5, 2 (%.1e); the 8^3 Dirac point gaps to 2m (%.1e)"
      % (r_me, d_disp, d_gap),
      r_me == 0.0 and d_disp < 1e-13 and d_gap < 1e-12)

FB = []
for word in itertools.product("IXYZ", repeat=3):
    O = kr(*[PAULI[c] for c in word])
    if all(com(O, g) == 0.0 for g in GAM + [EPSC]) and abs(np.trace(O)) < 1e-12:
        FB.append(("".join(word), O))
check("A6 [exact] the commutant of {G_1, G_2, G_3, Eps} is 4-dimensional -- I and traceless taste "
      "generators F_b = %s -- each commuting with W at %.1e: exact cell commutant only"
      % (", ".join(f[0] for f in FB), max(com(F, WWALL) for _, F in FB)),
      len(FB) == 3 and max(com(F, WWALL) for _, F in FB) == 0.0)

# ============================================ B -- localized matter on the wall

best, node = None, None
for i in range(8):
    for j in range(8):
        kY, kZ = 2 * np.pi * i / 8, 2 * np.pi * j / 8
        g = float(np.abs(np.linalg.eigvalsh(build_slab(LX, kY, kZ, sharp(LX, M0)))).min())
        if i == j == 4:
            node = g
        elif best is None or g < best:
            best = g
check("B1 [numerical] 8x8 transverse-BZ scan, L_x = 32, m = 1: the wall slab's min|E| is lowest "
      "at (pi, pi), the projection of the (pi,pi,pi) Dirac point (%.6f against %.6f)"
      % (node, best), node < best)

ok_b2 = True
worst_ind = 0.0
for Lx in (32, 64):
    for m in (0.5, 1.0, 2.0):
        H, e, VB, VA, ev = split_walls(Lx, sharp(Lx, m))
        nin = int((np.abs(np.linalg.eigvalsh(H)) < 0.9 * m).sum())
        ok_b2 = ok_b2 and nin == 8 and VA.shape[1] == 4 and VB.shape[1] == 4 \
            and ev[3] < 0.05 and ev[4] > 0.95
        worst_ind = max(worst_ind, float(ev[3]))
check("B2 [cutoff/count] SHARP fixtures: 8 states at |E| < 0.9 m at (pi,pi), splitting "
      "4 + 4 by the wall indicator (worst %.4f / %.4f), L_x = 32, 64, m = 0.5, 1, 2"
      % (worst_ind, 1 - worst_ind), ok_b2)

ok_b3 = True
b3row = ""
for Lx in (32, 64):
    for m in (0.5, 1.0, 2.0):
        H = build_slab(Lx, np.pi, np.pi, sharp_open(Lx, m), periodic_x=False)
        w, V = np.linalg.eigh(H)
        o = np.argsort(np.abs(w))[:10]
        o = o[np.argsort(w[o])]
        lab = []
        for i in o:
            p = (np.abs(V[:, i].reshape(Lx, 4)) ** 2).sum(1)
            lab.append("W" if p[Lx // 2 - 4:Lx // 2 + 4].sum() > 0.5 else "E")
        Ew = np.array([w[i] for i, l in zip(o, lab) if l == "W"])
        Ee = np.array([abs(w[i]) for i, l in zip(o, lab) if l == "E"])
        ok_b3 = ok_b3 and len(Ew) == 4 and abs(Ew[0] + Ew[3]) < 1e-9 \
            and abs(Ew[0] - Ew[1]) < 1e-9 and abs(Ew[1]) < 0.9 * m \
            and Ee.min() > 0.9 * m and abs(Ee.min() / m - 1) < 0.1
        if m == 1.0 and Lx == 64:
            b3row = "E_w = %+.6f (x2), ends at %.6f" % (Ew[3], Ee.min())
check("B3 [numerical classification] among the ten lowest open-sharp states, four meet the wall-density test, 2 at +E_w and 2 at "
      "-E_w, ends separate at |E| ~ m; L_x = 32, 64, m = 0.5, 1, 2 (L=64, m=1: %s)"
      % b3row, ok_b3)

print("   decay length [fits]:  m | sharp | w=4 | xi = 2/arccosh(1+m^2/2)")
ok_b4 = True
dens = {}
TAIL_FITS = {}
for m in (0.5, 1.0, 2.0):
    row = []
    for tag, mv in (("sharp", sharp(64, m)), ("res", resolved(64, m, 4))):
        _, _, _, VA, _ = split_walls(64, mv)
        n = (np.abs(VA.reshape(64, 4, 4)) ** 2).sum(axis=(1, 2)) / 4.0
        dens[(tag, m)] = n
        d = np.abs(np.arange(64) - 31.5)
        sel = (d >= 4.5) & (d <= 14.5) & (n > 1e-14)
        row.append(-2.0 / np.polyfit(d[sel], np.log(n[sel]), 1)[0])
    TAIL_FITS[m] = tuple(row)
    xi = 2.0 / np.arccosh(1 + m * m / 2)
    print("     m=%.1f  %.4f  %.4f  %.4f  (%+.2f per cent)"
          % (m, row[0], row[1], xi, 100 * (row[1] / xi - 1)))
    ok_b4 = ok_b4 and abs(row[1] / xi - 1) < 0.031 and abs(row[0] / xi - 1) < 0.25
check("B4 [finite fits] the DISTINCT zero-energy bulk comparison and resolved fitted length "
      "agree within 3.1 per cent in the stated finite window at m = 0.5, 1, 2", ok_b4)

fr = {k: float(v[27:37].sum()) for k, v in dens.items()}
fl = {k: (float(v[30] / v[29]), float(v[31] / v[30])) for k, v in dens.items()}
check("B5 [numerical] within 4.5 coarse sites lie %.1f / %.1f per cent of the density (sharp / "
      "resolved) at m = 1, %.1f / %.1f at m = 2, %.1f / %.1f at m = 0.5; and at m = 1 the sharp "
      "profile is PAIR-FLAT about the seam, n(30)/n(29) = %.4f with a step n(31)/n(30) = %.3f per "
      "pair, against %.3f and %.3f resolved"
      % (100 * fr[("sharp", 1.0)], 100 * fr[("res", 1.0)], 100 * fr[("sharp", 2.0)],
         100 * fr[("res", 2.0)], 100 * fr[("sharp", 0.5)], 100 * fr[("res", 0.5)],
         fl[("sharp", 1.0)][0], fl[("sharp", 1.0)][1], fl[("res", 1.0)][0], fl[("res", 1.0)][1]),
      fr[("sharp", 1.0)] > 0.97 and fr[("res", 1.0)] > 0.96 and fr[("sharp", 2.0)] > 0.99
      and abs(fl[("sharp", 1.0)][0] - 1) < 1e-6 and fl[("sharp", 1.0)][1] > 5.0
      and fl[("res", 1.0)][1] < 1.5)

vs = []
ok_b6 = True
for tag, mk in (("sharp", lambda m: sharp(64, m)), ("res", lambda m: resolved(64, m, 4))):
    for m in (0.5, 1.0, 2.0):
        mv = mk(m)
        E0 = float(np.abs(np.linalg.eigvalsh(build_slab(64, np.pi, np.pi, mv))).min())
        for dv in ((1, 0), (0, 1), (1, 1)):
            ps = np.array([0.02, 0.04, 0.06, 0.08])
            Es = np.array([np.abs(np.linalg.eigvalsh(
                build_slab(64, np.pi + p * dv[0], np.pi + p * dv[1], mv))).min() for p in ps])
            pn = ps * np.sqrt(dv[0] ** 2 + dv[1] ** 2)
            v = np.sqrt(max(np.polyfit(pn ** 2, Es ** 2 - E0 ** 2, 1)[0], 0.0))
            vs.append(v)
            ok_b6 = ok_b6 and abs(v - 1.0) < 3e-3
check("B6 [fits] a massive small-cell-momentum band at (pi,pi): fitted cell velocity %.4f to %.4f "
      "along q_y, q_z and the diagonal, m = 0.5, 1, 2, both profiles -- isotropic, m-independent, "
      "cell coefficient 1; multiply by 2 for coarse or 4 for fine site units per supplied time"
      % (min(vs), max(vs)), ok_b6)

# ================================================ C -- the wall band is gapped

print("   m | E_w(L=32) | E_w(L=64) | sqrt(1+m^2)-1 | w=4 | w=8 | bulk")
ok_c1 = ok_c2 = True
for m in (0.25, 0.5, 1.0, 2.0):
    e32 = float(np.abs(np.linalg.eigvalsh(build_slab(32, np.pi, np.pi, sharp(32, m)))).min())
    e64 = float(np.abs(np.linalg.eigvalsh(build_slab(64, np.pi, np.pi, sharp(64, m)))).min())
    r4 = float(np.abs(np.linalg.eigvalsh(build_slab(64, np.pi, np.pi, resolved(64, m, 4)))).min())
    r8 = float(np.abs(np.linalg.eigvalsh(build_slab(64, np.pi, np.pi, resolved(64, m, 8)))).min())
    cf = np.sqrt(1 + m * m) - 1
    print("     %.2f  %.6f %.6f %.6f  %.1e %.1e  %.2f" % (m, e32, e64, cf, r4, r8, m))
    ok_c1 = ok_c1 and abs(e32 - cf) < 1e-6 and abs(e64 - cf) < 1e-6 and cf < m
    ok_c2 = ok_c2 and r4 < 2e-3 * cf and r8 < 1.1e-6
check("C1 [fit, 1e-6] E_w = sqrt(1 + m^2) - 1 to six decimals at m = 0.25, 0.5, 1, 2, IDENTICAL "
      "at L_x = 32 and 64: the sharp band is gapped by 2(sqrt(1+m^2) - 1), inside the bulk gap 2m "
      "but not zero; two-size agreement alone is not an all-size proof", ok_c1)
check("C2 [numerical] an interpolant crossing BETWEEN sites gives small finite levels: at w = 4 the gap "
      "falls three to five orders (under 1e-6 for m <= 0.5), at w = 8 to 1.0e-6 or less at every "
      "m; none of these small numbers proves an exact zero", ok_c2)

# =========================================== D -- no chirality on the record wall

print("   L=64:  m | <W> sharp A / B | <W> w=4 A / B | 1/sqrt(1+m^2)")
mx = 0.0
ok_d2 = True
for m in (0.5, 1.0, 2.0):
    got = {}
    for tag, mv in (("sharp", sharp(64, m)), ("res", resolved(64, m, 4))):
        _, _, VB, VA, _ = split_walls(64, mv)
        wA = herm_eigs(cell_matrix(VA, 64, WWALL))
        wB = herm_eigs(cell_matrix(VB, 64, WWALL))
        mx = max(mx, float(np.abs(herm_eigs(cell_matrix(VA, 64, XCHI))).max()),
                 float(np.abs(herm_eigs(cell_matrix(VB, 64, XCHI))).max()))
        ok_d2 = ok_d2 and np.ptp(wA) < 1e-9 and np.ptp(wB) < 1e-9 \
            and abs(wA[0] + wB[0]) < 1e-7 and wA[0] > 0.4
        got[tag] = (float(wA[0]), float(wB[0]))
    ok_d2 = ok_d2 and abs(got["sharp"][0] - 1 / np.sqrt(1 + m * m)) < 1e-6
    print("     %.1f  %+.6f / %+.6f  %+.6f / %+.6f  %.6f"
          % (m, got["sharp"][0], got["sharp"][1], got["res"][0], got["res"][1],
             1 / np.sqrt(1 + m * m)))
check("D1 [1e-12] directly measured X compression on each selected four-dimensional wall space, m = 0.5, 1, "
      "2, both profiles, worst %.1e; NOT inferred from {W,X}=0"
      % mx, mx < 1e-12)
check("D2 [fit, 1e-7] <W> = +-1 IN SIGN, opposite on the two walls, constant across each wall's "
      "four selected modes; this noninteger expectation is NOT an index; magnitude 1/sqrt(1 + m^2) sharp (a fit, to 1e-6)", ok_d2)

print("   H|wall = (G_1 X)(x)(n.F):  m | singlet | |n| | E_w | residual")
ok_d3 = ok_d4 = True
DENSITY_SCALAR_ERROR = 0.0
SHARP_SPACES = {}
for m in (0.5, 1.0, 2.0):
    Hs, _, VB, VA, _ = split_walls(64, sharp(64, m))
    SHARP_SPACES[m] = (Hs, VB, VA)
    coeff, resid = [], []
    for Vw in (VA, VB):
        for x in range(64):
            block = Vw[4*x:4*x+4]
            px = block.conj().T @ block
            DENSITY_SCALAR_ERROR = max(DENSITY_SCALAR_ERROR,
                float(np.abs(px - np.trace(px) * np.eye(4) / 4).max()))
        Hw = Vw.conj().T @ Hs @ Vw
        ops = [MASS2D] + [MASS2D @ F for _, F in FB]
        cs = np.array([float(np.real(np.trace(Hw @ cell_matrix(Vw, 64, O)))) / 4 for O in ops])
        rec = sum(c * cell_matrix(Vw, 64, O) for c, O in zip(cs, ops))
        coeff.append(cs)
        resid.append(float(np.abs(Hw - rec).max()))
        ok_d4 = ok_d4 and all(abs(herm_eigs(cell_matrix(Vw, 64, F)).sum()) < 1e-9 for _, F in FB)
    nA, nB = coeff[0][1:], coeff[1][1:]
    sing = max(abs(coeff[0][0]), abs(coeff[1][0]))
    ok_d3 = ok_d3 and sing < 1e-12 and float(np.abs(nA + nB).max()) < 1e-12 \
        and abs(np.linalg.norm(nA) - (np.sqrt(1 + m * m) - 1)) < 1e-6 and max(resid) < 1e-12
    print("     %.1f  %.1e  %.6f  %.6f  %.1e"
          % (m, sing, np.linalg.norm(nA), np.sqrt(1 + m * m) - 1, max(resid)))
check("D3 [1e-12] the SHARP finite mass reconstruction H|wall = (G_1 X) (x) (n . F), with "
      "TASTE-SINGLET coefficient below tolerance on the sharp m=.5,1,2 fixtures, |n| fits E_w, n reversed "
      "between selected walls; no physical anomaly is computed", ok_d3)
check("D4 [1e-9] each F_b is traceless on each selected SHARP wall subspace "
      "-- equal coarse-x-plane density after summing four transverse-cell coordinates is separately checked", ok_d4)

# ================================= E -- two orthogonal walls: a line, not a wire

MG = {}
for L in (24, 32):
    g = np.zeros((L, L))
    for x in range(L):
        for y in range(L):
            g[x, y] = (1.0 if x < L // 2 else -1.0) * (1.0 if y < L // 2 else -1.0)
    MG[L] = g

e24 = np.sort(np.abs(np.linalg.eigvalsh(build_line(24, np.pi, MG[24]))))[:10]
w32, V32 = np.linalg.eigh(build_line(32, np.pi, MG[32]))
e32 = np.sort(np.abs(w32))[:10]
check("E1 [1e-6] L = 24 and 32, m = 1, k_z = pi: the line binds an eightfold band at |E| = %.6f, "
      "IDENTICAL at both sizes (%.1e), under the single-wall gap %.6f; numerical two-size evidence"
      % (e32[0], abs(e24[0] - e32[0]), np.sqrt(2.0) - 1),
      abs(e24[0] - e32[0]) < 1e-6 and float(np.ptp(e32[:8])) < 1e-6 and e32[0] < np.sqrt(2.0) - 1
      and abs(e32[0] - 0.317837) < 5e-7
      and all(np.array_equal(MG[L], np.outer(np.where(np.arange(L) < L//2, 1., -1.),
                      np.where(np.arange(L) < L//2, 1., -1.))) for L in (24, 32)))

print("   k_z dispersion:  dk | |E|(pi-dk) | |E|(pi+dk)")
ok_e2 = True
LINE_DISPERSION = []
for dk in (0.08, 0.16):
    a = float(np.abs(np.linalg.eigvalsh(build_line(24, np.pi - dk, MG[24]))).min())
    b = float(np.abs(np.linalg.eigvalsh(build_line(24, np.pi + dk, MG[24]))).min())
    print("     %.2f  %.6f  %.6f" % (dk, a, b))
    LINE_DISPERSION.append((dk, a, b))
    ok_e2 = ok_e2 and abs(a - b) < 1e-9 and a > e24[0]
    ok_e2 = ok_e2 and abs(a*a - e24[0]**2 - 4*np.sin(dk/2)**2) < 1e-10
    ok_e2 = ok_e2 and abs(a - ({0.08: 0.327745, 0.16: 0.355761}[dk])) < 5e-7
check("E2 [1e-9] the band is EVEN and DISPERSING about its minimum %.6f: derivative zero only there; "
      "opposite nonzero off-node velocities occur; no complete "
      "chiral-wire classification follows" % e24[0], ok_e2)

gr = np.zeros((24, 24))
for x in range(24):
    for y in range(24):
        gr[x, y] = (np.tanh((11.5 - x) / 3.0) * np.tanh((x + 0.5) / 3.0) * np.tanh((23.5 - x) / 3.0)
                    * np.tanh((11.5 - y) / 3.0) * np.tanh((y + 0.5) / 3.0) * np.tanh((23.5 - y) / 3.0))
z0 = float(np.abs(np.linalg.eigvalsh(build_line(24, np.pi, gr))).min())
z1 = float(np.abs(np.linalg.eigvalsh(build_line(24, np.pi + 0.1, gr))).min())
check("E3 [numerical] two minima of the RESOLVED w=3 crossing, not a complete "
      "plane/line mode census -- |E| = %.1e at the node, %.6f at k_z - pi = 0.1" % (z0, z1),
      z0 < 1e-4 and abs(z1 - 0.1) < 2e-3)

o32 = np.argsort(np.abs(w32))[:8]
p = (np.abs(V32[:, o32].reshape(32, 32, 2, 8)) ** 2).sum(axis=(2, 3)) / 8.0


def dline(c):
    d = np.abs(np.arange(32) - c)
    return np.minimum(d, 32 - d)


dx = np.minimum(np.minimum(dline(-0.5), dline(31.5)), dline(15.5))
msk = np.outer(dx < 1.5, dx < 1.5)
enh = float(p[msk].sum()) / (msk.sum() / 32.0 ** 2)
check("E4 [numerical] the line does bind: the band density is enhanced %.1f-fold within 1.5 "
      "coarse sites of the four intersection lines (L = 32), %.1f per cent on %d of 1024 cells" % (enh, 100 * p[msk].sum(), msk.sum()), enh > 10.0)


# Independent corrections: finite matrices, actual subspaces and input fixtures.
prof = np.array([.2, -.7, .9, .4, -.3, 1.1, -.8, .6])
h0 = build_slab(8, np.pi, np.pi, prof)
square_err = 0.0
for qy, qz in ((.13, .0), (.0, -.21), (.13, -.21)):
    h = build_slab(8, np.pi+qy, np.pi+qz, prof)
    shift = 4*np.sin(qy/2)**2 + 4*np.sin(qz/2)**2
    square_err = max(square_err, float(np.abs(h@h-h0@h0-shift*np.eye(32)).max()))
check("Q1 [1e-12] actual transverse square identity; q spans TWO coarse sites (FOUR fine), no physical time calibration", square_err < 1e-12)

TAIL_REFS = {m: (2/np.arcsinh(m), 2/np.arccosh(1+m*m/2)) for m in TAIL_FITS}
check("Q2 [finite tail fits] energy-dependent sharp recurrence 2/asinh(m), distinct from zero-energy kernel; actual fitted tails agree within 1e-4 relative",
      all(abs(TAIL_FITS[m][0]/a-1) < 1e-4 and abs(a/b-1) > .02
          for m,(a,b) in TAIL_REFS.items()))

RESOLVED_CENSUS = {}
for m in (1.,2.):
    mv = resolved(64,m,4)
    ev = np.linalg.eigvalsh(build_slab(64,np.pi,np.pi,mv))
    RESOLVED_CENSUS[m] = (int((np.abs(ev)<m).sum()), float(np.abs(ev).min()), float(np.abs(mv).min()))
check("Q3 [complete finite spectra] resolved |E|<m counts 24 and 72; selected eight are incomplete and sampled mass/low energy are nonzero",
      [RESOLVED_CENSUS[m][0] for m in (1.,2.)] == [24,72]
      and all(v[1]>1e-6 and v[2]>.1 for v in RESOLVED_CENSUS.values()))

_, states = np.linalg.eigh((WWALL+XCHI)/np.sqrt(2))
u = states[:,-1]
means = [float(np.real(u.conj()@op@u)) for op in (WWALL,XCHI)]
_, VB, VA = SHARP_SPACES[1.]
XB = np.kron(np.eye(32),XCHI); WB = np.kron(np.eye(32),WWALL)
pa = VA@VA.conj().T; pb=VB@VB.conj().T
LEAKAGE = (float(np.linalg.norm((np.eye(256)-pa)@WB@VA,2)),
           float(np.linalg.norm(VB.conj().T@XB@VA,2)),
           float(np.linalg.norm((np.eye(256)-pa-pb)@XB@VA,2)))
check("Q4 [actual counterexample] anticommuting W/X have simultaneous means 1/sqrt2; actual X exits selected light spaces instead of swapping walls",
      max(abs(v-1/np.sqrt(2)) for v in means)<1e-12
      and LEAKAGE[0]>.7 and LEAKAGE[1]<3e-5 and LEAKAGE[2]>.999)
check("Q5 [1e-12] each summed coarse-x-plane projector compression is scalar on each selected SHARP wall space; identical x marginals after summing four transverse-cell coordinates, not vertex densities", DENSITY_SCALAR_ERROR < 1e-12)

lg = np.arange(36,dtype=float).reshape(6,6)/37-.4
l0=build_line(6,np.pi,lg); lq=build_line(6,np.pi+.19,lg)
LINE_SQUARE_ERROR=float(np.abs(lq@lq-l0@l0-4*np.sin(.19/2)**2*np.eye(72)).max())
LINE_VELOCITIES=[float(np.sin(dk)/np.sqrt(e24[0]**2+4*np.sin(dk/2)**2)) for dk in (-.08,.08)]
check("Q6 [1e-12/1e-7] actual arbitrary-profile line square identity; original band has opposite NONZERO off-node velocities about +/-0.24383155",
      LINE_SQUARE_ERROR<1e-12 and abs(LINE_VELOCITIES[0]+.24383155)<1e-7
      and abs(LINE_VELOCITIES[1]-.24383155)<1e-7)

print("SUMMARY: supplied finite sharp/selected resolved wall bands, distinct tail scales and cell units; directly checked projections and paired sharp taste coefficients; a massive dispersing line. No physical readout, formation, exact-zero or anomaly theorem.")
print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
