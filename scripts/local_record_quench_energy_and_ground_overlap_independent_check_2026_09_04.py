#!/usr/bin/env python3
"""Independent checker for singleton local-quench energy and ground overlap.

The arithmetic is deliberately disjoint from the primary runner: exact
exterior-algebra amplitudes, rational SPD controls, scalar spectral moments,
and integer antiperiodic momentum grids.  It reads no repository science input.

Scope: h=[[0,Q],[Q^dagger,0]] with square invertible Q, deletion sites S in
one sublattice, and the canonical theta=pi (N even), theta=0 (N odd) twist in
each axis for cubic side L=2N, N>=2.  Every finite Fock comparison stays in its
original fixed-number sector.
"""

import ast
import hashlib
import math
import sys
from itertools import combinations, product
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import quad


AUDIT_TIMEOUT_SEC = 180
EXPECTED_FILENAME = "local_record_quench_energy_and_ground_overlap_independent_check_2026_09_04.py"
TOL = 2.0e-10


class CheckFailure(RuntimeError):
    pass


def require(condition, message):
    if not bool(condition):
        raise CheckFailure(message)


def exact_zero(value):
    return sp.simplify(value) == 0


def state_norm(state):
    return sp.simplify(sum(sp.conjugate(value) * value for value in state.values()))


def slater_amplitudes(orbitals):
    """Exterior amplitudes in the canonical increasing-mode occupation basis."""
    modes, particles = orbitals.shape
    state = {}
    for occupied in combinations(range(modes), particles):
        amplitude = sp.simplify(orbitals.extract(occupied, range(particles)).det())
        if amplitude != 0:
            mask = sum(1 << mode for mode in occupied)
            state[mask] = amplitude
    require(exact_zero(state_norm(state) - 1), "Slater exterior state is not normalized")
    return state


def annihilate(mask, mode):
    mask = int(mask)
    mode = int(mode)
    if not (mask >> mode) & 1:
        return None
    sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
    return mask ^ (1 << mode), sign


def create(mask, mode):
    mask = int(mask)
    mode = int(mode)
    if (mask >> mode) & 1:
        return None
    sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
    return mask | (1 << mode), sign


def cdag_c_expectation(state, create_mode, annihilate_mode):
    total = 0
    for mask, amplitude in state.items():
        first = annihilate(mask, annihilate_mode)
        if first is None:
            continue
        intermediate, sign1 = first
        second = create(intermediate, create_mode)
        if second is None:
            continue
        final, sign2 = second
        total += sp.conjugate(state.get(final, 0)) * sign1 * sign2 * amplitude
    return sp.simplify(total)


def covariance_from_state(state, modes):
    """C[p,q]=<c_q^dagger c_p>, matching the one-particle projector convention."""
    return sp.Matrix(
        modes,
        modes,
        lambda p, q: cdag_c_expectation(state, q, p),
    )


def project_occupation(state, mode, outcome):
    selected = {
        mask: amplitude
        for mask, amplitude in state.items()
        if ((mask >> mode) & 1) == outcome
    }
    probability = state_norm(selected)
    require(probability > 0, "zero-probability branch in exact Fock control")
    normalized = {
        mask: sp.simplify(amplitude / sp.sqrt(probability))
        for mask, amplitude in selected.items()
    }
    require(exact_zero(state_norm(normalized) - 1), "projected branch is not normalized")
    return probability, normalized


def fock_inner(left, right):
    return sp.simplify(
        sum(sp.conjugate(left.get(mask, 0)) * value for mask, value in right.items())
    )


def second_quantized_energy(state, one_particle_h):
    total = 0
    for p in range(one_particle_h.rows):
        for q in range(one_particle_h.cols):
            if one_particle_h[p, q] != 0:
                total += one_particle_h[p, q] * cdag_c_expectation(state, p, q)
    return sp.simplify(total)


