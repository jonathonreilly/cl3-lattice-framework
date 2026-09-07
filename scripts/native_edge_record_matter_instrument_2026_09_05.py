#!/usr/bin/env python3
"""Finite-matrix primary checks for a native BKSF edge-Record instrument.

The runner is deliberately finite.  It checks graph and binary-Pauli algebra,
constructs the physical cube code and a direct even-CAR reference independently,
and follows selected no-reset Record histories.  It does not derive the event
clock, the Born/Lueders rule, a covariant placement, or a renewal mechanism.
"""

from __future__ import annotations

import os

for _thread_var in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_var] = "1"

import hashlib
import itertools
import math
import resource
import sys
import time
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

import numpy as np
import scipy.linalg as la
import scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply


AUDIT_TIMEOUT_SEC = 180
TOL = 2.0e-10
PROB_TOL = 2.0e-13
SEED = 20260905


class CheckBook:
    """Collect family-level checks and emit a bounded final report."""

    def __init__(self) -> None:
        self.passes = 0
        self.failures: list[str] = []

    def check(self, family: str, condition: bool, detail: str) -> None:
        if condition:
            self.passes += 1
            print(f"PASS {family}: {detail}")
        else:
            self.failures.append(f"{family}: {detail}")
            print(f"FAIL {family}: {detail}")

    def finish(self) -> None:
        print(f"TOTAL: PASS={self.passes} FAIL={len(self.failures)}")
        if self.failures:
            raise SystemExit(1)


@dataclass(frozen=True)
class Pauli:
    """Coefficient times X^x Z^z, with X factors written before Z factors."""

    x: int
    z: int
    coeff: complex = 1.0 + 0.0j

    def __matmul__(self, other: "Pauli") -> "Pauli":
        sign = -1.0 if ((self.z & other.x).bit_count() & 1) else 1.0
        return Pauli(
            self.x ^ other.x,
            self.z ^ other.z,
            self.coeff * other.coeff * sign,
        )

    def scaled(self, value: complex) -> "Pauli":
        return Pauli(self.x, self.z, self.coeff * value)

    def dagger(self) -> "Pauli":
        sign = -1.0 if ((self.x & self.z).bit_count() & 1) else 1.0
        return Pauli(self.x, self.z, self.coeff.conjugate() * sign)

    def symplectic(self, other: "Pauli") -> int:
        return (
            (self.x & other.z).bit_count()
            + (self.z & other.x).bit_count()
        ) & 1


Operator = dict[tuple[int, int], complex]


def operator(*terms: Pauli, tol: float = 1.0e-14) -> Operator:
    out: Operator = {}
    for term in terms:
        key = (term.x, term.z)
        out[key] = out.get(key, 0.0j) + term.coeff
    return {key: value for key, value in out.items() if abs(value) > tol}


def op_add(*ops: Operator) -> Operator:
    out: Operator = {}
    for op in ops:
        for key, value in op.items():
            out[key] = out.get(key, 0.0j) + value
    return {key: value for key, value in out.items() if abs(value) > 1.0e-13}


def op_scale(op: Operator, value: complex) -> Operator:
    return {
        key: value * coefficient
        for key, coefficient in op.items()
        if abs(value * coefficient) > 1.0e-13
    }


def op_mul(left: Operator, right: Operator) -> Operator:
    terms: list[Pauli] = []
    for (x1, z1), c1 in left.items():
        for (x2, z2), c2 in right.items():
            terms.append(Pauli(x1, z1, c1) @ Pauli(x2, z2, c2))
    return operator(*terms)


def op_dagger(op: Operator) -> Operator:
    return operator(
        *(Pauli(x, z, coefficient).dagger() for (x, z), coefficient in op.items())
    )


def op_residual(left: Operator, right: Operator) -> float:
    keys = set(left) | set(right)
    return max((abs(left.get(key, 0.0j) - right.get(key, 0.0j)) for key in keys), default=0.0)


def op_commutator(left: Operator, right: Operator) -> Operator:
    return op_add(op_mul(left, right), op_scale(op_mul(right, left), -1.0))


def parity_signs(indices: np.ndarray, zmask: int) -> np.ndarray:
    return np.fromiter(
        (-1.0 if ((int(index) & zmask).bit_count() & 1) else 1.0 for index in indices),
        dtype=np.float64,
        count=len(indices),
    )


def apply_pauli(word: Pauli, values: np.ndarray, dimension: int) -> np.ndarray:
    indices = np.arange(dimension, dtype=np.int64)
    rows = indices ^ word.x
    phases = word.coeff * parity_signs(indices, word.z)
    out = np.empty_like(values, dtype=np.complex128)
    if values.ndim == 1:
        out[rows] = phases * values
    else:
        out[rows, :] = phases[:, None] * values
    return out


def sparse_pauli(word: Pauli, qubits: int) -> sp.csr_matrix:
    dimension = 1 << qubits
    columns = np.arange(dimension, dtype=np.int64)
    rows = columns ^ word.x
    data = word.coeff * parity_signs(columns, word.z)
    return sp.csr_matrix((data, (rows, columns)), shape=(dimension, dimension))


def sparse_operator(op: Operator, qubits: int) -> sp.csr_matrix:
    result = sp.csr_matrix((1 << qubits, 1 << qubits), dtype=np.complex128)
    for (xmask, zmask), coefficient in op.items():
        result = result + sparse_pauli(Pauli(xmask, zmask, coefficient), qubits)
    result.eliminate_zeros()
    return result


def gf2_rank(rows: Iterable[int]) -> int:
    pivots: dict[int, int] = {}
    for raw in rows:
        row = int(raw)
        while row:
            pivot = row.bit_length() - 1
            if pivot in pivots:
                row ^= pivots[pivot]
            else:
                pivots[pivot] = row
                break
    return len(pivots)


@dataclass(frozen=True)
class Graph:
    """Finite connected loopless simple graph with ordered neighbors."""

    vertices: int
    edges: tuple[tuple[int, int], ...]
    coefficients: tuple[float, ...]
    neighbor_orders: tuple[tuple[int, ...], ...]
    coordinates: tuple[tuple[int, int, int], ...] | None = None
    hopping_bound: float = 1.0

    def __post_init__(self) -> None:
        if self.vertices < 2 or self.hopping_bound <= 0.0:
            raise ValueError("graph size and hopping bound must be positive")
        if len(self.edges) != len(self.coefficients):
            raise ValueError("one coefficient is required per edge")
        normalized: set[tuple[int, int]] = set()
        adjacency = [set() for _ in range(self.vertices)]
        for edge, coefficient in zip(self.edges, self.coefficients):
            if len(edge) != 2:
                raise ValueError("edges have two endpoints")
            u, v = edge
            if not (0 <= u < v < self.vertices):
                raise ValueError("edges must be normalized, in range, and loopless")
            if edge in normalized:
                raise ValueError("parallel edges are outside this runner")
            if not math.isfinite(coefficient) or abs(coefficient) > self.hopping_bound:
                raise ValueError("bond coefficient exceeds the supplied bound")
            normalized.add(edge)
            adjacency[u].add(v)
            adjacency[v].add(u)
        if len(self.neighbor_orders) != self.vertices:
            raise ValueError("one neighbor order is required per vertex")
        for vertex, order in enumerate(self.neighbor_orders):
            if tuple(sorted(order)) != tuple(sorted(adjacency[vertex])):
                raise ValueError("neighbor order must list each neighbor exactly once")
        if len(components(self.vertices, self.edges, (1 << len(self.edges)) - 1)) != 1:
            raise ValueError("graph must be connected")
        if self.coordinates is not None and len(self.coordinates) != self.vertices:
            raise ValueError("coordinate count must match vertex count")

    @property
    def edge_index(self) -> dict[tuple[int, int], int]:
        return {edge: index for index, edge in enumerate(self.edges)}

    @property
    def full_mask(self) -> int:
        return (1 << len(self.edges)) - 1

    def incident_mask(self, vertex: int) -> int:
        mask = 0
        for index, (u, v) in enumerate(self.edges):
            if vertex in (u, v):
                mask |= 1 << index
        return mask

    def edge_number(self, u: int, v: int) -> int:
        return self.edge_index[tuple(sorted((u, v)))]


def components(
    vertices: int,
    edges: Sequence[tuple[int, int]],
    live_mask: int,
) -> list[tuple[int, ...]]:
    adjacency = [[] for _ in range(vertices)]
    for edge_index, (u, v) in enumerate(edges):
        if (live_mask >> edge_index) & 1:
            adjacency[u].append(v)
            adjacency[v].append(u)
    seen: set[int] = set()
    result: list[tuple[int, ...]] = []
    for start in range(vertices):
        if start in seen:
            continue
        queue = [start]
        seen.add(start)
        part: list[int] = []
        while queue:
            vertex = queue.pop()
            part.append(vertex)
            for neighbor in adjacency[vertex]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        result.append(tuple(sorted(part)))
    return sorted(result)


def path_edges(
    graph: Graph,
    live_mask: int,
    start: int,
    target: int,
) -> tuple[list[int], list[int]] | None:
    queue: deque[int] = deque([start])
    parent: dict[int, tuple[int, int] | None] = {start: None}
    while queue:
        vertex = queue.popleft()
        if vertex == target:
            break
        for edge_index, (u, v) in enumerate(graph.edges):
            if not ((live_mask >> edge_index) & 1):
                continue
            if vertex == u:
                neighbor = v
            elif vertex == v:
                neighbor = u
            else:
                continue
            if neighbor not in parent:
                parent[neighbor] = (vertex, edge_index)
                queue.append(neighbor)
    if target not in parent:
        return None
    vertices = [target]
    used_edges: list[int] = []
    cursor = target
    while cursor != start:
        predecessor, edge_index = parent[cursor]  # type: ignore[misc]
        used_edges.append(edge_index)
        vertices.append(predecessor)
        cursor = predecessor
    vertices.reverse()
    used_edges.reverse()
    return vertices, used_edges


