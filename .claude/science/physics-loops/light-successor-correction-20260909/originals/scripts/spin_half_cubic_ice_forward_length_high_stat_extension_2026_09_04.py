#!/usr/bin/env python3
"""High-statistics detuned forward-length extension through F=20.

The first paired-F receipt found sub-percent but statistically unresolved
motion among F=8,10,12.  This immutable data runner increases both independent
outer populations and walkers, extends the same shared trajectories through
F=20, and leaves every plateau decision to a separate cheap join.
"""

from __future__ import annotations

import numpy as np

import spin_half_cubic_ice_forward_length_ladder_2026_09_04 as paired


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py",
    "scripts/spin_half_cubic_ice_forward_length_ladder_2026_09_04.py",
)

AUDIT_TIMEOUT_SEC = 10800
FORWARD_LENGTHS = (6, 8, 10, 12, 14, 16, 20)
TARGET_WINDOWS = ((2, 6), (8, 14))


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
    paired.FORWARD_LENGTHS = FORWARD_LENGTHS
    replicas = [
        paired.run_replica(-0.05, 3072, 36_000_000 + replica)
        for replica in range(10)
    ]
    summary = paired.summarize(-0.05, replicas)
    checks.check(
        summary.count_consistent and summary.sector_consistent,
        "every high-statistics population preserves exact counts and sectors",
    )
    checks.check(
        summary.minimum_effective_fraction > 0.85
        and summary.minimum_origin_tau16_count >= 40
        and summary.minimum_forward_count >= 40,
        "the extended trajectories retain the declared weight and genealogy floors",
    )
    checks.check(
        all(
            np.all(np.isfinite(summary.gaps[window]))
            and np.all(summary.gaps[window] > 0.0)
            and np.all(np.isfinite(summary.covariances[window]))
            for window in paired.WINDOWS
        )
        and np.all(summary.mean_curves.real > 0.0)
        and summary.imaginary_residual < 0.06,
        "every extended correlator, gap, and covariance remains finite and positive",
    )
    long_indices = [
        FORWARD_LENGTHS.index(value) for value in (12, 14, 16, 20)
    ]
    checks.check(
        all(
            np.linalg.matrix_rank(
                summary.covariances[window][
                    np.ix_(long_indices, long_indices)
                ],
                tol=1.0e-14,
            )
            == len(long_indices)
            for window in TARGET_WINDOWS
        ),
        "each predeclared long-forward covariance block has full rank",
    )
    for window in paired.WINDOWS:
        print(
            "EXTENDED_FORWARD_GAPS",
            "V=0.95",
            f"window={window[0]}-{window[1]}",
            "values="
            + ",".join(
                f"{forward}:{summary.gaps[window][index]:.8f}"
                for index, forward in enumerate(FORWARD_LENGTHS)
            ),
        )
        if window in TARGET_WINDOWS:
            print(
                "EXTENDED_FORWARD_COVARIANCE",
                "V=0.95",
                f"window={window[0]}-{window[1]}",
                "row_major="
                + ",".join(
                    f"{value:.12e}"
                    for value in summary.covariances[window].ravel()
                ),
            )
    print(
        "HEALTH",
        f"min_ess={summary.minimum_effective_fraction:.6f}",
        f"min_origin_tau16={summary.minimum_origin_tau16_count:.0f}",
        f"min_forward={summary.minimum_forward_count:.0f}",
    )
    print(
        "CERTIFICATE: fixed_L=8 detuned_only=True "
        "paired_forward_lengths=6,8,10,12,14,16,20 "
        "outer_populations=10 walkers=3072 result_test_deferred=True"
    )
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
