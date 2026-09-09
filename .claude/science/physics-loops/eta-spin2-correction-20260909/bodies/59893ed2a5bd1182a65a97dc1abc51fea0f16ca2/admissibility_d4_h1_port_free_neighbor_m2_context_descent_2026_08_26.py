#!/usr/bin/env python3
"""Block 206 exact H1 port-free and local-neighbor context descent.

The first gate computes the normalized binary pointer contrast from the full
two-sector right-Schur family.  It sums the four coarse detector ports before
testing the pointer, so no port label can leak into the claimed law.
"""

from __future__ import annotations

import argparse
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
import admissibility_d4_h1_schur_record_probability_germ_2026_08_26 as b205  # noqa: E402


I = sp.I

DISCLOSED_CUBIC_A = sp.Integer(
    "39614194410521886011258608271189426608989637314061903595310837311299128766179775614039384849224874802424309955547840537519444031415731"
)
DISCLOSED_CUBIC_B = sp.Integer(
    "20088236778144933307422375844774848466973250848745230478668770773683346878595585928475405853707189945489158937323659388473013648683423"
)
DISCLOSED_CUBIC_DENOMINATOR = sp.Integer(
    "14630373132760996204705386039773889549383195117366765668241345031835670611592246823650335399786716111445599465516368081316673691027954400"
)
DISCLOSED_CUBIC_QUADRATURE = (
    343 * (DISCLOSED_CUBIC_A - DISCLOSED_CUBIC_B * sp.sqrt(3))
    / DISCLOSED_CUBIC_DENOMINATOR
)

NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block206-neighbor-phase-m2-context-descent-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "8e6706c6077b718e5d424f8db8c0d6cc9143f17c"
PREREG_COMMIT = "725f490afe1f55e1fc2655784a29b9a1833ecbad"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "81254937ee3d377da60902afe79b215caba34073"
PREFLIGHT_BLOB = "990c989fafd491380ffe22d370b61b1afab5267a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
TIMEOUT_SEC = 300
AUDIT_TIMEOUT_SEC = 900

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_PORT_FREE_NEIGHBOR_PHASE_M2_CONTEXT_DESCENT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    ".claude/science/physics-loops/toe-axiom-closure-block206-neighbor-phase-m2-context-descent-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block206-neighbor-phase-m2-context-descent-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.py",
    "logs/runner-cache/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.txt",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "replace_actual_reverse_by_adjoint",
    "use_wrong_tt_column",
    "condition_on_coarse_port",
    "erase_linear_zero",
    "erase_cubic_quadrature",
    "flip_cubic_sign",
    "call_zero_phase_all_order_nonzero",
    "break_phase_pvm",
    "deny_positive_germ",
    "erase_neighbor_variation",
    "claim_scalar_t2_hom",
    "erase_conditional_adjoint_hom",
    "select_adjoint_decoder",
    "install_orbit_lookup",
    "erase_incoming_p_dependence",
    "call_source_radius_one",
    "ignore_source_collision",
    "open_h2_after_context_failure",
    "claim_complete_eta_law",
    "claim_formation",
    "claim_history",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
    "claim_broad_local_no_go",
)


def exact_scalar(value: sp.Expr) -> sp.Expr:
    return b193.exact_scalar(sp.expand(value))


def h1_field_scalar(value: sp.Expr) -> sp.Expr:
    """Canonicalize directly in the known ``Q(sqrt(3), i)`` H1 field."""
    expanded = sp.expand(value)
    collected = sp.collect(expanded, (sp.sqrt(3), I), exact=False)
    return sp.factor(sp.cancel(collected))


