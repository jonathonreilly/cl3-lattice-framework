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
import eta_spin2_affine_model_2026_09_09 as affine
import eta_spin2_native_model_2026_09_09 as native
R=sp.Rational
SQRT2=sp.sqrt(2)
I3=sp.eye(3)
TAU=R(1,24)
DIRECTIONS=tuple(sp.Matrix(v) for v in affine.DIRECTIONS)
CORNERS=tuple(sp.Matrix(v) for v in affine.CORNERS)
rotations=affine.rotations
def key(vector: sp.MatrixBase) -> tuple[sp.Expr, ...]:
    return tuple(sp.simplify(item) for item in vector)


def stf(matrix: sp.MatrixBase) -> sp.Matrix:
    symmetric = sp.expand((matrix + matrix.T) / 2)
    return sp.expand(symmetric - sp.trace(symmetric) * I3 / 3)


def condition_tensor(vectors: tuple[sp.Matrix, ...]) -> sp.Matrix:
    if len(vectors) != 6:
        raise ValueError("six neighboring Bloch vectors are required")
    raw = sum(
        (direction * vector.T + vector * direction.T
         for direction, vector in zip(DIRECTIONS, vectors)),
        sp.zeros(3),
    ) / 4
    return stf(raw)


def local_distribution(vectors: tuple[sp.Matrix, ...]) -> dict[tuple[str, tuple[sp.Expr, ...]], sp.Expr]:
    """Conditional probability law on six supplied Bloch vectors; no instrument asserted."""
    tensor = condition_tensor(vectors)
    result: dict[tuple[str, tuple[sp.Expr, ...]], sp.Expr] = {}
    for direction in DIRECTIONS:
        axis = next(index for index in range(3) if direction[index] != 0)
        result[("axis", key(direction))] = sp.expand(
            sp.Rational(1, 12) + TAU * tensor[axis, axis] / 2
        )
    for corner in CORNERS:
        mixed = (
            tensor[0, 1] * corner[0] * corner[1]
            + tensor[1, 2] * corner[1] * corner[2]
            + tensor[0, 2] * corner[0] * corner[2]
        )
        result[("corner", key(corner))] = sp.expand(
            sp.Rational(1, 16) + 3 * TAU * mixed / 8
        )
    return result


def distribution_moment(
    probabilities: dict[tuple[str, tuple[sp.Expr, ...]], sp.Expr]
) -> sp.Matrix:
    raw = sp.zeros(3)
    for direction in DIRECTIONS:
        raw += probabilities[("axis", key(direction))] * direction * direction.T
    for corner in CORNERS:
        raw += probabilities[("corner", key(corner))] * corner * corner.T / 3
    return stf(raw)


def coeff_to_tensor(coefficients: sp.MatrixBase) -> sp.Matrix:
    tensor = sp.zeros(3)
    tensor[0, 0], tensor[1, 1], tensor[2, 2] = (
        coefficients[1], coefficients[2], coefficients[3]
    )
    for value, (left, right) in zip(
        (coefficients[7], coefficients[8], coefficients[9]),
        ((0, 1), (0, 2), (1, 2)),
    ):
        tensor[left, right] = tensor[right, left] = value / SQRT2
    return sp.expand(tensor)


def tensor_to_coeff(tensor: sp.MatrixBase) -> sp.Matrix:
    coefficients = sp.zeros(10, 1)
    coefficients[1], coefficients[2], coefficients[3] = (
        tensor[0, 0], tensor[1, 1], tensor[2, 2]
    )
    coefficients[7] = SQRT2 * tensor[0, 1]
    coefficients[8] = SQRT2 * tensor[0, 2]
    coefficients[9] = SQRT2 * tensor[1, 2]
    return sp.expand(coefficients)


def prepare_target(tensor: sp.MatrixBase) -> tuple[sp.Matrix, ...]:
    return tuple(sp.expand(-sp.Rational(3, 4) * tensor * direction)
                 for direction in DIRECTIONS)


def composite_corner(
    vectors: tuple[sp.Matrix, ...], corner: sp.MatrixBase
) -> sp.Matrix:
    selected = []
    for axis in range(3):
        direction = sp.zeros(3, 1)
        direction[axis] = corner[axis]
        selected.append(vectors[next(
            index for index, item in enumerate(DIRECTIONS)
            if item == direction
        )])
    return sp.expand(sum(selected, sp.zeros(3, 1)) / 3)


