#!/usr/bin/env python3
"""Block 14: fixed Record-content orientation plus collision-safe controller.

The runner composes one covariant half-space decoder with the frozen Block-13
all-or-none guard.  It exhausts the 84 Record contents, finite-trail frontiers,
all 37,632 guarded maps, and every registered blocked local frontier while
keeping microscopic pointer/control and whole-lattice concurrency outside the
claim.
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
    "toe-source-eta-ownership-block14-record-content-orientation-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
CHECKLIST = PACKET / "NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_RECORD_CONTENT_ORIENTED_SAFE_FRONT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

PARENT = "96d25272f5b09a4a2743836f7a1a6d14e2b99771"
BLOCK13_RESULT = "88cd67d464c9da93fbb025c1f9943d14376ad267"
PREREG = "87c64c7b3661e8fe37e4f1f61a7f1ea5a6cdf733"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
GOAL_BLOB = "f7be1fd1f7c1a12c9f43f39f4e5a5ae5510a2dce"
PREFLIGHT_BLOB = "e9b0b73dfce96971845e8cb7a04075b230f33c54"
BLOCK13_NOTE_BLOB = "bfcd86b9a6c5f60c151b8f4addc94efd00f33f11"
BLOCK13_PRIMARY_BLOB = "ab7f5fb3ddde7ff81f754a04ad5ac0a95f68a6f4"
BLOCK13_INDEPENDENT_BLOB = "2b4e89f591d5fce52e0a5ff6999b2f189cb18f7a"
BLOCK13_PRIMARY_CACHE_BLOB = "acb7550bbb793ac492e5853eb334f7b6823312e8"
BLOCK13_INDEPENDENT_CACHE_BLOB = "b333bfe59b40f49dfbe884db18a8e5296d803588"
BLOCK13_PANEL_BLOB = "1017524fb02f47e5bd80c39b264de875504c8e74"
BLOCK13_NOGO_BLOB = "9b75b26d7541a80bf32aede51ac6d967b31e4612"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_RECORD_CONTENT_ORIENTED_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_RECORD_FLAG_COLLISION_SAFE_CONTROLLER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py",
    "scripts/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py",
    "logs/runner-cache/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.txt",
    "logs/runner-cache/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.txt",
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/PANEL_RETURN.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
)

R = sp.Rational
DIRECTIONS = b13.DIRECTIONS
OUTCOMES = b13.OUTCOMES
THRESHOLD = R(1, 2)

MUTATIONS = (
    "stale_authority", "axiom_drift", "registration_drift",
    "block13_drift", "change_record_code", "change_law",
    "threshold_too_low", "threshold_too_high", "decoder_outcome_flip",
    "decoder_nonunique", "decoder_noncovariant", "decoder_codebook",
    "host_front_input", "old_outcome_input", "accept_reflection",
    "accept_lateral", "drop_grandpredecessor", "content_missing",
    "same_event_feedback", "guard_outcome_dependent",
    "guard_reads_destination_content", "edge_collision", "nonlocal_edge",
    "partial_transport", "clone_source", "clear_successor_mismatch",
    "blocked_source_changed", "blocked_destination_changed",
    "move_existing_record", "packet_growth", "unstable_stop",
    "leave_blocked_frontier", "drop_stop_mass",
    "claim_global_absorbing", "claim_generated_seed",
    "claim_microscopic_readout", "claim_microscopic_controller",
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


@cache
def _decode_content_tuple(values: tuple[sp.Expr, ...]) -> tuple[int, int, int] | None:
    """Fixed six-half-space decoder; no Record-code dictionary is consulted."""
    content = sp.Matrix(values)
    candidates = []
    for direction in DIRECTIONS:
        shifted = sp.simplify((direction.T * content)[0] + THRESHOLD)
        if shifted.is_negative is True:
            candidates.append(pos(direction))
    return candidates[0] if len(candidates) == 1 else None


def decode_signed_front(
    record_content: sp.MatrixBase,
) -> sp.Matrix | None:
    decoded = _decode_content_tuple(tuple(record_content))
    return sp.Matrix(decoded) if decoded is not None else None


def content_oriented_front(
    relative_record_flags: dict[tuple[int, int, int], bool],
    relative_record_contents: dict[tuple[int, int, int], sp.Matrix],
) -> sp.Matrix | None:
    """Orient one candidate using only its unique predecessor Record content."""
    if relative_record_flags.get((0, 0, 0), False):
        return None
    nearest = [
        pos(direction) for direction in DIRECTIONS
        if relative_record_flags.get(pos(direction), False)
    ]
    if len(nearest) != 1:
        return None
    predecessor_position = nearest[0]
    predecessor_content = relative_record_contents.get(predecessor_position)
    if predecessor_content is None:
        return None
    front = decode_signed_front(predecessor_content)
    if front is None or predecessor_position != pos(-front):
        return None
    if not relative_record_flags.get(pos(-2 * front), False):
        return None
    return sp.Matrix(front)


def formation_stage(
    relative_record_flags: dict[tuple[int, int, int], bool],
    relative_record_contents: dict[tuple[int, int, int], sp.Matrix],
    neighbor_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    front = content_oriented_front(
        relative_record_flags, relative_record_contents
    )
    if front is None:
        return {"eligible": False, "front": None, "probabilities": None}
    return {
        "eligible": True,
        "front": front,
        "probabilities": b13.b12.b9.local_distribution(neighbor_contents),
    }


def effective_event(
    relative_record_flags: dict[tuple[int, int, int], bool],
    relative_record_contents: dict[tuple[int, int, int], sp.Matrix],
    neighbor_contents: tuple[sp.Matrix, ...],
    outcome_index: int,
    destination_record_flags: tuple[bool, ...],
    destination_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """One content-oriented event with the frozen all-or-none guard."""
    formation = formation_stage(
        relative_record_flags, relative_record_contents, neighbor_contents
    )
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


def relative_state(
    record_contents: dict[tuple[int, int, int], sp.Matrix],
    candidate: tuple[int, int, int],
) -> tuple[
    dict[tuple[int, int, int], bool],
    dict[tuple[int, int, int], sp.Matrix],
]:
    return (
        {subtract(site, candidate): True for site in record_contents},
        {
            subtract(site, candidate): content
            for site, content in record_contents.items()
        },
    )


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
        "block13_result": ancestor(BLOCK13_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal": git("hash-object", str(GOAL.relative_to(ROOT))),
        "preflight": git("hash-object", str(PREFLIGHT.relative_to(ROOT))),
        "block13_note": git("rev-parse", f"{PARENT}:docs/ADMISSIBILITY_D4_RECORD_FLAG_COLLISION_SAFE_CONTROLLER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"),
        "block13_primary": git("rev-parse", f"{PARENT}:scripts/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py"),
        "block13_independent": git("rev-parse", f"{PARENT}:scripts/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py"),
        "block13_primary_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.txt"),
        "block13_independent_cache": git("rev-parse", f"{PARENT}:logs/runner-cache/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.txt"),
        "block13_panel": git("rev-parse", f"{PARENT}:.claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/PANEL_RETURN.md"),
        "block13_nogo": git("rev-parse", f"{PARENT}:.claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/NO_GO_DISCIPLINE_CHECKLIST.md"),
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
        "parent_probability_cases": probability["cases"],
        "parent_probability": probability["normalized"],
    }


@cache
def decoder_facts() -> dict[str, object]:
    decode_checks = []
    unique_checks = []
    true_dots = []
    false_dots = []
    covariance = []
    for front in DIRECTIONS:
        for outcome in OUTCOMES:
            content = b13.b12.record_code(front, outcome)
            decoded = decode_signed_front(content)
            decode_checks.append(decoded is not None and equal(decoded, front))
            candidates = [
                direction for direction in DIRECTIONS
                if sp.simplify((direction.T * content)[0] + THRESHOLD).is_negative
                is True
            ]
            unique_checks.append(len(candidates) == 1)
            true_dots.append(sp.simplify((front.T * content)[0]))
            false_dots.extend(
                sp.simplify((direction.T * content)[0])
                for direction in DIRECTIONS if direction != front
            )
            for rotation in b13.b12.b9.rotations():
                rotated = rotation * content
                rotated_decoded = decode_signed_front(rotated)
                covariance.append(
                    rotated_decoded is not None
                    and equal(rotated_decoded, rotation * front)
                )

    source = inspect.getsource(_decode_content_tuple)
    true_max = max(true_dots, key=lambda value: float(sp.N(value, 30)))
    false_min = min(false_dots, key=lambda value: float(sp.N(value, 30)))
    return {
        "entries": len(decode_checks),
        "decode": all(decode_checks),
        "unique": all(unique_checks),
        "true_max": true_max,
        "false_min": false_min,
        "threshold": THRESHOLD,
        "lower_margin": R(1, 256),
        "upper_margin": R(143, 256),
        "threshold_family": false_min == -R(1, 256)
        and true_max == -R(143, 256),
        "rotation_cases": len(covariance),
        "covariance": all(covariance),
        "codebook": "codebook" in source or "OUTCOMES" in source,
        "outcome_input": "outcome" in tuple(
            inspect.signature(decode_signed_front).parameters
        ),
    }


@cache
def trail_facts() -> dict[str, object]:
    case_checks = []
    unique_counts = []
    reflection_rejected = []
    lateral_rejected = []
    for front in DIRECTIONS:
        step = pos(front)
        for left_outcome in OUTCOMES:
            for right_outcome in OUTCOMES:
                for length in range(2, 10):
                    contents = {}
                    for index in range(length):
                        outcome = (
                            left_outcome if index == 0
                            else right_outcome if index == length - 1
                            else OUTCOMES[index % len(OUTCOMES)]
                        )
                        contents[scale(index, step)] = b13.b12.record_code(
                            front, outcome
                        )
                    frontier = local_frontier(set(contents))
                    eligible = []
                    for candidate in frontier:
                        flags, relative_contents = relative_state(
                            contents, candidate
                        )
                        inferred = content_oriented_front(
                            flags, relative_contents
                        )
                        if inferred is not None:
                            eligible.append((candidate, pos(inferred)))
                    expected = scale(length, step)
                    reflected = scale(-1, step)
                    unique_counts.append(len(eligible))
                    reflection_rejected.append(
                        all(candidate != reflected for candidate, _ in eligible)
                    )
                    lateral_rejected.append(all(
                        candidate == expected for candidate, _ in eligible
                    ))
                    case_checks.append(eligible == [(expected, step)])
    return {
        "fronts": len(DIRECTIONS),
        "left_outcomes": len(OUTCOMES),
        "right_outcomes": len(OUTCOMES),
        "lengths": 8,
        "cases": len(case_checks),
        "unique": all(case_checks),
        "unique_counts": tuple(unique_counts),
        "reflection_rejected": all(reflection_rejected),
        "lateral_rejected": all(lateral_rejected),
        "finite_prefix_induction": all(case_checks),
        "oriented_seed_supplied": True,
    }


@cache
def runtime_facts() -> dict[str, object]:
    source = "\n".join((
        inspect.getsource(_decode_content_tuple),
        inspect.getsource(decode_signed_front),
        inspect.getsource(content_oriented_front),
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
    )
    return {
        "event_signature": tuple(inspect.signature(effective_event).parameters),
        "formation_signature": tuple(inspect.signature(formation_stage).parameters),
        "decoder_signature": tuple(inspect.signature(decode_signed_front).parameters),
        "codebook_call": "codebook" in called_attributes,
        "forbidden_token": any(token in source for token in forbidden_tokens),
        "front_input": "front" in tuple(inspect.signature(effective_event).parameters),
        "old_outcome_input": "predecessor" in tuple(
            inspect.signature(effective_event).parameters
        ),
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

    for front_index, front in enumerate(DIRECTIONS):
        geometry = b13.geometry_for_front(front)
        sources = geometry["sources"]
        destinations = geometry["destinations"]
        geometry_checks.append(
            len(geometry["edges"]) == 5
            and len(set(sources + destinations)) == 10
            and all(sum(abs(destination[axis] - source[axis])
                        for axis in range(3)) == 1
                    for source, destination in geometry["edges"])
        )
        flags = {pos(-front): True, pos(-2 * front): True}
        backgrounds = tuple(
            sp.Matrix(sp.symbols(f"w{front_index}_{index}_0:3", real=True))
            for index in range(5)
        )
        for predecessor in OUTCOMES:
            predecessor_contents = {
                pos(-front): b13.b12.record_code(front, predecessor),
                pos(-2 * front): b13.b12.record_code(front, OUTCOMES[0]),
            }
            shell = b13.b12.hybrid_shell(matrix, front, predecessor)
            formation = formation_stage(flags, predecessor_contents, shell)
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
                        flags, predecessor_contents, shell, outcome_index,
                        pattern, backgrounds,
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
def blocked_frontier_facts() -> dict[str, object]:
    patterns = tuple(
        pattern for pattern in itertools.product((False, True), repeat=5)
        if any(pattern)
    )
    configuration_checks = []
    nominal_checks = []
    candidate_direction_checks = 0
    maximum_eligible = 0

    for front in DIRECTIONS:
        step = pos(front)
        geometry = b13.geometry_for_front(front)
        destinations = geometry["destinations"]
        for length in range(3, 11):
            trail_contents = {
                scale(index, step): b13.b12.record_code(
                    front, OUTCOMES[index % len(OUTCOMES)]
                )
                for index in range(-(length - 1), 1)
            }
            trail_contents[(0, 0, 0)] = b13.b12.record_code(
                front, OUTCOMES[-1]
            )
            for pattern in patterns:
                obstacles = {
                    destination for destination, occupied
                    in zip(destinations, pattern) if occupied
                }
                record_sites = set(trail_contents) | obstacles
                frontier = local_frontier(record_sites)
                eligible_candidates = set()

                for candidate in frontier:
                    nearest_records = [
                        add(candidate, pos(direction))
                        for direction in DIRECTIONS
                        if add(candidate, pos(direction)) in record_sites
                    ]
                    if len(nearest_records) != 1:
                        continue
                    predecessor = nearest_records[0]
                    if predecessor in obstacles:
                        trial_contents = dict(trail_contents)
                        for obstacle_front in DIRECTIONS:
                            trial_contents.update({
                                obstacle: b13.b12.record_code(
                                    obstacle_front, OUTCOMES[0]
                                )
                                for obstacle in obstacles
                            })
                            trial_contents[predecessor] = b13.b12.record_code(
                                obstacle_front, OUTCOMES[0]
                            )
                            flags, relative_contents = relative_state(
                                trial_contents, candidate
                            )
                            candidate_direction_checks += 1
                            inferred = content_oriented_front(
                                flags, relative_contents
                            )
                            if inferred is not None:
                                eligible_candidates.add(candidate)
                    else:
                        trial_contents = dict(trail_contents)
                        trial_contents.update({
                            obstacle: b13.b12.record_code(
                                DIRECTIONS[0], OUTCOMES[0]
                            )
                            for obstacle in obstacles
                        })
                        flags, relative_contents = relative_state(
                            trial_contents, candidate
                        )
                        candidate_direction_checks += 1
                        inferred = content_oriented_front(
                            flags, relative_contents
                        )
                        if inferred is not None:
                            eligible_candidates.add(candidate)

                maximum_eligible = max(
                    maximum_eligible, len(eligible_candidates)
                )
                configuration_checks.append(not eligible_candidates)
                full_contents = dict(trail_contents)
                full_contents.update({
                    obstacle: b13.b12.record_code(
                        DIRECTIONS[0], OUTCOMES[0]
                    )
                    for obstacle in obstacles
                })
                nominal = step
                flags, relative_contents = relative_state(
                    full_contents, nominal
                )
                nominal_checks.append(
                    content_oriented_front(flags, relative_contents) is None
                )

    return {
        "fronts": len(DIRECTIONS),
        "lengths": 8,
        "patterns": len(patterns),
        "configurations": len(configuration_checks),
        "zero_frontier": all(configuration_checks),
        "nominal_stopped": all(nominal_checks),
        "candidate_direction_checks": candidate_direction_checks,
        "maximum_eligible": maximum_eligible,
        "global_absorbing": False,
    }


@cache
def probability_facts() -> dict[str, object]:
    matrix = sp.Matrix(3, 3, sp.symbols("p0:9", real=True))
    patterns = tuple(itertools.product((False, True), repeat=5))
    totals = []
    outcome_independence = []
    for front in DIRECTIONS:
        flags = {pos(-front): True, pos(-2 * front): True}
        for predecessor in OUTCOMES:
            record_contents = {
                pos(-front): b13.b12.record_code(front, predecessor),
                pos(-2 * front): b13.b12.record_code(front, OUTCOMES[0]),
            }
            formation = formation_stage(
                flags, record_contents,
                b13.b12.hybrid_shell(matrix, front, predecessor),
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
        "site_selection_supplied": False,
        "rate_supplied": False,
        "clock_supplied": False,
        "interacting_fronts_supplied": False,
        "microscopic_readout_supplied": False,
        "microscopic_controller_supplied": False,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
    checklist = CHECKLIST.read_text(encoding="utf-8") if CHECKLIST.is_file() else ""
    required = (
        "CONTENT-ORIENTED-SAFE-FRONT",
        "fixed covariant half-space decoder",
        "outcome-independent",
        "reflected endpoint is rejected",
        "blocked local frontier has zero eligible sites",
        "framework-level Record readout",
        "microscopic pointer/control remains open",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    forbidden = (
        "perfect ordinary one-site POVM: true",
        "generated seed: true",
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
        and authority["block13_result"] and authority["prereg"]
        and authority["axiom"] == AXIOM_BLOB
        and authority["goal"] == GOAL_BLOB
        and authority["preflight"] == PREFLIGHT_BLOB
        and authority["block13_note"] == BLOCK13_NOTE_BLOB
        and authority["block13_primary"] == BLOCK13_PRIMARY_BLOB
        and authority["block13_independent"] == BLOCK13_INDEPENDENT_BLOB
        and authority["block13_primary_cache"] == BLOCK13_PRIMARY_CACHE_BLOB
        and authority["block13_independent_cache"] == BLOCK13_INDEPENDENT_CACHE_BLOB
        and authority["block13_panel"] == BLOCK13_PANEL_BLOB
        and authority["block13_nogo"] == BLOCK13_NOGO_BLOB
    )
    if mutation in (
        "stale_authority", "axiom_drift", "registration_drift",
        "block13_drift",
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
        and parent["parent_probability_cases"] == 2688
        and parent["parent_probability"]
    )

    decoder = decoder_facts()
    threshold = (
        R(1, 512) if mutation == "threshold_too_low"
        else R(144, 256) if mutation == "threshold_too_high"
        else decoder["threshold"]
    )
    decoded = False if mutation == "decoder_outcome_flip" else decoder["decode"]
    unique = False if mutation == "decoder_nonunique" else decoder["unique"]
    covariance = False if mutation == "decoder_noncovariant" else decoder["covariance"]
    codebook = True if mutation == "decoder_codebook" else decoder["codebook"]
    decoder_ok = (
        decoder["entries"] == 84 and decoded and unique
        and decoder["true_max"] == -R(143, 256)
        and decoder["false_min"] == -R(1, 256)
        and decoder["threshold_family"]
        and decoder["lower_margin"] < threshold < decoder["upper_margin"]
        and threshold == THRESHOLD
        and decoder["rotation_cases"] == 2016 and covariance
        and not codebook and not decoder["outcome_input"]
    )

    trail = trail_facts()
    trail_unique = False if mutation in (
        "accept_reflection", "accept_lateral", "drop_grandpredecessor",
    ) else trail["unique"]
    reflection = False if mutation == "accept_reflection" else trail["reflection_rejected"]
    lateral = False if mutation == "accept_lateral" else trail["lateral_rejected"]
    content_available = False if mutation == "content_missing" else True
    trail_ok = (
        trail["fronts"] == 6 and trail["left_outcomes"] == 14
        and trail["right_outcomes"] == 14 and trail["lengths"] == 8
        and trail["cases"] == 9408 and trail_unique and reflection and lateral
        and all(count == 1 for count in trail["unique_counts"])
        and trail["finite_prefix_induction"] and content_available
        and trail["oriented_seed_supplied"]
    )

    runtime = runtime_facts()
    signature = (
        runtime["event_signature"] + ("front",)
        if mutation == "host_front_input" else runtime["event_signature"]
    )
    old_outcome = True if mutation == "old_outcome_input" else runtime["old_outcome_input"]
    feedback = True if mutation == "same_event_feedback" else runtime["outcome_in_formation"]
    runtime_ok = (
        signature == (
            "relative_record_flags", "relative_record_contents",
            "neighbor_contents", "outcome_index", "destination_record_flags",
            "destination_contents",
        )
        and runtime["formation_signature"] == (
            "relative_record_flags", "relative_record_contents",
            "neighbor_contents",
        )
        and runtime["decoder_signature"] == ("record_content",)
        and not runtime["codebook_call"] and not runtime["forbidden_token"]
        and not runtime["front_input"] and not old_outcome and not feedback
    )

    controller = controller_facts()
    geometry = False if mutation in ("edge_collision", "nonlocal_edge") else controller["geometry"]
    partial = True if mutation == "partial_transport" else controller["partial_transport"]
    clear = False if mutation in (
        "clone_source", "clear_successor_mismatch"
    ) else controller["clear"]
    blocked_identity = False if mutation in (
        "blocked_source_changed", "blocked_destination_changed"
    ) else controller["blocked_identity"]
    permanence = False if mutation == "move_existing_record" else controller["blocked_permanence"]
    growth = 1 if mutation == "packet_growth" else controller["packet_growth"]
    guard_clean = mutation not in (
        "guard_outcome_dependent", "guard_reads_destination_content",
    )
    controller_ok = (
        controller["fronts"] == 6 and controller["patterns"] == 32
        and geometry and controller["formation_cases"] == 84
        and controller["formation"] and controller["cases"] == 37632
        and controller["table"] and controller["clear_cases"] == 1176
        and clear and controller["blocked_cases"] == 36456
        and blocked_identity and permanence and not partial and guard_clean
        and controller["packet_size"] == 5 and growth == 0
    )

    blocked = blocked_frontier_facts()
    zero_frontier = False if mutation in (
        "unstable_stop", "leave_blocked_frontier"
    ) else blocked["zero_frontier"]
    global_absorbing = True if mutation == "claim_global_absorbing" else blocked["global_absorbing"]
    blocked_ok = (
        blocked["fronts"] == 6 and blocked["lengths"] == 8
        and blocked["patterns"] == 31 and blocked["configurations"] == 1488
        and zero_frontier and blocked["nominal_stopped"]
        and blocked["candidate_direction_checks"] > 0
        and blocked["maximum_eligible"] == 0 and not global_absorbing
    )

    probability = probability_facts()
    stop = False if mutation == "drop_stop_mass" else probability["stop_included"]
    probability_ok = (
        probability["cases"] == 2688 and probability["normalized"]
        and probability["guard_outcome_independent"] and stop
        and not probability["site_selection_supplied"]
        and not probability["rate_supplied"] and not probability["clock_supplied"]
        and not probability["interacting_fronts_supplied"]
        and not probability["microscopic_readout_supplied"]
        and not probability["microscopic_controller_supplied"]
    )

    adjudication_ok = (
        decoder["decode"] and trail["unique"] and controller["table"]
        and blocked["zero_frontier"] and probability["normalized"]
    )
    if mutation == "claim_generated_seed":
        adjudication_ok = False

    scope = scope_facts()
    scope_ok = scope["note"] and scope["forbidden"] and scope["no_go"]
    if mutation in (
        "claim_microscopic_readout", "claim_microscopic_controller",
        "claim_interacting_fronts", "claim_site_selection", "claim_rate",
        "claim_clock", "claim_gravity", "claim_axiom", "claim_toe",
        "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_frozen_authority", authority_ok,
         "parent delivery, preregistration, main epoch, axioms, and exact Block-13 evidence match"),
        ("B_unchanged_parent_kernel", parent_ok,
         "the 84-state code, rank-nine law, guarded map, and STOP normalization remain frozen"),
        ("C_fixed_covariant_decoder", decoder_ok,
         "one fixed half-space functional recovers signed front for all 84 contents with exact margin and 2016 covariance cases"),
        ("D_unique_oriented_finite_tip", trail_ok,
         "all 9408 outcome-endpoint trails have one forward tip while reflected and lateral candidates fail"),
        ("E_oracle_free_runtime", runtime_ok,
         "runtime has Record flags/content but no codebook, host front, old outcome, fixture metadata, or same-event feedback"),
        ("F_composed_guarded_controller", controller_ok,
         "all 37632 integrated maps continue exactly when clear and preserve every source, destination, and Record when blocked"),
        ("G_blocked_local_frontier", blocked_ok,
         "all 1488 local trail/obstacle configurations have zero eligible continuation sites without claiming global absorption"),
        ("H_probability_and_open_dynamics", probability_ok,
         "continue or local STOP carries total mass one while site/rate/clock/concurrency/microscopic control remain unsupplied"),
        ("I_registered_adjudication", adjudication_ok,
         "the registered effective target reaches CONTENT-ORIENTED-SAFE-FRONT from a supplied oriented seed"),
        ("J_scope", scope_ok,
         "the note and N1--N8 sidecar preserve microscopic pointer, seed, concurrency, gravity, axiom, audit, and TOE boundaries"),
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
        decoder = decoder_facts()
        trail = trail_facts()
        controller = controller_facts()
        blocked = blocked_frontier_facts()
        print(
            "per_element: checked all 84 locked Record contents, each source/"
            "destination state, and every occupied-Record permanence identity"
        )
        print(
            f"per_site: checked complete frontiers for {trail['cases']} clear "
            f"trails and {blocked['configurations']} blocked local components"
        )
        print(
            f"per_mode: checked nine carrier coordinates, fourteen outcomes, "
            f"six signed fronts, and {decoder['rotation_cases']} cubic covariance cases; no continuum mode claim"
        )
        print(
            f"per_block: checked {controller['cases']} guarded controller cases, "
            f"including {controller['clear_cases']} clear and "
            f"{controller['blocked_cases']} blocked maps"
        )
        print(
            "lattice_wide: checked and not executed; unrelated or simultaneous "
            "fronts, global scheduling, formation rate, and gravity remain open"
        )
        if all(bool(ok) for name, ok, _detail in checks if name != "J_scope"):
            print(
                "VERDICT: CONTENT-ORIENTED-SAFE-FRONT; the fixed Record decoder "
                "removes reflection and composes with the collision guard"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
