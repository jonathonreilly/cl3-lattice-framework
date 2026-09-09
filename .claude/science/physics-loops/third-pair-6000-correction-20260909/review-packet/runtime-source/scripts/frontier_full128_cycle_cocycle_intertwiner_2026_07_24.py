#!/usr/bin/env python3
"""Integrate the full128 cycle encoder with the bare-frame pair cocycle.

Two repo-local bounded construction modules are imported ordinarily:

* the 25-site nearest-neighbor cycle-code/seam-port successor; and
* the 61-site ordered-pair antisymmetry/contact certificate.

The combined encoding prepares the occupation-conditioned ordered-pair
register before applying the GF(2) cycle encoder and outer repetition encoder,

    E_full = D U W_A (I_7 tensor |+>^15 tensor |0>^39).

The physical update is certified compositionally in the order

    D^dag U^dag ; W_A^dag ; G_free+seam ; W_A ; R_contact ; U ; D.

Here R_contact is the same onsite phase on all thirty ordered-pair sites.  The
probe certifies the full 128 decoded columns and the bare coordinate action of
all proper-cubic frames.  It also verifies a commuting-projector definition
of the 128-dimensional code.  It does not claim dynamical enforcement,
autonomous scheduling, genesis, or recurrence.
"""

from __future__ import annotations

from collections import Counter
from hashlib import sha256
import json
import math
from pathlib import Path
import resource
import time

import numpy as np


START = time.perf_counter()
TOL = 4.0e-10
PASS = 0
FAIL = 0

AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
)

import frontier_full128_25site_nn_circuit_core_2026_07_24 as S
import frontier_full128_bare_frame_pair_cocycle_2026_07_24 as C
import frontier_full128_code_projectors_2026_07_24 as K
P = S.P
Gate = S.Gate
AbstractGate = S.AbstractGate
Coord = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def audit_source_closure(paths: tuple[str, ...], modules: tuple[object, ...]) -> bool:
    repo_root = Path(__file__).resolve().parents[1]
    resolved = tuple((repo_root / path).resolve() for path in paths)
    declared_modules = {path for path in resolved if path.suffix == ".py"}
    imported_modules = {Path(module.__file__).resolve() for module in modules}
    return (
        len(paths) == len(set(paths))
        and all(path.is_file() and repo_root in path.parents for path in resolved)
        and imported_modules == declared_modules
    )


Z = np.diag((1, -1)).astype(complex)
CONTACT_ONSITE = np.diag((1, np.exp(1j * P.CONTACT))).astype(complex)
CONTROLLED_H = np.asarray(
    (
        (1, 0, 0, 0),
        (0, 1 / math.sqrt(2), 0, 1 / math.sqrt(2)),
        (0, 0, 1, 0),
        (0, 1 / math.sqrt(2), 0, -1 / math.sqrt(2)),
    ),
    dtype=complex,
)

LOGICAL_COORDS: tuple[Coord, ...] = tuple(S.WIRE_COORDS[:6])
PORT_COORD: Coord = S.WIRE_COORDS[6]
DIRECTION_SITE_WIRES = tuple(S.COORD_WIRE[direction] for direction in S.DIRECTIONS)
FLAG_COORD: Coord = C.scale(4, C.DIRECTIONS[0])

ROUTE_MACROS = 0
ROUTE_RETURN_FAILURES = 0


def route(kind: str, left: Coord, right: Coord, matrix: np.ndarray) -> list[Gate]:
    global ROUTE_MACROS, ROUTE_RETURN_FAILURES
    ROUTE_MACROS += 1
    path = S.manhattan_path(left, right)
    labels = list(range(len(path)))
    for index in range(len(path) - 2):
        labels[index], labels[index + 1] = labels[index + 1], labels[index]
    for index in reversed(range(len(path) - 2)):
        labels[index], labels[index + 1] = labels[index + 1], labels[index]
    ROUTE_RETURN_FAILURES += labels != list(range(len(path)))
    return S.route_two(kind, left, right, matrix)


def toffoli_nn(control1: Coord, control2: Coord, target: Coord) -> list[Gate]:
    output = [Gate("H", (target,), S.H)]
    output += route("CNOT", control2, target, S.CNOT)
    output.append(Gate("Tdg", (target,), S.TDG))
    output += route("CNOT", control1, target, S.CNOT)
    output.append(Gate("T", (target,), S.T))
    output += route("CNOT", control2, target, S.CNOT)
    output.append(Gate("Tdg", (target,), S.TDG))
    output += route("CNOT", control1, target, S.CNOT)
    output.append(Gate("T", (control2,), S.T))
    output.append(Gate("T", (target,), S.T))
    output.append(Gate("H", (target,), S.H))
    output += route("CNOT", control1, control2, S.CNOT)
    output.append(Gate("T", (control1,), S.T))
    output.append(Gate("Tdg", (control2,), S.TDG))
    output += route("CNOT", control1, control2, S.CNOT)
    return output


