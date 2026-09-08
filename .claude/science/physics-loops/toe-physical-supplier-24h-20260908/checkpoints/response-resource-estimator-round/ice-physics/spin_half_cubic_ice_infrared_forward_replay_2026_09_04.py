#!/usr/bin/env python3
"""Predeclared high-genealogy, paired-forward L=16,18 replay.

The earlier infrared receipt used one forward suffix and missed its declared
tau=16 origin-diversity floor.  This independent replay raises the detuned
population before looking at a new result and records F=6,12,20 endpoints
from each shared trajectory.  A separate join owns every physics decision.
"""

from __future__ import annotations

import argparse
from concurrent.futures import (
    ProcessPoolExecutor,
    ThreadPoolExecutor,
    as_completed,
)
from dataclasses import dataclass
import multiprocessing as mp

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
    "scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py",
)

AUDIT_TIMEOUT_SEC = 64800
LENGTHS = (16, 18)
FORWARD_LENGTHS = (6, 12, 20)
WINDOWS = ((2, 6), (8, 14))
PRIMARY_WINDOW = (8, 14)
REPLICA_COUNT = 6
DETUNED_POPULATION = 6144
RK_POPULATION = 1536


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
class PairedRow:
    length: int
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
    """Measure all forward suffixes on one shared population trajectory."""

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
    length: int,
    delta_v: float,
    population: int,
    seed: int,
) -> MultiForwardReplica:
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
    length: int,
    window: tuple[int, int],
) -> np.ndarray:
    return np.asarray(
        [
            effective_gap(
                np.mean(curves[:, forward_index], axis=0).real,
                length,
                float(np.mean(energies)),
                *window,
            )
            for forward_index in range(len(FORWARD_LENGTHS))
        ]
    )


