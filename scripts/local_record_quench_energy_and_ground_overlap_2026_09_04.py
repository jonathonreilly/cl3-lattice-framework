#!/usr/bin/env python3
"""Finite-matrix primary checks for a local occupation Record quench.

The runner uses one-particle correlation projectors only.  It constructs the
initial negative sea by diagonalising the full bipartite Hamiltonian, applies
occupation measurements by sequential Gaussian Schur updates, and compares
the result with closed forms only afterwards.  The cubic calculations stop at
512 one-particle sites and make no thermodynamic-limit claim.
"""

from __future__ import annotations

import itertools
import os

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
):
    os.environ[_thread_variable] = "1"

AUDIT_TIMEOUT_SEC = 180

import resource
import sys
import time
from dataclasses import dataclass

import numpy as np
from scipy.integrate import quad


MAX_ONE_PARTICLE_SITES = 512
LINEAR_TOL = 3.0e-10
QUAD_TOL = 2.0e-8


def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
    """Hermitian positive square root, rejecting a materially negative input."""

    values, vectors = np.linalg.eigh(matrix)
    scale = max(1.0, float(np.max(np.abs(values))))
    if float(np.min(values)) < -2.0e-12 * scale:
        raise ValueError("matrix is not positive semidefinite")
    return (vectors * np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T


def validate_q(q_matrix: np.ndarray) -> np.ndarray:
    q_matrix = np.asarray(q_matrix, dtype=np.complex128)
    if q_matrix.ndim != 2 or q_matrix.shape[0] != q_matrix.shape[1]:
        raise ValueError("Q must be a nonempty square matrix")
    if q_matrix.shape[0] == 0 or 2 * q_matrix.shape[0] > MAX_ONE_PARTICLE_SITES:
        raise ValueError("Q violates the one-particle dimension bound")
    if not np.all(np.isfinite(q_matrix)):
        raise ValueError("Q must be finite")
    singular_values = np.linalg.svd(q_matrix, compute_uv=False)
    if float(np.min(singular_values)) <= 1.0e-11 * max(1.0, float(np.max(singular_values))):
        raise ValueError("Q must be numerically invertible")
    return q_matrix


def bipartite_hamiltonian(q_matrix: np.ndarray) -> np.ndarray:
    q_matrix = validate_q(q_matrix)
    m = q_matrix.shape[0]
    zero = np.zeros((m, m), dtype=np.complex128)
    return np.block([[zero, q_matrix], [q_matrix.conj().T, zero]])


def negative_projector(hamiltonian: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    values, vectors = np.linalg.eigh(hamiltonian)
    scale = max(1.0, float(np.max(np.abs(values))))
    if float(np.min(np.abs(values))) <= 1.0e-11 * scale:
        raise ValueError("negative projector requires a zero-free Hamiltonian")
    occupied = vectors[:, values < 0.0]
    if occupied.shape[1] * 2 != hamiltonian.shape[0]:
        raise ValueError("bipartite spectrum has the wrong negative-level count")
    return occupied @ occupied.conj().T, values


def validate_measurement(
    dimension: int, measured: tuple[int, ...], outcomes: tuple[int, ...]
) -> None:
    if len(measured) != len(outcomes):
        raise ValueError("one binary outcome is required per measured mode")
    if len(set(measured)) != len(measured):
        raise ValueError("measured modes must be unique")
    if any(index < 0 or index >= dimension for index in measured):
        raise ValueError("measured mode is outside the covariance")
    if any(outcome not in (0, 1) for outcome in outcomes):
        raise ValueError("occupation outcomes must be binary")


def condition_occupations(
    initial: np.ndarray, measured: tuple[int, ...], outcomes: tuple[int, ...]
) -> tuple[np.ndarray, tuple[int, ...], float]:
    """Sequential number-measurement update, with measured modes removed."""

    validate_measurement(initial.shape[0], measured, outcomes)
    covariance = np.array(initial, dtype=np.complex128, copy=True)
    remaining = list(range(initial.shape[0]))
    probability = 1.0
    for original_index, outcome in zip(measured, outcomes):
        current_index = remaining.index(original_index)
        occupied_probability = float(covariance[current_index, current_index].real)
        branch_probability = occupied_probability if outcome == 1 else 1.0 - occupied_probability
        if branch_probability <= 1.0e-13:
            raise ValueError("requested measurement branch has zero probability")
        rest = [j for j in range(len(remaining)) if j != current_index]
        column = covariance[np.ix_(rest, [current_index])]
        row = covariance[np.ix_([current_index], rest)]
        sign = 1.0 if outcome == 0 else -1.0
        covariance = covariance[np.ix_(rest, rest)] + sign * column @ row / branch_probability
        covariance = 0.5 * (covariance + covariance.conj().T)
        probability *= branch_probability
        remaining.pop(current_index)
    return covariance, tuple(remaining), probability


def closed_conditional_covariance(
    unitary: np.ndarray, measured_a: tuple[int, ...], outcomes: tuple[int, ...]
) -> np.ndarray:
    """Closed expression used only as a comparator to the iterative update."""

    m = unitary.shape[0]
    validate_measurement(m, measured_a, outcomes)
    measured_set = set(measured_a)
    unmeasured = tuple(index for index in range(m) if index not in measured_set)
    u_t = unitary[np.array(unmeasured, dtype=int), :] if unmeasured else np.zeros((0, m), complex)
    lower = 0.5 * np.eye(m, dtype=complex)
    for index, outcome in zip(measured_a, outcomes):
        row = unitary[index, :]
        lower += (0.5 - float(outcome)) * np.outer(row.conj(), row)
    return np.block(
        [
            [0.5 * np.eye(len(unmeasured)), -0.5 * u_t],
            [-0.5 * u_t.conj().T, lower],
        ]
    )


def reduced_hamiltonian(q_matrix: np.ndarray, unmeasured: tuple[int, ...]) -> np.ndarray:
    q_t = q_matrix[np.array(unmeasured, dtype=int), :] if unmeasured else np.zeros((0, q_matrix.shape[1]), complex)
    return np.block(
        [
            [np.zeros((len(unmeasured), len(unmeasured)), complex), q_t],
            [q_t.conj().T, np.zeros((q_matrix.shape[1], q_matrix.shape[1]), complex)],
        ]
    )


def deterministic_unitary(raw: np.ndarray) -> np.ndarray:
    q_matrix, r_matrix = np.linalg.qr(np.asarray(raw, dtype=np.complex128))
    phases = np.diag(r_matrix)
    phases = np.where(np.abs(phases) > 0.0, phases / np.abs(phases), 1.0)
    return q_matrix @ np.diag(phases.conj())


def every_outcome(size: int) -> tuple[tuple[int, ...], ...]:
    return tuple(itertools.product((0, 1), repeat=size))


@dataclass
class GenericMetrics:
    initial_residual: float
    conditional_residual: float
    order_residual: float
    probability_residual: float
    purity_residual: float
    number_residual: float
    energy_residual: float
    ground_residual: float
    branch_spread: float
    jump_residual: float
    lower_violation: float
    upper_violation: float
    nonreducing_norm: float
    unitary_residual: float
    imaginary_norm: float
    diagonal_delta: float
    diagonal_jump: float
    probability_range: tuple[float, float]
    particle_range: tuple[float, float]
    post_energy_range: tuple[float, float]
    ground_energy_range: tuple[float, float]


def generic_gaussian_checks() -> GenericMetrics:
    """Complex finite example: eigensea -> iterative measurements -> formulas."""

    raw_k = np.array(
        [
            [1 + 2j, 2 - 1j, -1 + 0.5j, 0.3 + 0.7j],
            [0.2 - 1.1j, 1.5 + 0.4j, 2.2 + 0.1j, -0.8j],
            [1.7 + 0.3j, -0.4 + 1.3j, 0.9 - 0.2j, 1.1 + 0.6j],
            [-0.6 + 0.8j, 0.5 - 0.9j, 1.4 + 1.2j, 1.8 - 0.3j],
        ]
    )
    raw_u = np.array(
        [
            [0.5 + 0.7j, 1.2 - 0.2j, -0.3 + 1.1j, 0.8 + 0.4j],
            [1.1 - 0.6j, -0.4 + 0.9j, 0.7 + 0.3j, 1.5 - 0.8j],
            [-0.2 + 1.4j, 0.6 + 0.5j, 1.3 - 0.7j, -0.5 + 0.2j],
            [0.9 + 0.1j, -1.0 - 0.3j, 0.4 + 0.8j, 0.7 + 1.2j],
        ]
    )
    v_matrix = deterministic_unitary(raw_k)
    unitary = deterministic_unitary(raw_u)
    eigenvalues = np.array([0.7, 1.2, 1.9, 2.8])
    k_matrix = (v_matrix * eigenvalues) @ v_matrix.conj().T
    q_matrix = k_matrix @ unitary
    hamiltonian = bipartite_hamiltonian(q_matrix)
    initial, spectrum = negative_projector(hamiltonian)
    m = q_matrix.shape[0]

    recovered_k = positive_sqrt(q_matrix @ q_matrix.conj().T)
    recovered_u = np.linalg.solve(recovered_k, q_matrix)
    polar_initial = 0.5 * np.block(
        [
            [np.eye(m), -recovered_u],
            [-recovered_u.conj().T, np.eye(m)],
        ]
    )
    metrics = {
        "initial": float(np.linalg.norm(initial - polar_initial, ord="fro")),
        "conditional": 0.0,
        "order": 0.0,
        "probability": 0.0,
        "purity": 0.0,
        "number": 0.0,
        "energy": 0.0,
        "ground": 0.0,
        "branch": 0.0,
        "jump": 0.0,
        "lower": 0.0,
        "upper": 0.0,
    }
    initial_energy = float(np.trace(hamiltonian @ initial).real)
    subset_families = ((), tuple(range(m)), (0, 2))
    all_probabilities: list[float] = []
    all_particles: list[float] = []
    all_post_energies: list[float] = []
    all_ground_energies: list[float] = []
    for measured in subset_families:
        branch_energies: list[float] = []
        probability_sum = 0.0
        for outcomes in every_outcome(len(measured)):
            conditional, remaining, probability = condition_occupations(initial, measured, outcomes)
            unmeasured = tuple(index for index in range(m) if index not in set(measured))
            expected_remaining = unmeasured + tuple(range(m, 2 * m))
            if remaining != expected_remaining:
                raise RuntimeError("measurement output ordering changed")
            closed = closed_conditional_covariance(recovered_u, measured, outcomes)
            metrics["conditional"] = max(metrics["conditional"], float(np.linalg.norm(conditional - closed, ord="fro")))
            if measured:
                reverse_conditional, reverse_remaining, reverse_probability = condition_occupations(
                    initial, tuple(reversed(measured)), tuple(reversed(outcomes))
                )
                if reverse_remaining != remaining:
                    raise RuntimeError("measurement order changed the retained modes")
                metrics["order"] = max(
                    metrics["order"],
                    float(np.linalg.norm(conditional - reverse_conditional, ord="fro")),
                    abs(probability - reverse_probability),
                )
            target_probability = 2.0 ** (-len(measured))
            metrics["probability"] = max(metrics["probability"], abs(probability - target_probability))
            probability_sum += probability
            all_probabilities.append(probability)
            metrics["purity"] = max(
                metrics["purity"], float(np.linalg.norm(conditional @ conditional - conditional, ord="fro"))
            )
            target_number = m - sum(outcomes)
            all_particles.append(float(np.trace(conditional).real))
            metrics["number"] = max(metrics["number"], abs(float(np.trace(conditional).real) - target_number))

            q_t = q_matrix[np.array(unmeasured, dtype=int), :] if unmeasured else np.zeros((0, m), complex)
            h_reduced = reduced_hamiltonian(q_matrix, unmeasured)
            post_energy = float(np.trace(h_reduced @ conditional).real)
            branch_energies.append(post_energy)
            all_post_energies.append(post_energy)
            expected_post = -float(np.trace(recovered_k[np.ix_(unmeasured, unmeasured)]).real) if unmeasured else 0.0
            metrics["energy"] = max(metrics["energy"], abs(post_energy - expected_post))

            b_matrix = positive_sqrt(q_t @ q_t.conj().T) if unmeasured else np.zeros((0, 0), complex)
            ground_formula = -float(np.trace(b_matrix).real)
            particle_number = target_number
            direct_levels = np.linalg.eigvalsh(h_reduced)
            direct_ground = float(np.sum(np.sort(direct_levels)[:particle_number]).real)
            all_ground_energies.append(direct_ground)
            metrics["ground"] = max(metrics["ground"], abs(direct_ground - ground_formula))
            delta = post_energy - ground_formula
            local_jump = float(np.trace(recovered_k[np.ix_(measured, measured)]).real) if measured else 0.0
            metrics["jump"] = max(metrics["jump"], abs((post_energy - initial_energy) - local_jump))
            metrics["lower"] = max(metrics["lower"], max(0.0, -delta))
            metrics["upper"] = max(metrics["upper"], max(0.0, delta - local_jump))
        metrics["probability"] = max(metrics["probability"], abs(probability_sum - 1.0))
        metrics["branch"] = max(metrics["branch"], max(branch_energies) - min(branch_energies))

    projector_nonreducing = np.zeros((m, m), complex)
    projector_nonreducing[[0, 2], [0, 2]] = 1.0
    nonreducing_norm = float(np.linalg.norm(projector_nonreducing @ recovered_k - recovered_k @ projector_nonreducing))

    diagonal_k = np.diag([0.8, 1.3, 2.1, 3.4]).astype(complex)
    fourier = np.exp(2j * np.pi * np.outer(np.arange(m), np.arange(m)) / m) / np.sqrt(m)
    diagonal_q = diagonal_k @ fourier
    diagonal_h = bipartite_hamiltonian(diagonal_q)
    diagonal_initial, _ = negative_projector(diagonal_h)
    diagonal_s = (1,)
    diagonal_deltas: list[float] = []
    diagonal_jumps: list[float] = []
    for outcome in (0, 1):
        conditional, _, _ = condition_occupations(diagonal_initial, diagonal_s, (outcome,))
        unmeasured = tuple(index for index in range(m) if index not in diagonal_s)
        h_reduced = reduced_hamiltonian(diagonal_q, unmeasured)
        post = float(np.trace(h_reduced @ conditional).real)
        b_matrix = positive_sqrt(diagonal_q[np.array(unmeasured), :] @ diagonal_q[np.array(unmeasured), :].conj().T)
        ground = -float(np.trace(b_matrix).real)
        diagonal_deltas.append(post - ground)
        diagonal_jumps.append(post - float(np.trace(diagonal_h @ diagonal_initial).real))

    return GenericMetrics(
        initial_residual=metrics["initial"],
        conditional_residual=metrics["conditional"],
        order_residual=metrics["order"],
        probability_residual=metrics["probability"],
        purity_residual=metrics["purity"],
        number_residual=metrics["number"],
        energy_residual=metrics["energy"],
        ground_residual=metrics["ground"],
        branch_spread=metrics["branch"],
        jump_residual=metrics["jump"],
        lower_violation=metrics["lower"],
        upper_violation=metrics["upper"],
        nonreducing_norm=nonreducing_norm,
        unitary_residual=float(np.linalg.norm(recovered_u @ recovered_u.conj().T - np.eye(m))),
        imaginary_norm=float(np.linalg.norm(recovered_u.imag)),
        diagonal_delta=max(abs(value) for value in diagonal_deltas),
        diagonal_jump=min(diagonal_jumps),
        probability_range=(min(all_probabilities), max(all_probabilities)),
        particle_range=(max(0.0, min(all_particles)), max(all_particles)),
        post_energy_range=(min(all_post_energies), max(all_post_energies)),
        ground_energy_range=(min(all_ground_energies), max(all_ground_energies)),
    )


def lattice_index(coordinate: tuple[int, int, int], side: int) -> int:
    x, y, z = coordinate
    return (x * side + y) * side + z


@dataclass
class LatticeModel:
    side: int
    twist: int
    hamiltonian: np.ndarray
    q_matrix: np.ndarray
    max_degree_residual: float
    max_rownorm_residual: float
    plaquette_residual: float
    bipartite_residual: float


def staggered_cubic_model(side: int, hopping: float = 1.0) -> LatticeModel:
    if not isinstance(side, int) or side < 4 or side % 2:
        raise ValueError("side must be an even integer at least four")
    if side**3 > MAX_ONE_PARTICLE_SITES:
        raise ValueError("one-particle cubic carrier exceeds 512 sites")
    if not np.isfinite(hopping) or hopping <= 0.0:
        raise ValueError("hopping must be finite and positive")
    n_reduced = side // 2
    twist = (-1) ** (n_reduced + 1)
    dimension = side**3
    hamiltonian = np.zeros((dimension, dimension), dtype=float)
    for x in range(side):
        for y in range(side):
            for z in range(side):
                coordinate = (x, y, z)
                source = lattice_index(coordinate, side)
                for mu in range(3):
                    neighbor = [x, y, z]
                    wraps = neighbor[mu] == side - 1
                    neighbor[mu] = (neighbor[mu] + 1) % side
                    target = lattice_index(tuple(neighbor), side)
                    eta = (1, (-1) ** x, (-1) ** (x + y))[mu]
                    sign = eta * (twist if wraps else 1)
                    hamiltonian[source, target] = hopping * sign
                    hamiltonian[target, source] = hopping * sign

    a_sites = [
        lattice_index((x, y, z), side)
        for x in range(side)
        for y in range(side)
        for z in range(side)
        if (x + y + z) % 2 == 0
    ]
    a_set = set(a_sites)
    b_sites = [index for index in range(dimension) if index not in a_set]
    q_matrix = hamiltonian[np.ix_(a_sites, b_sites)]
    degree_residual = float(np.max(np.abs(np.count_nonzero(hamiltonian, axis=1) - 6)))
    rownorm_residual = float(np.max(np.abs(np.sum(hamiltonian**2, axis=1) - 6.0 * hopping**2)))
    plaquette_residual = 0.0
    for x in range(side):
        for y in range(side):
            for z in range(side):
                origin = (x, y, z)
                origin_index = lattice_index(origin, side)
                for mu, nu in ((0, 1), (0, 2), (1, 2)):
                    r_mu = list(origin)
                    r_nu = list(origin)
                    r_mu[mu] = (r_mu[mu] + 1) % side
                    r_nu[nu] = (r_nu[nu] + 1) % side
                    r_both = list(r_mu)
                    r_both[nu] = (r_both[nu] + 1) % side
                    product = (
                        hamiltonian[origin_index, lattice_index(tuple(r_mu), side)]
                        * hamiltonian[lattice_index(tuple(r_mu), side), lattice_index(tuple(r_both), side)]
                        * hamiltonian[lattice_index(tuple(r_both), side), lattice_index(tuple(r_nu), side)]
                        * hamiltonian[lattice_index(tuple(r_nu), side), origin_index]
                    ) / hopping**4
                    plaquette_residual = max(plaquette_residual, abs(product + 1.0))
    bipartite_residual = max(
        float(np.max(np.abs(hamiltonian[np.ix_(a_sites, a_sites)]))),
        float(np.max(np.abs(hamiltonian[np.ix_(b_sites, b_sites)]))),
    )
    return LatticeModel(
        side=side,
        twist=twist,
        hamiltonian=hamiltonian,
        q_matrix=q_matrix,
        max_degree_residual=degree_residual,
        max_rownorm_residual=rownorm_residual,
        plaquette_residual=plaquette_residual,
        bipartite_residual=bipartite_residual,
    )


def canonical_spectrum_lambdas(side: int) -> np.ndarray:
    n_reduced = side // 2
    momenta = (2 * np.arange(n_reduced) + 1) * np.pi / n_reduced
    values = [
        2.0 * sum(1.0 - np.cos(value) for value in (qx, qy, qz))
        for qx in momenta
        for qy in momenta
        for qz in momenta
    ]
    return np.asarray(values, dtype=float)


def scalar_momentum_lambdas(side: int) -> np.ndarray:
    """Independent sine-form implementation used only by scalar diagnostics."""

    n_reduced = side // 2
    momenta = (2 * np.arange(n_reduced) + 1) * np.pi / n_reduced
    values = [
        4.0 * sum(np.sin(value / 2.0) ** 2 for value in (qx, qy, qz))
        for qx in momenta
        for qy in momenta
        for qz in momenta
    ]
    return np.asarray(values, dtype=float)


def delta_quadrature(lambdas: np.ndarray, weights: np.ndarray) -> tuple[float, float]:
    lambdas = np.asarray(lambdas, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if lambdas.ndim != 1 or weights.shape != lambdas.shape or len(lambdas) == 0:
        raise ValueError("quadrature requires matching nonempty one-dimensional arrays")
    if not np.all(np.isfinite(lambdas)) or not np.all(np.isfinite(weights)):
        raise ValueError("quadrature spectrum and weights must be finite")
    if float(np.min(lambdas)) <= 0.0 or float(np.min(weights)) < 0.0:
        raise ValueError("quadrature spectrum must be positive with nonnegative weights")
    total_weight = float(np.sum(weights))
    if not np.isfinite(total_weight) or total_weight <= 0.0:
        raise ValueError("quadrature weights must have positive finite total")
    weights = weights / total_weight

    def integrand(x_value: float) -> float:
        resolvents = 1.0 / (x_value * x_value + lambdas)
        mean = float(weights @ resolvents)
        variance = float(weights @ ((resolvents - mean) ** 2))
        return (2.0 / np.pi) * x_value * x_value * variance / mean

    value, error = quad(integrand, 0.0, np.inf, epsabs=2.0e-11, epsrel=2.0e-11, limit=300)
    return float(value), float(error)


def l_quadrature(lambdas: np.ndarray, weights: np.ndarray) -> tuple[float, float]:
    lambdas = np.asarray(lambdas, dtype=float)
    weights = np.asarray(weights, dtype=float)
    if lambdas.ndim != 1 or weights.shape != lambdas.shape or len(lambdas) == 0:
        raise ValueError("L quadrature requires matching nonempty one-dimensional arrays")
    if not np.all(np.isfinite(lambdas)) or not np.all(np.isfinite(weights)):
        raise ValueError("L quadrature spectrum and weights must be finite")
    if float(np.min(lambdas)) <= 0.0 or float(np.min(weights)) < 0.0:
        raise ValueError("L quadrature spectrum must be positive with nonnegative weights")
    total_weight = float(np.sum(weights))
    if not np.isfinite(total_weight) or total_weight <= 0.0:
        raise ValueError("L quadrature weights must have positive finite total")
    weights = weights / total_weight

    def integrand(x_value: float) -> float:
        resolvents = 1.0 / (x_value * x_value + lambdas)
        g_value = float(weights @ resolvents)
        h2_value = float(weights @ (np.sqrt(lambdas) * resolvents**2))
        return (2.0 / np.pi) * h2_value / g_value

    integral, error = quad(integrand, 0.0, np.inf, epsabs=2.0e-11, epsrel=2.0e-11, limit=300)
    return -1.0 + float(integral), float(error)


def determinant_probability(ground_basis: np.ndarray, covariance: np.ndarray) -> float:
    restricted = ground_basis.conj().T @ covariance @ ground_basis
    eigenvalues = np.linalg.eigvalsh(0.5 * (restricted + restricted.conj().T))
    if float(np.min(eigenvalues)) < -2.0e-9 or float(np.max(eigenvalues)) > 1.0 + 2.0e-9:
        raise ValueError("restricted correlation matrix is outside [0,1]")
    return float(np.prod(np.clip(eigenvalues, 0.0, 1.0)))


@dataclass
class LatticeMetrics:
    side: int
    twist: int
    geometry_residual: float
    spectrum_residual: float
    gap: float
    gap_expected: float
    post_energy: float
    ground_energy: float
    delta: float
    jump: float
    branch_energy_spread: float
    direct_energy_residual: float
    delta_quadrature: float
    delta_quadrature_residual: float
    l_scalar: float
    l_integral_residual: float
    g0: float
    overlap_formula_residual: float
    overlap_definition_residual: float
    overlap_bound_violation: float
    g0_bound_violation: float
    min_overlap: float
    max_leakage: float
    positive_particles: tuple[float, float]
    negative_holes: tuple[float, float]
    zero_occupancies: tuple[float, float]
    overlaps: tuple[float, float]
    leakages: tuple[float, float]


def lattice_checks(side: int) -> LatticeMetrics:
    model = staggered_cubic_model(side)
    q_matrix = model.q_matrix.astype(complex)
    m = q_matrix.shape[0]
    block_h = bipartite_hamiltonian(q_matrix)
    initial, spectrum = negative_projector(block_h)
    k_matrix = positive_sqrt(q_matrix @ q_matrix.conj().T)
    unitary = np.linalg.solve(k_matrix, q_matrix)
    matrix_m = q_matrix @ q_matrix.conj().T
    m_values, m_vectors = np.linalg.eigh(matrix_m)
    scalar_values = canonical_spectrum_lambdas(side)
    expected_spectrum = np.repeat(scalar_values, 4)
    spectrum_residual = float(np.max(np.abs(np.sort(m_values) - np.sort(expected_spectrum))))
    gap = float(np.min(np.abs(spectrum)))
    gap_expected = float(2.0 * np.sqrt(3.0) * np.sin(np.pi / side))

    measured = (0,)
    unmeasured = tuple(range(1, m))
    h_reduced = reduced_hamiltonian(q_matrix, unmeasured)
    reduced_levels = np.linalg.eigvalsh(h_reduced)
    b_matrix = positive_sqrt(matrix_m[np.ix_(unmeasured, unmeasured)])
    post_formula = -float(np.trace(k_matrix[np.ix_(unmeasured, unmeasured)]).real)
    ground_formula = -float(np.trace(b_matrix).real)
    initial_energy = float(np.trace(block_h @ initial).real)
    branch_energies: list[float] = []
    direct_energy_residual = 0.0
    conditioned_by_outcome: dict[int, np.ndarray] = {}
    for outcome in (0, 1):
        conditional, remaining, probability = condition_occupations(initial, measured, (outcome,))
        expected_remaining = unmeasured + tuple(range(m, 2 * m))
        if remaining != expected_remaining or abs(probability - 0.5) > LINEAR_TOL:
            raise RuntimeError("singleton conditioning identity failed")
        conditioned_by_outcome[outcome] = conditional
        post_direct = float(np.trace(h_reduced @ conditional).real)
        branch_energies.append(post_direct)
        particle_number = m - outcome
        ground_direct = float(np.sum(np.sort(reduced_levels)[:particle_number]).real)
        direct_energy_residual = max(
            direct_energy_residual,
            abs(post_direct - post_formula),
            abs(ground_direct - ground_formula),
        )

    delta = post_formula - ground_formula
    jump = post_formula - initial_energy
    local_weights = np.abs(m_vectors[0, :]) ** 2
    delta_integral, _ = delta_quadrature(m_values, local_weights)

    a_matrix = k_matrix[np.ix_(unmeasured, unmeasured)]
    v_matrix = np.linalg.solve(b_matrix, q_matrix[np.array(unmeasured), :])
    identity_t = np.eye(m - 1)
    f_minus = np.vstack([identity_t, -v_matrix.conj().T]) / np.sqrt(2.0)
    f_plus = np.vstack([identity_t, v_matrix.conj().T]) / np.sqrt(2.0)
    p_minus = f_minus @ f_minus.conj().T
    p_plus = f_plus @ f_plus.conj().T
    e_i = np.zeros(m, dtype=complex)
    e_i[0] = 1.0
    k_inverse_i = np.linalg.solve(k_matrix, e_i)
    z_mode = unitary.conj().T @ k_inverse_i
    z_mode /= np.linalg.norm(z_mode)
    z_full = np.concatenate([np.zeros(m - 1, complex), z_mode])
    u_vector = unitary.conj().T @ e_i
    beta_direct = abs(np.vdot(z_mode, u_vector)) ** 2
    beta_scalar = abs(np.vdot(e_i, k_inverse_i)) ** 2 / float(np.vdot(k_inverse_i, k_inverse_i).real)
    beta = beta_scalar
    alpha = 1.0 - beta
    l_scalar = float((m - 1) - np.trace(np.linalg.solve(b_matrix, a_matrix)).real)
    l_integral, _ = l_quadrature(m_values, local_weights)
    g0 = float(np.sum(local_weights / m_values))
    overlap_formula_residual = max(
        abs(beta_direct - beta_scalar),
        float(np.linalg.norm(q_matrix[np.array(unmeasured), :] @ z_mode)),
        float(np.linalg.norm(v_matrix @ v_matrix.conj().T - identity_t, ord="fro")),
    )
    overlap_definition_residual = 0.0
    overlap_bound_violation = 0.0
    g0_bound_violation = 0.0
    overlaps: list[float] = []
    leakages: list[float] = []
    positive_counts: list[float] = []
    hole_counts: list[float] = []
    zero_counts: list[float] = []
    for outcome in (0, 1):
        conditional = conditioned_by_outcome[outcome]
        positive_particles = float(np.trace(p_plus @ conditional).real)
        negative_holes = float(np.trace(p_minus @ (np.eye(2 * m - 1) - conditional)).real)
        zero_occupancy = float(np.vdot(z_full, conditional @ z_full).real)
        expected_positive = l_scalar / 2.0 + (1.0 - 2.0 * outcome) * alpha / 4.0
        expected_holes = l_scalar / 2.0 - (1.0 - 2.0 * outcome) * alpha / 4.0
        expected_zero = 0.5 + (0.5 - outcome) * beta
        ell_expected = l_scalar / 2.0 + alpha / 4.0
        ground_basis = np.column_stack([f_minus, z_full]) if outcome == 0 else f_minus
        ground_projector = ground_basis @ ground_basis.conj().T
        leakage = float(np.trace(ground_projector @ (np.eye(2 * m - 1) - conditional)).real)
        frobenius_squared = float(np.linalg.norm(conditional - ground_projector, ord="fro") ** 2)
        overlap = determinant_probability(ground_basis, conditional)
        conditional_values, conditional_vectors = np.linalg.eigh(conditional)
        rank = m - outcome
        occupied_basis = conditional_vectors[:, np.argsort(conditional_values)[-rank:]]
        singular_values = np.linalg.svd(ground_basis.conj().T @ occupied_basis, compute_uv=False)
        overlap_from_orbitals = float(np.prod(singular_values**2))
        overlap_formula_residual = max(
            overlap_formula_residual,
            abs(positive_particles - expected_positive),
            abs(negative_holes - expected_holes),
            abs(zero_occupancy - expected_zero),
            abs(leakage - ell_expected),
            abs(frobenius_squared - 2.0 * leakage),
        )
        overlap_definition_residual = max(overlap_definition_residual, abs(overlap - overlap_from_orbitals))
        overlap_bound_violation = max(overlap_bound_violation, max(0.0, 1.0 - leakage - overlap))
        g0_bound_violation = max(g0_bound_violation, max(0.0, leakage - 1.5 * g0))
        overlaps.append(overlap)
        leakages.append(leakage)
        positive_counts.append(positive_particles)
        hole_counts.append(negative_holes)
        zero_counts.append(zero_occupancy)

    geometry_residual = max(
        model.max_degree_residual,
        model.max_rownorm_residual,
        model.plaquette_residual,
        model.bipartite_residual,
    )
    return LatticeMetrics(
        side=side,
        twist=model.twist,
        geometry_residual=geometry_residual,
        spectrum_residual=spectrum_residual,
        gap=gap,
        gap_expected=gap_expected,
        post_energy=post_formula,
        ground_energy=ground_formula,
        delta=delta,
        jump=jump,
        branch_energy_spread=max(branch_energies) - min(branch_energies),
        direct_energy_residual=direct_energy_residual,
        delta_quadrature=delta_integral,
        delta_quadrature_residual=abs(delta_integral - delta),
        l_scalar=l_scalar,
        l_integral_residual=abs(l_integral - l_scalar),
        g0=g0,
        overlap_formula_residual=overlap_formula_residual,
        overlap_definition_residual=overlap_definition_residual,
        overlap_bound_violation=overlap_bound_violation,
        g0_bound_violation=g0_bound_violation,
        min_overlap=min(overlaps),
        max_leakage=max(leakages),
        positive_particles=(positive_counts[0], positive_counts[1]),
        negative_holes=(hole_counts[0], hole_counts[1]),
        zero_occupancies=(zero_counts[0], zero_counts[1]),
        overlaps=(overlaps[0], overlaps[1]),
        leakages=(leakages[0], leakages[1]),
    )


@dataclass
class ScalarRow:
    side: int
    delta: float
    l_scalar: float
    g0: float
    ell_bound: float


def scalar_finite_size_checks(sides: tuple[int, ...]) -> tuple[list[ScalarRow], float]:
    rows: list[ScalarRow] = []
    max_identity_residual = 0.0
    for side in sides:
        lambdas_sine = scalar_momentum_lambdas(side)
        lambdas_cosine = canonical_spectrum_lambdas(side)
        max_identity_residual = max(
            max_identity_residual,
            float(np.max(np.abs(np.sort(lambdas_sine) - np.sort(lambdas_cosine)))),
        )
        weights = np.full(len(lambdas_sine), 1.0 / len(lambdas_sine))
        delta, _ = delta_quadrature(lambdas_sine, weights)
        l_scalar, _ = l_quadrature(lambdas_sine, weights)
        g0 = float(np.mean(1.0 / lambdas_sine))
        beta = float(np.mean(1.0 / np.sqrt(lambdas_sine)) ** 2 / g0)
        ell = l_scalar / 2.0 + (1.0 - beta) / 4.0
        max_identity_residual = max(
            max_identity_residual,
            max(0.0, -delta),
            max(0.0, -l_scalar),
            max(0.0, ell - 1.5 * g0),
        )
        rows.append(ScalarRow(side, delta, l_scalar, g0, 1.5 * g0))
    return rows, max_identity_residual


def max_rss_mib() -> float:
    usage = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    return usage / (1024.0**2) if sys.platform == "darwin" else usage / 1024.0


def display_value(value: float) -> float:
    """Suppress signed-zero display without changing any computed gate."""

    return 0.0 if abs(value) < 5.0e-13 else value


class Report:
    def __init__(self) -> None:
        self.lines: list[str] = []
        self.passes = 0
        self.failures = 0

    def gate(self, family: str, name: str, passed: bool, detail: str) -> None:
        if passed:
            self.passes += 1
            status = "PASS"
        else:
            self.failures += 1
            status = "FAIL"
        self.lines.append(f"{status} {family} {name}: {detail}")

    def finish(self) -> tuple[str, int]:
        # Fixed-point the displayed count because the digit count is part of stdout.
        estimated = 0
        while True:
            stdout_line = f"PASS G7 stdout envelope: chars={estimated} limit=6000"
            summary = f"TOTAL: PASS={self.passes + 1} FAIL={self.failures}"
            body = "\n".join(self.lines + [stdout_line, summary]) + "\n"
            new_estimated = len(body)
            if new_estimated == estimated:
                break
            estimated = new_estimated
        if estimated >= 6000:
            stdout_line = f"FAIL G7 stdout envelope: chars={estimated} limit=6000"
            summary = f"TOTAL: PASS={self.passes} FAIL={self.failures + 1}"
            body = "\n".join(self.lines + [stdout_line, summary]) + "\n"
            return body, self.failures + 1
        return body, self.failures


def domain_guard_checks() -> tuple[int, int]:
    accepted = 0
    bad_calls = (
        lambda: staggered_cubic_model(3),
        lambda: staggered_cubic_model(2),
        lambda: staggered_cubic_model(10),
        lambda: staggered_cubic_model(4, 0.0),
        lambda: validate_q(np.ones((2, 3))),
        lambda: condition_occupations(np.eye(2), (0,), (2,)),
        lambda: delta_quadrature(np.array([1.0, 2.0]), np.array([0.0, 0.0])),
        lambda: delta_quadrature(np.array([1.0, np.nan]), np.array([0.5, 0.5])),
        lambda: l_quadrature(np.array([1.0, 2.0]), np.array([0.0, 0.0])),
        lambda: l_quadrature(np.array([1.0, 2.0]), np.array([0.5, np.inf])),
    )
    for call in bad_calls:
        try:
            call()
        except ValueError:
            accepted += 1
    return accepted, len(bad_calls)


def main() -> int:
    started = time.perf_counter()
    report = Report()
    guards, expected_guards = domain_guard_checks()
    report.gate("G0", "constructor domains", guards == expected_guards, f"rejections={guards}/{expected_guards}")

    generic = generic_gaussian_checks()
    report.gate(
        "G1",
        "complex eigensea and polar comparator",
        max(generic.initial_residual, generic.unitary_residual) < LINEAR_TOL
        and generic.imaginary_norm > 0.2
        and generic.nonreducing_norm > 0.1,
        "max_res={:.3e} ImU={:.3f} nonreducing={:.3f}".format(
            max(generic.initial_residual, generic.unitary_residual),
            generic.imaginary_norm,
            generic.nonreducing_norm,
        ),
    )
    g1_residual = max(
        generic.conditional_residual,
        generic.order_residual,
        generic.probability_residual,
        generic.purity_residual,
        generic.number_residual,
    )
    report.gate(
        "G1",
        "all iterative occupation branches",
        g1_residual < LINEAR_TOL,
        f"max_res={g1_residual:.3e} subsets=empty/full/nonreducing outcomes=21",
    )
    report.lines.append(
        "DATA G1 p=[{:.6f},{:.6f}] N=[{:.1f},{:.1f}] Epost=[{:+.6f},{:+.6f}] Eground=[{:+.6f},{:+.6f}]".format(
            *generic.probability_range,
            *generic.particle_range,
            *generic.post_energy_range,
            *generic.ground_energy_range,
        )
    )

    g2_identity = max(
        generic.energy_residual,
        generic.ground_residual,
        generic.branch_spread,
        generic.jump_residual,
    )
    report.gate(
        "G2",
        "branch energy and fixed-N ground subtraction",
        g2_identity < LINEAR_TOL,
        f"max_res={g2_identity:.3e}",
    )
    g2_bound = max(generic.lower_violation, generic.upper_violation, generic.diagonal_delta)
    report.gate(
        "G2",
        "bounds and diagonal-K control",
        g2_bound < LINEAR_TOL and generic.diagonal_jump > 0.1,
        f"max_violation={g2_bound:.3e} diagonal_jump={generic.diagonal_jump:.6f} diagonal_delta={generic.diagonal_delta:.3e}",
    )

    lattice_rows = [lattice_checks(side) for side in (4, 6, 8)]
    max_geometry = max(row.geometry_residual for row in lattice_rows)
    report.gate(
        "G3",
        "staggered cubic geometry",
        max_geometry < LINEAR_TOL and [row.twist for row in lattice_rows] == [-1, 1, -1],
        f"max_res={max_geometry:.3e} boundary_twists={','.join(f'{row.twist:+d}' for row in lattice_rows)}",
    )
    max_spectral = max(
        max(row.spectrum_residual, abs(row.gap - row.gap_expected)) for row in lattice_rows
    )
    max_direct_energy = max(
        max(row.direct_energy_residual, row.branch_energy_spread) for row in lattice_rows
    )
    report.gate(
        "G3",
        "canonical spectra and direct deleted energies",
        max(max_spectral, max_direct_energy) < LINEAR_TOL,
        f"spectrum_max={max_spectral:.3e} energy_max={max_direct_energy:.3e}",
    )
    report.lines.append("DATA G3 L  gap       Epost        Eground      Delta       jump")
    for row in lattice_rows:
        report.lines.append(
            "DATA G3 {:d} {:.6f} {:+.6f} {:+.6f} {:.9f} {:.9f}".format(
                row.side, row.gap, row.post_energy, row.ground_energy, row.delta, row.jump
            )
        )

    max_delta_quad = max(row.delta_quadrature_residual for row in lattice_rows)
    report.gate(
        "G4",
        "singleton resolvent quadrature",
        max_delta_quad < QUAD_TOL,
        f"max_abs={max_delta_quad:.3e} values={','.join(f'{row.delta_quadrature:.9f}' for row in lattice_rows)}",
    )

    max_overlap_formula = max(row.overlap_formula_residual for row in lattice_rows)
    report.gate(
        "G5",
        "particles holes zero mode and leakage",
        max_overlap_formula < QUAD_TOL,
        f"max_res={max_overlap_formula:.3e}",
    )
    max_overlap_definition = max(row.overlap_definition_residual for row in lattice_rows)
    max_overlap_violation = max(
        max(row.overlap_bound_violation, row.g0_bound_violation) for row in lattice_rows
    )
    report.gate(
        "G5",
        "fixed-N Slater overlap and g0 bound",
        max(max_overlap_definition, max_overlap_violation) < QUAD_TOL,
        "definition_max={:.3e} bound_max={:.3e} minF={:.6f} maxell={:.6f}".format(
            max_overlap_definition,
            max_overlap_violation,
            min(row.min_overlap for row in lattice_rows),
            max(row.max_leakage for row in lattice_rows),
        ),
    )
    max_l_integral = max(row.l_integral_residual for row in lattice_rows)
    report.gate(
        "G5",
        "scalar integral for L",
        max_l_integral < QUAD_TOL,
        f"max_abs={max_l_integral:.3e} bound_source=g0_not_gap",
    )
    report.lines.append("DATA G5 L n  Nplus      Nholes     zero_occ   overlap    leakage")
    for row in lattice_rows:
        for outcome in (0, 1):
            report.lines.append(
                "DATA G5 {:d} {:d} {:.9f} {:.9f} {:.9f} {:.9f} {:.9f}".format(
                    row.side,
                    outcome,
                    display_value(row.positive_particles[outcome]),
                    display_value(row.negative_holes[outcome]),
                    display_value(row.zero_occupancies[outcome]),
                    display_value(row.overlaps[outcome]),
                    display_value(row.leakages[outcome]),
                )
            )

    scalar_rows, scalar_residual = scalar_finite_size_checks((4, 6, 8, 12, 16, 24, 32))
    actual_scalar_residual = max(
        abs(next(item.delta for item in scalar_rows if item.side == row.side) - row.delta)
        for row in lattice_rows
    )
    report.gate(
        "G6",
        "scalar momentum and finite-grid quadratures",
        max(scalar_residual, actual_scalar_residual) < QUAD_TOL,
        f"identity_max={scalar_residual:.3e} actual_max={actual_scalar_residual:.3e} diagnostic_only=no_limit_proof",
    )
    report.lines.append("DATA G6 L  Delta       Lscalar     g0")
    for row in scalar_rows:
        report.lines.append(f"DATA G6 {row.side:2d} {row.delta:.9f} {row.l_scalar:.9f} {row.g0:.9f}")

    elapsed = time.perf_counter() - started
    rss_mib = max_rss_mib()
    report.gate(
        "G7",
        "execution envelope",
        elapsed <= AUDIT_TIMEOUT_SEC and rss_mib < 200.0 and MAX_ONE_PARTICLE_SITES == 512,
        f"elapsed={elapsed:.2f}s timeout={AUDIT_TIMEOUT_SEC}s rss={rss_mib:.1f}MiB max_sites={MAX_ONE_PARTICLE_SITES}",
    )
    output, failures = report.finish()
    print(output, end="")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