def two_mode_exact_data():
    """Build one complex-polar two-mode quench entirely from exact amplitudes."""
    root2 = sp.sqrt(2)
    K = sp.Matrix([[2, 1], [1, 2]])
    U = sp.Matrix([[1, sp.I], [sp.I, 1]]) / root2
    Q = sp.simplify(K * U)
    require(K == K.conjugate().T and K.det() > 0 and K[0, 0] > 0, "K is not certified SPD")
    require(Q.rows == Q.cols and Q.det() != 0, "Q is not square and invertible")
    require(U * U.conjugate().T == sp.eye(2), "complex polar factor is not unitary")
    require(sp.simplify(Q * Q.conjugate().T - K**2) == sp.zeros(2), "Q Q^dagger != K^2")

    h_full = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(2), Q),
        sp.Matrix.hstack(Q.conjugate().T, sp.zeros(2)),
    )
    require(h_full == h_full.conjugate().T, "full one-particle Hamiltonian is not Hermitian")
    require(
        sp.simplify(h_full**2 - sp.diag(K**2, U.conjugate().T * K**2 * U)) == sp.zeros(4),
        "full h-squared block identity failed",
    )

    initial_orbitals = sp.Matrix.vstack(sp.eye(2), -U.conjugate().T) / root2
    initial_state = slater_amplitudes(initial_orbitals)

    measured = 1
    kept = [0]
    Q_T = Q.extract(kept, range(2))
    B = sp.sqrt((Q_T * Q_T.conjugate().T)[0, 0])
    V = sp.simplify(Q_T / B)
    u = U.conjugate().T[:, measured]
    raw_z = U.conjugate().T * K.inv()[:, measured]
    z = sp.simplify(raw_z / sp.sqrt((raw_z.conjugate().T * raw_z)[0]))
    require(sp.simplify(Q_T * z) == sp.zeros(1, 1), "proposed zero mode is not in ker Q_T")
    require(sp.simplify(V * V.conjugate().T) == sp.eye(1), "reduced polar factor is not a coisometry")

    beta = sp.simplify(abs((z.conjugate().T * u)[0]) ** 2)
    alpha = sp.simplify(1 - beta)
    L_value = sp.simplify(1 - K[0, 0] / B)
    expected_probability = sp.Rational(1, 2)
    expected_ell = sp.Rational(11, 20) - 1 / sp.sqrt(5)

    reduced_positive = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(1) / 2, V / 2),
        sp.Matrix.hstack(V.conjugate().T / 2, V.conjugate().T * V / 2),
    )
    reduced_negative = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.eye(1) / 2, -V / 2),
        sp.Matrix.hstack(-V.conjugate().T / 2, V.conjugate().T * V / 2),
    )

    h_deleted = sp.zeros(4)
    h_deleted[0, 2:4] = Q_T
    h_deleted[2:4, 0] = Q_T.conjugate().T
    require(h_deleted == h_deleted.conjugate().T, "deleted one-particle Hamiltonian is not Hermitian")

    negative_orbital = sp.Matrix(
        [1 / root2, 0, -sp.conjugate(V[0, 0]) / root2, -sp.conjugate(V[0, 1]) / root2]
    )
    zero_b_orbital = sp.Matrix([0, 0, z[0], z[1]])
    measured_orbital = sp.Matrix([0, 1, 0, 0])

    branches = {}
    for outcome in (0, 1):
        probability, state = project_occupation(initial_state, measured, outcome)
        covariance = covariance_from_state(state, 4)
        remaining_indices = [0, 2, 3]
        reduced_covariance = covariance.extract(remaining_indices, remaining_indices)

        U_T = U.extract(kept, range(2))
        analytic_reduced = sp.Matrix.vstack(
            sp.Matrix.hstack(sp.eye(1) / 2, -U_T / 2),
            sp.Matrix.hstack(
                -U_T.conjugate().T / 2,
                sp.eye(2) / 2 + (sp.Rational(1, 2) - outcome) * u * u.conjugate().T,
            ),
        )
        require(
            sp.simplify(reduced_covariance - analytic_reduced) == sp.zeros(3),
            f"Fock conditioning covariance mismatch for n={outcome}",
        )
        require(exact_zero(probability - expected_probability), f"branch probability mismatch n={outcome}")
        require(
            all(((mask >> measured) & 1) == outcome for mask in state),
            f"occupation projection failed n={outcome}",
        )

        post_energy = second_quantized_energy(state, h_deleted)
        require(exact_zero(post_energy + 2), f"post energy mismatch n={outcome}")

        ground_orbitals = sp.Matrix.hstack(
            negative_orbital,
            zero_b_orbital if outcome == 0 else measured_orbital,
        )
        ground_state = slater_amplitudes(ground_orbitals)
        ground_energy = second_quantized_energy(ground_state, h_deleted)
        require(exact_zero(ground_energy + sp.sqrt(5)), f"ground energy mismatch n={outcome}")

        ground_covariance = sp.simplify(ground_orbitals * ground_orbitals.conjugate().T)
        ell = sp.simplify(sp.trace(ground_covariance * (sp.eye(4) - covariance)))
        frobenius_squared = sp.simplify(sp.trace((covariance - ground_covariance) ** 2))
        amplitude = fock_inner(ground_state, state)
        fidelity = sp.simplify(sp.conjugate(amplitude) * amplitude)
        zero_occupancy = sp.simplify(
            (z.conjugate().T * covariance.extract([2, 3], [2, 3]) * z)[0]
        )

        n_plus = sp.simplify(sp.trace(reduced_positive * reduced_covariance))
        n_holes = sp.simplify(sp.trace(reduced_negative * (sp.eye(3) - reduced_covariance)))
        require(
            exact_zero(n_plus - (L_value / 2 + (1 - 2 * outcome) * alpha / 4)),
            f"positive excitation mismatch n={outcome}",
        )
        require(
            exact_zero(n_holes - (L_value / 2 - (1 - 2 * outcome) * alpha / 4)),
            f"negative hole mismatch n={outcome}",
        )
        require(exact_zero(n_plus + n_holes - L_value), f"excitation sum mismatch n={outcome}")
        require(exact_zero(ell - expected_ell), f"ground leakage mismatch n={outcome}")
        require(exact_zero(frobenius_squared - 2 * ell), f"projector distance mismatch n={outcome}")
        require(exact_zero(fidelity - (1 - ell)), f"squared Slater overlap mismatch n={outcome}")
        require(
            exact_zero(zero_occupancy - (sp.Rational(1, 2) + (sp.Rational(1, 2) - outcome) * beta)),
            f"zero-mode occupation mismatch n={outcome}",
        )
        require(not exact_zero(abs(amplitude) - fidelity), "overlap amplitude was confused with its square")
        branches[outcome] = {
            "probability": probability,
            "post_energy": post_energy,
            "ground_energy": ground_energy,
            "ell": ell,
            "fidelity": fidelity,
            "zero_occupancy": zero_occupancy,
        }

    return {
        "K": K,
        "U": U,
        "Q": Q,
        "beta": beta,
        "alpha": alpha,
        "L": L_value,
        "ell": expected_ell,
        "branches": branches,
    }


