#!/usr/bin/env python3
"""Block 186: common-metric pullback, torus, and constraint boundary.

The runner tests the hard line-metric restriction of the supplied reflected
edge action.  It verifies its exact Ward/source/curvature identities and
Einstein infrared limit, then executes three early kills: generic off-axis
transverse-trace-visible poles, the axial conformal block, and inequivalent
ranks at equivalent Brillouin-torus representatives.  It also preserves the
strongest positive control, a two-TT interior atlas.

The bounded failures apply only to this line-map pullback as a global
full-source lattice covariance.  They are not a gravity no-go.
"""

from __future__ import annotations

import itertools
import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import brentq


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14 as block74  # noqa: E402
import admissibility_reflected_curvature_gravity_physical_reconstruction_cut_gate_boundary_2026_08_14 as block76  # noqa: E402
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402


block48 = block74.block48
block49 = block74.block49
MU = 1.0 / 1024.0
RCOND = 1.0e-12
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_COMMON_METRIC_PULLBACK_TORUS_"
    "CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_MOMENTUM_SOURCE_QUOTIENT_SIGN_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
INCIDENCE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_COMMON_METRIC_PULLBACK_TORUS_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_MOMENTUM_SOURCE_QUOTIENT_SIGN_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_reflected_curvature_common_metric_pullback_torus_constraint_boundary_2026_08_24.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_reflected_curvature_gravity_physical_reconstruction_cut_gate_boundary_2026_08_14.py",
)
MUTATIONS = (
    "factorization_input",
    "infrared_input",
    "off_axis_input",
    "axial_input",
    "torus_input",
    "tt_input",
    "note_boundary",
)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 180 else detail[:177] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def hermitian(matrix: np.ndarray) -> np.ndarray:
    return 0.5 * (matrix + matrix.conj().T)


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(hermitian(matrix))
    scale = max(1.0, float(np.max(np.abs(values))))
    cutoff = tolerance * scale
    return (
        int(np.sum(values < -cutoff)),
        int(np.sum(values > cutoff)),
        int(np.sum(np.abs(values) <= cutoff)),
    )


def metric_gauge(momentum: np.ndarray, mutation: str = "") -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    if mutation == "factorization_input":
        q = 2.0 * np.sin(q / 2.0)
    result = np.zeros((len(block48.HCOMPS), 4), dtype=complex)
    for row, (left, right) in enumerate(block48.HCOMPS):
        for column in range(4):
            result[row, column] = 1.0j * (
                q[left] * int(right == column)
                + q[right] * int(left == column)
            )
    return result


def fiber(union, momentum: np.ndarray, mu: float = MU, mutation: str = ""):
    q_real = np.asarray(momentum, dtype=float)
    q = q_real.astype(complex)
    metric = block49.union_line_metric_map(union, q)
    gauge = metric_gauge(q_real, mutation)
    edge = -block74.cross_action_symbol(union, q, mu)
    kernel = metric.conj().T @ edge @ metric
    quotient = null_space(gauge.conj().T, rcond=RCOND)
    reduced = hermitian(quotient.conj().T @ kernel @ quotient)
    return metric, gauge, edge, kernel, quotient, reduced


def transverse_trace_source(momentum: np.ndarray) -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    projector = np.eye(4) - np.outer(q, q) / float(q @ q)
    return np.asarray(
        [
            projector[left, right] * (2.0 if left != right else 1.0)
            for left, right in block48.HCOMPS
        ],
        dtype=complex,
    )


def bordered_response(union, momentum: np.ndarray, source: np.ndarray) -> float:
    _, gauge, _, kernel, _, _ = fiber(union, momentum)
    border = np.block(
        [[kernel, gauge], [gauge.conj().T, np.zeros((4, 4), dtype=complex)]]
    )
    solution = np.linalg.solve(
        border, np.concatenate((source, np.zeros(4, dtype=complex)))
    )[: len(block48.HCOMPS)]
    return float(np.vdot(source, solution).real)


