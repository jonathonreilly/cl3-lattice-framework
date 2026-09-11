#!/usr/bin/env python3
"""Finite constructors for the released #7359-A recovery.

This module extracts only the exact constructions needed by the corrected
Blocks 176--179 runners.  The antiperiodic cover, Hodge quotient, connection,
carrier, and temporal reflection come from the reviewed released7332--7334
finite helper, which in turn binds the current Block 105 matrices.  No theorem,
audit status, physical interpretation, probability law, or premise is imported
from the archived 49-script chain.
"""

from __future__ import annotations

from collections import Counter
import hashlib
import itertools
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_released7332_7334_fixtures_2026_09_10 as base


ROOT = Path(__file__).resolve().parents[1]
BASE_HELPER_PATH = (
    "scripts/admissibility_dirac_kahler_released7332_7334_"
    "fixtures_2026_09_10.py"
)
BASE_HELPER_SHA256 = "594e7032f453fec4c6791067a147d1544636ddce9567a87a3449352b5546d5f5"

R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I = sp.I
SX = base.SX
ST = base.ST
MASS = base.MASS

COVER_EXTENTS = (("8x4", 8, 4), ("12x4", 12, 4))
MENU = (ZERO, R(1, 5), R(2, 5), R(3, 5))
AMBIENT_SIGMA = R(3, 5)
CONSTANT_VOLUME = R(7, 5)
PINNED_LEVELS = (0, 1)
VOLUME_PROFILE = (1, 2, 3, 4)
VOLUME_DIAGONAL = (R(25, 16), R(3, 2), R(17, 8), R(17, 6))
OMEGA = (-ONE + sp.sqrt(3) * I) / 2
P3 = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])


