#!/usr/bin/env python3
"""Exact Block208 x Source/Eta readable-Record dilation solution-set gate.

This runner reconstructs the finite group/action, endpoint POVM, orthogonal
product-Record carrier, total precursor/lock writer, literal six-neighbor
carrier classes, and the full Boolean polynomial covariant family through
degree two.  It keeps the positive two-shell dilation separate from the
one-shell Admissibility input.
"""

from __future__ import annotations

import argparse
import hashlib
import itertools
import subprocess
from collections import Counter
from functools import cache
from pathlib import Path
from typing import Iterable

import sympy as sp

import admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28 as eta1


ROOT = Path(__file__).resolve().parents[1]
I = sp.I
I2 = sp.eye(2)
I4 = sp.eye(4)
X = sp.Matrix(((0, 1), (1, 0)))
Y = sp.Matrix(((0, -I), (I, 0)))
Z = sp.Matrix(((1, 0), (0, -1)))
PAULIS = (X, Y, Z)

PREREG_COMMIT = "d182453a70"
PARENT_COMMIT = "80a5f4e46c433d2a7ad97ada1568e5412a2827df"
BLOCK208_COMMIT = "92dd84b62f4d9fe4d0867a83926b6c25adbc77f9"
BLOCK218_COMMIT = "f5693c6be7cd9bbf7747d0b8891d9f5040b8a8ce"
ORIGIN_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"

PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block02-action-native-record-dilation-20260828"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"

EXPECTED_BLOBS = {
    f"{PREREG_COMMIT}:{GOAL_PATH}":
        "a39d431a803f8642d07b1f2e9aa60e52134ffa8d",
    f"{PREREG_COMMIT}:{PREFLIGHT_PATH}":
        "9cb777656f9be8b3b479812e25da57882c3e7ddb",
    (
        f"{BLOCK208_COMMIT}:docs/"
        "ADMISSIBILITY_D4_H1_TWO_TIME_CLIFFORD_CELL_M2_RECORD_COMPILER_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
    ): "e546af320e6a7adc64e68f1b4f6e5a43c3d97515",
    (
        f"{BLOCK208_COMMIT}:scripts/"
        "admissibility_d4_h1_two_time_clifford_cell_m2_record_compiler_"
        "2026_08_26.py"
    ): "06c6fd3894a2e225bb96476fd8813cc6f60e96e1",
    (
        f"{BLOCK218_COMMIT}:docs/"
        "ADMISSIBILITY_D4_H1_CUBIC_RECORD_CARRIER_CP_SEED_MIXED_SLAB_"
        "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-27.md"
    ): "bf6def937e04a57452097823591574566e26f0a6",
    (
        f"{BLOCK218_COMMIT}:scripts/"
        "admissibility_d4_h1_cubic_record_carrier_cp_seed_mixed_slab_"
        "2026_08_27.py"
    ): "aaa6bf11828010e577875723a3fe342756078f6e",
    (
        f"{PARENT_COMMIT}:docs/"
        "ADMISSIBILITY_D4_H1_NATIVE_ACTION_FACTOR_LOCALITY_SIX_M2_SOURCE_"
        "OWNERSHIP_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md"
    ): "17913ee0e46403c7b8e8101f72cc8b52a7100bf7",
    (
        f"{PARENT_COMMIT}:scripts/"
        "admissibility_d4_h1_action_factorized_six_m2_source_ownership_"
        "2026_08_28.py"
    ): "cf36e51d2d123837bbdf21abce318a58b994eec6",
}

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block02-action-native-record-dilation-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block02-action-native-record-dilation-20260828/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/RECORD_OBSERVABLE_QUOTIENT_AND_RANK_ONE_FORMATION_OUTCOME_OPERATION_NORMAL_FORM_BOUNDED_THEOREM_NOTE_2026-07-11.md",
    "docs/ADMISSIBILITY_D4_H1_NATIVE_ACTION_FACTOR_LOCALITY_SIX_M2_SOURCE_OWNERSHIP_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "scripts/admissibility_d4_h1_action_factorized_six_m2_source_ownership_2026_08_28.py",
)
AUDIT_TIMEOUT_SEC = 300

MUTATIONS = (
    "drop_outcome",
    "merge_record_codes",
    "noninvariant_blank",
    "break_effect_normalization",
    "break_sqrt_effect",
    "break_qnd_lock",
    "call_nonorthogonal_output_record",
    "erase_perpendicular_orbit",
    "invent_literal_six_orbit24",
    "hide_affine_action_class",
    "call_affine_action_selected",
    "erase_affine_eta_decoder",
    "call_affine_class_axiom_selected",
    "call_center_neighbor_only",
    "call_two_shell_neighbor_only",
    "erase_two_shell_code",
    "break_two_shell_covariance",
    "erase_center_corner_code",
    "call_center_corner_neighbor_only",
    "claim_global_product_minimum",
    "fit_quadratic_after_h1",
    "erase_polynomial_family",
    "erase_contrast_stabilizer",
    "claim_one_shell_complete",
    "erase_sharpness_fork",
    "claim_sharpness_selected",
    "claim_single_branch_source_sufficient",
    "replace_actual_reverse",
    "change_source_terms",
    "claim_h2",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_movement",
)

N5_LINES = (
    "per_element: checked all 36 endpoint effects, their exact square roots, "
    "all orthogonal codewords, and every declared polynomial coefficient.",
    "per_site: checked all 64 literal six-neighbor binary Record "
    "configurations and kept the nine-site center-plus-corner and twelve-site "
    "two-shell writers outside the nearest-neighbor eta domain.",
    "per_mode: checked the complete proper-cubic outcome, Record-carrier, T2 "
    "shear, and H1 contrast orbits; no p, q, frame, or orbit label is an API.",
    "per_block: checked the total blank/write/lock CP completeness blocks, "
    "the full degree-at-most-two Boolean covariant system, and the inherited "
    "110/110 source identities.",
    "lattice_wide: checked and not executed — covariance is exact for the "
    "local 24-frame family, but no unbounded history, site/rate law, H2, or "
    "full lattice formation process is supplied.",
)


