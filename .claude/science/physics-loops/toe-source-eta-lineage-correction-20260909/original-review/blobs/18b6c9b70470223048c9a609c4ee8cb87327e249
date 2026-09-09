#!/usr/bin/env python3
"""Exact Block-05 H1 static Record joint-law square-curl gate.

The checker joins the pinned Source/Eta Block-03 scalar H1 probability germ
to the finite binary full-conditional compatibility criterion.  It tests the
static binary Record-measure reading only; ordered processes and enlarged
state carriers remain outside the negative claim.
"""

from __future__ import annotations

import argparse
from collections import Counter
from functools import cache
from pathlib import Path
import subprocess
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block05-h1-static-joint-law-curl-gate-20260829"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_"
    "CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PREREG = "e188f12b2a75dddf755d6d11f31de134b8464c6b"
PARENT = "9097902138f1e33d322057e6501e71f255fa7a8f"
BLOCK04_RESULT = "54032f5737367851f3d84c7ce2ec27f7399ebf2e"
BLOCK03_RESULT = "d8cc11fb5210321cf081866572b90a6ce290edcf"
CURRENT_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "4e2b1d3303db8d748e2f2237f58b530dd4fdf2ee"
PREFLIGHT_BLOB = "70b684a80156a2ef1b7eca07b296cbb118c35f7e"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK03_NOTE = (
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_"
    "REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
BLOCK03_NOTE_BLOB = "f5ead306fdf7d2e887cb3b31f323d7fd4b82ab2a"
BLOCK03_RUNNER = (
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py"
)
BLOCK03_RUNNER_BLOB = "0f29ff74b3816a15847aea104f3faa44d6a0ea4f"
COMPAT_NOTE = (
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
COMPAT_NOTE_BLOB = "6be62abbbb5607f913908faec0222f96e6ea513a"
COMPAT_RUNNER = (
    "scripts/admissibility_binary_full_conditional_compatibility_ising_action_"
    "axiom_boundary_2026_08_10.py"
)
COMPAT_RUNNER_BLOB = "ee92aa2a71bee6f59854ee6e2cea3b90058b1a28"
FRONT_NOTE = (
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_"
    "HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md"
)
FRONT_NOTE_BLOB = "494ed4d1be589e7f2a37cf79f65997504de4579c"
ATTACHMENT_NOTE = (
    "docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_"
    "BOUNDED_THEOREM_NOTE_2026-08-12.md"
)
ATTACHMENT_NOTE_BLOB = "6bcca990308cacc2ec32c3c7a8547089cb8bc133"
AUDIT_TIMEOUT_SEC = 300

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block05-h1-static-joint-law-curl-gate-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block05-h1-static-joint-law-curl-gate-20260829/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "scripts/admissibility_binary_full_conditional_compatibility_ising_action_axiom_boundary_2026_08_10.py",
    "docs/ADMISSIBILITY_STRICT_NEAREST_NEIGHBOR_STATE_DEPENDENT_RECORD_BORN_HISTORY_SINGLE_FRONT_POSITIVE_THEOREM_NOTE_2026-08-12.md",
    "docs/ADMISSIBILITY_PHYSICAL_STATE_TO_RECORD_ATTACHMENT_SELECTION_CUT_BOUNDED_THEOREM_NOTE_2026-08-12.md",
)

INVERSE = (1, 0, 3, 2, 5, 4)
EXPECTED_ACTIVE = (
    5, 6, 9, 10, 17, 18, 20, 23, 24, 27, 29, 30,
    33, 34, 36, 39, 40, 43, 45, 46, 53, 54, 57, 58,
)

MUTATIONS = (
    "stale_main",
    "drop_parent",
    "drop_prereg",
    "drift_goal",
    "drift_preflight",
    "drift_axiom",
    "replace_active_orbit",
    "erase_probability_transport",
    "erase_cubic_germ",
    "call_cubic_zero",
    "make_inactive_nonneutral",
    "wrong_inverse_pairing",
    "skip_edge_contexts",
    "erase_square_witness",
    "claim_odds_inversion_repairs",
    "lower_compatibility_rank",
    "allow_varying_compatible_extension",
    "erase_weight_two",
    "erase_weight_four",
    "claim_static_joint_exists",
    "claim_ordered_process_closed",
    "claim_hidden_state_closed",
    "claim_axiom_defect",
    "claim_obligation_retirement",
    "claim_toe_movement",
    "claim_retained",
    "claim_gravity",
)

N5_LINES = (
    "per_element: checked every active and inactive six-bit condition, both branch-odds conventions, and the exact nonzero cubic response coefficient.",
    "per_site: checked one binary target conditional and a literal adjacent-site square with ten independently supplied exterior Record bits.",
    "per_mode: checked and not executed — no momentum, spectral, temporal, or continuum mode enters this finite static full-conditional theorem.",
    "per_block: checked all 64 masks, all six oriented neighbor bits, 6,144 endpoint-environment squares, and the complete compatible log-odds kernel.",
    "lattice_wide: checked finite positive static binary joint-law compatibility; ordered histories, hidden states, formation dynamics, and infinite-volume phases were not executed.",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=120
    ).strip()


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
    ).returncode == 0


