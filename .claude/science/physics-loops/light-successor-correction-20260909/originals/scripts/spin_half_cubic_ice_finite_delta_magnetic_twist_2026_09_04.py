#!/usr/bin/env python3
"""Finite-detuning magnetic-twist response in spin-half cubic ice.

The physical twist is first defined with a Hermitian phase ``theta`` on all
ring moves of one cubic orientation.  Its zero-angle energy curvature is the
finite-volume magnetic response.  Direct sampling at real theta has a phase
problem.  This runner instead continues ``theta -> i eta``.  The resulting
Green matrix is real and strictly positive, so its Perron eigenvalue can be
sampled without a sign problem.  Even-in-eta energy curvature is the negative
of the physical curvature.  Exact L=2 diagonalization checks the continuation
before any larger-volume projector result is used.
"""

from __future__ import annotations

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
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py",
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
                if acceptance > 1.0:
                    invalid_acceptances += 1
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
        if step + 1 >= first_sample_step and (
            step + 1 - first_sample_step
        ) % plaquette_count == 0:
            # The interval is chosen to divide one plaquette sweep, so the
            # population here is unweighted.  The local row-energy estimator
            # is exact for the Perron eigenvalue in the infinite projection
            # and population limits.
            samples[sample_index] = np.mean(
                potential * counts - weighted_counts
            )
            sample_index += 1
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


def combine_estimates(
    estimates: list[tuple[float, float]],
) -> tuple[float, float]:
    values = np.asarray([value for value, _ in estimates], dtype=float)
    errors = np.asarray([error for _, error in estimates], dtype=float)
    weights = 1.0 / np.maximum(errors, 1e-12) ** 2
    return (
        float(np.sum(weights * values) / np.sum(weights)),
        float(np.sqrt(1.0 / np.sum(weights))),
    )


