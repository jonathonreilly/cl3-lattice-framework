#!/usr/bin/env python3
"""Finite-detuning charge response in the spin-half cubic-ice model."""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt

import numpy as np
from scipy import sparse
from scipy.sparse.linalg import eigsh

from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import (
    blocked_mean_and_error,
    build_geometry,
    count_flippable,
    run_population_core,
)
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
    build_small_rk_orbit,
    decode_small,
    electric_flux,
    gauss_charges,
    initial_ice,
    small_flip_destinations,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py",
    "scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py",
)

AUDIT_TIMEOUT_SEC = 480


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


def directed_charge_start(
    length: int,
    segments: tuple[tuple[int, int], ...],
) -> tuple[np.ndarray, tuple[int, int, int]]:
    """Flip a directed alternating path and leave only its endpoint charges."""
    occupation = initial_ice(length)
    position = [0, 0, 0]
    displacement = [0, 0, 0]
    used_links: set[tuple[int, int, int, int]] = set()
    for axis, signed_steps in segments:
        if axis not in (0, 1, 2) or signed_steps == 0:
            raise ValueError("each path segment needs an axis and nonzero step")
        direction = 1 if signed_steps > 0 else -1
        for _ in range(abs(signed_steps)):
            if direction > 0:
                root = tuple(position)
                next_position = position.copy()
                next_position[axis] = (next_position[axis] + 1) % length
            else:
                next_position = position.copy()
                next_position[axis] = (next_position[axis] - 1) % length
                root = tuple(next_position)
            link = (*root, axis)
            if link in used_links:
                raise ValueError("directed path reuses a physical link")
            occupation_number = int(occupation[link])
            electric_change = (-1) ** sum(root) * (1 - 2 * occupation_number)
            if electric_change != direction:
                raise ValueError(
                    f"segment does not follow the alternating electric arrow at {link}"
                )
            occupation[link] ^= 1
            used_links.add(link)
            position = next_position
            displacement[axis] += direction
    charges = gauss_charges(occupation)
    if sorted(int(value) for value in charges[charges != 0]) != [-1, 1]:
        raise AssertionError("directed path did not leave exactly two unit charges")
    return occupation, tuple(displacement)


def axial_segments(separation: int) -> tuple[tuple[int, int], ...]:
    return ((0, separation),)


@dataclass(frozen=True)
class ChargeResult:
    length: int
    delta_v: float
    displacement: tuple[int, int, int]
    energy: float
    energy_error: float
    charge_signature: tuple[int, ...]
    plane_flux: tuple[int, int, int]
    minimum_effective_population_fraction: float
    final_unique_fraction: float
    count_consistent: bool
    charge_consistent: bool

    @property
    def distance(self) -> float:
        return sqrt(sum(component**2 for component in self.displacement))


