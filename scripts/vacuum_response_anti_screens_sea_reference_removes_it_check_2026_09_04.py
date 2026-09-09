#!/usr/bin/env python3
"""Finite supplied gravity model, corrected after independent review.

No physical carrier, source law, clock, metric, or cosmological conclusion is
derived. See the source-bound companion note for all assumptions and scopes.
Central derivatives have O(g**2) error for smooth dependence; finite packet
Richardson values assume an unproved width expansion. Deterministic inputs do
not guarantee bitwise reproducibility across platforms. Historical originals
are archived outside active discovery.
"""
from __future__ import annotations

import sys

from pathlib import Path
import hashlib

# Exact note body supplies all model assumptions; every science helper is inline.
AUDIT_INPUT_PATHS = ('docs/THE_VACUUM_RESPONSE_UNDER_THE_RATE_RULER_ANTI_SCREENS_AND_THE_SEA_REFERENCED_SOURCE_REMOVES_IT_BOUNDED_THEOREM_NOTE_2026-09-04.md',)
EXPECTED_INPUT_SHA256 = {'docs/THE_VACUUM_RESPONSE_UNDER_THE_RATE_RULER_ANTI_SCREENS_AND_THE_SEA_REFERENCED_SOURCE_REMOVES_IT_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'ca9ec41e7df7a0f286fce92e6ddf6999742a827df1d066e5585be8f7c06bbf34'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    for rel, expected in EXPECTED_INPUT_SHA256.items():
        actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"scientific input changed: {rel}")
    print("INPUT_BINDING: exact companion note verified; finite supplied definitions only")

verify_inputs()


import numpy as np

AUDIT_TIMEOUT_SEC = 150

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
LANDED_D = (3, 4, 6, 8, 10, 16)    # the distances the supplied notes tabulate
LANDED_LB = (32, 64)               # the supplied notes' response boxes


# Finite calculation group

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
        """The half-filled sea: negative levels occupied, zero modes half occupied (a covariance there)."""
        w, U = np.linalg.eigh(H)
        occ = (w < -1e-12).astype(float) + 0.5 * (np.abs(w) <= 1e-12)
        return (U * occ) @ U.T

    def dens(self, m, Phi, ab):
        """(occupation odds, E_v, hop part, mass part), E_v counted from HALF FILLING."""
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


# Finite calculation group

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
    'A1' + " " + f'Periodic4^3, six declared masses: E0<0 at every site; m1 E0={M1[1]:.8f}, site spread={M1[2]:.3e}.',
    all(q[1] < 0 for q in ROWS) and max(q[2] for q in ROWS) < 1e-13,
)
KFORM = max(abs(q[5] - (2.0 * (1 - q[3]) + q[3])) for q in ROWS)
check(
    'A2' + " " + f'Uniform K identity residual {KFORM:.3e}; m1 w_m={M1[3]:.6f}, K2={M1[5]:.6f}, half-reference chi2={M1[1]*M1[5]:.7f}, chi1={M1[1]*M1[4]:.7f}.',
    KFORM < 1e-9 and M1[1] * M1[5] < 0 and M1[1] * M1[4] < 0,
)
check(
    'A3' + " " + f'Uniform positive H(1,1) rescaling: max K1 departure={max(abs(q[4]-1) for q in ROWS):.3e}; response multiplication={M1[5]:.6f}.',
    max(abs(q[4] - 1.0) for q in ROWS) < 1e-9,
)
KMIN = min(min(a * (1 - q[3]) + q[3] for a in np.linspace(1.0, 2.0, 101)) for q in ROWS)
ROOTS = [-q[3] / (1 - q[3]) for q in ROWS]
check(
    'A4' + " " + f'Uniform conditional algebra K>=1 for alpha>=1 and 0<=w_m<=1; finite grid min={KMIN:.6f}, roots={ROOTS} (formula needs w_m!=1).',
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
    'A5' + " " + f'Open2x2x3 half-filled Fock sector{DIM}: independent uniform energy derivatives (name,manybody,onebody,error)={MB}.',
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
    'A6' + " " + f'8^3 AXIAL sample fits: first3 chi0={CHI_0:.7f}, c={C_GRAD:.7f}, maxres={RES_SM:.3e}; all5 maxres={RES_BZ:.3e}; sampled staggered/off residual={STAG:.3e}/{OFF:.3e}. Neither full-zone isotropy nor exact Laplacian established.',
    RES_SM < 1e-3 and STAG < 1e-9 and OFF < 1e-9 and CHI_0 < 0.0,
)

