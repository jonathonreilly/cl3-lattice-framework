#!/usr/bin/env python3
"""Independent real-space check of partial parity-class deletion and propagation.

The checker constructs the supplied staggered nearest-neighbour hopping matrix
directly on finite periodic tori.  It imports no project code and uses no
gamma-matrix representation.
"""

from __future__ import annotations

import itertools
import resource
import time

import numpy as np

AUDIT_TIMEOUT_SEC = 60

EVEN_CLASSES = ((0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 0))
SPECTRAL_TOL = 1e-9
PASS = 0
FAIL = 0


def check(label, condition):
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    print(("PASS " if ok else "FAIL ") + label)


def real_space_torus(length):
    coords = [(x, y, z) for x in range(length) for y in range(length) for z in range(length)]
    index = {coord: i for i, coord in enumerate(coords)}
    h = np.zeros((length**3, length**3), dtype=np.float64)
    edge_count = 0
    for coord in coords:
        x, y, z = coord
        for axis in range(3):
            neighbor = list(coord)
            neighbor[axis] = (neighbor[axis] + 1) % length
            eta = 1 if axis == 0 else ((-1) ** x if axis == 1 else (-1) ** (x + y))
            i, j = index[coord], index[tuple(neighbor)]
            assert i != j and h[i, j] == 0.0
            h[i, j] = h[j, i] = -float(eta)
            edge_count += 1
    classes = [tuple(component % 2 for component in coord) for coord in coords]
    return h, coords, index, classes, edge_count


def live_subgraph(h, classes, removed):
    live = np.array([i for i, parity_class in enumerate(classes) if parity_class not in removed],
                    dtype=np.int64)
    return h[np.ix_(live, live)], live


