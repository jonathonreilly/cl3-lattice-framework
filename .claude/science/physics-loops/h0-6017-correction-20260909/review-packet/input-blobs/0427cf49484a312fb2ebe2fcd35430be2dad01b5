#!/usr/bin/env python3
"""Independent basis-gauge audit for the Cycle708 open-cube tableau."""

from __future__ import annotations

from itertools import product
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_cycle708_endpoint_cube_tableau_core_2026_07_26 as T


Coord = tuple[int, int, int]
CELLS: tuple[Coord, ...] = tuple(product(range(2), repeat=3))


def _rank(rows, qubits: int) -> int:
    return T.gf2_rank(row.symplectic(qubits) for row in rows)


def _reference_axis(graph, edge: int):
    u, v, _kind, _owner = graph.edges[edge]
    left = graph.vertices[u][0]
    right = graph.vertices[v][0]
    delta = tuple(b - a for a, b in zip(left, right))
    axis = next(
        candidate for candidate in range(3)
        if delta in (
            tuple(int(index == candidate) for index in range(3)),
            tuple(-int(index == candidate) for index in range(3)),
        )
    )
    return min(left, right), axis


def _target_loop(descriptor, open_graph, patch_graph):
    return patch_graph.loop_pauli(tuple(
        patch_graph.vertex_index[open_graph.vertices[vertex]]
        for vertex in descriptor.vertices
    ))


def _relation_mask(rows, qubits: int) -> int:
    pivots: dict[int, tuple[int, int]] = {}
    relations = []
    for index, pauli in enumerate(rows):
        row = pauli.symplectic(qubits)
        combination = 1 << index
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                previous, previous_combination = pivots[pivot]
                row ^= previous
                combination ^= previous_combination
            else:
                pivots[pivot] = row, combination
                break
        if not row:
            relations.append(combination)
    if len(relations) != 1:
        raise ValueError(("expected unique W relation", len(relations)))
    return relations[0]


def _multiply(rows):
    result = T.Pauli()
    for row in rows:
        result = result @ row
    return result


