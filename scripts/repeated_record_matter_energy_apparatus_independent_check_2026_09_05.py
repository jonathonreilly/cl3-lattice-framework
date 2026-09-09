#!/usr/bin/env python3
"""Independent checker for repeated Record matter and a finite battery gate.

The checker uses direct fixed-number Fock matrices and a commensurate finite
spectral lift. It reads no science artifact or runner output. Its finite ladder
and Fourier-register fixtures are not a proof of a continuous battery bound,
and its normalized Choi trace distances are not diamond-norm bounds.
"""

import os

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import ast
import hashlib
import math
import sys
from itertools import combinations
from pathlib import Path

import numpy as np
from scipy import sparse
from scipy.integrate import quad, solve_ivp
from scipy.linalg import expm


AUDIT_TIMEOUT_SEC = 180
EXPECTED_FILENAME = "repeated_record_matter_energy_apparatus_independent_check_2026_09_05.py"
TOL = 3.0e-9
DENSE_MATRIX_LIMIT = 600
BATTERY_TOP = 12


class CheckFailure(RuntimeError):
    pass


def require(condition, message):
    if not bool(condition):
        raise CheckFailure(message)


def frobenius(value):
    if sparse.issparse(value):
        return float(sparse.linalg.norm(value))
    return float(np.linalg.norm(value))


def require_small(value, message, tolerance=TOL):
    residual = frobenius(value)
    if not residual < tolerance:
        raise CheckFailure(f"{message}; residual={residual:.6g}")


def certify_dense(*arrays):
    for array in arrays:
        require(not sparse.issparse(array), "dense-size audit received a sparse matrix")
        if getattr(array, "ndim", 0) == 2:
            require(max(array.shape) <= DENSE_MATRIX_LIMIT, f"dense matrix exceeds {DENSE_MATRIX_LIMIT}: {array.shape}")


def fixed_basis(modes, particles):
    return tuple(sum(1 << mode for mode in occupied) for occupied in combinations(range(modes), particles))


def annihilate(mask, mode):
    if not ((mask >> mode) & 1):
        return None
    sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
    return mask ^ (1 << mode), sign


def create(mask, mode):
    if (mask >> mode) & 1:
        return None
    sign = -1 if (mask & ((1 << mode) - 1)).bit_count() % 2 else 1
    return mask | (1 << mode), sign


def second_quantize(one_particle, basis):
    positions = {mask: index for index, mask in enumerate(basis)}
    result = np.zeros((len(basis), len(basis)), dtype=complex)
    for column, mask in enumerate(basis):
        for annihilation_mode in range(one_particle.shape[1]):
            first = annihilate(mask, annihilation_mode)
            if first is None:
                continue
            intermediate, first_sign = first
            for creation_mode in range(one_particle.shape[0]):
                coefficient = one_particle[creation_mode, annihilation_mode]
                if coefficient == 0:
                    continue
                second = create(intermediate, creation_mode)
                if second is None:
                    continue
                final, second_sign = second
                result[positions[final], column] += coefficient * first_sign * second_sign
    return result


def occupation_projector(basis, site, outcome):
    return np.diag([float(((mask >> site) & 1) == outcome) for mask in basis]).astype(complex)


def delete_sites(one_particle, recorded):
    retained = one_particle.copy()
    if recorded:
        indices = sorted(recorded)
        retained[indices, :] = 0.0
        retained[:, indices] = 0.0
    return retained


def incident_star(one_particle, site):
    star = np.zeros_like(one_particle)
    for other in range(one_particle.shape[0]):
        if other == site:
            continue
        star[site, other] = one_particle[site, other]
        star[other, site] = np.conjugate(one_particle[site, other])
    return star


def complex_hopping_fixture():
    hopping = np.array(
        [
            [0, 1 + 1j, 2, 0],
            [1 - 1j, 0, -1j, 1],
            [2, 1j, 0, 1 + 1j],
            [0, 1, 1 - 1j, 0],
        ],
        dtype=complex,
    )
    amplitudes = np.array([1, -1, 1 + 1j, 2, -1j, 1], dtype=complex)
    amplitudes /= np.linalg.norm(amplitudes)
    require_small(hopping - hopping.conj().T, "complex hopping fixture is not Hermitian")
    require_small(np.diag(np.diag(hopping)), "complex hopping fixture has onsite terms")
    return hopping, amplitudes


def trace_real(density, observable):
    value = np.trace(density @ observable)
    require(abs(value.imag) < 2.0e-9, "Hermitian expectation acquired an imaginary part")
    return float(value.real)


def selective_event(density, one_particle, basis, site):
    old_hamiltonian = second_quantize(one_particle, basis)
    one_star = incident_star(one_particle, site)
    star = second_quantize(one_star, basis)
    retained_one = one_particle - one_star
    retained = second_quantize(retained_one, basis)
    require_small(old_hamiltonian - retained - star, "event star decomposition failed")
    before = trace_real(density, old_hamiltonian)
    retained_mean = trace_real(density, retained)
    star_mean = trace_real(density, star)
    branches = {}
    weighted_after = 0.0
    for outcome in (0, 1):
        projector = occupation_projector(basis, site, outcome)
        probability = trace_real(density, projector)
        require_small(projector @ retained - retained @ projector, "retained Hamiltonian changes measured occupation")
        require_small(projector @ star @ projector, "star has a diagonal occupation block")
        if probability < 1.0e-13:
            continue
        branch = projector @ density @ projector / probability
        energy = trace_real(branch, retained)
        covariance = trace_real(density, (projector - probability * np.eye(len(basis))) @ retained)
        predicted = retained_mean + covariance / probability
        jump = energy - before
        predicted_jump = -star_mean + covariance / probability
        require(abs(energy - predicted) < TOL, f"conditional selection formula failed n={outcome}")
        require(abs(jump - predicted_jump) < TOL, f"signed branch jump failed n={outcome}")
        require(abs(trace_real(branch, star)) < TOL, f"projected star expectation survives n={outcome}")
        require(abs(np.trace(branch) - 1.0) < TOL, f"branch normalization failed n={outcome}")
        branches[outcome] = {
            "probability": probability,
            "density": branch,
            "energy": energy,
            "covariance": covariance,
        }
        weighted_after += probability * energy
    require(abs(sum(item["probability"] for item in branches.values()) - 1.0) < TOL, "Born probabilities do not normalize")
    require(abs(weighted_after - retained_mean) < TOL, "selective energies do not average to retained energy")
    require(abs(weighted_after - before + star_mean) < TOL, "unconditional signed jump is wrong")
    return retained_one, branches, before, weighted_after, star_mean


