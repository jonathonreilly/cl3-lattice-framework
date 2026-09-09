#!/usr/bin/env python3
"""Collision-safe auxiliary-port catch-up for the physical Cycle-269 code.

Replace the single reservoir M2 at a coarse cell by one auxiliary M2 for each
of its six matter half-edge ports.  On every undirected outer edge (u,v), use
the local XOR occupation control (I-B_u B_v)/2 to swap only the two paired
port auxiliaries.  Outer edges partition the port auxiliaries and every face
control is diagonal, so the catch-up gates commute despite bounded overlaps
of their physical face support.  The product therefore needs no physical
axis order or global parity service.

This runner proves the bounded operator and decoded multiparticle catch-up
word.  It does not construct a physical state encoder or the local joint
matter-coin/port-routing update required by a full-Fock compiler.
"""

from __future__ import annotations

from itertools import combinations, product
from pathlib import Path
import sys

import numpy as np
from scipy import sparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import exact_3d_higher_form_bosonization_cycle235_2026_07_17 as c235
import physical_cycle269_staggered_reservoir_catchup_2026_07_17 as old
import wilson_subsystem_sector_free_compiler_cycle269_2026_07_17 as c269


NOTE = ROOT / (
    "docs/work_history/repo/review_feedback/"
    "PHYSICAL_CYCLE269_COLLISION_SAFE_AUXILIARY_PORTS_NOTE_2026-07-17.md"
)
TRAINING_SIZES = (3, 4, 5)
HELD_SIZES = (6,)
SIZES = TRAINING_SIZES + HELD_SIZES
TOLERANCE = 5e-12

