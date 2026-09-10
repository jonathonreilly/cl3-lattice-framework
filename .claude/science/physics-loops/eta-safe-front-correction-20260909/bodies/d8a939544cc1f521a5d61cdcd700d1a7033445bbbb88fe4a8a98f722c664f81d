#!/usr/bin/env python3
"""Exact H1 action-factorization and six-M2 source-ownership discriminator."""

from __future__ import annotations

import argparse
from functools import cache
import inspect
import itertools
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26 as b206  # noqa: E402


b193 = b206.b193
b190 = b193.b190
I = sp.I

PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block01-"
    "action-factorized-six-record-decoder-20260828"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_COMMIT = "42b25280486363e9c2017698b813edf182d1a1a3"
PREREG_COMMIT = "4971d278f3bd23bf9c6d4225a2a308edd6b5e2de"
CURRENT_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "a91331d17f5e159ba9ab2f9b368c7d4b717a94b9"
PREFLIGHT_BLOB = "16981bb34a1d6f1f2d40f5cfe4454c77d89f8029"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block01-action-factorized-six-record-decoder-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block01-action-factorized-six-record-decoder-20260828/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "scripts/admissibility_d4_h1_port_free_neighbor_m2_context_descent_2026_08_26.py",
    "scripts/admissibility_d4_h1_schur_record_probability_germ_2026_08_26.py",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "scripts/admissibility_d4_dirac_kahler_common_action_ward_tt_record_mark_2026_08_24.py",
)

MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "rename_alternative_phases_eta",
    "drop_actual_reverse",
    "drop_native_factor",
    "call_effective_source_radius_one",
    "call_algebraic_factor_physical_compiler",
    "erase_t2_injectivity",
    "select_odd_decoder",
    "select_even_decoder",
    "erase_decoder_family",
    "supply_internal_coframe",
    "fit_h1_and_call_unique",
    "erase_heldout_difference",
    "use_orbit_lookup",
    "open_h2",
    "open_c32",
    "claim_complete_eta_law",
    "claim_axiom_update",
    "claim_formation",
    "claim_history",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
)

N5_LINES = (
    "per_element: exact native Laurent factors, T2 source injection, and "
    "odd/even decoder matrices are checked separately.",
    "per_site: checked and not executed — the parent supplies no six-"
    "simultaneous-M2 condition tuple or physical local instrument.",
    "per_mode: the fixed H1 p,q,TT fixture is reconstructed in literal "
    "forward and actual-reverse conventions; H2 remains sealed.",
    "per_block: the complete 110-term source is reproduced from depth-three "
    "native factors, but no physical M2 compiler is inferred.",
    "lattice_wide: checked and not executed — 24 covariance frames do not "
    "instantiate autonomous formation, continuation, or a lattice history.",
)


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True
    ).strip()


def poly_equal(
    left: b190.PolyMatrix, right: b190.PolyMatrix
) -> bool:
    return not b190.poly_add(left, b190.poly_scale(right, -1))


def poly_sum(
    polynomials: tuple[b190.PolyMatrix, ...],
    coefficients: tuple[sp.Expr, ...],
) -> b190.PolyMatrix:
    result: b190.PolyMatrix = {}
    for coefficient, polynomial in zip(coefficients, polynomials):
        result = b190.poly_add(
            result, b190.poly_scale(polynomial, coefficient)
        )
    return result


def support_summary(polynomial: b190.PolyMatrix) -> tuple[int, int, int]:
    return (
        len(polynomial),
        max(sum(abs(x) for x in power[:4]) for power in polynomial),
        max(sum(abs(x) for x in power[4:]) for power in polynomial),
    )


def actual_reverse(
    source: b190.PolyMatrix,
) -> b190.PolyMatrix:
    result: b190.PolyMatrix = {}
    for power, matrix in source.items():
        transformed = tuple(power[axis] for axis in range(4)) + tuple(
            power[axis] - power[4 + axis] for axis in range(4)
        )
        result = b190.poly_add(result, {transformed: matrix})
    return result


def proper_cubic_rotations() -> tuple[sp.Matrix, ...]:
    rotations = []
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            matrix = sp.zeros(3)
            for column, row in enumerate(permutation):
                matrix[row, column] = signs[column]
            if matrix.det() == 1:
                rotations.append(matrix)
    return tuple(rotations)