def check_fixed_number_process():
    one_particle, state = complex_hopping_fixture()
    basis = fixed_basis(4, 2)
    density = np.outer(state, state.conj())
    full_hamiltonian = second_quantize(one_particle, basis)
    dwell = expm(-0.317j * full_hamiltonian)
    pre_first = dwell @ density @ dwell.conj().T
    retained_one, first, before, after, first_star = selective_event(pre_first, one_particle, basis, 0)
    first_covariances = [abs(item["covariance"]) for item in first.values()]
    require(max(first_covariances) > 1.0e-3 and abs(first_star) > 1.0e-3, "first event is selection-degenerate")

    retained_hamiltonian = second_quantize(retained_one, basis)
    second_dwell = expm(-0.229j * retained_hamiltonian)
    joint = {}
    final_energies = {}
    recursively_before = 0.0
    recursively_after = 0.0
    recursively_star = 0.0
    for first_outcome, first_item in first.items():
        evolved = second_dwell @ first_item["density"] @ second_dwell.conj().T
        require(abs(trace_real(evolved, retained_hamiltonian) - first_item["energy"]) < TOL, "dwell changed branch energy")
        twice_retained, second, second_before, second_after, second_star = selective_event(
            evolved, retained_one, basis, 2
        )
        recursively_before += first_item["probability"] * second_before
        recursively_after += first_item["probability"] * second_after
        recursively_star += first_item["probability"] * second_star
        require_small(twice_retained[[0, 2], :], "recorded rows are not frozen")
        require_small(twice_retained[:, [0, 2]], "recorded columns are not frozen")
        for second_outcome, second_item in second.items():
            path = (first_outcome, second_outcome)
            path_probability = first_item["probability"] * second_item["probability"]
            require(path_probability > 1.0e-5, f"two-event path {path} has zero probability")
            joint[path] = path_probability
            final_energies[path] = second_item["energy"]
    require(abs(sum(joint.values()) - 1.0) < TOL, "two-event probabilities do not normalize")
    require(abs(recursively_after - recursively_before + recursively_star) < TOL, "second-event ensemble ledger failed")
    require(max(final_energies.values()) - min(final_energies.values()) > 0.1, "two-event energies are branch independent")
    return (
        f"E0={before:.9f} E1mean={after:.9f} <V0>={first_star:.9f} "
        f"paths={','.join(f'{a}{b}:{joint[(a,b)]:.6f}' for a,b in sorted(joint))} "
        f"spreadE2={max(final_energies.values())-min(final_energies.values()):.9f}"
    )


def record_hamiltonians(one_particle, basis):
    return {
        recorded: second_quantize(
            delete_sites(one_particle, {site for site in range(4) if (recorded >> site) & 1}),
            basis,
        )
        for recorded in range(16)
    }


def pinching(density, projectors):
    return sum((projector @ density @ projector for projector in projectors), np.zeros_like(density))


def check_uniform_and_clock_laws():
    one_particle, state = complex_hopping_fixture()
    basis = fixed_basis(4, 2)
    density = np.outer(state, state.conj())
    hamiltonians = record_hamiltonians(one_particle, basis)
    projectors = {
        site: tuple(occupation_projector(basis, site, outcome) for outcome in (0, 1))
        for site in range(4)
    }
    initial_energy = trace_real(density, hamiltonians[0])
    blocks = {0: density}
    event_energies = []
    live_particle_means = []
    maximum_hypergeometric_error = 0.0
    for event_count in range(5):
        energy = sum(trace_real(block, hamiltonians[recorded]) for recorded, block in blocks.items())
        live_particles = sum(
            trace_real(
                block,
                sum(
                    (
                        occupation_projector(basis, site, 1)
                        for site in range(4)
                        if not ((recorded >> site) & 1)
                    ),
                    np.zeros_like(block),
                ),
            )
            for recorded, block in blocks.items()
        )
        pair_fraction = (
            (4 - event_count) * (3 - event_count) / 12.0 if event_count < 4 else 0.0
        )
        require(abs(energy - initial_energy * pair_fraction) < 5.0e-9, f"uniform-site mean failed k={event_count}")
        require(
            abs(live_particles - 2.0 * (4 - event_count) / 4.0) < 5.0e-9,
            f"uniform-site live-particle recursion failed k={event_count}",
        )
        live_size = 4 - event_count
        denominator = math.comb(4, live_size)
        for remaining_particles in range(3):
            actual_probability = 0.0
            for recorded, block in blocks.items():
                live_sites = tuple(site for site in range(4) if not ((recorded >> site) & 1))
                count_projector = np.diag(
                    [
                        float(
                            sum((mask >> site) & 1 for site in live_sites)
                            == remaining_particles
                        )
                        for mask in basis
                    ]
                ).astype(complex)
                actual_probability += trace_real(block, count_projector)
            particle_choices = (
                math.comb(2, remaining_particles)
                if 0 <= remaining_particles <= 2
                else 0
            )
            hole_count = live_size - remaining_particles
            hole_choices = math.comb(2, hole_count) if 0 <= hole_count <= 2 else 0
            expected_probability = particle_choices * hole_choices / denominator
            distribution_error = abs(actual_probability - expected_probability)
            require(
                distribution_error < 5.0e-9,
                f"live-number hypergeometric law failed k={event_count} r={remaining_particles}",
            )
            maximum_hypergeometric_error = max(
                maximum_hypergeometric_error,
                distribution_error,
            )
        event_energies.append(energy)
        live_particle_means.append(live_particles)
        if event_count == 4:
            break
        live_count = 4 - event_count
        successors = {}
        for recorded, block in blocks.items():
            current_hamiltonian = hamiltonians[recorded]
            dwell_time = 0.101 + 0.037 * recorded + 0.053 * event_count
            dwell = expm(-1j * dwell_time * current_hamiltonian)
            evolved = dwell @ block @ dwell.conj().T
            for site in range(4):
                if (recorded >> site) & 1:
                    continue
                successor = recorded | (1 << site)
                contribution = pinching(evolved, projectors[site]) / live_count
                successors[successor] = successors.get(successor, np.zeros_like(block)) + contribution
        blocks = successors
        require(abs(sum(np.trace(block).real for block in blocks.values()) - 1.0) < TOL, "uniform event blocks lost probability")

    gamma = 0.63
    final_time = 0.79
    dimension = len(basis)
    initial_blocks = np.zeros((16, dimension, dimension), dtype=complex)
    initial_blocks[0] = density

    def generator(_time, flat):
        current = flat.reshape((16, dimension, dimension))
        derivative = np.zeros_like(current)
        for recorded in range(16):
            live_count = 4 - recorded.bit_count()
            hamiltonian = hamiltonians[recorded]
            derivative[recorded] += -1j * (hamiltonian @ current[recorded] - current[recorded] @ hamiltonian)
            derivative[recorded] -= gamma * live_count * current[recorded]
            for site in range(4):
                if not ((recorded >> site) & 1):
                    continue
                predecessor = recorded ^ (1 << site)
                derivative[recorded] += gamma * pinching(current[predecessor], projectors[site])
        return derivative.reshape(-1)

    solution = solve_ivp(
        generator,
        (0.0, final_time),
        initial_blocks.reshape(-1),
        method="DOP853",
        rtol=2.0e-11,
        atol=2.0e-12,
    )
    require(solution.success, "hybrid Record generator integration failed")
    final_blocks = solution.y[:, -1].reshape((16, dimension, dimension))
    probability = sum(np.trace(block).real for block in final_blocks)
    require(abs(probability - 1.0) < 3.0e-10, "hybrid generator lost probability")
    actual_energy = sum(trace_real(final_blocks[recorded], hamiltonians[recorded]) for recorded in range(16))
    expected_energy = initial_energy * math.exp(-2.0 * gamma * final_time)
    require(abs(actual_energy - expected_energy) < 5.0e-9, "constant-clock exponential energy law failed")
    survival = math.exp(-gamma * final_time)
    maximum_record_error = max(
        abs(
            np.trace(final_blocks[recorded]).real
            - survival ** (4 - recorded.bit_count()) * (1.0 - survival) ** recorded.bit_count()
        )
        for recorded in range(16)
    )
    require(maximum_record_error < 4.0e-10, "independent-clock Record probabilities failed")
    return (
        f"Ek={','.join(f'{value:.6f}' for value in event_energies)} "
        f"Nlive={','.join(f'{value:.6f}' for value in live_particle_means)} "
        f"NhypErr={maximum_hypergeometric_error:.2e} "
        f"gamma={gamma} t={final_time} Et={actual_energy:.9f} target={expected_energy:.9f}"
    )