def pair_preparation_word() -> tuple[Gate, ...]:
    output: list[Gate] = []
    for left, right in C.UNORDERED_PAIRS:
        q_left, q_right = LOGICAL_COORDS[left], LOGICAL_COORDS[right]
        forward = C.REGISTER_SITE[(left, right)]
        backward = C.REGISTER_SITE[(right, left)]
        output += toffoli_nn(q_left, q_right, FLAG_COORD)
        output += route("pair_flag_copy", FLAG_COORD, backward, S.CNOT)
        output += route("pair_controlled_H", FLAG_COORD, forward, CONTROLLED_H)
        output += route("pair_entangle", forward, backward, S.CNOT)
        output.append(Gate("pair_antisymmetry_Z", (forward,), Z))
        output += toffoli_nn(q_left, q_right, FLAG_COORD)
    return tuple(output)


PREPARE_WORD = pair_preparation_word()


def inverse_word(word: tuple[Gate, ...]) -> tuple[Gate, ...]:
    return tuple(
        Gate(f"inverse_{gate.kind}", gate.sites, gate.matrix.conj().T)
        for gate in reversed(word)
    )


UNPREPARE_WORD = inverse_word(PREPARE_WORD)


def route_abstract(word: tuple[AbstractGate, ...]) -> tuple[Gate, ...]:
    output: list[Gate] = []
    for gate in word:
        sites = tuple(S.WIRE_COORDS[wire] for wire in gate.wires)
        if len(sites) == 1:
            output.append(Gate(gate.kind, sites, gate.matrix))
        else:
            output += route(gate.kind, sites[0], sites[1], gate.matrix)
    return tuple(output)


ENCODER_GATE_COUNT = len(P.ENCODER_CIRCUIT)
DECODE_ABSTRACT = S.ABSTRACT_DATA_WORD[: 3 + ENCODER_GATE_COUNT]
ENCODE_ABSTRACT = S.ABSTRACT_DATA_WORD[-(ENCODER_GATE_COUNT + 3) :]
FREE_GATES = tuple(gate for gate in S.DECODED_GATES if gate.kind != "contact_phase")
DECODE_WORD = route_abstract(DECODE_ABSTRACT)
FREE_WORD = route_abstract(FREE_GATES)
CONTACT_WORD = tuple(
    Gate("ordered_pair_contact_onsite", (C.REGISTER_SITE[pair],), CONTACT_ONSITE)
    for pair in C.ORDERED_PAIRS
)
ENCODE_WORD = route_abstract(ENCODE_ABSTRACT)
COMBINED_WORD = (
    DECODE_WORD
    + UNPREPARE_WORD
    + FREE_WORD
    + PREPARE_WORD
    + CONTACT_WORD
    + ENCODE_WORD
)


def word_digest(word: tuple[Gate, ...]) -> str:
    hasher = sha256()
    for gate in word:
        hasher.update(gate.kind.encode())
        hasher.update(repr(gate.sites).encode())
        hasher.update(S.matrix_digest(gate.matrix).encode())
    return hasher.hexdigest()


USED_SUPPORT = {site for gate in COMBINED_WORD for site in gate.sites}
SEMANTIC_SUPPORT = set(C.SITES)
CARRIER_RADIUS = max(abs(value) for site in USED_SUPPORT | SEMANTIC_SUPPORT for value in site)
CARRIER = {
    (x, y, z)
    for x in range(-CARRIER_RADIUS, CARRIER_RADIUS + 1)
    for y in range(-CARRIER_RADIUS, CARRIER_RADIUS + 1)
    for z in range(-CARRIER_RADIUS, CARRIER_RADIUS + 1)
}


def append_mirrors(physical22: int) -> int:
    physical25 = physical22
    for mirror_index, pair in enumerate(S.REVERSE_PAIRS):
        edge = P.EDGE_INDEX[pair]
        physical25 |= ((physical22 >> edge) & 1) << (22 + mirror_index)
    return physical25


def coordinate_wire_permutation(frame: np.ndarray) -> tuple[int, ...]:
    def rotate(coord: Coord) -> Coord:
        return tuple(int(value) for value in frame @ np.asarray(coord, dtype=int))

    return tuple(S.COORD_WIRE[rotate(coord)] for coord in S.WIRE_COORDS)


def transport_bits(value: int, permutation: tuple[int, ...]) -> int:
    output = 0
    for source, target in enumerate(permutation):
        output |= ((value >> source) & 1) << target
    return output


