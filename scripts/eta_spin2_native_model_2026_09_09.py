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
R=sp.Rational
I=sp.I
SQRT2=sp.sqrt(2)
MASS=R(2,7)
FORM_SUBSETS=tuple(tuple(i for i in range(4) if mask&(1<<i)) for mask in range(16))
FORM_INDEX={v:i for i,v in enumerate(FORM_SUBSETS)}
def exterior_creation(axis: int) -> sp.Matrix:
    result = sp.zeros(16)
    for column, subset in enumerate(FORM_SUBSETS):
        if axis in subset:
            continue
        target = tuple(sorted(subset + (axis,)))
        sign = (-1) ** sum(item < axis for item in subset)
        result[FORM_INDEX[target], column] = sign
    return result

CREATION=tuple(exterior_creation(i) for i in range(4))
ANNIHILATION=tuple(c.T for c in CREATION)
NUMBER=tuple(c*a for c,a in zip(CREATION,ANNIHILATION))
IDENTITY_FORM=sp.eye(16)
PAIRS4=((3,3),(0,0),(1,1),(2,2),(0,3),(1,3),(2,3),(0,1),(0,2),(1,2))
SPATIAL_SLOTS=(1,2,3,7,8,9)
def centered_differential(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.expand(sum(
        (sp.sin(momentum[axis]) * CREATION[axis] for axis in range(4)),
        sp.zeros(16),
    ))


def centered_objects(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[sp.Matrix, tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    differential_0 = centered_differential(incoming)
    differential_1 = centered_differential(outgoing)
    action = sp.expand(
        MASS * IDENTITY_FORM
        + I * (differential_0 + differential_0.T)
    )
    cosines = tuple(
        sp.cos(incoming[axis] + transfer[axis] / 2)
        for axis in range(4)
    )
    hodge_vertices: list[sp.Matrix] = []
    for left, right in PAIRS4:
        if left == right:
            vertex = cosines[left] ** 2 * (
                R(1, 2) * IDENTITY_FORM - NUMBER[left]
            )
        else:
            vertex = -cosines[left] * cosines[right] / SQRT2 * (
                CREATION[left] * ANNIHILATION[right]
                + CREATION[right] * ANNIHILATION[left]
            )
        hodge_vertices.append(sp.expand(vertex))
    action_vertices = tuple(
        sp.expand(
            MASS * vertex
            + I * (
                vertex * differential_0
                + differential_1.T * vertex
            )
        )
        for vertex in hodge_vertices
    )
    return action, tuple(hodge_vertices), action_vertices


def tensor_basis4() -> tuple[sp.Matrix, ...]:
    result = []
    for left, right in PAIRS4:
        matrix = sp.zeros(4)
        value = 1 if left == right else 1 / SQRT2
        matrix[left, right] = value
        matrix[right, left] = value
        result.append(matrix)
    return tuple(result)

TENSOR_BASIS4=tensor_basis4()
def wedge_representation(transform: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(16)
    for column, subset in enumerate(FORM_SUBSETS):
        images: list[int] = []
        coefficient = sp.Integer(1)
        for old_axis in subset:
            rows = [row for row in range(4) if transform[row, old_axis] != 0]
            new_axis = rows[0]
            coefficient *= transform[new_axis, old_axis]
            images.append(new_axis)
        inversions = sum(
            images[left] > images[right]
            for left in range(len(images))
            for right in range(left + 1, len(images))
        )
        coefficient *= (-1) ** inversions
        result[FORM_INDEX[tuple(sorted(images))], column] = coefficient
    return result


def tensor_representation(transform: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(10, 10, lambda row, column: sp.trace(
        TENSOR_BASIS4[row].T
        * transform * TENSOR_BASIS4[column] * transform.T
    ))


def symmetric_basis3() -> tuple[sp.Matrix, ...]:
    result = []
    for left, right in ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)):
        matrix = sp.zeros(3)
        value = 1 if left == right else 1 / SQRT2
        matrix[left, right] = value
        matrix[right, left] = value
        result.append(matrix)
    return tuple(result)

SYMMETRIC_BASIS3=symmetric_basis3()
def tt_basis(spatial_incidence: sp.Matrix) -> sp.Matrix:
    rows = [sp.Matrix([[sp.trace(item) for item in SYMMETRIC_BASIS3]])]
    for axis in range(3):
        rows.append(sp.Matrix([[
            (item * spatial_incidence)[axis] for item in SYMMETRIC_BASIS3
        ]]))
    constraint = sp.Matrix.vstack(*rows)
    spatial_section = sp.Matrix.hstack(*constraint.nullspace())
    embedding = sp.zeros(10, 6)
    for column, row in enumerate(SPATIAL_SLOTS):
        embedding[row, column] = 1
    return sp.expand(embedding * spatial_section)

POINTS={
'H1':((sp.pi/6,sp.pi/3,0,sp.pi/6),(sp.pi/3,sp.pi/2,0,0)),
'H2':((sp.pi/4,sp.pi/6,sp.pi/3,sp.pi/6),(sp.pi/6,sp.pi/3,sp.pi/2,0))}
def tt_source_coefficients(name):
    q=POINTS[name][1]
    return tt_basis(sp.Matrix([2*sp.sin(q[i]/2) for i in range(3)]))[:,1].applyfunc(sp.simplify)