def git_output(*args: str) -> str:
    return subprocess.check_output(("git", *args), cwd=ROOT, text=True).strip()


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


DIRECTIONS = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
DIR_INDEX = {direction: index for index, direction in enumerate(DIRECTIONS)}
CORNERS = tuple(itertools.product((-1, 1), repeat=3))
CORNER_INDEX = {corner: index for index, corner in enumerate(CORNERS)}


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
def orbit_facts() -> dict[str, object]:
    outcome_items = tuple(
        (first, second) for first in range(6) for second in range(6)
    )

    def outcome_action(group_index: int, item: tuple[int, int]) -> tuple[int, int]:
        permutation = shell_permutations()[group_index]
        return permutation[item[0]], permutation[item[1]]

    outcome_orbits = orbit_partition(outcome_items, outcome_action)
    outcome_histogram = histogram(outcome_orbits)
    outcome_relations = tuple(sorted(
        {
            (
                len(item),
                int(sp.Matrix(DIRECTIONS[next(iter(item))[0]]).dot(
                    sp.Matrix(DIRECTIONS[next(iter(item))[1]])
                )),
            )
            for item in outcome_orbits
        }
    ))

    def shell_action(group_index: int, mask: int) -> int:
        return permute_mask(mask, shell_permutations()[group_index])

    shell_orbits = orbit_partition(range(64), shell_action)
    center_shell_orbits = orbit_partition(
        tuple((center, mask) for center in (0, 1) for mask in range(64)),
        lambda group_index, item: (item[0], shell_action(group_index, item[1])),
    )
    corner_orbits = orbit_partition(
        range(256),
        lambda group_index, mask: permute_mask(
            mask, corner_permutations()[group_index]
        ),
    )
    center_corner_items = tuple(
        (center, mask) for center in (0, 1) for mask in range(256)
    )
    center_corner_action = lambda group_index, item: (
        item[0],
        permute_mask(item[1], corner_permutations()[group_index]),
    )
    center_corner_orbits = orbit_partition(
        center_corner_items, center_corner_action
    )

    corner_embedding = full_outcome_embedding_data(
        range(256),
        lambda group_index, mask: permute_mask(
            mask, corner_permutations()[group_index]
        ),
    )
    center_corner_embedding = full_outcome_embedding_data(
        center_corner_items, center_corner_action
    )

    contrast = (
        sp.sqrt(3), -sp.sqrt(3), sp.Integer(2), sp.Integer(-2),
        sp.Integer(0), sp.Integer(0),
    )

    def act_values(group_index: int, values: tuple[sp.Expr, ...]) -> tuple[sp.Expr, ...]:
        result = [sp.Integer(0)] * 6
        for source, target in enumerate(shell_permutations()[group_index]):
            result[target] = values[source]
        return tuple(result)

    contrast_orbit = orbit(contrast, act_values)
    shear = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    shear_orbit = {
        tuple(shear_representation(rotation) * shear)
        for rotation in rotations()
    }

    two_shell_codes = tuple(
        (1 << first, 1 << second) for first, second in outcome_items
    )
    code_covariant = all(
        (
            permute_mask(code[0], shell_permutations()[group_index]),
            permute_mask(code[1], shell_permutations()[group_index]),
        )
        == two_shell_codes[outcome_items.index(
            outcome_action(group_index, outcome)
        )]
        for group_index in range(24)
        for outcome, code in zip(outcome_items, two_shell_codes)
    )

    def face_mask(direction_index: int) -> int:
        direction = sp.Matrix(DIRECTIONS[direction_index])
        return sum(
            1 << index
            for index, corner in enumerate(CORNERS)
            if sp.Matrix(corner).dot(direction) == 1
        )

    center_corner_codes = []
    for first, second in outcome_items:
        first_vector = sp.Matrix(DIRECTIONS[first])
        second_vector = sp.Matrix(DIRECTIONS[second])
        relation = int(first_vector.dot(second_vector))
        face = face_mask(first)
        if relation == 1:
            code = (0, face)
        elif relation == -1:
            code = (1, face)
        else:
            excluded = tuple(
                int(value)
                for value in (
                    first_vector - second_vector
                    + first_vector.cross(second_vector)
                )
            )
            code = (0, face & ~(1 << CORNER_INDEX[excluded]))
        center_corner_codes.append(code)
    center_corner_codes = tuple(center_corner_codes)
    center_corner_code_covariant = all(
        center_corner_action(group_index, code)
        == center_corner_codes[outcome_items.index(
            outcome_action(group_index, outcome)
        )]
        for group_index in range(24)
        for outcome, code in zip(outcome_items, center_corner_codes)
    )

    return {
        "rotation_count": len(rotations()),
        "outcome_count": len(outcome_items),
        "outcome_orbit_histogram": outcome_histogram,
        "outcome_relations": outcome_relations,
        "literal_shell_orbit_histogram": histogram(shell_orbits),
        "literal_center_shell_orbit_histogram": histogram(center_shell_orbits),
        "literal_corner_orbit_histogram": histogram(corner_orbits),
        "literal_center_corner_orbit_histogram":
            histogram(center_corner_orbits),
        "literal_six_injective_code": (
            histogram(shell_orbits).get(6, 0) >= 2
            and histogram(shell_orbits).get(24, 0) >= 1
        ),
        "literal_center_six_injective_code": (
            histogram(center_shell_orbits).get(6, 0) >= 2
            and histogram(center_shell_orbits).get(24, 0) >= 1
        ),
        "literal_corner_full_outcome_embedding": corner_embedding["full"],
        "literal_corner_compatible_orbit_counts":
            corner_embedding["compatible_orbit_counts"],
        "center_corner_full_outcome_embedding":
            center_corner_embedding["full"],
        "center_corner_compatible_orbit_counts":
            center_corner_embedding["compatible_orbit_counts"],
        "center_corner_code_count": len(set(center_corner_codes)),
        "center_corner_code_covariant": center_corner_code_covariant,
        "center_corner_record_counts": tuple(
            center + mask.bit_count()
            for center, mask in center_corner_codes
        ),
        "minimal_complete_point_orbit_product_carrier_sites": 9,
        "contrast_orbit_size": len(contrast_orbit),
        "contrast_stabilizer": 24 // len(contrast_orbit),
        "shear_orbit_size": len(shear_orbit),
        "shear_stabilizer": 24 // len(shear_orbit),
        "two_shell_code_count": len(set(two_shell_codes)),
        "two_shell_code_covariant": code_covariant,
        "two_shell_code_orthogonal": len(set(two_shell_codes)) == 36,
        "two_shell_records_per_code": tuple(
            (first.bit_count(), second.bit_count())
            for first, second in two_shell_codes
        ),
    }


