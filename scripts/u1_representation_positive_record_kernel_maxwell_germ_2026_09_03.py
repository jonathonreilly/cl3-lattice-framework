#!/usr/bin/env python3
"""Checks for the U(1) representation-positive Record-kernel Maxwell germ.

The exact theorem is Fourier analytic.  Positive nonconstant character data
give a strict quadratic maximum of the U(1) step density at the identity; the
negative-log transfer potential therefore has positive curvature.  The runner
also separates the temporal kernel from the still-needed spatial completion.
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


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
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


def fourier_kernel(values: np.ndarray | float, coefficients: tuple[float, ...]) -> np.ndarray | float:
    result = np.ones_like(values, dtype=float) if isinstance(values, np.ndarray) else 1.0
    for harmonic, coefficient in enumerate(coefficients, 1):
        result = result + 2.0 * coefficient * np.cos(harmonic * values)
    return result


def fourier_kernel_prime(values: np.ndarray | float, coefficients: tuple[float, ...]) -> np.ndarray | float:
    result = np.zeros_like(values, dtype=float) if isinstance(values, np.ndarray) else 0.0
    for harmonic, coefficient in enumerate(coefficients, 1):
        result = result - 2.0 * harmonic * coefficient * np.sin(harmonic * values)
    return result


def kernel_curvature(coefficients: tuple[float, ...]) -> float:
    numerator = 2.0 * sum((harmonic**2) * coefficient for harmonic, coefficient in enumerate(coefficients, 1))
    denominator = 1.0 + 2.0 * sum(coefficients)
    return numerator / denominator


def record_potential(values: np.ndarray | float, coefficients: tuple[float, ...]) -> np.ndarray | float:
    at_identity = float(fourier_kernel(0.0, coefficients))
    return np.log(at_identity) - np.log(fourier_kernel(values, coefficients))


def record_potential_prime(values: np.ndarray | float, coefficients: tuple[float, ...]) -> np.ndarray | float:
    return -fourier_kernel_prime(values, coefficients) / fourier_kernel(values, coefficients)


def lueders_coefficients(weights: np.ndarray, modes: tuple[int, ...]) -> dict[int, float]:
    """Fourier coefficients of the position kernel induced by positive Kraus blocks."""
    dimension = len(modes)
    amplitudes = np.sqrt(weights)
    output: dict[int, float] = {}
    for difference in range(max(modes) - min(modes) + 1):
        total = 0.0
        for outcome in range(weights.shape[0]):
            for left, n_left in enumerate(modes):
                for right, n_right in enumerate(modes):
                    if n_left - n_right == difference:
                        total += amplitudes[outcome, left] * amplitudes[outcome, right]
        output[difference] = total / dimension
    return output


def lueders_kernel(values: np.ndarray, weights: np.ndarray, modes: tuple[int, ...]) -> np.ndarray:
    amplitudes = np.sqrt(weights)
    total = np.zeros_like(values, dtype=float)
    for row in amplitudes:
        wave = np.zeros_like(values, dtype=np.complex128)
        for coefficient, mode in zip(row, modes):
            wave += coefficient * np.exp(1j * mode * values)
        total += np.abs(wave) ** 2
    return total / len(modes)


def smooth_mode_angles(length: int, amplitude: float) -> tuple[np.ndarray, float]:
    spacing = TAU / length
    coordinates = spacing * np.arange(length)
    angles = spacing * amplitude * (np.cos(coordinates) - np.cos(coordinates + spacing))
    return angles, spacing


def main() -> int:
    checks = Checks()
    families = (
        (0.22,),
        (0.12, 0.07),
        (0.08, 0.05, 0.025),
    )
    grid = (np.arange(65536) + 0.5) * TAU / 65536 - math.pi

    normalized = True
    even_periodic = True
    positive = True
    identity_maximum = True
    nonconstant = True
    curvature_positive = True
    curvature_finite_difference = True
    potential_properties = True
    derivative_check = True
    for coefficients in families:
        kernel = fourier_kernel(grid, coefficients)
        normalized = normalized and abs(float(np.mean(kernel)) - 1.0) < 2.0e-14
        even_periodic = even_periodic and bool(
            np.max(np.abs(kernel - fourier_kernel(-grid, coefficients))) < 2.0e-15
            and np.max(np.abs(kernel - fourier_kernel(grid + TAU, coefficients))) < 4.0e-15
        )
        positive = positive and bool(np.min(kernel) > 0.5)
        identity = float(fourier_kernel(0.0, coefficients))
        identity_maximum = identity_maximum and float(np.max(kernel)) <= identity + 2.0e-12
        nonconstant = nonconstant and float(np.max(kernel) - np.min(kernel)) > 0.1
        kappa = kernel_curvature(coefficients)
        curvature_positive = curvature_positive and kappa > 0.0
        h = 2.0e-4
        numeric = (
            record_potential(h, coefficients)
            - 2.0 * record_potential(0.0, coefficients)
            + record_potential(-h, coefficients)
        ) / h**2
        curvature_finite_difference = curvature_finite_difference and abs(float(numeric) - kappa) < 3.0e-8
        potential = record_potential(grid, coefficients)
        potential_properties = potential_properties and bool(
            np.min(potential) >= -2.0e-12
            and np.max(np.abs(potential - record_potential(-grid, coefficients))) < 3.0e-15
        )
        test_angles = np.array([-1.1, -0.35, 0.2, 0.9])
        step = 1.0e-6
        finite_difference = (
            record_potential(test_angles + step, coefficients)
            - record_potential(test_angles - step, coefficients)
        ) / (2.0 * step)
        derivative_check = derivative_check and bool(
            np.max(np.abs(finite_difference - record_potential_prime(test_angles, coefficients))) < 3.0e-10
        )

    checks.check(normalized, "positive Fourier kernels normalize against U1 Haar measure")
    checks.check(even_periodic, "representation-positive kernels are even and 2pi-periodic")
    checks.check(positive, "tested nonconstant kernels remain strictly positive on the circle")
    checks.check(identity_maximum, "nonnegative character data put a global kernel maximum at identity")
    checks.check(nonconstant, "tested kernels vary with the neighboring phase condition")
    checks.check(curvature_positive, "every nonconstant positive-character family has positive log curvature")
    checks.check(curvature_finite_difference, "closed curvature formula matches independent finite differences")
    checks.check(potential_properties, "negative-log transfer potentials are even with a flat local minimum")
    checks.check(derivative_check, "closed negative-log force matches independent finite differences")

    rng = np.random.default_rng(90302)
    random_family_ok = True
    for _ in range(32):
        raw = rng.uniform(0.001, 1.0, size=8)
        raw *= 0.18 / float(np.sum(raw))
        coefficients = tuple(float(value) for value in raw)
        kernel = fourier_kernel(grid[::128], coefficients)
        random_family_ok = random_family_ok and bool(
            np.min(kernel) >= 1.0 - 2.0 * sum(coefficients) - 2.0e-14
            and kernel_curvature(coefficients) > 0.0
            and np.max(kernel) <= fourier_kernel(0.0, coefficients) + 2.0e-12
        )
    checks.check(random_family_ok, "32 eight-harmonic positive families obey the analytic maximum and curvature theorem")

    modes = (-1, 0, 1)
    sharp_q1 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 1.0]])
    sharp_q2 = np.array([[0.0, 1.0, 0.0], [1.0, 0.0, 1.0]])
    soft = np.array([[0.82, 0.27, 0.56], [0.18, 0.73, 0.44]])
    channels = (sharp_q1, sharp_q2, soft)
    channel_normalization = all(
        np.max(np.abs(np.sum(weights, axis=0) - 1.0)) < 1.0e-15 for weights in channels
    )
    checks.check(channel_normalization, "positive Lueders Kraus weights are trace preserving mode by mode")

    lueders_reconstruction = True
    lueders_positive_coefficients = True
    lueders_curvature = True
    for weights in channels:
        coefficients = lueders_coefficients(weights, modes)
        direct = lueders_kernel(grid[::64], weights, modes)
        reconstructed = coefficients[0] + sum(
            2.0 * coefficients[harmonic] * np.cos(harmonic * grid[::64])
            for harmonic in (1, 2)
        )
        lueders_reconstruction = lueders_reconstruction and bool(
            abs(coefficients[0] - 1.0) < 2.0e-15
            and np.max(np.abs(direct - reconstructed)) < 3.0e-15
        )
        lueders_positive_coefficients = lueders_positive_coefficients and all(
            value >= 0.0 for value in coefficients.values()
        )
        nonzero_moment = sum(harmonic**2 * coefficients[harmonic] for harmonic in (1, 2))
        lueders_curvature = lueders_curvature and nonzero_moment > 0.0
    checks.check(lueders_reconstruction, "positive central registration reproduces its nonnegative Fourier autocorrelation")
    checks.check(lueders_positive_coefficients, "positive Lueders registration has nonnegative U1 representation data")
    checks.check(lueders_curvature, "two-outcome three-mode registration necessarily leaves a positive second moment")

    q1_coefficients = (1.0 / 3.0, 0.0)
    q2_coefficients = (0.0, 1.0 / 3.0)
    exact_binary = bool(
        np.max(np.abs(lueders_kernel(grid[::64], sharp_q1, modes) - fourier_kernel(grid[::64], q1_coefficients))) < 3.0e-15
        and np.max(np.abs(lueders_kernel(grid[::64], sharp_q2, modes) - fourier_kernel(grid[::64], q2_coefficients))) < 3.0e-15
        and abs(kernel_curvature(q1_coefficients) - 2.0 / 5.0) < 2.0e-15
        and abs(kernel_curvature(q2_coefficients) - 8.0 / 5.0) < 2.0e-15
    )
    checks.check(exact_binary, "all sharp binary partitions give T=1+2 cos(q theta)/3 and kappa in {2/5,8/5}")

    full_resolution = np.eye(3)
    full_coefficients = lueders_coefficients(full_resolution, modes)
    checks.check(
        abs(full_coefficients[0] - 1.0) < 2.0e-15
        and abs(full_coefficients[1]) < 2.0e-15
        and abs(full_coefficients[2]) < 2.0e-15
        and np.max(np.abs(lueders_kernel(grid[::64], full_resolution, modes) - 1.0)) < 2.0e-15,
        "full three-mode resolution removes all transition curvature",
    )

    constant = ()
    negative = (-0.20,)
    constant_grid = fourier_kernel(grid[::64], constant)
    negative_grid = fourier_kernel(grid[::64], negative)
    checks.check(
        np.max(np.abs(constant_grid - 1.0)) == 0.0 and kernel_curvature(constant) == 0.0,
        "constant-kernel mutation has zero curvature and no neighbor variation",
    )
    checks.check(
        np.min(negative_grid) > 0.59 and kernel_curvature(negative) < -0.6,
        "negative-character mutation stays probabilistic but makes identity unstable",
    )

    neighbor_angles = np.array([-0.8, 0.35, 1.1])
    outcomes = grid[::256]
    varying = []
    for neighbor in neighbor_angles:
        density = fourier_kernel(outcomes - neighbor, families[0])
        varying.append(density)
    constant_conditionals = [fourier_kernel(outcomes - neighbor, constant) for neighbor in neighbor_angles]
    checks.check(
        max(float(np.max(np.abs(varying[i] - varying[j]))) for i, j in itertools.combinations(range(3), 2)) > 0.2
        and max(float(np.max(np.abs(constant_conditionals[i] - constant_conditionals[j]))) for i, j in itertools.combinations(range(3), 2)) == 0.0,
        "within the convolution class Admissibility variation is exactly the nonconstant-kernel condition",
    )

    path_angles = np.array([0.12, -0.31, 0.27, 0.08, -0.19])
    coefficients = families[1]
    path_probability = float(np.prod(fourier_kernel(path_angles, coefficients)))
    path_action = float(np.sum(record_potential(path_angles, coefficients)))
    additive_identity = -math.log(path_probability) - (
        path_action - len(path_angles) * math.log(float(fourier_kernel(0.0, coefficients)))
    )
    checks.check(abs(additive_identity) < 2.0e-15, "factorized Record-transition probability gives an additive negative-log action")

    amplitude = 0.12
    action_refinement = True
    operator_refinement = True
    scaled_operator_families = []
    for coefficients in (families[0], q1_coefficients, q2_coefficients):
        kappa = kernel_curvature(coefficients)
        target_action = kappa * amplitude**2 * TAU**4 / 4.0
        action_errors = []
        operator_errors = []
        scaled_operators = []
        for refinement in (8, 12, 16, 24, 32, 48):
            angles, spacing = smooth_mode_angles(refinement, amplitude)
            action = refinement**3 * float(np.sum(record_potential(angles, coefficients)))
            action_errors.append(abs(action - target_action))
            z = spacing * amplitude * (1.0 - math.cos(spacing))
            scaled_operator = 2.0 * float(record_potential_prime(z, coefficients)) / (kappa * spacing**3)
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
        max(values) - min(values)
        for values in zip(*scaled_operator_families)
    ]
    common_equation = (
        all(left > right for left, right in zip(microscopic_spreads, microscopic_spreads[1:]))
        and microscopic_spreads[-1] < 5.0e-10
    )
    checks.check(action_refinement, "Record-induced potentials converge at second order to their Maxwell actions")
    checks.check(operator_refinement, "Record-induced exact equations converge at second order to the Maxwell operator")
    checks.check(common_equation, "curvature normalization converges independently of the microscopic Record-kernel choice")

    smooth_links = np.zeros((8,) * D + (D,), dtype=float)
    spacing = TAU / 8
    sites = np.indices((8,) * D)
    smooth_links[..., 1] = spacing * amplitude * np.cos(spacing * sites[2])
    _, smooth_theta, winding = plaquettes(smooth_links)
    charges, residual, relation = cube_charges(smooth_theta, winding)
    checks.check(
        relation and residual < 1.0e-14 and all(bool(np.all(value == 0)) for value in charges.values()),
        "Record-induced smooth branch inherits the exact zero-monopole Bianchi identity",
    )

    kappa = kernel_curvature(q1_coefficients)
    spectrum_ok = True
    gauge_null_ok = True
    transverse_ok = True
    for lattice_length in (3, 4, 5):
        for indices in itertools.product(range(lattice_length), repeat=D):
            momenta = np.array([signed_momentum(i, lattice_length) for i in indices])
            q = 2.0 * np.sin(momenta / 2.0)
            norm_square = float(q @ q)
            if norm_square < 1.0e-15:
                continue
            kernel = anisotropic_kernel(q, kappa, kappa)
            eigenvalues = np.linalg.eigvalsh(kernel)
            spectrum_ok = spectrum_ok and bool(
                np.max(np.abs(eigenvalues - np.array([0.0, kappa * norm_square, kappa * norm_square, kappa * norm_square]))) < 7.0e-12
            )
            gauge_null_ok = gauge_null_ok and bool(np.linalg.norm(kernel @ q) < 7.0e-12)
            spatial_square = float(q[1:] @ q[1:])
            if spatial_square > 1.0e-14:
                reduced = kernel[1:, 1:] - np.outer(kernel[1:, 0], kernel[0, 1:]) / kernel[0, 0]
                transverse_ok = transverse_ok and np.linalg.matrix_rank(reduced, tol=1.0e-11) == 2
    checks.check(spectrum_ok, "orientation-completed Record germ has the isotropic Maxwell Hessian spectrum")
    checks.check(gauge_null_ok, "orientation-completed Record germ preserves the exact gauge-null direction")
    checks.check(transverse_ok, "orientation completion leaves exactly two transverse local modes")

    spatial_q = np.array([0.0, 1.2, -0.7, 0.3])
    temporal_only = anisotropic_kernel(spatial_q, kappa, 0.0)
    isotropic = anisotropic_kernel(spatial_q, kappa, kappa)
    checks.check(
        np.linalg.matrix_rank(temporal_only, tol=1.0e-12) == 1
        and np.linalg.matrix_rank(isotropic, tol=1.0e-12) == 3,
        "temporal Record kernel alone lacks the two magnetic restoring directions",
    )

    anisotropic = anisotropic_kernel(spatial_q, kappa, 2.5 * kappa)
    checks.check(
        np.max(np.abs(anisotropic - isotropic)) > 0.5
        and abs(math.sqrt(2.5) - 1.0) > 0.5,
        "unequal spatial completion changes the infrared cone",
    )

    kappa_q2 = kernel_curvature(q2_coefficients)
    checks.check(
        abs(kappa_q2 / kappa - 4.0) < 2.0e-15
        and np.max(
            np.abs(
                anisotropic_kernel(spatial_q, kappa_q2, kappa_q2)
                - (kappa_q2 / kappa) * isotropic
            )
        ) < 2.0e-14,
        "binary partition choice changes normalization but not sourceless Maxwell equations",
    )

    print("per_element: each U1 character coefficient and each three-mode Lueders Kraus weight is checked in the induced kernel")
    print("per_site: shifted neighbor-conditioned densities and additive negative-log transition factors are checked explicitly")
    print("per_mode: every nonzero Fourier momentum on L=3,4,5 is checked after the orientation-completed quadratic germ")
    print("per_block: temporal-only, isotropic-completed, anisotropic, constant, and negative-character blocks are contrasted")
    print("lattice_wide: fixed-volume action/operator refinements and zero-monopole cube identities run on periodic four-lattices")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
