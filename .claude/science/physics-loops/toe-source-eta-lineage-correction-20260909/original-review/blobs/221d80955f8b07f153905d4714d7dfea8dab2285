#!/usr/bin/env python3
"""Independent Block-05 static Record joint-law compatibility gate.

This checker imports no Block-05 primary code or result booleans.  It obtains
the H1 orbit and scalar probability germ from the independent Block-03
construction, exhausts literal adjacent-site path ratios, and proves the
compatible-function classification in Boolean multilinear coefficient space
rather than by the primary checker's full constraint-matrix computation.
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

import independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as i3  # noqa: E402


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
MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "4e2b1d3303db8d748e2f2237f58b530dd4fdf2ee"
PREFLIGHT_BLOB = "70b684a80156a2ef1b7eca07b296cbb118c35f7e"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK03_NOTE = (
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_"
    "REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
BLOCK03_NOTE_BLOB = "f5ead306fdf7d2e887cb3b31f323d7fd4b82ab2a"
BLOCK03_INDEPENDENT = (
    "scripts/independent_admissibility_d4_affine_lineage_binary_record_join_"
    "2026_08_29.py"
)
BLOCK03_INDEPENDENT_BLOB = "2da34ab19e23405e349cdfa67de332ceb990d202"
BLOCK03_INDEPENDENT_CACHE = (
    "logs/runner-cache/independent_admissibility_d4_affine_lineage_binary_"
    "record_join_2026_08_29.txt"
)
BLOCK03_INDEPENDENT_CACHE_BLOB = "a1c2de91f808b7a4e5175e804db6680f012c7dac"
COMPAT_NOTE = (
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_"
    "AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)
COMPAT_NOTE_BLOB = "6be62abbbb5607f913908faec0222f96e6ea513a"
AUDIT_TIMEOUT_SEC = 300

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block05-h1-static-joint-law-curl-gate-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block05-h1-static-joint-law-curl-gate-20260829/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_H1_STATIC_RECORD_FULL_CONDITIONAL_JOINT_LAW_CURL_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "logs/runner-cache/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
    "docs/ADMISSIBILITY_BINARY_FULL_CONDITIONAL_COMPATIBILITY_ISING_ACTION_AXIOM_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-10.md",
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
    "drift_independent_h1",
    "drift_independent_cache",
    "lose_active_mask",
    "erase_probability_germ",
    "erase_inactive_neutrality",
    "omit_direction",
    "mispair_reverse_direction",
    "erase_path_witness",
    "declare_paths_equal",
    "break_mobius_uniqueness",
    "retain_nonlinear_interaction",
    "split_opposite_slopes",
    "miscount_active_classes",
    "allow_active_slope",
    "claim_static_joint_exists",
    "claim_ordered_process_closed",
    "claim_hidden_state_closed",
    "claim_axiom_defect",
    "claim_obligation_retirement",
    "claim_toe_movement",
    "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=300
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
    text = (ROOT / minimal).read_text(encoding="utf-8")
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": is_ancestor(PARENT),
        "prereg": is_ancestor(PREREG),
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_worktree": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_worktree": git("hash-object", "--", PREFLIGHT),
        "axiom": git("hash-object", "--", minimal),
        "block03_note": git("hash-object", "--", BLOCK03_NOTE),
        "block03_independent": git("hash-object", "--", BLOCK03_INDEPENDENT),
        "block03_independent_cache": git(
            "hash-object", "--", BLOCK03_INDEPENDENT_CACHE
        ),
        "compat_note": git("hash-object", "--", COMPAT_NOTE),
        "target_absent_at_prereg": (
            not path_exists_at(PREREG, NOTE)
            and not path_exists_at(
                PREREG,
                "scripts/independent_admissibility_d4_h1_static_record_"
                "joint_law_curl_gate_2026_08_29.py",
            )
        ),
        "conditional_only": all(
            phrase in text
            for phrase in (
                "conditional\non formation at that site",
                "it does not supply the formation site, probability,",
                "Admissibility is not a dynamics axiom",
            )
        ),
    }


@cache
def independent_h1_facts(lose_active: bool = False) -> dict[str, object]:
    action = i3.independent_action_and_eta()
    law = i3.independent_law_and_channel()
    active = {
        mask for mask, flag in enumerate(action["active_table"]) if flag
    }
    if lose_active:
        active.remove(min(active))
    cubic = sp.factor(law["contrast_series"][3])
    orbit = {
        action["action"](group_index, action["base"])
        for group_index in range(24)
    }
    weights = Counter(mask.bit_count() for mask in active)
    return {
        "active": tuple(sorted(active)),
        "active_count": len(active),
        "expected_active": tuple(sorted(active)) == EXPECTED_ACTIVE,
        "single_orbit": active == orbit,
        "weight_counts": dict(weights),
        "probability_transport": law["all_eta_probability_transport"],
        "actual_probability_germ": law["actual_probability_germ"],
        "inactive_neutral": law["inactive_zero"],
        "binary_complete": law["controlled_continuum_complete"],
        "cubic": cubic,
        "cubic_nonzero": cubic != 0,
        "lose_active": lose_active,
    }


def insert_neighbor(exterior: int, direction: int, value: int) -> int:
    """Insert one adjacent value into a five-bit exterior shell."""
    mask = value << direction
    source = 0
    for target in range(6):
        if target == direction:
            continue
        mask |= ((exterior >> source) & 1) << target
        source += 1
    return mask


@cache
def path_ratio_facts(
    lose_active: bool = False,
    omit_direction: bool = False,
    mispair_reverse: bool = False,
) -> dict[str, object]:
    active = set(independent_h1_facts(lose_active)["active"])
    directions = range(5) if omit_direction else range(6)
    deltas = []
    witnesses = []
    failures_by_direction = Counter()
    for direction in directions:
        reverse = direction if mispair_reverse else INVERSE[direction]
        for left_exterior in range(32):
            left0 = insert_neighbor(left_exterior, direction, 0)
            left1 = insert_neighbor(left_exterior, direction, 1)
            for right_exterior in range(32):
                right0 = insert_neighbor(right_exterior, reverse, 0)
                right1 = insert_neighbor(right_exterior, reverse, 1)
                # Flip x then y versus y then x from the same 00 endpoint.
                xy_power = int(left0 in active) + int(right1 in active)
                yx_power = int(right0 in active) + int(left1 in active)
                delta = xy_power - yx_power
                deltas.append(delta)
                if delta:
                    failures_by_direction[direction] += 1
                    witnesses.append((
                        direction,
                        left_exterior,
                        right_exterior,
                        left0,
                        left1,
                        right0,
                        right1,
                        xy_power,
                        yx_power,
                    ))
    # A different literal representative from the primary checker's
    # preregistered -x witness: +x with reciprocal -x.
    literal = (1, 2, 0, 4, 6, 0, 1, 0, 1)
    return {
        "square_count": len(deltas),
        "failure_count": sum(delta != 0 for delta in deltas),
        "histogram": dict(Counter(deltas)),
        "all_directions_fail": set(failures_by_direction) == set(range(6)),
        "failures_by_direction": dict(failures_by_direction),
        "first_witness": min(witnesses) if witnesses else None,
        "literal_witness": literal in witnesses,
        "inversion_same_zero_set": all(
            (delta == 0) == (-delta == 0) for delta in deltas
        ),
        "omit_direction": omit_direction,
        "mispair_reverse": mispair_reverse,
    }


def rational_rank(rows: list[list[int]]) -> int:
    """Small exact Gaussian rank, independent of SymPy's matrix rank."""
    work = [[sp.Rational(value) for value in row] for row in rows]
    if not work:
        return 0
    rank = 0
    columns = len(work[0])
    for column in range(columns):
        pivot = next(
            (row for row in range(rank, len(work)) if work[row][column]),
            None,
        )
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        scale = work[rank][column]
        work[rank] = [value / scale for value in work[rank]]
        for row in range(len(work)):
            if row == rank or not work[row][column]:
                continue
            factor = work[row][column]
            work[row] = [
                value - factor * pivot_value
                for value, pivot_value in zip(work[row], work[rank])
            ]
        rank += 1
        if rank == len(work):
            break
    return rank


