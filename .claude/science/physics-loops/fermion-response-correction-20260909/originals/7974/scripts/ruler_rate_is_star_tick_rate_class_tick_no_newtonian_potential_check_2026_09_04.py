"""The ruler's per-site formation rate is the star tick's rate under the sum sharing rule, which is
the endpoint mean exactly; the sea-preserving class tick has Fourier support {0, pi}^3 and carries no
Newtonian potential.

The ruler chain puts a record formation rate r_v at a coarse corner of 2Z^3 whose records are the six
coarse edge sites of its star; the tick lane's formation units are the star of one corner and the
whole parity class of corners.  This runner puts both units on the landed 4D cubic-Coxeter complex
under two declared sharing rules for a record site shared by two stars (S1 sum, S2 even cover) and
two declared clock readings for a corner (C1 own ticks, C2 records in the star), and measures what
each unit's geometry does to the linearised Regge equations.

PROVENANCE (load-bearing).  The complex, the 15 edge classes, the 50 hinge classes per 4-cell, the
area and dihedral machinery, the Bloch Hessian bloch_Q, the line-averaged metric_map and the
Euclidean linearised Einstein pairing are the landed 3+1 runner's,
  scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py
imported as module R4 (declared in AUDIT_INPUT_PATHS).  Nothing is imported from any unmerged
branch.  Every helper below is COPIED, not imported, from the probe scripts that produced the
result; each block names the source block it reproduces:
  precompute_terms, Q_grid, Q_an, M_grid, M_map, QEH, h_nu, h_split
                    reproduce the "copied from G1 (unchanged)" block of g4_common.py, which is the
                    G1 runner's own copy (scripts/formation_rate_defines_static_regge_edges_exactly_
                    check_2026_09_03.py) of the landed tri_rows, bloch_Q, metric_map and
                    einstein_pairing_4d; 'line' = the landed metric_map, 'am' = the endpoint mean.
  torus, parity, c_of, kernel_K, nn_mean, edge_site_rates, corner_counts, build_edge_field,
  fft_field, ifft_field
                    reproduce the "new: torus, rates, readings" block of g4_common.py: the corner
                    lattice as an L^3 torus, the sharing rules S1/S2, the clock readings C1/C2 and
                    the position-space 15-class edge field in G1's anchor convention.
  A1-A7            reproduce g4_a_star_sum.py (star tick, sharing S1, clocks C1 and C2).
  B1-B4            reproduce g4_b_even_cover.py (star tick under T2's even cover S2, clock C2).
  C1-C5            reproduce g4_c_class.py (the class tick on 6^3, 8^3, 12^3).
  D1-D3            reproduce g4_d_converse.py (the C2 map, the S1 incidence map, the class map).
  E1-E2            reproduce g4_e_sea.py (T2's one-particle eigen-set criterion, re-implemented).

CONVENTIONS.  Euclidean/OS0 signature.  HCOMPS order xx,yy,zz,tt,xy,xz,xt,yz,yt,zt (tick = index 3).
The corner lattice of the complex is the fermion law's coarse corner lattice 2Z^3 and the record
sites are the coarse edge sites, each shared by exactly two corners.  Star rate r_S(v) = r_S0
(1 + Phi_v) with r_S0 = 1 and kappa_r = 1.  Sharing S1: a record site's record forms at each tick of
either of its two stars, r_e = r_S(u) + r_S(u').  Sharing S2 (T2's even cover): only the even-parity
stars tick, r_e = r_S(even endpoint).  Clock C1: a corner's proper time counts its own star's ticks.
Clock C2: it counts the records registered at the six record sites of its star.  Axis spatial edges
read the record site at nu_r = 1; the recordless diagonal classes take G1's metric rule, with the
declared variants V1 (they follow the corner clock) and V2 (they follow the even-sublattice field
Psi = 2 Phi_e).  khat^2 = sum_i 4 sin^2(k_i/2); the static source is a unit point mass at the even
corner 0 of an L^3 torus, Phi(k) = -M/khat^2, M = 1, Phi(0) = 0.  Declared momenta (G1's, no seeds):
(0.37,-0.81,0.22), (1.9,0.4,-2.3), (2.9,2.7,-3.0), (0.013,0.007,-0.02); declared tori 6^3, 8^3,
12^3 (7^3 for the odd-L contrast, 4^3 for the flat sea case).

CHECKS (machine-exact statements are tested at 1e-12 unless a looser tolerance is named; no seeds,
no fitted constant, no PDG value):
  A1  provenance: the copied Q_grid and M_grid('line') reproduce the landed bloch_Q and metric_map.
  A2a sharing S1 IS the endpoint-mean rule identically, not only at first order.
  A2b (C1,S1): the star-rate edge field built in position space equals G1's M_AM h_1 Phi.
  A2c (C1,S1): linearised Regge IS the 6-NN lattice Poisson equation on the temporal edges.
  A3  (C2,S1): the clock kernel is K(k) = (1 + c(k))/2 = 1 - khat^2/12 exactly, K(pi,pi,pi) = 0.
  A4  (C2,S1): the tt (Poisson) equation is untouched; the spatial residual is exactly
      (khat^2/12)(A_s + khat^2 e_tt) and is nonzero at every declared momentum.
  A5  no constant exponent puts the C2 geometry on shell: it would need nu = K(k).
  A6  at |k| = 0.05 the C2 residual is (khat^2/12) times G1's continuum tidal pattern, tt zero.
  A7  (C1,S1) keeps G1's selections: nu != 1 off shell, bending 1 + kappa_r nu_r = 2, TT overlap 0.
  B1  S2 splits the record site into the endpoint mean plus a staggered bond gradient; the C2 clock
      is the Newtonian clock at every corner off the source.
  B2  the staggered term's Bloch amplitude is (1 + e^{i k_a})/2 Phi(k + Q), Q = (pi,pi,pi).
  B3  under V2 the metric-projected residual is exactly A_s(k) Phi(k + Q) and the source acquires
      the inverse kernel 2M/K(k) = 24M/(12 - khat^2).
  B4  the even cover is off shell at O(1) near the zone corner under both diagonal-class variants,
      and at every momentum under V1.
  C1  the class-tick edge field has Fourier support exactly {0, pi}^3 (7 nonzero amplitudes).
  C2  it keeps the closed-form fraction (3/16 + 3/64 + 1/144)/sum_k khat^-4 of ||Phi_N||^2.
  C3  its Regge residual is at least 1.001 of the source and the mass is spread over a whole class.
  C4  the clock difference between two corners of one class is exactly 0 at every separation.
  C5  the temporal equation sees the unit mass only as eight class totals.
  D1  the C2 map and the S1 incidence map have the staggered (pi,pi,pi) mode as exact kernel on even
      tori; their dense spectra match the symbols; their conditionings.
  D2  G1's record-site profile lies in the incidence range and the star rates are recovered exactly
      modulo that mode.
  D3  the class map is an isometric embedding of R^8 and loses N - 8 dimensions.
  E1  the 4^3 (1,1,1) torus is flat (h^2 = 6I): the only place where star = class.
  E2  the sea's price on 6^3 and 8^3: a single-corner unit and a class minus one corner both fail at
      O(1); the whole class is exact; the residual contains no rate.

MEMORY: largest dense objects (1728, 15, 15) complex, a 1536 x 512 incidence matrix and a 512 x 512
one-particle Hamiltonian; peak well under 0.5 GB.  RUNTIME: about 5 s (the sympy dihedral build of
the landed module dominates the start-up).  Exit code 1 if any check fails, 0 otherwise.
SUPPLIED, NOT DERIVED: G1's complex, action, orientation and G; the Euclidean/OS0 reading; the tick
identification l_tau = l_0 r_v/r_0; the worldline coupling; linear order; static sources; the rate
law r_v = r_0 (1 + Phi_v) with kappa_r = 1 and the whole conditional chain behind it; the
identification of the complex's corner lattice with the coarse corner lattice 2Z^3 and of the record
sites with the coarse edge sites; the star tick and the class tick; S1, S2, C1, C2, V1, V2; the
class means as class rates; the declared tori, momenta, twist sectors and pattern families; the
designed fermion law and the half-filled sea as vacuum.  The axioms supply none of it.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

import os
import sys

sys.dont_write_bytecode = True
import numpy as np

_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as R4      # noqa: E402

PASS = 0
FAIL = 0
TOL = 1e-12


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


def fmt(x):
    return f"{x:.1e}"


# ------------------------------------------------------------------ copied from g4_common.py (G1 block)
HC = R4.HCOMPS
TAU = R4.DIR_IDX[(0, 0, 0, 1)]
DIRS = np.array(R4.DIRS15, float)
L0 = np.sqrt((DIRS ** 2).sum(1))
E_TT = np.zeros(10); E_TT[3] = 1.0
AXIS = [R4.DIR_IDX[(1, 0, 0, 0)], R4.DIR_IDX[(0, 1, 0, 0)], R4.DIR_IDX[(0, 0, 1, 0)]]

K_PIN = np.array([0.41, -0.23, 0.67, 0.0])
K_STATIC = [np.array([0.37, -0.81, 0.22, 0.0]), np.array([1.9, 0.4, -2.3, 0.0]),
            np.array([2.9, 2.7, -3.0, 0.0]), np.array([0.013, 0.007, -0.02, 0.0])]
K_SMALL = {"axis": np.array([0.05, 0.0, 0.0, 0.0]),
           "face": np.array([0.05, 0.05, 0.0, 0.0]) / np.sqrt(2.0)}


def precompute_terms():
    """Copied from g4_common.precompute_terms (= the G1 runner's, = PR #7910's): every area- and
    deficit-gradient row of the landed tri_rows as sum_j c_j exp(i k.a_j) e_{class_j}."""
    a_terms, d_terms = [], []
    for tri in R4.TRI_CLASSES:
        vts = [np.array(x) for x in tri]
        qvals, einfo = [], []
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            cls, anc = R4.edge_class(tuple(vts[i]), tuple(vts[j]))
            v = np.array(R4.DIRS15[cls])
            qvals.append(float(v @ v))
            einfo.append((cls, anc, float(np.sqrt(v @ v))))
        aout = R4.AREA(*qvals)
        at = [(cls, np.array(anc, float), 2 * ell * float(aout[1 + n]))
              for n, (cls, anc, ell) in enumerate(einfo)]
        dt = []
        for vs in R4.STARS[tri]:
            loc = {v: i for i, v in enumerate(vs)}
            hl = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
            miss = tuple(sorted([i for i in range(5) if i not in hl]))
            qv, edata = [], []
            for (i, j) in R4.PAIRS5:
                cls, anc = R4.edge_class(vs[i], vs[j])
                v = np.array(R4.DIRS15[cls])
                qv.append(float(v @ v))
                edata.append((cls, anc, float(np.sqrt(v @ v))))
            out = R4.THETA[miss](*qv)
            dt += [(cls, np.array(anc, float), -2 * ell * float(out[1 + n]))
                   for n, (cls, anc, ell) in enumerate(edata)]
        for src, dst in ((at, a_terms), (dt, d_terms)):
            W = np.zeros((len(src), 15))
            anc = np.zeros((len(src), 4))
            for r, (cls, a, c) in enumerate(src):
                W[r, cls] = c
                anc[r] = a
            dst.append((anc, W))
    return a_terms, d_terms


A_TERMS, D_TERMS = precompute_terms()


def Q_grid(K):
    """Copied from g4_common.Q_grid: the landed bloch_Q batched over real momenta."""
    N = K.shape[0]
    Q = np.zeros((N, 15, 15), complex)
    for (anc_a, Wa), (anc_d, Wd) in zip(A_TERMS, D_TERMS):
        A = np.exp(1j * (K @ anc_a.T)) @ Wa
        D = np.exp(1j * (K @ anc_d.T)) @ Wd
        Q += 0.5 * (np.conj(A)[:, :, None] * D[:, None, :] + np.conj(D)[:, :, None] * A[:, None, :])
    return Q


def Q_an(k):
    """Copied from g4_common.Q_an: the same Hessian at one momentum."""
    k = np.asarray(k, complex)
    Q = np.zeros((15, 15), complex)
    for (anc_a, Wa), (anc_d, Wd) in zip(A_TERMS, D_TERMS):
        Ap, Am = np.exp(1j * (anc_a @ k)) @ Wa, np.exp(-1j * (anc_a @ k)) @ Wa
        Dp, Dm = np.exp(1j * (anc_d @ k)) @ Wd, np.exp(-1j * (anc_d @ k)) @ Wd
        Q += 0.5 * (np.outer(Am, Dp) + np.outer(Dm, Ap))
    return Q


def _phase(kv, mode):
    if mode == "am":
        return 0.5 * (1.0 + np.exp(1j * kv))
    z = kv / 2.0
    small = np.abs(z) < 1e-13
    zs = np.where(small, 1.0, z)
    return np.where(small, 1.0 + 0j, (np.exp(2j * zs) - 1.0) / (2j * zs))


def M_grid(K, mode="am"):
    """Copied from g4_common.M_grid: 'line' = the landed metric_map, 'am' = the endpoint mean."""
    K = np.asarray(K, complex)
    N = K.shape[0]
    M = np.zeros((N, 15, 10), complex)
    for ci, vv in enumerate(DIRS):
        ph = _phase(K @ vv, mode)
        for hj, (a, b) in enumerate(HC):
            M[:, ci, hj] = ph * vv[a] * vv[b] * (2 if a != b else 1) / (2 * L0[ci])
    return M


def M_map(k, mode="am"):
    return M_grid(np.asarray(k, complex)[None], mode)[0]


_E4 = np.eye(4)
_C = {}
for _m in range(4):
    _C[(_m, _m)] = R4.einstein_pairing_4d(_E4[_m])
for _m in range(4):
    for _n in range(_m + 1, 4):
        _C[(_m, _n)] = R4.einstein_pairing_4d(_E4[_m] + _E4[_n]) - _C[(_m, _m)] - _C[(_n, _n)]


def QEH(k):
    """Copied from g4_common.QEH: einstein_pairing_4d recast as ten quadratic coefficient matrices."""
    out = np.zeros((10, 10))
    for (m, n), Cm in _C.items():
        out += (k[m] * k[n]) * Cm
    return out


def h_nu(nu):
    v = np.zeros(10)
    v[0] = v[1] = v[2] = -2.0 * nu
    v[3] = 2.0
    return v


def h_split(nu_s, nu_t):
    """Copied from g4_common.h_split: (-2 nu_s I_3, +2 nu_t)."""
    v = np.zeros(10, complex)
    v[0] = v[1] = v[2] = -2.0 * nu_s
    v[3] = 2.0 * nu_t
    return v


def khat2_of(k):
    return float((4 * np.sin(np.asarray(k, float)[:3] / 2) ** 2).sum())


# ------------------------------------------------------------------ copied from g4_common.py (rates block)
def torus(L):
    """Copied from g4_common.torus: fft-ordered momenta, khat^2 and the unit point mass."""
    n = np.fft.fftfreq(L) * L
    NX, NY, NZ = np.meshgrid(n, n, n, indexing="ij")
    K3 = 2 * np.pi * np.stack([NX.ravel(), NY.ravel(), NZ.ravel()], 1) / L
    K = np.concatenate([K3, np.zeros((K3.shape[0], 1))], 1)
    khat2 = (4 * np.sin(K3 / 2) ** 2).sum(1)
    nz = khat2 > 1e-12
    Phi_k = np.zeros(K.shape[0])
    Phi_k[nz] = -1.0 / khat2[nz]
    Phi_x = np.fft.ifftn(Phi_k.reshape(L, L, L)).real
    return dict(L=L, N=L ** 3, K=K, K3=K3, khat2=khat2, nz=nz, Phi_k=Phi_k, Phi_x=Phi_x)


def c_of(K3):
    return np.cos(K3).sum(1) / 3.0


def kernel_K(K3):
    """Copied from g4_common.kernel_K: the C2 corner-count kernel (1 + c(k))/2."""
    return 0.5 * (1.0 + c_of(K3))


def parity(L):
    """Copied from g4_common.parity: eps(x) = (-1)^(x+y+z) and the class label (x,y,z) mod 2."""
    x = np.arange(L)
    X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    eps = (-1.0) ** (X + Y + Z)
    cls = (X % 2) * 4 + (Y % 2) * 2 + (Z % 2)
    return eps, cls


def nn_mean(f):
    out = np.zeros_like(f)
    for a in range(3):
        out += np.roll(f, 1, axis=a) + np.roll(f, -1, axis=a)
    return out / 6.0


def edge_site_rates(rS, sharing):
    """Copied from g4_common.edge_site_rates: S1 'sum' and S2 'even' at the bond x -> x + e_a."""
    L = rS.shape[0]
    eps, _ = parity(L)
    out = np.zeros((3,) + rS.shape)
    for a in range(3):
        nb = np.roll(rS, -1, axis=a)
        if sharing == "sum":
            out[a] = rS + nb
        elif sharing == "even":
            out[a] = np.where(eps > 0, rS, nb)
        else:
            raise ValueError(sharing)
    return out


def corner_counts(rS, sharing):
    """Copied from g4_common.corner_counts: reading C2, the records registered in star(x) per tick."""
    re = edge_site_rates(rS, sharing)
    tot = np.zeros_like(rS)
    for a in range(3):
        tot += re[a] + np.roll(re[a], 1, axis=a)
    return tot


def build_edge_field(Phi_s_bond, Phi_t, Phi_diag):
    """Copied from g4_common.build_edge_field: the 15-class position-space edge field, G1's anchor
    convention; axis classes from the record sites at nu_r = 1, the temporal class from the clock,
    the recordless diagonal classes from G1's metric rule."""
    L = Phi_t.shape[0]
    F = np.zeros((L, L, L, 15))
    for ci, w in enumerate(R4.DIRS15):
        ws = np.array(w[:3]); wt = w[3]
        ns = int(ws.sum())
        if ci == TAU:
            F[..., ci] = Phi_t
            continue
        if ci in AXIS:
            F[..., ci] = -Phi_s_bond[AXIS.index(ci)]
            continue
        g = (wt * Phi_t - ns * Phi_diag) / np.sqrt(wt + ns)
        sh = g
        for a in range(3):
            if ws[a]:
                sh = np.roll(sh, -1, axis=a)
        F[..., ci] = 0.5 * (g + sh)
    return F


