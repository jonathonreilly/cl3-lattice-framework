#!/usr/bin/env python3
"""Independent exact reconstruction of Source/Eta Block 14.

This checker deliberately imports no Source/Eta runner.  It reconstructs the
84 locked Record contents in the exact field Q(1/sqrt(3)), the 24 proper cubic
rotations, the content-only half-space decoder, long finite trails, the
five-edge all-or-none controller, the complete blocked local frontier, and the
formal fourteen-way probability normalization from integer/rational data.

The public runtime functions never receive a host front, old outcome, role,
epoch, scheduler, clock, site identifier, target fixture, or content lookup
table.  Front direction is recovered from locked content at the point of use.
"""

from __future__ import annotations

import argparse
import ast
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
import itertools
from pathlib import Path
import subprocess


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block14-record-content-orientation-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
CHECKLIST_PATH = f"{PACKET}/NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_RECORD_CONTENT_ORIENTED_SAFE_FRONT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
PRIMARY_PATH = (
    "scripts/admissibility_d4_record_content_oriented_safe_front_"
    "2026_08_29.py"
)

PARENT = "96d25272f5b09a4a2743836f7a1a6d14e2b99771"
BLOCK13_RESULT = "88cd67d464c9da93fbb025c1f9943d14376ad267"
PREREG = "87c64c7b3661e8fe37e4f1f61a7f1ea5a6cdf733"
MAIN = "3cc632921c36aa90266c5c62e56816577ce59a0a"
AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
BLOCK13_INDEPENDENT_BLOB = "2b4e89f591d5fce52e0a5ff6999b2f189cb18f7a"
BLOCK13_INDEPENDENT_PATH = (
    "scripts/independent_admissibility_d4_record_flag_collision_safe_"
    "controller_2026_08_29.py"
)

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block14-record-content-orientation-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_RECORD_CONTENT_ORIENTED_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "scripts/independent_admissibility_d4_record_flag_collision_safe_controller_2026_08_29.py",
)

F = Fraction
Position = tuple[int, int, int]
Direction = Position
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
TRAIL_LENGTHS = tuple(range(2, 18))
BLOCKED_TRAIL_LENGTHS = tuple(range(2, 18))
LEADING_NUMERATOR = 144
RUNTIME_THRESHOLD_NUMERATOR = F(128)


@dataclass(frozen=True, slots=True)
class Rad3:
    """Exact a + b/sqrt(3), with a,b rational."""

    rational: Fraction = F(0)
    root_coefficient: Fraction = F(0)

    def __post_init__(self) -> None:
        object.__setattr__(self, "rational", F(self.rational))
        object.__setattr__(self, "root_coefficient", F(self.root_coefficient))

    def __add__(self, other: "Rad3") -> "Rad3":
        return Rad3(
            self.rational + other.rational,
            self.root_coefficient + other.root_coefficient,
        )

    def __sub__(self, other: "Rad3") -> "Rad3":
        return Rad3(
            self.rational - other.rational,
            self.root_coefficient - other.root_coefficient,
        )

    def __neg__(self) -> "Rad3":
        return Rad3(-self.rational, -self.root_coefficient)

    def __mul__(self, other: object) -> "Rad3":
        if isinstance(other, Rad3):
            return Rad3(
                self.rational * other.rational
                + self.root_coefficient * other.root_coefficient / 3,
                self.rational * other.root_coefficient
                + self.root_coefficient * other.rational,
            )
        if isinstance(other, (int, Fraction)):
            scalar = F(other)
            return Rad3(
                scalar * self.rational,
                scalar * self.root_coefficient,
            )
        return NotImplemented

    def __rmul__(self, other: object) -> "Rad3":
        return self * other

    def sign(self) -> int:
        a = self.rational
        b = self.root_coefficient
        if a == 0:
            return (b > 0) - (b < 0)
        if b == 0 or (a > 0) == (b > 0):
            return (a > 0) - (a < 0)
        comparison = 3 * a * a - b * b
        if comparison == 0:
            return 0
        dominant = a if comparison > 0 else b
        return (dominant > 0) - (dominant < 0)

    def __lt__(self, other: "Rad3") -> bool:
        return (self - other).sign() < 0

    def __le__(self, other: "Rad3") -> bool:
        return (self - other).sign() <= 0


ZERO = Rad3()


def rational_vector(vector: Position) -> tuple[Rad3, Rad3, Rad3]:
    return tuple(Rad3(component, 0) for component in vector)  # type: ignore[return-value]


AXIS_OUTCOMES = tuple(rational_vector(direction) for direction in DIRECTIONS)
CORNER_OUTCOMES = tuple(
    tuple(Rad3(0, sign) for sign in signs)
    for signs in itertools.product((-1, 1), repeat=3)
)
OUTCOMES = AXIS_OUTCOMES + CORNER_OUTCOMES


MUTATIONS = (
    "stale_main", "parent_missing", "prereg_drift", "axiom_drift",
    "import_block14_primary", "import_block13_primary",
    "drop_content", "collapse_front_code", "nonphysical_content",
    "weak_decoder_margin", "ambiguous_decoder", "outcome_leak_decoder",
    "preferred_axis_decoder", "drop_rotation", "close_threshold_interval",
    "short_trails", "drop_left_outcome", "flag_only_tip",
    "allow_lateral",
    "edge_collision", "outcome_dependent_guard", "partial_transport",
    "clone_packet", "move_record", "drop_new_record",
    "sample_blocked_patterns", "short_blocked_trails",
    "skip_obstacle_directions", "remove_blocking_obstacle",
    "drop_stop_mass", "same_event_feedback", "nonnormalized_law",
    "runtime_codebook", "host_front", "old_outcome",
    "claim_perfect_povm", "claim_generated_seed", "claim_microscopic",
    "claim_interacting", "claim_site_occurrence", "claim_rate_clock",
    "claim_global_absorbing", "claim_gravity", "claim_axiom",
    "claim_obligation", "claim_toe", "claim_retained",
)


