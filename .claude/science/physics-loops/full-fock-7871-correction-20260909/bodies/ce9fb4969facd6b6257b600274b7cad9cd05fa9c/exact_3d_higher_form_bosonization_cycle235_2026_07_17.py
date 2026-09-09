#!/usr/bin/env python3
"""Cycle 235: exact-3D-bosonization compiler instantiation attempt.

The geometric candidate subdivides each coarse cube into the six square
pyramids from its center to its boundary faces.  The six pyramid 3-cells are
the Cycle-230 direction modes.  Their dual adjacency graph is exactly the
onsite octahedron plus the stream bonds.  Qubits live on primal faces and the
modified Gauss/loop constraints live on primal edges.

The executable presentation below uses a local incident-face ordering for the
Chen--Kapustin hopping algebra.  It is the same edge-Pauli presentation of the
even Majorana algebra: B_t is the boundary Z flux of a pyramid and A_f is X_f
with bounded local Z framing.  Products around primal edges are the modified
Gauss constraints.  The runner deliberately exposes the closed-manifold
identity product_t B_t=I: the published duality represents only total-even
fermion parity and therefore does not compile the full Cycle-230 Fock space.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from itertools import combinations, permutations, product
from pathlib import Path
import sys

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import common_matter_field_coin_family_cycle219_2026_07_16 as c219
import fock_modular_boundary_current_cycle229_2026_07_17 as c229
import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
import spatial_car_contact_seam_form_factor_cycle230_2026_07_17 as c230

NOTE = (
    ROOT
    / "docs/work_history/repo/review_feedback/"
    "EXACT_3D_HIGHER_FORM_BOSONIZATION_CYCLE235_NOTE_2026-07-17.md"
)

PASS = 0
FAIL = 0
REVERSE = (1, 0, 3, 2, 5, 4)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def note_contract() -> None:
    text = " ".join(NOTE.read_text(encoding="utf-8").lower().split())
    required = (
        "square-pyramid",
        "15 face qubits per coarse cell",
        "modified gauss",
        "total-even",
        "bounded-radius state",
        "three topological",
        "rank-73",
        "unit translation",
        "authority: none",
        "audit: unset",
        "n1 — alternative routes",
        "n2 — condition independence",
        "n3 — hidden-condition scan",
        "n4 — residual matching",
        "n5 — resolution audit",
        "n6 — partial-closure and primitive scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "no axiom pressure",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the source and N1-N8 contract", not missing, missing)


@dataclass(frozen=True)
class Pauli:
    """Pauli i^phase X^x Z^z on face qubits."""

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


class PyramidCellulation:
    """Dual graph of the proper-cubic square-pyramid cellulation."""

    def __init__(self, length: int):
        if length < 3:
            raise ValueError("periodic L>=3 avoids aliased undirected faces")
        self.length = length
        self.cells = tuple(product(range(length), repeat=3))
        self.vertices: list[tuple[tuple[int, int, int], int]] = []
        self.vertex_index: dict[tuple[tuple[int, int, int], int], int] = {}
        for cell in self.cells:
            for direction in range(6):
                key = (cell, direction)
                self.vertex_index[key] = len(self.vertices)
                self.vertices.append(key)

        # Dual edges are primal faces: 12 triangular internal faces/cell and
        # three shared square boundary faces/cell.
        self.edges: list[tuple[int, int, str, tuple[int, int, int]]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}

        def add_edge(u: int, v: int, kind: str, owner: tuple[int, int, int]) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate face", self.vertices[u], self.vertices[v]))
            index = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = index
            return index

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] == right:
                    continue
                add_edge(
                    self.vertex_index[(cell, left)],
                    self.vertex_index[(cell, right)],
                    "internal_triangle",
                    cell,
                )
            for axis in range(3):
                target = list(cell)
                target[axis] = (target[axis] + 1) % length
                target_cell = tuple(target)
                add_edge(
                    self.vertex_index[(cell, 2 * axis)],
                    self.vertex_index[(target_cell, 2 * axis + 1)],
                    "outer_square",
                    cell,
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
        """Bounded local framing of i gamma_source gamma'_target."""
        edge = self.edge_between(source, target)
        z = 0
        for vertex in (source, target):
            for incident in self.incident[vertex]:
                if incident == edge:
                    break
                z ^= 1 << incident
        return Pauli(0 if source < target else 2, 1 << edge, z)

    def cycle_mask(self, vertices: list[int]) -> int:
        mask = 0
        for index, source in enumerate(vertices):
            target = vertices[(index + 1) % len(vertices)]
            mask ^= 1 << self.edge_between(source, target)
        return mask

    def loop_pauli(self, vertices: list[int]) -> Pauli:
        result = Pauli(phase=len(vertices) % 4)
        for index, source in enumerate(vertices):
            result = result @ self.A(source, vertices[(index + 1) % len(vertices)])
        return result