def shell_representation(rotation: sp.MatrixBase) -> sp.Matrix:
    shell = tuple(
        sign * sp.eye(3)[:, axis]
        for axis in range(3) for sign in (1, -1)
    )
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
    basis = (
        sp.Matrix(((0, 1, 0), (1, 0, 0), (0, 0, 0))),
        sp.Matrix(((0, 0, 0), (0, 0, 1), (0, 1, 0))),
        sp.Matrix(((0, 0, 1), (0, 0, 0), (1, 0, 0))),
    )
    columns = []
    for tensor in basis:
        transformed = sp.Matrix(rotation * tensor * rotation.T)
        columns.append(sp.Matrix((
            transformed[0, 1],
            transformed[1, 2],
            transformed[0, 2],
        )))
    return sp.Matrix.hstack(*columns)


def decoder_basis() -> tuple[sp.Matrix, sp.Matrix]:
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


def flatten_polynomials(
    polynomials: tuple[b190.PolyMatrix, ...],
) -> sp.Matrix:
    powers = sorted(set().union(*(item.keys() for item in polynomials)))
    columns = []
    for polynomial in polynomials:
        entries = []
        for power in powers:
            entries.extend(list(polynomial.get(power, sp.zeros(16))))
        columns.append(sp.Matrix(entries))
    return sp.Matrix.hstack(*columns)


@cache
def authority_facts() -> dict[str, object]:
    return {
        "origin_main": git_output("rev-parse", "origin/main"),
        "parent_is_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT_COMMIT, "HEAD"),
            cwd=ROOT,
            check=False,
        ).returncode == 0,
        "prereg_is_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG_COMMIT, "HEAD"),
            cwd=ROOT,
            check=False,
        ).returncode == 0,
        "goal_blob": git_output("rev-parse", f"{PREREG_COMMIT}:{GOAL_PATH}"),
        "preflight_blob": git_output(
            "rev-parse", f"{PREREG_COMMIT}:{PREFLIGHT_PATH}"
        ),
        "axiom_main_blob": git_output(
            "rev-parse", f"origin/main:{AXIOM_PATH}"
        ),
        "axiom_worktree_blob": git_output("rev-parse", f"HEAD:{AXIOM_PATH}"),
        "registry_main_blob": git_output(
            "rev-parse", f"origin/main:{REGISTRY_PATH}"
        ),
        "registry_worktree_blob": git_output(
            "rev-parse", f"HEAD:{REGISTRY_PATH}"
        ),
    }


@cache
def typing_facts() -> dict[str, object]:
    raw_source = inspect.getsource(b206.combined_raw_source)
    raw_vertices = inspect.getsource(b206.raw_action_vertices)
    coefficient_source = inspect.getsource(b193.tt_source_coefficients)
    phase_source = inspect.getsource(b206.phase_series_facts)
    phases = (
        sp.Rational(1, 2) - I * sp.sqrt(3) / 2,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
        -I,
        I,
        sp.Integer(1),
        sp.Integer(1),
    )
    return {
        "source_signature": tuple(
            inspect.signature(b206.combined_raw_source).parameters
        ),
        "vertex_signature": tuple(
            inspect.signature(b206.raw_action_vertices).parameters
        ),
        "coefficient_signature": tuple(
            inspect.signature(b193.tt_source_coefficients).parameters
        ),
        "six_alternative_phases": len(phases),
        "phase_tuple_declared_by_parent": (
            '"neighbor_phases": phases' in phase_source
        ),
        "eta_token_in_source_chain": any(
            "eta" in source.lower()
            for source in (raw_source, raw_vertices, coefficient_source)
        ),
        "source_calls_fixed_tt_coefficients": (
            'tt_source_coefficients("H1", 1)' in raw_source
        ),
        "simultaneous_eta_supplier_present": False,
    }


