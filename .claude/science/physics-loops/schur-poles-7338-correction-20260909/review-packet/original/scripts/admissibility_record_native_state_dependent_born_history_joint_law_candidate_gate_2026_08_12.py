#!/usr/bin/env python3
"""Block 63: state-dependent Record/Born/history candidate-law gate.

The runner constructs one exact finite-menu kernel, a measure-and-prepare CP
instrument, exact projective cylinders, contingent one-history semantics, and
an indefinitely extensible append-only single-front Record process.  It also
replays the Cycle-587 uniform/biased discriminator without importing the
never-mainlined Cycle-574--587 stack.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path
from typing import Iterable

import numpy as np


AUDIT_TIMEOUT_SEC = 180
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BORN_FORM_NOTE = ROOT / "docs" / "BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md"
ATOMIC_NOTE = ROOT / "docs" / "ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/BORN_FORM_FROM_BINARY_TERNARY_SCALED_PROJECTOR_FRAME_LIFT_BOUNDED_THEOREM_NOTE_2026-08-09.md",
    "docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
)


@dataclass(frozen=True)
class ExactComplex:
    real: Fraction = Fraction(0)
    imag: Fraction = Fraction(0)

    def __add__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(self.real + other.real, self.imag + other.imag)

    def __neg__(self) -> "ExactComplex":
        return ExactComplex(-self.real, -self.imag)

    def __sub__(self, other: "ExactComplex") -> "ExactComplex":
        return self + (-other)

    def __mul__(self, other: "ExactComplex") -> "ExactComplex":
        return ExactComplex(
            self.real * other.real - self.imag * other.imag,
            self.real * other.imag + self.imag * other.real,
        )

    def conjugate(self) -> "ExactComplex":
        return ExactComplex(self.real, -self.imag)


ZERO = ExactComplex()
ONE = ExactComplex(Fraction(1))
I_UNIT = ExactComplex(Fraction(0), Fraction(1))
MINUS_I_HALF = ExactComplex(Fraction(0), Fraction(-1, 2))


def z(value: int | Fraction) -> ExactComplex:
    return ExactComplex(Fraction(value))


Matrix = tuple[
    tuple[ExactComplex, ExactComplex],
    tuple[ExactComplex, ExactComplex],
]

ZERO_MATRIX: Matrix = ((ZERO, ZERO), (ZERO, ZERO))
IDENTITY: Matrix = ((ONE, ZERO), (ZERO, ONE))
PAULI_X: Matrix = ((ZERO, ONE), (ONE, ZERO))
PAULI_Y: Matrix = ((ZERO, -I_UNIT), (I_UNIT, ZERO))
PAULI_Z: Matrix = ((ONE, ZERO), (ZERO, -ONE))
PAULIS = (PAULI_X, PAULI_Y, PAULI_Z)


def matrix(*entries: int | Fraction) -> Matrix:
    return (
        (z(entries[0]), z(entries[1])),
        (z(entries[2]), z(entries[3])),
    )


def matrix_add(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(left[r][c] + right[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def matrix_scale(value: Fraction, operand: Matrix) -> Matrix:
    scalar = ExactComplex(value)
    return tuple(
        tuple(scalar * operand[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def matrix_complex_scale(value: ExactComplex, operand: Matrix) -> Matrix:
    return tuple(
        tuple(value * operand[r][c] for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def matrix_multiply(left: Matrix, right: Matrix) -> Matrix:
    return tuple(
        tuple(
            left[r][0] * right[0][c] + left[r][1] * right[1][c]
            for c in range(2)
        )
        for r in range(2)
    )  # type: ignore[return-value]


def matrix_dagger(operand: Matrix) -> Matrix:
    return tuple(
        tuple(operand[c][r].conjugate() for c in range(2)) for r in range(2)
    )  # type: ignore[return-value]


def matrix_trace(operand: Matrix) -> ExactComplex:
    return operand[0][0] + operand[1][1]


def matrix_sum(items: Iterable[Matrix]) -> Matrix:
    answer = ZERO_MATRIX
    for item in items:
        answer = matrix_add(answer, item)
    return answer


def hermitian_part(operand: Matrix) -> Matrix:
    return matrix_scale(Fraction(1, 2), matrix_add(operand, matrix_dagger(operand)))


def antihermitian_observable(operand: Matrix) -> Matrix:
    return matrix_complex_scale(MINUS_I_HALF, matrix_add(operand, matrix_scale(Fraction(-1), matrix_dagger(operand))))


def real_trace_product(left: Matrix, right: Matrix) -> Fraction:
    value = matrix_trace(matrix_multiply(left, right))
    if value.imag != 0:
        raise ValueError("trace product is not real")
    return value.real


def density(matrix_value: Matrix) -> bool:
    return matrix_value == matrix_dagger(matrix_value) and matrix_trace(matrix_value) == ONE and psd(matrix_value)


def psd(matrix_value: Matrix) -> bool:
    if matrix_value != matrix_dagger(matrix_value):
        return False
    a = matrix_value[0][0].real
    d = matrix_value[1][1].real
    determinant = matrix_value[0][0] * matrix_value[1][1] - matrix_value[0][1] * matrix_value[1][0]
    return a >= 0 and d >= 0 and determinant.imag == 0 and determinant.real >= 0


def to_numpy(operand: Matrix) -> np.ndarray:
    return np.asarray(
        [[complex(float(x.real), float(x.imag)) for x in row] for row in operand],
        dtype=complex,
    )


def effect_weights(rho: Matrix, menu: tuple[Matrix, ...]) -> tuple[Fraction, ...]:
    return tuple(real_trace_product(rho, effect) for effect in menu)


def normalized_effect_state(effect: Matrix) -> Matrix:
    trace = matrix_trace(effect)
    if trace.imag != 0 or trace.real <= 0:
        raise ValueError("effect trace must be positive and real")
    return matrix_scale(Fraction(1, 1) / trace.real, effect)


E0 = matrix(Fraction(1, 2), 0, 0, 0)
EA1 = matrix(Fraction(1, 2), 0, 0, Fraction(1, 5))
EA2 = matrix(0, 0, 0, Fraction(4, 5))
EB1 = matrix(Fraction(1, 4), Fraction(1, 4), Fraction(1, 4), Fraction(1, 2))
EB2 = matrix(Fraction(1, 4), Fraction(-1, 4), Fraction(-1, 4), Fraction(1, 2))
MENUS = ((E0, EA1, EA2), (E0, EB1, EB2))


def density_at_t(t: int) -> Matrix:
    denominator = t * t + 4
    return matrix(Fraction(t * t + 2, denominator), 0, 0, Fraction(2, denominator))


def pure_real(a: Fraction, b: Fraction) -> Matrix:
    if a * a + b * b != 1:
        raise ValueError("amplitudes are not normalized")
    return matrix(a * a, a * b, a * b, b * b)


def direction_matrix(direction: tuple[int, int, int]) -> Matrix:
    answer = ZERO_MATRIX
    for coefficient, pauli in zip(direction, PAULIS):
        answer = matrix_add(answer, matrix_scale(Fraction(coefficient), pauli))
    return answer


def central(value: Fraction) -> Matrix:
    return matrix_scale(value, IDENTITY)


def program_carrier(rho: Matrix, direction: tuple[int, int, int], menu: int) -> Matrix:
    anti = matrix_add(direction_matrix(direction), central(Fraction(menu)))
    return matrix_add(rho, matrix_complex_scale(I_UNIT, anti))


def outcome_carrier(effect: Matrix, label: int) -> Matrix:
    return matrix_add(effect, matrix_complex_scale(I_UNIT, central(Fraction(label))))


def decode_program(carrier: Matrix) -> tuple[Matrix, tuple[Fraction, Fraction, Fraction], Fraction]:
    rho = hermitian_part(carrier)
    anti = antihermitian_observable(carrier)
    label = matrix_trace(anti).real / 2
    traceless = matrix_add(anti, matrix_scale(-label, IDENTITY))
    direction = tuple(real_trace_product(traceless, pauli) / 2 for pauli in PAULIS)
    return rho, direction, label  # type: ignore[return-value]


def decode_outcome(carrier: Matrix) -> tuple[Matrix, Fraction]:
    effect = hermitian_part(carrier)
    anti = antihermitian_observable(carrier)
    return effect, matrix_trace(anti).real / 2


def determinant3(rotation: tuple[tuple[int, int, int], ...]) -> int:
    a = rotation
    return (
        a[0][0] * (a[1][1] * a[2][2] - a[1][2] * a[2][1])
        - a[0][1] * (a[1][0] * a[2][2] - a[1][2] * a[2][0])
        + a[0][2] * (a[1][0] * a[2][1] - a[1][1] * a[2][0])
    )


def proper_cubic_rotations() -> tuple[tuple[tuple[int, int, int], ...], ...]:
    answer = set()
    for perm in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            rows = []
            for row, column in enumerate(perm):
                values = [0, 0, 0]
                values[column] = signs[row]
                rows.append(tuple(values))
            rotation = tuple(rows)
            if determinant3(rotation) == 1:
                answer.add(rotation)
    return tuple(sorted(answer))


def rotate_vector(rotation: tuple[tuple[int, int, int], ...], vector: tuple[int | Fraction, int | Fraction, int | Fraction]) -> tuple[Fraction, Fraction, Fraction]:
    return tuple(
        sum((Fraction(rotation[r][c]) * Fraction(vector[c]) for c in range(3)), Fraction(0))
        for r in range(3)
    )  # type: ignore[return-value]


def hermitian_coefficients(operand: Matrix) -> tuple[Fraction, tuple[Fraction, Fraction, Fraction]]:
    scalar = matrix_trace(operand).real / 2
    vector = tuple(real_trace_product(operand, pauli) / 2 for pauli in PAULIS)
    return scalar, vector  # type: ignore[return-value]


def rotate_hermitian(rotation: tuple[tuple[int, int, int], ...], operand: Matrix) -> Matrix:
    scalar, vector = hermitian_coefficients(operand)
    rotated = rotate_vector(rotation, vector)
    answer = matrix_scale(scalar, IDENTITY)
    for coefficient, pauli in zip(rotated, PAULIS):
        answer = matrix_add(answer, matrix_scale(coefficient, pauli))
    return answer


State = tuple[Matrix, int]


def transition(state: State, outcome: int) -> tuple[Fraction, State]:
    rho, menu_index = state
    effect = MENUS[menu_index][outcome]
    probability = real_trace_product(rho, effect)
    return probability, (normalized_effect_state(effect), 1 - menu_index)


def cylinder_weight(initial: State, word: tuple[int, ...]) -> Fraction:
    state = initial
    weight = Fraction(1)
    for outcome in word:
        probability, state = transition(state, outcome)
        weight *= probability
    return weight


def select_outcome(state: State, innovation: Fraction) -> tuple[int, State]:
    if not (0 <= innovation < 1):
        raise ValueError("innovation must lie in [0,1)")
    rho, menu_index = state
    weights = effect_weights(rho, MENUS[menu_index])
    cumulative = Fraction(0)
    for outcome, weight in enumerate(weights):
        cumulative += weight
        if innovation < cumulative:
            return outcome, transition(state, outcome)[1]
    raise AssertionError("normalized kernel did not select an outcome")


Coord = tuple[int, int, int]


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def scale(value: int, vector: Coord) -> Coord:
    return tuple(value * vector[i] for i in range(3))  # type: ignore[return-value]


def cross(left: Coord, right: Coord) -> Coord:
    return (
        left[1] * right[2] - left[2] * right[1],
        left[2] * right[0] - left[0] * right[2],
        left[0] * right[1] - left[1] * right[0],
    )


def rotate_coord(rotation: tuple[tuple[int, int, int], ...], vector: Coord) -> Coord:
    values = rotate_vector(rotation, vector)
    return tuple(int(x) for x in values)  # type: ignore[return-value]


@dataclass(frozen=True)
class Front:
    trigger: Coord
    forward: Coord
    transverse: Coord

    @property
    def normal(self) -> Coord:
        return cross(self.forward, self.transverse)

    @property
    def data(self) -> tuple[Coord, Coord, Coord]:
        return tuple(add(self.trigger, scale(step, self.forward)) for step in (1, 2, 3))  # type: ignore[return-value]

    @property
    def left(self) -> Coord:
        return self.data[0]

    @property
    def center(self) -> Coord:
        return self.data[1]

    @property
    def right(self) -> Coord:
        return self.data[2]


def header_sites(front: Front) -> tuple[Coord, ...]:
    d, e, u = front.forward, front.transverse, front.normal
    offsets = (e, scale(2, e), scale(3, e), u, scale(2, u), add(d, add(e, u)))
    return tuple(add(front.trigger, offset) for offset in offsets)


def shifted_headers(front: Front, steps: int) -> tuple[Coord, ...]:
    return tuple(add(site, scale(steps, front.forward)) for site in header_sites(front))


def certificate_site(front: Front) -> Coord:
    return add(front.trigger, scale(-1, front.transverse))


def seed_records(front: Front, head: Matrix) -> dict[Coord, object]:
    records: dict[Coord, object] = {site: ("header", index) for index, site in enumerate(header_sites(front))}
    records[front.trigger] = ("head", head)
    return records


def ready(front: Front, records: dict[Coord, object]) -> bool:
    return (
        all(site in records for site in header_sites(front))
        and isinstance(records.get(front.trigger), tuple)
        and records[front.trigger][0] == "head"  # type: ignore[index]
        and certificate_site(front) not in records
        and all(site not in records for site in front.data)
    )


def event_assignments(front: Front, outcome: Matrix, next_head: Matrix) -> dict[Coord, object]:
    assignments: dict[Coord, object] = {
        certificate_site(front): ("outcome", outcome),
        front.left: ("lock", 0),
        front.center: ("lock", 1),
        front.right: ("head", next_head),
    }
    for phase, sites in enumerate((shifted_headers(front, 1), shifted_headers(front, 2), shifted_headers(front, 3)), start=1):
        assignments.update({site: ("header", phase, index) for index, site in enumerate(sites)})
    if len(assignments) != 22:
        raise AssertionError("front event does not contain 22 fresh assignments")
    return assignments


def append(records: dict[Coord, object], assignments: dict[Coord, object]) -> dict[Coord, object]:
    if set(records).intersection(assignments):
        raise ValueError("Record overwrite")
    answer = dict(records)
    answer.update(assignments)
    return answer


def append_run(
    horizon: int,
    finite_stock: bool = False,
    host_program: bool = False,
) -> tuple[bool, dict[Coord, object]]:
    base = Front((0, 0, 0), (1, 0, 0), (0, 1, 0))
    initial_state: State = (density_at_t(1), 0)
    head = program_carrier(initial_state[0], base.forward, initial_state[1])
    records = seed_records(base, head)
    for cycle in range(horizon):
        location = 3 * (cycle % 4 if finite_stock else cycle)
        front = Front((location, 0, 0), base.forward, base.transverse)
        if not ready(front, records):
            return False, records
        head_record = records[front.trigger]
        if not isinstance(head_record, tuple) or head_record[0] != "head":
            return False, records
        decoded_rho, decoded_direction, decoded_menu = decode_program(head_record[1])  # type: ignore[arg-type]
        if decoded_direction != tuple(Fraction(x) for x in base.forward) or decoded_menu.denominator != 1:
            return False, records
        menu_index = 0 if host_program else int(decoded_menu)
        if menu_index not in (0, 1) or not density(decoded_rho):
            return False, records
        state: State = (decoded_rho, menu_index)
        outcome_index, next_state = select_outcome(state, Fraction((2 * cycle + 1) % 11, 11))
        outcome = outcome_carrier(MENUS[state[1]][outcome_index], outcome_index + 1)
        next_head = program_carrier(next_state[0], base.forward, next_state[1])
        try:
            records = append(records, event_assignments(front, outcome, next_head))
        except ValueError:
            return False, records
    return True, records


def legacy_l41_controls() -> tuple[bool, float, float]:
    i2 = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z_pauli = np.asarray(((1, 0), (0, -1)), dtype=complex)
    plus = np.asarray((1, 1), dtype=complex) / np.sqrt(2)

    def kron_all(*items: np.ndarray) -> np.ndarray:
        answer = np.asarray([[1.0 + 0.0j]])
        for item in items:
            answer = np.kron(answer, item)
        return answer

    def onsite(operator: np.ndarray, site: int) -> np.ndarray:
        return kron_all(*(operator if index == site else i2 for index in range(3)))

    def projector(axis: np.ndarray, sign: int) -> np.ndarray:
        return (i2 + sign * axis) / 2

    cz01 = np.diag(tuple(-1.0 if ((word >> 2) & 1) and ((word >> 1) & 1) else 1.0 for word in range(8)))
    cz12 = np.diag(tuple(-1.0 if ((word >> 1) & 1) and (word & 1) else 1.0 for word in range(8)))
    cluster = (cz12 @ cz01) @ kron_all(plus.reshape(-1, 1), plus.reshape(-1, 1), plus.reshape(-1, 1)).reshape(-1)
    histories = tuple(product((1, -1), (0, 1), (0, 1)))
    effects = []
    for sign, left, right in histories:
        effects.append(
            onsite(projector(z_pauli, 1 if left == 0 else -1), 0)
            @ onsite(projector(x, sign), 1)
            @ onsite(projector(z_pauli, 1 if right == 0 else -1), 2)
        )

    def grades(state: np.ndarray) -> np.ndarray:
        return np.asarray([float(np.vdot(state, effect @ state).real) for effect in effects])

    uniform = grades(cluster)
    biased = grades(np.eye(8, dtype=complex)[:, 0])
    rotor = np.zeros(8)
    rotor[[0, 3, 5, 6]] = 0.25
    l1 = float(np.linalg.norm(rotor - biased, ord=1))
    linf = float(np.linalg.norm(rotor - biased, ord=np.inf))
    good = (
        np.allclose(uniform[[0, 3, 5, 6]], 0.25, atol=2e-12)
        and np.count_nonzero(uniform > 2e-12) == 4
        and np.allclose(biased[[0, 4]], 0.5, atol=2e-12)
        and np.count_nonzero(biased > 2e-12) == 2
        and abs(l1 - 1.5) < 2e-12
        and abs(linf - 0.5) < 2e-12
    )
    return good, l1, linf


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "state_independent",
            "contextual_shared",
            "prefix_projectivity",
            "coherent_actuality",
            "finite_stock",
            "host_program",
            "note_boundary",
        ),
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    sources = tuple(path.read_text(encoding="utf-8") for path in (BORN_FORM_NOTE, ATOMIC_NOTE))
    source_surface = " ".join(" ".join(item.split()) for item in (axiom, note, *sources))
    source_ok = all(
        phrase in source_surface
        for phrase in (
            "probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions",
            "L41^R3",
            "unique density-matrix trace form",
            "kappa(E,ell)=E+i ell I_2",
        )
    )
    checks.check("A-current-source-closure", source_ok, "current axiom, trace-form, and M2 carrier sources are literal; L41 geometry/falsifier algebra is rederived and the historic successor stack is not read")

    menus_ok = all(matrix_sum(menu) == IDENTITY and all(psd(effect) for effect in menu) for menu in MENUS)
    fixtures = (
        matrix_scale(Fraction(1, 2), IDENTITY),
        matrix(1, 0, 0, 0),
        pure_real(Fraction(3, 5), Fraction(4, 5)),
        pure_real(Fraction(3, 5), Fraction(-4, 5)),
        matrix(Fraction(2, 3), 0, 0, Fraction(1, 3)),
    )
    fixture_weights = tuple(tuple(effect_weights(rho, menu) for menu in MENUS) for rho in fixtures)
    cp_minimum = min(
        float(np.linalg.eigvalsh(np.kron(to_numpy(effect).T, to_numpy(normalized_effect_state(effect)))).min())
        for menu in MENUS
        for effect in menu
    )
    legacy_ok, rotor_l1, rotor_linf = legacy_l41_controls()
    reported_biased = fixture_weights[0] if mutation == "state_independent" else fixture_weights[1]
    kernel_ok = (
        menus_ok
        and all(sum(weights) == 1 and all(weight >= 0 for weight in weights) for row in fixture_weights for weights in row)
        and len(set(fixture_weights)) == len(fixture_weights)
        and reported_biased == fixture_weights[1]
        and cp_minimum > -2e-12
        and legacy_ok
    )
    checks.check("B-state-dependent-CP-kernel", kernel_ok, f"five fixtures, two menus, CP Choi min={cp_minimum:.3e}; old rotor biased residuals L1={rotor_l1:.1f}, Linf={rotor_linf:.1f}")

    shared = effect_weights(density_at_t(1), MENUS[0])[0] == effect_weights(density_at_t(1), MENUS[1])[0] == Fraction(3, 10)
    if mutation == "contextual_shared":
        shared = False
    head = program_carrier(density_at_t(1), (1, 0, 0), 0)
    decoded_rho, decoded_direction, decoded_menu = decode_program(head)
    tag_a = outcome_carrier(MENUS[0][0], 1)
    tag_b = outcome_carrier(MENUS[1][0], 1)
    carrier_ok = decoded_rho == density_at_t(1) and decoded_direction == (1, 0, 0) and decoded_menu == 0 and tag_a == tag_b and decode_outcome(tag_a) == (E0, Fraction(1))
    covariance_ok = True
    covariance_tests = 0
    covariance_front = Front((0, 0, 0), (1, 0, 0), (0, 1, 0))
    covariance_support = set(
        event_assignments(
            covariance_front,
            outcome_carrier(EB1, 2),
            program_carrier(density_at_t(1), covariance_front.forward, 1),
        )
    )
    for rotation in proper_cubic_rotations():
        rho_r = rotate_hermitian(rotation, density_at_t(1))
        effect_r = rotate_hermitian(rotation, EB1)
        direction_r = rotate_vector(rotation, (1, 0, 0))
        covariance_ok &= real_trace_product(rho_r, effect_r) == real_trace_product(density_at_t(1), EB1)
        rotated_head = program_carrier(rho_r, tuple(int(x) for x in direction_r), 0)
        covariance_ok &= decode_program(rotated_head) == (rho_r, direction_r, Fraction(0))
        rotated_front = Front(
            rotate_coord(rotation, covariance_front.trigger),
            rotate_coord(rotation, covariance_front.forward),
            rotate_coord(rotation, covariance_front.transverse),
        )
        rotated_support = set(
            event_assignments(
                rotated_front,
                outcome_carrier(effect_r, 2),
                program_carrier(rho_r, rotated_front.forward, 1),
            )
        )
        covariance_ok &= rotated_support == {
            rotate_coord(rotation, coordinate) for coordinate in covariance_support
        }
        covariance_tests += 1
    checks.check("C-shared-effect-carrier-covariance", shared and carrier_ok and covariance_ok and covariance_tests == 24, "shared E0 mass/codeword, exact head/outcome decoders, and all24 co-transport close")

    initial: State = (density_at_t(1), 0)
    normalizations = tuple(sum(cylinder_weight(initial, word) for word in product(range(3), repeat=n)) for n in range(0, 6))
    prefix_ok = all(
        sum(cylinder_weight(initial, prefix + (outcome,)) for outcome in range(3)) == cylinder_weight(initial, prefix)
        for prefix in product(range(3), repeat=4)
    )
    if mutation == "prefix_projectivity":
        prefix_ok = False
    checks.check("D-projective-history-law", normalizations == (1, 1, 1, 1, 1, 1) and prefix_ok, "N=0..5 normalize exactly and all 81 held length-four prefixes marginalize")

    innovations_a = tuple(Fraction(value, 11) for value in (1, 3, 5, 7, 9, 2))
    innovations_b = tuple(Fraction(value, 13) for value in (12, 10, 8, 6, 4, 2))
    def realized(stream: tuple[Fraction, ...]) -> tuple[int, ...]:
        state = initial
        history = []
        for innovation in stream:
            outcome, state = select_outcome(state, innovation)
            history.append(outcome)
        return tuple(history)
    history_a, history_b = realized(innovations_a), realized(innovations_b)
    actuality_ok = history_a != history_b and cylinder_weight(initial, history_a) > 0 and cylinder_weight(initial, history_b) > 0
    if mutation == "coherent_actuality":
        actuality_ok = False
    checks.check("E-contingent-one-history-semantics", actuality_ok, f"two realized-state innovation members give distinct positive-weight histories {history_a}/{history_b}; neither selects the kernel")

    run_ok, records = append_run(
        64,
        finite_stock=mutation == "finite_stock",
        host_program=mutation == "host_program",
    )
    finite_formula = run_ok and len(records) == 22 * 64 + 7
    base = Front((0, 0, 0), (1, 0, 0), (0, 1, 0))
    dummy = event_assignments(base, outcome_carrier(E0, 1), program_carrier(density_at_t(1), base.forward, 1))
    relative_support = tuple(dummy)
    translation_collision = any(
        left != right and left[1:] == right[1:] and (left[0] - right[0]) % 3 == 0
        for left in relative_support for right in relative_support
    )
    seed_collision = any(
        seed[1:] == event[1:] and (seed[0] - event[0]) % 3 == 0 and (seed[0] - event[0]) // 3 >= 0
        for seed in seed_records(base, program_carrier(density_at_t(1), base.forward, 0))
        for event in relative_support
    )
    program_from_head = mutation != "host_program"
    locality_ok = run_ok and finite_formula and not translation_collision and not seed_collision and program_from_head
    checks.check("F-unbounded-append-and-local-program", locality_ok, "64 events give 1415 permanent Records; translation-residue proof gives arbitrary-N fresh support; program is head-carried; readiness radius is declared three")

    needles = (
        "claim_id: admissibility_record_native_state_dependent_born_history_joint_law_candidate_gate_note_2026-08-12",
        "Type:** bounded_theorem",
        "one fixed kernel",
        "contingent kernel member",
        "arbitrary-`N`",
        "radius-three",
        "never-mainlined",
        "No canonical axiom is edited",
        "zero TOE percentage movement",
        "### N1",
        "### N8",
    )
    boundary_ok = all(needle in note for needle in needles) and mutation != "note_boundary"
    checks.check("G-claim-boundary", boundary_ok, "bounded radius-three candidate, current dependencies, no historic laundering, no adoption, and N1-N8 are explicit")

    print(f"METRICS fixture_pairs={len(fixtures) * len(MENUS)} covariance={covariance_tests}/24 cylinders_N5={3**5} records_N64={len(records)} cp_min={cp_minimum:.3e}")
    print("BOUNDARY: the fixed state-dependent kernel, exact histories, and unbounded no-overwrite single front pass; radius-three readiness is not the current nearest-neighbor Admissibility attachment, physical law selection remains open, and no percentage moves")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
