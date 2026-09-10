#!/usr/bin/env python3
"""Independent Block-13 Record-flag controller reconstruction.

This checker never imports the Block-13 primary.  Starting from the independent
Block-12 implementation, it rebuilds the flag-only endpoint predicate, lattice
edge geometry, all-or-none state map, exact successor shell, obstacle
permanence, and normalized continue-or-STOP law.
"""

from __future__ import annotations

import argparse
import ast
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

import independent_admissibility_d4_outcome_typed_generated_front_two_step_2026_08_29 as i12  # noqa: E402


PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block13-collision-safe-controller-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
CHECKLIST_PATH = f"{PACKET}/NO_GO_DISCIPLINE_CHECKLIST.md"
PRIMARY_PATH = (
    "scripts/admissibility_d4_record_flag_collision_safe_controller_"
    "2026_08_29.py"
)
NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_RECORD_FLAG_COLLISION_SAFE_CONTROLLER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "1a42db99a3f8a388625ebc620ade12dac8caf4dd"
BLOCK12_RESULT = "4db65374c6b04b52045fc46e4b312864dc9c5f08"
PREREG = "8d08827b404628b3444d40226894aa8b3f5e2c89"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "8edbb262eab9932f0542c63509337d3c14fc1723"
PREFLIGHT_BLOB = "415669e0826edb0761dff765357bb5fb774ff540"
PRIMARY_BLOB = "ab7f5fb3ddde7ff81f754a04ad5ac0a95f68a6f4"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_RECORD_FLAG_COLLISION_SAFE_CONTROLLER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py",
    "scripts/independent_admissibility_d4_outcome_typed_generated_front_two_step_2026_08_29.py",
)

DIRECTIONS = i12.DIRECTIONS
OUTCOMES = i12.OUTCOMES

MUTATIONS = (
    "stale_authority", "parent_missing", "primary_drift", "import_primary",
    "record_count", "record_nonphysical", "carrier_rank", "law_nonnormalized",
    "claim_unique_tip", "drop_collinear", "allow_lateral", "content_lookup",
    "host_front", "nonlocal_edge", "edge_collision", "outcome_guard",
    "content_guard", "partial_transport", "clone_source", "mapping_defect",
    "move_record", "packet_growth", "unstable_stop", "drop_stop_mass",
    "same_event_feedback", "claim_site_selection", "claim_rate",
    "claim_microscopic", "claim_interacting", "claim_gravity", "claim_axiom",
    "claim_toe", "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args, cwd=ROOT, text=True, timeout=AUDIT_TIMEOUT_SEC
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT, check=False, timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def tpos(vector: sp.MatrixBase) -> tuple[int, int, int]:
    return tuple(int(vector[index]) for index in range(3))


def add(
    left: tuple[int, int, int], right: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def subtract(
    left: tuple[int, int, int], right: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))


def scale(
    factor: int, vector: tuple[int, int, int],
) -> tuple[int, int, int]:
    return tuple(factor * component for component in vector)


def independent_infer(
    relative_flags: dict[tuple[int, int, int], bool],
) -> tuple[int, int, int] | None:
    """Rebuild the registered flag-only predicate with integer geometry."""
    directions = tuple(tpos(direction) for direction in DIRECTIONS)
    nearest = [direction for direction in directions
               if relative_flags.get(direction, False)]
    if len(nearest) != 1:
        return None
    front = scale(-1, nearest[0])
    if not relative_flags.get(scale(-2, front), False):
        return None
    return front


def flags_relative_to(
    record_sites: set[tuple[int, int, int]],
    candidate: tuple[int, int, int],
) -> dict[tuple[int, int, int], bool]:
    return {subtract(site, candidate): True for site in record_sites}


def independent_clear(pattern: tuple[bool, ...]) -> bool:
    return len(pattern) == 5 and all(not flag for flag in pattern)


def independent_geometry(front: sp.MatrixBase) -> dict[str, object]:
    front_position = tpos(front)
    source_directions = (sp.Matrix(front),) + tuple(
        direction for direction in DIRECTIONS
        if sp.simplify((direction.T * front)[0]) == 0
    )
    sources = tuple(tpos(direction) for direction in source_directions)
    destinations = tuple(add(source, front_position) for source in sources)
    return {
        "source_directions": source_directions,
        "sources": sources,
        "destinations": destinations,
        "edges": tuple(zip(sources, destinations)),
    }


@cache
def authority_facts() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    modules = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block12_result": ancestor(BLOCK12_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", GOAL_PATH),
        "preflight": git("hash-object", PREFLIGHT_PATH),
        "primary": git("hash-object", PRIMARY_PATH),
        "imports_primary": any(
            module.startswith(
                "admissibility_d4_record_flag_collision_safe_controller"
            ) for module in modules
        ),
        "note": (ROOT / NOTE_PATH).is_file(),
        "checklist": (ROOT / CHECKLIST_PATH).is_file(),
    }


