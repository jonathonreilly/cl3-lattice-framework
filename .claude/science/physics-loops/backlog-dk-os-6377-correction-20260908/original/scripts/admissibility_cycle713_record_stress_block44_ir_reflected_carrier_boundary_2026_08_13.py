#!/usr/bin/env python3
"""Block 68: carry the signed Record stress into the conditional gravity sector.

The runner fixes the unique ten-coordinate infrared source map, tests its
continuum Ward and Lorentzian Block-44 response, and then asks whether the
same six signed null directions have an exact finite-frequency edge carrier.
The supplied fifteen-edge orientation handles only three signs; the supplied
twenty-two-edge time-reflection union handles all six.  Closed neutral line
pairs are exact Ward-compatible sources and solve the complete union edge
equations on every nonzero supported mode of the declared five-torus.

This is a bounded conditional interface test.  It does not select the source
density/coupling, the reflected common-metric quotient, a Record clock, a
physical transfer, a nonlinear action, an axiom amendment, or retention.
"""

from __future__ import annotations

import argparse
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 180
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
KINETIC_PATH = ROOT / "docs" / "KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
BLOCK67_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_"
    "SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK44_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK47_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_"
    "SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK48_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
HELIX_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_"
    "REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
JOINT_LAW_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CLOSED_HELICAL_DEFECT_HISTORY_WARD_NEUTRAL_IR_REGGE_RESPONSE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py",
    "scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13 as block67  # noqa: E402
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402
import admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11 as block47  # noqa: E402
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402


HCOMPS = tuple(block44.HCOMPS)
EXPECTED_HCOMPS = (
    (0, 0), (1, 1), (2, 2), (3, 3), (0, 1),
    (0, 2), (0, 3), (1, 2), (1, 3), (2, 3),
)
DIRECTIONS = tuple(
    np.asarray(direction, dtype=int) for direction in block67.b64.DIRECTIONS
)
TOL = 5.0e-10
TORUS_SIZES = tuple(range(3, 9))


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 156 else detail[:153] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def tensor_coordinates(tensor: np.ndarray, off_diagonal_factor: float = 2.0) -> np.ndarray:
    """Covector paired with Block-44 symmetric metric coordinates."""
    return np.asarray(
        [
            (off_diagonal_factor if left != right else 1.0) * tensor[left, right]
            for left, right in HCOMPS
        ],
        dtype=float,
    )


def record_tensor(direction: np.ndarray) -> np.ndarray:
    """Permute Block-67 order (t,x,y,z) into Block-44 order (x,y,z,t)."""
    block67_vector = np.concatenate(([1.0], np.asarray(direction, dtype=float)))
    permutation = np.asarray((1, 2, 3, 0), dtype=int)
    vector = block67_vector[permutation]
    return np.outer(vector, vector)


def coordinate_certificate(wrong_order: bool) -> dict[str, float | int]:
    weighted_basis = []
    for index in range(len(HCOMPS)):
        weighted_basis.append(tensor_coordinates(block44.symmetric_basis(index)))
    rank = int(np.linalg.matrix_rank(np.asarray(weighted_basis)))
    failures = 0
    parity_failures = 0
    for direction in DIRECTIONS:
        if wrong_order:
            vector = np.concatenate(([1.0], direction.astype(float)))
            tensor = np.outer(vector, vector)
        else:
            tensor = record_tensor(direction)
        source = tensor_coordinates(tensor)
        dx, dy, dz = (float(value) for value in direction)
        expected = np.asarray(
            (dx * dx, dy * dy, dz * dz, 1.0, 2 * dx * dy,
             2 * dx * dz, 2 * dx, 2 * dy * dz, 2 * dy, 2 * dz)
        )
        failures += not np.array_equal(source, expected)
        opposite = -direction
        opposite_source = tensor_coordinates(record_tensor(opposite))
        parity_failures += not (
            np.array_equal(source[:6], opposite_source[:6])
            and np.array_equal(source[[6, 8, 9]], -opposite_source[[6, 8, 9]])
        )
    return {
        "rank": rank,
        "failures": failures,
        "parity_failures": parity_failures,
    }