def regular_data(union, mutation: str) -> dict[str, object]:
    q = np.asarray((0.31, -0.47, 0.23, 0.19), dtype=float)
    metric, gauge, edge, kernel, _, _ = fiber(union, q, mutation=mutation)
    edge_gauge = block48.union_gauge_map(union, q.astype(complex))
    curvature = block49.centered_curvature_intertwiner(union, q.astype(complex))
    expected = block49.expected_centered_metric_rows(q.astype(complex))
    source = transverse_trace_source(q)
    representative = metric @ np.linalg.solve(metric.conj().T @ metric, source)
    return {
        "ranks": (
            int(np.linalg.matrix_rank(metric, tol=1.0e-11)),
            int(np.linalg.matrix_rank(gauge, tol=1.0e-11)),
        ),
        "factor": float(np.linalg.norm(metric @ gauge - edge_gauge)),
        "edge_ward": float(np.linalg.norm(edge @ edge_gauge)),
        "metric_ward": float(np.linalg.norm(kernel @ gauge)),
        "curvature": float(np.linalg.norm(curvature @ metric - expected)),
        "source_pullback": float(
            np.linalg.norm(metric.conj().T @ representative - source)
        ),
        "edge_source_ward": float(
            np.linalg.norm(edge_gauge.conj().T @ representative)
        ),
        "metric_source_ward": float(np.linalg.norm(gauge.conj().T @ source)),
    }


def infrared_errors(union, mutation: str) -> tuple[float, ...]:
    direction = np.asarray((0.31, -0.47, 0.23, 0.19), dtype=float)
    direction /= np.linalg.norm(direction)
    comparator = 0.5 * block44.einstein_action_pairing(direction, np.eye(4))
    if mutation == "infrared_input":
        comparator *= 1.01
    errors = []
    for epsilon in (1.0e-2, 5.0e-3, 2.5e-3):
        q = epsilon * direction
        metric, _, edge, _, _, _ = fiber(union, q)
        kernel = hermitian(metric.conj().T @ edge @ metric) / epsilon**2
        errors.append(float(np.linalg.norm(kernel - comparator) / np.linalg.norm(comparator)))
    return tuple(errors)


def off_axis_data(union, mutation: str) -> dict[str, object]:
    shift = 0.12 if mutation == "off_axis_input" else 0.08

    def momentum(parameter: float) -> np.ndarray:
        return np.asarray((parameter, parameter - shift, parameter - 0.37, 0.13))

    def minimum(parameter: float, mu: float) -> float:
        return float(np.linalg.eigvalsh(fiber(union, momentum(parameter), mu)[-1])[0])

    brackets = ((2.84, 2.93), (3.05, 3.13))
    roots_by_mu = tuple(
        tuple(brentq(lambda value: minimum(value, mu), *bracket, xtol=1.0e-14) for bracket in brackets)
        for mu in (MU, 0.0, -MU)
    )
    roots = roots_by_mu[0]
    singular = []
    responses = []
    wards = []
    root_slopes = []
    root_gaps = []
    for root in roots:
        metric = fiber(union, momentum(root))[0]
        singular.append(float(np.linalg.svd(metric, compute_uv=False)[-1]))
        root_values = np.linalg.eigvalsh(fiber(union, momentum(root))[-1])
        root_gaps.append(float(root_values[1]))
        step = 1.0e-6
        root_slopes.append(
            (
                minimum(root + step, MU)
                - minimum(root - step, MU)
            )
            / (2.0 * step)
        )
        pair = []
        for offset in (-1.0e-6, 1.0e-6):
            q = momentum(root + offset)
            source = transverse_trace_source(q)
            pair.append(bordered_response(union, q, source))
            wards.append(float(np.linalg.norm(metric_gauge(q).conj().T @ source)))
        responses.append(tuple(pair))

    generic_q = np.pi * np.asarray((1.0 / 5.0, -1.0 / 7.0, 2.0 / 9.0, 1.0 / 6.0))
    generic_metric, generic_gauge, _, _, generic_quotient, _ = fiber(union, generic_q)
    visible_edge = generic_metric @ generic_quotient
    curvature = block49.curvature_intertwiner(union, generic_q.astype(complex))
    curvature_kernel = null_space(curvature @ visible_edge, rcond=RCOND)
    curvature_forms = []
    for coefficient in (0.0, MU, -MU, 1.0e6):
        edge = -block74.cross_action_symbol(union, generic_q.astype(complex), coefficient)
        curvature_forms.append(
            hermitian(
                curvature_kernel.conj().T
                @ visible_edge.conj().T
                @ edge
                @ visible_edge
                @ curvature_kernel
            )
        )
    return {
        "roots": roots,
        "root_shifts": tuple(
            max(abs(roots_by_mu[index][slot] - roots[slot]) for index in (1, 2))
            for slot in (0, 1)
        ),
        "singular": tuple(singular),
        "root_slopes": tuple(root_slopes),
        "root_gaps": tuple(root_gaps),
        "responses": tuple(responses),
        "ward": max(wards),
        "inertias": tuple(inertia(fiber(union, momentum(value))[-1]) for value in (2.7, 2.9, 3.12)),
        "curvature_rank": int(np.linalg.matrix_rank(curvature @ visible_edge, tol=1.0e-10)),
        "curvature_null": float(np.linalg.norm(curvature @ visible_edge @ curvature_kernel)),
        "curvature_inertias": tuple(inertia(item) for item in curvature_forms),
        "curvature_independence": max(
            float(np.linalg.norm(item - curvature_forms[0]))
            for item in curvature_forms[1:]
        ),
        "curvature_eigenvalues": tuple(
            float(value) for value in np.linalg.eigvalsh(curvature_forms[0])
        ),
        "generic_metric_rank": int(np.linalg.matrix_rank(generic_metric, tol=1.0e-10)),
        "generic_gauge_rank": int(np.linalg.matrix_rank(generic_gauge, tol=1.0e-10)),
    }


