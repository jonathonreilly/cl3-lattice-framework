#!/usr/bin/env python3
"""Forward-walking transverse correlators in finite-detuning cubic ice.

This runner applies the exact positive Green kernel

    G = I - H/M,  M = 3 L^3,

to the spin-half cubic-ice Hamiltonian used by the parent finite-detuning
stiffness calculations.  Descendant labels supply a forward-walking estimate
of the pure imaginary-time transverse electric-field autocorrelation.
"""

from __future__ import annotations

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
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py",
)

AUDIT_TIMEOUT_SEC = 1800


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
            slopes = [0.0] * len(ordered_detunings)
            slopes[detuning_index] = q_value**2
            design_rows.append([abs(delta_v), *slopes])
    matrix = np.asarray(design_rows)
    values = np.asarray(response)
    uncertainties = np.asarray(errors)
    weights = np.diag(1.0 / uncertainties**2)
    covariance = np.linalg.inv(matrix.T @ weights @ matrix)
    coefficients = covariance @ (matrix.T @ weights @ values)
    residual = (values - matrix @ coefficients) / uncertainties
    return (
        float(coefficients[0]),
        float(np.sqrt(covariance[0, 0])),
        float(np.dot(residual, residual)),
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
) -> float:
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
    return summarize_gaps(length, delta_v, rows).gap