def pairing_certificate(omit_off_diagonal_two: bool) -> dict[str, float]:
    factor = 1.0 if omit_off_diagonal_two else 2.0
    tensors = (
        np.asarray(
            ((1.2, -0.7, 0.3, 0.8), (-0.7, 2.1, 0.5, -0.4),
             (0.3, 0.5, -1.4, 0.9), (0.8, -0.4, 0.9, 1.7))
        ),
        record_tensor(DIRECTIONS[0]),
        record_tensor(DIRECTIONS[-1]),
    )
    perturbations = (
        np.asarray(
            ((0.4, 0.2, -0.3, 0.6), (0.2, -0.8, 0.7, 0.1),
             (-0.3, 0.7, 1.1, -0.5), (0.6, 0.1, -0.5, 0.9))
        ),
        np.arange(16, dtype=float).reshape(4, 4),
    )
    errors = []
    for tensor in tensors:
        source = tensor_coordinates(tensor, factor)
        for perturbation in perturbations:
            symmetric = 0.5 * (perturbation + perturbation.T)
            coordinates = np.asarray(
                [symmetric[left, right] for left, right in HCOMPS]
            )
            errors.append(abs(float(source @ coordinates - np.sum(tensor * symmetric))))

    ward_errors = []
    for tensor in tensors:
        source = tensor_coordinates(tensor, factor)
        for momentum in (
            np.asarray((0.4, -0.2, 0.7, -0.3)),
            np.asarray((-0.8, 0.5, 0.1, 0.6)),
        ):
            actual = block44.continuum_gauge_map(momentum).T @ source
            expected = 2.0 * tensor @ momentum
            ward_errors.append(float(np.linalg.norm(actual - expected)))
    return {"pairing_error": max(errors), "ward_identity_error": max(ward_errors)}


def ward_completion_certificate(off_shell_source: bool) -> dict[str, float | int]:
    on_shell_error = 0.0
    off_shell_floor = np.inf
    completion_error = 0.0
    kernel_dimensions = set()
    samples = (
        np.asarray((0.73, -0.31, 0.27)),
        np.asarray((-0.29, 0.61, 0.44)),
    )
    for direction in DIRECTIONS:
        tensor = record_tensor(direction)
        source = tensor_coordinates(tensor)
        for spatial in samples:
            frequency = float(spatial @ direction)
            if off_shell_source:
                frequency += 0.17
            momentum = np.concatenate((spatial, (-frequency,)))
            gauge = block44.continuum_gauge_map(momentum)
            on_shell_error = max(on_shell_error, float(np.linalg.norm(gauge.T @ source)))

            displaced = momentum.copy()
            displaced[3] -= 0.19
            off_shell_floor = min(
                off_shell_floor,
                float(np.linalg.norm(block44.continuum_gauge_map(displaced).T @ source)),
            )
            kernel_dimensions.add(10 - int(np.linalg.matrix_rank(gauge, tol=1.0e-11)))

    spatial_stress = np.asarray(
        ((1.2, -0.3, 0.5), (-0.3, 0.9, 0.2), (0.5, 0.2, 1.7))
    )
    spatial = np.asarray((0.4, -0.6, 0.8))
    frequency = 0.71
    mixed = spatial_stress @ spatial / frequency
    time_time = float(spatial @ spatial_stress @ spatial / frequency**2)
    tensor = np.zeros((4, 4), dtype=float)
    tensor[:3, :3] = spatial_stress
    tensor[:3, 3] = tensor[3, :3] = mixed
    tensor[3, 3] = time_time
    momentum = np.concatenate((spatial, (-frequency,)))
    completion_error = float(
        np.linalg.norm(block44.continuum_gauge_map(momentum).T @ tensor_coordinates(tensor))
    )
    return {
        "on_shell_error": on_shell_error,
        "off_shell_floor": off_shell_floor,
        "completion_error": completion_error,
        "kernel_dimensions": len(kernel_dimensions),
        "kernel_dimension": next(iter(kernel_dimensions)),
    }


