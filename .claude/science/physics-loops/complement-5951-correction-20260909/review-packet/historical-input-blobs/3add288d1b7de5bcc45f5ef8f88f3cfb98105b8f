#!/usr/bin/env python3
"""Cycle 719 core: local marker/handshake replacement for the bank sweep.

The marker starts at the matter-side bank, advances only across the next
incident edge until it reaches a token with a complete-blank selected cell,
applies the unchanged packet word, and follows the retained link latches back.
The trace is a certificate for a local controller law; controller-gate
synthesis is kept distinct from the selected physical data word.
"""
from __future__ import annotations

from hashlib import sha256
import itertools
import json
from pathlib import Path
import random
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 300
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
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle719_source_local_finalizer_core_2026_07_26 as M


A = M.A
B = M.B
P = M.P
R3 = M.R3
C712 = M.C712
TOL = 5.0e-10


HANDOFF_FORWARD = B.transient_pre_latch_word() + P.forward_transfer_word()
RELAY_LATCH = B.relay_latch_word(pending_marker_required=True)
RELAY_SWAP = B.relay_swap_word()
RELAY_UNLATCH = B.relay_latch_word(pending_marker_required=False)
HANDOFF_RETURN = P.carrier_return_word() + B.transient_post_latch_word()
PACKET = B.transient_packet_word()


def selected_complete_blank(bank):
    """Local predicate; it contains no bank address or packet count."""
    for index, layout in enumerate(A.CELLS):
        if bank[A.TOKEN[index]] and not any(bank[wire] for wire in layout["payload"]):
            return True
    return False


def mapped_action(kind, index, local):
    if kind == "bank":
        return tuple(M.offset_gate(gate, M.R12.BANK_BASES[index]) for gate in local)
    if kind in ("handoff", "relay"):
        return tuple(M.map_pair_gate(gate, index, kind) for gate in local)
    if kind == "cross":
        return (A.cn(
            M.R12.LINK_BASES[index],
            M.R12.BANK_BASES[index + 1] + int(A.CELLS[0]["pred"][1]),
        ),)
    raise ValueError(kind)


def apply_one(banks, links, action, *, inverse=False):
    return B.apply_actions(banks, links, (action,), inverse=inverse)


def write_modules(bits, banks, links, bank_count):
    output = list(bits)
    for base, bank in zip(M.R12.BANK_BASES[:bank_count], banks):
        output[base:base + A.N] = bank
    for base, link in zip(M.R12.LINK_BASES[:bank_count - 1], links):
        output[base:base + B.LINK_WIDTH] = link
    return tuple(output)


def local_handshake_word(
    before,
    bank_count,
    *,
    marker_positions=(0,),
    mutation=None,
    candidate_scan=None,
):
    """Select the data word by the one-marker local transition law.

    ``candidate_scan`` changes only the order in which candidate sites are
    inspected.  Exactly one marker makes the enabled local transition unique.
    The returned word is the literal selected reversible data word, not yet a
    physical synthesis of the marker transition itself.
    """
    if len(marker_positions) != 1 or len(set(marker_positions)) != 1:
        return {
            "lawful": False,
            "reason": "one-marker sector",
            "marker_count": len(marker_positions),
        }
    position = marker_positions[0]
    if position != 0:
        return {
            "lawful": False,
            "reason": "source-boundary marker",
            "marker_count": 1,
        }
    scan = tuple(range(bank_count)) if candidate_scan is None else tuple(candidate_scan)
    if set(scan) != set(range(bank_count)):
        raise ValueError("candidate scan must be a bank permutation")

    source_word = R3.source_compute_word()
    current = A.apply_semantic(before, source_word)
    banks, links = M.unpack_state(current, bank_count)
    selected = list(source_word)
    trace = []
    mode = "forward"

    def append_action(action):
        nonlocal banks, links
        banks, links = apply_one(banks, links, action)
        selected.extend(mapped_action(*action))
        trace.append((mode, position, action[0], action[1]))

    # The scan is operationally inert on the one-marker domain: it only finds
    # the unique marked bank.  This explicitly tests host enumeration removal.
    while True:
        enabled = tuple(candidate for candidate in scan if candidate == position)
        if enabled != (position,):
            raise AssertionError((scan, position, enabled))
        if selected_complete_blank(banks[position]) or position == bank_count - 1:
            break
        actions = [
            ("handoff", position, HANDOFF_FORWARD),
            ("relay", position, RELAY_LATCH),
            ("relay", position, RELAY_SWAP),
        ]
        if mutation == "swap_forward_local_phases":
            actions[0], actions[2] = actions[2], actions[0]
        elif mutation == "delete_forward_transfer" and position == 0:
            actions[0] = ("handoff", position, HANDOFF_FORWARD[:-3])
        for action in actions:
            append_action(action)
        position += 1

    packet = PACKET
    if mutation == "delete_success_marker":
        packet = B.transient_packet_word(omit="success_marker")
    append_action(("bank", position, packet))
    if position:
        append_action(("cross", position - 1, ()))

    mode = "return"
    while position:
        edge = position - 1
        actions = [
            ("relay", edge, RELAY_SWAP),
            ("relay", edge, RELAY_UNLATCH),
            ("handoff", edge, HANDOFF_RETURN),
        ]
        if mutation == "swap_return_local_phases":
            actions[0], actions[2] = actions[2], actions[0]
        for action in actions:
            append_action(action)
        position -= 1

    body_after = write_modules(current, banks, links, bank_count)
    finalizer = M.source_finalizer_word(bank_count)
    selected.extend(finalizer)
    after = A.apply_semantic(body_after, finalizer)
    literal = tuple(selected)
    if A.apply_semantic(before, literal) != after:
        raise AssertionError("selected word/transition trace mismatch")
    return {
        "lawful": True,
        "after": after,
        "word": literal,
        "trace": tuple(trace),
        "marker_returned_source": position == 0,
        "marker_phase": "done",
    }


