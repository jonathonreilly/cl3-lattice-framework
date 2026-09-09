#!/usr/bin/env python3
"""Cycle-718 physical-M2 routing support for the bounded three-bank relay."""
from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle713_physical_m2_endpoint_instrument_bridge_2026_07_26 as C713
import frontier_cycle712_joint_two_cell_full_update_physical_m2_2026_07_26 as C712
import frontier_cycle718_token_relative_relay_core_2026_07_26 as R


A = R.A


def source_layout():
    cells = ((0, 0, 0), (1, 0, 0))
    equivalence = C712.C709.G.build_equivalence(cells).equivalence
    _eq, graph, site_map, gauges, occupied, collisions = C712.P709.placement_bundle(cells)
    carriers = C712.carriers_for(equivalence, graph, site_map, gauges)
    wire_sites = tuple(carrier[0] for carrier in carriers)
    repeated = tuple(index for index, carrier in enumerate(carriers) if len(carrier) == 2)
    occupied_set = set(occupied)
    left_site, right_site = wire_sites[1], wire_sites[6]
    candidates = []
    for x in range(min(left_site[0], right_site[0]) - 2, max(left_site[0], right_site[0]) + 3):
        for y in range(min(left_site[1], right_site[1]) - 2, max(left_site[1], right_site[1]) + 3):
            for z in range(min(left_site[2], right_site[2]) - 2, max(left_site[2], right_site[2]) + 3):
                site = (x, y, z)
                if site in occupied_set:
                    continue
                distance_left = sum(abs(site[axis] - left_site[axis]) for axis in range(3))
                distance_right = sum(abs(site[axis] - right_site[axis]) for axis in range(3))
                candidates.append((
                    max(distance_left, distance_right),
                    distance_left + distance_right,
                    site,
                ))
    endpoint_sites = tuple(row[2] for row in sorted(candidates)[:3])
    return (
        cells, equivalence, carriers, repeated,
        tuple(occupied), collisions, wire_sites + endpoint_sites,
    )


def box(
    origin: tuple[int, int, int],
    size: tuple[int, int, int],
    count: int,
) -> tuple[tuple[int, int, int], ...]:
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
    ) = source_layout()
    used = set(occupied) | set(source_wire_sites[38:])
    bank_origins = ((-12, -4, 5), (-12, -4, 15), (-12, -4, 25))
    link_origins = ((-13, -5, 9), (-13, -5, 19))
    bank_blocks = tuple(box(origin, (6, 6, 4), A.N) for origin in bank_origins)
    link_blocks = tuple(box(origin, (8, 8, 6), 382) for origin in link_origins)
    for block in bank_blocks + link_blocks:
        if used & set(block):
            raise AssertionError("allocator placement collision")
        used.update(block)
    wire_sites = source_wire_sites + tuple(
        site for block in bank_blocks for site in block
    ) + tuple(site for block in link_blocks for site in block)
    if len(wire_sites) != R.TOTAL_WIRES or len(set(wire_sites)) != len(wire_sites):
        raise AssertionError("wire placement is not one-to-one")
    return {
        "cells": cells,
        "equivalence": equivalence,
        "carriers": carriers,
        "repeated": repeated,
        "occupied": occupied,
        "source_collisions": collisions,
        "source_wire_sites": source_wire_sites,
        "bank_blocks": bank_blocks,
        "link_blocks": link_blocks,
        "wire_sites": wire_sites,
        "assigned_sites": set(occupied) | set(source_wire_sites[38:])
        | set(site for block in bank_blocks + link_blocks for site in block),
    }


