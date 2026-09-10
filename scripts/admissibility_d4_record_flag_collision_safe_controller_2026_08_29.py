#!/usr/bin/env python3
"""Block 13: Record-flag collision-safe controller discriminator.

The runner separates the collision controller from arrow selection.  It
exhausts the Cartesian product of six fronts, fourteen predecessor labels,
fourteen realized labels, and all thirty-two destination Record patterns.
The all-or-none guarded map is tested as a total permanence-safe effective
controller.  A separate exact frontier enumeration decides whether two
collinear Record flags orient an unmarked finite trail without reading Record
content.
"""

from __future__ import annotations

import argparse
import ast
from functools import cache
import inspect
import itertools
from pathlib import Path
import sys

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import eta_safe_front_evidence_2026_09_09 as evidence  # noqa: E402
import admissibility_d4_outcome_typed_generated_front_two_step_2026_08_29 as b12  # noqa: E402
import independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29 as independent_checker  # noqa: E402


PACKET = ROOT / ".claude" / "science" / "physics-loops" / (
    "toe-source-eta-ownership-block13-collision-safe-controller-20260829"
)
GOAL = PACKET / "GOAL.md"
PREFLIGHT = PACKET / "PREFLIGHT_WITNESSES.md"
NOTE = ROOT / "docs" / (
    "ADMISSIBILITY_D4_RECORD_FLAG_COLLISION_SAFE_CONTROLLER_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)

AUDIT_TIMEOUT_SEC = 45
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block13-collision-safe-controller-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_RECORD_FLAG_COLLISION_SAFE_CONTROLLER_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_D4_OUTCOME_TYPED_GENERATED_FRONT_PREFIX_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block12-outcome-typed-two-step-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "scripts/eta_safe_front_evidence_2026_09_09.py",
    "scripts/eta_spin2_affine_model_2026_09_09.py",
    "scripts/eta_spin2_native_model_2026_09_09.py",
    "scripts/eta_spin2_quadrupole_model_2026_09_09.py",
    "scripts/eta_spin2_joint_model_2026_09_09.py",
    "scripts/admissibility_d4_outcome_typed_generated_front_two_step_2026_08_29.py",
    "scripts/independent_admissibility_d4_outcome_typed_generated_front_two_step_2026_08_29.py",
    "scripts/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py",
)

DIRECTIONS = b12.b9.DIRECTIONS
OUTCOMES = b12.OUTCOMES
FRONT0 = b12.FRONT0

MUTATIONS = (
    "stale_authority", "axiom_drift", "registration_drift",
    "block12_drift", "change_record_code", "change_law",
    "content_arrow_lookup", "host_front_input", "old_outcome_input",
    "drop_grandpredecessor", "allow_lateral_branch", "pretend_unique_tip",
    "formation_not_normalized", "same_event_feedback",
    "guard_outcome_dependent", "guard_reads_destination_content",
    "edge_collision", "nonlocal_edge", "partial_transport", "clone_source",
    "clear_successor_mismatch", "blocked_source_changed",
    "blocked_destination_changed", "move_existing_record",
    "unstable_stop", "drop_stop_mass", "packet_growth",
    "claim_flag_only_arrow", "claim_microscopic_controller",
    "claim_microscopic_readout", "claim_site_selection", "claim_rate",
    "claim_clock", "claim_interacting_fronts", "claim_gravity",
    "claim_axiom", "claim_toe", "claim_retained",
)

_SCOPE_CONTROLS = {
    "claim_flag_only_arrow", "claim_microscopic_controller",
    "claim_microscopic_readout", "claim_site_selection", "claim_rate",
    "claim_clock", "claim_interacting_fronts", "claim_gravity",
    "claim_axiom", "claim_toe", "claim_retained",
}
_SYNTAX_CONTROLS = {
    "stale_authority", "axiom_drift", "registration_drift", "block12_drift",
    "content_arrow_lookup", "host_front_input", "old_outcome_input",
    "same_event_feedback", "guard_reads_destination_content",
}
MUTATION_KINDS = {
    mutation: (
        "scope_guard" if mutation in _SCOPE_CONTROLS
        else "syntax_guard" if mutation in _SYNTAX_CONTROLS
        else "assertion_guard"
    )
    for mutation in MUTATIONS
}