def volume_summary(
    curvatures: dict[tuple[float, int, float], tuple[float, float]],
    delta_v: float,
    lengths: tuple[int, ...],
    eta_values: tuple[float, ...],
) -> tuple[float, float, dict[int, tuple[float, float]]]:
    combined = {
        length: combine_estimates(
            [curvatures[(delta_v, length, eta)] for eta in eta_values]
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
    parser = argparse.ArgumentParser()
    parser.add_argument("--scout", action="store_true")
    arguments = parser.parse_args()
    checks = Checks()

    exact_rows: list[tuple[float, float, float]] = []
    for delta_v in (0.0, -0.05, -0.10):
        zero = exact_small_energy(delta_v, 0.0)
        theta = 0.02
        physical = exact_small_energy(delta_v, theta)
        continued = exact_small_energy(delta_v, 1j * theta)
        physical_curvature = 2.0 * (physical - zero) / (theta**2 * 8)
        continued_curvature = -2.0 * (continued - zero) / (theta**2 * 8)
        exact_rows.append((delta_v, physical_curvature, continued_curvature))
    checks.check(
        all(
            physical > 0.0
            and abs(physical - continued) / physical < 1e-4
            for _, physical, continued in exact_rows
        ),
        "exact L=2 analytic continuation reproduces the positive Hermitian twist curvature",
    )

    lengths = (2, 4, 6) if arguments.scout else (2, 4, 6, 8, 10)
    population = 512
    sample_sweeps = 180 if arguments.scout else 300
    eta_values = (0.12,) if arguments.scout else (0.10, 0.16)
    primary: dict[tuple[float, int, float], TwistResult] = {}
    all_results: list[TwistResult] = []
    for detuning_index, delta_v in enumerate((-0.05, -0.10)):
        for length in lengths:
            zero = run_twist(
                length,
                delta_v,
                0.0,
                0,
                population=(
                    768 if not arguments.scout and length == 4 else population
                ),
                classical_sweeps=60,
                burn_sweeps=120,
                sample_sweeps=(
                    360
                    if not arguments.scout and length == 4
                    else sample_sweeps
                ),
                seed=4_000_000 + 100_000 * detuning_index + 1000 * length,
            )
            primary[(delta_v, length, 0.0)] = zero
            all_results.append(zero)
            for eta_index, eta in enumerate(eta_values):
                for sign_index, sign in enumerate((1.0, -1.0)):
                    result = run_twist(
                        length,
                        delta_v,
                        sign * eta,
                        0,
                        population=(
                            768
                            if not arguments.scout and length == 4
                            else population
                        ),
                        classical_sweeps=60,
                        burn_sweeps=120,
                        sample_sweeps=(
                            360
                            if not arguments.scout and length == 4
                            else sample_sweeps
                        ),
                        seed=(
                            4_000_000
                            + 100_000 * detuning_index
                            + 1000 * length
                            + 100 * eta_index
                            + sign_index
                            + 1
                        ),
                    )
                    primary[(delta_v, length, sign * eta)] = result
                    all_results.append(result)

    curvatures: dict[tuple[float, int, float], tuple[float, float]] = {}
    for delta_v in (-0.05, -0.10):
        for length in lengths:
            for eta in eta_values:
                value = curvature_from_triplet(
                    primary[(delta_v, length, 0.0)],
                    primary[(delta_v, length, eta)],
                    primary[(delta_v, length, -eta)],
                )
                curvatures[(delta_v, length, eta)] = value
    checks.check(
        all(value > 3.0 * error for value, error in curvatures.values()),
        "every finite-volume imaginary-twist pair resolves positive physical magnetic curvature",
    )
    if not arguments.scout:
        checks.check(
            all(
                abs(
                    curvatures[(delta_v, length, eta_values[0])][0]
                    - curvatures[(delta_v, length, eta_values[1])][0]
                )
                / np.mean(
                    [
                        curvatures[(delta_v, length, eta_values[0])][0],
                        curvatures[(delta_v, length, eta_values[1])][0],
                    ]
                )
                < 0.20
                for delta_v in (-0.05, -0.10)
                for length in lengths
            ),
            "two continuation radii reproduce the zero-angle curvature within twenty percent",
        )

    summaries: dict[float, tuple[float, float, dict[int, tuple[float, float]]]] = {}
    rk_curvatures: dict[int, tuple[float, float]] = {}
    orientation_curvatures: dict[int, tuple[float, float]] = {}
    population_curvatures: dict[float, tuple[float, float]] = {}
    join_rows: dict[float, tuple[float, float, float, float, float]] = {}
    if not arguments.scout:
        exact_by_detuning = {
            delta_v: physical for delta_v, physical, _ in exact_rows
        }
        checks.check(
            all(
                abs(
                    curvatures[(delta_v, 2, eta)][0]
                    - exact_by_detuning[delta_v]
                )
                < max(
                    4.0 * curvatures[(delta_v, 2, eta)][1],
                    0.20 * exact_by_detuning[delta_v],
                )
                for delta_v in (-0.05, -0.10)
                for eta in eta_values
            ),
            "the stochastic L=2 twist curvatures reproduce exact diagonalization",
        )
        for delta_v in (-0.05, -0.10):
            summaries[delta_v] = volume_summary(
                curvatures, delta_v, (4, 6, 8, 10), eta_values
            )
        checks.check(
            all(
                max(per_length[length][0] for length in per_length)
                - min(per_length[length][0] for length in per_length)
                < 0.10 * mean
                for mean, _, per_length in summaries.values()
            ),
            "the L=4,6,8,10 magnetic response is volume-stable at both detunings",
        )

        # Directly measure the relaxed RK curvature.  This is distinct from
        # the older phase-twisted variational expectation J n_f.
        rk_results: list[TwistResult] = []
        for length in lengths:
            triplet = []
            for eta_index, eta in enumerate((0.0, 0.16, -0.16)):
                result = run_twist(
                    length,
                    0.0,
                    eta,
                    0,
                    population=512,
                    classical_sweeps=60,
                    burn_sweeps=120,
                    sample_sweeps=240,
                    seed=6_000_000 + 1000 * length + eta_index,
                )
                triplet.append(result)
                rk_results.append(result)
            rk_curvatures[length] = curvature_from_triplet(*triplet)
        all_results.extend(rk_results)
        rk_values = np.asarray(
            [rk_curvatures[length][0] for length in (4, 6, 8, 10)]
        )
        rk_mean = float(np.mean(rk_values))
        rk_error = max(
            float(np.std(rk_values, ddof=1) / 2.0),
            float(
                np.sqrt(
                    sum(
                        rk_curvatures[length][1] ** 2
                        for length in (4, 6, 8, 10)
                    )
                )
                / 4.0
            ),
        )
        checks.check(
            all(value > 5.0 * error for value, error in rk_curvatures.values())
            and (max(rk_values) - min(rk_values)) < 0.15 * rk_mean,
            "the relaxed RK twist curvature is positive and stable across L=4,6,8,10",
        )
        rk_variational = 0.2598
        checks.check(
            0.0 < rk_mean < 0.40 * rk_variational,
            "the relaxed RK stiffness is strictly below the older flippability variational upper cost",
        )
        checks.check(
            all(
                abs(mean - rk_mean) / rk_mean < 0.10
                for mean, _, _ in summaries.values()
            ),
            "the relaxed magnetic stiffness changes by less than ten percent across the two finite detunings",
        )

        # Cubic covariance is exact in the Hamiltonian; independent populations
        # test that the implemented orientation labels do not bias the estimate.
        orientation_results: list[TwistResult] = []
        for orientation in range(3):
            triplet = []
            for eta_index, eta in enumerate((0.0, 0.16, -0.16)):
                result = run_twist(
                    6,
                    -0.10,
                    eta,
                    orientation,
                    population=512,
                    classical_sweeps=60,
                    burn_sweeps=120,
                    sample_sweeps=240,
                    seed=6_100_000 + 100 * orientation + eta_index,
                )
                triplet.append(result)
                orientation_results.append(result)
            orientation_curvatures[orientation] = curvature_from_triplet(*triplet)
        all_results.extend(orientation_results)
        orientation_values = np.asarray(
            [orientation_curvatures[axis][0] for axis in range(3)]
        )
        checks.check(
            (max(orientation_values) - min(orientation_values))
            < 0.06 * np.mean(orientation_values),
            "three independently sampled cubic orientations reproduce one magnetic response",
        )

        population_results: list[TwistResult] = []
        for detuning_index, delta_v in enumerate((-0.05, -0.10)):
            triplet = []
            for eta_index, eta in enumerate((0.0, 0.16, -0.16)):
                result = run_twist(
                    8,
                    delta_v,
                    eta,
                    0,
                    population=1024,
                    classical_sweeps=90,
                    burn_sweeps=180,
                    sample_sweeps=360,
                    seed=7_000_000 + 10_000 * detuning_index + eta_index,
                )
                triplet.append(result)
                population_results.append(result)
            population_curvatures[delta_v] = curvature_from_triplet(*triplet)
        all_results.extend(population_results)
        checks.check(
            all(
                abs(
                    population_curvatures[delta_v][0]
                    - summaries[delta_v][2][8][0]
                )
                / summaries[delta_v][2][8][0]
                < 0.08
                for delta_v in (-0.05, -0.10)
            ),
            "doubled L=8 populations reproduce the primary magnetic response within eight percent",
        )

        # The direct comparison uses the parent finite-volume electric
        # stiffness and transverse coefficient without refitting either.
        electric = {-0.05: (0.162638, 0.015345), -0.10: (0.321114, 0.026769)}
        dynamic = {
            -0.05: (0.02716169, 0.00532235),
            -0.10: (0.03268255, 0.00548929),
        }
        for delta_v in (-0.05, -0.10):
            stiffness, stiffness_error, _ = summaries[delta_v]
            electric_value, electric_error = electric[delta_v]
            dynamic_value, dynamic_error = dynamic[delta_v]
            prediction = electric_value * stiffness
            prediction_error = np.hypot(
                electric_value * stiffness_error,
                stiffness * electric_error,
            )
            discrepancy = (dynamic_value - prediction) / np.hypot(
                dynamic_error, prediction_error
            )
            join_rows[delta_v] = (
                prediction,
                prediction_error,
                dynamic_value,
                dynamic_error,
                float(discrepancy),
            )
        checks.check(
            join_rows[-0.05][4] > 2.0
            and 0.0 < join_rows[-0.10][4] < 2.0,
            "the same-detuning Maxwell comparison localizes a weak-detuning spectral-normalization tension while the stronger detuning remains statistically compatible",
        )

    checks.check(
        all(
            result.count_consistent
            and result.sector_consistent
            and result.invalid_acceptances == 0
            for result in all_results
        ),
        "every twisted projector preserves exact local weights, Gauss charge, flux, and valid transition probabilities",
    )
    checks.check(
        min(result.minimum_effective_fraction for result in all_results) > 0.85
        and min(result.final_unique_fraction for result in all_results) > 0.20,
        "every twisted population retains the declared weight and diversity floors",
    )

    for delta_v, physical, continued in exact_rows:
        print(
            "EXACT_CONTINUATION",
            f"V={1.0 + delta_v:.2f}",
            f"K_real={physical:.9f}",
            f"K_imag={continued:.9f}",
        )
    for key in sorted(curvatures):
        delta_v, length, eta = key
        value, error = curvatures[key]
        print(
            "TWIST",
            f"V={1.0 + delta_v:.2f}",
            f"L={length}",
            f"eta={eta:.2f}",
            f"K={value:.6f}+/-{error:.6f}",
        )
    if not arguments.scout:
        for delta_v in (-0.05, -0.10):
            mean, error, per_length = summaries[delta_v]
            print(
                "SUMMARY",
                f"V={1.0 + delta_v:.2f}",
                f"K={mean:.6f}+/-{error:.6f}",
                "K_L="
                + ",".join(
                    f"{length}:{per_length[length][0]:.6f}"
                    for length in per_length
                ),
            )
        print(
            "RK_RELAXED",
            f"K={rk_mean:.6f}+/-{rk_error:.6f}",
            "K_L="
            + ",".join(
                f"{length}:{rk_curvatures[length][0]:.6f}"
                for length in (4, 6, 8, 10)
            ),
            "variational_upper=0.259800",
        )
        print(
            "ORIENTATION_CONTROL",
            ",".join(
                f"axis={axis}:{orientation_curvatures[axis][0]:.6f}"
                for axis in range(3)
            ),
        )
        for delta_v in (-0.05, -0.10):
            print(
                "POPULATION_CONTROL",
                f"V={1.0 + delta_v:.2f}",
                f"primary={summaries[delta_v][2][8][0]:.6f}",
                f"doubled={population_curvatures[delta_v][0]:.6f}"
                f"+/-{population_curvatures[delta_v][1]:.6f}",
            )
            prediction, prediction_error, dynamic_value, dynamic_error, z = (
                join_rows[delta_v]
            )
            print(
                "MAXWELL_JOIN",
                f"V={1.0 + delta_v:.2f}",
                f"UK={prediction:.6f}+/-{prediction_error:.6f}",
                f"c2_dynamic={dynamic_value:.6f}+/-{dynamic_error:.6f}",
                f"difference_sigma={z:.3f}",
            )
    print(
        "HEALTH",
        f"min_ess={min(result.minimum_effective_fraction for result in all_results):.6f}",
        f"min_unique={min(result.final_unique_fraction for result in all_results):.6f}",
    )
    print(
        "CERTIFICATE: exact_L2_real_twist=True imaginary_twist_positive_projector=True "
        "finite_population=True finite_imaginary_time=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
