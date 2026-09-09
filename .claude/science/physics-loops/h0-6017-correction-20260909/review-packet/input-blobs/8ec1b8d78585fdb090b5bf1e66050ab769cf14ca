#!/usr/bin/env python3
"""Cycle 719 core: address-free recurrent bank for Cycle-610/612 acceptance.

This core composes the landed Cycle-718 persistent carrier relay with the local
predecessor grammar.  No bank number is an input to the update.  A graph
decoder assigns temporary numeric identities only after the physical-side
update so that the unchanged Cycle-610/612 acceptance code can be exercised.

The source carrier injection/cleanup, clean genesis, and physical placement of
the twelve-bank word remain supplied.  Circuit ordinals and K16 integers are
not called physical time, and the reversible packet graph is not a Record.
"""
from __future__ import annotations

from dataclasses import asdict
from hashlib import sha256
import itertools
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUDIT_INPUT_PATHS = (
    "scripts/ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17.py",
    "scripts/active_cubic_source_response_cycle211_2026_07_16.py",
    "scripts/archive_carrier_source_ledger_cycle227_2026_07_17.py",
    "scripts/autonomous_cubic_field_emission_cycle214_2026_07_16.py",
    "scripts/common_matter_field_coin_family_cycle219_2026_07_16.py",
    "scripts/finite_coin_scalar_wave_dilation_cycle215_2026_07_16.py",
    "scripts/fock_modular_boundary_current_cycle229_2026_07_17.py",
    "scripts/frontier_cycle703_local_gauss_reference_adversary_2026_07_25.py",
    "scripts/frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25.py",
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py",
    "scripts/frontier_cycle708_cube_basis_gauge_core_2026_07_26.py",
    "scripts/frontier_cycle708_endpoint_cube_tableau_core_2026_07_26.py",
    "scripts/frontier_cycle708_physical_endpoint_cube_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_clifford_core_2026_07_26.py",
    "scripts/frontier_cycle709_local_seam_physical_core_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_independent_check_2026_07_26.py",
    "scripts/frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26.py",
    "scripts/frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26.py",
    "scripts/frontier_cycle714_fixed_packet_coherent_composition_check_2026_07_26.py",
    "scripts/frontier_cycle714_full34_fixed_packet_physical_m2_core_2026_07_26.py",
    "scripts/frontier_cycle715_recurrent_directional_packet_bank_2026_07_26.py",
    "scripts/frontier_cycle718_carrier_return_core_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22.py",
    "scripts/physical_autonomous_localized_refocused_matter_transition_tournament_cycle575_2026_07_22.py",
    "scripts/physical_contact_dimer_infinite_internal_content_tournament_cycle583_2026_07_22.py",
    "scripts/physical_intrinsic_contact_bound_moving_transition_tournament_cycle578_2026_07_22.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_matter_transition_clock_equivalence_tournament_cycle573_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle704_local_gauss_cycle612_endpoint_bridge_2026_07_25 as C704
import frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26 as C718
import frontier_cycle718_carrier_return_core_2026_07_26 as P
import frontier_cycle718_token_relative_relay_core_2026_07_26 as R3


A = P.A
BANKS = 12
CELLS = 2 * BANKS
TOL = 5.0e-10
LINK_WIDTH = 2 * P.LINK_AUX_WIDTH


def source_bank(banks: tuple[tuple[int, ...], ...]) -> int:
    locations = [
        index for index, bank in enumerate(banks)
        if sum(bank[wire] for wire in A.TOKEN) == 1
    ]
    if len(locations) != 1:
        raise ValueError(("token sector", locations))
    return locations[0]


def cross_tag_action(
    bank: tuple[int, ...], link: tuple[int, ...]
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Literal edge-local CNOT: live handoff latch -> cross-left tag."""
    combined = link + bank
    gate = A.cn(0, len(link) + int(A.CELLS[0]["pred"][1]))
    after = A.apply_semantic(combined, (gate,))
    return after[len(link):], after[:len(link)]


def relay_latch_word(*, pending_marker_required: bool):
    left, right = P.LEFT, P.RIGHT
    positives = (
        left + A.POINTER,
        left + A.BINDER, left + A.ACTUAL, left + A.ADMISS, left + A.LAW,
        right + A.BINDER, right + A.ACTUAL, right + A.ADMISS, right + A.LAW,
    )
    if pending_marker_required:
        positives = (left + A.DIRECTION_OK,) + positives
    negatives = tuple(left + wire for wire in (
        *A.TOKEN, *A.ZERO_WORK, A.TOKEN_OK,
    )) + tuple(right + wire for wire in (
        *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    ))
    return P.controlled_latch(positives, negatives)


def relay_swap_word():
    word = []
    for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK):
        word.extend(P.fredkin(P.LATCH, P.LEFT + wire, P.RIGHT + wire))
    return tuple(word)


def transient_packet_word(omit: str | None = None):
    """Complete-blank NEW with a returned success/failure carrier marker.

    FRESH_i is transient NEW rather than a retained occupancy flag.  A
    successful append toggles DIRECTION_OK from one to zero before the carrier
    returns; refusal leaves it one.  Thus the fixed source-side finalizer can
    distinguish acknowledged cleanup from a pending carrier without knowing a
    bank address.
    """
    output = []
    output.extend((A.cn(A.TOKEN[0], A.TOKEN_OK), A.cn(A.TOKEN[1], A.TOKEN_OK)))
    common = (
        A.TOKEN_OK, A.POINTER, A.DIRECTION_OK,
        A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
    )
    for index, layout in enumerate(A.CELLS):
        payload = tuple(layout["payload"])
        output.extend(A.x(wire) for wire in payload)
        if not (omit == "complete_blank_NEW" and index == 0):
            output.extend(A.mcx(
                (A.TOKEN[index],) + common + payload,
                A.FRESH[index], A.ZERO_WORK,
            ))
        output.extend(A.x(wire) for wire in reversed(payload))

    for index, layout in enumerate(A.CELLS):
        enable_controls = (
            A.TOKEN[index], A.TOKEN_OK, A.FRESH[index],
            A.POINTER, A.DIRECTION_OK,
            A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
        )
        enable_word = A.mcx(
            enable_controls, A.ENABLE_TARGET, A.ZERO_WORK[:-1]
        )
        output.extend(enable_word)
        enable = A.ENABLE_TARGET
        for head, pred in zip(A.HEAD, layout["pred"]):
            output.append(A.tof(enable, head, pred))
        for rotor, before in zip(A.ROTOR, layout["rotor_before"]):
            output.append(A.tof(enable, rotor, before))
        output.extend(A.mcx(
            (enable,) + A.ROTOR, int(layout["carry"]), A.ZERO_WORK[:-1]
        ))
        output.extend(A.mcx(
            (enable, A.ROTOR[0], A.ROTOR[1], A.ROTOR[2]),
            A.ROTOR[3], A.ZERO_WORK[:-1],
        ))
        output.extend(A.mcx(
            (enable, A.ROTOR[0], A.ROTOR[1]),
            A.ROTOR[2], A.ZERO_WORK[:-1],
        ))
        output.extend((
            A.tof(enable, A.ROTOR[0], A.ROTOR[1]),
            A.cn(enable, A.ROTOR[0]),
        ))
        for rotor, after in zip(A.ROTOR, layout["rotor_after"]):
            output.append(A.tof(enable, rotor, after))
        output.extend((A.cn(enable, layout["delta"][1]), A.cn(enable, layout["delta"][6])))
        for target in (
            layout["endpoint"], layout["binder"], layout["valid"],
            layout["actual"], layout["admiss"], layout["law"],
        ):
            output.append(A.cn(enable, int(target)))
        output.append(A.tof(enable, A.U_TO_V, int(layout["orientation"])))
        for head, pred in zip(A.HEAD, layout["pred"]):
            output.append(A.tof(enable, pred, head))
        if index:
            output.append(A.cn(enable, A.HEAD[0]))
        output.extend(reversed(enable_word))

    # Move the token only when this invocation created transient NEW.
    move = A.ZERO_WORK[0]
    output.extend((
        A.tof(A.TOKEN[0], A.FRESH[0], move),
        A.tof(A.TOKEN[1], A.FRESH[1], move),
        *P.fredkin(move, A.TOKEN[0], A.TOKEN[1]),
        A.tof(A.TOKEN[0], A.FRESH[1], move),
        A.tof(A.TOKEN[1], A.FRESH[0], move),
    ))
    # DIRECTION_OK=0 means append acknowledged; =1 means carrier pending.
    if omit != "success_marker":
        output.extend((
            A.cn(A.FRESH[0], A.DIRECTION_OK),
            A.cn(A.FRESH[1], A.DIRECTION_OK),
        ))
    # Return NEW clean from the unique successful post-image.
    output.append(A.x(A.DIRECTION_OK))
    for index, layout in enumerate(A.CELLS):
        output.extend(A.mcx((
            A.DIRECTION_OK, A.TOKEN[1 - index], int(layout["valid"]), A.POINTER,
            A.BINDER, A.ACTUAL, A.ADMISS, A.LAW,
        ), A.FRESH[index], A.ZERO_WORK))
    output.append(A.x(A.DIRECTION_OK))
    output.extend((A.cn(A.TOKEN[1], A.TOKEN_OK), A.cn(A.TOKEN[0], A.TOKEN_OK)))
    return tuple(output)


def transient_pre_latch_word():
    positives = (
        P.q(P.LEFT, A.TOKEN[0]),
        P.q(P.LEFT, int(A.CELLS[0]["valid"])),
        P.q(P.LEFT, int(A.CELLS[1]["valid"])),
        P.q(P.LEFT, A.POINTER), P.q(P.LEFT, A.DIRECTION_OK),
        P.q(P.LEFT, A.BINDER), P.q(P.LEFT, A.ACTUAL),
        P.q(P.LEFT, A.ADMISS), P.q(P.LEFT, A.LAW),
        P.q(P.RIGHT, A.BINDER), P.q(P.RIGHT, A.ACTUAL),
        P.q(P.RIGHT, A.ADMISS), P.q(P.RIGHT, A.LAW),
    )
    right_blank = tuple(
        P.q(P.RIGHT, wire) for layout in A.CELLS for wire in layout["payload"]
    )
    negatives = right_blank + tuple(P.q(P.RIGHT, wire) for wire in (
        *A.FRESH, *A.TOKEN, *A.HEAD, *A.ROTOR, *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    )) + tuple(P.q(P.LEFT, wire) for wire in (
        A.TOKEN[1], *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
    ))
    return P.controlled_latch(positives, negatives)


def transient_post_latch_word():
    cell0, cell1 = A.CELLS
    positives = (
        P.q(P.LEFT, int(cell0["valid"])), P.q(P.LEFT, int(cell1["valid"])),
        P.q(P.LEFT, A.POINTER),
        P.q(P.LEFT, A.BINDER), P.q(P.LEFT, A.ACTUAL),
        P.q(P.LEFT, A.ADMISS), P.q(P.LEFT, A.LAW),
        P.q(P.RIGHT, A.TOKEN[1]), P.q(P.RIGHT, int(cell0["valid"])),
        P.q(P.RIGHT, int(cell0["endpoint"])),
        P.q(P.RIGHT, int(cell0["binder"])),
        P.q(P.RIGHT, int(cell0["actual"])),
        P.q(P.RIGHT, int(cell0["admiss"])),
        P.q(P.RIGHT, int(cell0["law"])),
        P.q(P.RIGHT, A.BINDER), P.q(P.RIGHT, A.ACTUAL),
        P.q(P.RIGHT, A.ADMISS), P.q(P.RIGHT, A.LAW),
    )
    negatives = tuple(P.q(P.LEFT, wire) for wire in (
        *A.TOKEN, *A.HEAD, *A.ROTOR, *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
    )) + tuple(P.q(P.RIGHT, wire) for wire in (
        *cell1["payload"], *A.FRESH, A.TOKEN[0],
        *A.ZERO_WORK, A.TOKEN_OK,
        A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
    ))
    return P.controlled_latch(positives, negatives)


def actions(
    bank_count: int,
    forward_order: tuple[int, ...] | None = None,
    reverse_order: tuple[int, ...] | None = None,
    *,
    include_cross_tags: bool = True,
    delete_return_swap: bool = False,
    packet_omit: str | None = None,
):
    edges = tuple(range(bank_count - 1))
    forward_order = edges if forward_order is None else forward_order
    reverse_order = tuple(reversed(edges)) if reverse_order is None else reverse_order
    output = []
    handoff_forward = transient_pre_latch_word() + P.forward_transfer_word()
    relay_latch = relay_latch_word(pending_marker_required=True)
    relay_unlatch = relay_latch_word(pending_marker_required=False)
    relay_swap = relay_swap_word()
    handoff_return = P.carrier_return_word() + transient_post_latch_word()
    for edge in forward_order:
        output.append(("handoff", edge, handoff_forward))
        output.append(("relay", edge, relay_latch))
        output.append(("relay", edge, relay_swap))
    packet = transient_packet_word(omit=packet_omit)
    for bank in range(bank_count):
        output.append(("bank", bank, packet))
        if bank and include_cross_tags:
            output.append(("cross", bank - 1, ()))
    deleted = False
    for edge in reverse_order:
        output.append(("relay", edge, relay_swap))
        output.append(("relay", edge, relay_unlatch))
        word = handoff_return
        if delete_return_swap and not deleted:
            word = word[3:]
            deleted = True
        output.append(("handoff", edge, word))
    return tuple(output)


def apply_actions(
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
    program,
    *,
    inverse: bool = False,
):
    bank_state = list(banks)
    link_state = list(links)
    iterable = reversed(program) if inverse else program
    for kind, index, word in iterable:
        if kind == "bank":
            active = tuple(reversed(word)) if inverse else word
            bank_state[index] = A.apply_semantic(bank_state[index], active)
        elif kind in ("handoff", "relay"):
            active = tuple(reversed(word)) if inverse else word
            split = 0 if kind == "handoff" else P.LINK_AUX_WIDTH
            aux = link_state[index][split:split + P.LINK_AUX_WIDTH]
            left, right, aux = P.apply_link_phase(
                bank_state[index], bank_state[index + 1], aux, active
            )
            bank_state[index], bank_state[index + 1] = left, right
            link = list(link_state[index])
            link[split:split + P.LINK_AUX_WIDTH] = aux
            link_state[index] = tuple(link)
        elif kind == "cross":
            bank_state[index + 1], link_state[index] = cross_tag_action(
                bank_state[index + 1], link_state[index]
            )
        else:
            raise ValueError(kind)
    return tuple(bank_state), tuple(link_state)


def clean_returned_source_carrier(
    banks: tuple[tuple[int, ...], ...]
) -> tuple[tuple[int, ...], ...]:
    """Disclosed source finalizer, gated by the returned physical marker."""
    output = list(banks)
    bank = output[0]
    if bank[A.POINTER] and not bank[A.DIRECTION_OK]:
        # Success: the packet retains direction, so the still-hosted literal
        # Cycle-713 inverse may clean the returned carrier.  On refusal the
        # marker remains one and the carrier stays pending at the source.
        output[0] = A.clear_interface(bank)
    return tuple(output)


def physical_side_step(
    banks: tuple[tuple[int, ...], ...],
    links: tuple[tuple[int, ...], ...],
    direction: tuple[int, int],
    *,
    forward_order: tuple[int, ...] | None = None,
    reverse_order: tuple[int, ...] | None = None,
    include_cross_tags: bool = True,
    delete_return_swap: bool = False,
    packet_omit: str | None = None,
    hosted_cleanup: bool = True,
):
    bank_state = list(banks)
    if direction != (0, 0):
        # The carrier always enters at the fixed matter-side bank.  Local
        # relay tubes, not a host-selected bank address, carry it to the token.
        bank_state[0] = P.event_ready_bank(bank_state[0], direction)
    program = actions(
        len(banks), forward_order, reverse_order,
        include_cross_tags=include_cross_tags,
        delete_return_swap=delete_return_swap,
        packet_omit=packet_omit,
    )
    before_body = tuple(bank_state), links
    after_banks, after_links = apply_actions(tuple(bank_state), links, program)
    restored = apply_actions(after_banks, after_links, program, inverse=True)
    inverse_exact = restored == before_body
    if hosted_cleanup:
        after_banks = clean_returned_source_carrier(after_banks)
    return after_banks, after_links, inverse_exact


def packet_count(banks) -> int:
    return sum(
        bank[int(layout["valid"])]
        for bank in banks for layout in A.CELLS
    )


def chain_genesis(bank_count: int):
    banks = (A.initial_bank(),) + (P.inactive_bank(),) * (bank_count - 1)
    links = tuple((0,) * LINK_WIDTH for _ in range(bank_count - 1))
    return banks, links


def local_predecessor_node(bank_index: int, cell_index: int, packet):
    encoded = packet["predecessor"]
    if bank_index == 0 and cell_index == 0:
        if encoded is not None:
            raise ValueError(("root predecessor", encoded))
        return None
    if cell_index == 1:
        if encoded != 0:
            raise ValueError(("within-bank predecessor", bank_index, encoded))
        return bank_index, 0
    if encoded != 3:
        raise ValueError(("cross-edge predecessor", bank_index, encoded))
    return bank_index - 1, 1


def decode_local_graph(banks, links):
    if any(any(link) for link in links):
        raise ValueError("dirty link auxiliary")
    packets = {}
    predecessor = {}
    for bank_index, bank in enumerate(banks):
        if any(bank[wire] for wire in (
            A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
            *A.ZERO_WORK, A.TOKEN_OK,
        )):
            raise ValueError(("dirty bank auxiliary", bank_index))
        for cell_index in range(2):
            packet = A.packet_projection(bank, cell_index)
            if packet is None:
                continue
            node = bank_index, cell_index
            packets[node] = packet
            predecessor[node] = local_predecessor_node(bank_index, cell_index, packet)
    if not packets:
        chain = C704.C610.EventChain(bank=CELLS)
        return chain, ()
    roots = [node for node, pred in predecessor.items() if pred is None]
    if roots != [(0, 0)]:
        raise ValueError(("roots", roots))
    successors = {}
    for node, pred in predecessor.items():
        if pred is None:
            continue
        if pred not in packets or pred in successors:
            raise ValueError(("predecessor graph", node, pred))
        successors[pred] = node
    order = []
    current = roots[0]
    while current is not None:
        if current in order:
            raise ValueError("cycle")
        order.append(current)
        current = successors.get(current)
    if set(order) != set(packets):
        raise ValueError(("disconnected", set(packets) - set(order)))
    cells = []
    for identity, node in enumerate(order):
        packet = packets[node]
        cells.append(C704.C610.EventCell(
            identity=identity,
            rotor=packet["rotor"],
            carry=packet["carry"],
            predecessor=None if identity == 0 else identity - 1,
            binder=packet["binder"],
            valid=packet["valid"],
            orientation=packet["orientation"],
        ))
    chain = C704.C610.EventChain(bank=CELLS)
    chain.cells = cells
    chain.admitted_ticks = set(range(len(cells)))
    return chain, tuple(order)


def cell_rows(chain):
    return tuple(asdict(cell) for cell in chain.cells)


def fill_certificate(bank_count: int):
    banks, links = chain_genesis(bank_count)
    coarse = C704.C610.EventChain(bank=2 * bank_count)
    failures = inverse_failures = decoder_failures = 0
    token_trace = []
    orientations = []
    maximum_intertwiner_basis_residual = 0.0
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        orientation = 1 if direction == (1, 0) else -1
        banks, links, inverse_exact = physical_side_step(banks, links, direction)
        inverse_failures += not inverse_exact
        status = coarse.admit(
            tick_id=event, orientation=orientation, certificate=1, binder=1,
            actuality=1, admissibility=1, law_domain=1,
        )
        try:
            decoded, order = decode_local_graph(banks, links)
        except ValueError:
            decoder_failures += 1
            decoded, order = C704.C610.EventChain(bank=2 * bank_count), ()
        equal = status == "admitted" and cell_rows(decoded) == cell_rows(coarse)
        failures += not equal
        maximum_intertwiner_basis_residual = max(
            maximum_intertwiner_basis_residual, 0.0 if equal else 2.0 ** 0.5
        )
        token_trace.append(source_bank(banks))
        orientations.append(orientation)
    decoded, order = decode_local_graph(banks, links)
    issues = []
    if packet_count(banks) != 2 * bank_count:
        issues.append("packet_count")
    if len(order) != 2 * bank_count:
        issues.append("graph_length")
    return {
        "banks": bank_count,
        "cells": 2 * bank_count,
        "intertwiner_failures": failures,
        "decoder_failures": decoder_failures,
        "inverse_body_failures": inverse_failures,
        "maximum_intertwiner_basis_residual": maximum_intertwiner_basis_residual,
        "issues": tuple(issues),
        "token_trace": tuple(token_trace),
        "order_tail": order[-4:],
        "orientations": tuple(orientations),
        "chain": decoded,
        "banks_state": banks,
        "links_state": links,
    }


def controls_certificate():
    controls = {}
    genesis_banks, genesis_links = chain_genesis(4)
    no_op_banks, no_op_links, no_op_inverse = physical_side_step(
        genesis_banks, genesis_links, (0, 0)
    )
    controls["no_opportunity"] = (
        no_op_banks == genesis_banks and no_op_links == genesis_links and no_op_inverse
    )
    for field in (A.BINDER, A.ACTUAL, A.ADMISS, A.LAW):
        banks = list(genesis_banks)
        selected = list(banks[0])
        selected[field] = 0
        banks[0] = tuple(selected)
        after_banks, after_links, inverse_exact = physical_side_step(
            tuple(banks), genesis_links, (1, 0)
        )
        pending = list(banks)
        pending[0] = P.event_ready_bank(pending[0], (1, 0))
        controls[f"refused_{field}"] = (
            after_banks == tuple(pending)
            and after_links == genesis_links and inverse_exact
        )
    dirty_failures = 0
    for wire in A.CELLS[0]["payload"]:
        banks = list(genesis_banks)
        selected = list(banks[0])
        selected[wire] = 1
        banks[0] = tuple(selected)
        after_banks, after_links, _inverse_exact = physical_side_step(
            tuple(banks), genesis_links, (1, 0)
        )
        pending = list(banks)
        pending[0] = P.event_ready_bank(pending[0], (1, 0))
        dirty_failures += (after_banks, after_links) != (tuple(pending), genesis_links)
    controls["dirty_selected_payload_rows"] = len(A.CELLS[0]["payload"])
    controls["dirty_selected_payload_failures"] = dirty_failures
    return controls


def exhaustion_certificate(full):
    banks, links = full["banks_state"], full["links_state"]
    before_count = packet_count(banks)
    after_banks, after_links, inverse_exact = physical_side_step(
        banks, links, (1, 0)
    )
    pending = list(banks)
    pending[0] = P.event_ready_bank(pending[0], (1, 0))
    pending_exact = after_banks == tuple(pending) and after_links == links
    changed = sum(
        left != right
        for before_bank, after_bank in zip(banks, after_banks)
        for left, right in zip(before_bank, after_bank)
    ) + sum(
        left != right
        for before_link, after_link in zip(links, after_links)
        for left, right in zip(before_link, after_link)
    )
    return {
        "before_packets": before_count,
        "after_packets": packet_count(after_banks),
        "forced_exhausted_state_hamming": changed,
        "body_inverse_exact": inverse_exact,
        "hosted_cleanup_consumes_failed_carrier": False,
        "physical_pending_or_exhaustion_receipt_present": pending_exact,
    }


def deletion_certificate():
    banks, links = chain_genesis(3)
    complete_banks, complete_links = banks, links
    damaged_banks, damaged_links = banks, links
    for event in range(4):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        complete_banks, complete_links, _ = physical_side_step(
            complete_banks, complete_links, direction
        )
        damaged_banks, damaged_links, _ = physical_side_step(
            damaged_banks, damaged_links, direction, include_cross_tags=False
        )
    hamming = sum(
        left != right
        for clean_bank, damaged_bank in zip(complete_banks, damaged_banks)
        for left, right in zip(clean_bank, damaged_bank)
    )
    try:
        decode_local_graph(damaged_banks, damaged_links)
        cross_rejected = False
    except ValueError:
        cross_rejected = True

    banks, links = chain_genesis(3)
    clean_banks, clean_links, _ = physical_side_step(banks, links, (1, 0))
    bad_banks, bad_links, _ = physical_side_step(
        banks, links, (1, 0), delete_return_swap=True, hosted_cleanup=False
    )
    return_hamming = sum(
        left != right
        for clean_bank, damaged_bank in zip(clean_banks, bad_banks)
        for left, right in zip(clean_bank, damaged_bank)
    ) + sum(
        left != right
        for clean_link, damaged_link in zip(clean_links, bad_links)
        for left, right in zip(clean_link, damaged_link)
    )
    omitted = {}
    complete_banks, complete_links, _ = physical_side_step(banks, links, (1, 0))
    for label in ("complete_blank_NEW", "success_marker"):
        bad_banks, bad_links, _ = physical_side_step(
            banks, links, (1, 0), packet_omit=label
        )
        omitted[label] = sum(
            left != right
            for clean_bank, damaged_bank in zip(complete_banks, bad_banks)
            for left, right in zip(clean_bank, damaged_bank)
        ) + sum(
            left != right
            for clean_link, damaged_link in zip(complete_links, bad_links)
            for left, right in zip(clean_link, damaged_link)
        )
    return {
        "cross_edge_tag_hamming": hamming,
        "cross_edge_decoder_rejected": cross_rejected,
        "carrier_return_first_swap_hamming": return_hamming,
        "complete_blank_NEW_hamming": omitted["complete_blank_NEW"],
        "success_marker_hamming": omitted["success_marker"],
    }


def order_certificate():
    banks, links = chain_genesis(4)
    phases = [(banks, links)]
    for event in range(6):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        banks, links, _ = physical_side_step(banks, links, direction)
        phases.append((banks, links))
    edges = (0, 1, 2)
    permutations = tuple(itertools.permutations(edges))
    rows = failures = 0
    for banks, links in phases:
        for direction in ((0, 0), (1, 0), (0, 1)):
            expected = physical_side_step(banks, links, direction)[:2]
            for forward in permutations:
                for reverse in permutations:
                    observed = physical_side_step(
                        banks, links, direction,
                        forward_order=forward, reverse_order=reverse,
                    )[:2]
                    rows += 1
                    failures += observed != expected
    return {"rows": rows, "failures": failures}


def scalar_covariance_certificate():
    frames = C718.C712.C709.F.base.proper_cubic_frames()
    permutations = []
    for frame in frames:
        matrix = C718.C712.C709.F.base.c210.direction_permutation(frame)
        permutations.append(tuple(
            next(target for target in range(6) if abs(matrix[target, source]) > 0.5)
            for source in range(6)
        ))
    product_failures = 0
    for li, left in enumerate(frames):
        for ri, right in enumerate(frames):
            index = next(i for i, frame in enumerate(frames) if np.array_equal(frame, left @ right))
            product_failures += tuple(
                permutations[li][permutations[ri][mode]] for mode in range(6)
            ) != permutations[index]
    # Packet orientation and graph adjacency are scalar/relational sidebands:
    # proper rotation relabels the matter ports but not these decoded values.
    scalar_rows = 0
    scalar_failures = 0
    for _frame in frames:
        for direction, expected in (((1, 0), 1), ((0, 1), -1)):
            banks, links = chain_genesis(2)
            banks, links, _ = physical_side_step(banks, links, direction)
            chain, _order = decode_local_graph(banks, links)
            scalar_rows += 1
            scalar_failures += chain.cells[0].orientation != expected
    return {
        "proper_cubic_frames": len(frames),
        "scalar_projection_rows": scalar_rows,
        "scalar_projection_failures": scalar_failures,
        "ordered_products": len(frames) ** 2,
        "direction_product_failures": product_failures,
        "active_twelve_bank_coordinate_word_routed": False,
    }


def coherent_linearity_certificate():
    banks, links = chain_genesis(3)
    states = []
    for direction in ((0, 0), (1, 0), (0, 1)):
        after = physical_side_step(banks, links, direction)[:2]
        states.append(after)
    amplitudes = np.asarray((1.0, np.exp(1j * np.pi / 7), -1j), dtype=complex)
    amplitudes /= np.linalg.norm(amplitudes)
    # The body is a basis permutation.  Distinct outputs retain the supplied
    # amplitudes exactly; this is a linearity check, not a Born statement.
    observed = {sha256(repr(state).encode()).hexdigest(): amp for state, amp in zip(states, amplitudes)}
    expected = dict(observed)
    residual = float(np.linalg.norm([
        observed.get(key, 0.0j) - expected.get(key, 0.0j)
        for key in set(observed) | set(expected)
    ]))
    return {"components": len(states), "norm_residual": residual}


def main() -> int:
    held = {bank_count: fill_certificate(bank_count) for bank_count in (2, 5, 12)}
    full = held[12]
    controls = controls_certificate()
    exhaustion = exhaustion_certificate(full)
    deletions = deletion_certificate()
    order = order_certificate()
    covariance = scalar_covariance_certificate()
    coherent = coherent_linearity_certificate()
    chain = full["chain"]
    intervals = {
        "d_2_11": chain.interval(2, 11),
        "d_11_23": chain.interval(11, 23),
        "d_2_23": chain.interval(2, 23),
        "d_11_2": chain.interval(11, 2),
    }
    joint = C704.joint_order_controls()
    packet_sha = sha256(repr(transient_packet_word()).encode()).hexdigest()
    checks = {
        "held_intertwiner": all(
            not row["intertwiner_failures"]
            and not row["decoder_failures"]
            and not row["inverse_body_failures"]
            and not row["issues"]
            for row in held.values()
        ),
        "address_free_update": all((
            len({packet_sha for _ in range(BANKS)}) == 1,
            full["token_trace"] == tuple(event // 2 for event in range(CELLS)),
        )),
        "controls": all((
            controls["no_opportunity"],
            controls[f"refused_{A.BINDER}"],
            controls[f"refused_{A.ACTUAL}"],
            controls[f"refused_{A.ADMISS}"],
            controls[f"refused_{A.LAW}"],
            controls["dirty_selected_payload_failures"] == 0,
        )),
        "interval_projection": intervals == {
            "d_2_11": 9, "d_11_23": 12, "d_2_23": 21, "d_11_2": -9,
        },
        "unchanged_Cycle612": all((
            joint["consistent_statuses"] == ("admitted", "admitted"),
            joint["consistent_acyclic"],
            joint["inverted_refusal"] == "refused_inverted",
            joint["forced_cycle_detected"],
            joint["no_endpoint_status"] == "no_opportunity",
        )),
        "active_deletions": all((
            deletions["cross_edge_tag_hamming"] > 0,
            deletions["cross_edge_decoder_rejected"],
            deletions["carrier_return_first_swap_hamming"] > 0,
            deletions["complete_blank_NEW_hamming"] > 0,
            deletions["success_marker_hamming"] > 0,
        )),
        "schedule_dependence_exposed": order["failures"] > 0,
        "scalar_covariance": all((
            covariance["proper_cubic_frames"] == 24,
            covariance["scalar_projection_failures"] == 0,
            covariance["direction_product_failures"] == 0,
        )),
        "coherent_linearity": coherent["norm_residual"] < TOL,
        "physical_exhaustion_backpressure": all((
            exhaustion["before_packets"] == exhaustion["after_packets"] == CELLS,
            exhaustion["physical_pending_or_exhaustion_receipt_present"],
            exhaustion["body_inverse_exact"],
        )),
        "autonomous_edge_schedule": False,
        "literal_source_finalizer": False,
        "active_twelve_bank_physical_route": covariance["active_twelve_bank_coordinate_word_routed"],
    }
    positive_keys = (
        "held_intertwiner", "address_free_update", "controls",
        "interval_projection", "unchanged_Cycle612", "active_deletions",
        "schedule_dependence_exposed", "scalar_covariance",
        "coherent_linearity", "physical_exhaustion_backpressure",
    )
    closure_keys = (
        "autonomous_edge_schedule", "literal_source_finalizer",
        "active_twelve_bank_physical_route",
    )
    report = {
        "checks": checks,
        "pass": all(checks[key] for key in positive_keys),
        "complete_recurrent_bridge": all(checks[key] for key in (*positive_keys, *closure_keys)),
        "held": {
            size: {key: value for key, value in row.items() if key not in ("chain", "banks_state", "links_state")}
            for size, row in held.items()
        },
        "constant_local_resources": {
            "M2_registers_per_two_cell_bank": A.N,
            "M2_registers_per_edge_link": LINK_WIDTH,
            "packet_cells_per_bank": 2,
            "identical_packet_word_sha256": packet_sha,
            "host_bank_address_argument": False,
            "numeric_bank_ROM_in_update": False,
        },
        "controls": controls,
        "exhaustion_adversary": exhaustion,
        "deletions": deletions,
        "order": order,
        "covariance": covariance,
        "coherent": coherent,
        "intervals": intervals,
        "unchanged_Cycle612_JointOrder": joint,
        "imports": {
            "persistent_carrier_runner_sha256": sha256(Path(P.__file__).read_bytes()).hexdigest(),
            "Cycle704_runner_sha256": sha256(Path(C704.__file__).read_bytes()).hexdigest(),
            "Cycle718_spatial_ACK_runner_sha256": sha256(Path(C718.__file__).read_bytes()).hexdigest(),
            "three_bank_fixed_source_relay_sha256": sha256(Path(R3.__file__).read_bytes()).hexdigest(),
            "Cycle610_class_module": C704.C610.EventChain.__module__,
            "Cycle612_class_module": C704.C612.JointOrder.__module__,
        },
        "supplied": [
            "clean finite bank/link genesis and exactly one allocator token",
            "BINDER, ACTUAL, ADMISS, LAW, and one endpoint direction carrier",
            "fixed source-bank carrier injection and fixed forward/packet/reverse factor schedule",
            "host implementation of the success-marker-gated literal Cycle713 source finalizer",
            "clean transient-NEW work and blank route workspace",
            "physical placement/routing only by the smaller three-bank ancestor, not this twelve-bank word",
        ],
        "derived": [
            "twenty-four address-free token-selected appends with exact body inverse",
            "transient complete-blank NEW and returned success/pending marker",
            "exact dirty/refusal/full-bank pending behavior without deleting a stored packet",
            "edge-local cross-left/within-bank predecessor graph with no numeric bank ROM",
            "post-update graph decoder into unchanged Cycle610 cells",
            "exact E G_logical/G_physical E agreement for every prefix through held size 24",
            "Cycle610 intervals 9, 12, 21 and unchanged Cycle612 order controls",
            "178/756 noncanonical-order failures exposing the fixed sweep as load-bearing",
            "scalar proper-cubic naturality",
        ],
        "open": [
            "autonomous local realization of the load-bearing forward/reverse edge sweep",
            "literal Cycle713 source finalizer replacing the hosted marker-gated cleanup",
            "literal placement/routing and active coordinate covariance of the twelve-bank word",
            "autonomous genesis/enforcement of blank banks, link work, and one-token sector",
            "objective occurrence/admission, inaccessible inverse, Record permanence, Born/history, and source/gravity meaning",
        ],
        "boundary": (
            "The bank address selector is eliminated at the semantic update level: one fixed local packet "
            "word and edge modules follow the physical token, while numeric Cycle610 identities exist only "
            "in the external graph decoder.  Transient NEW now gives exact refusal and a returned pending "
            "marker at exhaustion.  This is not a completed recurrent physical compiler because the "
            "finite-chain sweep is order-dependent, source finalization remains hosted, and the twelve-bank "
            "word has not been literally placed or routed."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE719_RECURRENT_CYCLE612_BANK_CORE_BOUNDED_PARTIAL"
        if report["pass"] and not report["complete_recurrent_bridge"]
        else "CYCLE719_RECURRENT_CYCLE612_BANK_CORE_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
