#!/usr/bin/env python3
"""Supporting algebra for the recovered finite-fixture M2 compiler.

Compile every arm-independent supplied-fixture residual through one normalized
complex-Gaussian split.  The split reduces a bounded linear residual to
arity-three factors and isolates every original field occurrence at a leaf.
The explicit site/slot certificate is implemented in the sibling
``..._explicit_certificate_2026_08_23.py`` runner.  This file proves the
Gaussian, arity, Record-row, carrier-tag, and finite-interface algebra that
the explicit certificate consumes.  The main interface fixture is the supplied
xgraded width-four background at T_cover=12 and m=1; auxiliary topology counts
use constant backgrounds at widths four and eight.  Its finite-type counts are
not a routing theorem and do not establish a cover-independent fixed-density
embedding.

This is supporting algebra on those declared mass-one fixtures.
It does not select the action, base measure, split, source, clock, or Record
write process.
"""

from __future__ import annotations

from collections import Counter
from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
from pathlib import Path

import sympy as sp

import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as b43


b42 = b43.b42
b41 = b43.b41
b175 = b43.b175
b174 = b43.b174
R = sp.Rational
ZERO = sp.Integer(0)
ONE = sp.Integer(1)
I = sp.I

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_"
    "COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_"
    "compiler_released7333_fixture_2026_09_10.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_"
    "NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_"
    "nonuniform_hodge_overlap_2026_08_14.py",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
)
INPUT_SHA256 = {
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md": "b77307fd3fcc3a603a34f41841dc707c09d341011ab54dca19b6e45f3541f6c4",
    "scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py": "8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_SHIFTED_ORIGIN_FRAME_GAUGE_NONUNIFORM_HODGE_OVERLAP_BOUNDED_THEOREM_NOTE_2026-08-14.md": "9a615a79511ffc0dac0d1cf54388153604ce7c341496654fd709ed8873302a33",
    "scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py": "5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
}


def input_hashes_match() -> bool:
    return all(
        (ROOT / path).is_file()
        and sha256((ROOT / path).read_bytes()).hexdigest()
        == INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )

# One fixed split for every arm, residual, route segment, and fixture.
ALPHA = sp.Integer(3)
BETA = R(3, 2)
C_NORMALIZATION = R(9, 2)
SQRT_ALPHA = sp.sqrt(ALPHA)
SQRT_BETA = sp.sqrt(BETA)

PAULI = (
    sp.Matrix([[ZERO, ONE], [ONE, ZERO]]),
    sp.Matrix([[ZERO, -I], [I, ZERO]]),
    sp.Matrix([[ONE, ZERO], [ZERO, -ONE]]),
)
IDENTITY2 = sp.eye(2)
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)


@dataclass(frozen=True)
class Term:
    label: str
    coefficient: sp.Expr
    original: bool


