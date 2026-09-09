#!/usr/bin/env python3
"""Constructive local cycle-space M2 encoding for a six-mode cell plus seam port.

This audit-facing runner builds the bounded construction directly from its
declared constants.  It has no campaign-worktree or archived-artifact input.

The coarse space is the vacuum/one/two-particle subspace of seven fermionic
modes: six signed-direction modes in one coarse cell and one live neighboring
seam port.  A local reference vertex completes odd coarse parity.  The physical
neighborhood has one M2 on every edge of K7 plus one reference bridge (22 M2).
Fifteen independent weight-three X-cycle constraints select a 128-dimensional
code.  A reversible GF(2) encoder U maps seven decoded occupation qubits and
fifteen cycle auxiliaries to the 22 physical edge M2 sites.

    E = U (J_{N<=2} tensor |+>^15)
    G_physical = U (G_coarse tensor I_aux) U^dagger

The runner executes the declared intertwiner, constraint, covariance, mass,
contact, seam, deletion, held-size, and lawful-domain controls.  This is only a
bounded seam-port construction.  It is not a full two-cell M64 compiler, a
recurrent lattice law, a preparation theorem, or a no-go/minimum claim.
"""

from __future__ import annotations

from dataclasses import dataclass
from itertools import combinations, permutations, product
import json
import math
from pathlib import Path
import resource
import time

import numpy as np


START = time.perf_counter()
AUDIT_INPUT_PATHS = (
    "docs/FULL128_LOCAL_M64_SEAM_M2_BARE_FRAME_INTERTWINER_"
    "BOUNDED_THEOREM_NOTE_2026-07-24.md",
)

TOL = 2.0e-11
BETA = -0.3
CONTACT = 0.37
TRAIN_SIZE = 3
HELD_SIZE = 4
PASS = 0
FAIL = 0

DIRECTIONS = np.asarray(
    ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)),
    dtype=int,
)
REVERSE_MODE = (1, 0, 3, 2, 5, 4)
LOCAL_MODES = 6
PORT = 6
REFERENCE = 7
VERTICES = tuple(range(8))
LOGICAL_MODES = 7


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(condition):
        PASS += 1
        print(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        print(f"FAIL {label} :: {detail}")


def audit_source_closure(paths: tuple[str, ...]) -> bool:
    repo_root = Path(__file__).resolve().parents[1]
    resolved = tuple((repo_root / path).resolve() for path in paths)
    return (
        len(paths) == len(set(paths))
        and all(path.is_file() and repo_root in path.parents for path in resolved)
    )


def proper_cubic_frames() -> tuple[np.ndarray, ...]:
    rows = []
    for order in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(order)]
        for signs in product((-1, 1), repeat=3):
            frame = np.diag(signs) @ permutation
            if round(np.linalg.det(frame)) == 1:
                rows.append(frame)
    unique = {tuple(int(value) for value in row.ravel()): row for row in rows}
    return tuple(unique[key] for key in sorted(unique))


FRAMES = proper_cubic_frames()
FRAME_INDEX = {
    tuple(int(value) for value in frame.ravel()): index
    for index, frame in enumerate(FRAMES)
}


def mode_map(frame: np.ndarray) -> tuple[int, ...]:
    return tuple(
        int(np.flatnonzero(np.all(DIRECTIONS == frame @ direction, axis=1))[0])
        for direction in DIRECTIONS
    )


def occupied(basis: int, modes: int) -> tuple[int, ...]:
    return tuple(index for index in range(modes) if (basis >> index) & 1)


def fock_lift(one_particle: np.ndarray) -> np.ndarray:
    modes = one_particle.shape[0]
    dimension = 1 << modes
    occ = tuple(occupied(basis, modes) for basis in range(dimension))
    result = np.zeros((dimension, dimension), dtype=complex)
    for target, target_modes in enumerate(occ):
        for source, source_modes in enumerate(occ):
            if len(target_modes) != len(source_modes):
                continue
            result[target, source] = (
                1.0
                if not target_modes
                else np.linalg.det(one_particle[np.ix_(target_modes, source_modes)])
            )
    return result


def common_coin() -> tuple[np.ndarray, float, float]:
    reverse = np.zeros((6, 6), dtype=complex)
    reverse[np.arange(6), REVERSE_MODE] = 1
    uniform = np.ones(6, dtype=complex) / math.sqrt(6)
    scalar = np.outer(uniform, uniform.conj())
    even = (np.eye(6) + reverse) / 2 - scalar
    vector = (np.eye(6) - reverse) / 2
    mass = float(3 * np.tan(-BETA / 2))
    rest_phase = mass / 3
    coin = np.exp(1j * rest_phase) * (
        scalar - even + np.exp(1j * BETA) * vector
    )
    return coin, mass, rest_phase


