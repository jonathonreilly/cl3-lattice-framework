#!/usr/bin/env python3
"""Independent finite checks for the fixed-half cubic flux theorem note."""

import ast, time

import numpy as np
import sympy as sp


TOL = 3e-9
AUDIT_TIMEOUT_SEC = 180
START = time.perf_counter()
I2 = np.eye(2, dtype=complex)
Z2 = np.diag([1.0, -1.0]).astype(complex)
LOWER = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)


def kron_all(items):
    out = np.array([[1.0]], dtype=complex)
    for item in items:
        out = np.kron(out, item)
    return out


def fermion_ops(modes):
    return [kron_all([Z2 if k < j else LOWER if k == j else I2 for k in range(modes)]) for j in range(modes)]


def defect(a):
    return float(np.max(np.abs(a)))


def restricted(a, indices):
    return a[np.ix_(indices, indices)]


A8 = fermion_ops(8)
AD8 = [a.conj().T for a in A8]
NOPS8 = [AD8[j] @ A8[j] for j in range(8)]
NUM8 = sum(NOPS8)
QOPS8 = [n - 0.5 * np.eye(256) for n in NOPS8]
NDIAG8 = np.rint(np.real(np.diag(NUM8))).astype(int)
N4IDX = np.flatnonzero(NDIAG8 == 4)
COORDS = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
MODE = {x: j for j, x in enumerate(COORDS)}
EDGES = []
for x in COORDS:
    for axis in range(3):
        if x[axis] == 0:
            y = list(x)
            y[axis] = 1
            EDGES.append((MODE[x], MODE[tuple(y)], axis))
BIL8 = {(p, q): AD8[p] @ A8[q] for p, q, _ in EDGES for p, q in ((p, q), (q, p))}
QQ8 = {(p, q): QOPS8[p] @ QOPS8[q] for p, q, _ in EDGES}
NN8 = {(p, q): NOPS8[p] @ NOPS8[q] for p, q, _ in EDGES}

A4 = fermion_ops(4)
AD4 = [a.conj().T for a in A4]
NOPS4 = [AD4[j] @ A4[j] for j in range(4)]
NUM4 = sum(NOPS4)
QOPS4 = [n - 0.5 * np.eye(16) for n in NOPS4]
BIL4 = {(p, q): AD4[p] @ A4[q] for p in range(4) for q in range(4)}
NDIAG4 = np.rint(np.real(np.diag(NUM4))).astype(int)
QDIAG = (NDIAG4[:, None] - NDIAG4[None, :]).reshape(-1)
Q0IDX = np.flatnonzero(QDIAG == 0)


def full_hamiltonian(coefficients, coupling, centered=True):
    if coupling < 0: raise ValueError("reflection domain requires V >= 0")
    h = np.zeros((256, 256), dtype=complex)
    densities = QQ8 if centered else NN8
    for p, q, _ in EDGES:
        z = coefficients[(p, q)]
        h += z * BIL8[(p, q)] + z.conjugate() * BIL8[(q, p)]
        h += coupling * densities[(p, q)]
    return h


def local_hamiltonian(hopping, coupling, local_edges):
    h = np.zeros((16, 16), dtype=complex)
    for p, q in local_edges:
        z = hopping[p, q]
        h += z * BIL4[(p, q)] + z.conjugate() * BIL4[(q, p)]
        h += coupling * (QOPS4[p] @ QOPS4[q])
    return h


def post_hamiltonian(left, right, coupling):
    h = np.kron(left, np.eye(16)) + np.kron(np.eye(16), right)
    for j in range(4):
        kp = (AD4[j] + A4[j]) / np.sqrt(2.0)
        km = (AD4[j] - A4[j]) / np.sqrt(2.0)
        h -= np.kron(kp, kp) + np.kron(km, km)
        h -= coupling * np.kron(QOPS4[j], QOPS4[j])
    return h


def cut_fixture(axis, coupling, sample):
    if coupling < 0: raise ValueError("reflection domain requires V >= 0")
    left = [j for j, x in enumerate(COORDS) if x[axis] == 0]
    right = [j for j, x in enumerate(COORDS) if x[axis] == 1]
    li, ri = {j: k for k, j in enumerate(left)}, {j: k for k, j in enumerate(right)}
    rng = np.random.default_rng(7301 + 101 * axis + sample)
    hl, hr = np.zeros((4, 4), dtype=complex), np.zeros((4, 4), dtype=complex)
    coefficients, local_edges = {}, []
    for p, q, edge_axis in EDGES:
        if edge_axis == axis:
            coefficients[(p, q)] = -1.0
        else:
            z = -np.exp(1j * rng.uniform(-np.pi, np.pi))
            coefficients[(p, q)] = z
            table, index = (hl, li) if p in li else (hr, ri)
            u, v = index[p], index[q]
            table[u, v], table[v, u] = z, z.conjugate()
            if p in li:
                local_edges.append((u, v))
    return hl, hr, coefficients, sorted(local_edges), li, ri