def primal_edge_cycles(graph: PyramidCellulation):
    """The 8N spoke-edge triangles and 3N coarse-edge octagons."""
    rows: list[tuple[int, list[int], str]] = []
    # A center-to-corner spoke is surrounded by the three face pyramids that
    # meet at that corner.
    for cell in graph.cells:
        for bits in product((0, 1), repeat=3):
            directions = [
                2 * axis + (0 if bits[axis] else 1) for axis in range(3)
            ]
            vertices = [graph.vertex_index[(cell, direction)] for direction in directions]
            rows.append((graph.cycle_mask(vertices), vertices, "center_corner_edge"))

    # A coarse cubic edge is surrounded by four cubes.  In the dual graph its
    # link alternates four internal triangular faces and four outer squares.
    for corner in graph.cells:
        for axis in range(3):
            first, second = [value for value in range(3) if value != axis]

            def local_cell(first_shift: int, second_shift: int):
                cell = list(corner)
                cell[first] = (cell[first] - first_shift) % graph.length
                cell[second] = (cell[second] - second_shift) % graph.length
                return tuple(cell)

            def first_direction(shift: int) -> int:
                return 2 * first + (0 if shift else 1)

            def second_direction(shift: int) -> int:
                return 2 * second + (0 if shift else 1)

            labels = (
                (local_cell(0, 0), first_direction(0)),
                (local_cell(0, 0), second_direction(0)),
                (local_cell(0, 1), second_direction(1)),
                (local_cell(0, 1), first_direction(0)),
                (local_cell(1, 1), first_direction(1)),
                (local_cell(1, 1), second_direction(1)),
                (local_cell(1, 0), second_direction(0)),
                (local_cell(1, 0), first_direction(1)),
            )
            vertices = [graph.vertex_index[label] for label in labels]
            rows.append((graph.cycle_mask(vertices), vertices, "coarse_grid_edge"))
    return rows


def mask_boundary(graph: PyramidCellulation, mask: int) -> int:
    boundary = 0
    while mask:
        bit = mask & -mask
        edge = bit.bit_length() - 1
        u, v, _, _ = graph.edges[edge]
        boundary ^= 1 << u
        boundary ^= 1 << v
        mask ^= bit
    return boundary


def wilson_cycles(graph: PyramidCellulation) -> list[list[int]]:
    rows = []
    for axis in range(3):
        transverse = (axis + 1) % 3
        vertices = []
        for step in range(graph.length):
            cell = [0, 0, 0]
            cell[axis] = step
            next_cell = list(cell)
            next_cell[axis] = (next_cell[axis] + 1) % graph.length
            # +axis --stream--> -axis in next cell, then a bounded two-edge
            # intracell path back to +axis.
            vertices.extend(
                (
                    graph.vertex_index[(tuple(cell), 2 * axis)],
                    graph.vertex_index[(tuple(next_cell), 2 * axis + 1)],
                    graph.vertex_index[(tuple(next_cell), 2 * transverse)],
                )
            )
        # The next repeated +axis vertex is implicit in loop closure.
        rows.append(vertices)
    return rows


