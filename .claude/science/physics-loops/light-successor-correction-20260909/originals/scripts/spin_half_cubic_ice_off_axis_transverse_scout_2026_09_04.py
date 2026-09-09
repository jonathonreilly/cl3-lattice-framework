#!/usr/bin/env python3
"""Scout off-axis transverse dynamics in finite-detuning cubic ice.

The established spectral runner measures axial momenta.  This bounded scout
uses the same positive projector and forward-walking estimator, but replaces
the axial coefficient table by lattice-divergence-transverse polarizations at
the axial, face-diagonal, and body-diagonal first harmonics.  It records
health and raw polarization/direction diagnostics without a physics-result
acceptance threshold.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import (
    build_geometry,
    count_flippable,
)
from spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03 import (
    ReplicaResult,
    effective_gap,
    measure_correlation_block,
    prepare_population,
    propagate_sweep,
)
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
    CubicIceSampler,
    electric_flux,
    initial_ice,
    vertex_degrees,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py",
)

AUDIT_TIMEOUT_SEC = 3600
PATTERNS = ((1, 0, 0), (1, 1, 0), (1, 1, 1))


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
class ModeEstimate:
    length: int
    delta_v: float
    pattern: tuple[int, int, int]
    polarization: int
    q_squared: float
    gap: float
    gap_error: float


def real_transverse_basis(q_vector: np.ndarray) -> np.ndarray:
    """Return a deterministic real orthonormal basis perpendicular to q."""

    q_hat = q_vector / np.linalg.norm(q_vector)
    reference_axis = int(np.argmin(np.abs(q_hat)))
    reference = np.eye(3)[reference_axis]
    first = reference - np.dot(reference, q_hat) * q_hat
    first /= np.linalg.norm(first)
    second = np.cross(q_hat, first)
    second /= np.linalg.norm(second)
    return np.asarray((first, second))


def off_axis_coefficients(
    length: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    list[tuple[tuple[int, int, int], int]],
    np.ndarray,
]:
    """Build link-centred transverse rows and longitudinal null controls."""

    coordinates = np.indices((length, length, length))
    coordinate_rows = np.moveaxis(coordinates, 0, -1).reshape((-1, 3))
    normalization = np.sqrt(length**3)
    modes: list[tuple[tuple[int, int, int], int]] = []
    transverse_rows: list[np.ndarray] = []
    longitudinal_rows: list[np.ndarray] = []
    for pattern in PATTERNS:
        momentum = 2.0 * np.pi * np.asarray(pattern, dtype=float) / length
        q_vector = 2.0 * np.sin(0.5 * momentum)
        q_hat = q_vector / np.linalg.norm(q_vector)
        link_centre_phase = np.exp(0.5j * momentum)
        site_phase = np.exp(1j * (coordinate_rows @ momentum))
        longitudinal = np.empty(3 * length**3, dtype=np.complex128)
        for axis in range(3):
            longitudinal[axis :: 3] = (
                q_hat[axis]
                * link_centre_phase[axis]
                * site_phase
                / normalization
            )
        longitudinal_rows.append(longitudinal)
        for polarization, vector in enumerate(real_transverse_basis(q_vector)):
            row = np.empty(3 * length**3, dtype=np.complex128)
            for axis in range(3):
                row[axis :: 3] = (
                    vector[axis]
                    * link_centre_phase[axis]
                    * site_phase
                    / normalization
                )
            transverse_rows.append(row)
            modes.append((pattern, polarization))
    transverse = np.asarray(transverse_rows)
    return (
        transverse.real.copy(),
        transverse.imag.copy(),
        modes,
        np.asarray(longitudinal_rows),
    )


def run_off_axis_replica(
    length: int,
    delta_v: float,
    *,
    population: int,
    seed: int,
) -> tuple[ReplicaResult, list[tuple[tuple[int, int, int], int]]]:
    geometry = build_geometry(length)
    start = initial_ice(length).ravel()
    interval = max(8, geometry.plaquette_count // 8)
    while geometry.plaquette_count % interval:
        interval -= 1
    states, counts, mean_count, minimum_effective = prepare_population(
        start,
        delta_v,
        population,
        80,
        160 if delta_v else 120,
        geometry.plaquette_links,
        geometry.affected_plaquettes,
        geometry.affected_counts,
        interval,
        seed,
    )
    coefficient_real, coefficient_imag, modes, _ = off_axis_coefficients(length)
    blocks = []
    block_origin_survival = []
    block_origin_diversity = []
    block_forward_survival = []
    minimum_dynamic_effective = float(population)
    for origin_index in range(3):
        (
            states,
            counts,
            correlation,
            effective,
            origin_survival,
            origin_diversity,
            survival,
        ) = measure_correlation_block(
            states,
            counts,
            delta_v,
            10,
            4,
            coefficient_real,
            coefficient_imag,
            geometry.plaquette_links,
            geometry.affected_plaquettes,
            geometry.affected_counts,
            interval,
        )
        blocks.append(correlation)
        block_origin_survival.append(origin_survival)
        block_origin_diversity.append(origin_diversity)
        block_forward_survival.append(survival)
        minimum_dynamic_effective = min(minimum_dynamic_effective, effective)
        if origin_index < 2:
            ancestors = np.arange(population, dtype=np.int32)
            labels = np.full((1, population), -1, dtype=np.int32)
            for _ in range(2):
                states, counts, ancestors, labels, effective = propagate_sweep(
                    states,
                    counts,
                    ancestors,
                    labels,
                    delta_v,
                    geometry.plaquette_links,
                    geometry.affected_plaquettes,
                    geometry.affected_counts,
                    interval,
                )
                minimum_dynamic_effective = min(
                    minimum_dynamic_effective, effective
                )
    reshaped = states.reshape((population, length, length, length, 3))
    normalized_blocks = np.asarray(blocks)
    return (
        ReplicaResult(
            correlations=np.mean(normalized_blocks, axis=0),
            correlation_blocks=normalized_blocks,
            population=population,
            energy=delta_v * mean_count,
            minimum_effective_population_fraction=min(
                minimum_effective, minimum_dynamic_effective
            )
            / population,
            origin_survival_fraction=min(block_origin_survival),
            origin_diversity_fractions=np.min(
                np.asarray(block_origin_diversity), axis=0
            ),
            forward_survival_fractions=np.min(
                np.asarray(block_forward_survival), axis=0
            ),
            count_consistent=all(
                count_flippable(state, geometry.plaquette_links) == count
                for state, count in zip(states, counts, strict=True)
            ),
            sector_consistent=all(
                np.all(vertex_degrees(state) == 3)
                and electric_flux(state) == (0, 0, 0)
                for state in reshaped
            ),
        ),
        modes,
    )


def summarize_modes(
    length: int,
    delta_v: float,
    replicas: list[
        tuple[ReplicaResult, list[tuple[tuple[int, int, int], int]]]
    ],
) -> list[ModeEstimate]:
    modes = replicas[0][1]
    if any(replica_modes != modes for _, replica_modes in replicas):
        raise AssertionError("off-axis mode ordering changed")
    energies = np.asarray([result.energy for result, _ in replicas])
    rows = []
    for mode_index, (pattern, polarization) in enumerate(modes):
        curves = np.asarray(
            [result.correlations[:, mode_index] for result, _ in replicas]
        )
        central = effective_gap(
            np.mean(curves, axis=0).real,
            length,
            float(np.mean(energies)),
            2,
            6,
        )
        leave_one_out = []
        for omitted in range(len(curves)):
            mask = np.arange(len(curves)) != omitted
            leave_one_out.append(
                effective_gap(
                    np.mean(curves[mask], axis=0).real,
                    length,
                    float(np.mean(energies[mask])),
                    2,
                    6,
                )
            )
        jackknife = np.asarray(leave_one_out)
        gap_error = float(
            np.sqrt(
                (len(jackknife) - 1.0)
                / len(jackknife)
                * np.sum((jackknife - np.mean(jackknife)) ** 2)
            )
        )
        momentum = 2.0 * np.pi * np.asarray(pattern, dtype=float) / length
        q_squared = float(np.sum((2.0 * np.sin(0.5 * momentum)) ** 2))
        rows.append(
            ModeEstimate(
                length,
                delta_v,
                pattern,
                polarization,
                q_squared,
                float(central),
                gap_error,
            )
        )
    return rows


def longitudinal_null_control() -> float:
    maximum = 0.0
    for length in (6, 8):
        sampler = CubicIceSampler(length, 27_000_000 + length)
        _, _, _, longitudinal_rows = off_axis_coefficients(length)
        coordinates = np.indices((length, length, length))
        staggering = (-1.0) ** np.sum(coordinates, axis=0)
        for _ in range(12):
            sampler.sweep()
            electric = (
                staggering[..., None]
                * (sampler.occupation.astype(float) - 0.5)
            ).ravel()
            maximum = max(
                maximum,
                float(np.max(np.abs(longitudinal_rows @ electric))),
            )
    return maximum


def main() -> int:
    checks = Checks()
    longitudinal_residual = longitudinal_null_control()
    checks.check(
        longitudinal_residual < 1.0e-12,
        "link-centred longitudinal modes vanish on every sampled ice state",
    )

    replicas: dict[
        tuple[float, int],
        list[tuple[ReplicaResult, list[tuple[tuple[int, int, int], int]]]],
    ] = {}
    for delta_index, delta_v in enumerate((-0.05, 0.0)):
        population = 512 if delta_v else 384
        for length in (8, 10):
            replicas[(delta_v, length)] = [
                run_off_axis_replica(
                    length,
                    delta_v,
                    population=population,
                    seed=(
                        27_100_000
                        + 100_000 * delta_index
                        + 1_000 * length
                        + replica
                    ),
                )
                for replica in range(2)
            ]
    all_replicas = [
        result
        for family in replicas.values()
        for result, _ in family
    ]
    checks.check(
        all(
            result.count_consistent and result.sector_consistent
            for result in all_replicas
        ),
        "every off-axis population preserves exact counts, Gauss charge, and zero electric flux",
    )
    checks.check(
        min(
            result.minimum_effective_population_fraction
            for result in all_replicas
        )
        > 0.85
        and min(
            result.population * result.origin_diversity_fractions[6]
            for result in all_replicas
        )
        >= 10
        and min(
            result.population * np.min(result.forward_survival_fractions)
            for result in all_replicas
        )
        >= 10,
        "scout populations retain effective weight and fitted-time genealogy",
    )
    checks.check(
        all(
            np.all(result.correlations[:7].real > 0.0)
            and np.max(np.abs(result.correlations[:7].imag)) < 0.10
            for result in all_replicas
        ),
        "every off-axis mode stays positive with bounded imaginary residual through the fitted window",
    )

    summaries = {
        key: summarize_modes(*key[::-1], family)
        for key, family in replicas.items()
    }
    for delta_v in (-0.05, 0.0):
        for length in (8, 10):
            for row in summaries[(delta_v, length)]:
                print(
                    "OFF_AXIS_SCOUT",
                    f"V={1.0 + delta_v:.2f}",
                    f"L={length}",
                    "pattern=" + "".join(str(value) for value in row.pattern),
                    f"pol={row.polarization}",
                    f"Q2={row.q_squared:.8f}",
                    f"gap={row.gap:.8f}+/-{row.gap_error:.8f}",
                )
    for length in (8, 10):
        for pattern in PATTERNS:
            detuned = [
                row
                for row in summaries[(-0.05, length)]
                if row.pattern == pattern
            ]
            rk = [
                row
                for row in summaries[(0.0, length)]
                if row.pattern == pattern
            ]
            velocities = [
                (detuned[index].gap**2 - rk[index].gap**2)
                / detuned[index].q_squared
                for index in range(2)
            ]
            split = abs(detuned[0].gap - detuned[1].gap) / np.mean(
                [detuned[0].gap, detuned[1].gap]
            )
            print(
                "DIRECTION_SCOUT",
                f"L={length}",
                "pattern=" + "".join(str(value) for value in pattern),
                f"polarization_split={split:.6f}",
                f"excess_c2_pol0={velocities[0]:.8f}",
                f"excess_c2_pol1={velocities[1]:.8f}",
            )
    print(
        "SCOUT_SCOPE: result_threshold=False axial_face_body=True "
        "finite_population=True thermodynamic_limit=False"
    )
    print(f"LONGITUDINAL_NULL max={longitudinal_residual:.3e}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
