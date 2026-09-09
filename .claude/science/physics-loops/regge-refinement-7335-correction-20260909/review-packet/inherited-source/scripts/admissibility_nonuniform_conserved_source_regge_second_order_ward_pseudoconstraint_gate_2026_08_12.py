#!/usr/bin/env python3
"""Nonuniform conserved-source Regge second-order Ward gate.

It constructs the period-three, transversely homogeneous reduction of the
actual 4D Kuhn complex, evaluates
the Regge-plus-deficit-square action and its exact first derivative, and solves
the stationary equations after fixing the flat metric moduli and the four
linear displacement directions.
"""

from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
import json
import os
from pathlib import Path
import subprocess
import sys

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge  # noqa: E402
import admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10 as block20  # noqa: E402


AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_"
    "PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
BLOCK54_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CURVED_REGGE_PSEUDOCONSTRAINT_PERFECT_ACTION_ROUTE_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_NONUNIFORM_CONSERVED_SOURCE_REGGE_SECOND_ORDER_WARD_PSEUDOCONSTRAINT_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_CURVED_REGGE_PSEUDOCONSTRAINT_PERFECT_ACTION_ROUTE_GATE_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_fixed_metric_nonlinear_regge_kkt_continuation_2026_08_10.py",
    "scripts/admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py",
    "scripts/frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py",
)


L = 3
ALPHA = float(os.environ.get("TOE_ALPHA", str(1.0 / 1024.0)))
K = 2.0 * np.pi / L
SOURCE_KIND = os.environ.get("TOE_SOURCE", "static")
AXIS = 0 if SOURCE_KIND == "static" else 1
MOMENTUM = np.zeros(4)
MOMENTUM[AXIS] = K


def edge_ref(left, right):
    cls, anchor = regge.edge_class(tuple(left), tuple(right))
    return int(anchor[AXIS]), cls


HINGES = []
TRIANGLE_TYPES = ((1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4))
for triangle in regge.TRI_CLASSES:
    triangle_vertices = [np.asarray(vertex, dtype=int) for vertex in triangle]
    triangle_type = tuple(
        sorted(
            int(np.dot(triangle_vertices[i] - triangle_vertices[j], triangle_vertices[i] - triangle_vertices[j]))
            for i, j in ((0, 1), (0, 2), (1, 2))
        )
    )
    area_refs = tuple(
        edge_ref(triangle_vertices[i], triangle_vertices[j])
        for i, j in ((0, 1), (0, 2), (1, 2))
    )
    stars = []
    for simplex in regge.STARS[triangle]:
        local = {vertex: index for index, vertex in enumerate(simplex)}
        hinge = sorted(local[vertex] for vertex in triangle)
        missing = tuple(sorted(index for index in range(5) if index not in hinge))
        vertices = [np.asarray(vertex, dtype=int) for vertex in simplex]
        refs = tuple(edge_ref(vertices[i], vertices[j]) for i, j in regge.PAIRS5)
        stars.append((missing, refs))
    HINGES.append((triangle_type, area_refs, tuple(stars)))
HINGES = tuple(HINGES)


FLAT_LENGTHS = np.sqrt(np.asarray([sum(direction) for direction in regge.DIRS15]))


def get_length(lengths, base, reference):
    shift, cls = reference
    return lengths[(base + shift) % L, cls]