def fft_field(F):
    L = F.shape[0]
    out = np.zeros((L ** 3, 15), complex)
    for c in range(15):
        out[:, c] = np.fft.fftn(F[..., c]).ravel()
    return out


def ifft_field(Fk, L):
    out = np.zeros((L, L, L, Fk.shape[1]))
    for c in range(Fk.shape[1]):
        out[..., c] = np.fft.ifftn(Fk[:, c].reshape(L, L, L)).real
    return out


_QCACHE = {}


def Q_of(T):
    if T["L"] not in _QCACHE:
        _QCACHE[T["L"]] = Q_grid(T["K"])
    return _QCACHE[T["L"]]


# ================================================================== A: star tick, sharing S1
dq = float(np.abs(Q_grid(K_PIN[None])[0] - R4.bloch_Q(K_PIN)).max())
dm = float(np.abs(M_map(K_PIN, "line") - R4.metric_map(K_PIN)).max())
check("A1 provenance: the copied Q_grid and M_grid('line') ARE the landed bloch_Q and metric_map",
      dq < TOL and dm < TOL, f"max|Q_grid-bloch_Q| {fmt(dq)}, |M_line-metric_map| {fmt(dm)}")

T8 = torus(8); N8 = T8["N"]; Phi8x = T8["Phi_x"]
rS = 1.0 + Phi8x
re_sum = edge_site_rates(rS, "sum")
Phi_bond = re_sum / 2.0 - 1.0
endpoint_mean = np.stack([0.5 * (Phi8x + np.roll(Phi8x, -1, axis=a)) for a in range(3)])
dev_am = float(np.abs(Phi_bond - endpoint_mean).max())
check("A2a sharing S1 IS the endpoint-mean rule identically: r_e/(2 r_S0) - 1 = (Phi_x + Phi_{x+e_a})/2 "
      "at every record site",
      dev_am < TOL, f"max deviation {fmt(dev_am)} over {3 * N8} record sites")