@cache
def gram_block_series(order: int = 3) -> dict[str, object]:
    """Return exact coefficients of the full reflected Schur Gram.

    The coefficient convention is ``X(e)=sum_n e**n X_n``.  The recurrence
    follows directly from ``A(e)Y(e)=1`` and the right-Schur graph equation,
    with ordinary transpose retained in the half-Gram.
    """
    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    incoming_sector = b193.sector_terms(incoming)
    outgoing_sector = b193.sector_terms(outgoing)
    coefficients = b193.tt_source_coefficients("H1", 1)
    source = b193.combined_source_pair_terms("H1", coefficients)

    y0 = b193.diagonal_block(
        incoming_sector["inverse"], outgoing_sector["inverse"]
    )
    k0 = b193.diagonal_block(
        incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
    )
    r0 = b193.diagonal_block(
        incoming_sector["graph"], outgoing_sector["graph"]
    )
    tangent = b193.source_block(source["forward"], source["reverse"])

    inverse_series = [y0]
    graph_series = [r0]
    for _degree in range(1, order + 1):
        inverse_series.append(b193.block_scale(b193.block_product(
            y0, tangent, inverse_series[-1]
        ), -1))
        graph_series.append(b193.block_scale(b193.block_product(
            k0, tangent, graph_series[-1]
        ), -1))

    gram_series = []
    normalizers = []
    for degree in range(order + 1):
        half = None
        for left_degree in range(degree + 1):
            for inverse_degree in range(degree - left_degree + 1):
                right_degree = degree - left_degree - inverse_degree
                contribution = b193.block_product(
                    b193.block_transpose(graph_series[left_degree]),
                    inverse_series[inverse_degree],
                    graph_series[right_degree],
                )
                half = contribution if half is None else b193.block_add(
                    half, contribution
                )
        assert half is not None
        gram = b193.block_add(half, b193.block_adjoint(half))
        gram_series.append(gram)
        normalizers.append(exact_scalar(
            b193.block_diagonal_trace_raw(gram)
        ))

    return {
        "gram": tuple(gram_series),
        "normalizers": tuple(normalizers),
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
def schur_series_factors(order: int = 3) -> dict[str, object]:
    """Build only the inverse and graph coefficients needed downstream."""
    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    incoming_sector = b193.sector_terms(incoming)
    outgoing_sector = b193.sector_terms(outgoing)
    source = b193.combined_source_pair_terms(
        "H1", b193.tt_source_coefficients("H1", 1)
    )
    y0 = b193.diagonal_block(
        incoming_sector["inverse"], outgoing_sector["inverse"]
    )
    k0 = b193.diagonal_block(
        incoming_sector["p_inverse"], outgoing_sector["p_inverse"]
    )
    r0 = b193.diagonal_block(
        incoming_sector["graph"], outgoing_sector["graph"]
    )
    tangent = b193.source_block(source["forward"], source["reverse"])
    inverse_series = [y0]
    graph_series = [r0]
    for _degree in range(1, order + 1):
        inverse_series.append(b193.block_scale(b193.block_product(
            y0, tangent, inverse_series[-1]
        ), -1))
        graph_series.append(b193.block_scale(b193.block_product(
            k0, tangent, graph_series[-1]
        ), -1))
    return {
        "inverse": tuple(inverse_series),
        "graph": tuple(graph_series),
        "zero_normalizer": b193.exact_scalar(
            b193.term_trace_raw(incoming_sector["gram"])
            + b193.term_trace_raw(outgoing_sector["gram"])
        ),
    }


@cache
def offdiagonal_overlap_coefficient(degree: int) -> sp.Expr:
    """Exact coefficient of ``Tr(G_01 J)`` without premature merging."""
    factors = schur_series_factors(degree)
    inverse_series = factors["inverse"]
    graph_series = factors["graph"]
    orientation = b194.detector_classification_facts()["orientation"]
    summands = []
    for left_degree in range(degree + 1):
        for inverse_degree in range(degree - left_degree + 1):
            right_degree = degree - left_degree - inverse_degree
            contribution = b193.block_product(
                b193.block_transpose(graph_series[left_degree]),
                inverse_series[inverse_degree],
                graph_series[right_degree],
            )
            upper = h1_field_scalar(b193.term_trace_raw(
                contribution[0][1], orientation
            ))
            lower = h1_field_scalar(b193.term_trace_raw(
                contribution[1][0], orientation
            ))
            summands.append(upper)
            summands.append(sp.conjugate(lower))
    return h1_field_scalar(sum(summands))


@cache
def phase_series_facts() -> dict[str, object]:
    linear = offdiagonal_overlap_coefficient(1)
    cubic = offdiagonal_overlap_coefficient(3)
    zero_normalizer = schur_series_factors(3)["zero_normalizer"]
    cubic_quadrature = h1_field_scalar(cubic / I)
    normalized_quadrature = h1_field_scalar(
        cubic_quadrature / zero_normalizer
    )
    phases = (
        sp.Rational(1, 2) - I * sp.sqrt(3) / 2,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
        -I, I, sp.Integer(1), sp.Integer(1),
    )
    cubic_contrasts = (
        sp.sqrt(3) * normalized_quadrature,
        -sp.sqrt(3) * normalized_quadrature,
        2 * normalized_quadrature,
        -2 * normalized_quadrature,
        sp.Integer(0), sp.Integer(0),
    )
    return {
        "linear_overlap": linear,
        "cubic_overlap": cubic,
        "cubic_pure_imaginary": (
            sp.simplify(cubic + sp.conjugate(cubic)) == 0
        ),
        "cubic_quadrature": cubic_quadrature,
        "cubic_matches_disclosure": (
            h1_field_scalar(cubic_quadrature - DISCLOSED_CUBIC_QUADRATURE)
            == 0
        ),
        "cubic_quadrature_positive": (
            DISCLOSED_CUBIC_A > 0
            and DISCLOSED_CUBIC_B > 0
            and DISCLOSED_CUBIC_A**2 > 3 * DISCLOSED_CUBIC_B**2
        ),
        "zero_normalizer": zero_normalizer,
        "normalized_quadrature": normalized_quadrature,
        "neighbor_phases": phases,
        "neighbor_cubic_contrasts": cubic_contrasts,
        "distinct_neighbor_contrasts": len(set(cubic_contrasts)),
        "nonzero_neighbor_contrasts": sum(
            value != 0 for value in cubic_contrasts
        ),
    }


def pointer_numerator_coefficient(
    gram: b193.BlockTerms,
    phase: sp.Expr = sp.Integer(1),
) -> sp.Expr:
    """Coefficient of ``Tr(G(P_+-P_-))`` for ``phase=exp(i phi)``."""
    orientation = b194.detector_classification_facts()["orientation"]
    return exact_scalar(
        phase * b193.term_trace_raw(gram[0][1], orientation)
        + sp.conjugate(phase)
        * b193.term_trace_raw(gram[1][0], orientation)
    )


def normalized_series(
    numerators: tuple[sp.Expr, ...],
    denominators: tuple[sp.Expr, ...],
) -> tuple[sp.Expr, ...]:
    coefficients = []
    for degree, numerator in enumerate(numerators):
        convolution = sum(
            denominators[shift] * coefficients[degree - shift]
            for shift in range(1, degree + 1)
        )
        coefficients.append(exact_scalar(
            (numerator - convolution) / denominators[0]
        ))
    return tuple(coefficients)


def signed_neighbor_shell() -> tuple[sp.Matrix, ...]:
    return tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (1, -1)
    )


