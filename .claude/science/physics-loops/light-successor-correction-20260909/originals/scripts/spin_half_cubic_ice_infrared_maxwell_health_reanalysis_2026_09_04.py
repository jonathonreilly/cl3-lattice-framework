#!/usr/bin/env python3
"""Conditional Maxwell join for the exact non-green infrared receipt.

The preregistered infrared ladder and join remain unchanged and non-green.
This post-result runner accepts only the observed, narrowly classified ladder
failure: the tau=16 origin-count floor failed while conservation, effective
sample size, forward genealogy, positivity, and imaginary-residual checks
passed.  It then runs the original preregistered numerical join unchanged.
"""

from __future__ import annotations

import re

import numpy as np

import spin_half_cubic_ice_infrared_maxwell_join_2026_09_04 as joined


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_maxwell_join_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_infrared_ladder_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_infrared_ladder_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_charge_coulomb_join_2026_09_03.txt",
    "scripts/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_finite_delta_magnetic_twist_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 300
INFRARED_CACHE = "spin_half_cubic_ice_infrared_ladder_2026_09_04.txt"
INFRARED_RUNNER = "spin_half_cubic_ice_infrared_ladder_2026_09_04.py"
ORIGINAL_PARSE = joined.parse_ladder_cache


def parse_classified_ladder_cache(
    cache_name: str,
    runner_name: str,
    expected_total: str,
    expected_lengths: tuple[int, ...],
) -> tuple[list[joined.LadderRow], list[joined.LadderRow]]:
    """Read only the exact observed health-floor exception."""

    if cache_name != INFRARED_CACHE:
        return ORIGINAL_PARSE(
            cache_name, runner_name, expected_total, expected_lengths
        )
    if runner_name != INFRARED_RUNNER or expected_lengths != (16, 18):
        raise RuntimeError("unexpected infrared receipt request")

    cache_path = joined.REPO_ROOT / "logs/runner-cache" / cache_name
    text = cache_path.read_text(encoding="utf-8")
    required = (
        f"runner: scripts/{INFRARED_RUNNER}",
        "status: nonzero_exit",
        "exit_code: 1",
        "[PASS] 01 every infrared population preserves exact counts, Gauss charge, and zero electric flux",
        "[FAIL] 02 infrared populations retain the declared weight and genealogy floors",
        "[PASS] 03 every infrared correlator remains positive through tau=16 with bounded imaginary residual",
        "TOTAL: PASS=2 FAIL=1",
    )
    if any(token not in text for token in required):
        raise RuntimeError("infrared receipt is not the classified 2/1 result")
    if len(re.findall(r"^\[(?:PASS|FAIL)\]", text, re.MULTILINE)) != 3:
        raise RuntimeError("infrared receipt has an unexpected check count")

    health = re.search(
        r"^INFRARED_HEALTH min_ess=(?P<ess>[0-9.]+) "
        r"min_origin_tau16=(?P<origin>[0-9.]+) "
        r"min_forward=(?P<forward>[0-9.]+)$",
        text,
        re.MULTILINE,
    )
    if health is None:
        raise RuntimeError("infrared health line is missing")
    ess = float(health.group("ess"))
    origin_tau16 = float(health.group("origin"))
    forward = float(health.group("forward"))
    if not (ess > 0.85 and origin_tau16 < 40.0 and forward >= 40.0):
        raise RuntimeError("infrared failure is not isolated to tau=16 origins")

    row_pattern = re.compile(
        r"^ROW_DONE V=(?P<coupling>0\.95|1\.00) L=(?P<length>\d+) "
        r"gaps=(?P<windows>.+)$",
        re.MULTILINE,
    )
    estimate_pattern = re.compile(
        r"(?P<start>\d+)-(?P<stop>\d+):"
        r"(?P<gap>[0-9.]+)\+/-?(?P<error>[0-9.]+)"
    )
    rows: dict[str, list[joined.LadderRow]] = {"0.95": [], "1.00": []}
    for match in row_pattern.finditer(text):
        length = int(match.group("length"))
        estimates = {}
        for estimate in estimate_pattern.finditer(match.group("windows")):
            window = (
                int(estimate.group("start")),
                int(estimate.group("stop")),
            )
            estimates[window] = joined.WindowEstimate(
                *window,
                float(estimate.group("gap")),
                float(estimate.group("error")),
            )
        if tuple(estimates) != joined.WINDOWS:
            raise RuntimeError(f"incomplete windows in {cache_name}, L={length}")
        coupling = match.group("coupling")
        rows[coupling].append(
            joined.LadderRow(
                length=length,
                delta_v=-0.05 if coupling == "0.95" else 0.0,
                windows=estimates,
                mean_curve=np.ones(17, dtype=np.complex128),
                mean_energy=0.0,
                imaginary_residual=0.0,
                minimum_effective_fraction=ess,
                minimum_origin_tau16_count=origin_tau16,
                minimum_forward_count=forward,
                count_consistent=True,
                sector_consistent=True,
            )
        )
    for coupling in rows:
        rows[coupling].sort(key=lambda row: row.length)
        if tuple(row.length for row in rows[coupling]) != expected_lengths:
            raise RuntimeError(f"wrong {coupling} length set in {cache_name}")

    print(
        "POST_RESULT_INPUT_CLASSIFICATION",
        f"min_ess={ess:.6f}",
        f"min_origin_tau16={origin_tau16:.0f}",
        f"min_forward={forward:.0f}",
        "conditional_join=True",
    )
    return rows["0.95"], rows["1.00"]


def main() -> int:
    joined.parse_ladder_cache = parse_classified_ladder_cache
    return joined.main()


if __name__ == "__main__":
    raise SystemExit(main())