def fibre_event_operators(one_particle, basis, live_sites, selected_site, dwell_time):
    H_in = second_quantize(one_particle, basis)
    retained_one = delete_sites(one_particle, {selected_site})
    H_retained = second_quantize(retained_one, basis)
    projectors = tuple(occupation_projector(basis, selected_site, outcome) for outcome in (0, 1))
    W = local_record_isometry(projectors)
    H_out = np.kron(np.eye(2), H_retained)
    N_out_matter = sum(
        (
            occupation_projector(basis, site, 1)
            for site in live_sites
            if site != selected_site
        ),
        np.zeros_like(H_in),
    )
    N_out = np.kron(np.eye(2), N_out_matter)
    occupied_record = np.kron(np.diag([0.0, 1.0]), np.eye(len(basis)))
    fibre = expm(-1j * dwell_time * H_out) @ W @ expm(1j * dwell_time * H_in)
    require_small(fibre.conj().T @ fibre - np.eye(len(basis)), "event fibre is not isometric")
    require_small(H_out - H_out.conj().T, "fibre output energy is not Hermitian")
    require_small(N_out - N_out.conj().T, "fibre live number is not Hermitian")
    require_small(occupied_record @ H_out - H_out @ occupied_record,
                  "new Record outcome does not commute with output energy")
    return fibre, H_out, N_out, occupied_record


def check_uniform_fibre_operator_identities():
    original_one, _state = complex_hopping_fixture()
    basis = fixed_basis(4, 2)
    history_masks = (0b0000, 0b0001, 0b0101)
    dwell_times = (0.137, 0.491, 1.031)
    maximum_energy_residual = 0.0
    maximum_second_residual = 0.0
    maximum_number_residual = 0.0
    maximum_outcome_residual = 0.0
    cases = 0
    for recorded in history_masks:
        live_sites = tuple(site for site in range(4) if not ((recorded >> site) & 1))
        live_count = len(live_sites)
        current_one = delete_sites(
            original_one,
            {site for site in range(4) if (recorded >> site) & 1},
        )
        H_current = second_quantize(current_one, basis)
        N_current = sum(
            (occupation_projector(basis, site, 1) for site in live_sites),
            np.zeros_like(H_current),
        )
        star_sum = sum(
            (second_quantize(incident_star(current_one, site), basis) for site in live_sites),
            np.zeros_like(H_current),
        )
        require_small(star_sum - 2.0 * H_current, "live incident stars do not sum to twice H_R")
        require_small(H_current @ N_current - N_current @ H_current,
                      "current hopping does not preserve live particle number")
        for dwell_time in dwell_times:
            energy_average = np.zeros_like(H_current)
            second_average = np.zeros_like(H_current)
            second_correction = np.zeros_like(H_current)
            number_average = np.zeros_like(N_current)
            occupied_average = np.zeros_like(N_current)
            for selected_site in live_sites:
                fibre, H_out, N_out, occupied_record = fibre_event_operators(
                    current_one,
                    basis,
                    live_sites,
                    selected_site,
                    dwell_time,
                )
                energy_average += fibre.conj().T @ H_out @ fibre / live_count
                second_average += fibre.conj().T @ H_out @ H_out @ fibre / live_count
                number_average += fibre.conj().T @ N_out @ fibre / live_count
                occupied_average += fibre.conj().T @ occupied_record @ fibre / live_count
                V_selected = second_quantize(incident_star(current_one, selected_site), basis)
                kappa_squared = float(np.sum(np.abs(current_one[selected_site, :]) ** 2))
                require(
                    float(np.max(np.linalg.eigvalsh(V_selected @ V_selected)))
                    <= kappa_squared + 2.0e-8,
                    "star square exceeds its one-particle row-norm bound",
                )
                input_phase = expm(-1j * dwell_time * H_current)
                second_correction += (
                    input_phase @ V_selected @ V_selected @ input_phase.conj().T / live_count
                )
            energy_target = (1.0 - 2.0 / live_count) * H_current
            second_target = (
                (1.0 - 4.0 / live_count) * (H_current @ H_current)
                + second_correction
            )
            number_target = (1.0 - 1.0 / live_count) * N_current
            occupied_target = N_current / live_count
            energy_residual = frobenius(energy_average - energy_target)
            second_residual = frobenius(second_average - second_target)
            number_residual = frobenius(number_average - number_target)
            outcome_residual = frobenius(occupied_average - occupied_target)
            require(energy_residual < 2.0e-8,
                    f"uniform fibre energy identity failed R={recorded:04b} tau={dwell_time}")
            require(second_residual < 2.0e-8,
                    f"uniform fibre second-moment identity failed R={recorded:04b} tau={dwell_time}")
            require(number_residual < 2.0e-8,
                    f"uniform fibre live-number identity failed R={recorded:04b} tau={dwell_time}")
            require(outcome_residual < 2.0e-8,
                    f"uniform occupied-outcome effect failed R={recorded:04b} tau={dwell_time}")
            maximum_energy_residual = max(maximum_energy_residual, energy_residual)
            maximum_second_residual = max(maximum_second_residual, second_residual)
            maximum_number_residual = max(maximum_number_residual, number_residual)
            maximum_outcome_residual = max(maximum_outcome_residual, outcome_residual)
            cases += 1

    recorded = 0b0001
    live_sites = tuple(site for site in range(4) if not ((recorded >> site) & 1))
    live_count = len(live_sites)
    current_one = delete_sites(original_one, {0})
    H_current = second_quantize(current_one, basis)
    N_current = sum(
        (occupation_projector(basis, site, 1) for site in live_sites),
        np.zeros_like(H_current),
    )
    phase_points = (0.113, 0.379, 0.941)
    base_dwell = 0.227
    lifted_energy_average = np.zeros((len(phase_points) * len(basis),) * 2, dtype=complex)
    lifted_second_average = np.zeros_like(lifted_energy_average)
    lifted_second_correction = np.zeros_like(lifted_energy_average)
    lifted_number_average = np.zeros_like(lifted_energy_average)
    lifted_occupied_average = np.zeros_like(lifted_energy_average)
    for selected_site in live_sites:
        fibres = []
        output_energies = []
        output_numbers = []
        occupied_records = []
        second_corrections = []
        V_selected = second_quantize(incident_star(current_one, selected_site), basis)
        for phase in phase_points:
            fibre, H_out, N_out, occupied_record = fibre_event_operators(
                current_one,
                basis,
                live_sites,
                selected_site,
                base_dwell + phase,
            )
            fibres.append(fibre)
            output_energies.append(H_out)
            output_numbers.append(N_out)
            occupied_records.append(occupied_record)
            input_phase = expm(-1j * (base_dwell + phase) * H_current)
            second_corrections.append(
                input_phase @ V_selected @ V_selected @ input_phase.conj().T
            )
        lifted_fibre = sparse.block_diag(fibres, format="csr").toarray()
        lifted_H_out = sparse.block_diag(output_energies, format="csr").toarray()
        lifted_N_out = sparse.block_diag(output_numbers, format="csr").toarray()
        lifted_occupied = sparse.block_diag(occupied_records, format="csr").toarray()
        lifted_correction = sparse.block_diag(second_corrections, format="csr").toarray()
        certify_dense(lifted_fibre, lifted_H_out, lifted_N_out, lifted_occupied, lifted_correction)
        lifted_energy_average += lifted_fibre.conj().T @ lifted_H_out @ lifted_fibre / live_count
        lifted_second_average += (
            lifted_fibre.conj().T @ lifted_H_out @ lifted_H_out @ lifted_fibre / live_count
        )
        lifted_second_correction += lifted_correction / live_count
        lifted_number_average += lifted_fibre.conj().T @ lifted_N_out @ lifted_fibre / live_count
        lifted_occupied_average += (
            lifted_fibre.conj().T @ lifted_occupied @ lifted_fibre / live_count
        )
    lifted_energy_target = np.kron(
        np.eye(len(phase_points)),
        (1.0 - 2.0 / live_count) * H_current,
    )
    lifted_number_target = np.kron(
        np.eye(len(phase_points)),
        (1.0 - 1.0 / live_count) * N_current,
    )
    lifted_second_target = (
        np.kron(
            np.eye(len(phase_points)),
            (1.0 - 4.0 / live_count) * (H_current @ H_current),
        )
        + lifted_second_correction
    )
    lifted_occupied_target = np.kron(
        np.eye(len(phase_points)),
        N_current / live_count,
    )
    require_small(lifted_energy_average - lifted_energy_target,
                  "finite Fourier-register energy identity failed", 2.0e-8)
    require_small(lifted_second_average - lifted_second_target,
                  "finite Fourier-register second-moment identity failed", 2.0e-8)
    require_small(lifted_number_average - lifted_number_target,
                  "finite Fourier-register live-number identity failed", 2.0e-8)
    require_small(lifted_occupied_average - lifted_occupied_target,
                  "finite Fourier-register occupied-outcome identity failed", 2.0e-8)

    correlated_amplitudes = np.array(
        [
            [1, 1j, 0, 2, 0, -1],
            [0, 1 + 1j, 2j, 0, -2, 1],
            [1 - 1j, 0, 1, -1j, 2, 0],
        ],
        dtype=complex,
    )
    correlated_amplitudes /= np.linalg.norm(correlated_amplitudes)
    phase_reduced = correlated_amplitudes @ correlated_amplitudes.conj().T
    phase_purity = float(np.trace(phase_reduced @ phase_reduced).real)
    require(phase_purity < 0.8, "finite Fourier-register witness is not correlated")
    correlated_state = correlated_amplitudes.reshape(-1)
    actual_energy = float(np.vdot(correlated_state, lifted_energy_average @ correlated_state).real)
    target_energy = float(np.vdot(correlated_state, lifted_energy_target @ correlated_state).real)
    actual_number = float(np.vdot(correlated_state, lifted_number_average @ correlated_state).real)
    target_number = float(np.vdot(correlated_state, lifted_number_target @ correlated_state).real)
    actual_second = float(np.vdot(correlated_state, lifted_second_average @ correlated_state).real)
    target_second = float(np.vdot(correlated_state, lifted_second_target @ correlated_state).real)
    require(abs(actual_energy - target_energy) < TOL,
            "correlated Fourier-register energy expectation failed")
    require(abs(actual_number - target_number) < TOL,
            "correlated Fourier-register live-number expectation failed")
    require(abs(actual_second - target_second) < TOL,
            "correlated Fourier-register second-moment expectation failed")
    return (
        f"histories={','.join(f'{mask:04b}' for mask in history_masks)} "
        f"taus={','.join(f'{value:.3f}' for value in dwell_times)} cases={cases} "
        f"maxResidual(E={maximum_energy_residual:.2e},H2={maximum_second_residual:.2e},"
        f"N={maximum_number_residual:.2e},n1={maximum_outcome_residual:.2e}) "
        f"FourierPurity={phase_purity:.9f} "
        f"correlated(E={actual_energy:.9f},H2={actual_second:.9f},N={actual_number:.9f})"
    )