def coefficients_from_halves(axis, hl, hr, li, ri):
    out = {}
    for p, q, edge_axis in EDGES:
        if edge_axis == axis:
            out[(p, q)] = -1.0
        else:
            table, index = (hl, li) if p in li else (hr, ri)
            out[(p, q)] = table[index[p], index[q]]
    return out


def algebra_check():
    car = 0.0
    zero = np.zeros((256, 256), dtype=complex)
    eye = np.eye(256)
    for i in range(8):
        for j in range(8):
            car = max(car, defect(A8[i] @ A8[j] + A8[j] @ A8[i]))
            target = eye if i == j else zero
            car = max(car, defect(A8[i] @ AD8[j] + AD8[j] @ A8[i] - target))
    v = 1.4
    empty = {(p, q): 0.0 for p, q, _ in EDGES}
    hc, hu = full_hamiltonian(empty, v, True), full_hamiltonian(empty, v, False)
    identity = hc - hu + 1.5 * v * NUM8 - 3.0 * v * eye
    centering = max(defect(restricted(identity, np.flatnonzero(NDIAG8 == n))) for n in (2, 4, 6))
    ok = car < TOL and centering < TOL and len(N4IDX) == 70
    return ok, f"CAR={car:.1e} centering_N2,4,6={centering:.1e} dimN4={len(N4IDX)}"


def exact_polar_check():
    ii = sp.I
    sy = sp.Matrix([[0, -ii], [ii, 0]])
    ident = sp.eye(2)
    c = ident - sy / 2
    norm = sp.trace(c.H * c)
    vec = sp.Matrix([c[i, j] for i in range(2) for j in range(2)])
    energy = lambda x, a, b: sp.simplify((x.H * (sp.kronecker_product(a, ident) +
                                                  sp.kronecker_product(ident, b)) * x)[0] / norm)
    original = energy(vec, sy, -sy)
    reflected = (energy(vec, sy, sy.conjugate()) + energy(vec, (-sy).conjugate(), -sy)) / 2
    mutated = (energy(vec, sy, sy) + energy(vec, -sy, -sy)) / 2
    c2 = sp.Matrix([[0, 1], [2, 0]])
    l2, r2, k = sp.diag(1, 2), sp.diag(2, 1), sp.diag(1, -1)
    svec = lambda m: sp.Matrix([m[i, j] for i in range(2) for j in range(2)])
    v2 = svec(c2)
    cross = lambda x: sp.simplify(-(x.H * sp.kronecker_product(k, k) * x)[0] / (x.H * x)[0])
    polar_margin = sp.simplify(cross(v2) - (cross(svec(l2)) + cross(svec(r2))) / 2)
    cross_trace = -sp.trace(c2.H * k * c2 * k.T) / sp.trace(c2.H * c2)
    ci = sp.eye(2)
    ki = ii * sp.eye(2)
    vi = svec(ci)
    direct_transpose = (vi.H * sp.kronecker_product(ki, ki) * vi)[0] / 2
    transpose = sp.trace(ci.H * ki * ci * ki.T) / 2
    wrong_adjoint = sp.trace(ci.H * ki * ci * ki.H) / 2
    number = sp.diag(0, 1)
    cq = sp.Matrix([[0, 0], [1, 0]])
    lq, rq = sp.diag(0, 1), sp.diag(1, 0)
    charge = number * cq - cq * number
    closure = number * lq - lq * number == sp.zeros(2) and number * rq - rq * number == sp.zeros(2)
    ok = (original == reflected == sp.Rational(-8, 5) and original - mutated == sp.Rational(-8, 5)
          and polar_margin == 2 and cross(v2) == cross_trace and l2**2 == c2 * c2.H
          and r2**2 == c2.H * c2 and direct_transpose == transpose == -1
          and wrong_adjoint == 1 and charge == cq and closure)
    cert = (f"local={original} drop_bar_margin={original-mutated} polar_margin={polar_margin} "
            f"KT={transpose} Kdag={wrong_adjoint} q_to_Q0={closure}")
    return ok, cert


