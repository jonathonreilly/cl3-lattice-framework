#!/usr/bin/env python3
"""Paired multi-forward-length ladder for the cubic-ice spectrum.

One trajectory propagated through F=12 contains every shorter descendant
projection. This runner measures F=2,4,6,8,10,12 together on each independent
L=8 population, then emits the outer-population covariance across forward
lengths. A separate cheap join owns the plateau decision.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03 import (
    build_geometry,
    count_flippable,
)
from spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03 import (
    effective_gap,
    evaluate_observables,
    prepare_population,
    propagate_sweep,
    transverse_coefficients,
)
from spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03 import (
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
FORWARD_LENGTHS = (2, 4, 6, 8, 10, 12)
WINDOWS = ((2, 6), (6, 12), (8, 14), (10, 16))
TARGET_WINDOWS = ((2, 6), (8, 14))


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
class MultiForwardReplica:
    correlations: np.ndarray
    population: int
    energy: float
    minimum_effective_fraction: float
    origin_diversity_fractions: np.ndarray
    forward_survival_fractions: np.ndarray
    count_consistent: bool
    sector_consistent: bool


@dataclass(frozen=True)
class ForwardSummary:
    delta_v: float
    gaps: dict[tuple[int, int], np.ndarray]
    covariances: dict[tuple[int, int], np.ndarray]
    mean_curves: np.ndarray
    imaginary_residual: float
    minimum_effective_fraction: float
    minimum_origin_tau16_count: float
    minimum_forward_count: float
    count_consistent: bool
    sector_consistent: bool


def measure_multi_forward_block(
    states: np.ndarray,
    counts: np.ndarray,
    delta_v: float,
    coefficient_real: np.ndarray,
    coefficient_imag: np.ndarray,
    plaquette_links: np.ndarray,
    affected_plaquettes: np.ndarray,
    affected_counts: np.ndarray,
    interval: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    float,
    np.ndarray,
    np.ndarray,
]:
    population = states.shape[0]
    tau_max = 16
    tau_count = tau_max + 1
    mode_count = coefficient_real.shape[0]
    origin_observables = evaluate_observables(
        states, coefficient_real, coefficient_imag
    )
    ancestors = np.arange(population, dtype=np.int32)
    labels = np.full((tau_count, population), -1, dtype=np.int32)
    tau_origins = np.full((tau_count, population), -1, dtype=np.int32)
    tau_observables = np.zeros(
        (tau_count, population, mode_count), dtype=np.complex128
    )
    labels[0] = np.arange(population, dtype=np.int32)
    tau_origins[0] = ancestors
    tau_observables[0] = origin_observables
    correlations = np.zeros(
        (len(FORWARD_LENGTHS), tau_count, mode_count),
        dtype=np.complex128,
    )
    survival = np.zeros((len(FORWARD_LENGTHS), tau_count), dtype=float)
    origin_diversity = np.zeros(tau_count, dtype=float)
    origin_diversity[0] = 1.0
    minimum_effective = float(population)
    final_sweep = tau_max + max(FORWARD_LENGTHS)
    for sweep in range(final_sweep + 1):
        if 0 < sweep <= tau_max:
            labels[sweep] = np.arange(population, dtype=np.int32)
            tau_origins[sweep] = ancestors
            tau_observables[sweep] = evaluate_observables(
                states, coefficient_real, coefficient_imag
            )
            origin_diversity[sweep] = len(np.unique(ancestors)) / population
        for forward_index, forward_sweeps in enumerate(FORWARD_LENGTHS):
            if sweep < forward_sweeps:
                continue
            tau = sweep - forward_sweeps
            if tau > tau_max:
                continue
            final_labels = labels[tau]
            survival[forward_index, tau] = (
                len(np.unique(final_labels)) / population
            )
            products = np.empty(
                (population, mode_count), dtype=np.complex128
            )
            for walker, label in enumerate(final_labels):
                origin = tau_origins[tau, label]
                products[walker] = origin_observables[origin] * np.conjugate(
                    tau_observables[tau, label]
                )
            correlations[forward_index, tau] = np.mean(products, axis=0)
        if sweep == final_sweep:
            break
        states, counts, ancestors, labels, effective = propagate_sweep(
            states,
            counts,
            ancestors,
            labels,
            delta_v,
            plaquette_links,
            affected_plaquettes,
            affected_counts,
            interval,
        )
        minimum_effective = min(minimum_effective, effective)
    for forward_index in range(len(FORWARD_LENGTHS)):
        correlations[forward_index] /= correlations[
            forward_index, 0
        ].real[None, :]
    return (
        states,
        counts,
        correlations,
        minimum_effective,
        origin_diversity,
        survival,
    )


def run_replica(
    delta_v: float,
    population: int,
    seed: int,
) -> MultiForwardReplica:
    length = 8
    geometry = build_geometry(length)
    interval = max(8, geometry.plaquette_count // 8)
    while geometry.plaquette_count % interval:
        interval -= 1
    states, counts, mean_count, minimum_effective = prepare_population(
        initial_ice(length).ravel(),
        delta_v,
        population,
        100,
        200 if delta_v else 120,
        geometry.plaquette_links,
        geometry.affected_plaquettes,
        geometry.affected_counts,
        interval,
        seed,
    )
    coefficient_real, coefficient_imag, _ = transverse_coefficients(
        length, (1,)
    )
    blocks = []
    diversity_rows = []
    survival_rows = []
    minimum_dynamic_effective = float(population)
    for origin_index in range(4):
        (
            states,
            counts,
            correlations,
            effective,
            diversity,
            survival,
        ) = measure_multi_forward_block(
            states,
            counts,
            delta_v,
            coefficient_real,
            coefficient_imag,
            geometry.plaquette_links,
            geometry.affected_plaquettes,
            geometry.affected_counts,
            interval,
        )
        blocks.append(correlations)
        diversity_rows.append(diversity)
        survival_rows.append(survival)
        minimum_dynamic_effective = min(minimum_dynamic_effective, effective)
        if origin_index < 3:
            ancestors = np.arange(population, dtype=np.int32)
            labels = np.full((1, population), -1, dtype=np.int32)
            for _ in range(3):
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
    return MultiForwardReplica(
        correlations=np.mean(np.asarray(blocks), axis=0),
        population=population,
        energy=delta_v * mean_count,
        minimum_effective_fraction=min(
            minimum_effective, minimum_dynamic_effective
        )
        / population,
        origin_diversity_fractions=np.min(
            np.asarray(diversity_rows), axis=0
        ),
        forward_survival_fractions=np.min(
            np.asarray(survival_rows), axis=0
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
    )


def gap_vector(
    curves: np.ndarray,
    energies: np.ndarray,
    window: tuple[int, int],
) -> np.ndarray:
    return np.asarray(
        [
            effective_gap(
                np.mean(curves[:, forward_index], axis=0).real,
                8,
                float(np.mean(energies)),
                *window,
            )
            for forward_index in range(len(FORWARD_LENGTHS))
        ]
    )


def summarize(
    delta_v: float,
    replicas: list[MultiForwardReplica],
) -> ForwardSummary:
    curves = np.asarray(
        [np.mean(replica.correlations, axis=2) for replica in replicas]
    )
    energies = np.asarray([replica.energy for replica in replicas])
    gaps = {}
    covariances = {}
    for window in WINDOWS:
        gaps[window] = gap_vector(curves, energies, window)
        leave_one_out = []
        for omitted in range(len(curves)):
            mask = np.arange(len(curves)) != omitted
            leave_one_out.append(gap_vector(curves[mask], energies[mask], window))
        jackknife = np.asarray(leave_one_out)
        deviations = jackknife - np.mean(jackknife, axis=0)
        covariances[window] = (
            (len(jackknife) - 1.0)
            / len(jackknife)
            * deviations.T
            @ deviations
        )
    mean_curves = np.mean(curves, axis=0)
    return ForwardSummary(
        delta_v=delta_v,
        gaps=gaps,
        covariances=covariances,
        mean_curves=mean_curves,
        imaginary_residual=float(np.max(np.abs(mean_curves.imag))),
        minimum_effective_fraction=min(
            replica.minimum_effective_fraction for replica in replicas
        ),
        minimum_origin_tau16_count=min(
            replica.population * replica.origin_diversity_fractions[16]
            for replica in replicas
        ),
        minimum_forward_count=min(
            replica.population * np.min(replica.forward_survival_fractions)
            for replica in replicas
        ),
        count_consistent=all(replica.count_consistent for replica in replicas),
        sector_consistent=all(replica.sector_consistent for replica in replicas),
    )


def main() -> int:
    checks = Checks()
    summaries = {}
    for coupling_index, delta_v in enumerate((-0.05, 0.0)):
        population = 2048 if delta_v else 1024
        replicas = [
            run_replica(
                delta_v,
                population,
                34_000_000 + 1_000_000 * coupling_index + replica,
            )
            for replica in range(6)
        ]
        summaries[delta_v] = summarize(delta_v, replicas)
    rows = list(summaries.values())
    checks.check(
        all(row.count_consistent and row.sector_consistent for row in rows),
        "every multi-forward population preserves exact counts and sectors",
    )
    checks.check(
        min(row.minimum_effective_fraction for row in rows) > 0.85
        and min(row.minimum_origin_tau16_count for row in rows) >= 40
        and min(row.minimum_forward_count for row in rows) >= 40,
        "every forward length retains the declared weight and genealogy floors",
    )
    checks.check(
        all(
            all(
                np.all(np.isfinite(row.gaps[window]))
                and np.all(row.gaps[window] > 0.0)
                and np.all(np.isfinite(row.covariances[window]))
                for window in WINDOWS
            )
            and np.all(row.mean_curves.real > 0.0)
            and row.imaginary_residual < 0.06
            for row in rows
        ),
        "every multi-forward correlator, gap, and covariance remains finite and positive",
    )
    target_indices = [FORWARD_LENGTHS.index(value) for value in (8, 10, 12)]
    checks.check(
        all(
            np.linalg.matrix_rank(
                row.covariances[window][np.ix_(target_indices, target_indices)],
                tol=1.0e-14,
            )
            == 3
            for row in rows
            for window in TARGET_WINDOWS
        ),
        "every long-forward three-point covariance has full rank",
    )
    for delta_v in (-0.05, 0.0):
        row = summaries[delta_v]
        for window in WINDOWS:
            print(
                "FORWARD_GAPS",
                f"V={1.0 + delta_v:.2f}",
                f"window={window[0]}-{window[1]}",
                "values="
                + ",".join(
                    f"{forward}:{row.gaps[window][index]:.8f}"
                    for index, forward in enumerate(FORWARD_LENGTHS)
                ),
            )
            if window in TARGET_WINDOWS:
                print(
                    "FORWARD_COVARIANCE",
                    f"V={1.0 + delta_v:.2f}",
                    f"window={window[0]}-{window[1]}",
                    "row_major="
                    + ",".join(
                        f"{value:.12e}"
                        for value in row.covariances[window].ravel()
                    ),
                )
    print(
        "HEALTH",
        f"min_ess={min(row.minimum_effective_fraction for row in rows):.6f}",
        f"min_origin_tau16={min(row.minimum_origin_tau16_count for row in rows):.0f}",
        f"min_forward={min(row.minimum_forward_count for row in rows):.0f}",
    )
    print(
        "CERTIFICATE: fixed_L=8 paired_forward_lengths=2,4,6,8,10,12 "
        "outer_population_covariance=True result_test_deferred=True"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