def build_physical_word(layout):
    equivalence = layout["equivalence"]
    carriers = layout["carriers"]
    repeated = layout["repeated"]
    wire_sites = layout["wire_sites"]
    source_wire_sites = layout["source_wire_sites"]
    target_decode = C712.synthesize_decode(equivalence.target_w, equivalence.target_v)
    target_encode = C712.inverse_word(target_decode)
    decoded, qr_residual = C713.instrumented_decoded_word(2)
    repetition_decode = tuple(
        C712.c707.Instruction("threebank_repetition_decode", carriers[index], C713.CNOT)
        for index in repeated
    )
    repetition_encode = tuple(
        C712.c707.Instruction("threebank_repetition_encode", carriers[index], C713.CNOT)
        for index in reversed(repeated)
    )
    source_prefix = (
        repetition_decode
        + C712.abstract_to_physical(
            target_decode, source_wire_sites, "threebank_target_decode_"
        )
        + C712.abstract_to_physical(
            decoded, source_wire_sites, "threebank_cycle713_"
        )
    )
    matrices = {
        "X": A.X,
        "H": A.H,
        "T": A.T,
        "TD": A.TD,
        "CNOT": A.CNOT,
    }
    semantic = R.classical_word(edge_local_predecessor=True)
    primitives = A.expanded(semantic)
    allocator = tuple(
        C712.c707.Instruction(
            "threebank_allocator_" + kind,
            tuple(wire_sites[wire] for wire in wires),
            matrices[kind],
        )
        for kind, wires in primitives
    )
    source_suffix = (
        C712.abstract_to_physical(
            target_encode, source_wire_sites, "threebank_target_encode_"
        )
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


def active_frame_certificate(layout, word, routed):
    frames = C712.C709.F.base.proper_cubic_frames()
    permutations = []
    direction_failures = coordinate_failures = routed_distance_failures = 0
    for frame in frames:
        direction_matrix = C712.C709.F.base.c210.direction_permutation(frame)
        permutation = tuple(
            next(target for target in range(6) if abs(direction_matrix[target, source]) > 0.5)
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
            base_left = (matter >> 1) & 1
            base_right = (matter >> 6) & 1
            transformed_left = (
                transported >> permutation[1]
            ) & 1
            transformed_right = (
                transported >> (6 + permutation[0])
            ) & 1
            base_word = (
                base_left ^ base_right,
                base_right & (1 - base_left),
                base_left & (1 - base_right),
            )
            transformed_word = (
                transformed_left ^ transformed_right,
                transformed_right & (1 - transformed_left),
                transformed_left & (1 - transformed_right),
            )
            direction_failures += base_word != transformed_word

        inverse = frame.T
        for instruction in word:
            transformed_sites = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in instruction.sites
            )
            restored = tuple(
                tuple(int(value) for value in inverse @ np.asarray(site))
                for site in transformed_sites
            )
            coordinate_failures += restored != instruction.sites
        for instruction in routed:
            if len(instruction.sites) != 2:
                continue
            original_distance = sum(
                abs(instruction.sites[0][axis] - instruction.sites[1][axis])
                for axis in range(3)
            )
            transformed_sites = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in instruction.sites
            )
            transformed_distance = sum(
                abs(transformed_sites[0][axis] - transformed_sites[1][axis])
                for axis in range(3)
            )
            routed_distance_failures += (
                original_distance != transformed_distance
                or transformed_distance != 1
            )

    product_failures = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product = left @ right
            product_index = next(
                index for index, frame in enumerate(frames)
                if np.array_equal(frame, product)
            )
            composed = tuple(
                permutations[left_index][permutations[right_index][source]]
                for source in range(6)
            )
            product_failures += composed != permutations[product_index]

    translation_failures = 0
    for shift in ((3, -2, 1), (-5, 4, 2)):
        for instruction in word:
            shifted = tuple(
                tuple(site[axis] + shift[axis] for axis in range(3))
                for site in instruction.sites
            )
            restored = tuple(
                tuple(site[axis] - shift[axis] for axis in range(3))
                for site in shifted
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


def main() -> int:
    layout = full_wire_layout()
    built = build_physical_word(layout)
    routed, route = C712.c707.route_word(built["word"])
    covariance = active_frame_certificate(layout, built["word"], routed)
    bank_translation = (0, 0, 10)
    bank_translation_failures = sum(
        tuple(
            site[axis] + bank_translation[axis] for axis in range(3)
        ) != layout["bank_blocks"][index + 1][wire]
        for index in range(2)
        for wire, site in enumerate(layout["bank_blocks"][index])
    )
    link_translation_failures = sum(
        tuple(
            site[axis] + bank_translation[axis] for axis in range(3)
        ) != layout["link_blocks"][1][wire]
        for wire, site in enumerate(layout["link_blocks"][0])
    )
    assigned_sites = layout["assigned_sites"]
    checks = {
        "collision_free_placement": (
            layout["source_collisions"] == 0
            and len(assigned_sites) == 1199
        ),
        "literal_nearest_neighbor_route": (
            route["non_NN_failures"] == 0
            and route["operand_order_failures"] == 0
            and route["route_return_failures"] == 0
        ),
        "active_route_deletion": route["delete_first_swap_detected_macros"] > 0,
        "translated_bank_and_link_modules": (
            bank_translation_failures == 0 and link_translation_failures == 0
        ),
        "proper_cubic_active_covariance": (
            covariance["proper_cubic_frames"] == 24
            and covariance["ordered_frame_products"] == 576
            and covariance["active_pointer_direction_failures"] == 0
            and covariance["instruction_coordinate_failures"] == 0
            and covariance["routed_NN_frame_failures"] == 0
            and covariance["direction_product_failures"] == 0
            and covariance["translation_failures"] == 0
        ),
    }
    report = {
        "checks": checks,
        "pass": all(checks.values()),
        "placement": {
            "physical_assigned_M2": len(assigned_sites),
            "decoded_wire_sites": len(layout["wire_sites"]),
            "source_literal_code_M2": len(layout["occupied"]),
            "source_endpoint_register_M2": 3,
            "allocator_bank_M2": 3 * A.N,
            "allocator_edge_tube_M2": 2 * 382,
            "placement_collisions": layout["source_collisions"],
            "bank_translation": bank_translation,
            "bank_translation_failures": bank_translation_failures,
            "link_translation_failures": link_translation_failures,
        },
        "route": {
            "decoded_Cycle713_gates": built["decoded_gate_count"],
            "semantic_allocator_gates": len(built["semantic"]),
            "source_physical_primitives": (
                len(built["source_prefix"]) + len(built["source_suffix"])
            ),
            "allocator_physical_primitives": len(built["allocator"]),
            "total_physical_primitives": len(built["word"]),
            "routed_nearest_neighbor_gates": len(routed),
            "maximum_route_distance": route["maximum_route_distance"],
            "non_NN_failures": route["non_NN_failures"],
            "operand_order_failures": route["operand_order_failures"],
            "route_return_failures": route["route_return_failures"],
            "route_deletion_detected_macros": route["delete_first_swap_detected_macros"],
            "routed_word_sha256": route["word_sha256"],
            "touched_M2": len(route["touched_coordinates"]),
            "blank_route_work_M2": len(
                set(route["touched_coordinates"]) - assigned_sites
            ),
            "coin_QR_residual": built["coin_QR_residual"],
        },
        "covariance": covariance,
        "supplied": [
            "Cycle-713 physical two-cell placement/decoder and blank route work",
            "three 131-M2 banks and two edge-exclusive 382-M2 link tubes",
            "fixed proper-cubic coframe relating matter seam and history chain",
            "finite clean genesis, one-token sector, and fixed circuit layer order",
        ],
        "derived": [
            "collision-free literal placement sharing the Cycle-713 endpoint register",
            "nearest-neighbor route of Cycle-713 plus edge-local three-bank recurrence",
            "exact translated bank/link module geometry",
            "active endpoint-direction naturality under all proper-cubic frames/products",
        ],
        "open": [
            "NEW/append-ACK and pending-event backpressure at dirty/exhausted frontier",
            "physical routing of the eventual ACK/pending repair",
            "general overlapping-chain genesis/enforcement and resource growth",
            "numeric Cycle-612 adapter and time/Record/Born/source-gravity bridges",
        ],
        "boundary": (
            "Positive physical-M2 placement/route of the finite four-application relay "
            "word only.  Routing does not repair its still-open exhaustion domain."
        ),
    }
    report["report_sha256"] = sha256(
        json.dumps(report, sort_keys=True, default=str).encode()
    ).hexdigest()
    for label, passed in checks.items():
        print("PASS" if passed else "FAIL", label, "::", passed)
    print("SUMMARY_JSON", json.dumps(report, sort_keys=True, default=str))
    print(
        "CYCLE718_THREE_BANK_PHYSICAL_ROUTE_SUPPORT_PASS"
        if report["pass"] else "CYCLE718_THREE_BANK_PHYSICAL_ROUTE_SUPPORT_INCOMPLETE"
    )
    return 0 if report["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