Position = tuple[int, int, int]
OuterEdge = tuple[int, int, int]

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
        check("the collision-safe auxiliary-port note exists", False, NOTE)
        return
    text = normalized(NOTE)
    required = (
        "authority: none",
        "audit: unset",
        "physical cycle-269",
        "six auxiliary port m2 per coarse cell",
        "(i-b_u b_v)/2",
        "ten-m2",
        "local port constraint",
        "multiparticle",
        "all 24 proper-cubic frames",
        "all l=3 translations",
        "held l=6",
        "inverse",
        "constraint leakage",
        "decoded four-bit",
        "not an assembled encoded",
        "collision deletion",
        "preferred frame",
        "substep schedule is not physical time",
        "no global parity service",
        "no host-side control",
        "bounded state encoder remains open",
        "local matter-coin/port routing remains open",
        "no no-go claim",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check(
        "the note pins the auxiliary-port construction, controls, and open boundary",
        not missing,
        missing,
    )


def outer_edges(code: c269.WilsonSubsystemCode) -> tuple[OuterEdge, ...]:
    return tuple(
        (left, right, edge)
        for edge, (left, right, kind, _owner) in enumerate(code.graph.edges)
        if kind == "outer_square"
    )


def swap_bits(bits: int, left: int, right: int) -> int:
    if ((bits >> left) ^ (bits >> right)) & 1:
        bits ^= (1 << left) | (1 << right)
    return bits


def stream_occupations(
    code: c269.WilsonSubsystemCode, occupations: int
) -> tuple[int, int]:
    """Outer FSWAP layer on decoded occupations and its fermionic sign."""

    output = occupations
    sign = 1
    for left, right, _edge in outer_edges(code):
        left_bit = (occupations >> left) & 1
        right_bit = (occupations >> right) & 1
        if left_bit and right_bit:
            sign *= -1
        output = swap_bits(output, left, right)
    return output, sign


def auxiliary_port_catchup(
    code: c269.WilsonSubsystemCode,
    arrival_occupations: int,
    port_tags: int,
    order: tuple[OuterEdge, ...] | None = None,
) -> int:
    """Apply the XOR-controlled port swaps in any supplied enumeration."""

    output = port_tags
    edges = outer_edges(code) if order is None else order
    for left, right, _edge in edges:
        occupied_xor = ((arrival_occupations >> left) ^ (arrival_occupations >> right)) & 1
        if occupied_xor:
            output = swap_bits(output, left, right)
    return output


def port_macrostep(
    code: c269.WilsonSubsystemCode,
    occupations: int,
    port_tags: int,
    order: tuple[OuterEdge, ...] | None = None,
) -> tuple[int, int, int]:
    arrival, sign = stream_occupations(code, occupations)
    caught = auxiliary_port_catchup(code, arrival, port_tags, order)
    return arrival, caught, sign


def port_constraint_holds(occupations: int, port_tags: int) -> bool:
    return occupations == port_tags


def validate_port_domain(
    code: c269.WilsonSubsystemCode, occupations: int, port_tags: int
) -> None:
    limit = 1 << len(code.graph.vertices)
    if occupations < 0 or occupations >= limit or port_tags < 0 or port_tags >= limit:
        raise ValueError("occupation and tag masks must fit the finite port set")
    if occupations.bit_count() % 2:
        raise ValueError("Cycle-269 exposes the total-even matter algebra")
    if not port_constraint_holds(occupations, port_tags):
        raise ValueError("the local B_v Z_port(v)=+1 constraint is not satisfied")


def local_sparse_swap(qubits: int, left: int, right: int) -> sparse.csr_matrix:
    dimension = 1 << qubits
    rows = np.empty(dimension, dtype=int)
    for source in range(dimension):
        rows[source] = swap_bits(source, left, right)
    return sparse.csr_matrix(
        (np.ones(dimension), (rows, np.arange(dimension))),
        shape=(dimension, dimension),
    )


def local_ten_m2_matrix_controls() -> None:
    print("\nLOCAL TEN-M2 XOR-CONTROLLED PORT SWAP")
    face_qubits = 8
    tag_qubits = 2
    qubits = face_qubits + tag_qubits
    dimension = 1 << qubits
    parity = np.asarray(
        [(-1) ** (basis & ((1 << face_qubits) - 1)).bit_count() for basis in range(dimension)]
    )
    odd = (1 - parity) / 2
    swap = local_sparse_swap(qubits, face_qubits, face_qubits + 1)
    identity = sparse.eye(dimension, dtype=complex, format="csr")
    gate = sparse.diags(1 - odd, format="csr") + sparse.diags(odd, format="csr") @ swap
    tag_number = sparse.diags(
        [
            ((basis >> face_qubits) & 1)
            + ((basis >> (face_qubits + 1)) & 1)
            for basis in range(dimension)
        ],
        dtype=float,
        format="csr",
    )
    action_failures = 0
    for source in range(dimension):
        expected = (
            swap_bits(source, face_qubits, face_qubits + 1)
            if odd[source]
            else source
        )
        column = gate.getcol(source)
        action_failures += not (
            column.nnz == 1
            and column.indices[0] == 0
            and column.nonzero()[0][0] == expected
            and abs(column.data[0] - 1) < TOLERANCE
        )
    unitarity = float(sparse.linalg.norm(gate.conj().T @ gate - identity))
    involution = float(sparse.linalg.norm(gate @ gate - identity))
    number_commutator = float(sparse.linalg.norm(gate @ tag_number - tag_number @ gate))
    check(
        "the local XOR-controlled auxiliary transposition is an exact ten-M2 auxiliary-tag-number-preserving involution",
        action_failures == 0
        and unitarity < TOLERANCE
        and involution < TOLERANCE
        and number_commutator < TOLERANCE,
        {
            "dimension": dimension,
            "face_control_weight": face_qubits,
            "auxiliary_ports": tag_qubits,
            "basis_action_failures": action_failures,
            "unitarity_residual": unitarity,
            "involution_residual": involution,
            "tag_number_commutator": number_commutator,
        },
    )


def local_abstract_macro_matrix(
    include_catchup: bool = True,
) -> np.ndarray:
    """Two matter modes plus their two port tags, ordered by bit index."""

    dimension = 16
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        matter = source & 0b0011
        tags = (source >> 2) & 0b0011
        both = matter == 0b0011
        streamed_matter = swap_bits(matter, 0, 1)
        caught_tags = tags
        if include_catchup and (streamed_matter in (0b0001, 0b0010)):
            caught_tags = swap_bits(tags, 0, 1)
        target = streamed_matter | (caught_tags << 2)
        matrix[target, source] = -1 if both else 1
    return matrix


def local_constraint_and_deletion_controls() -> None:
    print("\nLOCAL PORT CONSTRAINT / INVERSE / CATCH-UP DELETION")
    macro = local_abstract_macro_matrix(True)
    deleted = local_abstract_macro_matrix(False)
    identity = np.eye(16, dtype=complex)
    projector = np.diag(
        [1.0 if (basis & 0b0011) == ((basis >> 2) & 0b0011) else 0.0 for basis in range(16)]
    )
    leakage = float(np.linalg.norm((identity - projector) @ macro @ projector, 2))
    deleted_leakage = float(
        np.linalg.norm((identity - projector) @ deleted @ projector, 2)
    )
    code_action_failures = 0
    for matter in range(4):
        source = matter | (matter << 2)
        streamed = swap_bits(matter, 0, 1)
        target = streamed | (streamed << 2)
        expected_phase = -1 if matter == 3 else 1
        code_action_failures += abs(macro[target, source] - expected_phase) > TOLERANCE
    check(
        "the two-port stream/catch-up word is unitary, involutive, and preserves the local B_v Z_port constraint",
        np.linalg.norm(macro.conj().T @ macro - identity) < TOLERANCE
        and np.linalg.norm(macro @ macro - identity) < TOLERANCE
        and np.linalg.norm(macro @ projector - projector @ macro) < TOLERANCE
        and leakage < TOLERANCE
        and code_action_failures == 0,
        {
            "unitarity_residual": float(np.linalg.norm(macro.conj().T @ macro - identity)),
            "inverse_residual": float(np.linalg.norm(macro @ macro - identity)),
            "constraint_commutator": float(np.linalg.norm(macro @ projector - projector @ macro)),
            "constraint_leakage": leakage,
            "code_basis_action_failures": code_action_failures,
        },
    )
    check(
        "deleting the auxiliary catch-up produces unit constraint leakage on a one-carrier edge fixture",
        deleted_leakage > 0.99,
        {"deleted_catchup_constraint_leakage_operator_norm": deleted_leakage},
    )


def mapped_support_commutation_controls() -> dict[int, c269.WilsonSubsystemCode]:
    print("\nMAPPED XOR SUPPORT / COMMUTATION / LOCAL-CHECK LEAKAGE")
    cache = {}
    rows = []
    for length in SIZES:
        code = c269.build_code(length)
        cache[length] = code
        edges = outer_edges(code)
        controls = [code.B[left] @ code.B[right] for left, right, _edge in edges]
        support_weights = [control.z.bit_count() for control in controls]
        stream_supports = []
        macro_union_supports = []
        leakage = sum(
            not control.commutes(row)
            for control in controls
            for row in code.local_checks + code.wilsons
        )
        control_failures = sum(
            control.phase != 0 or control.x != 0 for control in controls
        )
        port_degree = [0] * len(code.graph.vertices)
        face_incidence = [0] * len(code.graph.edges)
        for (left, right, edge), control in zip(edges, controls):
            port_degree[left] += 1
            port_degree[right] += 1
            stream_face_union = 0
            for operator in (code.B[left], code.B[right], code.A[edge]):
                stream_face_union |= operator.x | operator.z
            stream_supports.append(stream_face_union.bit_count())
            macro_union_supports.append(
                (stream_face_union | control.x | control.z).bit_count() + 2
            )
            for face in range(len(code.graph.edges)):
                face_incidence[face] += (control.z >> face) & 1
        conflict_degrees = []
        anticommuting_pairs = 0
        for index, control in enumerate(controls):
            conflict_degrees.append(
                sum(
                    other != index and bool(control.z & candidate.z)
                    for other, candidate in enumerate(controls)
                )
            )
            anticommuting_pairs += sum(
                not control.commutes(candidate)
                for candidate in controls[index + 1 :]
            )
        extended_qubits = code.qubits + len(code.graph.vertices)
        port_constraints = tuple(
            c235.Pauli(
                0,
                0,
                code.B[vertex].z | (1 << (code.qubits + vertex)),
            )
            for vertex in range(len(code.graph.vertices))
        )
        inherited_local_rank = c269.rank(list(code.local_checks), code.qubits)
        inherited_fixed_rank = c269.rank(
            list(code.local_checks + code.wilsons), code.qubits
        )
        extended_local_rank = c269.rank(
            list(code.local_checks) + list(port_constraints), extended_qubits
        )
        extended_fixed_rank = c269.rank(
            list(code.local_checks + code.wilsons) + list(port_constraints),
            extended_qubits,
        )
        port_constraint_commutation_failures = sum(
            not constraint.commutes(row)
            for constraint in port_constraints
            for row in code.local_checks + code.wilsons + port_constraints
        )
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "outer_edges": len(edges),
                "face_M2_per_cell": code.qubits // length**3,
                "port_M2_per_cell": len(code.graph.vertices) // length**3,
                "total_face_plus_port_M2_per_cell": extended_qubits // length**3,
                "XOR_control_face_weights": sorted(set(support_weights)),
                "catchup_support_M2": sorted(set(weight + 2 for weight in support_weights)),
                "outer_FSWAP_support_M2": sorted(set(stream_supports)),
                "outer_FSWAP_plus_catchup_union_M2": sorted(
                    set(macro_union_supports)
                ),
                "port_outer_edge_degrees": sorted(set(port_degree)),
                "maximum_face_control_incidence": max(face_incidence),
                "maximum_support_conflict_degree": max(conflict_degrees),
                "noncommuting_control_pairs": anticommuting_pairs,
                "control_form_failures": control_failures,
                "local_check_or_Wilson_leakage": leakage,
                "local_port_constraint_count": len(port_constraints),
                "local_port_constraint_rank": c235.gf2_rank(
                    constraint.z for constraint in port_constraints
                ),
                "port_constraint_commutation_failures": (
                    port_constraint_commutation_failures
                ),
                "local_rank_increment_from_port_constraints": (
                    extended_local_rank - inherited_local_rank
                ),
                "fixed_rank_increment_from_port_constraints": (
                    extended_fixed_rank - inherited_fixed_rank
                ),
                "local_code_exponent_before_ports": (
                    code.qubits - inherited_local_rank
                ),
                "local_code_exponent_after_port_constraints": (
                    extended_qubits - extended_local_rank
                ),
            }
        )
    check(
        "every outer edge has a bounded pure-Z XOR control, unique port pair, and zero local-check/Wilson leakage through held L=6",
        all(
            row["outer_edges"] == 3 * row["L"] ** 3
            and row["face_M2_per_cell"] == 15
            and row["port_M2_per_cell"] == 6
            and row["total_face_plus_port_M2_per_cell"] == 21
            and row["XOR_control_face_weights"] == [8]
            and row["catchup_support_M2"] == [10]
            and row["outer_FSWAP_support_M2"] == [9]
            and row["outer_FSWAP_plus_catchup_union_M2"] == [11]
            and row["port_outer_edge_degrees"] == [1]
            and row["maximum_face_control_incidence"] == 2
            and row["maximum_support_conflict_degree"] == 8
            and row["noncommuting_control_pairs"] == 0
            and row["control_form_failures"] == 0
            and row["local_check_or_Wilson_leakage"] == 0
            and row["local_port_constraint_count"] == 6 * row["L"] ** 3
            and row["local_port_constraint_rank"]
            == row["local_port_constraint_count"]
            and row["port_constraint_commutation_failures"] == 0
            and row["local_rank_increment_from_port_constraints"]
            == row["local_port_constraint_count"]
            and row["fixed_rank_increment_from_port_constraints"]
            == row["local_port_constraint_count"]
            and row["local_code_exponent_after_port_constraints"]
            == row["local_code_exponent_before_ports"]
            for row in rows
        ),
        rows,
    )
    return cache


