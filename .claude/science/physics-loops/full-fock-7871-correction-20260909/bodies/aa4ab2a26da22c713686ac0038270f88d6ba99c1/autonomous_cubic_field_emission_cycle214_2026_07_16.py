#!/usr/bin/env python3
"""Cycle 214: autonomous finite-alphabet cubic field emission.

Extend the Cycle-210 bound-object sector by a zero/one-field direct sum.  The
same onsite unitary at every occupied body site mixes the no-field scalar
object with an object plus a six-direction acoustic field carrier.  Coins and
one-edge streams then propagate both carriers.  The construction is unitary,
translation invariant, proper-cubic, reversible, and needs no external source
schedule.

This is a one-field-sector candidate, not a quantum theory of gravity.  The
field coin, number-changing vertex, vacuum reference, and charge-to-angle map
are supplied.  No static Green sector, many-field limit, Born rule, record
formation, or axiom conclusion is claimed.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np

import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "AUTONOMOUS_CUBIC_FIELD_EMISSION_CYCLE214_NOTE_2026-07-16.md"
)

FIELD_COIN = c210.P_SCALAR + c210.P_VECTOR - c210.P_EVEN
PAIR_SCALAR = np.outer(c210.UNIFORM, c210.UNIFORM)
COUPLING = 0.4

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


def vertex_matrix(angle: float) -> np.ndarray:
    return np.asarray(
        (
            (np.cos(angle), 1j * np.sin(angle)),
            (1j * np.sin(angle), np.cos(angle)),
        ),
        dtype=complex,
    )


def apply_vertex(
    source: np.ndarray,
    contact_pair: np.ndarray,
    angle: float,
    *,
    inverse: bool = False,
) -> tuple[np.ndarray, np.ndarray]:
    source_amplitude = np.vdot(c210.UNIFORM, source)
    pair_amplitude = np.vdot(PAIR_SCALAR, contact_pair)
    matrix = vertex_matrix(angle)
    if inverse:
        matrix = matrix.conj().T
    new_source, new_pair = matrix @ np.asarray((source_amplitude, pair_amplitude))
    source_output = source + (new_source - source_amplitude) * c210.UNIFORM
    pair_output = contact_pair + (new_pair - pair_amplitude) * PAIR_SCALAR
    return source_output, pair_output


def relative_stream(
    pair: np.ndarray, total_momentum: np.ndarray, *, inverse: bool = False
) -> np.ndarray:
    output = np.zeros_like(pair)
    for body_direction, field_direction in product(range(6), repeat=2):
        shift = tuple(
            int(value)
            for value in (
                c210.DIRECTIONS[field_direction]
                - c210.DIRECTIONS[body_direction]
            )
        )
        phase = np.exp(
            -1j
            * float(total_momentum @ c210.DIRECTIONS[body_direction])
        )
        if inverse:
            output[..., body_direction, field_direction] = (
                phase.conjugate()
                * np.roll(
                    pair[..., body_direction, field_direction],
                    tuple(-value for value in shift),
                    axis=(0, 1, 2),
                )
            )
        else:
            output[..., body_direction, field_direction] = phase * np.roll(
                pair[..., body_direction, field_direction],
                shift,
                axis=(0, 1, 2),
            )
    return output


def source_stream(
    source: np.ndarray, total_momentum: np.ndarray, *, inverse: bool = False
) -> np.ndarray:
    phases = np.exp(-1j * (c210.DIRECTIONS @ total_momentum))
    return source * (phases.conj() if inverse else phases)


def relative_step(
    source: np.ndarray,
    pair: np.ndarray,
    species: c210.Species,
    angle: float,
    total_momentum: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    if total_momentum is None:
        total_momentum = np.zeros(3)
    coined_source = species.coin @ source
    coined_pair = np.einsum(
        "ab,cd,xyzbd->xyzac",
        species.coin,
        FIELD_COIN,
        pair,
        optimize=True,
    )
    coined_source, coined_pair[0, 0, 0] = apply_vertex(
        coined_source, coined_pair[0, 0, 0], angle
    )
    return (
        source_stream(coined_source, total_momentum),
        relative_stream(coined_pair, total_momentum),
    )


def inverse_relative_step(
    source: np.ndarray,
    pair: np.ndarray,
    species: c210.Species,
    angle: float,
    total_momentum: np.ndarray | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    if total_momentum is None:
        total_momentum = np.zeros(3)
    unstreamed_source = source_stream(source, total_momentum, inverse=True)
    unstreamed_pair = relative_stream(pair, total_momentum, inverse=True)
    unstreamed_source, unstreamed_pair[0, 0, 0] = apply_vertex(
        unstreamed_source, unstreamed_pair[0, 0, 0], angle, inverse=True
    )
    return (
        species.coin.conj().T @ unstreamed_source,
        np.einsum(
            "ab,cd,xyzbd->xyzac",
            species.coin.conj().T,
            FIELD_COIN.conj().T,
            unstreamed_pair,
            optimize=True,
        ),
    )


def norm(source: np.ndarray, pair: np.ndarray) -> float:
    return float(np.vdot(source, source).real + np.vdot(pair, pair).real)


def rotate_pair(pair: np.ndarray, frame: np.ndarray) -> np.ndarray:
    side = pair.shape[0]
    coordinates = np.indices(pair.shape[:3]).reshape(3, -1)
    moved = (frame @ coordinates) % side
    spatial = np.empty_like(pair)
    spatial[moved[0], moved[1], moved[2]] = pair.reshape(
        -1, pair.shape[3], pair.shape[4]
    )
    representation = c210.direction_permutation(frame)
    return np.einsum(
        "ab,cd,xyzbd->xyzac",
        representation,
        representation,
        spatial,
        optimize=True,
    )


def rotate_source(source: np.ndarray, frame: np.ndarray) -> np.ndarray:
    return c210.direction_permutation(frame) @ source


def full_step(
    source: np.ndarray,
    pair: np.ndarray,
    species: c210.Species,
    angle: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Literal position-space law in the body plus zero/one-field sector."""
    coined_source = np.einsum("ab,xyzb->xyza", species.coin, source, optimize=True)
    coined_pair = np.einsum(
        "ab,cd,ijklmnbd->ijklmnac",
        species.coin,
        FIELD_COIN,
        pair,
        optimize=True,
    )
    side = source.shape[0]
    for position in product(range(side), repeat=3):
        contact = position + position
        coined_source[position], coined_pair[contact] = apply_vertex(
            coined_source[position], coined_pair[contact], angle
        )

    streamed_source = np.zeros_like(coined_source)
    for body_direction in range(6):
        shift = tuple(int(value) for value in c210.DIRECTIONS[body_direction])
        streamed_source[..., body_direction] = np.roll(
            coined_source[..., body_direction], shift, axis=(0, 1, 2)
        )

    streamed_pair = np.zeros_like(coined_pair)
    for body_direction, field_direction in product(range(6), repeat=2):
        body_shift = tuple(int(value) for value in c210.DIRECTIONS[body_direction])
        field_shift = tuple(int(value) for value in c210.DIRECTIONS[field_direction])
        streamed_pair[..., body_direction, field_direction] = np.roll(
            coined_pair[..., body_direction, field_direction],
            body_shift + field_shift,
            axis=(0, 1, 2, 3, 4, 5),
        )
    return streamed_source, streamed_pair


