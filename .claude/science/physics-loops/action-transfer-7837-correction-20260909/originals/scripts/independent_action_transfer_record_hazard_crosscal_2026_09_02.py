#!/usr/bin/env python3
"""Independent exact checks for the Block 50 action/Record construction.

This runner is deliberately self-contained: it imports no project runner and
uses the six signed cubic axes as an exact spherical two-design.
"""

from __future__ import annotations

import sys

import sympy as sp


ID2 = sp.eye(2)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)
PAULI = (SX, SY, SZ)
MU = sp.Rational(1, 6)
DIRS = (
    sp.Matrix((1, 0, 0)),
    sp.Matrix((-1, 0, 0)),
    sp.Matrix((0, 1, 0)),
    sp.Matrix((0, -1, 0)),
    sp.Matrix((0, 0, 1)),
    sp.Matrix((0, 0, -1)),
)
SPINORS = (
    sp.Matrix((1, 1)) / sp.sqrt(2),
    sp.Matrix((1, -1)) / sp.sqrt(2),
    sp.Matrix((1, sp.I)) / sp.sqrt(2),
    sp.Matrix((1, -sp.I)) / sp.sqrt(2),
    sp.Matrix((1, 0)),
    sp.Matrix((0, 1)),
)


def projector(direction: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        (ID2 + sum((direction[k] * PAULI[k] for k in range(3)), sp.zeros(2))) / 2
    )


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(left - right)


def bloch_data(w: sp.Matrix) -> tuple[sp.Expr, sp.Matrix]:
    alpha = sp.simplify(sp.trace(w) / 2)
    r = sp.Matrix(
        [sp.simplify(sp.trace(w * sigma) / sp.trace(w)) for sigma in PAULI]
    )
    return alpha, r


RESULTS: list[bool] = []


def report(name: str, passed: bool, detail: str) -> None:
    RESULTS.append(bool(passed))
    print(f"{'PASS' if passed else 'FAIL'}: {name} | {detail}")


def check_cubic_two_design() -> None:
    mean = sp.zeros(3, 1)
    second = sp.zeros(3)
    pmean = sp.zeros(2)
    for direction in DIRS:
        mean += MU * direction
        second += MU * direction * direction.T
        pmean += MU * projector(direction)
    passed = (
        sum((MU for _ in DIRS), sp.S.Zero) == 1
        and matrix_zero(mean)
        and matrix_equal(second, sp.eye(3) / 3)
        and matrix_equal(pmean, ID2 / 2)
        and all((direction.T * direction)[0] == 1 for direction in DIRS)
    )
    report("cubic_2_design", passed, "mean=0 second=I3/3 integral(P)=I2/2")


def check_determinant_rate_biconditional() -> None:
    transfers = (
        sp.eye(2),
        sp.diag(2, sp.Rational(1, 2)),
        sp.Matrix([[sp.Rational(5, 4), sp.Rational(3, 4)],
                   [sp.Rational(3, 4), sp.Rational(5, 4)]]),
        sp.diag(3, sp.Rational(1, 2)),
    )
    biconditional = True
    decomposition = True
    positivity_and_rate = True
    for w in transfers:
        alpha, r = bloch_data(w)
        r2 = sp.simplify((r.T * r)[0])
        rebuilt = alpha * (
            ID2 + sum((r[k] * PAULI[k] for k in range(3)), sp.zeros(2))
        )
        decomposition &= matrix_equal(w, rebuilt)
        decomposition &= sp.simplify(w.det() - alpha**2 * (1 - r2)) == 0
        det_equal = sp.simplify(w.det() - 1) == 0
        rate_equal = sp.simplify(alpha**2 * (1 - r2) - 1) == 0
        biconditional &= det_equal == rate_equal
        positivity_and_rate &= all(value.is_positive for value in w.eigenvals())
        integrated_rate = sp.simplify(
            sum((MU * sp.trace(projector(n) * w) for n in DIRS), sp.S.Zero)
        )
        positivity_and_rate &= sp.simplify(integrated_rate - alpha) == 0
        positivity_and_rate &= all(
            sp.trace(projector(n) * w).is_positive for n in DIRS
        )
    witness = transfers[1]
    alpha, r = bloch_data(witness)
    rnorm = sp.sqrt(sp.simplify((r.T * r)[0]))
    direct_rate_law = sp.simplify(alpha - 1 / sp.sqrt(1 - rnorm**2)) == 0
    report(
        "positive_transfer_determinant_rate_biconditional",
        decomposition and positivity_and_rate and biconditional and direct_rate_law,
        f"det={witness.det()} alpha={alpha} |r|={rnorm} constant-det iff rate law",
    )


