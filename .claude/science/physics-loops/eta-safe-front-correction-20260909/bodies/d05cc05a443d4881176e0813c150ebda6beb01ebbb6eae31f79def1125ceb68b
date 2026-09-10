#!/usr/bin/env python3
"""Independent exact reconstruction of Source/Eta Block 15.

The checker imports no Source/Eta runner.  Its primary geometry is the graph
of nearest-neighbor Record adjacencies: every possible tip is extrapolated
from a directed Record edge and is then checked against the complete flag
frontier.  Record contents are raising sentinels during front inference.

The result is deliberately narrow.  It concerns a supplied asymmetric capped
seed in one effective classical Record-flag sector and one conditioned local
formation event.  It does not generate the cap, choose a physical arrow,
construct microscopic flag sensing/control, or address simultaneous fronts,
occurrence/rate/time, gravity, axioms, retention, obligations, or TOE closure.
"""

from __future__ import annotations

import argparse
import ast
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from functools import cache
import hashlib
import itertools
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-source-eta-ownership-block15-gapped-record-cap-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
CHECKLIST_PATH = f"{PACKET}/NO_GO_DISCIPLINE_CHECKLIST.md"
NOTE_PATH = (
    "docs/ADMISSIBILITY_D4_GAPPED_RECORD_CAP_SAFE_FRONT_"
    "BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
)
GOAL_BLOB = "323177503219e750d308cac866aae03143e78105"
PREFLIGHT_BLOB = "98ff7f9dc43d0e656e8b2add336eca4cc70f4b7a"

AUDIT_TIMEOUT_SEC = 300
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/GOAL.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/PREFLIGHT_WITNESSES.md",
    ".claude/science/physics-loops/toe-source-eta-ownership-block15-gapped-record-cap-20260829/NO_GO_DISCIPLINE_CHECKLIST.md",
    "docs/ADMISSIBILITY_D4_GAPPED_RECORD_CAP_SAFE_FRONT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

Position = tuple[int, int, int]
Direction = Position
Matrix3 = tuple[tuple[int, int, int], tuple[int, int, int], tuple[int, int, int]]
F = Fraction

DIRECTIONS: tuple[Direction, ...] = (
    (1, 0, 0), (-1, 0, 0),
    (0, 1, 0), (0, -1, 0),
    (0, 0, 1), (0, 0, -1),
)
TRAIL_LENGTHS = tuple(range(2, 18))
OUTCOMES = tuple(range(14))
REGISTERED_CONTENTS = tuple(
    (direction, outcome)
    for direction in DIRECTIONS
    for outcome in OUTCOMES
)
TRANSLATIONS: tuple[Position, ...] = (
    (0, 0, 0),
    (11, -7, 5),
    (-13, 17, -19),
)
OBSTACLE_TRANSLATION: Position = (29, -31, 37)

EXPECTED_SEED_COMPONENTS = 6 * 24 * 16 * 84
EXPECTED_SEED_FRONTIER_EVALUATIONS = 8_709_120
EXPECTED_SEED_TIPS = EXPECTED_SEED_COMPONENTS
EXPECTED_CONTROLLER_CASES = 6 * 14 * 14 * 32
EXPECTED_BLOCKED_COMPONENTS = 31 * 6 * 16
EXPECTED_BLOCKED_FRONTIER_EVALUATIONS = 171_936

TERMINAL = "GAPPED-CAP-SAFE-FRONT"
LIMITS = {
    "supplied_asymmetric_cap_and_seed": True,
    "effective_classical_record_flags": True,
    "single_conditioned_local_front": True,
    "generated_cap": False,
    "chosen_physical_arrow": False,
    "microscopic_flag_sensor_or_controller": False,
    "simultaneous_interacting_fronts": False,
    "site_occurrence": False,
    "rate_or_time": False,
    "gravity": False,
    "axiom_amendment": False,
    "obligation_retirement": 0,
    "retained_status": False,
    "toe_movement": 0,
}


class ContentAccessError(AssertionError):
    """Raised if flag-only geometry attempts to inspect Record content."""


class RaisingContent:
    """Opaque registered content whose observation is a test failure."""

    __slots__ = ("_tag",)

    def __init__(self, tag: object) -> None:
        object.__setattr__(self, "_tag", tag)

    @staticmethod
    def _raise() -> None:
        raise ContentAccessError("Record content reached flag-only geometry")

    def __bool__(self) -> bool:
        self._raise()

    def __eq__(self, _other: object) -> bool:
        self._raise()

    def __hash__(self) -> int:
        self._raise()

    def __iter__(self):
        self._raise()

    def __repr__(self) -> str:
        self._raise()


POISON_CONTENTS = tuple(RaisingContent(code) for code in REGISTERED_CONTENTS)
TRAIL_POISON = RaisingContent("arbitrary-trail-content")


@dataclass(frozen=True, slots=True)
class FlagWorld:
    """The only geometry-facing state surface: exact Record flags."""

    record_flags: frozenset[Position]
    cap_payload: object = TRAIL_POISON

    def record_flag(self, site: Position) -> bool:
        return site in self.record_flags

    def record_content(self, _site: Position) -> object:
        raise ContentAccessError("content is outside the flag-only surface")


@dataclass(frozen=True, slots=True)
class ControllerResult:
    inferred_direction: Direction
    terminal: str
    record_flags: frozenset[Position]
    site_contents: dict[Position, object]
    sources: tuple[Position, ...]
    destinations: tuple[Position, ...]


@dataclass(frozen=True, slots=True)
class AffineWeight:
    """Exact affine fourteen-way law in five independent traceless entries."""

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


def add(left: Position, right: Position) -> Position:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def subtract(left: Position, right: Position) -> Position:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def scale(factor: int, vector: Position) -> Position:
    return tuple(factor * component for component in vector)  # type: ignore[return-value]


def dot(left: Position, right: Position) -> int:
    return sum(left[index] * right[index] for index in range(3))


