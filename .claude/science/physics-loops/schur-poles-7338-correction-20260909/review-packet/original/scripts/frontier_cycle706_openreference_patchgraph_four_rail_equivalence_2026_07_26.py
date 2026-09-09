#!/usr/bin/env python3
"""Cycle 706: exact 80 <-> 76+4 OpenReference/PatchGraph bridge.

This runner independently reconstructs the landed Cycle-703 OpenReferenceGraph
and no-reference-bond PatchGraph definitions, then tests two distinct propositions:

1. the natural edge relabeling to PatchGraph tensor four single-Pauli rails;
2. a signed Clifford tableau equivalence which fixes all matter logical pairs
   and sends each bond-rectangle stabilizer to one prepared Z rail.

The second map is an exact finite code equivalence.  Its ambient tableau
completion is not asserted to be a bounded recurrent edge-qubit circuit or a
literal one-M2-per-Z3-site implementation.
"""

from __future__ import annotations

from collections import Counter, deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import json
import math
import sys
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_2026_07_17 as base


EXPECTED_OPEN_2X2_EDGE_DIGEST = (
    "324a88a72a23afb0f2d8ac445aa6d3a8709d4a2d4ce0eee6a8fea031f33ea6c4"
)
EXPECTED_PATCH_PATH_2X2_EDGE_DIGEST = (
    "d9e04aca40f3e2ffeaaf6c6dfa02e5d7066b4891ecd273fe54d537483c6a64b8"
)
REVERSE = (1, 0, 3, 2, 5, 4)
TOL = 1.0e-12
PASS = 0
FAIL = 0
REPORT: dict[str, object] = {}

Coord = tuple[int, int, int]


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def pauli_product(rows) -> base.Pauli:
    result = base.Pauli()
    for row in rows:
        result = result @ row
    return result


def pauli_weight(row: base.Pauli) -> int:
    return (row.x | row.z).bit_count()


def is_hermitian(row: base.Pauli) -> bool:
    return row.phase % 2 == (row.x & row.z).bit_count() % 2


def symplectic(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    lx, lz = left & mask, left >> qubits
    rx, rz = right & mask, right >> qubits
    return ((lx & rz).bit_count() + (lz & rx).bit_count()) & 1


class ReferencePatchGraph:
    """Seven-vertex cells, optionally including parallel reference bonds."""

    def __init__(self, cells: tuple[Coord, ...], reference_bonds: bool):
        if not cells:
            raise ValueError("empty cell set")
        if len(set(cells)) != len(cells):
            raise ValueError("duplicate cells")
        # The landed Cycle703 OpenReferenceGraph sorts its cell set, while PatchGraph keeps
        # the supplied Hamiltonian cell path.  That distinction changes one
        # signed coarse-plaquette row on 2x2 and is deliberately preserved.
        self.cells = tuple(sorted(cells)) if reference_bonds else tuple(cells)
        self.cell_set = set(self.cells)
        self.reference_bonds = reference_bonds
        self.vertices: list[tuple[Coord, int]] = []
        self.vertex_index: dict[tuple[Coord, int], int] = {}
        for cell in self.cells:
            for mode in range(7):
                self.vertex_index[(cell, mode)] = len(self.vertices)
                self.vertices.append((cell, mode))

        self.edges: list[tuple[int, int, str, Coord]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.cross_edges: list[
            tuple[Coord, int, int, int | None]
        ] = []

        def add_edge(u: int, v: int, kind: str, owner: Coord) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate graph edge", self.vertices[u], self.vertices[v]))
            edge = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = edge
            return edge

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] == right:
                    continue
                add_edge(
                    self.vertex_index[(cell, left)],
                    self.vertex_index[(cell, right)],
                    "octahedral",
                    cell,
                )
            reference = self.vertex_index[(cell, 6)]
            for mode in range(6):
                add_edge(
                    reference,
                    self.vertex_index[(cell, mode)],
                    "spoke",
                    cell,
                )

        for cell in self.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] += 1
                target_cell = tuple(target)
                if target_cell not in self.cell_set:
                    continue
                matter = add_edge(
                    self.vertex_index[(cell, 2 * axis + 1)],
                    self.vertex_index[(target_cell, 2 * axis)],
                    "matter_stream",
                    cell,
                )
                reference = None
                if reference_bonds:
                    reference = add_edge(
                        self.vertex_index[(cell, 6)],
                        self.vertex_index[(target_cell, 6)],
                        "reference_bond",
                        cell,
                    )
                self.cross_edges.append((cell, axis, matter, reference))

        self.incident: list[list[int]] = [[] for _ in self.vertices]
        for edge, (u, v, _kind, _owner) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()

        seen = {self.cells[0]}
        queue = deque([self.cells[0]])
        adjacency = {cell: set() for cell in self.cells}
        for cell, axis, _matter, _reference in self.cross_edges:
            target = list(cell)
            target[axis] += 1
            target_cell = tuple(target)
            adjacency[cell].add(target_cell)
            adjacency[target_cell].add(cell)
        while queue:
            cell = queue.popleft()
            for target in adjacency[cell] - seen:
                seen.add(target)
                queue.append(target)
        if len(seen) != len(self.cells):
            raise ValueError("cell set is disconnected")

    def edge_between(self, u: int, v: int) -> int:
        return self.edge_lookup[frozenset((u, v))]

    def B(self, vertex: int) -> base.Pauli:
        return base.Pauli(z=sum(1 << edge for edge in self.incident[vertex]))

    def A(self, source: int, target: int) -> base.Pauli:
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        return base.Pauli(0 if source < target else 2, 1 << edge, z)

    def loop_pauli(self, vertices: tuple[int, ...] | list[int]) -> base.Pauli:
        result = base.Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(source, vertices[(index + 1) % len(vertices)])
        return result


@dataclass(frozen=True)
class CycleDescriptor:
    vertices: tuple[int, ...]
    kind: str
    owner: object


