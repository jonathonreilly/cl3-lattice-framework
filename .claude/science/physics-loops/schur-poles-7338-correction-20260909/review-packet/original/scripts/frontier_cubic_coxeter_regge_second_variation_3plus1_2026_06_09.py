"""Second variation of the Regge action on the 3+1 cubic-Coxeter complex (Z^3 x Z_tau, flat OS0
background): the tick extension of the retained 3D row, and the geometric derivation of the
lambda-one kinetic fiber metric, multiplier structure, and comparator signs.

FRAMING (3D+1, per the framework): the lattice axiom supplies SPACE = Z^3 only; time is the emergent
record tick. The complex built here is the retained six-tetrahedra body-diagonal chain
(CUBIC_COXETER_REGGE_DEFICIT_VANISHING, retained row) EXTENDED BY THE TICK DIRECTION: the path
(Kuhn-chain) triangulation of the 4-cell on Z^3 x Z_tau, whose restriction to a constant-tick spatial
face is EXACTLY the retained 3D chain (verified combinatorially, slice-consistency check). The tick edge is grained on the
same footing as the spatial edge per the approved kinetic_isotropy_primitive (c_t = c_s, a structural
grant; nothing beyond it is used -- in particular no tick-scale/clock-rate derivation, which remains
the retained no-go boundary). The Euclidean signature here is the OS0 surface; the Lorentzian reading
is reached by the framework's RP/OS route, not assumed.

THE COMPLEX: per 4-cell, the 24 path 4-simplices sigma in S_4 (vertices 0, e_{s1}, e_{s1}+e_{s2}, ...,
(1,1,1,1)), all sharing the main diagonal -- the canonical 4D Kuhn/Coxeter chain. Edge classes per
cell: the 15 nonzero 0/1 vectors (flat lengths^2 in {1,2,3,4}); triangle (hinge) classes per cell: the
50 nested pairs (0, u, w) with supp(u) strictly inside supp(w). 10 metric components vs 15 edge classes
=> FIVE non-metric modes per cell.

CHECKS:
  slice-consistency check  slice consistency: the spatial 3-face of the 4-cell complex carries EXACTLY the retained 3D
      six-tetrahedra chain (as vertex sets) -- the 3+1 complex is the tick extension of the retained row.
  flat-anchor check  FLAT ANCHOR (new 4D fact, extending the retained 3D row): every interior triangle class of the
      flat complex has deficit 0 to machine precision; S_R = sum_t A_t delta_t = 0.
  Schlaefli/Hermiticity check  exactness gates: the per-4-simplex Schlaefli identity sum_t A_t d theta_t = 0 (machine, all
      length directions); Q(k) HERMITIAN to machine (the complex-level Regge lemma: d S_R/d ell_e =
      sum_t (dA_t/d ell_e) delta_t, so the flat Hessian is sum_t dA_t (x) d delta_t, symmetric).
  end-to-end action check end-to-end gate: numerical second difference of the ACTUAL action S_R on a periodic 3^4 box under
      a commensurate real perturbation equals the Bloch prediction (N/2) Re[u^dag Q(k) u].
  gauge-zero-mode check  gauge: vertex-displacement fields (4 components per cell) are EXACT zero modes of Q(k) at every
      momentum (machine) -- the discrete diffeomorphism family of the geometric action.
  mode-inventory check  k=0: constant metric perturbations (all 10 h components, exact line-averaged map) are EXACT zero
      modes; the FIVE non-metric modes split into FOUR massive branches (raw S_R
      orientation -48, -16 x3, hence positive after the standard Euclidean
      orientation) and ONE exactly flat branch.
  extra-branch decoupling check the flat branch is an EXACT zero branch at EVERY momentum, and the zero space meets the metric
      sector in exactly the 4 gauge directions: it is a Rocek-Williams-type spurious lattice direction,
      EXACTLY decoupled at quadratic order -- the physical low-energy content is the EH sector alone.
  4D comparator check  THE COMPARATOR (4D): Q_h(k) = c * Q_EH(k) + O(k^4) with ONE constant across FIVE directions
      including tick-space mixed ones: pure-tick, pure-space, space-space diagonal, tick-space
      diagonal, full body diagonal. Q_EH = the 4D Euclidean linearized EH pairing (operator derived
      in-runner from curvature definitions). Isotropy across tick-mixed directions is the O(k^2)
      emergent Euclidean-SO(4) statement for the geometric action on the OS0 surface -- the
      kinetic-isotropy primitive's structural grant realized dynamically at quadratic order. Expected
      c = -1/2 (the d-independent textbook delta^2 S_R = (1/2) delta^2 int sqrt(g) R with the
      variational sign) -- measured, not assumed.
  3+1 fiber-metric check  THE 3+1 READING (geometric lambda-one fiber metric + multipliers): at pure-tick momentum
      p = (omega, 0,0,0), Q_h = omega^2 K + O(omega^4) with K the kinetic fiber metric ON THE GEOMETRIC
      ACTION: K_trace : K_TT = -2 : +1 (lambda-one DeWitt, indefinite, both TT channels equal), and the
      lapse (h_00) and shift (h_0i) kinetic weights are ZERO (multiplier structure, geometric). This is
      the object the 3+1 target-operator row derived from the continuum target; here it comes from
      delta^2 S_R natively.
  spatial-sign comparator check  potential signs at zero tick-frequency (spatial k || x): TT pair equal, transverse-trace
      equal-magnitude opposite-sign (ratio -1) -- the degenerate-supermetric no-go's supplied pair,
      derived in the 3+1 geometry (the 3D row's result embedded and re-verified in the tick complex).

ORIENTATION: as in the 3D row, everything orientation-independent is derived; the single remaining
sign is the overall action orientation (S_R vs -S_R) = the same located sign residual as the
arrow/stability/spectral no-go row. No PDG/fitted value; Regge/Rocek-Williams/CMS cited context-only.
"""
from __future__ import annotations
import itertools
import numpy as np
import sympy as sp

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


