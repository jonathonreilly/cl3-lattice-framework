#!/usr/bin/env python3
"""Predeclared decision surface for the high-genealogy infrared replay."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
import sys

import numpy as np

from spin_half_cubic_ice_infrared_forward_replay_2026_09_04 import (
    FORWARD_LENGTHS,
    PRIMARY_WINDOW,
    WINDOWS,
)
from spin_half_cubic_ice_infrared_maxwell_join_2026_09_04 import (
    fit_polynomial_excess,
    fit_polynomial_spectrum,
    parse_ladder_cache,
    parse_static_maxwell_target,
)
from spin_half_cubic_ice_late_time_maxwell_join_2026_09_04 import (
    LadderRow,
    WindowEstimate,
    fit_higher_gradient_excess,
)


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py",
    "logs/runner-cache/"
    "spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt",
    "scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_CACHE = (
    REPO_ROOT
    / "logs/runner-cache/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.txt"
)
OLD_CACHE = (
    REPO_ROOT
    / "logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt"
)
HOTELLING_LIMIT = 17.361
STUDENT_LIMIT = 2.571


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
class PairedEstimate:
    gaps: np.ndarray
    errors: np.ndarray
    covariance: np.ndarray


@dataclass(frozen=True)
class ForwardControl:
    hotelling: float
    maximum_contrast: float
    relative_span: float


def parse_rows(text: str) -> dict[tuple[float, int, tuple[int, int]], PairedEstimate]:
    row_pattern = re.compile(
        r"^PAIRED_ROW V=(?P<coupling>0\.95|1\.00) "
        r"L=(?P<length>16|18) window=(?P<start>2|8)-(?P<stop>6|14) "
        r"gaps=(?P<gaps>\S+) cov=(?P<cov>\S+)$",
        re.MULTILINE,
    )
    gap_pattern = re.compile(
        r"(?P<forward>6|12|20):(?P<gap>[0-9.]+)"
        r"\+/-?(?P<error>[0-9.]+)"
    )
    rows = {}
    for match in row_pattern.finditer(text):
        parsed = {
            int(item.group("forward")): (
                float(item.group("gap")),
                float(item.group("error")),
            )
            for item in gap_pattern.finditer(match.group("gaps"))
        }
        if tuple(parsed) != FORWARD_LENGTHS:
            raise RuntimeError("paired-forward row has the wrong endpoint set")
        covariance_values = np.asarray(
            [float(value) for value in match.group("cov").split(",")]
        )
        if len(covariance_values) != len(FORWARD_LENGTHS) ** 2:
            raise RuntimeError("paired-forward covariance has the wrong size")
        key = (
            float(match.group("coupling")),
            int(match.group("length")),
            (int(match.group("start")), int(match.group("stop"))),
        )
        rows[key] = PairedEstimate(
            gaps=np.asarray([parsed[value][0] for value in FORWARD_LENGTHS]),
            errors=np.asarray([parsed[value][1] for value in FORWARD_LENGTHS]),
            covariance=covariance_values.reshape(
                (len(FORWARD_LENGTHS), len(FORWARD_LENGTHS))
            ),
        )
    expected = {
        (coupling, length, window)
        for coupling in (0.95, 1.0)
        for length in (16, 18)
        for window in WINDOWS
    }
    if set(rows) != expected:
        raise RuntimeError("paired-forward receipt is incomplete")
    return rows


def parse_replay(
    *, allow_nonzero: bool = False
) -> dict[tuple[float, int, tuple[int, int]], PairedEstimate]:
    text = DATA_CACHE.read_text(encoding="utf-8")
    identity_required = (
        "runner: scripts/spin_half_cubic_ice_infrared_forward_replay_2026_09_04.py",
        "primary_window=8-14",
    )
    if any(token not in text for token in identity_required):
        raise RuntimeError("high-genealogy replay receipt is incomplete")
    green_required = (
        "status: ok",
        "exit_code: 0",
        "TOTAL: PASS=4 FAIL=0",
    )
    if not allow_nonzero and any(token not in text for token in green_required):
        raise RuntimeError("high-genealogy replay receipt is not green")
    return parse_rows(text)


def replay_receipt_is_green() -> bool:
    """Return the upstream replay status without changing strict parsing."""
    text = DATA_CACHE.read_text(encoding="utf-8")
    return all(
        token in text
        for token in (
            "status: ok",
            "exit_code: 0",
            "TOTAL: PASS=4 FAIL=0",
        )
    )


def parse_old_rows() -> dict[tuple[float, int, tuple[int, int]], WindowEstimate]:
    text = OLD_CACHE.read_text(encoding="utf-8")
    required = (
        "runner: scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
        "status: nonzero_exit",
        "TOTAL: PASS=2 FAIL=1",
    )
    if any(token not in text for token in required):
        raise RuntimeError("old infrared boundary receipt changed")
    row_pattern = re.compile(
        r"^ROW_DONE V=(?P<coupling>0\.95|1\.00) L=(?P<length>16|18) "
        r"gaps=(?P<gaps>.+)$",
        re.MULTILINE,
    )
    gap_pattern = re.compile(
        r"(?P<start>\d+)-(?P<stop>\d+):(?P<gap>[0-9.]+)"
        r"\+/-?(?P<error>[0-9.]+)"
    )
    rows = {}
    for row_match in row_pattern.finditer(text):
        coupling = float(row_match.group("coupling"))
        length = int(row_match.group("length"))
        for item in gap_pattern.finditer(row_match.group("gaps")):
            window = (int(item.group("start")), int(item.group("stop")))
            rows[(coupling, length, window)] = WindowEstimate(
                *window,
                float(item.group("gap")),
                float(item.group("error")),
            )
    if any(
        (coupling, length, PRIMARY_WINDOW) not in rows
        for coupling in (0.95, 1.0)
        for length in (16, 18)
    ):
        raise RuntimeError("old infrared boundary rows are incomplete")
    return rows


def as_ladder_rows(
    rows: dict[tuple[float, int, tuple[int, int]], PairedEstimate],
    coupling: float,
    forward_index: int,
) -> list[LadderRow]:
    result = []
    for length in (16, 18):
        estimates = {
            window: WindowEstimate(
                *window,
                rows[(coupling, length, window)].gaps[forward_index],
                rows[(coupling, length, window)].errors[forward_index],
            )
            for window in WINDOWS
        }
        result.append(
            LadderRow(
                length=length,
                delta_v=coupling - 1.0,
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
    return result


def forward_control(row: PairedEstimate) -> ForwardControl:
    contrast = np.asarray(((-1.0, 1.0, 0.0), (-1.0, 0.0, 1.0)))
    differences = contrast @ row.gaps
    covariance = contrast @ row.covariance @ contrast.T
    errors = np.sqrt(np.maximum(np.diag(covariance), 0.0))
    return ForwardControl(
        hotelling=float(differences @ np.linalg.inv(covariance) @ differences),
        maximum_contrast=float(np.max(np.abs(differences) / errors)),
        relative_span=float(np.ptp(row.gaps) / np.mean(row.gaps)),
    )


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


def main() -> int:
    checks = Checks()
    diagnostic = "--diagnostic" in sys.argv[1:]
    replay = parse_replay(allow_nonzero=diagnostic)
    if diagnostic:
        checks.check(
            replay_receipt_is_green(),
            "the upstream replay receipt is green (diagnostic mode keeps this gate visible)",
        )
    old = parse_old_rows()
    parent_detuned, parent_rk = parse_ladder_cache(
        "spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
        "spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
        "TOTAL: PASS=11 FAIL=0",
        (8, 10, 12, 14),
    )
    checks.check(
        [row.length for row in parent_detuned] == [8, 10, 12, 14]
        and [row.length for row in parent_rk] == [8, 10, 12, 14],
        "the source-pinned parent and replay provide matched six-volume ladders",
    )

    replay_z = {}
    for coupling in (0.95, 1.0):
        for length in (16, 18):
            current = replay[(coupling, length, PRIMARY_WINDOW)]
            previous = old[(coupling, length, PRIMARY_WINDOW)]
            replay_z[(coupling, length)] = abs(
                current.gaps[0] - previous.gap
            ) / np.hypot(current.errors[0], previous.gap_error)
    checks.check(
        max(replay_z.values()) < 2.0,
        "every new F=6 primary gap reproduces the independent earlier infrared receipt",
    )

    controls = {
        length: forward_control(replay[(0.95, length, PRIMARY_WINDOW)])
        for length in (16, 18)
    }
    checks.check(
        all(
            control.hotelling < HOTELLING_LIMIT
            and control.maximum_contrast < STUDENT_LIMIT
            and control.relative_span < 0.05
            for control in controls.values()
        ),
        "both detuned infrared volumes pass the paired primary-window forward plateau",
    )

    maxwell_c_squared, maxwell_c_squared_error = parse_static_maxwell_target()
    fits = {}
    for forward_index, forward in enumerate(FORWARD_LENGTHS):
        detuned = parent_detuned + as_ladder_rows(
            replay, 0.95, forward_index
        )
        rk = parent_rk + as_ladder_rows(replay, 1.0, forward_index)
        higher = fit_higher_gradient_excess(
            detuned,
            rk,
            PRIMARY_WINDOW,
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        mass = fit_polynomial_excess(
            detuned, rk, PRIMARY_WINDOW, (0, 2, 4, 6)
        )
        q8 = fit_polynomial_excess(
            detuned, rk, PRIMARY_WINDOW, (2, 4, 6, 8)
        )
        direct_detuned = fit_polynomial_spectrum(
            detuned, PRIMARY_WINDOW, (2, 4, 6)
        )
        direct_rk = fit_polynomial_spectrum(
            rk, PRIMARY_WINDOW, (2, 4, 6)
        )
        early_higher = fit_higher_gradient_excess(
            detuned,
            rk,
            WINDOWS[0],
            maxwell_c_squared,
            maxwell_c_squared_error,
        )
        early_rk = fit_polynomial_spectrum(rk, WINDOWS[0], (2, 4, 6))
        fits[forward] = (
            higher,
            mass,
            q8,
            direct_detuned,
            direct_rk,
            early_higher,
            early_rk,
        )

    checks.check(
        all(
            higher.c_squared > 0.0
            and compatible(
                higher.c_squared,
                higher.c_squared_error,
                maxwell_c_squared,
                maxwell_c_squared_error,
            )
            for higher, *_ in fits.values()
        ),
        "every paired forward endpoint gives a positive U K-compatible "
        "primary coefficient",
    )
    checks.check(
        all(
            higher.fixed_chi_squared < 9.488
            and higher.fixed_delta_chi_squared < 3.841
            for higher, *_ in fits.values()
        ),
        "fixed central U K plus q-fourth and q-sixth passes at every forward endpoint",
    )
    checks.check(
        all(
            abs(mass.coefficients[0])
            < 2.0 * mass.coefficient_errors[0]
            and higher.chi_squared - mass.chi_squared < 3.841
            and higher.chi_squared - q8.chi_squared < 3.841
            and compatible(
                q8.coefficients[0],
                q8.coefficient_errors[0],
                higher.c_squared,
                higher.c_squared_error,
            )
            for higher, mass, q8, *_ in fits.values()
        ),
        "mass and q-eighth extensions neither improve nor destabilize the primary fits",
    )
    checks.check(
        all(
            direct_detuned.coefficients[0] > 0.0
            and compatible(
                direct_detuned.coefficients[0],
                direct_detuned.coefficient_errors[0],
                maxwell_c_squared,
                maxwell_c_squared_error,
            )
            and abs(direct_rk.coefficients[0])
            < 2.0 * direct_rk.coefficient_errors[0]
            and direct_detuned.chi_squared < 7.815
            and direct_rk.chi_squared < 7.815
            for _, _, _, direct_detuned, direct_rk, _, _ in fits.values()
        ),
        "primary direct detuned spectra carry U K-compatible weight while RK does not",
    )

    for (coupling, length), value in replay_z.items():
        print(
            "REPLAY_COMPARISON",
            f"V={coupling:.2f}",
            f"L={length}",
            f"F6_z={value:.4f}",
        )
    for length, control in controls.items():
        print(
            "FORWARD_CONTROL",
            f"V=0.95 L={length}",
            f"window={PRIMARY_WINDOW[0]}-{PRIMARY_WINDOW[1]}",
            f"hotelling={control.hotelling:.4f}",
            f"max_contrast={control.maximum_contrast:.4f}",
            f"span={control.relative_span:.6f}",
        )
    for forward, values in fits.items():
        higher, mass, q8, direct_detuned, direct_rk, early, early_rk = values
        print(
            "PRIMARY_MAXWELL",
            f"F={forward}",
            f"c2={higher.c_squared:.8f}+/-{higher.c_squared_error:.8f}",
            f"fixed_chi2={higher.fixed_chi_squared:.4f}",
            f"fixed_delta_chi2={higher.fixed_delta_chi_squared:.4f}",
            f"mass2={mass.coefficients[0]:.8f}"
            f"+/-{mass.coefficient_errors[0]:.8f}",
            f"q8_delta_chi2={higher.chi_squared - q8.chi_squared:.4f}",
            f"detuned_c2={direct_detuned.coefficients[0]:.8f}"
            f"+/-{direct_detuned.coefficient_errors[0]:.8f}",
            f"RK_c2={direct_rk.coefficients[0]:.8f}"
            f"+/-{direct_rk.coefficient_errors[0]:.8f}",
        )
        print(
            "EARLY_DIAGNOSTIC",
            f"F={forward}",
            f"c2={early.c_squared:.8f}+/-{early.c_squared_error:.8f}",
            f"RK_c2={early_rk.coefficients[0]:.8f}"
            f"+/-{early_rk.coefficient_errors[0]:.8f}",
            "acceptance_role=none",
        )
    print(
        "MAXWELL_TARGET",
        f"UK={maxwell_c_squared:.8f}+/-{maxwell_c_squared_error:.8f}",
    )
    print(
        "CERTIFICATE: result_thresholds_predeclared=True "
        "new_lower_momenta=L16,L18 paired_forward_lengths=6,12,20 "
        "primary_window=8-14 early_window_diagnostic_only=True "
        "finite_volume=True thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
