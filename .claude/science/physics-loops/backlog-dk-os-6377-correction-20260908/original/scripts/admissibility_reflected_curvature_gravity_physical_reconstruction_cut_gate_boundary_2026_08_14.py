#!/usr/bin/env python3
"""Block 75: discriminate the shortest physical gravity reconstructions.

The runner keeps the complete twenty-two-edge reflected action from Block 74.
It resolves a finite-frequency collision between a positive tensor-like pole
and an opposite-residue companion, tests two explicit canonical reductions,
and checks the rank-minimal auxiliary/connection rewrite.  The result is a
boundary on these supplied interfaces, not a no-go for canonical, connection,
or lattice gravity.
"""

from __future__ import annotations

from dataclasses import dataclass
import os
from pathlib import Path
import sys

import numpy as np
from scipy.linalg import null_space
from scipy.optimize import root


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_"
    "CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK49_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_"
    "INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK50_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_"
    "SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK53_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_"
    "UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK68_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK74_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_"
    "TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_GRAVITY_PHYSICAL_RECONSTRUCTION_CUT_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REFLECTED_PLAQUETTE_CURVATURE_RECORD_RICCI_SOURCE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_FINITE_FREQUENCY_POLE_SURVIVAL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CYCLE713_RECORD_STRESS_BLOCK44_IR_REFLECTED_CARRIER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_REFLECTED_CURVATURE_ACTION_RECORD_SOURCE_TWO_STEP_TRANSFER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11.py",
    "scripts/admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py",
    "scripts/admissibility_reflected_curvature_gravity_physical_reconstruction_cut_gate_boundary_2026_08_14.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_repaired_regge_full_edge_schur_ir_lorentzian_constraint_tt_boundary_2026_08_11 as block44  # noqa: E402
import admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11 as block48  # noqa: E402
import admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11 as block49  # noqa: E402
import admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11 as block53  # noqa: E402
import admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14 as block74  # noqa: E402


MU_VALUES = (1.0 / 2048.0, 1.0 / 1024.0, 2.0 / 1024.0)
MU = MU_VALUES[1]
OUTER_POLES = (
    (1.25, (1.118, 1.159)),
    (1.32, (1.116, 1.160)),
)
COMPLEX_POLES = (
    (1.27, 1.138 + 0.008j, 1.138 - 0.008j),
    (1.28, 1.138 + 0.012j, 1.138 - 0.012j),
    (1.29, 1.138 + 0.012j, 1.138 - 0.012j),
    (1.30, 1.138 + 0.006j, 1.138 - 0.006j),
)
GRID_SIZE = 9
KINETIC_STEP = 1.0e-3


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 168 else detail[:165] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


@dataclass(frozen=True)
class Sector:
    name: str
    edge_basis: np.ndarray
    gauge_basis: np.ndarray
    observable: np.ndarray
    tt_vector: np.ndarray


@dataclass(frozen=True)
class PoleDatum:
    wave_number: float
    frequency: complex
    solver_success: bool
    determinant_residual: float
    bordered_null_ratio: float
    next_singular_ratio: float
    multiplier_ratio: float
    edge_null_ratio: float
    spectral_weights: tuple[complex, complex]


@dataclass(frozen=True)
class DiracCertificate:
    ranks: tuple[int, int, int, int, int]
    inertias: tuple[tuple[int, int, int], ...]
    repaired_constraint_norm: float
    einstein_constraint_rank: int
    einstein_constraint_norm: float
    quotient_eigenvalues: tuple[float, float, float]
    tt_scalar_mixing: float
    source_components: tuple[float, float, float]
    source_eigencomponents: tuple[float, float, float]
    source_ward: float


@dataclass(frozen=True)
class ZoneCertificate:
    modes: int
    gauge_identity_error: float
    tt_dimensions: tuple[int, ...]
    negative_counts: tuple[tuple[int, int], ...]
    minimum_static: tuple[float, ...]
    minimum_kinetic: tuple[float, ...]
    hostile_static: tuple[float, float]
    hostile_kinetic: tuple[float, float]


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def matrix_rank(matrix: np.ndarray, tolerance: float = 1.0e-9) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tolerance))


def inertia(matrix: np.ndarray, tolerance: float = 1.0e-9) -> tuple[int, int, int]:
    eigenvalues = np.linalg.eigvalsh(0.5 * (matrix + matrix.conj().T))
    return (
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(np.abs(eigenvalues) <= tolerance)),
    )