F_c1 = build_edge_field(Phi_bond, Phi8x, Phi8x)
dl1 = fft_field(F_c1)
MAM8 = M_grid(T8["K"], "am")
dl_g1 = np.einsum("nij,j->ni", MAM8, h_nu(1.0)) * T8["Phi_k"][:, None]
dev_field = float(np.abs(dl1 - dl_g1).max())
check("A2b (C1,S1): the star-rate edge field, built in position space, IS G1's M_AM(k) h_1 Phi(k)",
      dev_field < 1e-10, f"max|dl_star - dl_G1| {fmt(dev_field)} (|dl| up to {np.abs(dl_g1).max():.3f})")

Q8 = Q_of(T8)
E1x = ifft_field(np.einsum("nij,nj->ni", Q8, dl1), 8)
target = np.zeros((8, 8, 8)); target[0, 0, 0] = 2.0; target -= 2.0 / N8
dev_tau = float(np.abs(E1x[..., TAU] - target).max())
dev_oth = float(np.abs(np.delete(E1x, TAU, axis=-1)).max())
check("A2c (C1,S1): linearised Regge IS the lattice Poisson equation on the temporal edges, (Q dl)_tau(x) "
      "= 2M(delta_x0 - 1/N), the other 14 classes 0",
      dev_tau < 1e-10 and dev_oth < 1e-10,
      f"E_tau(0) = {E1x[0, 0, 0, TAU]:+.6f} = 2 - 2/N; dev {fmt(dev_tau)} and {fmt(dev_oth)}")