def run_charge_population(
    length: int,
    delta_v: float,
    segments: tuple[tuple[int, int], ...] | None,
    *,
    population: int,
    classical_sweeps: int,
    burn_sweeps: int,
    sample_sweeps: int,
    seed: int,
) -> ChargeResult:
    if segments is None:
        occupation = initial_ice(length)
        displacement = (0, 0, 0)
    else:
        occupation, displacement = directed_charge_start(length, segments)
    initial_charges = gauss_charges(occupation)
    initial_flux = electric_flux(occupation)
    geometry = build_geometry(length)
    (
        samples,
        effective_populations,
        count_checks,
        final_states,
        final_counts,
    ) = run_population_core(
        occupation.ravel(),
        geometry.plaquette_links,
        geometry.affected_plaquettes,
        geometry.affected_counts,
        delta_v,
        population,
        classical_sweeps,
        burn_sweeps,
        sample_sweeps,
        max(16, geometry.plaquette_count // 8),
        seed,
    )
    mean, error = blocked_mean_and_error(samples)
    charge_consistent = True
    for state in final_states:
        final_occupation = state.reshape((length, length, length, 3))
        charge_consistent = charge_consistent and bool(
            np.array_equal(gauss_charges(final_occupation), initial_charges)
        )
    count_consistent = bool(
        np.all(count_checks == 0)
        and all(
            count_flippable(state, geometry.plaquette_links) == count
            for state, count in zip(final_states, final_counts, strict=True)
        )
    )
    packed = np.packbits(final_states, axis=1)
    unique_fraction = np.unique(packed, axis=0).shape[0] / population
    return ChargeResult(
        length=length,
        delta_v=delta_v,
        displacement=displacement,
        energy=delta_v * mean,
        energy_error=abs(delta_v) * error,
        charge_signature=tuple(
            sorted(int(value) for value in initial_charges[initial_charges != 0])
        ),
        plane_flux=initial_flux,
        minimum_effective_population_fraction=float(
            np.min(effective_populations) / population
        ),
        final_unique_fraction=float(unique_fraction),
        count_consistent=count_consistent,
        charge_consistent=charge_consistent,
    )


def periodic_green(length: int, displacement: tuple[int, int, int]) -> float:
    result = 0.0
    vector = np.asarray(displacement, dtype=float)
    for mode in np.ndindex(length, length, length):
        if mode == (0, 0, 0):
            continue
        momentum = 2.0 * np.pi * np.asarray(mode, dtype=float) / length
        eigenvalue = 4.0 * float(np.sum(np.sin(momentum / 2.0) ** 2))
        result += float(np.cos(momentum @ vector)) / eigenvalue
    return result / length**3


def coulomb_coordinate(length: int, displacement: tuple[int, int, int]) -> float:
    origin = periodic_green(length, (0, 0, 0))
    separated = periodic_green(length, displacement)
    harmonic = sum(component**2 for component in displacement) / (
        2.0 * length**3
    )
    return origin - separated + harmonic


@dataclass(frozen=True)
class ResponseFit:
    coefficient: float
    coefficient_error: float
    rss: float


def fit_response(
    results_by_length: dict[int, list[ChargeResult]],
    model: str,
) -> ResponseFit:
    lengths = sorted(results_by_length)
    rows = [
        result
        for length in lengths
        for result in results_by_length[length]
        if result.displacement != (0, 0, 0)
    ]
    intercepts = np.column_stack(
        [np.asarray([result.length == length for result in rows], dtype=float) for length in lengths]
    )
    if model == "coulomb":
        predictor = np.asarray(
            [coulomb_coordinate(result.length, result.displacement) for result in rows]
        )
    elif model == "inverse_distance":
        predictor = np.asarray([-1.0 / result.distance for result in rows])
    elif model == "linear_distance":
        predictor = np.asarray([result.distance for result in rows])
    elif model == "quadratic_distance":
        predictor = np.asarray([result.distance**2 for result in rows])
    elif model == "constant":
        prediction = np.asarray(
            [
                np.mean(
                    [item.energy for item in results_by_length[result.length] if item.displacement != (0, 0, 0)]
                )
                for result in rows
            ]
        )
        values = np.asarray([result.energy for result in rows])
        return ResponseFit(0.0, 0.0, float(np.sum((values - prediction) ** 2)))
    else:
        raise ValueError(model)
    design = np.column_stack((intercepts, predictor))
    values = np.asarray([result.energy for result in rows], dtype=float)
    errors = np.asarray(
        [max(result.energy_error, 1.0e-8) for result in rows], dtype=float
    )
    weights = 1.0 / errors**2
    normal = design.T @ (weights[:, None] * design)
    covariance = np.linalg.inv(normal)
    coefficients = covariance @ (design.T @ (weights * values))
    prediction = design @ coefficients
    return ResponseFit(
        coefficient=float(coefficients[-1]),
        coefficient_error=float(np.sqrt(covariance[-1, -1])),
        rss=float(np.sum((values - prediction) ** 2)),
    )


def exact_charged_energy(delta_v: float) -> tuple[float, float, int]:
    occupation, _ = directed_charge_start(2, axial_segments(1))
    orbit = build_small_rk_orbit(occupation)
    flippabilities = np.asarray(
        [len(small_flip_destinations(decode_small(state))) for state in orbit.states],
        dtype=float,
    )
    hamiltonian = orbit.hamiltonian + sparse.diags(delta_v * flippabilities)
    values, vectors = eigsh(
        hamiltonian,
        k=1,
        which="SA",
        v0=np.linspace(1.0, 2.0, len(orbit.states)),
        tol=1.0e-12,
    )
    vector = vectors[:, 0]
    if np.sum(vector) < 0:
        vector = -vector
    mixed = delta_v * float(np.dot(vector, flippabilities) / np.sum(vector))
    return float(values[0]), mixed, len(orbit.states)


def main() -> int:
    checks = Checks()
    detunings = (-0.05, -0.10)
    flux_stiffness_reference = {-0.05: 0.162638, -0.10: 0.321114}

    path_specs = (
        ((0, 1),),
        ((0, 2),),
        ((0, 2), (1, 1)),
        ((0, 2), (1, 2)),
        ((0, 2), (1, 2), (2, 1)),
    )
    path_ok = True
    for length in (4, 6, 8):
        for segments in path_specs:
            occupation, _ = directed_charge_start(length, segments)
            path_ok = path_ok and bool(
                sorted(
                    int(value)
                    for value in gauss_charges(occupation)[gauss_charges(occupation) != 0]
                )
                == [-1, 1]
            )
    checks.check(
        path_ok,
        "axial and off-axis directed paths leave exactly one positive and one negative unit charge",
    )

    green_symmetry_ok = True
    for length in (4, 6, 8):
        reference = coulomb_coordinate(length, (2, 1, 0))
        for vector in ((1, 2, 0), (2, 0, 1), (-2, 1, 0), (2, -1, 0)):
            green_symmetry_ok = green_symmetry_ok and abs(
                coulomb_coordinate(length, vector) - reference
            ) < 1.0e-12
    checks.check(
        green_symmetry_ok,
        "the periodic Coulomb plus harmonic coordinate is cubic- and inversion-invariant",
    )

    exact_controls: list[tuple[float, float, float, int, ChargeResult]] = []
    for detuning_index, delta_v in enumerate(detunings):
        exact, mixed, orbit_size = exact_charged_energy(delta_v)
        projector = run_charge_population(
            2,
            delta_v,
            axial_segments(1),
            population=2048,
            classical_sweeps=100,
            burn_sweeps=200,
            sample_sweeps=500,
            seed=6_000_000 + 100_000 * detuning_index,
        )
        exact_controls.append((delta_v, exact, mixed, orbit_size, projector))
    checks.check(
        all(
            orbit_size == 508 and abs(exact - mixed) < 1.0e-9
            for _, exact, mixed, orbit_size, _ in exact_controls
        ),
        "the complete 508-state charged L=2 orbit obeys the mixed-estimator identity at both detunings",
    )
    checks.check(
        all(
            abs(projector.energy - exact)
            < max(8.0 * projector.energy_error, 0.004)
            for _, exact, _, _, projector in exact_controls
        ),
        "the charged projector reproduces both exact L=2 finite-detuning ground energies",
    )

    axial: dict[tuple[float, int], list[ChargeResult]] = {}
    all_results = [row[-1] for row in exact_controls]
    for detuning_index, delta_v in enumerate(detunings):
        for length in (4, 6, 8):
            results: list[ChargeResult] = []
            for separation in range(0, length // 2 + 1):
                result = run_charge_population(
                    length,
                    delta_v,
                    None if separation == 0 else axial_segments(separation),
                    population=384,
                    classical_sweeps=120,
                    burn_sweeps=200,
                    sample_sweeps=400,
                    seed=(
                        6_500_000
                        + 100_000 * detuning_index
                        + 100 * length
                        + separation
                    ),
                )
                results.append(result)
                all_results.append(result)
            axial[(delta_v, length)] = results

    checks.check(
        all(result.count_consistent and result.charge_consistent for result in all_results),
        "every projector population preserves its exact charge pattern and local flippability count",
    )
    checks.check(
        min(result.minimum_effective_population_fraction for result in all_results) > 0.90
        and min(result.final_unique_fraction for result in all_results if result.length >= 4) > 0.25,
        "all charged populations retain effective weight and final-state diversity",
    )
    checks.check(
        all(
            result.energy - results[0].energy
            > 4.0 * np.hypot(result.energy_error, results[0].energy_error)
            for results in axial.values()
            for result in results[1:]
        ),
        "every separated charge pair has a resolved positive creation energy above its vacuum component",
    )
    checks.check(
        all(
            results[-1].energy - results[1].energy
            > 2.0 * np.hypot(results[-1].energy_error, results[1].energy_error)
            for results in axial.values()
        ),
        "opposite-charge energy rises from one-link separation to the half-box endpoint on every volume",
    )

    axial_fits: dict[float, dict[str, ResponseFit]] = {}
    for delta_v in detunings:
        by_length = {length: axial[(delta_v, length)] for length in (4, 6, 8)}
        axial_fits[delta_v] = {
            model: fit_response(by_length, model)
            for model in (
                "coulomb",
                "inverse_distance",
                "linear_distance",
                "quadratic_distance",
                "constant",
            )
        }
    checks.check(
        all(
            fits["coulomb"].coefficient
            > 5.0 * fits["coulomb"].coefficient_error
            for fits in axial_fits.values()
        ),
        "the periodic Coulomb coordinate has a resolved positive coefficient at both detunings",
    )
    checks.check(
        all(
            fits["coulomb"].rss <= 1.25 * fits["inverse_distance"].rss
            and fits["coulomb"].rss < 0.80 * fits["linear_distance"].rss
            and fits["coulomb"].rss < 0.80 * fits["quadratic_distance"].rss
            and fits["coulomb"].rss < 0.50 * fits["constant"].rss
            for fits in axial_fits.values()
        ),
        "periodic and raw 1/R Coulomb forms remain near-degenerate and beat confining or constant controls",
    )
    checks.check(
        all(
            abs(
                axial_fits[delta_v]["coulomb"].coefficient
                / flux_stiffness_reference[delta_v]
                - 1.0
            )
            < 0.25
            for delta_v in detunings
        ),
        "charge-response and topological-flux determinations of U agree within twenty-five percent",
    )
    checks.check(
        all(
            abs(
                axial_fits[delta_v]["inverse_distance"].coefficient
                / (flux_stiffness_reference[delta_v] / (4.0 * pi))
                - 1.0
            )
            < 0.30
            for delta_v in detunings
        ),
        "the raw 1/R amplitude tracks the independently fixed U/(4 pi) normalization within thirty percent",
    )

    off_axis_specs = (
        ((0, 2), (1, 1)),
        ((0, 2), (1, 2)),
        ((0, 2), (1, 2), (2, 1)),
    )
    off_axis: dict[int, list[ChargeResult]] = {}
    for length in (6, 8):
        results = list(axial[(-0.10, length)])
        for index, segments in enumerate(off_axis_specs):
            result = run_charge_population(
                length,
                -0.10,
                segments,
                population=256,
                classical_sweeps=100,
                burn_sweeps=150,
                sample_sweeps=300,
                seed=7_000_000 + 100 * length + index,
            )
            results.append(result)
            all_results.append(result)
        off_axis[length] = results
    off_axis_fits = {
        model: fit_response(off_axis, model)
        for model in (
            "coulomb",
            "inverse_distance",
            "linear_distance",
            "quadratic_distance",
            "constant",
        )
    }
    checks.check(
        off_axis_fits["coulomb"].coefficient > 0.0
        and abs(
            off_axis_fits["coulomb"].coefficient
            / flux_stiffness_reference[-0.10]
            - 1.0
        )
        < 0.30
        and off_axis_fits["coulomb"].rss
        < 0.85 * off_axis_fits["linear_distance"].rss
        and off_axis_fits["coulomb"].rss
        < 0.85 * off_axis_fits["quadratic_distance"].rss,
        "off-axis charge geometries keep a positive flux-matched Coulomb coefficient and reject string growth",
    )

    path_order = []
    for index, segments in enumerate(
        (
            ((0, 2), (1, 2)),
            ((1, 2), (0, 2)),
            ((0, 2), (1, 1)),
            ((1, 2), (0, 1)),
        )
    ):
        path_order.append(
            run_charge_population(
                6,
                -0.10,
                segments,
                population=256,
                classical_sweeps=100,
                burn_sweeps=150,
                sample_sweeps=300,
                seed=7_500_000 + index,
            )
        )
    same_endpoint_ok = abs(path_order[0].energy - path_order[1].energy) < 4.0 * np.hypot(
        path_order[0].energy_error, path_order[1].energy_error
    )
    rotated_ok = abs(path_order[2].energy - path_order[3].energy) < 4.0 * np.hypot(
        path_order[2].energy_error, path_order[3].energy_error
    )
    checks.check(
        same_endpoint_ok and rotated_ok,
        "path-order and cubic-rotation controls reproduce equal charge energies within four errors",
    )

    population_control = []
    for separation in (1, 4):
        population_control.append(
            run_charge_population(
                8,
                -0.10,
                axial_segments(separation),
                population=768,
                classical_sweeps=150,
                burn_sweeps=250,
                sample_sweeps=500,
                seed=8_000_000 + separation,
            )
        )
    primary_rise = axial[(-0.10, 8)][-1].energy - axial[(-0.10, 8)][1].energy
    control_rise = population_control[-1].energy - population_control[0].energy
    checks.check(
        primary_rise > 0.0
        and control_rise > 0.0
        and abs(primary_rise - control_rise)
        / (0.5 * (primary_rise + control_rise))
        < 0.30,
        "doubled L=8 populations reproduce the positive long-distance charge-energy rise",
    )

    for delta_v, exact, _, orbit_size, projector in exact_controls:
        print(
            "EXACT_CHARGE",
            f"V={1.0 + delta_v:.2f}",
            f"orbit={orbit_size}",
            f"E0={exact:.9f}",
            f"projector={projector.energy:.9f}+/-{projector.energy_error:.9f}",
        )
    for delta_v in detunings:
        fits = axial_fits[delta_v]
        print(
            "AXIAL_FIT",
            f"V={1.0 + delta_v:.2f}",
            f"U_charge={fits['coulomb'].coefficient:.6f}+/-{fits['coulomb'].coefficient_error:.6f}",
            f"U_flux={flux_stiffness_reference[delta_v]:.6f}",
            f"A_1overR={fits['inverse_distance'].coefficient:.6f}",
            f"U_flux/(4pi)={flux_stiffness_reference[delta_v] / (4.0 * pi):.6f}",
            "rss="
            + ",".join(
                f"{model}:{fits[model].rss:.8f}"
                for model in (
                    "coulomb",
                    "inverse_distance",
                    "linear_distance",
                    "quadratic_distance",
                    "constant",
                )
            ),
        )
    print(
        "OFF_AXIS_FIT",
        f"U_charge={off_axis_fits['coulomb'].coefficient:.6f}+/-{off_axis_fits['coulomb'].coefficient_error:.6f}",
        f"U_flux={flux_stiffness_reference[-0.10]:.6f}",
        f"rss_coulomb={off_axis_fits['coulomb'].rss:.8f}",
        f"rss_linear={off_axis_fits['linear_distance'].rss:.8f}",
    )
    print(
        "POPULATION_CONTROL",
        f"primary_rise={primary_rise:.9f}",
        f"doubled_rise={control_rise:.9f}",
    )
    print(
        "CERTIFICATE: fixed_opposite_unit_charges=True finite_population=True "
        "finite_imaginary_time=True component_complete=False thermodynamic_limit=False "
        "real_time_spectrum=False"
    )
    print(
        "RESOLUTION: per_element=directed path and square flips; per_site=two fixed charges and exact Gauss; "
        "per_mode=periodic Coulomb kernel plus harmonic sector; per_block=L2 exact and L4,6,8 projector; "
        "lattice_wide=finite-volume static response, not an infinite-volume potential theorem"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
