#!/usr/bin/env python3
"""Finite supplied-model definitions and historical receipt diagnostics.

Original production recipe and all earlier claims: .claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py.
Current execution is bounded diagnostics only; no production/physical Maxwell
certificate is supplied. Imaginary-time projection is not a Record formation law.
"""

from __future__ import annotations

from pathlib import Path
import re
import json
from types import SimpleNamespace


from spin_half_cubic_ice_historical_receipt_integrity_2026_09_09 import (historical_text, load_receipt, validate_covariance, check_inputs, held_production, historical_target, shared_zero_covariance, gls_mean)

import argparse
from dataclasses import dataclass

import numpy as np
from numba import njit
from scipy import sparse
from scipy.sparse.linalg import eigs, eigsh

from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import (
    build_geometry,
    count_flippable,
    is_flippable,
)
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
    build_small_rk_orbit,
    decode_small,
    electric_flux,
    encode_small,
    initial_ice,
    vertex_degrees,
)


AUDIT_INPUT_PATHS = (
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md',
    'docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    'docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py',
    'scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py',
    'scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py',
    'scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py',
    'scripts/spin_half_cubic_ice_historical_receipt_integrity_2026_09_09.py',
    'scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py',
    'scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py',
    'scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py',
    'scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py',
    'scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py',
    'scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py',
    'scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py',
    'scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py',
    'scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py',
    'scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py',
)

AUDIT_TIMEOUT_SEC = 150


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, condition: bool, label: str) -> None:
        if condition:
            self.passed += 1
            print(f"[PASS] {self.passed + self.failed:02d} {label}")
        else:
            self.failed += 1
            print(f"[FAIL] {self.passed + self.failed:02d} {label}")


@njit(cache=True)
def flip_weight(
    state: np.ndarray,
    plaquette: int,
    target_orientation: int,
    eta: float,
    plaquette_links: np.ndarray,
    orientation_volume: int,
) -> float:
    if plaquette // orientation_volume != target_orientation:
        return 1.0
    sign = 1.0 if state[plaquette_links[plaquette, 0]] else -1.0
    return np.exp(-eta * sign)


@njit(cache=True)
def count_flippable_and_weight(
    state: np.ndarray,
    target_orientation: int,
    eta: float,
    plaquette_links: np.ndarray,
    orientation_volume: int,
) -> tuple[int, float]:
    count = 0
    weighted = 0.0
    for plaquette in range(plaquette_links.shape[0]):
        if is_flippable(state, plaquette_links[plaquette]):
            count += 1
            weighted += flip_weight(
                state,
                plaquette,
                target_orientation,
                eta,
                plaquette_links,
                orientation_volume,
            )
    return count, weighted


@njit(cache=True)
def flip_and_update_twisted(
    state: np.ndarray,
    plaquette: int,
    current_count: int,
    current_weight: float,
    target_orientation: int,
    eta: float,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    orientation_volume: int,
) -> tuple[int, float]:
    before_count = 0
    before_weight = 0.0
    for slot in range(affected_counts[plaquette]):
        neighbor = affected_plaquettes[plaquette, slot]
        if is_flippable(state, plaquette_links[neighbor]):
            before_count += 1
            before_weight += flip_weight(
                state,
                neighbor,
                target_orientation,
                eta,
                plaquette_links,
                orientation_volume,
            )
    for link in plaquette_links[plaquette]:
        state[link] ^= np.uint8(1)
    after_count = 0
    after_weight = 0.0
    for slot in range(affected_counts[plaquette]):
        neighbor = affected_plaquettes[plaquette, slot]
        if is_flippable(state, plaquette_links[neighbor]):
            after_count += 1
            after_weight += flip_weight(
                state,
                neighbor,
                target_orientation,
                eta,
                plaquette_links,
                orientation_volume,
            )
    return (
        current_count + after_count - before_count,
        current_weight + after_weight - before_weight,
    )


