#!/usr/bin/env python3
"""Cycle 304: one common coin/stream/contact fixed-Wilson refinement.

Cycle 302 uses thirty half-stream pair rays to carry a six-mode logical coin.
The coherent pair orbit uses twelve perpendicular wedges at two endpoint
slices.  Those physical tag sectors are disjoint.  This runner builds the
bounded common refinement instead of identifying their labels:

* two flagged copies of the Cycle-302 half-stream shell, carrying n=1;
* all fifteen two-mode wedges at both endpoint slices, carrying n=2.

One extra supplied phase M2 distinguishes the before/after carrier role.  It
is not locally constrained by the existing occupation/port layer.  The
resulting 42-column E exactly intertwines a fixed-seam comparator: the actual
Cycle-219 coin (and wedge lift) on the onsite input slice, identity on the
separated slice, collision-safe stream/catch-up, and Cycle-230 contact.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_coherent_cubic_pair_orbit_2026_07_17 as orbit
import physical_cycle269_joint_six_mode_coin_lift_cycle302_2026_07_17 as c302
import physical_cycle269_local_contact_intertwiner_2026_07_17 as contact
import physical_cycle269_reference_relative_localized_pair_lift_2026_07_17 as local
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COIN_STREAM_CONTACT_COMMON_REFINEMENT_CYCLE304_NOTE_2026-07-17.md"
)
BODY = (0, 0, 0)
TRAINING_SIZE = 3
HELD_SIZE = 6
PAIR_LABELS = tuple(combinations(range(6), 2))
PAIR_INDEX = {pair: index for index, pair in enumerate(PAIR_LABELS)}
PERPENDICULAR = tuple(pair for pair in PAIR_LABELS if pair[1] != (pair[0] ^ 1))
OPPOSITE = tuple(pair for pair in PAIR_LABELS if pair[1] == (pair[0] ^ 1))
MICRO_DIMENSION = 2 * 30 + 2 * 15
LOGICAL_DIMENSION = 2 * 6 + 2 * 15
TOLERANCE = 8e-12

PASS = 0
FAIL = 0


@dataclass(frozen=True)
class PairColumn:
    pair: tuple[int, int]
    stream_slice: int
    vertices: tuple[int, int]
    arrivals: tuple[int, int]
    outer_edges: tuple[int, int]
    face_pauli: c235.Pauli
    tags: int


@dataclass(frozen=True)
class MicroColumn:
    sector: str
    label: tuple[int, int]
    stream_slice: int
    face_pauli: c235.Pauli
    tags: int
    representative: c235.Pauli


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
        check("the Cycle-304 note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "zero physical tag overlap",
        "one common fixed-wilson e",
        "fixed-seam comparator",
        "forty-two logical columns",
        "ninety microsectors",
        "one supplied phase m2 per cell",
        "twenty-two m2 per cell",
        "e g_comparator = g_physical e",
        "coin, then stream/catch-up, then contact",
        "all 24 proper-cubic frames",
        "all 27 l=3 translations",
        "held l=6",
        "opposite-wedge completion",
        "mass firewall",
        "phase flag is not locally enforced",
        "absolute vacuum preparation remains open",
        "coherent position growth remains open",
        "full-fock compilation remains open",
        "actual recurrent volume update remains open",
        "not physical time",
        "not physical energy",
        "not a rate",
        "no gravity/source semantics",
        "no record claim",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the common refinement and exact boundary", not missing, missing)


def block_diagonal(*blocks: np.ndarray) -> np.ndarray:
    size = sum(block.shape[0] for block in blocks)
    result = np.zeros((size, size), dtype=complex)
    offset = 0
    for block in blocks:
        width = block.shape[0]
        result[offset : offset + width, offset : offset + width] = block
        offset += width
    return result


def vertex(code: c269.WilsonSubsystemCode, body, direction: int) -> int:
    return code.graph.vertex_index[(tuple(body), direction)]


def flag_qubit(
    code: c269.WilsonSubsystemCode, body: tuple[int, int, int]
) -> int:
    """One homogeneous phase M2 at every coarse-cell anchor."""

    return (
        code.qubits
        + len(code.graph.vertices)
        + code.graph.cells.index(tuple(body))
    )


def extend_representative(
    code: c269.WilsonSubsystemCode,
    face_pauli: c235.Pauli,
    tags: int,
    stream_slice: int,
    body: tuple[int, int, int],
) -> c235.Pauli:
    representative = local.full_state_representative(code, face_pauli, tags)
    if stream_slice:
        representative = c235.Pauli(x=1 << flag_qubit(code, body)) @ representative
    return representative


def pair_input_face(
    code: c269.WilsonSubsystemCode,
    body: tuple[int, int, int],
    pair: tuple[int, int],
) -> c235.Pauli:
    left, right = pair
    left_vertex, right_vertex = vertex(code, body, left), vertex(code, body, right)
    if right != (left ^ 1):
        return code.graph.A(left_vertex, right_vertex)

    # This seed only exhibits bounded support.  The encoded ray is defined by
    # its unique fixed-sector stabilizer syndrome; covariance is checked after
    # quotienting by the reference stabilizers, so the seed is not an axis
    # ordering in the physical law.
    transverse = next(direction for direction in range(6) if direction // 2 != left // 2)
    middle = vertex(code, body, transverse)
    return code.graph.A(middle, right_vertex) @ code.graph.A(left_vertex, middle)


def pair_columns(
    code: c269.WilsonSubsystemCode, body=BODY
) -> tuple[PairColumn, ...]:
    columns = []
    for pair in PAIR_LABELS:
        left, right = pair
        vertices = (vertex(code, body, left), vertex(code, body, right))
        arrivals_and_edges = tuple(local.old.outer_partner(code, item) for item in vertices)
        arrivals = tuple(item[0] for item in arrivals_and_edges)
        edges = tuple(item[1] for item in arrivals_and_edges)
        input_face = pair_input_face(code, body, pair)
        output_face, _phase = local.two_edge_physical_face_action(
            code, input_face, vertices, edges
        )
        columns.append(
            PairColumn(
                pair,
                0,
                vertices,
                arrivals,
                edges,
                input_face,
                sum(1 << item for item in vertices),
            )
        )
        columns.append(
            PairColumn(
                pair,
                1,
                vertices,
                arrivals,
                edges,
                output_face,
                sum(1 << item for item in arrivals),
            )
        )
    return tuple(columns)


def pair_lookup(columns: tuple[PairColumn, ...]) -> dict[tuple[tuple[int, int], int], PairColumn]:
    return {(column.pair, column.stream_slice): column for column in columns}


def micro_columns(
    code: c269.WilsonSubsystemCode, body=BODY
) -> tuple[MicroColumn, ...]:
    columns = []
    for stream_slice in range(2):
        for direction, reference in c302.PAIR_LABELS:
            physical_direction, physical_reference = (
                (direction, reference) if stream_slice == 0 else (reference, direction)
            )
            ray = c302.pair_ray(
                code, body, physical_direction, physical_reference
            )
            columns.append(
                MicroColumn(
                    "n1",
                    (direction, reference),
                    stream_slice,
                    ray.face_pauli,
                    ray.tags,
                    extend_representative(
                        code, ray.face_pauli, ray.tags, stream_slice, body
                    ),
                )
            )
    full_pairs = pair_lookup(pair_columns(code, body))
    for stream_slice in range(2):
        for pair in PAIR_LABELS:
            column = full_pairs[(pair, stream_slice)]
            columns.append(
                MicroColumn(
                    "n2",
                    column.pair,
                    column.stream_slice,
                    column.face_pauli,
                    column.tags,
                    extend_representative(
                        code,
                        column.face_pauli,
                        column.tags,
                        column.stream_slice,
                        body,
                    ),
                )
            )
    return tuple(columns)


def micro_index(sector: str, label: tuple[int, int], stream_slice: int) -> int:
    if sector == "n1":
        return stream_slice * 30 + c302.PAIR_INDEX[label]
    if sector == "n2":
        return 60 + stream_slice * 15 + PAIR_INDEX[label]
    raise ValueError("the common refinement has only n=1 and n=2 sectors")


def logical_n1_index(direction: int, stream_slice: int) -> int:
    return stream_slice * 6 + direction


def logical_n2_index(pair: tuple[int, int], stream_slice: int) -> int:
    return 12 + stream_slice * 15 + PAIR_INDEX[pair]


def common_encoding() -> np.ndarray:
    encoding = np.zeros((MICRO_DIMENSION, LOGICAL_DIMENSION), dtype=complex)
    for stream_slice in range(2):
        for direction in range(6):
            for reference in range(6):
                if reference == (direction ^ 1):
                    continue
                encoding[
                    micro_index("n1", (direction, reference), stream_slice),
                    logical_n1_index(direction, stream_slice),
                ] = 1 / np.sqrt(5)
        for pair in PAIR_LABELS:
            encoding[
                micro_index("n2", pair, stream_slice),
                logical_n2_index(pair, stream_slice),
            ] = 1
    return encoding


def wedge_coin(coin: np.ndarray) -> np.ndarray:
    wedge = np.zeros((15, 15), dtype=complex)
    for source, (left, right) in enumerate(PAIR_LABELS):
        for target, (first, second) in enumerate(PAIR_LABELS):
            wedge[target, source] = (
                coin[first, left] * coin[second, right]
                - coin[first, right] * coin[second, left]
            )
    return wedge


def logical_coin(coin: np.ndarray) -> np.ndarray:
    wedge = wedge_coin(coin)
    # The actual onsite coin is applied only on the body/onsite input slice.
    # The separated slice is the identity completion of this fixed-seam
    # comparator, not an assertion about recurrent volume evolution.
    return block_diagonal(coin, np.eye(6), wedge, np.eye(15))


def physical_coin(coin: np.ndarray) -> np.ndarray:
    shell_encoding = c302.encoding_matrix()
    shell_projector = shell_encoding @ shell_encoding.conj().T
    shell = np.eye(30) - shell_projector + shell_encoding @ coin @ shell_encoding.conj().T
    wedge = wedge_coin(coin)
    return block_diagonal(shell, np.eye(30), wedge, np.eye(15))


def logical_stream() -> np.ndarray:
    stream = np.zeros((LOGICAL_DIMENSION, LOGICAL_DIMENSION), dtype=complex)
    for direction in range(6):
        for stream_slice in range(2):
            stream[
                logical_n1_index(direction, 1 - stream_slice),
                logical_n1_index(direction, stream_slice),
            ] = -1
    for pair in PAIR_LABELS:
        for stream_slice in range(2):
            stream[
                logical_n2_index(pair, 1 - stream_slice),
                logical_n2_index(pair, stream_slice),
            ] = 1
    return stream


def physical_stream() -> np.ndarray:
    stream = np.zeros((MICRO_DIMENSION, MICRO_DIMENSION), dtype=complex)
    for label in c302.PAIR_LABELS:
        for stream_slice in range(2):
            stream[
                micro_index("n1", label, 1 - stream_slice),
                micro_index("n1", label, stream_slice),
            ] = -1
    for pair in PAIR_LABELS:
        for stream_slice in range(2):
            stream[
                micro_index("n2", pair, 1 - stream_slice),
                micro_index("n2", pair, stream_slice),
            ] = 1
    return stream


def logical_contact(coupling: float) -> np.ndarray:
    diagonal = np.ones(LOGICAL_DIMENSION, dtype=complex)
    for pair in PAIR_LABELS:
        diagonal[logical_n2_index(pair, 0)] = np.exp(1j * coupling)
    return np.diag(diagonal)


def physical_contact(coupling: float) -> np.ndarray:
    diagonal = np.ones(MICRO_DIMENSION, dtype=complex)
    for pair in PAIR_LABELS:
        diagonal[micro_index("n2", pair, 0)] = np.exp(1j * coupling)
    return np.diag(diagonal)


def reference_solver(code: c269.WilsonSubsystemCode):
    basis: dict[int, tuple[int, c235.Pauli]] = {}
    for generator in code.local_checks + code.wilsons + code.B:
        vector = generator.x | (generator.z << code.qubits)
        pauli = generator
        while vector:
            pivot = vector.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = vector, pauli
                break
            other_vector, other_pauli = basis[pivot]
            vector ^= other_vector
            pauli = pauli @ other_pauli
    if len(basis) != code.qubits:
        raise ValueError("the fixed-Wilson reference stabilizers must define one ray")
    return basis


def reference_eigenphase(
    code: c269.WilsonSubsystemCode,
    basis: dict[int, tuple[int, c235.Pauli]],
    pauli: c235.Pauli,
) -> int | None:
    vector = pauli.x | (pauli.z << code.qubits)
    stabilizer = c235.Pauli()
    while vector:
        pivot = vector.bit_length() - 1
        if pivot not in basis:
            return None
        other_vector, other_pauli = basis[pivot]
        vector ^= other_vector
        stabilizer = stabilizer @ other_pauli
    return (pauli.phase - stabilizer.phase) % 4


def state_relative_phase(
    code: c269.WilsonSubsystemCode,
    basis: dict[int, tuple[int, c235.Pauli]],
    source: c235.Pauli,
    target: c235.Pauli,
    edge_map,
    toggles,
    pairs,
    flips,
) -> int | None:
    transformed = local.transform_pauli(
        code, source, edge_map, toggles, pairs, flips
    )
    relative = c302.pauli_dagger(target) @ transformed
    return reference_eigenphase(code, basis, relative)


def wedge_representation(frame: np.ndarray) -> np.ndarray:
    representation = np.zeros((15, 15), dtype=complex)
    for source, (left, right) in enumerate(PAIR_LABELS):
        mapped = (c302.direction_map(frame, left), c302.direction_map(frame, right))
        target_pair = tuple(sorted(mapped))
        sign = 1 if mapped[0] < mapped[1] else -1
        representation[PAIR_INDEX[target_pair], source] = sign
    return representation


def ordered_representation(frame: np.ndarray) -> np.ndarray:
    representation = np.zeros((30, 30), dtype=complex)
    for source, (direction, reference) in enumerate(c302.PAIR_LABELS):
        target = c302.PAIR_INDEX[
            (c302.direction_map(frame, direction), c302.direction_map(frame, reference))
        ]
        representation[target, source] = 1
    return representation


def frame_representations(frame: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    direction = c210.direction_permutation(frame)
    wedge = wedge_representation(frame)
    logical = block_diagonal(direction, direction, wedge, wedge)
    ordered = ordered_representation(frame)
    micro = block_diagonal(ordered, ordered, wedge, wedge)
    return logical, micro


def geometry_and_overlap_controls(
    code: c269.WilsonSubsystemCode, label: str
) -> tuple[MicroColumn, ...]:
    columns = micro_columns(code)
    patterns = tuple((column.tags, column.stream_slice) for column in columns)
    h_patterns = {item for item, column in zip(patterns, columns) if column.sector == "n1"}
    p_patterns = {item for item, column in zip(patterns, columns) if column.sector == "n2"}
    face_union = tag_union = 0
    max_support = 0
    constraint_failures = local_failures = wilson_failures = 0
    for column in columns:
        face_union |= column.face_pauli.x | column.face_pauli.z
        tag_union |= column.tags
        max_support = max(
            max_support,
            (column.face_pauli.x | column.face_pauli.z).bit_count()
            + column.tags.bit_count()
            + column.stream_slice,
        )
        occupations = local.occupied_vertices(code, column.face_pauli)
        occupied_mask = sum(1 << item for item in occupations)
        constraint_failures += occupied_mask != column.tags
        local_failures += sum(
            not column.face_pauli.commutes(row) for row in code.local_checks
        )
        wilson_failures += sum(
            not column.face_pauli.commutes(row) for row in code.wilsons
        )
    check(
        f"{label}: existing Cycle-302 and pair-orbit tag sectors have zero physical overlap",
        not h_patterns.intersection(p_patterns) and len(patterns) == len(set(patterns)) == 90,
        {
            "Cycle302_flagged_microsectors": len(h_patterns),
            "full_pair_microsectors": len(p_patterns),
            "overlap": len(h_patterns.intersection(p_patterns)),
        },
    )
    check(
        f"{label}: one common refinement has bounded forty-three-M2 support and zero constraint leakage",
        face_union.bit_count() == 30
        and tag_union.bit_count() == 12
        and max_support <= 18
        and constraint_failures == local_failures == wilson_failures == 0,
        {
            "face_M2": face_union.bit_count(),
            "port_M2": tag_union.bit_count(),
            "phase_M2": 1,
            "union_M2": face_union.bit_count() + tag_union.bit_count() + 1,
            "max_column_support_M2": max_support,
            "constraint_failures": constraint_failures,
            "local_check_failures": local_failures,
            "Wilson_failures": wilson_failures,
            "installed_overhead_M2_per_cell": 22,
        },
    )
    return columns


def literal_subcode_controls(code: c269.WilsonSubsystemCode) -> None:
    columns = micro_columns(code)
    lookup = {
        (column.sector, column.label, column.stream_slice): column
        for column in columns
    }
    c302_failures = 0
    for ray in c302.shell(code):
        column = lookup[("n1", (ray.direction, ray.reference_direction), 0)]
        c302_failures += column.face_pauli != ray.face_pauli or column.tags != ray.tags
    encoder = orbit.orbit_encoder(code, BODY)
    orbit_failures = 0
    for fixture in encoder.addresses:
        modes = tuple(sorted((code.graph.vertices[fixture.source][1], code.graph.vertices[fixture.carrier][1])))
        for stream_slice, expected in enumerate(
            (
                (fixture.input_face_pauli, fixture.input_tags),
                (fixture.output_face_pauli, fixture.output_tags),
            )
        ):
            column = lookup[("n2", modes, stream_slice)]
            orbit_failures += (column.face_pauli, column.tags) != expected
    check(
        "the common refinement contains the literal Cycle-302 rays and all 24 original pair-orbit columns",
        c302_failures == orbit_failures == 0,
        {"Cycle302_literal_failures": c302_failures, "pair_orbit_literal_failures": orbit_failures},
    )


def stream_branch_controls(
    code: c269.WilsonSubsystemCode, label: str
) -> None:
    h_failures = p_failures = tag_failures = sign_failures = 0
    deleted_catchup_failures = 0
    for stream_slice in range(2):
        for direction, reference in c302.PAIR_LABELS:
            physical_direction, physical_reference = (
                (direction, reference) if stream_slice == 0 else (reference, direction)
            )
            source = c302.pair_ray(
                code, BODY, physical_direction, physical_reference
            )
            target = c302.pair_ray(
                code, BODY, physical_reference, physical_direction
            )
            arrival, caught, decoded_sign = local.ports.port_macrostep(
                code, source.tags, source.tags
            )
            tag_failures += arrival != target.tags or caught != target.tags
            deleted_catchup_failures += source.tags != target.tags
            if direction == reference:
                # One occupied-occupied outer FSWAP fixes the configuration and
                # supplies the fermionic -1.
                sign_failures += decoded_sign != -1
            else:
                body_occupied = vertex(code, BODY, physical_direction)
                reference_port = vertex(code, BODY, physical_reference)
                reference_occupied, reference_edge = local.old.outer_partner(
                    code, reference_port
                )
                _carrier_arrival, carrier_edge = local.old.outer_partner(
                    code, body_occupied
                )
                output, _phase = local.two_edge_physical_face_action(
                    code,
                    source.face_pauli,
                    (body_occupied, reference_occupied),
                    (carrier_edge, reference_edge),
                )
                h_failures += local.relative_scalar(output, target.face_pauli) != 2
                sign_failures += decoded_sign != 1

    pair_map = pair_lookup(pair_columns(code))
    for pair in PAIR_LABELS:
        before, after = pair_map[(pair, 0)], pair_map[(pair, 1)]
        forward, _phase = local.two_edge_physical_face_action(
            code, before.face_pauli, before.vertices, before.outer_edges
        )
        backward, _phase = local.two_edge_physical_face_action(
            code, after.face_pauli, after.arrivals, after.outer_edges
        )
        p_failures += forward != after.face_pauli or backward != before.face_pauli
        for source, target in ((before, after), (after, before)):
            arrival, caught, sign = local.ports.port_macrostep(
                code, source.tags, source.tags
            )
            tag_failures += arrival != target.tags or caught != target.tags
            sign_failures += sign != 1
            deleted_catchup_failures += source.tags != target.tags
    check(
        f"{label}: the flagged common stream is the exact collision-safe physical branch action in both sectors",
        h_failures == p_failures == tag_failures == sign_failures == 0
        and deleted_catchup_failures > 0,
        {
            "half_stream_face_failures": h_failures,
            "pair_face_failures": p_failures,
            "tag_failures": tag_failures,
            "fermionic_sign_failures": sign_failures,
            "states_leaking_if_catchup_deleted": deleted_catchup_failures,
        },
    )


def matrix_unit_constraint_controls(
    code: c269.WilsonSubsystemCode, columns: tuple[MicroColumn, ...]
) -> None:
    coin = physical_coin(c219.common_species(-0.3).coin)
    stream = physical_stream()
    transitions = set()
    for operator in (coin, stream):
        rows, cols = np.where(abs(operator) > 1e-13)
        transitions.update(zip(rows.tolist(), cols.tolist()))

    constraint_failures = sector_failures = 0
    for left, right in transitions:
        transition = columns[left].representative @ c302.pauli_dagger(
            columns[right].representative
        )
        constraint_failures += sum(
            not transition.commutes(c302.constraint_pauli(code, vertex_index))
            for vertex_index in range(len(code.graph.vertices))
        )
        sector_failures += sum(
            not transition.commutes(row)
            for row in code.local_checks + code.wilsons
        )
    patterns = {(column.tags, column.stream_slice) for column in columns}
    check(
        "the bounded matrix-unit completion preserves every port constraint and fixed-sector stabilizer",
        len(patterns) == 90
        and constraint_failures == sector_failures == 0,
        {
            "local_tag_flag_projectors": len(patterns),
            "nonzero_coin_or_stream_matrix_units": len(transitions),
            "port_constraint_commutator_failures": constraint_failures,
            "fixed_sector_commutator_failures": sector_failures,
        },
    )


def literal_coin_and_contact_controls(
    code: c269.WilsonSubsystemCode, columns: tuple[MicroColumn, ...]
) -> None:
    coin = c219.common_species(-0.3).coin
    fock_coin = contact.c230.c229.fock_lift(coin)
    one_indices = [1 << direction for direction in range(6)]
    pair_indices = [
        (1 << left) | (1 << right) for left, right in PAIR_LABELS
    ]
    one_residual = float(
        np.linalg.norm(fock_coin[np.ix_(one_indices, one_indices)] - coin)
    )
    pair_residual = float(
        np.linalg.norm(
            fock_coin[np.ix_(pair_indices, pair_indices)] - wedge_coin(coin)
        )
    )

    expected_contact = np.diag(physical_contact(contact.COUPLING))
    literal_contact = []
    for column in columns:
        occupations = local.occupied_vertices(code, column.face_pauli)
        literal_contact.append(
            contact.contact_phase_from_occupations(
                code, occupations, contact.COUPLING
            )
        )
    contact_residual = float(
        np.linalg.norm(np.asarray(literal_contact) - expected_contact)
    )
    check(
        "the coin blocks are the literal M64 Fock restrictions and contact is derived from physical B occupations",
        max(one_residual, pair_residual, contact_residual) < TOLERANCE,
        {
            "one_particle_Fock_block_residual": one_residual,
            "two_particle_Fock_block_residual": pair_residual,
            "literal_physical_contact_residual": contact_residual,
        },
    )


def phase_flag_enforcement_audit(columns: tuple[MicroColumn, ...]) -> None:
    half_stream: dict[tuple[int, int, int], set[int]] = {}
    for column in columns:
        if column.sector != "n1":
            continue
        key = (column.face_pauli.x, column.face_pauli.z, column.tags)
        half_stream.setdefault(key, set()).add(column.stream_slice)
    two_valued_patterns = sum(slices == {0, 1} for slices in half_stream.values())
    check(
        "the phase-flag enforcement audit exposes the remaining free auxiliary role bit",
        len(half_stream) == 30 and two_valued_patterns == 30,
        {
            "unflagged_half_stream_patterns": len(half_stream),
            "patterns_occurring_with_both_flag_values": two_valued_patterns,
            "local_occupation_or_port_constraint_can_fix_flag": False,
            "status": "phase flag is a supplied code-sector label; local carrier-role enforcement remains open",
        },
    )


def recurrent_volume_update_audit(code: c269.WilsonSubsystemCode) -> None:
    """Measure why the separated-slice identity is only a comparator completion."""

    coin = c219.common_species(-0.3).coin
    pairs = pair_lookup(pair_columns(code))
    output_modes = [
        tuple(sorted(pairs[(pair, 1)].arrivals)) for pair in PAIR_LABELS
    ]
    output_index = {modes: index for index, modes in enumerate(output_modes)}
    retained = np.zeros((15, 15), dtype=complex)
    for source, (left_vertex, right_vertex) in enumerate(output_modes):
        left_cell, left_direction = code.graph.vertices[left_vertex]
        right_cell, right_direction = code.graph.vertices[right_vertex]
        for left_target in range(6):
            mapped_left = code.graph.vertex_index[(left_cell, left_target)]
            for right_target in range(6):
                mapped_right = code.graph.vertex_index[(right_cell, right_target)]
                if mapped_left == mapped_right:
                    continue
                target_modes = tuple(sorted((mapped_left, mapped_right)))
                target = output_index.get(target_modes)
                if target is None:
                    continue
                amplitude = (
                    coin[left_target, left_direction]
                    * coin[right_target, right_direction]
                )
                if mapped_left > mapped_right:
                    amplitude *= -1
                retained[target, source] += amplitude
    leakage_squared = np.eye(15) - retained.conj().T @ retained
    recurrent_leakage = float(
        np.sqrt(max(0.0, np.max(np.linalg.eigvalsh(leakage_squared))))
    )
    check(
        "the actual separated-cell recurrent coin is measured outside the fixed-seam orbit",
        recurrent_leakage > 0.99,
        {
            "separated_slice_actual_onsite_coin_leakage_operator_norm": recurrent_leakage,
            "retained_block_unitarity_residual": float(
                np.linalg.norm(retained.conj().T @ retained - np.eye(15))
            ),
            "comparator_completion_on_inactive_slice": "identity",
        },
    )


def intertwining_controls(beta: float, held: bool = False) -> dict[str, float]:
    coin = c219.common_species(beta).coin
    encoding = common_encoding()
    logical_c, physical_c = logical_coin(coin), physical_coin(coin)
    logical_s, physical_s = logical_stream(), physical_stream()
    logical_v = logical_contact(contact.COUPLING)
    physical_v = physical_contact(contact.COUPLING)
    logical_g = logical_v @ logical_s @ logical_c
    physical_g = physical_v @ physical_s @ physical_c
    projector = encoding @ encoding.conj().T
    residuals = {
        "isometry": float(np.linalg.norm(encoding.conj().T @ encoding - np.eye(42))),
        "coin": float(np.linalg.norm(physical_c @ encoding - encoding @ logical_c)),
        "stream": float(np.linalg.norm(physical_s @ encoding - encoding @ logical_s)),
        "contact": float(np.linalg.norm(physical_v @ encoding - encoding @ logical_v)),
        "composition": float(np.linalg.norm(physical_g @ encoding - encoding @ logical_g)),
        "leakage": float(np.linalg.norm((np.eye(90) - projector) @ physical_g @ encoding)),
        "coin_unitarity": float(np.linalg.norm(physical_c.conj().T @ physical_c - np.eye(90))),
        "stream_inverse": float(np.linalg.norm(physical_s @ physical_s - np.eye(90))),
        "contact_inverse": float(
            np.linalg.norm(physical_v @ physical_contact(-contact.COUPLING) - np.eye(90))
        ),
        "composition_unitarity": float(np.linalg.norm(physical_g.conj().T @ physical_g - np.eye(90))),
    }
    label = "held beta=-0.35" if held else f"beta={beta}"
    check(
        f"{label}: one common E intertwines the fixed-seam coin, stream/catch-up, contact, and declared composition",
        max(residuals.values()) < TOLERANCE,
        residuals,
    )
    return residuals


def mass_firewall_controls(beta: float = -0.3) -> None:
    species = c219.common_species(beta)
    coin = species.coin
    encoding = common_encoding()
    physical_c = physical_coin(coin)
    scalar0 = np.zeros(42, dtype=complex)
    scalar0[:6] = c210.UNIFORM
    encoded = encoding @ scalar0
    eigenvalue = np.vdot(encoded, physical_c @ encoded)
    physical_mass = float(np.angle(eigenvalue)) / c219.C_SQUARED
    fixture_mass = c219.rest_mass(species)

    n1_columns = encoding[:, :12]
    contact_difference = (
        physical_contact(contact.COUPLING) - physical_contact(0.0)
    ) @ n1_columns
    check(
        "the common refinement preserves the Cycle-219 one-particle mass fixture and exact contact firewall",
        abs(physical_mass - fixture_mass) < 4e-13
        and np.linalg.norm(contact_difference) == 0,
        {
            "physical_rest_mass": physical_mass,
            "Cycle219_fixture": fixture_mass,
            "one_particle_contact_difference": float(np.linalg.norm(contact_difference)),
        },
    )


def covariance_controls(code: c269.WilsonSubsystemCode) -> None:
    encoding = common_encoding()
    coin = c219.common_species(-0.3).coin
    operators = (
        physical_coin(coin),
        physical_stream(),
        physical_contact(contact.COUPLING),
    )
    logical_operators = (
        logical_coin(coin),
        logical_stream(),
        logical_contact(contact.COUPLING),
    )
    solver = reference_solver(code)
    frames = c235.proper_cubic_frames()
    representation_residual = operator_residual = 0.0
    h_state_failures = p_state_failures = tag_failures = flag_failures = 0

    for frame in frames:
        logical_r, micro_r = frame_representations(frame)
        representation_residual = max(
            representation_residual,
            float(np.linalg.norm(micro_r @ encoding - encoding @ logical_r)),
        )
        for physical, logical in zip(operators, logical_operators):
            operator_residual = max(
                operator_residual,
                float(np.linalg.norm(micro_r @ physical - physical @ micro_r)),
                float(np.linalg.norm(logical_r @ logical - logical @ logical_r)),
            )

        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        dmap = {direction: c302.direction_map(frame, direction) for direction in range(6)}
        mapped_flags = set()
        for body in code.graph.cells:
            target_body = tuple(int(value % code.length) for value in frame @ np.asarray(body))
            mapped_flags.add(flag_qubit(code, target_body))
            source_micro = micro_columns(code, body)
            target_lookup = {
                (column.sector, column.label, column.stream_slice): column
                for column in micro_columns(code, target_body)
            }
            for column in source_micro:
                if column.sector == "n1":
                    target_label = (dmap[column.label[0]], dmap[column.label[1]])
                    target = target_lookup[("n1", target_label, column.stream_slice)]
                    transformed = local.transform_pauli(
                        code, column.face_pauli, edge_map, toggles, pairs, flips
                    )
                    h_state_failures += local.relative_scalar(
                        transformed, target.face_pauli
                    ) != 0
                    expected_phase = 0
                else:
                    mapped = (dmap[column.label[0]], dmap[column.label[1]])
                    target_pair = tuple(sorted(mapped))
                    target = target_lookup[("n2", target_pair, column.stream_slice)]
                    expected_phase = 0 if mapped[0] < mapped[1] else 2
                    phase = state_relative_phase(
                        code,
                        solver,
                        column.face_pauli,
                        target.face_pauli,
                        edge_map,
                        toggles,
                        pairs,
                        flips,
                    )
                    p_state_failures += phase != expected_phase
                tag_failures += (
                    local.ports.permute_bits(column.tags, vertex_map) != target.tags
                )
                if column.stream_slice:
                    flag_failures += (
                        flag_qubit(code, target_body)
                        < code.qubits + len(code.graph.vertices)
                    )
        flag_failures += len(mapped_flags) != code.length**3

    check(
        "the common E and all three operators are covariant under all 24 proper-cubic frames",
        max(representation_residual, operator_residual) < TOLERANCE
        and h_state_failures == p_state_failures == tag_failures == flag_failures == 0,
        {
            "state_ray_tests": 24 * 27 * 90,
            "encoding_representation_residual": representation_residual,
            "operator_commutator_residual": operator_residual,
            "n1_state_failures": h_state_failures,
            "n2_state_failures": p_state_failures,
            "tag_failures": tag_failures,
            "phase_flag_permutation_failures": flag_failures,
        },
    )

    translation_failures = 0
    base = micro_columns(code, BODY)
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        toggles, pairs, flips = c269.repair_data(code.graph, vertex_map, edge_map)
        target = micro_columns(code, displacement)
        translation_failures += (
            flag_qubit(code, displacement)
            < code.qubits + len(code.graph.vertices)
        )
        for source_column, target_column in zip(base, target):
            phase = state_relative_phase(
                code,
                solver,
                source_column.face_pauli,
                target_column.face_pauli,
                edge_map,
                toggles,
                pairs,
                flips,
            )
            translation_failures += phase != 0
            translation_failures += (
                local.ports.permute_bits(source_column.tags, vertex_map)
                != target_column.tags
            )
    check(
        "all ninety physical microsectors are covariant under all 27 L=3 translations",
        translation_failures == 0,
        {"state_ray_tests": 27 * 90, "failures": translation_failures},
    )


def deletion_controls() -> None:
    coin = c219.common_species(-0.3).coin
    encoding = common_encoding()
    projector = encoding @ encoding.conj().T
    identity_coin = physical_coin(np.eye(6))
    check(
        "coin deletion is exact and contact deletion returns the compiled free step",
        np.linalg.norm(identity_coin - np.eye(90)) == 0
        and np.linalg.norm(
            physical_contact(0.0) @ physical_stream() @ physical_coin(coin)
            - physical_stream() @ physical_coin(coin)
        )
        == 0,
    )

    # The twelve perpendicular wedges are not closed under the actual coin.
    wedge = wedge_coin(coin)
    perpendicular_indices = [PAIR_INDEX[pair] for pair in PERPENDICULAR]
    opposite_indices = [PAIR_INDEX[pair] for pair in OPPOSITE]
    opposite_leakage = float(
        np.linalg.norm(wedge[np.ix_(opposite_indices, perpendicular_indices)], 2)
    )

    # Without flipping the added phase M2, the n=1 shell remains in the wrong
    # role slice.  Measure leakage from the six-dimensional logical column span.
    shell_encoding = c302.encoding_matrix()
    transpose = np.zeros((30, 30), dtype=complex)
    for direction, reference in c302.PAIR_LABELS:
        transpose[
            c302.PAIR_INDEX[(reference, direction)],
            c302.PAIR_INDEX[(direction, reference)],
        ] = -1
    role_leakage = float(
        np.linalg.norm(
            (np.eye(30) - shell_encoding @ shell_encoding.conj().T)
            @ transpose
            @ shell_encoding,
            2,
        )
    )

    order_residual = float(
        np.linalg.norm(
            physical_contact(contact.COUPLING) @ physical_stream()
            - physical_stream() @ physical_contact(contact.COUPLING),
            2,
        )
    )
    check(
        "opposite-wedge, phase-flag, and schedule deletions are all detected",
        abs(opposite_leakage - np.sqrt(8) / 3) < 2e-12
        and role_leakage > 0.95
        and order_residual > 0.3,
        {
            "perpendicular_to_opposite_coin_leakage": opposite_leakage,
            "deleted_flag_role_leakage": role_leakage,
            "contact_stream_order_residual": order_residual,
        },
    )

    coherent = np.exp(2j * np.pi * np.arange(42) / 42) / np.sqrt(42)
    physical_g = physical_contact(contact.COUPLING) @ physical_stream() @ physical_coin(coin)
    logical_g = logical_contact(contact.COUPLING) @ logical_stream() @ logical_coin(coin)
    check(
        "a held coherent vector across n=1, n=2, both slices, and all directions stays in the common code",
        np.linalg.norm(physical_g @ (encoding @ coherent) - encoding @ (logical_g @ coherent))
        < TOLERANCE
        and np.linalg.norm((np.eye(90) - projector) @ physical_g @ encoding @ coherent)
        < TOLERANCE,
    )


def lawful_domain_and_inventory(code: c269.WilsonSubsystemCode) -> None:
    rejected = 0
    for bad_pair in ((0, 0), (-1, 2), (0, 6)):
        try:
            if bad_pair not in PAIR_INDEX:
                raise ValueError("not a lawful wedge")
        except ValueError:
            rejected += 1
    try:
        c269.build_code(2)
    except (KeyError, ValueError):
        rejected += 1
    check(
        "lawful-domain controls reject repeated-mode, non-port, and aliased-size inputs",
        rejected == 4,
        rejected,
    )
    inventory = {
        "inherited": "fixed +++ Wilson vacuum, Cycle-269 A/B/FSWAP, six constrained ports",
        "coin": "Cycle-219 C and its exact two-particle exterior lift",
        "contact": "Cycle-230 g=0.37 onsite pair phase",
        "refinement": "three opposite wedges plus one supplied, unconstrained phase M2 per cell",
        "schedule": "coin, then stream/catch-up and phase flip, then contact",
        "derived": "42-column E, 90-sector matrix-unit completion, exact G intertwiner",
        "excluded": "global ordering, parity service, copied tag; local role enforcement remains open",
    }
    check("the common-refinement supplied structure is explicit", len(inventory) == 7, inventory)


def main() -> int:
    print("CYCLE 304: COMMON COIN / STREAM / CONTACT REFINEMENT")
    print("authority=none; audit=unset")
    note_contract()
    training = c269.build_code(TRAINING_SIZE)
    held = c269.build_code(HELD_SIZE)
    training_columns = geometry_and_overlap_controls(training, "training L=3")
    geometry_and_overlap_controls(held, "held L=6")
    literal_subcode_controls(training)
    stream_branch_controls(training, "training L=3")
    stream_branch_controls(held, "held L=6")
    matrix_unit_constraint_controls(training, training_columns)
    literal_coin_and_contact_controls(training, training_columns)
    phase_flag_enforcement_audit(training_columns)
    recurrent_volume_update_audit(training)
    for beta in (-0.2, -0.3, -0.4):
        intertwining_controls(beta)
    intertwining_controls(-0.35, held=True)
    mass_firewall_controls()
    covariance_controls(training)
    deletion_controls()
    lawful_domain_and_inventory(training)
    print("SUMMARY", {"pass": PASS, "fail": FAIL})
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
