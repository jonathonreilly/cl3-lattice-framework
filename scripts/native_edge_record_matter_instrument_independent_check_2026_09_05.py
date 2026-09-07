#!/usr/bin/env python3
"""Independent finite checks for the native physical-edge Record instrument.

This checker uses dense edge-Pauli matrices only for graphs with at most six
edges and direct occupation-sign fermion matrices for four modes.  It is an
independent same-model-family check and does not import another scientific
runner.
"""

from __future__ import annotations

import os

for _thread_variable in (
    "OPENBLAS_NUM_THREADS",
    "OMP_NUM_THREADS",
    "MKL_NUM_THREADS",
    "VECLIB_MAXIMUM_THREADS",
    "NUMEXPR_NUM_THREADS",
):
    os.environ[_thread_variable] = "1"

import ast
import hashlib
import math
import pathlib
import sys
from dataclasses import dataclass

import numpy as np
import scipy.linalg


AUDIT_TIMEOUT_SEC = 180
DENSE_MATRIX_AXIS_LIMIT = 600
ATOL = 3.0e-10
RANK_TOL = 2.0e-9
SOURCE_INTEGRITY_SHA256 = "03abb51917e8830210de90f2021ed2cb2baec9230e28f3b35221ea2358d39e77"
EXPECTED_CHECK_NAMES = (
    "direct_dictionary",
    "nonbridge_instrument",
    "bridge_and_history",
    "uniform_history_moments",
    "bipartite_energy_bound",
    "placement_and_support",
    "shared_battery_native_history",
    "fibre_moment_identity",
    "source_contract",
)

I2 = np.eye(2, dtype=complex)
X2 = np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex)
Z2 = np.diag([1.0, -1.0]).astype(complex)


class CheckFailure(AssertionError):
    """A scientific or source-contract check failed."""


def require(condition: bool, message: str) -> None:
    if not condition:
        raise CheckFailure(message)


def max_abs(value: np.ndarray) -> float:
    return float(np.max(np.abs(value))) if value.size else 0.0


def close(left: np.ndarray, right: np.ndarray, message: str, tol: float = ATOL) -> None:
    error = max_abs(np.asarray(left) - np.asarray(right))
    require(error <= tol, f"{message}: residual={error:.3e}")


def matrix_rank(matrix: np.ndarray, tol: float = RANK_TOL) -> int:
    return int(np.linalg.matrix_rank(matrix, tol=tol))


def pauli_word(edge_count: int, operators: dict[int, np.ndarray]) -> np.ndarray:
    require(2**edge_count <= DENSE_MATRIX_AXIS_LIMIT, "dense Pauli matrix too large")
    result = np.ones((1, 1), dtype=complex)
    for edge_index in range(edge_count):
        result = np.kron(result, operators.get(edge_index, I2))
    return result


@dataclass(frozen=True)
class SmallGraph:
    vertex_count: int
    edges: tuple[tuple[int, int], ...]

    def __post_init__(self) -> None:
        normalized = tuple(tuple(sorted(edge)) for edge in self.edges)
        require(normalized == self.edges, "edges must be stored in canonical orientation")
        require(len(set(normalized)) == len(normalized), "graph has a repeated edge")
        require(all(i != j for i, j in normalized), "graph has a loop")

    @property
    def edge_count(self) -> int:
        return len(self.edges)

    @property
    def dimension(self) -> int:
        return 2**self.edge_count

    def edge_index(self, i: int, j: int) -> int:
        return self.edges.index(tuple(sorted((i, j))))

    def neighbors(self, vertex: int) -> tuple[int, ...]:
        values = []
        for i, j in self.edges:
            if i == vertex:
                values.append(j)
            elif j == vertex:
                values.append(i)
        return tuple(sorted(values))

    def vertex_parity(self, vertex: int) -> np.ndarray:
        operators = {
            self.edge_index(vertex, neighbor): Z2
            for neighbor in self.neighbors(vertex)
        }
        return pauli_word(self.edge_count, operators)

    def edge_generator(self, i: int, j: int) -> np.ndarray:
        edge_position = self.edge_index(i, j)
        operators: dict[int, np.ndarray] = {edge_position: X2}
        for neighbor in self.neighbors(i):
            if neighbor < j:
                operators[self.edge_index(i, neighbor)] = Z2
        for neighbor in self.neighbors(j):
            if neighbor < i:
                operators[self.edge_index(j, neighbor)] = Z2
        orientation = 1.0 if i < j else -1.0
        return orientation * pauli_word(self.edge_count, operators)

    def hopping_generator(self, edge: tuple[int, int]) -> np.ndarray:
        i, j = edge
        a_ij = self.edge_generator(i, j)
        return 0.5j * a_ij @ (self.vertex_parity(i) - self.vertex_parity(j))

    def edge_z(self, edge: tuple[int, int]) -> np.ndarray:
        return pauli_word(self.edge_count, {self.edge_index(*edge): Z2})

    def cycle_stabilizer(self, oriented_vertices: tuple[int, ...]) -> np.ndarray:
        require(oriented_vertices[0] == oriented_vertices[-1], "cycle must be closed")
        length = len(oriented_vertices) - 1
        result = (1j**length) * np.eye(self.dimension, dtype=complex)
        for i, j in zip(oriented_vertices[:-1], oriented_vertices[1:]):
            result = result @ self.edge_generator(i, j)
        return result


@dataclass(frozen=True)
class FockCarrier:
    mode_count: int
    masks: tuple[int, ...]
    annihilators_full: tuple[np.ndarray, ...]
    vertex_parities: tuple[np.ndarray, ...]
    edge_generators: dict[tuple[int, int], np.ndarray]
    hoppings: dict[tuple[int, int], np.ndarray]
    number: np.ndarray


@dataclass(frozen=True)
class WeightedHistory:
    live_edges: tuple[tuple[int, int], ...]
    records: tuple[tuple[tuple[int, int], int], ...]
    density: np.ndarray


def direct_even_fock(mode_count: int) -> FockCarrier:
    full_dimension = 2**mode_count
    annihilators = []
    for mode in range(mode_count):
        operator = np.zeros((full_dimension, full_dimension), dtype=complex)
        lower_mask = (1 << mode) - 1
        for mask in range(full_dimension):
            if (mask >> mode) & 1:
                sign = -1.0 if (mask & lower_mask).bit_count() % 2 else 1.0
                operator[mask ^ (1 << mode), mask] = sign
        annihilators.append(operator)
    masks = tuple(mask for mask in range(full_dimension) if mask.bit_count() % 2 == 0)
    selector = np.ix_(masks, masks)
    identity = np.eye(full_dimension, dtype=complex)
    majoranas = [operator + operator.conj().T for operator in annihilators]
    vertex_parities = []
    for operator in annihilators:
        parity = identity - 2.0 * operator.conj().T @ operator
        vertex_parities.append(parity[selector])
    edge_generators: dict[tuple[int, int], np.ndarray] = {}
    hoppings: dict[tuple[int, int], np.ndarray] = {}
    for i in range(mode_count):
        for j in range(i + 1, mode_count):
            edge = (i, j)
            a_ij = -1j * majoranas[i] @ majoranas[j]
            edge_generators[edge] = a_ij[selector]
            direct_hop = (
                annihilators[i].conj().T @ annihilators[j]
                + annihilators[j].conj().T @ annihilators[i]
            )
            hoppings[edge] = direct_hop[selector]
    number_values = np.array([mask.bit_count() for mask in masks], dtype=float)
    return FockCarrier(
        mode_count=mode_count,
        masks=masks,
        annihilators_full=tuple(annihilators),
        vertex_parities=tuple(vertex_parities),
        edge_generators=edge_generators,
        hoppings=hoppings,
        number=np.diag(number_values).astype(complex),
    )