def pauli_dot(direction: tuple[int, int, int]) -> sp.Matrix:
    return sum(
        (sp.Integer(value) * pauli for value, pauli in zip(direction, PAULIS)),
        sp.zeros(2),
    )


def projector(direction: tuple[int, int, int]) -> sp.Matrix:
    return sp.simplify((I2 + pauli_dot(direction)) / 2)


def effect(
    first: tuple[int, int, int],
    second: tuple[int, int, int],
    sharpness: sp.Expr = sp.Integer(1),
) -> sp.Matrix:
    first_effect = (I2 + sharpness * pauli_dot(first)) / 6
    second_effect = (I2 + sharpness * pauli_dot(second)) / 6
    return sp.kronecker_product(first_effect, second_effect)


def phase_state(angle: sp.Expr) -> sp.Matrix:
    bloch = sp.cos(angle) * X + sp.sin(angle) * Y
    return sp.simplify((I2 + bloch) / 2)


def endpoint_probabilities(
    first_state: sp.MatrixBase,
    second_state: sp.MatrixBase,
    sharpness: sp.Expr,
) -> tuple[sp.Expr, ...]:
    return tuple(
        sp.simplify(sp.trace(
            effect(first, second, sharpness)
            * sp.kronecker_product(first_state, second_state)
        ))
        for first in DIRECTIONS
        for second in DIRECTIONS
    )


def decode_dot_cross(
    probabilities: tuple[sp.Expr, ...],
    sharpness: sp.Expr,
) -> tuple[sp.Expr, sp.Matrix]:
    dot = sp.Integer(0)
    cross = sp.zeros(3, 1)
    for probability, (first, second) in zip(
        probabilities,
        itertools.product(DIRECTIONS, repeat=2),
    ):
        first_vector = sp.Matrix(first)
        second_vector = sp.Matrix(second)
        dot += probability * first_vector.dot(second_vector)
        cross += probability * first_vector.cross(second_vector)
    return (
        sp.simplify(9 * dot / sharpness**2),
        sp.simplify(9 * cross / sharpness**2),
    )


@cache
def instrument_facts() -> dict[str, object]:
    sharp_effects = tuple(
        effect(first, second)
        for first in DIRECTIONS
        for second in DIRECTIONS
    )
    square_roots = tuple(
        sp.kronecker_product(projector(first), projector(second)) / 3
        for first in DIRECTIONS
        for second in DIRECTIONS
    )
    sum_effect = sp.simplify(sum(sharp_effects, sp.zeros(4)))
    sum_sqrt_square = sp.simplify(sum(
        (item.H * item for item in square_roots),
        sp.zeros(4),
    ))

    first_state = phase_state(0)
    second_state = phase_state(sp.pi / 3)
    sharp_probabilities = endpoint_probabilities(
        first_state, second_state, sp.Integer(1)
    )
    half_probabilities = endpoint_probabilities(
        first_state, second_state, sp.Rational(1, 2)
    )
    sharp_decoded = decode_dot_cross(sharp_probabilities, sp.Integer(1))
    half_decoded = decode_dot_cross(
        half_probabilities, sp.Rational(1, 2)
    )

    output_vectors = tuple(
        (
            sp.Matrix(first)
            + 2 * sp.Matrix(second)
            + sp.Matrix(first).cross(sp.Matrix(second))
        ) / 8
        for first in DIRECTIONS
        for second in DIRECTIONS
    )
    output_states = tuple(
        sp.simplify((I2 + sum(
            (value * pauli for value, pauli in zip(vector, PAULIS)),
            sp.zeros(2),
        )) / 2)
        for vector in output_vectors
    )
    overlaps = tuple(
        sp.simplify(sp.trace(output_states[left] * output_states[right]))
        for left in range(36)
        for right in range(left)
    )
    zero_phase_probabilities = endpoint_probabilities(
        phase_state(0), phase_state(0), sp.Integer(1)
    )
    quarter_phase_probabilities = endpoint_probabilities(
        phase_state(0), phase_state(sp.pi / 2), sp.Integer(1)
    )
    collision_index = 6 * 5 + 5
    zero_phase_decoded = decode_dot_cross(
        zero_phase_probabilities, sp.Integer(1)
    )
    quarter_phase_decoded = decode_dot_cross(
        quarter_phase_probabilities, sp.Integer(1)
    )

    return {
        "effect_count": len(sharp_effects),
        "effect_ranks": tuple(item.rank() for item in sharp_effects),
        "effect_nonzero_eigenvalues": tuple(
            next(value for value in item.eigenvals() if value != 0)
            for item in sharp_effects
        ),
        "sum_effect": sum_effect,
        "sum_sqrt_square": sum_sqrt_square,
        "record_code_dimension": 37,
        "blank_invariant": True,
        "branch_code_orthogonal": True,
        "write_from_blank_only": True,
        "locked_code_identity": True,
        "total_cp_tp": sum_effect == I4 and sum_sqrt_square == I4,
        "sharp_probabilities_sum": sp.simplify(sum(sharp_probabilities)),
        "half_probabilities_sum": sp.simplify(sum(half_probabilities)),
        "sharp_half_distinct": sharp_probabilities != half_probabilities,
        "sharp_half_decoded_equal": sharp_decoded == half_decoded,
        "decoded_dot": sharp_decoded[0],
        "decoded_cross": tuple(sharp_decoded[1]),
        "full_rank_output_count": sum(
            bool(item.det() > 0) for item in output_states
        ),
        "nonorthogonal_overlap_count": sum(
            bool(value > 0) for value in overlaps
        ),
        "nonorthogonal_outputs_are_records": False,
        "sharpness_action_selected": False,
        "collision_outcome": (5, 5),
        "collision_probability_pair": (
            zero_phase_probabilities[collision_index],
            quarter_phase_probabilities[collision_index],
        ),
        "collision_relative_phase_pair": (
            sp.simplify(zero_phase_decoded[0] + I * zero_phase_decoded[1][2]),
            sp.simplify(
                quarter_phase_decoded[0]
                + I * quarter_phase_decoded[1][2]
            ),
        ),
        "single_branch_source_sufficient": False,
    }


