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
DIRECTIONS = ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1))
DIR_INDEX = {v:i for i,v in enumerate(DIRECTIONS)}
CORNERS = tuple(itertools.product((-1,1),repeat=3))
CORNER_INDEX = {v:i for i,v in enumerate(CORNERS)}
def matrix_key(matrix: sp.MatrixBase) -> tuple[int, ...]:
    return tuple(int(value) for value in matrix)


@cache
def rotations() -> tuple[sp.ImmutableMatrix, ...]:
    result: dict[tuple[int, ...], sp.ImmutableMatrix] = {}
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                immutable = sp.ImmutableMatrix(matrix)
                result[matrix_key(immutable)] = immutable
    return tuple(result[key] for key in sorted(result))


def act_direction(rotation: sp.MatrixBase, direction: tuple[int, int, int]) -> tuple[int, int, int]:
    value = rotation * sp.Matrix(direction)
    return tuple(int(item) for item in value)


@cache
def shell_permutations() -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(DIR_INDEX[act_direction(rotation, direction)] for direction in DIRECTIONS)
        for rotation in rotations()
    )


def permute_mask(mask: int, permutation: tuple[int, ...]) -> int:
    output = 0
    for source, target in enumerate(permutation):
        if (mask >> source) & 1:
            output |= 1 << target
    return output


@cache
def corner_permutations() -> tuple[tuple[int, ...], ...]:
    return tuple(
        tuple(
            CORNER_INDEX[act_direction(rotation, corner)]
            for corner in CORNERS
        )
        for rotation in rotations()
    )


@cache
def multiplication_table() -> tuple[tuple[int, ...], ...]:
    lookup = {matrix_key(rotation): index for index, rotation in enumerate(rotations())}
    return tuple(
        tuple(lookup[matrix_key(left * right)] for right in rotations())
        for left in rotations()
    )


def orbit(seed, action) -> frozenset:
    return frozenset(action(index, seed) for index in range(len(rotations())))


def orbit_partition(items: Iterable, action) -> tuple[frozenset, ...]:
    unseen = set(items)
    result = []
    while unseen:
        seed = min(unseen)
        found = orbit(seed, action)
        result.append(found)
        unseen -= found
    return tuple(result)


def histogram(orbits: Iterable[frozenset]) -> dict[int, int]:
    return dict(sorted(Counter(len(item) for item in orbits).items()))


def full_outcome_embedding_data(items: Iterable, action) -> dict[str, object]:
    outcome_permutations = shell_permutations()
    bases = ((0, 0), (0, 1), (0, 2))
    compatible = []
    for base in bases:
        stabilizer = tuple(
            group_index
            for group_index, permutation in enumerate(outcome_permutations)
            if (permutation[base[0]], permutation[base[1]]) == base
        )
        outcome_size = len({
            (permutation[base[0]], permutation[base[1]])
            for permutation in outcome_permutations
        })
        compatible.append({
            orbit(item, action)
            for item in items
            if len(orbit(item, action)) == outcome_size
            and all(action(group_index, item) == item
                    for group_index in stabilizer)
        })
    full = (
        all(compatible)
        and any(
            len({parallel, antiparallel, perpendicular}) == 3
            for parallel in compatible[0]
            for antiparallel in compatible[1]
            for perpendicular in compatible[2]
        )
    )
    return {
        "compatible_orbit_counts": tuple(len(values) for values in compatible),
        "full": full,
    }


def shear_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in basis:
        transformed = rotation * tensor * rotation.T
        columns.append(sp.Matrix((
            transformed[0, 1],
            transformed[1, 2],
            transformed[0, 2],
        )))
    return sp.Matrix.hstack(*columns)


def gf2_rref(rows: Iterable[int], ncols: int) -> tuple[list[int], list[int]]:
    work = [row for row in dict.fromkeys(rows) if row]
    pivot_columns = []
    pivot_row = 0
    for column in range(ncols):
        found = next(
            (index for index in range(pivot_row, len(work))
             if (work[index] >> column) & 1),
            None,
        )
        if found is None:
            continue
        work[pivot_row], work[found] = work[found], work[pivot_row]
        pivot = work[pivot_row]
        for index, row in enumerate(work):
            if index != pivot_row and ((row >> column) & 1):
                work[index] ^= pivot
        pivot_columns.append(column)
        pivot_row += 1
        if pivot_row == len(work):
            break
    return work[:pivot_row], pivot_columns


def gf2_nullspace(rows: Iterable[int], ncols: int) -> tuple[int, ...]:
    reduced, pivots = gf2_rref(rows, ncols)
    pivot_set = set(pivots)
    result = []
    for free in range(ncols):
        if free in pivot_set:
            continue
        vector = 1 << free
        for row, pivot in zip(reduced, pivots):
            if (row >> free) & 1:
                vector |= 1 << pivot
        result.append(vector)
    return tuple(result)


