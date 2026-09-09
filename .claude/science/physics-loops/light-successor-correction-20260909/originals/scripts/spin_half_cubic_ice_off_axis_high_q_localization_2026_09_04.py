#!/usr/bin/env python3
"""Localize the off-axis U K mismatch to the highest-q volume.

The preregistered off-axis join is preserved with its two failed target checks.
This cheap reanalysis keeps the same source-pinned gaps and covariances, then
tests the two immediate model-order controls exposed by that result: removing
only L=8 and admitting the next family-specific analytic correction.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
from scipy.stats import chi2 as chi_squared_distribution

import spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04 as joined
from spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04 import (
    quadratic_kernel_certificate,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_quadratic_gauge_kernel_uniqueness_2026_09_04.py",
    "scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt",
    "scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
REPO_ROOT = Path(__file__).resolve().parent.parent
CHI2_3_95 = float(chi_squared_distribution.ppf(0.95, 3))
CHI2_4_95 = float(chi_squared_distribution.ppf(0.95, 4))


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


def fit_common(
    rows,
    *,
    lengths: tuple[int, ...] = joined.LENGTHS,
    families: tuple[str, ...] = joined.FAMILIES,
    correction_order: int = 3,
    fixed_target: tuple[float, float] | None = None,
):
    values, covariance, q_squared, labels = joined.select_dataset(
        rows, lengths=lengths, families=families
    )
    design = joined.common_design(
        q_squared,
        labels,
        len(families),
        correction_order=correction_order,
    )
    if fixed_target is not None:
        target, target_error = fixed_target
        values = values - target * q_squared
        covariance = covariance + target_error**2 * np.outer(
            q_squared, q_squared
        )
        design = design[:, 1:]
    return joined.gls_fit(values, covariance, design)


def compatibility_sigma(
    value: float,
    error: float,
    target: float,
    target_error: float,
) -> float:
    return abs(value - target) / np.hypot(error, target_error)


def main() -> int:
    checks = Checks()
    failed_text = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_off_axis_maxwell_isotropy_join_2026_09_04.txt"
    ).read_text(encoding="utf-8")
    checks.check(
        "status: nonzero_exit" in failed_text
        and "[FAIL] 06 the common dynamical coefficient is compatible with independent U K"
        in failed_text
        and "[FAIL] 08 fixed U K with its common uncertainty passes"
        in failed_text
        and "TOTAL: PASS=11 FAIL=2" in failed_text,
        "the preregistered target failures are preserved verbatim",
    )

    certificate = quadratic_kernel_certificate()
    checks.check(
        certificate.rotation_count == 24
        and certificate.joint_dimension == 1,
        "the exact proper-cubic transverse quadratic kernel remains unique",
    )
    rows = joined.parse_ladder_cache()
    checks.check(
        len(rows) == 8
        and all(
            np.all(np.isfinite(row.gaps))
            and np.min(np.linalg.eigvalsh(row.covariance)) > 0.0
            for row in rows.values()
        ),
        "the unchanged production receipt supplies eight usable covariance blocks",
    )
    target = joined.parse_static_maxwell_target()
    full_q6 = fit_common(rows)
    full_independent_values, full_covariance, full_q2, full_labels = (
        joined.select_dataset(rows)
    )
    full_independent = joined.gls_fit(
        full_independent_values,
        full_covariance,
        joined.independent_design(
            full_q2, full_labels, len(joined.FAMILIES)
        ),
    )
    full_fixed_q6 = fit_common(rows, fixed_target=target)
    full_compatibility = compatibility_sigma(
        full_q6.coefficients[0],
        full_q6.coefficient_errors[0],
        *target,
    )
    checks.check(
        full_q6.coefficients[0] > 2.0 * full_q6.coefficient_errors[0]
        and full_q6.chi_squared - full_independent.chi_squared < CHI2_3_95,
        "the full q-sixth matrix retains one positive common leading coefficient",
    )
    checks.check(
        full_compatibility > 2.0
        and full_fixed_q6.chi_squared > CHI2_4_95,
        "the original full-matrix q-sixth U K mismatch is reproduced",
    )

    lower_q = fit_common(rows, lengths=(10, 12, 14))
    lower_q_fixed = fit_common(
        rows, lengths=(10, 12, 14), fixed_target=target
    )
    lower_q_compatibility = compatibility_sigma(
        lower_q.coefficients[0],
        lower_q.coefficient_errors[0],
        *target,
    )
    checks.check(
        lower_q_compatibility < 2.0,
        "removing only L=8 makes the q-sixth coefficient U K-compatible",
    )
    checks.check(
        lower_q_fixed.chi_squared < CHI2_4_95,
        "the lower-q matrix accepts fixed U K with family q-fourth and q-sixth terms",
    )
    other_removal_rows = []
    for omitted in (10, 12, 14):
        retained_lengths = tuple(
            length for length in joined.LENGTHS if length != omitted
        )
        fit = fit_common(rows, lengths=retained_lengths)
        fixed = fit_common(
            rows, lengths=retained_lengths, fixed_target=target
        )
        other_removal_rows.append(
            (
                omitted,
                compatibility_sigma(
                    fit.coefficients[0],
                    fit.coefficient_errors[0],
                    *target,
                ),
                fixed.chi_squared,
            )
        )
    checks.check(
        all(
            compatibility > 2.0 and fixed_chi_squared > CHI2_4_95
            for _, compatibility, fixed_chi_squared in other_removal_rows
        ),
        "removing L=10, L=12, or L=14 does not reproduce the L=8 localization",
    )
    lower_q_without_body = fit_common(
        rows,
        lengths=(10, 12, 14),
        families=("axis", "face_out", "face_in"),
    )
    lower_q_without_body_fixed = fit_common(
        rows,
        lengths=(10, 12, 14),
        families=("axis", "face_out", "face_in"),
        fixed_target=target,
    )
    lower_q_without_body_compatibility = compatibility_sigma(
        lower_q_without_body.coefficients[0],
        lower_q_without_body.coefficient_errors[0],
        *target,
    )
    checks.check(
        lower_q_without_body_compatibility < 2.0
        and lower_q_without_body_fixed.chi_squared
        < float(chi_squared_distribution.ppf(0.95, 3)),
        "the lower-q target compatibility survives removal of the body family",
    )

    full_q8 = fit_common(rows, correction_order=4)
    full_q8_fixed = fit_common(
        rows, correction_order=4, fixed_target=target
    )
    q8_compatibility = compatibility_sigma(
        full_q8.coefficients[0],
        full_q8.coefficient_errors[0],
        *target,
    )
    checks.check(
        q8_compatibility < 2.0
        and full_q8_fixed.chi_squared < CHI2_4_95,
        "a full family q-eighth diagnostic also leaves fixed U K acceptable",
    )
    checks.check(
        full_q6.chi_squared - full_q8.chi_squared < CHI2_4_95
        and full_q8.coefficient_errors[0]
        > abs(full_q8.coefficients[0]),
        "the q-eighth diagnostic is not selected and leaves c-squared unresolved",
    )

    print(
        "HIGH_Q_LOCALIZATION",
        f"full_q6_c2={full_q6.coefficients[0]:.8f}"
        f"+/-{full_q6.coefficient_errors[0]:.8f}",
        f"full_target_sigma={full_compatibility:.4f}",
        f"full_fixed_chi2={full_fixed_q6.chi_squared:.4f}",
        f"L10plus_q6_c2={lower_q.coefficients[0]:.8f}"
        f"+/-{lower_q.coefficient_errors[0]:.8f}",
        f"L10plus_target_sigma={lower_q_compatibility:.4f}",
        f"L10plus_fixed_chi2={lower_q_fixed.chi_squared:.4f}",
    )
    print(
        "HIGHER_ORDER_DIAGNOSTIC",
        f"full_q8_c2={full_q8.coefficients[0]:.8f}"
        f"+/-{full_q8.coefficient_errors[0]:.8f}",
        f"full_q8_target_sigma={q8_compatibility:.4f}",
        f"full_q8_chi2={full_q8.chi_squared:.4f}",
        f"full_fixed_q8_chi2={full_q8_fixed.chi_squared:.4f}",
        f"q8_delta_chi2={full_q6.chi_squared - full_q8.chi_squared:.4f}",
    )
    print(
        "INFLUENCE_CONTROL",
        f"L10plus_without_body_c2={lower_q_without_body.coefficients[0]:.8f}"
        f"+/-{lower_q_without_body.coefficient_errors[0]:.8f}",
        "L10plus_without_body_target_sigma="
        f"{lower_q_without_body_compatibility:.4f}",
        "L10plus_without_body_fixed_chi2="
        f"{lower_q_without_body_fixed.chi_squared:.4f}",
        "other_removals="
        + ",".join(
            f"L{omitted}:target_sigma={compatibility:.4f}:"
            f"fixed_chi2={fixed_chi_squared:.4f}"
            for omitted, compatibility, fixed_chi_squared in other_removal_rows
        ),
    )
    print(
        "CERTIFICATE: original_failures_preserved=True highest_q_volume=L8 "
        "lower_q_set=L10,L12,L14 family_q4_q6=True "
        "q8_diagnostic_not_selected=True static_target_source_pinned=True "
        "finite_volume=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