cnt = corner_counts(rS, "sum")
Phi_t2 = cnt / 12.0 - 1.0
dev_x = float(np.abs(Phi_t2 - 0.5 * (Phi8x + nn_mean(Phi8x))).max())
Kk8 = kernel_K(T8["K3"])
dev_k = float(np.abs(np.fft.fftn(Phi_t2).ravel() - Kk8 * T8["Phi_k"]).max())
dev_id = float(np.abs(Kk8 - (1.0 - T8["khat2"] / 12.0)).max())
check("A3 (C2,S1): the corner count is 6 r_S + sum_nn r_S, so Phi_t(k) = K(k) Phi(k) with K = (1 + c)/2 "
      "= 1 - khat^2/12 exactly and K(pi,pi,pi) = 0",
      dev_x < TOL and dev_k < 1e-10 and dev_id < TOL,
      f"position {fmt(dev_x)}, Bloch {fmt(dev_k)}, |K - (1 - khat^2/12)| {fmt(dev_id)}, min K {Kk8.min():.1e}")

rows = []; ok4 = ok5 = okK = True; ratios = []; bend = []; worst = 0.0; worst5 = 0.0
for k in K_STATIC:
    k2 = khat2_of(k); Kv = float(kernel_K(k[None, :3])[0])
    Qk, Ma = Q_an(k), M_map(k, "am")
    def Eh(h, Qk=Qk, Ma=Ma):
        return Ma.conj().T @ Qk @ Ma @ h
    E_c1 = Eh(h_split(1.0, 1.0)); E_c2 = Eh(h_split(1.0, Kv))
    A_s = Eh(h_split(1.0, 0.0)); A_t = Eh(h_split(0.0, 1.0))
    res_c1 = float(np.abs(E_c1 + k2 * E_TT).max())
    tt_c2 = float(abs(E_c2[3] + k2))
    res_c2 = E_c2 + k2 * E_TT
    dev_pred = float(np.abs(res_c2 - (k2 / 12.0) * (A_s + k2 * E_TT)).max())
    sp = float(np.abs(res_c2[[0, 1, 2, 4, 5, 7]]).max())
    ok4 &= res_c1 < 1e-11 and tt_c2 < 1e-11 and dev_pred < 1e-11 and float(abs(A_t[3])) < 1e-11
    worst = max(worst, res_c1, tt_c2, dev_pred, float(abs(A_t[3])))
    sp_fit = float(np.abs((Eh(h_split(Kv, Kv)) + Kv * k2 * E_TT)[[0, 1, 2, 4, 5, 7]]).max())
    ok5 &= sp_fit < 1e-11; worst5 = max(worst5, sp_fit)
    okK &= sp > 0.05 * k2 * (k2 / 12.0)
    ratios.append(sp / (k2 * k2 / 12)); bend.append(1 + 1 / Kv)
    rows.append(f"{k2:.5g}/{Kv:.5f}")
