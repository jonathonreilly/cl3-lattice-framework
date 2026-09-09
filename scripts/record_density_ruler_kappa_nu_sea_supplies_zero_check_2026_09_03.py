#!/usr/bin/env python3
"""Conditional density dressing and finite sea-occupation diagnostics.
Pointwise differentiable positive dressing gives alpha=1+kappa*nu. A global
r-parameter proof establishes the uniform-amplitude t=1 toy bound. The massive
sea has a numerically near-zero fitted slope but nonzero local response and fit residual.
Fock/Born occupations do not construct fine-site Records. All original fixtures
and check identities remain. No physical clock, density law or gravity is derived.
Largest dense matrix is the 924-dimensional fixed-number Fock block; packet slab
192x16x4 is sparse. Declared note/definition/memo inputs are literal and guarded.
"""

from __future__ import annotations

import sys
import hashlib
from pathlib import Path

import numpy as np
import scipy.sparse as sp
import sympy as smp
from mpmath import mp
from scipy.optimize import minimize_scalar
from scipy.special import jv

AUDIT_TIMEOUT_SEC = 150

AUDIT_INPUT_PATHS = ('docs/THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md')
EXPECTED_INPUT_SHA256 = {'docs/THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'b825a35dcb4f73488ddd06d4607eb40f8a6e87b34ca0f44c6098bd963cf10b99', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c27e83f4d8f3fe21113a4f09d2f816591679854a31ba93d8d8c5ad8e23f81324', 'docs/RECORD_DENSITY_SLOWS_LR_FRONT_OPTICAL_METRIC_TOY_BOUNDED_THEOREM_NOTE_2026-06-09.md': 'acd91d88c48e67edebe9a18afa3e622caa5d170a6aed06bdfc0f8afb8d83c4f3'}

def verify_declared_inputs(root=None):
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    bad = [p for p in AUDIT_INPUT_PATHS
           if not (root/p).is_file() or hashlib.sha256((root/p).read_bytes()).hexdigest() != EXPECTED_INPUT_SHA256[p]]
    return bad

_input_failures = verify_declared_inputs()
if _input_failures:
    print("FAIL Q0 [current source/definition/memo inputs] " + repr(_input_failures))
    raise SystemExit(1)
print("INPUT_GUARD: all declared current note/definition/memo bytes match")

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
G_FIELD = 1.0e-3                 # finite central-difference field, with O(g^2) bias
FULL, ENERGY = (2.0, 1.0), (1.0, 1.0)
SIG = (32.0, 44.0)               # the two declared packet widths
T_HOP = 1.0                      # the toy's bare hopping
G_TOY = 0.4                      # the supplied toy definition's registration coupling
# The historical toy table, quoted for comparison (t = 1, g = 0.4).
NOTE_TABLE = ((0.0, 2.0000), (0.125, 1.7986), (0.25, 1.7379), (0.5, 1.6396), (1.0, 1.5649))
# Declared (kappa, nu) pairs on the surface kappa nu = 1, and one control off it.
KN_PAIRS = ((8.0, 0.125), (1.0, 1.0), (-8.0, -0.125), (-1.0, -1.0), (2.0, 0.5))
KN_CONTROL = (1.0, 0.125)
KAP8, NU8 = -8.0, -0.125         # the toy's own bound: |nu| <= 1/8 forces |kappa| >= 8


# ============================================ A. THE DERIVED CONDITION (exact, symbolic)

Phib, kap, nu, rho0 = smp.symbols("Phibar kappa nu rho0", real=True)
a_, b_, c_ = smp.symbols("alpha beta c", real=True)
m_ = smp.symbols("m", positive=True)

# S1 + S2: the bond already carries one unit of Phi from the energy-density coupling,
# and is dressed by f(rho_rec)/f(rho_0) with rho_rec = rho_0 (1 + kappa Phibar).
rho_bond = rho0 * (1 + kap * Phib)
w_pow = (1 + Phib) * (rho_bond / rho0) ** nu
c1 = smp.simplify(smp.expand(smp.series(w_pow, Phib, 0, 2).removeO()).coeff(Phib, 1))
fgen = smp.Function("f")
w_gen = (1 + Phib) * fgen(rho_bond) / fgen(rho0)
c1g = smp.simplify(smp.expand(smp.series(w_gen, Phib, 0, 2).removeO()).coeff(Phib, 1))
nu_def = rho0 * smp.Derivative(fgen(rho0), rho0).doit() / fgen(rho0)
pow_ok = smp.simplify(c1 - (1 + kap * nu)) == 0
gen_ok = smp.simplify(c1g - (1 + kap * nu_def)) == 0
# alpha = 1 + kappa nu against the family's bond weight 1 + alpha Phibar; beta = 1.
alpha_of = 1 + kap * nu
two_iff = smp.simplify(smp.solve(smp.Eq(alpha_of, 2), kap * nu)[0] - 1) == 0
check(
    'A1 [conditional derivative] For positive rho0 and differentiable positive f, pointwise rho_b=rho0(1+kappa Phi_b)+o(Phi_b) gives alpha=1+kappa nu, beta=1, nu=rho0 fprime/f. Alpha=2 iff kappa nu=1. O(Phi^2) requires second-order hypotheses.',
    pow_ok and gen_ok and two_iff,
)

