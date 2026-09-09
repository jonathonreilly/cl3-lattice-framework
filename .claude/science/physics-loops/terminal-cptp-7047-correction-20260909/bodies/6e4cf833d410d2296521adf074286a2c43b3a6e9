#!/usr/bin/env python3
"""Cycle 227: archive-carrier energy versus rest-source accounting.

Cross the Cycle-215 massless field endpoint with a naive family-wide extension
of Cycle 219's supplied static matter rest-source map.  A normalized massless
carrier can have a positive conserved projected-wave energy and positive
conserved stiffness coordinate while that Q-only extension assigns zero.  A
massive branch can also change its near-origin quasienergy with momentum while
the same extension retains the static rest scalar.

Cycle 219 does not license either extrapolation as a physical source law. This
is a bounded accounting fork. It does not identify either positive coordinate
with a selected physical Hamiltonian, prove that Records must use these
carriers, derive stress-energy gravity, or support an axiom change.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

import active_cubic_source_response_cycle211_2026_07_16 as c211
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import retarded_cubic_mass_field_cycle213_2026_07_16 as c213
import autonomous_cubic_field_emission_cycle214_2026_07_16 as c214
import finite_coin_scalar_wave_dilation_cycle215_2026_07_16 as c215
import virtual_exchange_green_kernel_cycle216_2026_07_16 as c216
import common_matter_field_coin_family_cycle219_2026_07_16 as c219


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "ARCHIVE_CARRIER_SOURCE_LEDGER_CYCLE227_NOTE_2026-07-17.md"
)

DT = 1 / np.sqrt(3)
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


def carrier_packet(
    side: int,
    center: tuple[int, int, int],
    width: float,
    internal: np.ndarray = c210.UNIFORM,
) -> np.ndarray:
    """One supplied normalized packet of the beta=0 field carrier."""
    coordinates = np.indices((side, side, side))
    radius_squared = np.zeros((side, side, side), dtype=float)
    for axis, origin in enumerate(center):
        signed = (coordinates[axis] - origin + side // 2) % side - side // 2
        radius_squared += signed**2
    envelope = np.exp(-radius_squared / (4 * width**2))
    state = envelope[..., None] * np.asarray(internal)
    return state / np.linalg.norm(state)


def point_carrier(side: int, position: tuple[int, int, int]) -> np.ndarray:
    state = np.zeros((side, side, side, 6), dtype=complex)
    state[position] = c210.UNIFORM
    return state


def plane_wave_state(side: int, momentum: np.ndarray, internal: np.ndarray) -> np.ndarray:
    coordinates = np.indices((side, side, side))
    phase = np.exp(
        1j
        * sum(
            momentum[axis] * coordinates[axis]
            for axis in range(3)
        )
    )
    state = phase[..., None] * internal
    return state / np.linalg.norm(state)


def projected_wave_energy(state: np.ndarray) -> float:
    """Cycle-213 energy of two consecutive real scalar projections."""
    following = c215.field_step(state)
    current_scalar = c215.scalar_projection(state)
    following_scalar = c215.scalar_projection(following)
    if max(
        float(np.max(np.abs(current_scalar.imag))),
        float(np.max(np.abs(following_scalar.imag))),
    ) > 2e-14:
        raise ValueError("the bounded wave-energy fixture requires real projections")
    return c213.field_energy(
        following_scalar.real,
        current_scalar.real,
        dt=DT,
    )


def stiffness_coordinate(state: np.ndarray) -> float:
    """Positive K/2 coordinate, where K=2I-U-U^dagger."""
    return float(np.vdot(state, c216.apply_stiffness(state)).real / 2)


def orbit_coordinates(state: np.ndarray, ticks: int = 14) -> dict[str, np.ndarray]:
    wave = []
    stiffness = []
    norms = []
    for _ in range(ticks):
        wave.append(projected_wave_energy(state))
        stiffness.append(stiffness_coordinate(state))
        norms.append(float(np.linalg.norm(state)))
        state = c215.field_step(state)
    return {
        "wave": np.asarray(wave),
        "stiffness": np.asarray(stiffness),
        "norm": np.asarray(norms),
    }


def q_only_extension_field(side: int, rest_scalar: float) -> np.ndarray:
    """Explicitly unlicensed extension of the static matter vertex."""
    return c211.solve_field(rest_scalar * c211.point_source(side))


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "rest-scalar source is not a universal energy ledger",
        "source-ledger fork",
        "naive q-only extension",
        "massless endpoint",
        "physical carrier",
        "logical redundancy",
        "positive conserved",
        "stress-energy remains open",
        "quasienergy",
        "conditional",
        "general relativity",
        "no axiom conclusion",
        "no-go discipline",
        "n1 — alternative routes",
        "n8 — cross-cycle echo",
        "draft parking branch",
    )
    missing = tuple(phrase for phrase in required if phrase not in text)
    check("note preserves the accounting boundary and scope", not missing, missing)


def massless_carrier_controls() -> tuple[np.ndarray, dict[str, np.ndarray]]:
    massless = c219.common_species(0.0)
    rest_scalar = c219.rest_mass(massless)
    check(
        "the common-family beta=0 endpoint has zero vacuum-relative rest scalar",
        abs(rest_scalar) < 2e-14
        and np.linalg.norm(massless.coin - c214.FIELD_COIN) < 2e-12,
        rest_scalar,
    )

    rows = []
    reference_state = None
    reference_orbit = None
    for side, width in ((17, 0.6), (17, 1.7), (23, 1.0), (23, 2.4)):
        center = (side // 2, side // 2, side // 2)
        state = carrier_packet(side, center, width)
        orbit = orbit_coordinates(state)
        rows.append(
            {
                "side": side,
                "width": width,
                "wave": float(orbit["wave"][0]),
                "wave_drift": float(np.ptp(orbit["wave"])),
                "stiffness": float(orbit["stiffness"][0]),
                "stiffness_drift": float(np.ptp(orbit["stiffness"])),
                "norm_drift": float(np.max(np.abs(orbit["norm"] - 1))),
            }
        )
        if side == 23 and width == 1.0:
            reference_state = state
            reference_orbit = orbit

    check(
        "massless packets carry positive conserved candidate field coordinates",
        min(row["wave"] for row in rows) > 0.05
        and min(row["stiffness"] for row in rows) > 0.015
        and max(row["wave_drift"] for row in rows) < 9e-13
        and max(row["stiffness_drift"] for row in rows) < 9e-13
        and max(row["norm_drift"] for row in rows) < 9e-13,
        rows,
    )
    assert reference_state is not None and reference_orbit is not None
    zero_field = q_only_extension_field(reference_state.shape[0], rest_scalar)
    check(
        "a naive Q-only extension produces no field from that carrier",
        np.linalg.norm(zero_field) < 2e-14
        and reference_orbit["wave"][0] > 0
        and reference_orbit["stiffness"][0] > 0,
        {
            "rest_scalar": rest_scalar,
            "field_norm": float(np.linalg.norm(zero_field)),
            "wave": float(reference_orbit["wave"][0]),
            "stiffness": float(reference_orbit["stiffness"][0]),
        },
    )
    return reference_state, reference_orbit


def exact_compact_and_normalization_controls() -> None:
    side = 17
    first = point_carrier(side, (4, 4, 4))
    second = point_carrier(side, (12, 12, 12))
    orbit = orbit_coordinates(first, ticks=16)
    check(
        "a compact scalar carrier has exact positive conserved coordinates",
        abs(orbit["wave"][0] - 5 / 4) < 3e-14
        and abs(orbit["stiffness"][0] - 1) < 3e-14
        and np.ptp(orbit["wave"]) < 3e-13
        and np.ptp(orbit["stiffness"]) < 3e-13
        and np.max(np.abs(orbit["norm"] - 1)) < 3e-13,
        {
            "wave": float(orbit["wave"][0]),
            "stiffness_half": float(orbit["stiffness"][0]),
            "wave_drift": float(np.ptp(orbit["wave"])),
            "stiffness_drift": float(np.ptp(orbit["stiffness"])),
        },
    )

    unnormalized_pair = first + second
    normalized_superposition = unnormalized_pair / np.sqrt(2)
    check(
        "quadratic additivity does not turn one normalized superposition into two carriers",
        abs(projected_wave_energy(unnormalized_pair) - 5 / 2) < 3e-14
        and abs(stiffness_coordinate(unnormalized_pair) - 2) < 3e-14
        and abs(projected_wave_energy(normalized_superposition) - 5 / 4) < 3e-14
        and abs(stiffness_coordinate(normalized_superposition) - 1) < 3e-14,
        {
            "unnormalized_wave": projected_wave_energy(unnormalized_pair),
            "normalized_wave": projected_wave_energy(normalized_superposition),
            "unnormalized_stiffness": stiffness_coordinate(unnormalized_pair),
            "normalized_stiffness": stiffness_coordinate(normalized_superposition),
        },
    )

    scaled = 1.7 * first
    check(
        "both quadratic coordinates scale with amplitude squared",
        abs(projected_wave_energy(scaled) / projected_wave_energy(first) - 1.7**2)
        < 3e-14
        and abs(stiffness_coordinate(scaled) / stiffness_coordinate(first) - 1.7**2)
        < 3e-14,
    )


def acoustic_and_hidden_mode_controls() -> None:
    side = 31
    momentum = 2 * np.pi * np.asarray((1, 0, 0), dtype=float) / side
    walk = c216.walk(momentum)
    values, vectors = np.linalg.eig(walk)
    overlaps = np.abs(vectors.conj().T @ c210.UNIFORM)
    acoustic_index = int(np.argmax(overlaps))
    acoustic = vectors[:, acoustic_index] / np.linalg.norm(vectors[:, acoustic_index])
    acoustic_state = plane_wave_state(side, momentum, acoustic)
    full_stiffness = 2 * stiffness_coordinate(acoustic_state)
    laplacian_symbol = c216.laplacian_symbol(momentum)
    check(
        "a nonzero acoustic mode has exact K eigenvalue L(k)/3 at zero rest scalar",
        abs(full_stiffness - laplacian_symbol / 3) < 3e-13
        and full_stiffness > 0.01
        and abs(c219.rest_mass(c219.common_species(0.0))) < 2e-14,
        {
            "K": full_stiffness,
            "L_over_3": laplacian_symbol / 3,
            "phase": float(np.angle(values[acoustic_index])),
        },
    )

    phases = np.angle(values)
    plus_indices = np.where(np.abs(phases) < 2e-10)[0]
    minus_indices = np.where(np.abs(np.abs(phases) - np.pi) < 2e-10)[0]
    rows = []
    for label, indices, expected_half_stiffness in (
        ("plus", plus_indices, 0.0),
        ("minus", minus_indices, 2.0),
    ):
        for index in indices:
            state = plane_wave_state(side, momentum, vectors[:, index])
            rows.append(
                {
                    "label": label,
                    "scalar_norm": float(np.linalg.norm(c215.scalar_projection(state))),
                    "K_half": stiffness_coordinate(state),
                    "expected_K_half": expected_half_stiffness,
                }
            )
    check(
        "two plus and two minus flat modes separate scalar visibility from stiffness",
        len(plus_indices) == 2
        and len(minus_indices) == 2
        and max(row["scalar_norm"] for row in rows) < 2e-13
        and max(
            abs(row["K_half"] - row["expected_K_half"])
            for row in rows
        )
        < 8e-13,
        rows,
    )


def covariance_and_encoding_controls(reference_state: np.ndarray) -> None:
    side = reference_state.shape[0]
    shift = (3, -4, 2)
    translated = np.roll(reference_state, shift, axis=(0, 1, 2))
    check(
        "both candidate coordinates are translation invariant",
        abs(projected_wave_energy(translated) - projected_wave_energy(reference_state))
        < 3e-14
        and abs(stiffness_coordinate(translated) - stiffness_coordinate(reference_state))
        < 3e-14,
    )

    frame_rows = []
    for frame in c210.proper_cubic_frames():
        rotated = c215.rotate_field_state(reference_state, frame)
        frame_rows.append(
            (
                abs(projected_wave_energy(rotated) - projected_wave_energy(reference_state)),
                abs(stiffness_coordinate(rotated) - stiffness_coordinate(reference_state)),
            )
        )
    check(
        "both candidate coordinates agree in all 24 proper-cubic frames",
        len(frame_rows) == 24
        and max(row[0] for row in frame_rows) < 4e-14
        and max(row[1] for row in frame_rows) < 4e-14,
        {
            "wave": max(row[0] for row in frame_rows),
            "stiffness": max(row[1] for row in frame_rows),
        },
    )

    rng = np.random.default_rng(227024)
    anisotropic = rng.normal(size=(7, 7, 7, 6))
    anisotropic = anisotropic / np.linalg.norm(anisotropic)
    anisotropic_rows = []
    for frame in c210.proper_cubic_frames():
        rotated = c215.rotate_field_state(anisotropic, frame)
        anisotropic_rows.append(
            (
                abs(projected_wave_energy(rotated) - projected_wave_energy(anisotropic)),
                abs(stiffness_coordinate(rotated) - stiffness_coordinate(anisotropic)),
            )
        )
    check(
        "a held-out anisotropic state preserves both coordinates in all frames",
        len(anisotropic_rows) == 24
        and max(row[0] for row in anisotropic_rows) < 2e-13
        and max(row[1] for row in anisotropic_rows) < 2e-13,
        {
            "wave": max(row[0] for row in anisotropic_rows),
            "stiffness": max(row[1] for row in anisotropic_rows),
        },
    )

    center = side // 2
    zero_carrier = carrier_packet(side, (center - 5, center, center), 1.0)
    one_carrier = carrier_packet(side, (center + 5, center, center), 1.0)
    bit_rows = (
        (projected_wave_energy(zero_carrier), stiffness_coordinate(zero_carrier)),
        (projected_wave_energy(one_carrier), stiffness_coordinate(one_carrier)),
    )
    check(
        "a two-position logical encoding has value-independent carrier coordinates",
        abs(bit_rows[0][0] - bit_rows[1][0]) < 3e-14
        and abs(bit_rows[0][1] - bit_rows[1][1]) < 3e-14,
        bit_rows,
    )

    one_rail = np.stack((zero_carrier,))
    two_rails = np.stack((zero_carrier, one_carrier))
    one_wave = sum(projected_wave_energy(state) for state in one_rail)
    two_wave = sum(projected_wave_energy(state) for state in two_rails)
    one_stiffness = sum(stiffness_coordinate(state) for state in one_rail)
    two_stiffness = sum(stiffness_coordinate(state) for state in two_rails)
    check(
        "two independent carrier rails add while two zero rest scalars remain zero",
        abs(two_wave - 2 * one_wave) < 3e-14
        and abs(two_stiffness - 2 * one_stiffness) < 3e-14
        and abs(2 * c219.rest_mass(c219.common_species(0.0))) < 2e-14,
        {
            "one_wave": one_wave,
            "two_wave": two_wave,
            "one_stiffness": one_stiffness,
            "two_stiffness": two_stiffness,
        },
    )

    deleted = np.zeros_like(zero_carrier)
    check(
        "carrier deletion removes both candidate coordinates",
        projected_wave_energy(deleted) == 0
        and stiffness_coordinate(deleted) == 0,
    )


def massive_kinetic_and_archive_controls(reference_state: np.ndarray) -> None:
    species = c219.common_species(-0.3)
    charge = c219.rest_mass(species)
    momenta = (
        np.zeros(3),
        np.asarray((0.2, 0.0, 0.0)),
        np.asarray((0.3, 0.0, 0.0)),
    )
    phases = np.asarray([c210.phase_near_origin(momentum, species) for momentum in momenta])
    kinetic = phases - phases[0]
    fields = tuple(q_only_extension_field(23, charge) for _ in momenta)
    check(
        "a naive rest-only extension misses massive kinetic quasienergy",
        kinetic[0] == 0
        and kinetic[1] > 0.03
        and kinetic[2] > kinetic[1]
        and max(np.linalg.norm(field - fields[0]) for field in fields[1:]) < 2e-14,
        {
            "rest_scalar": charge,
            "phases": phases.tolist(),
            "kinetic": kinetic.tolist(),
        },
    )

    covariance = []
    reference_momentum = np.asarray((0.21, -0.13, 0.08))
    reference_phase = c210.phase_near_origin(reference_momentum, species)
    for frame in c210.proper_cubic_frames():
        covariance.append(
            abs(c210.phase_near_origin(frame @ reference_momentum, species) - reference_phase)
        )
    check(
        "the Q-only kinetic blind spot survives all 24 proper-cubic frames",
        len(covariance) == 24 and max(covariance) < 3e-14,
        max(covariance),
    )

    carrier_rest_scalar = c219.rest_mass(c219.common_species(0.0))
    one_carrier_energy = projected_wave_energy(reference_state)
    extended_rest_scalars = np.asarray(
        (
            charge,
            charge + carrier_rest_scalar,
            charge + 2 * carrier_rest_scalar,
        )
    )
    q_only_fields = tuple(
        q_only_extension_field(23, value) for value in extended_rest_scalars
    )
    carrier_coordinates = np.asarray((0.0, one_carrier_energy, 2 * one_carrier_energy))
    check(
        "archive rails change the carrier ledger but not a Q-only source extension",
        carrier_coordinates[2] > carrier_coordinates[1] > carrier_coordinates[0]
        and np.ptp(extended_rest_scalars) < 2e-14
        and max(
            np.linalg.norm(field - q_only_fields[0])
            for field in q_only_fields[1:]
        )
        < 2e-14,
        {
            "extended_rest_scalars": extended_rest_scalars.tolist(),
            "carrier_wave_coordinates": carrier_coordinates.tolist(),
        },
    )

    alternative_fields = tuple(
        q_only_extension_field(23, charge + coordinate)
        for coordinate in carrier_coordinates
    )
    check(
        "an energy-weighted source alternative is computationally distinct but unselected",
        np.linalg.norm(alternative_fields[1] - alternative_fields[0]) > 1e-3
        and np.linalg.norm(alternative_fields[2] - alternative_fields[1]) > 1e-3,
        {
            "one_minus_zero": float(
                np.linalg.norm(alternative_fields[1] - alternative_fields[0])
            ),
            "two_minus_one": float(
                np.linalg.norm(alternative_fields[2] - alternative_fields[1])
            ),
        },
    )


def representation_and_scope_controls(reference_state: np.ndarray) -> None:
    phase_state = np.exp(0.37j) * reference_state
    check(
        "global presentation phase does not change the stiffness coordinate",
        abs(stiffness_coordinate(phase_state) - stiffness_coordinate(reference_state))
        < 3e-14,
    )

    spectator_zero = np.asarray((1.0, 0.0), dtype=complex)
    spectator_plus = np.asarray((1.0, 1.0), dtype=complex) / np.sqrt(2)
    species = c219.common_species(-0.3)
    charge = c219.rest_mass(species)
    abstract = (
        charge,
        charge * float(np.vdot(spectator_zero, spectator_zero).real),
        charge
        * float(np.vdot(spectator_zero, spectator_zero).real)
        * float(np.vdot(spectator_plus, spectator_plus).real),
    )
    check(
        "abstract logical spectators remain exactly redundancy invariant",
        max(abs(value - charge) for value in abstract) < 2e-14,
        abstract,
    )

    eigenvalues = np.linalg.eigvalsh(c216.stiffness(np.asarray((0.41, -0.23, 0.17))))
    check(
        "the stiffness coordinate is positive but is not silently named a Hamiltonian",
        float(np.min(eigenvalues)) > -2e-12
        and stiffness_coordinate(reference_state) > 0,
        {
            "minimum_mode_stiffness": float(np.min(eigenvalues)),
            "packet_stiffness": stiffness_coordinate(reference_state),
        },
    )


def main() -> int:
    global PASS, FAIL
    PASS = FAIL = 0
    note_contract()
    reference_state, _ = massless_carrier_controls()
    exact_compact_and_normalization_controls()
    acoustic_and_hidden_mode_controls()
    covariance_and_encoding_controls(reference_state)
    massive_kinetic_and_archive_controls(reference_state)
    representation_and_scope_controls(reference_state)
    print(f"SUMMARY {PASS} passed, {FAIL} failed")
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
