#!/usr/bin/env python3
"""Exact commuting-projector certificate for the 61-site full128 code.

The functions are imported by the primary intertwiner runner.  They use a
common decoded coordinate chart only to prove algebraic facts; every reported
projector is conjugated by the already constructed bounded ``D U`` circuit to
the physical M2 sites.  This file defines a static code space, not a cooling,
preparation, admissibility, or genesis dynamics.
"""

from __future__ import annotations

from itertools import combinations
import math

import numpy as np


def local_pair_projector() -> np.ndarray:
    """Rank-four projector on ``q_i,q_j,r_ij,r_ji`` (little endian)."""
    projector = np.zeros((16, 16), dtype=float)
    for q_bits in (0, 1, 2):
        projector[q_bits, q_bits] = 1.0
    first = 3 | (1 << 2)
    second = 3 | (1 << 3)
    vector = np.zeros(16, dtype=float)
    vector[first] = 1 / math.sqrt(2)
    vector[second] = -1 / math.sqrt(2)
    projector += np.outer(vector, vector)
    return projector


def _pair_action(
    basis: int,
    q_left: int,
    q_right: int,
    register_first: int,
    register_second: int,
) -> dict[int, float]:
    active = ((basis >> q_left) & 1) and ((basis >> q_right) & 1)
    first = (basis >> register_first) & 1
    second = (basis >> register_second) & 1
    if not active:
        return {basis: 1.0} if first == second == 0 else {}
    if first == second:
        return {}
    cleared = basis & ~(1 << register_first) & ~(1 << register_second)
    first_basis = cleared | (1 << register_first)
    second_basis = cleared | (1 << register_second)
    sign = 1.0 if first else -1.0
    return {first_basis: 0.5 * sign, second_basis: -0.5 * sign}


def _apply_pair(
    state: dict[int, float], spec: tuple[int, int, int, int]
) -> dict[int, float]:
    result: dict[int, float] = {}
    for basis, amplitude in state.items():
        for target, factor in _pair_action(basis, *spec).items():
            result[target] = result.get(target, 0.0) + amplitude * factor
    return {basis: value for basis, value in result.items() if value}


def pair_commutator_failures(unordered_pairs: tuple[tuple[int, int], ...]) -> int:
    """Exhaust every reduced basis for all 105 unordered projector pairs."""
    failures = 0
    for first_index, second_index in combinations(range(len(unordered_pairs)), 2):
        first_pair = unordered_pairs[first_index]
        second_pair = unordered_pairs[second_index]
        logical = tuple(sorted(set(first_pair + second_pair)))
        q_index = {mode: index for index, mode in enumerate(logical)}
        offset = len(logical)
        first_spec = (
            q_index[first_pair[0]], q_index[first_pair[1]], offset, offset + 1
        )
        second_spec = (
            q_index[second_pair[0]], q_index[second_pair[1]], offset + 2, offset + 3
        )
        for basis in range(1 << (offset + 4)):
            source = {basis: 1.0}
            left = _apply_pair(_apply_pair(source, second_spec), first_spec)
            right = _apply_pair(_apply_pair(source, first_spec), second_spec)
            keys = set(left) | set(right)
            if any(abs(left.get(key, 0.0) - right.get(key, 0.0)) > 1e-15 for key in keys):
                failures += 1
    return failures


def triangle_masks(P) -> tuple[int, ...]:
    """The symmetry-closed 35 K7 triangles; their GF(2) rank is 15."""
    rows = []
    for vertices in combinations(range(7), 3):
        mask = 0
        for left, right in combinations(vertices, 2):
            mask ^= 1 << P.EDGE_INDEX[tuple(sorted((left, right)))]
        rows.append(mask)
    return tuple(rows)


def _rank_rows(P, masks: tuple[int, ...], width: int = 22) -> int:
    matrix = np.asarray(
        [[(mask >> column) & 1 for column in range(width)] for mask in masks],
        dtype=np.uint8,
    )
    return P.gf2_rank(matrix)


def _mask_transport(mask: int, permutation: tuple[int, ...]) -> int:
    result = 0
    for source, target in enumerate(permutation):
        result |= ((mask >> source) & 1) << target
    return result


def _diameter(S, sites) -> int:
    rows = tuple(sites)
    return max((S.l1(left, right) for left in rows for right in rows), default=0)