CHI_0P, C_GRADP, _, _, _ = chi0_c(P8, 1.0, 1.0, (0, 1, 2))
M2_RULER = CHI_0 / (1.0 + C_GRAD)
M2_PARENT = CHI_0P / (1.0 + C_GRADP)
check(
    'A7' + " " + f'SURROGATE chi=chi0+c*lambda: (L+chi)Phi=-P0rho gives m2={M2_RULER:.6f},{M2_PARENT:.6f}; normalization factors={1/(1+C_GRAD):.6f},{1/(1+C_GRADP):.6f}. Negative fitted mass-squared, not a true-kernel conclusion.',
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
    'A8' + " " + f'SURROGATE negative eigenvalue counts (L,count,min)={NEG}; 1/sqrt(abs(m2))={1/np.sqrt(abs(M2_RULER)):.6f}. Loss of positivity is not noninvertibility or dynamical runaway; no positive real Yukawa decay length.',
    all(t[1] > 0 for t in NEG),
)
sys.stdout.flush()


# Finite calculation group

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
    'B1' + " " + f'Gapped constant-rank spectral P(H): tr(H*dP)=0 is a TOTAL-trace identity. Actual m1 uniform/two-wave controls (trace,Frobenius bound,relative)={TRD}; not a local zero theorem.',
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
    'B2' + " " + f'Fixed P(0): uniform12^3 chi={CHI0_FIX:.3e}; axial sample ratios={[r[1]/r[0] for r in V12[1:]]}; two-point slope={C_FIX:.7f}, 1/(1+slope)={1/(1+C_FIX):.7f}; max of four8^3 AXIAL samples={BND_FIX:.7f}. No zone bound or pure Laplacian claim.',
    abs(CHI0_FIX) < 1e-9 and abs(1.0 / (1.0 + C_FIX) - 1.0) < 0.02,
)
FIELD = [vac_chi(P8, P8_REF, (n, 0, 0), "field") for n in (0, 1, 2, 3)]
check(
    'B3' + " " + f'Field-dressed reference gives P(Phi)-P(Phi)=0 by definition; four axial controls={FIELD}. Fixed reference is different.',
    max(t[1] for t in FIELD) == 0.0,
)
# Actual same-lambda response, not an interpolation: an axial sample does not
# determine the off-axis susceptibility even on this very same8^3 fixture.
SAME_LAMBDA = []
for wave_index in ((4,0,0), (2,2,0)):
    lambda_value = float(6-2*np.cos(2*PI*np.array(wave_index)/8).sum())
    SAME_LAMBDA.append((wave_index, lambda_value,
        vac_chi(P8, P8_REF, wave_index, "fixed")[0],
        vac_chi(P8, P8_REF, wave_index, "half")[0]))
check(f"B4 same-lambda4 counterexample (index,lambda,fixed,half)={SAME_LAMBDA}",
      abs(SAME_LAMBDA[0][1]-SAME_LAMBDA[1][1]) < 1e-12
      and abs(SAME_LAMBDA[1][2]-SAME_LAMBDA[0][2]) > 0.02
      and abs(SAME_LAMBDA[1][2]) > 0.01)

sys.stdout.flush()


# Finite calculation group

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
    'C1' + " " + f'P0 preserves constant coefficient times zero-mean field: fieldmean={PHI_C.mean():.3e}, projection residual={np.max(np.abs(RESP-(RESP-RESP.mean()))):.3e}. P0 also kills arbitrary additive constants in rho.',
    abs(float(PHI_C.mean())) < 1e-12
    and float(np.max(np.abs(RESP - (RESP - RESP.mean())))) < 1e-14,
)
RR = (1.0, 3.0, 10.0, 1e3, 1e6)
LAMS = [3.0 / R ** 2 for R in RR]
check(
    'C2' + " " + f'Separate arithmetic 3/R**2 at R={RR}: {LAMS}, positive for finite R>0. P0 source convention implies neither Lambda=0 nor R=infinity.',
    all(x > 0.0 for x in LAMS) and LAMS[-1] < 1e-10,
)
FP = []
for q in ROWS:
    wm = q[3]
    kap = 2.0 - wm                        # kappa_r* = 1/nu_r* at the F1 fixed point alpha* = 2
    FP.append((q[0], wm, 1.0 / kap, kap, q[1], q[1] * kap, q[1] * q[5]))
ERR_FP = max(abs(t[5] - t[6]) for t in FP)
check(
    'C3' + " " + f'Uniform scalar identity chi=E0*(2-w_m), error={ERR_FP:.3e}; rows(m,wm,nu,kappa,E0,pred,computed)={FP}; no spatial feedback solution.',
    ERR_FP < 1e-9,
)
sys.stdout.flush()