def action_gradient(lengths, beta=0.0, alpha_weights=None):
    lengths = np.asarray(lengths)
    dtype = np.result_type(lengths.dtype, np.float64)
    total = np.asarray(0.0, dtype=dtype)
    gradient = np.zeros((L, 15), dtype=dtype)
    deficits = []
    for base in range(L):
        for triangle_type, area_refs, stars in HINGES:
            alpha = ALPHA if alpha_weights is None else alpha_weights[TRIANGLE_TYPES.index(triangle_type)]
            area_lengths = np.asarray(
                [get_length(lengths, base, reference) for reference in area_refs]
            )
            area_out = np.asarray(regge.AREA(*(area_lengths * area_lengths)))
            area = area_out[0]
            area_derivatives = 2.0 * area_lengths * area_out[1:]

            deficit = np.asarray(2.0 * np.pi, dtype=dtype)
            deficit_derivatives = np.zeros((L, 15), dtype=dtype)
            for missing, refs in stars:
                simplex_lengths = np.asarray(
                    [get_length(lengths, base, reference) for reference in refs]
                )
                angle_out = np.asarray(regge.THETA[missing](*(simplex_lengths * simplex_lengths)))
                deficit -= angle_out[0]
                derivatives = -2.0 * simplex_lengths * angle_out[1:]
                for reference, derivative in zip(refs, derivatives):
                    shift, cls = reference
                    deficit_derivatives[(base + shift) % L, cls] += derivative

            deficits.append(deficit)
            weight = deficit + alpha * deficit * deficit + beta * deficit**3
            total += area * weight
            for reference, derivative in zip(area_refs, area_derivatives):
                shift, cls = reference
                gradient[(base + shift) % L, cls] += derivative * weight
            gradient += area * (
                1.0 + 2.0 * alpha * deficit + 3.0 * beta * deficit**2
            ) * deficit_derivatives
    return total, gradient, np.asarray(deficits)


def parameterization():
    metric_zero = regge.metric_map(np.zeros(4)).real
    normal_zero = null_space(metric_zero.T)
    momentum = MOMENTUM
    gauge = regge.gauge_map(momentum)
    physical = null_space(gauge.conj().T)
    matrix = np.zeros((L * 15, 27))
    gauge_matrix = np.zeros((L * 15, 8))
    for site in range(L):
        rows = slice(15 * site, 15 * (site + 1))
        matrix[rows, :5] = normal_zero
        phase_physical = np.exp(1j * K * site) * physical
        matrix[rows, 5:16] = 2.0 * phase_physical.real
        matrix[rows, 16:27] = -2.0 * phase_physical.imag
        phase_gauge = np.exp(1j * K * site) * gauge
        gauge_matrix[rows, :4] = 2.0 * phase_gauge.real
        gauge_matrix[rows, 4:8] = -2.0 * phase_gauge.imag
    return matrix, gauge_matrix, metric_zero, normal_zero, gauge, physical


B, BG, M0, N0, GAUGE, PHYSICAL = parameterization()


def source_field():
    momentum = MOMENTUM
    metric = regge.metric_map(momentum)
    target = np.zeros(10, dtype=complex)
    if SOURCE_KIND == "static":
        target[3] = 1.0  # h_tt, with tick coordinate last
    else:
        target[0] = 1.0
        target[3] = 1.0
        target[6] = 2.0  # 2 T_xt h_xt for the null t+x Record bundle
    source = metric @ np.linalg.solve(metric.conj().T @ metric, target)
    field = np.asarray(
        [2.0 * np.real(np.exp(1j * K * site) * source) for site in range(L)]
    )
    return source, field


SOURCE_K, SOURCE = source_field()


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, key, statement, condition, detail=""):
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 150 else detail[:147] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat_text(path):
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def source_target():
    target = np.zeros(10, dtype=complex)
    if SOURCE_KIND == "static":
        target[3] = 1.0
    else:
        target[0] = 1.0
        target[3] = 1.0
        target[6] = 2.0
    return target


def lengths_from_coordinates(coordinates):
    delta = (B @ np.asarray(coordinates)).reshape(L, 15)
    return FLAT_LENGTHS[None, :] + delta


def source_gradient(lengths, power):
    return SOURCE * (lengths / FLAT_LENGTHS[None, :]) ** (power - 1.0)


def equations(coordinates, coupling, power=1.0, beta=0.0):
    lengths = lengths_from_coordinates(coordinates)
    _action, gradient, _deficits = action_gradient(lengths, beta)
    residual = gradient - coupling * source_gradient(lengths, power)
    return B.T @ residual.reshape(-1)


def full_equations(coordinates, coupling, power=1.0, beta=0.0):
    physical = coordinates[:27]
    gauge = coordinates[27:]
    delta = B @ physical + BG @ gauge
    lengths = FLAT_LENGTHS[None, :] + delta.reshape(L, 15)
    _action, gradient, _deficits = action_gradient(lengths, beta)
    residual = gradient - coupling * source_gradient(lengths, power)
    flat = residual.reshape(-1)
    return np.concatenate((B.T @ flat, BG.T @ flat))


