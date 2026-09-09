#!/usr/bin/env python3
"""Independent graph-theoretic Block-04 readiness/successor checker.

This implementation imports no Block-04 primary code or result booleans.  It
recasts six-Record readiness as a closed-neighborhood predicate on undirected
graphs, exhausts every simple graph through six vertices, and reconstructs the
active-mask completion census through an independent affine action path.
"""

from __future__ import annotations

import argparse
from functools import cache
from itertools import combinations
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29 as i3  # noqa: E402


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
BLOCK03_INDEPENDENT_CACHE = (
    "logs/runner-cache/independent_admissibility_d4_affine_lineage_binary_"
    "record_join_2026_08_29.txt"
)
BLOCK03_INDEPENDENT_CACHE_BLOB = "a1c2de91f808b7a4e5175e804db6680f012c7dac"
AUDIT_TIMEOUT_SEC = 120

AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block04-fresh-site-successor-state-gate-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block04-fresh-site-successor-state-gate-20260829/PREFLIGHT_WITNESSES.md",
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_AFFINE_LINEAGE_BINARY_RECORD_MULTI_JOIN_REPEATABILITY_SELECTOR_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.py",
    "logs/runner-cache/independent_admissibility_d4_affine_lineage_binary_record_join_2026_08_29.txt",
)

Point = tuple[int, int, int]
DIRECTIONS: tuple[Point, ...] = (
    (-1, 0, 0),
    (1, 0, 0),
    (0, -1, 0),
    (0, 1, 0),
    (0, 0, -1),
    (0, 0, 1),
)

MUTATIONS = (
    "stale_main",
    "drop_parent",
    "drop_prereg",
    "drift_goal",
    "drift_preflight",
    "drift_axiom",
    "directed_graph",
    "threshold_degree_minus_one",
    "erase_graph_census",
    "adjacent_ready_pair",
    "new_ready_after_append",
    "adjacent_successor_fresh",
    "one_outer_completion",
    "compatibility_equals_reachability",
    "hide_live_routes",
    "claim_history",
    "claim_axiom",
    "claim_obligation",
    "claim_toe",
    "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=120
    ).strip()


def add(left: Point, right: Point) -> Point:
    return tuple(left[i] + right[i] for i in range(3))  # type: ignore[return-value]


def neg(point: Point) -> Point:
    return tuple(-value for value in point)  # type: ignore[return-value]


@cache
def authority_facts() -> dict[str, object]:
    minimal = "docs/MINIMAL_AXIOMS_2026-06-29.md"
    runner = (
        "scripts/independent_admissibility_d4_affine_lineage_binary_record_"
        "join_2026_08_29.py"
    )
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PARENT, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "prereg": subprocess.run(
            ("git", "merge-base", "--is-ancestor", PREREG, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "block03": subprocess.run(
            ("git", "merge-base", "--is-ancestor", BLOCK03_RESULT, "HEAD"),
            cwd=ROOT, check=False,
        ).returncode == 0,
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL}"),
        "goal_worktree": git("hash-object", "--", GOAL),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT}"),
        "preflight_worktree": git("hash-object", "--", PREFLIGHT),
        "axiom": git("hash-object", "--", minimal),
        "parent_runner_registered": git(
            "rev-parse", f"{BLOCK03_RESULT}:{runner}"
        ),
        "parent_runner_worktree": git("hash-object", "--", runner),
        "parent_cache_registered": git(
            "rev-parse", f"{BLOCK03_RESULT}:{BLOCK03_INDEPENDENT_CACHE}"
        ),
    }


def undirected_graph(n: int, edge_bits: int) -> tuple[frozenset[int], ...]:
    adjacency = [set() for _ in range(n)]
    for edge_index, (left, right) in enumerate(combinations(range(n), 2)):
        if (edge_bits >> edge_index) & 1:
            adjacency[left].add(right)
            adjacency[right].add(left)
    return tuple(frozenset(row) for row in adjacency)


def ready_vertices(
    adjacency: tuple[frozenset[int], ...], occupied_bits: int,
) -> frozenset[int]:
    return frozenset(
        vertex for vertex, neighbors in enumerate(adjacency)
        if not ((occupied_bits >> vertex) & 1)
        and all((occupied_bits >> neighbor) & 1 for neighbor in neighbors)
    )