def local_record_isometry(projectors):
    return np.vstack(projectors)


def check_local_defects():
    one_particle, _state = complex_hopping_fixture()
    basis = fixed_basis(4, 2)
    site = 0
    one_star = incident_star(one_particle, site)
    retained_one = one_particle - one_star
    H_in = second_quantize(one_particle, basis)
    V = second_quantize(one_star, basis)
    H_retained = second_quantize(retained_one, basis)
    projectors = tuple(occupation_projector(basis, site, outcome) for outcome in (0, 1))
    W = local_record_isometry(projectors)
    H_out = sparse.block_diag((H_retained, H_retained), format="csr").toarray()
    defect = H_out @ W - W @ H_in
    require_small(defect + W @ V, "local defect sign D=-WV failed")
    kappa = float(np.linalg.norm(defect, ord=2))
    one_kappa = math.sqrt(float(np.sum(np.abs(one_particle[site, :]) ** 2)))
    require(abs(kappa - one_kappa) < TOL, "defect norm differs from one-particle star radius")
    require(abs(float(np.linalg.norm(V, ord=2)) - one_kappa) < TOL, "fixed-N star norm differs from radius")
    full_sector_norms = []
    for particles in range(5):
        sector_basis = fixed_basis(4, particles)
        sector_star = second_quantize(one_star, sector_basis)
        full_sector_norms.append(float(np.linalg.norm(sector_star, ord=2)))
    require(abs(max(full_sector_norms) - one_kappa) < TOL, "full-Fock star norm differs from radius")

    K2 = H_out @ defect - defect @ H_in
    commutator = V @ H_in - H_in @ V
    require_small(K2 - W @ (V @ V + commutator), "K2 identity failed")
    q = one_particle[:, site].copy()
    q[site] = 0.0
    r = retained_one @ q
    rank_two = np.zeros_like(one_particle)
    rank_two[site, :] = np.conjugate(r)
    rank_two[:, site] -= r
    one_commutator = one_star @ retained_one - retained_one @ one_star
    require_small(one_commutator - rank_two, "rank-two one-particle commutator formula failed")
    require(np.linalg.matrix_rank(one_commutator, tol=1.0e-10) == 2, "one-particle commutator is not rank two")
    commutator_norm = float(np.linalg.norm(commutator, ord=2))
    r_norm = float(np.linalg.norm(r))
    require(abs(commutator_norm - r_norm) < TOL, "many-body commutator norm differs from ||r||")
    maximum_hopping = float(np.max(np.abs(one_particle)))
    require(r_norm <= 6.0 * maximum_hopping * kappa + TOL, "degree-six commutator bound failed")
    C_value = (float(np.linalg.norm(K2, ord=2)) + kappa**2) / 2.0
    require(C_value <= kappa**2 + 3.0 * maximum_hopping * kappa + TOL, "local C bound failed")
    C_maximum = (6.0 + 3.0 * math.sqrt(6.0)) * maximum_hopping**2
    require(C_value <= C_maximum + TOL, "uniform Cmax bound failed")
    return (
        f"kappa={kappa:.9f} sectors={','.join(f'{value:.6f}' for value in full_sector_norms)} "
        f"||r||={r_norm:.9f} ||K2||={np.linalg.norm(K2,ord=2):.9f} C={C_value:.9f}"
    )


def pi_flux_one_particle():
    hopping = np.zeros((4, 4), dtype=complex)
    for left, right, amplitude in ((0, 1, 1.0), (1, 2, 1.0), (2, 3, 1.0), (3, 0, -1.0)):
        hopping[left, right] = amplitude
        hopping[right, left] = amplitude
    return hopping


