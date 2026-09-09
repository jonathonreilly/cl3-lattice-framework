#!/usr/bin/env python3
"""The vacuum's response under the rate ruler anti-screens, and the
sea-referenced source removes it.

Class-A runner.  Conditional on exactly what the formation-rate-ruler note
(F1) is conditional on -- the designed fermion law, the landed weak-field
response surface phi = G0 P0 rho, the CHOICE of the half-filled staggered sea
as the vacuum, and the spatial-metric note's DECLARED two-weight family

    H(alpha, beta) = sum_bonds [1 + alpha (Phi_v + Phi_j)/2] M_vj
                   + sum_v     [1 + beta  Phi_v]            m eps_v n_v

-- and on three STIPULATIONS made here and derived from nothing: (V1) the
bridge's Phi is minus its phi, since the coordinate energy of a static body is
m(1 + Phi) and phi > 0 near a source, so Phi is the Newtonian potential;
(V2) the vacuum's Phi-linear energy density is fed back into the bridge's
source at FIRST order only, the field equation being solved with the response
linearised about Phi = 0; (V3) the reference an energy density is counted from
is a LAW-LEVEL declaration, three candidates being run side by side --
half filling (I/2), the fixed sea P(0), and the field-dressed sea P(Phi).

F1 named, as its second price, a Phi-linear vacuum energy fed back through the
bridge, and left its sign, its size and its removability open.  This runner
takes that named interface.

  A  (T1)  THE SIGN AND WHAT IT COSTS.  The sea's own energy density is
           NEGATIVE at every site and every mass and K(alpha) > 0, so
           chi_vac < 0; with Phi = -phi the induced term is
           mass^2 = chi_0/(1 + c) < 0 -- ANTI-SCREENING.  The bridge operator
           -Delta_lat + mass^2 loses positivity on every torus tried, so no
           length exists; the term is present already at the parent's coupling
           H(1,1); and K(alpha) >= beta = 1 on the ruler surface alpha >= 1,
           so no (kappa_r, nu_r) removes it.
  B  (T2)  THE SEA-REFERENCED SOURCE.  tr(H dP/dPhi) = 0 for a spectral
           projector, so the k = 0 response of ANY sea-referenced source
           vanishes; the fixed reference leaves chi(0) = 0 to numerical
           precision and a pure Laplacian residual, G -> 1.00534 G and no
           mass; the field-dressed reference -- the landed definition read
           literally -- leaves the ZERO FUNCTION.
  C  (T3)  THREE ROUTES.  (a) the constant-mode projector P0 acts as the
           identity on this term; (b) the counterterm route IS the landed
           definition, at the declared price Lambda_vac = 0, i.e. R = infinity
           in the landed identity Lambda_vac = 3/R^2; (c) the F1 rate fixed
           point does not absorb the term -- chi_vac = E^(0) kappa_r*
           reproduces the computed value, so anti-screening is what alpha* = 2
           COSTS.
  D  (T4)  THE TWO-BODY LAW.  Unsubtracted, the landed E1 E2 G(D) is destroyed
           -- sign flips and order-ten magnitudes on the landed response boxes.
           On the sea reference it survives as a flat sub-per-cent rescaling of
           the coupling.  The tolerance: 1 per cent survival needs a length of
           at least 100 spacings.
  E  (T5)  TWO CORRECTIONS TO THE BRIEFED PREMISES.  The bridge's G0 = H^{-1}
           carries NO coupling constant, so G = 1 in lattice units and
           G_Newton = 1/(4 pi) per spacing; and the gradient coefficient c is
           NOT the vacuum mass fraction w_m.

Groups A3, A4, B3, C1, C2 and E1's normalisation statement are exact
identities; every other check is a finite floating-point computation reporting
its residual against a tolerance declared before the run.  Every response is an
exact central difference in the field knob, so the O(Phi^2) part cancels by
construction and nothing is fitted except the two declared linear regressions
of chi(k) on lambda_k, whose maximum residual is printed.

No random number is drawn anywhere: every mass, coupling, wavevector, box,
distance and field knob is a declared constant, so the runner is
bit-reproducible without a seed.

Largest dense object: the 12 x 12 x 12 periodic sea's one-body matrix,
1728 x 1728.  The many-body cross-check is the 2 x 2 x 3 coarse cube read in
its 12-qubit space (dim 2^12 = 4096), whose half-filled sector has dimension
924; nothing above 4096 x 4096 is formed.  Every torus kernel is an FFT on
vectors, never a matrix.

This runner is self-contained: it re-declares the coarse lattice, the KS sign
field, the record-native staggered mass, the two-weight family, the local
energy density, the three references, the bridge kernel and the response, and
imports nothing from the repository.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""
from __future__ import annotations

import sys

import numpy as np

AUDIT_TIMEOUT_SEC = 300

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


PI = np.pi
GK = 1.0e-5                        # the field knob; every response is a central difference in it
GK_MB = 1.0e-4                     # the many-body knob
FULL, ENERGY = (2.0, 1.0), (1.0, 1.0)
MASSES = (0.0, 0.3, 0.9, 1.0, 2.0, 6.0)
LANDED_D = (3, 4, 6, 8, 10, 16)    # the distances the landed notes tabulate
LANDED_LB = (32, 64)               # the landed notes' response boxes


# ===================================================== THE LATTICE, DECLARED HERE

def eta_ks(v, a):
    """Kawamoto-Smit sign of the coarse bond (v, v + e_a)."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


