#!/usr/bin/env python3
"""Finite-sample reanalysis of the preserved paired-F failed receipt.

The first cheap join used asymptotic chi-squared and normal thresholds while
its covariance came from only six outer populations.  This runner preserves
that failure and applies the corresponding Hotelling/F and Student-t
calibrations without changing a datum, window, forward length, or covariance.
"""

from __future__ import annotations

import numpy as np
from scipy.stats import f as f_distribution
from scipy.stats import t as t_distribution

from spin_half_cubic_ice_forward_length_convergence_join_2026_09_04 import (
    FORWARD_LENGTHS,
    TARGET_WINDOWS,
    covariance_is_usable,
    excess_data,
    gls_constant,
    parse_cache,
    rk_forward_identity_is_exact,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_forward_length_convergence_join_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
OUTER_POPULATIONS = 6
LONG_FORWARD_LENGTHS = (8, 10, 12)
LONG_INDICES = np.asarray(
    [FORWARD_LENGTHS.index(value) for value in LONG_FORWARD_LENGTHS]
)
F6_INDEX = FORWARD_LENGTHS.index(6)
CONTRAST_DIMENSION = len(LONG_FORWARD_LENGTHS) - 1
HOTELLING_95 = float(
    CONTRAST_DIMENSION
    * (OUTER_POPULATIONS - 1)
    / (OUTER_POPULATIONS - CONTRAST_DIMENSION)
    * f_distribution.ppf(
        0.95,
        CONTRAST_DIMENSION,
        OUTER_POPULATIONS - CONTRAST_DIMENSION,
    )
)
STUDENT_95 = float(t_distribution.ppf(0.975, OUTER_POPULATIONS - 1))


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


def fixed_f6_contrast(
    values: np.ndarray, covariance: np.ndarray
) -> tuple[float, float, float]:
    weights = np.full(len(LONG_INDICES), 1.0 / len(LONG_INDICES))
    long_mean = float(weights @ values[LONG_INDICES])
    cross = covariance[F6_INDEX, LONG_INDICES]
    long_covariance = covariance[np.ix_(LONG_INDICES, LONG_INDICES)]
    variance = float(
        covariance[F6_INDEX, F6_INDEX]
        + weights @ long_covariance @ weights
        - 2.0 * cross @ weights
    )
    difference = float(values[F6_INDEX] - long_mean)
    error = float(np.sqrt(max(variance, 0.0)))
    return difference, error, abs(difference) / max(error, 1.0e-15)


def main() -> int:
    checks = Checks()
    data = parse_cache()
    checks.check(
        len(data.gaps) == 8 and len(data.covariances) == 4,
        "the preserved nonzero-exit receipt supplies its complete data matrix",
    )
    checks.check(
        all(
            covariance_is_usable(data.covariances[(0.95, window)])
            for window in TARGET_WINDOWS
        )
        and all(
            rk_forward_identity_is_exact(
                data.gaps[(1.0, window)],
                data.covariances[(1.0, window)],
            )
            for window in TARGET_WINDOWS
        ),
        "the detuned covariance is usable and the RK rank-one identity is exact",
    )
    raw_fits = {}
    raw_contrasts = {}
    excess_fits = {}
    excess_contrasts = {}
    for window in TARGET_WINDOWS:
        raw_values = data.gaps[(0.95, window)]
        raw_covariance = data.covariances[(0.95, window)]
        raw_fits[window] = gls_constant(
            raw_values[LONG_INDICES],
            raw_covariance[np.ix_(LONG_INDICES, LONG_INDICES)],
        )
        raw_contrasts[window] = fixed_f6_contrast(
            raw_values, raw_covariance
        )
        values, covariance = excess_data(data, window)
        excess_fits[window] = gls_constant(
            values[LONG_INDICES],
            covariance[np.ix_(LONG_INDICES, LONG_INDICES)],
        )
        excess_contrasts[window] = fixed_f6_contrast(values, covariance)
    checks.check(
        all(fit.chi_squared < HOTELLING_95 for fit in raw_fits.values()),
        "both raw long-F ladders pass the finite-sample Hotelling threshold",
    )
    checks.check(
        all(row[2] < STUDENT_95 for row in raw_contrasts.values()),
        "both fixed F=6 raw contrasts pass the finite-sample Student threshold",
    )
    checks.check(
        all(fit.chi_squared < HOTELLING_95 for fit in excess_fits.values()),
        "both excess long-F ladders pass the finite-sample Hotelling threshold",
    )
    checks.check(
        all(row[2] < STUDENT_95 for row in excess_contrasts.values()),
        "both fixed F=6 excess contrasts pass the finite-sample Student threshold",
    )
    checks.check(
        HOTELLING_95 > 5.991 and STUDENT_95 > 1.96,
        "finite-sample thresholds are strictly wider than the failed asymptotic thresholds",
    )
    for window in TARGET_WINDOWS:
        raw_fit = raw_fits[window]
        raw_difference, raw_error, raw_sigma = raw_contrasts[window]
        excess_fit = excess_fits[window]
        excess_difference, excess_error, excess_sigma = excess_contrasts[window]
        print(
            "FINITE_SAMPLE_FORWARD",
            f"window={window[0]}-{window[1]}",
            f"gap={raw_fit.value:.8f}+/-{raw_fit.error:.8f}",
            f"Hotelling_stat={raw_fit.chi_squared:.4f}",
            f"Hotelling95={HOTELLING_95:.4f}",
            f"F6_equal_mean_delta={raw_difference:.8f}+/-{raw_error:.8f}",
            f"Student_stat={raw_sigma:.4f}",
            f"Student95={STUDENT_95:.4f}",
        )
        print(
            "FINITE_SAMPLE_FORWARD_EXCESS",
            f"window={window[0]}-{window[1]}",
            f"squared_gap_excess={excess_fit.value:.8f}"
            f"+/-{excess_fit.error:.8f}",
            f"Hotelling_stat={excess_fit.chi_squared:.4f}",
            f"F6_equal_mean_delta={excess_difference:.8f}"
            f"+/-{excess_error:.8f}",
            f"Student_stat={excess_sigma:.4f}",
        )
    print(
        "CERTIFICATE: original_failed_receipts_preserved=True "
        "outer_populations=6 covariance_estimated=True "
        "Hotelling_F_calibration=True fixed_contrast_Student_t=True "
        "fixed_L=8 thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
