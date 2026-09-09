#!/usr/bin/env python3
"""Literal Cycle707 M2 lift and routed Clifford words for Cycle709."""

from __future__ import annotations

from collections import Counter
from itertools import product
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle709_local_seam_clifford_core_2026_07_26 as C


G = C.G
c707 = G.c707
route = G.route
Coord = tuple[int, int, int]


def c707_edge_key(graph, edge: int):
    u, v, kind, _owner = graph.edges[edge]
    return frozenset((graph.vertices[u], graph.vertices[v])), kind


def placement_bundle(cells, origin=(0, 0, 0)):
    C.canonical_box_shape(tuple(cells))
    equivalence = G.build_equivalence(tuple(cells)).equivalence
    graph = c707.PatchGraph(tuple(cells))
    site_map, gauges = c707.placement(
        graph, origin=origin, include_edge_gauge=True
    )
    occupied = c707.occupied_sites(site_map, gauges)
    collisions = sum(len(sites) for sites in site_map.values()) + len(gauges) - len(occupied)
    return equivalence, graph, site_map, gauges, tuple(sorted(occupied)), collisions


def rail_sites(equivalence, graph, gauges) -> tuple[Coord, ...]:
    seam_to_site = {
        (source, axis): gauges[edge]
        for edge, source, _target, _smode, _tmode, axis in graph.stream_edges
    }
    return tuple(seam_to_site[C.seam_key(label)] for label in equivalence.rail_labels)


def physical_lift(row, equivalence, graph, site_map, gauges):
    all_sites = tuple(sorted(c707.occupied_sites(site_map, gauges)))
    site_index = {site: index for index, site in enumerate(all_sites)}
    graph_lookup = {
        c707_edge_key(graph, edge): edge for edge in range(len(graph.edges))
    }
    patch = len(equivalence.patch_graph.edges)
    x = z = 0
    for patch_edge in range(patch):
        graph_edge = graph_lookup[G.c706.edge_key(equivalence.patch_graph, patch_edge)]
        carriers = site_map[graph_edge]
        if (row.x >> patch_edge) & 1:
            for site in carriers:
                x |= 1 << site_index[site]
        if (row.z >> patch_edge) & 1:
            z |= 1 << site_index[carriers[0]]
    for rail, site in enumerate(rail_sites(equivalence, graph, gauges)):
        source = patch + rail
        target = site_index[site]
        x |= ((row.x >> source) & 1) << target
        z |= ((row.z >> source) & 1) << target
    return c707.Pauli(row.phase, x, z), all_sites


def repetition_failures(row, graph, site_map, all_sites) -> int:
    index = {site: position for position, site in enumerate(all_sites)}
    failures = 0
    for edge, *_rest in graph.stream_edges:
        left, right = site_map[edge]
        stabilizer = c707.Pauli(z=(1 << index[left]) | (1 << index[right]))
        failures += not row.commutes(stabilizer)
    return failures


def restrict_pauli(row, all_sites, support):
    lookup = {site: index for index, site in enumerate(support)}
    x = z = 0
    for source, site in enumerate(all_sites):
        if site in lookup:
            target = lookup[site]
            x |= ((row.x >> source) & 1) << target
            z |= ((row.z >> source) & 1) << target
    return c707.Pauli(row.phase, x, z)


def compile_clifford_rotation(row, sites, rotation_sign: int):
    """Compile exp(-i rotation_sign*pi*row/4) with Clifford primitives."""
    axes, pauli_sign = c707.pauli_axes(row, sites)
    effective_sign = rotation_sign * pauli_sign
    pivot = axes[0][0]
    word = []
    for site, axis in axes:
        if axis == "X":
            word.append(c707.Instruction("basis_H", (site,), c707.c655.H))
        elif axis == "Y":
            word.append(c707.Instruction("basis_Sdg", (site,), c707.SDG_GATE))
            word.append(c707.Instruction("basis_H", (site,), c707.c655.H))
    for site, _axis in axes[1:]:
        word.append(c707.Instruction("parity_CNOT", (site, pivot), c707.c655.CNOT))
    if effective_sign == 1:
        word.append(c707.Instruction("phase_S", (pivot,), c707.S_GATE))
    else:
        word.append(c707.Instruction("phase_Sdg", (pivot,), c707.SDG_GATE))
    for site, _axis in reversed(axes[1:]):
        word.append(c707.Instruction("parity_CNOT", (site, pivot), c707.c655.CNOT))
    for site, axis in reversed(axes):
        if axis == "X":
            word.append(c707.Instruction("basis_H", (site,), c707.c655.H))
        elif axis == "Y":
            word.append(c707.Instruction("basis_H", (site,), c707.c655.H))
            word.append(c707.Instruction("basis_S", (site,), c707.S_GATE))
    return tuple(word)


