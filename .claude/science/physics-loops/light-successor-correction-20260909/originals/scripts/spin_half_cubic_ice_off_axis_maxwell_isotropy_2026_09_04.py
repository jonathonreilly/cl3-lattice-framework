#!/usr/bin/env python3
"""Covariance-bearing off-axis spectral ladder in cubic ice.

The runner promotes the corrected cubic-orbit scout to four volumes and eight
independent outer populations per coupling and volume. It keeps the axial,
face-out, face-in, and body-diagonal families separate and emits their complete
within-population covariance. A separate cheap join runner owns all dispersion
models so this expensive stochastic receipt remains reusable.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import permutations, product

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

AUDIT_TIMEOUT_SEC = 10800
LENGTHS = (8, 10, 12, 14)
FAMILIES = ("axis", "face_out", "face_in", "body")


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
class FamilyRow:
    length: int
    delta_v: float
    gaps: np.ndarray
    covariance: np.ndarray
    q_squared: np.ndarray
    imaginary_residuals: np.ndarray


def signed_permutation_orbit(
    base: tuple[int, int, int],
) -> tuple[tuple[int, int, int], ...]:
    rows = set()
    for permutation in set(permutations(base)):
        nonzero = [index for index, value in enumerate(permutation) if value]
        for signs in product((-1, 1), repeat=len(nonzero)):
            row = list(permutation)
            for index, sign in zip(nonzero, signs, strict=True):
                row[index] *= sign
            rows.add(tuple(row))
    return tuple(sorted(rows))


def real_transverse_basis(q_vector: np.ndarray) -> np.ndarray:
    q_hat = q_vector / np.linalg.norm(q_vector)
    reference_axis = int(np.argmin(np.abs(q_hat)))
    reference = np.eye(3)[reference_axis]
    first = reference - np.dot(reference, q_hat) * q_hat
    first /= np.linalg.norm(first)
    second = np.cross(q_hat, first)
    second /= np.linalg.norm(second)
    return np.asarray((first, second))


def append_coefficient(
    rows: list[np.ndarray],
    length: int,
    coordinate_rows: np.ndarray,
    site_staggering: np.ndarray,
    momentum: np.ndarray,
    polarization: np.ndarray,
) -> None:
    normalization = np.sqrt(length**3)
    link_centre_phase = np.exp(0.5j * momentum)
    site_phase = (
        site_staggering
        * np.exp(1j * (coordinate_rows @ momentum))
        / normalization
    )
    row = np.empty(3 * length**3, dtype=np.complex128)
    for axis in range(3):
        row[axis :: 3] = (
            polarization[axis] * link_centre_phase[axis] * site_phase
        )
    rows.append(row)


def cubic_orbit_coefficients(
    length: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    list[tuple[str, tuple[int, int, int], int]],
    np.ndarray,
]:
    coordinates = np.indices((length, length, length))
    coordinate_rows = np.moveaxis(coordinates, 0, -1).reshape((-1, 3))
    site_staggering = (-1.0) ** np.sum(coordinates, axis=0).ravel()
    rows: list[np.ndarray] = []
    longitudinal_rows: list[np.ndarray] = []
    modes: list[tuple[str, tuple[int, int, int], int]] = []
    for kind, base in (
        ("axis", (1, 0, 0)),
        ("face", (1, 1, 0)),
        ("body", (1, 1, 1)),
    ):
        for pattern in signed_permutation_orbit(base):
            momentum = 2.0 * np.pi * np.asarray(pattern, dtype=float) / length
            q_vector = 2.0 * np.sin(0.5 * momentum)
            q_hat = q_vector / np.linalg.norm(q_vector)
            append_coefficient(
                longitudinal_rows,
                length,
                coordinate_rows,
                site_staggering,
                momentum,
                q_hat,
            )
            if kind == "face":
                zero_axis = int(np.flatnonzero(np.asarray(pattern) == 0)[0])
                out_of_plane = np.eye(3)[zero_axis]
                in_plane = np.cross(q_hat, out_of_plane)
                in_plane /= np.linalg.norm(in_plane)
                polarizations = (
                    ("face_out", out_of_plane),
                    ("face_in", in_plane),
                )
            else:
                family = "axis" if kind == "axis" else "body"
                polarizations = tuple(
                    (family, vector)
                    for vector in real_transverse_basis(q_vector)
                )
            for polarization_index, (family, vector) in enumerate(
                polarizations
            ):
                append_coefficient(
                    rows,
                    length,
                    coordinate_rows,
                    site_staggering,
                    momentum,
                    vector,
                )
                modes.append((family, pattern, polarization_index))
    matrix = np.asarray(rows)
    return (
        matrix.real.copy(),
        matrix.imag.copy(),
        modes,
        np.asarray(longitudinal_rows),
    )


def longitudinal_null_control() -> float:
    maximum = 0.0
    for length in (6, 8):
        sampler = CubicIceSampler(length, 31_000_000 + length)
        _, _, _, longitudinal = cubic_orbit_coefficients(length)
        for _ in range(12):
            sampler.sweep()
            centered = (sampler.occupation.astype(float) - 0.5).ravel()
            maximum = max(
                maximum,
                float(np.max(np.abs(longitudinal @ centered))),
            )
    return maximum


def run_replica(
    length: int,
    delta_v: float,
    *,
    population: int,
    seed: int,
) -> tuple[ReplicaResult, list[tuple[str, tuple[int, int, int], int]]]:
    geometry = build_geometry(length)
    interval = max(8, geometry.plaquette_count // 8)
    while geometry.plaquette_count % interval:
        interval -= 1
    states, counts, mean_count, minimum_effective = prepare_population(
        initial_ice(length).ravel(),
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
    coefficient_real, coefficient_imag, modes, _ = cubic_orbit_coefficients(
        length
    )
    blocks = []
    origin_survival_rows = []
    origin_diversity_rows = []
    forward_survival_rows = []
    minimum_dynamic_effective = float(population)
    for origin_index in range(3):
        (
            states,
            counts,
            correlation,
            effective,
            origin_survival,
            origin_diversity,
            forward_survival,
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
        origin_survival_rows.append(origin_survival)
        origin_diversity_rows.append(origin_diversity)
        forward_survival_rows.append(forward_survival)
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
            origin_survival_fraction=min(origin_survival_rows),
            origin_diversity_fractions=np.min(
                np.asarray(origin_diversity_rows), axis=0
            ),
            forward_survival_fractions=np.min(
                np.asarray(forward_survival_rows), axis=0
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


def family_curves(
    result: ReplicaResult,
    modes: list[tuple[str, tuple[int, int, int], int]],
) -> np.ndarray:
    return np.asarray(
        [
            np.mean(
                result.correlations[
                    :,
                    [
                        index
                        for index, mode in enumerate(modes)
                        if mode[0] == family
                    ],
                ],
                axis=1,
            )
            for family in FAMILIES
        ]
    )


def gap_vector(
    curves: np.ndarray,
    energies: np.ndarray,
    length: int,
) -> np.ndarray:
    return np.asarray(
        [
            effective_gap(
                np.mean(curves[:, family_index], axis=0).real,
                length,
                float(np.mean(energies)),
                2,
                6,
            )
            for family_index in range(len(FAMILIES))
        ]
    )


def summarize_row(
    length: int,
    delta_v: float,
    replicas: list[
        tuple[ReplicaResult, list[tuple[str, tuple[int, int, int], int]]]
    ],
) -> FamilyRow:
    modes = replicas[0][1]
    if any(replica_modes != modes for _, replica_modes in replicas):
        raise AssertionError("off-axis production mode ordering changed")
    curves = np.asarray(
        [family_curves(result, modes) for result, _ in replicas]
    )
    energies = np.asarray([result.energy for result, _ in replicas])
    central = gap_vector(curves, energies, length)
    leave_one_out = []
    for omitted in range(len(curves)):
        mask = np.arange(len(curves)) != omitted
        leave_one_out.append(gap_vector(curves[mask], energies[mask], length))
    jackknife = np.asarray(leave_one_out)
    deviations = jackknife - np.mean(jackknife, axis=0)
    covariance = (
        (len(jackknife) - 1.0)
        / len(jackknife)
        * deviations.T
        @ deviations
    )
    base_q_squared = (2.0 * np.sin(np.pi / length)) ** 2
    return FamilyRow(
        length=length,
        delta_v=delta_v,
        gaps=central,
        covariance=covariance,
        q_squared=base_q_squared * np.asarray((1.0, 2.0, 2.0, 3.0)),
        imaginary_residuals=np.max(
            np.abs(np.mean(curves, axis=0).imag), axis=1
        ),
    )


def main() -> int:
    checks = Checks()
    checks.check(
        longitudinal_null_control() < 1.0e-12,
        "the production coefficient table retains an exact longitudinal ice null",
    )
    replicas = {}
    for delta_index, delta_v in enumerate((-0.05, 0.0)):
        for length in LENGTHS:
            population = (
                1536 if delta_v and length == 14
                else 1024 if delta_v
                else 768 if length == 14
                else 512
            )
            replicas[(delta_v, length)] = [
                run_replica(
                    length,
                    delta_v,
                    population=population,
                    seed=(
                        30_000_000
                        + 100_000 * delta_index
                        + 1_000 * length
                        + replica
                    ),
                )
                for replica in range(8)
            ]
    all_replicas = [
        result for family in replicas.values() for result, _ in family
    ]
    checks.check(
        all(
            result.count_consistent and result.sector_consistent
            for result in all_replicas
        ),
        "every production population preserves exact counts, Gauss charge, and zero electric flux",
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
        >= 40
        and min(
            result.population * np.min(result.forward_survival_fractions)
            for result in all_replicas
        )
        >= 40,
        "production populations retain the declared weight and genealogy floors",
    )
    rows = {
        key: summarize_row(key[1], key[0], family)
        for key, family in replicas.items()
    }
    checks.check(
        all(
            np.all(np.isfinite(row.gaps))
            and np.all(row.gaps > 0.0)
            and np.all(np.isfinite(row.covariance))
            and np.all(np.diag(row.covariance) > 0.0)
            and np.max(row.imaginary_residuals) < 0.03
            for row in rows.values()
        ),
        "every family gap and jackknife covariance is finite with bounded phase residual",
    )
    checks.check(
        all(
            np.linalg.matrix_rank(row.covariance, tol=1.0e-12)
            == len(FAMILIES)
            for row in rows.values()
        ),
        "every within-population four-family covariance has full rank",
    )

    for delta_v in (-0.05, 0.0):
        for length in LENGTHS:
            row = rows[(delta_v, length)]
            print(
                "OFF_AXIS_GAPS",
                f"V={1.0 + delta_v:.2f}",
                f"L={length}",
                "values="
                + ",".join(
                    f"{family}:{row.q_squared[family_index]:.8f}:"
                    f"{row.gaps[family_index]:.8f}"
                    for family_index, family in enumerate(FAMILIES)
                ),
            )
            print(
                "OFF_AXIS_COVARIANCE",
                f"V={1.0 + delta_v:.2f}",
                f"L={length}",
                "row_major="
                + ",".join(f"{value:.12e}" for value in row.covariance.ravel()),
            )
    print(
        "HEALTH",
        f"min_ess={min(result.minimum_effective_population_fraction for result in all_replicas):.6f}",
        f"min_origin_tau6={min(result.population * result.origin_diversity_fractions[6] for result in all_replicas):.0f}",
        f"min_forward={min(result.population * np.min(result.forward_survival_fractions) for result in all_replicas):.0f}",
    )
    print(
        "CERTIFICATE: complete_cubic_orbits=True outer_population_covariance=True "
        "models_deferred_to_join=True finite_volume=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
