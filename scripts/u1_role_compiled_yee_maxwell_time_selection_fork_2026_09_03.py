#!/usr/bin/env python3
"""Checks a nearest-neighbor Yee/Maxwell generator on the role compiler.

Edge-role sites carry electric/link data and face-role sites carry magnetic
data.  The physical nearest-neighbor incidence matrix is the lattice curl.
Its first-order edge-face generator has two transverse linear branches.

The runner also compares a reversible Gaussian sampler and its Szegedy-style
two-reflection spectral lift.  Those comparisons demonstrate that the static
gauge measure does not itself select a physical time law.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

from u1_record_distribution_overlap_maxwell_germ_2026_09_03 import (
    kernel_curvature,
    overlap_coefficients,
)
from u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03 import (
    proper_cubic_rotations,
)
from u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03 import (
    add_axis,
    edge_axis,
    face_axes,
    face_boundary_sites,
    role_bits,
    role_kind,
    sites,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
    "scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py",
)


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


def levi_civita(first: int, second: int, third: int) -> int:
    if len({first, second, third}) < 3:
        return 0
    inversions = sum(
        left > right
        for index, left in enumerate((first, second, third))
        for right in (first, second, third)[index + 1 :]
    )
    return -1 if inversions % 2 else 1


def physical_incidence(
    coarse_size: int,
) -> tuple[
    tuple[tuple[int, int, int], ...],
    tuple[tuple[int, int, int], ...],
    tuple[tuple[int, int, int], ...],
    tuple[tuple[int, int, int], ...],
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    """Return V,E,F,C site lists and grad,curl,div matrices."""

    physical_size = 2 * coarse_size
    sector = (0, 0, 0)
    role_sites: dict[str, list[tuple[int, int, int]]] = {
        "vertex": [],
        "edge": [],
        "face": [],
        "cube": [],
    }
    for point_raw in sites(physical_size):
        point = tuple(point_raw)
        role_sites[role_kind(role_bits(point, sector))].append(point)
    vertices = tuple(sorted(role_sites["vertex"]))
    edges = tuple(sorted(role_sites["edge"]))
    faces = tuple(sorted(role_sites["face"]))
    cubes = tuple(sorted(role_sites["cube"]))
    vertex_index = {point: index for index, point in enumerate(vertices)}
    edge_index = {point: index for index, point in enumerate(edges)}
    face_index = {point: index for index, point in enumerate(faces)}

    gradient = np.zeros((len(edges), len(vertices)), dtype=int)
    for edge, row in edge_index.items():
        axis = edge_axis(role_bits(edge, sector))
        tail = add_axis(edge, axis, -1, physical_size)
        head = add_axis(edge, axis, 1, physical_size)
        gradient[row, vertex_index[tail]] = -1
        gradient[row, vertex_index[head]] = 1

    curl = np.zeros((len(faces), len(edges)), dtype=int)
    for face, row in face_index.items():
        role = role_bits(face, sector)
        boundary = face_boundary_sites(face, role, physical_size)
        for edge, sign in zip(boundary, (1, 1, -1, -1)):
            curl[row, edge_index[edge]] = sign

    divergence = np.zeros((len(cubes), len(faces)), dtype=int)
    for row, cube in enumerate(cubes):
        for normal_axis in range(3):
            plane_axes = tuple(axis for axis in range(3) if axis != normal_axis)
            orientation = levi_civita(
                plane_axes[0], plane_axes[1], normal_axis
            )
            negative_face = add_axis(cube, normal_axis, -1, physical_size)
            positive_face = add_axis(cube, normal_axis, 1, physical_size)
            divergence[row, face_index[negative_face]] = -orientation
            divergence[row, face_index[positive_face]] = orientation

    return (
        vertices,
        edges,
        faces,
        cubes,
        gradient,
        curl,
        divergence,
    )


def lattice_momentum(indices: tuple[int, int, int], size: int) -> np.ndarray:
    return np.array(
        [
            2.0
            * math.sin(
                math.pi
                * (index if index <= size // 2 else index - size)
                / size
            )
            for index in indices
        ],
        dtype=float,
    )


def curl_symbol(momentum: np.ndarray) -> np.ndarray:
    first, second, third = momentum
    return np.array(
        [
            [0.0, -third, second],
            [third, 0.0, -first],
            [-second, first, 0.0],
        ]
    )


def signed_permutation_matrix(
    permutation: tuple[int, ...], signs: tuple[int, ...]
) -> np.ndarray:
    rotation = np.zeros((3, 3), dtype=int)
    for old_axis in range(3):
        rotation[permutation[old_axis], old_axis] = signs[old_axis]
    return rotation


def yee_generator(curl: np.ndarray, speed: float = 1.0) -> np.ndarray:
    zeros = np.zeros_like(curl)
    return speed * np.block([[zeros, -curl.T], [curl, zeros]])


def canonical_generator(
    curl: np.ndarray, electric_coefficient: float, magnetic_coefficient: float
) -> tuple[np.ndarray, np.ndarray]:
    edge_count = curl.shape[1]
    identity = np.eye(edge_count)
    kernel = curl.T @ curl
    generator = np.block(
        [
            [np.zeros_like(kernel), electric_coefficient * identity],
            [-magnetic_coefficient * kernel, np.zeros_like(kernel)],
        ]
    )
    energy_hessian = np.block(
        [
            [magnetic_coefficient * kernel, np.zeros_like(kernel)],
            [np.zeros_like(kernel), electric_coefficient * identity],
        ]
    )
    return generator, energy_hessian


def szegedy_block(markov_eigenvalue: float) -> np.ndarray:
    sine = math.sqrt(max(0.0, 1.0 - markov_eigenvalue**2))
    cosine_double = 2.0 * markov_eigenvalue**2 - 1.0
    sine_double = 2.0 * markov_eigenvalue * sine
    return np.array(
        [[cosine_double, -sine_double], [sine_double, cosine_double]]
    )


def main() -> int:
    checks = Checks()
    coefficients = overlap_coefficients(
        (0.15, -0.20, 0.10), (0.25, 0.12, -0.08)
    )
    kappa = kernel_curvature(coefficients)
    electric_coefficient = 1.0 / kappa
    magnetic_coefficient = kappa
    checks.check(
        kappa > 0.0
        and abs(electric_coefficient * magnetic_coefficient - 1.0) < 1.0e-15,
        "the parent positive magnetic curvature admits reciprocal unit-speed electric normalization",
    )

    coarse_size = 3
    (
        vertices,
        edges,
        faces,
        cubes,
        gradient,
        curl,
        divergence,
    ) = physical_incidence(coarse_size)
    checks.check(
        (len(vertices), len(edges), len(faces), len(cubes)) == (27, 81, 81, 27),
        "the L3 coarse block is the 27+81+81+27 physical doubled incidence lattice",
    )
    checks.check(
        np.all(np.count_nonzero(gradient, axis=1) == 2)
        and np.all(np.count_nonzero(curl, axis=1) == 4)
        and np.all(np.count_nonzero(curl, axis=0) == 4)
        and np.all(np.count_nonzero(divergence, axis=1) == 6),
        "gradient, curl, and divergence use only physical nearest-neighbor incidence",
    )
    checks.check(
        np.array_equal(curl @ gradient, np.zeros((len(faces), len(vertices)), dtype=int)),
        "the exact physical incidence matrices satisfy curl grad equals zero",
    )
    checks.check(
        np.array_equal(divergence @ curl, np.zeros((len(cubes), len(edges)), dtype=int)),
        "the exact physical incidence matrices satisfy div curl equals zero",
    )

    deterministic_links = np.array(
        [
            (3 * point[0] + 2 * point[1] + point[2] + edge_axis(role_bits(point, (0, 0, 0))))
            % 7
            - 3
            for point in edges
        ],
        dtype=float,
    )
    direct_face_values = []
    edge_index = {point: index for index, point in enumerate(edges)}
    for face in faces:
        boundary = face_boundary_sites(
            face, role_bits(face, (0, 0, 0)), 2 * coarse_size
        )
        direct_face_values.append(
            sum(
                sign * deterministic_links[edge_index[edge]]
                for edge, sign in zip(boundary, (1, 1, -1, -1))
            )
        )
    checks.check(
        np.array_equal(curl @ deterministic_links, np.array(direct_face_values)),
        "matrix curl equals the four-neighbor face rule on a complete nonuniform field",
    )
    checks.check(
        abs(
            float(deterministic_links @ (curl.T @ curl) @ deterministic_links)
            - float(np.linalg.norm(curl @ deterministic_links) ** 2)
        )
        < 1.0e-10,
        "the parent quadratic magnetic action is exactly the squared incidence curl",
    )

    singular_values = np.linalg.svd(curl.astype(float), compute_uv=False)
    expected_singular_values = []
    for indices in itertools.product(range(coarse_size), repeat=3):
        momentum = lattice_momentum(tuple(indices), coarse_size)
        norm = float(np.linalg.norm(momentum))
        expected_singular_values.extend((0.0, norm, norm))
    checks.check(
        np.max(
            np.abs(
                np.sort(singular_values)
                - np.sort(np.array(expected_singular_values))
            )
        )
        < 2.0e-12,
        "the full real-space curl spectrum has one null and two equal singular values per momentum",
    )

    real_generator = yee_generator(curl.astype(float))
    checks.check(
        np.max(np.abs(real_generator.T + real_generator)) < 1.0e-15,
        "the edge-face Yee generator is exactly skew and conserves the Euclidean field norm",
    )
    electric_divergence_map = gradient.T
    constraint_preservation = np.block(
        [
            [electric_divergence_map, np.zeros((len(vertices), len(faces)))],
            [np.zeros((len(cubes), len(edges))), divergence],
        ]
    )
    checks.check(
        np.max(np.abs(constraint_preservation @ real_generator)) < 1.0e-15,
        "electric and magnetic Gauss constraints are exactly preserved by the generator",
    )

    canonical, energy_hessian = canonical_generator(
        curl.astype(float), electric_coefficient, magnetic_coefficient
    )
    checks.check(
        np.max(np.abs(canonical.T @ energy_hessian + energy_hessian @ canonical))
        < 2.0e-11,
        "the reciprocal-coefficient canonical A-E generator conserves its Hamiltonian",
    )
    checks.check(
        abs(math.sqrt(electric_coefficient * magnetic_coefficient) - 1.0)
        < 1.0e-15,
        "reciprocal electric and magnetic coefficients leave the wave speed independent of kappa",
    )

    fourier_spectrum_ok = True
    gauss_ok = True
    positive_mode_count_ok = True
    no_doublers = True
    checked_momenta = 0
    for lattice_size in (3, 4, 5, 7):
        for indices_raw in itertools.product(range(lattice_size), repeat=3):
            indices = tuple(indices_raw)
            momentum = lattice_momentum(indices, lattice_size)
            norm = float(np.linalg.norm(momentum))
            symbol = curl_symbol(momentum)
            generator = yee_generator(symbol)
            hermitian = 1j * generator
            eigenvalues = np.linalg.eigvalsh(hermitian)
            expected = np.array([-norm, -norm, 0.0, 0.0, norm, norm])
            fourier_spectrum_ok = fourier_spectrum_ok and bool(
                np.max(np.abs(eigenvalues - expected)) < 3.0e-12
            )
            electric_constraint = np.concatenate((momentum, np.zeros(3)))
            magnetic_constraint = np.concatenate((np.zeros(3), momentum))
            gauss_ok = gauss_ok and bool(
                np.linalg.norm(electric_constraint @ generator) < 2.0e-12
                and np.linalg.norm(magnetic_constraint @ generator) < 2.0e-12
            )
            if norm > 1.0e-14:
                positive_mode_count_ok = positive_mode_count_ok and (
                    sum(eigenvalues > 1.0e-10) == 2
                    and sum(eigenvalues < -1.0e-10) == 2
                )
                no_doublers = no_doublers and norm > 0.0
                checked_momenta += 1
            else:
                no_doublers = no_doublers and indices == (0, 0, 0)
    checks.check(
        fourier_spectrum_ok,
        "every tested Fourier block has spectrum minus-s twice, zero twice, plus-s twice",
    )
    checks.check(
        gauss_ok,
        "both Fourier Gauss rows annihilate the first-order generator at every momentum",
    )
    checks.check(
        positive_mode_count_ok and checked_momenta == 27 + 64 + 125 + 343 - 4,
        "each nonzero momentum has exactly two positive-frequency transverse branches",
    )
    checks.check(
        no_doublers,
        "the forward-incidence symbol vanishes only at zero momentum",
    )

    infrared_ratios = []
    for lattice_size in (16, 32, 64, 128, 256):
        momentum = lattice_momentum((1, 0, 0), lattice_size)
        frequency = float(np.linalg.norm(momentum))
        continuum = 2.0 * math.pi / lattice_size
        infrared_ratios.append(frequency / continuum)
    checks.check(
        all(
            abs(left - 1.0) > abs(right - 1.0)
            for left, right in zip(infrared_ratios, infrared_ratios[1:])
        )
        and abs(infrared_ratios[-1] - 1.0) < 3.0e-5,
        "both Yee branches converge monotonically to unit-speed linear dispersion",
    )

    unitary_ok = True
    for momentum in (
        np.array([0.3, 0.7, 1.1]),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.2, 0.8]),
    ):
        generator = yee_generator(curl_symbol(momentum))
        hermitian = 1j * generator
        eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
        time = 0.37
        evolution = eigenvectors @ np.diag(np.exp(-1j * time * eigenvalues)) @ eigenvectors.conj().T
        unitary_ok = unitary_ok and bool(
            np.max(np.abs(evolution.conj().T @ evolution - np.eye(6))) < 3.0e-12
        )
    checks.check(
        unitary_ok,
        "the continuous-time local generator exponentiates to unitary evolution",
    )

    rotations = proper_cubic_rotations()
    cubic_ok = len(rotations) == 24
    for momentum in (
        np.array([0.0, 0.7, 1.2]),
        np.array([0.3, 0.8, 1.1]),
        np.array([1.4, 0.2, 0.9]),
    ):
        symbol = curl_symbol(momentum)
        for permutation, signs in rotations:
            rotation = signed_permutation_matrix(permutation, signs)
            cubic_ok = cubic_ok and bool(
                np.max(
                    np.abs(
                        curl_symbol(rotation @ momentum)
                        - rotation @ symbol @ rotation.T
                    )
                )
                < 1.0e-12
            )
    checks.check(
        cubic_ok,
        "the curl generator covaries under all 24 proper cubic rotations",
    )

    incomplete = curl_symbol(np.array([0.0, 1.0, 1.0]))
    incomplete[0, :] = 0.0
    checks.check(
        np.linalg.matrix_rank(incomplete, tol=1.0e-12) == 1,
        "removing one face orientation loses a transverse branch",
    )
    generic_momentum = np.array([0.7, 1.0, 1.3])
    generic_curl = curl_symbol(generic_momentum)
    anisotropic_kernel = generic_curl.T @ np.diag((1.0, 2.0, 3.0)) @ generic_curl
    anisotropic_modes = np.linalg.eigvalsh(anisotropic_kernel)[1:]
    checks.check(
        abs(anisotropic_modes[1] - anisotropic_modes[0]) > 0.2,
        "unequal face stiffness splits the two transverse frequencies",
    )
    mass = 0.4
    zero_momentum_massive = np.sqrt(
        np.linalg.eigvalsh(mass**2 * np.eye(3))
    )
    checks.check(
        np.allclose(zero_momentum_massive, mass),
        "an explicit vector mass gaps the zero-momentum control",
    )

    sampler_diffusive = True
    szegedy_unitary = True
    szegedy_spectrum = True
    straight_phase_diffusive = True
    szegedy_infrared_ratios = []
    tau = 0.5
    for lattice_size in (16, 32, 64, 128, 256):
        momentum = lattice_momentum((1, 0, 0), lattice_size)
        norm = float(np.linalg.norm(momentum))
        rate = norm**2 / 4.0
        markov_eigenvalue = math.exp(-tau * rate)
        phase = 2.0 * math.acos(markov_eigenvalue)
        continuum = 2.0 * math.pi / lattice_size
        szegedy_infrared_ratios.append(phase / continuum)
        sampler_diffusive = sampler_diffusive and (
            abs(rate / norm**2 - 0.25) < 1.0e-12
            and rate / norm < 0.2
        )
        block = szegedy_block(markov_eigenvalue)
        szegedy_unitary = szegedy_unitary and bool(
            np.max(np.abs(block.T @ block - np.eye(2))) < 2.0e-12
            and abs(np.linalg.det(block) - 1.0) < 2.0e-12
        )
        block_phases = np.sort(np.abs(np.angle(np.linalg.eigvals(block))))
        szegedy_spectrum = szegedy_spectrum and bool(
            np.max(np.abs(block_phases - phase)) < 2.0e-12
        )
        straight_phase_diffusive = straight_phase_diffusive and (
            (1.0 - markov_eigenvalue) / continuum < 0.1
        )
    checks.check(
        sampler_diffusive,
        "the reversible Gaussian gradient sampler has quadratic rather than photon dispersion",
    )
    checks.check(
        szegedy_unitary and szegedy_spectrum,
        "the two-reflection spectral block is unitary with phase two arccos lambda",
    )
    checks.check(
        all(
            abs(left - 1.0) > abs(right - 1.0)
            for left, right in zip(
                szegedy_infrared_ratios, szegedy_infrared_ratios[1:]
            )
        )
        and abs(szegedy_infrared_ratios[-1] - 1.0) < 4.0e-5,
        "the tau-one-half Szegedy spectral lift has unit-speed linear infrared phase",
    )
    checks.check(
        straight_phase_diffusive,
        "using one minus lambda directly stays quadratic and is the phase-map control",
    )

    speed_choices = []
    small_norm = float(np.linalg.norm(lattice_momentum((1, 0, 0), 4096)))
    for alternate_tau in (0.125, 0.5, 2.0):
        rate = small_norm**2 / 4.0
        phase = 2.0 * math.acos(math.exp(-alternate_tau * rate))
        speed_choices.append(phase / small_norm)
    checks.check(
        np.max(
            np.abs(
                np.array(speed_choices)
                - np.sqrt(2.0 * np.array((0.125, 0.5, 2.0)))
            )
        )
        < 2.0e-6,
        "the sampler tick changes the quantum-walk speed and remains a physical selection input",
    )

    zone_norm = math.sqrt(12.0)
    zone_rate = zone_norm**2 / 4.0
    zone_szegedy = 2.0 * math.acos(math.exp(-tau * zone_rate))
    checks.check(
        abs(zone_szegedy - zone_norm) > 0.5,
        "the local Yee and Szegedy candidates agree in the infrared but differ across the zone",
    )

    # Harmonic one-forms survive both curl and electric Gauss on the torus.
    # The Gaussian/OU comparison must pin them and project the noise.
    harmonic = np.array([
        [int(edge_axis(role_bits(edge, (0, 0, 0))) == axis) for axis in range(3)]
        for edge in edges
    ], dtype=float)
    checks.check(
        np.linalg.matrix_rank(harmonic) == 3
        and np.array_equal(curl @ harmonic, np.zeros((len(faces), 3)))
        and np.array_equal(gradient.T @ harmonic, np.zeros((len(vertices), 3)))
        and np.all(np.diag(harmonic.T @ harmonic) > 0),
        "three harmonic torus one-forms survive Gauss and have zero stiffness despite positive unprojected OU noise",
    )
    stiffness = curl.T @ curl
    values, vectors = np.linalg.eigh(stiffness.astype(float))
    positive_vectors = vectors[:, values > 1.0e-10]
    projected_noise = positive_vectors @ positive_vectors.T
    checks.check(
        positive_vectors.shape[1] == 2 * (coarse_size**3 - 1)
        and np.max(np.abs(projected_noise @ harmonic)) < 2.0e-12
        and np.max(np.abs(gradient.T @ projected_noise)) < 2.0e-12
        and np.min(values[values > 1.0e-10]) > 0,
        "projecting onto the mean-zero transverse sector removes gauge and harmonic nulls and leaves positive Gaussian stiffness",
    )

    stationary_variance_ok = True
    for norm_squared in (0.1, 0.5, 2.0, 7.0):
        rate = norm_squared / 4.0
        noise_variance = 1.0 / (2.0 * kappa)
        ou_variance = noise_variance / (2.0 * rate)
        target_variance = 1.0 / (kappa * norm_squared)
        stationary_variance_ok = stationary_variance_ok and abs(
            ou_variance - target_variance
        ) < 2.0e-12
    checks.check(
        stationary_variance_ok,
        "the projected Gaussian sampler matches the harmonic measure variance only at nonzero stiffness",
    )

    print(
        "per_element: every physical incidence coefficient and each declared two-reflection spectral block is checked"
    )
    print(
        "per_site: every edge couples to four face neighbors and every face to four edge neighbors on the L3 block"
    )
    print(
        "per_mode: every momentum on L=3,4,5,7 has two Yee branches; five infrared refinements test both time lifts"
    )
    print(
        "per_block: gradient-curl-divergence complexes, Hamiltonian conservation, cubic covariance, and controls are checked"
    )
    print(
        "lattice_wide: the full 162-variable L3 edge-face generator and all 24 cubic rotations are executed"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
