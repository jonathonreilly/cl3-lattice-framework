"""Native linearised graviton on the 4D cubic-Coxeter complex T(Z^3 x Z_tau): the propagating-mode
census and the exact lattice dispersion of delta^2 S_Regge, read from the geometric action itself.

PROVENANCE (load-bearing). The complex, the edge classes, the hinge classes, the area and dihedral
machinery, the Bloch Hessian, the line-averaged metric map and the gauge map are NOT rebuilt here.
This runner IMPORTS the landed 3+1 runner
  scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py
as a library (module R4) and uses its own objects, so the complex analysed here is provably
identical to the landed one. The landed 3D runner is imported as R3 for the spatial comparator.
Both landed runners are re-executed in-process (gate T1) and must reproduce PASS=10 FAIL=0.

WHAT IS NEW. The landed 4D runner evaluates Q(k) only at REAL Euclidean momenta and never extracts
a dispersion: there is no omega(k), no pole and no finite-frequency mode count in it. This runner
adds exactly that. The signature is Euclidean/OS0, so the dispersion is read as the poles of the
lattice propagator by the holomorphic continuation of the tick momentum,
    k_tau = i*omega   (equivalently z = exp(i k_tau) = exp(-omega)).
Q(k) is entire in k -- every entry is a finite sum c_j exp(i k . a_j) with real c_j and real
anchors a_j -- so the continuation is unique. The landed bloch_Q writes conj(x(k)), which is valid
only for real k; the continuation replaces it by x(-k) (Qan below), and the same replacement is
made in the metric map (Man: the midpoint phase x sinc written as the entire (exp(2iz)-1)/(2iz)).
Gate T0 pins Qan and Man against the landed bloch_Q and metric_map at a declared real momentum.
The gauge map is already entire as landed and is used verbatim.

MEMORY. One 15x15 momentum-space Hessian per momentum; no position-space Hessian is built here.
No random seeds: every momentum is a declared constant of this module.

CHECKS:
  T0 continuation-provenance check   Qan/Man reproduce the landed bloch_Q/metric_map at a declared
      real momentum; the complex identity (24 path 4-simplices, 15 edge classes, 50 hinge classes
      per 4-cell) is read off the imported module.
  T1a landed-3D-reproduction check   the landed 3D runner reproduces PASS=10 FAIL=0 and its
      comparator numbers (c = -1/2 with direction spread ~1e-8; TT -0.25; transverse-trace +0.25).
  T1b landed-4D-reproduction check   the landed 3+1 runner reproduces PASS=10 FAIL=0.
  T2a kernel-census check            dim ker Q(k) = 5 at every declared momentum = 4 discrete
      diffeomorphisms + 1 identically flat non-metric branch; the metric-sector kernel is exactly 4.
  T2b continuum-gauge-family check   the metric-sector kernel is EXACTLY the continuum family
      h_munu = i(k_mu xi_nu + k_nu xi_mu), not merely approximately.
  T3  propagating-mode-count check   exactly one on-shell frequency per declared spatial momentum,
      doubly degenerate (sigma_6 ~ sigma_7 ~ 1e-17 against sigma_8 fourteen orders larger), over
      omega in (0,8] out to the zone boundary: no doubler, no spurious propagating branch.
  T4a exact-dispersion check         4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2) over declared zone
      points in five directions -- the zero set of the standard hypercubic k-hat^2.
  T4b small-k-expansion check        omega^2 = k^2 - (k^4/12)(1 + sum_i n_i^4) + O(k^6), against the
      exact rationals -1/6, -1/8, -1/9, -7/50: massless, light speed 1 in tick units.
  T4c isotropy check                 the direction spread of omega scales as k^2 relative, i.e.
      omega is isotropic at O(k^2) and anisotropic only at O(k^4).
  T4d multiplier-structure check     the lapse h_tautau and shift h_i,tau kinetic weights vanish on
      shell.
  T5  TT-fraction-and-comparator check  the two propagating polarisations are transverse-traceless
      up to gauge -- a small-k statement, degrading at the zone corner; and the landed
      target-operator row's omega = +-k across the zone is NOT reproduced by the geometric action.

SUPPLIED, NOT DERIVED (unchanged by this runner): the edge lengths as the geometric variables, the
selection of S_R as the action, its overall orientation, the Lorentzian signature, the nonlinear
completion, and the record-to-geometry link.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "scripts/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)

import contextlib
import io
import os
import re
import sys

import numpy as np

_SCRIPTS = os.path.dirname(os.path.abspath(__file__))
if _SCRIPTS not in sys.path:
    sys.path.insert(0, _SCRIPTS)

import frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09 as R3          # noqa: E402
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


# ------------------------------------------------------------------ declared momenta (no seeds)
K_PIN = np.array([0.37, -0.83, 0.51, 0.29])                      # T0 pinning momentum
K_KERNEL = [np.array([0.410, -0.230, 0.670, 0.310]),             # T2 census momenta
            np.array([1.100, 0.600, -0.400, 0.200]),
            np.array([2.300, 1.700, -2.900, 0.830]),
            np.array([0.013, 0.000, 0.000, 0.021])]
AXIS = np.array([1.0, 0.0, 0.0])
FACE = np.array([1.0, 1.0, 0.0]) / np.sqrt(2.0)
BODY = np.array([1.0, 1.0, 1.0]) / np.sqrt(3.0)
D210 = np.array([2.0, 1.0, 0.0]) / np.sqrt(5.0)
D211 = np.array([2.0, 1.0, 1.0]) / np.sqrt(6.0)
D312 = np.array([3.0, 1.0, 2.0]) / np.sqrt(14.0)
K_BRANCH = [0.3, 1.0, 2.0, 2.5, 3.0, np.pi]                      # T3 magnitudes, axis and body
K_ZONE = [0.1, 0.5, 1.0, 2.0, 3.0, np.pi, 4.0]                   # T4a magnitudes
K_SMALL = [0.05, 0.02, 0.01]                                     # T4b magnitudes
K_ISO = [0.02, 0.05, 0.10, 0.20, 0.80]                           # T4c magnitudes
K_POL = [0.05, 0.20, 0.80, 2.00, 3.00]                           # T5 magnitudes
K_CMP = [0.10, 0.40, 1.20, 2.00, 3.00]                           # T5 comparator magnitudes
NDIR = {"axis(100)": AXIS, "face(110)": FACE, "body(111)": BODY,
        "(2,1,0)": D210, "(2,1,1)": D211}
ZDIR = {"axis(100)": AXIS, "face(110)": FACE, "body(111)": BODY,
        "(2,1,0)": D210, "(3,1,2)": D312}
HIDX = {c: i for i, c in enumerate(R4.HCOMPS)}
NTRI = len(R4.TRI_CLASSES)


# ------------------------------------------------------------------ holomorphic continuation
def precompute_terms():
    """Each area-gradient and deficit-gradient row of the landed runner is
    sum_j coef_j exp(i k . anchor_j) e_{class_j} with real coef_j and k-independent anchors.
    Built here from the imported module's own edge classes, areas and dihedral derivatives."""
    a_terms, d_terms = [], []
    for tri in R4.TRI_CLASSES:
        vts = [np.array(x) for x in tri]
        qvals, einfo = [], []
        for (i, j) in [(0, 1), (0, 2), (1, 2)]:
            cls, anc = R4.edge_class(tuple(vts[i]), tuple(vts[j]))
            v = np.array(R4.DIRS15[cls])
            qvals.append(float(v @ v))
            einfo.append((cls, anc, float(np.sqrt(float(v @ v)))))
        aout = R4.AREA(*qvals)
        at = [(cls, np.array(anc, float), 2 * ell * float(aout[1 + n]))
              for n, (cls, anc, ell) in enumerate(einfo)]
        dt = []
        for vs in R4.STARS[tri]:
            loc = {v: i for i, v in enumerate(vs)}
            hinge_local = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
            miss = tuple(sorted([i for i in range(5) if i not in hinge_local]))
            qv, edata = [], []
            for (i, j) in R4.PAIRS5:
                cls, anc = R4.edge_class(vs[i], vs[j])
                v = np.array(R4.DIRS15[cls])
                qv.append(float(v @ v))
                edata.append((cls, anc, float(np.sqrt(float(v @ v)))))
            out = R4.THETA[miss](*qv)
            dt += [(cls, np.array(anc, float), -2 * ell * float(out[1 + n]))
                   for n, (cls, anc, ell) in enumerate(edata)]
        for src, dst in ((at, a_terms), (dt, d_terms)):
            dst.append((np.array([t[0] for t in src], int),
                        np.array([t[1] for t in src], float),
                        np.array([t[2] for t in src], float)))
    return a_terms, d_terms