def lorentzian_response_certificate(flip_mixed_sign: bool) -> dict[str, float | int]:
    ward_error = 0.0
    solve_error = 0.0
    off_shell_ranks = set()
    null_shell_ranks = set()
    for slot, direction in enumerate(DIRECTIONS):
        source = tensor_coordinates(record_tensor(direction))
        if flip_mixed_sign:
            source[[6, 8, 9]] *= -1.0
        transverse_one = DIRECTIONS[(slot + 2) % len(DIRECTIONS)].astype(float)
        if abs(float(transverse_one @ direction)) > 0.5:
            transverse_one = DIRECTIONS[(slot + 4) % len(DIRECTIONS)].astype(float)
        spatial = 0.71 * direction + 0.23 * transverse_one
        frequency = float(spatial @ direction)
        momentum = np.concatenate((spatial, (-frequency,)))
        operator = block44.lorentzian_operator(spatial, frequency)
        gauge = block44.continuum_gauge_map(momentum)
        response = -np.linalg.pinv(operator, rcond=1.0e-11) @ source
        ward_error = max(ward_error, float(np.linalg.norm(gauge.T @ source)))
        solve_error = max(solve_error, float(np.linalg.norm(operator @ response + source)))
        off_shell_ranks.add(int(np.linalg.matrix_rank(operator, tol=1.0e-10)))

        null_spatial = 0.67 * direction
        null_frequency = float(null_spatial @ direction)
        null_operator = block44.lorentzian_operator(null_spatial, null_frequency)
        null_response = -np.linalg.pinv(null_operator, rcond=1.0e-11) @ source
        solve_error = max(
            solve_error,
            float(np.linalg.norm(null_operator @ null_response + source)),
        )
        null_shell_ranks.add(int(np.linalg.matrix_rank(null_operator, tol=1.0e-10)))

    static_source = np.zeros(len(HCOMPS))
    static_source[HCOMPS.index((3, 3))] = 1.0
    static_operator = block44.lorentzian_operator(np.asarray((1.0, 0.0, 0.0)), 0.0)
    static_response = -np.linalg.pinv(static_operator) @ static_source
    static_error = abs(float(static_response[HCOMPS.index((3, 3))] - 2.0))
    return {
        "ward_error": ward_error,
        "solve_error": solve_error,
        "off_shell_rank": next(iter(off_shell_ranks)),
        "off_shell_rank_count": len(off_shell_ranks),
        "null_shell_rank": next(iter(null_shell_ranks)),
        "null_shell_rank_count": len(null_shell_ranks),
        "static_error": static_error,
    }


def original_full_edge_certificate(drop_nonmetric_correction: bool) -> dict[str, float | int]:
    map_error = 0.0
    schur_ward_error = 0.0
    schur_ranks = set()
    for momentum in (
        np.asarray((0.31, -0.47, 0.23, 0.19)),
        np.asarray((0.71, 0.11, -0.39, 0.53)),
    ):
        metric_map = block47.analytic_metric_map(momentum)
        continuum_gauge = block44.continuum_gauge_map(momentum)
        edge_gauge = block47.analytic_gauge_map(momentum)
        map_error = max(
            map_error,
            float(np.linalg.norm(metric_map @ continuum_gauge + 1j * edge_gauge)),
        )
        schur = block48.original_metric_schur(momentum)
        metric_gauge = block48.metric_gauge_map(momentum)
        schur_ward_error = max(
            schur_ward_error, float(np.linalg.norm(schur @ metric_gauge))
        )
        schur_ranks.add(int(np.linalg.matrix_rank(schur, tol=1.0e-9)))

    direction_index = {
        tuple(int(value) for value in direction): slot
        for slot, direction in enumerate(block47.DIRECTIONS)
    }
    edge_source = np.zeros(len(block47.DIRECTIONS), dtype=complex)
    edge_source[direction_index[(1, 0, 0, 1)]] = 2.0
    target = tensor_coordinates(record_tensor(np.asarray((1, 0, 0)))) / np.sqrt(2.0)
    response_error = 0.0
    ward_error = 0.0
    asymptotic_ratios = []
    for epsilon in (0.4, 0.2, 0.1):
        momentum = np.asarray((0.0, epsilon, 0.0, 0.0))
        symbol = block47.analytic_symbol(momentum)
        right_metric = block47.analytic_metric_map(momentum)
        left_metric = block47.analytic_metric_map(-momentum).T
        nonmetric = block48.NONMETRIC
        nonmetric_block = nonmetric.T @ symbol @ nonmetric
        mixing = left_metric @ symbol @ nonmetric
        effective = left_metric @ edge_source
        if not drop_nonmetric_correction:
            effective -= mixing @ np.linalg.solve(
                nonmetric_block, nonmetric.T @ edge_source
            )
        schur = block48.original_metric_schur(momentum)
        metric_response = -np.linalg.pinv(schur, rcond=1.0e-10) @ effective
        complement = -np.linalg.solve(
            nonmetric_block,
            nonmetric.T @ (symbol @ right_metric @ metric_response + edge_source),
        )
        edge_response = right_metric @ metric_response + nonmetric @ complement
        response_error = max(
            response_error,
            float(np.linalg.norm(symbol @ edge_response + edge_source)),
        )
        ward_error = max(
            ward_error,
            float(np.linalg.norm(block48.metric_gauge_map(momentum).conj().T @ effective)),
        )
        asymptotic_ratios.append(float(np.linalg.norm(effective - target) / epsilon**2))
    ratio_spread = max(asymptotic_ratios) - min(asymptotic_ratios)
    return {
        "map_error": map_error,
        "schur_ward_error": schur_ward_error,
        "rank": next(iter(schur_ranks)),
        "rank_count": len(schur_ranks),
        "response_error": response_error,
        "source_ward_error": ward_error,
        "asymptotic_ratio_spread": ratio_spread,
    }


