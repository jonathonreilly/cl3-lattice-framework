#!/usr/bin/env python3
"""Literal Z3/M2 placement and fixed-controller probe for a 2x2 PatchGraph.

The probe independently rebuilds the corrected open 2x2 graph (76 abstract
edge qubits), places it in the spacing-16 Cycle-232 macro-geometry, compiles
one nontrivial scheduled two-cell factor, and instantiates the Cycle-655 and
Cycle-656 controller grammars on that finite word.  The construction is
bounded and conditional on its declared chart, ordering, program, and genesis.
It is not a recurrent lattice compiler or a local preparation theorem.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from hashlib import sha256
from itertools import combinations, product
import math
from pathlib import Path
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import frontier_full128_25site_nn_circuit_core_2026_07_24 as c655
import frontier_literal_patchgraph_cycle656_projected_trace_cycle707_2026_07_26 as c707trace
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210


NOTE = ROOT / (
    "docs/LITERAL_PATCHGRAPH_Z3_M2_PLACEMENT_AND_FIXED_CONTROLLER_"
    "CYCLE707_BOUNDED_THEOREM_NOTE_2026-07-26.md"
)


PASS = 0
FAIL = 0
TOL = 4.0e-10
REVERSE = (1, 0, 3, 2, 5, 4)
DIRECTIONS = tuple(tuple(int(v) for v in row) for row in c210.DIRECTIONS)
EXPECTED_PHYSICAL_SCHEDULE_DIGEST = (
    "f90bc5256e8c6e16863870c1445029fc793f3e259c7814687e55db6d221e8d22"
)
SEGMENT_KEY = ("stream", 3, 0)
SEGMENT_ANGLE = 0.37


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "**type:** bounded_theorem",
        "**authority:** none",
        "**audit:** unset",
        "76 abstract graph-edge qubits",
        "80 occupied physical m2 sites",
        "84 occupied physical m2 sites",
        "cycle-655",
        "cycle-656",
        "cycle-706",
        "supplied origin",
        "supplied coframe",
        "supplied order",
        "supplied schedule",
        "n1 — alternative routes",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — exact residual matching",
        "n5 — resolution and rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no route-independent no-go",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the bounded claim and N1-N8 boundary", not missing, missing)


Coord = tuple[int, int, int]


@dataclass(frozen=True)
class Pauli:
    phase: int = 0
    x: int = 0
    z: int = 0

    def __matmul__(self, other: "Pauli") -> "Pauli":
        phase = (self.phase + other.phase + 2 * (self.z & other.x).bit_count()) % 4
        return Pauli(phase, self.x ^ other.x, self.z ^ other.z)

    def commutes(self, other: "Pauli") -> bool:
        return (
            (self.x & other.z).bit_count() + (self.z & other.x).bit_count()
        ) % 2 == 0


def pauli_product(rows) -> Pauli:
    result = Pauli()
    for row in rows:
        result = result @ row
    return result


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


def square_cells(size: int) -> tuple[Coord, ...]:
    cells = []
    for y in range(size):
        xs = range(size) if y % 2 == 0 else range(size - 1, -1, -1)
        cells.extend((x, y, 0) for x in xs)
    return tuple(cells)


class PatchGraph:
    """Six matter modes plus one scalar reference, without reference bonds."""

    def __init__(self, cells: tuple[Coord, ...]):
        if len(set(cells)) != len(cells):
            raise ValueError("duplicate cell")
        self.cells = tuple(cells)
        self.cell_set = set(cells)
        self.cell_index = {cell: index for index, cell in enumerate(cells)}
        self.vertices: list[tuple[Coord, int]] = []
        self.vertex_index: dict[tuple[Coord, int], int] = {}
        for cell in self.cells:
            for mode in range(7):
                key = (cell, mode)
                self.vertex_index[key] = len(self.vertices)
                self.vertices.append(key)

        self.edges: list[tuple[int, int, str, Coord]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.stream_edges: list[tuple[int, Coord, Coord, int, int, int]] = []

        def add(u: int, v: int, kind: str, owner: Coord) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError("duplicate graph edge")
            edge = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = edge
            return edge

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] == right:
                    continue
                add(
                    self.vertex_index[(cell, left)],
                    self.vertex_index[(cell, right)],
                    "octahedral",
                    cell,
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
                source_mode = 2 * axis + 1
                target_mode = 2 * axis
                edge = add(
                    self.vertex_index[(cell, source_mode)],
                    self.vertex_index[(target_cell, target_mode)],
                    "matter_stream",
                    cell,
                )
                self.stream_edges.append(
                    (edge, cell, target_cell, source_mode, target_mode, axis)
                )

        self.incident: list[list[int]] = [[] for _ in self.vertices]
        for edge, (u, v, _, _) in enumerate(self.edges):
            self.incident[u].append(edge)
            self.incident[v].append(edge)
        for row in self.incident:
            row.sort()

    def edge_between(self, u: int, v: int) -> int:
        return self.edge_lookup[frozenset((u, v))]

    def B(self, vertex: int) -> Pauli:
        z = 0
        for edge in self.incident[vertex]:
            z ^= 1 << edge
        return Pauli(z=z)

    def A(self, source: int, target: int) -> Pauli:
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        return Pauli(0 if source < target else 2, 1 << edge, z)

    def loop_pauli(self, vertices: list[int]) -> Pauli:
        result = Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(source, vertices[(index + 1) % len(vertices)])
        return result


def tree_path(source: int, target: int, parent: list[int | None]) -> list[int]:
    left = []
    vertex: int | None = source
    while vertex is not None:
        left.append(vertex)
        vertex = parent[vertex]
    right = []
    vertex = target
    while vertex is not None:
        right.append(vertex)
        vertex = parent[vertex]
    positions = {vertex: index for index, vertex in enumerate(left)}
    common = next(vertex for vertex in right if vertex in positions)
    return left[: positions[common] + 1] + list(
        reversed(right[: right.index(common)])
    )


def fundamental_loops(graph: PatchGraph) -> list[Pauli]:
    adjacency: list[list[tuple[int, int]]] = [[] for _ in graph.vertices]
    for edge, (u, v, _, _) in enumerate(graph.edges):
        adjacency[u].append((v, edge))
        adjacency[v].append((u, edge))
    for row in adjacency:
        row.sort()
    parent: list[int | None] = [None] * len(graph.vertices)
    seen = {0}
    queue = deque((0,))
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
        raise ValueError("disconnected patch")
    return [
        graph.loop_pauli(tree_path(u, v, parent))
        for edge, (u, v, _, _) in enumerate(graph.edges)
        if edge not in tree_edges
    ]


def local_d(graph: PatchGraph, cell: Coord) -> Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(cell, mode)]) for mode in range(7)
    )


def stabilizers(graph: PatchGraph) -> list[Pauli]:
    return fundamental_loops(graph) + [
        local_d(graph, cell) for cell in graph.cells[:-1]
    ]


def pauli_weight(row: Pauli) -> int:
    return (row.x | row.z).bit_count()


def greedy_localize(row: Pauli, basis: list[Pauli]) -> tuple[Pauli, int]:
    current = row
    mask = 0
    while True:
        weight = pauli_weight(current)
        choices = []
        for index, stabilizer in enumerate(basis):
            candidate = current @ stabilizer
            if pauli_weight(candidate) < weight:
                choices.append((pauli_weight(candidate), index, candidate))
        if not choices:
            break
        _, index, current = min(choices, key=lambda item: (item[0], item[1]))
        mask ^= 1 << index
    reconstructed = row @ pauli_product(
        basis[index] for index in range(len(basis)) if (mask >> index) & 1
    )
    if reconstructed != current:
        raise ValueError("localization certificate failed")
    return current, mask


def intermediate_parity(graph: PatchGraph, left: int, right: int) -> Pauli:
    return pauli_product(
        graph.B(graph.vertex_index[(graph.cells[index], mode)])
        for index in range(left + 1, right)
        for mode in range(6)
    )


def stream_terms(
    graph: PatchGraph,
    source_cell: Coord,
    target_cell: Coord,
    source_mode: int,
    target_mode: int,
) -> tuple[Pauli, Pauli]:
    source_index = graph.cell_index[source_cell]
    target_index = graph.cell_index[target_cell]
    if source_index < target_index:
        left_cell, left_mode = source_cell, source_mode
        right_cell, right_mode = target_cell, target_mode
        left_index, right_index = source_index, target_index
    else:
        left_cell, left_mode = target_cell, target_mode
        right_cell, right_mode = source_cell, source_mode
        left_index, right_index = target_index, source_index
    u = graph.vertex_index[(left_cell, left_mode)]
    v = graph.vertex_index[(right_cell, right_mode)]
    ru = graph.vertex_index[(left_cell, 6)]
    rv = graph.vertex_index[(right_cell, 6)]
    core = graph.A(ru, u) @ graph.A(v, rv)
    between = intermediate_parity(graph, left_index, right_index)
    spectator = pauli_product(
        graph.B(graph.vertex_index[(right_cell, mode)])
        for mode in range(6)
        if mode != right_mode
    )
    return (
        Pauli(phase=2) @ between @ spectator @ core,
        between @ spectator @ graph.B(u) @ graph.B(v) @ core,
    )


@dataclass(frozen=True)
class ScheduledFactor:
    key: tuple[object, ...]
    kind: str
    rows: tuple[Pauli, ...]
    support: int


def factor_schedule(graph: PatchGraph) -> tuple[list[ScheduledFactor], list[int], int]:
    basis = stabilizers(graph)
    factors: list[ScheduledFactor] = []

    def append(key, kind, rows) -> None:
        localized = tuple(greedy_localize(row, basis)[0] for row in rows)
        if any(not row.commutes(stabilizer) for row in localized for stabilizer in basis):
            raise ValueError("scheduled factor leaves code")
        support = 0
        for row in localized:
            support |= row.x | row.z
        factors.append(ScheduledFactor(tuple(key), kind, localized, support))

    for cell_index, cell in enumerate(graph.cells):
        for left, right in combinations(range(6), 2):
            if REVERSE[left] == right:
                continue
            u = graph.vertex_index[(cell, left)]
            v = graph.vertex_index[(cell, right)]
            a = graph.A(u, v)
            append(
                ("coin", cell_index, left, right),
                "onsite_coin",
                (Pauli(phase=3) @ graph.B(u) @ a, Pauli(phase=1) @ graph.B(v) @ a),
            )
    for stream_index, (_, source, target, smode, tmode, axis) in enumerate(
        graph.stream_edges
    ):
        append(
            ("stream", stream_index, axis),
            "directed_seam",
            stream_terms(graph, source, target, smode, tmode),
        )
    for cell_index, cell in enumerate(graph.cells):
        for left, right in combinations(range(6), 2):
            row = graph.B(graph.vertex_index[(cell, left)]) @ graph.B(
                graph.vertex_index[(cell, right)]
            )
            append(("contact", cell_index, left, right), "onsite_contact", (row,))

    layers: list[int] = []
    colors = []
    for factor in factors:
        for color, occupied in enumerate(layers):
            if not (factor.support & occupied):
                break
        else:
            color = len(layers)
            layers.append(0)
        colors.append(color)
        layers[color] |= factor.support
    collisions = sum(
        bool(left.support & right.support)
        for i, left in enumerate(factors)
        for j, right in enumerate(factors)
        if i < j and colors[i] == colors[j]
    )
    return factors, colors, collisions


def factor_digest(factors: list[ScheduledFactor], colors: list[int]) -> str:
    lines = []
    for factor, color in zip(factors, colors):
        payload = ";".join(f"{row.phase}:{row.x:x}:{row.z:x}" for row in factor.rows)
        lines.append(f"{color}:{factor.key}:{payload}")
    return sha256("\n".join(lines).encode("ascii")).hexdigest()


def edge_digest(graph: PatchGraph) -> str:
    lines = []
    for index, (u, v, kind, owner) in enumerate(graph.edges):
        lines.append(f"{index}:{graph.vertices[u]}:{graph.vertices[v]}:{kind}:{owner}")
    return sha256("\n".join(lines).encode("ascii")).hexdigest()


def center_shift(cells: tuple[Coord, ...]) -> np.ndarray:
    minimum = np.min(np.asarray(cells, dtype=int), axis=0)
    maximum = np.max(np.asarray(cells, dtype=int), axis=0)
    return 8 * (minimum + maximum)


def placement(
    graph: PatchGraph,
    origin: Coord = (0, 0, 0),
    frame: np.ndarray | None = None,
    include_edge_gauge: bool = False,
) -> tuple[dict[int, tuple[Coord, ...]], dict[int, Coord]]:
    frame = np.eye(3, dtype=int) if frame is None else np.asarray(frame, dtype=int)
    origin_array = np.asarray(origin, dtype=int)
    shift = center_shift(graph.cells)
    abstract: dict[int, tuple[Coord, ...]] = {}
    gauges: dict[int, Coord] = {}
    stream_by_edge = {row[0]: row for row in graph.stream_edges}
    for edge, (u, v, kind, owner) in enumerate(graph.edges):
        center = origin_array + frame @ (16 * np.asarray(owner, dtype=int) - shift)
        if kind == "octahedral":
            left = graph.vertices[u][1]
            right = graph.vertices[v][1]
            offset = 2 * (np.asarray(DIRECTIONS[left]) + np.asarray(DIRECTIONS[right]))
            sites = (tuple(int(x) for x in center + frame @ offset),)
        elif kind == "spoke":
            mode = graph.vertices[v][1] if graph.vertices[v][1] != 6 else graph.vertices[u][1]
            offset = 4 * np.asarray(DIRECTIONS[mode])
            sites = (tuple(int(x) for x in center + frame @ offset),)
        else:
            axis = stream_by_edge[edge][-1]
            direction = np.eye(3, dtype=int)[axis]
            sites = (
                tuple(int(x) for x in center + frame @ (7 * direction)),
                tuple(int(x) for x in center + frame @ (9 * direction)),
            )
            if include_edge_gauge:
                gauges[edge] = tuple(int(x) for x in center + frame @ (8 * direction))
        abstract[edge] = sites
    return abstract, gauges


def occupied_sites(site_map: dict[int, tuple[Coord, ...]], gauges: dict[int, Coord] | None = None) -> set[Coord]:
    output = {site for sites in site_map.values() for site in sites}
    if gauges:
        output.update(gauges.values())
    return output


def physical_pauli(row: Pauli, graph: PatchGraph, site_map: dict[int, tuple[Coord, ...]]) -> tuple[Pauli, tuple[Coord, ...]]:
    sites = tuple(sorted(occupied_sites(site_map)))
    index = {site: position for position, site in enumerate(sites)}
    x = z = 0
    for edge, carriers in site_map.items():
        if (row.x >> edge) & 1:
            for carrier in carriers:
                x ^= 1 << index[carrier]
        if (row.z >> edge) & 1:
            z ^= 1 << index[carriers[0]]
    return Pauli(row.phase, x, z), sites


def repetition_controls() -> dict[str, float]:
    embedding = np.asarray(((1, 0), (0, 0), (0, 0), (0, 1)), dtype=complex)
    x = c655.X
    z = np.diag((1, -1)).astype(complex)
    exact = max(
        np.linalg.norm(np.kron(x, x) @ embedding - embedding @ x),
        np.linalg.norm(np.kron(z, c655.I2) @ embedding - embedding @ z),
    )
    deleted = np.linalg.norm(np.kron(x, c655.I2) @ embedding - embedding @ x)
    return {"exact_residual": float(exact), "delete_second_X_residual": float(deleted)}


def l1_diameter(points: set[Coord]) -> int:
    return max(
        (sum(abs(a - b) for a, b in zip(left, right)) for left in points for right in points),
        default=0,
    )


@dataclass(frozen=True)
class Instruction:
    kind: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray


S_GATE = np.diag((1, 1j)).astype(complex)
SDG_GATE = S_GATE.conj().T


def rz(angle: float) -> np.ndarray:
    return np.diag((np.exp(-0.5j * angle), np.exp(0.5j * angle))).astype(complex)


def pauli_axes(row: Pauli, sites: tuple[Coord, ...]) -> tuple[list[tuple[Coord, str]], int]:
    axes = []
    y_count = 0
    for index, site in enumerate(sites):
        x = (row.x >> index) & 1
        z = (row.z >> index) & 1
        if x and z:
            axes.append((site, "Y"))
            y_count += 1
        elif x:
            axes.append((site, "X"))
        elif z:
            axes.append((site, "Z"))
    exponent = (row.phase - y_count) % 4
    if exponent not in (0, 2):
        raise ValueError(("non-Hermitian scheduled Pauli", exponent))
    return axes, 1 if exponent == 0 else -1


def compile_pauli_rotation(row: Pauli, sites: tuple[Coord, ...], angle: float) -> tuple[Instruction, ...]:
    axes, sign = pauli_axes(row, sites)
    pivot = axes[0][0]
    word: list[Instruction] = []
    for site, axis in axes:
        if axis == "X":
            word.append(Instruction("basis_H", (site,), c655.H))
        elif axis == "Y":
            word.append(Instruction("basis_Sdg", (site,), SDG_GATE))
            word.append(Instruction("basis_H", (site,), c655.H))
    for site, _ in axes[1:]:
        word.append(Instruction("parity_CNOT", (site, pivot), c655.CNOT))
    word.append(Instruction("axis_RZ", (pivot,), rz(sign * angle)))
    for site, _ in reversed(axes[1:]):
        word.append(Instruction("parity_CNOT", (site, pivot), c655.CNOT))
    for site, axis in reversed(axes):
        if axis == "X":
            word.append(Instruction("basis_H", (site,), c655.H))
        elif axis == "Y":
            word.append(Instruction("basis_H", (site,), c655.H))
            word.append(Instruction("basis_S", (site,), S_GATE))
    return tuple(word)


def apply_gate(state: np.ndarray, matrix: np.ndarray, wires: tuple[int, ...], count: int) -> np.ndarray:
    wire_axes = [count - 1 - wire for wire in wires]
    local_axes = list(reversed(wire_axes))
    other = [axis for axis in range(count) if axis not in local_axes]
    order = other + local_axes
    inverse = np.argsort(order)
    tensor = state.reshape((2,) * count).transpose(order)
    flat = tensor.reshape((-1, 1 << len(wires)))
    updated = flat @ matrix.T
    return updated.reshape(tensor.shape).transpose(inverse).reshape(-1)


def apply_pauli(state: np.ndarray, row: Pauli, count: int) -> np.ndarray:
    output = state
    for wire in range(count):
        x = (row.x >> wire) & 1
        z = (row.z >> wire) & 1
        if x or z:
            matrix = np.linalg.matrix_power(c655.X, x) @ np.linalg.matrix_power(
                np.diag((1, -1)).astype(complex), z
            )
            output = apply_gate(output, matrix, (wire,), count)
    return (1j ** row.phase) * output


def direct_rotation(state: np.ndarray, row: Pauli, angle: float, count: int) -> np.ndarray:
    return math.cos(angle / 2) * state - 1j * math.sin(angle / 2) * apply_pauli(
        state, row, count
    )


def execute_segment(rows: tuple[Pauli, Pauli], all_sites: tuple[Coord, ...]) -> dict[str, object]:
    union = tuple(
        site
        for index, site in enumerate(all_sites)
        if any(((row.x | row.z) >> index) & 1 for row in rows)
    )
    union_index = {site: index for index, site in enumerate(union)}

    def restrict(row: Pauli) -> Pauli:
        x = z = 0
        for global_index, site in enumerate(all_sites):
            if site not in union_index:
                continue
            local = union_index[site]
            x |= ((row.x >> global_index) & 1) << local
            z |= ((row.z >> global_index) & 1) << local
        return Pauli(row.phase, x, z)

    local_rows = tuple(restrict(row) for row in rows)
    abstract_word = tuple(
        instruction
        for row in local_rows
        for instruction in compile_pauli_rotation(row, union, SEGMENT_ANGLE)
    )
    rng = np.random.default_rng(707)
    residuals = []
    deleted_residuals = []
    for sample in range(4):
        if sample == 0:
            state = np.zeros(1 << len(union), dtype=complex)
            state[0] = 1
        else:
            state = rng.normal(size=1 << len(union)) + 1j * rng.normal(size=1 << len(union))
            state /= np.linalg.norm(state)
        direct = state
        for row in local_rows:
            direct = direct_rotation(direct, row, SEGMENT_ANGLE, len(union))
        compiled = state
        for instruction in abstract_word:
            wires = tuple(union_index[site] for site in instruction.sites)
            compiled = apply_gate(compiled, instruction.matrix, wires, len(union))
        residuals.append(float(np.linalg.norm(compiled - direct)))
        deleted = state
        deleted_word = tuple(
            instruction for instruction in abstract_word if instruction.kind != "axis_RZ"
        )
        for instruction in deleted_word:
            wires = tuple(union_index[site] for site in instruction.sites)
            deleted = apply_gate(deleted, instruction.matrix, wires, len(union))
        deleted_residuals.append(float(np.linalg.norm(deleted - direct)))
    return {
        "union_sites": len(union),
        "row_weights": tuple(pauli_weight(row) for row in local_rows),
        "rows_commute": local_rows[0].commutes(local_rows[1]),
        "abstract_gate_count": len(abstract_word),
        "maximum_execution_residual": max(residuals),
        "minimum_delete_all_RZ_residual": min(deleted_residuals),
        "word": abstract_word,
    }


def route_word(word: tuple[Instruction, ...]) -> tuple[tuple[c655.Gate, ...], dict[str, object]]:
    routed: list[c655.Gate] = []
    maximum_distance = 0
    return_failures = operand_failures = nn_failures = 0
    delete_first_swap_failures = 0
    for instruction in word:
        if len(instruction.sites) == 1:
            macro = (c655.Gate(instruction.kind, instruction.sites, instruction.matrix),)
        else:
            left, right = instruction.sites
            path = c655.manhattan_path(left, right)
            maximum_distance = max(maximum_distance, len(path) - 1)
            macro = tuple(c655.route_two(instruction.kind, left, right, instruction.matrix))
            labels = list(path)
            for index in range(len(path) - 2):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            operand_failures += labels[-2:] != [left, right]
            for index in reversed(range(len(path) - 2)):
                labels[index], labels[index + 1] = labels[index + 1], labels[index]
            return_failures += labels != list(path)
            if len(path) > 2:
                deleted_labels = list(path)
                for index in range(1, len(path) - 2):
                    deleted_labels[index], deleted_labels[index + 1] = (
                        deleted_labels[index + 1],
                        deleted_labels[index],
                    )
                for index in reversed(range(len(path) - 2)):
                    deleted_labels[index], deleted_labels[index + 1] = (
                        deleted_labels[index + 1],
                        deleted_labels[index],
                    )
                delete_first_swap_failures += deleted_labels != list(path)
        nn_failures += sum(
            len(gate.sites) == 2 and c655.l1(*gate.sites) != 1 for gate in macro
        )
        routed.extend(macro)
    digest = sha256(
        "".join(
            gate.kind + repr(gate.sites) + c655.matrix_digest(gate.matrix)
            for gate in routed
        ).encode()
    ).hexdigest()
    touched = {site for gate in routed for site in gate.sites}
    return tuple(routed), {
        "routed_gate_count": len(routed),
        "routed_one_site": sum(len(gate.sites) == 1 for gate in routed),
        "routed_two_site": sum(len(gate.sites) == 2 for gate in routed),
        "touched_sites": len(touched),
        "maximum_route_distance": maximum_distance,
        "non_NN_failures": nn_failures,
        "operand_order_failures": operand_failures,
        "route_return_failures": return_failures,
        "delete_first_swap_detected_macros": delete_first_swap_failures,
        "word_sha256": digest,
        "touched_coordinates": tuple(sorted(touched)),
    }


def serpentine_clock(length: int, radius: int) -> tuple[Coord, ...]:
    rows = []
    for row_index, z in enumerate(range(-radius, radius + 1)):
        xs = list(range(-radius, radius + 1))
        if row_index & 1:
            xs.reverse()
        rows.extend((x, radius, z) for x in xs)
    if len(rows) < length:
        raise ValueError("controller face too small")
    return tuple(rows[:length])


def cycle655_controller(word: tuple[c655.Gate, ...], code_sites: int) -> dict[str, object]:
    length = len(word)
    radius = max(14, math.ceil((math.sqrt(length) - 1) / 2))
    clock = serpentine_clock(length, radius)
    relay = (0, radius - 2, radius)
    work0 = (0, radius - 1, radius)
    work1 = (1, radius - 1, radius)
    occupied = set(clock) | {relay, work0, work1}
    if occupied & set(site for gate in word for site in gate.sites):
        raise ValueError("controller overlaps data")
    token = [1] + [0] * (length - 1)
    selected = []
    for _ in range(length):
        selected.append(token.index(1))
        for index in reversed(range(length - 1)):
            token[index], token[index + 1] = token[index + 1], token[index]
    deleted = [1] + [0] * (length - 1)
    deleted_selected = []
    for _ in range(length):
        deleted_selected.append(deleted.index(1))
        for index in reversed(range(1, length - 1)):
            deleted[index], deleted[index + 1] = deleted[index + 1], deleted[index]
    toffoli_residual, fredkin_residual = c655.local_decomposition_residuals()
    bypass_opcode_controls = []
    for arity, digest in sorted({(len(gate.sites), c655.matrix_digest(gate.matrix)) for gate in word}):
        gate = next(
            row for row in word
            if len(row.sites) == arity and c655.matrix_digest(row.matrix) == digest
        )
        residual, leakage = c655.ideal_bypass(gate.matrix, arity)
        bypass_opcode_controls.append({
            "kind": gate.kind,
            "arity": arity,
            "matrix_sha256": digest,
            "action_residual": float(residual),
            "work_leakage": float(leakage),
        })
    cube = (2 * radius + 1) ** 3
    return {
        "program_length": length,
        "fixed_cube_radius": radius,
        "fixed_cube_M2": cube,
        "code_occupied_M2": code_sites,
        "clock_M2": len(clock),
        "relay_and_bypass_work_M2": 3,
        "remaining_cube_M2": cube - code_sites - len(clock) - 3,
        "selected_order_failures": int(selected != list(range(length))),
        "token_return_failures": int(token != [1] + [0] * (length - 1)),
        "delete_clock_shift_changes_word": deleted_selected != selected,
        "Toffoli_residual": toffoli_residual,
        "Fredkin_residual": fredkin_residual,
        "maximum_bypass_action_residual": max(
            row["action_residual"] for row in bypass_opcode_controls
        ),
        "maximum_bypass_work_leakage": max(
            row["work_leakage"] for row in bypass_opcode_controls
        ),
        "bypass_opcode_controls": tuple(bypass_opcode_controls),
        "microscopic_controller_macro_schedule": "supplied",
        "clock_coordinates_sha256": sha256(repr(clock).encode()).hexdigest(),
    }


cycle656_controller = c707trace.cycle656_controller


def covariance_controls(graph: PatchGraph, routed: tuple[c655.Gate, ...]) -> dict[str, object]:
    frames = c210.proper_cubic_frames()
    base_map, base_gauges = placement(graph, include_edge_gauge=True)
    base_sites = occupied_sites(base_map)
    base_gauge_sites = set(base_gauges.values())
    placement_failures = gauge_failures = word_nn_failures = 0
    canonical_set_equal = 0
    canonical_word_equal = 0
    base_signature = tuple((gate.kind, gate.sites, c655.matrix_digest(gate.matrix)) for gate in routed)
    for frame in frames:
        transformed_map, transformed_gauges = placement(
            graph, frame=frame, include_edge_gauge=True
        )
        expected = {
            tuple(int(value) for value in frame @ np.asarray(site)) for site in base_sites
        }
        expected_gauges = {
            tuple(int(value) for value in frame @ np.asarray(site))
            for site in base_gauge_sites
        }
        placement_failures += occupied_sites(transformed_map) != expected
        gauge_failures += set(transformed_gauges.values()) != expected_gauges
        canonical_set_equal += expected == base_sites
        transformed_word = tuple(
            (
                gate.kind,
                tuple(tuple(int(value) for value in frame @ np.asarray(site)) for site in gate.sites),
                c655.matrix_digest(gate.matrix),
            )
            for gate in routed
        )
        word_nn_failures += sum(
            len(sites) == 2 and c655.l1(*sites) != 1 for _, sites, _ in transformed_word
        )
        canonical_word_equal += transformed_word == base_signature
    frame_keys = {tuple(int(value) for value in frame.flat) for frame in frames}
    frame_closure_failures = direction_action_failures = 0
    placement_product_failures = gauge_product_failures = 0
    word_product_failures = matrix_associativity_failures = 0
    for left in frames:
        for right in frames:
            direct_frame = left @ right
            frame_closure_failures += (
                tuple(int(value) for value in direct_frame.flat) not in frame_keys
            )
            direction_action_failures += sum(
                tuple(int(value) for value in direct_frame @ np.asarray(direction))
                not in DIRECTIONS
                for direction in DIRECTIONS
            )
            direct_map, direct_gauges = placement(
                graph, frame=direct_frame, include_edge_gauge=True
            )
            expected_sites = {
                tuple(int(value) for value in left @ (right @ np.asarray(site)))
                for site in base_sites
            }
            expected_gauges = {
                tuple(int(value) for value in left @ (right @ np.asarray(site)))
                for site in base_gauge_sites
            }
            placement_product_failures += occupied_sites(direct_map) != expected_sites
            gauge_product_failures += set(direct_gauges.values()) != expected_gauges
            direct_word = tuple(
                (
                    gate.kind,
                    tuple(
                        tuple(int(value) for value in direct_frame @ np.asarray(site))
                        for site in gate.sites
                    ),
                    c655.matrix_digest(gate.matrix),
                )
                for gate in routed
            )
            sequential_word = tuple(
                (
                    gate.kind,
                    tuple(
                        tuple(int(value) for value in left @ (right @ np.asarray(site)))
                        for site in gate.sites
                    ),
                    c655.matrix_digest(gate.matrix),
                )
                for gate in routed
            )
            word_product_failures += direct_word != sequential_word
            for site in base_sites:
                sequential = left @ (right @ np.asarray(site))
                direct = (left @ right) @ np.asarray(site)
                matrix_associativity_failures += not np.array_equal(sequential, direct)
    translation_failures = translation_gauge_failures = 0
    translated_word_failures = translated_word_nn_failures = 0
    for shift in ((0, 0, 0), (1, -2, 3), (-7, 4, 1), (16, 16, 0)):
        moved, moved_gauges = placement(graph, origin=shift, include_edge_gauge=True)
        expected = {
            tuple(a + b for a, b in zip(site, shift)) for site in base_sites
        }
        expected_gauges = {
            tuple(a + b for a, b in zip(site, shift)) for site in base_gauge_sites
        }
        translation_failures += occupied_sites(moved) != expected
        translation_gauge_failures += set(moved_gauges.values()) != expected_gauges
        translated_word = tuple(
            (
                gate.kind,
                tuple(tuple(a + b for a, b in zip(site, shift)) for site in gate.sites),
                c655.matrix_digest(gate.matrix),
            )
            for gate in routed
        )
        expected_word = tuple(
            (
                kind,
                tuple(tuple(a + b for a, b in zip(site, shift)) for site in sites),
                digest,
            )
            for kind, sites, digest in base_signature
        )
        translated_word_failures += translated_word != expected_word
        translated_word_nn_failures += sum(
            len(sites) == 2 and c655.l1(*sites) != 1
            for _, sites, _ in translated_word
        )
    unit_translation_equal = sum(
        {tuple(a + b for a, b in zip(site, shift)) for site in base_sites} == base_sites
        for shift in ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    )
    return {
        "proper_cubic_frames": len(frames),
        "ordered_frame_products": len(frames) ** 2,
        "placement_family_failures": placement_failures,
        "optional_gauge_family_failures": gauge_failures,
        "rotated_word_NN_failures": word_nn_failures,
        "frame_closure_failures": frame_closure_failures,
        "direction_action_failures": direction_action_failures,
        "placement_product_diagram_failures": placement_product_failures,
        "optional_gauge_product_diagram_failures": gauge_product_failures,
        "routed_word_product_diagram_failures": word_product_failures,
        "matrix_associativity_site_failures": matrix_associativity_failures,
        "translated_placement_failures": translation_failures,
        "translated_optional_gauge_failures": translation_gauge_failures,
        "translated_word_diagram_failures": translated_word_failures,
        "translated_word_NN_failures": translated_word_nn_failures,
        "canonical_site_set_equal_frames": canonical_set_equal,
        "canonical_word_equal_frames": canonical_word_equal,
        "unit_translation_canonical_equalities": unit_translation_equal,
    }


def held_placement_controls() -> tuple[dict[str, object], ...]:
    rows = []
    for size, split in ((2, "direct"), (3, "held-no-refit"), (4, "held-no-refit")):
        graph = PatchGraph(square_cells(size))
        sites, gauges = placement(graph, include_edge_gauge=True)
        expected_streams = 2 * size * (size - 1)
        rows.append({
            "size": size,
            "split": split,
            "cells": size * size,
            "abstract_edges": len(graph.edges),
            "stream_edges": len(graph.stream_edges),
            "literal_physical_M2": len(occupied_sites(sites)),
            "prepared_plus_gauge_M2": len(occupied_sites(sites, gauges)),
            "collisions": sum(len(value) for value in sites.values()) - len(occupied_sites(sites)),
            "expected_stream_failures": int(len(graph.stream_edges) != expected_streams),
            "parameters_refit": 0,
        })
    return tuple(rows)
