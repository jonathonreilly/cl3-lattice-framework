#!/usr/bin/env python3
"""The record-density ruler is one product kappa * nu = 1, and the half-filled sea
supplies kappa = 0.

Class-A runner.  Conditional on exactly what the spatial-metric note
(PR #7905) is conditional on -- the designed fermion law, the landed weak-field
response surface phi = G0 P0 rho, the choice of the half-filled staggered sea as
the vacuum, and that note's own DECLARED two-weight family

    H(alpha, beta) = sum_bonds [1 + alpha (Phi_v + Phi_j)/2] M_vj
                   + sum_v     [1 + beta  Phi_v]            m eps_v n_v

-- plus four STIPULATIONS made here and derived from nothing: (S1) the bond
amplitude is dressed by f(rho_rec)/f(rho_0) with rho_rec the record density of
the bond's two endpoints; (S2) rho_rec = rho_0 (1 + kappa Phi), a linear
response of the record density to the potential; (S3) the parent's
energy-density coupling stands, so the bond already carries one unit of Phi and
f multiplies only the bond, the mass being a site term; (S4) the background is
the half-filled staggered sea, one-particle sector, first order in Phi.

PR #7905 named the object a derivation of alpha = 2 would need: "a ruler factor:
on this lattice, a record-density or hop-rate dependence on the local energy
density, so that the effective bond amplitude carries a second factor of
(1 + Phi) the on-site term does not."  This runner answers that named interface.

  A  THE DERIVED CONDITION.  alpha = 1 + kappa nu, beta = 1, bending factor
     1 + kappa nu, for a power law and for a general f; alpha = 2 iff the single
     dimensionless product kappa nu = 1 exactly.  The sign structure.
  B  THE LANDED 1D TOY'S OWN COEFFICIENT.  Its medium dispersion reproduced, and
     the exact bound max |dln v_F/dln n| = 1/8 at g0^2 n = 3/5.
  C  THE SEA'S OWN RECORD STATISTICS.  The cube's 12-qubit space and the
     one-particle projector, agreeing; kappa = 0 on the half-filled sea.
  D  THE TWO OBSTRUCTIONS.  The constant mode of Phi, physical once
     alpha != beta; and a response to the local energy density is a Laplacian.
  E  IF kappa nu = 1 IS DECLARED.  The dressed Hamiltonian is H(2, 1) to
     O(Phi^2), and the wavepacket rows return bending 2 and free fall -4.

Group A and group D's algebra are exact identities, checked symbolically; group
B's bound is exact at its stationary point and confirmed at 40 digits; every
other group is a finite floating-point computation reporting its residual
against a tolerance declared before the run.  The acceleration of group E is
never fitted: it is the exact Ehrenfest expectation a(t) = -<[H,[H,X]]>,
differenced centrally in g so that the g-independent part cancels exactly.
No random number is drawn anywhere: every momentum, mass, width, weight pair,
coupling and profile is a declared constant, so the runner is bit-reproducible
without a seed.

Largest dense object: the 924-dimensional half-filled sector of the cube's
12-qubit space (dim 2^12 = 4096); nothing above 4096 x 4096 is formed.  The
192 x 16 x 4 slab of group E is sparse and matrix-free throughout.

This runner is self-contained: it re-declares the coarse lattice, the KS sign
field, the record-native staggered mass, the two-weight family, the record
dressing, the Chebyshev propagator and the response, and imports nothing from
the repository.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import sys

import numpy as np
import scipy.sparse as sp
import sympy as smp
from mpmath import mp
from scipy.optimize import minimize_scalar
from scipy.special import jv

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


def fmt(xs, nd=3):
    return "/".join(("%." + str(nd) + "f") % x for x in xs)


PI = np.pi
G_FIELD = 1.0e-3                 # the weak-field knob; every response is d/dg at g = 0
FULL, ENERGY = (2.0, 1.0), (1.0, 1.0)
SIG = (32.0, 44.0)               # the two declared packet widths
T_HOP = 1.0                      # the toy's bare hopping
G_TOY = 0.4                      # the landed toy's own declared registration coupling
# The landed toy's own table, quoted for comparison (t = 1, g = 0.4).
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
    "A1 [exact] THE RULER FACTOR IS ONE DIMENSIONLESS PRODUCT. Dressing the bond amplitude by "
    "f(rho_rec)/f(rho_0) with rho_rec = rho_0 (1 + kappa Phi) gives bond weight "
    "1 + (1 + kappa nu) Phibar for a power law and 1 + kappa rho_0 f'(rho_0)/f(rho_0) Phibar for a "
    "GENERAL f -- only the log-derivative nu = dln f/dln rho_rec at the background enters. Against "
    "the declared family: alpha = 1 + kappa nu, beta = 1 (f is a bond object, the mass is a site "
    "term), bending factor alpha/beta = 1 + kappa nu, so alpha = 2 IFF kappa nu = 1 EXACTLY",
    pow_ok and gen_ok and two_iff,
)

# The sign structure: near a mass Phi < 0 and the ruler must shrink the bond amplitude.
fnum = smp.lambdify((Phib, kap, nu), (1 + kap * Phib) ** nu, "numpy")
s_bm = float(fnum(-0.1, -1.0, -1.0))     # B-: records denser near mass, denser records slower
s_bp = float(fnum(-0.1, +1.0, +1.0))     # B+: records sparser near mass, denser records faster
s_wrong = float(fnum(-0.1, -1.0, +1.0))  # kappa nu < 0: the dressing GROWS the amplitude
check(
    "A2 [exact] THE SIGN IS NOT THE PROBLEM. alpha = 1 + kappa nu exceeds the parent's 1 iff "
    "kappa nu > 0, and near a mass Phi < 0 the dressing f(rho_rec)/f(rho_0) must then SHRINK the "
    "bond amplitude further: at Phi = -0.1 branch B- (kappa < 0, records denser where the energy "
    "density is higher; nu < 0, denser records slower) gives %.4f and branch B+ (kappa > 0, nu > 0) "
    "gives %.4f, both below 1, while a product kappa nu < 0 gives %.4f, above 1. B- is the direction "
    "the landed optical-metric toy exhibits, so the qualitative sign comes out right"
    % (s_bm, s_bp, s_wrong),
    s_bm < 1.0 and s_bp < 1.0 and s_wrong > 1.0,
)


# =========================== B. THE LANDED 1D TOY'S OWN COEFFICIENT (exact + numerical)

def v_front(G2, t=T_HOP, K=200001):
    """Front speed of the landed toy's medium: eliminating the frozen record mode gives
    eps_eff(E) = g^2/E, hence E(k) = -t cos k + sqrt(t^2 cos^2 k + g^2) with the note's
    smooth-profile weight g(x)^2 = g0^2 n(x); v_F(n) = max_k |dE/dk|."""
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
    "B1 [numerical, 5e-4] THE LANDED TOY'S MEDIUM, REPRODUCED. v_F(n) = %s against the landed note's "
    "%s at n = 0, 1/8, 1/4, 1/2, 1 (exact at both ends; the intermediate gap is that note's own "
    "periodic-dilution-against-smooth-weight difference), strictly decreasing, so records SLOW the "
    "front and nu_toy < 0. The note's small-g law v_F = 2t - sqrt(2) g is reproduced: (2 - v_F)/g = "
    "%s at g = 0.02, 0.01, 0.005 against sqrt(2) = %.6f, so v_F is SQUARE-ROOT in the record density"
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
# An independent 40-digit confirmation that no G2 goes below -1/8.
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
    "B2 [exact + numerical, 1e-10] AND IT IS BOUNDED AT ONE EIGHTH. The toy's ruler exponent is a "
    "supplied dial in g0 and n, %.5f at its own strongest declared point (n = 1, g0 = 0.4). It is "
    "bounded, and the extremum is EXACT: at g0^2 n = 3/5 the front condition df/dc = 0 holds with "
    "cos k* = -1/sqrt 5 and v_F = 3/sqrt 5, and there nu = -1/8 exactly (sympy), confirmed at 40 "
    "digits to %.1e. A bounded float search over g0^2 n returns %.9f at %.6f, and a 40-digit sweep "
    "over 61 declared points finds nothing below -1/8. So this class supplies |nu| <= 1/8 and "
    "DEMANDS |kappa| >= 8"
    % (nu_at_1, abs(float(mp_at + mp.mpf(1) / 8)), _r.fun, float(np.exp(_r.x))),
    stat_ok and vF_ok and nu_ok and abs(_r.fun + 0.125) < 1e-6 and _r.fun > -0.1250001
    and abs(float(mp_at + mp.mpf(1) / 8)) < 1e-30 and mp_min >= -mp.mpf(1) / 8 - mp.mpf(10) ** -30,
)


# ================================ C. THE SEA'S OWN RECORD STATISTICS (exact + numerical)

def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a): eta_1 = 1, eta_2 = (-1)^{v_1},
    eta_3 = (-1)^{v_1+v_2}, the landed staggered kinetic-form clause read on 2Z^3."""
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
        """One-particle route: rho_rec(v) = <n_v> = (projector onto the sea)_vv."""
        w, U = np.linalg.eigh(self.hmat(m, Phi, ab))
        neg = w < -1e-12
        occ = np.einsum("ik,ik->i", U[:, neg], U[:, neg])
        zm = np.abs(w) <= 1e-12
        if int(np.sum(zm)):        # declared convention: each zero mode carries weight one half
            Zc = U[:, zm]
            occ = occ + 0.5 * np.einsum("ik,ik->i", Zc, Zc)
        return occ


