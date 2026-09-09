#!/usr/bin/env python3
"""Cycle 216: exact Green kernel from static exchange of the finite coin.

Hermitianize the Cycle-214/215 field walk as K=2I-U-U^dagger.  Prove and test
that the scalar-source block of K^+ is exactly 3 L^+, where L is the cubic
graph Laplacian.  Couple Cycle-210 objects through one local scalar vertex and
test the resulting pair potential, molecular acceleration, covariance,
composition, and untuned controls.

The quadratic action/effective-exchange interpretation and coupling remain
supplied candidate physics.  This is not general relativity, a dynamical
radiation theory, or an axiom conclusion.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import finite_coin_scalar_wave_dilation_cycle215_2026_07_16 as c215
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "VIRTUAL_EXCHANGE_GREEN_KERNEL_CYCLE216_NOTE_2026-07-16.md"
)

COUPLING = 0.08
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def walk(momentum: np.ndarray) -> np.ndarray:
    stream = np.diag(np.exp(-1j * (c210.DIRECTIONS @ momentum)))
    return stream @ c214.FIELD_COIN


def stiffness(momentum: np.ndarray) -> np.ndarray:
    unitary = walk(momentum)
    return 2 * np.eye(6) - unitary - unitary.conj().T


def laplacian_symbol(momentum: np.ndarray) -> float:
    return float(6 - 2 * np.sum(np.cos(momentum)))


def inverse_field_step(state: np.ndarray) -> np.ndarray:
    unstreamed = np.zeros_like(state)
    for direction in range(6):
        shift = tuple(-int(value) for value in c210.DIRECTIONS[direction])
        unstreamed[..., direction] = np.roll(
            state[..., direction], shift, axis=(0, 1, 2)
        )
    return np.einsum(
        "ab,xyzb->xyza",
        c214.FIELD_COIN.conj().T,
        unstreamed,
        optimize=True,
    )


def apply_stiffness(state: np.ndarray) -> np.ndarray:
    return 2 * state - c215.field_step(state) - inverse_field_step(state)


def solve_coin_field(source: np.ndarray) -> np.ndarray:
    side = source.shape[0]
    source_hat = np.fft.fftn(source, norm="ortho")
    field_hat = np.zeros(source.shape + (6,), dtype=complex)
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    for indices in product(range(side), repeat=3):
        momentum = np.asarray([momenta[index] for index in indices])
        local_source = source_hat[indices]
        if abs(local_source) < 1e-15:
            continue
        field_hat[indices] = (
            np.linalg.pinv(stiffness(momentum), rcond=1e-11)
            @ c210.UNIFORM
            * local_source
        )
    return np.fft.ifftn(field_hat, axes=(0, 1, 2), norm="ortho")


def scalar_field(field: np.ndarray) -> np.ndarray:
    return np.einsum("d,xyzd->xyz", c210.UNIFORM.conj(), field, optimize=True)


def rotate_field_state(state: np.ndarray, frame: np.ndarray) -> np.ndarray:
    return c215.rotate_field_state(state, frame)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "static virtual exchange",
        "k=2i-u-u^dagger",
        "exactly 3 l^+",
        "local quadratic action",
        "vacuum-relative mass scalar",
        "species-independent molecular response",
        "proper-cubic",
        "uniform background subtraction",
        "effective-action interpretation remains supplied",
        "not general relativity",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves mechanism, attribution, and scope", not missing, missing)


def exact_mode_controls() -> None:
    rng = np.random.default_rng(216)
    rows = []
    for _ in range(64):
        momentum = rng.uniform(-2.8, 2.8, size=3)
        local_stiffness = stiffness(momentum)
        laplacian = laplacian_symbol(momentum)
        scalar_inverse = float(
            np.vdot(
                c210.UNIFORM,
                np.linalg.pinv(local_stiffness, rcond=1e-11) @ c210.UNIFORM,
            ).real
        )
        eigenvalues, eigenvectors = np.linalg.eigh(local_stiffness)
        null_overlap = max(
            (
                abs(np.vdot(c210.UNIFORM, eigenvectors[:, index]))
                for index, value in enumerate(eigenvalues)
                if abs(value) < 2e-10
            ),
            default=0.0,
        )
        rows.append(
            (
                abs(scalar_inverse / (3 / laplacian) - 1),
                float(np.min(eigenvalues)),
                float(null_overlap),
            )
        )
    check(
        "every held-out mode has <s|K^+|s> = 3/L exactly",
        max(row[0] for row in rows) < 8e-13,
        max(row[0] for row in rows),
    )
    check(
        "K is positive semidefinite and scalar sources miss its flat null modes",
        min(row[1] for row in rows) > -3e-12
        and max(row[2] for row in rows) < 3e-12,
        {
            "minimum_eigenvalue": min(row[1] for row in rows),
            "maximum_null_overlap": max(row[2] for row in rows),
        },
    )

    frames = c210.proper_cubic_frames()
    momentum = np.array((0.41, -0.23, 0.17))
    covariance = []
    for frame in frames:
        representation = c210.direction_permutation(frame)
        covariance.append(
            np.linalg.norm(
                stiffness(frame @ momentum)
                - representation
                @ stiffness(momentum)
                @ representation.conj().T
            )
        )
    check(
        "the complete stiffness transforms in all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 3e-12,
        max(covariance),
    )

    random_state = rng.normal(size=(9, 9, 9, 6)) + 1j * rng.normal(
        size=(9, 9, 9, 6)
    )
    local_output = apply_stiffness(random_state)
    source = np.zeros_like(random_state)
    source[0, 0, 0] = c210.UNIFORM
    point_output = apply_stiffness(source)
    coordinates = np.indices((9, 9, 9))
    signed = np.minimum(coordinates, 9 - coordinates)
    manhattan = np.sum(signed, axis=0)
    check(
        "the Hermitian stiffness is a radius-one local operator",
        np.max(np.abs(point_output[manhattan > 1])) < 2e-15,
    )
    check(
        "the local quadratic form is real and nonnegative on held-out states",
        abs(np.vdot(random_state, local_output).imag) < 2e-11
        and np.vdot(random_state, local_output).real > 0,
        np.vdot(random_state, local_output),
    )


def position_space_controls() -> tuple[np.ndarray, np.ndarray]:
    side = 15
    source = c211.point_source(side)
    field = solve_coin_field(source)
    scalar = scalar_field(field).real
    green = c211.solve_field(source)
    residual = apply_stiffness(field) - source[..., None] * c210.UNIFORM
    check(
        "the generated coin field solves K Psi = rho |s> on the zero-mean source domain",
        np.linalg.norm(residual) < 2e-11,
        np.linalg.norm(residual),
    )
    check(
        "the scalar projection of the coin field is exactly three Green fields",
        np.linalg.norm(scalar - 3 * green) < 2e-11,
        np.linalg.norm(scalar - 3 * green),
    )
    stiffness_energy = float(np.vdot(field, apply_stiffness(field)).real)
    source_pairing = float(np.sum(source * scalar))
    check(
        "the on-shell positive stiffness equals the scalar source pairing",
        stiffness_energy > 0
        and abs(stiffness_energy - source_pairing) < 2e-11,
        {"stiffness": stiffness_energy, "source_pairing": source_pairing},
    )

    covariance = []
    for frame in c210.proper_cubic_frames():
        covariance.append(
            np.linalg.norm(rotate_field_state(field, frame) - field)
        )
    check(
        "the point-source coin field is invariant in all cubic frames",
        max(covariance) < 2e-11,
        max(covariance),
    )
    return scalar, green


def asymptotic_and_exchange_controls() -> tuple[np.ndarray, np.ndarray]:
    side = 41
    source = c211.point_source(side)
    green = c211.solve_field(source)
    kernel = 3 * green
    radii = np.arange(4, 13)
    samples = np.asarray([kernel[radius, 0, 0] for radius in radii])
    design = np.column_stack((np.ones(len(radii)), 1 / radii))
    offset, coefficient = np.linalg.lstsq(design, samples, rcond=None)[0]
    predicted = offset + coefficient / radii
    r_squared = 1 - np.sum((samples - predicted) ** 2) / np.sum(
        (samples - np.mean(samples)) ** 2
    )
    target = 3 / (4 * np.pi)
    check(
        "the static exchange kernel has the cubic 1/r exterior profile",
        r_squared > 0.9994 and abs(coefficient / target - 1) < 0.01,
        {
            "offset": offset,
            "coefficient": coefficient,
            "target": target,
            "R2": r_squared,
        },
    )

    separation = (4, 0, 0)
    left = c210.tuned_species(-0.2)
    right = c210.tuned_species(-0.4)
    left_charge = c213.rest_charge(left.coin, c210.P_SCALAR)
    right_charge = c213.rest_charge(right.coin, c210.P_SCALAR)
    gradient_right = c211.gradient(kernel, separation)
    opposite = tuple((-np.asarray(separation)) % side)
    gradient_left = c211.gradient(kernel, opposite)
    force_on_right = COUPLING**2 * left_charge * right_charge * gradient_right
    force_on_left = COUPLING**2 * left_charge * right_charge * gradient_left
    check(
        "static virtual exchange gives equal-and-opposite pair forces",
        np.linalg.norm(force_on_left + force_on_right) < 2e-14
        and np.linalg.norm(force_on_right) > 1e-8,
        {"left": force_on_left.tolist(), "right": force_on_right.tolist()},
    )
    potential_lr = -COUPLING**2 * left_charge * right_charge * kernel[separation]
    potential_rl = -COUPLING**2 * right_charge * left_charge * kernel[opposite]
    check(
        "the pair potential is symmetric and has the attractive -q1 q2/r sign",
        abs(potential_lr - potential_rl) < 2e-14 and potential_lr < 0,
        (potential_lr, potential_rl),
    )
    return kernel, gradient_right


def molecular_response_controls(kernel: np.ndarray, gradient_at_probe: np.ndarray) -> None:
    species_set = tuple(c210.tuned_species(beta) for beta in (-0.2, -0.3, -0.4))
    source_species = species_set[-1]
    source_charge = c213.rest_charge(source_species.coin, c210.P_SCALAR)
    rows = []
    for species in species_set:
        test_charge = c213.rest_charge(species.coin, c210.P_SCALAR)
        force = (
            COUPLING**2
            * source_charge
            * test_charge
            * gradient_at_probe[0]
        )
        response = c210.force_response(species, force)
        expected_acceleration = -COUPLING**2 * source_charge * gradient_at_probe[0]
        rows.append(
            (
                species.beta,
                response.measured_mass,
                response.acceleration / expected_acceleration,
                response.band_probability,
            )
        )
    check(
        "static exchange gives species-independent molecular response",
        max(abs(row[2] - 1) for row in rows) < 0.007
        and min(row[3] for row in rows) > 0.999,
        rows,
    )

    charges = np.asarray(
        [c213.rest_charge(species.coin, c210.P_SCALAR) for species in species_set]
    )
    combined = np.sum(charges) * kernel
    separate = sum(charge * kernel for charge in charges)
    check(
        "held-out source composition is additive under one exchange kernel",
        np.max(np.abs(combined - separate)) < 2e-14,
    )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    archived = (
        source_charge,
        source_charge * np.vdot(record_zero, record_zero).real,
        source_charge
        * np.vdot(record_zero, record_zero).real
        * np.vdot(record_plus, record_plus).real,
    )
    check(
        "redundant spectator records do not multiply static exchange charge",
        max(abs(value - source_charge) for value in archived) < 2e-14,
        archived,
    )

    untuned = []
    for species in species_set:
        shifted_coin = c210.cubic_coin(
            species.alpha + 0.1,
            species.beta,
            species.rest_phase - 0.1 / 3,
        )
        charge = c213.rest_charge(shifted_coin, c210.P_SCALAR)
        untuned.append(charge / species.analytic_mass)
    check(
        "detuning rest charge from inertia breaks exchange universality",
        max(untuned) - min(untuned) > 0.05,
        untuned,
    )

    deleted_force = 0.0 * source_charge * gradient_at_probe[0]
    deleted_response = c210.force_response(source_species, deleted_force)
    check(
        "coupling deletion removes molecular acceleration without deleting the body",
        abs(deleted_response.acceleration) < 2e-12
        and deleted_response.band_probability > 1 - 2e-12,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    exact_mode_controls()
    position_space_controls()
    kernel, gradient_at_probe = asymptotic_and_exchange_controls()
    molecular_response_controls(kernel, gradient_at_probe)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