def execute_word(state, word, sites):
    index = {site: wire for wire, site in enumerate(sites)}
    output = state
    for instruction in word:
        output = c707.apply_gate(
            output,
            instruction.matrix,
            tuple(index[site] for site in instruction.sites),
            len(sites),
        )
    return output


def phase_aligned_residual(observed, expected) -> float:
    overlap = np.vdot(expected, observed)
    phase = overlap / abs(overlap) if abs(overlap) else 1.0
    return float(np.linalg.norm(observed - phase * expected))


def compile_factor_rows(rows, signs, all_sites):
    support = tuple(
        site for index, site in enumerate(all_sites)
        if any(((row.x | row.z) >> index) & 1 for row in rows)
    )
    local = tuple(restrict_pauli(row, all_sites, support) for row in rows)
    word = tuple(
        instruction
        for row, sign in zip(local, signs)
        for instruction in compile_clifford_rotation(row, support, sign)
    )
    return local, support, word


def reference_certificate() -> dict[str, object]:
    cells = ((0, 0, 0), (1, 0, 0))
    eq, graph, site_map, gauges, all_sites, collisions = placement_bundle(cells)
    factors = C.seam_factors(eq, (0, 0, 0), 0)
    physical = tuple(
        physical_lift(row, eq, graph, site_map, gauges)[0] for row in factors
    )
    local, support, word = compile_factor_rows(physical, C.ROTATION_SIGNS, all_sites)
    rng = np.random.default_rng(709)
    residuals = []
    direct_states = []
    input_states = []
    for sample in range(3):
        if sample == 0:
            state = np.zeros(1 << len(support), dtype=complex)
            state[0] = 1
        else:
            state = rng.normal(size=1 << len(support)) + 1j * rng.normal(size=1 << len(support))
            state /= np.linalg.norm(state)
        direct = state
        for row, sign in zip(local, C.ROTATION_SIGNS):
            direct = c707.direct_rotation(direct, row, sign * math.pi / 2, len(support))
        compiled = execute_word(state, word, support)
        residuals.append(phase_aligned_residual(compiled, direct))
        direct_states.append(direct)
        input_states.append(state)
    deletion_residuals = {}
    for kind in sorted({instruction.kind for instruction in word}):
        deleted = tuple(instruction for instruction in word if instruction.kind != kind)
        deletion_residuals[kind] = phase_aligned_residual(
            execute_word(input_states[-1], deleted, support), direct_states[-1]
        )
    routed, route_report = c707.route_word(word)
    endpoints = {site for instruction in word for site in instruction.sites}
    touched = set(route_report["touched_coordinates"])
    inverse_local_residual = max(
        float(np.linalg.norm(gate.matrix.conj().T @ gate.matrix - np.eye(gate.matrix.shape[0])))
        for gate in routed
    )
    cleanup_h = np.kron(c707.c655.H, c707.c655.I2)
    cleanup_cz_residual = float(np.linalg.norm(
        cleanup_h @ c707.c655.CNOT @ cleanup_h
        - np.diag((1, 1, 1, -1))
    ))
    return {
        "abstract_qubits": eq.qubits,
        "literal_M2": len(all_sites),
        "placement_collisions": collisions,
        "abstract_factor_weights": tuple((row.x | row.z).bit_count() for row in factors),
        "physical_factor_weights": tuple((row.x | row.z).bit_count() for row in physical),
        "factor_union_M2": len(support),
        "repetition_stabilizer_failures": sum(
            repetition_failures(row, graph, site_map, all_sites) for row in physical
        ),
        "primitive_gate_count": len(word),
        "primitive_kind_census": dict(Counter(instruction.kind for instruction in word)),
        "maximum_state_residual_up_to_global_phase": max(residuals),
        "delete_primitive_kind_residuals": deletion_residuals,
        "routed_gate_count": len(routed),
        "routed_kind_census": dict(Counter(gate.kind for gate in routed)),
        "maximum_route_distance": route_report["maximum_route_distance"],
        "non_NN_failures": route_report["non_NN_failures"],
        "operand_order_failures": route_report["operand_order_failures"],
        "route_return_failures": route_report["route_return_failures"],
        "delete_first_swap_detected_macros": route_report["delete_first_swap_detected_macros"],
        "occupied_spectator_sites_traversed_and_returned": len(
            (touched & set(all_sites)) - endpoints
        ),
        "maximum_local_gate_inverse_residual": inverse_local_residual,
        "H_CNOT_H_minus_CZ_residual": cleanup_cz_residual,
        "routed_word_sha256": route_report["word_sha256"],
        "reference_route_geometry_covariance": covariance_certificate(routed),
        "routed_word": routed,
    }