def axial_data(union, mutation: str) -> dict[str, object]:
    index = {pair: slot for slot, pair in enumerate(block48.HCOMPS)}
    basis = np.zeros((len(block48.HCOMPS), 4), dtype=complex)
    basis[index[(1, 1)], 0] = 1.0 / np.sqrt(2.0)
    basis[index[(2, 2)], 0] = 1.0 / np.sqrt(2.0)
    basis[index[(3, 3)], 1] = 1.0
    basis[index[(1, 2)], 2] = 1.0
    basis[index[(1, 3)], 3] = 1.0 / np.sqrt(2.0)
    basis[index[(2, 3)], 3] = 1.0 / np.sqrt(2.0)
    k = 2.0 * np.pi / 72.0
    q = np.asarray((k, 0.0, 0.0, 0.03 if mutation == "axial_input" else 0.0))
    metric, gauge, _, kernel, _, reduced = fiber(union, q)
    block = hermitian(basis.conj().T @ kernel @ basis) / k**2
    source_temporal = np.zeros(len(block48.HCOMPS), dtype=complex)
    source_temporal[index[(3, 3)]] = 1.0
    source_trace = np.zeros(len(block48.HCOMPS), dtype=complex)
    for pair in ((1, 1), (2, 2), (3, 3)):
        source_trace[index[pair]] = 1.0
    comparator = np.asarray(
        [
            [-0.25, -1.0 / (2.0 * np.sqrt(2.0)), 0.0, 0.0],
            [-1.0 / (2.0 * np.sqrt(2.0)), 0.0, 0.0, 0.0],
            [0.0, 0.0, 0.5, 0.0],
            [0.0, 0.0, 0.0, 0.5],
        ]
    )
    return {
        "block_error": float(np.linalg.norm(block.real - comparator)),
        "scalar_determinant": float(np.linalg.det(block[:2, :2]).real),
        "inertia": inertia(reduced),
        "temporal_response": bordered_response(union, q, source_temporal),
        "trace_response": bordered_response(union, q, source_trace),
        "trace_ward": float(np.linalg.norm(gauge.conj().T @ source_trace)),
        "rank_metric": int(np.linalg.matrix_rank(metric, tol=1.0e-10)),
    }


