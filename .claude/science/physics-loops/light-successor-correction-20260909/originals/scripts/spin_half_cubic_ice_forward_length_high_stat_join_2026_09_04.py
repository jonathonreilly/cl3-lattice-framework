#!/usr/bin/env python3
"""Predeclared GLS decision for the high-statistics F=6,...,20 ladder."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.stats import f as f_distribution
from scipy.stats import t as t_distribution

from spin_half_cubic_ice_forward_length_convergence_join_2026_09_04 import (
    parse_cache as parse_first_receipt,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
REPO_ROOT = Path(__file__).resolve().parent.parent
FORWARD_LENGTHS = (6, 8, 10, 12, 14, 16, 20)
TARGET_WINDOWS = ((2, 6), (8, 14))
PLATEAU_FORWARD_LENGTHS = (12, 14, 16, 20)
OUTER_POPULATIONS = 10
PLATEAU_CONTRASTS = len(PLATEAU_FORWARD_LENGTHS) - 1
HOTELLING_95 = float(
    PLATEAU_CONTRASTS
    * (OUTER_POPULATIONS - 1)
    / (OUTER_POPULATIONS - PLATEAU_CONTRASTS)
    * f_distribution.ppf(
        0.95,
        PLATEAU_CONTRASTS,
        OUTER_POPULATIONS - PLATEAU_CONTRASTS,
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


@dataclass(frozen=True)
class ExtendedData:
    gaps: dict[tuple[int, int], np.ndarray]
    covariances: dict[tuple[int, int], np.ndarray]


@dataclass(frozen=True)
class ConstantFit:
    value: float
    error: float
    chi_squared: float
    weights: np.ndarray


@dataclass(frozen=True)
class PlateauDecision:
    fit: ConstantFit
    held_out_sigmas: dict[int, float]
    long_span_fraction: float


def parse_extended_cache() -> ExtendedData:
    path = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.txt"
    )
    text = path.read_text(encoding="utf-8")
    required = (
        "runner: scripts/spin_half_cubic_ice_forward_length_high_stat_extension_2026_09_04.py",
        "status: ok",
        "exit_code: 0",
        "TOTAL: PASS=4 FAIL=0",
    )
    if any(token not in text for token in required):
        raise RuntimeError("high-statistics forward cache is incomplete or unclean")
    gap_pattern = re.compile(
        r"^EXTENDED_FORWARD_GAPS V=0\.95 window=(?P<start>\d+)-"
        r"(?P<stop>\d+) values=(?P<values>.+)$",
        re.MULTILINE,
    )
    covariance_pattern = re.compile(
        r"^EXTENDED_FORWARD_COVARIANCE V=0\.95 "
        r"window=(?P<start>\d+)-(?P<stop>\d+) "
        r"row_major=(?P<values>[-+0-9.eE,]+)$",
        re.MULTILINE,
    )
    gaps = {}
    for match in gap_pattern.finditer(text):
        window = (int(match.group("start")), int(match.group("stop")))
        values_by_forward = {}
        for field in match.group("values").split(","):
            forward_text, value_text = field.split(":", maxsplit=1)
            values_by_forward[int(forward_text)] = float(value_text)
        if set(values_by_forward) != set(FORWARD_LENGTHS) or window in gaps:
            raise RuntimeError(f"malformed extended gap row: {window}")
        gaps[window] = np.asarray(
            [values_by_forward[value] for value in FORWARD_LENGTHS]
        )
    covariances = {}
    for match in covariance_pattern.finditer(text):
        window = (int(match.group("start")), int(match.group("stop")))
        values = np.asarray(
            [float(value) for value in match.group("values").split(",")]
        )
        if len(values) != len(FORWARD_LENGTHS) ** 2 or window in covariances:
            raise RuntimeError(f"malformed extended covariance row: {window}")
        covariances[window] = values.reshape(
            (len(FORWARD_LENGTHS), len(FORWARD_LENGTHS))
        )
    if set(gaps) != {(2, 6), (6, 12), (8, 14), (10, 16)}:
        raise RuntimeError("extended cache has the wrong window matrix")
    if set(covariances) != set(TARGET_WINDOWS):
        raise RuntimeError("extended cache has the wrong covariance matrix")
    return ExtendedData(gaps, covariances)


def constant_fit(values: np.ndarray, covariance: np.ndarray) -> ConstantFit:
    ones = np.ones(len(values))
    solved = np.linalg.solve(covariance, ones)
    normalization = float(ones @ solved)
    weights = solved / normalization
    central = float(weights @ values)
    residual = values - central
    return ConstantFit(
        value=central,
        error=float(np.sqrt(1.0 / normalization)),
        chi_squared=float(
            residual @ np.linalg.solve(covariance, residual)
        ),
        weights=weights,
    )


def plateau_decision(
    values: np.ndarray, covariance: np.ndarray
) -> PlateauDecision:
    plateau_indices = np.asarray(
        [FORWARD_LENGTHS.index(value) for value in PLATEAU_FORWARD_LENGTHS]
    )
    plateau_values = values[plateau_indices]
    plateau_covariance = covariance[
        np.ix_(plateau_indices, plateau_indices)
    ]
    fit = constant_fit(plateau_values, plateau_covariance)
    held_out_sigmas = {}
    # Fixed equal weights keep each held-out contrast predeclared rather than
    # making it depend on an estimated inverse-covariance weight vector.
    contrast_weights = np.full(
        len(plateau_indices), 1.0 / len(plateau_indices)
    )
    contrast_central = float(contrast_weights @ plateau_values)
    for forward in (6, 8, 10):
        index = FORWARD_LENGTHS.index(forward)
        cross = covariance[index, plateau_indices]
        variance = float(
            covariance[index, index]
            + contrast_weights @ plateau_covariance @ contrast_weights
            - 2.0 * cross @ contrast_weights
        )
        held_out_sigmas[forward] = abs(
            values[index] - contrast_central
        ) / max(
            np.sqrt(max(variance, 0.0)), 1.0e-15
        )
    return PlateauDecision(
        fit=fit,
        held_out_sigmas=held_out_sigmas,
        long_span_fraction=float(
            np.ptp(plateau_values) / max(abs(fit.value), 1.0e-15)
        ),
    )


def matched_excess(
    extended: ExtendedData,
    first_receipt,
    window: tuple[int, int],
) -> tuple[np.ndarray, np.ndarray]:
    detuned = extended.gaps[window]
    detuned_covariance = extended.covariances[window]
    rk_gap = first_receipt.gaps[(1.0, window)][0]
    rk_variance = first_receipt.covariances[(1.0, window)][0, 0]
    detuned_jacobian = np.diag(2.0 * detuned)
    covariance = (
        detuned_jacobian @ detuned_covariance @ detuned_jacobian
        + (2.0 * rk_gap) ** 2
        * rk_variance
        * np.ones((len(FORWARD_LENGTHS), len(FORWARD_LENGTHS)))
    )
    return detuned**2 - rk_gap**2, covariance


def main() -> int:
    checks = Checks()
    extended = parse_extended_cache()
    first = parse_first_receipt()
    checks.check(
        len(extended.gaps) == 4
        and len(extended.covariances) == 2
        and all(
            np.all(np.isfinite(values)) and np.all(values > 0.0)
            for values in extended.gaps.values()
        ),
        "the source-pinned extension supplies the complete positive gap matrix",
    )
    checks.check(
        all(
            np.allclose(covariance, covariance.T, atol=1.0e-14)
            and np.all(np.diag(covariance) > 0.0)
            and np.linalg.matrix_rank(covariance, tol=1.0e-14)
            == len(FORWARD_LENGTHS)
            for covariance in extended.covariances.values()
        ),
        "both seven-forward covariance matrices are symmetric and full rank",
    )
    raw = {
        window: plateau_decision(
            extended.gaps[window], extended.covariances[window]
        )
        for window in TARGET_WINDOWS
    }
    excess = {}
    for window in TARGET_WINDOWS:
        values, covariance = matched_excess(extended, first, window)
        excess[window] = plateau_decision(values, covariance)
    checks.check(
        all(result.fit.chi_squared < HOTELLING_95 for result in raw.values()),
        "F=12,14,16,20 pass the finite-sample Hotelling raw-gap plateau test",
    )
    checks.check(
        all(
            max(result.held_out_sigmas.values()) < STUDENT_95
            for result in raw.values()
        ),
        "each fixed earlier detuned contrast passes its finite-sample Student threshold",
    )
    checks.check(
        all(result.long_span_fraction < 0.05 for result in raw.values()),
        "each long-F raw-gap span is below five percent",
    )
    checks.check(
        all(
            result.fit.chi_squared < HOTELLING_95
            for result in excess.values()
        ),
        "the matched squared-gap excess passes the finite-sample Hotelling plateau test",
    )
    checks.check(
        all(
            max(result.held_out_sigmas.values()) < STUDENT_95
            for result in excess.values()
        ),
        "each fixed earlier excess contrast passes its finite-sample Student threshold",
    )
    checks.check(
        all(
            abs(
                extended.gaps[window][0]
                - first.gaps[(0.95, window)][2]
            )
            < 2.0
            * np.hypot(
                np.sqrt(extended.covariances[window][0, 0]),
                np.sqrt(first.covariances[(0.95, window)][2, 2]),
            )
            for window in TARGET_WINDOWS
        ),
        "the larger-population high-statistics F=6 gaps reproduce the first paired receipt",
    )
    for window in TARGET_WINDOWS:
        raw_result = raw[window]
        excess_result = excess[window]
        print(
            "HIGH_STAT_FORWARD_JOIN",
            f"window={window[0]}-{window[1]}",
            f"gap={raw_result.fit.value:.8f}+/-{raw_result.fit.error:.8f}",
            f"chi2={raw_result.fit.chi_squared:.4f}",
            "held_out_sigma="
            + ",".join(
                f"F{forward}:{raw_result.held_out_sigmas[forward]:.4f}"
                for forward in (6, 8, 10)
            ),
            f"long_span_fraction={raw_result.long_span_fraction:.6f}",
            f"Hotelling95={HOTELLING_95:.4f}",
            f"Student95={STUDENT_95:.4f}",
        )
        print(
            "HIGH_STAT_FORWARD_EXCESS",
            f"window={window[0]}-{window[1]}",
            f"squared_gap_excess={excess_result.fit.value:.8f}"
            f"+/-{excess_result.fit.error:.8f}",
            f"chi2={excess_result.fit.chi_squared:.4f}",
            "held_out_sigma="
            + ",".join(
                f"F{forward}:{excess_result.held_out_sigmas[forward]:.4f}"
                for forward in (6, 8, 10)
            ),
            f"long_span_fraction={excess_result.long_span_fraction:.6f}",
        )
    print(
        "CERTIFICATE: fixed_L=8 high_statistics=True "
        "paired_forward_lengths=6,8,10,12,14,16,20 "
        "long_forward_set=12,14,16,20 GLS_covariance=True "
        "finite_sample_calibration=True paired_RK_identity=True "
        "thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