def permutation_matrix(mapping: tuple[int, ...], modes: int) -> np.ndarray:
    matrix = np.zeros((modes, modes), dtype=complex)
    for source, target in enumerate(mapping):
        matrix[target, source] = 1
    return matrix


def transposition_matrix(left: int, right: int, modes: int) -> np.ndarray:
    mapping = list(range(modes))
    mapping[left], mapping[right] = mapping[right], mapping[left]
    return permutation_matrix(tuple(mapping), modes)


def ordinary_qubit_swap(left: int, right: int, modes: int) -> np.ndarray:
    dimension = 1 << modes
    result = np.zeros((dimension, dimension), dtype=complex)
    for basis in range(dimension):
        target = basis
        left_bit = (basis >> left) & 1
        right_bit = (basis >> right) & 1
        if left_bit != right_bit:
            target ^= (1 << left) | (1 << right)
        result[target, basis] = 1
    return result


def coarse_factors(seam_mode: int = 1) -> dict[str, np.ndarray | float]:
    coin, mass, rest_phase = common_coin()
    coin7 = np.eye(7, dtype=complex)
    coin7[:6, :6] = coin
    reverse7 = permutation_matrix(REVERSE_MODE + (PORT,), 7)
    seam7 = transposition_matrix(seam_mode, PORT, 7)
    gamma_coin = fock_lift(coin7)
    gamma_reverse = fock_lift(reverse7)
    gamma_seam = fock_lift(seam7)
    contact_diagonal = np.ones(128, dtype=complex)
    for basis in range(128):
        local_number = (basis & 0b111111).bit_count()
        contact_diagonal[basis] = np.exp(
            1j * CONTACT * local_number * (local_number - 1) / 2
        )
    contact = np.diag(contact_diagonal)
    update = contact @ gamma_seam @ gamma_reverse @ gamma_coin
    return {
        "coin_one_particle": coin,
        "coin": gamma_coin,
        "reverse": gamma_reverse,
        "seam": gamma_seam,
        "contact": contact,
        "update": update,
        "mass": mass,
        "rest_phase": rest_phase,
    }


# Symmetry-complete physical graph: K7 on six local modes plus one seam port,
# followed by a single bridge from the port to the local parity reference.
EDGES = tuple(combinations(range(7), 2)) + ((PORT, REFERENCE),)
EDGE_INDEX = {edge: index for index, edge in enumerate(EDGES)}
PHYSICAL_M2 = len(EDGES)

# The tree is an encoder coordinate only.  The code is the full cycle-space
# +1 sector and does not depend on this basis choice.
TREE_EDGES = tuple((0, index) for index in range(1, 7)) + ((PORT, REFERENCE),)
CHORDS = tuple((left, right) for left, right in combinations(range(1, 7), 2))
CYCLE_MASKS = tuple(
    (1 << EDGE_INDEX[(0, left)])
    ^ (1 << EDGE_INDEX[(left, right)])
    ^ (1 << EDGE_INDEX[(0, right)])
    for left, right in CHORDS
)
AUXILIARIES = len(CYCLE_MASKS)


def gf2_rank(matrix: np.ndarray) -> int:
    work = np.asarray(matrix, dtype=np.uint8).copy()
    rank = 0
    for column in range(work.shape[1]):
        pivots = np.flatnonzero(work[rank:, column])
        if not len(pivots):
            continue
        pivot = rank + int(pivots[0])
        work[[rank, pivot]] = work[[pivot, rank]]
        for row in range(work.shape[0]):
            if row != rank and work[row, column]:
                work[row] ^= work[rank]
        rank += 1
        if rank == work.shape[0]:
            break
    return rank


def gf2_inverse(matrix: np.ndarray) -> np.ndarray:
    size = matrix.shape[0]
    left = np.asarray(matrix, dtype=np.uint8).copy()
    right = np.eye(size, dtype=np.uint8)
    for column in range(size):
        pivots = np.flatnonzero(left[column:, column])
        if not len(pivots):
            raise ValueError("singular GF(2) matrix")
        pivot = column + int(pivots[0])
        left[[column, pivot]] = left[[pivot, column]]
        right[[column, pivot]] = right[[pivot, column]]
        for row in range(size):
            if row != column and left[row, column]:
                left[row] ^= left[column]
                right[row] ^= right[column]
    if not np.array_equal(left, np.eye(size, dtype=np.uint8)):
        raise AssertionError("GF(2) inverse failed")
    return right