def numerical_jacobian(function, point, step=2.0e-6):
    point = np.asarray(point, dtype=float)
    matrix = np.zeros((len(point), len(point)))
    for column in range(len(point)):
        plus = point.copy()
        minus = point.copy()
        plus[column] += step
        minus[column] -= step
        matrix[:, column] = (function(plus) - function(minus)) / (2.0 * step)
    return 0.5 * (matrix + matrix.T)


def flat_bloch(momentum, alpha_weights=None):
    matrix = np.zeros((15, 15), dtype=complex)
    correction = np.zeros((15, 15), dtype=complex)
    for triangle in regge.TRI_CLASSES:
        area_row, deficit_row, _deficit = regge.tri_rows(triangle, momentum)
        matrix += 0.5 * (
            np.outer(np.conj(area_row), deficit_row)
            + np.outer(np.conj(deficit_row), area_row)
        )
        vertices = [np.asarray(vertex, dtype=float) for vertex in triangle]
        squared = [
            float(np.dot(vertices[i] - vertices[j], vertices[i] - vertices[j]))
            for i, j in ((0, 1), (0, 2), (1, 2))
        ]
        area = float(regge.AREA(*squared)[0])
        triangle_type = tuple(sorted(int(value) for value in squared))
        alpha = ALPHA if alpha_weights is None else alpha_weights[TRIANGLE_TYPES.index(triangle_type)]
        correction += 2.0 * alpha * area * np.outer(np.conj(deficit_row), deficit_row)
    return matrix + correction


def flat_real_hessian(alpha_weights=None):
    momenta = [2.0 * np.pi * index / L for index in range(L)]
    vectors = []
    for momentum in momenta:
        vector = np.zeros(4)
        vector[AXIS] = momentum
        vectors.append(vector)
    symbols = [flat_bloch(vector, alpha_weights) for vector in vectors]
    hessian = np.zeros((L * 15, L * 15), dtype=float)
    for left in range(L):
        for right in range(L):
            block = sum(
                np.exp(1j * momentum * (left - right)) * symbol
                for momentum, symbol in zip(momenta, symbols)
            ) / L
            hessian[
                15 * left : 15 * (left + 1),
                15 * right : 15 * (right + 1),
            ] = np.real_if_close(block, tol=1000).real
    return 0.5 * (hessian + hessian.T)


def forward_jacobian(function, point, step):
    point = np.asarray(point, dtype=float)
    center = function(point)
    matrix = np.zeros((len(center), len(point)))
    for column in range(len(point)):
        shifted = point.copy()
        shifted[column] += step
        matrix[:, column] = (function(shifted) - center) / step
    return matrix


def gauge_newton_jacobian(function, point, physical_hessian, step):
    center = function(point)
    matrix = np.zeros((35, 35))
    matrix[:27, :27] = physical_hessian
    for column in range(8):
        shifted = point.copy()
        shifted[27 + column] += step
        matrix[:, 27 + column] = (function(shifted) - center) / step
    matrix[27:, :27] = matrix[:27, 27:].T
    matrix[27:, 27:] = 0.5 * (matrix[27:, 27:] + matrix[27:, 27:].T)
    return matrix


def fourier(field):
    return sum(
        np.exp(-1j * K * site) * field[site] for site in range(L)
    ) / L


def solve_projected(coupling, flat_jacobian, linear, power=1.0, beta=0.0, start=None):
    coordinates = coupling * linear if start is None else np.asarray(start).copy()
    for _iteration in range(10):
        residual = equations(coordinates, coupling, power, beta)
        if np.linalg.norm(residual) < 5.0e-12:
            break
        coordinates += np.linalg.solve(flat_jacobian, -residual)
    return coordinates