class Box:
    """A dense coarse box: hopping matrix, half-filled sea, local energy density."""

    def __init__(self, Lx, Ly, Lz, per=(False, False, False)):
        self.L = (Lx, Ly, Lz)
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(*[np.arange(n) for n in self.L], indexing="ij")
        self.ix, self.iy, self.iz = ix.ravel(), iy.ravel(), iz.ravel()
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()
        r, c, val = [], [], []

        def idx(a, b, k):
            return (a * Ly + b) * Lz + k

        for a in range(Lx):
            for b in range(Ly):
                for k in range(Lz):
                    i, v = idx(a, b, k), (a, b, k)
                    for ax in range(3):
                        w = [a, b, k]
                        w[ax] += 1
                        if w[ax] >= self.L[ax]:
                            if not per[ax]:
                                continue
                            w[ax] = 0
                        j = idx(*w)
                        s = float(eta_ks(v, ax))
                        r += [i, j]
                        c += [j, i]
                        val += [s, s]
        self.r, self.c = np.array(r), np.array(c)
        self.vhop = np.array(val)
        self.zero = np.zeros(self.V)
        self.one = np.ones(self.V)

    def hmat(self, m, Phi, ab):
        """The declared two-weight family H(alpha, beta) on this box."""
        alpha, beta = ab
        H = np.zeros((self.V, self.V))
        np.add.at(H, (self.r, self.c),
                  self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c])))
        return H + np.diag(m * self.sgn * (1.0 + beta * Phi))

    def sea(self, H):
        """The half-filled sea: the spectral projector on the negative levels."""
        w, U = np.linalg.eigh(H)
        occ = (w < -1e-12).astype(float) + 0.5 * (np.abs(w) <= 1e-12)
        return (U * occ) @ U.T

    def dens(self, m, Phi, ab):
        """(record odds, E_v, hop part, mass part), E_v counted from HALF FILLING."""
        H = self.hmat(m, Phi, ab)
        R = self.sea(H)
        Rt = R - 0.5 * np.eye(self.V)
        Ev = np.einsum("vj,jv->v", H, Rt)
        Em = np.diag(H) * np.diag(Rt)
        return np.diag(R).copy(), Ev, Ev - Em, Em

    def wave(self, nvec):
        """The declared plane-wave field profile cos(k.v), k = 2 pi n / L."""
        kk = [2 * PI * nvec[i] / self.L[i] for i in range(3)]
        return np.cos(kk[0] * self.ix + kk[1] * self.iy + kk[2] * self.iz)


P4 = Box(4, 4, 4, per=(True, True, True))
P8 = Box(8, 8, 8, per=(True, True, True))


# ==================================== A (T1). THE SIGN, AND WHAT NO RULER REMOVES

def e0_and_K(box, m, alpha):
    """E^(0)_v (SIGNED) and K = (dE_v/dPhi)/E_v for a UNIFORM Phi."""
    Ep = box.dens(m, +GK * box.one, (alpha, 1.0))[1]
    Em = box.dens(m, -GK * box.one, (alpha, 1.0))[1]
    E0 = box.dens(m, box.zero, (alpha, 1.0))[1]
    dE = (Ep - Em) / (2 * GK)
    return E0, dE, dE / E0


ROWS = []
for m in MASSES:
    E0, dE, K1 = e0_and_K(P4, m, 1.0)
    _, _, K2 = e0_and_K(P4, m, 2.0)
    _, Ev, _, Em = P4.dens(m, P4.zero, ENERGY)
    ROWS.append((m, float(E0.mean()), float(np.max(np.abs(E0 - E0.mean()))),
                 float((Em / Ev).mean()), float(K1.mean()), float(K2.mean())))
print("   m     E^(0)_v      spread     w_m        K(1)      K(2)      chi_vac[H(2,1)]")
for q in ROWS:
    print("  %4.1f  %+11.8f  %8.1e  %.6f  %.6f  %.6f  %+12.7f"
          % (q[0], q[1], q[2], q[3], q[4], q[5], q[1] * q[5]))