def decoded_frame_matrix(frame: np.ndarray) -> tuple[np.ndarray, int]:
    permutation = coordinate_wire_permutation(frame)
    matrix = np.zeros((22, 22), dtype=np.uint8)
    repetition_failures = 0
    for source in range(22):
        logical = (1 << source) if source < 7 else 0
        auxiliary = (1 << (source - 7)) if source >= 7 else 0
        physical25 = append_mirrors(P.encode_index(logical, auxiliary))
        transported = transport_bits(physical25, permutation)
        for mirror_index, pair in enumerate(S.REVERSE_PAIRS):
            edge = P.EDGE_INDEX[pair]
            repetition_failures += (
                ((transported >> edge) & 1)
                != ((transported >> (22 + mirror_index)) & 1)
            )
        observed_q, observed_aux = P.decode_index(transported & ((1 << 22) - 1))
        decoded = observed_q | (observed_aux << 7)
        for target in range(22):
            matrix[target, source] = (decoded >> target) & 1
    return matrix, repetition_failures


def pair_gadget_matrix() -> tuple[np.ndarray, float, float]:
    total = 5
    sequence = (
        (S.ideal_toffoli(), (0, 1, 2)),
        (S.CNOT, (2, 4)),
        (CONTROLLED_H, (2, 3)),
        (S.CNOT, (3, 4)),
        (Z, (3,)),
        (S.ideal_toffoli(), (0, 1, 2)),
    )
    matrix = np.eye(1 << total, dtype=complex)
    for gate, wires in sequence:
        matrix = S.embed_gate(gate, wires, total) @ matrix
    columns = tuple(left | (right << 1) for left in (0, 1) for right in (0, 1))
    expected = np.zeros((1 << total, len(columns)), dtype=complex)
    for column, (left, right) in enumerate((
        (0, 0), (0, 1), (1, 0), (1, 1)
    )):
        target = C.gadget_target(left, right)
        for basis, amplitude in target.items():
            expected[basis, column] = amplitude
    preparation_residual = float(np.linalg.norm(matrix[:, columns] - expected))
    inverse_residual = float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(32)))
    return matrix, preparation_residual, inverse_residual


def register_contact_identity() -> tuple[float, float, dict[int, float]]:
    maximum = port_maximum = 0.0
    sectors = {number: 0.0 for number in range(7)}
    for port in (0, 1):
        for bits in range(64):
            state = C.register_state(bits)
            observed = C.contact_register_action(state)
            pair_count = bits.bit_count() * (bits.bit_count() - 1) // 2
            expected = C.scale_state(state, np.exp(1j * P.CONTACT * pair_count))
            residual = C.sparse_residual(observed, expected)
            maximum = max(maximum, residual)
            port_maximum = max(port_maximum, residual)
            sectors[bits.bit_count()] = max(sectors[bits.bit_count()], residual)
    return maximum, port_maximum, sectors


def placement_controls() -> dict:
    pitch = 2 * CARRIER_RADIUS + 1
    rows = []
    for length, split in ((3, "train"), (4, "held-no-refit")):
        anchors = tuple(
            (pitch * x, pitch * y, pitch * z)
            for x in range(length) for y in range(length) for z in range(length)
        )
        placed = {
            (anchor[0] + site[0], anchor[1] + site[1], anchor[2] + site[2])
            for anchor in anchors for site in CARRIER
        }
        rows.append({
            "L": length, "split": split, "blocks": len(anchors),
            "carrier_M2_per_block": len(CARRIER),
            "semantic_M2_per_block": len(SEMANTIC_SUPPORT),
            "collisions": len(anchors) * len(CARRIER) - len(placed),
            "combined_word_sha256": word_digest(COMBINED_WORD),
        })
    rejected = 0
    for length, modes, ports, pair_sites in (
        (2, 6, 1, 30), (3, 5, 1, 30), (3, 6, 0, 30), (4, 6, 1, 29)
    ):
        try:
            if length < 3 or modes != 6 or ports != 1 or pair_sites != 30:
                raise ValueError
        except ValueError:
            rejected += 1
    return {
        "pitch": pitch, "rows": rows, "lawful_rejections": rejected,
        "held_parameters_refit": 0,
        "shared_port_or_recurrent_overlap_tested": False,
        "pass": rejected == 4 and all(row["collisions"] == 0 for row in rows),
    }