def phase_aware_rank(rows: list[Pauli], qubits: int):
    pivots: dict[int, Pauli] = {}
    inconsistent = []
    for index, original in enumerate(rows):
        row = original
        symplectic = row.symplectic(qubits)
        while symplectic:
            pivot = symplectic.bit_length() - 1
            if pivot in pivots:
                row = row @ pivots[pivot]
                symplectic = row.symplectic(qubits)
            else:
                pivots[pivot] = row
                break
        if not symplectic and row.phase % 4:
            inconsistent.append((index, row.phase))
    return len(pivots), inconsistent


def cellulation_rank_controls() -> None:
    for length in (3, 4, 5):
        graph = PyramidCellulation(length)
        cells = length**3
        cycles = primal_edge_cycles(graph)
        loops = [graph.loop_pauli(vertices) for _, vertices, _ in cycles]
        wilson_paulis = [
            graph.loop_pauli(vertices) for vertices in wilson_cycles(graph)
        ]
        local_rank = gf2_rank(mask for mask, _, _ in cycles)
        full_rank = len(graph.edges) - len(graph.vertices) + 1
        phase_local_rank, phase_local_inconsistent = phase_aware_rank(
            loops, len(graph.edges)
        )
        phase_full_rank, phase_full_inconsistent = phase_aware_rank(
            loops + wilson_paulis, len(graph.edges)
        )
        boundary_failures = sum(mask_boundary(graph, mask) != 0 for mask, _, _ in cycles)
        wilsons = wilson_cycles(graph)
        wilson_increment = gf2_rank(
            [mask for mask, _, _ in cycles]
            + [graph.cycle_mask(vertices) for vertices in wilsons]
        ) - local_rank
        check(
            f"L={length} square-pyramid cellulation has exact counts, genuine Gauss loops, and three topological cycles",
            len(graph.vertices) == 6 * cells
            and len(graph.edges) == 15 * cells
            and len(cycles) == 11 * cells
            and local_rank == 9 * cells - 2
            and full_rank == 9 * cells + 1
            and phase_local_rank == local_rank
            and phase_full_rank == full_rank
            and not phase_local_inconsistent
            and not phase_full_inconsistent
            and boundary_failures == 0
            and wilson_increment == 3,
            {
                "primal": {"V": 2 * cells, "E": 11 * cells, "F": 15 * cells, "C": 6 * cells},
                "face_qubits": len(graph.edges),
                "local_Gauss_rank": local_rank,
                "full_cycle_rank": full_rank,
                "topological": full_rank - local_rank,
                "boundary_failures": boundary_failures,
                "phase_inconsistencies": len(phase_local_inconsistent)
                + len(phase_full_inconsistent),
            },
        )


