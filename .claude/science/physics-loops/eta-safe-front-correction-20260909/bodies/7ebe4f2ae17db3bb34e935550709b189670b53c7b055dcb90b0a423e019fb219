#!/usr/bin/env python3
"""Block 191: carrier, grade-3 source, native history, and write boundary.

The runner executes the preregistered plain Block-128 port and the one allowed
native four-slice 4D reflection fallback.  It then freezes the independently
scouted commuting Clifford-grade-three context and tests positive weights,
conditioned total Ward/recoil, discovery and held-out TT response, a
same-action temporal-mode port, reverse reality, and an adjacent write.  The
native AP history and held-out source actions fail the same-mode spectral gate;
ordinary and graded reverse conventions are reported only as downstream
classifications, not silently admitted into a joined chain.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import re
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190  # noqa: E402
import admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17 as b128  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_GRADE3_SOURCE_INSTRUMENT_HISTORY_WRITE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PREREG_COMMIT = "cbcd2d8b70afcb0e03c4deeec23d6119723738dc"
PARENT_COMMIT = "c6737fe46df64315f895921c2362f50f00f0b036"
CURRENT_MAIN = "c79384cb8ffa27fcb53cb89c53a84a708442eaad"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_GRADE3_SOURCE_INSTRUMENT_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "logs/runner-cache/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.txt",
    "docs/ADMISSIBILITY_DIRAC_KAHLER_CURVED_CARRIER_DEPENDENCY_BOUNDED_THEOREM_NOTE_2026-08-17.md",
    "scripts/admissibility_dirac_kahler_curved_carrier_dependency_2026_08_17.py",
)

MUTATIONS = (
    "stale_main_authority",
    "claim_plain_block128_port",
    "erase_wick_phase_escape",
    "break_native_dual",
    "claim_raw_cut_positive",
    "break_bischur_positive",
    "break_grade3_projectors",
    "claim_nonuniform_weights",
    "break_heldout_source_rank",
    "break_conditioned_ward",
    "break_instrument_covariance",
    "claim_same_action_history_port",
    "claim_ordinary_reverse_reality",
    "erase_graded_reverse_escape",
    "erase_hermitianized_reverse_escape",
    "claim_permanent_record",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "claim_plain_block128_port": "B",
    "erase_wick_phase_escape": "B",
    "break_native_dual": "C",
    "claim_raw_cut_positive": "C",
    "break_bischur_positive": "C",
    "break_grade3_projectors": "D",
    "claim_nonuniform_weights": "D",
    "break_heldout_source_rank": "E",
    "break_conditioned_ward": "E",
    "break_instrument_covariance": "E",
    "claim_same_action_history_port": "F",
    "claim_ordinary_reverse_reality": "F",
    "erase_graded_reverse_escape": "F",
    "erase_hermitianized_reverse_escape": "F",
    "claim_permanent_record": "G",
    "claim_toe_progress": "G",
}

I = sp.I
R = sp.Rational
MASS = R(2, 7)
IDENTITY16 = sp.eye(16)


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


def is_ancestor(ancestor: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", ancestor, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in (left - right))


def nonzero_entries(matrix: sp.Matrix) -> int:
    return sum(sp.simplify(value) != 0 for value in matrix)


def exact_rank(matrix: sp.Matrix) -> int:
    """Use exact domain elimination; far faster on the curved rational cover."""
    return DomainMatrix.from_Matrix(matrix).rank()


def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": worktree_blob(AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": worktree_blob(REGISTRY_PATH),
        "parent_ancestor": is_ancestor(PARENT_COMMIT),
        "prereg_ancestor": is_ancestor(PREREG_COMMIT),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def carrier_facts() -> dict[str, object]:
    subsets = ((), (0,), (3,), (0, 3))
    injection = sp.zeros(16, 4)
    for column, subset in enumerate(subsets):
        injection[b190.FORM_INDEX[subset], column] = 1
    creation_x = sp.expand(injection.T * b190.CREATION[0] * injection)
    creation_t = sp.expand(injection.T * b190.CREATION[3] * injection)
    incidence = sp.expand(b128.S_X * creation_x + b128.S_T * creation_t)
    restricted_action = sp.expand(
        MASS * sp.eye(4) + I * (incidence + incidence.T)
    )
    block128_differential = I * incidence
    block128_action = sp.expand(
        MASS * sp.eye(4)
        + I * (block128_differential + block128_differential.H)
    )
    action_residual = sp.expand(block128_action - restricted_action)

    origins = tuple(
        (time, space)
        for time in (0, 2, 4, 6)
        for space in (0, 2)
    )
    binary_map = sp.Matrix.hstack(*(
        b128.cover_embedding(time, space) for time, space in origins
    ))
    repeated_incidence = sp.kronecker_product(sp.eye(8), incidence)
    chart = b128.chart_differential_cover((0, 0))
    chart_coordinates = sp.expand(binary_map.T * chart * binary_map)
    differential_residual = sp.expand(
        chart_coordinates - repeated_incidence
    )

    curved_hodge = b128.curved_hodge_cover()
    cover_incidence = sp.expand(
        binary_map * repeated_incidence * binary_map.T
    )
    curved_restricted_action = sp.expand(
        MASS * curved_hodge
        + I * (
            curved_hodge * cover_incidence
            + cover_incidence.T * curved_hodge
        )
    )
    curved_block128_action = sp.expand(
        MASS * curved_hodge
        + I * (curved_hodge * chart + chart.H * curved_hodge)
    )
    curved_residual = sp.expand(
        curved_block128_action - curved_restricted_action
    )

    degree_phase = sp.diag(1, -I, -I, -1)
    phase_residual = sp.expand(
        degree_phase.H * restricted_action * degree_phase
        - block128_action
    )
    return {
        "injection_rank": injection.rank(),
        "injection_isometry": matrix_equal(injection.T * injection, sp.eye(4)),
        "creation_residuals": (
            (nonzero_entries(creation_x - b128.block105.EX),
             (creation_x - b128.block105.EX).rank()),
            (nonzero_entries(creation_t - b128.block105.ET),
             (creation_t - b128.block105.ET).rank()),
        ),
        "incidence_rank_nilpotent": (
            incidence.rank(), matrix_equal(incidence * incidence, sp.zeros(4))
        ),
        "binary_map": (
            binary_map.rank(),
            matrix_equal(binary_map.T * binary_map, sp.eye(32)),
        ),
        "chart_relation": matrix_equal(
            chart_coordinates, I * repeated_incidence
        ),
        "differential_residual": (
            nonzero_entries(differential_residual), differential_residual.rank()
        ),
        "action_residual": (
            nonzero_entries(action_residual),
            action_residual.rank(),
            sp.factor(action_residual.det()),
        ),
        "action_controls": (
            restricted_action.rank(), block128_action.rank(),
            sp.factor(restricted_action.det()),
            sp.factor(block128_action.det()),
        ),
        "curved_hodge": (
            exact_rank(curved_hodge), nonzero_entries(curved_hodge)
        ),
        "curved_actions": (
            exact_rank(curved_restricted_action),
            exact_rank(curved_block128_action),
        ),
        "curved_residual": (
            nonzero_entries(curved_residual), exact_rank(curved_residual)
        ),
        "phase_flat_rescue": matrix_equal(phase_residual, sp.zeros(4)),
    }


def native_history_facts() -> dict[str, object]:
    mass, momentum = sp.symbols("mass momentum", positive=True, real=True)
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.diag(1, -1)
    ap_shift = sp.zeros(4)
    for time in range(4):
        ap_shift[(time + 1) % 4, time] = -1 if time == 3 else 1
    temporal_differential = sp.expand((ap_shift - ap_shift.T) / 2)
    edge_reflection = sp.zeros(4)
    for time in range(4):
        edge_reflection[3 - time, time] = -1
    action = sp.expand(
        sp.kronecker_product(
            sp.eye(4), mass * sp.eye(2) + I * momentum * sigma_x
        )
        + sp.kronecker_product(temporal_differential, sigma_z)
    )
    reflection = sp.kronecker_product(edge_reflection, sp.eye(2))
    dual = sp.expand(reflection * action.H * reflection.T)
    doubled_action = sp.diag(action, dual)
    doubled_reflection = sp.Matrix.vstack(
        sp.Matrix.hstack(sp.zeros(8), reflection.T),
        sp.Matrix.hstack(reflection, sp.zeros(8)),
    )
    kernel = sp.simplify(doubled_reflection * doubled_action.inv())

    history_injection = sp.Matrix.vstack(sp.eye(4), sp.zeros(4))
    raw_port = sp.diag(history_injection, history_injection)
    raw_gram = sp.simplify(raw_port.T * kernel * raw_port)
    raw_scale = 1 / (2 * mass**2 + 2 * momentum**2 + 1) ** 2
    raw_root = 1 / (2 * mass**2 + 2 * momentum**2 + 1)
    raw_rank = raw_gram.rank()
    raw_balance = sp.simplify(sp.trace(raw_gram) / raw_root)
    raw_inertia = (
        sp.simplify((raw_rank + raw_balance) / 2),
        sp.simplify((raw_rank - raw_balance) / 2),
        8 - raw_rank,
    )

    block_a = action[:4, :4]
    block_b = action[:4, 4:]
    block_c = action[4:, :4]
    block_d = action[4:, 4:]
    right_graph = sp.Matrix.vstack(
        sp.eye(4), -block_d.inv() * block_c
    )
    left_graph = sp.Matrix.vstack(
        sp.eye(4), -block_d.T.inv() * block_b.T
    )
    plus_port = sp.Matrix.vstack(
        right_graph, reflection * sp.conjugate(right_graph)
    )
    minus_port = sp.Matrix.vstack(
        right_graph, -reflection * sp.conjugate(right_graph)
    )
    plus_gram = sp.simplify(plus_port.H * kernel * plus_port)
    minus_gram = sp.simplify(minus_port.H * kernel * minus_port)
    full_boundary_gram = sp.kronecker_product(plus_gram, sp.eye(8))
    full_boundary_state = sp.simplify(
        full_boundary_gram / sp.trace(full_boundary_gram)
    )
    local_boundary_state = sp.expand(
        full_boundary_state[:16, :16]
        + full_boundary_state[16:, 16:]
    )
    radius = momentum**2
    positive_scalar = sp.factor(
        8 * mass * (
            8 * mass**4 + 16 * mass**2 * radius + 6 * mass**2
            + 8 * radius**2 - 2 * radius + 1
        )
        / (
            (2 * mass**2 + 2 * radius + 1)
            * (4 * mass**2 + 4 * radius + 1) ** 2
        )
    )
    numerator_positive_decomposition = sp.expand(
        8 * (radius - R(1, 8)) ** 2 + R(7, 8)
        + 16 * mass**2 * radius + 6 * mass**2 + 8 * mass**4
    )
    numerator = sp.expand(
        8 * mass**4 + 16 * mass**2 * radius + 6 * mass**2
        + 8 * radius**2 - 2 * radius + 1
    )
    fixture_values = tuple(sp.factor(
        positive_scalar.subs({mass: MASS, momentum: sp.sqrt(value)})
    ) for value in (0, 1, R(3, 2)))
    raw_magnitudes = tuple(sp.factor(
        1 / (2 * MASS**2 + 2 * value + 1)
    ) for value in (0, 1, R(3, 2)))
    return {
        "ap_fourth": matrix_equal(ap_shift**4, -sp.eye(4)),
        "temporal_square": matrix_equal(
            temporal_differential**2, -sp.eye(4) / 2
        ),
        "reflection_twist": matrix_equal(
            edge_reflection * temporal_differential * edge_reflection.T,
            -temporal_differential,
        ),
        "polar_scalar": matrix_equal(
            action.H * action,
            (mass**2 + momentum**2 + R(1, 2)) * sp.eye(8),
        ),
        "dual_conjugate": matrix_equal(dual, sp.conjugate(action)),
        "kernel_hermitian": matrix_equal(kernel, kernel.H),
        "raw_hermitian": matrix_equal(raw_gram, raw_gram.H),
        "raw_square": matrix_equal(raw_gram**2, raw_scale * sp.eye(8)),
        "raw_trace_rank": (sp.trace(raw_gram), raw_rank),
        "raw_inertia": raw_inertia,
        "block_determinant": sp.factor(block_d.det()),
        "block_determinant_identity": sp.simplify(
            block_d.det()
            - (mass**2 + momentum**2 + R(1, 4)) ** 2
        ) == 0,
        "schur_identities": (
            matrix_equal(
                action * right_graph,
                sp.Matrix.vstack(
                    block_a - block_b * block_d.inv() * block_c,
                    sp.zeros(4),
                ),
            ),
            matrix_equal(
                left_graph.T * action,
                sp.Matrix.hstack(
                    block_a - block_b * block_d.inv() * block_c,
                    sp.zeros(4),
                ),
            ),
        ),
        "left_right_difference_rank": (right_graph - left_graph).rank(),
        "plus_scalar": matrix_equal(
            plus_gram, positive_scalar * sp.eye(4)
        ),
        "minus_scalar": matrix_equal(
            minus_gram, -positive_scalar * sp.eye(4)
        ),
        "positive_decomposition": sp.expand(
            numerator_positive_decomposition - numerator
        ) == 0,
        "fixture_values": fixture_values,
        "raw_magnitudes": raw_magnitudes,
        "boundary_state": matrix_equal(
            full_boundary_state, sp.eye(32) / 32
        ),
        "local_state": matrix_equal(
            local_boundary_state, sp.eye(16) / 16
        ),
    }


GAMMAS = tuple(
    item
    for axis in range(4)
    for item in (
        b190.CREATION[axis] + b190.ANNIHILATION[axis],
        I * (b190.CREATION[axis] - b190.ANNIHILATION[axis]),
    )
)
O1 = sp.expand(I * GAMMAS[0] * GAMMAS[2] * GAMMAS[3])
O2 = sp.expand(I * GAMMAS[1] * GAMMAS[2] * GAMMAS[5])
OUTCOME_LABELS = ((-1, -1), (-1, 1), (1, -1), (1, 1))
EFFECTS = tuple(sp.expand(
    (IDENTITY16 + sign1 * O1) * (IDENTITY16 + sign2 * O2) / 4
) for sign1, sign2 in OUTCOME_LABELS)
FORM_PARITY = sp.diag(*(
    (-1) ** len(subset) for subset in b190.FORM_SUBSETS
))

POINTS = (
    ("D1", (0, 0, 0, sp.pi / 4), (sp.pi / 2, 0, 0, 0)),
    ("D2", (0, 0, 0, sp.pi / 4),
     (sp.pi / 2, sp.pi / 2, 0, 0)),
    ("D3", (0, 0, 0, sp.pi / 4),
     (sp.pi / 2, sp.pi / 2, sp.pi / 2, 0)),
    ("H1", (sp.pi / 6, sp.pi / 3, 0, sp.pi / 6),
     (sp.pi / 3, sp.pi / 2, 0, 0)),
    ("H2", (sp.pi / 4, sp.pi / 6, sp.pi / 3, sp.pi / 6),
     (sp.pi / 6, sp.pi / 3, sp.pi / 2, 0)),
)
EXPECTED_POLAR_SCALARS = (
    R(57, 98), R(57, 98), R(57, 98), R(261, 196), R(359, 196)
)
EXPECTED_TT_DETERMINANTS = (
    sp.sqrt(2) * I / 32,
    sp.sqrt(2) * I / 64,
    -3 * I / 128,
    I * (13 - 7 * sp.sqrt(3)) / 2048,
    I * (2 * sp.sqrt(6) + 5 * sp.sqrt(2)) / 4096,
)
EXPECTED_HISTORY_ACTION_RESIDUALS = (
    (0, 0), (0, 0), (0, 0), (-R(1, 4), -R(1, 4)),
    (-R(1, 4), -R(1, 4)),
)


def ward_terms(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> tuple[tuple[sp.Matrix, sp.Matrix, sp.Matrix], ...]:
    action_0, _hodge, vertices = b190.centered_objects(incoming, transfer)
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    differential_0 = b190.centered_differential(incoming)
    differential_1 = b190.centered_differential(outgoing)
    action_1 = sp.expand(
        MASS * IDENTITY16 + I * (differential_1 + differential_1.T)
    )
    gauge = b190.centered_gauge(transfer)
    cosines = tuple(
        sp.cos(incoming[axis] + transfer[axis] / 2)
        for axis in range(4)
    )
    result = []
    for axis in range(4):
        contraction = cosines[axis] * b190.ANNIHILATION[axis]
        right_recoil = sp.expand(
            differential_1 * contraction + contraction * differential_0
        )
        left_recoil = sp.expand(
            (differential_0 * contraction
             + contraction * differential_1).T
        )
        vertex_term = sp.expand(sum(
            (gauge[row, axis] * vertices[row] for row in range(10)),
            sp.zeros(16),
        ))
        result.append((
            vertex_term,
            sp.expand(action_1 * right_recoil),
            sp.expand(left_recoil * action_0),
        ))
    return tuple(result)


def connected_tensor_response(
    incoming: tuple[sp.Expr, ...],
    transfer: tuple[sp.Expr, ...],
    effects: tuple[sp.Matrix, ...] = EFFECTS,
) -> tuple[sp.Matrix, tuple[sp.Matrix, ...], tuple[sp.Matrix, ...]]:
    _action, hodge, vertices = b190.centered_objects(incoming, transfer)
    centered_effects = tuple(effect / 4 - IDENTITY16 / 16 for effect in effects)
    response = sp.Matrix([
        [sp.simplify(sp.trace(effect * vertex)) for vertex in vertices]
        for effect in centered_effects
    ])
    hodge_response = sp.Matrix([
        [sp.simplify(sp.trace(effect * vertex)) for vertex in hodge]
        for effect in centered_effects
    ])
    return response, hodge_response, centered_effects


def point_facts(
    incoming: tuple[sp.Expr, ...], transfer: tuple[sp.Expr, ...]
) -> dict[str, object]:
    action, hodge, vertices = b190.centered_objects(incoming, transfer)
    polar = sp.expand(action.H * action)
    scalar = sp.factor(polar[0, 0])
    right_polar = sp.expand(action * action.H)
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    outgoing_differential = b190.centered_differential(outgoing)
    outgoing_action = sp.expand(
        MASS * IDENTITY16
        + I * (outgoing_differential + outgoing_differential.T)
    )
    outgoing_polar = sp.expand(outgoing_action.H * outgoing_action)
    outgoing_scalar = sp.factor(outgoing_polar[0, 0])
    outgoing_right_polar = sp.expand(outgoing_action * outgoing_action.H)
    native_history_scalars = tuple(sp.factor(
        MASS**2
        + sum(sp.sin(momentum[axis]) ** 2 for axis in range(3))
        + R(1, 2)
    ) for momentum in (incoming, outgoing))
    history_action_residual = (
        sp.simplify(scalar - native_history_scalars[0]),
        sp.simplify(outgoing_scalar - native_history_scalars[1]),
    )
    weights = tuple(sp.simplify(sp.trace(effect) / 16) for effect in EFFECTS)
    section = b190.tt_basis(sp.Matrix(tuple(
        2 * sp.sin(transfer[axis] / 2) for axis in range(3)
    )))
    tt_vertices = tuple(sp.expand(sum(
        (section[row, column] * vertices[row] for row in range(10)),
        sp.zeros(16),
    )) for column in range(2))
    tt_hodge = tuple(sp.expand(sum(
        (section[row, column] * hodge[row] for row in range(10)),
        sp.zeros(16),
    )) for column in range(2))
    coefficient_matrix = sp.Matrix([
        [sp.simplify(sp.trace(operator * vertex) / 16)
         for vertex in tt_vertices]
        for operator in (O1, O2)
    ])
    hodge_coefficients = sp.Matrix([
        [sp.simplify(sp.trace(operator * vertex) / 16)
         for vertex in tt_hodge]
        for operator in (O1, O2)
    ])
    response, hodge_response, centered_effects = connected_tensor_response(
        incoming, transfer
    )
    outcome_tt = sp.expand(response * section)
    expected_outcome_tt = sp.Matrix([
        [sign1 * coefficient_matrix[0, column]
         + sign2 * coefficient_matrix[1, column]
         for column in range(2)]
        for sign1, sign2 in OUTCOME_LABELS
    ])

    conditioned_ward = []
    hermitianized_conditioned_ward = []
    nonzero_heldout_terms = []
    for vertex_term, right_term, left_term in ward_terms(incoming, transfer):
        triples = tuple(tuple(sp.simplify(sp.trace(effect * term)) for term in (
            vertex_term, right_term, left_term
        )) for effect in centered_effects)
        conditioned_ward.extend(
            sp.simplify(left + middle - right) == 0
            for left, middle, right in triples
        )
        hermitianized_conditioned_ward.extend(
            sp.simplify(-I * left - I * middle + I * right) == 0
            for left, middle, right in triples
        )
        nonzero_heldout_terms.append(tuple(
            all(value != 0 for value in triple) for triple in triples
        ))

    reverse_transfer = tuple(-item for item in transfer)
    _reverse_action, _reverse_hodge_vertices, reverse_vertices = (
        b190.centered_objects(outgoing, reverse_transfer)
    )
    reverse_response, _reverse_hodge, _reverse_effects = (
        connected_tensor_response(outgoing, reverse_transfer)
    )
    same_label_anti_reality = matrix_equal(
        reverse_response, -sp.conjugate(response)
    )
    relabel = (3, 2, 1, 0)
    graded_reverse = reverse_response[list(relabel), :]
    graded_reality = matrix_equal(graded_reverse, sp.conjugate(response))
    hermitianized_reality = matrix_equal(
        -I * reverse_response, sp.conjugate(-I * response)
    )
    vertex_adjoint = all(matrix_equal(
        vertices[slot].H,
        FORM_PARITY
        * reverse_vertices[slot]
        * FORM_PARITY,
    ) for slot in range(10))
    return {
        "polar_scalar": scalar,
        "polar_identity": matrix_equal(polar, scalar * IDENTITY16),
        "right_polar_identity": matrix_equal(
            right_polar, scalar * IDENTITY16
        ),
        "outgoing_polar_identity": matrix_equal(
            outgoing_polar, outgoing_scalar * IDENTITY16
        ),
        "outgoing_right_polar_identity": matrix_equal(
            outgoing_right_polar, outgoing_scalar * IDENTITY16
        ),
        "history_action_residual": history_action_residual,
        "weights": weights,
        "coefficient_determinant": sp.factor(coefficient_matrix.det()),
        "tt_rank": outcome_tt.rank(),
        "direct_coefficient_match": matrix_equal(
            outcome_tt, expected_outcome_tt
        ),
        "mass_hodge_zero": matrix_equal(hodge_coefficients, sp.zeros(2)),
        "mass_hodge_full_outcome_zero": matrix_equal(
            hodge_response, sp.zeros(4, 10)
        ),
        "mass_hodge_outcome_zero": matrix_equal(
            hodge_response * section, sp.zeros(4, 2)
        ),
        "conditioned_ward": all(conditioned_ward),
        "hermitianized_conditioned_ward": all(
            hermitianized_conditioned_ward
        ),
        "nonzero_ward_terms": tuple(nonzero_heldout_terms),
        "same_label_anti_reality": same_label_anti_reality,
        "ordinary_reality": matrix_equal(
            reverse_response, sp.conjugate(response)
        ),
        "graded_reality": graded_reality,
        "hermitianized_reality": hermitianized_reality,
        "vertex_adjoint": vertex_adjoint,
    }


def instrument_facts() -> dict[str, object]:
    projectors = tuple(
        matrix_equal(effect.H, effect)
        and matrix_equal(effect * effect, effect)
        and effect.rank() == 4
        for effect in EFFECTS
    )
    orthogonal = all(matrix_equal(
        EFFECTS[left] * EFFECTS[right], sp.zeros(16)
    ) for left in range(4) for right in range(4) if left != right)
    parity_map = all(matrix_equal(
        FORM_PARITY * EFFECTS[index] * FORM_PARITY,
        EFFECTS[3 - index],
    ) for index in range(4))
    points = tuple(point_facts(incoming, transfer) for _name, incoming, transfer in POINTS)

    spatial_rotation = sp.Matrix(((0, 1, 0), (-1, 0, 0), (0, 0, 1)))
    full_rotation = sp.eye(4)
    full_rotation[:3, :3] = spatial_rotation
    form_rotation = b190.wedge_representation(full_rotation)
    tensor_rotation = b190.tensor_representation(full_rotation)
    _name, incoming, transfer = POINTS[-1]
    rotated_incoming = tuple(full_rotation * sp.Matrix(incoming))
    rotated_transfer = tuple(full_rotation * sp.Matrix(transfer))
    rotated_effects = tuple(sp.expand(
        form_rotation * effect * form_rotation.T
    ) for effect in EFFECTS)
    original_response, _hodge, _effects = connected_tensor_response(
        incoming, transfer
    )
    rotated_response, _rot_hodge, _rot_effects = connected_tensor_response(
        rotated_incoming, rotated_transfer, rotated_effects
    )
    covariance_residual = sp.expand(
        tensor_rotation.T * rotated_response.T - original_response.T
    )
    rotated_section = b190.tt_basis(sp.Matrix(tuple(
        2 * sp.sin(rotated_transfer[axis] / 2) for axis in range(3)
    )))
    return {
        "involutions": (
            matrix_equal(O1.H, O1), matrix_equal(O2.H, O2),
            matrix_equal(O1 * O1, IDENTITY16),
            matrix_equal(O2 * O2, IDENTITY16),
            matrix_equal(O1 * O2, O2 * O1),
        ),
        "projectors": projectors,
        "orthogonal": orthogonal,
        "sum_identity": matrix_equal(sum(EFFECTS, sp.zeros(16)), IDENTITY16),
        "parity_map": parity_map,
        "points": points,
        "covariance_residual": (
            nonzero_entries(covariance_residual), covariance_residual.rank()
        ),
        "rotated_tt_rank": (rotated_response * rotated_section).rank(),
    }


def write_facts() -> dict[str, object]:
    write = sp.Matrix.vstack(*EFFECTS)
    output_state = sp.expand(write * (IDENTITY16 / 16) * write.H)
    pointer_projectors = []
    for selected in range(4):
        pointer = sp.zeros(64)
        pointer[selected * 16:(selected + 1) * 16,
                selected * 16:(selected + 1) * 16] = IDENTITY16
        pointer_projectors.append(pointer)
    correlations = tuple(matrix_equal(
        pointer_projectors[index] * write,
        write * EFFECTS[index],
    ) for index in range(4))
    probabilities = tuple(sp.simplify(sp.trace(
        pointer * output_state
    )) for pointer in pointer_projectors)
    boundary_write = sp.kronecker_product(sp.eye(2), write)
    history_output_state = sp.diag(output_state / 2, output_state / 2)
    history_congruence = sp.expand(
        boundary_write * (sp.eye(32) / 32) * boundary_write.H
    )
    return {
        "isometry": matrix_equal(write.H * write, IDENTITY16),
        "output_state": (
            matrix_equal(output_state.H, output_state),
            exact_rank(output_state),
            sp.trace(output_state),
            matrix_equal(output_state * output_state, output_state / 16),
        ),
        "correlations": correlations,
        "probabilities": probabilities,
        "pointer_orthogonality": all(matrix_equal(
            pointer_projectors[left] * pointer_projectors[right], sp.zeros(64)
        ) for left in range(4) for right in range(4) if left != right),
        "next_identity_invariance": all(matrix_equal(
            sp.eye(64) * pointer, pointer * sp.eye(64)
        ) for pointer in pointer_projectors),
        "history_isometry": matrix_equal(
            boundary_write.H * boundary_write, sp.eye(32)
        ),
        "history_congruence": matrix_equal(
            history_congruence, history_output_state
        ),
        "history_output_state": (
            matrix_equal(history_output_state.H, history_output_state),
            2 * exact_rank(output_state),
            sp.trace(history_output_state),
            matrix_equal(
                history_output_state * history_output_state,
                history_output_state / 32,
            ),
        ),
    }


N5_LINES = (
    "per_element: checked Clifford involutions, joint projectors, polar state, and outcome weights.",
    "per_site: checked the plain Block-128 carrier map and the local adjacent write isometry.",
    "per_mode: checked the reduced analytic AP history family and five separate source momenta plus one transported frame.",
    "per_block: checked separate carrier, source, history, and write blocks plus the failed same-action temporal port with ordinary, graded, and Hermitianized reverse tests.",
    "lattice_wide: checked and not executed — no arbitrary lattice, nonlinear gravity, Born derivation, selected permanent Record law, refinement, or retained TOE theory is claimed.",
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
            "ordinary_reverse_reality: failed",
            "graded_reverse_status: live_unadmitted_escape",
            "hermitianized_reverse_status: live_unadmitted_escape",
            "same_action_history_port: failed_heldout_temporal_spectrum",
            "composed_source_history_write: not_claimed",
            "permanent_record_write: not_claimed",
            "obligation_retirement: 0",
            "toe_percentage_movement: 0",
            "axiom_status: unchanged",
            "retained_positive_end_to_end_theory_count: 0",
        )),
    }


def build_claims(mutation: str) -> dict[str, object]:
    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "plain_port": False,
        "phase_escape": True,
        "native_dual": True,
        "raw_inertia": (4, 4, 0),
        "bischur_positive": True,
        "projectors": True,
        "weights": (R(1, 4),) * 4,
        "tt_determinants": EXPECTED_TT_DETERMINANTS,
        "ward": True,
        "covariance": (0, 0),
        "same_action_history": False,
        "ordinary_reality": False,
        "graded_escape": True,
        "hermitianized_escape": True,
        "permanent_record": False,
        "toe_movement": 0,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "0" * 40
    elif mutation == "claim_plain_block128_port":
        claims["plain_port"] = True
    elif mutation == "erase_wick_phase_escape":
        claims["phase_escape"] = False
    elif mutation == "break_native_dual":
        claims["native_dual"] = False
    elif mutation == "claim_raw_cut_positive":
        claims["raw_inertia"] = (8, 0, 0)
    elif mutation == "break_bischur_positive":
        claims["bischur_positive"] = False
    elif mutation == "break_grade3_projectors":
        claims["projectors"] = False
    elif mutation == "claim_nonuniform_weights":
        claims["weights"] = (R(1, 5), R(1, 5), R(1, 5), R(2, 5))
    elif mutation == "break_heldout_source_rank":
        changed = list(EXPECTED_TT_DETERMINANTS)
        changed[-1] = 0
        claims["tt_determinants"] = tuple(changed)
    elif mutation == "break_conditioned_ward":
        claims["ward"] = False
    elif mutation == "break_instrument_covariance":
        claims["covariance"] = (1, 1)
    elif mutation == "claim_same_action_history_port":
        claims["same_action_history"] = True
    elif mutation == "claim_ordinary_reverse_reality":
        claims["ordinary_reality"] = True
    elif mutation == "erase_graded_reverse_escape":
        claims["graded_escape"] = False
    elif mutation == "erase_hermitianized_reverse_escape":
        claims["hermitianized_escape"] = False
    elif mutation == "claim_permanent_record":
        claims["permanent_record"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_movement"] = 1
    return claims


def evaluate(mutation: str) -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    carrier = carrier_facts()
    history = native_history_facts()
    instrument = instrument_facts()
    write = write_facts()
    note = note_facts()
    claims = build_claims(mutation)
    points = instrument["points"]
    history_action_residuals = tuple(
        point["history_action_residual"] for point in points
    )
    same_action_history = all(
        all(residual == 0 for residual in pair)
        for pair in history_action_residuals
    )
    bischur_positive = (
        history["plus_scalar"] and history["positive_decomposition"]
    )
    projector_ok = (
        all(instrument["involutions"])
        and all(instrument["projectors"])
        and instrument["orthogonal"]
        and instrument["sum_identity"]
    )
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["parent_ancestor"]
            and authority["prereg_ancestor"]
            and authority["inputs"],
            "current main/axiom authority, exact Block-190 parent and preregistration, and literal inputs",
        ),
        "B": (
            carrier["injection_rank"] == 4
            and carrier["injection_isometry"]
            and carrier["creation_residuals"] == ((0, 0), (0, 0))
            and carrier["incidence_rank_nilpotent"] == (2, True)
            and carrier["binary_map"] == (32, True)
            and carrier["chart_relation"]
            and carrier["differential_residual"] == (32, 16)
            and carrier["action_residual"] == (8, 4, 4)
            and carrier["action_controls"] == (4, 4, R(2809, 2401), R(2809, 2401))
            and carrier["curved_hodge"] == (32, 88)
            and carrier["curved_actions"] == (32, 32)
            and carrier["curved_residual"] == (160, 32)
            and ((carrier["action_residual"][1] == 0) == claims["plain_port"])
            and carrier["phase_flat_rescue"] == claims["phase_escape"],
            "the canonical exterior restriction passes, while the frozen plain Block-128 action port fails at the Wick phase",
        ),
        "C": (
            history["ap_fourth"]
            and history["temporal_square"]
            and history["reflection_twist"]
            and history["polar_scalar"]
            and history["dual_conjugate"] == claims["native_dual"]
            and history["kernel_hermitian"]
            and history["raw_hermitian"]
            and history["raw_square"]
            and history["raw_trace_rank"] == (0, 8)
            and history["raw_inertia"] == claims["raw_inertia"]
            and history["block_determinant_identity"]
            and all(history["schur_identities"])
            and history["left_right_difference_rank"] == 4
            and bischur_positive == claims["bischur_positive"]
            and history["minus_scalar"]
            and history["fixture_values"]
            == (R(112, 65), R(2379664, 10558755), R(414624, 2190977))
            and history["raw_magnitudes"]
            == (R(49, 57), R(49, 155), R(49, 204))
            and history["boundary_state"]
            and history["local_state"],
            "the reduced AP raw cut is indefinite but its displayed reflection-even doubled Schur port is positive for every m>0 and spatial momentum",
        ),
        "D": (
            projector_ok == claims["projectors"]
            and instrument["parity_map"]
            and all(
                point["polar_identity"]
                and point["right_polar_identity"]
                and point["outgoing_polar_identity"]
                and point["outgoing_right_polar_identity"]
                and point["polar_scalar"] == expected_scalar
                and point["weights"] == claims["weights"]
                for point, expected_scalar in zip(points, EXPECTED_POLAR_SCALARS)
            ),
            "the frozen grade-three context is a positive four-outcome PVM and the action polar state gives candidate trace weights 1/4",
        ),
        "E": (
            all(
                sp.simplify(point["coefficient_determinant"] - expected) == 0
                for point, expected in zip(points, claims["tt_determinants"])
            )
            and all(
                point["tt_rank"] == 2
                and point["direct_coefficient_match"]
                and point["mass_hodge_zero"]
                and point["mass_hodge_full_outcome_zero"]
                and point["mass_hodge_outcome_zero"]
                and point["conditioned_ward"] == claims["ward"]
                for point in points
            )
            and all(all(all(axis) for axis in point["nonzero_ward_terms"][:3])
                    for point in points[3:])
            and instrument["covariance_residual"] == claims["covariance"]
            and instrument["rotated_tt_rank"] == 2,
            "the conditioned response candidate is derivative-only, Ward/recoil exact, rank two on discovery and held-out points, and frame covariant",
        ),
        "F": (
            history_action_residuals == EXPECTED_HISTORY_ACTION_RESIDUALS
            and same_action_history == claims["same_action_history"]
            and all(point["same_label_anti_reality"] for point in points)
            and (all(point["ordinary_reality"] for point in points)
                 == claims["ordinary_reality"])
            and all(point["vertex_adjoint"] for point in points)
            and instrument["parity_map"]
            and (all(point["graded_reality"] for point in points)
                 == claims["graded_escape"])
            and all(point["hermitianized_conditioned_ward"] for point in points)
            and (all(point["hermitianized_reality"] for point in points)
                 == claims["hermitianized_escape"]),
            "the AP history/source same-mode port fails on both held-outs; graded-outcome and Hermitianized-source reverse conventions remain exact downstream escapes",
        ),
        "G": (
            write["isometry"]
            and write["output_state"] == (True, 16, 1, True)
            and all(write["correlations"])
            and write["probabilities"] == (R(1, 4),) * 4
            and write["pointer_orthogonality"]
            and write["next_identity_invariance"]
            and write["history_isometry"]
            and write["history_congruence"]
            and write["history_output_state"] == (True, 32, 1, True)
            and note["exists"] and note["n1_n8"] and note["n5"] and note["scope"]
            and not claims["permanent_record"]
            and claims["toe_movement"] == 0,
            "the adjacent write isometry is positive and stable algebraically, but no permanent Record or TOE closure is claimed",
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
        return self.failed


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
    for line in N5_LINES:
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
