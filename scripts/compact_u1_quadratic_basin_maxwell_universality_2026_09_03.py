#!/usr/bin/env python3
"""Checks for the compact-U(1) quadratic-basin Maxwell universality theorem.

The theorem concerns an even, 2*pi-periodic, one-plaquette potential whose
germ at the flat connection has positive curvature.  The explicit harmonic
family below supplies genuinely different microscopic laws with the same
germ.  Zero-curvature, wrong-sign, and anisotropic mutations keep the scope
honest.
"""

from __future__ import annotations

import itertools
import math

import numpy as np

from compact_u1_wilson_to_source_free_maxwell_2026_09_02 import (
    D,
    TAU,
    anisotropic_kernel,
    backward,
    cube_charges,
    forward,
    plaquettes,
    signed_momentum,
)


AUDIT_TIMEOUT_SEC = 120


AUDIT_INPUT_PATHS = (
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
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


def harmonic_potential(values: np.ndarray | float, lam: float) -> np.ndarray | float:
    """Positive periodic family with V''(0)=1 for every lam >= 0."""
    return ((1.0 - np.cos(values)) + 0.25 * lam * (1.0 - np.cos(2.0 * values))) / (1.0 + lam)


def harmonic_derivative(values: np.ndarray | float, lam: float) -> np.ndarray | float:
    return (np.sin(values) + 0.5 * lam * np.sin(2.0 * values)) / (1.0 + lam)


def fourth_derivative_bound(lam: float) -> float:
    return (1.0 + 4.0 * lam) / (1.0 + lam)


def plaquette_action(
    theta: np.ndarray,
    lam: float,
    kappa_t: float = 1.0,
    kappa_s: float = 1.0,
) -> float:
    total = 0.0
    for mu in range(D):
        for nu in range(mu + 1, D):
            kappa = kappa_t if mu == 0 else kappa_s
            total += kappa * float(np.sum(harmonic_potential(theta[..., mu, nu], lam)))
    return total


def plaquette_gradient(
    theta: np.ndarray,
    lam: float,
    kappa_t: float = 1.0,
    kappa_s: float = 1.0,
    *,
    linear: bool = False,
) -> np.ndarray:
    result = np.zeros(theta.shape[:-2] + (D,), dtype=float)
    for rho in range(D):
        for nu in range(D):
            if nu == rho:
                continue
            kappa = kappa_t if (rho == 0 or nu == 0) else kappa_s
            oriented = theta[..., rho, nu]
            field = oriented if linear else harmonic_derivative(oriented, lam)
            result[..., rho] += kappa * (field - backward(field, nu))
    return result


def quartic_potential(values: np.ndarray | float) -> np.ndarray | float:
    return (1.0 - np.cos(values)) ** 2


def quartic_derivative(values: np.ndarray | float) -> np.ndarray | float:
    return 2.0 * (1.0 - np.cos(values)) * np.sin(values)


def smooth_mode_angles(length: int, amplitude: float) -> tuple[np.ndarray, float]:
    spacing = TAU / length
    coordinates = spacing * np.arange(length)
    angles = spacing * amplitude * (np.cos(coordinates) - np.cos(coordinates + spacing))
    return angles, spacing


def main() -> int:
    checks = Checks()
    lambdas = (0.0, 0.5, 2.0)
    scalar_grid = np.linspace(-math.pi, math.pi, 40001)

    periodic_even = True
    positive = True
    taylor_action = True
    taylor_gradient = True
    curvature = True
    h = 1.0e-5
    for lam in lambdas:
        values = harmonic_potential(scalar_grid, lam)
        periodic_even = periodic_even and bool(
            np.max(np.abs(values - harmonic_potential(-scalar_grid, lam))) < 2.0e-15
            and np.max(np.abs(values - harmonic_potential(scalar_grid + TAU, lam))) < 4.0e-15
        )
        positive = positive and bool(np.min(values) >= -2.0e-16)
        m4 = fourth_derivative_bound(lam)
        taylor_action = taylor_action and bool(
            np.max(np.abs(values - 0.5 * scalar_grid**2) - m4 * scalar_grid**4 / 24.0) < 3.0e-15
        )
        derivative = harmonic_derivative(scalar_grid, lam)
        taylor_gradient = taylor_gradient and bool(
            np.max(np.abs(derivative - scalar_grid) - m4 * np.abs(scalar_grid) ** 3 / 6.0) < 3.0e-15
        )
        numerical_curvature = (
            harmonic_potential(h, lam) - 2.0 * harmonic_potential(0.0, lam) + harmonic_potential(-h, lam)
        ) / h**2
        curvature = curvature and abs(float(numerical_curvature) - 1.0) < 2.0e-6

    checks.check(periodic_even, "representative laws are even and exactly 2pi-periodic")
    checks.check(positive, "representative laws have a common stable flat minimum")
    checks.check(curvature, "distinct microscopic laws have common unit flat-background curvature")
    checks.check(taylor_action, "C4 action remainder obeys the uniform fourth-derivative bound")
    checks.check(taylor_gradient, "C4 first-variation remainder obeys the uniform cubic bound")

    probe_angle = 1.137
    finite_values = [float(harmonic_potential(probe_angle, lam)) for lam in lambdas]
    finite_slopes = [float(harmonic_derivative(probe_angle, lam)) for lam in lambdas]
    checks.check(
        min(abs(a - b) for a, b in itertools.combinations(finite_values, 2)) > 1.0e-3,
        "same-curvature laws remain distinct at finite plaquette angle",
    )
    checks.check(
        min(abs(a - b) for a, b in itertools.combinations(finite_slopes, 2)) > 1.0e-3,
        "same-curvature exact lattice equations remain microscopically distinct",
    )

    rng = np.random.default_rng(90301)
    length = 3
    links = rng.normal(0.0, 0.23, size=(length,) * D + (D,))
    _, theta, _ = plaquettes(links)
    gauge = rng.normal(0.0, 0.41, size=(length,) * D)
    transformed = links.copy()
    for mu in range(D):
        transformed[..., mu] += gauge - forward(gauge, mu)
    _, transformed_theta, _ = plaquettes(transformed)
    checks.check(
        max(
            abs(plaquette_action(theta, lam) - plaquette_action(transformed_theta, lam))
            for lam in lambdas
        ) < 2.0e-12,
        "every representative action is exactly link-gauge invariant",
    )

    finite_difference_ok = True
    step = 2.0e-5
    sites = [((0, 1, 2, 0), 0), ((2, 0, 1, 2), 2), ((1, 2, 0, 1), 3)]
    for lam in lambdas:
        analytic = plaquette_gradient(theta, lam, 1.3, 2.1)
        for site, mu in sites:
            plus = links.copy()
            minus = links.copy()
            plus[site + (mu,)] += step
            minus[site + (mu,)] -= step
            _, theta_plus, _ = plaquettes(plus)
            _, theta_minus, _ = plaquettes(minus)
            numeric = (
                plaquette_action(theta_plus, lam, 1.3, 2.1)
                - plaquette_action(theta_minus, lam, 1.3, 2.1)
            ) / (2.0 * step)
            finite_difference_ok = finite_difference_ok and abs(numeric - analytic[site + (mu,)]) < 2.0e-8
    checks.check(finite_difference_ok, "generic exact link equation matches independent finite differences")

    gauge_direction = np.zeros_like(links)
    for mu in range(D):
        gauge_direction[..., mu] = gauge - forward(gauge, mu)
    checks.check(
        max(
            abs(float(np.sum(plaquette_gradient(theta, lam) * gauge_direction)))
            for lam in lambdas
        ) < 3.0e-12,
        "generic exact gradients annihilate tested gauge directions",
    )

    small_links = 0.035 * links
    _, small_theta, _ = plaquettes(small_links)
    epsilon = float(np.max(np.abs(small_theta)))
    local_action_bounds = True
    local_gradient_bounds = True
    quadratic = 0.0
    for mu in range(D):
        for nu in range(mu + 1, D):
            quadratic += 0.5 * float(np.sum(small_theta[..., mu, nu] ** 2))
    linear_gradient = plaquette_gradient(small_theta, 0.0, linear=True)
    for lam in lambdas:
        m4 = fourth_derivative_bound(lam)
        action_error = abs(plaquette_action(small_theta, lam) - quadratic)
        fourth_sum = 0.0
        for mu in range(D):
            for nu in range(mu + 1, D):
                fourth_sum += float(np.sum(small_theta[..., mu, nu] ** 4))
        local_action_bounds = local_action_bounds and action_error <= m4 * fourth_sum / 24.0 + 3.0e-13
        gradient_error = float(np.max(np.abs(plaquette_gradient(small_theta, lam) - linear_gradient)))
        local_gradient_bounds = local_gradient_bounds and gradient_error <= m4 * epsilon**3 + 3.0e-13
    checks.check(local_action_bounds, "finite-lattice actions obey their common quadratic-germ bounds")
    checks.check(local_gradient_bounds, "finite-lattice equations obey their common linearized bounds")

    flat_theta = np.zeros_like(theta)
    checks.check(
        all(float(np.max(np.abs(plaquette_gradient(flat_theta, lam)))) == 0.0 for lam in lambdas),
        "flat connection is stationary throughout the tested basin",
    )

    direction = rng.normal(0.0, 1.0, size=links.shape)
    _, direction_theta, _ = plaquettes(direction)
    hessian_ok = True
    for lam in lambdas:
        hessian_errors = []
        for scale in (1.0e-2, 5.0e-3, 2.5e-3):
            numeric_hessian_action = 2.0 * plaquette_action(scale * direction_theta, lam) / scale**2
            exact_hessian_action = 0.0
            for mu in range(D):
                for nu in range(mu + 1, D):
                    exact_hessian_action += float(np.sum(direction_theta[..., mu, nu] ** 2))
            hessian_errors.append(abs(numeric_hessian_action - exact_hessian_action))
        hessian_ok = hessian_ok and all(
            left > 3.9 * right for left, right in zip(hessian_errors, hessian_errors[1:])
        ) and hessian_errors[-1] / exact_hessian_action < 1.0e-5
    checks.check(hessian_ok, "flat-background Hessians collapse to one common gauge quadratic form")

    smooth_links = np.zeros((8,) * D + (D,), dtype=float)
    spacing = TAU / 8
    sites_grid = np.indices((8,) * D)
    smooth_links[..., 1] = spacing * 0.12 * np.cos(spacing * sites_grid[2])
    _, smooth_theta, smooth_winding = plaquettes(smooth_links)
    charges, cube_residual, relation = cube_charges(smooth_theta, smooth_winding)
    checks.check(
        relation
        and cube_residual < 1.0e-14
        and all(bool(np.all(value == 0)) for value in charges.values()),
        "smooth principal branch inherits the exact zero-monopole Bianchi sector",
    )

    amplitude = 0.12
    target_action = amplitude**2 * TAU**4 / 4.0
    continuum_action_ok = True
    common_limit_ok = True
    operator_ok = True
    operator_bound_ok = True
    final_actions: list[float] = []
    for lam in lambdas:
        action_errors = []
        operator_errors = []
        analytic_bounds = []
        actions = []
        for refinement in (8, 12, 16, 24, 32, 48):
            angles, a = smooth_mode_angles(refinement, amplitude)
            action = refinement**3 * float(np.sum(harmonic_potential(angles, lam)))
            actions.append(action)
            action_errors.append(abs(action - target_action))
            z = a * amplitude * (1.0 - math.cos(a))
            scaled_operator = 2.0 * float(harmonic_derivative(z, lam)) / a**3
            operator_errors.append(abs(scaled_operator - amplitude))
            analytic_bounds.append(
                amplitude * a**2 / 12.0
                + fourth_derivative_bound(lam) * amplitude**3 * a**6 / 24.0
            )
        continuum_action_ok = continuum_action_ok and all(
            left > right for left, right in zip(action_errors, action_errors[1:])
        ) and math.log(action_errors[-2] / action_errors[-1]) / math.log(48.0 / 32.0) > 1.95
        operator_ok = operator_ok and all(
            left > right for left, right in zip(operator_errors, operator_errors[1:])
        ) and math.log(operator_errors[-2] / operator_errors[-1]) / math.log(48.0 / 32.0) > 1.95
        operator_bound_ok = operator_bound_ok and all(
            error <= bound + 3.0e-15 for error, bound in zip(operator_errors, analytic_bounds)
        )
        final_actions.append(actions[-1])
    common_limit_ok = (
        max(abs(value - target_action) for value in final_actions) < 0.009
        and max(final_actions) - min(final_actions) < 4.0e-6
    )
    checks.check(continuum_action_ok, "all distinct laws converge at second order to the Maxwell action")
    checks.check(common_limit_ok, "same-curvature laws share one normalized continuum action")
    checks.check(operator_ok, "all exact nonlinear equations converge at second order to the Maxwell operator")
    checks.check(operator_bound_ok, "all smooth-mode operators satisfy the explicit analytic error bound")

    spectral_ok = True
    gauge_null_ok = True
    schur_ok = True
    for lattice_length in (3, 4, 5):
        for indices in itertools.product(range(lattice_length), repeat=D):
            momenta = np.array([signed_momentum(i, lattice_length) for i in indices])
            q = 2.0 * np.sin(momenta / 2.0)
            norm_square = float(q @ q)
            if norm_square < 1.0e-15:
                continue
            kernel = anisotropic_kernel(q, 1.0, 1.0)
            eigenvalues = np.linalg.eigvalsh(kernel)
            spectral_ok = spectral_ok and bool(
                np.max(np.abs(eigenvalues - np.array([0.0, norm_square, norm_square, norm_square]))) < 7.0e-12
            )
            gauge_null_ok = gauge_null_ok and bool(np.linalg.norm(kernel @ q) < 7.0e-12)
            spatial_square = float(q[1:] @ q[1:])
            if spatial_square > 1.0e-14:
                spatial = q[1:]
                reduced = kernel[1:, 1:] - np.outer(kernel[1:, 0], kernel[0, 1:]) / kernel[0, 0]
                projector = np.eye(3) - np.outer(spatial, spatial) / spatial_square
                schur_ok = schur_ok and bool(
                    np.max(np.abs(reduced - norm_square * projector)) < 7.0e-12
                    and np.linalg.matrix_rank(projector, tol=1.0e-12) == 2
                )
    checks.check(spectral_ok, "common Hessian has the exact rank-three Euclidean spectrum")
    checks.check(gauge_null_ok, "common Hessian retains the exact gauge-null direction")
    checks.check(schur_ok, "Gauss elimination leaves exactly two transverse local modes")

    zero_curvature_actions = []
    zero_curvature_operators = []
    for refinement in (8, 12, 16, 24, 48):
        angles, a = smooth_mode_angles(refinement, amplitude)
        zero_curvature_actions.append(refinement**3 * float(np.sum(quartic_potential(angles))))
        z = a * amplitude * (1.0 - math.cos(a))
        zero_curvature_operators.append(2.0 * float(quartic_derivative(z)) / a**3)
    checks.check(
        zero_curvature_actions[-1] < zero_curvature_actions[0] / 50.0
        and zero_curvature_actions[-1] < target_action / 1000.0,
        "zero-curvature mutation collapses instead of producing finite Maxwell action",
    )
    checks.check(
        zero_curvature_operators[-1] < zero_curvature_operators[0] / 30000.0
        and zero_curvature_operators[-1] < amplitude / 5.0e7,
        "zero-curvature mutation loses the scaled Maxwell equation",
    )

    q = np.array([0.0, 1.2, -0.7, 0.3])
    anisotropic = anisotropic_kernel(q, 1.0, 2.5)
    wrong_sign = anisotropic_kernel(q, 1.0, -0.4)
    isotropic = anisotropic_kernel(q, 1.0, 1.0)
    checks.check(
        np.max(np.abs(anisotropic - isotropic)) > 1.0
        and abs(math.sqrt(2.5) - 1.0) > 0.5,
        "anisotropic curvature mutation changes the infrared cone",
    )
    checks.check(
        float(np.min(np.linalg.eigvalsh(wrong_sign))) < -0.7,
        "wrong-sign spatial curvature mutation creates unstable transverse directions",
    )

    scaled_kernel = anisotropic_kernel(q, 3.7, 3.7)
    checks.check(
        np.max(np.abs(scaled_kernel - 3.7 * isotropic)) < 2.0e-14
        and np.linalg.norm(scaled_kernel @ q) < 2.0e-14,
        "common positive curvature rescales but does not change sourceless Maxwell equations",
    )

    print("per_element: every representative potential is checked across the full principal-angle interval with analytic Taylor bounds")
    print("per_site: exact link gradients are checked against independent finite differences on a periodic four-dimensional lattice")
    print("per_mode: every nonzero Fourier momentum on L=3,4,5 is checked for the common spectrum and exact gauge null")
    print("per_block: temporal and spatial curvature blocks are Schur-reduced and challenged by anisotropic and wrong-sign controls")
    print("lattice_wide: fixed-volume refinement and exact zero-monopole cube identities are executed on periodic four-lattices")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