M1 = [q for q in ROWS if q[0] == 1.0][0]
check(
    "A1 [numerical, exact sign] THE SEA'S OWN LOCAL ENERGY DENSITY IS NEGATIVE AT EVERY SITE AND "
    "EVERY MASS. On the 4x4x4 periodic half-filled staggered sea E^(0)_v = %+0.5f at m = 1 with "
    "site spread %.1e, and E^(0)_v < 0 for every m in 0, 0.3, 0.9, 1, 2, 6. This sign decides "
    "anti-screening against a Yukawa suppression" % (M1[1], M1[2]),
    all(q[1] < 0 for q in ROWS) and max(q[2] for q in ROWS) < 1e-13,
)
KFORM = max(abs(q[5] - (2.0 * (1 - q[3]) + q[3])) for q in ROWS)
check(
    "A2 [numerical, 1e-9] chi_vac IS NEGATIVE AND OF ORDER ONE IN LATTICE UNITS. Writing the "
    "Phi-linear part of the sea's energy density as delta eps_v = chi_vac Phi_v, chi_vac = "
    "E^(0)_v K(alpha) with K(alpha) = alpha (1 - w_m) + beta w_m > 0, so chi_vac < 0 ALWAYS. At "
    "m = 1: w_m = %.6f, K(2) = %.6f matching the exact form to %.1e, chi_vac[H(2,1)] = %+0.7f and "
    "chi_vac[H(1,1)] = %+0.7f; F1's price (alpha-1)(1-w_m) = %.6f is the difference K(2) - K(1)"
    % (M1[3], M1[5], KFORM, M1[1] * M1[5], M1[1] * M1[4], (2.0 - 1.0) * (1 - M1[3])),
    KFORM < 1e-9 and M1[1] * M1[5] < 0 and M1[1] * M1[4] < 0,
)
check(
    "A3 [exact] THE TERM IS PRESENT ALREADY AT THE PARENT'S OWN COUPLING. K(1) = 1 EXACTLY at "
    "every mass (max departure %.1e), because H(1,1) = (1 + Phi) H0 is a pure rescaling of the "
    "whole Hamiltonian, so chi_vac[H(1,1)] = E^(0)_v = %+0.7f at m = 1 -- NONZERO. The ruler "
    "multiplies the coefficient by K(2)/K(1) = %.6f, adding %.1f per cent; it does not create the "
    "term, which is inherited, not introduced"
    % (max(abs(q[4] - 1.0) for q in ROWS), M1[1], M1[5], 100.0 * (M1[5] - 1.0)),
    max(abs(q[4] - 1.0) for q in ROWS) < 1e-9,
)
KMIN = min(min(a * (1 - q[3]) + q[3] for a in np.linspace(1.0, 2.0, 101)) for q in ROWS)
ROOTS = [-q[3] / (1 - q[3]) for q in ROWS]
check(
    "A4 [exact algebra + numerical] NO (kappa_r, nu_r) ON THE RULER SURFACE REMOVES chi_vac. "
    "K(alpha) = alpha (1 - w_m) + beta w_m vanishes only at alpha = -w_m/(1 - w_m) <= 0 (largest "
    "root over the masses tried: %+0.6f), while the ruler surface is alpha = 1 + kappa_r nu_r >= 1 "
    "for any positive rate exponent. Over alpha in [1, 2] the minimum of K is %.6f -- K is bounded "
    "BELOW by beta = 1 whenever alpha >= 1, so the dressing exponent cannot cancel it"
    % (max(ROOTS), KMIN),
    max(ROOTS) <= 0.0 and KMIN >= 1.0 - 1e-12,
)