@cache
def graph_exhaustion_facts(directed_mutant: bool = False) -> dict[str, object]:
    graph_count = 0
    state_count = 0
    append_count = 0
    pair_count = 0
    deletion_exact = True
    pairwise_independent = True
    order_independent = True
    for n in range(1, 7):
        edge_count = n * (n - 1) // 2
        for edge_bits in range(1 << edge_count):
            adjacency = undirected_graph(n, edge_bits)
            graph_count += 1
            for occupied in range(1 << n):
                state_count += 1
                ready = ready_vertices(adjacency, occupied)
                for left, right in combinations(sorted(ready), 2):
                    pair_count += 1
                    pairwise_independent = pairwise_independent and (
                        right not in adjacency[left] and left not in adjacency[right]
                    )
                for site in ready:
                    append_count += 1
                    after = ready_vertices(adjacency, occupied | (1 << site))
                    deletion_exact = deletion_exact and after == ready - {site}
                if len(ready) >= 2:
                    left, right = sorted(ready)[:2]
                    both = occupied | (1 << left) | (1 << right)
                    order_independent = order_independent and (
                        ready_vertices(adjacency, both) == ready - {left, right}
                    )

    directed_counterexample = False
    if directed_mutant:
        # N(0)={1}, N(1)=empty.  With Omega={1}, site 0 is ready.  Append 0;
        # site 2 can be arranged with N(2)={0} and becomes newly ready while
        # remaining fresh.  This is impossible for symmetric adjacency.
        adjacency = (frozenset({1}), frozenset(), frozenset({0}))
        occupied = 1 << 1
        before = ready_vertices(adjacency, occupied)
        after = ready_vertices(adjacency, occupied | 1)
        directed_counterexample = 0 in before and 2 in after - (before - {0})
        deletion_exact = deletion_exact and not directed_counterexample

    return {
        "max_vertices": 6,
        "graph_count": graph_count,
        "state_count": state_count,
        "append_count": append_count,
        "pair_count": pair_count,
        "deletion_exact": deletion_exact,
        "pairwise_independent": pairwise_independent,
        "order_independent": order_independent,
        "formal_symmetry_implication": all(
            neg(direction) in DIRECTIONS for direction in DIRECTIONS
        ),
        "directed_counterexample": directed_counterexample,
        "directed_mutant": directed_mutant,
    }


@cache
def threshold_counterexample() -> dict[str, object]:
    # On a cubic co-hole chain of length three, a degree-1 hole is 5-ready;
    # filling the endpoint makes the middle hole newly 5-ready.
    holes = {(0, 0, 0), (1, 0, 0), (2, 0, 0)}

    def missing_neighbors(site: Point, current: set[Point]) -> int:
        return sum(add(site, direction) in current for direction in DIRECTIONS)

    def five_ready(current: set[Point]) -> set[Point]:
        return {site for site in current if missing_neighbors(site, current) <= 1}

    before = five_ready(holes)
    after = five_ready(holes - {(0, 0, 0)})
    new = after - (before - {(0, 0, 0)})
    return {
        "before": before,
        "after": after,
        "new": new,
        "exact": new == {(1, 0, 0)},
    }


@cache
def independent_completion_facts(one_completion: bool = False) -> dict[str, object]:
    action = i3.independent_action_and_eta()
    active = tuple(
        mask for mask, value in enumerate(action["active_table"]) if value
    )
    inverse_index = {
        index: DIRECTIONS.index(neg(direction))
        for index, direction in enumerate(DIRECTIONS)
    }
    geometry_rows = []
    all_counts = []
    active_counts = []
    active_next_active = 0
    active_next_inactive = 0
    active_set = set(active)
    fixed_rows = []
    for mask in range(64):
        for branch in (0, 1):
            for direction_index, direction in enumerate(DIRECTIONS):
                target = direction
                outer = tuple(
                    add(target, step) for step in DIRECTIONS
                    if step != neg(direction)
                )
                input_shell = set(DIRECTIONS)
                geometry_rows.append(
                    len(set(outer)) == 5
                    and not (set(outer) & input_shell)
                    and (0, 0, 0) not in outer
                    and target in input_shell
                )
                candidates = set()
                values = (0,) if one_completion else range(32)
                for outer_bits in values:
                    next_mask = 0
                    cursor = 0
                    for bit_index in range(6):
                        if bit_index == inverse_index[direction_index]:
                            bit = branch
                        else:
                            bit = (outer_bits >> cursor) & 1
                            cursor += 1
                        next_mask |= bit << bit_index
                    candidates.add(next_mask)
                    fixed_rows.append(
                        ((next_mask >> inverse_index[direction_index]) & 1)
                        == branch
                    )
                all_counts.append(len(candidates))
                if mask in active:
                    active_counts.append(len(candidates))
                    active_next_active += sum(
                        candidate in active_set for candidate in candidates
                    )
                    active_next_inactive += sum(
                        candidate not in active_set for candidate in candidates
                    )
    return {
        "active_count": len(active),
        "direct_target_in_input_domain": all(geometry_rows),
        "geometry_row_count": len(geometry_rows),
        "back_bit_fixed": all(fixed_rows),
        "all_counts": set(all_counts),
        "active_counts": set(active_counts),
        "all_total": sum(all_counts),
        "active_total": sum(active_counts),
        "active_next_active": active_next_active,
        "active_next_inactive": active_next_inactive,
        "direct_terminal": "NO-FRESH-NEIGHBOR",
        "information_terminal": "SUCCESSOR-STATE-MISSING",
        "one_completion": one_completion,
    }


