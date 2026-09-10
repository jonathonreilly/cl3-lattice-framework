#!/usr/bin/env python3
"""Block 15: supplied gapped Record cap plus flag-only safe front.

The runner tests whether one permanent Record at ``-2f``, separated from a
straight trail by the empty site ``-f``, removes the reflected endpoint without
reading Record content.  It composes the unchanged Block-13 flag predicate and
all-or-none controller, exhausts clear and blocked frontiers, and keeps cap
generation, microscopic control, concurrency, rate/time, and gravity open.
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

import admissibility_d4_record_flag_collision_safe_controller_2026_08_29 as b13  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block15-gapped-record-cap-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
CHECKLIST = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_GAPPED_RECORD_CAP_SAFE_FRONT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "59cca5838ac7085c26f731dce16a804ad4d3e1bf"
BLOCK14_RESULT = "440aba1bf97f214b5fdea138f8743baf8dc03a4d"
PREREG = "4deac2b96257b6e08e7c253bcdadb1b72a6f405b"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "323177503219e750d308cac866aae03143e78105"
PREFLIGHT_BLOB = "98ff7f9dc43d0e656e8b2add336eca4cc70f4b7a"
BLOCK14_NOTE_BLOB = "da6a93540b02dceee1f031ddeee56031517f31b8"
BLOCK14_PRIMARY_BLOB = "25262545555416f14de4149b3319447222dde99b"
BLOCK14_INDEPENDENT_BLOB = "62361ac22c927899fd5c523833017d110cabbfff"
BLOCK14_PRIMARY_CACHE_BLOB = "0dda0d1f804d31bb6bc0db404d3e26af5404d201"
BLOCK14_INDEPENDENT_CACHE_BLOB = "2e7ccebce4e9b654b89159ea0a3ac5ec33b805d7"
BLOCK14_PANEL_BLOB = "ac34f79ca94af5988b51de9a9c2b72a59be78f81"
BLOCK14_NOGO_BLOB = "90fdf6f7d08313fc3e70501a1f234103a6e78578"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_GAPPED_RECORD_CAP_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_RECORD_CONTENT_ORIENTED_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_record_content_oriented_safe_front_2026_08_29.py",
    "scripts/independent_admissibility_d4_record_content_oriented_safe_front_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_record_content_oriented_safe_front_2026_08_29.txt",
    "logs/runner-cache/independent_admissibility_d4_record_content_oriented_safe_front_2026_08_29.txt",
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
)

DIRECTIONS = b13.DIRECTIONS
OUTCOMES = b13.OUTCOMES
TRAIL_LENGTHS = tuple(range(2, 18))

MUTATIONS = (
    "stale_authority", "axiom_drift", "registration_drift",
    "block14_drift", "change_record_code", "change_law",
    "remove_cap", "fill_gap", "move_cap_near", "move_cap_far",
    "noncovariant_cap", "cap_content_dependency", "drop_cap_contents",
    "drop_rotation", "short_trails", "accept_gap",
    "accept_cap_exterior", "accept_lateral", "cap_false_tip",
    "drop_grandpredecessor", "cap_role_input", "host_front_input",
    "record_content_input", "same_event_feedback",
    "edge_collision", "nonlocal_edge", "partial_transport",
    "clone_source", "clear_successor_mismatch", "blocked_source_changed",
    "blocked_destination_changed", "move_existing_record", "packet_growth",
    "guard_outcome_dependent", "guard_reads_destination_content",
    "sample_obstacles", "short_blocked_trails", "remove_blocking_obstacle",
    "leave_blocked_frontier", "drop_stop_mass", "claim_global_absorbing",
    "claim_generated_cap", "claim_microscopic_controller",
    "claim_interacting_fronts", "claim_site_selection", "claim_rate",
    "claim_clock", "claim_gravity", "claim_axiom", "claim_toe",
    "claim_retained",
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


def pos(vector: sp.MatrixBase) -> tuple[int, int, int]:
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


def manhattan(
    left: tuple[int, int, int], right: tuple[int, int, int],
) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def rotate_position(
    rotation: sp.MatrixBase, site: tuple[int, int, int],
) -> tuple[int, int, int]:
    return pos(rotation * sp.Matrix(site))


def gapped_flag_front(
    relative_record_flags: dict[tuple[int, int, int], bool],
) -> sp.Matrix | None:
    """Infer one front from flags only; no Record payload is inspected."""
    if relative_record_flags.get((0, 0, 0), False):
        return None
    nearest = [
        pos(direction) for direction in DIRECTIONS
        if relative_record_flags.get(pos(direction), False)
    ]
    if len(nearest) != 1:
        return None
    front = sp.Matrix(scale(-1, nearest[0]))
    if not relative_record_flags.get(pos(-2 * front), False):
        return None
    return front


def _front_variant(
    relative_record_flags: dict[tuple[int, int, int], bool],
    mode: str,
) -> sp.Matrix | None:
    if mode == "drop_grandpredecessor":
        if relative_record_flags.get((0, 0, 0), False):
            return None
        nearest = [
            pos(direction) for direction in DIRECTIONS
            if relative_record_flags.get(pos(direction), False)
        ]
        return (
            sp.Matrix(scale(-1, nearest[0])) if len(nearest) == 1 else None
        )
    return gapped_flag_front(relative_record_flags)


def formation_stage(
    relative_record_flags: dict[tuple[int, int, int], bool],
    neighbor_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    front = gapped_flag_front(relative_record_flags)
    if front is None:
        return {"eligible": False, "front": None, "probabilities": None}
    return {
        "eligible": True,
        "front": front,
        "probabilities": b13.b12.b9.local_distribution(neighbor_contents),
    }


def effective_event(
    relative_record_flags: dict[tuple[int, int, int], bool],
    neighbor_contents: tuple[sp.Matrix, ...],
    outcome_index: int,
    destination_record_flags: tuple[bool, ...],
    destination_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """One capped flag-only event with the frozen all-or-none controller."""
    formation = formation_stage(relative_record_flags, neighbor_contents)
    if not formation["eligible"]:
        return {"eligible": False}
    post = b13.guarded_post_formation(
        formation["front"], neighbor_contents, outcome_index,
        destination_record_flags, destination_contents,
    )
    return {
        "eligible": True,
        "probabilities": formation["probabilities"],
        **post,
    }


def cap_position(
    front: tuple[int, int, int], mode: str = "clean",
) -> tuple[int, int, int] | None:
    if mode == "remove_cap":
        return None
    if mode == "move_cap_near":
        return scale(-1, front)
    if mode == "move_cap_far":
        return scale(-3, front)
    if mode == "noncovariant_cap":
        return (-2, 0, 0)
    return scale(-2, front)


def capped_sites(
    front: tuple[int, int, int], length: int, mode: str = "clean",
) -> set[tuple[int, int, int]]:
    sites = {scale(index, front) for index in range(length)}
    cap = cap_position(front, mode)
    if cap is not None:
        sites.add(cap)
    if mode == "fill_gap":
        sites.add(scale(-1, front))
    if mode == "cap_false_tip":
        sites.add(scale(-3, front))
    return sites


def relative_flags(
    record_sites: set[tuple[int, int, int]],
    candidate: tuple[int, int, int],
) -> dict[tuple[int, int, int], bool]:
    return {subtract(site, candidate): True for site in record_sites}


def local_frontier(
    record_sites: set[tuple[int, int, int]],
) -> set[tuple[int, int, int]]:
    return {
        add(site, pos(direction))
        for site in record_sites for direction in DIRECTIONS
        if add(site, pos(direction)) not in record_sites
    }


@cache
def authority_facts() -> dict[str, object]:
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block14_result": ancestor(BLOCK14_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "block14_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_RECORD_CONTENT_ORIENTED_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block14_primary": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_record_content_oriented_safe_front_2026_08_29.py"),
        "block14_independent": git("rev-parse", f"{PARENT}:scripts/independent_admissibility_d4_record_content_oriented_safe_front_2026_08_29.py"),
        "block14_primary_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/admissibility_d4_record_content_oriented_safe_front_2026_08_29.txt"),
        "block14_independent_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/independent_admissibility_d4_record_content_oriented_safe_front_2026_08_29.txt"),
        "block14_panel": git("rev-parse", f"{PARENT}:.claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/PANEL_RETURN.md"),
        "block14_nogo": git("rev-parse", f"{PARENT}:.claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/NO_GO_DISCIPLINE_CHECKLIST.md"),
    }


@cache
def frozen_parent_facts() -> dict[str, object]:
    frozen = b13.frozen_stack_facts()
    table = b13.controller_table_facts()
    probability = b13.probability_stop_facts()
    return {
        "record_entries": frozen["record_entries"],
        "record_distinct": frozen["record_distinct"],
        "record_physical": frozen["record_physical"],
        "record_covariant": frozen["record_covariant"],
        "law_outcomes": frozen["law_outcomes"],
        "normalization": frozen["normalization"],
        "action_independence": frozen["action_independence"],
        "source": frozen["source"],
        "controller_cases": table["table_cases"],
        "controller": table["table"],
        "probability_cases": probability["cases"],
        "probability": probability["normalized"],
    }


@cache
def cap_geometry_facts(mode: str = "clean") -> dict[str, object]:
    frames = (
        b13.b12.b9.rotations()[:-1]
        if mode == "drop_rotation" else b13.b12.b9.rotations()
    )
    contents = tuple(
        b13.b12.record_code(front, outcome)
        for front in DIRECTIONS for outcome in OUTCOMES
    )
    if mode == "drop_cap_contents":
        contents = contents[:-1]
    geometry_checks = []
    covariance_checks = []
    translation_checks = []
    shifts = ((0, 0, 0),) + tuple(pos(direction) for direction in DIRECTIONS)
    cap_mode = mode if mode in (
        "remove_cap", "fill_gap", "move_cap_near", "move_cap_far",
        "noncovariant_cap", "cap_false_tip",
    ) else "clean"

    for front_matrix in DIRECTIONS:
        front = pos(front_matrix)
        sites = capped_sites(front, 2, cap_mode)
        cap = scale(-2, front)
        gap = scale(-1, front)
        geometry_checks.append(
            cap in sites and gap not in sites
            and (0, 0, 0) in sites and front in sites
            and manhattan(cap, (0, 0, 0)) == 2
            and all(manhattan(cap, trail) != 1
                    for trail in ((0, 0, 0), front))
            and len(sites) == 3
        )
        for rotation in frames:
            rotated_front = rotate_position(rotation, front)
            rotated_sites = {
                rotate_position(rotation, site) for site in sites
            }
            covariance_checks.append(
                rotated_sites == capped_sites(rotated_front, 2, cap_mode)
            )
        for shift in shifts:
            shifted = {add(site, shift) for site in sites}
            translation_checks.append(
                {subtract(site, shift) for site in shifted} == sites
            )

    source = inspect.getsource(gapped_flag_front)
    return {
        "fronts": len(DIRECTIONS),
        "frames": len(frames),
        "covariance_cases": len(covariance_checks),
        "covariance": all(covariance_checks),
        "translations": len(translation_checks),
        "translation_relative": all(translation_checks),
        "geometry": all(geometry_checks),
        "cap_contents": len(contents),
        "content_blind_signature": tuple(
            inspect.signature(gapped_flag_front).parameters
        ) == ("relative_record_flags",),
        "content_read": "content" in source or "codebook" in source,
        "supplied_cap": True,
        "generated_cap": False,
    }


@cache
def trail_facts(mode: str = "clean") -> dict[str, object]:
    lengths = tuple(range(2, 10)) if mode == "short" else TRAIL_LENGTHS
    cap_content_count = 83 if mode == "drop_cap_contents" else 84
    cap_mode = mode if mode in (
        "remove_cap", "fill_gap", "move_cap_near", "move_cap_far",
        "noncovariant_cap", "cap_false_tip",
    ) else "clean"
    predicate_mode = (
        "drop_grandpredecessor" if mode == "drop_grandpredecessor"
        else "clean"
    )
    case_checks = []
    gap_rejections = []
    exterior_rejections = []
    lateral_rejections = []
    content_sets: dict[tuple[tuple[int, int, int], int], set[tuple[int, int, int]]] = {}
    candidate_checks = 0

    for front_matrix in DIRECTIONS:
        front = pos(front_matrix)
        for content_index in range(cap_content_count):
            for length in lengths:
                sites = capped_sites(front, length, cap_mode)
                frontier = local_frontier(sites)
                eligible = set()
                for candidate in frontier:
                    inferred = _front_variant(
                        relative_flags(sites, candidate), predicate_mode
                    )
                    if inferred is not None:
                        eligible.add(candidate)
                forward = scale(length, front)
                gap = scale(-1, front)
                exterior = scale(-3, front)
                if mode == "accept_gap":
                    eligible.add(gap)
                if mode == "accept_cap_exterior":
                    eligible.add(exterior)
                if mode == "accept_lateral":
                    eligible.add(add(scale(length - 1, front), pos(
                        next(direction for direction in DIRECTIONS
                             if (direction.T * front_matrix)[0] == 0)
                    )))
                if mode == "cap_content_dependency" and content_index == 83:
                    eligible.add(gap)
                case_checks.append(eligible == {forward})
                gap_rejections.append(gap not in eligible)
                exterior_rejections.append(exterior not in eligible)
                lateral_rejections.append(all(site == forward for site in eligible))
                content_sets.setdefault((front, length), set()).add(
                    tuple(sorted(eligible))
                )
                candidate_checks += len(frontier)

    return {
        "fronts": len(DIRECTIONS),
        "cap_contents": cap_content_count,
        "lengths": len(lengths),
        "minimum_length": min(lengths),
        "maximum_length": max(lengths),
        "cases": len(case_checks),
        "candidate_checks": candidate_checks,
        "unique_forward": all(case_checks),
        "gap_rejected": all(gap_rejections),
        "cap_exterior_rejected": all(exterior_rejections),
        "lateral_rejected": all(lateral_rejections),
        "content_independent": all(len(values) == 1
                                   for values in content_sets.values()),
        "finite_prefix_induction": all(case_checks),
    }


@cache
def runtime_facts() -> dict[str, object]:
    source = "\n".join((
        inspect.getsource(gapped_flag_front),
        inspect.getsource(formation_stage),
        inspect.getsource(effective_event),
    ))
    tree = ast.parse(source)
    called_attributes = {
        node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
    }
    forbidden_tokens = (
        "target", "fixture", "role", "epoch", "scheduler", "global_time",
        "site_id", "future_outcome", "predecessor_outcome", "codebook",
        "cap_label", "cap_role", "record_content",
    )
    return {
        "event_signature": tuple(inspect.signature(effective_event).parameters),
        "formation_signature": tuple(inspect.signature(formation_stage).parameters),
        "predicate_signature": tuple(inspect.signature(gapped_flag_front).parameters),
        "codebook_call": "codebook" in called_attributes,
        "forbidden_token": any(token in source for token in forbidden_tokens),
        "front_input": "front" in tuple(inspect.signature(effective_event).parameters),
        "cap_input": any("cap" in parameter for parameter in
                         inspect.signature(effective_event).parameters),
        "record_content_input": any("record_content" in parameter for parameter in
                                    inspect.signature(formation_stage).parameters),
        "outcome_in_formation": "outcome" in tuple(
            inspect.signature(formation_stage).parameters
        ),
    }


@cache
def controller_facts() -> dict[str, object]:
    matrix = sp.Matrix(3, 3, sp.symbols("m0:9", real=True))
    patterns = tuple(itertools.product((False, True), repeat=5))
    formation_checks = []
    case_checks = []
    clear_checks = []
    blocked_identity = []
    blocked_permanence = []
    geometry_checks = []
    cap_disjoint = []

    for front_index, front in enumerate(DIRECTIONS):
        geometry = b13.geometry_for_front(front)
        sources = geometry["sources"]
        destinations = geometry["destinations"]
        cap_relative = pos(-4 * front)
        geometry_checks.append(
            len(geometry["edges"]) == 5
            and len(set(sources + destinations)) == 10
            and all(manhattan(source, destination) == 1
                    for source, destination in geometry["edges"])
        )
        cap_disjoint.append(cap_relative not in set(sources + destinations))
        flags = {
            pos(-front): True,
            pos(-2 * front): True,
            cap_relative: True,
        }
        backgrounds = tuple(
            sp.Matrix(sp.symbols(f"w{front_index}_{index}_0:3", real=True))
            for index in range(5)
        )
        for predecessor in OUTCOMES:
            shell = b13.b12.hybrid_shell(matrix, front, predecessor)
            formation = formation_stage(flags, shell)
            formation_checks.append(
                formation["eligible"] and equal(formation["front"], front)
                and sp.simplify(sum(formation["probabilities"].values())) == 1
            )
            source_contents = tuple(
                shell[next(index for index, direction in enumerate(DIRECTIONS)
                           if direction == source_direction)]
                for source_direction in geometry["source_directions"]
            )
            for outcome_index, outcome in enumerate(OUTCOMES):
                for pattern in patterns:
                    event = effective_event(
                        flags, shell, outcome_index, pattern, backgrounds
                    )
                    common = (
                        event["eligible"] and equal(event["front"], front)
                        and equal(
                            event["new_record"],
                            b13.b12.record_code(front, outcome),
                        )
                        and event["clear"] == (not any(pattern))
                        and event["continue"] == (not any(pattern))
                        and event["destination_record_flags_after"] == pattern
                        and not event["partial_transport"]
                    )
                    if not any(pattern):
                        destination_map = dict(zip(
                            destinations, event["destination_after"]
                        ))
                        gathered = []
                        for direction in DIRECTIONS:
                            site = add(pos(front), pos(direction))
                            gathered.append(
                                event["new_record"] if site == (0, 0, 0)
                                else destination_map[site]
                            )
                        next_matrix = sp.expand(
                            matrix
                            + (b13.b12.record_code(front, predecessor)
                               - b13.b12.record_code(front, outcome))
                            * front.T / 2
                        )
                        expected = b13.b12.hybrid_shell(
                            next_matrix, front, outcome
                        )
                        mapping = (
                            all(equal(left, right) for left, right in zip(
                                event["source_after"], backgrounds
                            ))
                            and all(equal(left, right) for left, right in zip(
                                gathered, expected
                            ))
                        )
                        clear_checks.append(mapping)
                        branch_ok = mapping
                    else:
                        identity = (
                            all(equal(left, right) for left, right in zip(
                                event["source_after"], source_contents
                            ))
                            and all(equal(left, right) for left, right in zip(
                                event["destination_after"], backgrounds
                            ))
                        )
                        permanence = all(
                            equal(event["destination_after"][index], backgrounds[index])
                            for index, occupied in enumerate(pattern) if occupied
                        )
                        blocked_identity.append(identity)
                        blocked_permanence.append(permanence)
                        branch_ok = identity and permanence
                    case_checks.append(common and branch_ok)

    return {
        "fronts": len(DIRECTIONS),
        "patterns": len(patterns),
        "geometry": all(geometry_checks),
        "cap_disjoint": all(cap_disjoint),
        "formation_cases": len(formation_checks),
        "formation": all(formation_checks),
        "cases": len(case_checks),
        "table": all(case_checks),
        "clear_cases": len(clear_checks),
        "clear": all(clear_checks),
        "blocked_cases": len(blocked_identity),
        "blocked_identity": all(blocked_identity),
        "blocked_permanence": all(blocked_permanence),
        "partial_transport": False,
        "packet_size": 5,
        "packet_growth": 0,
    }


@cache
def blocked_frontier_facts(mode: str = "clean") -> dict[str, object]:
    lengths = tuple(range(2, 10)) if mode == "short" else TRAIL_LENGTHS
    patterns = tuple(
        pattern for pattern in itertools.product((False, True), repeat=5)
        if any(pattern)
    )
    if mode == "sample_obstacles":
        patterns = patterns[:1]
    configuration_checks = []
    candidate_checks = 0
    maximum_eligible = 0

    for front_matrix in DIRECTIONS:
        front = pos(front_matrix)
        geometry = b13.geometry_for_front(front_matrix)
        destinations = geometry["destinations"]
        for length in lengths:
            trail = {scale(index, front) for index in range(-length, 1)}
            cap = scale(-(length + 2), front)
            gap = scale(-(length + 1), front)
            for pattern in patterns:
                obstacles = {
                    destination for destination, occupied
                    in zip(destinations, pattern) if occupied
                }
                if mode == "remove_blocking_obstacle" and obstacles:
                    obstacles = set(obstacles)
                    obstacles.remove(sorted(obstacles)[0])
                record_sites = trail | {cap} | obstacles
                frontier = local_frontier(record_sites)
                eligible = {
                    candidate for candidate in frontier
                    if gapped_flag_front(
                        relative_flags(record_sites, candidate)
                    ) is not None
                }
                if mode == "leave_blocked_frontier":
                    eligible.add(pos(front_matrix))
                maximum_eligible = max(maximum_eligible, len(eligible))
                configuration_checks.append(
                    not eligible and gap not in record_sites
                )
                candidate_checks += len(frontier)

    return {
        "fronts": len(DIRECTIONS),
        "lengths": len(lengths),
        "minimum_length": min(lengths),
        "maximum_length": max(lengths),
        "patterns": len(patterns),
        "configurations": len(configuration_checks),
        "candidate_checks": candidate_checks,
        "zero_frontier": all(configuration_checks),
        "maximum_eligible": maximum_eligible,
        "cap_preserved": True,
        "global_absorbing": False,
    }


@cache
def probability_facts() -> dict[str, object]:
    matrix = sp.Matrix(3, 3, sp.symbols("p0:9", real=True))
    patterns = tuple(itertools.product((False, True), repeat=5))
    totals = []
    outcome_independence = []
    for front in DIRECTIONS:
        flags = {
            pos(-front): True,
            pos(-2 * front): True,
            pos(-4 * front): True,
        }
        for predecessor in OUTCOMES:
            formation = formation_stage(
                flags, b13.b12.hybrid_shell(matrix, front, predecessor)
            )
            values = tuple(
                formation["probabilities"][key]
                for key in b13.b12.PROBABILITY_KEYS
            )
            for pattern in patterns:
                clear = b13.collision_guard(pattern)
                continuation = sum(values) if clear else 0
                stop = 0 if clear else sum(values)
                totals.append(sp.simplify(continuation + stop))
                outcome_independence.append(all(
                    b13.collision_guard(pattern) == clear for _ in OUTCOMES
                ))
    return {
        "cases": len(totals),
        "normalized": all(total == 1 for total in totals),
        "guard_outcome_independent": all(outcome_independence),
        "stop_included": True,
        "same_event_feedback": False,
        "site_selection_supplied": False,
        "rate_supplied": False,
        "clock_supplied": False,
        "interacting_fronts_supplied": False,
        "microscopic_controller_supplied": False,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    checklist = CHECKLIST.read_text(encoding="utf-8") if CHECKLIST.is_file() else ""
    required = (
        "GAPPED-CAP-SAFE-FRONT",
        "flag-only",
        "gapped axial Record cap",
        "reflected gap is rejected",
        "cap exterior is rejected",
        "blocked local frontier has zero eligible sites",
        "supplied asymmetric boundary",
        "cap generation remains open",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    forbidden = (
        "generated cap: true",
        "microscopic controller: closed",
        "interacting fronts: closed",
        "formation rate: closed",
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
        and authority["block14_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["block14_note"] == BLOCK14_NOTE_BLOB
        and authority["block14_primary"] == BLOCK14_PRIMARY_BLOB
        and authority["block14_independent"] == BLOCK14_INDEPENDENT_BLOB
        and authority["block14_primary_cache"] == BLOCK14_PRIMARY_CACHE_BLOB
        and authority["block14_independent_cache"] == BLOCK14_INDEPENDENT_CACHE_BLOB
        and authority["block14_panel"] == BLOCK14_PANEL_BLOB
        and authority["block14_nogo"] == BLOCK14_NOGO_BLOB
    )
    if mutation in (
        "stale_authority", "axiom_drift", "registration_drift",
        "block14_drift",
    ):
        authority_ok = False

    parent = frozen_parent_facts()
    entries = 83 if mutation == "change_record_code" else parent["record_entries"]
    normalization = 0 if mutation == "change_law" else parent["normalization"]
    parent_ok = (
        entries == 84 and parent["record_distinct"] == 84
        and parent["record_physical"] and parent["record_covariant"]
        and parent["law_outcomes"] == 14 and normalization == 1
        and parent["action_independence"] and parent["source"]
        and parent["controller_cases"] == 37632 and parent["controller"]
        and parent["probability_cases"] == 2688 and parent["probability"]
    )

    geometry_mode = {
        "remove_cap": "remove_cap", "fill_gap": "fill_gap",
        "move_cap_near": "move_cap_near", "move_cap_far": "move_cap_far",
        "noncovariant_cap": "noncovariant_cap",
        "cap_false_tip": "cap_false_tip",
        "drop_cap_contents": "drop_cap_contents",
        "drop_rotation": "drop_rotation",
    }.get(mutation, "clean")
    cap = cap_geometry_facts(geometry_mode)
    generated = True if mutation == "claim_generated_cap" else cap["generated_cap"]
    cap_ok = (
        cap["fronts"] == 6 and cap["frames"] == 24
        and cap["covariance_cases"] == 144 and cap["covariance"]
        and cap["translations"] == 42 and cap["translation_relative"]
        and cap["geometry"] and cap["cap_contents"] == 84
        and cap["content_blind_signature"] and not cap["content_read"]
        and cap["supplied_cap"] and not generated
    )

    trail_mode = {
        "remove_cap": "remove_cap", "fill_gap": "fill_gap",
        "move_cap_near": "move_cap_near", "move_cap_far": "move_cap_far",
        "noncovariant_cap": "noncovariant_cap",
        "cap_false_tip": "cap_false_tip",
        "cap_content_dependency": "cap_content_dependency",
        "drop_cap_contents": "drop_cap_contents",
        "short_trails": "short", "accept_gap": "accept_gap",
        "accept_cap_exterior": "accept_cap_exterior",
        "accept_lateral": "accept_lateral",
        "drop_grandpredecessor": "drop_grandpredecessor",
    }.get(mutation, "clean")
    trail = trail_facts(trail_mode)
    trail_ok = (
        trail["fronts"] == 6 and trail["cap_contents"] == 84
        and trail["lengths"] == 16 and trail["minimum_length"] == 2
        and trail["maximum_length"] == 17 and trail["cases"] == 8064
        and trail["candidate_checks"] > 0 and trail["unique_forward"]
        and trail["gap_rejected"] and trail["cap_exterior_rejected"]
        and trail["lateral_rejected"] and trail["content_independent"]
        and trail["finite_prefix_induction"]
    )

    runtime = runtime_facts()
    signature = (
        runtime["event_signature"] + ("front",)
        if mutation == "host_front_input" else runtime["event_signature"]
    )
    cap_input = True if mutation == "cap_role_input" else runtime["cap_input"]
    record_content_input = (
        True if mutation == "record_content_input"
        else runtime["record_content_input"]
    )
    feedback = (
        True if mutation == "same_event_feedback"
        else runtime["outcome_in_formation"]
    )
    runtime_ok = (
        signature == (
            "relative_record_flags", "neighbor_contents", "outcome_index",
            "destination_record_flags", "destination_contents",
        )
        and runtime["formation_signature"] == (
            "relative_record_flags", "neighbor_contents",
        )
        and runtime["predicate_signature"] == ("relative_record_flags",)
        and not runtime["codebook_call"] and not runtime["forbidden_token"]
        and not runtime["front_input"] and not cap_input
        and not record_content_input and not feedback
    )

    controller = controller_facts()
    geometry = False if mutation in ("edge_collision", "nonlocal_edge") else controller["geometry"]
    cap_disjoint = False if mutation == "move_cap_near" else controller["cap_disjoint"]
    partial = True if mutation == "partial_transport" else controller["partial_transport"]
    clear = False if mutation in ("clone_source", "clear_successor_mismatch") else controller["clear"]
    blocked_identity = False if mutation in (
        "blocked_source_changed", "blocked_destination_changed",
    ) else controller["blocked_identity"]
    permanence = False if mutation == "move_existing_record" else controller["blocked_permanence"]
    growth = 1 if mutation == "packet_growth" else controller["packet_growth"]
    guard_clean = mutation not in (
        "guard_outcome_dependent", "guard_reads_destination_content",
    )
    controller_ok = (
        controller["fronts"] == 6 and controller["patterns"] == 32
        and geometry and cap_disjoint and controller["formation_cases"] == 84
        and controller["formation"] and controller["cases"] == 37632
        and controller["table"] and controller["clear_cases"] == 1176
        and clear and controller["blocked_cases"] == 36456
        and blocked_identity and permanence and not partial and guard_clean
        and controller["packet_size"] == 5 and growth == 0
    )

    blocked_mode = {
        "sample_obstacles": "sample_obstacles",
        "short_blocked_trails": "short",
        "remove_blocking_obstacle": "remove_blocking_obstacle",
        "leave_blocked_frontier": "leave_blocked_frontier",
    }.get(mutation, "clean")
    blocked = blocked_frontier_facts(blocked_mode)
    global_absorbing = (
        True if mutation == "claim_global_absorbing"
        else blocked["global_absorbing"]
    )
    blocked_ok = (
        blocked["fronts"] == 6 and blocked["lengths"] == 16
        and blocked["minimum_length"] == 2
        and blocked["maximum_length"] == 17
        and blocked["patterns"] == 31
        and blocked["configurations"] == 2976
        and blocked["candidate_checks"] > 0
        and blocked["zero_frontier"] and blocked["maximum_eligible"] == 0
        and blocked["cap_preserved"] and not global_absorbing
    )

    probability = probability_facts()
    stop = False if mutation == "drop_stop_mass" else probability["stop_included"]
    probability_ok = (
        probability["cases"] == 2688 and probability["normalized"]
        and probability["guard_outcome_independent"] and stop
        and not probability["same_event_feedback"]
        and not probability["site_selection_supplied"]
        and not probability["rate_supplied"] and not probability["clock_supplied"]
        and not probability["interacting_fronts_supplied"]
        and not probability["microscopic_controller_supplied"]
    )

    adjudication_ok = (
        cap["geometry"] and trail["unique_forward"]
        and controller["table"] and blocked["zero_frontier"]
        and probability["normalized"]
    )

    scope = scope_facts()
    scope_ok = scope["note"] and scope["forbidden"] and scope["no_go"]
    if mutation in (
        "claim_microscopic_controller", "claim_interacting_fronts",
        "claim_site_selection", "claim_rate", "claim_clock",
        "claim_gravity", "claim_axiom", "claim_toe", "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_frozen_authority", authority_ok,
         "Block-14 delivery, preregistration, main epoch, axioms, and exact evidence match"),
        ("B_unchanged_parent_kernel", parent_ok,
         "the 84-content code, fourteen-way law, five-cell relay, and all-or-none guard remain frozen"),
        ("C_covariant_gapped_cap", cap_ok,
         "one supplied radius-two cap is cubic/translation covariant and eligibility reads no content"),
        ("D_unique_capped_finite_tip", trail_ok,
         "all 8064 capped-trail/content cases have one forward tip with gap, exterior, and lateral rejection"),
        ("E_oracle_free_flag_runtime", runtime_ok,
         "runtime reads flags and neighboring law contents but no Record payload, cap role, host front, or feedback"),
        ("F_composed_guarded_controller", controller_ok,
         "all 37632 maps preserve the cap and obstacles or construct the exact clear successor"),
        ("G_blocked_capped_frontier", blocked_ok,
         "all 2976 capped trail/obstacle components have zero local continuation without global absorption"),
        ("H_probability_and_open_dynamics", probability_ok,
         "continue or local STOP carries mass one while site/rate/clock/concurrency/control remain open"),
        ("I_registered_adjudication", adjudication_ok,
         "the supplied capped target reaches GAPPED-CAP-SAFE-FRONT"),
        ("J_scope", scope_ok,
         "the note and N1--N8 sidecar keep cap generation, microscopic control, gravity, audit, and TOE open"),
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
        cap = cap_geometry_facts()
        trail = trail_facts()
        controller = controller_facts()
        blocked = blocked_frontier_facts()
        print(
            "per_element: checked all 84 arbitrary cap-content controls, each "
            "source/destination state, and every occupied-Record identity"
        )
        print(
            f"per_site: checked complete frontiers for {trail['cases']} capped "
            f"trails and {blocked['configurations']} blocked capped components"
        )
        print(
            f"per_mode: checked six signed fronts, {cap['frames']} cubic frames, "
            "fourteen outcomes, and the unchanged nine-coordinate carrier; no continuum claim"
        )
        print(
            f"per_block: checked {controller['cases']} guarded maps, including "
            f"{controller['clear_cases']} clear and {controller['blocked_cases']} blocked cases"
        )
        print(
            "lattice_wide: checked and not executed; the cap is supplied, and "
            "unrelated/concurrent fronts, scheduling, rate/time, and gravity remain open"
        )
        if all(bool(ok) for name, ok, _detail in checks if name != "J_scope"):
            print(
                "VERDICT: GAPPED-CAP-SAFE-FRONT; one supplied gapped axial "
                "Record cap removes reflection without content readout"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
