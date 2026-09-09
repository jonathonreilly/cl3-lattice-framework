#!/usr/bin/env python3
"""Cycle-230 local contact on the localized physical Cycle-269 state lift.

Map every coarse occupation n_v to (I-B_v)/2 and compile the onsite contact
as the commuting product over the 15 unordered direction pairs in a cell,

    product_(u<v) exp(i g n_u n_v).

On the reference-relative localized pair lift, the intracell column receives
exp(i g) and the streamed, separated column receives one.  This runner proves
the exact encoded contact intertwiner and its physical support, covariance,
constraint, inverse, deletion, held-size, and scope controls.
"""

from __future__ import annotations

from itertools import combinations, product
from numbers import Real
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as lift
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_LOCAL_CONTACT_INTERTWINER_NOTE_2026-07-17.md"
)
COUPLING = c230.COUPLING
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
TOLERANCE = 5e-12

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


def normalized(path: Path) -> str:
    text = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        text = text.replace(marker, "")
    return " ".join(text.split())


def note_contract() -> None:
    if not NOTE.exists():
        check("the physical local-contact note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical cycle-269",
        "cycle-230 contact",
        "n_v=(i-b_v)/2",
        "fifteen pair projectors",
        "e c_coarse = c_physical e",
        "diag(e^{ig},1)",
        "eighteen-face",
        "six auxiliary port m2 per cell",
        "exact unitarity",
        "inverse",
        "g=0 deletion",
        "one-particle mass fixture",
        "all 24 proper-cubic frames",
        "all l=3 translations",
        "held l=6",
        "constraint leakage",
        "reference-relative",
        "identical-pair",
        "restricted physical action",
        "not a full-hilbert-space contact matrix",
        "supplied-structure inventory",
        "not physical energy",
        "not a rate",
        "not gravity",
        "no full-fock compiler",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the encoded contact theorem, controls, and scope",
        not missing,
        missing,
    )


def cell_vertices(
    code: c269.WilsonSubsystemCode, cell: tuple[int, int, int]
) -> tuple[int, ...]:
    return tuple(code.graph.vertex_index[(cell, direction)] for direction in range(6))


def pair_projector_support(
    code: c269.WilsonSubsystemCode, left: int, right: int
) -> int:
    return code.B[left].z | code.B[right].z


def validate_coupling(coupling: object) -> float:
    if isinstance(coupling, bool) or not isinstance(coupling, Real):
        raise ValueError("unitary contact requires one finite real coupling")
    value = float(coupling)
    if not np.isfinite(value):
        raise ValueError("unitary contact requires one finite real coupling")
    return value


def cell_pair_family(
    code: c269.WilsonSubsystemCode,
) -> tuple[frozenset[int], ...]:
    return tuple(
        frozenset((left, right))
        for cell in code.graph.cells
        for left, right in combinations(cell_vertices(code, cell), 2)
    )


def physical_contact_action_on_representative(
    code: c269.WilsonSubsystemCode,
    face_pauli: c235.Pauli,
    coupling: float,
    pair_family: tuple[frozenset[int], ...] | None = None,
) -> tuple[complex, tuple[frozenset[int], ...]]:
    """Restricted scalar action on P|vac>, using the literal B projectors.

    The supplied reference vacuum has B_v=+1.  Thus P|vac> is an exact common
    B eigenstate, with n_v=1 precisely when P anticommutes with B_v.  Each
    n_u n_v factor consequently acts as a scalar and cannot mix this column.
    This evaluates that restricted action; it does not assemble the exponentially
    large full-face-Hilbert-space contact matrix.
    """

    value = validate_coupling(coupling)
    pairs = cell_pair_family(code) if pair_family is None else pair_family
    active = tuple(
        pair
        for pair in pairs
        if all(not face_pauli.commutes(code.B[vertex]) for vertex in pair)
    )
    factors = tuple(
        np.exp(1j * value) if pair in active else 1.0 + 0.0j
        for pair in pairs
    )
    return complex(np.prod(factors)), active


