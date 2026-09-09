#!/usr/bin/env python3
"""Block 192: full temporal carrier and source/history/write seam.

This runner executes the preregistered periodic-L24 carrier, the minimal
four-mode compression control, the frozen Block-191 grade-three source, and
the first source tangent of the recomputed reflected Schur history.  It keeps
carrier existence, history positivity, source susceptibility, and Record
typing as separate gates.
"""

from __future__ import annotations

import argparse
from functools import cache
from math import lcm
from pathlib import Path
import subprocess
import sys

import sympy as sp
from sympy.polys.matrices import DomainMatrix


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24 as b190  # noqa: E402
import admissibility_d4_grade3_source_instrument_history_write_2026_08_24 as b191  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md"
)
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "480f633a5fbe34f444ec57e079abdd81b42e7728"
PREREG_COMMIT = "d1f55e02b1e8750165682156dbbc3b021ec3bb00"
CURRENT_MAIN = "b11811704efa98a12272d572f666e530a807f6c1"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
CURRENT_REGISTRY_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
WORKTREE_REGISTRY_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 240

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_GRADE3_SOURCE_INSTRUMENT_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.py",
    "logs/runner-cache/admissibility_d4_grade3_source_instrument_history_write_2026_08_24.txt",
    "docs/ADMISSIBILITY_D4_DIRAC_KAHLER_COMMON_ACTION_WARD_TT_RECORD_MARK_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-24.md",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
    "logs/runner-cache/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.txt",
)

I = sp.I
R = sp.Rational
MASS = R(2, 7)
L_TIME = 24
HALF_TIME = 12
IDENTITY16 = sp.eye(16)
GSPACE = tuple(
    b190.CREATION[axis] + b190.ANNIHILATION[axis]
    for axis in range(3)
)
GTIME = b190.CREATION[3] + b190.ANNIHILATION[3]

X1 = (
    "X1",
    (sp.pi / 6, sp.pi / 4, 0, sp.pi / 6),
    (sp.pi / 3, sp.pi / 6, sp.pi / 2, sp.pi / 12),
)
POINTS = b191.POINTS + (X1,)

MUTATIONS = (
    "stale_main_authority",
    "break_periodic_minimality",
    "break_mode_intertwiner",
    "break_temporal_modulation",
    "claim_four_mode_x1_closure",
    "break_reflection_positive_history",
    "break_uniform_internal_marginal",
    "break_x1_source_rank",
    "break_conditioned_ward",
    "erase_h1_tangent_support_wall",
    "erase_d1_normalization_contradiction",
    "break_conditioned_gram_write",
    "claim_permanent_record",
    "claim_toe_progress",
)
MUTATION_FAMILY = {
    "stale_main_authority": "A",
    "break_periodic_minimality": "B",
    "break_mode_intertwiner": "B",
    "break_temporal_modulation": "B",
    "claim_four_mode_x1_closure": "C",
    "break_reflection_positive_history": "D",
    "break_uniform_internal_marginal": "D",
    "break_x1_source_rank": "E",
    "break_conditioned_ward": "E",
    "erase_h1_tangent_support_wall": "E",
    "erase_d1_normalization_contradiction": "E",
    "break_conditioned_gram_write": "F",
    "claim_permanent_record": "F",
    "claim_toe_progress": "G",
}


def matrix_equal(left: sp.Matrix, right: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def nonzero_entries(matrix: sp.Matrix) -> int:
    return sum(sp.simplify(value) != 0 for value in matrix)


def exact_field_inverse(matrix: sp.Matrix) -> sp.Matrix:
    """Invert over the exact rational/algebraic field, never EX."""
    return DomainMatrix.from_Matrix(
        matrix, extension=True
    ).to_field().inv().to_Matrix()


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
        "worktree_registry": git_output(
            "hash-object", "--", REGISTRY_PATH
        ),
    }


def temporal_matrices(length: int = L_TIME) -> tuple[sp.Matrix, ...]:
    shift = sp.zeros(length)
    for time in range(length):
        shift[(time + 1) % length, time] = 1
    differential = sp.expand((shift - shift.T) / 2)
    cosine = sp.expand((shift + shift.T) / 2)
    reflection = sp.zeros(length)
    for time in range(length):
        reflection[length - 1 - time, time] = -1
    return shift, differential, cosine, reflection


def root(momentum: sp.Expr) -> sp.Expr:
    return sp.expand_complex(sp.exp(-I * momentum))


def mode(momentum: sp.Expr) -> sp.Matrix:
    value = root(momentum)
    return sp.Matrix(tuple(value**time / sp.sqrt(L_TIME)
                           for time in range(L_TIME)))


