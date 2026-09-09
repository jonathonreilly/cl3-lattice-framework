#!/usr/bin/env python3
"""Bounded Cycle-269 operator implementation of the staggered catch-up.

Map the occupation of matter half-edge vertex v to n_v=(I-B_v)/2 in the
Cycle-269 square-pyramid face code.  One auxiliary reservoir M2 per coarse cell
is supplied.  The arrival-mode catch-up is the B_v-controlled transposition of
the reservoir tags at the two cells adjacent to v's unique outer face.

The runner proves that each controlled transposition is a seven-M2 involution,
preserves every local check and Wilson label, and completes the inherited outer
FSWAP stream on the declared decoded port/tag permutation.  Cycle 269
represents total-even matter only, so the lawful decoded fixture uses one
active carrier plus a separated spectator.  No encoded state execution,
bounded state encoder, or full-Fock compiler is inferred.
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
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_STAGGERED_RESERVOIR_CATCHUP_NOTE_2026-07-17.md"
)
SIZES = (3, 4, 5, 6)
HELD_OUT = 6
TOLERANCE = 5e-12

Position = tuple[int, int, int]

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
        check("the physical catch-up note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical cycle-269",
        "n_v=(i-b_v)/2",
        "one auxiliary reservoir m2 per coarse cell",
        "conditional transposition",
        "seven-m2",
        "eleven-m2",
        "local checks",
        "wilson",
        "all 24 proper-cubic frames",
        "held-out l=6",
        "even-parity spectator",
        "collision",
        "no bounded state encoder",
        "no full-fock compiler",
        "not physical time",
        "not gravity",
        "not a record",
        "supplied structure",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("the note pins the operator component and its lawful boundary", not missing, missing)


def cell_add(left: Position, right: np.ndarray, length: int) -> Position:
    return tuple(
        int((left[axis] + int(right[axis])) % length) for axis in range(3)
    )


def rotated_cell(cell: Position, frame: np.ndarray, length: int) -> Position:
    return tuple(int(value % length) for value in frame @ np.asarray(cell))


def translated_cell(cell: Position, displacement: Position, length: int) -> Position:
    return tuple((cell[axis] + displacement[axis]) % length for axis in range(3))


def outer_partner(
    code: c269.WilsonSubsystemCode, vertex: int
) -> tuple[int, int]:
    outer = [
        edge
        for edge in code.graph.incident[vertex]
        if code.graph.edges[edge][2] == "outer_square"
    ]
    if len(outer) != 1:
        raise ValueError(("matter port must have one outer edge", vertex, outer))
    edge = outer[0]
    left, right, _kind, _owner = code.graph.edges[edge]
    return (right if left == vertex else left), edge


def edge_cells(code: c269.WilsonSubsystemCode, vertex: int) -> frozenset[Position]:
    partner, _edge = outer_partner(code, vertex)
    return frozenset((code.graph.vertices[vertex][0], code.graph.vertices[partner][0]))


def catch_up_tag(
    code: c269.WilsonSubsystemCode, arrival_vertex: int, reservoir: Position
) -> Position:
    partner, _edge = outer_partner(code, arrival_vertex)
    arrival_cell = code.graph.vertices[arrival_vertex][0]
    upstream_cell = code.graph.vertices[partner][0]
    if reservoir == upstream_cell:
        return arrival_cell
    if reservoir == arrival_cell:
        return upstream_cell
    return reservoir


def stream_then_catch_up(
    code: c269.WilsonSubsystemCode, source_vertex: int, reservoir: Position
) -> tuple[int, Position]:
    arrival, _edge = outer_partner(code, source_vertex)
    return arrival, catch_up_tag(code, arrival, reservoir)


def multi_catch_up(
    code: c269.WilsonSubsystemCode,
    occupied_vertices: tuple[int, ...],
    reservoir: Position,
) -> Position:
    output = reservoir
    for vertex in occupied_vertices:
        output = catch_up_tag(code, vertex, output)
    return output


def swap_matrix(qubits: int, left: int, right: int) -> np.ndarray:
    dimension = 1 << qubits
    answer = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        left_bit = (source >> left) & 1
        right_bit = (source >> right) & 1
        target = source
        if left_bit != right_bit:
            target ^= (1 << left) | (1 << right)
        answer[target, source] = 1
    return answer


def local_physical_matrix_controls() -> None:
    print("\nLOCAL SEVEN-M2 CONDITIONAL TRANSPOSITION")
    parity_values = np.asarray(
        [(-1) ** basis.bit_count() for basis in range(1 << 5)], dtype=complex
    )
    parity = np.diag(parity_values)
    identity_faces = np.eye(1 << 5, dtype=complex)
    p_empty = (identity_faces + parity) / 2
    p_occupied = (identity_faces - parity) / 2
    swap = swap_matrix(2, 0, 1)
    identity_tags = np.eye(4, dtype=complex)
    gate = np.kron(p_empty, identity_tags) + np.kron(p_occupied, swap)
    identity = np.eye(gate.shape[0], dtype=complex)
    tag_number = np.kron(identity_faces, np.diag((0.0, 1.0, 1.0, 2.0)))

    action_failures = 0
    for face_basis in range(1 << 5):
        occupied = face_basis.bit_count() % 2
        for tag_basis in range(4):
            source = 4 * face_basis + tag_basis
            swapped_tag = (
                ((tag_basis & 1) << 1) | ((tag_basis >> 1) & 1)
                if occupied
                else tag_basis
            )
            target = 4 * face_basis + swapped_tag
            expected = np.zeros(gate.shape[0], dtype=complex)
            expected[target] = 1
            action_failures += np.linalg.norm(gate[:, source] - expected) > TOLERANCE

    check(
        "the B_v-controlled auxiliary swap is an exact seven-M2 number-preserving involution",
        np.linalg.norm(gate.conj().T @ gate - identity) < TOLERANCE
        and np.linalg.norm(gate @ gate - identity) < TOLERANCE
        and np.linalg.norm(gate @ tag_number - tag_number @ gate) < TOLERANCE
        and action_failures == 0,
        {
            "physical_dimension": gate.shape[0],
            "unitarity_residual": float(np.linalg.norm(gate.conj().T @ gate - identity)),
            "involution_residual": float(np.linalg.norm(gate @ gate - identity)),
            "reservoir_number_commutator": float(
                np.linalg.norm(gate @ tag_number - tag_number @ gate)
            ),
            "basis_action_failures": action_failures,
        },
    )


def mapped_support_and_leakage_controls() -> dict[int, c269.WilsonSubsystemCode]:
    print("\nMAPPED B_v CONTROLS / SUPPORT / CHECK LEAKAGE")
    cache = {}
    rows = []
    for length in SIZES:
        code = c269.build_code(length)
        cache[length] = code
        catchup_supports = []
        stream_supports = []
        macro_supports = []
        port_failures = 0
        b_control_form_failures = 0
        catchup_leakage = 0
        stream_generator_leakage = 0
        for vertex, (cell, direction) in enumerate(code.graph.vertices):
            partner, edge = outer_partner(code, vertex)
            partner_cell, partner_direction = code.graph.vertices[partner]
            expected_cell = cell_add(cell, c210.DIRECTIONS[direction], length)
            port_failures += partner_cell != expected_cell
            port_failures += partner_direction != (direction ^ 1)

            b_vertex = code.B[vertex]
            b_control_form_failures += (
                b_vertex.phase != 0
                or b_vertex.x != 0
                or b_vertex.z.bit_count() != 5
            )
            catchup_supports.append((b_vertex.x | b_vertex.z).bit_count() + 2)
            catchup_leakage += sum(
                not b_vertex.commutes(row)
                for row in code.local_checks + code.wilsons
            )

            left, right, kind, _owner = code.graph.edges[edge]
            port_failures += kind != "outer_square"
            stream_terms = (code.B[left], code.B[right], code.A[edge])
            face_union = 0
            for operator in stream_terms:
                face_union |= operator.x | operator.z
                stream_generator_leakage += sum(
                    not operator.commutes(row)
                    for row in code.local_checks + code.wilsons
                )
            stream_supports.append(face_union.bit_count())
            macro_supports.append(face_union.bit_count() + 2)

        rows.append(
            {
                "L": length,
                "held_out": length == HELD_OUT,
                "face_M2_per_cell": 15,
                "auxiliary_reservoir_M2_per_cell": 1,
                "matter_ports": len(code.graph.vertices),
                "catchup_gate_supports": sorted(set(catchup_supports)),
                "outer_FSWAP_supports": sorted(set(stream_supports)),
                "staggered_gate_union_supports": sorted(set(macro_supports)),
                "port_decoder_failures": port_failures,
                "pure_Z_weight_five_B_control_failures": b_control_form_failures,
                "catchup_check_or_Wilson_leakage": catchup_leakage,
                "stream_term_check_or_Wilson_leakage": stream_generator_leakage,
            }
        )

    check(
        "mapped arrival occupations control bounded gates with zero local-check and Wilson leakage through held-out L=6",
        all(
            row["catchup_gate_supports"] == [7]
            and row["outer_FSWAP_supports"] == [9]
            and row["staggered_gate_union_supports"] == [11]
            and row["port_decoder_failures"] == 0
            and row["pure_Z_weight_five_B_control_failures"] == 0
            and row["catchup_check_or_Wilson_leakage"] == 0
            and row["stream_term_check_or_Wilson_leakage"] == 0
            for row in rows
        ),
        rows,
    )
    return cache


def port_tag_macrostep_controls(cache: dict[int, c269.WilsonSubsystemCode]) -> None:
    print("\nPORT/TAG MACROSTEP / INVOLUTION / HELD SIZE")
    rows = []
    for length, code in cache.items():
        targets = set()
        inverse_failures = 0
        macrostep_failures = 0
        omitted_catchup_failures = 0
        for vertex in range(len(code.graph.vertices)):
            for reservoir in code.graph.cells:
                output = catch_up_tag(code, vertex, reservoir)
                targets.add((vertex, output))
                inverse_failures += (
                    catch_up_tag(code, vertex, output) != reservoir
                )

            source_cell = code.graph.vertices[vertex][0]
            arrival, caught = stream_then_catch_up(code, vertex, source_cell)
            arrival_cell = code.graph.vertices[arrival][0]
            macrostep_failures += caught != arrival_cell
            omitted_catchup_failures += source_cell != arrival_cell

        basis_size = len(code.graph.vertices) * len(code.graph.cells)
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_OUT,
                "port_tag_basis": basis_size,
                "permutation_image_size": len(targets),
                "catchup_inverse_failures": inverse_failures,
                "staggered_vs_co_moving_failures": macrostep_failures,
                "fixed_stream_mismatches_without_catchup": omitted_catchup_failures,
            }
        )

    check(
        "the decoded port/tag permutation is bijective and exactly completes fixed stream to co-moving transport through held-out L=6",
        all(
            row["permutation_image_size"] == row["port_tag_basis"]
            and row["catchup_inverse_failures"] == 0
            and row["staggered_vs_co_moving_failures"] == 0
            and row["fixed_stream_mismatches_without_catchup"] == 6 * row["L"] ** 3
            for row in rows
        ),
        rows,
    )


def covariance_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nPROPER-CUBIC / TRANSLATION COVARIANCE")
    graph = code.graph
    frame_failures = 0
    frame_tests = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(graph, frame)
        toggles, pairs, flips = c269.repair_data(graph, vertex_map, edge_map)
        for vertex in range(len(graph.vertices)):
            partner, edge = outer_partner(code, vertex)
            mapped_vertex = vertex_map[vertex]
            mapped_partner, mapped_edge = outer_partner(code, mapped_vertex)
            frame_failures += mapped_partner != vertex_map[partner]
            frame_failures += mapped_edge != edge_map[edge]
            frame_failures += (
                c235.permute_pauli(code.B[vertex], edge_map)
                != code.B[mapped_vertex]
            )
            transformed_a = c235.apply_gauge(
                c235.permute_pauli(code.A[edge], edge_map),
                toggles,
                pairs,
                flips,
            )
            source, target, _kind, _owner = graph.edges[edge]
            frame_failures += transformed_a != graph.A(
                vertex_map[source], vertex_map[target]
            )
            for reservoir in graph.cells:
                rotated_reservoir = rotated_cell(reservoir, frame, code.length)
                left = rotated_cell(
                    catch_up_tag(code, vertex, reservoir), frame, code.length
                )
                right = catch_up_tag(code, mapped_vertex, rotated_reservoir)
                frame_failures += left != right
                frame_tests += 1

    translation_failures = 0
    translation_tests = 0
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(graph, displacement)
        for vertex in range(len(graph.vertices)):
            partner, edge = outer_partner(code, vertex)
            mapped_vertex = vertex_map[vertex]
            mapped_partner, mapped_edge = outer_partner(code, mapped_vertex)
            translation_failures += mapped_partner != vertex_map[partner]
            translation_failures += mapped_edge != edge_map[edge]
            for reservoir in graph.cells:
                moved_reservoir = translated_cell(
                    reservoir, displacement, code.length
                )
                left = translated_cell(
                    catch_up_tag(code, vertex, reservoir),
                    displacement,
                    code.length,
                )
                right = catch_up_tag(code, mapped_vertex, moved_reservoir)
                translation_failures += left != right
                translation_tests += 1

    check(
        "the mapped outer-FSWAP/catch-up descriptor and decoded tag action are covariant under all 24 proper-cubic frames and all L=3 translations",
        len(c235.proper_cubic_frames()) == 24
        and frame_failures == 0
        and translation_failures == 0,
        {
            "proper_frames": len(c235.proper_cubic_frames()),
            "frame_port_tag_tests": frame_tests,
            "frame_failures": frame_failures,
            "translations": code.length**3,
            "translation_port_tag_tests": translation_tests,
            "translation_failures": translation_failures,
        },
    )


def separated_spectator(
    code: c269.WilsonSubsystemCode, mobile: int
) -> int | None:
    mobile_edge = edge_cells(code, mobile)
    return next(
        (
            candidate
            for candidate in range(len(code.graph.vertices))
            if candidate != mobile
            and mobile_edge.isdisjoint(edge_cells(code, candidate))
        ),
        None,
    )


def separated_spectator_for_ports(
    code: c269.WilsonSubsystemCode, mobiles: tuple[int, ...]
) -> int | None:
    occupied_cells = frozenset().union(*(edge_cells(code, vertex) for vertex in mobiles))
    return next(
        (
            candidate
            for candidate in range(len(code.graph.vertices))
            if candidate not in mobiles
            and occupied_cells.isdisjoint(edge_cells(code, candidate))
        ),
        None,
    )


def validate_even_domain(
    code: c269.WilsonSubsystemCode,
    mobile: int,
    spectator: int | None,
    reservoir: Position,
) -> None:
    if spectator is None:
        raise ValueError("Cycle-269 requires an even-parity spectator")
    if spectator == mobile:
        raise ValueError("mobile and spectator modes must be distinct")
    if reservoir != code.graph.vertices[mobile][0]:
        raise ValueError("the incoming local image has the tag at the mobile cell")
    if not edge_cells(code, mobile).isdisjoint(edge_cells(code, spectator)):
        raise ValueError("the active and spectator tag-swap edges collide")


def lawful_even_sector_controls(cache: dict[int, c269.WilsonSubsystemCode]) -> None:
    print("\nTOTAL-EVEN SPECTATOR DOMAIN / COLLISION CONTROL")
    rows = []
    for length, code in cache.items():
        failures = 0
        order_failures = 0
        inverse_failures = 0
        fixed_spectator_blocks = 0
        for body in code.graph.cells:
            mobiles = tuple(
                code.graph.vertex_index[(body, direction)] for direction in range(6)
            )
            spectator = separated_spectator_for_ports(code, mobiles)
            if spectator is None:
                failures += 1
                continue
            fixed_spectator_blocks += 1
            for mobile in mobiles:
                reservoir = code.graph.vertices[mobile][0]
                validate_even_domain(code, mobile, spectator, reservoir)
                mobile_arrival, _ = outer_partner(code, mobile)
                spectator_arrival, _ = outer_partner(code, spectator)
                controls = (mobile_arrival, spectator_arrival)
                forward = multi_catch_up(code, controls, reservoir)
                reverse_order = multi_catch_up(
                    code, tuple(reversed(controls)), reservoir
                )
                target = code.graph.vertices[mobile_arrival][0]
                failures += forward != target
                order_failures += reverse_order != forward
                inverse_failures += (
                    multi_catch_up(code, controls, forward) != reservoir
                )
        rows.append(
            {
                "L": length,
                "held_out": length == HELD_OUT,
                "fixed_spectator_direction_blocks": fixed_spectator_blocks,
                "lawful_mobile_ports": 6 * fixed_spectator_blocks,
                "macrostep_failures": failures,
                "control_order_failures": order_failures,
                "catchup_inverse_failures": inverse_failures,
            }
        )

    check(
        "one active carrier plus a disjoint even-parity spectator exactly preserves the decoded reversible catch-up action through held-out L=6",
        all(
            row["fixed_spectator_direction_blocks"] == row["L"] ** 3
            and row["lawful_mobile_ports"] == 6 * row["L"] ** 3
            and row["macrostep_failures"] == 0
            and row["control_order_failures"] == 0
            and row["catchup_inverse_failures"] == 0
            for row in rows
        ),
        rows,
    )

    code = cache[3]
    body = (0, 0, 0)
    first = code.graph.vertex_index[(body, 0)]
    second = code.graph.vertex_index[(body, 2)]
    rejected = 0
    fixtures = (
        (first, None, body),
        (first, first, body),
        (first, second, body),
        (first, separated_spectator(code, first), (1, 1, 1)),
    )
    for fixture in fixtures:
        try:
            validate_even_domain(code, *fixture)
        except ValueError:
            rejected += 1

    order_left = multi_catch_up(code, (first, second), body)
    order_right = multi_catch_up(code, (second, first), body)
    swap_first = swap_matrix(3, 0, 1)
    swap_second = swap_matrix(3, 0, 2)
    collision_commutator = float(
        np.linalg.norm(swap_first @ swap_second - swap_second @ swap_first, 2)
    )
    check(
        "the lawful-domain guard rejects odd, coincident, overlapping-edge, and mistagged fixtures while exposing the multiparticle schedule collision",
        rejected == len(fixtures)
        and order_left != order_right
        and collision_commutator > 1,
        {
            "rejected_fixtures": rejected,
            "overlapping_edge_order_outputs": (order_left, order_right),
            "overlapping_swap_commutator_operator_norm": collision_commutator,
            "meaning": "unfinished multiparticle schedule, not a shared obstruction",
        },
    )


def scope_controls() -> None:
    print("\nSCOPE / SUPPLIED STRUCTURE")
    check(
        "the result is a bounded physical catch-up gate plus decoded operator-action controls, not a state or full-Fock compiler",
        True,
        {
            "executed": (
                "the n_v=(I-B_v)/2 controlled auxiliary transposition as a seven-M2 matrix",
                "outer-FSWAP then catch-up equality on the complete decoded port/tag permutation",
                "local-check/Wilson preservation plus descriptor-level covariance, inverse, held-size, and lawful-domain controls",
            ),
            "not_executed": (
                "a bounded Cycle-269 state encoder E",
                "E G_coarse = G_physical E on a full physical state code",
                "an assembled full stream/catch-up macrostep matrix on encoded states",
                "multiparticle collision scheduling",
                "contact, stationary dressing, energy, gravity, clock, Record, or Born semantics",
            ),
            "authority": "none",
            "audit": "unset",
            "axiom_pressure": False,
        },
    )


def main() -> int:
    note_contract()
    local_physical_matrix_controls()
    cache = mapped_support_and_leakage_controls()
    port_tag_macrostep_controls(cache)
    covariance_controls(cache[3])
    lawful_even_sector_controls(cache)
    scope_controls()
    print(
        "DIAGNOSTIC",
        {
            "physical_code": "Cycle-269 local-check-only square-pyramid face code",
            "mapped_control": "n_v=(I-B_v)/2",
            "auxiliary_overhead": "one reservoir M2 per coarse cell",
            "catchup_support_M2": 7,
            "outer_FSWAP_plus_catchup_union_M2": 11,
            "held_out": HELD_OUT,
            "lawful_matter_domain": "one-cell six-direction active block plus one fixed disjoint spectator (total even)",
            "decoded_action_only": True,
            "state_compiler": False,
        },
    )
    print(f"TOTAL PASS={PASS} FAIL={FAIL}")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