def git(*args: str) -> str:
    return subprocess.check_output(
        ("git",) + args,
        cwd=ROOT,
        text=True,
        timeout=AUDIT_TIMEOUT_SEC,
    ).strip()


def ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        check=False,
        timeout=AUDIT_TIMEOUT_SEC,
    ).returncode == 0


def add(left: Position, right: Position) -> Position:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def subtract(left: Position, right: Position) -> Position:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def scale(factor: int, vector: Position) -> Position:
    return tuple(factor * component for component in vector)  # type: ignore[return-value]


def dot(left: Position, right: Position) -> int:
    return sum(left[index] * right[index] for index in range(3))


def manhattan(left: Position, right: Position) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3) for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


@cache
def rotations() -> tuple[Matrix3, ...]:
    result: set[Matrix3] = set()
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = []
            for row in range(3):
                rows.append(tuple(
                    signs[row] if column == permutation[row] else 0
                    for column in range(3)
                ))
            result.add(tuple(rows))  # type: ignore[arg-type]
    return tuple(sorted(result))


def rotate_position(matrix: Matrix3, vector: Position) -> Position:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotate_content(
    matrix: Matrix3,
    vector: tuple[Rad3, Rad3, Rad3],
) -> tuple[Rad3, Rad3, Rad3]:
    return tuple(
        sum(
            (matrix[row][column] * vector[column] for column in range(3)),
            ZERO,
        )
        for row in range(3)
    )  # type: ignore[return-value]


def encode_content(
    direction: Direction,
    outcome_vector: tuple[Rad3, Rad3, Rad3],
    *,
    leading_numerator: int = LEADING_NUMERATOR,
) -> tuple[Rad3, Rad3, Rad3]:
    """Return 256 r = -leading*direction + outcome_vector exactly."""
    return tuple(
        outcome_vector[index] - Rad3(leading_numerator * direction[index], 0)
        for index in range(3)
    )  # type: ignore[return-value]


def content_score(
    direction: Direction,
    content: tuple[Rad3, Rad3, Rad3],
) -> Rad3:
    return sum(
        (direction[index] * content[index] for index in range(3)),
        ZERO,
    )


@cache
def decode_content(
    content: tuple[Rad3, Rad3, Rad3],
    threshold_numerator: Fraction = RUNTIME_THRESHOLD_NUMERATOR,
) -> Direction | None:
    """The public fixed half-space functional; it sees content only."""
    cutoff = Rad3(-threshold_numerator, 0)
    passing = tuple(
        direction for direction in DIRECTIONS
        if content_score(direction, content) < cutoff
    )
    return passing[0] if len(passing) == 1 else None


def decoder_variant(
    content: tuple[Rad3, Rad3, Rad3],
    mode: str,
) -> Direction | None:
    if mode == "weak_margin":
        return decode_content(content, F(144))
    if mode == "ambiguous":
        return decode_content(content, F(0))
    decoded = decode_content(content)
    if mode == "outcome_leak" and any(
        component.root_coefficient for component in content
    ):
        return None if decoded is None else scale(-1, decoded)
    if mode == "preferred_axis" and decoded is not None and decoded[0] == 0:
        return None
    return decoded


def maximum(values: tuple[Rad3, ...]) -> Rad3:
    current = values[0]
    for value in values[1:]:
        if current < value:
            current = value
    return current


def minimum(values: tuple[Rad3, ...]) -> Rad3:
    current = values[0]
    for value in values[1:]:
        if value < current:
            current = value
    return current


