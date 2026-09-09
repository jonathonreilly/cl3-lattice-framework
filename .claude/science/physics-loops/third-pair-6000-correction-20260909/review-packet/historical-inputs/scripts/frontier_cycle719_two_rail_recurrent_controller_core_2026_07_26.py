#!/usr/bin/env python3
"""Cycle 719 core: two-rail physical controller for the handshake program.

One controller token visits a geometry-carried program ring.  At station s,
Q applies only the bounded local macro stored there; two disjoint SWAP layers
R move the token to station s+1.  One full orbit executes the recurrent bank
handshake.  Controller ordinals are circuit structure, not physical time.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import random
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
    "scripts/frontier_cycle719_recurrent_physical_route_core_2026_07_26.py",
    "scripts/frontier_cycle719_source_local_finalizer_core_2026_07_26.py",
    "scripts/frontier_cycle719_local_handshake_controller_core_2026_07_26.py",
    "scripts/frontier_cycle719_two_rail_recurrent_controller_core_2026_07_26.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_local_handshake_controller_core_2026_07_26 as H


A = H.A
B = H.B
M = H.M
R3 = H.R3
C712 = H.C712


def interleaved_program(bank_count, *, physical_padding=False):
    """Geometry-generated packet/edge/return program; no bank address ROM."""
    prefix = [("source", 0, R3.source_compute_word())]
    for bank in range(bank_count):
        prefix.append(("bank", bank, H.PACKET))
        if bank:
            prefix.append(("cross", bank - 1, ()))
        if bank < bank_count - 1:
            prefix.extend((
                ("handoff", bank, H.HANDOFF_FORWARD),
                ("relay", bank, H.RELAY_LATCH),
                ("relay", bank, H.RELAY_SWAP),
            ))
    reverse = []
    for edge in reversed(range(bank_count - 1)):
        reverse.extend((
            ("relay", edge, H.RELAY_SWAP),
            ("relay", edge, H.RELAY_UNLATCH),
            ("handoff", edge, H.HANDOFF_RETURN),
        ))
        if physical_padding and edge:
            reverse.extend((("identity", edge, ()), ("identity", edge, ())))
    suffix = [("finalizer", 0, M.source_finalizer_word(bank_count))]
    if not physical_padding:
        return tuple(prefix + reverse + suffix)
    if bank_count != 12:
        raise ValueError("the physical track fixture is the held 12-bank case")
    # 130 A/B stations fit a 12 by 120 rectangle.  Prefix ascends one side;
    # the padded reverse descends the other beside the same bank/link modules.
    before_reverse = prefix + [("identity", 0, ())] * 15
    program = before_reverse + reverse + suffix
    program += [("identity", 0, ())] * (130 - len(program))
    if len(program) != 130:
        raise AssertionError(len(program))
    return tuple(program)


def mapped_macro(row):
    kind, index, local = row
    if kind in ("source", "finalizer"):
        return tuple(local)
    if kind == "identity":
        return ()
    return H.mapped_action(kind, index, local)


def program_word(program):
    return tuple(gate for row in program for gate in mapped_macro(row))


def gate_digest(word):
    return sha256("".join(gate.kind + repr(gate.wires) for gate in word).encode()).hexdigest()


def controlled_macro(word, control, work):
    output = []
    for gate in word:
        if gate.kind == "X":
            output.append(A.cn(control, gate.wires[0]))
        elif gate.kind == "CNOT":
            output.append(A.tof(control, gate.wires[0], gate.wires[1]))
        elif gate.kind == "TOF":
            output.extend(A.mcx((control,) + gate.wires[:2], gate.wires[2], (work,)))
        else:
            raise ValueError(gate.kind)
    return tuple(output)


def swap_word(left, right):
    return (A.cn(left, right), A.cn(right, left), A.cn(left, right))


def controller_word(program, data_wires):
    stations = len(program)
    a_base, b_base, work_base = data_wires, data_wires + stations, data_wires + 2 * stations
    q = tuple(
        gate
        for station, row in enumerate(program)
        for gate in controlled_macro(mapped_macro(row), a_base + station, work_base + station)
    )
    r1 = tuple(
        gate for station in range(stations)
        for gate in swap_word(a_base + station, b_base + station)
    )
    r2 = tuple(
        gate for station in range(stations)
        for gate in swap_word(b_base + station, a_base + (station + 1) % stations)
    )
    return q + r1 + r2


def apply_controller_step(data, program, a_tokens, b_tokens, *, reverse=False, q_order=None):
    stations = len(program)
    a = list(a_tokens)
    b = list(b_tokens)
    output = data
    if not reverse:
        order = tuple(range(stations)) if q_order is None else tuple(q_order)
        for station in order:
            if a[station]:
                output = A.apply_semantic(output, mapped_macro(program[station]))
        for station in range(stations):
            a[station], b[station] = b[station], a[station]
        for station in range(stations):
            target = (station + 1) % stations
            b[station], a[target] = a[target], b[station]
    else:
        for station in reversed(range(stations)):
            target = (station + 1) % stations
            b[station], a[target] = a[target], b[station]
        for station in reversed(range(stations)):
            a[station], b[station] = b[station], a[station]
        order = tuple(reversed(range(stations))) if q_order is None else tuple(q_order)
        for station in order:
            if a[station]:
                output = A.apply_semantic(output, tuple(reversed(mapped_macro(program[station]))))
    return output, tuple(a), tuple(b)


def run_orbit(data, program, *, token_positions=(0,), reverse=False, q_orders=None):
    stations = len(program)
    a = tuple(int(station in token_positions) for station in range(stations))
    b = (0,) * stations
    trace = []
    orders = q_orders or (None,) * stations
    iterable = range(stations) if not reverse else range(stations)
    for step in iterable:
        live_before = tuple(index for index, value in enumerate(a) if value)
        data, a, b = apply_controller_step(
            data, program, a, b, reverse=reverse, q_order=orders[step]
        )
        live_after = tuple(index for index, value in enumerate(a) if value)
        trace.append((live_before, live_after, sum(b)))
    return data, a, b, tuple(trace)


def held_certificate(bank_count):
    program = interleaved_program(bank_count)
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    coarse = B.C704.C610.EventChain(bank=2 * bank_count)
    logical = fixed = inverse = postimage = token_failures = 0
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        after, a, b, trace = run_orbit(before, program)
        expected = A.apply_semantic(before, M.global_allocator_word(bank_count))
        fixed += after != expected
        token_failures += a != (1,) + (0,) * (len(program) - 1) or any(b)
        restored, ia, ib, _ = run_orbit(after, program, reverse=True)
        inverse += restored != before
        inverse += ia != a or ib != b
        banks, links = M.unpack_state(after, bank_count)
        decoded, _order = B.decode_local_graph(banks, links)
        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1, binder=1, actuality=1, admissibility=1, law_domain=1,
        )
        logical += status != "admitted" or B.cell_rows(decoded) != B.cell_rows(coarse)
        postimage += any((
            after[R3.X.SOURCE_POINTER],
            any(bank[wire] for bank in banks for wire in (
                A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
            )),
            any(any(link) for link in links),
        ))
        state = after
    return {
        "banks": bank_count,
        "program_stations": len(program),
        "program_semantic_gates": len(program_word(program)),
        "events": 2 * bank_count,
        "logical_failures": logical,
        "fixed_word_failures": fixed,
        "inverse_failures": inverse,
        "postimage_failures": postimage,
        "token_return_failures": token_failures,
        "state": state,
        "chain": coarse,
    }


def controlled_truth_certificate():
    rows = failures = work_failures = dirty_rows = dirty_differences = 0
    local_words = (
        ((A.x(0),), 1, 2, False),
        ((A.cn(0, 1),), 2, 3, False),
        ((A.tof(0, 1, 2),), 3, 5, True),
    )
    for word, data_width, total_width, separate_work in local_words:
        lifted = controlled_macro(word, data_width, total_width - 1)
        for basis in range(1 << total_width):
            before = tuple((basis >> wire) & 1 for wire in range(total_width))
            observed = A.apply_semantic(before, lifted)
            expected = list(before)
            if before[data_width]:
                acted = A.apply_semantic(before[:data_width], word)
                expected[:data_width] = acted
            if separate_work and before[-1]:
                dirty_rows += 1
                dirty_differences += observed != tuple(expected)
                continue
            rows += 1
            failures += observed != tuple(expected)
            if separate_work:
                work_failures += observed[-1] != 0
    return {
        "clean_rows": rows,
        "clean_failures": failures,
        "clean_work_return_failures": work_failures,
        "dirty_rows_outside_domain": dirty_rows,
        "dirty_rows_changing_declared_action": dirty_differences,
    }


def order_and_domain_controls():
    program = interleaved_program(5)
    banks, links = B.chain_genesis(5)
    state = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    expected, *_ = run_orbit(state, program)
    rng = random.Random(7272026)
    orders = []
    for _step in range(len(program)):
        order = list(range(len(program)))
        rng.shuffle(order)
        orders.append(tuple(order))
    shuffled, *_ = run_orbit(state, program, q_orders=tuple(orders))
    zero, za, zb, _ = run_orbit(state, program, token_positions=())
    double, da, db, _ = run_orbit(state, program, token_positions=(0, 1))
    deleted = list(program)
    deleted[1] = ("identity", 0, ())
    deleted_output, *_ = run_orbit(state, tuple(deleted))
    # R before Q shifts the token first and therefore selects a cyclic program.
    a = (1,) + (0,) * (len(program) - 1)
    b = (0,) * len(program)
    hostile = state
    for _ in range(len(program)):
        for station in range(len(program)):
            a_l, b_l = list(a), list(b)
            a_l[station], b_l[station] = b_l[station], a_l[station]
            a, b = tuple(a_l), tuple(b_l)
        for station in range(len(program)):
            target = (station + 1) % len(program)
            a_l, b_l = list(a), list(b)
            b_l[station], a_l[target] = a_l[target], b_l[station]
            a, b = tuple(a_l), tuple(b_l)
        for station in range(len(program)):
            if a[station]:
                hostile = A.apply_semantic(hostile, mapped_macro(program[station]))
    return {
        "shuffled_Q_station_order_equal": shuffled == expected,
        "zero_token_data_unchanged": zero == state,
        "zero_token_return": not any(za) and not any(zb),
        "two_token_count_conserved": sum(da) + sum(db) == 2,
        "two_token_output_changed": double != expected,
        "delete_packet_station_changed": deleted_output != expected,
        "R_before_Q_changed": hostile != expected,
    }


def rectangle_track(width, height, origin=(-26, -7, -4)):
    ox, oy, oz = origin
    rows = [(ox + x, oy, oz) for x in range(width)]
    rows += [(ox + width - 1, oy, oz + z) for z in range(1, height)]
    rows += [(ox + x, oy, oz + height - 1) for x in reversed(range(width - 1))]
    rows += [(ox, oy, oz + z) for z in reversed(range(1, height - 1))]
    return tuple(rows)


def held_physical_program_and_track(bank_count):
    if bank_count == 2:
        program = interleaved_program(2)
        track = rectangle_track(3, 10, origin=(-17, -7, 4))
    elif bank_count == 5:
        base = list(interleaved_program(5))
        base += [("identity", 0, ())] * (45 - len(base))
        program = tuple(base)
        track = rectangle_track(5, 42, origin=(-19, -7, 4))
    elif bank_count == 12:
        program = interleaved_program(12, physical_padding=True)
        track = rectangle_track(12, 120)
    else:
        raise ValueError(bank_count)
    if len(track) != 2 * len(program):
        raise AssertionError((bank_count, len(track), len(program)))
    return program, track


def streaming_route(semantic_word, wire_sites):
    c655 = C712.c707.c655
    matrices = {"X": A.X, "H": A.H, "T": A.T, "TD": A.TD, "CNOT": A.CNOT}
    hasher = sha256()
    primitives = routed = one = two = maximum = deletions = 0
    nn = operand = returned = 0
    touched = set()
    for semantic in semantic_word:
        for kind, wires in A.expanded((semantic,)):
            primitives += 1
            sites = tuple(wire_sites[wire] for wire in wires)
            matrix = matrices[kind]
            hasher.update(kind.encode())
            hasher.update(repr(sites).encode())
            hasher.update(c655.matrix_digest(matrix).encode())
            if len(sites) == 1:
                one += 1
                routed += 1
                touched.add(sites[0])
                continue
            two += 1
            left, right = sites
            path = c655.manhattan_path(left, right)
            distance = len(path) - 1
            maximum = max(maximum, distance)
            routed += 2 * distance - 1
            nn += any(c655.l1(a, b) != 1 for a, b in zip(path, path[1:]))
            labels = list(path)
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            operand += labels[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            returned += labels != list(path)
            deletions += distance > 1
            touched.update(path)
            hasher.update(repr(path).encode())
    return {
        "physical_primitives": primitives,
        "one_M2_primitives": one,
        "two_M2_primitives": two,
        "routed_NN_gates": routed,
        "maximum_route_distance": maximum,
        "non_NN_failures": nn,
        "operand_order_failures": operand,
        "route_return_failures": returned,
        "delete_first_route_swap_detected": deletions,
        "touched_M2": len(touched),
        "route_blueprint_sha256": hasher.hexdigest(),
    }


def physical_controller_certificate(bank_count):
    program, track = held_physical_program_and_track(bank_count)
    layout = M.R12.full_wire_layout()
    data_sites = layout["wire_sites"]
    a_sites = track[::2]
    b_sites = track[1::2]
    work_sites = tuple((x, y - 1, z) for x, y, z in a_sites)
    wire_sites = data_sites + a_sites + b_sites + work_sites
    controller_sites = a_sites + b_sites + work_sites
    assigned = set(layout["assigned_sites"])
    placement_collisions = (
        len(controller_sites) - len(set(controller_sites))
        + len(assigned & set(controller_sites))
    )
    occupied = assigned | set(controller_sites)
    h_word = controller_word(program, len(data_sites))
    forward = streaming_route(h_word, wire_sites)
    inverse = streaming_route(tuple(reversed(h_word)), wire_sites)
    frames = C712.C709.F.base.proper_cubic_frames()
    coordinate_failures = translation_failures = rail_failures = 0
    for left, right in zip(track, track[1:] + track[:1]):
        rail_failures += sum(abs(a - b) for a, b in zip(left, right)) != 1
    for frame in frames:
        inverse_frame = frame.T
        for site in wire_sites[len(data_sites):]:
            moved = tuple(int(value) for value in frame @ np.asarray(site))
            restored = tuple(int(value) for value in inverse_frame @ np.asarray(moved))
            coordinate_failures += restored != site
    for shift in ((3, -2, 1), (-5, 4, 2)):
        for site in wire_sites[len(data_sites):]:
            moved = tuple(site[axis] + shift[axis] for axis in range(3))
            restored = tuple(moved[axis] - shift[axis] for axis in range(3))
            translation_failures += restored != site
    product_failures = 0
    for left in frames:
        for right in frames:
            product = left @ right
            product_failures += not any(np.array_equal(product, frame) for frame in frames)
    return {
        "banks": bank_count,
        "stations": len(program),
        "program_nonidentity_stations": sum(bool(mapped_macro(row)) for row in program),
        "program_semantic_gates": len(program_word(program)),
        "program_word_sha256": gate_digest(program_word(program)),
        "controller_semantic_gates": len(h_word),
        "controller_word_sha256": gate_digest(h_word),
        "controller_M2": 3 * len(program),
        "total_declared_M2": len(occupied),
        "placement_collisions": placement_collisions,
        "rail_cycle_NN_failures": rail_failures,
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "coordinate_failures": coordinate_failures,
        "frame_product_failures": product_failures,
        "translation_failures": translation_failures,
        "forward": forward,
        "inverse": inverse,
    }


def main():
    held = {size: held_certificate(size) for size in (2, 5, 12)}
    truth = controlled_truth_certificate()
    controls = order_and_domain_controls()
    physical = {size: physical_controller_certificate(size) for size in (2, 5, 12)}
    matter = H.inherited_matter_certificate()
    chain = held[12]["chain"]
    checks = {
        "held_2_5_12_full_orbit": all(
            not row["logical_failures"]
            and not row["fixed_word_failures"]
            and not row["inverse_failures"]
            and not row["postimage_failures"]
            and not row["token_return_failures"]
            for row in held.values()
        ),
        "controlled_gate_truth": (
            truth["clean_failures"] == truth["clean_work_return_failures"] == 0
            and truth["dirty_rows_changing_declared_action"] > 0
        ),
        "order_and_domain_controls": all(controls.values()),
        "literal_controller_route": all(
            row["placement_collisions"] == 0
            and row["rail_cycle_NN_failures"] == 0
            for row in physical.values()
        )
        and all(
            row[direction][key] == 0
            for row in physical.values()
            for direction in ("forward", "inverse")
            for key in ("non_NN_failures", "operand_order_failures", "route_return_failures")
        ),
        "controller_24_576_translations": all(
            row[key] == 0
            for row in physical.values()
            for key in (
                "coordinate_failures", "frame_product_failures", "translation_failures",
            )
        ),
        "matter_fixtures_preserved": all(
            matter[key] < H.TOL for key in (
                "coin_QR_residual", "mass_residual", "coin_matrix_residual",
                "FSWAP_matrix_residual", "onsite_64_state_contact_residual",
                "internal_depth_two_stream_residual", "coin_stage_residual",
                "reverse_stage_residual", "seam_stage_residual", "contact_stage_residual",
            )
        ) and matter["single_FSWAP_falsifier_residual"] > 1,
        "unchanged_Cycle610_612": (
            chain.interval(2, 11), chain.interval(11, 23), chain.interval(2, 23)
        ) == (9, 12, 21),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "held": {
            size: {key: value for key, value in row.items() if key not in ("state", "chain")}
            for size, row in held.items()
        },
        "controlled_truth": truth,
        "controls": controls,
        "physical": physical,
        "matter": matter,
        "supplied": [
            "one controller token at source station and zero B/work rails",
            "source boundary and oriented finite program ring",
            "Q-before-R layer order and bounded local macro gate order",
            "clean data-bank/link/route genesis and event predicates",
        ],
        "derived": [
            "two-rail time-homogeneous controller step H=R Q",
            "one full controller orbit selects the geometry-generated handshake program",
            "exact held 2/5/12 full-orbit intertwining and inverse",
            "station-block order invariance on the one-token sector",
            "literal controlled-gate and nearest-neighbor routing blueprints",
        ],
        "open": [
            "autonomous preparation/enforcement of one-token and clean-work genesis",
            "removal of the supplied source boundary/ring orientation if demanded",
            "distant multiple-controller-token composition",
            "post-capacity renewal and autonomous occurrence/admission",
        ],
        "boundary": (
            "On the declared one-token program-ring code, H^P executes the same fixed local "
            "handshake and returns controller/data work to the same encoding.  P is a circuit "
            "orbit length, not time.  This is not a genesis/enforcement, multi-source, Record, "
            "Born, or source/gravity law."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE719_TWO_RAIL_RECURRENT_CONTROLLER_CORE_PASS" if report["pass"] else "CYCLE719_TWO_RAIL_RECURRENT_CONTROLLER_CORE_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