def internal_analysis():
    flat_lengths = np.tile(FLAT_LENGTHS, (L, 1))
    flat_action, flat_gradient, flat_deficits = action_gradient(flat_lengths)
    real_hessian = flat_real_hessian()
    flat_jacobian = B.T @ real_hessian @ B
    flat_values = np.linalg.eigvalsh(flat_jacobian)
    source_coordinates = B.T @ SOURCE.reshape(-1)
    linear = np.linalg.solve(flat_jacobian, source_coordinates)

    probe = np.linspace(-1.0, 1.0, 27)
    probe_step = 2.0e-6
    directional = (
        equations(probe_step * probe, 0.0)
        - equations(-probe_step * probe, 0.0)
    ) / (2.0 * probe_step)
    directional_relative = float(
        np.linalg.norm(directional - flat_jacobian @ probe)
        / np.linalg.norm(flat_jacobian @ probe)
    )

    rng = np.random.default_rng(580 if SOURCE_KIND == "static" else 581)
    delta = rng.normal(size=(L, 15))
    delta *= 2.0e-4 / np.linalg.norm(delta)
    perturbed = flat_lengths + delta
    reduced_action, reduced_gradient, _deficits = action_gradient(perturbed)

    def epsilon(edge_class, anchor):
        return float(delta[int(anchor[AXIS]) % L, edge_class])

    independent_action = (
        regge.box_action(L, epsilon)
        + ALPHA * block20.box_curvature_square(L, epsilon)
    ) / L**3
    action_relative = float(
        abs(float(reduced_action) - independent_action)
        / max(abs(independent_action), 1.0e-14)
    )
    gradient_indices = (0, 7, 22, 44)
    gradient_step = 1.0e-5
    numerical_gradient = []
    for index in gradient_indices:
        plus = perturbed.copy().reshape(-1)
        minus = perturbed.copy().reshape(-1)
        plus[index] += gradient_step
        minus[index] -= gradient_step
        plus_action = action_gradient(plus.reshape(L, 15))[0]
        minus_action = action_gradient(minus.reshape(L, 15))[0]
        numerical_gradient.append((plus_action - minus_action) / (2.0 * gradient_step))
    analytic_gradient = reduced_gradient.reshape(-1)[list(gradient_indices)]
    gradient_relative = float(
        np.linalg.norm(np.asarray(numerical_gradient) - analytic_gradient)
        / max(np.linalg.norm(analytic_gradient), 1.0e-14)
    )

    couplings = (1.0e-5, 2.0e-5, 5.0e-5, 1.0e-4, 2.0e-4, 5.0e-4, 1.0e-3)
    branches = []
    solutions = {}
    previous = None
    previous_coupling = None
    metric_map = regge.metric_map(MOMENTUM)
    for coupling in couplings:
        start = None
        if previous is not None:
            start = previous * (coupling / previous_coupling)
        coordinates = solve_projected(
            coupling, flat_jacobian, linear, start=start
        )
        lengths = lengths_from_coordinates(coordinates)
        _action, gradient, deficits = action_gradient(lengths)
        residual = gradient - coupling * SOURCE
        residual_k = fourier(residual)
        response_k = fourier(lengths - FLAT_LENGTHS[None, :])
        metric_fit = metric_map @ np.linalg.lstsq(
            metric_map, response_k, rcond=None
        )[0]
        nonmetric = float(np.linalg.norm(response_k - metric_fit))
        branches.append(
            {
                "coupling": coupling,
                "projected": float(np.linalg.norm(B.T @ residual.reshape(-1))),
                "gauge": float(np.linalg.norm(GAUGE.conj().T @ residual_k)),
                "gauge_over_c2": float(
                    np.linalg.norm(GAUGE.conj().T @ residual_k) / coupling**2
                ),
                "deficit": float(np.max(np.abs(deficits))),
                "metric": float(np.linalg.norm(metric_fit)),
                "nonmetric": nonmetric,
                "minimum_length": float(np.min(lengths)),
            }
        )
        solutions[coupling] = coordinates
        previous = coordinates
        previous_coupling = coupling

    central_step = 1.0e-4
    _action, plus_gradient, _deficits = action_gradient(
        lengths_from_coordinates(central_step * linear)
    )
    _action, minus_gradient, _deficits = action_gradient(
        lengths_from_coordinates(-central_step * linear)
    )
    leading_vector = BG.T @ (
        plus_gradient + minus_gradient - 2.0 * flat_gradient
    ).reshape(-1) / (2.0 * central_step**2)

    seagull_vectors = []
    seagull_coupling = 1.0e-4
    for power in (1.0, 2.0):
        coordinates = solve_projected(
            seagull_coupling, flat_jacobian, linear, power=power
        )
        lengths = lengths_from_coordinates(coordinates)
        _action, gradient, _deficits = action_gradient(lengths)
        residual = gradient - seagull_coupling * source_gradient(lengths, power)
        seagull_vectors.append(
            BG.T @ residual.reshape(-1) / seagull_coupling**2
        )
    seagull_direction = seagull_vectors[1] - seagull_vectors[0]
    seagull_scalar = -float(seagull_direction @ seagull_vectors[0]) / float(
        seagull_direction @ seagull_direction
    )
    seagull_best = seagull_vectors[0] + seagull_scalar * seagull_direction

    cubic_ratios = []
    for coupling in (1.0e-3, 5.0e-4, 2.5e-4):
        lengths = lengths_from_coordinates(coupling * linear)
        _action, gradient_zero, _deficits = action_gradient(lengths, beta=0.0)
        _action, gradient_one, _deficits = action_gradient(lengths, beta=1.0)
        cubic_ratios.append(
            float(
                np.linalg.norm(BG.T @ (gradient_one - gradient_zero).reshape(-1))
                / coupling**2
            )
        )

    pseudo_spectra = []
    for coupling in (5.0e-4, 1.0e-3):
        complete = np.concatenate((solutions[coupling], np.zeros(8)))
        jacobian = numerical_jacobian(
            lambda point: full_equations(point, coupling), complete, step=1.0e-6
        )
        jpp = jacobian[:27, :27]
        jpg = jacobian[:27, 27:]
        jgp = jacobian[27:, :27]
        jgg = jacobian[27:, 27:]
        schur = jgg - jgp @ np.linalg.solve(jpp, jpg)
        spectrum = np.linalg.eigvalsh(0.5 * (schur + schur.T))
        pseudo_spectra.append(
            {
                "coupling": coupling,
                "rank": int(np.sum(np.abs(spectrum) > 1.0e-6)),
                "eigenvalues": spectrum.tolist(),
            }
        )

    target_error = float(
        np.linalg.norm(regge.metric_map(MOMENTUM).conj().T @ SOURCE_K - source_target())
    )
    return {
        "kind": SOURCE_KIND,
        "axis": AXIS,
        "hinges": len(HINGES),
        "stars": sum(len(stars) for _kind, _refs, stars in HINGES),
        "parameter_rank": int(np.linalg.matrix_rank(B)),
        "flat_action": float(flat_action),
        "flat_gradient": float(np.max(np.abs(flat_gradient))),
        "flat_deficit": float(np.max(np.abs(flat_deficits))),
        "flat_inertia": [
            int(np.sum(flat_values < -1.0e-7)),
            int(np.sum(flat_values > 1.0e-7)),
            int(np.sum(np.abs(flat_values) <= 1.0e-7)),
        ],
        "flat_gap": float(np.min(np.abs(flat_values))),
        "hessian_directional_relative": directional_relative,
        "independent_action": float(independent_action),
        "reduced_action": float(reduced_action),
        "action_relative": action_relative,
        "gradient_relative": gradient_relative,
        "source_target_error": target_error,
        "source_ward": float(np.linalg.norm(GAUGE.conj().T @ SOURCE_K)),
        "source_mean": float(np.linalg.norm(SOURCE.sum(axis=0))),
        "branches": branches,
        "leading_vector": leading_vector.tolist(),
        "leading_norm": float(np.linalg.norm(leading_vector)),
        "seagull_power_norms": [
            float(np.linalg.norm(vector)) for vector in seagull_vectors
        ],
        "seagull_scalar": seagull_scalar,
        "seagull_fraction": float(
            np.linalg.norm(seagull_best) / np.linalg.norm(seagull_vectors[0])
        ),
        "cubic_ratios": cubic_ratios,
        "pseudo_spectra": pseudo_spectra,
    }