# Declared sign convention: Phi<0; these selected powers shrink the hop amplitude.
fnum = smp.lambdify((Phib, kap, nu), (1 + kap * Phib) ** nu, "numpy")
s_bm = float(fnum(-0.1, -1.0, -1.0))     # B-: supplied density and speed signs
s_bp = float(fnum(-0.1, +1.0, +1.0))     # B+: alternative supplied signs
s_wrong = float(fnum(-0.1, -1.0, +1.0))  # kappa nu < 0: the dressing GROWS the amplitude
check(
    'A2 [conditional sign] Declared finite power-law dressing factors %.4f/%.4f and opposite-sign control %.4f; positive power bases are required. These are coefficient signs, not a physical density law.'
    % (s_bm, s_bp, s_wrong),
    s_bm < 1.0 and s_bp < 1.0 and s_wrong > 1.0,
)


# =========================== B. THE SUPPLIED 1D TOY'S OWN COEFFICIENT (exact + numerical)

def v_front(G2, t=T_HOP, K=200001):
    """Front speed of the supplied uniform-amplitude t=1 medium: eliminating the frozen record mode gives
    eps_eff(E) = g^2/E, hence E(k) = -t cos k + sqrt(t^2 cos^2 k + g^2) with the note's
    smooth-profile weight g(x)^2 = g0^2 n(x); v_F(n) = max_k |dE/dk|."""
    if t != 1.0 or G2 < 0 or K < 3:
        raise ValueError("This toy front implementation requires t=1, G2>=0 and K>=3")
    k = np.linspace(0.0, PI, K)
    ck, sk = np.cos(k), np.sin(k)
    r = np.sqrt(t * t * ck * ck + G2)
    dE = sk * (1.0 - np.where(r > 0, t * ck / np.maximum(r, 1e-300), 0.0))
    return float(np.max(np.abs(dE)))


def nu_of(G2, h=1e-4):
    """nu_toy = dln v_F/dln n; v_F depends on n only through G2 = g0^2 n."""
    lo, hi = v_front(G2 * (1 - h)), v_front(G2 * (1 + h))
    return (np.log(hi) - np.log(lo)) / (2 * h)


toy_v = [v_front(G_TOY ** 2 * n) for n, _ in NOTE_TABLE]
toy_ref = [ref for _, ref in NOTE_TABLE]
dec = all(toy_v[i] > toy_v[i + 1] for i in range(len(toy_v) - 1))
small_g = [(2.0 - v_front(gg * gg)) / gg for gg in (0.02, 0.01, 0.005)]
nu_at_1 = nu_of(G_TOY ** 2)
check(
    'B1 [finite toy comparison] Uniform-amplitude front values %s versus historical periodic-dilution table %s; small-g estimates %s versus sqrt(2)=%.6f. The implementations and their intermediate-density values are distinct.'
    % (fmt(toy_v, 4), fmt(toy_ref, 4), fmt(small_g, 6), np.sqrt(2.0)),
    abs(toy_v[0] - 2.0) < 1e-9 and abs(toy_v[-1] - 1.5649) < 5e-4 and dec
    and abs(small_g[-1] - np.sqrt(2.0)) < 5e-3 and nu_at_1 < 0,
)

# The exact stationary point, symbolically: with c = cos k and s = sqrt(1 - c^2),
# f(c, G2) = s (1 - c/sqrt(c^2 + G2)) is the front speed at the stationary momentum, and
# nu = G2 (df/dG2)/f there by the envelope theorem.
cs, G2s = smp.symbols("c G2", real=True)
ss = smp.sqrt(1 - cs ** 2)
rr = smp.sqrt(cs ** 2 + G2s)
fsym = ss * (1 - cs / rr)
star = {cs: -1 / smp.sqrt(5), G2s: smp.Rational(3, 5)}
stat_ok = smp.simplify(smp.diff(fsym, cs).subs(star)) == 0
vF_ok = smp.simplify(fsym.subs(star) - 3 / smp.sqrt(5)) == 0
nu_sym = smp.simplify(G2s * smp.diff(fsym, G2s) / fsym)
nu_ok = smp.simplify(nu_sym.subs(star) + smp.Rational(1, 8)) == 0
# A retained 40-digit finite stationary diagnostic; globality is proved separately.
mp.dps = 40


