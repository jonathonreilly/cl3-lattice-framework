#!/usr/bin/env python3
"""Check the reflected-orientation and common-metric Regge transfer gate.

The supplied repaired fifteen-edge action has small complex pole phases under
the conditional single-orientation continuation.  This runner constructs the
minimal local union of that edge complex and its time reflection, proves the
exact three-dimensional relative-shift flat sector of every orientation-
separable constant-metric action, and tests a narrower common-metric
two-orientation candidate.  The latter has real sampled tensor poles and a
positive conditional two-step spectral kernel, but its metric identification
and action-to-physical-transfer map are not selected by the current axioms.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
import sys

import numpy as np
from scipy.optimize import root
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
POLE_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_"
    "SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
IR_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
JOINT_LAW_NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_"
    "GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
TWO_STEP_NOTE_PATH = ROOT / "docs" / (
    "AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md"
)
PREMISE_REGISTRY_PATH = (
    ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"
)

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REGGE_REFLECTED_ORIENTATION_COMMON_METRIC_TRANSFER_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_JOINT_RECORD_GRAVITY_LAW_FIVE_CONTROL_AXIOM_CUT_GATE_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py",
    "scripts/admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11 as block47  # noqa: E402


HCOMPS = tuple(block47.HCOMPS)
ORIGINAL_DIRECTIONS = tuple(
    tuple(int(value) for value in direction) for direction in block47.DIRECTIONS
)
TIME_REFLECTION = np.diag((1, 1, 1, -1)).astype(int)
STATIC_MOMENTA = (0.05, 0.10, 0.20, 0.40, 0.80, np.pi / 2.0, 2.40, np.pi)
TRANSFER_MOMENTA = (0.10, 0.40, np.pi / 2.0, np.pi)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)


@dataclass(frozen=True)
class ReflectionUnion:
    directions: tuple[tuple[int, ...], ...]
    shifts: np.ndarray
    matrices: np.ndarray
    original_matrices: np.ndarray
    reflected_matrices: np.ndarray
    reflected_label_map: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]


@dataclass(frozen=True)
class MetricSector:
    name: str
    metric_basis: np.ndarray
    gauge_basis: np.ndarray


@dataclass(frozen=True)
class CommonPole:
    wave_number: float
    sector: str
    frequency: complex
    success: bool
    determinant_residual: float
    null_ratio: float
    next_ratio: float
    ward_relative: float


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def canonical_reflected_direction(
    direction: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    reflected = tuple(int(value) for value in TIME_REFLECTION @ np.asarray(direction))
    if reflected == (0, 0, 0, -1):
        return (0, 0, 0, 1), reflected
    return reflected, (0, 0, 0, 0)


def build_reflection_union() -> ReflectionUnion:
    reflected_map = tuple(
        canonical_reflected_direction(direction)
        for direction in ORIGINAL_DIRECTIONS
    )
    extra = sorted(
        {
            canonical
            for canonical, _ in reflected_map
            if canonical not in ORIGINAL_DIRECTIONS
        }
    )
    directions = ORIGINAL_DIRECTIONS + tuple(extra)
    index = {direction: slot for slot, direction in enumerate(directions)}
    size = len(directions)
    original_kernel: defaultdict[tuple[int, ...], np.ndarray] = defaultdict(
        lambda: np.zeros((size, size), dtype=float)
    )
    reflected_kernel: defaultdict[tuple[int, ...], np.ndarray] = defaultdict(
        lambda: np.zeros((size, size), dtype=float)
    )

    for shift, matrix in zip(
        block47.SHIFTS.astype(int), block47.MATRICES
    ):
        original_kernel[tuple(int(value) for value in shift)][:15, :15] += matrix
        reflected_shift = TIME_REFLECTION @ shift
        rows, columns = np.where(np.abs(matrix) > 1.0e-15)
        for row, column in zip(rows, columns):
            row_direction, row_offset = reflected_map[int(row)]
            column_direction, column_offset = reflected_map[int(column)]
            transformed_shift = tuple(
                int(value)
                for value in (
                    reflected_shift
                    + np.asarray(column_offset)
                    - np.asarray(row_offset)
                )
            )
            reflected_kernel[transformed_shift][
                index[row_direction], index[column_direction]
            ] += matrix[row, column]

    all_shifts = sorted(set(original_kernel) | set(reflected_kernel))
    original_matrices = np.asarray(
        [original_kernel[shift] for shift in all_shifts], dtype=float
    )
    reflected_matrices = np.asarray(
        [reflected_kernel[shift] for shift in all_shifts], dtype=float
    )
    return ReflectionUnion(
        directions=directions,
        shifts=np.asarray(all_shifts, dtype=float),
        matrices=0.5 * (original_matrices + reflected_matrices),
        original_matrices=original_matrices,
        reflected_matrices=reflected_matrices,
        reflected_label_map=reflected_map,
    )


def union_symbol(
    union: ReflectionUnion,
    momentum: np.ndarray,
    matrices: np.ndarray | None = None,
) -> np.ndarray:
    coefficients = union.matrices if matrices is None else matrices
    phases = np.exp(1j * (union.shifts @ np.asarray(momentum, dtype=complex)))
    return np.einsum("s,sij->ij", phases, coefficients, optimize=True)


def union_gauge_map(union: ReflectionUnion, momentum: np.ndarray) -> np.ndarray:
    directions = np.asarray(union.directions, dtype=float)
    lengths = np.linalg.norm(directions, axis=1)
    phases = np.exp(1j * (directions @ np.asarray(momentum, dtype=complex))) - 1.0
    return phases[:, None] * directions / lengths[:, None]


def metric_coefficients(directions: np.ndarray) -> np.ndarray:
    coefficients = np.zeros((len(directions), len(HCOMPS)), dtype=float)
    for row, direction in enumerate(np.asarray(directions, dtype=float)):
        length = float(np.linalg.norm(direction))
        for column, (left, right) in enumerate(HCOMPS):
            value = direction[left] * direction[right]
            if left != right:
                value *= 2.0
            coefficients[row, column] = value / (2.0 * length)
    return coefficients


def exact_reflection_fiber_ranks(
    union: ReflectionUnion,
) -> tuple[int, int, int, int]:
    """Return exact ranks for the shared, common, relative, and joint fibers."""

    def exact_metric(direction: tuple[int, ...]) -> sp.Matrix:
        squared_length = sum(value * value for value in direction)
        return sp.Matrix(
            [
                sp.Rational(
                    direction[left]
                    * direction[right]
                    * (2 if left != right else 1),
                    2,
                )
                / sp.sqrt(squared_length)
                for left, right in HCOMPS
            ]
        ).T

    original_index = {
        direction: slot for slot, direction in enumerate(ORIGINAL_DIRECTIONS)
    }
    reflected_labels = tuple(
        canonical for canonical, _ in union.reflected_label_map
    )
    reflected_index = {
        direction: slot for slot, direction in enumerate(reflected_labels)
    }
    original_metric = tuple(exact_metric(direction) for direction in ORIGINAL_DIRECTIONS)
    reflected_directions = tuple(
        tuple(int(value) for value in TIME_REFLECTION @ np.asarray(direction))
        for direction in ORIGINAL_DIRECTIONS
    )
    reflected_metric = tuple(exact_metric(direction) for direction in reflected_directions)
    shared = sorted(set(original_index) & set(reflected_index))
    shared_constraint = sp.Matrix.vstack(
        *(
            original_metric[original_index[direction]].row_join(
                -reflected_metric[reflected_index[direction]]
            )
            for direction in shared
        )
    )

    pair_to_union = sp.zeros(len(union.directions), 2 * len(HCOMPS))
    union_index = {
        direction: slot for slot, direction in enumerate(union.directions)
    }
    for direction, row in union_index.items():
        in_original = direction in original_index
        in_reflected = direction in reflected_index
        if in_original:
            factor = sp.Rational(1, 2) if in_reflected else sp.Integer(1)
            pair_to_union[row, : len(HCOMPS)] = (
                factor * original_metric[original_index[direction]]
            )
        if in_reflected:
            factor = sp.Rational(1, 2) if in_original else sp.Integer(1)
            pair_to_union[row, len(HCOMPS) :] = (
                factor * reflected_metric[reflected_index[direction]]
            )

    common_pairs = sp.zeros(2 * len(HCOMPS), len(HCOMPS))
    common_pairs[: len(HCOMPS), :] = sp.eye(len(HCOMPS))
    common_pairs[len(HCOMPS) :, :] = sp.eye(len(HCOMPS))
    relative_pairs = sp.zeros(2 * len(HCOMPS), 3)
    for column, spatial in enumerate(range(3)):
        component = HCOMPS.index((spatial, 3))
        relative_pairs[component, column] = 1
        relative_pairs[len(HCOMPS) + component, column] = -1

    common_fiber = pair_to_union * common_pairs
    relative_fiber = pair_to_union * relative_pairs
    return (
        int(shared_constraint.rank()),
        int(common_fiber.rank()),
        int(relative_fiber.rank()),
        int(common_fiber.row_join(relative_fiber).rank()),
    )


def union_time_reflection_matrix(
    union: ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    reflected_momentum = TIME_REFLECTION @ np.asarray(momentum, dtype=complex)
    transformation = np.zeros(
        (len(union.directions), len(union.directions)), dtype=complex
    )
    for column, direction in enumerate(union.directions):
        reflected = tuple(
            int(value) for value in TIME_REFLECTION @ np.asarray(direction)
        )
        if reflected in index:
            canonical = reflected
            offset = (0, 0, 0, 0)
        else:
            canonical = tuple(-np.asarray(reflected))
            offset = reflected
        transformation[index[canonical], column] = np.exp(
            -1j * np.dot(reflected_momentum, offset)
        )
    return transformation


def union_reflection_split(
    union: ReflectionUnion,
) -> tuple[tuple[np.ndarray, np.ndarray, np.ndarray], np.ndarray]:
    original_metric = metric_coefficients(np.asarray(ORIGINAL_DIRECTIONS))
    reflected_directions = np.asarray(
        [TIME_REFLECTION @ np.asarray(direction) for direction in ORIGINAL_DIRECTIONS]
    )
    reflected_metric = metric_coefficients(reflected_directions)
    original_index = {
        direction: slot for slot, direction in enumerate(ORIGINAL_DIRECTIONS)
    }
    reflected_index = {
        canonical: slot
        for slot, (canonical, _) in enumerate(union.reflected_label_map)
    }
    shared = sorted(set(original_index) & set(reflected_index))
    shared_constraint = np.asarray(
        [
            np.concatenate(
                (
                    original_metric[original_index[direction]],
                    -reflected_metric[reflected_index[direction]],
                )
            )
            for direction in shared
        ]
    )

    pair_to_union = np.zeros((len(union.directions), 2 * len(HCOMPS)), dtype=float)
    union_index = {
        direction: slot for slot, direction in enumerate(union.directions)
    }
    for direction, slot in union_index.items():
        in_original = direction in original_index
        in_reflected = direction in reflected_index
        if in_original and in_reflected:
            pair_to_union[slot, : len(HCOMPS)] = (
                0.5 * original_metric[original_index[direction]]
            )
            pair_to_union[slot, len(HCOMPS) :] = (
                0.5 * reflected_metric[reflected_index[direction]]
            )
        elif in_original:
            pair_to_union[slot, : len(HCOMPS)] = original_metric[
                original_index[direction]
            ]
        elif in_reflected:
            pair_to_union[slot, len(HCOMPS) :] = reflected_metric[
                reflected_index[direction]
            ]
        else:
            raise AssertionError("union direction belongs to neither orientation")
    return (shared_constraint, pair_to_union, original_metric), reflected_metric


def matrix_null_basis(matrix: np.ndarray, tolerance: float = 1.0e-12) -> np.ndarray:
    _, singular_values, right_vectors = np.linalg.svd(matrix, full_matrices=True)
    rank = int(np.sum(singular_values > tolerance))
    return right_vectors.conj().T[:, rank:]


def swap_matrix_for_directions(directions: tuple[tuple[int, ...], ...]) -> np.ndarray:
    index = {direction: slot for slot, direction in enumerate(directions)}
    swap = np.zeros((len(directions), len(directions)), dtype=float)
    for column, direction in enumerate(directions):
        image = list(direction)
        image[1], image[2] = image[2], image[1]
        swap[index[tuple(image)], column] = 1.0
    return swap


def sign_basis(involution: np.ndarray, sign: int) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(involution)
    return eigenvectors[:, np.isclose(eigenvalues, float(sign))]


def metric_sectors() -> tuple[MetricSector, ...]:
    metric_swap = np.zeros((len(HCOMPS), len(HCOMPS)), dtype=float)
    for column, (left, right) in enumerate(HCOMPS):
        mapped = tuple(
            sorted(
                (
                    {1: 2, 2: 1}.get(left, left),
                    {1: 2, 2: 1}.get(right, right),
                )
            )
        )
        metric_swap[HCOMPS.index(mapped), column] = 1.0
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    return (
        MetricSector(
            "even", sign_basis(metric_swap, +1), sign_basis(gauge_swap, +1)
        ),
        MetricSector(
            "odd", sign_basis(metric_swap, -1), sign_basis(gauge_swap, -1)
        ),
    )


NONMETRIC = block47.nonmetric_basis()
METRIC_TIME_REFLECTION = np.diag(
    [
        -1.0 if 3 in (left, right) and left != right else 1.0
        for left, right in HCOMPS
    ]
)


def original_metric_schur(momentum: np.ndarray) -> np.ndarray:
    symbol = block47.analytic_symbol(momentum)
    right_metric = block47.analytic_metric_map(momentum)
    left_metric = block47.analytic_metric_map(-momentum).T
    nonmetric_block = NONMETRIC.T @ symbol @ NONMETRIC
    return left_metric @ symbol @ right_metric - (
        left_metric @ symbol @ NONMETRIC
    ) @ np.linalg.solve(
        nonmetric_block, NONMETRIC.T @ symbol @ right_metric
    )


def metric_gauge_map(momentum: np.ndarray) -> np.ndarray:
    return np.linalg.lstsq(
        block47.analytic_metric_map(momentum),
        block47.analytic_gauge_map(momentum),
        rcond=None,
    )[0]


def common_metric_operator(momentum: np.ndarray) -> np.ndarray:
    reflected_momentum = TIME_REFLECTION @ np.asarray(momentum, dtype=complex)
    return 0.5 * (
        original_metric_schur(momentum)
        + METRIC_TIME_REFLECTION
        @ original_metric_schur(reflected_momentum)
        @ METRIC_TIME_REFLECTION
    )


def common_bordered_operator(
    wave_number: float, frequency: complex, sector: MetricSector
) -> np.ndarray:
    momentum = np.asarray((wave_number, 0.0, 0.0, -1j * frequency), dtype=complex)
    operator = common_metric_operator(momentum)
    right_gauge = sector.metric_basis.T @ metric_gauge_map(momentum) @ sector.gauge_basis
    left_gauge = sector.metric_basis.T @ metric_gauge_map(-momentum) @ sector.gauge_basis
    reduced = sector.metric_basis.T @ operator @ sector.metric_basis
    zeros = np.zeros(
        (sector.gauge_basis.shape[1], sector.gauge_basis.shape[1]), dtype=complex
    )
    return np.block([[reduced, left_gauge], [right_gauge.T, zeros]])


def solve_common_pole(wave_number: float, sector: MetricSector) -> CommonPole:
    initial = block47.scalar_lattice_frequency(wave_number)
    scale = float(np.linalg.norm(common_bordered_operator(wave_number, initial, sector)))

    def determinant_pair(values: np.ndarray) -> np.ndarray:
        frequency = complex(values[0], values[1])
        determinant = np.linalg.det(
            common_bordered_operator(wave_number, frequency, sector) / scale
        )
        return np.asarray((determinant.real, determinant.imag))

    result = root(
        determinant_pair,
        np.asarray((initial, 0.0)),
        method="hybr",
        options={"xtol": 1.0e-11},
    )
    frequency = complex(result.x[0], result.x[1])
    bordered = common_bordered_operator(wave_number, frequency, sector)
    singular_values = np.linalg.svd(bordered, compute_uv=False)
    momentum = np.asarray((wave_number, 0.0, 0.0, -1j * frequency), dtype=complex)
    operator = common_metric_operator(momentum)
    gauge = metric_gauge_map(momentum)
    ward_relative = float(np.linalg.norm(operator @ gauge)) / (
        float(np.linalg.norm(operator)) * float(np.linalg.norm(gauge))
    )
    return CommonPole(
        wave_number=wave_number,
        sector=sector.name,
        frequency=frequency,
        success=bool(result.success),
        determinant_residual=float(np.linalg.norm(result.fun)),
        null_ratio=float(singular_values[-1] / singular_values[0]),
        next_ratio=float(singular_values[-2] / singular_values[0]),
        ward_relative=ward_relative,
    )


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def main() -> int:
    checks = Checks()
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    pole_note = flat(POLE_NOTE_PATH)
    ir_note = flat(IR_NOTE_PATH)
    joint_note = flat(JOINT_LAW_NOTE_PATH)
    two_step_note = flat(TWO_STEP_NOTE_PATH)

    checks.check(
        "source-and-scope-bindings",
        "the current axioms, gravity parents, joint-law cut, and bounded two-step precedent are read without importing a physical transfer",
        all(
            path.exists()
            for path in (
                NOTE_PATH,
                AXIOM_PATH,
                POLE_NOTE_PATH,
                IR_NOTE_PATH,
                JOINT_LAW_NOTE_PATH,
                TWO_STEP_NOTE_PATH,
                PREMISE_REGISTRY_PATH,
            )
        )
        and "sampled finite-frequency survival" in pole_note
        and "four gauge directions plus two" in ir_note
        and "exact immutable referent" in joint_note
        and "action-to-physical" in two_step_note
        and "does not choose a hamiltonian or transfer operator" in axiom,
    )

    original_sectors = block47.sector_data()[0]
    original_poles = tuple(
        block47.solve_pole(wave_number, sector)
        for wave_number in (0.4, np.pi / 2.0)
        for sector in original_sectors
    )
    original_phases = [abs(frequency.imag) for frequency, _, _ in original_poles]
    transfer_imaginary = [
        abs(np.exp(-frequency).imag) for frequency, _, _ in original_poles
    ]
    checks.check(
        "single-orientation-positive-transfer-obstruction",
        "the direct lambda=exp(-omega) identification has a nonreal eigenvalue and therefore cannot be a positive self-adjoint one-step transfer",
        all(success for _, success, _ in original_poles)
        and max(original_phases) > 6.0e-4
        and max(transfer_imaginary) > 1.0e-4,
        f"max |Im omega|={max(original_phases):.6e}; max |Im exp(-omega)|={max(transfer_imaginary):.6e}",
    )

    union = build_reflection_union()
    original_types = set(ORIGINAL_DIRECTIONS)
    reflected_types = {
        canonical for canonical, _ in union.reflected_label_map
    }
    shared_types = original_types & reflected_types
    coefficient_lookup = {
        tuple(int(value) for value in shift): matrix
        for shift, matrix in zip(union.shifts, union.matrices)
    }
    pairing_error = max(
        float(
            np.max(
                np.abs(
                    matrix.T
                    - coefficient_lookup[tuple(-int(value) for value in shift)]
                )
            )
        )
        for shift, matrix in zip(union.shifts, union.matrices)
    )
    checks.check(
        "minimal-local-reflection-union",
        "time reflection glues eight shared edge classes and adds seven reflected mixed diagonals to the original fifteen",
        len(union.directions) == 22
        and len(shared_types) == 8
        and len(original_types - reflected_types) == 7
        and len(reflected_types - original_types) == 7
        and len(union.shifts) == 133
        and pairing_error < 5.0e-15,
        f"edges=22; shared=8; unique=7+7; shifts=133; pair error={pairing_error:.3e}",
    )

    reflection_error = 0.0
    involution_error = 0.0
    for momentum in (
        np.asarray((0.3, 0.2, -0.1, 0.4), dtype=complex),
        np.asarray((0.4, 0.0, 0.0, -0.395j), dtype=complex),
        np.asarray((1.2, -0.2, 0.4, 0.7), dtype=complex),
    ):
        reflected_momentum = TIME_REFLECTION @ momentum
        transformation = union_time_reflection_matrix(union, momentum)
        reflection_error = max(
            reflection_error,
            float(
                np.max(
                    np.abs(
                        union_symbol(union, momentum)
                        - union_time_reflection_matrix(union, -momentum).T
                        @ union_symbol(union, reflected_momentum)
                        @ transformation
                    )
                )
            ),
        )
        involution_error = max(
            involution_error,
            float(
                np.max(
                    np.abs(
                        union_time_reflection_matrix(union, reflected_momentum)
                        @ transformation
                        - np.eye(22)
                    )
                )
            ),
        )
    checks.check(
        "exact-union-time-reflection",
        "the 22-edge union symbol has an explicit momentum-dependent time-reflection involution and exact covariance",
        reflection_error < 5.0e-14 and involution_error < 1.0e-14,
        f"covariance error={reflection_error:.3e}; involution error={involution_error:.3e}",
    )

    ward_error = 0.0
    gauge_ranks = set()
    for momentum in (
        np.asarray((0.3, 0.2, -0.1, 0.4), dtype=complex),
        np.asarray((0.4, 0.0, 0.0, 0.7), dtype=complex),
        np.asarray((0.4, 0.0, 0.0, -0.395j), dtype=complex),
    ):
        symbol = union_symbol(union, momentum)
        right_gauge = union_gauge_map(union, momentum)
        left_gauge = union_gauge_map(union, -momentum)
        ward_error = max(
            ward_error,
            float(np.max(np.abs(symbol @ right_gauge))),
            float(np.max(np.abs(left_gauge.T @ symbol))),
        )
        gauge_ranks.add(int(np.linalg.matrix_rank(right_gauge, tol=1.0e-10)))
    checks.check(
        "reflected-union-displacement-ward",
        "the local reflection completion preserves all four exact two-sided displacement columns at real and complex momentum",
        ward_error < 5.0e-13 and gauge_ranks == {4},
        f"max absolute Ward residual={ward_error:.3e}; ranks={sorted(gauge_ranks)}",
    )

    (shared_constraint, pair_to_union, _), _ = union_reflection_split(union)
    pair_null = matrix_null_basis(shared_constraint)
    fiber_metric_family = pair_to_union @ pair_null
    union_metric = metric_coefficients(np.asarray(union.directions))
    zero_symbol = union_symbol(union, np.zeros(4))
    exact_fiber_ranks = exact_reflection_fiber_ranks(union)
    checks.check(
        "constant-metric-fiber-dimension",
        "the two ten-component orientation metrics agree on a rank-seven shared-edge image, leaving a thirteen-dimensional flat fiber",
        shared_constraint.shape == (8, 20)
        and np.linalg.matrix_rank(shared_constraint, tol=1.0e-12) == 7
        and exact_fiber_ranks == (7, 10, 3, 13)
        and pair_null.shape == (20, 13)
        and np.linalg.matrix_rank(fiber_metric_family, tol=1.0e-12) == 13
        and np.linalg.matrix_rank(union_metric, tol=1.0e-12) == 10
        and np.max(np.abs(zero_symbol @ fiber_metric_family)) < 8.0e-14
        and inertia(zero_symbol) == (7, 2, 13),
        f"exact ranks={exact_fiber_ranks}; flat fiber=13; Q0 inertia=(7,2,13)",
    )

    relative_pairs = np.zeros((20, 3), dtype=float)
    for column, spatial in enumerate(range(3)):
        component = HCOMPS.index((spatial, 3))
        relative_pairs[component, column] = 1.0
        relative_pairs[len(HCOMPS) + component, column] = -1.0
    relative_shifts = pair_to_union @ relative_pairs
    checks.check(
        "three-relative-shift-flat-modes",
        "the excess flat fiber is exactly three independent forward/backward mixed-time metric differences beyond one common metric",
        np.max(np.abs(shared_constraint @ relative_pairs)) < 1.0e-15
        and np.linalg.matrix_rank(relative_shifts, tol=1.0e-12) == 3
        and np.linalg.matrix_rank(
            np.column_stack((union_metric, relative_shifts)), tol=1.0e-12
        )
        == 13
        and np.max(np.abs(zero_symbol @ relative_shifts)) < 8.0e-14,
        f"rank(relative shifts)={np.linalg.matrix_rank(relative_shifts)}; residual={np.max(np.abs(zero_symbol @ relative_shifts)):.3e}",
    )

    original_zero = union_symbol(union, np.zeros(4), union.original_matrices)
    reflected_zero = union_symbol(union, np.zeros(4), union.reflected_matrices)
    separable_residual = max(
        float(np.max(np.abs(original_zero @ fiber_metric_family))),
        float(np.max(np.abs(reflected_zero @ fiber_metric_family))),
    )
    checks.check(
        "orientation-separable-coefficients-cannot-lift",
        "each orientation-local flat action annihilates the full thirteen-dimensional fiber, so retuning their two coefficients cannot remove the excess",
        separable_residual < 2.0e-13,
        f"max component-action flat-fiber residual={separable_residual:.3e}",
    )

    static_inertias = set()
    static_nullities = set()
    gauge_plus_null_ranks = set()
    static_next_gap = np.inf
    for wave_number in STATIC_MOMENTA:
        momentum = np.asarray((wave_number, 0.0, 0.0, 0.0))
        symbol = union_symbol(union, momentum)
        singular_values = np.linalg.svd(symbol, compute_uv=False)
        null_basis = matrix_null_basis(symbol, tolerance=1.0e-9)
        gauge = union_gauge_map(union, momentum)
        static_inertias.add(inertia(symbol))
        static_nullities.add(null_basis.shape[1])
        gauge_plus_null_ranks.add(
            int(np.linalg.matrix_rank(np.column_stack((gauge, null_basis)), 1.0e-9))
        )
        static_next_gap = min(static_next_gap, float(singular_values[-6]))
    checks.check(
        "sampled-static-fifth-null-branch",
        "the reflected local union has four gauge nulls plus one extra exact static null at every declared nonzero axis momentum",
        static_inertias == {(14, 3, 5)}
        and static_nullities == {5}
        and gauge_plus_null_ranks == {5}
        and static_next_gap > 4.0e-4,
        f"inertia={sorted(static_inertias)}; nullity={sorted(static_nullities)}; next gap={static_next_gap:.3e}",
    )

    metric_reflection_error = 0.0
    common_ward = 0.0
    for momentum in (
        np.asarray((0.4, 0.0, 0.0, 0.7), dtype=complex),
        np.asarray((0.4, 0.0, 0.0, -0.395j), dtype=complex),
    ):
        reflected_momentum = TIME_REFLECTION @ momentum
        operator = common_metric_operator(momentum)
        metric_reflection_error = max(
            metric_reflection_error,
            float(
                np.max(
                    np.abs(
                        operator
                        - METRIC_TIME_REFLECTION
                        @ common_metric_operator(reflected_momentum)
                        @ METRIC_TIME_REFLECTION
                    )
                )
            ),
        )
        common_ward = max(
            common_ward,
            float(np.max(np.abs(operator @ metric_gauge_map(momentum)))),
            float(np.max(np.abs(metric_gauge_map(-momentum).T @ operator))),
        )
    checks.check(
        "common-metric-reflection-and-ward-repair",
        "identifying the two orientation metrics before averaging gives an exactly time-reflection-covariant gauge operator",
        metric_reflection_error < 5.0e-14 and common_ward < 5.0e-12,
        f"reflection error={metric_reflection_error:.3e}; Ward residual={common_ward:.3e}",
    )

    sectors = metric_sectors()
    common_poles = tuple(
        solve_common_pole(wave_number, sector)
        for wave_number in TRANSFER_MOMENTA
        for sector in sectors
    )
    max_pole_phase = max(abs(pole.frequency.imag) for pole in common_poles)
    max_root_residual = max(pole.determinant_residual for pole in common_poles)
    max_null_ratio = max(pole.null_ratio for pole in common_poles)
    min_next_ratio = min(pole.next_ratio for pole in common_poles)
    max_pole_ward = max(pole.ward_relative for pole in common_poles)
    checks.check(
        "common-metric-real-two-mode-poles",
        "the common-metric reflected candidate has one real positive tensor pole in each sector at all four declared momenta",
        len(common_poles) == 8
        and all(pole.success for pole in common_poles)
        and all(pole.frequency.real > 0.0 for pole in common_poles)
        and max_pole_phase < 1.0e-11
        and max_root_residual < 1.0e-12
        and max_null_ratio < 5.0e-13
        and min_next_ratio > 2.0e-8
        and max_pole_ward < 3.0e-12,
        f"phase={max_pole_phase:.3e}; null={max_null_ratio:.3e}; next={min_next_ratio:.3e}; Ward={max_pole_ward:.3e}",
    )

    two_step_eigenvalues = np.asarray(
        [np.exp(-2.0 * pole.frequency.real) for pole in common_poles]
    )
    static_residues = []
    source = np.zeros(len(HCOMPS), dtype=float)
    static_index = HCOMPS.index((3, 3))
    source[static_index] = 1.0
    for wave_number in (0.025, 0.05, 0.10, 0.20):
        operator = common_metric_operator(
            np.asarray((wave_number, 0.0, 0.0, 0.0), dtype=complex)
        )
        response = -np.linalg.pinv(operator, rcond=1.0e-10) @ source
        static_residues.append(
            float((wave_number**2 * response[static_index]).real)
        )
    checks.check(
        "conditional-positive-two-step-spectral-candidate",
        "choosing the decaying branches gives a positive Hermitian two-mode diagonal kernel while retaining the infrared static residue",
        np.all(two_step_eigenvalues > 0.0)
        and np.all(two_step_eigenvalues < 1.0)
        and max(abs(value - 2.0) for value in static_residues) < 2.0e-2
        and abs(static_residues[0] - 2.0) < 1.0e-4,
        f"lambda_2 range={two_step_eigenvalues.min():.6f}..{two_step_eigenvalues.max():.6f}; k^2 h_tt={static_residues}",
    )

    checks.check(
        "physical-transfer-and-axiom-boundary",
        "the source identifies orientation-shift gluing and decaying-branch/inner-product selection as exact missing law content",
        all(
            phrase in note
            for phrase in (
                "three-component orientation-shift intertwiner",
                "action-to-physical-transfer",
                "no canonical axiom is edited",
                "no toe percentage moves",
                "not a gravity no-go",
            )
        )
        and all(
            phrase in axiom
            for phrase in (
                "does not choose a hamiltonian or transfer operator",
                "time metric",
                "update laws",
            )
        ),
    )

    checks.check(
        "fresh-no-go-discipline-packet",
        "the direct-transfer and separable-reflection negatives pass N1 through N8 while retaining the common-metric and exact-law routes",
        all(f"### n{index}" in note for index in range(1, 9))
        and "status: pass" in note
        and all(
            phrase in note
            for phrase in (
                "alternating-orientation",
                "metric-first carrier",
                "unitary dilation",
                "not proved necessary",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: fifteen original edges, fifteen reflected labels, twenty-two union edges, eight shared classes, 133 shifts, ten common metric coordinates, three relative shifts, eight static probes, and eight common-metric pole solves are resolved"
    )
    print(
        "per_element: checked every reflected edge label, every union Laurent coefficient, all ten metric coordinates, and all three relative shifts"
    )
    print(
        "per_site: checked the local original-plus-time-reflected unit-cell union and its exact reflection involution"
    )
    print(
        "per_mode: checked single-orientation complex poles, eight nonzero static union momenta, and two common-metric sectors at four momenta"
    )
    print(
        "per_block: checked the 13-versus-10 constant flat fiber, sampled fifth static branch, common-metric Ward repair, and conditional two-step spectrum"
    )
    print(
        "lattice_wide: no alternating full-Z3 complex, OS half-space form, local physical Hilbert map, nonlinear constraints, or Record-clock update is inferred"
    )
    print(
        "scope_boundary: direct single-orientation positive-transfer obstruction and separable-reflection shift-glue boundary with a conditional common-metric repair; not gravity failure, selected law, axiom adoption, or TOE closure"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