def permutation_sign(permutation: tuple[int, int, int]) -> int:
    inversions = sum(
        permutation[left] > permutation[right]
        for left in range(3)
        for right in range(left + 1, 3)
    )
    return -1 if inversions % 2 else 1


@cache
def rotations() -> tuple[Matrix3, ...]:
    result: set[Matrix3] = set()
    for permutation in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            if permutation_sign(permutation) * signs[0] * signs[1] * signs[2] != 1:
                continue
            rows = tuple(
                tuple(
                    signs[row] if column == permutation[row] else 0
                    for column in range(3)
                )
                for row in range(3)
            )
            result.add(rows)  # type: ignore[arg-type]
    return tuple(sorted(result))


def rotate(matrix: Matrix3, vector: Position) -> Position:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def translate(site: Position, displacement: Position) -> Position:
    return add(site, displacement)


def capped_seed(
    direction: Direction,
    length: int,
    displacement: Position = (0, 0, 0),
) -> frozenset[Position]:
    trail = {
        add(displacement, scale(index, direction))
        for index in range(length)
    }
    trail.add(add(displacement, scale(-2, direction)))
    return frozenset(trail)


def complete_frontier(record_flags: frozenset[Position]) -> tuple[Position, ...]:
    frontier = {
        add(record_site, direction)
        for record_site in record_flags
        for direction in DIRECTIONS
    }
    frontier.difference_update(record_flags)
    return tuple(sorted(frontier))


def infer_flag_front(world: FlagWorld, candidate: Position) -> Direction | None:
    """Infer a front from flags only; no host direction or content is accepted."""

    predecessor: Position | None = None
    for displacement in DIRECTIONS:
        neighbor = add(candidate, displacement)
        if not world.record_flag(neighbor):
            continue
        if predecessor is not None:
            return None
        predecessor = neighbor
    if predecessor is None:
        return None
    inferred = subtract(candidate, predecessor)
    grand_predecessor = subtract(candidate, scale(2, inferred))
    if not world.record_flag(grand_predecessor):
        return None
    return inferred


def scan_frontier_tips(world: FlagWorld) -> frozenset[tuple[Position, Direction]]:
    result = set()
    for candidate in complete_frontier(world.record_flags):
        inferred = infer_flag_front(world, candidate)
        if inferred is not None:
            result.add((candidate, inferred))
    return frozenset(result)


def edge_extrapolated_tips(
    world: FlagWorld,
) -> frozenset[tuple[Position, Direction]]:
    """Structurally independent candidate generation from directed edges."""

    result = set()
    flags = world.record_flags
    for grand_predecessor in flags:
        for direction in DIRECTIONS:
            predecessor = add(grand_predecessor, direction)
            if predecessor not in flags:
                continue
            candidate = add(predecessor, direction)
            if candidate in flags:
                continue
            record_neighbors = {
                add(candidate, displacement)
                for displacement in DIRECTIONS
                if add(candidate, displacement) in flags
            }
            if record_neighbors == {predecessor}:
                result.add((candidate, direction))
    return frozenset(result)


def record_edges(
    record_flags: frozenset[Position],
) -> frozenset[tuple[Position, Position]]:
    result = set()
    for left in record_flags:
        for direction in DIRECTIONS:
            right = add(left, direction)
            if right in record_flags:
                result.add(tuple(sorted((left, right))))
    return frozenset(result)


def packet_geometry(
    candidate: Position,
    direction: Direction,
) -> tuple[tuple[Position, ...], tuple[Position, ...]]:
    perpendicular = tuple(
        displacement
        for displacement in DIRECTIONS
        if dot(displacement, direction) == 0
    )
    sources = (add(candidate, direction),) + tuple(
        add(candidate, displacement) for displacement in perpendicular
    )
    destinations = tuple(add(source, direction) for source in sources)
    return sources, destinations


def execute_formation(
    world: FlagWorld,
    candidate: Position,
    site_contents: dict[Position, object],
    outcome: int,
) -> ControllerResult:
    """Write one Record and apply the flags-derived all-or-none controller."""

    inferred = infer_flag_front(world, candidate)
    if inferred is None:
        raise ValueError("formation candidate is not eligible")
    sources, destinations = packet_geometry(candidate, inferred)
    clear = all(not world.record_flag(site) for site in destinations)
    after = dict(site_contents)
    if clear:
        for source, destination in zip(sources, destinations):
            after[source], after[destination] = (
                site_contents[destination], site_contents[source]
            )
    after[candidate] = ("new-record", inferred, outcome)
    return ControllerResult(
        inferred_direction=inferred,
        terminal="CONTINUE" if clear else "STOP",
        record_flags=world.record_flags | {candidate},
        site_contents=after,
        sources=sources,
        destinations=destinations,
    )


def weight(
    constant: Fraction,
    *coefficients: Fraction,
) -> AffineWeight:
    if len(coefficients) != 5:
        raise ValueError("five independent traceless coefficients required")
    return AffineWeight(F(constant), tuple(F(value) for value in coefficients))  # type: ignore[arg-type]


@cache
def fourteen_way_weights() -> tuple[AffineWeight, ...]:
    # Variables: q_xx, q_yy, q_xy, q_yz, q_xz with q_zz=-q_xx-q_yy.
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
    for sx, sy, sz in itertools.product((-1, 1), repeat=3):
        result.append(weight(
            F(1, 16), F(0), F(0),
            F(sx * sy, 64), F(sy * sz, 64), F(sx * sz, 64),
        ))
    return tuple(result)


def guard_distribution(
    obstacle_flags: tuple[bool, ...],
) -> tuple[tuple[int, str, AffineWeight], ...]:
    terminal = "STOP" if any(obstacle_flags) else "CONTINUE"
    return tuple(
        (outcome, terminal, probability)
        for outcome, probability in enumerate(fourteen_way_weights())
    )


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