def fundamental_cycles(graph: Graph, live_mask: int) -> list[tuple[list[int], int]]:
    tree_mask = 0
    visited: set[int] = set()
    for root in range(graph.vertices):
        if root in visited:
            continue
        visited.add(root)
        queue: deque[int] = deque([root])
        while queue:
            vertex = queue.popleft()
            for edge_index, (u, v) in enumerate(graph.edges):
                if not ((live_mask >> edge_index) & 1):
                    continue
                if vertex == u:
                    neighbor = v
                elif vertex == v:
                    neighbor = u
                else:
                    continue
                if neighbor not in visited:
                    visited.add(neighbor)
                    tree_mask |= 1 << edge_index
                    queue.append(neighbor)
    cycles: list[tuple[list[int], int]] = []
    for edge_index, (u, v) in enumerate(graph.edges):
        if not ((live_mask >> edge_index) & 1) or ((tree_mask >> edge_index) & 1):
            continue
        found = path_edges(graph, tree_mask, u, v)
        if found is None:
            raise AssertionError("forest path missing for non-tree edge")
        vertices, used_edges = found
        cycle_mask = 1 << edge_index
        for used in used_edges:
            cycle_mask |= 1 << used
        cycles.append((vertices, cycle_mask))
    return cycles


def cycle_through_edge(graph: Graph, live_mask: int, edge_index: int) -> list[int] | None:
    u, v = graph.edges[edge_index]
    found = path_edges(graph, live_mask & ~(1 << edge_index), u, v)
    if found is None:
        return None
    vertices, _ = found
    return vertices


def boundary_mask(graph: Graph, vertex_subset: Iterable[int]) -> int:
    subset = set(vertex_subset)
    mask = 0
    for edge_index, (u, v) in enumerate(graph.edges):
        if (u in subset) != (v in subset):
            mask |= 1 << edge_index
    return mask


def make_open_cube() -> Graph:
    coordinates = tuple(
        (x, y, z)
        for x in range(2)
        for y in range(2)
        for z in range(2)
    )
    index = {coordinate: number for number, coordinate in enumerate(coordinates)}
    edge_data: list[tuple[tuple[int, int], float]] = []
    for coordinate in coordinates:
        x, y, z = coordinate
        for axis in range(3):
            if coordinate[axis] != 0:
                continue
            neighbor = list(coordinate)
            neighbor[axis] = 1
            u, v = index[coordinate], index[tuple(neighbor)]
            eta = (1.0, (-1.0) ** x, (-1.0) ** (x + y))[axis]
            edge_data.append((tuple(sorted((u, v))), -eta))
    edge_data.sort()
    edges = tuple(item[0] for item in edge_data)
    coefficients = tuple(item[1] for item in edge_data)
    adjacency = [list() for _ in coordinates]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    return Graph(
        len(coordinates),
        edges,
        coefficients,
        tuple(tuple(sorted(neighbors)) for neighbors in adjacency),
        coordinates,
        1.0,
    )


def graph_from_edges(vertices: int, raw_edges: Sequence[tuple[int, int]]) -> Graph:
    edges = tuple(sorted(tuple(sorted(edge)) for edge in raw_edges))
    adjacency = [list() for _ in range(vertices)]
    for u, v in edges:
        adjacency[u].append(v)
        adjacency[v].append(u)
    return Graph(
        vertices,
        edges,
        tuple(1.0 for _ in edges),
        tuple(tuple(sorted(neighbors)) for neighbors in adjacency),
    )


class BKSF:
    """Binary-Pauli realization for one edge qubit per graph edge."""

    def __init__(self, graph: Graph) -> None:
        self.graph = graph
        self.qubits = len(graph.edges)
        self.identity = Pauli(0, 0, 1.0)
        self.B = tuple(Pauli(0, graph.incident_mask(v), 1.0) for v in range(graph.vertices))
        self.A_forward = tuple(self.A(u, v) for u, v in graph.edges)
        self.T = tuple(self._make_T(index) for index in range(self.qubits))
        self.h = tuple(
            op_scale(term, coefficient)
            for term, coefficient in zip(self.T, graph.coefficients)
        )

    def A(self, i: int, j: int) -> Pauli:
        edge_index = self.graph.edge_number(i, j)
        zmask = 0
        for neighbor in self.graph.neighbor_orders[i]:
            if neighbor == j:
                break
            zmask |= 1 << self.graph.edge_number(i, neighbor)
        for neighbor in self.graph.neighbor_orders[j]:
            if neighbor == i:
                break
            zmask |= 1 << self.graph.edge_number(j, neighbor)
        orientation = 1.0 if i < j else -1.0
        return Pauli(1 << edge_index, zmask, orientation)

    def _make_T(self, edge_index: int) -> Operator:
        i, j = self.graph.edges[edge_index]
        a_word = self.A(i, j)
        left = (a_word @ self.B[i]).scaled(0.5j)
        right = (a_word @ self.B[j]).scaled(-0.5j)
        return operator(left, right)

    def cycle(self, vertices: Sequence[int]) -> Pauli:
        if len(vertices) < 3:
            raise ValueError("a cycle needs at least three vertices")
        word = Pauli(0, 0, (1j) ** len(vertices))
        for index, vertex in enumerate(vertices):
            word = word @ self.A(vertex, vertices[(index + 1) % len(vertices)])
        return word


def source_identity() -> str:
    return hashlib.sha256(Path(__file__).read_bytes()).hexdigest()


