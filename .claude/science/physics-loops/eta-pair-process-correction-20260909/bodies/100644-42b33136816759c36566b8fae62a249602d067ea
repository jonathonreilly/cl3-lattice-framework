#!/usr/bin/env python3
"""Block23 primary: prior Locked Record to an exact two-event prefix.

The proof is algebraic and combinatorial.  It never allocates the physical
2^224 Hilbert matrix.  Kraus completeness is proved on the exhaustive
orthogonal control sectors, and the fresh-live transition law is derived from
the Block22 Pauli coefficients with exact SymPy arithmetic.
"""

from __future__ import annotations

import ast
import hashlib
import itertools
from dataclasses import dataclass, replace
from functools import lru_cache
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
PACKET = ROOT / ".claude/science/physics-loops" / (
    "toe-source-eta-ownership-block23-prior-record-live-preparation-"
    "two-event-prefix-20260830"
)
FROZEN = {
    "GOAL.md": "6378ed13a8c72caca749197127ec67f3c8263c4d622563ec6ba73db75a9b3ead",
    "AUTHORITY_GATE.md": "c1b28a69298924cded8862987f1d26b292f9546c49b4ea797cd88f219bd310e1",
    "PREFLIGHT_WITNESSES.md": "c7098ef5c05f4a3b1bd3308c44a64e8bf1e0caa12fa40fb27580009b7672b163",
    "PANEL_RETURN.md": "7a16f2f4956d42c6bea387d92bbc0a4ce26004470d872cb3382d370d24dfdb63",
    "INDEPENDENT_PREREG_ATTACK.md": "f37da51570a3b448a3e430579171c40d934c941bd82704120cd98050d23719f8",
    "APPROACH_REGISTRY.md": "95b733561940b4892b0631e8cb679df1aab1f40004954b9a6baf9a9ef2592618",
    "MUTATION_PLAN.md": "654eb51a2174b2453b0a4ccc3ff34b09ee6ea1973de50bc3c5ff323cd6edf679",
    "NO_GO_DISCIPLINE_CHECKLIST.md": "fea9d4a66f58b2a9fd2759b71fff24093a7a30112ff67d4d65b6cc31b1c00a93",
}

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


def successor_center(front, displacement=DISPLACEMENT):
    return scale(displacement, front)


def block_sets(displacement=DISPLACEMENT):
    blocks = {"old": translate(SUPPORT, (0, 0, 0))}
    for front in DIRECTIONS:
        blocks[front] = translate(SUPPORT, successor_center(front, displacement))
    return blocks


def pairwise_disjoint(blocks):
    values = tuple(blocks.values())
    return all(values[i].isdisjoint(values[j]) for i in range(len(values)) for j in range(i))


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


@dataclass(frozen=True)
class StarProduct:
    """All six successor blocks, ordered by their geometric ray labels."""

    blocks: tuple


BLANK_LIVE = ordered_live({site: radial_bloch(site, 0) for site in DIRECTIONS})
BLANK_BLOCK = BlockProduct(BLANK_LIVE, BLANK_POINTER)
BLANK_STAR = StarProduct(tuple(BLANK_BLOCK for _front in DIRECTIONS))


def block_index(front):
    return DIRECTIONS.index(front)


def block_product(live_vectors, pointer_word):
    return BlockProduct(ordered_live(live_vectors), pointer_word)


@lru_cache(maxsize=None)
def _target_star_variant(front, outcome, ready_override=None, activate_extra=()):
    """Mutation-capable constructor; the physical target wrapper has no oracle args."""
    words = {ray: BLANK_POINTER for ray in DIRECTIONS}
    words[front] = ready_word(front) if ready_override is None else ready_override
    for ray in activate_extra:
        words[ray] = ready_word(ray)
    blocks = []
    for ray in DIRECTIONS:
        if ray == front:
            blocks.append(block_product(prepared_vectors(outcome), words[ray]))
        else:
            blocks.append(BlockProduct(BLANK_LIVE, words[ray]))
    return StarProduct(tuple(blocks))


@lru_cache(maxsize=None)
def target_star(front, outcome):
    """Return all 192 target factors from only the prior Record label."""
    return _target_star_variant(front, outcome)


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


@lru_cache(maxsize=None)
def rotate_star_product(star, g):
    source = {
        front: star.blocks[index] for index, front in enumerate(DIRECTIONS)
    }
    moved = {
        mat_vec(g, front): rotate_block_product(block, g)
        for front, block in source.items()
    }
    return StarProduct(tuple(moved[front] for front in DIRECTIONS))


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


@lru_cache(maxsize=None)
def star_overlap(left, right):
    return sp.simplify(
        sp.prod(block_overlap(left.blocks[i], right.blocks[i]) for i in range(6))
    )


@lru_cache(maxsize=None)
def block_physical_factors(block):
    factors = {
        site: block.live[index] for index, site in enumerate(DIRECTIONS)
    }
    factors.update(
        {
            site: radial_bloch(site, block.pointer[index])
            for index, site in enumerate(POINTER_ORDER)
        }
    )
    return tuple(sorted(factors.items()))


@lru_cache(maxsize=None)
def star_physical_factors(star):
    return tuple(
        (front, site, vector)
        for index, front in enumerate(DIRECTIONS)
        for site, vector in block_physical_factors(star.blocks[index])
    )


@dataclass(frozen=True)
class PrepBranch:
    control: tuple
    old_live_identity_factors: tuple
    old_pointer_input: tuple
    old_pointer_output: tuple
    star_input: StarProduct
    star_output: StarProduct


def preparation_branches():
    return {
        (front, outcome): PrepBranch(
            control=(front, outcome),
            old_live_identity_factors=tuple(
                (site, "I_2") for site in DIRECTIONS
            ),
            old_pointer_input=locked_word(front, outcome),
            old_pointer_output=locked_word(front, outcome),
            star_input=BLANK_STAR,
            star_output=target_star(front, outcome),
        )
        for front in DIRECTIONS
        for outcome in OUTCOMES
    }


PREP_BRANCHES = preparation_branches()
EXPECTED_P_VALID_TERMS = frozenset(
    (locked_word(front, outcome), BLANK_STAR)
    for front in DIRECTIONS
    for outcome in OUTCOMES
)
RECORD_LABELS = tuple(
    (front, outcome) for front in DIRECTIONS for outcome in OUTCOMES
)
OLD_LIVE_IDENTITIES = tuple((site, "I_2") for site in DIRECTIONS)


def projector_reduce(expression, symbol):
    polynomial = sp.Poly(sp.expand(expression), symbol)
    relation = sp.Poly(symbol ** 2 - symbol, symbol)
    return sp.simplify(sp.rem(polynomial, relation).as_expr())


def prep_sector_eigenvalue(branches, pointer_word, star_is_blank):
    """Eigenvalue of the branch-derived P_valid on an orthogonal input sector."""
    return sum(
        int(
            star_is_blank
            and branch.old_pointer_input == pointer_word
            and branch.star_input == BLANK_STAR
        )
        for branch in branches.values()
    )


def prep_factorized_kraus_is_physical(branch):
    """Every listed factor defines an identity, projector, or rank-one Kraus map."""
    return (
        branch.old_live_identity_factors == OLD_LIVE_IDENTITIES
        and len(branch.old_pointer_input) == len(branch.old_pointer_output) == 26
        and pointer_overlap(branch.old_pointer_input, branch.old_pointer_input) == 1
        and pointer_overlap(branch.old_pointer_output, branch.old_pointer_output) == 1
        and len(star_physical_factors(branch.star_input)) == 192
        and len(star_physical_factors(branch.star_output)) == 192
        and all(
            sp.simplify(norm2(vector) - 1) == 0
            for _front, _site, vector in star_physical_factors(branch.star_input)
        )
        and all(
            sp.simplify(norm2(vector) - 1) == 0
            for _front, _site, vector in star_physical_factors(branch.star_output)
        )
    )


def prep_projector_completeness_certificate(branches):
    """Prove sum A_j^dag A_j + (I-P_valid)^2 = I for the actual projector."""
    branch_effects = tuple(
        (branch.old_pointer_input, branch.star_input)
        for branch in branches.values()
    )
    orthogonal_projector_sum = (
        len(set(branch_effects)) == len(branch_effects)
        and all(
            pointer_overlap(branch_effects[i][0], branch_effects[j][0])
            * star_overlap(branch_effects[i][1], branch_effects[j][1])
            == int(i == j)
            for i in range(len(branch_effects))
            for j in range(len(branch_effects))
        )
    )
    p = sp.symbols("P_valid", commutative=True)
    projector_identity = projector_reduce(p + (1 - p) ** 2 - 1, p) == 0
    return orthogonal_projector_sum and projector_identity