def torus_data(union, mutation: str) -> dict[str, object]:
    q_a = np.asarray((np.pi, np.pi, np.pi, 0.0))
    q_b = np.asarray((-np.pi + (0.01 if mutation == "torus_input" else 0.0), np.pi, np.pi, 0.0))
    data = [fiber(union, q) for q in (q_a, q_b)]
    metrics = [item[0] for item in data]
    kernels = [item[3] for item in data]
    actions = [block74.cross_action_symbol(union, q.astype(complex), MU) for q in (q_a, q_b)]
    gauges = [block48.union_gauge_map(union, q.astype(complex)) for q in (q_a, q_b)]
    projectors = [metric @ np.linalg.pinv(metric, rcond=RCOND) for metric in metrics]
    rank_counts: dict[int, int] = {}
    for values in itertools.product((-np.pi, 0.0, np.pi), repeat=4):
        metric = block49.union_line_metric_map(union, np.asarray(values, dtype=complex))
        rank = int(np.linalg.matrix_rank(metric, tol=1.0e-10))
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    index = {pair: slot for slot, pair in enumerate(block48.HCOMPS)}
    pair_metric = block49.union_line_metric_map(
        union, np.asarray((np.pi, np.pi, 0.0, 0.0), dtype=complex)
    )
    h_xy = np.zeros(len(block48.HCOMPS), dtype=complex)
    h_xy[index[(0, 1)]] = 1.0
    return {
        "metric_ranks": tuple(int(np.linalg.matrix_rank(item, tol=1.0e-10)) for item in metrics),
        "kernel_ranks": tuple(int(np.linalg.matrix_rank(item, tol=1.0e-9)) for item in kernels),
        "inertias": tuple(inertia(item[-1]) for item in data),
        "action_match": float(np.linalg.norm(actions[0] - actions[1])),
        "gauge_match": float(np.linalg.norm(gauges[0] - gauges[1])),
        "projector_gap": float(np.linalg.norm(projectors[0] - projectors[1])),
        "rank_counts": rank_counts,
        "pair_rank": int(np.linalg.matrix_rank(pair_metric, tol=1.0e-10)),
        "pair_null": float(np.linalg.norm(pair_metric @ h_xy)),
    }