def _centered_cell(frame, cell: Coord) -> Coord:
    doubled = 2 * np.asarray(cell, dtype=int) - 1
    return tuple(int(value) for value in ((frame @ doubled) + 1) // 2)


def _descriptor_label(descriptor, graph):
    if descriptor.kind == "cell_triangle":
        cell = descriptor.owner
        modes = frozenset(
            graph.vertices[vertex][1]
            for vertex in descriptor.vertices
            if graph.vertices[vertex][1] != 6
        )
        return "triangle", cell, modes
    if descriptor.kind == "coarse_plaquette":
        cells = frozenset(graph.vertices[vertex][0] for vertex in descriptor.vertices)
        return "coarse", cells
    raise ValueError(descriptor.kind)


def _transform_label(label, frame):
    if label[0] == "triangle":
        direction = T.direction_map(frame)
        return "triangle", _centered_cell(frame, label[1]), frozenset(
            direction[mode] for mode in label[2]
        )
    return "coarse", frozenset(_centered_cell(frame, cell) for cell in label[1])


def certificate() -> dict[str, object]:
    open_graph = T.ReferencePatchGraph(CELLS, True)
    patch_graph = T.ReferencePatchGraph(CELLS, False)
    descriptors = T.local_cycles(open_graph)
    cell_descriptors = tuple(row for row in descriptors if row.kind == "cell_triangle")
    coarse_descriptors = tuple(row for row in descriptors if row.kind == "coarse_plaquette")
    bond_descriptors = {
        row.owner: open_graph.loop_pauli(row.vertices)
        for row in descriptors if row.kind == "bond_rectangle"
    }
    reference_edges = tuple(
        edge for edge, (_u, _v, kind, _owner) in enumerate(open_graph.edges)
        if kind == "reference_bond"
    )
    source_z, source_x = T.logical_rows(open_graph, CELLS)
    target_z, target_x = T.logical_rows(patch_graph, CELLS)
    source_cells = [open_graph.loop_pauli(row.vertices) for row in cell_descriptors]
    target_cells = [_target_loop(row, open_graph, patch_graph) for row in cell_descriptors]
    source_coarse = [open_graph.loop_pauli(row.vertices) for row in coarse_descriptors]
    target_coarse = [_target_loop(row, open_graph, patch_graph) for row in coarse_descriptors]
    source_ds = [T.local_d(open_graph, cell) for cell in CELLS[:-1]]
    target_ds = [T.local_d(patch_graph, cell) for cell in CELLS[:-1]]
    source_bonds = [bond_descriptors[_reference_axis(open_graph, edge)] for edge in reference_edges]
    target_rails = [
        T.Pauli(z=1 << (len(patch_graph.edges) + index))
        for index in range(len(reference_edges))
    ]
    source_full = source_z + source_cells + source_coarse + source_ds + source_bonds
    target_full = target_z + target_cells + target_coarse + target_ds + target_rails
    kinds = (
        ("logical_Z",) * len(source_z)
        + ("cell_triangle",) * len(source_cells)
        + ("coarse_plaquette",) * len(source_coarse)
        + ("local_D",) * len(source_ds)
        + ("bond_rectangle",) * len(source_bonds)
    )
    labels = (
        (None,) * len(source_z)
        + tuple(_descriptor_label(row, open_graph) for row in cell_descriptors)
        + tuple(_descriptor_label(row, open_graph) for row in coarse_descriptors)
        + (None,) * (len(source_ds) + len(source_bonds))
    )
    qubits = len(open_graph.edges)
    relation = _relation_mask(source_full, qubits)
    relation_indices = tuple(
        index for index in range(len(source_full)) if (relation >> index) & 1
    )
    relation_labels = frozenset(labels[index] for index in relation_indices)
    if None in relation_labels:
        raise AssertionError("relation unexpectedly contains an unlabeled row")

    source_ranks = []
    target_ranks = []
    canonical_failures = []
    endpoint_failures = 0
    source_endpoint_pairs = []
    target_endpoint_pairs = []
    for cell, axis, _matter, _reference in open_graph.cross_edges:
        target_cell = list(cell)
        target_cell[axis] += 1
        target_cell = tuple(target_cell)
        source_vertices = (
            open_graph.vertex_index[(cell, 2 * axis + 1)],
            open_graph.vertex_index[(target_cell, 2 * axis)],
        )
        target_vertices = (
            patch_graph.vertex_index[(cell, 2 * axis + 1)],
            patch_graph.vertex_index[(target_cell, 2 * axis)],
        )
        source_pair = tuple(open_graph.B(vertex) for vertex in source_vertices)
        target_pair = tuple(patch_graph.B(vertex) for vertex in target_vertices)
        source_endpoint_pairs.extend(source_pair + (source_pair[0] @ source_pair[1],))
        target_endpoint_pairs.extend(target_pair + (target_pair[0] @ target_pair[1],))
    for deleted in relation_indices:
        source_w = [row for index, row in enumerate(source_full) if index != deleted]
        target_w = [row for index, row in enumerate(target_full) if index != deleted]
        source_ranks.append(_rank(source_w, qubits))
        target_ranks.append(_rank(target_w, qubits))
        source_v = T.complete_tableau(source_w, source_x, qubits)
        target_v = T.complete_tableau(target_w, target_x, qubits)
        canonical_failures.append(
            T.canonical_failures(source_w, source_v, qubits)
            + T.canonical_failures(target_w, target_v, qubits)
        )
        for source, expected in zip(source_endpoint_pairs, target_endpoint_pairs):
            coordinates = T.decode(source, source_w, source_v, qubits)
            endpoint_failures += T.encode(coordinates, target_w, target_v, qubits) != expected

    outside_ranks = tuple(
        _rank([row for row_index, row in enumerate(source_full) if row_index != deleted], qubits)
        for deleted in range(len(source_full)) if deleted not in relation_indices
    )
    frames = T.proper_cubic_frames()
    action_failures = 0
    fixed_rows = []
    for label in relation_labels:
        images = {_transform_label(label, frame) for frame in frames}
        action_failures += sum(image not in relation_labels for image in images)
        if images == {label}:
            fixed_rows.append(label)
    unseen = set(relation_labels)
    orbit_sizes = []
    while unseen:
        seed = next(iter(unseen))
        orbit = {_transform_label(seed, frame) for frame in frames}
        orbit_sizes.append(len(orbit))
        unseen -= orbit

    relation_source_product = _multiply(source_full[index] for index in relation_indices)
    relation_target_product = _multiply(target_full[index] for index in relation_indices)
    return {
        "full_W_rows": len(source_full),
        "full_source_rank": _rank(source_full, qubits),
        "full_target_rank": _rank(target_full, qubits),
        "relation_dimension": len(source_full) - _rank(source_full, qubits),
        "unique_relation_weight": len(relation_indices),
        "relation_kind_counts": {
            kind: sum(kinds[index] == kind for index in relation_indices)
            for kind in sorted(set(kinds)) if any(kinds[index] == kind for index in relation_indices)
        },
        "source_relation_identity": (
            relation_source_product.phase,
            relation_source_product.x,
            relation_source_product.z,
        ),
        "target_relation_identity": (
            relation_target_product.phase,
            relation_target_product.x,
            relation_target_product.z,
        ),
        "eligible_deletion_rows": len(relation_indices),
        "eligible_source_rank_failures": sum(rank != qubits for rank in source_ranks),
        "eligible_target_rank_failures": sum(rank != qubits for rank in target_ranks),
        "eligible_canonical_failures": sum(canonical_failures),
        "eligible_endpoint_maps": len(relation_indices) * len(source_endpoint_pairs),
        "eligible_endpoint_map_failures": endpoint_failures,
        "outside_deletion_rows": len(outside_ranks),
        "outside_deletion_rank_values": tuple(sorted(set(outside_ranks))),
        "proper_cubic_frames": len(frames),
        "relation_row_action_failures": action_failures,
        "relation_row_orbit_sizes": tuple(sorted(orbit_sizes)),
        "globally_fixed_eligible_rows": len(fixed_rows),
        "basis_gauge_boundary": (
            "a deletion row is supplied basis gauge; no eligible row is invariant under all frames"
        ),
    }
