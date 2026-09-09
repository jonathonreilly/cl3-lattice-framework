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
AUDIT_INPUT_PATHS = ('docs/A_FORMATION_RATE_RULER_EVADES_THE_SEAS_SUBLATTICE_CANCELLATION_AND_THE_BRIDGES_CONSTANT_MODE_FIXES_KAPPA_R_EQUALS_ONE_BOUNDED_THEOREM_NOTE_2026-09-04.md',)
EXPECTED_INPUT_SHA256 = {'docs/A_FORMATION_RATE_RULER_EVADES_THE_SEAS_SUBLATTICE_CANCELLATION_AND_THE_BRIDGES_CONSTANT_MODE_FIXES_KAPPA_R_EQUALS_ONE_BOUNDED_THEOREM_NOTE_2026-09-04.md': '4576cd5d09f50e4d194ec9ae625ed4cd0df812c204da5cf5aa2e77ef9c4ea514'}

def verify_inputs():
    root = Path(__file__).resolve().parents[1]
    for rel, expected in EXPECTED_INPUT_SHA256.items():
        actual = hashlib.sha256((root / rel).read_bytes()).hexdigest()
        if actual != expected:
            raise RuntimeError(f"scientific input changed: {rel}")
    print("INPUT_BINDING: exact companion note verified; finite supplied definitions only")

verify_inputs()


import numpy as np
import scipy.sparse as sp
import sympy as smp
from scipy.special import jv

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


def fmt(xs, nd=3):
    return "/".join(("%." + str(nd) + "f") % x for x in xs)


PI = np.pi
G_FIELD = 1.0e-3                 # field knob for a finite central approximation to d/dg at zero
GS_SMALL = 2.5e-4                # the reduced field of the O(Phi^2) scaling row
FULL, ENERGY = (2.0, 1.0), (1.0, 1.0)
SIG = (32.0, 44.0)               # the two declared packet widths
MASSES_K = (0.0, 0.3, 0.9, 2.0, 6.0)
ALPHAS_K = (1.0, 1.5, 2.0, 3.0)


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
        self.xs = ix.ravel().astype(float)
        self.zs = iz.ravel().astype(float)
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
        self.bi = np.arange(0, len(self.r), 2)          # one entry per undirected bond

    def hmat(self, m, Phi, ab):
        alpha, beta = ab
        H = np.zeros((self.V, self.V))
        np.add.at(H, (self.r, self.c),
                  self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c])))
        return H + np.diag(m * self.sgn * (1.0 + beta * Phi))

    def sea(self, H):
        """One-body density matrix of the half-filled sea (zero modes at weight 1/2)."""
        w, U = np.linalg.eigh(H)
        occ = (w < -1e-12).astype(float) + 0.5 * (np.abs(w) <= 1e-12)
        return (U * occ) @ U.T

    def dens(self, m, Phi, ab):
        """rho_rec(v) = <n_v>; E_v the half-filling-referenced local energy density; its split."""
        H = self.hmat(m, Phi, ab)
        R = self.sea(H)
        occ = np.diag(R).copy()
        Rt = R - 0.5 * np.eye(self.V)                    # normal-order about half filling
        Ev = np.einsum("vj,jv->v", H, Rt)
        Emass = np.diag(H) * np.diag(Rt)
        return occ, Ev, Ev - Emass, Emass


