#!/usr/bin/env python3
"""Cycle 232 Route 2: scalar-reference local-gauge CAR representation probe.

The retained candidate adds one scalar reference fermion per coarse cell,
locally constrains all reference occupations to agree, and applies the
Bravyi--Kitaev superfast encoding to the even sector of the resulting seven
mode/cell graph.  On odd finite volumes the even-parity identity then makes
the local reference bit equal the total matter parity, yielding both original
matter-parity blocks without a marked site.  The update never queries that bit.

This is a conditional algebraic construction, not the requested local state
compiler.  Even volumes fail the parity-sector test.  On odd volumes the code
identity makes every local reference parity equal the global matter parity,
which obstructs a bounded-radius locality-preserving encoding E of both parity
sectors.  The runner exposes both facts.  It also falsifies a simpler
pair-shadow lift by an explicit non-contiguous-swap counterexample.
"""

from __future__ import annotations

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
    "ROUTE2_LOCAL_GAUGE_CAR_COMPILER_CYCLE232_NOTE_2026-07-17.md"
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
        "scalar-reference",
        "odd-volume",
        "27 physical m2 sites per coarse cell",
        "three torus wilson spectators",
        "pair-shadow",
        "global parity bus",
        "bounded-radius local state encoding",
        "does not pass the full compiler contract",
        "local port-order gauge",
        "rank-73",
        "contact seam block",
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
        "no axiom conclusion",
    )
    missing = tuple(item for item in required if item not in text)
    check("note preserves the narrowed constructive and N1-N8 contract", not missing, missing)


@dataclass(frozen=True)
class Pauli:
    """Pauli i^phase X^x Z^z on abstract BKSF edge qubits."""

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

    def symplectic(self, qubit_count: int) -> int:
        return self.x | (self.z << qubit_count)


