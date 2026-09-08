#!/usr/bin/env python3
"""Finite-delta-V projector Monte Carlo for the spin-half cubic-ice model.

The Hamiltonian is

    H(V) = - sum_p (|clockwise><counterclockwise| + h.c.) + V N_f

inside a fixed three-of-six ice and electric-flux sector.  At V=1 it is the
Rokhsar-Kivelson graph Laplacian.  For V<1 it is stoquastic.  The runner uses
the exact positive Green function G=I-H/M, where M=3L^3 is the number of
oriented square roots, together with fixed-population stochastic
reconfiguration.  A constant trial state makes the mixed estimator simply
(V-1)<N_f>.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
from numba import njit
from scipy import sparse
from scipy.sparse.linalg import eigsh

from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
    build_small_rk_orbit,
    decode_small,
    electric_flux,
    initial_ice,
    small_flip_destinations,
    vertex_degrees,
)
from spin_half_cubic_ice_topological_electric_stiffness_2026_09_03 import (
    insert_flux_lines,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py",
    "scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py",
)

AUDIT_TIMEOUT_SEC = 480


ORIENTATIONS = ((0, 1), (0, 2), (1, 2))


@dataclass(frozen=True)
class Geometry:
    length: int
    plaquette_links: np.ndarray
    affected_plaquettes: np.ndarray
    affected_counts: np.ndarray

    @property
    def link_count(self) -> int:
        return 3 * self.length**3

    @property
    def plaquette_count(self) -> int:
        return 3 * self.length**3


def link_index(length: int, coordinate: tuple[int, int, int], axis: int) -> int:
    return int(np.ravel_multi_index((*coordinate, axis), (length, length, length, 3)))


def build_geometry(length: int) -> Geometry:
    plaquettes: list[tuple[int, int, int, int]] = []
    for first_axis, second_axis in ORIENTATIONS:
        for root in np.ndindex(length, length, length):
            first_neighbor = list(root)
            first_neighbor[first_axis] = (first_neighbor[first_axis] + 1) % length
            second_neighbor = list(root)
            second_neighbor[second_axis] = (second_neighbor[second_axis] + 1) % length
            plaquettes.append(
                (
                    link_index(length, root, first_axis),
                    link_index(length, tuple(first_neighbor), second_axis),
                    link_index(length, tuple(second_neighbor), first_axis),
                    link_index(length, root, second_axis),
                )
            )
    plaquette_links = np.asarray(plaquettes, dtype=np.int32)
    link_to_plaquettes: list[list[int]] = [[] for _ in range(3 * length**3)]
    for plaquette, links in enumerate(plaquettes):
        for link in links:
            link_to_plaquettes[link].append(plaquette)
    affected: list[tuple[int, ...]] = []
    for links in plaquettes:
        affected.append(
            tuple(
                sorted(
                    {
                        neighbor
                        for link in links
                        for neighbor in link_to_plaquettes[link]
                    }
                )
            )
        )
    width = max(len(values) for values in affected)
    padded = np.full((len(affected), width), -1, dtype=np.int32)
    counts = np.empty(len(affected), dtype=np.int32)
    for row, values in enumerate(affected):
        counts[row] = len(values)
        padded[row, : len(values)] = values
    return Geometry(
        length=length,
        plaquette_links=plaquette_links,
        affected_plaquettes=padded,
        affected_counts=counts,
    )


def neutral_flux_pair_start(length: int, axis: int, offset: int) -> np.ndarray:
    """Flip two oppositely oriented winding lines while keeping net flux zero."""
    result = initial_ice(length)
    transverse = [index for index in range(3) if index != axis]
    positions = [
        (first, second)
        for first in range(length)
        for second in range(length)
    ]
    shift = offset % len(positions)
    positions = positions[shift:] + positions[:shift]
    used: set[tuple[int, int]] = set()
    for desired in (1, -1):
        found = False
        for first, second in positions:
            if (first, second) in used:
                continue
            candidate = result.copy()
            line = [slice(None), slice(None), slice(None), axis]
            line[transverse[0]] = first
            line[transverse[1]] = second
            before = electric_flux(result)[axis]
            candidate[tuple(line)] ^= 1
            after = electric_flux(candidate)[axis]
            if after - before == desired:
                result = candidate
                used.add((first, second))
                found = True
                break
        if not found:
            raise ValueError("could not build a neutral opposite winding-line pair")
    if electric_flux(result) != (0, 0, 0):
        raise AssertionError("neutral line pair changed total flux")
    if not np.all(vertex_degrees(result) == 3):
        raise AssertionError("neutral line pair changed Gauss charge")
    return result


@njit(cache=True)
def is_flippable(state: np.ndarray, links: np.ndarray) -> bool:
    first_low = state[links[0]]
    second_high = state[links[1]]
    first_high = state[links[2]]
    second_low = state[links[3]]
    return (
        first_low == first_high
        and second_low == second_high
        and first_low != second_low
    )


@njit(cache=True)
def count_flippable(state: np.ndarray, plaquette_links: np.ndarray) -> int:
    count = 0
    for plaquette in range(plaquette_links.shape[0]):
        if is_flippable(state, plaquette_links[plaquette]):
            count += 1
    return count


@njit(cache=True)
def flip_and_update_count(
    state: np.ndarray,
    plaquette: int,
    current_count: int,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
) -> int:
    before = 0
    for slot in range(affected_counts[plaquette]):
        neighbor = affected_plaquettes[plaquette, slot]
        if is_flippable(state, plaquette_links[neighbor]):
            before += 1
    for link in plaquette_links[plaquette]:
        state[link] ^= np.uint8(1)
    after = 0
    for slot in range(affected_counts[plaquette]):
        neighbor = affected_plaquettes[plaquette, slot]
        if is_flippable(state, plaquette_links[neighbor]):
            after += 1
    return current_count + after - before


@njit(cache=True)
def systematic_resample(
    states: np.ndarray,
    flippable_counts: np.ndarray,
    log_weights: np.ndarray,
) -> tuple[np.ndarray, np.ndarray]:
    population = states.shape[0]
    maximum = np.max(log_weights)
    weights = np.exp(log_weights - maximum)
    total = np.sum(weights)
    cumulative = np.cumsum(weights / total)
    offset = np.random.random() / population
    output_states = np.empty_like(states)
    output_counts = np.empty_like(flippable_counts)
    source = 0
    for destination in range(population):
        position = offset + destination / population
        while source + 1 < population and cumulative[source] < position:
            source += 1
        output_states[destination] = states[source]
        output_counts[destination] = flippable_counts[source]
    return output_states, output_counts


@njit(cache=True)
def run_population_core(
    start_state: np.ndarray,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    delta_v: float,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    sample_sweeps: int,
    resample_interval: int,
    seed: int,
) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    np.random.seed(seed)
    plaquette_count = plaquette_links.shape[0]
    link_count = start_state.shape[0]
    states = np.empty((population, link_count), dtype=np.uint8)
    flippable_counts = np.empty(population, dtype=np.int32)
    for walker in range(population):
        states[walker] = start_state
        flippable_counts[walker] = count_flippable(
            states[walker], plaquette_links
        )

    # Symmetric random-plaquette dynamics has the uniform RK distribution.
    # Independent walkers are decorrelated before projector branching begins.
    for _ in range(classical_sweeps * plaquette_count):
        for walker in range(population):
            plaquette = np.random.randint(plaquette_count)
            if is_flippable(states[walker], plaquette_links[plaquette]):
                flippable_counts[walker] = flip_and_update_count(
                    states[walker],
                    plaquette,
                    flippable_counts[walker],
                    plaquette_links,
                    affected_plaquettes,
                    affected_counts,
                )

    total_steps = (burn_sweeps + sample_sweeps) * plaquette_count
    first_sample_step = burn_sweeps * plaquette_count
    sample_interval = plaquette_count
    samples = np.empty(sample_sweeps, dtype=np.float64)
    effective_populations = np.empty(sample_sweeps, dtype=np.float64)
    count_checks = np.empty(sample_sweeps, dtype=np.int32)
    sample_index = 0
    log_weights = np.zeros(population, dtype=np.float64)
    minimum_effective_population = float(population)

    for step in range(total_steps):
        for walker in range(population):
            count = flippable_counts[walker]
            branch = 1.0 - delta_v * count / plaquette_count
            log_weights[walker] += np.log(branch)
            plaquette = np.random.randint(plaquette_count)
            if (
                is_flippable(states[walker], plaquette_links[plaquette])
                and np.random.random() < 1.0 / branch
            ):
                flippable_counts[walker] = flip_and_update_count(
                    states[walker],
                    plaquette,
                    count,
                    plaquette_links,
                    affected_plaquettes,
                    affected_counts,
                )

        if (step + 1) % resample_interval == 0:
            maximum = np.max(log_weights)
            weights = np.exp(log_weights - maximum)
            effective_population = np.sum(weights) ** 2 / np.sum(weights**2)
            minimum_effective_population = min(
                minimum_effective_population, effective_population
            )
            states, flippable_counts = systematic_resample(
                states, flippable_counts, log_weights
            )
            log_weights[:] = 0.0
        else:
            effective_population = float(population)

        if step + 1 >= first_sample_step and (
            step + 1 - first_sample_step
        ) % sample_interval == 0:
            maximum = np.max(log_weights)
            weights = np.exp(log_weights - maximum)
            samples[sample_index] = np.sum(
                weights * flippable_counts
            ) / np.sum(weights)
            current_effective_population = (
                np.sum(weights) ** 2 / np.sum(weights**2)
            )
            minimum_effective_population = min(
                minimum_effective_population, current_effective_population
            )
            effective_populations[sample_index] = minimum_effective_population
            walker = sample_index % population
            count_checks[sample_index] = (
                count_flippable(states[walker], plaquette_links)
                - flippable_counts[walker]
            )
            sample_index += 1

    return (
        samples,
        effective_populations,
        count_checks,
        states,
        flippable_counts,
    )


@dataclass(frozen=True)
class ProjectorResult:
    length: int
    flux: int
    delta_v: float
    energy: float
    energy_error: float
    flippability: float
    flippability_error: float
    minimum_effective_population_fraction: float
    count_consistent: bool
    sector_consistent: bool
    final_unique_fraction: float


def blocked_mean_and_error(
    values: np.ndarray, block_count: int = 10
) -> tuple[float, float]:
    usable = (len(values) // block_count) * block_count
    blocks = values[:usable].reshape(block_count, -1).mean(axis=1)
    return float(np.mean(blocks)), float(
        np.std(blocks, ddof=1) / np.sqrt(block_count)
    )


def run_population(
    length: int,
    flux: int,
    delta_v: float,
    *,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    sample_sweeps: int,
    seed: int,
    start_family: int = 0,
) -> ProjectorResult:
    geometry = build_geometry(length)
    if start_family == 0:
        base_occupation = initial_ice(length)
    else:
        base_occupation = neutral_flux_pair_start(
            length, (start_family - 1) % 3, seed
        )
    occupation = insert_flux_lines(
        base_occupation, 0, flux, line_offset=seed
    )
    expected_flux = (flux, 0, 0)
    if not np.all(vertex_degrees(occupation) == 3):
        raise AssertionError("projector start leaves the ice sector")
    if electric_flux(occupation) != expected_flux:
        raise AssertionError("projector start has the wrong electric flux")
    (
        samples,
        effective_populations,
        count_checks,
        final_states,
        final_counts,
    ) = run_population_core(
        occupation.ravel(),
        geometry.plaquette_links,
        geometry.affected_plaquettes,
        geometry.affected_counts,
        delta_v,
        population,
        classical_sweeps,
        burn_sweeps,
        sample_sweeps,
        max(16, geometry.plaquette_count // 8),
        seed,
    )
    mean, error = blocked_mean_and_error(samples)
    sector_consistent = True
    for state in final_states:
        final_occupation = state.reshape((length, length, length, 3))
        sector_consistent = sector_consistent and bool(
            np.all(vertex_degrees(final_occupation) == 3)
            and electric_flux(final_occupation) == expected_flux
        )
    packed = np.packbits(final_states, axis=1)
    final_unique_fraction = np.unique(packed, axis=0).shape[0] / population
    return ProjectorResult(
        length=length,
        flux=flux,
        delta_v=delta_v,
        energy=delta_v * mean,
        energy_error=abs(delta_v) * error,
        flippability=mean,
        flippability_error=error,
        minimum_effective_population_fraction=float(
            np.min(effective_populations) / population
        ),
        count_consistent=bool(
            np.all(count_checks == 0)
            and all(
                count_flippable(state, geometry.plaquette_links) == count
                for state, count in zip(final_states, final_counts, strict=True)
            )
        ),
        sector_consistent=sector_consistent,
        final_unique_fraction=float(final_unique_fraction),
    )


def exact_small_energy(delta_v: float, flux: int) -> tuple[float, float]:
    start = insert_flux_lines(initial_ice(2), 0, flux)
    orbit = build_small_rk_orbit(start)
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
    vector = vectors[:, 0]
    if np.sum(vector) < 0:
        vector = -vector
    mixed = delta_v * float(np.dot(vector, flippabilities) / np.sum(vector))
    return float(values[0]), mixed


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


@dataclass(frozen=True)
class FluxCurveFit:
    length: int
    delta_v: float
    electric_stiffness: float
    electric_stiffness_error: float
    quadratic_rss: float
    linear_rss: float


def fit_flux_curve(results: list[ProjectorResult]) -> FluxCurveFit:
    ordered = sorted(results, key=lambda result: result.flux)
    if ordered[0].flux != 0:
        raise ValueError("a flux curve needs a zero-flux reference")
    reference = ordered[0]
    nonzero = ordered[1:]
    predictor = np.asarray(
        [result.flux**2 / result.length for result in nonzero], dtype=float
    )
    differences = np.asarray(
        [result.energy - reference.energy for result in nonzero], dtype=float
    )
    errors = np.asarray(
        [
            np.hypot(result.energy_error, reference.energy_error)
            for result in nonzero
        ],
        dtype=float,
    )
    weights = 1.0 / np.maximum(errors, 1.0e-12) ** 2
    slope = float(np.sum(weights * predictor * differences) / np.sum(weights * predictor**2))
    slope_error = float(np.sqrt(1.0 / np.sum(weights * predictor**2)))
    quadratic_rss = float(np.sum((differences - slope * predictor) ** 2))
    linear_predictor = np.asarray(
        [float(result.flux) for result in nonzero], dtype=float
    )
    linear_slope = float(
        np.dot(linear_predictor, differences)
        / np.dot(linear_predictor, linear_predictor)
    )
    linear_rss = float(
        np.sum((differences - linear_slope * linear_predictor) ** 2)
    )
    return FluxCurveFit(
        length=reference.length,
        delta_v=reference.delta_v,
        electric_stiffness=2.0 * slope,
        electric_stiffness_error=2.0 * slope_error,
        quadratic_rss=quadratic_rss,
        linear_rss=linear_rss,
    )


def endpoint_stiffness(
    zero: ProjectorResult, endpoint: ProjectorResult
) -> tuple[float, float]:
    predictor = endpoint.flux**2 / endpoint.length
    stiffness = 2.0 * (endpoint.energy - zero.energy) / predictor
    error = 2.0 * np.hypot(
        endpoint.energy_error, zero.energy_error
    ) / predictor
    return float(stiffness), float(error)


def model_rss(
    curves: dict[int, list[ProjectorResult]],
    predictor_kind: str,
) -> tuple[float, float]:
    predictors: list[float] = []
    differences: list[float] = []
    for length, results in curves.items():
        ordered = sorted(results, key=lambda result: result.flux)
        reference = ordered[0].energy
        for result in ordered[1:]:
            flux = float(result.flux)
            if predictor_kind == "quadratic_over_length":
                predictor = flux**2 / length
            elif predictor_kind == "linear":
                predictor = flux
            elif predictor_kind == "linear_over_length":
                predictor = flux / length
            elif predictor_kind == "quadratic":
                predictor = flux**2
            elif predictor_kind == "step":
                predictor = 1.0
            else:
                raise ValueError(predictor_kind)
            predictors.append(predictor)
            differences.append(result.energy - reference)
    x_values = np.asarray(predictors, dtype=float)
    y_values = np.asarray(differences, dtype=float)
    slope = float(np.dot(x_values, y_values) / np.dot(x_values, x_values))
    residual = y_values - slope * x_values
    return slope, float(np.dot(residual, residual))


def main() -> int:
    checks = Checks()
    detunings = (-0.05, -0.10)

    geometry_ok = True
    for length in (2, 4, 6, 8, 10):
        geometry = build_geometry(length)
        geometry_ok = geometry_ok and bool(
            geometry.plaquette_links.shape == (3 * length**3, 4)
            and np.all(geometry.affected_counts > 0)
            and np.all(geometry.affected_counts <= geometry.affected_plaquettes.shape[1])
            and all(len(set(int(link) for link in links)) == 4 for links in geometry.plaquette_links)
        )
    checks.check(
        geometry_ok,
        "the L=2,4,6,8,10 projector geometries contain exactly 3L^3 four-link square moves",
    )
    neutral_starts_ok = all(
        np.all(vertex_degrees(neutral_flux_pair_start(8, axis, axis)) == 3)
        and electric_flux(neutral_flux_pair_start(8, axis, axis)) == (0, 0, 0)
        for axis in range(3)
    )
    checks.check(
        neutral_starts_ok,
        "opposite noncontractible line pairs provide three nonlocal zero-flux initialization controls",
    )

    exact_controls: list[tuple[float, int, float, float, ProjectorResult]] = []
    for detuning_index, delta_v in enumerate(detunings):
        for flux in (0, 1):
            exact, exact_mixed = exact_small_energy(delta_v, flux)
            projector = run_population(
                2,
                flux,
                delta_v,
                population=2048,
                classical_sweeps=100,
                burn_sweeps=200,
                sample_sweeps=500,
                seed=1_200_000 + 10_000 * detuning_index + flux,
            )
            exact_controls.append(
                (delta_v, flux, exact, exact_mixed, projector)
            )
    checks.check(
        all(abs(exact - mixed) < 1.0e-9 for _, _, exact, mixed, _ in exact_controls),
        "the exact L=2 eigenvectors satisfy the constant-trial mixed-estimator identity in both flux sectors",
    )
    checks.check(
        all(
            abs(projector.energy - exact)
            < max(8.0 * projector.energy_error, 0.004)
            for _, _, exact, _, projector in exact_controls
        ),
        "the stochastic projector reproduces four exact L=2 ground energies at V=0.95 and V=0.90",
    )

    primary: dict[tuple[float, int], list[ProjectorResult]] = {}
    all_projectors = [control[-1] for control in exact_controls]
    for detuning_index, delta_v in enumerate(detunings):
        for length in (4, 6, 8):
            curve: list[ProjectorResult] = []
            for flux in range(length // 2 + 1):
                result = run_population(
                    length,
                    flux,
                    delta_v,
                    population=256,
                    classical_sweeps=100,
                    burn_sweeps=150,
                    sample_sweeps=300,
                    seed=(
                        2_000_000
                        + 100_000 * detuning_index
                        + 100 * length
                        + flux
                    ),
                )
                curve.append(result)
                all_projectors.append(result)
            primary[(delta_v, length)] = curve

    endpoint_ten: dict[float, tuple[ProjectorResult, ProjectorResult]] = {}
    for detuning_index, delta_v in enumerate(detunings):
        pair = tuple(
            run_population(
                10,
                flux,
                delta_v,
                population=256,
                classical_sweeps=100,
                burn_sweeps=150,
                sample_sweeps=300,
                seed=2_500_000 + 100_000 * detuning_index + flux,
            )
            for flux in (0, 5)
        )
        endpoint_ten[delta_v] = pair
        all_projectors.extend(pair)

    checks.check(
        all(
            result.count_consistent and result.sector_consistent
            for result in all_projectors
        ),
        "every projector population preserves exact local flippability, three-of-six Gauss charge, and assigned flux",
    )
    checks.check(
        min(
            result.minimum_effective_population_fraction
            for result in all_projectors
        )
        > 0.90
        and min(result.final_unique_fraction for result in all_projectors if result.length >= 4)
        > 0.25,
        "all populations retain effective weight and final-state diversity above the declared collapse controls",
    )

    curve_fits = [
        fit_flux_curve(primary[(delta_v, length)])
        for delta_v in detunings
        for length in (4, 6, 8)
    ]
    checks.check(
        all(
            fit.electric_stiffness > 6.0 * fit.electric_stiffness_error
            for fit in curve_fits
        ),
        "every L=4,6,8 finite-detuning flux ladder has resolved positive electric stiffness",
    )
    checks.check(
        all(
            fit.quadratic_rss < 0.25 * fit.linear_rss
            for fit in curve_fits
        ),
        "Phi^2/L beats a linear-in-|Phi| curve separately on every full flux ladder",
    )

    endpoint_ten_fits = {
        delta_v: endpoint_stiffness(*endpoint_ten[delta_v])
        for delta_v in detunings
    }
    checks.check(
        all(value > 6.0 * error for value, error in endpoint_ten_fits.values()),
        "the shrinking-density L=10 endpoints independently retain positive stiffness",
    )

    controls: dict[float, tuple[ProjectorResult, ProjectorResult]] = {}
    for detuning_index, delta_v in enumerate(detunings):
        pair = tuple(
            run_population(
                8,
                flux,
                delta_v,
                population=512,
                classical_sweeps=150,
                burn_sweeps=250,
                sample_sweeps=500,
                seed=3_000_000 + 100_000 * detuning_index + flux,
                start_family=detuning_index + 1,
            )
            for flux in (0, 4)
        )
        controls[delta_v] = pair
    control_fits = {
        delta_v: endpoint_stiffness(*controls[delta_v])
        for delta_v in detunings
    }
    primary_eight = {
        delta_v: endpoint_stiffness(
            primary[(delta_v, 8)][0], primary[(delta_v, 8)][-1]
        )
        for delta_v in detunings
    }
    checks.check(
        all(
            control > 6.0 * error
            and abs(control - primary_eight[delta_v][0])
            / (0.5 * (control + primary_eight[delta_v][0]))
            < 0.15
            for delta_v, (control, error) in control_fits.items()
        ),
        "doubled L=8 populations reproduce the positive endpoint stiffness within fifteen percent",
    )

    global_results: dict[float, dict[str, tuple[float, float]]] = {}
    for delta_v in detunings:
        curves = {
            length: primary[(delta_v, length)] for length in (4, 6, 8)
        }
        curves[10] = list(endpoint_ten[delta_v])
        global_results[delta_v] = {
            kind: model_rss(curves, kind)
            for kind in (
                "quadratic_over_length",
                "linear",
                "linear_over_length",
                "quadratic",
                "step",
            )
        }
    checks.check(
        all(
            global_results[delta_v]["quadratic_over_length"][1]
            < 0.20
            * min(
                global_results[delta_v][kind][1]
                for kind in (
                    "linear",
                    "linear_over_length",
                    "quadratic",
                    "step",
                )
            )
            for delta_v in detunings
        ),
        "the joint L=4,6,8,10 data prefer Maxwell Phi^2/L scaling over four named controls",
    )

    first_order_normalized = 3.183873
    volume_stiffness: dict[float, list[float]] = {}
    for delta_v in detunings:
        values = [
            next(
                fit.electric_stiffness
                for fit in curve_fits
                if fit.delta_v == delta_v and fit.length == length
            )
            for length in (4, 6)
        ]
        values.append(control_fits[delta_v][0])
        values.append(endpoint_ten_fits[delta_v][0])
        volume_stiffness[delta_v] = values
    checks.check(
        all(
            (max(values) - min(values)) / np.mean(values) < 0.20
            and abs(np.mean(values) / abs(delta_v) - first_order_normalized)
            / first_order_normalized
            < 0.20
            for delta_v, values in volume_stiffness.items()
        ),
        "the volume ladder is stable and remains near the independent first-order U/|delta V| coefficient",
    )

    for delta_v, flux, exact, _, projector in exact_controls:
        print(
            "EXACT",
            f"V={1.0 + delta_v:.2f}",
            f"Phi={flux}",
            f"E0={exact:.9f}",
            f"projector={projector.energy:.9f}+/-{projector.energy_error:.9f}",
        )
    for fit in curve_fits:
        print(
            "CURVE",
            f"V={1.0 + fit.delta_v:.2f}",
            f"L={fit.length}",
            f"U={fit.electric_stiffness:.6f}+/-{fit.electric_stiffness_error:.6f}",
            f"rss_quad={fit.quadratic_rss:.8f}",
            f"rss_linear={fit.linear_rss:.8f}",
        )
    for delta_v in detunings:
        print(
            "POPULATION_CONTROL",
            f"V={1.0 + delta_v:.2f}",
            f"U_256={primary_eight[delta_v][0]:.6f}",
            f"U_512={control_fits[delta_v][0]:.6f}+/-{control_fits[delta_v][1]:.6f}",
        )
    for delta_v in detunings:
        print(
            "DATA",
            f"V={1.0 + delta_v:.2f}",
            "U_L="
            + ",".join(
                f"{length}:{value:.6f}"
                for length, value in zip(
                    (4, 6, 8, 10), volume_stiffness[delta_v], strict=True
                )
            ),
            f"U/|deltaV|={np.mean(volume_stiffness[delta_v]) / abs(delta_v):.6f}",
            f"global_rss={global_results[delta_v]['quadratic_over_length'][1]:.8f}",
        )
        print(
            "MODEL_CONTROL",
            f"V={1.0 + delta_v:.2f}",
            "rss="
            + ",".join(
                f"{kind}:{global_results[delta_v][kind][1]:.8f}"
                for kind in (
                    "quadratic_over_length",
                    "linear",
                    "linear_over_length",
                    "quadratic",
                    "step",
                )
            ),
        )
    print(
        "CERTIFICATE: exact_stoquastic_green_function=True constant_trial_mixed_estimator=True "
        "finite_population=True finite_imaginary_time=True thermodynamic_limit=False "
        "real_time_spectrum=False"
    )
    print(
        "RESOLUTION: per_element=every accepted square flip; per_site=all final walkers preserve Gauss; "
        "per_mode=electric topological flux; per_block=exact L2 plus projector L4,6,8,10; "
        "lattice_wide=finite-volume finite-detuning stiffness, not a thermodynamic phase proof"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