def sha256_path(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def supplier_certificate() -> bool:
    """Bind the complete live finite-constructor chain."""
    return bool(
        sha256_path(ROOT / BASE_HELPER_PATH) == BASE_HELPER_SHA256
        and base.supplier_certificate()
    )


def matrix_zero(matrix: sp.MatrixBase) -> bool:
    return all(sp.expand(value) == 0 for value in matrix)


def exact_scalar(value):
    return sp.cancel(sp.expand(sp.simplify(value)))


def nnz(matrix: sp.MatrixBase) -> int:
    return sum(sp.expand(value) != 0 for value in matrix)


def support(matrix: sp.MatrixBase) -> frozenset[tuple[int, int]]:
    return frozenset(
        (row, column)
        for row in range(matrix.rows)
        for column in range(matrix.cols)
        if sp.expand(matrix[row, column]) != 0
    )


def value_set(matrix: sp.MatrixBase) -> frozenset:
    return frozenset(
        sp.expand(value) for value in matrix if sp.expand(value) != 0
    )


def carrier_field(bench: base.Bench, shear_of, volume_of) -> dict:
    return {
        (time, space): (
            sp.sympify(shear_of(time, space)),
            sp.sympify(volume_of(time, space)),
        )
        for time, space in bench.fx.CELLS
    }


def hodge_from(bench: base.Bench, field: dict) -> sp.Matrix:
    substitutions = base.finite.carrier_substitution(bench.fx, field)
    sparse = base.finite.ssubs(bench.fx.H_free, substitutions)
    return sp.expand(
        base.finite.dense(
            bench.fx.quotient(sparse), bench.N, bench.N
        )
    )


def hodge_from_moduli(bench: base.Bench, substitutions: dict) -> sp.Matrix:
    sparse = base.finite.ssubs(bench.fx.H_free, substitutions)
    return sp.expand(
        base.finite.dense(
            bench.fx.quotient(sparse), bench.N, bench.N
        )
    )


def connection_from(bench: base.Bench, field: dict) -> sp.Matrix:
    substitutions = base.finite.carrier_substitution(bench.fx, field)
    hodge = base.finite.ssubs(bench.fx.H_free, substitutions)
    sparse = bench.fx.quotient_connection(
        bench.fx.edge_d[(0, 0)], hodge
    )
    return sp.expand(base.finite.dense(sparse, bench.N, bench.N))


def action_from(
    bench: base.Bench,
    field: dict,
    sx=R(3, 5),
    st=ZERO,
    mass=ONE,
) -> sp.Matrix:
    substitutions = base.finite.carrier_substitution(bench.fx, field)
    substitutions.update({SX: sp.sympify(sx), ST: sp.sympify(st), MASS: sp.sympify(mass)})
    return sp.expand(bench.Q.subs(substitutions))


def commutator_defect(bench: base.Bench, matrix: sp.MatrixBase) -> sp.Matrix:
    """Historical comparison r X r-X; not the antiunitary condition."""
    return sp.expand(bench.r * matrix * bench.r - matrix)


def transpose_defect(bench: base.Bench, matrix: sp.MatrixBase) -> sp.Matrix:
    """Antiunitary quadratic-form condition r X r=X^T."""
    return sp.expand(bench.r * matrix * bench.r - matrix.T)


def hop_census(bench: base.Bench, matrix: sp.MatrixBase) -> dict:
    counter: Counter = Counter()
    for row, column in support(matrix):
        time_row, space_row = divmod(row, bench.lx)
        time_col, space_col = divmod(column, bench.lx)
        dt = (time_row - time_col) % bench.T
        dx = (space_row - space_col) % bench.lx
        counter[(min(dt, (-dt) % bench.T), min(dx, (-dx) % bench.lx))] += 1
    return dict(sorted(counter.items()))


def selected_reflected_covariance(
    bench: base.Bench, action: sp.MatrixBase
) -> tuple[sp.Matrix, sp.Matrix]:
    inverse = base.finite.exact_inv(sp.Matrix(action))
    product = sp.expand(bench.r * inverse.T)
    raw = sp.Matrix(
        len(bench.rows),
        len(bench.rows),
        lambda row, column: product[
            bench.rows[row], bench.rows[column]
        ],
    )
    hermitian = sp.expand((raw + raw.H) / 2)
    return raw, hermitian


def realify(matrix: sp.MatrixBase) -> sp.Matrix:
    matrix = sp.Matrix(matrix)
    real = matrix.applyfunc(sp.re)
    imaginary = matrix.applyfunc(sp.im)
    return sp.Matrix.vstack(
        sp.Matrix.hstack(real, -imaginary),
        sp.Matrix.hstack(imaginary, real),
    )


def permanent(matrix: sp.MatrixBase):
    return sp.expand(
        sum(
            (
                sp.prod(matrix[row, permutation[row]] for row in range(matrix.rows))
                for permutation in itertools.permutations(range(matrix.rows))
            ),
            ZERO,
        )
    )


def monomial_gram(
    kernel: sp.MatrixBase,
    word_left: tuple[int, ...],
    word_right: tuple[int, ...],
):
    block = sp.Matrix(
        len(word_left),
        len(word_right),
        lambda row, column: kernel[word_left[row], word_right[column]],
    )
    return permanent(block)


def constant_wide_fixture() -> tuple[base.Bench, tuple[int, ...], sp.Matrix]:
    """The disclosed 12x6 constant-volume finite action."""
    bench = base.Bench("released7359-a-12x6", 12, 6)
    pinned = tuple(sorted({(bench.c - 1) % bench.T, bench.c % bench.T}))
    field = carrier_field(
        bench,
        lambda time, _space: ZERO if time in pinned else AMBIENT_SIGMA,
        lambda _time, _space: CONSTANT_VOLUME,
    )
    return bench, pinned, action_from(bench, field)


def chart_translation(bench: base.Bench) -> sp.Matrix:
    translation = sp.zeros(bench.N)
    for time in range(bench.T):
        for space in range(bench.lx):
            translation[
                bench.lx * time + (space + 2) % bench.lx,
                bench.lx * time + space,
            ] = ONE
    return translation


def chart_character(
    bench: base.Bench, time: int, parity: int, momentum: int
) -> sp.Matrix:
    vector = sp.zeros(bench.N, 1)
    for index in range(3):
        vector[bench.lx * time + parity + 2 * index] = (
            OMEGA ** (-momentum * index) / sp.sqrt(3)
        )
    return vector


def orbit_embedding(bench: base.Bench, time: int, parity: int) -> sp.Matrix:
    embedding = sp.zeros(bench.N, 3)
    for index in range(3):
        embedding[bench.lx * time + parity + 2 * index, index] = ONE
    return embedding


def supplied_slot_ratio(slot_count: int):
    """Historical flavor convention retained as an explicit supplied map."""
    return R(slot_count, 2)


def supplied_q_from_ratio(ratio):
    """Historical flavor convention retained as an explicit supplied map."""
    return sp.cancel((ONE + 2 * sp.sympify(ratio)) / 3)


def source_hygiene(paths: tuple[str, ...], hashes: dict[str, str]) -> bool:
    return bool(
        tuple(hashes) == paths
        and all(len(value) == 64 for value in hashes.values())
        and {path: sha256_path(ROOT / path) for path in paths} == hashes
        and supplier_certificate()
    )