def nu_mp(x):
    g2 = mp.mpf(x)
    kst = mp.findroot(lambda k: mp.diff(
        lambda kk: mp.sin(kk) * (1 - mp.cos(kk) / mp.sqrt(mp.cos(kk) ** 2 + g2)), k), mp.mpf(2))
    cc, sc = mp.cos(kst), mp.sin(kst)
    rc = mp.sqrt(cc ** 2 + g2)
    return g2 * (sc * cc / (2 * rc ** 3)) / (sc * (1 - cc / rc))


# 61 declared points: a geometric sweep over g0^2 n and a fine sweep across the extremum.
MP_GRID = ([mp.mpf(5) / 100 * (mp.mpf(20) / mp.mpf("0.05")) ** (mp.mpf(j) / 40) for j in range(41)]
           + [mp.mpf(3) / 5 + mp.mpf(j) / 200 for j in range(-10, 11)])
mp_at = nu_mp(mp.mpf(3) / 5)
mp_min = min(nu_mp(x) for x in MP_GRID)
_r = minimize_scalar(lambda u: nu_of(float(np.exp(u))), bounds=(-3.0, 3.0),
                     method="bounded", options={"xatol": 1e-12})
check(
    'B2 [stationary diagnostic plus global proof below] At n=1,g0=.4 slope %.5f; 40-digit residual at s=3/5 is %.1e; finite minimizer %.9f at %.6f. The global bound follows from the r-parameter proof, not this grid or minimization.'
    % (nu_at_1, abs(float(mp_at + mp.mpf(1) / 8)), _r.fun, float(np.exp(_r.x))),
    stat_ok and vF_ok and nu_ok and abs(_r.fun + 0.125) < 1e-6 and _r.fun > -0.1250001
    and abs(float(mp_at + mp.mpf(1) / 8)) < 1e-30 and mp_min >= -mp.mpf(1) / 8 - mp.mpf(10) ** -30,
)


# ================================ C. THE SEA'S OWN RECORD STATISTICS (exact + numerical)


def global_toy_bound_control():
    """Exact parameter proof; the note supplies its domain and endpoint argument."""
    r = smp.symbols("r", positive=True)
    u2 = r*(1-r)/(1+r-r*r)
    coupling = (1-r)**2*(1+r)/(r*(1+r-r*r))
    derivative = (r-1)*(3*r+1)/(r*r*(r*r-r-1)**2)
    # From the stationary condition u^2(1+r)=(1-u^2)r(1-r^2).
    stationary = smp.factor(u2*(1+r)-(1-u2)*r*(1-r*r))
    # At fixed u, s*partial_s log F = -r(1-r^2)/(2*(1+r)).
    envelope = smp.factor(-r*(1-r*r)/(2*(1+r)))
    square = smp.factor(smp.Rational(1,8)+envelope)
    tests = [stationary==0, smp.factor(smp.diff(coupling,r)-derivative)==0,
             smp.factor(coupling-u2*(1-r*r)/r**2)==0,
             smp.factor(square-(2*r-1)**2/8)==0,
             coupling.subs(r,smp.Rational(1,2))==smp.Rational(3,5),
             smp.limit(coupling,r,0,dir='+')==smp.oo,
             smp.limit(coupling,r,1,dir='-')==0]
    return {"nu":str(envelope),"one_eighth_plus_nu":str(square),
            "coupling_derivative":str(derivative),"pass":all(tests)}


def zero_mode_control():
    """A chosen pure half-filled zero-mode state differs from the explicit mixture."""
    H=np.zeros((2,2));e,U=np.linalg.eigh(H)
    Pneg=U[:,e<0]@U[:,e<0].T
    Pzero=U[:,e==0]@U[:,e==0].T
    pure=np.diag([1.,0.]);mixed=Pneg+.5*Pzero
    return {"pure":np.diag(pure).tolist(),"mixture":np.diag(mixed).tolist(),
            "pass":np.array_equal(np.diag(mixed),[.5,.5])
                 and np.max(abs(np.diag(pure)-.5))==.5
                 and np.array_equal(2*np.diag(Pneg),1-np.diag(Pzero))}


_q1=global_toy_bound_control()
check("Q1 [global uniform-toy proof] " + str(_q1), _q1["pass"])
_q2=zero_mode_control()
check("Q2 [zero-mode filling domain] " + str(_q2), _q2["pass"])

def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a): eta_1 = 1, eta_2 = (-1)^{v_1},
    eta_3 = (-1)^{v_1+v_2}, the supplied coarse-lattice sign field."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