def check_same_qubit_filter() -> None:
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    dt = sp.Rational(1, 4)
    rho = ID2 / 2
    k0 = sp.diag(sp.sqrt(1 - 2 * dt), sp.sqrt(1 - dt / 2))
    completeness = k0.H * k0
    pure_outputs = True
    for direction in DIRS:
        p = projector(direction)
        kn = sp.sqrt(2 * dt) * p * sqrt_w
        completeness += MU * kn.H * kn
        branch = sp.simplify(kn * rho * kn.H)
        pure_outputs &= matrix_equal(branch, dt * sp.trace(p * w) * p)
    no_jump = sp.simplify(k0 * rho * k0.H)
    no_jump /= sp.trace(no_jump)
    filtering = not matrix_equal(no_jump, rho)
    alpha = sp.trace(w) / 2
    mixture_second_derivative = sp.Rational(1, 2) * (
        w[0, 0] ** 2 + w[1, 1] ** 2
    )
    survival_not_single = sp.simplify(mixture_second_derivative - alpha**2) != 0
    integrated_transfer = sp.simplify(w * w.inv())
    eventual_marks = [
        sp.simplify(sp.trace(projector(direction) * integrated_transfer))
        for direction in DIRS
    ]
    eventual_uniform = all(mark == 1 for mark in eventual_marks)
    passed = (
        matrix_equal(completeness, ID2)
        and pure_outputs
        and filtering
        and survival_not_single
        and eventual_uniform
    )
    report(
        "same_qubit_filtering",
        passed,
        f"complete; no-jump diag={tuple(no_jump.diagonal())}; S''mix={mixture_second_derivative} != {alpha**2}; marks=1",
    )


def check_orthogonal_blank() -> None:
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    blank = sp.Matrix((1, 0, 0))
    blank_p = blank * blank.H
    record_p = sp.diag(0, 1, 1)
    basis = (sp.Matrix((1, 0)), sp.Matrix((0, 1)))
    gamma = sp.simplify(sp.trace(w) / 2)
    rate_effect = sp.zeros(3)
    kraus_by_mark: list[list[sp.Matrix]] = []
    pure_branches = True
    absorbing = True
    for spinor in SPINORS:
        record = sp.Matrix((0, spinor[0], spinor[1]))
        p = spinor * spinor.H
        operators = []
        branch = sp.zeros(3)
        for e_j in basis:
            amplitude = sp.simplify((spinor.H * sqrt_w * e_j)[0])
            v = sp.sqrt(MU) * amplitude * (record * blank.H)
            operators.append(v)
            rate_effect += v.H * v
            branch += v * blank_p * v.H
            absorbing &= matrix_zero(v * record_p)
        expected = MU * sp.trace(p * w) * (record * record.H)
        pure_branches &= matrix_equal(branch, expected)
        kraus_by_mark.append(operators)
    expected_effect = gamma * blank_p
    survival_probability = sp.Rational(1, 4)
    k_hold = sp.sqrt(survival_probability) * blank_p + record_p
    finite_completeness = k_hold.H * k_hold
    scale = sp.sqrt((1 - survival_probability) / gamma)
    for operators in kraus_by_mark:
        for operator in operators:
            finite = scale * operator
            finite_completeness += finite.H * finite
    for spinor in SPINORS:
        record = sp.Matrix((0, spinor[0], spinor[1]))
        state = record * record.H
        held = k_hold * state * k_hold.H
        absorbing &= matrix_equal(held, state)
    passed = (
        matrix_equal(rate_effect, expected_effect)
        and matrix_equal(finite_completeness, sp.eye(3))
        and pure_branches
        and absorbing
    )
    report(
        "orthogonal_blank_kraus",
        passed,
        f"rate={gamma} exact finite completeness; blank survives scalar; Record sector absorbing",
    )


def basis_vector(dimension: int, index: int) -> sp.Matrix:
    vector = sp.zeros(dimension, 1)
    vector[index] = 1
    return vector


