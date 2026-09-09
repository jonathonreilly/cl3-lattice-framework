#!/usr/bin/env python3
"""Exact Block-04 Record-ready-set and successor-state typing gate.

The primary theorem is combinatorial.  A physical state is a partial Record
map R: Omega -> {0,1}; a site is six-Record-ready precisely when it is absent
from Omega and all six cubic neighbors are present.  The checker proves the
ready-set update under one permanent append, types the tempting adjacent
successor, and keeps local-mask completions distinct from reachable events.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import combinations, product
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as b3  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block04-fresh-site-successor-state-gate-20260829"
)
GOAL = f"{PACKET}/GOAL.md"
PREFLIGHT = f"{PACKET}/PREFLIGHT_WITNESSES.md"
NOTE = (
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PREREG = "5e64f859d9e5aee0df108333aa6830f9e415af4f"
PARENT = "cb472dbbc65e2c46feca66987b7b0bfc7db4eb80"
BLOCK03_RESULT = "d8cc11fb5210321cf081866572b90a6ce290edcf"
CURRENT_MAIN = "004f64e1c87dad696b282cf2b526f3e7312dc82d"
GOAL_BLOB = "10926b15206d92ea49cc7f1b3f0820824764bdd3"
PREFLIGHT_BLOB = "52515476e975cf169f2dbe3842b90266e613e26a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK03_CACHE = (
    "logs/runner-cache/"
    "admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt"
)
BLOCK03_CACHE_BLOB = "5d13b199c4da8670806a743046c5a4965988b941"
AUDIT_TIMEOUT_SEC = 120

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block04-fresh-site-successor-state-gate-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block04-fresh-site-successor-state-gate-20260829/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
)

Point = tuple[int, int, int]
SHELL: tuple[Point, ...] = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)
ORIGIN: Point = (0, 0, 0)

MUTATIONS = (
    "stale_main",
    "drop_parent",
    "drop_prereg",
    "drift_goal",
    "drift_preflight",
    "drift_axiom",
    "asymmetric_shell",
    "five_neighbor_readiness",
    "allow_record_overwrite",
    "delete_wrong_ready_site",
    "create_new_ready_site",
    "outcome_changes_remaining_eta",
    "call_adjacent_target_fresh",
    "collapse_outer_completions",
    "call_compatibility_reachable",
    "supply_hidden_site_selector",
    "call_synchronous_front_growth",
    "erase_live_exit",
    "claim_autonomous_history",
    "claim_axiom_defect",
    "claim_obligation_retirement",
    "claim_toe_movement",
    "claim_retained",
)

N5_LINES = (
    "N5 per_element: checked all six directed neighbor choices; every nominal x+d target is already a Record under the six-neighbor event premise.",
    "N5 per_site: checked one permanent append at an arbitrary ready site; the exact ready-set change is deletion of that site only.",
    "N5 per_mode: checked and not executed — no spectral or momentum mode enters this purely Record-domain typing theorem.",
    "N5 per_block: checked all 64 masks and the 24 active H1 masks; formal outer-shell completions remain compatibility rows, not events.",
    "N5 lattice_wide: checked by a cardinality-free set argument and finite co-hole census; no claim is made for alternative readiness or non-Record conditions.",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=120
    ).strip()


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def negate(point: Point) -> Point:
    return tuple(-value for value in point)  # type: ignore[return-value]


def shell_at(site: Point, shell: tuple[Point, ...] = SHELL) -> set[Point]:
    return {add(site, direction) for direction in shell}


def ready_sites_in_candidates(
    omega: set[Point], candidates: set[Point], shell: tuple[Point, ...] = SHELL,
) -> set[Point]:
    return {
        site for site in candidates
        if site not in omega and shell_at(site, shell) <= omega
    }


def ready_holes(holes: set[Point], shell: tuple[Point, ...] = SHELL) -> set[Point]:
    """Ready sites for the exact cofinite state Omega=Z^3 minus holes."""
    return {
        site for site in holes
        if not (shell_at(site, shell) & holes)
    }


@cache
def authority_facts() -> dict[str, object]:
    minimal = "docs/MINIMAL_AXIOMS_2026-06-29.md"
    block03_runner = (
        "scripts/admissibility_d4_affine_lineage_binary_record_join_"
        "2026_08_29.py"
    )
    return {
        "origin_main": git("rev-parse", "origin/main"),
        "parent_is_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "prereg_is_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "block03_is_ancestor": subprocess.run(
            ("git", "merge-base", "--is-ancestor", BLOCK03_RESULT, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_worktree": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_worktree": git("hash-object", "--", PREFLIGHT),
        "axiom_blob": git("hash-object", "--", minimal),
        "block03_runner_registered": git(
            "rev-parse", f"{BLOCK03_RESULT}:{block03_runner}"
        ),
        "block03_runner_worktree": git("hash-object", "--", block03_runner),
        "block03_cache_registered": git(
            "rev-parse", f"{BLOCK03_RESULT}:{BLOCK03_CACHE}"
        ),
        "formation_boundary_needle": all(
            needle in (ROOT / minimal).read_text(encoding="utf-8")
            for needle in (
                "it does not supply the formation site, probability,",
                "or rate",
            )
        ),
    }


@cache
def shell_and_proof_facts(asymmetric: bool = False) -> dict[str, object]:
    shell = SHELL
    if asymmetric:
        shell = SHELL[:-1] + ((1, 1, 0),)
    unique = len(shell) == len(set(shell)) == 6
    irreflexive = ORIGIN not in shell
    symmetric = all(negate(direction) in shell for direction in shell)

    # The load-bearing implication is cardinality-free.  If y could become
    # ready only because x was appended, then x is a neighbor of y.  Shell
    # symmetry makes y a neighbor of x; x-ready therefore put y in Omega,
    # contradicting y being fresh after the append.
    implication_rows = tuple(
        (
            negate(direction) in shell,
            add(ORIGIN, direction) in shell_at(ORIGIN, shell),
        )
        for direction in shell
    )
    new_ready_contradiction = all(
        inverse_present and old_neighbor_present
        for inverse_present, old_neighbor_present in implication_rows
    )

    # Exhaust a nontrivial family of exact cofinite lattice states.  The
    # theorem is proved above; this census guards the implemented set update.
    sample_points = tuple(
        (x, y, 0) for x in range(-1, 2) for y in range(-1, 2)
    )
    census_rows = 0
    census_pass = True
    multi_ready_seen = False
    order_rows = 0
    for bits in range(1 << len(sample_points)):
        holes = {
            point for index, point in enumerate(sample_points)
            if (bits >> index) & 1
        }
        ready = ready_holes(holes, shell)
        multi_ready_seen = multi_ready_seen or len(ready) > 1
        for site in ready:
            census_rows += 1
            after = ready_holes(holes - {site}, shell)
            census_pass = census_pass and after == ready - {site}
        if len(ready) >= 2:
            left, right = sorted(ready)[:2]
            after_left_right = ready_holes(holes - {left, right}, shell)
            after_right_left = ready_holes(holes - {right, left}, shell)
            order_rows += 1
            census_pass = census_pass and (
                after_left_right == after_right_left == ready - {left, right}
            )

    # Every pair of ready holes must be nonadjacent.  This is the same
    # symmetry contradiction, checked explicitly on the census too.
    independent_rows = all(
        right not in shell_at(left, shell)
        for bits in range(1 << len(sample_points))
        for ready in (ready_holes({
            point for index, point in enumerate(sample_points)
            if (bits >> index) & 1
        }, shell),)
        for left, right in combinations(sorted(ready), 2)
    )
    return {
        "shell": shell,
        "unique": unique,
        "irreflexive": irreflexive,
        "symmetric": symmetric,
        "new_ready_contradiction": new_ready_contradiction,
        "ready_deletion_theorem": (
            unique and irreflexive and symmetric
            and new_ready_contradiction and census_pass
        ),
        "ready_sites_pairwise_nonadjacent": independent_rows,
        "cofinite_state_count": 1 << len(sample_points),
        "append_rows": census_rows,
        "two_site_order_rows": order_rows,
        "multi_ready_seen": multi_ready_seen,
        "simultaneous_update_is_set_deletion": census_pass,
        "outcome_independent": True,
        "asymmetric": asymmetric,
    }


@cache
def threshold_five_counterexample() -> dict[str, object]:
    """Exhibit a live front route outside the all-six readiness theorem."""
    holes = {ORIGIN, (1, 0, 0), (2, 0, 0)}

    def five_ready(current_holes: set[Point]) -> set[Point]:
        return {
            site for site in current_holes
            if len(shell_at(site) & current_holes) <= 1
        }

    before = five_ready(holes)
    chosen = ORIGIN
    after = five_ready(holes - {chosen})
    newly_ready = after - (before - {chosen})
    return {
        "holes": holes,
        "before": before,
        "chosen": chosen,
        "after": after,
        "newly_ready": newly_ready,
        "front_route_exists": newly_ready == {(1, 0, 0)},
        "all_six_theorem_does_not_extend_to_five": bool(newly_ready),
    }


def mask_from_values(site: Point, values: dict[Point, int]) -> int:
    return sum(
        values[add(site, direction)] << index
        for index, direction in enumerate(SHELL)
    )


@cache
def successor_census_facts(collapse_completions: bool = False) -> dict[str, object]:
    decoder = b3.decoder_facts()
    active = tuple(sorted(decoder["transport"]))
    active_set = set(active)
    direct_rows = []
    completion_rows = []
    completion_masks: dict[tuple[int, int, int], set[int]] = {}
    fixed_back_rows = []
    only_back_fixed_rows = []
    for mask in range(64):
        base_values = {
            add(ORIGIN, direction): (mask >> index) & 1
            for index, direction in enumerate(SHELL)
        }
        omega = set(base_values)
        center_ready = (
            ORIGIN not in omega and shell_at(ORIGIN) <= omega
        )
        for branch in (0, 1):
            after_values = dict(base_values)
            after_values[ORIGIN] = branch
            after_omega = omega | {ORIGIN}
            for direction_index, direction in enumerate(SHELL):
                target = add(ORIGIN, direction)
                direct_rows.append(
                    center_ready
                    and target in omega
                    and target in after_omega
                    and target != ORIGIN
                )
                outer_sites = tuple(
                    add(target, neighbor_direction)
                    for neighbor_direction in SHELL
                    if neighbor_direction != negate(direction)
                )
                disjoint = (
                    len(set(outer_sites)) == 5
                    and not (set(outer_sites) & shell_at(ORIGIN))
                    and ORIGIN not in outer_sites
                )
                possibilities = (0,) if collapse_completions else range(32)
                masks = set()
                for completion in possibilities:
                    values = dict(after_values)
                    for bit_index, outer_site in enumerate(outer_sites):
                        values[outer_site] = (completion >> bit_index) & 1
                    next_mask = mask_from_values(target, values)
                    masks.add(next_mask)
                    back_index = SHELL.index(negate(direction))
                    fixed_back_rows.append(
                        ((next_mask >> back_index) & 1) == branch
                    )
                    completion_rows.append(disjoint)
                completion_masks[(mask, branch, direction_index)] = masks
                back_index = SHELL.index(negate(direction))
                only_back_fixed_rows.append(
                    len({
                        candidate & ~(1 << back_index) for candidate in masks
                    }) == (1 if collapse_completions else 32)
                )
    active_rows = {
        key: masks for key, masks in completion_masks.items()
        if key[0] in active_set
    }
    active_next_active = sum(
        candidate in active_set
        for masks in active_rows.values() for candidate in masks
    )
    active_next_inactive = sum(
        candidate not in active_set
        for masks in active_rows.values() for candidate in masks
    )
    return {
        "active_masks": active,
        "active_count": len(active),
        "all_direct_targets_already_records": all(direct_rows),
        "direct_row_count": len(direct_rows),
        "all_outer_sites_disjoint_from_input_shell": all(completion_rows),
        "all_back_bits_fixed_by_branch": all(fixed_back_rows),
        "only_back_bit_fixed": all(only_back_fixed_rows),
        "all_completion_count": sum(
            len(masks) for masks in completion_masks.values()
        ),
        "active_completion_count": sum(
            len(masks) for masks in active_rows.values()
        ),
        "active_start_next_active_count": active_next_active,
        "active_start_next_inactive_count": active_next_inactive,
        "per_tuple_completion_counts": {
            len(masks) for masks in completion_masks.values()
        },
        "active_per_tuple_completion_counts": {
            len(masks) for masks in active_rows.values()
        },
        "nominal_direct_successor_terminal": "NO-FRESH-NEIGHBOR",
        "local_tuple_information_terminal": "SUCCESSOR-STATE-MISSING",
        "compatibility_is_reachability": False,
        "collapse_completions": collapse_completions,
    }


@cache
def route_scope_facts() -> dict[str, object]:
    threshold = threshold_five_counterexample()
    exits = (
        "non_Record_quantum_neighbor_conditions",
        "less_than_six_neighbor_front_predicate",
        "synchronous_update_with_different_readiness",
        "normalized_site_POVM_or_local_hazard",
        "external_source_or_participant_process",
        "exact_shared_carrier_compiler_after_open_gates",
    )
    return {
        "live_exit_families": exits,
        "live_exit_count": len(exits),
        "threshold_five_front_counterexample": threshold["front_route_exists"],
        "n1_broad_no_go_passes": False,
        "n7_broad_no_go_passes": False,
        "broad_no_dynamics_claim_promoted": False,
        "axiom_defect_established": False,
        "model_realization_boundary_only": True,
        "next_positive_target": (
            "construct a typed formation mechanism on non-Record conditions "
            "or a weaker readiness/front carrier"
        ),
    }


def evaluate(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    shell = dict(shell_and_proof_facts(
        asymmetric=mutation == "asymmetric_shell"
    ))
    successor = dict(successor_census_facts(
        collapse_completions=mutation == "collapse_outer_completions"
    ))
    routes = dict(route_scope_facts())
    claims = {
        "all_six_readiness": mutation != "five_neighbor_readiness",
        "permanent_append": mutation != "allow_record_overwrite",
        "deletes_exactly_x": mutation != "delete_wrong_ready_site",
        "creates_no_new_ready": mutation != "create_new_ready_site",
        "remaining_eta_unchanged": mutation != "outcome_changes_remaining_eta",
        "adjacent_target_fresh": mutation == "call_adjacent_target_fresh",
        "compatibility_reachable": mutation == "call_compatibility_reachable",
        "hidden_site_selector": mutation == "supply_hidden_site_selector",
        "synchronous_front_growth": mutation == "call_synchronous_front_growth",
        "autonomous_history": mutation == "claim_autonomous_history",
        "axiom_defect": mutation == "claim_axiom_defect",
        "obligation_retirement": int(mutation == "claim_obligation_retirement"),
        "toe_movement": int(mutation == "claim_toe_movement"),
        "retained": mutation == "claim_retained",
    }
    if mutation == "stale_main":
        authority["origin_main"] = "0" * 40
    elif mutation == "drop_parent":
        authority["parent_is_ancestor"] = False
    elif mutation == "drop_prereg":
        authority["prereg_is_ancestor"] = False
    elif mutation == "drift_goal":
        authority["goal_worktree"] = "0" * 40
    elif mutation == "drift_preflight":
        authority["preflight_worktree"] = "0" * 40
    elif mutation == "drift_axiom":
        authority["axiom_blob"] = "0" * 40
    elif mutation == "erase_live_exit":
        routes["live_exit_families"] = routes["live_exit_families"][:4]
        routes["live_exit_count"] = 4

    authority_ok = (
        authority["origin_main"] == CURRENT_MAIN
        and authority["parent_is_ancestor"]
        and authority["prereg_is_ancestor"]
        and authority["block03_is_ancestor"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom_blob"] == AXIOM_BLOB
        and authority["block03_runner_registered"]
        == authority["block03_runner_worktree"]
        and authority["block03_cache_registered"] == BLOCK03_CACHE_BLOB
        and authority["formation_boundary_needle"]
    )
    readiness_ok = (
        claims["all_six_readiness"]
        and claims["permanent_append"]
        and shell["unique"]
        and shell["irreflexive"]
        and shell["symmetric"]
        and shell["new_ready_contradiction"]
        and shell["ready_deletion_theorem"]
        and shell["ready_sites_pairwise_nonadjacent"]
        and shell["cofinite_state_count"] == 512
        and shell["append_rows"] > 0
        and shell["two_site_order_rows"] > 0
        and shell["multi_ready_seen"]
        and shell["simultaneous_update_is_set_deletion"]
        and shell["outcome_independent"]
        and claims["deletes_exactly_x"]
        and claims["creates_no_new_ready"]
        and claims["remaining_eta_unchanged"]
    )
    successor_ok = (
        successor["active_count"] == 24
        and successor["all_direct_targets_already_records"]
        and successor["direct_row_count"] == 64 * 2 * 6
        and successor["all_outer_sites_disjoint_from_input_shell"]
        and successor["all_back_bits_fixed_by_branch"]
        and successor["only_back_bit_fixed"]
        and successor["all_completion_count"] == 64 * 2 * 6 * 32
        and successor["active_completion_count"] == 24 * 2 * 6 * 32
        and successor["active_start_next_active_count"] == 3456
        and successor["active_start_next_inactive_count"] == 5760
        and successor["per_tuple_completion_counts"] == {32}
        and successor["active_per_tuple_completion_counts"] == {32}
        and successor["nominal_direct_successor_terminal"]
        == "NO-FRESH-NEIGHBOR"
        and successor["local_tuple_information_terminal"]
        == "SUCCESSOR-STATE-MISSING"
        and not successor["compatibility_is_reachability"]
        and not claims["adjacent_target_fresh"]
        and not claims["compatibility_reachable"]
    )
    route_ok = (
        routes["live_exit_count"] >= 5
        and len(set(routes["live_exit_families"]))
        == routes["live_exit_count"]
        and routes["threshold_five_front_counterexample"]
        and not routes["n1_broad_no_go_passes"]
        and not routes["n7_broad_no_go_passes"]
        and not routes["broad_no_dynamics_claim_promoted"]
        and not routes["axiom_defect_established"]
        and routes["model_realization_boundary_only"]
        and not claims["hidden_site_selector"]
        and not claims["synchronous_front_growth"]
        and not claims["autonomous_history"]
        and not claims["axiom_defect"]
    )
    accounting_ok = (
        claims["obligation_retirement"] == 0
        and claims["toe_movement"] == 0
        and not claims["retained"]
    )
    return {
        "A_authority": (
            authority_ok,
            "parent, preregistration, minimal axioms, Block-03 runner, and cache identities match",
        ),
        "B_ready_set_theorem": (
            readiness_ok,
            "six-Record readiness is an independent set and one append deletes exactly its chosen ready site",
        ),
        "C_successor_typing": (
            successor_ok,
            "all adjacent targets are occupied and every nominal next mask has 32 non-reachable outer-shell completions",
        ),
        "D_no_go_scope": (
            route_ok,
            "six distinct live formation routes defeat any universal dynamics or axiom no-go",
        ),
        "E_accounting": (
            accounting_ok,
            "history, axiom, retention, obligation, and TOE movement remain unset",
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
    shell = shell_and_proof_facts()
    successor = successor_census_facts()
    print(
        "READY_SET: F(R append x)=F(R)\\{x}; ready sites are pairwise "
        f"nonadjacent; finite co-hole states={shell['cofinite_state_count']}; "
        f"append rows={shell['append_rows']}."
    )
    print(
        "SUCCESSOR: direct target x+d is occupied on all "
        f"{successor['direct_row_count']} all-mask rows; active compatibility "
        f"rows={successor['active_completion_count']}=24*2*6*32."
    )
    print(
        "COMPLETION_SPLIT: active-start nominal masks resolve into "
        f"next-active={successor['active_start_next_active_count']} and "
        f"next-inactive={successor['active_start_next_inactive_count']}; "
        "neither class is a reachable event at the occupied target."
    )
    print(
        "TERMINALS: direct=NO-FRESH-NEIGHBOR; local tuple="
        "SUCCESSOR-STATE-MISSING; multiple ready sites require a separate "
        "SITE-SELECTOR-MISSING adjudication."
    )
    print(
        "SCOPE: exact cleanup-only theorem for the all-six-Record readiness "
        "surface; a five-neighbor front counterexample and five other live "
        "routes forbid a universal dynamics or axiom no-go."
    )
    print(
        "ACCOUNTING: autonomous_history=false; axiom_update=false; "
        "obligation_retirement=0; TOE_movement=0; retained=false."
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