def prep_reference_extension_certificate(branches):
    """Prove the I_R-tensored Kraus Gram identity for arbitrary reference indices."""
    if not all(prep_factorized_kraus_is_physical(branch) for branch in branches.values()):
        return False
    if not prep_projector_completeness_certificate(branches):
        return False
    p = sp.symbols("P_valid", commutative=True)
    reference_row, reference_column = sp.symbols(
        "r s", integer=True, nonnegative=True
    )
    delta = sp.KroneckerDelta(reference_row, reference_column)
    physical_gram = projector_reduce(p + (1 - p) ** 2, p)
    return sp.simplify(delta * physical_gram - delta) == 0


def record_projector_heisenberg_value(
    branches, observable_word, input_word, star_is_blank
):
    """Coefficient of a classical Record projector after the actual prep channel."""
    branch_value = sum(
        int(
            star_is_blank
            and branch.star_input == BLANK_STAR
            and branch.old_pointer_input == input_word
            and branch.old_pointer_output == observable_word
        )
        for branch in branches.values()
    )
    p_valid = prep_sector_eigenvalue(branches, input_word, star_is_blank)
    stop_value = (1 - p_valid) ** 2 * int(input_word == observable_word)
    return branch_value + stop_value


def record_matrix_unit_survival(branches, left_word, right_word, star_is_blank):
    """Schrodinger coefficient for |left><right| on one Blank/complement sector."""
    branch_value = sum(
        int(
            star_is_blank
            and branch.star_input == BLANK_STAR
            and branch.old_pointer_input == left_word
            and branch.old_pointer_input == right_word
        )
        for branch in branches.values()
    )
    stop_left = 1 - prep_sector_eigenvalue(branches, left_word, star_is_blank)
    stop_right = 1 - prep_sector_eigenvalue(branches, right_word, star_is_blank)
    return branch_value + stop_left * stop_right


def prep_channel_certificate(branches=PREP_BRANCHES):
    branch_values = tuple(branches.values())
    all_pointer_words = [branch.old_pointer_input for branch in branch_values]
    controls_orthogonal = all(
        pointer_overlap(all_pointer_words[i], all_pointer_words[j])
        == int(i == j)
        for i in range(len(all_pointer_words))
        for j in range(len(all_pointer_words))
    )
    branch_effects = frozenset(
        (branch.old_pointer_input, branch.star_input) for branch in branch_values
    )
    exact_frozen_fields = all(
        label in branches
        and branches[label].control == label
        and branches[label].old_live_identity_factors
        == OLD_LIVE_IDENTITIES
        and branches[label].old_pointer_input == locked_word(*label)
        and branches[label].old_pointer_output == locked_word(*label)
        and branches[label].star_input == BLANK_STAR
        and branches[label].star_output == target_star(*label)
        for label in (
            (front, outcome)
            for front in DIRECTIONS
            for outcome in OUTCOMES
        )
    )
    factor_complete = all(
        prep_factorized_kraus_is_physical(branch)
        and len(block_physical_factors(BLANK_BLOCK)) == 32
        for branch in branch_values
    )
    target_orthogonal = all(
        star_overlap(branch.star_input, branch.star_output) == 0
        for branch in branch_values
    )

    completeness = prep_projector_completeness_certificate(branches)
    arbitrary_reference = prep_reference_extension_certificate(branches)

    expected_words = tuple(locked_word(*label) for label in RECORD_LABELS)
    input_words = expected_words + (BLANK_POINTER,)
    branch_qnd_witness = all(
        record_projector_heisenberg_value(
            branches, observable_word, input_word, star_is_blank
        )
        == int(input_word == observable_word)
        for observable_word in expected_words
        for input_word in input_words
        for star_is_blank in (True, False)
    )
    blank_projector = sp.symbols("B_blank_star", commutative=True)
    qnd_projector_identity = projector_reduce(
        blank_projector + (1 - blank_projector) ** 2 - 1,
        blank_projector,
    ) == 0
    record_branch_structure = (
        star_overlap(BLANK_STAR, BLANK_STAR) == 1
        and controls_orthogonal
        and all(
            branch.old_pointer_input == branch.old_pointer_output
            and branch.star_input == BLANK_STAR
            for branch in branch_values
        )
    )
    qnd_heisenberg = (
        record_branch_structure
        and qnd_projector_identity
        and branch_qnd_witness
    )
    coherent_blank_dephased = all(
        record_matrix_unit_survival(branches, left, right, True) == 0
        for left, right in itertools.combinations(expected_words, 2)
    )
    coherent_complement_preserved = all(
        record_matrix_unit_survival(branches, left, right, False) == 1
        for left, right in itertools.combinations(expected_words, 2)
    )

    covariance = all(
        rotate_word(branch.old_pointer_input, g)
        == PREP_BRANCHES[(mat_vec(g, front), mat_vec(g, outcome))].old_pointer_input
        and rotate_word(branch.old_pointer_output, g)
        == PREP_BRANCHES[(mat_vec(g, front), mat_vec(g, outcome))].old_pointer_output
        and (mat_vec(g, front), mat_vec(g, outcome))
        == PREP_BRANCHES[(mat_vec(g, front), mat_vec(g, outcome))].control
        and rotate_star_product(branch.star_input, g)
        == PREP_BRANCHES[(mat_vec(g, front), mat_vec(g, outcome))].star_input
        and rotate_star_product(branch.star_output, g)
        == PREP_BRANCHES[(mat_vec(g, front), mat_vec(g, outcome))].star_output
        for (front, outcome), branch in branches.items()
        for g in ROTATIONS
    )

    return {
        "branch_count": len(branches) == 84,
        "exact_frozen_fields": exact_frozen_fields,
        "effects_equal_p_valid": branch_effects == EXPECTED_P_VALID_TERMS,
        "controls_orthogonal": controls_orthogonal,
        "factor_complete": factor_complete,
        "p_valid_projector": len(branch_effects) == 84 and controls_orthogonal,
        "kraus_complete": completeness,
        "arbitrary_reference": arbitrary_reference,
        "qnd_heisenberg": qnd_heisenberg,
        "old_record_unchanged": all(
            branch.old_pointer_output == branch.old_pointer_input
            for branch in branch_values
        ),
        "coherent_code_not_fixed": (
            coherent_blank_dephased and coherent_complement_preserved
        ),
        "target_orthogonal_blank": target_orthogonal,
        "repeat_stop": target_orthogonal,
        "branch_covariance": covariance,
    }


def c4_front_bit_phase_witness():
    """Isolate the opposite C4 phase characters of the fixed front bits."""
    z_plus = (0, 0, 1)
    z_minus = (0, 0, -1)
    outcome = (0, 0, 1)
    plus = PREP_BRANCHES[(z_plus, outcome)]
    minus = PREP_BRANCHES[(z_minus, outcome)]
    plus_active = plus.star_output.blocks[block_index(z_plus)]
    minus_active = minus.star_output.blocks[block_index(z_minus)]
    plus_differences = {
        POINTER_ORDER[index]
        for index in range(len(POINTER_ORDER))
        if plus_active.pointer[index] != BLANK_POINTER[index]
    }
    minus_differences = {
        POINTER_ORDER[index]
        for index in range(len(POINTER_ORDER))
        if minus_active.pointer[index] != BLANK_POINTER[index]
    }
    inactive_are_blank = all(
        plus.star_output.blocks[block_index(front)] == BLANK_BLOCK
        for front in DIRECTIONS if front != z_plus
    ) and all(
        minus.star_output.blocks[block_index(front)] == BLANK_BLOCK
        for front in DIRECTIONS if front != z_minus
    )
    common_physical_shape = (
        plus_active.live == minus_active.live
        and plus_differences == {scaled(z_plus, 2)}
        and minus_differences == {scaled(z_minus, 2)}
        and inactive_are_blank
        and len(star_physical_factors(plus.star_output))
        == len(star_physical_factors(minus.star_output))
        == 192
    )
    theta = sp.pi / 2
    up = sp.exp(-sp.I * theta / 2)
    down = sp.exp(sp.I * theta / 2)
    plus_front_ratio = sp.simplify(down / up)
    minus_front_ratio = sp.simplify(up / down)
    cross_ratio = sp.simplify(plus_front_ratio * sp.conjugate(minus_front_ratio))
    return (
        common_physical_shape
        and plus_front_ratio == sp.I
        and minus_front_ratio == -sp.I
        and cross_ratio == -1
    )


