#!/usr/bin/env python3
"""Independent exact checks for the corrected action/Record packet.

The helper does not import the primary runner. It evaluates the resolved
measurement menu, both stopped-process constructions, and the complete Route-B
finite channel on matrix units. Its inputs are the current bounded note and
the current Minimal Axioms memo.
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/ACTION_TRANSFER_RECORD_HAZARD_CONTENT_CROSSCALIBRATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md"
)
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ACTION_TRANSFER_RECORD_HAZARD_CONTENT_CROSSCALIBRATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
EXPECTED_INPUT_SHA256 = {
    NOTE_PATH: "28359fef35519587bc8f457df3d5e8d4c9bbf6cc7b9d731a1393f84450f12e47",
    MINIMAL_PATH: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
}

ID2 = sp.eye(2)
ID3 = sp.eye(3)
SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.diag(1, -1)
PAULI = (SX, SY, SZ)
MU = sp.Rational(1, 6)
DIRS = (
    sp.Matrix((1, 0, 0)), sp.Matrix((-1, 0, 0)),
    sp.Matrix((0, 1, 0)), sp.Matrix((0, -1, 0)),
    sp.Matrix((0, 0, 1)), sp.Matrix((0, 0, -1)),
)
SPINORS = (
    sp.Matrix((1, 1)) / sp.sqrt(2), sp.Matrix((1, -1)) / sp.sqrt(2),
    sp.Matrix((1, sp.I)) / sp.sqrt(2), sp.Matrix((1, -sp.I)) / sp.sqrt(2),
    sp.Matrix((1, 0)), sp.Matrix((0, 1)),
)
RESULTS: list[bool] = []


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(sp.simplify(left - right))


def projector(direction: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        (ID2 + sum((direction[k] * PAULI[k] for k in range(3)), sp.zeros(2))) / 2
    )


def matrix_units(dimension: int) -> tuple[sp.Matrix, ...]:
    units: list[sp.Matrix] = []
    for row in range(dimension):
        for column in range(dimension):
            unit = sp.zeros(dimension)
            unit[row, column] = 1
            units.append(unit)
    return tuple(units)


def report(name: str, passed: bool, detail: str) -> None:
    RESULTS.append(bool(passed))
    print(f"{'PASS' if passed else 'FAIL'}: {name} | {detail}")


def sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def check_input_binding() -> None:
    paths_exact = set(AUDIT_INPUT_PATHS) == set(EXPECTED_INPUT_SHA256)
    present = all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
    pinned = present and all(
        sha256(path) == EXPECTED_INPUT_SHA256[path] for path in AUDIT_INPUT_PATHS
    )
    report(
        "current_input_binding", paths_exact and pinned,
        f"declared={len(AUDIT_INPUT_PATHS)} note+current-minimal-memo hashes match",
    )


def measurement_rank(menu: tuple[sp.Matrix, ...]) -> int:
    return sp.Matrix([[1, *tuple(direction)] for direction in menu]).rank()


def check_measure_and_tomography_scope() -> None:
    mean = sum(DIRS, sp.zeros(3, 1)) * MU
    second = sum((n * n.T for n in DIRS), sp.zeros(3)) * MU
    sparse = (DIRS[4], DIRS[5])
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    rho_alt = sp.Matrix([
        [sp.Rational(1, 2), sp.Rational(1, 4)],
        [sp.Rational(1, 4), sp.Rational(1, 2)],
    ])
    discrepancy = sp.simplify(sqrt_w * rho_alt * sqrt_w - w / 2)
    sparse_blind = all(
        sp.simplify(sp.trace(projector(n) * discrepancy)) == 0 for n in sparse
    )
    six_detects = any(
        sp.simplify(sp.trace(projector(n) * discrepancy)) != 0 for n in DIRS
    )
    report(
        "moment_and_tomography_domains",
        matrix_zero(mean) and matrix_equal(second, sp.eye(3) / 3)
        and measurement_rank(DIRS) == 4 and measurement_rank(sparse) == 2
        and sparse_blind and six_detects and rho_alt.det() > 0,
        "zero mean gives half trace; six effects rank=4; +/-z rank=2 misses explicit coherence",
    )


def bloch_data(w: sp.Matrix) -> tuple[sp.Expr, sp.Matrix]:
    alpha = sp.simplify(sp.trace(w) / 2)
    r = sp.Matrix([
        sp.simplify(sp.trace(w * sigma) / sp.trace(w)) for sigma in PAULI
    ])
    return alpha, r


def check_determinant_rate_biconditional() -> None:
    alpha, alpha0 = sp.symbols("alpha alpha0", positive=True)
    rx, ry, rz = sp.symbols("rx ry rz", real=True)
    r2 = rx**2 + ry**2 + rz**2
    w = alpha * (ID2 + rx * SX + ry * SY + rz * SZ)
    determinant_identity = sp.simplify(w.det() - alpha**2 * (1 - r2)) == 0
    rate_from_det = alpha0 / sp.sqrt(1 - r2)
    forward = sp.simplify(rate_from_det**2 * (1 - r2) - alpha0**2) == 0
    witness = sp.diag(2, sp.Rational(1, 2))
    witness_alpha, witness_r = bloch_data(witness)
    witness_law = witness.det() == 1 and sp.simplify(
        witness_alpha - 1 / sp.sqrt(1 - (witness_r.T * witness_r)[0])
    ) == 0
    report(
        "constant_determinant_rate_biconditional",
        determinant_identity and forward and witness_law,
        "det W=alpha^2(1-|r|^2); positive alpha selects the positive root; witness=5/4",
    )


def check_same_qubit_step() -> None:
    gamma = sp.Rational(3, 2)
    dt = sp.Rational(1, 4)
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    rho = ID2 / 2
    k0 = sp.diag(
        sp.sqrt(1 - dt * gamma * w[0, 0]),
        sp.sqrt(1 - dt * gamma * w[1, 1]),
    )
    completeness = k0.H * k0
    pure_and_weighted = True
    for direction in DIRS:
        p = projector(direction)
        jump = sp.sqrt(2 * dt * gamma) * p * sqrt_w
        completeness += MU * jump.H * jump
        branch = sp.simplify(jump * rho * jump.H)
        pure_and_weighted &= matrix_equal(
            branch, dt * gamma * sp.trace(p * w) * p
        )
    no_jump = sp.simplify(k0 * rho * k0.H)
    no_jump /= sp.trace(no_jump)
    report(
        "same_qubit_first_step",
        dt * gamma * max(w.diagonal()) <= 1
        and matrix_equal(completeness, ID2) and pure_and_weighted
        and not matrix_equal(no_jump, rho),
        f"gamma={gamma}>0 domain holds; six-axis weights exact; no-jump={tuple(no_jump.diagonal())}",
    )


def check_rate_and_scalar_exceptions() -> None:
    gamma = sp.Rational(3, 2)
    w = sp.diag(2, sp.Rational(1, 2))
    alpha = sp.trace(w) / 2
    mix_second = gamma**2 * (w[0, 0] ** 2 + w[1, 1] ** 2) / 2
    single_second = (gamma * alpha) ** 2
    scalar = sp.Rational(7, 5)
    scalar_exact = sp.simplify(gamma * scalar / (gamma * scalar) - 1) == 0
    eventual_operator = sp.simplify(gamma * w * (gamma * w).inv())
    zero_rate_has_no_flux = matrix_equal(sp.S.Zero * w, sp.zeros(2))
    report(
        "positive_rate_and_scalar_null_cases",
        gamma > 0 and sp.simplify(mix_second - single_second) > 0
        and scalar_exact and matrix_equal(eventual_operator, ID2)
        and zero_rate_has_no_flux,
        "nonscalar mixture variance is positive; W=cI is exponential; gamma=0 has no event",
    )


def route_b_rate_and_ops(
    w: sp.Matrix, basis: tuple[sp.Matrix, sp.Matrix]
) -> tuple[sp.Expr, tuple[sp.Matrix, ...]]:
    sqrt_w = w ** sp.Rational(1, 2)
    blank = sp.Matrix((1, 0, 0))
    operators: list[sp.Matrix] = []
    for spinor in SPINORS:
        record = sp.Matrix((0, spinor[0], spinor[1]))
        for vector in basis:
            amplitude = sp.simplify((spinor.H * sqrt_w * vector)[0])
            operators.append(sp.sqrt(MU) * amplitude * record * blank.H)
    return sp.simplify(sp.trace(w) / 2), tuple(operators)


def route_b_tau(w: sp.Matrix, basis: tuple[sp.Matrix, sp.Matrix]) -> sp.Matrix:
    gamma, operators = route_b_rate_and_ops(w, basis)
    blank_p = sp.diag(1, 0, 0)
    deposited = sum((v * blank_p * v.H for v in operators), sp.zeros(3))
    return sp.simplify(deposited[1:3, 1:3] / gamma)


def route_b_finite_kraus(
    w: sp.Matrix,
    basis: tuple[sp.Matrix, sp.Matrix],
    survival: sp.Expr,
    record_unitary: sp.Matrix | None = None,
) -> tuple[sp.Matrix, ...]:
    gamma, operators = route_b_rate_and_ops(w, basis)
    hold = sp.zeros(3)
    hold[0, 0] = sp.sqrt(survival)
    hold[1:3, 1:3] = ID2 if record_unitary is None else record_unitary
    scale = sp.sqrt((1 - survival) / gamma)
    return (hold, *(sp.simplify(scale * v) for v in operators))


def apply_kraus(operators: tuple[sp.Matrix, ...], x: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sum((k * x * k.H for k in operators), sp.zeros(3)))


def route_b_channel_formula(x: sp.Matrix, survival: sp.Expr, tau: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(3)
    out[0, 0] = sp.simplify(survival * x[0, 0])
    for index in (1, 2):
        out[0, index] = sp.simplify(sp.sqrt(survival) * x[0, index])
        out[index, 0] = sp.simplify(sp.sqrt(survival) * x[index, 0])
    out[1:3, 1:3] = sp.simplify(
        x[1:3, 1:3] + (1 - survival) * x[0, 0] * tau
    )
    return out


def check_route_b_full_channel() -> None:
    w = sp.diag(2, sp.Rational(1, 2))
    e0, e1 = sp.eye(2).col(0), sp.eye(2).col(1)
    standard = (e0, e1)
    rotated = ((e0 + e1) / sp.sqrt(2), (e0 - e1) / sp.sqrt(2))
    survival = sp.Rational(1, 4)
    tau = route_b_tau(w, standard)
    canonical = route_b_finite_kraus(w, standard, survival)
    rotated_kraus = route_b_finite_kraus(w, rotated, survival)
    units = matrix_units(3)
    full_formula = all(
        matrix_equal(apply_kraus(canonical, u), route_b_channel_formula(u, survival, tau))
        for u in units
    )
    basis_independent = all(
        matrix_equal(apply_kraus(canonical, u), apply_kraus(rotated_kraus, u))
        for u in units
    )
    record_units = (units[4], units[5], units[7], units[8])
    record_absorption = all(matrix_equal(apply_kraus(canonical, u), u) for u in record_units)
    first, second = sp.Rational(1, 4), sp.Rational(4, 9)
    semigroup = all(
        matrix_equal(
            route_b_channel_formula(route_b_channel_formula(u, second, tau), first, tau),
            route_b_channel_formula(u, first * second, tau),
        ) for u in units
    )
    phase_kraus = route_b_finite_kraus(w, standard, survival, sp.diag(1, -1))
    phase_complete = matrix_equal(sum((k.H * k for k in phase_kraus), sp.zeros(3)), ID3)
    phase_changes = any(
        not matrix_equal(apply_kraus(phase_kraus, u), apply_kraus(canonical, u))
        for u in units
    )
    report(
        "route_b_full_matrix_channel",
        full_formula and basis_independent and record_absorption and semigroup
        and phase_complete and phase_changes,
        "9/9 units obey block formula/semigroup; 4/4 Record units fixed; complete phase mutant rejected",
    )


def basis_vector(dimension: int, index: int) -> sp.Matrix:
    vector = sp.zeros(dimension, 1)
    vector[index] = 1
    return vector


def check_carrier_and_parity_scope() -> None:
    blank = basis_vector(8, 0)
    logical_zero = basis_vector(8, 3)
    logical_one = basis_vector(8, 5)
    parity = sp.diag(*[(-1) ** index.bit_count() for index in range(8)])
    encoding = logical_zero.row_join(logical_one)
    parity_safe = all(
        matrix_equal(parity * vector, vector)
        for vector in (blank, logical_zero, logical_one)
    )
    for spinor in SPINORS:
        jump = encoding * spinor * blank.H
        parity_safe &= matrix_zero(parity * jump - jump * parity)
    dimensions = tuple(
        sum(index.bit_count() % 2 == 0 for index in range(2**qubits))
        for qubits in (2, 3)
    )
    report(
        "narrow_carrier_and_parity_escape",
        dimensions == (2, 4) and parity_safe,
        "two Record rays span the append carrier; fixed-parity dimensions=(2,4)",
    )


def check_race_discriminator() -> None:
    w1 = (sp.Integer(1), sp.Integer(1))
    w2 = (sp.Integer(2), sp.Rational(1, 2))
    gamma1 = sum(w1, sp.S.Zero) / 2
    gamma2 = sum(w2, sp.S.Zero) / 2
    memoryless = sp.simplify(gamma1 / (gamma1 + gamma2))
    filtering = sp.simplify(
        sp.Rational(1, 4) * sum((a / (a + b) for a in w1 for b in w2), sp.S.Zero)
    )
    r2 = sp.simplify((w2[0] - w2[1]) / (w2[0] + w2[1]))
    odds = sp.simplify(memoryless / (1 - memoryless))
    report(
        "two_site_race_discriminator",
        memoryless == sp.Rational(4, 9) and filtering == sp.Rational(1, 2)
        and r2 == sp.Rational(3, 5) and odds == sp.Rational(4, 5),
        f"P_B(1)={memoryless}; P_Q(1)={filtering}; r2={r2}; positive common rate cancels",
    )


def check_conditional_record_scope() -> None:
    probabilities = (sp.Rational(4, 9), sp.Rational(1, 3), sp.Rational(3, 5))
    centered = all(
        sp.simplify(p * (1 - p) + (1 - p) * (-p)) == 0 for p in probabilities
    )
    note = " ".join((ROOT / NOTE_PATH).read_text(encoding="utf-8").split())
    guarded = (
        "predictive probability is supplied" in note
        and "No formal audit verdict is assigned here" in note
        and "categorical physical wall-independence" in note
    )
    report(
        "conditional_record_filtration_scope", centered and guarded,
        "Bernoulli centering only after candidate probabilities are supplied; no empirical or audit claim",
    )


def main() -> int:
    check_input_binding()
    check_measure_and_tomography_scope()
    check_determinant_rate_biconditional()
    check_same_qubit_step()
    check_rate_and_scalar_exceptions()
    check_route_b_full_channel()
    check_carrier_and_parity_scope()
    check_race_discriminator()
    check_conditional_record_scope()
    failures = sum(not result for result in RESULTS)
    print("per_element: exact positive qubit transfers, spanning effects, and determinant identities")
    print("per_site: one same-qubit stopped filter and one full 3x3 blank/Record channel")
    print("per_mode: six resolved marks and a finite fixed-parity embedding; no menu uniqueness claim")
    print("per_block: the conditional two-site 4/9 versus 1/2 race fixture")
    print("lattice_wide: not executed; physical source, allocation, collisions, and empirical realization remain open")
    print(f"TOTAL: PASS={len(RESULTS) - failures} FAIL={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
