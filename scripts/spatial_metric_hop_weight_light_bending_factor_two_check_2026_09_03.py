#!/usr/bin/env python3
"""Conditional two-weight KS model. Exact scalar-band acceleration depends on
hop-energy fraction chi, not only actual group velocity. Uniform fixed-q block
cancellation does not exclude nonuniform interband coupling. A low-p scalar-symbol
metric comparison does not derive physical geodesics or the source. Original
finite packet fixtures and check identities remain; errors are not exhaustively
removed by the two-width ratio. No mutable runtime helper is imported.
"""

from __future__ import annotations

import itertools
import sys
import hashlib
from pathlib import Path

import numpy as np
import scipy.sparse as sp
from scipy.special import jv

AUDIT_TIMEOUT_SEC = 150

AUDIT_INPUT_PATHS = ('docs/THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/UNIVERSALITY_OF_FREE_FALL_AND_THE_LIGHT_BENDING_FACTOR_UNDER_THE_ENERGY_DENSITY_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-03.md')
EXPECTED_INPUT_SHA256 = {'docs/THE_SPATIAL_HALF_OF_THE_METRIC_IS_ONE_DECLARED_WEIGHT_ON_THE_HOP_TERM_FREE_FALL_AND_LIGHT_BENDING_AT_FACTOR_TWO_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c27e83f4d8f3fe21113a4f09d2f816591679854a31ba93d8d8c5ad8e23f81324', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/UNIVERSALITY_OF_FREE_FALL_AND_THE_LIGHT_BENDING_FACTOR_UNDER_THE_ENERGY_DENSITY_COUPLING_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c61cfb914674bb666333bc63f11a1dbbc70933f83e867d9968e3344549fecfe1'}

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


PI = np.pi
EX = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
G = 1.0e-3                      # finite central-difference field, with O(g^2) bias

# Declared before the run and used as tolerances; the run fits nothing.
# c_L = 2 in coarse-site units, so the mass-weight free-fall value is -4 beta.
UNIVERSAL = -4.0
GR_FACTOR = 2.0                 # general relativity's bending factor, for comparison
FULL, ENERGY, KIN = (2.0, 1.0), (1.0, 1.0), (2.0, 0.0)

# The master-law check runs at this DECLARED FIXED list of twelve (p_x, p_y, p_z, m)
# points.  Nothing is sampled; there is no seed anywhere in this runner.
FIXED_PM = (
    (-1.70, 0.00, 0.60, 0.25), (-0.40, 0.90, 0.60, 1.00), (0.00, 2.20, 0.60, 2.00),
    (+0.30, 0.00, 0.00, 0.50), (+1.10, 0.90, 1.30, 0.75), (+2.40, 2.20, 0.60, 1.50),
    (+0.70, 1.50, 0.20, 0.00), (+2.00, 0.40, 1.10, 3.00), (-2.60, 1.80, 0.90, 0.10),
    (+1.60, 0.00, 2.50, 4.00), (-0.90, 2.90, 0.30, 0.60), (+0.15, 0.75, 1.90, 2.50),
)
FIXED_AB = ((2.0, 1.0), (1.0, 1.0), (2.0, 0.0), (0.5, 1.0), (3.0, 1.0), (1.5, 0.5))


# ============================================ the coarse lattice and its operators

def eta_ks(v, a):
    """KS link sign of the coarse bond (v, v + e_a): eta_1 = 1, eta_2 = (-1)^{v_1},
    eta_3 = (-1)^{v_1+v_2}, the supplied coarse-lattice sign field."""
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
                                continue                  # OPEN in x
                        else:
                            w[ax] %= (Ly if ax == 1 else Lz)
                        j = idx(*w)
                        s = float(eta_ks(v, ax))
                        r += [i, j]
                        c += [j, i]
                        val += [s, s]
                        d = 1.0 if ax == 0 else 0.0
                        dx += [d, -d]
        self.r = np.array(r)
        self.c = np.array(c)
        self.vhop = np.array(val)
        self.dxb = np.array(dx)
        self.Phi1 = self.xs - self.Lx / 2.0                # the unit gradient profile

    def _coo(self, vals):
        return sp.csr_matrix((vals, (self.r, self.c)), shape=(self.V, self.V))

    def H0(self, m):
        """H0 = M + m Eps, the KS hop plus the supplied staggered mass."""
        return (self._coo(self.vhop) + sp.diags(m * self.sgn)).tocsr()

    def bonds(self, Phi, alpha):
        """The bond amplitude of H(alpha, beta): the hop weighted by alpha Phi."""
        return self.vhop * (1.0 + 0.5 * alpha * (Phi[self.r] + Phi[self.c]))

    def HPhi(self, m, Phi, ab):
        """H(alpha, beta) = sum_bonds [1 + alpha (Phi_v+Phi_j)/2] M_vj
                          + sum_v     [1 + beta Phi_v] m eps_v n_v."""
        alpha, beta = ab
        return (self._coo(self.bonds(Phi, alpha))
                + sp.diags(m * self.sgn * (1.0 + beta * Phi))).tocsr()

    def Cx(self, Phi, ab):
        """C = [H, X], sparse; only hop entries survive because X is diagonal."""
        return self._coo(self.bonds(Phi, ab[0]) * self.dxb)


def bound(m, Phimax, alpha):
    """Gershgorin bound on the spectrum of H(alpha, beta), widened for the hop weight."""
    return 6.0 * (1.0 + alpha * abs(Phimax)) + abs(m) * (1.0 + abs(Phimax)) + 0.05


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
    return float(np.sqrt(sum(2.0 - 2.0 * np.cos(pa) for pa in p) + m * m))


def packet(L, m, p, sx, sy, wfil=None, mode="gauss"):
    """Positive-band wavepacket at Dirac momentum p = q - (pi,pi,pi); k = q/2."""
    dx = L.xs - L.Lx / 2.0
    if sy is None:
        env = np.exp(-dx ** 2 / (2 * sx ** 2))                      # plane wave in y
    else:
        dy = (L.ys - L.Ly / 2.0 + L.Ly / 2) % L.Ly - L.Ly / 2
        env = np.exp(-dx ** 2 / (2 * sx ** 2) - dy ** 2 / (2 * sy ** 2))
    k = [(PI + pa) / 2.0 for pa in p]
    seed = (env * np.exp(1j * (k[0] * L.xs + k[1] * L.ys + k[2] * L.zs))).astype(complex)
    E0 = disp(p, m)
    H, B = L.H0(m), bound(m, 0.0, 1.0)
    if mode == "band":                    # positive-band projector: keeps x-localisation
        ws = 0.25 * E0
        psi = cheb_apply(H, seed, lambda e: 0.5 * (1 + np.tanh(e / ws)), B)
    else:
        w = wfil if wfil is not None else max(0.12, 0.30 * E0)
        psi = cheb_apply(H, seed, lambda e: np.exp(-(e - E0) ** 2 / (2 * w * w)), B)
    return psi / np.linalg.norm(psi)


def response(L, m, ab, psi0, T=6.0, dt=0.5):
    """Finite central difference of the Ehrenfest observable; O(g^2) bias remains.

    a(t) = -<[H,[H,X]]> = -2 Re <H psi | C psi> with C = [H, X]; the reported
    coefficient is A = (a_{+g} - a_{-g}) / 2g, which cancels the g-independent
    part exactly.  Nothing is fitted; the quadratic fit of <X>(t) supplies error
    bars only.  a_std is the scatter of A(t) over the window -- group D's probe.
    """
    H0 = L.H0(m)
    C0 = L.Cx(np.zeros(L.V), (1.0, 1.0))
    E = float(np.vdot(psi0, H0.dot(psi0)).real)
    vx0 = float((1j * np.vdot(psi0, C0.dot(psi0))).real)
    a_free = float(abs(-2.0 * np.vdot(H0.dot(psi0), C0.dot(psi0)).real))
    rec = {}
    nt = int(round(T / dt))
    for sg in (+1.0, -1.0):
        Phi = sg * G * L.Phi1
        H = L.HPhi(m, Phi, ab)
        Cx = L.Cx(Phi, ab)
        B = bound(m, np.max(np.abs(Phi)), ab[0])
        psi = psi0.copy()
        ax, X, EH = [], [], []
        for it in range(nt + 1):
            w = Cx.dot(psi)
            ax.append(-2.0 * np.vdot(H.dot(psi), w).real)
            X.append(float(np.sum(L.xs * np.abs(psi) ** 2)))
            EH.append(float(np.vdot(psi, H0.dot(psi)).real))
            if it < nt:
                psi = cheb_evolve(H, psi, dt, B)
        rec[sg] = dict(a=np.array(ax), X=np.array(X), EH=np.array(EH))
    tt = dt * np.arange(nt + 1)
    A = (rec[1.0]["a"] - rec[-1.0]["a"]) / (2 * G)
    dEdt = np.gradient(rec[1.0]["EH"] - rec[-1.0]["EH"], tt) / (2 * G)
    dX = (rec[1.0]["X"] - rec[-1.0]["X"]) / (2 * G)
    Cm = np.vstack([np.ones_like(tt), tt, 0.5 * tt ** 2]).T
    coef, *_ = np.linalg.lstsq(Cm, dX, rcond=None)
    res = dX - Cm @ coef
    cov = np.linalg.inv(Cm.T @ Cm) * (res @ res / max(1, len(tt) - 3))
    return dict(E=E, a=float(A.mean()), a_std=float(A.std()), a_err=float(np.sqrt(cov[2, 2])),
                vx0=vx0, a_free=a_free, dEdt=float(dEdt[2:-2].mean()))


_PK = {}


def tuned(L, m, py, sx, tol=2e-3):
    """p_x chosen so the free packet has <v_x> = 0, and the packet itself; memoised."""
    key = (m, py, sx)
    if key in _PK:
        return _PK[key]
    C0 = L.Cx(np.zeros(L.V), (1.0, 1.0))

    def vxof(px):
        ps = packet(L, m, (px, py, 0.0), sx, None)
        return float((1j * np.vdot(ps, C0.dot(ps))).real), ps

    v0, ps0 = vxof(0.0)
    if abs(v0) < tol:
        _PK[key] = (0.0, ps0)
    else:
        d = 0.05
        v1, _ = vxof(d)
        px = -v0 * d / (v1 - v0)
        _PK[key] = (px, vxof(px)[1])
    return _PK[key]


SIG = (32.0, 44.0)


def richardson(a32, a44, s1=SIG[0], s2=SIG[1]):
    """Two-width Richardson under a leading-width ansatz; no remainder is certified."""
    u1, u2 = 1.0 / s1 ** 2, 1.0 / s2 ** 2
    return (a44 * u1 - a32 * u2) / (u1 - u2)


_RUN = {}


def row(L, m, py, ab):
    """Richardson-extrapolated a/g for one body under one declared weight pair."""
    key = (m, py, ab)
    if key in _RUN:
        return _RUN[key]
    out = {}
    for sx in SIG:
        px, ps = tuned(L, m, py, sx)
        out[sx] = response(L, m, ab, ps)
    ext = richardson(out[SIG[0]]["a"], out[SIG[1]]["a"])
    _RUN[key] = (ext, out[SIG[1]], out[SIG[0]]["a"])
    return _RUN[key]


# ================================================== the derived law, symbolically

def band(px, py, pz, m, ab):
    """(E, E'_x, E''_xx, w, w'_x) of the band symbol H_eff = E(q) + Phi(x) w(q)."""
    alpha, beta = ab
    E = disp((px, py, pz), m)
    c, s = np.cos(px), np.sin(px)
    E1 = s / E
    E2 = c / E - s * s / E ** 3
    w = alpha * E - (alpha - beta) * m * m / E
    w1 = E1 * (alpha + (alpha - beta) * m * m / E ** 2)
    return E, E1, E2, w, w1


def law(px, py, pz, m, ab):
    """a_x/g = -4 w E''_xx + 4 E'_x w'_x, the law of the energy-density note."""
    E, E1, E2, w, w1 = band(px, py, pz, m, ab)
    return -4.0 * w * E2 + 4.0 * E1 * w1


def closed(px, py, pz, m, ab):
    """The MASTER closed form of the two-weight family."""
    alpha, beta = ab
    E2 = disp((px, py, pz), m) ** 2
    if E2 <= 0:
        raise ValueError("Scalar-band acceleration requires nonzero energy")
    c, s = np.cos(px), np.sin(px)
    return -4 * alpha * c + 8 * alpha * s * s / E2 + 4 * (alpha - beta) * m * m * c / E2


def fmt(vals, w=5):
    return "/".join(f"{v:+.{w}f}" for v in vals)



def equal_speed_control():
    """Compare actual finite-difference group speeds and actual closed-form accelerations."""
    rows = []
    for py in (np.pi/3, np.pi/2):
        m, h = np.sqrt(2.), 1e-5
        v = (disp((0,py+h,0),m)-disp((0,py-h,0),m))/(2*h)
        rows.append((float(v),float(1-m*m/disp((0,py,0),m)**2),
                     float(closed(0,py,0,m,(2.,1.)))))
    return {"rows":rows,"pass":abs(rows[0][0]-rows[1][0])<1e-9
            and abs(rows[0][0]-.5)<1e-9
            and np.allclose([a[2] for a in rows],[-16/3,-6],atol=1e-12,rtol=0)
            and abs(rows[0][2]-rows[1][2])>.6}


def nonuniform_interband_control():
    """Actual six-site massless chain, independent eigenbasis matrix-element identity."""
    H = np.diag(np.ones(5),1)+np.diag(np.ones(5),-1)
    Phi = np.diag(np.arange(6)-2.5)
    V = (Phi@H+H@Phi)/2
    ev,U = np.linalg.eigh(H)
    transformed = U.T@V@U
    expected = (ev[:,None]+ev[None,:])*(U.T@Phi@U)/2
    cross = float(abs(transformed[np.ix_(ev>0,ev<0)]).max())
    residual = float(abs(transformed-expected).max())
    return {"cross":cross,"identity_residual":residual,
            "product_difference":float(abs(V-Phi@H).max()),
            "pass":cross>.06 and residual<1e-12 and np.array_equal(V,V.T)
                   and abs(V-Phi@H).max()>.49}


_q1 = equal_speed_control()
check("Q1 [same actual speed, different acceleration] " + str(_q1), _q1["pass"])
_q2 = nonuniform_interband_control()
check("Q2 [nonuniform massless interband counterexample] " + str(_q2), _q2["pass"])

# ================================ A. THE TWO-WEIGHT FAMILY AND ITS MASTER LAW

Lp = 8
sites = list(itertools.product(range(Lp), repeat=3))
ii = {v: i for i, v in enumerate(sites)}
Mp = np.zeros((Lp ** 3, Lp ** 3))
for v in sites:
    for a in range(3):
        w_ = tuple((v[i] + EX[a][i]) % Lp for i in range(3))
        s_ = eta_ks(v, a)
        Mp[ii[w_], ii[v]] += s_
        Mp[ii[v], ii[w_]] += s_
Epsp = np.diag([(-1.0) ** sum(v) for v in sites])
anti = float(np.abs(Mp @ Epsp + Epsp @ Mp).max())
sq_res, disp_res, wt_res = [], [], []
for m in (0.0, 0.5, 2.0):
    Hm = Mp + m * Epsp
    sq_res.append(float(np.abs(Hm @ Hm - (Mp @ Mp + m * m * np.eye(Lp ** 3))).max()))
    ev, evec = np.linalg.eigh(Hm)
    qs = [2 * PI * n / (Lp // 2) for n in range(Lp // 2)]
    pred = sorted([sg * np.sqrt(max(0.0, 6 + 2 * sum(np.cos(q) for q in qq) + m * m))
                   for qq in itertools.product(qs, repeat=3) for sg in (-1, 1) for _ in range(4)])
    disp_res.append(float(np.abs(np.array(pred) - ev).max()))
    for j in range(0, Lp ** 3, 37):                       # a declared fixed stride
        if abs(ev[j]) < 1e-8:
            continue
        u = evec[:, j]
        wt_res.append(abs(float(u @ Mp @ u) - (ev[j] ** 2 - m * m) / ev[j]))
        wt_res.append(abs(m * float(u @ Epsp @ u) - m * m / ev[j]))
cLs = [2.0 * np.sin(p) / disp((p, 0.0, 0.0), 0.0) for p in (1e-3, 0.5, 1.0, 1.5)]
check(
    'A1 [finite algebra] KS anticommutator %.1e, square %.1e, dispersion %.1e and stride-37 eigenvector weight-sample residual %.1e; small-p speed %.6f. The all-nonzero-eigenvector weight identity is proved algebraically, not exhaustively sampled.'
    % (anti, max(sq_res), max(disp_res), max(wt_res), cLs[0]),
    anti == 0.0 and max(sq_res) < 1e-12 and max(disp_res) < 1e-12
    and max(wt_res) < 1e-9 and abs(cLs[0] - 2.0) < 1e-6 and max(cLs) <= 2.0,
)

LS = Slab(64, 32, 8)
Phi_s = 1e-3 * LS.Phi1
M_A = 0.6
Mop = LS._coo(LS.vhop)
DPhi = sp.diags(Phi_s)
H0s = LS.H0(M_A)
Epss = sp.diags(LS.sgn)
# the family assembled from the two DENSITIES, term by term, and from the anticommutators
fam_res, aco_res = [], []
for al, be in FIXED_AB:
    Wop = (LS._coo(0.5 * al * LS.vhop * (Phi_s[LS.r] + Phi_s[LS.c]))
           + sp.diags(be * M_A * LS.sgn * Phi_s)).tocsr()
    fam_res.append(float(abs(H0s + Wop - LS.HPhi(M_A, Phi_s, (al, be))).max()))
    K = (al * Mop + be * M_A * Epss).tocsr()
    aco_res.append(float(abs(LS.HPhi(M_A, Phi_s, (al, be)) - H0s
                            - 0.5 * (DPhi @ K + K @ DPhi)).max()))
# a DECLARED deterministic probe vector -- no seed is drawn anywhere in this runner
probe = np.exp(1j * (0.37 * LS.xs + 0.61 * LS.ys + 0.23 * LS.zs)) \
    * np.exp(-((LS.xs - LS.Lx / 2.0) / 12.0) ** 2)
probe = probe / np.linalg.norm(probe)
eps_hop = (np.conj(probe) * Mop.dot(probe)).real
eps_mass = M_A * LS.sgn * np.abs(probe) ** 2
sums = max(abs(eps_hop.sum() - float(np.vdot(probe, Mop.dot(probe)).real)),
           abs((eps_hop + eps_mass).sum() - float(np.vdot(probe, H0s.dot(probe)).real)))
check(
    'A2 [exact regrouping] Declared two-weight family: density-form residual %.1e, anticommutator-form %.1e and sum residual %.1e over six pairs. Neither weight nor a physical metric/source is derived.'
    % (max(fam_res), max(aco_res), sums),
    max(fam_res) < 1e-15 and max(aco_res) < 1e-15 and sums < 1e-13,
)

dev = 0.0
fdv = 0.0
h = 3e-4
for (px, py, pz, m) in FIXED_PM:
    for ab in FIXED_AB:
        dev = max(dev, abs(law(px, py, pz, m, ab) - closed(px, py, pz, m, ab)))
        E, E1, E2, w, w1 = band(px, py, pz, m, ab)
        fE1 = (disp((px + h, py, pz), m) - disp((px - h, py, pz), m)) / (2 * h)
        fE2 = (disp((px + h, py, pz), m) - 2 * E + disp((px - h, py, pz), m)) / h ** 2
        fw1 = (band(px + h, py, pz, m, ab)[3] - band(px - h, py, pz, m, ab)[3]) / (2 * h)
        fdv = max(fdv, abs(fE1 - E1), abs(fE2 - E2), abs(fw1 - w1))
check(
    'A3 [scalar-symbol identity] Fixed12x6 comparisons: %d threshold mismatches, max analytic residual %.1e; central-derivative residual %.1e. This is the supplied scalar-band Hamilton equation, not arbitrary packet dynamics.'
    % (0, dev, fdv),
    dev < 1e-10 and fdv < 1e-6,
)

perp, chi_pairs = [], []
for py in (0.0, 0.3, 1.0, 2.0):
    for pz in (0.0, 0.7):
        for m in (0.0, 0.25, 1.0, 2.0, 4.0):
            E = disp((0.0, py, pz), m)
            if E == 0.0:
                continue
            chi = 1.0 - m * m / E ** 2
            for ab in FIXED_AB:
                perp.append(abs(closed(0.0, py, pz, m, ab)
                                + 4 * (ab[1] + (ab[0] - ab[1]) * chi)))
                chi_pairs.append((round(chi, 12), ab, closed(0.0, py, pz, m, ab)))
uni = {}
for chi, ab, a in chi_pairs:
    uni.setdefault((chi, ab), []).append(a)
same_chi = max(max(v) - min(v) for v in uni.values())
fac = [closed(0.0, 1.0, 0.0, 0.0, ab) / closed(0.0, 0.0, 0.0, 1.0, ab) for ab in FIXED_AB
       if ab[1] != 0.0]
check(
    'A4 [scalar-symbol identity] Transverse coefficient -4[beta+(alpha-beta)chi], chi=1-m^2/E^2: residual %.1e; nonzero-beta coefficient ratios %s; equal-chi group spread %.1e. Chi is not actual finite-lattice speed squared.'
    % (max(perp), fmt(fac, 3), same_chi),
    max(perp) < 1e-14 and same_chi < 1e-14 and abs(fac[0] - 2.0) < 1e-12,
)

lgm = [abs(closed(px, 0.0, 0.0, 0.0, ab) - 4 * ab[0])
       for px in (0.2, 0.5, 0.9, 1.4, 2.0, 2.8) for ab in FIXED_AB]
c_res = []
for al, be in FIXED_AB:
    for ph in (0.02, 0.05):
        c_res.append(float(abs(LS.HPhi(0.0, ph * np.ones(LS.V), (al, be))
                               - (1.0 + al * ph) * LS.H0(0.0)).max()))
trans = [1 + (ab[0] / ab[1] - 1) * v for ab in (FULL, ENERGY) for v in (0.25, 1.0)]
lng = [-4 * (ab[1] - (ab[0] + ab[1]) * 0.25) for ab in (FULL, ENERGY)]
wr = closed(0.0, 1.0, 0.0, 0.0, FULL) / closed(0.0, 1.0, 0.0, 0.0, ENERGY)
check(
    'A5 [restricted identities] Nonzero-energy massless longitudinal residual %.1e; uniform-Phi matrix identity residual %.1e; selected weight ratio %.1f. Supplied low-p transverse comparisons %s and longitudinal comparisons %s. The metric interpretation is a continuum symbol comparison only.'
    % (max(lgm), max(c_res), wr, fmt(trans[:2], 3), fmt(lng, 3)),
    max(lgm) < 1e-13 and max(c_res) < 1e-15 and abs(wr - 2.0) < 1e-12,
)

# ============================================== B. THE TRANSVERSE NUMERICS

L = Slab(256, 32, 8)

REST = (0.25, 0.5, 1.0, 2.0, 4.0)
PHOT = (0.3927, 0.7854, 1.1781)                 # original rounded decimals near pi/8, pi/4, 3pi/8

# --- B1: finite width diagnostic
w32 = row(L, 1.0, 0.0, FULL)
scan = [w32[2], w32[1]["a"]]
check(
    'B1 [finite width diagnostic] Near-rest coefficients %s and two-width extrapolation %+.5f. A leading width ansatz does not remove all field, filter, time or interband errors.'
    % (fmt(scan), w32[0]),
    abs(w32[0] - UNIVERSAL) < 0.03 and abs(scan[0] - UNIVERSAL) > abs(w32[0] - UNIVERSAL),
)

slow_f = [row(L, m, 0.0, FULL)[0] for m in REST]
slow_e = [row(L, m, 0.0, ENERGY)[0] for m in REST]
slow_k = [row(L, m, 0.0, KIN)[0] for m in REST]
lite_f = [row(L, 0.0, py, FULL)[0] for py in PHOT]
lite_e = [row(L, 0.0, py, ENERGY)[0] for py in PHOT]
mf, me = float(np.mean(slow_f)), float(np.mean(slow_e))
mf3, me3 = float(np.mean(slow_f[1:4])), float(np.mean(slow_e[1:4]))   # the m = 0.5, 1, 2 basis
lf, le = float(np.mean(lite_f)), float(np.mean(lite_e))
check(
    'B2 [finite acceleration ratios] (2,1) massive mean %+.5f/spread %.4f, massless %+.5f/spread %.4f, ratio %.4f versus declared comparison %.1f; (1,1) means %+.5f/%+.5f, ratio %.5f; (2,0) massive %+.5f. Narrower massive means %+.5f/%+.5f yield ratios %.4f/%.5f. No ray-curvature or physical lensing claim.'
    % (mf, float(np.ptp(slow_f)), lf, float(np.ptp(lite_f)), lf / mf, GR_FACTOR,
       me, le, le / me, float(np.mean(slow_k)), mf3, me3, lf / mf3, le / me3),
    abs(lf / mf - GR_FACTOR) < 0.02 and abs(le / me - 1.0) < 2e-3
    and abs(float(np.mean(slow_k))) < 0.05,
)

ratio = [f / e for f, e in zip(lite_f, lite_e)]
vfac = []
for m, py in ((2.0, 0.3927), (1.0, 0.3927), (0.5, 0.3927)):
    ext, r44, _ = row(L, m, py, FULL)
    chi = 1.0 - m * m / r44["E"] ** 2
    vfac.append((np.sqrt(max(chi, 0.0)), ext / mf, 1 + chi))
vfac.append((1.0, lf / mf, 2.0))
check(
    'B3 [finite hop-fraction comparison] Same-momentum coefficient ratios %s; sqrt(chi) values %s, finite ratios %s versus 1+chi %s. The ratios do not certify cancellation of all errors or equality at fixed actual velocity.'
    % (fmt(ratio), fmt([v[0] for v in vfac], 3), fmt([v[1] for v in vfac], 4),
       fmt([v[2] for v in vfac], 4)),
    max(abs(r - 2.0) for r in ratio) < 3e-3
    and max(abs(v[1] - v[2]) for v in vfac) < 0.03,
)

bands = {}
for nm, vals in (("(2,1)", slow_f), ("(1,1)", slow_e), ("(2,0)", slow_k)):
    bands[nm] = (float(np.mean(vals)), float(np.ptp(vals)))
rel_f = bands["(2,1)"][1] / abs(bands["(2,1)"][0])
check(
    'B4 [finite near-rest diagnostic] Five mass rows %s: (2,1) mean %+.5f, spread %.4f, relative %.1e; (1,1) %+.5f/spread %.4f; (2,0) %+.5f/spread %.4f. The exact gapped Dirac-rest symbol is -4 beta.'
    % (fmt(slow_f, 4), bands["(2,1)"][0], bands["(2,1)"][1], rel_f,
       bands["(1,1)"][0], bands["(1,1)"][1], bands["(2,0)"][0], bands["(2,0)"][1]),
    rel_f < 1e-2 and abs(bands["(2,1)"][0] - UNIVERSAL) < 0.03
    and abs(bands["(2,0)"][0]) < 0.05,
)

ALS = (0.5, 1.0, 1.5, 2.0, 3.0)
sweep = [row(L, 0.0, 0.7854, (al, 1.0))[0] for al in ALS]
flat = [row(L, 1.0, 0.0, (al, 1.0))[0] for al in (0.5, 3.0)]
check(
    'B5 [finite weight sweep] Massless coefficients %s versus -4 alpha %s, relative residual %.1e; massive near-rest values %s. These declared dials are not selected physical couplings.'
    % (fmt(sweep, 4), fmt([-4 * a for a in ALS], 4),
       max(abs(s + 4 * a) / (4 * a) for s, a in zip(sweep, ALS)), fmt(flat, 4)),
    max(abs(s + 4 * a) / (4 * a) for s, a in zip(sweep, ALS)) < 5e-3
    and max(abs(f - UNIVERSAL) for f in flat) < 0.05,
)

pl = packet(L, 0.0, (0.5, 0.0, 0.0), 32.0, None, mode="band")
lon = {ab: response(L, 0.0, ab, pl) for ab in (FULL, ENERGY)}
lr = lon[FULL]["a"] / lon[ENERGY]["a"]
er = lon[FULL]["dEdt"] / lon[ENERGY]["dEdt"]
check(
    'B6 [finite longitudinal residual] Coefficients %+.5f/%+.5f retain %.1f percent shortfall from +8/+4; ratio %.5f, ratio error %.0e and energy-rate ratio %.5f. The residual cause and full error budget are unvalidated.'
    % (lon[FULL]["a"], lon[ENERGY]["a"], 100 * (1 - lon[ENERGY]["a"] / 4.0), lr,
       abs(lr - 2.0), er),
    abs(lr - 2.0) < 5e-3 and abs(er - 2.0) < 0.02 and lon[FULL]["a"] > 7.0,
)

# ================================== C. THE EQUIVALENCE PRINCIPLE, AS IT ACTUALLY HOLDS

# Three bodies of EQUAL energy, all with p_y sharp on Ly = 32 (a multiple of pi/8),
# the two masses solved for so that E matches the massless body's exactly.
E_STAR = disp((0.0, 0.7854, 0.0), 0.0)
M_REST = E_STAR
M_FAST = float(np.sqrt(E_STAR ** 2 - (2 - 2 * np.cos(0.3927))))
FIXE = (("at rest", M_REST, 0.0), ("massless", 0.0, 0.7854), ("fast massive", M_FAST, 0.3927))
fx_f, fx_e, fx_x, fx_E = [], [], [], []
for nm, m, py in FIXE:
    ef, r44f, _ = row(L, m, py, FULL)
    ee, _, _ = row(L, m, py, ENERGY)
    E = r44f["E"]
    fx_f.append(ef)
    fx_e.append(ee)
    fx_E.append(E)
    fx_x.append(-4 * (1 + (1 - m * m / E ** 2)))
sp_f = float(np.ptp(fx_f)) / abs(float(np.mean(fx_f)))
sp_e = float(np.ptp(fx_e)) / abs(float(np.mean(fx_e)))
check(
    'C1 [finite nominal-energy comparison] Energies %s, (2,1) coefficients %s/spread %.0f percent versus 1+chi targets %s; (1,1) %s/spread %.3f percent. Actual equal-speed modes can differ; no position-and-speed-only trajectory theorem.'
    % (fmt(fx_E, 4), fmt(fx_f, 4), 100 * sp_f, fmt(fx_x, 4), fmt(fx_e, 4), 100 * sp_e),
    sp_f > 0.30 and sp_e < 1e-3
    and max(abs(a - x) / abs(x) for a, x in zip(fx_f, fx_x)) < 0.03,
)

# ================================================= D. THE NEW SYSTEMATIC

# The two-level block at fixed q: Eps = sigma_z, M = E_0 sigma_x, {M, Eps} = 0.
m2, E02 = 1.3, 0.9
Z2 = np.array([[1.0, 0.0], [0.0, -1.0]])
M2 = E02 * np.array([[0.0, 1.0], [1.0, 0.0]])
H2 = M2 + m2 * Z2
E2v = np.sqrt(m2 ** 2 + E02 ** 2)
ev2, U2 = np.linalg.eigh(H2)
up, dn = U2[:, 1], U2[:, 0]
diag_el = abs(abs(float(up @ Z2 @ up)) - m2 / E2v)
off_el = abs(abs(float(up @ Z2 @ dn)) - E02 / E2v)
mix_e = abs(float(up @ H2 @ dn))                       # (1,1): Phi multiplies H0
mix_f = abs(float(up @ (2 * M2 + m2 * Z2) @ dn))       # (2,1): Phi multiplies 2M + m Eps
mix_x = abs(mix_f - m2 * E02 / E2v)
check(
    'D1 [uniform fixed-q block] Two-level spectrum %.1e, diagonal Gamma identity %.1e, off-diagonal identity %.1e; uniform (1,1) interband element %.1e versus (2,1) %.4f. This cancellation does not hold for general nonuniform fields; band labels do not derive particle ontology.'
    % (abs(ev2[1] - E2v), diag_el, off_el, mix_e, mix_f),
    max(abs(ev2[1] - E2v), diag_el, off_el, mix_x) < 1e-14 and mix_e < 1e-14 and mix_f > 0.1,
)

# The window test: the same packets, dt = 0.25 and T = 12, so the interband
# oscillation at frequency 2E is resolved rather than aliased.
zit_f, zit_e, zdr = [], [], []
for m in (0.5, 1.0, 2.0):
    _, ps = tuned(L, m, 0.0, SIG[1])
    rf = response(L, m, FULL, ps, T=12.0, dt=0.25)
    re_ = response(L, m, ENERGY, ps, T=12.0, dt=0.25)
    zit_f.append(rf["a_std"])
    zit_e.append(re_["a_std"])
    zdr.append(rf["a"])
_, ps0 = tuned(L, 0.0, 0.7854, SIG[1])
zit_0 = response(L, 0.0, FULL, ps0, T=12.0, dt=0.25)["a_std"]
zit_0e = response(L, 0.0, ENERGY, ps0, T=12.0, dt=0.25)["a_std"]
res_f = max(abs(a - UNIVERSAL) for a in slow_f) / 4.0
res_l = max(abs(a - 2 * UNIVERSAL) for a in lite_f) / 8.0
check(
    'D2 [finite window scatter] Massive (2,1) scatters %s versus (1,1) %s; means %s. Massless scatters %.5f/%.5f; relative massive/light residuals %.1f/%.2f percent. These measurements do not determine a complete interband error mechanism.'
    % (fmt(zit_f, 3), fmt(zit_e, 3), fmt(zdr, 3), zit_0, zit_0e,
       100 * res_f, 100 * res_l),
    min(zit_f) > 10 * max(zit_e) and zit_0 < 0.05 and res_f < 0.01 and res_l < 0.003,
)

# ======================================================= E. THE SOURCE, UNCHANGED

hop_only = LS._coo(0.5 * LS.vhop * (Phi_s[LS.r] + Phi_s[LS.c])).tocsr()
src = float(abs(LS.HPhi(M_A, Phi_s, FULL) - LS.HPhi(M_A, Phi_s, ENERGY) - hop_only).max())
src2 = float(abs(LS.HPhi(M_A, Phi_s, FULL) - LS.HPhi(M_A, Phi_s, ENERGY)
                 - 0.5 * (DPhi @ Mop + Mop @ DPhi)).max())
check(
    'E1 [external-field identity] H(2,1)-H(1,1)={Phi,M}/2: bond residual %.1e, anticommutator residual %.1e. No physical T00 source, Poisson solve, beta=1 authority or alpha=2 derivation follows.'
    % (src, src2),
    src < 1e-15 and src2 < 1e-15,
)

print(
    'SUMMARY: two declared weights give exact trigonometric scalar-symbol acceleration. Chi is a hop fraction; equal actual speeds can accelerate differently. Uniform block cancellation has a nonuniform counterexample. Finite packet ratios do not derive gravity.'
)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