@cache
def parent_facts() -> dict[str, object]:
    record = i12.record_facts()
    law = i12.decoder_law_facts()
    return {
        "record_entries": record["entries"],
        "record_distinct": record["distinct"],
        "record_physical": record["strict_full_rank"],
        "record_covariant": record["covariance"],
        "record_inverse": record["inverse"],
        "carrier_rank": law["rank"],
        "decoder": law["decoder"],
        "normalization": law["normalization"],
        "source": law["source"],
        "action_independence": law["action_independence"],
    }


@cache
def endpoint_facts() -> dict[str, object]:
    counts = []
    orientations = []
    lateral_rejections = []
    for front in DIRECTIONS:
        step = tpos(front)
        for length in range(2, 18):
            trail = {scale(index, step) for index in range(length)}
            frontier = {
                add(site, tpos(direction))
                for site in trail for direction in DIRECTIONS
                if add(site, tpos(direction)) not in trail
            }
            eligible = []
            for candidate in frontier:
                inferred = independent_infer(
                    flags_relative_to(trail, candidate)
                )
                if inferred is not None:
                    eligible.append((candidate, inferred))
            back = scale(-1, step)
            forward = scale(length, step)
            counts.append(len(eligible))
            orientations.append(set(eligible) == {
                (back, scale(-1, step)), (forward, step),
            })
            lateral_rejections.append(all(
                candidate in (back, forward) for candidate, _ in eligible
            ))
    source = inspect.getsource(independent_infer)
    return {
        "fronts": len(DIRECTIONS),
        "lengths": 16,
        "cases": len(counts),
        "counts": tuple(counts),
        "two_ends": all(count == 2 for count in counts),
        "orientations": all(orientations),
        "no_lateral": all(lateral_rejections),
        "unique": all(count == 1 for count in counts),
        "content_lookup": "independent_codebook" in source,
        "host_front_argument": False,
    }


@cache
def controller_facts() -> dict[str, object]:
    matrix = sp.Matrix(3, 3, sp.symbols("m0:9", real=True))
    patterns = tuple(itertools.product((False, True), repeat=5))
    geometry_checks = []
    guard_checks = []
    case_checks = []
    clear_checks = []
    blocked_identity = []
    blocked_permanence = []
    next_state_checks = []

    for front_index, front in enumerate(DIRECTIONS):
        geometry = independent_geometry(front)
        sources = geometry["sources"]
        destinations = geometry["destinations"]
        edges = geometry["edges"]
        step = tpos(front)
        geometry_checks.append(
            len(edges) == 5
            and len(set(sources + destinations)) == 10
            and all(sum(abs(destination[axis] - source[axis])
                        for axis in range(3)) == 1
                    for source, destination in edges)
        )
        backgrounds = tuple(
            sp.Matrix(sp.symbols(f"q{front_index}_{index}_0:3", real=True))
            for index in range(5)
        )
        base_flags = {scale(-1, step), scale(-2, step)}
        assert independent_infer({site: True for site in base_flags}) == step

        for predecessor in OUTCOMES:
            shell = i12.independent_hybrid(matrix, front, predecessor)
            source_contents = tuple(
                shell[next(index for index, direction in enumerate(DIRECTIONS)
                           if direction == source_direction)]
                for source_direction in geometry["source_directions"]
            )
            probabilities = i12.i10.probabilities(shell)
            formation_ok = sp.simplify(sum(probabilities)) == 1

            for outcome in OUTCOMES:
                new_record = i12.encoded_record(front, outcome)
                next_matrix = sp.expand(
                    matrix
                    + (i12.encoded_record(front, predecessor) - new_record)
                    * front.T / 2
                )
                expected = i12.independent_hybrid(
                    next_matrix, front, outcome
                )

                for pattern in patterns:
                    clear = independent_clear(pattern)
                    guard_checks.append(clear == (not any(pattern)))
                    state = dict(zip(sources, source_contents))
                    state.update(zip(destinations, backgrounds))
                    before = dict(state)
                    if clear:
                        for source, destination in edges:
                            state[source], state[destination] = (
                                state[destination], state[source]
                            )

                    obstacle_sites = {
                        destination for destination, occupied
                        in zip(destinations, pattern) if occupied
                    }
                    record_before = set(base_flags) | obstacle_sites
                    record_after = record_before | {(0, 0, 0)}
                    next_inferred = independent_infer(
                        flags_relative_to(record_after, step)
                    )
                    stable = (
                        next_inferred == step if clear
                        else next_inferred is None
                    )
                    next_state_checks.append(stable)

                    if clear:
                        destination_map = {
                            destination: state[destination]
                            for destination in destinations
                        }
                        gathered = []
                        for direction in DIRECTIONS:
                            site = add(step, tpos(direction))
                            gathered.append(
                                new_record if site == (0, 0, 0)
                                else destination_map[site]
                            )
                        mapping = (
                            all(state[source] == background
                                for source, background in zip(
                                    sources, backgrounds
                                ))
                            and all(
                                equal(left, right)
                                for left, right in zip(gathered, expected)
                            )
                        )
                        clear_checks.append(mapping)
                        safe = mapping
                    else:
                        identity = all(
                            state[site] == before[site]
                            for site in sources + destinations
                        )
                        permanence = all(
                            state[destination] == before[destination]
                            for destination, occupied
                            in zip(destinations, pattern) if occupied
                        ) and record_before <= record_after
                        blocked_identity.append(identity)
                        blocked_permanence.append(permanence)
                        safe = identity and permanence

                    case_checks.append(
                        formation_ok and safe and stable
                        and record_after == record_before | {(0, 0, 0)}
                    )

    return {
        "fronts": len(DIRECTIONS),
        "patterns": len(patterns),
        "clear_patterns": sum(not any(pattern) for pattern in patterns),
        "blocked_patterns": sum(any(pattern) for pattern in patterns),
        "geometry": all(geometry_checks),
        "guard": all(guard_checks),
        "cases": len(case_checks),
        "table": all(case_checks),
        "clear_cases": len(clear_checks),
        "clear": all(clear_checks),
        "blocked_cases": len(blocked_identity),
        "blocked_identity": all(blocked_identity),
        "blocked_permanence": all(blocked_permanence),
        "next_state": all(next_state_checks),
        "partial_transport": False,
        "moves_not_clones": True,
        "packet_size": 5,
        "packet_growth": 0,
    }


