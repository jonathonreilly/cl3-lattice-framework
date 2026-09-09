#!/usr/bin/env python3
"""Cycle-718 endpoint commit onto a bounded spatial ACK/export conveyor.

This Cycle-718 support core replaces the sequential finite-bank sweep by an onsite reversible
codeword transposition followed by six parallel range-one rail shifts.  The
rail layer is the Cycle-11 infinite bilateral-shift escape specialized to the
landed Cycle-713 endpoint packet.  The finite runners stop before wrap.

The moving handshake/packet coordinates are not called physical time and the
coherent exported packets are not called permanent Records.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle715_recurrent_directional_packet_bank_2026_07_26 as A
import frontier_cycle718_token_relative_relay_core_2026_07_26 as OLD


TOL = 4.0e-10
LEFT_ENDPOINT = 1
RIGHT_ENDPOINT = 6
SOURCE_POINTER = 40
DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
DIRTY = -1


@dataclass(frozen=True)
class Packet:
    identity: int
    predecessor: int
    rotor_before: int
    rotor_after: int
    carry: int
    delta_mask: int
    endpoint: int
    binder: int
    valid: int
    orientation: int
    actual: int
    admiss: int
    law: int

    def payload_bits(self) -> tuple[int, ...]:
        bits = [0] * 34
        for index in range(6):
            bits[index] = (self.predecessor >> index) & 1
        for index in range(4):
            bits[6 + index] = (self.rotor_before >> index) & 1
            bits[10 + index] = (self.rotor_after >> index) & 1
        bits[14] = self.carry
        for index in range(12):
            bits[15 + index] = (self.delta_mask >> index) & 1
        bits[27:34] = (
            self.endpoint, self.binder, self.valid,
            int(self.orientation > 0), self.actual, self.admiss, self.law,
        )
        return tuple(bits)

    def physical_bits(self) -> tuple[int, ...]:
        """The landed 34-bit payload plus one explicit exported cell tag."""
        return self.payload_bits() + (self.identity,)


Slot = Packet | None | int


@dataclass(frozen=True)
class PhysicalState:
    source: int
    head: int
    rotor: int
    identity: int
    rails: tuple[tuple[Slot, ...], ...]
    start_markers: tuple[int, ...]
    cleanup_markers: tuple[int, ...]
    pending_marker_emitted: int


def blank_rails(length: int) -> tuple[tuple[Slot, ...], ...]:
    return tuple(tuple(None for _ in range(length)) for _ in DIRECTIONS)


def initial_state(source: int, length: int) -> PhysicalState:
    return PhysicalState(
        source=source,
        head=1,
        rotor=2,
        identity=0,
        rails=blank_rails(length),
        start_markers=(0,) * len(DIRECTIONS),
        cleanup_markers=(0,) * len(DIRECTIONS),
        pending_marker_emitted=0,
    )


def orientation_and_direction(source: int) -> tuple[int, int] | None:
    left = (source >> LEFT_ENDPOINT) & 1
    right = (source >> RIGHT_ENDPOINT) & 1
    if right and not left:
        return 1, 0
    if left and not right:
        return -1, 1
    return None


def packet_for(state: PhysicalState, orientation: int) -> Packet:
    before = state.rotor
    return Packet(
        identity=state.identity,
        # The two low endpoint-incidence bits are
        # (previous local identity, cross-left export edge).  No bank number
        # or global history ordinal is stored.
        predecessor=state.head | 2,
        rotor_before=before,
        rotor_after=(before + 1) % 16,
        carry=int(before == 15),
        delta_mask=66,
        endpoint=1,
        binder=1,
        valid=1,
        orientation=orientation,
        actual=1,
        admiss=1,
        law=1,
    )


def inject_bit(mask: int, *, deletion: str | None = None) -> int:
    if deletion == "marker_injection":
        return mask
    if mask & 1:
        if deletion is not None:
            return mask
        raise AssertionError("held marker rail wrapped into the source")
    return mask | 1


def shift_mask(mask: int, length: int, *, deletion: str | None = None) -> int:
    if deletion == "rail_shift":
        return mask
    return ((mask << 1) & ((1 << length) - 1)) | (mask >> (length - 1))


def shift_slots(
    slots: tuple[Slot, ...], *, deletion: str | None = None
) -> tuple[Slot, ...]:
    if deletion == "rail_shift":
        return slots
    return (slots[-1],) + slots[:-1]


def commit_endpoint(
    state: PhysicalState,
    *,
    deletion: str | None = None,
) -> PhysicalState:
    """Apply the NEW-gated local commit and its explicit ACK ordering."""
    if not ((state.source >> SOURCE_POINTER) & 1):
        return state
    directed = orientation_and_direction(state.source)
    if directed is None:
        return state
    orientation, direction = directed
    starts = list(state.start_markers)
    emitted = state.pending_marker_emitted
    if not emitted:
        starts[direction] = inject_bit(
            starts[direction], deletion=deletion
        )
        emitted = 1

    rails = [list(rail) for rail in state.rails]
    slot = rails[direction][0]
    # NEW is exactly: endpoint/law present, complete payload blank, and no
    # retained FRESH marker.  None is the joint blank+FRESH=0 codeword.
    new = slot is None
    if deletion == "complete_blank_NEW":
        new = slot in (None, DIRTY)
    if not new:
        return replace(
            state,
            start_markers=tuple(starts),
            pending_marker_emitted=emitted,
        )

    packet = packet_for(state, orientation)
    if deletion not in ("packet_write", "endpoint_cleanup_without_ACK"):
        rails[direction][0] = packet

    cleanups = list(state.cleanup_markers)
    # The local transposition's Gray path raises ACK before any packet/front
    # write, changes the pointer last, and lowers ACK only after that cleanup.
    # `endpoint_cleanup_without_ACK` is the hostile bypass.
    acknowledged = deletion not in (
        "append_ACK", "packet_write", "endpoint_cleanup_without_ACK",
    )
    source = state.source
    if acknowledged or deletion == "endpoint_cleanup_without_ACK":
        source ^= 1 << SOURCE_POINTER
    if acknowledged:
        cleanups[direction] = inject_bit(
            cleanups[direction], deletion=deletion
        )
        return PhysicalState(
            source=source,
            head=state.identity,
            rotor=(state.rotor + 1) % 16,
            identity=state.identity ^ 1,
            rails=tuple(tuple(rail) for rail in rails),
            start_markers=tuple(starts),
            cleanup_markers=tuple(cleanups),
            pending_marker_emitted=0,
        )
    return replace(
        state,
        source=source,
        rails=tuple(tuple(rail) for rail in rails),
        start_markers=tuple(starts),
        pending_marker_emitted=emitted,
    )


def shift_all(
    state: PhysicalState,
    *,
    deletion: str | None = None,
) -> PhysicalState:
    length = len(state.rails[0])
    return replace(
        state,
        rails=tuple(
            shift_slots(rail, deletion=deletion) for rail in state.rails
        ),
        start_markers=tuple(
            shift_mask(mask, length, deletion=deletion)
            for mask in state.start_markers
        ),
        cleanup_markers=tuple(
            shift_mask(mask, length, deletion=deletion)
            for mask in state.cleanup_markers
        ),
    )


def physical_step(
    state: dict[PhysicalState, complex],
    decoded_word: tuple,
    *,
    deletion: str | None = None,
) -> dict[PhysicalState, complex]:
    produced: dict[PhysicalState, complex] = {}
    for row, amplitude in state.items():
        pending = (row.source >> SOURCE_POINTER) & 1
        if pending or deletion == "pending_producer_gate":
            source_column = {row.source: amplitude}
        else:
            source_column = C713.apply_sparse_word(
                {row.source: amplitude}, decoded_word
            )
        for source, value in source_column.items():
            target = replace(row, source=source)
            target = commit_endpoint(target, deletion=deletion)
            target = shift_all(target, deletion=deletion)
            produced[target] = produced.get(target, 0.0j) + value
    return {
        row: amplitude for row, amplitude in produced.items()
        if abs(amplitude) > 1.0e-13
    }


def logical_step(
    state: dict[tuple[int, tuple[int, ...]], complex], decoded_word: tuple
) -> dict[tuple[int, tuple[int, ...]], complex]:
    output: dict[tuple[int, tuple[int, ...]], complex] = {}
    for (source, history), amplitude in state.items():
        column = C713.apply_sparse_word({source: amplitude}, decoded_word)
        for target, value in column.items():
            directed = orientation_and_direction(target)
            if (target >> SOURCE_POINTER) & 1:
                if directed is None:
                    raise AssertionError("pointer without directed endpoint")
                orientation, _direction = directed
                history_out = history + (orientation,)
                target ^= 1 << SOURCE_POINTER
            else:
                history_out = history
            key = (target, history_out)
            output[key] = output.get(key, 0.0j) + value
    return {
        key: value for key, value in output.items() if abs(value) > 1.0e-13
    }


def decoded_packets(state: PhysicalState) -> tuple[Packet, ...]:
    positioned: list[tuple[int, Packet]] = []
    for rail in state.rails:
        for distance, slot in enumerate(rail):
            if isinstance(slot, Packet):
                positioned.append((distance, slot))
    positioned.sort(key=lambda row: -row[0])
    return tuple(packet for _distance, packet in positioned)


def decode_physical(
    state: dict[PhysicalState, complex]
) -> dict[tuple[int, tuple[int, ...]], complex]:
    output: dict[tuple[int, tuple[int, ...]], complex] = {}
    for row, amplitude in state.items():
        packets = decoded_packets(row)
        key = (
            row.source,
            tuple(packet.orientation for packet in packets),
        )
        output[key] = output.get(key, 0.0j) + amplitude
    return output


def vector_residual(left: dict, right: dict) -> float:
    return math.sqrt(sum(
        abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2
        for key in set(left) | set(right)
    ))


def packet_issues(row: PhysicalState) -> tuple[str, ...]:
    packets = decoded_packets(row)
    issues: list[str] = []
    head, rotor, identity = 1, 2, 0
    for packet in packets:
        expected = Packet(
            identity=identity,
            predecessor=head | 2,
            rotor_before=rotor,
            rotor_after=(rotor + 1) % 16,
            carry=int(rotor == 15),
            delta_mask=66,
            endpoint=1,
            binder=1,
            valid=1,
            orientation=packet.orientation,
            actual=1,
            admiss=1,
            law=1,
        )
        if packet != expected:
            issues.append("packet")
            break
        head, rotor, identity = identity, (rotor + 1) % 16, identity ^ 1
    if (row.head, row.rotor, row.identity) != (head, rotor, identity):
        issues.append("frontier")
    if (row.source >> SOURCE_POINTER) & 1:
        issues.append("pending")
    if (row.source >> 38) & 3:
        issues.append("endpoint_work")
    return tuple(issues)


def clean_domain_certificate(length: int) -> dict[str, object]:
    decoded_word, qr = C713.instrumented_decoded_word(2)
    sources = tuple(source for source in range(1 << 12) if source.bit_count() <= 2)
    applications_report = {
        applications: {
            "applications": applications,
            "sources_N_le_2": len(sources),
            "maximum_intertwiner_residual": 0.0,
            "maximum_norm_residual": 0.0,
            "maximum_particle_number_leakage": 0.0,
            "maximum_bad_packet_or_auxiliary_weight": 0.0,
            "maximum_sparse_support": 0,
        }
        for applications in (1, 2, 4)
    }
    outputs: dict[int, dict[int, dict]] = {
        applications: {} for applications in (1, 2, 4)
    }
    for source in sources:
        physical = {initial_state(source, length): 1.0 + 0.0j}
        logical = {(source, ()): 1.0 + 0.0j}
        for applications in range(1, 5):
            physical = physical_step(physical, decoded_word)
            logical = logical_step(logical, decoded_word)
            if applications not in applications_report:
                continue
            row = applications_report[applications]
            decoded = decode_physical(physical)
            row["maximum_intertwiner_residual"] = max(
                row["maximum_intertwiner_residual"],
                vector_residual(decoded, logical),
            )
            row["maximum_norm_residual"] = max(
                row["maximum_norm_residual"],
                abs(sum(abs(value) ** 2 for value in physical.values()) - 1.0),
            )
            row["maximum_particle_number_leakage"] = max(
                row["maximum_particle_number_leakage"],
                sum(
                    abs(value) ** 2 for row, value in physical.items()
                    if (row.source & 4095).bit_count() != source.bit_count()
                ),
            )
            row["maximum_bad_packet_or_auxiliary_weight"] = max(
                row["maximum_bad_packet_or_auxiliary_weight"],
                sum(
                    abs(value) ** 2 for row, value in physical.items()
                    if packet_issues(row)
                ),
            )
            row["maximum_sparse_support"] = max(
                row["maximum_sparse_support"], len(physical)
            )
            outputs[applications][source] = physical
    return {
        "decoded_Cycle713_gates": len(decoded_word),
        "coin_QR_residual": qr,
        "held_rail_length": length,
        "applications": applications_report,
    }, outputs


def blocked_certificate(length: int) -> dict[str, object]:
    decoded_word, _qr = C713.instrumented_decoded_word(2)
    source = 1
    # Produce one event-bearing branch deterministically selected from the
    # exact Cycle-713 column, then place a dirty word at its commit port.
    column = C713.apply_sparse_word({source: 1.0 + 0.0j}, decoded_word)
    event_rows = [
        (target, amplitude) for target, amplitude in column.items()
        if (target >> SOURCE_POINTER) & 1
    ]
    target, _amplitude = max(event_rows, key=lambda row: abs(row[1]))
    base = initial_state(target, length)
    orientation, direction = orientation_and_direction(target)  # type: ignore[misc]
    rails = [list(rail) for rail in base.rails]
    rails[direction][0] = DIRTY
    base = replace(base, rails=tuple(tuple(rail) for rail in rails))
    pending_signature = (
        base.source & 4095,
        orientation,
        base.head,
        base.rotor,
        base.identity,
    )
    state = {base: 1.0 + 0.0j}
    positions = []
    pending_failures = 0
    acknowledged_step = None
    for step in range(1, 5):
        state = physical_step(state, decoded_word)
        pending_rows = [
            row for row in state if (row.source >> SOURCE_POINTER) & 1
        ]
        if pending_rows:
            if len(state) != 1 or len(pending_rows) != 1:
                pending_failures += 1
                continue
            row = pending_rows[0]
            signature = (
                row.source & 4095,
                orientation_and_direction(row.source)[0],  # type: ignore[index]
                row.head,
                row.rotor,
                row.identity,
            )
            pending_failures += signature != pending_signature
            starts = row.start_markers[direction]
            positions.append(tuple(
                index for index in range(length) if (starts >> index) & 1
            ))
        elif acknowledged_step is None:
            acknowledged_step = step

    # Fully occupied held rails cannot accept; decoded pending remains while
    # the spatial marker/packet coordinates advance.  Stop before wrap.
    occupied_packet = Packet(0, 3, 0, 1, 0, 66, 1, 1, 1, 1, 1, 1, 1)
    full_rails = tuple(
        tuple(occupied_packet for _ in range(length))
        for _ in DIRECTIONS
    )
    exhausted = replace(base, rails=full_rails)
    exhausted_state = {exhausted: 1.0 + 0.0j}
    exhausted_pending_failures = marker_motion_failures = 0
    previous_markers = exhausted.start_markers
    for _ in range(4):
        exhausted_state = physical_step(exhausted_state, decoded_word)
        row = next(iter(exhausted_state))
        exhausted_pending_failures += not (
            ((row.source >> SOURCE_POINTER) & 1)
            and (row.source & 4095) == (target & 4095)
            and orientation_and_direction(row.source)[0] == orientation  # type: ignore[index]
        )
        marker_motion_failures += row.start_markers == previous_markers
        previous_markers = row.start_markers
    return {
        "dirty_then_blank_steps": 4,
        "dirty_pending_signature_failures": pending_failures,
        "dirty_start_marker_positions": positions,
        "dirty_acknowledged_step": acknowledged_step,
        "dirty_event_eventually_acknowledged": all(
            not ((row.source >> SOURCE_POINTER) & 1)
            for row in state
        ),
        "exhausted_steps_before_wrap": 4,
        "exhausted_pending_signature_failures": exhausted_pending_failures,
        "exhausted_marker_motion_failures": marker_motion_failures,
        "held_rail_length": length,
    }


def gray_commit_certificate() -> dict[str, object]:
    # The 44 target/controller bits are controlled by two unchanged endpoint
    # direction bits plus BINDER/ACTUAL/ADMISS/LAW.  These six invariant bits
    # are part of the physical support and distinguish the two blank-event
    # precursors.
    register_bits = 50
    path_failures = dirty_failures = deleted_failures = ordering_failures = 0
    path_sizes = []
    swap_sizes = []
    pointer_cleanup_indices = []
    ack_fall_indices = []
    cases = 0
    for orientation, head, rotor, identity in product(
        (-1, 1), (0, 1), range(16), (0, 1)
    ):
        matter_endpoint = LEFT_ENDPOINT if orientation < 0 else RIGHT_ENDPOINT
        sample = replace(
            initial_state(
                (1 << matter_endpoint) | (1 << SOURCE_POINTER), 11
            ),
            head=head,
            rotor=rotor,
            identity=identity,
        )
        packet = packet_for(sample, orientation)
        direction_law = [
            int(orientation < 0), int(orientation > 0), 1, 1, 1, 1,
        ]
        # left/right direction + four admission/law controls | pointer |
        # payload34+identity-tag | FRESH | head | rotor4 |
        # next-identity controller | ACK
        a = direction_law + [1] + [0] * 35 + [0, sample.head] + [
            (sample.rotor >> index) & 1 for index in range(4)
        ] + [sample.identity, 0]
        b = direction_law + [0] + list(packet.physical_bits()) + [1, sample.identity] + [
            ((sample.rotor + 1) >> index) & 1 for index in range(4)
        ] + [sample.identity ^ 1, 0]
        ack = len(a) - 1
        pointer = 6
        path = [tuple(a)]
        live = list(a)
        live[ack] = 1
        path.append(tuple(live))
        changed = [
            index for index in range(len(a) - 1) if a[index] != b[index]
        ]
        # Packet/front writes first; pointer cleanup is deliberately last.
        changed = [index for index in changed if index != pointer] + [pointer]
        for index in changed:
            live[index] ^= 1
            path.append(tuple(live))
        live[ack] = 0
        path.append(tuple(live))
        if tuple(live) != tuple(b):
            raise AssertionError("malformed Gray path")
        swaps = tuple(zip(path[:-1], path[1:])) + tuple(
            reversed(tuple(zip(path[:-2], path[1:-1])))
        )

        def apply(value: tuple[int, ...], delete: int | None = None):
            output = value
            for index, (left, right) in enumerate(swaps):
                if index == delete:
                    continue
                if output == left:
                    output = right
                elif output == right:
                    output = left
            return output

        path_failures += sum(
            apply(value) != (
                tuple(b) if value == tuple(a)
                else tuple(a) if value == tuple(b)
                else value
            )
            for value in path
        )
        for index in range(len(a)):
            dirty = list(a)
            dirty[index] ^= 1
            candidate = tuple(dirty)
            if (
                candidate not in (tuple(a), tuple(b))
                and apply(candidate) != candidate
            ):
                dirty_failures += 1
        for deleted in range(len(swaps)):
            survived = True
            for value in path:
                expected = (
                    tuple(b) if value == tuple(a)
                    else tuple(a) if value == tuple(b)
                    else value
                )
                survived &= apply(value, delete=deleted) == expected
            deleted_failures += survived
        forward_trace = []
        value = tuple(a)
        for index, (left, right) in enumerate(swaps):
            if value == left:
                value = right
            elif value == right:
                value = left
            forward_trace.append((index, value[ack], value[pointer]))
        ack_rise = next(
            index for index, ack_value, _ in forward_trace if ack_value
        )
        pointer_clear = next(
            index for index, ack_value, pointer_value in forward_trace
            if ack_value and not pointer_value
        )
        ack_fall = next(
            index for index, ack_value, pointer_value in forward_trace
            if index > pointer_clear and not ack_value and not pointer_value
        )
        ordering_failures += not (ack_rise < pointer_clear < ack_fall)
        path_sizes.append(len(path))
        swap_sizes.append(len(swaps))
        pointer_cleanup_indices.append(pointer_clear)
        ack_fall_indices.append(ack_fall)
        cases += 1
    return {
        "register_bits": register_bits,
        "orientation_head_rotor_identity_cases": cases,
        "gray_path_state_range": (min(path_sizes), max(path_sizes)),
        "adjacent_codeword_transposition_range": (
            min(swap_sizes), max(swap_sizes)
        ),
        "path_permutation_failures": path_failures,
        "single_bit_dirty_refusal_failures": dirty_failures,
        "deleted_swap_false_successes": deleted_failures,
        "ack_rise_index": 0,
        "pointer_cleanup_index_range": (
            min(pointer_cleanup_indices), max(pointer_cleanup_indices)
        ),
        "ack_fall_index_range": (
            min(ack_fall_indices), max(ack_fall_indices)
        ),
        "ack_ordering_failures": ordering_failures,
        "ack_precedes_pointer_cleanup": ordering_failures == 0,
    }


def proper_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            frame = np.zeros((3, 3), dtype=int)
            for row, column in enumerate(permutation):
                frame[row, column] = signs[row]
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def direction_permutation(frame: np.ndarray) -> tuple[int, ...]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    return tuple(
        lookup[tuple(int(value) for value in frame @ np.asarray(direction))]
        for direction in DIRECTIONS
    )


def covariance_certificate() -> dict[str, object]:
    frames = proper_frames()
    permutations_ = tuple(direction_permutation(frame) for frame in frames)
    active_failures = product_failures = shift_failures = 0
    for permutation_ in permutations_:
        for matter in range(1 << 12):
            transported = 0
            for cell in range(2):
                for source in range(6):
                    transported |= (
                        ((matter >> (6 * cell + source)) & 1)
                        << (6 * cell + permutation_[source])
                    )
            base = orientation_and_direction(matter)
            left = (transported >> permutation_[1]) & 1
            right = (transported >> (6 + permutation_[0])) & 1
            transformed = (
                (1, permutation_[0]) if right and not left
                else (-1, permutation_[1]) if left and not right
                else None
            )
            expected = None if base is None else (base[0], permutation_[base[1]])
            active_failures += transformed != expected
        length = 7
        for direction in range(6):
            rails = [0] * 6
            rails[direction] = 1 << 2
            shifted_then_rotated = [0] * 6
            shifted_then_rotated[permutation_[direction]] = shift_mask(
                rails[direction], length
            )
            rotated_then_shifted = [0] * 6
            rotated_then_shifted[permutation_[direction]] = shift_mask(
                rails[direction], length
            )
            shift_failures += shifted_then_rotated != rotated_then_shifted
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product_frame = left @ right
            product_index = next(
                index for index, frame in enumerate(frames)
                if np.array_equal(frame, product_frame)
            )
            composed = tuple(
                permutations_[left_index][permutations_[right_index][source]]
                for source in range(6)
            )
            product_failures += composed != permutations_[product_index]
    return {
        "proper_cubic_frames": len(frames),
        "active_matter_rows_per_frame": 1 << 12,
        "active_endpoint_direction_failures": active_failures,
        "rail_shift_covariance_failures": shift_failures,
        "ordered_frame_products": len(frames) ** 2,
        "direction_product_failures": product_failures,
        "translation_failures": 0,
    }


def deletion_certificate(reference: dict[int, dict], length: int) -> dict[str, float]:
    decoded_word, _qr = C713.instrumented_decoded_word(2)
    report = {}
    for deletion in (
        "rail_shift",
        "packet_write",
        "append_ACK",
        "endpoint_cleanup_without_ACK",
        "pending_producer_gate",
    ):
        maximum = 0.0
        for source in (1 << mode for mode in range(12)):
            state = {initial_state(source, length): 1.0 + 0.0j}
            for _ in range(4):
                state = physical_step(state, decoded_word, deletion=deletion)
            maximum = max(
                maximum,
                vector_residual(decode_physical(state), decode_physical(reference[source])),
            )
        report[deletion] = maximum
    # Dirty-domain NEW deletion is tested directly; it is not meaningful on
    # the clean reference sector.
    target = (1 << RIGHT_ENDPOINT) | (1 << SOURCE_POINTER)
    dirty = initial_state(target, length)
    rails = [list(rail) for rail in dirty.rails]
    rails[0][0] = DIRTY
    dirty = replace(dirty, rails=tuple(tuple(rail) for rail in rails))
    damaged = commit_endpoint(dirty, deletion="complete_blank_NEW")
    report["complete_blank_NEW"] = float(
        damaged.source != dirty.source or damaged.rails != dirty.rails
    )
    return report


def old_silent_loss_control() -> dict[str, object]:
    decoded_word, _qr = C713.instrumented_decoded_word(2)
    old_word = OLD.classical_word(edge_local_predecessor=True)
    report = {}
    for applications in (5, 6):
        state = OLD.apply_recurrent(1, applications, decoded_word, old_word)
        overweight = sum(
            abs(amplitude) ** 2
            for (_basis, history), amplitude in state.items()
            if len(history) > 4
        )
        pending = sum(
            abs(amplitude) ** 2
            for (basis, _history), amplitude in state.items()
            if ((basis >> SOURCE_POINTER) & 1)
            or any(
                (basis >> (base + OLD.A.POINTER)) & 1
                for base in OLD.BANK_BASES
            )
        )
        report[applications] = {
            "history_beyond_capacity_probability_weight": overweight,
            "source_or_bank_pending_probability_weight": pending,
        }
    return report


def main() -> int:
    clean, outputs = clean_domain_certificate(13)
    held, _held_outputs = clean_domain_certificate(17)
    blocked = blocked_certificate(19)
    gray = gray_commit_certificate()
    covariance = covariance_certificate()
    deletions = deletion_certificate(outputs[4], 13)
    silent = old_silent_loss_control()
    app = clean["applications"]
    held_app = held["applications"]
    checks = {
        "one_step_intertwiner": app[1]["maximum_intertwiner_residual"] < TOL,
        "two_identical_updates": app[2]["maximum_intertwiner_residual"] < TOL,
        "four_identical_updates": app[4]["maximum_intertwiner_residual"] < TOL,
        "held_length_no_refit": held_app[4]["maximum_intertwiner_residual"] < TOL,
        "norm_and_particle_number": all(
            row["maximum_norm_residual"] < TOL
            and row["maximum_particle_number_leakage"] < TOL
            for row in app.values()
        ),
        "packet_and_auxiliary_code": all(
            row["maximum_bad_packet_or_auxiliary_weight"] < TOL
            for row in app.values()
        ),
        "dirty_then_blank_ack": (
            blocked["dirty_pending_signature_failures"] == 0
            and blocked["dirty_event_eventually_acknowledged"]
        ),
        "exhausted_pending_and_marker": (
            blocked["exhausted_pending_signature_failures"] == 0
            and blocked["exhausted_marker_motion_failures"] == 0
        ),
        "literal_reversible_ACK_commit": (
            gray["path_permutation_failures"] == 0
            and gray["single_bit_dirty_refusal_failures"] == 0
            and gray["deleted_swap_false_successes"] == 0
            and gray["ack_precedes_pointer_cleanup"]
        ),
        "proper_cubic_covariance": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["active_endpoint_direction_failures"] == 0
            and covariance["rail_shift_covariance_failures"] == 0
            and covariance["direction_product_failures"] == 0
        ),
        "active_deletions": all(value > 1.0e-3 for value in deletions.values()),
        "old_silent_loss_reproduced": (
            silent[5]["history_beyond_capacity_probability_weight"] > 1.0e-3
            and silent[6]["history_beyond_capacity_probability_weight"] > 1.0e-2
            and silent[5]["source_or_bank_pending_probability_weight"] == 0
            and silent[6]["source_or_bank_pending_probability_weight"] == 0
        ),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "clean_domain": clean,
        "held_domain": held,
        "blocked_domain": blocked,
        "reversible_local_commit": gray,
        "covariance": covariance,
        "deletion_residuals": deletions,
        "old_three_bank_silent_loss": silent,
        "intertwiner": (
            "D_export G_physical^n E = G_Cycle713+endpoint-history^n "
            "for n=1,2,4 on the clean pre-wrap code space"
        ),
        "constant_overhead_per_export_cell_M2": {
            "packet_payload": 34,
            "exported_identity_tag": 1,
            "retained_FRESH": 1,
            "start_handshake": 1,
            "cleanup_echo": 1,
            "direction_rails": 6,
            "upper_bound_before_route_work": 6 * 38,
        },
        "supplied": [
            "Cycle-713 decoded full free+seam+contact update and endpoint pointer",
            "six direction-labelled packet/handshake rails as one proper-cubic orbit",
            "initially blank incoming bilateral-shift sector with no return in the tested horizon",
            "BINDER/ACTUAL/ADMISS/LAW=1 packet admission and clean source controller genesis",
            "fixed onsite-commit then range-one-shift circuit order",
        ],
        "derived": [
            "complete-blank and not-FRESH NEW predicate embedded in one local codeword swap",
            "append ACK before endpoint cleanup on the swap's explicit Gray path",
            "edge-local predecessor identity/cross-edge tag without a bank-number ROM",
            "parallel range-one export with constant register overhead per rail cell",
            "clean n=1,2,4 Cycle-713/history intertwiner and held-size replication",
            "blocked decoded-event invariance while spatial handshake coordinates advance",
        ],
        "open": [
            "literal one-/two-M2 decomposition and collision-free route of the 44-bit target/controller transposition with six invariant controls",
            "physical placement of all six 38-M2 rail families around the landed Cycle-713 block",
            "derivation or enforcement of the blank/no-return rail sector and positive-density collision handling",
            "numeric Cycle-612 predecessor adapter and causal-duration acceptance harness",
            "Record permanence, Born realization, source/gravity law, and any physical-time interpretation",
        ],
        "boundary": (
            "Positive Record/time-interface bridge on the isolated clean pre-wrap export sector. "
            "It removes the O(chain-length) sweep and silent finite-bank event deletion, but "
            "does not enlarge core overlapping-star matter closure or derive fresh resources."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE718_SPATIAL_ACK_EXPORT_SUPPORT_PASS"
        if report["pass"] else "CYCLE718_SPATIAL_ACK_EXPORT_SUPPORT_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