def local_cycles(graph: ReferencePatchGraph) -> tuple[CycleDescriptor, ...]:
    rows = []
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for left, right in combinations(range(6), 2):
            if REVERSE[left] == right:
                continue
            rows.append(
                CycleDescriptor(
                    (
                        reference,
                        graph.vertex_index[(cell, left)],
                        graph.vertex_index[(cell, right)],
                    ),
                    "cell_triangle",
                    cell,
                )
            )
    if graph.reference_bonds:
        for cell, axis, _matter, reference_edge in graph.cross_edges:
            if reference_edge is None:
                raise AssertionError("open graph cross edge lost its reference bond")
            target = list(cell)
            target[axis] += 1
            target_cell = tuple(target)
            rows.append(
                CycleDescriptor(
                    (
                        graph.vertex_index[(cell, 6)],
                        graph.vertex_index[(cell, 2 * axis + 1)],
                        graph.vertex_index[(target_cell, 2 * axis)],
                        graph.vertex_index[(target_cell, 6)],
                    ),
                    "bond_rectangle",
                    (cell, axis),
                )
            )
    for cell in graph.cells:
        for first, second in combinations(range(3), 2):
            c10 = list(cell)
            c10[first] += 1
            c10 = tuple(c10)
            c01 = list(cell)
            c01[second] += 1
            c01 = tuple(c01)
            c11 = list(cell)
            c11[first] += 1
            c11[second] += 1
            c11 = tuple(c11)
            if not all(row in graph.cell_set for row in (c10, c01, c11)):
                continue
            rows.append(
                CycleDescriptor(
                    (
                        graph.vertex_index[(cell, 2 * first + 1)],
                        graph.vertex_index[(c10, 2 * first)],
                        graph.vertex_index[(c10, 2 * second + 1)],
                        graph.vertex_index[(c11, 2 * second)],
                        graph.vertex_index[(c11, 2 * first)],
                        graph.vertex_index[(c01, 2 * first + 1)],
                        graph.vertex_index[(c01, 2 * second)],
                        graph.vertex_index[(cell, 2 * second + 1)],
                    ),
                    "coarse_plaquette",
                    (cell, first, second),
                )
            )
    return tuple(rows)


def local_d(graph: ReferencePatchGraph, cell: Coord) -> base.Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def tree_path(source: int, target: int, parent: list[int | None]) -> list[int]:
    source_chain = []
    vertex: int | None = source
    while vertex is not None:
        source_chain.append(vertex)
        vertex = parent[vertex]
    target_chain = []
    vertex = target
    while vertex is not None:
        target_chain.append(vertex)
        vertex = parent[vertex]
    positions = {vertex: index for index, vertex in enumerate(source_chain)}
    common = next(vertex for vertex in target_chain if vertex in positions)
    return (
        source_chain[: positions[common] + 1]
        + list(reversed(target_chain[: target_chain.index(common)]))
    )


def fundamental_loop_rows(graph: ReferencePatchGraph) -> list[base.Pauli]:
    adjacency: list[list[tuple[int, int]]] = [[] for _ in graph.vertices]
    for edge, (u, v, _kind, _owner) in enumerate(graph.edges):
        adjacency[u].append((v, edge))
        adjacency[v].append((u, edge))
    for row in adjacency:
        row.sort()
    parent: list[int | None] = [None] * len(graph.vertices)
    seen = {0}
    queue = deque([0])
    tree_edges = set()
    while queue:
        u = queue.popleft()
        for v, edge in adjacency[u]:
            if v in seen:
                continue
            seen.add(v)
            parent[v] = u
            tree_edges.add(edge)
            queue.append(v)
    if len(seen) != len(graph.vertices):
        raise ValueError("graph is disconnected")
    return [
        graph.loop_pauli(tree_path(u, v, parent))
        for edge, (u, v, _kind, _owner) in enumerate(graph.edges)
        if edge not in tree_edges
    ]


def logical_rows(
    graph: ReferencePatchGraph,
    cell_order: tuple[Coord, ...] | None = None,
) -> tuple[list[base.Pauli], list[base.Pauli]]:
    logical_z = []
    logical_x = []
    for cell in graph.cells if cell_order is None else cell_order:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            matter = graph.vertex_index[(cell, mode)]
            logical_z.append(graph.B(matter))
            suffix = pauli_product(
                graph.B(graph.vertex_index[(cell, suffix_mode)])
                for suffix_mode in range(mode, 6)
            )
            logical_x.append(
                base.Pauli(phase=3) @ suffix @ graph.A(matter, reference)
            )
    return logical_z, logical_x


def dual_vectors(w_vectors: list[int], qubits: int) -> list[int]:
    pivots: dict[int, tuple[int, int]] = {}
    for index, vector in enumerate(w_vectors):
        mask = (vector >> qubits) | ((vector & ((1 << qubits) - 1)) << qubits)
        combination = 1 << index
        while mask:
            pivot = mask.bit_length() - 1
            if pivot in pivots:
                previous, previous_combination = pivots[pivot]
                mask ^= previous
                combination ^= previous_combination
            else:
                pivots[pivot] = (mask, combination)
                break
        else:
            raise ValueError("W rows are not independent")
    for pivot in sorted(pivots):
        pivot_mask, pivot_combination = pivots[pivot]
        for other in tuple(pivots):
            if other != pivot and (pivots[other][0] >> pivot) & 1:
                other_mask, other_combination = pivots[other]
                pivots[other] = (
                    other_mask ^ pivot_mask,
                    other_combination ^ pivot_combination,
                )
    duals = [0] * qubits
    for pivot, (_mask, combination) in pivots.items():
        while combination:
            bit = combination & -combination
            duals[bit.bit_length() - 1] |= 1 << pivot
            combination ^= bit
    return duals


