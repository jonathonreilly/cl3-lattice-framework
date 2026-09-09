#!/usr/bin/env python3
"""Block 190: full-band Schur gate and a 4D DK/Ward/TT/mark slice.

The runner first closes the deliberately capped two-dimensional regression:
the full five-band action has exact positive reflection-paired Schur graphs,
but the frozen-chart graphs do not intertwine the inherited one-site spatial
shift.  It then constructs a genuine 16-form, four-dimensional finite-Laurent
Dirac--Kahler symbol.  One local metric vertex supplies an exact coefficient-
wise total Ward identity with reciprocal matter recoil, couples with rank two
to the two positive gravity TT directions, and is separated by a fixed finite
family of local one-body mark contexts on three spatial momentum strata.  The
marks see only the mass--Hodge part of that image and are exactly blind to the
degree-changing derivative/recoil part.

The mark calculation is a candidate readout diagnostic, not a permanent
Record write, probability law, nonlinear completion, or TOE closure.
"""

from __future__ import annotations

import argparse
from itertools import permutations, product
from pathlib import Path
import re
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_common_action_stationarity_gravity_stage_orientation_boundary_2026_08_24 as b187  # noqa: E402
import admissibility_dirac_kahler_dual_frame_temporal_link_stage_intertwiner_boundary_2026_08_24 as b188  # noqa: E402
import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_REF = (
    "origin/physics-loop/toe-axiom-closure-block189-compatible-positive-"
    "involution-20260824"
)
PARENT_COMMIT = "98d544ae8e94a78d986c96c65cfe3f588801ba3e"
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_COMMON_ACTION_STATIONARITY_GRAVITY_STAGE_ORIENTATION_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_common_action_stationarity_gravity_stage_orientation_boundary_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_DUAL_FRAME_TEMPORAL_LINK_STAGE_INTERTWINER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_dual_frame_temporal_link_stage_intertwiner_boundary_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_STAGE_EXCHANGE_POSITIVE_DRESSING_SOURCE_PORT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_dirac_kahler_stage_exchange_positive_dressing_source_port_boundary_2026_08_24.py",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
    "docs/ADMISSIBILITY_INCIDENCE_FIERZ_PAULI_SIGNED_RECORD_SOURCE_FULL_TENSOR_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_incidence_fierz_pauli_signed_record_source_full_tensor_cadence_boundary_2026_08_14.py",
    "docs/ADMISSIBILITY_INCIDENCE_SCALAR_GRAPH_MATTER_FIRST_ORDER_TOTAL_WARD_CADENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/admissibility_incidence_scalar_graph_matter_first_order_total_ward_cadence_boundary_2026_08_14.py",
)

MUTATIONS = (
    "stale_main_authority",
    "drop_distance_two_band",
    "claim_schur_spatial_covariance",
    "break_exterior_car",
    "break_raw_locality",
    "break_total_ward",
    "break_cubic_covariance",
    "break_gravity_tt",
    "claim_form_degree_reads_tt",
    "claim_one_context_reads_all_tt",
    "claim_marks_read_recoil",
    "claim_permanent_record_write",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "drop_distance_two_band": "B",
    "claim_schur_spatial_covariance": "B",
    "break_exterior_car": "C",
    "break_raw_locality": "C",
    "break_total_ward": "D",
    "break_cubic_covariance": "D",
    "break_gravity_tt": "E",
    "claim_form_degree_reads_tt": "F",
    "claim_one_context_reads_all_tt": "F",
    "claim_marks_read_recoil": "F",
    "claim_permanent_record_write": "G",
    "claim_toe_progress": "G",
}

I = sp.I
R = sp.Rational
SQRT2 = sp.sqrt(2)
MASS = R(2, 7)
ZERO_EXPONENT = (0,) * 8


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def worktree_blob(path: str) -> str:
    result = subprocess.run(
        ("git", "hash-object", "--", path), cwd=ROOT, text=True,
        capture_output=True, check=False, timeout=AUDIT_TIMEOUT_SEC,
    )
    return result.stdout.strip() if result.returncode == 0 else ""


def is_ancestor(ancestor: str, descendant: str = "HEAD") -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, descendant),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.expand(entry) == 0 for entry in left - right
    )


def nonzero_entries(matrix: sp.MatrixBase) -> int:
    return sum(entry != 0 for entry in matrix)


def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent": git_output("rev-parse", PARENT_REF),
        "parent_ancestor": is_ancestor(PARENT_COMMIT),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def positive_leading_minors(matrix: sp.Matrix) -> tuple[bool, tuple[int, ...]]:
    signs = tuple(
        int(sp.sign(sp.factor(matrix[:size, :size].det(method="domain-ge"))))
        for size in range(1, matrix.rows + 1)
    )
    return all(sign == 1 for sign in signs), signs