class Box:
    """Coarse box Lx x Ly x Lz; `per` gives periodicity per axis."""

    def __init__(self, Lx, Ly, Lz, per=(False, False, False)):
        self.L = (Lx, Ly, Lz)
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(*[np.arange(n) for n in self.L], indexing="ij")
        self.xs = ix.ravel().astype(float)
        self.zs = iz.ravel().astype(float)
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()        # eps_v, the STAGGERING SIGN
        r, c, val = [], [], []

        def idx(a, b, cc):
            return (a * Ly + b) * Lz + cc

        for a in range(Lx):
            for b in range(Ly):
                for cc in range(Lz):
                    i = idx(a, b, cc)
                    v = (a, b, cc)
                    for ax in range(3):
                        w = [a, b, cc]
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
        self.r = np.array(r)
        self.c = np.array(c)
        self.vhop = np.array(val)

    def hmat(self, m, Phi, ab):
        """H(alpha, beta) as a dense one-body matrix."""
        alpha, beta = ab
        H = np.zeros((self.V, self.V))
        np.add.at(H, (self.r, self.c),
                  self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c])))
        return H + np.diag(m * self.sgn * (1.0 + beta * Phi))

    def occ_sp(self, m, Phi, ab):
        """One-body occupation, with explicit half-filled zero-mode mixture convention."""
        w, U = np.linalg.eigh(self.hmat(m, Phi, ab))
        neg = w < -1e-12
        occ = np.einsum("ik,ik->i", U[:, neg], U[:, neg])
        zm = np.abs(w) <= 1e-12
        if int(np.sum(zm)):        # declared convention: each zero mode carries weight one half
            Zc = U[:, zm]
            occ = occ + 0.5 * np.einsum("ik,ik->i", Zc, Zc)
        return occ


CUBE = Box(2, 2, 3)                # 12 coarse sites, 12 supplied fermionic modes: Fock dimension 2^12 = 4096
NQ, NF = CUBE.V, CUBE.V // 2
BASIS = [b for b in range(4096) if bin(b).count("1") == NF]
POSN = {b: i for i, b in enumerate(BASIS)}
DIM = len(BASIS)                   # the half-filled sector, 924


def many_body_occ(m, Phi, ab):
    """Supplied fixed-number Fock ground state and Born occupations; no fine-site Record map."""
    Hs = CUBE.hmat(m, Phi, ab)
    if np.min(np.abs(np.linalg.eigvalsh(Hs))) < 1e-10:
        raise ValueError("Pure ground-state comparison requires a gapped one-body fixture")
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
    ev, EV = np.linalg.eigh(A)
    if ev[1]-ev[0] < 1e-10:
        raise ValueError("Selected pure many-body ground state must be nondegenerate")
    p = EV[:, 0] ** 2
    occ = np.array([sum(p[i] for i, b in enumerate(BASIS) if (b >> v) & 1) for v in range(NQ)])
    return occ, ev[0]


ZERO = np.zeros(CUBE.V)
RAMP = CUBE.zs - 1.0               # a ramp along the cube's length-3 axis
occ_mb, E0_cube = many_body_occ(0.0, ZERO, ENERGY)
occ_sp0 = CUBE.occ_sp(0.0, ZERO, ENERGY)
two_routes = float(np.max(np.abs(occ_mb - occ_sp0)))
flat = float(np.max(np.abs(occ_mb - 0.5)))
check(
    'C1 [supplied Fock/Born model] Twelve coarse modes, N=6 sector %d, energy %.6f: many-body versus one-body occupation difference %.1e; gapped m=0 flatness %.1e. This is not the fine-edge BKSF carrier or physical Record formation.'
    % (DIM, E0_cube, two_routes, flat),
    two_routes < 1e-9 and flat < 1e-12,
)

m0_rows = []
for ab in (ENERGY, FULL):
    for prof in (np.ones(CUBE.V), RAMP):
        o, _ = many_body_occ(0.0, 1e-3 * prof, ab)
        m0_rows.append(float(np.max(np.abs(o - 0.5))))
check(
    'C2 [gapped bipartite fixtures] Four m=0 uniform/ramp rows have max occupation deviation %.1e. Invertible H implies Pminus_vv=1/2; half-occupied zero-mode mixture also does, but arbitrary pure zero-mode ground states need not.'
    % max(m0_rows),
    max(m0_rows) < 1e-12,
)