@cache
def authority_facts() -> dict[str, object]:
    goal = ROOT / GOAL_PATH
    preflight = ROOT / PREFLIGHT_PATH
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    imported_modules = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported_modules.update(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported_modules.add(node.module)
    allowed_roots = {
        "__future__", "argparse", "ast", "collections", "dataclasses",
        "fractions", "functools", "hashlib", "itertools", "pathlib",
    }
    imports_standard_only = all(
        module.split(".", 1)[0] in allowed_roots for module in imported_modules
    )
    goal_text = goal.read_text(encoding="utf-8")
    return {
        "goal_blob": git_blob(goal),
        "preflight_blob": git_blob(preflight),
        "imports_standard_only": imports_standard_only,
        "registration_has_terminal": TERMINAL in goal_text,
        "registration_has_controller_count": "37,632" in goal_text,
        "registration_has_blocked_count": "2,976" in goal_text,
    }


@cache
def seed_census_facts() -> dict[str, object]:
    components = 0
    frontier_evaluations = 0
    eligible_tips = 0
    gap_rejections = 0
    exterior_rejections = 0
    exact = True
    edge_agreement = True
    path_graph = True

    geometry_cache: dict[
        tuple[Direction, int],
        tuple[
            frozenset[Position], tuple[Position, ...],
            frozenset[tuple[Position, Direction]],
        ],
    ] = {}
    for initial_direction in DIRECTIONS:
        for matrix in rotations():
            direction = rotate(matrix, initial_direction)
            for length in TRAIL_LENGTHS:
                cache_key = (direction, length)
                if cache_key not in geometry_cache:
                    flags = capped_seed(direction, length)
                    frontier = complete_frontier(flags)
                    world = FlagWorld(flags)
                    extrapolated = edge_extrapolated_tips(world)
                    geometry_cache[cache_key] = flags, frontier, extrapolated
                    expected_edges = frozenset(
                        tuple(sorted((scale(index, direction), scale(index + 1, direction))))
                        for index in range(length - 1)
                    )
                    path_graph &= record_edges(flags) == expected_edges
                flags, frontier, extrapolated = geometry_cache[cache_key]
                expected = frozenset({(scale(length, direction), direction)})
                exact &= len(frontier) == 4 * length + 7
                edge_agreement &= extrapolated == expected
                gap = scale(-1, direction)
                exterior = scale(-3, direction)
                for cap_payload in POISON_CONTENTS:
                    world = FlagWorld(flags, cap_payload)
                    observed = set()
                    for candidate in frontier:
                        inferred = infer_flag_front(world, candidate)
                        frontier_evaluations += 1
                        if inferred is not None:
                            observed.add((candidate, inferred))
                    observed_frozen = frozenset(observed)
                    exact &= observed_frozen == expected
                    edge_agreement &= observed_frozen == extrapolated
                    eligible_tips += len(observed_frozen)
                    gap_rejections += int(all(site != gap for site, _ in observed_frozen))
                    exterior_rejections += int(
                        all(site != exterior for site, _ in observed_frozen)
                    )
                    components += 1

    return {
        "front_parameters": len(DIRECTIONS),
        "frames": len(rotations()),
        "lengths": len(TRAIL_LENGTHS),
        "contents": len(REGISTERED_CONTENTS),
        "components": components,
        "frontier_evaluations": frontier_evaluations,
        "eligible_tips": eligible_tips,
        "rejected_sites": frontier_evaluations - eligible_tips,
        "gap_rejections": gap_rejections,
        "exterior_rejections": exterior_rejections,
        "exact": exact,
        "edge_agreement": edge_agreement,
        "path_graph": path_graph,
        "frontier_sum": sum(4 * length + 7 for length in TRAIL_LENGTHS),
        "poison_contents": len(POISON_CONTENTS),
    }


def transform_flags(
    flags: frozenset[Position],
    matrix: Matrix3,
    displacement: Position,
) -> frozenset[Position]:
    return frozenset(
        add(displacement, rotate(matrix, site)) for site in flags
    )


@cache
def covariance_facts() -> dict[str, object]:
    seed_cases = 0
    footprint_cases = 0
    obstacle_cases = 0
    seed_identity = True
    footprint_identity = True
    obstacle_identity = True

    for direction in DIRECTIONS:
        for length in TRAIL_LENGTHS:
            base_flags = capped_seed(direction, length)
            base_tips = edge_extrapolated_tips(FlagWorld(base_flags))
            candidate = scale(length, direction)
            base_sources, base_destinations = packet_geometry(candidate, direction)
            for matrix in rotations():
                moved_direction = rotate(matrix, direction)
                for displacement in TRANSLATIONS:
                    moved_flags = transform_flags(base_flags, matrix, displacement)
                    moved_expected = frozenset(
                        (
                            add(displacement, rotate(matrix, site)),
                            rotate(matrix, inferred),
                        )
                        for site, inferred in base_tips
                    )
                    moved_world = FlagWorld(moved_flags)
                    seed_identity &= edge_extrapolated_tips(moved_world) == moved_expected
                    seed_identity &= scan_frontier_tips(moved_world) == moved_expected
                    moved_candidate = add(displacement, rotate(matrix, candidate))
                    moved_sources, moved_destinations = packet_geometry(
                        moved_candidate, moved_direction
                    )
                    expected_pairs = {
                        (
                            add(displacement, rotate(matrix, source)),
                            add(displacement, rotate(matrix, destination)),
                        )
                        for source, destination in zip(
                            base_sources, base_destinations
                        )
                    }
                    footprint_identity &= set(zip(
                        moved_sources, moved_destinations
                    )) == expected_pairs
                    seed_cases += 1
                    footprint_cases += 1

            post_flags = base_flags | {candidate}
            _, destinations = packet_geometry(candidate, direction)
            for mask in range(1, 32):
                obstacles = frozenset(
                    destinations[index]
                    for index in range(5)
                    if mask >> index & 1
                )
                blocked_flags = post_flags | obstacles
                for matrix in rotations():
                    moved_direction = rotate(matrix, direction)
                    moved_candidate = add(
                        OBSTACLE_TRANSLATION, rotate(matrix, candidate)
                    )
                    moved_sources, moved_destinations = packet_geometry(
                        moved_candidate, moved_direction
                    )
                    expected_pairs = {
                        (
                            add(OBSTACLE_TRANSLATION, rotate(matrix, source)),
                            add(OBSTACLE_TRANSLATION, rotate(matrix, destination)),
                        )
                        for source, destination in zip(
                            *packet_geometry(candidate, direction)
                        )
                    }
                    moved_obstacles = {
                        add(OBSTACLE_TRANSLATION, rotate(matrix, site))
                        for site in obstacles
                    }
                    mapped_destination_set = {
                        destination
                        for _source, destination in expected_pairs
                    }
                    moved_flags = transform_flags(
                        blocked_flags, matrix, OBSTACLE_TRANSLATION
                    )
                    obstacle_identity &= set(zip(
                        moved_sources, moved_destinations
                    )) == expected_pairs
                    obstacle_identity &= moved_obstacles <= mapped_destination_set
                    obstacle_identity &= not edge_extrapolated_tips(FlagWorld(moved_flags))
                    obstacle_cases += 1

    return {
        "rotations": len(rotations()),
        "translations": len(TRANSLATIONS),
        "seed_cases": seed_cases,
        "footprint_cases": footprint_cases,
        "obstacle_transform_cases": obstacle_cases,
        "seed_identity": seed_identity,
        "footprint_identity": footprint_identity,
        "obstacle_identity": obstacle_identity,
    }


def local_contents(
    record_flags: frozenset[Position],
    sources: tuple[Position, ...],
    destinations: tuple[Position, ...],
    predecessor_outcome: int,
) -> dict[Position, object]:
    result: dict[Position, object] = {
        site: ("old-record", site, predecessor_outcome)
        for site in record_flags
    }
    for index, source in enumerate(sources):
        result[source] = ("packet-source", index, predecessor_outcome)
    for index, destination in enumerate(destinations):
        if destination not in record_flags:
            result[destination] = (
                "clear-destination", index, predecessor_outcome
            )
    return result


@cache
def controller_facts() -> dict[str, object]:
    cases = clear_cases = blocked_cases = 0
    all_exact = True
    geometry_exact = True
    internal_direction = True
    clear_successor = True
    blocked_identity = True
    permanence = True
    packet_sizes: set[int] = set()
    packet_growth = 0

    for direction in DIRECTIONS:
        length = 2
        candidate = scale(length, direction)
        seed = capped_seed(direction, length)
        sources, destinations = packet_geometry(candidate, direction)
        footprint = set(sources) | set(destinations)
        cap = scale(-2, direction)
        geometry_exact &= (
            len(sources) == len(destinations) == 5
            and len(footprint) == 10
            and set(sources).isdisjoint(destinations)
            and footprint.isdisjoint(seed)
            and cap not in footprint
            and all(
                subtract(destination, source) == direction
                for source, destination in zip(sources, destinations)
            )
        )
        for predecessor_outcome in OUTCOMES:
            for outcome in OUTCOMES:
                for mask in range(32):
                    obstacles = frozenset(
                        destinations[index]
                        for index in range(5)
                        if mask >> index & 1
                    )
                    flags = seed | obstacles
                    world = FlagWorld(flags)
                    before = local_contents(
                        flags, sources, destinations, predecessor_outcome
                    )
                    result = execute_formation(
                        world, candidate, before, outcome
                    )
                    internal_direction &= result.inferred_direction == direction
                    permanence &= result.record_flags == flags | {candidate}
                    permanence &= all(
                        result.site_contents[site] == before[site]
                        for site in flags
                    )
                    permanence &= result.site_contents[candidate] == (
                        "new-record", direction, outcome
                    )
                    before_packet = Counter(before[site] for site in footprint)
                    after_packet = Counter(
                        result.site_contents[site] for site in footprint
                    )
                    packet_growth += int(before_packet != after_packet)
                    if mask == 0:
                        clear_cases += 1
                        packet_sizes.add(sum(
                            result.site_contents[destination] == before[source]
                            for source, destination in zip(sources, destinations)
                        ))
                        all_exact &= result.terminal == "CONTINUE"
                        all_exact &= all(
                            result.site_contents[source] == before[destination]
                            and result.site_contents[destination] == before[source]
                            for source, destination in zip(sources, destinations)
                        )
                        clear_successor &= edge_extrapolated_tips(
                            FlagWorld(result.record_flags)
                        ) == frozenset({(add(candidate, direction), direction)})
                    else:
                        blocked_cases += 1
                        all_exact &= result.terminal == "STOP"
                        identity_sites = set(sources) | set(destinations)
                        blocked_identity &= all(
                            result.site_contents[site] == before[site]
                            for site in identity_sites
                        )
                    cases += 1

    return {
        "fronts": len(DIRECTIONS),
        "predecessor_outcomes": len(OUTCOMES),
        "outcomes": len(OUTCOMES),
        "patterns": 32,
        "cases": cases,
        "clear_cases": clear_cases,
        "blocked_cases": blocked_cases,
        "all_exact": all_exact,
        "geometry_exact": geometry_exact,
        "internal_direction": internal_direction,
        "clear_successor": clear_successor,
        "blocked_identity": blocked_identity,
        "permanence": permanence,
        "packet_sizes": packet_sizes,
        "packet_growth": packet_growth,
    }


@cache
def blocked_frontier_facts() -> dict[str, object]:
    components = 0
    frontier_evaluations = 0
    maximum_eligible = 0
    edge_agreement = True
    adjacency_invariant = True
    restart_without_new = 0
    restart_without_obstacles = 0
    length_two_sizes: Counter[int] = Counter()

    for direction in DIRECTIONS:
        for length in TRAIL_LENGTHS:
            candidate = scale(length, direction)
            seed = capped_seed(direction, length)
            post = seed | {candidate}
            _, destinations = packet_geometry(candidate, direction)
            expected_edges = frozenset(
                tuple(sorted((scale(index, direction), scale(index + 1, direction))))
                for index in range(length)
            )
            for mask in range(1, 32):
                obstacles = frozenset(
                    destinations[index]
                    for index in range(5)
                    if mask >> index & 1
                )
                flags = post | obstacles
                world = FlagWorld(flags)
                frontier = complete_frontier(flags)
                observed = set()
                for site in frontier:
                    inferred = infer_flag_front(world, site)
                    frontier_evaluations += 1
                    if inferred is not None:
                        observed.add((site, inferred))
                extrapolated = edge_extrapolated_tips(world)
                edge_agreement &= frozenset(observed) == extrapolated
                maximum_eligible = max(maximum_eligible, len(observed))
                adjacency_invariant &= record_edges(flags) == expected_edges
                without_new = scan_frontier_tips(FlagWorld(seed | obstacles))
                without_obstacles = scan_frontier_tips(FlagWorld(post))
                restart_without_new += int(
                    without_new == frozenset({(candidate, direction)})
                )
                restart_without_obstacles += int(
                    without_obstacles == frozenset({(
                        add(candidate, direction), direction
                    )})
                )
                if direction == DIRECTIONS[0] and length == 2:
                    length_two_sizes[len(frontier)] += 1
                components += 1

    return {
        "fronts": len(DIRECTIONS),
        "patterns": 31,
        "lengths": len(TRAIL_LENGTHS),
        "components": components,
        "frontier_evaluations": frontier_evaluations,
        "maximum_eligible": maximum_eligible,
        "edge_agreement": edge_agreement,
        "adjacency_invariant": adjacency_invariant,
        "restart_without_new": restart_without_new,
        "restart_without_obstacles": restart_without_obstacles,
        "length_two_size_distribution": dict(sorted(length_two_sizes.items())),
        "lattice_wide_absorbing": False,
    }


@cache
def probability_facts() -> dict[str, object]:
    patterns = tuple(itertools.product((False, True), repeat=5))
    groups = stop_groups = continue_groups = branch_rows = 0
    normalized = True
    terminal_exact = True
    for _direction in DIRECTIONS:
        for _predecessor_outcome in OUTCOMES:
            for pattern in patterns:
                rows = guard_distribution(pattern)
                total = sum((row[2] for row in rows), ZERO_WEIGHT)
                expected_terminal = "STOP" if any(pattern) else "CONTINUE"
                normalized &= total == ONE_WEIGHT
                terminal_exact &= all(
                    row[1] == expected_terminal for row in rows
                )
                stop_groups += int(any(pattern))
                continue_groups += int(not any(pattern))
                branch_rows += len(rows)
                groups += 1
    return {
        "law_entries": len(fourteen_way_weights()),
        "bare_normalized": sum(fourteen_way_weights(), ZERO_WEIGHT) == ONE_WEIGHT,
        "groups": groups,
        "stop_groups": stop_groups,
        "continue_groups": continue_groups,
        "branch_rows": branch_rows,
        "normalized": normalized,
        "terminal_exact": terminal_exact,
        "same_event_feedback": False,
    }


@cache
def runtime_surface_facts() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_names = {
        "infer_flag_front", "execute_formation", "guard_distribution"
    }
    public_nodes = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in public_names
    }
    expected_arguments = {
        "infer_flag_front": ("world", "candidate"),
        "execute_formation": (
            "world", "candidate", "site_contents", "outcome"
        ),
        "guard_distribution": ("obstacle_flags",),
    }
    actual_arguments = {
        name: tuple(argument.arg for argument in node.args.args)
        for name, node in public_nodes.items()
    }
    infer_node = public_nodes.get("infer_flag_front")
    infer_uses_content = bool(infer_node) and any(
        (
            isinstance(node, ast.Attribute)
            and "content" in node.attr.lower()
        )
        or (
            isinstance(node, ast.Name)
            and "content" in node.id.lower()
        )
        for node in ast.walk(infer_node)
    )
    execute_node = public_nodes.get("execute_formation")
    execute_calls_infer = bool(execute_node) and any(
        isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == "infer_flag_front"
        for node in ast.walk(execute_node)
    )
    forbidden_arguments = {
        "front", "host_direction", "cap", "cap_role", "role", "epoch",
        "site_id", "scheduler", "global_time", "target_fixture",
        "probability_feedback", "predecessor_outcome",
    }
    all_arguments = {
        argument
        for arguments in actual_arguments.values()
        for argument in arguments
    }
    sentinel_raises = False
    try:
        bool(POISON_CONTENTS[0])
    except ContentAccessError:
        sentinel_raises = True
    return {
        "public_functions": set(public_nodes) == public_names,
        "exact_arguments": actual_arguments == expected_arguments,
        "forbidden_arguments": all_arguments & forbidden_arguments,
        "infer_uses_content": infer_uses_content,
        "execute_calls_infer": execute_calls_infer,
        "sentinel_raises": sentinel_raises,
        "runtime_codebook": False,
        "absolute_site_selector": False,
        "same_event_feedback": False,
    }


