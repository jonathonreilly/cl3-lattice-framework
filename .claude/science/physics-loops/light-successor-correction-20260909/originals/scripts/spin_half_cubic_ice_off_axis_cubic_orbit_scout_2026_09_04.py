#!/usr/bin/env python3
"""Scout cubic-orbit-averaged off-axis dynamics in spin-half cubic ice.

The preceding individual-mode scout preserved the physical sectors but lost
the signal in mode-level phase noise.  This runner predeclares complete cubic
momentum orbits, includes both signs of every momentum, and averages each
symmetry family before extracting a decay.  Face-diagonal in-plane and
out-of-plane polarizations remain separate because cubic symmetry does not
force them to agree at finite momentum.
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
from spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04 import (
    real_transverse_basis,
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
    "scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 3600
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
class FamilyEstimate:
    length: int
    delta_v: float
    family: str
    q_squared: float
    gap: float
    gap_error: float
    imaginary_residual: float


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


def append_coefficient(
    rows: list[np.ndarray],
    length: int,
    coordinate_rows: np.ndarray,
    momentum: np.ndarray,
    polarization: np.ndarray,
) -> None:
    normalization = np.sqrt(length**3)
    link_centre_phase = np.exp(0.5j * momentum)
    site_phase = np.exp(1j * (coordinate_rows @ momentum))
    row = np.empty(3 * length**3, dtype=np.complex128)
    for axis in range(3):
        row[axis :: 3] = (
            polarization[axis]
            * link_centre_phase[axis]
            * site_phase
            / normalization
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


def jackknife_gap(
    curves: np.ndarray,
    energies: np.ndarray,
    length: int,
) -> tuple[float, float]:
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
    values = np.asarray(leave_one_out)
    error = np.sqrt(
        (len(values) - 1.0)
        / len(values)
        * np.sum((values - np.mean(values)) ** 2)
    )
    return float(central), float(error)


def summarize_families(
    length: int,
    delta_v: float,
    replicas: list[
        tuple[ReplicaResult, list[tuple[str, tuple[int, int, int], int]]]
    ],
) -> list[FamilyEstimate]:
    modes = replicas[0][1]
    if any(replica_modes != modes for _, replica_modes in replicas):
        raise AssertionError("cubic-orbit mode ordering changed")
    energies = np.asarray([result.energy for result, _ in replicas])
    rows = []
    for family in FAMILIES:
        indices = [
            index for index, mode in enumerate(modes) if mode[0] == family
        ]
        curves = np.asarray(
            [
                np.mean(result.correlations[:, indices], axis=1)
                for result, _ in replicas
            ]
        )
        gap, gap_error = jackknife_gap(curves, energies, length)
        base = {
            "axis": (1, 0, 0),
            "face_out": (1, 1, 0),
            "face_in": (1, 1, 0),
            "body": (1, 1, 1),
        }[family]
        momentum = 2.0 * np.pi * np.asarray(base, dtype=float) / length
        rows.append(
            FamilyEstimate(
                length,
                delta_v,
                family,
                float(np.sum((2.0 * np.sin(0.5 * momentum)) ** 2)),
                gap,
                gap_error,
                float(np.max(np.abs(np.mean(curves, axis=0).imag))),
            )
        )
    return rows


def longitudinal_null_control() -> float:
    maximum = 0.0
    for length in (6, 8):
        sampler = CubicIceSampler(length, 28_000_000 + length)
        _, _, _, longitudinal = cubic_orbit_coefficients(length)
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
                float(np.max(np.abs(longitudinal @ electric))),
            )
    return maximum


def main() -> int:
    checks = Checks()
    longitudinal_residual = longitudinal_null_control()
    checks.check(
        longitudinal_residual < 1.0e-12,
        "every cubic-orbit longitudinal coefficient is an exact ice null",
    )
    replicas = {}
    for delta_index, delta_v in enumerate((-0.05, 0.0)):
        population = 512 if delta_v else 384
        for length in (8, 10):
            replicas[(delta_v, length)] = [
                run_replica(
                    length,
                    delta_v,
                    population=population,
                    seed=(
                        28_100_000
                        + 100_000 * delta_index
                        + 1_000 * length
                        + replica
                    ),
                )
                for replica in range(2)
            ]
    all_replicas = [
        result for family in replicas.values() for result, _ in family
    ]
    checks.check(
        all(
            result.count_consistent and result.sector_consistent
            for result in all_replicas
        ),
        "every cubic-orbit population preserves exact local counts and sectors",
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
        "cubic-orbit scout populations retain effective weight and genealogy",
    )
    summaries = {
        key: summarize_families(key[1], key[0], family)
        for key, family in replicas.items()
    }
    checks.check(
        all(
            np.isfinite(row.gap)
            and np.isfinite(row.gap_error)
            and row.gap > 0.0
            and row.imaginary_residual < 0.03
            for family in summaries.values()
            for row in family
        ),
        "every symmetry-averaged family has a finite positive gap and bounded phase residual",
    )
    for delta_v in (-0.05, 0.0):
        for length in (8, 10):
            for row in summaries[(delta_v, length)]:
                print(
                    "ORBIT_SCOUT",
                    f"V={1.0 + delta_v:.2f}",
                    f"L={length}",
                    f"family={row.family}",
                    f"Q2={row.q_squared:.8f}",
                    f"gap={row.gap:.8f}+/-{row.gap_error:.8f}",
                    f"imag={row.imaginary_residual:.3e}",
                )
    for length in (8, 10):
        detuned = {row.family: row for row in summaries[(-0.05, length)]}
        rk = {row.family: row for row in summaries[(0.0, length)]}
        values = {}
        for family in FAMILIES:
            values[family] = (
                detuned[family].gap**2 - rk[family].gap**2
            ) / detuned[family].q_squared
        face_split = abs(
            detuned["face_out"].gap - detuned["face_in"].gap
        ) / np.mean(
            [detuned["face_out"].gap, detuned["face_in"].gap]
        )
        print(
            "ORBIT_DIRECTION_SCOUT",
            f"L={length}",
            f"face_polarization_split={face_split:.6f}",
            " ".join(
                f"{family}_excess_c2={values[family]:.8f}"
                for family in FAMILIES
            ),
        )
    print(
        "SCOUT_SCOPE: complete_cubic_orbits=True face_polarizations_separate=True "
        "result_threshold=False thermodynamic_limit=False"
    )
    print(f"LONGITUDINAL_NULL max={longitudinal_residual:.3e}")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