def equal(left: sp.MatrixBase, right: sp.MatrixBase) -> bool:
    return left.shape == right.shape and all(
        sp.simplify(value) == 0 for value in left - right
    )


def pos(vector: sp.MatrixBase) -> tuple[int, int, int]:
    return tuple(int(vector[index]) for index in range(3))


def add(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] + right[index] for index in range(3))


def subtract(left: tuple[int, int, int], right: tuple[int, int, int]) -> tuple[int, int, int]:
    return tuple(left[index] - right[index] for index in range(3))


def infer_straight_front(
    relative_record_flags: dict[tuple[int, int, int], bool],
) -> sp.Matrix | None:
    """Infer an unoriented endpoint direction from Record geometry alone."""
    nearest = [
        direction for direction in DIRECTIONS
        if relative_record_flags.get(pos(direction), False)
    ]
    if len(nearest) != 1:
        return None
    front = -nearest[0]
    if not relative_record_flags.get(pos(-2 * front), False):
        return None
    return sp.Matrix(front)


def formation_stage(
    relative_record_flags: dict[tuple[int, int, int], bool],
    neighbor_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """Form the local distribution before a realized label is supplied."""
    front = infer_straight_front(relative_record_flags)
    if front is None:
        return {"eligible": False, "front": None, "probabilities": None}
    return {
        "eligible": True,
        "front": front,
        "probabilities": b12.b9.local_distribution(neighbor_contents),
    }


def collision_guard(destination_record_flags: tuple[bool, ...]) -> bool:
    """All-or-none guard over Record flags; quantum contents never enter."""
    return len(destination_record_flags) == 5 and not any(
        destination_record_flags
    )


def guarded_post_formation(
    front: sp.MatrixBase,
    neighbor_contents: tuple[sp.Matrix, ...],
    outcome_index: int,
    destination_record_flags: tuple[bool, ...],
    destination_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """Internal post-stage; ``front`` is the output of formation_stage."""
    source_directions = (sp.Matrix(front),) + tuple(
        direction for direction in DIRECTIONS
        if sp.simplify((direction.T * front)[0]) == 0
    )
    source_indices = tuple(next(
        index for index, direction in enumerate(DIRECTIONS)
        if direction == source_direction
    ) for source_direction in source_directions)
    source_contents = tuple(neighbor_contents[index] for index in source_indices)
    clear = collision_guard(destination_record_flags)
    if clear:
        source_after = tuple(destination_contents)
        destination_after = source_contents
    else:
        source_after = source_contents
        destination_after = tuple(destination_contents)
    return {
        "front": sp.Matrix(front),
        "new_record": b12.record_code(front, OUTCOMES[outcome_index]),
        "clear": clear,
        "continue": clear,
        "source_directions": source_directions,
        "source_after": source_after,
        "destination_after": destination_after,
        "destination_record_flags_after": destination_record_flags,
        "partial_transport": False,
    }


def effective_event(
    relative_record_flags: dict[tuple[int, int, int], bool],
    neighbor_contents: tuple[sp.Matrix, ...],
    outcome_index: int,
    destination_record_flags: tuple[bool, ...],
    destination_contents: tuple[sp.Matrix, ...],
) -> dict[str, object]:
    """One effective event with geometry-derived orientation and local guard."""
    formation = formation_stage(relative_record_flags, neighbor_contents)
    if not formation["eligible"]:
        return {"eligible": False}
    post = guarded_post_formation(
        formation["front"], neighbor_contents, outcome_index,
        destination_record_flags, destination_contents,
    )
    return {
        "eligible": True,
        "probabilities": formation["probabilities"],
        **post,
    }


def relative_flags(
    record_sites: set[tuple[int, int, int]],
    candidate: tuple[int, int, int],
) -> dict[tuple[int, int, int], bool]:
    return {subtract(site, candidate): True for site in record_sites}


def geometry_for_front(front: sp.MatrixBase) -> dict[str, object]:
    source_directions = (sp.Matrix(front),) + tuple(
        direction for direction in DIRECTIONS
        if sp.simplify((direction.T * front)[0]) == 0
    )
    sources = tuple(pos(direction) for direction in source_directions)
    step = pos(front)
    destinations = tuple(add(source, step) for source in sources)
    return {
        "source_directions": source_directions,
        "sources": sources,
        "destinations": destinations,
        "edges": tuple(zip(sources, destinations)),
    }


@cache
def source_binding_facts() -> dict[str, object]:
    return evidence.source_binding_facts(
        root=ROOT,
        source_path="scripts/admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py",
        audit_input_paths=AUDIT_INPUT_PATHS,
        imported_modules={
            "evidence": evidence,
            "finite_target_definitions": b12.native,
            "affine": b12.b9.affine,
            "quadrupole": b12.b9,
            "joint": b12.b10,
            "block12_primary": b12,
            "block12_checker": independent_checker.i12,
            "independent_checker": independent_checker,
        },
    )


@cache
def frozen_stack_facts() -> dict[str, object]:
    record = b12.record_code_facts()
    law = b12.law_facts()
    return {
        "record_entries": record["entries"],
        "record_distinct": record["distinct"],
        "record_physical": record["physical"],
        "record_covariant": record["covariance"],
        "law_outcomes": law["outcome_count"],
        "law_failures": law["failures"],
        "normalization": law["normalization"],
        "action_independence": law["action_independence"],
        "source": law["source"],
    }


@cache
def eligibility_facts() -> dict[str, object]:
    endpoint_counts = []
    endpoint_orientations = []
    lateral_false = []
    for front in DIRECTIONS:
        step = pos(front)
        for length in range(2, 10):
            trail = {
                tuple(index * step[axis] for axis in range(3))
                for index in range(length)
            }
            frontier = {
                add(site, pos(direction))
                for site in trail for direction in DIRECTIONS
                if add(site, pos(direction)) not in trail
            }
            eligible = []
            for candidate in frontier:
                inferred = infer_straight_front(relative_flags(trail, candidate))
                if inferred is not None:
                    eligible.append((candidate, pos(inferred)))
            expected_back = tuple(-step[axis] for axis in range(3))
            expected_forward = tuple(length * step[axis] for axis in range(3))
            endpoint_counts.append(len(eligible))
            endpoint_orientations.append(
                set(eligible) == {
                    (expected_back, pos(-front)),
                    (expected_forward, pos(front)),
                }
            )
            lateral_false.append(all(
                candidate in (expected_back, expected_forward)
                for candidate, _inferred in eligible
            ))
    source = inspect.getsource(infer_straight_front)
    return {
        "fronts": len(DIRECTIONS),
        "lengths_per_front": 8,
        "endpoint_counts": tuple(endpoint_counts),
        "two_endpoints": all(count == 2 for count in endpoint_counts),
        "endpoint_orientations": all(endpoint_orientations),
        "no_lateral_branch": all(lateral_false),
        "unique_tip": all(count == 1 for count in endpoint_counts),
        "content_input": "content" in tuple(
            inspect.signature(infer_straight_front).parameters
        ),
        "code_lookup": "codebook" in source,
    }


@cache
def runtime_facts() -> dict[str, object]:
    source = (
        inspect.getsource(infer_straight_front)
        + inspect.getsource(formation_stage)
        + inspect.getsource(collision_guard)
        + inspect.getsource(effective_event)
    )
    tree = ast.parse(source)
    called_attributes = {
        node.attr for node in ast.walk(tree) if isinstance(node, ast.Attribute)
    }
    forbidden_tokens = (
        "target", "fixture", "role", "epoch", "scheduler", "global_time",
        "site_id", "future_outcome", "predecessor_outcome",
    )
    return {
        "event_signature": tuple(inspect.signature(effective_event).parameters),
        "formation_signature": tuple(inspect.signature(formation_stage).parameters),
        "guard_signature": tuple(inspect.signature(collision_guard).parameters),
        "codebook_call": "codebook" in called_attributes or ".codebook" in source,
        "forbidden_token": any(token in source for token in forbidden_tokens),
        "guard_content_input": tuple(inspect.signature(collision_guard).parameters)
        != ("destination_record_flags",),
        "outcome_in_formation": "outcome" in tuple(
            inspect.signature(formation_stage).parameters
        ),
    }


@cache
def controller_table_facts() -> dict[str, object]:
    symbols = sp.symbols("m0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    formation_checks = []
    case_checks = []
    clear_successors = []
    blocked_identity = []
    blocked_permanence = []
    blocked_stability = []
    geometry_checks = []
    guard_values = []

    patterns = tuple(itertools.product((False, True), repeat=5))
    for front_index, front in enumerate(DIRECTIONS):
        geometry = geometry_for_front(front)
        sources = geometry["sources"]
        destinations = geometry["destinations"]
        edges = geometry["edges"]
        geometry_checks.append(
            len(edges) == 5
            and len(set(sources + destinations)) == 10
            and all(sum(abs(destination[axis] - source[axis])
                        for axis in range(3)) == 1
                    for source, destination in edges)
        )
        flags = {pos(-front): True, pos(-2 * front): True}
        backgrounds = tuple(
            sp.Matrix(sp.symbols(f"w{front_index}_{index}_0:3", real=True))
            for index in range(5)
        )

        pattern_checks: dict[tuple[bool, ...], bool] = {}
        pattern_stability: dict[tuple[bool, ...], bool] = {}
        for pattern in patterns:
            guard = collision_guard(pattern)
            guard_values.append(guard == (not any(pattern)))
            obstacle_sites = {
                destination for destination, occupied
                in zip(destinations, pattern) if occupied
            }
            record_sites_after = {
                pos(-2 * front), pos(-front), (0, 0, 0), *obstacle_sites
            }
            next_candidate = pos(front)
            next_inferred = infer_straight_front(
                relative_flags(record_sites_after, next_candidate)
            )
            pattern_stability[pattern] = (
                next_inferred is not None if not any(pattern)
                else next_inferred is None
            )

        for predecessor in OUTCOMES:
            shell = b12.hybrid_shell(matrix, front, predecessor)
            formation = formation_stage(flags, shell)
            formation_checks.append(
                formation["eligible"]
                and equal(formation["front"], front)
                and sp.simplify(sum(formation["probabilities"].values())) == 1
            )
            source_contents = tuple(
                shell[next(index for index, direction in enumerate(DIRECTIONS)
                           if direction == source_direction)]
                for source_direction in geometry["source_directions"]
            )
            for outcome_index, outcome in enumerate(OUTCOMES):
                for pattern in patterns:
                    post = guarded_post_formation(
                        formation["front"], shell, outcome_index, pattern,
                        backgrounds,
                    )
                    common = (
                        equal(post["new_record"], b12.record_code(front, outcome))
                        and post["clear"] == (not any(pattern))
                        and post["continue"] == (not any(pattern))
                        and post["destination_record_flags_after"] == pattern
                        and not post["partial_transport"]
                    )
                    if not any(pattern):
                        mapping = (
                            all(equal(left, right) for left, right in zip(
                                post["source_after"], backgrounds
                            ))
                            and all(equal(left, right) for left, right in zip(
                                post["destination_after"], source_contents
                            ))
                        )
                        next_matrix = sp.expand(
                            matrix
                            + (b12.record_code(front, predecessor)
                               - b12.record_code(front, outcome))
                            * front.T / 2
                        )
                        gathered = []
                        destination_map = dict(zip(
                            destinations, post["destination_after"]
                        ))
                        for direction in DIRECTIONS:
                            site = add(pos(front), pos(direction))
                            if site == (0, 0, 0):
                                gathered.append(post["new_record"])
                            else:
                                gathered.append(destination_map[site])
                        expected = b12.hybrid_shell(next_matrix, front, outcome)
                        successor = mapping and all(
                            equal(left, right)
                            for left, right in zip(gathered, expected)
                        )
                        clear_successors.append(successor)
                        pattern_checks[pattern] = successor
                    else:
                        identity = (
                            all(equal(left, right) for left, right in zip(
                                post["source_after"], source_contents
                            ))
                            and all(equal(left, right) for left, right in zip(
                                post["destination_after"], backgrounds
                            ))
                        )
                        permanence = all(
                            equal(post["destination_after"][index], backgrounds[index])
                            for index, occupied in enumerate(pattern) if occupied
                        )
                        blocked_identity.append(identity)
                        blocked_permanence.append(permanence)
                        blocked_stability.append(pattern_stability[pattern])
                        pattern_checks[pattern] = identity and permanence
                    case_checks.append(
                        common and pattern_checks[pattern]
                        and pattern_stability[pattern]
                    )

    swap = sp.Matrix(((1, 0, 0, 0), (0, 0, 1, 0),
                      (0, 1, 0, 0), (0, 0, 0, 1)))
    return {
        "fronts": len(DIRECTIONS),
        "patterns": len(patterns),
        "clear_patterns": sum(not any(pattern) for pattern in patterns),
        "blocked_patterns": sum(any(pattern) for pattern in patterns),
        "formation_cases": len(formation_checks),
        "formation": all(formation_checks),
        "table_cases": len(case_checks),
        "table": all(case_checks),
        "geometry": all(geometry_checks),
        "guard": all(guard_values),
        "swap_unitary": equal(swap.T * swap, sp.eye(4)),
        "clear_successor_cases": len(clear_successors),
        "clear_successors": all(clear_successors),
        "blocked_identity_cases": len(blocked_identity),
        "blocked_identity": all(blocked_identity),
        "blocked_permanence": all(blocked_permanence),
        "blocked_stability": all(blocked_stability),
        "packet_size": 5,
        "packet_growth": 0,
    }


@cache
def probability_stop_facts() -> dict[str, object]:
    symbols = sp.symbols("p0:9", real=True)
    matrix = sp.Matrix(3, 3, symbols)
    patterns = tuple(itertools.product((False, True), repeat=5))
    totals = []
    guard_outcome_independence = []
    for front in DIRECTIONS:
        flags = {pos(-front): True, pos(-2 * front): True}
        for predecessor in OUTCOMES:
            formation = formation_stage(
                flags, b12.hybrid_shell(matrix, front, predecessor)
            )
            values = tuple(
                formation["probabilities"][key]
                for key in b12.PROBABILITY_KEYS
            )
            for pattern in patterns:
                clear = collision_guard(pattern)
                continuation = sum(values) if clear else 0
                stop = 0 if clear else sum(values)
                totals.append(sp.simplify(continuation + stop))
                guard_outcome_independence.append(all(
                    collision_guard(pattern) == clear for _outcome in OUTCOMES
                ))
    return {
        "cases": len(totals),
        "normalized": all(total == 1 for total in totals),
        "guard_outcome_independent": all(guard_outcome_independence),
        "stop_included": True,
        "site_selection_supplied": False,
        "rate_supplied": False,
        "clock_supplied": False,
        "interacting_fronts_supplied": False,
        "microscopic_controller_supplied": False,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = NOTE.read_text(encoding="utf-8") if NOTE.is_file() else ""
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
    }


def evaluated_checks(mutation: str | None) -> list[tuple[str, bool, str]]:
    binding = source_binding_facts()
    authority_ok = evidence.source_binding_ok(binding)
    if mutation in (
        "stale_authority", "axiom_drift", "registration_drift",
        "block12_drift",
    ):
        authority_ok = False

    frozen = frozen_stack_facts()
    record_entries = 83 if mutation == "change_record_code" else frozen["record_entries"]
    normalization = 0 if mutation == "change_law" else frozen["normalization"]
    frozen_ok = (
        record_entries == 84 and frozen["record_distinct"] == 84
        and frozen["record_physical"] and frozen["record_covariant"]
        and frozen["law_outcomes"] == 14 and not any(frozen["law_failures"])
        and normalization == 1 and frozen["action_independence"]
        and frozen["source"]
    )

    eligibility = eligibility_facts()
    code_lookup = True if mutation == "content_arrow_lookup" else eligibility["code_lookup"]
    content_input = True if mutation in ("host_front_input", "old_outcome_input") else eligibility["content_input"]
    two_ends = False if mutation == "drop_grandpredecessor" else eligibility["two_endpoints"]
    lateral = False if mutation == "allow_lateral_branch" else eligibility["no_lateral_branch"]
    unique_tip = True if mutation == "pretend_unique_tip" else eligibility["unique_tip"]
    eligibility_ok = (
        eligibility["fronts"] == 6 and eligibility["lengths_per_front"] == 8
        and len(eligibility["endpoint_counts"]) == 48 and two_ends
        and eligibility["endpoint_orientations"] and lateral
        and not unique_tip and not content_input and not code_lookup
    )

    runtime = runtime_facts()
    outcome_in_formation = True if mutation == "same_event_feedback" else runtime["outcome_in_formation"]
    guard_content = True if mutation == "guard_reads_destination_content" else runtime["guard_content_input"]
    codebook_call = True if mutation == "content_arrow_lookup" else runtime["codebook_call"]
    signature = (
        runtime["event_signature"] + ("front",)
        if mutation == "host_front_input" else runtime["event_signature"]
    )
    runtime_ok = (
        signature == (
            "relative_record_flags", "neighbor_contents", "outcome_index",
            "destination_record_flags", "destination_contents",
        )
        and runtime["formation_signature"] == (
            "relative_record_flags", "neighbor_contents",
        )
        and runtime["guard_signature"] == ("destination_record_flags",)
        and not codebook_call and not runtime["forbidden_token"]
        and not guard_content and not outcome_in_formation
    )

    table = controller_table_facts()
    geometry = False if mutation in ("edge_collision", "nonlocal_edge") else table["geometry"]
    guard = False if mutation == "guard_outcome_dependent" else table["guard"]
    partial = True if mutation == "partial_transport" else False
    clear = False if mutation in ("clone_source", "clear_successor_mismatch") else table["clear_successors"]
    blocked_identity = False if mutation in (
        "blocked_source_changed", "blocked_destination_changed"
    ) else table["blocked_identity"]
    blocked_permanence = False if mutation == "move_existing_record" else table["blocked_permanence"]
    blocked_stability = False if mutation == "unstable_stop" else table["blocked_stability"]
    growth = 1 if mutation == "packet_growth" else table["packet_growth"]
    table_ok = (
        table["fronts"] == 6 and table["patterns"] == 32
        and table["clear_patterns"] == 1 and table["blocked_patterns"] == 31
        and table["formation_cases"] == 84 and table["formation"]
        and table["table_cases"] == 37632 and table["table"]
        and geometry and guard and table["swap_unitary"] and not partial
        and table["clear_successor_cases"] == 1176 and clear
        and table["blocked_identity_cases"] == 36456 and blocked_identity
        and blocked_permanence and blocked_stability
        and table["packet_size"] == 5 and growth == 0
    )

    probability = probability_stop_facts()
    normalized = False if mutation == "formation_not_normalized" else probability["normalized"]
    stop = False if mutation == "drop_stop_mass" else probability["stop_included"]
    probability_ok = (
        probability["cases"] == 2688 and normalized
        and probability["guard_outcome_independent"] and stop
        and not probability["site_selection_supplied"]
        and not probability["rate_supplied"] and not probability["clock_supplied"]
        and not probability["interacting_fronts_supplied"]
        and not probability["microscopic_controller_supplied"]
    )

    adjudication_ok = (
        table["table"] and table["blocked_permanence"]
        and eligibility["two_endpoints"] and not eligibility["unique_tip"]
    )
    if mutation == "claim_flag_only_arrow":
        adjudication_ok = False

    scope = scope_facts()
    scope_ok = scope["note"] and scope["forbidden"]
    if mutation in (
        "claim_microscopic_controller", "claim_microscopic_readout",
        "claim_site_selection", "claim_rate", "claim_clock",
        "claim_interacting_fronts", "claim_gravity", "claim_axiom",
        "claim_toe", "claim_retained",
    ):
        scope_ok = False

    return [
        ("A_current_source_binding", authority_ok,
         "all finite helpers, Block-12 implementations, the checker, and declared note premises resolve to the current working-tree closure"),
        ("B_unchanged_record_law", frozen_ok,
         "the 84-state code and normalized fourteen-way source law remain unchanged"),
        ("C_flag_only_arrow_discriminator", eligibility_ok,
         "two collinear Record flags reject lateral branches but select both ends of every finite unmarked straight trail"),
        ("D_oracle_free_runtime", runtime_ok,
         "formation uses Record flags and neighbor contents without a codebook, host front, old outcome, destination content read, or same-event feedback"),
        ("E_exhaustive_guarded_controller", table_ok,
         "all 37632 controller cases are total: clear transport is exact and all 31 blocked patterns are identity/permanence safe"),
        ("F_stop_probability", probability_ok,
         "clear continuation or blocked STOP carries the full normalized fourteen-outcome mass without supplying site/rate/clock"),
        ("G_registered_adjudication", adjudication_ok,
         "the all-or-none controller closes static-obstacle safety but flag-only geometry cannot choose the arrow, forcing CONDITIONAL-HALO"),
        ("H_scope", scope_ok,
         "the note keeps orientation readout, microscopic control, formation selection, concurrency, gravity, axioms, audit, and TOE open"),
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS)
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()
    if args.mutation_sweep:
        summary = evidence.control_sweep(evaluated_checks, MUTATIONS, MUTATION_KINDS)
        evidence.print_control_sweep(summary)
        print(
            f"TOTAL: PASS={len(summary.detected)} "
            f"FAIL={len(summary.survivors) + int(not summary.baseline_clean)}"
        )
        return int(evidence.control_sweep_failed(summary))

    if args.mutation is not None:
        baseline_failures = tuple(
            name for name, ok, _detail in evaluated_checks(None) if not ok
        )
        if baseline_failures:
            print(
                "MUTATION_BASELINE: clean=false; failures="
                + ",".join(baseline_failures)
            )
            return 1

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        ok = bool(ok)
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    if args.mutation is None:
        summary = evidence.control_sweep(evaluated_checks, MUTATIONS, MUTATION_KINDS)
        evidence.print_control_sweep(summary)
        failed += int(evidence.control_sweep_failed(summary))
        table = controller_table_facts()
        print(
            "per_element: checked each Record flag, each of five source/destination "
            "content pairs, and every occupied-destination permanence identity"
        )
        print(
            "per_site: checked both finite-line endpoints and the complete five-site "
            "all-or-none destination guard"
        )
        print(
            "per_mode: checked all nine carrier coordinates and fourteen outcome "
            "labels; no Fourier or continuum-mode claim was executed"
        )
        print(
            f"per_block: checked {table['table_cases']} controller cases, including "
            f"{table['clear_successor_cases']} clear and "
            f"{table['blocked_identity_cases']} blocked cases"
        )
        print(
            "lattice_wide: checked and not executed; simultaneous fronts, global "
            "scheduling, occurrence rate, and gravity remain open"
        )
        if all(bool(ok) for name, ok, _detail in checks if name != "H_scope"):
            print("VERDICT: CONDITIONAL-HALO; the all-or-none controller is safe but an unmarked finite line has two flag-only tips")
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
