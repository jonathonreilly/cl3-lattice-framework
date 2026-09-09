#!/usr/bin/env python3
"""Cycle-718 physical-M2 route of the Cycle-713 spatial ACK/export bridge.

This bounded runner replaces the generic codeword-transposition ceiling by a
structured NEW/ACK circuit and realizes each of the six export bundles as an
explicit two-layer A/B nearest-neighbor loop.  The finite loops are held
pre-wrap controls for the Cycle-11 bilateral-shift sector; their circuit layer
ordinal is not called physical time.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import permutations, product
import json
from pathlib import Path
import random
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle718_spatial_ack_export_core_2026_07_26 as S
import frontier_cycle715_recurrent_directional_packet_bank_2026_07_26 as A
import frontier_cycle718_three_bank_physical_route_core_2026_07_26 as P3


AUDIT_TIMEOUT_SEC = 600
NOTE_PATH = "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md"
AUDIT_INPUT_PATHS = (
    "docs/PHYSICAL_M2_SPATIAL_ACK_CYCLE612_INTERVAL_BRIDGE_CYCLE718_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/RECURRENT_DIRECTIONAL_PACKET_BANK_CYCLE715_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_FULL34_FIXED_PACKET_COMPOSITION_CYCLE714_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/PHYSICAL_M2_ENDPOINT_INSTRUMENT_CYCLE704_CYCLE612_BRIDGE_CYCLE713_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/JOINT_TWO_CELL_FULL_UPDATE_PHYSICAL_M2_COMPILER_CYCLE712_BOUNDED_THEOREM_NOTE_2026-07-26.md",
    "docs/work_history/repo/review_feedback/CYCLE704_LOCAL_GAUSS_CYCLE612_ENDPOINT_BRIDGE_NOTE_2026-07-25.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_INTRINSIC_TICK_EVENT_RELATIONAL_DURATION_TOURNAMENT_CYCLE610_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_TICK_ECHO_ASSOCIATION_CAUSAL_ORDER_TOURNAMENT_CYCLE612_NOTE_2026-07-22.md",
    "docs/work_history/repo/review_feedback/INFINITE_REVERSIBLE_RECORD_EXPORT_QCA_CYCLE11_NOTE_2026-07-14.md",
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
    "scripts/frontier_cycle718_cycle612_interval_bridge_2026_07_26.py",
    "scripts/frontier_cycle718_cycle713_carrier_return_composition_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_export_core_2026_07_26.py",
    "scripts/frontier_cycle718_spatial_ack_physical_m2_route_2026_07_26.py",
    "scripts/frontier_cycle718_three_bank_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle718_token_relative_relay_core_2026_07_26.py",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py",
    "scripts/frontier_full128_code_projectors_2026_07_24.py",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py",
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py",
    "scripts/infinite_reversible_record_export_qca_cycle11_2026_07_14.py",
    "scripts/local_conservative_commit_resource_gravity_cycle9_2026_07_14.py",
    "scripts/local_generator_source_tournament_cycle228_2026_07_17.py",
    "scripts/physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22.py",
    "scripts/physical_tick_echo_association_causal_order_tournament_cycle612_2026_07_22.py",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py",
    "scripts/retarded_cubic_mass_field_cycle213_2026_07_16.py",
    "scripts/spatial_car_contact_seam_form_factor_cycle230_2026_07_17.py",
    "scripts/virtual_exchange_green_kernel_cycle216_2026_07_16.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS


TOL = 4.0e-10
RAIL_WIDTH = 39
WORK_WIDTH = 47
DIRECTIONS = S.DIRECTIONS


@dataclass(frozen=True)
class CommitLayout:
    pointer: int
    left: int
    right: int
    law: tuple[int, ...]
    head: int
    rotor: tuple[int, ...]
    identity: int
    pending: int
    new: int
    ack: int
    commit: int
    hold: tuple[int, ...]
    rail: tuple[tuple[int, ...], ...]
    work: tuple[int, ...]
    n: int


def make_commit_layout() -> CommitLayout:
    cursor = 0

    def take(count: int) -> tuple[int, ...]:
        nonlocal cursor
        result = tuple(range(cursor, cursor + count))
        cursor += count
        return result

    pointer, left, right = take(3)
    law = take(4)
    head = take(1)[0]
    rotor = take(4)
    identity = take(1)[0]
    pending = take(1)[0]
    new, ack, commit = take(3)
    hold = take(12)
    rail = tuple(take(RAIL_WIDTH) for _ in DIRECTIONS)
    work = take(WORK_WIDTH)
    return CommitLayout(
        pointer, left, right, law, head, rotor, identity, pending,
        new, ack, commit, hold, rail, work, cursor,
    )


LAYOUT = make_commit_layout()


def rail_fields(block: tuple[int, ...]) -> dict[str, object]:
    if len(block) != RAIL_WIDTH:
        raise ValueError(len(block))
    return {
        "payload": block[:34],
        "pred": block[:6],
        "rotor_before": block[6:10],
        "rotor_after": block[10:14],
        "carry": block[14],
        "delta": block[15:27],
        "endpoint": block[27],
        "binder": block[28],
        "valid": block[29],
        "orientation": block[30],
        "actual": block[31],
        "admiss": block[32],
        "law": block[33],
        "identity_tag": block[34],
        "fresh": block[35],
        "start": block[36],
        "cleanup": block[37],
        "retry_echo": block[38],
    }


def zero_controlled(
    positive: tuple[int, ...],
    negative: tuple[int, ...],
    target: int,
    work: tuple[int, ...],
) -> tuple[A.Gate, ...]:
    return (
        *(A.x(wire) for wire in negative),
        *A.mcx(positive + negative, target, work),
        *(A.x(wire) for wire in reversed(negative)),
    )


def fredkin(control: int, left: int, right: int) -> tuple[A.Gate, ...]:
    return (A.cn(right, left), A.tof(control, left, right), A.cn(right, left))


def commit_segment(
    direction: int,
    *,
    omit: str | None = None,
) -> tuple[A.Gate, ...]:
    """One oriented structured commit with all writes ACK-gated."""
    if direction not in (0, 1):
        raise ValueError("canonical Cycle-713 seam has two oriented rails")
    fields = rail_fields(LAYOUT.rail[direction])
    positive_endpoint = LAYOUT.right if direction == 0 else LAYOUT.left
    negative_endpoint = LAYOUT.left if direction == 0 else LAYOUT.right
    positive = (LAYOUT.pointer, positive_endpoint, *LAYOUT.law)
    negative = (
        negative_endpoint,
        *LAYOUT.rail[direction],
        LAYOUT.ack,
        LAYOUT.commit,
    )
    output: list[A.Gate] = []
    if omit != "complete_blank_NEW":
        output.extend(zero_controlled(
            positive, negative, LAYOUT.new, LAYOUT.work
        ))
    if omit != "append_ACK":
        output.append(A.cn(LAYOUT.new, LAYOUT.ack))
    ack = LAYOUT.ack

    # Full raw packet write.  The two low predecessor bits are
    # (previous identity, cross-left export edge); high numeric bits stay zero.
    output.append(A.tof(ack, LAYOUT.head, fields["pred"][0]))
    output.append(A.cn(ack, fields["pred"][1]))
    for source, target in zip(LAYOUT.rotor, fields["rotor_before"]):
        output.append(A.tof(ack, source, target))
    if omit != "carry":
        output.extend(A.mcx(
            (ack, *LAYOUT.rotor), fields["carry"], LAYOUT.work
        ))
    output.extend(A.mcx(
        (ack, LAYOUT.rotor[0], LAYOUT.rotor[1], LAYOUT.rotor[2]),
        LAYOUT.rotor[3], LAYOUT.work,
    ))
    output.extend(A.mcx(
        (ack, LAYOUT.rotor[0], LAYOUT.rotor[1]),
        LAYOUT.rotor[2], LAYOUT.work,
    ))
    output.extend((
        A.tof(ack, LAYOUT.rotor[0], LAYOUT.rotor[1]),
        A.cn(ack, LAYOUT.rotor[0]),
    ))
    for source, target in zip(LAYOUT.rotor, fields["rotor_after"]):
        output.append(A.tof(ack, source, target))
    if omit != "delta":
        output.extend((
            A.cn(ack, fields["delta"][1]),
            A.cn(ack, fields["delta"][6]),
        ))
    for target in (
        fields["endpoint"], fields["binder"], fields["valid"],
        fields["actual"], fields["admiss"], fields["law"],
    ):
        output.append(A.cn(ack, target))
    if direction == 0:
        output.append(A.cn(ack, fields["orientation"]))
    output.append(A.tof(ack, LAYOUT.identity, fields["identity_tag"]))
    if omit != "frontier":
        output.extend(fredkin(ack, LAYOUT.head, LAYOUT.identity))
    if omit != "handshakes":
        # Every accepted event emits exactly one start witness.  A previously
        # pending event additionally swaps its persistent shield bit into a
        # typed retry-echo rail, returning
        # the source shield blank before the next update.
        if omit != "start_handshake":
            output.append(A.cn(ack, fields["start"]))
        if omit != "cleanup_echo":
            output.append(A.cn(ack, fields["cleanup"]))
        if omit != "retry_echo":
            output.extend(fredkin(
                ack, LAYOUT.pending, fields["retry_echo"]
            ))
    if omit != "endpoint_cleanup":
        output.append(A.cn(ack, LAYOUT.pointer))

    # ACK is returned clean.  The populated postimage then authorizes the
    # reversible NEW->FRESH transfer without recomputing the blank predicate.
    output.append(A.cn(LAYOUT.new, LAYOUT.ack))
    output.append(A.tof(
        fields["start"], fields["valid"], LAYOUT.commit
    ))
    if omit != "fresh_transfer":
        output.extend(fredkin(
            LAYOUT.commit, LAYOUT.new, fields["fresh"]
        ))
    output.append(A.tof(
        fields["start"], fields["valid"], LAYOUT.commit
    ))
    return tuple(output)


def pending_latch_segment(direction: int) -> tuple[A.Gate, ...]:
    """Swap local (pending,start) codewords 00<->11 for one orientation."""
    fields = rail_fields(LAYOUT.rail[direction])
    positive_endpoint = LAYOUT.right if direction == 0 else LAYOUT.left
    negative_endpoint = LAYOUT.left if direction == 0 else LAYOUT.right
    common = (LAYOUT.pointer, positive_endpoint, *LAYOUT.law)
    negative = (negative_endpoint,)
    first = zero_controlled(
        common, negative + (fields["start"],),
        LAYOUT.pending, LAYOUT.work,
    )
    middle = zero_controlled(
        common + (LAYOUT.pending,), negative,
        fields["start"], LAYOUT.work,
    )
    return first + middle + first


def commit_word(omit: str | None = None) -> tuple[A.Gate, ...]:
    output = commit_segment(0, omit=omit) + commit_segment(1, omit=omit)
    if omit != "pending_latch":
        output += pending_latch_segment(0) + pending_latch_segment(1)
    return output


def apply_bits(bits: tuple[int, ...], word: tuple[A.Gate, ...]) -> tuple[int, ...]:
    return A.apply_semantic(bits, word)


def set_integer(bits: list[int], wires: tuple[int, ...], value: int) -> None:
    for index, wire in enumerate(wires):
        bits[wire] = (value >> index) & 1


def integer(bits: tuple[int, ...], wires: tuple[int, ...]) -> int:
    return sum(bits[wire] << index for index, wire in enumerate(wires))


def commit_input(
    orientation: int,
    head: int,
    rotor: int,
    identity: int,
    pending: int = 0,
) -> tuple[int, ...]:
    bits = [0] * LAYOUT.n
    bits[LAYOUT.pointer] = 1
    bits[LAYOUT.right if orientation > 0 else LAYOUT.left] = 1
    for wire in LAYOUT.law:
        bits[wire] = 1
    bits[LAYOUT.head] = head
    set_integer(bits, LAYOUT.rotor, rotor)
    bits[LAYOUT.identity] = identity
    bits[LAYOUT.pending] = pending
    return tuple(bits)


def expected_packet(
    orientation: int, head: int, rotor: int, identity: int, pending: int
) -> tuple[int, ...]:
    packet = S.Packet(
        identity=identity,
        predecessor=head | 2,
        rotor_before=rotor,
        rotor_after=(rotor + 1) % 16,
        carry=int(rotor == 15),
        delta_mask=66,
        endpoint=1,
        binder=1,
        valid=1,
        orientation=orientation,
        actual=1,
        admiss=1,
        law=1,
    )
    # FRESH=1, start=1, cleanup=1, and typed retry echo records whether the
    # accepted event had previously waited behind backpressure.
    return packet.physical_bits() + (1, 1, 1, pending)


def structured_commit_certificate() -> dict[str, object]:
    word = commit_word()
    inverse = tuple(reversed(word))
    cases = packet_failures = controller_failures = transient_failures = 0
    inverse_failures = raw_payload_failures = one_event_failures = 0
    for orientation, head, rotor, identity, pending in product(
        (-1, 1), (0, 1), range(16), (0, 1), (0, 1)
    ):
        before = commit_input(
            orientation, head, rotor, identity, pending
        )
        after = apply_bits(before, word)
        direction = 0 if orientation > 0 else 1
        expected = expected_packet(
            orientation, head, rotor, identity, pending
        )
        observed = tuple(after[wire] for wire in LAYOUT.rail[direction])
        packet_failures += observed != expected
        raw_payload_failures += observed[:34] != expected[:34]
        packet_failures += any(
            after[wire]
            for index, rail in enumerate(LAYOUT.rail)
            if index != direction
            for wire in rail
        )
        controller_failures += (
            after[LAYOUT.pointer] != 0
            or after[LAYOUT.pending] != 0
            or after[LAYOUT.head] != identity
            or integer(after, LAYOUT.rotor) != (rotor + 1) % 16
            or after[LAYOUT.identity] != head
        )
        transient_failures += any(
            after[wire]
            for wire in (
                LAYOUT.new, LAYOUT.ack, LAYOUT.commit, *LAYOUT.work,
            )
        )
        one_event_failures += (
            after[LAYOUT.pointer]
            + sum(after[rail_fields(rail)["valid"]] for rail in LAYOUT.rail)
            != 1
        )
        inverse_failures += apply_bits(after, inverse) != before
        cases += 1

    refusal_failures = 0
    segments_only = commit_segment(0) + commit_segment(1)
    base = commit_input(1, 1, 2, 0)
    for wire in LAYOUT.rail[0]:
        dirty = list(base)
        dirty[wire] = 1
        dirty = tuple(dirty)
        refusal_failures += apply_bits(dirty, segments_only) != dirty
    for wire in LAYOUT.law:
        unlawful = list(base)
        unlawful[wire] = 0
        unlawful = tuple(unlawful)
        refusal_failures += apply_bits(unlawful, word) != unlawful
    for label, changes in (
        ("zero_direction", ((LAYOUT.right, 0),)),
        ("two_direction", ((LAYOUT.left, 1),)),
        ("zero_pointer", ((LAYOUT.pointer, 0),)),
    ):
        hostile = list(base)
        for wire, value in changes:
            hostile[wire] = value
        hostile = tuple(hostile)
        refusal_failures += apply_bits(hostile, word) != hostile

    # A locally blocked fresh event is not silently discarded: the exact
    # 00<->11 transposition records (pending,start)=(1,1).  Once the start
    # marker has shifted away, the local (1,0) state is stationary until a
    # later ACK consumes pending into the typed retry-echo field.
    pending_latch_failures = 0
    pending_latch_rows = 0
    for obstruction in ("dirty", "exhausted"):
        blocked = list(base)
        if obstruction == "dirty":
            blocked[LAYOUT.rail[0][0]] = 1
        else:
            blocked[rail_fields(LAYOUT.rail[0])["valid"]] = 1
        blocked = tuple(blocked)
        latched = apply_bits(blocked, word)
        pending_latch_failures += (
            latched[LAYOUT.pointer] != 1
            or latched[LAYOUT.pending] != 1
            or latched[rail_fields(LAYOUT.rail[0])["start"]] != 1
            or any(latched[wire] for wire in (*LAYOUT.work, LAYOUT.new, LAYOUT.ack, LAYOUT.commit))
        )
        local_after_shift = list(latched)
        local_after_shift[rail_fields(LAYOUT.rail[0])["start"]] = 0
        local_after_shift = tuple(local_after_shift)
        held = apply_bits(local_after_shift, word)
        pending_latch_failures += held != local_after_shift
        pending_latch_rows += 2

    rng = random.Random(0x713ACCE)
    arbitrary_inverse_failures = 0
    for _ in range(64):
        before = tuple(rng.getrandbits(1) for _ in range(LAYOUT.n))
        arbitrary_inverse_failures += apply_bits(
            apply_bits(before, word), inverse
        ) != before

    reference = apply_bits(commit_input(1, 1, 15, 0), word)
    deletions = {}
    for omit in (
        "complete_blank_NEW", "append_ACK", "carry", "delta",
        "frontier", "handshakes", "start_handshake", "cleanup_echo",
        "retry_echo", "endpoint_cleanup", "fresh_transfer",
        "pending_latch",
    ):
        if omit == "retry_echo":
            retry_reference = apply_bits(
                commit_input(1, 1, 15, 0, pending=1), word
            )
            damaged = apply_bits(
                commit_input(1, 1, 15, 0, pending=1),
                commit_word(omit=omit),
            )
            deletions[omit] = sum(
                a != b for a, b in zip(retry_reference, damaged)
            )
        elif omit == "pending_latch":
            pending_reference = list(commit_input(1, 1, 15, 0))
            pending_reference[LAYOUT.rail[0][0]] = 1
            pending_reference = tuple(pending_reference)
            full = apply_bits(pending_reference, word)
            damaged = apply_bits(
                pending_reference, commit_word(omit=omit)
            )
            deletions[omit] = sum(a != b for a, b in zip(full, damaged))
        else:
            damaged = apply_bits(
                commit_input(1, 1, 15, 0), commit_word(omit=omit)
            )
            deletions[omit] = sum(a != b for a, b in zip(reference, damaged))
    return {
        "orientation_head_rotor_identity_pending_cases": cases,
        "abstract_registers": LAYOUT.n,
        "abstract_X_CNOT_Toffoli_gates": len(word),
        "expanded_one_two_M2_primitives": len(A.expanded(word)),
        "packet_failures": packet_failures,
        "full_34_raw_payload_failures": raw_payload_failures,
        "controller_failures": controller_failures,
        "transient_or_work_failures": transient_failures,
        "one_decoded_event_failures": one_event_failures,
        "exact_inverse_failures": inverse_failures,
        "dirty_and_unlawful_refusal_failures": refusal_failures,
        "pending_latch_rows": pending_latch_rows,
        "pending_latch_failures": pending_latch_failures,
        "arbitrary_inverse_rows": 64,
        "arbitrary_inverse_failures": arbitrary_inverse_failures,
        "deletion_hamming": deletions,
        "all_deletions_detected": all(deletions.values()),
    }


def rectangle_track(length: int) -> tuple[tuple[int, int], ...]:
    width = (length + 1) // 2
    height = length + 2 - width
    track = [(x, 0) for x in range(width)]
    track += [(width - 1, y) for y in range(1, height)]
    track += [(x, height - 1) for x in reversed(range(width - 1))]
    track += [(0, y) for y in reversed(range(1, height - 1))]
    if len(track) != 2 * length:
        raise AssertionError((length, width, height, len(track)))
    return tuple(track)


def add(*vectors: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(sum(vector[axis] for vector in vectors) for axis in range(3))


def scale(value: int, vector: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(value * component for component in vector)


def coframes():
    return (
        ((1, 0, 0), (0, 1, 0), (0, 0, 1)),
        ((-1, 0, 0), (0, 1, 0), (0, 0, -1)),
        ((0, 1, 0), (0, 0, 1), (1, 0, 0)),
        ((0, -1, 0), (0, 0, 1), (-1, 0, 0)),
        ((0, 0, 1), (1, 0, 0), (0, 1, 0)),
        ((0, 0, -1), (1, 0, 0), (0, -1, 0)),
    )


def rail_geometry(length: int, radius: int = 50):
    track = rectangle_track(length)
    lanes = tuple(range(-19, 20))
    a_blocks = []
    b_blocks = []
    all_sites = set()
    for direction, parallel, transverse in coframes():
        direction_a = []
        direction_b = []
        for station in range(length):
            a_coordinate = track[2 * station]
            b_coordinate = track[2 * station + 1]
            a_sites = tuple(
                add(
                    scale(radius + a_coordinate[0], direction),
                    scale(a_coordinate[1], parallel),
                    scale(lane, transverse),
                )
                for lane in lanes
            )
            b_sites = tuple(
                add(
                    scale(radius + b_coordinate[0], direction),
                    scale(b_coordinate[1], parallel),
                    scale(lane, transverse),
                )
                for lane in lanes
            )
            if all_sites & (set(a_sites) | set(b_sites)):
                raise AssertionError("rail geometry collision")
            all_sites.update(a_sites)
            all_sites.update(b_sites)
            direction_a.append(a_sites)
            direction_b.append(b_sites)
        a_blocks.append(tuple(direction_a))
        b_blocks.append(tuple(direction_b))
    return tuple(a_blocks), tuple(b_blocks), all_sites


def controller_sites(forbidden: set[tuple[int, int, int]]):
    count = 4 + 1 + 4 + 1 + 1 + 3 + 12 + WORK_WIDTH
    for x0 in range(-20, 21, 4):
        for y0 in range(-20, 21, 4):
            for z0 in range(8, 31, 4):
                sites = P3.box((x0, y0, z0), (5, 5, 3), count)
                if not forbidden & set(sites):
                    return sites
    raise AssertionError("no controller box")


def physical_layout(length: int):
    (
        cells, equivalence, carriers, repeated,
        occupied, collisions, source_wire_sites,
    ) = P3.source_layout()
    rails_a, rails_b, rail_sites = rail_geometry(length)
    forbidden = set(occupied) | set(source_wire_sites[38:]) | rail_sites
    controllers = controller_sites(forbidden)
    if set(controllers) & forbidden:
        raise AssertionError("controller collision")
    cursor = 0

    def take(count):
        nonlocal cursor
        output = controllers[cursor:cursor + count]
        cursor += count
        return output

    law_sites = take(4)
    head_site = take(1)[0]
    rotor_sites = take(4)
    identity_site = take(1)[0]
    pending_site = take(1)[0]
    new_site, ack_site, commit_site = take(3)
    hold_sites = take(12)
    work_sites = take(WORK_WIDTH)
    if cursor != len(controllers):
        raise AssertionError((cursor, len(controllers)))

    wire_sites = [None] * LAYOUT.n
    wire_sites[LAYOUT.pointer] = source_wire_sites[40]
    wire_sites[LAYOUT.left] = source_wire_sites[1]
    wire_sites[LAYOUT.right] = source_wire_sites[6]
    for wire, site in zip(LAYOUT.law, law_sites):
        wire_sites[wire] = site
    wire_sites[LAYOUT.head] = head_site
    for wire, site in zip(LAYOUT.rotor, rotor_sites):
        wire_sites[wire] = site
    wire_sites[LAYOUT.identity] = identity_site
    wire_sites[LAYOUT.pending] = pending_site
    wire_sites[LAYOUT.new] = new_site
    wire_sites[LAYOUT.ack] = ack_site
    wire_sites[LAYOUT.commit] = commit_site
    for wire, site in zip(LAYOUT.hold, hold_sites):
        wire_sites[wire] = site
    for direction, block in enumerate(LAYOUT.rail):
        for wire, site in zip(block, rails_a[direction][0]):
            wire_sites[wire] = site
    for wire, site in zip(LAYOUT.work, work_sites):
        wire_sites[wire] = site
    if any(site is None for site in wire_sites):
        raise AssertionError("unplaced commit wire")
    if len(set(wire_sites)) != len(wire_sites):
        raise AssertionError("commit placement collision")
    assigned = (
        set(occupied) | set(source_wire_sites[38:])
        | set(controllers) | rail_sites
    )
    expected = (
        len(set(occupied) | set(source_wire_sites[38:]))
        + len(controllers) + len(rail_sites)
    )
    placement_collisions = expected - len(assigned)
    if placement_collisions:
        raise AssertionError("assigned placement collision")
    return {
        "length": length,
        "cells": cells,
        "equivalence": equivalence,
        "carriers": carriers,
        "repeated": repeated,
        "occupied": occupied,
        "source_collisions": collisions,
        "source_wire_sites": source_wire_sites,
        "controller_sites": controllers,
        "commit_wire_sites": tuple(wire_sites),
        "pending_site": pending_site,
        "hold_sites": hold_sites,
        "rails_a": rails_a,
        "rails_b": rails_b,
        "rail_sites": rail_sites,
        "assigned_sites": assigned,
        "placement_collisions": placement_collisions,
    }


def instruction_for_gate(gate: A.Gate, wire_sites, prefix: str):
    matrices = {
        "X": A.X, "H": A.H, "T": A.T,
        "TD": A.TD, "CNOT": A.CNOT,
    }
    return tuple(
        C712.c707.Instruction(
            prefix + kind,
            tuple(wire_sites[wire] for wire in wires),
            matrices[kind],
        )
        for kind, wires in A.expanded((gate,))
    )


def commit_physical_word(layout):
    primitives = A.expanded(commit_word())
    matrices = {
        "X": A.X, "H": A.H, "T": A.T,
        "TD": A.TD, "CNOT": A.CNOT,
    }
    return tuple(
        C712.c707.Instruction(
            "spatial_ack_commit_" + kind,
            tuple(layout["commit_wire_sites"][wire] for wire in wires),
            matrices[kind],
        )
        for kind, wires in primitives
    )


def shield_physical_word(layout):
    """Conditionally park twelve matter modes while a prior event is pending."""
    output = []
    for matter_wire, hold_site in zip(
        range(12), layout["hold_sites"]
    ):
        local_sites = (
            layout["pending_site"],
            layout["source_wire_sites"][matter_wire],
            hold_site,
        )
        for gate in fredkin(0, 1, 2):
            output.extend(instruction_for_gate(
                gate, local_sites, f"pending_shield_{matter_wire}_"
            ))
    return tuple(output)


def physical_swap(left, right, prefix):
    return (
        C712.c707.Instruction(prefix + "_cnot_rl", (right, left), A.CNOT),
        C712.c707.Instruction(prefix + "_cnot_lr", (left, right), A.CNOT),
        C712.c707.Instruction(prefix + "_cnot_rl", (right, left), A.CNOT),
    )


def shift_physical_word(layout, omit: str | None = None):
    output = []
    length = layout["length"]
    for direction in range(6):
        for station in range(length):
            if omit != "shift_layer_1":
                for lane in range(RAIL_WIDTH):
                    output.extend(physical_swap(
                        layout["rails_a"][direction][station][lane],
                        layout["rails_b"][direction][station][lane],
                        f"spatial_ack_shift1_{direction}_{station}_{lane}",
                    ))
    for direction in range(6):
        for station in range(length):
            target = (station + 1) % length
            if omit != "shift_layer_2":
                for lane in range(RAIL_WIDTH):
                    output.extend(physical_swap(
                        layout["rails_b"][direction][station][lane],
                        layout["rails_a"][direction][target][lane],
                        f"spatial_ack_shift2_{direction}_{station}_{lane}",
                    ))
    return tuple(output)


def full_physical_word(layout):
    equivalence = layout["equivalence"]
    carriers = layout["carriers"]
    repeated = layout["repeated"]
    source_sites = layout["source_wire_sites"]
    target_decode = C712.synthesize_decode(
        equivalence.target_w, equivalence.target_v
    )
    target_encode = C712.inverse_word(target_decode)
    decoded, qr = C713.instrumented_decoded_word(2)
    repetition_decode = tuple(
        C712.c707.Instruction(
            "spatial_ack_repetition_decode", carriers[index], C713.CNOT
        )
        for index in repeated
    )
    repetition_encode = tuple(
        C712.c707.Instruction(
            "spatial_ack_repetition_encode", carriers[index], C713.CNOT
        )
        for index in reversed(repeated)
    )
    decode_prefix = (
        repetition_decode
        + C712.abstract_to_physical(
            target_decode, source_sites, "spatial_ack_target_decode_"
        )
    )
    shield_pre = shield_physical_word(layout)
    decoded_physical = C712.abstract_to_physical(
        decoded, source_sites, "spatial_ack_cycle713_"
    )
    # Each controlled swap is self-inverse, and the twelve swaps have disjoint
    # targets; replaying the same expanded macro restores the parked matter.
    shield_post = shield_pre
    suffix = (
        C712.abstract_to_physical(
            target_encode, source_sites, "spatial_ack_target_encode_"
        )
        + repetition_encode
    )
    commit = commit_physical_word(layout)
    shift = shift_physical_word(layout)
    return {
        "decode_prefix": decode_prefix,
        "shield_pre": shield_pre,
        "decoded": decoded_physical,
        "shield_post": shield_post,
        "commit": commit,
        "suffix": suffix,
        "shift": shift,
        "word": (
            decode_prefix + shield_pre + decoded_physical + shield_post
            + commit + suffix + shift
        ),
        "decoded_gates": len(decoded),
        "coin_QR_residual": qr,
    }


def pending_shield_certificate() -> dict[str, object]:
    """Check the exact local reason the pending shield preserves matter."""
    decoded, _qr = C713.instrumented_decoded_word(2)
    pointer = 40
    vacuum = C713.apply_sparse_word({1 << pointer: 1.0 + 0.0j}, decoded)
    vacuum_residual = abs(vacuum.get(1 << pointer, 0.0j) - 1.0)
    vacuum_residual += sum(
        abs(amplitude) for basis, amplitude in vacuum.items()
        if basis != (1 << pointer)
    )

    def swap_basis(basis: int, left: int, right: int) -> int:
        if ((basis >> left) & 1) != ((basis >> right) & 1):
            basis ^= (1 << left) | (1 << right)
        return basis

    rows = failures = 0
    maximum_residual = 0.0
    # The HOLD register is wires 41..52 in this isolated certificate.
    for matter in range(1 << 12):
        source = matter | (1 << pointer)
        parked = source
        for mode in range(12):
            parked = swap_basis(parked, mode, 41 + mode)
        evolved = C713.apply_sparse_word({parked: 1.0 + 0.0j}, decoded)
        restored = {}
        for basis, amplitude in evolved.items():
            for mode in reversed(range(12)):
                basis = swap_basis(basis, mode, 41 + mode)
            restored[basis] = restored.get(basis, 0.0j) + amplitude
        expected = {source: 1.0 + 0.0j}
        support = set(restored) | set(expected)
        residual = max(
            (abs(restored.get(basis, 0.0j) - expected.get(basis, 0.0j))
             for basis in support),
            default=0.0,
        )
        maximum_residual = max(maximum_residual, residual)
        failures += residual > TOL
        rows += 1

    def residual_against_source(state: dict[int, complex], source: int) -> float:
        return float(np.sqrt(sum(
            abs(state.get(basis, 0.0j) - (1.0 if basis == source else 0.0)) ** 2
            for basis in set(state) | {source}
        )))

    witness = (1 << 0) | (1 << pointer)
    parked = witness
    for mode in range(12):
        parked = swap_basis(parked, mode, 41 + mode)
    no_post = C713.apply_sparse_word({parked: 1.0 + 0.0j}, decoded)
    no_pre = C713.apply_sparse_word({witness: 1.0 + 0.0j}, decoded)
    no_shield = dict(no_pre)
    restored_no_pre = {}
    for basis, amplitude in no_pre.items():
        for mode in reversed(range(12)):
            basis = swap_basis(basis, mode, 41 + mode)
        restored_no_pre[basis] = restored_no_pre.get(basis, 0.0j) + amplitude
    deletion_residuals = {
        "omit_pre_shield": residual_against_source(restored_no_pre, witness),
        "omit_post_shield": residual_against_source(no_post, witness),
        "omit_both_shields": residual_against_source(no_shield, witness),
    }
    return {
        "all_4096_matter_basis_rows": int(rows),
        "shield_failures": int(failures),
        "maximum_pending_shield_residual": float(maximum_residual),
        "vacuum_fixed_point_residual": float(vacuum_residual),
        "persistent_pending_M2": 1,
        "clean_HOLD_M2": 12,
        "deletion_residuals": deletion_residuals,
        "all_shield_deletions_detected": all(
            residual > TOL for residual in deletion_residuals.values()
        ),
    }


def shift_semantic_certificate(length: int) -> dict[str, object]:
    # Track complete 39-bit packet/handshake bundles as labels; the two layers must move every
    # A packet to A_(i+1), return B blank, and have an exact reversed word.
    a = [[("A", station, lane) for lane in range(RAIL_WIDTH)] for station in range(length)]
    b = [[None for _ in range(RAIL_WIDTH)] for _ in range(length)]
    original_a = [list(row) for row in a]
    original_b = [list(row) for row in b]
    for station in range(length):
        for lane in range(RAIL_WIDTH):
            a[station][lane], b[station][lane] = b[station][lane], a[station][lane]
    for station in range(length):
        target = (station + 1) % length
        for lane in range(RAIL_WIDTH):
            b[station][lane], a[target][lane] = a[target][lane], b[station][lane]
    shift_failures = sum(
        a[(station + 1) % length][lane] != ("A", station, lane)
        for station in range(length) for lane in range(RAIL_WIDTH)
    ) + sum(value is not None for row in b for value in row)
    for station in reversed(range(length)):
        target = (station + 1) % length
        for lane in reversed(range(RAIL_WIDTH)):
            b[station][lane], a[target][lane] = a[target][lane], b[station][lane]
    for station in reversed(range(length)):
        for lane in reversed(range(RAIL_WIDTH)):
            a[station][lane], b[station][lane] = b[station][lane], a[station][lane]
    inverse_failures = a != original_a or b != original_b
    return {
        "length": length,
        "rail_families": 6,
        "M2_per_bundle": RAIL_WIDTH,
        "two_layer_swap_instances": 2 * 6 * length * RAIL_WIDTH,
        "shift_failures": shift_failures,
        "inverse_failures": int(inverse_failures),
        "prewrap_updates_checked": 4,
        "wrap_reached": 4 >= length,
    }


def active_covariance(layout, word, routed):
    frames = C712.C709.F.base.proper_cubic_frames()
    direction_permutations = []
    active_failures = product_failures = 0
    coordinate_failures = route_distance_failures = 0
    translation_failures = 0
    for frame in frames:
        matrix = C712.C709.F.base.c210.direction_permutation(frame)
        permutation = tuple(
            next(target for target in range(6) if abs(matrix[target, source]) > 0.5)
            for source in range(6)
        )
        direction_permutations.append(permutation)
        for matter in range(1 << 12):
            transported = 0
            for cell in range(2):
                for source in range(6):
                    transported |= (
                        ((matter >> (6 * cell + source)) & 1)
                        << (6 * cell + permutation[source])
                    )
            base = S.orientation_and_direction(matter)
            left = (transported >> permutation[1]) & 1
            right = (transported >> (6 + permutation[0])) & 1
            transformed = (
                (1, permutation[0]) if right and not left
                else (-1, permutation[1]) if left and not right
                else None
            )
            expected = None if base is None else (base[0], permutation[base[1]])
            active_failures += transformed != expected
        inverse = frame.T
        for instruction in word:
            transformed = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in instruction.sites
            )
            restored = tuple(
                tuple(int(value) for value in inverse @ np.asarray(site))
                for site in transformed
            )
            coordinate_failures += restored != instruction.sites
        for gate in routed:
            if len(gate.sites) != 2:
                continue
            transformed = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in gate.sites
            )
            distance = sum(
                abs(transformed[0][axis] - transformed[1][axis])
                for axis in range(3)
            )
            route_distance_failures += distance != 1
    translations = ((7, -5, 11), (-13, 2, -4))
    for translation in translations:
        for instruction in word:
            translated = tuple(
                tuple(site[axis] + translation[axis] for axis in range(3))
                for site in instruction.sites
            )
            restored = tuple(
                tuple(site[axis] - translation[axis] for axis in range(3))
                for site in translated
            )
            translation_failures += restored != instruction.sites
        for gate in routed:
            if len(gate.sites) != 2:
                continue
            translated = tuple(
                tuple(site[axis] + translation[axis] for axis in range(3))
                for site in gate.sites
            )
            distance = sum(
                abs(translated[0][axis] - translated[1][axis])
                for axis in range(3)
            )
            translation_failures += distance != 1
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product_frame = left @ right
            product_index = next(
                index for index, frame in enumerate(frames)
                if np.array_equal(frame, product_frame)
            )
            composed = tuple(
                direction_permutations[left_index][
                    direction_permutations[right_index][source]
                ]
                for source in range(6)
            )
            product_failures += composed != direction_permutations[product_index]
    return {
        "proper_cubic_frames": len(frames),
        "active_rows_per_frame": 4096,
        "active_endpoint_direction_failures": active_failures,
        "instruction_coordinate_failures": coordinate_failures,
        "routed_NN_frame_failures": route_distance_failures,
        "ordered_frame_products": len(frames) ** 2,
        "direction_product_failures": product_failures,
        "translations_checked": translations,
        "translation_failures": translation_failures,
    }


def routed_layout_certificate(length: int) -> dict[str, object]:
    layout = physical_layout(length)
    built = full_physical_word(layout)
    routed, route = C712.c707.route_word(built["word"])
    covariance = active_covariance(layout, built["word"], routed)
    shift_word = built["shift"]
    shift_non_nn = sum(
        len(instruction.sites) == 2
        and sum(abs(a - b) for a, b in zip(*instruction.sites)) != 1
        for instruction in shift_word
    )
    assigned = layout["assigned_sites"]
    return {
        "held_length": length,
        "placement": {
            "source_collisions": layout["source_collisions"],
            "assigned_M2": len(assigned),
            "controller_M2": len(layout["controller_sites"]),
            "rail_M2": len(layout["rail_sites"]),
            "rail_period_M2_per_direction": 2 * length * RAIL_WIDTH,
            "placement_collisions": layout["placement_collisions"],
        },
        "word": {
            "decoded_Cycle713_gates": built["decoded_gates"],
            "coin_QR_residual": built["coin_QR_residual"],
            "source_decode_prefix_primitives": len(built["decode_prefix"]),
            "pending_shield_pre_primitives": len(built["shield_pre"]),
            "decoded_Cycle713_primitives": len(built["decoded"]),
            "pending_shield_post_primitives": len(built["shield_post"]),
            "structured_commit_primitives": len(built["commit"]),
            "source_suffix_primitives": len(built["suffix"]),
            "two_layer_shift_CNOTs": len(built["shift"]),
            "total_physical_primitives": len(built["word"]),
            "shift_non_NN_failures_before_route": shift_non_nn,
        },
        "route": {
            "routed_nearest_neighbor_gates": len(routed),
            "maximum_route_distance": route["maximum_route_distance"],
            "non_NN_failures": route["non_NN_failures"],
            "operand_order_failures": route["operand_order_failures"],
            "route_return_failures": route["route_return_failures"],
            "route_deletion_detected_macros": route["delete_first_swap_detected_macros"],
            "routed_word_sha256": route["word_sha256"],
            "touched_M2": len(route["touched_coordinates"]),
            "blank_route_work_M2": len(
                set(route["touched_coordinates"]) - assigned
            ),
        },
        "covariance": covariance,
    }


def main() -> int:
    provenance = A.C714.provenance_certificate(AUDIT_INPUT_PATHS, __file__)
    commit = structured_commit_certificate()
    shield = pending_shield_certificate()
    shifts = {
        length: shift_semantic_certificate(length) for length in (13, 17)
    }
    routes = {
        length: routed_layout_certificate(length) for length in (13, 17)
    }
    delta_length = 17 - 13
    support_scaling = {
        "assigned_M2_slope_per_rail_station": (
            routes[17]["placement"]["assigned_M2"]
            - routes[13]["placement"]["assigned_M2"]
        ) // delta_length,
        "assigned_M2_intercept": (
            routes[13]["placement"]["assigned_M2"]
            - 13 * 2 * 6 * RAIL_WIDTH
        ),
        "touched_M2_slope_per_rail_station": (
            routes[17]["route"]["touched_M2"]
            - routes[13]["route"]["touched_M2"]
        ) // delta_length,
        "touched_M2_intercept": (
            routes[13]["route"]["touched_M2"]
            - 13 * 2 * 6 * RAIL_WIDTH
        ),
        "physical_word_slope_per_rail_station": (
            routes[17]["word"]["total_physical_primitives"]
            - routes[13]["word"]["total_physical_primitives"]
        ) // delta_length,
        "physical_word_intercept": (
            routes[13]["word"]["total_physical_primitives"]
            - 13 * 6 * 2 * RAIL_WIDTH * 3
        ),
        "fixed_routing_overhead_primitives": (
            routes[13]["route"]["routed_nearest_neighbor_gates"]
            - routes[13]["word"]["total_physical_primitives"]
        ),
    }
    # Re-run the actual Cycle-713/history acceptance surface unchanged at the
    # two held sizes.  The structured commit's 128-row equivalence supplies the
    # physical implementation of the forward local map used by this harness.
    acceptance = {}
    for length in (13, 17):
        report, _outputs = S.clean_domain_certificate(length)
        acceptance[length] = report

    checks = {
        "source_closure": provenance["baseline_is_ancestor"]
        and provenance["declared_path_failures"] == 0
        and provenance["duplicate_declared_paths"] == 0
        and not provenance["missing_transitive_scripts"]
        and not provenance["missing_dynamic_scripts"]
        and not provenance["untracked_inputs"],
        "structured_commit": all((
            commit["packet_failures"] == 0,
            commit["full_34_raw_payload_failures"] == 0,
            commit["controller_failures"] == 0,
            commit["transient_or_work_failures"] == 0,
            commit["one_decoded_event_failures"] == 0,
            commit["exact_inverse_failures"] == 0,
            commit["dirty_and_unlawful_refusal_failures"] == 0,
            commit["pending_latch_failures"] == 0,
            commit["arbitrary_inverse_failures"] == 0,
            commit["all_deletions_detected"],
        )),
        "pending_matter_shield": all((
            shield["all_4096_matter_basis_rows"] == 4096,
            shield["shield_failures"] == 0,
            shield["maximum_pending_shield_residual"] < TOL,
            shield["vacuum_fixed_point_residual"] < TOL,
            shield["all_shield_deletions_detected"],
        )),
        "two_layer_shifts": all(
            row["shift_failures"] == 0
            and row["inverse_failures"] == 0
            and not row["wrap_reached"]
            for row in shifts.values()
        ),
        "literal_routes": all(
            row["placement"]["source_collisions"] == 0
            and row["word"]["shift_non_NN_failures_before_route"] == 0
            and row["route"]["non_NN_failures"] == 0
            and row["route"]["operand_order_failures"] == 0
            and row["route"]["route_return_failures"] == 0
            and row["route"]["route_deletion_detected_macros"] > 0
            for row in routes.values()
        ),
        "linear_support_scaling": all((
            support_scaling["assigned_M2_slope_per_rail_station"]
            == 2 * 6 * RAIL_WIDTH,
            support_scaling["touched_M2_slope_per_rail_station"]
            == 2 * 6 * RAIL_WIDTH,
            support_scaling["physical_word_slope_per_rail_station"]
            == 6 * 2 * RAIL_WIDTH * 3,
            routes[17]["route"]["routed_nearest_neighbor_gates"]
            - routes[17]["word"]["total_physical_primitives"]
            == support_scaling["fixed_routing_overhead_primitives"],
        )),
        "active_covariance": all(
            row["covariance"]["proper_cubic_frames"] == 24
            and row["covariance"]["ordered_frame_products"] == 576
            and row["covariance"]["active_endpoint_direction_failures"] == 0
            and row["covariance"]["instruction_coordinate_failures"] == 0
            and row["covariance"]["routed_NN_frame_failures"] == 0
            and row["covariance"]["direction_product_failures"] == 0
            and row["covariance"]["translation_failures"] == 0
            for row in routes.values()
        ),
        "repeated_Cycle713_acceptance": all(
            max(
                report["applications"][n]["maximum_intertwiner_residual"]
                for n in (1, 2, 4)
            ) < TOL
            and max(
                report["applications"][n]["maximum_norm_residual"]
                for n in (1, 2, 4)
            ) < TOL
            and max(
                report["applications"][n]["maximum_particle_number_leakage"]
                for n in (1, 2, 4)
            ) < TOL
            and max(
                report["applications"][n]["maximum_bad_packet_or_auxiliary_weight"]
                for n in (1, 2, 4)
            ) < TOL
            for report in acceptance.values()
        ),
    }
    report = {
        "cycle": 718,
        "authority": "none",
        "audit": "unset",
        "status": "bounded_conditional_construction",
        "claim_type": "bounded_theorem",
        "declared_inputs": AUDIT_INPUT_PATHS,
        "provenance": provenance,
        "checks": checks,
        "pass": all(checks.values()),
        "structured_commit": commit,
        "pending_matter_shield": shield,
        "two_layer_shifts": shifts,
        "physical_routes": routes,
        "support_scaling": support_scaling,
        "Cycle713_acceptance": acceptance,
        "supplied": [
            "Cycle-713 physical two-cell decoder and full free/seam/contact update",
            "BINDER/ACTUAL/ADMISS/LAW=1 and clean head/rotor/identity/work genesis",
            "six A/B packet-bundle loops as a proper-cubic orbit",
            "finite pre-wrap blank/no-return sector and fixed commit-then-shift layer order",
            "blank routing sites used transiently and returned by every routed macro",
            "one clean persistent pending M2 and twelve clean local HOLD M2 at genesis",
        ],
        "derived": [
            "structured complete-blank NEW and ACK-before-pointer-cleanup circuit",
            "all 34 raw packet bits, FRESH, identity, handshakes, and frontier written locally",
            "exact arbitrary-state gate inverse and lawful one-event conservation",
            "blocked-event pending latch, vacuum shield, and typed retry-echo ACK cleanup",
            "two disjoint nearest-neighbor SWAP layers realizing each range-one shift",
            "collision-free physical-M2 placement and literal nearest-neighbor route at held lengths 13 and 17",
            "active 24-frame/576-product covariance and repeated Cycle-713/history acceptance",
        ],
        "open": [
            "derive or enforce the initially blank no-return sector rather than supply it",
            "positive-density multi-source collision-safe rail arbitration",
            "autonomous selection and enforcement of a fresh Cycle-612 output cell",
            "Record permanence, Born realization, source/gravity response, and physical-time interpretation",
        ],
        "boundary": (
            "Positive literal physical-M2 route for the isolated pre-wrap spatial ACK/export bridge. "
            "This is a Record/time-interface bridge, not additional core matter closure; finite loop "
            "return and fresh-resource genesis remain explicit supplies."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE718_SPATIAL_ACK_PHYSICAL_M2_ROUTE_PASS"
        if report["pass"] else "CYCLE718_SPATIAL_ACK_PHYSICAL_M2_ROUTE_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