def spectral_projectors(hamiltonian, labels, spacing):
    identity = np.eye(hamiltonian.shape[0], dtype=complex)
    scaled = hamiltonian / spacing
    projectors = {}
    for label in labels:
        projector = identity.copy()
        for other in labels:
            if other != label:
                projector = projector @ (scaled - other * identity) / (label - other)
        projector = (projector + projector.conj().T) / 2.0
        require_small(projector @ projector - projector, f"energy projector {label} is not idempotent")
        require_small(hamiltonian @ projector - spacing * label * projector, f"energy projector {label} is mistyped")
        projectors[label] = projector
    require_small(sum(projectors.values()) - identity, "energy projectors are incomplete")
    return projectors


def frequency_groups(W, H_in, input_labels, H_out, output_labels, spacing):
    input_projectors = spectral_projectors(H_in, input_labels, spacing)
    output_projectors = spectral_projectors(H_out, output_labels, spacing)
    groups = {}
    for input_label, input_projector in input_projectors.items():
        for output_label, output_projector in output_projectors.items():
            frequency = input_label - output_label
            term = output_projector @ W @ input_projector
            groups[frequency] = groups.get(frequency, np.zeros_like(W)) + term
    groups = {frequency: term for frequency, term in groups.items() if frobenius(term) > 1.0e-11}
    require_small(sum(groups.values()) - W, "frequency groups do not reconstruct W")
    for frequency, term in groups.items():
        require_small(H_out @ term - term @ H_in + spacing * frequency * term,
                      f"frequency group q={frequency} has the wrong sign")
    return groups


def finite_shift(length, amount):
    rows = []
    columns = []
    for column in range(length):
        row = column + amount
        if 0 <= row < length:
            rows.append(row)
            columns.append(column)
    return sparse.csr_matrix(
        (np.ones(len(rows), dtype=complex), (rows, columns)),
        shape=(length, length),
    )


def capped_lift(groups, length):
    terms = []
    for frequency, term in sorted(groups.items()):
        shift_amount = frequency
        terms.append(sparse.kron(sparse.csr_matrix(term), finite_shift(length, shift_amount), format="csr"))
    rows = next(iter(groups.values())).shape[0] * length
    columns = next(iter(groups.values())).shape[1] * length
    return sum(terms, sparse.csr_matrix((rows, columns), dtype=complex))


def total_hamiltonian(system_hamiltonian, spacing, length):
    battery = np.diag(spacing * np.arange(length, dtype=float))
    result = np.kron(system_hamiltonian, np.eye(length)) + np.kron(np.eye(system_hamiltonian.shape[0]), battery)
    certify_dense(result)
    return result


def refusal_gate(S, H_in_total, H_out_total):
    source_dimension = S.shape[1]
    success_dimension = S.shape[0]
    gram = (S.conj().T @ S).toarray()
    loss = np.eye(source_dimension) - gram
    loss = (loss + loss.conj().T) / 2.0
    require_small(loss @ loss - loss, "cap loss is not a projector in this fixture")
    F = loss
    require_small(F @ F + gram - np.eye(source_dimension), "refusal square root identity failed")
    require_small(F @ H_in_total - H_in_total @ F, "refusal does not commute with energy")
    zero_source = sparse.csr_matrix((source_dimension, source_dimension), dtype=complex)
    zero_source_success = sparse.csr_matrix((source_dimension, success_dimension), dtype=complex)
    zero_success_source = sparse.csr_matrix((success_dimension, source_dimension), dtype=complex)
    zero_success = sparse.csr_matrix((success_dimension, success_dimension), dtype=complex)
    J = sparse.bmat(
        [
            [zero_source, zero_source_success, zero_source],
            [S, zero_success, zero_success_source],
            [sparse.csr_matrix(F), zero_source_success, zero_source],
        ],
        format="csr",
    )
    total_dimension = 2 * source_dimension + success_dimension
    P_ready = sparse.diags(
        np.concatenate((np.ones(source_dimension), np.zeros(success_dimension + source_dimension))),
        format="csr",
    )
    Q_destination = (J @ J.conj().T).tocsr()
    identity = sparse.eye(total_dimension, dtype=complex, format="csr")
    U = (J + J.conj().T + identity - P_ready - Q_destination).tocsr()
    global_hamiltonian = sparse.block_diag((H_in_total, H_out_total, H_in_total), format="csr")
    require_small(J.conj().T @ J - P_ready, "J is not isometric on ready inputs")
    require_small(P_ready @ Q_destination, "ready and destination flags overlap")
    require_small(U.conj().T @ U - identity, "swap extension is not unitary", 1.0e-8)
    require_small(U @ U - identity, "swap extension is not involutive", 1.0e-8)
    require_small(global_hamiltonian @ U - U @ global_hamiltonian,
                  "swap extension does not conserve energy", 1.0e-8)
    require(U.shape[0] <= 700 and sparse.issparse(U), "swap gate violates sparse-size contract")
    return {
        "S": S,
        "F": F,
        "J": J,
        "U": U,
        "H_in_total": H_in_total,
        "H_out_total": H_out_total,
        "source_dimension": source_dimension,
        "success_dimension": success_dimension,
    }


def discrete_sine(length, width):
    require(width <= length - 4, "sine packet lacks two-level cap margin")
    start = (length - width) // 2
    packet = np.zeros(length, dtype=complex)
    r = np.arange(1, width + 1, dtype=float)
    packet[start : start + width] = math.sqrt(2.0 / (width + 1)) * np.sin(math.pi * r / (width + 1))
    require(abs(np.vdot(packet, packet).real - 1.0) < TOL, "discrete sine packet is not normalized")
    overlap = float(np.vdot(packet[1:], packet[:-1]).real)
    difference_squared = 2.0 - 2.0 * overlap
    expected = 2.0 * (1.0 - math.cos(math.pi / (width + 1)))
    require(abs(difference_squared - expected) < TOL, "discrete sine identity failed")
    return packet


def pi_flux_stages():
    spacing = math.sqrt(2.0)
    basis = fixed_basis(4, 2)
    h0 = pi_flux_one_particle()
    h1 = delete_sites(h0, {0})
    h2 = delete_sites(h0, {0, 2})
    H0 = second_quantize(h0, basis)
    H1 = second_quantize(h1, basis)
    H2 = second_quantize(h2, basis)
    require_small(H2, "two selected pi-square sites do not delete every bond")
    P0_site0 = occupation_projector(basis, 0, 0)
    P1_site0 = occupation_projector(basis, 0, 1)
    W1 = local_record_isometry((P0_site0, P1_site0))
    H1_records = sparse.block_diag((H1, H1), format="csr").toarray()
    P0_site2 = occupation_projector(basis, 2, 0)
    P1_site2 = occupation_projector(basis, 2, 1)
    W_site2 = local_record_isometry((P0_site2, P1_site2))
    W2 = np.kron(np.eye(2), W_site2)
    H2_records = np.zeros((24, 24), dtype=complex)
    groups1 = frequency_groups(W1, H0, (-2, 0, 2), H1_records, (-1, 0, 1), spacing)
    groups2 = frequency_groups(W2, H1_records, (-1, 0, 1), H2_records, (0,), spacing)
    W_composite = W2 @ W1
    groups_composite = frequency_groups(W_composite, H0, (-2, 0, 2), H2_records, (0,), spacing)
    return {
        "spacing": spacing,
        "basis": basis,
        "H0": H0,
        "H1_records": H1_records,
        "H2_records": H2_records,
        "W1": W1,
        "W2": W2,
        "W_composite": W_composite,
        "groups1": groups1,
        "groups2": groups2,
        "groups_composite": groups_composite,
        "P0_site0": P0_site0,
        "P1_site0": P1_site0,
        "P0_site2": P0_site2,
        "P1_site2": P1_site2,
    }


