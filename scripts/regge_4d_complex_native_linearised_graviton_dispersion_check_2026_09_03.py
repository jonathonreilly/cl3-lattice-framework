"""Finite supplied Regge diagnostics for #7910.

The current own note defines the precise finite/conditional scope. Original numerical
fixtures and check IDs are retained; historical source and labels are archived.
No physical Record-to-geometry, full spectral or OS reconstruction result is implied.
R3/R4 are unchanged geometry implementations, not imported audit/status authority.
"""
from __future__ import annotations

AUDIT_TIMEOUT_SEC = 150

INPUT_SHA256 = {'docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'aad9fa7b70fe00a18ea627248270c4d47250ff214e98d2ae2466760ad2084bf8', 'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md': '5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b', 'scripts/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.py': 'e30746e2ce2be1104ad6074c6854278227f98c18ccd6a4b9dccce06d220e71c7', 'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py': '537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce'}
AUDIT_INPUT_PATHS = ('docs/THE_REGGE_SECOND_VARIATION_ON_THE_4D_CUBIC_COXETER_COMPLEX_CARRIES_A_NATIVE_LINEARISED_GRAVITON_BOUNDED_THEOREM_NOTE_2026-09-03.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'scripts/frontier_cubic_coxeter_regge_second_variation_3d_2026_06_09.py', 'scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py')


def require_inputs(root=None):
    from pathlib import Path
    import hashlib
    root = Path(root) if root is not None else Path(__file__).resolve().parents[1]
    for relative, expected in INPUT_SHA256.items():
        path = root / relative
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise RuntimeError("missing or changed declared input: " + relative)


require_inputs()

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



def correction_controls():
    """A finite principal-angle witness distinguishing exact from approximate membership."""
    ks = np.array([0.8, 0.0, 0.0])
    omega = 2 * np.arcsinh(np.sqrt(np.sum(4 * np.sin(ks / 2) ** 2)) / 2)
    k = np.r_[ks, 1j * omega]
    Q = Qan(k)
    _, s, vh = np.linalg.svd(Q)
    Z = vh.conj().T[:, s / s.max() < 1e-10]
    Mq, _ = np.linalg.qr(Man(k))
    cosines = np.linalg.svd(Mq.conj().T @ Z, compute_uv=False)
    metric_nullity = kerdim(Qh(k), 1e-10)
    ok = (Z.shape[1] == 7 and cosines.shape == (7,)
          and np.all(np.isfinite(cosines)) and np.max(np.abs(cosines[:4] - 1)) < 1e-10
          and 1e-5 < 1 - cosines[4] < 1e-3 and 1e-5 < 1 - cosines[5] < 1e-3
          and cosines[6] < 0.6 and metric_nullity == 4)
    check("C1 actual metric-intersection witness: only four precision-level intersections; two extra directions approximate", ok,
          f"principal cosines {cosines.tolist()}; Q_h numerical nullity {metric_nullity}")
    return ok


def main() -> int:
    print("T(Z^3 x Z_tau), supplied Euclidean Regge Hessian: finite continued spectra")
    print(f"  complex imported from the landed 3+1 runner: {len(R4.cell_simplices(np.zeros(4, int)))}"
          f" 4-simplices, {len(R4.DIRS15)} edge classes, {NTRI} hinge classes per 4-cell;"
          f" 15x15 Hessian per momentum")

    # ---------------------------------------------------------------- T0
    dq = float(np.abs(Qan(K_PIN) - R4.bloch_Q(K_PIN)).max())
    dm = float(np.abs(Man(K_PIN) - R4.metric_map(K_PIN)).max())
    check('T0 finite provenance: continued Q and line map agree with actual R4 at the declared real momentum',
          dq < 1e-12 and dm < 1e-12 and len(R4.DIRS15) == 15 and NTRI == 50,
          f"max|Qan-bloch_Q| = {dq:.1e}; max|Man-metric_map| = {dm:.1e} at the declared k; "
          f"the gauge map is entire as landed and reused verbatim")

    # ---------------------------------------------------------------- T1
    for tag, mod, lbl in (("T1a", R3, "3D"), ("T1b", R4, "3+1")):
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            helper_return = mod.main()
        txt = buf.getvalue()
        print(f"  BEGIN unchanged {lbl} finite helper output (historical labels are not adopted)")
        print(txt, end="")
        print(f"  END unchanged {lbl} finite helper output")
        m = re.search(r"TOTAL: PASS=(\d+) FAIL=(\d+)", txt)
        npass, nfail = (int(m.group(1)), int(m.group(2))) if m else (-1, -1)
        if tag == "T1a":
            sp = re.search(r"spread/mean = ([0-9.eE+-]+)", txt)
            tt = re.search(r"TT\(yz\)=([-+0-9.]+) = TT\(E\)=([-+0-9.]+); "
                           r"transverse-trace=([-+0-9.]+)", txt)
            spread = float(sp.group(1)) if sp else float("nan")
            tt1, tt2, trt = (float(tt.group(1)), float(tt.group(2)), float(tt.group(3))) \
                if tt else (float("nan"),) * 3
            check('T1a finite R3 reproduction: ten original predicates and selected printed comparator values; no parent status or global proof imported',
                  npass == 10 and nfail == 0 and helper_return == 0 and mod.FAIL == 0 and spread < 1e-7
                  and abs(tt1 + 0.25) < 1e-6 and abs(tt2 + 0.25) < 1e-6 and abs(trt - 0.25) < 1e-6,
                  f"PASS={npass} FAIL={nfail}; c = -1/2, spread/mean {spread:.2e}; "
                  f"TT {tt1:+.4f} = {tt2:+.4f}; transverse-trace {trt:+.4f}")
        else:
            check('T1b finite R4 reproduction: ten original predicates and real return status; no parent physical or all-momentum claim imported',
                  npass == 10 and nfail == 0 and helper_return == 0 and mod.FAIL == 0, f"PASS={npass} FAIL={nfail}")

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
    check('T2a numerical nullities five/four and gauge residuals at the four declared nonzero real momenta',
          ok2, f"ker Q = {sorted(set(r[1] for r in rows))}, ker Q_h = "
               f"{sorted(set(r[2] for r in rows))}, worst max|Q Gamma| = {max(r[3] for r in rows):.1e}")
    worst_gh = 0.0
    for k in K_KERNEL:
        Qm = Qh(k)
        worst_gh = max(worst_gh, float(np.abs(Qm @ gauge_h(k)).max() / np.abs(Qm).max()))
    check('T2b line-map continuum gauge identity, with residuals checked at four declared momenta',
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
    check('T3 finite 900-point interior-minimum search: one detected frequency and numerical nullity seven per declared momentum; completeness unresolved',
          all(len(v) == 1 for v in branches.values()) and nulls == {7},
          f"branches/momentum {sorted(set(len(v) for v in branches.values()))}; on-shell nulls "
          f"{sorted(nulls)} = five background numerical zeros plus two additional small singular values, over {len(branches)} declared momenta")

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
    check('T4a proposed lattice dispersion matches 32 declared zone points; no all-zone zero-set certificate',
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
    check('T4b conditional Taylor formula for the proposed scalar dispersion, compared at three small magnitudes; no physical light-speed derivation',
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
    check('T4c five finite direction-spread diagnostics consistent with the conditional Taylor formula',
          all(abs(r / km ** 2 - base) < 0.06 * base for km, r in iso if km <= 0.2),
          f"finite spread/k^2 reference {base:.4f}; asymptotic conclusion is conditional on the scalar formula")

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
    check('T4d selected lapse and one shift diagonal forms near zero at one axis momentum; no full multiplier analysis',
          max(abs(r[4]) for r in out) < 1e-12 and max(abs(r[5]) for r in out) < 1e-12,
          f"lapse {out[1][4]:.1e}, shift {out[1][5]:.1e} on shell, raw S_R orientation; the "
          f"static and continued selected forms are reported above; no complete constraint result")

    # ---------------------------------------------------------------- T5
    print("  TT fraction of two selected best metric projections after gauge subtraction:")
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
    check('T5 least-squares metric/gauge-projected TT fractions at five axis fixtures; no exact finite-k metric polarization or proved limit',
          min(frac_lo[0], frac_hi[0]) > 0.999999 and frac_lo[-1] < 0.95
          and abs(dev[-2][1] + 0.47) < 0.05 and abs(dev[-1][1] + 1.24) < 0.05,
          f"TT fraction {frac_lo[0]:.8f} at |k|={K_POL[0]}, {frac_lo[2]:.3f} at {K_POL[2]}, "
          f"{frac_hi[-1]:.2f}/{frac_lo[-1]:.2f} at the corner; omega*-k = {dev[-2][1]:+.2f} at "
          f"|k|=2 and {dev[-1][1]:+.2f} at 3; no Lorentzian target-operator identity is inferred")

    print()
    correction_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("SUPPLIED, not derived: the edge lengths, the action selection and its orientation, the")
    print("Lorentzian signature, the nonlinear completion, the record-to-geometry link.")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
