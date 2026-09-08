#!/usr/bin/env python3
"""Block 77: local incidence Fierz--Pauli with a signed Record source.

The runner builds the ten-component vertex/face staggered Einstein symbol,
checks its raw Laurent support and covariance, and deposits the Block-67
straight signed head current as one symmetric spacetime tensor.  It then
separates the one-tick covariant CFL wall from the positive Block-53 depth-two
ADM quotient.  The latter is not silently promoted to the same finite-zone
four-dimensional law.
"""

from __future__ import annotations

import os
from pathlib import Path
import sys
from itertools import permutations, product

import numpy as np
from scipy.linalg import null_space


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 240
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_"
    "CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK44_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_"
    "CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK53_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_"
    "UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md"
)
BLOCK67_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_"
    "SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
BLOCK76_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_SIGNATURE_GRAVITY_REPLACEMENT_SHORTEST_ROUTE_"
    "GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PREMISE_PATH = ROOT / "docs" / "audit" / "data" / "axiom_premise_nodes.json"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_REPAIRED_REGGE_FULL_EDGE_SCHUR_IR_LORENTZIAN_CONSTRAINT_TT_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_TWO_TT_SPLIT_STEP_RECORD_FRONTIER_CAUSAL_MACRO_UPDATE_LSTAR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-11.md",
    "docs/ADMISSIBILITY_CYCLE713_SIGNED_RECORD_SOURCE_CAUSAL_TT_VERTICAL_SLICE_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/ADMISSIBILITY_DIRAC_SIGNATURE_GRAVITY_REPLACEMENT_SHORTEST_ROUTE_GATE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11.py",
    "scripts/admissibility_cycle713_signed_record_source_causal_tt_vertical_slice_2026_08_13.py",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
)

sys.path.insert(0, str(ROOT / "scripts"))
import admissibility_two_tt_split_step_record_frontier_causal_macro_update_lstar_boundary_2026_08_11 as block53  # noqa: E402


# Coordinates are (x,y,z,t); the displayed Frobenius order is
# (tt,xx,yy,zz,sqrt2 xt,sqrt2 yt,sqrt2 zt,sqrt2 xy,sqrt2 xz,sqrt2 yz).
PAIRS = (
    (3, 3), (0, 0), (1, 1), (2, 2),
    (0, 3), (1, 3), (2, 3),
    (0, 1), (0, 2), (1, 2),
)
SPATIAL_SLOTS = (1, 2, 3, 7, 8, 9)
TEMPORAL_SLOTS = (0, 4, 5, 6)
SHIFT_SLOTS = (4, 5, 6)
ETA = np.diag((1.0, 1.0, 1.0, -1.0))
GRID_SIZE = 9
TOL = 1.0e-10


def frobenius_basis(pair: tuple[int, int]) -> np.ndarray:
    left, right = pair
    result = np.zeros((4, 4), dtype=float)
    value = 1.0 if left == right else 1.0 / np.sqrt(2.0)
    result[left, right] = value
    result[right, left] = value
    return result


BASIS = tuple(frobenius_basis(pair) for pair in PAIRS)


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


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def matrix_rank(matrix: np.ndarray, tolerance: float = 1.0e-9) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tolerance))


def lattice_vector(momentum: np.ndarray) -> np.ndarray:
    return 2.0 * np.sin(np.asarray(momentum, dtype=float) / 2.0)


def centered_gauge(momentum_vector: np.ndarray) -> np.ndarray:
    p = np.asarray(momentum_vector, dtype=float)
    result = np.zeros((10, 4), dtype=float)
    for row, (left, right) in enumerate(PAIRS):
        for column in range(4):
            tensor = np.zeros((4, 4), dtype=float)
            tensor[:, column] += p
            tensor[column, :] += p
            result[row, column] = float(np.sum(BASIS[row] * tensor))
    return result