def check_source_integrity():
    source_path = Path(__file__).resolve()
    require(source_path.name == EXPECTED_FILENAME, "unexpected checker filename")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    allowed_imports = {"ast", "hashlib", "itertools", "math", "pathlib", "sys", "numpy", "scipy", "sympy"}
    seen_imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots = {alias.name.split(".")[0] for alias in node.names}
            seen_imports.update(roots)
            require(roots <= allowed_imports, f"forbidden import roots: {sorted(roots - allowed_imports)}")
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            seen_imports.add(root)
            require(node.level == 0 and root in allowed_imports, f"forbidden from-import: {node.module}")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in {"open", "exec", "eval", "compile", "__import__"}, f"forbidden dynamic/file call: {node.func.id}")
    read_calls = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"read_text", "read_bytes", "read", "load", "loads"}
    ]
    require(len(read_calls) == 1 and read_calls[0].func.attr == "read_text", "external read surface detected")
    timeout_values = []
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(
            isinstance(target, ast.Name) and target.id == "AUDIT_TIMEOUT_SEC" for target in node.targets
        ):
            timeout_values.append(ast.literal_eval(node.value))
    require(timeout_values == [180], f"timeout declaration drifted: {timeout_values}")
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    return f"sha256={digest[:16]} imports={','.join(sorted(seen_imports))} reads=self-only"


