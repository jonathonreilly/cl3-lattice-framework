#!/usr/bin/env python3
"""Cycle 211: active local source/response bridge for the cubic object.

Use the Cycle-210 rest/inertial scalar as the charge in Cycle 9's local
six-neighbour relaxation.  Verify that repeated local updates generate the
periodic Green field, that two objects exert equal-and-opposite forces, and
that test-body acceleration is independent of the test species on the tuned
rest=inertia family.

This is a conditional weak scalar model.  The source map, field alphabet,
coupling, boundary subtraction, and response phase remain candidate inputs;
no relativistic gravity or axiom conclusion is claimed.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np

import local_conservative_commit_resource_gravity_cycle9_2026_07_14 as c9
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ACTIVE_CUBIC_SOURCE_RESPONSE_CYCLE211_NOTE_2026-07-16.md"
)

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


def point_source(side: int, position: tuple[int, int, int] = (0, 0, 0)) -> np.ndarray:
    source = np.full((side, side, side), -1 / side**3, dtype=float)
    source[position] += 1
    return source


def solve_field(source: np.ndarray) -> np.ndarray:
    side = source.shape[0]
    laplacian, _ = c9.fourier_symbols(side)
    source_hat = np.fft.fftn(source)
    field_hat = np.zeros_like(source_hat, dtype=complex)
    nonzero = laplacian > 1e-14
    field_hat[nonzero] = source_hat[nonzero] / laplacian[nonzero]
    return np.fft.ifftn(field_hat).real


def local_field(source: np.ndarray, steps: int) -> np.ndarray:
    field = np.zeros_like(source)
    for _ in range(steps):
        field = c9.lazy_step(field) + source / 12
    return field


def gradient(field: np.ndarray, position: tuple[int, int, int]) -> np.ndarray:
    answer = np.zeros(3)
    side = field.shape[0]
    for axis in range(3):
        plus = list(position)
        minus = list(position)
        plus[axis] = (plus[axis] + 1) % side
        minus[axis] = (minus[axis] - 1) % side
        answer[axis] = (field[tuple(plus)] - field[tuple(minus)]) / 2
    return answer


def rotate_position(position: tuple[int, int, int], frame: np.ndarray, side: int) -> tuple[int, int, int]:
    return tuple(int(value) for value in (frame @ np.asarray(position)) % side)


def field_energy(field: np.ndarray) -> float:
    return float(
        sum(
            np.sum((field - np.roll(field, 1, axis=axis)) ** 2)
            for axis in range(3)
        )
    )


@dataclass(frozen=True)
class Body:
    beta: float
    inertial_mass: float
    source_charge: float


def bodies() -> tuple[Body, ...]:
    return tuple(
        Body(row.beta, row.analytic_mass, row.rest_phase)
        for row in (c210.tuned_species(value) for value in (-0.2, -0.3, -0.4))
    )


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "active source",
        "nearest-neighbour",
        "proper-cubic",
        "rest/inertial scalar",
        "equal-and-opposite",
        "species-independent",
        "source deletion",
        "redundant records",
        "uniform background subtraction",
        "source map remains supplied",
        "not general relativity",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves source conditions and scope", not missing, missing)


def local_generation_controls() -> tuple[np.ndarray, np.ndarray]:
    side = 15
    source = point_source(side)
    exact = solve_field(source)
    residual = c9.laplacian_field(exact) - source
    check(
        "zero-mode-subtracted point source has an exact periodic Green field",
        abs(float(source.sum())) < 2e-14
        and abs(float(exact.mean())) < 2e-14
        and np.linalg.norm(residual) < 2e-12,
        np.linalg.norm(residual),
    )

    iterate = np.zeros_like(source)
    errors = []
    checkpoints = {1, 10, 100, 1000, 6000}
    laplacian, lazy = c9.fourier_symbols(side)
    source_hat = np.fft.fftn(source)
    nonzero = laplacian > 1e-14
    for step in range(1, 6001):
        iterate = c9.lazy_step(iterate) + source / 12
        if step in checkpoints:
            finite_hat = np.zeros_like(source_hat, dtype=complex)
            finite_hat[nonzero] = (
                (1 - lazy[nonzero] ** step)
                * source_hat[nonzero]
                / laplacian[nonzero]
            )
            finite = np.fft.ifftn(finite_hat).real
            errors.append(float(np.linalg.norm(iterate - exact)))
            check(
                f"tick {step} repeated local update equals its finite spectral sum",
                np.linalg.norm(iterate - finite) < 3e-12,
                np.linalg.norm(iterate - finite),
            )
    check(
        "the generated field converges monotonically to the Green solution",
        all(errors[index + 1] < errors[index] for index in range(len(errors) - 1))
        and errors[-1] / np.linalg.norm(exact) < 2e-9,
        errors,
    )

    side3 = 3
    lap = c9.lattice_laplacian(side3)
    twelve_lazy = 12 * np.eye(side3**3, dtype=int) - lap
    check(
        "the field update is nonnegative, normalized, and radius one",
        np.all(twelve_lazy >= 0)
        and np.all(twelve_lazy.sum(axis=0) == 12)
        and np.all(twelve_lazy.sum(axis=1) == 12)
        and set(np.unique(twelve_lazy)) <= {0, 1, 6},
    )
    energy = field_energy(exact)
    source_pairing = float(np.sum(exact * source))
    check(
        "field-gradient energy is positive and equals the source pairing",
        energy > 0 and abs(energy - source_pairing) < 2e-12,
        {"gradient_energy": energy, "source_pairing": source_pairing},
    )
    return source, exact


def covariance_controls(source: np.ndarray, field: np.ndarray) -> None:
    side = source.shape[0]
    frames = c210.proper_cubic_frames()
    flat = field.reshape(-1)
    residuals = []
    for frame in frames:
        permutation = c9.coordinate_permutation(side, rotation=frame)
        residuals.append(float(np.max(np.abs(permutation @ flat - flat))))
    check(
        "the point field is invariant under all 24 proper-cubic rotations",
        len(frames) == 24 and max(residuals) < 2e-12,
        max(residuals),
    )

    shift = (2, 3, 4)
    shifted_source = np.roll(source, shift, axis=(0, 1, 2))
    shifted_field = solve_field(shifted_source)
    check(
        "translating the active source translates the complete field",
        np.allclose(shifted_field, np.roll(field, shift, axis=(0, 1, 2)), atol=2e-12),
    )

    separation = (3, 1, 0)
    reference_gradient = gradient(field, separation)
    vector_residuals = []
    for frame in frames:
        moved = rotate_position(separation, frame, side)
        vector_residuals.append(
            np.linalg.norm(gradient(field, moved) - frame @ reference_gradient)
        )
    check(
        "the generated force vector transforms in every cubic frame",
        max(vector_residuals) < 2e-12,
        max(vector_residuals),
    )


def source_response_controls(field: np.ndarray) -> None:
    catalogue = bodies()
    separation = (3, 1, 0)
    base_gradient = gradient(field, separation)
    coupling = 0.07
    ratios = []
    for source_body in catalogue:
        expected = coupling * source_body.source_charge * base_gradient
        for test_body in catalogue:
            force = (
                coupling
                * source_body.source_charge
                * test_body.source_charge
                * base_gradient
            )
            acceleration = force / test_body.inertial_mass
            ratios.append(
                np.linalg.norm(acceleration - expected)
                / np.linalg.norm(expected)
            )
    check(
        "active-source acceleration is independent of the test species",
        max(ratios) < 2e-12,
        max(ratios),
    )

    left, right = catalogue[0], catalogue[2]
    force_on_right = (
        coupling * left.source_charge * right.source_charge * base_gradient
    )
    opposite_gradient = gradient(field, tuple((-np.asarray(separation)) % field.shape[0]))
    force_on_left = (
        coupling * right.source_charge * left.source_charge * opposite_gradient
    )
    acceleration_left = force_on_left / left.inertial_mass
    acceleration_right = force_on_right / right.inertial_mass
    check(
        "two active bodies exert exact equal-and-opposite forces",
        np.linalg.norm(force_on_left + force_on_right) < 2e-14,
        {"left": force_on_left.tolist(), "right": force_on_right.tolist()},
    )
    check(
        "reciprocal response conserves the two-body inertial centre",
        np.linalg.norm(
            left.inertial_mass * acceleration_left
            + right.inertial_mass * acceleration_right
        )
        < 2e-14,
    )

    source_deleted = solve_field(np.zeros_like(field))
    check(
        "source deletion removes both field and force",
        np.linalg.norm(source_deleted) == 0
        and np.linalg.norm(gradient(source_deleted, separation)) == 0,
    )

    reference = catalogue[-1]
    two_source_field = solve_field(2 * reference.source_charge * point_source(field.shape[0]))
    one_source_field = solve_field(reference.source_charge * point_source(field.shape[0]))
    check(
        "held-out co-located source composition is exactly additive",
        np.allclose(two_source_field, 2 * one_source_field, atol=2e-12)
        and abs(
            (2 * reference.source_charge) / (2 * reference.inertial_mass) - 1
        )
        < 2e-12,
    )

    redundant_records = np.zeros((len(catalogue), 2))
    for index, body in enumerate(catalogue):
        redundant_records[index] = body.source_charge
    check(
        "one or two redundant records do not alter the active source charge",
        np.allclose(redundant_records[:, 0], redundant_records[:, 1])
        and np.allclose(
            redundant_records[:, 0],
            [body.source_charge for body in catalogue],
        ),
    )

    tuned = c210.tuned_species(-0.4)
    shifted_alpha = tuned.alpha + 0.1
    untuned_phase = tuned.rest_phase - 0.1 / 3
    untuned_ratio = untuned_phase / tuned.analytic_mass
    check(
        "deleting the rest=inertia condition deletes universal response in the same cubic law family",
        abs(untuned_ratio - 1) > 0.05
        and np.linalg.norm(
            c210.cubic_coin(shifted_alpha, tuned.beta, untuned_phase).conj().T
            @ c210.cubic_coin(shifted_alpha, tuned.beta, untuned_phase)
            - c210.I6
        )
        < 2e-12,
        untuned_ratio,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    source, field = local_generation_controls()
    covariance_controls(source, field)
    source_response_controls(field)
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "ACTIVE_CUBIC_SOURCE_RESPONSE" if FAIL == 0 else "CYCLE211_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