def frame_schur_facts(name: str, hodge: sp.Matrix) -> dict[str, object]:
    identity_ap = sp.eye(16)
    injection = sp.Matrix.vstack(-identity_ap, identity_ap)
    selection = sp.Matrix.hstack(sp.zeros(16), identity_ap)
    reflection_cover = sp.expand(b188.edge_reflection() * b188.time_parity())
    reflection = sp.expand(selection * reflection_cover * injection)
    differential = b128.chart_differential_cover((0, 0))
    action_cover = b188.completion(hodge, differential)
    full_five_band = sp.expand(sum(
        (b188.temporal_band(action_cover, displacement)
         for displacement in (-2, -1, 0, 1, 2)),
        sp.zeros(action_cover.rows),
    ))
    action = sp.expand(selection * full_five_band * injection)

    embedding_n = sp.eye(16)[:, :8]
    embedding_p = sp.eye(16)[:, 8:]
    a_block = embedding_n.T * action * embedding_n
    b_block = embedding_n.T * action * embedding_p
    c_block = embedding_p.T * action * embedding_n
    d_block = embedding_p.T * action * embedding_p
    d_inverse = d_block.inv(method="DM")
    schur = sp.expand(a_block - b_block * d_inverse * c_block)
    right_graph = sp.expand(
        embedding_n - embedding_p * d_inverse * c_block
    )
    left_graph = sp.expand(
        embedding_n - embedding_p * d_block.T.inv(method="DM") * b_block.T
    )

    dual = sp.expand(reflection * action * reflection.T)
    dual_adjoint = dual.T
    zero_ap = sp.zeros(16)
    doubled_reflection = sp.Matrix.vstack(
        sp.Matrix.hstack(zero_ap, reflection.T),
        sp.Matrix.hstack(reflection, zero_ap),
    )
    doubled_action_inverse = sp.diag(
        action.inv(method="DM"), dual_adjoint.inv(method="DM")
    )
    reflected_kernel = sp.expand(doubled_reflection * doubled_action_inverse)

    plus_port = sp.Matrix.vstack(
        right_graph, sp.expand(reflection * right_graph.conjugate())
    )
    minus_port = sp.Matrix.vstack(
        right_graph, sp.expand(-reflection * right_graph.conjugate())
    )
    plus_gram = sp.expand(plus_port.H * reflected_kernel * plus_port)
    minus_gram = sp.expand(minus_port.H * reflected_kernel * minus_port)
    plus_positive, plus_signs = positive_leading_minors(plus_gram)
    minus_negative, minus_signs = positive_leading_minors(-minus_gram)

    shift = sp.expand(
        selection * b188.cover_shift(0, 1) * injection
    )
    shift_n = sp.expand(embedding_n.T * shift * embedding_n)
    action_shift = sp.expand(action * shift - shift * action)
    right_shift = sp.expand(shift * right_graph - right_graph * shift_n)
    left_shift = sp.expand(shift * left_graph - left_graph * shift_n)

    return {
        "name": name,
        "five_band_complete": matrix_equal(full_five_band, action_cover),
        "distance_two_live": all(
            nonzero_entries(b188.temporal_band(action_cover, displacement)) > 0
            for displacement in (-2, 2)
        ),
        "block_ranks": tuple(
            block.rank() for block in
            (a_block, b_block, c_block, d_block, schur)
        ),
        "right_identity": matrix_equal(
            action * right_graph, embedding_n * schur
        ),
        "left_identity": matrix_equal(
            left_graph.T * action, schur * embedding_n.T
        ),
        "bi_identity": matrix_equal(
            left_graph.T * action * right_graph, schur
        ),
        "inverse_identity": matrix_equal(
            (action.inv(method="DM")).extract(range(8), range(8)),
            schur.inv(method="DM"),
        ),
        "left_right_difference": (
            nonzero_entries(right_graph - left_graph),
            (right_graph - left_graph).rank(),
        ),
        "kernel_hermitian": matrix_equal(
            reflected_kernel, reflected_kernel.H
        ),
        "reflection_ports": (
            matrix_equal(
                doubled_reflection * plus_port.conjugate(), plus_port
            ),
            matrix_equal(
                doubled_reflection * minus_port.conjugate(), -minus_port
            ),
        ),
        "gram_hermitian": (
            matrix_equal(plus_gram, plus_gram.H),
            matrix_equal(minus_gram, minus_gram.H),
        ),
        "gram_ranks": (plus_gram.rank(), minus_gram.rank()),
        "plus_positive": plus_positive,
        "minus_negative": minus_negative,
        "plus_signs": plus_signs,
        "minus_signs": minus_signs,
        "action_shift": (
            nonzero_entries(action_shift), action_shift.rank()
        ),
        "right_shift": (
            nonzero_entries(right_shift), right_shift.rank()
        ),
        "left_shift": (
            nonzero_entries(left_shift), left_shift.rank()
        ),
    }


def schur_facts() -> tuple[dict[str, object], ...]:
    field = b128.block105.overlap_field()
    landed_hodge = b188.hodge_cover(field)
    spatial_shift = b188.cover_shift(0, 1)
    minimal_hodge = sp.expand(
        (landed_hodge + spatial_shift.T * landed_hodge * spatial_shift) / 2
    )
    orbit_hodge = b188.orbit_average(landed_hodge)
    return (
        frame_schur_facts("minimal", minimal_hodge),
        frame_schur_facts("orbit", orbit_hodge),
    )


FORM_SUBSETS = tuple(
    tuple(axis for axis in range(4) if mask & (1 << axis))
    for mask in range(16)
)
FORM_INDEX = {subset: index for index, subset in enumerate(FORM_SUBSETS)}


def exterior_creation(axis: int) -> sp.Matrix:
    result = sp.zeros(16)
    for column, subset in enumerate(FORM_SUBSETS):
        if axis in subset:
            continue
        target = tuple(sorted(subset + (axis,)))
        sign = (-1) ** sum(item < axis for item in subset)
        result[FORM_INDEX[target], column] = sign
    return result


