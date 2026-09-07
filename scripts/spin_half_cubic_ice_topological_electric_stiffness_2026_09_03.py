#!/usr/bin/env python3
"""Exact component derivatives and finite-protocol electric-stiffness fits."""

from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from fractions import Fraction

import numpy as np

from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
    CubicIceSampler,
    decode_small,
    electric_flux,
    enumerate_small_ice_sector,
    flippable_count,
    initial_ice,
    small_flip_destinations,
    vertex_degrees,
)


AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md",
    "scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py",
    "scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py",
    "scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py",
    "scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py",
    "scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py",
    "scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py",
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


@dataclass(frozen=True)
class ExactComponent:
    flux: tuple[int, int, int]
    size: int
    total_flippability: int
    minimum_flippability: int
    maximum_flippability: int

    @property
    def mean_flippability(self) -> float:
        return self.total_flippability / self.size


def exact_components() -> tuple[tuple[int, ...], tuple[ExactComponent, ...], bool]:
    states = enumerate_small_ice_sector()
    state_set = set(states)
    destinations = {
        state: tuple(small_flip_destinations(decode_small(state)))
        for state in states
    }
    move_consistency = True
    for state, targets in destinations.items():
        state_flux = electric_flux(decode_small(state))
        target_counts = Counter(targets)
        for target, multiplicity in target_counts.items():
            move_consistency = move_consistency and bool(
                target in state_set
                and electric_flux(decode_small(target)) == state_flux
                and Counter(destinations[target])[state] == multiplicity
            )

    seen: set[int] = set()
    components: list[ExactComponent] = []
    for start in states:
        if start in seen:
            continue
        queue = deque([start])
        seen.add(start)
        members: list[int] = []
        while queue:
            state = queue.popleft()
            members.append(state)
            for target in destinations[state]:
                if target not in seen:
                    seen.add(target)
                    queue.append(target)
        fluxes = {electric_flux(decode_small(state)) for state in members}
        if len(fluxes) != 1:
            raise AssertionError(f"component crosses flux sectors: {fluxes}")
        flippabilities = [len(destinations[state]) for state in members]
        components.append(
            ExactComponent(
                flux=next(iter(fluxes)),
                size=len(members),
                total_flippability=sum(flippabilities),
                minimum_flippability=min(flippabilities),
                maximum_flippability=max(flippabilities),
            )
        )
    return states, tuple(components), move_consistency


def insert_flux_lines(
    occupation: np.ndarray,
    axis: int,
    signed_flux: int,
    line_offset: int = 0,
) -> np.ndarray:
    result = occupation.copy()
    if signed_flux == 0:
        return result
    length = result.shape[0]
    sign = 1 if signed_flux > 0 else -1
    needed = abs(signed_flux)
    transverse = [index for index in range(3) if index != axis]
    inserted = 0
    positions = [
        (first, second)
        for first in range(length)
        for second in range(length)
    ]
    shift = line_offset % len(positions)
    positions = positions[shift:] + positions[:shift]
    for first, second in positions:
        if inserted == needed:
            break
        candidate = result.copy()
        line = [slice(None), slice(None), slice(None), axis]
        line[transverse[0]] = first
        line[transverse[1]] = second
        before = electric_flux(result)
        candidate[tuple(line)] ^= 1
        after = electric_flux(candidate)
        delta = after[axis] - before[axis]
        if delta == sign:
            result = candidate
            inserted += 1
    if inserted != needed:
        raise ValueError(
            f"could insert only {inserted} of {needed} requested flux lines"
        )
    expected = tuple(signed_flux if index == axis else 0 for index in range(3))
    if electric_flux(result) != expected:
        raise AssertionError(
            f"wrong inserted flux: {electric_flux(result)} != {expected}"
        )
    if not np.all(vertex_degrees(result) == 3):
        raise AssertionError("noncontractible alternating loops changed Gauss charge")
    return result


@dataclass(frozen=True)
class FluxChain:
    axis: int
    signed_flux: int
    mean: float
    error: float
    block_means: tuple[float, ...]
    sector_ok: bool