def spatial_action(momentum: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.expand(
        MASS * IDENTITY16
        + I * sum(
            (sp.sin(momentum[axis]) * GSPACE[axis] for axis in range(3)),
            sp.zeros(16),
        )
    )


def full_mode_intertwiner(
    differential: sp.Matrix, momentum: tuple[sp.Expr, ...]
) -> bool:
    vector = mode(momentum[3])
    base = spatial_action(momentum)
    fiber = sp.expand(base + I * sp.sin(momentum[3]) * GTIME)
    block190_differential = b190.centered_differential(momentum)
    block190_action = sp.expand(
        MASS * IDENTITY16
        + I * (block190_differential + block190_differential.T)
    )
    return (
        matrix_equal(
            differential * vector,
            I * sp.sin(momentum[3]) * vector,
        )
        and matrix_equal(fiber, block190_action)
    )


@cache
def periodic_carrier_facts() -> dict[str, object]:
    shift, differential, cosine, reflection = temporal_matrices()
    endpoint_momenta = []
    for _name, incoming, transfer in POINTS:
        outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
        endpoint_momenta.extend((incoming, outgoing))

    temporal_values = (sp.pi / 6, sp.pi / 4)
    mode_checks = []
    reflection_checks = []
    for momentum in temporal_values:
        vector = mode(momentum)
        phase = -root(momentum) ** (L_TIME - 1)
        mode_checks.append((
            sp.simplify((vector.H * vector)[0]) == 1,
            matrix_equal(
                differential * vector, I * sp.sin(momentum) * vector
            ),
            matrix_equal(cosine * vector, sp.cos(momentum) * vector),
        ))
        reflection_checks.append(matrix_equal(
            reflection * vector, phase * sp.conjugate(vector)
        ))

    q_time = sp.pi / 12
    modulation = sp.diag(*(
        root(q_time) ** time for time in range(L_TIME)
    ))
    incoming_mode = mode(sp.pi / 6)
    outgoing_mode = mode(sp.pi / 4)
    link_vertex = sp.expand(
        sp.exp(I * q_time / 2)
        * (modulation * shift + shift.T * modulation) / 2
    )
    link_amplitude = sp.cos(sp.pi / 6 + q_time / 2)

    x1_action, _x1_hodge, x1_vertices = b190.centered_objects(
        X1[1], X1[2]
    )
    modulation_exact = matrix_equal(
        modulation * incoming_mode, outgoing_mode
    )
    # Once M_q f_k=f_{k+q}, the full-16 identity
    # (M_q tensor V_A)(f_k tensor I)=f_{k+q} tensor V_A is a literal
    # Kronecker-product identity.  Retain every nonempty 16x16 vertex here.
    source_mode_residuals = tuple(
        modulation_exact and vertex.shape == (16, 16)
        for vertex in x1_vertices
    )

    spatial_clifford = tuple(
        matrix_equal(GTIME * generator, -generator * GTIME)
        for generator in GSPACE
    )
    full_reflection = (
        matrix_equal(
            reflection * differential * reflection.T, -differential
        )
        and matrix_equal(reflection * cosine * reflection.T, cosine)
        and matrix_equal(GTIME * GTIME, IDENTITY16)
        and all(spatial_clifford)
    )
    outcome_reflection = all(matrix_equal(
        GTIME * b191.EFFECTS[index] * GTIME,
        b191.EFFECTS[3 - index],
    ) for index in range(4))

    order_checks = tuple(
        sp.simplify(sp.exp(-I * sp.pi * power / 12) - 1) != 0
        for power in range(1, 24)
    )
    return {
        "periodic": matrix_equal(shift**L_TIME, sp.eye(L_TIME)),
        "local": nonzero_entries(shift) == L_TIME,
        "centered": matrix_equal(
            cosine**2 - differential**2, sp.eye(L_TIME)
        ),
        "minimal_length": lcm(8, 12) == L_TIME,
        "twist_forced_periodic": (
            L_TIME % 8 == 0 and L_TIME % 12 == 0
        ),
        "mode_checks": tuple(mode_checks),
        "reflection_checks": tuple(reflection_checks),
        "full_mode_intertwiners": tuple(
            full_mode_intertwiner(differential, momentum)
            for momentum in endpoint_momenta
        ),
        "weyl": matrix_equal(
            modulation * shift * modulation.H,
            root(q_time) * shift,
        ),
        "modulation": modulation_exact,
        "modulation_adjoint": matrix_equal(
            modulation.H,
            sp.diag(*(root(-q_time) ** time
                      for time in range(L_TIME))),
        ),
        "link_vertex": all(
            sp.simplify(sp.expand_complex(value)) == 0
            for value in (
                link_vertex * incoming_mode
                - link_amplitude * outgoing_mode
            )
        ),
        "link_amplitude": sp.simplify(
            link_amplitude - sp.cos(5 * sp.pi / 24)
        ) == 0,
        "source_mode_residuals": source_mode_residuals,
        "full_reflection": full_reflection,
        "outcome_reflection": outcome_reflection,
        "weyl_order_24": all(order_checks)
        and sp.simplify(sp.exp(-2 * I * sp.pi) - 1) == 0,
        "x1_action_rank": x1_action.rank(),
    }


@cache
def compressed_carrier_facts() -> dict[str, object]:
    a = 2 ** (-sp.Rational(3, 4))
    b = (sp.sqrt(2) - 1) / 2
    differential = sp.Matrix((
        (0, -a, 0, 0),
        (a, 0, -b, 0),
        (0, b, 0, -a),
        (0, 0, a, 0),
    ))
    reflection = sp.zeros(4)
    for time in range(4):
        reflection[3 - time, time] = 1
    variable = sp.symbols("z")
    expected_characteristic = (
        variable**2 + R(1, 2)
    ) * (variable**2 + R(1, 4))

    mass, radius = sp.symbols("mass radius", positive=True, real=True)
    hamiltonian = sp.Matrix(((mass, -sp.sqrt(radius)),
                             (-sp.sqrt(radius), -mass)))
    scalar = mass**2 + radius
    delta = (a**2 + scalar) ** 2 + b**2 * scalar
    factor = sp.Matrix.vstack(hamiltonian, a * sp.eye(2))
    raw_gram = sp.expand(b * factor * factor.T / delta)
    weyl_phase = root(sp.pi / 12)
    minimum_weyl_dimension = next(
        dimension for dimension in range(1, 49)
        if sp.simplify(sp.expand_complex(weyl_phase**dimension - 1)) == 0
    )
    return {
        "skew": matrix_equal(differential.T, -differential),
        "reflection": matrix_equal(
            reflection * differential * reflection, -differential
        ),
        "characteristic": sp.simplify(
            differential.charpoly(variable).as_expr()
            - expected_characteristic
        ) == 0,
        "minimal_real_dimension": differential.rows == 4,
        "raw_positive_factor": matrix_equal(
            raw_gram,
            b * factor * factor.T / delta,
        ),
        "raw_rank": factor.rank(),
        "positive_coefficient": b.is_positive and delta.is_positive,
        "x1_weyl_closed": sp.simplify(
            sp.expand_complex(weyl_phase**differential.rows - 1)
        ) == 0,
        "minimum_weyl_dimension": minimum_weyl_dimension,
    }


@cache
def reduced_history_fixture() -> dict[str, object]:
    shift, differential, _cosine, time_reflection = temporal_matrices()
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.diag(1, -1)
    skew = sp.Matrix(((0, 1), (-1, 0)))
    phase = sp.diag(1, -I)
    original = sp.expand(
        sp.kronecker_product(
            sp.eye(L_TIME), MASS * sp.eye(2) + I * sigma_x
        )
        + sp.kronecker_product(differential, sigma_z)
    )
    full_phase = sp.kronecker_product(sp.eye(L_TIME), phase)
    real_action = sp.expand(full_phase.H * original * full_phase)
    expected_real = sp.expand(
        MASS * sp.eye(2 * L_TIME)
        + sp.kronecker_product(sp.eye(L_TIME), skew)
        + sp.kronecker_product(differential, sigma_z)
    )
    transformed_reflection = sp.kronecker_product(
        time_reflection, sigma_z
    )

    cut = L_TIME
    block_c = real_action[cut:, :cut]
    block_d = real_action[cut:, cut:]
    right_graph = sp.Matrix.vstack(
        sp.eye(cut), -block_d.inv(method="DM") * block_c
    )
    action_inverse = real_action.inv(method="DM")
    positive_gram = sp.expand(
        right_graph.T
        * (action_inverse + action_inverse.T)
        * right_graph
    )
    amplitude = action_inverse * right_graph
    factor_gram = sp.expand(2 * MASS * amplitude.T * amplitude)
    _lower, diagonal = positive_gram.LDLdecomposition(hermitian=True)
    pivots = tuple(sp.factor(diagonal[index, index])
                   for index in range(cut))

    # Recompute the honest complex reflected port and its local marginal.
    complex_c = original[cut:, :cut]
    complex_d = original[cut:, cut:]
    complex_graph = sp.Matrix.vstack(
        sp.eye(cut), -complex_d.inv(method="DM") * complex_c
    )
    complex_inverse = original.inv(method="DM")
    half_gram = sp.expand(
        complex_graph.T * complex_inverse * complex_graph
    )
    complex_gram = sp.expand(half_gram + half_gram.H)
    marginal = sum((
        complex_gram[2 * time:2 * time + 2,
                     2 * time:2 * time + 2]
        for time in range(HALF_TIME)
    ), sp.zeros(2))

    alternating = sp.diag(*((-1) ** time for time in range(L_TIME)))
    unit_symmetry = sp.kronecker_product(alternating, sigma_x)
    antiunitary_matrix = sp.kronecker_product(
        sp.eye(L_TIME), sigma_z
    )
    p_symbol = sp.symbols("p", real=True)
    symbolic_action = sp.expand(
        MASS * sp.eye(2 * L_TIME)
        + sp.kronecker_product(differential, sigma_z)
        + I * p_symbol * sp.kronecker_product(
            sp.eye(L_TIME), sigma_x
        )
    )
    scalar_a, scalar_d, scalar_b, scalar_c = sp.symbols(
        "scalar_a scalar_d scalar_b scalar_c", real=True
    )
    generic_hermitian = sp.Matrix((
        (scalar_a, scalar_b + I * scalar_c),
        (scalar_b - I * scalar_c, scalar_d),
    ))
    fixed_equations = tuple(
        sp.expand(value) for value in (
            list(sigma_x * generic_hermitian * sigma_x - generic_hermitian)
            + list(
                sigma_z * sp.conjugate(generic_hermitian) * sigma_z
                - generic_hermitian
            )
        )
    )
    fixed_solution = sp.solve(
        fixed_equations,
        (scalar_d, scalar_b, scalar_c),
        dict=True,
    )
    return {
        "phase_real": matrix_equal(real_action, expected_real),
        "real_skew": matrix_equal(
            real_action + real_action.T,
            2 * MASS * sp.eye(2 * L_TIME),
        ),
        "reflection_self_dual": matrix_equal(
            transformed_reflection * real_action.T
            * transformed_reflection.T,
            real_action,
        ),
        "right_graph_rank": right_graph.rank(),
        "positive_identity": matrix_equal(positive_gram, factor_gram),
        "positive_pivots": all(pivot.is_positive for pivot in pivots),
        "positive_rank": sum(pivot != 0 for pivot in pivots),
        "odd_port_negative": all(
            sp.simplify(-pivot).is_negative for pivot in pivots
        ),
        "marginal": matrix_equal(
            sp.simplify(marginal / sp.trace(complex_gram)),
            sp.eye(2) / 2,
        ),
        "unit_symmetry": matrix_equal(
            unit_symmetry.H * symbolic_action * unit_symmetry,
            symbolic_action,
        ),
        "antiunitary_symmetry": matrix_equal(
            antiunitary_matrix * sp.conjugate(symbolic_action)
            * antiunitary_matrix,
            symbolic_action,
        ),
        "scalar_fixed_algebra": fixed_solution == [{
            scalar_b: 0, scalar_c: 0, scalar_d: scalar_a
        }],
        "local_blocks_scalar": all(matrix_equal(
            complex_gram[2 * time:2 * time + 2,
                         2 * time:2 * time + 2],
            complex_gram[2 * time, 2 * time] * sp.eye(2),
        ) for time in range(HALF_TIME)),
    }


def pair_ldl_pivots(
    real_part: sp.Matrix, imaginary_part: sp.Matrix, radius: sp.Expr
) -> tuple[sp.Expr, ...]:
    """No-pivot Hermitian LDL over K[j]/(j**2+radius)."""
    size = real_part.rows
    combined = DomainMatrix.from_Matrix(
        real_part.row_join(imaginary_part),
        fmt="dense",
        extension=True,
    ).to_field()
    domain = combined.domain
    rows = combined.to_list()
    lower_real = [row[:size] for row in rows]
    lower_imag = [row[size:] for row in rows]
    radius_element = domain.convert(radius)
    pivots = []
    for column in range(size):
        if lower_imag[column][column] != domain.zero:
            return ()
        pivot = lower_real[column][column]
        pivots.append(pivot)
        for row in range(column + 1, size):
            left_real = lower_real[row][column]
            left_imag = lower_imag[row][column]
            for inner in range(column + 1, row + 1):
                right_real = lower_real[inner][column]
                right_imag = lower_imag[inner][column]
                product_real = (
                    left_real * right_real
                    + radius_element * left_imag * right_imag
                )
                product_imag = (
                    left_imag * right_real
                    - left_real * right_imag
                )
                lower_real[row][inner] -= product_real / pivot
                lower_imag[row][inner] -= product_imag / pivot
    return tuple(domain.to_sympy(pivot) for pivot in pivots)


@cache
def frozen_history_positivity_facts() -> dict[str, object]:
    """Exact ordinary-transpose OS positivity at every frozen radius."""
    _shift, differential, _cosine, _reflection = temporal_matrices()
    half = HALF_TIME
    embedding_n = sp.Matrix.vstack(sp.eye(half), sp.zeros(half))
    embedding_p = sp.Matrix.vstack(sp.zeros(half), sp.eye(half))
    full_n = sp.kronecker_product(embedding_n, sp.eye(2))
    full_p = sp.kronecker_product(embedding_p, sp.eye(2))
    differential_p = embedding_p.T * differential * embedding_p
    differential_pn = embedding_p.T * differential * embedding_n
    sigma_x = sp.Matrix(((0, 1), (1, 0)))
    sigma_z = sp.diag(1, -1)
    coupling = sp.kronecker_product(differential_pn, sigma_z)

    expected_radii = (
        R(0), R(3, 4), R(1), R(5, 4), R(3, 2), R(2), R(3),
        (7 + sp.sqrt(3)) / 4,
        (10 + sp.sqrt(3)) / 4,
    )
    endpoint_momenta = tuple(
        momentum for _name, incoming, transfer in POINTS
        for momentum in (
            incoming,
            tuple(incoming[axis] + transfer[axis] for axis in range(4)),
        )
    )
    endpoint_radii = tuple(sp.simplify(sum(
        sp.sin(momentum[axis]) ** 2 for axis in range(3)
    )) for momentum in endpoint_momenta)
    full_copy_checks = tuple(
        matrix_equal(GTIME**2, IDENTITY16)
        and sp.trace(GTIME) == 0
        and matrix_equal(
            spatial_action(momentum) - MASS * IDENTITY16,
            I * sum((
                sp.sin(momentum[axis]) * GSPACE[axis]
                for axis in range(3)
            ), sp.zeros(16)),
        )
        and matrix_equal(
            sum((
                sp.sin(momentum[axis]) * GSPACE[axis]
                for axis in range(3)
            ), sp.zeros(16)) ** 2,
            radius * IDENTITY16,
        )
        and sp.trace(sum((
            sp.sin(momentum[axis]) * GSPACE[axis]
            for axis in range(3)
        ), sp.zeros(16))) == 0
        and matrix_equal(
            GTIME * sum((
                sp.sin(momentum[axis]) * GSPACE[axis]
                for axis in range(3)
            ), sp.zeros(16))
            + sum((
                sp.sin(momentum[axis]) * GSPACE[axis]
                for axis in range(3)
            ), sp.zeros(16)) * GTIME,
            sp.zeros(16),
        )
        for momentum, radius in zip(endpoint_momenta, endpoint_radii)
    )
    radii_exact = (
        all(any(sp.simplify(value - expected) == 0
                for expected in expected_radii)
            for value in endpoint_radii)
        and all(any(sp.simplify(value - expected) == 0
                    for value in endpoint_radii)
                for expected in expected_radii)
    )

    pivot_sets = []
    for radius in expected_radii:
        temporal_inverse = exact_field_inverse(
            (MASS**2 + radius) * sp.eye(L_TIME) - differential**2
        )
        p_inverse = exact_field_inverse(
            (MASS**2 + radius) * sp.eye(half)
            - differential_p**2
        )
        full_temporal_inverse = sp.kronecker_product(
            temporal_inverse, sp.eye(2)
        )
        full_p_inverse = sp.kronecker_product(p_inverse, sp.eye(2))
        inverse_real = full_temporal_inverse * (
            MASS * sp.eye(2 * L_TIME)
            - sp.kronecker_product(differential, sigma_z)
        )
        inverse_imag = -full_temporal_inverse * sp.kronecker_product(
            sp.eye(L_TIME), sigma_x
        )
        p_inverse_real = full_p_inverse * (
            MASS * sp.eye(2 * half)
            - sp.kronecker_product(differential_p, sigma_z)
        )
        p_inverse_imag = -full_p_inverse * sp.kronecker_product(
            sp.eye(half), sigma_x
        )
        graph_real = full_n - full_p * p_inverse_real * coupling
        graph_imag = -full_p * p_inverse_imag * coupling
        amplitude_real = (
            inverse_real * graph_real
            - radius * inverse_imag * graph_imag
        )
        amplitude_imag = (
            inverse_real * graph_imag + inverse_imag * graph_real
        )
        h_real = (
            graph_real.T * amplitude_real
            - radius * graph_imag.T * amplitude_imag
        )
        h_imag = (
            graph_real.T * amplitude_imag
            + graph_imag.T * amplitude_real
        )
        gram_real = h_real + h_real.T
        gram_imag = h_imag - h_imag.T
        pivot_sets.append(pair_ldl_pivots(
            gram_real, gram_imag, radius
        ))

    inertias = tuple((
        sum(pivot.is_positive is True for pivot in pivots),
        sum(pivot.is_negative is True for pivot in pivots),
        sum(pivot == 0 for pivot in pivots),
    ) for pivots in pivot_sets)
    full_inertias = tuple(
        tuple(8 * entry for entry in inertia) for inertia in inertias
    )
    minimum_pivots = tuple(
        min(float(sp.N(pivot, 16)) for pivot in pivots)
        for pivots in pivot_sets if pivots
    )
    return {
        "radii_exact": radii_exact,
        "radii": expected_radii,
        "pivot_counts": tuple(len(pivots) for pivots in pivot_sets),
        "full_copy_checks": full_copy_checks,
        "all_positive": all(
            pivot.is_positive is True
            for pivots in pivot_sets for pivot in pivots
        ),
        "minimum_pivots": minimum_pivots,
        "reduced_inertias": inertias,
        "full_inertias": full_inertias,
    }


def tensor_multiply(
    left: tuple[tuple[sp.Matrix, sp.Matrix], ...],
    right: tuple[tuple[sp.Matrix, sp.Matrix], ...],
) -> tuple[tuple[sp.Matrix, sp.Matrix], ...]:
    return tuple(
        (left_time * right_time, left_internal * right_internal)
        for left_time, left_internal in left
        for right_time, right_internal in right
    )


def tensor_scale(
    terms: tuple[tuple[sp.Matrix, sp.Matrix], ...], scalar: sp.Expr
) -> tuple[tuple[sp.Matrix, sp.Matrix], ...]:
    return tuple((scalar * time, internal) for time, internal in terms)


def tensor_transpose(
    terms: tuple[tuple[sp.Matrix, sp.Matrix], ...]
) -> tuple[tuple[sp.Matrix, sp.Matrix], ...]:
    return tuple((time.T, internal.T) for time, internal in terms)


def tensor_trace(
    terms: tuple[tuple[sp.Matrix, sp.Matrix], ...],
    effect: sp.Matrix | None = None,
) -> sp.Expr:
    value = 0
    for temporal, internal in terms:
        internal_factor = internal if effect is None else effect * internal
        value += sp.trace(temporal) * sp.trace(internal_factor)
    return sp.cancel(value)


@cache
def h1_actual_os_tangent_facts() -> dict[str, object]:
    """Recompute the exact H1/(--)/A=8 actual reflected-Gram tangent."""
    shift, differential, _cosine, _reflection = temporal_matrices()
    del shift
    half = HALF_TIME
    embedding_n = sp.Matrix.vstack(sp.eye(half), sp.zeros(half))
    embedding_p = sp.Matrix.vstack(sp.zeros(half), sp.eye(half))
    differential_p = sp.expand(
        embedding_p.T * differential * embedding_p
    )
    differential_pn = sp.expand(
        embedding_p.T * differential * embedding_n
    )

    spatial = sp.expand(GSPACE[0] / 2 + sp.sqrt(3) * GSPACE[1] / 2)
    temporal_inverse = (
        (MASS**2 + 1) * sp.eye(L_TIME) - differential**2
    ).inv(method="DM")
    p_inverse = (
        (MASS**2 + 1) * sp.eye(half) - differential_p**2
    ).inv(method="DM")
    internal_inverse = sp.expand(MASS * IDENTITY16 - I * spatial)

    action_inverse = (
        (temporal_inverse, internal_inverse),
        (-temporal_inverse * differential, GTIME),
    )
    p_action_inverse = (
        (p_inverse, internal_inverse),
        (-p_inverse * differential_p, GTIME),
    )

    graph = (
        (embedding_n, IDENTITY16),
        (embedding_p * p_inverse * differential_p * differential_pn,
         IDENTITY16),
        (
            embedding_p * p_inverse * differential_pn,
            sp.expand(-MASS * GTIME + I * spatial * GTIME),
        ),
    )

    creation = b190.CREATION
    annihilation = b190.ANNIHILATION
    metric_slot = sp.expand(-(
        creation[0] * annihilation[2]
        + creation[2] * annihilation[0]
    ) / (2 * sp.sqrt(2)))
    differential_in = sp.expand(
        creation[0] / 2 + sp.sqrt(3) * creation[1] / 2
    )
    differential_out = sp.expand(
        creation[0] + creation[1] / 2
    )
    vertex_zero = sp.expand(
        MASS * metric_slot
        + I * (
            metric_slot * differential_in
            + differential_out.T * metric_slot
        )
    )
    vertex_sine = sp.expand(I * (
        metric_slot * creation[3]
        + annihilation[3] * metric_slot
    ))
    source = (
        (sp.eye(L_TIME), vertex_zero),
        (differential, -I * vertex_sine),
    )
    source_without_zero = ((differential, -I * vertex_sine),)

    # The closed graph derivative is -E_P d^{-1} E_P^T dotA V.
    embedded_p_inverse = tuple(
        (embedding_p * temporal * embedding_p.T, internal)
        for temporal, internal in p_action_inverse
    )

    def response_for(
        source_terms: tuple[tuple[sp.Matrix, sp.Matrix], ...]
    ) -> tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr, int]:
        graph_derivative = tensor_scale(
            tensor_multiply(
                tensor_multiply(embedded_p_inverse, source_terms), graph
            ),
            -1,
        )
        inverse_derivative = tensor_scale(
            tensor_multiply(
                tensor_multiply(action_inverse, source_terms),
                action_inverse,
            ),
            -1,
        )
        dot_h = (
            tensor_multiply(
                tensor_multiply(tensor_transpose(graph_derivative),
                                action_inverse),
                graph,
            )
            + tensor_multiply(
                tensor_multiply(tensor_transpose(graph),
                                inverse_derivative),
                graph,
            )
            + tensor_multiply(
                tensor_multiply(tensor_transpose(graph), action_inverse),
                graph_derivative,
            )
        )
        h = tensor_multiply(
            tensor_multiply(tensor_transpose(graph), action_inverse), graph
        )
        effect = b191.EFFECTS[0]
        trace_h = tensor_trace(h)
        trace_h_effect = tensor_trace(h, effect)
        trace_dot_h = tensor_trace(dot_h)
        trace_dot_h_effect = tensor_trace(dot_h, effect)
        z_value = sp.cancel(trace_h + sp.conjugate(trace_h))
        z_effect = sp.cancel(
            trace_h_effect + sp.conjugate(trace_h_effect)
        )
        dot_z = sp.cancel(trace_dot_h + sp.conjugate(trace_dot_h))
        dot_z_effect = sp.cancel(
            trace_dot_h_effect + sp.conjugate(trace_dot_h_effect)
        )
        response = sp.cancel(
            dot_z_effect / z_effect - dot_z / z_value
        )
        return z_value, z_effect, dot_z, response, len(dot_h)

    z_value, z_effect, dot_z, response, term_count = response_for(source)
    _z0, _ze0, _dz0, without_zero, _count0 = response_for(
        source_without_zero
    )
    expected_z = (
        sp.Integer(3771838801812706831317695172263571939076232352)
        / sp.Integer(55184829647280561987785927697838347401837285)
    )
    expected_response = -(
        sp.Integer(60152486349300630788094853463157702307183068975741688011109)
        * sp.sqrt(6)
        / sp.Integer(1367578267202679321096642792688675885888759047856166126012160)
    )
    _action, _hodge, vertices = b190.centered_objects(
        POINTS[3][1], POINTS[3][2]
    )
    return {
        "vertex_symbol": matrix_equal(
            vertex_zero + sp.sin(sp.pi / 6) * vertex_sine,
            vertices[8],
        ),
        "z": z_value,
        "z_expected": sp.simplify(z_value - expected_z) == 0,
        "uniform_weight": sp.simplify(z_effect / z_value - R(1, 4)) == 0,
        "dot_z_zero": sp.simplify(dot_z) == 0,
        "response": response,
        "response_expected": sp.simplify(
            response - expected_response
        ) == 0,
        "response_nonzero": response != 0 and expected_response.is_negative,
        "without_vertex_zero": sp.simplify(without_zero) == 0,
        "term_count": term_count,
    }