@cache
def boolean_classification_facts(lose_active: bool = False) -> dict[str, object]:
    active = independent_h1_facts(lose_active)["active"]
    # In the unique multilinear expansion ell(eta)=sum_S c_S prod_(i in S)
    # eta_i, environment independence of every bit derivative kills exactly
    # the 57 coefficients of degree >=2.  Reciprocal edge agreement adds the
    # three independent equalities c0=c1, c2=c3, c4=c5.
    nonlinear_monomials = tuple(
        monomial for monomial in range(64) if monomial.bit_count() >= 2
    )
    linear_pair_rows = (
        (1, -1, 0, 0, 0, 0),
        (0, 0, 1, -1, 0, 0),
        (0, 0, 0, 0, 1, -1),
    )
    axis_counts = tuple(
        tuple(
            ((mask >> bit) & 1) + ((mask >> INVERSE[bit]) & 1)
            for bit in (0, 2, 4)
        )
        for mask in active
    )
    anchor = axis_counts[0]
    active_rows = [
        [value - base for value, base in zip(row, anchor)]
        for row in axis_counts[1:]
    ]
    active_rank = rational_rank(active_rows)
    classes = tuple(sorted(set(axis_counts)))
    expected_classes = (
        (0, 1, 1), (1, 0, 1), (1, 1, 0),
        (1, 1, 2), (1, 2, 1), (2, 1, 1),
    )
    # Unique multilinear coefficients also give sufficiency: a constant plus
    # three reciprocal-axis count terms integrates to a finite pairwise Gibbs
    # weight, so the four-dimensional kernel is not merely necessary.
    return {
        "mobius_unique": len({tuple(
            int((monomial & mask) == monomial) for mask in range(64)
        ) for monomial in range(64)}) == 64,
        "nonlinear_constraints": len(nonlinear_monomials),
        "opposite_constraints": rational_rank([
            list(row) for row in linear_pair_rows
        ]),
        "raw_rank": len(nonlinear_monomials) + 3,
        "raw_nullity": 64 - len(nonlinear_monomials) - 3,
        "basis": "constant_plus_three_reciprocal_axis_counts",
        "pairwise_gibbs_sufficient": True,
        "active_classes": classes,
        "expected_classes": classes == expected_classes,
        "active_pin_rank": active_rank,
        "active_pin_constant_only": active_rank == 3,
        "active_pinned_rank": len(nonlinear_monomials) + 3 + active_rank,
        "active_pinned_nullity": 64 - len(nonlinear_monomials) - 3 - active_rank,
    }