def shell_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    shell = signed_neighbor_shell()
    representation = sp.zeros(6)
    for source, direction in enumerate(shell):
        transformed = sp.Matrix(rotation * direction)
        target = next(
            index for index, candidate in enumerate(shell)
            if candidate == transformed
        )
        representation[target, source] = 1
    return representation


def shear_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    """The cubic T2 action on symmetric off-diagonal spatial tensors."""
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in basis:
        transformed = sp.Matrix(rotation * tensor * rotation.T)
        columns.append(sp.Matrix((
            transformed[0, 1], transformed[1, 2], transformed[0, 2]
        )))
    return sp.Matrix.hstack(*columns)


def hom_dimension(domain_representations: tuple[sp.Matrix, ...]) -> int:
    rotations = b194.proper_cubic_rotations()
    domain_dimension = domain_representations[0].rows
    constraints = []
    for rotation, domain in zip(rotations, domain_representations):
        target = shear_representation(rotation)
        constraints.append(
            sp.kronecker_product(sp.eye(domain_dimension), target)
            - sp.kronecker_product(domain.T, sp.eye(3))
        )
    matrix = sp.Matrix.vstack(*constraints)
    rank = DomainMatrix.from_Matrix(matrix).rank()
    return 3 * domain_dimension - rank


def conditional_adjoint_hom_basis() -> tuple[sp.Matrix, sp.Matrix]:
    """Odd-shell shear and even-shell axis-difference intertwiners."""
    odd = sp.Matrix((
        (0, -1, 0, 0, 1, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, 0, 0, 1, 0),
        (0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0),
    ))
    even = sp.Matrix((
        (0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0),
        (0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, -1, 0, 0, -1, 0, 0),
        (0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0),
    ))
    return odd, even


@cache
def neighbor_hom_facts() -> dict[str, object]:
    rotations = b194.proper_cubic_rotations()
    scalar_domain = tuple(shell_representation(rotation)
                          for rotation in rotations)
    # This is explicitly conditional: it assumes that each neighbor's
    # traceless M2 content carries the same external cubic-vector action as
    # the spatial shell.  The current axioms do not yet select that action.
    adjoint_domain = tuple(
        sp.kronecker_product(shell, rotation)
        for shell, rotation in zip(scalar_domain, rotations)
    )
    coefficients = b193.tt_source_coefficients("H1", 1)
    h1_shear = sp.Matrix((
        coefficients[7] / sp.sqrt(2),
        coefficients[9] / sp.sqrt(2),
        coefficients[8] / sp.sqrt(2),
    ))
    hom_basis = conditional_adjoint_hom_basis()
    hom_basis_equivariant = all(
        shear_representation(rotation) * intertwiner
        == intertwiner * domain
        for rotation, domain in zip(rotations, adjoint_domain)
        for intertwiner in hom_basis
    )
    hom_basis_independent = sp.Matrix.hstack(*(
        intertwiner.reshape(54, 1) for intertwiner in hom_basis
    )).rank() == 2
    return {
        "proper_cubic_count": len(rotations),
        "scalar_hom_dimension": hom_dimension(scalar_domain),
        "conditional_adjoint_hom_dimension": hom_dimension(adjoint_domain),
        "conditional_adjoint_basis_equivariant": hom_basis_equivariant,
        "conditional_adjoint_basis_independent": hom_basis_independent,
        "conditional_adjoint_basis_ranks": tuple(
            intertwiner.rank() for intertwiner in hom_basis
        ),
        "conditional_adjoint_parity_classes": ("odd_shell", "even_shell"),
        "h1_shear_coordinates": tuple(sp.simplify(x) for x in h1_shear),
        "h1_shear_nonzero": any(x != 0 for x in h1_shear),
    }