def check_exact_fock_projection():
    data = two_mode_exact_data()
    branch0, branch1 = data["branches"][0], data["branches"][1]
    require(branch0["probability"] == branch1["probability"] == sp.Rational(1, 2), "Fock probabilities not equiprobable")
    require(branch0["post_energy"] == branch1["post_energy"] == -2, "branch energies differ")
    return "P(n=0)=P(n=1)=1/2 Epost=-2 zero_occ=(9/10,1/10)"


def check_fixed_number_energy_and_trace_bounds():
    K = sp.Matrix(
        [[3, 1, 0, 0],
         [1, 3, 1, 0],
         [0, 1, 3, 1],
         [0, 0, 1, 3]]
    )
    require(tuple(K[:n, :n].det() for n in range(1, 5)) == (3, 8, 21, 55), "K is not certified SPD")
    deleted, kept = [0, 2], [1, 3]
    projection = sp.diag(0, 1, 0, 1)
    require(projection * K != K * projection, "multisite control unexpectedly reduces K")
    M_T = (K**2).extract(kept, kept)
    trace_sqrt = sp.sqrt(sp.trace(M_T) + 2 * sp.sqrt(M_T.det()))
    delta = sp.simplify(trace_sqrt - sum(K[index, index] for index in kept))
    expected_multisite = sp.sqrt(21 + 2 * sp.sqrt(109)) - 6
    require(exact_zero(delta - expected_multisite), "noncommuting multisite excess mismatch")
    jump = sum(K[index, index] for index in deleted)
    require(delta > 0 and delta < jump, "trace bounds fail on noncommuting control")

    diagonal = sp.diag(1, 2, 4)
    diagonal_delta = sp.sqrt((diagonal**2)[0, 0]) - diagonal[0, 0]
    require(diagonal_delta == 0 and diagonal[0, 0] == 1, "diagonal singleton zero-excess control failed")
    K_float = np.array(K, dtype=float)
    for label, deleted, expected_jump in (("empty", (), 0.0), ("full", tuple(range(4)), 12.0)):
        kept_numeric = tuple(index for index in range(4) if index not in deleted)
        if kept_numeric:
            compressed = (K_float @ K_float)[np.ix_(kept_numeric, kept_numeric)]
            nuclear = float(np.sqrt(np.linalg.eigvalsh(compressed)).sum())
            kept_trace = float(np.trace(K_float[np.ix_(kept_numeric, kept_numeric)]))
        else:
            nuclear = kept_trace = 0.0
        edge_delta = nuclear - kept_trace
        edge_jump = float(np.trace(K_float[np.ix_(deleted, deleted)])) if deleted else 0.0
        require(abs(edge_delta) < TOL and abs(edge_jump - expected_jump) < TOL, f"{label} deletion edge case failed")
    return f"Delta_multi={float(delta):.12f} jump_multi=6 diagonal=(jump=1,Delta=0) empty=(0,0) full=(12,0)"


def check_leakage_and_squared_overlap():
    data = two_mode_exact_data()
    expected_ell = sp.Rational(11, 20) - 1 / sp.sqrt(5)
    expected_fidelity = sp.Rational(9, 20) + 1 / sp.sqrt(5)
    require(exact_zero(data["ell"] - expected_ell), "exact leakage value mismatch")
    for outcome in (0, 1):
        branch = data["branches"][outcome]
        require(exact_zero(branch["ell"] - expected_ell), f"branch leakage mismatch n={outcome}")
        require(exact_zero(branch["fidelity"] - expected_fidelity), f"branch fidelity mismatch n={outcome}")
        require(branch["fidelity"] >= 1 - branch["ell"], f"determinant lower bound fails n={outcome}")
    return f"alpha=1/5 L={float(data['L']):.12f} ell={float(expected_ell):.12f} F={float(expected_fidelity):.12f}"


def variance_quadrature(eigenvalues, weights):
    eigenvalues = np.asarray(eigenvalues, dtype=float)
    weights = np.asarray(weights, dtype=float)

    def integrand(s):
        values = 1.0 / (s + eigenvalues)
        mean = float(weights @ values)
        variance = float(weights @ ((values - mean) ** 2))
        return math.sqrt(s) * variance / mean / math.pi

    return quad(integrand, 0.0, np.inf, epsabs=2.0e-12, epsrel=2.0e-12, limit=300)


