#!/usr/bin/env python3
"""A formation-rate ruler evades the sea's sublattice cancellation, and the
bridge's constant mode fixes kappa_r = 1.

Class-A runner.  Conditional on exactly what the spatial-metric note (PR #7905)
is conditional on -- the designed fermion law, the landed weak-field response
surface phi = G0 P0 rho, the choice of the half-filled staggered sea as the
vacuum, and that note's own DECLARED two-weight family

    H(alpha, beta) = sum_bonds [1 + alpha (Phi_v + Phi_j)/2] M_vj
                   + sum_v     [1 + beta  Phi_v]            m eps_v n_v

-- plus five STIPULATIONS made here and derived from nothing: (F1) a record
formation rate r_v at a coarse corner is a supplied law-level quantity,
axiom-legal in kind; (F2) r_v = r_0 (1 + kappa_r Phi_v), or r_v tracking the
sea's own local energy density; (F3) the coarse bond amplitude is dressed by
g(r_v, r_j)/g(r_0, r_0) with g symmetric and homogeneous of degree nu_r;
(F4) the parent's energy-density coupling stands, so the bond already carries
one unit of Phi and the dressing multiplies only the bond, the mass being a
site term; (F5) the background is the half-filled staggered sea, one-particle
sector, first order in Phi.

The record-density note (PR #7916) computed the record-density reading of this
named interface on this vacuum and reported it negative: the sea's record
density responds to Phi only through a staggered part, and every coarse bond
joins opposite sublattices, so the bond average annihilates it.  That note named
a formation-rate dependence as untouched and left it open.  This runner takes
that named interface.  A formation rate is a site quantity EVEN under sublattice exchange,
so the bond average that annihilated the record density leaves it alone.

  A  (T1)  THE FIRST-ORDER CONDITION AND WHY THERE IS NO CANCELLATION.
           alpha = 1 + kappa_r nu_r and beta = 1 for EVERY symmetric dressing
           homogeneous of degree nu_r (Euler); AM - GM is exactly a tidal term;
           the sublattice decomposition theorem; and the two site quantities
           side by side on one slab and one field.
  B  (T2)  THE CONSTANT MODE FIXES kappa_r.  The bending factor is independent
           of the constant mode the bridge removes iff kappa_r = 1; with
           kappa_r nu_r = 1 the unique solution is (kappa_r, nu_r) = (1, 1).
  C  (T3)  THE CORRECTION TO PR #7916.  The sea's OWN local energy density is
           nonzero everywhere and responds with K(alpha) = alpha (1 - w_m) +
           beta w_m, exactly 1 at the parent's coupling.  The Laplacian clause
           holds for the matter source density, not for this object.
  D  (T4)  SELF-CONSISTENCY AND ITS TWO PRICES.  The rate loop closes at first
           order and the state-level fixed point is a contraction; the
           self-consistent exponent is vacuum-mass-dependent, and the dressing
           shifts the sea's energy density at first order -- a Phi-linear
           vacuum energy that feeds back on the potential through the bridge.
  E  (T5)  WAVEPACKETS AT (1, 1).  Bending factor, universal slow-body free
           fall, and the O(Phi^2) mismatch scaling, on the 192 x 16 x 4 slab.
  F  (T6)  THE LOCAL READING OF THE MINIMAL TIME STEP.  a_tau(v) = 1/((1 +
           Phi_v) M_Pl c) gives r_v = r_0 (1 + Phi_v): the right sign and
           exactly one unit, the same value B forces.  A NAMED OPEN BRIDGE
           only: both min-time-step notes are unaudited and the companion is an
           open gate whose own boundary forbids citation for clock-rate
           normalisation.  This check verifies the arithmetic of the reading
           and nothing about its authority.

Groups A, B, D's algebra and F are exact identities, checked symbolically;
every other group is a finite floating-point computation reporting its residual
against a tolerance declared before the run.  The acceleration of group E is
never fitted: it is the exact Ehrenfest expectation a(t) = -<[H,[H,X]]>,
differenced centrally in g so that the g-independent part cancels exactly, and
Richardson-extrapolated in 1/sigma_x^2 from the two declared packet widths.
No random number is drawn anywhere: every momentum, mass, width, weight pair,
coupling, exponent and profile is a declared constant, so the runner is
bit-reproducible without a seed.

Largest dense object: the 924-dimensional half-filled sector of the coarse
cube's 12-qubit space (dim 2^12 = 4096); nothing above 4096 x 4096 is formed.
The 192 x 16 x 4 slab of group E is sparse and matrix-free throughout.

This runner is self-contained: it re-declares the coarse lattice, the KS sign
field, the record-native staggered mass, the two-weight family, the rate
dressings, the local energy density, the Chebyshev propagator and the response,
and imports nothing from the repository.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""
from __future__ import annotations

import sys

import numpy as np
import scipy.sparse as sp
import sympy as smp
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
GS_SMALL = 2.5e-4                # the reduced field of the O(Phi^2) scaling row
FULL, ENERGY = (2.0, 1.0), (1.0, 1.0)
SIG = (32.0, 44.0)               # the two declared packet widths
MASSES_K = (0.0, 0.3, 0.9, 2.0, 6.0)
ALPHAS_K = (1.0, 1.5, 2.0, 3.0)


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
        """rho_rec(v) = <n_v>; E_v the normal-ordered local energy density; its split."""
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


# ============================== A (T1). THE FIRST-ORDER CONDITION, AND NO CANCELLATION

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
    "A1 [exact] AM DRESSING. (1 + Phibar)((r_v + r_j)/2r_0)^nu_r with r_v = r_0 (1 + kappa_r Phi_v) "
    "is 1 + (1 + kappa_r nu_r) Phibar + O(Phi^2): alpha = 1 + kappa_r nu_r, beta = 1 (the mass is a "
    "site term the dressing does not touch), so ALPHA = 2 IFF kappa_r nu_r = 1 EXACTLY",
    smp.simplify(lin_am - want) == 0,
)
check(
    "A2 [exact] GM DRESSING IS IDENTICAL AT FIRST ORDER. (sqrt(r_v r_j)/r_0)^nu_r gives the same "
    "1 + (1 + kappa_r nu_r) Phibar: the choice of mean is invisible, and kappa_r is one number for "
    "both dressings",
    smp.simplify(lin_gm - want) == 0,
)
dq = smp.simplify(smp.expand(q_am - q_gm))
pred = nu * kap ** 2 * (Pv - Pj) ** 2 / 8
check(
    "A3 [exact] AM - GM = (nu_r kappa_r^2/8)(Phi_v - Phi_j)^2 EXACTLY, a pure squared bond gradient "
    "vanishing on any uniform Phi: the two dressings are one ruler up to a tidal term",
    smp.simplify(dq - pred) == 0,
)

# A general symmetric dressing homogeneous of degree nu: Euler forces the same answer.
A_, B_ = smp.symbols("A B", positive=True)
gen_ok = []
for p in (1, 2, 3):
    x, y = 1 + kap * Pv, 1 + kap * Pj
    g = (A_ * x ** p + A_ * y ** p + B_ * (x * y) ** (smp.Rational(p, 2))) / (2 * A_ + B_)
    gen_ok.append(smp.simplify(lin_quad(BASE * g ** (nu / p))[0] - want) == 0)
W_odd = BASE * (((1 + kap * Pv) ** nu + (1 + kap * Pj) ** nu) / 2)    # not a mean at all
gen_ok.append(smp.simplify(lin_quad(W_odd)[0] - want) == 0)
check(
    "A4 [exact] ONLY THE DEGREE ENTERS. For power means p = 1, 2, 3 with arbitrary weights A, B and "
    "for the non-mean (r_v^nu + r_j^nu)/2r_0^nu the first-order coefficient is nu_r kappa_r Phibar "
    "in every case, by Euler's theorem: the dressing's functional form is not a free choice",
    all(gen_ok),
)

S_v, S_j, T_v, T_j, ev = smp.symbols("S_v S_j T_v T_j epsilon_v", real=True)
bond_avg = ((S_v + ev * T_v) + (S_j - ev * T_j)) / 2      # a bond joins opposite sublattices
check(
    "A5 [exact] SUBLATTICE DECOMPOSITION THEOREM. Every coarse bond joins opposite sublattices, so "
    "the bond average of dA_v = S_v + eps_v T_v is Sbar + eps_v (T_v - T_j)/2: the STAGGERED part "
    "survives only as a gradient, the EVEN part in full. A C-even site quantity has T = 0 and "
    "nothing to cancel -- the record-density obstruction is absent by construction",
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
    "A6 [numerical, 1e-9] THE BOND AVERAGE ANNIHILATES ONE AND KEEPS THE OTHER. 16x4x4 slab, "
    "Phi = g(x - L/2), g = 1e-3, interior bonds: the RECORD density's bond response is <= %.1e, its "
    "site response purely staggered (up to %.3f); the ENERGY density's is >= %.4f, staggered part "
    "%.1e" % (kap_rec, max(abs(r[3]) for r in tab), K_min, stag_e),
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
    "A7 [numerical, 2e-3] THE TIDAL TERM ON THE SLAB. On 192x16x4, H_AM - H_GM matches "
    "(nu_r kappa_r^2/8)(Phi_v - Phi_j)^2 x (bond) to relative %.1e, and %.1e at half the field"
    % (amgm[0], amgm[1]),
    amgm[0] < 2e-3,
)


# ================================== B (T2). THE CONSTANT MODE FIXES kappa_r = 1

lnWb_am = smp.log(1 + Pb) + nu * smp.log(1 + kap * Pb)
lnWb_gm = smp.log(1 + Pb) + (nu / 2) * (smp.log(1 + kap * Pv) + smp.log(1 + kap * Pj))
lnWm = smp.log(1 + Pv)
bend = {}
for tag, lw in (("AM", lnWb_am), ("GM", lnWb_gm)):
    num = (smp.diff(lw, Pv) + smp.diff(lw, Pj)).subs({Pv: cc, Pj: cc})
    bend[tag] = smp.simplify(num / smp.diff(lnWm, Pv).subs({Pv: cc}))
pred_b = 1 + nu * kap * (1 + cc) / (1 + kap * cc)
check(
    "B1 [exact] THE CONSTANT MODE. phi = G_0 P_0 rho delivers Phi only modulo a constant c; around "
    "Phi = c + phi the bending factor is 1 + nu_r kappa_r (1 + c)/(1 + kappa_r c) for BOTH dressings, "
    "with d/dc at 0 equal to nu_r kappa_r (1 - kappa_r), vanishing on kappa_r nu_r = 1 IFF "
    "kappa_r = 1. The price the record-density route could not pay is paid at one point",
    smp.simplify(bend["AM"] - pred_b) == 0 and smp.simplify(bend["GM"] - pred_b) == 0
    and smp.simplify(smp.diff(pred_b, cc).subs(cc, 0) - nu * kap * (1 - kap)) == 0
    and smp.simplify((nu * kap * (1 - kap)).subs(nu, 1 / kap)) == smp.simplify(1 - kap),
)
sols = smp.solve([smp.Eq(kap * nu, 1), smp.Eq(nu * kap * (1 - kap), 0)], [kap, nu], dict=True)
check(
    "B2 [exact] UNIQUENESS. {kappa_r nu_r = 1, constant-mode invariance} has the single solution "
    "(kappa_r, nu_r) = (1, 1): %s. The supplied object shrinks to one exponent, nu_r = 1 -- the hop "
    "amplitude proportional to the FIRST power of the rate" % str(sols),
    len(sols) == 1 and sols[0][kap] == 1 and sols[0][nu] == 1,
)


# =============== C (T3). THE SEA'S OWN LOCAL ENERGY DENSITY, AND THE CORRECTION

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
    "C1 [numerical, 1e-8] THE LOCAL ENERGY DENSITY SUMS TO THE ENERGY. E_v := sum_j H_vj (rho - "
    "1/2)_jv on the coarse cube (2x2x3, dim 2^12 = 4096, half-filled sector 924) at m = 0.7, ramp "
    "Phi, (2,1): sum_v E_v matches the exact many-body ground-state energy to %.1e and the record "
    "odds <n_v> to %.1e" % (d_E, d_occ),
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
    "C2 [numerical, 1e-9] THE CORRECTION TO PR #7916, WHOSE LAPLACIAN CLAUSE HOLDS FOR THE MATTER "
    "SOURCE DENSITY. The sea's OWN local energy density is nonzero everywhere: 4x4x4 periodic sea, "
    "m = 0.9, UNIFORM Phi, H(1,1) = (1 + Phi) H_0 exactly, so d ln|E_v|/dPhi = %.10f at every site "
    "(site spread of |E_v| itself %.1e) -- the record density registers zero here, this one one full "
    "unit" % (float(K11.mean()), uni),
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
    "C3 [numerical, 2e-6] K(alpha) IS A WEIGHTED MEAN OF THE TWO COUPLINGS. With w_m = E_mass/E, "
    "K(alpha) := d ln|E_v|/dPhi = alpha (1 - w_m) + beta w_m over m = 0, 0.3, 0.9, 2, 6 and "
    "alpha = 1, 1.5, 2, 3 to max error %.1e (Feynman-Hellmann: m dE/dm = E_mass). It lies strictly "
    "between beta = 1 and alpha" % errK,
    errK < 2e-6,
)
print("   w_m/K at alpha 2: " + " ".join(
    "%.1f:%.4f/%.4f" % (r[0], r[2], r[3]) for r in rows_K if r[1] == 2.0))


# ========================= D (T4). SELF-CONSISTENCY, AND THE TWO NAMED PRICES

nur, wm_s, al = smp.symbols("nu_r w_m alpha", real=True)
Kex = al - (al - 1) * wm_s
fix = smp.solve(smp.Eq(al, 1 + nur * Kex), al)[0]
nu_need = smp.simplify(smp.solve(smp.Eq(fix, 2), nur)[0])
check(
    "D1 [exact] THE STATE-LEVEL READING DERIVES kappa_r, AND THE SUPPLIED NUMBER BECOMES nu_r. With "
    "kappa_r = K(alpha) and alpha = 1 + nu_r kappa_r, alpha* = %s and alpha* = 2 iff nu_r = %s. "
    "FIRST PRICE: that exponent is vacuum-mass-dependent, 1/2 massless to 1 heavy, not universal"
    % (smp.simplify(fix), nu_need),
    smp.simplify(fix - (1 + nur * wm_s) / (1 - nur * (1 - wm_s))) == 0
    and smp.simplify(nu_need - 1 / (2 - wm_s)) == 0,
)
slope = smp.simplify(smp.diff(1 + nur * Kex, al).subs(nur, 1 / (2 - wm_s)))
check(
    "D2 [exact] THE LOOP IS A CONTRACTION AT alpha = 2: the map alpha -> 1 + nu_r K(alpha) has slope "
    "%s at nu_r = 1/(2 - w_m), below 1/2 for every w_m in [0, 1]. At nu_r = 1 the slope is 1 - w_m, "
    "exactly 1 on a massless sea, where the map has no fixed point: the two readings do not agree, "
    "and the tension is reported rather than absorbed" % slope,
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
    "D3 [numerical, 1e-5] THE FIXED POINT BY ITERATION. alpha <- 1 + nu_r K_computed(alpha) from "
    "alpha = 1 on the 4x4x4 periodic sea at nu_r = 1/(2 - w_m) converges to alpha = 2 to %.1e at "
    "every mass tested, with kappa_r = K(2) = 2 - w_m" % err_fp,
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
    "D4 [numerical, 0.4] THE RATE LOOP CLOSES AT FIRST ORDER. max_v |E_v[H_rate(1,1)] - E_v[H(2,1)]| "
    "is %.3e at g = 4e-3 and %.3e at g = 2e-3, ratio %.2f against the 4 an O(Phi^2) residual gives"
    % (d1[0], d1[1], d1[0] / d1[1]),
    abs(d1[0] / d1[1] - 4.0) < 0.4,
)
d2 = [float(Kof(1.0, 2.0)[0].mean() - Kof(1.0, 1.0)[0].mean()), float(1.0 - wm_of(1.0)[0].mean())]
check(
    "D5 [numerical, 1e-6] SECOND PRICE: A Phi-LINEAR VACUUM ENERGY. Against the bare hop the dressing "
    "shifts d ln|E_v|/dPhi by %.6f, matching the exact (alpha - 1)(1 - w_m) = %.6f. Through "
    "phi = G_0 P_0 rho that is a feedback on the potential, Laplacian Phi ~ -(rho_matter + "
    "K E^0 Phi): a named price excluded by boundary, with no G_Newton to size it" % (d2[0], d2[1]),
    abs(d2[0] - d2[1]) < 1e-6 and d2[0] > 0.5,
)


# ========================================= E (T5). WAVEPACKETS AT (kappa_r, nu_r) = (1, 1)

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
    "E1 [numerical, 0.35] EVERY POINT ON kappa_r nu_r = 1 IS H(2,1) TO O(Phi^2). On 192x16x4 the "
    "residual against the declared H(2,1) quarters for (1,1), (2,1/2) and (1/2,2), both means: "
    "ratios %s. A control at kappa_r nu_r = 1/2 leaves %.3e, a FIRST-order mismatch that does not "
    "vanish" % (fmt([r[2] for r in rows], 2), ctl),
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
        B = bnd(m, np.max(np.abs(Phi)), amax)
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
print("   rest/massless/bending: " + " | ".join(
    "%s %.5f %.5f %.4f" % (k_, v_[0], v_[1], v_[2]) for k_, v_ in SCH.items()))
check(
    "E2 [extrapolated] BENDING FACTOR 2 FROM A FORMATION-RATE RULER. Exact Ehrenfest "
    "a = -<[H,[H,X]]>, differenced in g = 1e-3, Richardson in 1/sigma_x^2 from sigma_x = 32, 44: the "
    "rate-dressed H at (1,1) gives %.4f (AM) and %.4f (GM), the declared H(2,1) %.4f, the undressed "
    "parent H(1,1) %.4f, and the state-level massless point (2, 1/2) %.4f"
    % (SCH["rate AM (1,1)"][2], SCH["rate GM (1,1)"][2], SCH["declared H(2,1)"][2],
       SCH["parent H(1,1)"][2], SCH["rate AM (2,1/2)"][2]),
    all(abs(SCH[k][2] - 2.0) < 0.03 for k in ("rate AM (1,1)", "rate GM (1,1)", "rate AM (2,1/2)"))
    and abs(SCH["parent H(1,1)"][2] - 1.0) < 0.03,
)

ffr = {mm: rest_row(RATE_MK[0], RATE_MK[1], 2.0, mm) for mm in (0.5, 2.0)}
ffd = {mm: rest_row(DECL_MK[0], DECL_MK[1], 2.0, mm) for mm in (0.5, 2.0)}
ffr[1.0], ffd[1.0] = SCH["rate AM (1,1)"][0], SCH["declared H(2,1)"][0]
spread = max(ffr.values()) - min(ffr.values())
gap = max(abs(ffr[mm] - ffd[mm]) for mm in ffr)
check(
    "E3 [extrapolated, 0.09] UNIVERSAL SLOW-BODY FREE FALL. Rate-dressed rest acceleration "
    "%.5f/%.5f/%.5f at m = 0.5/1/2, spread %.4f about -4 beta = -4, against the declared H(2,1)'s "
    "%.5f/%.5f/%.5f on the same packets (max gap %.4f); the m = 0.5 row is the delta p_x ~ 2/sigma_x "
    "packet systematic, the outlier in BOTH schemes alike"
    % (ffr[0.5], ffr[1.0], ffr[2.0], spread, ffd[0.5], ffd[1.0], ffd[2.0], gap),
    all(abs(x + 4.0) < 0.09 for x in ffr.values()) and spread < 0.09 and gap < 0.07,
)

sc_small = scheme_rows(RATE_MK[0], RATE_MK[1], 2.0, GS_SMALL)
de_small = scheme_rows(DECL_MK[0], DECL_MK[1], 2.0, GS_SMALL)
e_big = abs(SCH["rate AM (1,1)"][2] - SCH["declared H(2,1)"][2])
e_sml = abs(sc_small[2] - de_small[2])
PMAX = G_FIELD * np.max(np.abs(L.Phi1))
check(
    "E4 [numerical, 2.0] THE MISMATCH IS O(Phi^2) AND SCALES AWAY. |bending(rate) - "
    "bending(declared)| at the SAME field is %.5f at g = 1e-3 (max|Phi| = %.3f) and %.5f at "
    "g = 2.5e-4 (%.4f), a reduction of %.2f for a field cut by 4; small-field bending %.4f against "
    "%.4f. At (1,1) the expansion parameter is Phi itself, %.3f, not kappa_r Phi"
    % (e_big, PMAX, e_sml, GS_SMALL * np.max(np.abs(L.Phi1)),
       e_big / max(e_sml, 1e-12), sc_small[2], de_small[2], PMAX),
    e_sml < e_big and e_big / max(e_sml, 1e-12) > 2.0,
)


# ============ F (T6). THE LOCAL READING OF THE MINIMAL TIME STEP -- A NAMED OPEN BRIDGE

Ph_s, MPl, c_s = smp.symbols("Phi_v M_Pl c", positive=True)
a_tau = 1 / ((1 + Ph_s) * MPl * c_s)              # the LOCAL reading, stipulated here
a_tau0 = 1 / (MPl * c_s)                          # the notes' single global scale reference
ratio = smp.simplify((1 / a_tau) / (1 / a_tau0))  # r_v / r_0 in coordinate time
kappa_read = smp.simplify(smp.diff(ratio, Ph_s).subs(Ph_s, 0))
slower = float(ratio.subs(Ph_s, smp.Rational(-1, 10)))     # near a mass Phi < 0
check(
    "F1 [exact] THE LOCAL READING GIVES EXACTLY ONE UNIT -- A NAMED OPEN BRIDGE. The min-time-step "
    "notes tie the tick to ONE GLOBAL scale reference with no local-energy notion. A LOCAL reading "
    "a_tau(v) = 1/((1 + Phi_v) M_Pl c) gives r_v/r_0 = %s, so kappa_r = %s exactly -- one unit, the "
    "value B2 forces -- and %.4f at Phi = -0.1, so records register more slowly near a mass. BOTH "
    "NOTES UNAUDITED, THE COMPANION AN OPEN GATE FORBIDDING CITATION FOR CLOCK-RATE NORMALISATION: "
    "an open bridge, never evidence; the axioms supply no formation rate"
    % (str(ratio), str(kappa_read), slower),
    smp.simplify(ratio - (1 + Ph_s)) == 0 and kappa_read == 1 and slower < 1.0,
)

print(
    "SUMMARY: a formation rate is a sublattice-EVEN site quantity, so the bond average that "
    "annihilated the record density's response leaves it untouched; the ruler condition is "
    "kappa_r nu_r = 1 for every symmetric dressing homogeneous of degree nu_r, only the degree "
    "entering; the sea's own local energy density responds with alpha (1 - w_m) + beta w_m, one at "
    "the parent's coupling, correcting PR #7916's clause, which holds for the matter source "
    "density; and constant-mode invariance forces (kappa_r, nu_r) = (1, 1) uniquely, leaving one "
    "supplied exponent. Two prices are named: a vacuum-mass-dependent self-consistent exponent, and "
    "a Phi-linear vacuum energy that feeds back on the potential."
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