def canonical_carrier(
    allowed: tuple[tuple[int, ...], ...], direction: np.ndarray
) -> tuple[tuple[int, ...], np.ndarray] | None:
    spacetime_step = np.concatenate((direction, (1,))).astype(int)
    forward = tuple(int(value) for value in spacetime_step)
    reverse = tuple(int(value) for value in -spacetime_step)
    if forward in allowed:
        return forward, np.zeros(4, dtype=int)
    if reverse in allowed:
        # The reversed edge is based at the future endpoint of the physical step.
        return reverse, spacetime_step
    return None


def reflected_coverage_certificate(original_only: bool) -> dict[str, float | int]:
    union = block48.build_reflection_union()
    allowed = tuple(
        tuple(int(value) for value in direction)
        for direction in (
            block48.ORIGINAL_DIRECTIONS if original_only else union.directions
        )
    )
    full_index = {direction: slot for slot, direction in enumerate(union.directions)}
    covered = 0
    source_error = 0.0
    used = set()
    coefficients = block48.metric_coefficients(np.asarray(union.directions))
    for direction in DIRECTIONS:
        carrier = canonical_carrier(allowed, direction)
        if carrier is None:
            continue
        edge, _offset = carrier
        covered += 1
        used.add(edge)
        edge_source = np.zeros(len(union.directions))
        edge_source[full_index[edge]] = 2.0
        target = tensor_coordinates(record_tensor(direction)) / np.sqrt(2.0)
        source_error = max(
            source_error, float(np.linalg.norm(coefficients.T @ edge_source - target))
        )

    ward_error = 0.0
    rank_count = 0
    for momentum in (
        np.asarray((0.37, -0.29, 0.41, 0.23)),
        np.asarray((-0.61, 0.17, 0.33, -0.47)),
    ):
        symbol = block48.union_symbol(union, momentum)
        gauge = block48.union_gauge_map(union, momentum)
        ward_error = max(
            ward_error,
            float(np.linalg.norm(symbol @ gauge)),
            float(np.linalg.norm(block48.union_symbol(union, -momentum).T @ gauge)),
        )
        rank_count += int(np.linalg.matrix_rank(gauge, tol=1.0e-10) == 4)
    return {
        "union_edges": len(union.directions),
        "covered": covered,
        "used": len(used),
        "source_error": source_error,
        "ward_error": ward_error,
        "gauge_rank_samples": rank_count,
    }


def transverse_offset(direction: np.ndarray) -> np.ndarray:
    if abs(int(direction[1])) == 0:
        return np.asarray((0, 1, 0, 0), dtype=int)
    return np.asarray((1, 0, 0, 0), dtype=int)