@cache
def authority_facts() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imports = {
        alias.name
        for node in ast.walk(tree)
        if isinstance(node, ast.Import)
        for alias in node.names
    } | {
        node.module or ""
        for node in ast.walk(tree)
        if isinstance(node, ast.ImportFrom)
    }
    forbidden = (
        "admissibility_d4_record_content_oriented_safe_front",
        "admissibility_d4_record_flag_collision_safe_controller",
    )
    return {
        "main": git("rev-parse", "origin/main"),
        "parent": ancestor(PARENT),
        "block13_result": ancestor(BLOCK13_RESULT),
        "prereg": ancestor(PREREG),
        "axiom": git("rev-parse", "HEAD:docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "goal_current": git("hash-object", GOAL_PATH),
        "goal_registered": git("rev-parse", f"{PREREG}:{GOAL_PATH}"),
        "preflight_current": git("hash-object", PREFLIGHT_PATH),
        "preflight_registered": git("rev-parse", f"{PREREG}:{PREFLIGHT_PATH}"),
        "block13_independent": git("hash-object", BLOCK13_INDEPENDENT_PATH),
        "forbidden_import": any(
            module.startswith(prefix)
            for module in imports for prefix in forbidden
        ),
        "local_science_imports": tuple(sorted(
            module for module in imports
            if module.startswith("admissibility_d4")
            or module.startswith("independent_admissibility_d4")
        )),
        "note": (ROOT / NOTE_PATH).is_file(),
        "checklist": (ROOT / CHECKLIST_PATH).is_file(),
        "primary_exists": (ROOT / PRIMARY_PATH).is_file(),
    }


@cache
def content_decoder_facts(mode: str = "clean") -> dict[str, object]:
    leading = {
        "collapse": 0,
        "nonphysical": 300,
        "weak_code": 127,
    }.get(mode, LEADING_NUMERATOR)
    outcome_vectors = OUTCOMES[:-1] if mode == "drop_content" else OUTCOMES
    frames = rotations()[:-1] if mode == "drop_rotation" else rotations()
    decoder_mode = {
        "weak_decoder": "weak_margin",
        "ambiguous": "ambiguous",
        "outcome_leak": "outcome_leak",
        "preferred_axis": "preferred_axis",
    }.get(mode, "clean")

    rows = tuple(
        (direction, outcome, encode_content(
            direction, outcome, leading_numerator=leading,
        ))
        for direction in DIRECTIONS for outcome in outcome_vectors
    )
    contents = tuple(row[2] for row in rows)
    decoded = tuple(
        decoder_variant(content, decoder_mode)
        for _direction, _outcome, content in rows
    )
    outcome_independent = all(
        got == direction
        for (direction, _outcome, _content), got in zip(rows, decoded)
    )

    true_scores = tuple(
        content_score(direction, content)
        for direction, _outcome, content in rows
    )
    false_scores = tuple(
        content_score(candidate, content)
        for direction, _outcome, content in rows
        for candidate in DIRECTIONS if candidate != direction
    )
    max_true = maximum(true_scores)
    min_false = minimum(false_scores)
    threshold_interval = (
        max_true <= Rad3(-143, 0)
        and Rad3(-1, 0) <= min_false
        and F(1) < RUNTIME_THRESHOLD_NUMERATOR < F(143)
    )
    if mode == "close_interval":
        threshold_interval = False

    covariance = []
    registered_outcomes = set(OUTCOMES)
    rotated_outcomes_registered = []
    for matrix in frames:
        for direction, outcome, content in rows:
            next_direction = rotate_position(matrix, direction)
            next_outcome = rotate_content(matrix, outcome)
            transported = rotate_content(matrix, content)
            direct = encode_content(
                next_direction, next_outcome, leading_numerator=leading,
            )
            rotated_outcomes_registered.append(next_outcome in registered_outcomes)
            covariance.append(
                transported == direct
                and decoder_variant(transported, decoder_mode) == next_direction
            )

    norm_squares = tuple(
        sum((component * component for component in content), ZERO)
        for content in contents
    )
    strict_full_rank = all(
        value < Rad3(256 * 256, 0) for value in norm_squares
    )
    return {
        "entries": len(contents),
        "distinct": len(set(contents)),
        "directions": len(DIRECTIONS),
        "outcomes": len(outcome_vectors),
        "frames": len(frames),
        "covariance_cases": len(covariance),
        "covariance": all(covariance),
        "rotated_outcomes_registered": all(rotated_outcomes_registered),
        "unique_outcome_independent_decoder": outcome_independent,
        "max_true_score": max_true,
        "min_false_score": min_false,
        "threshold_interval": threshold_interval,
        "runtime_threshold": RUNTIME_THRESHOLD_NUMERATOR,
        "strict_full_rank": strict_full_rank,
        "perfect_ordinary_one_site_povm": False,
    }


def neighboring_records(
    records: dict[Position, tuple[Rad3, Rad3, Rad3]],
    candidate: Position,
) -> tuple[Position, ...]:
    return tuple(
        site for direction in DIRECTIONS
        if (site := add(candidate, direction)) in records
    )


def orientation_eligible(
    records: dict[Position, tuple[Rad3, Rad3, Rad3]],
    candidate: Position,
) -> bool:
    """Public content-oriented predicate on a no-Record candidate."""
    if candidate in records:
        return False
    nearest = neighboring_records(records, candidate)
    if len(nearest) != 1:
        return False
    predecessor = nearest[0]
    direction = decode_content(records[predecessor])
    return bool(
        direction is not None
        and predecessor == subtract(candidate, direction)
        and subtract(candidate, scale(2, direction)) in records
    )


def eligibility_variant(
    records: dict[Position, tuple[Rad3, Rad3, Rad3]],
    candidate: Position,
    mode: str,
) -> bool:
    if mode == "clean":
        return orientation_eligible(records, candidate)
    if candidate in records:
        return False
    nearest = neighboring_records(records, candidate)
    if len(nearest) != 1:
        return False
    if mode == "lateral_loose":
        return True
    predecessor = nearest[0]
    inferred = subtract(candidate, predecessor)
    return subtract(candidate, scale(2, inferred)) in records


@cache
def trail_facts(mode: str = "clean") -> dict[str, object]:
    lengths = tuple(range(2, 10)) if mode == "short" else TRAIL_LENGTHS
    left_outcomes = OUTCOMES[:-1] if mode == "drop_left" else OUTCOMES
    eligibility_mode = {
        "flag_only": "flag_only",
        "lateral_loose": "lateral_loose",
    }.get(mode, "clean")

    cases = 0
    candidate_checks = 0
    exact_forward = []
    reflected_rejections = []
    lateral_rejections = []
    for direction in DIRECTIONS:
        for left_outcome in left_outcomes:
            for right_outcome in OUTCOMES:
                for length in lengths:
                    records = {
                        scale(index, direction): encode_content(
                            direction,
                            left_outcome if index == 0 else (
                                right_outcome if index == length - 1
                                else OUTCOMES[0]
                            ),
                        )
                        for index in range(length)
                    }
                    frontier = {
                        add(site, neighbor)
                        for site in records for neighbor in DIRECTIONS
                        if add(site, neighbor) not in records
                    }
                    eligible = {
                        candidate for candidate in frontier
                        if eligibility_variant(records, candidate, eligibility_mode)
                    }
                    forward = scale(length, direction)
                    reflected = scale(-1, direction)
                    exact_forward.append(eligible == {forward})
                    reflected_rejections.append(reflected not in eligible)
                    lateral_rejections.append(all(
                        candidate in (forward, reflected)
                        for candidate in eligible
                    ))
                    candidate_checks += len(frontier)
                    cases += 1
    return {
        "fronts": len(DIRECTIONS),
        "left_outcomes": len(left_outcomes),
        "right_outcomes": len(OUTCOMES),
        "lengths": len(lengths),
        "minimum_length": min(lengths),
        "maximum_length": max(lengths),
        "cases": cases,
        "candidate_checks": candidate_checks,
        "one_forward_tip": all(exact_forward),
        "reflected_rejected": all(reflected_rejections),
        "lateral_rejected": all(lateral_rejections),
    }


def packet_geometry(direction: Direction) -> tuple[tuple[Position, ...], tuple[Position, ...]]:
    sources = (direction,) + tuple(
        candidate for candidate in DIRECTIONS if dot(candidate, direction) == 0
    )
    destinations = tuple(add(source, direction) for source in sources)
    return sources, destinations


def form_record(
    predecessor_content: tuple[Rad3, Rad3, Rad3],
    realized_outcome: tuple[Rad3, Rad3, Rad3],
) -> tuple[Rad3, Rad3, Rad3] | None:
    """Write content using only the direction decoded from the predecessor."""
    direction = decode_content(predecessor_content)
    return None if direction is None else encode_content(direction, realized_outcome)


def _transport_variant(
    formed_content: tuple[Rad3, Rad3, Rad3],
    obstacle_flags: tuple[bool, ...],
    state: dict[Position, object],
    mode: str,
    branch_index: int,
) -> tuple[Direction | None, dict[Position, object], str, tuple[Position, ...], tuple[Position, ...]]:
    direction = decode_content(formed_content)
    if direction is None:
        return None, dict(state), "INVALID", (), ()
    sources, destinations = packet_geometry(direction)
    if mode == "edge_collision":
        destinations = destinations[:-1] + (destinations[0],)
    result = dict(state)
    clear = not any(obstacle_flags)
    if mode == "outcome_guard" and branch_index % 2:
        clear = False
    if clear:
        for source, destination in zip(sources, destinations):
            if mode == "clone_packet":
                result[destination] = result[source]
            else:
                result[source], result[destination] = (
                    result[destination], result[source]
                )
    elif mode == "partial_transport":
        for source, destination, occupied in zip(
            sources, destinations, obstacle_flags
        ):
            if not occupied:
                result[source], result[destination] = (
                    result[destination], result[source]
                )
                break
    return direction, result, "CONTINUE" if clear else "STOP", sources, destinations


def guarded_transport(
    formed_content: tuple[Rad3, Rad3, Rad3],
    obstacle_flags: tuple[bool, ...],
    state: dict[Position, object],
) -> tuple[Direction | None, dict[Position, object], str, tuple[Position, ...], tuple[Position, ...]]:
    """Public all-or-none map; its geometry is decoded from formed content."""
    return _transport_variant(formed_content, obstacle_flags, state, "clean", 0)


@cache
def controller_facts(mode: str = "clean") -> dict[str, object]:
    patterns = tuple(itertools.product((False, True), repeat=5))
    case_checks = []
    geometry_checks = []
    clear_checks = []
    blocked_identity = []
    blocked_permanence = []
    packet_sizes = []
    internal_directions = []

    for expected_direction in DIRECTIONS:
        clean_sources, clean_destinations = packet_geometry(expected_direction)
        geometry_checks.append(
            len(clean_sources) == len(clean_destinations) == 5
            and len(set(clean_sources + clean_destinations)) == 10
            and all(manhattan(source, destination) == 1
                    for source, destination
                    in zip(clean_sources, clean_destinations))
        )
        for predecessor_outcome in OUTCOMES:
            predecessor_content = encode_content(
                expected_direction, predecessor_outcome
            )
            for branch_index, realized_outcome in enumerate(OUTCOMES):
                formed = form_record(predecessor_content, realized_outcome)
                if formed is None:
                    case_checks.extend(False for _ in patterns)
                    continue
                for pattern in patterns:
                    source_payloads = tuple(
                        ("payload", index) for index in range(5)
                    )
                    destination_backgrounds = tuple(
                        ("background", index) for index in range(5)
                    )
                    state = dict(zip(clean_sources, source_payloads))
                    state.update(zip(clean_destinations, destination_backgrounds))
                    before = dict(state)
                    direction, after, terminal, sources, destinations = (
                        _transport_variant(
                            formed, pattern, state, mode, branch_index
                        )
                    )
                    internal_directions.append(direction == expected_direction)
                    clear = not any(pattern)
                    guard_exact = terminal == (
                        "CONTINUE" if clear else "STOP"
                    )

                    obstacle_sites = {
                        destination for destination, occupied
                        in zip(clean_destinations, pattern) if occupied
                    }
                    record_before = {
                        scale(-1, expected_direction),
                        scale(-2, expected_direction),
                    } | obstacle_sites
                    record_after = set(record_before)
                    if mode != "drop_new_record":
                        record_after.add((0, 0, 0))
                    if mode == "move_record" and obstacle_sites:
                        record_after.remove(sorted(obstacle_sites)[0])

                    if clear:
                        mapping = (
                            len(sources) == len(destinations) == 5
                            and all(
                                after.get(destination) == payload
                                for destination, payload
                                in zip(clean_destinations, source_payloads)
                            )
                            and all(
                                after.get(source) == background
                                for source, background
                                in zip(clean_sources, destination_backgrounds)
                            )
                        )
                        clear_checks.append(mapping)
                        safe = mapping
                    else:
                        identity = after == before
                        permanence = (
                            record_before <= record_after
                            and obstacle_sites <= record_after
                        )
                        blocked_identity.append(identity)
                        blocked_permanence.append(permanence)
                        safe = identity and permanence

                    packet_size = sum(
                        isinstance(value, tuple) and value[0] == "payload"
                        for value in after.values()
                    )
                    packet_sizes.append(packet_size)
                    case_checks.append(
                        direction == expected_direction
                        and guard_exact and safe
                        and record_after == record_before | {(0, 0, 0)}
                    )

    return {
        "fronts": len(DIRECTIONS),
        "predecessor_outcomes": len(OUTCOMES),
        "new_outcomes": len(OUTCOMES),
        "patterns": len(patterns),
        "clear_patterns": sum(not any(pattern) for pattern in patterns),
        "blocked_patterns": sum(any(pattern) for pattern in patterns),
        "cases": len(case_checks),
        "all_cases": all(case_checks),
        "geometry": all(geometry_checks),
        "internal_direction": all(internal_directions),
        "clear_cases": len(clear_checks),
        "clear_successor": all(clear_checks),
        "blocked_cases": len(blocked_identity),
        "blocked_identity": all(blocked_identity),
        "blocked_permanence": all(blocked_permanence),
        "packet_size": set(packet_sizes),
        "packet_growth": max(packet_sizes) - 5,
    }


def direction_eligible_with_supplied_content_direction(
    record_sites: set[Position],
    candidate: Position,
    predecessor: Position,
    decoded_direction: Direction,
) -> bool:
    return (
        predecessor == subtract(candidate, decoded_direction)
        and subtract(candidate, scale(2, decoded_direction)) in record_sites
    )


@cache
def blocked_frontier_facts(mode: str = "clean") -> dict[str, object]:
    lengths = (
        tuple(range(3, 11)) if mode == "short"
        else BLOCKED_TRAIL_LENGTHS
    )
    patterns = tuple(
        pattern for pattern in itertools.product((False, True), repeat=5)
        if any(pattern)
    )
    if mode == "sample_patterns":
        patterns = patterns[:1]

    components = 0
    candidate_direction_checks = 0
    maximum_eligible = 0
    obstacle_predecessor_checks = 0
    for direction in DIRECTIONS:
        _sources, destinations = packet_geometry(direction)
        trail_content = encode_content(direction, OUTCOMES[0])
        for length in lengths:
            trail = {scale(-index, direction) for index in range(length)}
            for pattern in patterns:
                obstacles = {
                    destination for destination, occupied
                    in zip(destinations, pattern) if occupied
                }
                if mode == "remove_obstacle" and obstacles:
                    obstacles = set(obstacles)
                    obstacles.remove(sorted(obstacles)[0])
                record_sites = trail | obstacles
                record_contents = {site: trail_content for site in trail}
                frontier = {
                    add(site, neighbor)
                    for site in record_sites for neighbor in DIRECTIONS
                    if add(site, neighbor) not in record_sites
                }
                eligible = 0
                for candidate in frontier:
                    nearest = tuple(
                        site for site in record_sites
                        if manhattan(site, candidate) == 1
                    )
                    if len(nearest) != 1:
                        continue
                    predecessor = nearest[0]
                    if predecessor in obstacles:
                        possible_directions = (
                            DIRECTIONS[:1]
                            if mode == "skip_obstacle_directions"
                            else DIRECTIONS
                        )
                        obstacle_predecessor_checks += len(possible_directions)
                    else:
                        decoded = decode_content(record_contents[predecessor])
                        possible_directions = () if decoded is None else (decoded,)
                    for decoded_direction in possible_directions:
                        candidate_direction_checks += 1
                        eligible += int(
                            direction_eligible_with_supplied_content_direction(
                                record_sites,
                                candidate,
                                predecessor,
                                decoded_direction,
                            )
                        )
                maximum_eligible = max(maximum_eligible, eligible)
                components += 1
    return {
        "fronts": len(DIRECTIONS),
        "patterns": len(patterns),
        "lengths": len(lengths),
        "minimum_length": min(lengths),
        "maximum_length": max(lengths),
        "components": components,
        "candidate_direction_checks": candidate_direction_checks,
        "obstacle_predecessor_checks": obstacle_predecessor_checks,
        "maximum_eligible": maximum_eligible,
        "zero_eligible": maximum_eligible == 0,
        "lattice_wide_absorbing": False,
    }


@dataclass(frozen=True, slots=True)
class AffineWeight:
    constant: Fraction
    coefficients: tuple[Fraction, Fraction, Fraction, Fraction, Fraction]

    def __add__(self, other: "AffineWeight") -> "AffineWeight":
        return AffineWeight(
            self.constant + other.constant,
            tuple(
                self.coefficients[index] + other.coefficients[index]
                for index in range(5)
            ),  # type: ignore[arg-type]
        )


ZERO_WEIGHT = AffineWeight(F(0), (F(0),) * 5)
ONE_WEIGHT = AffineWeight(F(1), (F(0),) * 5)


def weight(
    constant: Fraction,
    *coefficients: Fraction,
) -> AffineWeight:
    assert len(coefficients) == 5
    return AffineWeight(F(constant), tuple(F(value) for value in coefficients))  # type: ignore[arg-type]


@cache
def fourteen_way_weights() -> tuple[AffineWeight, ...]:
    # Variables are (q_xx, q_yy, q_xy, q_yz, q_xz), with q_zz=-q_xx-q_yy.
    diagonal = (
        (F(1), F(0), F(0), F(0), F(0)),
        (F(0), F(1), F(0), F(0), F(0)),
        (F(-1), F(-1), F(0), F(0), F(0)),
    )
    result = []
    for direction in DIRECTIONS:
        axis = next(index for index, value in enumerate(direction) if value)
        result.append(weight(
            F(1, 12), *(coefficient / 48 for coefficient in diagonal[axis])
        ))
    for signs in itertools.product((-1, 1), repeat=3):
        sx, sy, sz = signs
        result.append(weight(
            F(1, 16), F(0), F(0),
            F(sx * sy, 64), F(sy * sz, 64), F(sx * sz, 64),
        ))
    return tuple(result)


def guard_distribution(
    obstacle_flags: tuple[bool, ...],
) -> tuple[tuple[int, str, AffineWeight], ...]:
    """The guard routes existing outcome mass; it never changes the weights."""
    terminal = "STOP" if any(obstacle_flags) else "CONTINUE"
    return tuple(
        (branch, terminal, value)
        for branch, value in enumerate(fourteen_way_weights())
    )


def distribution_variant(
    obstacle_flags: tuple[bool, ...],
    mode: str,
) -> tuple[tuple[int, str, AffineWeight], ...]:
    rows = list(guard_distribution(obstacle_flags))
    if mode == "drop_stop" and any(obstacle_flags):
        return ()
    if mode == "feedback":
        rows = [
            (branch, "STOP" if branch % 2 else terminal, value)
            for branch, terminal, value in rows
        ]
    if mode == "nonnormalized":
        branch, terminal, value = rows[0]
        rows[0] = (
            branch,
            terminal,
            AffineWeight(value.constant + F(1, 100), value.coefficients),
        )
    return tuple(rows)


@cache
def probability_facts(mode: str = "clean") -> dict[str, object]:
    patterns = tuple(itertools.product((False, True), repeat=5))
    totals = []
    terminal_checks = []
    stop_mass_checks = []
    branch_counts = []
    for _direction in DIRECTIONS:
        for _predecessor_outcome in OUTCOMES:
            for pattern in patterns:
                rows = distribution_variant(pattern, mode)
                total = sum((row[2] for row in rows), ZERO_WEIGHT)
                totals.append(total)
                expected = "STOP" if any(pattern) else "CONTINUE"
                terminal_checks.append(all(row[1] == expected for row in rows))
                if any(pattern):
                    stop_mass_checks.append(total == ONE_WEIGHT)
                branch_counts.append(len(rows))
    bare_total = sum(fourteen_way_weights(), ZERO_WEIGHT)
    return {
        "law_entries": len(fourteen_way_weights()),
        "formal_law_normalized": bare_total == ONE_WEIGHT,
        "cases": len(totals),
        "normalized": all(total == ONE_WEIGHT for total in totals),
        "outcome_independent_guard": all(terminal_checks),
        "stop_mass_preserved": all(stop_mass_checks),
        "branch_counts": set(branch_counts),
        "same_event_feedback": mode == "feedback",
        "site_occurrence": False,
        "rate_or_clock": False,
    }


@cache
def runtime_surface_facts() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_names = {
        "decode_content", "orientation_eligible", "form_record",
        "guarded_transport", "guard_distribution",
    }
    public_nodes = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in public_names
    }
    forbidden_arguments = {
        "front", "host_front", "old_outcome", "role", "epoch", "site_id",
        "scheduler", "global_time", "target_fixture", "probability_feedback",
    }
    arguments = {
        argument.arg
        for node in public_nodes.values()
        for argument in node.args.args + node.args.kwonlyargs
    }
    decoder = public_nodes.get("decode_content")
    decoder_dictionary_free = bool(decoder) and not any(
        isinstance(node, (ast.Dict, ast.DictComp)) for node in ast.walk(decoder)
    )
    decoder_does_not_encode = bool(decoder) and not any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "encode_content"
        for node in ast.walk(decoder)
    )
    return {
        "public_functions": set(public_nodes) == public_names,
        "forbidden_public_arguments": arguments & forbidden_arguments,
        "decoder_dictionary_free": decoder_dictionary_free,
        "decoder_does_not_encode": decoder_does_not_encode,
        "runtime_codebook": False,
        "host_front": False,
        "old_outcome": False,
        "role_epoch_scheduler_clock": False,
        "target_fixture": False,
        "same_event_probability_feedback": False,
    }