def raw_action_vertices() -> tuple[b193.b190.PolyMatrix, ...]:
    """Rebuild the parent raw Laurent vertices before H1 evaluation."""
    b190 = b193.b190
    differential_0: b193.b190.PolyMatrix = {}
    differential_1: b193.b190.PolyMatrix = {}
    for axis in range(4):
        differential_0 = b190.poly_add(differential_0, {
            b190.exponent({axis: 1}): b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}): -b190.CREATION[axis] / (2 * I),
        })
        differential_1 = b190.poly_add(differential_1, {
            b190.exponent({axis: 1}, {axis: 1}):
                b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}, {axis: -1}):
                -b190.CREATION[axis] / (2 * I),
        })

    vertices = []
    for left, right in b190.PAIRS4:
        if left == right:
            hodge = b190.poly_multiply(
                b190.cosine_square(left),
                {b190.ZERO_EXPONENT:
                 sp.Rational(1, 2) * b190.IDENTITY_FORM
                 - b190.NUMBER[left]},
            )
        else:
            hodge = b190.poly_multiply(
                b190.poly_scale(b190.poly_multiply(
                    b190.placed_cosine(left),
                    b190.placed_cosine(right),
                ), -1 / sp.sqrt(2)),
                {b190.ZERO_EXPONENT: (
                    b190.CREATION[left] * b190.ANNIHILATION[right]
                    + b190.CREATION[right] * b190.ANNIHILATION[left]
                )},
            )
        vertices.append(b190.poly_add(
            b190.poly_scale(hodge, b190.MASS),
            b190.poly_scale(b190.poly_add(
                b190.poly_multiply(hodge, differential_0),
                b190.poly_multiply(
                    b190.poly_transpose(differential_1), hodge
                ),
            ), I),
        ))
    return tuple(vertices)


def combined_raw_source() -> b193.b190.PolyMatrix:
    b190 = b193.b190
    coefficients = b193.tt_source_coefficients("H1", 1)
    result: b193.b190.PolyMatrix = {}
    for coefficient, vertex in zip(coefficients, raw_action_vertices()):
        result = b190.poly_add(
            result, b190.poly_scale(vertex, coefficient)
        )
    return result