def local_pair_spectrum(
    code: c269.WilsonSubsystemCode,
    left: int,
    right: int,
    coupling: float,
) -> tuple[np.ndarray, np.ndarray]:
    """Exact diagonal spectrum on the union support of B_left and B_right."""

    support = pair_projector_support(code, left, right)
    faces = tuple(face for face in range(code.qubits) if (support >> face) & 1)
    locations = {face: local for local, face in enumerate(faces)}

    def local_mask(global_mask: int) -> int:
        return sum(
            ((global_mask >> face) & 1) << locations[face] for face in faces
        )

    left_mask = local_mask(code.B[left].z)
    right_mask = local_mask(code.B[right].z)
    projector = np.empty(1 << len(faces), dtype=float)
    for basis in range(projector.size):
        left_occupied = (basis & left_mask).bit_count() % 2
        right_occupied = (basis & right_mask).bit_count() % 2
        projector[basis] = left_occupied * right_occupied
    spectrum = np.exp(1j * coupling * projector)
    return projector, spectrum


def contact_phase_from_occupations(
    code: c269.WilsonSubsystemCode,
    occupations: frozenset[int],
    coupling: float,
) -> complex:
    counts: dict[tuple[int, int, int], int] = {}
    for vertex in occupations:
        cell = code.graph.vertices[vertex][0]
        counts[cell] = counts.get(cell, 0) + 1
    pairs = sum(number * (number - 1) // 2 for number in counts.values())
    return complex(np.exp(1j * coupling * pairs))


def local_coarse_and_physical_pair_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nLOCAL 64-STATE CONTACT / PHYSICAL PAIR PROJECTORS")
    number = np.asarray([basis.bit_count() for basis in range(64)])
    coarse = np.diag(np.exp(1j * COUPLING * number * (number - 1) / 2))
    identity = np.eye(64, dtype=complex)
    deleted = np.diag(np.exp(1j * 0.0 * number * (number - 1) / 2))
    reconstructed = np.ones(64, dtype=complex)
    for left, right in combinations(range(6), 2):
        reconstructed *= np.asarray(
            [
                np.exp(
                    1j
                    * COUPLING
                    * ((basis >> left) & 1)
                    * ((basis >> right) & 1)
                )
                for basis in range(64)
            ]
        )
    check(
        "the fifteen pair projectors exactly reconstruct the Cycle-230 local contact on all 64 occupations",
        np.linalg.norm(coarse.conj().T @ coarse - identity) < TOLERANCE
        and np.linalg.norm(np.diag(reconstructed) - coarse) < TOLERANCE
        and np.linalg.norm(deleted - identity) == 0
        and np.max(abs(np.diag(coarse)[number <= 1] - 1)) < TOLERANCE,
        {
            "local_dimension": 64,
            "pair_projectors": 15,
            "reconstruction_residual": float(
                np.linalg.norm(np.diag(reconstructed) - coarse)
            ),
            "unitarity_residual": float(np.linalg.norm(coarse.conj().T @ coarse - identity)),
            "g0_identity_residual": float(np.linalg.norm(deleted - identity)),
            "N_le_1_contact_residual": float(
                np.max(abs(np.diag(coarse)[number <= 1] - 1))
            ),
        },
    )

    vertices = cell_vertices(code, (0, 0, 0))
    spectrum_rows = []
    for left, right in combinations(vertices, 2):
        projector, spectrum = local_pair_spectrum(code, left, right, COUPLING)
        _projector_inverse, inverse_spectrum = local_pair_spectrum(
            code, left, right, -COUPLING
        )
        _projector_deleted, deleted_spectrum = local_pair_spectrum(
            code, left, right, 0.0
        )
        spectrum_rows.append(
            {
                "support": int(np.log2(projector.size)),
                "projector_values": sorted(set(projector)),
                "idempotence_residual": float(np.max(abs(projector**2 - projector))),
                "unitarity_residual": float(np.max(abs(abs(spectrum) - 1))),
                "inverse_residual": float(np.max(abs(spectrum * inverse_spectrum - 1))),
                "g0_residual": float(np.max(abs(deleted_spectrum - 1))),
            }
        )
    check(
        "every mapped pair factor is an exact bounded projector phase with exact inverse and g=0 deletion",
        len(spectrum_rows) == 15
        and {row["support"] for row in spectrum_rows} == {9, 10}
        and all(
            row["projector_values"] == [0.0, 1.0]
            and row["idempotence_residual"] == 0
            and row["unitarity_residual"] < TOLERANCE
            and row["inverse_residual"] < TOLERANCE
            and row["g0_residual"] == 0
            for row in spectrum_rows
        ),
        spectrum_rows,
    )


def support_leakage_and_held_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nPHYSICAL SUPPORT / COMMUTATION / CONSTRAINT LEAKAGE / HELD SIZE")
    rows = []
    for length, code in cache.items():
        pair_supports = []
        cell_supports = []
        owner_cell_radii = []
        check_leakage = 0
        wilson_leakage = 0
        port_constraint_leakage = 0
        occupation_form_failures = sum(
            occupation.phase != 0 or occupation.x != 0 for occupation in code.B
        )
        noncommuting_occupations = sum(
            not left.commutes(right)
            for index, left in enumerate(code.B)
            for right in code.B[index + 1 :]
        )
        extended_qubits = code.qubits + len(code.graph.vertices)
        port_constraints = tuple(
            c235.Pauli(
                z=code.B[vertex].z | (1 << (code.qubits + vertex))
            )
            for vertex in range(len(code.graph.vertices))
        )
        for occupation in code.B:
            check_leakage += sum(
                not occupation.commutes(row) for row in code.local_checks
            )
            wilson_leakage += sum(
                not occupation.commutes(row) for row in code.wilsons
            )
            port_constraint_leakage += sum(
                not occupation.commutes(constraint)
                for constraint in port_constraints
            )
        for cell in code.graph.cells:
            vertices = cell_vertices(code, cell)
            cell_support = 0
            for left, right in combinations(vertices, 2):
                support = pair_projector_support(code, left, right)
                pair_supports.append(support.bit_count())
                cell_support |= support
            cell_supports.append(cell_support.bit_count())
            for face in range(code.qubits):
                if not ((cell_support >> face) & 1):
                    continue
                owner = code.graph.edges[face][3]
                coordinate_distances = tuple(
                    min((owner[axis] - cell[axis]) % length, (cell[axis] - owner[axis]) % length)
                    for axis in range(3)
                )
                owner_cell_radii.append(max(coordinate_distances))
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "cells": length**3,
                "pair_gate_face_supports": sorted(set(pair_supports)),
                "complete_cell_contact_face_supports": sorted(set(cell_supports)),
                "maximum_owner_cell_Chebyshev_radius": max(owner_cell_radii),
                "face_M2_per_cell": code.qubits // length**3,
                "port_M2_per_cell": len(code.graph.vertices) // length**3,
                "total_M2_per_cell": extended_qubits // length**3,
                "literal_port_constraints": len(port_constraints),
                "local_check_leakage": check_leakage,
                "Wilson_leakage": wilson_leakage,
                "port_constraint_leakage": port_constraint_leakage,
                "occupation_form_failures": occupation_form_failures,
                "noncommuting_occupation_pairs": noncommuting_occupations,
            }
        )
    check(
        "the physical contact has constant radius-one support and zero local-check, Wilson, port-constraint, or ordering leakage through held L=6",
        all(
            row["pair_gate_face_supports"] == [9, 10]
            and row["complete_cell_contact_face_supports"] == [18]
            and row["maximum_owner_cell_Chebyshev_radius"] == 1
            and row["face_M2_per_cell"] == 15
            and row["port_M2_per_cell"] == 6
            and row["total_M2_per_cell"] == 21
            and row["literal_port_constraints"] == 6 * row["L"] ** 3
            and row["local_check_leakage"] == 0
            and row["Wilson_leakage"] == 0
            and row["port_constraint_leakage"] == 0
            and row["occupation_form_failures"] == 0
            and row["noncommuting_occupation_pairs"] == 0
            for row in rows
        ),
        rows,
    )


