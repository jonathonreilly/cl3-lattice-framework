#!/usr/bin/env python3
"""Finite supplied-model definitions and historical receipt diagnostics.

Original production recipe and all earlier claims: .claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py.
Current execution is bounded diagnostics only; no production/physical Maxwell
certificate is supplied. Imaginary-time projection is not a Record formation law.
"""

from __future__ import annotations

from pathlib import Path
import re
import json
from types import SimpleNamespace
from spin_half_cubic_ice_historical_receipt_integrity_2026_09_09 import parse_ladder_payload

from spin_half_cubic_ice_historical_receipt_integrity_2026_09_09 import (historical_text, load_receipt, validate_covariance, check_inputs, held_production, historical_target, shared_zero_covariance, gls_mean)

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
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md',
    'docs/MINIMAL_AXIOMS_2026-06-29.md',
    'docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md',
    'docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md',
    'scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py',
    'scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py',
    'scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py',
    'scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py',
    'scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py',
    'scripts/spin_half_cubic_ice_historical_receipt_integrity_2026_09_09.py',
    'scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py',
    'scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py',
    'scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py',
    'scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py',
    'scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py',
    'scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py',
    'scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py',
    'scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py',
    'scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py',
    'scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py',
)

AUDIT_TIMEOUT_SEC = 150


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
    check_inputs(Path(__file__).resolve().parent.parent, AUDIT_EXPECTED_SHA256)
    checks=Checks(); receipt=load_receipt("spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt")
    windows=((2,6),(6,12),(8,14),(10,16)); lengths=(8,10,12,14)
    parsed=parse_ladder_payload(receipt.stdout,lengths,windows)
    def rows(v):
        return [SimpleNamespace(length=l,windows={w:WindowEstimate(*w,*parsed[(v,l,w)]) for w in windows}) for l in lengths]
    detuned,rk=rows(.95),rows(1.); reference=historical_target()["central_product"]
    checks.check(len(parsed)==32 and receipt.total==(11,0), "all thirty-two historical window estimates and original eleven checks are preserved")
    for window in windows:
        two=fit_excess(detuned,rk,window,reference)
        three=fit_higher_gradient_excess(detuned,rk,window,reference,0.)
        checks.check(np.isfinite(two.chi_squared+three.chi_squared) and three.chi_squared <= two.chi_squared+1e-8,
            f"nested polynomial fits use the same historical response at window {window}")
        print("FINITE_WINDOW_FIT",f"window={window[0]}-{window[1]}",f"q4_c2={two.c_squared:.8f}",f"q6_c2={three.c_squared:.8f}",f"q4_loss={two.chi_squared:.6f}",f"q6_loss={three.chi_squared:.6f}",f"fixed_number_loss={three.fixed_chi_squared:.6f}")
    print("FIXED_NUMBER",reference,"physical_target=False measured_target_error=unavailable fixed_scenario_variance=0")
    print("SCOPE: conditional arithmetic on rounded historical windows; overlapping-window significance uncalibrated; no projection-limit or physical-cause conclusion; long production held")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return int(checks.failed != 0)




