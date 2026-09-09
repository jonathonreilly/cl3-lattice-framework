#!/usr/bin/env python3
"""Source-pinned L=16,18 transverse ladder for the cubic-ice Maxwell join.

This runner contains only the expensive new lower-momentum calculation.  A
separate cheap join runner combines its receipt with the already computed
L=8,10,12,14 parent receipt, so neither stochastic ladder is rerun merely to
change the infrared fit or its diagnostics.
"""

from __future__ import annotations

import numpy as np

from spin_half_cubic_ice_late_time_maxwell_join_2026_09_04 import run_ladder


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py",
    "scripts/spin_half_cubic_ice_late_time_maxwell_join_2026_09_04.py",
)

AUDIT_TIMEOUT_SEC = 21600


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
    lengths = (16, 18)
    detuned = run_ladder(
        -0.05,
        lengths,
        {16: 8, 18: 12},
        {16: 2048, 18: 2048},
        18_000_000,
    )
    rk = run_ladder(
        0.0,
        lengths,
        {16: 8, 18: 10},
        {16: 512, 18: 512},
        19_000_000,
    )
    rows = detuned + rk
    checks.check(
        all(row.count_consistent and row.sector_consistent for row in rows),
        "every infrared population preserves exact counts, Gauss charge, and zero electric flux",
    )
    checks.check(
        min(row.minimum_effective_fraction for row in rows) > 0.85
        and min(row.minimum_origin_tau16_count for row in rows) >= 40
        and min(row.minimum_forward_count for row in rows) >= 40,
        "infrared populations retain the declared weight and genealogy floors",
    )
    checks.check(
        all(
            np.all(row.mean_curve.real > 0.0)
            and row.imaginary_residual < 0.06
            for row in rows
        ),
        "every infrared correlator remains positive through tau=16 with bounded imaginary residual",
    )
    print(
        "INFRARED_HEALTH",
        f"min_ess={min(row.minimum_effective_fraction for row in rows):.6f}",
        f"min_origin_tau16={min(row.minimum_origin_tau16_count for row in rows):.0f}",
        f"min_forward={min(row.minimum_forward_count for row in rows):.0f}",
    )
    print(
        "CERTIFICATE: lower_momenta=L16,L18 outer_populations=True "
        "finite_population=True finite_imaginary_time=True "
        "thermodynamic_limit=False"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