def complete_tableau(
    w_rows: list[base.Pauli], explicit_x: list[base.Pauli], qubits: int
) -> list[base.Pauli]:
    w_vectors = [row.symplectic(qubits) for row in w_rows]
    vectors = dual_vectors(w_vectors, qubits)
    logical_count = len(explicit_x)
    for index, row in enumerate(explicit_x):
        vector = row.symplectic(qubits)
        if any(
            symplectic(vector, w_vectors[column], qubits) != int(index == column)
            for column in range(qubits)
        ):
            raise ValueError(("explicit logical X is not canonical", index))
        vectors[index] = vector
    for index in range(logical_count, qubits):
        vector = vectors[index]
        for logical in range(logical_count):
            if symplectic(vector, explicit_x[logical].symplectic(qubits), qubits):
                vector ^= w_vectors[logical]
        vectors[index] = vector
    for left in range(logical_count, qubits):
        for right in range(left + 1, qubits):
            if symplectic(vectors[left], vectors[right], qubits):
                vectors[left] ^= w_vectors[right]
    mask = (1 << qubits) - 1
    rows = list(explicit_x)
    for vector in vectors[logical_count:]:
        x, z = vector & mask, vector >> qubits
        rows.append(base.Pauli(phase=(x & z).bit_count() & 1, x=x, z=z))
    return rows


@dataclass(frozen=True)
class Coordinates:
    phase: int
    v_mask: int
    w_mask: int


def decode(
    row: base.Pauli,
    w_rows: list[base.Pauli],
    v_rows: list[base.Pauli],
    qubits: int,
) -> Coordinates:
    vector = row.symplectic(qubits)
    v_mask = sum(
        symplectic(vector, w.symplectic(qubits), qubits) << index
        for index, w in enumerate(w_rows)
    )
    w_mask = sum(
        symplectic(vector, v.symplectic(qubits), qubits) << index
        for index, v in enumerate(v_rows)
    )
    reconstructed = pauli_product(
        v_rows[index] for index in range(qubits) if (v_mask >> index) & 1
    ) @ pauli_product(
        w_rows[index] for index in range(qubits) if (w_mask >> index) & 1
    )
    if reconstructed.x != row.x or reconstructed.z != row.z:
        raise ValueError("tableau coordinate reconstruction failed")
    return Coordinates((row.phase - reconstructed.phase) % 4, v_mask, w_mask)


def encode(
    coordinates: Coordinates,
    w_rows: list[base.Pauli],
    v_rows: list[base.Pauli],
    qubits: int,
) -> base.Pauli:
    return (
        base.Pauli(phase=coordinates.phase)
        @ pauli_product(
            v_rows[index]
            for index in range(qubits)
            if (coordinates.v_mask >> index) & 1
        )
        @ pauli_product(
            w_rows[index]
            for index in range(qubits)
            if (coordinates.w_mask >> index) & 1
        )
    )


