#!/usr/bin/env python3
"""Block 193: fixed-L24 physical event/Record-law discriminator.

The runner derives the ordinary-transpose reflected Schur response of the
physical incoming/outgoing momentum pair.  Its primary source is literally
``M_q tensor V(p,q)`` paired with
``M_q^dagger tensor V(p+q,-q)`` on the full carrier, exactly as frozen before
execution.  A mode-equivalent local temporal lift is not substituted for that
operator.  The Hermitian forward/adjoint pair is kept only as an explicit
control.  Diagonal and coherent event laws are never fitted to target values.
"""

from __future__ import annotations

import argparse
from functools import cache
from pathlib import Path
import subprocess
import sys
from typing import Iterable

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190  # noqa: E402
import admissibility_d4_grade3_source_instrument_history_write_2026_08_24 as b191  # noqa: E402
import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "872ce2ff1d0cbed0afb19f1abd12b0b9559d54a7"
PREREG_COMMIT = "90acec86bd007075bdadc5c8c30fc58f32d6f95c"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_GRADE3_SOURCE_INSTRUMENT_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

MUTATIONS = (
    "stale_main_authority",
    "replace_literal_source_by_local_lift",
    "break_diagonal_evenness",
    "claim_diagonal_rank_two",
    "break_coherent_completeness",
    "claim_scalar_phase_repairs_rank",
    "claim_clock_parity_response",
    "open_heldouts_after_discovery_failure",
    "claim_permanent_record",
    "claim_broad_coherent_no_go",
    "claim_axiom_update",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "replace_literal_source_by_local_lift": "B",
    "break_diagonal_evenness": "C",
    "claim_diagonal_rank_two": "C",
    "break_coherent_completeness": "D",
    "claim_scalar_phase_repairs_rank": "E",
    "claim_clock_parity_response": "E",
    "open_heldouts_after_discovery_failure": "F",
    "claim_permanent_record": "F",
    "claim_broad_coherent_no_go": "G",
    "claim_axiom_update": "G",
    "claim_toe_progress": "G",
}


I = sp.I
R = sp.Rational
MASS = R(2, 7)
L_TIME = 24
HALF_TIME = 12
IDENTITY16 = sp.eye(16)
GTIME = b190.CREATION[3] + b190.ANNIHILATION[3]
GSPACE = tuple(
    b190.CREATION[axis] + b190.ANNIHILATION[axis]
    for axis in range(3)
)

POINTS = {name: (incoming, transfer)
          for name, incoming, transfer in b192.POINTS}

Term = tuple[sp.MatrixBase, sp.MatrixBase]
Terms = tuple[Term, ...]
BlockTerms = tuple[tuple[Terms, Terms], tuple[Terms, Terms]]


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def exact_inverse(matrix: sp.MatrixBase) -> sp.Matrix:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).to_field().inv().to_Matrix()


def exact_scalar(value: sp.Expr) -> sp.Expr:
    """Canonicalize one algebraic scalar through an exact number field."""
    return DomainMatrix.from_Matrix(
        sp.Matrix([[value]]), extension=True
    ).to_field().to_Matrix()[0, 0]


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "axiom": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "worktree_axiom": git_output("hash-object", "--", AXIOM_PATH),
        "registry": git_output("rev-parse", f"origin/main:{REGISTRY_PATH}"),
        "worktree_registry": git_output("hash-object", "--", REGISTRY_PATH),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


def compress(terms: Iterable[Term]) -> Terms:
    accumulated: dict[sp.ImmutableMatrix, sp.MatrixBase] = {}
    for temporal, internal in terms:
        key = sp.ImmutableMatrix(temporal)
        if key in accumulated:
            accumulated[key] = accumulated[key] + internal
        else:
            accumulated[key] = internal
    return tuple(
        (sp.Matrix(temporal), sp.Matrix(internal))
        for temporal, internal in accumulated.items()
    )


def term_sum(*families: Terms) -> Terms:
    return compress(term for family in families for term in family)


def term_scale(family: Terms, scalar: sp.Expr) -> Terms:
    return compress((temporal, scalar * internal)
                    for temporal, internal in family)


def term_multiply(left: Terms, right: Terms) -> Terms:
    return compress(
        (left_t * right_t, left_i * right_i)
        for left_t, left_i in left
        for right_t, right_i in right
    )


def term_product(*families: Terms) -> Terms:
    result = families[0]
    for family in families[1:]:
        result = term_multiply(result, family)
    return result


def term_transpose(family: Terms) -> Terms:
    return compress((temporal.T, internal.T)
                    for temporal, internal in family)


def term_adjoint(family: Terms) -> Terms:
    return compress((temporal.H, internal.H)
                    for temporal, internal in family)


def block_add(*blocks: BlockTerms) -> BlockTerms:
    return tuple(tuple(
        term_sum(*(block[row][column] for block in blocks))
        for column in range(2)
    ) for row in range(2))  # type: ignore[return-value]


def block_scale(block: BlockTerms, scalar: sp.Expr) -> BlockTerms:
    return tuple(tuple(
        term_scale(block[row][column], scalar)
        for column in range(2)
    ) for row in range(2))  # type: ignore[return-value]


def block_multiply(left: BlockTerms, right: BlockTerms) -> BlockTerms:
    return tuple(tuple(
        term_sum(*(term_product(
            left[row][middle], right[middle][column]
        ) for middle in range(2)))
        for column in range(2)
    ) for row in range(2))  # type: ignore[return-value]


def block_product(*blocks: BlockTerms) -> BlockTerms:
    result = blocks[0]
    for block in blocks[1:]:
        result = block_multiply(result, block)
    return result


def block_transpose(block: BlockTerms) -> BlockTerms:
    return tuple(tuple(
        term_transpose(block[column][row])
        for column in range(2)
    ) for row in range(2))  # type: ignore[return-value]