def code_isometry(
    graph: SmallGraph,
    fock: FockCarrier,
    cycles: tuple[tuple[int, ...], ...],
) -> np.ndarray:
    physical_dimension = graph.dimension
    fock_dimension = len(fock.masks)
    physical_identity = np.eye(physical_dimension, dtype=complex)
    fock_identity = np.eye(fock_dimension, dtype=complex)
    constraints = []
    for vertex in range(graph.vertex_count):
        constraints.append(
            np.kron(fock_identity, graph.vertex_parity(vertex))
            - np.kron(fock.vertex_parities[vertex].T, physical_identity)
        )
    for edge in graph.edges:
        constraints.append(
            np.kron(fock_identity, graph.edge_generator(*edge))
            - np.kron(fock.edge_generators[edge].T, physical_identity)
        )
    for cycle in cycles:
        stabilizer = graph.cycle_stabilizer(cycle)
        constraints.append(np.kron(fock_identity, stabilizer - physical_identity))
    constraint_matrix = np.vstack(constraints)
    null_basis = scipy.linalg.null_space(constraint_matrix, rcond=1.0e-11)
    require(null_basis.shape[1] == 1, f"intertwiner nullity is {null_basis.shape[1]}")
    isometry = null_basis[:, 0].reshape((physical_dimension, fock_dimension), order="F")
    gram = isometry.conj().T @ isometry
    eigenvalues, eigenvectors = np.linalg.eigh(gram)
    require(float(np.min(eigenvalues)) > 1.0e-10, "intertwiner has deficient rank")
    inverse_root = eigenvectors @ np.diag(eigenvalues**-0.5) @ eigenvectors.conj().T
    isometry = isometry @ inverse_root
    close(isometry.conj().T @ isometry, fock_identity, "intertwiner isometry")
    return isometry


def commutant_nullity(generators: list[np.ndarray]) -> int:
    dimension = generators[0].shape[0]
    identity = np.eye(dimension, dtype=complex)
    constraints = [
        np.kron(identity, generator) - np.kron(generator.T, identity)
        for generator in generators
    ]
    singular_values = np.linalg.svd(np.vstack(constraints), compute_uv=False)
    return int(np.count_nonzero(singular_values <= RANK_TOL))


def normalized(vector: np.ndarray) -> np.ndarray:
    norm = float(np.linalg.norm(vector))
    require(norm > 1.0e-14, "cannot normalize a zero vector")
    return vector / norm


def fixed_number_vector(fock: FockCarrier, particle_number: int) -> np.ndarray:
    vector = np.zeros(len(fock.masks), dtype=complex)
    rng = np.random.default_rng(20260905 + particle_number)
    for position, mask in enumerate(fock.masks):
        if mask.bit_count() == particle_number:
            vector[position] = rng.normal() + 1j * rng.normal()
    return normalized(vector)


def projector_from_involution(involution: np.ndarray, sign: int) -> np.ndarray:
    require(sign in (-1, 1), "projector sign must be plus or minus one")
    return 0.5 * (np.eye(involution.shape[0], dtype=complex) + sign * involution)


def range_basis(projector: np.ndarray) -> np.ndarray:
    eigenvalues, eigenvectors = np.linalg.eigh(projector)
    basis = eigenvectors[:, eigenvalues > 0.5]
    close(basis.conj().T @ basis, np.eye(basis.shape[1]), "range basis")
    return basis


def physical_number(graph: SmallGraph) -> np.ndarray:
    identity = np.eye(graph.dimension, dtype=complex)
    return sum(
        (identity - graph.vertex_parity(vertex)) / 2.0
        for vertex in range(graph.vertex_count)
    )


def basis_vector(fock: FockCarrier, mask: int) -> np.ndarray:
    vector = np.zeros(len(fock.masks), dtype=complex)
    vector[fock.masks.index(mask)] = 1.0
    return vector


def restricted_generators(
    fock: FockCarrier,
    edges: tuple[tuple[int, int], ...],
    subspace: np.ndarray,
) -> list[np.ndarray]:
    generators = list(fock.vertex_parities) + [fock.edge_generators[edge] for edge in edges]
    return [subspace.conj().T @ generator @ subspace for generator in generators]


