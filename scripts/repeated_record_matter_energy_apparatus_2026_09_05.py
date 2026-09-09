#!/usr/bin/env python3
"""Finite-matrix primary checks for repeated Records, matter, and apparatus energy.

The 216-mode Gaussian trajectories use the ideal occupation/deletion instrument.
Energy-conserving battery lifts are exercised only by separate four-mode fixtures.
The runner does not derive a Record compiler, clock, battery preparation, renewal
law, stationary matter state, continuum limit, or physical scale.
"""

from __future__ import annotations

import os

# Fix numerical-library parallelism before importing NumPy.
for _thread_var in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_var] = "1"

import resource
import sys
import time
from dataclasses import dataclass
from itertools import combinations

import numpy as np


AUDIT_TIMEOUT_SEC = 180
L = 6
N_SITES = L**3
N_PARTICLES = N_SITES // 2
N_TRAJECTORIES = 16
N_EVENTS = 27
DWELLS = (0.0, 0.5)
SITE_SEED_BASE = 2026090400
OUTCOME_SEED_BASE = 2026091400
TOL_MATRIX = 2.0e-9
TOL_ENERGY = 3.0e-9
TOL_NUMBER = 2.0e-9
PROB_FLOOR = 1.0e-10
PROB_TOL = 2.0e-10
RSS_LIMIT_MIB = 180.0
RUNTIME_LIMIT_SEC = 180.0
STDOUT_LIMIT = 6000


def site_index(x: int, y: int, z: int) -> int:
    return (x * L + y) * L + z


def eta(coord: tuple[int, int, int], axis: int) -> float:
    x, y, _ = coord
    if axis == 0:
        return 1.0
    if axis == 1:
        return -1.0 if x % 2 else 1.0
    return -1.0 if (x + y) % 2 else 1.0


def forward_edge_sign(coord: tuple[int, int, int], axis: int) -> float:
    # N=L/2=3, so the prescribed wrap sign (-1)^(N-1) is +1.
    wrap_sign = 1.0
    return eta(coord, axis) * (wrap_sign if coord[axis] == L - 1 else 1.0)


def build_pi_flux_hamiltonian() -> np.ndarray:
    hamiltonian = np.zeros((N_SITES, N_SITES), dtype=float)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                coord = (x, y, z)
                source = site_index(*coord)
                for axis in range(3):
                    target_coord = list(coord)
                    target_coord[axis] = (target_coord[axis] + 1) % L
                    target = site_index(*target_coord)
                    sign = forward_edge_sign(coord, axis)
                    hamiltonian[source, target] += sign
                    hamiltonian[target, source] += sign
    return hamiltonian


def plaquette_residual() -> float:
    residual = 0.0
    for x in range(L):
        for y in range(L):
            for z in range(L):
                coord = (x, y, z)
                for first in range(3):
                    for second in range(first + 1, 3):
                        along_first = list(coord)
                        along_first[first] = (along_first[first] + 1) % L
                        along_second = list(coord)
                        along_second[second] = (along_second[second] + 1) % L
                        product = (
                            forward_edge_sign(coord, first)
                            * forward_edge_sign(tuple(along_first), second)
                            * forward_edge_sign(tuple(along_second), first)
                            * forward_edge_sign(coord, second)
                        )
                        residual = max(residual, abs(product + 1.0))
    return residual


def energy(hamiltonian: np.ndarray, covariance: np.ndarray) -> float:
    return float(np.real(np.sum(hamiltonian * covariance.T)))


def gaussian_energy_second_moment(
    hamiltonian: np.ndarray, covariance: np.ndarray
) -> float:
    """Return <dGamma(h)^2> from a number-conserving Gaussian covariance."""
    identity = np.eye(len(covariance), dtype=np.complex128)
    mean = energy(hamiltonian, covariance)
    variance = np.trace(
        covariance @ hamiltonian @ (identity - covariance) @ hamiltonian
    )
    return mean**2 + float(np.real(variance))


def projector_residual(covariance: np.ndarray) -> float:
    hermitian = float(np.max(np.abs(covariance - covariance.conj().T)))
    idempotent = float(np.max(np.abs(covariance @ covariance - covariance)))
    return max(hermitian, idempotent)


def occupation_candidates(
    covariance: np.ndarray, site: int
) -> tuple[float, np.ndarray, np.ndarray]:
    probability_one = float(np.real(covariance[site, site]))
    if not PROB_FLOOR < probability_one < 1.0 - PROB_FLOOR:
        raise ValueError(f"non-null two-outcome probability required, got {probability_one:.16g}")
    keep = np.arange(len(covariance)) != site
    column = covariance[keep, site]
    block = covariance[np.ix_(keep, keep)]

    outcome_zero = np.zeros_like(covariance)
    outcome_zero[np.ix_(keep, keep)] = block + np.outer(column, column.conj()) / (
        1.0 - probability_one
    )

    outcome_one = np.zeros_like(covariance)
    outcome_one[np.ix_(keep, keep)] = block - np.outer(column, column.conj()) / probability_one
    outcome_one[site, site] = 1.0

    outcome_zero = (outcome_zero + outcome_zero.conj().T) / 2.0
    outcome_one = (outcome_one + outcome_one.conj().T) / 2.0
    return probability_one, outcome_zero, outcome_one


def occupation_branches(
    covariance: np.ndarray, site: int
) -> tuple[float, list[tuple[int, float, np.ndarray]]]:
    """Discard Born branches whose weights are numerically zero at PROB_TOL."""
    if covariance.ndim != 2 or covariance.shape[0] != covariance.shape[1]:
        raise ValueError("covariance must be square")
    if not 0 <= site < len(covariance):
        raise ValueError("site is outside covariance")
    raw = covariance[site, site]
    probability_one = float(np.real(raw))
    if not np.isfinite(probability_one) or abs(float(np.imag(raw))) > TOL_MATRIX:
        raise ValueError("occupation probability is not finite and real")
    if probability_one < -PROB_TOL or probability_one > 1.0 + PROB_TOL:
        raise ValueError("occupation probability is outside [0,1]")
    probability_one = min(1.0, max(0.0, probability_one))
    deterministic = dephased_covariance(covariance, site)
    if probability_one <= PROB_TOL:
        deterministic[site, site] = 0.0
        return probability_one, [(0, 1.0, deterministic)]
    if probability_one >= 1.0 - PROB_TOL:
        deterministic[site, site] = 1.0
        return probability_one, [(1, 1.0, deterministic)]
    probability_one, outcome_zero, outcome_one = occupation_candidates(covariance, site)
    return probability_one, [
        (0, 1.0 - probability_one, outcome_zero),
        (1, probability_one, outcome_one),
    ]


def dephased_covariance(covariance: np.ndarray, site: int) -> np.ndarray:
    result = covariance.copy()
    probability_one = result[site, site]
    result[site, :] = 0.0
    result[:, site] = 0.0
    result[site, site] = probability_one
    return result


def delete_site(hamiltonian: np.ndarray, site: int) -> np.ndarray:
    result = hamiltonian.copy()
    result[site, :] = 0.0
    result[:, site] = 0.0
    return result