def reflection_check():
    max_spec = max_herm = max_conserve = max_closure = max_norm = 0.0
    min_ground_margin = min_trial_margin = np.inf
    cases = 0
    for axis in (0, 1):
        for coupling in (0.0, 0.6, 2.0):
            for sample in (0, 1):
                hl, hr, coeff, ledges, li, ri = cut_fixture(axis, coupling, sample)
                left = local_hamiltonian(hl, coupling, ledges)
                right = local_hamiltonian(-hr.T, coupling, ledges)
                t0 = post_hamiltonian(left, right, coupling)
                t1 = post_hamiltonian(left, left.conjugate(), coupling)
                t2 = post_hamiltonian(right.conjugate(), right, coupling)
                h0 = full_hamiltonian(coeff, coupling)
                c1 = coefficients_from_halves(axis, hl, -hl, li, ri)
                c2 = coefficients_from_halves(axis, -hr, hr, li, ri)
                h1, h2 = full_hamiltonian(c1, coupling), full_hamiltonian(c2, coupling)
                mats = (h0, h1, h2, t0, t1, t2)
                max_herm = max(max_herm, *(defect(h - h.conj().T) for h in mats))
                max_conserve = max(max_conserve, *(defect(h * (NDIAG8[None, :] - NDIAG8[:, None])) for h in mats[:3]),
                                   *(defect(h * (QDIAG[None, :] - QDIAG[:, None])) for h in mats[3:]))
                wp = [np.linalg.eigvalsh(restricted(h, N4IDX)) for h in mats[:3]]
                wt0, vt0 = np.linalg.eigh(restricted(t0, Q0IDX))
                wt = [wt0, np.linalg.eigvalsh(restricted(t1, Q0IDX)), np.linalg.eigvalsh(restricted(t2, Q0IDX))]
                max_spec = max(max_spec, *(float(np.max(np.abs(a - b))) for a, b in zip(wp, wt)))
                min_ground_margin = min(min_ground_margin, wt[0][0] - (wt[1][0] + wt[2][0]) / 2)
                full_vec = np.zeros(256, dtype=complex)
                full_vec[Q0IDX] = vt0[:, 0]
                cm = full_vec.reshape(16, 16)
                u, s, vh = np.linalg.svd(cm, full_matrices=False)
                lp = (u * s) @ u.conj().T
                rp = (vh.conj().T * s) @ vh
                vl, vr = lp.reshape(-1), rp.reshape(-1)
                trial = (np.vdot(vl, t1 @ vl).real + np.vdot(vr, t2 @ vr).real) / 2
                min_trial_margin = min(min_trial_margin, wt0[0] - trial)
                max_closure = max(max_closure, defect(lp * (NDIAG4[None, :] - NDIAG4[:, None])),
                                  defect(rp * (NDIAG4[None, :] - NDIAG4[:, None])))
                max_norm = max(max_norm, abs(np.vdot(vl, vl).real - 1), abs(np.vdot(vr, vr).real - 1))
                cases += 1
    ok = (max_spec < TOL and max_herm < TOL and max_conserve < TOL and max_closure < TOL
          and max_norm < TOL and min_ground_margin > -TOL and min_trial_margin > -TOL)
    cert = (f"cases={cases} spec={max_spec:.1e} herm={max_herm:.1e} N/Q={max_conserve:.1e} "
            f"polar_Q0={max_closure:.1e} norm={max_norm:.1e} margins=({min_trial_margin:.3e},{min_ground_margin:.3e})")
    return ok, cert


def canonical_cube_diagnostic():
    coeff = {}
    plaquette_products = []
    for p, q, axis in EDGES:
        x = COORDS[p]
        eta = 1 if axis == 0 else (-1) ** x[0] if axis == 1 else (-1) ** (x[0] + x[1])
        coeff[(p, q)] = -eta
    for a, b in ((0, 1), (0, 2), (1, 2)):
        for x in COORDS:
            if x[a] == x[b] == 0:
                xa, xb = list(x), list(x)
                xa[a], xb[b] = 1, 1
                p, pa, pb = MODE[x], MODE[tuple(xa)], MODE[tuple(xb)]
                edge = lambda u, v: coeff[(u, v)] if (u, v) in coeff else coeff[(v, u)].conjugate()
                pab = list(xa)
                pab[b] = 1
                qab = MODE[tuple(pab)]
                plaquette_products.append(edge(p, pa) * edge(pa, qab) * edge(qab, pb) * edge(pb, p))
    max_gap = 0.0
    for coupling in (0.0, 0.75, 3.0):
        h = full_hamiltonian(coeff, coupling)
        max_gap = max(max_gap, abs(np.linalg.eigvalsh(h)[0] - np.linalg.eigvalsh(restricted(h, N4IDX))[0]))
    flux_defect = max(abs(z + 1) for z in plaquette_products)
    return max_gap < TOL and flux_defect < TOL, f"diagnostic_only centered_full_vs_N4={max_gap:.1e} plaquette={flux_defect:.1e}"


