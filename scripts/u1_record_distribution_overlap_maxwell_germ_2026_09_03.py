#!/usr/bin/env python3
"""Checks for the Record-distribution overlap route to a U(1) Maxwell germ.

The exact theorem is an autocorrelation identity.  Any nonconstant positive
U(1) probability density in H^2 has an overlap kernel with squared Fourier
coefficients and a strictly positive negative-log curvature at identity.
The runner also keeps the statistical kernel distinct from a physical action
and rechecks the temporal-only versus orientation-completed Maxwell boundary.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

from compact_u1_wilson_to_source_free_maxwell_2026_09_02 import (
    D,
    TAU,
    anisotropic_kernel,
    cube_charges,
    plaquettes,
    signed_momentum,
)
from u1_representation_positive_record_kernel_maxwell_germ_2026_09_03 import (
    kernel_curvature,
    record_potential,
    record_potential_prime,
    smooth_mode_angles,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py",
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


def density(
    values: np.ndarray | float,
    cosine: tuple[float, ...],
    sine: tuple[float, ...],
) -> np.ndarray | float:
    result = np.ones_like(values, dtype=float) if isinstance(values, np.ndarray) else 1.0
    for harmonic, (cosine_coefficient, sine_coefficient) in enumerate(
        zip(cosine, sine), 1
    ):
        result = result + cosine_coefficient * np.cos(harmonic * values)
        result = result + sine_coefficient * np.sin(harmonic * values)
    return result


def density_prime(
    values: np.ndarray | float,
    cosine: tuple[float, ...],
    sine: tuple[float, ...],
) -> np.ndarray | float:
    result = np.zeros_like(values, dtype=float) if isinstance(values, np.ndarray) else 0.0
    for harmonic, (cosine_coefficient, sine_coefficient) in enumerate(
        zip(cosine, sine), 1
    ):
        result = result - harmonic * cosine_coefficient * np.sin(harmonic * values)
        result = result + harmonic * sine_coefficient * np.cos(harmonic * values)
    return result


def overlap_coefficients(
    cosine: tuple[float, ...], sine: tuple[float, ...]
) -> tuple[float, ...]:
    return tuple(
        (cosine_coefficient**2 + sine_coefficient**2) / 4.0
        for cosine_coefficient, sine_coefficient in zip(cosine, sine)
    )


def overlap_direct(
    shifts: np.ndarray,
    integration_grid: np.ndarray,
    cosine: tuple[float, ...],
    sine: tuple[float, ...],
) -> np.ndarray:
    reference = density(integration_grid, cosine, sine)
    return np.array(
        [
            float(
                np.mean(
                    reference
                    * density(integration_grid + shift, cosine, sine)
                )
            )
            for shift in shifts
        ]
    )


def overlap_fourier(
    values: np.ndarray | float, coefficients: tuple[float, ...]
) -> np.ndarray | float:
    result = np.ones_like(values, dtype=float) if isinstance(values, np.ndarray) else 1.0
    for harmonic, coefficient in enumerate(coefficients, 1):
        result = result + 2.0 * coefficient * np.cos(harmonic * values)
    return result


def deterministic_record_counts(probabilities: np.ndarray, total: int) -> np.ndarray:
    expected = total * probabilities
    counts = np.floor(expected).astype(int)
    remaining = total - int(np.sum(counts))
    if remaining:
        order = np.argsort(-(expected - counts), kind="stable")
        counts[order[:remaining]] += 1
    return counts


def main() -> int:
    checks = Checks()
    families = (
        ((0.55,), (0.0,)),
        ((-0.55,), (0.0,)),
        ((0.15, -0.20, 0.10), (0.25, 0.12, -0.08)),
    )
    grid = (np.arange(65536) + 0.5) * TAU / 65536 - math.pi
    shifts = np.array([-2.1, -0.9, -0.2, 0.0, 0.4, 1.3, 2.7])

    normalized = True
    positive = True
    varying = True
    reconstruction = True
    overlap_normalized = True
    overlap_nonnegative = True
    overlap_even_periodic = True
    identity_maximum = True
    squared_coefficients = True
    curvature_positive = True
    sobolev_identity = True
    curvature_finite_difference = True
    local_log_minimum = True
    for cosine, sine in families:
        values = density(grid, cosine, sine)
        coefficients = overlap_coefficients(cosine, sine)
        normalized = normalized and abs(float(np.mean(values)) - 1.0) < 2.0e-14
        positive = positive and float(np.min(values)) > 0.30
        translated = [density(grid[::128] - shift, cosine, sine) for shift in shifts[:3]]
        varying = varying and max(
            float(np.max(np.abs(translated[i] - translated[j])))
            for i, j in itertools.combinations(range(3), 2)
        ) > 0.1

        direct = overlap_direct(shifts, grid, cosine, sine)
        closed = overlap_fourier(shifts, coefficients)
        reconstruction = reconstruction and bool(np.max(np.abs(direct - closed)) < 2.0e-14)
        overlap_grid = overlap_fourier(grid, coefficients)
        overlap_normalized = overlap_normalized and abs(float(np.mean(overlap_grid)) - 1.0) < 2.0e-14
        overlap_nonnegative = overlap_nonnegative and float(np.min(overlap_grid)) >= -2.0e-14
        overlap_even_periodic = overlap_even_periodic and bool(
            np.max(np.abs(overlap_grid - overlap_fourier(-grid, coefficients))) < 3.0e-15
            and np.max(np.abs(overlap_grid - overlap_fourier(grid + TAU, coefficients))) < 6.0e-15
        )
        at_identity = float(overlap_fourier(0.0, coefficients))
        identity_maximum = identity_maximum and float(np.max(overlap_grid)) <= at_identity + 2.0e-12
        squared_coefficients = squared_coefficients and all(value >= 0.0 for value in coefficients)
        kappa = kernel_curvature(coefficients)
        curvature_positive = curvature_positive and kappa > 0.0
        derivative_norm = float(np.mean(density_prime(grid, cosine, sine) ** 2))
        density_norm = float(np.mean(values**2))
        sobolev_identity = sobolev_identity and abs(kappa - derivative_norm / density_norm) < 3.0e-14
        step = 2.0e-4
        numeric_curvature = (
            record_potential(step, coefficients)
            - 2.0 * record_potential(0.0, coefficients)
            + record_potential(-step, coefficients)
        ) / step**2
        curvature_finite_difference = curvature_finite_difference and abs(
            float(numeric_curvature) - kappa
        ) < 4.0e-8
        local_log_minimum = local_log_minimum and bool(
            np.min(record_potential(grid[32700:32836], coefficients)) >= -2.0e-14
        )

    checks.check(normalized, "input U1 probability densities normalize against Haar measure")
    checks.check(positive, "tested densities are strictly positive without a Fourier-sign restriction")
    checks.check(varying, "shifted conditional distributions vary with neighboring phase conditions")
    checks.check(reconstruction, "direct distribution overlaps equal squared-Fourier reconstructions")
    checks.check(overlap_normalized, "overlap kernels normalize against Haar measure")
    checks.check(overlap_nonnegative, "overlap kernels are nonnegative probability densities")
    checks.check(overlap_even_periodic, "distribution overlap removes drift and is even and periodic")
    checks.check(identity_maximum, "Cauchy-Schwarz puts a global overlap maximum at identity")
    checks.check(squared_coefficients, "all overlap representation coefficients are modulus squares")
    checks.check(curvature_positive, "every tested nonuniform density gives positive log curvature")
    checks.check(sobolev_identity, "curvature equals derivative norm divided by density norm")
    checks.check(curvature_finite_difference, "closed overlap curvature matches finite differences")
    checks.check(local_log_minimum, "negative-log overlap has a stable flat local minimum")

    rng = np.random.default_rng(90303)
    random_ok = True
    for _ in range(32):
        raw_cosine = rng.normal(size=8)
        raw_sine = rng.normal(size=8)
        scale = 0.42 / float(
            np.sum(np.sqrt(raw_cosine**2 + raw_sine**2))
        )
        cosine = tuple(float(value * scale) for value in raw_cosine)
        sine = tuple(float(value * scale) for value in raw_sine)
        values = density(grid[::128], cosine, sine)
        coefficients = overlap_coefficients(cosine, sine)
        direct = overlap_direct(shifts, grid[::32], cosine, sine)
        random_ok = random_ok and bool(
            np.min(values) >= 0.58 - 2.0e-14
            and np.max(np.abs(direct - overlap_fourier(shifts, coefficients))) < 3.0e-14
            and kernel_curvature(coefficients) > 0.0
        )
    checks.check(random_ok, "32 signed asymmetric eight-harmonic densities obey the overlap theorem")

    von_mises_one = np.exp(0.9 * np.cos(grid - 0.4)) / np.i0(0.9)
    von_mises_two = np.exp(1.7 * np.cos(grid + 1.1)) / np.i0(1.7)
    smooth_density = 0.63 * von_mises_one + 0.37 * von_mises_two
    smooth_derivative = (
        -0.63 * 0.9 * np.sin(grid - 0.4) * von_mises_one
        - 0.37 * 1.7 * np.sin(grid + 1.1) * von_mises_two
    )
    smooth_curvature = float(np.mean(smooth_derivative**2) / np.mean(smooth_density**2))
    finite_step = 5.0e-4
    shifted_smooth_density = (
        0.63
        * np.exp(0.9 * np.cos(grid + finite_step - 0.4))
        / np.i0(0.9)
        + 0.37
        * np.exp(1.7 * np.cos(grid + finite_step + 1.1))
        / np.i0(1.7)
    )
    smooth_overlap_zero = float(np.mean(smooth_density**2))
    smooth_overlap_step = float(np.mean(smooth_density * shifted_smooth_density))
    numeric_smooth_curvature = 2.0 * (
        math.log(smooth_overlap_zero) - math.log(smooth_overlap_step)
    ) / finite_step**2
    checks.check(
        abs(float(np.mean(smooth_density)) - 1.0) < 2.0e-14
        and float(np.min(smooth_density)) > 0.30
        and smooth_curvature > 0.22
        and abs(numeric_smooth_curvature - smooth_curvature) < 3.0e-9,
        "asymmetric non-polynomial density obeys the overlap norm-ratio curvature",
    )

    negative_cosine = (-0.60,)
    negative_sine = (0.0,)
    raw_identity_curvature = -0.60 / (1.0 - 0.60)
    repaired_coefficients = overlap_coefficients(negative_cosine, negative_sine)
    checks.check(
        raw_identity_curvature < -1.0
        and kernel_curvature(repaired_coefficients) > 0.15,
        "autocorrelation repairs a positive density whose raw identity germ is unstable",
    )

    uniform_coefficients = overlap_coefficients((), ())
    checks.check(
        uniform_coefficients == ()
        and kernel_curvature(uniform_coefficients) == 0.0,
        "uniform-distribution mutation has zero overlap curvature and no shift variation",
    )

    cosine, sine = families[2]
    conditions = np.array([-0.7, 0.2, 1.15])
    shifted_overlap_ok = True
    for left, right in itertools.product(conditions, repeat=2):
        direct = float(
            np.mean(
                density(grid - left, cosine, sine)
                * density(grid - right, cosine, sine)
            )
        )
        expected = float(overlap_fourier(left - right, overlap_coefficients(cosine, sine)))
        shifted_overlap_ok = shifted_overlap_ok and abs(direct - expected) < 2.0e-14
    checks.check(
        shifted_overlap_ok,
        "pairwise Record-distribution comparison depends only on relative neighbor condition",
    )

    bins = 256
    bin_grid = (np.arange(bins) + 0.5) * TAU / bins - math.pi
    probabilities = density(bin_grid, cosine, sine) / bins
    shift_bins = 32
    exact_histogram_overlap = float(
        overlap_fourier(TAU * shift_bins / bins, overlap_coefficients(cosine, sine))
    )
    record_errors = []
    for total in (2048, 8192, 32768, 131072):
        counts = deterministic_record_counts(probabilities, total)
        empirical_density = bins * counts / total
        empirical_overlap = float(
            np.mean(empirical_density * np.roll(empirical_density, shift_bins))
        )
        record_errors.append(abs(empirical_overlap - exact_histogram_overlap))
    checks.check(
        record_errors[-1] < 2.0e-5 and record_errors[-1] < record_errors[0] / 8.0,
        "deterministic count rounding at fixed 256 uniform bins approaches the finite-bin overlap",
    )

    # Exact bin integrals for p(theta)=1+a cos(theta), with mass-one Haar
    # measure. Orthogonality gives C(delta)=1+(a*a/2)cos(delta).
    amplitude_histogram = 0.25
    uniform_errors = []
    nonuniform_values = []
    for bin_count in (32, 64, 128, 256):
        edges = np.linspace(0.0, TAU, bin_count + 1)
        mass = (np.diff(edges) + amplitude_histogram * np.diff(np.sin(edges))) / TAU
        discrete = bin_count * float(mass @ np.roll(mass, bin_count // 8))
        target = 1.0 + amplitude_histogram**2 * math.cos(math.pi / 4.0) / 2.0
        uniform_errors.append(abs(discrete - target))
        unequal_edges = np.concatenate((
            np.linspace(0.0, math.pi, bin_count // 4 + 1),
            np.linspace(math.pi, TAU, 3 * bin_count // 4 + 1)[1:],
        ))
        unequal_mass = (np.diff(unequal_edges) + amplitude_histogram * np.diff(np.sin(unequal_edges))) / TAU
        nonuniform_values.append(bin_count * float(unequal_mass @ unequal_mass))
    checks.check(
        all(b < a / 3.9 for a, b in zip(uniform_errors, uniform_errors[1:]))
        and uniform_errors[-1] < 2.0e-6,
        "equal Haar-bin refinement at a fixed physical shift converges to the independent density integral",
    )
    checks.check(
        abs(nonuniform_values[-1] - 1.375) < 2.0e-5
        and abs(nonuniform_values[-1] - (1.0 + amplitude_histogram**2 / 2.0)) > 0.34,
        "nonuniform refining bins give a different unweighted overlap despite vanishing mesh size",
    )

    path_angles = np.array([0.17, -0.29, 0.31, 0.06, -0.22])
    coefficients = overlap_coefficients(*families[2])
    path_probability = float(np.prod(overlap_fourier(path_angles, coefficients)))
    path_action = float(np.sum(record_potential(path_angles, coefficients)))
    identity_value = float(overlap_fourier(0.0, coefficients))
    checks.check(
        abs(
            -math.log(path_probability)
            - (path_action - len(path_angles) * math.log(identity_value))
        )
        < 2.0e-15,
        "supplied factorized overlap weights give an additive negative-log action",
    )

    amplitude = 0.12
    continuum_families = (
        overlap_coefficients(*families[0]),
        overlap_coefficients(*families[1]),
        overlap_coefficients(*families[2]),
    )
    action_refinement = True
    operator_refinement = True
    scaled_operator_families = []
    for coefficients in continuum_families:
        kappa = kernel_curvature(coefficients)
        target_action = kappa * amplitude**2 * TAU**4 / 4.0
        action_errors = []
        operator_errors = []
        scaled_operators = []
        for refinement in (8, 12, 16, 24, 32, 48):
            angles, spacing = smooth_mode_angles(refinement, amplitude)
            action = refinement**3 * float(np.sum(record_potential(angles, coefficients)))
            action_errors.append(abs(action - target_action))
            argument = spacing * amplitude * (1.0 - math.cos(spacing))
            scaled_operator = (
                2.0
                * float(record_potential_prime(argument, coefficients))
                / (kappa * spacing**3)
            )
            scaled_operators.append(scaled_operator)
            operator_errors.append(abs(scaled_operator - amplitude))
        action_order = math.log(action_errors[-2] / action_errors[-1]) / math.log(48.0 / 32.0)
        operator_order = math.log(operator_errors[-2] / operator_errors[-1]) / math.log(48.0 / 32.0)
        action_refinement = action_refinement and all(
            left > right for left, right in zip(action_errors, action_errors[1:])
        ) and action_order > 1.95
        operator_refinement = operator_refinement and all(
            left > right for left, right in zip(operator_errors, operator_errors[1:])
        ) and operator_order > 1.95
        scaled_operator_families.append(scaled_operators)
    microscopic_spreads = [
        max(values) - min(values) for values in zip(*scaled_operator_families)
    ]
    checks.check(action_refinement, "overlap potentials converge at second order to Maxwell actions")
    checks.check(operator_refinement, "overlap forces converge at second order to the Maxwell operator")
    checks.check(
        all(left > right for left, right in zip(microscopic_spreads, microscopic_spreads[1:]))
        and microscopic_spreads[-1] < 2.0e-9,
        "curvature-normalized overlap laws converge independently of input-distribution shape",
    )

    smooth_links = np.zeros((8,) * D + (D,), dtype=float)
    spacing = TAU / 8
    sites = np.indices((8,) * D)
    smooth_links[..., 1] = spacing * amplitude * np.cos(spacing * sites[2])
    _, smooth_theta, winding = plaquettes(smooth_links)
    charges, residual, relation = cube_charges(smooth_theta, winding)
    checks.check(
        relation
        and residual < 1.0e-14
        and all(bool(np.all(value == 0)) for value in charges.values()),
        "overlap-induced smooth branch inherits the exact zero-monopole Bianchi identity",
    )

    kappa = kernel_curvature(continuum_families[2])
    spectrum_ok = True
    gauge_null_ok = True
    transverse_ok = True
    for lattice_length in (3, 4, 5):
        for indices in itertools.product(range(lattice_length), repeat=D):
            momenta = np.array(
                [signed_momentum(index, lattice_length) for index in indices]
            )
            q = 2.0 * np.sin(momenta / 2.0)
            norm_square = float(q @ q)
            if norm_square < 1.0e-15:
                continue
            kernel = anisotropic_kernel(q, kappa, kappa)
            eigenvalues = np.linalg.eigvalsh(kernel)
            spectrum_ok = spectrum_ok and bool(
                np.max(
                    np.abs(
                        eigenvalues
                        - np.array(
                            [
                                0.0,
                                kappa * norm_square,
                                kappa * norm_square,
                                kappa * norm_square,
                            ]
                        )
                    )
                )
                < 7.0e-12
            )
            gauge_null_ok = gauge_null_ok and bool(np.linalg.norm(kernel @ q) < 7.0e-12)
            spatial_square = float(q[1:] @ q[1:])
            if spatial_square > 1.0e-14:
                reduced = (
                    kernel[1:, 1:]
                    - np.outer(kernel[1:, 0], kernel[0, 1:]) / kernel[0, 0]
                )
                transverse_ok = transverse_ok and np.linalg.matrix_rank(
                    reduced, tol=1.0e-11
                ) == 2
    checks.check(spectrum_ok, "orientation-completed overlap germ has the isotropic Maxwell spectrum")
    checks.check(gauge_null_ok, "orientation-completed overlap germ preserves the exact gauge null")
    checks.check(transverse_ok, "orientation completion leaves exactly two transverse local modes")

    spatial_q = np.array([0.0, 1.2, -0.7, 0.3])
    temporal_only = anisotropic_kernel(spatial_q, kappa, 0.0)
    isotropic = anisotropic_kernel(spatial_q, kappa, kappa)
    checks.check(
        np.linalg.matrix_rank(temporal_only, tol=1.0e-12) == 1
        and np.linalg.matrix_rank(isotropic, tol=1.0e-12) == 3,
        "Record-distribution overlap alone remains temporal and lacks magnetic stiffness",
    )

    anisotropic = anisotropic_kernel(spatial_q, kappa, 2.5 * kappa)
    checks.check(
        np.max(np.abs(anisotropic - isotropic)) > 0.05,
        "unequal spatial completion remains physically visible in the infrared cone",
    )

    print("per_element: every Fourier component of each input density is squared analytically in the overlap kernel")
    print("per_site: shifted neighbor-conditioned distributions and finite Record histograms are compared directly")
    print("per_mode: every nonzero Fourier momentum on L=3,4,5 is checked after orientation completion")
    print("per_block: raw-sign, uniform, temporal-only, isotropic, and anisotropic blocks are contrasted")
    print("lattice_wide: fixed-volume action/operator refinements and zero-monopole cube identities run on four-lattices")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