@cache
def d1_holomorphic_normalization_facts() -> dict[str, object]:
    """Test the most generous two-quadrature ordinary-OS normalization."""
    _shift, differential, _cosine, _reflection = temporal_matrices()
    half = HALF_TIME
    embedding_n = sp.Matrix.vstack(sp.eye(half), sp.zeros(half))
    embedding_p = sp.Matrix.vstack(sp.zeros(half), sp.eye(half))
    differential_p = sp.expand(
        embedding_p.T * differential * embedding_p
    )
    differential_pn = sp.expand(
        embedding_p.T * differential * embedding_n
    )
    temporal_inverse = (
        MASS**2 * sp.eye(L_TIME) - differential**2
    ).inv(method="DM")
    p_inverse = (
        MASS**2 * sp.eye(half) - differential_p**2
    ).inv(method="DM")
    action_inverse = (
        (MASS * temporal_inverse, IDENTITY16),
        (-temporal_inverse * differential, GTIME),
    )
    p_action_inverse = (
        (MASS * p_inverse, IDENTITY16),
        (-p_inverse * differential_p, GTIME),
    )
    graph = (
        (embedding_n, IDENTITY16),
        (
            embedding_p * p_inverse * differential_p * differential_pn,
            IDENTITY16,
        ),
        (
            -MASS * embedding_p * p_inverse * differential_pn,
            GTIME,
        ),
    )
    embedded_p_inverse = tuple(
        (embedding_p * temporal * embedding_p.T, internal)
        for temporal, internal in p_action_inverse
    )
    h_terms = tensor_multiply(
        tensor_multiply(tensor_transpose(graph), action_inverse), graph
    )
    effect = b191.EFFECTS[0]
    z_value = sp.cancel(
        tensor_trace(h_terms) + sp.conjugate(tensor_trace(h_terms))
    )
    z_effect = sp.cancel(
        tensor_trace(h_terms, effect)
        + sp.conjugate(tensor_trace(h_terms, effect))
    )

    creation = b190.CREATION
    annihilation = b190.ANNIHILATION
    metrics = {
        2: sp.eye(16) / 2 - creation[1] * annihilation[1],
        9: -(
            creation[1] * annihilation[2]
            + creation[2] * annihilation[1]
        ) / sp.sqrt(2),
    }

    def response(metric: sp.Matrix) -> sp.Expr:
        vertex_zero = sp.expand(
            MASS * metric + I * annihilation[0] * metric
        )
        vertex_sine = sp.expand(I * (
            metric * creation[3] + annihilation[3] * metric
        ))
        source_terms = (
            (sp.eye(L_TIME), vertex_zero),
            (differential, -I * vertex_sine),
        )
        graph_derivative = tensor_scale(
            tensor_multiply(
                tensor_multiply(
                    embedded_p_inverse, source_terms
                ),
                graph,
            ),
            -1,
        )
        inverse_derivative = tensor_scale(
            tensor_multiply(
                tensor_multiply(
                    action_inverse, source_terms
                ),
                action_inverse,
            ),
            -1,
        )
        dot_h = (
            tensor_multiply(
                tensor_multiply(
                    tensor_transpose(graph_derivative), action_inverse
                ),
                graph,
            )
            + tensor_multiply(
                tensor_multiply(
                    tensor_transpose(graph), inverse_derivative
                ),
                graph,
            )
            + tensor_multiply(
                tensor_multiply(
                    tensor_transpose(graph), action_inverse
                ),
                graph_derivative,
            )
        )
        return sp.factor(
            tensor_trace(dot_h, effect) / z_effect
            - tensor_trace(dot_h) / z_value
        )

    responses = {slot: response(metric) for slot, metric in metrics.items()}
    block191_response, _hodge, _effects = b191.connected_tensor_response(
        POINTS[0][1], POINTS[0][2]
    )
    candidates = {
        slot: sp.factor(block191_response[0, slot]) for slot in metrics
    }
    cross = sp.factor(
        candidates[2] * responses[9]
        - candidates[9] * responses[2]
    )
    expected_z = R(
        9474251037834009824975984,
        16082031076968867229245,
    )
    expected_r2 = -I * R(
        50293412165579896956069392595363895,
        352171157596474667627510500819643152,
    )
    expected_r9 = sp.sqrt(2) * R(
        118579089902841470734642733193729647,
        704342315192949335255021001639286304,
    )
    expected_cross = I * sp.sqrt(2) * R(
        8535709717157696722321667574795719,
        352171157596474667627510500819643152,
    )
    alpha2 = sp.factor(candidates[2] / responses[2])
    alpha9 = sp.factor(candidates[9] / responses[9])
    return {
        "z_expected": sp.simplify(z_value - expected_z) == 0,
        "uniform_weight": sp.simplify(z_effect / z_value - R(1, 4)) == 0,
        "candidate_values": (
            candidates[2] == I / 4
            and candidates[9] == -sp.sqrt(2) / 8
        ),
        "response_values": (
            sp.simplify(responses[2] - expected_r2) == 0
            and sp.simplify(responses[9] - expected_r9) == 0
        ),
        "cross_expected": sp.simplify(cross - expected_cross) == 0,
        "cross_nonzero": cross != 0,
        "normalizations_unequal": sp.simplify(alpha2 - alpha9) != 0,
        "alpha2": alpha2,
        "alpha9": alpha9,
        "cross": cross,
    }