@cache
def scope_facts() -> dict[str, object]:
    note = (ROOT / NOTE_PATH).read_text(encoding="utf-8")
    checklist = (ROOT / CHECKLIST_PATH).read_text(encoding="utf-8")
    normalized_note = " ".join(note.split())
    normalized_checklist = " ".join(checklist.split())
    required_note = (
        "CONTENT-ORIENTED-SAFE-FRONT",
        "framework-level Record readout",
        "not a lattice-wide absorbing state",
        "microscopic pointer/control remains open",
        "obligation retirement: 0",
        "TOE percentage movement: 0",
    )
    no_go = (
        all(f"## N{index}" in checklist for index in range(1, 9))
        and "Status: `PASS`" in checklist
        and "No statement is made against other content decoders"
        in normalized_checklist
        and "No negative here licenses a global no-member claim"
        in normalized_checklist
    )
    return {
        "note_boundary": all(
            phrase in normalized_note for phrase in required_note
        ),
        "no_go": no_go,
        "perfect_povm": False,
        "generated_seed": False,
        "microscopic_controller": False,
        "interacting_fronts": False,
        "site_occurrence": False,
        "rate_clock": False,
        "global_absorbing": False,
        "gravity": False,
        "axiom_amendment": False,
        "obligation_retirement": 0,
        "toe_movement": 0,
        "retained": False,
    }