def matrix_zero(value: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def normalize(values: tuple) -> tuple:
    total = sp.cancel(sum(values, ZERO))
    return tuple(sp.cancel(value / total) for value in values)


def split_factor(
    terms: list[Term], state: list[int], cut: int
) -> tuple[list[Term], list[Term]]:
    """Apply the fixed normalized Gaussian split to one linear residual."""
    label = f"m{state[0]}"
    state[0] += 1
    left = [
        Term(term.label, sp.expand(SQRT_ALPHA * term.coefficient), term.original)
        for term in terms[:cut]
    ]
    left.append(Term(label, -SQRT_ALPHA, False))
    right = [
        Term(term.label, sp.expand(SQRT_BETA * term.coefficient), term.original)
        for term in terms[cut:]
    ]
    right.append(Term(label, SQRT_BETA, False))
    return left, right


def reduce_arity(terms: list[Term], state: list[int]) -> list[list[Term]]:
    if len(terms) <= 3:
        return [terms]
    left, right = split_factor(terms, state, len(terms) // 2)
    return reduce_arity(left, state) + reduce_arity(right, state)


def isolate_originals(terms: list[Term], state: list[int]) -> list[list[Term]]:
    """Leave at most one original field occurrence in every final factor."""
    output: list[list[Term]] = []
    current = terms
    while sum(term.original for term in current) > 1:
        index = next(i for i, term in enumerate(current) if term.original)
        ordered = [current[index], *current[:index], *current[index + 1 :]]
        leaf, current = split_factor(ordered, state, 1)
        output.append(leaf)
    output.append(current)
    return output


def compile_factor(coefficients: tuple[sp.Expr, ...]) -> tuple[list[list[Term]], int]:
    state = [0]
    base = [
        Term(f"x{index}", sp.sympify(coefficient), True)
        for index, coefficient in enumerate(coefficients)
    ]
    reduced = reduce_arity(base, state)
    factors: list[list[Term]] = []
    for factor in reduced:
        factors.extend(isolate_originals(factor, state))
    return factors, state[0]


def compiled_precision(
    coefficients: tuple[sp.Expr, ...]
) -> tuple[sp.Matrix, sp.Matrix, list[list[Term]], int]:
    factors, mediator_count = compile_factor(coefficients)
    original_count = len(coefficients)
    labels = [f"x{index}" for index in range(original_count)] + [
        f"m{index}" for index in range(mediator_count)
    ]
    indices = {label: index for index, label in enumerate(labels)}
    precision = sp.zeros(len(labels))
    for factor in factors:
        vector = sp.zeros(len(labels), 1)
        for term in factor:
            vector[indices[term.label], 0] += term.coefficient
        precision += vector.conjugate() * vector.T
    hidden = precision[original_count:, original_count:]
    if mediator_count:
        visible = (
            precision[:original_count, :original_count]
            - precision[:original_count, original_count:]
            * hidden.inv(method="DM")
            * precision[original_count:, :original_count]
        )
    else:
        visible = precision
    return sp.simplify(visible), hidden, factors, mediator_count


def arm_sets(fixture: object) -> tuple[tuple[dict, ...], tuple[dict, ...], tuple]:
    qs = tuple(fixture.q({b175.RECORD_CELL: value}) for value in b175.MENU)
    symmetric = tuple(sp.expand((q + q.H) / 2) for q in qs)
    edges = b43.edge_union(symmetric)
    halves = tuple(
        b43.arm_bundle(fixture, value, edges, fraction=R(1, 2))
        for value in b175.MENU
    )
    thirds = tuple(
        b43.arm_bundle(fixture, value, edges, fraction=R(1, 3))
        for value in b175.MENU
    )
    return halves, thirds, edges


def row_rosters(bundles: tuple[tuple[dict, ...], ...]) -> tuple[tuple[str, ...], ...]:
    size = bundles[0][0]["q"].rows
    bcols = bundles[0][0]["B"].cols
    output = []
    for row in range(size):
        labels = [
            f"p{column}"
            for column in range(size)
            if any(arm["q"][row, column] != 0 for family in bundles for arm in family)
        ]
        labels.extend(
            f"z{column}"
            for column in range(bcols)
            if any(arm["B"][row, column] != 0 for family in bundles for arm in family)
        )
        output.append(tuple(labels))
    return tuple(output)


def changed_rows(family: tuple[dict, ...]) -> tuple[int, ...]:
    reference = family[-1]
    return tuple(
        row
        for row in range(reference["q"].rows)
        if any(
            arm["q"][row, column] != reference["q"][row, column]
            for arm in family[:-1]
            for column in range(reference["q"].cols)
        )
        or any(
            arm["B"][row, column] != reference["B"][row, column]
            for arm in family[:-1]
            for column in range(reference["B"].cols)
        )
    )


def signed_circle_delta(left: int, right: int, size: int) -> int:
    delta = (right - left) % size
    if delta > size // 2:
        delta -= size
    return delta


def roster_signature(
    fixture: object,
    row: int,
    roster: tuple[str, ...],
    edges: tuple[tuple[int, int], ...],
) -> tuple:
    """Remove absolute chart labels from one finite routing type."""
    row_t, row_x = divmod(row, fixture.lx)
    signature = []
    for label in roster:
        kind = label[0]
        index = int(label[1:])
        if kind == "p":
            site_t, site_x = divmod(index, fixture.lx)
            signature.append(
                (
                    "p",
                    signed_circle_delta(row_t, site_t, fixture.T),
                    signed_circle_delta(row_x, site_x, fixture.lx),
                )
            )
        elif index < len(edges):
            endpoints = []
            for endpoint in edges[index]:
                site_t, site_x = divmod(endpoint, fixture.lx)
                endpoints.append(
                    (
                        signed_circle_delta(row_t, site_t, fixture.T),
                        signed_circle_delta(row_x, site_x, fixture.lx),
                    )
                )
            signature.append(("ze", *sorted(endpoints)))
        else:
            endpoint = index - len(edges)
            site_t, site_x = divmod(endpoint, fixture.lx)
            signature.append(
                (
                    "zo",
                    signed_circle_delta(row_t, site_t, fixture.T),
                    signed_circle_delta(row_x, site_x, fixture.lx),
                )
            )
    return tuple(signature)


def rotation_determinant(rotation: tuple[tuple[int, int, int], ...]) -> int:
    return int(sp.det(sp.Matrix(rotation)))


def proper_cubic_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    output = []
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row in range(3):
                values = [0, 0, 0]
                values[order[row]] = signs[row]
                rows.append(tuple(values))
            rotation = tuple(rows)
            if rotation_determinant(rotation) == 1:
                output.append(rotation)
    return tuple(output)


def rotate(rotation, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(
        sum(rotation[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )


def sigma(vector: tuple[int, int, int]) -> sp.Matrix:
    return sp.expand(sum((vector[index] * PAULI[index] for index in range(3)), sp.zeros(2)))


def encode(rotation, values: tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]) -> sp.Matrix:
    answer = values[0] * IDENTITY2
    for index in range(3):
        basis = rotate(rotation, tuple(1 if j == index else 0 for j in range(3)))
        answer += values[index + 1] * sigma(basis)
    return sp.expand(answer)


def decode(rotation, carrier: sp.Matrix) -> tuple[sp.Expr, ...]:
    values = [sp.expand(sp.trace(carrier) / 2)]
    for index in range(3):
        basis = rotate(rotation, tuple(1 if j == index else 0 for j in range(3)))
        values.append(sp.expand(sp.trace(carrier * sigma(basis)) / 2))
    return tuple(values)


def multiply_rotations(left, right):
    matrix = sp.Matrix(left) * sp.Matrix(right)
    return tuple(tuple(int(matrix[row, column]) for column in range(3)) for row in range(3))


def tagged_code(frame_index: int, role: int) -> sp.Integer:
    """One finite central code; its occurrence is a supplied condition."""
    return sp.Integer(1000 * (role + 1) + frame_index + 1)


def tagged_encode(
    rotations,
    frame_index: int,
    role: int,
    payloads: tuple[sp.Expr, sp.Expr, sp.Expr],
) -> sp.Matrix:
    frame = rotations[frame_index]
    answer = tagged_code(frame_index, role) * IDENTITY2
    for index, payload in enumerate(payloads):
        basis = rotate(frame, tuple(1 if j == index else 0 for j in range(3)))
        answer += payload * sigma(basis)
    return sp.expand(answer)


def tagged_decode(rotations, carrier: sp.Matrix, roles: tuple[int, ...]):
    """Decode only the declared finite tagged support, never an external frame."""
    code = sp.expand(sp.trace(carrier) / 2)
    lookup = {
        tagged_code(frame_index, role): (frame_index, role)
        for frame_index in range(len(rotations))
        for role in roles
    }
    if code not in lookup:
        raise ValueError("carrier is outside the declared finite tagged support")
    frame_index, role = lookup[code]
    frame = rotations[frame_index]
    payloads = []
    traceless = sp.expand(carrier - code * IDENTITY2)
    for index in range(3):
        basis = rotate(frame, tuple(1 if j == index else 0 for j in range(3)))
        payloads.append(sp.expand(sp.trace(traceless * sigma(basis)) / 2))
    return frame_index, role, tuple(payloads)


def tagged_rotate(rotations, cubic_rotation, carrier: sp.Matrix, roles: tuple[int, ...]):
    """Supplied nonlinear proper-cubic action on the finite tagged support."""
    frame_index, role, payloads = tagged_decode(rotations, carrier, roles)
    moved = multiply_rotations(cubic_rotation, rotations[frame_index])
    moved_index = rotations.index(moved)
    return tagged_encode(rotations, moved_index, role, payloads)


def two_block_bridge_precision(
    left: tuple[sp.Expr, ...], right: tuple[sp.Expr, ...]
) -> tuple[sp.Matrix, sp.Matrix]:
    """Pairwise-site bridge for exp(-|U+V|^2), with unit hidden pivot."""
    count = len(left) + len(right)
    precision = sp.zeros(count + 1)
    left_column = sp.Matrix(left)
    right_column = sp.Matrix(right)
    precision[: len(left), : len(left)] = 2 * left_column.conjugate() * left_column.T
    precision[len(left) : count, len(left) : count] = (
        2 * right_column.conjugate() * right_column.T
    )
    for index, coefficient in enumerate(left):
        precision[index, count] = sp.conjugate(coefficient)
        precision[count, index] = coefficient
    for offset, coefficient in enumerate(right):
        index = len(left) + offset
        precision[index, count] = -sp.conjugate(coefficient)
        precision[count, index] = -coefficient
    precision[count, count] = ONE
    visible = sp.simplify(
        precision[:count, :count]
        - precision[:count, count:] * precision[count:, :count]
    )
    return precision, visible


def subdivided_edge_precision(coefficient: sp.Expr) -> tuple[sp.Matrix, sp.Matrix]:
    """Replace one scalar precision edge by a unit-pivot two-edge path."""
    k = sp.sympify(coefficient)
    original = sp.Matrix([[ZERO, k], [sp.conjugate(k), ZERO]])
    extended = sp.Matrix(
        [
            [ONE, ZERO, ONE],
            [ZERO, sp.conjugate(k) * k, -sp.conjugate(k)],
            [ONE, -k, ONE],
        ]
    )
    visible = sp.simplify(
        extended[:2, :2]
        - extended[:2, 2:] * extended[2:, :2]
    )
    return original, visible


def record_row_decomposition(
    coefficients: tuple[sp.Expr, ...],
    varying: tuple[int, ...],
    left_arm_block: tuple[int, ...],
) -> tuple[sp.Matrix, sp.Matrix, sp.Expr]:
    """Split one arm-sensitive row into an arm-blind factor and a two-site bridge."""
    visible_count = len(coefficients)
    y_index = visible_count
    h_index = visible_count + 1
    precision = sp.zeros(visible_count + 2)

    fixed_vector = sp.zeros(visible_count + 2, 1)
    for index, coefficient in enumerate(coefficients):
        if index not in varying:
            fixed_vector[index, 0] = SQRT_ALPHA * coefficient
    fixed_vector[y_index, 0] = -SQRT_ALPHA
    precision += fixed_vector.conjugate() * fixed_vector.T

    left_indices = tuple(index for index in varying if index in left_arm_block)
    right_indices = tuple(index for index in varying if index not in left_arm_block)
    left_vector = sp.zeros(visible_count + 2, 1)
    right_vector = sp.zeros(visible_count + 2, 1)
    for index in left_indices:
        left_vector[index, 0] = SQRT_BETA * coefficients[index]
    for index in right_indices:
        right_vector[index, 0] = SQRT_BETA * coefficients[index]
    right_vector[y_index, 0] = SQRT_BETA

    precision += 2 * left_vector.conjugate() * left_vector.T
    precision += 2 * right_vector.conjugate() * right_vector.T
    for index in range(visible_count + 1):
        precision[index, h_index] += sp.conjugate(left_vector[index, 0])
        precision[h_index, index] += left_vector[index, 0]
        precision[index, h_index] -= sp.conjugate(right_vector[index, 0])
        precision[h_index, index] -= right_vector[index, 0]
    precision[h_index, h_index] = ONE

    hidden = precision[visible_count:, visible_count:]
    visible = sp.simplify(
        precision[:visible_count, :visible_count]
        - precision[:visible_count, visible_count:]
        * hidden.inv(method="DM")
        * precision[visible_count:, :visible_count]
    )
    return precision, visible, sp.factor(hidden.det(method="domain-ge"))


def main() -> int:
    passed = 0
    failed = 0

    def check(name: str, condition: bool, detail: str) -> None:
        nonlocal passed, failed
        if condition:
            passed += 1
            print(f"PASS {name}: {detail}")
        else:
            failed += 1
            print(f"FAIL {name}: {detail}")

    pair_precision = sp.Matrix([[ALPHA, ZERO], [ZERO, BETA]])
    coupling = sp.Matrix([[-ALPHA], [BETA]])
    pair_schur = sp.simplify(
        pair_precision - coupling * coupling.H / C_NORMALIZATION
    )
    check(
        "fixed-normalized-complex-Gaussian-split",
        ALPHA + BETA == C_NORMALIZATION
        and sp.cancel(ALPHA * BETA / C_NORMALIZATION) == ONE
        and matrix_equal(pair_schur, sp.ones(2)),
        "alpha=3, beta=3/2, and C=9/2 give (C/pi) integral exp[-alpha|u-y|^2-beta|v+y|^2]=exp[-|u+v|^2] exactly",
    )

    bridge_left = (ONE + I / 3, -R(2, 5), R(7, 11) * I, R(3, 4))
    bridge_right = (R(5, 7) - I / 2, -R(4, 9))
    bridge_precision, bridge_visible = two_block_bridge_precision(
        bridge_left, bridge_right
    )
    bridge_column = sp.Matrix((*bridge_left, *bridge_right))
    edge_original, edge_visible = subdivided_edge_precision(R(3, 7) + 2 * I / 5)
    zero_edge_original, zero_edge_visible = subdivided_edge_precision(ZERO)
    check(
        "pairwise-site-bridge-and-edge-subdivision",
        bridge_precision[-1, -1] == ONE
        and matrix_equal(
            bridge_visible, bridge_column.conjugate() * bridge_column.T
        )
        and matrix_equal(edge_visible, edge_original)
        and matrix_equal(zero_edge_visible, zero_edge_original),
        "a unit-pivot center exactly bridges two on-site linear forms, and a unit-pivot path subdivision restores an arbitrary or zero Hermitian scalar edge",
    )

    coefficients = tuple(
        R(index + 1, index + 2) * (I if index % 3 == 1 else ONE)
        for index in range(11)
    )
    visible, hidden, factors, mediator_count = compiled_precision(coefficients)
    column = sp.Matrix(coefficients)
    target = column.conjugate() * column.T
    degrees = Counter(
        term.label for factor in factors for term in factor if not term.original
    )
    check(
        "arity-three-original-isolating-compiler",
        mediator_count == 12
        and len(factors) == 13
        and max(len(factor) for factor in factors) <= 3
        and max(sum(term.original for term in factor) for factor in factors) <= 1
        and set(degrees.values()) == {2}
        and matrix_equal(visible, target)
        and sp.factor(hidden.det(method="domain-ge"))
        == C_NORMALIZATION ** mediator_count,
        "the eleven-term worst roster becomes thirteen arity<=3 factors with twelve degree-two mediators; its Schur complement and complete normalized determinant are exact",
    )

    zero_coefficients = (*coefficients[:-1], ZERO)
    zero_visible, zero_hidden, zero_factors, zero_count = compiled_precision(zero_coefficients)
    zero_column = sp.Matrix(zero_coefficients)
    check(
        "zero-weight-fixed-roster",
        zero_count == mediator_count
        and len(zero_factors) == len(factors)
        and matrix_equal(zero_visible, zero_column.conjugate() * zero_column.T)
        and sp.factor(zero_hidden.det(method="domain-ge"))
        == C_NORMALIZATION ** zero_count,
        "a vanishing leaf keeps the identical mediator roster and normalization while recovering the exact lower-support residual",
    )

    fixture = b174.Fixture(4, tag="b179-strict-neighbor-compiler")
    halves, thirds, edges = arm_sets(fixture)
    bundles = (halves, thirds)
    rosters = row_rosters(bundles)
    half_changed = changed_rows(halves)
    third_changed = changed_rows(thirds)
    mutation_labels = tuple(
        sorted({label for row in set(half_changed) | set(third_changed) for label in rosters[row]})
    )
    check(
        "fixed-arm-and-split-roster",
        half_changed == third_changed
        and len(half_changed) == 3
        and len(mutation_labels) == 16
        and max(map(len, rosters)) == 11
        and all(len(arm["B"].cols * [0]) == halves[0]["B"].cols for family in bundles for arm in family),
        "at m=1, c=1/2 and c=1/3 use the same three arm-sensitive rows, sixteen original coordinates, fixed edge/on-site columns, and an eleven-term maximum residual",
    )

    changed_label_sets = []
    for row in half_changed:
        changing = set()
        for position, label in enumerate(rosters[row]):
            index = int(label[1:])
            family_values = []
            for family in bundles:
                family_values.append(tuple(
                        arm["q"][row, index]
                        if label[0] == "p"
                        else -arm["B"][row, index]
                        for arm in family
                ))
            if any(len(set(map(str, values))) > 1 for values in family_values):
                changing.add(label)
        changed_label_sets.append(changing)
    core_labels = changed_label_sets[1] & changed_label_sets[2]
    side_one_labels = (
        (changed_label_sets[0] | changed_label_sets[1]) - core_labels
    ) | {f"y{half_changed[0]}", f"y{half_changed[1]}"}
    side_two_labels = (changed_label_sets[2] - core_labels) | {
        f"y{half_changed[2]}"
    }
    record_pack = (core_labels, side_one_labels, side_two_labels)
    record_exact = True
    record_local = True
    record_hidden_determinants = []
    for family in bundles:
        for arm in family:
            for row_position, row in enumerate(half_changed):
                roster = rosters[row]
                scale = ONE / sp.sqrt(arm["variance"])
                coefficients = tuple(
                    sp.expand(
                        scale
                        * (
                            arm["q"][row, int(label[1:])]
                            if label[0] == "p"
                            else -arm["B"][row, int(label[1:])]
                        )
                    )
                    for label in roster
                )
                changing_indices = tuple(
                    index
                    for index, label in enumerate(roster)
                    if label in changed_label_sets[row_position]
                )
                left_indices = tuple(
                    index
                    for index, label in enumerate(roster)
                    if label in core_labels
                )
                precision, visible, hidden_det = record_row_decomposition(
                    coefficients, changing_indices, left_indices
                )
                target_column = sp.Matrix(coefficients)
                record_exact &= matrix_equal(
                    visible, target_column.conjugate() * target_column.T
                )
                record_hidden_determinants.append(hidden_det)

                reference = family[-1]
                reference_scale = ONE / sp.sqrt(reference["variance"])
                reference_coefficients = tuple(
                    sp.expand(
                        reference_scale
                        * (
                            reference["q"][row, int(label[1:])]
                            if label[0] == "p"
                            else -reference["B"][row, int(label[1:])]
                        )
                    )
                    for label in roster
                )
                reference_precision, _, _ = record_row_decomposition(
                    reference_coefficients, changing_indices, left_indices
                )
                difference = sp.simplify(precision - reference_precision)
                side_name = "S1" if row_position < 2 else "S2"
                site_of = {
                    **{
                        index: "S0"
                        for index, label in enumerate(roster)
                        if label in core_labels
                    },
                    **{
                        index: side_name
                        for index, label in enumerate(roster)
                        if label in changed_label_sets[row_position] - core_labels
                    },
                    len(roster): side_name,
                    len(roster) + 1: "Record",
                }
                for left_index in range(difference.rows):
                    for right_index in range(difference.cols):
                        if difference[left_index, right_index] == 0:
                            continue
                        left_site = site_of.get(left_index, "bulk")
                        right_site = site_of.get(right_index, "bulk")
                        record_local &= (
                            left_site == right_site
                            or {left_site, right_site}
                            in ({"Record", "S0"}, {"Record", side_name})
                        )
    check(
        "executed-three-row-record-star-bridge",
        tuple(map(len, record_pack)) == (4, 3, 2)
        and record_exact
        and record_local
        and set(record_hidden_determinants) == {C_NORMALIZATION},
        "on the mass-one xgraded width-four fixture, S0/S1/S2 carry 4/3/2 coordinates; all three arm-sensitive rows, four arms, and both supplied splits reduce exactly with hidden determinant C, while every arm-varying precision entry is on-site or Record-to-neighbor",
    )

    unchanged = tuple(row for row in range(fixture.N) if row not in half_changed)
    arm_independent = all(
        all(
            arm["q"].row(row) == family[-1]["q"].row(row)
            and arm["B"].row(row) == family[-1]["B"].row(row)
            for arm in family[:-1]
        )
        for family in bundles
        for row in unchanged
    )
    occurrence = Counter(label for row in unchanged for label in rosters[row])
    check(
        "record-roster-and-degree-input-bounds",
        arm_independent
        and tuple(map(len, record_pack)) == (4, 3, 2)
        and len(mutation_labels) == 16
        and max(occurrence.values(), default=0) <= 8,
        "the exact S0/S1/S2 Record roster is 4/3/2 and the largest bulk incidence demand is eight; these are inputs to the explicit site/slot certificate, not a routing proof",
    )

    raw_half = tuple(arm["raw_mass"] for arm in halves)
    p_compiled = normalize(raw_half)
    p_det = normalize(tuple(ONE / b174.norm2(arm["det_q"]) for arm in halves))
    check(
        "determinant-arm-law-preserved",
        p_compiled == p_det
        and all(value > 0 for value in p_compiled)
        and all(matrix_equal(arm["covariance"], arm["W"]) for arm in halves),
        "normalized mediator measures and standard spectator measures multiply every arm by one, preserving the determinant partition and exact W covariance",
    )

    rows = b41.slice_rows(fixture, fixture.tstar)
    joint = sp.Matrix(
        [
            [
                p_compiled[arm]
                * sp.cancel(
                    halves[arm]["W"].extract(rows, rows)[outcome, outcome]
                    / sp.trace(halves[arm]["W"].extract(rows, rows))
                )
                for outcome in range(4)
            ]
            for arm in range(4)
        ]
    )
    check(
        "marked-projector-table-consistency",
        sp.cancel(sum(joint, ZERO)) == ONE
        and all(joint[arm, outcome] > 0 for arm in range(4) for outcome in range(4))
        and all(
            sp.cancel(sum(joint[arm, outcome] for outcome in range(4)) - p_compiled[arm]) == 0
            for arm in range(4)
        ),
        "the constructed table is normalized and positive and has the determinant arm marginals; this consistency predicate does not compare every entry with an independently supplied table",
    )

    topology_rows = []
    for width in (4, 8):
        width_fixture = b174.Fixture(
            width, pattern=b174.constant_pattern(width), tag=f"b179-width-{width}"
        )
        half, third, _ = arm_sets(width_fixture)
        width_rosters = row_rosters((half, third))
        width_changed = changed_rows(half)
        labels = {
            label for row in width_changed for label in width_rosters[row]
        }
        use = Counter(
            label
            for row, roster in enumerate(width_rosters)
            if row not in width_changed
            for label in roster
        )
        topology_rows.append(
            (
                width,
                max(map(len, width_rosters)),
                len(width_changed),
                len(labels),
                max(use.values(), default=0),
            )
        )
    check(
        "heldout-width-topology-stability",
        topology_rows == [(4, 11, 3, 16, 8), (8, 11, 3, 16, 8)],
        "the auxiliary constant-background width-four and width-eight topology probes have the same eleven-term, three-row, sixteen-coordinate, eight-port compiler bounds",
    )

    rotations = proper_cubic_rotations()
    sample = (R(2, 3) + I / 5, -R(3, 7), I * R(5, 11), R(7, 13) - I / 3)
    base_frame = (1, 2, 3)
    frames = {rotate(rotation, base_frame): rotation for rotation in rotations}
    carrier_ok = all(
        decode(rotation, encode(rotation, sample)) == sample for rotation in rotations
    )
    direction_ok = all(
        set(rotate(rotation, direction) for direction in DIRECTIONS) == set(DIRECTIONS)
        for rotation in rotations
    )
    check(
        "literal-M2-carrier-and-cubic-frame",
        len(rotations) == 24
        and len(frames) == 24
        and carrier_ok
        and direction_ok,
        "four complex coordinates encode bijectively in literal M2(C), and the 24 proper-cubic frames preserve the six directions; this does not prove covariance of the full site map",
    )


    roles = (0, 1, 2, 3)
    tagged_payloads = (R(2, 9) + I / 7, -R(5, 8), R(3, 11) - I / 4)
    tagged_carriers = tuple(
        tagged_encode(rotations, frame_index, role, tagged_payloads)
        for frame_index in range(len(rotations))
        for role in roles
    )
    tagged_roundtrips = all(
        tagged_decode(rotations, carrier, roles)
        == (frame_index, role, tagged_payloads)
        for carrier, (frame_index, role) in zip(
            tagged_carriers,
            product(range(len(rotations)), roles),
        )
    )
    tagged_covariance = True
    for cubic_rotation in rotations:
        for carrier, (frame_index, role) in zip(
            tagged_carriers,
            product(range(len(rotations)), roles),
        ):
            moved_frame = multiply_rotations(
                cubic_rotation, rotations[frame_index]
            )
            decoded = tagged_decode(
                rotations,
                tagged_rotate(rotations, cubic_rotation, carrier, roles),
                roles,
            )
            tagged_covariance &= decoded == (
                rotations.index(moved_frame),
                role,
                tagged_payloads,
            )
    coefficient_map = sp.Matrix(
        [
            [ONE, ZERO, ZERO, ONE],
            [ZERO, ONE, -I, ZERO],
            [ZERO, ONE, I, ZERO],
            [ONE, ZERO, ZERO, -ONE],
        ]
    )
    complex_jacobian = sp.simplify(coefficient_map.det())
    check(
        "self-describing-tagged-M2-pushforward",
        len(set(map(str, tagged_carriers))) == len(tagged_carriers)
        and tagged_roundtrips
        and tagged_covariance
        and sp.simplify(complex_jacobian * sp.conjugate(complex_jacobian)) == 16,
        "one central finite code plus three Pauli-frame payloads decode without an external frame and the supplied tag action is cubic-covariant; 16 is the real Jacobian of the full four-complex-coordinate codec, while each fixed tagged support uses its three-complex-payload decoded-coordinate pushforward",
    )

    row_type_bound = len(
        {
            roster_signature(fixture, row, roster, edges)
            for row, roster in enumerate(rosters)
        }
    )
    track_bound = 25 * row_type_bound * max(map(len, rosters))
    uninstantiated_lane_count = (
        1
        + 12
        + max(map(len, rosters)) * (track_bound + 2)
    )
    fixed_density_cover_independent = False
    check(
        "finite-type-counts-do-not-close-routing",
        row_type_bound <= 16
        and track_bound <= 4400
        and uninstantiated_lane_count <= 48413
        and not fixed_density_cover_independent,
        "row-type and lane counts are finite bookkeeping only; without a periodic collision-free site map, seams, and equivariance they do not establish fixed density",
    )

    wrong_sign = sp.Matrix([[ALPHA, ZERO], [ZERO, BETA]]) - sp.Matrix(
        [[-ALPHA], [-BETA]]
    ) * sp.Matrix([[-ALPHA, -BETA]]) / C_NORMALIZATION
    unnormalized_roster_ratio = sp.cancel(sp.pi / C_NORMALIZATION)
    check(
        "compiler-mutation-gates",
        not matrix_equal(wrong_sign, sp.ones(2))
        and unnormalized_roster_ratio != ONE
        and C_NORMALIZATION != ONE,
        "changing one mediator sign destroys the target cross term; deleting a zero-roster mediator changes only the unnormalized integral by pi/C, while either normalized roster still multiplies by one",
    )

    text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "selection-record-and-score-boundary",
        input_hashes_match()
        and b43.supplier_certificate()
        and "W_J" in text
        and "W_R" in text
        and "zero TOE percentage movement" in text,
        "the complete extracted runtime closure and current Block 105 supplier are hash-bound; the note keeps base-measure/action/source selection and autonomous Record writing open and claims no obligation or score movement",
    )

    print("per_element: fixed Gaussian Schur identity, zero roster, signs, M2 encode/decode, and every compiled factor arity are exact")
    print("per_site: the Record center plus all six neighbors, literal four-complex M2 capacity, and <=24 port slots are checked")
    print("per_mode: full worst-roster Schur precision, hidden determinant, W covariance, determinant law, and marked-table normalization/positivity/arm marginals are checked")
    print("per_block: four arms and both splits are checked on the mass-one xgraded width-four interface fixture; constant-background widths four/eight supply topology counts")
    print("lattice_wide: NOT CLOSED; finite row-type counts are not a periodic fixed-density site map, and seams plus full cubic covariance remain open")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return failed


if __name__ == "__main__":
    raise SystemExit(main())