# Current source/input identity: literal finite closure.
AUDIT_EXPECTED_SHA256 = {
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/NO_GO_DISCIPLINE_CHECKLIST_SPIN_HALF_INFRARED_FORWARD_REPLAY_2026-09-05.md': 'd005e28ff0cba15f5e5b27580055c2ae51958dfeb967c3603df0d01d8bd4526b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_CUBIC_GAUGE_QUADRATIC_MAXWELL_KERNEL_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'd9c836c854ee20dddf399d51d7bab6b13f9164a920a10ed2c0713cd6b4f150e4',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_CHARGE_COULOMB_FLUX_STIFFNESS_JOIN_BOUNDED_THEOREM_NOTE_2026-09-03.md': '1f6811e0f9a872c2a23946dbf313a32c378ca697f658423e0c13dcad708e0ff9',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_RELAXED_MAGNETIC_TWIST_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-04.md': '73d66f716fdfacc5c6d02f902b2021392e5139041b6018985d2886264a5007ed',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md': '862311719f14a9ba1ee6fc660477fd01510631a87db636f9098a626d5291316d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_FORWARD_LENGTH_CONVERGENCE_BOUNDED_THEOREM_NOTE_2026-09-04.md': '9b2aba542ed2f36643ce4b511b1f85db9b96a0a5b3570e5f306e561b6b8b246e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_FORWARD_REPLAY_RECOVERY_BOUNDARY_NOTE_2026-09-05.md': '1d22ab5c1f16784462b68ddf4021b7e14a110a6ca7be6cff92ffd279f9011715',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_INFRARED_MAXWELL_JOIN_HEALTH_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-04.md': '139bd99c4f1f9c86bf8f222cb6986957d8f24bfca335a5f3c0ea1654a5a4abbd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': '8a3369b50204369ddfd0311704cf71423a91c5c87df51a6e41dae4657b0ab947',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/docs/SPIN_HALF_CUBIC_ICE_OFF_AXIS_MAXWELL_HIGH_MOMENTUM_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'c47db40a423d54580b0e27ba844e302c0e9d5cb1105705fb1b5392f21ac00e36',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt': '992136071fbd1f87efbae5daec0689ce7309913ccc12fd294bdfc39a54ae569f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt': '2e483ff3d5bc34e7fdde41b8ab06790be1ea487a167bb10b33936e35ff22c894',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.txt': '97687c182b2c0a8f095bea6ddc90018e2580163af81757e1bbeaf2650c04fde7',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt': '366e0cfbca4cc582cc28c34c2e822990b5a1216d42513417677e818584cd4fea',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.txt': 'db3f966552fb31bab95a3d487220dd0622b21b5da127515f197e7e441ad68445',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt': '484c30b66ccbe992290da328e785c22f597dfc698173044c4cec178d3fbaf8b6',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.txt': '8ec096ed4b50bf92ee7d709470833d9355b8461c9e9c35e5579d1fec4402ed17',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt': 'd6ffe038be4e0a5dc6824965dbdcc24595aac7ba2241ef0ca059310ffeabd59e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt': '849646d782df0c360fd1d180b4d966b3499979b43d1c709b11b5c1e43c2a92e0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.txt': '5131098b985eab3d4991a5c767c1f057ba047ff694b5d074383037a27f65622c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt': '09f1e590b9cf2cade315bca1a854156a42faba262d22b55f21167bad7a6b798c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.txt': '88552107e8ce428aec277c61645322a927b209b3a3936ec4471e3344b4d50a35',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt': 'e6e00baa0a8bcb38afdd7cf1e46e09e0c8f5b6ba4422bc2fdcb45fac72a6a92c',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt': '2c2dec102b9758f4249818ed2ce935a0c582a5a3c3fead19d91b12aadb8b51af',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt': '17345ac4bd2839c8d0cd315fdc0d5c6126e3b8879f1b3f49bd055c637d0ec481',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt': 'acdfb65d3e785f08ba61b6958461db6154fcd2771e1d309834d00ece3ca48992',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.txt': '82e2ad2b36cc44b9a367a16554a52dc5a68c94690a571d642f37e9ececcb5216',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt': '6ec74acaacd3909cd39b0520c0bc93e690ca949c54119a60e84a89d55a7ea1d0',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt': '7d7cfba76fe8a0de63de2ecd2b2a6241d7401e3904258a45969d30ae76b3f728',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.txt': 'c77aab04384741c1bca11852b0554742db0b8c157545bded3c1b09735b3b42dc',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt': '5eda05ddbf46d54e600839ecd30f552d3362e3704071037e38c0632dc2f86e81',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/logs/runner-cache/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.txt': 'f28a3a727508e6c2df4a4f1e77d0d0bcfdb77a5d41a282f13219d9ef4a4aa202',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py': '97881c8721ee3177aeaa610a59f139ef44be809b49bc9c6ed9f0490fe6b10418',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py': 'a61b5ca89ea5b39ac932744b12e3af46167d81fd4ed5eb52acdb08644f74b28b',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py': '5bb190ef328d095d83eacf927e2c3964499f178e6f41254368047957a893227d',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py': 'aaa07511fdd1650fe317bd8fe03e4826beaa7f7cf5659c475b7b53e4a6b30733',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_finite_sample_reanalysis_2026_09_04.py': '421cd0399b35947d90f208ddab78b38b2caf7e7cd5f593613ff53af300aaf434',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py': '75461521b7bd0d3806e3a0598c4c82603f7127623762990d478784ad2ef542b1',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_high_stat_join_2026_09_04.py': '1aa54dbb1b298ee8064603b89e97470d541900d7affb61bf329f269908a2ceca',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py': '7ac21e04324b48c9215524d1e889693ee329a5fe0e3495d1a8c14832249bd953',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py': '8d87b4c4ffc219e7557cf0ad19213842738f8f8a2879493612e3740fd19d26da',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_forward_replay_join_2026_09_04.py': 'b0556cf80af1a4515ca1a134c435dd40c011f0dfb058acd743c2948522e12af8',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py': '80108851a3d3a77e8e2593502abfa17ee72eab7174ad7043f039afe2e5133867',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_failure_localization_2026_09_04.py': '756173baab1c9966bf8c2cdd03860f7736710e17edb7b453fe9e69bf2e328dfb',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py': '9b4fbd65bc089f160e90fef8d2e95b3eaaedb276fd582c9b4697ed393abd0eae',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py': 'fdb9e0d0de5d10282c782cd888a9e3823c76a9c2a253887e76ae8a686de8da1f',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py': '8cea10e54e91b643a39d2a757eb120ee992197defdf45dce4cac98e36d5197cd',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py': 'e93ddc34b6bdbca4e17a89aa1d1f2ebef140c8717138d9aa429c8911751dc189',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_high_q_localization_2026_09_04.py': '8be752a7b03f7db990958e4813c7e029e85e06736a7cc6644db712452ceddf96',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py': '6057a37e1415b3dce55c85923514ec481f6cb007921d2ed634c8237be18b7655',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py': 'fef6248c3b90c88c1038af037cd152b8e3d33577dcc31286328bdffe6cdfa0ec',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_staggered_orbit_scout_2026_09_04.py': 'ae6390773d562d8ffe37bae981cc64246e0cbebb817eff88b6383ca376e7eeac',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py': '477ca4a1af788464bb798ffa0bc5c2f42fd3c3c3591d22fd075b80e24cb82a4e',
    '.claude/science/physics-loops/light-successor-correction-20260909/originals/scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py': 'f621e2b2d00bf85525dae4a1a3f103dd156cb9ba837c5f8f4d5199282ae5c2cb',
    'data/field/spin_half_cubic_ice_successor_historical_receipts_2026_09_09.json': 'c1c7a1cdd92236409d829be9a8dad7700b169e6e8bc3f5d94e28fa34c25653a7',
    'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md': '5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b',
    'docs/MINIMAL_AXIOMS_2026-06-29.md': '93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753',
    'docs/SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md': '0d40064ad01d7754e65b787c2697c248b206624844a7098d83ebf7834cbc4b04',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_PROJECTOR_MAXWELL_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'c1cc8df7ae97504527fd26195e65670ad6ccf4e01982d0665040662b22ba0d7e',
    'docs/SPIN_HALF_CUBIC_ICE_FINITE_DETUNING_TRANSVERSE_LINEAR_SPECTRAL_CROSSOVER_BOUNDED_THEOREM_NOTE_2026-09-03.md': '16433c4b9b823cfbf453687be3bcfffc880542c72bb17180a8bd4c66f64352f8',
    'docs/SPIN_HALF_CUBIC_ICE_LATE_TIME_HIGHER_GRADIENT_MAXWELL_JOIN_LOCALIZATION_BOUNDED_THEOREM_NOTE_2026-09-04.md': 'cf6328fc34cbdb9b69411fbbc12dd00daeaa1f7eeade240c2ed5b20958bd9913',
    'docs/SPIN_HALF_CUBIC_ICE_POSITIVE_TOPOLOGICAL_ELECTRIC_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-03.md': '38aeb623dcec523202326e4b4e2c30cd05a2a612d8bcd81216599a038b91fcaa',
    'docs/U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.md': '4b05e927da85639cf5bd7aaa45244189467ba8f0ad0c7325e07e8f692b032d2d',
    'docs/U1_ROLE_COMPILED_YEE_MAXWELL_GENERATOR_AND_TIME_SELECTION_FORK_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'f238e2e384e1737b64df96adcbc30c48f7ceebe67b55c69a449c9a19ee95429d',
    'docs/U1_ROLE_ENCODED_DOUBLED_INCIDENCE_NEAREST_NEIGHBOR_GAUGE_LAW_BOUNDED_THEOREM_NOTE_2026-09-03.md': 'b8a6f37dff7ab8c7263ff8b8cd27faf549b268c3ac79a6a4ba26d56e38b8fe77',
    'scripts/compact_u1_quadratic_basin_maxwell_universality_2026_09_03.py': '7881de5fd06a33c2c36d6c252b7a363e8d357775ce16f0c82e517b9ce4848c44',
    'scripts/compact_u1_wilson_to_source_free_maxwell_2026_09_02.py': '585c9d0ab507aae8f7c66e0806ae071d99ffc781c56f42c0d0d8c08e6ece4aac',
    'scripts/gauge_link_central_registration_induced_bi_invariant_step_kernel_2026_07_02.py': '317b726df0cf682d2bce47ff839b2e0ed7c1fa3aa56d08e824d3d4676b46f466',
    'scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py': 'a710a92baaaa7492cfeb7eaaa8db1e88cf902b6abc3531d4d9031a90310e3210',
    'scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py': 'b33240c4575531738a01ca14e4d43d9687432c7eee27e434d389c24b0ee1986c',
    'scripts/spin_half_cubic_ice_historical_receipt_integrity_2026_09_09.py': 'a5514a656d9d3b82c0b76c46e5aff2b9e731eb6b634de2bc99b25b9af458f54f',
    'scripts/spin_half_cubic_ice_rk_coulomb_photon_phase_bridge_2026_09_03.py': 'd10e0a59dedf58df6a23b9a08162a7b8bff58f55fd00ecdfb68e5ad7e5eda5d8',
    'scripts/spin_half_cubic_ice_topological_electric_stiffness_2026_09_03.py': '405acaa8d0e7cd0e2621fc1bc188dce61fd42ae60bb9d44b58bce65e37175300',
    'scripts/u1_auxiliary_face_local_conditionals_gauge_measure_2026_09_03.py': 'bbfdc4b33ac1725d82d778ddc2da805d79e3bfc3ca8e73a0a1fa558e8521719e',
    'scripts/u1_local_reversible_yee_leapfrog_tick_2026_09_03.py': '8b8e950015cd7b3befe6515a270d81c4435187fb4477a6997751652c80f49bf6',
    'scripts/u1_minimal_maxwell_generator_uniqueness_2026_09_03.py': 'd5963665437c2bec0af54dc64f9c27ba6c3a714c96f32843ad89125b712dc0c9',
    'scripts/u1_record_distribution_overlap_maxwell_germ_2026_09_03.py': 'db523208f850ea9eb0028e028b9fcadffe65a8a1d35a71535fa7a9dd6b345e3b',
    'scripts/u1_record_face_likelihood_spatial_gauge_photon_germ_2026_09_03.py': 'e3a2cd41c739475b341d7a9b173f344e30920d4bf49d461a11af0d0c2a7bbf8f',
    'scripts/u1_representation_positive_record_kernel_maxwell_germ_2026_09_03.py': 'd450a0f17e886ab4ba6ccf7caf56068751a439601ea5ed9d1bdeb98e61e4b467',
    'scripts/u1_role_compiled_yee_maxwell_time_selection_fork_2026_09_03.py': '05ccde69a2b55aa701a6baf3d4a7f2b79668be5cd9f0f2fc9a4402e2af1051d5',
    'scripts/u1_role_encoded_nearest_neighbor_gauge_law_2026_09_03.py': '24c2032bfa3b6dfcb2b86f0a1e096f80f89de5140ef0beea56ade88a447ae919',
}

if __name__ == "__main__":
    raise SystemExit(main())
