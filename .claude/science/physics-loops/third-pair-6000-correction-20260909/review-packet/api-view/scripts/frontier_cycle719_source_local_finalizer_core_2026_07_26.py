#!/usr/bin/env python3
"""Cycle 719 core: source-local reversible finalizer for the 12-bank route.

The returned success/pending marker gates an uncompute from the post-update
matter endpoint occupations already present at bank zero.  Successful appends
return source pointer and carrier clean; refusal/exhaustion retain both.  No
remote newly-written packet bit controls the source finalizer.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys


AUDIT_TIMEOUT_SEC = 300
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
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle718_token_relative_relay_core_2026_07_26 as R3
import frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26 as B
import frontier_cycle719_recurrent_physical_route_core_2026_07_26 as R12


A = B.A
P = B.P
TOL = 5.0e-10


def offset_gate(gate, base):
    return A.Gate(gate.kind, tuple(base + wire for wire in gate.wires))


def map_pair_gate(gate, edge, kind):
    split = 0 if kind == "handoff" else P.LINK_AUX_WIDTH
    wires = []
    for wire in gate.wires:
        if wire < A.N:
            wires.append(R12.BANK_BASES[edge] + wire)
        elif wire < 2 * A.N:
            wires.append(R12.BANK_BASES[edge + 1] + wire - A.N)
        else:
            wires.append(R12.LINK_BASES[edge] + split + wire - 2 * A.N)
    return A.Gate(gate.kind, tuple(wires))


def mapped_body_word(bank_count: int):
    output = []
    for kind, index, local in B.actions(bank_count):
        if kind == "bank":
            output.extend(offset_gate(gate, R12.BANK_BASES[index]) for gate in local)
        elif kind in ("handoff", "relay"):
            output.extend(map_pair_gate(gate, index, kind) for gate in local)
        elif kind == "cross":
            output.append(A.cn(
                R12.LINK_BASES[index],
                R12.BANK_BASES[index + 1] + int(A.CELLS[0]["pred"][1]),
            ))
        else:
            raise ValueError(kind)
    return tuple(output)


def source_finalizer_word(_bank_count: int, deletion: str | None = None):
    """Clean success locally; leave refusal/exhaustion pending.

    DIRECTION_OK is zero after an acknowledged append and one after refusal.
    The post-update matter endpoints reconstruct POINTER/U_TO_V/V_TO_U, so
    the finalizer need not query the remote packet cell.
    """
    bank_zero = R12.BANK_BASES[0]
    marker = bank_zero + A.DIRECTION_OK
    source_pointer = R3.X.SOURCE_POINTER
    left, right = R3.X.LEFT_ENDPOINT, R3.X.RIGHT_ENDPOINT
    work = tuple(bank_zero + wire for wire in A.ZERO_WORK)
    output = [A.x(marker)]
    if deletion != "direction_cleanup":
        output.extend(A.mcx(
            (marker, source_pointer, right), bank_zero + A.U_TO_V, work
        ))
        output.extend(A.mcx(
            (marker, source_pointer, left), bank_zero + A.V_TO_U, work
        ))
    if deletion != "carrier_pointer_cleanup":
        output.append(A.tof(marker, source_pointer, bank_zero + A.POINTER))
    if deletion != "source_pointer_cleanup":
        output.extend((
            A.tof(marker, left, source_pointer),
            A.tof(marker, right, source_pointer),
        ))
    output.append(A.x(marker))
    return tuple(output)


def global_allocator_word(bank_count: int = B.BANKS, deletion: str | None = None):
    return (
        R3.source_compute_word()
        + mapped_body_word(bank_count)
        + source_finalizer_word(bank_count, deletion=deletion)
    )


def pack_state(banks, links, matter: int = 0, pointer: int = 0):
    bits = [0] * R12.TOTAL_WIRES
    for wire in range(12):
        bits[wire] = (matter >> wire) & 1
    bits[R3.X.SOURCE_POINTER] = pointer
    for base, bank in zip(R12.BANK_BASES, banks):
        for wire, value in enumerate(bank):
            bits[base + wire] = value
    for base, link in zip(R12.LINK_BASES, links):
        for wire, value in enumerate(link):
            bits[base + wire] = value
    return tuple(bits)


def unpack_state(bits, bank_count):
    banks = tuple(
        tuple(bits[base + wire] for wire in range(A.N))
        for base in R12.BANK_BASES[:bank_count]
    )
    links = tuple(
        tuple(bits[base + wire] for wire in range(B.LINK_WIDTH))
        for base in R12.LINK_BASES[:bank_count - 1]
    )
    return banks, links


def prepare_endpoint(bits, direction):
    output = list(bits)
    if output[R3.X.SOURCE_POINTER]:
        raise ValueError("source pointer pending")
    output[R3.X.LEFT_ENDPOINT] = int(direction == (0, 1))
    output[R3.X.RIGHT_ENDPOINT] = int(direction == (1, 0))
    output[R3.X.SOURCE_POINTER] = int(direction != (0, 0))
    return tuple(output)


def register_fill_certificate(bank_count: int):
    banks, links = B.chain_genesis(bank_count)
    state = pack_state(banks, links)
    word = global_allocator_word(bank_count)
    inverse = tuple(reversed(word))
    coarse = B.C704.C610.EventChain(bank=2 * bank_count)
    failures = inverse_failures = postimage_failures = 0
    maximum_residual = 0.0
    for event in range(2 * bank_count):
        direction = (1, 0) if event % 2 == 0 else (0, 1)
        before = prepare_endpoint(state, direction)
        after = A.apply_semantic(before, word)
        inverse_failures += A.apply_semantic(after, inverse) != before
        banks, links = unpack_state(after, bank_count)
        try:
            decoded, _order = B.decode_local_graph(banks, links)
        except ValueError:
            decoded = B.C704.C610.EventChain(bank=2 * bank_count)
            failures += 1
        status = coarse.admit(
            tick_id=event, orientation=1 if direction == (1, 0) else -1,
            certificate=1, binder=1, actuality=1, admissibility=1, law_domain=1,
        )
        equal = status == "admitted" and B.cell_rows(decoded) == B.cell_rows(coarse)
        failures += not equal
        maximum_residual = max(maximum_residual, 0.0 if equal else 2.0 ** 0.5)
        postimage_failures += any((
            after[R3.X.SOURCE_POINTER],
            any(banks[0][wire] for wire in (
                A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
            )),
            any(bank[wire] for bank in banks for wire in (*A.FRESH, *A.ZERO_WORK, A.TOKEN_OK)),
            any(any(link) for link in links),
        ))
        state = after
    return {
        "banks": bank_count,
        "events": 2 * bank_count,
        "intertwiner_failures": failures,
        "inverse_failures": inverse_failures,
        "lawful_postimage_failures": postimage_failures,
        "maximum_basis_residual": maximum_residual,
        "state": state,
        "chain": coarse,
    }


def exhaustion_certificate(full):
    state = full["state"]
    before = prepare_endpoint(state, (1, 0))
    word = global_allocator_word(B.BANKS)
    after = A.apply_semantic(before, word)
    banks_before, links_before = unpack_state(state, B.BANKS)
    banks_after, links_after = unpack_state(after, B.BANKS)
    persistent_before = [list(bank) for bank in banks_before]
    persistent_after = [list(bank) for bank in banks_after]
    for banks in (persistent_before, persistent_after):
        for bank in banks:
            for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK):
                bank[wire] = 0
    return {
        "packet_count_before": B.packet_count(banks_before),
        "packet_count_after": B.packet_count(banks_after),
        "persistent_bank_state_unchanged": persistent_before == persistent_after,
        "links_unchanged": links_before == links_after,
        "source_pointer_pending": bool(after[R3.X.SOURCE_POINTER]),
        "returned_pending_carrier": tuple(
            banks_after[0][wire]
            for wire in (A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK)
        ),
        "inverse_exact": A.apply_semantic(after, tuple(reversed(word))) == before,
    }


def source_truth_certificate():
    word = global_allocator_word(2)
    failures = event_rows = no_event_rows = 0
    for matter in range(1 << 12):
        left, right = (matter >> R3.X.LEFT_ENDPOINT) & 1, (matter >> R3.X.RIGHT_ENDPOINT) & 1
        pointer = left ^ right
        banks, links = B.chain_genesis(2)
        before = pack_state(banks, links, matter=matter, pointer=pointer)
        after = A.apply_semantic(before, word)
        observed_banks, observed_links = unpack_state(after, 2)
        packets = B.packet_count(observed_banks)
        if pointer:
            event_rows += 1
            expected_orientation = 1 if right and not left else -1
            packet = A.packet_projection(observed_banks[0], 0)
            failures += any((
                packets != 1,
                packet is None,
                packet is not None and packet["orientation"] != expected_orientation,
                after[R3.X.SOURCE_POINTER],
                any(observed_banks[0][wire] for wire in (
                    A.POINTER, A.U_TO_V, A.V_TO_U, A.DIRECTION_OK,
                )),
            ))
        else:
            no_event_rows += 1
            failures += any((packets, after[R3.X.SOURCE_POINTER]))
        failures += any(any(link) for link in observed_links)
    return {
        "matter_rows": 1 << 12,
        "event_rows": event_rows,
        "no_event_rows": no_event_rows,
        "failures": failures,
    }


def deletion_certificate():
    banks, links = B.chain_genesis(2)
    before = prepare_endpoint(pack_state(banks, links), (1, 0))
    complete = A.apply_semantic(before, global_allocator_word(2))
    return {
        deletion: sum(
            left != right for left, right in zip(
                complete,
                A.apply_semantic(before, global_allocator_word(2, deletion=deletion)),
            )
        )
        for deletion in (
            "direction_cleanup", "carrier_pointer_cleanup", "source_pointer_cleanup",
        )
    }


def build_physical_word(layout):
    equivalence = layout["equivalence"]
    carriers = layout["carriers"]
    repeated = layout["repeated"]
    sites = layout["wire_sites"]
    source_sites = layout["source_wire_sites"]
    target_decode = C712.synthesize_decode(equivalence.target_w, equivalence.target_v)
    target_encode = C712.inverse_word(target_decode)
    decoded, qr = C713.instrumented_decoded_word(2)
    repetition_decode = tuple(
        C712.c707.Instruction("samee_repetition_decode", carriers[index], C713.CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        C712.c707.Instruction("samee_repetition_encode", carriers[index], C713.CNOT)
        for index in reversed(repeated)
    )
    prefix = (
        repetition_decode
        + C712.abstract_to_physical(target_decode, source_sites, "samee_target_decode_")
        + C712.abstract_to_physical(decoded, source_sites, "samee_cycle713_")
    )
    semantic = global_allocator_word(B.BANKS)
    primitives = A.expanded(semantic)
    matrices = {"X": A.X, "H": A.H, "T": A.T, "TD": A.TD, "CNOT": A.CNOT}
    allocator = tuple(
        C712.c707.Instruction(
            "samee_allocator_" + kind,
            tuple(sites[wire] for wire in wires), matrices[kind],
        )
        for kind, wires in primitives
    )
    suffix = (
        C712.abstract_to_physical(target_encode, source_sites, "samee_target_encode_")
        + repetition_encode
    )
    return {
        "semantic": semantic,
        "allocator": allocator,
        "prefix": prefix,
        "suffix": suffix,
        "word": prefix + allocator + suffix,
        "decoded_gates": len(decoded),
        "coin_QR_residual": qr,
    }


def main() -> int:
    held = {size: register_fill_certificate(size) for size in (2, 5, 12)}
    exhaustion = exhaustion_certificate(held[12])
    truth = source_truth_certificate()
    deletions = deletion_certificate()
    order = B.order_certificate()
    joint = B.C704.joint_order_controls()

    layout = R12.full_wire_layout()
    built = build_physical_word(layout)
    routed, route = C712.c707.route_word(built["word"])
    inverse_routed, inverse_route = C712.c707.route_word(tuple(reversed(built["word"])))
    covariance = R12.active_frame_certificate(built["word"], routed)
    assigned = layout["assigned_sites"]
    touched = set(route["touched_coordinates"]) | set(inverse_route["touched_coordinates"])
    chain = held[12]["chain"]
    checks = {
        "same_E_held_reapplication": all(
            not row["intertwiner_failures"]
            and not row["inverse_failures"]
            and not row["lawful_postimage_failures"]
            and row["maximum_basis_residual"] == 0.0
            for row in held.values()
        ),
        "all_4096_source_rows": truth["matter_rows"] == 4096 and truth["failures"] == 0,
        "pending_exhaustion": all((
            exhaustion["packet_count_before"] == exhaustion["packet_count_after"] == 24,
            exhaustion["persistent_bank_state_unchanged"],
            exhaustion["links_unchanged"],
            exhaustion["source_pointer_pending"],
            exhaustion["returned_pending_carrier"] == (1, 1, 0, 1),
            exhaustion["inverse_exact"],
        )),
        "unchanged_Cycle610_612": all((
            (chain.interval(2, 11), chain.interval(11, 23), chain.interval(2, 23)) == (9, 12, 21),
            joint["consistent_acyclic"], joint["inverted_refusal"] == "refused_inverted",
            joint["forced_cycle_detected"],
        )),
        "active_finalizer_deletions": all(value > 0 for value in deletions.values()),
        "literal_forward_inverse_routes": all((
            route["non_NN_failures"] == inverse_route["non_NN_failures"] == 0,
            route["operand_order_failures"] == inverse_route["operand_order_failures"] == 0,
            route["route_return_failures"] == inverse_route["route_return_failures"] == 0,
            route["delete_first_swap_detected_macros"] > 0,
            inverse_route["delete_first_swap_detected_macros"] > 0,
        )),
        "active_24_576_translations": all(
            value == 0 for key, value in covariance.items() if key.endswith("failures")
        ),
        "fixed_sweep_dependence_exposed": order["failures"] == 178,
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "held": {
            size: {key: value for key, value in row.items() if key not in ("state", "chain")}
            for size, row in held.items()
        },
        "source_truth": truth,
        "exhaustion": exhaustion,
        "deletions": deletions,
        "order": order,
        "covariance": covariance,
        "route": {
            "physical_assigned_M2": len(assigned),
            "semantic_allocator_gates": len(built["semantic"]),
            "allocator_physical_primitives": len(built["allocator"]),
            "total_physical_primitives": len(built["word"]),
            "forward_routed_NN_gates": len(routed),
            "inverse_routed_NN_gates": len(inverse_routed),
            "maximum_route_distance": max(route["maximum_route_distance"], inverse_route["maximum_route_distance"]),
            "non_NN_failures": route["non_NN_failures"] + inverse_route["non_NN_failures"],
            "operand_order_failures": route["operand_order_failures"] + inverse_route["operand_order_failures"],
            "route_return_failures": route["route_return_failures"] + inverse_route["route_return_failures"],
            "forward_route_deletions": route["delete_first_swap_detected_macros"],
            "inverse_route_deletions": inverse_route["delete_first_swap_detected_macros"],
            "forward_word_sha256": route["word_sha256"],
            "inverse_word_sha256": inverse_route["word_sha256"],
            "touched_M2": len(touched),
            "blank_route_work_M2": len(touched - assigned),
            "coin_QR_residual": built["coin_QR_residual"],
        },
        "imports": {
            "acceptance_runner_sha256": sha256(Path(B.__file__).read_bytes()).hexdigest(),
            "physical_route_runner_sha256": sha256(Path(R12.__file__).read_bytes()).hexdigest(),
            "Cycle713_runner_sha256": sha256(Path(C713.__file__).read_bytes()).hexdigest(),
        },
        "supplied": [
            "clean finite 12-bank/link genesis, one-token sector, and blank route work",
            "BINDER/ACTUAL/ADMISS/LAW and the fixed outward/packet/inward factor order",
            "the Cycle713 endpoint pointer produced before the allocator word",
            "matter endpoint occupations used by the fixed bank-zero carrier copy",
        ],
        "derived": [
            "source-local success-marker-gated reversible carrier finalization",
            "post-update endpoint occupations uncompute source pointer and direction carrier",
            "transient NEW returned clean before the reverse sweep and pending retained on exhaustion",
            "same auxiliary code after every successful append through 24 events",
            "literal forward/inverse physical-M2 routes and active covariance",
        ],
        "open": [
            "autonomous preparation/enforcement of clean banks, links, token, and route work",
            "retirement of the supplied fixed outward/inward sweep if demanded by the final recurrent-law criterion",
            "positive-density or post-capacity renewal beyond the declared finite Cycle610 bank",
            "objective occurrence/admission, inaccessible inverse, permanent Record, Born/history, and source/gravity meaning",
        ],
        "boundary": (
            "The previous hosted source-finalizer defect is closed on the declared successful post-image: "
            "the literal word returns to the same clean auxiliary encoding and can be applied again after "
            "the next lawful Cycle713 endpoint.  Exhaustion retains a pending carrier.  The fixed finite "
            "outward/inward factor order and genesis remain supplied; no circuit ordinal is called time."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print("CYCLE719_SOURCE_LOCAL_FINALIZER_CORE_PASS" if report["pass"] else "CYCLE719_SOURCE_LOCAL_FINALIZER_CORE_INCOMPLETE")
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