def run_flux_chain(
    length: int,
    axis: int,
    signed_flux: int,
    seed: int,
    *,
    thermal_sweeps: int = 500,
    sample_count: int = 500,
    sweep_stride: int = 2,
    block_count: int = 10,
) -> FluxChain:
    sampler = CubicIceSampler(length, seed)
    sampler.occupation = insert_flux_lines(
        initial_ice(length), axis, signed_flux, line_offset=seed
    )
    expected_flux = tuple(
        signed_flux if index == axis else 0 for index in range(3)
    )
    for _ in range(thermal_sweeps):
        sampler.sweep()
    values: list[float] = []
    for _ in range(sample_count):
        for _ in range(sweep_stride):
            sampler.sweep()
        values.append(float(flippable_count(sampler.occupation)))

    data = np.asarray(values, dtype=float)
    usable = (len(data) // block_count) * block_count
    blocks = data[:usable].reshape(block_count, -1).mean(axis=1)
    mean = float(np.mean(blocks))
    error = float(np.std(blocks, ddof=1) / np.sqrt(block_count))
    sector_ok = bool(
        np.all(vertex_degrees(sampler.occupation) == 3)
        and electric_flux(sampler.occupation) == expected_flux
    )
    return FluxChain(
        axis=axis,
        signed_flux=signed_flux,
        mean=mean,
        error=error,
        block_means=tuple(float(value) for value in blocks),
        sector_ok=sector_ok,
    )


@dataclass(frozen=True)
class FluxOrbitAverage:
    length: int
    flux_magnitude: int
    mean: float
    error: float
    chain_spread: float
    chain_count: int
    sector_ok: bool


def run_flux_orbit(length: int, flux_magnitude: int) -> FluxOrbitAverage:
    chains: list[FluxChain] = []
    if flux_magnitude == 0:
        specifications = [(0, 0, replica) for replica in range(3)]
    else:
        specifications = [
            (axis, sign * flux_magnitude, 0)
            for axis in range(3)
            for sign in (-1, 1)
        ]
    for axis, signed_flux, replica in specifications:
        seed = (
            903_000
            + 10_000 * length
            + 100 * flux_magnitude
            + 10 * axis
            + (1 if signed_flux > 0 else 0)
            + 3 * replica
        )
        chains.append(run_flux_chain(length, axis, signed_flux, seed))

    blocks = np.asarray(
        [value for chain in chains for value in chain.block_means],
        dtype=float,
    )
    chain_means = np.asarray([chain.mean for chain in chains], dtype=float)
    return FluxOrbitAverage(
        length=length,
        flux_magnitude=flux_magnitude,
        mean=float(np.mean(blocks)),
        error=float(np.std(blocks, ddof=1) / np.sqrt(len(blocks))),
        chain_spread=float(np.max(chain_means) - np.min(chain_means)),
        chain_count=len(chains),
        sector_ok=all(chain.sector_ok for chain in chains),
    )


@dataclass(frozen=True)
class LinearFit:
    intercept: float
    slope: float
    slope_error: float
    rms: float


def weighted_linear_fit(
    x_values: np.ndarray,
    y_values: np.ndarray,
    errors: np.ndarray,
) -> LinearFit:
    design = np.column_stack((np.ones_like(x_values), x_values))
    weights = 1.0 / np.maximum(errors, 1.0e-12) ** 2
    normal = design.T @ (weights[:, None] * design)
    covariance = np.linalg.inv(normal)
    coefficients = covariance @ (design.T @ (weights * y_values))
    prediction = design @ coefficients
    return LinearFit(
        intercept=float(coefficients[0]),
        slope=float(coefficients[1]),
        slope_error=float(np.sqrt(covariance[1, 1])),
        rms=float(np.sqrt(np.mean((y_values - prediction) ** 2))),
    )


def common_slope_rss(
    lengths: np.ndarray,
    predictor: np.ndarray,
    values: np.ndarray,
) -> tuple[float, float]:
    unique_lengths = sorted(set(int(value) for value in lengths))
    intercept_columns = np.column_stack(
        [lengths == length for length in unique_lengths]
    ).astype(float)
    design = np.column_stack((intercept_columns, predictor))
    coefficients, *_ = np.linalg.lstsq(design, values, rcond=None)
    residual = values - design @ coefficients
    return float(coefficients[-1]), float(residual @ residual)


def weighted_common_slope(
    lengths: np.ndarray,
    predictor: np.ndarray,
    values: np.ndarray,
    errors: np.ndarray,
) -> tuple[float, float, float]:
    unique_lengths = sorted(set(int(value) for value in lengths))
    intercept_columns = np.column_stack(
        [lengths == length for length in unique_lengths]
    ).astype(float)
    design = np.column_stack((intercept_columns, predictor))
    weights = 1.0 / np.maximum(errors, 1.0e-12) ** 2
    normal = design.T @ (weights[:, None] * design)
    covariance = np.linalg.inv(normal)
    coefficients = covariance @ (design.T @ (weights * values))
    residual = values - design @ coefficients
    return (
        float(coefficients[-1]),
        float(np.sqrt(covariance[-1, -1])),
        float(np.sqrt(np.mean(residual**2))),
    )


def sector_branch_coefficients(
    components: tuple[ExactComponent, ...], delta_sign: int
) -> dict[tuple[int, int, int], Fraction]:
    """Coefficient of delta V on each finite sector's selected ground branch.

    RK zero states have disjoint component supports. For negative delta V
    the largest component mean wins; for positive delta V the smallest wins.
    Averaging all configurations in a sector is a different operation.
    """
    if delta_sign not in (-1, 1):
        raise ValueError("delta_sign must be -1 or +1")
    means_by_flux: dict[tuple[int, int, int], list[Fraction]] = defaultdict(list)
    for component in components:
        means_by_flux[component.flux].append(
            Fraction(component.total_flippability, component.size)
        )
    return {
        flux: max(means) if delta_sign < 0 else min(means)
        for flux, means in means_by_flux.items()
    }


def main() -> int:
    checks = Checks()

    states, components, moves_ok = exact_components()
    checks.check(
        len(states) == 9600
        and len(components) == 937
        and sum(component.size for component in components) == len(states)
        and moves_ok,
        "the exact L=2 move graph partitions all ice states into flux-preserving reversible components",
    )

    mobile_components = [component for component in components if component.size > 1]
    zero_mobile = [
        component
        for component in mobile_components
        if component.flux == (0, 0, 0)
    ]
    maximum_mean = max(
        component.mean_flippability for component in mobile_components
    )
    checks.check(
        len(zero_mobile) == 1
        and zero_mobile[0].size == 864
        and zero_mobile[0].total_flippability == 864 * 8
        and sum(
            abs(component.mean_flippability - maximum_mean) < 1.0e-14
            for component in mobile_components
        )
        == 1,
        "the unique most-flippable L=2 mobile component lies in the zero-electric-flux sector",
    )

    unit_flux = [
        component
        for component in mobile_components
        if sum(value * value for value in component.flux) == 1
    ]
    checks.check(
        len(unit_flux) == 6
        and all(component.size == 464 for component in unit_flux)
        and all(
            component.total_flippability * 29 == 188 * component.size
            for component in unit_flux
        )
        and all(
            abs(
                zero_mobile[0].mean_flippability
                - component.mean_flippability
                - 44.0 / 29.0
            )
            < 1.0e-14
            for component in unit_flux
        ),
        "all six unit-flux L=2 sectors have one exact cubic- and inversion-degenerate energy cost",
    )

    maximum_by_flux: dict[tuple[int, int, int], float] = defaultdict(float)
    for component in components:
        maximum_by_flux[component.flux] = max(
            maximum_by_flux[component.flux], component.mean_flippability
        )
    checks.check(
        all(
            value < zero_mobile[0].mean_flippability
            for flux, value in maximum_by_flux.items()
            if flux != (0, 0, 0)
        )
        and any(component.size == 1 for component in components),
        "negative delta V selects zero flux while the opposite sign provides a frozen-sector control",
    )
    negative_branches = sector_branch_coefficients(components, -1)
    positive_branches = sector_branch_coefficients(components, 1)
    zero_components = [component for component in components if component.flux == (0, 0, 0)]
    whole_zero_mean = Fraction(
        sum(component.total_flippability for component in zero_components),
        sum(component.size for component in zero_components),
    )
    checks.check(
        negative_branches[(0, 0, 0)] == 8
        and positive_branches[(0, 0, 0)] == 0
        and whole_zero_mean == Fraction(432, 55)
        and whole_zero_mean != negative_branches[(0, 0, 0)]
        and all(
            negative_branches[component.flux] == Fraction(188, 29)
            for component in unit_flux
        )
        and all(
            Fraction(component.total_flippability, component.size)
            <= negative_branches[component.flux]
            and Fraction(component.total_flippability, component.size)
            >= positive_branches[component.flux]
            for component in components
        ),
        "exact signed component-branch choices differ from a uniform whole-sector mean",
    )

    orbit_results: dict[int, list[FluxOrbitAverage]] = {}
    for length in (6, 8, 10, 12):
        orbit_results[length] = [
            run_flux_orbit(length, flux)
            for flux in range(length // 2 + 1)
        ]
    checks.check(
        all(
            result.sector_ok
            for results in orbit_results.values()
            for result in results
        ),
        "every large-volume chain preserves exact Gauss charge and its constructed signed electric flux",
    )

    per_length_fits: dict[int, LinearFit] = {}
    for length, results in orbit_results.items():
        fluxes = np.asarray(
            [result.flux_magnitude for result in results], dtype=float
        )
        values = np.asarray([result.mean for result in results], dtype=float)
        errors = np.asarray([result.error for result in results], dtype=float)
        per_length_fits[length] = weighted_linear_fit(
            fluxes**2 / length, values, errors
        )
    stiffness_coefficients = np.asarray(
        [-fit.slope for fit in per_length_fits.values()], dtype=float
    )
    stiffness_errors = np.asarray(
        [fit.slope_error for fit in per_length_fits.values()], dtype=float
    )
    checks.check(
        np.all(stiffness_coefficients > 0.0)
        and np.all(stiffness_coefficients > 3.0 * stiffness_errors),
        "each finite-volume sampling fit has a positive quadratic coefficient relative to nominal block errors",
    )
    checks.check(
        np.ptp(stiffness_coefficients) / np.mean(stiffness_coefficients) < 0.5,
        "the Phi-squared-over-L coefficient remains finite and size-stable across four volumes",
    )

    lengths = []
    fluxes = []
    values = []
    errors = []
    for length, results in orbit_results.items():
        for result in results:
            lengths.append(float(length))
            fluxes.append(float(result.flux_magnitude))
            values.append(result.mean)
            errors.append(result.error)
    length_array = np.asarray(lengths)
    flux_array = np.asarray(fluxes)
    value_array = np.asarray(values)
    error_array = np.asarray(errors)
    predictor = flux_array**2 / length_array
    weighted_slope, weighted_slope_error, weighted_rms = weighted_common_slope(
        length_array, predictor, value_array, error_array
    )
    quadratic_slope, quadratic_rss = common_slope_rss(
        length_array, predictor, value_array
    )
    controls = {
        "Phi": common_slope_rss(length_array, flux_array, value_array)[1],
        "Phi/L": common_slope_rss(
            length_array, flux_array / length_array, value_array
        )[1],
        "Phi^2": common_slope_rss(
            length_array, flux_array**2, value_array
        )[1],
        "sector_step": common_slope_rss(
            length_array, (flux_array > 0).astype(float), value_array
        )[1],
    }
    checks.check(
        quadratic_slope < 0.0
        and quadratic_rss < 0.75 * min(controls.values()),
        "the common Phi-squared-over-L law beats linear, unscaled-quadratic, and sector-step controls",
    )

    collapse_stiffness = -quadratic_slope
    weighted_stiffness = -weighted_slope
    common_stiffness_spread = float(np.ptp(stiffness_coefficients))
    relative_stiffness_spread = float(
        common_stiffness_spread / np.mean(stiffness_coefficients)
    )
    checks.check(
        collapse_stiffness > 0.0
        and relative_stiffness_spread < 0.5
        and weighted_stiffness > 5.0 * weighted_slope_error
        and abs(weighted_stiffness - collapse_stiffness) / weighted_stiffness
        < 0.25,
        "the finite-protocol fits give a positive Maxwell-normalized parameter U_fit/abs(delta V)=2c",
    )

    maximum_flux_density = max(
        result.flux_magnitude / result.length**2
        for results in orbit_results.values()
        for result in results
    )
    terminal_flux_density = [
        results[-1].flux_magnitude / length**2
        for length, results in orbit_results.items()
    ]
    checks.check(
        maximum_flux_density <= 1.0 / 12.0
        and all(
            terminal_flux_density[index + 1] < terminal_flux_density[index]
            for index in range(len(terminal_flux_density) - 1)
        ),
        "the fitted flux window becomes a shrinking field-density probe under volume refinement",
    )

    maximum_normalized_chain_spread = max(
        result.chain_spread / (result.error * np.sqrt(result.chain_count))
        for results in orbit_results.values()
        for result in results
        if result.flux_magnitude > 0
    )
    checks.check(
        maximum_normalized_chain_spread < 4.0,
        "signed-axis means agree within four single-chain standard errors at every nonzero flux",
    )

    print(
        "diagnostic exact graph:",
        f"states={len(states)}",
        f"components={len(components)}",
        f"mobile={len(mobile_components)}",
        f"zero_mean={zero_mobile[0].mean_flippability:.8f}",
        f"unit_mean={unit_flux[0].mean_flippability:.8f}",
        f"unit_cost={44.0 / 29.0:.8f}",
        f"whole_zero_mean={whole_zero_mean}",
        f"negative_zero_branch={negative_branches[(0, 0, 0)]}",
        f"positive_zero_branch={positive_branches[(0, 0, 0)]}",
    )
    for length, results in orbit_results.items():
        print(
            f"diagnostic L={length} orbit means:",
            " ".join(
                f"Phi={result.flux_magnitude}:{result.mean:.5f}"
                f"+/-{result.error:.5f}"
                f"[spread={result.chain_spread:.5f}]"
                for result in results
            ),
        )
        fit = per_length_fits[length]
        print(
            f"diagnostic L={length} finite-protocol fit:",
            f"c={-fit.slope:.6f}",
            f"error={fit.slope_error:.6f}",
            f"rms={fit.rms:.6f}",
        )
    print(
        "diagnostic common scaling:",
        f"c={weighted_stiffness:.6f}+/-{weighted_slope_error:.6f}",
        f"unweighted_c={collapse_stiffness:.6f}",
        f"weighted_rms={weighted_rms:.6f}",
        f"relative_c_spread={relative_stiffness_spread:.6f}",
        f"U_fit/abs(deltaV)={2.0 * weighted_stiffness:.6f}",
        f"rss={quadratic_rss:.6f}",
        "controls=" + ",".join(
            f"{name}:{value:.6f}" for name, value in controls.items()
        ),
        f"max_normalized_chain_spread={maximum_normalized_chain_spread:.6f}",
    )
    print(
        "per_element: each noncontractible alternating loop and each local plaquette move are checked"
    )
    print(
        "per_site: exact three-of-six Gauss charge is preserved in every signed-flux chain"
    )
    print(
        "per_mode: finite-protocol flippability fits have positive Maxwell-normalized coefficients; microscopic U is conditional"
    )
    print(
        "per_block: all 9600 L=2 states and signed-axis Monte Carlo orbits on L=6 through L=12 are checked"
    )
    print(
        "lattice_wide: exact L=2 component costs and finite sampling fits are checked; sector-ground and thermodynamic identification remain open"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