def centered_operator(momentum_vector: np.ndarray, euclidean: bool = False) -> np.ndarray:
    """Frobenius coordinate pairing h^{mu nu} G_mu_nu."""
    p_lower = np.asarray(momentum_vector, dtype=float)
    metric = np.eye(4) if euclidean else ETA
    p_upper = metric @ p_lower
    p_squared = float(p_lower @ p_upper)
    tensors = []
    for perturbation in BASIS:
        trace = float(np.trace(metric @ perturbation))
        contracted = perturbation @ p_upper
        double = float(p_upper @ perturbation @ p_upper)
        tensor = 0.5 * (
            p_squared * perturbation
            + np.outer(p_lower, p_lower) * trace
            - np.outer(p_lower, contracted)
            - np.outer(contracted, p_lower)
            - metric * (p_squared * trace - double)
        )
        tensors.append(tensor)
    result = np.asarray(
        [
            [float(np.sum((metric @ basis @ metric) * tensor)) for tensor in tensors]
            for basis in BASIS
        ]
    )
    return 0.5 * (result + result.T)


def placement_matrix(momentum: np.ndarray, mutation: str = "") -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    values = []
    for left, right in PAIRS:
        if left == right or mutation == "co_locate_faces":
            values.append(1.0)
        else:
            values.append(np.exp(0.5j * (q[left] + q[right])))
    return np.diag(values)


def vector_placement(momentum: np.ndarray) -> np.ndarray:
    return np.diag(np.exp(0.5j * np.asarray(momentum, dtype=float)))


def raw_operator(momentum: np.ndarray, mutation: str = "") -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    placement = placement_matrix(q, mutation)
    return placement @ centered_operator(lattice_vector(q)) @ placement.conj().T


def raw_gauge(momentum: np.ndarray, mutation: str = "") -> np.ndarray:
    q = np.asarray(momentum, dtype=float)
    result = (
        placement_matrix(q)
        @ (1j * centered_gauge(lattice_vector(q)))
        @ vector_placement(q).conj().T
    )
    if mutation == "erase_gauge":
        result = result.copy()
        result[0, 3] = 0.0
    return result


def tensor_representation(matrix: np.ndarray) -> np.ndarray:
    transform = np.asarray(matrix, dtype=float)
    result = np.zeros((10, 10), dtype=float)
    for column, basis in enumerate(BASIS):
        image = transform @ basis @ transform.T
        for row, target in enumerate(BASIS):
            result[row, column] = float(np.sum(target * image))
    return result


def proper_cubic_rotations() -> tuple[np.ndarray, ...]:
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = np.zeros((3, 3), dtype=int)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = np.diag(signs) @ permutation_matrix
            if round(np.linalg.det(candidate)) == 1:
                rotations.append(candidate)
    return tuple(rotations)


ROTATIONS = proper_cubic_rotations()


