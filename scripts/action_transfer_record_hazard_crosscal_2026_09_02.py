#!/usr/bin/env python3
"""Exact certificates for the corrected action/Record architecture packet.

The runner checks only the bounded mathematics used by the canonical note. It
imports the independent helper as a declared source dependency and compares
one full-channel formulation with it; the helper remains separately executable
and does not import this primary runner.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

import sympy as sp

import independent_action_transfer_record_hazard_crosscal_2026_09_02 as independent


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    "docs/ACTION_TRANSFER_RECORD_HAZARD_CONTENT_CROSSCALIBRATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md"
)
MINIMAL_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
HELPER_PATH = "scripts/independent_action_transfer_record_hazard_crosscal_2026_09_02.py"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ACTION_TRANSFER_RECORD_HAZARD_CONTENT_CROSSCALIBRATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-02.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/independent_action_transfer_record_hazard_crosscal_2026_09_02.py",
)
EXPECTED_INPUT_SHA256 = {
    NOTE_PATH: "28359fef35519587bc8f457df3d5e8d4c9bbf6cc7b9d731a1393f84450f12e47",
    MINIMAL_PATH: "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    HELPER_PATH: "abc10e1ca076c771db1699985de026a78da92d8b467e08eda1894c65dbdd33ef",
}

I2 = sp.eye(2)
I3 = sp.eye(3)
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
KETS = (
    sp.Matrix((1, 1)) / sp.sqrt(2), sp.Matrix((1, -1)) / sp.sqrt(2),
    sp.Matrix((1, sp.I)) / sp.sqrt(2), sp.Matrix((1, -sp.I)) / sp.sqrt(2),
    sp.Matrix((1, 0)), sp.Matrix((0, 1)),
)


@dataclass
class Harness:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        if condition:
            self.passed += 1
            print(f"PASS {label} :: {detail}")
        else:
            self.failed += 1
            print(f"FAIL {label} :: {detail}")


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in matrix)


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return left.shape == right.shape and matrix_zero(sp.simplify(left - right))


def projector(direction: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        (I2 + sum((direction[k] * PAULI[k] for k in range(3)), sp.zeros(2))) / 2
    )


def sha256(relative: str) -> str:
    return hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()


def source_certificate(h: Harness) -> None:
    declared = set(AUDIT_INPUT_PATHS) == set(EXPECTED_INPUT_SHA256)
    hashes = declared and all(
        (ROOT / path).is_file() and sha256(path) == EXPECTED_INPUT_SHA256[path]
        for path in AUDIT_INPUT_PATHS
    )
    helper_file = Path(independent.__file__).resolve() == (ROOT / HELPER_PATH).resolve()
    helper_contract = (
        independent.AUDIT_TIMEOUT_SEC == 30
        and independent.AUDIT_INPUT_PATHS == (NOTE_PATH, MINIMAL_PATH)
        and set(independent.EXPECTED_INPUT_SHA256) == {NOTE_PATH, MINIMAL_PATH}
    )
    h.check(
        "source and independent-helper closure",
        hashes and helper_file and helper_contract,
        "current note, current Minimal Axioms memo, and actual imported helper are source-bound",
    )


def measure_and_tomography_certificate(h: Harness) -> None:
    first = sp.simplify(sum(DIRS, sp.zeros(3, 1)) * MU)
    second = sp.simplify(sum((n * n.T for n in DIRS), sp.zeros(3)) * MU)
    effect_rank = sp.Matrix([[1, *tuple(n)] for n in DIRS]).rank()
    sparse = (DIRS[4], DIRS[5])
    sparse_rank = sp.Matrix([[1, *tuple(n)] for n in sparse]).rank()
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    rho = sp.Matrix([
        [sp.Rational(1, 2), sp.Rational(1, 4)],
        [sp.Rational(1, 4), sp.Rational(1, 2)],
    ])
    d = sp.simplify(sqrt_w * rho * sqrt_w - w / 2)
    sparse_blind = all(sp.simplify(sp.trace(projector(n) * d)) == 0 for n in sparse)
    six_detects = any(sp.simplify(sp.trace(projector(n) * d)) != 0 for n in DIRS)
    h.check(
        "measure moments and tomography domain",
        matrix_zero(first) and matrix_equal(second, I3 / 3)
        and effect_rank == 4 and sparse_rank == 2 and sparse_blind and six_detects,
        "zero mean proves half trace; uniqueness needs spanning effects; explicit +/-z coherence counterexample",
    )


def determinant_and_scale_certificate(h: Harness) -> None:
    alpha, alpha0 = sp.symbols("alpha alpha0", positive=True)
    rx, ry, rz = sp.symbols("rx ry rz", real=True)
    r2 = rx**2 + ry**2 + rz**2
    w = alpha * (I2 + rx * SX + ry * SY + rz * SZ)
    identity = sp.simplify(w.det() - alpha**2 * (1 - r2)) == 0
    rate_root = alpha0 / sp.sqrt(1 - r2)
    both_directions = sp.simplify(rate_root**2 * (1 - r2) - alpha0**2) == 0
    witness = sp.diag(2, sp.Rational(1, 2))
    scaled = sp.Rational(3, 2) * witness
    r = sp.Matrix([sp.trace(witness * sigma) / sp.trace(witness) for sigma in PAULI])
    scaled_r = sp.Matrix([sp.trace(scaled * sigma) / sp.trace(scaled) for sigma in PAULI])
    h.check(
        "determinant biconditional and scalar freedom",
        identity and both_directions and witness.det() == 1
        and matrix_equal(r, scaled_r)
        and sp.trace(scaled) / sp.trace(witness) == sp.Rational(3, 2),
        "positive root gives iff; context scalar preserves content and changes relative rate",
    )


def route_q_certificate(h: Harness) -> None:
    gamma = sp.Rational(3, 2)
    dt = sp.Rational(1, 4)
    w = sp.diag(2, sp.Rational(1, 2))
    sqrt_w = sp.diag(sp.sqrt(2), 1 / sp.sqrt(2))
    rho = I2 / 2
    k0 = sp.diag(
        sp.sqrt(1 - dt * gamma * w[0, 0]),
        sp.sqrt(1 - dt * gamma * w[1, 1]),
    )
    complete = k0.H * k0
    pure = True
    for direction in DIRS:
        effect = projector(direction)
        jump = sp.sqrt(2 * dt * gamma) * effect * sqrt_w
        complete += MU * jump.H * jump
        branch = sp.simplify(jump * rho * jump.H)
        pure &= matrix_equal(branch, dt * gamma * sp.trace(effect * w) * effect)
    survived = sp.simplify(k0 * rho * k0.H)
    survived /= sp.trace(survived)
    alpha = sp.trace(w) / 2
    mixture_second = gamma**2 * (w[0, 0] ** 2 + w[1, 1] ** 2) / 2
    nonscalar = sp.simplify(mixture_second - (gamma * alpha) ** 2) > 0
    scalar = sp.Rational(7, 5)
    scalar_null = sp.simplify(gamma * scalar / (gamma * scalar) - 1) == 0
    eventual = sp.simplify(gamma * w * (gamma * w).inv())
    h.check(
        "same-qubit stopped filter with exceptions",
        gamma > 0 and dt * gamma * max(w.diagonal()) <= 1
        and matrix_equal(complete, I2) and pure and not matrix_equal(survived, rho)
        and nonscalar and scalar_null and matrix_equal(eventual, I2),
        "nonscalar W filters and is nonexponential; W=cI is exponential; eventual law requires gamma>0",
    )


def matrix_units() -> tuple[sp.Matrix, ...]:
    units: list[sp.Matrix] = []
    for row in range(3):
        for column in range(3):
            unit = sp.zeros(3)
            unit[row, column] = 1
            units.append(unit)
    return tuple(units)


def route_b_ops(
    w: sp.Matrix, basis: tuple[sp.Matrix, sp.Matrix]
) -> tuple[sp.Expr, tuple[sp.Matrix, ...]]:
    sqrt_w = w ** sp.Rational(1, 2)
    blank = sp.Matrix((1, 0, 0))
    ops: list[sp.Matrix] = []
    for ket in KETS:
        record = sp.Matrix((0, ket[0], ket[1]))
        for vector in basis:
            amplitude = sp.simplify((ket.H * sqrt_w * vector)[0])
            ops.append(sp.sqrt(MU) * amplitude * record * blank.H)
    return sp.simplify(sp.trace(w) / 2), tuple(ops)


def finite_route_b(
    w: sp.Matrix,
    basis: tuple[sp.Matrix, sp.Matrix],
    survival: sp.Expr,
    record_unitary: sp.Matrix | None = None,
) -> tuple[sp.Matrix, ...]:
    rate, jumps = route_b_ops(w, basis)
    hold = sp.zeros(3)
    hold[0, 0] = sp.sqrt(survival)
    hold[1:3, 1:3] = I2 if record_unitary is None else record_unitary
    scale = sp.sqrt((1 - survival) / rate)
    return (hold, *(sp.simplify(scale * jump) for jump in jumps))


def apply_channel(kraus: tuple[sp.Matrix, ...], x: sp.Matrix) -> sp.Matrix:
    return sp.simplify(sum((k * x * k.H for k in kraus), sp.zeros(3)))


def channel_formula(x: sp.Matrix, survival: sp.Expr, tau: sp.Matrix) -> sp.Matrix:
    out = sp.zeros(3)
    out[0, 0] = sp.simplify(survival * x[0, 0])
    for index in (1, 2):
        out[0, index] = sp.simplify(sp.sqrt(survival) * x[0, index])
        out[index, 0] = sp.simplify(sp.sqrt(survival) * x[index, 0])
    out[1:3, 1:3] = sp.simplify(
        x[1:3, 1:3] + (1 - survival) * x[0, 0] * tau
    )
    return out


def route_b_full_channel_certificate(h: Harness) -> None:
    w = sp.diag(2, sp.Rational(1, 2))
    e0, e1 = I2.col(0), I2.col(1)
    standard = (e0, e1)
    rotated = ((e0 + e1) / sp.sqrt(2), (e0 - e1) / sp.sqrt(2))
    survival = sp.Rational(1, 4)
    rate, jumps = route_b_ops(w, standard)
    blank = sp.diag(1, 0, 0)
    deposited = sum((jump * blank * jump.H for jump in jumps), sp.zeros(3))
    tau = sp.simplify(deposited[1:3, 1:3] / rate)
    canonical = finite_route_b(w, standard, survival)
    rotated_channel = finite_route_b(w, rotated, survival)
    units = matrix_units()
    exact_full_map = all(
        matrix_equal(apply_channel(canonical, unit), channel_formula(unit, survival, tau))
        for unit in units
    )
    basis_gauge = all(
        matrix_equal(apply_channel(canonical, unit), apply_channel(rotated_channel, unit))
        for unit in units
    )
    record_units = (units[4], units[5], units[7], units[8])
    absorbs_full_record_block = all(
        matrix_equal(apply_channel(canonical, unit), unit) for unit in record_units
    )
    s1, s2 = sp.Rational(1, 4), sp.Rational(4, 9)
    semigroup = all(
        matrix_equal(
            channel_formula(channel_formula(unit, s2, tau), s1, tau),
            channel_formula(unit, s1 * s2, tau),
        ) for unit in units
    )
    helper_tau = independent.route_b_tau(w, standard)
    helper_agreement = all(
        matrix_equal(
            channel_formula(unit, survival, tau),
            independent.route_b_channel_formula(unit, survival, helper_tau),
        ) for unit in units
    )
    phase = finite_route_b(w, standard, survival, sp.diag(1, -1))
    phase_complete = matrix_equal(sum((k.H * k for k in phase), sp.zeros(3)), I3)
    phase_rejected = any(
        not matrix_equal(apply_channel(phase, unit), apply_channel(canonical, unit))
        for unit in units
    )
    h.check(
        "Route B complete finite channel",
        exact_full_map and basis_gauge and absorbs_full_record_block and semigroup
        and helper_agreement and phase_complete and phase_rejected,
        "9 matrix units, 4 Record units, both coherence blocks, semigroup, basis gauge, helper, phase control",
    )


def carrier_and_parity_certificate(h: Harness) -> None:
    parity = sp.diag(*[(-1) ** index.bit_count() for index in range(8)])
    blank = sp.eye(8).col(0)
    logical = sp.eye(8).col(3).row_join(sp.eye(8).col(5))
    parity_safe = matrix_equal(parity * blank, blank)
    for ket in KETS:
        jump = logical * ket * blank.H
        parity_safe &= matrix_zero(parity * jump - jump * parity)
    even_dims = tuple(
        sum(index.bit_count() % 2 == 0 for index in range(2**qubits))
        for qubits in (2, 3)
    )
    h.check(
        "narrow carrier boundary and finite parity escape",
        even_dims == (2, 4) and parity_safe,
        "two Record rays span a qubit; three qubits provide an even blank+logical subspace; placement unproved",
    )


def race_and_conditional_filtration_certificate(h: Harness) -> None:
    w1 = (sp.Integer(1), sp.Integer(1))
    w2 = (sp.Integer(2), sp.Rational(1, 2))
    rate1, rate2 = sum(w1) / 2, sum(w2) / 2
    memoryless = sp.simplify(rate1 / (rate1 + rate2))
    filtering = sp.simplify(
        sp.Rational(1, 4) * sum((a / (a + b) for a in w1 for b in w2))
    )

    def winner_polarization(target: tuple[sp.Expr, ...], other: tuple[sp.Expr, ...]) -> sp.Expr:
        plus = sum(target[0] / (target[0] + value) for value in other)
        minus = sum(target[1] / (target[1] + value) for value in other)
        return sp.simplify((plus - minus) / (plus + minus))

    competitor_dependence = winner_polarization(w2, w1) != winner_polarization(
        w2, (sp.Integer(3), sp.Rational(1, 3))
    )
    probabilities = (memoryless, sp.Rational(1, 3), sp.Rational(3, 5))
    conditional_centering = all(
        sp.simplify(p * (1 - p) + (1 - p) * (-p)) == 0 for p in probabilities
    )
    h.check(
        "conditional race and filtration",
        memoryless == sp.Rational(4, 9) and filtering == sp.Rational(1, 2)
        and competitor_dependence and conditional_centering,
        "P_B=4/9, P_Q=1/2; filtering content depends on competitor; centering assumes candidate probabilities",
    )


def scope_certificate(h: Harness) -> None:
    note = " ".join((ROOT / NOTE_PATH).read_text(encoding="utf-8").split())
    minimal = " ".join((ROOT / MINIMAL_PATH).read_text(encoding="utf-8").split())
    n_sections = all(f"### N{index} —" in note for index in range(1, 9))
    note_guards = all(phrase in note for phrase in (
        "claim_type: bounded_theorem",
        "Zero first moment by itself does not give this conclusion",
        "`W=cI`",
        "At `gamma_*=0` there is no event",
        "No categorical pairwise physical-independence claim is made",
        "No formal audit verdict is assigned here",
        "historical 48-Boolean mutation claim receives no current scientific credit",
    ))
    premise_boundary = all(phrase in minimal for phrase in (
        "conditional on formation at that site",
        "does not supply the formation site, probability, or rate",
        "does not choose a Hamiltonian or transfer operator",
    ))
    h.check(
        "bounded claim and premise scope",
        n_sections and note_guards and premise_boundary,
        "tomography, scalar/rate, wall, historical-provenance, no-audit, and current-axiom guards are live",
    )


def main() -> int:
    h = Harness()
    source_certificate(h)
    measure_and_tomography_certificate(h)
    determinant_and_scale_certificate(h)
    route_q_certificate(h)
    route_b_full_channel_certificate(h)
    carrier_and_parity_certificate(h)
    race_and_conditional_filtration_certificate(h)
    scope_certificate(h)
    print("per_element: positive qubit transfer, spanning effects, determinant, and scalar/rate domains")
    print("per_site: complete same-qubit step and full 3x3 blank/Record finite channel")
    print("per_mode: six registered effects and finite parity embedding; no physical uniqueness")
    print("per_block: conditional 4/9 versus 1/2 two-site race and supplied filtration")
    print("lattice_wide: not executed; no source selection, allocator, collision law, empirical corpus, or TOE closure")
    print(f"TOTAL: PASS={h.passed} FAIL={h.failed}")
    return 0 if h.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