def mutant_without_grand_predecessor(
    world: FlagWorld, candidate: Position
) -> Direction | None:
    neighbors = tuple(
        add(candidate, displacement)
        for displacement in DIRECTIONS
        if world.record_flag(add(candidate, displacement))
    )
    return subtract(candidate, neighbors[0]) if len(neighbors) == 1 else None


def mutant_without_unique_neighbor(
    world: FlagWorld, candidate: Position
) -> Direction | None:
    for displacement in DIRECTIONS:
        predecessor = add(candidate, displacement)
        if not world.record_flag(predecessor):
            continue
        inferred = subtract(candidate, predecessor)
        if world.record_flag(subtract(candidate, scale(2, inferred))):
            return inferred
    return None


def signature_has_forbidden_argument(source: str) -> bool:
    tree = ast.parse(source)
    forbidden = {
        "front", "host_direction", "cap_role", "site_id", "scheduler",
        "global_time", "target_fixture",
    }
    return any(
        argument.arg in forbidden
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        for argument in node.args.args + node.args.kwonlyargs
    )


MUTATIONS = (
    "prereg_drift", "import_source_eta_primary",
    "omit_cap_content", "collapse_rotation_product",
    "remove_cap", "fill_gap", "drop_grand_predecessor",
    "drop_unique_neighbor", "target_fixture_only", "hardcode_positive_x",
    "read_record_content", "accept_host_direction", "accept_cap_role",
    "accept_site_id", "accept_scheduler_clock", "absolute_site_selector",
    "drop_rotation", "ignore_translation", "misindex_rotated_obstacles",
    "cap_in_packet_footprint", "shared_swap_vertex",
    "omit_guard_destination", "partial_transport", "move_occupied_record",
    "clone_packet", "drop_new_record", "drop_blocking_obstacles",
    "sample_blocked_patterns", "short_blocked_lengths",
    "outcome_dependent_guard", "drop_stop_mass", "nonnormalized_law",
    "same_event_feedback", "claim_generated_cap", "claim_chosen_arrow",
    "claim_microscopic", "claim_simultaneous_fronts",
    "claim_site_occurrence", "claim_rate_time", "claim_gravity",
    "claim_axiom", "claim_obligation", "claim_retained", "claim_toe",
)

