#!/usr/bin/env python3
"""Source-only extraction of exact finite block23 definitions used by the pair-process unit.
Original complete source is recoverable in eta-pair-process-correction-20260909/RECOVERY.json.
No parent controller, certification campaign, or physical standing is imported.
"""

from __future__ import annotations


import ast


import hashlib


import itertools


from dataclasses import dataclass, replace


from functools import lru_cache


from pathlib import Path


import sympy as sp


R = sp.Rational


TAU = R(1, 24)


DISPLACEMENT = 9


DIRECTIONS = tuple(
    tuple(sign if j == axis else 0 for j in range(3))
    for axis in range(3)
    for sign in (-1, 1)
)


CORNERS = tuple(itertools.product((-1, 1), repeat=3))


OUTCOMES = DIRECTIONS + CORNERS


def dot(a, b):
    return sp.simplify(sum(a[i] * b[i] for i in range(3)))


def norm2(a):
    return sp.simplify(dot(a, a))


def add(a, b):
    return tuple(sp.simplify(a[i] + b[i]) for i in range(3))


def scale(c, a):
    return tuple(sp.simplify(c * a[i]) for i in range(3))


def negate(a):
    return scale(-1, a)


def mat_vec(g, v):
    return tuple(
        sp.simplify(sum(g[i][j] * v[j] for j in range(3))) for i in range(3)
    )


def determinant3(g):
    return (
        g[0][0] * (g[1][1] * g[2][2] - g[1][2] * g[2][1])
        - g[0][1] * (g[1][0] * g[2][2] - g[1][2] * g[2][0])
        + g[0][2] * (g[1][0] * g[2][1] - g[1][1] * g[2][0])
    )


def rotations():
    answer = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[i] if j == permutation[i] else 0 for j in range(3))
                for i in range(3)
            )
            if determinant3(matrix) == 1:
                answer.append(matrix)
    assert len(set(answer)) == 24
    return tuple(answer)


ROTATIONS = rotations()


def is_axis(label):
    return sum(value != 0 for value in label) == 1


def axis_index(label):
    return next(i for i, value in enumerate(label) if value)


@lru_cache(maxsize=None)
def effect(label):
    """Return the exact Block22 constant and six local Pauli vectors."""
    coefficients = {}
    if is_axis(label):
        selected = axis_index(label)
        constant = R(1, 12)
        for site in DIRECTIONS:
            j = axis_index(site)
            epsilon = site[j]
            vector = [sp.S.Zero] * 3
            vector[j] = TAU * R(1, 4) * epsilon * (
                int(selected == j) - R(1, 3)
            )
            coefficients[site] = tuple(vector)
    else:
        constant = R(1, 16)
        for site in DIRECTIONS:
            j = axis_index(site)
            epsilon = site[j]
            vector = [sp.S.Zero] * 3
            for k in range(3):
                if k != j:
                    vector[k] = (
                        R(3, 32) * TAU * epsilon * label[j] * label[k]
                    )
            coefficients[site] = tuple(vector)
    return constant, coefficients


def expectation(label, vectors):
    constant, coefficients = effect(label)
    return sp.simplify(
        constant
        + sum(dot(coefficients[site], vectors[site]) for site in DIRECTIONS)
    )


@lru_cache(maxsize=None)
def q_matrix(label, sign=1):
    column = sp.Matrix(label)
    unit = column / sp.sqrt(sp.simplify((column.T * column)[0]))
    return sp.simplify(sign * (unit * unit.T - sp.eye(3) / 3))


@lru_cache(maxsize=None)
def prepared_vectors(label, sign=1):
    q = q_matrix(label, sign=sign)
    answer = {}
    for site in DIRECTIONS:
        raw = sp.simplify(q * sp.Matrix(site))
        length = sp.sqrt(sp.simplify((raw.T * raw)[0]))
        answer[site] = tuple(sp.simplify(raw[i] / length) for i in range(3))
    return answer


@lru_cache(maxsize=None)
def transition(source, target, sign=1):
    return sp.simplify(expectation(target, prepared_vectors(source, sign=sign)))


def scaled(site, factor):
    return tuple(factor * value for value in site)


LIVE = set(DIRECTIONS)


FRONT = {scaled(site, 2) for site in DIRECTIONS}


AXIS_SLOTS = {scaled(site, 3) for site in DIRECTIONS}


CORNER_SLOTS = {scaled(corner, 2) for corner in CORNERS}


STATUS = {scaled(site, 4) for site in DIRECTIONS}


POINTER = FRONT | AXIS_SLOTS | CORNER_SLOTS | STATUS


SUPPORT = LIVE | POINTER


POINTER_ORDER = tuple(sorted(POINTER))


def translate(sites, center):
    return {add(site, center) for site in sites}


def outcome_slot(label):
    return scaled(label, 3 if is_axis(label) else 2)


def ready_word(front):
    bits = {site: 0 for site in POINTER}
    bits[scaled(front, 2)] = 1
    return tuple(bits[site] for site in POINTER_ORDER)


def locked_word(front, outcome):
    bits = {site: 0 for site in POINTER}
    for site in STATUS:
        bits[site] = 1
    bits[scaled(front, 2)] = 1
    bits[outcome_slot(outcome)] = 1
    return tuple(bits[site] for site in POINTER_ORDER)


BLANK_POINTER = tuple(0 for _site in POINTER_ORDER)


def rotate_word(word, g):
    bits = {POINTER_ORDER[i]: word[i] for i in range(len(POINTER_ORDER))}
    moved = {mat_vec(g, site): value for site, value in bits.items()}
    return tuple(moved[site] for site in POINTER_ORDER)