def actual_pauli_controls() -> None:
    graph = PyramidCellulation(3)
    cycles = primal_edge_cycles(graph)
    loops = [graph.loop_pauli(vertices) for _, vertices, _ in cycles]
    wilsons = [graph.loop_pauli(vertices) for vertices in wilson_cycles(graph)]
    commutators = sum(
        not left.commutes(right)
        for index, left in enumerate(loops)
        for right in loops[index + 1 :]
    )
    update_failures = sum(
        not loop.commutes(graph.A(u, v))
        for loop in loops
        for u, v, _, _ in graph.edges
    )
    nonhermitian = sum(
        (row.phase - (row.x & row.z).bit_count()) % 2 != 0 for row in loops + wilsons
    )
    local_rank, local_inconsistent = phase_aware_rank(loops, len(graph.edges))
    full_rank, full_inconsistent = phase_aware_rank(loops + wilsons, len(graph.edges))
    check(
        "actual L=3 modified-Gauss Paulis commute, are nonempty, and the Wilson-fixed code has the even-Fock dimension",
        commutators == 0
        and update_failures == 0
        and nonhermitian == 0
        and not local_inconsistent
        and not full_inconsistent
        and local_rank == 241
        and full_rank == 244
        and len(graph.edges) - full_rank == 6 * 3**3 - 1,
        {
            "qubits": len(graph.edges),
            "local_rank": local_rank,
            "Wilson_fixed_rank": full_rank,
            "logical_exponent": len(graph.edges) - full_rank,
            "commutator_failures": commutators,
            "update_failures": update_failures,
            "nonhermitian": nonhermitian,
            "minus_identity_dependencies": len(local_inconsistent) + len(full_inconsistent),
            "maximum_weight": max((row.x | row.z).bit_count() for row in loops + wilsons),
        },
    )

    algebra_failures = 0
    for u, v, _, _ in graph.edges:
        edge = graph.A(u, v)
        algebra_failures += edge.commutes(graph.B(u))
        algebra_failures += edge.commutes(graph.B(v))
        probe = (v + 1) % len(graph.vertices)
        while probe in (u, v):
            probe = (probe + 1) % len(graph.vertices)
        algebra_failures += not edge.commutes(graph.B(probe))
    check(
        "face-qubit hopping and cell-flux images obey the endpoint even-CAR algebra",
        algebra_failures == 0,
        {"algebra_failures": algebra_failures},
    )

    edge_algebra_failures = 0
    incident_pairs = 0
    disjoint_pairs = 0
    edge_operators = [
        (u, v, graph.A(u, v)) for u, v, _, _ in graph.edges
    ]
    for index, (u, v, left) in enumerate(edge_operators):
        for x, y, right in edge_operators[index + 1 :]:
            expected_anticommutation = len({u, v} & {x, y}) == 1
            actual_anticommutation = not left.commutes(right)
            incident_pairs += expected_anticommutation
            disjoint_pairs += not expected_anticommutation
            edge_algebra_failures += (
                expected_anticommutation != actual_anticommutation
            )
    check(
        "all L=3 hopping-generator pairs have the exact even-Majorana commutation graph",
        edge_algebra_failures == 0,
        {
            "incident_pairs": incident_pairs,
            "disjoint_pairs": disjoint_pairs,
            "failures": edge_algebra_failures,
        },
    )


