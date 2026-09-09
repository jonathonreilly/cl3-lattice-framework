#!/usr/bin/env python3
"""Cycle 229: Fock positivity, modular boundary, and local deviation current.

Execute the finite spectral-kinematic core of the Cycle-228 particle-hole
steelman on the supplied proper-cubic one-particle family.  The runner builds
an eigenmode-diagonal finite CAR/free-Fock lift, verifies nonnegative additive
particle/hole excitation coordinates relative to a chosen sea, instantiates
the discrete-time modular-seam alias at the current U=-1 crossing, exposes the
number-sector condition behind global phase, and derives an exact local
continuity equation for the reference-relative one-step-deviation vector.

This does not select a physical vacuum, phase reference, Hamiltonian, source,
clock, record process, or interacting Fock law.  It changes no constitutional
surface.
"""

from __future__ import annotations

from itertools import permutations
from pathlib import Path

import numpy as np

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import local_generator_source_tournament_cycle228_2026_07_17 as c228
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "FOCK_MODULAR_BOUNDARY_CURRENT_CYCLE229_NOTE_2026-07-17.md"
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


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "eigenmode-diagonal finite car representation",
        "free fock lift",
        "particle-hole",
        "modular boundary",
        "gupta and short",
        "number-sector",
        "local deviation continuity",
        "positive excitation energy is not yet physical energy",
        "n1 — alternative routes",
        "n2 — wall-independence",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — resolution",
        "n6 — primitive and reframe",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "physical energy remains unselected",
        "phase convention",
        "conjugate orientation",
        "finite onsite-qubit realization in three dimensions",
        "no axiom conclusion",
        "global novelty has not been established",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the bounded result and N1-N8 gate", not missing, missing)


def annihilation_operators(mode_count: int) -> tuple[np.ndarray, ...]:
    dimension = 1 << mode_count
    operators = []
    for mode in range(mode_count):
        operator = np.zeros((dimension, dimension), dtype=complex)
        lower_mask = (1 << mode) - 1
        for basis in range(dimension):
            if (basis >> mode) & 1:
                target = basis ^ (1 << mode)
                sign = -1 if (basis & lower_mask).bit_count() % 2 else 1
                operator[target, basis] = sign
        operators.append(operator)
    return tuple(operators)


def occupation_table(mode_count: int) -> np.ndarray:
    basis = np.arange(1 << mode_count, dtype=np.uint64)[:, None]
    modes = np.arange(mode_count, dtype=np.uint64)[None, :]
    return ((basis >> modes) & 1).astype(float)