def canonical_seam(length):
    if length < 4 or length % 2:
        raise ValueError("simple even torus requires L >= 4")
    return -1 if length % 4 == 0 else 1


def shift_matrix(length, seam):
    t = np.zeros((length, length))
    for j in range(length - 1):
        t[j, j + 1] = t[j + 1, j] = 1
    t[0, -1] = t[-1, 0] = seam
    return t


def torus_matrix(shape, seams=None):
    seams = tuple(canonical_seam(n) for n in shape) if seams is None else seams
    ts = [shift_matrix(n, w) for n, w in zip(shape, seams)]
    zs = [np.diag([(-1) ** j for j in range(n)]) for n in shape]
    ids = [np.eye(n) for n in shape]
    terms = [np.kron(np.kron(ts[0], ids[1]), ids[2]), np.kron(np.kron(zs[0], ts[1]), ids[2]),
             np.kron(np.kron(zs[0], zs[1]), ts[2])]
    h = -sum(terms)
    square = (np.kron(np.kron(ts[0] @ ts[0], ids[1]), ids[2]) + np.kron(np.kron(ids[0], ts[1] @ ts[1]), ids[2])
              + np.kron(np.kron(ids[0], ids[1]), ts[2] @ ts[2]))
    clifford = max(defect(terms[i] @ terms[j] + terms[j] @ terms[i]) for i in range(3) for j in range(i + 1, 3))
    return h, defect(h @ h - square), clifford, seams


def torus_check():
    gap_error = square_error = clifford_error = herm = 0.0
    certificates = []
    for shape in ((4, 4, 4), (4, 4, 6), (6, 6, 6)):
        h, sq, cl, seams = torus_matrix(shape)
        gap = float(np.min(np.abs(np.linalg.eigvalsh(h))))
        formula = 2 * np.sqrt(sum(np.sin(np.pi / n) ** 2 for n in shape))
        gap_error, square_error = max(gap_error, abs(gap - formula)), max(square_error, sq)
        clifford_error, herm = max(clifford_error, cl), max(herm, defect(h - h.T))
        certificates.append(f"{shape}:{2*gap:.6f}/{seams}")
    wrong, _, _, wrong_seams = torus_matrix((4, 4, 4), (1, 1, 1))
    wrong_gap = float(np.min(np.abs(np.linalg.eigvalsh(wrong))))
    control = wrong_seams != (-1, -1, -1) and wrong_gap < TOL
    ok = max(gap_error, square_error, clifford_error, herm) < TOL and control
    cert = (f"bandgaps={';'.join(certificates)} formula={gap_error:.1e} h2={square_error:.1e} "
            f"clifford={clifford_error:.1e} herm={herm:.1e} wrong4_gap={wrong_gap:.1e}")
    return ok, cert


def guard_and_firewall_check():
    rejected = 0
    for action in (lambda: canonical_seam(5), lambda: canonical_seam(2), lambda: cut_fixture(0, -0.1, 0)):
        try:
            action()
        except ValueError:
            rejected += 1
    tree = ast.parse(open(__file__, encoding="utf-8").read())
    roots = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            roots.add((node.module or "").split(".")[0])
    allowed = {"ast", "time", "numpy", "sympy"}
    certificate = f"domain_rejections={rejected}/3 imports={','.join(sorted(roots))} local_imports={len(roots-allowed)}"
    return rejected == 3 and roots <= allowed, certificate


def main():
    checks = [("pauli_car_centering", algebra_check), ("exact_polar_mutations", exact_polar_check),
              ("fixed_half_reflection", reflection_check), ("centered_ground_diagnostic", canonical_cube_diagnostic),
              ("canonical_torus", torus_check),
              ("guards_import_firewall", guard_and_firewall_check)]
    passed = failed = 0
    for name, check in checks:
        try:
            ok, certificate = check()
        except Exception as exc:
            ok, certificate = False, f"exception={type(exc).__name__}:{exc}"
        print(f"{'PASS' if ok else 'FAIL'} {name} {certificate}")
        passed += int(ok)
        failed += int(not ok)
    print(f"RUNTIME_SECONDS={time.perf_counter()-START:.3f}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    raise SystemExit(1 if failed else 0)


if __name__ == "__main__":
    main()