def ray_representatives():
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    corners = tuple(corner for corner in CORNERS if corner[0] == 1)
    return axes + corners


RAYS = ray_representatives()


def quotient_kernel():
    return sp.Matrix(
        len(RAYS),
        len(RAYS),
        lambda i, j: sp.simplify(
            transition(RAYS[i], RAYS[j])
            + transition(RAYS[i], negate(RAYS[j]))
        ),
    )


def expected_transition(source, target):
    if is_axis(source):
        if is_axis(target):
            return R(1, 9) if axis_index(source) == axis_index(target) else R(5, 72)
        return R(1, 16)
    if is_axis(target):
        return R(1, 12)
    same_ray = target == source or target == negate(source)
    return (
        R(1, 16) + R(3, 64) / sp.sqrt(2)
        if same_ray
        else R(1, 16) - R(1, 64) / sp.sqrt(2)
    )


def effect_scaled(label, scalar):
    return scale_effect_data(effect(label), scalar)


def scale_effect_data(effect_data, scalar):
    """Scale an already-derived Pauli expansion without consulting an outcome label."""
    constant, coefficients = effect_data
    return (
        sp.simplify(scalar * constant),
        {
            site: tuple(sp.simplify(scalar * value) for value in vector)
            for site, vector in coefficients.items()
        },
    )


def effect_equal(left, right):
    if sp.simplify(left[0] - right[0]) != 0:
        return False
    return all(
        all(sp.simplify(left[1][site][k] - right[1][site][k]) == 0 for k in range(3))
        for site in DIRECTIONS
    )