def check_resolvent_and_scalar_quadrature():
    K = sp.Matrix([[2, 1], [1, 2]])
    M = K**2
    s = sp.symbols("s", positive=True)
    g = sp.factor((s * sp.eye(2) + M).inv()[0, 0])
    expected_g = (s + 5) / ((s + 1) * (s + 9))
    require(exact_zero(g - expected_g), "singleton resolvent g sign/denominator mismatch")
    M_T = sp.Matrix([[M[1, 1]]])
    jacobi_residual = sp.simplify((s + M_T[0, 0]) - (s * sp.eye(2) + M).det() * g)
    trace_residual = sp.simplify(
        sp.trace((s * sp.eye(2) + M).inv())
        - 1 / (s + M_T[0, 0])
        + sp.diff(g, s) / g
    )
    r1, r9 = 1 / (s + 1), 1 / (s + 9)
    mean = (r1 + r9) / 2
    variance = ((r1 - mean) ** 2 + (r9 - mean) ** 2) / 2
    variance_residual = sp.simplify(-sp.diff(g, s) / g - g - variance / mean)
    require(jacobi_residual == trace_residual == variance_residual == 0, "Schur/Jacobi/variance identity failed")

    quadrature, error = variance_quadrature([1, 9], [sp.Rational(1, 2), sp.Rational(1, 2)])
    direct = math.sqrt(5.0) - 2.0
    require(abs(quadrature - direct) < 3.0e-11, "scalar quadrature disagrees with deleted singular value")
    return f"g=(s+5)/((s+1)(s+9)) quadrature={quadrature:.12f} direct={direct:.12f}"


def antiperiodic_lambdas(N):
    require(isinstance(N, int) and N >= 2, "canonical grid requires integer N>=2")
    q = 2.0 * math.pi * (np.arange(N, dtype=float) + 0.5) / N
    return np.array(
        [2.0 * sum(1.0 - math.cos(angle) for angle in angles) for angles in product(q, repeat=3)],
        dtype=float,
    )


def energy_delta_from_moments(lambdas):
    def integrand(s):
        values = 1.0 / (s + lambdas)
        return math.sqrt(s) * float(np.var(values)) / float(np.mean(values)) / math.pi

    return quad(integrand, 0.0, np.inf, epsabs=2.0e-11, epsrel=2.0e-11, limit=400)[0]


def overlap_scalars_from_moments(lambdas):
    g0 = float(np.mean(1.0 / lambdas))
    beta = float(np.mean(1.0 / np.sqrt(lambdas)) ** 2 / g0)
    alpha = 1.0 - beta

    def integrand(x):
        denominator = x * x + lambdas
        g = float(np.mean(1.0 / denominator))
        h2 = float(np.mean(np.sqrt(lambdas) / denominator**2))
        return 2.0 * h2 / g / math.pi

    L_value = -1.0 + quad(integrand, 0.0, np.inf, epsabs=2.0e-11, epsrel=2.0e-11, limit=400)[0]
    ell = L_value / 2.0 + alpha / 4.0
    return g0, alpha, L_value, ell


def spectrum_counts(lambdas):
    values, counts = np.unique(np.round(lambdas, 12), return_counts=True)
    return tuple((float(value), int(count)) for value, count in zip(values, counts))


def secular_deleted_delta(lambdas):
    """Deleted principal spectrum from local weights, without a lattice matrix."""
    values, counts = np.unique(np.round(lambdas, 12), return_counts=True)
    total = int(counts.sum())
    polynomial = np.poly1d([0.0])
    for index, value in enumerate(values):
        term = np.poly1d([1.0])
        for other, other_value in enumerate(values):
            if other != index:
                term *= np.poly1d([1.0, -other_value])
        polynomial += (counts[index] / total) * term
    roots = np.roots(polynomial) if len(values) > 1 else np.array([], dtype=float)
    require(np.max(np.abs(roots.imag), initial=0.0) < 2.0e-9, "secular deleted roots are not real")
    deleted_nuclear = sum(
        (int(count) - 1) * math.sqrt(float(value)) for value, count in zip(values, counts)
    ) + sum(math.sqrt(float(root.real)) for root in roots)
    post_trace = (total - 1) * float(np.mean(np.sqrt(lambdas)))
    return deleted_nuclear - post_trace


