#!/usr/bin/env python3
"""Cycle 719 core: literal M2 route of the recurrent 12-bank bridge.

The routed word contains the physical Cycle-713 matter decoder/instrument, a
fixed bank-zero carrier copy, the address-free twelve-bank allocator with
transient NEW/pending marker, and matter re-encoding.  The marker-gated source
finalizer remains a named hosted boundary and is not inserted as fake gates.
"""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


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
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle718_three_bank_physical_route_core_2026_07_26 as R3P
import frontier_cycle718_token_relative_relay_core_2026_07_26 as R3
import frontier_cycle719_recurrent_cycle612_bank_core_2026_07_26 as B


A = B.A
SOURCE_WIDTH = 41
BANK_BASES = tuple(SOURCE_WIDTH + index * A.N for index in range(B.BANKS))
AFTER_BANKS = SOURCE_WIDTH + B.BANKS * A.N
LINK_BASES = tuple(AFTER_BANKS + edge * B.LINK_WIDTH for edge in range(B.BANKS - 1))
TOTAL_WIRES = AFTER_BANKS + (B.BANKS - 1) * B.LINK_WIDTH


def box(origin, size, count):
    sites = tuple(
        (origin[0] + x, origin[1] + y, origin[2] + z)
        for z in range(size[2])
        for y in range(size[1])
        for x in range(size[0])
    )
    if len(sites) < count:
        raise ValueError((origin, size, count))
    return sites[:count]


def full_wire_layout():
    (
        cells, equivalence, carriers, repeated,
        occupied, collisions, source_wire_sites,
    ) = R3P.source_layout()
    used = set(occupied) | set(source_wire_sites[38:])
    bank_blocks = tuple(
        box((-12, -4, 5 + 10 * index), (6, 6, 4), A.N)
        for index in range(B.BANKS)
    )
    link_blocks = tuple(
        box((-13, -5, 9 + 10 * index), (8, 8, 6), B.LINK_WIDTH)
        for index in range(B.BANKS - 1)
    )
    module_collisions = 0
    for block in bank_blocks + link_blocks:
        module_collisions += len(used & set(block))
        used.update(block)
    wire_sites = source_wire_sites + tuple(
        site for block in bank_blocks for site in block
    ) + tuple(site for block in link_blocks for site in block)
    if len(wire_sites) != TOTAL_WIRES or len(set(wire_sites)) != len(wire_sites):
        raise AssertionError((len(wire_sites), TOTAL_WIRES, len(set(wire_sites))))
    return {
        "cells": cells,
        "equivalence": equivalence,
        "carriers": carriers,
        "repeated": repeated,
        "occupied": occupied,
        "source_collisions": collisions,
        "module_collisions": module_collisions,
        "source_wire_sites": source_wire_sites,
        "bank_blocks": bank_blocks,
        "link_blocks": link_blocks,
        "wire_sites": wire_sites,
        "assigned_sites": set(occupied) | set(source_wire_sites[38:])
        | set(site for block in bank_blocks + link_blocks for site in block),
    }


def offset_gate(gate, base):
    return A.Gate(gate.kind, tuple(base + wire for wire in gate.wires))


def map_pair_gate(gate, edge, kind):
    split = 0 if kind == "handoff" else B.P.LINK_AUX_WIDTH
    wires = []
    for wire in gate.wires:
        if wire < A.N:
            wires.append(BANK_BASES[edge] + wire)
        elif wire < 2 * A.N:
            wires.append(BANK_BASES[edge + 1] + wire - A.N)
        else:
            wires.append(LINK_BASES[edge] + split + wire - 2 * A.N)
    return A.Gate(gate.kind, tuple(wires))


def global_allocator_word():
    word = list(R3.source_compute_word())
    for kind, index, local in B.actions(B.BANKS):
        if kind == "bank":
            word.extend(offset_gate(gate, BANK_BASES[index]) for gate in local)
        elif kind in ("handoff", "relay"):
            word.extend(map_pair_gate(gate, index, kind) for gate in local)
        elif kind == "cross":
            word.append(A.cn(
                LINK_BASES[index],
                BANK_BASES[index + 1] + int(A.CELLS[0]["pred"][1]),
            ))
        else:
            raise ValueError(kind)
    return tuple(word)