CUBE = Box(2, 2, 3)                # 12 coarse sites, one qubit per site: dim 2^12 = 4096
NQ, NF = CUBE.V, CUBE.V // 2
BASIS = [b for b in range(4096) if bin(b).count("1") == NF]
POSN = {b: i for i, b in enumerate(BASIS)}
DIM = len(BASIS)                   # the half-filled sector, 924


def many_body_occ(m, Phi, ab):
    """EXACT half-filled ground state in the cube's 12-qubit space (Jordan-Wigner), and the
    Born odds <n_v> that site v's record registers occupied."""
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
    ev, EV = np.linalg.eigh(A)
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
    "C1 [numerical, 1e-9] THE OBJECT, COMPUTED TWICE. rho_rec(v) is the Born odds that site v's "
    "record registers occupied in the half-filled ground state. On the cube's 12-qubit space (12 "
    "coarse sites, dim 2^12 = 4096, half-filled sector %d, E0 = %.6f) the exact many-body value and "
    "the one-particle sea projector agree to %.1e, and at m = 0, Phi = 0 the record odds are flat at "
    "one half to %.1e -- the landed determinantal-sea value P_vv = 1/2 at every site"
    % (DIM, E0_cube, two_routes, flat),
    two_routes < 1e-9 and flat < 1e-12,
)

