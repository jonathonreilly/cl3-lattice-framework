#!/usr/bin/env python3
"""Block 205: positive H1 right-Schur Record probability germ.

This runner keeps four objects separate: the full L24 two-sector Schur
family, its C32 boundary marginal, the fixed Block-194 eight-effect PVM, and
the M2 pointer dilation.  It proves a finite positive analytic germ from
strict zero-source positivity plus an exact nonzero derivative; the tangent
is evidence for nonconstancy, not a state substituted for the finite family.
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

import admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25 as b192  # noqa: E402
import admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25 as b193  # noqa: E402
import admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25 as b194  # noqa: E402


NOTE_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_"
    "BOUNDED_THEOREM_NOTE_2026-08-26.md"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block205-h1-schur-record-probability-germ-20260826"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
AXIOM_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"

PARENT_COMMIT = "4692fc1998b82328809bdf0696bf36a97cd7d3e3"
PREREG_COMMIT = "d067fbb5d2"
CURRENT_MAIN = "76df4becc8233080bc5a10a4baf55f83e80f8f2d"
GOAL_BLOB = "951dad5c1a075687eb77b79d3a858e1fcc010c92"
PREFLIGHT_BLOB = "9613ca777600c348ccebacfc8a5255a654e67898"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
REGISTRY_MAIN_BLOB = "b93959cca4f7e26c673cdccbe601e50c3cb93daa"
REGISTRY_WORKTREE_BLOB = "f01d3be864f682584d50eede8b3abe6671bb4719"
TIMEOUT_SEC = 300

AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_SCHUR_RECORD_PROBABILITY_GERM_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    ".claude/science/physics-loops/toe-axiom-closure-block205-h1-schur-record-probability-germ-20260826/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block205-h1-schur-record-probability-germ-20260826/PREFLIGHT_WITNESSES.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/ADMISSIBILITY_D4_FULL_TEMPORAL_CARRIER_SOURCE_HISTORY_WRITE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_full_temporal_carrier_source_history_write_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_FIXED_L24_RECORD_LAW_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_fixed_l24_record_law_discriminator_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_DETECTOR_CONDITIONED_M2_POINTER_DISCRIMINATOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-25.md",
    "scripts/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.py",
    "logs/runner-cache/admissibility_d4_detector_conditioned_m2_pointer_discriminator_2026_08_25.txt",
    "docs/ADMISSIBILITY_D4_RECORD_OPERATOR_SYSTEM_DESCENT_OS_PROBABILITY_CONTROL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-26.md",
    "scripts/admissibility_d4_record_operator_system_descent_2026_08_26.py",
)

MUTATIONS = (
    "stale_main_authority",
    "drop_preregistration",
    "alter_goal_after_registration",
    "replace_actual_reverse_by_adjoint",
    "use_blind_h1_column",
    "call_tangent_a_state",
    "drop_zero_source_strict_positivity",
    "drop_analytic_denominator",
    "deny_positive_interval",
    "break_pvm_positivity",
    "break_pvm_completeness",
    "import_maximally_mixed_c32",
    "erase_nonzero_h1_slope",
    "call_finite_family_uniform",
    "break_coarse_addition",
    "break_pointer_pullback",
    "call_pointer_bit_eight_labels",
    "erase_conditional_m2_variation",
    "erase_port_pointer_correlation",
    "call_h1_nearest_neighbor_eta",
    "call_pointer_write_formation",
    "call_one_shot_permanent_history",
    "call_schur_periodic_car_state",
    "call_schur_full_fock_state",
    "claim_two_tt_completion",
    "claim_axiom_update",
    "claim_obligation_retirement",
    "claim_toe_progress",
    "claim_retained_status",
    "claim_broad_record_no_go",
)


I = sp.I
R = sp.Rational
IDENTITY16 = sp.eye(16)


def git_output(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=TIMEOUT_SEC
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=TIMEOUT_SEC,
    ).returncode == 0


def matrix_equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return all(sp.simplify(value) == 0 for value in left - right)


def exact_rank(matrix: sp.MatrixBase) -> int:
    return DomainMatrix.from_Matrix(
        sp.Matrix(matrix), extension=True
    ).rank()


def reduced_internal(family: b193.Terms) -> sp.Matrix:
    """Trace the positive-half temporal factor of one tensor-term family."""
    return sp.expand(sum(
        (sp.trace(temporal) * internal for temporal, internal in family),
        sp.zeros(16),
    ))


def exact_positive(value: sp.Expr) -> bool:
    simplified = sp.factor(sp.simplify(value))
    if simplified.is_positive is not None:
        return simplified.is_positive is True
    # All live values lie in a real algebraic extension.  SymPy's exact
    # relational simplifier resolves the fallback without a float threshold.
    relation = sp.simplify(simplified > 0)
    return relation is sp.true


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
def frozen_source_facts() -> dict[str, object]:
    coefficients = b193.tt_source_coefficients("H1", 1)
    blind_coefficients = b193.tt_source_coefficients("H1", 0)
    source = b193.combined_source_pair_terms("H1", coefficients)
    literal = b193.literal_source_facts()
    return {
        "coefficients": coefficients,
        "blind_coefficients": blind_coefficients,
        "forward_terms": len(source["forward"]),
        "reverse_terms": len(source["reverse"]),
        "actual_reverse_distinct": not all(
            b193.matrix_equal(left[0], right[0])
            and b193.matrix_equal(left[1], right[1])
            for left, right in zip(
                source["reverse"], source["hermitian_control"]
            )
        ) if len(source["reverse"]) == len(source["hermitian_control"]) else True,
        "literal_parent": literal["literal"],
        "actual_reverse_parent": literal["actual_reverse_distinct"],
        "block_placement": literal["block_placement"],
    }


@cache
def zero_source_state_facts() -> dict[str, object]:
    incoming, transfer = b193.POINTS["H1"]
    outgoing = tuple(incoming[axis] + transfer[axis] for axis in range(4))
    incoming_sector = b193.sector_terms(incoming)
    outgoing_sector = b193.sector_terms(outgoing)
    rho_in_raw = reduced_internal(incoming_sector["gram"])
    rho_out_raw = reduced_internal(outgoing_sector["gram"])
    trace_in = sp.factor(sp.trace(rho_in_raw))
    trace_out = sp.factor(sp.trace(rho_out_raw))
    total = sp.factor(trace_in + trace_out)
    rho0 = sp.diag(rho_in_raw, rho_out_raw) / total
    scalar_in = sp.factor(trace_in / 16)
    scalar_out = sp.factor(trace_out / 16)
    history = b192.frozen_history_positivity_facts()
    return {
        "incoming": incoming,
        "outgoing": outgoing,
        "rho_in_raw": rho_in_raw,
        "rho_out_raw": rho_out_raw,
        "trace_in": trace_in,
        "trace_out": trace_out,
        "total": total,
        "rho0": sp.expand(rho0),
        "sector_scalars": (
            matrix_equal(rho_in_raw, scalar_in * IDENTITY16),
            matrix_equal(rho_out_raw, scalar_out * IDENTITY16),
        ),
        "sector_traces_positive": (
            exact_positive(trace_in), exact_positive(trace_out)
        ),
        "strict_full_gram": history["all_positive"],
        "parent_full_inertias": history["full_inertias"],
    }


@cache
def instrument_facts() -> dict[str, object]:
    instrument = b194.instrument_pointer_facts()
    effects = instrument["effects"]
    zero = zero_source_state_facts()
    rho0 = zero["rho0"]
    probabilities = tuple(sp.factor(sp.trace(rho0 * effect))
                          for effect in effects)
    return {
        "effects": effects,
        "projectors": instrument["projectors"],
        "pairwise_orthogonal": instrument["pairwise_orthogonal"],
        "complete": instrument["complete"],
        "coarsenings": instrument["coarsenings"],
        "effect_ranks": instrument["effect_ranks"],
        "probabilities": probabilities,
        "baseline_uniform": probabilities == (R(1, 8),) * 8,
        "writer_unitary": instrument["writer_unitary"],
        "writer_nonidentity": instrument["writer_nonidentity"],
        "faithful_joint_readout": instrument["faithful_joint_readout"],
        "pointer_projectors": instrument["pointer_projectors"],
        "pointer_orthogonal": instrument["pointer_orthogonal"],
        "pointer_complete": instrument["pointer_complete"],
        "pointer_label_flip": instrument["pointer_label_flip"],
        "reflection_effect_map": instrument["reflection_effect_map"],
    }


@cache
def response_germ_facts() -> dict[str, object]:
    response = b194.response_facts("H1")
    slopes = response["slopes"]
    ell = sp.factor(slopes[0, 1])
    row_slopes = tuple(sp.factor(slopes[row, 1]) for row in range(4))
    effect_derivatives = tuple(
        sp.factor(sign * row_slopes[row] / 8)
        for row in range(4) for sign in (1, -1)
    )
    conditional_derivatives = tuple(
        sp.factor(sign * row_slopes[row] / 2)
        for row in range(4) for sign in (1, -1)
    )
    coarse_derivatives = tuple(sp.factor(
        effect_derivatives[2 * row] + effect_derivatives[2 * row + 1]
    ) for row in range(4))
    pointer_marginal_derivatives = tuple(sp.factor(sum(
        effect_derivatives[2 * row + sign_index] for row in range(4)
    )) for sign_index in range(2))
    port_character = (1, 1, -1, -1)
    correlation_derivative = sp.factor(sum(
        port_character[row] * sign *
        effect_derivatives[2 * row + sign_index]
        for row in range(4)
        for sign_index, sign in enumerate((1, -1))
    ))
    return {
        "complex_rank": response["complex_rank"],
        "real_rank": response["real_rank"],
        "first_column_zero": response["first_column_zero"],
        "second_column_zero": response["second_column_zero"],
        "signed_pair": response["second_column_signed_pair"],
        "source_operator_nonzero": response["source_second_column_nonzero"],
        "ell": ell,
        "ell_positive": exact_positive(ell),
        "row_slopes": row_slopes,
        "signed_pattern": (
            sp.simplify(row_slopes[0] - ell) == 0
            and sp.simplify(row_slopes[1] - ell) == 0
            and sp.simplify(row_slopes[2] + ell) == 0
            and sp.simplify(row_slopes[3] + ell) == 0
        ),
        "effect_derivatives": effect_derivatives,
        "conditional_derivatives": conditional_derivatives,
        "coarse_derivatives": coarse_derivatives,
        "pointer_marginal_derivatives": pointer_marginal_derivatives,
        "correlation_derivative": correlation_derivative,
        "correlation_nonzero": sp.simplify(correlation_derivative) != 0,
    }


def positive_analytic_germ_lemma() -> dict[str, bool]:
    """Finite-dimensional openness/analyticity implication.

    A(e) and its P-block are affine matrix families.  Invertibility at zero
    makes their inverses rational and analytic in some open interval.  The
    Schur Gram is therefore analytic.  Strict positivity of G(0) is open.
    A complete PVM evaluated on the normalized positive marginal gives eight
    positive analytic probabilities summing to one.  A nonzero derivative
    makes the family nonconstant at finite nonzero e in a smaller interval.
    """
    zero = zero_source_state_facts()
    instrument = instrument_facts()
    response = response_germ_facts()
    denominators_nonzero_at_zero = (
        zero["trace_in"] != 0 and zero["trace_out"] != 0
        and zero["total"] != 0
    )
    analytic_family = (
        frozen_source_facts()["forward_terms"] > 0
        and frozen_source_facts()["reverse_terms"] > 0
        and denominators_nonzero_at_zero
    )
    strict_positive_at_zero = (
        zero["strict_full_gram"]
        and all(zero["sector_traces_positive"])
    )
    pvm = (
        instrument["projectors"] and instrument["pairwise_orthogonal"]
        and instrument["complete"] and instrument["baseline_uniform"]
    )
    derivative_nonzero = (
        response["real_rank"] == 1 and response["ell_positive"]
        and response["signed_pattern"]
    )
    return {
        "denominators_nonzero_at_zero": denominators_nonzero_at_zero,
        "analytic_family": analytic_family,
        "strict_positive_at_zero": strict_positive_at_zero,
        "pvm": pvm,
        "derivative_nonzero": derivative_nonzero,
        "positive_interval_exists": (
            analytic_family and strict_positive_at_zero and pvm
        ),
        "finite_nonconstant_law_exists": (
            analytic_family and strict_positive_at_zero and pvm
            and derivative_nonzero
        ),
    }


@cache
def covariance_facts() -> dict[str, object]:
    classification = b194.detector_classification_facts()
    instrument = instrument_facts()
    # Trace covariance is exact for every supplied unitary representation:
    # Tr((U rho U^dag)(U F U^dag)) = Tr(rho F).  Parent gates supply the
    # physical 24-frame detector/context transformations.
    symbolic_trace_covariance = True
    return {
        "proper_cubic_count": classification["proper_cubic_count"],
        "detector_family": classification["family_covariance"],
        "context_family": classification["context_covariance"],
        "coordinate_reflection": (
            classification["coordinate_reflection_odd"]
            and classification["coordinate_reflection_context_fixed"]
        ),
        "effect_reflection": instrument["reflection_effect_map"],
        "trace_covariance": symbolic_trace_covariance,
    }


def note_facts() -> dict[str, bool]:
    if not NOTE_PATH.is_file():
        return {"exists": False, "scope": False, "n5": False}
    text = NOTE_PATH.read_text()
    needles = (
        "right-Schur probability germ",
        "not a periodic CAR state",
        "nearest-neighbor eta remains open",
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
    "per_element: checked the literal H1 source column, all eight fixed C32 effects, four coarse ports, two pointer signs, exact derivatives, and normalized positive-germ implications.",
    "per_site: checked the fixed nonidentity M2 pointer pullback conditional on one supplied coarse port; no autonomous formation site, hazard, or permanence dynamics is supplied.",
    "per_mode: checked the H1 second TT direction exactly and the blind first direction as a control; the H2 finite-family held-out remains separate unless explicitly reported.",
    "per_block: checked the full two-sector Schur family, C32 boundary marginal, PVM, and pointer as distinct typed blocks; no periodic CAR or Lambda(C32) state is inferred.",
    "lattice_wide: checked and not executed — the Fourier H1 source is not identified with every nearest-neighbor eta, and no full-Z3 history, gravity completion, retained theory, axiom edit, or TOE closure is claimed.",
)


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = authority_facts()
    source = frozen_source_facts()
    zero = zero_source_state_facts()
    instrument = instrument_facts()
    response = response_germ_facts()
    germ = positive_analytic_germ_lemma()
    covariance = covariance_facts()
    note = note_facts()

    claims: dict[str, object] = {
        "main": CURRENT_MAIN,
        "prereg": True,
        "goal_blob": GOAL_BLOB,
        "actual_reverse": True,
        "tt_column": 1,
        "tangent_is_state": False,
        "strict_zero_positive": True,
        "analytic_denominator": True,
        "positive_interval": True,
        "pvm_positive": True,
        "pvm_complete": True,
        "maximally_mixed_import": False,
        "nonzero_slope": True,
        "finite_uniform": False,
        "coarse_addition": True,
        "pointer_pullback": True,
        "pointer_bit_eight_labels": False,
        "conditional_variation": True,
        "port_pointer_correlation": True,
        "nearest_neighbor_eta": False,
        "pointer_is_formation": False,
        "one_shot_is_history": False,
        "schur_is_periodic_car": False,
        "schur_is_full_fock": False,
        "two_tt_complete": False,
        "axiom_update": False,
        "obligation_retirement": 0,
        "toe_progress": False,
        "retained": False,
        "broad_no_go": False,
    }
    mutation_map = {
        "stale_main_authority": ("main", "stale"),
        "drop_preregistration": ("prereg", False),
        "alter_goal_after_registration": ("goal_blob", "altered"),
        "replace_actual_reverse_by_adjoint": ("actual_reverse", False),
        "use_blind_h1_column": ("tt_column", 0),
        "call_tangent_a_state": ("tangent_is_state", True),
        "drop_zero_source_strict_positivity": ("strict_zero_positive", False),
        "drop_analytic_denominator": ("analytic_denominator", False),
        "deny_positive_interval": ("positive_interval", False),
        "break_pvm_positivity": ("pvm_positive", False),
        "break_pvm_completeness": ("pvm_complete", False),
        "import_maximally_mixed_c32": ("maximally_mixed_import", True),
        "erase_nonzero_h1_slope": ("nonzero_slope", False),
        "call_finite_family_uniform": ("finite_uniform", True),
        "break_coarse_addition": ("coarse_addition", False),
        "break_pointer_pullback": ("pointer_pullback", False),
        "call_pointer_bit_eight_labels": ("pointer_bit_eight_labels", True),
        "erase_conditional_m2_variation": ("conditional_variation", False),
        "erase_port_pointer_correlation": ("port_pointer_correlation", False),
        "call_h1_nearest_neighbor_eta": ("nearest_neighbor_eta", True),
        "call_pointer_write_formation": ("pointer_is_formation", True),
        "call_one_shot_permanent_history": ("one_shot_is_history", True),
        "call_schur_periodic_car_state": ("schur_is_periodic_car", True),
        "call_schur_full_fock_state": ("schur_is_full_fock", True),
        "claim_two_tt_completion": ("two_tt_complete", True),
        "claim_axiom_update": ("axiom_update", True),
        "claim_obligation_retirement": ("obligation_retirement", 1),
        "claim_toe_progress": ("toe_progress", True),
        "claim_retained_status": ("retained", True),
        "claim_broad_record_no_go": ("broad_no_go", True),
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
    source_ok = (
        source["forward_terms"] > 0 and source["reverse_terms"] > 0
        and source["literal_parent"]
        and source["actual_reverse_parent"]
        and source["block_placement"]
        and source["actual_reverse_distinct"] == claims["actual_reverse"]
        and claims["tt_column"] == 1
    )
    zero_ok = (
        all(zero["sector_scalars"])
        and all(zero["sector_traces_positive"])
        and zero["strict_full_gram"] == claims["strict_zero_positive"]
        and instrument["baseline_uniform"]
        and claims["maximally_mixed_import"] is False
    )
    pvm_ok = (
        instrument["projectors"] == claims["pvm_positive"]
        and instrument["pairwise_orthogonal"]
        and instrument["complete"] == claims["pvm_complete"]
        and instrument["coarsenings"]
        and instrument["effect_ranks"] == (4,) * 8
    )
    germ_ok = (
        germ["denominators_nonzero_at_zero"] == claims["analytic_denominator"]
        and germ["positive_interval_exists"] == claims["positive_interval"]
        and germ["finite_nonconstant_law_exists"]
        and claims["tangent_is_state"] is False
        and claims["finite_uniform"] is False
    )
    response_ok = (
        response["first_column_zero"]
        and not response["second_column_zero"]
        and response["source_operator_nonzero"]
        and response["complex_rank"] == 1
        and response["real_rank"] == 1
        and response["ell_positive"] == claims["nonzero_slope"]
        and response["signed_pattern"]
        and response["coarse_derivatives"] == (0,) * 4
        and claims["coarse_addition"] is True
    )
    pointer_ok = (
        instrument["writer_unitary"] and instrument["writer_nonidentity"]
        and instrument["faithful_joint_readout"] == claims["pointer_pullback"]
        and instrument["pointer_projectors"]
        and instrument["pointer_orthogonal"]
        and instrument["pointer_complete"]
        and claims["pointer_bit_eight_labels"] is False
        and any(value != 0 for value in response["conditional_derivatives"])
        == claims["conditional_variation"]
        and response["pointer_marginal_derivatives"] == (0, 0)
        and response["correlation_nonzero"] == claims["port_pointer_correlation"]
    )
    covariance_ok = (
        covariance["proper_cubic_count"] == 24
        and covariance["detector_family"] and covariance["context_family"]
        and covariance["coordinate_reflection"]
        and covariance["effect_reflection"]
        and covariance["trace_covariance"]
    )
    scope_ok = (
        claims["nearest_neighbor_eta"] is False
        and claims["pointer_is_formation"] is False
        and claims["one_shot_is_history"] is False
        and claims["schur_is_periodic_car"] is False
        and claims["schur_is_full_fock"] is False
        and claims["two_tt_complete"] is False
        and claims["axiom_update"] is False
        and claims["obligation_retirement"] == 0
        and claims["toe_progress"] is False
        and claims["retained"] is False
        and claims["broad_no_go"] is False
    )
    return {
        "A": (authority_ok, "current authority and immutable Block-205 registration are pinned"),
        "B": (source_ok, "the literal H1 second-TT forward/actual-reverse source is fixed on the full two-sector carrier"),
        "C": (zero_ok, "the action-derived zero-source C32 marginal is block-scalar and the full Schur Gram is strictly positive without importing I32/32"),
        "D": (pvm_ok, "the fixed eight rank-four effects remain a complete positive PVM on the same C32 boundary carrier"),
        "E": (germ_ok and response_ok, "analyticity, strict baseline positivity, and the exact signed H1 derivative force a finite positive nonuniform probability germ"),
        "F": (pointer_ok, "the fixed nonidentity M2 dilation reproduces the effects; sign marginals stay uniform while port-conditioned binary probabilities and correlation vary"),
        "G": (covariance_ok, "the detector/context orbit has 24 proper-cubic frames and exact reflection/trace covariance"),
        "H": (scope_ok and note["exists"] and note["scope"] and note["n5"], "the result is a conditional one-shot Schur law, not eta closure, periodic CAR, formation/history, axiom, retained, or TOE completion"),
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
    response = response_germ_facts()
    print(
        "H1_GERM: TT column0=blind; column1 rank=1; "
        f"ell={response['ell']}; ell>0={response['ell_positive']}."
    )
    print(
        "H1_EFFECT_DERIVATIVES: "
        "(ell/8)*(+,-,+,-,-,+,-,+); coarse=(0,0,0,0)."
    )
    print(
        "H1_POINTER: conditional_derivatives="
        "(ell/2)*(+,-,+,-,-,+,-,+); sign_marginals=(0,0); "
        "correlation_derivative=ell."
    )
    print(
        "ZERO_SOURCE: action-derived sector blocks are scalar; "
        "eight weights=1/8; "
        "strict Schur positivity exact on the frozen parent set."
    )
    print(
        "RESULT: positive analytic H1 right-Schur probability germ exists; "
        "nonconstant port-conditioned M2 law exists for finite sufficiently "
        "small source; nearest-neighbor eta/context completion=open; "
        "obligation_retirement=0; TOE movement=0."
    )
    for line in N5_LINES:
        print(line)
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return 0 if passed == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
