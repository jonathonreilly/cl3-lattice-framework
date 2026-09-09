#!/usr/bin/env python3
"""Covariance-aware convergence test for the paired forward-length ladder.

No stochastic evolution occurs here.  The runner reads the immutable paired-F
receipt, fits F=8,10,12 to a common plateau with the measured covariance, and
tests the held-out F=6 contrast.  It repeats the test after subtracting the
matched RK squared gap, propagating both coupling covariances by the delta
method.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
REPO_ROOT = Path(__file__).resolve().parent.parent
FORWARD_LENGTHS = (2, 4, 6, 8, 10, 12)
WINDOWS = ((2, 6), (6, 12), (8, 14), (10, 16))
TARGET_WINDOWS = ((2, 6), (8, 14))
LONG_INDICES = np.asarray(
    [FORWARD_LENGTHS.index(value) for value in (8, 10, 12)], dtype=int
)
F6_INDEX = FORWARD_LENGTHS.index(6)


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
class ForwardData:
    gaps: dict[tuple[float, tuple[int, int]], np.ndarray]
    covariances: dict[tuple[float, tuple[int, int]], np.ndarray]


@dataclass(frozen=True)
class ConstantFit:
    value: float
    error: float
    chi_squared: float
    weights: np.ndarray


@dataclass(frozen=True)
class PlateauResult:
    fit: ConstantFit
    f6_difference: float
    f6_error: float
    f6_sigma: float
    long_span_fraction: float


def parse_cache() -> ForwardData:
    path = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_forward_length_ladder_2026_09_04.txt"
    )
    text = path.read_text(encoding="utf-8")
    required = (
        "runner: scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py",
        "status: nonzero_exit",
        "exit_code: 1",
        "TOTAL: PASS=3 FAIL=1",
    )
    if any(token not in text for token in required):
        raise RuntimeError("forward-length cache is incomplete or unclean")
    gap_pattern = re.compile(
        r"^FORWARD_GAPS V=(?P<coupling>0\.95|1\.00) "
        r"window=(?P<start>\d+)-(?P<stop>\d+) values=(?P<values>.+)$",
        re.MULTILINE,
    )
    covariance_pattern = re.compile(
        r"^FORWARD_COVARIANCE V=(?P<coupling>0\.95|1\.00) "
        r"window=(?P<start>\d+)-(?P<stop>\d+) "
        r"row_major=(?P<values>.+)$",
        re.MULTILINE,
    )
    gaps: dict[tuple[float, tuple[int, int]], np.ndarray] = {}
    for match in gap_pattern.finditer(text):
        key = (
            float(match.group("coupling")),
            (int(match.group("start")), int(match.group("stop"))),
        )
        if key in gaps:
            raise RuntimeError(f"duplicate forward gap row: {key}")
        values_by_forward = {}
        for field in match.group("values").split(","):
            forward_text, value_text = field.split(":", maxsplit=1)
            values_by_forward[int(forward_text)] = float(value_text)
        if set(values_by_forward) != set(FORWARD_LENGTHS):
            raise RuntimeError(f"wrong forward-length set: {key}")
        gaps[key] = np.asarray(
            [values_by_forward[value] for value in FORWARD_LENGTHS]
        )
    expected_gaps = {
        (coupling, window)
        for coupling in (0.95, 1.0)
        for window in WINDOWS
    }
    if set(gaps) != expected_gaps:
        raise RuntimeError("forward cache has the wrong gap matrix")
    covariances: dict[tuple[float, tuple[int, int]], np.ndarray] = {}
    for match in covariance_pattern.finditer(text):
        key = (
            float(match.group("coupling")),
            (int(match.group("start")), int(match.group("stop"))),
        )
        if key in covariances:
            raise RuntimeError(f"duplicate forward covariance row: {key}")
        values = np.asarray(
            [float(value) for value in match.group("values").split(",")]
        )
        if len(values) != len(FORWARD_LENGTHS) ** 2:
            raise RuntimeError(f"wrong covariance shape: {key}")
        covariances[key] = values.reshape(
            (len(FORWARD_LENGTHS), len(FORWARD_LENGTHS))
        )
    expected_covariances = {
        (coupling, window)
        for coupling in (0.95, 1.0)
        for window in TARGET_WINDOWS
    }
    if set(covariances) != expected_covariances:
        raise RuntimeError("forward cache has the wrong covariance matrix")
    return ForwardData(gaps, covariances)


def gls_constant(values: np.ndarray, covariance: np.ndarray) -> ConstantFit:
    ones = np.ones(len(values))
    solved_ones = np.linalg.solve(covariance, ones)
    normalization = float(ones @ solved_ones)
    weights = solved_ones / normalization
    value = float(weights @ values)
    residual = values - value
    error = float(np.sqrt(1.0 / normalization))
    chi_squared = float(residual @ np.linalg.solve(covariance, residual))
    return ConstantFit(value, error, chi_squared, weights)


def plateau_result(values: np.ndarray, covariance: np.ndarray) -> PlateauResult:
    long_values = values[LONG_INDICES]
    long_covariance = covariance[np.ix_(LONG_INDICES, LONG_INDICES)]
    fit = gls_constant(long_values, long_covariance)
    cross = covariance[F6_INDEX, LONG_INDICES]
    difference = float(values[F6_INDEX] - fit.value)
    variance = float(
        covariance[F6_INDEX, F6_INDEX]
        + fit.weights @ long_covariance @ fit.weights
        - 2.0 * cross @ fit.weights
    )
    error = float(np.sqrt(max(variance, 0.0)))
    sigma = abs(difference) / max(error, 1.0e-15)
    span = float(np.ptp(long_values) / max(abs(fit.value), 1.0e-15))
    return PlateauResult(fit, difference, error, sigma, span)


def excess_data(data: ForwardData, window: tuple[int, int]) -> tuple[np.ndarray, np.ndarray]:
    detuned = data.gaps[(0.95, window)]
    rk = data.gaps[(1.0, window)]
    detuned_jacobian = np.diag(2.0 * detuned)
    rk_jacobian = np.diag(2.0 * rk)
    covariance = (
        detuned_jacobian
        @ data.covariances[(0.95, window)]
        @ detuned_jacobian
        + rk_jacobian
        @ data.covariances[(1.0, window)]
        @ rk_jacobian
    )
    return detuned**2 - rk**2, covariance


def covariance_is_usable(covariance: np.ndarray) -> bool:
    if not np.all(np.isfinite(covariance)):
        return False
    if not np.allclose(covariance, covariance.T, rtol=1.0e-8, atol=1.0e-14):
        return False
    if not np.all(np.diag(covariance) > 0.0):
        return False
    for indices in (LONG_INDICES, np.asarray([F6_INDEX, *LONG_INDICES])):
        submatrix = covariance[np.ix_(indices, indices)]
        if np.linalg.matrix_rank(submatrix, tol=1.0e-14) != len(indices):
            return False
        if np.min(np.linalg.eigvalsh(submatrix)) <= 0.0:
            return False
    return True


def rk_forward_identity_is_exact(
    values: np.ndarray, covariance: np.ndarray
) -> bool:
    """At delta V=0 uniform projector weights make F exactly irrelevant."""

    return (
        np.all(values == values[0])
        and np.all(covariance == covariance[0, 0])
        and covariance[0, 0] > 0.0
        and np.linalg.matrix_rank(covariance, tol=1.0e-14) == 1
    )


def main() -> int:
    checks = Checks()
    data = parse_cache()
    checks.check(
        len(data.gaps) == 8
        and len(data.covariances) == 4
        and all(
            np.all(np.isfinite(values)) and np.all(values > 0.0)
            for values in data.gaps.values()
        ),
        "the source-pinned receipt supplies the complete positive gap matrix",
    )
    checks.check(
        all(
            covariance_is_usable(data.covariances[(0.95, window)])
            for window in TARGET_WINDOWS
        ),
        "the detuned paired-F covariance blocks are symmetric and usable for GLS",
    )
    checks.check(
        all(
            rk_forward_identity_is_exact(
                data.gaps[(1.0, window)],
                data.covariances[(1.0, window)],
            )
            for window in TARGET_WINDOWS
        ),
        "uniform RK projector weights make every forward length exactly identical",
    )
    raw_results = {
        (coupling, window): plateau_result(
            data.gaps[(coupling, window)], data.covariances[(coupling, window)]
        )
        for coupling in (0.95,)
        for window in TARGET_WINDOWS
    }
    checks.check(
        all(result.fit.chi_squared < 5.991 for result in raw_results.values()),
        "detuned F=8,10,12 pass the nominal two-dof raw-gap plateau test",
    )
    checks.check(
        all(result.f6_sigma < 1.96 for result in raw_results.values()),
        "the paired detuned F=6 gaps are compatible with the long-F plateaus",
    )
    checks.check(
        all(result.long_span_fraction < 0.05 for result in raw_results.values()),
        "each detuned long-F raw-gap span is below five percent",
    )
    excess_results = {}
    for window in TARGET_WINDOWS:
        values, covariance = excess_data(data, window)
        excess_results[window] = plateau_result(values, covariance)
    checks.check(
        all(result.fit.chi_squared < 5.991 for result in excess_results.values()),
        "the matched squared-gap excess passes the nominal long-F plateau test",
    )
    checks.check(
        all(result.f6_sigma < 1.96 for result in excess_results.values()),
        "the paired F=6 excess is compatible with each long-F plateau",
    )
    for coupling in (0.95,):
        for window in TARGET_WINDOWS:
            result = raw_results[(coupling, window)]
            print(
                "FORWARD_PLATEAU",
                f"V={coupling:.2f}",
                f"window={window[0]}-{window[1]}",
                f"gap={result.fit.value:.8f}+/-{result.fit.error:.8f}",
                f"chi2={result.fit.chi_squared:.4f}",
                f"F6_delta={result.f6_difference:.8f}+/-{result.f6_error:.8f}",
                f"F6_sigma={result.f6_sigma:.4f}",
                f"long_span_fraction={result.long_span_fraction:.6f}",
            )
    for window in TARGET_WINDOWS:
        print(
            "RK_FORWARD_IDENTITY",
            f"window={window[0]}-{window[1]}",
            f"gap={data.gaps[(1.0, window)][0]:.8f}",
            "all_forward_lengths_exactly_equal=True covariance_rank=1",
        )
    for window in TARGET_WINDOWS:
        result = excess_results[window]
        print(
            "FORWARD_EXCESS_PLATEAU",
            f"window={window[0]}-{window[1]}",
            f"squared_gap_excess={result.fit.value:.8f}+/-{result.fit.error:.8f}",
            f"chi2={result.fit.chi_squared:.4f}",
            f"F6_delta={result.f6_difference:.8f}+/-{result.f6_error:.8f}",
            f"F6_sigma={result.f6_sigma:.4f}",
            f"long_span_fraction={result.long_span_fraction:.6f}",
        )
    print(
        "CERTIFICATE: fixed_L=8 paired_forward_lengths=2,4,6,8,10,12 "
        "failed_rank_gate_preserved=True GLS_covariance=True "
        "RK_forward_identity=True long_forward_set=8,10,12 "
        "paired_RK_excess=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
