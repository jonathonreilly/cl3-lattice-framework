#!/usr/bin/env python3
"""Minimal signed-Pauli graph/tableau substrate needed by Cycle708.

This is a local extraction of the finite graph and canonical-basis machinery;
it deliberately omits the larger Cycle706 runner and every unrelated probe.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, permutations, product

import numpy as np


@dataclass(frozen=True)
class Pauli:
    phase: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, other: "Pauli") -> "Pauli":
        phase = (self.phase + other.phase + 2 * (self.z & other.x).bit_count()) % 4
        return Pauli(phase, self.x ^ other.x, self.z ^ other.z)

    def symplectic(self, qubits: int) -> int:
        return self.x | (self.z << qubits)


def gf2_rank(rows) -> int:
    pivots: dict[int, int] = {}
    for original in rows:
        row = int(original)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


DIRECTIONS = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for permutation in permutations(range(3)):
        matrix = np.zeros((3, 3), dtype=int)
        matrix[np.arange(3), permutation] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ matrix
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def direction_map(frame: np.ndarray) -> dict[int, int]:
    lookup = {direction: index for index, direction in enumerate(DIRECTIONS)}
    return {
        index: lookup[tuple(int(value) for value in frame @ np.asarray(direction))]
        for index, direction in enumerate(DIRECTIONS)
    }


class _Base:
    Pauli = Pauli
    gf2_rank = staticmethod(gf2_rank)
    proper_cubic_frames = staticmethod(proper_cubic_frames)
    direction_map = staticmethod(direction_map)


base = _Base()


Coord = tuple[int, int, int]
REVERSE = (1, 0, 3, 2, 5, 4)


def pauli_product(rows) -> base.Pauli:
    result = base.Pauli()
    for row in rows:
        result = result @ row
    return result


def pauli_weight(row: base.Pauli) -> int:
    return (row.x | row.z).bit_count()


class ReferencePatchGraph:
    """Seven-vertex cells, optionally including local reference bonds."""

    def __init__(self, cells: tuple[Coord, ...], reference_bonds: bool):
        if not cells:
            raise ValueError("empty cell set")
        if len(set(cells)) != len(cells):
            raise ValueError("duplicate cells")
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
        self.cross_edges: list[tuple[Coord, int, int, int | None]] = []

        def add(u: int, v: int, kind: str, owner: Coord) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate graph edge", self.vertices[u], self.vertices[v]))
            edge = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = edge
            return edge

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] != right:
                    add(
                        self.vertex_index[(cell, left)],
                        self.vertex_index[(cell, right)],
                        "octahedral", cell,
                    )
            reference = self.vertex_index[(cell, 6)]
            for mode in range(6):
                add(reference, self.vertex_index[(cell, mode)], "spoke", cell)
        for cell in self.cells:
            for axis in range(3):
                target = list(cell)
                target[axis] += 1
                target_cell = tuple(target)
                if target_cell not in self.cell_set:
                    continue
                matter = add(
                    self.vertex_index[(cell, 2 * axis + 1)],
                    self.vertex_index[(target_cell, 2 * axis)],
                    "matter_stream", cell,
                )
                reference = None
                if reference_bonds:
                    reference = add(
                        self.vertex_index[(cell, 6)],
                        self.vertex_index[(target_cell, 6)],
                        "reference_bond", cell,
                    )
                self.cross_edges.append((cell, axis, matter, reference))
        self.incident: list[list[int]] = [[] for _ in self.vertices]
        adjacency = {cell: set() for cell in self.cells}
        for edge, (u, v, _kind, _owner) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()
        for cell, axis, _matter, _reference in self.cross_edges:
            target = list(cell)
            target[axis] += 1
            target_cell = tuple(target)
            adjacency[cell].add(target_cell)
            adjacency[target_cell].add(cell)
        seen = {self.cells[0]}
        queue = deque(seen)
        while queue:
            cell = queue.popleft()
            for target in adjacency[cell] - seen:
                seen.add(target)
                queue.append(target)
        if len(seen) != len(self.cells):
            raise ValueError("cell set is disconnected")

    def edge_between(self, source: int, target: int) -> int:
        return self.edge_lookup[frozenset((source, target))]

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

    def loop_pauli(self, vertices) -> base.Pauli:
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
            if REVERSE[left] != right:
                rows.append(CycleDescriptor((
                    reference,
                    graph.vertex_index[(cell, left)],
                    graph.vertex_index[(cell, right)],
                ), "cell_triangle", cell))
    if graph.reference_bonds:
        for cell, axis, _matter, reference_edge in graph.cross_edges:
            if reference_edge is None:
                raise AssertionError("missing reference bond")
            target = list(cell)
            target[axis] += 1
            target_cell = tuple(target)
            rows.append(CycleDescriptor((
                graph.vertex_index[(cell, 6)],
                graph.vertex_index[(cell, 2 * axis + 1)],
                graph.vertex_index[(target_cell, 2 * axis)],
                graph.vertex_index[(target_cell, 6)],
            ), "bond_rectangle", (cell, axis)))
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
            if not all(candidate in graph.cell_set for candidate in (c10, c01, c11)):
                continue
            rows.append(CycleDescriptor((
                graph.vertex_index[(cell, 2 * first + 1)],
                graph.vertex_index[(c10, 2 * first)],
                graph.vertex_index[(c10, 2 * second + 1)],
                graph.vertex_index[(c11, 2 * second)],
                graph.vertex_index[(c11, 2 * first)],
                graph.vertex_index[(c01, 2 * first + 1)],
                graph.vertex_index[(c01, 2 * second)],
                graph.vertex_index[(cell, 2 * second + 1)],
            ), "coarse_plaquette", (cell, first, second)))
    return tuple(rows)


def local_d(graph: ReferencePatchGraph, cell: Coord) -> base.Pauli:
    return pauli_product(graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7))


def _tree_path(source: int, target: int, parent: list[int | None]) -> list[int]:
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
    return source_chain[:positions[common] + 1] + list(
        reversed(target_chain[:target_chain.index(common)])
    )


def logical_rows(graph: ReferencePatchGraph, cell_order: tuple[Coord, ...]):
    logical_z = []
    logical_x = []
    for cell in cell_order:
        reference = graph.vertex_index[(cell, 6)]
        for mode in range(6):
            matter = graph.vertex_index[(cell, mode)]
            logical_z.append(graph.B(matter))
            suffix = pauli_product(
                graph.B(graph.vertex_index[(cell, suffix_mode)])
                for suffix_mode in range(mode, 6)
            )
            logical_x.append(base.Pauli(phase=3) @ suffix @ graph.A(matter, reference))
    return logical_z, logical_x


def _symplectic(left: int, right: int, qubits: int) -> int:
    mask = (1 << qubits) - 1
    lx, lz = left & mask, left >> qubits
    rx, rz = right & mask, right >> qubits
    return ((lx & rz).bit_count() + (lz & rx).bit_count()) & 1


def _dual_vectors(w_vectors: list[int], qubits: int) -> list[int]:
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
                pivots[other] = other_mask ^ pivot_mask, other_combination ^ pivot_combination
    duals = [0] * qubits
    for pivot, (_mask, combination) in pivots.items():
        while combination:
            bit = combination & -combination
            duals[bit.bit_length() - 1] |= 1 << pivot
            combination ^= bit
    return duals


def complete_tableau(w_rows, explicit_x, qubits: int):
    w_vectors = [row.symplectic(qubits) for row in w_rows]
    vectors = _dual_vectors(w_vectors, qubits)
    logical_count = len(explicit_x)
    for index, row in enumerate(explicit_x):
        vector = row.symplectic(qubits)
        if any(
            _symplectic(vector, w_vectors[column], qubits) != int(index == column)
            for column in range(qubits)
        ):
            raise ValueError(("explicit logical X is not canonical", index))
        vectors[index] = vector
    for index in range(logical_count, qubits):
        vector = vectors[index]
        for logical in range(logical_count):
            if _symplectic(vector, explicit_x[logical].symplectic(qubits), qubits):
                vector ^= w_vectors[logical]
        vectors[index] = vector
    for left in range(logical_count, qubits):
        for right in range(left + 1, qubits):
            if _symplectic(vectors[left], vectors[right], qubits):
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


def decode(row, w_rows, v_rows, qubits: int) -> Coordinates:
    vector = row.symplectic(qubits)
    v_mask = sum(
        _symplectic(vector, w.symplectic(qubits), qubits) << index
        for index, w in enumerate(w_rows)
    )
    w_mask = sum(
        _symplectic(vector, v.symplectic(qubits), qubits) << index
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


def encode(coordinates: Coordinates, w_rows, v_rows, qubits: int):
    return base.Pauli(phase=coordinates.phase) @ pauli_product(
        v_rows[index] for index in range(qubits) if (coordinates.v_mask >> index) & 1
    ) @ pauli_product(
        w_rows[index] for index in range(qubits) if (coordinates.w_mask >> index) & 1
    )


def canonical_failures(w_rows, v_rows, qubits: int) -> int:
    w = [row.symplectic(qubits) for row in w_rows]
    v = [row.symplectic(qubits) for row in v_rows]
    return sum(_symplectic(w[i], w[j], qubits) for i in range(qubits) for j in range(qubits)) + sum(
        _symplectic(v[i], v[j], qubits) for i in range(qubits) for j in range(qubits)
    ) + sum(
        _symplectic(v[i], w[j], qubits) != int(i == j)
        for i in range(qubits) for j in range(qubits)
    )


def edge_key(graph: ReferencePatchGraph, edge: int):
    u, v, kind, _owner = graph.edges[edge]
    return frozenset((graph.vertices[u], graph.vertices[v])), kind


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

    def forward(self, row):
        return encode(
            decode(row, self.source_w, self.source_v, self.qubits),
            self.target_w, self.target_v, self.qubits,
        )

    def inverse(self, row):
        return encode(
            decode(row, self.target_w, self.target_v, self.qubits),
            self.source_w, self.source_v, self.qubits,
        )


def target_support_cells(row, equivalence: Equivalence) -> set[Coord]:
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
            cells.update(cell for cell, _mode in equivalence.rail_labels[qubit - patch_qubits])
        support ^= bit
    return cells


def cell_diameter(cells: set[Coord]) -> int:
    return max((
        sum(abs(a - b) for a, b in zip(left, right))
        for left in cells for right in cells
    ), default=0)