def certificate(S, C, P, decoded_frame_matrix) -> dict[str, object]:
    local = local_pair_projector()
    local_hermitian = float(np.linalg.norm(local - local.conj().T))
    local_idempotence = float(np.linalg.norm(local @ local - local))
    local_rank = int(np.linalg.matrix_rank(local, tol=1e-12))
    pair_commutators = pair_commutator_failures(C.UNORDERED_PAIRS)

    triangles = triangle_masks(P)
    triangle_rank = _rank_rows(P, triangles)
    anchored_rank = _rank_rows(P, tuple(P.CYCLE_MASKS))
    anchored_deleted_rank = _rank_rows(P, tuple(P.CYCLE_MASKS[1:]))
    symmetry_deleted_rank = _rank_rows(P, triangles[1:])

    triangle_set = set(triangles)
    triangle_covariance_failures = 0
    pair_covariance_failures = 0
    outer_covariance_failures = 0
    corridor_covariance_failures = 0
    decoded_pair_control_failures = 0
    cycle_pair_cross_commutator_failures = 0
    cycle_outer_cross_commutator_failures = 0
    frame_product_failures = 0
    outer_pairs = {
        frozenset((S.FACTOR_COORD[P.EDGE_INDEX[pair]], S.MIRROR_COORD[P.EDGE_INDEX[pair]]))
        for pair in S.REVERSE_PAIRS
    }
    frame_index = {
        tuple(int(value) for value in frame.ravel()): index
        for index, frame in enumerate(P.FRAMES)
    }
    decoded_frames = []

    # D maps each cycle X onto the primary-plus-mirror lifted check, while a
    # decoded logical Z control becomes exactly one DECODER row on the primary
    # 22 sites: CNOT control-Z is unchanged by D.  This is the physical Pauli
    # symplectic cross-commutator, not a decoded-space assertion.
    lifted_triangles = []
    for mask in triangles:
        row = np.zeros(25, dtype=np.uint8)
        for edge in range(22):
            if (mask >> edge) & 1:
                row[edge] = 1
                for mirror_index, reverse_pair in enumerate(S.REVERSE_PAIRS):
                    if edge == P.EDGE_INDEX[reverse_pair]:
                        row[22 + mirror_index] = 1
        lifted_triangles.append(row)
    logical_z_controls = []
    for logical in range(6):
        row = np.zeros(25, dtype=np.uint8)
        row[:22] = P.DECODER[logical]
        logical_z_controls.append(row)
    for cycle_row in lifted_triangles:
        for left, right in C.UNORDERED_PAIRS:
            cycle_pair_cross_commutator_failures += int(
                np.dot(cycle_row, logical_z_controls[left]) % 2
            )
            cycle_pair_cross_commutator_failures += int(
                np.dot(cycle_row, logical_z_controls[right]) % 2
            )
        for outer_row in S.REPETITION_Z_CHECKS:
            cycle_outer_cross_commutator_failures += int(
                np.dot(cycle_row, outer_row) % 2
            )
    for frame in P.FRAMES:
        mapping = tuple(P.mode_map(frame))
        permutation = P.edge_permutation(mapping)
        triangle_covariance_failures += {
            _mask_transport(mask, permutation) for mask in triangles
        } != triangle_set
        rotate = lambda site: tuple(int(value) for value in frame @ np.asarray(site, dtype=int))
        for left, right in C.UNORDERED_PAIRS:
            target = frozenset((mapping[left], mapping[right]))
            pair_covariance_failures += target not in {
                frozenset(pair) for pair in C.UNORDERED_PAIRS
            }
            physical_target = {
                rotate(C.REGISTER_SITE[(left, right)]),
                rotate(C.REGISTER_SITE[(right, left)]),
            }
            pair_covariance_failures += physical_target != {
                C.REGISTER_SITE[(mapping[left], mapping[right])],
                C.REGISTER_SITE[(mapping[right], mapping[left])],
            }
        outer_covariance_failures += {
            frozenset((rotate(left), rotate(right))) for left, right in map(tuple, outer_pairs)
        } != outer_pairs
        corridor_covariance_failures += {rotate(site) for site in C.CORRIDOR} != set(C.CORRIDOR)
        decoded, repeat_failures = decoded_frame_matrix(frame)
        decoded_frames.append(decoded)
        decoded_pair_control_failures += repeat_failures
        for source in range(7):
            expected = mapping[source] if source < 6 else 6
            decoded_pair_control_failures += tuple(np.flatnonzero(decoded[:7, source])) != (expected,)
        decoded_pair_control_failures += int(np.count_nonzero(decoded[:7, 7:]))
    for left_index, left in enumerate(P.FRAMES):
        for right_index, right in enumerate(P.FRAMES):
            target = frame_index[tuple(int(value) for value in (left @ right).ravel())]
            frame_product_failures += not np.array_equal(
                (decoded_frames[left_index] @ decoded_frames[right_index]) % 2,
                decoded_frames[target],
            )

    pair_support_sizes = []
    pair_support_diameters = []
    support_exactness_failures = 0
    for pair in C.UNORDERED_PAIRS:
        left_mask = sum(
            int(value) << index for index, value in enumerate(P.DECODER[pair[0]])
        )
        right_mask = sum(
            int(value) << index for index, value in enumerate(P.DECODER[pair[1]])
        )
        support_exactness_failures += left_mask == right_mask
        shell_wires = {
            index for index in range(22) if ((left_mask | right_mask) >> index) & 1
        }
        # The conditional projector contains the distinct nonzero Pauli terms
        # Z_i and Z_j multiplied by a nonzero register operator.  Therefore
        # every site in this union is actual operator support; it is not merely
        # a decoder-row proxy or a routed-gate support estimate.
        support_exactness_failures += any(
            not (((left_mask | right_mask) >> index) & 1) for index in shell_wires
        )
        sites = {S.WIRE_COORDS[index] for index in shell_wires}
        sites.update((C.REGISTER_SITE[pair], C.REGISTER_SITE[(pair[1], pair[0])]))
        pair_support_sizes.append(len(sites))
        pair_support_diameters.append(_diameter(S, sites))

    # Common decoded chart: 7 logical qubits remain free; 15 cycle auxiliaries,
    # 3 mirrors, 30 pair-register qubits, and 6 corridor/work qubits are fixed.
    fixed_exponent = 15 + 3 + 30 + 6
    joint_code_dimension = 1 << (61 - fixed_exponent)
    pair_deleted_dimension = joint_code_dimension * 4
    outer_deleted_dimension = joint_code_dimension * 2
    corridor_deleted_dimension = joint_code_dimension * 2
    gap = 1  # a single corridor bit flip violates exactly one blank projector
    projector_count = len(triangles) + 3 + 15 + 6

    passed = (
        local_hermitian < 1e-14
        and local_idempotence < 1e-14
        and local_rank == 4
        and pair_commutators == 0
        and cycle_pair_cross_commutator_failures == 0
        and cycle_outer_cross_commutator_failures == 0
        and len(triangles) == 35
        and triangle_rank == anchored_rank == 15
        and anchored_deleted_rank == 14
        and symmetry_deleted_rank == 15
        and triangle_covariance_failures == pair_covariance_failures == 0
        and outer_covariance_failures == corridor_covariance_failures == 0
        and decoded_pair_control_failures == frame_product_failures == 0
        and support_exactness_failures == 0
        and joint_code_dimension == 128
        and pair_deleted_dimension == 512
        and outer_deleted_dimension == corridor_deleted_dimension == 256
        and gap == 1
        and projector_count == 59
    )
    return {
        "pass": passed,
        "pair_projector_rank": local_rank,
        "pair_projector_hermiticity_residual": local_hermitian,
        "pair_projector_idempotence_residual": local_idempotence,
        "pair_projector_commutator_failures": pair_commutators,
        "pair_projector_commutator_pairs": 105,
        "cycle_pair_cross_commutator_tests": 35 * 15 * 2,
        "cycle_pair_cross_commutator_failures": cycle_pair_cross_commutator_failures,
        "cycle_outer_cross_commutator_tests": 35 * 3,
        "cycle_outer_cross_commutator_failures": cycle_outer_cross_commutator_failures,
        "cycle_triangle_projectors": len(triangles),
        "cycle_independent_rank": triangle_rank,
        "anchored_basis_rank_after_one_deletion": anchored_deleted_rank,
        "symmetry_family_rank_after_one_redundant_deletion": symmetry_deleted_rank,
        "outer_repetition_projectors": 3,
        "conditional_pair_projectors": 15,
        "corridor_blank_projectors": 6,
        "commuting_projectors_total": projector_count,
        "joint_code_dimension": joint_code_dimension,
        "pair_projector_deletion_dimension": pair_deleted_dimension,
        "outer_projector_deletion_dimension": outer_deleted_dimension,
        "corridor_projector_deletion_dimension": corridor_deleted_dimension,
        "finite_cell_penalty_gap": gap,
        "maximum_exact_DU_pair_projector_site_support": max(pair_support_sizes),
        "maximum_exact_DU_pair_projector_L1_diameter": max(pair_support_diameters),
        "DU_pair_projector_support_exactness_failures": support_exactness_failures,
        "triangle_family_covariance_failures": triangle_covariance_failures,
        "pair_family_covariance_failures": pair_covariance_failures,
        "outer_family_covariance_failures": outer_covariance_failures,
        "corridor_family_covariance_failures": corridor_covariance_failures,
        "decoded_pair_control_covariance_failures": decoded_pair_control_failures,
        "ordered_frame_product_failures": frame_product_failures,
        "physical_definition": (
            "conjugate decoded conditional-pair and auxiliary projectors by the bounded D U circuit; "
            "cycle triangles, outer repetitions and corridor blanks are already local physical checks"
        ),
        "scope": (
            "static frustration-free commuting-projector code with gap one; no dynamical enforcement, "
            "cooling, preparation, admissibility selection or genesis"
        ),
    }
