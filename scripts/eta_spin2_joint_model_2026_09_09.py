"""Finite source-only extraction for corrected Eta spin-2 notes.
No historical controller, Git authority guard, physical compiler or cache is imported.
Exact upstream bodies and extraction provenance are in the dated recovery packet.
"""
from __future__ import annotations
import itertools
from collections import Counter
from typing import Iterable
from functools import cache
import sympy as sp
import eta_spin2_quadrupole_model_2026_09_09 as b9
R=sp.Rational
I3=sp.eye(3)
ALPHA=-R(1,2)
BETA=R(1,8)
def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def cross_matrix(vector: sp.MatrixBase) -> sp.Matrix:
    x, y, z = vector
    return sp.Matrix(((0, -z, y), (z, 0, -x), (-y, x, 0)))


def axial(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix((matrix[2, 1], matrix[0, 2], matrix[1, 0]))


def joint_vectors(
    tensor: sp.MatrixBase,
    spatial_action: sp.MatrixBase,
    time_action: sp.Expr,
) -> tuple[sp.Matrix, ...]:
    """Fixed registered preparation; this is a reachability witness, not the law."""
    return tuple(
        sp.expand(
            ALPHA * tensor * direction
            + BETA * (time_action * direction + spatial_action.cross(direction))
        )
        for direction in b9.DIRECTIONS
    )


def odd_shell_matrix(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    if len(vectors) != 6:
        raise ValueError("six neighboring Bloch vectors are required")
    return sp.expand(sum(
        (vector * direction.T
         for direction, vector in zip(b9.DIRECTIONS, vectors)),
        sp.zeros(3),
    ) / 2)


def joint_decode(vectors: tuple[sp.Matrix, ...]) -> dict[str, object]:
    """Decode only the six local contents; no external label enters."""
    matrix = odd_shell_matrix(vectors)
    symmetric = sp.expand((matrix + matrix.T) / 2)
    skew = sp.expand((matrix - matrix.T) / 2)
    tensor = sp.expand(
        (symmetric - sp.trace(symmetric) * I3 / 3) / ALPHA
    )
    spatial_action = sp.expand(axial(skew) / BETA)
    time_action = sp.simplify(sp.trace(matrix) / (3 * BETA))
    return {
        "matrix": matrix,
        "tensor": tensor,
        "spatial_action": spatial_action,
        "time_action": time_action,
    }


def normalized_action(point: tuple[sp.Expr, ...]) -> tuple[sp.Matrix, sp.Expr]:
    return sp.Matrix(tuple(sp.simplify(point[index] / sp.pi)
                           for index in range(3))), sp.simplify(point[3] / sp.pi)


def decoded_point(vectors: tuple[sp.Matrix, ...]) -> tuple[sp.Expr, ...]:
    decoded = joint_decode(vectors)
    spatial = decoded["spatial_action"]
    assert isinstance(spatial, sp.MatrixBase)
    return tuple(sp.simplify(sp.pi * spatial[index]) for index in range(3)) + (
        sp.simplify(sp.pi * decoded["time_action"]),
    )


def norm_squared(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def strictly_inside_bloch_ball(vector: sp.MatrixBase) -> bool:
    return b9.strictly_below_one(sp.simplify(norm_squared(vector)))


def maximum_exact(values: tuple[sp.Expr, ...]) -> sp.Expr:
    return max(values, key=lambda value: float(sp.N(value, 30)))


def flatten(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(tuple(matrix[row, column]
                           for row in range(matrix.rows)
                           for column in range(matrix.cols)))


@cache
def decomposition_facts() -> dict[str, object]:
    shell_symbols = sp.symbols("x0:18", real=True)
    shell = tuple(sp.Matrix(shell_symbols[3 * index:3 * index + 3])
                  for index in range(6))
    matrix = odd_shell_matrix(shell)
    symmetric = sp.expand((matrix + matrix.T) / 2)
    scalar = sp.trace(symmetric) * I3 / 3
    trace_free = sp.expand(symmetric - scalar)
    skew = sp.expand((matrix - matrix.T) / 2)
    matrix_map = flatten(matrix).jacobian(shell_symbols)
    scalar_map = flatten(scalar).jacobian(shell_symbols)
    vector_map = flatten(skew).jacobian(shell_symbols)
    spin2_map = flatten(trace_free).jacobian(shell_symbols)

    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    prepared = joint_vectors(tensor, spatial, s)
    decoded = joint_decode(prepared)
    parameters = (q0, q1, q2, q3, q4, ux, uy, uz, s)
    prepared_map = sp.Matrix.vstack(*prepared).jacobian(parameters)
    decoded_coordinates = sp.Matrix((
        decoded["tensor"][0, 0], decoded["tensor"][1, 1],
        decoded["tensor"][0, 1], decoded["tensor"][0, 2],
        decoded["tensor"][1, 2],
        *tuple(decoded["spatial_action"]), decoded["time_action"],
    ))
    return {
        "matrix_rank": matrix_map.rank(),
        "scalar_rank": scalar_map.rank(),
        "vector_rank": vector_map.rank(),
        "spin2_rank": spin2_map.rank(),
        "sum_rank": sp.Matrix.vstack(scalar_map, vector_map, spin2_map).rank(),
        "prepared_rank": prepared_map.rank(),
        "decode_identity": decoded_coordinates == sp.Matrix(parameters),
        "matrix_identity": matrix_equal(
            decoded["matrix"], ALPHA * tensor + BETA * (s * I3 + cross_matrix(spatial))
        ),
    }


@cache
def covariance_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = joint_vectors(tensor, spatial, s)
    failures = []
    for rotation in b9.rotations():
        transformed_tensor = sp.expand(rotation * tensor * rotation.T)
        transformed_spatial = sp.expand(rotation * spatial)
        direct = joint_vectors(transformed_tensor, transformed_spatial, s)
        transported = []
        for direction in b9.DIRECTIONS:
            old_direction = rotation.T * direction
            old_index = next(index for index, item in enumerate(b9.DIRECTIONS)
                             if item == old_direction)
            transported.append(sp.expand(rotation * vectors[old_index]))
        decoded = joint_decode(tuple(transported))
        failures.append(not (
            all(matrix_equal(left, right)
                for left, right in zip(direct, transported))
            and matrix_equal(decoded["tensor"], transformed_tensor)
            and matrix_equal(decoded["spatial_action"], transformed_spatial)
            and sp.simplify(decoded["time_action"] - s) == 0
            and matrix_equal(
                decoded["matrix"], rotation * odd_shell_matrix(vectors) * rotation.T
            )
        ))
    return {"rotation_count": len(b9.rotations()), "failures": tuple(failures)}


@cache
def orthogonality_and_law_facts() -> dict[str, object]:
    q0, q1, q2, q3, q4, ux, uy, uz, s = sp.symbols(
        "q0 q1 q2 q3 q4 ux uy uz s", real=True
    )
    tensor = sp.Matrix(((q0, q2, q3), (q2, q1, q4), (q3, q4, -q0 - q1)))
    spatial = sp.Matrix((ux, uy, uz))
    vectors = joint_vectors(tensor, spatial, s)
    geometry_only = joint_vectors(tensor, sp.zeros(3, 1), 0)
    condition = b9.condition_tensor(vectors)
    probabilities = b9.local_distribution(vectors)
    geometry_probabilities = b9.local_distribution(geometry_only)
    moment = b9.distribution_moment(probabilities)
    universal = b9.universal_facts()
    return {
        "condition": condition,
        "condition_identity": matrix_equal(condition, ALPHA * tensor),
        "probability_independence": all(
            sp.simplify(probabilities[key] - geometry_probabilities[key]) == 0
            for key in probabilities
        ),
        "moment_identity": matrix_equal(moment, b9.TAU * ALPHA * tensor),
        "source_identity": matrix_equal(-48 * moment, tensor),
        "normalization": sp.simplify(sum(probabilities.values())),
        "universal_axis_floor": universal["axis_floor"],
        "universal_corner_floor": universal["corner_floor"],
        "universal_condition_rank": universal["condition_rank"],
        "universal_probability_rank": universal["probability_rank"],
    }