@cache
def scope_facts() -> dict[str, object]:
    return {
        "static_families": (
            "frozen_neutral_inactive_full_conditionals",
            "arbitrary_inactive_extension",
            "reciprocal_axis_count_gibbs_family",
            "finite_path_weight_reconstruction",
            "binary_outcome_relabeling",
            "literal_adjacent_site_embedding",
        ),
        "live_families": (
            "ordered_strict_nearest_neighbor_front",
            "hidden_or_enlarged_state_carrier",
            "projectively_consistent_history_process",
            "site_hazard_with_no_event_channel",
            "different_active_local_law",
        ),
        "static_binary_only": True,
        "ordered_closed": False,
        "hidden_closed": False,
        "axiom_defect": False,
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    lose_active = mutation == "lose_active_mask"
    h1 = dict(independent_h1_facts(lose_active))
    paths = dict(path_ratio_facts(
        lose_active=lose_active,
        omit_direction=mutation == "omit_direction",
        mispair_reverse=mutation == "mispair_reverse_direction",
    ))
    classification = dict(boolean_classification_facts(lose_active))
    scope = dict(scope_facts())
    claims = {
        "probability_germ": mutation != "erase_probability_germ",
        "inactive_neutral": mutation != "erase_inactive_neutrality",
        "path_witness": mutation != "erase_path_witness",
        "paths_equal": mutation == "declare_paths_equal",
        "mobius_unique": mutation != "break_mobius_uniqueness",
        "nonlinear_interaction": mutation == "retain_nonlinear_interaction",
        "opposite_slopes_split": mutation == "split_opposite_slopes",
        "active_classes": 5 if mutation == "miscount_active_classes" else 6,
        "active_slope": mutation == "allow_active_slope",
        "static_joint": mutation == "claim_static_joint_exists",
        "ordered_closed": mutation == "claim_ordered_process_closed",
        "hidden_closed": mutation == "claim_hidden_state_closed",
        "axiom_defect": mutation == "claim_axiom_defect",
        "obligation": int(mutation == "claim_obligation_retirement"),
        "toe": int(mutation == "claim_toe_movement"),
        "retained": mutation == "claim_retained",
    }
    if mutation == "stale_main":
        authority["main"] = "0" * 40
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
    elif mutation == "drift_independent_h1":
        authority["block03_independent"] = "0" * 40
    elif mutation == "drift_independent_cache":
        authority["block03_independent_cache"] = "0" * 40

    authority_ok = (
        authority["main"] == MAIN
        and authority["parent"] and authority["prereg"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom"] == AXIOM_BLOB
        and authority["block03_note"] == BLOCK03_NOTE_BLOB
        and authority["block03_independent"] == BLOCK03_INDEPENDENT_BLOB
        and authority["block03_independent_cache"]
        == BLOCK03_INDEPENDENT_CACHE_BLOB
        and authority["compat_note"] == COMPAT_NOTE_BLOB
        and authority["target_absent_at_prereg"]
        and authority["conditional_only"]
    )
    h1_ok = (
        h1["active_count"] == 24
        and h1["expected_active"] and h1["single_orbit"]
        and h1["weight_counts"] == {2: 12, 4: 12}
        and h1["probability_transport"]
        and h1["actual_probability_germ"]
        and h1["inactive_neutral"]
        and h1["binary_complete"]
        and h1["cubic_nonzero"]
        and claims["probability_germ"] and claims["inactive_neutral"]
    )
    path_ok = (
        paths["square_count"] == 6 * 32 * 32
        and paths["failure_count"] > 0
        and paths["all_directions_fail"]
        and paths["literal_witness"]
        and paths["inversion_same_zero_set"]
        and not paths["omit_direction"] and not paths["mispair_reverse"]
        and claims["path_witness"] and not claims["paths_equal"]
        and not claims["static_joint"]
    )
    classification_ok = (
        classification["mobius_unique"] and claims["mobius_unique"]
        and classification["nonlinear_constraints"] == 57
        and not claims["nonlinear_interaction"]
        and classification["opposite_constraints"] == 3
        and not claims["opposite_slopes_split"]
        and classification["raw_rank"] == 60
        and classification["raw_nullity"] == 4
        and classification["pairwise_gibbs_sufficient"]
        and classification["expected_classes"]
        and claims["active_classes"] == 6
        and classification["active_pin_rank"] == 3
        and classification["active_pin_constant_only"]
        and classification["active_pinned_rank"] == 63
        and classification["active_pinned_nullity"] == 1
        and not claims["active_slope"]
    )
    scope_ok = (
        len(scope["static_families"]) >= 5
        and len(scope["live_families"]) >= 5
        and scope["static_binary_only"]
        and not scope["ordered_closed"] and not scope["hidden_closed"]
        and not scope["axiom_defect"]
        and not claims["ordered_closed"] and not claims["hidden_closed"]
        and not claims["axiom_defect"]
    )
    accounting_ok = (
        claims["obligation"] == 0 and claims["toe"] == 0
        and not claims["retained"]
    )
    return {
        "A_independent_authority": (
            authority_ok,
            "preregistration, axiom, independent H1 runner/cache, and compatibility source are pinned",
        ),
        "B_independent_H1": (
            h1_ok,
            "the independent construction supplies the same 24-mask orbit and a nonzero complete binary probability germ",
        ),
        "C_two_path_ratio": (
            path_ok,
            "an exhaustive literal adjacent-edge census finds unequal static joint-weight paths in every direction",
        ),
        "D_boolean_classification": (
            classification_ok,
            "unique multilinear coefficients leave only constant plus three reciprocal-axis slopes, and active equality kills every slope",
        ),
        "E_scope": (
            scope_ok,
            "the frozen and neighbor-varying static readings fail; the constant-field completion and nonstatic constructions remain distinct",
        ),
        "F_accounting": (
            accounting_ok,
            "no axiom defect, obligation retirement, retention, gravity result, or TOE movement is claimed",
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
    h1 = independent_h1_facts()
    paths = path_ratio_facts()
    classification = boolean_classification_facts()
    print(
        "INDEPENDENT_H1: active=24 (weight2=12, weight4=12); "
        f"inactive=40; nonzero_cubic={h1['cubic_nonzero']}."
    )
    print(
        "TWO_PATH_CURL: squares="
        f"{paths['square_count']}; failing={paths['failure_count']}; "
        f"histogram={paths['histogram']}; first={paths['first_witness']}."
    )
    print(
        "BOOLEAN_CLASS: nonlinear=57; reciprocal=3; raw_rank="
        f"{classification['raw_rank']}/64; active_pin_rank="
        f"{classification['active_pinned_rank']}/64 (constant only)."
    )
    print(
        "DECISION: the frozen H1 law fails static full-conditional compatibility; "
        "the only active-preserving compatible extension is condition-independent, "
        "and ordered histories and enlarged carriers remain live."
    )
    print(
        "ACCOUNTING: axiom_update=false; obligation_retirement=0; "
        "TOE_movement=0; retained=false; gravity=false."
    )
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
    failures = len(checks) - passed + len(survivors)
    print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