def norm_squared(vector: sp.MatrixBase) -> sp.Expr:
    return sp.expand((vector.T * vector)[0])


def strictly_below_one(value: sp.Expr) -> bool:
    return bool(sp.simplify(1 - value).is_positive)


@cache
def universal_facts() -> dict[str, object]:
    symbols = sp.symbols("v0:18", real=True)
    vectors = tuple(sp.Matrix(symbols[3 * index:3 * index + 3]) for index in range(6))
    tensor = condition_tensor(vectors)
    probabilities = local_distribution(vectors)
    moment = distribution_moment(probabilities)
    tensor_coordinates = (tensor[0, 0], tensor[1, 1], tensor[0, 1], tensor[0, 2], tensor[1, 2])
    condition_matrix = sp.Matrix(tensor_coordinates).jacobian(symbols)

    a, b, d, e, f = sp.symbols("A B D E F", real=True)
    generic = sp.Matrix(((a, d, e), (d, b, f), (e, f, -a - b)))
    generic_probs = []
    for direction in DIRECTIONS:
        axis = next(index for index in range(3) if direction[index] != 0)
        generic_probs.append(sp.Rational(1, 12) + TAU * generic[axis, axis] / 2)
    for corner in CORNERS:
        generic_probs.append(sp.Rational(1, 16) + 3 * TAU * (
            generic[0, 1] * corner[0] * corner[1]
            + generic[1, 2] * corner[1] * corner[2]
            + generic[0, 2] * corner[0] * corner[2]
        ) / 8)
    probability_matrix = sp.Matrix(generic_probs).jacobian((a, b, d, e, f))

    def coefficient_l1(expression: sp.Expr) -> sp.Expr:
        polynomial = sp.Poly(sp.expand(expression), *symbols)
        return sp.simplify(sum(abs(value) for value in polynomial.coeffs()))

    diagonal_l1 = tuple(coefficient_l1(tensor[index, index]) for index in range(3))
    off_diagonal_l1 = tuple(
        coefficient_l1(tensor[left, right])
        for left, right in ((0, 1), (0, 2), (1, 2))
    )
    axis_floor = sp.Rational(1, 12) - TAU * max(diagonal_l1) / 2
    corner_floor = sp.Rational(1, 16) - 3 * TAU * sum(off_diagonal_l1) / 8
    return {
        "symbols": symbols,
        "vectors": vectors,
        "tensor": tensor,
        "probabilities": probabilities,
        "normalization": sp.simplify(sum(probabilities.values())),
        "moment": moment,
        "moment_residual": sp.simplify(moment - TAU * tensor),
        "condition_rank": condition_matrix.rank(),
        "probability_rank": probability_matrix.rank(),
        "diagonal_l1": diagonal_l1,
        "off_diagonal_l1": off_diagonal_l1,
        "axis_floor": axis_floor,
        "corner_floor": corner_floor,
    }


@cache
def covariance_facts() -> dict[str, object]:
    universal = universal_facts()
    vectors = universal["vectors"]
    assert isinstance(vectors, tuple)
    tensor = universal["tensor"]
    assert isinstance(tensor, sp.MatrixBase)
    probabilities = universal["probabilities"]
    assert isinstance(probabilities, dict)
    failures = []
    for rotation in rotations():
        transformed_vectors = []
        inverse = rotation.T
        for direction in DIRECTIONS:
            old_direction = inverse * direction
            old_index = next(index for index, item in enumerate(DIRECTIONS)
                             if item == old_direction)
            transformed_vectors.append(rotation * vectors[old_index])
        transformed_vectors_tuple = tuple(transformed_vectors)
        transformed_tensor = condition_tensor(transformed_vectors_tuple)
        tensor_ok = sp.simplify(transformed_tensor - rotation * tensor * rotation.T) == sp.zeros(3)
        transformed_probabilities = local_distribution(transformed_vectors_tuple)
        probability_ok = True
        for direction in DIRECTIONS:
            old_direction = inverse * direction
            probability_ok &= sp.simplify(
                transformed_probabilities[("axis", key(direction))]
                - probabilities[("axis", key(old_direction))]
            ) == 0
        for corner in CORNERS:
            old_corner = inverse * corner
            probability_ok &= sp.simplify(
                transformed_probabilities[("corner", key(corner))]
                - probabilities[("corner", key(old_corner))]
            ) == 0
        failures.append((not tensor_ok, not probability_ok))
    return {
        "rotation_count": len(rotations()),
        "failures": tuple(failures),
    }