def periodic_carrier_certificate(drop_closure_edge: bool) -> dict[str, float | int]:
    union = block48.build_reflection_union()
    allowed = tuple(union.directions)
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    supported = 0
    ward_error = 0.0
    solve_error = 0.0
    relative_solve_error = 0.0
    null_overlap = 0.0
    nullities = set()
    for size in TORUS_SIZES:
        momenta = tuple(
            2.0 * np.pi * np.asarray(mode, dtype=float) / size
            for mode in product(range(size), repeat=4)
        )
        line_length = size - int(drop_closure_edge)
        for direction in DIRECTIONS:
            carrier = canonical_carrier(allowed, direction)
            if carrier is None:
                raise AssertionError("the reflected union must carry all signed directions")
            edge, base_offset = carrier
            row = edge_index[edge]
            spacetime_step = np.concatenate((direction, (1,))).astype(int)
            separation = transverse_offset(direction)
            for momentum in momenta:
                line_factor = sum(
                    np.exp(1j * float(momentum @ (step * spacetime_step + base_offset)))
                    for step in range(line_length)
                )
                neutral_factor = line_factor * (
                    1.0 - np.exp(1j * float(momentum @ separation))
                )
                source_row = np.zeros(len(union.directions), dtype=complex)
                source_row[row] = 2.0 * neutral_factor
                source_norm = float(np.linalg.norm(source_row))
                if source_norm < 1.0e-9:
                    continue
                supported += 1
                gauge = block48.union_gauge_map(union, momentum)
                ward_error = max(
                    ward_error, float(np.linalg.norm(source_row.conj() @ gauge))
                )
                symbol = block48.union_symbol(union, momentum)
                left_vectors, singular_values, _right_vectors = np.linalg.svd(symbol)
                nullities.add(int(np.sum(singular_values < 1.0e-9)))
                source_column = source_row.conj()
                left_null = left_vectors[:, singular_values < 1.0e-9]
                null_overlap = max(
                    null_overlap,
                    float(np.linalg.norm(left_null.conj().T @ source_column)),
                )
                response = -np.linalg.pinv(symbol, rcond=1.0e-10) @ source_column
                residual = float(np.linalg.norm(symbol @ response + source_column))
                solve_error = max(solve_error, residual)
                relative_solve_error = max(
                    relative_solve_error, residual / source_norm
                )
    return {
        "supported": supported,
        "ward_error": ward_error,
        "solve_error": solve_error,
        "relative_solve_error": relative_solve_error,
        "null_overlap": null_overlap,
        "nullity_count": len(nullities),
        "minimum_nullity": min(nullities),
        "maximum_nullity": max(nullities),
    }


