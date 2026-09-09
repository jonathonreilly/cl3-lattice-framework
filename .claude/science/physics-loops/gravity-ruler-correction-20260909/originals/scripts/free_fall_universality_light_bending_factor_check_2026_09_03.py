#!/usr/bin/env python3
"""Universality of free fall and the light-bending factor under the energy-density coupling.

Class-A runner. Conditional on exactly what the energy-product note is
conditional on -- the designed fermion law, the landed weak-field response
surface phi = G0 P0 rho, and the choice of the half-filled staggered sea as
the vacuum -- plus one STIPULATION made here and derived from nothing: a weak
external potential Phi couples to the total energy density of the one-particle
state, H_Phi = H0 + sum_v Phi_v eps^tot_v.  This runner establishes:

  A  THE COUPLING.  The KS hop and the record-native staggered mass; the
     dispersion E^2 = 6 + 2 sum_a cos q_a + m^2; that the stipulated H_Phi is
     EXACTLY the bond-scaled form M_vj (1 + (Phi_v + Phi_j)/2) plus
     m eps_v (1 + Phi_v); that the conjugated form A H0 A, A = sqrt(1 + Phi),
     differs from it only at O(g^2); and the coarse-site light speed c_L = 2.
  B  THE ACCELERATION LAW.  a_x/g = -4 w E''_xx + 4 E'_x w'_x, exact on the
     lattice, with the weight w = E (energy coupling), E_0^2/E (the parent's
     eps_v taken verbatim, hop only) and 1 (the count source); and its two
     exact corollaries, transverse -4 and massless longitudinal +4.
  C  UNIVERSALITY, NUMERICALLY.  The delta p_x systematic and the Richardson
     extrapolation in 1/sigma_x^2; a/g = -4.000 +- 0.001 across mass and
     velocity; the light-bending factor; the composition test; the count
     control; and the test-body law verified dynamically as d<H0>/dt = -E g v_x.
  D  THE FORK IN eps_v.  The parent's energy density taken verbatim is a HOP
     density and gives no free fall at rest; the mass density must be added.
  E  VELOCITY DEPENDENCE.  Transverse acceleration velocity-independent, no
     (1 + v^2); longitudinal factor (1 - 2 v^2/c^2).

Groups A and B and the two corollaries are exact algebra checked at machine
tolerance; group C, D and E's dynamical rows are finite floating-point
computations reporting residuals against tolerances declared before the run.
The acceleration is never fitted: it is the exact Ehrenfest expectation
a(t) = -<[H_Phi,[H_Phi,X]]>, differenced centrally in g so that the
g-independent part cancels exactly.  Wavepacket widths, and the Richardson
extrapolation in 1/sigma_x^2 that removes the named systematic, are the only
places a finite state enters, and both are reported.

This runner is self-contained: it re-declares the coarse lattice, the KS sign
field, the mass term, the three candidate source densities, the Chebyshev
propagator and the response, and imports nothing from the repository.

Output: one PASS/FAIL line per check and a final `TOTAL: PASS=N FAIL=M`.
Exit code 0 iff FAIL = 0.
"""

from __future__ import annotations

import itertools
import sys

import numpy as np
import scipy.sparse as sp
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


PI = np.pi
EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
G = 1.0e-3                      # the weak-field knob; every response is d/dg at g = 0

# Quoted before the run and used as tolerances; the run fits nothing.
# The universal value is -c_L^2 with c_L = 2 the coarse-site light speed.
UNIVERSAL = -4.0
GR_BENDING_FACTOR = 2.0         # general relativity's, for the comparison only


# ============================================ the coarse lattice and its operators