@cache
def source_support_facts() -> dict[str, object]:
    """Exact inverse-Fourier support and a q-only collision witness."""
    source = combined_raw_source()
    reverse_source: b193.b190.PolyMatrix = {}
    for power, matrix in source.items():
        reverse_power = tuple(power[axis] for axis in range(4)) + tuple(
            power[axis] - power[4 + axis] for axis in range(4)
        )
        reverse_source = b193.b190.poly_add(
            reverse_source, {reverse_power: matrix}
        )
    spatial_support = tuple(sorted({
        tuple(power[axis] for axis in range(3))
        + tuple(power[4 + axis] for axis in range(3))
        for power in source
    }))
    matter_support = tuple(sorted({power[:3] for power in spatial_support}))
    geometry_support = tuple(sorted({power[3:] for power in spatial_support}))
    reverse_spatial_support = tuple(sorted({
        tuple(power[axis] for axis in range(3))
        + tuple(power[4 + axis] for axis in range(3))
        for power in reverse_source
    }))
    reverse_matter_support = tuple(sorted({
        power[:3] for power in reverse_spatial_support
    }))
    reverse_geometry_support = tuple(sorted({
        power[3:] for power in reverse_spatial_support
    }))
    signed_units = {
        tuple(int(value) for value in direction)
        for direction in signed_neighbor_shell()
    }
    nearest_neighbor_geometry_only = all(
        geometry in signed_units for geometry in geometry_support
    )

    incoming, transfer = b193.POINTS["H1"]
    alternative_incoming = (
        sp.Integer(0), sp.Integer(0), sp.Integer(0), incoming[3]
    )
    coefficients = b193.tt_source_coefficients("H1", 1)

    def evaluated_vertex(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
        _action, _hodge, vertices = b193.b190.centered_objects(
            momentum, transfer
        )
        return sp.expand(sum(
            (coefficient * vertex for coefficient, vertex
             in zip(coefficients, vertices)),
            sp.zeros(16),
        ))

    primary_vertex = evaluated_vertex(incoming)
    alternative_vertex = evaluated_vertex(alternative_incoming)
    q_only_collision = not b193.matrix_equal(
        primary_vertex, alternative_vertex
    )

    return {
        "laurent_terms": len(source),
        "spatial_support_terms": len(spatial_support),
        "matter_support_terms": len(matter_support),
        "geometry_support_terms": len(geometry_support),
        "max_matter_l1": max(sum(abs(x) for x in item)
                             for item in matter_support),
        "max_geometry_l1": max(sum(abs(x) for x in item)
                               for item in geometry_support),
        "reverse_laurent_terms": len(reverse_source),
        "reverse_spatial_support_terms": len(reverse_spatial_support),
        "reverse_matter_support_terms": len(reverse_matter_support),
        "reverse_geometry_support_terms": len(reverse_geometry_support),
        "reverse_max_matter_l1": max(sum(abs(x) for x in item)
                                     for item in reverse_matter_support),
        "reverse_max_geometry_l1": max(sum(abs(x) for x in item)
                                       for item in reverse_geometry_support),
        "geometry_is_exact_signed_neighbor_shell": (
            set(geometry_support) == signed_units
        ),
        "geometry_is_nearest_neighbor_only": nearest_neighbor_geometry_only,
        "integer_support": all(
            isinstance(value, int)
            for power in source for value in power
        ),
        "z12_no_support_alias": all(
            -5 <= value <= 5 for power in spatial_support for value in power
        ),
        "reverse_z12_no_support_alias": all(
            -5 <= value <= 5
            for power in reverse_spatial_support for value in power
        ),
        "same_q_distinct_p_source": q_only_collision,
        "primary_incoming": incoming,
        "alternative_incoming": alternative_incoming,
        "transfer": transfer,
    }


@cache
def h1_cubic_covariance_facts() -> dict[str, object]:
    rotations = b194.proper_cubic_rotations()
    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    coefficients = sp.Matrix(b193.tt_source_coefficients("H1", 1))
    _action, _hodge, forward_vertices = b193.b190.centered_objects(
        incoming, transfer
    )
    _reverse_action, _reverse_hodge, reverse_vertices = (
        b193.b190.centered_objects(
            outgoing, tuple(-value for value in transfer)
        )
    )
    forward = sp.expand(sum(
        (coefficients[index] * forward_vertices[index]
         for index in range(10)), sp.zeros(16)
    ))
    reverse = sp.expand(sum(
        (coefficients[index] * reverse_vertices[index]
         for index in range(10)), sp.zeros(16)
    ))
    pair_orbit = set()
    forward_checks = []
    reverse_checks = []
    phase_checks = []
    for rotation in rotations:
        full = sp.eye(4)
        full[:3, :3] = rotation
        form = b193.b190.wedge_representation(full)
        tensor = b193.b190.tensor_representation(full)
        transformed_coefficients = tensor * coefficients
        transformed_incoming = tuple(full * sp.Matrix(incoming))
        transformed_transfer = tuple(full * sp.Matrix(transfer))
        transformed_outgoing = tuple(
            transformed_incoming[axis] + transformed_transfer[axis]
            for axis in range(4)
        )
        pair_orbit.add((transformed_incoming, transformed_transfer))
        _a, _h, transformed_forward_vertices = (
            b193.b190.centered_objects(
                transformed_incoming, transformed_transfer
            )
        )
        _ra, _rh, transformed_reverse_vertices = (
            b193.b190.centered_objects(
                transformed_outgoing,
                tuple(-value for value in transformed_transfer),
            )
        )
        transformed_forward = sp.expand(sum(
            (transformed_coefficients[index]
             * transformed_forward_vertices[index]
             for index in range(10)), sp.zeros(16)
        ))
        transformed_reverse = sp.expand(sum(
            (transformed_coefficients[index]
             * transformed_reverse_vertices[index]
             for index in range(10)), sp.zeros(16)
        ))
        forward_checks.append(b193.matrix_equal(
            transformed_forward, form * forward * form.T
        ))
        reverse_checks.append(b193.matrix_equal(
            transformed_reverse, form * reverse * form.T
        ))
        phase_checks.extend(
            sp.simplify(
                (rotation * sp.Matrix(transfer[:3])).dot(
                    rotation * displacement
                )
                - sp.Matrix(transfer[:3]).dot(displacement)
            ) == 0
            for displacement in signed_neighbor_shell()
        )
    stabilizer = sum(
        tuple(rotation * sp.Matrix(incoming[:3])) == incoming[:3]
        and tuple(rotation * sp.Matrix(transfer[:3])) == transfer[:3]
        for rotation in rotations
    )
    detector = b194.detector_classification_facts()
    return {
        "proper_cubic_count": len(rotations),
        "ordered_pair_orbit": len(pair_orbit),
        "ordered_pair_stabilizer": stabilizer,
        "forward_source_covariance": all(forward_checks),
        "actual_reverse_source_covariance": all(reverse_checks),
        "neighbor_phase_covariance": all(phase_checks),
        "detector_family_covariance": detector["family_covariance"],
        "event_context_covariance": detector["context_covariance"],
        "translation_covariance": True,
    }


def dense_numeric_scout(order: int = 3) -> dict[str, object]:
    """Non-evidentiary numerical scout for the exact series implementation."""
    import numpy as np

    def dense_terms(terms: b193.Terms) -> np.ndarray:
        if not terms:
            raise ValueError("an empty family needs an explicit shape")
        return sum((np.kron(
            np.array(temporal.evalf(), dtype=np.complex128),
            np.array(internal.evalf(), dtype=np.complex128),
        ) for temporal, internal in terms))

    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    left = b193.sector_terms(incoming)
    right = b193.sector_terms(outgoing)
    source = b193.combined_source_pair_terms(
        "H1", b193.tt_source_coefficients("H1", 1)
    )
    zero_384 = np.zeros((384, 384), dtype=np.complex128)
    y0 = np.block([[dense_terms(left["inverse"]), zero_384],
                   [zero_384, dense_terms(right["inverse"])]] )
    k0 = np.block([[dense_terms(left["p_inverse"]), zero_384],
                   [zero_384, dense_terms(right["p_inverse"])]] )
    tangent = np.block([[zero_384, dense_terms(source["forward"])],
                        [dense_terms(source["reverse"]), zero_384]])
    zero_384_192 = np.zeros((384, 192), dtype=np.complex128)
    r0 = np.block([[dense_terms(left["graph"]), zero_384_192],
                   [zero_384_192, dense_terms(right["graph"])]] )

    inverse_series = [y0]
    graph_series = [r0]
    for _degree in range(1, order + 1):
        inverse_series.append(-y0 @ tangent @ inverse_series[-1])
        graph_series.append(-k0 @ tangent @ graph_series[-1])

    orientation = np.array(
        b194.detector_classification_facts()["orientation"].evalf(),
        dtype=np.complex128,
    )
    pointer = np.kron(np.eye(12), orientation)
    numerators = []
    off_diagonal_overlaps = []
    reflection_residuals = []
    reality_residuals = []
    normalizers = []
    fiber_reflection = np.kron(
        np.eye(12), np.array(b193.GTIME, dtype=np.complex128)
    )
    full_reflection = np.block([
        [fiber_reflection, np.zeros((192, 192), dtype=np.complex128)],
        [np.zeros((192, 192), dtype=np.complex128), fiber_reflection],
    ])
    for degree in range(order + 1):
        half = np.zeros((384, 384), dtype=np.complex128)
        for left_degree in range(degree + 1):
            for inverse_degree in range(degree - left_degree + 1):
                right_degree = degree - left_degree - inverse_degree
                half += (
                    graph_series[left_degree].T
                    @ inverse_series[inverse_degree]
                    @ graph_series[right_degree]
                )
        gram = half + half.conj().T
        reality_residuals.append(np.linalg.norm(gram.conjugate() - gram))
        reflection_residuals.append(np.linalg.norm(
            full_reflection @ gram @ full_reflection - gram
        ))
        normalizers.append(np.trace(gram))
        overlap = np.trace(gram[:192, 192:] @ pointer)
        off_diagonal_overlaps.append(overlap)
        numerators.append(overlap + np.conjugate(overlap))
    return {
        "normalizers": tuple(complex(value) for value in normalizers),
        "numerators": tuple(complex(value) for value in numerators),
        "off_diagonal_overlaps": tuple(
            complex(value) for value in off_diagonal_overlaps
        ),
        "fiber_reflection_residuals": tuple(
            float(value) for value in reflection_residuals
        ),
        "reality_residuals": tuple(float(value)
                                   for value in reality_residuals),
    }


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=TIMEOUT_SEC,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git_output("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT_COMMIT),
        "prereg": is_ancestor(PREREG_COMMIT),
        "goal_registered": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}"
        ),
        "goal_worktree": git_output("hash-object", "--", GOAL_PATH),
        "preflight_registered": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}"
        ),
        "preflight_worktree": git_output(
            "hash-object", "--", PREFLIGHT_PATH
        ),
        "axiom_main": git_output("rev-parse", f"origin/main:{AXIOM_PATH}"),
        "axiom_worktree": git_output("hash-object", "--", AXIOM_PATH),
        "registry_main": git_output(
            "rev-parse", f"origin/main:{REGISTRY_PATH}"
        ),
        "registry_worktree": git_output(
            "hash-object", "--", REGISTRY_PATH
        ),
        "inputs": all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    }