o_ref, _ = many_body_occ(1.0, ZERO, ENERGY)
o_u11, _ = many_body_occ(1.0, 0.037 * np.ones(CUBE.V), ENERGY)
o_u21, _ = many_body_occ(1.0, 0.037 * np.ones(CUBE.V), FULL)
d11 = float(np.max(np.abs(o_u11 - o_ref)))
d21 = float(np.max(np.abs(o_u21 - o_ref)))
sc21 = abs(float(np.mean(o_u21 - o_ref)))
st21 = float(np.mean((o_u21 - o_ref) * CUBE.sgn))
check(
    'C3 [uniform finite occupation response] (1,1) change %.1e; (2,1) local change %.2e, mean %.1e and staggered projection %.2e. The rescaled mass ratio is dimensionless; a zero mean does not remove local density response.'
    % (d11, d21, sc21, st21),
    d11 < 1e-12 and d21 > 1e-4 and sc21 < 1e-12,
)

SLAB = Box(16, 4, 4, per=(False, True, True))      # 256 coarse sites, one-particle route
GS = 1e-3
PHI_S = SLAB.xs - SLAB.L[0] / 2.0
kbond, ksite, rmax = [], [], []
for m in (0.0, 0.5, 1.0, 2.0):
    for ab in (ENERGY, FULL):
        d = (SLAB.occ_sp(m, +GS * PHI_S, ab) - SLAB.occ_sp(m, -GS * PHI_S, ab)) / (2 * GS)
        rb = 0.5 * (d[SLAB.r] + d[SLAB.c])          # finite d rho_bar/dg on every bond
        Pb = 0.5 * (PHI_S[SLAB.r] + PHI_S[SLAB.c])
        kbond.append(float(np.dot(rb, Pb) / np.dot(Pb, Pb)) / 0.5)
        ksite.append(float(np.dot(d, PHI_S) / np.dot(PHI_S, PHI_S)) / 0.5)
        rmax.append(float(np.max(np.abs(rb))))
kmax = max(abs(x) for x in kbond)
check(
    'C4 [projected slope versus local response] Eight ramp rows: max fitted |kappa_bond| %.2e and |kappa_site| %.2e, but max pointwise bond response %.2e. A zero fitted projection is not the pointwise kappa=0 hypothesis.'
    % (kmax, max(abs(x) for x in ksite), max(rmax)),
    kmax < 1e-6,
)

d = (SLAB.occ_sp(1.0, +GS * PHI_S, FULL) - SLAB.occ_sp(1.0, -GS * PHI_S, FULL)) / (2 * GS)
rb = 0.5 * (d[SLAB.r] + d[SLAB.c])
Pb = 0.5 * (PHI_S[SLAB.r] + PHI_S[SLAB.c])
epsb = SLAB.sgn[SLAB.r]
grad = PHI_S[SLAB.r] - PHI_S[SLAB.c]
Bm = np.vstack([Pb, epsb, epsb * grad, np.ones_like(Pb)]).T
co, *_ = np.linalg.lstsq(Bm, rb, rcond=None)
fit_residual = rb - Bm @ co
fit_max = float(np.max(np.abs(fit_residual)))
fit_rms = float(np.sqrt(np.mean(fit_residual**2)))
ksub = [float(np.dot(rb[epsb == s], Pb[epsb == s]) / np.dot(Pb[epsb == s], Pb[epsb == s])) / 0.5
        for s in (+1.0, -1.0)]
check(
    'C5 [finite regression] Coefficients on {Phibar,eps,eps*gradient,1}: %.2e,%.2e,%.3e,%.2e; within-sublattice projected kappas %.2e/%.2e. The nonzero residual is enforced separately: the fit is not the whole local response.'
    % (co[0], co[1], co[2], co[3], ksub[0], ksub[1]),
    abs(co[0]) < 1e-6 and abs(co[2]) > 1e-3 and max(abs(x) for x in ksub) < 1e-6
    and fit_max > .01 and fit_rms > .005,
)


def projector_derivative(H, V):
    """Independent first-order spectral-projector perturbation, no finite difference."""
    ev,U=np.linalg.eigh(H)
    if np.min(abs(ev))<1e-10:
        raise ValueError("Projector derivative requires a spectral gap at zero")
    N=U[:,ev<0];Q=U[:,ev>0]
    C=(Q.T@V@N)/(ev[ev<0][None,:]-ev[ev>0][:,None])
    return 2*np.einsum("vi,ij,vj->v",Q,C,N)


def local_response_control(H, V, measured, measured_fine, edge_r, edge_c, profile, grading):
    """Compare actual local response with independent projector derivative and fit residual."""
    exact=projector_derivative(H,V)
    local=.5*(measured[edge_r]+measured[edge_c])
    ph=.5*(profile[edge_r]+profile[edge_c])
    A=np.column_stack([ph,grading[edge_r],grading[edge_r]*(profile[edge_r]-profile[edge_c]),np.ones(len(ph))])
    coeff=np.linalg.lstsq(A,local,rcond=None)[0]
    res=local-A@coeff
    delta=float(max(abs(exact-measured)))
    delta_fine=float(max(abs(exact-measured_fine)))
    projection=float(2*np.dot(local,ph)/np.dot(ph,ph))
    max_local=float(max(abs(local)));max_res=float(max(abs(res)))
    return {"independent_derivative_difference":delta,"half_field_difference":delta_fine,"projected_kappa":projection,
            "max_local":max_local,"fit_max":max_res,"fit_rms":float(np.sqrt(np.mean(res**2))),
            "pass":delta>1e-10 and delta_fine<.3*delta and delta<.01*max(abs(exact))
                 and abs(projection)<1e-8 and max_local>.1 and max_res>.04}