def lift_momentum(
    source: np.ndarray,
    pair: np.ndarray,
    total_momentum: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    side = pair.shape[0]
    volume = side**3
    full_source = np.zeros((side, side, side, 6), dtype=complex)
    full_pair = np.zeros((side,) * 6 + (6, 6), dtype=complex)
    for body_position in product(range(side), repeat=3):
        phase = np.exp(1j * float(total_momentum @ np.asarray(body_position)))
        full_source[body_position] = phase * source / np.sqrt(volume)
        for relative_position in product(range(side), repeat=3):
            field_position = tuple(
                (body_position[axis] + relative_position[axis]) % side
                for axis in range(3)
            )
            full_pair[body_position + field_position] = (
                phase * pair[relative_position] / np.sqrt(volume)
            )
    return full_source, full_pair


def extract_momentum(
    source: np.ndarray,
    pair: np.ndarray,
    total_momentum: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    side = source.shape[0]
    volume = side**3
    reduced_source = np.zeros(6, dtype=complex)
    reduced_pair = np.zeros((side, side, side, 6, 6), dtype=complex)
    for body_position in product(range(side), repeat=3):
        phase = np.exp(-1j * float(total_momentum @ np.asarray(body_position)))
        reduced_source += phase * source[body_position] / np.sqrt(volume)
        for relative_position in product(range(side), repeat=3):
            field_position = tuple(
                (body_position[axis] + relative_position[axis]) % side
                for axis in range(3)
            )
            reduced_pair[relative_position] += (
                phase
                * pair[body_position + field_position]
                / np.sqrt(volume)
            )
    return reduced_source, reduced_pair


def translate_full(
    source: np.ndarray, pair: np.ndarray, shift: tuple[int, int, int]
) -> tuple[np.ndarray, np.ndarray]:
    return (
        np.roll(source, shift, axis=(0, 1, 2)),
        np.roll(pair, shift + shift, axis=(0, 1, 2, 3, 4, 5)),
    )


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "autonomous finite-alphabet",
        "zero/one-field sector",
        "acoustic field carrier",
        "same onsite vertex",
        "external source history",
        "proper-cubic",
        "vacuum-relative mass scalar",
        "body recoil",
        "static green sector remains open",
        "global novelty has not been established",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves mechanism, attribution, and scope", not missing, missing)


def acoustic_field_controls() -> None:
    check(
        "the six-direction acoustic coin is exactly unitary",
        np.linalg.norm(FIELD_COIN.conj().T @ FIELD_COIN - np.eye(6)) < 2e-12,
    )
    covariance = []
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        covariance.append(
            np.linalg.norm(
                representation @ FIELD_COIN @ representation.conj().T - FIELD_COIN
            )
        )
    check(
        "the field coin commutes with all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 2e-12,
        max(covariance),
    )

    step = 1e-4
    directions = (
        np.array((1.0, 0.0, 0.0)),
        np.array((1.0, 1.0, 0.0)) / np.sqrt(2),
        np.array((1.0, 1.0, 1.0)) / np.sqrt(3),
        np.array((2.0, -1.0, 3.0)) / np.sqrt(14),
    )
    slopes = []
    for direction in directions:
        momentum = step * direction
        walk = np.diag(
            np.exp(-1j * (c210.DIRECTIONS @ momentum))
        ) @ FIELD_COIN
        phases = np.angle(np.linalg.eigvals(walk))
        positive = min(value for value in phases if value > 1e-8)
        slopes.append(float(positive / step))
    check(
        "the scalar/longitudinal field pair has an isotropic acoustic slope 1/sqrt(3)",
        max(abs(value - 1 / np.sqrt(3)) for value in slopes) < 2e-8,
        slopes,
    )
    check(
        "the source and pair scalar vectors are normalized cubic singlets",
        abs(np.linalg.norm(c210.UNIFORM) - 1) < 2e-12
        and abs(np.linalg.norm(PAIR_SCALAR) - 1) < 2e-12
        and all(
            np.linalg.norm(
                c210.direction_permutation(frame)
                @ c210.UNIFORM
                - c210.UNIFORM
            )
            < 2e-12
            for frame in c210.proper_cubic_frames()
        ),
    )


def literal_local_law_controls() -> None:
    rng = np.random.default_rng(214)
    side = 3
    species = c210.tuned_species(-0.35)
    angle = COUPLING * c213.rest_charge(species.coin, c210.P_SCALAR)
    source = rng.normal(size=(side, side, side, 6)) + 1j * rng.normal(
        size=(side, side, side, 6)
    )
    pair = rng.normal(size=(side,) * 6 + (6, 6)) + 1j * rng.normal(
        size=(side,) * 6 + (6, 6)
    )
    scale = np.sqrt(np.vdot(source, source).real + np.vdot(pair, pair).real)
    source, pair = source / scale, pair / scale
    next_source, next_pair = full_step(source, pair, species, angle)
    check(
        "the literal full-position local law preserves total probability",
        abs(
            np.vdot(next_source, next_source).real
            + np.vdot(next_pair, next_pair).real
            - 1
        )
        < 3e-12,
    )

    shift = (1, 2, 0)
    shifted_source, shifted_pair = translate_full(source, pair, shift)
    shifted_next = full_step(shifted_source, shifted_pair, species, angle)
    translated_next = translate_full(next_source, next_pair, shift)
    check(
        "one identical onsite law at every site commutes with lattice translation",
        np.max(np.abs(shifted_next[0] - translated_next[0])) < 2e-13
        and np.max(np.abs(shifted_next[1] - translated_next[1])) < 2e-13,
    )

    reduced_source = rng.normal(size=6) + 1j * rng.normal(size=6)
    reduced_pair = rng.normal(size=(side, side, side, 6, 6)) + 1j * rng.normal(
        size=(side, side, side, 6, 6)
    )
    reduced_scale = np.sqrt(norm(reduced_source, reduced_pair))
    reduced_source, reduced_pair = (
        reduced_source / reduced_scale,
        reduced_pair / reduced_scale,
    )
    block_residuals = []
    for total_momentum in (
        np.zeros(3),
        2 * np.pi * np.array((1, -1, 0)) / side,
    ):
        full_source, full_pair = lift_momentum(
            reduced_source, reduced_pair, total_momentum
        )
        full_output = full_step(full_source, full_pair, species, angle)
        extracted = extract_momentum(*full_output, total_momentum)
        relative_output = relative_step(
            reduced_source, reduced_pair, species, angle, total_momentum
        )
        block_residuals.append(
            max(
                float(np.max(np.abs(extracted[0] - relative_output[0]))),
                float(np.max(np.abs(extracted[1] - relative_output[1]))),
            )
        )
    check(
        "the relative law exactly matches literal K=0 and held-out K blocks",
        max(block_residuals) < 2e-12,
        block_residuals,
    )

    covariance_source = rng.normal(size=6) + 1j * rng.normal(size=6)
    covariance_pair = rng.normal(size=(5, 5, 5, 6, 6)) + 1j * rng.normal(
        size=(5, 5, 5, 6, 6)
    )
    covariance_scale = np.sqrt(norm(covariance_source, covariance_pair))
    covariance_source /= covariance_scale
    covariance_pair /= covariance_scale
    covariance_output = relative_step(
        covariance_source, covariance_pair, species, angle
    )
    covariance_residuals = []
    for frame in c210.proper_cubic_frames():
        rotated_output = relative_step(
            rotate_source(covariance_source, frame),
            rotate_pair(covariance_pair, frame),
            species,
            angle,
        )
        covariance_residuals.append(
            max(
                np.linalg.norm(
                    rotated_output[0] - rotate_source(covariance_output[0], frame)
                ),
                np.linalg.norm(
                    rotated_output[1] - rotate_pair(covariance_output[1], frame)
                ),
            )
        )
    check(
        "the autonomous law commutes with all cubic frames on an arbitrary state",
        max(covariance_residuals) < 3e-12,
        max(covariance_residuals),
    )


def autonomous_emission_controls() -> None:
    side = 31
    zero_pair = np.zeros((side, side, side, 6, 6), dtype=complex)
    species_set = tuple(c210.tuned_species(beta) for beta in (-0.2, -0.3, -0.4))
    first_tick_rows = []
    for species in species_set:
        charge = c213.rest_charge(species.coin, c210.P_SCALAR)
        angle = COUPLING * charge
        source, pair = relative_step(
            c210.UNIFORM.copy(), zero_pair.copy(), species, angle
        )
        pair_probability = float(np.vdot(pair, pair).real)
        first_tick_rows.append((species.beta, charge, angle, pair_probability))
        check(
            f"beta={species.beta} autonomous one-tick emission is sin^2(g Q)",
            abs(pair_probability - np.sin(angle) ** 2) < 2e-12
            and abs(norm(source, pair) - 1) < 2e-12,
            first_tick_rows[-1],
        )

    reference = species_set[-1]
    charge = c213.rest_charge(reference.coin, c210.P_SCALAR)
    angle = COUPLING * charge
    source = c210.UNIFORM.copy()
    pair = zero_pair.copy()
    history = [(source.copy(), pair.copy())]
    support_rows = []
    coordinates = np.indices((side, side, side))
    signed = np.minimum(coordinates, side - coordinates)
    manhattan = np.sum(signed, axis=0)
    for tick in range(1, 8):
        source, pair = relative_step(source, pair, reference, angle)
        history.append((source.copy(), pair.copy()))
        probability = np.sum(np.abs(pair) ** 2, axis=(3, 4))
        outside = float(np.max(probability[manhattan > 2 * tick]))
        support_rows.append(
            (
                tick,
                float(np.vdot(source, source).real),
                float(np.vdot(pair, pair).real),
                outside,
            )
        )
    check(
        "the same autonomous unitary emits, propagates, and can reabsorb without a source schedule",
        all(abs(row[1] + row[2] - 1) < 3e-12 for row in support_rows)
        and max(row[3] for row in support_rows) < 2e-15
        and max(row[2] for row in support_rows) > 0.15,
        support_rows,
    )
    check(
        "relative separation grows by at most two edges because each carrier moves one edge",
        max(row[3] for row in support_rows) < 2e-15,
        support_rows,
    )

    for _ in range(7):
        source, pair = inverse_relative_step(source, pair, reference, angle)
    check(
        "reversing the seven identical local ticks restores body plus field vacuum",
        np.linalg.norm(source - c210.UNIFORM) < 3e-12
        and np.linalg.norm(pair) < 3e-12,
    )

    recurrence_side = 15
    recurrence_source = c210.UNIFORM.copy()
    recurrence_pair = np.zeros(
        (recurrence_side, recurrence_side, recurrence_side, 6, 6), dtype=complex
    )
    recurrence_probabilities = []
    for _ in range(40):
        recurrence_source, recurrence_pair = relative_step(
            recurrence_source, recurrence_pair, reference, angle
        )
        recurrence_probabilities.append(
            float(np.vdot(recurrence_source, recurrence_source).real)
        )
    minimum_index = int(np.argmin(recurrence_probabilities))
    check(
        "the forward finite-volume history contains coherent field reabsorption",
        minimum_index < len(recurrence_probabilities) - 5
        and max(recurrence_probabilities[minimum_index + 1 :])
        > 20 * recurrence_probabilities[minimum_index],
        {
            "minimum_tick": minimum_index + 1,
            "minimum_source_probability": recurrence_probabilities[minimum_index],
            "later_maximum": max(recurrence_probabilities[minimum_index + 1 :]),
        },
    )

    deleted_source = c210.UNIFORM.copy()
    deleted_pair = zero_pair.copy()
    for _ in range(7):
        deleted_source, deleted_pair = relative_step(
            deleted_source, deleted_pair, reference, 0.0
        )
    check(
        "deleting the number-changing vertex leaves the field vacuum exact",
        np.linalg.norm(deleted_pair) < 2e-12
        and abs(np.vdot(deleted_source, deleted_source).real - 1) < 2e-12,
    )

    source = c210.UNIFORM.copy()
    pair = zero_pair.copy()
    for _ in range(7):
        source, pair = relative_step(source, pair, reference, angle)
    rotation_residuals = []
    for frame in c210.proper_cubic_frames():
        rotation_residuals.append(
            max(
                np.linalg.norm(rotate_source(source, frame) - source),
                np.linalg.norm(rotate_pair(pair, frame) - pair),
            )
        )
    check(
        "an invariant source history remains invariant in all 24 cubic frames",
        max(rotation_residuals) < 3e-12,
        max(rotation_residuals),
    )

    momentum = np.array((0.17, -0.11, 0.07))
    source_k = c210.UNIFORM.copy()
    pair_k = zero_pair.copy()
    for _ in range(5):
        source_k, pair_k = relative_step(
            source_k, pair_k, reference, angle, momentum
        )
    check(
        "a held-out nonzero-total-momentum block is normalized and dynamically populated",
        abs(norm(source_k, pair_k) - 1) < 3e-12
        and np.vdot(pair_k, pair_k).real > 0.05,
        {
            "source": float(np.vdot(source_k, source_k).real),
            "field": float(np.vdot(pair_k, pair_k).real),
        },
    )

    pair_fourier = np.fft.fftn(pair_k, axes=(0, 1, 2), norm="ortho")
    weights = np.sum(np.abs(pair_fourier) ** 2, axis=(3, 4))
    momenta = 2 * np.pi * np.fft.fftfreq(side)
    grids = np.meshgrid(momenta, momenta, momenta, indexing="ij")
    field_mean = np.asarray(
        [float(np.sum(weights * grid) / np.sum(weights)) for grid in grids]
    )
    body_mean = momentum - field_mean
    check(
        "every populated relative Fourier cell assigns body plus field momentum to fixed K",
        np.linalg.norm(body_mean + field_mean - momentum) < 2e-14
        and float(np.sum(weights)) > 0.05,
        {
            "K": momentum.tolist(),
            "body_mean": body_mean.tolist(),
            "field_mean": field_mean.tolist(),
        },
    )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    record_norms = (
        1.0,
        float(np.vdot(record_zero, record_zero).real),
        float(
            np.vdot(record_zero, record_zero).real
            * np.vdot(record_plus, record_plus).real
        ),
    )
    check(
        "one or two normalized spectator records change neither charge nor emission angle",
        max(abs(charge * value - charge) for value in record_norms) < 2e-14,
        tuple(charge * value for value in record_norms),
    )

    untuned_ratios = []
    for species in species_set:
        shifted_coin = c210.cubic_coin(
            species.alpha + 0.1,
            species.beta,
            species.rest_phase - 0.1 / 3,
        )
        shifted_charge = c213.rest_charge(shifted_coin, c210.P_SCALAR)
        untuned_ratios.append(shifted_charge / species.analytic_mass)
    check(
        "cubic unitarity alone does not align autonomous source strength with inertia",
        max(untuned_ratios) - min(untuned_ratios) > 0.05,
        untuned_ratios,
    )

    angles = [row[2] for row in first_tick_rows]
    check(
        "the bounded source vertices use generic complex non-Clifford angles",
        all(
            min(abs(value - multiple * np.pi / 4) for multiple in range(-4, 5))
            > 1e-3
            for value in angles
        ),
        angles,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    acoustic_field_controls()
    literal_local_law_controls()
    autonomous_emission_controls()
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
