#!/usr/bin/env python3
"""Finite supplied-model definitions and historical receipt diagnostics.

Original production recipe and all earlier claims: .claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py.
Current execution is bounded diagnostics only; no production/physical Maxwell
certificate is supplied. Imaginary-time projection is not a Record formation law.
"""

from __future__ import annotations

from pathlib import Path
import re
import json
from types import SimpleNamespace
from spin_half_cubic_ice_historical_receipt_integrity_2026_09_09 import spectral_health

from spin_half_cubic_ice_historical_receipt_integrity_2026_09_09 import (historical_text, load_receipt, validate_covariance, check_inputs, held_production, historical_target, shared_zero_covariance, gls_mean)

from dataclasses import dataclass
from itertools import permutations

import numpy as np
from numba import njit
from scipy import sparse
from scipy.sparse.linalg import eigsh

from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import (
    build_geometry,
    count_flippable,
    flip_and_update_count,
    is_flippable,
    neutral_flux_pair_start,
)
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
    build_small_rk_orbit,
    decode_small,
    electric_flux,
    initial_ice,
    small_flip_destinations,
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
    'docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md',
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
def systematic_indices(log_weights: np.ndarray) -> tuple[np.ndarray, float]:
    population = log_weights.shape[0]
    maximum = np.max(log_weights)
    weights = np.exp(log_weights - maximum)
    total = np.sum(weights)
    normalized = weights / total
    effective_population = total * total / np.sum(weights * weights)
    cumulative = np.cumsum(normalized)
    offset = np.random.random() / population
    indices = np.empty(population, dtype=np.int32)
    source = 0
    for destination in range(population):
        position = offset + destination / population
        while source + 1 < population and cumulative[source] < position:
            source += 1
        indices[destination] = source
    return indices, effective_population