def path_exists_at(commit: str, path: str) -> bool:
    return subprocess.run(
        ("git", "cat-file", "-e", f"{commit}:{path}"),
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


@cache
def authority_facts() -> dict[str, object]:
    minimal = "docs/MINIMAL_AXIOMS_2026-06-29.md"
    minimal_text = (ROOT / minimal).read_text(encoding="utf-8")
    return {
        "origin_main": git("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT),
        "prereg": is_ancestor(PREREG),
        "block04": is_ancestor(BLOCK04_RESULT),
        "block03": is_ancestor(BLOCK03_RESULT),
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_worktree": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_worktree": git("hash-object", "--", PREFLIGHT),
        "axiom": git("hash-object", "--", minimal),
        "block03_note": git("hash-object", "--", BLOCK03_NOTE),
        "block03_runner": git("hash-object", "--", BLOCK03_RUNNER),
        "compat_note": git("hash-object", "--", COMPAT_NOTE),
        "compat_runner": git("hash-object", "--", COMPAT_RUNNER),
        "front_note": git("hash-object", "--", FRONT_NOTE),
        "attachment_note": git("hash-object", "--", ATTACHMENT_NOTE),
        "target_runner_absent_at_prereg": not path_exists_at(
            PREREG,
            "scripts/admissibility_d4_h1_static_record_joint_law_curl_gate_2026_08_29.py",
        ),
        "target_note_absent_at_prereg": not path_exists_at(PREREG, NOTE),
        "axiom_variation_needle": (
            "determined by, and varies with, the nearest-neighbor conditions"
            in minimal_text
        ),
        "axiom_process_boundary": all(
            needle in minimal_text
            for needle in (
                "it does not supply the formation site, probability,",
                "or rate",
                "Admissibility is not a dynamics axiom",
            )
        ),
    }


def mask_with_bit(rest: int, bit: int, value: int) -> int:
    mask = value << bit
    cursor = 0
    for target in range(6):
        if target == bit:
            continue
        mask |= ((rest >> cursor) & 1) << target
        cursor += 1
    return mask


@cache
def h1_scalar_germ_facts(replace_active: bool = False) -> dict[str, object]:
    decoder = b3.decoder_facts()
    action_data = b3.action_facts()
    lift = b3.operator_lift_facts()
    active = set(decoder["transport"])
    if replace_active:
        active.symmetric_difference_update({0, 5})
    base = decoder["base_mask"]
    orbit = {
        action_data["action"](group_index, base)
        for group_index in range(24)
    }
    weights = Counter(mask.bit_count() for mask in active)
    series = lift["contrast_series"]
    kappa = sp.factor(series[3])
    e, u = sp.symbols("e u", real=True)
    active_odds_truncation = sp.series(
        (1 - u * kappa * e**3) / (1 + u * kappa * e**3),
        e,
        0,
        4,
    ).removeO()
    inverse_odds_truncation = sp.series(
        (1 + u * kappa * e**3) / (1 - u * kappa * e**3),
        e,
        0,
        4,
    ).removeO()
    return {
        "active": tuple(sorted(active)),
        "active_count": len(active),
        "expected_active": tuple(sorted(active)) == EXPECTED_ACTIVE,
        "active_is_one_orbit": active == orbit,
        "weight_counts": dict(weights),
        "probability_transport": lift["all_eta_probability_transport"],
        "writer_covariance": lift["proper_cubic_writer_intertwiner"],
        "inactive_neutral": lift["inactive_zero_effect_direction"],
        "strict_positive_normalized": lift[
            "all_eta_positive_on_interval"
        ],
        "series": series,
        "kappa": kappa,
        "kappa_positive": bool(kappa > 0),
        "active_odds_truncation": sp.expand(active_odds_truncation),
        "inverse_odds_truncation": sp.expand(inverse_odds_truncation),
        "odds_cubic": sp.expand(active_odds_truncation).coeff(e, 3),
        "inverse_odds_cubic": sp.expand(inverse_odds_truncation).coeff(e, 3),
        "odds_cubic_expected": sp.simplify(
            sp.expand(active_odds_truncation).coeff(e, 3) + 2 * u * kappa
        ) == 0,
        "inverse_cubic_expected": sp.simplify(
            sp.expand(inverse_odds_truncation).coeff(e, 3) - 2 * u * kappa
        ) == 0,
        "active_scalar_common": (
            active == orbit
            and lift["all_eta_probability_transport"]
            and lift["proper_cubic_writer_intertwiner"]
        ),
        "replace_active": replace_active,
    }


@cache
def square_curl_facts(
    replace_active: bool = False,
    wrong_inverse: bool = False,
) -> dict[str, object]:
    active = set(h1_scalar_germ_facts(replace_active)["active"])
    inverse = tuple(range(6)) if wrong_inverse else INVERSE
    rows = []
    direction_failures = Counter()
    witnesses = []
    for direction in range(6):
        reverse = inverse[direction]
        for left_rest in range(32):
            x0 = mask_with_bit(left_rest, direction, 0)
            x1 = mask_with_bit(left_rest, direction, 1)
            for right_rest in range(32):
                y0 = mask_with_bit(right_rest, reverse, 0)
                y1 = mask_with_bit(right_rest, reverse, 1)
                left_power = int(x0 in active) + int(y1 in active)
                right_power = int(y0 in active) + int(x1 in active)
                delta = left_power - right_power
                rows.append(delta)
                if delta:
                    direction_failures[direction] += 1
                    witnesses.append(
                        (
                            direction,
                            left_rest,
                            right_rest,
                            x0,
                            x1,
                            y0,
                            y1,
                            left_power,
                            right_power,
                        )
                    )
    literal_witness = (0, 2, 0, 4, 5, 0, 2, 0, 1)
    reverse_deltas = tuple(-delta for delta in rows)
    return {
        "square_count": len(rows),
        "failing_count": sum(bool(delta) for delta in rows),
        "delta_counts": dict(Counter(rows)),
        "direction_failures": dict(direction_failures),
        "all_directions_fail": set(direction_failures) == set(range(6)),
        "first_witness": min(witnesses) if witnesses else None,
        "literal_witness_present": literal_witness in witnesses,
        "odds_inversion_preserves_failures": all(
            (delta == 0) == (reverse == 0)
            for delta, reverse in zip(rows, reverse_deltas)
        ),
        "wrong_inverse": wrong_inverse,
    }


def delta_row(bit: int, rest: int) -> list[int]:
    row = [0] * 64
    row[mask_with_bit(rest, bit, 1)] += 1
    row[mask_with_bit(rest, bit, 0)] -= 1
    return row


def subtract_rows(left: list[int], right: list[int]) -> list[int]:
    return [a - b for a, b in zip(left, right)]


@cache
def compatibility_class_facts(
    replace_active: bool = False,
) -> dict[str, object]:
    active = h1_scalar_germ_facts(replace_active)["active"]
    rows = []
    # Square curl with independent endpoint environments is equivalent to
    # each bit derivative being environment-independent and each edge's two
    # endpoint derivatives agreeing.
    for bit in range(6):
        reference = delta_row(bit, 0)
        for rest in range(1, 32):
            rows.append(subtract_rows(delta_row(bit, rest), reference))
    for bit in (0, 2, 4):
        rows.append(subtract_rows(delta_row(bit, 0), delta_row(INVERSE[bit], 0)))
    matrix = sp.Matrix(rows)
    raw_rank = matrix.rank()
    constant = sp.Matrix([1] * 64)
    axis_counts = tuple(sp.Matrix([
        ((mask >> bit) & 1) + ((mask >> INVERSE[bit]) & 1)
        for mask in range(64)
    ]) for bit in (0, 2, 4))
    expected_basis = (constant,) + axis_counts
    basis_kernel = all(matrix * vector == sp.zeros(matrix.rows, 1)
                       for vector in expected_basis)
    basis_independent = sp.Matrix.hstack(*expected_basis).rank() == 4

    pinned_rows = list(rows)
    anchor = active[0]
    for mask in active[1:]:
        row = [0] * 64
        row[mask] += 1
        row[anchor] -= 1
        pinned_rows.append(row)
    pinned_matrix = sp.Matrix(pinned_rows)
    pinned_rank = pinned_matrix.rank()
    pinned_constant_only = (
        pinned_rank == 63
        and pinned_matrix * constant == sp.zeros(pinned_matrix.rows, 1)
    )
    active_weight_two = tuple(mask for mask in active if mask.bit_count() == 2)
    active_weight_four = tuple(mask for mask in active if mask.bit_count() == 4)
    return {
        "constraint_rows": len(rows),
        "raw_rank": raw_rank,
        "raw_nullity": 64 - raw_rank,
        "expected_basis_kernel": basis_kernel,
        "expected_basis_independent": basis_independent,
        "pinned_rows": len(pinned_rows),
        "pinned_rank": pinned_rank,
        "pinned_nullity": 64 - pinned_rank,
        "pinned_constant_only": pinned_constant_only,
        "active_weight_two_count": len(active_weight_two),
        "active_weight_four_count": len(active_weight_four),
        "compatible_extension_varies": not pinned_constant_only,
        "replace_active": replace_active,
    }


@cache
def route_scope_facts() -> dict[str, object]:
    routes = (
        "frozen_neutral_inactive_static_conditionals",
        "arbitrary_inactive_extension_linear_classification",
        "geometric_count_odds_specialization",
        "finite_joint_weight_path_reconstruction",
        "output_relabel_or_inverse_odds",
        "literal_twelve_site_boundary_embedding",
    )
    live_outside_scope = (
        "ordered_strict_nearest_neighbor_record_front",
        "hidden_state_or_enlarged_carrier_joint_law",
        "projectively_consistent_history_process",
        "formation_hazard_or_participant_process",
        "replace_the_active_H1_candidate_law",
    )
    return {
        "attempted_static_routes": routes,
        "attempted_static_route_count": len(routes),
        "live_outside_scope": live_outside_scope,
        "live_outside_scope_count": len(live_outside_scope),
        "static_binary_only": True,
        "ordered_process_closed": False,
        "hidden_state_closed": False,
        "axiom_defect": False,
        "gravity_result": False,
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    replace_active = mutation == "replace_active_orbit"
    h1 = dict(h1_scalar_germ_facts(replace_active))
    square = dict(square_curl_facts(
        replace_active,
        mutation == "wrong_inverse_pairing",
    ))
    compatible = dict(compatibility_class_facts(replace_active))
    routes = dict(route_scope_facts())
    claims = {
        "probability_transport": mutation != "erase_probability_transport",
        "cubic_germ": mutation != "erase_cubic_germ",
        "cubic_zero": mutation == "call_cubic_zero",
        "inactive_neutral": mutation != "make_inactive_nonneutral",
        "all_edge_contexts": mutation != "skip_edge_contexts",
        "square_witness": mutation != "erase_square_witness",
        "odds_inversion_repairs": mutation == "claim_odds_inversion_repairs",
        "compatibility_rank": 59 if mutation == "lower_compatibility_rank" else 60,
        "varying_extension": mutation == "allow_varying_compatible_extension",
        "weight_two": mutation != "erase_weight_two",
        "weight_four": mutation != "erase_weight_four",
        "static_joint_exists": mutation == "claim_static_joint_exists",
        "ordered_process_closed": mutation == "claim_ordered_process_closed",
        "hidden_state_closed": mutation == "claim_hidden_state_closed",
        "axiom_defect": mutation == "claim_axiom_defect",
        "obligation": int(mutation == "claim_obligation_retirement"),
        "toe": int(mutation == "claim_toe_movement"),
        "retained": mutation == "claim_retained",
        "gravity": mutation == "claim_gravity",
    }
    if mutation == "stale_main":
        authority["origin_main"] = "0" * 40
    elif mutation == "drop_parent":
        authority["parent"] = False
    elif mutation == "drop_prereg":
        authority["prereg"] = False
    elif mutation == "drift_goal":
        authority["goal_worktree"] = "0" * 40
    elif mutation == "drift_preflight":
        authority["preflight_worktree"] = "0" * 40
    elif mutation == "drift_axiom":
        authority["axiom"] = "0" * 40

    authority_ok = (
        authority["origin_main"] == CURRENT_MAIN
        and authority["parent"] and authority["prereg"]
        and authority["block04"] and authority["block03"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom"] == AXIOM_BLOB
        and authority["block03_note"] == BLOCK03_NOTE_BLOB
        and authority["block03_runner"] == BLOCK03_RUNNER_BLOB
        and authority["compat_note"] == COMPAT_NOTE_BLOB
        and authority["compat_runner"] == COMPAT_RUNNER_BLOB
        and authority["front_note"] == FRONT_NOTE_BLOB
        and authority["attachment_note"] == ATTACHMENT_NOTE_BLOB
        and authority["target_runner_absent_at_prereg"]
        and authority["target_note_absent_at_prereg"]
        and authority["axiom_variation_needle"]
        and authority["axiom_process_boundary"]
    )
    h1_ok = (
        h1["expected_active"]
        and h1["active_count"] == 24
        and h1["active_is_one_orbit"]
        and h1["weight_counts"] == {2: 12, 4: 12}
        and h1["probability_transport"]
        and h1["writer_covariance"]
        and h1["inactive_neutral"]
        and h1["strict_positive_normalized"]
        and h1["series"][:3] == (0, 0, 0)
        and h1["kappa_positive"]
        and h1["odds_cubic_expected"]
        and h1["inverse_cubic_expected"]
        and h1["active_scalar_common"]
        and claims["probability_transport"]
        and claims["cubic_germ"]
        and not claims["cubic_zero"]
        and claims["inactive_neutral"]
    )
    square_ok = (
        square["square_count"] == 6 * 32 * 32
        and square["failing_count"] > 0
        and square["all_directions_fail"]
        and square["literal_witness_present"]
        and square["odds_inversion_preserves_failures"]
        and not square["wrong_inverse"]
        and claims["all_edge_contexts"]
        and claims["square_witness"]
        and not claims["odds_inversion_repairs"]
        and not claims["static_joint_exists"]
    )
    extension_ok = (
        compatible["constraint_rows"] == 6 * 31 + 3
        and compatible["raw_rank"] == 60
        and compatible["raw_nullity"] == 4
        and compatible["expected_basis_kernel"]
        and compatible["expected_basis_independent"]
        and compatible["pinned_rank"] == 63
        and compatible["pinned_nullity"] == 1
        and compatible["pinned_constant_only"]
        and compatible["active_weight_two_count"] == 12
        and compatible["active_weight_four_count"] == 12
        and not compatible["compatible_extension_varies"]
        and claims["compatibility_rank"] == 60
        and not claims["varying_extension"]
        and claims["weight_two"] and claims["weight_four"]
    )
    scope_ok = (
        routes["attempted_static_route_count"] >= 5
        and routes["live_outside_scope_count"] >= 5
        and routes["static_binary_only"]
        and not routes["ordered_process_closed"]
        and not routes["hidden_state_closed"]
        and not routes["axiom_defect"]
        and not routes["gravity_result"]
        and not claims["ordered_process_closed"]
        and not claims["hidden_state_closed"]
        and not claims["axiom_defect"]
        and not claims["gravity"]
    )
    accounting_ok = (
        claims["obligation"] == 0
        and claims["toe"] == 0
        and not claims["retained"]
    )
    return {
        "A_authority": (
            authority_ok,
            "preregistration and every frozen H1, compatibility, front, attachment, and axiom authority match",
        ),
        "B_H1_scalar_germ": (
            h1_ok,
            "the exact 24-mask orbit has one nontrivial cubic scalar odds germ while the frozen inactive extension is neutral",
        ),
        "C_static_square_curl": (
            square_ok,
            "the frozen H1 conditionals violate an exact adjacent-site odds square in every direction",
        ),
        "D_extension_classification": (
            extension_ok,
            "every compatible binary extension preserving the common active odds is constant and therefore not neighbor-varying",
        ),
        "E_scope": (
            scope_ok,
            "the frozen and neighbor-varying static readings fail; the constant-field completion and nonstatic processes are distinguished",
        ),
        "F_accounting": (
            accounting_ok,
            "no axiom defect, gravity result, obligation retirement, retention, or TOE movement is claimed",
        ),
    }


def mutation_sweep() -> tuple[int, tuple[str, ...]]:
    survivors = tuple(
        mutation for mutation in MUTATIONS
        if all(ok for ok, _message in evaluate(mutation).values())
    )
    return len(MUTATIONS) - len(survivors), survivors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--list-mutations", action="store_true")
    args = parser.parse_args()
    if args.list_mutations:
        print("\n".join(MUTATIONS))
        return 0

    checks = evaluate(args.mutation)
    passed = 0
    for name, (ok, message) in checks.items():
        print(f"PASS {name}: {message}" if ok else f"FAIL {name}: {message}")
        passed += int(ok)
    rejected, survivors = mutation_sweep()
    h1 = h1_scalar_germ_facts()
    square = square_curl_facts()
    compatible = compatibility_class_facts()
    witness = square["first_witness"]
    print(
        "H1_GERM: active=24 (weight2=12, weight4=12); inactive=40 neutral; "
        f"odds cubic coefficient={h1['odds_cubic']}."
    )
    print(
        "STATIC_CURL: squares="
        f"{square['square_count']}; failing={square['failing_count']}; "
        f"delta_counts={square['delta_counts']}; first_witness={witness}."
    )
    print(
        "COMPATIBLE_CLASS: raw_rank="
        f"{compatible['raw_rank']}/64 (nullity 4); active-pinned rank="
        f"{compatible['pinned_rank']}/64 (constant-only nullity 1)."
    )
    print(
        "DECISION: the frozen H1 law is not a static binary Record full-conditional law; "
        "the only active-preserving compatible extension is condition-independent, "
        "while ordered fronts, hidden states, projective histories, and hazards remain live."
    )
    print(
        "ACCOUNTING: axiom_update=false; obligation_retirement=0; "
        "TOE_movement=0; retained=false; gravity=false."
    )
    for line in N5_LINES:
        print(line)
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
    failures = len(checks) - passed + len(survivors)
    print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