def held_certificate(bank_count):
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    coarse = B.C704.C610.EventChain(bank=2 * bank_count)
    failures = inverse_failures = fixed_failures = postimage_failures = 0
    traces = []
    worst_input = None
    worst_word = ()
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        row = local_handshake_word(before, bank_count)
        after = row["after"]
        fixed = A.apply_semantic(before, M.global_allocator_word(bank_count))
        fixed_failures += after != fixed
        inverse_failures += A.apply_semantic(after, tuple(reversed(row["word"]))) != before
        banks, links = M.unpack_state(after, bank_count)
        decoded, _order = B.decode_local_graph(banks, links)
        status = coarse.admit(
            tick_id=event,
            orientation=1 if direction == (1, 0) else -1,
            certificate=1,
            binder=1,
            actuality=1,
            admissibility=1,
            law_domain=1,
        )
        failures += status != "admitted" or B.cell_rows(decoded) != B.cell_rows(coarse)
        postimage_failures += any((
            after[R3.X.SOURCE_POINTER],
            any(bank[wire] for bank in banks for wire in (
                A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                *A.FRESH, *A.ZERO_WORK, A.TOKEN_OK,
            )),
            any(any(link) for link in links),
        ))
        traces.append(len(row["trace"]))
        if len(row["word"]) > len(worst_word):
            worst_input, worst_word = before, row["word"]
        state = after
    return {
        "banks": bank_count,
        "events": 2 * bank_count,
        "logical_failures": failures,
        "fixed_sweep_equivalence_failures": fixed_failures,
        "inverse_failures": inverse_failures,
        "lawful_postimage_failures": postimage_failures,
        "minimum_local_transitions": min(traces),
        "maximum_local_transitions": max(traces),
        "selected_semantic_gate_range": (
            len(local_handshake_word(
                M.prepare_endpoint(M.pack_state(*B.chain_genesis(bank_count)), (1, 0)),
                bank_count,
            )["word"]),
            len(worst_word),
        ),
        "state": state,
        "chain": coarse,
        "worst_input": worst_input,
        "worst_word": worst_word,
    }


def scan_order_certificate():
    bank_count = 5
    banks, links = B.chain_genesis(bank_count)
    state = M.pack_state(banks, links)
    rng = random.Random(7262026)
    scans = [
        tuple(range(bank_count)),
        tuple(reversed(range(bank_count))),
    ]
    for _ in range(22):
        row = list(range(bank_count))
        rng.shuffle(row)
        scans.append(tuple(row))
    rows = failures = 0
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        expected = local_handshake_word(before, bank_count, candidate_scan=scans[0])
        for scan in scans:
            observed = local_handshake_word(before, bank_count, candidate_scan=scan)
            rows += 1
            failures += observed["after"] != expected["after"]
            failures += observed["trace"] != expected["trace"]
        state = expected["after"]
    return {"rows": rows, "failures": failures, "scan_orders": len(scans)}


