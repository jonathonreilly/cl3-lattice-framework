#!/usr/bin/env python3
"""Cycle 230: spatial CAR lift and a local modular-seam interaction probe.

Construct the canonical intrinsic-CAR lift of the supplied six-direction
proper-cubic walk on a finite periodic lattice.  Add one supplied onsite even
contact gate,

    W_g = product_x exp(i g binom(N_x, 2)),

and evaluate its first-order two-particle/two-hole form factor for a supplied
principal-branch sea.  The runner checks strict CAR support, the depth-two
fermionic stream factorization, a full finite-torus occupied-mode projector, a
machine-precision finite modular channel, and a shrinking finite-volume seam
sequence.

This is an abstract six-CAR-mode cell, not a one-qubit-per-site compiler.  It
does not select the sea, phase origin, interaction, physical energy, clock,
records, probability law, transition rate, vacuum, or axiom content.
"""

from __future__ import annotations

from itertools import product
from pathlib import Path

import numpy as np
from scipy.linalg import schur

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import local_generator_source_tournament_cycle228_2026_07_17 as c228
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "SPATIAL_CAR_CONTACT_SEAM_FORM_FACTOR_CYCLE230_NOTE_2026-07-17.md"
)

BETA = -0.3
COUPLING = 0.37
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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "intrinsic car",
        "six fermionic modes per coarse cell",
        "not a one-qubit-per-site compiler",
        "depth-two fermionic swap",
        "principal-branch slater sea ray",
        "two-particle/two-hole",
        "machine-precision fixture resonance",
        "plane-wave-factor-stripped",
        "universal 1/l^3",
        "thirring quantum cellular automaton",
        "farrelly and short",
        "gupta and short",
        "first-order generator coupling",
        "not a transition probability",
        "physical energy remains unselected",
        "n1 — alternative routes",
        "n2 — wall-independence",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — resolution",
        "n6 — primitive and reframe",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom conclusion",
        "global priority is not claimed",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the bounded result and N1-N8 gate", not missing, missing)


def site_index(site: tuple[int, int, int], direction: int, length: int) -> int:
    x, y, z = site
    return (((x * length + y) * length + z) * 6) + direction


def all_sites(length: int) -> tuple[tuple[int, int, int], ...]:
    return tuple(product(range(length), repeat=3))


def shifted_site(
    site: tuple[int, int, int], displacement: np.ndarray, length: int
) -> tuple[int, int, int]:
    return tuple(
        int((site[axis] + int(displacement[axis])) % length) for axis in range(3)
    )