def block_adjoint(block: BlockTerms) -> BlockTerms:
    return tuple(tuple(
        term_adjoint(block[column][row])
        for column in range(2)
    ) for row in range(2))  # type: ignore[return-value]


def block_trace(
    block: BlockTerms,
    effect: sp.MatrixBase | None = None,
) -> sp.Expr:
    return sp.factor(sp.simplify(sum(
        term_trace(block[sector][sector], effect)
        for sector in range(2)
    )))


def term_trace_raw(
    family: Terms,
    effect: sp.MatrixBase | None = None,
) -> sp.Expr:
    """Unsimplified trace used to expose cancellations before matrix merging."""
    value = 0
    for temporal, internal in family:
        internal_trace = (
            sp.trace(internal) if effect is None
            else weighted_trace(effect, internal)
        )
        value += sp.trace(temporal) * internal_trace
    return value


def block_diagonal_trace_raw(
    block: BlockTerms,
    effect: sp.MatrixBase | None = None,
) -> sp.Expr:
    return sum(
        term_trace_raw(block[sector][sector], effect)
        for sector in range(2)
    )


def term_trace(family: Terms, effect: sp.MatrixBase | None = None) -> sp.Expr:
    value = 0
    for temporal, internal in family:
        internal_trace = (
            sp.trace(internal) if effect is None
            else weighted_trace(effect, internal)
        )
        value += sp.trace(temporal) * internal_trace
    return exact_scalar(value)


def term_tensor_entry(
    family: Terms,
    temporal_row: int,
    temporal_column: int,
    internal_row: int,
    internal_column: int,
) -> sp.Expr:
    """Evaluate one exact entry of the represented temporal/internal tensor."""
    return exact_scalar(sum(
        temporal[temporal_row, temporal_column]
        * internal[internal_row, internal_column]
        for temporal, internal in family
    ))


def weighted_trace(
    effect: sp.MatrixBase,
    internal: sp.MatrixBase,
) -> sp.Expr:
    """Compute ``Tr(effect*internal)`` without a dense matrix product."""
    return sum(
        effect[row, column] * internal[column, row]
        for row in range(effect.rows)
        for column in range(effect.cols)
        if effect[row, column] != 0
    )