CUBE = Box(2, 2, 3, per=(False, False, False))
NQ = CUBE.V
BASIS = [b for b in range(1 << NQ) if bin(b).count("1") == NQ // 2]
POSN = {b: i for i, b in enumerate(BASIS)}
DIM = len(BASIS)


def many_body_E0(m, Phi, ab):
    """The exact ground-state energy in the cube's half-filled 12-qubit sector."""
    Hs = CUBE.hmat(m, Phi, ab)
    A = np.zeros((DIM, DIM))
    for i, b in enumerate(BASIS):
        for v in range(NQ):
            if not (b >> v) & 1:
                continue
            A[i, i] += Hs[v, v]
            for w in range(NQ):
                if w == v or Hs[v, w] == 0.0 or ((b >> w) & 1):
                    continue
                b2 = (b ^ (1 << v)) | (1 << w)
                lo, hi = (v, w) if v < w else (w, v)
                mask = ((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1)
                s = -1.0 if (bin(b & mask).count("1") & 1) else 1.0
                A[POSN[b2], i] += s * Hs[w, v]
    return float(np.linalg.eigvalsh(A)[0])


MB = []
for ab, nm in ((ENERGY, "H(1,1)"), (FULL, "H(2,1)")):
    dmb = (many_body_E0(1.0, +GK_MB * CUBE.one, ab)
           - many_body_E0(1.0, -GK_MB * CUBE.one, ab)) / (2 * GK_MB)
    dsp = (CUBE.dens(1.0, +GK_MB * CUBE.one, ab)[1].sum()
           - CUBE.dens(1.0, -GK_MB * CUBE.one, ab)[1].sum()) / (2 * GK_MB)
    MB.append((nm, dmb, dsp, abs(dmb - dsp)))
check(
    "A5 [numerical, 1e-7] THE Phi-LINEAR VACUUM ENERGY IS A PROPERTY OF THE EXACT MANY-BODY GROUND "
    "STATE, NOT OF THE ONE-BODY BOOKKEEPING. In the 2x2x3 cube's 12-qubit space (dim 2^12 = 4096, "
    "half-filled sector %d) the exact ground-state energy's derivative in a uniform Phi is %+0.7f "
    "for H(1,1) and %+0.7f for H(2,1), matching sum_v dE_v/dPhi to %.1e and %.1e. Both NEGATIVE"
    % (DIM, MB[0][1], MB[1][1], MB[0][3], MB[1][3]),
    MB[0][3] < 1e-7 and MB[1][3] < 1e-7 and MB[0][1] < 0 and MB[1][1] < 0,
)


def chi_of_k(box, m, alpha, nvec):
    """The Phi-linear response at wavevector k: (chi, staggered part, off-projection)."""
    f = box.wave(nvec)
    dE = (box.dens(m, +GK * f, (alpha, 1.0))[1]
          - box.dens(m, -GK * f, (alpha, 1.0))[1]) / (2 * GK)
    chi = float(f @ dE) / float(f @ f)
    fs = box.sgn * f
    stag = float(fs @ dE) / float(fs @ fs)
    off = float(np.linalg.norm(dE - chi * f - stag * fs) / np.linalg.norm(dE))
    return chi, stag, off


def chi0_c(box, m, alpha, ns):
    """Fit chi(k) = chi_0 + c lambda_k over the declared wavevectors."""
    lam = np.array([2.0 * (1.0 - np.cos(2 * PI * n / box.L[0])) for n in ns])
    ch = np.array([chi_of_k(box, m, alpha, (n, 0, 0))[0] for n in ns])
    co = np.polyfit(lam, ch, 1)
    return float(co[1]), float(co[0]), float(np.max(np.abs(np.polyval(co, lam) - ch))), lam, ch


KTAB = [(n,) + chi_of_k(P8, 1.0, 2.0, (n, 0, 0)) for n in (0, 1, 2, 3, 4)]
LAM8 = np.array([6.0 - 2.0 * (np.cos(2 * PI * n / 8) + 2.0) for n in (0, 1, 2, 3, 4)])
print("   chi(k) on the 8x8x8 sea, m = 1, alpha = 2, k along x:")
print("   " + "  ".join("lam=%.3f chi=%+0.5f" % (LAM8[i], KTAB[i][1]) for i in range(5)))
CHI_0, C_GRAD, RES_SM, _, _ = chi0_c(P8, 1.0, 2.0, (0, 1, 2))
_, _, RES_BZ, _, _ = chi0_c(P8, 1.0, 2.0, (0, 1, 2, 3, 4))
STAG = max(abs(t[2]) for t in KTAB)
OFF = max(t[3] for t in KTAB)
check(
    "A6 [numerical, 1e-3] THE RESPONSE IS chi_0 Phi PLUS A LAPLACIAN, AND chi_0 SURVIVES k -> 0. "
    "On the 8x8x8 sea (m = 1, alpha = 2) chi(k) is linear in lambda_k = 6 - 2 sum cos k_a: the "
    "small-k fit chi(k) = %+0.7f %+0.7f lambda_k holds to %.1e (over the whole Brillouin zone, "
    "%.1e). In real space delta eps_v = chi_0 Phi_v + c (-Delta_lat Phi)_v with chi_0 = %+0.7f and "
    "c = %+0.7f. The staggered projection is <= %.1e and the off-projection residual <= %.1e, so "
    "the response is a pure scalar. The Laplacian piece renormalises the bridge operator; the "
    "CONSTANT piece is a genuine mass term"
    % (CHI_0, C_GRAD, RES_SM, RES_BZ, CHI_0, C_GRAD, STAG, OFF),
    RES_SM < 1e-3 and STAG < 1e-9 and OFF < 1e-9 and CHI_0 < 0.0,
)

CHI_0P, C_GRADP, _, _, _ = chi0_c(P8, 1.0, 1.0, (0, 1, 2))
M2_RULER = CHI_0 / (1.0 + C_GRAD)
M2_PARENT = CHI_0P / (1.0 + C_GRADP)
check(
    "A7 [exact sign chain + numerical] THE SIGN IS ANTI-SCREENING, NOT A YUKAWA SUPPRESSION. The "
    "bridge's phi is MINUS the Newtonian Phi that dresses H, so Delta_lat Phi = P0 [rho_matter + "
    "chi_0 Phi + c (-Delta_lat) Phi] gives (-Delta_lat + mass^2) Phi = -P0 rho_matter/(1 + c) with "
    "mass^2 = chi_0/(1 + c) and G -> G/(1 + c). Since E^(0)_v < 0 (A1) and K > 0 (A2), chi_0 < 0, "
    "hence mass^2 = %+0.6f for the ruler H(2,1) (G -> %.6f G) and %+0.6f for the parent H(1,1) "
    "(G -> %.6f G). BOTH NEGATIVE: near a mass the sea's negative energy is lifted toward zero, an "
    "energy EXCESS, which attracts more"
    % (M2_RULER, 1.0 / (1.0 + C_GRAD), M2_PARENT, 1.0 / (1.0 + C_GRADP)),
    M2_RULER < 0 and M2_PARENT < 0,
)


def lamk(L):
    """lambda(k) = 6 - 2 sum_a cos k_a on the L^3 torus, as a vector grid."""
    k = 2 * PI * np.fft.fftfreq(L, d=1.0)
    kx, ky, kz = np.meshgrid(k, k, k, indexing="ij")
    return 6.0 - 2.0 * (np.cos(kx) + np.cos(ky) + np.cos(kz))


def green(L, M2):
    """(1/V) sum_{k != 0} e^{ikx}/(lambda_k + M2): the P0-projected kernel, FFT on VECTORS."""
    den = lamk(L) + M2
    nz = np.ones(den.shape, dtype=bool)
    nz[0, 0, 0] = False
    inv = np.zeros_like(den)
    inv[nz] = 1.0 / den[nz]
    return np.real(np.fft.ifftn(inv)), int(np.sum(den[nz] < 0)), float(np.min(den[nz]))


NEG = []
for L in (16, 24, 32, 64):
    _, nneg, dmin = green(L, M2_RULER)
    NEG.append((L, nneg, dmin))
check(
    "A8 [numerical] AT THE LANDED NORMALISATION THE BRIDGE OPERATOR LOSES POSITIVITY, SO NO LENGTH "
    "EXISTS. With G = 1 and mass^2 = %+0.4f the operator -Delta_lat + mass^2 has %d, %d, %d and %d "
    "negative modes on L = 16, 24, 32, 64, its lowest eigenvalue %+0.4f at L = 64. The bridge "
    "note's own premise -- 'The nearest-neighbor graph Laplacian H=-Delta_lat is symmetric "
    "positive semidefinite, with kernel exactly the constant mode' -- does not hold once the sea's "
    "own response sits in the source, and there is no stable static solution to read a range off; "
    "the nominal 1/sqrt(|mass^2|) = %.3f is SUB-LATTICE"
    % (M2_RULER, NEG[0][1], NEG[1][1], NEG[2][1], NEG[3][1], NEG[3][2],
       1.0 / np.sqrt(abs(M2_RULER))),
    all(t[1] > 0 for t in NEG),
)
sys.stdout.flush()


# ============================= B (T2). THE SEA-REFERENCED SOURCE VANISHES IDENTICALLY

def dP_dPhi(box, m, alpha, f):
    """The sea projector's response to Phi = g f, a central difference in g."""
    return (box.sea(box.hmat(m, +GK * f, (alpha, 1.0)))
            - box.sea(box.hmat(m, -GK * f, (alpha, 1.0)))) / (2 * GK)


H8 = P8.hmat(1.0, P8.zero, FULL)
P8_SEA = P8.sea(H8)
TRD = []
for f in (P8.one, P8.wave((1, 0, 0)), P8.wave((2, 1, 0))):
    dP = dP_dPhi(P8, 1.0, 2.0, f)
    sc = float(np.linalg.norm(H8) * np.linalg.norm(dP))        # the Frobenius bound on |tr(H dP)|
    dp = abs(float(np.einsum("vj,jv->", H8, dP)))
    TRD.append((dp, sc, dp / sc))
check(
    "B1 [numerical, 1e-9 relative] THE k = 0 RESPONSE OF ANY SEA-REFERENCED SOURCE VANISHES, AND "
    "THE REASON IS EXACT. For a source counted from the sea, sum_v eps_v = tr(H (P' - P_ref)), and "
    "differentiating in Phi about the vacuum leaves tr(H dP/dPhi), ZERO for a spectral projector: "
    "the first-order energy variation is carried entirely by dH (Hellmann-Feynman). On the 8x8x8 "
    "sea |tr(H dP/dPhi)| is %.1e, %.1e, %.1e for a uniform field and two plane waves against the "
    "Frobenius bound %.0f, %.0f, %.0f the trace could have reached -- relative %.1e, %.1e, %.1e, "
    "the central difference's own floor. chi(0) is the mean of the response, so it vanishes for "
    "the fixed and the field-dressed reference alike"
    % (TRD[0][0], TRD[1][0], TRD[2][0], TRD[0][1], TRD[1][1], TRD[2][1],
       TRD[0][2], TRD[1][2], TRD[2][2]),
    max(t[2] for t in TRD) < 1e-9,
)

P12 = Box(12, 12, 12, per=(True, True, True))
P12_REF = P12.sea(P12.hmat(1.0, P12.zero, FULL))
P8_REF = P8.sea(P8.hmat(1.0, P8.zero, FULL))


def vac_chi(box, ref0, nvec, ref):
    """chi(k) of the VACUUM source (no matter above the sea) for the named reference."""
    f = box.wave(nvec)
    out = []
    for s in (+1.0, -1.0):
        H = box.hmat(1.0, s * GK * f, FULL)
        P = box.sea(H)
        R = {"half": P - 0.5 * np.eye(box.V), "fixed": P - ref0, "field": P - P}[ref]
        out.append(np.einsum("vj,jv->v", H, R))
    dE = (out[0] - out[1]) / (2 * GK)
    return float(f @ dE) / float(f @ f), float(np.max(np.abs(dE)))


V12 = [(6.0 - 2.0 * (np.cos(2 * PI * n / 12) + 2.0), vac_chi(P12, P12_REF, (n, 0, 0), "fixed")[0])
       for n in (0, 1, 2)]
V8 = [(6.0 - 2.0 * (np.cos(2 * PI * n / 8) + 2.0), vac_chi(P8, P8_REF, (n, 0, 0), "fixed")[0])
      for n in (0, 1, 2, 3)]
CHI0_FIX = float(V12[0][1])
C_FIX = float(np.polyfit([r[0] for r in V12[1:]], [r[1] for r in V12[1:]], 1)[0])
BND_FIX = max(abs(r[1]) for r in V8)
print("   fixed-reference residual (12^3): " + "  ".join(
    "lam=%.4f chi=%+0.3e" % (r[0], r[1]) for r in V12))
check(
    "B2 [numerical, 1e-9] THE FIXED SEA REFERENCE LEAVES NO MASS AT ALL, ONLY A RENORMALISATION OF "
    "THE COUPLING. Counting the sea's energy from the Phi = 0 sea instead of from half filling "
    "leaves chi(k = 0) = %+0.3e on the 12^3 sea -- zero to numerical precision -- against %+0.4f "
    "from half filling, a suppression of %.0e. The residual is O(lambda_k): chi/lambda_k = %+0.5f "
    "and %+0.5f at the two smallest nonzero k, a pure Laplacian piece, so it shifts the coupling by "
    "G -> G/(1 %+0.5f) = %.5f G and supplies NO mass; |chi| <= %.4f across the whole zone. The mass "
    "term is an artefact of the reference, not a property of the vacuum"
    % (CHI0_FIX, CHI_0, abs(CHI_0 / CHI0_FIX), V12[1][1] / V12[1][0], V12[2][1] / V12[2][0],
       C_FIX, 1.0 / (1.0 + C_FIX), BND_FIX),
    abs(CHI0_FIX) < 1e-9 and abs(1.0 / (1.0 + C_FIX) - 1.0) < 0.02,
)
FIELD = [vac_chi(P8, P8_REF, (n, 0, 0), "field") for n in (0, 1, 2, 3)]
check(
    "B3 [exact] THE FIELD-DRESSED REFERENCE -- THE LANDED DEFINITION READ LITERALLY -- LEAVES THE "
    "ZERO FUNCTION. The landed source is eps_v = sum_j M_vj (P' - P)_vj, the excess above the sea's "
    "own projector. With no matter above the sea P' = P, so eps_v is identically zero at every "
    "site, every k and every Phi: max |d eps_v/dPhi| = %.1e over the four k tried, and max |chi| = "
    "%.1e. The landed source carries NO vacuum response by construction, not by cancellation"
    % (max(t[1] for t in FIELD), max(abs(t[0]) for t in FIELD)),
    max(t[1] for t in FIELD) == 0.0,
)
sys.stdout.flush()


# ================================================================ C (T3). THREE ROUTES

LC = 16
xg, yg, zg = np.meshgrid(*[np.arange(LC)] * 3, indexing="ij")
SRC = (np.cos(2 * PI * xg / LC) * np.cos(4 * PI * yg / LC)
       + 0.5 * np.sin(2 * PI * zg / LC) * np.cos(2 * PI * xg / LC))
SRC[0, 0, 0] += 1.0
SRC[3, 5, 7] -= 0.5                      # a declared, non-random, inhomogeneous test source
GB16, _, _ = green(LC, 0.0)
PHI_C = np.real(np.fft.ifftn(np.fft.fftn(SRC - SRC.mean()) * np.fft.fftn(GB16)))
RESP = CHI_0 * PHI_C
check(
    "C1 [exact] ROUTE (a): THE CONSTANT-MODE PROJECTOR ACTS AS THE IDENTITY ON THIS TERM. P0 "
    "removes the CONSTANT mode, which the bridge names the total-mass/background sector. Any "
    "solution phi = G0 P0 rho already has zero mean (%.1e on the declared L = 16 source), so "
    "chi_0 Phi has zero mean too and P0 (chi_0 Phi) = chi_0 Phi exactly: max difference %.1e. The "
    "vacuum's response is a local multiple of Phi, living in the very zero-mean subspace P0 "
    "projects ONTO, so the landed projector leaves it untouched"
    % (abs(float(PHI_C.mean())), float(np.max(np.abs(RESP - (RESP - RESP.mean()))))),
    abs(float(PHI_C.mean())) < 1e-12
    and float(np.max(np.abs(RESP - (RESP - RESP.mean())))) < 1e-14,
)
RR = (1.0, 3.0, 10.0, 1e3, 1e6)
LAMS = [3.0 / R ** 2 for R in RR]
check(
    "C2 [exact arithmetic + statement] ROUTE (b): THE COUNTERTERM IS THE LANDED DEFINITION, AND ITS "
    "PRICE IS A DECLARED INTERFACE. A source identically zero in vacuum at every k, k = 0 included, "
    "contributes nothing to phi = G0 P0 rho: the vacuum's own energy does not gravitate, "
    "Lambda_vac = 0. The landed identity is Lambda_vac = lambda_1(S^3_R) = 3/R^2 for every R > 0, "
    "STRICTLY POSITIVE at every finite radius (%s at R = 1, 3, 10, 1e3, 1e6) and reaching zero only "
    "as R -> infinity. The tension is named, not resolved. Checked by reading, not by this runner: "
    "none of the 26 docs/GRAVITY*, docs/RESTRICTED_STRONG_FIELD* or docs/BACKREACTION* files on "
    "main contains the word 'vacuum'"
    % "/".join("%.3g" % x for x in LAMS),
    all(x > 0.0 for x in LAMS) and LAMS[-1] < 1e-10,
)
FP = []
for q in ROWS:
    wm = q[3]
    kap = 2.0 - wm                        # kappa_r* = 1/nu_r* at the F1 fixed point alpha* = 2
    FP.append((q[0], wm, 1.0 / kap, kap, q[1], q[1] * kap, q[1] * q[5]))
ERR_FP = max(abs(t[5] - t[6]) for t in FP)
check(
    "C3 [numerical, 1e-9] ROUTE (c): THE F1 FIXED POINT DOES NOT ABSORB THE TERM -- IT FIXES ITS "
    "VALUE. F1's loop closes in the RATE (kappa_r = K(alpha), alpha = 1 + nu_r kappa_r); the "
    "vacuum's response closes in the FIELD EQUATION. They are one susceptibility read in two "
    "directions. At the fixed point nu_r* = 1/(2 - w_m) and kappa_r* = 2 - w_m, so chi_vac = "
    "E^(0) kappa_r*, which reproduces the directly computed chi_vac[H(2,1)] to %.1e at every mass "
    "(m = 0: %+0.7f; m = 6: %+0.7f). Since kappa_r* = 2 - w_m lies in [1, 2], chi_vac is bounded "
    "away from zero by |E^(0)|: anti-screening is what alpha* = 2 COSTS, not what makes it "
    "consistent" % (ERR_FP, FP[0][5], FP[-1][5]),
    ERR_FP < 1e-9,
)
sys.stdout.flush()


# ======================================================= D (T4). THE TWO-BODY LAW

print("   Lb = 64, unsubtracted: D  4piD G_bare  ruler/bare  parent/bare")
FLIPS, ROWS_D1 = {}, []
for Lb in LANDED_LB:
    gb, _, _ = green(Lb, 0.0)
    gr, _, _ = green(Lb, M2_RULER)
    gp, _, _ = green(Lb, M2_PARENT)
    ds = tuple(d for d in sorted(set(tuple(range(1, 9)) + LANDED_D)) if d < Lb // 2)
    rr = [(d, 4 * PI * d * gb[d, 0, 0], gr[d, 0, 0] / (1 + C_GRAD) / gb[d, 0, 0],
           gp[d, 0, 0] / (1 + C_GRADP) / gb[d, 0, 0]) for d in ds]
    ROWS_D1.append((Lb, rr))
    FLIPS[Lb] = [d for d, _, a, _ in rr if a < 0]
    if Lb == 64:
        for t in rr:
            if t[0] <= 8 or t[0] in LANDED_D:
                print("     %2d  %7.4f  %+9.3f  %+9.3f" % t)
MAG = {Lb: max(abs(a) for d, _, a, _ in rr if d <= 8) for Lb, rr in ROWS_D1}
MAGL = max(abs(a) for _, rr in ROWS_D1 for d, _, a, _ in rr if d in LANDED_D)
MAG8 = MAG[64]
GB64 = green(64, 0.0)[0]
check(
    "D1 [numerical] ON THE HALF-FILLING REFERENCE THE LANDED E1 E2 G(D) IS DESTROYED, NOT "
    "CORRECTED. On the landed boxes Lb = 32, 64 the bare kernel gives 4 pi D G(D) = %.4f, %.4f, "
    "%.4f at D = 1, 8, 16 (Lb = 64). With the vacuum's response in the source the kernel CHANGES "
    "SIGN at D = %s on Lb = 64 and D = %s on Lb = 32, and departs from the bare kernel by factors "
    "up to %.1f over D = 1..8 on Lb = 64 (%.1f on Lb = 32) and %.0f at the landed D = 3, 4, 6, 8, "
    "10, 16. A per-cent-level law and a sign-indefinite order-ten kernel are incompatible, and the "
    "nominal length %.3f is smaller than every torus tried: this sits at the lattice scale"
    % (4 * PI * GB64[1, 0, 0], 4 * PI * 8 * GB64[8, 0, 0], 4 * PI * 16 * GB64[16, 0, 0],
       ", ".join(str(d) for d in FLIPS[64]), ", ".join(str(d) for d in FLIPS[32]),
       MAG8, MAG[32], MAGL, 1.0 / np.sqrt(abs(M2_RULER))),
    len(FLIPS[64]) >= 1 and MAG8 > 5.0,
)

LAM_S = np.array([r[0] for r in V8])
CHI_S = np.array([0.0] + [r[1] for r in V8[1:]])
SLOPE_TAIL = CHI_S[-1] / LAM_S[-1]


def chi_fixed_of_lam(lm):
    """The computed sea-referenced residual chi_fixed(lambda), linear beyond the last point."""
    out = np.interp(lm, LAM_S, CHI_S)
    tail = lm > LAM_S[-1]
    out[tail] = SLOPE_TAIL * lm[tail]
    return out


ROWS_D2 = []
for LL in (16, 24, 64):
    den = lamk(LL) - chi_fixed_of_lam(lamk(LL))
    nz = np.ones(den.shape, dtype=bool)
    nz[0, 0, 0] = False
    inv = np.zeros_like(den)
    inv[nz] = 1.0 / den[nz]
    gs = np.real(np.fft.ifftn(inv))
    gb, _, _ = green(LL, 0.0)
    ROWS_D2.append((LL, [gs[d, 0, 0] / gb[d, 0, 0] for d in range(1, 9)],
                    [gs[d, 0, 0] / gb[d, 0, 0] for d in LANDED_D if d < LL // 2]))
FLAT = np.median([r for _, rr, _ in ROWS_D2 for r in rr])
MAXDEV = max(abs(r - 1.0) for _, rr, ll in ROWS_D2 for r in rr + ll)
check(
    "D2 [numerical] ON THE SEA REFERENCE THE TWO-BODY LAW SURVIVES AS A FLAT SUB-PER-CENT "
    "RESCALING OF THE COUPLING. Solving the bridge with the computed residual chi_fixed(k) in "
    "place, G_dressed(D)/G_bare(D) is %.6f in the median and departs from 1 by at most %.4f over "
    "D = 1..8 and the landed D = 3, 4, 6, 8, 10, 16 on L = 16, 24 and 64 -- a flat %.2f per cent "
    "rescaling with essentially no change of shape, because chi_fixed(0) = 0 exactly and there is "
    "no length. The landed rigid-copy ratios 0.9462 / 0.9736 / 0.9938 / 0.9986 at D = 3, 4, 8, 16 "
    "are untouched" % (FLAT, MAXDEV, 100.0 * (1.0 - FLAT)),
    MAXDEV < 0.02 and abs(1.0 - FLAT) < 0.01,
)
TOL = []
for M2a in (2.0217, 1.0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-6):
    gb, _, _ = green(64, 0.0)
    gs, _, _ = green(64, +M2a)            # the Yukawa (suppressing) sign, for calibration
    TOL.append((M2a, 1.0 / np.sqrt(M2a),
                max(abs(gs[d, 0, 0] / gb[d, 0, 0] - 1.0) for d in range(1, 9))))
NEED = [t for t in TOL if t[2] < 0.01][0]
check(
    "D3 [numerical] THE TOLERANCE. Taking the Yukawa (suppressing) sign for calibration, a mass "
    "term changes the landed kernel at D = 1..8 by less than 1 per cent only once |mass^2| <= "
    "%.0e, i.e. a length 1/sqrt(|mass^2|) >= %.0f lattice spacings (the row above it, |mass^2| = "
    "%.0e, already costs %.1f per cent). The half-filling value is |mass^2| = %.4f, length %.3f: "
    "short by a factor %.0e in mass^2 and %.0f in length"
    % (NEED[0], NEED[1], TOL[TOL.index(NEED) - 1][0], 100 * TOL[TOL.index(NEED) - 1][2],
       abs(M2_RULER), 1.0 / np.sqrt(abs(M2_RULER)), abs(M2_RULER) / NEED[0],
       NEED[1] * np.sqrt(abs(M2_RULER))),
    NEED[0] <= 1e-4 and NEED[1] >= 100.0,
)
sys.stdout.flush()


# ============================================ E (T5). TWO CORRECTIONS TO THE PREMISES

CTRL = [(Lb, 4 * PI * (Lb // 4) * green(Lb, 0.0)[0][Lb // 4, 0, 0]) for Lb in LANDED_LB]
NEAR = [(d, 4 * PI * d * GB64[d, 0, 0]) for d in (1, 2, 3, 4)]
check(
    "E1 [exact + numerical, 5e-4] THE BRIDGE'S NORMALISATION CARRIES NO COUPLING CONSTANT. The "
    "landed bridge is H = -Delta_lat, lambda(k) = 6 - 2 sum_a cos k_a -- the UNNORMALISED graph "
    "Laplacian, no 1/(2d) -- with G0 = H^{-1} literally. So G = 1 in lattice units, "
    "G(r) -> 1/(4 pi |r|) and G_Newton = 1/(4 pi) per spacing. The landed point control "
    "4 pi r G at r = Lb/4 is reproduced, %.4f and %.4f at Lb = 32, 64 against their quoted 0.3307 "
    "and 0.3275; near the source 4 pi D G(D) = %s at D = 1, 2, 3, 4. Every mass^2 above is in those "
    "units and every length in spacings"
    % (CTRL[0][1], CTRL[1][1], "/".join("%.4f" % v for _, v in NEAR)),
    abs(CTRL[0][1] - 0.3307) < 5e-4 and abs(CTRL[1][1] - 0.3275) < 5e-4
    and abs(NEAR[0][1] - 1.0) < 0.1,
)
CROWS = []
for m in (0.0, 1.0, 2.0):
    c0, cg, _, _, _ = chi0_c(P8, m, 2.0, (0, 1, 2))
    _, Ev, _, Em = P8.dens(m, P8.zero, ENERGY)
    CROWS.append((m, c0, cg, float((Em / Ev).mean())))
check(
    "E2 [numerical, reported] THE GRADIENT COEFFICIENT c IS NOT THE VACUUM MASS FRACTION w_m. At "
    "m = 0, w_m = %.6f EXACTLY but c = %+0.7f; at m = 1, c = %+0.7f against w_m = %.6f; at m = 2, "
    "c = %+0.7f against w_m = %.6f, where the two have separated by %.2f. The near-match at m = 1 "
    "is a coincidence and is REPORTED, not claimed. What the bridge needs is only that c is O(0.2) "
    "and finite, so the Laplacian piece shifts G by O(20 per cent) and cannot cancel chi_0"
    % (CROWS[0][3], CROWS[0][2], CROWS[1][2], CROWS[1][3], CROWS[2][2], CROWS[2][3],
       abs(CROWS[2][2] - CROWS[2][3])),
    CROWS[0][3] < 1e-12 and CROWS[0][2] > 0.1 and abs(CROWS[2][2] - CROWS[2][3]) > 0.1,
)

print(
    "SUMMARY: counted from half filling the sea's Phi-linear energy density is NEGATIVE and its "
    "response positive, so the induced term ANTI-SCREENS -- the bridge operator loses positivity "
    "and no length exists; it is present already at the parent's coupling and no ruler exponent "
    "removes it. Counted from the sea, as the landed matter notes define their source, the vacuum "
    "response vanishes identically because the sea is a spectral projector, leaving a flat "
    "sub-per-cent rescaling of the coupling and no mass. The price is removable and the landed "
    "definition has already removed it, at the declared cost Lambda_vac = 0."
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
