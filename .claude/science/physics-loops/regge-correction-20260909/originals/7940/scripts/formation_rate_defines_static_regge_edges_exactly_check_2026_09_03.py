"""The formation rate defines the static Regge edge lengths exactly: on the 4D cubic-Coxeter complex
T(Z^3 x Z_tau) the linearised Regge equations, evaluated on the rate-induced edge-length field with
the endpoint-mean rule, ARE the 6-NN lattice Poisson equation on the temporal edges, they force the
spatial exponent nu_r = 1, and the propagating modes are not rate fluctuations.

PROVENANCE (load-bearing). The complex, the 15 edge classes, the 50 hinge classes per 4-cell, the
area and dihedral machinery, the Bloch Hessian bloch_Q, the line-averaged metric_map, the Euclidean
linearised Einstein pairing and the nonlinear box action are the landed 3+1 runner's,
  scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py
imported as module R4 (declared in AUDIT_INPUT_PATHS). Nothing is imported from any unmerged branch.
The helpers below are COPIED, not imported, from the probe scripts that produced the result; each
block names the function it reproduces:
  precompute_terms  reproduces g1_rate_regge_check.precompute_terms, itself the graviton runner's
                    (PR #7910) precompute_terms: every area-gradient / deficit-gradient row of the
                    landed tri_rows written as sum_j c_j exp(i k.a_j) e_{class_j}, real c_j, real a_j.
  Q_grid            reproduces g1_rate_regge_check.Q_grid: the landed bloch_Q batched over real k.
  Q_an              reproduces the graviton runner's Qan: the holomorphic continuation of bloch_Q,
                    conj(x(k)) -> x(-k), valid at complex k_tau = i omega.
  M_grid, M_map     reproduce g1_rate_regge_check.M_grid: 'line' = the landed metric_map (midpoint
                    phase x sinc, written in its entire form (exp(2iz)-1)/(2iz)); 'am' = the
                    endpoint-mean rule, phase (1 + exp(i k.v))/2, the ruler's Phibar = (Phi_v+Phi_j)/2.
  QEH               reproduces g1_rate_regge_check.QEH: einstein_pairing_4d recast as ten quadratic
                    coefficient matrices, so it evaluates at any k without sympy.
  h_nu, gauge_invariants, the static L^3 grid, the pseudo-inverse solve and the zero-mode projection
                    reproduce g1_rate_regge_check (grid section) and g1_refine (sections 1-3).
  T6 reproduces g1_timedep; T7 reproduces g1_endtoend (A) and (B).

CONVENTIONS. Euclidean/OS0 signature. HCOMPS order xx,yy,zz,tt,xy,xz,xt,yz,yt,zt (tick = index 3).
Rate law r_v = r_0 (1 + Phi_v) (kappa_r = 1); tick = proper time gives l_tau = l_0 (1 + Phi); the
spatial edge l_s = l_0 (1 - nu Phi). The 15-class edge field is the metric map applied to
h_nu = Phi (-2nu, -2nu, -2nu, +2, 0, ...): delta l = M h_nu. Euler-Lagrange residual E = Q delta l;
metric-projected residual E_h = M^dagger E. khat^2 = sum_i 4 sin^2(k_i/2) is the symbol of the
6-NN lattice Laplacian (the Lattice axiom's adjacency). Static source: Phi(k) = -M/khat^2, unit
mass M = 1, neutralised (Phi(k=0) = 0), so nabla^2_lat Phi = M (delta - 1/N).

CHECKS (all machine-exact statements are tested at 1e-12; no seeds; no fitted constant):
  T1a provenance: Q_grid, Q_an, M_grid('line') and QEH reproduce the landed bloch_Q, metric_map and
      einstein_pairing_4d at declared real momenta.
  T1b dispersion witness: at k_tau = i omega with 4 sinh^2(omega/2) = khat^2 the continued Hessian
      has nullity 7 (5 kinematic + 2 propagating) and nullity 5 off shell -- the graviton runner's
      exact dispersion, reproduced from the copied code.
  T2a the exact identity at declared incommensurate static momenta: M_AM^dag Q M_AM h_1 = -khat^2 e_tt
      and Q M_AM h_1 = -2 khat^2 e_tau; every diagonal edge class drops out.
  T2b position space on the 8^3 torus: (Q delta l_rate)_tau(x) = 2 M (delta_x0 - 1/N), all other
      classes zero: the linearised Regge equation is the lattice Poisson equation on temporal edges.
  T3a the residual is linear in nu; its tt slot is -nu khat^2 exactly for every nu.
  T3b the (nu - 1) coefficient is the anisotropic-stress (tidal) operator c Q_EH, c = -1/2, at O(k^2),
      and is nonzero at every declared momentum: nu != 1 fails exactly.
  T4a a pure worldline source sigma e_tau lies in range Q(k) at every static k; dim ker Q(k) = 5.
  T4b the exact lattice solution equals the rate field (M = sigma/2) after zero-mode projection, at
      the declared momenta and at every site of the 8^3 torus; Psi/Phi = 1, Phi khat^2 = -1/2.
  T5  the landed line-average rule is NOT exact: nonzero residual, source coefficient 0.900 not 1.
  T6a a time-dependent rate ansatz is not a vacuum solution: its residual carries spatial and mixed
      slots of the size of the tt slot, matching c Q_EH h_1 at O(k^2).
  T6b the rate direction has zero overlap with both TT polarisations, spans 1 of the 6 physical
      metric degrees of freedom, and is not annihilated on shell where the two propagating modes are.
  T7a the position-space endpoint-mean rule Fourier-transforms to M_AM(k) h (anchor convention).
  T7b the landed NONLINEAR box action S_R on a periodic 3^4 box, second-differenced along the
      rate-induced field, equals (N/2) Re[u^dag Q u] and the identity's prediction (N/2)(-khat^2)(2).

MEMORY: largest dense object (512, 15, 15). RUNTIME: ~15 s (the sympy dihedral build dominates).
SUPPLIED, NOT DERIVED: S_R, its orientation and G; the Euclidean/OS0 reading; the tick
identification l_tau = r/r_0; the worldline coupling S_m = m sum l_tau; linear order; the rate law
with kappa_r = 1 (the conditional chain of PR #7925); the reading "edge length = records registered
along the edge" and the endpoint mean as a record count.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

import itertools
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


def check(name, cond, detail=""):
    global PASS, FAIL
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")
    if detail:
        print(f"       {detail}")
    PASS += int(bool(cond))
    FAIL += int(not cond)
    return bool(cond)


HC = R4.HCOMPS
TAU = R4.DIR_IDX[(0, 0, 0, 1)]
DIRS = np.array(R4.DIRS15, float)
NS = DIRS[:, :3].sum(1)
NT = DIRS[:, 3]
L0 = np.sqrt((DIRS ** 2).sum(1))
E_TT = np.zeros(10); E_TT[3] = 1.0
E_TAU = np.zeros(15); E_TAU[TAU] = 1.0
TOL = 1e-12

# ------------------------------------------------------------------ declared momenta (no seeds)
K_PIN = np.array([0.41, -0.23, 0.67, 0.0])                        # T1a provenance, real
K_QEH = np.array([0.3, -0.2, 0.5, 0.0])                           # T1a QEH recast
K_STATIC = [np.array([0.37, -0.81, 0.22, 0.0]),                   # T2-T5 incommensurate static k
            np.array([1.9, 0.4, -2.3, 0.0]),
            np.array([2.9, 2.7, -3.0, 0.0]),
            np.array([0.013, 0.007, -0.02, 0.0])]
K_SMALL = {"axis": np.array([0.05, 0.0, 0.0, 0.0]),               # T3b/T6a continuum comparator
           "face": np.array([0.05, 0.05, 0.0, 0.0]) / np.sqrt(2.0)}
K_DISP = [np.array([0.5, 0.0, 0.0]),                              # T1b/T6b spatial momenta
          np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0),
          2.0 * np.array([2.0, 1.0, 0.0]) / np.sqrt(5.0)]
K_TDEP = [np.array([0.05, 0.0, 0.0, 0.05]), np.array([0.4, 0.2, -0.3, 0.5])]   # T6a
L_GRID = 8                                                        # T2b/T4/T5 torus
L_BOX = 3                                                         # T7b box


# ------------------------------------------------------------------ copied: precompute_terms
def precompute_terms():
    """Copied from g1_rate_regge_check.precompute_terms (= PR #7910 precompute_terms): the landed
    tri_rows rewritten as (anchors, weight matrix) pairs per hinge class, built from R4's own
    TRI_CLASSES, STARS, AREA, THETA, edge_class, PAIRS5."""
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
    """Copied from g1_rate_regge_check.Q_grid: the landed bloch_Q at every row of real K (N, 4)."""
    N = K.shape[0]
    Q = np.zeros((N, 15, 15), complex)
    for (anc_a, Wa), (anc_d, Wd) in zip(A_TERMS, D_TERMS):
        A = np.exp(1j * (K @ anc_a.T)) @ Wa
        D = np.exp(1j * (K @ anc_d.T)) @ Wd
        Q += 0.5 * (np.conj(A)[:, :, None] * D[:, None, :] + np.conj(D)[:, :, None] * A[:, None, :])
    return Q


def Q_an(k):
    """Copied from the graviton runner's Qan: bloch_Q continued to complex k by conj(x(k)) -> x(-k)."""
    k = np.asarray(k, complex)
    Q = np.zeros((15, 15), complex)
    for (anc_a, Wa), (anc_d, Wd) in zip(A_TERMS, D_TERMS):
        Ap, Am = np.exp(1j * (anc_a @ k)) @ Wa, np.exp(-1j * (anc_a @ k)) @ Wa
        Dp, Dm = np.exp(1j * (anc_d @ k)) @ Wd, np.exp(-1j * (anc_d @ k)) @ Wd
        Q += 0.5 * (np.outer(Am, Dp) + np.outer(Dm, Ap))
    return Q


def _phase(kv, mode):
    """'line': the landed midpoint phase x sinc in its entire form; 'am': the endpoint mean."""
    if mode == "am":
        return 0.5 * (1.0 + np.exp(1j * kv))
    z = kv / 2.0
    small = np.abs(z) < 1e-13
    zs = np.where(small, 1.0, z)
    return np.where(small, 1.0 + 0j, (np.exp(2j * zs) - 1.0) / (2j * zs))


def M_grid(K, mode):
    """Copied from g1_rate_regge_check.M_grid: edge-length response (N, 15, 10) to h e^{ik.x}."""
    K = np.asarray(K, complex)
    N = K.shape[0]
    M = np.zeros((N, 15, 10), complex)
    for ci, vv in enumerate(DIRS):
        ph = _phase(K @ vv, mode)
        for hj, (a, b) in enumerate(HC):
            M[:, ci, hj] = ph * vv[a] * vv[b] * (2 if a != b else 1) / (2 * L0[ci])
    return M


def M_map(k, mode):
    return M_grid(np.asarray(k, complex)[None], mode)[0]


# ------------------------------------------------------------------ copied: QEH recast, h_nu, invariants
_E4 = np.eye(4)
_C = {}
for _m in range(4):
    _C[(_m, _m)] = R4.einstein_pairing_4d(_E4[_m])
for _m in range(4):
    for _n in range(_m + 1, 4):
        _C[(_m, _n)] = R4.einstein_pairing_4d(_E4[_m] + _E4[_n]) - _C[(_m, _m)] - _C[(_n, _n)]


def QEH(k):
    """Copied from g1_rate_regge_check.QEH: the landed einstein_pairing_4d as a quadratic form in k."""
    out = np.zeros((10, 10))
    for (m, n), Cm in _C.items():
        out += (k[m] * k[n]) * Cm
    return out


def h_nu(nu):
    v = np.zeros(10)
    v[0] = v[1] = v[2] = -2.0 * nu
    v[3] = 2.0
    return v


def khat2_of(k):
    return float((4 * np.sin(np.asarray(k, float)[:3] / 2) ** 2).sum())


def gauge_invariants(h, K3):
    """Copied from g1_rate_regge_check.gauge_invariants: Phi_gi = h_tt/2, Psi_gi = -(1/4) P_ij h_ij."""
    kk = 2 * np.sin(K3 / 2)
    hij = np.zeros((h.shape[0], 3, 3), complex)
    for hj, (a, b) in enumerate(HC):
        if a < 3 and b < 3:
            hij[:, a, b] += h[:, hj]
            if a != b:
                hij[:, b, a] += h[:, hj]
    tr = np.einsum("nii->n", hij)
    kk2 = (kk ** 2).sum(1)
    kk2[kk2 == 0] = 1
    kkh = np.einsum("ni,nij,nj->n", kk, hij, kk) / kk2
    return h[:, 3] / 2, -(tr - kkh) / 4


def null_space(Q, tol=1e-9):
    w, V = np.linalg.eigh((Q + Q.conj().T) / 2)
    return V[:, np.abs(w) < tol]


def nullity(Q, rel=1e-10):
    """(number of relative singular values below rel, ascending normalised singular values)."""
    s = np.sort(np.linalg.svd(Q, compute_uv=False))
    return int((s / s.max() < rel).sum()), s / s.max()


def fmt(x):
    return f"{x:.1e}"


def main() -> int:
    print("T(Z^3 x Z_tau), Euclidean/OS0: the rate-induced edge field delta l = M_AM h_nu against Q(k)")
    print(f"  {len(R4.DIRS15)} edge classes, {len(R4.TRI_CLASSES)} hinge classes per 4-cell; "
          f"h_nu = Phi(-2nu,-2nu,-2nu,+2); khat^2 = sum 4 sin^2(k_i/2)")

    # ---------------------------------------------------------------- T1a
    dq = float(np.abs(Q_grid(K_PIN[None])[0] - R4.bloch_Q(K_PIN)).max())
    dqa = float(np.abs(Q_an(K_PIN) - R4.bloch_Q(K_PIN)).max())
    dm = float(np.abs(M_map(K_PIN, "line") - R4.metric_map(K_PIN)).max())
    de = float(np.abs(QEH(K_QEH) - R4.einstein_pairing_4d(K_QEH)).max())
    check("T1a provenance: Q_grid, Q_an, M_grid('line') and QEH reproduce the landed bloch_Q, "
          "metric_map and einstein_pairing_4d",
          dq < TOL and dqa < TOL and dm < TOL and de < TOL,
          f"max|Q_grid-bloch_Q| {fmt(dq)}, |Q_an-bloch_Q| {fmt(dqa)}, |M_line-metric_map| {fmt(dm)}, "
          f"|QEH-pairing| {fmt(de)}")

    # ---------------------------------------------------------------- T1b
    rows, ok = [], True
    for ks in K_DISP:
        om = 2.0 * np.arcsinh(np.sqrt(khat2_of(ks)) / 2.0)
        n_on, s_on = nullity(Q_an(np.r_[ks, 1j * om]))
        n_off, _ = nullity(Q_an(np.r_[ks, 1.05j * om]))
        ok &= (n_on == 7 and n_off == 5 and s_on[7] > 1e-3)
        rows.append(f"|k|={np.linalg.norm(ks):.2f} om={om:.4f} null {n_on}/{n_off} "
                    f"s7={fmt(s_on[6])} s8={fmt(s_on[7])}")
    check("T1b dispersion witness: 4 sinh^2(omega/2) = khat^2 puts exactly two propagating modes on "
          "shell (nullity 7 on shell, 5 off shell) at every declared spatial momentum",
          ok, "; ".join(rows))

    # ---------------------------------------------------------------- T2a
    worst_h, worst_e, worst_diag, ok_lin, worst_lin = 0.0, 0.0, 0.0, True, 0.0
    line_res = []
    for k in K_STATIC:
        k2 = khat2_of(k)
        Qk, Ma, Ml = Q_an(k), M_map(k, "am"), M_map(k, "line")
        E = Qk @ Ma @ h_nu(1.0)
        Eh = Ma.conj().T @ E
        worst_h = max(worst_h, float(np.abs(Eh + k2 * E_TT).max()))
        worst_e = max(worst_e, float(np.abs(E + 2 * k2 * E_TAU).max()))
        worst_diag = max(worst_diag, float(np.abs(np.delete(E, TAU)).max()))
        line_res.append(float(np.abs(Ml.conj().T @ Qk @ Ml @ h_nu(1.0) + k2 * E_TT).max()))
        Eh0 = Ma.conj().T @ Qk @ Ma @ h_nu(0.0)
        Eh2 = Ma.conj().T @ Qk @ Ma @ h_nu(2.0)
        worst_lin = max(worst_lin, float(np.abs(Eh0 + Eh2 - 2 * Eh).max()))
        for nu in (0.0, 0.5, 2.0):
            Ehn = Ma.conj().T @ Qk @ Ma @ h_nu(nu)
            ok_lin &= abs(Ehn[3] + nu * k2) < TOL
    check("T2a exact identity at 4 declared incommensurate static momenta: M_AM^dag Q M_AM h_1 = "
          "-khat^2 e_tt and Q M_AM h_1 = -2 khat^2 e_tau; the 14 other edge classes drop out",
          worst_h < TOL and worst_e < TOL and worst_diag < TOL,
          f"khat^2 = {', '.join(f'{khat2_of(k):.5g}' for k in K_STATIC)}; worst |E_h + khat^2 e_tt| "
          f"{fmt(worst_h)}, |E + 2 khat^2 e_tau| {fmt(worst_e)}, non-temporal classes {fmt(worst_diag)}")

    # ---------------------------------------------------------------- static grid (shared by T2b/T4/T5)
    L = L_GRID
    n = np.fft.fftfreq(L) * L
    NX, NY, NZ = np.meshgrid(n, n, n, indexing="ij")
    K3 = 2 * np.pi * np.stack([NX.ravel(), NY.ravel(), NZ.ravel()], 1) / L
    K = np.concatenate([K3, np.zeros((K3.shape[0], 1))], 1)
    khat2 = (4 * np.sin(K3 / 2) ** 2).sum(1)
    nz = khat2 > 1e-12
    Nsites = K.shape[0]
    Phi = np.zeros(Nsites)
    Phi[nz] = -1.0 / khat2[nz]
    Q = Q_grid(K)
    MAM, MLI = M_grid(K, "am"), M_grid(K, "line")

    def ifft3(F):
        return np.fft.ifftn(F.reshape(L, L, L)).real

    dl_rate = np.einsum("nij,nj->ni", MAM, Phi[:, None] * h_nu(1.0)[None, :])
    E = np.einsum("nij,nj->ni", Q, dl_rate)
    Ex = np.stack([ifft3(E[:, c]) for c in range(15)], -1)
    target = np.zeros((L, L, L)); target[0, 0, 0] = 2.0; target -= 2.0 / Nsites
    dev_tau = float(np.abs(Ex[..., TAU] - target).max())
    dev_oth = float(np.abs(np.delete(Ex, TAU, axis=-1)).max())
    check(f"T2b position space, {L}^3 torus, unit mass: (Q delta l_rate)_tau(x) = 2M (delta_x0 - 1/N) and "
          "every other edge class vanishes at every site -- the lattice Poisson equation on temporal edges",
          dev_tau < TOL and dev_oth < TOL,
          f"E_tau(0) = {Ex[0, 0, 0, TAU]:+.6f} (2 - 2/N = {2 - 2 / Nsites:.6f}); max dev temporal "
          f"{fmt(dev_tau)}, other classes {fmt(dev_oth)}")

    # ---------------------------------------------------------------- T3a
    check("T3a nu-linearity: E_h(nu) is affine in nu, E_h(0) + E_h(2) = 2 E_h(1), and its tt slot is "
          "-nu khat^2 exactly for nu in {0, 1/2, 2}",
          worst_lin < TOL and ok_lin, f"worst |E_h(0)+E_h(2)-2E_h(1)| {fmt(worst_lin)}; tt slot exact")

    # ---------------------------------------------------------------- T3b
    names = ["xx", "yy", "zz", "tt", "xy"]
    ok3b, cells, worst_cmp = True, [], 0.0
    for nm, k in K_SMALL.items():
        k2, kc2 = khat2_of(k), float(k @ k)
        Qk, Ma = Q_an(k), M_map(k, "am")
        for nu in (0.0, 2.0):
            lat = (Ma.conj().T @ Qk @ Ma @ h_nu(nu)).real * (-1.0 / k2)
            con = -0.5 * QEH(k) @ h_nu(nu) * (-1.0 / kc2)
            dev = float(np.abs(lat[:5] - con[:5]).max())
            worst_cmp = max(worst_cmp, dev)
            ok3b &= dev < 5e-3
            if nu == 0.0:
                cells.append(f"{nm} nu=0: " + " ".join(f"{names[i]}={lat[i]:+.4f}/{con[i]:+.4f}"
                                                        for i in (0, 1, 2, 3, 4)))
    dmin = min(float(np.abs(np.delete((M_map(k, 'am').conj().T @ Q_an(k) @ M_map(k, 'am')
                                       @ (h_nu(2.0) - h_nu(1.0))) / khat2_of(k), 3)).max())
               for k in K_STATIC)
    print("  " + "; ".join(cells) + "  (lattice/continuum, Phi = -1/khat^2 resp. -1/k^2)")
    check("T3b the (nu-1) coefficient is the tidal operator c Q_EH (c = -1/2) at O(k^2), with spatial "
          "slots that do not vanish at any declared momentum: nu != 1 fails exactly",
          ok3b and dmin > 1e-2,
          f"worst lattice-continuum deviation {fmt(worst_cmp)} at |k| = 0.05; smallest max spatial "
          f"|D_ij|/khat^2 over the 4 static momenta {dmin:.3f}")

    # ---------------------------------------------------------------- T4a
    worst_c, kers = 0.0, set()
    for k in K_STATIC:
        Qk = Q_an(k)
        dl = np.linalg.pinv(Qk, rcond=1e-9) @ E_TAU
        worst_c = max(worst_c, float(np.abs(Qk @ dl - E_TAU).max()))
        kers.add(null_space(Qk).shape[1])
    Qp = np.linalg.pinv(Q[nz], rcond=1e-9)
    dl_ex = np.einsum("nij,j->ni", Qp, E_TAU)
    cons = float(np.abs(np.einsum("nij,nj->ni", Q[nz], dl_ex) - E_TAU[None, :]).max())
    kers |= {null_space(Q[i]).shape[1] for i in np.where(nz)[0]}
    check("T4a a pure worldline source sigma e_tau lies in range Q(k): the static equations with a "
          "point-mass worldline are solvable and dim ker Q(k) = 5 (4 gauge + 1 flat branch)",
          worst_c < 1e-10 and cons < 1e-10 and kers == {5},
          f"max|Q dl_ex - e_tau| {fmt(worst_c)} (declared k), {fmt(cons)} ({int(nz.sum())} torus momenta); "
          f"ker dims {sorted(kers)}")

    # ---------------------------------------------------------------- T4b
    # At the declared momenta the pseudo-inverse solve is conditioned at ~1/khat^2 (6e-4 at the
    # smallest one), so its own residual sits at ~1e-11; the identity T2a is the exact statement
    # and this comparison is held at 1e-9. The torus comparison (smallest khat^2 = 0.586) is at 1e-12.
    worst_d = 0.0
    for k in K_STATIC:
        Qk, Ma = Q_an(k), M_map(k, "am")
        dl = np.linalg.pinv(Qk, rcond=1e-9) @ E_TAU
        dr = Ma @ h_nu(1.0) * (-0.5 / khat2_of(k))
        Z = null_space(Qk)
        d = dl - dr
        d -= Z @ (Z.conj().T @ d)
        worst_d = max(worst_d, float(np.abs(d).max() / np.abs(dr).max()))
    dl_ex_k = np.zeros((Nsites, 15), complex); dl_ex_k[nz] = dl_ex
    dl_r = 0.5 * dl_rate
    diff = dl_ex_k - dl_r
    for i in np.where(nz)[0]:
        Z = null_space(Q[i])
        diff[i] -= Z @ (Z.conj().T @ diff[i])
    dx = np.sqrt((np.stack([ifft3(diff[:, c]) for c in range(15)], -1) ** 2).sum(-1))
    rx = np.sqrt((np.stack([ifft3(dl_r[:, c]) for c in range(15)], -1) ** 2).sum(-1))
    Mp = np.linalg.pinv(MAM[nz])
    Pg, Sg = gauge_invariants(np.einsum("nij,nj->ni", Mp, dl_ex), K3[nz])
    order = np.argsort(khat2[nz])[:6]
    ratio = (Sg / Pg)[order]
    gk = (Pg * khat2[nz])[order]
    ok_gi = bool(np.abs(ratio - 1).max() < 1e-9 and np.abs(gk + 0.5).max() < 1e-9)
    check("T4b the exact lattice solution IS the rate field (M = sigma/2) once the 5 zero modes are "
          "projected out, at the declared momenta and at every torus site; Psi/Phi = 1 and "
          "Phi khat^2 = -1/2 at the six smallest momenta",
          worst_d < 1e-9 and float(dx.max()) < TOL and ok_gi,
          f"relative residual {fmt(worst_d)} (declared k, solve conditioned at 1/khat^2); "
          f"position space max|diff| {fmt(float(dx.max()))} "
          f"vs |dl_rate|(r=1) {rx[1, 0, 0]:.3e}; Psi/Phi-1 {fmt(float(np.abs(ratio - 1).max()))}, "
          f"Phi khat^2+1/2 {fmt(float(np.abs(gk + 0.5).max()))}")

    # ---------------------------------------------------------------- T5
    dl_line = np.einsum("nij,nj->ni", MLI, Phi[:, None] * h_nu(1.0)[None, :])
    Eh_line = np.einsum("nji,nj->ni", np.conj(MLI), np.einsum("nij,nj->ni", Q, dl_line))
    src_line = float(ifft3(Eh_line[:, 3])[0, 0, 0] * Nsites / (Nsites - 1))
    Eh_am = np.einsum("nji,nj->ni", np.conj(MAM), E)
    src_am = float(ifft3(Eh_am[:, 3])[0, 0, 0] * Nsites / (Nsites - 1))
    rel_small = line_res[3] / khat2_of(K_STATIC[3])
    check("T5 the landed line-average rule is NOT exact and the endpoint mean is: line residuals are "
          "nonzero at every declared momentum and its source coefficient is 0.900, not 1",
          min(line_res[:3]) > 1e-4 and rel_small > 1e-8 and abs(src_line - 1) > 0.05
          and abs(src_am - 1) < TOL,
          f"line |E_h + khat^2 e_tt| = {', '.join(fmt(r) for r in line_res)} (last relative {fmt(rel_small)}); "
          f"source coefficient line {src_line:.5f}, endpoint mean {src_am:.5f}")

    # ---------------------------------------------------------------- T6a
    nm10 = ["xx", "yy", "zz", "tt", "xy", "xz", "xt", "yz", "yt", "zt"]
    ok6, cells = True, []
    for j, k in enumerate(K_TDEP):
        k4 = float((4 * np.sin(k / 2) ** 2).sum())
        Qk, Ma = Q_an(k), M_map(k, "am")
        lat = (Ma.conj().T @ Qk @ Ma @ h_nu(1.0)) / k4
        con = -0.5 * QEH(k) @ h_nu(1.0) / float(k @ k)
        spatial = float(np.abs(lat[[0, 1, 2]]).max()); mixed = float(np.abs(lat[[6, 8, 9]]).max())
        ok6 &= spatial > 0.1 and mixed > 0.1
        if j == 0:
            ok6 &= float(np.abs(lat - con).max()) < 5e-3
        klab = "(" + ",".join(f"{x:g}" for x in k) + ")"
        cells.append(f"k={klab}: " + " ".join(f"{nm10[i]}={lat[i].real:+.3f}/{con[i]:+.3f}"
                                              for i in (0, 3, 6, 8, 9) if abs(con[i]) > 1e-12 or i in (0, 3, 6)))
    print("  " + "; ".join(cells) + "  (lattice/continuum, per khat^2_4D resp. k^2)")
    check("T6a a time-dependent rate ansatz is NOT a vacuum solution: its residual carries spatial and "
          "mixed (momentum-density) slots of the size of the tt slot, the continuum c Q_EH h_1 at O(k^2)",
          ok6, "spatial and mixed slots > 0.1 of khat^2_4D at both declared 4-momenta; deviation from "
               "continuum at |k| = 0.07 < 5e-3")

    # ---------------------------------------------------------------- T6b
    tt_xy = float(h_nu(1.0) @ np.eye(10)[4]); tt_pm = float(h_nu(1.0) @ (np.eye(10)[0] - np.eye(10)[1]))
    Gh = np.zeros((10, 4), complex)
    k = np.r_[K_DISP[0], 0.0]
    for jj in range(4):
        for i, (a, b) in enumerate(HC):
            Gh[i, jj] = (1j * k[a] if b == jj else 0.0) + (1j * k[b] if a == jj else 0.0)
    phys_rank = 10 - np.linalg.matrix_rank(Gh)
    rows, ok6b = [], True
    for ks in K_DISP:
        om = 2.0 * np.arcsinh(np.sqrt(khat2_of(ks)) / 2.0)
        kk = np.r_[ks, 1j * om]
        Qk, Ma = Q_an(kk), M_map(kk, "am")
        u = Ma @ h_nu(1.0)
        r = float(np.linalg.norm(Qk @ u) / np.linalg.norm(u))
        ok6b &= r > 0.1
        rows.append(f"|k|={np.linalg.norm(ks):.2f}: |Q u_rate|/|u_rate| = {r:.3f}")
    check("T6b the propagating modes are not rate fluctuations: the rate direction (-2,-2,-2,+2) has "
          "zero overlap with both TT polarisations, spans 1 of the 6 physical metric d.o.f., and is not "
          "annihilated on shell where the two propagating modes are",
          tt_xy == 0.0 and tt_pm == 0.0 and phys_rank == 6 and ok6b,
          f"overlaps h_xy {tt_xy:.0f}, h_xx-h_yy {tt_pm:.0f}; physical d.o.f. 10 - 4 = {phys_rank}; " + "; ".join(rows))

    # ---------------------------------------------------------------- T7a
    Lp = 8
    kA = np.array([2 * np.pi / Lp, 2 * np.pi * 2 / Lp, 0.0, 0.0])
    h = h_nu(1.0)
    Hm = np.zeros((4, 4))
    for hj, (a, b) in enumerate(HC):
        Hm[a, b] += h[hj]
        if a != b:
            Hm[b, a] += h[hj]
    u = M_map(kA, "am") @ h
    X = np.array(list(itertools.product(range(Lp), repeat=3)), float)
    worst7 = 0.0
    for c, vv in enumerate(DIRS):
        phi0 = np.cos(X @ kA[:3]); phi1 = np.cos((X + vv[:3]) @ kA[:3])
        fld = (vv @ Hm @ vv) / (2 * L0[c]) * 0.5 * (phi0 + phi1)
        pred = np.real(u[c] * np.exp(1j * (X @ kA[:3])))
        worst7 = max(worst7, float(np.abs(pred - fld).max()))
    check("T7a anchor convention: the position-space endpoint-mean rule delta l_e(x) = (v^T h v)/(2l) "
          "(Phi(x)+Phi(x+v))/2 equals Re[M_AM(k) h e^{ikx}] at every site and class",
          worst7 < TOL, f"max deviation {fmt(worst7)} on the {Lp}^3 torus at k = 2pi(1,2,0)/{Lp}")

    # ---------------------------------------------------------------- T7b
    kc = np.array([2 * np.pi / L_BOX, 0.0, 0.0, 0.0])
    ub = M_map(kc, "am") @ h

    def eps_scaled(t):
        def f(cls, anc):
            return t * float(np.real(ub[cls] * np.exp(1j * np.dot(kc, anc))))
        return f
    hh = 1e-4
    s_p, s_0, s_m = (R4.box_action(L_BOX, eps_scaled(t)) for t in (+hh, 0.0, -hh))
    fd2 = (s_p - 2 * s_0 + s_m) / hh ** 2
    Nb = L_BOX ** 4
    pred_bloch = (Nb / 2.0) * float(np.real(np.conj(ub) @ R4.bloch_Q(kc) @ ub))
    pred_ident = (Nb / 2.0) * (-khat2_of(kc)) * float(h @ E_TT)
    check(f"T7b the landed NONLINEAR Regge action on the periodic {L_BOX}^4 box, second-differenced along "
          "the rate-induced field, equals (N/2) Re[u^dag Q u] and the identity's (N/2)(-khat^2)(h_tt = 2)",
          abs(fd2 - pred_bloch) / abs(pred_bloch) < 1e-4 and abs(pred_bloch - pred_ident) < 1e-9
          and abs(s_0) < 1e-9,
          f"finite difference {fd2:.6f}; Bloch {pred_bloch:.6f}; identity {pred_ident:.6f}; "
          f"S_R(flat) = {s_0:.1e}")

    print()
    print("SUPPLIED, not derived: S_R, its orientation and G; the OS0 reading; l_tau = r/r_0; the")
    print("worldline coupling; linear order; the rate law with kappa_r = 1; the record-count reading.")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