@cache
def two_sector_typing_facts() -> dict[str, object]:
    _action, _hodge, vertices = b190.centered_objects(
        POINTS[3][1], POINTS[3][2]
    )
    vertex = vertices[8]
    effect = b191.EFFECTS[0]
    zero = sp.zeros(16)
    identity32 = sp.eye(32)
    sector_parity = sp.diag(IDENTITY16, -IDENTITY16)
    unperturbed = sp.diag(2 * IDENTITY16, 3 * IDENTITY16)
    tangent = sp.Matrix.vstack(
        sp.Matrix.hstack(zero, vertex),
        sp.Matrix.hstack(vertex.H, zero),
    )
    diagonal_event = sp.diag(effect, effect)
    offdiagonal_readout = sp.Matrix.vstack(
        sp.Matrix.hstack(zero, effect),
        sp.Matrix.hstack(effect, zero),
    )
    phase = sp.symbols("phase", real=True)
    coherent_event = sp.Matrix.vstack(
        sp.Matrix.hstack(effect, sp.exp(I * phase) * effect),
        sp.Matrix.hstack(sp.exp(-I * phase) * effect, effect),
    ) / 2
    coherent_complement = identity32 - coherent_event
    return {
        "actual_vertex_nonzero": vertex.rank() > 0,
        "unperturbed_diagonal": matrix_equal(
            sector_parity * unperturbed,
            unperturbed * sector_parity,
        ),
        "tangent_offdiagonal": matrix_equal(
            sector_parity * tangent, -tangent * sector_parity
        ),
        "diagonal_event": matrix_equal(
            sector_parity * diagonal_event,
            diagonal_event * sector_parity,
        ),
        "diagonal_response_zero": sp.trace(
            diagonal_event * tangent
        ) == 0 and sp.trace(tangent) == 0,
        "pure_coherence_not_positive": (
            matrix_equal(offdiagonal_readout.H, offdiagonal_readout)
            and matrix_equal(
                offdiagonal_readout**2, diagonal_event
            )
            and offdiagonal_readout.rank() == 8
            and sp.trace(offdiagonal_readout) == 0
        ),
        "coherent_event_positive": (
            matrix_equal(coherent_event.H, coherent_event)
            and matrix_equal(coherent_event**2, coherent_event)
            and coherent_event.rank() == 4
            and matrix_equal(
                coherent_complement**2, coherent_complement
            )
        ),
        "coherent_raw_tangent_response_zero": sp.simplify(
            sp.trace(coherent_event * tangent)
        ) == 0,
        "coherent_phase_is_new": coherent_event.free_symbols == {phase},
    }