def peak_rss_mib() -> float:
    raw = float(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
    if sys.platform == "darwin":
        return raw / (1024.0 * 1024.0)
    return raw / 1024.0


class EvenCAR:
    """Direct Jordan-Wigner matrices on the even-global-parity sector."""

    def __init__(self, vertices: int, edges: Sequence[tuple[int, int]]) -> None:
        self.vertices = vertices
        self.edges = tuple(edges)
        self.basis = tuple(
            bits for bits in range(1 << vertices) if not (bits.bit_count() & 1)
        )
        self.index = {bits: position for position, bits in enumerate(self.basis)}
        self.dimension = len(self.basis)
        self.B = tuple(self._make_B(vertex) for vertex in range(vertices))
        self.A_forward = tuple(self._make_A(i, j) for i, j in self.edges)
        self.T = tuple(self._make_T(edge_index) for edge_index in range(len(edges)))
        self.N = np.diag([float(bits.bit_count()) for bits in self.basis]).astype(
            np.complex128
        )

    @staticmethod
    def _gamma_even_action(bits: int, vertex: int) -> tuple[int, complex]:
        lower = bits & ((1 << vertex) - 1)
        sign = -1.0 if (lower.bit_count() & 1) else 1.0
        return bits ^ (1 << vertex), complex(sign)

    @staticmethod
    def _ladder_action(bits: int, vertex: int, create: bool) -> tuple[int, complex] | None:
        occupied = bool((bits >> vertex) & 1)
        if occupied == create:
            return None
        lower = bits & ((1 << vertex) - 1)
        sign = -1.0 if (lower.bit_count() & 1) else 1.0
        return bits ^ (1 << vertex), complex(sign)

    def _make_B(self, vertex: int) -> np.ndarray:
        diagonal = [
            -1.0 if ((bits >> vertex) & 1) else 1.0 for bits in self.basis
        ]
        return np.diag(diagonal).astype(np.complex128)

    def A(self, i: int, j: int) -> np.ndarray:
        matrix = np.zeros((self.dimension, self.dimension), dtype=np.complex128)
        for column, bits in enumerate(self.basis):
            after_j, phase_j = self._gamma_even_action(bits, j)
            after_i, phase_i = self._gamma_even_action(after_j, i)
            row = self.index[after_i]
            matrix[row, column] = -1j * phase_i * phase_j
        return matrix

    def _make_A(self, i: int, j: int) -> np.ndarray:
        return self.A(i, j)

    def _make_T(self, edge_index: int) -> np.ndarray:
        i, j = self.edges[edge_index]
        return 0.5j * self.A_forward[edge_index] @ (self.B[i] - self.B[j])

    def explicit_hop(self, i: int, j: int) -> np.ndarray:
        matrix = np.zeros((self.dimension, self.dimension), dtype=np.complex128)
        for column, bits in enumerate(self.basis):
            for source, target in ((j, i), (i, j)):
                first = self._ladder_action(bits, source, create=False)
                if first is None:
                    continue
                after_annihilation, phase_one = first
                second = self._ladder_action(after_annihilation, target, create=True)
                if second is None:
                    continue
                after_creation, phase_two = second
                matrix[self.index[after_creation], column] += phase_one * phase_two
        return matrix

    def hamiltonian(self, coefficients: Sequence[float], live_mask: int) -> np.ndarray:
        result = np.zeros((self.dimension, self.dimension), dtype=np.complex128)
        for edge_index, (coefficient, term) in enumerate(zip(coefficients, self.T)):
            if (live_mask >> edge_index) & 1:
                result += coefficient * term
        return result


def tree_edge_solution(graph: Graph, vertex_bits: int) -> int:
    """Solve incidence(edge_bits)=vertex_bits on a fixed spanning tree."""

    if vertex_bits.bit_count() & 1:
        raise ValueError("the unaugmented BKSF carrier represents even parity only")
    parent: list[int | None] = [None] * graph.vertices
    parent_edge: list[int | None] = [None] * graph.vertices
    order = [0]
    parent[0] = 0
    for vertex in order:
        for edge_index, (u, v) in enumerate(graph.edges):
            if vertex == u:
                neighbor = v
            elif vertex == v:
                neighbor = u
            else:
                continue
            if parent[neighbor] is None:
                parent[neighbor] = vertex
                parent_edge[neighbor] = edge_index
                order.append(neighbor)
    if len(order) != graph.vertices:
        raise ValueError("tree solve needs a connected graph")
    subtree = [((vertex_bits >> vertex) & 1) for vertex in range(graph.vertices)]
    edge_bits = 0
    for vertex in reversed(order[1:]):
        if subtree[vertex]:
            edge_bits |= 1 << int(parent_edge[vertex])
        subtree[int(parent[vertex])] ^= subtree[vertex]
    if subtree[0]:
        raise AssertionError("even incidence solve left odd root parity")
    observed = 0
    for vertex in range(graph.vertices):
        if (edge_bits & graph.incident_mask(vertex)).bit_count() & 1:
            observed |= 1 << vertex
    if observed != vertex_bits:
        raise AssertionError("tree incidence solve failed")
    return edge_bits


@dataclass
class FaithfulCode:
    isometry: np.ndarray
    phase_consistency: float
    generator_residual: float
    loop_residual: float
    six_cycle_residual: float


def construct_faithful_code(graph: Graph, bksf: BKSF, car: EvenCAR) -> FaithfulCode:
    dimension = 1 << len(graph.edges)
    cycles = fundamental_cycles(graph, graph.full_mask)
    stabilizers = [bksf.cycle(vertices) for vertices, _ in cycles]
    group = [Pauli(0, 0, 1.0)]
    for stabilizer in stabilizers:
        group += [stabilizer @ existing for existing in group]
    if len({word.x for word in group}) != len(group):
        raise AssertionError("loop-stabilizer X masks are not independent")

    raw = np.zeros((dimension, car.dimension), dtype=np.complex128)
    normalization = math.sqrt(float(len(group)))
    for column, vertex_bits in enumerate(car.basis):
        representative = tree_edge_solution(graph, vertex_bits)
        for word in group:
            row = representative ^ word.x
            sign = -1.0 if ((representative & word.z).bit_count() & 1) else 1.0
            raw[row, column] += word.coeff * sign / normalization

    gram_residual = float(np.max(np.abs(raw.conj().T @ raw - np.eye(car.dimension))))
    if gram_residual > TOL:
        raise AssertionError(f"raw code isometry is not orthonormal: {gram_residual}")

    phases: dict[int, complex] = {car.basis[0]: 1.0 + 0.0j}
    queue: deque[int] = deque([car.basis[0]])
    consistency = 0.0
    while queue:
        bits = queue.popleft()
        column = car.index[bits]
        for edge_index, (i, j) in enumerate(graph.edges):
            target_bits = bits ^ (1 << i) ^ (1 << j)
            target = car.index[target_bits]
            physical_action = apply_pauli(
                bksf.A_forward[edge_index], raw[:, column], dimension
            )
            physical_amplitude = np.vdot(raw[:, target], physical_action)
            direct_amplitude = car.A_forward[edge_index][target, column]
            if abs(abs(physical_amplitude) - 1.0) > TOL or abs(direct_amplitude) < 0.5:
                raise AssertionError("A generator does not map between code columns")
            proposed = phases[bits] * physical_amplitude / direct_amplitude
            proposed /= abs(proposed)
            if target_bits not in phases:
                phases[target_bits] = proposed
                queue.append(target_bits)
            else:
                consistency = max(consistency, abs(phases[target_bits] - proposed))
    if len(phases) != car.dimension:
        raise AssertionError("edge-pair flips did not connect the even sector")

    aligned = raw.copy()
    for column, bits in enumerate(car.basis):
        aligned[:, column] *= phases[bits]

    generator_residual = 0.0
    for vertex, physical_B in enumerate(bksf.B):
        physical = apply_pauli(physical_B, aligned, dimension)
        direct = aligned @ car.B[vertex]
        generator_residual = max(generator_residual, float(np.max(np.abs(physical - direct))))
    for edge_index, physical_A in enumerate(bksf.A_forward):
        physical = apply_pauli(physical_A, aligned, dimension)
        direct = aligned @ car.A_forward[edge_index]
        generator_residual = max(generator_residual, float(np.max(np.abs(physical - direct))))

    loop_residual = 0.0
    for stabilizer in stabilizers:
        loop_residual = max(
            loop_residual,
            float(np.max(np.abs(apply_pauli(stabilizer, aligned, dimension) - aligned))),
        )

    six_vertices = [0, 1, 3, 7, 6, 4]
    six_stabilizer = bksf.cycle(six_vertices)
    physical_six = apply_pauli(six_stabilizer, aligned, dimension)
    direct_six = np.eye(car.dimension, dtype=np.complex128)
    for index, vertex in enumerate(six_vertices):
        direct_six = direct_six @ car.A(vertex, six_vertices[(index + 1) % 6])
    direct_six *= (1j) ** 6
    six_cycle_residual = max(
        float(np.max(np.abs(physical_six - aligned))),
        float(np.max(np.abs(direct_six - np.eye(car.dimension)))),
    )
    return FaithfulCode(
        aligned,
        consistency,
        generator_residual,
        loop_residual,
        six_cycle_residual,
    )


def fixed_number_dimension(
    component_sizes: Sequence[int],
    parities: Sequence[int],
    number: int,
) -> int:
    if len(component_sizes) != len(parities):
        raise ValueError("component sizes and parities must align")
    coefficients = [1] + [0] * number
    for size, parity in zip(component_sizes, parities):
        updated = [0] * (number + 1)
        for old_number, old_count in enumerate(coefficients):
            if not old_count:
                continue
            for local_number in range(size + 1):
                local_parity = -1 if (local_number & 1) else 1
                if local_parity != parity or old_number + local_number > number:
                    continue
                updated[old_number + local_number] += old_count * math.comb(size, local_number)
        coefficients = updated
    return coefficients[number]


@dataclass(frozen=True)
class CensusMetrics:
    masks: int
    pairs: int
    bridges: int
    nonbridges: int
    split_nontrivial: int
    max_rank_error: int
    algebra_residual: float
    fixed_number_cases: int
    impossible_fixed_number_cases: int


def exhaustive_cube_census(graph: Graph, bksf: BKSF) -> CensusMetrics:
    edge_count = len(graph.edges)
    all_masks = 1 << edge_count
    pair_count = 0
    bridge_count = 0
    nonbridge_count = 0
    split_nontrivial = 0
    max_rank_error = 0
    algebra_residual = 0.0
    component_layouts: set[tuple[int, ...]] = set()

    for recorded_mask in range(all_masks):
        live_mask = graph.full_mask ^ recorded_mask
        parts = components(graph.vertices, graph.edges, live_mask)
        component_count = len(parts)
        component_layouts.add(
            tuple(sorted(sum(1 << vertex for vertex in part) for part in parts))
        )
        live_edges = live_mask.bit_count()
        expected_cycle_rank = live_edges - graph.vertices + component_count
        cycle_data = fundamental_cycles(graph, live_mask)
        cycle_masks = [cycle_mask for _, cycle_mask in cycle_data]
        max_rank_error = max(
            max_rank_error,
            abs(len(cycle_data) - expected_cycle_rank),
            abs(gf2_rank(cycle_masks) - expected_cycle_rank),
        )
        cycle_words = [bksf.cycle(vertices) for vertices, _ in cycle_data]
        constraint_rows: list[int] = []
        for edge_index in range(edge_count):
            if (recorded_mask >> edge_index) & 1:
                constraint_rows.append((1 << edge_index) << edge_count)
        for word, cycle_mask in zip(cycle_words, cycle_masks):
            constraint_rows.append(word.x | (word.z << edge_count))
            square = word @ word
            algebra_residual = max(
                algebra_residual,
                abs(square.coeff - 1.0),
                float(square.x != 0 or square.z != 0),
                float(word.x != cycle_mask),
                abs(word.coeff.imag),
                abs(abs(word.coeff) - 1.0),
            )
        for left, right in itertools.combinations(cycle_words, 2):
            algebra_residual = max(algebra_residual, float(left.symplectic(right)))
        for edge_index in range(edge_count):
            if not ((recorded_mask >> edge_index) & 1):
                continue
            record_word = Pauli(0, 1 << edge_index)
            for cycle_word in cycle_words:
                algebra_residual = max(
                    algebra_residual, float(record_word.symplectic(cycle_word))
                )
        constraint_rank = gf2_rank(constraint_rows)
        expected_constraint_rank = edge_count - graph.vertices + component_count
        max_rank_error = max(
            max_rank_error, abs(constraint_rank - expected_constraint_rank)
        )
        physical_dimension = 1 << (edge_count - constraint_rank)
        max_rank_error = max(
            max_rank_error,
            abs(physical_dimension - (1 << (graph.vertices - component_count))),
        )

        for edge_index, (u, v) in enumerate(graph.edges):
            if not ((live_mask >> edge_index) & 1):
                continue
            pair_count += 1
            after_mask = live_mask & ~(1 << edge_index)
            after_parts = components(graph.vertices, graph.edges, after_mask)
            is_bridge = len(after_parts) == component_count + 1
            cycle_vertices = cycle_through_edge(graph, live_mask, edge_index)
            if is_bridge:
                bridge_count += 1
                if cycle_vertices is not None:
                    algebra_residual = max(algebra_residual, 1.0)
                cut_part = next(part for part in after_parts if u in part)
                cut_mask = boundary_mask(graph, cut_part)
                algebra_residual = max(
                    algebra_residual,
                    float((cut_mask & live_mask) != (1 << edge_index)),
                )
                b_product = 0
                for vertex in cut_part:
                    b_product ^= bksf.B[vertex].z
                algebra_residual = max(
                    algebra_residual, float(b_product != cut_mask)
                )
                other_size = len(next(part for part in after_parts if v in part))
                if len(cut_part) > 1 and other_size > 1:
                    split_nontrivial += 1
            else:
                nonbridge_count += 1
                if cycle_vertices is None:
                    algebra_residual = max(algebra_residual, 1.0)
                    continue
                stabilizer = bksf.cycle(cycle_vertices)
                record_word = Pauli(0, 1 << edge_index)
                algebra_residual = max(
                    algebra_residual,
                    abs(float(stabilizer.symplectic(record_word)) - 1.0),
                )
                for vertex_word in bksf.B:
                    algebra_residual = max(
                        algebra_residual,
                        float(stabilizer.symplectic(vertex_word)),
                    )
                for live_edge, a_word in enumerate(bksf.A_forward):
                    if live_edge != edge_index and ((live_mask >> live_edge) & 1):
                        algebra_residual = max(
                            algebra_residual, float(stabilizer.symplectic(a_word))
                        )

    fixed_number_cases = 0
    impossible_cases = 0
    half_number = graph.vertices // 2
    fixed_number_residual = 0
    half_basis = [
        bits
        for bits in range(1 << graph.vertices)
        if bits.bit_count() == half_number
    ]
    for layout in component_layouts:
        component_count = len(layout)
        sizes = [mask.bit_count() for mask in layout]
        for free_parities in range(1 << max(0, component_count - 1)):
            parities = [
                -1 if ((free_parities >> index) & 1) else 1
                for index in range(component_count - 1)
            ]
            parities.append(math.prod(parities))
            formula = fixed_number_dimension(sizes, parities, half_number)
            direct = 0
            for bits in half_basis:
                observed = [
                    -1 if ((bits & mask).bit_count() & 1) else 1 for mask in layout
                ]
                direct += int(observed == parities)
            fixed_number_residual = max(fixed_number_residual, abs(formula - direct))
            impossible_cases += int(formula == 0)
            fixed_number_cases += 1
    algebra_residual = max(algebra_residual, float(fixed_number_residual))
    return CensusMetrics(
        all_masks,
        pair_count,
        bridge_count,
        nonbridge_count,
        split_nontrivial,
        max_rank_error,
        algebra_residual,
        fixed_number_cases,
        impossible_cases,
    )


@dataclass(frozen=True)
class AlgebraMetrics:
    residual: float
    separate_word_commutator: float
    max_support: int
    max_radius: int
    max_diameter: int
    distinct_edge_sites: int


def full_algebra_and_placement(graph: Graph, bksf: BKSF) -> AlgebraMetrics:
    edge_count = len(graph.edges)
    identity = operator(Pauli(0, 0, 1.0))
    total_number = op_scale(identity, graph.vertices / 2.0)
    for vertex_word in bksf.B:
        total_number = op_add(total_number, operator(vertex_word.scaled(-0.5)))

    residual = 0.0
    separate_commutator = 0.0
    all_b = Pauli(0, 0, 1.0)
    for vertex_word in bksf.B:
        all_b = all_b @ vertex_word
    residual = max(
        residual,
        abs(all_b.coeff - 1.0),
        float(all_b.x != 0 or all_b.z != 0),
    )
    for edge_index, (i, j) in enumerate(graph.edges):
        forward = bksf.A(i, j)
        reverse = bksf.A(j, i)
        residual = max(
            residual,
            abs(forward.coeff + reverse.coeff),
            float(forward.x != reverse.x or forward.z != reverse.z),
        )
        reverse_left = (reverse @ bksf.B[j]).scaled(0.5j)
        reverse_right = (reverse @ bksf.B[i]).scaled(-0.5j)
        reverse_t = operator(reverse_left, reverse_right)
        residual = max(residual, op_residual(reverse_t, bksf.T[edge_index]))
        residual = max(
            residual,
            op_residual(op_dagger(bksf.T[edge_index]), bksf.T[edge_index]),
            max(
                (
                    abs(value)
                    for value in op_commutator(
                        bksf.T[edge_index], total_number
                    ).values()
                ),
                default=0.0,
            ),
        )
        target_square = op_scale(
            op_add(identity, operator((bksf.B[i] @ bksf.B[j]).scaled(-1.0))),
            0.5 * graph.coefficients[edge_index] ** 2,
        )
        residual = max(
            residual,
            op_residual(op_mul(bksf.h[edge_index], bksf.h[edge_index]), target_square),
        )
        first_word = operator(next(iter(
            Pauli(x, z, coefficient)
            for (x, z), coefficient in bksf.T[edge_index].items()
        )))
        separate_commutator = max(
            separate_commutator,
            max(
                (
                    abs(value)
                    for value in op_commutator(first_word, total_number).values()
                ),
                default=0.0,
            ),
        )
        for other_edge, other_a in enumerate(bksf.A_forward):
            if other_edge != edge_index:
                residual = max(
                    residual,
                    float(Pauli(0, 1 << edge_index).symplectic(other_a)),
                )
        for vertex_word in bksf.B:
            residual = max(
                residual,
                float(Pauli(0, 1 << edge_index).symplectic(vertex_word)),
            )

    if graph.coordinates is None:
        return AlgebraMetrics(residual, separate_commutator, 0, 0, 0, 0)

    edge_sites: list[tuple[int, int, int]] = []
    for u, v in graph.edges:
        cu, cv = graph.coordinates[u], graph.coordinates[v]
        edge_sites.append(tuple(cu[axis] + cv[axis] for axis in range(3)))
    virtual_vertices = {
        tuple(2 * coordinate[axis] for axis in range(3))
        for coordinate in graph.coordinates
    }
    residual = max(
        residual,
        float(len(set(edge_sites)) != edge_count),
        float(any(site in virtual_vertices for site in edge_sites)),
    )
    max_support = 0
    max_radius = 0
    max_diameter = 0
    degrees = [graph.incident_mask(vertex).bit_count() for vertex in range(graph.vertices)]
    for edge_index, (u, v) in enumerate(graph.edges):
        support_mask = 0
        for xmask, zmask in bksf.h[edge_index]:
            support_mask |= xmask | zmask
        support = [number for number in range(edge_count) if (support_mask >> number) & 1]
        endpoint_stars = graph.incident_mask(u) | graph.incident_mask(v)
        max_support = max(max_support, len(support))
        center = edge_sites[edge_index]
        radii = [
            sum(abs(edge_sites[number][axis] - center[axis]) for axis in range(3))
            for number in support
        ]
        max_radius = max(max_radius, max(radii, default=0))
        for left, right in itertools.combinations(support, 2):
            distance = sum(
                abs(edge_sites[left][axis] - edge_sites[right][axis]) for axis in range(3)
            )
            max_diameter = max(max_diameter, distance)
        residual = max(
            residual,
            float(bool(support_mask & ~endpoint_stars)),
            float(len(support) > degrees[u] + degrees[v] - 1),
            float(any(radius > 2 for radius in radii)),
        )
    residual = max(residual, float(max_diameter > 4))
    return AlgebraMetrics(
        residual,
        separate_commutator,
        max_support,
        max_radius,
        max_diameter,
        len(set(edge_sites)),
    )


@dataclass
class CubeModel:
    graph: Graph
    bksf: BKSF
    car: EvenCAR
    code: FaithfulCode
    physical_hops: tuple[sp.csr_matrix, ...]
    direct_hops: tuple[np.ndarray, ...]
    physical_number_diagonal: np.ndarray
    physical_indices: np.ndarray

    def physical_hamiltonian(self, live_mask: int) -> sp.csr_matrix:
        result = sp.csr_matrix(
            (1 << len(self.graph.edges), 1 << len(self.graph.edges)),
            dtype=np.complex128,
        )
        for edge_index, term in enumerate(self.physical_hops):
            if (live_mask >> edge_index) & 1:
                result = result + term
        result.eliminate_zeros()
        return result

    def direct_hamiltonian(self, live_mask: int) -> np.ndarray:
        result = np.zeros((self.car.dimension, self.car.dimension), dtype=np.complex128)
        for edge_index, term in enumerate(self.direct_hops):
            if (live_mask >> edge_index) & 1:
                result += term
        return result


def build_cube_model() -> CubeModel:
    graph = make_open_cube()
    bksf = BKSF(graph)
    car = EvenCAR(graph.vertices, graph.edges)
    code = construct_faithful_code(graph, bksf, car)
    physical_hops = tuple(
        sparse_operator(term, len(graph.edges)) for term in bksf.h
    )
    direct_hops = tuple(
        coefficient * term
        for coefficient, term in zip(graph.coefficients, car.T)
    )
    indices = np.arange(1 << len(graph.edges), dtype=np.int64)
    number_diagonal = np.zeros(len(indices), dtype=np.float64)
    for vertex in range(graph.vertices):
        number_diagonal += 0.5 * (
            1.0 - parity_signs(indices, graph.incident_mask(vertex))
        )
    return CubeModel(
        graph,
        bksf,
        car,
        code,
        physical_hops,
        direct_hops,
        number_diagonal,
        indices,
    )


@dataclass(frozen=True)
class BulkMetrics:
    cube_energy: float
    ell4_energy_density: float
    max_spectral_residual: float
    max_trace_residual: float
    max_norm_margin: float
    ell4_quarter_tail_bound: float


def open_cubic_one_particle(side: int, hopping: float = 1.0) -> tuple[np.ndarray, int, int]:
    if side < 2 or side % 2:
        raise ValueError("the open cubic side must be even and at least two")
    vertices = side ** 3
    if vertices % 4:
        raise ValueError("half filling must have even global parity")
    index = {
        (x, y, z): (x * side + y) * side + z
        for x in range(side)
        for y in range(side)
        for z in range(side)
    }
    matrix = np.zeros((vertices, vertices), dtype=np.float64)
    edge_count = 0
    for x in range(side):
        for y in range(side):
            for z in range(side):
                coordinate = (x, y, z)
                for axis in range(3):
                    if coordinate[axis] + 1 >= side:
                        continue
                    neighbor = list(coordinate)
                    neighbor[axis] += 1
                    eta = (1.0, (-1.0) ** x, (-1.0) ** (x + y))[axis]
                    u, v = index[coordinate], index[tuple(neighbor)]
                    matrix[u, v] = matrix[v, u] = -hopping * eta
                    edge_count += 1
    return matrix, vertices, edge_count


def bulk_energy_checks(model: CubeModel) -> BulkMetrics:
    maximum_spectral_residual = 0.0
    maximum_trace_residual = 0.0
    maximum_norm_margin = 0.0
    ell4_quarter_tail_bound = math.nan
    energies: dict[int, float] = {}
    for side in (2, 4):
        one_particle, vertices, edges = open_cubic_one_particle(side)
        eigenvalues = np.linalg.eigvalsh(one_particle)
        degree_bound = 3 if side == 2 else 6
        maximum_spectral_residual = max(
            maximum_spectral_residual,
            float(np.max(np.abs(eigenvalues + eigenvalues[::-1]))),
        )
        maximum_trace_residual = max(
            maximum_trace_residual,
            abs(float(np.trace(one_particle @ one_particle)) - 2.0 * edges),
            abs(edges - 3 * side * side * (side - 1)),
        )
        operator_norm = float(np.max(np.abs(eigenvalues)))
        maximum_norm_margin = max(maximum_norm_margin, max(0.0, operator_norm - degree_bound))
        ground_energy = float(np.sum(eigenvalues[: vertices // 2]))
        trace_absolute_energy = -0.5 * float(np.sum(np.abs(eigenvalues)))
        maximum_spectral_residual = max(
            maximum_spectral_residual,
            abs(ground_energy - trace_absolute_energy),
            max(0.0, ground_energy + edges / degree_bound),
        )
        energies[side] = ground_energy
        for deleted in (1, edges // 4, edges // 2, edges - 1):
            tail = min(1.0, degree_bound ** 2 * deleted / (edges - deleted) ** 2)
            direct_chebyshev = min(
                1.0,
                deleted
                / (ground_energy ** 2 * (1.0 - deleted / edges) ** 2),
            )
            maximum_spectral_residual = max(
                maximum_spectral_residual,
                max(0.0, direct_chebyshev - tail),
            )
            if side == 4 and deleted == edges // 4:
                ell4_quarter_tail_bound = tail

    cube_h = model.direct_hamiltonian(model.graph.full_mask)
    number_four = [
        index for index, bits in enumerate(model.car.basis) if bits.bit_count() == 4
    ]
    cube_many_ground = float(
        np.min(np.linalg.eigvalsh(cube_h[np.ix_(number_four, number_four)]))
    )
    maximum_spectral_residual = max(
        maximum_spectral_residual, abs(cube_many_ground - energies[2])
    )
    return BulkMetrics(
        energies[2],
        energies[4] / 64.0,
        maximum_spectral_residual,
        maximum_trace_residual,
        maximum_norm_margin,
        ell4_quarter_tail_bound,
    )


def physical_record_projection(
    model: CubeModel,
    state: np.ndarray,
    edge_index: int,
    outcome: int,
) -> np.ndarray:
    if outcome not in (-1, 1):
        raise ValueError("a Z outcome is +1 or -1")
    keep_bit = 1 if outcome == -1 else 0
    allowed = ((model.physical_indices >> edge_index) & 1) == keep_bit
    return np.where(allowed, state, 0.0j)


def bridge_component(graph: Graph, live_mask: int, edge_index: int) -> tuple[int, ...]:
    after_mask = live_mask & ~(1 << edge_index)
    before_count = len(components(graph.vertices, graph.edges, live_mask))
    after_parts = components(graph.vertices, graph.edges, after_mask)
    if len(after_parts) != before_count + 1:
        raise ValueError("the requested edge is not a bridge")
    u, _ = graph.edges[edge_index]
    return next(part for part in after_parts if u in part)


def old_boundary_sign(
    graph: Graph,
    component: Sequence[int],
    recorded_mask: int,
    record_sign_bits: int,
) -> int:
    old_boundary = boundary_mask(graph, component) & recorded_mask
    return -1 if ((old_boundary & record_sign_bits).bit_count() & 1) else 1


def direct_parity_projection(
    car: EvenCAR,
    state: np.ndarray,
    component: Sequence[int],
    desired_parity: int,
) -> np.ndarray:
    vertex_mask = sum(1 << vertex for vertex in component)
    allowed = np.array(
        [
            (-1 if ((bits & vertex_mask).bit_count() & 1) else 1) == desired_parity
            for bits in car.basis
        ],
        dtype=bool,
    )
    return np.where(allowed, state, 0.0j)


def branch_embed(
    model: CubeModel,
    direct_state: np.ndarray,
    recorded_mask: int,
    record_sign_bits: int,
) -> np.ndarray:
    physical = model.code.isometry @ direct_state
    allowed = (model.physical_indices & recorded_mask) == (
        record_sign_bits & recorded_mask
    )
    physical = np.where(allowed, physical, 0.0j)
    live_mask = model.graph.full_mask ^ recorded_mask
    component_count = len(components(model.graph.vertices, model.graph.edges, live_mask))
    nonbridge_records = recorded_mask.bit_count() - (component_count - 1)
    return physical * math.sqrt(float(1 << nonbridge_records))


def phase_aligned_distance(left: np.ndarray, right: np.ndarray) -> float:
    overlap = np.vdot(right, left)
    if abs(overlap) <= PROB_TOL:
        return float(np.linalg.norm(left - right))
    phase = overlap / abs(overlap)
    return float(np.linalg.norm(left - phase * right))


def alignment_phase(left: np.ndarray, right: np.ndarray) -> complex:
    overlap = np.vdot(right, left)
    if abs(overlap) <= PROB_TOL:
        return 1.0 + 0.0j
    return overlap / abs(overlap)


def expectation(state: np.ndarray, operator_state: np.ndarray) -> float:
    value = np.vdot(state, operator_state)
    if abs(value.imag) > 5.0e-9:
        raise AssertionError(f"expected a real observable value, got {value}")
    return float(value.real)


def evolve_direct(hamiltonian: np.ndarray, state: np.ndarray, dwell: float) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    amplitudes = eigenvectors.conj().T @ state
    return eigenvectors @ (np.exp(-1j * dwell * eigenvalues) * amplitudes)


def evolve_physical(
    hamiltonian: sp.csr_matrix,
    state: np.ndarray,
    dwell: float,
) -> np.ndarray:
    if dwell == 0.0:
        return state.copy()
    return np.asarray(
        expm_multiply(-1j * dwell * hamiltonian, state, traceA=0.0),
        dtype=np.complex128,
    )


@dataclass
class Branch:
    weight: float
    physical: np.ndarray
    direct: np.ndarray
    recorded_mask: int
    record_sign_bits: int


@dataclass
class HistoryMetrics:
    histories: int = 0
    nonzero_branches: int = 0
    zero_outcomes: int = 0
    deterministic_outcomes: int = 0
    bridge_events: int = 0
    nonbridge_events: int = 0
    max_probability_residual: float = 0.0
    max_state_residual: float = 0.0
    max_generator_residual: float = 0.0
    max_record_residual: float = 0.0
    max_number_residual: float = 0.0
    max_energy_residual: float = 0.0
    max_dwell_energy_residual: float = 0.0
    max_nonbridge_functional_residual: float = 0.0

    def merge(self, other: "HistoryMetrics") -> None:
        for name in (
            "histories",
            "nonzero_branches",
            "zero_outcomes",
            "deterministic_outcomes",
            "bridge_events",
            "nonbridge_events",
        ):
            setattr(self, name, getattr(self, name) + getattr(other, name))
        for name in (
            "max_probability_residual",
            "max_state_residual",
            "max_generator_residual",
            "max_record_residual",
            "max_number_residual",
            "max_energy_residual",
            "max_dwell_energy_residual",
            "max_nonbridge_functional_residual",
        ):
            setattr(self, name, max(getattr(self, name), getattr(other, name)))

    @property
    def maximum_residual(self) -> float:
        return max(
            self.max_probability_residual,
            self.max_state_residual,
            self.max_generator_residual,
            self.max_record_residual,
            self.max_number_residual,
            self.max_energy_residual,
            self.max_dwell_energy_residual,
            self.max_nonbridge_functional_residual,
        )


def branch_observable_checks(
    model: CubeModel, branch: Branch
) -> tuple[float, float, float, float, float]:
    live_mask = model.graph.full_mask ^ branch.recorded_mask
    expected_state = branch_embed(
        model, branch.direct, branch.recorded_mask, branch.record_sign_bits
    )
    common_phase = alignment_phase(branch.physical, expected_state)
    state_residual = float(np.linalg.norm(branch.physical - common_phase * expected_state))
    generator_residual = 0.0
    dimension = 1 << len(model.graph.edges)
    for vertex, physical_word in enumerate(model.bksf.B):
        physical_action = apply_pauli(physical_word, branch.physical, dimension)
        direct_action = branch_embed(
            model,
            model.car.B[vertex] @ branch.direct,
            branch.recorded_mask,
            branch.record_sign_bits,
        )
        generator_residual = max(
            generator_residual,
            float(np.linalg.norm(physical_action - common_phase * direct_action)),
        )
    for edge_index, physical_word in enumerate(model.bksf.A_forward):
        if not ((live_mask >> edge_index) & 1):
            continue
        physical_action = apply_pauli(physical_word, branch.physical, dimension)
        direct_action = branch_embed(
            model,
            model.car.A_forward[edge_index] @ branch.direct,
            branch.recorded_mask,
            branch.record_sign_bits,
        )
        generator_residual = max(
            generator_residual,
            float(np.linalg.norm(physical_action - common_phase * direct_action)),
        )

    record_residual = 0.0
    for edge_index in range(len(model.graph.edges)):
        if not ((branch.recorded_mask >> edge_index) & 1):
            continue
        outcome = -1.0 if ((branch.record_sign_bits >> edge_index) & 1) else 1.0
        action = apply_pauli(
            Pauli(0, 1 << edge_index), branch.physical, dimension
        )
        record_residual = max(
            record_residual, float(np.linalg.norm(action - outcome * branch.physical))
        )

    direct_number = model.car.N @ branch.direct
    physical_number = model.physical_number_diagonal * branch.physical
    number_residual = max(
        abs(expectation(branch.direct, direct_number) - 4.0),
        float(np.linalg.norm(direct_number - 4.0 * branch.direct)),
        float(np.linalg.norm(physical_number - 4.0 * branch.physical)),
    )

    physical_h = model.physical_hamiltonian(live_mask)
    direct_h = model.direct_hamiltonian(live_mask)
    physical_h_state = physical_h @ branch.physical
    direct_h_state = direct_h @ branch.direct
    embedded_h_state = branch_embed(
        model, direct_h_state, branch.recorded_mask, branch.record_sign_bits
    )
    physical_energy = expectation(branch.physical, physical_h_state)
    direct_energy = expectation(branch.direct, direct_h_state)
    physical_second = float(np.vdot(physical_h_state, physical_h_state).real)
    direct_second = float(np.vdot(direct_h_state, direct_h_state).real)
    energy_residual = max(
        abs(physical_energy - direct_energy),
        abs(physical_second - direct_second),
        float(np.linalg.norm(physical_h_state - common_phase * embedded_h_state)),
    )
    return (
        state_residual,
        generator_residual,
        record_residual,
        number_residual,
        energy_residual,
    )


def nonbridge_functional_residual(
    model: CubeModel,
    parent: Branch,
    projected: np.ndarray,
    probability: float,
    deleted_edge: int,
) -> float:
    live_after = model.graph.full_mask ^ (parent.recorded_mask | (1 << deleted_edge))
    residual = 0.0
    dimension = 1 << len(model.graph.edges)
    normalized = projected / math.sqrt(probability)
    for vertex_word in model.bksf.B:
        before = expectation(
            parent.physical, apply_pauli(vertex_word, parent.physical, dimension)
        )
        after = expectation(normalized, apply_pauli(vertex_word, normalized, dimension))
        residual = max(residual, abs(before - after))
    for edge_index, a_word in enumerate(model.bksf.A_forward):
        if not ((live_after >> edge_index) & 1):
            continue
        before = expectation(parent.physical, apply_pauli(a_word, parent.physical, dimension))
        after = expectation(normalized, apply_pauli(a_word, normalized, dimension))
        residual = max(residual, abs(before - after))
    return residual


def run_history(
    model: CubeModel,
    initial_direct: np.ndarray,
    edge_order: Sequence[int],
    dwells: Sequence[float],
) -> tuple[HistoryMetrics, list[Branch]]:
    if len(edge_order) != len(dwells) or len(set(edge_order)) != len(edge_order):
        raise ValueError("history edges and dwells must be distinct and aligned")
    initial_direct = initial_direct / np.linalg.norm(initial_direct)
    branches = [
        Branch(
            1.0,
            model.code.isometry @ initial_direct,
            initial_direct.copy(),
            0,
            0,
        )
    ]
    metrics = HistoryMetrics(histories=1)
    for edge_index, dwell in zip(edge_order, dwells):
        if dwell < 0.0 or not math.isfinite(dwell):
            raise ValueError("dwell times must be finite and nonnegative")
        next_branches: list[Branch] = []
        for parent in branches:
            if (parent.recorded_mask >> edge_index) & 1:
                raise ValueError("an edge cannot form a second Record")
            live_mask = model.graph.full_mask ^ parent.recorded_mask
            physical_h = model.physical_hamiltonian(live_mask)
            direct_h = model.direct_hamiltonian(live_mask)
            energy_before_physical = expectation(parent.physical, physical_h @ parent.physical)
            energy_before_direct = expectation(parent.direct, direct_h @ parent.direct)
            parent.physical = evolve_physical(physical_h, parent.physical, dwell)
            parent.direct = evolve_direct(direct_h, parent.direct, dwell)
            energy_after_physical = expectation(parent.physical, physical_h @ parent.physical)
            energy_after_direct = expectation(parent.direct, direct_h @ parent.direct)
            metrics.max_dwell_energy_residual = max(
                metrics.max_dwell_energy_residual,
                abs(energy_before_physical - energy_after_physical),
                abs(energy_before_direct - energy_after_direct),
                abs(energy_after_physical - energy_after_direct),
                phase_aligned_distance(
                    parent.physical,
                    branch_embed(
                        model,
                        parent.direct,
                        parent.recorded_mask,
                        parent.record_sign_bits,
                    ),
                ),
            )
            cycle = cycle_through_edge(model.graph, live_mask, edge_index)
            is_bridge = cycle is None
            metrics.bridge_events += int(is_bridge)
            metrics.nonbridge_events += int(not is_bridge)
            component: tuple[int, ...] | None = None
            old_sign = 1
            if is_bridge:
                component = bridge_component(model.graph, live_mask, edge_index)
                old_sign = old_boundary_sign(
                    model.graph,
                    component,
                    parent.recorded_mask,
                    parent.record_sign_bits,
                )
            parent_probability_sum = 0.0
            for outcome in (1, -1):
                physical_projected = physical_record_projection(
                    model, parent.physical, edge_index, outcome
                )
                physical_probability = float(np.vdot(physical_projected, physical_projected).real)
                if is_bridge:
                    assert component is not None
                    direct_projected = direct_parity_projection(
                        model.car, parent.direct, component, outcome * old_sign
                    )
                    direct_probability = float(np.vdot(direct_projected, direct_projected).real)
                else:
                    direct_projected = math.sqrt(0.5) * parent.direct
                    direct_probability = 0.5
                    if physical_probability > PROB_TOL:
                        metrics.max_nonbridge_functional_residual = max(
                            metrics.max_nonbridge_functional_residual,
                            nonbridge_functional_residual(
                                model,
                                parent,
                                physical_projected,
                                physical_probability,
                                edge_index,
                            ),
                        )
                metrics.max_probability_residual = max(
                    metrics.max_probability_residual,
                    abs(physical_probability - direct_probability),
                    abs(direct_probability - 0.5) if not is_bridge else 0.0,
                )
                parent_probability_sum += physical_probability
                if direct_probability <= PROB_TOL:
                    metrics.zero_outcomes += 1
                    metrics.max_probability_residual = max(
                        metrics.max_probability_residual, physical_probability
                    )
                    continue
                if direct_probability >= 1.0 - PROB_TOL:
                    metrics.deterministic_outcomes += 1
                new_recorded = parent.recorded_mask | (1 << edge_index)
                new_sign_bits = parent.record_sign_bits
                if outcome == -1:
                    new_sign_bits |= 1 << edge_index
                else:
                    new_sign_bits &= ~(1 << edge_index)
                child = Branch(
                    parent.weight * physical_probability,
                    physical_projected / math.sqrt(physical_probability),
                    direct_projected / math.sqrt(direct_probability),
                    new_recorded,
                    new_sign_bits,
                )
                (
                    state_r,
                    generator_r,
                    record_r,
                    number_r,
                    energy_r,
                ) = branch_observable_checks(model, child)
                metrics.max_state_residual = max(metrics.max_state_residual, state_r)
                metrics.max_generator_residual = max(
                    metrics.max_generator_residual, generator_r
                )
                metrics.max_record_residual = max(metrics.max_record_residual, record_r)
                metrics.max_number_residual = max(
                    metrics.max_number_residual, number_r
                )
                metrics.max_energy_residual = max(metrics.max_energy_residual, energy_r)
                next_branches.append(child)
            metrics.max_probability_residual = max(
                metrics.max_probability_residual, abs(parent_probability_sum - 1.0)
            )
        branches = next_branches
        metrics.max_probability_residual = max(
            metrics.max_probability_residual,
            abs(sum(branch.weight for branch in branches) - 1.0),
        )
    metrics.nonzero_branches = len(branches)
    return metrics, branches


def selected_initial_states(model: CubeModel) -> dict[str, np.ndarray]:
    number_four = [
        index for index, bits in enumerate(model.car.basis) if bits.bit_count() == 4
    ]
    hamiltonian = model.direct_hamiltonian(model.graph.full_mask)
    eigenvalues, eigenvectors = np.linalg.eigh(
        hamiltonian[np.ix_(number_four, number_four)]
    )
    sea = np.zeros(model.car.dimension, dtype=np.complex128)
    sea[number_four] = eigenvectors[:, int(np.argmin(eigenvalues))]
    rng = np.random.default_rng(SEED)
    values = rng.normal(size=len(number_four)) + 1j * rng.normal(size=len(number_four))
    values /= np.linalg.norm(values)
    generic = np.zeros(model.car.dimension, dtype=np.complex128)
    generic[number_four] = values
    deterministic_bits = sum(1 << vertex for vertex in (0, 1, 2, 3))
    deterministic = np.zeros(model.car.dimension, dtype=np.complex128)
    deterministic[model.car.index[deterministic_bits]] = 1.0
    return {"sea": sea, "generic": generic, "deterministic": deterministic}


def history_suite(model: CubeModel) -> HistoryMetrics:
    states = selected_initial_states(model)
    incident = [
        index for index, edge in enumerate(model.graph.edges) if 0 in edge
    ]
    first_order = incident
    second_order = [incident[1], incident[0], incident[2]]
    combined = HistoryMetrics()
    for state_name in ("sea", "generic"):
        for order, dwells in (
            (first_order, (0.17, 0.29, 0.11)),
            (second_order, (0.23, 0.07, 0.31)),
        ):
            metrics, _ = run_history(model, states[state_name], order, dwells)
            combined.merge(metrics)
    deterministic_metrics, _ = run_history(
        model, states["deterministic"], first_order, (0.0, 0.0, 0.0)
    )
    combined.merge(deterministic_metrics)

    x_cut = [
        index
        for index, (u, v) in enumerate(model.graph.edges)
        if model.graph.coordinates is not None
        and model.graph.coordinates[u][0] != model.graph.coordinates[v][0]
    ]
    split_metrics, split_branches = run_history(
        model,
        states["generic"],
        x_cut,
        (0.09, 0.15, 0.21, 0.27),
    )
    combined.merge(split_metrics)
    final_parts = components(
        model.graph.vertices,
        model.graph.edges,
        model.graph.full_mask ^ sum(1 << edge for edge in x_cut),
    )
    if sorted(map(len, final_parts)) != [4, 4] or not split_branches:
        combined.max_state_residual = max(combined.max_state_residual, 1.0)
    return combined


@dataclass(frozen=True)
class UniformMetrics:
    states: int
    max_residual: float
    largest_variance_increment: float
    largest_local_square: float


def propagate_selected_branch(
    model: CubeModel,
    initial: np.ndarray,
    edge_order: Sequence[int],
    outcomes: Sequence[int],
    dwells: Sequence[float],
) -> Branch:
    branch = Branch(1.0, model.code.isometry @ initial, initial.copy(), 0, 0)
    for edge_index, outcome, dwell in zip(edge_order, outcomes, dwells):
        live_mask = model.graph.full_mask ^ branch.recorded_mask
        physical_h = model.physical_hamiltonian(live_mask)
        direct_h = model.direct_hamiltonian(live_mask)
        branch.physical = evolve_physical(physical_h, branch.physical, dwell)
        branch.direct = evolve_direct(direct_h, branch.direct, dwell)
        physical_projected = physical_record_projection(
            model, branch.physical, edge_index, outcome
        )
        physical_probability = float(np.vdot(physical_projected, physical_projected).real)
        cycle = cycle_through_edge(model.graph, live_mask, edge_index)
        if cycle is None:
            part = bridge_component(model.graph, live_mask, edge_index)
            sign = old_boundary_sign(
                model.graph, part, branch.recorded_mask, branch.record_sign_bits
            )
            direct_projected = direct_parity_projection(
                model.car, branch.direct, part, outcome * sign
            )
            direct_probability = float(np.vdot(direct_projected, direct_projected).real)
        else:
            direct_projected = math.sqrt(0.5) * branch.direct
            direct_probability = 0.5
        if min(physical_probability, direct_probability) <= PROB_TOL:
            raise ValueError("selected probe branch has zero probability")
        branch.physical = physical_projected / math.sqrt(physical_probability)
        branch.direct = direct_projected / math.sqrt(direct_probability)
        branch.weight *= physical_probability
        branch.recorded_mask |= 1 << edge_index
        if outcome == -1:
            branch.record_sign_bits |= 1 << edge_index
    return branch


def actual_uniform_edge_probe(model: CubeModel) -> UniformMetrics:
    states = selected_initial_states(model)
    incident = [
        index for index, edge in enumerate(model.graph.edges) if 0 in edge
    ]
    probes = [
        propagate_selected_branch(
            model, states["generic"], incident[:2], (1, -1), (0.19, 0.37)
        ),
        propagate_selected_branch(
            model, states["sea"], incident[:1], (-1,), (0.41,)
        ),
    ]
    maximum_residual = 0.0
    largest_increment = -math.inf
    largest_local_square = 0.0
    for branch in probes:
        live_mask = model.graph.full_mask ^ branch.recorded_mask
        live_edges = [
            edge for edge in range(len(model.graph.edges)) if (live_mask >> edge) & 1
        ]
        q = len(live_edges)
        edge_weight = 1.0 / float(q)
        current_physical_h = model.physical_hamiltonian(live_mask)
        current_direct_h = model.direct_hamiltonian(live_mask)
        current_physical_action = current_physical_h @ branch.physical
        current_direct_action = current_direct_h @ branch.direct
        current_mu = expectation(branch.physical, current_physical_action)
        current_q2 = float(np.vdot(current_physical_action, current_physical_action).real)
        current_variance = current_q2 - current_mu ** 2
        maximum_residual = max(
            maximum_residual,
            abs(current_mu - expectation(branch.direct, current_direct_action)),
            abs(current_q2 - float(np.vdot(current_direct_action, current_direct_action).real)),
        )

        actual_mu = 0.0
        actual_q2 = 0.0
        actual_number = 0.0
        direct_mu = 0.0
        direct_q2 = 0.0
        local_square = 0.0
        total_probability = 0.0
        for edge_index in live_edges:
            physical_out = current_physical_h - model.physical_hops[edge_index]
            direct_out = current_direct_h - model.direct_hops[edge_index]
            local_action = model.physical_hops[edge_index] @ branch.physical
            local_square += edge_weight * float(np.vdot(local_action, local_action).real)
            largest_local_square = max(
                largest_local_square, float(np.vdot(local_action, local_action).real)
            )
            for outcome in (1, -1):
                physical_projected = physical_record_projection(
                    model, branch.physical, edge_index, outcome
                )
                probability = float(np.vdot(physical_projected, physical_projected).real)
                total_probability += edge_weight * probability
                physical_out_state = physical_out @ physical_projected
                actual_mu += edge_weight * expectation(
                    physical_projected, physical_out_state
                )
                actual_q2 += edge_weight * float(
                    np.vdot(physical_out_state, physical_out_state).real
                )
                actual_number += edge_weight * expectation(
                    physical_projected,
                    model.physical_number_diagonal * physical_projected,
                )

                cycle = cycle_through_edge(model.graph, live_mask, edge_index)
                if cycle is None:
                    part = bridge_component(model.graph, live_mask, edge_index)
                    sign = old_boundary_sign(
                        model.graph,
                        part,
                        branch.recorded_mask,
                        branch.record_sign_bits,
                    )
                    direct_amplitudes = direct_parity_projection(
                        model.car, branch.direct, part, outcome * sign
                    )
                else:
                    direct_amplitudes = math.sqrt(0.5) * branch.direct
                direct_out_state = direct_out @ direct_amplitudes
                direct_mu += edge_weight * expectation(
                    direct_amplitudes, direct_out_state
                )
                direct_q2 += edge_weight * float(
                    np.vdot(direct_out_state, direct_out_state).real
                )

        target_mu = (1.0 - 1.0 / q) * current_mu
        target_q2 = (1.0 - 2.0 / q) * current_q2 + local_square
        actual_variance = actual_q2 - actual_mu ** 2
        target_variance = (
            (1.0 - 2.0 / q) * current_variance
            - current_mu ** 2 / q ** 2
            + local_square
        )
        largest_increment = max(largest_increment, actual_variance - current_variance)
        maximum_residual = max(
            maximum_residual,
            abs(total_probability - 1.0),
            abs(actual_mu - target_mu),
            abs(actual_q2 - target_q2),
            abs(actual_variance - target_variance),
            abs(actual_number - 4.0),
            abs(direct_mu - actual_mu),
            abs(direct_q2 - actual_q2),
            max(0.0, actual_variance - current_variance - 1.0),
        )
    return UniformMetrics(
        len(probes), maximum_residual, largest_increment, largest_local_square
    )


@dataclass(frozen=True)
class ApparatusIdentityMetrics:
    defect_residual: float
    defect_norm_margin: float
    telescope_residual: float
    support_residual: float
    tested_fibres: int


def event_defect_residual(
    model: CubeModel,
    branch: Branch,
    edge_index: int,
) -> tuple[float, float, int]:
    live_mask = model.graph.full_mask ^ branch.recorded_mask
    if not ((live_mask >> edge_index) & 1):
        raise ValueError("defect test requires a live edge")
    h_in = model.physical_hamiltonian(live_mask)
    h_edge = model.physical_hops[edge_index]
    h_out = h_in - h_edge
    input_h_state = h_in @ branch.physical
    edge_state = h_edge @ branch.physical
    residual = 0.0
    defect_norm = 0.0
    fibres = 0
    for outcome in (1, -1):
        projected = physical_record_projection(
            model, branch.physical, edge_index, outcome
        )
        left = h_out @ projected - physical_record_projection(
            model, input_h_state, edge_index, outcome
        )
        right = -physical_record_projection(
            model, edge_state, edge_index, outcome
        )
        residual = max(residual, float(np.linalg.norm(left - right)))
        defect_norm += float(np.vdot(left, left).real)
        fibres += 1
    norm_margin = max(0.0, math.sqrt(defect_norm) - 1.0)
    return residual, norm_margin, fibres


def apparatus_operator_identities(model: CubeModel) -> ApparatusIdentityMetrics:
    states = selected_initial_states(model)
    initial = Branch(
        1.0,
        model.code.isometry @ states["generic"],
        states["generic"].copy(),
        0,
        0,
    )
    incident = [
        index for index, edge in enumerate(model.graph.edges) if 0 in edge
    ]
    before_bridge = propagate_selected_branch(
        model,
        states["generic"],
        incident[:2],
        (1, -1),
        (0.13, 0.29),
    )
    defect_residual = 0.0
    norm_margin = 0.0
    fibres = 0
    for branch, edge_index in ((initial, incident[0]), (before_bridge, incident[2])):
        current_residual, current_margin, current_fibres = event_defect_residual(
            model, branch, edge_index
        )
        defect_residual = max(defect_residual, current_residual)
        norm_margin = max(norm_margin, current_margin)
        fibres += current_fibres

    first_edge, second_edge = incident[:2]
    h_in = model.physical_hamiltonian(model.graph.full_mask)
    h_middle = h_in - model.physical_hops[first_edge]
    h_out = h_middle - model.physical_hops[second_edge]
    telescope_residual = 0.0
    for tau in (0.0, 0.17, -0.43, 0.71):
        input_state = initial.physical
        first_pre = evolve_physical(h_in, input_state, -tau)
        for first_outcome in (1, -1):
            first_projected = physical_record_projection(
                model, first_pre, first_edge, first_outcome
            )
            first_lifted = evolve_physical(h_middle, first_projected, tau)
            second_pre = evolve_physical(h_middle, first_lifted, -tau)
            for second_outcome in (1, -1):
                sequential = evolve_physical(
                    h_out,
                    physical_record_projection(
                        model, second_pre, second_edge, second_outcome
                    ),
                    tau,
                )
                direct_endpoint_input = evolve_physical(h_in, input_state, -tau)
                direct_ideal = physical_record_projection(
                    model,
                    physical_record_projection(
                        model, direct_endpoint_input, first_edge, first_outcome
                    ),
                    second_edge,
                    second_outcome,
                )
                direct = evolve_physical(h_out, direct_ideal, tau)
                telescope_residual = max(
                    telescope_residual, float(np.linalg.norm(sequential - direct))
                )
                fibres += 1

    hopping_bound = model.graph.hopping_bound
    edge_count = len(model.graph.edges)
    history_norm_bound = hopping_bound * edge_count
    width = hopping_bound
    initial_low = 2.0 * history_norm_bound
    initial_high = initial_low + width
    cap_low = 0.0
    cap_high = 4.0 * history_norm_bound + width
    reachable_low = initial_low - 2.0 * history_norm_bound
    reachable_high = initial_high + 2.0 * history_norm_bound
    nodes, weights = np.polynomial.legendre.leggauss(64)
    energies = initial_low + 0.5 * width * (nodes + 1.0)
    quadrature_weights = 0.5 * width * weights
    sine_density = (2.0 / width) * np.sin(
        math.pi * (energies - initial_low) / width
    ) ** 2
    sine_norm = float(np.dot(quadrature_weights, sine_density))
    sine_mean = float(np.dot(quadrature_weights, sine_density * energies))
    support_residual = max(
        max(0.0, cap_low - reachable_low),
        max(0.0, reachable_high - cap_high),
        abs((initial_low + initial_high) / 2.0 - (2.0 * history_norm_bound + width / 2.0)),
        abs(sine_norm - 1.0),
        abs(sine_mean - (2.0 * history_norm_bound + width / 2.0)),
    )
    return ApparatusIdentityMetrics(
        defect_residual,
        norm_margin,
        telescope_residual,
        support_residual,
        fibres,
    )


def domain_guard_count() -> int:
    bad_calls = [
        lambda: graph_from_edges(3, ((0, 0), (1, 2))),
        lambda: graph_from_edges(3, ((0, 1), (1, 0), (1, 2))),
        lambda: graph_from_edges(4, ((0, 1), (2, 3))),
        lambda: Graph(
            2,
            ((0, 1),),
            (2.0,),
            ((1,), (0,)),
            None,
            1.0,
        ),
        lambda: tree_edge_solution(graph_from_edges(2, ((0, 1),)), 1),
        lambda: open_cubic_one_particle(3),
    ]
    caught = 0
    for bad_call in bad_calls:
        try:
            bad_call()
        except ValueError:
            caught += 1
    return caught


def main() -> None:
    started = time.perf_counter()
    checks = CheckBook()
    try:
        guard_count = domain_guard_count()
        checks.check(
            "G0 domains and identity",
            guard_count == 6,
            f"source={source_identity()[:16]} guards={guard_count}/6 even_global_parity_only",
        )

        graph = make_open_cube()
        bksf = BKSF(graph)
        algebra = full_algebra_and_placement(graph, bksf)
        checks.check(
            "G1 Pauli algebra and physical placement",
            algebra.residual <= TOL
            and algebra.separate_word_commutator > 0.0
            and algebra.max_support <= 5
            and algebra.max_radius <= 2
            and algebra.max_diameter <= 4
            and algebra.distinct_edge_sites == 12,
            (
                f"res={algebra.residual:.2e} separate_word_comm={algebra.separate_word_commutator:.2f} "
                f"support/radius/diameter={algebra.max_support}/{algebra.max_radius}/{algebra.max_diameter}"
            ),
        )

        census = exhaustive_cube_census(graph, bksf)
        checks.check(
            "G2 complete mask-edge census",
            census.masks == 4096
            and census.pairs == 24576
            and census.bridges + census.nonbridges == census.pairs
            and census.split_nontrivial > 0
            and census.max_rank_error == 0
            and census.algebra_residual <= TOL
            and census.impossible_fixed_number_cases > 0,
            (
                f"masks={census.masks} pairs={census.pairs} bridge/non={census.bridges}/{census.nonbridges} "
                f"fixedN={census.fixed_number_cases} impossible={census.impossible_fixed_number_cases}"
            ),
        )

        model = build_cube_model()
        hopping_residual = max(
            float(np.max(np.abs(model.car.T[index] - model.car.explicit_hop(*edge))))
            for index, edge in enumerate(graph.edges)
        )
        code_residual = max(
            model.code.phase_consistency,
            model.code.generator_residual,
            model.code.loop_residual,
            model.code.six_cycle_residual,
            hopping_residual,
        )
        checks.check(
            "G3 faithful physical-to-CAR dictionary",
            model.code.isometry.shape == (4096, 128) and code_residual <= TOL,
            f"shape=4096x128 all_A/B/T_res={code_residual:.2e} includes_length6_phase",
        )

        histories = history_suite(model)
        checks.check(
            "G4 no-reset native Record histories",
            histories.histories == 6
            and histories.nonzero_branches > 0
            and histories.zero_outcomes > 0
            and histories.deterministic_outcomes > 0
            and histories.bridge_events > 0
            and histories.nonbridge_events > 0
            and histories.maximum_residual <= TOL,
            (
                f"histories={histories.histories} final_branches={histories.nonzero_branches} "
                f"zero/deterministic={histories.zero_outcomes}/{histories.deterministic_outcomes} "
                f"split=4+4 max_res={histories.maximum_residual:.2e}"
            ),
        )

        uniform = actual_uniform_edge_probe(model)
        checks.check(
            "G5 actual uniform-live-edge moments",
            uniform.states == 2
            and uniform.max_residual <= TOL
            and uniform.largest_variance_increment <= 1.0 + TOL
            and uniform.largest_local_square <= 1.0 + TOL,
            (
                f"states={uniform.states} max_res={uniform.max_residual:.2e} "
                f"max_dVar={uniform.largest_variance_increment:.6f} max_<h_e2>={uniform.largest_local_square:.6f}"
            ),
        )

        bulk = bulk_energy_checks(model)
        bulk_residual = max(
            bulk.max_spectral_residual,
            bulk.max_trace_residual,
            bulk.max_norm_margin,
        )
        checks.check(
            "G6 finite open-box sea and tail arithmetic",
            bulk_residual <= TOL
            and bulk.cube_energy < -4.0
            and bulk.ell4_energy_density < -0.375
            and abs(bulk.ell4_quarter_tail_bound - 1.0 / 9.0) <= TOL,
            (
                f"cube_E0={bulk.cube_energy:.12f} ell4_E0/M={bulk.ell4_energy_density:.9f} "
                f"trace/pair/norm_res={bulk_residual:.2e} ell4_K=L/4_tail={bulk.ell4_quarter_tail_bound:.6f}"
            ),
        )

        apparatus = apparatus_operator_identities(model)
        apparatus_residual = max(
            apparatus.defect_residual,
            apparatus.defect_norm_margin,
            apparatus.telescope_residual,
            apparatus.support_residual,
        )
        checks.check(
            "G7 apparatus operator identities",
            apparatus_residual <= TOL and apparatus.tested_fibres >= 20,
            (
                f"fibres={apparatus.tested_fibres} defect/telescope/support_res="
                f"{apparatus.defect_residual:.2e}/{apparatus.telescope_residual:.2e}/"
                f"{apparatus.support_residual:.2e} actual_battery_fixture=checker_scope"
            ),
        )

        elapsed = time.perf_counter() - started
        rss = peak_rss_mib()
        checks.check(
            "G8 execution envelope",
            elapsed < AUDIT_TIMEOUT_SEC and rss < 180.0,
            f"elapsed={elapsed:.2f}s peak_rss={rss:.1f}MiB timeout={AUDIT_TIMEOUT_SEC}s",
        )
    except Exception as error:  # keep the final machine summary on unexpected faults
        checks.check("INTERNAL", False, f"{type(error).__name__}: {error}")
    checks.finish()


if __name__ == "__main__":
    main()