CREATION = tuple(exterior_creation(axis) for axis in range(4))
ANNIHILATION = tuple(matrix.T for matrix in CREATION)
NUMBER = tuple(
    CREATION[axis] * ANNIHILATION[axis] for axis in range(4)
)
IDENTITY_FORM = sp.eye(16)
PAIRS4 = (
    (3, 3), (0, 0), (1, 1), (2, 2),
    (0, 3), (1, 3), (2, 3),
    (0, 1), (0, 2), (1, 2),
)
SPATIAL_SLOTS = (1, 2, 3, 7, 8, 9)


def centered_differential(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.expand(sum(
        (sp.sin(momentum[axis]) * CREATION[axis] for axis in range(4)),
        sp.zeros(16),
    ))


def centered_objects(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[sp.Matrix, tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    differential_0 = centered_differential(incoming)
    differential_1 = centered_differential(outgoing)
    action = sp.expand(
        MASS * IDENTITY_FORM
        + I * (differential_0 + differential_0.T)
    )
    cosines = tuple(
        sp.cos(incoming[axis] + transfer[axis] / 2)
        for axis in range(4)
    )
    hodge_vertices: list[sp.Matrix] = []
    for left, right in PAIRS4:
        if left == right:
            vertex = cosines[left] ** 2 * (
                R(1, 2) * IDENTITY_FORM - NUMBER[left]
            )
        else:
            vertex = -cosines[left] * cosines[right] / SQRT2 * (
                CREATION[left] * ANNIHILATION[right]
                + CREATION[right] * ANNIHILATION[left]
            )
        hodge_vertices.append(sp.expand(vertex))
    action_vertices = tuple(
        sp.expand(
            MASS * vertex
            + I * (
                vertex * differential_0
                + differential_1.T * vertex
            )
        )
        for vertex in hodge_vertices
    )
    return action, tuple(hodge_vertices), action_vertices


def centered_gauge(transfer: tuple[sp.Expr, ...]) -> sp.Matrix:
    incidence = tuple(2 * sp.sin(item / 2) for item in transfer)
    result = sp.zeros(10, 4)
    for row, (left, right) in enumerate(PAIRS4):
        for column in range(4):
            if left == right:
                result[row, column] = (
                    2 * incidence[left] if column == left else 0
                )
            else:
                result[row, column] = SQRT2 * (
                    (incidence[left] if column == right else 0)
                    + (incidence[right] if column == left else 0)
                )
    return result


def centered_ward_facts() -> dict[str, object]:
    incoming = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.pi / 4)
    transfer = (sp.pi / 2, sp.pi / 2, sp.pi / 2, sp.Integer(0))
    action_0, hodge_vertices, action_vertices = centered_objects(
        incoming, transfer
    )
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    differential_0 = centered_differential(incoming)
    differential_1 = centered_differential(outgoing)
    action_1 = sp.expand(
        MASS * IDENTITY_FORM
        + I * (differential_1 + differential_1.T)
    )
    gauge = centered_gauge(transfer)
    cosines = tuple(
        sp.cos(incoming[axis] + transfer[axis] / 2)
        for axis in range(4)
    )
    hodge_residuals = []
    ward_residuals = []
    for axis in range(4):
        contraction = cosines[axis] * ANNIHILATION[axis]
        right_recoil = sp.expand(
            differential_1 * contraction
            + contraction * differential_0
        )
        left_recoil = sp.expand(
            (differential_0 * contraction
             + contraction * differential_1).T
        )
        contracted_hodge = sp.expand(sum(
            (gauge[row, axis] * hodge_vertices[row] for row in range(10)),
            sp.zeros(16),
        ))
        contracted_vertex = sp.expand(sum(
            (gauge[row, axis] * action_vertices[row] for row in range(10)),
            sp.zeros(16),
        ))
        hodge_residuals.append(sp.expand(
            contracted_hodge - (left_recoil - right_recoil)
        ))
        ward_residuals.append(sp.expand(
            contracted_vertex
            + action_1 * right_recoil
            - left_recoil * action_0
        ))
    return {
        "hodge_residuals": tuple(nonzero_entries(item) for item in hodge_residuals),
        "ward_residuals": tuple(nonzero_entries(item) for item in ward_residuals),
        "action_ranks": (action_0.rank(), action_1.rank()),
        "mass_hermitian": (
            matrix_equal((action_0 + action_0.H) / 2, MASS * IDENTITY_FORM),
            matrix_equal((action_1 + action_1.H) / 2, MASS * IDENTITY_FORM),
        ),
    }


PolyMatrix = dict[tuple[int, ...], sp.Matrix]


def exponent(
    matter: dict[int, int] | None = None,
    geometry: dict[int, int] | None = None,
) -> tuple[int, ...]:
    result = [0] * 8
    for axis, value in (matter or {}).items():
        result[axis] += value
    for axis, value in (geometry or {}).items():
        result[4 + axis] += value
    return tuple(result)


def poly_clean(polynomial: PolyMatrix) -> PolyMatrix:
    result: PolyMatrix = {}
    for power, matrix in polynomial.items():
        expanded = sp.expand(matrix)
        if any(entry != 0 for entry in expanded):
            result[power] = expanded
    return result


def poly_add(*polynomials: PolyMatrix) -> PolyMatrix:
    result: PolyMatrix = {}
    for polynomial in polynomials:
        for power, matrix in polynomial.items():
            result[power] = result.get(power, sp.zeros(16)) + matrix
    return poly_clean(result)


def poly_scale(polynomial: PolyMatrix, scalar: sp.Expr) -> PolyMatrix:
    return poly_clean({power: scalar * matrix for power, matrix in polynomial.items()})


def poly_multiply(left: PolyMatrix, right: PolyMatrix) -> PolyMatrix:
    result: PolyMatrix = {}
    for left_power, left_matrix in left.items():
        for right_power, right_matrix in right.items():
            power = tuple(
                left_power[index] + right_power[index] for index in range(8)
            )
            result[power] = result.get(power, sp.zeros(16)) + left_matrix * right_matrix
    return poly_clean(result)


def poly_transpose(polynomial: PolyMatrix) -> PolyMatrix:
    return {power: matrix.T for power, matrix in polynomial.items()}


def scalar_poly(terms: dict[tuple[int, ...], sp.Expr]) -> PolyMatrix:
    return poly_clean({
        power: value * IDENTITY_FORM for power, value in terms.items()
    })


def placed_cosine(axis: int) -> PolyMatrix:
    return scalar_poly({
        exponent({axis: 1}, {axis: 1}): R(1, 2),
        exponent({axis: -1}): R(1, 2),
    })


def cosine_square(axis: int) -> PolyMatrix:
    return scalar_poly({
        exponent({axis: 2}, {axis: 1}): R(1, 4),
        ZERO_EXPONENT: R(1, 2),
        exponent({axis: -2}, {axis: -1}): R(1, 4),
    })


def raw_polynomial_facts() -> dict[str, object]:
    differential_0: PolyMatrix = {}
    differential_1: PolyMatrix = {}
    for axis in range(4):
        differential_0 = poly_add(differential_0, {
            exponent({axis: 1}): CREATION[axis] / (2 * I),
            exponent({axis: -1}): -CREATION[axis] / (2 * I),
        })
        differential_1 = poly_add(differential_1, {
            exponent({axis: 1}, {axis: 1}): CREATION[axis] / (2 * I),
            exponent({axis: -1}, {axis: -1}): -CREATION[axis] / (2 * I),
        })
    action_0 = poly_add(
        {ZERO_EXPONENT: MASS * IDENTITY_FORM},
        poly_scale(poly_add(differential_0, poly_transpose(differential_0)), I),
    )
    action_1 = poly_add(
        {ZERO_EXPONENT: MASS * IDENTITY_FORM},
        poly_scale(poly_add(differential_1, poly_transpose(differential_1)), I),
    )

    hodge_vertices: list[PolyMatrix] = []
    action_vertices: list[PolyMatrix] = []
    for left, right in PAIRS4:
        if left == right:
            hodge = poly_multiply(
                cosine_square(left),
                {ZERO_EXPONENT: R(1, 2) * IDENTITY_FORM - NUMBER[left]},
            )
        else:
            hodge = poly_multiply(
                poly_scale(
                    poly_multiply(placed_cosine(left), placed_cosine(right)),
                    -1 / SQRT2,
                ),
                {ZERO_EXPONENT: (
                    CREATION[left] * ANNIHILATION[right]
                    + CREATION[right] * ANNIHILATION[left]
                )},
            )
        vertex = poly_add(
            poly_scale(hodge, MASS),
            poly_scale(poly_add(
                poly_multiply(hodge, differential_0),
                poly_multiply(poly_transpose(differential_1), hodge),
            ), I),
        )
        hodge_vertices.append(hodge)
        action_vertices.append(vertex)

    def gauge_minus_transpose(slot: int, axis: int) -> PolyMatrix:
        left, right = PAIRS4[slot]
        if left == right:
            if axis != left:
                return {}
            return scalar_poly({
                ZERO_EXPONENT: 2,
                exponent(geometry={left: 1}): -2,
            })
        if axis == right:
            return scalar_poly({
                exponent(geometry={left: -1}): SQRT2,
                ZERO_EXPONENT: -SQRT2,
            })
        if axis == left:
            return scalar_poly({
                exponent(geometry={right: -1}): SQRT2,
                ZERO_EXPONENT: -SQRT2,
            })
        return {}

    ward_residual_terms = []
    recoil_support: set[tuple[int, ...]] = set()
    for axis in range(4):
        gauge_vertex: PolyMatrix = {}
        for slot in range(10):
            gauge_vertex = poly_add(
                gauge_vertex,
                poly_multiply(
                    gauge_minus_transpose(slot, axis), action_vertices[slot]
                ),
            )
        placed_contraction = poly_multiply(
            placed_cosine(axis),
            {ZERO_EXPONENT: ANNIHILATION[axis]},
        )
        right_recoil = poly_scale(poly_add(
            poly_multiply(differential_1, placed_contraction),
            poly_multiply(placed_contraction, differential_0),
        ), -I)
        left_recoil = poly_scale(poly_transpose(poly_add(
            poly_multiply(differential_0, placed_contraction),
            poly_multiply(placed_contraction, differential_1),
        )), I)
        recoil_support.update(right_recoil)
        recoil_support.update(left_recoil)
        residual = poly_add(
            gauge_vertex,
            poly_multiply(action_1, right_recoil),
            poly_multiply(left_recoil, action_0),
        )
        ward_residual_terms.append((
            len(residual),
            sum(nonzero_entries(matrix) for matrix in residual.values()),
        ))

    def support_shape(powers: set[tuple[int, ...]]) -> tuple[int, ...]:
        return (
            len(powers),
            max(max(abs(power[index]) for index in range(4)) for power in powers),
            max(sum(abs(power[index]) for index in range(4)) for power in powers),
            max(max(abs(power[4 + index]) for index in range(4)) for power in powers),
            max(sum(abs(power[4 + index]) for index in range(4)) for power in powers),
            max(sum(abs(item) for item in power) for power in powers),
        )

    hodge_support = set().union(*(set(item) for item in hodge_vertices))
    vertex_support = set().union(*(set(item) for item in action_vertices))
    return {
        "ward_residual_terms": tuple(ward_residual_terms),
        "action_in_shape": support_shape(set(action_0)),
        "action_out_shape": support_shape(set(action_1)),
        "action_endpoint_union_shape": support_shape(set(action_0) | set(action_1)),
        "hodge_shape": support_shape(hodge_support),
        "vertex_shape": support_shape(vertex_support),
        "recoil_shape": support_shape(recoil_support),
        "hodge_terms": tuple(len(item) for item in hodge_vertices),
        "vertex_terms": tuple(len(item) for item in action_vertices),
        "integer_support": all(
            isinstance(component, int)
            for support in (set(action_0), hodge_support, vertex_support, recoil_support)
            for power in support for component in power
        ),
    }


def tensor_basis4() -> tuple[sp.Matrix, ...]:
    result = []
    for left, right in PAIRS4:
        matrix = sp.zeros(4)
        value = 1 if left == right else 1 / SQRT2
        matrix[left, right] = value
        matrix[right, left] = value
        result.append(matrix)
    return tuple(result)


TENSOR_BASIS4 = tensor_basis4()


def wedge_representation(transform: sp.Matrix) -> sp.Matrix:
    result = sp.zeros(16)
    for column, subset in enumerate(FORM_SUBSETS):
        images: list[int] = []
        coefficient = sp.Integer(1)
        for old_axis in subset:
            rows = [row for row in range(4) if transform[row, old_axis] != 0]
            new_axis = rows[0]
            coefficient *= transform[new_axis, old_axis]
            images.append(new_axis)
        inversions = sum(
            images[left] > images[right]
            for left in range(len(images))
            for right in range(left + 1, len(images))
        )
        coefficient *= (-1) ** inversions
        result[FORM_INDEX[tuple(sorted(images))], column] = coefficient
    return result


def tensor_representation(transform: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(10, 10, lambda row, column: sp.trace(
        TENSOR_BASIS4[row].T
        * transform * TENSOR_BASIS4[column] * transform.T
    ))


def covariance_facts() -> dict[str, object]:
    incoming = sp.Matrix((0, 0, 0, sp.pi / 4))
    transfer = sp.Matrix((sp.pi / 2, sp.pi / 2, sp.pi / 2, 0))
    action, hodge, vertex = centered_objects(tuple(incoming), tuple(transfer))
    rotations = []
    for permutation in permutations(range(3)):
        permutation_matrix = sp.zeros(3)
        for row, column in enumerate(permutation):
            permutation_matrix[row, column] = 1
        for signs in product((-1, 1), repeat=3):
            candidate = sp.diag(*signs) * permutation_matrix
            if candidate.det() == 1:
                rotations.append(candidate)
    transforms = []
    for spatial in rotations:
        full = sp.eye(4)
        full[:3, :3] = spatial
        transforms.append(full)
    transforms.append(sp.diag(1, 1, 1, -1))

    failures = []
    for transform in transforms:
        form_transform = wedge_representation(transform)
        tensor_transform = tensor_representation(transform)
        transformed_action, transformed_hodge, transformed_vertex = centered_objects(
            tuple(transform * incoming), tuple(transform * transfer)
        )
        action_ok = matrix_equal(
            transformed_action,
            form_transform * action * form_transform.T,
        )
        hodge_ok = all(matrix_equal(
            sum(
                (tensor_transform[row, column] * transformed_hodge[row]
                 for row in range(10)),
                sp.zeros(16),
            ),
            form_transform * hodge[column] * form_transform.T,
        ) for column in range(10))
        vertex_ok = all(matrix_equal(
            sum(
                (tensor_transform[row, column] * transformed_vertex[row]
                 for row in range(10)),
                sp.zeros(16),
            ),
            form_transform * vertex[column] * form_transform.T,
        ) for column in range(10))
        failures.append((not action_ok, not hodge_ok, not vertex_ok))
    return {
        "proper_cubic_count": len(rotations),
        "transform_count": len(transforms),
        "failures": tuple(failures),
    }


def symmetric_basis3() -> tuple[sp.Matrix, ...]:
    result = []
    for left, right in ((0, 0), (1, 1), (2, 2), (0, 1), (0, 2), (1, 2)):
        matrix = sp.zeros(3)
        value = 1 if left == right else 1 / SQRT2
        matrix[left, right] = value
        matrix[right, left] = value
        result.append(matrix)
    return tuple(result)


SYMMETRIC_BASIS3 = symmetric_basis3()


def tt_basis(spatial_incidence: sp.Matrix) -> sp.Matrix:
    rows = [sp.Matrix([[sp.trace(item) for item in SYMMETRIC_BASIS3]])]
    for axis in range(3):
        rows.append(sp.Matrix([[
            (item * spatial_incidence)[axis] for item in SYMMETRIC_BASIS3
        ]]))
    constraint = sp.Matrix.vstack(*rows)
    spatial_section = sp.Matrix.hstack(*constraint.nullspace())
    embedding = sp.zeros(10, 6)
    for column, row in enumerate(SPATIAL_SLOTS):
        embedding[row, column] = 1
    return sp.expand(embedding * spatial_section)


def mark_context_facts() -> dict[str, object]:
    context_checks = []
    contexts = [tuple(NUMBER)]
    union_marks = list(NUMBER)
    for left in range(4):
        for right in range(left + 1, 4):
            shear = (
                CREATION[left] * ANNIHILATION[right]
                + CREATION[right] * ANNIHILATION[left]
            )
            plus = sp.expand((NUMBER[left] + NUMBER[right] + shear) / 2)
            minus = sp.expand((NUMBER[left] + NUMBER[right] - shear) / 2)
            others = [NUMBER[axis] for axis in range(4) if axis not in (left, right)]
            context = [plus, minus] + others
            context_checks.append(bool(
                matrix_equal(plus * plus, plus)
                and matrix_equal(minus * minus, minus)
                and all(matrix_equal(a * b, b * a) for a in context for b in context)
            ))
            contexts.append(tuple(context))
            union_marks.append(shear)
    return {
        "contexts": len(context_checks) + 1,
        "context_checks": tuple(context_checks),
        "context_marks": tuple(contexts),
        "union_marks": tuple(union_marks),
    }


def stratum_facts(active_spatial_axes: int) -> dict[str, object]:
    incoming = (sp.Integer(0), sp.Integer(0), sp.Integer(0), sp.pi / 4)
    transfer = tuple(
        sp.pi / 2 if axis < active_spatial_axes else sp.Integer(0)
        for axis in range(3)
    ) + (sp.Integer(0),)
    _action, hodge, vertices = centered_objects(incoming, transfer)
    spatial_incidence = sp.Matrix(tuple(
        2 * sp.sin(transfer[axis] / 2) for axis in range(3)
    ))
    section = tt_basis(spatial_incidence)
    tt_vertices = tuple(sp.expand(sum(
        (section[row, column] * vertices[row] for row in range(10)),
        sp.zeros(16),
    )) for column in range(2))
    tt_hodge = tuple(sp.expand(sum(
        (section[row, column] * hodge[row] for row in range(10)),
        sp.zeros(16),
    )) for column in range(2))
    tt_derivative = tuple(
        sp.expand(tt_vertices[column] - MASS * tt_hodge[column])
        for column in range(2)
    )
    flattened = sp.Matrix.hstack(*(
        matrix.reshape(256, 1) for matrix in tt_vertices
    ))
    diagonal = sp.Matrix([
        [matrix[index, index] for matrix in tt_vertices]
        for index in range(16)
    ])
    occupation = sp.Matrix([
        [sp.trace(mark * matrix) for matrix in tt_vertices]
        for mark in NUMBER
    ])
    form_degree = sp.Matrix([
        [sum(
            matrix[index, index]
            for index, subset in enumerate(FORM_SUBSETS)
            if len(subset) == degree
        ) for matrix in tt_vertices]
        for degree in range(5)
    ])
    contexts = mark_context_facts()
    context_union = sp.Matrix([
        [sp.trace(mark * matrix) for matrix in tt_vertices]
        for mark in contexts["union_marks"]
    ])
    individual_context_ranks = tuple(sp.Matrix([
        [sp.trace(mark * matrix) for matrix in tt_vertices]
        for mark in context
    ]).rank() for context in contexts["context_marks"])
    form_projectors = tuple(sp.diag(*(
        1 if len(subset) == degree else 0
        for subset in FORM_SUBSETS
    )) for degree in range(5))
    declared_marks = tuple(
        mark
        for context in contexts["context_marks"]
        for mark in context
    ) + form_projectors
    mark_derivative_zero = all(
        sp.expand(sp.trace(mark * matrix)) == 0
        for mark in declared_marks
        for matrix in tt_derivative
    )
    massless_context_rank = sp.Matrix([
        [sp.trace(mark * matrix) for matrix in tt_derivative]
        for mark in contexts["union_marks"]
    ]).rank()
    massless_occupation_rank = sp.Matrix([
        [sp.trace(mark * matrix) for matrix in tt_derivative]
        for mark in NUMBER
    ]).rank()
    massless_form_degree_rank = sp.Matrix([
        [sp.trace(mark * matrix) for matrix in tt_derivative]
        for mark in form_projectors
    ]).rank()
    massless_flattened = sp.Matrix.hstack(*(
        matrix.reshape(256, 1) for matrix in tt_derivative
    ))

    full_momentum = sp.Matrix(tuple(spatial_incidence) + (0,))
    gravity = b187.centered_operator4(full_momentum)
    gravity_gauge = b187.centered_gauge4(full_momentum)
    tt_gravity = sp.expand(section.T * gravity * section)
    gravity_positive, gravity_signs = positive_leading_minors(tt_gravity)
    gravity_minors = tuple(
        sp.factor(tt_gravity[:size, :size].det(method="domain-ge"))
        for size in range(1, tt_gravity.rows + 1)
    )
    return {
        "active_axes": active_spatial_axes,
        "gravity_rank": gravity.rank(),
        "gauge_rank": gravity_gauge.rank(),
        "gravity_ward": matrix_equal(gravity * gravity_gauge, sp.zeros(10, 4)),
        "tt_dimension": section.cols,
        "tt_gravity_positive": gravity_positive,
        "tt_gravity_signs": gravity_signs,
        "tt_gravity_minors": gravity_minors,
        "tt_vertex_rank": flattened.rank(),
        "tt_vertex_matrix_ranks": tuple(matrix.rank() for matrix in tt_vertices),
        "diagonal_rank": diagonal.rank(),
        "occupation_rank": occupation.rank(),
        "form_degree_rank": form_degree.rank(),
        "context_union_rank": context_union.rank(),
        "individual_context_ranks": individual_context_ranks,
        "mark_derivative_zero": mark_derivative_zero,
        "massless_tt_vertex_rank": massless_flattened.rank(),
        "massless_context_rank": massless_context_rank,
        "massless_occupation_rank": massless_occupation_rank,
        "massless_form_degree_rank": massless_form_degree_rank,
        "context_count": contexts["contexts"],
        "context_checks": contexts["context_checks"],
    }


N5_LINES = (
    "per_element: checked the 16-form CAR, exact metric vertices, reciprocal recoil, and local mark projectors.",
    "per_site: checked the full five-band AP Schur graphs and seven fixed local one-body mark contexts.",
    "per_mode: checked exact coefficientwise Laurent Ward cancellation and three nonzero spatial momentum strata.",
    "per_block: checked the common gravity/DK/TT/mark vertical slice and the declared 25-frame fixture orbit.",
    "lattice_wide: checked and not executed — no full Brillouin-zone theorem, nonlinear completion, permanent write, arbitrary history, refinement, or retained TOE theory is claimed.",
)


def note_facts() -> dict[str, bool]:
    try:
        text = NOTE_PATH.read_text(encoding="utf-8")
    except OSError:
        text = ""
    normalized = " ".join(text.split())
    lowered = normalized.lower()
    return {
        "exists": bool(text),
        "n1_n8": all(f"### n{index}" in lowered for index in range(1, 9)),
        "n5": all(line in text for line in N5_LINES),
        "scope": all(token in normalized for token in (
            "obligation_retirement: 0",
            "toe_percentage_movement: 0",
            "axiom_status: unchanged",
            "permanent_record_write: not_executed",
            "mark_context_status: candidate_diagnostic",
            "retained_positive_end_to_end_theory_count: 0",
        )) and not any(re.search(pattern, normalized) for pattern in (
            r"obligation_retirement:\s*[1-9]",
            r"toe_percentage_movement:\s*[1-9]",
            r"permanent_record_write:\s*(?:executed|true|yes)",
        )),
    }


def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "distance_two_live": True,
        "schur_covariant": False,
        "car": True,
        "raw_vertex_shape": (361, 3, 3, 2, 3, 6),
        "raw_ward_zero": True,
        "covariance_failures": 0,
        "tt_ranks": (2, 2, 2),
        "tt_gravity_minors": ((2, 2), (8, 32), (9, R(243, 4))),
        "form_degree_ranks": (0, 1, 0),
        "occupation_ranks": (1, 1, 2),
        "context_ranks": (2, 2, 2),
        "axis_context_ranks": (1, 1, 1, 1, 1, 1, 1),
        "mass_only_marks": True,
        "permanent_write": False,
        "toe_movement": 0,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "0" * 40
    elif mutation == "drop_distance_two_band":
        claims["distance_two_live"] = False
    elif mutation == "claim_schur_spatial_covariance":
        claims["schur_covariant"] = True
    elif mutation == "break_exterior_car":
        claims["car"] = False
    elif mutation == "break_raw_locality":
        claims["raw_vertex_shape"] = (360, 3, 3, 2, 3, 6)
    elif mutation == "break_total_ward":
        claims["raw_ward_zero"] = False
    elif mutation == "break_cubic_covariance":
        claims["covariance_failures"] = 1
    elif mutation == "break_gravity_tt":
        claims["tt_ranks"] = (2, 2, 1)
    elif mutation == "claim_form_degree_reads_tt":
        claims["form_degree_ranks"] = (2, 2, 2)
    elif mutation == "claim_one_context_reads_all_tt":
        claims["occupation_ranks"] = (2, 2, 2)
    elif mutation == "claim_marks_read_recoil":
        claims["mass_only_marks"] = False
    elif mutation == "claim_permanent_record_write":
        claims["permanent_write"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_movement"] = 1
    return claims


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    seam = schur_facts()
    centered = centered_ward_facts()
    raw = raw_polynomial_facts()
    covariance = covariance_facts()
    strata = tuple(stratum_facts(count) for count in (1, 2, 3))
    note = note_facts()
    claims = build_claims(mutation)

    car_ok = all(
        matrix_equal(
            CREATION[left] * CREATION[right]
            + CREATION[right] * CREATION[left],
            sp.zeros(16),
        )
        and matrix_equal(
            ANNIHILATION[left] * CREATION[right]
            + CREATION[right] * ANNIHILATION[left],
            sp.eye(16) if left == right else sp.zeros(16),
        )
        for left in range(4) for right in range(4)
    )
    generic_differential = sum(
        ((axis + 1) * CREATION[axis] for axis in range(4)), sp.zeros(16)
    )
    car_ok = car_ok and matrix_equal(
        generic_differential * generic_differential, sp.zeros(16)
    )

    expected_shift = claims["schur_covariant"]
    covariance_failure_count = sum(sum(item) for item in covariance["failures"])
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["parent"] == PARENT_COMMIT
            and authority["parent_ancestor"]
            and authority["inputs"],
            "current main/axiom authority, exact Block-189 parent, and literal inputs",
        ),
        "B": (
            all(
                frame["five_band_complete"]
                and frame["distance_two_live"] == claims["distance_two_live"]
                and frame["block_ranks"] == (8, 8, 8, 8, 8)
                and frame["right_identity"]
                and frame["left_identity"]
                and frame["bi_identity"]
                and frame["inverse_identity"]
                and frame["left_right_difference"] == (16, 8)
                and frame["kernel_hermitian"]
                and frame["reflection_ports"] == (True, True)
                and frame["gram_hermitian"] == (True, True)
                and frame["gram_ranks"] == (8, 8)
                and frame["plus_positive"]
                and frame["minus_negative"]
                and frame["action_shift"] == (160, 16)
                and (frame["right_shift"] == (0, 0)) == expected_shift
                and (frame["left_shift"] == (0, 0)) == expected_shift
                and frame["right_shift"] == (48, 8)
                and frame["left_shift"] == (48, 8)
                for frame in seam
            ),
            "both full-band frames have exact positive Schur ports but fail only the frozen inherited spatial intertwiner",
        ),
        "C": (
            car_ok == claims["car"]
            and centered["action_ranks"] == (16, 16)
            and centered["mass_hermitian"] == (True, True)
            and raw["integer_support"]
            and raw["action_in_shape"] == (9, 1, 1, 0, 0, 1)
            and raw["action_out_shape"] == (9, 1, 1, 1, 1, 2)
            and raw["action_endpoint_union_shape"] == (17, 1, 1, 1, 1, 2)
            and raw["hodge_shape"] == (33, 2, 2, 1, 2, 4)
            and raw["vertex_shape"] == claims["raw_vertex_shape"]
            and raw["recoil_shape"] == (93, 2, 2, 2, 2, 4)
            and raw["hodge_terms"] == (3, 3, 3, 3, 4, 4, 4, 4, 4, 4)
            and raw["vertex_terms"] == (47, 47, 47, 47, 60, 60, 60, 60, 60, 60),
            "the full 16-form DK action, metric vertex, and recoil are exact finite Laurent polynomials",
        ),
        "D": (
            centered["hodge_residuals"] == (0, 0, 0, 0)
            and centered["ward_residuals"] == (0, 0, 0, 0)
            and (all(item == (0, 0) for item in raw["ward_residual_terms"]) == claims["raw_ward_zero"])
            and covariance["proper_cubic_count"] == 24
            and covariance["transform_count"] == 25
            and covariance_failure_count == claims["covariance_failures"],
            "metric variation plus reciprocal recoil cancels coefficientwise and is covariant on the declared 25-frame fixture orbit",
        ),
        "E": (
            all(
                item["gravity_rank"] == 6
                and item["gauge_rank"] == 4
                and item["gravity_ward"]
                and item["tt_dimension"] == 2
                and item["tt_gravity_positive"]
                for item in strata
            )
            and tuple(item["tt_vertex_rank"] for item in strata) == claims["tt_ranks"]
            and tuple(item["tt_gravity_minors"] for item in strata)
            == claims["tt_gravity_minors"],
            "one common first-order action has two positive gravity TT directions and a rank-two TT-projected DK vertex image on axis/face/body strata",
        ),
        "F": (
            tuple(item["form_degree_rank"] for item in strata)
            == claims["form_degree_ranks"]
            and tuple(item["occupation_rank"] for item in strata)
            == claims["occupation_ranks"]
            and tuple(item["context_union_rank"] for item in strata)
            == claims["context_ranks"]
            and strata[0]["individual_context_ranks"]
            == claims["axis_context_ranks"]
            and all(
                item["mark_derivative_zero"] == claims["mass_only_marks"]
                and item["massless_tt_vertex_rank"] == 2
                and item["massless_context_rank"] == 0
                and item["massless_occupation_rank"] == 0
                and item["massless_form_degree_rank"] == 0
                for item in strata
            )
            and all(
                item["context_count"] == 7
                and all(item["context_checks"])
                for item in strata
            ),
            "candidate marks separate the mass-Hodge TT image but are exactly blind to the derivative/recoil channel",
        ),
        "G": (
            note["exists"] and note["n1_n8"] and note["n5"] and note["scope"]
            and not claims["permanent_write"]
            and claims["toe_movement"] == 0,
            "the mark algebra remains a candidate diagnostic with no permanent write, axiom edit, obligation retirement, or TOE movement",
        ),
    }


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition: object) -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 96 else statement[:93] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return int(self.failed != 0)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        for mutation in MUTATIONS:
            print(f"{mutation} -> {MUTATION_FAMILY[mutation]}")
        return 0

    checks = Checks()
    for key, (condition, statement) in evaluate(args.mutation).items():
        checks.check(key, statement, condition)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