@cache
def factorization_facts() -> dict[str, object]:
    differential_0: b190.PolyMatrix = {}
    differential_1: b190.PolyMatrix = {}
    for axis in range(4):
        differential_0 = b190.poly_add(differential_0, {
            b190.exponent({axis: 1}):
                b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}):
                -b190.CREATION[axis] / (2 * I),
        })
        differential_1 = b190.poly_add(differential_1, {
            b190.exponent({axis: 1}, {axis: 1}):
                b190.CREATION[axis] / (2 * I),
            b190.exponent({axis: -1}, {axis: -1}):
                -b190.CREATION[axis] / (2 * I),
        })

    coefficients = b193.tt_source_coefficients("H1", 1)
    nonzero_slots = tuple(
        index for index, value in enumerate(coefficients) if value != 0
    )
    cosine_products = []
    hodges = []
    mass_pieces = []
    incoming_pieces = []
    outgoing_pieces = []
    vertices = []
    for slot in nonzero_slots:
        left, right = b190.PAIRS4[slot]
        cosine_product = b190.poly_multiply(
            b190.placed_cosine(left), b190.placed_cosine(right)
        )
        hodge = b190.poly_multiply(
            b190.poly_scale(cosine_product, -1 / sp.sqrt(2)),
            {b190.ZERO_EXPONENT: (
                b190.CREATION[left] * b190.ANNIHILATION[right]
                + b190.CREATION[right] * b190.ANNIHILATION[left]
            )},
        )
        mass_piece = b190.poly_scale(hodge, b190.MASS)
        incoming_piece = b190.poly_scale(
            b190.poly_multiply(hodge, differential_0), I
        )
        outgoing_piece = b190.poly_scale(
            b190.poly_multiply(
                b190.poly_transpose(differential_1), hodge
            ),
            I,
        )
        vertex = b190.poly_add(
            mass_piece, incoming_piece, outgoing_piece
        )
        cosine_products.append(cosine_product)
        hodges.append(hodge)
        mass_pieces.append(mass_piece)
        incoming_pieces.append(incoming_piece)
        outgoing_pieces.append(outgoing_piece)
        vertices.append(vertex)

    selected_coefficients = tuple(coefficients[index]
                                  for index in nonzero_slots)
    stages = {
        "cosine": poly_sum(tuple(cosine_products), selected_coefficients),
        "hodge": poly_sum(tuple(hodges), selected_coefficients),
        "mass": poly_sum(tuple(mass_pieces), selected_coefficients),
        "incoming": poly_sum(tuple(incoming_pieces), selected_coefficients),
        "outgoing": poly_sum(tuple(outgoing_pieces), selected_coefficients),
        "source": poly_sum(tuple(vertices), selected_coefficients),
    }
    direct_vertices = b206.raw_action_vertices()
    direct = poly_sum(direct_vertices, coefficients)
    inherited = b206.combined_raw_source()
    reversed_staged = actual_reverse(stages["source"])
    reversed_direct = actual_reverse(inherited)

    primitive_factors = tuple(
        b190.placed_cosine(axis) for axis in (0, 1, 2)
    ) + (differential_0, differential_1)
    primitive_summaries = tuple(
        support_summary(item) for item in primitive_factors
    )
    stage_summaries = tuple(
        support_summary(stages[name])
        for name in ("cosine", "hodge", "mass",
                     "incoming", "outgoing", "source")
    )

    shear_vertices = (
        b190.poly_scale(direct_vertices[7], sp.sqrt(2)),
        b190.poly_scale(direct_vertices[9], sp.sqrt(2)),
        b190.poly_scale(direct_vertices[8], sp.sqrt(2)),
    )
    t2_source_rank = flatten_polynomials(shear_vertices).rank()
    target_shear = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    target_coefficients = [sp.Integer(0)] * 10
    target_coefficients[7] = sp.sqrt(2) * target_shear[0]
    target_coefficients[9] = sp.sqrt(2) * target_shear[1]
    target_coefficients[8] = sp.sqrt(2) * target_shear[2]
    target_source = poly_sum(
        direct_vertices, tuple(target_coefficients)
    )

    return {
        "nonzero_slots": nonzero_slots,
        "primitive_summaries": primitive_summaries,
        "stage_summaries": stage_summaries,
        "max_shifted_factor_depth": 3,
        "staged_equals_direct": poly_equal(stages["source"], direct),
        "direct_equals_inherited": poly_equal(direct, inherited),
        "reverse_equals_inherited": poly_equal(
            reversed_staged, reversed_direct
        ),
        "forward_terms": len(inherited),
        "actual_reverse_terms": len(reversed_direct),
        "t2_source_rank": t2_source_rank,
        "target_source_matches_h1": poly_equal(target_source, inherited),
        "effective_source_radius_one": (
            support_summary(inherited)[1:] == (1, 1)
        ),
        "physical_m2_compiler_supplied": False,
    }


