#!/usr/bin/env python3
"""Test two candidate reductions of the reflected curvature action.

The runner attacks two independent requirements exposed by the prior
TT/Record observable-refinement analysis.  First,
it asks whether stationary elimination of the nonmetric edge directions gives
a section that continues across either declared path.  Second, it resolves the
declared odd-TT bordered Laurent polynomial at one hostile momentum and
checks the actual pole weights of the local TT observable.  A failure is a
bounded numerical result on this supplied action/reduction pair, not a gravity
no-go or a result for the distinct nonlinear sourced action.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations
import os
from pathlib import Path
import sys
import time

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import brentq, root


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14 as block74  # noqa: E402
from admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11 import sign_basis, swap_matrix  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_"
    "TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PLAN_PATH = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-axiom-closure-20260809"
) / "ARTIFACT_PLAN.md"
PACK_PLAN_PATH = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-axiom-closure-block181-canonical-reduction-20260823"
) / "ARTIFACT_PLAN.md"
BLOCK180_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_TT_RECORD_OBSERVABLE_INVERSE_AMPLIFICATION_"
    "REFINEMENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_CANONICAL_REDUCTION_SCHUR_POLE_TT_SPECTRAL_WEIGHT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/ADMISSIBILITY_REGGE_TT_RECORD_OBSERVABLE_INVERSE_AMPLIFICATION_REFINEMENT_GATE_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    ".claude/science/physics-loops/toe-axiom-closure-20260809/ARTIFACT_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block181-canonical-reduction-20260823/ARTIFACT_PLAN.md",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_curvature_canonical_reduction_schur_pole_tt_spectral_weight_boundary_2026_08_23.py",
)
AUDIT_TIMEOUT_SEC = 180

MU = block74.MU
SPATIAL_WAVE_NUMBER = np.pi / 2.0
FOURIER_SAMPLES = 32
MOMENT_SAMPLES = 4096


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


@dataclass(frozen=True)
class SectionPole:
    name: str
    root_parameter: float
    momentum: tuple[float, ...]
    start_inertia: tuple[int, int, int]
    end_inertia: tuple[int, int, int]
    vertical_rank: int
    vertical_gap: float
    vertical_residual: float
    metric_rank: int
    metric_gap: float
    frame_rank: int
    frame_gap: float
    full_rank: int
    full_quotient_gap: float
    gauge_rank: int
    ward_relative: float
    mixed_row_norm: float
    mixed_fraction: float
    basis_spectrum_error: float


@dataclass(frozen=True)
class SpectralBranch:
    root: complex
    weight: complex
    moment_weight: complex
    left_coupling: float
    right_coupling: float
    border_residual: float
    edge_residual: float
    multiplier_ratio: float
    solver_success: bool
    simplicity_ratio: float

    @property
    def coupled(self) -> bool:
        return (
            self.left_coupling > 1.0e-7
            and self.right_coupling > 1.0e-7
            and self.edge_residual < 1.0e-10
            and self.multiplier_ratio < 1.0e-8
        )


@dataclass(frozen=True)
class LaurentCertificate:
    coefficient_support: tuple[int, ...]
    outer_rank: int
    coefficient_pair_error: float
    coefficient_leakage: float
    odd_dimensions: tuple[int, int]
    ward_relative: float
    determinant_support: tuple[int, int]
    determinant_pair_error: float
    determinant_reconstruction: float
    root_count: int
    inside_count: int
    reciprocal_error: float
    polynomial_root_residual: float
    root_minimum_separation: float
    root_unit_circle_gap: float
    refined_root_minimum_separation: float
    branches: tuple[SpectralBranch, ...]
    moment_error: float
    one_step_shifted_minimum: float
    two_step_minimum: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    values = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(values < -tolerance)),
        int(np.sum(values > tolerance)),
        int(np.sum(np.abs(values) <= tolerance)),
    )


def metric_map(union, momentum: np.ndarray) -> np.ndarray:
    return block74.block49.union_line_metric_map(union, momentum)


def action(union, momentum: np.ndarray) -> np.ndarray:
    return block74.cross_action_symbol(union, momentum, MU)


def section_data(
    union,
    momentum: np.ndarray,
    moving_complement: bool,
    fixed_complement: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    metric = metric_map(union, momentum)
    complement = (
        null_space(metric.conj().T, rcond=1.0e-12)
        if moving_complement
        else fixed_complement
    )
    operator = action(union, momentum)
    vertical = complement.conj().T @ operator @ complement
    vertical = 0.5 * (vertical + vertical.conj().T)
    mixing = complement.conj().T @ operator @ metric
    return metric, complement, operator, vertical, mixing


def section_pole(
    union,
    name: str,
    endpoint: np.ndarray,
    eigenvalue_index: int,
    moving_complement: bool,
    fixed_complement: np.ndarray,
    mutation: str,
) -> SectionPole:
    start = np.asarray((0.4, 0.0, 0.0, 0.0))

    def point(parameter: float):
        momentum = (1.0 - parameter) * start + parameter * endpoint
        data = section_data(
            union, momentum, moving_complement, fixed_complement
        )
        values = np.linalg.eigvalsh(data[3])
        return momentum, data, values

    start_momentum, start_data, start_values = point(0.0)
    end_momentum, end_data, end_values = point(1.0)
    del start_momentum, end_momentum
    root_parameter = brentq(
        lambda value: point(value)[2][eigenvalue_index],
        0.0,
        1.0,
        xtol=1.0e-14,
    )
    momentum, (metric, complement, operator, vertical, mixing), _ = point(
        root_parameter
    )
    values, vectors = np.linalg.eigh(vertical)
    slot = int(np.argmin(np.abs(values)))
    zero_vector = vectors[:, slot]
    singular = np.linalg.svd(operator, compute_uv=False)
    gauge = block74.block48.union_gauge_map(union, momentum)
    frame = np.column_stack((metric, complement))
    if mutation == "fixed_section" and not moving_complement:
        frame = frame.copy()
        frame[:, -1] = frame[:, 0]
    frame_singular = np.linalg.svd(frame, compute_uv=False)

    deterministic = np.fromfunction(
        lambda row, column: np.sin((row + 1.0) * (column + 2.0))
        + np.cos((row + 3.0) * (column + 1.0)),
        (complement.shape[1], complement.shape[1]),
    )
    rotation = np.linalg.qr(deterministic)[0]
    rotated = rotation.conj().T @ vertical @ rotation
    basis_spectrum_error = float(
        np.max(np.abs(np.linalg.eigvalsh(rotated) - values))
    )
    certificate_mixing = mixing
    if mutation == "moving_section" and moving_complement:
        certificate_mixing = mixing - np.outer(
            zero_vector, zero_vector.conj() @ mixing
        )
    mixed_row_norm = float(
        np.linalg.norm(zero_vector.conj() @ certificate_mixing)
    )
    mixed_fraction = mixed_row_norm / max(
        float(np.linalg.norm(certificate_mixing)), 1.0e-30
    )

    return SectionPole(
        name=name,
        root_parameter=float(root_parameter),
        momentum=tuple(float(value) for value in momentum),
        start_inertia=inertia(start_data[3]),
        end_inertia=inertia(end_data[3]),
        vertical_rank=int(np.linalg.matrix_rank(vertical, tol=1.0e-10)),
        vertical_gap=float(np.min(np.abs(values))),
        vertical_residual=float(
            np.linalg.norm(vertical @ zero_vector)
            / max(float(np.linalg.norm(vertical)), 1.0e-30)
        ),
        metric_rank=int(np.linalg.matrix_rank(metric, tol=1.0e-10)),
        metric_gap=float(np.linalg.svd(metric, compute_uv=False)[-1]),
        frame_rank=int(
            np.linalg.matrix_rank(frame, tol=1.0e-10)
        ),
        frame_gap=float(frame_singular[-1]),
        full_rank=int(np.linalg.matrix_rank(operator, tol=1.0e-9)),
        full_quotient_gap=float(np.sort(singular)[4]),
        gauge_rank=int(np.linalg.matrix_rank(gauge, tol=1.0e-10)),
        ward_relative=float(
            np.linalg.norm(operator @ gauge)
            / (float(np.linalg.norm(operator)) * float(np.linalg.norm(gauge)))
        ),
        mixed_row_norm=mixed_row_norm,
        mixed_fraction=float(mixed_fraction),
        basis_spectrum_error=basis_spectrum_error,
    )


def matrix_fourier_coefficients(
    function,
    allowed: tuple[int, ...],
    samples: int = FOURIER_SAMPLES,
) -> tuple[dict[int, np.ndarray], float]:
    values = np.asarray(
        [function(2.0 * np.pi * index / samples) for index in range(samples)]
    )
    transformed = np.fft.fft(values, axis=0) / samples
    scale = max(float(np.linalg.norm(value)) for value in transformed)
    allowed_set = set(allowed)
    leakage = 0.0
    for index, value in enumerate(transformed):
        exponent = index if index <= samples // 2 else index - samples
        if exponent not in allowed_set:
            leakage = max(leakage, float(np.linalg.norm(value)) / scale)
    return {exponent: transformed[exponent % samples] for exponent in allowed}, leakage


def polynomial_multiply(
    left: dict[int, complex], right: dict[int, complex]
) -> dict[int, complex]:
    output: dict[int, complex] = {}
    for left_degree, left_value in left.items():
        for right_degree, right_value in right.items():
            degree = left_degree + right_degree
            output[degree] = output.get(degree, 0.0j) + left_value * right_value
    return output


def permutation_sign(permutation: tuple[int, ...]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(len(permutation))
        for right in range(left + 1, len(permutation))
    )
    return -1 if inversions % 2 else 1


def border_coefficients(
    operator: dict[int, np.ndarray],
    right_gauge: dict[int, np.ndarray],
    left_gauge: dict[int, np.ndarray],
) -> dict[int, np.ndarray]:
    edge_dimension = next(iter(operator.values())).shape[0]
    gauge_dimension = next(iter(right_gauge.values())).shape[1]
    dimension = edge_dimension + gauge_dimension
    exponents = sorted(set(operator) | set(right_gauge) | set(left_gauge))
    output = {}
    for exponent in exponents:
        matrix = np.zeros((dimension, dimension), dtype=complex)
        if exponent in operator:
            matrix[:edge_dimension, :edge_dimension] = operator[exponent]
        if exponent in left_gauge:
            matrix[:edge_dimension, edge_dimension:] = left_gauge[exponent]
        if exponent in right_gauge:
            matrix[edge_dimension:, :edge_dimension] = right_gauge[exponent].T
        output[exponent] = matrix
    return output


def determinant_polynomial(
    coefficients: dict[int, np.ndarray],
) -> dict[int, complex]:
    dimension = next(iter(coefficients.values())).shape[0]
    entries: list[list[dict[int, complex]]] = [
        [{} for _ in range(dimension)] for _ in range(dimension)
    ]
    entry_scale = max(float(np.linalg.norm(value)) for value in coefficients.values())
    for exponent, matrix in coefficients.items():
        for row in range(dimension):
            for column in range(dimension):
                value = matrix[row, column]
                if abs(value) > 1.0e-14 * entry_scale:
                    entries[row][column][exponent] = value

    determinant: dict[int, complex] = {}
    for permutation in permutations(range(dimension)):
        term: dict[int, complex] = {0: 1.0 + 0.0j}
        for row, column in enumerate(permutation):
            if not entries[row][column]:
                term = {}
                break
            term = polynomial_multiply(term, entries[row][column])
        if not term:
            continue
        sign = permutation_sign(permutation)
        for exponent, value in term.items():
            determinant[exponent] = determinant.get(exponent, 0.0j) + sign * value

    scale = max(abs(value) for value in determinant.values())
    return {
        exponent: value
        for exponent, value in determinant.items()
        if abs(value) > 1.0e-13 * scale
    }


def evaluate_laurent(
    coefficients: dict[int, np.ndarray], value: complex
) -> np.ndarray:
    return sum(matrix * value**exponent for exponent, matrix in coefficients.items())


def evaluate_laurent_derivative(
    coefficients: dict[int, np.ndarray], value: complex
) -> np.ndarray:
    return sum(
        exponent * matrix * value ** (exponent - 1)
        for exponent, matrix in coefficients.items()
        if exponent != 0
    )


def normalized_polynomial_residual(
    polynomial: dict[int, complex], value: complex
) -> float:
    numerator = abs(sum(coefficient * value**exponent for exponent, coefficient in polynomial.items()))
    denominator = sum(
        abs(coefficient * value**exponent)
        for exponent, coefficient in polynomial.items()
    )
    return float(numerator / max(denominator, 1.0e-300))


def laurent_certificate(union, mutation: str) -> LaurentCertificate:
    directions = np.asarray(union.directions, dtype=float)
    edge_swap = swap_matrix(directions, 1, 2)
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    edge_basis = sign_basis(edge_swap, -1)
    gauge_basis = sign_basis(gauge_swap, -1)

    def momentum(temporal: complex) -> np.ndarray:
        return np.asarray(
            (SPATIAL_WAVE_NUMBER, 0.0, 0.0, temporal), dtype=complex
        )

    def odd_operator_sample(temporal: float) -> np.ndarray:
        sample = (
            edge_basis.T
            @ (-action(union, momentum(temporal)))
            @ edge_basis
        )
        if mutation == "laurent_support":
            sample = sample + 1.0e-3 * np.exp(3.0j * temporal) * np.eye(
                edge_basis.shape[1]
            )
        return sample

    operator_coefficients, operator_leakage = matrix_fourier_coefficients(
        odd_operator_sample,
        (-2, -1, 0, 1, 2),
    )
    right_coefficients, right_leakage = matrix_fourier_coefficients(
        lambda temporal: edge_basis.T
        @ block74.block48.union_gauge_map(union, momentum(temporal))
        @ gauge_basis,
        (-1, 0, 1),
    )
    left_coefficients, left_leakage = matrix_fourier_coefficients(
        lambda temporal: edge_basis.T
        @ block74.block48.union_gauge_map(union, -momentum(temporal))
        @ gauge_basis,
        (-1, 0, 1),
    )
    coefficient_scale = max(
        float(np.linalg.norm(value)) for value in operator_coefficients.values()
    )
    coefficient_support = tuple(
        exponent
        for exponent, value in sorted(operator_coefficients.items())
        if np.linalg.norm(value) > 1.0e-11 * coefficient_scale
    )
    coefficient_pair_error = max(
        float(
            np.linalg.norm(
                operator_coefficients[-exponent]
                - operator_coefficients[exponent].conj().T
            )
        )
        for exponent in (0, 1, 2)
    ) / coefficient_scale
    outer_rank = int(
        np.linalg.matrix_rank(operator_coefficients[2], tol=1.0e-10)
    )

    ward_relative = 0.0
    for temporal in (0.0, 0.37, 1.1, 2.4):
        value = momentum(temporal)
        operator = action(union, value)
        right = block74.block48.union_gauge_map(union, value)
        left = block74.block48.union_gauge_map(union, -value)
        if mutation == "ward_identity":
            right = right.copy()
            right[0, 0] += 1.0e-3
        scale = float(np.linalg.norm(operator))
        ward_relative = max(
            ward_relative,
            float(np.linalg.norm(operator @ right))
            / (scale * float(np.linalg.norm(right))),
            float(np.linalg.norm(left.T @ operator))
            / (float(np.linalg.norm(left)) * scale),
        )

    bordered = border_coefficients(
        operator_coefficients, right_coefficients, left_coefficients
    )
    determinant = determinant_polynomial(bordered)
    lower, upper = min(determinant), max(determinant)
    determinant_scale = max(abs(value) for value in determinant.values())
    determinant_pair_error = max(
        abs(determinant.get(exponent, 0.0j) - np.conj(determinant.get(-exponent, 0.0j)))
        for exponent in range(lower, upper + 1)
    ) / determinant_scale

    reconstruction_determinant = dict(determinant)
    if mutation == "root_certificate":
        reconstruction_determinant[lower] += 1.0e-2 * determinant_scale
    reconstruction = 0.0
    for value in (np.exp(0.17 + 0.31j), np.exp(-0.23 + 0.47j)):
        direct = np.linalg.det(evaluate_laurent(bordered, value))
        rebuilt = sum(
            coefficient * value**exponent
            for exponent, coefficient in reconstruction_determinant.items()
        )
        reconstruction = max(
            reconstruction, abs(direct - rebuilt) / max(abs(direct), 1.0e-30)
        )

    polynomial = np.asarray(
        [determinant.get(exponent, 0.0j) for exponent in range(lower, upper + 1)]
    )
    roots = np.roots(polynomial[::-1])
    root_minimum_separation = min(
        abs(left - right)
        for index, left in enumerate(roots)
        for right in roots[index + 1 :]
    )
    root_unit_circle_gap = min(abs(abs(value) - 1.0) for value in roots)
    polynomial_root_residual = max(
        normalized_polynomial_residual(determinant, value) for value in roots
    )
    reciprocal_error = max(
        min(
            abs(candidate - 1.0 / np.conj(value))
            / max(abs(1.0 / np.conj(value)), 1.0)
            for candidate in roots
        )
        for value in roots
    )
    inside = tuple(value for value in roots if abs(value) < 1.0 - 1.0e-7)

    observable = block74.local_tt_observables(union, "")[0]
    right_hand_side = np.concatenate(
        (edge_basis.T @ observable, np.zeros(gauge_basis.shape[1]))
    ).astype(complex)
    branches = []
    for seed in inside:
        scale = float(np.linalg.norm(evaluate_laurent(bordered, seed)))

        def determinant_pair(values: np.ndarray) -> np.ndarray:
            value = complex(values[0], values[1])
            determinant_value = np.linalg.det(
                evaluate_laurent(bordered, value) / scale
            )
            return np.asarray(
                (determinant_value.real, determinant_value.imag), dtype=float
            )

        solved = root(
            determinant_pair,
            np.asarray((seed.real, seed.imag)),
            method="lm",
            options={"ftol": 1.0e-14, "xtol": 1.0e-14},
        )
        value = complex(solved.x[0], solved.x[1])
        border = evaluate_laurent(bordered, value)
        left_vectors, singular_values, right_vectors_h = np.linalg.svd(border)
        right_vector = right_vectors_h.conj().T[:, -1]
        left_vector = left_vectors[:, -1].conj()
        derivative = evaluate_laurent_derivative(bordered, value)
        denominator = left_vector.T @ derivative @ right_vector
        simplicity_ratio = float(
            abs(denominator)
            / max(
                float(np.linalg.norm(left_vector))
                * float(np.linalg.norm(derivative))
                * float(np.linalg.norm(right_vector)),
                1.0e-300,
            )
        )
        residue = (
            (right_hand_side.T @ right_vector)
            * (left_vector.T @ right_hand_side)
            / denominator
        )
        moment_weight = residue / value
        weight = (
            complex(abs(moment_weight))
            if mutation == "spectral_weight"
            else moment_weight
        )
        edge_coordinates = right_vector[: edge_basis.shape[1]]
        full_edge = edge_basis @ edge_coordinates
        multiplier = right_vector[edge_basis.shape[1] :]
        temporal = -1j * np.log(value)
        full_operator = action(union, momentum(temporal))
        branches.append(
            SpectralBranch(
                root=value,
                weight=complex(weight),
                moment_weight=complex(moment_weight),
                left_coupling=float(
                    abs(left_vector.T @ right_hand_side)
                    / (np.linalg.norm(left_vector) * np.linalg.norm(right_hand_side))
                ),
                right_coupling=float(
                    abs(right_hand_side.T @ right_vector)
                    / (np.linalg.norm(right_hand_side) * np.linalg.norm(right_vector))
                ),
                border_residual=float(singular_values[-1] / singular_values[0]),
                edge_residual=float(
                    np.linalg.norm(full_operator @ full_edge)
                    / (
                        float(np.linalg.norm(full_operator))
                        * float(np.linalg.norm(full_edge))
                    )
                ),
                multiplier_ratio=float(
                    np.linalg.norm(multiplier)
                    / max(float(np.linalg.norm(edge_coordinates)), 1.0e-30)
                ),
                solver_success=bool(
                    solved.success
                    and np.linalg.norm(determinant_pair(solved.x)) < 1.0e-9
                ),
                simplicity_ratio=simplicity_ratio,
            )
        )

    branches = tuple(sorted(branches, key=lambda item: abs(item.root)))
    refined_root_minimum_separation = min(
        abs(left.root - right.root)
        for index, left in enumerate(branches)
        for right in branches[index + 1 :]
    )
    coupled = tuple(branch for branch in branches if branch.coupled)
    temporal_values = 2.0 * np.pi * np.arange(MOMENT_SAMPLES) / MOMENT_SAMPLES
    covariance = np.asarray(
        [
            (
                right_hand_side.T
                @ np.linalg.solve(
                    evaluate_laurent(bordered, np.exp(1j * temporal)),
                    right_hand_side,
                )
            ).real
            for temporal in temporal_values
        ]
    )
    moments = np.asarray(
        [
            np.mean(np.exp(1j * temporal_values * order) * covariance).real
            for order in range(13)
        ]
    )
    reconstructed = np.asarray(
        [
            sum(
                branch.moment_weight
                * branch.root
                ** (order + int(mutation == "moment_reconstruction"))
                for branch in coupled
            ).real
            for order in range(13)
        ]
    )
    moment_error = float(
        np.max(np.abs(moments[:9] - reconstructed[:9]))
        / max(float(np.max(np.abs(moments[:9]))), 1.0e-30)
    )
    one_step_shifted = block74.hankel_minimum(
        moments, step=1, order=2, shift=1
    )
    two_step = block74.hankel_minimum(moments, step=2, order=3, shift=0)

    return LaurentCertificate(
        coefficient_support=coefficient_support,
        outer_rank=outer_rank,
        coefficient_pair_error=coefficient_pair_error,
        coefficient_leakage=max(
            operator_leakage, right_leakage, left_leakage
        ),
        odd_dimensions=(edge_basis.shape[1], gauge_basis.shape[1]),
        ward_relative=ward_relative,
        determinant_support=(lower, upper),
        determinant_pair_error=float(determinant_pair_error),
        determinant_reconstruction=float(reconstruction),
        root_count=len(roots),
        inside_count=len(inside),
        reciprocal_error=float(reciprocal_error),
        polynomial_root_residual=float(polynomial_root_residual),
        root_minimum_separation=float(root_minimum_separation),
        root_unit_circle_gap=float(root_unit_circle_gap),
        refined_root_minimum_separation=float(refined_root_minimum_separation),
        branches=branches,
        moment_error=moment_error,
        one_step_shifted_minimum=one_step_shifted,
        two_step_minimum=two_step,
    )


def section_gate(pole: SectionPole, expected_start, expected_end) -> bool:
    return (
        pole.start_inertia == expected_start
        and pole.end_inertia == expected_end
        and pole.vertical_rank == 11
        and pole.vertical_gap < 1.0e-10
        and pole.vertical_residual < 1.0e-10
        and pole.metric_rank == 10
        and pole.metric_gap > 0.3
        and pole.frame_rank == 22
        and pole.frame_gap > 0.1
        and pole.full_rank == 18
        and pole.full_quotient_gap > 1.0e-4
        and pole.gauge_rank == 4
        and pole.ward_relative < 1.0e-12
        and pole.mixed_row_norm > 1.0e-3
        and pole.mixed_fraction > 0.1
        and pole.basis_spectrum_error < 1.0e-11
    )


def main() -> int:
    started = time.perf_counter()
    mutation = os.environ.get("TOE_MUTATION", "")
    allowed_mutations = {
        "",
        "laurent_support",
        "ward_identity",
        "moving_section",
        "fixed_section",
        "root_certificate",
        "spectral_weight",
        "moment_reconstruction",
        "note_boundary",
    }
    if mutation not in allowed_mutations:
        raise ValueError(f"unknown TOE_MUTATION={mutation}")
    checks = Checks()
    note = flat(NOTE_PATH)
    if mutation == "note_boundary":
        note = note.replace(
            "tested two-chart/raw-quotient verdict: bounded failure",
            "tested two-chart/raw-quotient verdict: removed",
        )
    axiom = flat(AXIOM_PATH)
    plan = flat(PLAN_PATH)
    pack_plan = flat(PACK_PLAN_PATH)
    block180 = flat(BLOCK180_PATH)

    union = block74.block48.build_reflection_union()
    fixed_complement = null_space(
        metric_map(union, np.zeros(4)).conj().T, rcond=1.0e-12
    )
    moving = section_pole(
        union,
        "momentum-orthogonal",
        2.0 * np.pi / 9.0 * np.asarray((-2.0, 0.0, 1.0, 0.0)),
        9,
        True,
        fixed_complement,
        mutation,
    )
    fixed = section_pole(
        union,
        "fixed-zero-momentum",
        2.0 * np.pi / 9.0 * np.asarray((-4.0, -4.0, 1.0, 0.0)),
        10,
        False,
        fixed_complement,
        mutation,
    )
    laurent = laurent_certificate(union, mutation)

    print(
        "RESULT: both named stationary metric/nonmetric charts have metric-coupled vertical poles, and the declared odd-TT polynomial has non-positive spectral branches"
    )
    print(
        "INTERPRETATION: this bounds the tested two-chart section and raw-quotient transfer on the reflected action; the distinct nonlinear source-bearing action remains untested"
    )
    for pole in (moving, fixed):
        momentum_text = ",".join(f"{value:.8f}" for value in pole.momentum)
        print(
            f"section_pole: chart={pole.name} t={pole.root_parameter:.15f} "
            f"q=({momentum_text}) inertia={pole.start_inertia}->{pole.end_inertia} "
            f"C_rank={pole.vertical_rank} C_gap={pole.vertical_gap:.3e} "
            f"frame={pole.frame_rank}/{pole.frame_gap:.3e} Q_rank={pole.full_rank} "
            f"gauge_rank={pole.gauge_rank} quotient_gap={pole.full_quotient_gap:.3e} "
            f"mixed={pole.mixed_row_norm:.6e} fraction={pole.mixed_fraction:.6f}"
        )
    print(
        f"laurent: support={laurent.coefficient_support} outer_rank={laurent.outer_rank} "
        f"odd={laurent.odd_dimensions[0]}+{laurent.odd_dimensions[1]} "
        f"det={laurent.determinant_support[0]}..{laurent.determinant_support[1]} "
        f"roots={laurent.root_count} inside={laurent.inside_count} "
        f"reciprocal={laurent.reciprocal_error:.3e} reconstruction={laurent.determinant_reconstruction:.3e}"
    )
    for branch in laurent.branches:
        print(
            f"spectral_branch: z={branch.root.real:+.12e}{branch.root.imag:+.12e}i "
            f"weight={branch.weight.real:+.12e}{branch.weight.imag:+.12e}i "
            f"couplings={branch.left_coupling:.3e}/{branch.right_coupling:.3e} "
            f"edge={branch.edge_residual:.3e} multiplier={branch.multiplier_ratio:.3e} "
            f"simple={branch.simplicity_ratio:.3e} solver={int(branch.solver_success)} "
            f"coupled={int(branch.coupled)}"
        )

    authority = (
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axiom
        and "physical reduction/section" in block180
        and "block 181 pre-registered reflected-action canonical-reduction contract"
        in plan
        and "require eight formula/document mutations" in pack_plan
        and "are distinct typed actions" in note
        and "quadratic 22-edge reflected action" in note
        and "nonlinear 15-edge" in note
        and "no supplied intertwiner" in note
    )
    checks.check(
        "authority-and-distinct-action-bindings",
        "the exact parents are bound while the 15-edge nonlinear and 22-edge reflected actions remain distinctly typed",
        authority,
    )

    coefficient_gate = (
        laurent.coefficient_support == (-2, -1, 0, 1, 2)
        and laurent.outer_rank > 0
        and laurent.coefficient_pair_error < 1.0e-12
        and laurent.coefficient_leakage < 1.0e-12
        and laurent.odd_dimensions == (6, 1)
        and laurent.ward_relative < 1.0e-12
    )
    checks.check(
        "singular-higher-step-laurent-and-ward-structure",
        "the reflected action has a genuine two-step temporal stencil while exact odd-sector Ward structure survives",
        coefficient_gate,
        f"support={laurent.coefficient_support}; rank A2={laurent.outer_rank}; pair={laurent.coefficient_pair_error:.3e}; leakage={laurent.coefficient_leakage:.3e}; Ward={laurent.ward_relative:.3e}",
    )

    checks.check(
        "momentum-orthogonal-section-has-metric-coupled-pole",
        "the momentum-orthogonal stationary section becomes singular while the full gauge quotient remains regular and drives the zero mode",
        section_gate(moving, (10, 2, 0), (9, 3, 0)),
        f"t={moving.root_parameter:.15f}; C gap={moving.vertical_gap:.3e}; Q rank={moving.full_rank}; mixed={moving.mixed_row_norm:.6e}",
    )
    checks.check(
        "fixed-complement-section-has-independent-metric-coupled-pole",
        "the fixed zero-momentum complement moves rather than removes the stationary-section pole",
        section_gate(fixed, (10, 2, 0), (11, 1, 0)),
        f"t={fixed.root_parameter:.15f}; C gap={fixed.vertical_gap:.3e}; Q rank={fixed.full_rank}; mixed={fixed.mixed_row_norm:.6e}",
    )

    coupled = tuple(branch for branch in laurent.branches if branch.coupled)
    root_gate = (
        laurent.determinant_support == (-7, 7)
        and laurent.root_count == 14
        and laurent.inside_count == 7
        and laurent.determinant_pair_error < 1.0e-11
        and laurent.determinant_reconstruction < 1.0e-7
        and laurent.reciprocal_error < 1.0e-4
        and laurent.polynomial_root_residual < 1.0e-7
        and laurent.root_minimum_separation > 1.0e-6
        and laurent.root_unit_circle_gap > 1.0e-3
        and laurent.refined_root_minimum_separation > 1.0e-6
        and len(coupled) == 3
        and all(branch.solver_success for branch in laurent.branches)
        and min(branch.simplicity_ratio for branch in laurent.branches) > 1.0e-14
        and max(branch.border_residual for branch in coupled) < 1.0e-12
        and max(branch.edge_residual for branch in coupled) < 1.0e-10
        and max(branch.multiplier_ratio for branch in coupled) < 1.0e-8
    )
    checks.check(
        "declared-odd-bordered-root-certificate",
        "conditioned numerical reconstruction resolves the thresholded odd bordered roots and rejects gauge-border artifacts",
        root_gate,
        f"det={laurent.determinant_support}; roots={laurent.root_count}/{laurent.inside_count}; coupled={len(coupled)}; separation={laurent.root_minimum_separation:.3e}; unit-gap={laurent.root_unit_circle_gap:.3e}; simple={min(branch.simplicity_ratio for branch in laurent.branches):.3e}",
    )

    negative_positive_root = [
        branch
        for branch in coupled
        if branch.root.real > 0.0
        and abs(branch.root.imag) < 1.0e-8
        and branch.weight.real < -1.0e-5
    ]
    negative_root = [
        branch
        for branch in coupled
        if branch.root.real < 0.0
        and abs(branch.root.imag) < 1.0e-8
        and branch.weight.real > 1.0e-5
    ]
    target_root = [
        branch
        for branch in coupled
        if branch.root.real > 0.1 and branch.weight.real > 0.1
    ]
    spectral_gate = (
        len(negative_positive_root) == 1
        and len(negative_root) == 1
        and len(target_root) == 1
        and laurent.one_step_shifted_minimum < -1.0e-13
        and laurent.two_step_minimum < -1.0e-8
    )
    checks.check(
        "coupled-nonpositive-tt-spectral-branches",
        "the full odd TT quotient contains both an alternating branch and a positive root with negative spectral weight",
        spectral_gate,
        f"negative-weight positive roots={len(negative_positive_root)}; negative roots={len(negative_root)}; target={len(target_root)}; Hankel1={laurent.one_step_shifted_minimum:.3e}; Hankel2={laurent.two_step_minimum:.3e}",
    )

    checks.check(
        "residue-to-temporal-moment-reconstruction",
        "the coupled pole weights reconstruct the direct TT covariance moments rather than merely fitting determinant roots",
        laurent.moment_error < 1.0e-4,
        f"maximum relative first-nine-moment error={laurent.moment_error:.3e}",
    )

    note_boundary = (
        "tested two-chart/raw-quotient verdict: bounded failure" in note
        and all(f"### n{index}" in note for index in range(1, 9))
        and "n1--n8 status: `pass`" in note
        and "not gravity failure" in note
        and "zero toe percentage movement" in note
        and "no axiom is amended" in note
        and "half-space weyl" in note
        and "connection/holonomy" in note
        and "perfect-action" in note
    )
    checks.check(
        "scope-no-go-discipline-and-axiom-boundary",
        "the note lands N1-N8, preserves independent escape routes, and makes no gravity or axiom overclaim",
        note_boundary,
    )

    print(
        "N5_CERTIFICATE: two independent 12-direction stationary charts, one numerically reconstructed 7-by-7 odd gauge border, fourteen finite nonzero roots, and thirteen TT moments are resolved"
    )
    print(
        "per_element: checked all twenty-two reflected edge coordinates, all ten common-metric columns, and all four exact Ward columns"
    )
    print(
        "per_site: checked and not executed — only the translation-invariant reflected unit-cell Fourier symbol was used; no inhomogeneous multi-site carrier was run"
    )
    print(
        "per_mode: checked both declared real spatial section paths and every numerically resolved root of the thresholded odd-sector polynomial at k equals pi over two"
    )
    print(
        "per_block: checked vertical Schur compatibility, full gauge-quotient regularity, bordered roots, residues, and Hankel controls"
    )
    print(
        "lattice_wide: checked and not executed — no full Brillouin-zone, nonlinear-background, or all-lattice theorem was run or claimed"
    )
    print(
        "BOUNDARY: a physical constraint atlas, half-space contour/inner product, source and Record law, symplectic refinement, or changed action remains live"
    )
    print("TESTED_TWO_CHART_RAW_QUOTIENT_VERDICT: BOUNDED_FAILURE")
    print("GRAVITY_VERDICT: OPEN")
    print("TOE_MOVEMENT: obligations=0 percentages=0 axioms_amended=0")
    print(f"elapsed_sec={time.perf_counter() - started:.2f}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