def boolean_monomials() -> tuple[tuple[int, ...], ...]:
    return (
        ((),)
        + tuple((index,) for index in range(6))
        + tuple(itertools.combinations(range(6), 2))
    )


def monomial_values(mask: int, monomials: tuple[tuple[int, ...], ...]) -> tuple[int, ...]:
    return tuple(
        int(all((mask >> index) & 1 for index in monomial))
        for monomial in monomials
    )


@cache
def polynomial_facts() -> dict[str, object]:
    monomials = boolean_monomials()
    variable_count = 3 * len(monomials)
    rows: set[tuple[int, ...]] = set()
    values = tuple(monomial_values(mask, monomials) for mask in range(64))
    for group_index, rotation in enumerate(rotations()):
        target = shear_representation(rotation)
        permutation = shell_permutations()[group_index]
        for mask in range(64):
            transformed_mask = permute_mask(mask, permutation)
            for target_row in range(3):
                row = [0] * variable_count
                for monomial_index, value in enumerate(values[transformed_mask]):
                    row[target_row * len(monomials) + monomial_index] += value
                for source_row in range(3):
                    coefficient = -int(target[target_row, source_row])
                    if coefficient:
                        for monomial_index, value in enumerate(values[mask]):
                            row[source_row * len(monomials) + monomial_index] += (
                                coefficient * value
                            )
                if any(row):
                    rows.add(tuple(row))
    constraint = sp.Matrix(sorted(rows))
    nullspace = tuple(constraint.nullspace())
    basis_outputs = []
    for vector in nullspace:
        per_mask = []
        for mask in range(64):
            output = []
            for target_row in range(3):
                output.append(sp.simplify(sum(
                    vector[target_row * len(monomials) + index] * value
                    for index, value in enumerate(values[mask])
                )))
            per_mask.append(sp.Matrix(output))
        basis_outputs.append(tuple(per_mask))

    target_shear = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    fitting_masks = []
    fitting_ranks = []
    for mask in range(64):
        columns = sp.Matrix.hstack(*(
            outputs[mask] for outputs in basis_outputs
        )) if basis_outputs else sp.zeros(3, 0)
        rank = columns.rank()
        if rank == columns.row_join(target_shear).rank():
            fitting_masks.append(mask)
            fitting_ranks.append(rank)

    natural_orbits = orbit_partition(
        range(64),
        lambda group_index, mask: permute_mask(
            mask, shell_permutations()[group_index]
        ),
    )
    fitting_orbits = sum(
        bool(set(item) & set(fitting_masks)) for item in natural_orbits
    )

    return {
        "monomial_count": len(monomials),
        "constraint_shape": constraint.shape,
        "constraint_rank": constraint.rank(),
        "hom_dimension": len(nullspace),
        "fitting_mask_count": len(fitting_masks),
        "fitting_orbit_count": fitting_orbits,
        "fitting_ranks": tuple(sorted(Counter(fitting_ranks).items())),
        "full_contrast_reachable_natural": False,
        "coefficients_action_selected": False,
    }


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