# Finite calculation group

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
    'D1' + " " + f'FITTED NEGATIVE-MASS SURROGATE FFT kernels: flips={FLIPS}; maxmagnitudes={MAG}, selected-distance max={MAGL:.6f}. Near poles amplify fit error; not destruction of a physical two-body law.',
    len(FLIPS[64]) >= 1 and MAG8 > 5.0,
)

LAM_S = np.array([r[0] for r in V8])
CHI_S = np.array([0.0] + [r[1] for r in V8[1:]])
SLOPE_TAIL = CHI_S[-1] / LAM_S[-1]


def chi_fixed_of_lam(lm):
    """Declared axial-interpolant surrogate, tail proportional to lambda; not the full kernel."""
    out = np.interp(lm, LAM_S, CHI_S)
    tail = lm > LAM_S[-1]
    out[tail] = SLOPE_TAIL * lm[tail]
    return out


ROWS_D2 = []
for LL in (16, 24, 64):
    den = lamk(LL) + chi_fixed_of_lam(lamk(LL))
    nz = np.ones(den.shape, dtype=bool)
    nz[0, 0, 0] = False
    inv = np.zeros_like(den)
    inv[nz] = 1.0 / den[nz]
    # Verify the declared Fourier equation, including its plus sign.
    solver_residual = float(np.max(abs((lamk(LL)+chi_fixed_of_lam(lamk(LL)))[nz]*inv[nz]-1)))
    wrong_sign_residual = float(np.max(abs((lamk(LL)-chi_fixed_of_lam(lamk(LL)))[nz]*inv[nz]-1)))
    check(f"D2a L{LL} plus-equation residual={solver_residual:.3e}, minus residual={wrong_sign_residual:.6f}",
          solver_residual < 1e-12 and wrong_sign_residual > 1e-3)
    gs = np.real(np.fft.ifftn(inv))
    gb, _, _ = green(LL, 0.0)
    ROWS_D2.append((LL, [gs[d, 0, 0] / gb[d, 0, 0] for d in range(1, 9)],
                    [gs[d, 0, 0] / gb[d, 0, 0] for d in LANDED_D if d < LL // 2]))
FLAT = np.median([r for _, rr, _ in ROWS_D2 for r in rr])
MAXDEV = max(abs(r - 1.0) for _, rr, ll in ROWS_D2 for r in rr + ll)
check(
    'D2' + " " + f'AXIAL-INTERPOLANT SURROGATE uses lambda+chi_fixed: median={FLAT:.7f}, maxabsdeparture={MAXDEV:.7f}; rows={ROWS_D2}. First list includes L16 antipode d8. No full susceptibility or unchanged rigid-copy ratios established.',
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
    'D3' + " " + f'Selected POSITIVE mass-squared calibration on L64 d1..8: rows(m2,length,maxdev)={TOL}; first sampled <1percent row={NEED}. Not a necessary threshold, infinite-volume bound, or negative-mass calibration.',
    NEED[0] <= 1e-4 and NEED[1] >= 100.0,
)
sys.stdout.flush()


# Finite calculation group

CTRL = [(Lb, 4 * PI * (Lb // 4) * green(Lb, 0.0)[0][Lb // 4, 0, 0]) for Lb in LANDED_LB]
NEAR = [(d, 4 * PI * d * GB64[d, 0, 0]) for d in (1, 2, 3, 4)]
check(
    'E1' + " " + f'Defined unit-normalized inverse graph Laplacian: controls={CTRL}, near-source={NEAR}. Continuum asymptotic coefficient1/(4pi) in these units is not physical G_Newton.',
    abs(CTRL[0][1] - 0.3307) < 5e-4 and abs(CTRL[1][1] - 0.3275) < 5e-4
    and abs(NEAR[0][1] - 1.0) < 0.1,
)
CROWS = []
for m in (0.0, 1.0, 2.0):
    c0, cg, _, _, _ = chi0_c(P8, m, 2.0, (0, 1, 2))
    _, Ev, _, Em = P8.dens(m, P8.zero, ENERGY)
    CROWS.append((m, c0, cg, float((Em / Ev).mean())))
check(
    'E2' + " " + f'AXIAL fitted coefficient differs from mass fraction: (m,chi0,c,wm)={CROWS}; no full-zone derivative expansion inferred.',
    CROWS[0][3] < 1e-12 and CROWS[0][2] > 0.1 and abs(CROWS[2][2] - CROWS[2][3]) > 0.1,
)

print("SUMMARY: finite conditional identities and declared-fixture calculations only; physical source, carrier, metric and cosmology remain open.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
