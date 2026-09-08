#!/usr/bin/env python3
"""Exact finite-domain selector for the Block 84 Record instrument.

The runner classifies proper-cubic covariant density compilers on the 26
nonzero vectors in {-1,0,1}^3.  Covariance leaves one radial coefficient in
each k=1,2,3 orbit.  Two midpoint identities between actually executed
lattice directions and one axis-slot calibration select the linear compiler.
The resulting density is decomposed on the actual Block 84 spectral support,
which fixes its probabilities.  A positive covariant cubic-response compiler
is retained as an exact countermodel to covariance alone.
"""

from __future__ import annotations

from itertools import permutations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_AXIS_SEPARABLE_BARYCENTER_SELECTOR_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK84_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
BARYCENTER_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)

AUDIT_INPUT_PATHS = (
    'docs/ADMISSIBILITY_AXIS_SEPARABLE_BARYCENTER_SELECTOR_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/audit/data/axiom_premise_nodes.json',
    'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md',
    'docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md',
    'docs/ADMISSIBILITY_BARYCENTER_EVALUATION_MENU_KERNEL_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md',
    'docs/ADMISSIBILITY_REGISTERED_PARTITION_BARYCENTER_PUSHFORWARD_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'docs/RECORD_CONTENT_ONLY_SHARED_EFFECT_DESCENT_BOUNDED_THEOREM_NOTE_2026-08-12.md',
    'docs/ADMISSIBILITY_TAXICAB_SHELL_RECORD_INSTRUMENT_CYLINDER_LAW_BOUNDED_THEOREM_NOTE_2026-08-14.md',
    'scripts/frontier_admissibility_taxicab_shell_record_instrument_2026_08_14.py',
)

Vec = tuple[int, int, int]

I2 = sp.eye(2)
SIGMA = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -sp.I], [sp.I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
E1: Vec = (1, 0, 0)
E12: Vec = (1, 1, 0)
E123: Vec = (1, 1, 1)
DIRECTIONS: tuple[Vec, ...] = tuple(
    vector
    for vector in product((-1, 0, 1), repeat=3)
    if vector != (0, 0, 0)
)

PASS_COUNT = 0
FAIL_COUNT = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    """Record one compact fail-closed check."""
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"PASS: {label}")
    else:
        FAIL_COUNT += 1
        print(f"FAIL: {label} :: {detail}")


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(left[row, col] - right[row, col]) == 0
        for row in range(left.rows)
        for col in range(left.cols)
    )


def k_value(direction: Vec) -> int:
    return sum(component * component for component in direction)


def as_column(direction: Vec) -> sp.Matrix:
    return sp.Matrix(direction)


def as_vec(column: sp.Matrix) -> Vec:
    return tuple(int(column[index]) for index in range(3))  # type: ignore[return-value]


def proper_cubic_rotations() -> tuple[sp.ImmutableMatrix, ...]:
    rotations: set[sp.ImmutableMatrix] = set()
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for source_axis, target_axis in enumerate(permutation):
                matrix[target_axis, source_axis] = signs[source_axis]
            if matrix.det() == 1:
                rotations.add(sp.ImmutableMatrix(matrix))
    return tuple(sorted(rotations, key=lambda item: tuple(item)))


ROTATIONS = proper_cubic_rotations()


def rotate(rotation: sp.Matrix, direction: Vec) -> Vec:
    return as_vec(rotation * as_column(direction))


def orbit(direction: Vec) -> frozenset[Vec]:
    return frozenset(rotate(rotation, direction) for rotation in ROTATIONS)


def stabilizer(direction: Vec) -> tuple[sp.ImmutableMatrix, ...]:
    return tuple(
        rotation
        for rotation in ROTATIONS
        if rotate(rotation, direction) == direction
    )


def fixed_space(direction: Vec) -> list[sp.Matrix]:
    constraints = [sp.Matrix(rotation) - sp.eye(3) for rotation in stabilizer(direction)]
    return sp.Matrix.vstack(*constraints).nullspace()


def bloch_operator(direction: Vec | sp.Matrix) -> sp.Matrix:
    components = list(direction)
    return sp.simplify(
        sum(
            (sp.sympify(components[index]) * SIGMA[index] for index in range(3)),
            sp.zeros(2),
        )
    )


def density_from_vector(vector: sp.Matrix) -> sp.Matrix:
    return sp.simplify((I2 + bloch_operator(vector)) / 2)