def fock_diagonal(phases: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    occupations = occupation_table(len(phases))
    return occupations, np.exp(1j * (occupations @ phases))


def fock_lift(unitary: np.ndarray) -> np.ndarray:
    """Number-preserving exterior-algebra lift in the occupation basis."""
    mode_count = unitary.shape[0]
    dimension = 1 << mode_count
    occupied = tuple(
        tuple(mode for mode in range(mode_count) if (basis >> mode) & 1)
        for basis in range(dimension)
    )
    gamma = np.zeros((dimension, dimension), dtype=complex)
    for target, target_modes in enumerate(occupied):
        for source, source_modes in enumerate(occupied):
            if len(target_modes) != len(source_modes):
                continue
            if not target_modes:
                gamma[target, source] = 1
            else:
                gamma[target, source] = np.linalg.det(
                    unitary[np.ix_(target_modes, source_modes)]
                )
    return gamma


def particle_hole_ledger(
    phases: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, int]:
    occupations, fock_update = fock_diagonal(phases)
    negative = phases < 0
    excitation_occupations = np.where(
        negative[None, :], 1 - occupations, occupations
    )
    excitation_energy = excitation_occupations @ np.abs(phases)
    sea_index = int(sum((1 << mode) for mode, value in enumerate(negative) if value))
    relative_update = fock_update / fock_update[sea_index]
    return excitation_occupations, excitation_energy, relative_update, sea_index


def phase_set_distance(left: np.ndarray, right: np.ndarray) -> float:
    best = np.inf
    for order in permutations(range(len(right))):
        residual = max(
            abs(np.angle(np.exp(1j * (left[index] - right[order[index]]))))
            for index in range(len(left))
        )
        best = min(best, residual)
    return float(best)


def car_and_fock_controls() -> None:
    operators = annihilation_operators(6)
    identity = np.eye(64, dtype=complex)
    car_residuals = []
    for left, a_left in enumerate(operators):
        for right, a_right in enumerate(operators):
            expected = identity if left == right else np.zeros_like(identity)
            car_residuals.append(
                np.linalg.norm(
                    a_left @ a_right.conj().T
                    + a_right.conj().T @ a_left
                    - expected
                )
            )
            car_residuals.append(
                np.linalg.norm(a_left @ a_right + a_right @ a_left)
            )
    check(
        "the six-mode eigenmode representation satisfies the canonical anticommutation relations",
        max(car_residuals) < 2e-15,
        max(car_residuals),
    )

    rows = []
    for beta, momentum in (
        (-0.2, np.asarray((0.41, -0.23, 0.17))),
        (-0.3, np.asarray((0.70, 0.40, -0.20))),
        (-0.35, np.asarray((1.20, 0.50, 0.30))),
    ):
        phases = np.angle(np.linalg.eigvals(c228.walk_symbol(beta, momentum)))
        occupations, fock_update = fock_diagonal(phases)
        excitations, energy, relative_update, sea_index = particle_hole_ledger(
            phases
        )
        covariance_residuals = []
        gamma = np.diag(fock_update)
        number_operator = np.diag(np.sum(occupations, axis=1))
        for mode, creation in enumerate(operator.conj().T for operator in operators):
            covariance_residuals.append(
                np.linalg.norm(
                    gamma @ creation @ gamma.conj().T
                    - np.exp(1j * phases[mode]) * creation
                )
            )
        sea_state = np.zeros(64, dtype=complex)
        sea_state[sea_index] = 1
        occupation_projectors = tuple(
            np.diag(occupations[:, mode]) for mode in range(6)
        )
        particle_hole_annihilators = tuple(
            operators[mode]
            if phases[mode] > 0
            else operators[mode].conj().T
            for mode in range(6)
        )
        particle_hole_car = []
        for left, b_left in enumerate(particle_hole_annihilators):
            for right, b_right in enumerate(particle_hole_annihilators):
                expected = identity if left == right else np.zeros_like(identity)
                particle_hole_car.append(
                    np.linalg.norm(
                        b_left @ b_right.conj().T
                        + b_right.conj().T @ b_left
                        - expected
                    )
                )
                particle_hole_car.append(
                    np.linalg.norm(b_left @ b_right + b_right @ b_left)
                )
        particle_hole_evolution = tuple(
            np.linalg.norm(
                gamma @ annihilator.conj().T @ gamma.conj().T
                - np.exp(1j * abs(phases[mode])) * annihilator.conj().T
            )
            for mode, annihilator in enumerate(particle_hole_annihilators)
        )
        rows.append(
            {
                "beta": beta,
                "minimum_abs_phase": float(np.min(np.abs(phases))),
                "sea_rank": int(np.sum(phases < 0)),
                "sea_index": sea_index,
                "minimum_energy": float(np.min(energy)),
                "zero_count": int(np.sum(energy < 1e-12)),
                "phase_match": float(
                    np.max(np.abs(relative_update - np.exp(1j * energy)))
                ),
                "unitarity": float(
                    np.max(np.abs(np.abs(fock_update) - 1))
                ),
                "car_covariance": float(max(covariance_residuals)),
                "particle_hole_car": float(max(particle_hole_car)),
                "particle_hole_vacuum": float(
                    max(
                        np.linalg.norm(annihilator @ sea_state)
                        for annihilator in particle_hole_annihilators
                    )
                ),
                "particle_hole_evolution": float(max(particle_hole_evolution)),
                "sea_eigenstate": float(
                    np.linalg.norm(
                        gamma @ sea_state - fock_update[sea_index] * sea_state
                    )
                ),
                "mode_occupation_conservation": float(
                    max(
                        np.linalg.norm(
                            gamma @ projector - projector @ gamma
                        )
                        for projector in occupation_projectors
                    )
                ),
                "number_conservation": float(
                    np.linalg.norm(gamma @ number_operator - number_operator @ gamma)
                ),
                "one_particle_recovery": float(
                    max(
                        abs(fock_update[1 << mode] - np.exp(1j * phases[mode]))
                        for mode in range(6)
                    )
                ),
                "empty_vacuum_signed_minimum": float(
                    np.min(occupations @ phases)
                ),
                "additivity": float(
                    np.max(
                        np.abs(
                            energy
                            - np.sum(excitations * np.abs(phases)[None, :], axis=1)
                        )
                    )
                ),
                "occupation_rows": len(occupations),
            }
        )
    check(
        "the eigenmode-diagonal Fock lift is unitary and implements the diagonal one-particle eigenphases",
        max(row["unitarity"] for row in rows) < 2e-15
        and max(row["car_covariance"] for row in rows) < 2e-14
        and max(row["particle_hole_car"] for row in rows) < 2e-15
        and max(row["particle_hole_vacuum"] for row in rows) < 2e-15
        and max(row["particle_hole_evolution"] for row in rows) < 2e-14
        and max(row["sea_eigenstate"] for row in rows) < 2e-15
        and max(row["mode_occupation_conservation"] for row in rows) < 2e-15
        and max(row["number_conservation"] for row in rows) < 2e-15
        and max(row["one_particle_recovery"] for row in rows) < 2e-15,
        rows,
    )
    check(
        "the empty-vacuum signed lift retains negative excitation coordinates",
        max(row["empty_vacuum_signed_minimum"] for row in rows) < -5.0,
        rows,
    )
    check(
        "the supplied particle-hole sea gives a nonnegative additive excitation coordinate",
        min(row["minimum_energy"] for row in rows) >= 0
        and max(row["zero_count"] for row in rows) == 1
        and max(row["phase_match"] for row in rows) < 3e-15
        and max(row["additivity"] for row in rows) < 2e-15,
        rows,
    )


def branch_endpoint_controls() -> None:
    """Expose the exact U=+/-1 branch content of the beta=0 fixture."""
    momentum = np.asarray((0.41, -0.23, 0.17))
    values = np.linalg.eigvals(c228.walk_symbol(0.0, momentum))
    ordinary = [value for value in values if abs(value - 1) >= 1e-10 and abs(value + 1) >= 1e-10]
    zero_count = sum(abs(value - 1) < 1e-10 for value in values)
    pi_count = sum(abs(value + 1) < 1e-10 for value in values)
    ordinary_phases = sorted(float(np.angle(value)) for value in ordinary)
    plus_phases = np.asarray(ordinary_phases + [0.0] * zero_count + [np.pi] * pi_count)
    minus_phases = np.asarray(ordinary_phases + [0.0] * zero_count + [-np.pi] * pi_count)

    plus_q, plus_energy, plus_relative, plus_sea = particle_hole_ledger(plus_phases)
    minus_q, minus_energy, minus_relative, minus_sea = particle_hole_ledger(minus_phases)
    _, plus_update = fock_diagonal(plus_phases)
    _, minus_update = fock_diagonal(minus_phases)
    check(
        "the beta=0 endpoint fixture has explicit zero-mode degeneracy and inequivalent +/-pi sea conventions",
        zero_count == 2
        and pi_count == 2
        and int(np.sum(plus_energy < 1e-12)) == 4
        and int(np.sum(minus_energy < 1e-12)) == 4
        and plus_sea != minus_sea
        and not np.array_equal(plus_q, minus_q)
        and np.max(np.abs(plus_update - minus_update)) < 2e-14
        and np.max(np.abs(plus_relative - minus_relative)) < 2e-14
        and np.max(np.abs(np.sort(plus_energy) - np.sort(minus_energy))) < 2e-14,
        {
            "zero_modes": zero_count,
            "pi_modes": pi_count,
            "zero_energy_degeneracy": int(np.sum(plus_energy < 1e-12)),
            "plus_sea_rank": int(np.sum(plus_phases < 0)),
            "minus_sea_rank": int(np.sum(minus_phases < 0)),
            "relative_phase_residual": float(
                np.max(np.abs(plus_relative - minus_relative))
            ),
        },
    )


def small_reference_shift_controls() -> None:
    """Check the exact number-relative response while the sea is unchanged."""
    delta = 0.02
    momentum = np.asarray((0.41, -0.23, 0.17))
    phases = np.angle(np.linalg.eigvals(c228.walk_symbol(-0.3, momentum)))
    shifted_phases = phases + delta
    base_q, base_energy, base_relative, base_sea = particle_hole_ledger(phases)
    shifted_q, shifted_energy, shifted_relative, shifted_sea = particle_hole_ledger(
        shifted_phases
    )
    occupations = occupation_table(len(phases))
    number = np.sum(occupations, axis=1)
    sea_rank = int(np.sum(phases < 0))
    expected_energy = base_energy + delta * (number - sea_rank)
    expected_phase = np.exp(1j * delta * (number - sea_rank)) * base_relative
    check(
        "a small reference shift with no crossings obeys the exact number-minus-sea response",
        np.array_equal(base_q, shifted_q)
        and base_sea == shifted_sea
        and np.max(np.abs(shifted_energy - expected_energy)) < 2e-14
        and np.max(np.abs(shifted_relative - expected_phase)) < 2e-14,
        {
            "delta": delta,
            "sea_rank": sea_rank,
            "energy_response_residual": float(
                np.max(np.abs(shifted_energy - expected_energy))
            ),
            "phase_response_residual": float(
                np.max(np.abs(shifted_relative - expected_phase))
            ),
        },
    )


def rest_and_composition_controls() -> None:
    rows = []
    for beta in (-0.2, -0.3, -0.35, -0.4):
        species = c219.common_species(beta)
        phase, _ = c210.branch_eigenpair(np.zeros(3), species)
        phase = species.rest_phase + c210.angular_difference(
            phase, species.rest_phase
        )
        rows.append(
            {
                "beta": beta,
                "particle_energy": abs(phase),
                "mass_from_particle": 3 * abs(phase),
                "analytic_mass": species.analytic_mass,
            }
        )
    check(
        "one selected scalar Fock excitation retains the supplied rest calibration",
        max(
            abs(row["mass_from_particle"] / row["analytic_mass"] - 1)
            for row in rows
        )
        < 2e-12,
        rows,
    )

    phase_blocks = []
    for momentum in (
        np.asarray((0.41, -0.23, 0.17)),
        np.asarray((0.70, 0.40, -0.20)),
    ):
        phase_blocks.append(
            np.angle(np.linalg.eigvals(c228.walk_symbol(-0.3, momentum)))
        )
    phases = np.concatenate(phase_blocks)
    excitations, energies, relative_update, _ = particle_hole_ledger(phases)
    check(
        "the unwrapped particle-hole ledger composes across two momentum blocks",
        len(energies) == 4096
        and np.min(energies) >= 0
        and np.max(np.abs(relative_update - np.exp(1j * energies))) < 5e-15
        and np.max(energies) > 2 * np.pi
        and np.max(np.sum(excitations, axis=1)) == 12,
        {
            "states": len(energies),
            "maximum_energy": float(np.max(energies)),
            "wrapped_aliases_exist": bool(np.max(energies) > 2 * np.pi),
        },
    )


def number_sector_phase_reference_controls() -> None:
    delta = 0.4
    momentum = np.asarray((0.41, -0.23, 0.17))
    unitary = c228.walk_symbol(-0.3, momentum)
    shifted = np.exp(1j * delta) * unitary
    rng = np.random.default_rng(2291)
    vector = rng.normal(size=6) + 1j * rng.normal(size=6)
    vector /= np.linalg.norm(vector)
    density = np.outer(vector, vector.conj())

    phases = np.angle(np.linalg.eigvals(unitary))
    shifted_phases = np.angle(np.exp(1j * (phases + delta)))
    occupations, gamma = fock_diagonal(phases)
    _, shifted_gamma = fock_diagonal(shifted_phases)
    ratios = shifted_gamma / gamma
    numbers = np.sum(occupations, axis=1)
    fixed_sector_residuals = []
    for number in range(7):
        sector = ratios[numbers == number]
        fixed_sector_residuals.append(
            float(np.max(np.abs(sector - np.exp(1j * delta * number))))
        )
    best_global = ratios[0]
    full_residual = float(np.max(np.abs(ratios - best_global)))
    _, energies, _, _ = particle_hole_ledger(phases)
    _, shifted_energies, _, _ = particle_hole_ledger(shifted_phases)
    check(
        "one-particle global phase is projective but the full Fock lift carries number phase",
        np.linalg.norm(
            unitary @ density @ unitary.conj().T
            - shifted @ density @ shifted.conj().T
        )
        < 2e-15
        and max(fixed_sector_residuals) < 2e-14
        and full_residual > 0.5,
        {
            "fixed_sector_residual": max(fixed_sector_residuals),
            "full_Fock_nonprojective_residual": full_residual,
        },
    )
    check(
        "the particle-hole sea and positive ledger still depend on phase reference",
        int(np.sum(phases < 0)) != int(np.sum(shifted_phases < 0))
        and np.max(np.abs(np.sort(energies) - np.sort(shifted_energies))) > 0.2,
        {
            "base_sea_rank": int(np.sum(phases < 0)),
            "shifted_sea_rank": int(np.sum(shifted_phases < 0)),
            "energy_set_change": float(
                np.max(np.abs(np.sort(energies) - np.sort(shifted_energies)))
            ),
        },
    )


def crossing_phase(location: float, displacement: float, target: complex) -> float:
    unitary = c228.walk_symbol(
        -0.3, np.full(3, location + displacement, dtype=float)
    )
    values = np.linalg.eigvals(unitary)
    value = values[int(np.argmin(np.abs(values - target)))]
    return float(np.angle(value))


def modular_boundary_controls() -> None:
    # Numerically located in Cycle 228; the conditional seam identity itself is
    # algebraic, while these locations and shrinking-offset witnesses are
    # finite-precision fixture evidence.
    plus_location = 1.563199679844947
    minus_location = 1.5783929737448452
    plus_root_residual = float(
        np.min(
            np.abs(
                np.linalg.eigvals(
                    c228.walk_symbol(-0.3, np.full(3, plus_location))
                )
                - 1
            )
        )
    )
    minus_root_residual = float(
        np.min(
            np.abs(
                np.linalg.eigvals(
                    c228.walk_symbol(-0.3, np.full(3, minus_location))
                )
                + 1
            )
        )
    )
    rows = []
    for delta in (1e-2, 1e-3, 1e-4):
        zero_negative = crossing_phase(plus_location, -delta, 1)
        zero_positive = crossing_phase(plus_location, delta, 1)
        zero_energy = zero_positive - zero_negative
        zero_wrapped = float(np.angle(np.exp(1j * zero_energy)))

        zone_negative = crossing_phase(minus_location, -delta, -1)
        zone_positive = crossing_phase(minus_location, delta, -1)
        zone_energy = zone_positive - zone_negative
        zone_wrapped = float(np.angle(np.exp(1j * zone_energy)))
        rows.append(
            {
                "delta": delta,
                "zero_energy": zero_energy,
                "zero_wrapped": zero_wrapped,
                "zone_energy": zone_energy,
                "zone_wrapped": zone_wrapped,
                "zone_alias": abs(zone_energy - 2 * np.pi),
            }
        )
    check(
        "the U=+1 crossing has ordinary small particle-hole cost",
        plus_root_residual < 1e-12
        and all(row["zero_energy"] > 0 for row in rows)
        and max(
            abs(row["zero_energy"] - row["zero_wrapped"]) for row in rows
        )
        < 2e-15,
        {"root_residual": plus_root_residual, "offset_rows": rows},
    )
    check(
        "the tested sequence around the numerically located U=-1 root aliases a near-2pi chosen branch-coordinate difference to a phase near one",
        minus_root_residual < 1e-12
        and min(row["zone_energy"] for row in rows) > 6.27
        and max(abs(row["zone_wrapped"]) for row in rows) < 0.0031
        and rows[-1]["zone_alias"] < rows[0]["zone_alias"] / 90,
        {"root_residual": minus_root_residual, "offset_rows": rows},
    )

    phases = np.angle(
        np.linalg.eigvals(
            c228.walk_symbol(-0.3, np.asarray((0.41, -0.23, 0.17)))
        )
    )
    safe_negative = phases[(phases < 0) & (np.abs(phases) < np.pi / 2)]
    safe_positive = phases[(phases > 0) & (np.abs(phases) < np.pi / 2)]
    safe_rows = []
    for negative in safe_negative:
        for positive in safe_positive:
            energy = float(positive - negative)
            safe_rows.append((energy, float(np.angle(np.exp(1j * energy)))))
    check(
        "at the sampled momentum block, selected central mode pairs avoid one-pair wrapping",
        bool(safe_rows)
        and max(abs(energy - wrapped) for energy, wrapped in safe_rows) < 2e-15
        and max(energy for energy, _ in safe_rows) < np.pi,
        safe_rows,
    )


def local_deviation_continuity_controls() -> None:
    rng = np.random.default_rng(2292)
    rows = []
    for beta, reference in ((0.0, 0.0), (-0.3, 0.0), (-0.3, 0.4)):
        coin = c219.common_species(beta).coin
        state = rng.normal(size=(9, 9, 9, 6)) + 1j * rng.normal(
            size=(9, 9, 9, 6)
        )
        state /= np.linalg.norm(state)
        following = c228.walk_step(state, coin)
        deviation = state - np.exp(-1j * reference) * following
        coined = np.einsum("ab,xyzb->xyza", coin, deviation, optimize=True)
        flux = np.abs(coined) ** 2
        density = np.sum(np.abs(deviation) ** 2, axis=-1)
        following_twice = c228.walk_step(following, coin)
        next_deviation = following - np.exp(-1j * reference) * following_twice
        next_density = np.sum(np.abs(next_deviation) ** 2, axis=-1)
        divergence = np.zeros_like(density)
        for direction, vector in enumerate(c210.DIRECTIONS):
            divergence += np.roll(
                flux[..., direction],
                tuple(int(value) for value in vector),
                axis=(0, 1, 2),
            ) - flux[..., direction]
        transported = c228.walk_step(deviation, coin)
        rows.append(
            {
                "beta": beta,
                "reference": reference,
                "continuity": float(
                    np.max(np.abs(next_density - density - divergence))
                ),
                "transport": float(np.linalg.norm(next_deviation - transported)),
                "global_change": float(abs(np.sum(next_density - density))),
            }
        )
    check(
        "the reference-relative deviation vector obeys an exact local continuity equation",
        max(row["continuity"] for row in rows) < 2e-17
        and max(row["transport"] for row in rows) < 4e-15
        and max(row["global_change"] for row in rows) < 2e-14,
        rows,
    )


def covariance_and_complex_controls() -> None:
    momentum = np.asarray((0.41, -0.23, 0.17))
    spectral_residuals = []
    fock_residuals = []
    for beta in (0.0, -0.3, -0.35):
        unitary = c228.walk_symbol(beta, momentum)
        phases = np.angle(np.linalg.eigvals(unitary))
        gamma = fock_lift(unitary)
        for frame in c210.proper_cubic_frames():
            representation = c210.direction_permutation(frame)
            moved_unitary = c228.walk_symbol(beta, frame @ momentum)
            moved = np.angle(np.linalg.eigvals(moved_unitary))
            spectral_residuals.append(phase_set_distance(phases, moved))
            fock_representation = fock_lift(representation)
            fock_residuals.append(
                np.linalg.norm(
                    fock_lift(moved_unitary)
                    - fock_representation @ gamma @ fock_representation.conj().T
                )
            )
    check(
        "the finite Fock blocks are covariant over all proper-cubic frames",
        max(spectral_residuals) < 2e-14 and max(fock_residuals) < 1e-13,
        {
            "spectral_residual": max(spectral_residuals),
            "fock_covariance_residual": max(fock_residuals),
        },
    )

    coin = c219.common_species(-0.3).coin
    phases = np.angle(np.linalg.eigvals(c228.walk_symbol(-0.3, momentum)))
    quarter_turn_distance = np.min(
        np.abs(
            phases[:, None]
            - (np.pi / 4) * np.arange(-4, 5, dtype=float)[None, :]
        ),
        axis=1,
    )
    check(
        "the held family uses generic complex non-Clifford phase data",
        np.linalg.norm(coin.imag) > 0.1
        and np.max(quarter_turn_distance) > 0.1,
        {
            "imaginary_coin_norm": float(np.linalg.norm(coin.imag)),
            "maximum_quarter_turn_distance": float(
                np.max(quarter_turn_distance)
            ),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    car_and_fock_controls()
    branch_endpoint_controls()
    small_reference_shift_controls()
    rest_and_composition_controls()
    number_sector_phase_reference_controls()
    modular_boundary_controls()
    local_deviation_continuity_controls()
    covariance_and_complex_controls()
    print("PASS", PASS, "FAIL", FAIL)
    print("RESULT", "FOCK_PARTIAL_MODULAR_BOUNDARY_OPEN" if FAIL == 0 else "CYCLE229_OPEN")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