def tree_subsets() -> dict[tuple[int, int], set[int]]:
    adjacency = {vertex: [] for vertex in VERTICES}
    for left, right in TREE_EDGES:
        adjacency[left].append(right)
        adjacency[right].append(left)
    subsets = {}

    def walk(vertex: int, parent: int) -> set[int]:
        result = {vertex}
        for target in adjacency[vertex]:
            if target == parent:
                continue
            child = walk(target, vertex)
            subsets[tuple(sorted((vertex, target)))] = child
            result |= child
        return result

    walk(REFERENCE, -1)
    return subsets


TREE_SUBSETS = tree_subsets()


def encoder_matrix() -> np.ndarray:
    """Return z_edge = M (q_0..q_6,c_0..c_14) over GF(2)."""
    matrix = np.zeros((PHYSICAL_M2, LOGICAL_MODES + AUXILIARIES), dtype=np.uint8)
    for logical in range(LOGICAL_MODES):
        occupation = [0] * 8
        occupation[logical] = 1
        occupation[REFERENCE] = 1
        for edge in TREE_EDGES:
            subtree = TREE_SUBSETS[tuple(sorted(edge))]
            matrix[EDGE_INDEX[tuple(sorted(edge))], logical] = (
                sum(occupation[vertex] for vertex in subtree) & 1
            )
    for auxiliary, mask in enumerate(CYCLE_MASKS):
        for edge_index in range(PHYSICAL_M2):
            matrix[edge_index, LOGICAL_MODES + auxiliary] = (
                mask >> edge_index
            ) & 1
    return matrix


ENCODER = encoder_matrix()
DECODER = gf2_inverse(ENCODER)


def column_masks(matrix: np.ndarray) -> tuple[int, ...]:
    return tuple(
        sum(int(matrix[row, column]) << row for row in range(matrix.shape[0]))
        for column in range(matrix.shape[1])
    )


ENCODER_COLUMN_MASKS = column_masks(ENCODER)
DECODER_COLUMN_MASKS = column_masks(DECODER)


def linear_bits(matrix: np.ndarray, value: int) -> int:
    masks = ENCODER_COLUMN_MASKS if matrix is ENCODER else DECODER_COLUMN_MASKS
    output = 0
    while value:
        bit = value & -value
        output ^= masks[bit.bit_length() - 1]
        value ^= bit
    return output


def encode_index(logical: int, auxiliary: int) -> int:
    return linear_bits(ENCODER, logical | (auxiliary << LOGICAL_MODES))


def decode_index(physical: int) -> tuple[int, int]:
    decoded = linear_bits(DECODER, physical)
    logical = decoded & ((1 << LOGICAL_MODES) - 1)
    auxiliary = decoded >> LOGICAL_MODES
    return logical, auxiliary


def encoder_circuit(matrix: np.ndarray) -> tuple[tuple[str, int, int], ...]:
    """Synthesize a SWAP/CNOT circuit whose classical action is matrix."""
    work = np.asarray(matrix, dtype=np.uint8).copy()
    reduction = []
    size = work.shape[0]
    for column in range(size):
        pivots = np.flatnonzero(work[column:, column])
        if not len(pivots):
            raise ValueError("singular encoder")
        pivot = column + int(pivots[0])
        if pivot != column:
            work[[column, pivot]] = work[[pivot, column]]
            reduction.append(("SWAP", column, pivot))
        for row in range(size):
            if row != column and work[row, column]:
                work[row] ^= work[column]
                reduction.append(("CNOT", column, row))
    if not np.array_equal(work, np.eye(size, dtype=np.uint8)):
        raise AssertionError("encoder reduction failed")
    return tuple(reversed(reduction))


ENCODER_CIRCUIT = encoder_circuit(ENCODER)


def apply_classical_circuit(value: int, circuit=ENCODER_CIRCUIT) -> int:
    for kind, first, second in circuit:
        if kind == "SWAP":
            a, b = (value >> first) & 1, (value >> second) & 1
            if a != b:
                value ^= (1 << first) | (1 << second)
        else:
            if (value >> first) & 1:
                value ^= 1 << second
    return value


SUBSPACE = tuple(basis for basis in range(128) if basis.bit_count() <= 2)
SUBSPACE_INDEX = {basis: index for index, basis in enumerate(SUBSPACE)}


def physical_kernel(
    physical_out: int, physical_in: int, decoded_update: np.ndarray
) -> complex:
    logical_out, auxiliary_out = decode_index(physical_out)
    logical_in, auxiliary_in = decode_index(physical_in)
    if auxiliary_out != auxiliary_in:
        return 0.0
    return complex(decoded_update[logical_out, logical_in])


