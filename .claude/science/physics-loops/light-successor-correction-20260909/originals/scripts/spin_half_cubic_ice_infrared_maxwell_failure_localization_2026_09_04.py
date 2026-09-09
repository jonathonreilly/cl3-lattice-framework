#!/usr/bin/env python3
"""Post-result localization of the conditional infrared join failure.

This runner makes no acceptance decision and performs no stochastic work.  It
reports time-window, model-order, and leave-one-volume-out diagnostics for the
RK direct-spectrum control that failed in the conditional Maxwell join.
"""

from __future__ import annotations

import numpy as np

import spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04 as health
import spin_half_cubic_ice_infrared_maxwell_join_2026_09_04 as joined


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_health_reanalysis_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300


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


def main() -> int:
    checks = Checks()
    joined.parse_ladder_cache = health.parse_classified_ladder_cache
    _, parent_rk = joined.parse_ladder_cache(
        "spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
        "spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
        "TOTAL: PASS=11 FAIL=0",
        (8, 10, 12, 14),
    )
    _, infrared_rk = joined.parse_ladder_cache(
        "spin_half_cubic_ice_infrared_ladder_2026_09_04.txt",
        "spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
        "TOTAL: PASS=3 FAIL=0",
        (16, 18),
    )
    rk = parent_rk + infrared_rk
    checks.check(
        [row.length for row in rk] == [8, 10, 12, 14, 16, 18],
        "the classified RK receipt supplies the complete six-volume ladder",
    )

    scalars: list[float] = []
    leave_one_out_count = 0
    for window in joined.WINDOWS:
        base = joined.fit_polynomial_spectrum(rk, window, (2, 4, 6))
        fixed = joined.fit_polynomial_spectrum(rk, window, (4, 6))
        q8 = joined.fit_polynomial_spectrum(rk, window, (2, 4, 6, 8))
        fixed_q8 = joined.fit_polynomial_spectrum(rk, window, (4, 6, 8))
        base_z = base.coefficients[0] / base.coefficient_errors[0]
        q8_z = q8.coefficients[0] / q8.coefficient_errors[0]
        scalars.extend(
            (
                base.coefficients[0],
                base.coefficient_errors[0],
                base_z,
                base.chi_squared,
                fixed.chi_squared - base.chi_squared,
                q8.coefficients[0],
                q8.coefficient_errors[0],
                q8_z,
                q8.chi_squared,
                fixed_q8.chi_squared - q8.chi_squared,
            )
        )
        print(
            "RK_WINDOW_LOCALIZATION",
            f"window={window[0]}-{window[1]}",
            f"q6_c2={base.coefficients[0]:.8f}"
            f"+/-{base.coefficient_errors[0]:.8f}",
            f"q6_z={base_z:.4f}",
            f"q6_chi2={base.chi_squared:.4f}",
            f"zero_c2_delta_chi2={fixed.chi_squared - base.chi_squared:.4f}",
            f"q8_c2={q8.coefficients[0]:.8f}"
            f"+/-{q8.coefficient_errors[0]:.8f}",
            f"q8_z={q8_z:.4f}",
            f"q8_chi2={q8.chi_squared:.4f}",
            f"q8_zero_c2_delta_chi2="
            f"{fixed_q8.chi_squared - q8.chi_squared:.4f}",
        )

    early_window = (2, 6)
    for index, removed in enumerate(rk):
        subset = rk[:index] + rk[index + 1 :]
        fit = joined.fit_polynomial_spectrum(subset, early_window, (2, 4, 6))
        z_score = fit.coefficients[0] / fit.coefficient_errors[0]
        scalars.extend(
            (
                fit.coefficients[0],
                fit.coefficient_errors[0],
                z_score,
                fit.chi_squared,
            )
        )
        leave_one_out_count += 1
        print(
            "RK_EARLY_LEAVE_ONE_OUT",
            f"removed_L={removed.length}",
            f"c2={fit.coefficients[0]:.8f}"
            f"+/-{fit.coefficient_errors[0]:.8f}",
            f"z={z_score:.4f}",
            f"chi2={fit.chi_squared:.4f}",
        )

    checks.check(
        len(joined.WINDOWS) == 4 and leave_one_out_count == 6,
        "all four windows and all six early-window volume removals are reported",
    )
    checks.check(
        all(np.isfinite(value) for value in scalars),
        "every post-result localization diagnostic is finite",
    )
    print(
        "CERTIFICATE: post_result_localization=True stochastic_work=False "
        "acceptance_thresholds=False thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