def direct_dictionary_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    path = SmallGraph(4, ((0, 1), (1, 2), (2, 3)))
    fock = direct_even_fock(4)
    square_cycle = (0, 1, 2, 3, 0)
    square_stabilizer = square.cycle_stabilizer(square_cycle)
    close(square_stabilizer, square_stabilizer.conj().T, "square stabilizer Hermiticity")
    close(square_stabilizer @ square_stabilizer, np.eye(16), "square stabilizer square")
    require(matrix_rank(projector_from_involution(square_stabilizer, 1)) == 8, "square code rank")
    square_isometry = code_isometry(square, fock, (square_cycle,))
    path_isometry = code_isometry(path, fock, ())
    for graph, isometry in ((square, square_isometry), (path, path_isometry)):
        global_parity = np.eye(graph.dimension, dtype=complex)
        for vertex in range(4):
            physical_b = graph.vertex_parity(vertex)
            close(physical_b, physical_b.conj().T, f"B Hermiticity vertex={vertex}")
            close(physical_b @ physical_b, np.eye(graph.dimension), f"B square vertex={vertex}")
            global_parity = global_parity @ physical_b
            close(
                physical_b @ isometry,
                isometry @ fock.vertex_parities[vertex],
                f"B dictionary graph_edges={graph.edge_count} vertex={vertex}",
            )
        close(global_parity, np.eye(graph.dimension), "unaugmented carrier has even global parity")
        for edge in graph.edges:
            physical_a = graph.edge_generator(*edge)
            physical_t = graph.hopping_generator(edge)
            fock_a = fock.edge_generators[edge]
            fock_t_from_dictionary = (
                0.5j
                * fock_a
                @ (fock.vertex_parities[edge[0]] - fock.vertex_parities[edge[1]])
            )
            close(physical_a, physical_a.conj().T, f"A Hermiticity edge={edge}")
            close(physical_a @ physical_a, np.eye(graph.dimension), f"A square edge={edge}")
            close(physical_t, physical_t.conj().T, f"T Hermiticity edge={edge}")
            close(physical_a @ isometry, isometry @ fock_a, f"A dictionary edge={edge}")
            close(fock_t_from_dictionary, fock.hoppings[edge], f"direct CAR hopping edge={edge}")
            close(physical_t @ isometry, isometry @ fock.hoppings[edge], f"T dictionary edge={edge}")
            i, j = edge
            expected_square = 0.5 * (
                np.eye(graph.dimension) - graph.vertex_parity(i) @ graph.vertex_parity(j)
            )
            close(physical_t @ physical_t, expected_square, f"T square edge={edge}")
    generators = list(fock.vertex_parities) + [fock.edge_generators[e] for e in path.edges]
    require(commutant_nullity(generators) == 1, "connected-tree surviving algebra is not full")

    ring6 = SmallGraph(6, ((0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (0, 5)))
    oriented6 = (0, 1, 2, 3, 4, 5, 0)
    stabilizer6 = ring6.cycle_stabilizer(oriented6)
    close(stabilizer6, stabilizer6.conj().T, "length-six stabilizer Hermiticity")
    close(stabilizer6 @ stabilizer6, np.eye(64), "length-six stabilizer square")
    require(matrix_rank(projector_from_involution(stabilizer6, 1)) == 32, "length-six code rank")
    wrong_last_orientation = (-1.0) * stabilizer6
    direct_wrong = (1j**6) * np.eye(64, dtype=complex)
    for i, j in zip(oriented6[:-2], oriented6[1:-1]):
        direct_wrong = direct_wrong @ ring6.edge_generator(i, j)
    direct_wrong = direct_wrong @ ring6.edge_generator(0, 5)
    close(direct_wrong, wrong_last_orientation, "negative closing orientation is load-bearing")
    return "square/path dictionaries, full tree algebra, and length-6 phase verified"


def nonbridge_instrument_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    fock = direct_even_fock(4)
    cycle = (0, 1, 2, 3, 0)
    stabilizer = square.cycle_stabilizer(cycle)
    code_projector = projector_from_involution(stabilizer, 1)
    isometry = code_isometry(square, fock, (cycle,))
    recorded_edge = (0, 3)
    record_z = square.edge_z(recorded_edge)
    close(stabilizer @ record_z, -record_z @ stabilizer, "nonbridge cycle anticommutation")
    close(
        code_projector @ record_z @ code_projector,
        np.zeros_like(code_projector),
        "compressed nonbridge Z vanishes",
    )
    state = fixed_number_vector(fock, 2)
    physical_state = isometry @ state
    surviving_edges = tuple(edge for edge in square.edges if edge != recorded_edge)
    fock_generators = list(fock.vertex_parities) + [
        fock.edge_generators[edge] for edge in surviving_edges
    ]
    require(commutant_nullity(fock_generators) == 1, "nonbridge surviving algebra commutant")
    branch_states = []
    branch_projectors = []
    for sign in (-1, 1):
        projector = projector_from_involution(record_z, sign)
        close(projector, projector.conj().T, f"native Q Hermiticity sign={sign}")
        close(projector @ projector, projector, f"native Q idempotence sign={sign}")
        branch_projectors.append(projector)
        branch_map = math.sqrt(2.0) * projector @ isometry
        close(branch_map.conj().T @ branch_map, np.eye(8), f"nonbridge J_{sign} isometry")
        require(matrix_rank(projector) == 8, f"updated nonbridge code rank sign={sign}")
        probability = float(np.vdot(physical_state, projector @ physical_state).real)
        require(abs(probability - 0.5) <= ATOL, f"nonbridge probability sign={sign}")
        for vertex in range(4):
            close(
                square.vertex_parity(vertex) @ branch_map,
                branch_map @ fock.vertex_parities[vertex],
                f"nonbridge surviving B vertex={vertex} sign={sign}",
            )
        for edge in surviving_edges:
            close(
                square.edge_generator(*edge) @ branch_map,
                branch_map @ fock.edge_generators[edge],
                f"nonbridge surviving A edge={edge} sign={sign}",
            )
        branch_state = branch_map @ state
        close(record_z @ branch_state, sign * branch_state, f"sharp nonbridge Record {sign}")
        branch_states.append(branch_state)
    close(branch_projectors[0] + branch_projectors[1], np.eye(16), "native Q normalization")
    close(branch_projectors[0] @ branch_projectors[1], np.zeros((16, 16)), "native Q orthogonality")
    require(abs(np.vdot(branch_states[0], branch_states[1])) <= ATOL, "raw branches not orthogonal")
    return "fair physical Z branches and faithful full surviving CAR algebra verified"


def bridge_and_history_check() -> str:
    fock = direct_even_fock(4)
    path = SmallGraph(4, ((0, 1), (1, 2), (2, 3)))
    path_isometry = code_isometry(path, fock, ())
    number = physical_number(path)
    close(number @ path_isometry, path_isometry @ fock.number, "path original number dictionary")
    for edge in path.edges:
        close(
            number @ path.hopping_generator(edge),
            path.hopping_generator(edge) @ number,
            f"full physical number conservation edge={edge}",
        )

    central_z = path.edge_z((1, 2))
    central_parity = fock.vertex_parities[0] @ fock.vertex_parities[1]
    leaf_z = path.edge_z((0, 1))
    leaf_parity = fock.vertex_parities[0]
    close(central_z @ path_isometry, path_isometry @ central_parity, "bridge 2+2 identity")
    close(leaf_z @ path_isometry, path_isometry @ leaf_parity, "bridge 1+3 identity")
    number_two = np.diag([float(mask.bit_count() == 2) for mask in fock.masks]).astype(complex)
    expected_central_dimensions = {-1: 4, 1: 2}
    for record_z, parity, label, expected_dimensions in (
        (central_z, central_parity, "2+2", expected_central_dimensions),
        (leaf_z, leaf_parity, "1+3", {-1: 3, 1: 3}),
    ):
        for sign in (-1, 1):
            physical_projector = projector_from_involution(record_z, sign)
            parity_projector = projector_from_involution(parity, sign)
            close(
                physical_projector @ path_isometry,
                path_isometry @ parity_projector,
                f"bridge conditional map {label} sign={sign}",
            )
            require(matrix_rank(physical_projector) == 4, f"bridge code rank {label} sign={sign}")
            fixed_dimension = matrix_rank(number_two @ parity_projector)
            require(
                fixed_dimension == expected_dimensions[sign],
                f"fixed-N bridge dimension {label} sign={sign}: {fixed_dimension}",
            )

    even_left = basis_vector(fock, 0b0011)
    odd_left = basis_vector(fock, 0b0101)
    for state, certain_sign in ((even_left, 1), (odd_left, -1)):
        physical_state = path_isometry @ state
        certain = float(
            np.vdot(physical_state, projector_from_involution(central_z, certain_sign) @ physical_state).real
        )
        impossible = float(
            np.vdot(physical_state, projector_from_involution(central_z, -certain_sign) @ physical_state).real
        )
        require(abs(certain - 1.0) <= ATOL and abs(impossible) <= ATOL, "deterministic/zero bridge outcome")

    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    cycle = (0, 1, 2, 3, 0)
    square_isometry = code_isometry(square, fock, (cycle,))
    old_edge = (0, 3)
    new_edge = (1, 2)
    old_z_operator = square.edge_z(old_edge)
    new_z_operator = square.edge_z(new_edge)
    component_parity = fock.vertex_parities[0] @ fock.vertex_parities[1]
    state = fixed_number_vector(fock, 2)
    nonzero_joint_probabilities = []
    for old_sign in (-1, 1):
        old_projector = projector_from_involution(old_z_operator, old_sign)
        require(matrix_rank(old_projector) == 8, "first nonbridge history rank")
        close(
            (new_z_operator - old_sign * square.vertex_parity(0) @ square.vertex_parity(1))
            @ old_projector
            @ square_isometry,
            np.zeros((16, 8), dtype=complex),
            f"old-boundary bridge sign old={old_sign}",
        )
        for new_sign in (-1, 1):
            new_projector = projector_from_involution(new_z_operator, new_sign)
            parity_sign = new_sign * old_sign
            parity_projector = projector_from_involution(component_parity, parity_sign)
            history_map = new_projector @ old_projector @ square_isometry
            close(
                history_map,
                old_projector @ square_isometry @ parity_projector,
                f"two-event signed parity old={old_sign} new={new_sign}",
            )
            require(matrix_rank(history_map) == 4, "bridge history code rank")
            close(
                old_z_operator @ history_map,
                old_sign * history_map,
                "old Record permanence",
            )
            probability = float(np.linalg.norm(history_map @ state) ** 2)
            require(probability > 1.0e-4, "generic history unexpectedly has zero probability")
            nonzero_joint_probabilities.append(probability)
            parity_basis = range_basis(parity_projector)
            faithful_map = math.sqrt(2.0) * history_map @ parity_basis
            close(
                faithful_map.conj().T @ faithful_map,
                np.eye(4),
                "history faithful isometry",
            )
            surviving = ((0, 1), (2, 3))
            restricted = restricted_generators(fock, surviving, parity_basis)
            require(commutant_nullity(restricted) == 1, "split surviving algebra not full on branch")
            physical_generators = [square.vertex_parity(v) for v in range(4)] + [
                square.edge_generator(*edge) for edge in surviving
            ]
            fock_generators = list(fock.vertex_parities) + [
                fock.edge_generators[edge] for edge in surviving
            ]
            for physical_generator, fock_generator in zip(physical_generators, fock_generators):
                close(
                    physical_generator @ faithful_map,
                    faithful_map @ (parity_basis.conj().T @ fock_generator @ parity_basis),
                    "two-event full surviving generator",
                )
    require(abs(sum(nonzero_joint_probabilities) - 1.0) <= ATOL, "joint history normalization")
    return "2+2, 1+3, deterministic, zero, and signed old-boundary branches verified"


def history_hamiltonian(
    live_edges: tuple[tuple[int, int], ...],
    terms: dict[tuple[int, int], np.ndarray],
) -> np.ndarray:
    dimension = next(iter(terms.values())).shape[0]
    result = np.zeros((dimension, dimension), dtype=complex)
    for edge in live_edges:
        result = result + terms[edge]
    return result


def history_statistics(
    histories: list[WeightedHistory],
    terms: dict[tuple[int, int], np.ndarray],
    number: np.ndarray,
    sharp_number: int,
    edge_z: dict[tuple[int, int], np.ndarray],
) -> tuple[float, float, float, float]:
    weight = 0.0
    mean = 0.0
    second = 0.0
    number_residual = 0.0
    identity = np.eye(number.shape[0], dtype=complex)
    for history in histories:
        rho = history.density
        hamiltonian = history_hamiltonian(history.live_edges, terms)
        branch_weight = float(np.trace(rho).real)
        weight += branch_weight
        mean += float(np.trace(rho @ hamiltonian).real)
        second += float(np.trace(rho @ hamiltonian @ hamiltonian).real)
        number_residual += float(
            np.trace(rho @ (number - sharp_number * identity) @ (number - sharp_number * identity)).real
        )
        for edge, sign in history.records:
            record_residual = float(
                np.trace(rho @ (edge_z[edge] - sign * identity) @ (edge_z[edge] - sign * identity)).real
            )
            require(abs(record_residual) <= 2.0e-9, f"old Record lost edge={edge} sign={sign}")
    return weight, mean, second, number_residual


def dwell_time(records: tuple[tuple[tuple[int, int], int], ...], edge_order: dict[tuple[int, int], int]) -> float:
    signed_history = sum((edge_order[edge] + 1) * sign for edge, sign in records)
    return 0.061 * (len(records) + 1) + 0.007 * signed_history


def uniform_history_moments_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    fock = direct_even_fock(4)
    cycle = (0, 1, 2, 3, 0)
    isometry = code_isometry(square, fock, (cycle,))
    coefficients = {
        (0, 1): 0.83,
        (1, 2): -0.61,
        (2, 3): 1.0,
        (0, 3): -0.74,
    }
    terms = {
        edge: coefficients[edge] * square.hopping_generator(edge)
        for edge in square.edges
    }
    edge_z = {edge: square.edge_z(edge) for edge in square.edges}
    number = physical_number(square)
    state = isometry @ fixed_number_vector(fock, 2)
    initial_density = np.outer(state, state.conj())
    histories = [WeightedHistory(square.edges, (), initial_density)]
    edge_order = {edge: position for position, edge in enumerate(square.edges)}
    initial_hamiltonian = history_hamiltonian(square.edges, terms)
    initial_mean = float(np.vdot(state, initial_hamiltonian @ state).real)
    previous_second = float(np.vdot(state, initial_hamiltonian @ initial_hamiltonian @ state).real)
    previous_variance = previous_second - initial_mean**2
    largest_coefficient = max(abs(value) for value in coefficients.values())
    observed_branch_counts = []

    for event_index in range(square.edge_count + 1):
        weight, mean, second, number_residual = history_statistics(
            histories, terms, number, 2, edge_z
        )
        require(abs(weight - 1.0) <= 3.0e-9, f"history normalization event={event_index}")
        require(abs(number_residual) <= 3.0e-9, f"sharp N lost event={event_index}")
        target_mean = initial_mean * (square.edge_count - event_index) / square.edge_count
        require(abs(mean - target_mean) <= 5.0e-9, f"uniform mean law event={event_index}")
        variance = second - mean**2
        require(
            variance <= previous_variance + event_index * largest_coefficient**2 + 3.0e-9,
            f"variance accumulation bound event={event_index}",
        )
        observed_branch_counts.append(len(histories))
        if event_index == square.edge_count:
            require(abs(second) <= ATOL, "q=0 final Hamiltonian is not zero")
            break

        q = square.edge_count - event_index
        next_histories: list[WeightedHistory] = []
        correction = 0.0
        for history in histories:
            hamiltonian = history_hamiltonian(history.live_edges, terms)
            tau = dwell_time(history.records, edge_order)
            unitary = scipy.linalg.expm(-1j * tau * hamiltonian)
            dwelled = unitary @ history.density @ unitary.conj().T
            require(len(history.live_edges) == q, "live-edge count is history dependent")
            average_square = np.zeros_like(hamiltonian)
            for edge in history.live_edges:
                output_hamiltonian = hamiltonian - terms[edge]
                average_square = average_square + output_hamiltonian @ output_hamiltonian / q
                correction += float(np.trace(dwelled @ terms[edge] @ terms[edge]).real) / q
                for sign in (-1, 1):
                    projector = projector_from_involution(edge_z[edge], sign)
                    close(
                        output_hamiltonian @ projector,
                        projector @ output_hamiltonian,
                        f"outgoing Hamiltonian commutes native Record edge={edge}",
                    )
                    next_density = projector @ dwelled @ projector / q
                    next_live = tuple(candidate for candidate in history.live_edges if candidate != edge)
                    next_records = history.records + ((edge, sign),)
                    next_histories.append(WeightedHistory(next_live, next_records, next_density))
            expected_average_square = (
                (1.0 - 2.0 / q) * hamiltonian @ hamiltonian
                + sum(terms[edge] @ terms[edge] for edge in history.live_edges) / q
            )
            close(average_square, expected_average_square, f"second-moment operator q={q}")

        next_weight, next_mean, next_second, _ = history_statistics(
            next_histories, terms, number, 2, edge_z
        )
        require(abs(next_weight - 1.0) <= 3.0e-9, "weighted outcome sum")
        require(abs(next_mean - (1.0 - 1.0 / q) * mean) <= 5.0e-9, "actual first-moment recursion")
        predicted_second = (1.0 - 2.0 / q) * second + correction
        require(abs(next_second - predicted_second) <= 6.0e-9, "actual second-moment recursion")
        next_variance = next_second - next_mean**2
        if q >= 2:
            predicted_variance = (1.0 - 2.0 / q) * variance - mean**2 / q**2 + correction
            require(abs(next_variance - predicted_variance) <= 7.0e-9, "actual variance recursion")
            require(next_variance <= variance + largest_coefficient**2 + 3.0e-9, "one-event variance bound")
        else:
            require(abs(next_second) <= ATOL and abs(next_variance) <= ATOL, "q=1 zero output")
        histories = next_histories

    first_dwell = scipy.linalg.expm(-1j * dwell_time((), edge_order) * initial_hamiltonian)
    first_density = first_dwell @ initial_density @ first_dwell.conj().T
    uniform_candidate = sum(
        float(np.trace(first_density @ (initial_hamiltonian - terms[edge])).real)
        for edge in square.edges
    ) / 4.0
    biased_weights = np.array([abs(coefficients[edge]) for edge in square.edges], dtype=float)
    biased_weights /= np.sum(biased_weights)
    biased_candidate = sum(
        weight * float(np.trace(first_density @ (initial_hamiltonian - terms[edge])).real)
        for weight, edge in zip(biased_weights, square.edges)
    )
    require(abs(uniform_candidate - biased_candidate) > 1.0e-4, "fixture cannot distinguish biased edge choice")
    require(observed_branch_counts == [1, 8, 48, 192, 384], "unexpected history-tree census")
    return "384 actual edge/outcome histories obey uniform mean, second moment, variance, N, and Records"


def bipartite_energy_bound_check() -> str:
    fixtures = (
        (4, ((0, 1), (1, 2), (2, 3), (0, 3)), 2),
        (4, ((0, 1), (1, 2), (2, 3)), 2),
    )
    margins = []
    for vertex_count, edges, max_degree in fixtures:
        one_particle = np.zeros((vertex_count, vertex_count), dtype=float)
        for i, j in edges:
            one_particle[i, j] = 1.0
            one_particle[j, i] = 1.0
        eigenvalues = np.linalg.eigvalsh(one_particle)
        close(eigenvalues, -eigenvalues[::-1], "bipartite spectral pairing")
        require(abs(float(np.trace(one_particle @ one_particle)) - 2.0 * len(edges)) <= ATOL, "trace h^2")
        require(float(np.linalg.norm(one_particle, ord=2)) <= max_degree + ATOL, "row-sum norm bound")
        ground_energy = float(np.sum(eigenvalues[: vertex_count // 2]))
        derived_bound = -len(edges) / max_degree
        require(ground_energy <= derived_bound + ATOL, "general max-degree sea bound")
        margins.append(derived_bound - ground_energy)
    require(min(margins) >= -ATOL, "negative energy-bound margin")
    return "square/path verify E0<=-L t/d from pairing, trace square, and row-sum norm"


def lattice_distance(left: tuple[int, int, int], right: tuple[int, int, int]) -> int:
    return sum(abs(a - b) for a, b in zip(left, right))


def canonical_lattice_edge(
    left: tuple[int, int, int], right: tuple[int, int, int]
) -> tuple[tuple[int, int, int], tuple[int, int, int]]:
    return tuple(sorted((left, right)))  # type: ignore[return-value]


def cubic_star(vertex: tuple[int, int, int]) -> set[tuple[tuple[int, int, int], tuple[int, int, int]]]:
    result = set()
    for axis in range(3):
        for direction in (-1, 1):
            neighbor = list(vertex)
            neighbor[axis] += direction
            result.add(canonical_lattice_edge(vertex, tuple(neighbor)))
    return result


def edge_midpoint_site(
    edge: tuple[tuple[int, int, int], tuple[int, int, int]]
) -> tuple[int, int, int]:
    return tuple(left + right for left, right in zip(edge[0], edge[1]))  # type: ignore[return-value]


def multiply_pauli_labels(left: str, right: str) -> str:
    if left == "I":
        return right
    if right == "I":
        return left
    if left == right:
        return "I"
    return "Y" if {left, right} == {"X", "Z"} else "X" if {left, right} == {"Y", "Z"} else "Z"


def multiply_symbolic_words(
    left: dict[object, str], right: dict[object, str]
) -> dict[object, str]:
    result = dict(left)
    for site, label in right.items():
        product = multiply_pauli_labels(result.get(site, "I"), label)
        if product == "I":
            result.pop(site, None)
        else:
            result[site] = product
    return result


def placement_and_support_check() -> str:
    left = (0, 0, 0)
    right = (1, 0, 0)
    central_edge = canonical_lattice_edge(left, right)
    left_star = cubic_star(left)
    right_star = cubic_star(right)
    endpoint_union = left_star | right_star
    require(len(left_star) == 6 and len(right_star) == 6, "cubic endpoint degree")
    require(left_star & right_star == {central_edge}, "endpoint stars share wrong edges")
    require(len(endpoint_union) == 11, "degree-six endpoint union bound")
    center_site = edge_midpoint_site(central_edge)
    sites = {edge_midpoint_site(edge) for edge in endpoint_union}
    require(len(sites) == 11, "edge roles do not occupy distinct original sites")
    require(max(lattice_distance(site, center_site) for site in sites) == 2, "radius-two support")
    diameter = max(lattice_distance(a, b) for a in sites for b in sites)
    require(diameter == 4, "diameter-four support")

    left_neighbors = sorted(edge[1] if edge[0] == left else edge[0] for edge in left_star)
    right_neighbors = sorted(edge[1] if edge[0] == right else edge[0] for edge in right_star)
    a_word: dict[object, str] = {central_edge: "X"}
    for neighbor in left_neighbors:
        if neighbor < right:
            a_word[canonical_lattice_edge(left, neighbor)] = "Z"
    for neighbor in right_neighbors:
        if neighbor < left:
            a_word[canonical_lattice_edge(right, neighbor)] = "Z"
    left_b = {edge: "Z" for edge in left_star}
    right_b = {edge: "Z" for edge in right_star}
    hopping_words = (
        multiply_symbolic_words(a_word, left_b),
        multiply_symbolic_words(a_word, right_b),
    )
    for word in hopping_words:
        require(set(word) <= endpoint_union, "hopping word escapes endpoint stars")
        require(len(word) <= 11, "hopping word exceeds support bound")
        require(central_edge in word, "hopping word lost its physical edge site")
    require(len({central_edge}) == 1, "native Record projector is not one-site")
    return "cubic placement has 11-site union, radius 2, diameter 4, and one-site Record"


def native_record_isometry(record_z: np.ndarray) -> np.ndarray:
    return np.vstack(
        (
            projector_from_involution(record_z, -1),
            projector_from_involution(record_z, 1),
        )
    )


def next_native_record_isometry(record_z: np.ndarray, old_history_count: int) -> np.ndarray:
    dimension = record_z.shape[0]
    result = np.zeros(
        (2 * old_history_count * dimension, old_history_count * dimension),
        dtype=complex,
    )
    projectors = (
        projector_from_involution(record_z, -1),
        projector_from_involution(record_z, 1),
    )
    for old_history in range(old_history_count):
        input_slice = slice(old_history * dimension, (old_history + 1) * dimension)
        for new_history, projector in enumerate(projectors):
            output_history = 2 * old_history + new_history
            output_slice = slice(output_history * dimension, (output_history + 1) * dimension)
            result[output_slice, input_slice] = projector
    return result


def integer_spectral_projectors(hamiltonian: np.ndarray) -> dict[int, np.ndarray]:
    eigenvalues, eigenvectors = np.linalg.eigh(hamiltonian)
    integers = np.rint(eigenvalues).astype(int)
    require(max_abs(eigenvalues - integers) <= 2.0e-9, "fixture spectrum is not exactly commensurate")
    projectors = {}
    for energy in sorted(set(integers.tolist())):
        vectors = eigenvectors[:, integers == energy]
        projectors[energy] = vectors @ vectors.conj().T
    close(sum(projectors.values()), np.eye(hamiltonian.shape[0]), "spectral resolution")
    return projectors


def capped_integer_shift(battery_dimension: int, shift: int) -> np.ndarray:
    result = np.zeros((battery_dimension, battery_dimension), dtype=complex)
    for source in range(battery_dimension):
        target = source + shift
        if 0 <= target < battery_dimension:
            result[target, source] = 1.0
    return result


def translation_lift(
    input_hamiltonian: np.ndarray,
    output_hamiltonian: np.ndarray,
    instrument: np.ndarray,
    battery_dimension: int,
) -> tuple[np.ndarray, tuple[int, ...]]:
    input_projectors = integer_spectral_projectors(input_hamiltonian)
    output_projectors = integer_spectral_projectors(output_hamiltonian)
    output_dimension, input_dimension = instrument.shape
    require(output_hamiltonian.shape == (output_dimension, output_dimension), "output Hamiltonian shape")
    require(input_hamiltonian.shape == (input_dimension, input_dimension), "input Hamiltonian shape")
    require(
        max(output_dimension * battery_dimension, input_dimension * battery_dimension)
        <= DENSE_MATRIX_AXIS_LIMIT,
        "battery lift exceeds dense-axis contract",
    )
    lifted = np.zeros(
        (output_dimension * battery_dimension, input_dimension * battery_dimension),
        dtype=complex,
    )
    used_shifts = set()
    for output_energy, output_projector in output_projectors.items():
        for input_energy, input_projector in input_projectors.items():
            component = output_projector @ instrument @ input_projector
            if np.linalg.norm(component) <= 2.0e-10:
                continue
            shift = input_energy - output_energy
            used_shifts.add(shift)
            lifted = lifted + np.kron(component, capped_integer_shift(battery_dimension, shift))
    return lifted, tuple(sorted(used_shifts))


def reduced_system_from_vector(
    state: np.ndarray, system_dimension: int, battery_dimension: int
) -> np.ndarray:
    coefficients = state.reshape((system_dimension, battery_dimension))
    return coefficients @ coefficients.conj().T


def reduced_battery_from_vector(
    state: np.ndarray, system_dimension: int, battery_dimension: int
) -> np.ndarray:
    coefficients = state.reshape((system_dimension, battery_dimension))
    return coefficients.T @ coefficients.conj()


def joint_history_energy_probabilities(
    density: np.ndarray,
    history_count: int,
    physical_hamiltonian: np.ndarray,
) -> dict[tuple[int, int], float]:
    dimension = physical_hamiltonian.shape[0]
    energy_projectors = integer_spectral_projectors(physical_hamiltonian)
    probabilities = {}
    for history in range(history_count):
        history_projector = np.zeros((history_count, history_count), dtype=complex)
        history_projector[history, history] = 1.0
        for energy, projector in energy_projectors.items():
            observable = np.kron(history_projector, projector)
            probabilities[(history, energy)] = float(np.trace(density @ observable).real)
    return probabilities


def compare_probability_maps(
    left: dict[tuple[int, int], float],
    right: dict[tuple[int, int], float],
    label: str,
) -> None:
    require(left.keys() == right.keys(), f"{label} probability support")
    for key in left:
        require(abs(left[key] - right[key]) <= 4.0e-9, f"{label} probability {key}")
    require(abs(sum(left.values()) - 1.0) <= 4.0e-9, f"{label} left normalization")
    require(abs(sum(right.values()) - 1.0) <= 4.0e-9, f"{label} right normalization")
    histories = sorted({history for history, _ in left})
    for history in histories:
        left_weight = sum(value for (candidate, _), value in left.items() if candidate == history)
        right_weight = sum(value for (candidate, _), value in right.items() if candidate == history)
        require(abs(left_weight - right_weight) <= 4.0e-9, f"{label} history weight {history}")
        if left_weight > 1.0e-10:
            for key in left:
                if key[0] == history:
                    require(
                        abs(left[key] / left_weight - right[key] / right_weight) <= 5.0e-9,
                        f"{label} conditional energy {key}",
                    )


def shifted_packet(packet: np.ndarray, shift: int) -> np.ndarray:
    return capped_integer_shift(len(packet), shift) @ packet


def phase_averaged_eigenstate_output(
    ideal_density: np.ndarray,
    output_hamiltonian: np.ndarray,
    input_energy: int,
    packet: np.ndarray,
) -> np.ndarray:
    result = np.zeros_like(ideal_density)
    projectors = integer_spectral_projectors(output_hamiltonian)
    shifted = {
        energy: shifted_packet(packet, input_energy - energy)
        for energy in projectors
    }
    for left_energy, left_projector in projectors.items():
        for right_energy, right_projector in projectors.items():
            overlap = np.vdot(shifted[right_energy], shifted[left_energy])
            result = result + overlap * left_projector @ ideal_density @ right_projector
    return result


def fixed_number_eigenvectors(
    fock: FockCarrier,
    hamiltonian: np.ndarray,
    particle_number: int,
) -> tuple[np.ndarray, np.ndarray]:
    positions = [
        position for position, mask in enumerate(fock.masks) if mask.bit_count() == particle_number
    ]
    embedding = np.eye(len(fock.masks), dtype=complex)[:, positions]
    eigenvalues, vectors = np.linalg.eigh(embedding.conj().T @ hamiltonian @ embedding)
    return eigenvalues, embedding @ vectors


def shared_battery_native_history_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    fock = direct_even_fock(4)
    cycle = (0, 1, 2, 3, 0)
    code_isom = code_isometry(square, fock, (cycle,))
    first_edge = (0, 1)
    second_edge = (2, 3)
    first_term = square.hopping_generator(first_edge)
    second_term = square.hopping_generator(second_edge)
    input_hamiltonian = first_term + second_term
    after_first = second_term
    after_second = np.zeros_like(input_hamiltonian)
    first_instrument = native_record_isometry(square.edge_z(first_edge))
    second_instrument = next_native_record_isometry(square.edge_z(second_edge), 2)
    composite_instrument = second_instrument @ first_instrument
    first_output_hamiltonian = np.kron(np.eye(2), after_first)
    second_input_hamiltonian = first_output_hamiltonian
    second_output_hamiltonian = np.kron(np.eye(4), after_second)
    close(first_instrument.conj().T @ first_instrument, np.eye(16), "first native isometry")
    close(second_instrument.conj().T @ second_instrument, np.eye(32), "second native isometry")
    for old_sign in (-1, 1):
        old_projector = projector_from_involution(square.edge_z(first_edge), old_sign)
        close(
            (
                square.edge_z(second_edge)
                - old_sign * square.vertex_parity(1) @ square.vertex_parity(2)
            )
            @ old_projector
            @ code_isom,
            np.zeros((16, 8), dtype=complex),
            f"battery fixture bridge boundary sign {old_sign}",
        )
    close(
        first_output_hamiltonian @ first_instrument - first_instrument @ input_hamiltonian,
        -first_instrument @ first_term,
        "first native energy defect",
    )
    removed_second = np.kron(np.eye(2), second_term)
    close(
        second_output_hamiltonian @ second_instrument
        - second_instrument @ second_input_hamiltonian,
        -second_instrument @ removed_second,
        "second native energy defect",
    )

    battery_dimension = 8
    battery_hamiltonian = np.diag(np.arange(battery_dimension, dtype=float)).astype(complex)
    first_lift, first_shifts = translation_lift(
        input_hamiltonian,
        first_output_hamiltonian,
        first_instrument,
        battery_dimension,
    )
    second_lift, second_shifts = translation_lift(
        second_input_hamiltonian,
        second_output_hamiltonian,
        second_instrument,
        battery_dimension,
    )
    direct_lift, direct_shifts = translation_lift(
        input_hamiltonian,
        second_output_hamiltonian,
        composite_instrument,
        battery_dimension,
    )
    require(first_shifts == (-1, 0, 1), f"first transfer spectrum {first_shifts}")
    require(second_shifts == (-1, 0, 1), f"second transfer spectrum {second_shifts}")
    require(direct_shifts == (-2, 0, 2), f"composite transfer spectrum {direct_shifts}")

    input_total_hamiltonian = np.kron(input_hamiltonian, np.eye(battery_dimension)) + np.kron(
        np.eye(16), battery_hamiltonian
    )
    first_total_hamiltonian = np.kron(first_output_hamiltonian, np.eye(battery_dimension)) + np.kron(
        np.eye(32), battery_hamiltonian
    )
    second_total_hamiltonian = np.kron(second_output_hamiltonian, np.eye(battery_dimension)) + np.kron(
        np.eye(64), battery_hamiltonian
    )
    close(
        first_total_hamiltonian @ first_lift,
        first_lift @ input_total_hamiltonian,
        "first lifted total-energy intertwining",
        2.0e-9,
    )
    close(
        second_total_hamiltonian @ second_lift,
        second_lift @ first_total_hamiltonian,
        "second lifted total-energy intertwining",
        3.0e-9,
    )
    close(
        second_total_hamiltonian @ direct_lift,
        direct_lift @ input_total_hamiltonian,
        "direct composite total-energy intertwining",
        3.0e-9,
    )

    packet = np.zeros(battery_dimension, dtype=complex)
    packet_support = (2, 3, 4, 5)
    for packet_position, battery_level in enumerate(packet_support):
        packet[battery_level] = math.sin(math.pi * (packet_position + 1) / 5.0) * np.exp(
            0.37j * battery_level
        )
    packet = normalized(packet)
    packet_embedding = np.eye(battery_dimension, dtype=complex)[:, packet_support]
    safe_domain = np.kron(code_isom, packet_embedding)
    first_refusal = np.eye(first_lift.shape[1]) - first_lift.conj().T @ first_lift
    second_refusal = np.eye(second_lift.shape[1]) - second_lift.conj().T @ second_lift
    require(float(np.min(np.linalg.eigvalsh(first_refusal))) >= -3.0e-9, "first cap contraction")
    require(float(np.min(np.linalg.eigvalsh(second_refusal))) >= -3.0e-9, "second cap contraction")
    close(safe_domain.conj().T @ first_refusal @ safe_domain, np.zeros((32, 32)), "zero first refusal")
    reachable_domain = first_lift @ safe_domain
    close(
        reachable_domain.conj().T @ second_refusal @ reachable_domain,
        np.zeros((32, 32)),
        "zero second refusal on correlated reachable domain",
    )
    close(
        (second_lift @ first_lift - direct_lift) @ safe_domain,
        np.zeros((64 * battery_dimension, 32)),
        "same-battery telescoping on cap-safe domain",
        5.0e-9,
    )

    fock_input_hamiltonian = fock.hoppings[first_edge] + fock.hoppings[second_edge]
    fock_after_first = fock.hoppings[second_edge]
    eigenvalues, eigenvectors = fixed_number_eigenvectors(fock, fock_input_hamiltonian, 2)
    ground_fock = eigenvectors[:, 0]
    require(abs(eigenvalues[0] + 2.0) <= ATOL, "commensurate fixture ground energy")
    zero_positions = np.flatnonzero(np.abs(eigenvalues) <= 2.0e-9)
    zero_basis = eigenvectors[:, zero_positions]
    split_values, split_vectors = np.linalg.eigh(
        zero_basis.conj().T @ fock_after_first @ zero_basis
    )
    require(abs(split_values[0] + 1.0) <= ATOL and abs(split_values[-1] - 1.0) <= ATOL, "zero-energy dimer split")
    coherent_fock = normalized(
        zero_basis @ split_vectors[:, 0] + 1j * zero_basis @ split_vectors[:, -1]
    )
    close(fock_input_hamiltonian @ coherent_fock, np.zeros(8), "stationary degenerate input")
    ground_physical = code_isom @ ground_fock
    coherent_physical = code_isom @ coherent_fock

    for label, physical_state, input_energy in (
        ("ground", ground_physical, -2),
        ("degenerate", coherent_physical, 0),
    ):
        initial_state = np.kron(physical_state, packet)
        actual_first_state = first_lift @ initial_state
        actual_final_state = second_lift @ actual_first_state
        direct_final_state = direct_lift @ initial_state
        require(abs(float(np.vdot(actual_first_state, actual_first_state).real) - 1.0) <= 3.0e-9, f"first success {label}")
        require(abs(float(np.vdot(actual_final_state, actual_final_state).real) - 1.0) <= 4.0e-9, f"final success {label}")
        close(actual_final_state, direct_final_state, f"retained-battery state telescope {label}", 5.0e-9)
        ideal_first_state = first_instrument @ physical_state
        ideal_final_state = composite_instrument @ physical_state
        ideal_first_density = np.outer(ideal_first_state, ideal_first_state.conj())
        ideal_final_density = np.outer(ideal_final_state, ideal_final_state.conj())
        actual_first_density = reduced_system_from_vector(actual_first_state, 32, battery_dimension)
        actual_final_density = reduced_system_from_vector(actual_final_state, 64, battery_dimension)
        phase_average = phase_averaged_eigenstate_output(
            ideal_first_density, first_output_hamiltonian, input_energy, packet
        )
        close(actual_first_density, phase_average, f"stationary phase average {label}", 5.0e-9)
        compare_probability_maps(
            joint_history_energy_probabilities(actual_first_density, 2, after_first),
            joint_history_energy_probabilities(ideal_first_density, 2, after_first),
            f"first history-energy {label}",
        )
        compare_probability_maps(
            joint_history_energy_probabilities(actual_final_density, 4, after_second),
            joint_history_energy_probabilities(ideal_final_density, 4, after_second),
            f"complete history-energy {label}",
        )
        history_probabilities = []
        for history in range(2):
            history_probabilities.append(
                sum(
                    probability
                    for (candidate, _), probability in joint_history_energy_probabilities(
                        actual_first_density, 2, after_first
                    ).items()
                    if candidate == history
                )
            )
        require(all(probability > 1.0e-5 for probability in history_probabilities), f"nonzero histories {label}")

    coherent_initial = np.kron(coherent_physical, packet)
    coherent_first = first_lift @ coherent_initial
    coherent_reduced = reduced_system_from_vector(coherent_first, 32, battery_dimension)
    coherent_ideal_state = first_instrument @ coherent_physical
    coherent_ideal = np.outer(coherent_ideal_state, coherent_ideal_state.conj())
    full_history_distance = float(np.linalg.norm(coherent_reduced - coherent_ideal))
    conditional_distances = []
    for history in range(2):
        history_slice = slice(16 * history, 16 * (history + 1))
        actual_block = coherent_reduced[history_slice, history_slice]
        ideal_block = coherent_ideal[history_slice, history_slice]
        actual_probability = float(np.trace(actual_block).real)
        ideal_probability = float(np.trace(ideal_block).real)
        require(actual_probability > 1.0e-8, f"actual conditional history {history} is zero")
        require(ideal_probability > 1.0e-8, f"ideal conditional history {history} is zero")
        require(
            abs(actual_probability - ideal_probability) <= 4.0e-9,
            f"conditional history probability {history}",
        )
        actual_conditional_matter = actual_block / actual_probability
        ideal_conditional_matter = ideal_block / ideal_probability
        require(
            abs(float(np.trace(actual_conditional_matter).real) - 1.0) <= 4.0e-9,
            f"actual conditional normalization {history}",
        )
        require(
            abs(float(np.trace(ideal_conditional_matter).real) - 1.0) <= 4.0e-9,
            f"ideal conditional normalization {history}",
        )
        conditional_distances.append(
            float(np.linalg.norm(actual_conditional_matter - ideal_conditional_matter))
        )
    conditional_matter_distance = max(conditional_distances)
    require(
        conditional_matter_distance > 1.0e-3,
        "fixture does not witness conditional physical-matter coherence change",
    )
    battery_density = reduced_battery_from_vector(coherent_first, 32, battery_dimension)
    explicit_battery_density = np.zeros((battery_dimension, battery_dimension), dtype=complex)
    coefficient_rows = coherent_first.reshape((32, battery_dimension))
    for system_row in coefficient_rows:
        explicit_battery_density = explicit_battery_density + np.outer(
            system_row, system_row.conj()
        )
    close(battery_density, explicit_battery_density, "battery partial trace conjugation")
    close(battery_density, battery_density.conj().T, "battery reduced Hermiticity")
    require(abs(float(np.trace(battery_density).real) - 1.0) <= 4.0e-9, "battery reduced trace")
    require(max_abs(battery_density.imag) > 1.0e-3, "complex partial-trace control is inactive")
    battery_purity = float(np.trace(battery_density @ battery_density).real)
    require(battery_purity < 1.0 - 1.0e-4, "first event did not retain system-battery correlation")

    test_physical = code_isom @ fixed_number_vector(fock, 2)
    test_initial = np.kron(test_physical, packet)
    test_first = first_lift @ test_initial
    test_final = second_lift @ test_first
    matter_energy_initial = float(
        np.vdot(test_initial, np.kron(input_hamiltonian, np.eye(battery_dimension)) @ test_initial).real
    )
    battery_energy_initial = float(
        np.vdot(test_initial, np.kron(np.eye(16), battery_hamiltonian) @ test_initial).real
    )
    matter_energy_first = float(
        np.vdot(test_first, np.kron(first_output_hamiltonian, np.eye(battery_dimension)) @ test_first).real
    )
    battery_energy_first = float(
        np.vdot(test_first, np.kron(np.eye(32), battery_hamiltonian) @ test_first).real
    )
    matter_energy_final = float(
        np.vdot(test_final, np.kron(second_output_hamiltonian, np.eye(battery_dimension)) @ test_final).real
    )
    battery_energy_final = float(
        np.vdot(test_final, np.kron(np.eye(64), battery_hamiltonian) @ test_final).real
    )
    require(
        abs(matter_energy_initial + battery_energy_initial - matter_energy_first - battery_energy_first)
        <= 5.0e-9,
        "explicit first matter-battery energy ledger",
    )
    require(
        abs(matter_energy_initial + battery_energy_initial - matter_energy_final - battery_energy_final)
        <= 5.0e-9,
        "explicit final matter-battery energy ledger",
    )

    old_flag_first = np.kron(np.diag([-1.0, 1.0]), np.eye(16))
    old_physical_first = np.kron(np.eye(2), square.edge_z(first_edge))
    close(
        np.kron(old_flag_first - old_physical_first, np.eye(battery_dimension)) @ test_first,
        np.zeros_like(test_first),
        "first history label equals existing physical Record",
    )
    old_flag_final = np.kron(np.diag([-1.0, -1.0, 1.0, 1.0]), np.eye(16))
    new_flag_final = np.kron(np.diag([-1.0, 1.0, -1.0, 1.0]), np.eye(16))
    old_physical_final = np.kron(np.eye(4), square.edge_z(first_edge))
    new_physical_final = np.kron(np.eye(4), square.edge_z(second_edge))
    for difference, label in (
        (old_flag_final - old_physical_final, "old"),
        (new_flag_final - new_physical_final, "new"),
    ):
        close(
            np.kron(difference, np.eye(battery_dimension)) @ test_final,
            np.zeros_like(test_final),
            f"{label} history label equals physical Record",
        )
    number = physical_number(square)
    for state, histories in ((test_first, 2), (test_final, 4)):
        output_number = np.kron(np.eye(histories), number)
        close(
            np.kron(output_number - 2.0 * np.eye(output_number.shape[0]), np.eye(battery_dimension))
            @ state,
            np.zeros_like(state),
            "shared lift preserves sharp original N",
        )
    return (
        "integer native square lift reuses one correlated battery for two events; "
        f"conditional_matter_distance={conditional_matter_distance:.3e}, "
        f"full_history_distance={full_history_distance:.3e}, purity={battery_purity:.6f}"
    )


def fibre_moment_identity_check() -> str:
    square = SmallGraph(4, ((0, 1), (1, 2), (2, 3), (0, 3)))
    coefficients = {
        (0, 1): 0.83,
        (1, 2): -0.61,
        (2, 3): 1.0,
        (0, 3): -0.74,
    }
    terms = {
        edge: coefficients[edge] * square.hopping_generator(edge)
        for edge in square.edges
    }
    histories = (
        (square.edges, (), 0.137),
        (((0, 1), (1, 2), (2, 3)), (((0, 3), -1),), -0.211),
        (((0, 1), (2, 3)), (((0, 3), 1), ((1, 2), -1)), 0.319),
    )
    largest_coefficient = max(abs(value) for value in coefficients.values())
    for live_edges, records, tau in histories:
        q = len(live_edges)
        hamiltonian = history_hamiltonian(live_edges, terms)
        input_phase = scipy.linalg.expm(1j * tau * hamiltonian)
        mean_pullback = np.zeros_like(hamiltonian)
        second_pullback = np.zeros_like(hamiltonian)
        correction = np.zeros_like(hamiltonian)
        for edge in live_edges:
            output_hamiltonian = hamiltonian - terms[edge]
            instrument = native_record_isometry(square.edge_z(edge))
            history_hamiltonian_out = np.kron(np.eye(2), output_hamiltonian)
            output_phase = scipy.linalg.expm(-1j * tau * history_hamiltonian_out)
            fibre = output_phase @ instrument @ input_phase
            close(fibre.conj().T @ fibre, np.eye(16), f"fibre isometry q={q} edge={edge}")
            mean_pullback = mean_pullback + (
                fibre.conj().T @ history_hamiltonian_out @ fibre
            ) / q
            second_pullback = second_pullback + (
                fibre.conj().T @ history_hamiltonian_out @ history_hamiltonian_out @ fibre
            ) / q
            correction = correction + (
                scipy.linalg.expm(-1j * tau * hamiltonian)
                @ terms[edge]
                @ terms[edge]
                @ scipy.linalg.expm(1j * tau * hamiltonian)
            ) / q
        close(
            mean_pullback,
            (1.0 - 1.0 / q) * hamiltonian,
            f"fibre first moment q={q} records={records}",
            4.0e-9,
        )
        close(
            second_pullback,
            (1.0 - 2.0 / q) * hamiltonian @ hamiltonian + correction,
            f"fibre second moment q={q} records={records}",
            5.0e-9,
        )
        require(
            float(np.max(np.linalg.eigvalsh(correction)))
            <= largest_coefficient**2 + 3.0e-9,
            f"fibre correction bound q={q}",
        )

    rng = np.random.default_rng(20260905)
    correlated = normalized(
        rng.normal(size=32) + 1j * rng.normal(size=32)
    )
    live_edges = square.edges
    hamiltonian = history_hamiltonian(live_edges, terms)
    q = len(live_edges)
    averaged = np.zeros_like(hamiltonian)
    tau = 0.173
    for edge in live_edges:
        output_hamiltonian = hamiltonian - terms[edge]
        instrument = native_record_isometry(square.edge_z(edge))
        fibre = (
            scipy.linalg.expm(-1j * tau * np.kron(np.eye(2), output_hamiltonian))
            @ instrument
            @ scipy.linalg.expm(1j * tau * hamiltonian)
        )
        averaged = averaged + fibre.conj().T @ np.kron(
            np.eye(2), output_hamiltonian
        ) @ fibre / q
    left_expectation = float(
        np.vdot(correlated, np.kron(averaged, np.eye(2)) @ correlated).real
    )
    right_expectation = float(
        np.vdot(
            correlated,
            np.kron((1.0 - 1.0 / q) * hamiltonian, np.eye(2)) @ correlated,
        ).real
    )
    require(abs(left_expectation - right_expectation) <= 4.0e-9, "correlated ancillary witness")
    return "first/second fibre identities hold at q=4,3,2 and on a correlated input"


def source_contract_check() -> str:
    source_path = pathlib.Path(__file__).resolve()
    require(
        source_path.name == "native_edge_record_matter_instrument_independent_check_2026_09_05.py",
        "checker filename changed",
    )
    source = pathlib.Path(__file__).read_text(encoding="utf-8")
    digest_marker = 'SOURCE_INTEGRITY_SHA256 = "'
    digest_start = source.index(digest_marker) + len(digest_marker)
    digest_end = source.index('"', digest_start)
    require(digest_end - digest_start == 64, "source-integrity field width")
    normalized_source = source[:digest_start] + "0" * 64 + source[digest_end:]
    normalized_digest = hashlib.sha256(normalized_source.encode("utf-8")).hexdigest()
    require(normalized_digest == SOURCE_INTEGRITY_SHA256, "source-integrity digest")
    tree = ast.parse(source)
    allowed_import_roots = {
        "__future__",
        "ast",
        "dataclasses",
        "hashlib",
        "math",
        "numpy",
        "os",
        "pathlib",
        "scipy",
        "sys",
    }
    observed_import_roots = set()
    read_method_counts = {"read_text": 0, "read_bytes": 0}
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            observed_import_roots.update(alias.name.split(".")[0] for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            require(node.module is not None, "relative import is forbidden")
            observed_import_roots.add(node.module.split(".")[0])
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            require(
                node.func.id not in {"eval", "exec", "compile", "open", "__import__"},
                f"dynamic or external read call {node.func.id}",
            )
        elif isinstance(node, ast.Attribute):
            require(node.attr not in {"write_text", "write_bytes", "unlink", "rename"}, "source can mutate files")
            require(
                not (isinstance(node.value, ast.Name) and node.value.id == "sys" and node.attr == "path"),
                "checker changes import search path",
            )
            if node.attr in read_method_counts:
                read_method_counts[node.attr] += 1
    require(observed_import_roots <= allowed_import_roots, "import firewall rejected a module")
    require(AUDIT_TIMEOUT_SEC == 180, "timeout declaration")
    require(DENSE_MATRIX_AXIS_LIMIT == 600, "dense-axis declaration")
    require(ATOL <= 3.0e-10 and RANK_TOL <= 2.0e-9, "tolerance was weakened")
    for variable in (
        "OPENBLAS_NUM_THREADS",
        "OMP_NUM_THREADS",
        "MKL_NUM_THREADS",
        "VECLIB_MAXIMUM_THREADS",
        "NUMEXPR_NUM_THREADS",
    ):
        require(os.environ.get(variable) == "1", f"thread limit {variable}")
    function_names = {
        node.name for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }
    for name in EXPECTED_CHECK_NAMES:
        require(f"{name}_check" in function_names or name == "source_contract", f"missing check {name}")
    require(read_method_counts == {"read_text": 1, "read_bytes": 1}, "unexpected file read")
    return f"AST import/write firewall and execution envelope verified; bytes={len(source.encode())}"


def run_checks() -> int:
    checks = [
        ("direct_dictionary", direct_dictionary_check),
        ("nonbridge_instrument", nonbridge_instrument_check),
        ("bridge_and_history", bridge_and_history_check),
        ("uniform_history_moments", uniform_history_moments_check),
        ("bipartite_energy_bound", bipartite_energy_bound_check),
        ("placement_and_support", placement_and_support_check),
        ("shared_battery_native_history", shared_battery_native_history_check),
        ("fibre_moment_identity", fibre_moment_identity_check),
        ("source_contract", source_contract_check),
    ]
    require(tuple(name for name, _ in checks) == EXPECTED_CHECK_NAMES, "check registry changed")
    passed = 0
    failed = 0
    for name, function in checks:
        try:
            detail = function()
            print(f"PASS {name}: {detail}")
            passed += 1
        except Exception as error:  # deliberate runner boundary
            print(f"FAIL {name}: {type(error).__name__}: {error}")
            failed += 1
    source_bytes = pathlib.Path(__file__).read_bytes()
    print(f"source_sha256={hashlib.sha256(source_bytes).hexdigest()}")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(run_checks())