def radial_bloch(site, bit=0):
    length = sp.sqrt(norm2(site))
    sign = 1 if bit == 0 else -1
    return tuple(sp.simplify(sign * value / length) for value in site)


def ordered_live(vectors):
    return tuple(vectors[site] for site in DIRECTIONS)


@dataclass(frozen=True)
class BlockProduct:
    """All 32 physical one-qubit pure factors at one Block22 anchor."""

    live: tuple
    pointer: tuple


BLANK_LIVE = ordered_live({site: radial_bloch(site, 0) for site in DIRECTIONS})


BLANK_BLOCK = BlockProduct(BLANK_LIVE, BLANK_POINTER)


def block_product(live_vectors, pointer_word):
    return BlockProduct(ordered_live(live_vectors), pointer_word)


@lru_cache(maxsize=None)
def rotate_live(live, g):
    source = {site: live[index] for index, site in enumerate(DIRECTIONS)}
    moved = {
        mat_vec(g, site): mat_vec(g, vector) for site, vector in source.items()
    }
    return tuple(moved[site] for site in DIRECTIONS)


@lru_cache(maxsize=None)
def rotate_block_product(block, g):
    return BlockProduct(rotate_live(block.live, g), rotate_word(block.pointer, g))


def pure_overlap(left, right):
    return sp.simplify((1 + dot(left, right)) / 2)


@lru_cache(maxsize=None)
def pointer_overlap(left, right):
    return sp.simplify(
        sp.prod(
            pure_overlap(
                radial_bloch(site, left[index]),
                radial_bloch(site, right[index]),
            )
            for index, site in enumerate(POINTER_ORDER)
        )
    )


@lru_cache(maxsize=None)
def block_overlap(left, right):
    return sp.simplify(
        pointer_overlap(left.pointer, right.pointer)
        * sp.prod(pure_overlap(left.live[i], right.live[i]) for i in range(6))
    )


OLD_LIVE_IDENTITIES = tuple((site, "I_2") for site in DIRECTIONS)


def projector_reduce(expression, symbol):
    polynomial = sp.Poly(sp.expand(expression), symbol)
    relation = sp.Poly(symbol ** 2 - symbol, symbol)
    return sp.simplify(sp.rem(polynomial, relation).as_expr())


def effect_equal(left, right):
    if sp.simplify(left[0] - right[0]) != 0:
        return False
    return all(
        all(sp.simplify(left[1][site][k] - right[1][site][k]) == 0 for k in range(3))
        for site in DIRECTIONS
    )


@lru_cache(maxsize=None)
def spectral_resolution(label):
    constant, coefficients = effect(label)
    norms = {
        site: sp.sqrt(sp.simplify(dot(vector, vector)))
        for site, vector in coefficients.items()
    }
    values = {
        signs: sp.simplify(
            constant
            + sum(signs[index] * norms[site] for index, site in enumerate(DIRECTIONS))
        )
        for signs in itertools.product((-1, 1), repeat=6)
    }
    return norms, values


def walsh(values, subset):
    return sp.simplify(
        sum(
            sp.prod(signs[index] for index in subset) * value
            for signs, value in values.items()
        ) / 64
    )


def decode_ready_word(word):
    matches = [front for front in DIRECTIONS if word == ready_word(front)]
    return matches[0] if len(matches) == 1 else None


def decode_locked_word(word):
    matches = [
        (front, outcome)
        for front in DIRECTIONS
        for outcome in OUTCOMES
        if word == locked_word(front, outcome)
    ]
    return matches[0] if len(matches) == 1 else None


def live_dictionary(live):
    return {site: live[index] for index, site in enumerate(DIRECTIONS)}


@lru_cache(maxsize=None)
def root_spectrum(label):
    _norms, values = spectral_resolution(label)
    return tuple(
        (signs, sp.sqrt(value)) for signs, value in sorted(values.items())
    )


@lru_cache(maxsize=None)
def root_operator_factor(label):
    """Store the complete commuting spectral root: local axes and 64 roots."""
    _constant, coefficients = effect(label)
    norms, _values = spectral_resolution(label)
    local_axes = tuple(
        (
            site,
            (sp.S.Zero,) * 3
            if norms[site] == 0
            else scale(1 / norms[site], coefficients[site]),
        )
        for site in DIRECTIONS
    )
    return label, local_axes, root_spectrum(label)


@lru_cache(maxsize=None)
def contract_root_adjoint_root(root_factor):
    """Contract a stored spectral root, including every higher Walsh sector."""
    _label, local_axes, spectrum = root_factor
    squared_values = {
        signs: sp.simplify(root * root) for signs, root in spectrum
    }
    higher_terms = tuple(
        walsh(squared_values, subset)
        for order in range(2, 7)
        for subset in itertools.combinations(range(6), order)
    )
    if any(sp.simplify(value) != 0 for value in higher_terms):
        raise ValueError("root contraction contains higher Pauli sectors")
    axes = dict(local_axes)
    return (
        walsh(squared_values, ()),
        {
            site: scale(walsh(squared_values, (index,)), axes[site])
            for index, site in enumerate(DIRECTIONS)
        },
    )


def expectation_from_effect_data(effect_data, vectors):
    constant, coefficients = effect_data
    return sp.simplify(
        constant
        + sum(dot(coefficients[site], vectors[site]) for site in DIRECTIONS)
    )


def pointer_rank_one_maps(input_word, output_word):
    return tuple(
        (site, input_word[index], output_word[index])
        for index, site in enumerate(POINTER_ORDER)
    )