A_TERMS, D_TERMS = precompute_terms()


def _row(term, k):
    cls, anc, coef = term
    r = np.zeros(15, complex)
    np.add.at(r, cls, coef * np.exp(1j * (anc @ k)))
    return r


def Qan(k):
    """Holomorphic continuation of the landed bloch_Q: conj(x(k)) -> x(-k). Valid for complex k."""
    k = np.asarray(k, complex)
    Q = np.zeros((15, 15), complex)
    for t in range(NTRI):
        ap, am = _row(A_TERMS[t], k), _row(A_TERMS[t], -k)
        dp, dm = _row(D_TERMS[t], k), _row(D_TERMS[t], -k)
        Q += 0.5 * (np.outer(am, dp) + np.outer(dm, ap))
    return Q


def _entire_sinc_phase(z):
    z = complex(z)
    return 1.0 + 0j if abs(z) < 1e-13 else (np.exp(2j * z) - 1.0) / (2j * z)


def Man(k):
    """Holomorphic continuation of the landed metric_map (midpoint phase x sinc)."""
    k = np.asarray(k, complex)
    Mm = np.zeros((15, 10), complex)
    for ci, v in enumerate(R4.DIRS15):
        vv = np.array(v, float)
        ell = float(np.linalg.norm(vv))
        ph = _entire_sinc_phase((k @ vv) / 2.0)
        for hj, (a, b) in enumerate(R4.HCOMPS):
            Hm = np.zeros((4, 4))
            Hm[a, b] += 1.0
            if a != b:
                Hm[b, a] += 1.0
            Mm[ci, hj] = ph * (vv @ Hm @ vv) / (2 * ell)
    return Mm