def spatial_embedding() -> tuple[np.ndarray, tuple[np.ndarray, ...]]:
    pairs = ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2))
    embedding = np.zeros((len(block48.HCOMPS), 6), dtype=float)
    tensors = []
    for column, pair in enumerate(pairs):
        value = 1.0 if pair[0] == pair[1] else 1.0 / np.sqrt(2.0)
        embedding[block48.HCOMPS.index(pair), column] = value
        tensor = np.zeros((3, 3), dtype=float)
        tensor[pair] = value
        if pair[0] != pair[1]:
            tensor[pair[::-1]] = value
        tensors.append(tensor)
    return embedding, tuple(tensors)


SPATIAL_EMBEDDING, SPATIAL_TENSORS = spatial_embedding()
TEMPORAL_EMBEDDING = np.zeros((len(block48.HCOMPS), 4), dtype=float)
for _column, _pair in enumerate(((3, 3), (0, 3), (1, 3), (2, 3))):
    TEMPORAL_EMBEDDING[block48.HCOMPS.index(_pair), _column] = 1.0


def swap_matrix(vectors: np.ndarray, left: int, right: int) -> np.ndarray:
    integer_vectors = np.asarray(vectors, dtype=int)
    result = np.zeros((len(integer_vectors), len(integer_vectors)), dtype=float)
    for column, vector in enumerate(integer_vectors):
        image = vector.copy()
        image[left], image[right] = image[right], image[left]
        matches = np.flatnonzero(np.all(integer_vectors == image, axis=1))
        if len(matches) != 1:
            raise AssertionError("coordinate-swap image is not unique")
        result[matches[0], column] = 1.0
    return result


def sign_basis(involution: np.ndarray, sign: int) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(involution)
    return eigenvectors[:, np.isclose(eigenvalues, float(sign))]


def sector_data(
    union: block48.ReflectionUnion,
) -> tuple[tuple[Sector, Sector], np.ndarray, np.ndarray]:
    directions = np.asarray(union.directions, dtype=int)
    edge_swap = swap_matrix(directions, 1, 2)
    gauge_swap = np.eye(4)
    gauge_swap[[1, 2]] = gauge_swap[[2, 1]]
    plus, cross = block74.local_tt_observables(union, "")

    tt_cross = np.zeros(len(block48.HCOMPS), dtype=float)
    tt_cross[block48.HCOMPS.index((1, 2))] = 1.0 / np.sqrt(2.0)
    tt_plus = np.zeros(len(block48.HCOMPS), dtype=float)
    tt_plus[block48.HCOMPS.index((1, 1))] = 1.0 / np.sqrt(2.0)
    tt_plus[block48.HCOMPS.index((2, 2))] = -1.0 / np.sqrt(2.0)

    sectors = (
        Sector(
            "even",
            sign_basis(edge_swap, +1),
            sign_basis(gauge_swap, +1),
            cross,
            tt_cross,
        ),
        Sector(
            "odd",
            sign_basis(edge_swap, -1),
            sign_basis(gauge_swap, -1),
            plus,
            tt_plus,
        ),
    )
    return sectors, edge_swap, gauge_swap


def action_symbol(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mu: float = MU,
) -> np.ndarray:
    return block74.cross_action_symbol(union, momentum, mu, "")


def axis_momentum(wave_number: float, frequency: complex) -> np.ndarray:
    return np.asarray((wave_number, 0.0, 0.0, -1j * frequency), dtype=complex)


def bordered_operator(
    union: block48.ReflectionUnion,
    wave_number: float,
    frequency: complex,
    sector: Sector,
) -> np.ndarray:
    momentum = axis_momentum(wave_number, frequency)
    symbol = -action_symbol(union, momentum)
    right_gauge = (
        sector.edge_basis.T
        @ block48.union_gauge_map(union, momentum)
        @ sector.gauge_basis
    )
    left_gauge = (
        sector.edge_basis.T
        @ block48.union_gauge_map(union, -momentum)
        @ sector.gauge_basis
    )
    reduced = sector.edge_basis.T @ symbol @ sector.edge_basis
    zeros = np.zeros(
        (sector.gauge_basis.shape[1], sector.gauge_basis.shape[1]), dtype=complex
    )
    return np.block([[reduced, left_gauge], [right_gauge.T, zeros]])