def covariant_density(
    direction: Vec,
    lambdas: tuple[sp.Expr, sp.Expr, sp.Expr],
) -> sp.Matrix:
    radial = lambdas[k_value(direction) - 1]
    return density_from_vector(radial * as_column(direction))


def projector(direction: Vec, sign: int) -> sp.Matrix:
    k = k_value(direction)
    if k == 0 or sign not in (-1, 1):
        raise ValueError("spectral projectors need d != 0 and sign +/-1")
    return sp.simplify((I2 + sign * bloch_operator(direction) / sp.sqrt(k)) / 2)


def spectral_weight(direction: Vec, sign: int) -> sp.Expr:
    return sp.simplify((1 + sign * sp.sqrt(k_value(direction)) / 3) / 2)


def cubic_weight(direction: Vec, sign: int) -> sp.Expr:
    radial = sp.sqrt(k_value(direction)) / 3
    return sp.simplify((1 + sign * radial**3) / 2)


def axis_slot(axis: int, value: int) -> sp.Matrix:
    if axis not in (0, 1, 2) or value not in (-1, 0, 1):
        raise ValueError("axis slots use three axes and values -1,0,1")
    return sp.simplify((I2 + value * SIGMA[axis]) / 2)


def slot_barycenter(direction: Vec, weights: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.simplify(
        sum(
            (weights[axis] * axis_slot(axis, direction[axis]) for axis in range(3)),
            sp.zeros(2),
        )
    )


def matrix_coefficients(matrix: sp.Matrix) -> tuple[sp.Expr, sp.Expr, sp.Expr]:
    """Return Pauli coefficients Tr(matrix sigma_a)."""
    return tuple(sp.simplify(sp.trace(matrix * sigma)) for sigma in SIGMA)  # type: ignore[return-value]


def main() -> int:
    note_text = NOTE_PATH.read_text(encoding="utf-8")
    axiom_text = AXIOM_PATH.read_text(encoding="utf-8")
    block84_text = BLOCK84_PATH.read_text(encoding="utf-8")
    barycenter_text = BARYCENTER_PATH.read_text(encoding="utf-8")
    axiom_flat = " ".join(axiom_text.split())
    barycenter_flat = " ".join(barycenter_text.split())

    print("A. finite proper-cubic carrier and orbit classification")
    check("A1 proper cubic group has 24 elements", len(ROTATIONS) == 24, len(ROTATIONS))
    check(
        "A2 the three k-orbits partition all 26 executed directions",
        orbit(E1) | orbit(E12) | orbit(E123) == frozenset(DIRECTIONS)
        and not (orbit(E1) & orbit(E12))
        and not (orbit(E1) & orbit(E123))
        and not (orbit(E12) & orbit(E123)),
    )
    check(
        "A3 k=1,2,3 orbit sizes are exactly 6,12,8",
        tuple(len(orbit(rep)) for rep in (E1, E12, E123)) == (6, 12, 8),
    )
    fixed_results: list[bool] = []
    for representative in (E1, E12, E123):
        basis = fixed_space(representative)
        fixed_results.append(
            len(basis) == 1
            and sp.Matrix.hstack(basis[0], as_column(representative)).rank() == 1
        )
    check(
        "A4 every orbit stabilizer fixes only its radial line",
        all(fixed_results),
        fixed_results,
    )

    lambda1, lambda2, lambda3 = sp.symbols("lambda_1 lambda_2 lambda_3", real=True)
    lambdas = (lambda1, lambda2, lambda3)
    covariance_ok = True
    for direction in DIRECTIONS:
        vector = lambdas[k_value(direction) - 1] * as_column(direction)
        for rotation in ROTATIONS:
            rotated = rotate(rotation, direction)
            rotated_vector = lambdas[k_value(rotated) - 1] * as_column(rotated)
            covariance_ok &= rotated_vector == sp.Matrix(rotation) * vector
    check(
        "A5 three independent radial coefficients give every equivariant compiler",
        covariance_ok and all(fixed_results),
    )

    carrier_ok = True
    for direction in DIRECTIONS:
        operator = bloch_operator(direction)
        k = k_value(direction)
        carrier_ok &= matrix_equal(operator * operator, k * I2)
    spectral_variable = sp.symbols("z")
    spectrum_ok = carrier_ok
    for representative, radial in zip((E1, E12, E123), lambdas):
        k = k_value(representative)
        density = covariant_density(representative, lambdas)
        expected_characteristic = sp.expand(
            (
                spectral_variable - (1 + radial * sp.sqrt(k)) / 2
            )
            * (
                spectral_variable - (1 - radial * sp.sqrt(k)) / 2
            )
        )
        actual_characteristic = density.charpoly(spectral_variable).as_expr()
        spectrum_ok &= sp.simplify(
            actual_characteristic - expected_characteristic
        ) == 0
    check(
        "A6 each density spectrum is (1 +/- lambda_k sqrt(k))/2",
        spectrum_ok,
    )

    print("B. actual-sector midpoint selector")
    m12 = sp.simplify(
        (
            covariant_density((1, 1, 0), lambdas)
            + covariant_density((1, -1, 0), lambdas)
        )
        / 2
        - covariant_density(E1, lambdas)
    )
    m23 = sp.simplify(
        (
            covariant_density((1, 1, 1), lambdas)
            + covariant_density((1, 1, -1), lambdas)
        )
        / 2
        - covariant_density(E12, lambdas)
    )
    check(
        "B1 k1-k2 midpoint residual is (lambda2-lambda1) sigma1/2",
        matrix_equal(m12, (lambda2 - lambda1) * SIGMA[0] / 2),
        m12,
    )
    check(
        "B2 k2-k3 midpoint residual is (lambda3-lambda2)(sigma1+sigma2)/2",
        matrix_equal(m23, (lambda3 - lambda2) * (SIGMA[0] + SIGMA[1]) / 2),
        m23,
    )
    calibration_target = sp.simplify(
        (projector(E1, 1) + I2 / 2 + I2 / 2) / 3
    )
    calibration_residual = sp.simplify(
        covariant_density(E1, lambdas) - calibration_target
    )
    selector_solutions = sp.solve(
        [
            *matrix_coefficients(m12),
            *matrix_coefficients(m23),
            *matrix_coefficients(calibration_residual),
        ],
        (lambda1, lambda2, lambda3),
        dict=True,
    )
    check(
        "B3 two actual midpoints plus one axis calibration uniquely give lambda_k=1/3",
        selector_solutions
        == [{lambda1: sp.Rational(1, 3), lambda2: sp.Rational(1, 3), lambda3: sp.Rational(1, 3)}],
        selector_solutions,
    )
    selector_rows = sp.Matrix(
        [
            [-1, 1, 0],
            [0, -1, 1],
            [1, 0, 0],
        ]
    )
    drop_one_ranks = tuple(
        sp.Matrix(
            [
                list(selector_rows.row(index))
                for index in range(selector_rows.rows)
                if index != row
            ]
        ).rank()
        for row in range(selector_rows.rows)
    )
    drop_one_witnesses = (
        (sp.Rational(1, 3), sp.Rational(1, 4), sp.Rational(1, 4)),
        (sp.Rational(1, 3), sp.Rational(1, 3), sp.Rational(1, 4)),
        (sp.Rational(1, 4), sp.Rational(1, 4), sp.Rational(1, 4)),
    )
    witness_equations = (
        lambda2 - lambda1,
        lambda3 - lambda2,
        lambda1 - sp.Rational(1, 3),
    )
    drop_one_ok = selector_rows.rank() == 3 and drop_one_ranks == (2, 2, 2)
    for omitted, witness in enumerate(drop_one_witnesses):
        substitutions = dict(zip(lambdas, witness))
        drop_one_ok &= all(
            sp.simplify(equation.subs(substitutions)) == 0
            for index, equation in enumerate(witness_equations)
            if index != omitted
        )
        drop_one_ok &= sp.simplify(
            witness_equations[omitted].subs(substitutions)
        ) != 0
        drop_one_ok &= all(
            abs(witness[k - 1]) * sp.sqrt(k) <= 1 for k in (1, 2, 3)
        )
    check(
        "B4 M12, M23, and C1 are irredundant only within this declared equation family",
        drop_one_ok,
        {"ranks": drop_one_ranks, "witnesses": drop_one_witnesses},
    )

    print("C. axis-slot law and equal spatial weights")
    w1, w2, w3 = sp.symbols("w_1 w_2 w_3", real=True)
    weights = (w1, w2, w3)
    covariance_equations: set[sp.Expr] = {w1 + w2 + w3 - 1}
    for direction in DIRECTIONS:
        source_vector = sp.Matrix(
            [weights[index] * direction[index] for index in range(3)]
        )
        for rotation in ROTATIONS:
            rotated = rotate(rotation, direction)
            target_vector = sp.Matrix(
                [weights[index] * rotated[index] for index in range(3)]
            )
            residual = target_vector - sp.Matrix(rotation) * source_vector
            covariance_equations.update(sp.expand(item) for item in residual)
    weight_solutions = sp.solve(
        list(covariance_equations), (w1, w2, w3), dict=True
    )
    check(
        "C1 normalized proper-cubic slot weights are uniquely 1/3,1/3,1/3",
        weight_solutions
        == [{w1: sp.Rational(1, 3), w2: sp.Rational(1, 3), w3: sp.Rational(1, 3)}],
        weight_solutions,
    )
    uniform_weights = (sp.Rational(1, 3),) * 3
    slot_identity_ok = all(
        matrix_equal(
            slot_barycenter(direction, uniform_weights),
            density_from_vector(as_column(direction) / 3),
        )
        for direction in product((-1, 0, 1), repeat=3)
    )
    check(
        "C2 the equal-slot barycenter is exactly (I+d.sigma/3)/2 on all 27 conditions",
        slot_identity_ok,
    )
    check(
        "C3 the slot law implies both midpoint identities and the calibration",
        matrix_equal(
            slot_barycenter(E1, uniform_weights), calibration_target
        )
        and matrix_equal(
            slot_barycenter(E1, uniform_weights),
            (
                slot_barycenter((1, 1, 0), uniform_weights)
                + slot_barycenter((1, -1, 0), uniform_weights)
            )
            / 2,
        )
        and matrix_equal(
            slot_barycenter(E12, uniform_weights),
            (
                slot_barycenter((1, 1, 1), uniform_weights)
                + slot_barycenter((1, 1, -1), uniform_weights)
            )
            / 2,
        ),
    )

    print("D. actual spectral support fixes the Block 84 probabilities")
    spectral_ok = True
    barycenter_ok = True
    trace_weights_ok = True
    positivity_ok = True
    for direction in DIRECTIONS:
        plus = projector(direction, 1)
        minus = projector(direction, -1)
        density = slot_barycenter(direction, uniform_weights)
        spectral_ok &= (
            matrix_equal(plus * plus, plus)
            and matrix_equal(minus * minus, minus)
            and matrix_equal(plus * minus, sp.zeros(2))
            and matrix_equal(plus + minus, I2)
        )
        reconstructed = sp.simplify(
            spectral_weight(direction, 1) * plus
            + spectral_weight(direction, -1) * minus
        )
        barycenter_ok &= matrix_equal(reconstructed, density)
        trace_weights_ok &= all(
            sp.simplify(sp.trace(density * projector(direction, sign)))
            == spectral_weight(direction, sign)
            for sign in (-1, 1)
        )
        positivity_ok &= all(
            bool(sp.simplify(spectral_weight(direction, sign) > 0))
            and bool(sp.simplify(spectral_weight(direction, sign) < 1))
            for sign in (-1, 1)
        )
    check("D1 the actual support is an orthogonal rank-one pair", spectral_ok)
    check("D2 its unique barycentric weights reproduce the linear density", barycenter_ok)
    check("D3 trace extraction gives (1+s sqrt(k)/3)/2", trace_weights_ok)
    check("D4 all 52 selected weights are strictly between zero and one", positivity_ok)

    p = sp.symbols("p", real=True)
    generic_direction = E123
    generic_mixture = sp.simplify(
        p * projector(generic_direction, 1)
        + (1 - p) * projector(generic_direction, -1)
    )
    check(
        "D5 orthogonality makes the spectral mixture coefficient identifiable",
        sp.simplify(sp.trace(generic_mixture * projector(generic_direction, 1))) == p
        and sp.simplify(sp.trace(generic_mixture * projector(generic_direction, -1))) == 1 - p,
    )

    print("E. exact hostile twin and narrow nonselection")
    cubic_lambdas = (
        sp.Rational(1, 27),
        sp.Rational(2, 27),
        sp.Rational(3, 27),
    )
    cubic_contract_ok = True
    cubic_trace_ok = True
    for direction in DIRECTIONS:
        density = covariant_density(direction, cubic_lambdas)
        k = k_value(direction)
        cubic_contract_ok &= (
            matrix_equal(density, density.conjugate().T)
            and sp.simplify(sp.trace(density)) == 1
            and sp.simplify(density.det()) > 0
        )
        cubic_trace_ok &= all(
            sp.simplify(sp.trace(density * projector(direction, sign)))
            == cubic_weight(direction, sign)
            for sign in (-1, 1)
        )
    check(
        "E1 the cubic twin is a positive trace-one density on all 26 directions",
        cubic_contract_ok,
    )
    check(
        "E2 the cubic density gives the Block 84 cubic-response weights",
        cubic_trace_ok,
    )
    cubic_m12 = sp.simplify(
        (
            covariant_density((1, 1, 0), cubic_lambdas)
            + covariant_density((1, -1, 0), cubic_lambdas)
        )
        / 2
        - covariant_density(E1, cubic_lambdas)
    )
    cubic_m23 = sp.simplify(
        (
            covariant_density((1, 1, 1), cubic_lambdas)
            + covariant_density((1, 1, -1), cubic_lambdas)
        )
        / 2
        - covariant_density(E12, cubic_lambdas)
    )
    check(
        "E3 the cubic k1-k2 midpoint residual is exactly sigma1/54",
        matrix_equal(cubic_m12, SIGMA[0] / 54),
        cubic_m12,
    )
    check(
        "E4 the cubic k2-k3 midpoint residual is exactly (sigma1+sigma2)/54",
        matrix_equal(cubic_m23, (SIGMA[0] + SIGMA[1]) / 54),
        cubic_m23,
    )
    check(
        "E5 the cubic k1 calibration misses by exactly 4 sigma1/27",
        matrix_equal(
            calibration_target - covariant_density(E1, cubic_lambdas),
            4 * SIGMA[0] / 27,
        ),
    )

    entropy_probability = sp.symbols("p", positive=True)
    binary_entropy = -entropy_probability * sp.log(entropy_probability) - (
        1 - entropy_probability
    ) * sp.log(1 - entropy_probability)
    entropy_first = sp.simplify(sp.diff(binary_entropy, entropy_probability))
    entropy_second = sp.simplify(
        sp.diff(binary_entropy, entropy_probability, 2)
    )
    entropy_route_ok = (
        sp.solve(entropy_first, entropy_probability) == [sp.Rational(1, 2)]
        and entropy_second
        == 1 / (entropy_probability * (entropy_probability - 1))
        and
        sp.simplify(entropy_first.subs(entropy_probability, sp.Rational(1, 2)))
        == 0
        and sp.simplify(
            entropy_second.subs(entropy_probability, sp.Rational(1, 2))
        )
        == -4
        and all(
            spectral_weight(direction, 1) != sp.Rational(1, 2)
            for direction in DIRECTIONS
        )
    )
    check(
        "E6 unconstrained binary maximum entropy selects 1/2, not the linear k-sector weights",
        entropy_route_ok,
    )

    print("F. framework boundary and no-go discipline")
    required_axiom_needles = (
        "The full one-site possibility domain has algebraic presentation `M_2(C)`.",
        "the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.",
        "the distribution's form and values",
    )
    check(
        "F1 current axioms supply a distribution but explicitly leave its form and values open",
        all(needle in axiom_flat for needle in required_axiom_needles),
    )
    check(
        "F2 Block 84 exposes both linear and cubic executed laws",
        "linear spectral member" in block84_text
        and "cubic-response twin" in block84_text,
    )
    check(
        "F3 prior barycenter work labels physical restriction and registration as supplied",
        "identification of its barycenter with an effect-evaluation state" in barycenter_flat
        and "does not register a physical menu" in barycenter_flat,
    )
    note_lower = note_text.lower()
    check(
        "F4 note carries the complete N1-N8 structured stress test",
        "## no-go discipline gate" in note_lower
        and all(f"### n{index}" in note_lower for index in range(1, 9))
        and note_text.count("`ATTEMPTED`") >= 5,
    )
    check(
        "F5 narrow no-go gate passes without claiming universal nonderivability",
        "no-go-discipline status: pass" in note_lower
        and "not a universal no-go" in note_lower
        and "zero toe percentage movement" in note_lower,
    )

    print(
        "per_element: resolved exactly for all 26 directions, all 24 proper-cubic rotations, and both spectral atoms"
    )
    print(
        "per_site: resolved for one forming site under every nonzero opposite-neighbor difference in {-1,0,1}^3"
    )
    print(
        "per_mode: resolved separately on the k=1, k=2, and k=3 proper-cubic direction orbits"
    )
    print(
        "per_block: resolved for the Block 84 one-site spectral instrument; formation, scheduler, and history laws remain outside this block"
    )
    print(
        "lattice_wide: checked and not executed — the pointwise selector is compatible with Block 84, but no new formation or spacetime theorem is run here"
    )
    print(f"TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
