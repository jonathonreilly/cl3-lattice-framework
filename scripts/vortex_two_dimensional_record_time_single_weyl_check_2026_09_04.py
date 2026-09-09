#!/usr/bin/env python3
"""Finite supplied two-coordinate Wilson-Dirac vortex diagnostics.

All matrices, auxiliary graph coordinates, profiles, finite sizes and embeddings
are supplied mathematical data. No physical Record history or species bridge is
inferred. Complete block SVDs give the declared spectral cutoffs. Real mass
forces signed full-cutoff density cancellation, not absence of chiral subspaces.
Vortex chiral subspaces mix opposite nonzero energies; local masked/heat traces
are not nonzero global indices. The square balanced block has global index zero.
Original numerical checks are retained with corrected scope; focused controls
measure nonstationarity, unsigned boundary support and heat-scale dependence.
No audit verdict is granted. Historical originals are archived byte-exactly.
"""

from __future__ import annotations

import math
import sys
from pathlib import Path
import hashlib

import numpy as np

AUDIT_TIMEOUT_SEC = 150

AUDIT_INPUT_PATHS = ('docs/A_VORTEX_IN_A_TWO_DIMENSIONAL_RECORD_TIME_CARRIES_A_SINGLE_WEYL_MODE_IN_THE_INTERIOR_AND_A_REAL_MASS_CARRIES_NONE_BOUNDED_THEOREM_NOTE_2026-09-04.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md')
EXPECTED_INPUT_SHA256 = {'docs/A_VORTEX_IN_A_TWO_DIMENSIONAL_RECORD_TIME_CARRIES_A_SINGLE_WEYL_MODE_IN_THE_INTERIOR_AND_A_REAL_MASS_CARRIES_NONE_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'f62288c5d48e499b988aa541967e3dac2f23ae504a2d7be2683e8ce7117dd52e', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/THE_RECORD_TIME_DOMAIN_WALL_ON_AN_OPEN_INTERVAL_WHERE_THE_PARTNER_WEYL_MODE_LIVES_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'ac911d59c9bfaa54a1553f102df533a2dc1cdaae42df316adc3c250471eb7c52'}
ROOT = Path(__file__).resolve().parents[1]

def verify_inputs(root=ROOT):
    """Reject missing or changed note/context before computing; no scientific verdict."""
    actual = {path: hashlib.sha256((root / path).read_bytes()).hexdigest()
              for path in AUDIT_INPUT_PATHS}
    if actual != EXPECTED_INPUT_SHA256:
        raise ValueError("source input drift; re-review the affected conclusions")
    return actual


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


def nrm(a):
    return float(np.linalg.norm(a))


# ================================================== the eight-component embedding

I2 = np.eye(2, dtype=complex)
S1 = np.array([[0, 1], [1, 0]], dtype=complex)
S2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
S3 = np.array([[1, 0], [0, -1]], dtype=complex)
SIG = [S1, S2, S3]
I4 = np.eye(4, dtype=complex)

A1 = np.kron(S1, S1)
A2 = np.kron(S1, S2)
A3 = np.kron(S1, S3)
A4 = np.kron(S2, I2)
ALPHA = [A1, A2, A3, A4]
B4 = A1 @ A2 @ A3 @ A4                                   # = -t3 (x) I
G = [np.kron(s, B4) for s in SIG] + [np.kron(I2, a) for a in ALPHA]
CHI8 = np.kron(I2, B4)

M_DEF = 0.8
R_S = 1.0
R_SPACE = 1.0
CUT = 0.30


# ========================================= the supplied two-dimensional record time

def chain_ops(n, end_mode="hard"):
    """Hermitian momentum K and Wilson Laplacian L on one open record-time chain."""
    k = np.zeros((n, n), dtype=complex)
    lap = np.zeros((n, n), dtype=complex)
    for s in range(n - 1):
        k[s, s + 1] += -0.5j
        k[s + 1, s] += 0.5j
        lap[s, s] += 0.5
        lap[s + 1, s + 1] += 0.5
        lap[s, s + 1] += -0.5
        lap[s + 1, s] += -0.5
    if end_mode == "hard":
        lap[0, 0] += 0.5
        lap[n - 1, n - 1] += 0.5
    return k, lap


def square_ops(n, end_mode="hard"):
    """K_1, K_2 and L_1 + L_2 on the open n x n record-time square."""
    k1, l1 = chain_ops(n, end_mode)
    k2, l2 = chain_ops(n, end_mode)
    e = np.eye(n, dtype=complex)
    return np.kron(k1, e), np.kron(e, k2), np.kron(l1, e) + np.kron(e, l2)


def mass_blocks(n, m1, m2, end_mode, shift):
    k1, k2, lap = square_ops(n, end_mode)
    d1 = np.diag(np.asarray(m1, dtype=float).ravel() + shift) + R_S * lap
    d2 = np.diag(np.asarray(m2, dtype=float).ravel())
    return k1, k2, d1, d2


def D4(n, m1, m2, end_mode="hard", shift=0.0):
    """The 4-component transverse Wilson-Dirac operator on the square (p = 0)."""
    k1, k2, d1, d2 = mass_blocks(n, m1, m2, end_mode, shift)
    return np.kron(k1, A1) + np.kron(k2, A2) + np.kron(d1, A3) + np.kron(d2, A4)


def block_A(n, m1, m2, end_mode="hard", shift=0.0):
    """The SQUARE off-diagonal block of D_4 in the CHI eigenbasis."""
    k1, k2, d1, d2 = mass_blocks(n, m1, m2, end_mode, shift)
    return (np.kron(k1, S1) + np.kron(k2, S2) + np.kron(d1, S3)
            - 1j * np.kron(d2, I2))


def H8(n, m1, m2, p=(0.0, 0.0, 0.0), end_mode="hard"):
    """The full 8-component Hamiltonian at transverse Bloch momentum p."""
    w = R_SPACE * sum(1.0 - math.cos(x) for x in p)
    k1, k2, d1, d2 = mass_blocks(n, m1, m2, end_mode, w)
    h = np.kron(k1, G[3])
    h += np.kron(k2, G[4])
    h += np.kron(d1, G[5])
    h += np.kron(d2, G[6])
    for i, pi in enumerate(p):
        if math.sin(pi) != 0.0:
            h += np.kron(np.eye(n * n, dtype=complex), math.sin(pi) * G[i])
    return h


def lift8(m4, n):
    """Lift a 4 N^2 transverse matrix to the 8 N^2 spinor space (spin identity)."""
    sq = n * n
    a = m4.reshape(sq, 4, sq, 4)
    out = np.zeros((sq, 2, 4, sq, 2, 4), dtype=complex)
    for s in range(2):
        out[:, s, :, :, s, :] = a
    return out.reshape(8 * sq, 8 * sq)


# ============================================== supplied record-time mass profiles

def grid(n):
    u = np.arange(n)[:, None] - (n - 1) / 2.0
    v = np.arange(n)[None, :] - (n - 1) / 2.0
    return np.broadcast_to(u, (n, n)).copy(), np.broadcast_to(v, (n, n)).copy()


def prof_wall_s1(n, mag=M_DEF):
    u, _ = grid(n)
    return np.where(u < 0, -mag, mag), np.zeros((n, n))


def prof_quadrant(n, mag=M_DEF):
    u, v = grid(n)
    return -mag * np.sign(u) * np.sign(v), np.zeros((n, n))


def prof_radial(n, mag=M_DEF):
    u, v = grid(n)
    return np.where(np.hypot(u, v) < n / 4.0, -mag, mag), np.zeros((n, n))


def prof_uniform_topological(n, mag=M_DEF):
    return np.full((n, n), -mag), np.zeros((n, n))


def prof_vortex(n, w=1, core=0.0, dx=0.0, mag=M_DEF):
    """Winding-w complex mass of constant modulus (core = 0) or with a tanh core."""
    u, v = grid(n)
    u = u - dx
    r = np.hypot(u, v)
    th = np.arctan2(v, u)
    f = np.ones_like(r) if core <= 0 else np.tanh(r / core)
    return mag * f * np.cos(w * th), mag * f * np.sin(w * th)


def prof_pair(n, mag=M_DEF):
    """A vortex and an antivortex: winding +1 and -1 inside, ZERO at the boundary."""
    u, v = grid(n)
    ph = np.arctan2(v, u + n / 6.0) - np.arctan2(v, u - n / 6.0)
    return mag * np.cos(ph), mag * np.sin(ph)


def disc_mask(n, radius):
    u, v = grid(n)
    return np.hypot(u, v) < radius


def interior_mask(n, pad):
    m = np.zeros((n, n), dtype=bool)
    m[pad:n - pad, pad:n - pad] = True
    return m


# ==================================================== the basis-free chirality density

def spectrum(n, m1, m2, end_mode="hard", cut=CUT, shift=0.0):
    """One SVD of the square block A gives the whole spectrum and chi(x).

    In the CHI eigenbasis D_4 = [[0, A], [A^dag, 0]].  For each singular triple
    (s, u, v) the two eigenvectors are (u, +-v)/sqrt(2) at E = +-s, and CHI is
    -1 on the u half and +1 on the v half, so the chirality density of the pair
    is |v(x)|^2 - |u(x)|^2 -- exactly, and with no window step anywhere.  Zero
    singular values give (u, 0) and (0, v) separately and the same formula.
    """
    a = block_A(n, m1, m2, end_mode, shift)
    u_mat, sv, vh_mat = np.linalg.svd(a)
    v_mat = vh_mat.conj().T
    sel = sv < cut
    rest = sv[~sel]
    u = u_mat[:, sel].reshape(n * n, 2, -1)
    v = v_mat[:, sel].reshape(n * n, 2, -1)
    du = (np.abs(u) ** 2).sum(axis=1)
    dv = (np.abs(v) ** 2).sum(axis=1)
    dens = (dv - du).sum(axis=1).reshape(n, n)
    return dict(
        n_light=2 * int(sel.sum()),
        maxE=(float(sv[sel].max()) if sel.any() else float("nan")),
        gap=(float(rest.min()) if rest.size else float("inf")),
        dens=dens, sv=sv, u_mat=u_mat, v_mat=v_mat, A=a)


def boundary_projector_eigenvalues(res, n, mask, cut=CUT):
    """Boundary weights of every normalized direction in the full cutoff space.

    The chiral basis is (u,0),(0,v). A site mask does not mix those halves;
    the two Gram blocks therefore give the full compressed projector spectrum.
    """
    selected = res["sv"] < cut
    mask2 = np.repeat(np.asarray(mask, dtype=bool).ravel(), 2)
    blocks = [v[:, selected][mask2] for v in (res["u_mat"], res["v_mat"])]
    return np.concatenate([np.linalg.eigvalsh(v.conj().T @ v) for v in blocks])


def zones(res, n, core_radius=None, pad=None):
    d = res["dens"]
    if core_radius is None:
        core_radius = max(3.0, n / 6.0)
    if pad is None:
        pad = max(2, n // 6)
    inner = interior_mask(n, pad)
    return (float(d[disc_mask(n, core_radius)].sum()), float(d[inner].sum()),
            float(d[~inner].sum()), float(d.sum()), float(np.abs(d).max()))


def heat_index_density(res, n, lam):
    """q(x) = Tr_x[ CHI exp(-D_4^2 / lam^2) ].  Cut-free; sums to the exact index."""
    w = np.exp(-(res["sv"] / lam) ** 2)
    u = res["u_mat"].reshape(n * n, 2, -1)
    v = res["v_mat"].reshape(n * n, 2, -1)
    du = (np.abs(u) ** 2).sum(axis=1)
    dv = (np.abs(v) ** 2).sum(axis=1)
    return (((dv - du) * w).sum(axis=1)).reshape(n, n)


NETS = []


def record_net(tag, value):
    NETS.append((tag, abs(value)))


input_pins = verify_inputs()
check("SOURCE current own-note/memo/context hashes match (%d inputs)" % len(input_pins),
      set(input_pins) == set(AUDIT_INPUT_PATHS))

# ============================================================== GROUP A -- T1

print("== A  T1  Cl(7) exactly saturated, both chirality identities, and the rebuilt finite 1D "
      "diagnostic reproduced at its declared tolerance")

ANTI = max(nrm(G[a] @ G[b] + G[b] @ G[a] - 2 * (a == b) * np.eye(8))
           for a in range(7) for b in range(7))
HERM = max(nrm(g - g.conj().T) for g in G)
check("A1 [exact] two record-time coordinates plus a complex mass need SEVEN anticommuting "
      "Hermitian generators; Cl(7)'s irrep is 8-dimensional, so the spinor is 8-component and "
      "the algebra is EXACTLY SATURATED (7 is the maximum for 8x8): max ||{Gamma_A,Gamma_B} - "
      "2 delta|| = %.1e, max ||Gamma - Gamma^dag|| = %.1e" % (ANTI, HERM),
      ANTI == 0.0 and HERM == 0.0)

R_TRANSVERSE = nrm(G[3] @ G[4] @ G[5] @ G[6] - CHI8)
R_SPATIAL = nrm(-1j * G[0] @ G[1] @ G[2] - CHI8)
C_COMM = max(nrm(CHI8 @ g - g @ CHI8) for g in G[:3])
C_ANTI = max(nrm(CHI8 @ g + g @ CHI8) for g in G[3:])
check("A2 [exact] the 3+1D chirality is the volume element of the supplied spatial Clifford "
      "algebra inside the enlarged one: CHI = Gamma_4 Gamma_5 Gamma_6 Gamma_7 = -i Gamma_1 "
      "Gamma_2 Gamma_3, both identities at residual %.1e / %.1e; CHI^2 = 1, Hermitian, "
      "traceless, commuting with Gamma_1,2,3 (%.1e) and anticommuting with Gamma_4..7 (%.1e)"
      % (R_TRANSVERSE, R_SPATIAL, C_COMM, C_ANTI),
      R_TRANSVERSE == 0.0 and R_SPATIAL == 0.0 and C_COMM == 0.0 and C_ANTI == 0.0
      and nrm(CHI8 @ CHI8 - np.eye(8)) == 0.0 and nrm(CHI8 - CHI8.conj().T) == 0.0
      and abs(np.trace(CHI8)) < 1e-13)

NS1 = 64
M1D = np.full(NS1, -M_DEF)
M1D[NS1 // 2:] = M_DEF
K1D, L1D = chain_ops(NS1, "hard")
D1D = np.kron(K1D, S2) + np.kron(np.diag(M1D) + R_S * L1D, S3)
EV1, EVEC1 = np.linalg.eigh(D1D)
IDX1 = np.where(np.abs(EV1) < CUT)[0]
GAP1 = float(np.abs(EV1[np.abs(EV1) >= CUT]).min())
V1 = EVEC1[:, IDX1].reshape(NS1, 2, -1)
CD1 = np.einsum("scm,cd,sdm->s", V1.conj(), -S1, V1).real
check("A3 [1e-8] the 1D control, built with the GENUINE Cl(5) operator d = K_s sigma_2 + "
      "[diag(m) + r_s L_s] sigma_3, chi = i sigma_2 sigma_3, N_s = 64: %d light states per "
      "transverse mode, max|E| %.3e, next |E| %.6f; wall window [24,40) %+.12f, doubled by the "
      "supplied spin multiplicity to %+.9f against the historical +1.999950592685428 fixture; left end "
      "%+.9f, right end %+.9f, net %+.2e"
      % (len(IDX1), float(np.abs(EV1[IDX1]).max()), GAP1, CD1[24:40].sum(),
         2 * CD1[24:40].sum(), CD1[0:8].sum(), CD1[56:64].sum(), CD1.sum()),
      len(IDX1) == 2 and abs(2 * CD1[24:40].sum() - 1.999950592685428) < 1e-8
      and abs(CD1[0:8].sum() + 1.0) < 1e-8 and abs(CD1[56:64].sum()) < 1e-8
      and abs(CD1.sum()) < 1e-12 and abs(GAP1 - 0.801213) < 1e-6)

# ============================================================== GROUP B -- T2

print("== B  T2  a REAL mass has cancelling signed full-cutoff chirality: the "
      "density vanishes POINTWISE")

N24 = 24
D_REAL = D4(N24, *prof_wall_s1(N24))
G7_SITE = np.kron(np.eye(N24 * N24, dtype=complex), A4)
AC_D = nrm(G7_SITE @ D_REAL + D_REAL @ G7_SITE)
AC_CHI = max(nrm(A4 @ a + a @ A4) for a in ALPHA[:3] + [B4])
DIAG_OFF = nrm(G7_SITE - np.kron(np.eye(N24 * N24, dtype=complex), A4))
check("B1 [exact] with a REAL mass the seventh generator Gamma_7 is UNUSED and site-diagonal, "
      "with {Gamma_7, alpha_1,2,3} = {Gamma_7, CHI} = %.1e and {Gamma_7, D_4} = %.1e; it maps "
      "ker D_4 to ker D_4 and flips the chirality without leaving the site, so every zero mode "
      "has a SAME-SITE partner of opposite chirality.  An identity of the algebra, independent "
      "of profile and end convention" % (AC_CHI, AC_D),
      AC_CHI == 0.0 and AC_D == 0.0 and DIAG_OFF == 0.0)

REAL_PROFILES = (
    ("a wall in s_1", prof_wall_s1),
    ("the crossed-wall quadrant", prof_quadrant),
    ("the radial wall", prof_radial),
    ("the uniform topological mass", prof_uniform_topological),
)
WORST_REAL = 0.0
for tag, fn in REAL_PROFILES:
    res = spectrum(N24, *fn(N24))
    core, inner, edge, net, mx = zones(res, N24)
    record_net(tag, net)
    WORST_REAL = max(WORST_REAL, mx)
    check("B2 [1e-12] %s at 24x24: %d light states, max|E| %.3e, next |E| %.6f, "
          "max_x |chi(x)| = %.3e -- zero AT EVERY SITE, not merely on average "
          "(interior %+.9f, edge %+.9f, net %+.2e)"
          % (tag, res["n_light"], res["maxE"], res["gap"], mx, inner, edge, net),
          mx < 1e-12 and abs(net) < 1e-12)

N16 = 16
LC = [(n, spectrum(n, *prof_wall_s1(n))["n_light"]) for n in (N16, N24)]
check("B3 [exact] a wall in s_1 is a codimension-ONE wall in a TWO-dimensional transverse "
      "space, not the 1D pairing: its light-state count GROWS with the square, %s -- a "
      "finite comparison along the supplied second coordinate"
      % ", ".join("%d at %dx%d" % (c, n, n) for n, c in LC),
      LC[0][1] == 8 and LC[1][1] == 16 and LC[1][1] > LC[0][1])

# ============================================================== GROUP C -- T3

print("== C  T3  a COMPLEX mass: finite counts and masked signed density near winding")

for w, tol, why in ((-1, 1e-3, ""), (1, 1e-3, ""), (2, 1e-3, ""),
                    (3, 2e-3, "; the deficit is larger here because the winding-3 modes are "
                              "broader than the pad-4 interior mask on a 24x24 square -- a "
                              "finite-size property of the mask, the light-state count 2|n| "
                              "being exact")):
    res = spectrum(N24, *prof_vortex(N24, w=w))
    core, inner, edge, net, _ = zones(res, N24)
    record_net("vortex n = %+d" % w, net)
    check("C1 [%.0e] winding %+d at 24x24: EXACTLY %d light states (2|n| in this fixture), max|E| %.3e against a "
          "next |E| of %.5f, interior chirality %+.9f approximately the winding, %+.9f on the outer "
          "boundary%s" % (tol, w, res["n_light"], res["maxE"], res["gap"], inner, edge, why),
          res["n_light"] == 2 * abs(w) and abs(inner - w) < tol and abs(edge + w) < tol)

N32 = 32
R32 = spectrum(N32, *prof_vortex(N32, w=1))
C32, I32, E32, NET32, _ = zones(R32, N32)
RING32 = float(R32["dens"][~interior_mask(N32, 2)].sum())
CUM32 = [(w, float(R32["dens"][disc_mask(N32, w)].sum())) for w in (2, 4, 8, 12)]
record_net("vortex n = +1, 32x32", NET32)
check("C2 [1e-4] winding +1 at 32x32: 2 light states, max|E| %.3e against a next |E| of %.5f, "
      "chirality %+.9f inside r < N/4 and %+.9f on the outer boundary ring; cumulatively inside "
      "radius W, %s -- opposite chiral subspaces concentrate at core and boundary"
      % (R32["maxE"], R32["gap"],
         float(R32["dens"][disc_mask(N32, N32 / 4.0)].sum()), RING32,
         ", ".join("W=%d %+.9f" % t for t in CUM32)),
      R32["n_light"] == 2 and abs(float(R32["dens"][disc_mask(N32, N32 / 4.0)].sum()) - 1.0) < 1e-4
      and RING32 < -0.99)

RF = spectrum(N24, *prof_vortex(N24, w=1), end_mode="free")
RT = spectrum(N24, *prof_vortex(N24, w=1, core=1.5))
RH = spectrum(N24, *prof_vortex(N24, w=1))
CORE_H = float(RH["dens"][disc_mask(N24, 4.0)].sum())
CORE_F = float(RF["dens"][disc_mask(N24, 4.0)].sum())
record_net("vortex n = +1, free ends", zones(RF, N24)[3])
record_net("vortex n = +1, tanh core", zones(RT, N24)[3])
OFF = []
for dx in (0.0, 2.0, 4.0):
    r = spectrum(N24, *prof_vortex(N24, w=1, dx=dx))
    OFF.append((dx, r["n_light"], float(r["dens"][disc_mask(N24, 4.0)].sum())))
    record_net("vortex n = +1, offset %.0f" % dx, zones(r, N24)[3])
check("C3 [1e-3] the finite count is unchanged in these tests by the end convention (core "
      "disc, hard %+.9f against free %+.9f, 2 light states each), by the core shape (tanh core "
      "interior %+.9f against %+.9f for constant modulus) and by the core position (%s: the "
      "chirality in a disc about the ORIGIN falls away as the core sits elsewhere, the count "
      "staying at 2)"
      % (CORE_H, CORE_F, zones(RT, N24)[1], zones(RH, N24)[1],
         ", ".join("dx=%.0f: %d light, %+.9f" % t for t in OFF)),
      RF["n_light"] == 2 and RT["n_light"] == 2 and abs(zones(RT, N24)[1] - 1.0) < 1e-3
      and all(t[1] == 2 for t in OFF) and OFF[0][2] > OFF[1][2] > OFF[2][2])

HK = [(lam, heat_index_density(R32, N32, lam)) for lam in (0.1, 0.2, 0.4)]
check("C4 [1e-3] cut-free: the heat-kernel index density q(x) = Tr_x[CHI exp(-D_4^2/lam^2)], "
      "which uses NO light-mode cut and sums to the exact index for any lam, gives at 32x32 %s "
      "(core r < N/4, ring the outer boundary), lambda=0.1 closely matches the light-mode core number "
      "well inside the %.5f gap"
      % ("; ".join("lam=%.1f sum %+.1e core %+.12f ring %+.9f"
                   % (lam, q.sum(), q[disc_mask(N32, N32 / 4.0)].sum(),
                      q[~interior_mask(N32, 2)].sum()) for lam, q in HK), R32["gap"]),
      abs(HK[0][1][disc_mask(N32, N32 / 4.0)].sum() - 1.0) < 1e-3
      and all(abs(q.sum()) < 1e-12 for _, q in HK))

N20 = 20
MV1, MV2 = prof_vortex(N20, w=1)
R20 = spectrum(N20, MV1, MV2)
SEL20 = np.where(R20["sv"] < CUT)[0]
COLS = []
for k in SEL20:
    for sg in (+1, -1):
        p4 = np.zeros((N20 * N20, 4), dtype=complex)
        p4[:, 0:2] = R20["u_mat"][:, k].reshape(N20 * N20, 2)
        p4[:, 2:4] = sg * R20["v_mat"][:, k].reshape(N20 * N20, 2)
        p4 /= math.sqrt(2.0)
        for a in range(2):
            p8 = np.zeros((N20 * N20, 2, 4), dtype=complex)
            p8[:, a, :] = p4
            COLS.append((sg * R20["sv"][k], p8.ravel()))
PSI = np.column_stack([c for _, c in COLS])
EPSI = np.array([e for e, _ in COLS])
H20 = H8(N20, MV1, MV2)
RES20 = nrm(H20 @ PSI - PSI * EPSI)
del H20
CHI_SITE = np.kron(np.eye(N20 * N20, dtype=complex), CHI8)
XW, XV = np.linalg.eigh(PSI.conj().T @ CHI_SITE @ PSI)
UMODE = PSI @ XV
OCC = (np.abs(UMODE.reshape(N20 * N20, 8, -1)) ** 2).sum(axis=1)
COREMASK = disc_mask(N20, N20 / 4.0).ravel()
CW = [float((OCC[:, j] / OCC[:, j].sum())[COREMASK].sum()) for j in range(len(XW))]
CW_PLUS = float(np.mean([CW[j] for j in range(len(XW)) if XW[j] > 0]))
CW_MINUS = float(np.mean([CW[j] for j in range(len(XW)) if XW[j] < 0]))
check("C5 [1e-9] on the full 8-component operator at N = 20 (dense dimension %d) the four "
      "light states are exhibited explicitly, satisfying H PSI = PSI E at residual %.1e with "
      "max|E| %.3e against a next |E| of %.6f; CHI splits them into EXACT doublets at %+.9f and "
      "%+.9f, the chi = +1 doublet core-bound to %.4f%% and the chi = -1 doublet holding %.1e "
      "of its weight in the core"
      % (8 * N20 * N20, RES20, float(np.abs(EPSI).max()), float(R20["gap"]),
         XW[-1], XW[0], 100.0 * CW_PLUS, CW_MINUS),
      RES20 < 1e-11 and len(XW) == 4 and abs(XW[0] + 1) < 1e-9 and abs(XW[1] + 1) < 1e-9
      and abs(XW[2] - 1) < 1e-9 and abs(XW[3] - 1) < 1e-9
      and CW_PLUS > 0.99 and CW_MINUS < 1e-5)

HAND = {}
for tag, sel in (("core", XW > 0), ("boundary", XW < 0)):
    uu = UMODE[:, sel]
    vmats = [uu.conj().T @ np.kron(np.eye(N20 * N20, dtype=complex), G[i]) @ uu
             for i in range(3)]
    sq = max(nrm(vmats[i] @ vmats[i] - np.eye(uu.shape[1])) for i in range(3))
    ac = max(nrm(vmats[i] @ vmats[j] + vmats[j] @ vmats[i])
             for i in range(3) for j in range(3) if i != j)
    HAND[tag] = (float(np.trace(vmats[0] @ vmats[1] @ vmats[2]).imag) / 2.0, sq, ac)
check("C6 [1e-8] the projected velocities V_i = u^dag Gamma_i u close the Clifford algebra on "
      "each doublet (||V^2-1|| <= %.1e, ||{V_i,V_j}|| <= %.1e) and the handedness "
      "Tr(V_1V_2V_3)/2i is %+.9f at the core against %+.9f on the boundary: OPPOSITE handedness. "
      "Here handedness = +<chi>; in the rebuilt finite 1D embedding it is -<chi>.  Embedding convention differs; a "
      "reader comparing the two tables sees the correlation flip sign"
      % (max(HAND[t][1] for t in HAND), max(HAND[t][2] for t in HAND),
         HAND["core"][0], HAND["boundary"][0]),
      abs(HAND["core"][0] - 1.0) < 1e-8 and abs(HAND["boundary"][0] + 1.0) < 1e-8
      and max(HAND[t][1] for t in HAND) < 1e-8 and max(HAND[t][2] for t in HAND) < 1e-8)

IDENT = []
for nn in (12, N20):
    m1, m2 = prof_vortex(nn, w=1)
    for frac in (0.0, 0.2, 0.4):
        q = frac * math.pi
        h = H8(nn, m1, m2, p=(q, 0.0, 0.0))
        dt = D4(nn, m1, m2, shift=R_SPACE * (1.0 - math.cos(q)))
        rhs = math.sin(q) ** 2 * np.eye(8 * nn * nn) + lift8(dt @ dt, nn)
        IDENT.append((nn, frac, nrm(h @ h - rhs) / nrm(rhs)))
        del h, rhs, dt
check("C7 [1e-12] because Gamma_1,2,3 anticommute with every transverse generator, "
      "H(p)^2 = (sum_i sin^2 p_i) 1 + D_4(p)^2 is an OPERATOR identity: relative residual %s"
      % ", ".join("%.1e at N=%d, q=%.2f pi" % (e, n, f) for n, f, e in IDENT),
      max(e for _, _, e in IDENT) < 1e-12)

CONE = []
for frac in (0.0, 0.05, 0.10, 0.20, 0.40):
    q = frac * math.pi
    delta = float(np.linalg.svd(
        block_A(N20, MV1, MV2, shift=R_SPACE * (1.0 - math.cos(q))),
        compute_uv=False).min())
    CONE.append((frac, abs(math.sin(q)), delta, math.sqrt(math.sin(q) ** 2 + delta ** 2)))
QD = 0.10 * math.pi
E_DIRECT = float(np.sort(np.abs(np.linalg.eigvalsh(
    H8(N20, MV1, MV2, p=(QD, 0.0, 0.0)))))[0])
check("C8 [1e-9] the finite paired branch has a nonzero splitting, |E(q)| = sqrt(sin^2 q + "
      "Delta(q)^2) with Delta the finite-size transverse splitting: %s.  Diagonalizing the full "
      "8-component operator directly at q = 0.10 pi gives lowest |E| = %.12f against the "
      "predicted %.12f, to 10 decimals; the departure from |sin q| at larger q is entirely "
      "Delta(q)"
      % ("; ".join("q/pi %.2f: |sin q| %.9f, Delta %.3e, |E| %.9f" % c for c in CONE),
         E_DIRECT, CONE[2][3]),
      abs(E_DIRECT - CONE[2][3]) < 1e-9 and CONE[0][3] < 1e-5)

# ============================================================== GROUP D -- T4

print("== D  T4  the net over the whole square is identically zero, by linear algebra on a "
      "SQUARE block, not by the record-time geometry")

NB = 8
MB1, MB2 = prof_vortex(NB, w=1)
DB = D4(NB, MB1, MB2)
CHI_B = np.kron(np.eye(NB * NB, dtype=complex), B4)
AC_B = nrm(DB @ CHI_B + CHI_B @ DB)
DP = DB.reshape(NB * NB, 2, 2, NB * NB, 2, 2).transpose(1, 0, 2, 4, 3, 5).reshape(4 * NB * NB, 4 * NB * NB)
HALF = 2 * NB * NB
AB = block_A(NB, MB1, MB2)
BLOCK_RES = max(nrm(DP[:HALF, HALF:] - AB), nrm(DP[HALF:, :HALF] - AB.conj().T),
                nrm(DP[:HALF, :HALF]), nrm(DP[HALF:, HALF:]))
check("D1 [exact] {D_4, CHI} = 0 at residual %.1e on the lattice, for every profile and end "
      "convention, so in the CHI eigenbasis D_4 = [[0, A], [A^dag, 0]] at residual %.1e with A "
      "of shape %s -- SQUARE, each CHI eigenspace having dimension 2 N^2.  For a square matrix "
      "dim ker A = dim ker A^dag identically, so the index of this balanced finite realization is "
      "zero by equal chiral dimensions, not finiteness alone or record-time "
      "geometry"
      % (AC_B, BLOCK_RES, AB.shape),
      AC_B == 0.0 and BLOCK_RES == 0.0 and AB.shape[0] == AB.shape[1])

WORST_NET = max(v for _, v in NETS)
WORST_TAG = max(NETS, key=lambda t: t[1])[0]
check("D2 [1e-12] the net chirality over the WHOLE square is zero on every one of the %d "
      "profiles and sizes above, worst |net| = %.2e (%s)"
      % (len(NETS), WORST_NET, WORST_TAG), WORST_NET < 1e-12)

GAPS = []
for tfrac in (0.0, 0.25, 0.5, 0.75, 1.0):
    th = tfrac * math.pi
    a = M_DEF * math.cos(th)
    b = M_DEF * math.sin(th)
    row = []
    for k1, k2 in ((0.0, 0.0), (math.pi, 0.0), (0.0, math.pi), (math.pi, math.pi)):
        mk = a + R_S * (2 - math.cos(k1) - math.cos(k2))
        row.append(math.sqrt(math.sin(k1) ** 2 + math.sin(k2) ** 2 + mk ** 2 + b ** 2))
    GAPS.append(row)
MODULUS = float(np.abs(np.hypot(*prof_vortex(N24, w=1))).min())
check("D3 [1e-9] the sampled vortex profile has "
      "constant modulus |m| = %.6f; its separate constant-symbol comparison is "
      "gapped at all four record-time zone corners for every phase -- %.6f at (0,0), at least "
      "%.6f at (pi,0)/(0,pi), at least %.6f at (pi,pi) -- these constant-symbol corner values do not classify the "
      "inhomogeneous operator or exclude interfaces and boundary states"
      % (MODULUS, GAPS[0][0], min(min(r[1], r[2]) for r in GAPS), min(r[3] for r in GAPS)),
      abs(MODULUS - M_DEF) < 1e-9
      and all(abs(r[0] - M_DEF) < 1e-9 for r in GAPS)
      and min(min(r[1], r[2]) for r in GAPS) > 1.19
      and min(r[3] for r in GAPS) > 3.19)

RP = spectrum(N24, *prof_pair(N24))
DPAIR = RP["dens"]
LEFT = np.roll(disc_mask(N24, 4.0), -int(N24 / 6.0), axis=0)
RIGHT = np.roll(disc_mask(N24, 4.0), int(N24 / 6.0), axis=0)
_, _, EDGE_P, NET_P, _ = zones(RP, N24)
record_net("vortex/antivortex pair", NET_P)
check("D4 [1e-12] a vortex/antivortex pair -- winding +1 and -1 inside, ZERO winding at the "
      "square's boundary -- has signed boundary cancellation, |chi(edge)| = %.1e, both interior "
      "masked core contributions at %+.9f and %+.9f on the two cores, %d light states, net %+.2e.  This "
      "signed cancellation alone does not exclude boundary-localized states"
      % (abs(EDGE_P), float(DPAIR[LEFT].sum()), float(DPAIR[RIGHT].sum()),
         RP["n_light"], NET_P),
      abs(EDGE_P) < 1e-12 and float(DPAIR[LEFT].sum()) > 0.9
      and float(DPAIR[RIGHT].sum()) < -0.9 and abs(NET_P) < 1e-12)

# ============================================================== GROUP E -- T5

print("== E  T5  the price, and the supplied items the construction is a function of")

SUPPLIED = ("an ordered record-time coordinate with nearest-neighbour adjacency", "K_s",
            "r_s L_s", "a record-time Clifford generator", "a mass field m(s)",
            "a finite extent N", "an end convention")
ADDED = ("a SECOND ordered record index s_2, independent of the first, with its own K_2, "
         "Wilson term and Clifford generator",
         "a PHASE-VALUED mass m_1 + i m_2 carrying a winding, with its seventh Clifford "
         "generator and the 8-component embedding")
K1R, K2R, D1R, D2R = mass_blocks(N24, *prof_vortex(N24, w=1), "hard", 0.0)
REBUILD = nrm(np.kron(K1R, A1) + np.kron(K2R, A2) + np.kron(D1R, A3) + np.kron(D2R, A4)
              - D4(N24, *prof_vortex(N24, w=1)))
DROP = (nrm(np.kron(K1R, A1)), nrm(np.kron(K2R, A2)), nrm(np.kron(D1R, A3)),
        nrm(np.kron(D2R, A4)))
check("E1 [exact] the construction is rebuilt from the listed supplied objects -- %s "
      "-- with the additional definitions: %s.  Rebuilt from them alone it reproduces the winding-1 "
      "operator at residual %.1f, and deleting each displayed term changes the "
      "operator by %s; this is not an independent-necessity proof"
      % ("; ".join(SUPPLIED), "; ".join(ADDED), REBUILD,
         ", ".join("%.3f" % v for v in DROP)),
      REBUILD == 0.0 and all(v > 1e-9 for v in DROP))

print("SCOPE: auxiliary grid and coefficients are supplied; no Record history, phase formation, "
      "physical species selection, minimal supplier count or gauge inflow is established.")
print("SUMMARY: finite signed cancellation, vortex localization and paired dispersion; "
      "local masked traces are scale dependent and the balanced global index is zero.")
# Focused corrections test actual constructors and observables.
small = spectrum(12, *prof_wall_s1(12))
check("R1 real wall N12: %d light states, %d chiral directions of each sign; signed density %.3e"
      % (small["n_light"], small["n_light"] // 2, np.max(np.abs(small["dens"]))),
      small["n_light"] == 8 and np.max(np.abs(small["dens"])) < 1e-12)
small = spectrum(12, *prof_vortex(12))
k = int(np.argmin(small["sv"]))
phi = np.zeros((12 * 12, 4), complex)
phi[:, 2:] = small["v_mat"][:, k].reshape(12 * 12, 2)
phi = phi.ravel()
dphi = D4(12, *prof_vortex(12)) @ phi
energy = float(np.vdot(phi, dphi).real)
residual = nrm(dphi - energy * phi)
check("R2 chiral vector is not an energy eigenmode: N12 mean E %.3e, residual %.12g, splitting %.12g"
      % (energy, residual, small["sv"][k]),
      abs(energy) < 1e-12 and residual > 1e-4 and abs(residual - small["sv"][k]) < 1e-12)
heat_rows = [(lam, heat_index_density(small, 12, lam)) for lam in (0.1, 1.0, 10.0)]
heat_core = [float(q[disc_mask(12, 3)].sum()) for _, q in heat_rows]
check("R3 local heat trace depends on lambda: core at 0.1,1,10 = %s; full traces remain zero"
      % heat_core, all(abs(q.sum()) < 1e-12 for _, q in heat_rows)
      and heat_core[0] > heat_core[1] > heat_core[2] and heat_core[0] - heat_core[2] > 0.5)
edge_mask = ~interior_mask(N24, 4)
edge_eigs = boundary_projector_eigenvalues(RP, N24, edge_mask)
edge_point = float(np.max(np.abs(RP["dens"][edge_mask])))
check("R4 pair N24: compressed boundary eigenvalues %s, unsigned trace %.12g, max pointwise signed %.12g; "
      "all low-space directions have boundary weight below declared localization threshold 0.5"
      % (edge_eigs.tolist(), edge_eigs.sum(), edge_point),
      len(edge_eigs) == RP["n_light"] == 2 and np.min(edge_eigs) > 0
      and np.max(edge_eigs) < 0.5 and edge_eigs.sum() > 1e-3 and edge_point > 1e-5)
# Rectangular off-diagonal blocks need not have zero index.
rect = np.array([[1., 0., 0.], [0., 1., 0.]])
check("R5 finite rectangular 2x3 block has nullities 1 and 0, so finiteness alone does not force index zero",
      rect.shape[1] - np.linalg.matrix_rank(rect) == 1
      and rect.shape[0] - np.linalg.matrix_rank(rect.conj().T) == 0)
# For rs=1, 0<M<=1 and x=1-cos(k1), y=1-cos(k2),
# E^2-M^2 >= 2(1-M)(x+y)+2xy >=0, uniformly in mass phase.
uniform_gap_min = float("inf")
for k1 in np.linspace(-math.pi, math.pi, 17):
    for k2 in np.linspace(-math.pi, math.pi, 17):
        for theta in np.linspace(-math.pi, math.pi, 13):
            x, y = 1-math.cos(k1), 1-math.cos(k2)
            square = math.sin(k1)**2 + math.sin(k2)**2 + (M_DEF*math.cos(theta)+x+y)**2 + (M_DEF*math.sin(theta))**2
            uniform_gap_min = min(uniform_gap_min, square - M_DEF**2)
check("R6 separate uniform symbol: E^2-M^2 minimum %.3e on control grid; analytic bound holds for rs=1, 0<M<=1"
      % uniform_gap_min, 0 < M_DEF <= 1 and uniform_gap_min > -1e-14)

print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
sys.exit(0 if FAIL == 0 else 1)