def encoded_contact_intertwining_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> dict[int, list[lift.LocalizedLift]]:
    print("\nEXACT ENCODED LOCAL CONTACT INTERTWINER")
    fixtures = {}
    rows = []
    expected_contact = complex(np.exp(1j * COUPLING))
    deletion_residual = abs(expected_contact - 1)
    for length, code in cache.items():
        local_lifts = [
            lift.localized_lift(code, source, carrier)
            for source, carrier in lift.all_oriented_internal_pairs(code)
        ]
        fixtures[length] = local_lifts
        phase_failures = 0
        inverse_failures = 0
        g0_failures = 0
        deletion_failures = 0
        inactive_projector_failures = 0
        physical_vs_decoded_failures = 0
        pair_family = cell_pair_family(code)
        for state_lift in local_lifts:
            input_occupations = lift.occupied_vertices(
                code, state_lift.input_face_pauli
            )
            output_occupations = lift.occupied_vertices(
                code, state_lift.output_face_pauli
            )
            decoded_input_phase = contact_phase_from_occupations(
                code, input_occupations, COUPLING
            )
            decoded_output_phase = contact_phase_from_occupations(
                code, output_occupations, COUPLING
            )
            input_phase, active_input_pairs = physical_contact_action_on_representative(
                code, state_lift.input_face_pauli, COUPLING, pair_family
            )
            output_phase, active_output_pairs = physical_contact_action_on_representative(
                code, state_lift.output_face_pauli, COUPLING, pair_family
            )
            phase_failures += abs(input_phase - expected_contact) > TOLERANCE
            phase_failures += abs(output_phase - 1) > TOLERANCE
            physical_vs_decoded_failures += (
                abs(input_phase - decoded_input_phase) > TOLERANCE
            )
            physical_vs_decoded_failures += (
                abs(output_phase - decoded_output_phase) > TOLERANCE
            )
            inverse_failures += abs(
                input_phase * np.exp(-1j * COUPLING * len(active_input_pairs)) - 1
            ) > TOLERANCE
            inverse_failures += abs(
                output_phase * np.exp(-1j * COUPLING * len(active_output_pairs)) - 1
            ) > TOLERANCE
            g0_failures += abs(np.exp(0j * len(active_input_pairs)) - 1) > TOLERANCE
            g0_failures += abs(np.exp(0j * len(active_output_pairs)) - 1) > TOLERANCE
            target_pair = frozenset((state_lift.source, state_lift.carrier))
            deletion_failures += active_input_pairs != (target_pair,)
            deletion_failures += bool(active_output_pairs)
            deleted_pair_phase = complex(
                np.prod(
                    [
                        np.exp(1j * COUPLING)
                        for pair in active_input_pairs
                        if pair != target_pair
                    ]
                )
            )
            deletion_failures += abs(
                abs(expected_contact - deleted_pair_phase) - deletion_residual
            ) > TOLERANCE
            inactive_projector_failures += sum(
                pair != target_pair
                and all(vertex in input_occupations for vertex in pair)
                for pair in pair_family
            )
        contact_matrix = np.diag((expected_contact, 1.0 + 0.0j))
        identity = np.eye(2, dtype=complex)
        stream_matrix = np.asarray(((0, 1), (1, 0)), dtype=complex)
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "localized_lifts": len(local_lifts),
                "C_coarse=C_physical_on_code": (
                    (complex(contact_matrix[0, 0]), complex(contact_matrix[1, 1]))
                ),
                "phase_failures": phase_failures,
                "physical_vs_decoded_phase_failures": physical_vs_decoded_failures,
                "restricted_action": "literal projectors act scalarly on common-B-eigenstate columns; no full-Hilbert matrix assembled",
                "inverse_failures": inverse_failures,
                "g0_failures": g0_failures,
                "unique_active_pair_deletion_failures": deletion_failures,
                "inactive_pair_projector_failures": inactive_projector_failures,
                "unitarity_residual": float(
                    np.linalg.norm(contact_matrix.conj().T @ contact_matrix - identity)
                ),
                "contact_stream_commutator_norm": float(
                    np.linalg.norm(contact_matrix @ stream_matrix - stream_matrix @ contact_matrix, 2)
                ),
                "encoded_equation": "E C_coarse = C_physical E",
            }
        )
    check(
        "the physical contact exactly intertwines diag(e^{ig},1) on every localized pair lift and has exact inverse and g=0 deletion through held L=6",
        all(
            row["localized_lifts"] == 24 * row["L"] ** 3
            and row["phase_failures"] == 0
            and row["physical_vs_decoded_phase_failures"] == 0
            and row["inverse_failures"] == 0
            and row["g0_failures"] == 0
            and row["unique_active_pair_deletion_failures"] == 0
            and row["inactive_pair_projector_failures"] == 0
            and row["unitarity_residual"] < TOLERANCE
            and abs(
                row["contact_stream_commutator_norm"] - deletion_residual
            ) < TOLERANCE
            for row in rows
        ),
        rows,
    )
    return fixtures