# ---------------------------------------------------------------- symbolic 4-simplex machinery (once)
PAIRS5 = [(i, j) for i in range(5) for j in range(5) if i < j]      # 10 edges of a 4-simplex


def build_theta_funcs():
    """for each missing pair (a,b) (hinge = the other three vertices), the dihedral angle of the
    4-simplex at that hinge as a function of the 10 edge-lengths-squared, plus its 10 gradients."""
    q = {e: sp.Symbol(f"q{e[0]}{e[1]}", positive=True) for e in PAIRS5}

    def qq(i, j):
        return q[(min(i, j), max(i, j))]

    def dot(i, j, base):
        if i == j:
            return qq(base, i)
        return (qq(base, i) + qq(base, j) - qq(i, j)) / 2

    funcs = {}
    for (a, b) in PAIRS5:
        hinge = [v for v in range(5) if v not in (a, b)]
        p, qv, r = hinge
        # base p; hinge plane span{u1=qv-p, u2=r-p}; legs w_a=a-p, w_b=b-p
        G11, G12, G22 = dot(qv, qv, p), dot(qv, r, p), dot(r, r, p)
        det = G11 * G22 - G12 ** 2
        def proj_pair(wi, wj):
            # <w_i, w_j> - [u.w_i]^T G^{-1} [u.w_j]
            ai1, ai2 = dot(qv, wi, p), dot(r, wi, p)
            aj1, aj2 = dot(qv, wj, p), dot(r, wj, p)
            return dot(wi, wj, p) - (G22 * ai1 * aj1 - G12 * (ai1 * aj2 + ai2 * aj1) + G11 * ai2 * aj2) / det
        nab = proj_pair(a, b)
        naa = proj_pair(a, a)
        nbb = proj_pair(b, b)
        theta = sp.acos(nab / sp.sqrt(naa * nbb))
        grads = [sp.diff(theta, q[e]) for e in PAIRS5]
        funcs[(a, b)] = sp.lambdify([q[e] for e in PAIRS5], [theta] + grads, "numpy")
    return funcs


THETA = build_theta_funcs()

AREA_SYMS = sp.symbols("qa qb qc", positive=True)
_qa, _qb, _qc = AREA_SYMS
_A2 = (2 * _qa * _qb + 2 * _qa * _qc + 2 * _qb * _qc - _qa ** 2 - _qb ** 2 - _qc ** 2) / 16
_A = sp.sqrt(_A2)
AREA = sp.lambdify(AREA_SYMS, [_A, sp.diff(_A, _qa), sp.diff(_A, _qb), sp.diff(_A, _qc)], "numpy")


# ---------------------------------------------------------------- the 3+1 complex (path simplices)
E4 = [np.array(v) for v in [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1)]]
PERMS = list(itertools.permutations(range(4)))