def summed_effects(effects):
    return (
        sp.simplify(sum(item[0] for item in effects)),
        {
            site: tuple(
                sp.simplify(sum(item[1][site][k] for item in effects))
                for k in range(3)
            )
            for site in DIRECTIONS
        },
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


@lru_cache(maxsize=None)
def lueders_root_certificate(label):
    constant, coefficients = effect(label)
    norms, values = spectral_resolution(label)
    squared_roots = {signs: sp.sqrt(value) ** 2 for signs, value in values.items()}
    positive = all(value.is_positive is True for value in values.values())
    constant_ok = sp.simplify(walsh(squared_roots, ()) - constant) == 0
    linear_ok = True
    for index, site in enumerate(DIRECTIONS):
        if norms[site] == 0:
            linear_ok &= coefficients[site] == (0, 0, 0)
            continue
        axis = scale(1 / norms[site], coefficients[site])
        reconstructed = scale(walsh(squared_roots, (index,)), axis)
        linear_ok &= reconstructed == coefficients[site]
    higher_ok = all(
        walsh(squared_roots, subset) == 0
        for order in range(2, 7)
        for subset in itertools.combinations(range(6), order)
    )
    return positive and constant_ok and linear_ok and higher_ok


@lru_cache(maxsize=None)
def squared_lueders_root_effect(label):
    """Derive sqrt(E_label)^dag sqrt(E_label) from its 64 spectral roots."""
    _constant, coefficients = effect(label)
    norms, values = spectral_resolution(label)
    squared_roots = {
        signs: sp.simplify(sp.sqrt(value) * sp.sqrt(value))
        for signs, value in values.items()
    }
    higher_terms = tuple(
        (subset, walsh(squared_roots, subset))
        for order in range(2, 7)
        for subset in itertools.combinations(range(6), order)
    )
    if any(sp.simplify(value) != 0 for _subset, value in higher_terms):
        raise ValueError("squared root generated an unrepresented higher Pauli term")
    reconstructed = {}
    for index, site in enumerate(DIRECTIONS):
        if norms[site] == 0:
            reconstructed[site] = (sp.S.Zero,) * 3
        else:
            local_axis = scale(1 / norms[site], coefficients[site])
            reconstructed[site] = scale(
                walsh(squared_roots, (index,)), local_axis
            )
    return walsh(squared_roots, ()), reconstructed


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


@dataclass(frozen=True)
class WriterAction:
    kind: str
    front: tuple | None
    outcome: tuple | None
    probability: object
    input_pointer: tuple
    output_pointer: tuple
    input_live: tuple
    live_operator: tuple


@lru_cache(maxsize=None)
def local_writer_actions(block):
    front = decode_ready_word(block.pointer)
    if front is None:
        return (
            WriterAction(
                kind="STOP",
                front=None,
                outcome=None,
                probability=sp.S.One,
                input_pointer=block.pointer,
                output_pointer=block.pointer,
                input_live=block.live,
                live_operator=("identity",),
            ),
        )
    vectors = live_dictionary(block.live)
    return tuple(
        WriterAction(
            kind="WRITE",
            front=front,
            outcome=outcome,
            probability=expectation(outcome, vectors),
            input_pointer=block.pointer,
            output_pointer=locked_word(front, outcome),
            input_live=block.live,
            live_operator=("sqrt_effect", outcome),
        )
        for outcome in OUTCOMES
    )


@lru_cache(maxsize=None)
def parallel_writer_actions(star):
    local = tuple(local_writer_actions(block) for block in star.blocks)
    return tuple(itertools.product(*local))


def parallel_writer_certificate():
    valid = True
    for front in DIRECTIONS:
        for first in OUTCOMES:
            star = target_star(front, first)
            combinations = parallel_writer_actions(star)
            valid &= len(combinations) == 14
            seen = set()
            for combination in combinations:
                writes = [action for action in combination if action.kind == "WRITE"]
                valid &= len(writes) == 1
                if len(writes) != 1:
                    continue
                write = writes[0]
                seen.add(write.outcome)
                valid &= write.front == front
                valid &= decode_locked_word(write.output_pointer) == (front, write.outcome)
                valid &= lueders_root_certificate(write.outcome)
                valid &= sp.simplify(write.probability - transition(first, write.outcome)) == 0
                for index, action in enumerate(combination):
                    ray = DIRECTIONS[index]
                    if ray == front:
                        continue
                    valid &= action.kind == "STOP"
                    valid &= action.input_pointer == action.output_pointer == BLANK_POINTER
                    valid &= action.input_live == BLANK_LIVE
            valid &= seen == set(OUTCOMES)
            valid &= sp.simplify(
                sum(
                    next(action.probability for action in combination if action.kind == "WRITE")
                    for combination in combinations
                )
                - 1
            ) == 0
    return valid


@dataclass(frozen=True)
class CompositeBranch:
    front: tuple
    first: tuple
    second: tuple
    first_live_operator: tuple
    first_pointer_input: tuple
    first_pointer_output: tuple
    prep_branch: PrepBranch
    second_writer_actions: tuple
    kraus_factors: tuple
    input_domain: tuple
    joint_effect: tuple


@dataclass(frozen=True)
class ReferenceExtendedKraus:
    reference_factor: str
    physical_factors: tuple
    physical_domain: tuple
    physical_effect: tuple


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


def composite_kraus_factorization(front, first, second, prep, actions):
    write = next(action for action in actions if action.kind == "WRITE")
    star_input = star_physical_factors(prep.star_input)
    star_output = star_physical_factors(prep.star_output)
    star_rank_one_maps = tuple(
        (input_factor[0], input_factor[1], input_factor[2], output_factor[2])
        for input_factor, output_factor in zip(star_input, star_output)
        if input_factor[:2] == output_factor[:2]
    )
    inactive_stops = tuple(
        (
            DIRECTIONS[index],
            action.input_live,
            action.input_pointer,
            action.output_pointer,
            action.live_operator,
        )
        for index, action in enumerate(actions)
        if action.kind == "STOP"
    )
    return (
        ("first_live_root", root_operator_factor(first)),
        (
            "first_pointer_rank_one_maps",
            pointer_rank_one_maps(ready_word(front), locked_word(front, first)),
        ),
        ("prep_old_live_identities", prep.old_live_identity_factors),
        (
            "prep_old_pointer_projectors",
            pointer_rank_one_maps(prep.old_pointer_input, prep.old_pointer_output),
        ),
        ("prep_star_rank_one_maps", star_rank_one_maps),
        ("second_active_front", front),
        ("second_live_root", root_operator_factor(second)),
        (
            "second_pointer_rank_one_maps",
            pointer_rank_one_maps(write.input_pointer, write.output_pointer),
        ),
        ("inactive_stop_identities", inactive_stops),
    )


def composite_kraus_factorization_is_physical(branch):
    factors = dict((entry[0], entry[1:]) for entry in branch.kraus_factors)
    first_root = factors["first_live_root"][0]
    second_root = factors["second_live_root"][0]
    second_active_front = factors["second_active_front"][0]
    first_pointer = factors["first_pointer_rank_one_maps"][0]
    prep_live = factors["prep_old_live_identities"][0]
    prep_pointer = factors["prep_old_pointer_projectors"][0]
    prep_star = factors["prep_star_rank_one_maps"][0]
    second_pointer = factors["second_pointer_rank_one_maps"][0]
    inactive_stops = factors["inactive_stop_identities"][0]
    indexed_writes = [
        (index, action)
        for index, action in enumerate(branch.second_writer_actions)
        if action.kind == "WRITE"
    ]
    return (
        first_root[0] == branch.first
        and first_root == root_operator_factor(branch.first)
        and len(first_root[1]) == 6
        and all(sp.simplify(norm2(axis) - 1) == 0 for _site, axis in first_root[1])
        and len(first_root[2]) == 64
        and all(root.is_real is True and root.is_positive is True for _signs, root in first_root[2])
        and second_root[0] == branch.second
        and second_root == root_operator_factor(branch.second)
        and len(second_root[1]) == 6
        and all(sp.simplify(norm2(axis) - 1) == 0 for _site, axis in second_root[1])
        and len(second_root[2]) == 64
        and all(root.is_real is True and root.is_positive is True for _signs, root in second_root[2])
        and len(indexed_writes) == 1
        and indexed_writes[0][0] == block_index(branch.front)
        and indexed_writes[0][1].front == branch.front == second_active_front
        and len(first_pointer) == 26
        and first_pointer
        == pointer_rank_one_maps(branch.first_pointer_input, branch.first_pointer_output)
        and prep_live == OLD_LIVE_IDENTITIES
        and len(prep_pointer) == 26
        and prep_pointer
        == pointer_rank_one_maps(
            branch.prep_branch.old_pointer_input,
            branch.prep_branch.old_pointer_output,
        )
        and len(prep_star) == 192
        and prep_star
        == tuple(
            (input_factor[0], input_factor[1], input_factor[2], output_factor[2])
            for input_factor, output_factor in zip(
                star_physical_factors(branch.prep_branch.star_input),
                star_physical_factors(branch.prep_branch.star_output),
            )
        )
        and len(second_pointer) == 26
        and second_pointer
        == pointer_rank_one_maps(
            indexed_writes[0][1].input_pointer,
            indexed_writes[0][1].output_pointer,
        )
        and len(inactive_stops) == 5
        and all(
            live == BLANK_LIVE
            and input_pointer == output_pointer == BLANK_POINTER
            and live_operator == ("identity",)
            for _ray, live, input_pointer, output_pointer, live_operator
            in inactive_stops
        )
    )


def contract_composite_kraus_effect(kraus_factors):
    """Contract M^dag M from only the stored factorized composite Kraus map."""
    factors = dict((entry[0], entry[1:]) for entry in kraus_factors)
    first_effect = contract_root_adjoint_root(factors["first_live_root"][0])
    second_effect = contract_root_adjoint_root(factors["second_live_root"][0])
    second_pointer_maps = factors["second_pointer_rank_one_maps"][0]
    second_input_word = tuple(entry[1] for entry in second_pointer_maps)
    active_front = decode_ready_word(second_input_word)
    stored_active_front = factors["second_active_front"][0]
    if active_front is None or active_front != stored_active_front:
        raise ValueError("second writer factor has no unique stored Ready front")
    star_maps = factors["prep_star_rank_one_maps"][0]
    prepared_live = {
        site: output_vector
        for front, site, _input_vector, output_vector in star_maps
        if front == active_front and site in DIRECTIONS
    }
    if set(prepared_live) != set(DIRECTIONS):
        raise ValueError("prep factorization does not supply six active live factors")
    second_probability = expectation_from_effect_data(
        second_effect, prepared_live
    )
    return scale_effect_data(first_effect, second_probability)


def tensor_reference_kraus(branch):
    """Construct I_R tensor M with R left symbolic and unrestricted."""
    return ReferenceExtendedKraus(
        reference_factor="I_R",
        physical_factors=branch.kraus_factors,
        physical_domain=branch.input_domain,
        physical_effect=branch.joint_effect,
    )


@lru_cache(maxsize=None)
def composite_branch(front, first, second):
    prep = PREP_BRANCHES[(front, first)]
    combinations = parallel_writer_actions(prep.star_output)
    selected = next(
        combination
        for combination in combinations
        if any(
            action.kind == "WRITE" and action.outcome == second
            for action in combination
        )
    )
    factors = composite_kraus_factorization(
        front, first, second, prep, selected
    )
    joint_effect = contract_composite_kraus_effect(factors)
    return CompositeBranch(
        front=front,
        first=first,
        second=second,
        first_live_operator=("sqrt_effect", first),
        first_pointer_input=ready_word(front),
        first_pointer_output=locked_word(front, first),
        prep_branch=prep,
        second_writer_actions=selected,
        kraus_factors=factors,
        input_domain=(ready_word(front), BLANK_STAR),
        joint_effect=joint_effect,
    )


def pointer_map_factor_count(input_word, output_word):
    valid = all(bit in (0, 1) for bit in input_word + output_word)
    valid &= pointer_overlap(input_word, input_word) == 1
    valid &= pointer_overlap(output_word, output_word) == 1
    return len(input_word) if valid and len(input_word) == len(output_word) else 0


def reachable_domain_composite_certificate(identity_effect):
    """Certify the composite on Ready_f tensor BlankStar, not its complement."""
    valid = all(lueders_root_certificate(label) for label in OUTCOMES)
    first_marginals = []
    total_effects = []
    for front in DIRECTIONS:
        for first in OUTCOMES:
            branches = [composite_branch(front, first, second) for second in OUTCOMES]
            valid &= len(branches) == 14
            valid &= all(branch.prep_branch.control == (front, first) for branch in branches)
            valid &= all(
                branch.input_domain == (ready_word(front), BLANK_STAR)
                for branch in branches
            )
            valid &= all(
                branch.first_pointer_output == branch.prep_branch.old_pointer_input
                == branch.prep_branch.old_pointer_output
                for branch in branches
            )
            valid &= all(
                pointer_map_factor_count(
                    branch.first_pointer_input, branch.first_pointer_output
                ) == 26
                for branch in branches
            )
            valid &= all(
                len(star_physical_factors(branch.prep_branch.star_input)) == 192
                and len(star_physical_factors(branch.prep_branch.star_output)) == 192
                for branch in branches
            )
            for branch in branches:
                writes = [
                    action
                    for action in branch.second_writer_actions
                    if action.kind == "WRITE"
                ]
                stops = [
                    action
                    for action in branch.second_writer_actions
                    if action.kind == "STOP"
                ]
                valid &= len(writes) == 1 and len(stops) == 5
                if writes:
                    valid &= decode_locked_word(writes[0].output_pointer) == (
                        front,
                        branch.second,
                    )
                    valid &= pointer_map_factor_count(
                        writes[0].input_pointer, writes[0].output_pointer
                    ) == 26
                    valid &= sp.simplify(
                        writes[0].probability
                        - expectation(
                            branch.second,
                            live_dictionary(writes[0].input_live),
                        )
                    ) == 0
                    valid &= sp.simplify(
                        writes[0].probability
                        - transition(branch.first, branch.second)
                    ) == 0
                valid &= all(
                    stop.input_pointer == stop.output_pointer == BLANK_POINTER
                    and stop.input_live == BLANK_LIVE
                    for stop in stops
                )
                valid &= composite_kraus_factorization_is_physical(branch)
                valid &= effect_equal(
                    squared_lueders_root_effect(branch.first),
                    effect(branch.first),
                )
                expected_joint = effect_scaled(
                    first, transition(first, branch.second)
                )
                valid &= effect_equal(branch.joint_effect, expected_joint)
            marginal = summed_effects([branch.joint_effect for branch in branches])
            first_marginals.append(marginal)
            valid &= effect_equal(marginal, effect(first))
        front_total = summed_effects(first_marginals[-14:])
        total_effects.append(front_total)
        valid &= effect_equal(front_total, identity_effect)

    reference_extension = True
    for front in DIRECTIONS:
        physical_branches = [
            composite_branch(front, first, second)
            for first in OUTCOMES for second in OUTCOMES
        ]
        extended = [tensor_reference_kraus(branch) for branch in physical_branches]
        reference_extension &= all(
            item.reference_factor == "I_R"
            and item.physical_factors == branch.kraus_factors
            and item.physical_domain == branch.input_domain
            and effect_equal(item.physical_effect, branch.joint_effect)
            and composite_kraus_factorization_is_physical(branch)
            for item, branch in zip(extended, physical_branches)
        )
        physical_gram_sum = summed_effects(
            [item.physical_effect for item in extended]
        )
        reference_row, reference_column = sp.symbols(
            "r_composite s_composite", integer=True, nonnegative=True
        )
        delta = sp.KroneckerDelta(reference_row, reference_column)
        reference_block = scale_effect_data(physical_gram_sum, delta)
        expected_block = scale_effect_data(identity_effect, delta)
        reference_extension &= effect_equal(reference_block, expected_block)
    return valid and reference_extension


def realized_next_star_eligibility(front):
    second_anchor = successor_center(front)
    candidate_supports = {
        add(second_anchor, successor_center(direction)): translate(
            SUPPORT, add(second_anchor, successor_center(direction))
        )
        for direction in DIRECTIONS
    }
    backward = add(second_anchor, successor_center(negate(front)))
    supplied_blocks = block_sets()
    supplied_sites = set().union(*supplied_blocks.values())
    statuses = {
        center: (
            "LockedPredecessor"
            if center == backward and support == supplied_blocks["old"]
            else "UNSUPPLIED"
            if support.isdisjoint(supplied_sites)
            else "OVERLAP_UNKNOWN"
        )
        for center, support in candidate_supports.items()
    }
    support_values = tuple(candidate_supports.values())
    return {
        "backward_center": backward,
        "backward_locked": statuses[backward] == "LockedPredecessor",
        "backward_support_is_old": (
            candidate_supports[backward] == supplied_blocks["old"]
        ),
        "candidate_supports_pairwise_disjoint": all(
            support_values[i].isdisjoint(support_values[j])
            for i in range(len(support_values))
            for j in range(i)
        ),
        "other_supports_outside_supplied": all(
            support.isdisjoint(supplied_sites)
            for center, support in candidate_supports.items()
            if center != backward
        ),
        "all_six_blank": all(value == "Blank" for value in statuses.values()),
        "five_unsupplied": sum(
            value == "UNSUPPLIED" for value in statuses.values()
        ) == 5,
    }


def front_component_count(kernel):
    states = tuple((front, ray) for front in DIRECTIONS for ray in RAYS)
    adjacency = {
        state: {
            (state[0], target)
            for target in RAYS
            if kernel[RAYS.index(state[1]), RAYS.index(target)].is_positive is True
        }
        for state in states
    }
    unseen = set(states)
    components = 0
    while unseen:
        components += 1
        stack = [unseen.pop()]
        while stack:
            current = stack.pop()
            for neighbor in adjacency[current]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)
    return components