@cache
def source_facts() -> dict[str, object]:
    facts = tuple(
        b191.point_facts(incoming, transfer)
        for _name, incoming, transfer in POINTS
    )
    x1 = facts[-1]
    expected_x1_determinant = -3 * I * (2 * sp.sqrt(3) + 5) / 2048

    history_tangent = h1_actual_os_tangent_facts()
    d1_normalization = d1_holomorphic_normalization_facts()
    h1_source_response, _hodge, _effects = b191.connected_tensor_response(
        POINTS[3][1], POINTS[3][2]
    )
    sector_typing = two_sector_typing_facts()
    return {
        "facts": facts,
        "all_rank_two": all(point["tt_rank"] == 2 for point in facts),
        "all_derivative_only": all(
            point["mass_hodge_full_outcome_zero"] for point in facts
        ),
        "all_ward": all(point["conditioned_ward"] for point in facts),
        "x1_determinant": sp.simplify(
            x1["coefficient_determinant"] - expected_x1_determinant
        ) == 0,
        "x1_reverse": (
            x1["graded_reality"] and x1["hermitianized_reality"]
            and not x1["ordinary_reality"]
        ),
        "h1_local_slot_zero": sp.simplify(
            h1_source_response[0, 8]
        ) == 0,
        "h1_history_tangent": history_tangent,
        "h1_history_tangent_nonzero": history_tangent["response_nonzero"],
        "d1_normalization": d1_normalization,
        "d1_normalization_contradiction": (
            d1_normalization["cross_nonzero"]
            and d1_normalization["normalizations_unequal"]
        ),
        "sector_typing": sector_typing,
    }