def spatial_layers(
    length: int, coin: np.ndarray
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Return U=S C and the onsite coin, stream, A, B one-particle layers."""
    mode_count = 6 * length**3
    onsite_coin = np.kron(np.eye(length**3, dtype=complex), coin)
    stream = np.zeros((mode_count, mode_count), dtype=complex)
    reverse_layer = np.zeros_like(stream)
    edge_layer = np.zeros_like(stream)
    reverse = (1, 0, 3, 2, 5, 4)
    for site in all_sites(length):
        for direction, displacement in enumerate(c210.DIRECTIONS):
            source = site_index(site, direction, length)
            destination = site_index(
                shifted_site(site, displacement, length), direction, length
            )
            stream[destination, source] = 1

            reversed_direction = reverse[direction]
            reverse_layer[
                site_index(site, reversed_direction, length), source
            ] = 1
            edge_destination = shifted_site(site, -displacement, length)
            edge_layer[
                site_index(edge_destination, reversed_direction, length), source
            ] = 1
    return (
        stream @ onsite_coin,
        onsite_coin,
        stream,
        reverse_layer,
        edge_layer,
    )


def frame_representation(length: int, frame: np.ndarray) -> np.ndarray:
    mode_count = 6 * length**3
    representation = np.zeros((mode_count, mode_count), dtype=complex)
    direction_representation = c210.direction_permutation(frame)
    for site in all_sites(length):
        transformed_site = tuple(int(value % length) for value in frame @ site)
        for source_direction in range(6):
            target_direction = int(
                np.argmax(direction_representation[:, source_direction])
            )
            representation[
                site_index(transformed_site, target_direction, length),
                site_index(site, source_direction, length),
            ] = 1
    return representation


def translation_representation(length: int, displacement: np.ndarray) -> np.ndarray:
    mode_count = 6 * length**3
    representation = np.zeros((mode_count, mode_count), dtype=complex)
    for site in all_sites(length):
        target = shifted_site(site, displacement, length)
        for direction in range(6):
            representation[
                site_index(target, direction, length),
                site_index(site, direction, length),
            ] = 1
    return representation


def antisymmetric_norm(amplitude: np.ndarray) -> float:
    return float(np.sqrt(np.sum(np.abs(amplitude) ** 2) / 2))


def pair_amplitude(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    return np.outer(first, second) - np.outer(second, first)


def contact_pair_step(amplitude: np.ndarray, length: int, coupling: float) -> np.ndarray:
    result = amplitude.copy()
    phase = np.exp(1j * coupling)
    for site in all_sites(length):
        modes = tuple(site_index(site, direction, length) for direction in range(6))
        result[np.ix_(modes, modes)] *= phase
    return result


def contact_generator_action(amplitude: np.ndarray, length: int) -> np.ndarray:
    result = np.zeros_like(amplitude)
    for site in all_sites(length):
        modes = tuple(site_index(site, direction, length) for direction in range(6))
        result[np.ix_(modes, modes)] = amplitude[np.ix_(modes, modes)]
    return result


def spatial_car_controls() -> tuple[np.ndarray, int]:
    length = 3
    species = c219.common_species(BETA)
    unitary, onsite_coin, stream, reverse_layer, edge_layer = spatial_layers(
        length, species.coin
    )
    identity = np.eye(unitary.shape[0], dtype=complex)
    check(
        "the L=3 onsite-coin and one-edge stream give a unitary radius-one one-particle walk",
        np.linalg.norm(unitary.conj().T @ unitary - identity) < 8e-14
        and np.linalg.norm(stream.conj().T @ stream - identity) < 2e-15,
        {
            "dimension": unitary.shape[0],
            "unitarity": float(np.linalg.norm(unitary.conj().T @ unitary - identity)),
        },
    )
    check(
        "the stream has an exact depth-two intrinsic-fermion swap factorization S=B A",
        np.linalg.norm(stream - edge_layer @ reverse_layer) < 2e-15
        and np.linalg.norm(reverse_layer @ reverse_layer - identity) < 2e-15
        and np.linalg.norm(edge_layer @ edge_layer - identity) < 2e-15,
    )
    layer_rng = np.random.default_rng(2300)
    layer_pair = layer_rng.normal(size=stream.shape) + 1j * layer_rng.normal(
        size=stream.shape
    )
    layer_pair = layer_pair - layer_pair.T
    direct_stream_pair = stream @ layer_pair @ stream.T
    layered_stream_pair = edge_layer @ (
        reverse_layer @ layer_pair @ reverse_layer.T
    ) @ edge_layer.T
    check(
        "the two fermionic stream layers lift to the identical antisymmetric two-particle action",
        np.linalg.norm(direct_stream_pair - layered_stream_pair) < 2e-12,
        float(np.linalg.norm(direct_stream_pair - layered_stream_pair)),
    )

    two_mode_swap = np.asarray(
        (
            (1, 0, 0, 0),
            (0, 0, 1, 0),
            (0, 1, 0, 0),
            (0, 0, 0, -1),
        ),
        dtype=complex,
    )
    ordinary_swap = two_mode_swap.copy()
    ordinary_swap[3, 3] = 1
    exterior_swap = c229.fock_lift(
        np.asarray(((0, 1), (1, 0)), dtype=complex)
    )
    check(
        "the stream layers require fermionic swaps; an ordinary qubit SWAP misses the occupied-pair sign",
        np.linalg.norm(exterior_swap - two_mode_swap) < 2e-15
        and np.linalg.norm(ordinary_swap - exterior_swap) == 2,
    )

    unique_neighbors = []
    for length_control in (2, 3):
        origin = (0, 0, 0)
        unique_neighbors.append(
            len(
                {
                    shifted_site(origin, direction, length_control)
                    for direction in c210.DIRECTIONS
                }
            )
        )
    check(
        "L=3 is the smallest periodic cube that does not alias opposite nearest neighbors",
        unique_neighbors == [3, 6],
        unique_neighbors,
    )

    covariance = []
    for frame in c210.proper_cubic_frames():
        representation = frame_representation(length, frame)
        covariance.append(
            np.linalg.norm(representation @ unitary - unitary @ representation)
        )
    translation = []
    for axis in range(3):
        displacement = np.zeros(3, dtype=int)
        displacement[axis] = 1
        representation = translation_representation(length, displacement)
        translation.append(
            np.linalg.norm(representation @ unitary - unitary @ representation)
        )
    check(
        "the spatial walk is translation invariant and covariant under all 24 proper-cubic frames",
        max(covariance) < 8e-14 and max(translation) < 8e-14,
        {"cubic": max(covariance), "translation": max(translation)},
    )

    local_gamma_coin = c229.fock_lift(species.coin)
    occupations = c229.occupation_table(6)
    number = np.sum(occupations, axis=1)
    local_contact = np.diag(np.exp(1j * COUPLING * number * (number - 1) / 2))
    check(
        "the local 64-state exterior coin and contact gate are unitary and number preserving",
        np.linalg.norm(
            local_gamma_coin.conj().T @ local_gamma_coin - np.eye(64)
        )
        < 8e-14
        and np.linalg.norm(local_contact.conj().T @ local_contact - np.eye(64))
        < 3e-15
        and np.max(np.abs(np.diag(local_contact)[number <= 1] - 1)) < 2e-15,
        {"local_dimension": 64, "one_particle_contact": 0.0},
    )

    local_contact_covariance = []
    for frame in c210.proper_cubic_frames():
        direction_representation = c210.direction_permutation(frame)
        gamma_frame = c229.fock_lift(direction_representation)
        local_contact_covariance.append(
            np.linalg.norm(
                gamma_frame @ local_contact - local_contact @ gamma_frame
            )
        )
    check(
        "the supplied contact is proper-cubic invariant (indeed invariant under all mode permutations)",
        max(local_contact_covariance) < 2e-14,
        max(local_contact_covariance),
    )

    first = np.zeros(unitary.shape[0], dtype=complex)
    second = np.zeros_like(first)
    first[site_index((0, 0, 0), 0, length)] = 1
    second[site_index((0, 0, 0), 2, length)] = 1
    initial = pair_amplitude(first, second)
    free = unitary @ initial @ unitary.T
    interacting = contact_pair_step(free, length, COUPLING)
    reverse_schedule = unitary @ contact_pair_step(initial, length, COUPLING) @ unitary.T
    deleted = contact_pair_step(free, length, 0.0)
    check(
        "the exact two-particle CAR lift preserves antisymmetry and norm under free and contact steps",
        np.linalg.norm(free + free.T) < 2e-14
        and np.linalg.norm(interacting + interacting.T) < 2e-14
        and abs(antisymmetric_norm(initial) - 1) < 2e-15
        and abs(antisymmetric_norm(free) - 1) < 2e-14
        and abs(antisymmetric_norm(interacting) - 1) < 2e-14,
    )
    rng = np.random.default_rng(2301)
    random_pair = rng.normal(size=initial.shape) + 1j * rng.normal(size=initial.shape)
    random_pair = random_pair - random_pair.T
    random_pair /= antisymmetric_norm(random_pair)
    contacted_pair = contact_pair_step(random_pair, length, COUPLING)
    local_density = []
    contacted_density = []
    for site in all_sites(length):
        modes = tuple(site_index(site, direction, length) for direction in range(6))
        local_density.append(float(np.sum(np.abs(random_pair[modes, :]) ** 2)))
        contacted_density.append(
            float(np.sum(np.abs(contacted_pair[modes, :]) ** 2))
        )
    check(
        "the onsite contact leaves every cell occupation unchanged before the one-edge stream",
        np.max(np.abs(np.asarray(local_density) - np.asarray(contacted_density)))
        < 2e-15,
        float(
            np.max(np.abs(np.asarray(local_density) - np.asarray(contacted_density)))
        ),
    )
    check(
        "interaction deletion returns the free step while the undeclared schedule order is physically noncommuting",
        np.linalg.norm(deleted - free) < 2e-15
        and np.linalg.norm(interacting - reverse_schedule) > 1e-3,
        np.linalg.norm(interacting - reverse_schedule),
    )

    stiffness = 2 * identity - unitary - unitary.conj().T
    dgamma_stiffness = stiffness @ initial + initial @ stiffness.T
    commutator_witness = contact_generator_action(
        dgamma_stiffness, length
    ) - (
        stiffness @ contact_generator_action(initial, length)
        + contact_generator_action(initial, length) @ stiffness.T
    )
    check(
        "the contact generator preserves particle number but does not commute with the free local-deviation generator",
        antisymmetric_norm(commutator_witness) > 0.2,
        antisymmetric_norm(commutator_witness),
    )

    curvature = c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    forced = c210.force_response(species, 2e-5)
    check(
        "because the contact is identity for N<=1, the previously tested one-particle rest/curvature/inertial mass contract is unchanged",
        abs(c219.rest_mass(species) / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(forced.measured_mass / species.analytic_mass - 1) < 0.007,
        {
            "rest": c219.rest_mass(species),
            "dispersion": dispersion_mass,
            "forced": forced.measured_mass,
        },
    )
    return unitary, length


def finite_torus_modes(
    length: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, tuple[dict[str, object], ...]]:
    species = c219.common_species(BETA)
    unitary, _, _, _, _ = spatial_layers(length, species.coin)
    coordinates = np.asarray(all_sites(length), dtype=float)
    columns = []
    eigenvalues = []
    phases = []
    metadata = []
    momenta = 2 * np.pi * np.fft.fftfreq(length)
    for momentum_index in product(range(length), repeat=3):
        momentum = np.asarray(
            [momenta[index] for index in momentum_index], dtype=float
        )
        triangular, internal = schur(c228.walk_symbol(BETA, momentum), output="complex")
        values = np.diag(triangular)
        envelope = np.exp(1j * (coordinates @ momentum)) / np.sqrt(length**3)
        for band in range(6):
            column = (envelope[:, None] * internal[:, band][None, :]).reshape(-1)
            columns.append(column)
            eigenvalues.append(values[band])
            phases.append(float(np.angle(values[band])))
            metadata.append(
                {
                    "momentum_index": momentum_index,
                    "momentum": momentum,
                    "band": band,
                    "phase": float(np.angle(values[band])),
                }
            )
    return (
        unitary,
        np.column_stack(columns),
        np.asarray(eigenvalues),
        tuple(metadata),
    )


def finite_sea_controls(unitary: np.ndarray, length: int) -> None:
    mode_unitary, modes, eigenvalues, metadata = finite_torus_modes(length)
    phases = np.angle(eigenvalues)
    occupied = phases < -1e-10
    sea = modes[:, occupied]
    projector = sea @ sea.conj().T
    check(
        "the complete L=3 Bloch basis diagonalizes the spatial walk and is orthonormal",
        np.linalg.norm(mode_unitary - unitary) < 2e-15
        and np.linalg.norm(modes.conj().T @ modes - np.eye(modes.shape[1])) < 2e-13
        and np.linalg.norm(unitary @ modes - modes * eigenvalues[None, :]) < 2e-13,
        {"mode_count": modes.shape[1], "sea_rank": int(np.sum(occupied))},
    )
    check(
        "the supplied principal cut gives a full invariant occupied-mode projector and finite Slater sea ray",
        np.linalg.norm(projector @ projector - projector) < 2e-13
        and np.linalg.norm(unitary @ projector - projector @ unitary) < 2e-13
        and np.min(np.abs(phases)) > 1e-3
        and np.min(np.abs(np.abs(phases) - np.pi)) > 1e-3,
        {
            "rank": int(np.sum(occupied)),
            "zero_gap": float(np.min(np.abs(phases))),
            "seam_gap": float(np.min(np.abs(np.abs(phases) - np.pi))),
        },
    )

    cubic = []
    for frame in c210.proper_cubic_frames():
        representation = frame_representation(length, frame)
        cubic.append(
            np.linalg.norm(
                representation @ projector @ representation.conj().T - projector
            )
        )
    translations = []
    for axis in range(3):
        displacement = np.zeros(3, dtype=int)
        displacement[axis] = 1
        representation = translation_representation(length, displacement)
        translations.append(
            np.linalg.norm(
                representation @ projector @ representation.conj().T - projector
            )
        )
    check(
        "the supplied finite sea is translation and proper-cubic invariant",
        max(cubic) < 3e-13 and max(translations) < 3e-13,
        {"cubic": max(cubic), "translation": max(translations)},
    )

    shifted = np.angle(np.exp(1j * (phases + 0.4))) < 0
    check(
        "the full finite sea remains dependent on a supplied quasienergy phase origin",
        int(np.sum(shifted)) != int(np.sum(occupied)),
        {"base_rank": int(np.sum(occupied)), "shifted_rank": int(np.sum(shifted))},
    )
    check(
        "all occupied and empty modes used below belong to this one complete finite sea ledger",
        len(metadata) == 6 * length**3
        and int(np.sum(occupied)) + int(np.sum(~occupied)) == 6 * length**3,
    )


def circular_distance(phases: np.ndarray, target: float) -> np.ndarray:
    return np.abs(np.angle(np.exp(1j * (phases - target))))


def band_subspace(
    momentum: np.ndarray,
    target_phase: float | None = None,
    target_value: complex | None = None,
    dimension: int | None = None,
    tolerance: float = 1e-7,
) -> tuple[np.ndarray, np.ndarray]:
    triangular, vectors = schur(c228.walk_symbol(BETA, momentum), output="complex")
    values = np.diag(triangular)
    phases = np.angle(values)
    if target_phase is not None:
        indices = np.where(circular_distance(phases, target_phase) < tolerance)[0]
    elif target_value is not None and dimension is not None:
        indices = np.argsort(np.abs(values - target_value))[:dimension]
    else:
        raise ValueError("supply target_phase or target_value and dimension")
    return phases[indices], vectors[:, indices]


def internal_wedge(first: np.ndarray, second: np.ndarray) -> np.ndarray:
    amplitude = np.outer(first, second) - np.outer(second, first)
    return amplitude[np.triu_indices(6, 1)]


def contact_form_factor(
    particle_first: np.ndarray,
    particle_second: np.ndarray,
    hole_first: np.ndarray,
    hole_second: np.ndarray,
) -> np.ndarray:
    result = np.zeros(
        (
            particle_first.shape[1] * particle_second.shape[1],
            hole_first.shape[1] * hole_second.shape[1],
        ),
        dtype=complex,
    )
    for first_hole in range(hole_first.shape[1]):
        for second_hole in range(hole_second.shape[1]):
            hole_wedge = internal_wedge(
                hole_first[:, first_hole], hole_second[:, second_hole]
            )
            source = first_hole * hole_second.shape[1] + second_hole
            for first_particle in range(particle_first.shape[1]):
                for second_particle in range(particle_second.shape[1]):
                    particle_wedge = internal_wedge(
                        particle_first[:, first_particle],
                        particle_second[:, second_particle],
                    )
                    target = (
                        first_particle * particle_second.shape[1] + second_particle
                    )
                    result[target, source] = np.vdot(particle_wedge, hole_wedge)
    return result


def bloch_subspace(
    momentum: np.ndarray, internal: np.ndarray, length: int
) -> np.ndarray:
    coordinates = np.asarray(all_sites(length), dtype=float)
    envelope = np.exp(1j * (coordinates @ momentum)) / np.sqrt(length**3)
    return np.vstack(
        tuple((envelope[:, None] * internal[:, band][None, :]).reshape(-1)
              for band in range(internal.shape[1]))
    ).T


def direct_spatial_contact_block(
    particle_first: np.ndarray,
    particle_second: np.ndarray,
    hole_first: np.ndarray,
    hole_second: np.ndarray,
    length: int,
) -> np.ndarray:
    result = np.zeros(
        (
            particle_first.shape[1] * particle_second.shape[1],
            hole_first.shape[1] * hole_second.shape[1],
        ),
        dtype=complex,
    )
    for site_number in range(length**3):
        local = slice(6 * site_number, 6 * (site_number + 1))
        result += contact_form_factor(
            particle_first[local],
            particle_second[local],
            hole_first[local],
            hole_second[local],
        )
    return result


def l3_modular_channel_controls() -> np.ndarray:
    length = 3
    unit = 2 * np.pi / length
    momenta = {
        "h1": unit * np.asarray((0, 1, 0), dtype=float),
        "h2": unit * np.asarray((0, -1, 0), dtype=float),
        "p1": unit * np.asarray((1, 1, 1), dtype=float),
        "p2": unit * np.asarray((-1, -1, -1), dtype=float),
    }
    targets = {
        "h1": -0.148864781941705,
        "h2": -2.9904574355314986,
        "p1": 0.0759239848775555,
        "p2": 3.067939104828828,
    }
    subspaces = {
        name: band_subspace(momentum, target_phase=targets[name])
        for name, momentum in momenta.items()
    }
    phases = {name: subspaces[name][0] for name in subspaces}
    vectors = {name: subspaces[name][1] for name in subspaces}
    form = contact_form_factor(
        vectors["p1"], vectors["p2"], vectors["h1"], vectors["h2"]
    )
    singulars = np.linalg.svd(form, compute_uv=False)
    phase_costs = (
        phases["p1"][:, None, None, None]
        + phases["p2"][None, :, None, None]
        - phases["h1"][None, None, :, None]
        - phases["h2"][None, None, None, :]
    )
    check(
        "the L=3 principal sea contains a momentum-balanced machine-precision modular 2p2h channel",
        all(np.all(phases[name] < 0) for name in ("h1", "h2"))
        and all(np.all(phases[name] > 0) for name in ("p1", "p2"))
        and np.linalg.norm(momenta["h1"] + momenta["h2"]) < 2e-15
        and np.linalg.norm(momenta["p1"] + momenta["p2"]) < 2e-15
        and np.max(np.abs(phase_costs - 2 * np.pi)) < 3e-14,
        {
            "dimensions": {name: vectors[name].shape[1] for name in vectors},
            "phase_residual": float(np.max(np.abs(phase_costs - 2 * np.pi))),
        },
    )
    check(
        "the L=3 plane-wave-factor-stripped contact channel is rank two and nonzero independent of degenerate-band basis",
        len(singulars) == 2
        and singulars[-1] > 0.45
        and singulars[0] > 0.49
        and np.linalg.norm(form) > 0.67,
        {"singular_values": singulars, "frobenius": float(np.linalg.norm(form))},
    )
    rng = np.random.default_rng(2302)
    gauge_residuals = []
    for _ in range(12):
        rotated = {}
        for name, subspace in vectors.items():
            trial = rng.normal(size=(subspace.shape[1], subspace.shape[1]))
            trial = trial + 1j * rng.normal(size=trial.shape)
            gauge, _ = np.linalg.qr(trial)
            rotated[name] = subspace @ gauge
        rotated_form = contact_form_factor(
            rotated["p1"], rotated["p2"], rotated["h1"], rotated["h2"]
        )
        gauge_residuals.append(
            np.linalg.norm(np.linalg.svd(rotated_form, compute_uv=False) - singulars)
        )
    check(
        "random unitary changes of every degenerate band basis leave the reported contact singular values fixed",
        max(gauge_residuals) < 3e-15,
        max(gauge_residuals),
    )

    spatial = {
        name: bloch_subspace(momenta[name], vectors[name], length)
        for name in vectors
    }
    direct = direct_spatial_contact_block(
        spatial["p1"], spatial["p2"], spatial["h1"], spatial["h2"], length
    )
    check(
        "the direct spatial Slater-Condon sum equals the reduced form factor divided by L^3",
        np.linalg.norm(direct - form / length**3) < 2e-15,
        {
            "residual": float(np.linalg.norm(direct - form / length**3)),
            "raw_generator_norm_over_g": float(np.linalg.norm(direct)),
        },
    )

    unbalanced_momentum = momenta["p2"] + unit * np.asarray((1, 0, 0))
    triangular, unbalanced_vectors = schur(
        c228.walk_symbol(BETA, unbalanced_momentum), output="complex"
    )
    unbalanced_phases = np.angle(np.diag(triangular))
    unbalanced_vectors = unbalanced_vectors[:, unbalanced_phases > 1e-9]
    unbalanced_internal = contact_form_factor(
        vectors["p1"],
        unbalanced_vectors,
        vectors["h1"],
        vectors["h2"],
    )
    unbalanced_spatial = bloch_subspace(
        unbalanced_momentum, unbalanced_vectors, length
    )
    unbalanced_direct = direct_spatial_contact_block(
        spatial["p1"],
        unbalanced_spatial,
        spatial["h1"],
        spatial["h2"],
        length,
    )
    check(
        "an unbalanced channel with a nonzero internal overlap is exactly removed by translation momentum conservation",
        np.linalg.norm(unbalanced_internal) > 0.1
        and np.linalg.norm(unbalanced_direct) < 2e-15,
        {
            "internal": float(np.linalg.norm(unbalanced_internal)),
            "spatial": float(np.linalg.norm(unbalanced_direct)),
        },
    )

    frame_singulars = []
    for frame in c210.proper_cubic_frames():
        transformed = {
            name: band_subspace(
                frame @ momenta[name], target_phase=targets[name]
            )[1]
            for name in momenta
        }
        transformed_form = contact_form_factor(
            transformed["p1"],
            transformed["p2"],
            transformed["h1"],
            transformed["h2"],
        )
        frame_singulars.append(np.linalg.svd(transformed_form, compute_uv=False))
    check(
        "the finite modular contact block has the same singular values in all 24 proper-cubic frames",
        max(np.linalg.norm(row - singulars) for row in frame_singulars) < 2e-13,
        max(np.linalg.norm(row - singulars) for row in frame_singulars),
    )
    return form


def seam_block(
    lower: float, upper: float, target: complex
) -> tuple[np.ndarray, float, dict[str, np.ndarray]]:
    hole_phase_plus, hole_plus = band_subspace(
        np.full(3, lower), target_value=target, dimension=2
    )
    hole_phase_minus, hole_minus = band_subspace(
        np.full(3, -lower), target_value=target, dimension=2
    )
    particle_phase_plus, particle_plus = band_subspace(
        np.full(3, upper), target_value=target, dimension=2
    )
    particle_phase_minus, particle_minus = band_subspace(
        np.full(3, -upper), target_value=target, dimension=2
    )
    form = contact_form_factor(
        particle_plus, particle_minus, hole_plus, hole_minus
    )
    phase_cost = float(
        np.mean(particle_phase_plus)
        + np.mean(particle_phase_minus)
        - np.mean(hole_phase_plus)
        - np.mean(hole_phase_minus)
    )
    return (
        form,
        phase_cost,
        {
            "hole_plus": hole_phase_plus,
            "hole_minus": hole_phase_minus,
            "particle_plus": particle_phase_plus,
            "particle_minus": particle_phase_minus,
        },
    )


def finite_volume_seam_controls(form_l3: np.ndarray) -> None:
    minus_root = 1.5783929737448452
    rows = []
    for length in (18, 34, 78, 416):
        lower_index = int(np.floor(minus_root * length / (2 * np.pi)))
        lower = 2 * np.pi * lower_index / length
        upper = 2 * np.pi * (lower_index + 1) / length
        form, phase_cost, phase_data = seam_block(lower, upper, -1)
        singulars = np.linalg.svd(form, compute_uv=False)
        rows.append(
            {
                "L": length,
                "lower_gap": minus_root - lower,
                "upper_gap": upper - minus_root,
                "phase_cost": phase_cost,
                "wrapped_phase": abs(float(np.angle(np.exp(1j * phase_cost)))),
                "singular_min": float(np.min(singulars)),
                "singular_max": float(np.max(singulars)),
                "frobenius": float(np.linalg.norm(form)),
                "raw_operator_over_g": float(np.max(singulars) / length**3),
                "hole_phase_max": float(
                    max(
                        np.max(phase_data[name])
                        for name in ("hole_plus", "hole_minus")
                    )
                ),
                "particle_phase_min": float(
                    min(
                        np.min(phase_data[name])
                        for name in ("particle_plus", "particle_minus")
                    )
                ),
                "maximum_degenerate_spread": float(
                    max(np.ptp(values) for values in phase_data.values())
                ),
            }
        )
    check(
        "the sampled balanced finite-volume sequence tracks the conditional free-phase 4pi seam limit",
        rows[-1]["wrapped_phase"] < 0.0046
        and rows[-1]["wrapped_phase"] < rows[0]["wrapped_phase"] / 20
        and max(rows[-1]["lower_gap"], rows[-1]["upper_gap"]) < 0.0077
        and all(row["hole_phase_max"] < 0 for row in rows)
        and all(row["particle_phase_min"] > 0 for row in rows)
        and max(row["maximum_degenerate_spread"] for row in rows) < 3e-14,
        rows,
    )
    check(
        "the plane-wave-factor-stripped seam contact operator remains full rank with sampled values near one",
        min(row["singular_min"] for row in rows) > 0.97
        and rows[-1]["singular_min"] > 0.9998
        and abs(rows[-1]["singular_max"] - 1) < 2e-4
        and rows[-1]["raw_operator_over_g"] < rows[0]["raw_operator_over_g"] / 1000,
        rows,
    )

    plus_root = 1.563199679844947
    delta = 1e-3
    minus_form, _, _ = seam_block(
        minus_root - delta, minus_root + delta, -1
    )
    plus_form, plus_cost, _ = seam_block(
        plus_root - delta, plus_root + delta, 1
    )
    minus_singulars = np.linalg.svd(minus_form, compute_uv=False)
    plus_singulars = np.linalg.svd(plus_form, compute_uv=False)
    check(
        "for this contact the tested U=+1 crossing has the same reduced strength; nonzero coupling alone is not the seam signature",
        np.linalg.norm(minus_singulars - plus_singulars) < 3e-13
        and abs(plus_cost) < 7e-4,
        {
            "singular_residual": float(np.linalg.norm(minus_singulars - plus_singulars)),
            "ordinary_phase_cost": plus_cost,
        },
    )

    last_length = rows[-1]["L"]
    lower_index = int(np.floor(minus_root * last_length / (2 * np.pi)))
    lower = 2 * np.pi * lower_index / last_length
    upper = 2 * np.pi * (lower_index + 1) / last_length
    reference_singulars = np.linalg.svd(seam_block(lower, upper, -1)[0], compute_uv=False)
    frame_residuals = []
    for frame in c210.proper_cubic_frames():
        subspaces = []
        for momentum in (
            np.full(3, upper),
            np.full(3, -upper),
            np.full(3, lower),
            np.full(3, -lower),
        ):
            subspaces.append(
                band_subspace(
                    frame @ momentum, target_value=-1, dimension=2
                )[1]
            )
        transformed = contact_form_factor(*subspaces)
        frame_residuals.append(
            np.linalg.norm(
                np.linalg.svd(transformed, compute_uv=False) - reference_singulars
            )
        )
    check(
        "the shrinking-seam form factor is proper-cubic covariant in every tested frame",
        max(frame_residuals) < 3e-13,
        max(frame_residuals),
    )

    rng = np.random.default_rng(230)
    source = rng.normal(size=form_l3.shape[1]) + 1j * rng.normal(size=form_l3.shape[1])
    target = rng.normal(size=form_l3.shape[0]) + 1j * rng.normal(size=form_l3.shape[0])
    source /= np.linalg.norm(source)
    target /= np.linalg.norm(target)
    spectator = np.asarray((1, 1j), dtype=complex) / np.sqrt(2)
    extra = np.asarray((np.sqrt(0.3), np.sqrt(0.7)), dtype=complex)
    base = np.vdot(target, form_l3 @ source)
    one_spectator = np.vdot(
        np.kron(target, spectator),
        np.kron(form_l3, np.eye(2)) @ np.kron(source, spectator),
    )
    two_spectators = np.vdot(
        np.kron(np.kron(target, spectator), extra),
        np.kron(form_l3, np.eye(4))
        @ np.kron(np.kron(source, spectator), extra),
    )
    check(
        "one or two passive tensor spectators leave the contact matrix element unchanged",
        abs(base - one_spectator) < 2e-15
        and abs(base - two_spectators) < 2e-15,
        {
            "one_spectator": abs(base - one_spectator),
            "two_spectators": abs(base - two_spectators),
        },
    )


def main() -> None:
    note_contract()
    unitary, length = spatial_car_controls()
    finite_sea_controls(unitary, length)
    form_l3 = l3_modular_channel_controls()
    finite_volume_seam_controls(form_l3)
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