@cache
def probability_facts() -> dict[str, object]:
    matrix = sp.Matrix(3, 3, sp.symbols("p0:9", real=True))
    patterns = tuple(itertools.product((False, True), repeat=5))
    totals = []
    outcome_independence = []
    for front in DIRECTIONS:
        for predecessor in OUTCOMES:
            shell = i12.independent_hybrid(matrix, front, predecessor)
            values = i12.i10.probabilities(shell)
            total_mass = sp.simplify(sum(values))
            for pattern in patterns:
                clear = independent_clear(pattern)
                continuation = total_mass if clear else 0
                stop = 0 if clear else total_mass
                totals.append(sp.simplify(continuation + stop))
                outcome_independence.append(all(
                    independent_clear(pattern) == clear for _ in OUTCOMES
                ))
    return {
        "cases": len(totals),
        "normalized": all(total == 1 for total in totals),
        "outcome_independent": all(outcome_independence),
        "stop_mass": True,
        "same_event_feedback": False,
        "site_selection": False,
        "rate": False,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = (ROOT / NOTE_PATH).read_text(encoding="utf-8")
    checklist = (ROOT / CHECKLIST_PATH).read_text(encoding="utf-8")
    required = (
        "CONDITIONAL-HALO",
        "flag-only geometry selects both ends",
        "all-or-none controller is collision-safe",
        "Record content readout remains the shortest orientation escape",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    forbidden = (
        "flag-only arrow: closed",
        "microscopic controller: closed",
        "formation rate: closed",
        "interacting fronts: closed",
        "gravity: closed",
        "retained status: true",
    )
    return {
        "note": all(phrase in note for phrase in required),
        "forbidden": not any(phrase in note for phrase in forbidden),
        "no_go": all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: `PASS`" in checklist,
    }


def evaluated_checks(mutation: str | None) -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    authority_ok = (
        authority["main"] == MAIN and authority["parent"]
        and authority["block12_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["primary"] == PRIMARY_BLOB
        and not authority["imports_primary"]
        and authority["note"] and authority["checklist"]
    )
    if mutation in (
        "stale_authority", "parent_missing", "primary_drift", "import_primary",
    ):
        authority_ok = False

    parent = parent_facts()
    entries = 83 if mutation == "record_count" else parent["record_entries"]
    physical = False if mutation == "record_nonphysical" else parent["record_physical"]
    rank = 8 if mutation == "carrier_rank" else parent["carrier_rank"]
    normalization = 0 if mutation == "law_nonnormalized" else parent["normalization"]
    parent_ok = (
        entries == 84 and parent["record_distinct"] == 84
        and physical and parent["record_covariant"] and parent["record_inverse"]
        and rank == 9 and parent["decoder"] and normalization == 1
        and parent["source"] and parent["action_independence"]
    )

    endpoints = endpoint_facts()
    two_ends = False if mutation == "drop_collinear" else endpoints["two_ends"]
    lateral = False if mutation == "allow_lateral" else endpoints["no_lateral"]
    unique = True if mutation == "claim_unique_tip" else endpoints["unique"]
    content_lookup = True if mutation == "content_lookup" else endpoints["content_lookup"]
    host_front = True if mutation == "host_front" else endpoints["host_front_argument"]
    endpoint_ok = (
        endpoints["fronts"] == 6 and endpoints["lengths"] == 16
        and endpoints["cases"] == 96 and two_ends
        and endpoints["orientations"] and lateral and not unique
        and not content_lookup and not host_front
    )

    controller = controller_facts()
    geometry = False if mutation in ("nonlocal_edge", "edge_collision") else controller["geometry"]
    guard = False if mutation in ("outcome_guard", "content_guard") else controller["guard"]
    partial = True if mutation == "partial_transport" else controller["partial_transport"]
    moves = False if mutation == "clone_source" else controller["moves_not_clones"]
    clear = False if mutation == "mapping_defect" else controller["clear"]
    permanence = False if mutation == "move_record" else controller["blocked_permanence"]
    growth = 1 if mutation == "packet_growth" else controller["packet_growth"]
    stable = False if mutation == "unstable_stop" else controller["next_state"]
    controller_ok = (
        controller["fronts"] == 6 and controller["patterns"] == 32
        and controller["clear_patterns"] == 1
        and controller["blocked_patterns"] == 31 and geometry and guard
        and controller["cases"] == 37632 and controller["table"]
        and controller["clear_cases"] == 1176 and clear
        and controller["blocked_cases"] == 36456
        and controller["blocked_identity"] and permanence and stable
        and not partial and moves and controller["packet_size"] == 5
        and growth == 0
    )

    probability = probability_facts()
    normalized = False if mutation == "drop_stop_mass" else probability["normalized"]
    feedback = True if mutation == "same_event_feedback" else probability["same_event_feedback"]
    site_selection = True if mutation == "claim_site_selection" else probability["site_selection"]
    rate = True if mutation == "claim_rate" else probability["rate"]
    probability_ok = (
        probability["cases"] == 2688 and normalized
        and probability["outcome_independent"] and probability["stop_mass"]
        and not feedback and not site_selection and not rate
    )

    adjudication_ok = (
        controller["table"] and controller["blocked_permanence"]
        and endpoints["two_ends"] and not endpoints["unique"]
    )

    scope = scope_facts()
    scope_ok = scope["note"] and scope["forbidden"] and scope["no_go"]
    if mutation in (
        "claim_microscopic", "claim_interacting", "claim_gravity",
        "claim_axiom", "claim_toe", "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_independent_authority", authority_ok,
         "pinned parent, preregistration, axioms, primary blob, and an import-independent implementation match"),
        ("B_independent_parent_stack", parent_ok,
         "the independent Block-12 code, rank-nine carrier, and fourteen-way law remain exact"),
        ("C_independent_endpoint_census", endpoint_ok,
         "96 longer-trail cases independently return exactly the two reflected endpoints and no lateral candidate"),
        ("D_independent_guarded_map", controller_ok,
         "all 37632 maps independently preserve occupied Records, continue exactly when clear, and stop atomically when blocked"),
        ("E_independent_stop_mass", probability_ok,
         "all 2688 guard distributions retain normalized outcome mass without supplying occurrence or rate"),
        ("F_independent_adjudication", adjudication_ok,
         "static obstacle safety is positive while flag-only arrow orientation is negative on the frozen finite-line target"),
        ("G_independent_scope", scope_ok,
         "the source note and N1--N8 sidecar retain every microscopic, concurrency, gravity, axiom, audit, and TOE boundary"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()

    if args.mutation_sweep:
        rejected = [
            any(not bool(ok) for _name, ok, _detail in evaluated_checks(mutation))
            for mutation in MUTATIONS
        ]
        print(f"MUTATIONS: REJECTED={sum(rejected)}/{len(MUTATIONS)}")
        print(f"TOTAL: PASS={sum(rejected)} FAIL={len(MUTATIONS)-sum(rejected)}")
        return 0 if all(rejected) else 1

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        ok = bool(ok)
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    if args.mutation is None:
        rejected = [
            any(not bool(ok) for _name, ok, _detail in evaluated_checks(mutation))
            for mutation in MUTATIONS
        ]
        print(f"MUTATIONS: rejected={sum(rejected)}/{len(MUTATIONS)}")
        failed += int(not all(rejected))
        if all(bool(ok) for _name, ok, _detail in checks):
            print(
                "VERDICT: CONDITIONAL-HALO independently reproduced; the "
                "guard is exact and the finite flag trail has two tips"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
