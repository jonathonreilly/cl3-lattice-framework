#!/usr/bin/env python3
"""Corrected staggered-field off-axis cubic-orbit spectroscopy scout.

Two preserved predecessor scouts supplied link-centred transverse phases but
omitted the staggered-electric-field sign expected by the inherited occupation
evaluator.  This runner applies that missing sign to the complete cubic-orbit
coefficient table and then executes the otherwise unchanged predeclared scout.
"""

from __future__ import annotations

import numpy as np

import spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04 as orbit_scout


AUDIT_INPUT_PATHS = (
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/spin_half_cubic_ice_finite_delta_projector_stiffness_2026_09_03.py",
    "scripts/spin_half_cubic_ice_finite_delta_transverse_pole_2026_09_03.py",
    "scripts/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_off_axis_transverse_scout_2026_09_04.txt",
    "scripts/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.py",
    "logs/runner-cache/spin_half_cubic_ice_off_axis_cubic_orbit_scout_2026_09_04.txt",
)

AUDIT_TIMEOUT_SEC = 3600
_UNSTAGGERED_COEFFICIENTS = orbit_scout.cubic_orbit_coefficients


def staggered_cubic_orbit_coefficients(
    length: int,
) -> tuple[
    np.ndarray,
    np.ndarray,
    list[tuple[str, tuple[int, int, int], int]],
    np.ndarray,
]:
    real, imaginary, modes, longitudinal = _UNSTAGGERED_COEFFICIENTS(length)
    coordinates = np.indices((length, length, length))
    site_staggering = (-1.0) ** np.sum(coordinates, axis=0)
    link_staggering = np.repeat(site_staggering.ravel(), 3)
    transverse = (real + 1j * imaginary) * link_staggering[None, :]
    corrected_longitudinal = longitudinal * link_staggering[None, :]
    return (
        transverse.real.copy(),
        transverse.imag.copy(),
        modes,
        corrected_longitudinal,
    )


def staggered_longitudinal_null_control() -> float:
    maximum = 0.0
    for length in (6, 8):
        sampler = orbit_scout.CubicIceSampler(length, 29_000_000 + length)
        _, _, _, longitudinal = staggered_cubic_orbit_coefficients(length)
        for _ in range(12):
            sampler.sweep()
            centered_occupation = (
                sampler.occupation.astype(float) - 0.5
            ).ravel()
            maximum = max(
                maximum,
                float(np.max(np.abs(longitudinal @ centered_occupation))),
            )
    return maximum


def main() -> int:
    orbit_scout.cubic_orbit_coefficients = (
        staggered_cubic_orbit_coefficients
    )
    orbit_scout.longitudinal_null_control = (
        staggered_longitudinal_null_control
    )
    return orbit_scout.main()


if __name__ == "__main__":
    raise SystemExit(main())