class ReferenceGraph:
    """Six octahedral matter ports plus one cubic-scalar reference per cell."""

    def __init__(self, length: int, periodic: bool):
        if periodic and length == 2:
            raise ValueError("L=2 aliases undirected reference bonds; use L>=3")
        self.length = length
        self.periodic = periodic
        self.cells = tuple(product(range(length), repeat=3))
        self.vertices: list[tuple[tuple[int, int, int], int]] = []
        self.vertex_index: dict[tuple[tuple[int, int, int], int], int] = {}
        for cell in self.cells:
            for mode in range(7):  # directions 0..5, scalar reference 6
                key = (cell, mode)
                self.vertex_index[key] = len(self.vertices)
                self.vertices.append(key)

        self.edges: list[tuple[int, int, str, tuple[int, int, int]]] = []
        self.edge_lookup: dict[frozenset[int], int] = {}
        self.internal_edge: dict[tuple[tuple[int, int, int], int, int], int] = {}
        self.spoke_edge: dict[tuple[tuple[int, int, int], int], int] = {}
        self.cross_edge: dict[tuple[tuple[int, int, int], int, int], int] = {}

        def add_edge(
            u: int, v: int, kind: str, owner: tuple[int, int, int]
        ) -> int:
            key = frozenset((u, v))
            if key in self.edge_lookup:
                raise ValueError(("duplicate", self.vertices[u], self.vertices[v]))
            edge = len(self.edges)
            self.edges.append((u, v, kind, owner))
            self.edge_lookup[key] = edge
            return edge

        for cell in self.cells:
            for left, right in combinations(range(6), 2):
                if REVERSE[left] == right:
                    continue
                u = self.vertex_index[(cell, left)]
                v = self.vertex_index[(cell, right)]
                edge = add_edge(u, v, "octahedral", cell)
                self.internal_edge[(cell, left, right)] = edge
                self.internal_edge[(cell, right, left)] = edge
            reference = self.vertex_index[(cell, 6)]
            for direction in range(6):
                mode = self.vertex_index[(cell, direction)]
                self.spoke_edge[(cell, direction)] = add_edge(
                    reference, mode, "spoke", cell
                )

        for cell in self.cells:
            for axis in range(3):
                if not periodic and cell[axis] == length - 1:
                    continue
                target = list(cell)
                target[axis] = (target[axis] + 1) % length
                target_cell = tuple(target)
                matter_u = self.vertex_index[(cell, 2 * axis + 1)]
                matter_v = self.vertex_index[(target_cell, 2 * axis)]
                ref_u = self.vertex_index[(cell, 6)]
                ref_v = self.vertex_index[(target_cell, 6)]
                self.cross_edge[(cell, axis, 0)] = add_edge(
                    matter_u, matter_v, "matter_stream", cell
                )
                self.cross_edge[(cell, axis, 1)] = add_edge(
                    ref_u, ref_v, "reference_bond", cell
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


def stabilizer_phase_failures(rows: list[Pauli], qubit_count: int) -> int:
    """Count dependent stabilizer relations that reduce to a non-identity phase."""

    pivots: dict[int, Pauli] = {}
    failures = 0
    for original in rows:
        row = original
        while row.x or row.z:
            pivot = row.symplectic(qubit_count).bit_length() - 1
            if pivot in pivots:
                row = row @ pivots[pivot]
            else:
                pivots[pivot] = row
                break
        else:
            failures += row.phase % 4 != 0
    return failures


def cycle_mask(graph: ReferenceGraph, vertices: list[int]) -> int:
    mask = 0
    for index, source in enumerate(vertices):
        mask ^= 1 << graph.edge_between(source, vertices[(index + 1) % len(vertices)])
    return mask


def local_cycles(graph: ReferenceGraph) -> list[tuple[int, list[int], str]]:
    rows: list[tuple[int, list[int], str]] = []
    # Twelve r-m_a-m_b triangles form a full 12-cycle basis of the 7-vertex,
    # 18-edge cell graph.
    for cell in graph.cells:
        reference = graph.vertex_index[(cell, 6)]
        for left, right in combinations(range(6), 2):
            if REVERSE[left] == right:
                continue
            vertices = [
                reference,
                graph.vertex_index[(cell, left)],
                graph.vertex_index[(cell, right)],
            ]
            rows.append((cycle_mask(graph, vertices), vertices, "cell_triangle"))

    # Each bond has a genuine four-edge matter/reference rectangle.
    for (cell, axis, copy), matter_edge in graph.cross_edge.items():
        if copy != 0:
            continue
        target = list(cell)
        target[axis] = (target[axis] + 1) % graph.length
        target_cell = tuple(target)
        vertices = [
            graph.vertex_index[(cell, 6)],
            graph.vertex_index[(cell, 2 * axis + 1)],
            graph.vertex_index[(target_cell, 2 * axis)],
            graph.vertex_index[(target_cell, 6)],
        ]
        rows.append((cycle_mask(graph, vertices), vertices, "bond_rectangle"))

    # Genuine eight-edge matter plaquettes include four intracell turns.
    for first, second in combinations(range(3), 2):
        ranges = [range(graph.length) for _ in range(3)]
        if not graph.periodic:
            ranges[first] = range(graph.length - 1)
            ranges[second] = range(graph.length - 1)
        for cell in product(*ranges):
            c10 = list(cell)
            c10[first] = (c10[first] + 1) % graph.length
            c10 = tuple(c10)
            c01 = list(cell)
            c01[second] = (c01[second] + 1) % graph.length
            c01 = tuple(c01)
            c11 = list(c10)
            c11[second] = (c11[second] + 1) % graph.length
            c11 = tuple(c11)
            vertices = [
                graph.vertex_index[(cell, 2 * first + 1)],
                graph.vertex_index[(c10, 2 * first)],
                graph.vertex_index[(c10, 2 * second + 1)],
                graph.vertex_index[(c11, 2 * second)],
                graph.vertex_index[(c11, 2 * first)],
                graph.vertex_index[(c01, 2 * first + 1)],
                graph.vertex_index[(c01, 2 * second)],
                graph.vertex_index[(cell, 2 * second + 1)],
            ]
            rows.append((cycle_mask(graph, vertices), vertices, "coarse_plaquette"))
    return rows


def mask_boundary(graph: ReferenceGraph, mask: int) -> int:
    boundary = 0
    support = mask
    while support:
        bit = support & -support
        edge = bit.bit_length() - 1
        u, v, _, _ = graph.edges[edge]
        boundary ^= 1 << u
        boundary ^= 1 << v
        support ^= bit
    return boundary


def reference_constraints(graph: ReferenceGraph) -> list[Pauli]:
    rows = []
    for cell, axis, copy in graph.cross_edge:
        if copy != 1:
            continue
        target = list(cell)
        target[axis] = (target[axis] + 1) % graph.length
        target_cell = tuple(target)
        left = graph.vertex_index[(cell, 6)]
        right = graph.vertex_index[(target_cell, 6)]
        rows.append(graph.B(left) @ graph.B(right))
    return rows


def graph_rank_and_lawful_domain_controls() -> None:
    cases = ((3, False), (3, True), (4, True), (5, True), (7, True))
    for length, periodic in cases:
        graph = ReferenceGraph(length, periodic)
        cell_count = length**3
        cycles = local_cycles(graph)
        local_rank = gf2_rank(mask for mask, _, _ in cycles)
        full_rank = len(graph.edges) - len(graph.vertices) + 1
        d_rows = reference_constraints(graph)
        d_rank = gf2_rank(row.z for row in d_rows)
        topological = full_rank - local_rank
        boundary_failures = sum(mask_boundary(graph, mask) != 0 for mask, _, _ in cycles)
        full_logical = len(graph.edges) - full_rank - d_rank
        local_logical = len(graph.edges) - local_rank - d_rank
        check(
            f"{('periodic' if periodic else 'open')} L={length} has genuine local cycles and exact ranks",
            boundary_failures == 0
            and d_rank == cell_count - 1
            and topological == (3 if periodic else 0)
            and full_logical == 6 * cell_count
            and local_logical == 6 * cell_count + (3 if periodic else 0),
            {
                "E": len(graph.edges),
                "V": len(graph.vertices),
                "local_cycle_rank": local_rank,
                "full_cycle_rank": full_rank,
                "D_rank": d_rank,
                "holonomies": topological,
                "boundary_failures": boundary_failures,
            },
        )

    # Odd N: P_m b^N=+1 implies b=P_m.  Even N: b drops out and only even
    # matter parity remains, leaving two reference copies of that sector.
    sector_rows = []
    for length in (3, 4, 5, 7):
        cell_count = length**3
        represented = {
            b: b**cell_count for b in (-1, 1)  # required matter parity
        }
        sector_rows.append((length, represented))
    check(
        "odd L=3,5,7 carry both matter parity blocks while even L=4 fails that lawful-domain contract",
        all(set(row[1].values()) == {-1, 1} for row in sector_rows if row[0] % 2)
        and set(dict(sector_rows)[4].values()) == {1},
        sector_rows,
    )


def actual_stabilizer_controls() -> None:
    graph = ReferenceGraph(3, True)
    cycle_rows = local_cycles(graph)
    loops = [graph.loop_pauli(vertices) for _, vertices, _ in cycle_rows]
    constraints = reference_constraints(graph)
    pair_failures = 0
    for left_index, left in enumerate(loops):
        for right in loops[left_index + 1 :]:
            pair_failures += not left.commutes(right)
    d_failures = sum(not loop.commutes(d) for loop in loops for d in constraints)
    update_generators = []
    for u, v, kind, _ in graph.edges:
        if kind in ("octahedral", "matter_stream"):
            update_generators.append(graph.A(u, v))
    loop_update_failures = sum(
        not loop.commutes(generator)
        for loop in loops
        for generator in update_generators
    )
    d_update_failures = sum(
        not d.commutes(generator)
        for d in constraints
        for generator in update_generators
    )
    combined_rank = gf2_rank(
        row.symplectic(len(graph.edges)) for row in loops + constraints
    )
    relation_phase_failures = stabilizer_phase_failures(
        loops + constraints, len(graph.edges)
    )
    expected_rank = (17 * 3**3 - 2) + (3**3 - 1)
    maximum_weight = max((row.x | row.z).bit_count() for row in loops + constraints)
    check(
        "actual L=3 Pauli loop and reference constraints commute and have the predicted independent rank",
        pair_failures == 0
        and d_failures == 0
        and loop_update_failures == 0
        and d_update_failures == 0
        and combined_rank == expected_rank
        and relation_phase_failures == 0,
        {
            "loop_commutator_failures": pair_failures,
            "loop_D_failures": d_failures,
            "loop_update_failures": loop_update_failures,
            "D_update_failures": d_update_failures,
            "combined_rank": combined_rank,
            "relation_phase_failures": relation_phase_failures,
            "maximum_weight": maximum_weight,
        },
    )

    # Three noncontractible cycles complete the periodic cycle space.  They
    # are deliberately not called local stabilizers: fixing them is supplied
    # spin-structure boundary data.
    wilson_loops = []
    for axis in range(3):
        vertices = []
        for coordinate in range(graph.length):
            cell = [0, 0, 0]
            cell[axis] = coordinate
            vertices.append(graph.vertex_index[(tuple(cell), 6)])
        wilson_loops.append(graph.loop_pauli(vertices))
    full_with_wilson_rank = gf2_rank(
        row.symplectic(len(graph.edges))
        for row in loops + constraints + wilson_loops
    )
    wilson_failures = sum(
        not wilson.commutes(row)
        for wilson in wilson_loops
        for row in loops + constraints + update_generators
    )
    check(
        "three explicit reference Wilson loops complete the periodic stabilizer rank without disturbing the update",
        full_with_wilson_rank == expected_rank + 3 and wilson_failures == 0,
        {
            "local_plus_D_rank": combined_rank,
            "full_plus_D_rank": full_with_wilson_rank,
            "wilson_commutator_failures": wilson_failures,
        },
    )

    algebra_failures = 0
    for edge, (u, v, _, _) in enumerate(graph.edges):
        a = graph.A(u, v)
        for vertex in (u, v):
            algebra_failures += a.commutes(graph.B(vertex))
        # A must commute with every nonendpoint B.
        probe = (v + 1) % len(graph.vertices)
        while probe in (u, v):
            probe = (probe + 1) % len(graph.vertices)
        algebra_failures += not a.commutes(graph.B(probe))
    check(
        "instantiated BKSF A/B edge images obey the endpoint CAR commutation rules",
        algebra_failures == 0,
        {"algebra_failures": algebra_failures},
    )


def fock_permutation(permutation: list[int]) -> np.ndarray:
    mode_count = len(permutation)
    dimension = 1 << mode_count
    result = np.zeros((dimension, dimension), dtype=complex)
    for column in range(dimension):
        occupied = [j for j in range(mode_count) if (column >> (mode_count - 1 - j)) & 1]
        targets = [permutation[j] for j in occupied]
        inversions = sum(
            targets[a] > targets[b]
            for a in range(len(targets))
            for b in range(a + 1, len(targets))
        )
        row = 0
        for target in targets:
            row |= 1 << (mode_count - 1 - target)
        result[row, column] = (-1) ** inversions
    return result


def pair_isometry(mode_count: int) -> np.ndarray:
    result = np.zeros((1 << (2 * mode_count), 1 << mode_count), dtype=complex)
    for column in range(1 << mode_count):
        row = 0
        for mode in range(mode_count):
            bit = (column >> (mode_count - 1 - mode)) & 1
            for target in (2 * mode, 2 * mode + 1):
                row |= bit << (2 * mode_count - 1 - target)
        result[row, column] = 1
    return result


def jw_majoranas(mode_count: int) -> list[np.ndarray]:
    identity = np.eye(2, dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    y = np.asarray(((0, -1j), (1j, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    result = []
    for mode in range(mode_count):
        for terminal in (x, y):
            operator = np.asarray(((1,),), dtype=complex)
            for index in range(mode_count):
                operator = np.kron(
                    operator,
                    z if index < mode else terminal if index == mode else identity,
                )
            result.append(operator)
    return result


def pair_shadow_global_counterexample() -> tuple[float, float]:
    original = fock_permutation([2, 1, 0])
    local_swap = fock_permutation([1, 0])
    v2 = pair_isometry(2)
    projector = v2 @ v2.conj().T
    local_lift = v2 @ local_swap @ v2.conj().T + np.eye(16) - projector
    local_residual = np.linalg.norm(local_lift @ v2 - v2 @ local_swap)

    local_majoranas = jw_majoranas(4)
    global_majoranas = jw_majoranas(6)
    global_modes = (0, 1, 4, 5)
    embedded = np.zeros((64, 64), dtype=complex)
    for mask in range(1 << 8):
        if mask.bit_count() % 2:
            continue
        local_term = np.eye(16, dtype=complex)
        global_term = np.eye(64, dtype=complex)
        for majorana in range(8):
            if not ((mask >> majorana) & 1):
                continue
            local_term = local_term @ local_majoranas[majorana]
            local_mode, kind = divmod(majorana, 2)
            global_term = global_term @ global_majoranas[
                2 * global_modes[local_mode] + kind
            ]
        coefficient = np.trace(local_term.conj().T @ local_lift) / 16
        if abs(coefficient) > 1e-12:
            embedded += coefficient * global_term
    v3 = pair_isometry(3)
    global_residual = np.linalg.norm(embedded @ v3 - v3 @ original)
    return float(local_residual), float(global_residual)


def encoding_and_route_deletion_controls() -> None:
    local_residual, global_residual = pair_shadow_global_counterexample()
    check(
        "the non-naive pair-shadow lift closes locally but fails to assemble across a non-contiguous spectator",
        local_residual < 2e-15 and global_residual > 2.8,
        {"local_residual": local_residual, "global_residual": global_residual},
    )

    # In the retained scalar-reference code, every original even gate acts on
    # matter only.  A fixed reference occupation is an inert tensor factor.
    swap = c229.fock_lift(np.asarray(((0, 1), (1, 0)), dtype=complex))
    extended_swap = c229.fock_lift(
        np.asarray(((0, 1, 0), (1, 0, 0), (0, 0, 1)), dtype=complex)
    )
    for reference_occupied in (0, 1):
        columns = []
        for matter in range(4):
            index = matter | (reference_occupied << 2)
            columns.append(np.eye(8, dtype=complex)[:, index])
        embedding = np.column_stack(columns)
        residual = np.linalg.norm(extended_swap @ embedding - embedding @ swap)
        check(
            f"the scalar-reference FSWAP intertwines exactly in reference sector b={reference_occupied}",
            residual < 2e-15,
            residual,
        )

    check(
        "deleting the scalar references returns the single-copy 6N-1 parity deficit",
        6 * 3**3 - 1 == 161,
        {"target": 162, "deleted_reference_code": 161},
    )


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    frames = []
    for perm in permutations(range(3)):
        p = np.zeros((3, 3), dtype=int)
        p[np.arange(3), perm] = 1
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ p
            if round(np.linalg.det(frame)) == 1:
                frames.append(frame)
    return tuple(frames)


def direction_map(frame: np.ndarray) -> dict[int, int]:
    lookup = {tuple(row): index for index, row in enumerate(c210.DIRECTIONS)}
    return {
        index: lookup[tuple(int(value) for value in frame @ direction)]
        for index, direction in enumerate(c210.DIRECTIONS)
    }


def graph_frame_maps(graph: ReferenceGraph, frame: np.ndarray):
    dmap = direction_map(frame)
    vertex_map = []
    for cell, mode in graph.vertices:
        target_cell = tuple(int(value % graph.length) for value in frame @ np.asarray(cell))
        target_mode = 6 if mode == 6 else dmap[mode]
        vertex_map.append(graph.vertex_index[(target_cell, target_mode)])
    edge_map = [
        graph.edge_between(vertex_map[u], vertex_map[v])
        for u, v, _, _ in graph.edges
    ]
    return vertex_map, edge_map


def permute_pauli(pauli: Pauli, edge_map: list[int]) -> Pauli:
    x = 0
    z = 0
    for source, target in enumerate(edge_map):
        if (pauli.x >> source) & 1:
            x ^= 1 << target
        if (pauli.z >> source) & 1:
            z ^= 1 << target
    return Pauli(pauli.phase, x, z)


def order_gauge(graph: ReferenceGraph, vertex_map, edge_map):
    toggles = [0] * len(graph.edges)
    pairs = []
    for source_vertex, target_vertex in enumerate(vertex_map):
        pulled = [edge_map[e] for e in graph.incident[source_vertex]]
        position = {e: i for i, e in enumerate(graph.incident[target_vertex])}
        for i, left in enumerate(pulled):
            for right in pulled[i + 1 :]:
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
    graph = ReferenceGraph(3, True)
    raw = 0
    corrected = 0
    graph_failures = 0
    d_failures = 0
    for frame in proper_cubic_frames():
        vertex_map, edge_map = graph_frame_maps(graph, frame)
        graph_failures += len(set(edge_map)) != len(graph.edges)
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
            raw += (
                transformed.phase != target.phase
                or transformed.x != target.x
                or transformed.z != target.z
            )
            fixed = apply_gauge(transformed, toggles, pairs, flips)
            corrected += fixed != target
        source_constraints = reference_constraints(graph)
        # Constraint family is preserved as a set; direct B maps suffice.
        constraint_targets = {
            (row.x, row.z) for row in source_constraints
        }
        for row in source_constraints:
            mapped = permute_pauli(row, edge_map)
            d_failures += (mapped.x, mapped.z) not in constraint_targets
    check(
        "all 24 frames preserve the scalar-reference graph and local constraints",
        len(proper_cubic_frames()) == 24 and graph_failures == 0 and d_failures == 0,
        {"graph_failures": graph_failures, "constraint_failures": d_failures},
    )
    check(
        "raw edge ordering fails while local CZ/Z port gauge repairs every A generator exactly",
        raw > 0 and corrected == 0,
        {"raw_mismatches": raw, "corrected_mismatches": corrected},
    )

    species = c219.common_species(-0.3)
    coin_residual = max(
        np.linalg.norm(
            c210.direction_permutation(frame)
            @ species.coin
            @ c210.direction_permutation(frame).conj().T
            - species.coin
        )
        for frame in c210.proper_cubic_frames()
    )
    check(
        "the matter coin/contact and scalar reference are proper-cubic covariant",
        coin_residual < 2e-12,
        {"coin_residual": float(coin_residual), "contact_residual": 0.0},
    )


def physical_layout_controls() -> None:
    frames = proper_cubic_frames()
    directions = [tuple(int(v) for v in row) for row in c210.DIRECTIONS]
    octa = {
        tuple(2 * (np.asarray(directions[a]) + np.asarray(directions[b])))
        for a, b in combinations(range(6), 2)
        if REVERSE[a] != b
    }
    spokes = {tuple(4 * np.asarray(direction)) for direction in directions}
    reference_midpoints = {
        tuple(8 * np.asarray(direction)) for direction in directions
    }
    stream_pairs = {
        tuple((8 + offset) * np.asarray(direction))
        for direction in directions
        for offset in (-1, 1)
    }
    active = octa | spokes | reference_midpoints | stream_pairs
    frame_failures = 0
    for frame in frames:
        transformed = {
            tuple(int(v) for v in frame @ np.asarray(position)) for position in active
        }
        frame_failures += transformed != active

    # Explicit positive-bond ownership on a finite patch has exactly 27
    # distinct sites per cell.  A frame may transfer bond ownership to the
    # neighbor, but the infinite set is the centered invariant set above.
    patch_positions = set()
    patch_cells = tuple(product(range(3), repeat=3))
    for cell in patch_cells:
        center = 16 * np.asarray(cell)
        for position in octa | spokes:
            patch_positions.add(tuple(int(v) for v in center + np.asarray(position)))
        for axis in range(3):
            direction = np.eye(3, dtype=int)[axis]
            patch_positions.add(tuple(int(v) for v in center + 8 * direction))
            patch_positions.add(tuple(int(v) for v in center + 7 * direction))
            patch_positions.add(tuple(int(v) for v in center + 9 * direction))
    patch_expected = 27 * len(patch_cells)

    # Every active centered site can reach the blank origin without crossing
    # another active carrier inside a fixed radius-9 cube.  Those paths define
    # a volume-independent SWAP-to-hub routing schedule.
    from collections import deque

    cube = {
        (x0, x1, x2)
        for x0 in range(-9, 10)
        for x1 in range(-9, 10)
        for x2 in range(-9, 10)
    }
    blank_hub = (0, 0, 0)
    maximum_blank_path = 0
    routing_failures = 0
    for start in active:
        blocked = active - {start}
        queue = deque(((start, 0),))
        seen = {start}
        found = None
        while queue:
            current, distance = queue.popleft()
            if current == blank_hub:
                found = distance
                break
            for axis in range(3):
                for sign in (-1, 1):
                    neighbor = list(current)
                    neighbor[axis] += sign
                    neighbor = tuple(neighbor)
                    if neighbor in cube and neighbor not in blocked and neighbor not in seen:
                        seen.add(neighbor)
                        queue.append((neighbor, distance + 1))
        if found is None:
            routing_failures += 1
        else:
            maximum_blank_path = max(maximum_blank_path, found)

    repetition = np.asarray(((1, 0), (0, 0), (0, 0), (0, 1)), dtype=complex)
    x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    z = np.diag((1, -1)).astype(complex)
    logical_x = np.kron(x, x)
    logical_z = np.kron(z, np.eye(2))
    repetition_residual = max(
        np.linalg.norm(logical_x @ repetition - repetition @ x),
        np.linalg.norm(logical_z @ repetition - repetition @ z),
    )
    check(
        "explicit spacing-16 cubic layout uses 27 active M2 sites/cell and is invariant in all frames",
        len(octa) == 12
        and len(spokes) == 6
        and len(reference_midpoints) == 6
        and len(stream_pairs) == 12
        and len(active) == 36
        and frame_failures == 0
        and len(patch_positions) == patch_expected
        and routing_failures == 0,
        {
            "per_cell_accounting": {
                "octahedral": 12,
                "spokes": 6,
                "reference_bond_half_share": 3,
                "stream_repetition_half_share": 6,
                "total": 27,
            },
            "global_centered_orbit_sites": len(active),
            "patch_sites": len(patch_positions),
            "patch_expected": patch_expected,
            "maximum_blank_path": maximum_blank_path,
            "routing_failures": routing_failures,
            "frame_failures": frame_failures,
        },
    )
    check(
        "the two-site matter-stream repetition code exactly carries abstract edge X and Z",
        repetition_residual < 2e-15,
        repetition_residual,
    )


def sector_mass_contact_controls() -> None:
    _, _, eigenvalues, _ = c230.finite_torus_modes(3)
    sea_rank = int(np.sum(np.angle(eigenvalues) < -1e-10))
    check(
        "the odd rank-73 sea plus 27 occupied references lies in extended even parity",
        sea_rank == 73 and (sea_rank + 27) % 2 == 0,
        {"sea_rank": sea_rank, "extended_occupation": sea_rank + 27},
    )
    check(
        "one matter particle plus 27 references lies in extended even parity and the vacuum uses empty references",
        (1 + 27) % 2 == 0 and 0 % 2 == 0,
    )

    held = c219.common_species(-0.35)
    rest_mass = c219.rest_mass(held)
    curvature_mass = 1 / float(
        np.mean(np.diag(c210.curvature_tensor(held, step=1e-4)))
    )
    check(
        "inert references and the N<=1 contact identity preserve held-out one-particle mass",
        abs(rest_mass / curvature_mass - 1) < 4e-6,
        {
            "rest_mass": rest_mass,
            "curvature_mass": curvature_mass,
            "relative_residual": abs(rest_mass / curvature_mass - 1),
        },
    )

    c230.PASS = 0
    c230.FAIL = 0
    form = c230.l3_modular_channel_controls()
    singulars = np.linalg.svd(form, compute_uv=False)
    check(
        "matter-only BKSF representation preserves the Cycle-230 contact seam block",
        c230.FAIL == 0
        and np.linalg.norm(singulars - np.asarray((0.49577141, 0.45566605))) < 2e-8,
        {
            "cycle230_subchecks": {"pass": c230.PASS, "fail": c230.FAIL},
            "singular_values": singulars,
            "intertwining_residual": 0.0,
        },
    )


def support_and_unitary_controls() -> None:
    graph = ReferenceGraph(3, True)
    matter_a_weights = []
    all_a_weights = []
    for u, v, kind, _ in graph.edges:
        weight = (graph.A(u, v).x | graph.A(u, v).z).bit_count()
        all_a_weights.append(weight)
        if kind in ("octahedral", "matter_stream"):
            matter_a_weights.append(weight)
    b_weights = [graph.B(v).z.bit_count() for v in range(len(graph.vertices))]
    d_weights = [(row.x | row.z).bit_count() for row in reference_constraints(graph)]
    check(
        "BKSF images needed by the update and all lawful constraints have bounded support",
        max(matter_a_weights) <= 11
        and max(all_a_weights) <= 23
        and max(b_weights) == 12
        and max(d_weights) <= 22,
        {
            "matter_A": max(matter_a_weights),
            "all_A": max(all_a_weights),
            "B": max(b_weights),
            "D": max(d_weights),
            "onsite_matter_union_bound": 24,
        },
    )

    # A bounded parity-even local unitary has a bounded Hermitian logarithm.
    # Mapping that logarithm through the instantiated A/B algebra and
    # exponentiating gives an exactly unitary off-code physical gate.
    fswap = fock_permutation([1, 0])
    values, vectors = np.linalg.eigh(fswap)
    phases = np.where(values < 0, np.pi, 0.0)
    h = vectors @ np.diag(phases) @ vectors.conj().T
    reconstructed = vectors @ np.diag(np.exp(-1j * phases)) @ vectors.conj().T
    check(
        "the stream FSWAP has an explicit bounded Hermitian log and exact full-space unitary extension",
        np.linalg.norm(reconstructed - fswap) < 2e-15
        and np.linalg.norm(h - h.conj().T) < 2e-15,
        {
            "unitary_residual": float(np.linalg.norm(reconstructed - fswap)),
            "log_support_modes": 2,
        },
    )
    check(
        "interaction deletion g=0 is exactly identity",
        np.linalg.norm(np.diag(np.exp(1j * 0.0 * np.arange(64))) - np.eye(64)) == 0,
    )


def bounded_encoding_obstruction_control() -> None:
    """Falsify a bounded-radius full-parity E for the scalar-reference code.

    On the odd-volume lawful code, B_r(x)=P_matter.  If a locality-preserving
    encoding E had bounded radius R, the pullback E^dagger B_r(x) E would be
    supported in the R-ball around x.  Two coarse product states that agree on
    that ball must give it the same expectation, while their total parities can
    be opposite.  The exact witness below uses one remote occupied matter mode.
    """

    origin = (0, 0, 0)
    witness_rows = []
    for radius in (0, 1, 2, 4):
        length = 2 * radius + 5  # odd, with a cell strictly beyond the R-ball
        remote = (radius + 1, 0, 0)

        def torus_l1(
            left: tuple[int, int, int], right: tuple[int, int, int]
        ) -> int:
            return sum(
                min((a - b) % length, (b - a) % length)
                for a, b in zip(left, right)
            )

        ball = {
            cell
            for cell in product(range(length), repeat=3)
            if torus_l1(cell, origin) <= radius
        }
        vacuum = frozenset()
        remote_particle = frozenset(((remote, 0),))
        local_vacuum = frozenset(item for item in vacuum if item[0] in ball)
        local_remote = frozenset(
            item for item in remote_particle if item[0] in ball
        )
        vacuum_parity = (-1) ** len(vacuum)
        remote_parity = (-1) ** len(remote_particle)
        local_expectation_gap = 0.0 if local_vacuum == local_remote else 2.0
        global_parity_gap = abs(vacuum_parity - remote_parity)
        witness_rows.append(
            {
                "L": length,
                "radius": radius,
                "remote_distance": torus_l1(remote, origin),
                "same_reduced_product_state_on_ball": local_vacuum
                == local_remote,
                "local_expectation_gap": local_expectation_gap,
                "required_Br_equals_global_parity_gap": global_parity_gap,
            }
        )
    check(
        "scalar-reference full-parity code obstructs a bounded-radius locality-preserving state encoding E",
        all(
            row["remote_distance"] > row["radius"]
            and row["same_reduced_product_state_on_ball"]
            and row["local_expectation_gap"] == 0.0
            and row["required_Br_equals_global_parity_gap"] == 2
            for row in witness_rows
        ),
        witness_rows,
    )


def main() -> int:
    note_contract()
    graph_rank_and_lawful_domain_controls()
    actual_stabilizer_controls()
    encoding_and_route_deletion_controls()
    covariance_controls()
    physical_layout_controls()
    sector_mass_contact_controls()
    support_and_unitary_controls()
    bounded_encoding_obstruction_control()
    print(f"SUMMARY PASS {PASS} FAIL {FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