def live_spectrum(
    hamiltonian: np.ndarray, live_sites: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    live_hamiltonian = hamiltonian[np.ix_(live_sites, live_sites)]
    return np.linalg.eigh(live_hamiltonian)


def evolve_live_covariance(
    covariance: np.ndarray,
    hamiltonian: np.ndarray,
    live_sites: np.ndarray,
    eigenvalues: np.ndarray,
    eigenvectors: np.ndarray,
    dwell: float,
) -> tuple[np.ndarray, float]:
    if dwell == 0.0:
        return covariance, 0.0
    before = energy(hamiltonian, covariance)
    live_covariance = covariance[np.ix_(live_sites, live_sites)]
    in_energy_basis = eigenvectors.conj().T @ live_covariance @ eigenvectors
    phases = np.exp(-1j * dwell * eigenvalues)
    in_energy_basis = phases[:, None] * in_energy_basis * phases.conj()[None, :]
    evolved_live = eigenvectors @ in_energy_basis @ eigenvectors.conj().T
    result = covariance.copy()
    result[np.ix_(live_sites, live_sites)] = evolved_live
    result = (result + result.conj().T) / 2.0
    after = energy(hamiltonian, result)
    return result, abs(after - before)


def fixed_number_ground_energy(eigenvalues: np.ndarray, live_particles: int) -> float:
    if not 0 <= live_particles <= len(eigenvalues):
        raise ValueError("live fixed-particle number is outside the live carrier")
    return float(np.sum(eigenvalues[:live_particles]))


def rss_mib() -> float:
    raw = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return raw / (1024.0**2) if sys.platform == "darwin" else raw / 1024.0


def schedules() -> tuple[list[list[int]], list[np.ndarray]]:
    all_sites: list[list[int]] = []
    all_uniforms: list[np.ndarray] = []
    for trajectory in range(N_TRAJECTORIES):
        site_rng = np.random.default_rng(SITE_SEED_BASE + trajectory)
        outcome_rng = np.random.default_rng(OUTCOME_SEED_BASE + trajectory)
        remaining = list(range(N_SITES))
        chosen: list[int] = []
        for unit_uniform in site_rng.random(N_EVENTS):
            position = min(int(unit_uniform * len(remaining)), len(remaining) - 1)
            chosen.append(remaining.pop(position))
        all_sites.append(chosen)
        all_uniforms.append(outcome_rng.random(N_EVENTS))
    return all_sites, all_uniforms


@dataclass
class Diagnostics:
    max_projector: float = 0.0
    max_number: float = 0.0
    max_old_record: float = 0.0
    max_old_record_coherence: float = 0.0
    max_deleted_row: float = 0.0
    max_unitary_energy: float = 0.0
    max_mixture_covariance: float = 0.0
    max_weighted_post: float = 0.0
    max_weighted_selection: float = 0.0
    max_ledger: float = 0.0
    min_excess: float = float("inf")
    min_probability: float = 1.0
    max_probability: float = 0.0


@dataclass
class Scenario:
    dwell: float
    rows: list[list[dict[str, float]]]
    diagnostics: Diagnostics
    enumeration: dict[str, float] | None


def enumerate_live_vertex_expectation(
    covariance: np.ndarray, hamiltonian: np.ndarray, live_sites: np.ndarray
) -> dict[str, float]:
    """Enumerate site choice and both Born outcomes at one current state."""
    current_energy = energy(hamiltonian, covariance)
    current_live_number = float(
        np.trace(covariance[np.ix_(live_sites, live_sites)]).real
    )
    expected_posts: list[float] = []
    expected_live_numbers: list[float] = []
    max_local_identity = 0.0
    max_branch_selection = 0.0
    for site in live_sites:
        _probability_one, branches = occupation_branches(covariance, int(site))
        post_hamiltonian = delete_site(hamiltonian, int(site))
        post_live_sites = live_sites[live_sites != site]
        direct_post = energy(post_hamiltonian, covariance)
        post_energies = [energy(post_hamiltonian, branch[2]) for branch in branches]
        expected_post = sum(
            branch[1] * post for branch, post in zip(branches, post_energies)
        )
        max_local_identity = max(max_local_identity, abs(expected_post - direct_post))
        max_branch_selection = max(
            max_branch_selection,
            *(abs(post - direct_post) for post in post_energies),
        )
        expected_posts.append(expected_post)
        expected_live_numbers.append(
            sum(
                probability
                * float(
                    np.trace(candidate[np.ix_(post_live_sites, post_live_sites)]).real
                )
                for _outcome, probability, candidate in branches
            )
        )
    live_count = len(live_sites)
    enumerated_mean = float(np.mean(expected_posts))
    exact_target = (1.0 - 2.0 / live_count) * current_energy
    enumerated_number = float(np.mean(expected_live_numbers))
    number_target = (1.0 - 1.0 / live_count) * current_live_number
    return {
        "live": float(live_count),
        "energy": current_energy,
        "mean": enumerated_mean,
        "target": exact_target,
        "residual": abs(enumerated_mean - exact_target),
        "local_residual": max_local_identity,
        "branch_selection_max": max_branch_selection,
        "live_number": current_live_number,
        "number_mean": enumerated_number,
        "number_target": number_target,
        "number_residual": abs(enumerated_number - number_target),
    }


def run_scenario(
    dwell: float,
    initial_hamiltonian: np.ndarray,
    initial_covariance: np.ndarray,
    site_schedules: list[list[int]],
    outcome_uniforms: list[np.ndarray],
) -> Scenario:
    all_rows: list[list[dict[str, float]]] = []
    diag = Diagnostics()
    enumeration: dict[str, float] | None = None

    for trajectory in range(N_TRAJECTORIES):
        hamiltonian = initial_hamiltonian.copy()
        covariance = initial_covariance.copy()
        live_mask = np.ones(N_SITES, dtype=bool)
        measured_sites: list[int] = []
        measured_outcomes: list[int] = []
        eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
        cumulative_system_energy_change = 0.0
        trajectory_rows: list[dict[str, float]] = []

        for step, site in enumerate(site_schedules[trajectory], start=1):
            live_sites = np.flatnonzero(live_mask)
            covariance, unitary_residual = evolve_live_covariance(
                covariance,
                hamiltonian,
                live_sites,
                eigenvalues,
                eigenvectors,
                dwell if step > 1 else 0.0,
            )
            diag.max_unitary_energy = max(diag.max_unitary_energy, unitary_residual)
            pre_energy = energy(hamiltonian, covariance)

            if dwell == 0.5 and trajectory == 0 and step == 8:
                enumeration = enumerate_live_vertex_expectation(
                    covariance, hamiltonian, live_sites
                )

            probability_one, branches = occupation_branches(covariance, site)
            diag.min_probability = min(diag.min_probability, probability_one)
            diag.max_probability = max(diag.max_probability, probability_one)
            for _branch_outcome, _branch_probability, candidate in branches:
                diag.max_projector = max(diag.max_projector, projector_residual(candidate))
                diag.max_number = max(
                    diag.max_number,
                    abs(float(np.trace(candidate).real) - N_PARTICLES),
                )

            mixture = sum(
                (branch_probability * candidate for _, branch_probability, candidate in branches),
                np.zeros_like(covariance),
            )
            diag.max_mixture_covariance = max(
                diag.max_mixture_covariance,
                float(np.max(np.abs(mixture - dephased_covariance(covariance, site)))),
            )

            post_hamiltonian = delete_site(hamiltonian, site)
            reference_post = energy(post_hamiltonian, covariance)
            deleted_star = pre_energy - reference_post
            branch_values = {
                outcome: (
                    probability,
                    candidate,
                    energy(post_hamiltonian, candidate),
                )
                for outcome, probability, candidate in branches
            }
            weighted_post = sum(
                probability * post
                for probability, _candidate, post in branch_values.values()
            )
            weighted_selection = weighted_post - reference_post
            diag.max_weighted_post = max(
                diag.max_weighted_post, abs(weighted_post - reference_post)
            )
            diag.max_weighted_selection = max(
                diag.max_weighted_selection, abs(weighted_selection)
            )

            sampled_outcome = int(
                outcome_uniforms[trajectory][step - 1] < probability_one
            )
            outcome = sampled_outcome if sampled_outcome in branch_values else branches[0][0]
            _chosen_probability, covariance, post_energy = branch_values[outcome]
            selection = post_energy - reference_post
            system_energy_change = post_energy - pre_energy
            cumulative_system_energy_change += system_energy_change
            diag.max_ledger = max(
                diag.max_ledger,
                abs(system_energy_change - (selection - deleted_star)),
            )

            hamiltonian = post_hamiltonian
            live_mask[site] = False
            measured_sites.append(site)
            measured_outcomes.append(outcome)
            live_sites = np.flatnonzero(live_mask)
            eigenvalues, eigenvectors = live_spectrum(hamiltonian, live_sites)
            live_particles = N_PARTICLES - sum(measured_outcomes)
            ground_energy = fixed_number_ground_energy(eigenvalues, live_particles)
            excess = post_energy - ground_energy
            diag.min_excess = min(diag.min_excess, excess)

            measured = np.array(measured_sites, dtype=int)
            expected = np.array(measured_outcomes, dtype=float)
            diag.max_old_record = max(
                diag.max_old_record,
                float(np.max(np.abs(np.real(np.diag(covariance)[measured]) - expected))),
            )
            off_record = covariance[measured, :].copy()
            off_record[np.arange(len(measured)), measured] = 0.0
            diag.max_old_record_coherence = max(
                diag.max_old_record_coherence, float(np.max(np.abs(off_record)))
            )
            diag.max_deleted_row = max(
                diag.max_deleted_row,
                float(
                    max(
                        np.max(np.abs(hamiltonian[measured, :])),
                        np.max(np.abs(hamiltonian[:, measured])),
                    )
                ),
            )
            diag.max_projector = max(diag.max_projector, projector_residual(covariance))
            diag.max_number = max(
                diag.max_number, abs(float(np.trace(covariance).real) - N_PARTICLES)
            )
            surviving_bonds = int(np.count_nonzero(np.triu(np.abs(hamiltonian) > 0.0, 1)))
            trajectory_rows.append(
                {
                    "pre": pre_energy,
                    "post": post_energy,
                    "deleted": deleted_star,
                    "selection": selection,
                    "system_energy_change": system_energy_change,
                    "cumulative_system_energy_change": cumulative_system_energy_change,
                    "ground": ground_energy,
                    "excess_per_live": excess / len(live_sites),
                    "bonds": float(surviving_bonds),
                    "probability": probability_one,
                    "outcome": float(outcome),
                    "live_particles": float(live_particles),
                }
            )

        all_rows.append(trajectory_rows)

    return Scenario(
        dwell=dwell,
        rows=all_rows,
        diagnostics=diag,
        enumeration=enumeration,
    )


def mean_at(scenario: Scenario, step: int, key: str) -> float:
    return float(np.mean([trajectory[step - 1][key] for trajectory in scenario.rows]))


def mean_and_se_at(scenario: Scenario, step: int, key: str) -> tuple[float, float]:
    values = np.array(
        [trajectory[step - 1][key] for trajectory in scenario.rows], dtype=float
    )
    return float(np.mean(values)), float(np.std(values, ddof=1) / np.sqrt(len(values)))


def final_mean_and_se(scenario: Scenario, key: str) -> tuple[float, float]:
    values = np.array([trajectory[-1][key] for trajectory in scenario.rows], dtype=float)
    return float(np.mean(values)), float(np.std(values, ddof=1) / np.sqrt(len(values)))


def max_abs(matrix: np.ndarray) -> float:
    return float(np.max(np.abs(matrix))) if matrix.size else 0.0


def complex_gaussian_fixture() -> dict[str, float]:
    """Exercise deterministic and nontrivial branches under a complex current h_R."""
    size, particles = 8, 4
    rng = np.random.default_rng(2026090517)
    raw = rng.normal(size=(6, 6)) + 1j * rng.normal(size=(6, 6))
    orbitals, _ = np.linalg.qr(raw)
    occupied = np.zeros((size, particles), dtype=np.complex128)
    occupied[0, 0] = 1.0
    occupied[2:, 1:] = orbitals[:, :3]
    covariance = occupied @ occupied.conj().T

    raw_h = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    hamiltonian = (raw_h + raw_h.conj().T) / 2.0
    np.fill_diagonal(hamiltonian, 0.0)
    hamiltonian[0, :] = 0.0
    hamiltonian[:, 0] = 0.0
    hamiltonian[1, :] = 0.0
    hamiltonian[:, 1] = 0.0
    hamiltonian *= 0.7 / np.max(np.abs(hamiltonian))

    recorded: dict[int, int] = {}
    deterministic_seen: set[int] = set()
    max_projector = projector_residual(covariance)
    max_number = abs(float(np.trace(covariance).real) - particles)
    max_born = 0.0
    max_energy_identity = 0.0
    max_record = 0.0
    max_dwell_energy = 0.0
    enumeration: dict[str, float] | None = None

    for step, site in enumerate((0, 1, 2, 3, 4)):
        if step >= 2:
            before = energy(hamiltonian, covariance)
            values, vectors = np.linalg.eigh(hamiltonian)
            phases = np.exp(-1j * (0.17 + 0.09 * step) * values)
            unitary = (vectors * phases[None, :]) @ vectors.conj().T
            covariance = unitary @ covariance @ unitary.conj().T
            covariance = (covariance + covariance.conj().T) / 2.0
            max_dwell_energy = max(
                max_dwell_energy, abs(energy(hamiltonian, covariance) - before)
            )

        live_sites = np.array([i for i in range(size) if i not in recorded], dtype=int)
        if step == 3:
            enumeration = enumerate_live_vertex_expectation(
                covariance, hamiltonian, live_sites
            )

        probability_one, branches = occupation_branches(covariance, site)
        if len(branches) == 1:
            deterministic_seen.add(branches[0][0])
        max_born = max(max_born, abs(sum(branch[1] for branch in branches) - 1.0))
        mixture = sum((branch[1] * branch[2] for branch in branches), np.zeros_like(covariance))
        max_born = max(
            max_born, max_abs(mixture - dephased_covariance(covariance, site))
        )
        post_hamiltonian = delete_site(hamiltonian, site)
        direct_post = energy(post_hamiltonian, covariance)
        weighted_post = 0.0
        for outcome, probability, candidate in branches:
            weighted_post += probability * energy(post_hamiltonian, candidate)
            max_projector = max(max_projector, projector_residual(candidate))
            max_number = max(
                max_number, abs(float(np.trace(candidate).real) - particles)
            )
            for old_site, old_outcome in recorded.items():
                row = candidate[old_site, :].copy()
                row[old_site] = 0.0
                max_record = max(
                    max_record,
                    abs(float(candidate[old_site, old_site].real) - old_outcome),
                    max_abs(row),
                )
        max_energy_identity = max(max_energy_identity, abs(weighted_post - direct_post))
        chosen = branches[0] if len(branches) == 1 else branches[step % 2]
        outcome, _probability, covariance = chosen
        recorded[site] = outcome
        hamiltonian = post_hamiltonian

    if enumeration is None:
        raise RuntimeError("complex fixture missed its live-site enumeration")
    return {
        "deterministic_count": float(len(deterministic_seen)),
        "deterministic_mask": float(sum(1 << n for n in deterministic_seen)),
        "projector": max_projector,
        "number": max_number,
        "born": max_born,
        "energy": max_energy_identity,
        "record": max_record,
        "dwell": max_dwell_energy,
        "mean_energy": max(enumeration["residual"], enumeration["local_residual"]),
        "mean_number": enumeration["number_residual"],
        "branch_selection": enumeration["branch_selection_max"],
        "live": enumeration["live"],
    }


def phase_rotated_uniform_probe() -> dict[str, float]:
    """Enumerate unconditional events after common complex-H dwell at three phases."""
    size, particles = 7, 3
    rng = np.random.default_rng(2026090529)
    raw = rng.normal(size=(size, particles)) + 1j * rng.normal(
        size=(size, particles)
    )
    orbitals, _ = np.linalg.qr(raw)
    covariance = orbitals @ orbitals.conj().T
    raw_h = rng.normal(size=(size, size)) + 1j * rng.normal(size=(size, size))
    hamiltonian = (raw_h + raw_h.conj().T) / 2.0
    np.fill_diagonal(hamiltonian, 0.0)
    hamiltonian *= 0.8 / np.max(np.abs(hamiltonian))

    records: dict[int, int] = {}
    for site in (1, 5):
        _probability_one, branches = occupation_branches(covariance, site)
        outcome, _probability, covariance = max(branches, key=lambda branch: branch[1])
        records[site] = outcome
        hamiltonian = delete_site(hamiltonian, site)

    live_sites = np.array([site for site in range(size) if site not in records], dtype=int)
    live_count = len(live_sites)
    uniform_weights = np.ones(live_count, dtype=float)
    uniform_weights /= np.sum(uniform_weights)
    values, vectors = np.linalg.eigh(hamiltonian)
    initial_energy = energy(hamiltonian, covariance)
    initial_live_number = float(
        np.trace(covariance[np.ix_(live_sites, live_sites)]).real
    )
    max_energy_residual = 0.0
    max_number_residual = 0.0
    max_branch_identity = 0.0
    max_record_residual = 0.0
    max_second_residual = 0.0
    max_second_conservation = 0.0
    max_star_bound_residual = 0.0
    max_variance_budget_residual = 0.0
    max_star_square_bound = 0.0
    initial_second = gaussian_energy_second_moment(hamiltonian, covariance)
    initial_variance = initial_second - initial_energy**2
    for tau in (0.0, 0.23, 0.71):
        phases = np.exp(-1j * tau * values)
        unitary = (vectors * phases[None, :]) @ vectors.conj().T
        rotated = unitary @ covariance @ unitary.conj().T
        expected_energies: list[float] = []
        expected_numbers: list[float] = []
        expected_seconds: list[float] = []
        star_seconds: list[float] = []
        star_square_bounds: list[float] = []
        max_second_conservation = max(
            max_second_conservation,
            abs(gaussian_energy_second_moment(hamiltonian, rotated) - initial_second),
        )
        for site in live_sites:
            _probability_one, branches = occupation_branches(rotated, int(site))
            post_hamiltonian = delete_site(hamiltonian, int(site))
            post_live_sites = live_sites[live_sites != site]
            direct_energy = energy(post_hamiltonian, rotated)
            weighted_energy = sum(
                probability * energy(post_hamiltonian, candidate)
                for _outcome, probability, candidate in branches
            )
            max_branch_identity = max(
                max_branch_identity, abs(weighted_energy - direct_energy)
            )
            direct_second = gaussian_energy_second_moment(post_hamiltonian, rotated)
            weighted_second = sum(
                probability
                * gaussian_energy_second_moment(post_hamiltonian, candidate)
                for _outcome, probability, candidate in branches
            )
            max_branch_identity = max(
                max_branch_identity, abs(weighted_second - direct_second)
            )
            star = hamiltonian - post_hamiltonian
            star_second = gaussian_energy_second_moment(star, rotated)
            star_spectrum = np.linalg.eigvalsh(star)
            star_operator_norm = max(
                float(np.sum(star_spectrum[star_spectrum > 0.0])),
                float(-np.sum(star_spectrum[star_spectrum < 0.0])),
            )
            star_square_bound = star_operator_norm**2
            max_star_square_bound = max(max_star_square_bound, star_square_bound)
            max_star_bound_residual = max(
                max_star_bound_residual, max(0.0, star_second - star_square_bound)
            )
            expected_energies.append(weighted_energy)
            expected_numbers.append(
                sum(
                    probability
                    * float(
                        np.trace(
                            candidate[np.ix_(post_live_sites, post_live_sites)]
                        ).real
                    )
                    for _outcome, probability, candidate in branches
                )
            )
            expected_seconds.append(weighted_second)
            star_seconds.append(star_second)
            star_square_bounds.append(star_square_bound)
        mean_energy = float(np.dot(uniform_weights, expected_energies))
        mean_number = float(np.dot(uniform_weights, expected_numbers))
        mean_second = float(np.dot(uniform_weights, expected_seconds))
        second_reference = (
            (1.0 - 4.0 / live_count) * initial_second
            + float(np.dot(uniform_weights, star_seconds))
        )
        post_variance = mean_second - mean_energy**2
        variance_budget = initial_variance + float(
            np.dot(uniform_weights, star_square_bounds)
        )
        max_second_residual = max(
            max_second_residual, abs(mean_second - second_reference)
        )
        max_variance_budget_residual = max(
            max_variance_budget_residual, max(0.0, post_variance - variance_budget)
        )
        max_energy_residual = max(
            max_energy_residual,
            abs(mean_energy - (1.0 - 2.0 / live_count) * initial_energy),
        )
        max_number_residual = max(
            max_number_residual,
            abs(mean_number - (1.0 - 1.0 / live_count) * initial_live_number),
        )
        for site, outcome in records.items():
            row = rotated[site, :].copy()
            row[site] = 0.0
            max_record_residual = max(
                max_record_residual,
                abs(float(rotated[site, site].real) - outcome),
                max_abs(row),
            )
    return {
        "energy": max_energy_residual,
        "number": max_number_residual,
        "branch": max_branch_identity,
        "record": max_record_residual,
        "second": max_second_residual,
        "second_conservation": max_second_conservation,
        "star_bound": max_star_bound_residual,
        "variance_budget": max_variance_budget_residual,
        "max_star_square": max_star_square_bound,
        "live": float(live_count),
        "records": float(len(records)),
        "phases": 3.0,
    }


def jordan_wigner_annihilators(mode_count: int) -> list[np.ndarray]:
    if not 1 <= mode_count <= 4:
        raise ValueError("Jordan-Wigner fixture requires one through four modes")
    dimension = 1 << mode_count
    operators: list[np.ndarray] = []
    for mode in range(mode_count):
        annihilator = np.zeros((dimension, dimension), dtype=np.complex128)
        for state in range(dimension):
            if (state >> mode) & 1:
                target = state ^ (1 << mode)
                parity = (state & ((1 << mode) - 1)).bit_count()
                annihilator[target, state] = -1.0 if parity % 2 else 1.0
        operators.append(annihilator)
    return operators


def fixed_number_indices(mode_count: int, particles: int) -> np.ndarray:
    if not 0 <= particles <= mode_count:
        raise ValueError("fixed particle number is outside the Fock carrier")
    return np.array(
        [state for state in range(1 << mode_count) if state.bit_count() == particles],
        dtype=int,
    )


def second_quantized_one_body(
    one_body: np.ndarray, annihilators: list[np.ndarray], sector: np.ndarray
) -> np.ndarray:
    mode_count = len(annihilators)
    if one_body.shape != (mode_count, mode_count):
        raise ValueError("one-body matrix has the wrong dimension")
    full = np.zeros_like(annihilators[0])
    for i in range(mode_count):
        for j in range(mode_count):
            full += one_body[i, j] * annihilators[i].conj().T @ annihilators[j]
    return full[np.ix_(sector, sector)]


def block_diagonal(*blocks: np.ndarray) -> np.ndarray:
    rows = sum(block.shape[0] for block in blocks)
    cols = sum(block.shape[1] for block in blocks)
    result = np.zeros((rows, cols), dtype=np.complex128)
    row = col = 0
    for block in blocks:
        result[row : row + block.shape[0], col : col + block.shape[1]] = block
        row += block.shape[0]
        col += block.shape[1]
    return result


def matrix_sqrt_psd(matrix: np.ndarray) -> tuple[np.ndarray, float]:
    hermitian = (matrix + matrix.conj().T) / 2.0
    values, vectors = np.linalg.eigh(hermitian)
    minimum = float(np.min(values))
    cleaned = np.where(np.abs(values) < 1.0e-12, 0.0, values)
    root = (vectors * np.sqrt(np.maximum(cleaned, 0.0))[None, :]) @ vectors.conj().T
    return root, minimum


def discrete_sine(start: int, width: int, battery_levels: int) -> np.ndarray:
    if type(start) is not int or type(width) is not int or type(battery_levels) is not int:
        raise ValueError("discrete sine parameters must be integers")
    if start < 0 or width < 1 or start + width > battery_levels:
        raise ValueError("discrete sine support is outside the finite battery")
    result = np.zeros(battery_levels, dtype=np.complex128)
    points = np.arange(1, width + 1, dtype=float)
    result[start : start + width] = np.sqrt(2.0 / (width + 1.0)) * np.sin(
        np.pi * points / (width + 1.0)
    )
    return result


def spectral_lift_apply(
    operator: np.ndarray,
    input_hamiltonian: np.ndarray,
    output_hamiltonian: np.ndarray,
    input_tensor: np.ndarray,
) -> tuple[np.ndarray, float]:
    """Apply the integer-energy translation lift without tracing the battery."""
    if operator.shape != (len(output_hamiltonian), len(input_hamiltonian)):
        raise ValueError("operator dimensions do not match Hamiltonians")
    if input_tensor.ndim != 2 or input_tensor.shape[0] != len(input_hamiltonian):
        raise ValueError("input tensor has the wrong matter dimension")
    input_values, input_vectors = np.linalg.eigh(input_hamiltonian)
    output_values, output_vectors = np.linalg.eigh(output_hamiltonian)
    amplitudes = output_vectors.conj().T @ operator @ input_vectors
    input_spectral = input_vectors.conj().T @ input_tensor
    output_spectral = np.zeros(
        (len(output_hamiltonian), input_tensor.shape[1]), dtype=np.complex128
    )
    max_commensurability = 0.0
    for output_index, input_index in zip(*np.nonzero(np.abs(amplitudes) > 1.0e-12)):
        gap = input_values[input_index] - output_values[output_index]
        shift = int(np.rint(gap))
        max_commensurability = max(max_commensurability, abs(float(gap - shift)))
        if abs(gap - shift) > 2.0e-9:
            raise ValueError("spectral lift requires integer-commensurate gaps")
        amplitude = amplitudes[output_index, input_index]
        for q_in in range(input_tensor.shape[1]):
            q_out = q_in + shift
            if 0 <= q_out < input_tensor.shape[1]:
                output_spectral[output_index, q_out] += (
                    amplitude * input_spectral[input_index, q_in]
                )
    return output_vectors @ output_spectral, max_commensurability


def spectral_lift_matrix(
    operator: np.ndarray,
    input_hamiltonian: np.ndarray,
    output_hamiltonian: np.ndarray,
    battery_levels: int,
) -> tuple[np.ndarray, float]:
    if not 1 <= battery_levels <= 80:
        raise ValueError("finite fixture battery dimension is outside its domain")
    input_values, input_vectors = np.linalg.eigh(input_hamiltonian)
    output_values, output_vectors = np.linalg.eigh(output_hamiltonian)
    amplitudes = output_vectors.conj().T @ operator @ input_vectors
    spectral = np.zeros(
        (
            len(output_hamiltonian) * battery_levels,
            len(input_hamiltonian) * battery_levels,
        ),
        dtype=np.complex128,
    )
    max_commensurability = 0.0
    for output_index, input_index in zip(*np.nonzero(np.abs(amplitudes) > 1.0e-12)):
        gap = input_values[input_index] - output_values[output_index]
        shift = int(np.rint(gap))
        max_commensurability = max(max_commensurability, abs(float(gap - shift)))
        if abs(gap - shift) > 2.0e-9:
            raise ValueError("spectral lift requires integer-commensurate gaps")
        for q_in in range(battery_levels):
            q_out = q_in + shift
            if 0 <= q_out < battery_levels:
                spectral[
                    output_index * battery_levels + q_out,
                    input_index * battery_levels + q_in,
                ] += amplitudes[output_index, input_index]
    rotate_output = np.kron(output_vectors, np.eye(battery_levels))
    rotate_input = np.kron(input_vectors.conj().T, np.eye(battery_levels))
    return rotate_output @ spectral @ rotate_input, max_commensurability


def lift_map_for_battery(
    operator: np.ndarray,
    input_hamiltonian: np.ndarray,
    output_hamiltonian: np.ndarray,
    battery: np.ndarray,
) -> tuple[np.ndarray, float]:
    result = np.zeros(
        (len(output_hamiltonian), len(battery), len(input_hamiltonian)),
        dtype=np.complex128,
    )
    residual = 0.0
    for column in range(len(input_hamiltonian)):
        state = np.zeros((len(input_hamiltonian), len(battery)), dtype=np.complex128)
        state[column, :] = battery
        lifted, current = spectral_lift_apply(
            operator, input_hamiltonian, output_hamiltonian, state
        )
        result[:, :, column] = lifted
        residual = max(residual, current)
    return result, residual


def tensor_matter_energy(state: np.ndarray, hamiltonian: np.ndarray) -> float:
    return float(
        np.real(
            sum(np.vdot(state[:, q], hamiltonian @ state[:, q]) for q in range(state.shape[1]))
        )
    )


def tensor_battery_energy(state: np.ndarray) -> float:
    probabilities = np.sum(np.abs(state) ** 2, axis=0)
    return float(np.dot(np.arange(state.shape[1], dtype=float), probabilities).real)


def choi_state(kraus: list[np.ndarray]) -> np.ndarray:
    if not kraus:
        raise ValueError("a channel needs at least one Kraus operator")
    input_dimension = kraus[0].shape[1]
    choi = np.zeros(
        (kraus[0].shape[0] * input_dimension,) * 2, dtype=np.complex128
    )
    for operator in kraus:
        vector = operator.reshape(-1, order="F")
        choi += np.outer(vector, vector.conj())
    return (choi + choi.conj().T) / (2.0 * input_dimension)


def trace_distance(first: np.ndarray, second: np.ndarray) -> float:
    values = np.linalg.eigvalsh((first - second + first.conj().T - second.conj().T) / 2.0)
    return float(np.sum(np.abs(values)) / 2.0)


def fixed_battery_kraus(
    operator: np.ndarray,
    output_dimension: int,
    input_dimension: int,
    battery: np.ndarray,
) -> list[np.ndarray]:
    levels = len(battery)
    tensor = operator.reshape(output_dimension, levels, input_dimension, levels)
    return [tensor[:, level, :, :] @ battery for level in range(levels)]


def dimer_matter_data() -> dict[str, object]:
    mode_count, particles = 4, 2
    annihilators = jordan_wigner_annihilators(mode_count)
    sector = fixed_number_indices(mode_count, particles)
    one_body = np.zeros((mode_count, mode_count), dtype=np.complex128)
    phase_first = np.exp(0.37j)
    phase_second = np.exp(-0.61j)
    one_body[0, 1], one_body[1, 0] = phase_first, phase_first.conjugate()
    one_body[2, 3], one_body[3, 2] = phase_second, phase_second.conjugate()
    after_first = delete_site(one_body, 0)
    after_second = delete_site(after_first, 2)
    h0 = second_quantized_one_body(one_body, annihilators, sector)
    h1 = second_quantized_one_body(after_first, annihilators, sector)
    h2 = second_quantized_one_body(after_second, annihilators, sector)
    number_ops = [
        (annihilators[mode].conj().T @ annihilators[mode])[np.ix_(sector, sector)]
        for mode in range(mode_count)
    ]
    identity = np.eye(len(sector), dtype=np.complex128)
    p0 = [identity - number_ops[0], number_ops[0]]
    p2 = [identity - number_ops[2], number_ops[2]]
    w1 = np.vstack(p0)
    hmid = block_diagonal(h1, h1)
    w2_history = np.zeros((4 * len(sector), 2 * len(sector)), dtype=np.complex128)
    for first_outcome in range(2):
        for second_outcome in range(2):
            history = 2 * first_outcome + second_outcome
            w2_history[
                history * len(sector) : (history + 1) * len(sector),
                first_outcome * len(sector) : (first_outcome + 1) * len(sector),
            ] = p2[second_outcome]
    hfinal = block_diagonal(h2, h2, h2, h2)
    return {
        "sector": sector,
        "h0": h0,
        "h1": h1,
        "h2": h2,
        "hmid": hmid,
        "hfinal": hfinal,
        "p0": p0,
        "p2": p2,
        "w1": w1,
        "w2_history": w2_history,
    }


def boundary_apparatus_fixture(data: dict[str, object]) -> dict[str, float]:
    h0 = np.asarray(data["h0"])
    h1 = np.asarray(data["h1"])
    hmid = np.asarray(data["hmid"])
    w1 = np.asarray(data["w1"])
    p0 = list(data["p0"])
    dimension = len(h0)
    battery_levels = 5
    levels = np.arange(battery_levels, dtype=float)
    battery = discrete_sine(0, 3, battery_levels)
    lift, commensurability = spectral_lift_matrix(
        w1, h0, hmid, battery_levels
    )
    defect = np.eye(dimension * battery_levels) - lift.conj().T @ lift
    refusal_sqrt, defect_minimum = matrix_sqrt_psd(defect)
    defect_projector = max_abs(defect @ defect - defect)
    refusal = (defect + defect.conj().T) / 2.0
    square_root_residual = max_abs(refusal - refusal_sqrt)
    input_total = np.kron(h0, np.eye(battery_levels)) + np.kron(
        np.eye(dimension), np.diag(levels)
    )
    output_total = np.kron(hmid, np.eye(battery_levels)) + np.kron(
        np.eye(2 * dimension), np.diag(levels)
    )
    completion = max_abs(
        lift.conj().T @ lift + refusal.conj().T @ refusal - np.eye(len(defect))
    )
    energy_residual = max(
        max_abs(output_total @ lift - lift @ input_total),
        max_abs(input_total @ refusal - refusal @ input_total),
    )

    values, vectors = np.linalg.eigh(h0)
    ground = vectors[:, int(np.argmin(values))]
    rho = np.outer(ground, ground.conj())
    rho_battery = np.kron(rho, np.outer(battery, battery.conj()))
    success_state = lift @ rho_battery @ lift.conj().T
    refusal_state = refusal @ rho_battery @ refusal.conj().T
    refusal_probability = float(np.trace(refusal_state).real)
    total_before = float(np.trace(input_total @ rho_battery).real)
    total_after = float(
        np.trace(output_total @ success_state).real
        + np.trace(input_total @ refusal_state).real
    )

    success_kraus = fixed_battery_kraus(
        lift, 2 * dimension, dimension, battery
    )
    refusal_kraus = fixed_battery_kraus(
        refusal, dimension, dimension, battery
    )
    total_output = 3 * dimension
    coherent_kraus: list[np.ndarray] = []
    status_kraus: list[np.ndarray] = []
    cq_kraus: list[np.ndarray] = []
    for success, failed in zip(success_kraus, refusal_kraus):
        success_embed = np.zeros((total_output, dimension), dtype=np.complex128)
        refusal_embed = np.zeros_like(success_embed)
        success_embed[: 2 * dimension, :] = success
        refusal_embed[2 * dimension :, :] = failed
        coherent_kraus.append(success_embed + refusal_embed)
        status_kraus.extend([success_embed, refusal_embed])
        for outcome in range(2):
            outcome_embed = np.zeros_like(success_embed)
            sl = slice(outcome * dimension, (outcome + 1) * dimension)
            outcome_embed[sl, :] = success[sl, :]
            cq_kraus.append(outcome_embed)
        cq_kraus.append(refusal_embed)

    completeness_kraus = sum(
        (operator.conj().T @ operator for operator in cq_kraus),
        np.zeros((dimension, dimension), dtype=np.complex128),
    )
    cq_choi = choi_state(cq_kraus)
    coherent_choi = choi_state(coherent_kraus)
    status_choi = choi_state(status_kraus)
    ideal_kraus: list[np.ndarray] = []
    for outcome in range(2):
        operator = np.zeros((total_output, dimension), dtype=np.complex128)
        operator[outcome * dimension : (outcome + 1) * dimension, :] = p0[outcome]
        ideal_kraus.append(operator)
    ideal_choi = choi_state(ideal_kraus)
    status_output = sum(
        (operator @ rho @ operator.conj().T for operator in status_kraus),
        np.zeros((total_output, total_output), dtype=np.complex128),
    )
    status_off_diagonal = max_abs(status_output[: 2 * dimension, 2 * dimension :])

    v = h0 - h1
    d = hmid @ w1 - w1 @ h0
    k2 = hmid @ d - d @ h0
    kappa = float(np.linalg.norm(v, 2))
    k2_residual = max_abs(k2 - w1 @ (v @ v + v @ h0 - h0 @ v))
    d_residual = max_abs(d + w1 @ v)
    c_value = (float(np.linalg.norm(k2, 2)) + kappa**2) / 2.0
    c_bound = kappa**2 + 3.0 * kappa
    return {
        "commensurability": commensurability,
        "defect_minimum": defect_minimum,
        "completion": completion,
        "defect_projector": defect_projector,
        "square_root": square_root_residual,
        "energy": max(energy_residual, abs(total_after - total_before)),
        "refusal_probability": refusal_probability,
        "kraus": max_abs(completeness_kraus - np.eye(dimension)),
        "choi_minimum": float(np.min(np.linalg.eigvalsh(cq_choi))),
        "status_off_diagonal": status_off_diagonal,
        "status_read_distance": trace_distance(coherent_choi, status_choi),
        "normalized_choi_distance": trace_distance(cq_choi, ideal_choi),
        "d_residual": d_residual,
        "k2_residual": k2_residual,
        "kappa": kappa,
        "c_value": c_value,
        "c_bound": c_bound,
        "sine_norm": abs(float(np.vdot(battery, battery).real) - 1.0),
    }


def shared_battery_two_event_fixture(data: dict[str, object]) -> dict[str, float]:
    h0 = np.asarray(data["h0"])
    h1 = np.asarray(data["h1"])
    hmid = np.asarray(data["hmid"])
    hfinal = np.asarray(data["hfinal"])
    w1 = np.asarray(data["w1"])
    w2_history = np.asarray(data["w2_history"])
    p0 = list(data["p0"])
    p2 = list(data["p2"])
    dimension = len(h0)

    dwell = 0.41
    values1, vectors1 = np.linalg.eigh(h1)
    unitary1 = (vectors1 * np.exp(-1j * dwell * values1)[None, :]) @ vectors1.conj().T
    unitary_mid = block_diagonal(unitary1, unitary1)
    w_total = w2_history @ unitary_mid @ w1

    hopping_bound, modes = 1.0, 4
    system_bound = 3.0 * hopping_bound * modes
    margin = int(2.0 * system_bound)
    width = 9
    battery_levels = 2 * margin + width
    battery = discrete_sine(margin, width, battery_levels)
    first_map, commensurability1 = lift_map_for_battery(w1, h0, hmid, battery)
    after_dwell = np.einsum("ab,bqi->aqi", unitary_mid, first_map)
    sequential = np.zeros(
        (len(hfinal), battery_levels, dimension), dtype=np.complex128
    )
    commensurability2 = 0.0
    for column in range(dimension):
        lifted, residual = spectral_lift_apply(
            w2_history, hmid, hfinal, after_dwell[:, :, column]
        )
        sequential[:, :, column] = lifted
        commensurability2 = max(commensurability2, residual)
    direct, commensurability_direct = lift_map_for_battery(
        w_total, h0, hfinal, battery
    )
    composition_residual = max_abs(sequential - direct)
    first_flat = first_map.reshape(-1, dimension)
    final_flat = sequential.reshape(-1, dimension)
    isometry_residual = max(
        max_abs(first_flat.conj().T @ first_flat - np.eye(dimension)),
        max_abs(final_flat.conj().T @ final_flat - np.eye(dimension)),
    )

    _values0, vectors0 = np.linalg.eigh(h0)
    matter_state = (
        vectors0[:, 0]
        + (0.37 + 0.21j) * vectors0[:, 2]
        + 0.19j * vectors0[:, -1]
    )
    matter_state /= np.linalg.norm(matter_state)
    initial_matter = float(np.vdot(matter_state, h0 @ matter_state).real)
    initial_battery = float(
        np.dot(np.arange(battery_levels, dtype=float), np.abs(battery) ** 2).real
    )
    intermediate = np.tensordot(first_map, matter_state, axes=([2], [0]))
    intermediate_dwell = unitary_mid @ intermediate
    final = np.tensordot(sequential, matter_state, axes=([2], [0]))
    intermediate_matter = tensor_matter_energy(intermediate, hmid)
    intermediate_battery = tensor_battery_energy(intermediate)
    dwell_energy = abs(
        tensor_matter_energy(intermediate_dwell, hmid) - intermediate_matter
    )
    final_matter = tensor_matter_energy(final, hfinal)
    final_battery = tensor_battery_energy(final)
    energy_residual = max(
        abs(intermediate_matter + intermediate_battery - initial_matter - initial_battery),
        abs(final_matter + final_battery - initial_matter - initial_battery),
        dwell_energy,
    )

    record_residual = 0.0
    for first_outcome in range(2):
        for second_outcome in range(2):
            history = 2 * first_outcome + second_outcome
            block = final[history * dimension : (history + 1) * dimension, :]
            record_residual = max(
                record_residual,
                max_abs((np.eye(dimension) - p0[first_outcome]) @ block),
                max_abs((np.eye(dimension) - p2[second_outcome]) @ block),
            )

    singular_values = np.linalg.svd(intermediate_dwell, compute_uv=False)
    schmidt_rank = int(np.count_nonzero(singular_values > 1.0e-10))
    actual_kraus: list[np.ndarray] = []
    ideal_kraus: list[np.ndarray] = []
    for history in range(4):
        history_slice = slice(history * dimension, (history + 1) * dimension)
        for level in range(battery_levels):
            operator = np.zeros((4 * dimension, dimension), dtype=np.complex128)
            operator[history_slice, :] = sequential[history_slice, level, :]
            actual_kraus.append(operator)
        ideal = np.zeros((4 * dimension, dimension), dtype=np.complex128)
        ideal[history_slice, :] = w_total[history_slice, :]
        ideal_kraus.append(ideal)
    actual_choi = choi_state(actual_kraus)
    ideal_choi = choi_state(ideal_kraus)
    normalized_choi_distance = trace_distance(actual_choi, ideal_choi)
    support_first = np.flatnonzero(np.sum(np.abs(intermediate) ** 2, axis=0) > 1.0e-14)
    support_final = np.flatnonzero(np.sum(np.abs(final) ** 2, axis=0) > 1.0e-14)
    support_margin = float(
        min(
            int(support_first[0]),
            battery_levels - 1 - int(support_first[-1]),
            int(support_final[0]),
            battery_levels - 1 - int(support_final[-1]),
        )
    )
    return {
        "commensurability": max(
            commensurability1, commensurability2, commensurability_direct
        ),
        "composition": composition_residual,
        "isometry": isometry_residual,
        "energy": energy_residual,
        "record": record_residual,
        "schmidt_rank": float(schmidt_rank),
        "support_margin": support_margin,
        "normalized_choi_distance": normalized_choi_distance,
        "initial_matter": initial_matter,
        "intermediate_matter": intermediate_matter,
        "final_matter": final_matter,
        "initial_battery": initial_battery,
        "intermediate_battery": intermediate_battery,
        "final_battery": final_battery,
        "system_bound": system_bound,
        "declared_margin": float(margin),
        "battery_levels": float(battery_levels),
    }


def sine_and_budget_probes() -> dict[str, float]:
    nodes, weights = np.polynomial.legendre.leggauss(80)
    a, width, c = 3.0, 7.0, 4.0
    energies = a + width * (nodes + 1.0) / 2.0
    scaled_weights = weights * width / 2.0
    beta = np.sqrt(2.0 / width) * np.sin(np.pi * (energies - a) / width)
    beta_prime = (
        np.sqrt(2.0 / width)
        * np.pi
        / width
        * np.cos(np.pi * (energies - a) / width)
    )
    normalization = float(np.dot(scaled_weights, beta**2))
    second_moment = float(np.dot(scaled_weights, beta_prime**2))

    overlap_nodes, overlap_weights = np.polynomial.legendre.leggauss(80)
    overlap_energies = 1.0 + (overlap_nodes + 1.0) / 2.0
    overlap_beta = np.sqrt(0.5) * np.sin(np.pi * (overlap_energies - 1.0) / 4.0)
    shifted_beta = np.sqrt(0.5) * np.sin(
        np.pi * (overlap_energies + 1.0) / 4.0
    )
    overlap = float(np.dot(overlap_weights / 2.0, overlap_beta * shifted_beta))

    attempts, epsilon, hopping = 27.0, 0.08, 1.0
    delta = epsilon / attempts
    kappa_max = np.sqrt(6.0) * hopping
    c_max = (6.0 + 3.0 * np.sqrt(6.0)) * hopping**2
    fresh_margin = 2.0 * kappa_max / np.sqrt(delta)
    fresh_width = np.pi * np.sqrt(2.0 * c_max / delta)
    fresh_error = attempts * (
        c_max * np.pi**2 / fresh_width**2
        + kappa_max**2 * (fresh_margin**-2 + fresh_margin**-2)
    )
    fresh_refusal = attempts * kappa_max**2 * (
        fresh_margin**-2 + fresh_margin**-2
    )

    modes = 216.0
    system_bound = 3.0 * hopping * modes
    shared_width = 2.0 * np.pi * system_bound / np.sqrt(epsilon)
    shared_cap = 4.0 * system_bound + shared_width
    shared_error = 4.0 * system_bound**2 * np.pi**2 / shared_width**2
    shared_mean = shared_cap / 2.0
    shared_formula = modes * hopping * (6.0 + 3.0 * np.pi / np.sqrt(epsilon))

    bad_calls = 0
    for args in ((-1, 3, 5), (0, 0, 5), (4, 2, 5), (0.5, 2, 5)):
        try:
            discrete_sine(*args)
        except (TypeError, ValueError):
            bad_calls += 1
    return {
        "normalization": abs(normalization - 1.0),
        "second_moment": abs(second_moment - np.pi**2 / width**2),
        "left_margin": a,
        "right_margin": c,
        "status_overlap": overlap,
        "status_overlap_residual": abs(overlap - 1.0 / (2.0 * np.pi)),
        "fresh_error": fresh_error,
        "fresh_refusal": fresh_refusal,
        "shared_error": shared_error,
        "shared_mean": shared_mean,
        "shared_formula_residual": abs(shared_mean - shared_formula),
        "ground_excess_error": 12.0 * hopping * epsilon,
        "bad_calls": float(bad_calls),
    }


class Report:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0

    def check(self, family: str, description: str, condition: bool, detail: str) -> None:
        if condition:
            self.passes += 1
            self.lines.append(f"PASS {family} {description}: {detail}")
        else:
            self.failures += 1
            self.lines.append(f"FAIL {family} {description}: {detail}")


def main() -> int:
    started = time.perf_counter()
    report = Report()

    complex_fixture = complex_gaussian_fixture()
    report.check(
        "G0",
        "deterministic p=0/1 branches omit null outcomes",
        complex_fixture["deterministic_mask"] == 3.0
        and complex_fixture["deterministic_count"] == 2.0,
        f"outcome_mask={int(complex_fixture['deterministic_mask'])} "
        f"count={int(complex_fixture['deterministic_count'])} no_zero_division=yes",
    )
    complex_residual = max(
        complex_fixture["projector"],
        complex_fixture["number"],
        complex_fixture["born"],
        complex_fixture["energy"],
        complex_fixture["record"],
        complex_fixture["dwell"],
        complex_fixture["mean_energy"],
        complex_fixture["mean_number"],
    )
    report.check(
        "G1",
        "complex repeated Gaussian branches and uniform-live means",
        complex_residual < TOL_ENERGY,
        f"live={int(complex_fixture['live'])} max_res={complex_residual:.3e} "
        f"max_branch_selection={complex_fixture['branch_selection']:.6f}",
    )

    phase_probe = phase_rotated_uniform_probe()
    phase_residual = max(
        phase_probe["energy"],
        phase_probe["number"],
        phase_probe["branch"],
        phase_probe["record"],
        phase_probe["second"],
        phase_probe["second_conservation"],
        phase_probe["star_bound"],
        phase_probe["variance_budget"],
    )
    report.check(
        "G1",
        "phase-rotated uniform-live E, N, and H^2 laws after previous Records",
        phase_residual < TOL_ENERGY,
        f"phases={int(phase_probe['phases'])} live={int(phase_probe['live'])} "
        f"prior_records={int(phase_probe['records'])} "
        f"max_res={phase_residual:.3e} H2_res={phase_probe['second']:.3e} "
        f"star_square_bound={phase_probe['max_star_square']:.6f}",
    )

    hamiltonian = build_pi_flux_hamiltonian()
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    negative = eigenvalues < 0.0
    initial_covariance = (
        eigenvectors[:, negative] @ eigenvectors[:, negative].conj().T
    ).astype(np.complex128)
    degrees = np.count_nonzero(np.abs(hamiltonian) > 0.0, axis=1)
    geometry_residual = max(
        float(np.max(np.abs(hamiltonian - hamiltonian.T))),
        float(np.max(np.abs(np.diag(hamiltonian @ hamiltonian) - 6.0))),
        plaquette_residual(),
    )
    initial_residual = max(
        projector_residual(initial_covariance),
        abs(float(np.trace(initial_covariance).real) - N_PARTICLES),
    )
    gap = float(np.min(np.abs(eigenvalues)))
    report.check(
        "G2",
        "L6 pi-flux carrier and filled sea",
        geometry_residual < TOL_MATRIX
        and np.all(degrees == 6)
        and int(np.count_nonzero(negative)) == N_PARTICLES
        and initial_residual < TOL_MATRIX,
        f"sites={N_SITES} particles={np.count_nonzero(negative)} gap={gap:.9f} "
        f"geometry={geometry_residual:.3e} projector={initial_residual:.3e}",
    )

    site_schedules, outcome_uniforms = schedules()

    # Exact one-event, both-outcome control at a fixed site.
    control_site = site_index(3, 3, 3)
    control_p, control_zero, control_one = occupation_candidates(
        initial_covariance, control_site
    )
    control_h = delete_site(hamiltonian, control_site)
    control_pre = energy(hamiltonian, initial_covariance)
    control_reference = energy(control_h, initial_covariance)
    control_e0 = energy(control_h, control_zero)
    control_e1 = energy(control_h, control_one)
    control_weighted = (1.0 - control_p) * control_e0 + control_p * control_e1
    report.check(
        "G2",
        "special initial-sea single-event control",
        abs(control_p - 0.5) < TOL_MATRIX
        and abs(control_e0 - control_e1) < TOL_ENERGY
        and abs(control_weighted - control_reference) < TOL_ENERGY,
        f"p1={control_p:.9f} Epre={control_pre:.9f} Epost0={control_e0:.9f} "
        f"Epost1={control_e1:.9f} "
        f"mean_system_energy_change={control_reference-control_pre:+.9f}",
    )

    scenarios = {
        dwell: run_scenario(
            dwell,
            hamiltonian,
            initial_covariance,
            site_schedules,
            outcome_uniforms,
        )
        for dwell in DWELLS
    }

    for dwell in DWELLS:
        scenario = scenarios[dwell]
        diag = scenario.diagnostics
        invariant_max = max(
            diag.max_projector,
            diag.max_number,
            diag.max_old_record,
            diag.max_old_record_coherence,
            diag.max_deleted_row,
        )
        identity_max = max(
            diag.max_unitary_energy,
            diag.max_mixture_covariance,
            diag.max_weighted_post,
            diag.max_weighted_selection,
            diag.max_ledger,
        )
        report.check(
            "G2" if dwell == 0.0 else "G3",
            f"repeated ideal Gaussian occupation/deletion events tau={dwell:g}",
            invariant_max < TOL_MATRIX
            and identity_max < TOL_ENERGY
            and diag.min_excess >= -TOL_ENERGY,
            f"events={N_TRAJECTORIES*N_EVENTS} invariant_max={invariant_max:.3e} "
            f"identity_max={identity_max:.3e} min_excess={diag.min_excess:.3e} "
            f"p1_range=[{diag.min_probability:.4f},{diag.max_probability:.4f}]",
        )

    enumeration = scenarios[0.5].enumeration
    if enumeration is None:
        raise RuntimeError("missing deterministic live-vertex enumeration")
    enumeration_residual = max(
        enumeration["residual"],
        enumeration["local_residual"],
        enumeration["number_residual"],
    )
    report.check(
        "G3",
        "all-live-vertex energy and live-number expectations",
        enumeration_residual < TOL_ENERGY,
        f"live={int(enumeration['live'])} E={enumeration['energy']:+.9f} "
        f"enumerated={enumeration['mean']:+.9f} "
        f"(1-2/live)E={enumeration['target']:+.9f} "
        f"residual={enumeration_residual:.3e} "
        f"Nlive={enumeration['live_number']:.6f}->"
        f"{enumeration['number_mean']:.6f} "
        f"max_branch_selection={enumeration['branch_selection_max']:.6f}",
    )

    spectral_sea_energy = -0.5 * float(np.sum(np.abs(eigenvalues)))
    fraction = (
        (N_SITES - N_EVENTS)
        * (N_SITES - N_EVENTS - 1)
        / (N_SITES * (N_SITES - 1))
    )
    finite_density_energy = control_pre * fraction / N_SITES
    finite_density_bound = -0.5 * fraction
    exact_live_number = N_PARTICLES * (N_SITES - N_EVENTS) / N_SITES
    variance_growth_budget = float(np.max(np.diag(hamiltonian @ hamiltonian))) * N_EVENTS
    report.check(
        "G3",
        "regular half-filled finite-density arithmetic",
        abs(control_pre - spectral_sea_energy) < TOL_ENERGY
        and control_pre / N_SITES <= -0.5 + TOL_ENERGY
        and finite_density_energy <= finite_density_bound + TOL_ENERGY
        and abs(exact_live_number / (N_SITES - N_EVENTS) - 0.5) < TOL_NUMBER,
        f"E0/M={control_pre/N_SITES:+.9f} K={N_EVENTS} "
        f"EmeanK/M={finite_density_energy:+.9f} bound={finite_density_bound:+.9f} "
        f"E[Nlive]/live={exact_live_number/(N_SITES-N_EVENTS):.6f} "
        f"variance_increment_bound={variance_growth_budget:.3f}",
    )

    report.lines.append(
        "INFO seeds: site={}..{} outcome={}..{} trajectories={} events={} "
        "site stream separate from outcome stream".format(
            SITE_SEED_BASE,
            SITE_SEED_BASE + N_TRAJECTORIES - 1,
            OUTCOME_SEED_BASE,
            OUTCOME_SEED_BASE + N_TRAJECTORIES - 1,
            N_TRAJECTORIES,
            N_EVENTS,
        )
    )
    report.lines.append(
        "INFO ledger: D=Tr[(H_before-H_after)C_before], "
        "S_n=Tr[H_after C_n]-Tr[H_after C_before], "
        "DeltaE_sys,n=Epost_n-Epre=S_n-D; sum_n p_n S_n=0"
    )
    report.lines.append(
        "MC step exact_Emean tau0_mean tau0_SE tau05_mean tau05_SE "
        "exact_Nlive tau05_Nlive tau05_Nlive_SE "
        "(ideal-instrument finite-sample comparator; not a deterministic gate)"
    )
    for step in (1, 2, 5, 10, 18, 27):
        zero = scenarios[0.0]
        half = scenarios[0.5]
        zero_mean, zero_se = mean_and_se_at(zero, step, "post")
        half_mean, half_se = mean_and_se_at(half, step, "post")
        live_mean, live_se = mean_and_se_at(half, step, "live_particles")
        exact_mean = control_pre * (
            (N_SITES - step)
            * (N_SITES - step - 1)
            / (N_SITES * (N_SITES - 1))
        )
        exact_live = N_PARTICLES * (N_SITES - step) / N_SITES
        report.lines.append(
            f"MC {step:02d} {exact_mean:+.6f} {zero_mean:+.6f} {zero_se:.6f} "
            f"{half_mean:+.6f} {half_se:.6f} {exact_live:.4f} "
            f"{live_mean:.4f} {live_se:.4f}"
        )

    report.lines.append(
        "LEDGER tau step Epre Epost deleted_star selection delta_system_energy "
        "cumulative_delta_system_energy fixedN_ground excess/live surviving_bonds"
    )
    for step in (1, 10, 27):
        for dwell in DWELLS:
            scenario = scenarios[dwell]
            report.lines.append(
                f"LEDGER {dwell:g} {step:02d} "
                f"{mean_at(scenario,step,'pre'):+.6f} "
                f"{mean_at(scenario,step,'post'):+.6f} "
                f"{mean_at(scenario,step,'deleted'):+.6f} "
                f"{mean_at(scenario,step,'selection'):+.6f} "
                f"{mean_at(scenario,step,'system_energy_change'):+.6f} "
                f"{mean_at(scenario,step,'cumulative_system_energy_change'):+.6f} "
                f"{mean_at(scenario,step,'ground'):+.6f} "
                f"{mean_at(scenario,step,'excess_per_live'):.8f} "
                f"{mean_at(scenario,step,'bonds'):.2f}"
            )

    for dwell in DWELLS:
        scenario = scenarios[dwell]
        cumulative_mean, cumulative_se = final_mean_and_se(
            scenario, "cumulative_system_energy_change"
        )
        excess_mean, excess_se = final_mean_and_se(scenario, "excess_per_live")
        ground_mean, ground_se = final_mean_and_se(scenario, "ground")
        selection_values = np.array(
            [row["selection"] for trajectory in scenario.rows for row in trajectory]
        )
        deleted_values = np.array(
            [row["deleted"] for trajectory in scenario.rows for row in trajectory]
        )
        report.lines.append(
            f"SUMMARY tau={dwell:g} "
            f"final_cumulative_delta_system_energy={cumulative_mean:+.6f}"
            f"+/-{cumulative_se:.6f} "
            f"final_ground={ground_mean:+.6f}+/-{ground_se:.6f} "
            f"final_excess/live={excess_mean:.8f}+/-{excess_se:.8f} "
            f"sample_selection_mean={np.mean(selection_values):+.6f} "
            f"sample_deleted_star_mean={np.mean(deleted_values):+.6f}"
        )

    matter_data = dimer_matter_data()
    boundary = boundary_apparatus_fixture(matter_data)
    boundary_residual = max(
        boundary["commensurability"],
        max(0.0, -boundary["defect_minimum"]),
        boundary["completion"],
        boundary["defect_projector"],
        boundary["square_root"],
        boundary["energy"],
        boundary["kraus"],
        max(0.0, -boundary["choi_minimum"]),
        boundary["status_off_diagonal"],
        boundary["d_residual"],
        boundary["k2_residual"],
        boundary["sine_norm"],
    )
    report.check(
        "G4",
        "four-mode N=2 finite apparatus energy and CP completion",
        boundary_residual < 2.0e-9
        and 1.0e-8 < boundary["refusal_probability"] < 1.0
        and boundary["c_value"] <= boundary["c_bound"] + TOL_ENERGY,
        f"max_res={boundary_residual:.3e} refusal={boundary['refusal_probability']:.6f} "
        f"kappa={boundary['kappa']:.6f} C={boundary['c_value']:.6f} "
        f"bound={boundary['c_bound']:.6f}",
    )
    report.check(
        "G4",
        "explicit status readout removes success-refusal coherence",
        boundary["status_read_distance"] > 1.0e-6
        and boundary["status_off_diagonal"] < TOL_MATRIX
        and 0.0 <= boundary["normalized_choi_distance"] <= 1.0 + TOL_MATRIX,
        f"coherent_vs_read={boundary['status_read_distance']:.6f} "
        f"read_cross={boundary['status_off_diagonal']:.3e} "
        f"normalized_choi_distance={boundary['normalized_choi_distance']:.6f} "
        f"(not_diamond_bound)",
    )

    shared = shared_battery_two_event_fixture(matter_data)
    shared_residual = max(
        shared["commensurability"],
        shared["composition"],
        shared["isometry"],
        shared["energy"],
        shared["record"],
    )
    report.check(
        "G5",
        "two events reuse one correlated battery and telescope to total lift",
        shared_residual < 3.0e-9
        and shared["schmidt_rank"] > 1.0
        and shared["support_margin"] > 0.0,
        f"max_res={shared_residual:.3e} Schmidt_rank={int(shared['schmidt_rank'])} "
        f"support_margin={int(shared['support_margin'])} "
        f"declared_margin={int(shared['declared_margin'])} levels={int(shared['battery_levels'])}",
    )
    report.check(
        "G5",
        "intermediate and final matter-plus-battery ledger",
        shared["energy"] < TOL_ENERGY
        and 0.0 <= shared["normalized_choi_distance"] <= 1.0 + TOL_MATRIX,
        f"matter={shared['initial_matter']:+.6f}->{shared['intermediate_matter']:+.6f}"
        f"->{shared['final_matter']:+.6f} battery={shared['initial_battery']:.6f}"
        f"->{shared['intermediate_battery']:.6f}->{shared['final_battery']:.6f} "
        f"normalized_choi_distance={shared['normalized_choi_distance']:.6f} "
        f"(not_diamond_bound)",
    )

    probes = sine_and_budget_probes()
    probe_residual = max(
        probes["normalization"],
        probes["second_moment"],
        probes["status_overlap_residual"],
        abs(probes["fresh_error"] - 0.08),
        abs(probes["fresh_refusal"] - 0.04),
        abs(probes["shared_error"] - 0.08),
        probes["shared_formula_residual"],
    )
    report.check(
        "G6",
        "sine, margins, and fresh/shared error-budget arithmetic probes",
        probe_residual < 2.0e-10
        and probes["left_margin"] > 0.0
        and probes["right_margin"] > 0.0
        and probes["bad_calls"] == 4.0,
        f"max_res={probe_residual:.3e} overlap={probes['status_overlap']:.9f} "
        f"fresh=(err={probes['fresh_error']:.3f},ref={probes['fresh_refusal']:.3f}) "
        f"shared=(err={probes['shared_error']:.3f},meanE={probes['shared_mean']:.3f})",
    )
    report.lines.append(
        f"PROBE generic_continuity_bound epsilon=0.08 "
        f"broad_history_ground_excess_difference/M"
        f"<={probes['ground_excess_error']:.3f}; arithmetic_only=no_proof"
    )

    report.lines.append(
        "SCOPE 216-mode Gaussian rows use the ideal occupation/deletion instrument; "
        "energy-conserving battery lifts run only in separate four-mode dimer fixtures"
    )
    report.lines.append(
        "SCOPE MC +/- are trajectory standard errors, not pass windows; dimer spectra are "
        "commensurate; normalized Choi distances are not diamond bounds; sine/scaling "
        "rows are arithmetic probes, not continuum proofs"
    )
    report.lines.append(
        "SCOPE no physical clock/rate, Record compiler, local spectral-gate compiler, "
        "battery preparation/renewal, scheduler-memory bound, stationary matter, gravity "
        "source, thermodynamic convergence, or photon result is inferred"
    )
    elapsed = time.perf_counter() - started
    memory = rss_mib()
    report.check(
        "G7",
        "execution envelope",
        elapsed <= RUNTIME_LIMIT_SEC and memory < RSS_LIMIT_MIB,
        f"elapsed={elapsed:.2f}s limit={RUNTIME_LIMIT_SEC:.0f}s "
        f"rss={memory:.1f}MiB limit={RSS_LIMIT_MIB:.0f}MiB BLAS_threads=1",
    )
    projected_chars = len("\n".join(report.lines)) + 100
    report.check(
        "G7",
        "concise stdout",
        projected_chars < STDOUT_LIMIT,
        f"projected_chars={projected_chars} limit={STDOUT_LIMIT}",
    )
    report.lines.append(f"TOTAL: PASS={report.passes} FAIL={report.failures}")
    print("\n".join(report.lines))
    return 1 if report.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