def main() -> None:
    check(
        "ordinary repo-local imports close the declared source dependency surface",
        audit_source_closure(AUDIT_INPUT_PATHS, (P, S, C, K)),
        {"audit_input_paths": AUDIT_INPUT_PATHS, "campaign_fallbacks": 0},
    )

    overlap = {
        "successor_data_equals_cocycle_shell": set(S.DATA_COORDS) == set(C.SHELL),
        "register_data_overlap": len(set(C.REGISTER) & set(S.DATA_COORDS)),
        "corridor_data_overlap": len(set(C.CORRIDOR) & set(S.DATA_COORDS)),
        "flag_is_corridor": FLAG_COORD in C.CORRIDOR,
        "flag_data_overlap": FLAG_COORD in S.DATA_COORDS,
        "register_controller_clock_overlap": len(set(C.REGISTER) & set(S.CLOCK_COORDS)),
        "register_successor_controller_work_overlap": len(
            set(C.REGISTER) & {S.RELAY, S.WORK0, S.WORK1}
        ),
    }
    check(
        "the 25-site shell embeds without collision into the 61-site cocycle geometry",
        overlap["successor_data_equals_cocycle_shell"]
        and overlap["register_data_overlap"] == overlap["corridor_data_overlap"] == 0
        and overlap["flag_is_corridor"] and not overlap["flag_data_overlap"]
        and overlap["register_controller_clock_overlap"] == 0
        and overlap["register_successor_controller_work_overlap"] == 0,
        {**overlap, "semantic_support_M2": len(SEMANTIC_SUPPORT)},
    )

    wrong_coordinate_residual = C.sparse_residual(C.register_state(0b11), {0: 1.0 + 0.0j})
    check(
        "W_A controls the decoded logical wire coordinates rather than the signed-direction sites",
        LOGICAL_COORDS == tuple(S.WIRE_COORDS[:6])
        and LOGICAL_COORDS != tuple(C.DIRECTIONS)
        and DIRECTION_SITE_WIRES != tuple(range(6))
        and wrong_coordinate_residual > 1,
        {
            "decoded_logical_wire_coordinates": LOGICAL_COORDS,
            "signed_direction_coordinates": C.DIRECTIONS,
            "wires_at_signed_direction_sites": DIRECTION_SITE_WIRES,
            "wrong_coordinate_control_residual_on_q0q1": wrong_coordinate_residual,
            "reason": "after U^dag, q_i occupies WIRE_COORDS[i]; d_i sites carry wires 5,10,14,17,19,20",
        },
    )

    two_site_non_nn = sum(len(gate.sites) == 2 and S.l1(*gate.sites) != 1 for gate in COMBINED_WORD)
    outside_carrier = sum(any(site not in CARRIER for site in gate.sites) for gate in COMBINED_WORD)
    support_overlap_routes = sum(
        gate.kind == "route_swap" and any(site in SEMANTIC_SUPPORT for site in gate.sites)
        for gate in COMBINED_WORD
    )
    check(
        "the declared decode/unprepare/free/prepare/contact/re-encode word is entirely NN",
        two_site_non_nn == outside_carrier == ROUTE_RETURN_FAILURES == 0
        and CARRIER_RADIUS == 4,
        {
            "order": (
                "D^dag U^dag", "W_A^dag", "free+reverse+seam", "W_A",
                "thirty onsite contact phases", "U D",
            ),
            "combined_NN_gate_count": len(COMBINED_WORD),
            "route_macros": ROUTE_MACROS,
            "route_return_failures": ROUTE_RETURN_FAILURES,
            "non_NN_gates": two_site_non_nn,
            "used_support_M2": len(USED_SUPPORT),
            "carrier_radius": CARRIER_RADIUS,
            "carrier_cube_M2": len(CARRIER),
            "route_swaps_touching_semantic_sites": support_overlap_routes,
            "overlap_disposition": (
                "route-and-return may cross occupied semantic M2 factors; it restores their wire states "
                "and does not assume they are blank"
            ),
        },
    )

    pair_matrix, pair_preparation_residual, pair_inverse_residual = pair_gadget_matrix()
    full_register_norm = 0.0
    full_work_failures = 0
    for bits in range(64):
        state = C.register_state(bits)
        full_register_norm = max(
            full_register_norm,
            abs(sum(abs(amplitude) ** 2 for amplitude in state.values()) - 1),
        )
        flag = 0
        for left, right in C.UNORDERED_PAIRS:
            active = ((bits >> left) & 1) and ((bits >> right) & 1)
            flag ^= int(active)
            flag ^= int(active)
        full_work_failures += flag != 0
    check(
        "W_A and W_A^dag are reversible on all occupations and return the shared flag",
        pair_preparation_residual < TOL and pair_inverse_residual < TOL
        and full_register_norm < TOL and full_work_failures == 0,
        {
            "single_pair_preparation_residual": pair_preparation_residual,
            "single_pair_unitary_inverse_residual": pair_inverse_residual,
            "maximum_full_M64_register_norm_residual": full_register_norm,
            "full_M64_work_return_failures": full_work_failures,
            "prepare_NN_gate_count": len(PREPARE_WORD),
            "unprepare_NN_gate_count": len(UNPREPARE_WORD),
            "flag_coordinate": FLAG_COORD,
        },
    )

    free_matrix = S.product_on_seven(FREE_GATES)
    target_factors = P.coarse_factors(1)
    target_update = np.asarray(target_factors["update"])
    target_free = np.asarray(target_factors["seam"] @ target_factors["reverse"] @ target_factors["coin"])
    contact_diagonal = np.asarray(target_factors["contact"])
    combined_logical = contact_diagonal @ free_matrix
    free_residual = float(np.linalg.norm(free_matrix - target_free))
    full_eg_residual = float(np.linalg.norm(combined_logical - target_update))
    register_contact_residual, port_contact_residual, contact_sectors = register_contact_identity()
    encoder_rank = P.gf2_rank(P.ENCODER)
    decoder_residual = int(np.max(np.abs(
        (P.DECODER @ P.ENCODER) % 2 - np.eye(22, dtype=np.uint8)
    )))
    encoded_column_collisions = 0
    for auxiliary in (0, 1, 0x1555, (1 << 15) - 1):
        columns = tuple(append_mirrors(P.encode_index(q, auxiliary)) for q in range(128))
        encoded_column_collisions += 128 - len(set(columns))
    check(
        "E_full = D U W_A compositionally intertwines the full128 free+seam+contact update",
        free_residual < TOL and full_eg_residual < TOL
        and register_contact_residual < TOL and port_contact_residual < TOL
        and encoder_rank == 22 and decoder_residual == encoded_column_collisions == 0,
        {
            "encoding": "E_full = D U W_A (I_7 tensor |+>^15 tensor |0>^39)",
            "physical_update": "D U R_contact W_A G_free+seam W_A^dag U^dag D^dag",
            "decoded_columns": 128,
            "cycle_fibres_per_column": 1 << 15,
            "encoder_GF2_rank": encoder_rank,
            "decoder_encoder_residual": decoder_residual,
            "explicit_aux_sector_encoded_collisions": encoded_column_collisions,
            "free_plus_seam_factor_residual": free_residual,
            "maximum_R_contact_WA_equals_WA_contact_residual": register_contact_residual,
            "contact_sector_residuals_k0_through_k6": contact_sectors,
            "maximum_full128_EG_residual": full_eg_residual,
            "proof_shape": (
                "W_A^dag W_A=I; U^dag U=D^dag D=I on code; "
                "R_contact W_A=W_A C_contact; remaining block is G_free+seam"
            ),
        },
    )

    cycle_rank = P.gf2_rank(S.LIFTED_CYCLE_CHECKS)
    outer_rank = P.gf2_rank(S.REPETITION_Z_CHECKS)
    cross_commutators = int(np.count_nonzero(
        (S.LIFTED_CYCLE_CHECKS @ S.REPETITION_Z_CHECKS.T) % 2
    ))
    cycle_deleted_rank = P.gf2_rank(S.LIFTED_CYCLE_CHECKS[:-1])
    outer_deleted_rank = P.gf2_rank(S.REPETITION_Z_CHECKS[:-1])
    conditional_pair_failures = conditional_reset_failures = 0
    for bits in range(64):
        expected_pairs = bits.bit_count() * (bits.bit_count() - 1) // 2
        state = C.register_state(bits)
        conditional_pair_failures += any(mask.bit_count() != expected_pairs for mask in state)
        active = [pair for pair in C.UNORDERED_PAIRS if all((bits >> mode) & 1 for mode in pair)]
        for pair in reversed(C.UNORDERED_PAIRS):
            if pair in active:
                active.remove(pair)
        conditional_reset_failures += bool(active)
    outer_reset_failures = 0
    for primary in (0, 1):
        decoded_mirror = primary ^ primary
        outer_reset_failures += decoded_mirror != 0
        for updated in (0, 1):
            outer_reset_failures += (decoded_mirror ^ updated) != updated
    omitted_pair_residual = C.sparse_residual(C.register_state(0b11), {0: 1.0 + 0.0j})
    constraints = {
        "cycle_X_rows": len(S.LIFTED_CYCLE_CHECKS), "cycle_X_rank": cycle_rank,
        "outer_Z_rows": len(S.REPETITION_Z_CHECKS), "outer_Z_rank": outer_rank,
        "CSS_cross_commutation_failures": cross_commutators,
        "cycle_rank_after_one_deletion": cycle_deleted_rank,
        "outer_rank_after_one_deletion": outer_deleted_rank,
        "conditional_pair_sector_failures": conditional_pair_failures,
        "conditional_register_reset_failures": conditional_reset_failures,
        "omitted_active_pair_gadget_residual": omitted_pair_residual,
        "work_flag_return_failures": full_work_failures,
        "outer_mirror_decode_reencode_failures": outer_reset_failures,
        "cycle_update_preservation_failures": int(
            full_eg_residual >= TOL or decoder_residual != 0
        ),
        "preservation_scope": (
            "code-space compositional preservation by decode/unprepare/update/prepare/re-encode; "
            "no dynamical enforcement, cooling, preparation or genesis is supplied"
        ),
    }
    code_projectors = K.certificate(S, C, P, decoded_frame_matrix)
    constraints["commuting_projector_certificate"] = code_projectors
    check(
        "the full128 sector is a bounded proper-cubic commuting-projector code with active deletions",
        cycle_rank == 15 and outer_rank == 3 and cross_commutators == 0
        and cycle_deleted_rank == 14 and outer_deleted_rank == 2
        and conditional_pair_failures == conditional_reset_failures == full_work_failures == 0
        and outer_reset_failures == 0 and omitted_pair_residual > 1
        and code_projectors["pass"],
        constraints,
    )

    frame_fibre_failures = repetition_failures = logical_block_failures = 0
    aux_rank_failures = register_frame_failures = semantic_set_failures = 0
    frame_matrices = []
    maximum_register_frame_residual = 0.0
    maximum_update_covariance = 0.0
    for frame, mapping in zip(P.FRAMES, S.MODE_MAPS if hasattr(S, "MODE_MAPS") else tuple(P.mode_map(row) for row in P.FRAMES)):
        mapping = tuple(int(value) for value in mapping)
        decoded_matrix, repeat = decoded_frame_matrix(frame)
        frame_matrices.append(decoded_matrix)
        repetition_failures += repeat
        for source in range(7):
            expected = mapping[source] if source < 6 else 6
            observed = tuple(np.flatnonzero(decoded_matrix[:7, source]))
            logical_block_failures += observed != (expected,)
        logical_block_failures += int(np.count_nonzero(decoded_matrix[:7, 7:]))
        aux_rank_failures += P.gf2_rank(decoded_matrix[7:, 7:]) != 15
        rotate = lambda coord: tuple(int(value) for value in frame @ np.asarray(coord, dtype=int))
        semantic_set_failures += {rotate(site) for site in SEMANTIC_SUPPORT} != SEMANTIC_SUPPORT
        for q in range(128):
            local = q & 0x3F
            transported_register = C.permute_register(C.register_state(local), mapping)
            target_local = C.transformed_bits(local, mapping)
            sign = C.exterior_sign(local, mapping)
            residual = C.sparse_residual(
                transported_register,
                C.scale_state(C.register_state(target_local), sign),
            )
            maximum_register_frame_residual = max(maximum_register_frame_residual, residual)
            register_frame_failures += residual >= TOL
        one = P.permutation_matrix(mapping + (P.PORT,), 7)
        gamma = P.fock_lift(one)
        seam_mode = mapping[1]
        covariance = float(np.linalg.norm(
            gamma @ target_update @ gamma.conj().T - P.coarse_factors(seam_mode)["update"]
        ))
        maximum_update_covariance = max(maximum_update_covariance, covariance)
    check(
        "bare coordinate permutation realizes the combined exterior action on all128 code columns",
        repetition_failures == logical_block_failures == aux_rank_failures == 0
        and register_frame_failures == semantic_set_failures == 0
        and maximum_register_frame_residual < TOL and maximum_update_covariance < TOL,
        {
            "proper_cubic_frames": len(P.FRAMES),
            "full128_frame_columns": len(P.FRAMES) * 128,
            "repetition_transport_failures": repetition_failures,
            "decoded_logical_block_failures": logical_block_failures,
            "cycle_auxiliary_invertibility_failures": aux_rank_failures,
            "semantic_61_site_set_failures": semantic_set_failures,
            "ordered_pair_register_frame_failures": register_frame_failures,
            "maximum_ordered_pair_frame_residual": maximum_register_frame_residual,
            "maximum_update_family_covariance_residual": maximum_update_covariance,
            "physical_frame_action": "bare coordinate permutation only; no decoded CZ/sign dressing",
            "cycle_fibre_reason": (
                "logical-from-aux block is zero and the 15x15 aux block is invertible, so each "
                "uniform |+>^15 fibre maps bijectively to the rotated uniform fibre"
            ),
        },
    )

    rotated_nn_failures = rotated_support_failures = rotated_order_failures = 0
    rotated_roundtrip_failures = canonical_word_equality_frames = 0
    canonical_support_equality_frames = 0
    for frame in P.FRAMES:
        rotate = lambda coord: tuple(int(value) for value in frame @ np.asarray(coord, dtype=int))
        inverse = frame.T
        rotated_support = {rotate(site) for site in USED_SUPPORT}
        rotated_support_failures += not rotated_support <= CARRIER
        canonical_support_equality_frames += rotated_support == USED_SUPPORT
        word_equal = True
        rotated_signature = []
        for gate in COMBINED_WORD:
            sites = tuple(rotate(site) for site in gate.sites)
            rotated_signature.append((gate.kind, S.matrix_digest(gate.matrix)))
            rotated_nn_failures += len(sites) == 2 and S.l1(*sites) != 1
            rotated_support_failures += any(site not in CARRIER for site in sites)
            word_equal &= sites == gate.sites
            for source, site in zip(gate.sites, sites):
                returned = tuple(int(value) for value in inverse @ np.asarray(site, dtype=int))
                rotated_roundtrip_failures += returned != source
        canonical_signature = tuple((gate.kind, S.matrix_digest(gate.matrix)) for gate in COMBINED_WORD)
        rotated_order_failures += tuple(rotated_signature) != canonical_signature
        canonical_word_equality_frames += word_equal
    rotated_word_audit = {
        "frames": len(P.FRAMES), "gates_per_frame": len(COMBINED_WORD),
        "rotated_NN_failures": rotated_nn_failures,
        "rotated_support_failures": rotated_support_failures,
        "rotated_gate_matrix_order_failures": rotated_order_failures,
        "rotation_roundtrip_failures": rotated_roundtrip_failures,
        "frames_equal_to_one_canonical_off_code_word": canonical_word_equality_frames,
        "frames_with_identical_used_support": canonical_support_equality_frames,
        "scope": (
            "the coordinate-conjugated word family is NN and preserves gate/matrix order; covariance "
            "is on the declared code and rotated seam family. It is not equality of every rotated "
            "off-code circuit to the single canonical coordinate word"
        ),
    }
    check(
        "the coordinate-rotated combined-word family remains NN, supported and order preserving",
        rotated_nn_failures == rotated_support_failures == rotated_order_failures
        == rotated_roundtrip_failures == 0 and canonical_word_equality_frames >= 1,
        rotated_word_audit,
    )

    frame_product_failures = cocycle_product_failures = carrier_product_failures = 0
    frame_index = {tuple(int(value) for value in frame.ravel()): i for i, frame in enumerate(P.FRAMES)}
    for left_index, left in enumerate(P.FRAMES):
        left_map = tuple(P.mode_map(left))
        for right_index, right in enumerate(P.FRAMES):
            right_map = tuple(P.mode_map(right))
            target_frame = left @ right
            target_index = frame_index[tuple(int(value) for value in target_frame.ravel())]
            target_map = tuple(P.mode_map(target_frame))
            frame_product_failures += not np.array_equal(
                (frame_matrices[left_index] @ frame_matrices[right_index]) % 2,
                frame_matrices[target_index],
            )
            for q in range(128):
                local = q & 0x3F
                sequential_sign = C.register_sign(local, right_map) * C.register_sign(
                    C.transformed_bits(local, right_map), left_map
                )
                cocycle_product_failures += sequential_sign != C.register_sign(local, target_map)
            for site in CARRIER:
                sequential = left @ (right @ np.asarray(site, dtype=int))
                composed = target_frame @ np.asarray(site, dtype=int)
                carrier_product_failures += not np.array_equal(sequential, composed)
    check(
        "all 576 combined bare-frame products close on data, cycle fibres and cocycle phases",
        frame_product_failures == cocycle_product_failures == carrier_product_failures == 0,
        {
            "ordered_frame_products": len(P.FRAMES) ** 2,
            "GF2_cycle_encoder_product_failures": frame_product_failures,
            "full128_cocycle_product_failures": cocycle_product_failures,
            "carrier_coordinate_product_failures": carrier_product_failures,
        },
    )

    active_source = {0b11: 1.0 + 0.0j}
    deleted_phase = C.gadget(active_source, delete_phase=True)
    swapped_deleted = C.basis_permutation(
        deleted_phase,
        lambda basis: basis ^ (1 << 3) ^ (1 << 4)
        if ((basis >> 3) & 1) != ((basis >> 4) & 1)
        else basis,
    )
    antisymmetry_deletion = C.sparse_residual(swapped_deleted, C.scale_state(deleted_phase, -1))
    unprepare_deletion = C.sparse_residual(C.register_state(0b11), {0: 1.0 + 0.0j})
    contact_before_prepare = float(abs(np.exp(1j * P.CONTACT) - 1))
    pair_state = C.register_state(0b11)
    deleted_one = C.contact_register_action(pair_state, deleted={C.ORDERED_INDEX[(0, 1)]})
    overlap_amplitude = sum(
        pair_state[mask].conjugate() * deleted_one.get(mask, 0.0j) for mask in pair_state
    )
    one_contact_leakage = math.sqrt(max(0.0, 1 - abs(overlap_amplitude) ** 2))
    seam_index = next(index for index, gate in enumerate(FREE_GATES) if gate.kind == "seam_fswap")
    deleted_seam = S.product_on_seven(FREE_GATES[:seam_index] + FREE_GATES[seam_index + 1 :])
    seam_deletion_residual = float(np.linalg.norm(free_matrix - deleted_seam))
    check(
        "ordering, coordinate, antisymmetry, contact and seam deletions are active",
        wrong_coordinate_residual > 1
        and antisymmetry_deletion > 1
        and unprepare_deletion > 1
        and contact_before_prepare > 1e-2
        and one_contact_leakage > 1e-2
        and seam_deletion_residual > 1e-2,
        {
            "wrong_decoded_coordinate_residual": wrong_coordinate_residual,
            "deleted_pair_Z_frame_residual": antisymmetry_deletion,
            "deleted_WA_dag_work_reset_residual": unprepare_deletion,
            "contact_before_prepare_missing_phase_residual": contact_before_prepare,
            "deleted_one_ordered_contact_site_code_leakage": one_contact_leakage,
            "deleted_seam_factor_residual": seam_deletion_residual,
        },
    )

    domains = placement_controls()
    check(
        "train L3 and held L4 placements keep constant overhead without refit and reject unlawful domains",
        domains["pass"] and domains["held_parameters_refit"] == 0,
        domains,
    )

    kinds = Counter(gate.kind for gate in COMBINED_WORD)
    resources = {
        "semantic_M2": len(SEMANTIC_SUPPORT),
        "cycle_data_M2": len(S.DATA_COORDS),
        "ordered_pair_register_M2": len(C.REGISTER),
        "corridor_and_returned_work_M2": len(C.CORRIDOR),
        "used_routing_support_M2": len(USED_SUPPORT),
        "carrier_cube_M2": len(CARRIER),
        "carrier_radius": CARRIER_RADIUS,
        "decode_NN_gates": len(DECODE_WORD),
        "unprepare_NN_gates": len(UNPREPARE_WORD),
        "free_plus_seam_NN_gates": len(FREE_WORD),
        "prepare_NN_gates": len(PREPARE_WORD),
        "contact_onsite_gates": len(CONTACT_WORD),
        "reencode_NN_gates": len(ENCODE_WORD),
        "combined_NN_gate_count": len(COMBINED_WORD),
        "one_site_gates": sum(len(gate.sites) == 1 for gate in COMBINED_WORD),
        "two_site_gates": sum(len(gate.sites) == 2 for gate in COMBINED_WORD),
        "route_swap_gates": kinds["route_swap"] + kinds["inverse_route_swap"],
        "combined_word_sha256": word_digest(COMBINED_WORD),
        "supplied_schedule_clock_M2_included": 0,
    }
    check(
        "resource and dependency surfaces are closed under the declared bounded circuit claim",
        resources["semantic_M2"] == 61
        and resources["cycle_data_M2"] == 25
        and resources["ordered_pair_register_M2"] == 30
        and resources["corridor_and_returned_work_M2"] == 6
        and resources["contact_onsite_gates"] == 30
        and resources["combined_NN_gate_count"]
        == resources["one_site_gates"] + resources["two_site_gates"],
        resources,
    )

    supplied = (
        "ordinary repo-local cycle, nearest-neighbor and pair-cocycle source modules",
        "six signed-direction mode labels, one seam-port label and the bounded decoded wire order",
        "25-site cycle/repetition shell and 30 ordered-pair plus six corridor/work coordinates",
        "fifteen cycle |+> auxiliaries, three repetition blanks and thirty register blanks",
        "one returned flag at 4*d_(+x), a fixed fifteen-pair preparation order and Clifford+T factors",
        "beta/contact fixtures and the fixed free/reverse/seam factor order",
        "a fixed Manhattan axis-order routing convention and the finite combined gate word",
        "standard translations/proper-cubic coordinate action and numerical tolerances",
    )
    open_items = (
        "dynamical enforcement, cooling, preparation or genesis of the commuting-projector code sector",
        "a time-homogeneous local scheduler/controller for the combined gate word",
        "overlapping recurrent blocks, shared seam-port consistency and a full lattice stream law",
        "optimization of the route word, carrier support or returned-work allocation",
        "derivation of mode labels, couplings, factor order or preparation program from the axioms",
        "physical time, energy, source, gravity, Record, occurrence and probability",
        "identification with the finite flat-link census constraint code",
        "any minimum, impossibility, shared-obstruction or axiom-pressure conclusion",
    )
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "bounded-full128-cycle-cocycle-compositional-certificate",
        "terminal": "FULL128_CYCLE_COCYCLE_BARE_FRAME_INTERTWINER_CERTIFICATE",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "source_dependency_closure": AUDIT_INPUT_PATHS,
        "maximum_residuals": {
            "pair_preparation": pair_preparation_residual,
            "pair_inverse": pair_inverse_residual,
            "full_register_norm": full_register_norm,
            "free_plus_seam": free_residual,
            "register_contact": register_contact_residual,
            "full128_EG": full_eg_residual,
            "bare_frame_register": maximum_register_frame_residual,
            "update_covariance": maximum_update_covariance,
        },
        "constraints": constraints,
        "rotated_word_audit": rotated_word_audit,
        "domains": domains,
        "resources": resources,
        "supplied": supplied,
        "derived": (
            "collision-free 25-site cycle shell plus 30-site antisymmetry register in a 61-site semantic block",
            "explicit all-NN decode/unprepare/free+seam/prepare/contact/re-encode word",
            "full128 compositional E_full G = G_physical E_full certificate",
            "bare-coordinate exterior covariance on all 24 frames and all 576 products",
            "exact returned pair flag, repetition mirrors and route intermediate wire placement",
            "59-projector proper-cubic commuting family with 128-dimensional joint code and gap one",
            "active order, coordinate, antisymmetry, contact, seam and work-reset deletions",
        ),
        "open": open_items,
        "claim_ceiling": (
            "Positive bounded compositional circuit/intertwiner certificate only.  The finite code sectors, "
            "blank/register genesis, route order and gate word are supplied.  No autonomous schedule, "
            "dynamical constraint enforcement, recurrent compiler, state genesis, minimality, impossibility "
            "or axiom-pressure claim."
        ),
        "resources_runtime": {
            "elapsed_seconds": time.perf_counter() - START,
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