_Hbase=SLAB.hmat(1.,np.zeros(SLAB.V),FULL)
_V=(SLAB.hmat(1.,PHI_S,FULL)-SLAB.hmat(1.,-PHI_S,FULL))/2
_d_fine=(SLAB.occ_sp(1.,GS*PHI_S/2,FULL)-SLAB.occ_sp(1.,-GS*PHI_S/2,FULL))/GS
_q3=local_response_control(_Hbase,_V,d,_d_fine,SLAB.r,SLAB.c,PHI_S,SLAB.sgn)
check("Q3 [local response and nonzero fit residual] " + str(_q3), _q3["pass"])

alpha_fed = smp.simplify((1 + kap * nu).subs(kap, 0))
check(
    'C6 [conditional substitution only] If the response is pointwise kappa=0, alpha=%s. The gapped massless occupation model supplies that case; the massive zero projected slope does not. No general local-feedback no-go follows.' % alpha_fed,
    alpha_fed == 1,
)


# ================================================ D. TWO RESTRICTED NORMALIZATION/ANSATZ OBSERVATIONS (exact + stated)

m_eff = smp.simplify(m_ * (1 + b_ * c_) / (1 + a_ * c_))
const_ok = smp.simplify(m_eff.subs(b_, a_) - m_) == 0
d_meff = smp.simplify(smp.diff(m_eff, c_).subs(c_, 0))
price_ok = smp.simplify(d_meff.subs({a_: 2, b_: 1}) + m_) == 0
check(
    'D1 [normalization boundary] Uniform c gives hop-normalized m_eff=m(1+beta*c)/(1+alpha*c), derivative m(beta-alpha). At (2,1) it is -m, not a derived physical rest-mass change. G0P0 selects a zero-mean representative when that separate model is chosen.',
    const_ok and price_ok,
)

# On the slab the discrete Laplacian of the linear profile vanishes in the interior, which is
# where the bending and free-fall rows of group E are computed.
lap = np.zeros(SLAB.V)
np.add.at(lap, SLAB.r, PHI_S[SLAB.c] - PHI_S[SLAB.r])
inner = (SLAB.xs > 0.5) & (SLAB.xs < SLAB.L[0] - 1.5)
lap_in = float(np.max(np.abs(lap[inner])))
check(
    'D2 [pointwise source ansatz only] Open linear ramp: interior Laplacian %.1e over %d sites. A response proportional to the supplied source -Delta Phi vanishes there; this does not exclude all local laws, propagated fields or formation dynamics.'
    % (lap_in, int(np.sum(inner))),
    lap_in < 1e-13,
)


# ==================================== E. IF kappa nu = 1 IS DECLARED (numerical, conditional)

class Slab:
    """The parent runner's coarse slab, OPEN in x (the gradient direction), periodic in y, z."""

    def __init__(self, Lx, Ly, Lz):
        self.Lx, self.Ly, self.Lz = Lx, Ly, Lz
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(np.arange(Lx), np.arange(Ly), np.arange(Lz), indexing="ij")
        self.xs = ix.ravel().astype(float)
        self.ys = iy.ravel().astype(float)
        self.zs = iz.ravel().astype(float)
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()
        r, c, val, dx = [], [], [], []

        def idx(a, b, cc):
            return (a * Ly + b) * Lz + cc

        for a in range(Lx):
            for b in range(Ly):
                for cc in range(Lz):
                    i = idx(a, b, cc)
                    v = (a, b, cc)
                    for ax in range(3):
                        w = [a, b, cc]
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
        self.r = np.array(r)
        self.c = np.array(c)
        self.vhop = np.array(val)
        self.dxb = np.array(dx)
        self.Phi1 = self.xs - self.Lx / 2.0

    def _coo(self, vals):
        return sp.csr_matrix((vals, (self.r, self.c)), shape=(self.V, self.V))

    def H0(self, m):
        return (self._coo(self.vhop) + sp.diags(m * self.sgn)).tocsr()

    def bonds(self, Phi, alpha):
        return self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c]))

    def bonds_ruler(self, Phi, kappa, nu_):
        """The record-dressed bond: one unit of Phi from the energy-density coupling, times
        f(rho_rec)/f(rho_0) = (1 + kappa Phibar)^nu with rho_rec = rho_0 (1 + kappa Phibar)."""
        Pb = 0.5 * (Phi[self.r] + Phi[self.c])
        base = 1.0 + kappa * Pb
        if not np.all(np.isfinite(base)) or np.any(base <= 0):
            raise ValueError("Real power dressing requires positive finite 1+kappa*Phibar")
        return self.vhop * (1.0 + Pb) * np.power(base, nu_)

    def HPhi(self, m, Phi, ab):
        alpha, beta = ab
        return (self._coo(self.bonds(Phi, alpha))
                + sp.diags(m * self.sgn * (1.0 + beta * Phi))).tocsr()

    def HRuler(self, m, Phi, kappa, nu_):
        return (self._coo(self.bonds_ruler(Phi, kappa, nu_))
                + sp.diags(m * self.sgn * (1.0 + Phi))).tocsr()

    def Cx(self, Phi, ab):
        return self._coo(self.bonds(Phi, ab[0]) * self.dxb)

    def CxRuler(self, Phi, kappa, nu_):
        return self._coo(self.bonds_ruler(Phi, kappa, nu_) * self.dxb)