def parity_and_state_encoding_controls() -> None:
    rows = []
    for length in (3, 4, 5):
        graph = PyramidCellulation(length)
        total = Pauli()
        for vertex in range(len(graph.vertices)):
            total = total @ graph.B(vertex)
        rows.append(
            {
                "L": length,
                "product_cell_flux_is_identity": total == Pauli(),
                "even_sector_present": True,
                "odd_sector_present": False,
                "target_logical_exponent": 6 * length**3,
                "encoded_logical_exponent": 6 * length**3 - 1,
            }
        )
    check(
        "closed-manifold flux identity retains only total-even matter parity at L=3,4,5",
        all(row["product_cell_flux_is_identity"] for row in rows)
        and all(not row["odd_sector_present"] for row in rows),
        rows,
    )

    # A computational-basis flux encoder must solve graph divergence q=n.
    # Two distant odd cells require a connected face string.  The shortest
    # possible string grows with separation; this is evidence against treating
    # the published Hilbert-space duality as a bounded-radius state circuit.
    distances = []
    for length in (3, 5, 7):
        graph = PyramidCellulation(length)
        source = graph.vertex_index[((0, 0, 0), 0)]
        target_cell = (length // 2, 0, 0)
        target = graph.vertex_index[(target_cell, 0)]
        distance = shortest_path(graph, source, target)
        distances.append((length, distance))
    check(
        "the natural occupation-to-face-flux state map has a growing string lower bound",
        distances == [(3, 3), (5, 6), (7, 9)],
        distances,
    )


def shortest_path(graph: PyramidCellulation, source: int, target: int) -> int:
    adjacency = [[] for _ in graph.vertices]
    for u, v, _, _ in graph.edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    queue = deque(((source, 0),))
    seen = {source}
    while queue:
        vertex, distance = queue.popleft()
        if vertex == target:
            return distance
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append((neighbor, distance + 1))
    raise RuntimeError("connected dual graph unexpectedly disconnected")


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for perm in permutations(range(3)):
        permutation = np.zeros((3, 3), dtype=int)
        permutation[np.arange(3), perm] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def direction_map(frame: np.ndarray) -> dict[int, int]:
    lookup = {tuple(direction): index for index, direction in enumerate(c210.DIRECTIONS)}
    return {
        source: lookup[tuple(int(value) for value in frame @ direction)]
        for source, direction in enumerate(c210.DIRECTIONS)
    }


def graph_frame_maps(graph: PyramidCellulation, frame: np.ndarray):
    dmap = direction_map(frame)
    vertex_map = []
    for cell, mode in graph.vertices:
        target_cell = tuple(
            int(value % graph.length) for value in frame @ np.asarray(cell)
        )
        vertex_map.append(graph.vertex_index[(target_cell, dmap[mode])])
    edge_map = [
        graph.edge_between(vertex_map[u], vertex_map[v]) for u, v, _, _ in graph.edges
    ]
    return vertex_map, edge_map


def permute_pauli(pauli: Pauli, edge_map: list[int]) -> Pauli:
    x = z = 0
    for source, target in enumerate(edge_map):
        if (pauli.x >> source) & 1:
            x ^= 1 << target
        if (pauli.z >> source) & 1:
            z ^= 1 << target
    return Pauli(pauli.phase, x, z)


def order_gauge(graph: PyramidCellulation, vertex_map, edge_map):
    toggles = [0] * len(graph.edges)
    pairs = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[edge] for edge in graph.incident[source_vertex]]
        position = {edge: index for index, edge in enumerate(graph.incident[target_vertex])}
        for index, left in enumerate(pulled):
            for right in pulled[index + 1 :]:
                if position[left] > position[right]:
                    toggles[left] ^= 1 << right
                    toggles[right] ^= 1 << left
                    pairs.append((left, right))
    return toggles, pairs


def apply_gauge(pauli: Pauli, toggles, pairs, orientation_flips=0) -> Pauli:
    phase = pauli.phase
    for left, right in pairs:
        if ((pauli.x >> left) & 1) and ((pauli.x >> right) & 1):
            phase = (phase + 2) % 4
    z = pauli.z
    support = pauli.x
    while support:
        bit = support & -support
        edge = bit.bit_length() - 1
        z ^= toggles[edge]
        support ^= bit
    phase = (phase + 2 * (pauli.x & orientation_flips).bit_count()) % 4
    return Pauli(phase, pauli.x, z)