def mutation_certificate():
    banks, links = B.chain_genesis(5)
    state = M.pack_state(banks, links)
    rows = {label: 0 for label in (
        "swap_forward_local_phases",
        "delete_forward_transfer",
        "delete_success_marker",
        "swap_return_local_phases",
    )}
    trials = {label: 0 for label in rows}
    for event in range(10):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = M.prepare_endpoint(state, direction)
        expected = local_handshake_word(before, 5)
        for label in rows:
            observed = local_handshake_word(before, 5, mutation=label)
            trials[label] += 1
            rows[label] += observed["after"] != expected["after"]
        state = expected["after"]
    return {label: {"trials": trials[label], "changed_outputs": rows[label]} for label in rows}


def multi_source_certificate():
    banks, links = B.chain_genesis(5)
    before = M.prepare_endpoint(M.pack_state(banks, links), (1, 0))
    patterns = ((0, 1), (0, 4), (0, 2, 4), ())
    rows = []
    for markers in patterns:
        result = local_handshake_word(before, 5, marker_positions=markers)
        adjacent = sum(abs(left - right) == 1 for left, right in itertools.combinations(markers, 2))
        rows.append({
            "markers": markers,
            "lawful": result["lawful"],
            "local_shared_star_collisions": adjacent,
            "reason": result.get("reason"),
        })
    return {
        "rows": rows,
        "rejected_rows": sum(not row["lawful"] for row in rows),
        "adjacent_collision_rows": sum(row["local_shared_star_collisions"] > 0 for row in rows),
        "boundary": (
            "one source-root marker is the declared sector; adjacent duplicate markers "
            "also violate a bounded shared-star exclusion, while distant multi-source "
            "composition remains outside this compiler theorem"
        ),
    }


def physical_route_certificate(worst_word):
    layout = M.R12.full_wire_layout()
    baseline = M.build_physical_word(layout)
    sites = layout["wire_sites"]
    matrices = {"X": A.X, "H": A.H, "T": A.T, "TD": A.TD, "CNOT": A.CNOT}
    allocator = tuple(
        C712.c707.Instruction(
            "handshake_allocator_" + kind,
            tuple(sites[wire] for wire in wires),
            matrices[kind],
        )
        for kind, wires in A.expanded(worst_word)
    )
    word = baseline["prefix"] + allocator + baseline["suffix"]
    routed, route = C712.c707.route_word(word)
    inverse, inverse_route = C712.c707.route_word(tuple(reversed(word)))
    covariance = M.R12.active_frame_certificate(word, routed)
    return {
        "selected_semantic_gates": len(worst_word),
        "selected_allocator_primitives": len(allocator),
        "complete_physical_primitives": len(word),
        "forward_routed_NN_gates": len(routed),
        "inverse_routed_NN_gates": len(inverse),
        "maximum_route_distance": max(route["maximum_route_distance"], inverse_route["maximum_route_distance"]),
        "non_NN_failures": route["non_NN_failures"] + inverse_route["non_NN_failures"],
        "operand_order_failures": route["operand_order_failures"] + inverse_route["operand_order_failures"],
        "route_return_failures": route["route_return_failures"] + inverse_route["route_return_failures"],
        "forward_route_deletions": route["delete_first_swap_detected_macros"],
        "inverse_route_deletions": inverse_route["delete_first_swap_detected_macros"],
        "forward_word_sha256": route["word_sha256"],
        "inverse_word_sha256": inverse_route["word_sha256"],
        "covariance": covariance,
    }