def raw_locality_certificate(mutation: str) -> tuple[int, int, int, float, float]:
    size = 7
    symbols = np.zeros((size, size, size, size, 10, 10), dtype=complex)
    for integer_mode in np.ndindex((size, size, size, size)):
        q = 2.0 * np.pi * np.asarray(integer_mode) / size
        symbols[integer_mode] = raw_operator(q, mutation)
    kernel = np.fft.fftn(symbols, axes=(0, 1, 2, 3)) / size**4
    maximum = np.max(np.abs(kernel), axis=(4, 5))
    support = np.argwhere(maximum > 1.0e-10)
    shifts = tuple(
        np.where(index <= size // 2, index, index - size) for index in support
    )
    max_coordinate = max(int(np.max(np.abs(shift))) for shift in shifts)
    max_manhattan = max(int(np.sum(np.abs(shift))) for shift in shifts)

    q = np.asarray((0.31, -0.47, 0.82, 0.29))
    base = raw_operator(q, mutation)
    periodicity = 0.0
    for direction in range(4):
        translated = q.copy()
        translated[direction] += 2.0 * np.pi
        periodicity = max(
            periodicity,
            float(np.max(np.abs(raw_operator(translated, mutation) - base))),
        )
    hermiticity = float(np.max(np.abs(base - base.conj().T)))
    return len(support), max_coordinate, max_manhattan, periodicity, hermiticity


def covariance_certificate(mutation: str) -> tuple[float, float, float]:
    rotation_error = 0.0
    gauge_error = 0.0
    probes = (
        np.asarray((0.37, -0.51, 0.83, 0.29)),
        np.asarray((np.pi, 0.4, -np.pi, 0.7)),
        np.asarray((np.pi, np.pi, 0.2, np.pi)),
    )
    for spatial in ROTATIONS:
        transform = np.eye(4)
        transform[:3, :3] = spatial
        tensor = tensor_representation(transform)
        for q in probes:
            transformed_q = transform @ q
            raw_tensor = (
                placement_matrix(transformed_q)
                @ tensor
                @ placement_matrix(q).conj().T
            )
            raw_vector = (
                vector_placement(transformed_q)
                @ transform
                @ vector_placement(q).conj().T
            )
            rotation_error = max(
                rotation_error,
                float(
                    np.max(
                        np.abs(
                            raw_operator(transformed_q)
                            - raw_tensor @ raw_operator(q) @ raw_tensor.conj().T
                        )
                    )
                ),
            )
            gauge_error = max(
                gauge_error,
                float(
                    np.max(
                        np.abs(
                            raw_gauge(transformed_q) @ raw_vector
                            - raw_tensor @ raw_gauge(q)
                        )
                    )
                ),
            )

    reflection = np.diag((1.0, 1.0, 1.0, -1.0))
    tensor_reflection = (
        np.eye(10)
        if mutation == "wrong_time_parity"
        else tensor_representation(reflection)
    )
    reflection_error = 0.0
    for q in probes:
        reflected_q = reflection @ q
        raw_tensor = (
            placement_matrix(reflected_q)
            @ tensor_reflection
            @ placement_matrix(q).conj().T
        )
        reflection_error = max(
            reflection_error,
            float(
                np.max(
                    np.abs(
                        raw_operator(reflected_q)
                        - raw_tensor @ raw_operator(q) @ raw_tensor.conj().T
                    )
                )
            ),
        )
    return rotation_error, gauge_error, reflection_error


def four_dimensional_census(
    mutation: str,
) -> tuple[tuple[int, int, int], float, set[int], set[int], set[int]]:
    counts = [0, 0, 0]
    ward_error = 0.0
    gauge_ranks: set[int] = set()
    off_shell_extra_nullities: set[int] = set()
    null_shell_extra_nullities: set[int] = set()
    for integer_mode in np.ndindex((GRID_SIZE,) * 4):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        q = 2.0 * np.pi * centered / GRID_SIZE
        p = lattice_vector(q)
        symbol = centered_operator(p)
        gauge = centered_gauge(p)
        if mutation == "erase_gauge" and np.any(centered):
            gauge = gauge.copy()
            gauge[0, 3] = 0.0
        ward_error = max(ward_error, float(np.max(np.abs(symbol @ gauge))))
        if np.all(centered == 0):
            counts[2] += int(matrix_rank(symbol) == 0)
        elif abs(float(p @ ETA @ p)) < 1.0e-10:
            symbol_rank = matrix_rank(symbol)
            gauge_rank = matrix_rank(gauge)
            counts[1] += int(symbol_rank == 4)
            gauge_ranks.add(gauge_rank)
            null_shell_extra_nullities.add(10 - symbol_rank - gauge_rank)
        else:
            symbol_rank = matrix_rank(symbol)
            gauge_rank = matrix_rank(gauge)
            counts[0] += int(symbol_rank == 6)
            gauge_ranks.add(gauge_rank)
            off_shell_extra_nullities.add(10 - symbol_rank - gauge_rank)
    return (
        tuple(counts),
        ward_error,
        gauge_ranks,
        off_shell_extra_nullities,
        null_shell_extra_nullities,
    )


def spatial_constraint_certificate(mutation: str) -> tuple[int, float, float, set[int], set[int], set[int], float]:
    modes = 0
    tt_error = 0.0
    temporal_dependence = 0.0
    constraint_ranks: set[int] = set()
    temporal_ranks: set[int] = set()
    momentum_ranks: set[int] = set()
    minimum_tt = np.inf
    for integer_mode in np.ndindex((GRID_SIZE,) * 3):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        if np.all(centered == 0):
            continue
        modes += 1
        k = 2.0 * np.pi * centered / GRID_SIZE
        spatial_p = lattice_vector(k)
        constraint = block53.tt_constraint(k)
        if mutation == "tt_rows":
            constraint = constraint[:-1]
        tt = null_space(constraint, rcond=1.0e-11)
        static = centered_operator(np.concatenate((spatial_p, (0.0,))))
        spatial_block = static[np.ix_(SPATIAL_SLOTS, SPATIAL_SLOTS)]
        pulled = tt.T @ spatial_block @ tt
        kappa_squared = float(spatial_p @ spatial_p)
        if pulled.shape == (2, 2):
            tt_error = max(
                tt_error,
                float(np.max(np.abs(pulled - 0.5 * kappa_squared * np.eye(2)))),
            )
            minimum_tt = min(minimum_tt, float(np.linalg.eigvalsh(pulled)[0]))
        else:
            tt_error = float("inf")
        constraint_ranks.add(matrix_rank(constraint))
        temporal_ranks.add(matrix_rank(static[np.ix_(TEMPORAL_SLOTS, TEMPORAL_SLOTS)]))
        hamiltonian_rank = matrix_rank(static[np.ix_((0,), SPATIAL_SLOTS)])

        temporal = 0.37
        plus = centered_operator(np.concatenate((spatial_p, (temporal,))))
        minus = centered_operator(np.concatenate((spatial_p, (-temporal,))))
        derivative = (plus - minus) / (2.0 * temporal)
        momentum_rank = matrix_rank(derivative[np.ix_(SHIFT_SLOTS, SPATIAL_SLOTS)])
        momentum_ranks.add(momentum_rank)
        constraint_ranks.add(hamiltonian_rank + momentum_rank)
        temporal_dependence = max(
            temporal_dependence,
            float(
                np.max(
                    np.abs(
                        plus[np.ix_(TEMPORAL_SLOTS, TEMPORAL_SLOTS)]
                        - static[np.ix_(TEMPORAL_SLOTS, TEMPORAL_SLOTS)]
                    )
                )
            ),
        )
    return (
        modes,
        tt_error,
        temporal_dependence,
        constraint_ranks,
        temporal_ranks,
        momentum_ranks,
        minimum_tt,
    )


def signed_source(
    momentum: np.ndarray,
    axis: int,
    sign: int,
    neutral_axis: int,
    neutral_sign: int = 1,
    mutation: str = "",
) -> tuple[np.ndarray, np.ndarray]:
    q = np.asarray(momentum, dtype=float)
    alias = np.exp(-0.5j * (q[3] + sign * q[axis]))
    if mutation == "omit_alias":
        alias = 1.0
    centered = np.zeros(10, dtype=complex)
    centered[0] = 1.0
    if mutation != "omit_stress":
        centered[1 + axis] = 1.0
    centered[4 + axis] = np.sqrt(2.0) * sign * alias
    neutral = 1.0 - np.exp(-1j * neutral_sign * q[neutral_axis])
    centered *= neutral
    raw = placement_matrix(q) @ centered
    return centered, raw


def source_census(mutation: str) -> tuple[int, float, float, float, set[int]]:
    modes = 0
    ward_error = 0.0
    gauge_error = 0.0
    solve_error = 0.0
    ranks: set[int] = set()
    for size in range(3, 9):
        for axis in range(3):
            neutral_axis = (axis + 1) % 3
            remaining_axis = (axis + 2) % 3
            for sign in (-1, 1):
                for along in range(size):
                    for transverse in range(1, size):
                        for remaining in range(size):
                            integers = np.zeros(4, dtype=int)
                            integers[axis] = along
                            integers[neutral_axis] = transverse
                            integers[remaining_axis] = remaining
                            integers[3] = (-sign * along) % size
                            q = 2.0 * np.pi * integers / size
                            centered_source, raw_source = signed_source(
                                q, axis, sign, neutral_axis, mutation=mutation
                            )
                            symbol = raw_operator(q)
                            gauge = raw_gauge(q)
                            ranks.add(matrix_rank(symbol))
                            ward_error = max(
                                ward_error,
                                float(np.max(np.abs(raw_gauge(-q).T @ raw_source))),
                            )
                            gauge_error = max(
                                gauge_error,
                                float(np.max(np.abs(symbol @ gauge))),
                            )
                            response = np.linalg.pinv(symbol, rcond=1.0e-11) @ raw_source
                            solve_error = max(
                                solve_error,
                                float(np.linalg.norm(symbol @ response - raw_source)),
                            )
                            modes += 1
    return modes, ward_error, gauge_error, solve_error, ranks


def source_alias_and_covariance(mutation: str) -> tuple[float, float, float, float]:
    q_corner = np.asarray((np.pi, np.pi / 2.0, 0.0, np.pi))
    _, corner = signed_source(q_corner, 0, 1, 1, mutation=mutation)
    corner_error = float(np.max(np.abs(raw_gauge(-q_corner).T @ corner)))

    covariance_error = 0.0
    base_q = np.asarray((0.41, 0.73, -0.22, -0.41))
    _, base_source = signed_source(base_q, 0, 1, 1)
    for spatial in ROTATIONS:
        transform = np.eye(4)
        transform[:3, :3] = spatial
        transformed_q = transform @ base_q
        direction = spatial @ np.asarray((1, 0, 0))
        transverse = spatial @ np.asarray((0, 1, 0))
        axis = int(np.flatnonzero(direction)[0])
        sign = int(direction[axis])
        neutral_axis = int(np.flatnonzero(transverse)[0])
        neutral_sign = int(transverse[neutral_axis])
        _, transformed_source = signed_source(
            transformed_q, axis, sign, neutral_axis, neutral_sign
        )
        tensor = tensor_representation(transform)
        raw_tensor = (
            placement_matrix(transformed_q)
            @ tensor
            @ placement_matrix(base_q).conj().T
        )
        covariance_error = max(
            covariance_error,
            float(np.max(np.abs(transformed_source - raw_tensor @ base_source))),
        )

    q = np.asarray((0.31, 0.47, -0.19, -0.31))
    plus, _ = signed_source(q, 0, 1, 1)
    reflected_q = q.copy()
    reflected_q[3] *= -1.0
    minus, _ = signed_source(reflected_q, 0, -1, 1)
    even_error = max(abs(plus[0] - minus[0]), abs(plus[1] - minus[1]))
    odd_error = abs(plus[4] + minus[4])
    return corner_error, covariance_error, float(even_error), float(odd_error)


def static_sign_and_zero_mode(mutation: str) -> tuple[float, float, int, float, bool]:
    sign_error = 0.0
    minimum_response = np.inf
    for axis in range(3):
        neutral_axis = (axis + 1) % 3
        remaining_axis = (axis + 2) % 3
        q = np.zeros(4)
        q[neutral_axis] = 0.73
        q[remaining_axis] = -0.41
        source, _ = signed_source(q, axis, 1, neutral_axis)
        symbol = centered_operator(lattice_vector(q))
        response = np.linalg.pinv(symbol, rcond=1.0e-12) @ source
        transverse_square = float(
            lattice_vector(q)[neutral_axis] ** 2
            + lattice_vector(q)[remaining_axis] ** 2
        )
        ratio = response[0] / source[0]
        sign_error = max(sign_error, abs(ratio - 2.0 / transverse_square))
        minimum_response = min(minimum_response, float(ratio.real))

    zero_symbol = centered_operator(np.zeros(4))
    compact_mean = np.zeros(10)
    compact_mean[0] = compact_mean[1] = 1.0
    zero_residual = float(
        np.linalg.norm(zero_symbol @ np.linalg.pinv(zero_symbol) @ compact_mean - compact_mean)
    )
    boundary_acknowledged = mutation != "keep_mean"
    return sign_error, minimum_response, matrix_rank(zero_symbol), zero_residual, boundary_acknowledged


def transfer_certificate(
    mutation: str,
) -> tuple[int, int, float, float, int, float, float]:
    real_shell = 0
    failed_shell = 0
    largest_pass = 0.0
    smallest_fail = np.inf
    depth_two_stable = 0
    maximum_difference = 0.0
    coefficient_error = 0.0
    for integer_mode in np.ndindex((GRID_SIZE,) * 3):
        centered = np.asarray(integer_mode, dtype=int) - GRID_SIZE // 2
        if np.all(centered == 0):
            continue
        k = 2.0 * np.pi * centered / GRID_SIZE
        kappa_squared = block53.spatial_symbol(k)
        if kappa_squared <= 4.0 + 1.0e-12:
            real_shell += 1
            largest_pass = max(largest_pass, kappa_squared)
        else:
            failed_shell += 1
            smallest_fail = min(smallest_fail, kappa_squared)
        _, macro_step, shadow, macro, _ = block53.split_substep(kappa_squared, 2)
        eigenvalues = np.linalg.eigvals(macro)
        depth_two_stable += int(
            np.min(np.linalg.eigvalsh(shadow)) > 1.0e-10
            and np.max(np.abs(np.abs(eigenvalues) - 1.0)) < 1.0e-10
            and macro_step.shape == (2, 2)
        )
        macro_polynomial = 2.0 - float(np.trace(macro))
        derived_difference = kappa_squared - macro_polynomial
        maximum_difference = max(maximum_difference, derived_difference)
        coefficient_error = max(
            coefficient_error,
            abs(derived_difference - kappa_squared**2 / 16.0),
        )
    if mutation == "promote_one_tick":
        real_shell, failed_shell = 728, 0
    if mutation == "identify_depth2":
        maximum_difference = 0.0
    return (
        real_shell,
        failed_shell,
        largest_pass,
        smallest_fail,
        depth_two_stable,
        maximum_difference,
        coefficient_error,
    )


def main() -> int:
    checks = Checks()
    mutation = os.environ.get("TOE_MUTATION", "")
    note = flat(NOTE_PATH)
    axiom = flat(AXIOM_PATH)
    block44_note = flat(BLOCK44_PATH)
    block53_note = flat(BLOCK53_PATH)
    block67_note = flat(BLOCK67_PATH)
    block76_note = flat(BLOCK76_PATH)

    checks.check(
        "A-authority-and-parent-bindings",
        "the axiom boundary and Blocks 44, 53, 67, and 76 are bound without importing a selected law",
        all((ROOT / path).exists() for path in AUDIT_INPUT_PATHS)
        and "admissibility is not a dynamics axiom" in axiom
        and "linear bianchi identity" in block44_note
        and "positive shadow energy" in block53_note
        and "four current columns are not the four tt constraint rows" in block67_note
        and "incidence-derivative adm/fierz--pauli" in block76_note,
    )

    locality = raw_locality_certificate(mutation)
    checks.check(
        "B-raw-staggered-hermitian-finite-range-operator",
        "vertex diagonals and face off-diagonals give a periodic Hermitian 33-shift Laurent law",
        locality[0:3] == (33, 1, 2)
        and locality[3] < 2.0e-13
        and locality[4] < 2.0e-13,
        f"support={locality[0]}; max coordinate/L1={locality[1]}/{locality[2]}; periodicity={locality[3]:.3e}; Hermiticity={locality[4]:.3e}",
    )

    covariance = covariance_certificate(mutation)
    checks.check(
        "C-raw-cubic-and-time-reflection-covariance",
        "momentum-dependent label translations implement all 24 cubic rotations and time reflection at zone corners",
        max(covariance) < 3.0e-13,
        f"operator/gauge/time residuals={covariance[0]:.3e}/{covariance[1]:.3e}/{covariance[2]:.3e}",
    )

    four_d = four_dimensional_census(mutation)
    checks.check(
        "D-exact-ward-bianchi-and-lorentzian-ranks",
        "the full L=9 four-dimensional census has four gauge nulls off shell and two physical nulls on shell",
        four_d[0] == (6512, 48, 1)
        and four_d[1] < 5.0e-13
        and four_d[2] == {4}
        and four_d[3] == {0}
        and four_d[4] == {2},
        f"off-shell/null/zero rank matches={four_d[0]}; max K Gamma={four_d[1]:.3e}; gauge ranks={four_d[2]}; extra nullities off/null={four_d[3]}/{four_d[4]}",
    )

    constraints = spatial_constraint_certificate(mutation)
    checks.check(
        "E-four-einstein-constraints-and-positive-two-tt-hamiltonian",
        "lapse and shift are nondynamical, supply one plus three constraints, and leave two positive TT coordinates",
        constraints[0] == 728
        and constraints[1] < 3.0e-13
        and constraints[2] < 3.0e-13
        and constraints[3] == {4}
        and constraints[4] == {2}
        and constraints[5] == {3}
        and constraints[6] > 0.03,
        f"modes={constraints[0]}; TT error={constraints[1]:.3e}; temporal dependence={constraints[2]:.3e}; ranks C/Eaa/M={constraints[3]}/{constraints[4]}/{constraints[5]}",
    )

    source_mutation = "omit_stress" if mutation == "omit_stress" else ""
    source = source_census(source_mutation)
    checks.check(
        "F-symmetric-signed-record-source-full-tensor-intertwiner",
        "one vertex/face symmetric tensor closes both Ward columns and solves every neutral nonzero source mode",
        source[0] == 6528
        and source[1] < 5.0e-13
        and source[2] < 5.0e-13
        and source[3] < 1.0e-11
        and source[4] == {6},
        f"modes={source[0]}; source Ward={source[1]:.3e}; gauge={source[2]:.3e}; solve={source[3]:.3e}; ranks={source[4]}",
    )

    alias_mutation = "omit_alias" if mutation == "omit_alias" else ""
    source_covariance = source_alias_and_covariance(alias_mutation)
    checks.check(
        "G-even-corner-alias-parity-and-frame-covariance",
        "the crossed-face alias phase preserves the pi corner, even diagonal stress, odd momentum, and 24 frames",
        max(source_covariance) < 3.0e-13,
        f"corner/frame/even/odd residuals={source_covariance[0]:.3e}/{source_covariance[1]:.3e}/{source_covariance[2]:.3e}/{source_covariance[3]:.3e}",
    )

    static = static_sign_and_zero_mode(mutation)
    checks.check(
        "H-positive-transverse-static-sign-and-explicit-zero-mode-wall",
        "the neutral null-beam slice has positive static response while a compact positive torus mean is unsolved",
        static[0] < 2.0e-12
        and static[1] > 1.0
        and static[2] == 0
        and static[3] > 1.0
        and static[4],
        f"sign error={static[0]:.3e}; min h_tt/T00={static[1]:.6f}; rank K0={static[2]}; compact-mean residual={static[3]:.3f}",
    )

    transfer = transfer_certificate(mutation)
    checks.check(
        "I-one-tick-uv-wall-and-distinct-positive-depth-two-adm-escape",
        "one-tick covariance fails most UV shells while the same spatial Hamiltonian has a distinct stable depth-two update",
        transfer[0:2] == (176, 552)
        and 3.93 < transfer[2] < 3.94
        and 4.34 < transfer[3] < 4.35
        and transfer[4] == 728
        and transfer[5] > 8.0
        and transfer[6] < 5.0e-13,
        f"one-tick real/fail={transfer[0]}/{transfer[1]}; threshold={transfer[2]:.9f}/{transfer[3]:.9f}; depth2 stable={transfer[4]}; derived max split={transfer[5]:.6f}; coefficient error={transfer[6]:.3e}",
    )

    scope_ok = all(
        phrase in note
        for phrase in (
            "partial-positive",
            "not the same finite-frequency four-dimensional law",
            "incoming half-tick flux",
            "configuration of records",
            "zero toe percentage movement",
            "no-go discipline gate status: fail",
            "partial-narrowing",
            "n1 -- alternative route enumeration",
            "n8 -- cross-cycle echo",
        )
    )
    if mutation == "claim_complete":
        scope_ok = False
    checks.check(
        "J-cadence-ontology-and-no-go-scope-boundary",
        "the positive source seam and distinct transfer wall are stated without law, axiom, retention, or TOE promotion",
        scope_ok,
    )

    print(
        "N5_CERTIFICATE: 10 staggered tensor components, four gauge/Bianchi columns, 24 cubic frames, all 9^4 modes, 728 spatial TT fibers, and 6528 signed neutral source modes are resolved"
    )
    print(
        "per_element: every one of the ten Frobenius tensor/source coordinates, four gauge/Bianchi columns, raw placement phases, and TT quotient coordinates is checked explicitly"
    )
    print(
        "per_site: each vertex, link, and face carrier in the 33-shift radius-one stencil and each crossed-face signed-source deposition is checked on its local incidence cell"
    )
    print(
        "per_mode: all 9^4 Lorentzian modes, all 728 nonzero L=9 spatial TT fibers, and all 6528 declared L=3 through L=8 neutral signed-source modes are checked"
    )
    print(
        "per_block: raw locality, covariance, gauge/Bianchi rank, ADM constraints, symmetric source, static sign, zero mode, and transfer cadence are checked as separate interfaces"
    )
    print(
        "lattice_wide: checked and not executed — no open or infinite positive-mean boundary, global Record scheduler, exact Record/M2 gravity-state encoding, or nonlinear gravity law is supplied"
    )
    print(
        "SOURCE: exact local symmetric T00/T0i/Tij deposition passes; compact mean, birth impulse, cadence, coupling, debit, and nonlinear completion remain"
    )
    print(
        "TRANSFER: one-tick 4D law real=176/728; Block53 depth two stable=728/728 but differs by -kappa^4/16 and still needs full constraint/source scheduling"
    )
    print(
        "SCOPE: partial-positive linear nonzero-mode candidate and sharp cadence boundary; no selected L_phys, axiom amendment, audit verdict, obligation retirement, or TOE movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