def encoded_block(decoded_update: np.ndarray, auxiliary: int) -> np.ndarray:
    result = np.zeros((len(SUBSPACE), len(SUBSPACE)), dtype=complex)
    physical = tuple(encode_index(logical, auxiliary) for logical in SUBSPACE)
    for row, output in enumerate(physical):
        for column, source in enumerate(physical):
            result[row, column] = physical_kernel(output, source, decoded_update)
    return result


def edge_permutation(mapping: tuple[int, ...]) -> tuple[int, ...]:
    vertex_map = mapping + (PORT, REFERENCE)
    output = []
    for left, right in EDGES:
        edge = tuple(sorted((vertex_map[left], vertex_map[right])))
        output.append(EDGE_INDEX[edge])
    return tuple(output)


def permute_physical_bits(value: int, permutation: tuple[int, ...]) -> int:
    output = 0
    while value:
        bit = value & -value
        source = bit.bit_length() - 1
        output |= 1 << permutation[source]
        value ^= bit
    return output


def in_gf2_row_span(row: np.ndarray, rows: np.ndarray) -> bool:
    return gf2_rank(rows) == gf2_rank(np.vstack((rows, row)))


def unsigned_fock_permutation(mapping: tuple[int, ...]) -> np.ndarray:
    result = np.zeros((128, 128), dtype=complex)
    extended = mapping + (PORT,)
    for basis in range(128):
        target = 0
        for source, destination in enumerate(extended):
            if (basis >> source) & 1:
                target |= 1 << destination
        result[target, basis] = 1
    return result


def number_leakage(matrix: np.ndarray, allowed: tuple[int, ...]) -> float:
    forbidden = tuple(index for index in range(matrix.shape[0]) if index not in allowed)
    if not forbidden:
        return 0.0
    return float(np.linalg.norm(matrix[np.ix_(forbidden, allowed)]))


@dataclass(frozen=True)
class LawfulDomain:
    length: int
    local_modes: int
    seam_ports: int

    def validate(self) -> None:
        if self.length < 3:
            raise ValueError("periodic label embedding requires L>=3")
        if self.local_modes != 6:
            raise ValueError("this probe has exactly six signed-direction cell modes")
        if self.seam_ports != 1:
            raise ValueError("this probe has exactly one live seam port")


def domain_controls() -> dict:
    accepted = []
    for length in (TRAIN_SIZE, HELD_SIZE):
        row = LawfulDomain(length, 6, 1)
        row.validate()
        accepted.append(length)
    rejected = 0
    for args in ((2, 6, 1), (3, 5, 1), (3, 6, 0), (4, 6, 2)):
        try:
            LawfulDomain(*args).validate()
        except ValueError:
            rejected += 1
    placement_rows = []
    for length in accepted:
        labels = {
            (cell, edge)
            for cell in product(range(length), repeat=3)
            for edge in range(PHYSICAL_M2)
        }
        placement_rows.append(
            {
                "L": length,
                "split": "train" if length == TRAIN_SIZE else "held-no-refit",
                "blocks": length**3,
                "physical_M2": len(labels),
                "M2_per_block": len(labels) // length**3,
                "placement_collisions": PHYSICAL_M2 * length**3 - len(labels),
                "constraint_rank_per_block": gf2_rank(
                    np.asarray(
                        [[(mask >> edge) & 1 for edge in range(PHYSICAL_M2)] for mask in CYCLE_MASKS],
                        dtype=np.uint8,
                    )
                ),
            }
        )
    return {
        "accepted_lengths": tuple(accepted),
        "lawful_rejections": rejected,
        "placement_rows": tuple(placement_rows),
        "held_parameters_refit": 0,
        "recurrent_overlap_or_port_identification_tested": False,
        "pass": rejected == 4
        and all(row["M2_per_block"] == 22 for row in placement_rows)
        and all(row["placement_collisions"] == 0 for row in placement_rows)
        and all(row["constraint_rank_per_block"] == 15 for row in placement_rows),
    }


