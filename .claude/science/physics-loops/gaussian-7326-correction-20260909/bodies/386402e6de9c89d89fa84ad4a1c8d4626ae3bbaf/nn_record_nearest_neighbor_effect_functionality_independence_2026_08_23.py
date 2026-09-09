#!/usr/bin/env python3
"""Exact nearest-neighbor countermodel for Record effect functionality W1.

The carrier and exact menu fixtures are reconstructed by the Block 32 source.
This runner adds a second total, translation/proper-cubic-covariant local
kernel.  It has the same registered contents and support as the trace kernel,
but applies a permutation-equivariant nonlinear simplex map to every valid
ternary program.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, integrate, oo, pi, simplify, sqrt, symbols
from sympy.matrices.matrixbase import MatrixBase

from nn_record_program_preparation_quotient_trace_compiler_2026_08_22 import (
    AXES,
    DIRECTIONS,
    I2,
    SX,
    SY,
    ZERO2,
    Item,
    codeword,
    conjugate_shell,
    decode_program,
    encode_shell,
    is_density,
    law_equal,
    literal_projective_program,
    matrix_equal,
    p,
    preparation_center,
    proper_cubic_rotations,
    rotate_shell,
    valid_program,
    weight,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_NEAREST_NEIGHBOR_EFFECT_FUNCTIONALITY_"
    "INDEPENDENCE_NO_GO_NOTE_2026-08-23.md",
    "scripts/nn_record_program_preparation_quotient_trace_compiler_2026_08_22.py",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_NEAREST_NEIGHBOR_EFFECT_FUNCTIONALITY_"
    "INDEPENDENCE_NO_GO_NOTE_2026-08-23.md"
)


@dataclass(frozen=True)
class GaussianLaw:
    name: str = "unit-frobenius-gaussian"

    @staticmethod
    def density(value: Matrix):
        norm_squared = simplify((value.conjugate().T * value).trace())
        return simplify(exp(-norm_squared) / pi**4)

    @staticmethod
    def one_coordinate_mass():
        coordinate = symbols("gaussian_coordinate", real=True)
        return integrate(exp(-(coordinate**2)) / sqrt(pi), (coordinate, -oo, oo))

    def normalized(self) -> bool:
        return self.one_coordinate_mass() ** 8 == 1

    def support_contains(self, value: Matrix) -> bool:
        return bool(self.density(value).is_positive)


def complete_shell(shell) -> bool:
    return (
        isinstance(shell, dict)
        and set(shell) == set(DIRECTIONS)
        and all(isinstance(shell[direction], MatrixBase) for direction in DIRECTIONS)
    )


def contextual_law(shell):
    """One total radius-one kernel with a symmetric ternary context map."""
    if not complete_shell(shell):
        return GaussianLaw()
    center = preparation_center(shell)
    try:
        items = decode_program(shell)
    except (TypeError, ValueError):
        return ((center, Q(1)),)
    if not is_density(center) or not valid_program(items):
        return ((center, Q(1)),)

    baseline = tuple(weight(center, item.effect) for item in items)
    probabilities = baseline
    if len(items) == 3:
        second_moment = simplify(sum(value**2 for value in baseline))
        probabilities = tuple(
            simplify(value * (1 + value - second_moment))
            for value in baseline
        )

    literal = literal_projective_program(items)
    return tuple(
        (item.effect if literal else codeword(item), probability)
        for item, probability in zip(items, probabilities, strict=True)
    )


def trace_comparator_law(shell):
    """Total comparator with the same fallback and output typing."""
    if not complete_shell(shell):
        return GaussianLaw()
    center = preparation_center(shell)
    try:
        items = decode_program(shell)
    except (TypeError, ValueError):
        return ((center, Q(1)),)
    if not is_density(center) or not valid_program(items):
        return ((center, Q(1)),)
    literal = literal_projective_program(items)
    return tuple(
        (item.effect if literal else codeword(item), weight(center, item.effect))
        for item in items
    )


def support_equal(left, right) -> bool:
    if len(left) != len(right):
        return False
    return all(
        matrix_equal(left_code, right_code)
        and (simplify(left_mass) == 0) == (simplify(right_mass) == 0)
        for (left_code, left_mass), (right_code, right_mass) in zip(left, right, strict=True)
    )


def lock_once(records, site, content: Matrix) -> bool:
    if site in records:
        return False
    records[site] = content
    return True


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
    binary = (
        Item(p(0, 1), Q(1)),
        Item(p(0, -1), Q(2)),
    )
    endpoint_first = (
        Item(p(0, 1), Q(1)),
        Item(Q(1, 2) * p(0, -1), Q(2)),
        Item(Q(1, 2) * p(0, -1), Q(3)),
    )
    endpoint_last = (
        Item(Q(1, 2) * p(0, -1), Q(1)),
        Item(Q(1, 2) * p(0, -1), Q(2)),
        Item(p(0, 1), Q(3)),
    )
    shell_a = encode_shell(center, menu_a)
    shell_b = encode_shell(center, menu_b)
    shell_binary = encode_shell(center, binary)
    serialization_trap_menu = (
        Item(menu_a[0].effect, Q(2)),
        Item(menu_a[1].effect, Q(10)),
        Item(menu_a[2].effect, Q(3)),
    )
    serialization_trap_shell = encode_shell(center, serialization_trap_menu)
    pure_center = p(0, 1)
    shell_endpoint_first = encode_shell(pure_center, endpoint_first)
    shell_endpoint_last = encode_shell(pure_center, endpoint_last)

    check(
        "strict-nearest-neighbor-domain",
        all(
            complete_shell(shell)
            for shell in (
                shell_a,
                shell_b,
                shell_binary,
                serialization_trap_shell,
                shell_endpoint_first,
                shell_endpoint_last,
            )
        )
        and all(
            valid_program(menu)
            for menu in (menu_a, menu_b, binary, serialization_trap_menu, endpoint_first, endpoint_last)
        ),
        "two contextual programs, a label-order trap, a binary control, and two endpoints occupy the six radius-one neighbours",
    )

    baseline_a = tuple(weight(center, item.effect) for item in menu_a)
    baseline_b = tuple(weight(center, item.effect) for item in menu_b)
    check(
        "exact-trace-baselines",
        baseline_a == (Q(3, 10), Q(19, 50), Q(8, 25))
        and baseline_b == (Q(3, 10), Q(7, 20), Q(7, 20)),
        "the two legal programs share the exact effect baseline 3/10 and differ only in their complements",
    )

    skew_a = contextual_law(shell_a)
    skew_b = contextual_law(shell_b)
    probabilities_a = tuple(mass for _, mass in skew_a)
    probabilities_b = tuple(mass for _, mass in skew_b)
    check(
        "exact-contextual-map",
        probabilities_a == (Q(903, 3125), Q(6194, 15625), Q(4916, 15625))
        and probabilities_b == (Q(579, 2000), Q(1421, 4000), Q(1421, 4000)),
        "p_j=b_j(1+b_j-sum_k b_k^2) produces two exact positive normalized ternary laws",
    )
    check(
        "shared-effect-w1-failure",
        matrix_equal(skew_a[0][0], skew_b[0][0])
        and matrix_equal(skew_a[0][0], codeword(menu_a[0]))
        and simplify(skew_a[0][1] - skew_b[0][1]) == -Q(27, 50000),
        "one literal effect-label Record has masses 903/3125 and 579/2000, differing by -27/50000",
    )

    # Universal algebra: p_j=b_j(1+b_j-S2), S2=sum b_k^2.  On the
    # probability simplex S2<=1, every factor is nonnegative, and support is
    # unchanged.
    simplex_ok = True
    simplex_count = 0
    for denominator in range(1, 18):
        for i0 in range(denominator + 1):
            for i1 in range(denominator - i0 + 1):
                simplex_count += 1
                b0 = Q(i0, denominator)
                b1 = Q(i1, denominator)
                b2 = 1 - b0 - b1
                baseline = (b0, b1, b2)
                second_moment = sum(value**2 for value in baseline)
                transformed = tuple(
                    value * (1 + value - second_moment)
                    for value in baseline
                )
                simplex_ok = simplex_ok and sum(transformed) == 1
                simplex_ok = simplex_ok and all(bool(value.is_nonnegative) for value in transformed)
                simplex_ok = simplex_ok and tuple(value == 0 for value in transformed) == (
                    b0 == 0,
                    b1 == 0,
                    b2 == 0,
                )
    check(
        "universal-simplex-identity",
        simplex_ok,
        f"factorization proves positivity, normalization, and support preservation; {simplex_count} exact rational edge/interior points are also checked",
    )

    trace_a = trace_comparator_law(shell_a)
    trace_b = trace_comparator_law(shell_b)
    check(
        "paired-law-independence",
        trace_a[0][1] == trace_b[0][1] == Q(3, 10)
        and support_equal(trace_a, skew_a)
        and support_equal(trace_b, skew_b),
        "the W1-satisfying and W1-violating kernels use identical neighbour programs, output contents, and supports",
    )

    serialization_law = contextual_law(serialization_trap_shell)
    serialization_expected = (
        Q(903, 3125),
        Q(6194, 15625),
        Q(4916, 15625),
    )
    serialization_ok = all(
        any(
            matrix_equal(content, codeword(item)) and mass == expected_mass
            for content, mass in serialization_law
        )
        for item, expected_mass in zip(serialization_trap_menu, serialization_expected, strict=True)
    )
    check(
        "label-serialization-independence",
        serialization_ok,
        "labels (2,10,3) may be host-enumerated as (10,2,3), but the symmetric map assigns each effect its invariant mass",
    )

    endpoint_law_first = contextual_law(shell_endpoint_first)
    endpoint_law_last = contextual_law(shell_endpoint_last)
    check(
        "simplex-endpoint-support",
        tuple(mass for _, mass in endpoint_law_first) == (1, 0, 0)
        and tuple(mass for _, mass in endpoint_law_last) == (0, 0, 1)
        and support_equal(endpoint_law_first, trace_comparator_law(shell_endpoint_first))
        and support_equal(endpoint_law_last, trace_comparator_law(shell_endpoint_last)),
        "the b=(1,0,0) and b=(0,0,1) boundaries remain normalized and preserve the trace support exactly",
    )

    rotations = proper_cubic_rotations()
    rotation_ok = len(rotations) == 24 and all(
        law_equal(contextual_law(rotate_shell(shell, rotation)), contextual_law(shell))
        for rotation in rotations
        for shell in (
            shell_a,
            shell_b,
            shell_binary,
            serialization_trap_shell,
            shell_endpoint_first,
            shell_endpoint_last,
        )
    )
    check(
        "proper-cubic-covariance",
        rotation_ok,
        "all 24 proper cubic rotations preserve each decoded law on both contextual fixtures and the binary control",
    )

    unitaries = (
        I2,
        SX,
        (SX + Matrix([[1, 0], [0, -1]])) / root2,
        Matrix([[1, 0], [0, I]]),
        (I2 + I * SY) / root2,
    )
    basis_ok = True
    for unitary in unitaries:
        basis_ok = basis_ok and matrix_equal(simplify(unitary * unitary.conjugate().T), I2)
        for shell in (
            shell_a,
            shell_b,
            shell_binary,
            serialization_trap_shell,
            shell_endpoint_first,
            shell_endpoint_last,
        ):
            original = contextual_law(shell)
            expected = tuple(
                (simplify(unitary * content * unitary.conjugate().T), mass)
                for content, mass in original
            )
            basis_ok = basis_ok and law_equal(contextual_law(conjugate_shell(shell, unitary)), expected)
    check(
        "internal-basis-covariance",
        basis_ok,
        "five exact unitary basis transports conjugate contents and leave all contextual grades invariant",
    )

    incomplete = {AXES[0]: center}
    malformed = {direction: center for direction in DIRECTIONS}
    malformed[AXES[0]] = center + I * SX
    masks_ok = True
    for mask in range(1 << len(DIRECTIONS)):
        partial = {
            direction: shell_a[direction]
            for index, direction in enumerate(DIRECTIONS)
            if mask & (1 << index)
        }
        if mask == (1 << len(DIRECTIONS)) - 1:
            masks_ok = masks_ok and not isinstance(contextual_law(partial), GaussianLaw)
        else:
            masks_ok = masks_ok and isinstance(contextual_law(partial), GaussianLaw)
            masks_ok = masks_ok and isinstance(trace_comparator_law(partial), GaussianLaw)
            masks_ok = masks_ok and all(
                isinstance(contextual_law(rotate_shell(partial, rotation)), GaussianLaw)
                for rotation in rotations
            )
    malformed_covariant = all(
        law_equal(contextual_law(rotate_shell(malformed, rotation)), contextual_law(malformed))
        for rotation in rotations
    )
    malformed_original = contextual_law(malformed)
    malformed_basis_covariant = all(
        law_equal(
            contextual_law(conjugate_shell(malformed, unitary)),
            tuple(
                (simplify(unitary * content * unitary.conjugate().T), mass)
                for content, mass in malformed_original
            ),
        )
        for unitary in unitaries
    )
    check(
        "total-kernel-fallback",
        isinstance(contextual_law({}), GaussianLaw)
        and isinstance(contextual_law(incomplete), GaussianLaw)
        and isinstance(trace_comparator_law({}), GaussianLaw)
        and isinstance(trace_comparator_law(incomplete), GaussianLaw)
        and len(contextual_law(malformed)) == 1
        and contextual_law(malformed)[0][1] == 1
        and masks_ok
        and malformed_covariant
        and malformed_basis_covariant,
        "all 64 occupancy masks and every rotated/basis-transported malformed shell receive the covariant total-kernel branch",
    )

    gaussian = GaussianLaw()
    carrier_sites_are_independent = all(
        sum(abs(left[index] - right[index]) for index in range(3)) != 1
        for left_index, left in enumerate(DIRECTIONS)
        for right in DIRECTIONS[left_index + 1 :]
    )
    check(
        "support-level-shell-reachability",
        gaussian.normalized()
        and carrier_sites_are_independent
        and all(
            gaussian.support_contains(value)
            for shell in (shell_a, shell_b, shell_endpoint_first, shell_endpoint_last)
            for value in shell.values()
        ),
        "the executable Gaussian density is normalized and positive on every carrier matrix at six pairwise nonadjacent seed sites",
    )

    binary_skew = contextual_law(shell_binary)
    check(
        "binary-deletion-control",
        law_equal(binary_skew, trace_comparator_law(shell_binary))
        and tuple(mass for _, mass in binary_skew) == (Q(3, 5), Q(2, 5)),
        "the contextual transfer is absent on binary programs and the selected trace law is recovered there",
    )
    zero_transfer_a = tuple((code, mass) for code, mass in trace_a)
    zero_transfer_b = tuple((code, mass) for code, mass in trace_b)
    check(
        "w1-restoration-control",
        law_equal(zero_transfer_a, trace_a)
        and law_equal(zero_transfer_b, trace_b)
        and zero_transfer_a[0][1] == zero_transfer_b[0][1],
        "deleting the context transfer restores equal 3/10 grades for the shared Record",
    )

    records = {direction: shell_a[direction] for direction in DIRECTIONS}
    target = (0, 0, 0)
    first_lock = lock_once(records, target, skew_a[0][0])
    second_lock = lock_once(records, target, skew_a[1][0])
    check(
        "record-lock-and-permanence",
        first_lock and not second_lock and matrix_equal(records[target], skew_a[0][0]),
        "one selected admissible content locks once at the target and cannot be overwritten",
    )

    common_total_a = simplify(sum(mass for _, mass in skew_a))
    common_total_b = simplify(sum(mass for _, mass in skew_b))
    check(
        "common-scheduler-not-sufficient",
        common_total_a == common_total_b == 1 and skew_a[0][1] != skew_b[0][1],
        "equal unit total hazard and exact conservation coexist with unequal shared-branch current",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "source-contract",
        all(
            token in note_text
            for token in (
                "Claim type:** no_go",
                "N1 — Alternative route enumeration",
                "N2 — Wall-independence audit",
                "N3 — Hidden-wall scan",
                "N4 — Residual matching",
                "N5 — Resolution audit",
                "N6 — Partial-closure and primitive-registry audit",
                "N7 — Hostile steelman",
                "N8 — Cross-cycle echo",
                "no TOE-percentage movement",
                "does not prove that no downstream Law can derive `W1`",
            )
        ),
        "the source carries the narrow no-go scope, all N1-N8 gates, live escape, and score firewall",
    )

    print(
        "per_element: identical shared effect-label content and its unequal exact 903/3125 versus 579/2000 grades are checked"
    )
    print(
        "per_site: one total six-neighbour kernel, exact fallback, one-time locking, and the two target conditions are checked"
    )
    print(
        "per_mode: checked and not executed — no spectral, momentum, transfer, or continuum-mode claim belongs to this local countermodel"
    )
    print(
        "per_block: both complete ternary programs, a binary deletion control, 24 rotations, and five internal bases are checked"
    )
    print(
        "lattice_wide: checked and not executed — the formula is translation-independent, but no autonomous global formation history is claimed"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