def check_three_qubit_parity_embedding() -> None:
    parity = sp.diag(*[(-1) ** index.bit_count() for index in range(8)])
    blank = basis_vector(8, 0)       # |000>
    logical_zero = basis_vector(8, 3)  # |011>
    logical_one = basis_vector(8, 5)   # |101>
    encoding = logical_zero.row_join(logical_one)
    vectors = (blank, logical_zero, logical_one)
    orthonormal = all(
        (left.H * right)[0] == (1 if i == j else 0)
        for i, left in enumerate(vectors)
        for j, right in enumerate(vectors)
    )
    parity_safe = all(matrix_equal(parity * vector, vector) for vector in vectors)
    w = sp.diag(2, sp.Rational(1, 2))
    embedded_w = encoding * w * encoding.H
    parity_safe &= matrix_zero(parity * embedded_w - embedded_w * parity)
    for spinor in SPINORS:
        logical_n = encoding * spinor
        jump = logical_n * blank.H
        logical_projector = logical_n * logical_n.H
        parity_safe &= matrix_zero(parity * jump - jump * parity)
        parity_safe &= matrix_zero(
            parity * logical_projector - logical_projector * parity
        )
    even_dimensions = tuple(
        sum(index.bit_count() % 2 == 0 for index in range(2**qubits))
        for qubits in (2, 3)
    )
    minimal_fixed_parity = even_dimensions[0] < 3 <= even_dimensions[1]
    report(
        "three_qubit_parity_safe_embedding",
        orthonormal and parity_safe and minimal_fixed_parity,
        f"even-sector dims={even_dimensions}; |000>,|011>,|101> and jumps commute with parity",
    )


def check_race_discriminator() -> None:
    w1 = (sp.Integer(1), sp.Integer(1))
    w2 = (sp.Integer(2), sp.Rational(1, 2))
    gamma1 = sum(w1, sp.S.Zero) / 2
    gamma2 = sum(w2, sp.S.Zero) / 2
    memoryless_p1 = sp.simplify(gamma1 / (gamma1 + gamma2))
    filtering_p1 = sp.simplify(
        sp.Rational(1, 4)
        * sum((a / (a + b) for a in w1 for b in w2), sp.S.Zero)
    )
    r1 = sp.simplify((w1[0] - w1[1]) / (w1[0] + w1[1]))
    r2 = sp.simplify((w2[0] - w2[1]) / (w2[0] + w2[1]))
    odds = sp.simplify(memoryless_p1 / (1 - memoryless_p1))
    content_odds = sp.sqrt(sp.simplify((1 - r2**2) / (1 - r1**2)))
    passed = (
        memoryless_p1 == sp.Rational(4, 9)
        and filtering_p1 == sp.Rational(1, 2)
        and r1 == 0
        and r2 == sp.Rational(3, 5)
        and sp.simplify(odds - content_odds) == 0
    )
    report(
        "memoryless_vs_filtering_race",
        passed,
        f"P_B(1)={memoryless_p1} P_Q(1)={filtering_p1} r2={r2} odds={odds}",
    )


def check_record_only_boundary() -> None:
    required_records = {
        "pre_race_conditions",
        "event_codec",
        "joint_eligibility",
        "winner_order",
        "winner_content",
        "trial_id",
    }
    gamma1 = sp.Integer(1)
    gamma2 = sp.Rational(5, 4)
    simultaneous = sp.simplify(gamma1 / (gamma1 + gamma2))
    survival_until_delayed_start = sp.Rational(1, 2)  # delay log(2)/gamma1
    delayed = sp.simplify(
        1
        - survival_until_delayed_start
        + survival_until_delayed_start * simultaneous
    )
    w2 = sp.diag(2, sp.Rational(1, 2))
    _, r2 = bloch_data(w2)
    _, scaled_r2 = bloch_data(2 * w2)
    scaled_race = sp.simplify(gamma1 / (gamma1 + 2 * gamma2))
    premises_typed = (
        "duration" not in required_records
        and "blank_absence" not in required_records
        and len(required_records) == 6
    )
    confounding_exposed = (
        simultaneous == sp.Rational(4, 9)
        and delayed == sp.Rational(13, 18)
        and delayed != simultaneous
        and matrix_equal(r2, scaled_r2)
        and scaled_race == sp.Rational(2, 7)
        and scaled_race != simultaneous
    )
    report(
        "record_only_premise_boundary",
        premises_typed and confounding_exposed,
        f"sim={simultaneous} delayed={delayed} scalar-shift={scaled_race}; duration/blank absence not read",
    )


def main() -> int:
    check_cubic_two_design()
    check_determinant_rate_biconditional()
    check_same_qubit_filter()
    check_orthogonal_blank()
    check_three_qubit_parity_embedding()
    check_race_discriminator()
    check_record_only_boundary()
    failures = sum(not result for result in RESULTS)
    print(f"TOTAL: PASS={len(RESULTS) - failures} FAIL={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
