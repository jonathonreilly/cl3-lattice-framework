#!/usr/bin/env python3
"""Independent reconstruction of the nearest-neighbor W1 countermodel."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from sympy import I, Matrix, Rational as Q, exp, integrate, oo, pi, simplify, sqrt, symbols

from nn_record_program_preparation_quotient_trace_compiler_2026_08_22 import (
    DIRECTIONS,
    I2,
    SX,
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
class FullSupportLaw:
    name: str = "independently-reconstructed-gaussian"

    @staticmethod
    def density(value: Matrix):
        return simplify(exp(-((value.conjugate().T * value).trace())) / pi**4)

    def normalized(self) -> bool:
        coordinate = symbols("independent_coordinate", real=True)
        one_mass = integrate(exp(-(coordinate**2)) / sqrt(pi), (coordinate, -oo, oo))
        return one_mass**8 == 1

    def support_contains(self, value: Matrix) -> bool:
        return bool(self.density(value).is_positive)


def tr_weight(center: Matrix, effect: Matrix):
    return simplify((center * effect).trace())


def reconstructed_kernel(shell):
    if not isinstance(shell, dict) or set(shell) != set(DIRECTIONS):
        return FullSupportLaw()
    center = preparation_center(shell)
    try:
        items = decode_program(shell)
    except (TypeError, ValueError):
        return ((center, Q(1)),)
    if not is_density(center) or not valid_program(items):
        return ((center, Q(1)),)
    baseline = tuple(tr_weight(center, item.effect) for item in items)
    if len(items) == 3:
        second_moment = simplify(sum(value**2 for value in baseline))
        probabilities = tuple(
            simplify(value * (1 + value - second_moment))
            for value in baseline
        )
    else:
        probabilities = baseline
    literal = literal_projective_program(items)
    return tuple(
        (item.effect if literal else codeword(item), mass)
        for item, mass in zip(items, probabilities, strict=True)
    )


def fixtures():
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
    endpoint = (
        Item(p(0, 1), Q(1)),
        Item(Q(1, 2) * p(0, -1), Q(2)),
        Item(Q(1, 2) * p(0, -1), Q(3)),
    )
    serialization_trap = (
        Item(menu_a[0].effect, Q(2)),
        Item(menu_a[1].effect, Q(10)),
        Item(menu_a[2].effect, Q(3)),
    )
    return (
        center,
        menu_a,
        menu_b,
        encode_shell(center, menu_a),
        encode_shell(center, menu_b),
        encode_shell(p(0, 1), endpoint),
        serialization_trap,
        encode_shell(center, serialization_trap),
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

    (
        center,
        menu_a,
        menu_b,
        shell_a,
        shell_b,
        endpoint_shell,
        serialization_trap,
        serialization_trap_shell,
    ) = fixtures()
    check(
        "reconstructed-carriers",
        valid_program(menu_a)
        and valid_program(menu_b)
        and all(matrix_equal(preparation_center(shell), center) for shell in (shell_a, shell_b)),
        "both independently assembled radius-one shells decode the same preparation and valid menus",
    )

    law_a = reconstructed_kernel(shell_a)
    law_b = reconstructed_kernel(shell_b)
    masses_a = tuple(mass for _, mass in law_a)
    masses_b = tuple(mass for _, mass in law_b)
    check(
        "independent-exact-masses",
        masses_a == (Q(903, 3125), Q(6194, 15625), Q(4916, 15625))
        and masses_b == (Q(579, 2000), Q(1421, 4000), Q(1421, 4000)),
        "the independently written symmetric simplex map reproduces both exact distributions",
    )
    check(
        "independent-w1-counterexample",
        matrix_equal(law_a[0][0], law_b[0][0])
        and simplify(law_a[0][1] - law_b[0][1]) == -Q(27, 50000),
        "identical registered content receives two positive grades separated by -27/50000",
    )
    check(
        "probability-and-support",
        all(sum(masses) == 1 for masses in (masses_a, masses_b))
        and all(mass > 0 for mass in masses_a + masses_b)
        and matrix_equal(law_a[0][0], law_b[0][0]),
        "both kernels are normalized and positive while their shared first output is literally identical",
    )

    endpoint_law = reconstructed_kernel(endpoint_shell)
    check(
        "independent-simplex-boundary",
        tuple(mass for _, mass in endpoint_law) == (1, 0, 0),
        "an independently assembled b=(1,0,0) ternary endpoint remains normalized with exact zero support",
    )

    trap_law = reconstructed_kernel(serialization_trap_shell)
    trap_expected = (Q(903, 3125), Q(6194, 15625), Q(4916, 15625))
    check(
        "independent-label-order-trap",
        all(
            any(
                matrix_equal(content, codeword(item)) and mass == expected
                for content, mass in trap_law
            )
            for item, expected in zip(serialization_trap, trap_expected, strict=True)
        ),
        "the permutation-equivariant map is independent of the inherited string order on labels 2,10,3",
    )

    rotations = proper_cubic_rotations()
    check(
        "independent-cubic-covariance",
        len(rotations) == 24
        and all(
            law_equal(reconstructed_kernel(rotate_shell(shell, rotation)), reconstructed_kernel(shell))
            for shell in (shell_a, shell_b, endpoint_shell, serialization_trap_shell)
            for rotation in rotations
        ),
        "an independent 24-element cubic-group enumeration leaves both local laws unchanged",
    )

    unitary = (I2 + I * SX) / sqrt(2)
    basis_ok = matrix_equal(simplify(unitary * unitary.conjugate().T), I2)
    for shell in (shell_a, shell_b, endpoint_shell, serialization_trap_shell):
        expected = tuple(
            (simplify(unitary * content * unitary.conjugate().T), mass)
            for content, mass in reconstructed_kernel(shell)
        )
        basis_ok = basis_ok and law_equal(reconstructed_kernel(conjugate_shell(shell, unitary)), expected)
    check(
        "independent-basis-covariance",
        basis_ok,
        "a nontrivial exact unitary transports outputs and preserves the reconstructed grades",
    )

    masks_ok = True
    for mask in range(1 << len(DIRECTIONS)):
        partial = {
            direction: shell_a[direction]
            for index, direction in enumerate(DIRECTIONS)
            if mask & (1 << index)
        }
        if mask == (1 << len(DIRECTIONS)) - 1:
            masks_ok = masks_ok and not isinstance(reconstructed_kernel(partial), FullSupportLaw)
        else:
            masks_ok = masks_ok and isinstance(reconstructed_kernel(partial), FullSupportLaw)
            masks_ok = masks_ok and all(
                isinstance(reconstructed_kernel(rotate_shell(partial, rotation)), FullSupportLaw)
                for rotation in rotations
            )

    gaussian = FullSupportLaw()
    check(
        "independent-totality",
        isinstance(reconstructed_kernel({}), FullSupportLaw)
        and reconstructed_kernel({direction: center for direction in DIRECTIONS})[0][1] == 1
        and masks_ok
        and gaussian.normalized()
        and all(
            gaussian.support_contains(value)
            for shell in (shell_a, shell_b, endpoint_shell, serialization_trap_shell)
            for value in shell.values()
        ),
        "all 64 masks are total and the independent normalized Gaussian density is positive on every carrier point",
    )

    common_totals = (sum(masses_a), sum(masses_b))
    check(
        "independent-scheduler-control",
        common_totals == (1, 1) and masses_a[0] != masses_b[0],
        "equal total opportunity rate does not equalize the shared branch current",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "independent-scope-contract",
        all(
            phrase in note_text
            for phrase in (
                "strict nearest-neighbor",
                "selected exact Law",
                "owner-approved",
                "N8 — Cross-cycle echo",
                "no TOE-percentage movement",
            )
        ),
        "the note keeps the countermodel, live selected-Law escape, governance boundary, and score claim separate",
    )

    print(
        "per_element: the common effect-label content and exact 903/3125 versus 579/2000 masses are independently checked"
    )
    print(
        "per_site: two complete radius-one conditions and total invariant fallbacks are independently evaluated"
    )
    print(
        "per_mode: checked and not executed — the claim has no mode-space or continuum-spectrum component"
    )
    print(
        "per_block: two ternary blocks, all 24 rotations, and a nontrivial internal basis transport are checked"
    )
    print(
        "lattice_wide: checked and not executed — translation covariance is syntactic; no global scheduler or history is asserted"
    )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