def evaluated_checks(mutation: str = "") -> list[tuple[str, bool, str]]:
    authority = dict(authority_facts())
    if mutation == "stale_main":
        authority["main"] = "0" * 40
    elif mutation == "parent_missing":
        authority["parent"] = False
    elif mutation == "prereg_drift":
        authority["goal_current"] = "0" * 40
    elif mutation == "axiom_drift":
        authority["axiom"] = "0" * 40
    elif mutation in ("import_block14_primary", "import_block13_primary"):
        authority["forbidden_import"] = True
    authority_ok = (
        authority["main"] == MAIN
        and authority["parent"] and authority["block13_result"]
        and authority["prereg"] and authority["axiom"] == AXIOM_BLOB
        and authority["goal_current"] == authority["goal_registered"]
        and authority["preflight_current"] == authority["preflight_registered"]
        and authority["block13_independent"] == BLOCK13_INDEPENDENT_BLOB
        and not authority["forbidden_import"]
        and authority["local_science_imports"] == ()
        and authority["note"] and authority["checklist"]
        and authority["primary_exists"]
    )

    content_mode = {
        "drop_content": "drop_content",
        "collapse_front_code": "collapse",
        "nonphysical_content": "nonphysical",
        "weak_decoder_margin": "weak_code",
        "ambiguous_decoder": "ambiguous",
        "outcome_leak_decoder": "outcome_leak",
        "preferred_axis_decoder": "preferred_axis",
        "drop_rotation": "drop_rotation",
        "close_threshold_interval": "close_interval",
    }.get(mutation, "clean")
    content = content_decoder_facts(content_mode)
    content_ok = (
        content["entries"] == 84 and content["distinct"] == 84
        and content["directions"] == 6 and content["outcomes"] == 14
        and content["frames"] == 24 and content["covariance_cases"] == 2016
        and content["covariance"] and content["rotated_outcomes_registered"]
        and content["unique_outcome_independent_decoder"]
        and content["max_true_score"] == Rad3(-143, 0)
        and content["min_false_score"] == Rad3(-1, 0)
        and content["threshold_interval"]
        and content["runtime_threshold"] == F(128)
        and content["strict_full_rank"]
        and not content["perfect_ordinary_one_site_povm"]
    )

    trail_mode = {
        "short_trails": "short",
        "drop_left_outcome": "drop_left",
        "flag_only_tip": "flag_only",
        "allow_lateral": "lateral_loose",
    }.get(mutation, "clean")
    trail = trail_facts(trail_mode)
    trail_ok = (
        trail["fronts"] == 6
        and trail["left_outcomes"] == trail["right_outcomes"] == 14
        and trail["lengths"] == 16
        and trail["minimum_length"] == 2 and trail["maximum_length"] == 17
        and trail["cases"] == 18816
        and trail["candidate_checks"] == 752640
        and trail["one_forward_tip"]
        and trail["reflected_rejected"] and trail["lateral_rejected"]
    )

    controller_mode = {
        "edge_collision": "edge_collision",
        "outcome_dependent_guard": "outcome_guard",
        "partial_transport": "partial_transport",
        "clone_packet": "clone_packet",
        "move_record": "move_record",
        "drop_new_record": "drop_new_record",
    }.get(mutation, "clean")
    controller = controller_facts(controller_mode)
    controller_ok = (
        controller["fronts"] == 6
        and controller["predecessor_outcomes"] == 14
        and controller["new_outcomes"] == 14
        and controller["patterns"] == 32
        and controller["clear_patterns"] == 1
        and controller["blocked_patterns"] == 31
        and controller["cases"] == 37632 and controller["all_cases"]
        and controller["geometry"] and controller["internal_direction"]
        and controller["clear_cases"] == 1176
        and controller["clear_successor"]
        and controller["blocked_cases"] == 36456
        and controller["blocked_identity"]
        and controller["blocked_permanence"]
        and controller["packet_size"] == {5}
        and controller["packet_growth"] == 0
    )

    frontier_mode = {
        "sample_blocked_patterns": "sample_patterns",
        "short_blocked_trails": "short",
        "skip_obstacle_directions": "skip_obstacle_directions",
        "remove_blocking_obstacle": "remove_obstacle",
    }.get(mutation, "clean")
    frontier = blocked_frontier_facts(frontier_mode)
    frontier_ok = (
        frontier["fronts"] == 6 and frontier["patterns"] == 31
        and frontier["lengths"] == 16
        and frontier["minimum_length"] == 2
        and frontier["maximum_length"] == 17
        and frontier["components"] == 2976
        and frontier["candidate_direction_checks"] == 229728
        and frontier["obstacle_predecessor_checks"] == 119808
        and frontier["maximum_eligible"] == 0 and frontier["zero_eligible"]
        and not frontier["lattice_wide_absorbing"]
    )

    probability_mode = {
        "drop_stop_mass": "drop_stop",
        "same_event_feedback": "feedback",
        "nonnormalized_law": "nonnormalized",
    }.get(mutation, "clean")
    probability = probability_facts(probability_mode)
    probability_ok = (
        probability["law_entries"] == 14
        and probability["formal_law_normalized"]
        and probability["cases"] == 2688
        and probability["normalized"]
        and probability["outcome_independent_guard"]
        and probability["stop_mass_preserved"]
        and probability["branch_counts"] == {14}
        and not probability["same_event_feedback"]
        and not probability["site_occurrence"]
        and not probability["rate_or_clock"]
    )

    runtime = dict(runtime_surface_facts())
    if mutation == "runtime_codebook":
        runtime["runtime_codebook"] = True
    elif mutation == "host_front":
        runtime["host_front"] = True
    elif mutation == "old_outcome":
        runtime["old_outcome"] = True
    runtime_ok = (
        runtime["public_functions"]
        and not runtime["forbidden_public_arguments"]
        and runtime["decoder_dictionary_free"]
        and runtime["decoder_does_not_encode"]
        and not runtime["runtime_codebook"]
        and not runtime["host_front"] and not runtime["old_outcome"]
        and not runtime["role_epoch_scheduler_clock"]
        and not runtime["target_fixture"]
        and not runtime["same_event_probability_feedback"]
    )

    scope = dict(scope_facts())
    scope_mutations = {
        "claim_perfect_povm": "perfect_povm",
        "claim_generated_seed": "generated_seed",
        "claim_microscopic": "microscopic_controller",
        "claim_interacting": "interacting_fronts",
        "claim_site_occurrence": "site_occurrence",
        "claim_rate_clock": "rate_clock",
        "claim_global_absorbing": "global_absorbing",
        "claim_gravity": "gravity",
        "claim_axiom": "axiom_amendment",
        "claim_obligation": "obligation_retirement",
        "claim_toe": "toe_movement",
        "claim_retained": "retained",
    }
    if mutation in scope_mutations:
        scope[scope_mutations[mutation]] = (
            1 if mutation in ("claim_obligation", "claim_toe") else True
        )
    scope_ok = (
        scope["note_boundary"] and scope["no_go"]
        and not scope["perfect_povm"] and not scope["generated_seed"]
        and not scope["microscopic_controller"]
        and not scope["interacting_fronts"]
        and not scope["site_occurrence"] and not scope["rate_clock"]
        and not scope["global_absorbing"] and not scope["gravity"]
        and not scope["axiom_amendment"]
        and scope["obligation_retirement"] == 0
        and scope["toe_movement"] == 0 and not scope["retained"]
    )

    adjudication_ok = (
        content_ok and trail_ok and controller_ok and frontier_ok
        and probability_ok and runtime_ok and scope_ok
    )
    return [
        ("A_independent_authority", authority_ok,
         "pinned registration and predecessor authority match; no Source/Eta runner is imported"),
        ("B_exact_content_decoder", content_ok,
         "84 exact Q(1/sqrt(3)) contents decode uniquely with the full 24-frame covariance census"),
        ("C_long_oriented_trails", trail_ok,
         "18816 trails of lengths 2..17 have one forward tip with reflected and lateral rejection"),
        ("D_guarded_controller", controller_ok,
         "all 37632 maps continue by five disjoint swaps or preserve the entire blocked state"),
        ("E_complete_blocked_frontier", frontier_ok,
         "all 2976 longer blocked components and every obstacle direction have zero local continuation"),
        ("F_probability_and_runtime", probability_ok and runtime_ok,
         "2688 formal fourteen-way laws conserve continue-or-STOP mass without a host oracle or feedback"),
        ("G_scoped_adjudication", adjudication_ok,
         "CONTENT-ORIENTED-SAFE-FRONT is effective and local; microscopic, concurrent, rate, gravity, and TOE claims remain false"),
    ]