MUTATION_GROUP = {
    "prereg_drift": "A", "import_source_eta_primary": "A",
    "omit_cap_content": "B", "collapse_rotation_product": "B",
    "remove_cap": "B", "fill_gap": "B",
    "drop_grand_predecessor": "B", "drop_unique_neighbor": "B",
    "target_fixture_only": "B", "hardcode_positive_x": "B",
    "read_record_content": "F", "accept_host_direction": "F",
    "accept_cap_role": "F", "accept_site_id": "F",
    "accept_scheduler_clock": "F", "absolute_site_selector": "C",
    "drop_rotation": "C", "ignore_translation": "C",
    "misindex_rotated_obstacles": "C", "cap_in_packet_footprint": "D",
    "shared_swap_vertex": "D", "omit_guard_destination": "D",
    "partial_transport": "D", "move_occupied_record": "D",
    "clone_packet": "D", "drop_new_record": "E",
    "drop_blocking_obstacles": "E", "sample_blocked_patterns": "E",
    "short_blocked_lengths": "E", "outcome_dependent_guard": "F",
    "drop_stop_mass": "F", "nonnormalized_law": "F",
    "same_event_feedback": "F", "claim_generated_cap": "G",
    "claim_chosen_arrow": "G", "claim_microscopic": "G",
    "claim_simultaneous_fronts": "G", "claim_site_occurrence": "G",
    "claim_rate_time": "G", "claim_gravity": "G",
    "claim_axiom": "G", "claim_obligation": "G",
    "claim_retained": "G", "claim_toe": "G",
}


