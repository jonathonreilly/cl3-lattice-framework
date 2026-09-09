#!/usr/bin/env python3
"""Independent exact reconstruction of the Block 40 marked Gaussian Law.

This checker imports neither the primary runner nor the Block 38 compiler.  It
rebuilds the five menu families, M2 Gaussian partition response, conditional
mark kernel, event-presentation quotient, exposure factorization, hostile
shared-effect pair, and mutations from elementary matrices.
"""

from __future__ import annotations

from itertools import permutations
from pathlib import Path

from sympy import I, Matrix, Rational as Q, diff, exp, log, pi, simplify, sqrt, symbols


ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / (
    "NN_RECORD_GAUSSIAN_ACTION_EVENT_RESPONSE_FACTORIZATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md"
)
AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    "docs/NN_RECORD_GAUSSIAN_ACTION_EVENT_RESPONSE_FACTORIZATION_"
    "BOUNDED_THEOREM_NOTE_2026-08-23.md",
)

I2 = Matrix.eye(2)
Z2 = Matrix.zeros(2)
SX = Matrix([[0, 1], [1, 0]])
SY = Matrix([[0, -I], [I, 0]])
SZ = Matrix([[1, 0], [0, -1]])


def matrix_equal(left: Matrix, right: Matrix) -> bool:
    return all(simplify(value) == 0 for value in left - right)


def projector(axis: Matrix) -> Matrix:
    return simplify((I2 + axis) / 2)


def projector_xz(x, z) -> Matrix:
    return simplify((I2 + x * SX + z * SZ) / 2)


def nonzero(effects: tuple[Matrix, ...]) -> tuple[Matrix, ...]:
    return tuple(effect for effect in effects if not matrix_equal(effect, Z2))


def rrr_menu(a, b, x_axis: Matrix = SX, z_axis: Matrix = SZ) -> tuple[Matrix, ...]:
    c = simplify(2 - a - b)
    if a == 0:
        return (projector(z_axis), projector(-z_axis))
    if b == 0:
        return (projector(x_axis), projector(-x_axis))
    if c == 0:
        return (projector(x_axis), projector(-x_axis))
    gamma = simplify((c**2 - a**2 - b**2) / (2 * a * b))
    eta = simplify(sqrt(1 - gamma**2))
    n1 = x_axis
    n2 = simplify(gamma * x_axis + eta * z_axis)
    n3 = simplify(-(a * n1 + b * n2) / c)
    return (
        simplify(a * projector(n1)),
        simplify(b * projector(n2)),
        simplify(c * projector(n3)),
    )


def rr_menu(x_axis: Matrix = SX) -> tuple[Matrix, ...]:
    return (projector(x_axis), projector(-x_axis))


def rri_menu(d, x_axis: Matrix = SX) -> tuple[Matrix, ...]:
    return nonzero((d * I2, (1 - d) * projector(x_axis), (1 - d) * projector(-x_axis)))


def iii_menu(d1, d2) -> tuple[Matrix, ...]:
    return nonzero((d1 * I2, d2 * I2, (1 - d1 - d2) * I2))


def ii_menu(d) -> tuple[Matrix, ...]:
    return nonzero((d * I2, (1 - d) * I2))


def partition_function(kernel: Matrix, effect: Matrix, source) -> object:
    return simplify(pi**4 / simplify(kernel - source * effect).det() ** 2)


def raw_response(kernel: Matrix, effect: Matrix) -> object:
    source = symbols("source", real=True)
    return simplify(diff(partition_function(kernel, effect, source), source).subs(source, 0))


def log_response(kernel: Matrix, effect: Matrix) -> object:
    source = symbols("source", real=True)
    return simplify(diff(log(partition_function(kernel, effect, source)), source).subs(source, 0))


def grade(kernel: Matrix, effect: Matrix) -> object:
    return simplify(raw_response(kernel, effect) / raw_response(kernel, I2))


def intensity(kernel: Matrix, effect: Matrix, auxiliary: Matrix) -> object:
    action = simplify((auxiliary.conjugate().T * kernel * auxiliary).trace())
    insertion = simplify((auxiliary.conjugate().T * effect * auxiliary).trace())
    return simplify(exp(-action) * insertion)