def solve_pole(
    union: block48.ReflectionUnion,
    wave_number: float,
    initial: complex,
    sector: Sector,
) -> tuple[complex, bool, float]:
    scale = float(np.linalg.norm(bordered_operator(union, wave_number, initial, sector)))

    def determinant_pair(values: np.ndarray) -> np.ndarray:
        frequency = complex(values[0], values[1])
        determinant = np.linalg.det(
            bordered_operator(union, wave_number, frequency, sector) / scale
        )
        return np.asarray((determinant.real, determinant.imag), dtype=float)

    result = root(
        determinant_pair,
        np.asarray((initial.real, initial.imag), dtype=float),
        method="hybr",
        options={"xtol": 1.0e-12},
    )
    return complex(result.x[0], result.x[1]), bool(result.success), float(
        np.linalg.norm(result.fun)
    )


def analytic_covariance(
    union: block48.ReflectionUnion,
    wave_number: float,
    frequency: complex,
    observable: np.ndarray,
) -> complex:
    momentum = axis_momentum(wave_number, frequency)
    symbol = -action_symbol(union, momentum)
    right_gauge = block48.union_gauge_map(union, momentum)
    left_gauge = block48.union_gauge_map(union, -momentum)
    bordered = np.block(
        [
            [symbol, left_gauge],
            [right_gauge.T, np.zeros((4, 4), dtype=complex)],
        ]
    )
    response = np.linalg.solve(
        bordered, np.concatenate((observable, np.zeros(4, dtype=complex)))
    )
    return complex(observable.T @ response[: len(union.directions)])


def pole_datum(
    union: block48.ReflectionUnion,
    wave_number: float,
    initial: complex,
    sector: Sector,
    mutation: str,
) -> PoleDatum:
    frequency, success, determinant_residual = solve_pole(
        union, wave_number, initial, sector
    )
    momentum = axis_momentum(wave_number, frequency)
    symbol = -action_symbol(union, momentum)
    bordered = bordered_operator(union, wave_number, frequency, sector)
    _, singular_values, right_vectors = np.linalg.svd(bordered)
    null_vector = right_vectors.conj().T[:, -1]
    edge_count = sector.edge_basis.shape[1]
    sector_edge = null_vector[:edge_count]
    multipliers = null_vector[edge_count:]
    edge_vector = sector.edge_basis @ sector_edge
    edge_vector /= np.linalg.norm(edge_vector)

    delta = 1.0e-7
    weights = tuple(
        -(sign * delta)
        * analytic_covariance(
            union, wave_number, frequency + sign * delta, sector.observable
        )
        for sign in (-1, +1)
    )
    if mutation == "flip_residue":
        weights = tuple(-value for value in weights)

    return PoleDatum(
        wave_number=wave_number,
        frequency=frequency,
        solver_success=success,
        determinant_residual=determinant_residual,
        bordered_null_ratio=float(singular_values[-1] / singular_values[0]),
        next_singular_ratio=float(singular_values[-2] / singular_values[0]),
        multiplier_ratio=float(
            np.linalg.norm(multipliers) / np.linalg.norm(sector_edge)
        ),
        edge_null_ratio=float(np.linalg.norm(symbol @ edge_vector) / np.linalg.norm(symbol)),
        spectral_weights=(complex(weights[0]), complex(weights[1])),
    )