@njit(cache=True)
def systematic_resample_twisted(
    states: np.ndarray,
    counts: np.ndarray,
    weighted_counts: np.ndarray,
    log_weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    population = states.shape[0]
    maximum = np.max(log_weights)
    weights = np.exp(log_weights - maximum)
    total = np.sum(weights)
    effective = total * total / np.sum(weights * weights)
    cumulative = np.cumsum(weights / total)
    offset = np.random.random() / population
    new_states = np.empty_like(states)
    new_counts = np.empty_like(counts)
    new_weighted = np.empty_like(weighted_counts)
    source = 0
    for destination in range(population):
        position = offset + destination / population
        while source + 1 < population and cumulative[source] < position:
            source += 1
        new_states[destination] = states[source]
        new_counts[destination] = counts[source]
        new_weighted[destination] = weighted_counts[source]
    return new_states, new_counts, new_weighted, effective


@njit(cache=True)
def run_twisted_core(
    start_state: np.ndarray,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    delta_v: float,
    eta: float,
    target_orientation: int,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    sample_sweeps: int,
    resample_interval: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float, int]:
    if population <= 0 or sample_sweeps <= 0 or burn_sweeps < 0 or classical_sweeps < 0:
        raise ValueError("invalid sample/population schedule")
    if resample_interval <= 0 or plaquette_links.shape[0] % resample_interval != 0:
        raise ValueError("resampling must divide a complete plaquette sweep")
    if target_orientation < 0 or target_orientation > 2 or not np.isfinite(delta_v) or not np.isfinite(eta):
        raise ValueError("invalid source or coupling")
    np.random.seed(seed)
    plaquette_count = plaquette_links.shape[0]
    orientation_volume = plaquette_count // 3
    scale = 1.5
    green_denominator = scale * plaquette_count
    potential = 1.0 + delta_v
    states = np.empty((population, start_state.shape[0]), dtype=np.uint8)
    counts = np.empty(population, dtype=np.int32)
    weighted_counts = np.empty(population, dtype=np.float64)
    for walker in range(population):
        states[walker] = start_state
        count, weighted = count_flippable_and_weight(
            states[walker],
            target_orientation,
            eta,
            plaquette_links,
            orientation_volume,
        )
        counts[walker] = count
        weighted_counts[walker] = weighted

    # Symmetric ring flips decorrelate the identical ice starts before the
    # non-Hermitian positive projector is applied.
    for _ in range(classical_sweeps * plaquette_count):
        for walker in range(population):
            plaquette = np.random.randint(plaquette_count)
            if is_flippable(states[walker], plaquette_links[plaquette]):
                counts[walker], weighted_counts[walker] = (
                    flip_and_update_twisted(
                        states[walker],
                        plaquette,
                        counts[walker],
                        weighted_counts[walker],
                        target_orientation,
                        eta,
                        plaquette_links,
                        affected_plaquettes,
                        affected_counts,
                        orientation_volume,
                    )
                )

    total_steps = (burn_sweeps + sample_sweeps) * plaquette_count
    first_sample_step = burn_sweeps * plaquette_count
    samples = np.empty(sample_sweeps, dtype=np.float64)
    log_weights = np.zeros(population, dtype=np.float64)
    minimum_effective = float(population)
    invalid_acceptances = 0
    sample_index = 0
    for step in range(total_steps):
        for walker in range(population):
            branch = 1.0 + (
                weighted_counts[walker] - potential * counts[walker]
            ) / green_denominator
            if not np.isfinite(branch) or branch <= 0.0:
                raise ValueError("nonpositive projector branch")
            log_weights[walker] += np.log(branch)
            plaquette = np.random.randint(plaquette_count)
            if is_flippable(states[walker], plaquette_links[plaquette]):
                weight = flip_weight(
                    states[walker],
                    plaquette,
                    target_orientation,
                    eta,
                    plaquette_links,
                    orientation_volume,
                )
                acceptance = weight / (scale * branch)
                if not np.isfinite(acceptance) or acceptance < 0.0 or acceptance > 1.0:
                    raise ValueError("invalid projector transition probability")
                if np.random.random() < min(acceptance, 1.0):
                    counts[walker], weighted_counts[walker] = (
                        flip_and_update_twisted(
                            states[walker],
                            plaquette,
                            counts[walker],
                            weighted_counts[walker],
                            target_orientation,
                            eta,
                            plaquette_links,
                            affected_plaquettes,
                            affected_counts,
                            orientation_volume,
                        )
                    )
        if (step + 1) % resample_interval == 0:
            states, counts, weighted_counts, effective = (
                systematic_resample_twisted(
                    states, counts, weighted_counts, log_weights
                )
            )
            minimum_effective = min(minimum_effective, effective)
            log_weights[:] = 0.0
        if step + 1 > first_sample_step and (
            step + 1 - first_sample_step
        ) % plaquette_count == 0:
            # The interval is chosen to divide one plaquette sweep, so the
            # population here is unweighted.  The local row-energy estimator
            # is exact for the Perron eigenvalue in the infinite projection
            # and population limits.
            if sample_index >= sample_sweeps:
                raise AssertionError("sample buffer overflow")
            samples[sample_index] = np.mean(
                potential * counts - weighted_counts
            )
            sample_index += 1
    if sample_index != sample_sweeps:
        raise AssertionError("incorrect post-burn sample count")
    return (
        samples,
        states,
        counts,
        weighted_counts,
        minimum_effective,
        invalid_acceptances,
    )


def blocked_mean_error(
    values: np.ndarray, block_count: int = 12
) -> tuple[float, float]:
    usable = (len(values) // block_count) * block_count
    blocks = values[:usable].reshape(block_count, -1).mean(axis=1)
    return float(np.mean(blocks)), float(
        np.std(blocks, ddof=1) / np.sqrt(block_count)
    )


@dataclass(frozen=True)
class TwistResult:
    length: int
    delta_v: float
    eta: float
    orientation: int
    energy: float
    energy_error: float
    minimum_effective_fraction: float
    final_unique_fraction: float
    count_consistent: bool
    sector_consistent: bool
    invalid_acceptances: int


def run_twist(
    length: int,
    delta_v: float,
    eta: float,
    orientation: int,
    *,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    sample_sweeps: int,
    seed: int,
) -> TwistResult:
    geometry = build_geometry(length)
    interval = max(8, geometry.plaquette_count // 12)
    while geometry.plaquette_count % interval:
        interval -= 1
    (
        samples,
        states,
        counts,
        weighted_counts,
        minimum_effective,
        invalid_acceptances,
    ) = run_twisted_core(
        initial_ice(length).ravel(),
        geometry.plaquette_links,
        geometry.affected_plaquettes,
        geometry.affected_counts,
        delta_v,
        eta,
        orientation,
        population,
        classical_sweeps,
        burn_sweeps,
        sample_sweeps,
        interval,
        seed,
    )
    mean, error = blocked_mean_error(samples)
    volume = length**3
    count_consistent = True
    weight_consistent = True
    for state, count, weighted in zip(
        states, counts, weighted_counts, strict=True
    ):
        exact_count, exact_weight = count_flippable_and_weight(
            state,
            orientation,
            eta,
            geometry.plaquette_links,
            volume,
        )
        count_consistent = count_consistent and exact_count == count
        weight_consistent = weight_consistent and abs(exact_weight - weighted) < 1e-8
    sector_consistent = all(
        np.all(vertex_degrees(state.reshape(length, length, length, 3)) == 3)
        and electric_flux(state.reshape(length, length, length, 3)) == (0, 0, 0)
        for state in states
    )
    packed = np.packbits(states, axis=1)
    return TwistResult(
        length=length,
        delta_v=delta_v,
        eta=eta,
        orientation=orientation,
        energy=mean,
        energy_error=error,
        minimum_effective_fraction=minimum_effective / population,
        final_unique_fraction=np.unique(packed, axis=0).shape[0] / population,
        count_consistent=count_consistent and weight_consistent,
        sector_consistent=sector_consistent,
        invalid_acceptances=invalid_acceptances,
    )


def exact_small_hamiltonian(delta_v: float, angle: complex) -> sparse.csr_matrix:
    length = 2
    volume = length**3
    orbit = build_small_rk_orbit(initial_ice(length))
    index = {state: position for position, state in enumerate(orbit.states)}
    geometry = build_geometry(length)
    rows: list[int] = []
    columns: list[int] = []
    data: list[complex] = []
    for row, encoded in enumerate(orbit.states):
        state = decode_small(encoded).ravel()
        count = 0
        for plaquette, links in enumerate(geometry.plaquette_links):
            if not is_flippable(state, links):
                continue
            count += 1
            moved = state.copy()
            moved[links] ^= 1
            destination = encode_small(moved.reshape(2, 2, 2, 3))
            sign = 1.0 if state[links[0]] else -1.0
            phase = np.exp(1j * angle * sign) if plaquette // volume == 0 else 1.0
            rows.append(row)
            columns.append(index[destination])
            data.append(-phase)
        rows.append(row)
        columns.append(row)
        data.append((1.0 + delta_v) * count)
    return sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(index), len(index)),
        dtype=np.complex128,
    ).tocsr()


def exact_small_energy(delta_v: float, angle: complex) -> float:
    hamiltonian = exact_small_hamiltonian(delta_v, angle)
    if abs(angle.imag) < 1e-15:
        value = eigsh(
            hamiltonian,
            k=1,
            which="SA",
            return_eigenvectors=False,
            tol=1e-12,
        )[0]
    else:
        value = eigs(
            hamiltonian,
            k=1,
            which="SR",
            return_eigenvectors=False,
            tol=1e-12,
        )[0]
    if abs(value.imag) > 1e-9:
        raise AssertionError("continued ground energy is not real")
    return float(value.real)


def curvature_from_triplet(
    zero: TwistResult, positive: TwistResult, negative: TwistResult
) -> tuple[float, float]:
    if positive.eta <= 0.0 or negative.eta != -positive.eta:
        raise ValueError("curvature needs a symmetric nonzero eta pair")
    eta_squared = positive.eta**2
    even_energy = 0.5 * (positive.energy + negative.energy)
    even_error = 0.5 * np.hypot(
        positive.energy_error, negative.energy_error
    )
    curvature = -2.0 * (even_energy - zero.energy) / (
        eta_squared * zero.length**3
    )
    error = 2.0 * np.hypot(even_error, zero.energy_error) / (
        eta_squared * zero.length**3
    )
    return float(curvature), float(error)


def combine_estimates(estimates: list[tuple[float, float]], covariance: np.ndarray) -> tuple[float, float]:
    """Combine one estimator family with its actual shared-reference covariance."""
    validate_covariance(covariance, [error for _, error in estimates], positive_definite=True)
    return gls_mean([value for value, _ in estimates], covariance)


def volume_summary(
    curvatures: dict[tuple[float, int, float], tuple[float, float]],
    delta_v: float,
    lengths: tuple[int, ...],
    eta_values: tuple[float, ...],
    covariances: dict[int, np.ndarray],
) -> tuple[float, float, dict[int, tuple[float, float]]]:
    combined = {
        length: combine_estimates(
            [curvatures[(delta_v, length, eta)] for eta in eta_values], covariances[length]
        )
        for length in lengths
    }
    values = np.asarray([combined[length][0] for length in lengths])
    propagated = np.sqrt(
        np.sum([combined[length][1] ** 2 for length in lengths])
    ) / len(lengths)
    volume_sem = float(np.std(values, ddof=1) / np.sqrt(len(values)))
    return float(np.mean(values)), max(float(propagated), volume_sem), combined


def main() -> int:
    check_inputs(Path(__file__).resolve().parent.parent, AUDIT_EXPECTED_SHA256)
    checks = Checks()
    receipt = load_receipt("spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt")
    checks.check(receipt.total == (13,0) and not receipt.production_accepted,
        "old thirteen-check artifact is preserved without validating its unsafe sample execution")
    geometry = build_geometry(2); start = initial_ice(2).ravel()
    for burn, count in ((0,1),(1,2),(3,3)):
        samples, states, counts, weights, effective, invalid = run_twisted_core(
            start,geometry.plaquette_links,geometry.affected_plaquettes,geometry.affected_counts,
            -.05,.10,0,2,0,burn,count,3,42100+burn)
        checks.check(len(samples)==count and np.all(np.isfinite(samples)) and invalid==0
            and all(count_flippable(s,geometry.plaquette_links)==c for s,c in zip(states,counts)),
            f"compiled post-burn core returns exactly {count} samples at burn {burn}")
    ratios = set()
    for p, links in enumerate(geometry.plaquette_links):
        if p//8 != 0 or not is_flippable(start,links): continue
        changed = start.copy(); changed[links] ^= 1
        roots = [np.unravel_index(int(link)//3,(2,2,2)) for link in links]
        parity = np.array([(-1)**sum(root) for root in roots]); sign = 2*int(start[links[0]])-1
        actual = parity*(changed[links].astype(int)-start[links].astype(int))
        checks.check(np.array_equal(actual,-parity[0]*sign*np.array([1,1,-1,-1])),
            f"actual plaquette {p} follows the Cartesian electric-update convention")
        implemented = -np.log(flip_weight(start,p,0,.1,geometry.plaquette_links,8))/.1
        ratios.add(round(implemented/(parity[0]*sign)))
    checks.check(ratios=={-1,1}, "occupation-sign source differs at opposite root parities from a uniform Cartesian source")
    radii = np.array([.1,.16]); zero_error=.02; errors=np.array([.7,.3])
    covariance = shared_zero_covariance(errors,radii,zero_error,8)
    value,error = combine_estimates([(1.,errors[0]),(1.2,errors[1])],covariance)
    inverse = np.linalg.inv(covariance); expected_error=np.sqrt(1/(np.ones(2)@inverse@np.ones(2)))
    checks.check(abs(error-expected_error)<1e-12 and covariance[0,1]>0,
        "continuation-radius combination retains the actual shared-zero covariance")
    real = exact_small_hamiltonian(-.05,.02)
    checks.check(np.max(np.abs((real-real.getH()).data)) < 1e-12 if (real-real.getH()).nnz else True,
        "the supplied real-angle occupation-sign matrix is Hermitian on the finite component")
    print("SOURCE_RESPONSE",json.dumps(historical_target(),sort_keys=True))
    print("SCOPE: corrected tiny sampler and finite source algebra only; long magnetic production held; uniform stiffness, magnetic-sector energy and physical UK unavailable")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)




# Current source/input identity: literal finite closure.
AUDIT_EXPECTED_SHA256 = {
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md': 'd005e28ff0cba15f5e5b27580055c2ae51958dfeb967c3603df0d01d8bd4526b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'd9c836c854ee20dddf399d51d7bab6b13f9164a920a10ed2c0713cd6b4f150e4',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md': '1f6811e0f9a872c2a23946dbf313a32c378ca697f658423e0c13dcad708e0ff9',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '73d66f716fdfacc5c6d02f902b2021392e5139041b6018985d2886264a5007ed',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md': '862311719f14a9ba1ee6fc660477fd01510631a87db636f9098a626d5291316d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md': '9b2aba542ed2f36643ce4b511b1f85db9b96a0a5b3570e5f306e561b6b8b246e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md': '1d22ab5c1f16784462b68ddf4021b7e14a110a6ca7be6cff92ffd279f9011715',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md': '139bd99c4f1f9c86bf8f222cb6986957d8f24bfca335a5f3c0ea1654a5a4abbd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': '8a3369b50204369ddfd0311704cf71423a91c5c87df51a6e41dae4657b0ab947',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'c47db40a423d54580b0e27ba844e302c0e9d5cb1105705fb1b5392f21ac00e36',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt': '992136071fbd1f87efbae5daec0689ce7309913ccc12fd294bdfc39a54ae569f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt': '2e483ff3d5bc34e7fdde41b8ab06790be1ea487a167bb10b33936e35ff22c894',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt': '97687c182b2c0a8f095bea6ddc90018e2580163af81757e1bbeaf2650c04fde7',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt': '366e0cfbca4cc582cc28c34c2e822990b5a1216d42513417677e818584cd4fea',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt': 'db3f966552fb31bab95a3d487220dd0622b21b5da127515f197e7e441ad68445',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt': '484c30b66ccbe992290da328e785c22f597dfc698173044c4cec178d3fbaf8b6',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt': '8ec096ed4b50bf92ee7d709470833d9355b8461c9e9c35e5579d1fec4402ed17',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt': 'd6ffe038be4e0a5dc6824965dbdcc24595aac7ba2241ef0ca059310ffeabd59e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt': '849646d782df0c360fd1d180b4d966b3499979b43d1c709b11b5c1e43c2a92e0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt': '5131098b985eab3d4991a5c767c1f057ba047ff694b5d074383037a27f65622c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt': '09f1e590b9cf2cade315bca1a854156a42faba262d22b55f21167bad7a6b798c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt': '88552107e8ce428aec277c61645322a927b209b3a3936ec4471e3344b4d50a35',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt': 'e6e00baa0a8bcb38afdd7cf1e46e09e0c8f5b6ba4422bc2fdcb45fac72a6a92c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt': '2c2dec102b9758f4249818ed2ce935a0c582a5a3c3fead19d91b12aadb8b51af',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt': '17345ac4bd2839c8d0cd315fdc0d5c6126e3b8879f1b3f49bd055c637d0ec481',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt': 'acdfb65d3e785f08ba61b6958461db6154fcd2771e1d309834d00ece3ca48992',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt': '82e2ad2b36cc44b9a367a16554a52dc5a68c94690a571d642f37e9ececcb5216',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt': '6ec74acaacd3909cd39b0520c0bc93e690ca949c54119a60e84a89d55a7ea1d0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt': '7d7cfba76fe8a0de63de2ecd2b2a6241d7401e3904258a45969d30ae76b3f728',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt': 'c77aab04384741c1bca11852b0554742db0b8c157545bded3c1b09735b3b42dc',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt': '5eda05ddbf46d54e600839ecd30f552d3362e3704071037e38c0632dc2f86e81',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt': 'f28a3a727508e6c2df4a4f1e77d0d0bcfdb77a5d41a282f13219d9ef4a4aa202',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py': '97881c8721ee3177aeaa610a59f139ef44be809b49bc9c6ed9f0490fe6b10418',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py': 'a61b5ca89ea5b39ac932744b12e3af46167d81fd4ed5eb52acdb08644f74b28b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py': '5bb190ef328d095d83eacf927e2c3964499f178e6f41254368047957a893227d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py': 'aaa07511fdd1650fe317bd8fe03e4826beaa7f7cf5659c475b7b53e4a6b30733',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py': '421cd0399b35947d90f208ddab78b38b2caf7e7cd5f593613ff53af300aaf434',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py': '75461521b7bd0d3806e3a0598c4c82603f7127623762990d478784ad2ef542b1',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py': '1aa54dbb1b298ee8064603b89e97470d541900d7affb61bf329f269908a2ceca',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py': '7ac21e04324b48c9215524d1e889693ee329a5fe0e3495d1a8c14832249bd953',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py': '8d87b4c4ffc219e7557cf0ad19213842738f8f8a2879493612e3740fd19d26da',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py': 'b0556cf80af1a4515ca1a134c435dd40c011f0dfb058acd743c2948522e12af8',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py': '80108851a3d3a77e8e2593502abfa17ee72eab7174ad7043f039afe2e5133867',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py': '756173baab1c9966bf8c2cdd03860f7736710e17edb7b453fe9e69bf2e328dfb',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py': '9b4fbd65bc089f160e90fef8d2e95b3eaaedb276fd582c9b4697ed393abd0eae',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py': 'fdb9e0d0de5d10282c782cd888a9e3823c76a9c2a253887e76ae8a686de8da1f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py': '8cea10e54e91b643a39d2a757eb120ee992197defdf45dce4cac98e36d5197cd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py': 'e93ddc34b6bdbca4e17a89aa1d1f2ebef140c8717138d9aa429c8911751dc189',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py': '8be752a7b03f7db990958e4813c7e029e85e06736a7cc6644db712452ceddf96',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py': '6057a37e1415b3dce55c85923514ec481f6cb007921d2ed634c8237be18b7655',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py': 'fef6248c3b90c88c1038af037cd152b8e3d33577dcc31286328bdffe6cdfa0ec',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py': 'ae6390773d562d8ffe37bae981cc64246e0cbebb817eff88b6383ca376e7eeac',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py': '477ca4a1af788464bb798ffa0bc5c2f42fd3c3c3591d22fd075b80e24cb82a4e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py': 'f621e2b2d00bf85525dae4a1a3f103dd156cb9ba837c5f8f4d5199282ae5c2cb',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json': 'c1c7a1cdd92236409d829be9a8dad7700b169e6e8bc3f5d94e28fa34c25653a7',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md': '5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/SPIN_HALF_CARTESIAN_PLAQUETTE_SOURCE_NOTE_2026-09-07.md': '80ab2512f0f7706be19b87a2db8da34aa287be103715fdce9130072d6c4ce360',
    'docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md': '0d40064ad01d7754e65b787c2697c248b206624844a7098d83ebf7834cbc4b04',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c1cc8df7ae97504527fd26195e65670ad6ccf4e01982d0665040662b22ba0d7e',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'abcbed4c6bec81e7adef327f2443fec88540f0bf9069e1ce6383a46a4f22600b',
    'docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md': '38aeb623dcec523202326e4b4e2c30cd05a2a612d8bcd81216599a038b91fcaa',
    'docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md': '4b05e927da85639cf5bd7aaa45244189467ba8f0ad0c7325e07e8f692b032d2d',
    'docs/U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'f238e2e384e1737b64df96adcbc30c48f7ceebe67b55c69a449c9a19ee95429d',
    'docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'b8a6f37dff7ab8c7263ff8b8cd27faf549b268c3ac79a6a4ba26d56e38b8fe77',
    'scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py': '7881de5fd06a33c2c36d6c252b7a363e8d357775ce16f0c82e517b9ce4848c44',
    'scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py': '585c9d0ab507aae8f7c66e0806ae071d99ffc781c56f42c0d0d8c08e6ece4aac',
    'scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py': '317b726df0cf682d2bce47ff839b2e0ed7c1fa3aa56d08e824d3d4676b46f466',
    'scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py': 'a710a92baaaa7492cfeb7eaaa8db1e88cf902b6abc3531d4d9031a90310e3210',
    'scripts/spin_half_cubic_ice_historical_receipt_integrity_2026_09_09.py': 'a5514a656d9d3b82c0b76c46e5aff2b9e731eb6b634de2bc99b25b9af458f54f',
    'scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py': 'd10e0a59dedf58df6a23b9a08162a7b8bff58f55fd00ecdfb68e5ad7e5eda5d8',
    'scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py': '405acaa8d0e7cd0e2621fc1bc188dce61fd42ae60bb9d44b58bce65e37175300',
    'scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py': 'bbfdc4b33ac1725d82d778ddc2da805d79e3bfc3ca8e73a0a1fa558e8521719e',
    'scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py': '8b8e950015cd7b3befe6515a270d81c4435187fb4477a6997751652c80f49bf6',
    'scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py': 'd5963665437c2bec0af54dc64f9c27ba6c3a714c96f32843ad89125b712dc0c9',
    'scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py': 'db523208f850ea9eb0028e028b9fcadffe65a8a1d35a71535fa7a9dd6b345e3b',
    'scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py': 'e3a2cd41c739475b341d7a9b173f344e30920d4bf49d461a11af0d0c2a7bbf8f',
    'scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py': 'd450a0f17e886ab4ba6ccf7caf56068751a439601ea5ed9d1bdeb98e61e4b467',
    'scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py': '05ccde69a2b55aa701a6baf3d4a7f2b79668be5cd9f0f2fc9a4402e2af1051d5',
    'scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py': '24c2032bfa3b6dfcb2b86f0a1e096f80f89de5140ef0beea56ade88a447ae919',
}

if __name__ == "__main__":
    raise SystemExit(main())