class Slab:
    """The sparse, matrix-free 192 x 16 x 4 coarse slab of the parent's machinery."""

    def __init__(self, Lx, Ly, Lz):
        self.Lx, self.Ly, self.Lz = Lx, Ly, Lz
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(np.arange(Lx), np.arange(Ly), np.arange(Lz), indexing="ij")
        self.xs, self.ys, self.zs = (a.ravel().astype(float) for a in (ix, iy, iz))
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()
        r, c, val, dx = [], [], [], []

        def idx(a, b, k):
            return (a * Ly + b) * Lz + k

        for a in range(Lx):
            for b in range(Ly):
                for k in range(Lz):
                    i, v = idx(a, b, k), (a, b, k)
                    for ax in range(3):
                        w = [a, b, k]
                        w[ax] += 1
                        if ax == 0:
                            if w[0] >= Lx:
                                continue
                        else:
                            w[ax] %= (Ly if ax == 1 else Lz)
                        j = idx(*w)
                        s = float(eta_ks(v, ax))
                        r += [i, j]
                        c += [j, i]
                        val += [s, s]
                        dd = 1.0 if ax == 0 else 0.0
                        dx += [dd, -dd]
        self.r, self.c = np.array(r), np.array(c)
        self.vhop, self.dxb = np.array(val), np.array(dx)
        self.Phi1 = self.xs - self.Lx / 2.0

    def _coo(self, vals):
        return sp.csr_matrix((vals, (self.r, self.c)), shape=(self.V, self.V))

    def H0(self, m):
        return (self._coo(self.vhop) + sp.diags(m * self.sgn)).tocsr()

    def bonds(self, Phi, alpha):
        return self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c]))

    def bonds_rate(self, Phi, kappa, nur_, gm):
        """(1 + Phibar) x g(r_v, r_j)/g(r_0, r_0), r_v = r_0 (1 + kappa Phi_v)."""
        Pv_, Pj_ = Phi[self.r], Phi[self.c]
        Pb_ = 0.5 * (Pv_ + Pj_)
        d = (np.power((1.0 + kappa * Pv_) * (1.0 + kappa * Pj_), nur_ / 2.0) if gm
             else np.power(1.0 + kappa * Pb_, nur_))
        return self.vhop * (1.0 + Pb_) * d

    def HPhi(self, m, Phi, ab):
        return (self._coo(self.bonds(Phi, ab[0]))
                + sp.diags(m * self.sgn * (1.0 + ab[1] * Phi))).tocsr()

    def HRate(self, m, Phi, kappa, nur_, gm=False):
        return (self._coo(self.bonds_rate(Phi, kappa, nur_, gm))
                + sp.diags(m * self.sgn * (1.0 + Phi))).tocsr()

    def Cx(self, Phi, ab):
        return self._coo(self.bonds(Phi, ab[0]) * self.dxb)

    def CxRate(self, Phi, kappa, nur_, gm=False):
        return self._coo(self.bonds_rate(Phi, kappa, nur_, gm) * self.dxb)


CUBE = Box(2, 2, 3)                              # the coarse cube, read in 12 qubits
PBOX = Box(4, 4, 4, per=(True, True, True))      # the periodic sea, uniform Phi
SL = Box(16, 4, 4)                               # the dense slab, side-by-side responses
L = Slab(192, 16, 4)                             # the sparse slab, wavepackets


# Finite calculation group

t, Pv, Pj, kap, nu, cc = smp.symbols("t Phi_v Phi_j kappa nu c", real=True)
Pb = (Pv + Pj) / 2


def lin_quad(W):
    """Linear and quadratic coefficients of W(t Phi) in t."""
    s = smp.series(W.subs({Pv: t * Pv, Pj: t * Pj}), t, 0, 3).removeO()
    p = smp.Poly(smp.expand(s), t)
    return smp.simplify(p.coeff_monomial(t)), smp.simplify(p.coeff_monomial(t ** 2))


# The base energy-density coupling puts one unit of Phi on the bond (parent H(1,1)).
BASE = 1 + Pb
W_AM = BASE * (1 + kap * Pb) ** nu                                    # arithmetic mean
W_GM = BASE * ((1 + kap * Pv) * (1 + kap * Pj)) ** (nu / 2)           # geometric mean

lin_am, q_am = lin_quad(W_AM)
lin_gm, q_gm = lin_quad(W_GM)
want = (1 + kap * nu) * Pb
check(
    'A1' + " " + 'AM smooth positive-rate expansion: alpha=1+kappa*nu, beta=1; alpha=2 iff product=1.',
    smp.simplify(lin_am - want) == 0,
)
check(
    'A2' + " " + 'GM has the same first-order coefficient on its positive-rate domain.',
    smp.simplify(lin_gm - want) == 0,
)
dq = smp.simplify(smp.expand(q_am - q_gm))
pred = nu * kap ** 2 * (Pv - Pj) ** 2 / 8
check(
    'A3' + " " + 'AM minus GM quadratic coefficient is nu*kappa**2*(Phi_v-Phi_j)**2/8; full difference has cubic remainder.',
    smp.simplify(dq - pred) == 0,
)