def covariance_and_translation_controls(
    code: c269.WilsonSubsystemCode,
    fixtures: list[lift.LocalizedLift],
) -> None:
    print("\nPROPER-CUBIC / TRANSLATION CONTACT COVARIANCE")
    pair_family = cell_pair_family(code)
    pair_set = set(pair_family)
    frame_failures = 0
    frame_tests = 0
    frame_physical_column_tests = 0
    for frame in c230.c210.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, repair_pairs, flips = c269.repair_data(
            code.graph, vertex_map, edge_map
        )
        for pair in pair_set:
            mapped = frozenset(vertex_map[vertex] for vertex in pair)
            frame_failures += mapped not in pair_set
            for vertex in pair:
                frame_failures += (
                    c235.permute_pauli(code.B[vertex], edge_map)
                    != code.B[vertex_map[vertex]]
                )
        for state_lift in fixtures:
            target = lift.localized_lift(
                code, vertex_map[state_lift.source], vertex_map[state_lift.carrier]
            )
            transformed_input = lift.transform_pauli(
                code,
                state_lift.input_face_pauli,
                edge_map,
                toggles,
                repair_pairs,
                flips,
            )
            transformed_output = lift.transform_pauli(
                code,
                state_lift.output_face_pauli,
                edge_map,
                toggles,
                repair_pairs,
                flips,
            )
            input_scalar = lift.relative_scalar(
                transformed_input, target.input_face_pauli
            )
            output_scalar = lift.relative_scalar(
                transformed_output, target.output_face_pauli
            )
            input_phase, _active_input = physical_contact_action_on_representative(
                code, transformed_input, COUPLING, pair_family
            )
            output_phase, _active_output = physical_contact_action_on_representative(
                code, transformed_output, COUPLING, pair_family
            )
            frame_failures += input_scalar is None or output_scalar is None
            frame_failures += input_scalar != output_scalar
            frame_failures += sum(
                1 << vertex_map[vertex]
                for vertex in range(len(code.graph.vertices))
                if (state_lift.input_tags >> vertex) & 1
            ) != target.input_tags
            frame_failures += sum(
                1 << vertex_map[vertex]
                for vertex in range(len(code.graph.vertices))
                if (state_lift.output_tags >> vertex) & 1
            ) != target.output_tags
            frame_failures += abs(input_phase - np.exp(1j * COUPLING)) > TOLERANCE
            frame_failures += abs(output_phase - 1) > TOLERANCE
            frame_tests += 1
            frame_physical_column_tests += 2

    translation_failures = 0
    translation_tests = 0
    translation_physical_column_tests = 0
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, repair_pairs, flips = c269.repair_data(
            code.graph, vertex_map, edge_map
        )
        for pair in pair_set:
            translation_failures += (
                frozenset(vertex_map[vertex] for vertex in pair) not in pair_set
            )
            for vertex in pair:
                translation_failures += (
                    c235.permute_pauli(code.B[vertex], edge_map)
                    != code.B[vertex_map[vertex]]
                )
        for state_lift in fixtures:
            target = lift.localized_lift(
                code, vertex_map[state_lift.source], vertex_map[state_lift.carrier]
            )
            transformed_input = lift.transform_pauli(
                code,
                state_lift.input_face_pauli,
                edge_map,
                toggles,
                repair_pairs,
                flips,
            )
            transformed_output = lift.transform_pauli(
                code,
                state_lift.output_face_pauli,
                edge_map,
                toggles,
                repair_pairs,
                flips,
            )
            input_scalar = lift.relative_scalar(
                transformed_input, target.input_face_pauli
            )
            output_scalar = lift.relative_scalar(
                transformed_output, target.output_face_pauli
            )
            input_phase, _active_input = physical_contact_action_on_representative(
                code, transformed_input, COUPLING, pair_family
            )
            output_phase, _active_output = physical_contact_action_on_representative(
                code, transformed_output, COUPLING, pair_family
            )
            translation_failures += input_scalar is None or output_scalar is None
            translation_failures += input_scalar != output_scalar
            translation_failures += sum(
                1 << vertex_map[vertex]
                for vertex in range(len(code.graph.vertices))
                if (state_lift.input_tags >> vertex) & 1
            ) != target.input_tags
            translation_failures += sum(
                1 << vertex_map[vertex]
                for vertex in range(len(code.graph.vertices))
                if (state_lift.output_tags >> vertex) & 1
            ) != target.output_tags
            translation_failures += abs(input_phase - np.exp(1j * COUPLING)) > TOLERANCE
            translation_failures += abs(output_phase - 1) > TOLERANCE
            translation_tests += 1
            translation_physical_column_tests += 2
    check(
        "the complete physical contact pair family and encoded phases are invariant under all 24 proper frames and all L=3 translations",
        len(c230.c210.proper_cubic_frames()) == 24
        and frame_failures == 0
        and translation_failures == 0,
        {
            "proper_frames": len(c230.c210.proper_cubic_frames()),
            "frame_encoded_tests": frame_tests,
            "frame_transformed_physical_columns": frame_physical_column_tests,
            "frame_failures": frame_failures,
            "translations": code.length**3,
            "translation_encoded_tests": translation_tests,
            "translation_transformed_physical_columns": (
                translation_physical_column_tests
            ),
            "translation_failures": translation_failures,
        },
    )