def mutation_sweep() -> tuple[int, tuple[str, ...]]:
    survivors = tuple(
        mutation for mutation in MUTATIONS
        if all(ok for _name, ok, _detail in evaluated_checks(mutation))
    )
    return len(MUTATIONS) - len(survivors), survivors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=MUTATIONS, default="")
    parser.add_argument("--mutation-sweep", action="store_true")
    args = parser.parse_args()

    if args.mutation_sweep:
        rejected, survivors = mutation_sweep()
        print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))
        print(f"TOTAL: PASS={rejected} FAIL={len(survivors)}")
        return int(bool(survivors))

    checks = evaluated_checks(args.mutation)
    passed = failed = 0
    for name, ok, detail in checks:
        passed += int(bool(ok))
        failed += int(not bool(ok))
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")
    if not args.mutation:
        rejected, survivors = mutation_sweep()
        print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))
        failed += int(bool(survivors))
        if not failed:
            print(
                "VERDICT: CONTENT-ORIENTED-SAFE-FRONT independently "
                "reconstructed on the longer exact census"
            )
            print(
                "COUNTS: contents=84; frames=24; covariance=2016; "
                "trails=18816; controller=37632; blocked_components=2976; "
                "blocked_direction_checks=229728; probability_cases=2688"
            )
            print(
                "BOUNDARY: effective local single-lineage readout only; "
                "pointer/control, seed generation, interacting fronts, "
                "occurrence/rate/time, gravity, retention, obligations, and "
                "TOE closure remain unproved"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