# Smooth nonzero symmetric homogeneous examples: Euler fixes their linear coefficient.
A_, B_ = smp.symbols("A B", positive=True)
gen_ok = []
for p in (1, 2, 3):
    x, y = 1 + kap * Pv, 1 + kap * Pj
    g = (A_ * x ** p + A_ * y ** p + B_ * (x * y) ** (smp.Rational(p, 2))) / (2 * A_ + B_)
    gen_ok.append(smp.simplify(lin_quad(BASE * g ** (nu / p))[0] - want) == 0)
W_odd = BASE * (((1 + kap * Pv) ** nu + (1 + kap * Pj) ** nu) / 2)    # not a mean at all
gen_ok.append(smp.simplify(lin_quad(W_odd)[0] - want) == 0)
check(
    'A4' + " " + 'Differentiable symmetric homogeneous nonzero dressings: Euler coefficient; tested weighted homogeneous family p=1,2,3 and non-mean example.',
    all(gen_ok),
)

S_v, S_j, T_v, T_j, ev = smp.symbols("S_v S_j T_v T_j epsilon_v", real=True)
bond_avg = ((S_v + ev * T_v) + (S_j - ev * T_j)) / 2      # a bond joins opposite sublattices
check(
    'A5' + " " + 'Bipartite bond identity: average(S+eps*T)=average(S)+eps_v*(T_v-T_j)/2; no pointwise cancellation follows without equal endpoint T.',
    smp.simplify(bond_avg - ((S_v + S_j) / 2 + ev * (T_v - T_j) / 2)) == 0,
)

GR = 1e-3
Phi1 = SL.xs - SL.L[0] / 2.0
INT = (SL.xs > 3.5) & (SL.xs < SL.L[0] - 4.5)


def responses(m, ab):
    got = [SL.dens(m, s * GR * Phi1, ab) for s in (+1.0, -1.0)]
    docc = (got[0][0] - got[1][0]) / (2 * GR)
    dE = (got[0][1] - got[1][1]) / (2 * GR)
    return docc, dE / SL.dens(m, np.zeros(SL.V), ab)[1]


def decomp(q):
    """Least squares q_v = A Phi_v + B eps_v Phi_v + C + D eps_v on interior sites."""
    X = np.stack([Phi1, SL.sgn * Phi1, np.ones(SL.V), SL.sgn], axis=1)[INT]
    return np.linalg.lstsq(X, q[INT], rcond=None)[0]


def bondavg(q):
    i, j = SL.r[SL.bi], SL.c[SL.bi]
    keep = INT[i] & INT[j]
    qb = 0.5 * (q[i] + q[j])[keep]
    pb = 0.5 * (Phi1[i] + Phi1[j])[keep]
    return float(np.dot(qb, pb) / np.dot(pb, pb))


tab = []
for m in (0.5, 1.0, 2.0):
    for ab in (ENERGY, FULL):
        docc, dE = responses(m, ab)
        ao, bo, _, _ = decomp(docc)
        ae, be, _, _ = decomp(dE)
        tab.append((m, ab[0], ao, bo, bondavg(docc), ae, be, bondavg(dE)))