def affine_kkt_diagnostic():
    metric_zero = regge.metric_map(np.zeros(4)).real
    normal_zero = null_space(metric_zero.T)
    momentum = np.asarray((0.73, -0.41, 0.29, 0.17))
    gauge = regge.gauge_map(momentum)
    hessian = flat_bloch(momentum)
    bordered = np.block(
        [
            [hessian, metric_zero],
            [metric_zero.T, np.zeros((10, 10))],
        ]
    )
    return {
        "metric_rank": int(np.linalg.matrix_rank(metric_zero)),
        "normal_rank": int(np.linalg.matrix_rank(normal_zero)),
        "normal_metric_residual": float(np.linalg.norm(metric_zero.T @ normal_zero)),
        "constraint_gauge_rank": int(np.linalg.matrix_rank(metric_zero.T @ gauge)),
        "bordered_rank": int(np.linalg.matrix_rank(bordered)),
    }


def child_result(kind):
    environment = os.environ.copy()
    environment["TOE_SOURCE"] = kind
    process = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--internal"],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
        check=False,
    )
    if process.returncode != 0:
        raise RuntimeError(
            f"{kind} child failed with {process.returncode}: {process.stderr[-1000:]}"
        )
    return json.loads(process.stdout.strip().splitlines()[-1])