L = Slab(192, 16, 4)               # 12288 coarse sites, sparse and matrix-free throughout
PHI_U = 0.01 * L.Phi1 / np.max(np.abs(L.Phi1))

ratios, resid = [], []
for kk, nn in KN_PAIRS:
    rows = []
    for gsc in (1.0, 0.5):
        Ph = gsc * PHI_U
        D = L.HRuler(1.0, Ph, kk, nn) - L.HPhi(1.0, Ph, FULL)
        rows.append(float(np.abs(D.data).max()) if D.nnz else 0.0)
    resid.append(rows[0])
    ratios.append(rows[0] / max(rows[1], 1e-300))
Dw = L.HRuler(1.0, PHI_U, KN_CONTROL[0], KN_CONTROL[1]) - L.HPhi(1.0, PHI_U, FULL)
ctl = float(np.abs(Dw.data).max())
check(
    'E1 [finite dressing comparison] Valid power bases: two scales give residuals %s and quadratic ratios %s; off-product control %.3e. This tests the declared nonlinear dressing, not a derived density law.'
    % (fmt(resid, 6), fmt(ratios, 2), ctl),
    all(abs(x - 4.0) < 0.35 for x in ratios) and ctl > 1e-4,
)


def bound(m, Phimax, alpha):
    """Gershgorin bound on the spectrum, widened for the weighted hop."""
    return 6.0 * (1.0 + alpha * abs(Phimax)) + abs(m) * (1.0 + abs(Phimax)) + 0.05


def cheb_evolve(H, psi, dt, B):
    """exp(-i H dt) psi by Chebyshev expansion; spectrum inside [-B, B]."""
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
    """f(H) psi by Chebyshev expansion of f on [-B, B]."""
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
    """Positive-band wavepacket at Dirac momentum p; prepared on the FREE H0, so it is
    the same packet for every scheme under test."""
    dx = L.xs - L.Lx / 2.0
    env = np.exp(-dx ** 2 / (2 * sx ** 2))
    k = [(PI + pa) / 2.0 for pa in p]
    seed = (env * np.exp(1j * (k[0] * L.xs + k[1] * L.ys + k[2] * L.zs))).astype(complex)
    E0 = disp(p, m)
    w = max(0.12, 0.30 * E0)
    psi = cheb_apply(L.H0(m), seed, lambda e: np.exp(-(e - E0) ** 2 / (2 * w * w)),
                     bound(m, 0.0, 1.0))
    return psi / np.linalg.norm(psi)


C0 = L.Cx(np.zeros(L.V), ENERGY)
_PK = {}


def tuned(m, py, sx, tol=2e-3):
    """p_x chosen so the free packet has <v_x> = 0; memoised across schemes."""
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



def propagation_bound(H, m, Phimax, alpha):
    """Conservative Hermitian spectral bound, including nonlinear dressed matrices."""
    return max(bound(m,Phimax,alpha),float(np.max(np.asarray(abs(H).sum(axis=1))))+.05)


def nonlinear_bound_control(L):
    Phi=.001*L.Phi1
    H=L.HRuler(1.,Phi,-8.,-.125)
    rows=float(np.max(np.asarray(abs(H).sum(axis=1))))
    old=bound(1.,np.max(abs(Phi)),2.)
    new=propagation_bound(H,1.,np.max(abs(Phi)),2.)
    rejected=False
    try:
        L.bonds_ruler(np.ones(L.V),-1.,-.125)
    except ValueError:
        rejected=True
    return {"linear_family_bound":old,"actual_row_bound":rows,"used_bound":new,
            "invalid_power_rejected":rejected,
            "pass":new>rows and rows>old+.5 and rejected}