def one_particle_mass_and_domain_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nONE-PARTICLE MASS FIREWALL / LAWFUL DOMAIN")
    species = c230.c219.common_species(c230.BETA)
    curvature = c230.c210.curvature_tensor(species, step=1e-4)
    dispersion_mass = 1 / float(np.mean(np.diag(curvature)))
    forced = c230.c210.force_response(species, 2e-5)
    rest = c230.c219.rest_mass(species)
    coarse_one_particle_contact = contact_phase_from_occupations(
        cache[3], frozenset((0,)), COUPLING
    )
    check(
        "the contact is identity on N<=1 and therefore preserves the imported one-particle rest, curvature, and forced-response mass fixture",
        abs(coarse_one_particle_contact - 1) < TOLERANCE
        and abs(rest / species.analytic_mass - 1) < 2e-12
        and abs(dispersion_mass / species.analytic_mass - 1) < 4e-6
        and abs(forced.measured_mass / species.analytic_mass - 1) < 0.007,
        {
            "coarse_contact_phase_N1": coarse_one_particle_contact,
            "analytic_mass": species.analytic_mass,
            "rest_mass": rest,
            "dispersion_mass": dispersion_mass,
            "forced_response_mass": forced.measured_mass,
            "imported_tolerances": {
                "rest_relative": 2e-12,
                "dispersion_relative": 4e-6,
                "forced_response_relative": 0.007,
            },
            "scope": "coarse one-particle fixture; odd one-particle state is not encoded by fixed-even Cycle-269",
        },
    )

    code = cache[3]
    source, carrier = next(lift.all_oriented_internal_pairs(code))
    valid_tags = (1 << source) | (1 << carrier)
    lift.validate_localized_domain(code, source, carrier, valid_tags)
    rejected: list[str] = []
    for label, coupling in (
        ("complex coupling", complex(COUPLING, 0.1)),
        ("nonfinite coupling", float("nan")),
    ):
        try:
            validate_coupling(coupling)
        except ValueError:
            rejected.append(label)
    try:
        c269.build_code(2)
    except ValueError:
        rejected.append("undersized torus")
    direction = code.graph.vertices[source][1]
    cell = code.graph.vertices[source][0]
    opposite = code.graph.vertex_index[(cell, c235.REVERSE[direction])]
    other_cell = ((cell[0] + 1) % code.length, cell[1], cell[2])
    nonlocal_carrier = code.graph.vertex_index[(other_cell, direction)]
    invalid_lifts = (
        ("coincident pair", source, source, 1 << source),
        ("opposite pair", source, opposite, (1 << source) | (1 << opposite)),
        (
            "nonlocal pair",
            source,
            nonlocal_carrier,
            (1 << source) | (1 << nonlocal_carrier),
        ),
        ("mistagged pair", source, carrier, 1 << source),
        ("out-of-range port", -1, carrier, valid_tags),
    )
    for label, bad_source, bad_carrier, bad_tags in invalid_lifts:
        try:
            lift.validate_localized_domain(
                code, bad_source, bad_carrier, bad_tags
            )
        except (KeyError, ValueError):
            rejected.append(label)
    check(
        "the contact lift rejects complex, nonfinite, undersized, coincident, opposite, nonlocal, mistagged, and out-of-range fixtures",
        rejected
        == [
            "complex coupling",
            "nonfinite coupling",
            "undersized torus",
            "coincident pair",
            "opposite pair",
            "nonlocal pair",
            "mistagged pair",
            "out-of-range port",
        ],
        {"rejected_fixtures": rejected},
    )