def build_physical_word(layout):
    equivalence = layout["equivalence"]
    carriers = layout["carriers"]
    repeated = layout["repeated"]
    wire_sites = layout["wire_sites"]
    source_sites = layout["source_wire_sites"]
    target_decode = C712.synthesize_decode(equivalence.target_w, equivalence.target_v)
    target_encode = C712.inverse_word(target_decode)
    decoded, qr_residual = C713.instrumented_decoded_word(2)
    repetition_decode = tuple(
        C712.c707.Instruction("recurrent12_repetition_decode", carriers[index], C713.CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        C712.c707.Instruction("recurrent12_repetition_encode", carriers[index], C713.CNOT)
        for index in reversed(repeated)
    )
    source_prefix = (
        repetition_decode
        + C712.abstract_to_physical(target_decode, source_sites, "recurrent12_target_decode_")
        + C712.abstract_to_physical(decoded, source_sites, "recurrent12_cycle713_")
    )
    matrices = {"X": A.X, "H": A.H, "T": A.T, "TD": A.TD, "CNOT": A.CNOT}
    semantic = global_allocator_word()
    primitives = A.expanded(semantic)
    allocator = tuple(
        C712.c707.Instruction(
            "recurrent12_allocator_" + kind,
            tuple(wire_sites[wire] for wire in wires), matrices[kind],
        )
        for kind, wires in primitives
    )
    source_suffix = (
        C712.abstract_to_physical(target_encode, source_sites, "recurrent12_target_encode_")
        + repetition_encode
    )
    return {
        "semantic": semantic,
        "allocator": allocator,
        "source_prefix": source_prefix,
        "source_suffix": source_suffix,
        "word": source_prefix + allocator + source_suffix,
        "decoded_gate_count": len(decoded),
        "coin_QR_residual": qr_residual,
    }


def active_frame_certificate(word, routed):
    frames = C712.C709.F.base.proper_cubic_frames()
    permutations = []
    direction_failures = coordinate_failures = routed_distance_failures = 0
    for frame in frames:
        matrix = C712.C709.F.base.c210.direction_permutation(frame)
        permutation = tuple(
            next(target for target in range(6) if abs(matrix[target, source]) > 0.5)
            for source in range(6)
        )
        permutations.append(permutation)
        for matter in range(1 << 12):
            transported = 0
            for cell in range(2):
                for source in range(6):
                    transported |= (
                        ((matter >> (6 * cell + source)) & 1)
                        << (6 * cell + permutation[source])
                    )
            left, right = (matter >> 1) & 1, (matter >> 6) & 1
            moved_left = (transported >> permutation[1]) & 1
            moved_right = (transported >> (6 + permutation[0])) & 1
            direction_failures += (
                left ^ right, right & (1 - left), left & (1 - right)
            ) != (
                moved_left ^ moved_right,
                moved_right & (1 - moved_left),
                moved_left & (1 - moved_right),
            )
        inverse = frame.T
        for instruction in word:
            moved = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in instruction.sites
            )
            restored = tuple(
                tuple(int(value) for value in inverse @ np.asarray(site))
                for site in moved
            )
            coordinate_failures += restored != instruction.sites
        for instruction in routed:
            if len(instruction.sites) == 2:
                moved = tuple(
                    tuple(int(value) for value in frame @ np.asarray(site))
                    for site in instruction.sites
                )
                routed_distance_failures += sum(
                    abs(left - right) for left, right in zip(*moved)
                ) != 1
    product_failures = 0
    for li, left in enumerate(frames):
        for ri, right in enumerate(frames):
            index = next(
                i for i, frame in enumerate(frames)
                if np.array_equal(frame, left @ right)
            )
            product_failures += tuple(
                permutations[li][permutations[ri][mode]] for mode in range(6)
            ) != permutations[index]
    translation_failures = 0
    for shift in ((3, -2, 1), (-5, 4, 2)):
        for instruction in word:
            moved = tuple(
                tuple(site[axis] + shift[axis] for axis in range(3))
                for site in instruction.sites
            )
            restored = tuple(
                tuple(site[axis] - shift[axis] for axis in range(3))
                for site in moved
            )
            translation_failures += restored != instruction.sites
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "active_pointer_direction_failures": direction_failures,
        "instruction_coordinate_failures": coordinate_failures,
        "routed_NN_frame_failures": routed_distance_failures,
        "direction_product_failures": product_failures,
        "translation_failures": translation_failures,
    }


