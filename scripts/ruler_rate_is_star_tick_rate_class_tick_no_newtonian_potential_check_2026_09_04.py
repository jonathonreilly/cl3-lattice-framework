"""Finite star/class rate maps on supplied static Regge and fermion models.

The original A1-A7/B1-B4/C1-C5/D1-D3/E1-E2 numerical experiments are retained.
Only the finite declared momenta/tori and the stated linear model are tested.
The S1 endpoint-mean identity and C2/incidence Fourier symbols have algebraic
proofs in the note; no physical rate, clock, metric, formation process or
universal unit classification is derived. Repeated endpoint events are a
supplied counting model, not repeated formation of permanent same-site Records.

The retained norm fraction is Theta(L^-4)=Theta(N^-4/3), on even cubic tori;
the adjacent-difference ratio is a different statistic. Class indicators form
a scaled isometry, normalized by sqrt(8/N). The sea residual tests conditional
stationarity on named fixtures, not averaged-law response at rare event rates.

R4 is the only imported local module, for its finite complex/Bloch construction.
The copied g4/G1 blocks below preserve the original source provenance labels;
those unavailable scratch scripts are historical attributions, not additional
executed suppliers. A1 compares actual copied construction to the current R4
functions at its declared momentum. Wider R4 gravity claims are not assumed.
All current note/proof interfaces and R4 are pinned before any scientific work.
Original source and numerical cache are preserved in the dated history.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/THE_RULERS_PER_SITE_FORMATION_RATE_IS_THE_STAR_TICKS_RATE_UNDER_THE_SUM_SHARING_RULE_AND_THE_SEA_PRESERVING_CLASS_TICK_CARRIES_NO_NEWTONIAN_POTENTIAL_BOUNDED_NOTE_2026-09-04.md',
 'docs/MINIMAL_AXIOMS_2026-06-29.md',
 'docs/THE_FORMATION_RATE_DEFINES_THE_STATIC_REGGE_EDGE_LENGTHS_EXACTLY_REGGE_IS_THE_LATTICE_POISSON_EQUATION_AND_FORCES_NU_R_EQUAL_ONE_BOUNDED_THEOREM_NOTE_2026-09-03.md',
 'docs/THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_OF_THE_SUPERLATTICE_ROLE_PATTERN_THE_EIGEN_SET_CRITERION_IS_ONE_PARTICLE_AND_ITS_MINIMAL_SETS_ARE_THE_PARITY_CLASSES_BOUNDED_NOTE_2026-09-04.md',
 'docs/THE_STAR_TICKS_RECORD_LAW_IS_EXACTLY_DETERMINANTAL_WITH_A_ROTATED_KERNEL_THE_SECOND_READING_KEEPS_THE_RULER_THE_BORN_STRUCTURE_AND_THE_TT_READING_AND_COSTS_THE_SEA_AS_VACUUM_BOUNDED_NOTE_2026-09-05.md',
 'docs/THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md',
 'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py')
INPUT_SHA256 = {'docs/THE_RULERS_PER_SITE_FORMATION_RATE_IS_THE_STAR_TICKS_RATE_UNDER_THE_SUM_SHARING_RULE_AND_THE_SEA_PRESERVING_CLASS_TICK_CARRIES_NO_NEWTONIAN_POTENTIAL_BOUNDED_NOTE_2026-09-04.md': '70d13b1be62bbc31cec249bc8758ecc94e820f5e14917a34699dd1b3ae55840b',
 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
 'docs/THE_FORMATION_RATE_DEFINES_THE_STATIC_REGGE_EDGE_LENGTHS_EXACTLY_REGGE_IS_THE_LATTICE_POISSON_EQUATION_AND_FORCES_NU_R_EQUAL_ONE_BOUNDED_THEOREM_NOTE_2026-09-03.md': '45105f11c6691355252339d7886f842cf2d49288cff0dfd39d0f1beb7b042fd6',
 'docs/THE_FORMATION_UNIT_THAT_PRESERVES_THE_SEA_IS_A_WHOLE_CLASS_OF_THE_SUPERLATTICE_ROLE_PATTERN_THE_EIGEN_SET_CRITERION_IS_ONE_PARTICLE_AND_ITS_MINIMAL_SETS_ARE_THE_PARITY_CLASSES_BOUNDED_NOTE_2026-09-04.md': '60f8bb7819810c64216e556f69de9b900599783451849c2ecf91da32d6600e8a',
 'docs/THE_STAR_TICKS_RECORD_LAW_IS_EXACTLY_DETERMINANTAL_WITH_A_ROTATED_KERNEL_THE_SECOND_READING_KEEPS_THE_RULER_THE_BORN_STRUCTURE_AND_THE_TT_READING_AND_COSTS_THE_SEA_AS_VACUUM_BOUNDED_NOTE_2026-09-05.md': '700ae72e5801e0d45121d852b7c4a5659ed529cfa47f8ecf80b8ec1c6c3953de',
 'docs/THE_RECORD_DENSITY_RULER_IS_ONE_PRODUCT_KAPPA_NU_EQUALS_ONE_AND_THE_HALF_FILLED_SEA_SUPPLIES_ZERO_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'b825a35dcb4f73488ddd06d4607eb40f8a6e87b34ca0f44c6098bd963cf10b99',
 'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py': '537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce'}


def require_inputs(root):
    from pathlib import Path
    import hashlib
    root=Path(root)
    for rel,expected in INPUT_SHA256.items():
        path=root/rel
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
            raise RuntimeError("missing or changed scientific input: "+rel)

from pathlib import Path
require_inputs(Path(__file__).resolve().parents[1])


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
check("A5 on the four nonzero test momenta C2 residual vanishes at "
      "nu = K(k); distinct K values exclude one constant on these samples", ok5,
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
check("A7 the four nonzero affine-source tests distinguish nu_r = 1 "
      "and give optional scalar-symbol ratio 1 + kappa_r nu_r = 2; coordinate scalar TT comparators vanish",
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
      "Phi_{x+e_a}), and the C2 clock matches the supplied point-source profile off the source up to its torus offset", okB1,
      f"8^3, 12^3 dev <= {max(b_extra):.1e}; staggered term {b_clock[0]:.3f}, {b_clock[1]:.3f} of the mean")
check("B2 the endpoint-mean part alone is exactly on shell; the staggered term has Bloch amplitude "
      "(1 + e^{i k_a})/2 Phi(k + Q), the potential at the partner momentum",
      okB2, f"8^3, 12^3 dev <= {max(b_bloch):.1e}")
check("B3 under V2 the residual is EXACTLY A_s(k) Phi(k + Q) and the source the even cover sees carries "
      "the inverse kernel 2M/K(k)", okB3,
      f"dev <= {max(b_id[0][0], b_id[1][0]):.1e}; tt excess {b_id[0][1]:.4e}, {b_id[1][1]:.4e}")
check("B4 the even cover is NOT a vacuum solution: under V1 the sampled small-momentum residual is order one, "
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
      "scaling as Theta(L^-4)=Theta(N^-4/3) by the separate lattice-sum proof", okC2,
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
check("D3 the class map R^8 -> R^N is a scaled isometry (Gram = (N/8) I, condition 1, rank 8) whose "
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
              "stationary in this tested flat example; no classification of other geometries",
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
check("E2 named conditional stationary-branch residuals carry no event-rate parameter: a single corner and a class minus one "
      "corner have the same residual; the declared whole-class patterns pass",
      okE2, "; ".join(e_rows))


# Corrections: normalization and rare-event averaging are distinct from stationarity.
def correction_controls():
    L = 6; N = L ** 3
    _, labels = parity(L)
    C = np.stack([(labels == c).ravel().astype(float) for c in range(8)], 1)
    J = C * np.sqrt(8.0 / N)
    T = torus(L); lam = T["khat2"][T["nz"]]
    n2 = np.sum((T["K3"][T["nz"]] * L / (2 * np.pi)) ** 2, axis=1)
    # sin(pi |n|/L) lies between 2|n|/L and pi|n|/L on centered modes.
    bounds = np.all(lam >= 16*n2/L**2 - 1e-12) and np.all(lam <= 4*np.pi**2*n2/L**2 + 1e-12)
    check("F1 normalized class indicators and the spectral bounds underlying N^(-4/3)",
          np.allclose(J.T @ J, np.eye(8), atol=1e-14) and bounds,
          "Gram(C)=(N/8)I; 16|n|^2/L^2 <= khat^2 <= 4pi^2|n|^2/L^2; summable |n|^-4 in dimension3")
    rho0 = np.diag([1.,0.]); rho1 = np.diag([0.,1.]); rows=[]
    for event_p in (1., .1, .001):
        d = np.sum(np.abs(np.linalg.eigvalsh((1-event_p)*rho0+event_p*rho1-rho0)))
        rows.append(float(d))
    check("F2 a fixed conditional disturbance can have an arbitrarily small averaged rate effect",
          np.allclose(rows,[2.,.2,.002],atol=1e-14),
          "conditional trace norm=2; averaged trace norms="+str(rows)+"; no physical event law supplied")

correction_controls()

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
sys.exit(1 if FAIL else 0)
