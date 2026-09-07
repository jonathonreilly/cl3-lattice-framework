#!/usr/bin/env python3
"""Checks for a finite-depth local reversible Maxwell/Yee tick.

The tick is the palindromic three-shear composition

    B <- B + (h/2) C E
    E <- E - h C^T B
    B <- B + (h/2) C E

on the role-compiled physical edge/face incidence lattice.  Each shear reads
only the four opposite-role physical nearest neighbors.  The composition is
exactly reversible, preserves both Gauss rows, and conserves a positive local
modified field energy for 0 < h < 1/sqrt(3).
"""

from __future__ import annotations

import itertools
import math
from fractions import Fraction

import numpy as np

from u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03 import (
    curl_symbol,
    lattice_momentum,
    physical_incidence,
    signed_permutation_matrix,
    yee_generator,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py",
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


def magnetic_shear(curl: np.ndarray, step: float) -> np.ndarray:
    """Return B <- B + step C E in (E,B) ordering."""

    edge_count = curl.shape[1]
    face_count = curl.shape[0]
    return np.block(
        [
            [np.eye(edge_count), np.zeros((edge_count, face_count))],
            [step * curl, np.eye(face_count)],
        ]
    )


def electric_shear(curl: np.ndarray, step: float) -> np.ndarray:
    """Return E <- E - step C^T B in (E,B) ordering."""

    edge_count = curl.shape[1]
    face_count = curl.shape[0]
    return np.block(
        [
            [np.eye(edge_count), -step * curl.T],
            [np.zeros((face_count, edge_count)), np.eye(face_count)],
        ]
    )


def leapfrog_tick(curl: np.ndarray, step: float) -> np.ndarray:
    """Return the palindromic B/2-E-B/2 finite tick."""

    half_magnetic = magnetic_shear(curl, 0.5 * step)
    electric = electric_shear(curl, step)
    return half_magnetic @ electric @ half_magnetic


def dual_leapfrog_tick(curl: np.ndarray, step: float) -> np.ndarray:
    """Return the E/2-B-E/2 time-staggered sibling."""

    half_electric = electric_shear(curl, 0.5 * step)
    magnetic = magnetic_shear(curl, step)
    return half_electric @ magnetic @ half_electric


def modified_energy_metric(curl: np.ndarray, step: float) -> np.ndarray:
    """Positive tick invariant when step times the largest singular value < 2."""

    edge_count = curl.shape[1]
    face_count = curl.shape[0]
    return np.block(
        [
            [
                np.eye(edge_count) - 0.25 * step**2 * curl.T @ curl,
                np.zeros((edge_count, face_count)),
            ],
            [np.zeros((face_count, edge_count)), np.eye(face_count)],
        ]
    )


def all_cubic_transformations() -> tuple[np.ndarray, ...]:
    transforms = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            transforms.append(signed_permutation_matrix(permutation, signs))
    return tuple(transforms)


def periodic_l1(
    left: tuple[int, int, int], right: tuple[int, int, int], size: int
) -> int:
    return sum(
        min(abs(first - second), size - abs(first - second))
        for first, second in zip(left, right)
    )


def exact_half_step_matrices(curl: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    """Return integer numerators for h=1/2 B-half and E-full layers."""

    integer_curl = curl.astype(np.int64)
    edge_count = integer_curl.shape[1]
    face_count = integer_curl.shape[0]
    edge_identity = np.eye(edge_count, dtype=np.int64)
    face_identity = np.eye(face_count, dtype=np.int64)
    zeros_ef = np.zeros((edge_count, face_count), dtype=np.int64)
    zeros_fe = np.zeros((face_count, edge_count), dtype=np.int64)
    # B half-step is h/2=1/4 and E full-step is h=1/2.
    magnetic_numerator = np.block(
        [
            [4 * edge_identity, zeros_ef],
            [integer_curl, 4 * face_identity],
        ]
    )
    electric_numerator = np.block(
        [
            [2 * edge_identity, -integer_curl.T],
            [zeros_fe, 2 * face_identity],
        ]
    )
    return magnetic_numerator, electric_numerator


def skew_exponential(generator: np.ndarray, step: float) -> np.ndarray:
    hermitian = 1j * generator
    eigenvalues, eigenvectors = np.linalg.eigh(hermitian)
    return (
        eigenvectors
        @ np.diag(np.exp(-1j * step * eigenvalues))
        @ eigenvectors.conj().T
    )


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
    edge_count = len(edges)
    face_count = len(faces)
    total_count = edge_count + face_count
    checks.check(
        (len(vertices), edge_count, face_count, len(cubes)) == (27, 81, 81, 27)
        and np.array_equal(curl_integer @ gradient, np.zeros((81, 27), dtype=int))
        and np.array_equal(divergence @ curl_integer, np.zeros((27, 81), dtype=int)),
        "the parent physical incidence complex is reconstructed exactly",
    )

    physical_size = 6
    incidence_is_nearest_neighbor = True
    for face_index, edge_index in zip(*np.nonzero(curl_integer)):
        incidence_is_nearest_neighbor = incidence_is_nearest_neighbor and (
            periodic_l1(faces[face_index], edges[edge_index], physical_size) == 1
        )
    checks.check(
        incidence_is_nearest_neighbor
        and np.all(np.count_nonzero(curl_integer, axis=0) == 4)
        and np.all(np.count_nonzero(curl_integer, axis=1) == 4),
        "every curl coupling joins physical nearest neighbors and every star has four legs",
    )

    magnetic_numerator, electric_numerator = exact_half_step_matrices(curl_integer)
    checks.check(
        int(np.max(np.count_nonzero(magnetic_numerator, axis=1))) == 5
        and int(np.max(np.count_nonzero(electric_numerator, axis=1))) == 5,
        "each shear layer reads only self plus four physical nearest neighbors",
    )
    checks.check(
        np.all(np.diag(magnetic_numerator) == 4)
        and np.all(np.diag(electric_numerator) == 2),
        "both shear layers are triangular with unit diagonal after denominator removal",
    )

    # h=1/2 gives denominators 4,2,4 and therefore a denominator-32 tick.
    tick_numerator = magnetic_numerator @ electric_numerator @ magnetic_numerator
    negative_magnetic = magnetic_numerator.copy()
    negative_electric = electric_numerator.copy()
    negative_magnetic[edge_count:, :edge_count] *= -1
    negative_electric[:edge_count, edge_count:] *= -1
    reverse_numerator = negative_magnetic @ negative_electric @ negative_magnetic
    checks.check(
        np.array_equal(
            tick_numerator @ reverse_numerator,
            32**2 * np.eye(total_count, dtype=np.int64),
        )
        and np.array_equal(
            reverse_numerator @ tick_numerator,
            32**2 * np.eye(total_count, dtype=np.int64),
        ),
        "the depth-three tick obeys U(-h)=U(h)^-1 exactly over integers",
    )

    constraint = np.block(
        [
            [gradient.T, np.zeros((len(vertices), face_count), dtype=int)],
            [np.zeros((len(cubes), edge_count), dtype=int), divergence],
        ]
    ).astype(np.int64)
    checks.check(
        np.array_equal(constraint @ magnetic_numerator, 4 * constraint),
        "each magnetic half-shear preserves both electric and magnetic Gauss rows exactly",
    )
    checks.check(
        np.array_equal(constraint @ electric_numerator, 2 * constraint),
        "the electric full-shear preserves both Gauss rows exactly",
    )
    checks.check(
        np.array_equal(constraint @ tick_numerator, 32 * constraint),
        "the complete finite tick preserves both Gauss sectors exactly",
    )

    all_field_sites = edges + faces
    nonzero_rows, nonzero_columns = np.nonzero(tick_numerator)
    support_distances = tuple(
        periodic_l1(
            all_field_sites[row], all_field_sites[column], physical_size
        )
        for row, column in zip(nonzero_rows, nonzero_columns)
    )
    checks.check(
        max(support_distances) == 3
        and set(support_distances) == {0, 1, 2, 3},
        "the composed tick has causal radius three, exactly matching its three local layers",
    )

    # The declared three-shear schedule has tangent coefficients b and a+c.
    candidates = []
    grid = tuple(Fraction(n, 8) for n in range(-8, 17))
    for first, middle, last in itertools.product(grid, repeat=3):
        first_order = middle == 1 and first + last == 1
        palindromic = first == last
        if first_order and palindromic:
            candidates.append((first, middle, last))
    checks.check(
        candidates == [(Fraction(1, 2), Fraction(1), Fraction(1, 2))],
        "first-order Maxwell consistency plus a palindromic B-E-B schedule fixes half-full-half",
    )

    tangent = np.block(
        [
            [np.zeros((edge_count, edge_count)), -curl.T],
            [curl, np.zeros((face_count, face_count))],
        ]
    )
    checks.check(
        np.array_equal(tangent, yee_generator(curl)),
        "the selected finite tick has the classified Maxwell generator as its exact tangent",
    )

    step = 0.5
    tick = leapfrog_tick(curl, step)
    metric = modified_energy_metric(curl, step)
    metric_numerator = np.block(
        [
            [
                16 * np.eye(edge_count, dtype=np.int64)
                - curl_integer.T @ curl_integer,
                np.zeros((edge_count, face_count), dtype=np.int64),
            ],
            [
                np.zeros((face_count, edge_count), dtype=np.int64),
                16 * np.eye(face_count, dtype=np.int64),
            ],
        ]
    )
    checks.check(
        np.array_equal(
            tick_numerator.T @ metric_numerator @ tick_numerator,
            32**2 * metric_numerator,
        ),
        "the local modified field energy is conserved exactly over integers",
    )
    checks.check(
        np.max(np.abs(tick.T @ metric @ tick - metric)) < 2.0e-14,
        "the floating reconstruction is orthogonal in the modified energy metric",
    )

    maximum_symbol_norm = 2.0 * math.sqrt(3.0)
    analytic_lower_bound = 1.0 - 0.25 * step**2 * maximum_symbol_norm**2
    checks.check(
        abs(analytic_lower_bound - 0.25) < 1.0e-15
        and float(np.min(np.linalg.eigvalsh(metric))) > analytic_lower_bound - 1.0e-12,
        "h=1/2 gives a positive local invariant with infinite-lattice lower bound one quarter",
    )
    checks.check(
        np.max(np.abs(tick.T @ tick - np.eye(total_count))) > 1.0e-3,
        "the raw onsite Euclidean norm is not conserved, keeping circuit unitarity distinct",
    )

    time_reversal = np.diag([1.0] * edge_count + [-1.0] * face_count)
    checks.check(
        np.max(
            np.abs(
                time_reversal @ tick @ time_reversal
                - leapfrog_tick(curl, -step)
            )
        )
        < 2.0e-14,
        "magnetic sign reversal implements exact time reversal of the palindromic tick",
    )

    asymmetric = (
        magnetic_shear(curl, 0.25 * step)
        @ electric_shear(curl, step)
        @ magnetic_shear(curl, 0.75 * step)
    )
    asymmetric_backward = (
        magnetic_shear(curl, -0.25 * step)
        @ electric_shear(curl, -step)
        @ magnetic_shear(curl, -0.75 * step)
    )
    checks.check(
        np.max(np.abs(asymmetric_backward @ asymmetric - np.eye(total_count))) > 1.0e-3,
        "a quarter-full-three-quarter mutation keeps the tangent but loses self-adjoint time reversal",
    )

    spectrum_ok = True
    phase_count_ok = True
    no_doublers = True
    stability_ok = True
    checked_nonzero = 0
    for lattice_size in (3, 4, 5, 7):
        for indices_raw in itertools.product(range(lattice_size), repeat=3):
            indices = tuple(indices_raw)
            momentum = lattice_momentum(indices, lattice_size)
            norm = float(np.linalg.norm(momentum))
            symbol_tick = leapfrog_tick(curl_symbol(momentum), step)
            eigenvalues = np.linalg.eigvals(symbol_tick)
            angles = np.sort(np.angle(eigenvalues))
            theta = 2.0 * math.asin(0.5 * step * norm)
            expected = np.array([-theta, -theta, 0.0, 0.0, theta, theta])
            spectrum_ok = spectrum_ok and bool(
                np.max(np.abs(angles - expected)) < 4.0e-12
            )
            stability_ok = stability_ok and bool(
                np.max(np.abs(np.abs(eigenvalues) - 1.0)) < 4.0e-12
            )
            if norm > 1.0e-14:
                checked_nonzero += 1
                phase_count_ok = phase_count_ok and (
                    sum(angles > 1.0e-10) == 2
                    and sum(angles < -1.0e-10) == 2
                )
                no_doublers = no_doublers and theta > 1.0e-12
            else:
                no_doublers = no_doublers and indices == (0, 0, 0)
    checks.check(
        spectrum_ok,
        "every tested tick block has phases minus-theta twice, zero twice, plus-theta twice",
    )
    checks.check(
        phase_count_ok and checked_nonzero == 27 + 64 + 125 + 343 - 4,
        "each nonzero tested momentum has exactly two positive photon-phase branches",
    )
    checks.check(
        no_doublers,
        "the finite tick has no additional zero-phase momentum in the tested Brillouin zones",
    )
    checks.check(
        stability_ok,
        "all tick eigenvalues remain on the unit circle throughout the tested zones",
    )

    infrared_ratios = []
    for lattice_size in (16, 32, 64, 128, 256):
        momentum = lattice_momentum((1, 0, 0), lattice_size)
        norm = float(np.linalg.norm(momentum))
        phase = 2.0 * math.asin(0.5 * step * norm)
        infrared_ratios.append(
            (phase / step) / (2.0 * math.pi / lattice_size)
        )
    checks.check(
        all(
            abs(left - 1.0) > abs(right - 1.0)
            for left, right in zip(infrared_ratios, infrared_ratios[1:])
        )
        and abs(infrared_ratios[-1] - 1.0) < 2.0e-5,
        "both discrete-time branches converge monotonically to unit-speed Maxwell dispersion",
    )

    cubic_ok = True
    transformations = all_cubic_transformations()
    for momentum in (
        np.array([0.0, 0.7, 1.2]),
        np.array([0.3, 0.8, 1.1]),
        np.array([1.4, 0.2, 0.9]),
    ):
        base_tick = leapfrog_tick(curl_symbol(momentum), step)
        for transform in transformations:
            determinant = int(round(np.linalg.det(transform)))
            field_transform = np.block(
                [
                    [transform, np.zeros((3, 3))],
                    [np.zeros((3, 3)), determinant * transform],
                ]
            )
            transformed_tick = leapfrog_tick(
                curl_symbol(transform @ momentum), step
            )
            cubic_ok = cubic_ok and bool(
                np.max(
                    np.abs(
                        transformed_tick
                        - field_transform @ base_tick @ field_transform.T
                    )
                )
                < 2.0e-12
            )
    checks.check(
        len(transformations) == 48 and cubic_ok,
        "the tick covaries under all 48 cubic transformations with B axial under reflections",
    )

    dual_spectrum_ok = True
    for momentum in (
        np.array([0.3, 0.7, 1.1]),
        np.array([1.0, 0.0, 0.0]),
        np.array([0.8, 1.2, 0.4]),
    ):
        symbol = curl_symbol(momentum)
        first = np.sort_complex(np.linalg.eigvals(leapfrog_tick(symbol, step)))
        second = np.sort_complex(np.linalg.eigvals(dual_leapfrog_tick(symbol, step)))
        dual_spectrum_ok = dual_spectrum_ok and bool(
            np.max(np.abs(np.sort(np.angle(first)) - np.sort(np.angle(second))))
            < 2.0e-12
        )
    checks.check(
        dual_spectrum_ok,
        "the E-B-E time-staggered sibling has the identical physical phase spectrum",
    )

    unstable_step = 2.0 / 3.0
    corner_symbol = curl_symbol(np.array([2.0, 2.0, 2.0]))
    unstable_eigenvalues = np.linalg.eigvals(
        leapfrog_tick(corner_symbol, unstable_step)
    )
    checks.check(
        unstable_step * maximum_symbol_norm > 2.0
        and np.max(np.abs(np.abs(unstable_eigenvalues) - 1.0)) > 0.5,
        "a step beyond the positivity bound develops an explicit unstable corner mode",
    )

    sample_symbol = curl_symbol(np.array([0.4, 0.7, 1.1]))
    generator = yee_generator(sample_symbol)
    errors = []
    for trial_step in (0.2, 0.1, 0.05, 0.025):
        errors.append(
            float(
                np.linalg.norm(
                    leapfrog_tick(sample_symbol, trial_step)
                    - skew_exponential(generator, trial_step),
                    ord=2,
                )
            )
        )
    ratios = tuple(left / right for left, right in zip(errors, errors[1:]))
    checks.check(
        all(7.9 < ratio < 8.2 for ratio in ratios),
        "the palindromic local tick approaches the continuous Maxwell flow with cubic one-step error",
    )
    checks.check(
        errors[0] > 1.0e-4,
        "the finite tick differs from the exact exponential away from the infrared",
    )

    print(
        "per_element: every integer incidence coefficient and each half/full shear coefficient is checked"
    )
    print(
        "per_site: every shear reads one physical four-neighbor star; the three-layer tick has radius three"
    )
    print(
        "per_mode: all momenta on L=3,4,5,7 carry exactly two stable photon-phase branches"
    )
    print(
        "per_block: exact inverse, Gauss preservation, modified energy, time reversal, cubic covariance, and controls are checked"
    )
    print(
        "lattice_wide: the full 162-variable rational tick is multiplied exactly and compared with its local energy metric"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