print("   declared momenta, khat^2/K: " + ", ".join(rows))
check("A4 the tt (Poisson) slot is -khat^2 Phi under BOTH clocks (A_t,tt = 0); the C2 spatial residual is "
      "exactly (khat^2/12)(A_s + khat^2 e_tt), nonzero at all 4 momenta", ok4 and okK,
      f"C1, C2 tt, A_t,tt and prediction <= {worst:.1e}; residual {min(ratios):.4f}-{max(ratios):.4f} khat^4/12")
check("A5 no constant exponent puts C2 on shell: the spatial residual of (-2nu I_3, +2K) vanishes iff "
      "nu = K(k), momentum-dependent", ok5,
      f"spatial residual at nu = K(k) <= {worst5:.1e}")

cells = {}; ok6 = True
for nm, k in K_SMALL.items():
    k2, kc2 = khat2_of(k), float(k @ k); Kv = float(kernel_K(k[None, :3])[0])
    res = (M_map(k, "am").conj().T @ Q_an(k) @ M_map(k, "am") @ h_split(1.0, Kv)
           + k2 * E_TT).real * (-1.0 / k2)
    con = (k2 / 12.0) * (0.5 * QEH(k) @ h_nu(0.0)) * (-1.0 / kc2)
    dev = float(np.abs(res[:5] - con[:5]).max())
    ok6 &= dev < 1e-3 * (k2 / 12.0)
    cells[nm] = res
check("A6 at |k| = 0.05 the C2 residual is (khat^2/12) times G1's continuum tidal pattern with tt exactly "
      "0: the star average costs a tidal stress, not a source term", ok6,
      f"axis yy = {cells['axis'][1]:+.2e}, zz = {cells['axis'][2]:+.2e}; face xx = {cells['face'][0]:+.2e}, "
      f"zz = {cells['face'][2]:+.2e}, xy = {cells['face'][4]:+.2e}")

tid = []
for k in K_STATIC:
    k2 = khat2_of(k); Ma = M_map(k, "am")
    D = (Ma.conj().T @ Q_an(k) @ Ma @ (h_nu(2.0) - h_nu(1.0))) / k2
    tid.append(float(np.abs(D[[0, 1, 2, 4, 5, 7]]).max()))
h1 = h_nu(1.0)
tt_xy = float(abs(h1 @ np.eye(10)[4])); tt_pm = float(abs(h1 @ (np.eye(10)[0] - np.eye(10)[1])))
check("A7 (C1,S1) keeps every G1 selection: nu != 1 needs a tidal stress at every momentum, so nu_r = 1 "
      "and alpha/beta = 1 + kappa_r nu_r = 2, and the TT overlap is still zero",
      min(tid) > 0.3 and tt_xy == 0.0 and tt_pm == 0.0 and abs(bend[3] - 2.0) < 1e-3,
      f"smallest spatial slot {min(tid):.3f}; overlaps 0, 0; under C2 it is 1 + 1/K = "
      f"{bend[0]:.4f}, {bend[1]:.4f}, {bend[2]:.4f}, {bend[3]:.4f}")