kap_rec = max(abs(r[4]) for r in tab)
K_min = min(abs(r[7]) for r in tab)
stag_e = max(abs(r[6]) for r in tab)
check(
    'A6' + " " + f'All-open 16x4x4 ramp: projected occupation bond coefficient <= {kap_rec:.3e}; fitted staggered coefficient <= {max(abs(r[3]) for r in tab):.6f}; energy bond coefficient >= {K_min:.6f}, staggered fit <= {stag_e:.3e}. These are projections.',
    kap_rec < 1e-9 and K_min > 0.5 and stag_e < 1e-6,
)
print("   m/alpha | rho_rec scalar/stag/bond | E_v scalar/stag/bond")
for r in tab:
    print("   %.1f/%.0f | %8.1e %6.3f %8.1e | %7.5f %8.1e %7.5f"
          % (r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

P20 = 20.0 * 0.01 * L.Phi1 / np.max(np.abs(L.Phi1))     # the declared tidal-probe field
amgm = []
for sc in (1.0, 0.5):
    P = sc * P20
    D = L.HRate(1.0, P, 1.0, 1.0, False) - L.HRate(1.0, P, 1.0, 1.0, True)
    Dp = L._coo(L.vhop * (P[L.r] - P[L.c]) ** 2 / 8.0)
    amgm.append(float(np.abs((D - Dp).data).max()) / float(np.abs(Dp.data).max()))
check(
    'A7' + " " + f'192x16x4 AM-GM quadratic approximation relative residuals {amgm}; leading-order comparison only.',
    amgm[0] < 2e-3,
)


# Direct controls of the two errors the original projection could not detect.
q_control, _ = responses(1.0, FULL)
i_control, j_control = SL.r[SL.bi], SL.c[SL.bi]
keep_control = INT[i_control] & INT[j_control]
pointwise_control = float(np.max(abs(0.5*(q_control[i_control]+q_control[j_control])[keep_control])))
X_control = np.stack([Phi1, SL.sgn*Phi1, np.ones(SL.V), SL.sgn], axis=1)[INT]
fit_control = float(np.max(abs(q_control[INT] - X_control @ decomp(q_control))))
check(f"A6a projected zero is not pointwise: max bond={pointwise_control:.8f}, site-fit residual={fit_control:.8f}",
      abs(bondavg(q_control)) < 1e-9 and pointwise_control > 0.08 and fit_control > 0.02)
# A symmetric homogeneous function without differentiability need not obey Euler's linearization.
epsilon_control = 1e-3
cusp_error = max(1+epsilon_control, 1-epsilon_control)-1
check(f"A4a max(x,y) homogeneous cusp gives linear |epsilon|={cusp_error:.6f}",
      abs(cusp_error/epsilon_control-1) < 1e-12)

# Finite calculation group

lnWb_am = smp.log(1 + Pb) + nu * smp.log(1 + kap * Pb)
lnWb_gm = smp.log(1 + Pb) + (nu / 2) * (smp.log(1 + kap * Pv) + smp.log(1 + kap * Pj))
lnWm = smp.log(1 + Pv)
bend = {}
for tag, lw in (("AM", lnWb_am), ("GM", lnWb_gm)):
    num = (smp.diff(lw, Pv) + smp.diff(lw, Pj)).subs({Pv: cc, Pj: cc})
    bend[tag] = smp.simplify(num / smp.diff(lnWm, Pv).subs({Pv: cc}))
pred_b = 1 + nu * kap * (1 + cc) / (1 + kap * cc)
check(
    'B1' + " " + 'Log-derivative ratio Q(c)=1+nu*kappa*(1+c)/(1+kappa*c), AM and GM, nonzero denominators. Q is not physical constant-mode symmetry.',
    smp.simplify(bend["AM"] - pred_b) == 0 and smp.simplify(bend["GM"] - pred_b) == 0
    and smp.simplify(smp.diff(pred_b, cc).subs(cc, 0) - nu * kap * (1 - kap)) == 0
    and smp.simplify((nu * kap * (1 - kap)).subs(nu, 1 / kap)) == smp.simplify(1 - kap),
)
sols = smp.solve([smp.Eq(kap * nu, 1), smp.Eq(nu * kap * (1 - kap), 0)], [kap, nu], dict=True)
check(
    'B2' + " " + f'Q-constancy on product=1 selects {sols}; both constraints are stipulated, not derived gauge requirements.',
    len(sols) == 1 and sols[0][kap] == 1 and sols[0][nu] == 1,
)


# The actual uniform rate Hamiltonian still changes its dimensionless mass.
c_control = 0.1
h0_control = SL.hmat(1.0, np.zeros(SL.V), FULL)
mass_control = np.diag(SL.sgn)
hc_control = (1+c_control)**2*(h0_control-mass_control)+(1+c_control)*mass_control
scale_control = float(np.sum(hc_control*h0_control)/np.sum(h0_control*h0_control))
scalar_error = float(np.max(abs(hc_control-scale_control*h0_control)))
check(f"B3 Q constancy does not imply scalar rescaling: c=.1 bestscale={scale_control:.8f}, residual={scalar_error:.8f}, normalizedmass={1/(1+c_control):.8f}",
      scalar_error > 0.09)

# Finite calculation group

NQ, NF = CUBE.V, CUBE.V // 2
BASIS = [b for b in range(4096) if bin(b).count("1") == NF]
POSN = {b: i for i, b in enumerate(BASIS)}
DIM = len(BASIS)


def many_body(m, Phi, ab):
    """EXACT half-filled ground state in the coarse cube's 12-qubit space (Jordan-Wigner)."""
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
    ev_, EV = np.linalg.eigh(A)
    p = EV[:, 0] ** 2
    occ = np.array([sum(p[i] for i, b in enumerate(BASIS) if (b >> v) & 1) for v in range(NQ)])
    return occ, ev_[0]


RAMP = CUBE.zs - 1.0
for mtest, abtest in ((0.7, ENERGY), (0.7, FULL)):
    Ph = 0.05 * RAMP
    occ_mb, E0_mb = many_body(mtest, Ph, abtest)
    occ_sp, Ev_c, _, _ = CUBE.dens(mtest, Ph, abtest)
    d_occ = float(np.max(np.abs(occ_mb - occ_sp)))
    d_E = abs(float(Ev_c.sum()) - E0_mb)
check(
    'C1' + " " + f'Open 2x2x3, half-filled 924 sector, m=.7 ramp H(2,1): total-energy and occupation residuals {d_E:.3e}, {d_occ:.3e}.',
    d_E < 1e-8 and d_occ < 1e-8,
)

PZ = np.zeros(PBOX.V)


def Kof(m, alpha, g=1e-5):
    """d ln|E_v|/dPhi for a UNIFORM Phi (no gradient corrections at all)."""
    out = [PBOX.dens(m, s * g * np.ones(PBOX.V), (alpha, 1.0))[1] for s in (+1.0, -1.0)]
    E0 = PBOX.dens(m, PZ, (alpha, 1.0))[1]
    return (out[0] - out[1]) / (2 * g) / E0, E0


def wm_of(m, alpha=1.0):
    _, Ev_, Eh_, Em_ = PBOX.dens(m, PZ, (alpha, 1.0))
    return Em_ / Ev_, Ev_, Eh_, Em_


K11, E0p = Kof(0.9, 1.0)
uni = float(np.max(np.abs(E0p - E0p.mean())) / abs(E0p.mean()))
check(
    'C2' + " " + f'Uniform positive rescaling on periodic4^3 m=.9: K(1)={float(K11.mean()):.10f}, energy spread={uni:.3e}; supplied sea energy differs from a Poisson matter source.',
    np.max(np.abs(K11 - 1.0)) < 1e-9 and uni < 1e-12,
)

rows_K = []
for m in MASSES_K:
    wm = float(wm_of(m)[0].mean())
    for alpha in ALPHAS_K:
        rows_K.append((m, alpha, wm, float(Kof(m, alpha)[0].mean()),
                       alpha - (alpha - 1.0) * wm))
errK = max(abs(r[3] - r[4]) for r in rows_K)
check(
    'C3' + " " + f'Uniform response K=alpha*(1-w_m)+beta*w_m; inclusive endpoints; declared mass/alpha grid residual {errK:.3e}.',
    errK < 2e-6,
)
print("   w_m/K at alpha 2: " + " ".join(
    "%.1f:%.4f/%.4f" % (r[0], r[2], r[3]) for r in rows_K if r[1] == 2.0))


# Finite calculation group

nur, wm_s, al = smp.symbols("nu_r w_m alpha", real=True)
Kex = al - (al - 1) * wm_s
fix = smp.solve(smp.Eq(al, 1 + nur * Kex), al)[0]
nu_need = smp.simplify(smp.solve(smp.Eq(fix, 2), nur)[0])
check(
    'D1' + " " + f'Uniform scalar fixed point alpha={smp.simplify(fix)}, denominator nonzero; tuning to2 requires nu={nu_need}. No spatial energy-tracking loop solved.',
    smp.simplify(fix - (1 + nur * wm_s) / (1 - nur * (1 - wm_s))) == 0
    and smp.simplify(nu_need - 1 / (2 - wm_s)) == 0,
)
slope = smp.simplify(smp.diff(1 + nur * Kex, al).subs(nur, 1 / (2 - wm_s)))
check(
    'D2' + " " + f'Uniform scalar tuned slope {slope} lies in[0,1/2] for w_m in[0,1], equality at0; nu=1,w_m=0 has slope1 and no fixed point.',
    smp.simplify(slope - (1 - wm_s) / (2 - wm_s)) == 0
    and smp.simplify((smp.diff(1 + nur * Kex, al)).subs({nur: 1, wm_s: 0})) == 1,
)

rows_fp = []
for m in MASSES_K:
    wm = float(wm_of(m)[0].mean())
    nu_star = 1.0 / (2.0 - wm)
    a = 1.0
    for _ in range(200):                          # the COMPUTED K, never the formula
        a = 1.0 + nu_star * float(Kof(m, a)[0].mean())
    rows_fp.append((m, wm, nu_star, a, float(Kof(m, a)[0].mean())))
err_fp = max(abs(r[3] - 2.0) for r in rows_fp)
check(
    'D3' + " " + f'200 uniform scalar iterations for each declared mass reach alpha=2 within {err_fp:.3e}; no spatial self-consistency conclusion.',
    err_fp < 1e-5,
)
print("   m/nu*/alpha*/kappa*: " + " ".join(
    "%.1f:%.4f/%.6f/%.4f" % (r[0], r[2], r[3], r[4]) for r in rows_fp))


def edens_slab(m, mk, g):
    got = []
    for s in (+1.0, -1.0):
        H = mk(m, s * g * Phi1)
        got.append(np.einsum("vj,jv->v", H, SL.sea(H) - 0.5 * np.eye(SL.V)))
    return got[0], got[1]


def Hrate_dense(m, P, kappa, nur_, gm=False):
    H = np.zeros((SL.V, SL.V))
    Pv_, Pj_ = P[SL.r], P[SL.c]
    Pb_ = 0.5 * (Pv_ + Pj_)
    d = (np.power((1.0 + kappa * Pv_) * (1.0 + kappa * Pj_), nur_ / 2.0) if gm
         else np.power(1.0 + kappa * Pb_, nur_))
    np.add.at(H, (SL.r, SL.c), SL.vhop * (1.0 + Pb_) * d)
    return H + np.diag(m * SL.sgn * (1.0 + P))


d1 = []
for g in (4e-3, 2e-3):
    Ep, _ = edens_slab(1.0, lambda m, P: Hrate_dense(m, P, 1.0, 1.0), g)
    Fp, _ = edens_slab(1.0, lambda m, P: SL.hmat(m, P, FULL), g)
    d1.append(float(np.max(np.abs(Ep - Fp)[INT])))
check(
    'D4' + " " + f'All-open slab INTERIOR max energy residuals {d1}, ratio {d1[0]/d1[1]:.6f}; external-rate versus linear-family comparison.',
    abs(d1[0] / d1[1] - 4.0) < 0.4,
)
d2 = [float(Kof(1.0, 2.0)[0].mean() - Kof(1.0, 1.0)[0].mean()), float(1.0 - wm_of(1.0)[0].mean())]
check(
    'D5' + " " + f'Uniform response shift K(2)-K(1)={d2[0]:.6f}, 1-w_m={d2[1]:.6f}; feedback requires an additional source equation and reference.',
    abs(d2[0] - d2[1]) < 1e-6 and d2[0] > 0.5,
)


# Finite calculation group

PHI_U = 0.01 * L.Phi1 / np.max(np.abs(L.Phi1))

rows = []
for tag, kk, nn, gm in (("AM (1,1)", 1.0, 1.0, False), ("GM (1,1)", 1.0, 1.0, True),
                        ("AM (2,1/2)", 2.0, 0.5, False), ("GM (2,1/2)", 2.0, 0.5, True),
                        ("AM (1/2,2)", 0.5, 2.0, False)):
    rr = []
    for sc in (1.0, 0.5):
        D = L.HRate(1.0, sc * PHI_U, kk, nn, gm) - L.HPhi(1.0, sc * PHI_U, FULL)
        rr.append(float(np.abs(D.data).max()))
    rows.append((tag, rr[0], rr[0] / rr[1]))
Dctl = L.HRate(1.0, PHI_U, 1.0, 0.5, False) - L.HPhi(1.0, PHI_U, FULL)
ctl = float(np.abs(Dctl.data).max())
check(
    'E1' + " " + f'Declared rate parameters: sparse Hamiltonian residual ratios {fmt([r[2] for r in rows],2)}; off-product control {ctl:.3e}.',
    all(abs(r[2] - 4.0) < 0.35 for r in rows) and ctl > 1e-4,
)


def bnd(m, Pmax, alpha):
    return 6.0 * (1.0 + alpha * abs(Pmax)) + abs(m) * (1.0 + abs(Pmax)) + 0.05


def cheb_evolve(H, psi, dt, B):
    th = B * dt
    N = int(th + 25 + 4 * th ** (1.0 / 3.0))
    n = np.arange(N + 1)
    cf = (2.0 - (n == 0)) * (-1j) ** n * jv(n, th)
    N = int(np.where(np.abs(cf) > 1e-16)[0].max())
    t0, t1 = psi, H.dot(psi) / B
    out = cf[0] * t0 + cf[1] * t1
    for k in range(2, N + 1):
        t2 = 2.0 * (H.dot(t1) / B) - t0
        out = out + cf[k] * t2
        t0, t1 = t1, t2
    return out


def cheb_apply(H, psi, f, B, N=700, K=4096):
    th = PI * (np.arange(K) + 0.5) / K
    fv = f(B * np.cos(th))
    cf = np.array([(2.0 - (n == 0)) / K * np.sum(fv * np.cos(n * th)) for n in range(N + 1)])
    t0, t1 = psi, H.dot(psi) / B
    out = cf[0] * t0 + cf[1] * t1
    for k in range(2, N + 1):
        t2 = 2.0 * (H.dot(t1) / B) - t0
        out = out + cf[k] * t2
        t0, t1 = t1, t2
    return out


def disp(p, m):
    return float(np.sqrt(sum(2.0 - 2.0 * np.cos(pa) for pa in p) + m * m))


def packet(m, p, sx):
    dx = L.xs - L.Lx / 2.0
    env = np.exp(-dx ** 2 / (2 * sx ** 2))
    k = [(PI + pa) / 2.0 for pa in p]
    seed = (env * np.exp(1j * (k[0] * L.xs + k[1] * L.ys + k[2] * L.zs))).astype(complex)
    E0 = disp(p, m)
    w = max(0.12, 0.30 * E0)
    psi = cheb_apply(L.H0(m), seed, lambda e: np.exp(-(e - E0) ** 2 / (2 * w * w)), bnd(m, 0.0, 1.0))
    return psi / np.linalg.norm(psi)


C0 = L.Cx(np.zeros(L.V), ENERGY)
_PK = {}


def tuned(m, py, sx, tol=2e-3):
    """The packet prepared on the free H0, with p_x tuned so that <v_x> = 0."""
    key = (m, py, sx)
    if key in _PK:
        return _PK[key]

    def vxof(px):
        ps = packet(m, (px, py, 0.0), sx)
        return float((1j * np.vdot(ps, C0.dot(ps))).real), ps

    v0, ps0 = vxof(0.0)
    if abs(v0) < tol:
        _PK[key] = ps0
    else:
        dd = 0.05
        v1, _ = vxof(dd)
        _PK[key] = vxof(-v0 * dd / (v1 - v0))[1]
    return _PK[key]


def response(m, psi0, mk, mkC, amax, gfield, dt=0.5):
    """The exact Ehrenfest acceleration, centrally differenced in the field."""
    rec, nt = {}, int(round(6.0 / dt))
    for sg in (+1.0, -1.0):
        Phi = sg * gfield * L.Phi1
        H, Cx = mk(m, Phi), mkC(Phi)
        B = float(np.asarray(abs(H).sum(axis=1)).max()) + 0.05  # actual nonlinear matrix bound
        psi, ax = psi0.copy(), []
        for it in range(nt + 1):
            ax.append(-2.0 * np.vdot(H.dot(psi), Cx.dot(psi)).real)
            if it < nt:
                psi = cheb_evolve(H, psi, dt, B)
        rec[sg] = np.array(ax)
    return float(((rec[1.0] - rec[-1.0]) / (2 * gfield)).mean())


def richardson(a32, a44, s1=SIG[0], s2=SIG[1]):
    u1, u2 = 1.0 / s1 ** 2, 1.0 / s2 ** 2
    return (a44 * u1 - a32 * u2) / (u1 - u2)


def rest_row(mk, mkC, amax, m, gfield=G_FIELD):
    return richardson(*[response(m, tuned(m, 0.0, sx), mk, mkC, amax, gfield) for sx in SIG])


def scheme_rows(mk, mkC, amax, gfield=G_FIELD):
    out = {}
    for tag, (m, py) in (("rest", (1.0, 0.0)), ("light", (0.0, PI / 4))):
        out[tag] = richardson(*[response(m, tuned(m, py, sx), mk, mkC, amax, gfield) for sx in SIG])
    return out["rest"], out["light"], out["light"] / out["rest"]


RATE_MK = (lambda m, P: L.HRate(m, P, 1.0, 1.0), lambda P: L.CxRate(P, 1.0, 1.0))
DECL_MK = (lambda m, P: L.HPhi(m, P, FULL), lambda P: L.Cx(P, FULL))
SCH = {}
SCH["parent H(1,1)"] = scheme_rows(lambda m, P: L.HPhi(m, P, ENERGY), lambda P: L.Cx(P, ENERGY), 1.0)
SCH["declared H(2,1)"] = scheme_rows(DECL_MK[0], DECL_MK[1], 2.0)
SCH["rate AM (1,1)"] = scheme_rows(RATE_MK[0], RATE_MK[1], 2.0)
SCH["rate GM (1,1)"] = scheme_rows(lambda m, P: L.HRate(m, P, 1.0, 1.0, True),
                                   lambda P: L.CxRate(P, 1.0, 1.0, True), 2.0)
SCH["rate AM (2,1/2)"] = scheme_rows(lambda m, P: L.HRate(m, P, 2.0, 0.5),
                                     lambda P: L.CxRate(P, 2.0, 0.5), 2.0)
print("   rest/massless/acceleration-ratio: " + " | ".join(
    "%s %.5f %.5f %.4f" % (k_, v_[0], v_[1], v_[2]) for k_, v_ in SCH.items()))
check(
    'E2' + " " + f'Finite packet acceleration ratios (two-width Richardson assumption): {SCH}; not an exact curvature or light-bending observable.',
    all(abs(SCH[k][2] - 2.0) < 0.03 for k in ("rate AM (1,1)", "rate GM (1,1)", "rate AM (2,1/2)"))
    and abs(SCH["parent H(1,1)"][2] - 1.0) < 0.03,
)

ffr = {mm: rest_row(RATE_MK[0], RATE_MK[1], 2.0, mm) for mm in (0.5, 2.0)}
ffd = {mm: rest_row(DECL_MK[0], DECL_MK[1], 2.0, mm) for mm in (0.5, 2.0)}
ffr[1.0], ffd[1.0] = SCH["rate AM (1,1)"][0], SCH["declared H(2,1)"][0]
spread = max(ffr.values()) - min(ffr.values())
gap = max(abs(ffr[mm] - ffd[mm]) for mm in ffr)
check(
    'E3' + " " + f'Declared rest packets: rate {ffr}, linear {ffd}; spread={spread:.6f}, gap={gap:.6f}. Residual origin and all-mass universality not proved.',
    all(abs(x + 4.0) < 0.09 for x in ffr.values()) and spread < 0.09 and gap < 0.07,
)

sc_small = scheme_rows(RATE_MK[0], RATE_MK[1], 2.0, GS_SMALL)
de_small = scheme_rows(DECL_MK[0], DECL_MK[1], 2.0, GS_SMALL)
e_big = abs(SCH["rate AM (1,1)"][2] - SCH["declared H(2,1)"][2])
e_sml = abs(sc_small[2] - de_small[2])
PMAX = G_FIELD * np.max(np.abs(L.Phi1))
check(
    'E4' + " " + f'Two-field acceleration-ratio mismatch {e_big:.7f}->{e_sml:.7f}, reduction {e_big/max(e_sml,1e-12):.4f}; small-field ratios {sc_small[2]:.7f},{de_small[2]:.7f}; maxPhi={PMAX:.4f}. Not a convergence proof.',
    e_sml < e_big and e_big / max(e_sml, 1e-12) > 2.0,
)


# Finite calculation group

Ph_s, MPl, c_s = smp.symbols("Phi_v M_Pl c", positive=True)
a_tau = 1 / ((1 + Ph_s) * MPl * c_s)              # the LOCAL reading, stipulated here
a_tau0 = 1 / (MPl * c_s)                          # supplied reference scale
ratio = smp.simplify((1 / a_tau) / (1 / a_tau0))  # r_v / r_0 in coordinate time
kappa_read = smp.simplify(smp.diff(ratio, Ph_s).subs(Ph_s, 0))
slower = float(ratio.subs(Ph_s, smp.Rational(-1, 10)))     # illustrative negative potential
check(
    'F1' + " " + f'Stipulated local tick arithmetic only: r/r0={ratio}, derivative={kappa_read}, value(-.1)={slower:.4f}; no clock/carrier authority.',
    smp.simplify(ratio - (1 + Ph_s)) == 0 and kappa_read == 1 and slower < 1.0,
)

print("SUMMARY: finite conditional identities and declared-fixture calculations only; physical source, carrier, metric and cosmology remain open.")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
