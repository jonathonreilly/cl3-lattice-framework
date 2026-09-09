#!/usr/bin/env python3
"""Finite source-only fixture for the corrected PR #7338 Schur-pole packet.

The functions below are narrow extractions of the exercised current source
implementations.  Their source files and hashes are recorded in
``EXTRACTION_PROVENANCE``.  Only the fundamental Regge geometry module is
imported at runtime; historical campaign controllers are not imported.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from functools import lru_cache
import numpy as np
import sympy as sp

import frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09 as regge

ALPHA = 1.0 / 1024.0
MU = 1.0 / 1024.0
HCOMPS = tuple(regge.HCOMPS)
ORIGINAL_DIRECTIONS = tuple(tuple(int(value) for value in direction) for direction in regge.DIRS15)
TIME_REFLECTION = np.diag((1, 1, 1, -1)).astype(int)
EXTRACTION_PROVENANCE = {'admissibility_flat_regge_curvature_squared_branch_lift_2026_08_10.py': 'adb117ec956c27f486318673829464d47bc4cbe11fbffae88e70299ee2c35bce',
 'admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_2026_08_14.py': '8184091297088a47404f6a94646c62ce72848bb842ec53e70f9536654456dcdd',
 'admissibility_reflected_plaquette_curvature_record_ricci_source_intertwiner_boundary_2026_08_11.py': '64dc66c6492820b4051080eb4d6167dd55e09da2f23ebd8e920a2e4ed0ae607f',
 'admissibility_regge_fixed_average_tick_source_increasing_torus_ward_green_boundary_2026_08_11.py': '8cfe54ce6a3ecbcb82c52313b9b22bdfd8c6d0db3e131f5d9bf81d4b0e6c9353',
 'admissibility_regge_reflected_orientation_common_metric_transfer_gate_boundary_2026_08_11.py': '8b4002ee5491591ee35912e6d91e023a1fe16e0da37d068ae9982c6c560584eb',
 'admissibility_repaired_regge_full_edge_finite_frequency_pole_survival_boundary_2026_08_11.py': '15fd4711c7068412bc47859c8c4ae96dbb07605170745680e849bf7506d3f050'}
RUNTIME_INPUT_PROVENANCE = {
    "frontier_cubic_coxeter_regge_second_variation_3plus1_2026_06_09.py":
        "537371554e1a5244875645ca600f5f01e0ccfae64530572630d934e8ea0a85ce",
}

AREA_HESSIAN = sp.lambdify(
    regge.AREA_SYMS,
    [[sp.diff(regge._A, left, right) for right in regge.AREA_SYMS]
     for left in regge.AREA_SYMS],
    "numpy",
)



def edge_data(left, right, lengths):
    edge_class, anchor = regge.edge_class(tuple(left), tuple(right))
    return (
        edge_class,
        tuple(int(value) for value in anchor),
        float(lengths[edge_class]),
    )


def triangle_geometry(triangle, lengths):
    vertices = [np.asarray(vertex) for vertex in triangle]
    area_edges = [
        edge_data(vertices[left], vertices[right], lengths)
        for left, right in ((0, 1), (0, 2), (1, 2))
    ]
    area_lengths = np.asarray([entry[2] for entry in area_edges])
    area_out = regge.AREA(*(area_lengths * area_lengths))
    area = float(area_out[0])
    area_terms = [
        (edge_class, anchor, 2.0 * length * float(area_out[1 + slot]))
        for slot, (edge_class, anchor, length) in enumerate(area_edges)
    ]

    deficit = 2.0 * np.pi
    deficit_terms_raw = []
    for simplex in regge.STARS[triangle]:
        local = {vertex: index for index, vertex in enumerate(simplex)}
        hinge = sorted(local[vertex] for vertex in triangle)
        missing = tuple(sorted(index for index in range(5) if index not in hinge))
        simplex_edges = [
            edge_data(simplex[left], simplex[right], lengths)
            for left, right in regge.PAIRS5
        ]
        simplex_lengths = np.asarray([entry[2] for entry in simplex_edges])
        theta = regge.THETA[missing](*(simplex_lengths * simplex_lengths))
        deficit -= float(theta[0])
        for slot, (edge_class, anchor, length) in enumerate(simplex_edges):
            deficit_terms_raw.append(
                (edge_class, anchor, -2.0 * length * float(theta[1 + slot]))
            )

    deficit_map = defaultdict(float)
    for edge_class, anchor, value in deficit_terms_raw:
        deficit_map[(edge_class, anchor)] += value
    deficit_terms = [
        (key[0], key[1], value) for key, value in deficit_map.items()
    ]
    return area, area_edges, area_terms, deficit, deficit_terms


def add_kernel(kernel, shift, row, column, value):
    kernel[shift][row, column] += float(value)


def uniform_regge_kernel(lengths):
    """Real-space Hessian of the actual Regge action at uniform lengths."""
    kernel = defaultdict(lambda: np.zeros((15, 15), dtype=float))
    deficits = []
    for triangle in regge.TRI_CLASSES:
        area, area_edges, area_terms, deficit, deficit_terms = triangle_geometry(
            triangle, lengths
        )
        del area
        deficits.append(deficit)
        for row, row_anchor, row_value in area_terms:
            for column, column_anchor, column_value in deficit_terms:
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(
                    kernel,
                    shift,
                    row,
                    column,
                    0.5 * row_value * column_value,
                )
        for row, row_anchor, row_value in deficit_terms:
            for column, column_anchor, column_value in area_terms:
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(
                    kernel,
                    shift,
                    row,
                    column,
                    0.5 * row_value * column_value,
                )

        area_lengths = np.asarray([entry[2] for entry in area_edges])
        area_hessian_q = np.asarray(
            AREA_HESSIAN(*(area_lengths * area_lengths)), dtype=float
        )
        area_out = regge.AREA(*(area_lengths * area_lengths))
        for row_slot, (row, row_anchor, row_length) in enumerate(area_edges):
            for column_slot, (
                column,
                column_anchor,
                column_length,
            ) in enumerate(area_edges):
                value = (
                    4.0
                    * row_length
                    * column_length
                    * area_hessian_q[row_slot, column_slot]
                )
                if row_slot == column_slot:
                    value += 2.0 * float(area_out[1 + row_slot])
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(kernel, shift, row, column, deficit * value)
    return dict(kernel), np.asarray(deficits)


def curvature_squared_kernel(flat_lengths):
    """Exact flat-background Hessian of sum_h A_h epsilon_h**2."""
    kernel = defaultdict(lambda: np.zeros((15, 15), dtype=float))
    for triangle in regge.TRI_CLASSES:
        area, _, _, deficit, deficit_terms = triangle_geometry(
            triangle, flat_lengths
        )
        if abs(deficit) >= 1.0e-12:
            raise AssertionError("curvature-square Hessian requires the flat anchor")
        for row, row_anchor, row_value in deficit_terms:
            for column, column_anchor, column_value in deficit_terms:
                shift = tuple(
                    column_anchor[axis] - row_anchor[axis] for axis in range(4)
                )
                add_kernel(
                    kernel,
                    shift,
                    row,
                    column,
                    2.0 * area * row_value * column_value,
                )
    return dict(kernel)


@lru_cache(maxsize=1)
def flat_lengths() -> np.ndarray:
    return np.sqrt(
        np.asarray([sum(direction) for direction in regge.DIRS15], dtype=float)
    )


@lru_cache(maxsize=1)
def regge_kernel() -> dict:
    kernel, deficits = uniform_regge_kernel(flat_lengths())
    if np.max(np.abs(deficits)) >= 2.0e-13:
        raise AssertionError("flat Regge deficits failed to vanish")
    return kernel


@lru_cache(maxsize=1)
def curvature_square_kernel() -> dict:
    return curvature_squared_kernel(flat_lengths())


def combined_kernel() -> tuple[np.ndarray, np.ndarray]:
    merged: defaultdict[tuple[int, ...], np.ndarray] = defaultdict(
        lambda: np.zeros((15, 15), dtype=float)
    )
    for shift, matrix in regge_kernel().items():
        merged[tuple(int(value) for value in shift)] += np.asarray(matrix, dtype=float)
    for shift, matrix in curvature_square_kernel().items():
        merged[tuple(int(value) for value in shift)] += ALPHA * np.asarray(
            matrix, dtype=float
        )
    return (
        np.asarray(tuple(merged), dtype=float),
        np.asarray(tuple(merged.values()), dtype=float),
    )


SHIFTS, MATRICES = combined_kernel()


def swap_matrix(vectors: np.ndarray, left: int, right: int) -> np.ndarray:
    integer_vectors = np.asarray(vectors, dtype=int)
    permutation = np.zeros((len(integer_vectors), len(integer_vectors)), dtype=float)
    for column, vector in enumerate(integer_vectors):
        image = vector.copy()
        image[left], image[right] = image[right], image[left]
        matches = np.flatnonzero(np.all(integer_vectors == image, axis=1))
        if len(matches) != 1:
            raise AssertionError("coordinate-swap image is not unique")
        permutation[matches[0], column] = 1.0
    return permutation


def sign_basis(involution: np.ndarray, sign: int) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(involution)
    return eigenvectors[:, np.isclose(eigenvalues, float(sign))]


@dataclass(frozen=True)
class ReflectionUnion:
    directions: tuple[tuple[int, ...], ...]
    shifts: np.ndarray
    matrices: np.ndarray
    original_matrices: np.ndarray
    reflected_matrices: np.ndarray
    reflected_label_map: tuple[tuple[tuple[int, ...], tuple[int, ...]], ...]


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
        SHIFTS.astype(int), MATRICES
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


def basis_direction(index: int) -> tuple[int, int, int, int]:
    return tuple(1 if coordinate == index else 0 for coordinate in range(4))


def curvature_intertwiner(
    union: ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    """Three local two-diagonal-minus-four-side space--time plaquette rows."""
    q = np.asarray(momentum, dtype=complex)
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    time = basis_direction(3)
    rows = np.zeros((3, len(union.directions)), dtype=complex)
    for spatial in range(3):
        axis = basis_direction(spatial)
        forward = tuple(axis[mu] + time[mu] for mu in range(4))
        reflected = tuple(axis[mu] - time[mu] for mu in range(4))
        rows[spatial, index[forward]] = np.sqrt(2.0)
        rows[spatial, index[reflected]] = np.sqrt(2.0) * np.exp(1j * q[3])
        rows[spatial, index[axis]] = -(1.0 + np.exp(1j * q[3]))
        rows[spatial, index[time]] = -(1.0 + np.exp(1j * q[spatial]))
    return rows


def centered_curvature_intertwiner(
    union: ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    q = np.asarray(momentum, dtype=complex)
    centering = np.diag(np.exp(-0.5j * (q[:3] + q[3])))
    return centering @ curvature_intertwiner(union, q)


def union_line_metric_map(
    union: ReflectionUnion, momentum: np.ndarray
) -> np.ndarray:
    directions = np.asarray(union.directions, dtype=float)
    half_phase = directions @ np.asarray(momentum, dtype=complex) / 2.0
    factors = np.ones(len(directions), dtype=complex)
    nonzero = np.abs(half_phase) >= 1.0e-13
    factors[nonzero] = (
        np.exp(1j * half_phase[nonzero])
        * np.sin(half_phase[nonzero])
        / half_phase[nonzero]
    )
    return factors[:, None] * metric_coefficients(directions)


def cross_action_symbol(
    union: ReflectionUnion,
    momentum: np.ndarray,
    mu: float,
    mutation: str = "",
) -> np.ndarray:
    """Finite-range reflected action with an analytic D(-q)^T D(q) term."""

    q = np.asarray(momentum, dtype=complex)
    right = centered_curvature_intertwiner(union, q)
    if mutation == "wrong_reflection_factor":
        left = right.T
        penalty = left @ right
    else:
        left = centered_curvature_intertwiner(union, -q).T
        penalty = left @ right
    return union_symbol(union, q) + mu * penalty


def local_tt_observables(
    union: ReflectionUnion, mutation: str
) -> tuple[np.ndarray, np.ndarray]:
    index = {direction: slot for slot, direction in enumerate(union.directions)}
    plus = np.zeros(len(union.directions), dtype=complex)
    plus[index[(0, 1, 0, 0)]] = 1.0
    plus[index[(0, 0, 1, 0)]] = -1.0

    cross = np.zeros(len(union.directions), dtype=complex)
    cross[index[(0, 1, 1, 0)]] = np.sqrt(2.0)
    cross[index[(0, 1, 0, 0)]] = -1.0
    cross[index[(0, 0, 1, 0)]] = -1.0
    if mutation == "gauge_observable":
        cross[index[(1, 0, 0, 0)]] += 1.0
    return plus, cross


def hankel_minimum(
    moments: np.ndarray, step: int, order: int, shift: int
) -> float:
    matrix = np.asarray(
        [
            [moments[step * (left + right + shift)] for right in range(order)]
            for left in range(order)
        ],
        dtype=float,
    )
    return float(np.linalg.eigvalsh(matrix)[0])