def inherited_matter_certificate():
    word, qr = C712.decoded_word(2)
    cycle230 = C712.cycle230_semantic_certificate(word)
    basis = tuple(state for state in range(1 << 12) if state.bit_count() <= 2)
    _direct, _coin, free_one = C712.direct_restricted_update(basis)
    stages = C712.stage_and_falsifier_certificate(word, basis, free_one)
    return {
        "coin_QR_residual": qr,
        "mass_residual": cycle230["mass_residual"],
        "coin_matrix_residual": cycle230["coin_matrix_residual"],
        "FSWAP_matrix_residual": cycle230["FSWAP_matrix_residual"],
        "onsite_64_state_contact_residual": cycle230["onsite_64_state_contact_residual"],
        "internal_depth_two_stream_residual": cycle230["internal_depth_two_stream_residual"],
        "coin_stage_residual": stages["coin_stage_residual"],
        "reverse_stage_residual": stages["reverse_stage_residual"],
        "seam_stage_residual": stages["landed_seam_stage_residual"],
        "contact_stage_residual": stages["contact_stage_residual"],
        "single_FSWAP_falsifier_residual": stages["single_nonadjacent_tensor_FSWAP_residual"],
    }


def main():
    held = {size: held_certificate(size) for size in (2, 5, 12)}
    scan = scan_order_certificate()
    mutations = mutation_certificate()
    multi = multi_source_certificate()
    route = physical_route_certificate(held[12]["worst_word"])
    matter = inherited_matter_certificate()
    chain = held[12]["chain"]
    checks = {
        "held_2_5_12_exact": all(
            not row["logical_failures"]
            and not row["fixed_sweep_equivalence_failures"]
            and not row["inverse_failures"]
            and not row["lawful_postimage_failures"]
            for row in held.values()
        ),
        "candidate_scan_order_retired": scan["failures"] == 0,
        "local_phase_mutations_active": all(
            row["changed_outputs"] > 0 for row in mutations.values()
        ),
        "multi_source_controls_exposed": (
            multi["rejected_rows"] == len(multi["rows"])
            and multi["adjacent_collision_rows"] > 0
        ),
        "literal_physical_route": all(route[key] == 0 for key in (
            "non_NN_failures", "operand_order_failures", "route_return_failures",
        )),
        "active_24_576_translations": all(
            value == 0
            for key, value in route["covariance"].items()
            if key.endswith("failures")
        ),
        "matter_free_seam_contact_preserved": all(
            matter[key] < TOL for key in (
                "coin_QR_residual", "mass_residual", "coin_matrix_residual",
                "FSWAP_matrix_residual", "onsite_64_state_contact_residual",
                "internal_depth_two_stream_residual", "coin_stage_residual",
                "reverse_stage_residual", "seam_stage_residual", "contact_stage_residual",
            )
        ) and matter["single_FSWAP_falsifier_residual"] > 1.0,
        "unchanged_Cycle610_612": (
            chain.interval(2, 11), chain.interval(11, 23), chain.interval(2, 23)
        ) == (9, 12, 21),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "held": {
            size: {key: value for key, value in row.items() if key not in (
                "state", "chain", "worst_input", "worst_word",
            )}
            for size, row in held.items()
        },
        "candidate_scan": scan,
        "mutations": mutations,
        "multi_source": multi,
        "physical_route": route,
        "matter": matter,
        "supplied": [
            "source boundary, one marker, clean bank/link/route genesis",
            "bounded local handoff/relay/packet/return gate words",
            "BINDER/ACTUAL/ADMISS/LAW and the Cycle713 endpoint source",
            "the internal gate order inside each bounded local macro",
        ],
        "derived": [
            "destination discovery from token plus selected complete-blank predicate",
            "forward marker path and retained-latch return path with no bank address",
            "exact equivalence to the old global sweep on held 2/5/12",
            "candidate-site enumeration invariance in the one-marker sector",
            "literal physical-M2 route of the longest selected data trace",
        ],
        "open": [
            "literal reversible M2 synthesis of marker transition/control gates",
            "autonomous preparation/enforcement of the one-marker and clean-work sector",
            "distant multi-source composition beyond the declared one-root domain",
            "post-capacity renewal and autonomous occurrence/admission",
        ],
        "boundary": (
            "The bank address sweep is removed at the transition-law level: one local marker "
            "discovers the destination and returns along physical latches.  The selected data "
            "word is literal and routed, but the marker-controlled transition circuit itself "
            "is not yet synthesized into M2 gates.  No controller step is called time."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE719_LOCAL_HANDSHAKE_CONTROLLER_CORE_PASS" if report["pass"] else "CYCLE719_LOCAL_HANDSHAKE_CONTROLLER_CORE_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