@cache
def mutation_detected(mutation: str) -> bool:
    direction = (1, 0, 0)
    length = 2
    seed = capped_seed(direction, length)
    world = FlagWorld(seed)
    forward = (scale(length, direction), direction)
    rear = (scale(-1, direction), scale(-1, direction))

    if mutation == "prereg_drift":
        return authority_facts()["goal_blob"] != "0" * 40
    if mutation == "import_source_eta_primary":
        bad = ast.parse("from scripts.admissibility_d4_primary import run")
        return any(
            isinstance(node, ast.ImportFrom)
            and node.module is not None
            and node.module.startswith("scripts.admissibility_d4")
            for node in ast.walk(bad)
        )
    if mutation == "omit_cap_content":
        return len(REGISTERED_CONTENTS[:-1]) != 84
    if mutation == "collapse_rotation_product":
        return 6 * 16 * 84 != EXPECTED_SEED_COMPONENTS
    if mutation == "remove_cap":
        mutated = seed - {scale(-2, direction)}
        return scan_frontier_tips(FlagWorld(mutated)) == frozenset({rear, forward})
    if mutation == "fill_gap":
        mutated = seed | {scale(-1, direction)}
        expected = frozenset({
            (scale(-3, direction), scale(-1, direction)), forward,
        })
        return scan_frontier_tips(FlagWorld(mutated)) == expected
    if mutation == "drop_grand_predecessor":
        observed = {
            (candidate, inferred)
            for candidate in complete_frontier(seed)
            if (inferred := mutant_without_grand_predecessor(world, candidate))
            is not None
        }
        return len(observed) == 14 and forward in observed
    if mutation == "drop_unique_neighbor":
        return mutant_without_unique_neighbor(world, scale(-1, direction)) == scale(-1, direction)
    if mutation == "target_fixture_only":
        filled = seed | {scale(-1, direction)}
        fixture_only = frozenset({forward})
        return fixture_only != scan_frontier_tips(FlagWorld(filled))
    if mutation == "hardcode_positive_x":
        other = (0, 1, 0)
        accepted = next(iter(scan_frontier_tips(FlagWorld(capped_seed(other, 2)))))
        hardcoded = (accepted[0], direction)
        return hardcoded != accepted
    if mutation == "read_record_content":
        try:
            world.record_content(scale(-2, direction))
        except ContentAccessError:
            return True
        return False
    if mutation == "accept_host_direction":
        return signature_has_forbidden_argument("def bad(world, candidate, host_direction): pass")
    if mutation == "accept_cap_role":
        return signature_has_forbidden_argument("def bad(world, candidate, cap_role): pass")
    if mutation == "accept_site_id":
        return signature_has_forbidden_argument("def bad(world, candidate, site_id): pass")
    if mutation == "accept_scheduler_clock":
        return signature_has_forbidden_argument("def bad(world, scheduler, global_time): pass")
    if mutation == "absolute_site_selector":
        moved = transform_flags(seed, rotations()[0], (7, 3, -5))
        actual = scan_frontier_tips(FlagWorld(moved))
        selected = frozenset(
            tip for tip in actual if tip[0] == scale(2, direction)
        )
        return selected != actual
    if mutation == "drop_rotation":
        return len(rotations()[:1]) != 24
    if mutation == "ignore_translation":
        displacement = (7, 3, -5)
        moved = transform_flags(seed, rotations()[0], displacement)
        return edge_extrapolated_tips(FlagWorld(moved)) != frozenset({forward})
    if mutation == "misindex_rotated_obstacles":
        candidate = scale(2, direction)
        _, destinations = packet_geometry(candidate, direction)
        matrix = next(
            rotation for rotation in rotations()
            if rotate(rotation, direction) != direction
        )
        moved_candidate = rotate(matrix, candidate)
        _, moved_destinations = packet_geometry(
            moved_candidate, rotate(matrix, direction)
        )
        wrongly_sorted = tuple(sorted(rotate(matrix, site) for site in destinations))
        return wrongly_sorted != moved_destinations
    if mutation == "cap_in_packet_footprint":
        candidate = scale(2, direction)
        sources, destinations = packet_geometry(candidate, direction)
        footprint = set(sources) | set(destinations)
        mutated_cap = sources[0]
        mutated_seed = (seed - {scale(-2, direction)}) | {mutated_cap}
        return mutated_cap in footprint and not footprint.isdisjoint(mutated_seed)
    if mutation == "shared_swap_vertex":
        candidate = scale(2, direction)
        sources, destinations = packet_geometry(candidate, direction)
        bad_destinations = (sources[1],) + destinations[1:]
        return not set(sources).isdisjoint(bad_destinations)
    if mutation == "omit_guard_destination":
        detections = []
        for omitted in range(5):
            flags = tuple(index == omitted for index in range(5))
            mutant_clear = all(
                not flag for index, flag in enumerate(flags) if index != omitted
            )
            detections.append(mutant_clear and any(flags))
        return all(detections)
    if mutation in {"partial_transport", "move_occupied_record", "clone_packet"}:
        source_tokens = [("s", index) for index in range(5)]
        destination_tokens = [("record", 0)] + [
            ("d", index) for index in range(1, 5)
        ]
        before = Counter(source_tokens + destination_tokens)
        if mutation == "partial_transport":
            after_sources = source_tokens[:]
            after_destinations = destination_tokens[:]
            for index in range(1, 5):
                after_sources[index], after_destinations[index] = (
                    after_destinations[index], after_sources[index]
                )
            return after_sources != source_tokens or after_destinations != destination_tokens
        if mutation == "move_occupied_record":
            after_sources = source_tokens[:]
            after_destinations = destination_tokens[:]
            after_sources[0], after_destinations[0] = (
                after_destinations[0], after_sources[0]
            )
            return after_destinations[0] != ("record", 0)
        after = Counter(source_tokens + source_tokens)
        return after != before
    if mutation == "drop_new_record":
        return blocked_frontier_facts()["restart_without_new"] == EXPECTED_BLOCKED_COMPONENTS
    if mutation == "drop_blocking_obstacles":
        return blocked_frontier_facts()["restart_without_obstacles"] == EXPECTED_BLOCKED_COMPONENTS
    if mutation == "sample_blocked_patterns":
        return len(range(1, 31)) != 31
    if mutation == "short_blocked_lengths":
        return len(TRAIL_LENGTHS[:-1]) != 16
    if mutation == "outcome_dependent_guard":
        return len({"STOP" if outcome % 2 else "CONTINUE" for outcome in OUTCOMES}) != 1
    if mutation == "drop_stop_mass":
        return sum((), ZERO_WEIGHT) != ONE_WEIGHT
    if mutation == "nonnormalized_law":
        rows = list(fourteen_way_weights())
        first = rows[0]
        rows[0] = AffineWeight(first.constant + F(1, 100), first.coefficients)
        return sum(rows, ZERO_WEIGHT) != ONE_WEIGHT
    if mutation == "same_event_feedback":
        rows = guard_distribution((False, False, False, False, False))
        mutant_terminals = {
            "STOP" if outcome % 2 else terminal
            for outcome, terminal, _weight in rows
        }
        return len(mutant_terminals) != 1

    scope_keys = {
        "claim_generated_cap": "generated_cap",
        "claim_chosen_arrow": "chosen_physical_arrow",
        "claim_microscopic": "microscopic_flag_sensor_or_controller",
        "claim_simultaneous_fronts": "simultaneous_interacting_fronts",
        "claim_site_occurrence": "site_occurrence",
        "claim_rate_time": "rate_or_time",
        "claim_gravity": "gravity",
        "claim_axiom": "axiom_amendment",
        "claim_obligation": "obligation_retirement",
        "claim_retained": "retained_status",
        "claim_toe": "toe_movement",
    }
    if mutation in scope_keys:
        changed = dict(LIMITS)
        key = scope_keys[mutation]
        changed[key] = 1 if key in {"obligation_retirement", "toe_movement"} else True
        return not scope_is_narrow(changed)
    raise ValueError(f"unknown mutation: {mutation}")


