#!/usr/bin/env python3
"""Bounded Cycle708 OpenReference endpoint transport on one open 2x2x2 cube.

This module repairs the single W-row redundancy which first appears on the
open cube, transports the twelve pairs of Cycle704 endpoint B words through
the signed Cycle706 Clifford map, lifts them through the Cycle707 repetition
placement, and constructs a finite route-and-return parity extraction.  The
chart, coframe, cell order, drop choice, Manhattan route order, and blank work
site are supplied.  Nothing here is a recurrence, occurrence, time, or Record
construction.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as c706
import frontier_cycle708_cube_basis_gauge_core_2026_07_26 as basis_gauge
import frontier_full128_25site_nn_circuit_core_2026_07_24 as route
import frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26 as c707


Coord = tuple[int, int, int]
Owner = tuple[Coord, int, int]
CELLS: tuple[Coord, ...] = tuple(product(range(2), repeat=3))
EXPECTED_DEPENDENCIES = {
    "scripts/frontier_literal_patchgraph_z3_m2_placement_core_cycle707_2026_07_26.py":
        "b418c74e82405a0511de81be0eef7080f98d5fe760ccac5d47783a6a751c2480",
    "scripts/frontier_full128_25site_nn_circuit_core_2026_07_24.py":
        "e79b733bd3b8e273a2094679e6175b5d1f253ebef1a33b96544519cbdf278e13",
    "scripts/proper_cubic_bound_object_equivalence_cycle210_2026_07_16.py":
        "c410b754d4e984f6ee5ccbc7c5a52e776c50c91c4daa12d798044f104cc7435b",
    "scripts/frontier_full128_cycle_encoder_2026_07_24.py":
        "17eca725b72943d8804147dd800be044ffaa80dc209588adb37ae6543d0fa935",
    "scripts/frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26.py":
        "05cb2f6083cf6c4307c04284632e991b7fd7378cbd2a4eb08a52d5e3c7ae6b99",
    "scripts/frontier_full128_two_rail_fixed_law_core_2026_07_24.py":
        "b446ace0856b45108ae0ed4ed35614961ae3b69bf20d12132981f54809966afb",
    "scripts/frontier_full128_cycle_cocycle_intertwiner_2026_07_24.py":
        "ecae9048b4ee2d257315072cb7120335109f362fa7007573c46a82a1f0ed4195",
    "scripts/frontier_full128_bare_frame_pair_cocycle_2026_07_24.py":
        "94f0fbd1212e210d0e073c3a80cdc2f92afa3c9807f981bd220625a67e8d94a0",
    "scripts/frontier_full128_code_projectors_2026_07_24.py":
        "f561714d036c8c7568b1772110303d6c0da11c6d73c9df3bdcbae2db632f5b44",
}
EVIDENCE_DEPENDENCIES = {
    "scripts/frontier_cycle706_openreference_patchgraph_four_rail_equivalence_2026_07_26.py":
        "71d073a95d089c13baf6fbaff4c3e3ebbd63650a3c152bba49f8de78ee377c69",
}


@dataclass(frozen=True)
class Build:
    equivalence: c706.Equivalence
    coarse_owners: tuple[Owner, ...]
    selected_coarse_owners: tuple[Owner, ...]
    dropped_coarse_owners: tuple[Owner, ...]
    full_rows: int
    full_source_rank: int
    full_target_rank: int
    coarse_source_rank_alone: int
    coarse_target_rank_alone: int


@dataclass(frozen=True)
class Endpoint:
    cell: Coord
    target: Coord
    axis: int
    source_rows: tuple[c706.base.Pauli, ...]
    target_rows: tuple[c706.base.Pauli, ...]


def dependency_pins() -> dict[str, object]:
    observed = {
        name: sha256((ROOT / name).read_bytes()).hexdigest()
        for name in EXPECTED_DEPENDENCIES
    }
    evidence = {
        name: sha256((ROOT / name).read_bytes()).hexdigest()
        for name in EVIDENCE_DEPENDENCIES
    }
    return {
        "expected": EXPECTED_DEPENDENCIES,
        "observed": observed,
        "failures": tuple(
            name for name, digest in observed.items()
            if digest != EXPECTED_DEPENDENCIES[name]
        ),
        "nonruntime_evidence_expected": EVIDENCE_DEPENDENCIES,
        "nonruntime_evidence_observed": evidence,
        "nonruntime_evidence_failures": tuple(
            name for name, digest in evidence.items()
            if digest != EVIDENCE_DEPENDENCIES[name]
        ),
    }


def _rank(rows, qubits: int) -> int:
    return c706.base.gf2_rank(row.symplectic(qubits) for row in rows)


def _natural_data(open_graph, patch_graph):
    lookup = {
        c706.edge_key(patch_graph, edge): edge
        for edge in range(len(patch_graph.edges))
    }
    edge_map: dict[int, int] = {}
    reference_edges = []
    for edge in range(len(open_graph.edges)):
        key = c706.edge_key(open_graph, edge)
        if key in lookup:
            edge_map[edge] = lookup[key]
        elif key[1] == "reference_bond":
            reference_edges.append(edge)
        else:
            raise ValueError(("unmatched edge", key))
    for rail_index, edge in enumerate(reference_edges):
        edge_map[edge] = len(patch_graph.edges) + rail_index
    return edge_map, tuple(reference_edges)


def _target_loop(descriptor, open_graph, patch_graph):
    vertices = tuple(
        patch_graph.vertex_index[open_graph.vertices[vertex]]
        for vertex in descriptor.vertices
    )
    return patch_graph.loop_pauli(vertices)


def _reference_axis(open_graph, edge: int) -> tuple[Coord, int]:
    u, v, _kind, _owner = open_graph.edges[edge]
    left = open_graph.vertices[u][0]
    right = open_graph.vertices[v][0]
    delta = tuple(b - a for a, b in zip(left, right))
    axis = next(
        candidate for candidate in range(3)
        if delta in (
            tuple(int(index == candidate) for index in range(3)),
            tuple(-int(index == candidate) for index in range(3)),
        )
    )
    return min(left, right), axis


def _greedy_coarse_basis(base_source, base_target, coarse, qubits: int):
    source = list(base_source)
    target = list(base_target)
    selected = []
    source_rank = _rank(source, qubits)
    target_rank = _rank(target, qubits)
    for owner, source_row, target_row in coarse:
        next_source_rank = _rank(source + [source_row], qubits)
        next_target_rank = _rank(target + [target_row], qubits)
        if next_source_rank == source_rank + 1 and next_target_rank == target_rank + 1:
            source.append(source_row)
            target.append(target_row)
            selected.append(owner)
            source_rank = next_source_rank
            target_rank = next_target_rank
    if source_rank != qubits or target_rank != qubits:
        raise ValueError(("greedy coarse basis incomplete", source_rank, target_rank, qubits))
    return tuple(selected)


def build_equivalence(
    cells: tuple[Coord, ...],
    dropped_coarse_owners: tuple[Owner, ...] | None = None,
) -> Build:
    """Build the finite signed map, optionally freezing an explicit drop set."""
    cells = tuple(cells)
    open_graph = c706.ReferencePatchGraph(cells, True)
    patch_graph = c706.ReferencePatchGraph(cells, False)
    natural_edge_map, reference_edges = _natural_data(open_graph, patch_graph)
    descriptors = c706.local_cycles(open_graph)

    cell_rows = []
    coarse_rows = []
    bond_by_owner = {}
    for descriptor in descriptors:
        source = open_graph.loop_pauli(descriptor.vertices)
        if descriptor.kind == "bond_rectangle":
            bond_by_owner[descriptor.owner] = source
        elif descriptor.kind == "coarse_plaquette":
            coarse_rows.append(
                (descriptor.owner, source, _target_loop(descriptor, open_graph, patch_graph))
            )
        else:
            cell_rows.append(
                (descriptor.owner, source, _target_loop(descriptor, open_graph, patch_graph))
            )

    rail_labels = []
    source_bonds = []
    for edge in reference_edges:
        u, v, _kind, _owner = open_graph.edges[edge]
        rail_labels.append(frozenset((open_graph.vertices[u], open_graph.vertices[v])))
        source_bonds.append(bond_by_owner[_reference_axis(open_graph, edge)])

    source_z, source_x = c706.logical_rows(open_graph, cells)
    target_z, target_x = c706.logical_rows(patch_graph, cells)
    source_ds = [c706.local_d(open_graph, cell) for cell in cells[:-1]]
    target_ds = [c706.local_d(patch_graph, cell) for cell in cells[:-1]]
    target_rails = [
        c706.base.Pauli(z=1 << (len(patch_graph.edges) + index))
        for index in range(len(reference_edges))
    ]
    source_cell_rows = [row[1] for row in cell_rows]
    target_cell_rows = [row[2] for row in cell_rows]
    base_source = source_z + source_cell_rows + source_ds + source_bonds
    base_target = target_z + target_cell_rows + target_ds + target_rails
    qubits = len(open_graph.edges)
    owners = tuple(row[0] for row in coarse_rows)

    if dropped_coarse_owners is None:
        selected = _greedy_coarse_basis(base_source, base_target, coarse_rows, qubits)
        dropped = tuple(owner for owner in owners if owner not in selected)
    else:
        dropped = tuple(dropped_coarse_owners)
        if len(set(dropped)) != len(dropped) or any(owner not in owners for owner in dropped):
            raise ValueError("unknown or duplicate coarse-plaquette drop owner")
        selected = tuple(owner for owner in owners if owner not in dropped)

    selected_lookup = set(selected)
    source_coarse = [source for owner, source, _target in coarse_rows if owner in selected_lookup]
    target_coarse = [target for owner, _source, target in coarse_rows if owner in selected_lookup]
    source_shared = source_cell_rows + source_coarse
    target_shared = target_cell_rows + target_coarse
    source_w = source_z + source_shared + source_ds + source_bonds
    target_w = target_z + target_shared + target_ds + target_rails
    if len(source_w) != qubits or _rank(source_w, qubits) != qubits:
        raise ValueError(("source W is not a basis", len(source_w), _rank(source_w, qubits), qubits))
    if len(target_w) != qubits or _rank(target_w, qubits) != qubits:
        raise ValueError(("target W is not a basis", len(target_w), _rank(target_w, qubits), qubits))
    source_v = c706.complete_tableau(source_w, source_x, qubits)
    target_v = c706.complete_tableau(target_w, target_x, qubits)
    equivalence = c706.Equivalence(
        cells, open_graph, patch_graph, tuple(rail_labels), natural_edge_map,
        source_w, source_v, target_w, target_v, source_z, source_x,
        target_z, target_x, source_shared, target_shared, source_ds, target_ds,
        source_bonds, target_rails,
    )
    full_source = base_source + [row[1] for row in coarse_rows]
    full_target = base_target + [row[2] for row in coarse_rows]
    return Build(
        equivalence=equivalence,
        coarse_owners=owners,
        selected_coarse_owners=selected,
        dropped_coarse_owners=dropped,
        full_rows=len(full_source),
        full_source_rank=_rank(full_source, qubits),
        full_target_rank=_rank(full_target, qubits),
        coarse_source_rank_alone=_rank([row[1] for row in coarse_rows], qubits),
        coarse_target_rank_alone=_rank([row[2] for row in coarse_rows], qubits),
    )


def endpoints(equivalence: c706.Equivalence) -> tuple[Endpoint, ...]:
    rows = []
    for cell, axis, _matter, _reference in equivalence.open_graph.cross_edges:
        target_list = list(cell)
        target_list[axis] += 1
        target = tuple(target_list)
        source_vertices = (
            equivalence.open_graph.vertex_index[(cell, 2 * axis + 1)],
            equivalence.open_graph.vertex_index[(target, 2 * axis)],
        )
        target_vertices = (
            equivalence.patch_graph.vertex_index[(cell, 2 * axis + 1)],
            equivalence.patch_graph.vertex_index[(target, 2 * axis)],
        )
        source_pair = tuple(equivalence.open_graph.B(vertex) for vertex in source_vertices)
        target_pair = tuple(equivalence.patch_graph.B(vertex) for vertex in target_vertices)
        rows.append(Endpoint(
            cell, target, axis,
            source_pair + (source_pair[0] @ source_pair[1],),
            target_pair + (target_pair[0] @ target_pair[1],),
        ))
    return tuple(rows)


def _linf(left: Coord, right: Coord) -> int:
    return max(abs(a - b) for a, b in zip(left, right))


def _diameter(points, metric) -> int:
    return max((metric(left, right) for left in points for right in points), default=0)


def physical_support(row, graph, site_map):
    physical, all_sites = c707.physical_pauli(row, graph, site_map)
    support = tuple(
        site for index, site in enumerate(all_sites)
        if ((physical.x | physical.z) >> index) & 1
    )
    return physical, support


def route_parity_extraction(
    support: tuple[Coord, ...],
    rail: Coord,
    pointer: Coord,
    occupied: set[Coord],
) -> tuple[route.Gate, ...]:
    if len(support) != 10 or len(set(support)) != 10:
        raise ValueError("endpoint-pair support must contain ten distinct sites")
    if pointer in occupied or pointer == rail:
        raise ValueError("pointer must be a distinct blank work M2")
    return tuple(
        gate
        for site in support
        for gate in route.route_two("Bpair_parity_CNOT", site, pointer, route.CNOT)
    )


def extraction_certificate(support, rail, pointer, occupied):
    gates = route_parity_extraction(support, rail, pointer, occupied)
    touched = {site for gate in gates for site in gate.sites}
    wires = tuple(sorted(touched | {rail}))
    wire_index = {site: index for index, site in enumerate(wires)}
    failures = 0
    for mask in range(1 << len(support)):
        bits = [0] * len(wires)
        for index, site in enumerate(support):
            bits[wire_index[site]] = (mask >> index) & 1
        initial = bits.copy()
        for gate in gates:
            left, right = (wire_index[site] for site in gate.sites)
            if gate.kind == "route_swap":
                bits[left], bits[right] = bits[right], bits[left]
            else:
                bits[right] ^= bits[left]
        failures += bits[wire_index[pointer]] != (mask.bit_count() & 1)
        failures += any(
            bits[index] != initial[index]
            for index in range(len(wires)) if index != wire_index[pointer]
        )

    active = tuple(index for index, gate in enumerate(gates) if gate.kind == "Bpair_parity_CNOT")
    detected = 0
    for support_index, deleted in enumerate(active):
        bits = [0] * len(wires)
        bits[wire_index[support[support_index]]] = 1
        for index, gate in enumerate(gates):
            if index == deleted:
                continue
            left, right = (wire_index[site] for site in gate.sites)
            if gate.kind == "route_swap":
                bits[left], bits[right] = bits[right], bits[left]
            else:
                bits[right] ^= bits[left]
        detected += bits[wire_index[pointer]] == 0
    symbolic_failures = 0
    support_set = set(support)
    for basis_site in wires:
        bits = [0] * len(wires)
        bits[wire_index[basis_site]] = 1
        for gate in gates:
            left, right = (wire_index[site] for site in gate.sites)
            if gate.kind == "route_swap":
                bits[left], bits[right] = bits[right], bits[left]
            else:
                bits[right] ^= bits[left]
        expected = [0] * len(wires)
        expected[wire_index[basis_site]] = 1
        if basis_site in support_set:
            expected[wire_index[pointer]] ^= 1
        symbolic_failures += bits != expected
    route_swap_positions = tuple(
        index for index, gate in enumerate(gates) if gate.kind == "route_swap"
    )
    first_route_swap_deletion_detected = False
    if route_swap_positions:
        deleted = route_swap_positions[0]
        for basis_site in wires:
            bits = [0] * len(wires)
            bits[wire_index[basis_site]] = 1
            for index, gate in enumerate(gates):
                if index == deleted:
                    continue
                left, right = (wire_index[site] for site in gate.sites)
                if gate.kind == "route_swap":
                    bits[left], bits[right] = bits[right], bits[left]
                else:
                    bits[right] ^= bits[left]
            expected = [0] * len(wires)
            expected[wire_index[basis_site]] = 1
            if basis_site in support_set:
                expected[wire_index[pointer]] ^= 1
            if bits != expected:
                first_route_swap_deletion_detected = True
                break
    distances = tuple(route.l1(site, pointer) for site in support)
    return gates, {
        "truth_rows": 1 << len(support),
        "truth_or_return_failures": failures,
        "active_CNOTs": len(active),
        "active_CNOT_deletions_detected": detected,
        "route_SWAPs": len(route_swap_positions),
        "first_route_SWAP_deletion_detected": first_route_swap_deletion_detected,
        "nearest_neighbor_failures": sum(route.l1(*gate.sites) != 1 for gate in gates),
        "symbolic_GF2_basis_rows": len(wires),
        "symbolic_arbitrary_spectator_or_return_failures": symbolic_failures,
        "protected_rail_symbolically_returned": symbolic_failures == 0,
        "routed_compute_factors": len(gates),
        "touched_sites": len(touched),
        "maximum_pointer_distance": max(distances),
        "protected_rail_traversed_and_returned": rail in touched,
    }


def cube_certificate() -> dict[str, object]:
    first = build_equivalence(CELLS, (((0, 0, 0), 0, 1),))
    expected_owners = first.coarse_owners
    drop_rows = []
    reference_images = None
    for owner in expected_owners:
        built = build_equivalence(CELLS, (owner,))
        equivalence = built.equivalence
        images = tuple(
            equivalence.forward(source)
            for seam in endpoints(equivalence) for source in seam.source_rows
        )
        expected = tuple(row for seam in endpoints(equivalence) for row in seam.target_rows)
        drop_rows.append({
            "drop_owner": owner,
            "full_rows": built.full_rows,
            "full_source_rank": built.full_source_rank,
            "full_target_rank": built.full_target_rank,
            "coarse_source_rank_alone": built.coarse_source_rank_alone,
            "coarse_target_rank_alone": built.coarse_target_rank_alone,
            "source_canonical_failures": c706.canonical_failures(
                equivalence.source_w, equivalence.source_v, equivalence.qubits
            ),
            "target_canonical_failures": c706.canonical_failures(
                equivalence.target_w, equivalence.target_v, equivalence.qubits
            ),
            "endpoint_rows": len(images),
            "endpoint_expected_failures": sum(left != right for left, right in zip(images, expected)),
            "endpoint_inverse_failures": sum(
                equivalence.inverse(image) != source
                for image, source in zip(images, (row for seam in endpoints(equivalence) for row in seam.source_rows))
            ),
            "endpoint_image_differences_from_first_drop": 0 if reference_images is None else sum(
                left != right for left, right in zip(reference_images, images)
            ),
        })
        if reference_images is None:
            reference_images = images

    equivalence = first.equivalence
    graph = c707.PatchGraph(CELLS)
    if graph.edges != equivalence.patch_graph.edges:
        raise AssertionError("Cycle706/Cycle707 cube edge lists differ")
    site_map, gauges = c707.placement(graph, include_edge_gauge=True)
    active_sites = c707.occupied_sites(site_map)
    occupied = c707.occupied_sites(site_map, gauges)
    stream_lookup = {
        frozenset((source, target)): (gauges[edge], axis)
        for edge, source, target, _smode, _tmode, axis in graph.stream_edges
    }
    seam_rows = []
    all_gates = []
    for seam in endpoints(equivalence):
        images = tuple(equivalence.forward(row) for row in seam.source_rows)
        physical = tuple(physical_support(row, graph, site_map) for row in images)
        rail, axis = stream_lookup[frozenset((seam.cell, seam.target))]
        pointer_axis = (axis + 1) % 3
        pointer = tuple(
            value + int(index == pointer_axis) for index, value in enumerate(rail)
        )
        gates, extraction = extraction_certificate(
            physical[2][1], rail, pointer, occupied
        )
        all_gates.extend(gates)
        seam_rows.append({
            "cell": seam.cell,
            "target": seam.target,
            "axis": seam.axis,
            "abstract_weights": tuple(c706.pauli_weight(row) for row in images),
            "abstract_union_weight": (images[0].z | images[1].z).bit_count(),
            "rail_weights": tuple(
                (row.z >> len(equivalence.patch_graph.edges)).bit_count() for row in images
            ),
            "pure_Z": tuple(row.x == 0 and row.phase == 0 for row in images),
            "cell_diameters": tuple(
                c706.cell_diameter(c706.target_support_cells(row, equivalence)) for row in images
            ),
            "physical_weights": tuple((row.x | row.z).bit_count() for row, _sites in physical),
            "physical_L1_diameters": tuple(_diameter(sites, route.l1) for _row, sites in physical),
            "physical_Linf_diameters": tuple(_diameter(sites, _linf) for _row, sites in physical),
            "rail": rail,
            "pointer": pointer,
            "pointer_collision": pointer in occupied,
            "extraction": extraction,
        })
    return {
        "build": first,
        "drop_rows": tuple(drop_rows),
        "graph": graph,
        "site_map": site_map,
        "gauges": gauges,
        "all_gates": tuple(all_gates),
        "seams": tuple(seam_rows),
        "resources": {
            "open_graph_edge_qubits": len(equivalence.open_graph.edges),
            "patch_graph_edge_qubits": len(equivalence.patch_graph.edges),
            "prepared_Z_rails": len(equivalence.rail_labels),
            "literal_active_M2": len(active_sites),
            "literal_plus_midpoint_rails_M2": len(occupied),
        },
    }


def summarize_cube(certificate) -> dict[str, object]:
    seams = certificate["seams"]
    routed_coordinates = {
        site for gate in certificate["all_gates"] for site in gate.sites
    }
    carrier_and_rail_sites = c707.occupied_sites(
        certificate["site_map"], certificate["gauges"]
    )
    return {
        "scope": "open 2x2x2 cube; finite supplied chart only",
        "coarse_plaquette_owners": certificate["build"].coarse_owners,
        "drop_choices": certificate["drop_rows"],
        "resources": certificate["resources"],
        "endpoint": {
            "seams": len(seams),
            "mapped_rows": 3 * len(seams),
            "abstract_weight_tuples": sorted({row["abstract_weights"] for row in seams}),
            "rail_weight_tuples": sorted({row["rail_weights"] for row in seams}),
            "pure_Z_failures": sum(not all(row["pure_Z"]) for row in seams),
            "cell_diameter_tuples": sorted({row["cell_diameters"] for row in seams}),
            "physical_weight_tuples": sorted({row["physical_weights"] for row in seams}),
            "maximum_physical_L1_by_word": tuple(
                max(row["physical_L1_diameters"][index] for row in seams) for index in range(3)
            ),
            "maximum_physical_Linf_by_word": tuple(
                max(row["physical_Linf_diameters"][index] for row in seams) for index in range(3)
            ),
        },
        "extraction": {
            "pointer_collisions": sum(row["pointer_collision"] for row in seams),
            "distinct_pointers": len({row["pointer"] for row in seams}),
            "pairwise_pointer_collisions": len(seams) - len({row["pointer"] for row in seams}),
            "exhaustive_rows": sum(row["extraction"]["truth_rows"] for row in seams),
            "truth_or_return_failures": sum(row["extraction"]["truth_or_return_failures"] for row in seams),
            "nearest_neighbor_failures": sum(row["extraction"]["nearest_neighbor_failures"] for row in seams),
            "symbolic_GF2_basis_rows": sum(row["extraction"]["symbolic_GF2_basis_rows"] for row in seams),
            "symbolic_arbitrary_spectator_or_return_failures": sum(
                row["extraction"]["symbolic_arbitrary_spectator_or_return_failures"] for row in seams
            ),
            "protected_rails_symbolically_returned": sum(
                row["extraction"]["protected_rail_symbolically_returned"] for row in seams
            ),
            "selected_rails_traversed": sum(
                row["extraction"]["protected_rail_traversed_and_returned"] for row in seams
            ),
            "selected_rails_untraversed": sum(
                not row["extraction"]["protected_rail_traversed_and_returned"] for row in seams
            ),
            "all_selected_rails_final_return_failures": sum(
                not row["extraction"]["protected_rail_symbolically_returned"] for row in seams
            ),
            "active_CNOTs": sum(row["extraction"]["active_CNOTs"] for row in seams),
            "active_CNOT_deletions_detected": sum(row["extraction"]["active_CNOT_deletions_detected"] for row in seams),
            "first_route_SWAP_deletions_detected": sum(
                row["extraction"]["first_route_SWAP_deletion_detected"] for row in seams
            ),
            "routed_compute_factor_counts": sorted({row["extraction"]["routed_compute_factors"] for row in seams}),
            "selected_seam_routed_compute_factors": seams[0]["extraction"]["routed_compute_factors"],
            "all_12_independent_certificate_factors": sum(
                row["extraction"]["routed_compute_factors"] for row in seams
            ),
            "complete_routed_coordinates": len(routed_coordinates),
            "carrier_and_prepared_rail_sites": len(carrier_and_rail_sites),
            "routed_plus_carrier_rail_union": len(routed_coordinates | carrier_and_rail_sites),
            "execution_scope": "one selected seam per execution; aggregate word is covariance-only",
            "maximum_pointer_distance": max(row["extraction"]["maximum_pointer_distance"] for row in seams),
            "touched_sites_by_axis": {
                str(axis): sorted({
                    row["extraction"]["touched_sites"] for row in seams if row["axis"] == axis
                }) for axis in range(3)
            },
        },
    }


def covariance_certificate(certificate) -> dict[str, object]:
    """Check oriented endpoints and the complete routed word under 24/576."""
    frames = c706.base.proper_cubic_frames()
    base_endpoints = endpoints(certificate["build"].equivalence)
    semantic_failures = 0
    for frame in frames:
        moved_cells = tuple(
            tuple(int(value) for value in frame @ np.asarray(cell)) for cell in CELLS
        )
        moved = build_equivalence(moved_cells).equivalence
        direction = c706.base.direction_map(frame)
        for seam in base_endpoints:
            left_cell = tuple(int(value) for value in frame @ np.asarray(seam.cell))
            right_cell = tuple(int(value) for value in frame @ np.asarray(seam.target))
            vertices = (
                moved.open_graph.vertex_index[(left_cell, direction[2 * seam.axis + 1])],
                moved.open_graph.vertex_index[(right_cell, direction[2 * seam.axis])],
            )
            target_vertices = (
                moved.patch_graph.vertex_index[(left_cell, direction[2 * seam.axis + 1])],
                moved.patch_graph.vertex_index[(right_cell, direction[2 * seam.axis])],
            )
            source_pair = tuple(moved.open_graph.B(vertex) for vertex in vertices)
            expected_pair = tuple(moved.patch_graph.B(vertex) for vertex in target_vertices)
            source_rows = source_pair + (source_pair[0] @ source_pair[1],)
            expected_rows = expected_pair + (expected_pair[0] @ expected_pair[1],)
            semantic_failures += sum(
                moved.forward(source) != expected
                for source, expected in zip(source_rows, expected_rows)
            )

    composition_failures = 0
    for left in frames:
        left_direction = c706.base.direction_map(left)
        for right in frames:
            right_direction = c706.base.direction_map(right)
            direct = left @ right
            direct_direction = c706.base.direction_map(direct)
            for seam in base_endpoints:
                for cell, mode in (
                    (seam.cell, 2 * seam.axis + 1),
                    (seam.target, 2 * seam.axis),
                ):
                    sequential_cell = tuple(
                        int(value) for value in left @ (right @ np.asarray(cell))
                    )
                    direct_cell = tuple(int(value) for value in direct @ np.asarray(cell))
                    composition_failures += sequential_cell != direct_cell
                    composition_failures += (
                        left_direction[right_direction[mode]] != direct_direction[mode]
                    )
    literal = c707.covariance_controls(
        certificate["graph"], certificate["all_gates"]
    )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "oriented_endpoint_rows": len(frames) * len(base_endpoints) * 3,
        "oriented_endpoint_failures": semantic_failures,
        "endpoint_label_product_tests": len(frames) ** 2 * len(base_endpoints) * 2,
        "endpoint_label_product_failures": composition_failures,
        "literal_translation_vectors": 4,
        "claim_scope": "endpoint subalgebra and physical routed word only",
        "tableau_drop_covariance_claimed": False,
        "basis_gauge_warning": (
            "moved-cell greedy drops are independent gauges; no full tableau/drop covariance is inferred"
        ),
        "literal_full_extraction_word": literal,
    }


def cycle704_bridge_certificate() -> dict[str, object]:
    """Cross-check P_B on the dressed-FSWAP domain as a coherent eigenspace bit."""
    truth_rows = []
    for n_u, n_v in product((0, 1), repeat=2):
        before = (n_u, n_v)
        after = (n_v, n_u)
        b_before = tuple(1 - 2 * value for value in before)
        b_after = tuple(1 - 2 * value for value in after)
        p_b = int(any(left != right for left, right in zip(b_before, b_after)))
        b_product_eigenvalue = b_before[0] * b_before[1]
        extracted = (1 - b_product_eigenvalue) // 2
        truth_rows.append({
            "n_u": n_u,
            "n_v": n_v,
            "P_B": p_b,
            "n_u_xor_n_v": n_u ^ n_v,
            "B_u_B_v_eigenvalue": b_product_eigenvalue,
            "extracted_eigenbit": extracted,
        })

    # Basis is |n_u,n_v,p>, with p the high bit.  V is a unitary coherent
    # parity-to-pointer CNOT, not a measurement or a classical branch copy.
    embedding = np.zeros((8, 4), dtype=complex)
    target = np.zeros((8, 4), dtype=complex)
    unitary = np.zeros((8, 8), dtype=complex)
    parity_projector = np.zeros((4, 4), dtype=complex)
    b_product = np.zeros((4, 4), dtype=complex)
    for state in range(4):
        n_u, n_v = state & 1, (state >> 1) & 1
        parity = n_u ^ n_v
        embedding[state, state] = 1
        target[state + 4 * parity, state] = 1
        parity_projector[state, state] = parity
        b_product[state, state] = 1 - 2 * parity
        for pointer in (0, 1):
            source = state + 4 * pointer
            destination = state + 4 * (pointer ^ parity)
            unitary[destination, source] = 1
    unrestricted_mismatches = 0
    for n_u_before, n_v_before, n_u_after, n_v_after in product((0, 1), repeat=4):
        before = (n_u_before, n_v_before)
        after = (n_u_after, n_v_after)
        p_b = int(any(left != right for left, right in zip(before, after)))
        unrestricted_mismatches += p_b != (n_u_before ^ n_v_before)
    unchanged_false_fires = sum(
        (n_u ^ n_v) != 0 for n_u, n_v in product((0, 1), repeat=2)
    )
    return {
        "lawful_truth_rows": tuple(truth_rows),
        "truth_relation_failures": sum(
            row["P_B"] != row["n_u_xor_n_v"]
            or row["extracted_eigenbit"] != row["P_B"]
            for row in truth_rows
        ),
        "domain_controls": {
            "dressed_FSWAP_mismatches": sum(
                row["extracted_eigenbit"] != row["P_B"] for row in truth_rows
            ),
            "dressed_FSWAP_rows": len(truth_rows),
            "unrestricted_before_after_mismatches": unrestricted_mismatches,
            "unrestricted_before_after_rows": 16,
            "unchanged_diagonal_false_fires": unchanged_false_fires,
            "unchanged_diagonal_rows": 4,
        },
        "unitarity_residual": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(8))),
        "blank_pointer_isometry_residual": float(np.linalg.norm(unitary @ embedding - target)),
        "projector_relation_residual": float(np.linalg.norm(
            parity_projector - (np.eye(4) - b_product) / 2
        )),
        "superposition_semantics": (
            "V sum_q Pi_q|psi>|0> = sum_q Pi_q|psi>|q>; mixed-parity "
            "superpositions become coherently entangled with the pointer"
        ),
        "classification": "Cycle704 opportunity eigenspace only; no measurement, occurrence, or Record",
        "conditional_eigenspace_intertwiner": (
            "V(E_lit T |psi_+> tensor |0>) = E_lit T |psi_+> tensor |0>; "
            "V(E_lit T |psi_-> tensor |0>) = E_lit T |psi_-> tensor |1>"
        ),
        "map_boundary": (
            "T is the supplied abstract/dense signed tableau map; Cycle708 executes only V "
            "after the state is already in the literal PatchGraph/repetition code"
        ),
    }


def basis_gauge_certificate() -> dict[str, object]:
    return basis_gauge.certificate()


def box_cells(shape: tuple[int, int, int]) -> tuple[Coord, ...]:
    return tuple(product(*(range(size) for size in shape)))


def held_controls() -> tuple[dict[str, object], ...]:
    rows = []
    for shape in ((2, 2, 2), (3, 2, 2)):
        cells = box_cells(shape)
        built = build_equivalence(cells)
        equivalence = built.equivalence
        endpoint_rows = endpoints(equivalence)
        failures = sum(
            equivalence.forward(source) != expected
            for seam in endpoint_rows
            for source, expected in zip(seam.source_rows, seam.target_rows)
        )
        rows.append({
            "shape": shape,
            "split": "direct" if shape == (2, 2, 2) else "held-no-refit",
            "cells": len(cells),
            "open_edges": len(equivalence.open_graph.edges),
            "patch_edges": len(equivalence.patch_graph.edges),
            "rails": len(equivalence.rail_labels),
            "coarse_rows": len(built.coarse_owners),
            "dropped_coarse_rows": len(built.dropped_coarse_owners),
            "source_canonical_failures": c706.canonical_failures(
                equivalence.source_w, equivalence.source_v, equivalence.qubits
            ),
            "target_canonical_failures": c706.canonical_failures(
                equivalence.target_w, equivalence.target_v, equivalence.qubits
            ),
            "endpoint_rows": 3 * len(endpoint_rows),
            "endpoint_failures": failures,
            "parameters_refit": 0,
        })
    return tuple(rows)


def unlawful_controls() -> dict[str, object]:
    rejected = []
    cases = (
        ("empty", lambda: build_equivalence(())),
        ("duplicate", lambda: build_equivalence(((0, 0, 0), (0, 0, 0)))),
        ("disconnected", lambda: build_equivalence(((0, 0, 0), (2, 0, 0)))),
        ("unknown_drop", lambda: build_equivalence(CELLS, (((9, 9, 9), 0, 1),))),
        ("under_drop", lambda: build_equivalence(CELLS, ())),
        ("over_drop", lambda: build_equivalence(CELLS, (
            ((0, 0, 0), 0, 1), ((0, 0, 0), 0, 2)
        ))),
        ("non_ten_support", lambda: route_parity_extraction(
            ((0, 0, 0),), (1, 0, 0), (2, 0, 0), {(0, 0, 0), (1, 0, 0)}
        )),
        ("occupied_pointer", lambda: route_parity_extraction(
            tuple((index, 0, 0) for index in range(10)),
            (20, 0, 0), (0, 0, 0), set((index, 0, 0) for index in range(10))
        )),
    )
    for name, action in cases:
        try:
            action()
        except (ValueError, IndexError, StopIteration):
            rejected.append(name)
    return {
        "cases": tuple(name for name, _action in cases),
        "rejected": tuple(rejected),
        "failures": tuple(name for name, _action in cases if name not in rejected),
    }


def boundary_inventory() -> dict[str, tuple[str, ...]]:
    return {
        "supplied": (
            "the open 2x2x2 cell chart, origin, coframe, and lexicographic cell order",
            "one of six declared redundant coarse-plaquette rows to omit",
            "the Cycle706 signed tableau completion convention and prepared rail-Z sector",
            "the Cycle707 repetition placement and fixed x-y-z Manhattan route order",
            "one distinct blank pointer M2 per queried seam",
        ),
        "derived": (
            "the 168-rank cube basis for every one-row drop choice",
            "all 36 endpoint B/B/product images and their literal supports",
            "the 242-factor NN route-and-return parity extraction",
            "24/576 endpoint and literal routed-word covariance plus translations",
            "one 3x2x2 no-refit held-size control",
        ),
        "open": (
            "execution of the abstract/dense signed tableau map T as a local circuit",
            "local preparation and dynamical enforcement of the PatchGraph/rail/repetition code",
            "an autonomous pointer-genesis law",
            "a simultaneous overlap-safe schedule for all seam queries",
            "a before/after comparator and any occurrence predicate",
            "a recurrent translation-invariant compiler or realized-history construction",
        ),
        "not_claimed": (
            "the Cycle706 signed tableau T is not an executed local circuit",
            "Cycle708 physically executes only the selected-seam parity extractor V on an already encoded state",
            "the routed parity bit is not called a Record",
            "the supplied gate order is not called time",
            "no occurrence, recurrence, or global physical-site compiler is claimed",
            "each certificate executes one selected seam; no simultaneous all-seam schedule is built",
            "the finite cube result creates no route-independent no-go or axiom pressure",
        ),
    }
