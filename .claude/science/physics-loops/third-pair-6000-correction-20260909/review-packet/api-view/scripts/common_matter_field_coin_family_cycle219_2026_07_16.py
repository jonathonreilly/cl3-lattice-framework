#!/usr/bin/env python3
"""Cycle 219: one proper-cubic coin family for field and massive matter.

Use the Cycle-215-selected even phase -1 for both field and matter, and set
the vacuum-relative scalar phase by the common-cone relation.  The massless
endpoint beta=0 is exactly the acoustic field coin; beta<0 gives the
Cycle-210 bound object a robust inertial/rest/exchange mass.

This is a one-parameter candidate family, not one law-generated mass spectrum.
The beta value/species content and common-cone relation remain supplied.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "COMMON_MATTER_FIELD_COIN_FAMILY_CYCLE219_NOTE_2026-07-16.md"
)

C_SQUARED = 1 / 3
COUPLING = 0.04
PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def common_species(beta: float) -> c210.Species:
    inertial_mass = float(3 * np.tan(-beta / 2))
    rest_energy = C_SQUARED * inertial_mass
    return c210.Species(
        beta,
        np.pi,
        rest_energy,
        inertial_mass,
        c210.cubic_coin(np.pi, beta, rest_energy),
    )


def rest_mass(species: c210.Species) -> float:
    scalar_eigenvalue = np.trace(c210.P_SCALAR @ species.coin)
    return float(np.angle(scalar_eigenvalue)) / C_SQUARED


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "one proper-cubic coin family",
        "massless endpoint",
        "same even-sector phase",
        "common acoustic cone",
        "robust internal gap",
        "rest/dispersion/inertial/exchange mass",
        "one-parameter family is not one generated spectrum",
        "beta selection remains open",
        "det c=1 is not retained",
        "no axiom conclusion",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves common-law gain and spectrum caveat", not missing, missing)


def endpoint_and_family_controls() -> tuple[c210.Species, ...]:
    massless = common_species(0.0)
    check(
        "beta=0 is exactly the Cycle-214 acoustic field coin",
        abs(massless.rest_phase) < 2e-15
        and abs(massless.analytic_mass) < 2e-15
        and np.linalg.norm(massless.coin - c214.FIELD_COIN) < 2e-12,
    )

    species_set = tuple(common_species(beta) for beta in (-0.2, -0.3, -0.4))
    rows = []
    for species in species_set:
        curvature = c210.curvature_tensor(species, step=1e-4)
        dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
        rows.append(
            (
                species.beta,
                species.rest_phase,
                rest_mass(species),
                dispersion_mass,
                species.analytic_mass,
            )
        )
        check(
            f"beta={species.beta} common-family rest and dispersion mass agree",
            abs(rest_mass(species) / species.analytic_mass - 1) < 2e-12
            and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
            and np.linalg.norm(species.coin.conj().T @ species.coin - np.eye(6))
            < 2e-12,
            rows[-1],
        )
        check(
            f"beta={species.beta} exact contact correction keeps the object bound",
            np.linalg.norm(
                c210.interaction_correction(species).conj().T
                @ c210.interaction_correction(species)
                - np.eye(36)
            )
            < 3e-12,
        )

    held_out = common_species(-0.35)
    held_mass = 1 / float(
        np.mean(np.diag(c210.curvature_tensor(held_out, step=1e-4)))
    )
    check(
        "a held-out beta shares the same field-to-matter mass map",
        abs(rest_mass(held_out) / held_mass - 1) < 4e-6,
        {"rest_mass": rest_mass(held_out), "dispersion_mass": held_mass},
    )

    frames = c210.proper_cubic_frames()
    covariance = []
    for species in (massless,) + species_set:
        for frame in frames:
            representation = c210.direction_permutation(frame)
            covariance.append(
                np.linalg.norm(
                    representation @ species.coin @ representation.conj().T
                    - species.coin
                )
            )
    check(
        "massless and massive family members commute with all cubic frames",
        max(covariance) < 2e-12,
        max(covariance),
    )

    gaps = [min(abs(species.beta), np.pi) for species in species_set]
    check(
        "the shared phase -1 keeps the even sector maximally separated",
        all(abs(np.angle(-1) - np.pi) < 2e-15 for _ in species_set)
        and min(gaps) >= 0.2,
        gaps,
    )
    return species_set


def operational_mass_controls(species_set: tuple[c210.Species, ...]) -> None:
    inertia_rows = []
    for species in species_set:
        response = c210.force_response(species, 2e-5)
        inertia_rows.append(
            (
                species.beta,
                rest_mass(species),
                response.measured_mass,
                species.analytic_mass,
                response.band_probability,
            )
        )
    check(
        "rest/dispersion/inertial/exchange mass agrees on robust packets",
        max(abs(row[2] / row[3] - 1) for row in inertia_rows) < 0.007
        and max(abs(row[1] / row[3] - 1) for row in inertia_rows) < 2e-12
        and min(row[4] for row in inertia_rows) > 0.999,
        inertia_rows,
    )

    side = 31
    kernel = 3 * c211.solve_field(c211.point_source(side))
    gradient = c211.gradient(kernel, (4, 0, 0))[0]
    source = species_set[-1]
    source_charge = rest_mass(source)
    exchange_rows = []
    for species in species_set:
        charge = rest_mass(species)
        force = COUPLING**2 * source_charge * charge * gradient
        response = c210.force_response(species, force)
        expected = -COUPLING**2 * source_charge * gradient
        exchange_rows.append(
            (
                species.beta,
                charge,
                response.measured_mass,
                response.acceleration / expected,
            )
        )
    check(
        "one common-family charge gives species-independent static exchange",
        max(abs(row[3] - 1) for row in exchange_rows) < 0.007,
        exchange_rows,
    )

    for species in species_set:
        pair_mass = 2 * species.rest_phase / C_SQUARED
        check(
            f"beta={species.beta} held-out two-object composition adds mass",
            abs(pair_mass / (2 * species.analytic_mass) - 1) < 2e-12,
            pair_mass,
        )

    record_zero = np.array((1, 0), dtype=complex)
    record_plus = np.array((1, 1), dtype=complex) / np.sqrt(2)
    charge = source_charge
    archived = (
        charge,
        charge * np.vdot(record_zero, record_zero).real,
        charge
        * np.vdot(record_zero, record_zero).real
        * np.vdot(record_plus, record_plus).real,
    )
    check(
        "record redundancy does not multiply common-family mass",
        max(abs(value - charge) for value in archived) < 2e-14,
        archived,
    )


def controls_and_open_selection(species_set: tuple[c210.Species, ...]) -> None:
    determinants = [float(np.angle(np.linalg.det(species.coin))) for species in species_set]
    check(
        "the robust common family does not silently retain the optional det C=1 constraint",
        all(abs(value) > 1e-3 for value in determinants)
        and determinants[0] < determinants[1] < determinants[2],
        determinants,
    )

    shifted = []
    for species in species_set:
        shifted_phase = species.rest_phase + 0.03
        shifted_coin = c210.cubic_coin(np.pi, species.beta, shifted_phase)
        shifted_mass = float(np.angle(np.trace(c210.P_SCALAR @ shifted_coin))) / C_SQUARED
        shifted.append(shifted_mass / species.analytic_mass)
    check(
        "the common coin architecture alone does not force the cone mass relation",
        max(shifted) - min(shifted) > 0.09,
        shifted,
    )

    reference = species_set[-1]
    lifted = c210.cubic_coin(
        np.pi + 2 * np.pi,
        reference.beta + 2 * np.pi,
        reference.rest_phase + 2 * np.pi,
    )
    check(
        "phase-coordinate lifts leave the common-family physical coin unchanged",
        np.linalg.norm(lifted - reference.coin) < 2e-12,
    )

    distinct = [np.linalg.norm(left.coin - right.coin) for left, right in zip(species_set, species_set[1:])]
    check(
        "different tested beta values are distinct candidate laws unless beta becomes physical state",
        min(distinct) > 0.05,
        distinct,
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    species_set = endpoint_and_family_controls()
    operational_mass_controls(species_set)
    controls_and_open_selection(species_set)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