def record_mismatch_projector(basis, which_site, record_axis, old_record=False):
    diagonal = []
    for old_value in range(2):
        for new_value in range(2):
            for mask in basis:
                recorded_value = old_value if old_record else new_value
                occupied = (mask >> which_site) & 1
                diagonal.append(float(recorded_value != occupied))
    require(record_axis == 2, "unexpected two-Record axis count")
    return np.diag(diagonal).astype(complex)


def normalized_choi_distances(gate, W, groups, packet):
    length = packet.size
    input_dimension = W.shape[1]
    output_dimension = W.shape[0]
    X = np.zeros((input_dimension * length, input_dimension), dtype=complex)
    for reference in range(input_dimension):
        X[reference * length : (reference + 1) * length, reference] = packet / math.sqrt(input_dimension)
    success = gate["S"] @ X
    refusal = gate["F"] @ X
    amplitudes = np.zeros((output_dimension + input_dimension, length, input_dimension), dtype=complex)
    amplitudes[:output_dimension] = success.reshape(output_dimension, length, input_dimension)
    amplitudes[output_dimension:] = refusal.reshape(input_dimension, length, input_dimension)
    reduced_matrix = amplitudes.transpose(0, 2, 1).reshape((output_dimension + input_dimension) * input_dimension, length)
    actual = reduced_matrix @ reduced_matrix.conj().T
    ideal_columns = np.zeros((output_dimension + input_dimension, input_dimension), dtype=complex)
    ideal_columns[:output_dimension] = W / math.sqrt(input_dimension)
    ideal_vector = ideal_columns.reshape(-1)
    ideal = np.outer(ideal_vector, ideal_vector.conj())
    frequency_dephased = np.zeros_like(ideal)
    for term in groups.values():
        columns = np.zeros_like(ideal_columns)
        columns[:output_dimension] = term / math.sqrt(input_dimension)
        vector = columns.reshape(-1)
        frequency_dephased += np.outer(vector, vector.conj())
    return trace_distance(actual, ideal), trace_distance(actual, frequency_dephased)


def trace_distance(left, right):
    difference = (left - right + (left - right).conj().T) / 2.0
    certify_dense(difference)
    return float(np.sum(np.abs(np.linalg.eigvalsh(difference))) / 2.0)


def status_copy_check(gate):
    success_dimension = gate["success_dimension"]
    source_dimension = gate["source_dimension"]
    destination_dimension = success_dimension + source_dimension
    success_projector = sparse.diags(
        np.concatenate((np.ones(success_dimension), np.zeros(source_dimension))),
        format="csr",
    )
    refusal_projector = sparse.eye(destination_dimension, format="csr") - success_projector
    cell_identity = sparse.eye(2, dtype=complex, format="csr")
    cell_flip = sparse.csr_matrix(np.array([[0, 1], [1, 0]], dtype=complex))
    copy = sparse.kron(success_projector, cell_identity, format="csr") + sparse.kron(
        refusal_projector, cell_flip, format="csr"
    )
    destination_hamiltonian = sparse.block_diag(
        (gate["H_out_total"], gate["H_in_total"]), format="csr"
    )
    copied_hamiltonian = sparse.kron(destination_hamiltonian, cell_identity, format="csr")
    require_small(copy.conj().T @ copy - sparse.eye(copy.shape[0]), "status copy is not unitary")
    require_small(copy @ copied_hamiltonian - copied_hamiltonian @ copy,
                  "degenerate status copy does not conserve energy")
    return copy.shape[0]


