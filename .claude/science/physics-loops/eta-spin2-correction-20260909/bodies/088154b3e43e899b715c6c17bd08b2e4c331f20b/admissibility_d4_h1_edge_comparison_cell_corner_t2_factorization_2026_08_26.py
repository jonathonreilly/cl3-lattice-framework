#!/usr/bin/env python3
"""Block 207 exact H1 edge-comparison/cell-corner factorization.

This runner separates three claims that are easy to conflate:

* the raw H1 source factors into native one-hop Laurent pieces;
* a cubic cell can select an odd or even ``T2`` decoder from typed ``M2``
  edge content; and
* actual neighboring Record contents physically supply those pieces.

The first two are finite exact calculations here.  The third remains a
strictly fenced successor obligation.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402
import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as b206  # noqa: E402


I = sp.I
B = b193.b190
AUDIT_TIMEOUT_SEC = 120
NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_FACTORIZATION_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block207-edge-comparison-cell-corner-t2-"
    "factorization-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "42b25280486363e9c2017698b813edf182d1a1a3"
PREREG_COMMIT = "c5f6e2fc8dea20218313944c8d5f5dae0f4d90cc"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "78d0c9a24ccb4eb96fe2112f60c1aea491100514"
PREFLIGHT_BLOB = "11addbb97c79b5acc0489f3dd940356726989bb6"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_EDGE_COMPARISON_CELL_CORNER_T2_FACTORIZATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    ".claude/science/physics-loops/toe-axiom-closure-block207-edge-comparison-cell-corner-t2-factorization-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block207-edge-comparison-cell-corner-t2-factorization-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "docs/ADMISSIBILITY_M2_RECORD_CUBIC_VECTOR_DECODER_SECTOR_GRADING_CARRIER_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_RECORD_NATIVE_STATE_DEPENDENT_BORN_HISTORY_JOINT_LAW_CANDIDATE_GATE_NOTE_2026-08-12.md",
)

MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "claim_scalar_edge_t2",
    "erase_scalar_corner_t2",
    "mix_radial_and_handed_then_claim_selection",
    "rotate_sites_without_bloch_vectors",
    "replace_mixed_by_linear_corner_moment",
    "remove_commutator_i",
    "erase_full_feature_rank",
    "fit_h1_group_weights",
    "replace_actual_reverse_by_adjoint",
    "erase_forward_residual",
    "erase_reverse_residual",
    "erase_atom_uniqueness",
    "call_factor_choice_cube_physical",
    "drop_temporal_groups_and_claim_fit",
    "hide_temporal_witness",
    "erase_incoming_p_collision",
    "supply_p_as_external_label",
    "identify_exterior_action_with_m2",
    "claim_actual_record_map",
    "open_h2_before_h1_ownership",
    "claim_formation",
    "claim_history",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
    "claim_broad_context_no_go",
    "erase_no_go_discipline",
)


def dm_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(matrix, extension=True).rank()


def git_output(*args: str) -> str:
    return subprocess.run(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=True,
    ).stdout.strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        capture_output=True,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    def commit_blob(commit: str, path: str) -> str:
        return git_output("rev-parse", f"{commit}:{path}")

    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_registered": commit_blob(PREREG_COMMIT, GOAL_PATH),
        "goal_worktree": commit_blob("HEAD", GOAL_PATH),
        "preflight_registered": commit_blob(PREREG_COMMIT, PREFLIGHT_PATH),
        "preflight_worktree": commit_blob("HEAD", PREFLIGHT_PATH),
        "axiom_main": commit_blob("origin/main", AXIOM_PATH),
        "axiom_worktree": commit_blob("HEAD", AXIOM_PATH),
        "registry_main": commit_blob("origin/main", REGISTRY_PATH),
        "registry_worktree": commit_blob("HEAD", REGISTRY_PATH),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def corners() -> tuple[sp.Matrix, ...]:
    return tuple(
        sp.Matrix((x, y, z))
        for x in (-1, 1) for y in (-1, 1) for z in (-1, 1)
    )


def corner_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    shell = corners()
    result = sp.zeros(8)
    for source, corner in enumerate(shell):
        transformed = rotation * corner
        target = next(
            index for index, candidate in enumerate(shell)
            if candidate == transformed
        )
        result[target, source] = 1
    return result


def parity_hom_dimension(sign: int) -> int:
    rotations = b194.proper_cubic_rotations()
    shell_reps = tuple(b206.shell_representation(r) for r in rotations)
    domains = tuple(
        sp.kronecker_product(shell, rotation)
        for shell, rotation in zip(shell_reps, rotations)
    )
    constraints = []
    for rotation, domain in zip(rotations, domains):
        target = b206.shear_representation(rotation)
        constraints.append(
            sp.kronecker_product(sp.eye(18), target)
            - sp.kronecker_product(domain.T, sp.eye(3))
        )
    edge_parity = sp.zeros(6)
    for axis in range(3):
        edge_parity[2 * axis, 2 * axis + 1] = 1
        edge_parity[2 * axis + 1, 2 * axis] = 1
    domain_parity = sp.kronecker_product(edge_parity, sp.eye(3))
    constraints.append(
        sp.kronecker_product(domain_parity.T, sp.eye(3))
        - sign * sp.eye(54)
    )
    matrix = sp.Matrix.vstack(*constraints)
    return 54 - dm_rank(matrix)


@cache
def representation_facts() -> dict[str, object]:
    rotations = b194.proper_cubic_rotations()
    corner_reps = tuple(corner_representation(r) for r in rotations)
    scalar_corner_hom = b206.hom_dimension(corner_reps)
    bloch_corner_reps = tuple(
        sp.kronecker_product(corner, rotation)
        for corner, rotation in zip(corner_reps, rotations)
    )
    bloch_corner_hom = b206.hom_dimension(bloch_corner_reps)

    mixed = sp.Matrix((
        tuple(c[0] * c[1] / 8 for c in corners()),
        tuple(c[1] * c[2] / 8 for c in corners()),
        tuple(c[0] * c[2] / 8 for c in corners()),
    ))
    mixed_equivariant = all(
        b206.shear_representation(rotation) * mixed
        == mixed * corner
        for rotation, corner in zip(rotations, corner_reps)
    )

    radial = sp.zeros(8, 18)
    handed = sp.zeros(8, 18)
    shell = b206.signed_neighbor_shell()
    for row, corner in enumerate(corners()):
        for axis in range(3):
            direction = corner[axis] * sp.eye(3)[:, axis]
            edge = next(
                index for index, item in enumerate(shell)
                if item == direction
            )
            cross = direction.cross(corner) / sp.sqrt(3)
            for component in range(3):
                radial[row, 3 * edge + component] += (
                    corner[component] / sp.sqrt(3)
                )
                handed[row, 3 * edge + component] += cross[component]

    odd, even = b206.conditional_adjoint_hom_basis()
    radial_composition = mixed * radial
    handed_composition = mixed * handed
    selector_covariance = all(
        corner * radial
        == radial * sp.kronecker_product(
            b206.shell_representation(rotation), rotation
        )
        and corner * handed
        == handed * sp.kronecker_product(
            b206.shell_representation(rotation), rotation
        )
        for rotation, corner in zip(rotations, corner_reps)
    )

    edge_parity = sp.zeros(6)
    for axis in range(3):
        edge_parity[2 * axis, 2 * axis + 1] = 1
        edge_parity[2 * axis + 1, 2 * axis] = 1
    corner_parity = sp.zeros(8)
    shell_corners = corners()
    for source, corner in enumerate(shell_corners):
        target = next(
            index for index, item in enumerate(shell_corners)
            if item == -corner
        )
        corner_parity[target, source] = 1
    edge_bloch_parity = sp.kronecker_product(edge_parity, sp.eye(3))

    return {
        "proper_cubic_count": len(rotations),
        "scalar_edge_hom": b206.neighbor_hom_facts()["scalar_hom_dimension"],
        "bloch_edge_hom": (
            b206.neighbor_hom_facts()["conditional_adjoint_hom_dimension"]
        ),
        "scalar_corner_hom": scalar_corner_hom,
        "bloch_corner_hom": bloch_corner_hom,
        "hermitian_corner_hom": scalar_corner_hom + bloch_corner_hom,
        "mixed_rank": mixed.rank(),
        "mixed_equivariant": mixed_equivariant,
        "selector_covariance": selector_covariance,
        "radial_selects_odd": (
            radial_composition == -odd / (2 * sp.sqrt(3))
        ),
        "handed_selects_even": (
            handed_composition == even / (2 * sp.sqrt(3))
        ),
        "mixed_corner_even": mixed * corner_parity == mixed,
        "radial_parity": (
            corner_parity * radial == -radial * edge_bloch_parity
        ),
        "handed_parity": (
            corner_parity * handed == handed * edge_bloch_parity
        ),
        "odd_parity_hom": parity_hom_dimension(-1),
        "even_parity_hom": parity_hom_dimension(1),
    }


@cache
def face_average_m2_facts() -> dict[str, object]:
    rotations = b194.proper_cubic_rotations()
    shell = b206.signed_neighbor_shell()
    shell_reps = tuple(b206.shell_representation(r) for r in rotations)
    corner_reps = tuple(corner_representation(r) for r in rotations)
    face_average = sp.zeros(18, 24)
    for edge, direction in enumerate(shell):
        axis = next(index for index, value in enumerate(direction) if value)
        sign = direction[axis]
        for corner_index, corner in enumerate(corners()):
            if corner[axis] == sign:
                for component in range(3):
                    face_average[
                        3 * edge + component,
                        3 * corner_index + component,
                    ] = sp.Rational(1, 4)

    equivariant = all(
        sp.kronecker_product(shell_rep, rotation) * face_average
        == face_average * sp.kronecker_product(corner_rep, rotation)
        for rotation, shell_rep, corner_rep
        in zip(rotations, shell_reps, corner_reps)
    )
    odd, even = b206.conditional_adjoint_hom_basis()
    h = sp.Matrix(b206.neighbor_hom_facts()["h1_shear_coordinates"])
    tensor = sp.Matrix((
        (0, h[0], h[2]),
        (h[0], 0, h[1]),
        (h[2], h[1], 0),
    ))
    affine = -tensor / 4
    field = sp.Matrix.vstack(*(
        affine * corner for corner in corners()
    ))
    norm_squares = tuple(
        sp.simplify((
            (affine * corner).T * (affine * corner)
        )[0])
        for corner in corners()
    )
    faces = face_average * field
    face_norm_squares = tuple(
        sp.simplify((faces[3 * edge:3 * edge + 3, :].T
                     * faces[3 * edge:3 * edge + 3, :])[0])
        for edge in range(6)
    )
    return {
        "map_rank": face_average.rank(),
        "equivariant": equivariant,
        "odd_output": tuple(sp.simplify(x) for x in odd * faces),
        "even_output": tuple(sp.simplify(x) for x in even * faces),
        "target_shear": tuple(h),
        "odd_map_rank": (odd * face_average).rank(),
        "even_map_zero": even * face_average == sp.zeros(3, 24),
        "max_corner_norm_square": max(norm_squares, key=lambda x: float(x)),
        "max_face_norm_square": max(
            face_norm_squares, key=lambda x: float(x)
        ),
        "strict_corner_density_positive": all(x < 1 for x in norm_squares),
        "strict_face_density_positive": all(x < 1 for x in face_norm_squares),
        "action_derived_contents": False,
    }


def reverse_polynomial(polynomial: B.PolyMatrix) -> B.PolyMatrix:
    result: B.PolyMatrix = {}
    for power, matrix in polynomial.items():
        reverse_power = power[:4] + tuple(
            power[index] - power[4 + index] for index in range(4)
        )
        result = B.poly_add(result, {reverse_power: matrix})
    return result


def singleton_atoms(polynomial: B.PolyMatrix) -> list[B.PolyMatrix]:
    return [{power: matrix} for power, matrix in polynomial.items()]


def native_hodge(slot: int) -> B.PolyMatrix:
    left, right = B.PAIRS4[slot]
    assert left < right < 3
    scalar = B.poly_scale(
        B.poly_multiply(
            B.placed_cosine(left), B.placed_cosine(right)
        ),
        -1 / sp.sqrt(2),
    )
    internal = (
        B.CREATION[left] * B.ANNIHILATION[right]
        + B.CREATION[right] * B.ANNIHILATION[left]
    )
    return B.poly_multiply(scalar, {B.ZERO_EXPONENT: internal})


def axis_differences() -> tuple[
    tuple[B.PolyMatrix, ...], tuple[B.PolyMatrix, ...]
]:
    incoming = []
    outgoing = []
    for axis in range(4):
        incoming.append({
            B.exponent({axis: 1}): B.CREATION[axis] / (2 * I),
            B.exponent({axis: -1}): -B.CREATION[axis] / (2 * I),
        })
        outgoing.append({
            B.exponent({axis: 1}, {axis: 1}): (
                B.CREATION[axis] / (2 * I)
            ),
            B.exponent({axis: -1}, {axis: -1}): (
                -B.CREATION[axis] / (2 * I)
            ),
        })
    return tuple(incoming), tuple(outgoing)


def feature_library(
    slots: tuple[int, ...]
) -> tuple[
    list[tuple[str, B.PolyMatrix]],
    list[tuple[str, B.PolyMatrix]],
]:
    incoming, outgoing = axis_differences()
    grouped: list[tuple[str, B.PolyMatrix]] = []
    atoms: list[tuple[str, B.PolyMatrix]] = []
    for slot in slots:
        hodge = native_hodge(slot)
        grouped.append((f"{slot}:mass", hodge))
        atoms.extend(
            (f"{slot}:mass:{index}", item)
            for index, item in enumerate(singleton_atoms(hodge))
        )
        for axis in range(4):
            right = B.poly_scale(
                B.poly_multiply(hodge, incoming[axis]), I
            )
            left = B.poly_scale(
                B.poly_multiply(B.poly_transpose(outgoing[axis]), hodge), I
            )
            grouped.append((f"{slot}:right:{axis}", right))
            grouped.append((f"{slot}:left:{axis}", left))
            atoms.extend(
                (f"{slot}:right:{axis}:{index}", item)
                for index, item in enumerate(singleton_atoms(right))
            )
            atoms.extend(
                (f"{slot}:left:{axis}:{index}", item)
                for index, item in enumerate(singleton_atoms(left))
            )
    return grouped, atoms


def design_matrix(
    columns: list[tuple[str, B.PolyMatrix]],
    target: B.PolyMatrix | None = None,
) -> tuple[sp.Matrix, sp.Matrix, tuple[tuple[object, ...], ...]]:
    zero = sp.zeros(16)
    polynomials = [item for _name, item in columns]
    if target is not None:
        polynomials = [target] + polynomials
    rows = tuple(sorted({
        (power, row, column)
        for polynomial in polynomials
        for power, matrix in polynomial.items()
        for row in range(16) for column in range(16)
        if matrix[row, column] != 0
    }))
    matrix = sp.Matrix([
        [polynomial.get(power, zero)[row, column]
         for _name, polynomial in columns]
        for power, row, column in rows
    ])
    vector = sp.Matrix([
        (target or {}).get(power, zero)[row, column]
        for power, row, column in rows
    ])
    return matrix, vector, rows


@cache
def action_factorization_facts() -> dict[str, object]:
    incoming, outgoing = axis_differences()
    raw_vertices = b206.raw_action_vertices()
    vertex_matches = []
    component_counts = []
    for slot in (7, 8, 9):
        hodge = native_hodge(slot)
        right = B.poly_scale(
            B.poly_multiply(hodge, B.poly_add(*incoming)), I
        )
        left = B.poly_scale(
            B.poly_multiply(
                B.poly_transpose(B.poly_add(*outgoing)), hodge
            ),
            I,
        )
        mass = B.poly_scale(hodge, B.MASS)
        vertex = B.poly_add(mass, right, left)
        vertex_matches.append(vertex == raw_vertices[slot])
        component_counts.append((
            len(hodge), len(mass), len(right), len(left), len(vertex)
        ))

    generic_grouped, generic_atoms = feature_library((7, 8, 9))
    generic_matrix, _zero, _rows = design_matrix(generic_grouped)
    generic_atom_matrix, _zero, _rows = design_matrix(generic_atoms)

    active_grouped, active_atoms = feature_library((8, 9))
    source = b206.combined_raw_source()
    coefficients = b193.tt_source_coefficients("H1", 1)
    active_weights = []
    for slot in (8, 9):
        active_weights.extend(
            (B.MASS * coefficients[slot],)
            + (coefficients[slot],) * 8
        )
    atom_weights = []
    for slot in (8, 9):
        atom_weights.extend((B.MASS * coefficients[slot],) * 4)
        atom_weights.extend((coefficients[slot],) * 64)

    forward_matrix, forward_vector, forward_rows = design_matrix(
        active_grouped, source
    )
    atom_matrix, atom_vector, _atom_rows = design_matrix(
        active_atoms, source
    )
    reverse_source = reverse_polynomial(source)
    reverse_grouped = [
        (name, reverse_polynomial(item)) for name, item in active_grouped
    ]
    reverse_atoms = [
        (name, reverse_polynomial(item)) for name, item in active_atoms
    ]
    reverse_matrix, reverse_vector, _reverse_rows = design_matrix(
        reverse_grouped, reverse_source
    )
    reverse_atom_matrix, reverse_atom_vector, _reverse_atom_rows = design_matrix(
        reverse_atoms, reverse_source
    )

    stacked_matrix = forward_matrix.col_join(reverse_matrix)
    stacked_vector = forward_vector.col_join(reverse_vector)
    weight_vector = sp.Matrix(active_weights)
    atom_weight_vector = sp.Matrix(atom_weights)

    spatial_grouped = [
        (name, item) for name, item in active_grouped
        if not name.endswith(":3")
    ]
    spatial_matrix, spatial_vector, spatial_rows = design_matrix(
        spatial_grouped, source
    )
    uncovered = tuple(
        row for index, row in enumerate(spatial_rows)
        if all(spatial_matrix[index, column] == 0
               for column in range(spatial_matrix.cols))
        and spatial_vector[index] != 0
    )
    witness_power = (-1, 0, -1, -1, 0, 0, 0, -1)
    witness = source[witness_power][1, 12]

    active_support = set().union(*(
        set(item) for _name, item in active_grouped
    ))
    return {
        "vertex_matches": all(vertex_matches),
        "component_counts": tuple(component_counts),
        "generic_grouped_shape": generic_matrix.shape,
        "generic_grouped_rank": dm_rank(generic_matrix),
        "generic_atom_shape": generic_atom_matrix.shape,
        "generic_atom_rank": dm_rank(generic_atom_matrix),
        "generic_atom_nullity": generic_atom_matrix.cols - dm_rank(
            generic_atom_matrix
        ),
        "active_grouped_shape": forward_matrix.shape,
        "active_grouped_rank": dm_rank(forward_matrix),
        "active_grouped_augmented_rank": dm_rank(
            forward_matrix.row_join(forward_vector)
        ),
        "active_grouped_residual": sum(
            item != 0 for item in forward_matrix * weight_vector
            - forward_vector
        ),
        "active_atom_shape": atom_matrix.shape,
        "active_atom_rank": dm_rank(atom_matrix),
        "active_atom_augmented_rank": dm_rank(
            atom_matrix.row_join(atom_vector)
        ),
        "active_atom_residual": sum(
            item != 0 for item in atom_matrix * atom_weight_vector
            - atom_vector
        ),
        "reverse_grouped_rank": dm_rank(reverse_matrix),
        "reverse_grouped_augmented_rank": dm_rank(
            reverse_matrix.row_join(reverse_vector)
        ),
        "reverse_grouped_residual": sum(
            item != 0 for item in reverse_matrix * weight_vector
            - reverse_vector
        ),
        "reverse_atom_rank": dm_rank(reverse_atom_matrix),
        "reverse_atom_augmented_rank": dm_rank(
            reverse_atom_matrix.row_join(reverse_atom_vector)
        ),
        "reverse_atom_residual": sum(
            item != 0
            for item in reverse_atom_matrix * atom_weight_vector
            - reverse_atom_vector
        ),
        "stacked_rank": dm_rank(stacked_matrix),
        "stacked_augmented_rank": dm_rank(
            stacked_matrix.row_join(stacked_vector)
        ),
        "stacked_residual": sum(
            item != 0
            for item in stacked_matrix * weight_vector - stacked_vector
        ),
        "active_weights": tuple(active_weights),
        "source_support_exact_union": set(source) == active_support,
        "spatial_shape": spatial_matrix.shape,
        "spatial_rank": dm_rank(spatial_matrix),
        "spatial_augmented_rank": dm_rank(
            spatial_matrix.row_join(spatial_vector)
        ),
        "spatial_uncovered_rows": len(uncovered),
        "temporal_witness": sp.simplify(witness),
        "actual_reverse_used": True,
        "factor_choice_cube_is_physical_cube": False,
    }


def degree_project(matrix: sp.MatrixBase, shift: int) -> sp.Matrix:
    result = sp.zeros(16)
    for row, row_form in enumerate(B.FORM_SUBSETS):
        for column, column_form in enumerate(B.FORM_SUBSETS):
            if len(row_form) - len(column_form) == shift:
                result[row, column] = matrix[row, column]
    return result


@cache
def source_census_facts() -> dict[str, object]:
    source = b206.combined_raw_source()
    reverse = reverse_polynomial(source)
    spatial = {
        power[:3] + power[4:7] for power in source
    }
    matter = {item[:3] for item in spatial}
    geometry = {item[3:] for item in spatial}
    full_matter = {power[:4] for power in source}
    full_geometry = {power[4:] for power in source}
    flattened = sp.Matrix.hstack(*(
        matrix.reshape(256, 1) for matrix in source.values()
    ))
    rank_distribution = Counter(matrix.rank() for matrix in source.values())
    nonzero_values = {
        sp.expand(value)
        for matrix in source.values() for value in matrix if value != 0
    }
    expected_values = {
        sp.Rational(1, 14), -sp.Rational(1, 14),
        sp.Rational(1, 8), -sp.Rational(1, 8),
        -sp.sqrt(2) / 28,
        sp.sqrt(2) / 16, -sp.sqrt(2) / 16,
        sp.Rational(1, 8) + sp.sqrt(2) / 16,
        sp.Rational(1, 8) - sp.sqrt(2) / 16,
        -sp.Rational(1, 8) + sp.sqrt(2) / 16,
        -sp.Rational(1, 8) - sp.sqrt(2) / 16,
    }
    degree_ranks = tuple(
        dm_rank(sp.Matrix.hstack(*(
            degree_project(matrix, shift).reshape(256, 1)
            for matrix in source.values()
        )))
        for shift in (0, 1, -1)
    )
    return {
        "forward_terms": len(source),
        "reverse_terms": len(reverse),
        "spatial_support": len(spatial),
        "matter_support": len(matter),
        "geometry_support": len(geometry),
        "max_matter_l1": max(sum(abs(x) for x in item) for item in matter),
        "max_geometry_l1": max(
            sum(abs(x) for x in item) for item in geometry
        ),
        "full_matter_support": len(full_matter),
        "full_geometry_support": len(full_geometry),
        "time_exponents": tuple(sorted({
            power[3] for power in source
        } | {
            power[7] for power in source
        })),
        "coefficient_nnz": sum(
            value != 0 for matrix in source.values() for value in matrix
        ),
        "coefficient_span_rank": dm_rank(flattened),
        "degree_ranks": degree_ranks,
        "rank_distribution": dict(rank_distribution),
        "coefficient_values_exact": nonzero_values == expected_values,
        "integer_support": all(
            isinstance(value, int) for power in source for value in power
        ),
    }


@cache
def collision_facts() -> dict[str, object]:
    incoming, transfer = b193.POINTS["H1"]
    alternative = (sp.Integer(0), sp.Integer(0), sp.Integer(0), incoming[3])
    coefficients = b193.tt_source_coefficients("H1", 1)

    def evaluated(momentum: tuple[sp.Expr, ...]) -> tuple[sp.Matrix, sp.Matrix]:
        outgoing = tuple(
            momentum[index] + transfer[index] for index in range(4)
        )
        _action, _hodge, forward_vertices = B.centered_objects(
            momentum, transfer
        )
        _raction, _rhodge, reverse_vertices = B.centered_objects(
            outgoing, tuple(-value for value in transfer)
        )
        return tuple(
            sp.expand(sum(
                (coefficients[index] * vertices[index]
                 for index in range(10)),
                sp.zeros(16),
            ))
            for vertices in (forward_vertices, reverse_vertices)
        )  # type: ignore[return-value]

    primary = evaluated(incoming)
    control = evaluated(alternative)
    differences = tuple(
        sp.expand(left - right) for left, right in zip(primary, control)
    )
    return {
        "forward_rank": differences[0].rank(),
        "forward_nnz": sum(value != 0 for value in differences[0]),
        "forward_witness": sp.factor(differences[0][0, 4]),
        "reverse_rank": differences[1].rank(),
        "reverse_nnz": sum(value != 0 for value in differences[1]),
        "reverse_witness": sp.factor(differences[1][0, 4]),
        "same_q": True,
        "p_supplied_as_label": False,
    }


@cache
def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "scope": False, "n1n8": False, "n5": False}
    text = NOTE_PATH.read_text()
    return {
        "exists": True,
        "scope": all(phrase in text for phrase in (
            "operator-factorization support",
            "same-time spatial cube",
            "actual neighboring `M2`",
            "H2 remains sealed",
            "TOE percentage movement: 0",
        )),
        "n1n8": all(f"### N{index}" in text for index in range(1, 9)),
        "n5": all(prefix in text for prefix in (
            "per_element:", "per_site:", "per_mode:",
            "per_block:", "lattice_wide:",
        )),
    }


N5_LINES = (
    "per_element: checked all 204 native factor atoms, both exact orientation signs, and the radial/handed corner-comparison formulas.",
    "per_site: checked six directed M2 edge slots and eight cubic corners; actual Record-supplied neighbor contents were not executed because no physical comparison instrument is yet derived.",
    "per_mode: checked the fixed H1 incoming/transfer mode, its same-q different-p control, and all temporal derivative groups; H2 remained sealed.",
    "per_block: checked the complete literal forward and actual-reverse H1 source against grouped and independently weighted native Laurent features.",
    "lattice_wide: checked all 24 proper-cubic representation transports and exact finite support; no full-lattice history, retained theory, axiom edit, or TOE closure was executed.",
)


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    representation = representation_facts()
    face = face_average_m2_facts()
    action = action_factorization_facts()
    source = source_census_facts()
    collision = collision_facts()
    covariance = b206.h1_cubic_covariance_facts()
    note = note_facts()

    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal_blob": GOAL_BLOB,
        "scalar_edge_hom": 0,
        "scalar_corner_hom": 1,
        "selector_mixed": False,
        "selector_covariance": True,
        "mixed_corner": True,
        "commutator_i": True,
        "generic_grouped_rank": 27,
        "weights_fitted": False,
        "actual_reverse": True,
        "forward_residual": 0,
        "reverse_residual": 0,
        "active_atom_rank": 136,
        "factor_cube_physical": False,
        "spatial_fit": False,
        "temporal_witness": sp.Rational(1, 8),
        "incoming_p_collision": True,
        "p_external_label": False,
        "exterior_is_m2": False,
        "actual_record_map": False,
        "h2_opened": False,
        "formation": False,
        "history": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_progress": False,
        "retained": False,
        "broad_no_go": False,
        "no_go_discipline": True,
    }
    mutation_map = {
        "stale_main_authority": ("main", "stale"),
        "drop_preregistration": ("prereg", False),
        "alter_goal_after_registration": ("goal_blob", "altered"),
        "claim_scalar_edge_t2": ("scalar_edge_hom", 1),
        "erase_scalar_corner_t2": ("scalar_corner_hom", 0),
        "mix_radial_and_handed_then_claim_selection": ("selector_mixed", True),
        "rotate_sites_without_bloch_vectors": ("selector_covariance", False),
        "replace_mixed_by_linear_corner_moment": ("mixed_corner", False),
        "remove_commutator_i": ("commutator_i", False),
        "erase_full_feature_rank": ("generic_grouped_rank", 26),
        "fit_h1_group_weights": ("weights_fitted", True),
        "replace_actual_reverse_by_adjoint": ("actual_reverse", False),
        "erase_forward_residual": ("forward_residual", 1),
        "erase_reverse_residual": ("reverse_residual", 1),
        "erase_atom_uniqueness": ("active_atom_rank", 135),
        "call_factor_choice_cube_physical": ("factor_cube_physical", True),
        "drop_temporal_groups_and_claim_fit": ("spatial_fit", True),
        "hide_temporal_witness": ("temporal_witness", 0),
        "erase_incoming_p_collision": ("incoming_p_collision", False),
        "supply_p_as_external_label": ("p_external_label", True),
        "identify_exterior_action_with_m2": ("exterior_is_m2", True),
        "claim_actual_record_map": ("actual_record_map", True),
        "open_h2_before_h1_ownership": ("h2_opened", True),
        "claim_formation": ("formation", True),
        "claim_history": ("history", True),
        "claim_axiom_update": ("axiom_update", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_progress": ("toe_progress", True),
        "claim_retained_status": ("retained", True),
        "claim_broad_context_no_go": ("broad_no_go", True),
        "erase_no_go_discipline": ("no_go_discipline", False),
    }
    if mutation:
        key, value = mutation_map[mutation]
        claims[key] = value

    authority_ok = (
        authority["main"] == claims["main"]
        and authority["parent"]
        and authority["prereg"] == claims["prereg"]
        and authority["goal_registered"] == claims["goal_blob"]
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom_main"] == AXIOM_BLOB
        and authority["axiom_worktree"] == AXIOM_BLOB
        and authority["registry_main"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree"] == REGISTRY_WORKTREE_BLOB
        and authority["inputs"]
    )
    representation_ok = (
        representation["proper_cubic_count"] == 24
        and representation["scalar_edge_hom"] == claims["scalar_edge_hom"]
        and representation["bloch_edge_hom"] == 2
        and representation["scalar_corner_hom"]
        == claims["scalar_corner_hom"]
        and representation["bloch_corner_hom"] == 3
        and representation["hermitian_corner_hom"] == 4
        and representation["mixed_rank"] == 3
        and representation["mixed_equivariant"] == claims["mixed_corner"]
    )
    selector_ok = (
        representation["selector_covariance"]
        == claims["selector_covariance"]
        and representation["radial_selects_odd"]
        and representation["handed_selects_even"]
        and representation["mixed_corner_even"]
        and representation["radial_parity"]
        and representation["handed_parity"]
        and representation["odd_parity_hom"] == 1
        and representation["even_parity_hom"] == 1
        and claims["selector_mixed"] is False
        and claims["commutator_i"] is True
    )
    action_ok = (
        action["vertex_matches"]
        and action["component_counts"] == (
            (4, 4, 32, 32, 60),
            (4, 4, 32, 32, 60),
            (4, 4, 32, 32, 60),
        )
        and action["generic_grouped_shape"] == (816, 27)
        and action["generic_grouped_rank"]
        == claims["generic_grouped_rank"]
        and action["generic_atom_shape"] == (816, 204)
        and action["generic_atom_rank"] == 202
        and action["generic_atom_nullity"] == 2
        and claims["weights_fitted"] is False
    )
    reconstruction_ok = (
        action["active_grouped_shape"] == (560, 18)
        and action["active_grouped_rank"] == 18
        and action["active_grouped_augmented_rank"] == 18
        and action["active_grouped_residual"]
        == claims["forward_residual"]
        and action["active_atom_shape"] == (560, 136)
        and action["active_atom_rank"] == claims["active_atom_rank"]
        and action["active_atom_augmented_rank"] == 136
        and action["active_atom_residual"] == 0
        and action["reverse_grouped_rank"] == 18
        and action["reverse_grouped_augmented_rank"] == 18
        and action["reverse_grouped_residual"]
        == claims["reverse_residual"]
        and action["reverse_atom_rank"] == 136
        and action["reverse_atom_augmented_rank"] == 136
        and action["reverse_atom_residual"] == 0
        and action["stacked_rank"] == 18
        and action["stacked_augmented_rank"] == 18
        and action["stacked_residual"] == 0
        and action["actual_reverse_used"] == claims["actual_reverse"]
        and action["factor_choice_cube_is_physical_cube"]
        == claims["factor_cube_physical"]
    )
    census_ok = (
        action["source_support_exact_union"]
        and source["forward_terms"] == 110
        and source["reverse_terms"] == 110
        and source["spatial_support"] == 78
        and source["matter_support"] == 38
        and source["geometry_support"] == 26
        and source["max_matter_l1"] == 3
        and source["max_geometry_l1"] == 3
        and source["full_matter_support"] == 54
        and source["full_geometry_support"] == 38
        and source["time_exponents"] == (-1, 0, 1)
        and source["coefficient_nnz"] == 560
        and source["coefficient_span_rank"] == 18
        and source["degree_ranks"] == (2, 8, 8)
        and source["rank_distribution"] == {4: 80, 6: 4, 8: 24, 12: 2}
        and source["coefficient_values_exact"]
        and source["integer_support"]
    )
    boundary_ok = (
        action["spatial_shape"] == (560, 14)
        and action["spatial_rank"] == 14
        and action["spatial_augmented_rank"]
        == (14 if claims["spatial_fit"] else 15)
        and action["spatial_uncovered_rows"] == 128
        and action["temporal_witness"] == claims["temporal_witness"]
        and collision["same_q"]
        and (collision["forward_rank"] == 12)
        == claims["incoming_p_collision"]
        and collision["forward_nnz"] == 56
        and collision["reverse_rank"] == 12
        and collision["reverse_nnz"] == 56
        and sp.simplify(
            collision["forward_witness"]
            - I * (1 + sp.sqrt(3)) / 8
        ) == 0
        and sp.simplify(
            collision["reverse_witness"]
            - I * (5 - sp.sqrt(3)) / 8
        ) == 0
        and collision["p_supplied_as_label"] == claims["p_external_label"]
    )
    covariance_ok = (
        covariance["proper_cubic_count"] == 24
        and covariance["forward_source_covariance"]
        and covariance["actual_reverse_source_covariance"]
        and covariance["translation_covariance"]
        and representation["selector_covariance"]
    )
    m2_scope_ok = (
        face["map_rank"] == 12
        and face["equivariant"]
        and face["odd_map_rank"] == 3
        and face["even_map_zero"]
        and face["odd_output"] == face["target_shear"]
        and face["even_output"] == (0, 0, 0)
        and face["max_corner_norm_square"]
        == (3 + sp.sqrt(2)) / 16
        and face["max_face_norm_square"] == sp.Rational(3, 32)
        and face["strict_corner_density_positive"]
        and face["strict_face_density_positive"]
        and face["action_derived_contents"] == claims["actual_record_map"]
        and claims["exterior_is_m2"] is False
    )
    scope_ok = (
        claims["h2_opened"] is False
        and claims["formation"] is False
        and claims["history"] is False
        and claims["axiom_update"] is False
        and claims["obligation_retirement"] == 0
        and claims["toe_progress"] is False
        and claims["retained"] is False
        and claims["broad_no_go"] is False
        and claims["no_go_discipline"] is True
        and note["exists"] and note["scope"]
        and note["n1n8"] and note["n5"]
    )
    return {
        "A": (authority_ok, "current authority and immutable Block-207 registration are pinned"),
        "B": (representation_ok, "the scalar corner cube has one exact T2 channel while scalar edges have none"),
        "C": (selector_ok, "radial/Jordan and handed/commutator corner scores select the odd and even decoder classes exactly"),
        "D": (action_ok, "all three T2 action vertices split into independent native corner-average and oriented-difference groups"),
        "E": (reconstruction_ok, "the H1 forward and actual-reverse sources have one shared exact grouped and atom-level reconstruction"),
        "F": (census_ok, "all 110 Laurent coefficients, support classes, matrix ranks, and form-degree channels are accounted for"),
        "G": (boundary_ok, "a same-time spatial cube misses load-bearing temporal groups and q alone misses incoming-p dependence"),
        "H": (covariance_ok, "the source and edge/corner selectors pass all 24 simultaneous proper-cubic frames and translations"),
        "I": (m2_scope_ok, "a positive H1 corner-M2 consistency witness selects the odd shear without claiming action-derived Record contents"),
        "J": (scope_ok, "the result is operator-factorization support with a scoped temporal/M2 wall, not H2, formation, axiom, retained, or TOE closure"),
    }


def mutation_sweep() -> int:
    failures = []
    for mutation in MUTATIONS:
        checks = evaluate(mutation)
        if all(passed for passed, _message in checks.values()):
            failures.append(mutation)
    print(
        f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(failures)} "
        f"FAIL={len(failures)}"
    )
    if failures:
        print("MUTATION_SURVIVORS:", ",".join(failures))
        return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        return mutation_sweep()
    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(ok)
    representation = representation_facts()
    action = action_factorization_facts()
    source = source_census_facts()
    collision = collision_facts()
    print(
        "CORNER_HOM: scalar/Bloch/Hermitian-M2 -> T2 dimensions="
        f"{representation['scalar_corner_hom']}/"
        f"{representation['bloch_corner_hom']}/"
        f"{representation['hermitian_corner_hom']}; "
        "radial->odd; handed->even; parity-restricted dims=1/1."
    )
    print(
        "ACTION_FACTORIZATION: generic grouped rank=27/27; "
        "H1 grouped rank=18/18 and atom rank=136/136; "
        "forward/reverse stacked residual=0."
    )
    print(
        "SOURCE_CENSUS: forward/reverse terms=110/110; spatial="
        f"{source['spatial_support']}; p/q supports="
        f"{source['matter_support']}/{source['geometry_support']}; "
        "max L1=3/3; coefficient span=18."
    )
    print(
        "SPATIAL_TIME_GATE: same-time rank/augmented=14/15; "
        f"uncovered={action['spatial_uncovered_rows']}; "
        "first temporal coefficient witness=1/8."
    )
    print(
        "P_COLLISION: forward/reverse rank=12/12; nnz=56/56; "
        f"witnesses={collision['forward_witness']},"
        f"{collision['reverse_witness']}."
    )
    print(
        "RESULT: native one-hop edge/corner operator factorization and odd/even "
        "selector are exact; physical Record-supplied clock/M2 contents remain "
        "open; obligation_retirement=0; TOE movement=0."
    )
    for line in N5_LINES:
        print(line)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