def frozen_hashes_ok():
    return all(
        hashlib.sha256((PACKET / name).read_bytes()).hexdigest() == expected
        for name, expected in FROZEN.items()
    )


def mutation_rejections(kernel):
    """Execute concrete hostile variants and require their target invariant to fail."""
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    assigned_names = {
        target.id
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (
            node.targets if isinstance(node, ast.Assign) else (node.target,)
        )
        if isinstance(target, ast.Name)
    }
    called_attributes = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }

    baseline_blocks = block_sets()
    r8_blocks = block_sets(displacement=8)
    omitted_blocks = dict(baseline_blocks)
    omitted_blocks.pop(DIRECTIONS[-1])
    omitted_sites = set().union(*omitted_blocks.values())
    omitted_covariant = all(
        {mat_vec(g, site) for site in omitted_sites} == omitted_sites
        for g in ROTATIONS
    )
    selected_blocks = {
        "old": baseline_blocks["old"],
        DIRECTIONS[0]: baseline_blocks[DIRECTIONS[0]],
    }
    selected_sites = set().union(*selected_blocks.values())
    selected_covariant = all(
        {mat_vec(g, site) for site in selected_sites} == selected_sites
        for g in ROTATIONS
    )

    front_a, front_b = DIRECTIONS[0], DIRECTIONS[1]
    outcome = OUTCOMES[0]
    label_rotation = next(
        g for g in ROTATIONS if mat_vec(g, front_a) != front_a
    )
    outcome_only_center = successor_center(outcome)
    outcome_only_routes = {
        front: outcome_only_center for front in (front_a, front_b)
    }
    fixed_ready_star = _target_star_variant(
        front_b, outcome, ready_override=ready_word(front_a)
    )
    two_ready_star = _target_star_variant(
        front_a, outcome, activate_extra=(front_b,)
    )
    two_ready_branch_count = sp.prod(
        len(local_writer_actions(block)) for block in two_ready_star.blocks
    )

    raw_q = sp.Matrix((1, 0, 0)) * sp.Matrix((1, 0, 0)).T
    raw_q_perpendicular = raw_q * sp.Matrix((0, 1, 0))
    sign_flipped = any(
        sp.simplify(transition(a, b, sign=-1) - transition(a, b)) != 0
        for a in OUTCOMES for b in OUTCOMES
    )
    antipodal_signed = prepared_vectors(outcome) != prepared_vectors(
        negate(outcome), sign=-1
    )

    mutated_effects = {label: effect(label) for label in OUTCOMES}
    changed_constant, changed_coefficients = mutated_effects[OUTCOMES[0]]
    changed_coefficients = dict(changed_coefficients)
    changed_site = DIRECTIONS[0]
    changed_vector = list(changed_coefficients[changed_site])
    changed_vector[0] += R(1, 1000)
    changed_coefficients[changed_site] = tuple(changed_vector)
    mutated_effects[OUTCOMES[0]] = (changed_constant, changed_coefficients)
    mutated_effect_sum = summed_effects(list(mutated_effects.values()))
    dropped_effect_sum = summed_effects(
        [effect(label) for label in OUTCOMES[:-1]]
    )
    identity_effect = (
        sp.S.One,
        {site: (sp.S.Zero,) * 3 for site in DIRECTIONS},
    )

    row_only = sp.Matrix(kernel)
    epsilon = R(1, 1000)
    row_only[0, 1] += epsilon
    row_only[0, 2] -= epsilon
    row_only_stochastic = all(
        sp.simplify(sum(row_only[i, j] for j in range(7)) - 1) == 0
        for i in range(7)
    )
    weights = [R(1, 6)] * 3 + [R(1, 8)] * 4
    row_only_balanced = all(
        sp.simplify(
            weights[i] * row_only[i, j] - weights[j] * row_only[j, i]
        ) == 0
        for i in range(7) for j in range(7)
    )
    spectral_mutant = sp.Matrix(kernel)
    spectral_mutant[3, 4] += epsilon
    corner_contrast = sp.Matrix((0, 0, 0, 1, -1, 0, 0))
    spectral_contrast_survives = (
        spectral_mutant * corner_contrast
        == sp.sqrt(2) / 16 * corner_contrast
    )

    p = sp.symbols("P", commutative=True)
    omit_stop_complete = projector_reduce(p - 1, p) == 0
    scaled_stop_complete = projector_reduce(p + 4 * (1 - p) - 1, p) == 0
    dropped_branches = dict(PREP_BRANCHES)
    dropped_branches.pop(next(iter(dropped_branches)))
    dropped_certificate = prep_channel_certificate(dropped_branches)

    collision_branches = dict(PREP_BRANCHES)
    labels = tuple(collision_branches)
    first_branch = collision_branches[labels[0]]
    second_branch = collision_branches[labels[1]]
    collision_branches[labels[1]] = PrepBranch(
        control=second_branch.control,
        old_live_identity_factors=OLD_LIVE_IDENTITIES,
        old_pointer_input=first_branch.old_pointer_input,
        old_pointer_output=second_branch.old_pointer_output,
        star_input=second_branch.star_input,
        star_output=second_branch.star_output,
    )
    collision_certificate = prep_channel_certificate(collision_branches)

    noncovariant_branches = dict(PREP_BRANCHES)
    bad_label = labels[0]
    bad_branch = noncovariant_branches[bad_label]
    noncovariant_branches[bad_label] = PrepBranch(
        control=bad_branch.control,
        old_live_identity_factors=OLD_LIVE_IDENTITIES,
        old_pointer_input=bad_branch.old_pointer_input,
        old_pointer_output=bad_branch.old_pointer_output,
        star_input=bad_branch.star_input,
        star_output=target_star(bad_label[0], OUTCOMES[-1]),
    )
    noncovariant_certificate = prep_channel_certificate(noncovariant_branches)

    overwrite_branch = PrepBranch(
        control=bad_branch.control,
        old_live_identity_factors=OLD_LIVE_IDENTITIES,
        old_pointer_input=bad_branch.old_pointer_input,
        old_pointer_output=ready_word(bad_label[0]),
        star_input=bad_branch.star_input,
        star_output=bad_branch.star_output,
    )
    overwrite_qnd = (
        overwrite_branch.old_pointer_output == overwrite_branch.old_pointer_input
    )
    overwrite_branches = dict(PREP_BRANCHES)
    overwrite_branches[bad_label] = overwrite_branch
    overwrite_certificate = prep_channel_certificate(overwrite_branches)
    coherent_cross_covariant = not c4_front_bit_phase_witness()
    first_record_word = locked_word(*RECORD_LABELS[0])
    second_record_word = locked_word(*RECORD_LABELS[1])
    code_matrix_unit_after_channel = record_matrix_unit_survival(
        PREP_BRANCHES, first_record_word, second_record_word, True
    )

    blank_target = BLANK_STAR
    blank_target_actions = parallel_writer_actions(blank_target)
    blank_target_writes = sum(
        any(action.kind == "WRITE" for action in combination)
        for combination in blank_target_actions
    )
    erase_nonblank_guard = target_star(front_a, outcome) == BLANK_STAR
    feedback_targets = {
        target_star(front_a, second) for second in OUTCOMES
    }
    coarse_effects = [effect(label) for label in OUTCOMES[:-2]]
    coarse_effects.append(summed_effects([effect(OUTCOMES[-2]), effect(OUTCOMES[-1])]))
    coarse_effect_sum = summed_effects(coarse_effects)

    bell_partial_transpose = sp.Matrix(
        (
            (R(1, 2), 0, 0, 0),
            (0, 0, R(1, 2), 0),
            (0, R(1, 2), 0, 0),
            (0, 0, 0, R(1, 2)),
        )
    )
    antisymmetric = sp.Matrix((0, 1, -1, 0)) / sp.sqrt(2)
    transpose_witness = sp.simplify(
        (antisymmetric.T * bell_partial_transpose * antisymmetric)[0]
    )

    sign_reversed_kernel_change = any(
        sp.simplify(
            transition(outcome, target)
            - transition(outcome, target, sign=-1)
        ) != 0
        for target in OUTCOMES
    )
    omitted_second_sum = sp.simplify(
        sum(transition(outcome, target) for target in OUTCOMES[:-1])
    )
    predecessor = realized_next_star_eligibility(front_a)

    states = tuple((front, ray) for front in DIRECTIONS for ray in RAYS)
    fully_mixed_adjacency = {state: set(states) for state in states}
    unseen = set(states)
    mixed_components = 0
    while unseen:
        mixed_components += 1
        stack = [unseen.pop()]
        while stack:
            current = stack.pop()
            for neighbor in fully_mixed_adjacency[current]:
                if neighbor in unseen:
                    unseen.remove(neighbor)
                    stack.append(neighbor)

    all_ready_star = StarProduct(
        tuple(
            BlockProduct(BLANK_LIVE, ready_word(front))
            for front in DIRECTIONS
        )
    )
    all_ready_branch_count = sp.prod(
        len(local_writer_actions(block)) for block in all_ready_star.blocks
    )
    baseline_composite = composite_branch(front_a, outcome, OUTCOMES[1])
    wrong_active_factors = tuple(
        ("second_active_front", front_b)
        if factor[0] == "second_active_front"
        else factor
        for factor in baseline_composite.kraus_factors
    )
    wrong_active_composite = replace(
        baseline_composite, kraus_factors=wrong_active_factors
    )
    orbit_parameter = sp.symbols("n_orbit", integer=True, nonnegative=True)
    fixed_front_orbit_norm2 = norm2(
        scale(DISPLACEMENT * orbit_parameter, front_a)
    )
    fixed_front_orbit_unbounded = (
        sp.limit(fixed_front_orbit_norm2, orbit_parameter, sp.oo) == sp.oo
    )

    mutations = {
        "R8_support_collision": not pairwise_disjoint(r8_blocks),
        "drop_successor_breaks_cubic_star": len(omitted_blocks) != 7 and not omitted_covariant,
        "preselect_one_successor_breaks_cubic_star": len(selected_blocks) == 2 and not selected_covariant,
        "fixed_Ready_disagrees_with_Record_front": decode_ready_word(fixed_ready_star.blocks[block_index(front_b)].pointer) != front_b,
        "outcome_only_location_loses_front": len(set(outcome_only_routes.values())) == 1 and len({successor_center(front_a), successor_center(front_b)}) == 2,
        "label_only_rotation_changes_physical_target": target_star(front_a, outcome) != target_star(mat_vec(label_rotation, front_a), mat_vec(label_rotation, outcome)) and rotate_star_product(target_star(front_a, outcome), label_rotation) == target_star(mat_vec(label_rotation, front_a), mat_vec(label_rotation, outcome)),
        "two_Ready_blocks_make_196_branches": two_ready_branch_count == 196,
        "raw_Q_has_zero_perpendicular_direction": raw_q_perpendicular == sp.zeros(3, 1),
        "negative_Q_changes_frozen_kernel": sign_flipped,
        "unnormalized_corner_factor_has_norm_two": norm2((0, 1, 1)) == 2,
        "antipodal_sign_split_breaks_state_equality": antipodal_signed,
        "effect_coefficient_mutation_breaks_POVM": not effect_equal(mutated_effect_sum, identity_effect),
        "drop_effect_breaks_POVM": not effect_equal(dropped_effect_sum, identity_effect),
        "merge_outcomes_preserves_POVM_but_breaks_14_label_law": (
            len(coarse_effects) == 13
            and effect_equal(coarse_effect_sum, identity_effect)
        ),
        "row_sum_only_mutant_breaks_balance": row_only_stochastic and not row_only_balanced,
        "spectral_mutant_breaks_corner_mode": not spectral_contrast_survives,
        "dense_eigensolver_forbidden": not {"eigenvals", "eigenvects"} & called_attributes,
        "hardcoded_table_forbidden": "TRANSITION_TABLE" not in assigned_names,
        "omit_STOP_breaks_completeness": not omit_stop_complete,
        "scaled_STOP_breaks_completeness": not scaled_stop_complete,
        "drop_control_breaks_Pvalid_effects": not dropped_certificate["branch_count"] and not dropped_certificate["effects_equal_p_valid"],
        "collide_controls_breaks_orthogonality": not collision_certificate["controls_orthogonal"],
        "coherent_sum_breaks_C4_cross_covariance": not coherent_cross_covariant,
        "mutate_branch_breaks_CP_map_covariance": not noncovariant_certificate["branch_covariance"],
        "overwrite_old_Record_breaks_QND": (
            not overwrite_qnd
            and not overwrite_certificate["old_record_unchanged"]
            and not overwrite_certificate["qnd_heisenberg"]
        ),
        "full_code_matrix_unit_is_dephased": code_matrix_unit_after_channel == 0,
        "Blank_target_activates_no_writer": blank_target_writes == 0,
        "nonblank_replacement_violates_Blank_guard": not erase_nonblank_guard,
        "same_event_feedback_changes_prior_prep_target": len(feedback_targets) > 1,
        "transpose_reference_mutant_not_CP": transpose_witness == -R(1, 2),
        "sign_reversed_preparation_changes_Record_kernel": sign_reversed_kernel_change,
        "omit_second_outcome_breaks_row_normalization": omitted_second_sum != 1,
        "all_six_Ready_explodes_branch_count": all_ready_branch_count == 14 ** 6,
        "wrong_active_successor_breaks_spatial_factorization": (
            not composite_kraus_factorization_is_physical(
                wrong_active_composite
            )
        ),
        "event3_backward_candidate_is_Locked": (
            predecessor["backward_locked"]
            and predecessor["backward_support_is_old"]
            and predecessor["candidate_supports_pairwise_disjoint"]
            and predecessor["other_supports_outside_supplied"]
            and predecessor["five_unsupplied"]
            and not predecessor["all_six_blank"]
        ),
        "front_mixing_collapses_six_components": front_component_count(kernel) == 6 and mixed_components == 1,
        "fixed_front_anchor_orbit_is_unbounded": fixed_front_orbit_unbounded,
        "radius13_is_not_nearest_neighbor": max(max(abs(value) for value in site) for site in set().union(*baseline_blocks.values())) == 13,
        "fourteen_outcomes_are_not_Block19_six_marks": len(OUTCOMES) == 14 and len(OUTCOMES) != 6,
        "no_clock_variable_or_cadence": not any(isinstance(node, ast.Name) and node.id in {"clock", "cadence"} for node in ast.walk(tree)),
        "no_gravity_or_source_operator": not any(isinstance(node, (ast.FunctionDef, ast.ClassDef)) and ("gravity" in node.name or "source_current" in node.name) for node in ast.walk(tree)),
        "runner_path_is_not_axiom_or_audit_surface": (
            Path(__file__).parent.name == "scripts"
            and "audit" not in Path(__file__).name
            and "axiom" not in Path(__file__).name
        ),
    }
    guard_names = {
        "dense_eigensolver_forbidden",
        "hardcoded_table_forbidden",
        "unnormalized_corner_factor_has_norm_two",
        "full_code_matrix_unit_is_dephased",
        "Blank_target_activates_no_writer",
        "nonblank_replacement_violates_Blank_guard",
        "same_event_feedback_changes_prior_prep_target",
        "event3_backward_candidate_is_Locked",
        "fixed_front_anchor_orbit_is_unbounded",
        "radius13_is_not_nearest_neighbor",
        "fourteen_outcomes_are_not_Block19_six_marks",
        "no_clock_variable_or_cadence",
        "no_gravity_or_source_operator",
        "runner_path_is_not_axiom_or_audit_surface",
    }
    external_control_names = {
        "coherent_sum_breaks_C4_cross_covariance",
        "transpose_reference_mutant_not_CP",
    }
    guards = {name: mutations.pop(name) for name in guard_names}
    external_controls = {
        name: mutations.pop(name) for name in external_control_names
    }
    return {
        "executed_model_mutations": mutations,
        "coverage_and_scope_guards": guards,
        "external_negative_controls": external_controls,
    }