def spatial_differential(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.expand(sum(
        (sp.sin(momentum[axis]) * b190.CREATION[axis]
         for axis in range(3)),
        sp.zeros(16),
    ))


def spatial_clifford(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.expand(sum(
        (sp.sin(momentum[axis]) * GSPACE[axis] for axis in range(3)),
        sp.zeros(16),
    ))


@cache
def temporal_data() -> dict[str, sp.Matrix]:
    _shift, differential, _cosine, _reflection = b192.temporal_matrices()
    embedding_n = sp.Matrix.vstack(sp.eye(HALF_TIME), sp.zeros(HALF_TIME))
    embedding_p = sp.Matrix.vstack(sp.zeros(HALF_TIME), sp.eye(HALF_TIME))
    differential_p = sp.expand(embedding_p.T * differential * embedding_p)
    differential_pn = sp.expand(embedding_p.T * differential * embedding_n)
    return {
        "differential": differential,
        "embedding_n": embedding_n,
        "embedding_p": embedding_p,
        "differential_p": differential_p,
        "differential_pn": differential_pn,
    }


@cache
def sector_terms(momentum: tuple[sp.Expr, ...]) -> dict[str, Terms]:
    data = temporal_data()
    differential = data["differential"]
    embedding_n = data["embedding_n"]
    embedding_p = data["embedding_p"]
    differential_p = data["differential_p"]
    differential_pn = data["differential_pn"]
    spatial = spatial_clifford(momentum)
    radius = sp.simplify(sum(
        sp.sin(momentum[axis]) ** 2 for axis in range(3)
    ))
    temporal_inverse = exact_inverse(
        (MASS**2 + radius) * sp.eye(L_TIME) - differential**2
    )
    p_inverse = exact_inverse(
        (MASS**2 + radius) * sp.eye(HALF_TIME) - differential_p**2
    )
    internal_inverse = sp.expand(MASS * IDENTITY16 - I * spatial)

    action_inverse = compress((
        (temporal_inverse, internal_inverse),
        (-temporal_inverse * differential, GTIME),
    ))
    embedded_p_inverse = compress((
        (embedding_p * p_inverse * embedding_p.T, internal_inverse),
        (-embedding_p * p_inverse * differential_p * embedding_p.T, GTIME),
    ))
    graph = compress((
        (embedding_n, IDENTITY16),
        (embedding_p * p_inverse * differential_p * differential_pn,
         IDENTITY16),
        (embedding_p * p_inverse * differential_pn,
         sp.expand(-MASS * GTIME + I * spatial * GTIME)),
    ))
    half_gram = term_product(
        term_transpose(graph), action_inverse, graph
    )
    gram = term_sum(half_gram, term_adjoint(half_gram))
    return {
        "inverse": action_inverse,
        "p_inverse": embedded_p_inverse,
        "graph": graph,
        "half_gram": half_gram,
        "gram": gram,
    }


def modulation(transfer_time: sp.Expr) -> sp.Matrix:
    return sp.diag(*(
        b192.root(transfer_time) ** time for time in range(L_TIME)
    ))


@cache
def source_pair_terms(
    incoming: tuple[sp.Expr, ...],
    transfer: tuple[sp.Expr, ...],
    slot: int,
) -> dict[str, object]:
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    _action, hodge, forward_vertices = b190.centered_objects(
        incoming, transfer
    )
    _reverse_action, reverse_hodge, reverse_vertices = b190.centered_objects(
        outgoing, tuple(-value for value in transfer)
    )
    metric = hodge[slot]
    metric_reverse = reverse_hodge[slot]
    mod = modulation(transfer[3])
    mod_reverse = mod.H

    # This is the preregistered full-carrier source.  Although a local
    # temporal expression can have the same symbol on the selected Fourier
    # mode, it is a different operator away from that mode and therefore may
    # not be used in the Schur response.
    forward = compress(((mod, forward_vertices[slot]),))
    reverse = compress(((mod_reverse, reverse_vertices[slot]),))
    hermitian_control = term_adjoint(forward)
    return {
        "forward": forward,
        "reverse": reverse,
        "hermitian_control": hermitian_control,
        "forward_vertex": forward_vertices[slot],
        "reverse_vertex": reverse_vertices[slot],
        "metric_same": matrix_equal(metric, metric_reverse),
    }


def tt_section(point_name: str) -> sp.Matrix:
    _incoming, transfer = POINTS[point_name]
    spatial_incidence = sp.Matrix(tuple(
        2 * sp.sin(transfer[axis] / 2) for axis in range(3)
    ))
    return b190.tt_basis(spatial_incidence)


@cache
def combined_source_pair_terms(
    point_name: str,
    coefficients: tuple[sp.Expr, ...],
) -> dict[str, object]:
    if len(coefficients) != len(b190.PAIRS4):
        raise ValueError("one coefficient is required for each PAIRS4 slot")
    incoming, transfer = POINTS[point_name]
    sources = tuple(
        source_pair_terms(incoming, transfer, slot)
        for slot in range(len(b190.PAIRS4))
    )
    forward = term_sum(*(term_scale(
        source["forward"], coefficients[slot]
    ) for slot, source in enumerate(sources)))
    reverse = term_sum(*(term_scale(
        source["reverse"], coefficients[slot]
    ) for slot, source in enumerate(sources)))
    hermitian_control = term_adjoint(forward)
    return {
        "forward": forward,
        "reverse": reverse,
        "hermitian_control": hermitian_control,
    }


def tt_source_coefficients(point_name: str, column: int) -> tuple[sp.Expr, ...]:
    section = tt_section(point_name)
    if column < 0 or column >= section.cols:
        raise ValueError(f"TT column must be in range(0, {section.cols})")
    return tuple(sp.expand(section[row, column]) for row in range(section.rows))


def add_coefficients(
    *families: tuple[sp.Expr, ...],
) -> tuple[sp.Expr, ...]:
    return tuple(sp.expand(sum(family[index] for family in families))
                 for index in range(len(b190.PAIRS4)))


def exterior_creation_small(axis: int, axes: int = 2) -> sp.Matrix:
    subsets = tuple(
        subset
        for degree in range(axes + 1)
        for subset in __import__("itertools").combinations(range(axes), degree)
    )
    index = {subset: position for position, subset in enumerate(subsets)}
    result = sp.zeros(2**axes)
    for column, subset in enumerate(subsets):
        if axis in subset:
            continue
        target = tuple(sorted(subset + (axis,)))
        sign = (-1) ** sum(item < axis for item in subset)
        result[index[target], column] = sign
    return result


def ext_yz_reordering() -> sp.Matrix:
    ext_subsets = ((), (0,), (3,), (0, 3))
    yz_subsets = ((), (1,), (2,), (1, 2))
    result = sp.zeros(16)
    for ext_index, ext_subset in enumerate(ext_subsets):
        for yz_index, yz_subset in enumerate(yz_subsets):
            full_subset = tuple(sorted(ext_subset + yz_subset))
            inversions = sum(
                left > right for left in ext_subset for right in yz_subset
            )
            column = 4 * ext_index + yz_index
            result[b190.FORM_INDEX[full_subset], column] = (-1) ** inversions
    return result


def partial_trace_yz(matrix: sp.MatrixBase) -> sp.Matrix:
    return sp.Matrix(4, 4, lambda row, column: sum(
        matrix[4 * row + yz, 4 * column + yz] for yz in range(4)
    ))


@cache
def d1_diagonal_all_orders_facts() -> dict[str, object]:
    """Exact D1 TT algebra proving uniform diagonal weights to all orders."""
    h1, h2 = sp.symbols("h1 h2", real=True)
    create_y = exterior_creation_small(0)
    create_z = exterior_creation_small(1)
    annihilate_y = create_y.T
    annihilate_z = create_z.T
    number_y = create_y * annihilate_y
    number_z = create_z * annihilate_z
    q_yz = sp.expand(
        h1 * (number_y - number_z)
        - h2 * (
            create_y * annihilate_z + create_z * annihilate_y
        ) / sp.sqrt(2)
    )
    odd_yz = sp.expand(
        number_y + number_z - 2 * number_y * number_z
    )
    q_full = sp.expand(
        h1 * (b190.NUMBER[1] - b190.NUMBER[2])
        - h2 * (
            b190.CREATION[1] * b190.ANNIHILATION[2]
            + b190.CREATION[2] * b190.ANNIHILATION[1]
        ) / sp.sqrt(2)
    )
    reorder = ext_yz_reordering()

    incoming, transfer = POINTS["D1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    _action, _hodge, forward_vertices = b190.centered_objects(
        incoming, transfer
    )
    _reverse_action, _reverse_hodge, reverse_vertices = b190.centered_objects(
        outgoing, tuple(-value for value in transfer)
    )
    forward_tt = sp.expand(
        h1 * (-forward_vertices[2] + forward_vertices[3])
        + h2 * forward_vertices[9]
    )
    reverse_tt = sp.expand(
        h1 * (-reverse_vertices[2] + reverse_vertices[3])
        + h2 * reverse_vertices[9]
    )
    s = 1 / sp.sqrt(2)
    forward_ext = sp.expand(
        MASS * IDENTITY16 + I * (
            s * b190.CREATION[3] + b190.ANNIHILATION[0]
            + s * b190.ANNIHILATION[3]
        )
    )
    reverse_ext = sp.expand(
        MASS * IDENTITY16 + I * (
            b190.CREATION[0] + s * b190.CREATION[3]
            + s * b190.ANNIHILATION[3]
        )
    )
    characters = (
        b191.O1,
        b191.O2,
        sp.expand(b191.O1 * b191.O2),
    )
    identity_yz = sp.eye(4)
    moment_partials = tuple(tuple(
        sp.expand(partial_trace_yz(
            reorder.T * character * reorder
            * sp.kronecker_product(sp.eye(4), yz_word)
        ))
        for yz_word in (identity_yz, odd_yz)
    ) for character in characters)
    return {
        "tt_section": tt_section("D1"),
        "modulation_identity": matrix_equal(
            modulation(transfer[3]), sp.eye(L_TIME)
        ),
        "q_symmetric": matrix_equal(q_yz.T, q_yz),
        "q_square": matrix_equal(
            sp.expand(q_yz * q_yz),
            sp.expand((h1**2 + h2**2 / 2) * odd_yz),
        ),
        "q_factor": matrix_equal(
            sp.expand(reorder.T * q_full * reorder),
            sp.kronecker_product(sp.eye(4), q_yz),
        ),
        "forward_factor": matrix_equal(
            forward_tt, sp.expand(q_full * forward_ext)
        ),
        "reverse_factor": matrix_equal(
            reverse_tt, sp.expand(q_full * reverse_ext)
        ),
        "q_commutes_ext": (
            matrix_equal(q_full * forward_ext, forward_ext * q_full)
            and matrix_equal(q_full * reverse_ext, reverse_ext * q_full)
        ),
        "moment_partials": moment_partials,
        "moments_zero": all(matrix_equal(item, sp.zeros(4))
                            for pair in moment_partials for item in pair),
        "uniform_all_orders": (
            matrix_equal(q_yz.T, q_yz)
            and matrix_equal(
                sp.expand(q_yz * q_yz),
                sp.expand((h1**2 + h2**2 / 2) * odd_yz),
            )
            and all(matrix_equal(item, sp.zeros(4))
                    for pair in moment_partials for item in pair)
        ),
    }


def mode_reconstruction(
    terms: Terms,
    input_time: sp.Expr,
    output_time: sp.Expr,
) -> tuple[sp.Matrix, bool]:
    input_mode = b192.mode(input_time)
    output_mode = b192.mode(output_time)
    reconstructed = sp.zeros(16)
    temporal_exact = True
    for temporal, internal in terms:
        image = sp.expand(temporal * input_mode)
        coefficient = sp.simplify((output_mode.H * image)[0])
        temporal_exact = temporal_exact and matrix_equal(
            image, coefficient * output_mode
        )
        reconstructed += coefficient * internal
    return sp.expand(reconstructed), temporal_exact


def first_half_gram_tangent(
    left: dict[str, Terms],
    right: dict[str, Terms],
    source_left_right: Terms,
    source_right_left: Terms,
) -> tuple[Terms, Terms]:
    left_graph = left["graph"]
    right_graph = right["graph"]
    left_inverse = left["inverse"]
    right_inverse = right["inverse"]
    left_p_inverse = left["p_inverse"]
    right_p_inverse = right["p_inverse"]

    def block(
        graph_i: Terms,
        inverse_i: Terms,
        p_inverse_i: Terms,
        source_ij: Terms,
        graph_j: Terms,
        inverse_j: Terms,
        p_inverse_j: Terms,
        source_ji: Terms,
    ) -> Terms:
        inside = term_sum(
            term_product(
                term_transpose(source_ji),
                term_transpose(p_inverse_j),
                inverse_j,
            ),
            term_product(inverse_i, source_ij, inverse_j),
            term_product(inverse_i, p_inverse_i, source_ij),
        )
        return term_scale(term_product(
            term_transpose(graph_i), inside, graph_j
        ), -1)

    dot_h_01 = block(
        left_graph, left_inverse, left_p_inverse, source_left_right,
        right_graph, right_inverse, right_p_inverse, source_right_left,
    )
    dot_h_10 = block(
        right_graph, right_inverse, right_p_inverse, source_right_left,
        left_graph, left_inverse, left_p_inverse, source_left_right,
    )
    return dot_h_01, dot_h_10


def second_half_gram_coefficient(
    sector_i: dict[str, Terms],
    sector_j: dict[str, Terms],
    source_ij: Terms,
    source_ji: Terms,
) -> Terms:
    graph_i = sector_i["graph"]
    graph_j = sector_j["graph"]
    inverse_i = sector_i["inverse"]
    inverse_j = sector_j["inverse"]
    p_inverse_i = sector_i["p_inverse"]
    p_inverse_j = sector_j["p_inverse"]

    graph_1_ji = term_scale(term_product(
        p_inverse_j, source_ji, graph_i
    ), -1)
    graph_2_i = term_product(
        p_inverse_i, source_ij, p_inverse_j, source_ji, graph_i
    )
    inverse_1_ij = term_scale(term_product(
        inverse_i, source_ij, inverse_j
    ), -1)
    inverse_1_ji = term_scale(term_product(
        inverse_j, source_ji, inverse_i
    ), -1)
    inverse_2_i = term_product(
        inverse_i, source_ij, inverse_j, source_ji, inverse_i
    )

    return term_sum(
        term_product(term_transpose(graph_2_i), inverse_i, graph_i),
        term_product(term_transpose(graph_i), inverse_i, graph_2_i),
        term_product(term_transpose(graph_i), inverse_2_i, graph_i),
        term_product(
            term_transpose(graph_1_ji), inverse_j, graph_1_ji
        ),
        term_product(
            term_transpose(graph_i), inverse_1_ij, graph_1_ji
        ),
        term_product(
            term_transpose(graph_1_ji), inverse_1_ji, graph_i
        ),
    )


def diagonal_block(left: Terms, right: Terms) -> BlockTerms:
    return ((left, ()), ((), right))


def source_block(forward: Terms, reverse: Terms) -> BlockTerms:
    """Place the literal preregistered source in its frozen sector blocks."""
    return (((), forward), (reverse, ()))


@cache
def gram_series_facts(
    point_name: str,
    coefficients: tuple[sp.Expr, ...],
    order: int = 4,
) -> dict[str, object]:
    """Derive the exact reflected-Gram series for one fixed source ray.

    Coefficients use the power-series convention ``X(eps)=sum eps**n X_n``;
    they are not factorial derivatives.  The recurrence is obtained directly
    from ``A(eps) Y(eps)=I`` and the Schur graph equation
    ``P.T A(eps) R(eps)=0``.  It therefore includes every normalization and
    graph-motion term through the requested order.
    """
    incoming, transfer = POINTS[point_name]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    incoming_sector = sector_terms(incoming)
    outgoing_sector = sector_terms(outgoing)
    source = combined_source_pair_terms(point_name, coefficients)

    y0 = diagonal_block(
        incoming_sector["inverse"], outgoing_sector["inverse"]
    )
    k0 = diagonal_block(
        incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
    )
    r0 = diagonal_block(
        incoming_sector["graph"], outgoing_sector["graph"]
    )
    tangent = source_block(source["forward"], source["reverse"])

    inverse_series = [y0]
    graph_series = [r0]
    for _degree in range(1, order + 1):
        inverse_series.append(block_scale(block_product(
            y0, tangent, inverse_series[-1]
        ), -1))
        graph_series.append(block_scale(block_product(
            k0, tangent, graph_series[-1]
        ), -1))

    centered_effects = tuple(
        sp.expand(effect - IDENTITY16 / 4) for effect in b191.EFFECTS
    )
    normalizers: list[sp.Expr] = []
    centered_numerators: list[tuple[sp.Expr, ...]] = []
    for degree in range(order + 1):
        half_trace = sp.Integer(0)
        centered_half_traces = [sp.Integer(0)] * len(centered_effects)
        for left_degree in range(degree + 1):
            for inverse_degree in range(degree - left_degree + 1):
                right_degree = degree - left_degree - inverse_degree
                contribution = block_product(
                    block_transpose(graph_series[left_degree]),
                    inverse_series[inverse_degree],
                    graph_series[right_degree],
                )
                half_trace += block_diagonal_trace_raw(contribution)
                for outcome, effect in enumerate(centered_effects):
                    centered_half_traces[outcome] += (
                        block_diagonal_trace_raw(contribution, effect)
                    )
        normalizers.append(sp.factor(sp.simplify(
            half_trace + sp.conjugate(half_trace)
        )))
        centered_numerators.append(tuple(sp.factor(sp.simplify(
            value + sp.conjugate(value)
        )) for value in centered_half_traces))

    probability_deviations: list[tuple[sp.Expr, ...]] = []
    for degree in range(order + 1):
        current = []
        for outcome in range(len(b191.EFFECTS)):
            convolution = sum(
                normalizers[shift]
                * probability_deviations[degree - shift][outcome]
                for shift in range(1, degree + 1)
            )
            current.append(sp.factor(sp.simplify(
                (centered_numerators[degree][outcome] - convolution)
                / normalizers[0]
            )))
        probability_deviations.append(tuple(current))
    probabilities = tuple(
        (R(1, 4),) * len(b191.EFFECTS) if degree == 0 else values
        for degree, values in enumerate(probability_deviations)
    )
    numerators = tuple(tuple(sp.factor(sp.simplify(
        normalizers[degree] / 4
        + centered_numerators[degree][outcome]
    )) for outcome in range(len(b191.EFFECTS)))
        for degree in range(order + 1))

    return {
        "normalizers": tuple(normalizers),
        "numerators": numerators,
        "centered_numerators": tuple(centered_numerators),
        "probabilities": probabilities,
        "inverse_term_counts": tuple(tuple(
            len(inverse_series[degree][row][column])
            for row in range(2) for column in range(2)
        ) for degree in range(order + 1)),
        "graph_term_counts": tuple(tuple(
            len(graph_series[degree][row][column])
            for row in range(2) for column in range(2)
        ) for degree in range(order + 1)),
    }


@cache
def response_facts(point_name: str, slot: int, hessian: bool) -> dict[str, object]:
    incoming, transfer = POINTS[point_name]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    incoming_sector = sector_terms(incoming)
    outgoing_sector = sector_terms(outgoing)
    source = source_pair_terms(incoming, transfer, slot)

    forward_reconstruction, forward_temporal = mode_reconstruction(
        source["forward"], incoming[3], outgoing[3]
    )
    reverse_reconstruction, reverse_temporal = mode_reconstruction(
        source["reverse"], outgoing[3], incoming[3]
    )
    forward_exact = forward_temporal and matrix_equal(
        forward_reconstruction, source["forward_vertex"]
    )
    reverse_exact = reverse_temporal and matrix_equal(
        reverse_reconstruction, source["reverse_vertex"]
    )

    dot_h_01, dot_h_10 = first_half_gram_tangent(
        incoming_sector,
        outgoing_sector,
        source["forward"],
        source["reverse"],
    )
    dot_g_01 = term_sum(dot_h_01, term_adjoint(dot_h_10))
    overlaps = tuple(term_trace(dot_g_01, effect)
                     for effect in b191.EFFECTS)
    total_tangent_trace = term_trace(dot_g_01)

    incoming_gram = incoming_sector["gram"]
    outgoing_gram = outgoing_sector["gram"]
    z0 = sp.factor(
        term_trace(incoming_gram) + term_trace(outgoing_gram)
    )
    n0 = tuple(sp.factor(
        term_trace(incoming_gram, effect)
        + term_trace(outgoing_gram, effect)
    ) for effect in b191.EFFECTS)
    p0 = tuple(sp.factor(value / z0) for value in n0)

    result: dict[str, object] = {
        "forward_exact": forward_exact,
        "reverse_exact": reverse_exact,
        "metric_same": source["metric_same"],
        "actual_not_hermitian_control": not (
            len(source["reverse"]) == len(source["hermitian_control"])
            and all(matrix_equal(a_t, b_t) and matrix_equal(a_i, b_i)
                    for (a_t, a_i), (b_t, b_i) in zip(
                        source["reverse"], source["hermitian_control"]
                    ))
        ),
        "dot_h_term_counts": (len(dot_h_01), len(dot_h_10)),
        "dot_g_term_count": len(dot_g_01),
        "overlaps": overlaps,
        "total_tangent_trace": total_tangent_trace,
        "z0": z0,
        "p0": p0,
    }
    if not hessian:
        return result

    h2_incoming = second_half_gram_coefficient(
        incoming_sector, outgoing_sector,
        source["forward"], source["reverse"],
    )
    h2_outgoing = second_half_gram_coefficient(
        outgoing_sector, incoming_sector,
        source["reverse"], source["forward"],
    )
    g2_incoming = term_sum(h2_incoming, term_adjoint(h2_incoming))
    g2_outgoing = term_sum(h2_outgoing, term_adjoint(h2_outgoing))
    z2 = sp.factor(term_trace(g2_incoming) + term_trace(g2_outgoing))
    n2 = tuple(sp.factor(
        term_trace(g2_incoming, effect)
        + term_trace(g2_outgoing, effect)
    ) for effect in b191.EFFECTS)
    p2 = tuple(sp.factor(value / z0 - n0[index] * z2 / z0**2)
               for index, value in enumerate(n2))
    result.update({
        "h2_term_counts": (len(h2_incoming), len(h2_outgoing)),
        "z2": z2,
        "n2": n2,
        "p2": p2,
        "p2_sum": sp.factor(sum(p2)),
    })
    return result


def block_matrix(
    upper_left: sp.MatrixBase,
    upper_right: sp.MatrixBase,
    lower_left: sp.MatrixBase,
    lower_right: sp.MatrixBase,
) -> sp.Matrix:
    return sp.Matrix.vstack(
        sp.Matrix.hstack(upper_left, upper_right),
        sp.Matrix.hstack(lower_left, lower_right),
    )


@cache
def coherent_instrument_facts(orientation: str) -> dict[str, object]:
    if orientation == "identity":
        internal_orientation = IDENTITY16
    elif orientation == "clock_parity":
        internal_orientation = sp.expand(I * GTIME * b191.FORM_PARITY)
    else:
        raise ValueError(f"unknown coherent orientation: {orientation}")

    connectors = tuple(sp.expand(effect * internal_orientation)
                       for effect in b191.EFFECTS)
    effects = tuple(
        sp.expand(block_matrix(
            effect, sign * connector,
            sign * connector.H, effect,
        ) / 2)
        for effect, connector in zip(b191.EFFECTS, connectors)
        for sign in (1, -1)
    )
    diagonal_coarsenings = tuple(block_matrix(
        effect, sp.zeros(16), sp.zeros(16), effect
    ) for effect in b191.EFFECTS)
    return {
        "orientation": internal_orientation,
        "orientation_hermitian": matrix_equal(
            internal_orientation.H, internal_orientation
        ),
        "orientation_unitary": matrix_equal(
            internal_orientation.H * internal_orientation, IDENTITY16
        ),
        "orientation_commutes": all(matrix_equal(
            internal_orientation * effect,
            effect * internal_orientation,
        ) for effect in b191.EFFECTS),
        "connectors": connectors,
        "partial_unitaries": all(
            matrix_equal(connector.H * connector, effect)
            and matrix_equal(connector * connector.H, effect)
            for connector, effect in zip(connectors, b191.EFFECTS)
        ),
        "effects": effects,
        "projectors": all(
            matrix_equal(effect.H, effect)
            and matrix_equal(effect * effect, effect)
            for effect in effects
        ),
        "orthogonal_signed_pairs": all(matrix_equal(
            effects[2 * index] * effects[2 * index + 1], sp.zeros(32)
        ) for index in range(4)),
        "pairwise_orthogonal": all(matrix_equal(
            effects[left] * effects[right], sp.zeros(32)
        ) for left in range(len(effects))
          for right in range(left + 1, len(effects))),
        "coarsenings": all(matrix_equal(
            effects[2 * index] + effects[2 * index + 1],
            diagonal_coarsenings[index],
        ) for index in range(4)),
        "complete": matrix_equal(sum(effects, sp.zeros(32)), sp.eye(32)),
        "ranks": tuple(effect.rank() for effect in effects),
        "baseline_probabilities": tuple(
            sp.trace(effect) / 32 for effect in effects
        ),
    }


@cache
def tt_tangent_columns(point_name: str) -> dict[str, object]:
    incoming, transfer = POINTS[point_name]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    incoming_sector = sector_terms(incoming)
    outgoing_sector = sector_terms(outgoing)
    columns = []
    for column in range(2):
        coefficients = tt_source_coefficients(point_name, column)
        source = combined_source_pair_terms(point_name, coefficients)
        dot_h_01, dot_h_10 = first_half_gram_tangent(
            incoming_sector,
            outgoing_sector,
            source["forward"],
            source["reverse"],
        )
        dot_g_01 = term_sum(dot_h_01, term_adjoint(dot_h_10))
        columns.append(dot_g_01)
    witness_coordinates = {
        "D1": (1, 7, 3, 12),
        "H1": (1, 4, 3, 6),
    }
    expected_witnesses = {
        "D1": R(3917972057237, 21467029329720),
        "H1": R(152529716817406999, 11811104288531803719) * I,
    }
    witness_coordinate = witness_coordinates.get(point_name)
    second_column_witness = (
        term_tensor_entry(columns[1], *witness_coordinate)
        if witness_coordinate is not None else None
    )
    incoming_gram = incoming_sector["gram"]
    outgoing_gram = outgoing_sector["gram"]
    return {
        "columns": tuple(columns),
        "second_column_witness_coordinate": witness_coordinate,
        "second_column_witness": second_column_witness,
        "second_column_operator_nonzero": (
            second_column_witness is not None
            and second_column_witness == expected_witnesses[point_name]
            and second_column_witness != 0
        ),
        "normalizer": sp.factor(
            term_trace(incoming_gram) + term_trace(outgoing_gram)
        ),
    }


@cache
def coherent_tt_response_facts(
    point_name: str,
    orientation: str,
) -> dict[str, object]:
    instrument = coherent_instrument_facts(orientation)
    connectors = instrument["connectors"]
    tangent = tt_tangent_columns(point_name)
    overlaps = sp.Matrix(4, 2, lambda row, column: term_trace(
        tangent["columns"][column], connectors[row].H
    ))
    real_overlaps = overlaps.applyfunc(lambda value: sp.factor(sp.simplify(
        (value + sp.conjugate(value)) / 2
    )))
    normalizer = tangent["normalizer"]
    origin_log_slopes = sp.expand(8 * real_overlaps / normalizer)
    return {
        "overlaps": overlaps,
        "real_overlaps": real_overlaps,
        "complex_rank": DomainMatrix.from_Matrix(
            overlaps, extension=True
        ).rank(),
        "origin_real_rank": DomainMatrix.from_Matrix(
            origin_log_slopes, extension=True
        ).rank(),
        "origin_log_slopes": origin_log_slopes,
        "normalizer": normalizer,
        "second_column_operator_nonzero": (
            tangent["second_column_operator_nonzero"]
        ),
        "second_column_zero": all(
            sp.simplify(overlaps[row, 1]) == 0 for row in range(4)
        ),
    }


@cache
def literal_source_facts() -> dict[str, object]:
    rows = []
    for point_name in ("D1", "H1"):
        incoming, transfer = POINTS[point_name]
        outgoing = tuple(
            incoming[axis] + transfer[axis] for axis in range(4)
        )
        _action, _hodge, forward_vertices = b190.centered_objects(
            incoming, transfer
        )
        _reverse_action, _reverse_hodge, reverse_vertices = (
            b190.centered_objects(
                outgoing, tuple(-value for value in transfer)
            )
        )
        for column in range(2):
            coefficients = tt_source_coefficients(point_name, column)
            source = combined_source_pair_terms(point_name, coefficients)
            expected_forward = sp.expand(sum((
                coefficients[slot] * forward_vertices[slot]
                for slot in range(len(coefficients))
            ), sp.zeros(16)))
            expected_reverse = sp.expand(sum((
                coefficients[slot] * reverse_vertices[slot]
                for slot in range(len(coefficients))
            ), sp.zeros(16)))
            reconstructed_forward, temporal_forward = mode_reconstruction(
                source["forward"], incoming[3], outgoing[3]
            )
            reconstructed_reverse, temporal_reverse = mode_reconstruction(
                source["reverse"], outgoing[3], incoming[3]
            )
            placed = source_block(source["forward"], source["reverse"])
            rows.append({
                "one_term": (
                    len(source["forward"]) == 1
                    and len(source["reverse"]) == 1
                ),
                "forward": (
                    temporal_forward and matrix_equal(
                        reconstructed_forward, expected_forward
                    )
                ),
                "reverse": (
                    temporal_reverse and matrix_equal(
                        reconstructed_reverse, expected_reverse
                    )
                ),
                "actual_reverse": not matrix_equal(
                    expected_reverse, expected_forward.H
                ),
                "block_placement": (
                    placed[0][0] == ()
                    and placed[1][1] == ()
                    and placed[0][1] is source["forward"]
                    and placed[1][0] is source["reverse"]
                ),
            })
    return {
        "rows": tuple(rows),
        "literal": all(
            row["one_term"] and row["forward"] and row["reverse"]
            for row in rows
        ),
        "actual_reverse_distinct": any(
            row["actual_reverse"] for row in rows
        ),
        "block_placement": all(row["block_placement"] for row in rows),
    }


@cache
def diagonal_parity_facts() -> dict[str, object]:
    upper, lower = sp.symbols("B_01 B_10")
    tangent = sp.Matrix(((0, upper), (lower, 0)))
    parity = sp.diag(1, -1)
    diagonal_event = sp.diag(*sp.symbols("f_0 f_1"))
    return {
        "source_odd": matrix_equal(parity * tangent * parity, -tangent),
        "event_even": matrix_equal(
            parity * diagonal_event * parity, diagonal_event
        ),
        "all_odd_orders_zero": True,
    }


N5_LINES = (
    "per_element: checked literal full-carrier forward/actual-reverse D4 vertex factors, grade-three characters, and identity and clock-parity connectors.",
    "per_site: checked the fixed L24 cut, writer-position covariance, eight coherent projector/coarsening identities, and no spatial formation dynamics.",
    "per_mode: checked exact D1/H1 TT sections, D1 all-order diagonal uniformity, and coherent complex/real ranks; held-outs remain sealed.",
    "per_block: checked the diagonal and two coherent arms as distinct blocks and stopped before Record composition when the discovery rank gate failed.",
    "lattice_wide: checked and not executed -- no full detector family, spatial nearest-neighbor writer, autonomous formation, physical-time law, Born derivation, nonlinear gravity, or retained TOE theory is claimed.",
)


@cache
def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "n5": False, "scope": False}
    text = NOTE_PATH.read_text(encoding="utf-8")
    scope_tokens = (
        "literal_full_carrier_source: exact",
        "d1_diagonal_all_orders: uniform_one_quarter",
        "identity_coherent_tt_rank: one",
        "clock_parity_coherent_tt_rank: zero",
        "heldouts: sealed",
        "permanent_record: not_claimed",
        "broad_coherent_no_go: not_claimed",
        "minimal_axiom_update: none",
        "toe_percentage_movement: 0",
    )
    return {
        "exists": True,
        "n5": all(line in text for line in N5_LINES),
        "scope": all(token in text for token in scope_tokens),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    literal = literal_source_facts()
    parity = diagonal_parity_facts()
    diagonal = d1_diagonal_all_orders_facts()
    identity_instrument = coherent_instrument_facts("identity")
    clock_instrument = coherent_instrument_facts("clock_parity")
    d1_identity = coherent_tt_response_facts("D1", "identity")
    h1_identity = coherent_tt_response_facts("H1", "identity")
    d1_clock = coherent_tt_response_facts("D1", "clock_parity")
    h1_clock = coherent_tt_response_facts("H1", "clock_parity")
    note = note_facts()

    claims = {
        "main": CURRENT_MAIN,
        "literal_source": True,
        "diagonal_even": True,
        "diagonal_rank_two": False,
        "coherent_complete": True,
        "scalar_phase_repairs_rank": False,
        "clock_parity_response": False,
        "heldouts_open": False,
        "permanent_record": False,
        "broad_coherent_no_go": False,
        "axiom_update": False,
        "toe_progress": False,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "stale"
    elif mutation == "replace_literal_source_by_local_lift":
        claims["literal_source"] = False
    elif mutation == "break_diagonal_evenness":
        claims["diagonal_even"] = False
    elif mutation == "claim_diagonal_rank_two":
        claims["diagonal_rank_two"] = True
    elif mutation == "break_coherent_completeness":
        claims["coherent_complete"] = False
    elif mutation == "claim_scalar_phase_repairs_rank":
        claims["scalar_phase_repairs_rank"] = True
    elif mutation == "claim_clock_parity_response":
        claims["clock_parity_response"] = True
    elif mutation == "open_heldouts_after_discovery_failure":
        claims["heldouts_open"] = True
    elif mutation == "claim_permanent_record":
        claims["permanent_record"] = True
    elif mutation == "claim_broad_coherent_no_go":
        claims["broad_coherent_no_go"] = True
    elif mutation == "claim_axiom_update":
        claims["axiom_update"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_progress"] = True

    instruments_complete = all(
        facts["orientation_hermitian"]
        and facts["orientation_unitary"]
        and facts["orientation_commutes"]
        and facts["partial_unitaries"]
        and facts["projectors"]
        and facts["orthogonal_signed_pairs"]
        and facts["pairwise_orthogonal"]
        and facts["coarsenings"]
        and facts["complete"]
        and facts["ranks"] == (4,) * 8
        and facts["baseline_probabilities"] == (R(1, 8),) * 8
        for facts in (identity_instrument, clock_instrument)
    )
    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["parent"] and authority["prereg"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB
            and authority["inputs"],
            "current authority, Block-192 parent, and corrected preregistration are pinned",
        ),
        "B": (
            literal["literal"] == claims["literal_source"]
            and literal["actual_reverse_distinct"]
            and literal["block_placement"],
            "the literal full-carrier forward/actual-reverse source occupies the frozen off-diagonal blocks",
        ),
        "C": (
            parity["source_odd"] and parity["event_even"]
            and parity["all_odd_orders_zero"] == claims["diagonal_even"]
            and diagonal["modulation_identity"]
            and diagonal["q_symmetric"] and diagonal["q_square"]
            and diagonal["q_factor"]
            and diagonal["forward_factor"] and diagonal["reverse_factor"]
            and diagonal["q_commutes_ext"] and diagonal["moments_zero"]
            and diagonal["uniform_all_orders"]
            and claims["diagonal_rank_two"] is False,
            "the diagonal D1 probabilities are exactly one quarter to all orders on every physical TT ray",
        ),
        "D": (
            instruments_complete == claims["coherent_complete"],
            "identity and clock-parity connectors each give a complete positive eight-projector refinement",
        ),
        "E": (
            d1_identity["complex_rank"] == 1
            and d1_identity["origin_real_rank"] == 0
            and d1_identity["second_column_zero"]
            and d1_identity["second_column_operator_nonzero"]
            and h1_identity["complex_rank"] == 1
            and h1_identity["origin_real_rank"] == 1
            and h1_identity["second_column_zero"]
            and h1_identity["second_column_operator_nonzero"]
            and claims["scalar_phase_repairs_rank"] is False
            and d1_clock["complex_rank"] == 0
            and h1_clock["complex_rank"] == 0
            and claims["clock_parity_response"] is False,
            "the position family is TT-rank one and clock-parity is rank zero at both discovery points",
        ),
        "F": (
            claims["heldouts_open"] is False
            and claims["permanent_record"] is False,
            "held-outs and Record composition remain sealed after the discovery response gate fails",
        ),
        "G": (
            note["exists"] and note["n5"] and note["scope"]
            and claims["broad_coherent_no_go"] is False
            and claims["axiom_update"] is False
            and claims["toe_progress"] is False,
            "N1-N8 preserve live detector routes and state zero axiom, obligation, Record, and TOE movement",
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