# ================================================================== B: the even cover S2
b_extra = []; b_clock = []; b_bloch = []; b_id = []; b_tab = []
okB1 = okB2 = okB3 = okB4 = True
for L in (8, 12):
    T = torus(L); N = T["N"]; Phi = T["Phi_x"]; K3 = T["K3"]; nz = T["nz"]; kh = T["khat2"]
    eps, _ = parity(L)
    rSb = 1.0 + Phi
    Phi_bond_b = edge_site_rates(rSb, "even") - 1.0
    am = np.stack([0.5 * (Phi + np.roll(Phi, -1, axis=a)) for a in range(3)])
    extra = Phi_bond_b - am
    pred_extra = np.stack([0.5 * eps * (Phi - np.roll(Phi, -1, axis=a)) for a in range(3)])
    dev_extra = float(np.abs(extra - pred_extra).max())
    Phi_t = corner_counts(rSb, "even") / 6.0 - 1.0
    dev_even = float(np.abs((Phi_t - Phi)[eps > 0]).max())
    dev_odd = float(np.abs((Phi_t - Phi)[eps < 0] + 1.0 / (6 * N)).max())
    okB1 &= dev_extra < TOL and dev_even < TOL and dev_odd < TOL
    b_extra.append(max(dev_extra, dev_even, dev_odd))
    b_clock.append(float(np.abs(extra).max() / np.abs(am).max()))

    Q = Q_of(T); MAM = M_grid(T["K"], "am")
    src = np.zeros((N, 15)); src[nz, TAU] = 2.0
    Psi = (1.0 + eps) * Phi
    Phi_kQ = np.roll(T["Phi_k"].reshape(L, L, L), (L // 2,) * 3, axis=(0, 1, 2)).ravel()
    g1_exact = float(np.abs(np.einsum("nij,nj->ni", Q, fft_field(build_edge_field(am, Phi, Phi))) - src)[nz].max())
    dev_bloch = max(float(np.abs(np.fft.fftn(extra[a]).ravel()
                                 - 0.5 * (1 + np.exp(1j * K3[:, a])) * Phi_kQ).max()) for a in range(3))
    okB2 &= g1_exact < 1e-10 and dev_bloch < 1e-10
    b_bloch.append(max(g1_exact, dev_bloch))

    small = nz & np.isclose(kh, kh[nz].min())
    isQ = np.isclose(kh, 12.0)
    dQ = np.sqrt(((np.abs(K3) - np.pi) ** 2).sum(1)); zc = (dQ <= 2 * np.pi / L + 1e-9) & ~isQ
    out = {}
    for nm, F in (("V1", build_edge_field(Phi_bond_b, Phi_t, Phi)),
                  ("V2", build_edge_field(Phi_bond_b, Phi_t, Psi))):
        E = np.einsum("nij,nj->ni", Q, fft_field(F)); Rr = E - src
        out[nm] = (float(np.linalg.norm(Rr[nz]) / np.linalg.norm(src[nz])),
                   float(np.abs(Rr[small]).max() / 2.0), float(np.abs(Rr[zc]).max() / 2.0),
                   np.einsum("nji,nj->ni", np.conj(MAM), E))
    As = np.einsum("nji,nj->ni", np.conj(MAM),
                   np.einsum("nij,nj->ni", Q, np.einsum("nij,j->ni", MAM, h_split(1.0, 0.0))))
    sel = nz & ~isQ
    Eh2 = out["V2"][3]
    dev_id = float(np.abs(Eh2[sel] + kh[sel, None] * E_TT[None, :] * T["Phi_k"][sel, None]
                          - As[sel] * Phi_kQ[sel, None]).max())
    tt_rel = Eh2[small, 3].real - 1.0
    dev_tt = float(np.abs(tt_rel - kh[small] / (12.0 - kh[small])).max())
    okB3 &= dev_id < 1e-10 and dev_tt < 1e-10
    b_id.append((dev_id, float(tt_rel.max())))
    okB4 &= (out["V1"][1] > 0.1 and out["V2"][1] < 0.1 and out["V1"][0] > 1 and out["V2"][0] > 1
             and out["V1"][2] > 1 and out["V2"][2] > 1)
    b_tab.append(f"{L}^3 V1 {out['V1'][0]:.3f}/{out['V1'][1]:.3f}/{out['V1'][2]:.2f}, "
                 f"V2 {out['V2'][0]:.3f}/{out['V2'][1]:.3e}/{out['V2'][2]:.2f}")

check("B1 under S2 the record site is the endpoint mean plus a staggered bond gradient (eps_x/2)(Phi_x - "
      "Phi_{x+e_a}), and the C2 clock is Newtonian at EVERY corner off the source", okB1,
      f"8^3, 12^3 dev <= {max(b_extra):.1e}; staggered term {b_clock[0]:.3f}, {b_clock[1]:.3f} of the mean")
check("B2 the endpoint-mean part alone is exactly on shell; the staggered term has Bloch amplitude "
      "(1 + e^{i k_a})/2 Phi(k + Q), the potential at the partner momentum",
      okB2, f"8^3, 12^3 dev <= {max(b_bloch):.1e}")
check("B3 under V2 the residual is EXACTLY A_s(k) Phi(k + Q) and the source the even cover sees carries "
      "the inverse kernel 2M/K(k)", okB3,
      f"dev <= {max(b_id[0][0], b_id[1][0]):.1e}; tt excess {b_id[0][1]:.4e}, {b_id[1][1]:.4e}")
check("B4 the even cover is NOT a vacuum solution: under V1 the residual is order one at every momentum, "
      "and under both variants several times the source near Q", okB4,
      "||R||/||src|| / max|R|/2M at min khat^2 / near Q: " + "; ".join(b_tab))

# ================================================================== C: the class tick
EVEN = (0, 3, 5, 6)
c_supp = []; c_frac = []; c_res = []; c_clock = []; c_tot = None
okC1 = okC2 = okC3 = okC4 = okC5 = True
for L in (6, 8, 12):
    T = torus(L); N = T["N"]; Phi = T["Phi_x"]; K3 = T["K3"]; nz = T["nz"]
    eps, cls = parity(L)

    def cproj(f, labels):
        o = np.zeros_like(f)
        for c in labels:
            m = cls == c
            o[m] = f[m].mean()
        return o

    Phi8c = cproj(Phi, range(8))
    Phi4 = cproj(Phi, EVEN); Phi4[eps < 0] = 0.0
    rSc = 1.0 + Phi4
    Phi_bond_c = edge_site_rates(rSc, "even") - 1.0
    Phi_tc = corner_counts(rSc, "even") / 6.0 - 1.0
    dl = fft_field(build_edge_field(Phi_bond_c, Phi_tc, Phi_tc))
    amp = np.abs(dl).max(1)
    on = amp > 1e-12 * amp.max()
    is_zone = np.all(np.isclose(np.abs(K3), np.pi) | np.isclose(K3, 0.0), axis=1)
    okC1 &= bool(np.all(is_zone[on])) and int(on.sum()) == 7
    c_supp.append(float(amp[~is_zone].max()))

    f8 = float((Phi8c ** 2).sum() / (Phi ** 2).sum())
    ana = (3 / 16 + 3 / 64 + 1 / 144) / float((T["Phi_k"][nz] ** 2).sum())
    okC2 &= abs(f8 - ana) < 1e-9 and f8 < 0.05
    c_frac.append(f8)

    E = np.einsum("nij,nj->ni", Q_of(T), dl)
    src = np.zeros_like(E); src[nz, TAU] = 2.0
    nrm = float(np.linalg.norm((E - src)[nz]) / np.linalg.norm(src[nz]))
    Et = ifft_field(E, L)[..., TAU]
    okC3 &= nrm > 1.001 and float(np.abs(Et[cls == 0] - Et[0, 0, 0]).max()) < 1e-10
    c_res.append(nrm)

    same = float(np.abs(Phi_tc[cls == 0] - Phi_tc[0, 0, 0]).max())
    adj = max(float(np.abs(Phi_tc - np.roll(Phi_tc, -1, axis=a)).max()) for a in range(3))
    adjN = max(float(np.abs(Phi - np.roll(Phi, -1, axis=a)).max()) for a in range(3))
    okC4 &= same < TOL and adj < 0.05 * adjN
    c_clock.append(adj / adjN)

    spread = max(float(np.abs(Et[cls == c] - Et[cls == c].flat[0]).max()) for c in range(8))
    sums = [float(Et[cls == c].sum()) for c in range(8)]
    okC5 &= spread < 1e-10 and abs(sum(sums)) < 1e-10
    if L == 8:
        c_tot = sums

check("C1 the class tick's edge field has Fourier support exactly {0, pi}^3, 7 nonzero Bloch amplitudes on "
      "each torus: a class has no extent, it is the whole lattice mod 2", okC1,
      f"max amplitude off {{0, pi}}^3 <= {max(c_supp):.1e}")
check("C2 it keeps only the closed-form fraction (3/16 + 3/64 + 1/144)/sum_k khat^-4 of ||Phi_N||^2, "
      "falling like 1/N", okC2,
      "6^3/8^3/12^3: " + "/".join(f"{f:.3e}" for f in c_frac) + " = 0.241319 over 15.856, 48.719, 238.77")
check("C3 it misses the point source: the Regge residual exceeds 1.001 of the source, and the equation it "
      "does satisfy has the mass spread over a whole class of N/8 corners", okC3,
      "residual 6^3/8^3/12^3: " + "/".join(f"{r:.4f}" for r in c_res))
check("C4 the clock difference between two corners of one class is EXACTLY 0 at every separation; the "
      "adjacent-corner difference is a small fraction of the Newtonian one",
      okC4, "adjacent/Newtonian, 6^3/8^3/12^3: " + "/".join(f"{r:.2e}" for r in c_clock))
check("C5 it sees the unit mass only as eight class totals, uniform within each class and summing to zero: "
      "a class-uniform rate carries eight numbers, no 1/r potential", okC5,
      "8^3 class totals: " + ", ".join(f"{s:+.4f}" for s in c_tot))

# ================================================================== D: the converse maps
def adjacency(L):
    N = L ** 3; A = np.zeros((N, N))
    idx = np.arange(N).reshape(L, L, L)
    for a in range(3):
        nb = np.roll(idx, -1, axis=a).ravel()
        A[np.arange(N), nb] = 1.0; A[nb, np.arange(N)] = 1.0
    return A


def incidence(L):
    """Copied from g4_d_converse.incidence: the unsigned S1 incidence, row (a, x) hitting x and x + e_a."""
    N = L ** 3; idx = np.arange(N).reshape(L, L, L)
    M = np.zeros((3 * N, N))
    for a in range(3):
        nb = np.roll(idx, -1, axis=a).ravel()
        rows = a * N + np.arange(N)
        M[rows, np.arange(N)] = 1.0; M[rows, nb] = 1.0
    return M


okD1 = True; d_rows = []; d_dev = 0.0
for L in (6, 7, 8, 12):
    T = torus(L); N = T["N"]; Kc = 1.0 - T["khat2"] / 12.0
    nzK = np.abs(Kc) > 1e-12
    rank = int(nzK.sum()); cond = 1.0 / float(np.abs(Kc[nzK]).min())
    sv = np.sqrt(12.0 * Kc[nzK]); condN = float(sv.max() / sv.min())
    okD1 &= (rank == N - 1) if L % 2 == 0 else (rank == N)
    d_rows.append(f"{L}^3 {cond:.2f}/{condN:.3f}" + ("" if L % 2 == 0 else " (odd L: no kernel)"))
    if L in (6, 8):
        Kd = 0.5 * (np.eye(N) + adjacency(L) / 6.0)
        dev = float(np.abs(np.sort(np.linalg.eigvalsh(Kd)) - np.sort(Kc)).max())
        Ninc = incidence(L)
        dev_s = float(np.abs(np.sort(np.linalg.svd(Ninc, compute_uv=False))
                             - np.sort(np.sqrt(np.maximum(12 * Kc, 0)))).max())
        eps, _ = parity(L)
        ker = float(np.abs(Ninc @ eps.ravel()).max()); kerK = float(np.abs(Kd @ eps.ravel()).max())
        okD1 &= dev < 1e-10 and dev_s < 1e-9 and ker < TOL and kerK < TOL
        d_dev = max(d_dev, dev, dev_s)
check("D1 the C2 map (I + A/6)/2 and the S1 incidence map both have the staggered (pi,pi,pi) mode as EXACT "
      "kernel on even tori (rank N - 1; none on odd L); the spectra match their symbols",
      okD1, f"dense dev <= {d_dev:.1e}; cond(C2)/cond(inc) " + ", ".join(d_rows))

T = torus(8); N = T["N"]; Phi = T["Phi_x"]; eps, cls = parity(8)
Ninc = incidence(8)
am = np.stack([0.5 * (Phi + np.roll(Phi, -1, axis=a)) for a in range(3)])
r_tgt = 2.0 * (1.0 + am).reshape(3 * N)
rS_ls, _, rk, _ = np.linalg.lstsq(Ninc, r_tgt, rcond=None)
in_range = float(np.abs(Ninc @ rS_ls - r_tgt).max())
e = eps.ravel() / np.sqrt(N)
truth = (1.0 + Phi).ravel()
dev_rec = float(np.abs((rS_ls - e * (e @ rS_ls)) - (truth - e * (e @ truth))).max())
check("D2 G1's record-site profile lies in the incidence range and least squares recovers the star rates "
      "modulo that mode: a (pi,pi,pi) clock modulation changes no record site",
      in_range < 1e-10 and dev_rec < 1e-10 and rk == N - 1,
      f"range residual {fmt(in_range)}; recovery {fmt(dev_rec)}; rank {rk} = N - 1")

C8 = np.stack([(cls == c).ravel().astype(float) for c in range(8)], 1)
gram = C8.T @ C8
Pc = C8 @ np.linalg.solve(gram, C8.T @ Phi.ravel())
loss = float(np.linalg.norm(Phi.ravel() - Pc) / np.linalg.norm(Phi.ravel()))
check("D3 the class map R^8 -> R^N is an isometric embedding (Gram = (N/8) I, condition 1, rank 8) whose "
      "left inverse is the class mean; it loses everything but eight means",
      np.allclose(gram, (N / 8) * np.eye(8)) and loss > 0.95,
      f"||Phi - P_class Phi||/||Phi|| = {loss:.5f} on 8^3; lost N - 8 = {N - 8}")

# ================================================================== E: the sea's price
def torus_h(L, twist):
    """Copied from g4_e_sea.torus_h: Kawamoto-Smit signs with the declared twist, h_ij = -eta_ij."""
    V = L ** 3; idx = np.arange(V).reshape(L, L, L)
    x = np.arange(L); X, Y, Z = np.meshgrid(x, x, x, indexing="ij")
    h = np.zeros((V, V))
    for a in range(3):
        eta = np.ones((L, L, L)) if a == 0 else ((-1.0) ** X if a == 1 else (-1.0) ** (X + Y))
        wrap = np.zeros((L, L, L), bool)
        sl = [slice(None)] * 3; sl[a] = L - 1; wrap[tuple(sl)] = True
        if twist[a]:
            eta = np.where(wrap, -eta, eta)
        nb = np.roll(idx, -1, axis=a)
        h[idx.ravel(), nb.ravel()] = -eta.ravel()
        h[nb.ravel(), idx.ravel()] = -eta.ravel()
    clsv = ((X % 2) * 4 + (Y % 2) * 2 + (Z % 2)).ravel()
    return h, clsv, idx


def null_space(C, tol=1e-10):
    if C.shape[0] == 0:
        return np.eye(C.shape[1])
    _, s, vt = np.linalg.svd(C, full_matrices=True)
    return vt[int(np.sum(s > tol)):].conj().T


def residual(h, W, S, pattern, tol=1e-10):
    """Copied from g4_e_sea.residual: T2's one-particle eigen-set criterion, re-implemented from T2's
    Theorem 1 -- U = R_{V minus S}(W restricted to e_{S1}^perp), residual ||(I - P_U) h_R U||_F."""
    V = h.shape[0]; N = W.shape[1]; S = list(S)
    Sc = [v for v in range(V) if v not in set(S)]
    hR = h[np.ix_(Sc, Sc)]
    S1 = [S[a] for a in range(len(S)) if pattern[a]]
    Z = null_space(W[S1, :]) if S1 else np.eye(N)
    if Z.shape[1] != N - len(S1):
        return None
    U0 = (W @ Z)[Sc, :]
    u, s, _ = np.linalg.svd(U0, full_matrices=False)
    r = int(np.sum(s > tol))
    if r != N - len(S1):
        return None
    U = u[:, :r]; hU = hR @ U
    return float(np.linalg.norm(hU - U @ (U.conj().T @ hU)))


def declared_patterns(m):
    """Copied from g4_e_sea.declared_patterns: all-empty, all-full, first, alternating, last, first-two."""
    pats = [tuple([0] * m), tuple([1] * m)]
    if m > 1:
        pats += [tuple([1] + [0] * (m - 1)), tuple([i % 2 for i in range(m)]),
                 tuple([0] * (m - 1) + [1]), tuple([1, 1] + [0] * (m - 2))]
    return pats


e_rows = []; okE2 = True
for L, twist in ((4, (1, 1, 1)), (6, (0, 0, 0)), (8, (1, 1, 1))):
    h, clsv, idx = torus_h(L, twist)
    V = L ** 3; Nh = V // 2
    w, Uv = np.linalg.eigh(h); W = Uv[:, :Nh]
    if L == 4:
        flat = float(np.abs(h @ h - 6 * np.eye(V)).max())
        r_corner4 = max(residual(h, W, [0], p) for p in [(0,), (1,)])
        check("E1 the 4^3 torus in its declared (1,1,1) sector is flat, h^2 = 6I, so a single corner IS "
              "its own class: the one place where star = class, an L = 4 cancellation",
              flat < 1e-12 and r_corner4 < 1e-10,
              f"|h^2 - 6I| {fmt(flat)}; single-corner residual {fmt(r_corner4)}")
        continue
    r_corner = max(residual(h, W, [0], p) for p in [(0,), (1,)])
    C0 = [v for v in range(V) if clsv[v] == 0]
    r_class = max(residual(h, W, C0, p) for p in declared_patterns(len(C0)))
    r_minus = max(residual(h, W, C0[1:], p) for p in declared_patterns(len(C0) - 1))
    okE2 &= r_corner > 0.3 and r_class < 1e-11 and r_minus > 0.3 and abs(r_minus - r_corner) < 1e-9
    e_rows.append(f"{L}^3 corner {r_corner:.4f}, class ({len(C0)} corners) {r_class:.1e}, "
                  f"class minus one {r_minus:.4f}")
check("E2 the star tick's price is order one and carries no rate: a single corner and a class minus one "
      "corner have the same residual, the whole class is exact",
      okE2, "; ".join(e_rows))

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