@njit(cache=True)
def resample_population(
    states: np.ndarray,
    counts: np.ndarray,
    ancestors: np.ndarray,
    labels: np.ndarray,
    log_weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    indices, effective_population = systematic_indices(log_weights)
    population = states.shape[0]
    new_states = np.empty_like(states)
    new_counts = np.empty_like(counts)
    new_ancestors = np.empty_like(ancestors)
    new_labels = np.empty_like(labels)
    for destination in range(population):
        source = indices[destination]
        new_states[destination] = states[source]
        new_counts[destination] = counts[source]
        new_ancestors[destination] = ancestors[source]
        for row in range(labels.shape[0]):
            new_labels[row, destination] = labels[row, source]
    return (
        new_states,
        new_counts,
        new_ancestors,
        new_labels,
        effective_population,
    )


@njit(cache=True)
def propagate_sweep(
    states: np.ndarray,
    counts: np.ndarray,
    ancestors: np.ndarray,
    labels: np.ndarray,
    delta_v: float,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    resample_interval: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, float]:
    population = states.shape[0]
    plaquette_count = plaquette_links.shape[0]
    log_weights = np.zeros(population, dtype=np.float64)
    minimum_effective_population = float(population)
    for step in range(plaquette_count):
        for walker in range(population):
            count = counts[walker]
            branch = 1.0 - delta_v * count / plaquette_count
            log_weights[walker] += np.log(branch)
            plaquette = np.random.randint(plaquette_count)
            if (
                is_flippable(states[walker], plaquette_links[plaquette])
                and np.random.random() < 1.0 / branch
            ):
                counts[walker] = flip_and_update_count(
                    states[walker],
                    plaquette,
                    count,
                    plaquette_links,
                    affected_plaquettes,
                    affected_counts,
                )
        if (step + 1) % resample_interval == 0:
            (
                states,
                counts,
                ancestors,
                labels,
                effective_population,
            ) = resample_population(
                states, counts, ancestors, labels, log_weights
            )
            minimum_effective_population = min(
                minimum_effective_population, effective_population
            )
            log_weights[:] = 0.0
    if plaquette_count % resample_interval:
        (
            states,
            counts,
            ancestors,
            labels,
            effective_population,
        ) = resample_population(states, counts, ancestors, labels, log_weights)
        minimum_effective_population = min(
            minimum_effective_population, effective_population
        )
    return states, counts, ancestors, labels, minimum_effective_population


@njit(cache=True)
def evaluate_observables(
    states: np.ndarray,
    coefficient_real: np.ndarray,
    coefficient_imag: np.ndarray,
) -> np.ndarray:
    population = states.shape[0]
    mode_count = coefficient_real.shape[0]
    link_count = states.shape[1]
    result = np.zeros((population, mode_count), dtype=np.complex128)
    for walker in range(population):
        for mode in range(mode_count):
            real = 0.0
            imag = 0.0
            for link in range(link_count):
                electric = states[walker, link] - 0.5
                real += electric * coefficient_real[mode, link]
                imag += electric * coefficient_imag[mode, link]
            result[walker, mode] = real + 1j * imag
    return result


@njit(cache=True)
def prepare_population(
    start_state: np.ndarray,
    delta_v: float,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    resample_interval: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, float, float]:
    np.random.seed(seed)
    states = np.empty((population, start_state.shape[0]), dtype=np.uint8)
    counts = np.empty(population, dtype=np.int32)
    for walker in range(population):
        states[walker] = start_state
        counts[walker] = count_flippable(states[walker], plaquette_links)
    ancestors = np.arange(population, dtype=np.int32)
    labels = np.full((1, population), -1, dtype=np.int32)
    for _ in range(classical_sweeps):
        for step in range(plaquette_links.shape[0]):
            for walker in range(population):
                plaquette = np.random.randint(plaquette_links.shape[0])
                if is_flippable(states[walker], plaquette_links[plaquette]):
                    counts[walker] = flip_and_update_count(
                        states[walker],
                        plaquette,
                        counts[walker],
                        plaquette_links,
                        affected_plaquettes,
                        affected_counts,
                    )
    sample_count = min(40, burn_sweeps)
    count_samples = np.empty(sample_count, dtype=np.float64)
    minimum_effective_population = float(population)
    for sweep in range(burn_sweeps):
        states, counts, ancestors, labels, effective_population = propagate_sweep(
            states,
            counts,
            ancestors,
            labels,
            delta_v,
            plaquette_links,
            affected_plaquettes,
            affected_counts,
            resample_interval,
        )
        minimum_effective_population = min(
            minimum_effective_population, effective_population
        )
        if sweep >= burn_sweeps - sample_count:
            count_samples[sweep - burn_sweeps + sample_count] = np.mean(counts)
    return (
        states,
        counts,
        float(np.mean(count_samples)),
        minimum_effective_population,
    )


def transverse_coefficients(
    length: int, harmonics: tuple[int, ...] = (1, 2)
) -> tuple[np.ndarray, np.ndarray, list[tuple[int, int, int]]]:
    link_count = 3 * length**3
    modes: list[tuple[int, int, int]] = []
    coefficients: list[np.ndarray] = []
    normalization = np.sqrt(length**3)
    for harmonic in harmonics:
        if harmonic > length // 2:
            continue
        for momentum_axis in range(3):
            for polarization_axis in range(3):
                if polarization_axis == momentum_axis:
                    continue
                row = np.zeros(link_count, dtype=np.complex128)
                momentum = 2.0 * np.pi * harmonic / length
                for coordinate in np.ndindex(length, length, length):
                    flat = int(
                        np.ravel_multi_index(
                            (*coordinate, polarization_axis),
                            (length, length, length, 3),
                        )
                    )
                    stagger = (-1) ** sum(coordinate)
                    row[flat] = (
                        stagger
                        * np.exp(1j * momentum * coordinate[momentum_axis])
                        / normalization
                    )
                modes.append((harmonic, momentum_axis, polarization_axis))
                coefficients.append(row)
    matrix = np.asarray(coefficients)
    return matrix.real.copy(), matrix.imag.copy(), modes


@dataclass(frozen=True)
class ReplicaResult:
    correlations: np.ndarray
    correlation_blocks: np.ndarray
    population: int
    energy: float
    minimum_effective_population_fraction: float
    origin_survival_fraction: float
    origin_diversity_fractions: np.ndarray
    forward_survival_fractions: np.ndarray
    count_consistent: bool
    sector_consistent: bool


def measure_correlation_block(
    states: np.ndarray,
    counts: np.ndarray,
    delta_v: float,
    tau_max: int,
    forward_sweeps: int,
    coefficient_real: np.ndarray,
    coefficient_imag: np.ndarray,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    interval: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    float,
    float,
    np.ndarray,
    np.ndarray,
]:
    population = states.shape[0]
    mode_count = coefficient_real.shape[0]
    origin_observables = evaluate_observables(
        states, coefficient_real, coefficient_imag
    )
    tau_count = tau_max + 1
    ancestors = np.arange(population, dtype=np.int32)
    labels = np.full((tau_count, population), -1, dtype=np.int32)
    tau_origins = np.full((tau_count, population), -1, dtype=np.int32)
    tau_observables = np.zeros(
        (tau_count, population, mode_count), dtype=np.complex128
    )
    labels[0] = np.arange(population, dtype=np.int32)
    tau_origins[0] = ancestors
    tau_observables[0] = origin_observables
    minimum_effective = float(population)
    correlation = np.zeros((tau_count, mode_count), dtype=np.complex128)
    survival = np.zeros(tau_count, dtype=float)
    origin_diversity = np.zeros(tau_count, dtype=float)
    origin_diversity[0] = 1.0
    for sweep in range(tau_max + forward_sweeps + 1):
        if sweep > 0 and sweep <= tau_max:
            labels[sweep] = np.arange(population, dtype=np.int32)
            tau_origins[sweep] = ancestors
            tau_observables[sweep] = evaluate_observables(
                states, coefficient_real, coefficient_imag
            )
            origin_diversity[sweep] = len(np.unique(ancestors)) / population
        if sweep >= forward_sweeps:
            tau = sweep - forward_sweeps
            if tau <= tau_max:
                final_labels = labels[tau]
                survival[tau] = len(np.unique(final_labels)) / population
                products = np.empty(
                    (population, mode_count), dtype=np.complex128
                )
                for walker, label in enumerate(final_labels):
                    origin = tau_origins[tau, label]
                    products[walker] = origin_observables[origin] * np.conjugate(
                        tau_observables[tau, label]
                    )
                correlation[tau] = np.mean(products, axis=0)
        if sweep == tau_max + forward_sweeps:
            break
        states, counts, ancestors, labels, effective = propagate_sweep(
            states,
            counts,
            ancestors,
            labels,
            delta_v,
            plaquette_links,
            affected_plaquettes,
            affected_counts,
            interval,
        )
        minimum_effective = min(minimum_effective, effective)
    return (
        states,
        counts,
        correlation / correlation[0].real,
        minimum_effective,
        len(np.unique(ancestors)) / population,
        origin_diversity,
        survival,
    )


def run_replica(
    length: int,
    delta_v: float,
    *,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    tau_max: int,
    forward_sweeps: int,
    seed: int,
    harmonics: tuple[int, ...] = (1, 2),
    measurement_origins: int = 1,
    origin_spacing: int = 0,
    start_state: np.ndarray | None = None,
) -> tuple[ReplicaResult, list[tuple[int, int, int]]]:
    geometry = build_geometry(length)
    start = (
        initial_ice(length).ravel()
        if start_state is None
        else np.asarray(start_state, dtype=np.uint8).ravel()
    )
    interval = max(8, geometry.plaquette_count // 8)
    while geometry.plaquette_count % interval:
        interval -= 1
    states, counts, mean_count, minimum_effective = prepare_population(
        start,
        delta_v,
        population,
        classical_sweeps,
        burn_sweeps,
        geometry.plaquette_links,
        geometry.affected_plaquettes,
        geometry.affected_counts,
        interval,
        seed,
    )
    coefficient_real, coefficient_imag, modes = transverse_coefficients(
        length, harmonics
    )
    minimum_dynamic_effective = float(population)
    blocks: list[np.ndarray] = []
    block_origin_survival: list[float] = []
    block_origin_diversity: list[np.ndarray] = []
    block_forward_survival: list[np.ndarray] = []
    for origin_index in range(measurement_origins):
        (
            states,
            counts,
            correlation,
            effective,
            origin_survival,
            origin_diversity,
            survival,
        ) = measure_correlation_block(
            states,
            counts,
            delta_v,
            tau_max,
            forward_sweeps,
            coefficient_real,
            coefficient_imag,
            geometry.plaquette_links,
            geometry.affected_plaquettes,
            geometry.affected_counts,
            interval,
        )
        blocks.append(correlation)
        block_origin_survival.append(origin_survival)
        block_origin_diversity.append(origin_diversity)
        block_forward_survival.append(survival)
        minimum_dynamic_effective = min(minimum_dynamic_effective, effective)
        if origin_index + 1 < measurement_origins:
            ancestors = np.arange(population, dtype=np.int32)
            labels = np.full((1, population), -1, dtype=np.int32)
            for _ in range(origin_spacing):
                states, counts, ancestors, labels, effective = propagate_sweep(
                    states,
                    counts,
                    ancestors,
                    labels,
                    delta_v,
                    geometry.plaquette_links,
                    geometry.affected_plaquettes,
                    geometry.affected_counts,
                    interval,
                )
                minimum_dynamic_effective = min(
                    minimum_dynamic_effective, effective
                )
    normalized_blocks = np.asarray(blocks)
    reshaped = states.reshape((population, length, length, length, 3))
    sector_consistent = all(
        np.all(vertex_degrees(state) == 3)
        and electric_flux(state) == (0, 0, 0)
        for state in reshaped
    )
    count_consistent = all(
        count_flippable(state, geometry.plaquette_links) == count
        for state, count in zip(states, counts, strict=True)
    )
    return (
        ReplicaResult(
            correlations=np.mean(normalized_blocks, axis=0),
            correlation_blocks=normalized_blocks,
            population=population,
            energy=delta_v * mean_count,
            minimum_effective_population_fraction=min(
                minimum_effective, minimum_dynamic_effective
            )
            / population,
            origin_survival_fraction=min(block_origin_survival),
            origin_diversity_fractions=np.min(
                np.asarray(block_origin_diversity), axis=0
            ),
            forward_survival_fractions=np.min(
                np.asarray(block_forward_survival), axis=0
            ),
            count_consistent=count_consistent,
            sector_consistent=sector_consistent,
        ),
        modes,
    )


def exact_small_correlations(
    delta_v: float, tau_max: int
) -> tuple[float, np.ndarray, list[tuple[int, int, int]]]:
    length = 2
    orbit = build_small_rk_orbit(initial_ice(length))
    flippabilities = np.asarray(
        [len(small_flip_destinations(decode_small(state))) for state in orbit.states],
        dtype=float,
    )
    hamiltonian = orbit.hamiltonian + sparse.diags(delta_v * flippabilities)
    values, vectors = eigsh(
        hamiltonian,
        k=1,
        which="SA",
        v0=np.linspace(1.0, 2.0, len(orbit.states)),
        tol=1.0e-12,
    )
    ground_energy = float(values[0])
    ground = vectors[:, 0]
    if np.sum(ground) < 0:
        ground = -ground
    coefficient_real, coefficient_imag, modes = transverse_coefficients(
        length, (1,)
    )
    observables = np.empty((len(orbit.states), len(modes)), dtype=np.complex128)
    for row, state in enumerate(orbit.states):
        occupation = decode_small(state).ravel()
        centered = occupation.astype(float) - 0.5
        observables[row] = centered @ (
            coefficient_real + 1j * coefficient_imag
        ).T
    green = sparse.eye(len(orbit.states), format="csr") - hamiltonian / (
        3 * length**3
    )
    ground_green = 1.0 - ground_energy / (3 * length**3)
    correlations = np.empty((tau_max + 1, len(modes)), dtype=float)
    for mode in range(len(modes)):
        initial = observables[:, mode] * ground
        evolved = initial.copy()
        denominator = float(np.vdot(initial, initial).real)
        correlations[0, mode] = 1.0
        for tau in range(1, tau_max + 1):
            for _ in range(3 * length**3):
                evolved = green @ evolved
            correlations[tau, mode] = float(
                np.vdot(initial, evolved).real
                / (ground_green ** (tau * 3 * length**3) * denominator)
            )
    return ground_energy, correlations, modes


def grouped_correlations(
    replica: ReplicaResult, modes: list[tuple[int, int, int]]
) -> dict[int, np.ndarray]:
    result: dict[int, np.ndarray] = {}
    for harmonic in sorted({mode[0] for mode in modes}):
        indices = [index for index, mode in enumerate(modes) if mode[0] == harmonic]
        result[harmonic] = np.mean(replica.correlations[:, indices], axis=1)
    return result


def effective_gap(
    correlation: np.ndarray,
    length: int,
    ground_energy: float,
    fit_start: int,
    fit_stop: int,
) -> float:
    times = np.arange(fit_start, fit_stop + 1, dtype=float)
    values = correlation[fit_start : fit_stop + 1]
    if np.any(values <= 0.0):
        return float("nan")
    slope = float(np.polyfit(times, np.log(values), 1)[0])
    plaquette_count = 3 * length**3
    return (plaquette_count - ground_energy) * (
        1.0 - np.exp(slope / plaquette_count)
    )


@dataclass(frozen=True)
class GapSummary:
    length: int
    delta_v: float
    gap: float
    gap_error: float
    window_gaps: tuple[float, float, float]
    polarization_spread: float
    polarization_chi_squared: float
    imaginary_residual: float
    first_origin_gap: float
    last_origin_gap: float
    mean_correlation: np.ndarray


@dataclass(frozen=True)
class CrossoverFit:
    c_squared: float
    c_squared_error: float
    q4_coefficient: float
    q4_coefficient_error: float
    chi_squared: float


@dataclass(frozen=True)
class MassFit:
    mass_squared: float
    mass_squared_error: float
    chi_squared: float
    massless_chi_squared: float


def mean_and_error(values: np.ndarray) -> tuple[float, float]:
    finite = values[np.isfinite(values)]
    if len(finite) < 2:
        return float("nan"), float("nan")
    return float(np.mean(finite)), float(
        np.std(finite, ddof=1) / np.sqrt(len(finite))
    )


def summarize_gaps(
    length: int,
    delta_v: float,
    rows: list[tuple[ReplicaResult, list[tuple[int, int, int]]]],
) -> GapSummary:
    modes = rows[0][1]
    mode_indices = [index for index, mode in enumerate(modes) if mode[0] == 1]
    curves = np.asarray(
        [
            np.mean(result.correlations[:, mode_indices], axis=1)
            for result, _ in rows
        ]
    )
    energies = np.asarray([result.energy for result, _ in rows])
    gaps = np.asarray(
        [
            effective_gap(curve.real, length, energy, 2, 6)
            for curve, energy in zip(curves, energies, strict=True)
        ]
    )
    gap, gap_error = mean_and_error(gaps)
    window_gaps = []
    for fit_start, fit_stop in ((1, 4), (2, 6), (3, 8)):
        values = np.asarray(
            [
                effective_gap(
                    curve.real, length, energy, fit_start, fit_stop
                )
                for curve, energy in zip(curves, energies, strict=True)
            ]
        )
        window_gaps.append(mean_and_error(values)[0])
    polarization_gaps = []
    polarization_errors = []
    for mode_index in mode_indices:
        values = np.asarray(
            [
                effective_gap(
                    result.correlations[:, mode_index].real,
                    length,
                    result.energy,
                    2,
                    6,
                )
                for result, _ in rows
            ]
        )
        mode_gap, mode_error = mean_and_error(values)
        polarization_gaps.append(mode_gap)
        polarization_errors.append(mode_error)
    polarization_spread = (
        max(polarization_gaps) - min(polarization_gaps)
    ) / np.mean(polarization_gaps)
    polarization_weights = 1.0 / np.maximum(
        np.asarray(polarization_errors), 1.0e-12
    ) ** 2
    polarization_mean = float(
        np.sum(polarization_weights * polarization_gaps)
        / np.sum(polarization_weights)
    )
    polarization_chi_squared = float(
        np.sum(
            polarization_weights
            * (np.asarray(polarization_gaps) - polarization_mean) ** 2
        )
    )
    mean_curve = np.mean(curves, axis=0)
    imaginary_residual = float(np.max(np.abs(mean_curve.imag[:7])))
    first_gaps = []
    last_gaps = []
    for result, _ in rows:
        first_curve = np.mean(
            result.correlation_blocks[0, :, mode_indices], axis=0
        )
        last_curve = np.mean(
            result.correlation_blocks[-1, :, mode_indices], axis=0
        )
        first_gaps.append(
            effective_gap(first_curve.real, length, result.energy, 2, 6)
        )
        last_gaps.append(
            effective_gap(last_curve.real, length, result.energy, 2, 6)
        )
    return GapSummary(
        length=length,
        delta_v=delta_v,
        gap=gap,
        gap_error=gap_error,
        window_gaps=tuple(window_gaps),
        polarization_spread=float(polarization_spread),
        polarization_chi_squared=polarization_chi_squared,
        imaginary_residual=imaginary_residual,
        first_origin_gap=mean_and_error(np.asarray(first_gaps))[0],
        last_origin_gap=mean_and_error(np.asarray(last_gaps))[0],
        mean_correlation=mean_curve,
    )


def fit_crossover(
    rows: list[GapSummary], baseline: list[GapSummary] | None = None
) -> CrossoverFit:
    q_values = np.asarray(
        [2.0 * np.sin(np.pi / row.length) for row in rows]
    )
    response = np.asarray([(row.gap / q) ** 2 for row, q in zip(rows, q_values)])
    errors = np.asarray(
        [
            2.0 * row.gap * row.gap_error / q**2
            for row, q in zip(rows, q_values)
        ]
    )
    if baseline is not None:
        baseline_response = np.asarray(
            [
                (row.gap / q) ** 2
                for row, q in zip(baseline, q_values, strict=True)
            ]
        )
        baseline_errors = np.asarray(
            [
                2.0 * row.gap * row.gap_error / q**2
                for row, q in zip(baseline, q_values, strict=True)
            ]
        )
        response = response - baseline_response
        errors = np.hypot(errors, baseline_errors)
    design = np.column_stack((np.ones(len(rows)), q_values**2))
    weights = np.diag(1.0 / errors**2)
    covariance = np.linalg.inv(design.T @ weights @ design)
    coefficients = covariance @ (design.T @ weights @ response)
    residual = (response - design @ coefficients) / errors
    return CrossoverFit(
        c_squared=float(coefficients[0]),
        c_squared_error=float(np.sqrt(covariance[0, 0])),
        q4_coefficient=float(coefficients[1]),
        q4_coefficient_error=float(np.sqrt(covariance[1, 1])),
        chi_squared=float(np.dot(residual, residual)),
    )


def pure_dispersion_chi(rows: list[GapSummary], power: int) -> float:
    q_values = np.asarray(
        [2.0 * np.sin(np.pi / row.length) for row in rows]
    )
    response = np.asarray([row.gap for row in rows])
    errors = np.asarray([row.gap_error for row in rows])
    predictor = q_values**power
    coefficient = float(
        np.sum(predictor * response / errors**2)
        / np.sum(predictor**2 / errors**2)
    )
    return float(np.sum(((response - coefficient * predictor) / errors) ** 2))


def mass_resolution_fit(rows: list[GapSummary]) -> MassFit:
    q_values = np.asarray(
        [2.0 * np.sin(np.pi / row.length) for row in rows]
    )
    response = np.asarray([row.gap**2 for row in rows])
    errors = np.asarray([2.0 * row.gap * row.gap_error for row in rows])
    design = np.column_stack(
        (np.ones(len(rows)), q_values**2, q_values**4)
    )
    weights = np.diag(1.0 / errors**2)
    covariance = np.linalg.inv(design.T @ weights @ design)
    coefficients = covariance @ (design.T @ weights @ response)
    residual = (response - design @ coefficients) / errors
    massless_design = design[:, 1:]
    massless_covariance = np.linalg.inv(
        massless_design.T @ weights @ massless_design
    )
    massless_coefficients = massless_covariance @ (
        massless_design.T @ weights @ response
    )
    massless_residual = (
        response - massless_design @ massless_coefficients
    ) / errors
    return MassFit(
        mass_squared=float(coefficients[0]),
        mass_squared_error=float(np.sqrt(covariance[0, 0])),
        chi_squared=float(np.dot(residual, residual)),
        massless_chi_squared=float(
            np.dot(massless_residual, massless_residual)
        ),
    )


def joint_detuning_fit(
    baseline: list[GapSummary],
    detuned: dict[float, list[GapSummary]],
) -> tuple[float, float, float]:
    design_rows = []
    response = []
    errors = []
    reference_terms = []
    ordered_detunings = sorted(detuned)
    baseline_by_length = {row.length: row for row in baseline}
    for detuning_index, delta_v in enumerate(ordered_detunings):
        for row in detuned[delta_v]:
            reference = baseline_by_length[row.length]
            q_value = 2.0 * np.sin(np.pi / row.length)
            response.append(
                (row.gap / q_value) ** 2
                - (reference.gap / q_value) ** 2
            )
            errors.append(
                np.hypot(
                    2.0 * row.gap * row.gap_error / q_value**2,
                    2.0
                    * reference.gap
                    * reference.gap_error
                    / q_value**2,
                )
            )
            reference_terms.append((row.length, 2.0 * reference.gap * reference.gap_error / q_value**2))
            slopes = [0.0] * len(ordered_detunings)
            slopes[detuning_index] = q_value**2
            design_rows.append([abs(delta_v), *slopes])
    matrix = np.asarray(design_rows)
    values = np.asarray(response)
    uncertainties = np.asarray(errors)
    observation_covariance = np.diag(uncertainties**2)
    for i, (length_i, error_i) in enumerate(reference_terms):
        for j, (length_j, error_j) in enumerate(reference_terms):
            if i != j and length_i == length_j:
                observation_covariance[i, j] = error_i * error_j
    validate_covariance(observation_covariance, positive_definite=True)
    weights = np.linalg.inv(observation_covariance)
    covariance = np.linalg.inv(matrix.T @ weights @ matrix)
    coefficients = covariance @ (matrix.T @ weights @ values)
    residual = values - matrix @ coefficients
    return (
        float(coefficients[0]),
        float(np.sqrt(covariance[0, 0])),
        float(residual @ weights @ residual),
    )


def run_gap_control(
    length: int,
    delta_v: float,
    *,
    population: int,
    replicas: int,
    classical_sweeps: int,
    burn_sweeps: int,
    forward_sweeps: int,
    origins: int,
    seed: int,
    start_state: np.ndarray | None = None,
) -> tuple[float, list[tuple[ReplicaResult, list[tuple[int, int, int]]]]]:
    rows = [
        run_replica(
            length,
            delta_v,
            population=population,
            classical_sweeps=classical_sweeps,
            burn_sweeps=burn_sweeps,
            tau_max=10,
            forward_sweeps=forward_sweeps,
            seed=seed + replica,
            harmonics=(1,),
            measurement_origins=origins,
            origin_spacing=2,
            start_state=start_state,
        )
        for replica in range(replicas)
    ]
    # Preserve every actual control record for caller-side final aggregation.
    return summarize_gaps(length, delta_v, rows).gap, rows


def main() -> int:
    check_inputs(Path(__file__).resolve().parent.parent, AUDIT_EXPECTED_SHA256)
    checks = Checks()
    receipt=load_receipt("spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt")
    pattern=re.compile(r"^GAP V=([0-9.]+) L=(\d+) q=[0-9.]+ omega=([0-9.]+)\+/-([0-9.]+) ",re.M)
    rows={}
    for match in pattern.finditer(receipt.stdout):
        key=(float(match[1]),int(match[2]))
        if key in rows: raise ValueError("duplicate historical gap")
        rows[key]=SimpleNamespace(length=key[1],gap=float(match[3]),gap_error=float(match[4]))
    expected={(v,l) for v,ls in ((1.,(6,8,10,12,14)),(.95,(6,8,10,12)),(.90,(6,8,10,12,14))) for l in ls}
    checks.check(set(rows)==expected and receipt.total==(16,0), "all fourteen historical gap values and sixteen old checks are preserved")
    baseline=[r for (v,l),r in sorted(rows.items()) if v==1.]
    detuned={v-1:[r for (coupling,l),r in sorted(rows.items()) if coupling==v] for v in (.90,.95)}
    for delta, group in detuned.items():
        reference=[rows[(1.,r.length)] for r in group]
        fit=fit_crossover(group,reference)
        separate=(pure_dispersion_chi(group,1),pure_dispersion_chi(group,2))
        checks.check(np.all(np.isfinite([fit.c_squared,fit.chi_squared,*separate])),
            f"detuning {delta:.2f} retains finite separate diagnostic fits, with no cross-response model selection")
        print("HISTORICAL_FIT_REANALYSIS",f"delta={delta:.2f}",f"excess_c2={fit.c_squared:.8f}",f"excess_chi2={fit.chi_squared:.6f}",f"unsubtracted_pure_losses={separate}","losses_comparable=False")
    coefficient,error,loss=joint_detuning_fit(baseline,detuned)
    checks.check(np.all(np.isfinite([coefficient,error,loss])) and error>0,
        "joint detuning fit includes the common RK reference covariance")
    print("CORRECTED_SHARED_RK_FIT",f"coefficient={coefficient:.8f}",f"error={error:.8f}",f"chi2={loss:.8f}","nominal_delta_method_only=True")
    good=SimpleNamespace(count_consistent=True,sector_consistent=True,population=100,
        minimum_effective_population_fraction=.95,origin_diversity_fractions=np.ones(7),forward_survival_fractions=np.ones(7))
    bad=SimpleNamespace(**vars(good));bad.sector_consistent=False
    checks.check(spectral_health([good]) and not spectral_health([good,bad]),
        "final returned-control health aggregation rejects a later sector failure")
    energy,correlations,modes=exact_small_correlations(-.10,4)
    checks.check(np.isfinite(energy) and np.all(np.isfinite(correlations)) and np.allclose(correlations[0],1),
        "finite supplied-component Green normalization is retained")
    print("SCOPE: finite supplied Green/observable definitions and historical fits; late-control health not reconstructed; long production, asymptotic pole, physical clock and Maxwell matching held")
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
    'docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md': '0d40064ad01d7754e65b787c2697c248b206624844a7098d83ebf7834cbc4b04',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c1cc8df7ae97504527fd26195e65670ad6ccf4e01982d0665040662b22ba0d7e',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md': '16433c4b9b823cfbf453687be3bcfffc880542c72bb17180a8bd4c66f64352f8',
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