def axis_physical_certificates() -> tuple[dict[str, object], ...]:
    rows = []
    for axis in range(3):
        endpoint = tuple(int(index == axis) for index in range(3))
        cells = ((0, 0, 0), endpoint)
        eq, graph, site_map, gauges, all_sites, collisions = placement_bundle(cells)
        factors = C.seam_factors(eq, (0, 0, 0), axis)
        physical = tuple(
            physical_lift(row, eq, graph, site_map, gauges)[0] for row in factors
        )
        local, support, word = compile_factor_rows(
            physical, C.ROTATION_SIGNS, all_sites
        )
        rng = np.random.default_rng(709 + axis)
        state = rng.normal(size=1 << len(support)) + 1j * rng.normal(size=1 << len(support))
        state /= np.linalg.norm(state)
        direct = state
        for row, sign in zip(local, C.ROTATION_SIGNS):
            direct = c707.direct_rotation(
                direct, row, sign * math.pi / 2, len(support)
            )
        routed, route_report = c707.route_word(word)
        rows.append({
            "axis": axis,
            "literal_M2": len(all_sites),
            "placement_collisions": collisions,
            "abstract_factor_weights": tuple((row.x | row.z).bit_count() for row in factors),
            "physical_factor_weights": tuple((row.x | row.z).bit_count() for row in physical),
            "repetition_stabilizer_failures": sum(
                repetition_failures(row, graph, site_map, all_sites) for row in physical
            ),
            "state_residual_up_to_global_phase": phase_aligned_residual(
                execute_word(state, word, support), direct
            ),
            "primitive_gate_count": len(word),
            "routed_gate_count": len(routed),
            "non_NN_failures": route_report["non_NN_failures"],
            "operand_order_failures": route_report["operand_order_failures"],
            "route_return_failures": route_report["route_return_failures"],
        })
    return tuple(rows)


def placement_scaling_certificate() -> tuple[dict[str, object], ...]:
    rows = []
    for shape in ((2, 2, 2), (3, 2, 2), (4, 2, 2), (3, 3, 2), (3, 3, 3)):
        cells = G.box_cells(shape)
        eq, _graph, _site_map, _gauges, sites, collisions = placement_bundle(cells)
        seams = len(eq.rail_labels)
        rows.append({
            "shape": shape,
            "cells": len(cells),
            "seams": seams,
            "literal_M2": len(sites),
            "formula_18N_plus_3M": 18 * len(cells) + 3 * seams,
            "constant_bound_27N": 27 * len(cells),
            "placement_collisions": collisions,
            "parameters_refit": 0,
        })
    return tuple(rows)


def greedy_cleanup_colours(edges):
    colours = []
    for edge in edges:
        unavailable = {
            colour for prior, colour in zip(edges[:len(colours)], colours)
            if set(prior) & set(edge)
        }
        colours.append(next(colour for colour in range(4) if colour not in unavailable))
    return tuple(colours)