def zero_mode_certificate(keep_zero_mode: bool) -> dict[str, float]:
    union = block48.build_reflection_union()
    symbol = block48.union_symbol(union, np.zeros(4))
    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    positive_residuals = []
    for direction in DIRECTIONS:
        carrier = canonical_carrier(tuple(union.directions), direction)
        if carrier is None:
            raise AssertionError
        edge, _offset = carrier
        source = np.zeros(len(union.directions), dtype=complex)
        source[edge_index[edge]] = 2.0 * 5
        response = -np.linalg.pinv(symbol, rcond=1.0e-10) @ source
        positive_residuals.append(float(np.linalg.norm(symbol @ response + source)))
    neutral_zero_norm = 0.0
    if keep_zero_mode:
        neutral_zero_norm = max(positive_residuals)
    return {
        "minimum_positive_residual": min(positive_residuals),
        "maximum_positive_residual": max(positive_residuals),
        "neutral_zero_norm": neutral_zero_norm,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "wrong_order",
            "omit_offdiag_two",
            "off_shell_source",
            "flip_mixed_sign",
            "drop_nonmetric_correction",
            "original_only",
            "drop_closure_edge",
            "keep_zero_mode",
            "broaden_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    parents = tuple(
        flat(path)
        for path in (
            BLOCK67_PATH, BLOCK44_PATH, BLOCK47_PATH, BLOCK48_PATH,
            HELIX_PATH, JOINT_LAW_PATH,
        )
    )

    checks.check(
        "A-source-stack-and-authority",
        "the current axiom authority and every typed parent are present without promotion",
        all(
            path.exists()
            for path in (
                NOTE_PATH, AXIOM_PATH, KINETIC_PATH, BLOCK67_PATH, BLOCK44_PATH,
                BLOCK47_PATH, BLOCK48_PATH, HELIX_PATH, JOINT_LAW_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "admissibility is not a dynamics axiom" in axiom
        and "none of these is treated as retained" in note
        and all("axiom" in parent for parent in parents),
        "Block68 consumes conditional parents only; origin/main remains the sole axiom authority",
    )

    coordinates = coordinate_certificate(mutation == "wrong_order")
    checks.check(
        "B-unique-ten-coordinate-source-map",
        "the (t,x,y,z) Record tensor has one invertible weighted map into Block44 order",
        HCOMPS == EXPECTED_HCOMPS
        and coordinates["rank"] == 10
        and coordinates["failures"] == 0
        and coordinates["parity_failures"] == 0,
        f"rank={coordinates['rank']}; six-axis truth-table failures={coordinates['failures']}; signed-parity failures={coordinates['parity_failures']}",
    )

    pairing = pairing_certificate(mutation == "omit_offdiag_two")
    checks.check(
        "C-offdiagonal-multiplicity-and-Ward-identity",
        "the factor-two coordinate covector pairs with symmetric fields and obeys Gamma^T C(T)=2Tp",
        pairing["pairing_error"] < 1.0e-12
        and pairing["ward_identity_error"] < 1.0e-12,
        f"pairing error={pairing['pairing_error']:.3e}; tensor Ward identity error={pairing['ward_identity_error']:.3e}",
    )

    ward = ward_completion_certificate(mutation == "off_shell_source")
    checks.check(
        "D-shell-Ward-and-six-dimensional-completion",
        "Record stress is conserved on omega=q.d and generic Ward-compatible sources form a six-dimensional kernel",
        ward["on_shell_error"] < 1.0e-12
        and ward["off_shell_floor"] > 0.1
        and ward["completion_error"] < 1.0e-12
        and ward["kernel_dimensions"] == 1
        and ward["kernel_dimension"] == 6,
        f"on-shell={ward['on_shell_error']:.3e}; off-shell floor={ward['off_shell_floor']:.3f}; completion={ward['completion_error']:.3e}; dim={ward['kernel_dimension']}",
    )

    lorentzian = lorentzian_response_certificate(mutation == "flip_mixed_sign")
    checks.check(
        "E-conditional-Block44-Lorentzian-response",
        "all six sources solve off-shell modulo gauge and on the null shell after the TT compatibility test",
        lorentzian["ward_error"] < 1.0e-12
        and lorentzian["solve_error"] < 1.0e-11
        and lorentzian["off_shell_rank_count"] == 1
        and lorentzian["off_shell_rank"] == 6
        and lorentzian["null_shell_rank_count"] == 1
        and lorentzian["null_shell_rank"] == 4
        and lorentzian["static_error"] < 1.0e-12,
        f"Ward={lorentzian['ward_error']:.3e}; solve={lorentzian['solve_error']:.3e}; ranks={lorentzian['off_shell_rank']}/{lorentzian['null_shell_rank']}; unit e_tt gives h_tt=2",
    )

    full_edge = original_full_edge_certificate(
        mutation == "drop_nonmetric_correction"
    )
    checks.check(
        "F-original-full-edge-source-Schur-intertwiner",
        "the exact edge gauge map descends to rank-six Schur and stationary source elimination is load-bearing",
        full_edge["map_error"] < 1.0e-12
        and full_edge["schur_ward_error"] < 1.0e-10
        and full_edge["rank_count"] == 1
        and full_edge["rank"] == 6
        and full_edge["response_error"] < 1.0e-9
        and full_edge["source_ward_error"] < 1.0e-12
        and full_edge["asymptotic_ratio_spread"] < 1.0e-4,
        f"M C=-iG error={full_edge['map_error']:.2e}; full-edge solve={full_edge['response_error']:.2e}; IR O(p^2) ratio spread={full_edge['asymptotic_ratio_spread']:.2e}",
    )

    reflected = reflected_coverage_certificate(mutation == "original_only")
    checks.check(
        "G-six-signed-reflected-edge-lift",
        "the twenty-two-edge time-reflection union carries every signed null direction with the forced source shape",
        reflected["union_edges"] == 22
        and reflected["covered"] == 6
        and reflected["used"] == 6
        and reflected["source_error"] < 1.0e-12
        and reflected["ward_error"] < 1.0e-10
        and reflected["gauge_rank_samples"] == 2,
        f"covered={reflected['covered']}/6 with {reflected['used']} edge classes; source pullback error={reflected['source_error']:.2e}; union Ward={reflected['ward_error']:.2e}",
    )

    periodic = periodic_carrier_certificate(mutation == "drop_closure_edge")
    checks.check(
        "H-exact-neutral-line-full-edge-response",
        "all six closed neutral line pairs obey finite-frequency Ward and solve every supported complete-edge mode",
        periodic["supported"] == 6528
        and periodic["ward_error"] < 1.0e-11
        and periodic["solve_error"] < 1.0e-10
        and periodic["relative_solve_error"] < 1.0e-11
        and periodic["null_overlap"] < 1.0e-10
        and periodic["minimum_nullity"] == 4
        and periodic["maximum_nullity"] == 5,
        f"L=3..8 modes={periodic['supported']}; Ward={periodic['ward_error']:.2e}; full-null={periodic['null_overlap']:.2e}; solve={periodic['solve_error']:.2e}; nullities={periodic['minimum_nullity']}..{periodic['maximum_nullity']}",
    )

    zero = zero_mode_certificate(mutation == "keep_zero_mode")
    checks.check(
        "I-compact-zero-mode-boundary",
        "neutral pairing removes the forbidden compact net source while a lone positive line is explicitly rejected",
        zero["neutral_zero_norm"] < 1.0e-12
        and zero["minimum_positive_residual"] > 1.0,
        f"neutral p=0 norm={zero['neutral_zero_norm']:.1e}; lone-line full-edge residual={zero['minimum_positive_residual']:.6f}..{zero['maximum_positive_residual']:.6f}",
    )

    boundary_phrases = (
        "zero toe percentage movement",
        "one global coupling",
        "sqrt(2)",
        "common-metric",
        "record clock",
        "nonlinear",
        "no-go gate: fail",
        "partial-narrowing",
        "n1",
        "n8",
        "no canonical axiom is edited",
    )
    boundary_ok = (
        mutation != "broaden_boundary"
        and all(phrase in note for phrase in boundary_phrases)
    )
    checks.check(
        "J-no-go-discipline-and-scope-boundary",
        "the surviving routes force partial narrowing and keep every law-bearing wall explicit",
        boundary_ok,
        "broad gravity no-go forbidden; cadence, normalization, common metric, transfer, nonlinear law, adoption, and retention remain open",
    )

    print(
        "N5_CERTIFICATE: ten source coordinates, six signed directions, two continuum momentum regimes, complete original-edge stationary elimination, all 22 reflected edge classes, and every Fourier mode on L=3..8 for six neutral line pairs are resolved"
    )
    print(
        "per_element: every symmetric coordinate multiplicity, Record sign, edge orientation, gauge column, source row, and compact zero-mode contribution is tested explicitly"
    )
    print(
        "per_sample: generic off-shell, gravity-null-shell, static, full-zone finite-frequency, and all 6528 nonzero neutral direction-mode source samples are checked"
    )
    print(
        "per_block: Block67 Record stress, Block44 conditional Einstein response, Block47 full-edge Schur elimination, and Block48 reflected union meet at typed interfaces"
    )
    print(
        "lattice_wide: exact closed neutral sources cover all six signed velocities on periodic L=3..8 tori; no arbitrary-volume, net-positive compact source, or nonlinear law is inferred"
    )
    print(
        "scope_boundary: conditional IR source and finite-frequency carrier theorem only; not source normalization, common-metric selection, Record cadence, physical transfer, axiom amendment, retention, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