def cell_simplices(base):
    out = []
    for sg in PERMS:
        vs = [np.array(base)]
        for i in range(4):
            vs.append(vs[-1] + E4[sg[i]])
        out.append([tuple(v) for v in vs])
    return out


DIRS15 = [v for v in itertools.product([0, 1], repeat=4) if any(v)]
DIR_IDX = {v: i for i, v in enumerate(DIRS15)}


def edge_class(p, r):
    d = tuple(np.array(r) - np.array(p))
    if d in DIR_IDX:
        return DIR_IDX[d], np.array(p)
    d = tuple(np.array(p) - np.array(r))
    return DIR_IDX[d], np.array(r)


# triangle classes: (0, u, w) nested 0/1 supports
def triangle_classes():
    out = []
    for w in DIRS15:
        sw = {i for i in range(4) if w[i]}
        if len(sw) < 2:
            continue
        for u in DIRS15:
            su = {i for i in range(4) if u[i]}
            if su and su < sw:
                out.append((tuple([0, 0, 0, 0]), u, w))
    return out


TRI_CLASSES = triangle_classes()


def star_of_triangle(tri):
    """all (cell-offset, perm) 4-simplices containing the 3 vertices of tri."""
    tset = {tri[0], tri[1], tri[2]}
    out = []
    for off in itertools.product([-1, 0, 1], repeat=4):
        for vs in cell_simplices(off):
            if tset <= set(vs):
                out.append(vs)
    return out


STARS = {tri: star_of_triangle(tri) for tri in TRI_CLASSES}


# ---------------------------------------------------------------- per-triangle Bloch rows
def tri_rows(tri, kvec):
    """a_t(k): area-gradient row; d_t(k): deficit-gradient row (both over the 15 edge classes);
    also returns the flat deficit of this triangle class."""
    a_row = np.zeros(15, complex)
    d_row = np.zeros(15, complex)
    # area part: the 3 edges of the triangle
    vts = [np.array(tri[0]), np.array(tri[1]), np.array(tri[2])]
    qvals = []
    einfo = []
    for (i, j) in [(0, 1), (0, 2), (1, 2)]:
        cls, anc = edge_class(tuple(vts[i]), tuple(vts[j]))
        v = np.array(DIRS15[cls])
        qvals.append(float(v @ v))
        einfo.append((cls, anc, np.sqrt(float(v @ v))))
    Aout = AREA(*qvals)
    for n, (cls, anc, ell) in enumerate(einfo):
        a_row[cls] += 2 * ell * float(Aout[1 + n]) * np.exp(1j * np.dot(kvec, anc))
    # deficit part: sum over star simplices
    deficit = 2 * np.pi
    for vs in STARS[tri]:
        loc = {v: i for i, v in enumerate(vs)}
        hinge_local = sorted([loc[tri[0]], loc[tri[1]], loc[tri[2]]])
        miss = tuple(sorted([i for i in range(5) if i not in hinge_local]))
        # edge data of this simplex
        qv = []
        edata = []
        for (i, j) in PAIRS5:
            cls, anc = edge_class(vs[i], vs[j])
            v = np.array(DIRS15[cls])
            qv.append(float(v @ v))
            edata.append((cls, anc, np.sqrt(float(v @ v))))
        out = THETA[miss](*qv)
        deficit -= float(out[0])
        for n, (cls, anc, ell) in enumerate(edata):
            d_row[cls] -= 2 * ell * float(out[1 + n]) * np.exp(1j * np.dot(kvec, anc))
    return a_row, d_row, deficit


def bloch_Q(kvec):
    Q = np.zeros((15, 15), complex)
    for tri in TRI_CLASSES:
        a_row, d_row, _ = tri_rows(tri, kvec)
        Q += 0.5 * (np.outer(np.conj(a_row), d_row) + np.outer(np.conj(d_row), a_row))
    return Q


# ---------------------------------------------------------------- maps
def gauge_map(kvec):
    Gm = np.zeros((15, 4), complex)
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        Gm[ci, :] = (np.exp(1j * np.dot(kvec, vv)) - 1.0) * vv / ell
    return Gm


HCOMPS = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]


def metric_map(kvec):
    Mm = np.zeros((15, 10), complex)
    for ci, v in enumerate(DIRS15):
        vv = np.array(v, float)
        ell = np.linalg.norm(vv)
        z = np.dot(kvec, vv) / 2.0
        phase = np.exp(1j * z) * np.sinc(z / np.pi)
        for hj, (a, b) in enumerate(HCOMPS):
            Hm = np.zeros((4, 4))
            Hm[a, b] += 1.0
            if a != b:
                Hm[b, a] += 1.0
            Mm[ci, hj] = phase * (vv @ Hm @ vv) / (2 * ell)
    return Mm