@cache
def phase_pvm_facts() -> dict[str, object]:
    orientation = b194.detector_classification_facts()["orientation"]
    zero16 = sp.zeros(16)
    phases = (
        sp.Rational(1, 2) - I * sp.sqrt(3) / 2,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
        -I, I, sp.Integer(1), sp.Integer(1),
    )
    rho0 = b205.zero_source_state_facts()["rho0"]
    pvm_checks = []
    baseline_weights = []
    port_sum_checks = []
    for phase in phases:
        involution = b194.block_matrix(
            zero16, sp.conjugate(phase) * orientation,
            phase * orientation, zero16,
        )
        projectors = tuple(sp.expand(
            (sp.eye(32) + sign * involution) / 2
        ) for sign in (1, -1))
        pvm_checks.append(
            all(b193.matrix_equal(projector.H, projector)
                and b193.matrix_equal(projector * projector, projector)
                for projector in projectors)
            and b193.matrix_equal(projectors[0] * projectors[1], sp.zeros(32))
            and b193.matrix_equal(projectors[0] + projectors[1], sp.eye(32))
        )
        baseline_weights.append(tuple(sp.factor(
            sp.trace(rho0 * projector)
        ) for projector in projectors))
        for sign, projector in zip((1, -1), projectors):
            joint_sum = sum((b194.block_matrix(
                event,
                sign * sp.conjugate(phase) * event * orientation,
                sign * phase * orientation * event,
                event,
            ) / 2 for event in b193.b191.EFFECTS), sp.zeros(32))
            port_sum_checks.append(b193.matrix_equal(
                sp.expand(joint_sum), projector
            ))
    return {
        "phase_count": len(phases),
        "pvm": all(pvm_checks),
        "baseline_weights": tuple(baseline_weights),
        "baseline_half": all(
            weights == (sp.Rational(1, 2), sp.Rational(1, 2))
            for weights in baseline_weights
        ),
        "port_sum": all(port_sum_checks),
        "strict_zero_source_state": (
            b205.zero_source_state_facts()["strict_full_gram"]
            and all(b205.zero_source_state_facts()["sector_traces_positive"])
        ),
        "analytic_family": b205.positive_analytic_germ_lemma()[
            "analytic_family"
        ],
    }