def summarize(
    length: int,
    delta_v: float,
    replicas: list[MultiForwardReplica],
) -> PairedRow:
    curves = np.asarray(
        [np.mean(replica.correlations, axis=2) for replica in replicas]
    )
    energies = np.asarray([replica.energy for replica in replicas])
    gaps = {}
    covariances = {}
    for window in WINDOWS:
        gaps[window] = gap_vector(curves, energies, length, window)
        leave_one_out = []
        for omitted in range(len(curves)):
            mask = np.arange(len(curves)) != omitted
            leave_one_out.append(
                gap_vector(curves[mask], energies[mask], length, window)
            )
        jackknife = np.asarray(leave_one_out)
        deviations = jackknife - np.mean(jackknife, axis=0)
        covariances[window] = (
            (len(jackknife) - 1.0)
            / len(jackknife)
            * deviations.T
            @ deviations
        )
    mean_curves = np.mean(curves, axis=0)
    return PairedRow(
        length=length,
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


def run_row(
    length: int,
    delta_v: float,
    population: int,
    seed_root: int,
    workers: int,
) -> PairedRow:
    futures = {}
    replicas: dict[int, MultiForwardReplica] = {}
    context = mp.get_context("spawn")
    with ProcessPoolExecutor(
        max_workers=workers, mp_context=context
    ) as executor:
        for replica_index in range(REPLICA_COUNT):
            seed = seed_root + 1000 * length + replica_index
            future = executor.submit(
                run_replica, length, delta_v, population, seed
            )
            futures[future] = replica_index
        for future in as_completed(futures):
            replica_index = futures[future]
            replicas[replica_index] = future.result()
            print(
                "REPLICA_DONE",
                f"V={1.0 + delta_v:.2f}",
                f"L={length}",
                f"replica={replica_index + 1}/{REPLICA_COUNT}",
                flush=True,
            )
    return summarize(
        length,
        delta_v,
        [replicas[index] for index in range(REPLICA_COUNT)],
    )


def emit_row(row: PairedRow) -> None:
    """Emit one row in the stable receipt format after it closes."""
    for window in WINDOWS:
        errors = np.sqrt(np.diag(row.covariances[window]))
        print(
            "PAIRED_ROW",
            f"V={1.0 + row.delta_v:.2f}",
            f"L={row.length}",
            f"window={window[0]}-{window[1]}",
            "gaps="
            + ",".join(
                f"{forward}:{row.gaps[window][index]:.8f}"
                f"+/-{errors[index]:.8f}"
                for index, forward in enumerate(FORWARD_LENGTHS)
            ),
            "cov="
            + ",".join(
                f"{value:.12e}" for value in row.covariances[window].ravel()
            ),
            flush=True,
        )
    print(
        "ROW_HEALTH",
        f"V={1.0 + row.delta_v:.2f}",
        f"L={row.length}",
        f"min_ess={row.minimum_effective_fraction:.6f}",
        f"min_origin_tau16={row.minimum_origin_tau16_count:.0f}",
        f"min_forward={row.minimum_forward_count:.0f}",
        flush=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument(
        "--parallel-rows",
        action="store_true",
        help="run the four independent coupling/volume rows concurrently",
    )
    arguments = parser.parse_args()
    if not 1 <= arguments.workers <= 2:
        raise SystemExit("--workers must be 1 or 2 on the 8 GiB host")

    row_specs = [
        (
            coupling_index,
            delta_v,
            LENGTHS[length_index],
            DETUNED_POPULATION if delta_v else RK_POPULATION,
            41_000_000 + 1_000_000 * coupling_index,
        )
        for coupling_index, delta_v in enumerate((-0.05, 0.0))
        for length_index in range(len(LENGTHS))
    ]
    rows_by_key: dict[tuple[int, int], PairedRow] = {}
    if arguments.parallel_rows:
        with ThreadPoolExecutor(max_workers=len(row_specs)) as executor:
            futures = {
                executor.submit(
                    run_row, length, delta_v, population, seed_root, arguments.workers
                ): (coupling_index, length)
                for coupling_index, delta_v, length, population, seed_root in row_specs
            }
            for future in as_completed(futures):
                key = futures[future]
                row = future.result()
                rows_by_key[key] = row
                emit_row(row)
    else:
        for coupling_index, delta_v, length, population, seed_root in row_specs:
            row = run_row(
                length,
                delta_v,
                population,
                seed_root,
                arguments.workers,
            )
            rows_by_key[(coupling_index, length)] = row
            emit_row(row)
    rows = [
        rows_by_key[(coupling_index, length)]
        for coupling_index, _delta_v, length, _population, _seed_root in row_specs
    ]

    checks = Checks()
    checks.check(
        all(row.count_consistent and row.sector_consistent for row in rows),
        "every replay population preserves exact counts, Gauss charge, "
        "and zero electric flux",
    )
    checks.check(
        min(row.minimum_effective_fraction for row in rows) > 0.85
        and min(row.minimum_origin_tau16_count for row in rows) >= 40
        and min(row.minimum_forward_count for row in rows) >= 40,
        "every replay population satisfies the pre-existing weight and "
        "genealogy floors",
    )
    checks.check(
        all(
            np.all(row.mean_curves.real > 0.0)
            and row.imaginary_residual < 0.06
            and all(
                np.all(np.isfinite(row.gaps[window]))
                and np.all(row.gaps[window] > 0.0)
                and np.all(np.isfinite(row.covariances[window]))
                for window in WINDOWS
            )
            for row in rows
        ),
        "every paired-forward correlator, gap, and covariance is finite and positive",
    )
    detuned = [row for row in rows if row.delta_v]
    rk = [row for row in rows if not row.delta_v]
    checks.check(
        all(
            np.linalg.matrix_rank(
                row.covariances[PRIMARY_WINDOW], tol=1.0e-14
            )
            == len(FORWARD_LENGTHS)
            for row in detuned
        )
        and all(
            np.all(row.gaps[window] == row.gaps[window][0])
            for row in rk
            for window in WINDOWS
        ),
        "detuned primary covariances are full rank and RK forward identity is exact",
    )
    print(
        "CERTIFICATE: lower_momenta=L16,L18 replicas=6 "
        "detuned_population=6144 rk_population=1536 "
        "paired_forward_lengths=6,12,20 measurement_origins=4 "
        "primary_window=8-14 finite_volume=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