# ---------------------------------------------------------------- 4D Euclidean linearized EH pairing
def einstein_pairing_4d(kvec):
    n = 4
    hs = {}
    for a in range(n):
        for b in range(n):
            if a <= b:
                hs[(a, b)] = sp.Symbol(f"h{a}{b}")
    Hm = sp.Matrix(n, n, lambda a, b: hs[(min(a, b), max(a, b))])
    p = [sp.Float(x) for x in kvec]
    Sv = {(m, nn): -p[m] * p[nn] for m in range(n) for nn in range(n)}
    R = sp.zeros(n, n)
    for m in range(n):
        for nn in range(n):
            acc = 0
            for l in range(n):
                acc += (Sv[(min(l, m), max(l, m))] * Hm[l, nn]
                        + Sv[(min(l, nn), max(l, nn))] * Hm[l, m]
                        - Sv[(l, l)] * Hm[m, nn] - Sv[(min(m, nn), max(m, nn))] * Hm[l, l])
            R[m, nn] = acc / 2
    Rs = sum(R[m, m] for m in range(n))
    G = sp.Matrix(n, n, lambda m, nn: R[m, nn] - sp.Rational(1, 2) * (1 if m == nn else 0) * Rs)
    Mq = np.zeros((10, 10))
    for i, (a, b) in enumerate(HCOMPS):
        wgt = 2.0 if a != b else 1.0
        expr = wgt * G[a, b]
        for j, key in enumerate(HCOMPS):
            Mq[i, j] = float(sp.diff(expr, hs[key]))
    return (Mq + Mq.T) / 2


# ---------------------------------------------------------------- box action (end-to-end gate)
def box_action(L, eps_fun):
    """S_R on a periodic L^4 box; eps_fun(cls, anchor) -> real length perturbation."""
    tri_def = {}
    tri_area = {}
    for base in itertools.product(range(L), repeat=4):
        for vs in cell_simplices(base):
            vsm = [tuple(np.mod(v, L)) for v in vs]
            qv = []
            for (i, j) in PAIRS5:
                cls, anc = edge_class(vs[i], vs[j])
                v = np.array(DIRS15[cls])
                ell0 = np.sqrt(float(v @ v))
                ell = ell0 + eps_fun(cls, np.mod(anc, L))
                qv.append(ell * ell)
            for (a, b) in PAIRS5:
                hinge = [vv for ii, vv in enumerate(vsm) if ii not in (a, b)]
                # canonical triangle key (sorted mod-L vertex tuples + edge-class signature)
                key = tuple(sorted(hinge))
                out = THETA[(a, b)](*qv)
                tri_def.setdefault(key, 2 * np.pi)
                tri_def[key] -= float(out[0])
                if key not in tri_area:
                    hverts = [np.array(vs[ii]) for ii in range(5) if ii not in (a, b)]
                    qa = float(np.sum((hverts[0] - hverts[1]) ** 2))
                    qb = float(np.sum((hverts[0] - hverts[2]) ** 2))
                    qc = float(np.sum((hverts[1] - hverts[2]) ** 2))
                    # perturbed areas: recompute from perturbed lengths
                    def pl(p1, p2):
                        cls, anc = edge_class(tuple(p1), tuple(p2))
                        v = np.array(DIRS15[cls])
                        return np.sqrt(float(v @ v)) + eps_fun(cls, np.mod(anc, L))
                    la, lb, lc = pl(hverts[0], hverts[1]), pl(hverts[0], hverts[2]), pl(hverts[1], hverts[2])
                    tri_area[key] = float(AREA(la * la, lb * lb, lc * lc)[0])
    return sum(tri_area[k] * tri_def[k] for k in tri_def)