def check_shared_battery_two_events():
    data = pi_flux_stages()
    length = BATTERY_TOP + 1
    S1 = capped_lift(data["groups1"], length)
    S2 = capped_lift(data["groups2"], length)
    S_direct = capped_lift(data["groups_composite"], length)
    H0_total = total_hamiltonian(data["H0"], data["spacing"], length)
    H1_total = total_hamiltonian(data["H1_records"], data["spacing"], length)
    H2_total = total_hamiltonian(data["H2_records"], data["spacing"], length)
    gate1 = refusal_gate(S1, H0_total, H1_total)
    gate2 = refusal_gate(S2, H1_total, H2_total)
    copy_dimension = status_copy_check(gate1)
    require(gate1["U"].shape == (312, 312) and gate2["U"].shape == (624, 624), "sparse gate dimensions drifted")

    old_input_zero = sparse.block_diag((np.eye(6), np.zeros((6, 6))), format="csr")
    old_input_one = sparse.eye(12, format="csr") - old_input_zero
    old_output_zero = sparse.block_diag((np.eye(12), np.zeros((12, 12))), format="csr")
    old_output_one = sparse.eye(24, format="csr") - old_output_zero
    for old_input, old_output in ((old_input_zero, old_output_zero), (old_input_one, old_output_one)):
        require_small(
            sparse.kron(old_output, sparse.eye(length)) @ S2
            - S2 @ sparse.kron(old_input, sparse.eye(length)),
            "second lift changes the old Record",
        )

    interior_battery = sparse.diags(
        [float(2 <= level <= BATTERY_TOP - 2) for level in range(length)], format="csr"
    )
    interior_input = sparse.kron(sparse.eye(6), interior_battery, format="csr")
    require_small((S2 @ S1 - S_direct) @ interior_input,
                  "sequential shared-battery lift differs from direct composite")

    raw_state = np.array([1, 1j, -1, 2, 1 - 1j, -1j], dtype=complex)
    matter_state = raw_state / np.linalg.norm(raw_state)
    packet = discrete_sine(length, 7)
    initial = np.kron(matter_state, packet)
    intermediate = S1 @ initial
    require(abs(np.vdot(intermediate, intermediate).real - 1.0) < TOL, "first interior gate has refusal")
    intermediate_matrix = intermediate.reshape(12, length)
    battery_reduced = intermediate_matrix.T @ intermediate_matrix.conj()
    battery_purity = float(np.trace(battery_reduced @ battery_reduced).real)
    require(battery_purity < 0.999, "first gate did not retain system-battery correlations")
    second_input = intermediate
    sequential = gate2["S"] @ second_input
    direct = S_direct @ initial
    require_small(sequential - direct, "shared correlated battery composition failed")
    require(abs(np.vdot(sequential, sequential).real - 1.0) < TOL, "second interior gate has refusal")

    energies = (
        float(np.vdot(initial, H0_total @ initial).real),
        float(np.vdot(intermediate, H1_total @ intermediate).real),
        float(np.vdot(sequential, H2_total @ sequential).real),
    )
    require(max(energies) - min(energies) < 5.0e-9, "shared total energy changes across attempts")
    matter_operators = (
        np.kron(data["H0"], np.eye(length)),
        np.kron(data["H1_records"], np.eye(length)),
        np.kron(data["H2_records"], np.eye(length)),
    )
    matter_energies = (
        float(np.vdot(initial, matter_operators[0] @ initial).real),
        float(np.vdot(intermediate, matter_operators[1] @ intermediate).real),
        float(np.vdot(sequential, matter_operators[2] @ sequential).real),
    )
    battery_hamiltonian = data["spacing"] * np.diag(np.arange(length, dtype=float))
    battery_operators = tuple(
        np.kron(np.eye(system_dimension), battery_hamiltonian)
        for system_dimension in (6, 12, 24)
    )
    battery_energies = (
        float(np.vdot(initial, battery_operators[0] @ initial).real),
        float(np.vdot(intermediate, battery_operators[1] @ intermediate).real),
        float(np.vdot(sequential, battery_operators[2] @ sequential).real),
    )
    require(
        max(
            abs(total - matter - battery)
            for total, matter, battery in zip(energies, matter_energies, battery_energies)
        )
        < 5.0e-9,
        "direct matter plus battery ledger does not equal total energy",
    )
    require(
        max(abs((battery_energies[index + 1] - battery_energies[index])
                + (matter_energies[index + 1] - matter_energies[index])) for index in (0, 1)) < 5.0e-9,
        "spent shared battery does not balance matter energy",
    )

    mismatch_old = record_mismatch_projector(data["basis"], 0, 2, old_record=True)
    mismatch_new = record_mismatch_projector(data["basis"], 2, 2, old_record=False)
    composite = S2 @ S1
    require_small(sparse.kron(sparse.csr_matrix(mismatch_old), sparse.eye(length)) @ composite,
                  "final output corrupts the old Record")
    require_small(sparse.kron(sparse.csr_matrix(mismatch_new), sparse.eye(length)) @ composite,
                  "final output has an incorrect new Record")

    sharp_packet = np.zeros(length, dtype=complex)
    sharp_packet[length // 2] = 1.0
    broad_packet = discrete_sine(length, 7)
    sharp_distances = normalized_choi_distances(gate1, data["W1"], data["groups1"], sharp_packet)
    broad_distances = normalized_choi_distances(gate1, data["W1"], data["groups1"], broad_packet)
    require(sharp_distances[1] < TOL and broad_distances[0] < sharp_distances[0],
            "normalized Choi coherence controls failed")
    return (
        f"q1={tuple(sorted(data['groups1']))} q2={tuple(sorted(data['groups2']))} "
        f"q12={tuple(sorted(data['groups_composite']))} purityB1={battery_purity:.9f} "
        f"Etot={energies[0]:.9f} Emat={matter_energies[0]:.6f},{matter_energies[1]:.6f},{matter_energies[2]:.6f} "
        f"Ebat={battery_energies[0]:.6f},{battery_energies[1]:.6f},{battery_energies[2]:.6f} "
        f"normalizedChoi(sharpW={sharp_distances[0]:.6f},broadW={broad_distances[0]:.6f}) "
        f"statusCopyDim={copy_dimension}"
    )


def partial_trace_battery(amplitudes):
    return amplitudes @ amplitudes.conj().T


def status_dephase(density):
    return np.diag(np.diag(density))


def check_stationary_input_statistics():
    data = pi_flux_stages()
    length = BATTERY_TOP + 1
    S1 = capped_lift(data["groups1"], length)
    S2 = capped_lift(data["groups2"], length)
    S_direct = capped_lift(data["groups_composite"], length)
    H_initial = data["H0"]
    energy_scale = 2.0 * data["spacing"]
    ground_projector = (
        H_initial @ H_initial - energy_scale * H_initial
    ) / (2.0 * energy_scale**2)
    zero_projector = np.eye(6) - H_initial @ H_initial / energy_scale**2
    require_small(ground_projector @ ground_projector - ground_projector,
                  "polynomial ground projector is not idempotent")
    require_small(zero_projector @ zero_projector - zero_projector,
                  "polynomial zero-energy projector is not idempotent")
    require(round(np.trace(ground_projector).real) == 1, "ground projector rank changed")
    require(round(np.trace(zero_projector).real) == 4, "zero-energy projector rank changed")

    basis_vectors = np.eye(6, dtype=complex)
    ground_state = ground_projector @ basis_vectors[:, 0]
    ground_state /= np.linalg.norm(ground_state)
    zero_state = zero_projector @ basis_vectors[:, 1]
    zero_state /= np.linalg.norm(zero_state)
    stationary_inputs = (("ground", ground_state), ("zero", zero_state))
    packet = discrete_sine(length, 3)
    packet_overlap = float(np.vdot(packet[1:], packet[:-1]).real)
    require(0.6 < packet_overlap < 0.8, "stationary-input packet lacks finite translation sensitivity")

    first_energy_projectors = spectral_projectors(
        data["H1_records"],
        (-1, 0, 1),
        data["spacing"],
    )
    first_record_projectors = tuple(
        np.kron(
            np.diag([float(outcome == 0), float(outcome == 1)]),
            np.eye(6),
        )
        for outcome in (0, 1)
    )
    final_history_projectors = {
        (old_outcome, new_outcome): np.kron(
            np.diag([float(old_outcome == 0), float(old_outcome == 1)]),
            np.kron(
                np.diag([float(new_outcome == 0), float(new_outcome == 1)]),
                np.eye(6),
            ),
        )
        for old_outcome in (0, 1)
        for new_outcome in (0, 1)
    }

    maximum_joint_error = 0.0
    maximum_conditional_excess_error = 0.0
    maximum_history_error = 0.0
    maximum_final_state_distance = 0.0
    first_state_distances = {}
    zero_noncommuting_residual = 0.0
    for label, matter_state in stationary_inputs:
        initial_density = np.outer(matter_state, matter_state.conj())
        require_small(H_initial @ initial_density - initial_density @ H_initial,
                      f"{label} input is not energy stationary")
        initial_joint = np.kron(matter_state, packet)
        actual_first_joint = S1 @ initial_joint
        require(abs(np.vdot(actual_first_joint, actual_first_joint).real - 1.0) < TOL,
                f"{label} first stationary lift reaches a battery cap")
        actual_first_amplitudes = actual_first_joint.reshape(12, length)
        actual_first_density = partial_trace_battery(actual_first_amplitudes)
        ideal_first_state = data["W1"] @ matter_state
        ideal_first_density = np.outer(ideal_first_state, ideal_first_state.conj())
        first_difference = actual_first_density - ideal_first_density
        first_state_distances[label] = trace_distance(actual_first_density, ideal_first_density)

        joint_probabilities = {"actual": {}, "ideal": {}}
        for outcome, record_projector in enumerate(first_record_projectors):
            require_small(
                record_projector @ data["H1_records"]
                - data["H1_records"] @ record_projector,
                "first Record projector does not commute with output energy",
            )
            for energy_label, energy_projector in first_energy_projectors.items():
                effect = record_projector @ energy_projector
                require_small(effect @ data["H1_records"] - data["H1_records"] @ effect,
                              "joint first Record-energy effect is not stationary")
                actual_probability = trace_real(actual_first_density, effect)
                ideal_probability = trace_real(ideal_first_density, effect)
                joint_probabilities["actual"][(outcome, energy_label)] = actual_probability
                joint_probabilities["ideal"][(outcome, energy_label)] = ideal_probability
                maximum_joint_error = max(
                    maximum_joint_error,
                    abs(actual_probability - ideal_probability),
                )
        for outcome in (0, 1):
            actual_probability = sum(
                joint_probabilities["actual"][(outcome, energy_label)]
                for energy_label in (-1, 0, 1)
            )
            ideal_probability = sum(
                joint_probabilities["ideal"][(outcome, energy_label)]
                for energy_label in (-1, 0, 1)
            )
            require(actual_probability > 0.1 and ideal_probability > 0.1,
                    f"{label} stationary branch is probability zero")
            actual_excess = sum(
                data["spacing"] * (energy_label + 1)
                * joint_probabilities["actual"][(outcome, energy_label)]
                for energy_label in (-1, 0, 1)
            ) / actual_probability
            ideal_excess = sum(
                data["spacing"] * (energy_label + 1)
                * joint_probabilities["ideal"][(outcome, energy_label)]
                for energy_label in (-1, 0, 1)
            ) / ideal_probability
            maximum_conditional_excess_error = max(
                maximum_conditional_excess_error,
                abs(actual_excess - ideal_excess),
            )

        actual_final_joint = S2 @ actual_first_joint
        direct_final_joint = S_direct @ initial_joint
        require_small(actual_final_joint - direct_final_joint,
                      f"{label} stationary history did not reuse the correlated battery")
        require(abs(np.vdot(actual_final_joint, actual_final_joint).real - 1.0) < TOL,
                f"{label} complete stationary lift reaches a battery cap")
        actual_final_density = partial_trace_battery(actual_final_joint.reshape(24, length))
        ideal_final_state = data["W_composite"] @ matter_state
        ideal_final_density = np.outer(ideal_final_state, ideal_final_state.conj())
        maximum_final_state_distance = max(
            maximum_final_state_distance,
            trace_distance(actual_final_density, ideal_final_density),
        )
        for history_projector in final_history_projectors.values():
            actual_probability = trace_real(actual_final_density, history_projector)
            ideal_probability = trace_real(ideal_final_density, history_projector)
            maximum_history_error = max(
                maximum_history_error,
                abs(actual_probability - ideal_probability),
            )

        if label == "zero":
            zero_noncommuting_residual = frobenius(
                data["H1_records"] @ first_difference
                - first_difference @ data["H1_records"]
            )

    require(maximum_joint_error < TOL,
            "stationary first Record-energy probabilities differ from ideal")
    require(maximum_conditional_excess_error < TOL,
            "stationary conditional ground excess differs from ideal")
    require(maximum_history_error < TOL,
            "stationary complete Record-history probabilities differ from ideal")
    require(first_state_distances["ground"] < TOL,
            "ground control unexpectedly has first-stage energy coherence")
    require(first_state_distances["zero"] > 0.3 and zero_noncommuting_residual > 1.0,
            "stationary zero-energy input lacks a noncommuting state difference")
    require(maximum_final_state_distance < TOL,
            "zero final Hamiltonian did not close the stationary fixture state comparison")
    return (
        f"betaShiftOverlap={packet_overlap:.9f} "
        f"jointErr={maximum_joint_error:.2e} condExcessErr={maximum_conditional_excess_error:.2e} "
        f"historyErr={maximum_history_error:.2e} "
        f"firstDistance(ground={first_state_distances['ground']:.2e},zero={first_state_distances['zero']:.9f}) "
        f"zeroNoncomm={zero_noncommuting_residual:.9f} finalStateErr={maximum_final_state_distance:.2e}"
    )


def check_status_readout_correction():
    p = 0.04
    physical = np.zeros((3, 2), dtype=complex)
    bilateral = np.zeros((3, 2), dtype=complex)
    physical[0, 0] = math.sqrt(1.0 - p)
    physical[1, 0] = math.sqrt(p)
    bilateral[0, 0] = math.sqrt(1.0 - p)
    bilateral[2, 1] = math.sqrt(p)
    physical_reduced = partial_trace_battery(physical)
    bilateral_reduced = partial_trace_battery(bilateral)
    coherent_distance = trace_distance(physical_reduced, bilateral_reduced)
    predicted_coherent = (p + math.sqrt(4.0 * p - 3.0 * p * p)) / 2.0
    require(abs(coherent_distance - predicted_coherent) < TOL, "coherent cap counterexample formula failed")
    dephased_physical = status_dephase(physical_reduced)
    readout_distance = trace_distance(dephased_physical, bilateral_reduced)
    require(abs(readout_distance - p) < TOL, "status-readout cap distance is not p")
    require(coherent_distance > 4.0 * p, "coherent cap error is not amplitude order")

    def beta(energy):
        return math.sin(math.pi * (energy - 1.0) / 4.0) / math.sqrt(2.0)

    overlap, integration_error = quad(
        lambda energy: beta(energy + 2.0) * beta(energy),
        1.0,
        2.0,
        epsabs=2.0e-13,
        epsrel=2.0e-13,
    )
    require(abs(overlap - 1.0 / (2.0 * math.pi)) < 2.0e-12, "compact sine status overlap is not 1/(2*pi)")
    require(integration_error < 1.0e-12, "compact sine overlap quadrature is unresolved")
    return (
        f"p={p:.3f} coherent={coherent_distance:.9f} readout={readout_distance:.9f} "
        f"sineOverlap={overlap:.12f}=1/(2pi); fixture_status_readout_distance=p"
    )


def check_source_contract():
    source_path = Path(__file__).resolve()
    require(source_path.name == EXPECTED_FILENAME, "checker filename changed")
    source = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source)
    allowed = {"ast", "hashlib", "itertools", "math", "os", "pathlib", "sys", "numpy", "scipy"}
    imports = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            roots = {alias.name.split(".")[0] for alias in node.names}
            imports.update(roots)
            require(roots <= allowed, f"forbidden import roots: {sorted(roots - allowed)}")
        elif isinstance(node, ast.ImportFrom):
            root = (node.module or "").split(".")[0]
            imports.add(root)
            require(node.level == 0 and root in allowed, f"forbidden from-import: {node.module}")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(node.func.id not in {"open", "exec", "eval", "compile", "__import__"},
                    f"forbidden dynamic/file call: {node.func.id}")
    reads = [
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and node.func.attr in {"read", "read_text", "read_bytes", "load", "loads"}
    ]
    require(len(reads) == 1 and reads[0].func.attr == "read_text", "external read surface detected")
    timeout_values = [
        ast.literal_eval(node.value)
        for node in tree.body
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "AUDIT_TIMEOUT_SEC" for target in node.targets)
    ]
    require(timeout_values == [180], f"timeout declaration changed: {timeout_values}")
    for variable in (
        "OPENBLAS_NUM_THREADS",
        "OMP_NUM_THREADS",
        "MKL_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS",
        "NUMEXPR_NUM_THREADS",
    ):
        require(os.environ.get(variable) == "1", f"{variable} is not pinned to one")
    digest = hashlib.sha256(source.encode("utf-8")).hexdigest()
    return f"sha256={digest[:16]} imports={','.join(sorted(imports))} self-read-only BLAS=1 dense<={DENSE_MATRIX_LIMIT}"


CHECKS = (
    ("source_contract", check_source_contract),
    ("fixed_number_process", check_fixed_number_process),
    ("uniform_clock_laws", check_uniform_and_clock_laws),
    ("uniform_fibre_identities", check_uniform_fibre_operator_identities),
    ("local_defects", check_local_defects),
    ("shared_battery_two_events", check_shared_battery_two_events),
    ("stationary_input_statistics", check_stationary_input_statistics),
    ("status_readout_correction", check_status_readout_correction),
)


def main():
    passed = 0
    failed = 0
    for name, function in CHECKS:
        try:
            detail = function()
        except Exception as error:
            failed += 1
            print(f"FAIL {name}: {type(error).__name__}: {error}")
        else:
            passed += 1
            print(f"PASS {name}: {detail}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