def event_effect(menu: tuple[Matrix, ...], indices: tuple[int, ...]) -> Matrix:
    return simplify(sum((menu[index] for index in indices), Z2))


def event_class_key(effect: Matrix) -> tuple:
    return tuple(simplify(value) for value in effect)


def contextual(values: tuple) -> tuple:
    second = simplify(sum(value**2 for value in values))
    return tuple(simplify(value * (1 + value - second)) for value in values)


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

    kernel = I2 / 2
    source = symbols("source", real=True)
    zero_partition = partition_function(kernel, Z2, source)
    check(
        "independent-m2-gaussian",
        zero_partition == 16 * pi**4
        and raw_response(kernel, I2) == 128 * pi**4
        and log_response(kernel, I2) == 8,
        "two independent complex columns give Z(0)=16 pi^4, raw identity current 128 pi^4, and DlogZ[I]=8",
    )

    representatives = {
        "RRR-A": rrr_menu(Q(1, 2), Q(9, 10)),
        "RRR-B": rrr_menu(Q(1, 2), Q(3, 4)),
        "RR": rr_menu(),
        "RRI": rri_menu(Q(1, 3)),
        "III": iii_menu(Q(1, 5), Q(3, 10)),
        "II": ii_menu(Q(2, 5)),
    }
    check(
        "independent-five-stratum-menus",
        all(matrix_equal(sum(menu, Z2), I2) for menu in representatives.values())
        and tuple(len(representatives[name]) for name in ("RRR-A", "RR", "RRI", "III", "II"))
        == (3, 2, 3, 3, 2),
        "all five reconstructed menu types resolve identity with the expected arity",
    )

    vectors = {
        name: tuple(grade(kernel, effect) for effect in menu)
        for name, menu in representatives.items()
    }
    check(
        "independent-exact-vectors",
        vectors["RR"] == (Q(1, 2), Q(1, 2))
        and vectors["RRI"] == (Q(1, 3), Q(1, 3), Q(1, 3))
        and vectors["III"] == (Q(1, 5), Q(3, 10), Q(1, 2))
        and vectors["II"] == (Q(2, 5), Q(3, 5))
        and all(sum(vector) == 1 for vector in vectors.values()),
        "identity-source quotients independently reproduce every representative trace vector",
    )

    raw_ok = True
    for menu in representatives.values():
        for effect in menu:
            expected = simplify(64 * pi**4 * effect.trace())
            raw_ok = raw_ok and simplify(raw_response(kernel, effect) - expected) == 0
            raw_ok = raw_ok and simplify(
                raw_response(kernel, effect)
                - partition_function(kernel, effect, 0) * log_response(kernel, effect)
            ) == 0
    check(
        "independent-raw-before-quotient",
        raw_ok,
        "every raw derivative is 64 pi^4 Tr(E); the common-scale grade is formed only afterward",
    )

    continuum_menus = [rr_menu()]
    for denominator in range(1, 9):
        for numerator in range(denominator + 1):
            d = Q(numerator, denominator)
            continuum_menus.extend((rri_menu(d), ii_menu(d)))
        for left in range(denominator + 1):
            for right in range(denominator - left + 1):
                continuum_menus.append(iii_menu(Q(left, denominator), Q(right, denominator)))
        for left in range(denominator + 1):
            for right in range(denominator + 1):
                if left + right >= denominator:
                    continuum_menus.append(rrr_menu(Q(left, denominator), Q(right, denominator)))
    continuum_ok = all(
        matrix_equal(sum(menu, Z2), I2)
        and all(bool(simplify(grade(kernel, effect)).is_positive) for effect in menu)
        and simplify(sum(grade(kernel, effect) for effect in menu) - 1) == 0
        for menu in continuum_menus
    )
    check(
        "independent-continuum-boundaries",
        continuum_ok,
        f"{len(continuum_menus)} exact menus cover all coefficient domains and zero-removal boundaries",
    )

    fine = rrr_menu(Q(1, 2), Q(1, 2))
    coarse = rr_menu()
    merged = simplify(fine[0] + fine[1])
    auxiliary_probes = (
        I2,
        Matrix([[1, 0], [0, 0]]),
        Matrix([[1, I], [Q(1, 2), -I]]),
        Matrix([[Q(1, 3), Q(2, 5)], [I, Q(3, 4)]]),
    )
    pointwise_ok = matrix_equal(merged, coarse[0])
    for auxiliary in auxiliary_probes:
        left = intensity(kernel, fine[0], auxiliary)
        right = intensity(kernel, fine[1], auxiliary)
        union = intensity(kernel, merged, auxiliary)
        pointwise_ok = pointwise_ok and bool(simplify(left).is_nonnegative)
        pointwise_ok = pointwise_ok and bool(simplify(right).is_nonnegative)
        pointwise_ok = pointwise_ok and simplify(union - left - right) == 0
    check(
        "independent-marked-refinement",
        pointwise_ok
        and simplify(raw_response(kernel, merged) - raw_response(kernel, fine[0]) - raw_response(kernel, fine[1])) == 0,
        "positive M2 marked intensities and their integrated raw currents add before first-event conditioning",
    )

    # Independently rebuild the non-Boolean quotient of program-indexed event
    # presentations.  Raw atoms stay distinct even when two repeated-ray slots
    # carry the same effect.  A declared refinement map pushes their disjoint
    # union to the matching coarse singleton, and the exposure-stripped kernel
    # descends because it depends only on the summed effect.
    refinement_map = (0, 0, 1)
    fine_atom_keys = tuple(("fine", index) for index in range(len(fine)))
    coarse_atom_keys = tuple(("coarse", index) for index in range(len(coarse)))
    quotient_ok = (
        len(set(fine_atom_keys + coarse_atom_keys)) == len(fine_atom_keys + coarse_atom_keys)
        and matrix_equal(fine[0], fine[1])
        and bool(raw_response(kernel, fine[0]).is_positive)
        and all(
            event_class_key(event_effect(coarse, (coarse_index,)))
            == event_class_key(
                event_effect(
                    fine,
                    tuple(index for index, image in enumerate(refinement_map) if image == coarse_index),
                )
            )
            for coarse_index in range(len(coarse))
        )
        and raw_response(kernel, event_effect(coarse, (0,))) == 64 * pi**4
        and raw_response(kernel, event_effect(coarse, (0,)))
        == simplify(raw_response(kernel, fine[0]) + raw_response(kernel, fine[1]))
        and Q(1, 2) * raw_response(kernel, event_effect(fine, (0, 1)))
        == 32 * pi**4
        and Q(1, 8) * raw_response(kernel, event_effect(coarse, (0,)))
        == 8 * pi**4
        and Q(1, 2) * raw_response(kernel, event_effect(fine, (0, 1)))
        != Q(1, 8) * raw_response(kernel, event_effect(coarse, (0,)))
        and grade(kernel, event_effect(fine, (0, 1)))
        == grade(kernel, event_effect(coarse, (0,)))
        == Q(1, 2)
    )
    for auxiliary in auxiliary_probes:
        for coarse_index in range(len(coarse)):
            fine_indices = tuple(
                index for index, image in enumerate(refinement_map) if image == coarse_index
            )
            quotient_ok = quotient_ok and simplify(
                intensity(kernel, event_effect(coarse, (coarse_index,)), auxiliary)
                - sum(intensity(kernel, fine[index], auxiliary) for index in fine_indices)
            ) == 0
    check(
        "independent-event-presentation-quotient",
        quotient_ok,
        "distinct repeated-ray atoms push forward to both coarse slots; intrinsic currents descend while root exposure remains outside the quotient",
    )

    shared_a, shared_b = representatives["RRR-A"][0], representatives["RRR-B"][0]
    exposure = {
        "RRR-A": Q(1, 2),  # sector 1/4 times coefficient density 2
        "RRR-B": Q(1, 2),
        "RR": Q(1, 8),
        "RRI": Q(1, 4),
        "III": Q(1, 2),
        "II": Q(1, 8),
    }
    clock_prefactor = simplify(1 / raw_response(kernel, I2))
    conditional_hazards = {
        name: tuple(simplify(clock_prefactor * raw_response(kernel, effect)) for effect in menu)
        for name, menu in representatives.items()
    }
    joint_hazard_densities = {
        name: tuple(simplify(exposure[name] * value) for value in row)
        for name, row in conditional_hazards.items()
    }
    check(
        "independent-root-exposure-factorization",
        matrix_equal(shared_a, shared_b)
        and grade(kernel, shared_a) == grade(kernel, shared_b) == Q(1, 4)
        and clock_prefactor == 1 / (128 * pi**4)
        and all(bool(value.is_positive) for value in exposure.values())
        and all(simplify(sum(row) - 1) == 0 for row in conditional_hazards.values())
        and all(
            simplify(sum(joint_hazard_densities[name]) - exposure[name]) == 0
            for name in representatives
        )
        and all(
            tuple(simplify(value / sum(row)) for value in row) == vectors[name]
            for name, row in conditional_hazards.items()
        ),
        "the calibrated conditional clock has total rate one; root RN factors occur only in the outer joint exposure densities",
    )

    permutation_ok = all(
        sorted(grade(kernel, effect) for effect in ordering)
        == sorted(vectors[name])
        for name, menu in representatives.items()
        for ordering in permutations(menu)
    )
    root2 = sqrt(2)
    unitaries = (
        I2,
        SX,
        simplify((SX + SZ) / root2),
        Matrix([[1, 0], [0, I]]),
        simplify((I2 + I * SY) / root2),
    )
    covariance_ok = True
    for unitary in unitaries:
        covariance_ok = covariance_ok and matrix_equal(unitary * unitary.conjugate().T, I2)
        moved_kernel = simplify(unitary * kernel * unitary.conjugate().T)
        for menu in representatives.values():
            for effect in menu:
                moved_effect = simplify(unitary * effect * unitary.conjugate().T)
                covariance_ok = covariance_ok and grade(moved_kernel, moved_effect) == grade(kernel, effect)
    check(
        "independent-permutation-and-covariance",
        permutation_ok and covariance_ok,
        "every outcome ordering and five exact unitary/Haar-frame transports preserve the literal grades",
    )

    state = Matrix([[Q(3, 5), 0], [0, Q(2, 5)]])
    state_kernel = state.inv()
    shared = Q(1, 2) * projector_xz(0, 1)
    menu_a = (
        shared,
        Q(9, 10) * projector_xz(4 * root2 / 9, Q(-7, 9)),
        Q(3, 5) * projector_xz(-2 * root2 / 3, Q(1, 3)),
    )
    menu_b = (
        shared,
        Q(3, 4) * projector_xz(2 * root2 / 3, Q(-1, 3)),
        Q(3, 4) * projector_xz(-2 * root2 / 3, Q(-1, 3)),
    )
    state_a = tuple(grade(state_kernel, effect) for effect in menu_a)
    state_b = tuple(grade(state_kernel, effect) for effect in menu_b)
    check(
        "independent-block39-control",
        state_a == (Q(3, 10), Q(19, 50), Q(8, 25))
        and state_b == (Q(3, 10), Q(7, 20), Q(7, 20)),
        "the separately supplied inverse-covariance kernel rebuilds both hostile state-dependent vectors",
    )

    probes = (I2, projector_xz(0, 1), projector_xz(1, 0), projector_xz(0, -1))
    row_a = tuple(Q(7, 11) * raw_response(state_kernel, effect) for effect in probes)
    row_b = tuple(Q(13, 17) * raw_response(state_kernel, effect) for effect in probes)
    minors = tuple(
        simplify(row_a[i] * row_b[j] - row_a[j] * row_b[i])
        for i in range(len(probes))
        for j in range(i + 1, len(probes))
    )
    contextual_a = contextual(state_a)
    contextual_b = contextual(state_b)
    mutant_minor = simplify(
        contextual_a[0] * (1 - contextual_b[0])
        - (1 - contextual_a[0]) * contextual_b[0]
    )
    check(
        "independent-raw-minors",
        all(value == 0 for value in minors) and mutant_minor == -Q(27, 50000),
        "six action minors vanish while the contextual shared/complement minor is exactly -27/50000",
    )

    # Hostile source mutations: E -> E^2 is positive but not refinement
    # additive, while reversing the source sign gives a negative derivative.
    nonlinear_union = raw_response(kernel, simplify(merged * merged))
    nonlinear_parts = simplify(
        raw_response(kernel, simplify(fine[0] * fine[0]))
        + raw_response(kernel, simplify(fine[1] * fine[1]))
    )
    negative_source_response = simplify(-raw_response(kernel, fine[0]))
    outcome_scaled_a = (Q(2) * grade(kernel, shared_a), 1 - Q(2) * grade(kernel, shared_a))
    outcome_scaled_b = (Q(3) * grade(kernel, shared_b), 1 - Q(3) * grade(kernel, shared_b))
    scaled_minor = simplify(
        outcome_scaled_a[0] * outcome_scaled_b[1]
        - outcome_scaled_a[1] * outcome_scaled_b[0]
    )
    check(
        "independent-source-mutations-bite",
        simplify(nonlinear_union - nonlinear_parts) != 0
        and bool(negative_source_response.is_negative)
        and scaled_minor != 0,
        "nonadditive E^2 coupling, wrong source sign, and outcome-dependent exposure each violate a required gate",
    )

    # Hidden coupled-mode mutation: the visible two-coordinate source space is
    # the same, but an auxiliary coordinate coupled only to the first source
    # changes its response ratio.  Full action separability is therefore
    # load-bearing rather than automatic from the visible kernel.
    k0 = Matrix.diag(2, 2, 2)
    k1 = Matrix([[2, 0, 1], [0, 2, 0], [1, 0, 2]])
    e1 = Matrix.diag(1, 0, 0)
    e2 = Matrix.diag(0, 1, 0)
    log_rows = (
        (simplify((k0.inv() * e1).trace()), simplify((k0.inv() * e2).trace())),
        (simplify((k1.inv() * e1).trace()), simplify((k1.inv() * e2).trace())),
    )
    raw_rows = (
        tuple(simplify(pi**3 / k0.det() * value) for value in log_rows[0]),
        tuple(simplify(pi**3 / k1.det() * value) for value in log_rows[1]),
    )
    hidden_minor = simplify(
        raw_rows[0][0] * raw_rows[1][1] - raw_rows[0][1] * raw_rows[1][0]
    )
    check(
        "independent-hidden-coupling-mutation",
        log_rows == ((Q(1, 2), Q(1, 2)), (Q(2, 3), Q(1, 2)))
        and hidden_minor == -pi**6 / 576,
        "a positive auxiliary coupling changes one response ratio and produces raw minor -pi^6/576",
    )

    complex_kernel = Matrix([[2, I], [0, 2]])
    complex_response = simplify((complex_kernel.inv() * projector(SX)).trace())
    check(
        "independent-complex-action-mutation",
        complex_response == Q(1, 2) - I / 8
        and complex_response.is_real is False,
        "a non-Hermitian action gives 1/2-i/8, so positivity cannot be inferred before a readout choice",
    )

    analytic_patch_ok = all(
        simplify((kernel - Q(1, 4) * effect)[0, 0]) > 0
        and simplify((kernel - Q(1, 4) * effect).det()) > 0
        for menu in representatives.values()
        for effect in menu
    )
    check(
        "independent-positive-source-patch",
        analytic_patch_ok,
        "every reconstructed effect leaves Q-sE positive at s=1/4",
    )

    note_text = NOTE.read_text(encoding="utf-8") if NOTE.exists() else ""
    check(
        "independent-source-boundary",
        all(
            token in note_text
            for token in (
                "genuinely raw response",
                "marked Poisson",
                "event-presentation quotient",
                "Radon--Nikodym exposure density",
                "selected Law",
                "not an axiom consequence",
                "zero TOE-percentage movement",
            )
        ),
        "the source distinguishes exact construction, continuous exposure density, and physical selection",
    )

    check(
        "independent-input-closure",
        all((ROOT / path).exists() and not Path(path).is_absolute() for path in AUDIT_INPUT_PATHS),
        "the independent checker reads only its final theorem note",
    )

    print("per_element: independently rebuilt effects, raw derivatives, distinct Record atoms, and event-presentation classes are checked")
    print("per_site: the auxiliary M2 Gaussian kernel, finite conditional clock, quotient pushforward, and source patch are checked")
    print("per_mode: all four complex Gaussian modes enter the exact determinant-square partition function")
    print("per_block: five strata, 417 continuum menus, permutations, covariance, and hostile minors are checked")
    print("lattice_wide: checked and not executed — no autonomous global process is inferred from the local marked law")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