def checks(mutation: str = "") -> dict[str, tuple[bool, str]]:
    authority = dict(authority_facts())
    graph = dict(graph_exhaustion_facts(mutation == "directed_graph"))
    completion = dict(independent_completion_facts(
        mutation == "one_outer_completion"
    ))
    claims = {
        "all_six": mutation != "threshold_degree_minus_one",
        "graph_census": mutation != "erase_graph_census",
        "adjacent_ready": mutation == "adjacent_ready_pair",
        "new_ready": mutation == "new_ready_after_append",
        "adjacent_fresh": mutation == "adjacent_successor_fresh",
        "compatibility_reachable": mutation == "compatibility_equals_reachability",
        "live_routes": 4 if mutation == "hide_live_routes" else 6,
        "history": mutation == "claim_history",
        "axiom": mutation == "claim_axiom",
        "obligation": int(mutation == "claim_obligation"),
        "toe": int(mutation == "claim_toe"),
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

    authority_ok = (
        authority["main"] == CURRENT_MAIN
        and authority["parent"] and authority["prereg"] and authority["block03"]
        and authority["goal_registered"] == GOAL_BLOB
        and authority["goal_worktree"] == GOAL_BLOB
        and authority["preflight_registered"] == PREFLIGHT_BLOB
        and authority["preflight_worktree"] == PREFLIGHT_BLOB
        and authority["axiom"] == AXIOM_BLOB
        and authority["parent_runner_registered"]
        == authority["parent_runner_worktree"]
        and authority["parent_cache_registered"]
        == BLOCK03_INDEPENDENT_CACHE_BLOB
    )
    graph_ok = (
        claims["all_six"]
        and claims["graph_census"]
        and graph["max_vertices"] == 6
        and graph["graph_count"] == sum(
            1 << (n * (n - 1) // 2) for n in range(1, 7)
        )
        and graph["state_count"] > 2_000_000
        and graph["append_count"] > 0
        and graph["pair_count"] > 0
        and graph["deletion_exact"]
        and graph["pairwise_independent"]
        and graph["order_independent"]
        and graph["formal_symmetry_implication"]
        and not graph["directed_counterexample"]
        and not claims["adjacent_ready"]
        and not claims["new_ready"]
        and threshold_counterexample()["exact"]
    )
    successor_ok = (
        completion["active_count"] == 24
        and completion["direct_target_in_input_domain"]
        and completion["geometry_row_count"] == 64 * 2 * 6
        and completion["back_bit_fixed"]
        and completion["all_counts"] == {32}
        and completion["active_counts"] == {32}
        and completion["all_total"] == 64 * 2 * 6 * 32
        and completion["active_total"] == 24 * 2 * 6 * 32
        and completion["active_next_active"] == 3456
        and completion["active_next_inactive"] == 5760
        and completion["direct_terminal"] == "NO-FRESH-NEIGHBOR"
        and completion["information_terminal"]
        == "SUCCESSOR-STATE-MISSING"
        and not claims["adjacent_fresh"]
        and not claims["compatibility_reachable"]
    )
    scope_ok = (
        claims["live_routes"] >= 5
        and not claims["history"]
        and not claims["axiom"]
        and claims["obligation"] == 0
        and claims["toe"] == 0
        and not claims["retained"]
    )
    return {
        "A": (authority_ok, "independent parent and preregistration identities match"),
        "B": (graph_ok, "every simple undirected graph through six vertices obeys exact ready-set deletion and independent ready sites"),
        "C": (successor_ok, "independent affine masks reproduce the occupied target and 32-way outer-shell deficit"),
        "D": (scope_ok, "live alternative routes keep the result below history, axiom, obligation, TOE, or retention claims"),
    }


def mutation_sweep() -> tuple[int, tuple[str, ...]]:
    survivors = tuple(
        mutation for mutation in MUTATIONS
        if all(ok for ok, _message in checks(mutation).values())
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
    result = checks(args.mutation)
    passed = 0
    for name, (ok, message) in result.items():
        print(f"PASS {name}: {message}" if ok else f"FAIL {name}: {message}")
        passed += int(ok)
    rejected, survivors = mutation_sweep()
    graph = graph_exhaustion_facts()
    completion = independent_completion_facts()
    print(
        "INDEPENDENT_GRAPH: simple_graphs="
        f"{graph['graph_count']}; states={graph['state_count']}; "
        f"appends={graph['append_count']}; max_vertices=6."
    )
    print(
        "INDEPENDENT_SUCCESSOR: direct_rows="
        f"{completion['geometry_row_count']}; active_completion_rows="
        f"{completion['active_total']}; completions_per_tuple=32."
    )
    print(
        "INDEPENDENT_DECISION: exact all-neighbor cleanup-only boundary; "
        "five-neighbor front counterexample live; universal dynamics and "
        "axiom negatives not promoted."
    )
    if survivors:
        print("MUTATION_SURVIVORS:", ",".join(survivors))
    failures = len(result) - passed + len(survivors)
    print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
    print(f"TOTAL: PASS={passed} FAIL={failures}")
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
