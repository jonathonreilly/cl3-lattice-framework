#!/usr/bin/env python3
"""Join source-pinned cubic-ice spectra to the independently measured U K.

This runner performs no stochastic evolution.  It reads the source-identity-
pinned L=8,10,12,14 late-time receipt and L=16,18 infrared receipt, then tests
the two-gradient, q^6, possible-mass, and q^8 descriptions of their common
transverse excess spectrum.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

import numpy as np

from spin_half_cubic_ice_infrared_ladder_2026_09_04 import (
    AUDIT_TIMEOUT_SEC as INFRARED_LADDER_TIMEOUT_SEC,
)
from spin_half_cubic_ice_late_time_maxwell_join_2026_09_04 import (
    LadderRow,
    WindowEstimate,
    fit_excess,
    fit_higher_gradient_excess,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt",
    "scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
REPO_ROOT = Path(__file__).resolve().parent.parent
WINDOWS = ((2, 6), (6, 12), (8, 14), (10, 16))


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
class PolynomialFit:
    powers: tuple[int, ...]
    coefficients: np.ndarray
    coefficient_errors: np.ndarray
    chi_squared: float


def parse_static_maxwell_target() -> tuple[float, float]:
    """Derive U K and its propagated error from the two parent receipts."""

    charge_text = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt"
    ).read_text(encoding="utf-8")
    magnetic_text = (
        REPO_ROOT
        / "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt"
    ).read_text(encoding="utf-8")
    charge_match = re.search(
        r"^AXIAL_FIT V=0\.95 U_charge=[0-9.]+\+/-"
        r"(?P<error>[0-9.]+) U_flux=(?P<value>[0-9.]+) ",
        charge_text,
        re.MULTILINE,
    )
    magnetic_match = re.search(
        r"^SUMMARY V=0\.95 K=(?P<value>[0-9.]+)\+/-"
        r"(?P<error>[0-9.]+) ",
        magnetic_text,
        re.MULTILINE,
    )
    if charge_match is None or magnetic_match is None:
        raise RuntimeError("static Maxwell parent receipts are incomplete")
    electric_stiffness = float(charge_match.group("value"))
    electric_stiffness_error = float(charge_match.group("error"))
    magnetic_stiffness = float(magnetic_match.group("value"))
    magnetic_stiffness_error = float(magnetic_match.group("error"))
    return (
        electric_stiffness * magnetic_stiffness,
        float(
            np.hypot(
                electric_stiffness * magnetic_stiffness_error,
                magnetic_stiffness * electric_stiffness_error,
            )
        ),
    )


def parse_ladder_cache(
    cache_name: str,
    runner_name: str,
    expected_total: str,
    expected_lengths: tuple[int, ...],
) -> tuple[list[LadderRow], list[LadderRow]]:
    cache_path = REPO_ROOT / "logs/runner-cache" / cache_name
    text = cache_path.read_text(encoding="utf-8")
    required = (
        f"runner: scripts/{runner_name}",
        "status: ok",
        "exit_code: 0",
        expected_total,
    )
    if any(token not in text for token in required):
        raise RuntimeError(f"unclean or incomplete cache: {cache_name}")

    row_pattern = re.compile(
        r"^ROW_DONE V=(?P<coupling>0\.95|1\.00) L=(?P<length>\d+) "
        r"gaps=(?P<windows>.+)$",
        re.MULTILINE,
    )
    estimate_pattern = re.compile(
        r"(?P<start>\d+)-(?P<stop>\d+):"
        r"(?P<gap>[0-9.]+)\+/-?(?P<error>[0-9.]+)"
    )
    rows: dict[str, list[LadderRow]] = {"0.95": [], "1.00": []}
    for match in row_pattern.finditer(text):
        length = int(match.group("length"))
        estimates = {}
        for estimate in estimate_pattern.finditer(match.group("windows")):
            window = (
                int(estimate.group("start")),
                int(estimate.group("stop")),
            )
            estimates[window] = WindowEstimate(
                *window,
                float(estimate.group("gap")),
                float(estimate.group("error")),
            )
        if tuple(estimates) != WINDOWS:
            raise RuntimeError(f"incomplete windows in {cache_name}, L={length}")
        coupling = match.group("coupling")
        rows[coupling].append(
            LadderRow(
                length=length,
                delta_v=-0.05 if coupling == "0.95" else 0.0,
                windows=estimates,
                mean_curve=np.ones(17, dtype=np.complex128),
                mean_energy=0.0,
                imaginary_residual=0.0,
                minimum_effective_fraction=1.0,
                minimum_origin_tau16_count=1.0e9,
                minimum_forward_count=1.0e9,
                count_consistent=True,
                sector_consistent=True,
            )
        )
    for coupling in rows:
        rows[coupling].sort(key=lambda row: row.length)
        if tuple(row.length for row in rows[coupling]) != expected_lengths:
            raise RuntimeError(
                f"wrong {coupling} length set in {cache_name}"
            )
    return rows["0.95"], rows["1.00"]


def fit_polynomial_excess(
    detuned: list[LadderRow],
    rk: list[LadderRow],
    window: tuple[int, int],
    powers: tuple[int, ...],
) -> PolynomialFit:
    rk_by_length = {row.length: row for row in rk}
    response = []
    errors = []
    momenta = []
    for row in detuned:
        reference = rk_by_length[row.length]
        detuned_gap = row.windows[window]
        rk_gap = reference.windows[window]
        response.append(detuned_gap.gap**2 - rk_gap.gap**2)
        errors.append(
            2.0
            * np.hypot(
                detuned_gap.gap * detuned_gap.gap_error,
                rk_gap.gap * rk_gap.gap_error,
            )
        )
        momenta.append(2.0 * np.sin(np.pi / row.length))
    values = np.asarray(response)
    uncertainties = np.maximum(np.asarray(errors), 1.0e-10)
    matrix = np.column_stack(
        [np.asarray(momenta) ** power for power in powers]
    )
    weights = np.diag(1.0 / uncertainties**2)
    covariance = np.linalg.inv(matrix.T @ weights @ matrix)
    coefficients = covariance @ (matrix.T @ weights @ values)
    residual = (values - matrix @ coefficients) / uncertainties
    return PolynomialFit(
        powers=powers,
        coefficients=coefficients,
        coefficient_errors=np.sqrt(np.diag(covariance)),
        chi_squared=float(np.dot(residual, residual)),
    )


def fit_polynomial_spectrum(
    rows: list[LadderRow],
    window: tuple[int, int],
    powers: tuple[int, ...],
) -> PolynomialFit:
    """Fit one squared-gap ladder without importing the RK subtraction."""

    values = []
    uncertainties = []
    momenta = []
    for row in rows:
        estimate = row.windows[window]
        values.append(estimate.gap**2)
        uncertainties.append(2.0 * estimate.gap * estimate.gap_error)
        momenta.append(2.0 * np.sin(np.pi / row.length))
    response = np.asarray(values)
    errors = np.maximum(np.asarray(uncertainties), 1.0e-10)
    matrix = np.column_stack(
        [np.asarray(momenta) ** power for power in powers]
    )
    weights = np.diag(1.0 / errors**2)
    covariance = np.linalg.inv(matrix.T @ weights @ matrix)
    coefficients = covariance @ (matrix.T @ weights @ response)
    residual = (response - matrix @ coefficients) / errors
    return PolynomialFit(
        powers=powers,
        coefficients=coefficients,
        coefficient_errors=np.sqrt(np.diag(covariance)),
        chi_squared=float(np.dot(residual, residual)),
    )


def main() -> int:
    checks = Checks()
    parent_detuned, parent_rk = parse_ladder_cache(
        "spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
        "spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
        "TOTAL: PASS=11 FAIL=0",
        (8, 10, 12, 14),
    )
    infrared_detuned, infrared_rk = parse_ladder_cache(
        "spin_half_cubic_ice_infrared_ladder_2026_09_04.txt",
        "spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
        "TOTAL: PASS=3 FAIL=0",
        (16, 18),
    )
    detuned = parent_detuned + infrared_detuned
    rk = parent_rk + infrared_rk
    checks.check(
        [row.length for row in detuned] == [8, 10, 12, 14, 16, 18]
        and [row.length for row in rk] == [8, 10, 12, 14, 16, 18],
        "the two source-pinned receipts join into matched six-volume ladders",
    )
    checks.check(
        INFRARED_LADDER_TIMEOUT_SEC == 21600,
        "the imported infrared helper is the declared long-run source",
    )

    maxwell_c_squared, maxwell_c_squared_error = (
        parse_static_maxwell_target()
    )
    two_term_fits = {
        window: fit_excess(detuned, rk, window, maxwell_c_squared)
        for window in WINDOWS
    }
    higher_fits = {
        window: fit_higher_gradient_excess(
            detuned,
            rk,
            window,
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        for window in WINDOWS
    }
    mass_fits = {
        window: fit_polynomial_excess(
            detuned, rk, window, (0, 2, 4, 6)
        )
        for window in WINDOWS
    }
    q8_fits = {
        window: fit_polynomial_excess(
            detuned, rk, window, (2, 4, 6, 8)
        )
        for window in WINDOWS
    }
    direct_detuned_fits = {
        window: fit_polynomial_spectrum(detuned, window, (2, 4, 6))
        for window in WINDOWS
    }
    direct_rk_fits = {
        window: fit_polynomial_spectrum(rk, window, (2, 4, 6))
        for window in WINDOWS
    }
    lower_q_subset_higher = {
        window: fit_higher_gradient_excess(
            detuned[2:],
            rk[2:],
            window,
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        for window in WINDOWS
    }
    without_l18_higher = {
        window: fit_higher_gradient_excess(
            detuned[:-1],
            rk[:-1],
            window,
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        for window in WINDOWS
    }
    without_l16_higher = {
        window: fit_higher_gradient_excess(
            detuned[:4] + detuned[5:],
            rk[:4] + rk[5:],
            window,
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        for window in WINDOWS
    }
    all_scalar_values = []
    for window in WINDOWS:
        for fit in (
            two_term_fits[window],
            higher_fits[window],
            mass_fits[window],
            q8_fits[window],
            direct_detuned_fits[window],
            direct_rk_fits[window],
            lower_q_subset_higher[window],
            without_l18_higher[window],
            without_l16_higher[window],
        ):
            for value in vars(fit).values():
                if isinstance(value, (int, float, np.integer, np.floating)):
                    all_scalar_values.append(float(value))
                elif isinstance(value, np.ndarray):
                    all_scalar_values.extend(
                        np.asarray(value, dtype=float).ravel().tolist()
                    )
    checks.check(
        all(np.isfinite(all_scalar_values)),
        "every declared infrared fit is finite",
    )

    # These result thresholds were fixed before the production receipt was
    # inspected.  The early and primary-late windows are the two target
    # windows; the other two remain reported as non-selected controls.
    target_windows = ((2, 6), (8, 14))

    def compatible(
        first_value: float,
        first_error: float,
        second_value: float,
        second_error: float,
        threshold: float = 2.0,
    ) -> bool:
        return abs(first_value - second_value) < threshold * np.hypot(
            first_error, second_error
        )

    checks.check(
        all(higher_fits[window].c_squared > 0.0 for window in target_windows),
        "both target-window q-sixth fits retain a positive infrared coefficient",
    )
    checks.check(
        all(
            compatible(
                higher_fits[window].c_squared,
                higher_fits[window].c_squared_error,
                maxwell_c_squared,
                maxwell_c_squared_error,
            )
            for window in target_windows
        ),
        "both target-window infrared coefficients are compatible with independent U K",
    )
    checks.check(
        all(
            higher_fits[window].fixed_chi_squared < 9.488
            and higher_fits[window].fixed_delta_chi_squared < 3.841
            for window in target_windows
        ),
        "fixed central U K plus q-fourth and q-sixth passes the nominal four-dof fit and one-parameter penalty tests",
    )
    checks.check(
        all(
            abs(mass_fits[window].coefficients[0])
            < 2.0 * mass_fits[window].coefficient_errors[0]
            and higher_fits[window].chi_squared
            - mass_fits[window].chi_squared
            < 3.841
            for window in target_windows
        ),
        "a constant squared-mass term is unresolved and does not significantly improve either target fit",
    )
    checks.check(
        all(
            higher_fits[window].chi_squared - q8_fits[window].chi_squared
            < 3.841
            and compatible(
                q8_fits[window].coefficients[0],
                q8_fits[window].coefficient_errors[0],
                higher_fits[window].c_squared,
                higher_fits[window].c_squared_error,
            )
            for window in target_windows
        ),
        "a q-eighth extension neither significantly improves nor destabilizes the infrared coefficient",
    )
    checks.check(
        all(
            compatible(
                lower_q_subset_higher[window].c_squared,
                lower_q_subset_higher[window].c_squared_error,
                higher_fits[window].c_squared,
                higher_fits[window].c_squared_error,
            )
            and compatible(
                without_l18_higher[window].c_squared,
                without_l18_higher[window].c_squared_error,
                higher_fits[window].c_squared,
                higher_fits[window].c_squared_error,
            )
            and compatible(
                without_l16_higher[window].c_squared,
                without_l16_higher[window].c_squared_error,
                higher_fits[window].c_squared,
                higher_fits[window].c_squared_error,
            )
            for window in target_windows
        ),
        "the coefficient survives the lower-q subset and either infrared volume removal",
    )
    checks.check(
        all(
            direct_detuned_fits[window].coefficients[0] > 0.0
            and compatible(
                direct_detuned_fits[window].coefficients[0],
                direct_detuned_fits[window].coefficient_errors[0],
                maxwell_c_squared,
                maxwell_c_squared_error,
            )
            and abs(direct_rk_fits[window].coefficients[0])
            < 2.0 * direct_rk_fits[window].coefficient_errors[0]
            and direct_detuned_fits[window].chi_squared < 7.815
            and direct_rk_fits[window].chi_squared < 7.815
            for window in target_windows
        ),
        "direct detuned spectra carry U K-compatible q-squared weight while the RK control does not",
    )
    checks.check(
        compatible(
            higher_fits[(2, 6)].c_squared,
            higher_fits[(2, 6)].c_squared_error,
            higher_fits[(8, 14)].c_squared,
            higher_fits[(8, 14)].c_squared_error,
        ),
        "the early and primary-late infrared coefficients are compatible",
    )

    for window in WINDOWS:
        two = two_term_fits[window]
        higher = higher_fits[window]
        subset = lower_q_subset_higher[window]
        without_l18 = without_l18_higher[window]
        without_l16 = without_l16_higher[window]
        print(
            "INFRARED_JOIN",
            f"window={window[0]}-{window[1]}",
            f"two_c2={two.c_squared:.8f}+/-{two.c_squared_error:.8f}",
            f"two_chi2={two.chi_squared:.4f}",
            f"q6_c2={higher.c_squared:.8f}"
            f"+/-{higher.c_squared_error:.8f}",
            f"q6_chi2={higher.chi_squared:.4f}",
            f"fixed_UK_chi2={higher.fixed_chi_squared:.4f}",
            f"fixed_delta_chi2={higher.fixed_delta_chi_squared:.4f}",
            f"L12plus_c2={subset.c_squared:.8f}"
            f"+/-{subset.c_squared_error:.8f}",
            f"without_L18_c2={without_l18.c_squared:.8f}"
            f"+/-{without_l18.c_squared_error:.8f}",
            f"without_L16_c2={without_l16.c_squared:.8f}"
            f"+/-{without_l16.c_squared_error:.8f}",
        )
        direct = direct_detuned_fits[window]
        direct_rk = direct_rk_fits[window]
        print(
            "DIRECT_SPECTRUM",
            f"window={window[0]}-{window[1]}",
            f"detuned_c2={direct.coefficients[0]:.8f}"
            f"+/-{direct.coefficient_errors[0]:.8f}",
            f"detuned_chi2={direct.chi_squared:.4f}",
            f"RK_c2={direct_rk.coefficients[0]:.8f}"
            f"+/-{direct_rk.coefficient_errors[0]:.8f}",
            f"RK_chi2={direct_rk.chi_squared:.4f}",
        )
    for window in ((2, 6), (8, 14)):
        mass = mass_fits[window]
        q8 = q8_fits[window]
        print(
            "MODEL_EXTENSION",
            f"window={window[0]}-{window[1]}",
            f"mass2={mass.coefficients[0]:.8f}"
            f"+/-{mass.coefficient_errors[0]:.8f}",
            f"mass_c2={mass.coefficients[1]:.8f}"
            f"+/-{mass.coefficient_errors[1]:.8f}",
            f"mass_chi2={mass.chi_squared:.4f}",
            f"mass_delta_chi2="
            f"{higher_fits[window].chi_squared - mass.chi_squared:.4f}",
            f"q8_c2={q8.coefficients[0]:.8f}"
            f"+/-{q8.coefficient_errors[0]:.8f}",
            f"q8={q8.coefficients[3]:.8f}"
            f"+/-{q8.coefficient_errors[3]:.8f}",
            f"q8_chi2={q8.chi_squared:.4f}",
            f"q8_delta_chi2="
            f"{higher_fits[window].chi_squared - q8.chi_squared:.4f}",
        )
    print(
        "MAXWELL_TARGET",
        f"UK={maxwell_c_squared:.8f}+/-{maxwell_c_squared_error:.8f}",
    )
    print(
        "CERTIFICATE: parent_receipts_source_pinned=True "
        "new_lower_momenta=L16,L18 mass_control=True q8_control=True "
        "static_target_source_pinned=True "
        "finite_volume=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