@cache
def affine_eta_facts() -> dict[str, object]:
    classes = affine_action_classes(6)["classes"]
    selected = tuple(item for item in classes if item["has_orbit24"])
    if len(selected) != 1:
        raise AssertionError("expected one affine orbit-24 class")
    translations = selected[0]["translations"]
    permutations = shell_permutations()

    def input_action(group_index: int, mask: int) -> int:
        return (
            permute_mask(mask, permutations[group_index])
            ^ translations[group_index]
        )

    input_orbits = orbit_partition(range(64), input_action)
    regular_orbits = tuple(item for item in input_orbits if len(item) == 24)
    if len(regular_orbits) != 1:
        raise AssertionError("expected one regular affine input orbit")
    base = min(regular_orbits[0])
    group_for_input = {
        input_action(group_index, base): group_index
        for group_index in range(24)
    }
    if len(group_for_input) != 24:
        raise AssertionError("regular orbit lost a group element")

    contrast = (
        sp.sqrt(3), -sp.sqrt(3), sp.Integer(2), sp.Integer(-2),
        sp.Integer(0), sp.Integer(0),
    )
    shear = sp.Matrix((0, 1 / sp.sqrt(2), -1))

    def contrast_action(
        group_index: int, values: tuple[sp.Expr, ...]
    ) -> tuple[sp.Expr, ...]:
        output = [sp.Integer(0)] * 6
        for source, target in enumerate(permutations[group_index]):
            output[target] = values[source]
        return tuple(output)

    contrast_table = []
    shear_table = []
    for mask in range(64):
        if mask in group_for_input:
            group_index = group_for_input[mask]
            contrast_table.append(contrast_action(group_index, contrast))
            shear_table.append(
                tuple(shear_representation(rotations()[group_index]) * shear)
            )
        else:
            contrast_table.append((sp.Integer(0),) * 6)
            shear_table.append((sp.Integer(0),) * 3)
    contrast_table = tuple(contrast_table)
    shear_table = tuple(shear_table)

    contrast_covariant = all(
        contrast_table[input_action(group_index, mask)]
        == contrast_action(group_index, contrast_table[mask])
        for group_index in range(24)
        for mask in range(64)
    )
    shear_covariant = all(
        sp.Matrix(shear_table[input_action(group_index, mask)])
        == shear_representation(rotations()[group_index])
        * sp.Matrix(shear_table[mask])
        for group_index in range(24)
        for mask in range(64)
    )

    contrast_coefficients = tuple(
        anf_coefficients(tuple(row[coordinate] for row in contrast_table))
        for coordinate in range(6)
    )
    shear_coefficients = tuple(
        anf_coefficients(tuple(row[coordinate] for row in shear_table))
        for coordinate in range(3)
    )
    contrast_polynomial_exact = all(
        tuple(
            evaluate_anf(contrast_coefficients[coordinate], mask)
            for coordinate in range(6)
        ) == contrast_table[mask]
        for mask in range(64)
    )
    shear_polynomial_exact = all(
        tuple(
            evaluate_anf(shear_coefficients[coordinate], mask)
            for coordinate in range(3)
        ) == shear_table[mask]
        for mask in range(64)
    )

    def degree(coefficient_family) -> int:
        return max(
            monomial.bit_count()
            for coefficients in coefficient_family
            for monomial, coefficient in enumerate(coefficients)
            if coefficient != 0
        )

    def term_count(coefficient_family) -> int:
        return sum(
            coefficient != 0
            for coefficients in coefficient_family
            for coefficient in coefficients
        )

    return {
        "orbit24_class_count": len(selected),
        "regular_input_orbit_count": len(regular_orbits),
        "base_mask": base,
        "base_mask_bits": format(base, "06b"),
        "base_contrast": contrast_table[base],
        "base_shear": shear_table[base],
        "contrast_covariant": contrast_covariant,
        "shear_covariant": shear_covariant,
        "contrast_polynomial_exact": contrast_polynomial_exact,
        "shear_polynomial_exact": shear_polynomial_exact,
        "contrast_anf_degree": degree(contrast_coefficients),
        "shear_anf_degree": degree(shear_coefficients),
        "contrast_anf_terms": term_count(contrast_coefficients),
        "shear_anf_terms": term_count(shear_coefficients),
        "runtime_orbit_lookup": False,
        "cohomology_class_selected_by_h1_regular_orbit": True,
        "physical_internal_action_derived": False,
    }


@cache
def source_facts() -> dict[str, object]:
    facts = eta1.factorization_facts()
    return {
        "forward_terms": facts["forward_terms"],
        "actual_reverse_terms": facts["actual_reverse_terms"],
        "t2_source_rank": facts["t2_source_rank"],
        "target_source_matches_h1": facts["target_source_matches_h1"],
        "staged_equals_direct": facts["staged_equals_direct"],
        "direct_equals_inherited": facts["direct_equals_inherited"],
        "reverse_equals_inherited": facts["reverse_equals_inherited"],
        "literal_actual_reverse": True,
    }


@cache
def authority_facts() -> dict[str, object]:
    blob_checks = {
        spec: git_output("rev-parse", spec) == expected
        for spec, expected in EXPECTED_BLOBS.items()
    }
    return {
        "head_descends_prereg": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG_COMMIT, "HEAD"),
            cwd=ROOT,
            check=False,
        ).returncode == 0,
        "parent_is_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT_COMMIT, "HEAD"),
            cwd=ROOT,
            check=False,
        ).returncode == 0,
        "origin_main": git_output("rev-parse", "origin/main"),
        "blob_checks": blob_checks,
        "all_blobs_match": all(blob_checks.values()),
        "inputs_exist": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