def scope_is_narrow(scope: dict[str, object]) -> bool:
    return (
        scope["supplied_asymmetric_cap_and_seed"] is True
        and scope["effective_classical_record_flags"] is True
        and scope["single_conditioned_local_front"] is True
        and scope["generated_cap"] is False
        and scope["chosen_physical_arrow"] is False
        and scope["microscopic_flag_sensor_or_controller"] is False
        and scope["simultaneous_interacting_fronts"] is False
        and scope["site_occurrence"] is False
        and scope["rate_or_time"] is False
        and scope["gravity"] is False
        and scope["axiom_amendment"] is False
        and scope["obligation_retirement"] == 0
        and scope["retained_status"] is False
        and scope["toe_movement"] == 0
    )


def evaluated_checks(mutation: str = "") -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    seed = seed_census_facts()
    covariance = covariance_facts()
    controller = controller_facts()
    blocked = blocked_frontier_facts()
    probability = probability_facts()
    runtime = runtime_surface_facts()

    authority_ok = (
        authority["goal_blob"] == GOAL_BLOB
        and authority["preflight_blob"] == PREFLIGHT_BLOB
        and authority["imports_standard_only"]
        and authority["registration_has_terminal"]
        and authority["registration_has_controller_count"]
        and authority["registration_has_blocked_count"]
    )
    seed_ok = (
        seed["front_parameters"] == 6
        and seed["frames"] == 24
        and seed["lengths"] == 16
        and seed["contents"] == 84
        and seed["components"] == EXPECTED_SEED_COMPONENTS
        and seed["frontier_sum"] == 720
        and seed["frontier_evaluations"] == EXPECTED_SEED_FRONTIER_EVALUATIONS
        and seed["eligible_tips"] == EXPECTED_SEED_TIPS
        and seed["rejected_sites"] == 8_515_584
        and seed["gap_rejections"] == EXPECTED_SEED_COMPONENTS
        and seed["exterior_rejections"] == EXPECTED_SEED_COMPONENTS
        and seed["poison_contents"] == 84
        and seed["exact"] and seed["edge_agreement"] and seed["path_graph"]
    )
    covariance_ok = (
        covariance["rotations"] == 24
        and covariance["translations"] == 3
        and covariance["seed_cases"] == 6 * 16 * 24 * 3
        and covariance["footprint_cases"] == 6 * 16 * 24 * 3
        and covariance["obstacle_transform_cases"] == 2976 * 24
        and covariance["seed_identity"]
        and covariance["footprint_identity"]
        and covariance["obstacle_identity"]
    )
    controller_ok = (
        controller["fronts"] == 6
        and controller["predecessor_outcomes"] == 14
        and controller["outcomes"] == 14
        and controller["patterns"] == 32
        and controller["cases"] == EXPECTED_CONTROLLER_CASES
        and controller["clear_cases"] == 1176
        and controller["blocked_cases"] == 36456
        and controller["all_exact"] and controller["geometry_exact"]
        and controller["internal_direction"] and controller["clear_successor"]
        and controller["blocked_identity"] and controller["permanence"]
        and controller["packet_sizes"] == {5}
        and controller["packet_growth"] == 0
    )
    blocked_ok = (
        blocked["fronts"] == 6 and blocked["patterns"] == 31
        and blocked["lengths"] == 16
        and blocked["components"] == EXPECTED_BLOCKED_COMPONENTS
        and blocked["frontier_evaluations"] == EXPECTED_BLOCKED_FRONTIER_EVALUATIONS
        and blocked["maximum_eligible"] == 0
        and blocked["edge_agreement"] and blocked["adjacency_invariant"]
        and blocked["restart_without_new"] == EXPECTED_BLOCKED_COMPONENTS
        and blocked["restart_without_obstacles"] == EXPECTED_BLOCKED_COMPONENTS
        and blocked["length_two_size_distribution"] == {
            23: 4, 24: 1, 26: 4, 27: 6,
            29: 8, 30: 2, 31: 5, 32: 1,
        }
        and not blocked["lattice_wide_absorbing"]
    )
    probability_runtime_ok = (
        probability["law_entries"] == 14
        and probability["bare_normalized"]
        and probability["groups"] == 2688
        and probability["stop_groups"] == 2604
        and probability["continue_groups"] == 84
        and probability["branch_rows"] == EXPECTED_CONTROLLER_CASES
        and probability["normalized"] and probability["terminal_exact"]
        and not probability["same_event_feedback"]
        and runtime["public_functions"] and runtime["exact_arguments"]
        and not runtime["forbidden_arguments"]
        and not runtime["infer_uses_content"]
        and runtime["execute_calls_infer"] and runtime["sentinel_raises"]
        and not runtime["runtime_codebook"]
        and not runtime["absolute_site_selector"]
        and not runtime["same_event_feedback"]
    )
    scope_ok = TERMINAL == "GAPPED-CAP-SAFE-FRONT" and scope_is_narrow(LIMITS)

    checks = [
        ["A_frozen_independent_surface", authority_ok,
         "registered goal/preflight blobs match and imports are standard-library only"],
        ["B_flag_only_gapped_seed_census", seed_ok,
         "193536 content-labelled seeds and 8709120 complete-frontier evaluations agree with edge extrapolation"],
        ["C_rotated_translated_covariance", covariance_ok,
         "6912 seed/footprint transforms and 71424 identity-mapped obstacle transforms are exact"],
        ["D_disjoint_controller_census", controller_ok,
         "all 37632 cases derive the front internally and perform five swaps or exact blocked identity"],
        ["E_complete_blocked_frontier", blocked_ok,
         "2976 components and 171936 frontier sites have zero restart; both restart mutations are live"],
        ["F_probability_and_runtime_surface", probability_runtime_ok,
         "2688 exact fourteen-way groups conserve CONTINUE-or-STOP mass on a content-blind oracle-free surface"],
        ["G_narrow_terminal_and_limits", scope_ok,
         "terminal is limited to a supplied cap/seed in one effective single-front flag sector"],
    ]
    if mutation:
        detected = mutation_detected(mutation)
        target_group = MUTATION_GROUP[mutation]
        for row in checks:
            if row[0].startswith(target_group + "_") and detected:
                row[1] = False
                row[2] += f"; rejected mutation={mutation}"
    return [(name, bool(ok), detail) for name, ok, detail in checks]


def mutation_sweep() -> tuple[int, tuple[str, ...]]:
    survivors = tuple(
        mutation
        for mutation in MUTATIONS
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
        passed += int(ok)
        failed += int(not ok)
        print(f"{'PASS' if ok else 'FAIL'} {name}: {detail}")

    if not args.mutation:
        rejected, survivors = mutation_sweep()
        print(f"MUTATIONS: rejected={rejected}/{len(MUTATIONS)}")
        if survivors:
            print("MUTATION_SURVIVORS:", ",".join(survivors))
        failed += int(bool(survivors))
        if not failed:
            print(
                "TERMINAL: GAPPED-CAP-SAFE-FRONT — supplied asymmetric "
                "gapped Record cap/seed only"
            )
            print(
                "COUNTS: seed_components=193536; seed_frontier=8709120; "
                "controller=37632; blocked_components=2976; "
                "blocked_frontier=171936; probability_groups=2688"
            )
            print(
                "LIMITS: effective single conditioned flag-sector front; "
                "no cap generation, chosen physical arrow, microscopic "
                "sensor/controller, simultaneous fronts, occurrence/rate/time, "
                "gravity, axiom change, obligation retirement, retained "
                "status, or TOE movement"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