def check_canonical_integer_grids():
    expected_spectra = {
        2: ((6.0, 8),),
        3: ((3.0, 8), (6.0, 12), (9.0, 6), (12.0, 1)),
        4: (
            (round(6.0 - 3.0 * math.sqrt(2.0), 12), 8),
            (round(6.0 - math.sqrt(2.0), 12), 24),
            (round(6.0 + math.sqrt(2.0), 12), 24),
            (round(6.0 + 3.0 * math.sqrt(2.0), 12), 8),
        ),
    }
    expected_delta = {2: 0.0, 3: 0.054323624108, 4: 0.072903415447}
    expected_g0 = {2: 1.0 / 6.0, 3: 65.0 / 324.0, 4: 11.0 / 51.0}
    summaries = []
    for N in (2, 3, 4):
        lambdas = antiperiodic_lambdas(N)
        require(spectrum_counts(lambdas) == expected_spectra[N], f"antiperiodic spectrum mismatch N={N}")
        require(abs(float(np.mean(lambdas)) - 6.0) < TOL, f"mean lambda != 6 at N={N}")
        delta = energy_delta_from_moments(lambdas)
        secular_delta = secular_deleted_delta(lambdas)
        g0, alpha, L_value, ell = overlap_scalars_from_moments(lambdas)
        require(abs(delta - expected_delta[N]) < 4.0e-10, f"energy excess mismatch N={N}")
        require(abs(delta - secular_delta) < 4.0e-10, f"quadrature/secular deletion mismatch N={N}")
        require(abs(g0 - expected_g0[N]) < TOL, f"inverse moment mismatch N={N}")
        require(L_value >= -TOL and -TOL <= alpha <= 1.0 + TOL, f"overlap scalars out of range N={N}")
        require(ell <= 1.5 * g0 + TOL, f"Jensen leakage bound fails N={N}")
        shown_ell = 0.0 if abs(ell) < 5.0e-13 else ell
        summaries.append(f"L={2*N}:D={delta:.9f},ell={shown_ell:.9f}")
    return " ".join(summaries)


def wrap_angle(values):
    return (values + math.pi) % (2.0 * math.pi) - math.pi


CUBE_DENOMINATOR = 32


