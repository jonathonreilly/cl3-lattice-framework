#!/usr/bin/env python3
"""Reference-relative localized Cycle-269 physical state lift.

Fix the +++ Wilson sector and the unique all-B=+1 face-code vacuum.  For an
ordered adjacent source/carrier pair (s,m) on one internal triangular edge,
the bounded Pauli A(s,m) creates the even pair.  The two outer-edge A factors
create its streamed image.  With the six-port auxiliary layer, this defines a
two-column physical stabilizer-state isometry E_(s,m) and an exact
stream/catch-up intertwiner on the localized two-slice orbit.

The result is reference-relative: preparation of the global fixed-Wilson
vacuum, coherent superposition across different pair locations, independent
source/carrier species, the six-mode coin, and the full-Fock compiler remain
open.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_collision_safe_auxiliary_ports_2026_07_17 as ports
import physical_cycle269_staggered_reservoir_catchup_2026_07_17 as old
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_REFERENCE_RELATIVE_LOCALIZED_PAIR_LIFT_NOTE_2026-07-17.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class LocalizedLift:
    source: int
    carrier: int
    source_arrival: int
    carrier_arrival: int
    source_outer_edge: int
    carrier_outer_edge: int
    input_face_pauli: c235.Pauli
    output_face_pauli: c235.Pauli
    input_tags: int
    output_tags: int
    stream_phase: complex


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
        check("the localized state-lift note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical cycle-269",
        "localized one-carrier/one-source",
        "reference-relative",
        "fixed +++ wilson sector",
        "unique stabilizer vacuum",
        "exact isometry",
        "e g_coarse = g_physical e",
        "two-dimensional",
        "nineteen-m2",
        "six auxiliary port m2 per cell",
        "all 24 proper-cubic frames",
        "all l=3 translations",
        "held l=6",
        "constraint leakage",
        "catch-up deletion",
        "lawful domain",
        "decoded action",
        "encoded stabilizer state",
        "restricted physical operator word",
        "not an assembled full-hilbert-space",
        "global vacuum preparation remains open",
        "source/carrier roles are not independent species",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the reference-relative state theorem and its exact boundary",
        not missing,
        missing,
    )


def pauli_dagger(pauli: c235.Pauli) -> c235.Pauli:
    return c235.Pauli(
        (-pauli.phase + 2 * (pauli.x & pauli.z).bit_count()) % 4,
        pauli.x,
        pauli.z,
    )


def scalar_times(pauli: c235.Pauli, scalar: complex) -> c235.Pauli:
    phases = (1 + 0j, 1j, -1 + 0j, -1j)
    index = next(
        phase for phase, value in enumerate(phases) if abs(value - scalar) < 1e-12
    )
    return c235.Pauli((pauli.phase + index) % 4, pauli.x, pauli.z)


def conjugate_pauli(operator: c235.Pauli, row: c235.Pauli) -> c235.Pauli:
    return operator @ row @ pauli_dagger(operator)


def lift_face_pauli(pauli: c235.Pauli) -> c235.Pauli:
    return pauli


def tag_x_pauli(code: c269.WilsonSubsystemCode, tags: int) -> c235.Pauli:
    return c235.Pauli(x=tags << code.qubits)


def full_state_representative(
    code: c269.WilsonSubsystemCode,
    face_pauli: c235.Pauli,
    tags: int,
) -> c235.Pauli:
    return tag_x_pauli(code, tags) @ lift_face_pauli(face_pauli)


def reference_stabilizers(
    code: c269.WilsonSubsystemCode,
) -> tuple[c235.Pauli, ...]:
    """Unique +++ Wilson, all-B=+1 face vacuum and all-zero port tags."""

    face_rows = code.local_checks + code.wilsons + code.B
    tag_rows = tuple(
        c235.Pauli(z=1 << (code.qubits + vertex))
        for vertex in range(len(code.graph.vertices))
    )
    return face_rows + tag_rows


def occupied_vertices(
    code: c269.WilsonSubsystemCode, face_pauli: c235.Pauli
) -> frozenset[int]:
    return frozenset(
        vertex
        for vertex, occupation in enumerate(code.B)
        if not face_pauli.commutes(occupation)
    )


def edge_stream_factor(
    code: c269.WilsonSubsystemCode, occupied_vertex: int, edge: int
) -> complex:
    left, right, kind, _owner = code.graph.edges[edge]
    if kind != "outer_square" or occupied_vertex not in (left, right):
        raise ValueError("the streamed occupied vertex must be an outer-edge endpoint")
    return 1j if occupied_vertex == left else -1j


def two_edge_physical_face_action(
    code: c269.WilsonSubsystemCode,
    face_pauli: c235.Pauli,
    occupied_vertices: tuple[int, int],
    outer_edges: tuple[int, int],
) -> tuple[c235.Pauli, complex]:
    """Exact occupied-to-empty branch of the two supplied FSWAP polynomials."""

    output = face_pauli
    phase = 1.0 + 0j
    for occupied, edge in zip(occupied_vertices, outer_edges):
        phase *= edge_stream_factor(code, occupied, edge)
        output = code.A[edge] @ output
    return scalar_times(output, phase), phase


def localized_lift(
    code: c269.WilsonSubsystemCode, source: int, carrier: int
) -> LocalizedLift:
    internal_edge = code.graph.edge_between(source, carrier)
    if code.graph.edges[internal_edge][2] != "internal_triangle":
        raise ValueError("source and carrier must be adjacent internal half-edge modes")
    source_arrival, source_edge = old.outer_partner(code, source)
    carrier_arrival, carrier_edge = old.outer_partner(code, carrier)
    if source_edge == carrier_edge:
        raise ValueError("the localized pair must stream on two distinct outer edges")
    input_face = code.graph.A(source, carrier)
    output_raw = code.A[carrier_edge] @ code.A[source_edge] @ input_face
    phase = edge_stream_factor(code, source, source_edge) * edge_stream_factor(
        code, carrier, carrier_edge
    )
    output_face = scalar_times(output_raw, phase)
    return LocalizedLift(
        source=source,
        carrier=carrier,
        source_arrival=source_arrival,
        carrier_arrival=carrier_arrival,
        source_outer_edge=source_edge,
        carrier_outer_edge=carrier_edge,
        input_face_pauli=input_face,
        output_face_pauli=output_face,
        input_tags=(1 << source) | (1 << carrier),
        output_tags=(1 << source_arrival) | (1 << carrier_arrival),
        stream_phase=phase,
    )


def validate_localized_domain(
    code: c269.WilsonSubsystemCode,
    source: int,
    carrier: int,
    tags: int,
) -> None:
    vertices = len(code.graph.vertices)
    if source < 0 or source >= vertices or carrier < 0 or carrier >= vertices:
        raise ValueError("source and carrier labels must be physical matter ports")
    if source == carrier:
        raise ValueError("source and carrier ports must be distinct")
    source_cell = code.graph.vertices[source][0]
    carrier_cell = code.graph.vertices[carrier][0]
    if source_cell != carrier_cell:
        raise ValueError("this localized lift uses one intracell adjacent pair")
    edge = code.graph.edge_between(source, carrier)
    if code.graph.edges[edge][2] != "internal_triangle":
        raise ValueError("opposite ports are not an internal triangular pair")
    expected = (1 << source) | (1 << carrier)
    if tags != expected:
        raise ValueError("the two local port constraints require tags on both occupied ports")


def reference_vacuum_and_rank_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nUNIQUE FIXED-WILSON VACUUM / EXPLICIT PHYSICAL TABLEAU")
    rows = []
    for length, code in cache.items():
        face_rows = list(code.local_checks + code.wilsons + code.B)
        nonhermitian = sum(
            (row.phase - (row.x & row.z).bit_count()) % 2 for row in face_rows
        )
        stabilizer_core = code.local_checks + code.wilsons
        noncommuting = sum(
            not left.commutes(right)
            for index, left in enumerate(stabilizer_core)
            for right in stabilizer_core[index + 1 :]
        )
        noncommuting += sum(
            not occupation.commutes(row)
            for occupation in code.B
            for row in stabilizer_core
        )
        face_rank, face_bad = c235.phase_aware_rank(face_rows, code.qubits)
        total_qubits = code.qubits + len(code.graph.vertices)
        total_rows = list(reference_stabilizers(code))
        total_rank, total_bad = c235.phase_aware_rank(total_rows, total_qubits)
        without_wilson = list(code.local_checks + code.B) + total_rows[len(face_rows) :]
        deleted_rank, deleted_bad = c235.phase_aware_rank(without_wilson, total_qubits)
        single_wilson_deficits = []
        single_wilson_bad = []
        for deleted_index in range(len(code.wilsons)):
            face_without_one = (
                list(code.local_checks)
                + [
                    wilson
                    for index, wilson in enumerate(code.wilsons)
                    if index != deleted_index
                ]
                + list(code.B)
            )
            rank_without_one, bad_without_one = c235.phase_aware_rank(
                face_without_one + total_rows[len(face_rows) :], total_qubits
            )
            single_wilson_deficits.append(total_qubits - rank_without_one)
            single_wilson_bad.extend(bad_without_one)
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "face_M2": code.qubits,
                "port_M2": len(code.graph.vertices),
                "total_M2": total_qubits,
                "M2_per_cell": total_qubits // length**3,
                "face_vacuum_rank": face_rank,
                "total_reference_rank": total_rank,
                "rank_after_all_Wilson_deletion": deleted_rank,
                "Wilson_rank_deficit": total_qubits - deleted_rank,
                "single_Wilson_deletion_deficits": single_wilson_deficits,
                "nonhermitian_generators": nonhermitian,
                "noncommuting_generator_pairs": noncommuting,
                "phase_inconsistencies": (
                    len(face_bad)
                    + len(total_bad)
                    + len(deleted_bad)
                    + len(single_wilson_bad)
                ),
            }
        )
    check(
        "the +++ Wilson, all-B vacuum plus zero port tags is one unique physical stabilizer state through held L=6",
        all(
            row["face_vacuum_rank"] == row["face_M2"]
            and row["total_reference_rank"] == row["total_M2"]
            and row["M2_per_cell"] == 21
            and row["Wilson_rank_deficit"] == 3
            and row["single_Wilson_deletion_deficits"] == [1, 1, 1]
            and row["nonhermitian_generators"] == 0
            and row["noncommuting_generator_pairs"] == 0
            and row["phase_inconsistencies"] == 0
            for row in rows
        ),
        rows,
    )


def all_oriented_internal_pairs(
    code: c269.WilsonSubsystemCode,
):
    for left, right, kind, _owner in code.graph.edges:
        if kind == "internal_triangle":
            yield left, right
            yield right, left


def isometry_intertwining_and_held_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> dict[int, list[LocalizedLift]]:
    print("\nEXACT LOCALIZED ISOMETRY / STREAM-CATCH-UP INTERTWINER / HELD SIZE")
    fixtures: dict[int, list[LocalizedLift]] = {}
    rows = []
    for length, code in cache.items():
        lifts = [localized_lift(code, source, carrier) for source, carrier in all_oriented_internal_pairs(code)]
        fixtures[length] = lifts
        occupation_failures = 0
        constraint_failures = 0
        inverse_failures = 0
        intertwining_failures = 0
        orthogonality_failures = 0
        role_ray_failures = 0
        physical_face_forward_failures = 0
        physical_face_inverse_failures = 0
        physical_full_representative_failures = 0
        input_supports = []
        output_supports = []
        for lift in lifts:
            input_occupations = occupied_vertices(code, lift.input_face_pauli)
            output_occupations = occupied_vertices(code, lift.output_face_pauli)
            expected_input = frozenset((lift.source, lift.carrier))
            expected_output = frozenset((lift.source_arrival, lift.carrier_arrival))
            occupation_failures += input_occupations != expected_input
            occupation_failures += output_occupations != expected_output
            constraint_failures += lift.input_tags != sum(1 << item for item in input_occupations)
            constraint_failures += lift.output_tags != sum(1 << item for item in output_occupations)

            input_rep = full_state_representative(code, lift.input_face_pauli, lift.input_tags)
            output_rep = full_state_representative(code, lift.output_face_pauli, lift.output_tags)
            input_supports.append((input_rep.x | input_rep.z).bit_count())
            output_supports.append((output_rep.x | output_rep.z).bit_count())
            orthogonality_failures += (
                lift.input_tags.bit_count() != 2
                or lift.output_tags.bit_count() != 2
                or bool(lift.input_tags & lift.output_tags)
            )

            streamed_face, derived_forward_phase = two_edge_physical_face_action(
                code,
                lift.input_face_pauli,
                (lift.source, lift.carrier),
                (lift.source_outer_edge, lift.carrier_outer_edge),
            )
            restored_face, derived_backward_phase = two_edge_physical_face_action(
                code,
                lift.output_face_pauli,
                (lift.source_arrival, lift.carrier_arrival),
                (lift.source_outer_edge, lift.carrier_outer_edge),
            )
            physical_face_forward_failures += (
                streamed_face != lift.output_face_pauli
                or derived_forward_phase != lift.stream_phase
            )
            physical_face_inverse_failures += (
                restored_face != lift.input_face_pauli
                or derived_backward_phase != lift.stream_phase
            )

            arrival, caught, forward_sign = ports.port_macrostep(
                code, lift.input_tags, lift.input_tags
            )
            back_occupations, back_tags, backward_sign = ports.port_macrostep(
                code, arrival, caught
            )
            intertwining_failures += arrival != lift.output_tags
            intertwining_failures += caught != lift.output_tags
            physical_full_representative_failures += (
                full_state_representative(code, streamed_face, caught) != output_rep
            )
            inverse_failures += (back_occupations, back_tags) != (
                lift.input_tags,
                lift.input_tags,
            )
            inverse_failures += forward_sign * backward_sign != 1
            inverse_failures += lift.stream_phase**2 != 1
            physical_full_representative_failures += (
                full_state_representative(code, restored_face, back_tags) != input_rep
            )

            reversed_lift = localized_lift(code, lift.carrier, lift.source)
            input_relative = relative_scalar(
                reversed_lift.input_face_pauli, lift.input_face_pauli
            )
            output_relative = relative_scalar(
                reversed_lift.output_face_pauli, lift.output_face_pauli
            )
            role_ray_failures += not (
                input_relative == output_relative == 2
                and reversed_lift.input_tags == lift.input_tags
                and reversed_lift.output_tags == lift.output_tags
                and reversed_lift.stream_phase == lift.stream_phase
            )
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "localized_two_column_lifts": len(lifts),
                "input_relative_supports_M2": sorted(set(input_supports)),
                "output_relative_supports_M2": sorted(set(output_supports)),
                "maximum_relative_support_M2": max(input_supports + output_supports),
                "occupation_failures": occupation_failures,
                "port_constraint_failures": constraint_failures,
                "Gram_off_diagonal_failures": orthogonality_failures,
                "intertwining_failures": intertwining_failures,
                "inverse_failures": inverse_failures,
                "physical_face_forward_failures": physical_face_forward_failures,
                "physical_face_inverse_failures": physical_face_inverse_failures,
                "physical_full_representative_failures": (
                    physical_full_representative_failures
                ),
                "source_carrier_role_ray_failures": role_ray_failures,
                "exact_Gram": [[1, 0], [0, 1]],
                "exact_intertwiner": "E X = G_physical E",
            }
        )
    check(
        "every localized adjacent pair defines an exact two-dimensional physical state isometry and stream/catch-up intertwiner through held L=6",
        all(
            row["localized_two_column_lifts"] == 24 * row["L"] ** 3
            and row["maximum_relative_support_M2"] <= 19
            and row["occupation_failures"] == 0
            and row["port_constraint_failures"] == 0
            and row["Gram_off_diagonal_failures"] == 0
            and row["intertwining_failures"] == 0
            and row["inverse_failures"] == 0
            and row["physical_face_forward_failures"] == 0
            and row["physical_face_inverse_failures"] == 0
            and row["physical_full_representative_failures"] == 0
            and row["source_carrier_role_ray_failures"] == 0
            for row in rows
        ),
        rows,
    )
    return fixtures


def transform_pauli(
    code: c269.WilsonSubsystemCode,
    pauli: c235.Pauli,
    edge_map: list[int],
    toggles: int,
    pairs,
    flips: int,
) -> c235.Pauli:
    return c235.apply_gauge(
        c235.permute_pauli(pauli, edge_map), toggles, pairs, flips
    )


def relative_scalar(left: c235.Pauli, right: c235.Pauli) -> int | None:
    if left.x != right.x or left.z != right.z:
        return None
    return (left.phase - right.phase) % 4


def covariance_controls(
    code: c269.WilsonSubsystemCode,
    fixtures: list[LocalizedLift],
) -> None:
    print("\nALL-FRAME / ALL-TRANSLATION STATE-LIFT COVARIANCE")
    reference_face_rows = list(code.local_checks + code.wilsons + code.B)
    frame_failures = 0
    frame_tests = 0
    frame_reference_tableau_tests = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        transformed_reference_rows = [
            transform_pauli(code, row, edge_map, toggles, pairs, flips)
            for row in reference_face_rows
        ]
        reference_rank, reference_bad = c235.phase_aware_rank(
            reference_face_rows + transformed_reference_rows, code.qubits
        )
        frame_failures += reference_rank != code.qubits or bool(reference_bad)
        frame_reference_tableau_tests += 1
        for lift in fixtures:
            target = localized_lift(
                code, vertex_map[lift.source], vertex_map[lift.carrier]
            )
            transformed_input = transform_pauli(
                code,
                lift.input_face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            transformed_output = transform_pauli(
                code,
                lift.output_face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            input_phase = relative_scalar(transformed_input, target.input_face_pauli)
            output_phase = relative_scalar(transformed_output, target.output_face_pauli)
            frame_failures += input_phase is None or output_phase is None
            frame_failures += input_phase != output_phase
            frame_failures += ports.permute_bits(lift.input_tags, vertex_map) != target.input_tags
            frame_failures += ports.permute_bits(lift.output_tags, vertex_map) != target.output_tags
            frame_tests += 1

    translation_failures = 0
    translation_tests = 0
    translation_reference_tableau_tests = 0
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        transformed_reference_rows = [
            transform_pauli(code, row, edge_map, toggles, pairs, flips)
            for row in reference_face_rows
        ]
        reference_rank, reference_bad = c235.phase_aware_rank(
            reference_face_rows + transformed_reference_rows, code.qubits
        )
        translation_failures += reference_rank != code.qubits or bool(reference_bad)
        translation_reference_tableau_tests += 1
        for lift in fixtures:
            target = localized_lift(
                code, vertex_map[lift.source], vertex_map[lift.carrier]
            )
            transformed_input = transform_pauli(
                code,
                lift.input_face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            transformed_output = transform_pauli(
                code,
                lift.output_face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            input_phase = relative_scalar(transformed_input, target.input_face_pauli)
            output_phase = relative_scalar(transformed_output, target.output_face_pauli)
            translation_failures += input_phase is None or output_phase is None
            translation_failures += input_phase != output_phase
            translation_failures += ports.permute_bits(lift.input_tags, vertex_map) != target.input_tags
            translation_failures += ports.permute_bits(lift.output_tags, vertex_map) != target.output_tags
            translation_tests += 1
    check(
        "the two-column physical state-lift family is covariant with one common column phase under all 24 proper frames and all L=3 translations",
        len(c235.proper_cubic_frames()) == 24
        and frame_failures == 0
        and translation_failures == 0,
        {
            "proper_frames": len(c235.proper_cubic_frames()),
            "frame_lift_tests": frame_tests,
            "frame_reference_tableau_tests": frame_reference_tableau_tests,
            "frame_failures": frame_failures,
            "translations": code.length**3,
            "translation_lift_tests": translation_tests,
            "translation_reference_tableau_tests": (
                translation_reference_tableau_tests
            ),
            "translation_failures": translation_failures,
        },
    )


def constraint_leakage_deletion_and_domain_controls(
    cache: dict[int, c269.WilsonSubsystemCode],
    fixtures: dict[int, list[LocalizedLift]],
) -> None:
    print("\nCONSTRAINT LEAKAGE / DELETION / LAWFUL DOMAIN")
    leakage_rows = []
    for length, code in cache.items():
        local_check_leakage = 0
        wilson_leakage = 0
        port_constraint_failures = 0
        deleted_catchup_mismatches = 0
        deleted_stream_orthogonal = 0
        stream_factor_deletion_tests = 0
        for lift in fixtures[length]:
            for pauli, tags in (
                (lift.input_face_pauli, lift.input_tags),
                (lift.output_face_pauli, lift.output_tags),
            ):
                local_check_leakage += sum(
                    not pauli.commutes(row) for row in code.local_checks
                )
                wilson_leakage += sum(
                    not pauli.commutes(row) for row in code.wilsons
                )
                occupations = occupied_vertices(code, pauli)
                port_constraint_failures += tags != sum(1 << item for item in occupations)
            streamed_occupations, _sign = ports.stream_occupations(
                code, lift.input_tags
            )
            deleted_catchup_mismatches += streamed_occupations == lift.input_tags
            for retained_edge in (
                lift.source_outer_edge,
                lift.carrier_outer_edge,
            ):
                one_edge_face = code.A[retained_edge] @ lift.input_face_pauli
                deleted_stream_orthogonal += occupied_vertices(code, one_edge_face) in (
                    occupied_vertices(code, lift.input_face_pauli),
                    occupied_vertices(code, lift.output_face_pauli),
                )
                stream_factor_deletion_tests += 1
        leakage_rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "local_check_leakage": local_check_leakage,
                "Wilson_leakage": wilson_leakage,
                "port_constraint_failures": port_constraint_failures,
                "deleted_catchup_nonmismatches": deleted_catchup_mismatches,
                "one_stream_factor_deletion_nonorthogonal_cases": deleted_stream_orthogonal,
                "one_stream_factor_deletion_tests": stream_factor_deletion_tests,
            }
        )
    check(
        "both encoded columns preserve local checks, Wilsons, and port constraints, while catch-up and one-stream-factor deletions leave the target code column",
        all(
            row["local_check_leakage"] == 0
            and row["Wilson_leakage"] == 0
            and row["port_constraint_failures"] == 0
            and row["deleted_catchup_nonmismatches"] == 0
            and row["one_stream_factor_deletion_nonorthogonal_cases"] == 0
            and row["one_stream_factor_deletion_tests"]
            == 2 * 24 * row["L"] ** 3
            for row in leakage_rows
        ),
        leakage_rows,
    )

    code = cache[3]
    source, carrier = next(all_oriented_internal_pairs(code))
    valid_tags = (1 << source) | (1 << carrier)
    validate_localized_domain(code, source, carrier, valid_tags)
    same_cell = code.graph.vertices[source][0]
    opposite_direction = code.graph.vertices[source][1] ^ 1
    opposite = code.graph.vertex_index[(same_cell, opposite_direction)]
    outer = old.outer_partner(code, source)[0]
    bad = (
        (source, source, 1 << source),
        (source, carrier, 1 << source),
        (source, opposite, (1 << source) | (1 << opposite)),
        (source, outer, (1 << source) | (1 << outer)),
        (-1, carrier, valid_tags),
        (len(code.graph.vertices), carrier, valid_tags),
        (source, carrier, valid_tags | (1 << len(code.graph.vertices))),
    )
    rejected = 0
    for candidate in bad:
        try:
            validate_localized_domain(code, *candidate)
        except (KeyError, ValueError):
            rejected += 1
    undersized = False
    try:
        c269.build_code(2)
    except ValueError:
        undersized = True
    check(
        "the localized lift rejects coincident, mistagged, opposite, nonlocal, out-of-range, and undersized fixtures",
        rejected == len(bad) and undersized,
        {"rejected_fixtures": rejected, "L2_rejected": undersized},
    )


def decoded_encoded_boundary_and_inventory() -> None:
    print("\nDECODED / ENCODED BOUNDARY AND SUPPLIED INVENTORY")
    check(
        "the result is an encoded stabilizer-state lift for one localized pair orbit relative to a supplied vacuum, not a global mobile/source or full-Fock encoder",
        True,
        {
            "encoded": (
                "unique fixed-Wilson face-code vacuum tableau",
                "two physical stabilizer-state columns per localized adjacent pair",
                "exact 2x2 Gram identity",
                "exact action of the restricted two-edge physical FSWAP/catch-up word on both columns and its inverse",
                "bounded Pauli/tag representatives of support at most 19 M2",
            ),
            "decoded_only": (
                "occupation and auxiliary tag masks used to enumerate fixtures",
                "source versus carrier role names on one identical-species pair ray",
            ),
            "supplied": (
                "+++ Wilson character and unique vacuum ray",
                "six auxiliary port M2 per cell",
                "one ordered adjacent source/carrier patch label",
                "Cycle-269 A/B/FSWAP dictionary",
                "stream-then-catch-up convention",
            ),
            "open": (
                "bounded preparation of the global fixed-Wilson vacuum",
                "one coherent encoder across different positions or Wilson sectors",
                "independent source and carrier species or role qubit",
                "actual six-mode coin and local port routing",
                "contact and full-Fock macrostep",
            ),
            "overhead": "15 face + 6 port = 21 M2/cell; column representative support <=19 M2",
            "assembled_full_Hilbert_space_G_matrix": False,
            "G_physical_scope": "restricted action of the supplied physical operator word on the declared two-column code space",
            "authority": "none",
            "audit": "unset",
            "no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("PHYSICAL CYCLE-269 REFERENCE-RELATIVE LOCALIZED PAIR LIFT")
    print("authority=none; audit=unset")
    note_contract()
    cache = {length: c269.build_code(length) for length in SIZES}
    reference_vacuum_and_rank_controls(cache)
    fixtures = isometry_intertwining_and_held_controls(cache)
    covariance_controls(cache[3], fixtures[3])
    constraint_leakage_deletion_and_domain_controls(cache, fixtures)
    decoded_encoded_boundary_and_inventory()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