def reduce_gf2(vector: int, basis: dict[int, int]) -> int:
    for pivot in sorted(basis, reverse=True):
        if (vector >> pivot) & 1:
            vector ^= basis[pivot]
    return vector


def add_gf2_basis(vector: int, basis: dict[int, int]) -> bool:
    vector = reduce_gf2(vector, basis)
    if not vector:
        return False
    pivot = vector.bit_length() - 1
    for other_pivot, other in list(basis.items()):
        if (other >> pivot) & 1:
            basis[other_pivot] = other ^ vector
    basis[pivot] = vector
    return True


def module_permutations(site_count: int) -> tuple[tuple[int, ...], ...]:
    if site_count == 6:
        return shell_permutations()
    if site_count == 7:
        return tuple(((0,) + tuple(value + 1 for value in permutation))
                     for permutation in shell_permutations())
    raise ValueError(site_count)


@cache
def affine_action_classes(site_count: int) -> dict[str, object]:
    permutations = module_permutations(site_count)
    table = multiplication_table()
    group_size = len(rotations())
    ncols = group_size * site_count
    rows = []
    for left in range(group_size):
        for right in range(group_size):
            product = table[left][right]
            permutation = permutations[left]
            for coordinate in range(site_count):
                row = 0
                row ^= 1 << (product * site_count + coordinate)
                row ^= 1 << (left * site_count + coordinate)
                source_coordinate = permutation.index(coordinate)
                row ^= 1 << (right * site_count + source_coordinate)
                rows.append(row)
    cocycle_basis = gf2_nullspace(rows, ncols)

    coboundaries = []
    for coordinate in range(site_count):
        seed = 1 << coordinate
        vector = 0
        for group_index, permutation in enumerate(permutations):
            value = permute_mask(seed, permutation) ^ seed
            vector |= value << (group_index * site_count)
        coboundaries.append(vector)

    span: dict[int, int] = {}
    for vector in coboundaries:
        add_gf2_basis(vector, span)
    coboundary_rank = len(span)
    quotient_representatives = []
    for vector in cocycle_basis:
        if reduce_gf2(vector, span):
            quotient_representatives.append(vector)
            add_gf2_basis(vector, span)

    classes = []
    for bits in itertools.product((0, 1), repeat=len(quotient_representatives)):
        cocycle = 0
        for bit, representative in zip(bits, quotient_representatives):
            if bit:
                cocycle ^= representative
        translations = tuple(
            (cocycle >> (group_index * site_count)) & ((1 << site_count) - 1)
            for group_index in range(group_size)
        )

        homomorphism = all(
            translations[table[left][right]]
            == (
                translations[left]
                ^ permute_mask(translations[right], permutations[left])
            )
            for left in range(group_size)
            for right in range(group_size)
        )

        def action(group_index: int, mask: int) -> int:
            return (
                permute_mask(mask, permutations[group_index])
                ^ translations[group_index]
            )

        orbits = orbit_partition(range(1 << site_count), action)
        orbit_histogram = histogram(orbits)
        embedding = full_outcome_embedding_data(
            range(1 << site_count), action
        )
        classes.append({
            "bits": bits,
            "translations": translations,
            "homomorphism": homomorphism,
            "orbit_histogram": orbit_histogram,
            "compatible_target_orbit_counts":
                embedding["compatible_orbit_counts"],
            "has_orbit24": orbit_histogram.get(24, 0) >= 1,
            "full_outcome_embedding": embedding["full"],
        })

    return {
        "site_count": site_count,
        "cocycle_dimension": len(cocycle_basis),
        "coboundary_rank": coboundary_rank,
        "h1_dimension": len(quotient_representatives),
        "class_count": len(classes),
        "classes": tuple(classes),
    }

@cache
def selected_action():
    classes=affine_action_classes(6)['classes']
    selected=[c for c in classes if c['has_orbit24']]
    if len(selected)!=1: raise ValueError('finite affine class is not unique')
    shifts=selected[0]['translations']; permutations=shell_permutations()
    def action(g,mask):
        return permute_mask(mask,permutations[g]) ^ shifts[g]
    return action

@cache
def supplied_shear_table():
    action=selected_action()
    transport={action(g,5):g for g in range(24)}
    seed=sp.Matrix((0,1/sp.sqrt(2),-1))
    return tuple(tuple(shear_representation(rotations()[transport[m]])*seed)
                 if m in transport else (sp.Integer(0),)*3 for m in range(64))


def anf_coefficients(values: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
    coefficients = list(values)
    for bit in range(6):
        for mask in range(64):
            if (mask >> bit) & 1:
                coefficients[mask] = sp.simplify(
                    coefficients[mask] - coefficients[mask ^ (1 << bit)]
                )
    return tuple(coefficients)


def evaluate_anf(
    coefficients: tuple[sp.Expr, ...], mask: int
) -> sp.Expr:
    return sp.simplify(sum(
        coefficient
        for monomial, coefficient in enumerate(coefficients)
        if monomial & ~mask == 0
    ))