@cache
def conditioned_write_facts() -> dict[str, object]:
    write = sp.Matrix.vstack(*b191.EFFECTS)
    write_isometry = matrix_equal(write.H * write, IDENTITY16)
    pointer_projectors = []
    for selected in range(4):
        pointer = sp.zeros(64)
        pointer[selected * 16:(selected + 1) * 16,
                selected * 16:(selected + 1) * 16] = IDENTITY16
        pointer_projectors.append(pointer)
    correlations = tuple(matrix_equal(
        pointer_projectors[index] * write,
        write * b191.EFFECTS[index],
    ) for index in range(4))
    conditioned_states = tuple(effect / 4 for effect in b191.EFFECTS)
    outputs = tuple(sp.expand(write * state * write.H)
                    for state in conditioned_states)
    return {
        "write_isometry": write_isometry,
        "effect_probabilities": tuple(
            sp.trace(effect) / 16 for effect in b191.EFFECTS
        ),
        "conditioned_states": all(
            matrix_equal(state.H, state)
            and state.rank() == 4
            and sp.trace(state) == 1
            for state in conditioned_states
        ),
        "correlations": correlations,
        "output_positive": all(
            matrix_equal(output.H, output)
            and output.rank() == 4
            and sp.trace(output) == 1
            for output in outputs
        ),
        "selected_pointer": all(matrix_equal(
            pointer_projectors[index] * outputs[index], outputs[index]
        ) for index in range(4)),
        "actual_gram_congruence_principle": (
            write_isometry and all(correlations)
        ),
        "permanent_record": False,
    }