def tt_atlas_data(union, mutation: str) -> dict[str, object]:
    minimum = np.inf
    negatives = 0
    modes = 0
    for integer_mode in np.ndindex((7, 7, 7)):
        centered = np.asarray(integer_mode, dtype=int) - 3
        if np.all(centered == 0):
            continue
        spatial = centered * (2.0 * np.pi / 7.0)
        tensor = block76.SPATIAL_EMBEDDING @ block76.spatial_tt_basis(spatial)
        for temporal_mode in range(-3, 4):
            q = np.concatenate((spatial, (temporal_mode * 2.0 * np.pi / 7.0,)))
            metric, _, edge, _, _, _ = fiber(union, q)
            form = hermitian(tensor.conj().T @ metric.conj().T @ edge @ metric @ tensor)
            if mutation == "tt_input":
                form -= 0.1 * np.eye(2)
            values = np.linalg.eigvalsh(form)
            minimum = min(minimum, float(values[0]))
            negatives += int(values[0] < -1.0e-9)
            modes += 1
    corner = np.asarray((np.pi, np.pi, np.pi, 0.0))
    tensor = block76.SPATIAL_EMBEDDING @ block76.spatial_tt_basis(corner[:3])
    metric, _, edge, _, _, _ = fiber(union, corner)
    form = hermitian(tensor.conj().T @ metric.conj().T @ edge @ metric @ tensor)
    edge_gauge = block48.union_gauge_map(union, corner.astype(complex))
    gauge_projector = edge_gauge @ np.linalg.pinv(edge_gauge, rcond=RCOND)
    return {
        "modes": modes,
        "negatives": negatives,
        "minimum": minimum,
        "corner": tuple(float(value) for value in np.linalg.eigvalsh(form)),
        "corner_carrier_norm": float(np.linalg.norm(metric @ tensor)),
        "corner_gauge_distance": float(
            np.linalg.norm((np.eye(len(union.directions)) - gauge_projector) @ metric @ tensor)
        ),
    }


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    if mutation and mutation not in MUTATIONS:
        raise ValueError(f"unknown TOE_MUTATION={mutation!r}")
    checks = Checks()
    union = block48.build_reflection_union()

    regular = regular_data(union, mutation)
    checks.check(
        "exact-common-metric-ward-curvature-source-pullback",
        "the hard line-metric restriction exactly factors gauge, curvature, and conserved source pairing",
        len(union.directions) == 22
        and NOTE_PATH.exists()
        and AXIOM_PATH.exists()
        and PARENT_PATH.exists()
        and INCIDENCE_PATH.exists()
        and regular["ranks"] == (10, 4)
        and max(
            regular["factor"], regular["edge_ward"], regular["metric_ward"],
            regular["curvature"], regular["source_pullback"],
            regular["edge_source_ward"], regular["metric_source_ward"],
        ) < 5.0e-11,
        f"ranks={regular['ranks']}; MΓ-G={regular['factor']:.2e}; OG={regular['edge_ward']:.2e}; DM-FR={regular['curvature']:.2e}; source={regular['source_pullback']:.2e}",
    )

    ir = infrared_errors(union, mutation)
    checks.check(
        "einstein-infrared-limit",
        "successive halvings converge quadratically to the supplied linearized Einstein comparator",
        ir[0] < 4.0e-6 and ir[1] < 1.0e-6 and ir[2] < 2.5e-7
        and 0.23 < ir[1] / ir[0] < 0.27
        and 0.23 < ir[2] / ir[1] < 0.27,
        f"relative errors={tuple(f'{value:.3e}' for value in ir)}",
    )

    off_axis = off_axis_data(union, mutation)
    checks.check(
        "generic-off-axis-full-rank-transverse-trace-poles",
        "two simple full-rank quotient poles reverse an analytic conserved-source response",
        2.8788 < off_axis["roots"][0] < 2.8789
        and 3.0980 < off_axis["roots"][1] < 3.0982
        and max(off_axis["root_shifts"]) < 4.0e-4
        and min(off_axis["singular"]) > 0.05
        and min(abs(value) for value in off_axis["root_slopes"]) > 0.1
        and min(off_axis["root_gaps"]) > 0.03
        and off_axis["responses"][0][0] < -1.0e6
        and off_axis["responses"][0][1] > 1.0e6
        and off_axis["responses"][1][0] > 1.0e5
        and off_axis["responses"][1][1] < -1.0e5
        and off_axis["ward"] < 2.0e-12
        and off_axis["inertias"] == ((1, 5, 0), (0, 6, 0), (1, 5, 0))
        and off_axis["curvature_rank"] == 3
        and off_axis["curvature_null"] < 1.0e-12
        and off_axis["curvature_inertias"] == ((1, 2, 0),) * 4
        and off_axis["curvature_independence"] < 1.0e-9
        and off_axis["curvature_eigenvalues"][0] < -0.04
        and off_axis["generic_metric_rank"] == 10
        and off_axis["generic_gauge_rank"] == 4,
        f"roots={off_axis['roots'][0]:.12f}/{off_axis['roots'][1]:.12f}; shifts={off_axis['root_shifts']}; slopes={off_axis['root_slopes']}; gaps={off_axis['root_gaps']}; sigmaM={off_axis['singular']}",
    )

    axial = axial_data(union, mutation)
    k72 = 2.0 * np.pi / 72.0
    checks.check(
        "axial-even-conformal-source-boundary",
        "the symmetry-defined scalar block is indefinite while temporal and transverse-trace responses have opposite signs",
        axial["block_error"] < 5.0e-4
        and -0.126 < axial["scalar_determinant"] < -0.124
        and axial["inertia"] == (1, 5, 0)
        and 2.000 < k72**2 * axial["temporal_response"] < 2.003
        and -6.01 < k72**2 * axial["trace_response"] < -5.99
        and axial["trace_ward"] < 1.0e-12
        and axial["rank_metric"] == 10,
        f"block error={axial['block_error']:.3e}; det={axial['scalar_determinant']:.9f}; k2C(temporal/trace)={k72**2*axial['temporal_response']:.6f}/{k72**2*axial['trace_response']:.6f}",
    )

    torus = torus_data(union, mutation)
    checks.check(
        "brillouin-torus-rank-and-periodicity-boundary",
        "equivalent momentum labels leave Q and G fixed but change the line-metric image rank and quotient",
        torus["metric_ranks"] == (8, 10)
        and torus["kernel_ranks"] == (4, 6)
        and torus["inertias"] == ((0, 4, 2), (1, 5, 0))
        and torus["action_match"] < 1.0e-12
        and torus["gauge_match"] < 1.0e-12
        and torus["projector_gap"] > 2.0
        and torus["rank_counts"] == {10: 73, 9: 6, 8: 2}
        and torus["pair_rank"] == 9
        and torus["pair_null"] < 1.0e-12,
        f"rank M/K={torus['metric_ranks']}/{torus['kernel_ranks']}; inertia={torus['inertias']}; Q/G={torus['action_match']:.2e}/{torus['gauge_match']:.2e}; corner census={torus['rank_counts']}",
    )

    tt = tt_atlas_data(union, mutation)
    checks.check(
        "interior-two-tt-positive-atlas-and-nyquist-alias",
        "both spatial TT directions are positive on the L=7 interior atlas but alias into edge gauge at the static cubic corner",
        tt["modes"] == 2394
        and tt["negatives"] == 0
        and tt["minimum"] > 0.07
        and max(abs(value) for value in tt["corner"]) < 1.0e-12
        and tt["corner_carrier_norm"] > 0.3
        and tt["corner_gauge_distance"] < 1.0e-12,
        f"modes={tt['modes']}; negatives={tt['negatives']}; min={tt['minimum']:.9f}; corner={tt['corner']}; gauge distance={tt['corner_gauge_distance']:.2e}",
    )

    note = flat(NOTE_PATH)
    if mutation == "note_boundary":
        note = note.replace("gravity_verdict: open", "gravity_verdict: closed")
    checks.check(
        "no-go-discipline-axiom-retention-and-toe-firewall",
        "the supplied-map failures remain narrow while periodic carriers, constraints, gravity, and axioms stay open",
        "line_metric_global_lattice_carrier_verdict: bounded_infeasible" in note
        and "full_metric_positive_covariance_verdict: bounded_infeasible" in note
        and "gravity_verdict: open" in note
        and "axiom_update_verdict: not_justified" in note
        and "zero obligation retirement" in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: pass for the narrow supplied-map claims" in note
        and "periodic incidence" in note,
        "the note lands N1-N8, preserves the positive incidence escape, and makes no audit, axiom, retirement, or TOE-score claim",
    )

    print("COMMON_METRIC_CERTIFICATE: M Gamma=G, D M=F R, tau=M^dagger j, and the hard pullback approaches linearized Einstein gravity as O(epsilon^2)")
    print("PHYSICAL_BOUNDARY: the full metric inverse has two full-rank off-axis transverse-trace-visible poles and the axial transverse-trace source has negative response")
    print("TORUS_BOUNDARY: Q and G are periodic, but the supplied sinc line map changes rank 8 to 10 across equivalent cubic-corner representatives")
    print("POSITIVE_CONTROL: both spatial TT forms are positive on all 2394 L=7 interior samples; their static cubic-corner images alias into edge gauge")
    print("N5_CERTIFICATE: the following five resolution statements delimit the executed negative claims")
    print("per_element: checked all 22 edge coordinates, 10 metric coordinates, four Ward columns, and explicit conserved metric and edge sources")
    print("per_site: checked and not executed — the sinc line map is a momentum-space continuum line average, not a supplied finite-range site stencil")
    print("per_mode: checked generic off-axis roots, the full 2394-mode L=7 TT atlas, 81 closed-cube corners, and equivalent torus labels")
    print("per_block: checked the literal Block185 action, line-metric restriction, curvature map, source pairing, and incidence-carrier escape")
    print("lattice_wide: checked and not executed — no nonlinear background, global constraint algebra, Record compiler, refinement law, or selected gravity theory is supplied")
    print("LINE_METRIC_GLOBAL_LATTICE_CARRIER_VERDICT: BOUNDED_INFEASIBLE; FULL_METRIC_POSITIVE_COVARIANCE_VERDICT: BOUNDED_INFEASIBLE; GRAVITY_VERDICT: OPEN")
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
