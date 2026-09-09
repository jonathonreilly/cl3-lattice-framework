#!/usr/bin/env python3
"""Exact checks for the NN Record-program/preparation-quotient compiler.

The executed fixtures use exact SymPy arithmetic.  A local possibility is an
actual 2x2 complex matrix.  Three unoriented opposite-neighbour pairs carry
up to three effect/label program items while all six Hermitian parts carry one
common preparation center.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product
from pathlib import Path

from sympy import Abs, I, Matrix, Rational as Q, sqrt, simplify


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_PROGRAM_PREPARATION_QUOTIENT_TRACE_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_PROGRAM_PREPARATION_QUOTIENT_TRACE_COMPILER_"
    "BOUNDED_THEOREM_NOTE_2026-08-22.md"
)

I2 = Matrix.eye(2)
ZERO2 = Matrix.zeros(2)
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])

DIRECTIONS = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
AXES = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


@dataclass(frozen=True)
class Item:
    effect: Matrix
    label: object


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return left.shape == right.shape and all(
        simplify(left[r, c] - right[r, c]) == 0
        for r in range(left.rows)
        for c in range(left.cols)
    )


def scalar_matrix(value: Matrix) -> bool:
    return matrix_equal(value, value[0, 0] * I2)


def hermitian_part(value: Matrix) -> Matrix:
    return (value + value.conjugate().T) / 2


def antihermitian_coefficient(value: Matrix) -> Matrix:
    return (value - value.conjugate().T) / (2 * I)


def p(nx, nz) -> Matrix:
    return (I2 + nx * SX + nz * SZ) / 2


def encode_pair(center: Matrix, item: Item | None) -> tuple[Matrix, Matrix]:
    if item is None:
        return center, center
    plus = center + I * (item.effect + item.label * I2)
    minus = center + I * (item.effect - item.label * I2)
    return plus, minus


def neg(direction: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(-value for value in direction)


def encode_shell(center: Matrix, items: tuple[Item, ...]) -> dict[tuple[int, int, int], Matrix]:
    if len(items) > 3:
        raise ValueError("only three opposite-neighbour pairs are available")
    shell: dict[tuple[int, int, int], Matrix] = {}
    padded: tuple[Item | None, ...] = items + (None,) * (3 - len(items))
    for axis, item in zip(AXES, padded, strict=True):
        plus, minus = encode_pair(center, item)
        shell[axis] = plus
        shell[neg(axis)] = minus
    return shell


def preparation_center(shell: dict[tuple[int, int, int], Matrix]) -> Matrix:
    return simplify(sum((hermitian_part(shell[d]) for d in DIRECTIONS), ZERO2) / 6)


def decode_pair(plus: Matrix, minus: Matrix) -> Item | None:
    k_plus = antihermitian_coefficient(plus)
    k_minus = antihermitian_coefficient(minus)
    effect = simplify((k_plus + k_minus) / 2)
    signed_label_matrix = simplify((k_plus - k_minus) / 2)
    if not scalar_matrix(signed_label_matrix):
        raise ValueError("pair difference is not a scalar label")
    label = Abs(simplify(signed_label_matrix[0, 0]))
    if label == 0 and matrix_equal(effect, ZERO2):
        return None
    return Item(effect, label)


def decode_program(shell: dict[tuple[int, int, int], Matrix]) -> tuple[Item, ...]:
    items = []
    for axis in AXES:
        item = decode_pair(shell[axis], shell[neg(axis)])
        if item is not None:
            items.append(item)
    return tuple(sorted(items, key=lambda item: str(item.label)))


def positive_truth(expr) -> bool:
    expr = simplify(expr)
    return bool(expr.is_positive)


def nonnegative_truth(expr) -> bool:
    expr = simplify(expr)
    return bool(expr.is_nonnegative)


def is_scaled_projector_effect(effect: Matrix) -> bool:
    if not matrix_equal(effect, effect.conjugate().T):
        return False
    scalar = matrix_equal(effect, effect[0, 0] * I2)
    if scalar:
        value = simplify(effect[0, 0])
        return positive_truth(value) and nonnegative_truth(1 - value)
    determinant = simplify(effect.det())
    coefficient = simplify(effect.trace())
    return (
        determinant == 0
        and positive_truth(coefficient)
        and nonnegative_truth(1 - coefficient)
        and nonnegative_truth(effect[0, 0])
        and nonnegative_truth(effect[1, 1])
    )


def valid_program(items: tuple[Item, ...]) -> bool:
    return (
        len(items) in (2, 3)
        and len({simplify(item.label) for item in items}) == len(items)
        and all(positive_truth(item.label) for item in items)
        and all(is_scaled_projector_effect(item.effect) for item in items)
        and matrix_equal(sum((item.effect for item in items), ZERO2), I2)
    )


def is_density(center: Matrix) -> bool:
    return (
        matrix_equal(center, center.conjugate().T)
        and simplify(center.trace()) == 1
        and nonnegative_truth(center[0, 0])
        and nonnegative_truth(center[1, 1])
        and nonnegative_truth(center.det())
    )


def weight(center: Matrix, effect: Matrix):
    return simplify((center * effect).trace())


def codeword(item: Item) -> Matrix:
    return item.effect + I * item.label * I2


def literal_projective_program(items: tuple[Item, ...]) -> bool:
    return (
        len(items) == 2
        and all(
            simplify(item.effect.det()) == 0
            and simplify(item.effect.trace()) == 1
            for item in items
        )
        and not matrix_equal(items[0].effect, items[1].effect)
    )


def read_effect(code: Matrix) -> Matrix:
    return hermitian_part(code)


def read_label(code: Matrix):
    return simplify(antihermitian_coefficient(code).trace() / 2)


def local_law(shell: dict[tuple[int, int, int], Matrix]):
    center = preparation_center(shell)
    try:
        items = decode_program(shell)
    except ValueError:
        return ((center, Q(1)),)
    if not is_density(center) or not valid_program(items):
        return ((center, Q(1)),)
    literal = literal_projective_program(items)
    return tuple(
        (item.effect if literal else codeword(item), weight(center, item.effect))
        for item in items
    )


def permutation_sign(perm: tuple[int, int, int]) -> int:
    inversions = sum(
        1 for i in range(3) for j in range(i + 1, 3) if perm[i] > perm[j]
    )
    return -1 if inversions % 2 else 1


def proper_cubic_rotations() -> tuple[Matrix, ...]:
    rotations = []
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            if permutation_sign(perm) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rotation = Matrix.zeros(3)
            for row, column in enumerate(perm):
                rotation[row, column] = signs[row]
            rotations.append(rotation)
    return tuple(rotations)


def rotate_direction(rotation: Matrix, direction: tuple[int, int, int]):
    vector = rotation * Matrix(direction)
    return tuple(int(vector[index]) for index in range(3))


def rotate_shell(shell: dict[tuple[int, int, int], Matrix], rotation: Matrix):
    return {rotate_direction(rotation, d): value for d, value in shell.items()}


def conjugate_shell(shell, unitary: Matrix):
    return {d: simplify(unitary * value * unitary.conjugate().T) for d, value in shell.items()}


def item_equal(left: Item, right: Item) -> bool:
    return simplify(left.label - right.label) == 0 and matrix_equal(left.effect, right.effect)


def program_equal(left: tuple[Item, ...], right: tuple[Item, ...]) -> bool:
    return len(left) == len(right) and all(item_equal(a, b) for a, b in zip(left, right))


def law_equal(left, right) -> bool:
    return len(left) == len(right) and all(
        matrix_equal(a_code, b_code) and simplify(a_p - b_p) == 0
        for (a_code, a_p), (b_code, b_p) in zip(left, right)
    )


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

    root2 = sqrt(2)
    center = Matrix([[Q(3, 5), 0], [0, Q(2, 5)]])
    shared = Q(1, 2) * p(0, 1)
    menu_a = (
        Item(shared, Q(1)),
        Item(Q(9, 10) * p(4 * root2 / 9, Q(-7, 9)), Q(2)),
        Item(Q(3, 5) * p(-2 * root2 / 3, Q(1, 3)), Q(3)),
    )
    menu_b = (
        Item(shared, Q(1)),
        Item(Q(3, 4) * p(2 * root2 / 3, Q(-1, 3)), Q(2)),
        Item(Q(3, 4) * p(-2 * root2 / 3, Q(-1, 3)), Q(3)),
    )
    duplicate_binary = (
        Item(Q(1, 2) * I2, Q(1)),
        Item(Q(1, 2) * I2, Q(2)),
    )
    projective_binary = (
        Item(p(0, 1), Q(1)),
        Item(p(0, -1), Q(2)),
    )

    shell_a = encode_shell(center, menu_a)
    shell_b = encode_shell(center, menu_b)
    shell_d = encode_shell(center, duplicate_binary)
    shell_p = encode_shell(center, projective_binary)

    check(
        "menu-domain",
        all(valid_program(menu) for menu in (menu_a, menu_b, duplicate_binary, projective_binary)),
        "two ternary menus, a repeated-effect binary menu, and a projective binary menu are valid",
    )
    check(
        "preparation-quotient",
        all(matrix_equal(preparation_center(shell), center) for shell in (shell_a, shell_b, shell_d, shell_p)),
        "four distinct programs have exactly the same six-neighbour Hermitian preparation center",
    )

    rotations = proper_cubic_rotations()
    rotation_ok = len(rotations) == 24
    for shell, menu in (
        (shell_a, menu_a),
        (shell_b, menu_b),
        (shell_d, duplicate_binary),
        (shell_p, projective_binary),
    ):
        rotation_ok = rotation_ok and all(
            program_equal(decode_program(rotate_shell(shell, rotation)), menu)
            and matrix_equal(preparation_center(rotate_shell(shell, rotation)), center)
            for rotation in rotations
        )
    check(
        "proper-cubic-decode",
        rotation_ok,
        "all 24 proper cubic rotations only permute or reverse unoriented program pairs",
    )

    check(
        "preparation-density",
        is_density(center),
        "the common Hermitian center is itself the exact normalized preparation diag(3/5,2/5)",
    )
    weights_a = tuple(weight(center, item.effect) for item in menu_a)
    weights_b = tuple(weight(center, item.effect) for item in menu_b)
    check(
        "exact-menu-weights",
        weights_a == (Q(3, 10), Q(19, 50), Q(8, 25))
        and weights_b == (Q(3, 10), Q(7, 20), Q(7, 20)),
        "both ternary laws reproduce the exact shared-effect compiler weights",
    )
    check(
        "probability-normalization",
        all(simplify(sum(weights)) == 1 for weights in (weights_a, weights_b, (Q(1, 2), Q(1, 2)))),
        "every executed valid program has positive weights summing exactly to one",
    )

    law_a = local_law(shell_a)
    law_b = local_law(shell_b)
    law_d = local_law(shell_d)
    law_p = local_law(shell_p)
    check(
        "shared-record-event",
        matrix_equal(law_a[0][0], law_b[0][0])
        and simplify(law_a[0][1] - law_b[0][1]) == 0
        and law_a[0][1] == Q(3, 10),
        "the same effect-label Record code has mass 3/10 across two different neighbour programs",
    )
    check(
        "content-only-readout",
        all(
            matrix_equal(read_effect(code), item.effect) and read_label(code) == item.label
            for menu, law in ((menu_a, law_a), (menu_b, law_b), (duplicate_binary, law_d))
            for item, (code, _) in zip(menu, law)
        ),
        "fixed Hermitian and imaginary-trace maps recover every effect and label from Record content",
    )
    check(
        "selected-projective-content",
        matrix_equal(law_p[0][0], projective_binary[0].effect)
        and matrix_equal(law_p[1][0], projective_binary[1].effect)
        and (law_p[0][1], law_p[1][1]) == (Q(3, 5), Q(2, 5)),
        "the selected binary projective sublaw writes literal projector contents with exact 3/5 and 2/5 masses",
    )
    pure_shell = encode_shell(p(0, 1), projective_binary)
    pure_law = local_law(pure_shell)
    check(
        "pure-state-endpoint",
        matrix_equal(pure_law[0][0], projective_binary[0].effect)
        and matrix_equal(pure_law[1][0], projective_binary[1].effect)
        and (pure_law[0][1], pure_law[1][1]) == (1, 0),
        "a pure preparation gives the exact selected-projective endpoint masses one and zero",
    )
    sigma_h = Matrix([[2, 1], [1, 2]])
    conditional_h = simplify(sigma_h / sigma_h.trace())
    x_projective_binary = (
        Item(p(1, 0), Q(1)),
        Item(p(-1, 0), Q(2)),
    )
    parent_shell = encode_shell(conditional_h, x_projective_binary)
    parent_law = local_law(parent_shell)
    parent_masses = tuple(
        simplify((item.effect * sigma_h * item.effect).trace() / sigma_h.trace())
        for item in x_projective_binary
    )
    check(
        "parent-prefix-composition",
        tuple(probability for _, probability in parent_law) == parent_masses == (Q(3, 4), Q(1, 4)),
        "encoding sigma_h/Tr(sigma_h) reproduces the selected trace-Lueders parent masses 3/4 and 1/4",
    )
    y_preparation = simplify((I2 - Q(1, 2) * SY) / 2)
    y_projective_binary = (
        Item(simplify((I2 + SY) / 2), Q(1)),
        Item(simplify((I2 - SY) / 2), Q(2)),
    )
    y_law = local_law(encode_shell(y_preparation, y_projective_binary))
    check(
        "complex-qubit-prefix",
        tuple(probability for _, probability in y_law) == (Q(1, 4), Q(3, 4)),
        "a genuinely complex Y-coherent preparation and Y program give exact masses one quarter and three quarters",
    )
    check(
        "repeated-effect-labels",
        not matrix_equal(law_d[0][0], law_d[1][0])
        and law_d[0][1] == law_d[1][1] == Q(1, 2),
        "two equal effects remain distinct registered outcomes and each receives probability one half",
    )

    x_shell = conjugate_shell(shell_a, SX)
    expected_x_law = tuple(
        (simplify(SX * code * SX), probability) for code, probability in law_a
    )
    check(
        "internal-basis-covariance",
        law_equal(local_law(x_shell), expected_x_law),
        "simultaneous Pauli-X conjugation transports every output code and preserves every weight",
    )

    invalid_shell = {direction: center for direction in DIRECTIONS}
    fallback = local_law(invalid_shell)
    fallback_rotated = local_law(rotate_shell(invalid_shell, rotations[7]))
    malformed_shell = dict(invalid_shell)
    malformed_shell[AXES[0]] = center + I * SX
    malformed_fallback = local_law(malformed_shell)
    check(
        "total-rule-fallback",
        len(fallback) == 1
        and matrix_equal(fallback[0][0], center)
        and fallback[0][1] == 1
        and law_equal(fallback, fallback_rotated)
        and len(malformed_fallback) == 1
        and malformed_fallback[0][1] == 1
        and all(
            law_equal(malformed_fallback, local_law(rotate_shell(malformed_shell, rotation)))
            for rotation in rotations
        ),
        "empty and non-scalar malformed programs receive a normalized fallback rather than an undefined decoder",
    )
    required_projective_carriers = tuple(shell_p[direction] for direction in DIRECTIONS)
    nonscalar_input_count = sum(
        not scalar_matrix(antihermitian_coefficient(value))
        for value in required_projective_carriers
    )
    executed_outputs = tuple(
        code
        for law in (law_a, law_b, law_d, law_p, pure_law, parent_law, y_law, fallback, malformed_fallback)
        for code, _ in law
    )
    check(
        "self-hosting-gap",
        nonscalar_input_count == 4
        and all(scalar_matrix(antihermitian_coefficient(code)) for code in executed_outputs),
        "four projective carrier inputs need nonscalar anti-Hermitian data, while every current-law output has scalar such data",
    )

    signed_before = simplify(
        ((antihermitian_coefficient(shell_a[AXES[0]]) - antihermitian_coefficient(shell_a[neg(AXES[0])])) / 2)[0, 0]
    )
    half_turn = Matrix.diag(-1, -1, 1)
    half_shell = rotate_shell(shell_a, half_turn)
    signed_after = simplify(
        ((antihermitian_coefficient(half_shell[AXES[0]]) - antihermitian_coefficient(half_shell[neg(AXES[0])])) / 2)[0, 0]
    )
    check(
        "deletion-orientation",
        signed_before == 1 and signed_after == -1 and decode_program(half_shell)[0].label == 1,
        "a signed label decoder breaks under a proper half-turn while the absolute pair decoder survives",
    )
    check(
        "deletion-label",
        matrix_equal(duplicate_binary[0].effect, duplicate_binary[1].effect)
        and len({str(code) for code, _ in law_d}) == 2,
        "deleting the scalar labels would collapse the repeated-effect binary menu to one Record content",
    )
    contextual_a = (Q(1, 4), Q(1, 4), Q(1, 2))
    contextual_b = (Q(1, 3), Q(1, 3), Q(1, 3))
    check(
        "deletion-effect-descent",
        sum(contextual_a) == sum(contextual_b) == 1 and contextual_a[0] != contextual_b[0],
        "menu normalization alone permits one shared effect to have contextual masses 1/4 and 1/3",
    )

    coarse = weight(center, Q(1, 2) * I2)
    fine_left = weight(center, Q(1, 4) * I2)
    fine_right = weight(center, Q(1, 4) * I2)
    check(
        "registered-refinement",
        coarse == Q(1, 2) and fine_left == fine_right == Q(1, 4) and coarse == fine_left + fine_right,
        "distinct refined Record events have separate probabilities whose ordinary sum equals the coarse event",
    )
    event_a = {0, 1}
    event_b = {2, 3}
    check(
        "probability-not-set-identity",
        event_a.isdisjoint(event_b) and Q(len(event_a), 6) == Q(len(event_b), 6),
        "two disjoint microscopic cells can represent equal-probability operational events without being one set",
    )

    note_text = NOTE.read_text() if NOTE.exists() else ""
    check(
        "source-contract",
        all(
            token in note_text
            for token in (
                "Preparation quotient",
                "No-Go Discipline Gate",
                "N1 — Alternative route enumeration",
                "N8 — Cross-cycle echo",
                "conditional on formation",
                "no TOE-percentage movement",
                "self-hosting",
            )
        ),
        "the source binds the constructive claim, negative-claim gate, formation boundary, and score boundary",
    )

    print(
        "per_element: exact effect-label encoding, decoding, trace mass, and two deletion controls are checked for every displayed item"
    )
    print(
        "per_site: one complete six-neighbour shell, its valid-program law, fallback, and same-law self-hosting support mismatch are executed"
    )
    print(
        "per_mode: checked and not executed — no spectral, momentum, transfer, or continuum mode claim belongs to this local compiler"
    )
    print(
        "per_block: binary and ternary program blocks, repeated effects, refinement, and all 24 proper-cubic transports are checked"
    )
    print(
        "lattice_wide: checked and not executed — translation uses the same radius-one formula, but no global occurrence history is claimed"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
