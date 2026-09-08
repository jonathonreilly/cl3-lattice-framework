#!/usr/bin/env python3
"""Emergent Lorentz invariance at the Dirac point, and the taste census.

Self-contained finite-cluster runner.  The object is the coarse-lattice
staggered sector already on the table: the coarse lattice 2Z^3, one
fermionic mode per coarse vertex, and the Kawamoto-Smit (KS) link sign
field

    eta_1 = 1,  eta_2(v) = (-1)^{v_1},  eta_3(v) = (-1)^{v_1+v_2}

read on it as a supplied model. The historical pi-flux cell algebra is
redeclared here and recomputed: Gamma = (Y1, Z1 Y2, Z1 Z2 Y3),
Xi = (X1, Z1 X2, Z1 Z2 X3), T = diag(1,1,-1,-1), B = (XX, XY, XZ), and
the Clifford-averaging intertwiner U with U Gamma_a U^dag = -sigma_a (x) T,
U Xi_a U^dag = I (x) B_a.  No scientific helper is imported; the note and quoted context have identity guards.

  A  THE MAGNETIC CELL AND THE NODES.  The minimal magnetic cell of the KS
     sign field is 2x2x1 (four coarse sites), where H4(Q)^2 =
     (6 + 2 cos Q1 + 2 cos Q2 + 2 cos 2Q3) I and tr H4 = 0.  Direction 3
     carries one site per cell, so its hop is diagonal and enters squared:
     Q = (pi,pi,pi) is NOT a node.  E4 = 0 at exactly two points of the
     magnetic BZ; the 2x2x2 cell folds both onto q = (pi,pi,pi), 8-fold.
  B  THE CHIRALITY CENSUS.  With m_a = M_a/v_a, M_a = dH/dp_a at the node,
     X = -i m1 m2 m3 grades the zero modes.  Each 2x2x1 node carries
     1R + 1L; the folded node carries 2R + 2L.  Net chirality 0, N_f = 2
     four-component Dirac fields, vector-like.  M_a = -Gamma_a exactly and
     X = I (x) T exactly in the intertwiner basis.
  C  ONE VELOCITY.  E(pi+p)^2 = sum_a (2 - 2 cos p_a) exactly; the
     expansion is |p|^2 - (1/12) sum p_a^4 + (1/360) sum p_a^6 + O(p^8), so
     v_phase = 1 - (|p|^2/24) sum nhat_a^4 + O(p^4) in cell coordinates
     and supplied unit hopping/time; leading anisotropy at relative order p^2.
  D  THE EQUAL-TIME PROPAGATOR.  P(q) = (1/2)(I - H(q)/E(q)) has the exact
     one-odd-component selection rule away from the contact P_vv=1/2.
     Finite Fourier samples compare with (4/pi^2)|nhat_a|; no lattice
     infinite-distance remainder bound or historical-parent equivalence.
  E  SUM RULE AND PAULI REPULSION.  sum_{u!=v} P_vu^2 = P_vv - P_vv^2 = 1/4
     on the half-filled tori, and distinct-site pair covariance under an explicitly supplied Slater/Born law.
     A one-body projector alone does not derive physical permanent Records.

Groups A-C are exact where tagged [exact]: sympy symbolic identities,
integer and Z[i] matrix arithmetic at zero tolerance, exhaustive scan.  The
items tagged [numerical] are floating-point evaluations at the stated
tolerance.

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
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md')
INPUT_SHA256 = {'docs/EMERGENT_LORENTZ_INVARIANCE_AT_THE_DIRAC_POINT_AND_THE_TASTE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'f50b26e2774153a26efe1335317bb273c5cea7afb62d99a76cce2e9113ca4f6b', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md': '67ad0284ca494a4fc82c37dae248a70eb5f84b59d4fad101b0e076122f066d90'}

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


def verify_inputs():
    """Bind final prose and exact quoted context; no parent science is executed."""
    root = Path(__file__).resolve().parents[1]
    for relative, expected in INPUT_SHA256.items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError("missing or changed declared input: " + relative)
    return True


check("Z1 [input identity] final own-note/current memo/quoted gate pinned; no parent campaign approval", verify_inputs())


# ============================================================ KS sign field


def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a); axes 0,1,2 = 1,2,3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


# ======================================================== the cell algebra

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
TT = np.diag([1, 1, -1, -1]).astype(complex)
BB = [kr(SX, SX), kr(SX, SY), kr(SX, SZ)]
SIG = [SX, SY, SZ]


def cell_sites(cell):
    return list(itertools.product(*(range(c) for c in cell)))


def bloch_cell(Q, cell, deriv=None):
    """Bloch block of the KS hopping on a magnetic cell of the given extents."""
    sites = cell_sites(cell)
    idx = {v: i for i, v in enumerate(sites)}
    H = np.zeros((len(sites), len(sites)), dtype=complex)
    for v in sites:
        for a in range(3):
            w = list(v)
            w[a] += 1
            d = [0, 0, 0]
            if w[a] >= cell[a]:
                w[a] -= cell[a]
                d[a] = 1
            w = tuple(w)
            ph = np.exp(-1j * sum(Q[b] * d[b] for b in range(3)))
            f = (-1j * d[deriv]) if deriv is not None else 1.0
            c = eta_ks(v, a) * ph * f
            H[idx[w], idx[v]] += c
            H[idx[v], idx[w]] += np.conj(c)
    return H


def bloch_cell_sym(Q, cell):
    """Symbolic version of `bloch_cell`, exact in the cell momenta."""
    sites = cell_sites(cell)
    idx = {v: i for i, v in enumerate(sites)}
    H = sp.zeros(len(sites), len(sites))
    for v in sites:
        for a in range(3):
            w = list(v)
            w[a] += 1
            d = [0, 0, 0]
            if w[a] >= cell[a]:
                w[a] -= cell[a]
                d[a] = 1
            w = tuple(w)
            ph = sp.exp(-sp.I * sum(Q[b] * d[b] for b in range(3)))
            H[idx[w], idx[v]] += eta_ks(v, a) * ph
            H[idx[v], idx[w]] += eta_ks(v, a) * sp.conjugate(ph)
    return H


def bloch8(q):
    """The 2x2x2-cell Bloch block in closed Cl(6) form."""
    return sum((1 + np.cos(q[a])) * XI[a] + np.sin(q[a]) * GAM[a] for a in range(3))


print("--- A  magnetic cell ---")

# ---- A1 the 2x2x1 magnetic cell, symbolically -----------------------------
Qs = sp.symbols("Q1 Q2 Q3", real=True)
H4s = bloch_cell_sym(Qs, (2, 2, 1))
f4 = 6 + 2 * sp.cos(Qs[0]) + 2 * sp.cos(Qs[1]) + 2 * sp.cos(2 * Qs[2])
sq4_ok = sp.simplify(sp.expand_trig(sp.expand(H4s * H4s)) - f4 * sp.eye(4)) == sp.zeros(4, 4)
tr4_ok = sp.simplify(H4s.trace()) == 0
check(
    "A1 [exact, sympy] the 2x2x1 magnetic cell (4 coarse sites) has H4(Q)^2 = "
    "(6 + 2cosQ1 + 2cosQ2 + 2cos2Q3) I and tr H4 = 0: two doubly degenerate bands +-E4",
    sq4_ok and tr4_ok,
)

# ---- A2 direction 3 enters squared: (pi,pi,pi) is not a node --------------
ev_ppp = np.linalg.eigvalsh(bloch_cell((np.pi,) * 3, (2, 2, 1)))
diag3 = sp.simplify(sp.expand_trig(4 * sp.cos(Qs[2]) ** 2 - (2 + 2 * sp.cos(2 * Qs[2])))) == 0
check(
    "A2 [exact] direction 3 has one site per cell, so its hop is diagonal and enters "
    "squared: 4cos^2 Q3 = 2 + 2cos 2Q3.  Q = (pi,pi,pi) is NOT a node: spectrum %s"
    % np.array2string(np.round(ev_ppp.real, 12), separator=","),
    diag3 and abs(abs(ev_ppp).min() - 2.0) < 1e-12,
)

# ---- A3 exhaustive scan: exactly two nodes --------------------------------
NS = 60
g = 2 * np.pi * np.arange(NS) / NS
F = (
    6
    + 2 * np.cos(g)[:, None, None]
    + 2 * np.cos(g)[None, :, None]
    + 2 * np.cos(2 * g)[None, None, :]
)
hits = [(g[i], g[j], g[k]) for i, j, k in zip(*np.where(F < 1e-9))]
nodes4 = [(np.pi, np.pi, np.pi / 2), (np.pi, np.pi, 3 * np.pi / 2)]
scan_ok = len(hits) == 2 and all(
    any(max(abs(np.array(h) - np.array(nd))) < 1e-9 for nd in nodes4) for h in hits
)
deg4 = [
    int(np.sum(np.abs(np.linalg.eigvalsh(bloch_cell(nd, (2, 2, 1)))) < 1e-12))
    for nd in nodes4
]
check(
    "A3 [exact + exhaustive %d^3 scan] E4 = 0 iff cosQ1 = cosQ2 = cos2Q3 = -1: exactly "
    "TWO nodes, Q = (pi,pi,pi/2) and (pi,pi,3pi/2), each 4-fold (degeneracies %s)"
    % (NS, deg4),
    scan_ok and deg4 == [4, 4],
)

# ---- A4 the 2x2x2 cell folds both nodes onto one point --------------------
rng = np.random.default_rng(20260903)
maxdev = 0.0
for _ in range(60):
    Q = rng.uniform(0, 2 * np.pi, 3)
    q = (Q[0], Q[1], 2 * Q[2])
    s8 = np.sort(np.linalg.eigvalsh(bloch_cell(q, (2, 2, 2))))
    sA = np.linalg.eigvalsh(bloch_cell(Q, (2, 2, 1)))
    sB = np.linalg.eigvalsh(bloch_cell((Q[0], Q[1], Q[2] + np.pi), (2, 2, 1)))
    maxdev = max(maxdev, float(np.abs(s8 - np.sort(np.concatenate([sA, sB]))).max()))
    maxdev = max(maxdev, float(np.abs(bloch_cell(q, (2, 2, 2)) - bloch8(q)).max()))
z8 = int(np.sum(np.abs(np.linalg.eigvalsh(bloch8((np.pi,) * 3))) < 1e-12))
check(
    "A4 [numerical, 1e-11] the 2x2x2 cell folds both onto q = (pi,pi,pi): its spectrum at "
    "(Q1,Q2,2Q3) is the union of the 2x2x1 spectra at Q3, Q3+pi (dev %.1e), one %d-fold "
    "touching" % (maxdev, z8),
    maxdev < 1e-11 and z8 == 8,
)

print()
print("--- B  chirality census ---")


def census(Mlist):
    """(speeds, spectrum of X = -i m1 m2 m3) for velocity matrices M_a."""
    v = [float(np.sqrt(np.real((M @ M)[0, 0]))) for M in Mlist]
    m = [Mlist[a] / v[a] for a in range(3)]
    return v, np.linalg.eigvalsh(-1j * m[0] @ m[1] @ m[2])


# ---- B1 M_a = -Gamma_a exactly, and the 8-fold node is 2R + 2L ------------
qs = sp.symbols("q1 q2 q3", real=True)
H8s = bloch_cell_sym(qs, (2, 2, 2))
GS = [sp.Matrix(8, 8, lambda i, j: sp.nsimplify(GAM[a][i, j])) for a in range(3)]
exact_M = all(
    sp.simplify(sp.diff(H8s, qs[a]).subs({qs[b]: sp.pi for b in range(3)}) + GS[a])
    == sp.zeros(8, 8)
    for a in range(3)
)
M8 = [-GAM[a] for a in range(3)]
v8, x8 = census(M8)
nR8 = int(np.sum(x8 > 0.5))
nL8 = int(np.sum(x8 < -0.5))
check(
    "B1 [exact, sympy] at q = (pi,pi,pi), M_a = dH/dp_a = -Gamma_a exactly, speeds all 1, "
    "X = -i m1 m2 m3 spectrum +1 x%d, -1 x%d: %dR + %dL Weyl (2 components each) = N_f = %d "
    "four-component Dirac fields, net chirality %d (Nielsen-Ninomiya)"
    % (nR8, nL8, nR8 // 2, nL8 // 2, (nR8 + nL8) // 4, (nR8 - nL8) // 2),
    exact_M and nR8 == 4 and nL8 == 4 and max(abs(x - 1) for x in v8) < 1e-12,
)

# ---- B2 each 2x2x1 node is 1R + 1L, speeds (1,1,2) -----------------------
rows4 = []
for nd in nodes4:
    M4 = [bloch_cell(nd, (2, 2, 1), deriv=a) for a in range(3)]
    v4, x4 = census(M4)
    rows4.append((nd, v4, int(np.sum(x4 > 0.5)), int(np.sum(x4 < -0.5))))
check(
    "B2 [numerical, 1e-12] each 2x2x1 node is a 4-component Dirac point, 1R + 1L, speeds "
    "(1,1,2) in that cell's coordinates; the two are 2R + 2L, the same vector-like N_f = 2",
    all(r[2] == 2 and r[3] == 2 for r in rows4)
    and all(abs(r[1][0] - 1) < 1e-12 and abs(r[1][2] - 2) < 1e-12 for r in rows4),
)
print("  %-24s %-24s %4s %4s" % ("node (cell)", "speeds", "chi+", "chi-"))
for nd, v4, nr, nl in rows4:
    print("  %-24s (%.4f,%.4f,%.4f) %4d %4d"
          % ("(pi,pi,%s) 2x2x1" % ("pi/2" if nd[2] < 3 else "3pi/2"),
             v4[0], v4[1], v4[2], nr, nl))
print("  %-24s (%.4f,%.4f,%.4f) %4d %4d"
      % ("(pi,pi,pi) 2x2x2", v8[0], v8[1], v8[2], nR8, nL8))

# ---- B3 X = I (x) T exactly, and the relabelling -------------------------
def targets(sg):
    return [sg * np.kron(SIG[a], TT) for a in range(3)] + [np.kron(I2, BB[a]) for a in range(3)]


def averaging_intertwiner(N):
    pg, pn = {}, {}
    for m in range(64):
        gg = np.eye(8, dtype=complex)
        nn = np.eye(8, dtype=complex)
        for k in range(6):
            if (m >> k) & 1:
                gg = gg @ SIX[k]
                nn = nn @ N[k]
        pg[m] = gg.conj().T
        pn[m] = nn
    for r in range(8):
        for c in range(8):
            M = np.zeros((8, 8), dtype=complex)
            M[r, c] = 1
            U = sum(pn[m] @ M @ pg[m] for m in range(64))
            if abs(np.linalg.det(U)) > 1e-6:
                return U
    return None


UEX = {}
for sg in (1, -1):
    U = averaging_intertwiner(targets(sg))
    UEX[sg] = U / np.sqrt((U @ U.conj().T)[0, 0].real)
Um = UEX[-1]
tG = [np.kron(SIG[a], TT) for a in range(3)]
tB = [np.kron(I2, BB[a]) for a in range(3)]
Xu = -1j * tG[0] @ tG[1] @ tG[2]
X_is_T = np.array_equal(np.round(Xu.real).astype(int), np.kron(I2, TT).real.astype(int)) and (
    np.abs(Xu - np.kron(I2, TT)).max() < 1e-12
)
# transported velocity matrices on each branch, and det of the 2x2 Weyl block
detrows = {}
for sg in (1, -1):
    UM = [UEX[sg] @ M8[a] @ UEX[sg].conj().T for a in range(3)]
    per = []
    for tsign, sel in ((+1, [0, 1]), (-1, [2, 3])):
        pick = np.ix_([s * 4 + sel[0] for s in range(2)], [s * 4 + sel[0] for s in range(2)])
        Ms = [UM[a][pick] for a in range(3)]
        vmat = np.array(
            [[np.real(np.trace(Ms[a] @ SIG[b])) / 2 for b in range(3)] for a in range(3)]
        )
        per.append((tsign, float(np.linalg.det(vmat))))
    detrows[sg] = per
branch_indep = detrows[1][0][1] * detrows[1][1][1] < 0 and detrows[-1][0][1] * detrows[-1][1][1] < 0
inter_ok = all(
    np.abs(UEX[sg] @ SIX[k] @ UEX[sg].conj().T - targets(sg)[k]).max() == 0.0
    for sg in (1, -1)
    for k in range(6)
)
trans_ok = all(
    np.abs(UEX[-1] @ M8[a] @ UEX[-1].conj().T - tG[a]).max() == 0.0 for a in range(3)
)
lin = 0.0
for _ in range(60):
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    p = 1e-4 * n
    lin = max(
        lin,
        float(
            np.abs(
                Um @ bloch8(np.pi + p) @ Um.conj().T - sum(p[a] * tG[a] for a in range(3))
            ).max()
        )
        / 1e-8,
    )
check(
    "B3 [exact] in the branch U Gamma_a U^dag = -sigma_a x T the transported M_a are exactly "
    "sigma_a x T, so H(pi+p) = sum_a p_a (sigma_a x T) + O(p^2) (res/|p|^2 -> %.2f) and "
    "X = I x T EXACTLY: T = +1 is two RIGHT-handed Weyl (det v = %+.0f), T = -1 two LEFT-handed "
    "(det v = %+.0f), a branch swap only exchanging the labels"
    % (lin, detrows[-1][0][1], detrows[-1][1][1]),
    inter_ok
    and trans_ok
    and X_is_T
    and branch_indep
    and detrows[-1][0][1] > 0
    and detrows[-1][1][1] < 0
    and lin < 10,
)
print("  RELABELLING: the historical, unaccepted 'two-component spin x four-component taste' counts 8 = 2 x 4;"
      "\n  the census reads the same 8 as 2 (Weyl) x 2 (chiralities) x 2 (tastes), same multiplicities.")

# ---- B4 torus zero-mode counts ------------------------------------------
def ks_matrix(L, twist=None):
    sites = list(itertools.product(range(L), repeat=3))
    idx = {v: i for i, v in enumerate(sites)}
    M = np.zeros((len(sites), len(sites)))
    for v in sites:
        for a in range(3):
            w = list(v)
            wrapped = (w[a] + 1 == L)
            w[a] = (w[a] + 1) % L
            w = tuple(w)
            e = eta_ks(v, a) * (-1 if (wrapped and a == twist) else 1)
            M[idx[w], idx[v]] += e
            M[idx[v], idx[w]] += e
    return M, sites, idx


tor = []
for L in (4, 6, 8):
    M, _, _ = ks_matrix(L)
    nz = int(np.sum(np.abs(np.linalg.eigvalsh(M)) < 1e-9))
    tor.append((L, nz, 8 if L % 4 == 0 else 0))
check(
    "B4 [numerical, 1e-9] tori L = 4, 6, 8 carry %d, %d, %d zero modes: the cell momenta "
    "q_a = 4 pi m / L hit pi iff 4 | L, and then all 8 modes of the touching are on the grid"
    % tuple(t[1] for t in tor),
    all(t[1] == t[2] for t in tor) and [t[1] for t in tor] == [8, 0, 8],
)

print()
print("--- C  one velocity ---")

ps = sp.symbols("p1 p2 p3", real=True)
E2 = sum(2 - 2 * sp.cos(ps[a]) for a in range(3))
E2res = sp.simplify(6 + 2 * sum(sp.cos(sp.pi + ps[a]) for a in range(3)) - E2)
lam = sp.symbols("lam", positive=True)
ns = sp.symbols("n1 n2 n3", real=True)
ser = sp.expand(sp.series(E2.subs({ps[a]: lam * ns[a] for a in range(3)}), lam, 0, 8).removeO())
quart = sum(n ** 4 for n in ns)
c2_ok = sp.simplify(ser.coeff(lam, 2) - sum(n ** 2 for n in ns)) == 0
c4_ok = sp.simplify(ser.coeff(lam, 4) + quart / 12) == 0
c6_ok = sp.simplify(ser.coeff(lam, 6) - sum(n ** 6 for n in ns) / 360) == 0
check(
    "C1 [exact, sympy] E(pi+p)^2 = sum_a (2 - 2 cos p_a) exactly (residual %s), expanding as "
    "|p|^2 - (1/12) sum_a p_a^4 + (1/360) sum_a p_a^6 + O(p^8): the O(p^2) term is exactly "
    "isotropic; the anisotropic quartic class modulo |p|^4 has coefficient "
    "EXACTLY -1/12" % sp.simplify(E2res),
    E2res == 0 and c2_ok and c4_ok and c6_ok,
)

sub = {ns[2]: sp.sqrt(1 - ns[0] ** 2 - ns[1] ** 2)}
vsym = sp.simplify(
    sp.series(sp.sqrt(sp.expand(ser.subs(sub))) / lam, lam, 0, 3).removeO()
)
vdiff = sp.simplify(sp.expand(vsym - (1 - lam ** 2 * quart.subs(sub) / 24)))
check(
    "C2 [exact, sympy] hence phase velocity v = E/|p| = 1 - (|p|^2/24) sum_a nhat_a^4 + O(p^4): ONE velocity "
    "v -> 1 in every direction, every taste, both chiralities, supplied cell/hopping/time units (unit-sphere "
    "residual to O(p^2): %s)" % vdiff,
    vdiff == 0,
)


def vel(nhat, pm):
    p = pm * np.asarray(nhat, dtype=float)
    return float(np.sqrt(sum(2 - 2 * np.cos(p[a]) for a in range(3))) / pm)


dirs = (
    np.array([1.0, 0, 0]),
    np.array([1.0, 1, 0]) / np.sqrt(2),
    np.array([1.0, 1, 1]) / np.sqrt(3),
)
print("  %-7s %-11s %-11s %-11s %-11s %s"
      % ("|p|", "v[100]", "v[110]", "v[111]", "spread", "36 spread/|p|^2"))
tab = []
for pm in (0.8, 0.4, 0.1, 0.05, 0.0125):
    vs = [vel(d, pm) for d in dirs]
    spread = max(vs) - min(vs)
    tab.append((pm, spread))
    print(
        "  %-7.4f %-11.8f %-11.8f %-11.8f %-11.4e %.5f"
        % (pm, vs[0], vs[1], vs[2], spread, spread * 36 / pm ** 2)
    )
expo = float(np.polyfit(np.log([t[0] for t in tab]), np.log([t[1] for t in tab]), 1)[0])
rel = max(abs(t[1] - t[0] ** 2 / 36) / (t[0] ** 2 / 36) for t in tab)
check(
    "C3 [numerical] the [100]/[111] spread is |p|^2/36 + O(p^4) (max rel dev %.2e), log-log "
    "anisotropy exponent %.4f [exact 2]: isotropy fails only at relative order p^2"
    % (rel, expo),
    abs(expo - 2.0) < 5e-3 and rel < 3e-2,
)

form_dev = 0.0
mix = []
for pm in (0.4, 0.1, 0.05):
    mx = mm = 0.0
    for _ in range(40):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        p = pm * n
        lhs = Um @ bloch8(np.pi + p) @ Um.conj().T
        rhs = sum(np.sin(p[a]) * tG[a] + (1 - np.cos(p[a])) * tB[a] for a in range(3))
        mx = max(mx, float(np.abs(lhs - rhs).max()))
        mm = max(mm, float(np.abs(sum((1 - np.cos(p[a])) * tB[a] for a in range(3))).max()))
    form_dev = max(form_dev, mx)
    mix.append((pm, mm / pm ** 2))
SPIN = [np.kron(SIG[b], np.eye(4)) for b in range(3)]
singlet = all(
    np.abs(tB[a] @ SPIN[b] - SPIN[b] @ tB[a]).max() == 0.0
    for a in range(3)
    for b in range(3)
)
check(
    "C4 [numerical, 4e-16] U H(pi+p) U^dag = sum_a sin p_a (sigma_a x T) + sum_a "
    "(1 - cos p_a)(I x B_a) to %.1e; the taste-mixing term is O(p^2) (norm/|p|^2 -> %.2f) and "
    "commutes with every spin generator -- a singlet, so it leaves the leading velocity; mixing is not band splitting"
    % (form_dev, mix[-1][1]),
    form_dev < 1e-13 and singlet and abs(mix[-1][1] - 0.5) < 0.02,
)

print()
print("--- D  propagator ---")

# ---- D1 the exact selection identity -------------------------------------
sel_ok = True
for s in range(8):
    for t in range(8):
        pc = bin(s ^ t).count("1")
        if pc == 1:
            continue
        for a in range(3):
            if XI[a][s, t] != 0 or GAM[a][s, t] != 0:
                sel_ok = False
check(
    "D1 [exact] every entry of Xi_a, Gamma_a with popcount(s XOR s') != 1 vanishes, so "
    "P(q)_{ss'} = delta/2 - H(q)_{ss'}/(2E) is zero off the one-odd-component set except the contact "
    "and P_ss = 1/2: the selection rule is an identity of the projector, not asymptotics",
    sel_ok,
)


def kernel_blocks(NC):
    """|P_{s,0}(dR)| on an NC^3 half-shifted cell-momentum grid, per momentum."""
    qa = 2 * np.pi * (np.arange(NC) + 0.5) / NC
    q1 = qa[:, None, None]
    q2 = qa[None, :, None]
    q3 = qa[None, None, :]
    E = np.sqrt(6 + 2 * (np.cos(q1) + np.cos(q2) + np.cos(q3)))
    cq = (np.cos(q1), np.cos(q2), np.cos(q3))
    sq = (np.sin(q1), np.sin(q2), np.sin(q3))
    out = {}
    for s, a in ((4, 0), (2, 1), (1, 2)):
        coef = (1 + cq[a]) * XI[a][s, 0] + sq[a] * GAM[a][s, 0]
        out[s] = np.abs(np.fft.ifftn(-coef / (2 * E)))
        del coef
    del E, cq, sq
    return out


def shells(blk):
    """Per-shell (measured mean, predicted mean, count) and the axis ratios."""
    means = []
    for lo, hi, step in ((6, 24, 1), (30, 50, 2), (60, 90, 3)):
        vals, pred = [], []
        for s in (4, 2, 1):
            a = {4: 0, 2: 1, 1: 2}[s]
            for dR in itertools.product(range(0, hi // 2 + 1, step), repeat=3):
                r = np.array([2 * dR[b] + ((s >> (2 - b)) & 1) for b in range(3)], dtype=float)
                rn = float(np.linalg.norm(r))
                if rn < lo or rn > hi:
                    continue
                vals.append(blk[s][dR] * rn ** 3)
                pred.append((4 / np.pi ** 2) * abs(r[a]) / rn)
        means.append((lo, hi, float(np.mean(vals)), float(np.mean(pred)), len(vals)))
    ratios = [
        (n, float(blk[4][((n - 1) // 2, 0, 0)] / ((4 / np.pi ** 2) / n ** 3)))
        for n in (41, 61, 81)
    ]
    return means, ratios


C0 = 4 / np.pi ** 2
NC = 288
blk = kernel_blocks(NC)
means, ratios = shells(blk)
del blk
print("  |P_vu| |r|^3, %d^3 grid, stride-subsampled shells" % NC)
print("  %-10s %-10s %-22s %s" % ("shell |r|", "measured", "mean (4/pi^2)|nhat_a|", "pairs"))
for lo, hi, m, pr, n in means:
    print("  %-10s %-10.5f %-22.5f %d" % ("%d-%d" % (lo, hi), m, pr, n))
far = means[2][2]
check(
    "D2 [numerical, %d^3 momentum grid] finite |P_vu| |r|^3 compared with (4/pi^2)|nhat_a| = %.6f |nhat_a|: "
    "axis ratios %.4f, %.4f, %.4f at n = 41, 61, 81, approaching 1 with |r|"
    % (NC, C0, ratios[0][1], ratios[1][1], ratios[2][1]),
    all(abs(r - 1) < 0.01 for _, r in ratios),
)
check(
    "D3 [numerical] each shell mean tracks the mean of (4/pi^2)|nhat_a| over the same "
    "separations, finite means compared with sphere average 2/pi^2 = %.6f (measured %.5f -> %.5f -> "
    "%.5f); no infinite-distance proof or endorsement of historical 0.21" % (2 / np.pi ** 2, means[0][2], means[1][2], far),
    abs(far - 2 / np.pi ** 2) < 5e-3
    and means[0][2] > means[1][2] > far
    and all(abs(m - pr) < 3e-3 for _, _, m, pr, _ in means),
)

print()
print("--- E  sum rule ---")


def valid_occupation_projector(P):
    """Algebra needed before using a supplied Slater/Born occupation law."""
    d = np.real(np.diag(P))
    off = ~np.eye(len(P), dtype=bool)
    joint = np.outer(d, d) - np.abs(P) ** 2
    return bool(np.max(np.abs(P-P.conj().T)) < 1e-12
                and np.max(np.abs(P@P-P)) < 1e-12
                and np.min(d) >= -1e-12 and np.max(d) <= 1+1e-12
                and np.min(joint[off]) >= -1e-12
                and np.max(joint[off]-np.outer(d,d)[off]) <= 1e-12)


def projector(L, twist=None):
    M, sites, _ = ks_matrix(L, twist)
    ev, W = np.linalg.eigh(M)
    nz = int(np.sum(np.abs(ev) < 1e-9))
    neg = W[:, ev < -1e-9]
    return neg @ neg.T, nz


print("  %-21s %4s %4s %-10s %-14s %s"
      % ("torus", "V", "zero", "P_vv", "sum rule", "max excess"))
res = {}
pair_projectors_ok = True
for tag, L, tw in (
    ("8^3 antiperiodic x_3", 8, 2),
    ("6^3 periodic", 6, None),
    ("8^3 periodic", 8, None),
):
    P, nz = projector(L, tw)
    V = L ** 3
    diag = np.diag(P)
    lhs = (P ** 2).sum(axis=1) - diag ** 2
    sr = float(np.abs(lhs - (diag - diag ** 2)).max())
    pair_projectors_ok = pair_projectors_ok and valid_occupation_projector(P)
    outer = np.outer(diag, diag)
    worst = float(((outer - P ** 2) - outer).max())
    res[tag] = (V, nz, diag, lhs, sr, worst, int(round(float(np.trace(P)))))
    print("  %-21s %4d %4d %-10.7f %-14.10f %.1e" % (tag, V, nz, diag[0], lhs[0], worst))

V, nz, diag, lhs, sr, worst, rk = res["8^3 antiperiodic x_3"]
check(
    "E1 [numerical, 1e-15] on the 8^3 torus with one antiperiodic direction (zero modes "
    "lifted, an exact half-filled projector) P_vv = 1/2 at every site (dev %.1e) and "
    "sum_{u != v} P_vu^2 = P_vv - P_vv^2 = 1/4 exactly (dev %.1e): Var N = 0 under supplied Slater/Born law. "
    "  6^3 periodic gives the same 1/4"
    % (float(np.abs(diag - 0.5).max()), sr),
    float(np.abs(diag - 0.5).max()) < 1e-13
    and sr < 1e-13
    and abs(lhs[0] - 0.25) < 1e-13
    and res["6^3 periodic"][4] < 1e-13
    and abs(res["6^3 periodic"][3][0] - 0.25) < 1e-13,
)
check(
    "E2 [numerical] Hermitian idempotent projectors and distinct-site Slater/Born pair "
    "probabilities; original %d ordered-entry determinant diagnostic max excess %.1e "
    "(diagonal occupation uses n_v^2=n_v); no general Record negative-association claim" % (V * V, worst),
    worst <= 1e-14 and pair_projectors_ok,
)
Vp, nzp, diagp, lhsp, srp, worstp, rkp = res["8^3 periodic"]
check(
    "E3 [numerical, reported as ambiguous] on the 8^3 PERIODIC torus the zero modes make half "
    "filling ambiguous: proj(E < 0) has rank %d, P_vv = %d/%d, and the sum rule closes at "
    "%.7f, not 1/4 (identity dev %.1e).  Reported, not used" % (rkp, rkp, Vp, lhsp[0], srp),
    srp < 1e-11 and rkp == 252 and abs(diagp[0] - 252 / 512) < 1e-12,
)

print()
# Post-review bounded controls. These add conditions without changing the original grids.
# Four-site two-orbital Slater state: all six occupation outcomes by actual minors.
V4 = np.array([[1,1],[1,-1],[1,1],[1,-1]], float)/2
P4 = V4@V4.T
outcomes = list(itertools.combinations(range(4),2))
weights = np.array([abs(np.linalg.det(V4[list(o),:]))**2 for o in outcomes])
occ = np.array([[int(i in o) for i in range(4)] for o in outcomes])
means4 = weights@occ
joint4 = (occ.T*weights)@occ
cov4 = joint4-np.outer(means4,means4)
off4 = ~np.eye(4,dtype=bool)
# Different joint law with the same single-site means, not the same pure one-body matrix.
alt_occ = np.array([[1,1,0,0],[0,0,1,1]])
alt_mean = alt_occ.mean(axis=0)
alt_cov = alt_occ.T@alt_occ/2-np.outer(alt_mean,alt_mean)
check("E4 [bounded joint-law control] supplied Slater minors normalize and give distinct-site "
      "Cov=-|P_uv|^2, diagonal Var=n(1-n); same-marginal alternative has Cov(0,1)=+1/4; "
      "nonprojector rejected",
      valid_occupation_projector(P4) and abs(weights.sum()-1)<1e-13
      and np.max(abs(means4-np.diag(P4)))<1e-13
      and np.max(abs((cov4+abs(P4)**2)[off4]))<1e-13
      and np.max(abs(np.diag(joint4)-means4))<1e-13
      and np.max(abs(alt_mean-means4))<1e-13 and abs(alt_cov[0,1]-.25)<1e-13
      and not valid_occupation_projector(.4*np.eye(4)))
# Explicit occupation of four of eight zero modes: original strict-negative rule stays unchanged.
Mz, vz, _ = ks_matrix(4)
Z = np.zeros((64,8))
for i,v in enumerate(vz):
    corner = 4*(v[0]%2)+2*(v[1]%2)+(v[2]%2)
    Z[i,corner] = (-1)**sum(x//2 for x in v)/np.sqrt(8)
had = np.array([[1,1],[1,-1]])/np.sqrt(2)
walsh = np.kron(np.kron(had,had),had)
fill = Z@walsh[:,:4]
Pneg, _ = projector(4)
Pfill = Pneg+fill@fill.T
check("E5 [bounded zero-mode control] periodic 4^3 permits a supplied rank32 half-filled "
      "projector with uniform diagonal1/2; strict-negative convention remains separate",
      np.max(abs(Mz@Z))<1e-13 and np.max(abs(Z.T@Z-np.eye(8)))<1e-13
      and valid_occupation_projector(Pfill) and abs(np.trace(Pfill)-32)<1e-12
      and np.max(abs(np.diag(Pfill)-.5))<1e-13 and abs(np.trace(Pneg)-28)<1e-12)
# Unit-hop Hermitian normalization relative to the quoted coefficient-1/2 antihermitian D.
Da = np.zeros_like(Mz); iz = {v:i for i,v in enumerate(vz)}
for i,v in enumerate(vz):
    for a in range(3):
        w=list(v); w[a]=(w[a]+1)%4; j=iz[tuple(w)]
        Da[j,i] += .5*eta_ks(v,a); Da[i,j] -= .5*eta_ks(v,a)
Gphase=np.diag([1j**sum(v) for v in vz])
x=sp.symbols('x',positive=True)
phase_series=sp.series(2*sp.sin(x/2)/x,x,0,4).removeO()
group_series=sp.series(sp.diff(2*sp.sin(x/2),x),x,0,4).removeO()
check("C5 [normalization control] axis phase/group corrections -p^2/24 and -p^2/8; "
      "G(-iD)G^dag=M/2, cell p=2k; speed1 per cell or2 per coarse site in supplied units",
      sp.expand(phase_series-(1-x*x/24))==0 and sp.expand(group_series-(1-x*x/8))==0
      and np.max(abs(Gphase@(-1j*Da)@Gphase.conj().T-Mz/2))<1e-13)

print("TOTAL: PASS=%d FAIL=%d   runtime %.1f s" % (PASS, FAIL, time.time() - T0))
sys.exit(0 if FAIL == 0 else 1)