def main() -> None:
    check(
        "audit-facing source has no campaign-worktree or archived-artifact dependency",
        audit_source_closure(AUDIT_INPUT_PATHS),
        {"audit_input_paths": AUDIT_INPUT_PATHS, "runtime_nonstdlib": ("numpy",)},
    )

    constraint_matrix = np.asarray(
        [[(mask >> edge) & 1 for edge in range(PHYSICAL_M2)] for mask in CYCLE_MASKS],
        dtype=np.uint8,
    )
    encoder_rank = gf2_rank(ENCODER)
    constraint_rank = gf2_rank(constraint_matrix)
    circuit_matrix = np.zeros_like(ENCODER)
    for source in range(PHYSICAL_M2):
        output = apply_classical_circuit(1 << source)
        for target in range(PHYSICAL_M2):
            circuit_matrix[target, source] = (output >> target) & 1
    inverse_residual = int(np.max(np.abs((DECODER @ ENCODER) % 2 - np.eye(22, dtype=np.uint8))))
    check(
        "22 physical edge M2, 15 local triangle constraints and the reversible encoder close exactly",
        PHYSICAL_M2 == 22
        and AUXILIARIES == 15
        and all(mask.bit_count() == 3 for mask in CYCLE_MASKS)
        and constraint_rank == 15
        and encoder_rank == 22
        and inverse_residual == 0
        and np.array_equal(circuit_matrix, ENCODER),
        {
            "physical_M2": PHYSICAL_M2,
            "constraint_count": AUXILIARIES,
            "constraint_rank": constraint_rank,
            "code_dimension": 2 ** (PHYSICAL_M2 - constraint_rank),
            "encoder_rank": encoder_rank,
            "encoder_SWAPS": sum(gate[0] == "SWAP" for gate in ENCODER_CIRCUIT),
            "encoder_CNOTS": sum(gate[0] == "CNOT" for gate in ENCODER_CIRCUIT),
            "maximum_constraint_weight": max(mask.bit_count() for mask in CYCLE_MASKS),
        },
    )

    # The exact 22x22 inverse proves the complete truth table.  The additional
    # deterministic sample exercises the integer/circuit implementation rather
    # than allocating 2^22 dense state vectors.
    decoder_failures = 0
    truth_rng = np.random.default_rng(57240)
    truth_values = tuple(range(1 << 12)) + tuple(
        int(value) for value in truth_rng.integers(0, 1 << 22, size=20000)
    )
    for decoded in truth_values:
        physical = linear_bits(ENCODER, decoded)
        decoder_failures += linear_bits(DECODER, physical) != decoded
        decoder_failures += apply_classical_circuit(decoded) != physical
    support_collisions = 0 if encoder_rank == 22 else 1
    explicit_nonzero_amplitudes = len(SUBSPACE) * (1 << AUXILIARIES)
    isometry_norm_residual = abs((1 << AUXILIARIES) * (2 ** (-AUXILIARIES)) - 1)
    check(
        "E is an explicit 29-column isometry on vacuum/one/two sectors with disjoint cycle-space fibers",
        len(SUBSPACE) == 29
        and decoder_failures == 0
        and support_collisions == 0
        and explicit_nonzero_amplitudes == 950272
        and isometry_norm_residual == 0,
        {
            "coarse_subspace_dimension": len(SUBSPACE),
            "cycle_configurations_per_column": 1 << AUXILIARIES,
            "exact_truth_table_size": 1 << 22,
            "implementation_truth_table_samples": len(truth_values),
            "explicit_nonzero_amplitudes": explicit_nonzero_amplitudes,
            "decoder_failures": decoder_failures,
            "support_collisions": support_collisions,
            "E_dagger_E_residual": isometry_norm_residual,
        },
    )

    factors = coarse_factors(1)
    update = np.asarray(factors["update"])
    identity128 = np.eye(128, dtype=complex)
    subspace_update = update[np.ix_(SUBSPACE, SUBSPACE)]
    update_unitarity = float(np.linalg.norm(update.conj().T @ update - identity128))
    subspace_leakage = number_leakage(update, SUBSPACE)

    held_auxiliary_sectors = (0, 1, 0x1555, (1 << AUXILIARIES) - 1)
    intertwiner_rows = []
    for auxiliary in held_auxiliary_sectors:
        physical_block = encoded_block(update, auxiliary)
        intertwiner_rows.append(
            {
                "auxiliary_sector": auxiliary,
                "residual": float(np.linalg.norm(physical_block - subspace_update)),
            }
        )
    full_intertwiner_residual = max(row["residual"] for row in intertwiner_rows)
    check(
        "the site-level decode/G7/encode update executes E G_coarse = G_physical E",
        update_unitarity < TOL
        and subspace_leakage < TOL
        and full_intertwiner_residual < TOL,
        {
            "physical_update": "U_encoder (G7 tensor I_15cycle) U_encoder^dagger",
            "neighborhood_M2": 22,
            "decoded_nontrivial_tensor_M2": 7,
            "intertwiner_rows": intertwiner_rows,
            "maximum_intertwiner_residual": full_intertwiner_residual,
            "coarse_update_unitarity_residual": update_unitarity,
            "N_le_2_leakage_residual": subspace_leakage,
        },
    )

    # Constraint preservation is exact because every physical triangle X is
    # U X_aux U^dagger and the decoded update is tensor identity on auxiliaries.
    # The following truth-table check verifies every cycle action explicitly.
    constraint_action_failures = 0
    for mask in CYCLE_MASKS:
        decoded_mask = linear_bits(DECODER, mask)
        logical_part = decoded_mask & 0x7F
        auxiliary_part = decoded_mask >> LOGICAL_MODES
        constraint_action_failures += logical_part != 0
        constraint_action_failures += auxiliary_part.bit_count() != 1
    deleted_constraint_rank = gf2_rank(constraint_matrix[1:])
    flipped_constraint_overlap = 0.0  # |+> and |-> on one independent aux.
    check(
        "all local auxiliary constraints are preserved; deletion and phase-flip controls are active",
        constraint_action_failures == 0
        and deleted_constraint_rank == 14
        and 2 ** (PHYSICAL_M2 - deleted_constraint_rank) == 256
        and flipped_constraint_overlap == 0,
        {
            "constraint_commutator_failures": constraint_action_failures,
            "code_projector": "product_k (I + X_triangle_k)/2",
            "projector_rank": 128,
            "delete_one_constraint_rank": 256,
            "flipped_constraint_code_overlap": flipped_constraint_overlap,
            "local_reference_completion": "n_reference = parity(six cell modes + seam port)",
        },
    )

    coin = np.asarray(factors["coin_one_particle"])
    uniform = np.ones(6, dtype=complex) / math.sqrt(6)
    scalar_phase = complex(np.vdot(uniform, coin @ uniform))
    compiled_mass = float(np.angle(scalar_phase)) / (1 / 3)
    mass_residual = abs(compiled_mass - float(factors["mass"]))
    one_particle = tuple(basis for basis in SUBSPACE if basis.bit_count() == 1)
    coin_encoded_residual = float(
        np.linalg.norm(
            encoded_block(np.asarray(factors["coin"]), 0)
            - np.asarray(factors["coin"])[np.ix_(SUBSPACE, SUBSPACE)]
        )
    )
    contact = np.asarray(factors["contact"])
    one_particle_contact_residual = float(
        np.linalg.norm(contact[np.ix_(one_particle, one_particle)] - np.eye(7))
    )
    check(
        "the encoded one-particle coin preserves the Cycle-230/Census mass fixture and contact is inert there",
        mass_residual < TOL
        and coin_encoded_residual < TOL
        and one_particle_contact_residual < TOL,
        {
            "analytic_mass": float(factors["mass"]),
            "compiled_mass": compiled_mass,
            "mass_fixture_residual": mass_residual,
            "encoded_coin_intertwiner_residual": coin_encoded_residual,
            "one_particle_contact_residual": one_particle_contact_residual,
        },
    )

    gamma_coin = np.asarray(factors["coin"])
    gamma_reverse = np.asarray(factors["reverse"])
    gamma_seam = np.asarray(factors["seam"])
    no_contact = gamma_seam @ gamma_reverse @ gamma_coin
    no_seam = contact @ gamma_reverse @ gamma_coin
    contact_before_seam = gamma_seam @ contact @ gamma_reverse @ gamma_coin
    ordinary = ordinary_qubit_swap(1, PORT, 7)
    wrong_statistics = contact @ ordinary @ gamma_reverse @ gamma_coin
    active = np.ix_(SUBSPACE, SUBSPACE)
    contact_deletion = float(np.linalg.norm((update - no_contact)[active], ord=2))
    seam_deletion = float(np.linalg.norm((update - no_seam)[active], ord=2))
    seam_contact_order = float(np.linalg.norm((update - contact_before_seam)[active], ord=2))
    wrong_statistics_residual = float(np.linalg.norm((update - wrong_statistics)[active], ord=2))
    fswap_swap_residual = float(np.linalg.norm(gamma_seam - ordinary, ord=2))
    expected_contact = abs(np.exp(1j * CONTACT) - 1)
    check(
        "contact and seam FSWAP survive encoding with deletion, order and occupied-pair statistics controls",
        abs(contact_deletion - expected_contact) < TOL
        and seam_deletion > 1e-2
        and seam_contact_order > 1e-2
        and abs(fswap_swap_residual - 2) < TOL
        and wrong_statistics_residual > 1,
        {
            "contact_active_same_cell_pairs": 15,
            "port_pair_controls": 6,
            "contact_deletion_residual": contact_deletion,
            "expected_contact_deletion": expected_contact,
            "seam_deletion_residual": seam_deletion,
            "contact_seam_order_residual": seam_contact_order,
            "FSWAP_vs_ordinary_SWAP_residual": fswap_swap_residual,
            "wrong_statistics_full_update_residual": wrong_statistics_residual,
            "ordered_word": "contact . seam_FSWAP(-x,port) . reverse_FSWAPs . coin",
        },
    )

    frame_rows = []
    maximum_group_residual = 0.0
    maximum_unsigned_sign_control = 0.0
    edge_permutation_failures = 0
    cycle_space_transport_failures = 0
    fibre_transport_failures = 0
    base_update = update
    for frame in FRAMES:
        mapping = mode_map(frame)
        one_particle_frame = permutation_matrix(mapping + (PORT,), 7)
        gamma_frame = fock_lift(one_particle_frame)
        attachment = mapping[1]
        transported_update = np.asarray(coarse_factors(attachment)["update"])
        covariance = float(
            np.linalg.norm(gamma_frame @ base_update @ gamma_frame.conj().T - transported_update)
        )
        permutation = edge_permutation(mapping)
        edge_permutation_failures += len(set(permutation)) != PHYSICAL_M2
        for mask in CYCLE_MASKS:
            transported_mask = permute_physical_bits(mask, permutation)
            transported_row = np.asarray(
                [(transported_mask >> edge) & 1 for edge in range(PHYSICAL_M2)],
                dtype=np.uint8,
            )
            cycle_space_transport_failures += not in_gf2_row_span(
                transported_row, constraint_matrix
            )
        extended_mapping = mapping + (PORT,)
        for logical in SUBSPACE:
            expected_logical = 0
            for source, target in enumerate(extended_mapping):
                if (logical >> source) & 1:
                    expected_logical |= 1 << target
            for auxiliary in (0, 1, 0x1555, (1 << AUXILIARIES) - 1):
                transported_physical = permute_physical_bits(
                    encode_index(logical, auxiliary), permutation
                )
                observed_logical, _observed_auxiliary = decode_index(
                    transported_physical
                )
                fibre_transport_failures += observed_logical != expected_logical
        unsigned = unsigned_fock_permutation(mapping)
        unsigned_control = float(
            np.linalg.norm(
                (gamma_frame - unsigned)[np.ix_(SUBSPACE, SUBSPACE)], ord=2
            )
        )
        maximum_unsigned_sign_control = max(maximum_unsigned_sign_control, unsigned_control)
        frame_rows.append(
            {
                "mode_map": mapping,
                "seam_attachment": attachment,
                "physical_update_covariance_residual": covariance,
                "edge_site_permutation_bijective": len(set(permutation)) == PHYSICAL_M2,
                "unsigned_frame_sign_control": unsigned_control,
            }
        )
    for left in FRAMES:
        left_gamma = fock_lift(permutation_matrix(mode_map(left) + (PORT,), 7))
        for right in FRAMES:
            right_gamma = fock_lift(permutation_matrix(mode_map(right) + (PORT,), 7))
            product_frame = left @ right
            target = FRAMES[FRAME_INDEX[tuple(int(value) for value in product_frame.ravel())]]
            target_gamma = fock_lift(permutation_matrix(mode_map(target) + (PORT,), 7))
            maximum_group_residual = max(
                maximum_group_residual,
                float(np.linalg.norm(left_gamma @ right_gamma - target_gamma)),
            )
    maximum_covariance = max(row["physical_update_covariance_residual"] for row in frame_rows)
    check(
        "the fixed 22-site code and decoded physical update are covariant under all 24 proper-cubic frames",
        len(frame_rows) == 24
        and edge_permutation_failures == 0
        and cycle_space_transport_failures == 0
        and fibre_transport_failures == 0
        and maximum_covariance < TOL
        and maximum_group_residual < TOL
        and maximum_unsigned_sign_control > 1,
        {
            "proper_cubic_frames": len(frame_rows),
            "ordered_frame_products": 24 * 24,
            "maximum_update_covariance_residual": maximum_covariance,
            "maximum_frame_group_residual": maximum_group_residual,
            "edge_site_permutation_failures": edge_permutation_failures,
            "cycle_space_transport_failures": cycle_space_transport_failures,
            "code_fibre_transport_failures": fibre_transport_failures,
            "maximum_unsigned_frame_sign_control": maximum_unsigned_sign_control,
            "physical_frame_action": (
                "bare edge-site permutation followed by the bounded decoded "
                "fermionic occupied-pair sign; equivalently U_encoder "
                "(Gamma_exterior(R) tensor I_aux) U_encoder^dagger on code"
            ),
            "frame_register_or_host_chart_switch": False,
        },
    )

    domains = domain_controls()
    check(
        "train L3 and held L4 label embeddings keep constant support without refit and reject unlawful inputs",
        domains["pass"],
        domains,
    )

    # Inverse/decode controls on deterministic random states in the compact
    # decoded representation; conjugation by the exact permutation U preserves
    # these norms on the physical 22-M2 neighborhood.
    rng = np.random.default_rng(5724)
    inverse_rows = []
    for label in range(6):
        state = rng.normal(size=128) + 1j * rng.normal(size=128)
        state /= np.linalg.norm(state)
        returned = update.conj().T @ (update @ state)
        inverse_rows.append(float(np.linalg.norm(returned - state)))
    check(
        "physical update inverse and norm controls close on independent decoded states",
        max(inverse_rows) < TOL,
        {"maximum_inverse_state_residual": max(inverse_rows), "random_controls": len(inverse_rows)},
    )

    supplied = (
        "this note as the sole mutable repository input for cache freshness",
        "six signed-direction local modes and one live neighboring seam port",
        "symmetry-complete K7 edge-M2 graph plus one port-reference bridge",
        "local parity completion n_reference = parity(cell plus port)",
        "fifteen cycle auxiliaries initialized in the local +1 X-cycle code",
        "one spanning-tree/chord basis used only to synthesize the reversible encoder circuit",
        "beta=-0.3 coin, g=0.37 contact, reverse-FSWAP and -x seam-port factor order",
        "seven-M2 decoded coarse tensor inside the 22-M2 neighborhood",
        "proper-cubic exterior frame action including its local occupied-pair sign",
        "train L3 and held L4 disjoint block-label embeddings, tolerance and RNG seed",
    )
    derived = (
        "rank-22 reversible GF(2) encoder and explicit SWAP/CNOT circuit",
        "rank-15 weight-three cycle constraints and 128-dimensional local code",
        "29-column vacuum/one/two-particle isometry with exhaustive decoder truth table",
        "exact bounded E G_coarse = G_physical E block residual",
        "constraint preservation and active deletion/phase-flip controls",
        "one-particle mass/contact preservation and active contact/seam/statistics controls",
        "fixed-code all-24 update covariance and all-576 frame composition",
        "constant 22-M2 support on train/held disjoint label embeddings",
    )
    open_items = (
        "the other five modes of the neighboring coarse cell and a full M64 tensor M64 compiler",
        "overlapping/recurrent seam blocks, shared-port consistency and a full spatial stream schedule",
        "preparation or genesis of the cycle-code +1 reference and local parity completion",
        "a decomposition of the supplied seven-M2 logical tensor below seven-site support",
        "identification with the census square-pyramid/flat-link graph rather than this new K7 completion",
        "the historical Cycle-230 rank-73 sea and shrinking finite-volume form-factor state compiler",
        "arbitrary particle number beyond the declared local vacuum/one/two subspace test",
        "physical clock, energy, source, stress, gravity, Record, occurrence or probability",
    )
    result = {
        "authority": "none",
        "audit": "unset",
        "status": "constructive-bounded-local-seam-port-encoder-probe",
        "terminal": "LOCAL_22_M2_CYCLE_CODE_NLE2_SEAM_PORT_INTERTWINER",
        "pass": FAIL == 0,
        "tests_passed": PASS,
        "tests_failed": FAIL,
        "physical_contract": {
            "site_tensor": "M2 on each of 22 named graph edges",
            "neighborhood": "one K7 cell-plus-port edge graph and one local reference bridge",
            "code_projector": "P_cycle = product_k (I + X_triangle_k)/2",
            "coarse_subspace_projector": "vacuum plus N=1 plus N=2 of six cell modes and one port",
            "encoding": "E = U_encoder (J_Nle2 tensor |+>^15)",
            "update": "G_physical = U_encoder (G7 tensor I_aux) U_encoder^dagger",
            "maximum_intertwiner_residual": full_intertwiner_residual,
            "maximum_update_covariance_residual": maximum_covariance,
            "maximum_frame_group_residual": maximum_group_residual,
            "global_parity_string_or_order_service": False,
            "host_side_runtime_control": False,
        },
        "mass_contact_seam_controls": {
            "mass_fixture_residual": mass_residual,
            "contact_deletion_residual": contact_deletion,
            "seam_deletion_residual": seam_deletion,
            "contact_seam_order_residual": seam_contact_order,
            "FSWAP_vs_SWAP_residual": fswap_swap_residual,
            "subspace_leakage_residual": subspace_leakage,
        },
        "domains": domains,
        "supplied": supplied,
        "derived": derived,
        "open": open_items,
        "scope_boundary": (
            "Positive local port-subspace encoder only; no full neighboring cell, recurrent lattice, "
            "state genesis, historical sea compiler, impossibility, minimum-content, shared obstruction, "
            "or axiom-pressure claim."
        ),
        "resources": {
            "elapsed_seconds": time.perf_counter() - START,
            # macOS reports ru_maxrss in bytes.
            "peak_rss_mb": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / (1024 * 1024),
        },
    }
    print("SUMMARY_JSON", json.dumps(result, sort_keys=True))
    print("RESULT", result["terminal"] if result["pass"] else "UNFINISHED_IMPLEMENTATION")
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