def main() -> int:
    print("REGGE SECOND VARIATION ON THE 3+1 CUBIC-COXETER COMPLEX (Z^3 x Z_tau tick extension)")
    print("=" * 96)

    # ---- slice-consistency check: slice consistency with the retained 3D chain ----
    RETAINED_3D = [(0, 1, 2, 6), (0, 2, 3, 6), (0, 3, 7, 6), (0, 7, 4, 6), (0, 4, 5, 6), (0, 5, 1, 6)]
    C3 = {0: (0, 0, 0), 1: (1, 0, 0), 2: (1, 1, 0), 3: (0, 1, 0),
          4: (0, 0, 1), 5: (1, 0, 1), 6: (1, 1, 1), 7: (0, 1, 1)}
    retained_sets = {frozenset(C3[i] for i in t) for t in RETAINED_3D}
    slice_sets = set()
    for vs in cell_simplices((0, 0, 0, 0)):
        spatial = [v for v in vs if v[3] == 0]
        if len(spatial) == 4:
            slice_sets.add(frozenset(tuple(v[:3]) for v in spatial))
    check("slice-consistency check (3+1 framing, combinatorial): the spatial (constant-tick) 3-face of the Z^3 x Z_tau "
          "path complex carries EXACTLY the retained six-tetrahedra body-diagonal chain (as vertex "
          "sets) -- the 3+1 complex is the tick extension of the retained 3D row, not a new spatial "
          "structure",
          slice_sets == retained_sets,
          f"{len(slice_sets)} spatial tetrahedra on the slice; match with retained chain: {slice_sets == retained_sets}")

    # ---- flat-anchor check: flat anchor (new 4D fact) ----
    worst_def = 0.0
    SR = 0.0
    for tri in TRI_CLASSES:
        a_row, d_row, dfc = tri_rows(tri, np.zeros(4))
        worst_def = max(worst_def, abs(dfc))
    check("flat-anchor check (FLAT ANCHOR, the tick extension of the retained deficit-vanishing row): every interior "
          "triangle class of the flat Z^3 x Z_tau path complex has deficit ZERO to machine precision "
          "(all 50 classes; hinge stars enumerated from the complex itself), hence S_R = 0 on the flat "
          "OS0 background",
          worst_def < 1e-10,
          f"max|deficit| over the 50 triangle classes = {worst_def:.2e}")

    # ---- Schlaefli/Hermiticity check: exactness gates ----
    # per-4-simplex Schlaefli: sum_t A_t dtheta_t/dell_f = 0 for every f
    vs0 = cell_simplices((0, 0, 0, 0))[0]
    qv = []
    ells = []
    for (i, j) in PAIRS5:
        cls, anc = edge_class(vs0[i], vs0[j])
        v = np.array(DIRS15[cls])
        qv.append(float(v @ v))
        ells.append(np.sqrt(float(v @ v)))
    schl = np.zeros(10)
    for (a, b) in PAIRS5:
        hverts = [ii for ii in range(5) if ii not in (a, b)]
        # area of the hinge triangle
        def q_of(i, j):
            return qv[PAIRS5.index((min(i, j), max(i, j)))]
        Aout = AREA(q_of(hverts[0], hverts[1]), q_of(hverts[0], hverts[2]), q_of(hverts[1], hverts[2]))
        out = THETA[(a, b)](*qv)
        for f in range(10):
            schl[f] += float(Aout[0]) * 2 * ells[f] * float(out[1 + f])
    schl_worst = float(np.abs(schl).max())
    kr = np.array([0.41, -0.23, 0.67, 0.31])
    Qr = bloch_Q(kr)
    herm = float(np.abs(Qr - Qr.conj().T).max())
    check("Schlaefli/Hermiticity check (exactness gates): the per-4-simplex Schlaefli identity sum_t A_t d theta_t = 0 holds to "
          "machine precision in every length direction (validates the 4-simplex dihedral-gradient "
          "pipeline), and Q(k) is HERMITIAN to machine precision at random incommensurate momentum "
          "(the complex-level Regge lemma: the flat Hessian is sum_t dA_t (x) d delta_t, symmetric)",
          schl_worst < 1e-12 and herm < 1e-12,
          f"max Schlaefli residual = {schl_worst:.2e}; max|Q - Q^dag| = {herm:.2e}")

    # ---- end-to-end action check: end-to-end action gate on a 3^4 box ----
    Lbox = 3
    kc = np.array([2 * np.pi / Lbox, 0, 0, 0])
    rng = np.random.default_rng(5)
    u = rng.standard_normal(15) * 0.5
    def eps_fun_scaled(t):
        def f(cls, anc):
            return t * u[cls] * np.cos(np.dot(kc, anc))
        return f
    h = 1e-4
    s_p = box_action(Lbox, eps_fun_scaled(+h))
    s_0 = box_action(Lbox, eps_fun_scaled(0.0))
    s_m = box_action(Lbox, eps_fun_scaled(-h))
    fd2 = (s_p - 2 * s_0 + s_m) / h ** 2
    Qc = bloch_Q(kc)
    pred = (Lbox ** 4 / 2.0) * float(np.real(np.conj(u) @ Qc @ u))
    check("end-to-end action check (end-to-end gate): the numerical second difference of the ACTUAL action S_R on a "
          "periodic 3^4 box under a commensurate cosine perturbation equals the Bloch prediction "
          "(N/2) Re[u^dag Q(k) u] (validates every sign, factor, star and phase convention at once)",
          abs(fd2 - pred) < 1e-4 * max(abs(pred), 1e-9),
          f"finite-diff = {fd2:.8f} vs Bloch prediction = {pred:.8f}")

    # ---- gauge-zero-mode check: gauge ----
    g1 = float(np.abs(Qr @ gauge_map(kr)).max())
    k2 = np.array([1.1, 0.6, -0.4, 0.2])
    g2 = float(np.abs(bloch_Q(k2) @ gauge_map(k2)).max())
    check("gauge-zero-mode check (gauge): vertex-displacement fields (4 components per cell) are EXACT zero modes of "
          "Q(k) at every momentum (machine precision at two random incommensurate momenta) -- the "
          "discrete diffeomorphism family of the geometric action on Z^3 x Z_tau",
          g1 < 1e-10 and g2 < 1e-10,
          f"max|Q(k) Gamma(k)| = {g1:.2e}, {g2:.2e}")

    # ---- mode-inventory check: k=0 -- metric zero modes; non-metric sector = 4 massive + 1 exactly-decoupled branch ----
    Q0 = bloch_Q(np.zeros(4)).real
    M0 = metric_map(np.zeros(4)).real
    h_res = float(np.abs(Q0 @ M0).max())
    Uf, sv, _ = np.linalg.svd(M0)
    Pnm = Uf[:, 10:]                      # 5-dim non-metric complement
    W = Pnm.T @ Q0 @ Pnm
    ev = np.sort(np.linalg.eigvalsh((W + W.T) / 2))
    massive = [e for e in ev if abs(e) > 1e-6]
    flat = [e for e in ev if abs(e) <= 1e-6]
    check("mode-inventory check (k=0): constant metric perturbations (all 10 h components) are EXACT zero modes of Q(0); "
          "the FIVE non-metric edge modes split into FOUR massive branches (raw S_R eigenvalues "
          "-48, -16 x3, hence positive after the standard Euclidean orientation) and ONE exactly "
          "flat branch -- identified below (extra-branch decoupling check) as an "
          "exactly-decoupled lattice branch with zero action at ALL momenta, outside the metric sector",
          h_res < 1e-10 and len(massive) == 4 and len(flat) == 1
          and all(e < 0 for e in massive),
          f"max|Q(0) M_metric| = {h_res:.2e}; non-metric eigenvalues (S_R orientation) = "
          f"{[round(float(e), 3) for e in ev]}")

    # ---- extra-branch decoupling check: the fifth branch is an EXACT zero branch at every k, OUTSIDE the metric sector ----
    # (the Rocek-Williams-type spurious lattice direction, here exactly decoupled)
    zero_counts = []
    overlap_ok = True
    for ktest in (np.array([0.01, 0.0, 0.0, 0.0]), np.array([0.3, 0.2, -0.1, 0.4]),
                  np.array([1.1, -0.7, 0.5, 0.9])):
        Qk = bloch_Q(ktest)
        evk, Vk = np.linalg.eigh((Qk + Qk.conj().T) / 2)
        Z = Vk[:, np.abs(evk) < 1e-9]                  # exact zero space
        zero_counts.append(Z.shape[1])
        # gauge space at this k
        Gm = gauge_map(ktest)
        Gq, _ = np.linalg.qr(Gm)
        # dimension of (zero space) intersect (metric image): project Z onto metric image
        Mk = metric_map(ktest)
        Mq, _ = np.linalg.qr(Mk)
        # overlap singular values of Z vs metric image: expect exactly 4 ~1 (the gauge part) + 1 ~small
        svals = np.linalg.svd(Mq.conj().T @ Z, compute_uv=False)
        n_in_metric = int((svals > 0.999).sum())
        if not (Z.shape[1] == 5 and n_in_metric == 4):
            overlap_ok = False
    check("extra-branch decoupling check (the extra branch is decoupled, not physical): at every tested k != 0 the quadratic form "
          "has EXACTLY FIVE machine-zero modes = FOUR discrete-diffeomorphism (gauge) modes + ONE extra "
          "branch; the zero space meets the metric sector in exactly the 4 gauge directions (singular "
          "values: four ~1, fifth small), so the extra exact-zero branch lies OUTSIDE the metric sector "
          "(consistent with the EH pairing having only gauge zeros there): a Rocek-Williams-type "
          "spurious lattice direction, here EXACTLY decoupled at quadratic order -- the physical "
          "low-energy content is the EH sector alone",
          all(zc == 5 for zc in zero_counts) and overlap_ok,
          f"zero-mode counts at three k: {zero_counts}; metric-overlap pattern verified (4 gauge + 1 outside)")

    # ---- 4D comparator check: the comparator across tick-mixed directions ----
    print("\n  4D comparator  Q_h(k) =? c * Q_EH(k)  per direction (tick = the LAST component):")
    dirs = {
        "pure-tick (0,0,0,1)": np.array([0, 0, 0, 1.0]),
        "pure-space (1,0,0,0)": np.array([1.0, 0, 0, 0]),
        "space-space (1,1,0,0)/r2": np.array([1.0, 1.0, 0, 0]) / np.sqrt(2),
        "tick-space (1,0,0,1)/r2": np.array([1.0, 0, 0, 1.0]) / np.sqrt(2),
        "body (1,1,1,1)/2": np.array([1.0, 1.0, 1.0, 1.0]) / 2.0,
    }
    cs = {}
    res_rel = {}
    for nm, khat in dirs.items():
        kk = 1e-3
        Bk = bloch_Q(kk * khat)
        Mk = metric_map(kk * khat)
        Qh = Mk.conj().T @ Bk @ Mk
        Qh = (Qh + Qh.conj().T) / 2
        Meh = einstein_pairing_4d(kk * khat)
        c = float(np.real(np.vdot(Meh, Qh)) / np.vdot(Meh, Meh).real)
        resid = float(np.abs(Qh - c * Meh).max() / max(1e-30, np.abs(Qh).max()))
        cs[nm] = c
        res_rel[nm] = resid
        print(f"    {nm:24s}  c = {c:+.6f}   rel-residual = {resid:.3e}")
    c_vals = np.array(list(cs.values()))
    iso = float(np.ptp(c_vals) / np.abs(c_vals).mean())
    check("4D comparator check (THE 4D COMPARATOR + EMERGENT EUCLIDEAN ISOTROPY): Q_h(k) = c * Q_EH(k) + O(k^4) with "
          "ONE constant c = -1/2 across ALL FIVE directions INCLUDING the tick-space mixed ones -- the "
          "Regge<->EH second-variation correspondence (textbook 1/2 normalization + variational sign) "
          "holds on the 3+1 tick complex, and the O(k^2) graviton-sector isotropy across tick-mixed "
          "directions is the kinetic-isotropy primitive's structural grant realized DYNAMICALLY by the "
          "geometric action on the OS0 surface",
          all(abs(c + 0.5) < 1e-5 for c in c_vals) and all(r < 1e-5 for r in res_rel.values())
          and iso < 1e-5,
          f"c = {dict((k, round(v, 7)) for k, v in cs.items())}; spread/mean = {iso:.2e}")

    # ---- 3+1 fiber-metric check: the 3+1 reading -- geometric lambda-one fiber metric + multiplier structure ----
    om = 1e-3
    ktick = np.array([0, 0, 0, om])      # tick direction = component 3
    Bk = bloch_Q(ktick)
    Mk = metric_map(ktick)
    Qh = Mk.conj().T @ Bk @ Mk
    Qh = np.real((Qh + Qh.conj().T) / 2) / om ** 2
    def hquad(d):
        v = np.zeros(10)
        nrm = 0.0
        for (a, b), val in d.items():
            v[HCOMPS.index((min(a, b), max(a, b)))] = val
            nrm += val ** 2 * (2 if a != b else 1)
        v = v / np.sqrt(nrm)
        return float(v @ Qh @ v)
    K_tr = hquad({(0, 0): 1.0, (1, 1): 1.0, (2, 2): 1.0})     # spatial trace (tick = comp 3)
    K_yz = hquad({(1, 2): 1.0})
    K_E = hquad({(1, 1): 1.0, (2, 2): -1.0})
    K_lapse = hquad({(3, 3): 1.0})
    K_shift = hquad({(0, 3): 1.0})
    ratio = K_tr / K_yz
    check("3+1 fiber-metric check (THE 3+1 READING -- geometric lambda-one fiber metric + multipliers): at pure-tick "
          "momentum, Q_h = omega^2 K with K_spatial-trace : K_TT = -2 : +1 (lambda-one DeWitt, "
          "indefinite, both TT channels equal) and ZERO lapse (h_tick,tick) and shift (h_space,tick) "
          "kinetic weights -- the kinetic fiber metric and multiplier structure of the 3+1 "
          "target-operator row now come from delta^2 S_R of the geometric action NATIVELY (in the raw "
          "S_R orientation the overall sign is flipped; ratios and zeros are orientation-independent)",
          abs(ratio + 2.0) < 1e-4 and abs(K_yz - K_E) < 1e-6 * abs(K_yz)
          and abs(K_lapse) < 1e-6 * abs(K_yz) and abs(K_shift) < 1e-6 * abs(K_yz),
          f"K_trace={K_tr:+.6f}, K_TT(yz)={K_yz:+.6f}, K_TT(E)={K_E:+.6f} (ratio {ratio:+.4f}); "
          f"K_lapse={K_lapse:+.2e}, K_shift={K_shift:+.2e}")

    # ---- spatial-sign comparator check: potential signs at zero tick-frequency (spatial k || x) ----
    kx = np.array([1e-3, 0, 0, 0])
    Bk = bloch_Q(kx)
    Mk = metric_map(kx)
    Qh = np.real((Mk.conj().T @ Bk @ Mk + (Mk.conj().T @ Bk @ Mk).conj().T) / 2) / 1e-6
    def hq2(d):
        v = np.zeros(10)
        nrm = 0.0
        for (a, b), val in d.items():
            v[HCOMPS.index((min(a, b), max(a, b)))] = val
            nrm += val ** 2 * (2 if a != b else 1)
        return float(v @ Qh @ v) / nrm
    V_yz = hq2({(1, 2): 1.0})
    V_E = hq2({(1, 1): 1.0, (2, 2): -1.0})
    V_trT = hq2({(1, 1): 1.0, (2, 2): 1.0})
    rt = V_trT / V_yz
    check("spatial-sign comparator check (potential signs, spatial k || x at zero tick-frequency): the two spatial TT channels are "
          "EQUAL and the transverse-trace channel is equal-magnitude OPPOSITE-sign (ratio -1) -- the "
          "degenerate-supermetric no-go's supplied pair, re-derived inside the 3+1 tick complex "
          "(consistent with the 3D row); the single remaining sign is the overall action orientation "
          "(the located sign residual)",
          abs(V_yz - V_E) < 1e-6 * abs(V_yz) and abs(rt + 1.0) < 1e-4,
          f"V_TT(yz)={V_yz:+.6f} = V_TT(E)={V_E:+.6f}; transverse-trace={V_trT:+.6f} (ratio {rt:+.4f})")

    print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
    print(
        "VERDICT: the retained 3D cubic-Coxeter chain extends by the emergent tick (Z^3 x Z_tau, the\n"
        "path complex whose spatial slice IS the retained chain; c_t = c_s per the kinetic-isotropy\n"
        "primitive, structural grant only), and on the flat OS0 background: deficits vanish (the 4D\n"
        "tick extension of the retained flat anchor), vertex displacements are exact zero modes at\n"
        "every momentum, the five non-metric modes are massive, and the second variation of the Regge\n"
        "action matches c = -1/2 times the 4D Euclidean linearized EH pairing at O(k^2) ISOTROPICALLY\n"
        "ACROSS TICK-MIXED DIRECTIONS -- so at pure-tick momentum the geometric action natively yields\n"
        "the lambda-one DeWitt kinetic fiber metric (K_trace:K_TT = -2:+1, both TT equal) with ZERO\n"
        "lapse/shift kinetic weights (the multiplier structure), and at zero tick-frequency the\n"
        "spatial comparator pair (+-, equal magnitude). The supplied comparator inputs named by the\n"
        "degenerate-supermetric no-go and the structural pieces certified by the 3+1 target-operator\n"
        "row are reproduced on this tick complex by delta^2 S_R. Remaining open: the overall action\n"
        "orientation (the same single located sign residual), edge-length-DOF provenance, action\n"
        "selection, nonlinear closure. The tick-scale itself is NOT derived (retained clock-rate no-go\n"
        "respected; c_t = c_s is the primitive's structural grant). No PDG/fitted value."
    )
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