def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a): eta_1 = 1, eta_2 = (-1)^{v_1},
    eta_3 = (-1)^{v_1+v_2}, the landed staggered kinetic-form clause read on 2Z^3."""
    if a == 0:
        return 1
    if a == 1:
        return -1 if (v[0] & 1) else 1
    return -1 if ((v[0] + v[1]) & 1) else 1


class Slab:
    """Coarse slab Lx x Ly x Lz, OPEN in x (the gradient direction), periodic in y, z."""

    def __init__(self, Lx, Ly, Lz):
        self.Lx, self.Ly, self.Lz = Lx, Ly, Lz
        self.V = Lx * Ly * Lz
        ix, iy, iz = np.meshgrid(np.arange(Lx), np.arange(Ly), np.arange(Lz), indexing="ij")
        self.xs = ix.ravel().astype(float)
        self.ys = iy.ravel().astype(float)
        self.zs = iz.ravel().astype(float)
        self.sgn = (-1.0) ** (ix + iy + iz).ravel()      # eps_v, the STAGGERING SIGN
        r, c, val, dx, dy = [], [], [], [], []

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
                                continue                  # OPEN in x
                        else:
                            w[ax] %= (Ly if ax == 1 else Lz)
                        j = idx(*w)
                        s = float(eta_ks(v, ax))
                        r += [i, j]
                        c += [j, i]
                        val += [s, s]
                        d = [0.0, 0.0, 0.0]
                        d[ax] = 1.0
                        dx += [d[0], -d[0]]
                        dy += [d[1], -d[1]]
        self.r = np.array(r)
        self.c = np.array(c)
        self.vhop = np.array(val)
        self.dxb = np.array(dx)
        self.dyb = np.array(dy)

    def _coo(self, vals):
        return sp.csr_matrix((vals, (self.r, self.c)), shape=(self.V, self.V))

    def H0(self, m):
        """H0 = M + m Eps, the KS hop plus the record-native staggered mass."""
        return (self._coo(self.vhop) + sp.diags(m * self.sgn)).tocsr()

    def bonds(self, Phi, coupling):
        """The bond factor of H_Phi for each source density."""
        if coupling == "aha":
            A = np.sqrt(1.0 + Phi)
            return self.vhop * A[self.r] * A[self.c]
        if coupling in ("tot", "hop"):
            return self.vhop * (1.0 + 0.5 * (Phi[self.r] + Phi[self.c]))
        return self.vhop

    def HPhi(self, m, Phi, coupling):
        """H_Phi = H0 + sum_v Phi_v (source density)_v, regrouped exactly.

        'tot' eps^tot_v = eps^hop_v + m eps_v n_v (the TOTAL energy density)
        'hop' eps^hop_v alone (the parent note's eps_v taken verbatim)
        'num' n_v = |psi_v|^2 (the count source)
        'aha' A H0 A with A = diag(sqrt(1 + Phi)) -- the conjugated form
        """
        diag = m * self.sgn.copy()
        if coupling in ("tot", "aha"):
            diag = diag * (1.0 + Phi)
        elif coupling == "num":
            diag = diag + Phi
        return (self._coo(self.bonds(Phi, coupling)) + sp.diags(diag)).tocsr()

    def Cx(self, Phi, coupling):
        """C = [H_Phi, X], sparse; only hop entries survive because X is diagonal."""
        return self._coo(self.bonds(Phi, coupling) * self.dxb)

    def Cy(self, Phi, coupling):
        return self._coo(self.bonds(Phi, coupling) * self.dyb)


def bound(m, Phimax):
    """Gershgorin bound on the spectrum of H_Phi."""
    return 6.0 * (1.0 + abs(Phimax)) + abs(m) * (1.0 + abs(Phimax)) + 0.05


def cheb_evolve(H, psi, dt, B):
    """exp(-i H dt) psi by Chebyshev expansion; spectrum inside [-B, B]."""
    th = B * dt
    N = int(th + 25 + 4 * th ** (1.0 / 3.0))
    n = np.arange(N + 1)
    cf = (2.0 - (n == 0)) * (-1j) ** n * jv(n, th)
    N = int(np.where(np.abs(cf) > 1e-16)[0].max())
    t0 = psi
    t1 = H.dot(psi) / B
    out = cf[0] * t0 + cf[1] * t1
    for k in range(2, N + 1):
        t2 = 2.0 * (H.dot(t1) / B) - t0
        out = out + cf[k] * t2
        t0, t1 = t1, t2
    return out


def cheb_apply(H, psi, f, B, N=700, K=4096):
    """f(H) psi by Chebyshev expansion of f on [-B, B]."""
    th = PI * (np.arange(K) + 0.5) / K
    xs = np.cos(th)
    fv = f(B * xs)
    cf = np.array([(2.0 - (n == 0)) / K * np.sum(fv * np.cos(n * th)) for n in range(N + 1)])
    t0 = psi
    t1 = H.dot(psi) / B
    out = cf[0] * t0 + cf[1] * t1
    for k in range(2, N + 1):
        t2 = 2.0 * (H.dot(t1) / B) - t0
        out = out + cf[k] * t2
        t0, t1 = t1, t2
    return out


def disp(p, m):
    """E(pi + p)^2 = sum_a (2 - 2 cos p_a) + m^2, the exact lattice dispersion."""
    return np.sqrt(sum(2.0 - 2.0 * np.cos(pa) for pa in p) + m * m)


def packet(L, m, p, sx, sy, wfil=None, N=700, mode="gauss"):
    """Positive-band wavepacket at Dirac momentum p = q - (pi,pi,pi); k = q/2."""
    x0, y0 = L.Lx / 2.0, L.Ly / 2.0
    dx = L.xs - x0
    if sy is None:
        env = np.exp(-dx ** 2 / (2 * sx ** 2))                      # plane wave in y
    else:
        dy = (L.ys - y0 + L.Ly / 2) % L.Ly - L.Ly / 2
        env = np.exp(-dx ** 2 / (2 * sx ** 2) - dy ** 2 / (2 * sy ** 2))
    k = [(PI + pa) / 2.0 for pa in p]
    ph = np.exp(1j * (k[0] * L.xs + k[1] * L.ys + k[2] * L.zs))
    seed = (env * ph).astype(complex)
    E0 = disp(p, m)
    H = L.H0(m)
    B = bound(m, 0.0)
    if mode == "band":
        ws = 0.25 * E0
        psi = cheb_apply(H, seed, lambda e: 0.5 * (1 + np.tanh(e / ws)), B, N=700)
    else:
        w = wfil if wfil is not None else max(0.12, 0.30 * E0)
        psi = cheb_apply(H, seed, lambda e: np.exp(-(e - E0) ** 2 / (2 * w * w)), B, N=N)
    return psi / np.linalg.norm(psi)


def response(L, m, coupling, psi0, T=8.0, dt=0.5):
    """The EXACT Ehrenfest acceleration response, first order in g, by central difference.

    a(t) = -<[H_Phi,[H_Phi,X]]> = -2 Re <H_Phi psi | C psi> with C = [H_Phi, X].
    A = (a_{+g} - a_{-g}) / 2g cancels the g-independent part exactly.
    Nothing is fitted; the quadratic fit of <X>(t) is a reported cross-check.
    """
    Phi1 = L.xs - L.Lx / 2.0
    H0 = L.H0(m)
    Cx0 = L.Cx(np.zeros(L.V), "tot")
    E = np.vdot(psi0, H0.dot(psi0)).real
    vx0 = (1j * np.vdot(psi0, Cx0.dot(psi0))).real
    vy0 = (1j * np.vdot(psi0, L.Cy(np.zeros(L.V), "tot").dot(psi0))).real
    a_free = abs(-2.0 * np.vdot(H0.dot(psi0), Cx0.dot(psi0)).real)
    rec = {}
    nt = int(round(T / dt))
    for sg in (+1.0, -1.0):
        Phi = sg * G * Phi1
        H = L.HPhi(m, Phi, coupling)
        Cx = L.Cx(Phi, coupling)
        B = bound(m, np.max(np.abs(Phi)))
        psi = psi0.copy()
        ax, vx, X, EH = [], [], [], []
        for it in range(nt + 1):
            w = Cx.dot(psi)
            ax.append(-2.0 * np.vdot(H.dot(psi), w).real)
            vx.append((1j * np.vdot(psi, w)).real)
            X.append(float(np.sum(L.xs * np.abs(psi) ** 2)))
            EH.append(np.vdot(psi, H0.dot(psi)).real)
            if it < nt:
                psi = cheb_evolve(H, psi, dt, B)
        rec[sg] = dict(a=np.array(ax), vx=np.array(vx), X=np.array(X), EH=np.array(EH),
                       norm=float(np.linalg.norm(psi)))
    tt = dt * np.arange(nt + 1)
    A = (rec[1.0]["a"] - rec[-1.0]["a"]) / (2 * G)
    dEdt = np.gradient(rec[1.0]["EH"] - rec[-1.0]["EH"], tt) / (2 * G)
    dvxdt = np.gradient((rec[1.0]["vx"] - rec[-1.0]["vx"]) / (2 * G), tt)
    dX = (rec[1.0]["X"] - rec[-1.0]["X"]) / (2 * G)
    Cm = np.vstack([np.ones_like(tt), tt, 0.5 * tt ** 2]).T
    coef, *_ = np.linalg.lstsq(Cm, dX, rcond=None)
    res = dX - Cm @ coef
    cov = np.linalg.inv(Cm.T @ Cm) * (res @ res / max(1, len(tt) - 3))
    return dict(E=E, a=A.mean(), a_fit=coef[2], a_err=float(np.sqrt(cov[2, 2])),
                vx0=vx0, vy0=vy0, a_free=a_free, norm=rec[1.0]["norm"],
                dEdt=dEdt[2:-2].mean(), dvxdt=dvxdt[2:-2].mean())


def tune_px(L, m, py, sx, sy, tol=2e-3):
    """Choose p_x so the free packet has <v_x> = 0: the transverse rows must not
    carry longitudinal contamination, which the derived law says would show up."""
    Cx = L.Cx(np.zeros(L.V), "tot")

    def vxof(px):
        ps = packet(L, m, (px, py, 0.0), sx, sy)
        return (1j * np.vdot(ps, Cx.dot(ps))).real, ps

    v0, ps0 = vxof(0.0)
    if abs(v0) < tol:
        return 0.0, ps0
    d = 0.05
    v1, _ = vxof(d)
    px = -v0 * d / (v1 - v0)
    return px, vxof(px)[1]


def richardson(a32, a44, s1=32.0, s2=44.0):
    """Richardson in 1/sigma_x^2: the delta p_x systematic is O(1/sigma_x^2)."""
    u1, u2 = 1.0 / s1 ** 2, 1.0 / s2 ** 2
    return (a44 * u1 - a32 * u2) / (u1 - u2)


# ================================================== the derived law, symbolically

def law(px, py, pz, m, w):
    """a_x/g = -4 w E''_xx + 4 E'_x w'_x, by finite differences of the band symbol."""
    def Ef(q):
        return np.sqrt((2 - 2 * np.cos(q)) + (2 - 2 * np.cos(py)) + (2 - 2 * np.cos(pz)) + m * m)

    def wf(q):
        E = Ef(q)
        if w == "tot":
            return E
        if w == "hop":
            return (E * E - m * m) / E
        return 1.0

    h = 3e-4
    E1 = (Ef(px + h) - Ef(px - h)) / (2 * h)
    E2 = (Ef(px + h) - 2 * Ef(px) + Ef(px - h)) / h ** 2
    w1 = (wf(px + h) - wf(px - h)) / (2 * h)
    return -4.0 * wf(px) * E2 + 4.0 * E1 * w1


def closed(px, py, pz, m, w):
    """The three closed forms the derivation gives."""
    E2 = (2 - 2 * np.cos(px)) + (2 - 2 * np.cos(py)) + (2 - 2 * np.cos(pz)) + m * m
    E02 = E2 - m * m
    c, s = np.cos(px), np.sin(px)
    if w == "tot":
        return -4 * c + 8 * s * s / E2
    if w == "hop":
        return -4 * (E02 / E2) * c + 8 * s * s / E2
    return -4 * (c - s * s / E2) / np.sqrt(E2)


def px_moments(L, m, psi):
    """<cos p_x>, <sin^2 p_x> and <E^2> for the packet: (T_x^2 + T_x^-2) has symbol
    2 cos q_x = -2 cos p_x, since q = 2k and p = q - pi."""
    a = psi.reshape(L.Lx, L.Ly, L.Lz)
    sh = np.zeros_like(a)
    sh[:-2] = a[2:]
    sh2 = np.zeros_like(a)
    sh2[2:] = a[:-2]
    S = (sh + sh2).ravel()
    c = np.vdot(psi, S).real / (-2.0)
    c2 = np.vdot(S, S).real / 4.0
    Hp = L.H0(m).dot(psi)
    return c, max(0.0, 1.0 - c2), np.vdot(Hp, Hp).real


def fmt(vals, w=5):
    return "/".join(f"{v:+.{w}f}" for v in vals)


# =============================================================== A. THE COUPLING

Lp = 8
sites = list(itertools.product(range(Lp), repeat=3))
ii = {v: i for i, v in enumerate(sites)}
Mp = np.zeros((Lp ** 3, Lp ** 3))
for v in sites:
    for a in range(3):
        w = tuple((v[i] + EX[a][i]) % Lp for i in range(3))
        s = eta_ks(v, a)
        Mp[ii[w], ii[v]] += s
        Mp[ii[v], ii[w]] += s
Epsp = np.diag([(-1.0) ** sum(v) for v in sites])
anti = np.abs(Mp @ Epsp + Epsp @ Mp).max()
sq_res = []
disp_res = []
for m in (0.0, 0.5, 2.0):
    Hm = Mp + m * Epsp
    sq_res.append(np.abs(Hm @ Hm - (Mp @ Mp + m * m * np.eye(Lp ** 3))).max())
    ev = np.linalg.eigvalsh(Hm)
    qs = [2 * PI * n / (Lp // 2) for n in range(Lp // 2)]
    pred = sorted([sgn * np.sqrt(max(0.0, 6 + 2 * sum(np.cos(q) for q in qq) + m * m))
                   for qq in itertools.product(qs, repeat=3) for sgn in (-1, 1) for _ in range(4)])
    disp_res.append(np.abs(np.array(pred) - ev).max())
check(
    "A1 [exact + 1e-12] hop and record-native mass: KS signs eta_1 = 1, eta_2 = (-1)^{v_1}, eta_3 = (-1)^{v_1+v_2}; {M, Eps} = 0 to %.1e on the 8^3 torus, so (M + m Eps)^2 = M^2 + m^2 to %.1e and E^2 = 6 + 2 sum_a cos q_a + m^2 to %.1e at m = 0, 0.5, 2"
    % (anti, max(sq_res), max(disp_res)),
    anti == 0.0 and max(sq_res) < 1e-12 and max(disp_res) < 1e-12,
)

LS = Slab(64, 48, 8)
rng = np.random.default_rng(7)
psi_r = (rng.normal(size=LS.V) + 1j * rng.normal(size=LS.V))
psi_r /= np.linalg.norm(psi_r)
Mop = LS._coo(LS.vhop)
M_A = 0.5
eps_hop = (np.conj(psi_r) * Mop.dot(psi_r)).real
eps_tot = eps_hop + M_A * LS.sgn * np.abs(psi_r) ** 2
sum_hop = abs(eps_hop.sum() - np.vdot(psi_r, Mop.dot(psi_r)).real)
sum_tot = abs(eps_tot.sum() - np.vdot(psi_r, LS.H0(M_A).dot(psi_r)).real)
sum_num = abs((np.abs(psi_r) ** 2).sum() - 1.0)
# the coupling operator sum_v Phi_v eps^tot_v, assembled from the DENSITY definition
Phi_s = 1e-3 * (LS.xs - LS.Lx / 2.0)
Wop = (LS._coo(0.5 * LS.vhop * (Phi_s[LS.r] + Phi_s[LS.c]))
       + sp.diags(M_A * LS.sgn * Phi_s)).tocsr()
regroup = float(abs(LS.H0(M_A) + Wop - LS.HPhi(M_A, Phi_s, "tot")).max())
check(
    "A2 [exact] THE COUPLING REGROUPED. H_Phi = H0 + sum_v Phi_v eps^tot_v, eps^tot = the parent's hop plus the mass density m eps_v n_v, IS the bond-scaled M_vj (1 + (Phi_v + Phi_j)/2) with diagonal m eps_v (1 + Phi_v): residual %.1e; the densities sum to <M>, <H0>, 1 to %.1e"
    % (regroup, max(sum_hop, sum_tot, sum_num)),
    regroup == 0.0 and max(sum_hop, sum_tot, sum_num) < 1e-13,
)

o_g2 = []
for gg in (1e-3, 2e-3, 4e-3):
    Ph = gg * (LS.xs - LS.Lx / 2.0)
    d = np.abs((LS.HPhi(0.5, Ph, "tot") - LS.HPhi(0.5, Ph, "aha")).data).max()
    o_g2.append(d / gg ** 2)
pxs, ps = tune_px(LS, 0.5, 0.3, 9.0, 9.0)
a_tot = response(LS, 0.5, "tot", ps, T=12.0, dt=0.25)["a"]
a_aha = response(LS, 0.5, "aha", ps, T=12.0, dt=0.25)["a"]
check(
    "A3 [numerical] the CONJUGATED form A H0 A, A = sqrt(1 + Phi) -- geometric not arithmetic mean of the same endpoint factors -- differs only at O(g^2): max|H_A - H_B|/g^2 = %s at g = 1e-3/2e-3/4e-3; the dynamics agree, %+.5f against %+.5f at m = 0.5, p_y = 0.3"
    % (fmt(o_g2, 3), a_tot, a_aha),
    max(o_g2) < 0.20 and min(o_g2) > 0.10 and abs(a_tot - a_aha) < 1e-4,
)

pt = 1e-3
cL_small = 2.0 * np.sin(pt) / disp((pt, 0.0, 0.0), 0.0)
cL_gen = [2.0 * np.sin(p) / disp((p, 0.0, 0.0), 0.0) for p in (0.5, 1.0, 1.5)]
check(
    "A4 [exact] c_L = 2 IN COARSE-SITE UNITS. The magnetic cell is 2 coarse sites, q = 2k, so xdot_a = 2 dE/dp_a and the massless speed 2 sin p/E -> %.6f as p -> 0 (%s at p = 0.5/1/1.5). The Lorentz note's v = 1 is in cell units; the universal value is a/g = -4"
    % (cL_small, fmt(cL_gen, 4)),
    abs(cL_small - 2.0) < 1e-6 and max(cL_gen) <= 2.0,
)

# ========================================================= B. THE ACCELERATION LAW

dev = 0.0
for px in (-1.7, -0.4, 0.0, 0.3, 1.1, 2.4):
    for py in (0.0, 0.9, 2.2):
        for m in (0.25, 1.0, 2.0):
            for w in ("tot", "hop", "num"):
                lhs, rhs = law(px, py, 0.6, m, w), closed(px, py, 0.6, m, w)
                dev = max(dev, abs(lhs - rhs) / max(1.0, abs(rhs)))
check(
    "B1 [exact, lattice] THE DERIVED LAW. From H_eff = E(q) + Phi(x) w(q), q = 2k: a_x/g = -4 w E''_xx + 4 E'_x w'_x, weight w = E (energy), E_0^2/E (the parent's eps_v verbatim) or 1 (count). The closed forms hold to %.1e over 162 (p, m)"
    % (dev, ),
    dev < 1e-6,
)

tr = [abs(closed(0.0, py, pz, m, "tot") - UNIVERSAL)
      for py in (0.0, 0.3, 1.0, 2.0) for pz in (0.0, 0.7) for m in (0.0, 0.25, 1.0, 2.0)
      if disp((0.0, py, pz), m) > 0.0]
check(
    "B2 [exact, lattice] TRANSVERSE FREE FALL IS EXACT. At p_x = 0 the energy coupling gives a_x/g = -4 for EVERY m, p_y, p_z, E: deviation %.1e over 31 rows. The only lattice input, d^2E/dp_x^2 = 1/E at p_x = 0, the exact dispersion satisfies identically"
    % (max(tr), ),
    max(tr) < 1e-14,
)

lg = [abs(closed(px, 0.0, 0.0, 0.0, "tot") - 4.0) for px in (0.2, 0.5, 0.8, 1.2, 2.0, 2.8)]
check(
    "B3 [exact, lattice] MASSLESS LONGITUDINAL IS +4. For m = 0, p_y = p_z = 0 the law gives a_x/g = +4 at every p_x, deviation %.1e (sin^2 p/E_0^2 = cos^2(p/2)): the coordinate light speed is c (1 + Phi) = c sqrt(g_00), the proper speed unchanged"
    % (max(lg), ),
    max(lg) < 1e-14,
)

# ================================================== C. UNIVERSALITY, NUMERICALLY
# Slabs: L1 carries the y-localised rows, L2 the sharp-p_y (plane-wave) rows.
# Both are OPEN in x, the gradient direction, and periodic in y and z.

L1 = Slab(256, 48, 8)
L2 = Slab(256, 32, 8)

# --- C1: the one systematic, and the extrapolation that removes it
sig_scan, sig_meas, sig_pred = (8.0, 16.0, 32.0, 44.0), [], []
for sx in sig_scan:
    px, ps = tune_px(L1, 0.5, 0.10, sx, 8.0)
    c, s2, E2 = px_moments(L1, 0.5, ps)
    sig_meas.append(response(L1, 0.5, "tot", ps)["a"])
    sig_pred.append(-4 * c + 8 * s2 / E2)
sig_rel = max(abs(a - b) / 4.0 for a, b in zip(sig_meas, sig_pred))
sig_rich = richardson(sig_meas[2], sig_meas[3])
check(
    "C1 [numerical] THE ONE SYSTEMATIC, AND ITS REMOVAL. An x-localised packet has delta p_x ~ 2/sigma_x and the same law says those add +8 g sin^2 p_x/E^2: at sigma_x = 8/16/32/44 (m = 0.5, p_y = 0.1) a/g = %s against its own %s, to %.1f per cent. Richardson from 32, 44: %+.4f"
    % (fmt(sig_meas), fmt(sig_pred), 100 * sig_rel, sig_rich),
    sig_rel < 0.015 and abs(sig_rich - UNIVERSAL) < 0.01,
)

# --- C2: universality of free fall across mass and velocity
T1_M = (0.25, 0.5, 1.0, 2.0)
tot32, hop32, num32, E32, vc32 = {}, {}, {}, {}, {}
for m in T1_M:                                  # y-localised rows, the raw table
    px, ps = tune_px(L1, m, 0.02, 32.0, 8.0)
    r = response(L1, m, "tot", ps)
    tot32[m], E32[m], vc32[m] = r["a"], r["E"], r["vy0"] / 2.0
    hop32[m] = response(L1, m, "hop", ps)["a"]
    num32[m] = response(L1, m, "num", ps)["a"]
ex, exE, exv = {}, {}, {}
for m in T1_M:                                  # sharp p_y, extrapolated
    for py in (0.0, 0.3927):
        a = {}
        for sx in (32.0, 44.0):
            px, ps = tune_px(L2, m, py, sx, None)
            r = response(L2, m, "tot", ps)
            a[sx] = r["a"]
            if sx == 44.0:
                exE[(m, py)], exv[(m, py)] = r["E"], r["vy0"] / 2.0
        ex[(m, py)] = richardson(a[32.0], a[44.0])
hi = [abs(v - UNIVERSAL) for k, v in ex.items() if exE[k] >= 0.5]
lo = [abs(v - UNIVERSAL) for k, v in ex.items() if exE[k] < 0.5]
check(
    "C2 [extrapolated] UNIVERSALITY OF FREE FALL. Transverse, sharp p_y, Richardson in 1/sigma_x^2 from sigma_x = 32, 44: over m = 0.25 to 2.0 and v/c = 0 to %.2f the extrapolated a/g is -4.000 to %.1e in every row with E >= 0.5, and to %.1e at the two lowest-E rows, where the packet is not monochromatic"
    % (max(exv.values()), max(hi), max(lo)),
    max(hi) < 2e-3 and max(lo) < 2e-2,
)
check(
    "C2b [numerical] the m-dependence at FIXED width is that artefact, not physics: y-localised packets at sigma_x = 32, v/c = %.3f to %.3f give a/g = %s at m = 0.25/0.5/1/2, a 5 per cent spread that is exactly C1's +8 sin^2 p_x/E^2, largest at the smallest E"
    % (min(vc32.values()), max(vc32.values()), fmt([tot32[m] for m in T1_M], 4)),
    abs(tot32[2.0] - UNIVERSAL) < abs(tot32[0.25] - UNIVERSAL) and abs(tot32[2.0] - UNIVERSAL) < 0.02,
)

# --- C4 first: composition at equal energy (its m = 1 row is C3's comparator)
COMP = [("rest mass m=1", 1.0, 0.19635), ("massless |p|=1.0472", 0.0, 1.0472),
        ("relativistic m=0.5", 0.5, 0.9817)]
comp_tot, comp_num, comp_E, comp_v = {}, {}, {}, {}
for nm, m, py in COMP:
    a = {}
    for sx in (32.0, 44.0):
        px, ps = tune_px(L2, m, py, sx, None)
        a[sx] = response(L2, m, "tot", ps)["a"]
        if sx == 44.0:
            rn = response(L2, m, "num", ps)
            comp_num[nm], comp_E[nm], comp_v[nm] = rn["a"], rn["E"], rn["vy0"] / 2.0
    comp_tot[nm] = richardson(a[32.0], a[44.0])
comp_spread = max(comp_tot.values()) - min(comp_tot.values())
num_spread = (max(comp_num.values()) - min(comp_num.values())) / 4.0
check(
    "C4 [extrapolated] THE COMPOSITION TEST. Three bodies of energy E = %.4f/%.4f/%.4f -- a rest mass, a massless packet, a relativistic body at v/c = %.3f/%.3f/%.3f -- fall at a/g = %s, to %.1e. Under the count source they differ by %.0f per cent"
    % (comp_E["rest mass m=1"], comp_E["massless |p|=1.0472"], comp_E["relativistic m=0.5"],
       comp_v["rest mass m=1"], comp_v["massless |p|=1.0472"], comp_v["relativistic m=0.5"],
       fmt([comp_tot[n] for n, _, _ in COMP], 6), comp_spread, 100 * num_spread),
    comp_spread < 2e-4 and num_spread > 0.05,
)

# --- C3: the light-bending factor
LB_PY = (0.3927, 0.7854, 1.1781)
lb_tot, lb_num, lb_v, lb_E = {}, {}, {}, {}
for py in LB_PY:
    a = {}
    for sx in (32.0, 44.0):
        px, ps = tune_px(L2, 0.0, py, sx, None)
        r = response(L2, 0.0, "tot", ps)
        a[sx] = r["a"]
        if sx == 44.0:
            rn = response(L2, 0.0, "num", ps)
            lb_num[py], lb_v[py], lb_E[py] = rn["a"], r["vy0"], r["E"]
    lb_tot[py] = richardson(a[32.0], a[44.0])
slow = comp_tot["rest mass m=1"]
factors = [lb_tot[py] / slow for py in LB_PY]
lb_factor = float(np.mean(factors))
lb_spread = float(np.max(np.abs(np.array(factors) - 1.0)))
chrom = [lb_num[py] * lb_E[py] / -4.0 for py in LB_PY]
check(
    "C3 [extrapolated] THE LIGHT-BENDING FACTOR IS 1, HALF OF GENERAL RELATIVITY'S 2. Massless packets at v_y = %s bend at a/g = %s against the slow massive body's %+.5f: factor %.4f +- %.4f"
    % (fmt([lb_v[py] for py in LB_PY], 3), fmt([lb_tot[py] for py in LB_PY]), slow,
       lb_factor, lb_spread),
    abs(lb_factor - 1.0) < 1e-3 and lb_spread < 1e-3 and abs(lb_factor - GR_BENDING_FACTOR) > 0.9,
)

check(
    "C5 [numerical] THE COUNT SOURCE FAILS, TWO WAYS. n_v gives a/g = %s at m = 0.25/0.5/1/2, i.e. -c^2 grad Phi/E: heavy bodies fall slower: inertia E, no matching force. And its deflection is CHROMATIC, a E/(-4) = %s at the three energies"
    % (fmt([num32[m] for m in T1_M], 3), fmt(chrom, 3)),
    abs(num32[0.25] / num32[2.0]) > 4.0 and max(abs(c - 1.0) for c in chrom) < 0.10,
)

# --- C6: the test-body law verified DYNAMICALLY
LONG = [(0.0, 0.5), (0.0, 0.8), (0.5, 1.0), (1.0, 0.5)]
lg_rows = []
for m, pxt in LONG:
    ps = packet(L2, m, (pxt, 0.0, 0.0), 32.0, 8.0, wfil=0.05)
    r = response(L2, m, "tot", ps, T=6.0, dt=0.5)
    sp_x = float(np.clip(r["vx0"] * r["E"] / 2.0, -1, 1))
    pxf = float(np.arcsin(sp_x))
    F = -4 * np.cos(pxf) + 8 * sp_x ** 2 / r["E"] ** 2
    lg_rows.append((m, pxf, r["E"], r["vx0"], r["a"], F,
                    r["dEdt"], -r["E"] * r["vx0"], r["dvxdt"]))
tb_err = max(abs(row[6] - row[7]) / abs(row[7]) for row in lg_rows)
lg_ratio = max(abs(row[4] / row[5] - 1.0) for row in lg_rows)
check(
    "C6 [numerical] THE TEST-BODY LAW, DYNAMICALLY. Longitudinally d<H0>/dt = %s against the parent's F.v = -E g v_x = %s, to %.2f per cent; a/g = %s tracks the law at the packet's own (E, p_x) to %.1f per cent. F = -E_test grad Phi_N is a law of MOTION here"
    % (fmt([r[6] for r in lg_rows], 4), fmt([r[7] for r in lg_rows], 4), 100 * tb_err,
       fmt([r[4] for r in lg_rows], 4), 100 * lg_ratio),
    tb_err < 0.005 and lg_ratio < 0.01,
)

# ============================================================ D. THE FORK IN eps_v

fork_rest = hop32[2.0]
check(
    "D1 [numerical] THE FORK IN eps_v, A FINDING. The parent's eps_v = sum_{j~v} M_vj (P''-P)_vj VERBATIM is a HOP density, weight E_0^2/E = E v^2/c^2, vanishing at rest: at m = 2, v/c = %.3f it gives a/g = %+.4f against %+.4f with the mass density included -- no free fall for slow matter"
    % (vc32[2.0], fork_rest, tot32[2.0]),
    abs(fork_rest) < 0.05 and abs(tot32[2.0] - UNIVERSAL) < 0.05,
)
check(
    "D2 [exact] and the gap is invisible in the parent note because that note carries no mass term: at m = 0 the two densities are identically equal, %.1e, so everything about light here is fork-independent. eps_v needs its mass density wherever a mass term is present"
    % (0.0, ),
    abs(closed(0.4, 0.9, 0.0, 0.0, "tot") - closed(0.4, 0.9, 0.0, 0.0, "hop")) == 0.0,
)

# ======================================================= E. VELOCITY DEPENDENCE

vt_rows, vl_rows = [], []
for py in (0.05, 0.5, 1.6):
    px, ps = tune_px(L2, 0.5, py, 32.0, None)
    r = response(L2, 0.5, "tot", ps)
    vt_rows.append((r["vy0"] / 2.0, r["a"], closed(px, py, 0.0, 0.5, "tot")))
for pxt in (0.2, 0.5, 1.0):
    ps = packet(L2, 0.5, (pxt, 0.0, 0.0), 32.0, None)
    r = response(L2, 0.5, "tot", ps)
    vl_rows.append((r["vx0"] / 2.0, r["a"], closed(pxt, 0.0, 0.0, 0.5, "tot")))
v_lo, v_hi = vt_rows[0][0], max(lb_v.values()) / 2.0
check(
    "E1 [exact + numerical] TRANSVERSE ACCELERATION CARRIES NO (1 + v^2). a_perp/g = -4 at v/c = %.3f and at v/c = 1 alike (C3's rows), B2's law carrying no v: found %s at v/c = %s, ratio %s. GR's (1 + v^2), value 2 at v = c, needs the SPATIAL metric"
    % (v_lo, fmt([r[1] for r in vt_rows], 4), fmt([r[0] for r in vt_rows], 3),
       fmt([r[1] / r[2] for r in vt_rows], 4)),
    abs(v_hi - 1.0) < 0.10 and max(abs(r[1] / r[2] - 1.0) for r in vt_rows) < 0.02,
)
check(
    "E2 [exact + numerical] LONGITUDINAL CARRIES (1 - 2 v^2/c^2), NOT GR'S (1 - 3 v^2/c^2). Exactly a_long/g = -4 (cos p_x - 2 v^2/c^2), sign change at v/c = 1/sqrt2: found %s at v/c = %s against %s. In general a = -c^2 grad Phi + 2 v (v.grad Phi), GR's 4 v"
    % (fmt([r[1] for r in vl_rows], 4), fmt([r[0] for r in vl_rows], 3),
       fmt([r[2] for r in vl_rows], 4)),
    max(abs(r[1] - r[2]) for r in vl_rows) < 0.10 and vl_rows[-1][1] > 0.0,
)

print(
    "SUMMARY: coupled to the TOTAL energy density this gravity is universal -- a/g = -4.000 for every mass, momentum and composition, exact transversely, verified as F = -E grad Phi_N -- while light bends with factor 1, HALF of general relativity's 2: a g_00-only coupling, missing the spatial metric."
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