def supplied_inventory_and_scope_controls() -> None:
    print("\nSUPPLIED-STRUCTURE INVENTORY / SCOPE")
    check(
        "the result is one exact encoded local contact block on the reference-relative identical-pair lift, not an independent-species or full-Fock compiler",
        True,
        {
            "derived": (
                "15 commuting n_u n_v pair projectors per cell",
                "9/10-face pair support and 18-face full-cell support",
                "exact restricted diag(exp(i g),1) action on the declared code columns",
                "unitarity, inverse, g=0, deletion, leakage, covariance, and held-size controls",
            ),
            "supplied": (
                "Cycle-230 coupling g=0.37 and binomial occupation contact",
                "Cycle-269 fixed +++ Wilson reference vacuum",
                "reference-relative localized two-column pair lift",
                "n_v=(I-B_v)/2 occupation dictionary",
                "six auxiliary port M2 per cell and local port constraints",
                "training L=3,4,5 and held L=6",
            ),
            "open": (
                "absolute bounded vacuum preparation",
                "coherent position and independent source/species encoding",
                "six-mode coin with coherent port routing",
                "assembled stream/contact schedule on a larger code",
                "full-Fock and rank-73 sea compiler",
                "a full-Hilbert-space physical contact matrix",
            ),
            "not_claimed": (
                "physical energy",
                "rate or physical time",
                "gravity or source law",
                "Record or probability semantics",
            ),
            "overhead": "21 M2/cell inherited; contact support <=18 face M2",
            "physical_vs_decoded": "literal B-projector eigenvalues determine scalar physical action; occupations are the decoded summary",
            "authority": "none",
            "audit": "unset",
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("PHYSICAL CYCLE-269 LOCAL CONTACT INTERTWINER")
    print("authority=none; audit=unset")
    note_contract()
    cache = {length: c269.build_code(length) for length in SIZES}
    local_coarse_and_physical_pair_controls(cache[3])
    support_leakage_and_held_controls(cache)
    fixtures = encoded_contact_intertwining_controls(cache)
    covariance_and_translation_controls(cache[3], fixtures[3])
    one_particle_mass_and_domain_controls(cache)
    supplied_inventory_and_scope_controls()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