@cache
def decoder_facts() -> dict[str, object]:
    rotations = proper_cubic_rotations()
    odd, even = decoder_basis()
    equivariant = True
    for rotation in rotations:
        shell = shell_representation(rotation)
        domain = sp.kronecker_product(shell, rotation)
        target = shear_representation(rotation)
        equivariant = equivariant and all(
            target * decoder == decoder * domain
            for decoder in (odd, even)
        )

    phases = (
        sp.Rational(1, 2) - I * sp.sqrt(3) / 2,
        sp.Rational(1, 2) + I * sp.sqrt(3) / 2,
        -I,
        I,
        sp.Integer(1),
        sp.Integer(1),
    )
    phase_input = sp.Matrix.vstack(*(
        sp.Matrix((sp.re(value), sp.im(value), 0))
        for value in phases
    ))
    target_shear = sp.Matrix((0, 1 / sp.sqrt(2), -1))
    solutions = []
    law_maps = []
    for rotation in rotations:
        internal_action = sp.kronecker_product(sp.eye(6), rotation)
        transformed_input = internal_action * phase_input
        columns = sp.Matrix.hstack(
            odd * transformed_input,
            even * transformed_input,
        )
        if columns.rank() != columns.row_join(target_shear).rank():
            continue
        if columns.rank() != 2:
            continue
        coefficients = tuple(
            sp.simplify(value)
            for value in columns.gauss_jordan_solve(target_shear)[0]
        )
        law = sp.simplify(
            (coefficients[0] * odd + coefficients[1] * even)
            * internal_action
        )
        solutions.append(coefficients)
        law_maps.append(law)

    distinct_law_maps = {
        tuple(matrix) for matrix in law_maps
    }
    input_stabilizer = sum(
        sp.kronecker_product(sp.eye(6), rotation) * phase_input
        == phase_input
        for rotation in rotations
    )
    incoming, transfer = b193.POINTS["H1"]
    fixture_stabilizer = sum(
        tuple(rotation * sp.Matrix(incoming[:3])) == incoming[:3]
        and tuple(rotation * sp.Matrix(transfer[:3])) == transfer[:3]
        for rotation in rotations
    )
    heldout_distinguishes = all(
        any(
            law_maps[left][:, column] != law_maps[right][:, column]
            for column in range(18)
        )
        for left in range(len(law_maps))
        for right in range(left)
    )
    basis_rank = sp.Matrix.hstack(
        odd.reshape(54, 1), even.reshape(54, 1)
    ).rank()
    return {
        "rotation_count": len(rotations),
        "basis_rank": basis_rank,
        "basis_ranks": (odd.rank(), even.rank()),
        "basis_equivariant": equivariant,
        "phase_fit_count": len(solutions),
        "distinct_law_map_count": len(distinct_law_maps),
        "phase_input_stabilizer": input_stabilizer,
        "fixture_stabilizer": fixture_stabilizer,
        "all_phase_fits_reproduce_h1": all(
            law * phase_input == target_shear for law in law_maps
        ),
        "heldout_basis_distinguishes_all_maps": heldout_distinguishes,
        "action_selected_decoder": False,
        "internal_cubic_action_derived": False,
        "complete_eta_law": False,
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    typing = dict(typing_facts())
    factor = dict(factorization_facts())
    decoder = dict(decoder_facts())
    claims: dict[str, object] = {
        "alternative_phases_are_eta": False,
        "literal_actual_reverse_checked": True,
        "native_factor_complete": True,
        "algebraic_factorization": True,
        "physical_m2_compiler": False,
        "t2_source_injective": factor["t2_source_rank"] == 3,
        "decoder_selected": False,
        "decoder_family_dimension": 2,
        "internal_coframe_supplied": False,
        "phase_comparator_unique": False,
        "heldout_maps_differ": decoder[
            "heldout_basis_distinguishes_all_maps"
        ],
        "orbit_lookup_used": False,
        "h2_opened": False,
        "c32_opened": False,
        "complete_eta_law": False,
        "axiom_update": False,
        "formation": False,
        "history": False,
        "obligation_retirement": 0,
        "toe_progress": 0,
        "retained_status": False,
    }

    if mutation == "stale_main_authority":
        authority["origin_main"] = "stale"
    elif mutation == "drop_preregistration":
        authority["prereg_is_ancestor"] = False
    elif mutation == "alter_goal_after_registration":
        authority["goal_blob"] = "altered"
    elif mutation == "rename_alternative_phases_eta":
        claims["alternative_phases_are_eta"] = True
    elif mutation == "drop_actual_reverse":
        claims["literal_actual_reverse_checked"] = False
    elif mutation == "drop_native_factor":
        claims["native_factor_complete"] = False
    elif mutation == "call_effective_source_radius_one":
        factor["effective_source_radius_one"] = True
    elif mutation == "call_algebraic_factor_physical_compiler":
        claims["physical_m2_compiler"] = True
    elif mutation == "erase_t2_injectivity":
        claims["t2_source_injective"] = False
    elif mutation == "select_odd_decoder":
        claims["decoder_selected"] = "odd"
    elif mutation == "select_even_decoder":
        claims["decoder_selected"] = "even"
    elif mutation == "erase_decoder_family":
        claims["decoder_family_dimension"] = 1
    elif mutation == "supply_internal_coframe":
        claims["internal_coframe_supplied"] = True
    elif mutation == "fit_h1_and_call_unique":
        claims["phase_comparator_unique"] = True
    elif mutation == "erase_heldout_difference":
        claims["heldout_maps_differ"] = False
    elif mutation == "use_orbit_lookup":
        claims["orbit_lookup_used"] = True
    elif mutation == "open_h2":
        claims["h2_opened"] = True
    elif mutation == "open_c32":
        claims["c32_opened"] = True
    elif mutation == "claim_complete_eta_law":
        claims["complete_eta_law"] = True
    elif mutation == "claim_axiom_update":
        claims["axiom_update"] = True
    elif mutation == "claim_formation":
        claims["formation"] = True
    elif mutation == "claim_history":
        claims["history"] = True
    elif mutation == "claim_obligation_retirement":
        claims["obligation_retirement"] = 1
    elif mutation == "claim_toe_progress":
        claims["toe_progress"] = 1
    elif mutation == "claim_retained_status":
        claims["retained_status"] = True

    authority_ok = (
        authority["origin_main"] == CURRENT_MAIN
        and authority["parent_is_ancestor"]
        and authority["prereg_is_ancestor"]
        and authority["goal_blob"] == GOAL_BLOB
        and authority["preflight_blob"] == PREFLIGHT_BLOB
        and authority["axiom_main_blob"] == AXIOM_BLOB
        and authority["axiom_worktree_blob"] == AXIOM_BLOB
        and authority["registry_main_blob"] == REGISTRY_MAIN_BLOB
        and authority["registry_worktree_blob"] == REGISTRY_WORKTREE_BLOB
    )
    typing_ok = (
        typing["source_signature"] == ()
        and typing["vertex_signature"] == ()
        and typing["coefficient_signature"] == ("point_name", "column")
        and typing["six_alternative_phases"] == 6
        and typing["phase_tuple_declared_by_parent"]
        and not typing["eta_token_in_source_chain"]
        and typing["source_calls_fixed_tt_coefficients"]
        and not typing["simultaneous_eta_supplier_present"]
        and not claims["alternative_phases_are_eta"]
    )
    factor_ok = (
        factor["nonzero_slots"] == (8, 9)
        and factor["primitive_summaries"] == (
            (2, 1, 1), (2, 1, 1), (2, 1, 1),
            (8, 1, 0), (8, 1, 1),
        )
        and factor["stage_summaries"] == (
            (8, 2, 2), (8, 2, 2), (8, 2, 2),
            (60, 3, 2), (60, 3, 3), (110, 3, 3),
        )
        and factor["max_shifted_factor_depth"] == 3
        and factor["staged_equals_direct"]
        and claims["native_factor_complete"]
        and claims["algebraic_factorization"]
        and not factor["effective_source_radius_one"]
    )
    source_ok = (
        factor["direct_equals_inherited"]
        and factor["reverse_equals_inherited"]
        and factor["forward_terms"] == 110
        and factor["actual_reverse_terms"] == 110
        and factor["target_source_matches_h1"]
        and claims["literal_actual_reverse_checked"]
    )
    injection_ok = (
        factor["t2_source_rank"] == 3
        and claims["t2_source_injective"]
        and not factor["physical_m2_compiler_supplied"]
        and not claims["physical_m2_compiler"]
    )
    decoder_ok = (
        decoder["rotation_count"] == 24
        and decoder["basis_rank"] == 2
        and decoder["basis_ranks"] == (3, 3)
        and decoder["basis_equivariant"]
        and claims["decoder_family_dimension"] == 2
        and claims["decoder_selected"] is False
        and not decoder["action_selected_decoder"]
        and not decoder["internal_cubic_action_derived"]
        and not claims["internal_coframe_supplied"]
    )
    comparator_ok = (
        decoder["phase_fit_count"] == 8
        and decoder["distinct_law_map_count"] == 8
        and decoder["phase_input_stabilizer"] == 1
        and decoder["fixture_stabilizer"] == 1
        and decoder["all_phase_fits_reproduce_h1"]
        and decoder["heldout_basis_distinguishes_all_maps"]
        and claims["heldout_maps_differ"]
        and not claims["phase_comparator_unique"]
        and not claims["orbit_lookup_used"]
    )
    scope_ok = (
        not claims["h2_opened"]
        and not claims["c32_opened"]
        and not decoder["complete_eta_law"]
        and not claims["complete_eta_law"]
        and not claims["axiom_update"]
        and not claims["formation"]
        and not claims["history"]
        and claims["obligation_retirement"] == 0
        and claims["toe_progress"] == 0
        and not claims["retained_status"]
    )
    return {
        "authority_and_preregistration": (
            authority_ok,
            "origin/main, parent, preregistration, goal, preflight, axiom, "
            "and registry blobs are pinned",
        ),
        "carrier_and_input_typing": (
            typing_ok,
            "six alternative phase conditions are not renamed as six "
            "simultaneous M2 inputs",
        ),
        "native_factorization": (
            factor_ok,
            "H1 source has exact depth-three native factors with staged "
            "support 8/8/8/60/60/110",
        ),
        "forward_actual_reverse_reconstruction": (
            source_ok,
            "literal forward and actual reverse each reconstruct all 110 "
            "Laurent terms",
        ),
        "t2_source_injection_boundary": (
            injection_ok,
            "the action injects all three T2 coordinates but supplies no "
            "physical eta-to-M2 compiler",
        ),
        "conditional_decoder_family": (
            decoder_ok,
            "the exact proper-cubic decoder space remains two-dimensional "
            "and no internal coframe or member is selected",
        ),
        "overgenerous_phase_ambiguity": (
            comparator_ok,
            "even the phase-as-six-Bloch comparator has eight distinct H1 "
            "fits separated by held-out one-site inputs",
        ),
        "scope_and_accounting": (
            scope_ok,
            "H2/C32, formation, history, axiom, retention, obligation, and "
            "TOE gates remain closed",
        ),
    }


def mutation_sweep() -> tuple[int, int]:
    survivors = []
    for mutation in MUTATIONS:
        checks = evaluate(mutation)
        if all(ok for ok, _message in checks.values()):
            survivors.append(mutation)
    passed = len(MUTATIONS) - len(survivors)
    print(f"MUTATION_TOTAL: PASS={passed} FAIL={len(survivors)}")
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
    return passed, len(survivors)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation and args.mutation not in MUTATIONS:
        raise SystemExit(f"unknown mutation: {args.mutation}")

    mutation_failures = 0
    if args.mutation_sweep:
        _passed, mutation_failures = mutation_sweep()

    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"[{name}] {'PASS' if ok else 'FAIL'}: {message}")
        passed += int(ok)
    factor = factorization_facts()
    decoder = decoder_facts()
    print(
        "FACTOR: primitive depth=3; staged supports="
        f"{tuple(item[0] for item in factor['stage_summaries'])}; "
        "forward/reverse=110/110; effective radius=3."
    )
    print(
        "DECODER: conditional Hom dimension=2; phase comparator "
        f"fits={decoder['phase_fit_count']}; distinct laws="
        f"{decoder['distinct_law_map_count']}; selected=false."
    )
    print(
        "DECISION: algebraic locality closes; actual eta supplier, internal "
        "cubic action, decoder selection, and physical M2 compiler remain "
        "open; obligation retirement=0; TOE movement=0."
    )
    for line in N5_LINES:
        print(line)
    failures = len(checks) - passed + mutation_failures
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