def primary_word():
    cells = G.box_cells((3, 2, 2))
    eq, graph, site_map, gauges, all_sites, collisions = placement_bundle(cells)
    seams = tuple(
        (cell, axis) for cell, axis, _matter, _reference in eq.open_graph.cross_edges
    )
    by_colour = {colour: [] for colour in C.ALL_COLOURS}
    for seam in seams:
        by_colour[C.seam_colour(seam)].append(seam)
    word = []
    physical_rows = []
    same_colour_support_collisions = 0
    for colour in C.ALL_COLOURS:
        layer_supports = []
        for cell, axis in by_colour[colour]:
            factors = C.seam_factors(eq, cell, axis)
            physical = tuple(
                physical_lift(row, eq, graph, site_map, gauges)[0] for row in factors
            )
            physical_rows.extend(physical)
            support = {
                all_sites[index]
                for row in physical
                for index in range(len(all_sites))
                if ((row.x | row.z) >> index) & 1
            }
            same_colour_support_collisions += sum(bool(support & prior) for prior in layer_supports)
            layer_supports.append(support)
            _local, _support, seam_word = compile_factor_rows(
                physical, C.ROTATION_SIGNS, all_sites
            )
            word.extend(seam_word)
    composition = C.coloured_composition(cells)
    rails = rail_sites(eq, graph, gauges)
    for site in rails:
        word.append(c707.Instruction("cleanup_outer_H", (site,), c707.c655.H))
    cleanup_colours = greedy_cleanup_colours(composition.cleanup)
    for colour in range(max(cleanup_colours, default=-1) + 1):
        for (left, right), edge_colour in zip(composition.cleanup, cleanup_colours):
            if edge_colour != colour:
                continue
            target = rails[right]
            word.append(c707.Instruction("cleanup_CZ_H", (target,), c707.c655.H))
            word.append(c707.Instruction(
                "cleanup_CZ_CNOT", (rails[left], target), c707.c655.CNOT
            ))
            word.append(c707.Instruction("cleanup_CZ_H", (target,), c707.c655.H))
    for site in rails:
        word.append(c707.Instruction("cleanup_outer_H", (site,), c707.c655.H))
    return {
        "cells": cells,
        "equivalence": eq,
        "graph": graph,
        "site_map": site_map,
        "gauges": gauges,
        "all_sites": all_sites,
        "placement_collisions": collisions,
        "physical_factor_rows": tuple(physical_rows),
        "same_colour_support_collisions": same_colour_support_collisions,
        "cleanup_edge_colours": cleanup_colours,
        "word": tuple(word),
        "composition": composition,
    }


def address_placement(equivalence, graph, site_map, gauges):
    graph_lookup = {
        c707_edge_key(graph, edge): edge for edge in range(len(graph.edges))
    }
    output = {}
    for edge in range(len(equivalence.patch_graph.edges)):
        key = ("edge", G.c706.edge_key(equivalence.patch_graph, edge))
        output[key] = site_map[graph_lookup[key[1]]]
    for label, site in zip(equivalence.rail_labels, rail_sites(equivalence, graph, gauges)):
        output[("rail", label)] = (site,)
    return output


def overlap_certificate(primary) -> dict[str, object]:
    left_cells = G.box_cells((2, 2, 2))
    right_cells = tuple((x + 1, y, z) for x, y, z in G.box_cells((2, 2, 2)))
    left = placement_bundle(left_cells, origin=(-8, 0, 0))
    right = placement_bundle(right_cells, origin=(8, 0, 0))
    left_map = address_placement(*left[:4])
    right_map = address_placement(*right[:4])
    primary_map = address_placement(
        primary["equivalence"], primary["graph"], primary["site_map"], primary["gauges"]
    )
    shared_addresses = set(left_map) & set(right_map)
    return {
        "left_cube_M2": len(left[4]),
        "right_cube_M2": len(right[4]),
        "cube_overlap_M2": len(set(left[4]) & set(right[4])),
        "cube_union_M2": len(set(left[4]) | set(right[4])),
        "primary_M2": len(primary["all_sites"]),
        "shared_address_count": len(shared_addresses),
        "shared_cube_address_failures": sum(
            left_map[key] != right_map[key] for key in shared_addresses
        ),
        "left_to_primary_address_failures": sum(
            value != primary_map[key] for key, value in left_map.items()
        ),
        "right_to_primary_address_failures": sum(
            value != primary_map[key] for key, value in right_map.items()
        ),
        "cube_union_equals_primary": set(left[4]) | set(right[4]) == set(primary["all_sites"]),
    }