def canonical_failures(w_rows, v_rows, qubits: int) -> int:
    w = [row.symplectic(qubits) for row in w_rows]
    v = [row.symplectic(qubits) for row in v_rows]
    return sum(
        symplectic(w[left], w[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        symplectic(v[left], v[right], qubits)
        for left in range(qubits)
        for right in range(qubits)
    ) + sum(
        symplectic(v[left], w[right], qubits) != int(left == right)
        for left in range(qubits)
        for right in range(qubits)
    )


def edge_key(graph: ReferencePatchGraph, edge: int):
    u, v, kind, _owner = graph.edges[edge]
    return frozenset((graph.vertices[u], graph.vertices[v])), kind


def edge_digest(graph: ReferencePatchGraph) -> str:
    rows = [
        (graph.vertices[u], graph.vertices[v], kind, owner)
        for u, v, kind, owner in graph.edges
    ]
    return sha256(json.dumps(rows, separators=(",", ":")).encode()).hexdigest()


@dataclass
class Equivalence:
    cells: tuple[Coord, ...]
    open_graph: ReferencePatchGraph
    patch_graph: ReferencePatchGraph
    rail_labels: tuple[frozenset[tuple[Coord, int]], ...]
    natural_edge_map: dict[int, int]
    source_w: list[base.Pauli]
    source_v: list[base.Pauli]
    target_w: list[base.Pauli]
    target_v: list[base.Pauli]
    source_logical_z: list[base.Pauli]
    source_logical_x: list[base.Pauli]
    target_logical_z: list[base.Pauli]
    target_logical_x: list[base.Pauli]
    source_shared_loops: list[base.Pauli]
    target_shared_loops: list[base.Pauli]
    source_ds: list[base.Pauli]
    target_ds: list[base.Pauli]
    source_bond_loops: list[base.Pauli]
    target_rails: list[base.Pauli]

    @property
    def qubits(self) -> int:
        return len(self.open_graph.edges)

    @property
    def logical_count(self) -> int:
        return len(self.source_logical_z)

    @property
    def source_stabilizers(self) -> list[base.Pauli]:
        return self.source_w[self.logical_count :]

    @property
    def target_stabilizers(self) -> list[base.Pauli]:
        return self.target_w[self.logical_count :]

    def forward(self, row: base.Pauli) -> base.Pauli:
        return encode(
            decode(row, self.source_w, self.source_v, self.qubits),
            self.target_w,
            self.target_v,
            self.qubits,
        )

    def inverse(self, row: base.Pauli) -> base.Pauli:
        return encode(
            decode(row, self.target_w, self.target_v, self.qubits),
            self.source_w,
            self.source_v,
            self.qubits,
        )

    def natural(self, row: base.Pauli) -> base.Pauli:
        x = z = 0
        for source, target in self.natural_edge_map.items():
            if (row.x >> source) & 1:
                x |= 1 << target
            if (row.z >> source) & 1:
                z |= 1 << target
        return base.Pauli(row.phase, x, z)


def build_equivalence(cells: tuple[Coord, ...]) -> Equivalence:
    cells = tuple(cells)
    open_graph = ReferencePatchGraph(cells, True)
    patch_graph = ReferencePatchGraph(cells, False)
    patch_lookup = {
        edge_key(patch_graph, edge): edge for edge in range(len(patch_graph.edges))
    }
    natural_edge_map = {}
    reference_edges = []
    for edge in range(len(open_graph.edges)):
        key = edge_key(open_graph, edge)
        if key in patch_lookup:
            natural_edge_map[edge] = patch_lookup[key]
        elif key[1] == "reference_bond":
            reference_edges.append(edge)
        else:
            raise ValueError(("unmatched non-reference edge", key))
    for rail, edge in enumerate(reference_edges):
        natural_edge_map[edge] = len(patch_graph.edges) + rail
    if len(natural_edge_map) != len(open_graph.edges):
        raise ValueError("natural edge map is not bijective")

    descriptors = local_cycles(open_graph)
    source_shared_loops = []
    target_shared_loops = []
    source_bond_by_label = {}
    for descriptor in descriptors:
        source = open_graph.loop_pauli(descriptor.vertices)
        if descriptor.kind == "bond_rectangle":
            source_bond_by_label[descriptor.owner] = source
            continue
        source_shared_loops.append(source)
        target_vertices = tuple(
            patch_graph.vertex_index[open_graph.vertices[vertex]]
            for vertex in descriptor.vertices
        )
        target_shared_loops.append(patch_graph.loop_pauli(target_vertices))

    rail_labels = []
    source_bond_loops = []
    for edge in reference_edges:
        u, v, _kind, owner = open_graph.edges[edge]
        label = frozenset((open_graph.vertices[u], open_graph.vertices[v]))
        rail_labels.append(label)
        axis = next(
            axis
            for axis in range(3)
            if tuple(
                open_graph.vertices[v][0][component]
                - open_graph.vertices[u][0][component]
                for component in range(3)
            )
            in (
                tuple(int(component == axis) for component in range(3)),
                tuple(-int(component == axis) for component in range(3)),
            )
        )
        lower = min(open_graph.vertices[u][0], open_graph.vertices[v][0])
        source_bond_loops.append(source_bond_by_label[(lower, axis)])

    semantic_cell_order = open_graph.cells
    source_logical_z, source_logical_x = logical_rows(
        open_graph, semantic_cell_order
    )
    target_logical_z, target_logical_x = logical_rows(
        patch_graph, semantic_cell_order
    )
    source_ds = [local_d(open_graph, cell) for cell in semantic_cell_order[:-1]]
    target_ds = [local_d(patch_graph, cell) for cell in semantic_cell_order[:-1]]
    target_rails = [
        base.Pauli(z=1 << (len(patch_graph.edges) + rail))
        for rail in range(len(reference_edges))
    ]
    source_w = (
        source_logical_z
        + source_shared_loops
        + source_ds
        + source_bond_loops
    )
    target_w = (
        target_logical_z
        + target_shared_loops
        + target_ds
        + target_rails
    )
    qubits = len(open_graph.edges)
    if len(target_w) != qubits or len(source_w) != qubits:
        raise ValueError(("wrong canonical W count", len(source_w), len(target_w), qubits))
    source_v = complete_tableau(source_w, source_logical_x, qubits)
    target_v = complete_tableau(target_w, target_logical_x, qubits)
    return Equivalence(
        tuple(cells),
        open_graph,
        patch_graph,
        tuple(rail_labels),
        natural_edge_map,
        source_w,
        source_v,
        target_w,
        target_v,
        source_logical_z,
        source_logical_x,
        target_logical_z,
        target_logical_x,
        source_shared_loops,
        target_shared_loops,
        source_ds,
        target_ds,
        source_bond_loops,
        target_rails,
    )


def positive_span_status(row: base.Pauli, equivalence: Equivalence) -> str:
    coordinates = decode(
        row,
        equivalence.target_w,
        equivalence.target_v,
        equivalence.qubits,
    )
    logical_mask = (1 << equivalence.logical_count) - 1
    if coordinates.v_mask or (coordinates.w_mask & logical_mask):
        return "outside"
    return "positive" if coordinates.phase == 0 else "negative" if coordinates.phase == 2 else "nonhermitian"


def natural_map_controls(equivalence: Equivalence) -> dict[str, object]:
    qubits = equivalence.qubits
    mapped_source = [equivalence.natural(row) for row in equivalence.source_stabilizers]
    patch_stabilizers = (
        equivalence.target_shared_loops + equivalence.target_ds
    )
    rail_rows = {}
    for axis in "XYZ":
        rows = []
        for rail in range(len(equivalence.rail_labels)):
            qubit = len(equivalence.patch_graph.edges) + rail
            rows.append(
                base.Pauli(
                    phase=1 if axis == "Y" else 0,
                    x=(1 << qubit) if axis in "XY" else 0,
                    z=(1 << qubit) if axis in "YZ" else 0,
                )
            )
        target = patch_stabilizers + rows
        statuses = Counter()
        if axis == "Z":
            statuses.update(positive_span_status(row, equivalence) for row in mapped_source)
        rail_rows[axis] = {
            "target_rank": base.gf2_rank(row.symplectic(qubits) for row in target),
            "union_rank": base.gf2_rank(
                row.symplectic(qubits) for row in target + mapped_source
            ),
            "cross_commutator_failures": sum(
                not source.commutes(target_row)
                for source in mapped_source
                for target_row in target
            ),
            "Z_tableau_signed_status" if axis == "Z" else "signed_status_not_applicable": dict(statuses),
        }

    mixed_assignments = []
    for axes in product("XYZ", repeat=len(equivalence.rail_labels)):
        rows = []
        for rail, axis in enumerate(axes):
            qubit = len(equivalence.patch_graph.edges) + rail
            rows.append(
                base.Pauli(
                    phase=1 if axis == "Y" else 0,
                    x=(1 << qubit) if axis in "XY" else 0,
                    z=(1 << qubit) if axis in "YZ" else 0,
                )
            )
        target = patch_stabilizers + rows
        mixed_assignments.append(
            {
                "axes": "".join(axes),
                "union_rank": base.gf2_rank(
                    row.symplectic(qubits) for row in target + mapped_source
                ),
                "cross_commutator_failures": sum(
                    not source.commutes(target_row)
                    for source in mapped_source
                    for target_row in target
                ),
            }
        )

    natural_logical = {
        "logical_Z_exact_failures": sum(
            equivalence.natural(source) != target
            for source, target in zip(
                equivalence.source_logical_z, equivalence.target_logical_z
            )
        ),
        "logical_X_exact_failures": sum(
            equivalence.natural(source) != target
            for source, target in zip(
                equivalence.source_logical_x, equivalence.target_logical_x
            )
        ),
        "shared_loop_unsigned_failures": sum(
            equivalence.natural(source).x != target.x
            or equivalence.natural(source).z != target.z
            for source, target in zip(
                equivalence.source_shared_loops, equivalence.target_shared_loops
            )
        ),
        "shared_loop_signed_failures": sum(
            equivalence.natural(source) != target
            for source, target in zip(
                equivalence.source_shared_loops, equivalence.target_shared_loops
            )
        ),
    }
    exhaustive_rail = {
        "unsigned_axis_assignments": len(mixed_assignments),
        "minimum_union_rank": min(row["union_rank"] for row in mixed_assignments),
        "maximum_union_rank": max(row["union_rank"] for row in mixed_assignments),
        "minimum_cross_commutator_failures": min(
            row["cross_commutator_failures"] for row in mixed_assignments
        ),
        "maximum_cross_commutator_failures": max(
            row["cross_commutator_failures"] for row in mixed_assignments
        ),
        "exact_unsigned_assignments": sum(
            row["union_rank"] == 56 and row["cross_commutator_failures"] == 0
            for row in mixed_assignments
        ),
        "signed_axis_assignments": len(mixed_assignments)
        * (1 << len(equivalence.rail_labels)),
        "signed_assignments_rejected_by_support_or_coarse_loop_sign": len(mixed_assignments)
        * (1 << len(equivalence.rail_labels)),
    }
    check(
        "the natural edge relabeling fixes all matter logical pairs but all 1,296 signed independent single-Pauli rail codes fail",
        natural_logical["logical_Z_exact_failures"] == 0
        and natural_logical["logical_X_exact_failures"] == 0
        and natural_logical["shared_loop_unsigned_failures"] == 0
        and natural_logical["shared_loop_signed_failures"] == 1
        and all(row["union_rank"] > row["target_rank"] for row in rail_rows.values())
        and exhaustive_rail["unsigned_axis_assignments"] == 81
        and exhaustive_rail["exact_unsigned_assignments"] == 0
        and exhaustive_rail["signed_axis_assignments"] == 1296,
        {
            "logical_and_shared": natural_logical,
            "uniform_rail_axes": rail_rows,
            "exhaustive_independent_rail_scan": exhaustive_rail,
        },
    )
    return {
        "logical_and_shared": natural_logical,
        "uniform_rail_axes": rail_rows,
        "exhaustive_independent_rail_scan": exhaustive_rail,
    }


def target_support_cells(row: base.Pauli, equivalence: Equivalence) -> set[Coord]:
    cells = set()
    support = row.x | row.z
    patch_qubits = len(equivalence.patch_graph.edges)
    while support:
        bit = support & -support
        qubit = bit.bit_length() - 1
        if qubit < patch_qubits:
            u, v, _kind, _owner = equivalence.patch_graph.edges[qubit]
            cells.add(equivalence.patch_graph.vertices[u][0])
            cells.add(equivalence.patch_graph.vertices[v][0])
        else:
            for cell, _mode in equivalence.rail_labels[qubit - patch_qubits]:
                cells.add(cell)
        support ^= bit
    return cells


def cell_diameter(cells: set[Coord]) -> int:
    return max(
        (
            sum(abs(left[axis] - right[axis]) for axis in range(3))
            for left in cells
            for right in cells
        ),
        default=0,
    )


def candidate_controls(equivalence: Equivalence) -> dict[str, object]:
    qubits = equivalence.qubits
    logical = equivalence.logical_count
    source_rank = base.gf2_rank(row.symplectic(qubits) for row in equivalence.source_w)
    target_rank = base.gf2_rank(row.symplectic(qubits) for row in equivalence.target_w)
    source_phase_bad = base.stabilizer_phase_failures(
        equivalence.source_stabilizers, qubits
    )
    target_phase_bad = base.stabilizer_phase_failures(
        equivalence.target_stabilizers, qubits
    )
    semantic = {
        "logical_Z": (
            equivalence.source_logical_z,
            equivalence.target_logical_z,
        ),
        "logical_X": (
            equivalence.source_logical_x,
            equivalence.target_logical_x,
        ),
        "shared_loops": (
            equivalence.source_shared_loops,
            equivalence.target_shared_loops,
        ),
        "local_D": (equivalence.source_ds, equivalence.target_ds),
        "bond_to_rail_Z": (
            equivalence.source_bond_loops,
            equivalence.target_rails,
        ),
    }
    semantic_failures = {
        name: sum(equivalence.forward(source) != target for source, target in zip(*rows))
        for name, rows in semantic.items()
    }
    patch_fundamental = fundamental_loop_rows(equivalence.patch_graph)
    patch_fundamental_status = Counter(
        positive_span_status(row, equivalence) for row in patch_fundamental
    )

    edge_generators = []
    image_weights = []
    image_diameters = []
    inverse_failures = 0
    for qubit in range(qubits):
        for kind in "XZ":
            row = (
                base.Pauli(x=1 << qubit)
                if kind == "X"
                else base.Pauli(z=1 << qubit)
            )
            image = equivalence.forward(row)
            edge_generators.append((row, image))
            image_weights.append(pauli_weight(image))
            image_diameters.append(
                cell_diameter(target_support_cells(image, equivalence))
            )
            inverse_failures += equivalence.inverse(image) != row
    image_rank = base.gf2_rank(
        image.symplectic(qubits) for _source, image in edge_generators
    )
    multiplication_failures = 0
    for left, _left_image in edge_generators:
        for right, _right_image in edge_generators:
            multiplication_failures += (
                equivalence.forward(left @ right)
                != equivalence.forward(left) @ equivalence.forward(right)
            )

    deletion_ranks = {
        "source_bond_loop": sorted(
            {
                base.gf2_rank(
                    row.symplectic(qubits)
                    for index, row in enumerate(equivalence.source_w)
                    if index != logical + len(equivalence.source_shared_loops) + len(equivalence.source_ds) + deleted
                )
                for deleted in range(len(equivalence.source_bond_loops))
            }
        ),
        "target_rail_Z": sorted(
            {
                base.gf2_rank(
                    row.symplectic(qubits)
                    for index, row in enumerate(equivalence.target_w)
                    if index != logical + len(equivalence.target_shared_loops) + len(equivalence.target_ds) + deleted
                )
                for deleted in range(len(equivalence.target_rails))
            }
        ),
        "edge_map_any_generator_deleted": sorted(
            {
                base.gf2_rank(
                    image.symplectic(qubits)
                    for index, (_source, image) in enumerate(edge_generators)
                    if index != deleted
                )
                for deleted in range(len(edge_generators))
            }
        ),
    }
    sign_mutations_detected = 0
    for index, source in enumerate(equivalence.source_bond_loops):
        mutated = base.Pauli((source.phase + 2) % 4, source.x, source.z)
        sign_mutations_detected += (
            equivalence.forward(mutated)
            != equivalence.target_rails[index]
        )
    details = {
        "qubits": qubits,
        "logical_qubits": logical,
        "source_full_W_rank": source_rank,
        "target_full_W_rank": target_rank,
        "source_canonical_failures": canonical_failures(
            equivalence.source_w, equivalence.source_v, qubits
        ),
        "target_canonical_failures": canonical_failures(
            equivalence.target_w, equivalence.target_v, qubits
        ),
        "source_stabilizer_phase_failures": source_phase_bad,
        "target_stabilizer_phase_failures": target_phase_bad,
        "semantic_map_failures": semantic_failures,
        "patch_fundamental_loop_count": len(patch_fundamental),
        "patch_fundamental_signed_status": dict(patch_fundamental_status),
        "edge_generator_images": len(edge_generators),
        "edge_image_rank": image_rank,
        "inverse_failures": inverse_failures,
        "ordered_generator_pair_products": len(edge_generators) ** 2,
        "multiplication_failures": multiplication_failures,
        "image_weight_census": dict(sorted(Counter(image_weights).items())),
        "maximum_image_weight": max(image_weights),
        "maximum_image_cell_diameter": max(image_diameters),
        "deletion_ranks": deletion_ranks,
        "bond_sign_mutations_detected": sign_mutations_detected,
    }
    check(
        "the signed Clifford map fixes all 24 logical pairs and sends four bond checks to four prepared Z rails",
        source_rank == target_rank == qubits
        and details["source_canonical_failures"] == 0
        and details["target_canonical_failures"] == 0
        and source_phase_bad == target_phase_bad == 0
        and not any(semantic_failures.values())
        and patch_fundamental_status == {"positive": len(patch_fundamental)},
        details,
    )
    check(
        "the 160 graph-edge Pauli generators give a full-rank exact signed group isomorphism with exhaustive pair multiplication and inverse checks",
        image_rank == 2 * qubits
        and inverse_failures == 0
        and multiplication_failures == 0
        and deletion_ranks["edge_map_any_generator_deleted"] == [2 * qubits - 1],
        {
            key: details[key]
            for key in (
                "edge_generator_images",
                "edge_image_rank",
                "inverse_failures",
                "ordered_generator_pair_products",
                "multiplication_failures",
                "image_weight_census",
                "maximum_image_weight",
                "maximum_image_cell_diameter",
            )
        },
    )
    check(
        "deleting any bond/rail basis row loses one rank and every bond-sign mutation changes the prepared signed sector",
        deletion_ranks["source_bond_loop"] == [qubits - 1]
        and deletion_ranks["target_rail_Z"] == [qubits - 1]
        and sign_mutations_detected == len(equivalence.source_bond_loops),
        {
            "deletion_ranks": deletion_ranks,
            "bond_sign_mutations_detected": sign_mutations_detected,
        },
    )
    return details


def graph_transform_data(source, target, frame):
    direction = base.direction_map(frame)
    cell_map = {
        cell: tuple(int(value) for value in frame @ np.asarray(cell))
        for cell in source.cells
    }
    vertex_map = [
        target.vertex_index[(cell_map[cell], 6 if mode == 6 else direction[mode])]
        for cell, mode in source.vertices
    ]
    edge_map = [
        target.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _kind, _owner in source.edges
    ]
    toggles = [0] * len(target.edges)
    pairs = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[edge] for edge in source.incident[source_vertex]]
        position = {
            edge: index for index, edge in enumerate(target.incident[target_vertex])
        }
        for index, left in enumerate(pulled):
            for right in pulled[index + 1 :]:
                if position[left] > position[right]:
                    toggles[left] ^= 1 << right
                    toggles[right] ^= 1 << left
                    pairs.append((left, right))
    flips = 0
    failures = 0
    for source_edge, (u, v, _kind, _owner) in enumerate(source.edges):
        transformed = base.permute_pauli(source.A(u, v), edge_map)
        ordered = base.apply_gauge(transformed, toggles, pairs)
        expected = target.A(vertex_map[u], vertex_map[v])
        if ordered.x != expected.x or ordered.z != expected.z:
            failures += 1
        elif (ordered.phase - expected.phase) % 4 == 2:
            flips ^= 1 << edge_map[source_edge]
        elif ordered.phase != expected.phase:
            failures += 1
    return cell_map, direction, edge_map, toggles, pairs, flips, failures


def transform_graph_pauli(row, edge_map, toggles, pairs, flips):
    return base.apply_gauge(
        base.permute_pauli(row, edge_map), toggles, pairs, flips
    )


def transform_augmented_pauli(
    row: base.Pauli,
    source: Equivalence,
    target: Equivalence,
    patch_transform,
    cell_map,
) -> base.Pauli:
    patch_qubits = len(source.patch_graph.edges)
    patch_mask = (1 << patch_qubits) - 1
    _cells, _direction, edge_map, toggles, pairs, flips, _failures = patch_transform
    transformed = transform_graph_pauli(
        base.Pauli(row.phase, row.x & patch_mask, row.z & patch_mask),
        edge_map,
        toggles,
        pairs,
        flips,
    )
    target_rail_lookup = {
        label: index for index, label in enumerate(target.rail_labels)
    }
    x, z = transformed.x, transformed.z
    for rail, label in enumerate(source.rail_labels):
        mapped_label = frozenset((cell_map[cell], mode) for cell, mode in label)
        target_rail = target_rail_lookup[mapped_label]
        target_qubit = len(target.patch_graph.edges) + target_rail
        source_qubit = patch_qubits + rail
        if (row.x >> source_qubit) & 1:
            x |= 1 << target_qubit
        if (row.z >> source_qubit) & 1:
            z |= 1 << target_qubit
    return base.Pauli(transformed.phase, x, z)


def covariance_controls(equivalence: Equivalence) -> dict[str, object]:
    frames = base.proper_cubic_frames()
    frame_rows = []
    semantic_rows = (
        equivalence.source_logical_z
        + equivalence.source_logical_x
        + equivalence.source_stabilizers
    )
    for frame in frames:
        cells = tuple(
            tuple(int(value) for value in frame @ np.asarray(cell))
            for cell in equivalence.cells
        )
        target = build_equivalence(cells)
        open_transform = graph_transform_data(
            equivalence.open_graph, target.open_graph, frame
        )
        patch_transform = graph_transform_data(
            equivalence.patch_graph, target.patch_graph, frame
        )
        diagram_failures = 0
        for row in semantic_rows:
            transformed_source = transform_graph_pauli(
                row,
                open_transform[2],
                open_transform[3],
                open_transform[4],
                open_transform[5],
            )
            left = target.forward(transformed_source)
            right = transform_augmented_pauli(
                equivalence.forward(row),
                equivalence,
                target,
                patch_transform,
                patch_transform[0],
            )
            diagram_failures += left != right
        frame_rows.append(
            {
                "open_generator_transport_failures": open_transform[-1],
                "patch_generator_transport_failures": patch_transform[-1],
                "semantic_rows": len(semantic_rows),
                "equivalence_diagram_failures": diagram_failures,
                "source_canonical_failures": canonical_failures(
                    target.source_w, target.source_v, target.qubits
                ),
                "target_canonical_failures": canonical_failures(
                    target.target_w, target.target_v, target.qubits
                ),
            }
        )

    frame_lookup = {tuple(frame.flatten()): index for index, frame in enumerate(frames)}
    group_failures = 0
    rail_composition_failures = 0
    for left in frames:
        left_direction = base.direction_map(left)
        for right in frames:
            right_direction = base.direction_map(right)
            product_frame = left @ right
            group_failures += tuple(product_frame.flatten()) not in frame_lookup
            product_direction = base.direction_map(product_frame)
            group_failures += any(
                product_direction[mode]
                != left_direction[right_direction[mode]]
                for mode in range(6)
            )
            for label in equivalence.rail_labels:
                sequential = frozenset(
                    (
                        tuple(
                            int(value)
                            for value in left
                            @ (
                                right @ np.asarray(cell)
                            )
                        ),
                        mode,
                    )
                    for cell, mode in label
                )
                direct = frozenset(
                    (
                        tuple(int(value) for value in product_frame @ np.asarray(cell)),
                        mode,
                    )
                    for cell, mode in label
                )
                rail_composition_failures += sequential != direct
    details = {
        "proper_cubic_frames": len(frames),
        "frame_semantic_rows": sum(row["semantic_rows"] for row in frame_rows),
        "maximum_frame_row": {
            key: max(row[key] for row in frame_rows) for key in frame_rows[0]
        },
        "group_products": len(frames) ** 2,
        "group_failures": group_failures,
        "rail_group_composition_tests": len(frames) ** 2 * len(equivalence.rail_labels),
        "rail_group_composition_failures": rail_composition_failures,
    }
    check(
        "the code/logical equivalence diagram closes under all 24 proper frames and the frame/rail labels close under all 576 products",
        len(frames) == 24
        and all(
            row["open_generator_transport_failures"] == 0
            and row["patch_generator_transport_failures"] == 0
            and row["equivalence_diagram_failures"] == 0
            and row["source_canonical_failures"] == 0
            and row["target_canonical_failures"] == 0
            for row in frame_rows
        )
        and group_failures == 0
        and rail_composition_failures == 0,
        details,
    )
    return details


def geometry_controls() -> tuple[dict[str, object], Equivalence]:
    geometries = {
        "one_cell": ((0, 0, 0),),
        "one_edge": ((0, 0, 0), (1, 0, 0)),
        "L_triomino": ((0, 0, 0), (1, 0, 0), (1, 1, 0)),
        "held_2x2": (
            (0, 0, 0),
            (1, 0, 0),
            (1, 1, 0),
            (0, 1, 0),
        ),
    }
    rows = {}
    fixtures = {}
    for name, cells in geometries.items():
        fixture = build_equivalence(cells)
        fixtures[name] = fixture
        n = len(cells)
        adjacency = len(fixture.rail_labels)
        source_stabilizer_rank = base.gf2_rank(
            row.symplectic(fixture.qubits) for row in fixture.source_stabilizers
        )
        target_stabilizer_rank = base.gf2_rank(
            row.symplectic(fixture.qubits) for row in fixture.target_stabilizers
        )
        rows[name] = {
            "cells": n,
            "coarse_adjacencies": adjacency,
            "open_edge_qubits": len(fixture.open_graph.edges),
            "patch_edge_qubits": len(fixture.patch_graph.edges),
            "candidate_rails": len(fixture.rail_labels),
            "open_stabilizer_rank": source_stabilizer_rank,
            "patch_plus_rail_stabilizer_rank": target_stabilizer_rank,
            "logical_qubits": fixture.logical_count,
            "source_canonical_failures": canonical_failures(
                fixture.source_w, fixture.source_v, fixture.qubits
            ),
            "target_canonical_failures": canonical_failures(
                fixture.target_w, fixture.target_v, fixture.qubits
            ),
        }
    held = fixtures["held_2x2"]
    evidence = {
        "landed_cycle703_graph_source": "docs/RECURRENT_ENDPOINT_INCIDENCE_PHYSICAL_M2_COMPILER_TOURNAMENT_CYCLE703_NOTE_2026-07-25.md",
        "open_2x2_edge_digest": edge_digest(held.open_graph),
        "patch_path_2x2_edge_digest": edge_digest(held.patch_graph),
        "expected_open_digest": EXPECTED_OPEN_2X2_EDGE_DIGEST,
        "expected_patch_digest": EXPECTED_PATCH_PATH_2X2_EDGE_DIGEST,
    }
    check(
        "the independent reconstruction matches the landed Cycle703 2x2 graph digests and gives Open=Patch+one rail per coarse adjacency",
        evidence["open_2x2_edge_digest"] == evidence["expected_open_digest"]
        and evidence["patch_path_2x2_edge_digest"] == evidence["expected_patch_digest"]
        and all(
            row["open_edge_qubits"]
            == row["patch_edge_qubits"] + row["candidate_rails"]
            and row["candidate_rails"] == row["coarse_adjacencies"]
            and row["logical_qubits"] == 6 * row["cells"]
            and row["open_stabilizer_rank"]
            == row["patch_plus_rail_stabilizer_rank"]
            == row["open_edge_qubits"] - row["logical_qubits"]
            and row["source_canonical_failures"] == 0
            and row["target_canonical_failures"] == 0
            for row in rows.values()
        ),
        {"geometries": rows, "evidence": evidence},
    )
    return {"geometries": rows, "evidence": evidence}, held


def unlawful_domain_controls() -> dict[str, object]:
    rejected = 0
    for cells in (
        (),
        ((0, 0, 0), (0, 0, 0)),
        ((0, 0, 0), (2, 0, 0)),
    ):
        try:
            build_equivalence(cells)
        except ValueError:
            rejected += 1
    details = {
        "invalid_cases": 3,
        "invalid_rejections": rejected,
        "cases": ("empty", "duplicate", "disconnected"),
    }
    check(
        "empty, duplicate, and disconnected candidate domains are actively rejected",
        rejected == 3,
        details,
    )
    return details


def supplied_inventory() -> dict[str, object]:
    inventory = {
        "supplied": [
            "the landed Cycle703 graph definitions and their two edge-list digests",
            "the 2x2 cell set and its finite coordinate chart",
            "the six-mode intra-cell Fock order",
            "the local edge order used by the BKSF A generators",
            "the +1 loop, D, and prepared rail-Z characters",
            "a deterministic free-zero symplectic tableau completion",
        ],
        "derived": [
            "the 76 shared-edge bijection and four reference-bond rail labels",
            "the signed canonical bases and exact Clifford Pauli map",
            "the natural-map signed-sector falsifier",
            "the 24 individual-frame semantic covariance diagrams and 576-product direction/rail-label composition",
            "all ranks, inverse checks, multiplication checks, and deletion residuals",
        ],
        "open": [
            "a bounded recurrent Clifford circuit implementing the ambient tableau map",
            "an all-volume natural family with constant support independent of patch size",
            "composition with preparation controller, stream repetition, and literal Z3/M2 placement",
            "autonomous generation of the rail-Z reference state",
        ],
        "not_claimed": [
            "the direct edge relabeling is not an equivalence",
            "the finite tableau map is not called a local physical-site compiler",
            "no minimum four-rail content or graph-level impossibility is claimed",
            "no compiler order is called time and no stabilizer sign is called energy",
        ],
    }
    check(
        "the supplied, derived, open, and not-claimed inventories are explicit",
        all(inventory.values()),
        inventory,
    )
    return inventory


def main() -> int:
    print("CYCLE 706 OPENREFERENCEGRAPH 80 <-> PATCHGRAPH 76+4 EQUIVALENCE")
    REPORT["geometry"], equivalence = geometry_controls()
    REPORT["natural_map"] = natural_map_controls(equivalence)
    REPORT["signed_clifford_candidate"] = candidate_controls(equivalence)
    REPORT["covariance"] = covariance_controls(equivalence)
    REPORT["unlawful_domain"] = unlawful_domain_controls()
    REPORT["inventory"] = supplied_inventory()
    REPORT["disposition"] = {
        "natural_direct_relabeling": "falsified on the exact signed 2x2 code",
        "finite_signed_Clifford_equivalence": "constructed",
        "local_recurrent_equivalence": "open",
        "broad_no_go": False,
        "axiom_pressure": False,
        "authority": "none",
        "audit": "unset",
    }
    REPORT["checks"] = {"pass": PASS, "fail": FAIL}
    print("\nCYCLE706_REPORT_JSON")
    print(
        json.dumps(
            REPORT,
            indent=2,
            sort_keys=True,
            default=lambda value: (
                int(value)
                if isinstance(value, np.integer)
                else float(value)
                if isinstance(value, np.floating)
                else list(value)
                if isinstance(value, tuple)
                else str(value)
            ),
        )
    )
    print(f"SUMMARY pass={PASS} fail={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