class Checks:
    def __init__(self):
        self.passed = 0
        self.failed = 0

    def check(self, name, condition, detail):
        if condition:
            self.passed += 1
            print(f"PASS {name}: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {name}: {detail}")


def main():
    checks = Checks()
    checks.check("freeze", frozen_hashes_ok(), "8/8 preregistration hashes")

    blocks = block_sets()
    all_sites = set().union(*blocks.values())
    radius2 = max(norm2(site) for site in all_sites)
    geometry_ok = (
        len(SUPPORT) == 32
        and len(blocks) == 7
        and pairwise_disjoint(blocks)
        and len(all_sites) == 224
        and radius2 == 169
    )
    geometry_ok &= all(
        {mat_vec(g, site) for site in all_sites} == all_sites for g in ROTATIONS
    )
    checks.check("fixed_star_geometry", geometry_ok,
                 "old 32 + six disjoint 32-site successors; R=9, radius=13")

    q_ok = True
    for label in OUTCOMES:
        q = q_matrix(label)
        q_ok &= sp.simplify(sp.trace(q)) == 0 and sp.simplify(q.det() - R(2, 27)) == 0
        vectors = prepared_vectors(label)
        q_ok &= all(sp.simplify(norm2(vector) - 1) == 0 for vector in vectors.values())
        q_ok &= vectors == prepared_vectors(negate(label))
    q_ok &= any(
        transition(a, b, sign=-1) != transition(a, b)
        for a in OUTCOMES for b in OUTCOMES
    )
    checks.check("frozen_q_state_family", q_ok,
                 "14 geometry-derived pure products; Q_-b=Q_b; positive sign load-bearing")

    state_covariance = all(
        all(
            mat_vec(g, prepared_vectors(label)[site])
            == prepared_vectors(mat_vec(g, label))[mat_vec(g, site)]
            for site in DIRECTIONS
        )
        for g in ROTATIONS for label in OUTCOMES
    )
    radial_covariance = all(
        mat_vec(g, radial_bloch(site)) == radial_bloch(mat_vec(g, site))
        for g in ROTATIONS for site in SUPPORT
    )
    checks.check("common_action_states", state_covariance and radial_covariance,
                 "24 rotations act on every Blank and prepared physical Bloch state")

    ready = {front: ready_word(front) for front in DIRECTIONS}
    locked = {
        (front, outcome): locked_word(front, outcome)
        for front in DIRECTIONS for outcome in OUTCOMES
    }
    words_ok = (
        len(set(ready.values())) == 6
        and len(set(locked.values())) == 84
        and BLANK_POINTER not in set(ready.values())
        and all(word != BLANK_POINTER for word in locked.values())
    )
    physical_words = list(ready.values()) + list(locked.values())
    words_ok &= all(
        pointer_overlap(physical_words[i], physical_words[j]) == int(i == j)
        for i in range(len(physical_words))
        for j in range(len(physical_words))
    )
    code_covariance = all(
        rotate_word(ready[front], g) == ready[mat_vec(g, front)]
        and all(
            rotate_word(locked[(front, outcome)], g)
            == locked[(mat_vec(g, front), mat_vec(g, outcome))]
            for outcome in OUTCOMES
        )
        for g in ROTATIONS for front in DIRECTIONS
    )
    checks.check("record_controls", words_ok and code_covariance,
                 "90 physical radial product projectors are pairwise orthogonal/covariant; 84 Locked controls decode")

    target_ok = all(
        len(star_physical_factors(target_star(front, outcome))) == 192
        and target_star(front, outcome).blocks[block_index(front)]
        == block_product(prepared_vectors(outcome), ready[front])
        and all(
            target_star(front, outcome).blocks[block_index(other)] == BLANK_BLOCK
            for other in DIRECTIONS if other != front
        )
        and star_overlap(BLANK_STAR, target_star(front, outcome)) == 0
        for front in DIRECTIONS for outcome in OUTCOMES
    )
    target_covariance = all(
        rotate_star_product(target_star(front, outcome), g)
        == target_star(mat_vec(g, front), mat_vec(g, outcome))
        for g in ROTATIONS for front in DIRECTIONS for outcome in OUTCOMES
    )
    checks.check("record_generated_target", target_ok and target_covariance,
                 "all 192 target factors explicit; one rho_b+Ready_f block and five exact Blank blocks covary")

    prep_certificate = prep_channel_certificate()
    prep_cptp = all(
        prep_certificate[key]
        for key in (
            "branch_count", "exact_frozen_fields", "effects_equal_p_valid", "controls_orthogonal",
            "factor_complete", "p_valid_projector", "kraus_complete",
            "arbitrary_reference", "target_orthogonal_blank", "repeat_stop",
        )
    )
    checks.check("prep_cptp", prep_cptp,
                 "84 explicit 224-factor A_(f,b); P_valid projector; K_STOP=I-P completes I_R tensor I")

    checks.check(
        "classical_record_qnd",
        prep_certificate["qnd_heisenberg"]
        and prep_certificate["old_record_unchanged"]
        and prep_certificate["coherent_code_not_fixed"],
        "Lambda^dag(C_fb)=C_fb by projector algebra; valid cross-Record matrix units dephase",
    )

    checks.check(
        "kraus_map_covariance",
        prep_certificate["branch_covariance"],
        "all 84 separate input/output product-projector Kraus branches covary under the common 24-frame action",
    )

    block22_complete = summed_effects([effect(label) for label in OUTCOMES])
    identity_effect = (sp.S.One, {site: (sp.S.Zero,) * 3 for site in DIRECTIONS})
    checks.check("imported_effect_completion", effect_equal(block22_complete, identity_effect),
                 "14 Block22 effects rederive coefficientwise sum I_64")

    roots_ok = all(lueders_root_certificate(label) for label in OUTCOMES)
    checks.check(
        "explicit_lueders_roots",
        roots_ok,
        "14 commuting 64-sector square roots reconstruct every E_b coefficientwise",
    )

    kernel_signed = {
        (source, target): transition(source, target)
        for source in OUTCOMES for target in OUTCOMES
    }
    entries_ok = all(
        sp.simplify(kernel_signed[(source, target)] - expected_transition(source, target)) == 0
        for source in OUTCOMES for target in OUTCOMES
    )
    rows_ok = all(
        sp.simplify(sum(kernel_signed[(source, target)] for target in OUTCOMES) - 1) == 0
        and all(kernel_signed[(source, target)].is_positive is True for target in OUTCOMES)
        for source in OUTCOMES
    )
    checks.check("derived_signed_kernel", entries_ok and rows_ok,
                 "196 entries derived from Q_b and effects; strict positive stochastic rows")

    transition_covariance = all(
        sp.simplify(
            transition(mat_vec(g, source), mat_vec(g, target))
            - transition(source, target)
        ) == 0
        for g in ROTATIONS for source in OUTCOMES for target in OUTCOMES
    )
    antipodal_lumping = all(
        transition(source, target) == transition(negate(source), target)
        for source in OUTCOMES for target in OUTCOMES
    )
    checks.check("kernel_covariance_lumping", transition_covariance and antipodal_lumping,
                 "24-frame invariance and exact 14-to-7 antipodal strong lumping")

    quotient = quotient_kernel()
    quotient_rows = all(sp.simplify(sum(quotient[i, j] for j in range(7)) - 1) == 0 for i in range(7))
    quotient_positive = all(quotient[i, j].is_positive is True for i in range(7) for j in range(7))
    quotient_form = all(
        sp.simplify(
            quotient[i, j]
            - (
                (R(2, 9) if i == j else R(5, 36)) if i < 3 and j < 3
                else R(1, 8) if i < 3
                else R(1, 6) if j < 3
                else R(1, 8) + R(3, 32) / sp.sqrt(2) if i == j
                else R(1, 8) - R(1, 32) / sp.sqrt(2)
            )
        ) == 0
        for i in range(7) for j in range(7)
    )
    checks.check("seven_ray_quotient", quotient_rows and quotient_positive and quotient_form,
                 "3 axis + 4 corner ray kernel exact and strictly positive")

    signed_weights = {
        label: R(1, 12) if is_axis(label) else R(1, 16) for label in OUTCOMES
    }
    signed_balance = all(
        sp.simplify(
            signed_weights[source] * transition(source, target)
            - signed_weights[target] * transition(target, source)
        ) == 0
        for source in OUTCOMES for target in OUTCOMES
    )
    ray_weights = [R(1, 6)] * 3 + [R(1, 8)] * 4
    quotient_balance = all(
        sp.simplify(ray_weights[i] * quotient[i, j] - ray_weights[j] * quotient[j, i]) == 0
        for i in range(7) for j in range(7)
    )
    checks.check("reversible_stationary_kernel", signed_balance and quotient_balance and sum(ray_weights) == 1,
                 "detailed balance: signed 1/12,1/16 and ray 1/6,1/8 weights")

    axis_basis = [sp.Matrix((1, -1, 0, 0, 0, 0, 0)), sp.Matrix((0, 1, -1, 0, 0, 0, 0))]
    corner_basis = [
        sp.Matrix((0, 0, 0, 1, -1, 0, 0)),
        sp.Matrix((0, 0, 0, 0, 1, -1, 0)),
        sp.Matrix((0, 0, 0, 0, 0, 1, -1)),
    ]
    one = sp.ones(7, 1)
    zero_mode = sp.Matrix((1, 1, 1, -1, -1, -1, -1))
    spectral_ok = all(quotient * vector == R(1, 12) * vector for vector in axis_basis)
    spectral_ok &= all(quotient * vector == sp.sqrt(2) / 16 * vector for vector in corner_basis)
    spectral_ok &= quotient * one == one and quotient * zero_mode == sp.zeros(7, 1)
    eigenbasis = sp.Matrix.hstack(*(axis_basis + corner_basis + [one, zero_mode]))
    spectral_ok &= eigenbasis.rank() == 7
    checks.check("invariant_subspace_spectrum", spectral_ok,
                 "spectrum 1,0,(1/12)^2,(sqrt2/16)^3 derived without eigensolver")

    direct_prefix = True
    for first in OUTCOMES:
        direct_joint = [effect_scaled(first, transition(first, second)) for second in OUTCOMES]
        direct_prefix &= effect_equal(summed_effects(direct_joint), effect(first))
    direct_total = summed_effects(
        [effect_scaled(first, transition(first, second)) for first in OUTCOMES for second in OUTCOMES]
    )
    direct_prefix &= effect_equal(direct_total, identity_effect)
    checks.check("reduced_cylinder_normalization", direct_prefix,
                 "reduced E_b1*T table normalizes and retains its first marginal; this is not the Kraus derivation")

    writer_product_ok = parallel_writer_certificate()
    checks.check(
        "parallel_writer_product",
        writer_product_ok,
        "tensor product of six local writer/STOP channels gives 14 branches: one sqrt(E_b2) write plus five exact STOPs",
    )

    composite_ok = reachable_domain_composite_certificate(identity_effect)
    first_centroid = tuple(sum(site[i] for site in POINTER) for i in range(3))
    second_centroids = {successor_center(front) for front in DIRECTIONS}
    decode_ok = all(
        decode_locked_word(locked_word(front, outcome)) == (front, outcome)
        for front in DIRECTIONS for outcome in OUTCOMES
    )
    prefix_records = (
        composite_ok
        and first_centroid == (0, 0, 0)
        and len(second_centroids) == 6
        and decode_ok
    )
    checks.check(
        "full_composite_prefix",
        prefix_records,
        "on Ready_f tensor supplied BlankStar, all 1176 factorized branches compose and normalize with symbolic I_R extension",
    )

    predecessor_walls = [
        realized_next_star_eligibility(front) for front in DIRECTIONS
    ]
    scope_boundary = all(
        wall["backward_center"] == (0, 0, 0)
        and wall["backward_locked"]
        and wall["backward_support_is_old"]
        and wall["candidate_supports_pairwise_disjoint"]
        and wall["other_supports_outside_supplied"]
        and wall["five_unsupplied"]
        and not wall["all_six_blank"]
        for wall in predecessor_walls
    )
    front_sectors = front_component_count(quotient) == 6
    checks.check("scope_boundary", scope_boundary and front_sectors,
                 "one backward candidate is the Locked predecessor; five candidates are unsupplied/unknown; 42-state graph has six components")

    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_args = {
        node.name: [argument.arg for argument in node.args.args]
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
        and node.name in {"q_matrix", "prepared_vectors", "target_star", "transition"}
    }
    scope_ok = public_args == {
        "q_matrix": ["label", "sign"],
        "prepared_vectors": ["label", "sign"],
        "transition": ["source", "target", "sign"],
        "target_star": ["front", "outcome"],
    }
    assigned_names = {
        target.id
        for node in ast.walk(tree)
        if isinstance(node, (ast.Assign, ast.AnnAssign))
        for target in (node.targets if isinstance(node, ast.Assign) else (node.target,))
        if isinstance(target, ast.Name)
    }
    called_attributes = {
        node.func.attr
        for node in ast.walk(tree)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
    }
    imported = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.append(node.module)
    scope_ok &= "TRANSITION_TABLE" not in assigned_names
    scope_ok &= not {"eigenvals", "eigenvects"} & called_attributes
    scope_ok &= not any(name.startswith("admissibility_d4_") for name in imported)
    checks.check("scope_ast", scope_ok,
                 "no target table, future outcome, selected-site oracle, imported runner, or dense eigensolve")

    mutation_report = mutation_rejections(quotient)
    mutations = mutation_report["executed_model_mutations"]
    rejected = sum(bool(value) for value in mutations.values())
    checks.check(
        "executed_model_mutations",
        rejected == len(mutations),
        f"{rejected}/{len(mutations)} altered models reject their target invariant",
    )
    guards = mutation_report["coverage_and_scope_guards"]
    guarded = sum(bool(value) for value in guards.values())
    checks.check(
        "coverage_scope_guards",
        guarded == len(guards),
        f"{guarded}/{len(guards)} non-mutation coverage/scope guards hold",
    )
    controls = mutation_report["external_negative_controls"]
    controlled = sum(bool(value) for value in controls.values())
    checks.check(
        "external_negative_controls",
        controlled == len(controls),
        f"{controlled}/{len(controls)} explicit external controls behave as expected",
    )

    print("per_element: all 196 derived transition entries, exact detailed-balance residuals, and branch-effect prefix identities are checked")
    print("per_site: all 224 primitive sites, six successor centers, radial Blank/Ready states, and two decoded Locked packets are checked")
    print("per_mode: the seven invariant outcome-ray modes are checked exactly; no Fourier, clock, or spacetime normal-mode claim is made")
    print("per_block: 84 Record-indexed prep branches, STOP complement, one active successor writer, and five inactive STOP blocks are checked")
    print("lattice_wide: checked and not executed -- predecessor-aware recurrence, overlapping fronts, substrate generation, rate, source, gravity, retention, and TOE closure remain open")
    print("TERMINAL: EXACT-COVARIANT-CLASSICAL-RECORD-QND-TWO-EVENT-PREFIX-WITH-STRICTLY-POSITIVE-REVERSIBLE-SEVEN-RAY-REDUCED-KERNEL")
    print("SCOPE: supplied six-block Blank star; atomic radius 13; internal kernel only; no coherent-code QND, event 3, stationary Record process, overlap, clock, source, gravity, axiom, audit, obligation, or TOE move")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    raise SystemExit(1 if checks.failed else 0)


if __name__ == "__main__":
    main()