def constant_nonmetric_schur(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    nonmetric: np.ndarray,
    mu: float,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    q = np.asarray(momentum, dtype=complex)
    symbol = action_symbol(union, q, mu)
    metric = block49.union_line_metric_map(union, q)
    left_metric = block49.union_line_metric_map(union, -q).T
    complement = nonmetric.T @ symbol @ nonmetric
    effective = (
        left_metric @ symbol @ metric
        - left_metric
        @ symbol
        @ nonmetric
        @ np.linalg.solve(complement, nonmetric.T @ symbol @ metric)
    )
    return effective, complement, symbol


def dirac_certificate(
    union: block48.ReflectionUnion,
    mutation: str,
) -> DiracCertificate:
    momentum = np.asarray((0.4, 0.0, 0.0, 0.0), dtype=complex)
    metric_zero = block49.union_line_metric_map(union, np.zeros(4))
    nonmetric = null_space(metric_zero.T, rcond=1.0e-12)
    effective, complement, symbol = constant_nonmetric_schur(
        union, momentum, nonmetric, MU
    )

    spatial = SPATIAL_EMBEDDING
    temporal = TEMPORAL_EMBEDDING
    spatial_block = spatial.T @ effective @ spatial
    mixing = spatial.T @ effective @ temporal
    temporal_block = temporal.T @ effective @ temporal
    temporal_inverse = np.linalg.pinv(temporal_block, rcond=1.0e-10)
    reduced = spatial_block - mixing @ temporal_inverse @ mixing.conj().T

    repaired_left_null = null_space(
        temporal_block.conj().T, rcond=1.0e-10
    )
    repaired_constraint_norm = float(
        np.linalg.norm(repaired_left_null.conj().T @ (temporal.T @ effective @ spatial))
    )

    einstein = -0.5 * block44.einstein_action_pairing(
        np.asarray((0.4, 0.0, 0.0, 0.0)), np.eye(4)
    )
    einstein_temporal = temporal.T @ einstein @ temporal
    einstein_left_null = null_space(
        einstein_temporal.conj().T, rcond=1.0e-10
    )
    einstein_constraints = (
        einstein_left_null.conj().T @ (temporal.T @ einstein @ spatial)
    )

    plus = np.asarray((0.0, 1.0, -1.0, 0.0, 0.0, 0.0)) / np.sqrt(2.0)
    cross = np.asarray((0.0, 0.0, 0.0, 0.0, 0.0, 1.0))
    scalar = np.asarray((0.0, 1.0, 1.0, 0.0, 0.0, 0.0)) / np.sqrt(2.0)
    quotient = np.column_stack((plus, cross, scalar))
    quotient_form = quotient.conj().T @ (-reduced) @ quotient
    quotient_eigenvalues, quotient_vectors = np.linalg.eigh(quotient_form)
    tt_scalar_mixing = float(abs(quotient_form[1, 2]))

    edge_index = {direction: slot for slot, direction in enumerate(union.directions)}
    source = np.zeros(len(union.directions), dtype=complex)
    source[edge_index[(0, 0, 0, 1)]] = 2.0
    metric = block49.union_line_metric_map(union, momentum)
    left_metric = block49.union_line_metric_map(union, -momentum).T
    effective_source = (
        left_metric @ source
        - left_metric
        @ symbol
        @ nonmetric
        @ np.linalg.solve(complement, nonmetric.T @ source)
    )
    spatial_source = (
        spatial.T @ effective_source
        - mixing @ temporal_inverse @ (temporal.T @ effective_source)
    )
    quotient_source = quotient.conj().T @ spatial_source
    eigen_source = quotient_vectors.conj().T @ quotient_source

    if mutation == "restore_constraint":
        repaired_constraint_norm = float(np.linalg.norm(einstein_constraints))

    return DiracCertificate(
        ranks=(
            matrix_rank(symbol),
            matrix_rank(complement),
            matrix_rank(effective),
            matrix_rank(temporal_block),
            matrix_rank(reduced),
        ),
        inertias=tuple(
            inertia(item)
            for item in (symbol, complement, effective, temporal_block, reduced)
        ),
        repaired_constraint_norm=repaired_constraint_norm,
        einstein_constraint_rank=matrix_rank(einstein_constraints),
        einstein_constraint_norm=float(np.linalg.norm(einstein_constraints)),
        quotient_eigenvalues=tuple(float(item) for item in quotient_eigenvalues),
        tt_scalar_mixing=tt_scalar_mixing,
        source_components=tuple(float(abs(item)) for item in quotient_source),
        source_eigencomponents=tuple(float(abs(item)) for item in eigen_source),
        source_ward=float(
            np.linalg.norm(source.conj() @ block48.union_gauge_map(union, momentum))
        ),
    )


def metric_gauge_coordinates(momentum: np.ndarray, mutation: str) -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    if mutation == "wrong_gauge_phase":
        q = 2.0 * np.sin(q / 2.0)
    result = np.zeros((len(block48.HCOMPS), 4), dtype=complex)
    for column in range(4):
        for row, (left, right) in enumerate(block48.HCOMPS):
            result[row, column] = 1j * (
                q[left] * int(right == column) + q[right] * int(left == column)
            )
    return result


def spatial_tt_basis(momentum: np.ndarray) -> np.ndarray:
    k = np.asarray(momentum, dtype=float)
    rows = [np.asarray([np.trace(tensor) for tensor in SPATIAL_TENSORS])]
    rows.extend(
        np.asarray([(tensor @ k)[axis] for tensor in SPATIAL_TENSORS])
        for axis in range(3)
    )
    return null_space(np.asarray(rows), rcond=1.0e-11)


def orthogonal_metric_schur(
    union: block48.ReflectionUnion,
    momentum: np.ndarray,
    mu: float,
    constant_complement: np.ndarray | None,
) -> np.ndarray:
    q = np.asarray(momentum, dtype=complex)
    symbol = action_symbol(union, q, mu)
    metric = block49.union_line_metric_map(union, q)
    nonmetric = (
        null_space(metric.conj().T, rcond=1.0e-11)
        if constant_complement is None
        else constant_complement
    )
    complement = nonmetric.conj().T @ symbol @ nonmetric
    return (
        metric.conj().T @ symbol @ metric
        - metric.conj().T
        @ symbol
        @ nonmetric
        @ np.linalg.solve(complement, nonmetric.conj().T @ symbol @ metric)
    )


def tt_forms(
    union: block48.ReflectionUnion,
    spatial_momentum: np.ndarray,
    mu: float,
    constant_complement: np.ndarray | None,
) -> tuple[np.ndarray, np.ndarray]:
    k = np.asarray(spatial_momentum, dtype=float)
    tensor = SPATIAL_EMBEDDING @ spatial_tt_basis(k)
    values = []
    for temporal in (0.0, KINETIC_STEP, -KINETIC_STEP):
        effective = orthogonal_metric_schur(
            union, np.concatenate((k, (temporal,))), mu, constant_complement
        )
        values.append(tensor.conj().T @ effective @ tensor)
    static = -0.5 * (values[0] + values[0].conj().T)
    kinetic = -(
        0.5 * (values[1] + values[2]) - values[0]
    ) / (4.0 * np.sin(KINETIC_STEP / 2.0) ** 2)
    kinetic = 0.5 * (kinetic + kinetic.conj().T)
    return static, kinetic


def zone_certificate(
    union: block48.ReflectionUnion,
    mutation: str,
) -> ZoneCertificate:
    metric_zero = block49.union_line_metric_map(union, np.zeros(4))
    constant_complement = (
        null_space(metric_zero.T, rcond=1.0e-12)
        if mutation == "constant_complement"
        else None
    )
    gauge_identity_error = 0.0
    tt_dimensions: set[int] = set()
    negative_counts = [[0, 0] for _ in MU_VALUES]
    minimum_static = [np.inf for _ in MU_VALUES]
    minimum_kinetic = [np.inf for _ in MU_VALUES]
    modes = 0

    for integer_mode in np.ndindex((GRID_SIZE, GRID_SIZE, GRID_SIZE)):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        if np.all(centered == 0):
            continue
        modes += 1
        k = 2.0 * np.pi * centered / GRID_SIZE
        q = np.concatenate((k, (0.0,)))
        metric = block49.union_line_metric_map(union, q)
        gauge = block48.union_gauge_map(union, q)
        gauge_coordinates = metric_gauge_coordinates(q, mutation)
        gauge_identity_error = max(
            gauge_identity_error, float(np.max(np.abs(metric @ gauge_coordinates - gauge)))
        )
        tt_dimensions.add(spatial_tt_basis(k).shape[1])
        for slot, mu in enumerate(MU_VALUES):
            static, kinetic = tt_forms(union, k, mu, constant_complement)
            static_minimum = float(np.linalg.eigvalsh(static)[0])
            kinetic_minimum = float(np.linalg.eigvalsh(kinetic)[0])
            negative_counts[slot][0] += int(static_minimum < -1.0e-7)
            negative_counts[slot][1] += int(kinetic_minimum < -1.0e-5)
            minimum_static[slot] = min(minimum_static[slot], static_minimum)
            minimum_kinetic[slot] = min(minimum_kinetic[slot], kinetic_minimum)

    hostile_static = tuple(
        float(item)
        for item in np.linalg.eigvalsh(
            tt_forms(
                union,
                2.0 * np.pi * np.asarray((2, 0, -2)) / GRID_SIZE,
                MU,
                constant_complement,
            )[0]
        )
    )
    hostile_kinetic = tuple(
        float(item)
        for item in np.linalg.eigvalsh(
            tt_forms(
                union,
                2.0 * np.pi * np.asarray((3, 4, -3)) / GRID_SIZE,
                MU,
                constant_complement,
            )[1]
        )
    )
    return ZoneCertificate(
        modes=modes,
        gauge_identity_error=gauge_identity_error,
        tt_dimensions=tuple(sorted(tt_dimensions)),
        negative_counts=tuple(tuple(item) for item in negative_counts),
        minimum_static=tuple(float(item) for item in minimum_static),
        minimum_kinetic=tuple(float(item) for item in minimum_kinetic),
        hostile_static=hostile_static,
        hostile_kinetic=hostile_kinetic,
    )


def corner_alias_certificate(
    union: block48.ReflectionUnion,
    mutation: str,
) -> tuple[int, int, float, float]:
    spatial = (
        np.asarray((np.pi, 0.0, 0.0))
        if mutation == "axis_corner"
        else np.asarray((np.pi, np.pi, np.pi))
    )
    momentum = np.concatenate((spatial, (0.0,)))
    tt = null_space(block53.tt_constraint(spatial), rcond=1.0e-11)
    metric = block49.union_line_metric_map(union, momentum)
    carrier = metric @ SPATIAL_EMBEDDING @ tt
    gauge = block48.union_gauge_map(union, momentum)
    fitted = gauge @ np.linalg.lstsq(gauge, carrier, rcond=None)[0]
    symbol = action_symbol(union, momentum)
    return (
        matrix_rank(metric),
        matrix_rank(carrier),
        float(np.linalg.norm(carrier - fitted)),
        float(np.linalg.norm(symbol @ carrier)),
    )


def auxiliary_certificate(
    union: block48.ReflectionUnion,
) -> tuple[int, float, float]:
    momentum = np.asarray((0.37, -0.21, 0.14, 0.42), dtype=complex)
    right = block49.centered_curvature_intertwiner(union, momentum)
    left = block49.centered_curvature_intertwiner(union, -momentum).T
    base = block48.union_symbol(union, momentum)
    edge_block = base + 2.0 * MU * left @ right
    joint_right = -2.0 * MU * left
    joint_left = -2.0 * MU * right
    auxiliary = 4.0 * MU * np.eye(3)
    schur = edge_block - joint_right @ np.linalg.solve(auxiliary, joint_left)
    target = action_symbol(union, momentum)
    schur_error = float(np.max(np.abs(schur - target)))

    index = {direction: slot for slot, direction in enumerate(union.directions)}
    reconstructed = np.zeros_like(right)
    for spatial in range(3):
        axis = np.zeros(4, dtype=int)
        axis[spatial] = 1
        time = np.asarray((0, 0, 0, 1), dtype=int)
        forward = tuple(axis + time)
        reflected = tuple(axis - time)
        plus = np.zeros(len(union.directions), dtype=complex)
        minus = np.zeros(len(union.directions), dtype=complex)
        plus[index[forward]] = np.sqrt(2.0)
        plus[index[tuple(axis)]] = -1.0
        plus[index[tuple(time)]] = -np.exp(1j * momentum[spatial])
        minus[index[reflected]] = np.sqrt(2.0) * np.exp(1j * momentum[3])
        minus[index[tuple(axis)]] = -np.exp(1j * momentum[3])
        minus[index[tuple(time)]] = -1.0
        reconstructed[spatial] = (
            np.exp(-0.5j * (momentum[spatial] + momentum[3])) * (plus + minus)
        )
    connection_error = float(np.max(np.abs(reconstructed - right)))
    zero_rank = matrix_rank(
        block49.centered_curvature_intertwiner(union, np.zeros(4)), 1.0e-12
    )
    return zero_rank, schur_error, connection_error


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    axioms = flat(AXIOM_PATH)
    block49_note = flat(BLOCK49_PATH)
    block50_note = flat(BLOCK50_PATH)
    block53_note = flat(BLOCK53_PATH)
    block68_note = flat(BLOCK68_PATH)
    block74_note = flat(BLOCK74_PATH)

    checks.check(
        "A-authority-and-parent-bindings",
        "the actual axiom boundary and Blocks 49, 50, 53, 68, and 74 are bound without dynamics promotion",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "does not choose a hamiltonian or transfer operator" in axioms
        and "exact three-component intertwiner exists" in block49_note
        and "sampled finite-frequency survival" in block50_note
        and "stable finite-depth causal two-tt update exists" in block53_note
        and "6,528" in block68_note
        and "direct covariance fails necessary" in block74_note,
    )

    union = block48.build_reflection_union()
    sectors, edge_swap, gauge_swap = sector_data(union)
    symmetry_error = 0.0
    for frequency in (1.118, 1.138 + 0.012j, 1.160):
        momentum = axis_momentum(1.28, frequency)
        symbol = action_symbol(union, momentum)
        gauge = block48.union_gauge_map(union, momentum)
        symmetry_error = max(
            symmetry_error,
            float(np.max(np.abs(edge_swap @ symbol - symbol @ edge_swap))),
            float(np.max(np.abs(edge_swap @ gauge - gauge @ gauge_swap))),
        )
    checks.check(
        "B-exact-axis-sector-and-gauge-split",
        "the reflected action has exact 16+6 edge and 3+1 gauge y/z sectors on the analytic axis",
        len(union.directions) == 22
        and tuple(item.edge_basis.shape[1] for item in sectors) == (16, 6)
        and tuple(item.gauge_basis.shape[1] for item in sectors) == (3, 1)
        and np.max(np.abs(edge_swap @ edge_swap - np.eye(22))) < 1.0e-15
        and symmetry_error < 2.0e-13,
        f"sector dims={(16, 6)}/{(3, 1)}; symmetry error={symmetry_error:.3e}",
    )

    even = sectors[0]
    outer = tuple(
        pole_datum(union, wave_number, complex(initial), even, mutation)
        for wave_number, initials in OUTER_POLES
        for initial in initials
    )
    checks.check(
        "C-two-real-pole-pairs-are-complete-edge-nulls",
        "two isolated real even-sector poles exist on each side of the hostile collision band",
        all(item.solver_success for item in outer)
        and max(item.determinant_residual for item in outer) < 1.0e-14
        and max(abs(item.frequency.imag) for item in outer) < 5.0e-10
        and max(item.bordered_null_ratio for item in outer) < 1.0e-14
        and min(item.next_singular_ratio for item in outer) > 2.0e-5
        and max(item.multiplier_ratio for item in outer) < 1.0e-12
        and max(item.edge_null_ratio for item in outer) < 1.0e-14,
        "frequencies=" + ",".join(f"{item.frequency.real:.9f}" for item in outer)
        + f"; max null={max(item.bordered_null_ratio for item in outer):.3e}",
    )

    hostile_inputs = (
        COMPLEX_POLES
        if mutation != "erase_complex_pair"
        else ((1.25, 1.118 + 0j, 1.159 + 0j),) * len(COMPLEX_POLES)
    )
    hostile = tuple(
        (
            pole_datum(union, wave_number, complex(upper), even, mutation),
            pole_datum(union, wave_number, complex(lower), even, mutation),
        )
        for wave_number, upper, lower in hostile_inputs
    )
    conjugacy_error = max(
        abs(pair[0].frequency - pair[1].frequency.conjugate()) for pair in hostile
    )
    hostile_phases = tuple(abs(pair[0].frequency.imag) for pair in hostile)
    checks.check(
        "D-open-sampled-complex-pole-band",
        "the two real poles leave the real axis as a conjugate pair at four interior momenta",
        all(item.solver_success for pair in hostile for item in pair)
        and conjugacy_error < 2.0e-9
        and min(hostile_phases) > 4.0e-3
        and max(hostile_phases) < 2.0e-2
        and max(
            item.bordered_null_ratio for pair in hostile for item in pair
        )
        < 1.0e-14
        and max(item.edge_null_ratio for pair in hostile for item in pair) < 1.0e-14,
        "|Im omega|=" + ",".join(f"{item:.8f}" for item in hostile_phases)
        + f"; conjugacy={conjugacy_error:.3e}",
    )

    mean_weights = tuple(
        float(np.mean([value.real for value in item.spectral_weights]))
        for item in outer
    )
    side_error = max(
        abs(item.spectral_weights[0] - item.spectral_weights[1]) for item in outer
    )
    checks.check(
        "E-opposite-residue-companion-and-sign-exchange",
        "the local cross observable has one positive and one negative spectral weight which exchange branches",
        mean_weights[0] > 0.70
        and mean_weights[1] < -0.04
        and mean_weights[2] < -0.04
        and mean_weights[3] > 0.70
        and side_error < 2.0e-4,
        "-Res_E C=" + ",".join(f"{item:.9f}" for item in mean_weights)
        + f"; side error={side_error:.3e}",
    )

    dirac = dirac_certificate(union, mutation)
    checks.check(
        "F-repair-loses-einstein-hamiltonian-constraint",
        "the constant-complement metric Schur has only a gauge lapse null while Einstein has one constraint row",
        dirac.ranks == (18, 12, 6, 3, 3)
        and dirac.inertias[2] == (4, 2, 4)
        and dirac.inertias[3] == (2, 1, 1)
        and dirac.inertias[4] == (2, 1, 3)
        and dirac.repaired_constraint_norm < 1.0e-12
        and dirac.einstein_constraint_rank == 1
        and 0.05 < dirac.einstein_constraint_norm < 0.06,
        f"ranks={dirac.ranks}; repaired constraint={dirac.repaired_constraint_norm:.3e}; Einstein={dirac.einstein_constraint_norm:.9f}",
    )
    checks.check(
        "G-extra-indefinite-source-coupled-channel",
        "the three-channel quotient is indefinite, mixes TT with scalar, and the conserved static source reaches both",
        dirac.quotient_eigenvalues[0] < -0.018
        and dirac.quotient_eigenvalues[1] > 0.025
        and dirac.quotient_eigenvalues[2] > 0.038
        and dirac.tt_scalar_mixing > 0.011
        and dirac.source_components[1] > 0.20
        and dirac.source_components[2] > 0.27
        and dirac.source_eigencomponents[0] > 0.30
        and dirac.source_eigencomponents[2] > 0.14
        and dirac.source_ward < 1.0e-14,
        "eig=" + ",".join(f"{item:.9f}" for item in dirac.quotient_eigenvalues)
        + "; source eig="
        + ",".join(f"{item:.6f}" for item in dirac.source_eigencomponents),
    )

    zone = zone_certificate(union, mutation)
    checks.check(
        "H-exact-line-metric-gauge-and-two-tt-interface",
        "the raw-momentum metric gauge identity and two-dimensional analytic TT quotient hold on all 728 modes",
        zone.modes == 728
        and zone.gauge_identity_error < 2.0e-13
        and zone.tt_dimensions == (2,),
        f"modes={zone.modes}; gauge identity={zone.gauge_identity_error:.3e}; TT dims={zone.tt_dimensions}",
    )
    checks.check(
        "I-full-zone-canonical-schur-positivity-killed",
        "the orthogonal metric Schur has the same broad negative static and kinetic census at three mu values",
        zone.negative_counts == ((276, 174), (276, 174), (276, 174))
        and max(zone.minimum_static) < -40.0
        and max(zone.minimum_kinetic) < -3000.0
        and zone.hostile_static[0] < -47.0
        and zone.hostile_static[1] > 0.59
        and zone.hostile_kinetic[0] < -3000.0
        and zone.hostile_kinetic[1] > 0.16,
        f"counts={zone.negative_counts}; hostile B={zone.hostile_static}; hostile A={zone.hostile_kinetic}",
    )

    corner = corner_alias_certificate(union, mutation)
    checks.check(
        "J-cubic-corner-two-tt-carrier-alias",
        "both site-TT directions map into exact edge gauge at the cubic corner while the metric chart drops to rank eight",
        corner[0] == 8
        and corner[1] == 2
        and corner[2] < 1.0e-12
        and corner[3] < 1.0e-12,
        f"rank(M/F)={corner[:2]}; gauge residual={corner[2]:.3e}; QF={corner[3]:.3e}",
    )

    auxiliary = auxiliary_certificate(union)
    checks.check(
        "K-rank-three-connection-rewrite-is-exact-marginal",
        "the exact triangle-connection stencil and rank-three positive auxiliary Schur reduce back to Q_mu",
        auxiliary[0] == 3
        and auxiliary[1] < 1.0e-13
        and auxiliary[2] < 1.0e-13
        and "inherits every raw-edge moment" in note,
        f"rank D0={auxiliary[0]}; Schur={auxiliary[1]:.3e}; stencil={auxiliary[2]:.3e}",
    )

    checks.check(
        "L-physical-boundary-and-no-go-discipline",
        "the narrow route retirement passes N1 through N8 and preserves changed-action and changed-quotient escapes",
        mutation != "note_scope"
        and all(f"### n{index}" in note for index in range(1, 9))
        and "gate outcome: pass" in note.replace("**", "")
        and all(
            phrase in note
            for phrase in (
                "not a gravity no-go",
                "changed physical quotient",
                "changed cross action",
                "no canonical axiom is edited",
                "no toe percentage movement",
            )
        ),
    )

    print(
        "N5_CERTIFICATE: 22 edges, four exact gauge columns, two axis sectors, twelve nonmetric directions, 12 hostile poles, 728 spatial modes, three mu values, and two TT coordinates are resolved"
    )
    print(
        "per_element: checked every reflected edge, gauge column, metric coordinate, auxiliary row, and local TT observable"
    )
    print(
        "per_site: the supplied translation-invariant reflected Block-74 action and Block-49 line-metric chart are used unchanged"
    )
    print(
        "per_mode: checked the explicit pole-collision sample and all nonzero L=9 spatial momenta at three coefficients"
    )
    print(
        "per_block: checked analytic poles/residues, Dirac ranks, source coupling, full-zone TT Schurs, corner alias, and auxiliary elimination"
    )
    print(
        "lattice_wide: no continuum momentum theorem, nonlinear constraint algebra, selected clock, physical inner product, or complete Record dynamics is inferred"
    )
    print(
        "scope_boundary: route cut for the supplied Q_mu raw-edge marginal and two declared canonical charts; not canonical/connection gravity, axiom, or TOE closure"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