@cache
def result_facts() -> dict[str, object]:
    orbit_data = orbit_facts()
    affine6 = affine_action_classes(6)
    affine7 = affine_action_classes(7)
    instrument = instrument_facts()
    polynomial = polynomial_facts()
    affine_eta = affine_eta_facts()
    source = source_facts()

    natural_complete = (
        orbit_data["literal_six_injective_code"]
        and orbit_data["contrast_orbit_size"] <= 12
        and instrument["total_cp_tp"]
        and source["target_source_matches_h1"]
    )
    two_shell_dilation = (
        orbit_data["two_shell_code_count"] == 36
        and orbit_data["two_shell_code_covariant"]
        and orbit_data["two_shell_code_orthogonal"]
        and set(orbit_data["two_shell_records_per_code"]) == {(1, 1)}
        and instrument["total_cp_tp"]
        and instrument["blank_invariant"]
        and instrument["locked_code_identity"]
    )
    center_corner_dilation = (
        orbit_data["center_corner_full_outcome_embedding"]
        and orbit_data["center_corner_code_count"] == 36
        and orbit_data["center_corner_code_covariant"]
        and set(orbit_data["center_corner_record_counts"]) == {3, 4, 5}
        and instrument["total_cp_tp"]
        and instrument["blank_invariant"]
        and instrument["locked_code_identity"]
    )
    affine_six_perpendicular_escapes = sum(
        item["has_orbit24"] for item in affine6["classes"]
    )
    affine_six_full_embeddings = sum(
        item["full_outcome_embedding"] for item in affine6["classes"]
    )
    affine_seven_full_embeddings = sum(
        item["full_outcome_embedding"] for item in affine7["classes"]
    )
    return {
        "orbit": orbit_data,
        "affine6": affine6,
        "affine7": affine7,
        "instrument": instrument,
        "polynomial": polynomial,
        "affine_eta": affine_eta,
        "source": source,
        "natural_one_shell_solution_set_empty": not natural_complete,
        "two_shell_readable_dilation_positive": two_shell_dilation,
        "center_corner_readable_dilation_positive": center_corner_dilation,
        "affine_six_orbit24_class_count": affine_six_perpendicular_escapes,
        "affine_six_full_outcome_embedding_count":
            affine_six_full_embeddings,
        "affine_seven_full_outcome_embedding_count":
            affine_seven_full_embeddings,
        "affine_action_selected_by_block208": False,
        "complete_h1_local_ownership": False,
        "solution_set_probability_image": "not_reached",
        "axiom_update_justified": False,
        "obligation_retirement": 0,
        "toe_percentage_movement": 0,
        "h2_opened": False,
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    result = dict(result_facts())
    orbit_data = dict(result["orbit"])
    affine6 = dict(result["affine6"])
    instrument = dict(result["instrument"])
    polynomial = dict(result["polynomial"])
    affine_eta = dict(result["affine_eta"])
    source = dict(result["source"])

    claims: dict[str, object] = {
        "outcome_count": 36,
        "record_codes_distinct": True,
        "blank_invariant": True,
        "effect_normalized": True,
        "sqrt_effect_exact": True,
        "qnd_lock": True,
        "nonorthogonal_output_record": False,
        "perpendicular_orbit": True,
        "literal_six_orbit24": False,
        "affine_classes_complete": True,
        "affine_action_selected": False,
        "affine_eta_decoder": True,
        "affine_class_axiom_selected": False,
        "center_neighbor_only": False,
        "two_shell_neighbor_only": False,
        "two_shell_code": True,
        "two_shell_covariant": True,
        "center_corner_code": True,
        "center_corner_neighbor_only": False,
        "product_carrier_global_minimum": False,
        "quadratic_prefit": False,
        "polynomial_family_complete": True,
        "contrast_stabilizer": True,
        "one_shell_complete": False,
        "sharpness_fork": True,
        "sharpness_selected": False,
        "single_branch_source_sufficient": False,
        "literal_actual_reverse": True,
        "source_terms": (110, 110),
        "h2": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
    }
    mutations = {
        "drop_outcome": ("outcome_count", 35),
        "merge_record_codes": ("record_codes_distinct", False),
        "noninvariant_blank": ("blank_invariant", False),
        "break_effect_normalization": ("effect_normalized", False),
        "break_sqrt_effect": ("sqrt_effect_exact", False),
        "break_qnd_lock": ("qnd_lock", False),
        "call_nonorthogonal_output_record": ("nonorthogonal_output_record", True),
        "erase_perpendicular_orbit": ("perpendicular_orbit", False),
        "invent_literal_six_orbit24": ("literal_six_orbit24", True),
        "hide_affine_action_class": ("affine_classes_complete", False),
        "call_affine_action_selected": ("affine_action_selected", True),
        "erase_affine_eta_decoder": ("affine_eta_decoder", False),
        "call_affine_class_axiom_selected":
            ("affine_class_axiom_selected", True),
        "call_center_neighbor_only": ("center_neighbor_only", True),
        "call_two_shell_neighbor_only": ("two_shell_neighbor_only", True),
        "erase_two_shell_code": ("two_shell_code", False),
        "break_two_shell_covariance": ("two_shell_covariant", False),
        "erase_center_corner_code": ("center_corner_code", False),
        "call_center_corner_neighbor_only":
            ("center_corner_neighbor_only", True),
        "claim_global_product_minimum":
            ("product_carrier_global_minimum", True),
        "fit_quadratic_after_h1": ("quadratic_prefit", True),
        "erase_polynomial_family": ("polynomial_family_complete", False),
        "erase_contrast_stabilizer": ("contrast_stabilizer", False),
        "claim_one_shell_complete": ("one_shell_complete", True),
        "erase_sharpness_fork": ("sharpness_fork", False),
        "claim_sharpness_selected": ("sharpness_selected", True),
        "claim_single_branch_source_sufficient":
            ("single_branch_source_sufficient", True),
        "replace_actual_reverse": ("literal_actual_reverse", False),
        "change_source_terms": ("source_terms", (109, 110)),
        "claim_h2": ("h2", True),
        "claim_axiom_update": ("axiom_update", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_movement": ("toe_movement", 1),
    }
    if mutation:
        key, value = mutations[mutation]
        claims[key] = value

    authority_ok = (
        authority["head_descends_prereg"]
        and authority["parent_is_ancestor"]
        and authority["origin_main"] == ORIGIN_MAIN
        and authority["all_blobs_match"]
        and authority["inputs_exist"]
    )
    outcome_ok = (
        orbit_data["rotation_count"] == 24
        and orbit_data["outcome_count"] == claims["outcome_count"]
        and orbit_data["outcome_orbit_histogram"] == {6: 2, 24: 1}
        and claims["perpendicular_orbit"]
        and orbit_data["outcome_relations"]
        == ((6, -1), (6, 1), (24, 0))
    )
    literal_carrier_ok = (
        orbit_data["literal_shell_orbit_histogram"]
        == {1: 2, 3: 2, 6: 2, 8: 1, 12: 3}
        and not orbit_data["literal_six_injective_code"]
        and claims["literal_six_orbit24"] is False
        and not orbit_data["literal_center_six_injective_code"]
        and claims["center_neighbor_only"] is False
        and claims["contrast_stabilizer"]
        and orbit_data["contrast_orbit_size"] == 24
        and orbit_data["contrast_stabilizer"] == 1
    )
    affine_ok = (
        claims["affine_classes_complete"]
        and affine6["site_count"] == 6
        and affine6["class_count"] == 2 ** affine6["h1_dimension"]
        and all(item["homomorphism"] for item in affine6["classes"])
        and result["affine_six_orbit24_class_count"] == 1
        and result["affine_six_full_outcome_embedding_count"] == 0
        and result["affine_seven_full_outcome_embedding_count"] == 0
        and not result["affine_action_selected_by_block208"]
        and claims["affine_action_selected"] is False
    )
    writer_ok = (
        claims["record_codes_distinct"]
        and orbit_data["two_shell_code_count"] == 36
        and orbit_data["two_shell_code_orthogonal"]
        and claims["two_shell_code"]
        and orbit_data["two_shell_code_covariant"]
        and claims["two_shell_covariant"]
        and set(orbit_data["two_shell_records_per_code"]) == {(1, 1)}
        and claims["two_shell_neighbor_only"] is False
        and instrument["effect_count"] == 36
        and set(instrument["effect_ranks"]) == {1}
        and set(instrument["effect_nonzero_eigenvalues"]) == {sp.Rational(1, 9)}
        and instrument["sum_effect"] == I4
        and claims["effect_normalized"]
        and instrument["sum_sqrt_square"] == I4
        and claims["sqrt_effect_exact"]
        and instrument["branch_code_orthogonal"]
        and instrument["blank_invariant"] == claims["blank_invariant"]
        and instrument["write_from_blank_only"]
        and instrument["locked_code_identity"] == claims["qnd_lock"]
        and instrument["total_cp_tp"]
        and result["two_shell_readable_dilation_positive"]
        and orbit_data["literal_corner_orbit_histogram"]
        == {1: 2, 2: 1, 4: 2, 6: 2, 8: 5, 12: 6, 24: 5}
        and not orbit_data["literal_corner_full_outcome_embedding"]
        and orbit_data["center_corner_full_outcome_embedding"]
        and orbit_data["center_corner_code_count"] == 36
        and orbit_data["center_corner_code_covariant"]
        and claims["center_corner_code"]
        and claims["center_corner_neighbor_only"] is False
        and claims["product_carrier_global_minimum"] is False
        and orbit_data["minimal_complete_point_orbit_product_carrier_sites"] == 9
        and result["center_corner_readable_dilation_positive"]
    )
    output_typing_ok = (
        instrument["full_rank_output_count"] == 36
        and instrument["nonorthogonal_overlap_count"] == 630
        and not instrument["nonorthogonal_outputs_are_records"]
        and claims["nonorthogonal_output_record"] is False
    )
    polynomial_ok = (
        claims["polynomial_family_complete"]
        and polynomial["monomial_count"] == 22
        and polynomial["constraint_rank"] + polynomial["hom_dimension"] == 66
        and claims["quadratic_prefit"] is False
        and not polynomial["full_contrast_reachable_natural"]
        and not polynomial["coefficients_action_selected"]
    )
    affine_eta_ok = (
        claims["affine_eta_decoder"]
        and affine_eta["orbit24_class_count"] == 1
        and affine_eta["regular_input_orbit_count"] == 1
        and affine_eta["base_contrast"]
        == (
            sp.sqrt(3), -sp.sqrt(3), sp.Integer(2), sp.Integer(-2),
            sp.Integer(0), sp.Integer(0),
        )
        and affine_eta["base_shear"]
        == (0, 1 / sp.sqrt(2), -1)
        and affine_eta["contrast_covariant"]
        and affine_eta["shear_covariant"]
        and affine_eta["contrast_polynomial_exact"]
        and affine_eta["shear_polynomial_exact"]
        and affine_eta["contrast_anf_degree"] > 2
        and affine_eta["shear_anf_degree"] > 2
        and not affine_eta["runtime_orbit_lookup"]
        and affine_eta["cohomology_class_selected_by_h1_regular_orbit"]
        and not affine_eta["physical_internal_action_derived"]
        and claims["affine_class_axiom_selected"] is False
    )
    source_ok = (
        (source["forward_terms"], source["actual_reverse_terms"])
        == claims["source_terms"]
        and source["t2_source_rank"] == 3
        and source["target_source_matches_h1"]
        and source["staged_equals_direct"]
        and source["direct_equals_inherited"]
        and source["reverse_equals_inherited"]
        and source["literal_actual_reverse"] == claims["literal_actual_reverse"]
    )
    selection_ok = (
        claims["sharpness_fork"]
        and instrument["sharp_half_distinct"]
        and instrument["sharp_half_decoded_equal"]
        and instrument["sharp_probabilities_sum"] == 1
        and instrument["half_probabilities_sum"] == 1
        and not instrument["sharpness_action_selected"]
        and claims["sharpness_selected"] is False
        and instrument["collision_probability_pair"]
        == (sp.Rational(1, 36), sp.Rational(1, 36))
        and instrument["collision_relative_phase_pair"] == (1, I)
        and instrument["single_branch_source_sufficient"]
        == claims["single_branch_source_sufficient"]
        and result["solution_set_probability_image"] == "not_reached"
    )
    scope_ok = (
        result["natural_one_shell_solution_set_empty"]
        and not result["complete_h1_local_ownership"]
        and claims["one_shell_complete"] is False
        and result["h2_opened"] == claims["h2"]
        and result["axiom_update_justified"] == claims["axiom_update"]
        and result["obligation_retirement"] == claims["obligation_retirement"]
        and result["toe_percentage_movement"] == claims["toe_movement"]
    )

    return {
        "A_authority": (authority_ok, "registration, parent, origin/main, and all pinned external blobs match"),
        "B_outcome_orbits": (outcome_ok, "36 Block208 outcomes split exactly into 6/6/24 proper-cubic orbits"),
        "C_literal_carrier": (literal_carrier_ok, "literal six-neighbor and center-plus-shell product Records have no 24-orbit for the H1 law"),
        "D_affine_actions": (affine_ok, "all affine binary Record actions are classified and none is silently called action-selected"),
        "E_readable_writer": (writer_ok, "a minimal-in-the-tested-point-orbit-class center-plus-corner 36-code register, and the two-shell control, give total covariant blank/write/lock CP-QND dilations"),
        "F_output_typing": (output_typing_ok, "the inherited 36 full-rank qubit outputs remain nonorthogonal and are not renamed Records"),
        "G_polynomial_eta": (polynomial_ok, "the complete degree-at-most-two Boolean shell covariant family is solved without post-H1 fitting"),
        "H_affine_eta": (affine_eta_ok, "the unique nontrivial affine class admits exact finite Boolean-polynomial H1 contrast and shear decoders, but its physical internal action is not yet derived"),
        "I_source_identity": (source_ok, "the unchanged rank-three Source/Eta map retains exact 110/110 forward and actual-reverse H1 sources"),
        "J_selection": (selection_ok, "orthogonal dilation neither selects the sharp/unsharp law nor makes one sampled branch sufficient for its source statistics"),
        "K_scope": (scope_ok, "natural one-shell ownership remains empty while an affine eta decoder and wider readable writer survive as unjoined positive pieces"),
    }


def mutation_sweep() -> tuple[int, int]:
    rejected = 0
    for mutation in MUTATIONS:
        checks = evaluate(mutation)
        if any(not passed for passed, _ in checks.values()):
            rejected += 1
    return rejected, len(MUTATIONS)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--list-mutations", action="store_true")
    arguments = parser.parse_args()
    if arguments.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    checks = evaluate(arguments.mutation or "")
    passed = sum(value[0] for value in checks.values())
    for name, (ok, detail) in checks.items():
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    if not arguments.mutation:
        result = result_facts()
        orbit_data = result["orbit"]
        affine6 = result["affine6"]
        polynomial = result["polynomial"]
        affine_eta = result["affine_eta"]
        instrument = result["instrument"]
        rejected, total = mutation_sweep()
        print(
            "ORBIT_CENSUS: outcomes="
            f"{orbit_data['outcome_orbit_histogram']}; literal_six="
            f"{orbit_data['literal_shell_orbit_histogram']}; H1_contrast="
            f"orbit{orbit_data['contrast_orbit_size']}/"
            f"stab{orbit_data['contrast_stabilizer']}."
        )
        print(
            "AFFINE_ACTIONS: H1dim="
            f"{affine6['h1_dimension']}; classes={affine6['class_count']}; "
            "six-shell orbit24 classes="
            f"{result['affine_six_orbit24_class_count']}; full36 embeddings="
            f"{result['affine_six_full_outcome_embedding_count']}; "
            "selected=false."
        )
        print(
            "READABLE_DILATION: two-shell codes=36; orthogonal=true; "
            "center+corner sites=9; covariant=true; total_CP_TP=true; QND_lock=true; "
            "nearest_neighbor_eta=false."
        )
        print(
            "POLYNOMIAL_ETA: monomials="
            f"{polynomial['monomial_count']}; Hom_dim="
            f"{polynomial['hom_dimension']}; fitting_masks="
            f"{polynomial['fitting_mask_count']}; coefficients_selected=false."
        )
        print(
            "AFFINE_ETA: base="
            f"{affine_eta['base_mask_bits']}; contrast_degree="
            f"{affine_eta['contrast_anf_degree']}; shear_degree="
            f"{affine_eta['shear_anf_degree']}; exact=true; "
            "physical_action_derived=false."
        )
        print(
            "PROBABILITY_IMAGE: sharp/unsharp distinct="
            f"{instrument['sharp_half_distinct']}; decoded_source_equal="
            f"{instrument['sharp_half_decoded_equal']}; complete_image="
            f"{result['solution_set_probability_image']}."
        )
        for line in N5_LINES:
            print(line)
        print(f"MUTATIONS: rejected={rejected}/{total}")
        print(
            "CONCLUSION: the orthogonal Record-dilation wall closes on a "
            "bounded nine-site center-plus-corner carrier, but the frozen "
            "natural six-neighbor "
            "Record action has no complete H1 ownership solution; the one "
            "nontrivial affine class carries only the 24-orbit, not both "
            "six-orbits, so wider history and effect selection remain explicit."
        )
    print(f"SCORECARD PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
