#!/usr/bin/env python3
"""Cycle 213: a retarded proper-cubic field sourced by the bound object.

Replace Cycle 211's dissipative Green-field solver with the centered local
lattice wave law.  The law has a one-edge causal cone, exact time reversal,
and an exact sitewise energy/work/flux identity.  Couple the Cycle-210
composite through one candidate bilinear interaction, so the same
vacuum-relative rest generator supplies the field source and the matter kick.

The field alphabet, wave coefficient, vacuum-relative charge map, bilinear
coupling, and source history remain supplied candidate physics.  This runner
does not claim general relativity, quantized gravity, record formation, Born
frequencies, or an axiom conclusion.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "RETARDED_CUBIC_MASS_FIELD_CYCLE213_NOTE_2026-07-16.md"
)

DT = 0.45
COUPLING = 0.05

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


def laplacian(field: np.ndarray) -> np.ndarray:
    """Positive six-neighbour graph Laplacian on the cubic torus."""
    answer = 6 * field.copy()
    for axis in range(3):
        answer -= np.roll(field, 1, axis=axis)
        answer -= np.roll(field, -1, axis=axis)
    return answer


def wave_step(
    previous: np.ndarray,
    current: np.ndarray,
    source: np.ndarray,
    *,
    dt: float = DT,
    propagation: float = 1.0,
) -> np.ndarray:
    """One synchronous radius-one centered-wave update."""
    return (
        2 * current
        - previous
        - dt**2 * propagation * laplacian(current)
        + dt**2 * source
    )


def reverse_step(
    current: np.ndarray,
    following: np.ndarray,
    source: np.ndarray,
    *,
    dt: float = DT,
) -> np.ndarray:
    """Recover the unique predecessor under the same source slice."""
    return 2 * current - following - dt**2 * laplacian(current) + dt**2 * source


def field_energy(following: np.ndarray, current: np.ndarray, *, dt: float = DT) -> float:
    kinetic = np.sum((following - current) ** 2) / (2 * dt**2)
    cross_potential = np.sum(following * laplacian(current)) / 2
    return float(kinetic + cross_potential)


def energy_density(
    following: np.ndarray, current: np.ndarray, *, dt: float = DT
) -> np.ndarray:
    density = (following - current) ** 2 / (2 * dt**2)
    for axis in range(3):
        for shift in (-1, 1):
            density += (
                (following - np.roll(following, shift, axis=axis))
                * (current - np.roll(current, shift, axis=axis))
                / 4
            )
    return density


def outward_flux_divergence(
    previous: np.ndarray, current: np.ndarray, following: np.ndarray
) -> np.ndarray:
    """Sum the antisymmetric one-edge flux J_(x->y) at each site."""
    centered_difference = following - previous
    divergence = np.zeros_like(current)
    for axis in range(3):
        for shift in (-1, 1):
            neighbor_field = np.roll(current, shift, axis=axis)
            neighbor_difference = np.roll(centered_difference, shift, axis=axis)
            divergence += (
                (current - neighbor_field)
                * (centered_difference + neighbor_difference)
                / 4
            )
    return divergence


def work_density(
    previous: np.ndarray, following: np.ndarray, source: np.ndarray
) -> np.ndarray:
    return (following - previous) * source / 2


def rotate_scalar(field: np.ndarray, frame: np.ndarray) -> np.ndarray:
    side = field.shape[0]
    coordinates = np.indices(field.shape).reshape(3, -1)
    moved = (frame @ coordinates) % side
    answer = np.empty_like(field)
    answer[moved[0], moved[1], moved[2]] = field.reshape(-1)
    return answer


def point_source(
    side: int,
    position: tuple[int, int, int] = (0, 0, 0),
    strength: float = 1.0,
) -> np.ndarray:
    source = np.zeros((side, side, side), dtype=float)
    source[position] = strength
    return source


def gradient(field: np.ndarray, position: tuple[int, int, int]) -> np.ndarray:
    side = field.shape[0]
    answer = np.zeros(3)
    for axis in range(3):
        plus = list(position)
        minus = list(position)
        plus[axis] = (plus[axis] + 1) % side
        minus[axis] = (minus[axis] - 1) % side
        answer[axis] = (field[tuple(plus)] - field[tuple(minus)]) / 2
    return answer


def rest_charge(
    coin: np.ndarray,
    scalar_projector: np.ndarray,
    *,
    vacuum_phase: complex = 1.0 + 0.0j,
) -> float:
    """Principal vacuum-relative scalar-sector phase, not a phase coordinate."""
    rank = float(np.trace(scalar_projector).real)
    scalar_eigenvalue = np.trace(scalar_projector @ coin) / rank
    return float(np.angle(scalar_eigenvalue / vacuum_phase))


def site_order_step(
    previous: np.ndarray,
    current: np.ndarray,
    source: np.ndarray,
    order: np.ndarray,
) -> np.ndarray:
    """Evaluate the frozen-slice local stencil in an arbitrary site order."""
    side = current.shape[0]
    answer = np.empty_like(current)
    for flat_index in order:
        x, y, z = np.unravel_index(int(flat_index), current.shape)
        neighbor_sum = (
            current[(x + 1) % side, y, z]
            + current[(x - 1) % side, y, z]
            + current[x, (y + 1) % side, z]
            + current[x, (y - 1) % side, z]
            + current[x, y, (z + 1) % side]
            + current[x, y, (z - 1) % side]
        )
        local_laplacian = 6 * current[x, y, z] - neighbor_sum
        answer[x, y, z] = (
            2 * current[x, y, z]
            - previous[x, y, z]
            - DT**2 * local_laplacian
            + DT**2 * source[x, y, z]
        )
    return answer


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "retarded proper-cubic",
        "one-edge causal cone",
        "exact local energy",
        "vacuum-relative rest generator",
        "one bilinear interaction",
        "time-averaged green field",
        "species-independent response",
        "source/response reciprocity",
        "phase lift",
        "source history remains supplied",
        "not general relativity",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves conditions, representation control, and scope", not missing, missing)


def charge_and_representation_controls() -> tuple[c210.Species, ...]:
    species_set = tuple(c210.tuned_species(beta) for beta in (-0.2, -0.3, -0.4))
    rows = []
    for species in species_set:
        charge = rest_charge(species.coin, c210.P_SCALAR)
        rows.append((species.beta, charge, species.analytic_mass))
        check(
            f"beta={species.beta} vacuum-relative rest charge equals independent curvature mass",
            abs(charge - species.analytic_mass) < 2e-12,
            rows[-1],
        )

        lifted = c210.cubic_coin(
            species.alpha + 2 * np.pi,
            species.beta + 2 * np.pi,
            species.rest_phase + 2 * np.pi,
        )
        check(
            f"beta={species.beta} a 2pi phase lift changes neither the coin nor charge",
            np.linalg.norm(lifted - species.coin) < 2e-12
            and abs(rest_charge(lifted, c210.P_SCALAR) - charge) < 2e-12,
        )

    rng = np.random.default_rng(213)
    raw = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    basis, _ = np.linalg.qr(raw)
    reference = species_set[-1]
    represented_coin = basis @ reference.coin @ basis.conj().T
    represented_scalar = basis @ c210.P_SCALAR @ basis.conj().T
    check(
        "an arbitrary coin-basis representation leaves the vacuum-relative charge unchanged",
        abs(
            rest_charge(represented_coin, represented_scalar)
            - rest_charge(reference.coin, c210.P_SCALAR)
        )
        < 2e-12,
    )

    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        representation = c210.direction_permutation(frame)
        frame_residuals.append(
            abs(
                rest_charge(
                    representation @ reference.coin @ representation.conj().T,
                    representation @ c210.P_SCALAR @ representation.conj().T,
                )
                - reference.analytic_mass
            )
        )
    check(
        "all 24 proper-cubic representations preserve the source charge",
        len(frame_residuals) == 24 and max(frame_residuals) < 2e-12,
        max(frame_residuals),
    )

    pair_phase = np.exp(1j * rest_charge(species_set[0].coin, c210.P_SCALAR)) * np.exp(
        1j * rest_charge(species_set[1].coin, c210.P_SCALAR)
    )
    check(
        "a held-out two-object scalar sector adds vacuum-relative charge before phase wrapping",
        abs(
            np.angle(pair_phase)
            - species_set[0].analytic_mass
            - species_set[1].analytic_mass
        )
        < 2e-12,
        np.angle(pair_phase),
    )
    return species_set


def exact_law_controls() -> None:
    rng = np.random.default_rng(214)
    shape = (7, 7, 7)
    previous = rng.normal(scale=0.1, size=shape)
    current = rng.normal(scale=0.1, size=shape)
    source = rng.normal(scale=0.02, size=shape)
    following = wave_step(previous, current, source)

    check(
        "the centered update has a unique exact predecessor",
        np.max(np.abs(reverse_step(current, following, source) - previous)) < 2e-14,
    )

    reference = following
    forward_order = np.arange(np.prod(shape))
    reverse_order = forward_order[::-1]
    random_order = rng.permutation(forward_order)
    schedule_residuals = tuple(
        float(np.max(np.abs(site_order_step(previous, current, source, order) - reference)))
        for order in (forward_order, reverse_order, random_order)
    )
    check(
        "every frozen-predecessor site schedule implements the same local process",
        max(schedule_residuals) < 2e-14,
        schedule_residuals,
    )

    local_delta = energy_density(following, current) - energy_density(current, previous)
    local_rhs = work_density(previous, following, source) - outward_flux_divergence(
        previous, current, following
    )
    check(
        "each site obeys the exact local energy = source work - outward flux identity",
        np.max(np.abs(local_delta - local_rhs)) < 2e-14,
        np.max(np.abs(local_delta - local_rhs)),
    )
    check(
        "the site energy density sums to the global positive-CFL energy",
        abs(np.sum(energy_density(following, current)) - field_energy(following, current))
        < 2e-13,
    )
    global_delta = field_energy(following, current) - field_energy(current, previous)
    global_work = float(np.sum(work_density(previous, following, source)))
    check(
        "global field-energy change equals the source-port work exactly",
        abs(global_delta - global_work) < 2e-13,
        {"energy_change": global_delta, "source_work": global_work},
    )

    rotations = c210.proper_cubic_frames()
    covariance_residuals = []
    for frame in rotations:
        covariance_residuals.append(
            float(
                np.max(
                    np.abs(
                        wave_step(
                            rotate_scalar(previous, frame),
                            rotate_scalar(current, frame),
                            rotate_scalar(source, frame),
                        )
                        - rotate_scalar(following, frame)
                    )
                )
            )
        )
    check(
        "the complete field process commutes with all 24 proper-cubic rotations",
        len(rotations) == 24 and max(covariance_residuals) < 2e-14,
        max(covariance_residuals),
    )

    shift = (2, 3, 4)
    translated = wave_step(
        np.roll(previous, shift, axis=(0, 1, 2)),
        np.roll(current, shift, axis=(0, 1, 2)),
        np.roll(source, shift, axis=(0, 1, 2)),
    )
    check(
        "translating both state slices and source translates the next slice",
        np.max(
            np.abs(translated - np.roll(following, shift, axis=(0, 1, 2)))
        )
        < 2e-14,
    )

    momenta = 2 * np.pi * np.fft.fftfreq(31)
    symbols = 6 - 2 * (
        np.cos(momenta)[:, None, None]
        + np.cos(momenta)[None, :, None]
        + np.cos(momenta)[None, None, :]
    )
    half_trace = 1 - DT**2 * symbols / 2
    check(
        "the chosen coefficient is inside the exact cubic CFL stability domain",
        DT**2 * 12 < 4
        and np.max(np.abs(half_trace)) <= 1 + 2e-14,
        {"dt2_lambda_max": DT**2 * 12, "max_half_trace": np.max(np.abs(half_trace))},
    )

    positive_samples = []
    for _ in range(64):
        left = rng.normal(size=shape)
        right = rng.normal(size=shape)
        positive_samples.append(field_energy(left, right))
    check(
        "the CFL certificate makes field energy nonnegative modulo the uniform static mode",
        1 / DT**2 - 12 / 4 > 0 and min(positive_samples) > 0,
        {
            "delta_coefficient_lower_bound": 1 / DT**2 - 12 / 4,
            "held_out_minimum": min(positive_samples),
        },
    )

    source_history = [rng.normal(scale=0.01, size=shape) for _ in range(30)]
    history = [(previous.copy(), current.copy())]
    local_previous, local_current = previous.copy(), current.copy()
    for local_source in source_history:
        local_following = wave_step(local_previous, local_current, local_source)
        local_previous, local_current = local_current, local_following
        history.append((local_previous.copy(), local_current.copy()))
    for local_source in reversed(source_history):
        local_predecessor = reverse_step(local_previous, local_current, local_source)
        local_current, local_previous = local_previous, local_predecessor
    check(
        "a thirty-slice sourced process reverses to its exact initial state",
        np.max(np.abs(local_previous - previous)) < 3e-13
        and np.max(np.abs(local_current - current)) < 3e-13,
    )

    split_previous, split_current = history[17]
    for local_source in source_history[17:]:
        split_following = wave_step(split_previous, split_current, local_source)
        split_previous, split_current = split_current, split_following
    check(
        "cutting and recomposing the deterministic history at tick 17 changes no output",
        np.max(np.abs(split_previous - history[-1][0])) < 2e-14
        and np.max(np.abs(split_current - history[-1][1])) < 2e-14,
    )


def causal_and_conservative_controls() -> np.ndarray:
    side = 31
    zero = np.zeros((side, side, side))
    impulse = point_source(side)
    previous = zero.copy()
    current = zero.copy()
    coordinates = np.indices((side, side, side))
    signed = np.minimum(coordinates, side - coordinates)
    manhattan = np.sum(signed, axis=0)
    support_rows = []
    for tick in range(1, 9):
        source = impulse if tick == 1 else zero
        following = wave_step(previous, current, source)
        radius = tick - 1
        outside = float(np.max(np.abs(following[manhattan > radius])))
        shell = int(np.count_nonzero(np.abs(following) > 1e-15))
        support_rows.append((tick, radius, shell, outside))
        previous, current = current, following
    check(
        "a point impulse has an exact one-edge causal cone for eight generated slices",
        max(row[3] for row in support_rows) < 2e-15,
        support_rows,
    )

    previous = zero.copy()
    current = zero.copy()
    gradients = []
    separation = (4, 0, 0)
    for _tick in range(1, 11):
        following = wave_step(previous, current, impulse)
        previous, current = current, following
        gradients.append(float(gradient(current, separation)[0]))
    check(
        "a separated response stays exactly absent until the causal front arrives",
        max(abs(value) for value in gradients[:3]) < 2e-15
        and abs(gradients[3]) > 1e-8,
        gradients,
    )

    previous = zero.copy()
    current = zero.copy()
    for tick in range(1, 9):
        following = wave_step(
            previous,
            current,
            impulse if tick == 1 else zero,
            propagation=0.0,
        )
        previous, current = current, following
    away = current.copy()
    away[0, 0, 0] = 0
    check(
        "deleting neighbour propagation leaves the sourced value at its origin",
        np.max(np.abs(away)) < 2e-15 and abs(current[0, 0, 0]) > 0,
    )

    previous = zero.copy()
    current = zero.copy()
    reservoir = np.zeros_like(zero)
    energy_rows = []
    for tick in range(1, 401):
        source = impulse if tick <= 4 else zero
        following = wave_step(previous, current, source)
        work = float(np.sum(work_density(previous, following, source)))
        reservoir -= work_density(previous, following, source)
        energy = field_energy(following, current)
        reservoir_energy = float(np.sum(reservoir))
        energy_rows.append(
            (tick, energy, reservoir_energy, energy + reservoir_energy)
        )
        previous, current = current, following
    post_source = [row[1] for row in energy_rows[4:]]
    totals = [row[3] for row in energy_rows]
    check(
        "after source shutoff the reversible field conserves energy without relaxation",
        max(post_source) - min(post_source) < 3e-12,
        {"min": min(post_source), "max": max(post_source)},
    )
    check(
        "site-local source reservoirs plus the field have exact total-energy balance",
        max(totals) - min(totals) < 3e-12 and max(abs(value) for value in totals) < 3e-12,
        {"min": min(totals), "max": max(totals)},
    )

    deleted_previous = zero.copy()
    deleted_current = zero.copy()
    for _ in range(20):
        deleted_following = wave_step(deleted_previous, deleted_current, zero)
        deleted_previous, deleted_current = deleted_current, deleted_following
    check(
        "source deletion leaves the reachable zero field exactly zero",
        np.max(np.abs(deleted_current)) == 0,
    )
    return np.asarray(gradients)


def dynamic_to_green_control() -> None:
    side = 15
    source = c211.point_source(side)
    exact = c211.solve_field(source)
    previous = np.zeros_like(source)
    current = np.zeros_like(source)
    average = np.zeros_like(source)
    checkpoints = {}
    for tick in range(1, 6001):
        following = wave_step(previous, current, source)
        previous, current = current, following
        average += current
        if tick in (100, 1000, 6000):
            checkpoints[tick] = float(
                np.linalg.norm(average / tick - exact) / np.linalg.norm(exact)
            )
    check(
        "the retarded reversible law time-averages to Cycle 211's Green field",
        checkpoints[6000] < 7e-4
        and checkpoints[6000] < checkpoints[1000] < checkpoints[100],
        checkpoints,
    )

    modes = 2 * np.pi * np.fft.fftfreq(side)
    symbol = 6 - 2 * (
        np.cos(modes)[:, None, None]
        + np.cos(modes)[None, :, None]
        + np.cos(modes)[None, None, :]
    )
    source_hat = np.fft.fftn(source)
    omega = np.arccos(np.clip(1 - DT**2 * symbol / 2, -1, 1))
    finite_average_hat = np.zeros_like(source_hat, dtype=complex)
    nonzero = symbol > 1e-14
    ticks = 6000
    # With phi_-1=phi_0=0 and the source first applied in the update to
    # phi_1, each driven mode is
    #   (rho/lambda) [1-cos((n+1/2) omega)/cos(omega/2)].
    # The half-step is load-bearing for a second-order initial-value law.
    indices = np.arange(1, ticks + 1)
    transient_sum = np.sum(
        np.cos(omega[nonzero, None] * (indices[None, :] + 0.5))
        / np.cos(omega[nonzero, None] / 2),
        axis=1,
    )
    finite_average_hat[nonzero] = (
        source_hat[nonzero] / symbol[nonzero] * (1 - transient_sum / ticks)
    )
    finite_average = np.fft.ifftn(finite_average_hat).real
    check(
        "the literal time average equals the independently evaluated modal sum",
        np.linalg.norm(average / ticks - finite_average) < 2e-11,
        np.linalg.norm(average / ticks - finite_average),
    )


def source_response_controls(species_set: tuple[c210.Species, ...]) -> None:
    side = 51
    source_species = species_set[-1]
    source_charge = rest_charge(source_species.coin, c210.P_SCALAR)
    unit_source = point_source(side)
    previous = np.zeros_like(unit_source)
    current = np.zeros_like(unit_source)
    for _ in range(10):
        following = wave_step(
            previous,
            current,
            COUPLING * source_charge * unit_source,
        )
        previous, current = current, following
    separation = (4, 0, 0)
    source_gradient = gradient(current, separation)

    response_rows = []
    for species in species_set:
        test_charge = rest_charge(species.coin, c210.P_SCALAR)
        force = COUPLING * test_charge * source_gradient[0]
        response = c210.force_response(species, force)
        normalized_acceleration = response.acceleration / (-COUPLING * source_gradient[0])
        response_rows.append(
            (
                species.beta,
                test_charge,
                response.measured_mass,
                normalized_acceleration,
                response.band_probability,
            )
        )
    check(
        "the generated retarded field gives species-independent molecular acceleration",
        max(abs(row[3] - 1) for row in response_rows) < 0.007
        and min(row[4] for row in response_rows) > 0.999,
        response_rows,
    )

    left, right = species_set[0], species_set[2]
    left_charge = rest_charge(left.coin, c210.P_SCALAR)
    right_charge = rest_charge(right.coin, c210.P_SCALAR)
    left_field = current * (left_charge / source_charge)
    shift = separation
    right_field = np.roll(
        current * (right_charge / source_charge), shift, axis=(0, 1, 2)
    )
    force_on_right = COUPLING * right_charge * gradient(left_field, separation)
    force_on_left = COUPLING * left_charge * gradient(right_field, (0, 0, 0))
    check(
        "a simultaneously activated stationary pair has equal-and-opposite forces",
        np.linalg.norm(force_on_left + force_on_right) < 2e-14
        and np.linalg.norm(force_on_right) > 1e-10,
        {"left": force_on_left.tolist(), "right": force_on_right.tolist()},
    )
    interaction_left_right = -COUPLING * right_charge * left_field[separation]
    interaction_right_left = -COUPLING * left_charge * right_field[0, 0, 0]
    check(
        "the pair interaction energy is independent of which body is called source",
        abs(interaction_left_right - interaction_right_left) < 2e-14,
        (interaction_left_right, interaction_right_left),
    )

    combined_source = COUPLING * (
        left_charge * point_source(side)
        + right_charge * point_source(side, separation)
    )
    combined_previous = np.zeros_like(combined_source)
    combined_current = np.zeros_like(combined_source)
    for _ in range(10):
        combined_following = wave_step(
            combined_previous, combined_current, combined_source
        )
        combined_previous, combined_current = combined_current, combined_following

    # Evolve the two contributions independently as an ablation of linear
    # source composition, rather than reusing the combined history.
    fields = []
    for local_source in (
        COUPLING * left_charge * point_source(side),
        COUPLING * right_charge * point_source(side, separation),
    ):
        local_previous = np.zeros_like(local_source)
        local_current = np.zeros_like(local_source)
        for _ in range(10):
            local_following = wave_step(local_previous, local_current, local_source)
            local_previous, local_current = local_current, local_following
        fields.append(local_current)
    check(
        "two active source ports compose linearly under the same local field law",
        np.max(np.abs(combined_current - fields[0] - fields[1])) < 2e-14,
    )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    archived_charges = (
        source_charge,
        source_charge * float(np.vdot(record_zero, record_zero).real),
        source_charge
        * float(np.vdot(record_zero, record_zero).real)
        * float(np.vdot(record_plus, record_plus).real),
    )
    archived_fields = []
    for archived_charge in archived_charges:
        archived_previous = np.zeros_like(unit_source)
        archived_current = np.zeros_like(unit_source)
        for _ in range(10):
            archived_following = wave_step(
                archived_previous,
                archived_current,
                COUPLING * archived_charge * unit_source,
            )
            archived_previous, archived_current = archived_current, archived_following
        archived_fields.append(archived_current)
    check(
        "redundant spectator records do not duplicate the object's field source",
        max(abs(value - source_charge) for value in archived_charges) < 2e-14
        and max(
            float(np.max(np.abs(field - archived_fields[0])))
            for field in archived_fields[1:]
        )
        < 2e-14,
        archived_charges,
    )

    untuned_rows = []
    for species in species_set:
        shifted_phase = species.rest_phase - 0.1 / 3
        shifted_coin = c210.cubic_coin(
            species.alpha + 0.1, species.beta, shifted_phase
        )
        charge = rest_charge(shifted_coin, c210.P_SCALAR)
        untuned_rows.append(charge / species.analytic_mass)
    check(
        "the same cubic unitary family loses universal response when rest charge and inertia are untuned",
        max(untuned_rows) - min(untuned_rows) > 0.05
        and max(abs(value - 1) for value in untuned_rows) > 0.1,
        untuned_rows,
    )

    zero_force = 0.0
    zero_response = c210.force_response(source_species, zero_force)
    zero_previous = np.zeros_like(unit_source)
    zero_current = np.zeros_like(unit_source)
    for _ in range(10):
        zero_following = wave_step(
            zero_previous,
            zero_current,
            COUPLING * 0.0 * source_charge * unit_source,
        )
        zero_previous, zero_current = zero_current, zero_following
    check(
        "deleting the bilinear coupling removes the matter acceleration and field source",
        abs(zero_response.acceleration) < 2e-12
        and np.max(np.abs(zero_current)) == 0,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    species_set = charge_and_representation_controls()
    exact_law_controls()
    causal_and_conservative_controls()
    dynamic_to_green_control()
    source_response_controls(species_set)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