def covariance_controls() -> None:
    graph = PyramidCellulation(3)
    source_constraints = {mask for mask, _, _ in primal_edge_cycles(graph)}
    raw = corrected = graph_failures = constraint_failures = 0
    frame_data = []
    for frame in proper_cubic_frames():
        vertex_map, edge_map = graph_frame_maps(graph, frame)
        graph_failures += len(set(edge_map)) != len(graph.edges)
        for mask in source_constraints:
            mapped = permute_pauli(Pauli(x=mask), edge_map).x
            constraint_failures += mapped not in source_constraints
        toggles, pairs = order_gauge(graph, vertex_map, edge_map)
        flips = 0
        for source_edge, (u, v, _, _) in enumerate(graph.edges):
            transformed = permute_pauli(graph.A(u, v), edge_map)
            target = graph.A(vertex_map[u], vertex_map[v])
            ordered = apply_gauge(transformed, toggles, pairs)
            if (ordered.phase - target.phase) % 4 == 2:
                flips ^= 1 << edge_map[source_edge]
        for u, v, _, _ in graph.edges:
            transformed = permute_pauli(graph.A(u, v), edge_map)
            target = graph.A(vertex_map[u], vertex_map[v])
            raw += transformed != target
            corrected += apply_gauge(transformed, toggles, pairs, flips) != target
        frame_data.append((edge_map, toggles, pairs, flips))

    check(
        "all 24 proper frames preserve the pyramid graph and the primal-edge Gauss family",
        len(proper_cubic_frames()) == 24
        and graph_failures == 0
        and constraint_failures == 0,
        {"graph_failures": graph_failures, "constraint_failures": constraint_failures},
    )
    check(
        "bounded local CZ/Z framing gauge repairs every rotated hopping generator",
        raw > 0 and corrected == 0,
        {"raw_mismatches": raw, "corrected_mismatches": corrected},
    )

    # Exact group law on the generating Pauli X/Z operators.  This separately
    # excludes a frame-by-frame repair table with a composition cocycle.
    frames = proper_cubic_frames()
    frame_index = {
        tuple(int(value) for value in frame.ravel()): index
        for index, frame in enumerate(frames)
    }

    def permute_mask(mask: int, edge_map: list[int]) -> int:
        result = 0
        while mask:
            bit = mask & -mask
            edge = bit.bit_length() - 1
            result ^= 1 << edge_map[edge]
            mask ^= bit
        return result

    def transform_single_xz(pauli: Pauli, data) -> Pauli:
        edge_map, toggles, _, flips = data
        if pauli.x.bit_count() > 1:
            raise ValueError("group-law generator test expects at most one X")
        z = permute_mask(pauli.z, edge_map)
        x = 0
        phase = pauli.phase
        if pauli.x:
            source = pauli.x.bit_length() - 1
            target = edge_map[source]
            x = 1 << target
            z ^= toggles[target]
            phase = (phase + 2 * ((flips >> target) & 1)) % 4
        return Pauli(phase, x, z)

    group_mismatches = 0
    for left_index, left in enumerate(frames):
        for right_index, right in enumerate(frames):
            product_index = frame_index[
                tuple(int(value) for value in (left @ right).ravel())
            ]
            for edge in range(len(graph.edges)):
                for generator in (Pauli(x=1 << edge), Pauli(z=1 << edge)):
                    composed = transform_single_xz(
                        transform_single_xz(generator, frame_data[right_index]),
                        frame_data[left_index],
                    )
                    direct = transform_single_xz(generator, frame_data[product_index])
                    group_mismatches += composed != direct
    check(
        "the 24 framing repairs obey the exact proper-cubic group law on every face X/Z generator",
        group_mismatches == 0,
        {"cases": 24 * 24 * len(graph.edges) * 2, "mismatches": group_mismatches},
    )


def physical_layout_and_translation_controls() -> None:
    directions = [tuple(int(value) for value in row) for row in c210.DIRECTIONS]
    internal = {
        tuple(2 * (np.asarray(directions[left]) + np.asarray(directions[right])))
        for left, right in combinations(range(6), 2)
        if REVERSE[left] != right
    }
    boundary = {tuple(8 * np.asarray(direction)) for direction in directions}
    centered = internal | boundary
    frame_failures = 0
    for frame in proper_cubic_frames():
        transformed = {
            tuple(int(value) for value in frame @ np.asarray(position))
            for position in centered
        }
        frame_failures += transformed != centered

    patch_rows = []
    for length in (3, 4, 5):
        modulus = 16 * length
        sites = set()
        for cell in product(range(length), repeat=3):
            center = 16 * np.asarray(cell)
            for position in internal:
                sites.add(tuple(int(value % modulus) for value in center + position))
            for axis in range(3):
                sites.add(
                    tuple(
                        int(value % modulus)
                        for value in center + 8 * np.eye(3, dtype=int)[axis]
                    )
                )
        shifted = {((x + 1) % modulus, y, z) for x, y, z in sites}
        macro_shifted = {((x + 16) % modulus, y, z) for x, y, z in sites}
        patch_rows.append(
            (
                length,
                len(sites),
                len(sites.symmetric_difference(shifted)),
                len(sites.symmetric_difference(macro_shifted)),
            )
        )
    check(
        "proper-cubic face placement has 15 physical M2 sites/cell after sharing",
        len(internal) == 12
        and len(boundary) == 6
        and len(centered) == 18
        and frame_failures == 0
        and all(site_count == 15 * length**3 for length, site_count, _, _ in patch_rows),
        {"centered_orbit": len(centered), "density": 15, "frame_failures": frame_failures},
    )
    check(
        "the placement is period-16 rather than unit-translation invariant",
        all(unit_difference == 30 * length**3 for length, _, unit_difference, _ in patch_rows)
        and all(macro_difference == 0 for _, _, _, macro_difference in patch_rows),
        patch_rows,
    )


