#!/usr/bin/env python3
"""Late-time transverse spectrum and the same-detuning Maxwell join.

This runner reuses the exact positive-projector forward-walking estimator from
the transverse-crossover parent, but extends the first-momentum correlator to
tau=16.  Matched RK and V=0.95 populations test whether late projection repairs
the apparent c^2 versus U K mismatch and whether the first omitted q^6 term,
rather than excited-state contamination, controls that comparison.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

import numpy as np

from spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03 import (
    ReplicaResult,
    effective_gap,
    exact_small_correlations,
    run_replica,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py",
)

AUDIT_TIMEOUT_SEC = 10800


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
class WindowEstimate:
    start: int
    stop: int
    gap: float
    gap_error: float


@dataclass(frozen=True)
class LadderRow:
    length: int
    delta_v: float
    windows: dict[tuple[int, int], WindowEstimate]
    mean_curve: np.ndarray
    mean_energy: float
    imaginary_residual: float
    minimum_effective_fraction: float
    minimum_origin_tau16_count: float
    minimum_forward_count: float
    count_consistent: bool
    sector_consistent: bool


@dataclass(frozen=True)
class ExcessFit:
    c_squared: float
    c_squared_error: float
    q4_coefficient: float
    q4_coefficient_error: float
    chi_squared: float
    fixed_q4_coefficient: float
    fixed_q4_error: float
    fixed_chi_squared: float
    fixed_delta_chi_squared: float


@dataclass(frozen=True)
class HigherGradientFit:
    c_squared: float
    c_squared_error: float
    q4_coefficient: float
    q4_coefficient_error: float
    q6_coefficient: float
    q6_coefficient_error: float
    chi_squared: float
    fixed_q4_coefficient: float
    fixed_q4_error: float
    fixed_q6_coefficient: float
    fixed_q6_error: float
    fixed_chi_squared: float
    fixed_delta_chi_squared: float


def first_harmonic_curve(
    result: ReplicaResult, modes: list[tuple[int, int, int]]
) -> np.ndarray:
    indices = [index for index, mode in enumerate(modes) if mode[0] == 1]
    return np.mean(result.correlations[:, indices], axis=1)


def jackknife_window(
    curves: np.ndarray,
    energies: np.ndarray,
    length: int,
    start: int,
    stop: int,
) -> WindowEstimate:
    mean_curve = np.mean(curves, axis=0).real
    mean_energy = float(np.mean(energies))
    central = effective_gap(mean_curve, length, mean_energy, start, stop)
    leave_one_out = []
    for omitted in range(len(curves)):
        mask = np.arange(len(curves)) != omitted
        leave_one_out.append(
            effective_gap(
                np.mean(curves[mask], axis=0).real,
                length,
                float(np.mean(energies[mask])),
                start,
                stop,
            )
        )
    values = np.asarray(leave_one_out)
    error = np.sqrt(
        (len(values) - 1.0)
        / len(values)
        * np.sum((values - np.mean(values)) ** 2)
    )
    return WindowEstimate(start, stop, float(central), float(error))


def summarize_row(
    length: int,
    delta_v: float,
    replicas: list[tuple[ReplicaResult, list[tuple[int, int, int]]]],
) -> LadderRow:
    modes = replicas[0][1]
    if any(row_modes != modes for _, row_modes in replicas):
        raise AssertionError("mode ordering changed between replicas")
    curves = np.asarray(
        [first_harmonic_curve(result, modes) for result, _ in replicas]
    )
    energies = np.asarray([result.energy for result, _ in replicas])
    windows = {
        pair: jackknife_window(curves, energies, length, *pair)
        for pair in ((2, 6), (6, 12), (8, 14), (10, 16))
    }
    mean_curve = np.mean(curves, axis=0)
    return LadderRow(
        length=length,
        delta_v=delta_v,
        windows=windows,
        mean_curve=mean_curve,
        mean_energy=float(np.mean(energies)),
        imaginary_residual=float(np.max(np.abs(mean_curve.imag))),
        minimum_effective_fraction=min(
            result.minimum_effective_population_fraction
            for result, _ in replicas
        ),
        minimum_origin_tau16_count=min(
            result.population * result.origin_diversity_fractions[16]
            for result, _ in replicas
        ),
        minimum_forward_count=min(
            result.population * np.min(result.forward_survival_fractions)
            for result, _ in replicas
        ),
        count_consistent=all(
            result.count_consistent for result, _ in replicas
        ),
        sector_consistent=all(
            result.sector_consistent for result, _ in replicas
        ),
    )


def fit_excess(
    detuned: list[LadderRow],
    rk: list[LadderRow],
    window: tuple[int, int],
    fixed_c_squared: float,
) -> ExcessFit:
    rk_by_length = {row.length: row for row in rk}
    response = []
    errors = []
    design = []
    for row in detuned:
        reference = rk_by_length[row.length]
        detuned_gap = row.windows[window]
        rk_gap = reference.windows[window]
        q = 2.0 * np.sin(np.pi / row.length)
        response.append(detuned_gap.gap**2 - rk_gap.gap**2)
        errors.append(
            2.0
            * np.hypot(
                detuned_gap.gap * detuned_gap.gap_error,
                rk_gap.gap * rk_gap.gap_error,
            )
        )
        design.append((q**2, q**4))
    values = np.asarray(response)
    uncertainties = np.maximum(np.asarray(errors), 1e-10)
    matrix = np.asarray(design)
    weights = np.diag(1.0 / uncertainties**2)
    covariance = np.linalg.inv(matrix.T @ weights @ matrix)
    coefficients = covariance @ (matrix.T @ weights @ values)
    residual = (values - matrix @ coefficients) / uncertainties

    q2 = matrix[:, 0]
    q4 = matrix[:, 1]
    fixed_response = values - fixed_c_squared * q2
    scalar_weights = 1.0 / uncertainties**2
    fixed_q4 = float(
        np.sum(scalar_weights * q4 * fixed_response)
        / np.sum(scalar_weights * q4**2)
    )
    fixed_q4_error = float(
        np.sqrt(1.0 / np.sum(scalar_weights * q4**2))
    )
    fixed_residual = (
        values - fixed_c_squared * q2 - fixed_q4 * q4
    ) / uncertainties
    chi_squared = float(np.dot(residual, residual))
    fixed_chi_squared = float(np.dot(fixed_residual, fixed_residual))
    return ExcessFit(
        c_squared=float(coefficients[0]),
        c_squared_error=float(np.sqrt(covariance[0, 0])),
        q4_coefficient=float(coefficients[1]),
        q4_coefficient_error=float(np.sqrt(covariance[1, 1])),
        chi_squared=chi_squared,
        fixed_q4_coefficient=fixed_q4,
        fixed_q4_error=fixed_q4_error,
        fixed_chi_squared=fixed_chi_squared,
        fixed_delta_chi_squared=fixed_chi_squared - chi_squared,
    )


def fit_higher_gradient_excess(
    detuned: list[LadderRow],
    rk: list[LadderRow],
    window: tuple[int, int],
    fixed_c_squared: float,
    fixed_c_squared_error: float,
) -> HigherGradientFit:
    """Fit the excess through q^6, both freely and at fixed c^2=U K."""

    rk_by_length = {row.length: row for row in rk}
    response = []
    errors = []
    design = []
    for row in detuned:
        reference = rk_by_length[row.length]
        detuned_gap = row.windows[window]
        rk_gap = reference.windows[window]
        q = 2.0 * np.sin(np.pi / row.length)
        response.append(detuned_gap.gap**2 - rk_gap.gap**2)
        errors.append(
            2.0
            * np.hypot(
                detuned_gap.gap * detuned_gap.gap_error,
                rk_gap.gap * rk_gap.gap_error,
            )
        )
        design.append((q**2, q**4, q**6))
    values = np.asarray(response)
    uncertainties = np.maximum(np.asarray(errors), 1e-10)
    matrix = np.asarray(design)
    weights = np.diag(1.0 / uncertainties**2)
    covariance = np.linalg.inv(matrix.T @ weights @ matrix)
    coefficients = covariance @ (matrix.T @ weights @ values)
    residual = (values - matrix @ coefficients) / uncertainties

    fixed_matrix = matrix[:, 1:]
    fixed_response = values - fixed_c_squared * matrix[:, 0]
    fixed_covariance = np.linalg.inv(
        fixed_matrix.T @ weights @ fixed_matrix
    )
    fixed_coefficients = fixed_covariance @ (
        fixed_matrix.T @ weights @ fixed_response
    )
    fixed_sensitivity = -fixed_covariance @ (
        fixed_matrix.T @ weights @ matrix[:, 0]
    )
    fixed_total_covariance = fixed_covariance + np.outer(
        fixed_sensitivity, fixed_sensitivity
    ) * fixed_c_squared_error**2
    fixed_residual = (
        fixed_response - fixed_matrix @ fixed_coefficients
    ) / uncertainties
    chi_squared = float(np.dot(residual, residual))
    fixed_chi_squared = float(np.dot(fixed_residual, fixed_residual))
    return HigherGradientFit(
        c_squared=float(coefficients[0]),
        c_squared_error=float(np.sqrt(covariance[0, 0])),
        q4_coefficient=float(coefficients[1]),
        q4_coefficient_error=float(np.sqrt(covariance[1, 1])),
        q6_coefficient=float(coefficients[2]),
        q6_coefficient_error=float(np.sqrt(covariance[2, 2])),
        chi_squared=chi_squared,
        fixed_q4_coefficient=float(fixed_coefficients[0]),
        fixed_q4_error=float(np.sqrt(fixed_total_covariance[0, 0])),
        fixed_q6_coefficient=float(fixed_coefficients[1]),
        fixed_q6_error=float(np.sqrt(fixed_total_covariance[1, 1])),
        fixed_chi_squared=fixed_chi_squared,
        fixed_delta_chi_squared=fixed_chi_squared - chi_squared,
    )


def run_ladder(
    delta_v: float,
    lengths: tuple[int, ...],
    replica_counts: dict[int, int],
    populations: dict[int, int],
    seed_root: int,
) -> list[LadderRow]:
    rows = []
    for length in lengths:
        replicas = []
        for replica in range(replica_counts[length]):
            result = run_replica(
                length,
                delta_v,
                population=populations[length],
                classical_sweeps=100,
                burn_sweeps=200 if delta_v else 120,
                tau_max=16,
                forward_sweeps=6,
                seed=seed_root + 1000 * length + replica,
                harmonics=(1,),
                measurement_origins=4,
                origin_spacing=3,
            )
            replicas.append(result)
        rows.append(summarize_row(length, delta_v, replicas))
        print(
            "ROW_DONE",
            f"V={1.0 + delta_v:.2f}",
            f"L={length}",
            "gaps="
            + ",".join(
                f"{start}-{stop}:{rows[-1].windows[(start, stop)].gap:.6f}"
                f"+/-{rows[-1].windows[(start, stop)].gap_error:.6f}"
                for start, stop in ((2, 6), (6, 12), (8, 14), (10, 16))
            ),
            flush=True,
        )
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--scout", action="store_true")
    arguments = parser.parse_args()
    checks = Checks()
    lengths = (8, 10, 12) if arguments.scout else (8, 10, 12, 14)
    if arguments.scout:
        detuned_replica_counts = {length: 2 for length in lengths}
        rk_replica_counts = {length: 2 for length in lengths}
        detuned_populations = {length: 1024 for length in lengths}
        rk_populations = {length: 512 for length in lengths}
    else:
        detuned_replica_counts = {8: 6, 10: 6, 12: 6, 14: 4}
        rk_replica_counts = {8: 6, 10: 6, 12: 6, 14: 4}
        detuned_populations = {8: 2048, 10: 2048, 12: 2048, 14: 3072}
        rk_populations = {8: 1024, 10: 1024, 12: 1024, 14: 1536}

    detuned = run_ladder(
        -0.05,
        lengths,
        detuned_replica_counts,
        detuned_populations,
        12_000_000,
    )
    rk = run_ladder(
        0.0,
        lengths,
        rk_replica_counts,
        rk_populations,
        13_000_000,
    )
    all_rows = detuned + rk
    checks.check(
        all(row.count_consistent and row.sector_consistent for row in all_rows),
        "every late-time population preserves exact flippability, Gauss charge, and zero electric flux",
    )
    checks.check(
        min(row.minimum_effective_fraction for row in all_rows) > 0.85
        and min(row.minimum_origin_tau16_count for row in all_rows) >= 40
        and min(row.minimum_forward_count for row in all_rows) >= 40,
        "late-time populations retain effective weight and at least forty independent genealogy labels",
    )
    checks.check(
        all(
            np.all(row.mean_curve.real > 0.0)
            and row.imaginary_residual < 0.06
            for row in all_rows
        ),
        "every cubic-average correlator remains positive through tau=16 with a bounded imaginary residual",
    )

    electric_stiffness = 0.162638
    electric_stiffness_error = 0.015345
    magnetic_stiffness = 0.075561
    magnetic_stiffness_error = 0.000915
    maxwell_c_squared = electric_stiffness * magnetic_stiffness
    maxwell_c_squared_error = np.hypot(
        electric_stiffness * magnetic_stiffness_error,
        magnetic_stiffness * electric_stiffness_error,
    )
    fits = {
        window: fit_excess(detuned, rk, window, maxwell_c_squared)
        for window in ((2, 6), (6, 12), (8, 14), (10, 16))
    }
    higher_fits = {
        window: fit_higher_gradient_excess(
            detuned,
            rk,
            window,
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        for window in ((2, 6), (6, 12), (8, 14), (10, 16))
    }
    early = fits[(2, 6)]
    late = fits[(8, 14)]
    terminal = fits[(10, 16)]
    higher_late = higher_fits[(8, 14)]
    higher_terminal = higher_fits[(10, 16)]
    checks.check(
        early.c_squared > 0.0 and late.c_squared > 0.0,
        "both early and late transverse excess fits retain a positive q-squared coefficient",
    )
    if not arguments.scout:
        checks.check(
            abs(late.c_squared - early.c_squared)
            < 2.0
            * np.hypot(late.c_squared_error, early.c_squared_error),
            "late-time projection leaves the two-term infrared coefficient statistically unchanged",
        )
        checks.check(
            late.fixed_delta_chi_squared > 9.0
            and terminal.fixed_delta_chi_squared > 9.0,
            "the q-squared plus q-fourth truncation rejects fixed c-squared=U K at late time",
        )
        checks.check(
            abs(higher_late.c_squared - maxwell_c_squared)
            < 2.0
            * np.hypot(
                higher_late.c_squared_error, maxwell_c_squared_error
            )
            and abs(higher_terminal.c_squared - maxwell_c_squared)
            < 2.0
            * np.hypot(
                higher_terminal.c_squared_error, maxwell_c_squared_error
            ),
            "free q-sixth fits at both late windows are compatible with the independent U K prediction",
        )
        checks.check(
            all(
                fit.fixed_chi_squared < 6.0
                and fit.fixed_delta_chi_squared < 4.0
                for fit in higher_fits.values()
            ),
            "fixed c-squared=U K plus q-fourth and q-sixth fits every projection window without a significant penalty",
        )
        checks.check(
            higher_late.fixed_q4_coefficient
            > 3.0 * higher_late.fixed_q4_error
            and higher_late.fixed_q6_coefficient
            < -3.0 * higher_late.fixed_q6_error
            and higher_terminal.fixed_q4_coefficient
            > 3.0 * higher_terminal.fixed_q4_error
            and higher_terminal.fixed_q6_coefficient
            < -3.0 * higher_terminal.fixed_q6_error,
            "fixed-U K late fits resolve positive q-fourth and negative q-sixth corrections",
        )
        checks.check(
            abs(terminal.c_squared - late.c_squared)
            < 2.0
            * np.hypot(terminal.c_squared_error, late.c_squared_error),
            "the terminal and primary late-time windows give compatible infrared coefficients",
        )

    # The exact L=2 calculation is cheap and checks that extending tau does not
    # alter the Green-time normalization used by effective_gap.
    exact_energy, exact_curve, _ = exact_small_correlations(-0.05, 16)
    exact_mean = np.mean(exact_curve, axis=1)
    exact_gap_early = effective_gap(exact_mean, 2, exact_energy, 2, 6)
    exact_gap_late = effective_gap(exact_mean, 2, exact_energy, 8, 14)
    checks.check(
        exact_gap_early > 0.0 and exact_gap_late > 0.0,
        "the exact L=2 Green correlator retains positive early and late decay scales",
    )

    for window, fit in fits.items():
        print(
            "EXCESS_FIT",
            f"window={window[0]}-{window[1]}",
            f"c2={fit.c_squared:.8f}+/-{fit.c_squared_error:.8f}",
            f"q4={fit.q4_coefficient:.8f}+/-{fit.q4_coefficient_error:.8f}",
            f"chi2={fit.chi_squared:.4f}",
            f"fixed_UK_q4={fit.fixed_q4_coefficient:.8f}"
            f"+/-{fit.fixed_q4_error:.8f}",
            f"fixed_chi2={fit.fixed_chi_squared:.4f}",
            f"fixed_delta_chi2={fit.fixed_delta_chi_squared:.4f}",
        )
    for window, fit in higher_fits.items():
        print(
            "HIGHER_GRADIENT_FIT",
            f"window={window[0]}-{window[1]}",
            f"c2={fit.c_squared:.8f}+/-{fit.c_squared_error:.8f}",
            f"q4={fit.q4_coefficient:.8f}+/-{fit.q4_coefficient_error:.8f}",
            f"q6={fit.q6_coefficient:.8f}+/-{fit.q6_coefficient_error:.8f}",
            f"chi2={fit.chi_squared:.4f}",
            f"fixed_UK_q4={fit.fixed_q4_coefficient:.8f}"
            f"+/-{fit.fixed_q4_error:.8f}",
            f"fixed_UK_q6={fit.fixed_q6_coefficient:.8f}"
            f"+/-{fit.fixed_q6_error:.8f}",
            f"fixed_chi2={fit.fixed_chi_squared:.4f}",
            f"fixed_delta_chi2={fit.fixed_delta_chi_squared:.4f}",
        )
    print(
        "MAXWELL_TARGET",
        f"UK={maxwell_c_squared:.6f}+/-{maxwell_c_squared_error:.6f}",
        f"early_c2={early.c_squared:.6f}+/-{early.c_squared_error:.6f}",
        f"late_c2={late.c_squared:.6f}+/-{late.c_squared_error:.6f}",
        f"terminal_c2={terminal.c_squared:.6f}+/-{terminal.c_squared_error:.6f}",
    )
    print(
        "GENEALOGY",
        f"min_ess={min(row.minimum_effective_fraction for row in all_rows):.6f}",
        f"min_origin_tau16={min(row.minimum_origin_tau16_count for row in all_rows):.0f}",
        f"min_forward={min(row.minimum_forward_count for row in all_rows):.0f}",
    )
    print(
        "CERTIFICATE: exact_positive_green=True paired_RK_control=True "
        "finite_population=True finite_imaginary_time=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