def random_even_mask(rng: np.random.Generator, modes: int) -> int:
    words = rng.integers(0, 1 << 63, size=(modes + 62) // 63, dtype=np.uint64)
    value = 0
    for word_index, word in enumerate(words):
        value |= int(word) << (63 * word_index)
    value &= (1 << modes) - 1
    if value.bit_count() % 2:
        value ^= 1
    return value


def multiparticle_held_size_controls(
    cache: dict[int, c269.WilsonSubsystemCode]
) -> None:
    print("\nMULTIPARTICLE COLLISIONS / ORDER / INVERSE / HELD SIZE")
    rng = np.random.default_rng(20260717269)
    rows = []
    for length, code in cache.items():
        edges = outer_edges(code)
        reverse = tuple(reversed(edges))
        shuffled_list = list(edges)
        rng.shuffle(shuffled_list)
        shuffled = tuple(shuffled_list)
        collision_fixtures = 0
        collision_failures = 0
        order_failures = 0
        inverse_failures = 0
        constraint_failures = 0
        phase_failures = 0
        for body in code.graph.cells:
            local_ports = tuple(
                code.graph.vertex_index[(body, direction)] for direction in range(6)
            )
            for subset in range(1 << 6):
                if subset.bit_count() % 2:
                    continue
                occupations = sum(
                    ((subset >> local_index) & 1) << vertex
                    for local_index, vertex in enumerate(local_ports)
                )
                collision_fixtures += 1
                forward = port_macrostep(code, occupations, occupations, edges)
                reverse_word = port_macrostep(code, occupations, occupations, reverse)
                shuffled_word = port_macrostep(code, occupations, occupations, shuffled)
                collision_failures += not port_constraint_holds(forward[0], forward[1])
                order_failures += forward != reverse_word or forward != shuffled_word
                back = port_macrostep(code, forward[0], forward[1], shuffled)
                inverse_failures += back[:2] != (occupations, occupations)
                phase_failures += back[2] * forward[2] != 1

        random_fixtures = 128
        for _ in range(random_fixtures):
            occupations = random_even_mask(rng, len(code.graph.vertices))
            validate_port_domain(code, occupations, occupations)
            output = port_macrostep(code, occupations, occupations, shuffled)
            constraint_failures += not port_constraint_holds(output[0], output[1])
            arbitrary_tags = random_even_mask(rng, len(code.graph.vertices))
            first = port_macrostep(code, occupations, arbitrary_tags, reverse)
            second = port_macrostep(code, first[0], first[1], edges)
            inverse_failures += second[:2] != (occupations, arbitrary_tags)
            phase_failures += first[2] * second[2] != 1
        rows.append(
            {
                "L": length,
                "held": length in HELD_SIZES,
                "same_cell_even_collision_fixtures": collision_fixtures,
                "random_even_multiparticle_fixtures": random_fixtures,
                "constraint_failures": constraint_failures,
                "same_cell_collision_failures": collision_failures,
                "edge_order_failures": order_failures,
                "inverse_failures": inverse_failures,
                "FSWAP_phase_inverse_failures": phase_failures,
            }
        )
    check(
        "the port layer closes all same-cell even multiparticle collisions and random even fixtures independent of edge enumeration through held L=6",
        all(
            row["same_cell_even_collision_fixtures"] == 32 * row["L"] ** 3
            and row["constraint_failures"] == 0
            and row["same_cell_collision_failures"] == 0
            and row["edge_order_failures"] == 0
            and row["inverse_failures"] == 0
            and row["FSWAP_phase_inverse_failures"] == 0
            for row in rows
        ),
        rows,
    )


def permute_bits(bits: int, vertex_map: list[int]) -> int:
    output = 0
    for source, target in enumerate(vertex_map):
        output |= ((bits >> source) & 1) << target
    return output


def covariance_and_translation_controls(code: c269.WilsonSubsystemCode) -> None:
    print("\nALL-FRAME / ALL-TRANSLATION AUXILIARY-PORT COVARIANCE")
    rng = np.random.default_rng(20260717270)
    fixtures = []
    for _ in range(24):
        occupations = random_even_mask(rng, len(code.graph.vertices))
        tags = random_even_mask(rng, len(code.graph.vertices))
        fixtures.append((occupations, tags))

    frame_failures = 0
    frame_tests = 0
    for frame in c235.proper_cubic_frames():
        vertex_map, edge_map = c235.graph_frame_maps(code.graph, frame)
        for left, right, edge in outer_edges(code):
            mapped_left = vertex_map[left]
            mapped_right = vertex_map[right]
            mapped_edge = code.graph.edge_between(mapped_left, mapped_right)
            frame_failures += mapped_edge != edge_map[edge]
            framed_control = c235.permute_pauli(code.B[left] @ code.B[right], edge_map)
            frame_failures += framed_control != code.B[mapped_left] @ code.B[mapped_right]
            frame_failures += (
                c235.permute_pauli(code.B[left], edge_map) != code.B[mapped_left]
            )
            frame_failures += (
                c235.permute_pauli(code.B[right], edge_map) != code.B[mapped_right]
            )
        for occupations, tags in fixtures:
            output = port_macrostep(code, occupations, tags)
            framed_input = (
                permute_bits(occupations, vertex_map),
                permute_bits(tags, vertex_map),
            )
            framed_output = port_macrostep(code, *framed_input)
            expected = (
                permute_bits(output[0], vertex_map),
                permute_bits(output[1], vertex_map),
                output[2],
            )
            frame_failures += framed_output != expected
            frame_tests += 1

    translation_failures = 0
    translation_tests = 0
    for displacement in product(range(code.length), repeat=3):
        vertex_map, edge_map = c269.graph_translation_maps(code.graph, displacement)
        for left, right, edge in outer_edges(code):
            mapped_left = vertex_map[left]
            mapped_right = vertex_map[right]
            mapped_edge = code.graph.edge_between(mapped_left, mapped_right)
            translation_failures += mapped_edge != edge_map[edge]
            translated_control = c235.permute_pauli(
                code.B[left] @ code.B[right], edge_map
            )
            translation_failures += (
                translated_control != code.B[mapped_left] @ code.B[mapped_right]
            )
            translation_failures += (
                c235.permute_pauli(code.B[left], edge_map) != code.B[mapped_left]
            )
            translation_failures += (
                c235.permute_pauli(code.B[right], edge_map) != code.B[mapped_right]
            )
        for occupations, tags in fixtures:
            output = port_macrostep(code, occupations, tags)
            moved_input = (
                permute_bits(occupations, vertex_map),
                permute_bits(tags, vertex_map),
            )
            moved_output = port_macrostep(code, *moved_input)
            expected = (
                permute_bits(output[0], vertex_map),
                permute_bits(output[1], vertex_map),
                output[2],
            )
            translation_failures += moved_output != expected
            translation_tests += 1
    check(
        "the XOR control, individual port-constraint descriptors, auxiliary endpoints, decoded macrostep, and FSWAP sign are covariant under all 24 proper-cubic frames and all L=3 translations",
        len(c235.proper_cubic_frames()) == 24
        and frame_failures == 0
        and translation_failures == 0,
        {
            "proper_frames": len(c235.proper_cubic_frames()),
            "frame_decoded_tests": frame_tests,
            "frame_failures": frame_failures,
            "translations": code.length**3,
            "translation_decoded_tests": translation_tests,
            "translation_failures": translation_failures,
        },
    )


def permutation_matrix(qubits: int, mapping: tuple[int, ...]) -> np.ndarray:
    dimension = 1 << qubits
    matrix = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        target = 0
        for old, new in enumerate(mapping):
            target |= ((source >> old) & 1) << new
        matrix[target, source] = 1
    return matrix


def color_phase_and_preferred_frame_audit() -> None:
    print("\nCOLOR/PHASE SCHEDULE AND PREFERRED-FRAME AUDIT")
    axis_word = np.eye(16, dtype=complex)
    for endpoint in (1, 2, 3):
        axis_word = old.swap_matrix(4, 0, endpoint) @ axis_word
    axis_cycle = permutation_matrix(4, (0, 2, 3, 1))
    rotated_axis_word = axis_cycle @ axis_word @ axis_cycle.conj().T
    axis_frame_residual = float(np.linalg.norm(rotated_axis_word - axis_word, 2))
    reverse_axis_word = np.eye(16, dtype=complex)
    for endpoint in (3, 2, 1):
        reverse_axis_word = old.swap_matrix(4, 0, endpoint) @ reverse_axis_word
    axis_order_residual = float(np.linalg.norm(reverse_axis_word - axis_word, 2))

    port_word = np.eye(64, dtype=complex)
    port_swaps = tuple(old.swap_matrix(6, left, right) for left, right in ((0, 1), (2, 3), (4, 5)))
    for gate in port_swaps:
        port_word = gate @ port_word
    port_cycle = permutation_matrix(6, (2, 3, 4, 5, 0, 1))
    rotated_port_word = port_cycle @ port_word @ port_cycle.conj().T
    reversed_port_word = port_swaps[0] @ port_swaps[1] @ port_swaps[2]
    port_frame_residual = float(np.linalg.norm(rotated_port_word - port_word, 2))
    port_order_residual = float(np.linalg.norm(reversed_port_word - port_word, 2))
    check(
        "a tested shared-cell axis order exposes a preferred substep frame, whereas the disjoint-port product is cyclic-axis-rotation- and reversal-independent",
        axis_frame_residual > 1
        and axis_order_residual > 1
        and port_frame_residual < TOLERANCE
        and port_order_residual < TOLERANCE,
        {
            "shared_cell_axis_word_frame_residual": axis_frame_residual,
            "shared_cell_axis_word_order_residual": axis_order_residual,
            "disjoint_port_word_frame_residual": port_frame_residual,
            "disjoint_port_word_order_residual": port_order_residual,
            "scope": "failure of this supplied three-axis word only; alternate colorings remain open",
            "time_boundary": "compiler color phases are substeps, not physical time",
        },
    )


def collision_deletion_and_lawful_domain_controls(
    code: c269.WilsonSubsystemCode,
) -> None:
    print("\nCOLLISION DELETION / LAWFUL DOMAIN")
    body = (0, 0, 0)
    first = code.graph.vertex_index[(body, 0)]
    second = code.graph.vertex_index[(body, 2)]
    old_left = old.multi_catch_up(code, (first, second), body)
    old_right = old.multi_catch_up(code, (second, first), body)

    valid = (1 << first) | (1 << second)
    validate_port_domain(code, valid, valid)
    rejected = 0
    bad_fixtures = (
        (1 << first, 1 << first),
        (valid, 1 << first),
        (valid, -1),
        (valid, 1 << len(code.graph.vertices)),
    )
    for occupations, tags in bad_fixtures:
        try:
            validate_port_domain(code, occupations, tags)
        except ValueError:
            rejected += 1
    undersized = False
    try:
        c269.build_code(2)
    except ValueError:
        undersized = True
    check(
        "collapsing the six ports back to one cell tag reproduces the old decoded collision, while odd, mismatched, out-of-range, and undersized fixtures are rejected",
        old_left != old_right
        and rejected == len(bad_fixtures)
        and undersized,
        {
            "single_cell_tag_order_outputs": (old_left, old_right),
            "rejected_port_fixtures": rejected,
            "L2_rejected": undersized,
            "meaning": "the six-port resource is load-bearing for this construction",
        },
    )


def scope_and_inventory_controls() -> None:
    print("\nSCOPE / SUPPLIED STRUCTURE / OPEN ROUTES")
    check(
        "the result is a collision-safe bounded catch-up word on a declared auxiliary port-code space, not a bounded state or full-Fock compiler",
        True,
        {
            "derived": (
                "six port auxiliaries per cell",
                "weight-eight B_u B_v XOR control",
                "ten-M2 conditional port swap",
                "commuting order-free outer-edge product",
                "multiparticle decoded action and inverse through held L=6",
                "local-check/Wilson preservation, independent local port-constraint rank, and all-frame/all-translation covariance",
            ),
            "supplied": (
                "Cycle-269 B/A dictionary and outer FSWAP",
                "local constraints B_v Z_port(v)=+1",
                "prepared total-even port-code input",
                "six auxiliary port M2 per coarse cell",
                "stream then catch-up macrostep convention",
            ),
            "open": (
                "bounded physical state encoder into the port-code space",
                "local joint matter-coin/port-routing update",
                "full-Fock compiled macrostep",
                "whether a smaller frame-covariant auxiliary or color schedule closes",
                "same-code contact seam",
            ),
            "not_physical_time": "the commuting gate enumeration and any compiler colors are substep schedule only",
            "decoded_constraint_preservation_only": True,
            "assembled_encoded_stream_catchup_operator": False,
            "authority": "none",
            "audit": "unset",
            "no_go": False,
            "axiom_pressure": False,
        },
    )


def main() -> int:
    print("PHYSICAL CYCLE-269 COLLISION-SAFE AUXILIARY PORTS")
    print("authority=none; audit=unset")
    note_contract()
    local_ten_m2_matrix_controls()
    local_constraint_and_deletion_controls()
    cache = mapped_support_commutation_controls()
    multiparticle_held_size_controls(cache)
    covariance_and_translation_controls(cache[3])
    color_phase_and_preferred_frame_audit()
    collision_deletion_and_lawful_domain_controls(cache[3])
    scope_and_inventory_controls()
    print(f"\nSUMMARY: {PASS} passed, {FAIL} failed")
    return int(FAIL != 0)


if __name__ == "__main__":
    raise SystemExit(main())