N5_LINES = (
    "per_element: checked full exterior Clifford generators, fixed grade-three effects, and conditioned write correlations.",
    "per_site: checked the local L24 shift/link law, edge reflection, half-cut Schur graph, and lifted write-congruence principle.",
    "per_mode: checked all twelve D1-D3/H1-H2/X1 carrier endpoints, all six Block-191 source invariants, all nine exact spatial radii, and same-fiber proxy susceptibilities only at discovery points D1/H1.",
    "per_block: checked the periodic L24 carrier, four-mode control, reflected positive history, static conditioning, D1/H1 same-fiber proxy response, actual two-sector event typing, and write principle as distinct blocks.",
    "lattice_wide: checked and not executed — no full spatial lattice, general continuous-time law, nonlinear gravity, Born derivation, permanent Record dynamics, or retained TOE theory is claimed.",
)


@cache
def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "n5": False, "scope": False}
    text = NOTE_PATH.read_text(encoding="utf-8")
    scope_tokens = (
        "periodic_l24_carrier: exact",
        "four_mode_x1_closure: failed_weyl_dimension",
        "h1_same_fiber_proxy_tangent: failed_support_mismatch",
        "continuous_time_route: open",
        "permanent_record: not_claimed",
        "toe_percentage_movement: 0",
    )
    return {
        "exists": True,
        "n5": all(line in text for line in N5_LINES),
        "scope": all(token in text for token in scope_tokens),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    periodic = periodic_carrier_facts()
    compressed = compressed_carrier_facts()
    history = reduced_history_fixture()
    frozen_history = frozen_history_positivity_facts()
    source = source_facts()
    write = conditioned_write_facts()
    note = note_facts()

    claims = {
        "main": CURRENT_MAIN,
        "minimal_length": True,
        "mode_intertwiner": True,
        "modulation": True,
        "compressed_x1": False,
        "history_positive": True,
        "uniform_marginal": True,
        "x1_rank": True,
        "ward": True,
        "h1_wall": True,
        "d1_normalization_wall": True,
        "conditioned_write": True,
        "permanent_record": False,
        "toe_progress": False,
    }
    if mutation == "stale_main_authority":
        claims["main"] = "stale"
    elif mutation == "break_periodic_minimality":
        claims["minimal_length"] = False
    elif mutation == "break_mode_intertwiner":
        claims["mode_intertwiner"] = False
    elif mutation == "break_temporal_modulation":
        claims["modulation"] = False
    elif mutation == "claim_four_mode_x1_closure":
        claims["compressed_x1"] = True
    elif mutation == "break_reflection_positive_history":
        claims["history_positive"] = False
    elif mutation == "break_uniform_internal_marginal":
        claims["uniform_marginal"] = False
    elif mutation == "break_x1_source_rank":
        claims["x1_rank"] = False
    elif mutation == "break_conditioned_ward":
        claims["ward"] = False
    elif mutation == "erase_h1_tangent_support_wall":
        claims["h1_wall"] = False
    elif mutation == "erase_d1_normalization_contradiction":
        claims["d1_normalization_wall"] = False
    elif mutation == "break_conditioned_gram_write":
        claims["conditioned_write"] = False
    elif mutation == "claim_permanent_record":
        claims["permanent_record"] = True
    elif mutation == "claim_toe_progress":
        claims["toe_progress"] = True

    return {
        "A": (
            authority["main"] == claims["main"]
            and authority["parent"] and authority["prereg"]
            and authority["axiom"] == CURRENT_AXIOM_BLOB
            and authority["worktree_axiom"] == CURRENT_AXIOM_BLOB
            and authority["registry"] == CURRENT_REGISTRY_BLOB
            and authority["worktree_registry"] == WORKTREE_REGISTRY_BLOB,
            "current authority, exact Block-191 parent, and pre-target Block-192 registration are pinned",
        ),
        "B": (
            periodic["periodic"] and periodic["local"]
            and periodic["centered"]
            and periodic["minimal_length"] == claims["minimal_length"]
            and periodic["twist_forced_periodic"]
            and all(all(row) for row in periodic["mode_checks"])
            and all(periodic["reflection_checks"])
            and (all(periodic["full_mode_intertwiners"])
                 == claims["mode_intertwiner"])
            and periodic["weyl"]
            and periodic["modulation"] == claims["modulation"]
            and periodic["modulation_adjoint"]
            and periodic["link_vertex"] and periodic["link_amplitude"]
            and all(periodic["source_mode_residuals"])
            and periodic["full_reflection"]
            and periodic["outcome_reflection"]
            and periodic["weyl_order_24"],
            "periodic L24 is the minimal local carrier for both sectors and the X1 Weyl modulation, with exact full-16 endpoint/source intertwiners",
        ),
        "C": (
            compressed["skew"] and compressed["reflection"]
            and compressed["characteristic"]
            and compressed["minimal_real_dimension"]
            and compressed["raw_positive_factor"]
            and compressed["raw_rank"] == 2
            and compressed["positive_coefficient"]
            and (compressed["x1_weyl_closed"]
                 == claims["compressed_x1"])
            and compressed["minimum_weyl_dimension"] == L_TIME,
            "the exact four-mode carrier is a positive same-sector control but X1 Weyl closure forces temporal dimension at least 24",
        ),
        "D": (
            history["phase_real"] and history["real_skew"]
            and history["reflection_self_dual"]
            and history["right_graph_rank"] == L_TIME
            and history["positive_identity"]
            and (history["positive_pivots"]
                 == claims["history_positive"])
            and history["positive_rank"] == L_TIME
            and history["odd_port_negative"]
            and frozen_history["radii_exact"]
            and frozen_history["pivot_counts"] == (L_TIME,) * 9
            and all(frozen_history["full_copy_checks"])
            and frozen_history["all_positive"]
            and frozen_history["reduced_inertias"]
            == ((24, 0, 0),) * 9
            and frozen_history["full_inertias"]
            == ((192, 0, 0),) * 9
            and (history["marginal"] == claims["uniform_marginal"])
            and history["unit_symmetry"]
            and history["antiunitary_symmetry"]
            and history["scalar_fixed_algebra"]
            and history["local_blocks_scalar"],
            "at m=2/7 the honest full-form L24 reflected-even right-Schur history is positive on all nine frozen radii and has exact uniform internal marginal",
        ),
        "E": (
            source["all_rank_two"] == claims["x1_rank"]
            and source["all_derivative_only"]
            and source["all_ward"] == claims["ward"]
            and source["x1_determinant"] and source["x1_reverse"]
            and source["h1_local_slot_zero"]
            and source["h1_history_tangent"]["vertex_symbol"]
            and source["h1_history_tangent"]["z_expected"]
            and source["h1_history_tangent"]["uniform_weight"]
            and source["h1_history_tangent"]["dot_z_zero"]
            and source["h1_history_tangent"]["response_expected"]
            and source["h1_history_tangent"]["without_vertex_zero"]
            and source["h1_history_tangent"]["term_count"] == 216
            and (source["h1_history_tangent_nonzero"]
                 == claims["h1_wall"])
            and source["d1_normalization"]["z_expected"]
            and source["d1_normalization"]["uniform_weight"]
            and source["d1_normalization"]["candidate_values"]
            and source["d1_normalization"]["response_values"]
            and source["d1_normalization"]["cross_expected"]
            and (source["d1_normalization_contradiction"]
                 == claims["d1_normalization_wall"])
            and all(source["sector_typing"].values()),
            "the frozen response survives X1, but the recomputed positive-history tangent has exact D1 normalization and H1 support mismatches",
        ),
        "F": (
            write["write_isometry"]
            and write["effect_probabilities"] == (R(1, 4),) * 4
            and write["conditioned_states"]
            and all(write["correlations"])
            and write["output_positive"]
            and write["selected_pointer"]
            and write["actual_gram_congruence_principle"]
            == claims["conditioned_write"]
            and write["permanent_record"] == claims["permanent_record"],
            "the write isometry and effect correlations establish the lifted positive-congruence principle without instantiating permanence",
        ),
        "G": (
            note["exists"] and note["n5"] and note["scope"]
            and claims["toe_progress"] is False,
            "the bounded boundary, open general continuous-time route, no Record/Born claim, and zero TOE movement are stated at executed resolution",
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
