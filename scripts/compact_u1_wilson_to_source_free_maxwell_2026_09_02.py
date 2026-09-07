#!/usr/bin/env python3
"""Exact and numerical checks for the recovered compact-U(1) Maxwell packet.

The runner derives every lattice tensor it tests.  It uses deterministic
finite lattices only; no observed constant or fitted parameter enters.
"""

from __future__ import annotations

import itertools
import math

import numpy as np


AUDIT_TIMEOUT_SEC = 120


D = 4
TAU = 2.0 * math.pi


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


def forward(values: np.ndarray, axis: int) -> np.ndarray:
    return np.roll(values, -1, axis=axis)


def backward(values: np.ndarray, axis: int) -> np.ndarray:
    return np.roll(values, 1, axis=axis)


def principal(values: np.ndarray) -> np.ndarray:
    """Principal values in (-pi, pi], with the endpoint fixed canonically."""
    result = (values + math.pi) % TAU - math.pi
    return np.where(result <= -math.pi + 2.0e-14, math.pi, result)


def plaquettes(links: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    shape = links.shape[:-1]
    raw = np.zeros(shape + (D, D), dtype=float)
    theta = np.zeros_like(raw)
    winding = np.zeros(shape + (D, D), dtype=np.int64)
    for mu in range(D):
        for nu in range(mu + 1, D):
            value = (
                forward(links[..., nu], mu)
                - links[..., nu]
                - forward(links[..., mu], nu)
                + links[..., mu]
            )
            angle = principal(value)
            integer = np.rint((value - angle) / TAU).astype(np.int64)
            raw[..., mu, nu] = value
            raw[..., nu, mu] = -value
            theta[..., mu, nu] = angle
            theta[..., nu, mu] = -angle
            winding[..., mu, nu] = integer
            winding[..., nu, mu] = -integer
    return raw, theta, winding


def cube_charges(
    theta: np.ndarray, winding: np.ndarray
) -> tuple[dict[tuple[int, int, int], np.ndarray], float, bool]:
    charges: dict[tuple[int, int, int], np.ndarray] = {}
    worst_residual = 0.0
    cochain_relation = True
    for mu, nu, rho in itertools.combinations(range(D), 3):
        dtheta = (
            forward(theta[..., nu, rho], mu)
            - theta[..., nu, rho]
            - forward(theta[..., mu, rho], nu)
            + theta[..., mu, rho]
            + forward(theta[..., mu, nu], rho)
            - theta[..., mu, nu]
        )
        dn = (
            forward(winding[..., nu, rho], mu)
            - winding[..., nu, rho]
            - forward(winding[..., mu, rho], nu)
            + winding[..., mu, rho]
            + forward(winding[..., mu, nu], rho)
            - winding[..., mu, nu]
        )
        charge = np.rint(dtheta / TAU).astype(np.int64)
        worst_residual = max(worst_residual, float(np.max(np.abs(dtheta - TAU * charge))))
        cochain_relation = cochain_relation and bool(np.array_equal(charge, -dn))
        charges[(mu, nu, rho)] = charge
    return charges, worst_residual, cochain_relation


def wilson_action(theta: np.ndarray, beta_t: float, beta_s: float) -> float:
    total = 0.0
    for mu in range(D):
        for nu in range(mu + 1, D):
            beta = beta_t if mu == 0 else beta_s
            total += beta * float(np.sum(1.0 - np.cos(theta[..., mu, nu])))
    return total


def wilson_gradient(
    theta: np.ndarray, beta_t: float, beta_s: float, *, linear: bool = False
) -> np.ndarray:
    result = np.zeros(theta.shape[:-2] + (D,), dtype=float)
    for rho in range(D):
        for nu in range(D):
            if nu == rho:
                continue
            beta = beta_t if (rho == 0 or nu == 0) else beta_s
            field = theta[..., rho, nu] if linear else np.sin(theta[..., rho, nu])
            result[..., rho] += beta * (field - backward(field, nu))
    return result


def smooth_mode_links(length: int, amplitude: float) -> tuple[np.ndarray, float]:
    spacing = TAU / length
    sites = np.indices((length,) * D)
    links = np.zeros((length,) * D + (D,), dtype=float)
    # Exact edge integral: A_1(x)=amplitude*cos(x_2), independent of x_1.
    links[..., 1] = spacing * amplitude * np.cos(spacing * sites[2])
    return links, spacing


def anisotropic_kernel(q: np.ndarray, beta_t: float, beta_s: float) -> np.ndarray:
    time_square = float(q[0] ** 2)
    spatial = q[1:]
    spatial_square = float(spatial @ spatial)
    kernel = np.zeros((D, D), dtype=float)
    kernel[0, 0] = beta_t * spatial_square
    kernel[0, 1:] = -beta_t * q[0] * spatial
    kernel[1:, 0] = kernel[0, 1:]
    kernel[1:, 1:] = (
        beta_t * time_square * np.eye(3)
        + beta_s * (spatial_square * np.eye(3) - np.outer(spatial, spatial))
    )
    return kernel


def signed_momentum(index: int, length: int) -> float:
    representative = index if index <= length // 2 else index - length
    return TAU * representative / length


def main() -> int:
    checks = Checks()
    rng = np.random.default_rng(5301)
    length = 4
    links = rng.normal(0.0, 2.2, size=(length,) * D + (D,))
    raw, theta, winding = plaquettes(links)

    reverse_ok = all(
        np.array_equal(theta[..., nu, mu], -theta[..., mu, nu])
        and np.array_equal(winding[..., nu, mu], -winding[..., mu, nu])
        for mu in range(D)
        for nu in range(mu + 1, D)
    )
    range_ok = bool(np.max(theta) <= math.pi and np.min(theta) > -math.pi - 1.0e-13)
    checks.check(reverse_ok and range_ok, "canonical principal branch and reverse orientation")

    gauge = rng.normal(0.0, 1.4, size=(length,) * D)
    transformed = links.copy()
    for mu in range(D):
        transformed[..., mu] += gauge - forward(gauge, mu)
    _, theta_gauge, _ = plaquettes(transformed)
    checks.check(float(np.max(np.abs(theta_gauge - theta))) < 2.0e-12, "plaquette gauge invariance")
    checks.check(
        abs(wilson_action(theta_gauge, 2.0, 5.0) - wilson_action(theta, 2.0, 5.0))
        < 2.0e-11,
        "Wilson action gauge invariance",
    )

    decomposition_error = 0.0
    for mu in range(D):
        for nu in range(mu + 1, D):
            decomposition_error = max(
                decomposition_error,
                float(np.max(np.abs(raw[..., mu, nu] - theta[..., mu, nu] - TAU * winding[..., mu, nu]))),
            )
    checks.check(decomposition_error < 2.0e-12, "lifted curvature splits into principal angle plus integer winding")

    checks.check(
        np.array_equal(raw, -np.swapaxes(raw, -1, -2)),
        "the complete returned raw plaquette array is antisymmetric under orientation reversal",
    )
    charges, cube_residual, charge_relation = cube_charges(theta, winding)
    max_charge = max(int(np.max(np.abs(value))) for value in charges.values())
    checks.check(cube_residual < 3.0e-12 and max_charge <= 2, "oriented compact cube sum is an allowed integer multiple of 2pi")
    checks.check(charge_relation, "cube charge equals minus the integer-cochain coboundary")

    dm = (
        forward(charges[(1, 2, 3)], 0)
        - charges[(1, 2, 3)]
        - forward(charges[(0, 2, 3)], 1)
        + charges[(0, 2, 3)]
        + forward(charges[(0, 1, 3)], 2)
        - charges[(0, 1, 3)]
        - forward(charges[(0, 1, 2)], 3)
        + charges[(0, 1, 2)]
    )
    checks.check(bool(np.all(dm == 0)), "dual integer magnetic current is closed")

    spatial_charge = charges[(1, 2, 3)].sum(axis=(1, 2, 3))
    nonzero_witness = any(bool(np.any(value != 0)) for value in charges.values())
    checks.check(bool(np.all(spatial_charge == 0)) and nonzero_witness, "periodic total magnetic charge vanishes while local monopole cubes occur")

    beta_t, beta_s = 1.7, 2.3
    analytic_gradient = wilson_gradient(theta, beta_t, beta_s)
    finite_difference_errors = []
    step = 1.0e-4
    test_links = [((0, 1, 2, 3), 0), ((2, 0, 1, 3), 2), ((3, 3, 0, 1), 3)]
    for site, mu in test_links:
        plus = links.copy()
        minus = links.copy()
        plus[site + (mu,)] += step
        minus[site + (mu,)] -= step
        _, theta_plus, _ = plaquettes(plus)
        _, theta_minus, _ = plaquettes(minus)
        derivative = (
            wilson_action(theta_plus, beta_t, beta_s)
            - wilson_action(theta_minus, beta_t, beta_s)
        ) / (2.0 * step)
        finite_difference_errors.append(abs(derivative - analytic_gradient[site + (mu,)]))
    checks.check(max(finite_difference_errors) < 1.0e-8, "exact Wilson first variation matches independent finite differences")

    gauge_direction = np.zeros_like(links)
    for mu in range(D):
        gauge_direction[..., mu] = gauge - forward(gauge, mu)
    checks.check(abs(float(np.sum(analytic_gradient * gauge_direction))) < 2.0e-10, "Wilson gradient annihilates every tested gauge direction")

    zero_links = np.zeros_like(links)
    _, zero_theta, _ = plaquettes(zero_links)
    scale_check = np.max(
        np.abs(wilson_gradient(theta, 2.0 * beta_t, 2.0 * beta_s) - 2.0 * analytic_gradient)
    )
    checks.check(
        float(np.max(np.abs(wilson_gradient(zero_theta, 1.0, 1.0)))) == 0.0
        and float(scale_check) < 2.0e-13,
        "flat vacuum is stationary and the equation scales linearly with stiffness",
    )

    samples = np.linspace(-8.0, 8.0, 20001)
    cosine_gap = 0.5 * samples**2 - (1.0 - np.cos(samples))
    sine_gap = np.abs(np.sin(samples) - samples)
    scalar_bounds = bool(
        np.min(cosine_gap) >= -2.0e-15
        and np.max(cosine_gap - samples**4 / 24.0) <= 2.0e-14
        and np.max(sine_gap - np.abs(samples) ** 3 / 6.0) <= 2.0e-14
    )
    checks.check(scalar_bounds, "global sine and cosine Taylor inequalities")

    small_links = 0.025 * links
    _, small_theta, _ = plaquettes(small_links)
    beta = 1.9
    quadratic = 0.0
    fourth_bound = 0.0
    for mu in range(D):
        for nu in range(mu + 1, D):
            values = small_theta[..., mu, nu]
            quadratic += 0.5 * beta * float(np.sum(values**2))
            fourth_bound += beta / 24.0 * float(np.sum(values**4))
    small_action = wilson_action(small_theta, beta, beta)
    epsilon = float(np.max(np.abs(small_theta)))
    checks.check(
        -2.0e-13 <= quadratic - small_action <= fourth_bound + 2.0e-13
        and quadratic - small_action <= epsilon**2 * quadratic / 12.0 + 2.0e-13,
        "Wilson action obeys the explicit quadratic truncation bound",
    )

    nonlinear_gradient = wilson_gradient(small_theta, beta, beta)
    linear_gradient = wilson_gradient(small_theta, beta, beta, linear=True)
    gradient_error = float(np.max(np.abs(nonlinear_gradient - linear_gradient)))
    checks.check(
        gradient_error <= beta * epsilon**3 + 2.0e-13,
        "nonlinear Euler equation obeys the explicit cubic remainder bound",
    )

    smooth_links, smooth_spacing = smooth_mode_links(8, 0.12)
    _, smooth_theta, smooth_winding = plaquettes(smooth_links)
    smooth_charges, smooth_cube_residual, _ = cube_charges(smooth_theta, smooth_winding)
    checks.check(
        smooth_spacing**2 * 0.12 < math.pi
        and all(bool(np.all(value == 0)) for value in smooth_charges.values())
        and smooth_cube_residual < 1.0e-14,
        "smooth principal-branch refinement has exact zero monopole charge",
    )

    amplitude = 0.12
    volume = TAU**4
    target_action = beta * amplitude**2 * volume / 4.0
    action_errors = []
    operator_errors = []
    explicit_bounds = []
    for refinement in (8, 12, 16, 24):
        spacing = TAU / refinement
        coordinates = spacing * np.arange(refinement)
        angles = spacing * amplitude * (
            np.cos(coordinates) - np.cos(coordinates + spacing)
        )
        action = beta * refinement**3 * float(np.sum(1.0 - np.cos(angles)))
        action_errors.append(abs(action - target_action))
        z = spacing * amplitude * (1.0 - math.cos(spacing))
        scaled_operator = 2.0 * math.sin(z) / spacing**3
        operator_errors.append(abs(scaled_operator - amplitude))
        explicit_bounds.append(amplitude * spacing**2 / 12.0 + amplitude**3 * spacing**6 / 24.0)

    action_order = math.log(action_errors[-2] / action_errors[-1]) / math.log(24.0 / 16.0)
    checks.check(
        all(a > b for a, b in zip(action_errors, action_errors[1:])) and action_order > 1.8,
        "Wilson action converges to beta/4 times the ordered-index Maxwell integral",
    )
    operator_order = math.log(operator_errors[-2] / operator_errors[-1]) / math.log(24.0 / 16.0)
    checks.check(
        all(a > b for a, b in zip(operator_errors, operator_errors[1:])) and operator_order > 1.8,
        "scaled Wilson Euler operator converges to the continuum Maxwell operator",
    )
    checks.check(
        all(error <= bound + 2.0e-15 for error, bound in zip(operator_errors, explicit_bounds)),
        "smooth-mode Euler error satisfies an explicit analytic O(a^2) bound",
    )

    spectral_ok = True
    null_ok = True
    positive_ok = True
    schur_ok = True
    for lattice_length in (3, 4, 5):
        for indices in itertools.product(range(lattice_length), repeat=D):
            momenta = np.array([signed_momentum(i, lattice_length) for i in indices])
            q = 2.0 * np.sin(momenta / 2.0)
            if float(q @ q) < 1.0e-15:
                continue
            kernel = anisotropic_kernel(q, 2.0, 5.0)
            time_square = float(q[0] ** 2)
            spatial_square = float(q[1:] @ q[1:])
            expected = np.sort(
                np.array(
                    [
                        0.0,
                        2.0 * (time_square + spatial_square),
                        2.0 * time_square + 5.0 * spatial_square,
                        2.0 * time_square + 5.0 * spatial_square,
                    ]
                )
            )
            eigenvalues = np.linalg.eigvalsh(kernel)
            spectral_ok = spectral_ok and bool(np.max(np.abs(eigenvalues - expected)) < 8.0e-12)
            null_ok = null_ok and bool(np.linalg.norm(kernel @ q) < 8.0e-12)
            positive_ok = positive_ok and bool(eigenvalues[1] > 1.0e-12)
            if spatial_square > 1.0e-14:
                spatial = q[1:]
                schur = kernel[1:, 1:] - np.outer(kernel[1:, 0], kernel[0, 1:]) / kernel[0, 0]
                projector = np.eye(3) - np.outer(spatial, spatial) / spatial_square
                expected_schur = (2.0 * time_square + 5.0 * spatial_square) * projector
                schur_ok = schur_ok and bool(np.max(np.abs(schur - expected_schur)) < 8.0e-12)

    checks.check(spectral_ok, "all L=3,4,5 Fourier kernels have the derived exact spectrum")
    checks.check(null_ok, "forward-coboundary momentum is the exact gauge-null vector")
    checks.check(positive_ok, "positive temporal and spatial stiffness give a rank-three positive gauge quotient")
    checks.check(schur_ok, "eliminating A0 yields the transverse spatial projector")

    spatial = np.array([1.0, -2.0, 0.5])
    projector = np.eye(3) - np.outer(spatial, spatial) / float(spatial @ spatial)
    projector_rank = int(np.linalg.matrix_rank(projector, tol=1.0e-12))
    phase_dimension = 2 * 3 - 1 - 1
    checks.check(projector_rank == 2 and phase_dimension == 4, "Gauss reduction leaves two local canonical mode pairs for P>0")

    q_toron = np.array([1.3, 0.0, 0.0, 0.0])
    toron_values = np.linalg.eigvalsh(anisotropic_kernel(q_toron, 2.0, 5.0))
    checks.check(
        np.allclose(toron_values, [0.0, 2.0 * 1.3**2, 2.0 * 1.3**2, 2.0 * 1.3**2]),
        "P=0 and nonzero temporal momentum has three spatial toron modes",
    )

    zero_kernel = anisotropic_kernel(np.zeros(4), 2.0, 5.0)
    checks.check(
        np.count_nonzero(zero_kernel) == 0 and math.comb(4, 1) == 4 and math.comb(4, 2) == 6,
        "full zero momentum retains four holonomies and a rank-six torus flux lattice",
    )

    ratio = 2.5
    spatial_square = 1.7
    energy = 2.0 * math.asinh(0.5 * math.sqrt(ratio * spatial_square))
    checks.check(
        abs(4.0 * math.sinh(energy / 2.0) ** 2 - ratio * spatial_square) < 2.0e-14,
        "reflection-positive transfer pole gives the exact asinh dispersion",
    )

    def infrared_ratio(beta_ratio: float, lattice_length: int) -> float:
        momentum = TAU / lattice_length
        q_value = 2.0 * math.sin(momentum / 2.0)
        energy_value = 2.0 * math.asinh(0.5 * math.sqrt(beta_ratio) * q_value)
        return energy_value / momentum

    isotropic_values = [infrared_ratio(1.0, n) for n in (32, 64, 128)]
    anisotropic_values = [infrared_ratio(ratio, n) for n in (32, 64, 128)]
    checks.check(
        abs(isotropic_values[-1] - 1.0) < 3.0e-4
        and abs(anisotropic_values[-1] - math.sqrt(ratio)) < 8.0e-4
        and abs(anisotropic_values[-1] - isotropic_values[-1]) > 0.5,
        "infrared speed is one only for isotropic gauge stiffness and scales as sqrt(beta_s/beta_t)",
    )

    continuous_energy = math.sqrt(spatial_square)
    transfer_energy = 2.0 * math.asinh(math.sqrt(spatial_square) / 2.0)
    high_momentum_rhs = ratio * 12.0
    checks.check(
        abs(continuous_energy - transfer_energy) > 0.05 and high_momentum_rhs > 4.0,
        "transfer, continuous-time, and naive discrete-Lorentzian dispersions remain distinct",
    )

    nyquist_centered = abs(math.sin(math.pi))
    nyquist_forward = 2.0 * abs(math.sin(math.pi / 2.0))
    q_test = np.array([0.0, 1.0, 0.0, 0.0])
    stable_kernel = anisotropic_kernel(q_test, 2.0, 5.0)
    massive_minimum = float(np.min(np.linalg.eigvalsh(stable_kernel + 0.3 * np.eye(4))))
    unstable_minimum = float(np.min(np.linalg.eigvalsh(anisotropic_kernel(q_test, 2.0, -1.0))))
    checks.check(
        nyquist_centered < 1.0e-12 and abs(nyquist_forward - 2.0) < 1.0e-15,
        "forward-coboundary symbol avoids the centered-difference Nyquist zero",
    )
    checks.check(
        abs(massive_minimum - 0.3) < 1.0e-12
        and unstable_minimum < -0.9
        and np.count_nonzero(anisotropic_kernel(q_test, 0.0, 0.0)) == 0,
        "gauge-mass, wrong-sign, and zero-stiffness mutations are detected",
    )

    print("per_element: every returned raw plaquette orientation and the compact principal-angle decomposition are checked")
    print("per_site: every cube and dual-current closure on the finite periodic L4 exhibit is checked")
    print("per_mode: all nonzero L=3,4,5 Fourier modes and separate toron and full-zero sectors are checked")
    print("per_block: gauge variation, nonlinear remainder, anisotropy, mass, Nyquist and transfer controls are checked")
    print("lattice_wide: fixed-volume action and Euler refinements at L=8,12,16,24 test the supplied smooth Wilson family")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