_q4=nonlinear_bound_control(L)
check("Q4 [nonlinear domain and conservative propagation bound] " + str(_q4), _q4["pass"])

def response(m, psi0, mk, mkC, amax, gfield, T=6.0, dt=0.5):
    """Finite central difference of the Ehrenfest observable; O(g^2) bias remains."""
    rec = {}
    nt = int(round(T / dt))
    for sg in (+1.0, -1.0):
        Phi = sg * gfield * L.Phi1
        H, Cx = mk(m, Phi), mkC(Phi)
        B = propagation_bound(H, m, np.max(np.abs(Phi)), amax)
        psi = psi0.copy()
        ax = []
        for it in range(nt + 1):
            ax.append(-2.0 * np.vdot(H.dot(psi), Cx.dot(psi)).real)
            if it < nt:
                psi = cheb_evolve(H, psi, dt, B)
        rec[sg] = np.array(ax)
    return float(((rec[1.0] - rec[-1.0]) / (2 * gfield)).mean())


def richardson(a32, a44, s1=SIG[0], s2=SIG[1]):
    """Two-width Richardson under a leading 1/sigma_x^2 ansatz; no remainder certificate."""
    u1, u2 = 1.0 / s1 ** 2, 1.0 / s2 ** 2
    return (a44 * u1 - a32 * u2) / (u1 - u2)


def scheme_rows(mk, mkC, amax, gfield=G_FIELD):
    """Rest (m = 1) and massless (p_y = pi/4) rows, Richardson-extrapolated over two widths."""
    out = {}
    for tag, (m, py) in (("rest", (1.0, 0.0)), ("light", (0.0, PI / 4))):
        out[tag] = richardson(*[response(m, tuned(m, py, sx), mk, mkC, amax, gfield)
                                for sx in SIG])
    return out["rest"], out["light"], out["light"] / out["rest"]


r_par = scheme_rows(lambda m, P: L.HPhi(m, P, ENERGY), lambda P: L.Cx(P, ENERGY), 1.0)
r_dec = scheme_rows(lambda m, P: L.HPhi(m, P, FULL), lambda P: L.Cx(P, FULL), 2.0)
r_rul = scheme_rows(lambda m, P: L.HRuler(m, P, -1.0, -1.0),
                    lambda P: L.CxRuler(P, -1.0, -1.0), 2.0)
check(
    'E2 [finite acceleration ratios] Stipulated (-1,-1) dressing gives massive %.5f/massless %.5f/ratio %.4f; (2,1) %.5f/%.5f/%.4f; (1,1) %.5f/%.5f/%.4f. Central differences and width extrapolation have uncertified residual errors; ratios are not ray curvature.'
    % (r_rul[0], r_rul[1], r_rul[2], r_dec[0], r_dec[1], r_dec[2], r_par[0], r_par[1], r_par[2]),
    abs(r_rul[2] - 2.0) < 0.03 and abs(r_rul[0] + 4.0) < 0.05 and abs(r_par[2] - 1.0) < 0.03
    and abs(r_rul[0] - r_dec[0]) < 0.05 and abs(r_rul[1] - r_dec[1]) < 0.15,
)

r_r8 = scheme_rows(lambda m, P: L.HRuler(m, P, KAP8, NU8),
                   lambda P: L.CxRuler(P, KAP8, NU8), 2.0, G_FIELD)
r_r8s = scheme_rows(lambda m, P: L.HRuler(m, P, KAP8, NU8),
                    lambda P: L.CxRuler(P, KAP8, NU8), 2.0, 2.5e-4)
check(
    'E3 [finite nonlinearity] At kappa=-8, max |kappa Phi| %.2f versus |Phi| %.2f, acceleration ratio %.4f (massive %.5f, massless %.5f); at smaller g, %.5f/%.5f/ratio %.4f. Parameters and old finite targets are retained.'
    % (abs(KAP8) * G_FIELD * np.max(np.abs(L.Phi1)), G_FIELD * np.max(np.abs(L.Phi1)),
       r_r8[2], r_r8[0], r_r8[1], r_r8s[0], r_r8s[1], r_r8s[2]),
    r_r8[2] > 2.1 and abs(r_r8s[2] - 2.0) < 0.03,
)

print(
    'SUMMARY: pointwise dressing gives alpha=1+kappa*nu under stated regularity; the supplied uniform toy has a global 1/8 slope bound. Gapped massless occupations are flat, but massive near-zero fitted slope coexists with nonzero local response. Physical readout, formation and gravity remain supplied/open.'
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