def Qh(k):
    return Man(-np.asarray(k, complex)).T @ Qan(k) @ Man(k)


def kvec(kspat, omega):
    return np.array([kspat[0], kspat[1], kspat[2], 1j * omega], complex)


def svals(kspat, omega):
    s = np.linalg.svd(Qan(kvec(kspat, omega)), compute_uv=False)
    return np.sort(s) / s.max()


def sig6(kspat, omega):
    return svals(kspat, omega)[5]


def refine(kspat, lo, hi, f=sig6):
    """Golden-section minimisation of sigma_6 in omega; deterministic, no seeds."""
    gr = (np.sqrt(5.0) - 1.0) / 2.0
    a, b = lo, hi
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc, fd = f(kspat, c), f(kspat, d)
    for _ in range(200):
        if fc < fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = f(kspat, c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = f(kspat, d)
        if b - a < 1e-14:
            break
    om = 0.5 * (a + b)
    return om, f(kspat, om)


def on_shell(kspat):
    km = float(np.linalg.norm(kspat))
    return refine(kspat, 0.35 * km, 1.05 * km + 1e-3)[0]


def gauge_h(k):
    """The continuum gauge family h_munu = i(k_mu xi_nu + k_nu xi_mu) in metric components."""
    Gh = np.zeros((10, 4), complex)
    for j in range(4):
        for i, (a, b) in enumerate(R4.HCOMPS):
            Gh[i, j] = (1j * k[a] if b == j else 0.0) + (1j * k[b] if a == j else 0.0)
    return Gh


def kerdim(A, tol=1e-8):
    s = np.linalg.svd(A, compute_uv=False)
    return int((s / s.max() < tol).sum())


def main() -> int:
    print("T(Z^3 x Z_tau), Euclidean/OS0: delta^2 S_Regge, propagating modes and dispersion")
    print(f"  complex imported from the landed 3+1 runner: {len(R4.cell_simplices(np.zeros(4, int)))}"
          f" 4-simplices, {len(R4.DIRS15)} edge classes, {NTRI} hinge classes per 4-cell;"
          f" 15x15 Hessian per momentum")

    # ---------------------------------------------------------------- T0
    dq = float(np.abs(Qan(K_PIN) - R4.bloch_Q(K_PIN)).max())
    dm = float(np.abs(Man(K_PIN) - R4.metric_map(K_PIN)).max())
    check("T0 continuation provenance: the holomorphic continuation reproduces the landed Bloch "
          "Hessian and metric map at real momentum",
          dq < 1e-12 and dm < 1e-12 and len(R4.DIRS15) == 15 and NTRI == 50,
          f"max|Qan-bloch_Q| = {dq:.1e}; max|Man-metric_map| = {dm:.1e} at the declared k; "
          f"the gauge map is entire as landed and reused verbatim")

    # ---------------------------------------------------------------- T1
    for tag, mod, lbl in (("T1a", R3, "3D"), ("T1b", R4, "3+1")):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            mod.main()
        txt = buf.getvalue()
        m = re.search(r"TOTAL: PASS=(\d+) FAIL=(\d+)", txt)
        npass, nfail = (int(m.group(1)), int(m.group(2))) if m else (-1, -1)
        if tag == "T1a":
            sp = re.search(r"spread/mean = ([0-9.eE+-]+)", txt)
            tt = re.search(r"TT\(yz\)=([-+0-9.]+) = TT\(E\)=([-+0-9.]+); "
                           r"transverse-trace=([-+0-9.]+)", txt)
            spread = float(sp.group(1)) if sp else float("nan")
            tt1, tt2, trt = (float(tt.group(1)), float(tt.group(2)), float(tt.group(3))) \
                if tt else (float("nan"),) * 3
            check("T1a landed 3D row reproduces: the retained spatial comparator is unchanged",
                  npass == 10 and nfail == 0 and spread < 1e-7
                  and abs(tt1 + 0.25) < 1e-6 and abs(tt2 + 0.25) < 1e-6 and abs(trt - 0.25) < 1e-6,
                  f"PASS={npass} FAIL={nfail}; c = -1/2, spread/mean {spread:.2e}; "
                  f"TT {tt1:+.4f} = {tt2:+.4f}; transverse-trace {trt:+.4f}")
        else:
            check("T1b landed 3+1 row reproduces: the 4D complex and Hessian imported here are the "
                  "landed ones, re-executed clean",
                  npass == 10 and nfail == 0, f"PASS={npass} FAIL={nfail}")

    # ---------------------------------------------------------------- T2
    print("  kernel census, declared real Euclidean 4-momenta:")
    ok2, rows = True, []
    for k in K_KERNEL:
        Q = Qan(k)
        d15, d10 = kerdim(Q), kerdim(Qh(k))
        r = float(np.abs(Q @ R4.gauge_map(k)).max())
        ok2 &= (d15 == 5 and d10 == 4 and r < 1e-12)
        rows.append((k, d15, d10, r))
        print(f"    k={np.array2string(k, precision=3, floatmode='fixed', separator=','):<30s}"
              f" ker Q = {d15}  ker Q_h = {d10}  max|Q Gamma| = {r:.1e}")
    check("T2a kernel census: dim ker Q(k) = 5 at every declared momentum -- 4 discrete "
          "diffeomorphisms plus 1 identically flat non-metric branch that never goes on shell; "
          "the metric-sector kernel is exactly 4",
          ok2, f"ker Q = {sorted(set(r[1] for r in rows))}, ker Q_h = "
               f"{sorted(set(r[2] for r in rows))}, worst max|Q Gamma| = {max(r[3] for r in rows):.1e}")
    worst_gh = 0.0
    for k in K_KERNEL:
        Qm = Qh(k)
        worst_gh = max(worst_gh, float(np.abs(Qm @ gauge_h(k)).max() / np.abs(Qm).max()))
    check("T2b continuum gauge family: the metric-sector kernel coincides exactly with "
          "h_munu = i(k_mu xi_nu + k_nu xi_mu) -- the discrete diffeomorphism orbit is the "
          "continuum one here, not an approximation to it",
          worst_gh < 1e-12, f"worst max|Q_h Gamma_h|/|Q_h| = {worst_gh:.1e} over 4 momenta")

    # ---------------------------------------------------------------- T3
    print("  branch hunt, omega in (0,8], 900-point scan then refinement:")
    branches, nulls = {}, set()
    for nm, kh in (("axis", AXIS), ("body", BODY)):
        for km in K_BRANCH:
            ks = km * kh
            ws = np.linspace(1e-5, 8.0, 900)
            ys = np.array([sig6(ks, w) for w in ws])
            roots = []
            for i in range(1, len(ws) - 1):
                if ys[i] < ys[i - 1] and ys[i] <= ys[i + 1]:
                    om, y = refine(ks, ws[i - 1], ws[i + 1])
                    if y < 1e-11:
                        s = svals(ks, om)
                        roots.append((om, y, float(s[6]), float(s[7]), int((s < 1e-9).sum())))
            branches[(nm, km)] = roots
            for r in roots:
                nulls.add(r[4])
            head = roots[0] if roots else None
            print(f"    {nm:4s} |k|={km:7.5f} br={len(roots)}" + (
                f" om*={head[0]:.8f} s6={head[1]:.1e} s7={head[2]:.1e} s8={head[3]:.1e} "
                f"n={head[4]}" if head else ""))
    check("T3 propagating-mode count: exactly one on-shell frequency per declared spatial "
          "momentum, doubly degenerate -- sigma_6 and sigma_7 at machine zero against a sigma_8 "
          "fourteen orders larger; no doubler and no spurious propagating branch in omega in (0,8]",
          all(len(v) == 1 for v in branches.values()) and nulls == {7},
          f"branches/momentum {sorted(set(len(v) for v in branches.values()))}; on-shell nulls "
          f"{sorted(nulls)} = 5 kinematic + 2 physical, over {len(branches)} declared momenta")

    # ---------------------------------------------------------------- T4a
    worst, npts, per = 0.0, 0, {}
    for nm, kh in ZDIR.items():
        for km in K_ZONE:
            ks = km * kh
            if float(np.max(np.abs(ks))) > np.pi + 1e-9:
                continue
            om = on_shell(ks)
            lhs = 4 * np.sinh(om / 2) ** 2
            rhs = float(sum(4 * np.sin(x / 2) ** 2 for x in ks))
            rel = abs(lhs - rhs) / max(abs(rhs), 1e-30)
            worst = max(worst, rel)
            per[nm] = max(per.get(nm, 0.0), rel)
            npts += 1
    print("  4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2), worst relative residual per direction:")
    print("    " + "  ".join(f"{nm} {v:.1e}" for nm, v in per.items()))
    check("T4a exact all-zone dispersion: the on-shell locus is exactly the zero set of the "
          "standard hypercubic lattice d'Alembertian k-hat^2 continued to k_tau = i omega, "
          "4 sinh^2(omega/2) = sum_i 4 sin^2(k_i/2), across the whole zone",
          worst < 1e-11 and npts == 32,
          f"worst relative residual {worst:.3e} over {npts} declared zone points in "
          f"{len(ZDIR)} directions (root-finder limited; ~1e-15 typical)")

    # ---------------------------------------------------------------- T4b
    print("  (omega^2-k^2)/k^4 at |k|=0.01, computed/exact rational:")
    ok4b, cells = True, []
    for nm, kh in NDIR.items():
        vals = [((on_shell(km * kh)) ** 2 - km ** 2) / km ** 4 for km in K_SMALL]
        s4 = float(np.sum(kh ** 4))
        pred = -(1.0 + s4) / 12.0
        ok4b &= abs(vals[-1] - pred) < 5e-4
        cells.append(f"{nm} {vals[-1]:+.6f}/{pred:+.6f}")
    print("    " + "  ".join(cells))
    kax = 0.01
    om_ax = on_shell(kax * AXIS)
    check("T4b small-k expansion, derived not fitted: omega^2 = k^2 - (k^4/12)(1 + sum_i n_i^4) "
          "+ O(k^6) -- massless, light speed exactly 1 in tick units, the anisotropy the cubic "
          "invariant alone: -1/6 axis, -1/8 face, -1/9 body, -7/50 for (2,1,0)",
          ok4b and abs(om_ax / kax - 1.0) < 1e-4,
          f"pairs above; omega/|k| = {om_ax / kax:.9f} at |k| = {kax}")

    # ---------------------------------------------------------------- T4c
    print("  isotropy: spread of omega* over axis/face/body:")
    iso = []
    for km in K_ISO:
        a, f_, b = (on_shell(km * AXIS), on_shell(km * FACE), on_shell(km * BODY))
        rel = (max(a, f_, b) - min(a, f_, b)) / float(np.mean([a, f_, b]))
        iso.append((km, rel))
        print(f"    |k|={km:5.2f} axis {a:.9f} face {f_:.9f} body {b:.9f} "
              f"spread/k^2 {rel / km ** 2:.4f}")
    base = iso[0][1] / iso[0][0] ** 2
    check("T4c isotropy at quadratic order: the relative direction spread of omega scales as "
          "k^2, so omega is isotropic at O(k^2) and anisotropic only at O(k^4) -- the "
          "lattice-artefact order the landed rows leave uncharacterised",
          all(abs(r / km ** 2 - base) < 0.06 * base for km, r in iso if km <= 0.2),
          f"spread/k^2 constant at {base:.4f} => the anisotropy first enters omega^2 at O(k^4)")

    # ---------------------------------------------------------------- T4d
    ks = 0.2 * AXIS
    out = []
    for lbl, om in (("static", 0.0), ("on-shell", on_shell(ks))):
        Qm = Qh(kvec(ks, om))
        Qm = (Qm + Qm.conj().T) / 2

        def hq(d):
            v = np.zeros(10)
            nrm = 0.0
            for (a, b), val in d.items():
                v[HIDX[(min(a, b), max(a, b))]] = val
                nrm += val ** 2 * (2 if a != b else 1)
            return float(np.real(v @ Qm @ v)) / nrm
        out.append((lbl, hq({(1, 2): 1.0}), hq({(1, 1): 1.0, (2, 2): -1.0}),
                    hq({(1, 1): 1.0, (2, 2): 1.0}), hq({(3, 3): 1.0}), hq({(0, 3): 1.0})))
    for lbl, t1, t2, tr, la, sh in out:
        print(f"    k=(0.2,0,0) {lbl:8s} TT(yz) {t1:+.8f} TT(yy-zz) {t2:+.8f} "
              f"tr-trace {tr:+.8f} lapse {la:+.1e} shift {sh:+.1e}")
    check("T4d multiplier structure on shell: the lapse h_tautau and shift h_i,tau kinetic "
          "weights vanish on shell as well as statically -- the constraint multipliers carry no "
          "propagating weight",
          max(abs(r[4]) for r in out) < 1e-12 and max(abs(r[5]) for r in out) < 1e-12,
          f"lapse {out[1][4]:.1e}, shift {out[1][5]:.1e} on shell, raw S_R orientation; the "
          f"static row is the landed comparator pair, ratio -1")

    # ---------------------------------------------------------------- T5
    print("  TT fraction of the two propagating modes after gauge removal:")
    frac_lo, frac_hi = [], []
    for km in K_POL:
        ksp = km * AXIS
        k = kvec(ksp, on_shell(ksp))
        Q = Qan(k)
        _, s, Vh = np.linalg.svd(Q)
        Z = Vh.conj().T[:, s / s.max() < 1e-8]
        Gq, _ = np.linalg.qr(R4.gauge_map(k))
        Zr = Z - Gq @ (Gq.conj().T @ Z)
        Uz, sz, _ = np.linalg.svd(Zr)
        Bq, _ = np.linalg.qr(Uz[:, :len(sz)][:, sz > 1e-8])
        M = Man(k)
        Mq, _ = np.linalg.qr(M)
        _, _, Vc = np.linalg.svd(Mq.conj().T @ Bq)
        inB = Bq @ Vc.conj().T[:, :2]
        Gh = gauge_h(k)
        tt = np.zeros((10, 2), complex)
        tt[HIDX[(1, 2)], 0] = 1.0
        tt[HIDX[(1, 1)], 1] = 1.0
        tt[HIDX[(2, 2)], 1] = -1.0
        basis = np.hstack([tt, Gh])
        fr = []
        for j in range(2):
            h, *_ = np.linalg.lstsq(M, inB[:, j], rcond=None)
            c, *_ = np.linalg.lstsq(basis, h, rcond=None)
            hg = h - Gh @ c[2:]
            yy, zz, yz = hg[HIDX[(1, 1)]], hg[HIDX[(2, 2)]], hg[HIDX[(1, 2)]]
            num = 2 * abs((yy - zz) / 2) ** 2 + 2 * abs(yz) ** 2
            den = sum(abs(hg[i]) ** 2 * (2 if a != b else 1) for i, (a, b) in enumerate(R4.HCOMPS))
            fr.append(num / den)
        fr = sorted(fr)
        frac_lo.append(fr[0])
        frac_hi.append(fr[1])
        print(f"    |k|={km:5.2f} TT fraction {fr[1]:.8f}, {fr[0]:.8f}")
    dev = [(km, on_shell(km * AXIS) - km) for km in K_CMP]
    print("  omega* - k on axis: " + ", ".join(f"|k|={km:.1f} {d:+.2f}" for km, d in dev))
    check("T5 TT up to gauge is a small-k statement, and the target-operator row's omega = +-k "
          "across the zone is not reproduced here: both polarisations are transverse-traceless up "
          "to gauge as k -> 0 and deform at the corner, where omega* falls below k by O(1)",
          min(frac_lo[0], frac_hi[0]) > 0.999999 and frac_lo[-1] < 0.95
          and abs(dev[-2][1] + 0.47) < 0.05 and abs(dev[-1][1] + 1.24) < 0.05,
          f"TT fraction {frac_lo[0]:.8f} at |k|={K_POL[0]}, {frac_lo[2]:.3f} at {K_POL[2]}, "
          f"{frac_hi[-1]:.2f}/{frac_lo[-1]:.2f} at the corner; omega*-k = {dev[-2][1]:+.2f} at "
          f"|k|=2 and {dev[-1][1]:+.2f} at 3 -- the same polynomial read in Lorentzian signature "
          f"gives omega = +-k, and only on axis")

    print()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED, not derived: the edge lengths, the action selection and its orientation, the")
    print("Lorentzian signature, the nonlinear completion, the record-to-geometry link.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