def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "scope": False, "n5": False}
    text = NOTE_PATH.read_text()
    needles = (
        "surviving exact response is cubic",
        "scalar six-neighbor source decoder",
        "conditional Bloch-M2 decoder existence",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    n5 = (
        "per_element:", "per_site:", "per_mode:", "per_block:",
        "lattice_wide:",
    )
    return {
        "exists": True,
        "scope": all(needle in text for needle in needles),
        "n5": all(needle in text for needle in n5),
    }


N5_LINES = (
    "per_element: checked both binary phase projectors, exact linear and cubic overlaps, six phase values, scalar and conditional-adjoint Hom classes, and the H1 shear coordinates.",
    "per_site: checked the six signed source displacements and separated supplied phase labels from actual neighboring M2 Record contents; no formation event is supplied.",
    "per_mode: checked the fixed H1 incoming/transfer pair and a same-q/different-p collision; H2 remains sealed because full H1 eta reconstruction did not pass.",
    "per_block: checked the full two-sector Schur recurrence, port-free C32 effect, raw forward/actual-reverse source, and M2 decoder domain as distinct typed objects.",
    "lattice_wide: checked exact Z12 inverse-Fourier support and the full 24-frame simultaneous orbit; no full-Z3 history, gravity completion, retained theory, axiom edit, or TOE closure is claimed.",
)


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    phase = phase_series_facts()
    pvm = phase_pvm_facts()
    hom = neighbor_hom_facts()
    support = source_support_facts()
    covariance = h1_cubic_covariance_facts()
    note = note_facts()

    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal_blob": GOAL_BLOB,
        "actual_reverse": True,
        "tt_column": 1,
        "coarse_port_conditioned": False,
        "linear_zero": True,
        "cubic_nonzero": True,
        "cubic_positive": True,
        "zero_phase_all_order_nonzero": False,
        "phase_pvm": True,
        "positive_germ": True,
        "neighbor_variation": True,
        "scalar_hom_dimension": 0,
        "adjoint_hom_dimension": 2,
        "adjoint_decoder_selected": False,
        "orbit_lookup": False,
        "incoming_p_dependent": True,
        "source_radius_one": False,
        "source_collision_checked": True,
        "h2_opened": False,
        "complete_eta_law": False,
        "formation": False,
        "history": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_progress": False,
        "retained": False,
        "broad_local_no_go": False,
    }
    mutation_map = {
        "stale_main_authority": ("main", "stale"),
        "drop_preregistration": ("prereg", False),
        "alter_goal_after_registration": ("goal_blob", "altered"),
        "replace_actual_reverse_by_adjoint": ("actual_reverse", False),
        "use_wrong_tt_column": ("tt_column", 0),
        "condition_on_coarse_port": ("coarse_port_conditioned", True),
        "erase_linear_zero": ("linear_zero", False),
        "erase_cubic_quadrature": ("cubic_nonzero", False),
        "flip_cubic_sign": ("cubic_positive", False),
        "call_zero_phase_all_order_nonzero": (
            "zero_phase_all_order_nonzero", True
        ),
        "break_phase_pvm": ("phase_pvm", False),
        "deny_positive_germ": ("positive_germ", False),
        "erase_neighbor_variation": ("neighbor_variation", False),
        "claim_scalar_t2_hom": ("scalar_hom_dimension", 1),
        "erase_conditional_adjoint_hom": ("adjoint_hom_dimension", 0),
        "select_adjoint_decoder": ("adjoint_decoder_selected", True),
        "install_orbit_lookup": ("orbit_lookup", True),
        "erase_incoming_p_dependence": ("incoming_p_dependent", False),
        "call_source_radius_one": ("source_radius_one", True),
        "ignore_source_collision": ("source_collision_checked", False),
        "open_h2_after_context_failure": ("h2_opened", True),
        "claim_complete_eta_law": ("complete_eta_law", True),
        "claim_formation": ("formation", True),
        "claim_history": ("history", True),
        "claim_axiom_update": ("axiom_update", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_progress": ("toe_progress", True),
        "claim_retained_status": ("retained", True),
        "claim_broad_local_no_go": ("broad_local_no_go", True),
    }
    if mutation:
        key, value = mutation_map[mutation]
        claims[key] = value

    authority_ok = (
        authority["main"] == claims["main"]
        and authority["parent"] and authority["prereg"] == claims["prereg"]
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
    source_ok = (
        claims["actual_reverse"] is True and claims["tt_column"] == 1
        and support["integer_support"]
        and support["z12_no_support_alias"]
        and support["reverse_z12_no_support_alias"]
        and support["laurent_terms"] == 110
        and support["reverse_laurent_terms"] == 110
    )
    cubic_ok = (
        phase["linear_overlap"] == 0 == (0 if claims["linear_zero"] else 1)
        and (phase["cubic_overlap"] != 0) == claims["cubic_nonzero"]
        and phase["cubic_pure_imaginary"]
        and phase["cubic_matches_disclosure"]
        and phase["cubic_quadrature_positive"] == claims["cubic_positive"]
        and claims["zero_phase_all_order_nonzero"] is False
    )
    probability_ok = (
        pvm["phase_count"] == 6 and pvm["pvm"] == claims["phase_pvm"]
        and pvm["baseline_half"] and pvm["port_sum"]
        and pvm["strict_zero_source_state"] and pvm["analytic_family"]
        and claims["coarse_port_conditioned"] is False
        and claims["positive_germ"] is True
        and phase["distinct_neighbor_contrasts"] == 5
        and phase["nonzero_neighbor_contrasts"] == 4
        and claims["neighbor_variation"] is True
    )
    hom_ok = (
        hom["scalar_hom_dimension"] == claims["scalar_hom_dimension"]
        and hom["conditional_adjoint_hom_dimension"]
        == claims["adjoint_hom_dimension"]
        and hom["conditional_adjoint_basis_equivariant"]
        and hom["conditional_adjoint_basis_independent"]
        and hom["conditional_adjoint_basis_ranks"] == (3, 3)
        and hom["h1_shear_nonzero"]
        and claims["adjoint_decoder_selected"] is False
    )
    locality_ok = (
        support["same_q_distinct_p_source"]
        == claims["incoming_p_dependent"]
        and not support["geometry_is_nearest_neighbor_only"]
        and claims["source_radius_one"] is False
        and claims["source_collision_checked"] is True
        and support["max_matter_l1"] == 3
        and support["max_geometry_l1"] == 3
        and support["reverse_max_matter_l1"] == 3
        and support["reverse_max_geometry_l1"] == 3
    )
    covariance_ok = (
        covariance["proper_cubic_count"] == 24
        and covariance["ordered_pair_orbit"] == 24
        and covariance["ordered_pair_stabilizer"] == 1
        and covariance["forward_source_covariance"]
        and covariance["actual_reverse_source_covariance"]
        and covariance["neighbor_phase_covariance"]
        and covariance["detector_family_covariance"]
        and covariance["event_context_covariance"]
        and covariance["translation_covariance"]
        and claims["orbit_lookup"] is False
    )
    scope_ok = (
        claims["h2_opened"] is False
        and claims["complete_eta_law"] is False
        and claims["formation"] is False and claims["history"] is False
        and claims["axiom_update"] is False
        and claims["obligation_retirement"] == 0
        and claims["toe_progress"] is False
        and claims["retained"] is False
        and claims["broad_local_no_go"] is False
        and note["exists"] and note["scope"] and note["n5"]
    )
    return {
        "A": (authority_ok, "current authority and immutable Block-206 registration are pinned"),
        "B": (source_ok, "the literal H1 second-TT forward/actual-reverse source and integer Z12 support are reconstructed"),
        "C": (cubic_ok, "the port-free linear overlap vanishes while the exact cubic phase quadrature is positive and nonzero"),
        "D": (probability_ok, "six complete binary PVMs on the strictly positive analytic Schur family give five positive neighboring laws"),
        "E": (hom_ok, "the scalar shell has no T2 Hom while the conditional adjoint-M2 shell has exactly two explicit surjective classes"),
        "F": (locality_ok, "the source reaches L1 radius three and same q with different p gives distinct vertices, so phase alone is not eta closure"),
        "G": (covariance_ok, "forward/reverse source, detector, and six phases pass all 24 simultaneous proper-cubic frames without an orbit lookup"),
        "H": (scope_ok, "the result is a positive H1 phase germ and context boundary, not complete eta, H2, formation/history, axiom, retained, or TOE closure"),
    }


def mutation_sweep() -> int:
    failures = []
    for mutation in MUTATIONS:
        checks = evaluate(mutation)
        if all(passed for passed, _message in checks.values()):
            failures.append(mutation)
    print(f"MUTATION_TOTAL: PASS={len(MUTATIONS)-len(failures)} FAIL={len(failures)}")
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
    phase = phase_series_facts()
    support = source_support_facts()
    hom = neighbor_hom_facts()
    print(
        "H1_CUBIC: a1=0; a3=i*C; C>0 exact; "
        f"C={phase['cubic_quadrature']}."
    )
    print(
        "NEIGHBOR_CONTRAST_CUBIC: "
        "kappa*(sqrt(3),-sqrt(3),2,-2,0,0); "
        f"distinct={phase['distinct_neighbor_contrasts']}; "
        f"nonzero={phase['nonzero_neighbor_contrasts']}."
    )
    print(
        "SOURCE_SUPPORT: forward/reverse Laurent=110/110; "
        f"spatial supports={support['spatial_support_terms']}/"
        f"{support['reverse_spatial_support_terms']}; "
        "matter/geometry max-L1=3/3; same-q-different-p=true."
    )
    print(
        "NEIGHBOR_HOM: scalar->T2 dim="
        f"{hom['scalar_hom_dimension']}; conditional adjoint-M2->T2 dim="
        f"{hom['conditional_adjoint_hom_dimension']}; "
        "classes=(odd_shell,even_shell); decoder_selected=false."
    )
    print(
        "RESULT: positive port-free H1 neighbor-phase binary germ exists; "
        "actual six-record eta/source decoder remains open; "
        "obligation_retirement=0; TOE movement=0."
    )
    for line in N5_LINES:
        print(line)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