def main():
    checks = Checks()
    note = flat_text(NOTE_PATH)
    block54_note = flat_text(BLOCK54_NOTE_PATH)
    mutation = os.environ.get("TOE_MUTATION", "")
    affine = affine_kkt_diagnostic()
    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = {
            kind: executor.submit(child_result, kind) for kind in ("static", "null")
        }
        results = {kind: future.result() for kind, future in futures.items()}

    print("analytic_boundary: period-three transversely homogeneous full-edge Regge plus deficit-square action at alpha=1/1024")
    print("physical_boundary: the static source is Euclidean; the null Record bundle has only a conditional Lorentzian interpretation")
    print("progress_boundary: a decisive fixed-law route rejection is blocker burn-down, not TOE percentage movement")

    checks.check(
        "affine-surrogate-correction",
        "the prior affine KKT continuation freezes all ten metric tangents and all four displacement columns",
        affine["metric_rank"] == 10
        and affine["normal_rank"] == 5
        and affine["normal_metric_residual"] < 1.0e-12
        and affine["constraint_gauge_rank"] == 4
        and affine["bordered_rank"] == 25
        and mutation != "affine_rank"
        and "linear source and affine reaction terms have identically zero length-length hessians" in block54_note,
        f"metric/normal ranks={affine['metric_rank']}/{affine['normal_rank']}; M0^T Gamma rank={affine['constraint_gauge_rank']}; KKT rank={affine['bordered_rank']}",
    )

    checks.check(
        "independent-reduced-action",
        "the reduced action and derivative agree with the original periodic box action and central differences",
        all(
            result["hinges"] == 50
            and result["stars"] == 240
            and result["parameter_rank"] == 27
            and result["action_relative"] < 1.0e-8
            and result["gradient_relative"] < 1.0e-5
            and result["hessian_directional_relative"] < 2.0e-6
            and result["flat_inertia"] == [22, 5, 0]
            for result in results.values()
        ),
        "; ".join(
            f"{kind}: action={value['action_relative']:.2e}, gradient={value['gradient_relative']:.2e}, Hessian={value['hessian_directional_relative']:.2e}"
            for kind, value in results.items()
        ),
    )

    checks.check(
        "conserved-zero-total-sources",
        "both named Fourier sources realize their metric targets, have zero mean, and annihilate the flat gauge columns",
        all(
            result["source_target_error"] < 1.0e-11
            and result["source_ward"] < 1.0e-11
            and result["source_mean"] < 1.0e-11
            for result in results.values()
        ),
        "; ".join(
            f"{kind}: target={value['source_target_error']:.2e}, Ward={value['source_ward']:.2e}, mean={value['source_mean']:.2e}"
            for kind, value in results.items()
        ),
    )

    branch_condition = True
    branch_details = []
    for kind, result in results.items():
        last = result["branches"][-1]
        branch_condition &= (
            max(record["projected"] for record in result["branches"]) < 1.0e-9
            and last["deficit"] > 1.0e-4
            and last["metric"] > 2.0 * last["nonmetric"]
            and last["minimum_length"] > 0.9
        )
        branch_details.append(
            f"{kind}: proj={last['projected']:.2e}, deficit={last['deficit']:.3e}, metric/nonmetric={last['metric']/last['nonmetric']:.2f}"
        )
    checks.check(
        "genuine-nonuniform-full-edge-branches",
        "both conserved sources solve every nongauge equation with nonzero curvature and metric-dominated response",
        branch_condition,
        "; ".join(branch_details),
    )

    ward_condition = mutation != "ward_order"
    ward_details = []
    for kind, result in results.items():
        ratios = [record["gauge_over_c2"] for record in result["branches"][:4]]
        ward_condition &= min(ratios) > 1.0 and max(ratios) / min(ratios) < 1.02
        ward_condition &= result["leading_norm"] > 10.0
        ward_details.append(
            f"{kind}: ||W2||={result['leading_norm']:.6f}, gauge/c^2={ratios[0]:.6f}..{ratios[-1]:.6f}"
        )
    checks.check(
        "second-order-ward-obstruction",
        "a nonzero gauge residual stabilizes at order c squared for both named genuine metric sources",
        ward_condition,
        "; ".join(ward_details),
    )

    pseudo_condition = True
    pseudo_details = []
    for kind, result in results.items():
        spectra = result["pseudo_spectra"]
        extrema = []
        for record in spectra:
            values = np.asarray(record["eigenvalues"])
            pseudo_condition &= record["rank"] == 8 and values[0] < 0.0 < values[-1]
            extrema.append(float(np.max(np.abs(values))))
        pseudo_condition &= 1.5 < extrema[1] / extrema[0] < 2.6
        pseudo_details.append(
            f"{kind}: ranks={[record['rank'] for record in spectra]}, extrema={extrema[0]:.3e}/{extrema[1]:.3e}"
        )
    checks.check(
        "eight-pseudoconstraint-directions",
        "all eight real displacement directions lift into soft mixed-sign Schur modes on both branches",
        pseudo_condition,
        "; ".join(pseudo_details),
    )

    checks.check(
        "scalar-source-seagull-rejected",
        "the full one-parameter interval-power source family cannot cancel the leading Ward vectors",
        results["static"]["seagull_fraction"] > 0.90
        and results["null"]["seagull_fraction"] > 0.60,
        f"optimized residual fractions: static={results['static']['seagull_fraction']:.6f}, null={results['null']['seagull_fraction']:.6f}",
    )

    cubic_condition = True
    cubic_details = []
    for kind, result in results.items():
        values = result["cubic_ratios"]
        quotients = (values[1] / values[0], values[2] / values[1])
        cubic_condition &= all(0.40 < quotient < 0.60 for quotient in quotients)
        cubic_details.append(
            f"{kind}: beta influence/c^2={values[0]:.6f},{values[1]:.6f},{values[2]:.6f}"
        )
    checks.check(
        "cubic-deficit-order-mismatch",
        "a fixed finite sum A epsilon cubed coefficient enters one order after the leading Ward obstruction",
        cubic_condition,
        "; ".join(cubic_details),
    )

    checks.check(
        "scope-strategy-and-no-go-packet",
        "the source note carries N1 through N8, preserves live completions, and records zero lane movement",
        mutation != "note_boundary"
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "dynamical record/matter source" in note
        and "improved/perfect" in note
        and "pachner" in note
        and "not a gravity no-go" in note
        and "zero toe percentage points" in note
        and "no axiom is amended" in note,
    )

    print("N5_CERTIFICATE: two conserved sources, 45 full-edge variables, 27 fixed-gauge coordinates, eight gauge coordinates, and three explicit repair families were resolved")
    print("per_element: checked all 45 period-three edge lengths, 27 nongauge coordinates, and eight real displacement coordinates")
    print("per_site: checked all 50 hinge classes and 240 simplex-hinge incidences in each reduced slice against the independent periodic box action")
    print("per_mode: checked k=2pi/3 for a static density mode and a conditional Lorentzian null Record-bundle mode, including c-to-zero order tests")
    print("per_block: corrected the Block-19/21/54 affine surrogate, solved the genuine full-edge branch, and tested scalar-seagull, cubic-deficit, and pseudo-constraint responses")
    print("lattice_wide: not executed; full-Z3, continuous-zone, nonlinear Lorentzian evolution, and refinement/projective consistency remain open")
    print("scope_boundary: bounded fixed-action route decision; not a gravity no-go, nonlinear TOE closure, axiom amendment, or TOE score movement")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    if "--internal" in sys.argv:
        print(json.dumps(internal_analysis(), separators=(",", ":")))
    else:
        raise SystemExit(main())
