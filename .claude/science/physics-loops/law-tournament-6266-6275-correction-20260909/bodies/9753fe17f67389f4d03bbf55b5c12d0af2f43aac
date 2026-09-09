#!/usr/bin/env python3
"""Cycle707 abstract Cycle656 PacketTrace and projected resource census.

This helper instantiates the landed Cycle656 trace objects on the routed
Cycle707 word and computes the corresponding column-width resource formula.
It deliberately does not claim or construct a literal custom selector
blueprint for the enlarged lane/program dimensions.
"""

from __future__ import annotations

from hashlib import sha256
import math

import numpy as np

import frontier_full128_25site_nn_circuit_core_2026_07_24 as c655
import frontier_full128_two_rail_fixed_law_core_2026_07_24 as c656


Coord = tuple[int, int, int]


def cycle656_controller(
    word: tuple[c655.Gate, ...], touched: tuple[Coord, ...]
) -> dict[str, object]:
    """Run the abstract factor-index trace and report projected resources."""
    original = len(word)
    padded = original if original % 2 == 0 else original + 1
    lanes = len(touched)
    packet_lanes = lanes + 1
    opcode_count = len(
        {(len(gate.sites), c655.matrix_digest(gate.matrix)) for gate in word}
    )
    address_bits = math.ceil(math.log2(padded))
    opcode_bits = math.ceil(math.log2(opcode_count))
    lane_bits = math.ceil(math.log2(lanes))
    program_bits = 1 + address_bits + opcode_bits + 1 + 2 * lane_bits
    scratch = program_bits - 1
    a_column = packet_lanes + program_bits + 1 + scratch + 2
    b_column = packet_lanes
    footprint = padded * (a_column + b_column)
    side = padded // 2 + 1
    track = c656.square_track(side)
    rail_failures = int(len(track) != 2 * padded) + sum(
        c656.l1(track[index], track[(index + 1) % len(track)]) != 1
        for index in range(len(track))
    )
    lane_of = {site: lane for lane, site in enumerate(touched)}
    instructions = tuple(
        c656.Instruction(
            gate.kind, tuple(lane_of[site] for site in gate.sites), gate.matrix
        )
        for gate in word
    )
    if padded != original:
        instructions += (c656.Instruction("identity_padding", (0,), c655.I2),)
    keys = tuple(
        sorted(
            {
                (len(gate.lanes), c655.matrix_digest(gate.matrix))
                for gate in instructions
            }
        )
    )
    opcode = {key: index for index, key in enumerate(keys)}

    def program_word(
        index: int, gate: c656.Instruction
    ) -> tuple[int, ...]:
        fields = (
            (1, 1),
            (index, address_bits),
            (
                opcode[
                    (len(gate.lanes), c655.matrix_digest(gate.matrix))
                ],
                opcode_bits,
            ),
            (len(gate.lanes) - 1, 1),
            (gate.lanes[0], lane_bits),
            (gate.lanes[-1], lane_bits),
        )
        return tuple(
            (value >> bit) & 1
            for value, width in fields
            for bit in range(width)
        )

    programs = tuple(
        program_word(index, gate) for index, gate in enumerate(instructions)
    )
    selector = c656.SelectorLaw(
        tuple(
            c656.RomBlock(index, programs[index], instructions[index])
            for index in range(padded)
        )
    )
    shift = c656.RailShiftLaw(padded, packet_lanes, track)
    law = c656.AutoLaw(selector, shift, ("Q", "R"))

    def genesis(origin: int) -> c656.LawState:
        packets = [c656.VACUUM_PACKET for _ in range(padded)]
        packets[origin] = c656.PacketTrace(1, "E_full|psi>", origin)
        return c656.LawState(
            tuple(packets),
            tuple(c656.VACUUM_PACKET for _ in range(padded)),
            programs,
            tuple(c656.CLEAN_ANCILLA for _ in range(padded)),
        )

    final, orbit = c656.run_orbit(law, genesis(0), padded)
    final_packet = final.a_packets[0]
    selected = final_packet.factors
    wrong_final, _ = c656.run_orbit(law, genesis(1), padded)
    deleted_final, _ = c656.run_orbit(
        c656.AutoLaw(selector.without_block(17), shift, ("Q", "R")),
        genesis(0),
        padded,
    )
    deleted_factors = deleted_final.a_packets[0].factors
    selected_digest = sha256(
        "".join(
            (
                gate.kind
                + repr(gate.sites)
                + c655.matrix_digest(gate.matrix)
                if index < original
                else "identity-padding"
            )
            for index, gate in enumerate(
                word + (() if padded == original else (word[0],))
            )
        ).encode()
    ).hexdigest()
    station_zero_return = (
        final_packet.token == 1
        and final_packet.origin == 0
        and not any(packet.token for packet in final.a_packets[1:])
        and all(packet.is_vacuum for packet in final.b_packets)
    )
    controlled_one_residual = controlled_one_unitarity = 0.0
    bypass_action_residual = bypass_work_leakage = 0.0
    for arity, digest in sorted(
        {
            (len(gate.sites), c655.matrix_digest(gate.matrix))
            for gate in word
        }
    ):
        gate = next(
            row
            for row in word
            if len(row.sites) == arity
            and c655.matrix_digest(row.matrix) == digest
        )
        if arity == 1:
            controlled = c656.controlled_one(gate.matrix)
            expected = np.zeros((4, 4), dtype=complex)
            expected[np.ix_((0, 2), (0, 2))] = np.eye(2)
            expected[np.ix_((1, 3), (1, 3))] = gate.matrix
            controlled_one_residual = max(
                controlled_one_residual,
                float(np.linalg.norm(controlled - expected)),
            )
            controlled_one_unitarity = max(
                controlled_one_unitarity,
                float(
                    np.linalg.norm(
                        controlled.conj().T @ controlled - np.eye(4)
                    )
                ),
            )
        else:
            residual, leakage = c655.ideal_bypass(gate.matrix, 2)
            bypass_action_residual = max(
                bypass_action_residual, float(residual)
            )
            bypass_work_leakage = max(
                bypass_work_leakage, float(leakage)
            )
    return {
        "stations_A": padded,
        "stations_B": padded,
        "packet_data_lanes": lanes,
        "packet_live_token_lanes": 1,
        "program_bits_per_A": program_bits,
        "selector_flag_per_A": 1,
        "match_scratch_per_A": scratch,
        "bypass_work_per_A": 2,
        "projected_A_column_M2": a_column,
        "projected_B_column_M2": b_column,
        "projected_complete_footprint_M2": footprint,
        "rail_side": side,
        "rail_layer_edges_each": padded * packet_lanes,
        "rail_failures": rail_failures,
        "projected_maximum_A_column_route_distance": a_column - 1,
        "packet_trace_selected_events": orbit.selected_events,
        "selected_order_failures": int(selected != tuple(range(padded))),
        "live_count_failures": orbit.live_count_failures,
        "B_vacuum_failures": orbit.b_vacuum_failures,
        "program_change_failures": orbit.program_change_failures,
        "ancilla_change_failures": orbit.ancilla_change_failures,
        "station_zero_return": station_zero_return,
        "trace_sha256": orbit.trace_sha256,
        "selected_word_sha256": selected_digest,
        "wrong_origin_cyclic_history": (
            wrong_final.a_packets[1].factors
            == tuple(range(1, padded)) + (0,)
        ),
        "delete_ROM_17_missing": (
            17 not in deleted_factors and len(deleted_factors) == padded - 1
        ),
        "opcode_controlled_one_M2_residual": controlled_one_residual,
        "opcode_controlled_one_M2_unitarity_residual": controlled_one_unitarity,
        "opcode_two_M2_bypass_action_residual": bypass_action_residual,
        "opcode_two_M2_bypass_work_leakage": bypass_work_leakage,
        "literal_custom_selector_blueprint_executed": False,
        "packet_lane_order": (
            "supplied lexicographic order of touched Z3 coordinates"
        ),
        "selector_before_shift_order": "supplied Q then R",
        "station_zero_token_and_clean_work_genesis": "supplied",
    }