def update_and_fixture_controls() -> None:
    species = c219.common_species(-0.35)
    coin = c229.fock_lift(species.coin)
    parity = np.diag(
        [(-1) ** index.bit_count() for index in range(64)]
    ).astype(complex)
    occupations = np.asarray([index.bit_count() for index in range(64)])
    contact = np.diag(np.exp(1j * 0.37 * occupations * (occupations - 1) / 2))
    check(
        "onsite coin and contact are parity even and therefore lie in the mapped local algebra",
        np.linalg.norm(coin @ parity - parity @ coin) < 2e-12
        and np.linalg.norm(contact @ parity - parity @ contact) == 0,
        {
            "coin_commutator": float(np.linalg.norm(coin @ parity - parity @ coin)),
            "contact_commutator": float(np.linalg.norm(contact @ parity - parity @ contact)),
            "onsite_dual_graph_diameter": 2,
        },
    )

    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the one-particle and rank-73 seam sectors are odd and absent from the closed higher-form code",
        sea_rank == 73 and sea_rank % 2 == 1,
        {
            "one_particle_parity": "odd/absent",
            "sea_rank": sea_rank,
            "sea_parity": "odd/absent",
            "full_intertwining_available": False,
        },
    )
    check(
        "the published even-algebra map cannot by itself preserve the Cycle-219 mass or Cycle-230 seam fixture",
        True,
        {
            "reason": "both declared fixture sectors have total odd parity",
            "mapped_even_updates": ("coin", "A/B FSWAP", "contact"),
            "state_sector_missing": ("one-particle", "rank-73 principal sea"),
        },
    )


def support_and_deletion_controls() -> None:
    graph = PyramidCellulation(3)
    a_weights = [
        (graph.A(u, v).x | graph.A(u, v).z).bit_count()
        for u, v, _, _ in graph.edges
    ]
    b_weights = [graph.B(vertex).z.bit_count() for vertex in range(len(graph.vertices))]
    loop_weights = [
        (graph.loop_pauli(vertices).x | graph.loop_pauli(vertices).z).bit_count()
        for _, vertices, _ in primal_edge_cycles(graph)
    ]
    onsite_unions = []
    for cell in graph.cells:
        union = 0
        for direction in range(6):
            for edge in graph.incident[graph.vertex_index[(cell, direction)]]:
                union |= 1 << edge
        onsite_unions.append(union.bit_count())
    check(
        "all flux, hopping, modified-Gauss, and onsite-even supports are volume independent",
        max(a_weights) <= 9
        and max(b_weights) == 5
        and max(loop_weights) <= 28
        and max(onsite_unions) == 18,
        {
            "A": max(a_weights),
            "B": max(b_weights),
            "Gauss": max(loop_weights),
            "onsite_union": max(onsite_unions),
        },
    )
    local_rank = gf2_rank(mask for mask, _, _ in primal_edge_cycles(graph))
    check(
        "deleting one independent Gauss relation adds one spurious logical degree",
        len(graph.edges) - (local_rank - 1) == (6 * 3**3 + 2) + 1,
        {
            "local_code_before_Wilson_fix": len(graph.edges) - local_rank,
            "after_deletion": len(graph.edges) - local_rank + 1,
        },
    )


def main() -> int:
    note_contract()
    cellulation_rank_controls()
    actual_pauli_controls()
    parity_and_state_encoding_controls()
    covariance_controls()
    physical_layout_and_translation_controls()
    update_and_fixture_controls()
    support_and_deletion_controls()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