def main() -> int:
    checks = Checks()
    tau_max = 8
    exact_energy, exact_correlation, exact_modes = exact_small_correlations(
        -0.10, tau_max
    )
    small_replicas: list[ReplicaResult] = []
    for replica in range(6):
        result, modes = run_replica(
            2,
            -0.10,
            population=512,
            classical_sweeps=80,
            burn_sweeps=120,
            tau_max=tau_max,
            forward_sweeps=4,
            seed=7_000_000 + replica,
            harmonics=(1,),
            measurement_origins=4,
            origin_spacing=2,
        )
        if modes != exact_modes:
            raise AssertionError("small-mode ordering mismatch")
        small_replicas.append(result)
    small_mean = np.mean(
        [np.mean(result.correlations, axis=1) for result in small_replicas],
        axis=0,
    )
    exact_mean = np.mean(exact_correlation, axis=1)
    checks.check(
        np.max(np.abs(small_mean[:5].real - exact_mean[:5])) < 0.06,
        "forward walking reproduces the exact L=2 normalized transverse correlator through tau=4",
    )
    checks.check(
        abs(np.mean([result.energy for result in small_replicas]) - exact_energy)
        < 0.01,
        "the independent L=2 populations reproduce the exact finite-detuning ground energy",
    )

    primary: dict[
        tuple[float, int],
        list[tuple[ReplicaResult, list[tuple[int, int, int]]]],
    ] = {}
    lengths_by_detuning = {
        0.0: (6, 8, 10, 12, 14),
        -0.05: (6, 8, 10, 12),
        -0.10: (6, 8, 10, 12, 14),
    }
    for delta_index, delta_v in enumerate((0.0, -0.05, -0.10)):
        population = 384 if delta_v == 0.0 else 512
        origins = 4 if delta_v == 0.0 else 6
        burn_sweeps = 100 if delta_v == 0.0 else 140
        for length in lengths_by_detuning[delta_v]:
            row_population = (
                1024 if delta_v == -0.10 and length == 14 else population
            )
            row_origins = (
                4 if delta_v == -0.10 and length == 14 else origins
            )
            default_seed = (
                8_000_000
                + 100_000 * delta_index
                + 1_000 * length
            )
            if length == 14 and delta_v == 0.0:
                seeds = [19_100_000 + replica for replica in range(4)]
            elif length == 14 and delta_v == -0.10:
                seeds = [19_000_000 + replica for replica in range(4)]
            else:
                seeds = [default_seed + replica for replica in range(4)]
            if length == 12 and delta_v == -0.10:
                seeds.extend(19_201_200 + replica for replica in range(4))
            primary[(delta_v, length)] = [
                run_replica(
                    length,
                    delta_v,
                    population=row_population,
                    classical_sweeps=80,
                    burn_sweeps=burn_sweeps,
                    tau_max=10,
                    forward_sweeps=4,
                    seed=seed,
                    harmonics=(1,),
                    measurement_origins=row_origins,
                    origin_spacing=2,
                )
                for seed in seeds
            ]

    all_rows = [row for rows in primary.values() for row, _ in rows]
    checks.check(
        all(row.count_consistent and row.sector_consistent for row in all_rows),
        "every dynamical population preserves local counts, Gauss charge, and zero electric flux",
    )
    checks.check(
        min(row.minimum_effective_population_fraction for row in all_rows) > 0.85
        and min(
            row.population * row.forward_survival_fractions[0]
            for row in all_rows
        )
        >= 16
        and min(
            row.population * row.origin_diversity_fractions[6]
            for row in all_rows
        )
        >= 10,
        "effective weights and absolute fitted-time descendant counts remain above the declared genealogy controls",
    )
    summaries: dict[float, list[GapSummary]] = {}
    for delta_v in (0.0, -0.05, -0.10):
        summaries[delta_v] = [
            summarize_gaps(length, delta_v, primary[(delta_v, length)])
            for length in lengths_by_detuning[delta_v]
        ]
    checks.check(
        all(
            np.all(row.mean_correlation.real[:7] > 0.0)
            and row.imaginary_residual < 0.06
            for rows in summaries.values()
            for row in rows
        ),
        "every fitted correlation remains positive and its cubic-average imaginary residual stays below six percent",
    )
    mode_orbit = {
        (momentum_axis, polarization_axis)
        for momentum_axis in range(3)
        for polarization_axis in range(3)
        if momentum_axis != polarization_axis
    }
    cubic_orbit_closed = all(
        {
            (permutation[momentum_axis], permutation[polarization_axis])
            for momentum_axis, polarization_axis in mode_orbit
        }
        == mode_orbit
        for permutation in permutations(range(3))
    )
    symmetric_start = initial_ice(6)
    initial_state_covariant = True
    for permutation in permutations(range(3)):
        for coordinate in np.ndindex(6, 6, 6):
            mapped_coordinate = [0, 0, 0]
            for axis in range(3):
                mapped_coordinate[permutation[axis]] = coordinate[axis]
            for axis in range(3):
                initial_state_covariant = initial_state_covariant and bool(
                    symmetric_start[coordinate][axis]
                    == symmetric_start[tuple(mapped_coordinate)][
                        permutation[axis]
                    ]
                )
    checks.check(
        cubic_orbit_closed
        and initial_state_covariant
        and build_geometry(6).plaquette_links.shape == (648, 4),
        "the Hamiltonian orientations, symmetric start, and six measured transverse modes close under every axis permutation",
    )
    checks.check(
        all(
            row.gap > 5.0 * row.gap_error
            and (max(row.window_gaps) - min(row.window_gaps)) / row.gap
            < 0.25
            for rows in summaries.values()
            for row in rows
        ),
        "every decay is resolved and stable across three predeclared imaginary-time windows",
    )

    rk_fit = fit_crossover(summaries[0.0])
    detuned_fits = {
        delta_v: fit_crossover(
            summaries[delta_v],
            baseline=[
                next(
                    row
                    for row in summaries[0.0]
                    if row.length == detuned_row.length
                )
                for detuned_row in summaries[delta_v]
            ],
        )
        for delta_v in (-0.05, -0.10)
    }
    checks.check(
        rk_fit.q4_coefficient > 20.0 * rk_fit.q4_coefficient_error
        and abs(rk_fit.c_squared)
        < max(4.0 * rk_fit.c_squared_error, 0.10 * rk_fit.q4_coefficient)
        and pure_dispersion_chi(summaries[0.0], 2) < 20.0,
        "the RK control selects quadratic q^2 decay with no resolved linear infrared term",
    )
    checks.check(
        all(
            fit.c_squared > 3.0 * fit.c_squared_error
            for fit in detuned_fits.values()
        ),
        "both finite detunings resolve a positive q^2 term in omega squared after subtracting the RK control",
    )
    checks.check(
        all(
            fit.chi_squared
            < 0.25
            * min(
                pure_dispersion_chi(summaries[delta_v], 1),
                pure_dispersion_chi(summaries[delta_v], 2),
            )
            for delta_v, fit in detuned_fits.items()
        ),
        "the linear-plus-quadratic crossover beats pure linear and pure quadratic dispersions at both detunings",
    )
    mass_fits = {
        delta_v: mass_resolution_fit(summaries[delta_v])
        for delta_v in (-0.05, -0.10)
    }
    checks.check(
        all(
            abs(fit.mass_squared) < 2.0 * fit.mass_squared_error
            and fit.massless_chi_squared - fit.chi_squared < 4.0
            for fit in mass_fits.values()
        ),
        "adding a mass term gives no two-sigma mass and no significant one-parameter fit improvement",
    )
    gamma, gamma_error, joint_chi = joint_detuning_fit(
        summaries[0.0],
        {delta_v: summaries[delta_v] for delta_v in (-0.05, -0.10)},
    )
    checks.check(
        gamma > 5.0 * gamma_error
        and joint_chi < 20.0
        and detuned_fits[-0.10].c_squared
        > detuned_fits[-0.05].c_squared,
        "the infrared coefficient grows monotonically and a common coefficient times |delta V| fits both ladders",
    )

    parent_electric_stiffness = {-0.05: 0.162638, -0.10: 0.321114}
    parent_magnetic_stiffness = 0.2598
    dynamic_magnetic = {
        delta_v: detuned_fits[delta_v].c_squared
        / parent_electric_stiffness[delta_v]
        for delta_v in (-0.05, -0.10)
    }
    checks.check(
        all(value > 0.0 for value in dynamic_magnetic.values())
        and abs(dynamic_magnetic[-0.05] - parent_magnetic_stiffness)
        / parent_magnetic_stiffness
        < 0.45,
        "c^2/U is positive at both detunings and the weak-detuning value is consistent within forty-five percent with the independent RK flux response",
    )

    forward_controls = {
        forward: run_gap_control(
            8,
            -0.05,
            population=384,
            replicas=3,
            classical_sweeps=60,
            burn_sweeps=100,
            forward_sweeps=forward,
            origins=4,
            seed=9_000_000 + 100 * forward,
        )
        for forward in (0, 2, 6)
    }
    forward_controls[4] = summaries[-0.05][1].gap
    checks.check(
        (max(forward_controls.values()) - min(forward_controls.values()))
        / np.mean(list(forward_controls.values()))
        < 0.12,
        "zero-, two-, four-, and six-sweep forward projections give the same L=8 gap within twelve percent",
    )
    population_control = run_gap_control(
        8,
        -0.05,
        population=1024,
        replicas=3,
        classical_sweeps=100,
        burn_sweeps=200,
        forward_sweeps=4,
        origins=4,
        seed=9_100_000,
    )
    checks.check(
        abs(population_control - summaries[-0.05][1].gap)
        / summaries[-0.05][1].gap
        < 0.12,
        "doubling the population and lengthening equilibration reproduce the L=8 gap",
    )
    component_controls = []
    for axis in range(3):
        component_controls.append(
            run_gap_control(
                8,
                -0.05,
                population=384,
                replicas=2,
                classical_sweeps=60,
                burn_sweeps=100,
                forward_sweeps=4,
                origins=4,
                seed=9_200_000 + 100 * axis,
                start_state=neutral_flux_pair_start(8, axis, axis + 1),
            )
        )
    checks.check(
        all(
            abs(value - summaries[-0.05][1].gap)
            / summaries[-0.05][1].gap
            < 0.20
            for value in component_controls
        ),
        "three nonlocal zero-flux starts reproduce the primary L=8 decay within twenty percent",
    )

    for delta_v, rows in summaries.items():
        for row in rows:
            print(
                "GAP",
                f"V={1.0 + delta_v:.2f}",
                f"L={row.length}",
                f"q={2.0 * np.sin(np.pi / row.length):.6f}",
                f"omega={row.gap:.6f}+/-{row.gap_error:.6f}",
                "windows=" + ",".join(f"{value:.6f}" for value in row.window_gaps),
                f"pol_spread={row.polarization_spread:.4f}",
                f"pol_chi2={row.polarization_chi_squared:.4f}",
                f"imag={row.imaginary_residual:.4f}",
            )
    print(
        "RK_FIT",
        f"c2={rk_fit.c_squared:.8f}+/-{rk_fit.c_squared_error:.8f}",
        f"a2={rk_fit.q4_coefficient:.8f}+/-{rk_fit.q4_coefficient_error:.8f}",
        f"chi2={rk_fit.chi_squared:.4f}",
    )
    for delta_v, fit in detuned_fits.items():
        print(
            "EXCESS_FIT",
            f"V={1.0 + delta_v:.2f}",
            f"c2={fit.c_squared:.8f}+/-{fit.c_squared_error:.8f}",
            f"q2_slope={fit.q4_coefficient:.8f}+/-{fit.q4_coefficient_error:.8f}",
            f"chi2={fit.chi_squared:.4f}",
            f"Kdyn={dynamic_magnetic[delta_v]:.6f}",
            f"mass2={mass_fits[delta_v].mass_squared:.6f}+/-{mass_fits[delta_v].mass_squared_error:.6f}",
            f"mass_delta_chi2={mass_fits[delta_v].massless_chi_squared - mass_fits[delta_v].chi_squared:.4f}",
        )
    print(
        "DETUNING_JOIN",
        f"c2_per_abs_delta={gamma:.6f}+/-{gamma_error:.6f}",
        f"chi2={joint_chi:.4f}",
    )
    print(
        "FORWARD_CONTROL",
        ",".join(
            f"F={forward}:{value:.6f}"
            for forward, value in sorted(forward_controls.items())
        ),
    )
    print(
        "POPULATION_CONTROL",
        f"primary={summaries[-0.05][1].gap:.6f}",
        f"doubled={population_control:.6f}",
    )
    print(
        "COMPONENT_CONTROL",
        ",".join(
            f"axis={axis}:{value:.6f}"
            for axis, value in enumerate(component_controls)
        ),
    )
    print(
        "GENEALOGY_CONTROL",
        f"min_ess_fraction={min(row.minimum_effective_population_fraction for row in all_rows):.6f}",
        f"min_forward_count={min(row.population * row.forward_survival_fractions[0] for row in all_rows):.0f}",
        f"min_origin_tau6_count={min(row.population * row.origin_diversity_fractions[6] for row in all_rows):.0f}",
    )
    print(
        "SMALL_EXACT",
        f"E0={exact_energy:.9f}",
        "C=" + ",".join(f"{value:.6f}" for value in exact_mean),
    )
    print(
        "SMALL_PROJECTOR",
        "C=" + ",".join(f"{value.real:.6f}" for value in small_mean),
    )
    print(
        "per_mode: the first transverse momentum has a fitted finite-volume decay; no thermodynamic pole is claimed"
    )
    print(
        "per_block: exact L=2 calibration and projector L=6,8,10,12,14 populations are checked"
    )
    print(
        "lattice_wide: finite-volume forward walking is executed; continuum light identification remains open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