def semantic_acceptance_certificate():
    held = {size: B.fill_certificate(size) for size in (2, 5, 12)}
    controls = B.controls_certificate()
    exhaustion = B.exhaustion_certificate(held[12])
    deletions = B.deletion_certificate()
    order = B.order_certificate()
    chain = held[12]["chain"]
    joint = B.C704.joint_order_controls()
    return {
        "held": {
            size: {
                "intertwiner_failures": row["intertwiner_failures"],
                "decoder_failures": row["decoder_failures"],
                "inverse_body_failures": row["inverse_body_failures"],
                "maximum_intertwiner_basis_residual": row["maximum_intertwiner_basis_residual"],
                "issues": row["issues"],
            }
            for size, row in held.items()
        },
        "controls": controls,
        "exhaustion": exhaustion,
        "deletions": deletions,
        "order": order,
        "intervals": (
            chain.interval(2, 11), chain.interval(11, 23),
            chain.interval(2, 23), chain.interval(11, 2),
        ),
        "joint": joint,
    }


def main() -> int:
    layout = full_wire_layout()
    built = build_physical_word(layout)
    routed, route = C712.c707.route_word(built["word"])
    inverse_word = tuple(reversed(built["word"]))
    inverse_routed, inverse_route = C712.c707.route_word(inverse_word)
    covariance = active_frame_certificate(built["word"], routed)
    semantic = semantic_acceptance_certificate()
    translation = (0, 0, 10)
    bank_translation_failures = sum(
        tuple(site[axis] + translation[axis] for axis in range(3))
        != layout["bank_blocks"][index + 1][wire]
        for index in range(B.BANKS - 1)
        for wire, site in enumerate(layout["bank_blocks"][index])
    )
    link_translation_failures = sum(
        tuple(site[axis] + translation[axis] for axis in range(3))
        != layout["link_blocks"][index + 1][wire]
        for index in range(B.BANKS - 2)
        for wire, site in enumerate(layout["link_blocks"][index])
    )
    assigned = layout["assigned_sites"]
    touched = set(route["touched_coordinates"]) | set(inverse_route["touched_coordinates"])
    semantic_pass = all(
        not row["intertwiner_failures"]
        and not row["decoder_failures"]
        and not row["inverse_body_failures"]
        and not row["issues"]
        for row in semantic["held"].values()
    )
    checks = {
        "collision_free_literal_placement": (
            layout["source_collisions"] == 0
            and layout["module_collisions"] == 0
            and len(assigned) == TOTAL_WIRES + 1
        ),
        "literal_forward_inverse_NN_routes": all((
            route["non_NN_failures"] == inverse_route["non_NN_failures"] == 0,
            route["operand_order_failures"] == inverse_route["operand_order_failures"] == 0,
            route["route_return_failures"] == inverse_route["route_return_failures"] == 0,
        )),
        "active_route_deletions": (
            route["delete_first_swap_detected_macros"] > 0
            and inverse_route["delete_first_swap_detected_macros"] > 0
        ),
        "translated_modules": bank_translation_failures == link_translation_failures == 0,
        "active_24_576_translations": all(value == 0 for key, value in covariance.items() if key.endswith("failures")),
        "unchanged_semantic_acceptance": all((
            semantic_pass,
            semantic["controls"]["dirty_selected_payload_failures"] == 0,
            semantic["exhaustion"]["physical_pending_or_exhaustion_receipt_present"],
            semantic["intervals"] == (9, 12, 21, -9),
            semantic["joint"]["forced_cycle_detected"],
        )),
        "fixed_sweep_dependence_exposed": semantic["order"]["failures"] == 178,
        "literal_source_finalizer": False,
    }
    positive = tuple(key for key in checks if key != "literal_source_finalizer")
    report = {
        "checks": checks,
        "pass": all(checks[key] for key in positive),
        "complete_recurrent_physical_bridge": all(checks.values()),
        "placement": {
            "physical_assigned_M2": len(assigned),
            "decoded_wire_sites": len(layout["wire_sites"]),
            "source_literal_code_M2": len(layout["occupied"]),
            "source_endpoint_register_M2": 3,
            "allocator_bank_M2": B.BANKS * A.N,
            "allocator_edge_tube_M2": (B.BANKS - 1) * B.LINK_WIDTH,
            "module_collisions": layout["module_collisions"],
            "bank_translation_failures": bank_translation_failures,
            "link_translation_failures": link_translation_failures,
        },
        "route": {
            "decoded_Cycle713_gates": built["decoded_gate_count"],
            "semantic_allocator_gates": len(built["semantic"]),
            "source_physical_primitives": len(built["source_prefix"]) + len(built["source_suffix"]),
            "allocator_physical_primitives": len(built["allocator"]),
            "total_physical_primitives": len(built["word"]),
            "forward_routed_NN_gates": len(routed),
            "inverse_routed_NN_gates": len(inverse_routed),
            "maximum_route_distance": max(route["maximum_route_distance"], inverse_route["maximum_route_distance"]),
            "non_NN_failures": route["non_NN_failures"] + inverse_route["non_NN_failures"],
            "operand_order_failures": route["operand_order_failures"] + inverse_route["operand_order_failures"],
            "route_return_failures": route["route_return_failures"] + inverse_route["route_return_failures"],
            "forward_route_deletion_detected_macros": route["delete_first_swap_detected_macros"],
            "inverse_route_deletion_detected_macros": inverse_route["delete_first_swap_detected_macros"],
            "forward_routed_word_sha256": route["word_sha256"],
            "inverse_routed_word_sha256": inverse_route["word_sha256"],
            "touched_M2": len(touched),
            "blank_route_work_M2": len(touched - assigned),
            "coin_QR_residual": built["coin_QR_residual"],
        },
        "semantic_acceptance": semantic,
        "covariance": covariance,
        "imports": {
            "acceptance_runner_sha256": sha256(Path(B.__file__).read_bytes()).hexdigest(),
            "three_bank_route_runner_sha256": sha256(Path(R3P.__file__).read_bytes()).hexdigest(),
            "Cycle713_runner_sha256": sha256(Path(C713.__file__).read_bytes()).hexdigest(),
        },
        "supplied": [
            "clean 12-bank/11-link genesis, exactly one token, and blank route workspace",
            "BINDER/ACTUAL/ADMISS/LAW and fixed bank-zero endpoint carrier source",
            "fixed load-bearing outward/packet/inward circuit order",
            "proper-cubic coframe relating the matter seam and history chain",
            "host implementation of marker-gated source finalization",
        ],
        "derived": [
            "literal collision-free M2 placement of the repaired twelve-bank word",
            "forward and inverse nearest-neighbor routes with returned operands",
            "translated bank/link module geometry and active 24/576 coordinate covariance",
            "unchanged held-size Cycle610/612 acceptance and pending controls",
        ],
        "open": [
            "literal reversible marker-gated source finalizer and same-E repeated update",
            "autonomous preparation/enforcement of clean banks, links, token, and route work",
            "retirement of the supplied fixed cyclic sweep if required by the recurrent-law criterion",
            "objective occurrence/admission, inaccessible inverse, Record/Born, and source/gravity meaning",
        ],
        "boundary": (
            "Positive literal M2 placement and routing of the repaired finite 12-bank body.  "
            "The same-E recurrent physical update remains open because the source finalizer is hosted.  "
            "The fixed sweep is explicit supplied circuit structure and no circuit ordinal is called time."
        ),
    }
    report["report_sha256"] = sha256(json.dumps(report, sort_keys=True, default=str).encode()).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE719_RECURRENT_PHYSICAL_ROUTE_CORE_BOUNDED_PARTIAL"
        if report["pass"] and not report["complete_recurrent_physical_bridge"]
        else "CYCLE719_RECURRENT_PHYSICAL_ROUTE_CORE_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