def covariance_certificate(routed_word) -> dict[str, object]:
    frames = C.F.base.proper_cubic_frames()
    touched = tuple(sorted({site for gate in routed_word for site in gate.sites}))
    rotated_nn_failures = 0
    for frame in frames:
        for gate in routed_word:
            sites = tuple(
                tuple(int(value) for value in frame @ np.asarray(site))
                for site in gate.sites
            )
            rotated_nn_failures += len(sites) == 2 and route.l1(*sites) != 1
    product_site_failures = 0
    for left in frames:
        for right in frames:
            for site in touched:
                direct = (left @ right) @ np.asarray(site)
                sequential = left @ (right @ np.asarray(site))
                product_site_failures += not np.array_equal(direct, sequential)
    translation_failures = 0
    for shift in product(range(2), repeat=3):
        translation_failures += sum(
            len(gate.sites) == 2
            and route.l1(*tuple(tuple(a + b for a, b in zip(site, shift)) for site in gate.sites)) != 1
            for gate in routed_word
        )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "touched_word_sites": len(touched),
        "rotated_word_NN_failures": rotated_nn_failures,
        "frame_product_site_diagram_failures": product_site_failures,
        "translation_residue_diagrams": 8,
        "translated_word_NN_failures": translation_failures,
        "coframe_action": "transport the supplied chart word; canonical textual word invariance not claimed",
    }


def primary_certificate() -> dict[str, object]:
    primary = primary_word()
    routed, route_report = c707.route_word(primary["word"])
    endpoint_failures = 0
    cube = C.coloured_composition(G.box_cells((2, 2, 2)))
    for endpoint in G.endpoints(cube.equivalence):
        endpoint_failures += sum(
            C.apply_images(cube.cleaned, C.natural(cube.equivalence, source), cube.equivalence.qubits)
            != target
            for source, target in zip(endpoint.source_rows, endpoint.target_rows)
        )
    repetitions = sum(
        repetition_failures(
            row, primary["graph"], primary["site_map"], primary["all_sites"]
        )
        for row in primary["physical_factor_rows"]
    )
    cleanup_colour_count = max(primary["cleanup_edge_colours"], default=-1) + 1
    report = {
        "cells": len(primary["cells"]),
        "abstract_qubits": primary["equivalence"].qubits,
        "seams": len(primary["equivalence"].rail_labels),
        "literal_M2": len(primary["all_sites"]),
        "placement_collisions": primary["placement_collisions"],
        "signed_abstract_compiler_failures": primary["composition"].cleaned != primary["composition"].target,
        "physical_factor_rows": len(primary["physical_factor_rows"]),
        "repetition_stabilizer_failures": repetitions,
        "same_colour_abstract_support_collisions": primary["same_colour_support_collisions"],
        "seam_colour_layers": 6,
        "cleanup_edge_layers": cleanup_colour_count,
        "cleanup_edge_layer_collisions": sum(
            bool(set(left) & set(right)) and lc == rc
            for index, (left, lc) in enumerate(zip(primary["composition"].cleanup, primary["cleanup_edge_colours"]))
            for right, rc in zip(primary["composition"].cleanup[index + 1:], primary["cleanup_edge_colours"][index + 1:])
        ),
        "primitive_gate_count": len(primary["word"]),
        "routed_gate_count": len(routed),
        "maximum_route_distance": route_report["maximum_route_distance"],
        "non_NN_failures": route_report["non_NN_failures"],
        "operand_order_failures": route_report["operand_order_failures"],
        "route_return_failures": route_report["route_return_failures"],
        "delete_first_swap_detected_macros": route_report["delete_first_swap_detected_macros"],
        "Cycle708_endpoint_rows": 36,
        "Cycle708_endpoint_regression_failures": endpoint_failures,
        "routed_word_sha256": route_report["word_sha256"],
        "routed_kind_census": dict(Counter(gate.kind for gate in routed)),
        "overlap": overlap_certificate(primary),
        "full_box_semantic_covariance": (
            "open: the exact 24/576 result is the gauge-transported one-seam "
            "factor family; this primary word is not rebuilt on 24 rotated canonical tuples"
        ),
        "physical_schedule_boundary": (
            "a supplied serial Manhattan micro-schedule routes the exact bounded word; "
            "collision-free constant-depth parallel routing and an autonomous controller remain open"
        ),
    }
    return report