def centered_momenta(ncell):
    integers = np.arange(-(ncell // 2), ncell - ncell // 2, dtype=np.int64)
    return np.pi * integers / ncell


def analytic_spectrum(length, removed_count, omit_generic_zeros=False):
    ncell = length // 2
    values = []
    node_count = 0
    for kx, ky, kz in itertools.product(centered_momenta(ncell), repeat=3):
        epsilon = 2.0 * np.sqrt(np.cos(kx) ** 2 + np.cos(ky) ** 2 + np.cos(kz) ** 2)
        if epsilon <= 1e-12:
            node_count += 1
            values.extend([0.0] * (8 - removed_count))
        else:
            values.extend([-epsilon] * (4 - removed_count))
            if not omit_generic_zeros:
                values.extend([0.0] * removed_count)
            values.extend([epsilon] * (4 - removed_count))
    return np.sort(np.asarray(values, dtype=np.float64)), node_count


def removed_classes(mask):
    return {EVEN_CLASSES[bit] for bit in range(4) if (mask >> bit) & 1}


def spectrum_ladder():
    worst_global = 0.0
    for length in (4, 6, 8):
        h, coords, index, classes, edge_count = real_space_torus(length)
        construction_ok = (
            edge_count == 3 * length**3
            and np.count_nonzero(h) == 2 * edge_count
            and np.array_equal(h, h.T)
            and np.all(np.count_nonzero(h, axis=1) == 6)
        )
        max_error = 0.0
        worst_mask = 0
        cardinality_ok = True
        zero_count_ok = True
        node_counts = set()
        for mask in range(16):
            removed = removed_classes(mask)
            live_h, live = live_subgraph(h, classes, removed)
            computed = np.linalg.eigvalsh(live_h)
            claimed, node_count = analytic_spectrum(length, len(removed))
            node_counts.add(node_count)
            cardinality_ok &= len(computed) == len(claimed) == (8 - len(removed)) * (length // 2) ** 3
            if len(computed) == len(claimed):
                error = float(np.max(np.abs(computed - claimed))) if len(computed) else 0.0
                if error > max_error:
                    max_error, worst_mask = error, mask
            expected_zeros = (len(removed) * ((length // 2) ** 3 - node_count)
                              + (8 - len(removed)) * node_count)
            zero_count_ok &= int(np.sum(np.abs(computed) < SPECTRAL_TOL)) == expected_zeros
        check(f"L={length}: real-space torus construction", construction_ok)
        check(f"L={length}: all 16 deleted-class spectra and zero counts", cardinality_ok and zero_count_ok and max_error < 1e-10)
        print(
            f"SPECTRUM L={length} N={length // 2} subsets=16 nodes={sorted(node_counts)} "
            f"max_error={max_error:.3e} worst_mask={worst_mask:04b} max_dimension={length**3}"
        )
        worst_global = max(worst_global, max_error)
    return worst_global


def breadth_first_distances(h, start):
    distance = -np.ones(len(h), dtype=np.int64)
    distance[start] = 0
    queue = [start]
    for vertex in queue:
        for neighbor in np.flatnonzero(h[vertex]):
            if distance[neighbor] < 0:
                distance[neighbor] = distance[vertex] + 1
                queue.append(int(neighbor))
    return distance


def exact_krylov_support(h, start):
    """Vertices with a nonzero coefficient in H^n|start>, n < dim, using integer arithmetic."""
    rows, cols = np.nonzero(h)
    amplitudes = np.zeros(len(h), dtype=object)
    amplitudes[start] = 1
    support = np.zeros(len(h), dtype=bool)
    for _ in range(len(h)):
        support |= np.array([value != 0 for value in amplitudes], dtype=bool)
        following = np.zeros(len(h), dtype=object)
        for row, col in zip(rows, cols):
            following[row] += int(h[row, col]) * amplitudes[col]
        amplitudes = following
    return support


def open_cube_hopping():
    coords = [(x, y, z) for x in range(2) for y in range(2) for z in range(2)]
    index = {coord: i for i, coord in enumerate(coords)}
    h = np.zeros((8, 8), dtype=np.float64)
    for coord in coords:
        x, y, z = coord
        for axis in range(3):
            neighbor = list(coord)
            neighbor[axis] += 1
            if neighbor[axis] == 2:
                continue
            eta = 1 if axis == 0 else ((-1) ** x if axis == 1 else (-1) ** (x + y))
            i, j = index[coord], index[tuple(neighbor)]
            h[i, j] = h[j, i] = -float(eta)
    return h, coords


def half_filled_fock_sea(h):
    eigenvalues, eigenvectors = np.linalg.eigh(h)
    occupied_orbitals = eigenvectors[:, eigenvalues < -SPECTRAL_TOL]
    assert occupied_orbitals.shape == (8, 4)
    state = np.zeros(256, dtype=np.complex128)
    for occupied_sites in itertools.combinations(range(8), 4):
        bitstring = sum(1 << site for site in occupied_sites)
        state[bitstring] = np.linalg.det(occupied_orbitals[list(occupied_sites), :])
    state /= np.linalg.norm(state)
    return state


def projected_remaining_state(sea, formed, pattern):
    remaining = [site for site in range(8) if site not in formed]
    fixed_occupied = [site for site, value in zip(formed, pattern) if value]
    probability = 0.0
    state = np.zeros(1 << len(remaining), dtype=np.complex128)
    for bitstring, amplitude in enumerate(sea):
        if any(((bitstring >> site) & 1) != value for site, value in zip(formed, pattern)):
            continue
        probability += float(abs(amplitude) ** 2)
        local_bitstring = 0
        residual_occupied = []
        for local_site, global_site in enumerate(remaining):
            if (bitstring >> global_site) & 1:
                local_bitstring |= 1 << local_site
                residual_occupied.append(global_site)
        inversions = sum(fixed_site > residual_site
                         for fixed_site in fixed_occupied for residual_site in residual_occupied)
        state[local_bitstring] = amplitude * (-1 if inversions % 2 else 1)
    if probability > 0.0:
        state /= np.sqrt(probability)
    return state, remaining, probability


def one_body_density(state, fermionic=True):
    mode_count = int(round(np.log2(len(state))))
    density = np.zeros((mode_count, mode_count), dtype=np.complex128)
    for source, amplitude in enumerate(state):
        if amplitude == 0.0:
            continue
        for annihilated in range(mode_count):
            if not ((source >> annihilated) & 1):
                continue
            after_annihilation = source ^ (1 << annihilated)
            sign_annihilation = (-1) ** ((source & ((1 << annihilated) - 1)).bit_count()) \
                if fermionic else 1
            for created in range(mode_count):
                if (after_annihilation >> created) & 1:
                    continue
                target = after_annihilation | (1 << created)
                sign_creation = (-1) ** ((after_annihilation & ((1 << created) - 1)).bit_count()) \
                    if fermionic else 1
                # C_ij=<c_j^dagger c_i>, so a occupied orbital w has C=w w^dagger.
                density[annihilated, created] += (
                    np.conj(state[target]) * amplitude * sign_annihilation * sign_creation
                )
    return density


def conditional_fock_factorization():
    phase_state = np.array([0.0, 1.0, 1j, 0.0], dtype=complex) / np.sqrt(2.0)
    phase_orbital = np.array([1.0, 1j], dtype=complex) / np.sqrt(2.0)
    phase_target = np.outer(phase_orbital, phase_orbital.conj())
    phase_density = one_body_density(phase_state)
    check("complex one-fermion state fixes the covariance index convention",
          np.max(np.abs(phase_density - phase_target)) < 1e-14
          and np.max(np.abs(phase_density.T - phase_target)) > 0.9)
    h, coords = open_cube_hopping()
    sea = half_filled_fock_sea(h)
    even_vertices = tuple(i for i, coord in enumerate(coords) if sum(coord) % 2 == 0)
    case_count = 0
    max_probability_error = 0.0
    max_density_hermitian_error = 0.0
    max_density_projector_error = 0.0
    max_commutator = 0.0
    max_zero_support_error = 0.0
    max_delta_projector_error = 0.0
    max_rank_error = 0.0
    wrong_sign_gap = 0.0
    wrong_h_commutator = None
    wrong_h_bond = None
    spectral_counts_ok = True
    for formed_count in range(5):
        for formed in itertools.combinations(even_vertices, formed_count):
            for pattern in itertools.product((0, 1), repeat=formed_count):
                case_count += 1
                state, remaining, probability = projected_remaining_state(sea, formed, pattern)
                density = one_body_density(state)
                wrong_density = one_body_density(state, fermionic=False)
                h_remaining = h[np.ix_(remaining, remaining)]
                eigenvalues, eigenvectors = np.linalg.eigh(h_remaining)
                negative = eigenvectors[:, eigenvalues < -SPECTRAL_TOL]
                zero = eigenvectors[:, np.abs(eigenvalues) < SPECTRAL_TOL]
                p_negative = negative @ negative.T
                p_zero = zero @ zero.T
                delta = density - p_negative
                expected_rank = formed_count - sum(pattern)
                spectral_counts_ok &= negative.shape[1] == 4 - formed_count
                spectral_counts_ok &= zero.shape[1] == formed_count
                max_probability_error = max(max_probability_error, abs(probability - 2.0**(-formed_count)))
                max_density_hermitian_error = max(
                    max_density_hermitian_error, float(np.linalg.norm(density - density.conj().T))
                )
                max_density_projector_error = max(
                    max_density_projector_error, float(np.linalg.norm(density @ density - density))
                )
                max_commutator = max(
                    max_commutator, float(np.linalg.norm(density @ h_remaining - h_remaining @ density))
                )
                max_zero_support_error = max(
                    max_zero_support_error, float(np.linalg.norm(delta - p_zero @ delta @ p_zero))
                )
                max_delta_projector_error = max(
                    max_delta_projector_error, float(np.linalg.norm(delta @ delta - delta))
                )
                max_rank_error = max(max_rank_error, abs(float(np.trace(delta).real) - expected_rank))
                wrong_sign_gap = max(wrong_sign_gap, float(np.linalg.norm(wrong_density - density)))

                if formed == (even_vertices[0],) and pattern == (1,):
                    bad_h = h_remaining.copy()
                    bonds = np.argwhere(np.triu(np.abs(bad_h) > 0.0, 1))
                    a, b = (int(x) for x in bonds[0])
                    bad_h[a, b] = bad_h[b, a] = -bad_h[a, b]
                    wrong_h_commutator = float(np.linalg.norm(density @ bad_h - bad_h @ density))
                    wrong_h_bond = (remaining[a], remaining[b])

    correct = (
        case_count == 81
        and abs(float(np.vdot(sea, sea).real) - 1.0) < 1e-13
        and max_probability_error < 1e-13
        and spectral_counts_ok
        and max_density_hermitian_error < 1e-12
        and max_density_projector_error < 1e-12
        and max_commutator < 1e-12
        and max_zero_support_error < 1e-12
        and max_delta_projector_error < 1e-12
        and max_rank_error < 1e-12
    )
    check("open-cube direct-Fock conditional factorization over all 81 cases", correct)
    check(
        "wrong fermion signs and a different remaining Hamiltonian are rejected",
        wrong_sign_gap > 1e-3 and wrong_h_commutator is not None and wrong_h_commutator > 1e-3,
    )
    print(
        f"FOCK cases={case_count} even_vertices={even_vertices} probability_maxerr={max_probability_error:.3e} "
        f"spectral_counts_ok={spectral_counts_ok} hermitian_maxerr={max_density_hermitian_error:.3e} "
        f"projector_maxerr={max_density_projector_error:.3e} commutator_max={max_commutator:.3e} "
        f"zero_support_maxerr={max_zero_support_error:.3e} delta_projector_maxerr={max_delta_projector_error:.3e} "
        f"rank_maxerr={max_rank_error:.3e}"
    )
    print(
        f"FOCK_CONTROLS wrong_sign_density_gap={wrong_sign_gap:.6e} "
        f"wrong_h_bond={wrong_h_bond} wrong_h_commutator={wrong_h_commutator:.6e}"
    )


def mutation_and_propagation():
    length = 6
    h, coords, index, classes, edge_count = real_space_torus(length)
    removed = {(0, 0, 0)}
    live_h, live = live_subgraph(h, classes, removed)
    local = {int(global_index): i for i, global_index in enumerate(live)}
    initial_global = index[(0, 1, 1)]
    neighbor_global = index[(1, 1, 1)]
    initial = local[initial_global]
    neighbor = local[neighbor_global]

    computed = np.linalg.eigvalsh(live_h)
    mutated = live_h.copy()
    original_bond = mutated[initial, neighbor]
    mutated[initial, neighbor] = mutated[neighbor, initial] = -original_bond
    mutated_spectrum = np.linalg.eigvalsh(mutated)
    mutation_distance = float(np.max(np.abs(mutated_spectrum - computed)))
    fourth_moment_change = float(abs(np.sum(mutated_spectrum**4) - np.sum(computed**4)))
    changed_entries = int(np.count_nonzero(mutated - live_h))
    check(
        "single physical-bond sign twist changes the spectrum",
        changed_entries == 2 and mutation_distance > 1e-6 and fourth_moment_change > 1.0,
    )
    print(
        f"MUTATION L=6 R=000 bond=(0,1,1)-(1,1,1) changed_entries={changed_entries} "
        f"max_spectral_distance={mutation_distance:.9e} fourth_moment_change={fourth_moment_change:.6f}"
    )

    omitted, node_count = analytic_spectrum(length, 1, omit_generic_zeros=True)
    correct, _ = analytic_spectrum(length, 1)
    missing = len(correct) - len(omitted)
    check(
        "omitting generic zero branches fails spectral cardinality",
        node_count == 0 and len(computed) == len(correct) == 189 and len(omitted) == 162 and missing == 27,
    )
    print(f"OMITTED_ZERO L=6 N=3 nodes={node_count} live_dimension=189 wrong_count=162 missing={missing}")

    eigenvalues, eigenvectors = np.linalg.eigh(live_h)
    zero = np.abs(eigenvalues) < SPECTRAL_TOL
    basis = np.zeros(len(live_h), dtype=np.complex128)
    basis[initial] = 1.0
    coefficients = eigenvectors.T @ basis
    zero_weight = float(np.sum(np.abs(coefficients[zero]) ** 2))
    derivative_kernel = np.abs(live_h @ basis) ** 2
    nearest = np.flatnonzero(live_h[initial])
    kernel_values = derivative_kernel[nearest]
    distance = breadth_first_distances(live_h, initial)
    graph_max_distance = int(distance.max())
    krylov_support = exact_krylov_support(live_h, initial)
    max_occupied_distance = int(distance[krylov_support].max())
    connected = bool(np.all(distance >= 0))
    rows = []
    propagation_ok = connected and int(zero.sum()) == 27 and zero_weight < 1e-24
    propagation_ok &= len(nearest) == 6 and np.array_equal(kernel_values, np.ones(6))
    for tick in (0.2, 0.5, 1.0):
        state = eigenvectors @ (np.exp(-1j * tick * eigenvalues) * coefficients)
        probability = np.abs(state) ** 2
        norm_error = abs(float(probability.sum()) - 1.0)
        outside = float(1.0 - probability[initial])
        nearest_probability = float(probability[distance == 1].sum())
        farthest_probability = float(
            probability[krylov_support & (distance == max_occupied_distance)].sum()
        )
        propagation_ok &= norm_error < 1e-12 and outside > 0.0 and farthest_probability > 0.0
        rows.append((tick, norm_error, outside, nearest_probability, nearest_probability / tick**2,
                     farthest_probability))
    check("L=6 conditioned even-site propagation and zero-space control", propagation_ok)
    print(
        f"PROP_SETUP L=6 R=000 initial=(0,1,1) N=3 exact_nodes=0 zero_dim={int(zero.sum())} "
        f"zero_projection={zero_weight:.3e} degree={len(nearest)} kernel_per_neighbor={kernel_values[0]:.1f} "
        f"graph_max_distance={graph_max_distance} exact_krylov_sites={int(krylov_support.sum())} "
        f"max_occupied_distance={max_occupied_distance}"
    )
    for tick, norm_error, outside, near_probability, near_scaled, far_probability in rows:
        print(
            f"PROP t={tick:.1f} norm_error={norm_error:.3e} outside_probability={outside:.9e} "
            f"nearest_probability={near_probability:.9e} nearest_over_t2={near_scaled:.9e} "
            f"max_distance_probability={far_probability:.9e}"
        )


def main():
    started = time.monotonic()
    worst = spectrum_ladder()
    conditional_fock_factorization()
    mutation_and_propagation()
    elapsed = time.monotonic() - started
    peak_mib = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024.0 * 1024.0)
    check("resource limits", elapsed < 60.0 and peak_mib < 1024.0)
    print(f"RESOURCES seconds={elapsed:.3f} peak_MiB={peak_mib:.1f} global_spectrum_max_error={worst:.3e}")
    print("SCOPE finite tori and cube; supplied hopping/deletion/occupation instrument; physical record mapping and clock open")
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    raise SystemExit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
