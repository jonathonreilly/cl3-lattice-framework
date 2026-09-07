#!/usr/bin/env python3
"""Spin-half cubic ice, exact RK point, and Coulomb-phase diagnostics.

The microscopic variables are one occupation qubit on every cubic link with
exactly three occupied links touching each vertex.  Alternating plaquette
flips preserve that Gauss constraint.  The runner builds the exact RK graph on
the L=2 torus and performs deterministic-seed checkerboard Monte Carlo on
larger tori to resolve static Coulomb correlations, charged sectors, and
magnetic trial-state expectations. Renormalized stiffness is not proved here.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from itertools import combinations, product

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
    "scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py",
    "scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py",
)


ORIENTATIONS = ((0, 1), (0, 2), (1, 2))
TENSOR_PATTERNS = ((1, 0, 0), (1, 1, 0), (1, 1, 1), (2, 1, 0))


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


def initial_ice(length: int) -> np.ndarray:
    coordinates = np.indices((length, length, length))
    occupation = np.zeros((length, length, length, 3), dtype=np.uint8)
    for axis in range(3):
        occupation[..., axis] = coordinates[axis] % 2
    return occupation


def vertex_degrees(occupation: np.ndarray) -> np.ndarray:
    degree = np.zeros(occupation.shape[:3], dtype=np.int16)
    for axis in range(3):
        links = occupation[..., axis]
        degree += links
        degree += np.roll(links, 1, axis=axis)
    return degree


def gauss_charges(occupation: np.ndarray) -> np.ndarray:
    length = occupation.shape[0]
    coordinates = np.indices((length, length, length))
    staggering = (-1) ** np.sum(coordinates, axis=0)
    return staggering * (vertex_degrees(occupation) - 3)


def flippable_mask(
    occupation: np.ndarray, first_axis: int, second_axis: int
) -> np.ndarray:
    first_low = occupation[..., first_axis]
    second_high = np.roll(
        occupation[..., second_axis], -1, axis=first_axis
    )
    first_high = np.roll(
        occupation[..., first_axis], -1, axis=second_axis
    )
    second_low = occupation[..., second_axis]
    return (
        (first_low == first_high)
        & (second_low == second_high)
        & (first_low != second_low)
    )


def flippable_count(occupation: np.ndarray) -> int:
    return int(
        sum(
            np.count_nonzero(flippable_mask(occupation, first, second))
            for first, second in ORIENTATIONS
        )
    )


def electric_flux(occupation: np.ndarray) -> tuple[int, int, int]:
    length = occupation.shape[0]
    coordinates = np.indices((length, length, length))
    staggering = (-1.0) ** np.sum(coordinates, axis=0)
    electric = staggering[..., None] * (occupation.astype(float) - 0.5)
    flux = []
    for axis in range(3):
        plane = [slice(None), slice(None), slice(None), axis]
        plane[axis] = 0
        flux.append(int(round(float(np.sum(electric[tuple(plane)])))))
    return tuple(flux)


def apply_root_flips(
    occupation: np.ndarray,
    first_axis: int,
    second_axis: int,
    roots: np.ndarray,
) -> None:
    occupation[..., first_axis] ^= roots
    occupation[..., first_axis] ^= np.roll(
        roots, 1, axis=second_axis
    )
    occupation[..., second_axis] ^= roots
    occupation[..., second_axis] ^= np.roll(
        roots, 1, axis=first_axis
    )


def insert_defect_pair(
    occupation: np.ndarray, separation: int
) -> np.ndarray:
    result = occupation.copy()
    length = result.shape[0]
    for offset in range(separation):
        result[offset % length, 0, 0, 0] ^= 1
    return result


class CubicIceSampler:
    def __init__(
        self,
        length: int,
        seed: int,
    ) -> None:
        if length % 2 != 0 or length < 4:
            raise ValueError("checkerboard sampler needs an even L>=4")
        self.length = length
        self.rng = np.random.default_rng(seed)
        self.occupation = initial_ice(length)
        coordinates = np.indices((length, length, length))
        self.color_masks: dict[tuple[int, int, int, int], np.ndarray] = {}
        for first_axis, second_axis in ORIENTATIONS:
            for first_color, second_color in product((0, 1), repeat=2):
                self.color_masks[
                    (
                        first_axis,
                        second_axis,
                        first_color,
                        second_color,
                    )
                ] = (
                    (coordinates[first_axis] % 2 == first_color)
                    & (coordinates[second_axis] % 2 == second_color)
                )

    def sweep(self) -> None:
        orientation_order = self.rng.permutation(len(ORIENTATIONS))
        for orientation_index in orientation_order:
            first_axis, second_axis = ORIENTATIONS[orientation_index]
            color_order = self.rng.permutation(4)
            for color_index in color_order:
                first_color = int(color_index // 2)
                second_color = int(color_index % 2)
                allowed = self.color_masks[
                    (
                        first_axis,
                        second_axis,
                        first_color,
                        second_color,
                    )
                ]
                candidates = flippable_mask(
                    self.occupation, first_axis, second_axis
                )
                chosen = (
                    candidates
                    & allowed
                    & (self.rng.random(candidates.shape) < 0.5)
                )
                apply_root_flips(
                    self.occupation,
                    first_axis,
                    second_axis,
                    chosen.astype(np.uint8),
                )


def block_mean_error(values: list[float], block_count: int = 16) -> tuple[float, float]:
    data = np.asarray(values, dtype=float)
    usable = (len(data) // block_count) * block_count
    if usable == 0:
        raise ValueError("not enough values for blocks")
    blocks = data[:usable].reshape(block_count, -1).mean(axis=1)
    return float(np.mean(blocks)), float(
        np.std(blocks, ddof=1) / np.sqrt(block_count)
    )


@dataclass(frozen=True)
class RawStructureSample:
    longitudinal: float
    transverse_first: float
    transverse_second: float
    polarization_components: tuple[float, ...]
    tensor_amplitudes: tuple[tuple[complex, complex, complex], ...]


@dataclass(frozen=True)
class StructureResult:
    longitudinal: float
    transverse_first: float
    transverse_second: float
    transverse_split: float
    tensor_longitudinal_residual: float
    tensor_polarization_split: float
    tensor_weight_spread: float


def structure_sample(occupation: np.ndarray) -> RawStructureSample:
    length = occupation.shape[0]
    coordinates = np.indices((length, length, length))
    staggering = (-1.0) ** np.sum(coordinates, axis=0)
    electric = staggering[..., None] * (occupation.astype(float) - 0.5)
    transformed = np.fft.fftn(electric, axes=(0, 1, 2)) / np.sqrt(
        length**3
    )
    longitudinal = []
    transverse_first = []
    transverse_second = []
    polarization_components = []
    for mode, destination in (
        (1, transverse_first),
        (2, transverse_second),
    ):
        for axis in range(3):
            momentum_index = [0, 0, 0]
            momentum_index[axis] = mode
            amplitudes = transformed[tuple(momentum_index)]
            powers = np.abs(amplitudes) ** 2
            longitudinal.append(float(powers[axis]))
            transverse_axes = [index for index in range(3) if index != axis]
            first_value = float(powers[transverse_axes[0]])
            second_value = float(powers[transverse_axes[1]])
            destination.append(0.5 * (first_value + second_value))
            if mode == 1:
                polarization_components.extend((first_value, second_value))
    tensor_amplitudes = tuple(
        tuple(complex(value) for value in transformed[pattern])
        for pattern in TENSOR_PATTERNS
    )
    return RawStructureSample(
        longitudinal=float(np.mean(longitudinal)),
        transverse_first=float(np.mean(transverse_first)),
        transverse_second=float(np.mean(transverse_second)),
        polarization_components=tuple(polarization_components),
        tensor_amplitudes=tensor_amplitudes,
    )


@dataclass(frozen=True)
class ChainResult:
    flippable_mean: float
    flippable_error: float
    structure: StructureResult | None
    degree_signature: tuple[tuple[int, int], ...]
    electric_flux: tuple[int, int, int]


def run_chain(
    length: int,
    seed: int,
    *,
    thermal_sweeps: int = 600,
    sample_count: int = 2400,
    sweep_stride: int = 2,
    measure_structure: bool = False,
) -> ChainResult:
    sampler = CubicIceSampler(length, seed)
    initial_signature = tuple(
        sorted(Counter(vertex_degrees(sampler.occupation).ravel()).items())
    )
    initial_flux = electric_flux(sampler.occupation)
    for _ in range(thermal_sweeps):
        sampler.sweep()

    flippable_values: list[float] = []
    structures: list[RawStructureSample] = []
    for _ in range(sample_count):
        for _ in range(sweep_stride):
            sampler.sweep()
        flippable_values.append(float(flippable_count(sampler.occupation)))
        if measure_structure:
            structures.append(structure_sample(sampler.occupation))

    final_signature = tuple(
        sorted(Counter(vertex_degrees(sampler.occupation).ravel()).items())
    )
    if final_signature != initial_signature:
        raise AssertionError(
            f"local updates changed charge sector: {initial_signature} -> {final_signature}"
        )
    final_flux = electric_flux(sampler.occupation)
    if final_flux != initial_flux:
        raise AssertionError(
            f"local updates changed electric flux: {initial_flux} -> {final_flux}"
        )
    flippable_mean, flippable_error = block_mean_error(flippable_values)
    if structures:
        component_means = np.mean(
            np.asarray(
                [sample.polarization_components for sample in structures],
                dtype=float,
            ),
            axis=0,
        )
        ensemble_splits = [
            abs(component_means[index] - component_means[index + 1])
            / max(component_means[index] + component_means[index + 1], 1.0e-15)
            for index in range(0, len(component_means), 2)
        ]
        tensor_longitudinal_residuals = []
        tensor_polarization_splits = []
        tensor_weights = []
        for pattern_index, pattern in enumerate(TENSOR_PATTERNS):
            amplitudes = np.asarray(
                [sample.tensor_amplitudes[pattern_index] for sample in structures],
                dtype=complex,
            )
            covariance = np.einsum(
                "si,sj->ij", amplitudes, amplitudes.conj()
            ) / len(amplitudes)
            eigenvalues = np.linalg.eigvalsh(covariance)
            momentum = 2.0 * np.pi * np.asarray(pattern, dtype=float) / length
            divergence_symbol = 1.0 - np.exp(-1.0j * momentum)
            tensor_longitudinal_residuals.append(
                float(
                    np.linalg.norm(covariance @ divergence_symbol.conj())
                    / (
                        np.linalg.norm(covariance)
                        * np.linalg.norm(divergence_symbol)
                    )
                )
            )
            tensor_polarization_splits.append(
                float(
                    abs(eigenvalues[2] - eigenvalues[1])
                    / max(eigenvalues[2] + eigenvalues[1], 1.0e-15)
                )
            )
            tensor_weights.append(float(0.5 * (eigenvalues[1] + eigenvalues[2])))
        structure = StructureResult(
            longitudinal=float(
                np.mean([sample.longitudinal for sample in structures])
            ),
            transverse_first=float(
                np.mean([sample.transverse_first for sample in structures])
            ),
            transverse_second=float(
                np.mean([sample.transverse_second for sample in structures])
            ),
            transverse_split=float(np.mean(ensemble_splits)),
            tensor_longitudinal_residual=max(tensor_longitudinal_residuals),
            tensor_polarization_split=max(tensor_polarization_splits),
            tensor_weight_spread=float(
                (max(tensor_weights) - min(tensor_weights))
                / np.mean(tensor_weights)
            ),
        )
    else:
        structure = None
    return ChainResult(
        flippable_mean=flippable_mean,
        flippable_error=flippable_error,
        structure=structure,
        degree_signature=final_signature,
        electric_flux=final_flux,
    )


def encode_small(occupation: np.ndarray) -> int:
    encoded = 0
    for index, value in enumerate(occupation.ravel()):
        encoded |= int(value) << index
    return encoded


def decode_small(encoded: int) -> np.ndarray:
    return np.array(
        [(encoded >> index) & 1 for index in range(24)],
        dtype=np.uint8,
    ).reshape((2, 2, 2, 3))


def small_flip_destinations(occupation: np.ndarray) -> list[int]:
    length = 2
    destinations: list[int] = []
    for first_axis, second_axis in ORIENTATIONS:
        for root in product(range(length), repeat=3):
            root_list = list(root)
            first_neighbor = root_list.copy()
            first_neighbor[first_axis] = (
                first_neighbor[first_axis] + 1
            ) % length
            second_neighbor = root_list.copy()
            second_neighbor[second_axis] = (
                second_neighbor[second_axis] + 1
            ) % length
            links = (
                (*root, first_axis),
                (*first_neighbor, second_axis),
                (*second_neighbor, first_axis),
                (*root, second_axis),
            )
            values = [occupation[link] for link in links]
            if (
                values[0] == values[2]
                and values[1] == values[3]
                and values[0] != values[1]
            ):
                target = occupation.copy()
                for link in links:
                    target[link] ^= 1
                destinations.append(encode_small(target))
    return destinations


def enumerate_small_ice_sector() -> tuple[int, ...]:
    vertex_masks: list[int] = []
    for vertex in product(range(2), repeat=3):
        incident_indices = []
        for axis in range(3):
            outgoing = (*vertex, axis)
            incoming_vertex = list(vertex)
            incoming_vertex[axis] = (incoming_vertex[axis] - 1) % 2
            incoming = (*incoming_vertex, axis)
            incident_indices.extend(
                (
                    int(np.ravel_multi_index(outgoing, (2, 2, 2, 3))),
                    int(np.ravel_multi_index(incoming, (2, 2, 2, 3))),
                )
            )
        vertex_masks.append(sum(1 << index for index in incident_indices))

    allowed: list[int] = []
    for occupied_indices in combinations(range(24), 12):
        state = sum(1 << index for index in occupied_indices)
        if all((state & mask).bit_count() == 3 for mask in vertex_masks):
            allowed.append(state)
    return tuple(allowed)


@dataclass(frozen=True)
class RKOrbit:
    states: tuple[int, ...]
    hamiltonian: sparse.csr_matrix
    minimum_degree: int
    maximum_degree: int


def build_small_rk_orbit(
    start_occupation: np.ndarray | None = None,
) -> RKOrbit:
    if start_occupation is None:
        start_occupation = initial_ice(2)
    start = encode_small(start_occupation)
    queue = deque([start])
    states = [start]
    state_set = {start}
    while queue:
        state = queue.popleft()
        for destination in small_flip_destinations(decode_small(state)):
            if destination not in state_set:
                state_set.add(destination)
                states.append(destination)
                queue.append(destination)

    index = {state: position for position, state in enumerate(states)}
    rows: list[int] = []
    columns: list[int] = []
    data: list[float] = []
    degrees = []
    for state in states:
        row = index[state]
        destination_counts = Counter(
            small_flip_destinations(decode_small(state))
        )
        degree = sum(destination_counts.values())
        degrees.append(degree)
        rows.append(row)
        columns.append(row)
        data.append(float(degree))
        for destination, multiplicity in destination_counts.items():
            rows.append(row)
            columns.append(index[destination])
            data.append(float(-multiplicity))
    hamiltonian = sparse.coo_matrix(
        (data, (rows, columns)),
        shape=(len(states), len(states)),
        dtype=float,
    ).tocsr()
    return RKOrbit(
        states=tuple(states),
        hamiltonian=hamiltonian,
        minimum_degree=min(degrees),
        maximum_degree=max(degrees),
    )


def cubic_curl_spectrum(momentum: np.ndarray) -> np.ndarray:
    difference = np.exp(1.0j * momentum) - 1.0
    curl = np.array(
        (
            (0.0, -difference[2], difference[1]),
            (difference[2], 0.0, -difference[0]),
            (-difference[1], difference[0], 0.0),
        ),
        dtype=complex,
    )
    return np.linalg.eigvalsh(curl.conj().T @ curl)


def small_twisted_trial(orbit: RKOrbit) -> tuple[float, float, float]:
    """Actual L=2 phase-twisted vector: energy, variance, ground overlap.

    The supplied periodic Landau gauge has one flux quantum in the xy plane.
    The vector stays in the original electric component. Its energy is a
    trial expectation, not a magnetic-sector eigenvalue or a lower bound.
    """
    length = 2
    magnetic_phase = 2.0 * np.pi / length**2
    potential = np.zeros((length, length, length, 3))
    for x, y, z in product(range(length), repeat=3):
        potential[x, y, z, 1] = magnetic_phase * x
        if x == length - 1:
            potential[x, y, z, 0] = -magnetic_phase * length * y
    staggering = (-1.0) ** np.sum(np.indices((length,) * 3), axis=0)
    phases = []
    for encoded in orbit.states:
        electric = staggering[..., None] * (decode_small(encoded).astype(float) - 0.5)
        phases.append(np.exp(1.0j * float(np.sum(potential * electric))))
    trial = np.asarray(phases) / np.sqrt(len(orbit.states))
    applied = orbit.hamiltonian @ trial
    energy = float(np.vdot(trial, applied).real)
    variance = float(np.vdot(applied, applied).real - energy**2)
    ground_overlap = float(abs(np.sum(trial) / np.sqrt(len(orbit.states))) ** 2)
    return energy, variance, ground_overlap


def main() -> int:
    checks = Checks()

    initial_constraints_ok = True
    local_move_ok = True
    for length in (4, 6, 8):
        occupation = initial_ice(length)
        initial_constraints_ok = initial_constraints_ok and bool(
            np.all(vertex_degrees(occupation) == 3)
        )
        found_flip = False
        for first_axis, second_axis in ORIENTATIONS:
            mask = flippable_mask(occupation, first_axis, second_axis)
            locations = np.argwhere(mask)
            found_flip = found_flip or len(locations) > 0
            for location in locations:
                roots = np.zeros(mask.shape, dtype=np.uint8)
                root = tuple(int(value) for value in location)
                roots[root] = 1
                moved = occupation.copy()
                apply_root_flips(moved, first_axis, second_axis, roots)
                local_move_ok = local_move_ok and bool(
                    np.all(vertex_degrees(moved) == 3)
                    and electric_flux(moved) == electric_flux(occupation)
                    and np.count_nonzero(moved != occupation) == 4
                )
        local_move_ok = local_move_ok and found_flip
    checks.check(
        initial_constraints_ok,
        "one link qubit with three occupied links per cubic vertex realizes the exact ice Gauss sector",
    )
    checks.check(
        local_move_ok,
        "every tested alternating square move flips four qubits and preserves all vertex charges",
    )

    orbit = build_small_rk_orbit()
    small_sector = enumerate_small_ice_sector()
    small_zero_flux_sector = {
        state
        for state in small_sector
        if electric_flux(decode_small(state)) == (0, 0, 0)
    }
    mobile_small_sector = {
        state
        for state in small_zero_flux_sector
        if small_flip_destinations(decode_small(state))
    }
    frozen_small_sector = small_zero_flux_sector - mobile_small_sector
    orbit_constraint_ok = all(
        np.all(vertex_degrees(decode_small(state)) == 3)
        for state in orbit.states
    )
    checks.check(
        len(small_sector) == 9600
        and len(small_zero_flux_sector) == 880
        and len(frozen_small_sector) == 16
        and set(orbit.states) == mobile_small_sector
        and len(orbit.states) == 864
        and orbit.minimum_degree == 4
        and orbit.maximum_degree == 16
        and orbit_constraint_ok,
        "the full L=2 zero-flux sector is 864 connected mobile states plus 16 frozen states",
    )
    hermitian_residual = sparse.linalg.norm(
        orbit.hamiltonian - orbit.hamiltonian.T
    )
    equal_state = np.ones(len(orbit.states)) / np.sqrt(len(orbit.states))
    equal_residual = np.linalg.norm(orbit.hamiltonian @ equal_state)
    lowest = eigsh(
        orbit.hamiltonian,
        k=5,
        which="SA",
        v0=np.linspace(1.0, 2.0, len(orbit.states)),
        return_eigenvectors=False,
        tol=1.0e-12,
    )
    lowest = np.sort(lowest)
    checks.check(
        hermitian_residual < 1.0e-14
        and equal_residual < 1.0e-13
        and abs(lowest[0]) < 1.0e-12
        and lowest[1] > 0.1,
        "the RK graph Hamiltonian is positive with one exact equal-amplitude ground state on the connected orbit",
    )
    trial_energy, trial_variance, trial_overlap = small_twisted_trial(orbit)
    checks.check(
        abs(trial_energy - 8.0 / 3.0) < 1.0e-12
        and abs(trial_variance - 44.0 / 9.0) < 1.0e-12
        and abs(trial_overlap - 1.0 / 16.0) < 1.0e-12,
        "the actual L=2 twisted trial has the exact expectation, nonzero variance and nonzero RK-ground overlap",
    )

    vacuum_results: dict[int, ChainResult] = {}
    for length in (6, 8, 10, 12):
        vacuum_results[length] = run_chain(
            length,
            seed=90_300 + length,
            thermal_sweeps=500,
            sample_count=1600,
            sweep_stride=2,
            measure_structure=True,
        )
    replica_result = run_chain(
        12,
        seed=193_012,
        thermal_sweeps=500,
        sample_count=1600,
        sweep_stride=2,
        measure_structure=True,
    )
    checks.check(
        all(
            result.degree_signature == ((3, length**3),)
            and result.electric_flux == (0, 0, 0)
            for length, result in vacuum_results.items()
        ),
        "all deterministic Monte Carlo chains remain exactly inside their charge-free Gauss sectors",
    )
    checks.check(
        all(
            result.structure is not None
            and result.structure.longitudinal < 1.0e-24
            for result in vacuum_results.values()
        ),
        "the sampled electric structure factor has an exact longitudinal pinch-point zero",
    )

    transverse_splits = [
        result.structure.transverse_split
        for result in vacuum_results.values()
        if result.structure is not None
    ]
    checks.check(
        max(transverse_splits) < 0.08
        and transverse_splits[-1] < 0.06,
        "the two axial transverse structure-factor polarizations are ensemble-degenerate",
    )
    tensor_results = [
        result.structure
        for result in vacuum_results.values()
        if result.structure is not None
    ]
    checks.check(
        all(result.tensor_longitudinal_residual < 1.0e-12 for result in tensor_results)
        and all(result.tensor_polarization_split < 0.12 for result in tensor_results)
        and all(result.tensor_weight_spread < 0.12 for result in tensor_results)
        and tensor_results[-1].tensor_polarization_split < 0.10
        and tensor_results[-1].tensor_weight_spread < 0.10,
        "off-axis low-momentum covariance has one exact null and an isotropic transverse pair",
    )
    assert replica_result.structure is not None
    primary_density_12 = vacuum_results[12].flippable_mean / (3.0 * 12**3)
    replica_density_12 = replica_result.flippable_mean / (3.0 * 12**3)
    checks.check(
        replica_result.degree_signature == ((3, 12**3),)
        and replica_result.electric_flux == (0, 0, 0)
        and abs(replica_density_12 - primary_density_12) < 0.001
        and replica_result.structure.transverse_split < 0.08
        and replica_result.structure.tensor_longitudinal_residual < 1.0e-12
        and replica_result.structure.tensor_polarization_split < 0.12
        and replica_result.structure.tensor_weight_spread < 0.12,
        "an independent L=12 seed reproduces the Gauss, tensor, and flippability diagnostics",
    )
    scale_ratios = [
        result.structure.transverse_first
        / result.structure.transverse_second
        for result in vacuum_results.values()
        if result.structure is not None
    ]
    checks.check(
        all(0.85 < ratio < 1.15 for ratio in scale_ratios)
        and 0.90 < scale_ratios[-1] < 1.10,
        "the first two sampled momenta retain finite comparable transverse weight rather than a massive collapse",
    )

    charged_start = insert_defect_pair(initial_ice(2), 1)
    charged_signature = tuple(
        (int(degree), int(count))
        for degree, count in sorted(
            Counter(vertex_degrees(charged_start).ravel()).items()
        )
    )
    charged_orbit = build_small_rk_orbit(charged_start)
    charged_pattern = gauss_charges(charged_start)
    charged_constraint_ok = all(
        np.array_equal(gauss_charges(decode_small(state)), charged_pattern)
        for state in charged_orbit.states
    )
    charged_equal = np.ones(len(charged_orbit.states)) / np.sqrt(
        len(charged_orbit.states)
    )
    charged_residual = np.linalg.norm(
        charged_orbit.hamiltonian @ charged_equal
    )
    charged_lowest = np.sort(
        eigsh(
            charged_orbit.hamiltonian,
            k=3,
            which="SA",
            v0=np.linspace(1.0, 2.0, len(charged_orbit.states)),
            return_eigenvectors=False,
            tol=1.0e-12,
        )
    )
    checks.check(
        len(charged_orbit.states) > 100
        and sorted(charged_pattern[charged_pattern != 0]) == [-1, 1]
        and charged_constraint_ok
        and charged_residual < 1.0e-13
        and abs(charged_lowest[0]) < 1.0e-12
        and charged_lowest[1] > 0.1,
        "a fixed opposite-charge orbit has an exact equal-amplitude zero of the RK ring Hamiltonian",
    )

    flippability_density = {
        lattice_length: result.flippable_mean
        / (3.0 * lattice_length**3)
        for lattice_length, result in vacuum_results.items()
    }
    flippability_density_error = {
        lattice_length: result.flippable_error
        / (3.0 * lattice_length**3)
        for lattice_length, result in vacuum_results.items()
    }
    checks.check(
        all(0.22 < value < 0.32 for value in flippability_density.values())
        and abs(flippability_density[12] - flippability_density[6]) < 0.035,
        "the RK ensemble retains a positive size-stable density of magnetic ring moves",
    )
    threaded_flux_energy = {
        lattice_length: flippability_density[lattice_length]
        * lattice_length**3
        * (1.0 - np.cos(2.0 * np.pi / lattice_length**2))
        for lattice_length in vacuum_results
    }
    scaled_flux_ratio = {
        lattice_length: lattice_length * threaded_flux_energy[lattice_length]
        / (2.0 * np.pi**2 * flippability_density[lattice_length])
        for lattice_length in vacuum_results
    }
    checks.check(
        all(value > 0.0 for value in threaded_flux_energy.values())
        and all(0.995 < value < 1.001 for value in scaled_flux_ratio.values()),
        "the sampled-density trial formula has positive expectations and the declared finite 1/L ratios",
    )

    mode_count_ok = True
    for lattice_length in (4, 6, 8, 12):
        for indices in product(range(lattice_length), repeat=3):
            if indices == (0, 0, 0):
                continue
            momentum = (
                2.0 * np.pi * np.array(indices, dtype=float) / lattice_length
            )
            eigenvalues = cubic_curl_spectrum(momentum)
            expected = float(
                4.0 * np.sum(np.sin(0.5 * momentum) ** 2)
            )
            mode_count_ok = mode_count_ok and bool(
                abs(eigenvalues[0]) < 3.0e-12
                and abs(eigenvalues[1] - expected) < 3.0e-12
                and abs(eigenvalues[2] - expected) < 3.0e-12
            )
    infrared_ratios = []
    for lattice_length in (8, 16, 32, 64, 128):
        wave_number = 2.0 * np.pi / lattice_length
        probe = np.array((wave_number, 0.0, 0.0))
        frequency = np.sqrt(cubic_curl_spectrum(probe)[1])
        infrared_ratios.append(float(frequency / wave_number))
    infrared_ok = bool(
        all(
            infrared_ratios[index + 1] > infrared_ratios[index]
            for index in range(len(infrared_ratios) - 1)
        )
        and infrared_ratios[-1] > 0.9998
    )
    checks.check(
        mode_count_ok and infrared_ok,
        "the conditional positive-stiffness Maxwell kernel has exactly two linearly dispersing polarizations",
    )

    print("diagnostic RK orbit size:", len(orbit.states))
    print(
        "diagnostic actual L=2 twisted trial:",
        f"energy={trial_energy:.12f}",
        f"variance={trial_variance:.12f}",
        f"ground_overlap_squared={trial_overlap:.12f}",
    )
    print(
        "diagnostic full L=2 sector:",
        f"all_fluxes={len(small_sector)}",
        f"zero_flux={len(small_zero_flux_sector)}",
        f"mobile={len(mobile_small_sector)}",
        f"frozen={len(frozen_small_sector)}",
    )
    print(
        "diagnostic RK lowest eigenvalues:",
        " ".join(f"{value:.8e}" for value in lowest),
    )
    for lattice_length, result in vacuum_results.items():
        assert result.structure is not None
        print(
            f"diagnostic L={lattice_length} structure:",
            f"long={result.structure.longitudinal:.3e}",
            f"T1={result.structure.transverse_first:.6f}",
            f"T2={result.structure.transverse_second:.6f}",
            f"split={result.structure.transverse_split:.6f}",
            f"tensor_null={result.structure.tensor_longitudinal_residual:.3e}",
            f"tensor_split={result.structure.tensor_polarization_split:.6f}",
            f"tensor_spread={result.structure.tensor_weight_spread:.6f}",
        )
    print(
        "diagnostic independent L=12 replica:",
        f"density={replica_density_12:.6f}",
        f"split={replica_result.structure.transverse_split:.6f}",
        f"tensor_null={replica_result.structure.tensor_longitudinal_residual:.3e}",
        f"tensor_split={replica_result.structure.tensor_polarization_split:.6f}",
        f"tensor_spread={replica_result.structure.tensor_weight_spread:.6f}",
    )
    print(
        "diagnostic charged RK orbit:",
        f"states={len(charged_orbit.states)}",
        f"signature={charged_signature}",
        "lowest=" + " ".join(f"{value:.8e}" for value in charged_lowest),
    )
    print(
        "diagnostic flippability densities:",
        " ".join(
            f"L={length}:{flippability_density[length]:.6f}"
            f"+/-{flippability_density_error[length]:.6f}"
            for length in flippability_density
        ),
    )
    print(
        "diagnostic trial-formula L*E ratios:",
        " ".join(
            f"L={length}:{scaled_flux_ratio[length]:.8f}"
            for length in scaled_flux_ratio
        ),
    )
    print(
        "diagnostic infrared omega/|k| ratios:",
        " ".join(
            f"L={length}:{ratio:.8f}"
            for length, ratio in zip(
                (8, 16, 32, 64, 128), infrared_ratios
            )
        ),
    )
    print(
        "per_element: one occupation qubit per link and every four-link alternating plaquette move are checked"
    )
    print(
        "per_site: exact three-of-six Gauss constraints and a fixed opposite-charge sector are checked"
    )
    print(
        "per_mode: longitudinal pinch suppression, transverse weights, and conditional Maxwell polarizations are checked"
    )
    print(
        "per_block: the complete 864-state L=2 RK orbit and L=6 through L=12 Monte Carlo tori are checked"
    )
    print(
        "lattice_wide: finite tensor data and magnetic trial expectations are checked; renormalized stiffness and the thermodynamic phase are not proved"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