m0_rows = []
for ab in (ENERGY, FULL):
    for prof in (np.ones(CUBE.V), RAMP):
        o, _ = many_body_occ(0.0, 1e-3 * prof, ab)
        m0_rows.append(float(np.max(np.abs(o - 0.5))))
check(
    "C2 [exact + numerical, 1e-12] AT m = 0 THE RECORD DENSITY IS PINNED AT ONE HALF FOR EVERY Phi. "
    "Over a uniform and a ramp profile at both (1,1) and (2,1), max |rho_rec - 1/2| = %.1e: at m = 0 "
    "the Hamiltonian is pure hop on a bipartite graph WHATEVER the bond weights, so the sublattice "
    "grading eps_v = (-1)^(v1+v2+v3) with eps M eps = -M pins the odds site by site. kappa = 0 there "
    "identically, by symmetry and not by numerics, for every Phi profile and every (alpha, beta)"
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
    "C3 [numerical, 1e-12] AT m != 0 THE RESPONSE IS PURELY STAGGERED. Under a uniform Phi = 0.037 "
    "at (1,1) the record density is unchanged to %.1e, because H(1,1) = (1 + Phi) H0 exactly and "
    "every eigenvector is untouched. At (2,1) it does respond, %.2e, but the scalar (mean) part of "
    "that response is %.1e against a staggered part %.2e: it is the chiral-condensate readout "
    "m_eff = m (1 + Phi)/(1 + 2 Phi), odd under sublattice exchange, and not a density"
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
        rb = 0.5 * (d[SLAB.r] + d[SLAB.c])          # d rho_bar/dPhi on every bond
        Pb = 0.5 * (PHI_S[SLAB.r] + PHI_S[SLAB.c])
        kbond.append(float(np.dot(rb, Pb) / np.dot(Pb, Pb)) / 0.5)
        ksite.append(float(np.dot(d, PHI_S) / np.dot(PHI_S, PHI_S)) / 0.5)
        rmax.append(float(np.max(np.abs(rb))))
kmax = max(abs(x) for x in kbond)
check(
    "C4 [numerical, 1e-6] THE BOND NEIGHBOURHOOD -- WHAT A HOP RATE COULD SEE -- HAS NO LINEAR "
    "RESPONSE. On a 16 x 4 x 4 slab open in x with Phi = g (x - L/2), g = 1e-3, fitting rho_bar = "
    "(rho_v + rho_j)/2 = rho_0 (1 + kappa Phi) over 8 declared rows (m = 0, 0.5, 1, 2 at (1,1) and "
    "(2,1)): largest |kappa_bond| = %.2e and largest |kappa_site| = %.2e, while the POINTWISE "
    "response reaches %.2e. Required for alpha = 2 from the toy's own nu: |kappa| >= 8"
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
ksub = [float(np.dot(rb[epsb == s], Pb[epsb == s]) / np.dot(Pb[epsb == s], Pb[epsb == s])) / 0.5
        for s in (+1.0, -1.0)]
check(
    "C5 [numerical, 1e-6] WHAT SURVIVES IS A GRADIENT, ORTHOGONAL TO Phi ITSELF. Regressing the "
    "bond response at m = 1, (2,1) on {Phibar, eps, eps (Phi_v - Phi_j), 1} gives coefficients "
    "%.2e, %.2e, %.3e, %.2e: the whole surviving term is the STAGGERED GRADIENT one. And it is not "
    "a cancellation between sublattices -- fitting within each class separately gives kappa_bond = "
    "%.2e and %.2e. Every bond joins opposite sublattices, and a sublattice-balanced neighbourhood "
    "average annihilates an odd response exactly"
    % (co[0], co[1], co[2], co[3], ksub[0], ksub[1]),
    abs(co[0]) < 1e-6 and abs(co[2]) > 1e-3 and max(abs(x) for x in ksub) < 1e-6,
)

alpha_fed = smp.simplify((1 + kap * nu).subs(kap, 0))
check(
    "C6 [exact] FEEDING THE SEA'S OWN RESPONSE BACK GIVES alpha = 1 EXACTLY. With kappa = 0 the "
    "derived condition returns alpha = %s and bending factor 1 + 0 nu = 1 for EVERY f whatever, so "
    "on this vacuum no record-density dressing of the hop supplies the ruler factor: the miss is the "
    "whole unit of alpha, not a fraction of it. The statement is exactly this -- kappa = 0 on the "
    "half-filled sea of the cube by sublattice symmetry -- and it is bounded to that sea, that "
    "readout and first order in Phi" % alpha_fed,
    alpha_fed == 1,
)


# ================================================ D. THE TWO OBSTRUCTIONS (exact + stated)

m_eff = smp.simplify(m_ * (1 + b_ * c_) / (1 + a_ * c_))
const_ok = smp.simplify(m_eff.subs(b_, a_) - m_) == 0
d_meff = smp.simplify(smp.diff(m_eff, c_).subs(c_, 0))
price_ok = smp.simplify(d_meff.subs({a_: 2, b_: 1}) + m_) == 0
check(
    "D1 [exact] OBSTRUCTION (a), THE CONSTANT MODE, AND A PRICE OF THE DECLARED WEIGHT. The landed "
    "bridge delivers Phi only up to its constant mode, phi = G0 P0 rho with P0 projecting the "
    "constant off. At alpha = beta a constant shift Phi -> Phi + c is a PURE rescaling of H0 and the "
    "mass ratio is fixed; at alpha != beta it is not, d m_eff/dc = m (beta - alpha) = -m at (2,1), "
    "so a constant shift of Phi changes the rest mass at first order. The stipulation rho_rec = "
    "rho_0 (1 + kappa Phi) inherits the same non-invariance. Reported for PR #7905's owner",
    const_ok and price_ok,
)

# On the slab the discrete Laplacian of the linear profile vanishes in the interior, which is
# where the bending and free-fall rows of group E are computed.
lap = np.zeros(SLAB.V)
np.add.at(lap, SLAB.r, PHI_S[SLAB.c] - PHI_S[SLAB.r])
inner = (SLAB.xs > 0.5) & (SLAB.xs < SLAB.L[0] - 1.5)
lap_in = float(np.max(np.abs(lap[inner])))
check(
    "D2 [exact + stated] OBSTRUCTION (b), THE SOURCE IS NON-LOCAL. A record density set by the LOCAL "
    "energy density gives rho_rec - rho_0 proportional to rho_energy, and the landed bridge makes "
    "rho_energy proportional to the Laplacian of Phi, which on the declared linear profile -- the "
    "same profile every response row here uses -- is %.1e over the %d interior sites: it vanishes in "
    "vacuum, which is exactly where light bends and bodies fall. Only a response to Phi ITSELF gives "
    "a ruler factor, and Phi is the Green's-function integral of the energy density, not a local "
    "function of it"
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
        return self.vhop * (1.0 + Pb) * np.power(1.0 + kappa * Pb, nu_)

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
    "E1 [numerical, 0.35] THE DRESSED HAMILTONIAN IS THE DECLARED H(2,1) TO O(Phi^2). Over the five "
    "declared pairs (kappa, nu) = (8,1/8), (1,1), (-8,-1/8), (-1,-1), (2,1/2), all on kappa nu = 1, "
    "max |H_ruler - H(2,1)| = %s, and halving Phi divides each by %s against the 4 an O(Phi^2) "
    "residual gives. A control at kappa nu = 1/8 leaves %.3e, a FIRST-order mismatch that does not "
    "vanish. So the product, and nothing else about f, is what the mechanism needs"
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


def response(m, psi0, mk, mkC, amax, gfield, T=6.0, dt=0.5):
    """The EXACT Ehrenfest acceleration response, first order in g, by central difference."""
    rec = {}
    nt = int(round(T / dt))
    for sg in (+1.0, -1.0):
        Phi = sg * gfield * L.Phi1
        H, Cx = mk(m, Phi), mkC(Phi)
        B = bound(m, np.max(np.abs(Phi)), amax)
        psi = psi0.copy()
        ax = []
        for it in range(nt + 1):
            ax.append(-2.0 * np.vdot(H.dot(psi), Cx.dot(psi)).real)
            if it < nt:
                psi = cheb_evolve(H, psi, dt, B)
        rec[sg] = np.array(ax)
    return float(((rec[1.0] - rec[-1.0]) / (2 * gfield)).mean())


def richardson(a32, a44, s1=SIG[0], s2=SIG[1]):
    """Richardson in 1/sigma_x^2: the delta p_x ~ 2/sigma_x systematic is O(1/sigma_x^2)."""
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
    "E2 [extrapolated] THE MECHANISM IS FAITHFUL IF THE PRODUCT IS GRANTED. On the 192 x 16 x 4 "
    "slab, acceleration the exact Ehrenfest expectation differenced centrally in g = 1e-3 and never "
    "fitted, Richardson-extrapolated in 1/sigma_x^2 from sigma_x = 32, 44: the record-dressed H at "
    "the declared kappa = nu = -1 gives rest %.5f and massless %.5f, BENDING FACTOR %.4f, against "
    "the declared H(2,1)'s %.5f/%.5f/%.4f and the undressed parent H(1,1)'s %.5f/%.5f/%.4f. Free "
    "fall stays at -4 beta = -4 and the bending factor is 2"
    % (r_rul[0], r_rul[1], r_rul[2], r_dec[0], r_dec[1], r_dec[2], r_par[0], r_par[1], r_par[2]),
    abs(r_rul[2] - 2.0) < 0.03 and abs(r_rul[0] + 4.0) < 0.05 and abs(r_par[2] - 1.0) < 0.03
    and abs(r_rul[0] - r_dec[0]) < 0.05 and abs(r_rul[1] - r_dec[1]) < 0.15,
)

r_r8 = scheme_rows(lambda m, P: L.HRuler(m, P, KAP8, NU8),
                   lambda P: L.CxRuler(P, KAP8, NU8), 2.0, G_FIELD)
r_r8s = scheme_rows(lambda m, P: L.HRuler(m, P, KAP8, NU8),
                    lambda P: L.CxRuler(P, KAP8, NU8), 2.0, 2.5e-4)
check(
    "E3 [numerical] AT THE TOY'S OWN BOUND THE DRESSING IS NONLINEAR WHERE THE WEIGHT IS LINEAR. At "
    "kappa = -8, the smallest |kappa| the toy's |nu| <= 1/8 allows, the dressing's expansion "
    "parameter is kappa Phi ~ %.2f rather than Phi ~ %.2f, and the bending factor overshoots to "
    "%.4f (rest %.5f, massless %.5f). Reducing g to 2.5e-4 recovers rest %.5f, massless %.5f, "
    "bending %.4f. That is a genuine price of a small nu, and it is reported, not absorbed"
    % (abs(KAP8) * G_FIELD * np.max(np.abs(L.Phi1)), G_FIELD * np.max(np.abs(L.Phi1)),
       r_r8[2], r_r8[0], r_r8[1], r_r8s[0], r_r8s[1], r_r8s[2]),
    r_r8[2] > 2.1 and abs(r_r8s[2] - 2.0) < 0.03,
)

print(
    "SUMMARY: the ruler factor PR #7905 named reduces exactly to one dimensionless product, "
    "kappa nu = 1, for every f; the landed optical-metric toy fixes the sign and caps |nu| at 1/8, "
    "so that class demands |kappa| >= 8; and the half-filled sea, computed exactly in the cube's "
    "12-qubit space and again by the one-particle projector, supplies kappa = 0 by sublattice "
    "symmetry, so on this vacuum alpha = 1 exactly and the miss is the whole unit. Granted the "
    "product, the mechanism is faithful. What is still open: the rate at which records form, which "
    "the axioms do not supply, and a vacuum other than the half-filled sea."
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