def check_continuum_constants_and_shells():
    for N in (2, 3, 4, 5):
        theta = math.pi if N % 2 == 0 else 0.0
        k = (2.0 * math.pi * np.arange(N) + theta) / (2.0 * N)
        transformed = np.sort(np.round(wrap_angle(2.0 * k - math.pi), 12))
        antiperiodic = np.sort(
            np.round(wrap_angle(2.0 * math.pi * (np.arange(N) + 0.5) / N), 12)
        )
        require(np.array_equal(transformed, antiperiodic), f"canonical twist map fails N={N}")

    q_symbol = sp.symbols("q", real=True)
    mean_cosine = sp.integrate(sp.cos(q_symbol), (q_symbol, -sp.pi, sp.pi)) / (2 * sp.pi)
    continuum_mean_lambda = sp.simplify(6 - 6 * mean_cosine)
    require(continuum_mean_lambda == 6, "continuum mean lambda is not 6")

    max_shell_ratio = 0.0
    for shell in range(9):
        radius = shell + 0.5
        explicit_count = 0
        values = [integer + 0.5 for integer in range(-shell - 1, shell + 1)]
        inner = shell - 0.5
        for point in product(values, repeat=3):
            norm = max(abs(value) for value in point)
            if norm <= radius and norm > inner:
                explicit_count += 1
        formula_count = 24 * shell * shell + 24 * shell + 8
        require(explicit_count == formula_count, f"half-grid shell count mismatch shell={shell}")
        ratio = formula_count / radius**2
        max_shell_ratio = max(max_shell_ratio, ratio)
        require(ratio <= 32.0 + TOL, f"shell ratio bound fails shell={shell}")

    grid_size, cutoff = sp.symbols("N delta", positive=True)
    spacing = 2 * sp.pi / grid_size
    shell_cost = sp.simplify(
        grid_size**-3 * 32 * sp.pi**2 / (4 * spacing**2)
    )
    near_origin_bound = sp.simplify(shell_cost * (cutoff / spacing + 1))
    require(shell_cost == 2 / grid_size, "normalized half-grid shell cost mismatch")
    require(
        near_origin_bound == cutoff / sp.pi + 2 / grid_size,
        "near-origin inverse-dispersion bound mismatch",
    )

    x, epsilon = sp.symbols("x epsilon", positive=True)
    kinetic_integral = sp.integrate(x**2 * epsilon / (x**2 + epsilon**2) ** 2, (x, 0, sp.oo))
    inverse_integral = sp.integrate(6 * epsilon / (x**2 + epsilon**2) ** 2, (x, 0, sp.oo))
    require(sp.simplify(kinetic_integral - sp.pi / 4) == 0, "Jensen kinetic integral constant mismatch")
    require(
        sp.simplify(inverse_integral - 3 * sp.pi / (2 * epsilon**2)) == 0,
        "Jensen inverse-moment constant mismatch",
    )
    g_symbol, alpha_symbol = sp.symbols("g alpha", nonnegative=True)
    leakage_upper_at_alpha_one = (3 * g_symbol - sp.Rational(1, 2)) / 2 + sp.Rational(1, 4)
    require(
        sp.simplify(leakage_upper_at_alpha_one - 3 * g_symbol / 2) == 0,
        "Jensen leakage coefficient mismatch",
    )
    range_variance_constant = sp.Rational(12**2, 4)
    inner_full_integrand_constant = sp.Rational(2, 1) / sp.pi
    tail_inner_constant = range_variance_constant * 13
    tail_full_constant = 2 * tail_inner_constant / sp.pi
    require(
        inner_full_integrand_constant == 2 / sp.pi
        and tail_inner_constant == 468
        and tail_full_constant == 936 / sp.pi,
        "DCT majorant constants mismatch",
    )

    y = sp.symbols("y", real=True)
    face_relaxation = 24 * sp.integrate(1 / (1 + y**2), (y, 0, 1))
    require(sp.simplify(face_relaxation - 6 * sp.pi) == 0, "cube surface relaxation constant mismatch")
    cube_green_bound = sp.simplify(face_relaxation / CUBE_DENOMINATOR)
    expected_cube_bound = 3 * sp.pi / 16
    require(sp.simplify(cube_green_bound - expected_cube_bound) == 0, "cube Green bound mismatch")
    fidelity_floor = sp.simplify(1 - sp.Rational(3, 2) * cube_green_bound)
    expected_floor = 1 - 9 * sp.pi / 32
    require(sp.simplify(fidelity_floor - expected_floor) == 0, "continuum fidelity floor mismatch")
    require(float(fidelity_floor) > 0.1164, "continuum fidelity floor is not positive")
    return (
        f"twist_N=2..5 ok shell_count<=32r^2 near_sum<=delta/pi+2/N "
        f"g_inf<={float(cube_green_bound):.9f} liminfF>={float(fidelity_floor):.9f}"
    )


CHECKS = (
    ("source_import_firewall", check_source_integrity),
    ("exact_fock_projection", check_exact_fock_projection),
    ("fixed_number_energy_trace", check_fixed_number_energy_and_trace_bounds),
    ("leakage_squared_overlap", check_leakage_and_squared_overlap),
    ("resolvent_scalar_quadrature", check_resolvent_and_scalar_quadrature),
    ("canonical_integer_grids", check_canonical_integer_grids),
    ("continuum_constants_shells", check_continuum_constants_and_shells),
)


def main():
    passed = 0
    failed = 0
    for name, function in CHECKS:
        try:
            detail = function()
        except Exception as error:
            failed += 1
            print(f"FAIL {name}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"PASS {name}: {detail}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
