#!/usr/bin/env python3
"""Checks for a conserved source bridge into the local Maxwell photon tick.

Charge lives on vertex roles and current on edge roles.  With the incidence
orientation used by the light stack, rho' = rho + h d0^T J and the sourced
electric shear E' = E - h C^T B + h J preserve Gauss exactly.  Static
minimum-energy fields give the cubic-lattice Coulomb Green function, while
the Hodge-transverse current sector couples to the two photon branches.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

from u1_local_reversible_yee_leapfrog_tick_2026_09_03 import (
    all_cubic_transformations,
    leapfrog_tick,
    magnetic_shear,
    periodic_l1,
)
from u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03 import (
    curl_symbol,
    physical_incidence,
)


AUDIT_TIMEOUT_SEC = 120

# Actual helper closure plus the declared conditional premise/context closure.
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/U1_CONSERVED_VERTEX_CHARGE_EDGE_CURRENT_COULOMB_PHOTON_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
    "scripts/u1_radius_one_onsite_unitary_maxwell_obstruction_2026_09_03.py",
    "scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py",
    "scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
    "scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py",
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


def sourced_tick(
    curl: np.ndarray,
    electric: np.ndarray,
    magnetic: np.ndarray,
    current: np.ndarray,
    step: float,
) -> tuple[np.ndarray, np.ndarray]:
    magnetic_half = magnetic + 0.5 * step * curl @ electric
    electric_new = electric - step * curl.T @ magnetic_half + step * current
    magnetic_new = magnetic_half + 0.5 * step * curl @ electric_new
    return electric_new, magnetic_new


def lattice_laplacian(field: np.ndarray) -> np.ndarray:
    result = 6.0 * field
    for axis in range(3):
        result = result - np.roll(field, 1, axis=axis) - np.roll(field, -1, axis=axis)
    return result


def torus_green(size: int) -> np.ndarray:
    momenta = 2.0 * math.pi * np.fft.fftfreq(size)
    eigenvalues = 4.0 * (
        np.sin(0.5 * momenta[:, None, None]) ** 2
        + np.sin(0.5 * momenta[None, :, None]) ** 2
        + np.sin(0.5 * momenta[None, None, :]) ** 2
    )
    inverse = np.zeros_like(eigenvalues)
    inverse[eigenvalues > 1.0e-14] = 1.0 / eigenvalues[eigenvalues > 1.0e-14]
    return np.fft.ifftn(inverse).real


def fit_coulomb_coefficient(green: np.ndarray) -> tuple[float, float, float]:
    size = green.shape[0]
    radii = np.arange(4, size // 5, dtype=float)
    values = green[radii.astype(int), 0, 0]
    design = np.column_stack((1.0 / radii, np.ones_like(radii), 1.0 / radii**3))
    coefficient, offset, lattice_correction = np.linalg.lstsq(
        design, values, rcond=None
    )[0]
    return float(coefficient), float(offset), float(lattice_correction)


def source_symbol_tick(
    momentum: np.ndarray,
    electric: np.ndarray,
    magnetic: np.ndarray,
    current: np.ndarray,
    step: float,
) -> tuple[np.ndarray, np.ndarray]:
    return sourced_tick(curl_symbol(momentum), electric, magnetic, current, step)


def main() -> int:
    checks = Checks()
    (
        vertices,
        edges,
        faces,
        cubes,
        gradient,
        curl_integer,
        divergence,
    ) = physical_incidence(3)
    curl = curl_integer.astype(float)
    checks.check(
        np.array_equal(curl_integer @ gradient, np.zeros((81, 27), dtype=int))
        and np.array_equal(divergence @ curl_integer, np.zeros((27, 81), dtype=int)),
        "the source bridge uses the exact vertex-edge-face-cube incidence complex",
    )

    # Exact rational h=1/2 sourced update.  B_half has denominator 4,
    # E_new denominator 8, and B_new denominator 32.
    electric_integer = np.array(
        [(7 * index + 3) % 11 - 5 for index in range(len(edges))], dtype=np.int64
    )
    potential_integer = np.array(
        [(5 * index + 1) % 9 - 4 for index in range(len(edges))], dtype=np.int64
    )
    magnetic_integer = curl_integer @ potential_integer
    current_integer = np.array(
        [(3 * index + 2) % 7 - 3 for index in range(len(edges))], dtype=np.int64
    )
    charge_integer = gradient.T @ electric_integer
    magnetic_half_numerator = 4 * magnetic_integer + curl_integer @ electric_integer
    electric_new_numerator = (
        8 * electric_integer
        - curl_integer.T @ magnetic_half_numerator
        + 4 * current_integer
    )
    magnetic_new_numerator = (
        8 * magnetic_half_numerator + curl_integer @ electric_new_numerator
    )
    charge_new_numerator = 2 * charge_integer + gradient.T @ current_integer
    checks.check(
        np.array_equal(
            gradient.T @ electric_new_numerator,
            4 * charge_new_numerator,
        ),
        "the electric Gauss law and discrete continuity equation agree exactly over integers",
    )
    checks.check(
        np.array_equal(
            divergence @ magnetic_half_numerator,
            np.zeros(len(cubes), dtype=np.int64),
        )
        and np.array_equal(
            divergence @ magnetic_new_numerator,
            np.zeros(len(cubes), dtype=np.int64),
        ),
        "magnetic Gauss remains exact during both sourced magnetic half-steps",
    )
    checks.check(
        int(np.sum(charge_new_numerator)) == 0
        and int(np.sum(charge_integer)) == 0,
        "incidence continuity conserves total charge on the periodic lattice",
    )

    # Exercise the actual implementation against the independently expanded
    # rational numerators above. Binary denominators make these comparisons
    # exact; the old integer-only calculation did not test sourced_tick.
    actual_electric, actual_magnetic = sourced_tick(
        curl,
        electric_integer.astype(float),
        magnetic_integer.astype(float),
        current_integer.astype(float),
        0.5,
    )
    actual_half = actual_magnetic - 0.25 * curl @ actual_electric
    checks.check(
        np.array_equal(8 * actual_electric, electric_new_numerator)
        and np.array_equal(32 * actual_magnetic, magnetic_new_numerator)
        and np.array_equal(4 * actual_half, magnetic_half_numerator)
        and np.array_equal(2 * gradient.T @ actual_electric, charge_new_numerator)
        and np.array_equal(divergence @ actual_half, np.zeros(len(cubes)))
        and np.array_equal(divergence @ actual_magnetic, np.zeros(len(cubes))),
        "the actual nonzero-current tick matches independent full-field rational numerators and all Gauss rows",
    )

    step = 0.5
    electric = electric_integer.astype(float)
    magnetic = magnetic_integer.astype(float)
    zero_current = np.zeros(len(edges))
    source_free_electric, source_free_magnetic = sourced_tick(
        curl, electric, magnetic, zero_current, step
    )
    parent_tick = leapfrog_tick(curl, step) @ np.concatenate((electric, magnetic))
    checks.check(
        np.max(
            np.abs(
                np.concatenate((source_free_electric, source_free_magnetic))
                - parent_tick
            )
        )
        < 1.0e-13,
        "zero current reduces exactly to the parent finite-depth photon tick",
    )

    vertex_index = {point: index for index, point in enumerate(vertices)}
    edge_index = {point: index for index, point in enumerate(edges)}
    tail = vertices[0]
    physical_size = 6
    head = ((tail[0] + 2) % physical_size, tail[1], tail[2])
    midpoint = ((tail[0] + 1) % physical_size, tail[1], tail[2])
    spectator = vertices[len(vertices) // 2]
    old_charge = np.zeros(len(vertices))
    old_charge[vertex_index[tail]] = 1.0
    old_charge[vertex_index[spectator]] = -1.0
    unit_current = np.zeros(len(edges))
    unit_current[edge_index[midpoint]] = 1.0 / step
    new_charge = old_charge + step * gradient.T @ unit_current
    expected_charge = np.zeros(len(vertices))
    expected_charge[vertex_index[head]] = 1.0
    expected_charge[vertex_index[spectator]] = -1.0
    checks.check(
        np.array_equal(new_charge, expected_charge),
        "one oriented edge current transports one unit charge to its neighboring vertex exactly",
    )
    impulse_electric, impulse_magnetic = sourced_tick(
        curl, np.zeros(len(edges)), np.zeros(len(faces)), unit_current, step
    )
    charge_difference = expected_charge - old_charge
    checks.check(
        np.array_equal(impulse_electric, step * unit_current)
        and np.array_equal(gradient.T @ impulse_electric, charge_difference)
        and np.array_equal(impulse_magnetic, (step**2 / 2) * curl @ unit_current)
        and np.max(np.abs(gradient.T @ (2 * impulse_electric) - charge_difference)) == 1,
        "the actual one-edge source coefficient is one and doubling it fails charged Gauss",
    )

    laplacian = gradient.T @ gradient
    potential = np.linalg.pinv(laplacian.astype(float), rcond=1.0e-13) @ old_charge
    coulomb_electric = gradient @ potential
    checks.check(
        np.max(np.abs(gradient.T @ coulomb_electric - old_charge)) < 2.0e-13
        and abs(float(np.mean(potential))) < 2.0e-14,
        "the finite-torus Poisson solve reconstructs the neutral Gauss field",
    )

    deterministic_face = np.array(
        [(11 * index + 4) % 13 - 6 for index in range(len(faces))], dtype=float
    )
    divergence_free_variation = curl.T @ deterministic_face
    base_energy = 0.5 * float(coulomb_electric @ coulomb_electric)
    varied_energy = 0.5 * float(
        (coulomb_electric + divergence_free_variation)
        @ (coulomb_electric + divergence_free_variation)
    )
    checks.check(
        abs(float(coulomb_electric @ divergence_free_variation)) < 2.0e-11
        and varied_energy > base_energy + 1.0,
        "the Poisson field is orthogonal to curl variations and minimizes electric energy",
    )

    green_sizes = (48, 64, 96, 128)
    coulomb_coefficients = []
    poisson_ok = True
    cubic_green_ok = True
    zero_mean_ok = True
    for size in green_sizes:
        green = torus_green(size)
        source = np.zeros_like(green)
        source[0, 0, 0] = 1.0
        source -= 1.0 / size**3
        poisson_ok = poisson_ok and bool(
            np.max(np.abs(lattice_laplacian(green) - source)) < 2.0e-12
        )
        zero_mean_ok = zero_mean_ok and abs(float(np.mean(green))) < 2.0e-17
        radii = range(1, size // 5)
        cubic_green_ok = cubic_green_ok and all(
            abs(green[radius, 0, 0] - green[0, radius, 0]) < 2.0e-15
            and abs(green[radius, 0, 0] - green[0, 0, radius]) < 2.0e-15
            for radius in radii
        )
        coefficient, _offset, _correction = fit_coulomb_coefficient(green)
        coulomb_coefficients.append(coefficient)
    checks.check(
        poisson_ok and zero_mean_ok,
        "each FFT Green function solves the neutralized cubic Poisson equation",
    )
    checks.check(
        cubic_green_ok,
        "the lattice Coulomb Green function agrees on all three coordinate axes",
    )
    continuum_coefficient = 1.0 / (4.0 * math.pi)
    relative_errors = tuple(
        abs(value / continuum_coefficient - 1.0)
        for value in coulomb_coefficients
    )
    checks.check(
        all(left > right for left, right in zip(relative_errors, relative_errors[1:]))
        and relative_errors[-1] < 0.009,
        "fitted Green coefficient errors decrease across the named ladder toward 1/(4 pi)",
    )

    # Exact Hodge separation of source currents.
    vertex_profile = np.array(
        [(index * 7 + 1) % 10 - 4 for index in range(len(vertices))], dtype=float
    )
    longitudinal_current = gradient @ vertex_profile
    face_profile = np.array(
        [(index * 5 + 2) % 12 - 5 for index in range(len(faces))], dtype=float
    )
    transverse_current = curl.T @ face_profile
    checks.check(
        np.max(np.abs(curl @ longitudinal_current)) < 1.0e-13
        and np.linalg.norm(gradient.T @ longitudinal_current) > 1.0,
        "a gradient current changes charge but has exactly zero transverse curl",
    )
    checks.check(
        np.max(np.abs(gradient.T @ transverse_current)) < 1.0e-13
        and np.linalg.norm(curl @ transverse_current) > 1.0,
        "a co-curl current is charge-neutral and couples nontrivially to photon fields",
    )
    checks.check(
        abs(float(longitudinal_current @ transverse_current)) < 2.0e-11,
        "longitudinal Coulomb and transverse photon source sectors are orthogonal",
    )

    transverse_rank_ok = True
    source_projection_ok = True
    for momentum in (
        np.array([0.3, 0.7, 1.1]),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.8, 1.2, 0.4]),
    ):
        norm_squared = float(momentum @ momentum)
        longitudinal_projector = np.outer(momentum, momentum) / norm_squared
        transverse_projector = np.eye(3) - longitudinal_projector
        transverse_rank_ok = transverse_rank_ok and (
            np.linalg.matrix_rank(transverse_projector, tol=1.0e-12) == 2
        )
        symbol = curl_symbol(momentum)
        source_projection_ok = source_projection_ok and bool(
            np.max(np.abs(symbol @ longitudinal_projector)) < 2.0e-12
            and np.max(
                np.abs(symbol @ transverse_projector - symbol)
            )
            < 2.0e-12
        )
    checks.check(
        transverse_rank_ok and source_projection_ok,
        "the Fourier source split leaves exactly two curl-coupled transverse components",
    )

    # An impulse cannot outrun the finite-depth local layers.
    (
        _vertices5,
        edges5,
        faces5,
        _cubes5,
        _gradient5,
        curl5_integer,
        _divergence5,
    ) = physical_incidence(5)
    curl5 = curl5_integer.astype(float)
    impulse = np.zeros(len(edges5))
    impulse[0] = 1.0
    electric5 = np.zeros(len(edges5))
    magnetic5 = np.zeros(len(faces5))
    electric5, magnetic5 = sourced_tick(
        curl5, electric5, magnetic5, impulse, step
    )
    field_sites5 = edges5 + faces5
    source_site = edges5[0]
    support_one = np.flatnonzero(
        np.abs(np.concatenate((electric5, magnetic5))) > 1.0e-13
    )
    max_distance_one = max(
        periodic_l1(source_site, field_sites5[index], 10)
        for index in support_one
    )
    electric5, magnetic5 = sourced_tick(
        curl5, electric5, magnetic5, np.zeros(len(edges5)), step
    )
    support_two = np.flatnonzero(
        np.abs(np.concatenate((electric5, magnetic5))) > 1.0e-13
    )
    max_distance_two = max(
        periodic_l1(source_site, field_sites5[index], 10)
        for index in support_two
    )
    checks.check(
        max_distance_one == 1 and max_distance_two <= 4,
        "a local current impulse has a strict one-cycle and two-cycle causal support cone",
    )

    cubic_source_ok = True
    sample_electric = np.array([0.2, -0.3, 0.7])
    sample_magnetic = np.array([-0.4, 0.8, 0.1])
    sample_current = np.array([0.6, -0.2, 0.5])
    for momentum in (
        np.array([0.3, 0.7, 1.1]),
        np.array([1.0, 0.0, 0.0]),
    ):
        electric_out, magnetic_out = source_symbol_tick(
            momentum,
            sample_electric,
            sample_magnetic,
            sample_current,
            step,
        )
        for transform in all_cubic_transformations():
            determinant = int(round(np.linalg.det(transform)))
            transformed_electric, transformed_magnetic = source_symbol_tick(
                transform @ momentum,
                transform @ sample_electric,
                determinant * transform @ sample_magnetic,
                transform @ sample_current,
                step,
            )
            cubic_source_ok = cubic_source_ok and bool(
                np.max(np.abs(transformed_electric - transform @ electric_out))
                < 2.0e-12
                and np.max(
                    np.abs(
                        transformed_magnetic
                        - determinant * transform @ magnetic_out
                    )
                )
                < 2.0e-12
            )
    checks.check(
        cubic_source_ok,
        "the sourced tick covaries under all 48 cubic transformations with polar current",
    )

    print(
        "per_element: every incidence sign, one-edge charge transfer, and source coefficient is checked"
    )
    print(
        "per_site: vertex charge, edge current, edge electric field, and face magnetic updates are local"
    )
    print(
        "per_mode: longitudinal and rank-two transverse source projectors are checked at generic momenta"
    )
    print(
        "per_block: exact continuity, Hodge separation, Poisson minimization, cubic covariance, and causal support are checked"
    )
    print(
        "lattice_wide: full incidence blocks and L=48,64,96,128 Green functions recover the three-dimensional Coulomb coefficient"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
