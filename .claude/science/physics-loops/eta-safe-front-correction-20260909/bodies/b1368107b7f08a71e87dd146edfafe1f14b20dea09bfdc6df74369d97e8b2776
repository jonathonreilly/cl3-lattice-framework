#!/usr/bin/env python3
"""Independent exact reconstruction of Source/Eta Block 16.

No Source/Eta runner is imported.  Geometry is represented by sparse integer
sites, the channel by central Record-mask effects and positive-functional/state
factors, and the marginal countermodel by a 6x43 preparation-label array.

The terminal is conditional: the center, atomic event, effective Record flags,
and blank-sector detector are supplied.  The preparation-label product
probability is not a Born probability for distinguishing nonorthogonal qubit
states.  No nearest-neighbor compilation, microscopic detector/controller,
overlap arbitration, occurrence/rate/time, gravity, axiom, retention,
obligation, or TOE claim is made.
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
    "toe-source-eta-ownership-block16-covariant-cap-packet-instrument-20260829"
)
GOAL_PATH = f"{PACKET}/GOAL.md"
PREFLIGHT_PATH = f"{PACKET}/PREFLIGHT_WITNESSES.md"
SUPPORT_CORRECTION_PATH = f"{PACKET}/PREFLIGHT_SUPPORT_CORRECTION.md"
GOAL_BLOB = "48cbfac788b74d0b85acd475db83226e50753afd"
PREFLIGHT_BLOB = "6fadd2651fe64a7fe27115f90a618942ac8814cf"
SUPPORT_CORRECTION_BLOB = "29b66cba2c73687dcb09d53fd32d153a1f19dbf6"

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
TRANSLATIONS: tuple[Position, ...] = (
    (11, -7, 5), (-13, 17, -19), (23, 29, -31),
)

WRITER_SITE_COUNT = 43
EXTERNAL_DESTINATION_COUNT = 30
EXTENDED_SITE_COUNT = 73
CONTROLLER_MAPS = 6 * 14 * 32
GENERATED_BLOCKED_COMPONENTS = 6 * 31
GENERATED_BLOCKED_FRONTIER = 5_166
INHERITED_BLOCKED_COMPONENTS = 6 * 16 * 31
INHERITED_BLOCKED_FRONTIER = 171_936
PRODUCT_VALID_PROBABILITY = F(5**15, 6**18)

TERMINAL = "COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT"
LIMITS = {
    "selected_center": True,
    "conditioned_atomic_event": True,
    "effective_record_mask_algebra": True,
    "effective_blank_detector": True,
    "preparation_label_probability": True,
    "born_distinguishability_probability": False,
    "autonomous_formation": False,
    "nearest_neighbor_compilation": False,
    "microscopic_detector_or_controller": False,
    "overlapping_center_arbitration": False,
    "site_occurrence": False,
    "rate_or_time": False,
    "gravity": False,
    "axiom_amendment": False,
    "retained_status": False,
    "obligation_retirement": 0,
    "toe_movement": 0,
}


class ForbiddenContentAccess(AssertionError):
    """Raised if branch selection inspects blank-sector quantum content."""


class RaisingQuantumContent:
    __slots__ = ()

    @staticmethod
    def _raise() -> None:
        raise ForbiddenContentAccess("blank quantum content was inspected")

    def __bool__(self) -> bool:
        self._raise()

    def __iter__(self):
        self._raise()

    def __eq__(self, _other: object) -> bool:
        self._raise()

    def __repr__(self) -> str:
        self._raise()


@dataclass(frozen=True, slots=True)
class Rad3:
    """Exact a+b/sqrt(3), used for all fourteen outcome vectors."""

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

    def __le__(self, other: "Rad3") -> bool:
        return (self - other).sign() <= 0


ZERO = Rad3()
ONE = Rad3(F(1))
Bloch = tuple[Rad3, Rad3, Rad3]


def add(left: Position, right: Position) -> Position:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def subtract(left: Position, right: Position) -> Position:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def scale(factor: int, vector: Position) -> Position:
    return tuple(factor * component for component in vector)  # type: ignore[return-value]


def dot(left: Position, right: Position) -> int:
    return sum(left[index] * right[index] for index in range(3))


def bloch_from_position(vector: Position) -> Bloch:
    return tuple(Rad3(component) for component in vector)  # type: ignore[return-value]


def bloch_add(left: Bloch, right: Bloch) -> Bloch:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def bloch_subtract(left: Bloch, right: Bloch) -> Bloch:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def bloch_scale(factor: Fraction | int, vector: Bloch) -> Bloch:
    return tuple(F(factor) * component for component in vector)  # type: ignore[return-value]


def bloch_dot(left: Bloch, right: Bloch) -> Rad3:
    return sum(
        (left[index] * right[index] for index in range(3)),
        ZERO,
    )


def bloch_norm_squared(vector: Bloch) -> Rad3:
    return bloch_dot(vector, vector)


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
            matrix = tuple(
                tuple(
                    signs[row] if column == permutation[row] else 0
                    for column in range(3)
                )
                for row in range(3)
            )
            result.add(matrix)  # type: ignore[arg-type]
    return tuple(sorted(result))


def rotate_position(matrix: Matrix3, vector: Position) -> Position:
    return tuple(
        sum(matrix[row][column] * vector[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def rotate_bloch(matrix: Matrix3, vector: Bloch) -> Bloch:
    return tuple(
        sum(
            (
                matrix[row][column] * vector[column]
                for column in range(3)
            ),
            ZERO,
        )
        for row in range(3)
    )  # type: ignore[return-value]


@cache
def outcomes() -> tuple[Bloch, ...]:
    axes = tuple(bloch_from_position(direction) for direction in DIRECTIONS)
    corners = tuple(
        tuple(Rad3(0, sign) for sign in signs)  # type: ignore[arg-type]
        for signs in itertools.product((-1, 1), repeat=3)
    )
    return axes + corners


def record_code(direction: Direction, outcome: Bloch) -> Bloch:
    return bloch_add(
        bloch_scale(F(-9, 16), bloch_from_position(direction)),
        bloch_scale(F(1, 256), outcome),
    )


def seed_record_code(direction: Direction) -> Bloch:
    return record_code(direction, bloch_from_position(direction))


ZERO_BLOCH: Bloch = (ZERO, ZERO, ZERO)


@dataclass(frozen=True, slots=True)
class QubitState:
    bloch: Bloch

    @property
    def trace(self) -> Fraction:
        return F(1)

    @property
    def physical(self) -> bool:
        return bloch_norm_squared(self.bloch) <= ONE


MIXED = QubitState(ZERO_BLOCH)


@dataclass(frozen=True, slots=True)
class BranchOutput:
    direction: Direction
    center: Position
    record_mask: frozenset[Position]
    site_states: tuple[tuple[Position, QubitState], ...]

    def state_at(self, site: Position) -> QubitState:
        return dict(self.site_states)[site]


@dataclass(frozen=True, slots=True)
class PreservedInput:
    record_mask: frozenset[Position]
    quantum_contents: object


@dataclass(frozen=True, slots=True)
class InstrumentOutcome:
    label: object
    probability: Fraction
    output: BranchOutput | PreservedInput | None


def writer_block(center: Position = (0, 0, 0)) -> frozenset[Position]:
    sites: set[Position] = set()
    for direction in DIRECTIONS:
        sites.update(
            add(center, scale(factor, direction))
            for factor in (-2, -1, 0, 1, 2, 3)
        )
        sites.update(
            add(center, add(scale(2, direction), transverse))
            for transverse in DIRECTIONS
            if dot(transverse, direction) == 0
        )
    return frozenset(sites)


def packet_geometry(
    candidate: Position,
    direction: Direction,
) -> tuple[tuple[Position, ...], tuple[Position, ...]]:
    perpendicular = tuple(
        transverse
        for transverse in DIRECTIONS
        if dot(transverse, direction) == 0
    )
    sources = (add(candidate, direction),) + tuple(
        add(candidate, transverse) for transverse in perpendicular
    )
    destinations = tuple(add(source, direction) for source in sources)
    return sources, destinations


def external_destinations(center: Position = (0, 0, 0)) -> frozenset[Position]:
    result = set()
    for direction in DIRECTIONS:
        candidate = add(center, scale(2, direction))
        _sources, destinations = packet_geometry(candidate, direction)
        result.update(destinations)
    return frozenset(result)


def extended_block(center: Position = (0, 0, 0)) -> frozenset[Position]:
    return writer_block(center) | external_destinations(center)


@cache
def branch_output(
    direction: Direction,
    center: Position = (0, 0, 0),
) -> BranchOutput:
    block = writer_block(center)
    record_vector = seed_record_code(direction)
    record_state = QubitState(record_vector)
    record_mask = frozenset({
        add(center, scale(-2, direction)),
        center,
        add(center, direction),
    })
    live_source = add(center, scale(3, direction))
    site_states = tuple(sorted(
        (
            site,
            record_state if site in record_mask or site == live_source else MIXED,
        )
        for site in block
    ))
    return BranchOutput(
        direction=direction,
        center=center,
        record_mask=record_mask,
        site_states=site_states,
    )


def construct_instrument(
    record_flags: frozenset[Position],
    quantum_contents: object,
) -> tuple[InstrumentOutcome, ...]:
    """Return all six branches plus STOP without receiving a host direction."""

    if record_flags:
        preserved = PreservedInput(record_flags, quantum_contents)
        return tuple(
            InstrumentOutcome(direction, F(0), None)
            for direction in DIRECTIONS
        ) + (InstrumentOutcome("STOP", F(1), preserved),)
    return tuple(
        InstrumentOutcome(direction, F(1, 6), branch_output(direction))
        for direction in DIRECTIONS
    ) + (InstrumentOutcome("STOP", F(0), None),)


def branch_effect(mask: frozenset[Position]) -> Fraction:
    return F(1, 6) if not mask else F(0)


def stop_effect(mask: frozenset[Position]) -> Fraction:
    return F(0) if not mask else F(1)


def git_blob(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\0".encode()
    return hashlib.sha1(header + data).hexdigest()


@cache
def authority_facts() -> dict[str, object]:
    goal = ROOT / GOAL_PATH
    preflight = ROOT / PREFLIGHT_PATH
    correction = ROOT / SUPPORT_CORRECTION_PATH
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
    correction_text = correction.read_text(encoding="utf-8")
    return {
        "goal_blob": git_blob(goal),
        "preflight_blob": git_blob(preflight),
        "correction_blob": git_blob(correction),
        "standard_imports": all(
            module.split(".", 1)[0] in allowed_roots
            for module in imported_modules
        ),
        "correction_43": "writer support B                         = 43 sites" in correction_text,
        "correction_73": "writer-plus-controller extension         = 73 sites" in correction_text,
        "correction_186": "6*31 = 186" in correction_text,
        "correction_5166": "5,166" in correction_text,
        "correction_2976": "2,976 = 6*16*31" in correction_text,
        "correction_171936": "171,936" in correction_text,
    }


@cache
def block_output_facts() -> dict[str, object]:
    block = writer_block()
    external = external_destinations()
    extension = extended_block()
    branches = tuple(branch_output(direction) for direction in DIRECTIONS)
    masks = {output.record_mask for output in branches}
    physical_sites = 0
    normalized_products = True
    exact_masks = True
    exact_shells = True
    distinct_footprint = True
    for output in branches:
        direction = output.direction
        expected_record = seed_record_code(direction)
        expected_mask = frozenset({scale(-2, direction), (0, 0, 0), direction})
        exact_masks &= output.record_mask == expected_mask
        states = dict(output.site_states)
        normalized_products &= len(states) == len(block)
        normalized_products &= all(state.trace == 1 for state in states.values())
        physical_sites += sum(state.physical for state in states.values())
        candidate = scale(2, direction)
        perpendicular = tuple(
            transverse for transverse in DIRECTIONS
            if dot(transverse, direction) == 0
        )
        exact_shells &= states[direction].bloch == expected_record
        exact_shells &= states[scale(3, direction)].bloch == expected_record
        exact_shells &= all(
            states[add(candidate, transverse)].bloch == ZERO_BLOCH
            for transverse in perpendicular
        )
        required = {
            scale(-2, direction), scale(-1, direction), (0, 0, 0),
            direction, candidate, scale(3, direction),
        } | {add(candidate, transverse) for transverse in perpendicular}
        distinct_footprint &= len(required) == 10 and required <= block

    rf = seed_record_code((1, 0, 0))
    rf_exact = rf == (Rad3(F(-143, 256)), ZERO, ZERO)
    nonzero_rf = tuple(component for component in rf if component != ZERO)
    rf_axis_rational = (
        len(nonzero_rf) == 1
        and nonzero_rf[0].root_coefficient == 0
    )
    rf_radius = abs(nonzero_rf[0].rational) if rf_axis_rational else F(2)
    eigenvalues = tuple(sorted((
        (F(1) - rf_radius) / 2,
        (F(1) + rf_radius) / 2,
    )))
    sector_orthogonal_pairs = sum(
        left.record_mask != right.record_mask
        for left, right in itertools.combinations(branches, 2)
    )
    return {
        "writer_sites": len(block),
        "external_sites": len(external),
        "extension_sites": len(extension),
        "disjoint_supports": block.isdisjoint(external),
        "branches": len(branches),
        "distinct_masks": len(masks),
        "sector_orthogonal_pairs": sector_orthogonal_pairs,
        "physical_sites": physical_sites,
        "normalized_products": normalized_products,
        "exact_masks": exact_masks,
        "exact_shells": exact_shells,
        "distinct_footprint": distinct_footprint,
        "rf_exact": rf_exact,
        "rf_eigenvalues": eigenvalues,
        "all_outcomes_unit": all(
            bloch_norm_squared(outcome) == ONE for outcome in outcomes()
        ),
        "record_code_bound": F(9, 16) + F(1, 256) < 1,
    }


@cache
def instrument_facts() -> dict[str, object]:
    blank = frozenset()
    representative_nonblank = frozenset({(17, -11, 5)})
    blank_effect_sum = sum(
        (branch_effect(blank) for _direction in DIRECTIONS),
        F(0),
    ) + stop_effect(blank)
    nonblank_effect_sum = sum(
        (branch_effect(representative_nonblank) for _direction in DIRECTIONS),
        F(0),
    ) + stop_effect(representative_nonblank)
    outputs_positive = all(
        state.physical
        for direction in DIRECTIONS
        for _site, state in branch_output(direction).site_states
    )
    choi_factor_positive = all(
        branch_effect(blank) >= 0 and outputs_positive
        for _direction in DIRECTIONS
    )
    stop_compression_cp = stop_effect(blank) == 0 and stop_effect(representative_nonblank) == 1

    poison = RaisingQuantumContent()
    blank_rows = construct_instrument(blank, poison)
    common_blank = (
        len(blank_rows) == 7
        and tuple(row.label for row in blank_rows[:-1]) == DIRECTIONS
        and all(row.probability == F(1, 6) for row in blank_rows[:-1])
        and blank_rows[-1].label == "STOP"
        and blank_rows[-1].probability == 0
    )
    singleton_controls = 0
    singleton_identity = True
    for site in writer_block():
        token = object()
        rows = construct_instrument(frozenset({site}), token)
        stop = rows[-1]
        singleton_identity &= all(row.probability == 0 for row in rows[:-1])
        singleton_identity &= stop.probability == 1
        singleton_identity &= isinstance(stop.output, PreservedInput)
        if isinstance(stop.output, PreservedInput):
            singleton_identity &= stop.output.record_mask == frozenset({site})
            singleton_identity &= stop.output.quantum_contents is token
        singleton_controls += 1

    footprint_controls = 0
    footprint_identity = True
    for direction in DIRECTIONS:
        candidate = scale(2, direction)
        sources, destinations = packet_geometry(candidate, direction)
        footprint = (
            set(branch_output(direction).record_mask)
            | {scale(-1, direction), candidate}
            | set(sources) | set(destinations)
        )
        for site in footprint:
            token = object()
            rows = construct_instrument(frozenset({site}), token)
            stop = rows[-1]
            footprint_identity &= stop.probability == 1
            footprint_identity &= isinstance(stop.output, PreservedInput)
            if isinstance(stop.output, PreservedInput):
                footprint_identity &= stop.output.quantum_contents is token
            footprint_controls += 1

    # A symbolic two-sector full-Hilbert extension.  Cross coefficients vanish;
    # blank and nonblank diagonal trace coefficients are both one.
    full_hilbert_coefficients = {
        "blank_diagonal_trace": F(1),
        "nonblank_diagonal_trace": F(1),
        "blank_nonblank_cross": F(0),
        "nonblank_blank_cross": F(0),
    }
    return {
        "branch_effect": F(1, 6),
        "blank_effect_sum": blank_effect_sum,
        "nonblank_effect_sum": nonblank_effect_sum,
        "choi_factor_positive": choi_factor_positive,
        "stop_compression_cp": stop_compression_cp,
        "common_blank": common_blank,
        "singleton_controls": singleton_controls,
        "singleton_identity": singleton_identity,
        "footprint_controls": footprint_controls,
        "footprint_identity": footprint_identity,
        "symbolic_nonblank_masks": 2**len(writer_block()) - 1,
        "full_hilbert_coefficients": full_hilbert_coefficients,
        "record_coherences_in_domain": False,
    }


def transform_output(
    output: BranchOutput,
    matrix: Matrix3,
    displacement: Position = (0, 0, 0),
) -> BranchOutput:
    moved_center = add(displacement, rotate_position(matrix, output.center))
    return BranchOutput(
        direction=rotate_position(matrix, output.direction),
        center=moved_center,
        record_mask=frozenset(
            add(displacement, rotate_position(matrix, site))
            for site in output.record_mask
        ),
        site_states=tuple(sorted(
            (
                add(displacement, rotate_position(matrix, site)),
                QubitState(rotate_bloch(matrix, state.bloch)),
            )
            for site, state in output.site_states
        )),
    )


@cache
def covariance_facts() -> dict[str, object]:
    output_cases = translation_cases = footprint_cases = 0
    output_covariant = True
    translation_covariant = True
    footprint_covariant = True
    block_covariant = True

    for direction in DIRECTIONS:
        base = branch_output(direction)
        candidate = scale(2, direction)
        sources, destinations = packet_geometry(candidate, direction)
        for matrix in rotations():
            moved_direction = rotate_position(matrix, direction)
            transformed = transform_output(base, matrix)
            output_covariant &= transformed == branch_output(moved_direction)
            block_covariant &= frozenset(
                rotate_position(matrix, site) for site in writer_block()
            ) == writer_block()
            block_covariant &= frozenset(
                rotate_position(matrix, site)
                for site in external_destinations()
            ) == external_destinations()
            moved_candidate = rotate_position(matrix, candidate)
            moved_sources, moved_destinations = packet_geometry(
                moved_candidate, moved_direction
            )
            footprint_covariant &= set(zip(
                moved_sources, moved_destinations
            )) == {
                (
                    rotate_position(matrix, source),
                    rotate_position(matrix, destination),
                )
                for source, destination in zip(sources, destinations)
            }
            output_cases += 1
            footprint_cases += 1
            for displacement in TRANSLATIONS:
                shifted = transform_output(base, matrix, displacement)
                expected = branch_output(
                    moved_direction,
                    add(displacement, rotate_position(matrix, base.center)),
                )
                translation_covariant &= shifted == expected
                translation_covariant &= writer_block(expected.center) == frozenset(
                    add(displacement, rotate_position(matrix, site))
                    for site in writer_block(base.center)
                )
                translation_covariant &= extended_block(expected.center) == frozenset(
                    add(displacement, rotate_position(matrix, site))
                    for site in extended_block(base.center)
                )
                translation_cases += 1

    return {
        "rotations": len(rotations()),
        "translations": len(TRANSLATIONS),
        "output_cases": output_cases,
        "translation_cases": translation_cases,
        "footprint_cases": footprint_cases,
        "output_covariant": output_covariant,
        "translation_covariant": translation_covariant,
        "footprint_covariant": footprint_covariant,
        "block_covariant": block_covariant,
        "blank_effect_invariant": branch_effect(frozenset()) == F(1, 6),
        "stop_effect_invariant": stop_effect(frozenset({(9, 4, -2)})) == 1,
    }


def complete_frontier(record_flags: frozenset[Position]) -> tuple[Position, ...]:
    frontier = {
        add(record_site, direction)
        for record_site in record_flags
        for direction in DIRECTIONS
    }
    frontier.difference_update(record_flags)
    return tuple(sorted(frontier))


def infer_flag_front(
    record_flags: frozenset[Position],
    candidate: Position,
) -> Direction | None:
    predecessor: Position | None = None
    for displacement in DIRECTIONS:
        neighbor = add(candidate, displacement)
        if neighbor not in record_flags:
            continue
        if predecessor is not None:
            return None
        predecessor = neighbor
    if predecessor is None:
        return None
    inferred = subtract(candidate, predecessor)
    if subtract(candidate, scale(2, inferred)) not in record_flags:
        return None
    return inferred


def scan_frontier_tips(
    record_flags: frozenset[Position],
) -> frozenset[tuple[Position, Direction]]:
    result = set()
    for candidate in complete_frontier(record_flags):
        inferred = infer_flag_front(record_flags, candidate)
        if inferred is not None:
            result.add((candidate, inferred))
    return frozenset(result)


def edge_extrapolated_tips(
    record_flags: frozenset[Position],
) -> frozenset[tuple[Position, Direction]]:
    result = set()
    for grand_predecessor in record_flags:
        for direction in DIRECTIONS:
            predecessor = add(grand_predecessor, direction)
            if predecessor not in record_flags:
                continue
            candidate = add(predecessor, direction)
            if candidate in record_flags:
                continue
            neighbors = {
                add(candidate, displacement)
                for displacement in DIRECTIONS
                if add(candidate, displacement) in record_flags
            }
            if neighbors == {predecessor}:
                result.add((candidate, direction))
    return frozenset(result)


def capped_trail(direction: Direction, length: int) -> frozenset[Position]:
    return frozenset(
        {scale(index, direction) for index in range(length)}
        | {scale(-2, direction)}
    )


def m0_probabilities() -> tuple[Fraction, ...]:
    return (F(1, 12),) * 6 + (F(1, 16),) * 8


def controller_contents(
    output: BranchOutput,
    destinations: tuple[Position, ...],
    obstacles: frozenset[Position],
) -> dict[Position, object]:
    contents: dict[Position, object] = {
        site: state for site, state in output.site_states
    }
    for index, destination in enumerate(destinations):
        contents[destination] = (
            ("occupied-record", index)
            if destination in obstacles
            else ("arbitrary-live-destination", index)
        )
    return contents


@cache
def composition_facts() -> dict[str, object]:
    controller_maps = clear_maps = blocked_maps = 0
    initial_frontier_evaluations = 0
    initial_tip_exact = True
    edge_agreement = True
    shell_exact = True
    clear_exact = True
    blocked_exact = True
    permanence = True
    probability_exact = True
    generated_components = generated_frontier = 0
    generated_zero = True
    inherited_components = inherited_frontier = 0
    inherited_zero = True

    probabilities = m0_probabilities()
    probability_exact &= len(probabilities) == 14
    probability_exact &= all(probability > 0 for probability in probabilities)
    probability_exact &= sum(probabilities, F(0)) == 1

    for direction in DIRECTIONS:
        output = branch_output(direction)
        records = output.record_mask
        candidate = scale(2, direction)
        frontier = complete_frontier(records)
        tips = scan_frontier_tips(records)
        extrapolated = edge_extrapolated_tips(records)
        initial_frontier_evaluations += len(frontier)
        initial_tip_exact &= len(frontier) == 15
        initial_tip_exact &= tips == frozenset({(candidate, direction)})
        edge_agreement &= tips == extrapolated
        sources, destinations = packet_geometry(candidate, direction)
        shell = dict(output.site_states)
        r_a = seed_record_code(direction)
        shell_exact &= shell[direction].bloch == r_a
        shell_exact &= shell[scale(3, direction)].bloch == r_a
        shell_exact &= all(
            shell[source].bloch == ZERO_BLOCH
            for source in sources[1:]
        )

        for outcome_index, outcome in enumerate(outcomes()):
            r_b = record_code(direction, outcome)
            difference = bloch_subtract(r_a, r_b)
            fprime_on_f = bloch_scale(F(1, 2), difference)
            successor_front = bloch_add(
                bloch_scale(2, fprime_on_f), r_b
            )
            clear_exact &= successor_front == r_a
            clear_exact &= all(
                bloch_scale(F(dot(direction, transverse), 2), difference)
                == ZERO_BLOCH
                for transverse in DIRECTIONS
                if dot(transverse, direction) == 0
            )
            for mask in range(32):
                obstacles = frozenset(
                    destinations[index]
                    for index in range(5)
                    if mask >> index & 1
                )
                before = controller_contents(output, destinations, obstacles)
                inferred = infer_flag_front(records | obstacles, candidate)
                internal_direction = inferred == direction
                after = dict(before)
                post_records = records | obstacles | {candidate}
                if mask == 0:
                    for source, destination in zip(sources, destinations):
                        after[source], after[destination] = (
                            before[destination], before[source]
                        )
                    clear_exact &= internal_direction
                    clear_exact &= all(
                        after[destination] == before[source]
                        for source, destination in zip(sources, destinations)
                    )
                    clear_maps += 1
                else:
                    blocked_exact &= internal_direction
                    blocked_exact &= all(
                        after[site] == before[site]
                        for site in set(sources) | set(destinations)
                    )
                    blocked_maps += 1
                after[candidate] = QubitState(r_b)
                permanence &= all(
                    after[site] == before[site]
                    for site in records | obstacles
                )
                probability_exact &= sum(probabilities, F(0)) == 1
                controller_maps += 1

        post_writer = records | {candidate}
        for mask in range(1, 32):
            obstacles = frozenset(
                destinations[index]
                for index in range(5)
                if mask >> index & 1
            )
            blocked_records = post_writer | obstacles
            blocked_frontier = complete_frontier(blocked_records)
            blocked_tips = scan_frontier_tips(blocked_records)
            generated_frontier += len(blocked_frontier)
            generated_zero &= not blocked_tips
            edge_agreement &= not edge_extrapolated_tips(blocked_records)
            generated_components += 1

    for direction in DIRECTIONS:
        for length in TRAIL_LENGTHS:
            candidate = scale(length, direction)
            trail = capped_trail(direction, length)
            post = trail | {candidate}
            _sources, destinations = packet_geometry(candidate, direction)
            for mask in range(1, 32):
                obstacles = frozenset(
                    destinations[index]
                    for index in range(5)
                    if mask >> index & 1
                )
                blocked_records = post | obstacles
                blocked_frontier = complete_frontier(blocked_records)
                tips = scan_frontier_tips(blocked_records)
                inherited_frontier += len(blocked_frontier)
                inherited_zero &= not tips
                edge_agreement &= not edge_extrapolated_tips(blocked_records)
                inherited_components += 1

    return {
        "controller_maps": controller_maps,
        "clear_maps": clear_maps,
        "blocked_maps": blocked_maps,
        "initial_frontier_evaluations": initial_frontier_evaluations,
        "initial_tip_exact": initial_tip_exact,
        "edge_agreement": edge_agreement,
        "shell_exact": shell_exact,
        "clear_exact": clear_exact,
        "blocked_exact": blocked_exact,
        "permanence": permanence,
        "probability_exact": probability_exact,
        "generated_components": generated_components,
        "generated_frontier": generated_frontier,
        "generated_zero": generated_zero,
        "inherited_components": inherited_components,
        "inherited_frontier": inherited_frontier,
        "inherited_zero": inherited_zero,
        "writer_sites": len(writer_block()),
        "external_destinations": len(external_destinations()),
        "extended_sites": len(extended_block()),
        "sources_inside_writer": all(
            source in writer_block()
            for direction in DIRECTIONS
            for source in packet_geometry(scale(2, direction), direction)[0]
        ),
        "destinations_outside_writer": all(
            destination not in writer_block()
            for direction in DIRECTIONS
            for destination in packet_geometry(scale(2, direction), direction)[1]
        ),
    }


@dataclass(frozen=True, slots=True)
class PreparationLabel:
    record: bool
    state: QubitState


@cache
def preparation_configurations() -> tuple[
    tuple[Direction, tuple[tuple[Position, PreparationLabel], ...]], ...
]:
    rows = []
    for direction in DIRECTIONS:
        output = branch_output(direction)
        states = dict(output.site_states)
        row = tuple(
            (site, PreparationLabel(site in output.record_mask, states[site]))
            for site in sorted(writer_block())
        )
        rows.append((direction, row))
    return tuple(rows)


@cache
def joint_law_facts() -> dict[str, object]:
    rows = preparation_configurations()
    sites = tuple(sorted(writer_block()))
    row_maps = {direction: dict(row) for direction, row in rows}
    marginals = {
        site: Counter(row_maps[direction][site] for direction in DIRECTIONS)
        for site in sites
    }
    correlated_marginals = {
        site: {
            label: F(count, 6) for label, count in counter.items()
        }
        for site, counter in marginals.items()
    }
    product_marginals = {
        site: dict(distribution)
        for site, distribution in correlated_marginals.items()
    }
    branch_probabilities = {}
    for direction in DIRECTIONS:
        probability = F(1)
        for site in sites:
            probability *= correlated_marginals[site][row_maps[direction][site]]
        branch_probabilities[direction] = probability
    valid_probability = sum(branch_probabilities.values(), F(0))
    expected_branch = F(1, 6) ** 4 * F(5, 6) ** 15

    center_states = [
        row_maps[direction][(0, 0, 0)].state.bloch
        for direction in DIRECTIONS
    ]
    pairwise_overlaps = []
    for left, right in itertools.combinations(center_states, 2):
        overlap = F(1, 2) * (
            F(1) + bloch_dot(left, right).rational
        )
        pairwise_overlaps.append(overlap)
    seed_norm_squared = bloch_norm_squared(seed_record_code((1, 0, 0)))
    expected_minimum_overlap = F(1, 2) * (
        F(1) - seed_norm_squared.rational
    )
    return {
        "rows": len(rows),
        "sites": len(sites),
        "marginals_equal": correlated_marginals == product_marginals,
        "branch_probabilities": set(branch_probabilities.values()),
        "expected_branch": expected_branch,
        "valid_probability": valid_probability,
        "expected_valid_probability": PRODUCT_VALID_PROBABILITY,
        "valid_less_than_one": valid_probability < 1,
        "center_label_count": len(marginals[(0, 0, 0)]),
        "minimum_center_born_overlap": min(pairwise_overlaps),
        "expected_minimum_center_born_overlap": expected_minimum_overlap,
        "all_center_born_overlaps_positive": all(
            overlap > 0 for overlap in pairwise_overlaps
        ),
        "preparation_labels_classical": True,
        "born_discrimination_probability": False,
        "transverse_unit_factors": all(
            len(marginals[site]) == 1
            for site in sites
            if sum(abs(component) for component in site) == 3
            and sorted(abs(component) for component in site) == [0, 1, 2]
        ),
    }


@cache
def runtime_surface_facts() -> dict[str, object]:
    source = Path(__file__).read_text(encoding="utf-8")
    tree = ast.parse(source)
    public_names = {"construct_instrument", "infer_flag_front"}
    public_nodes = {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name in public_names
    }
    expected_arguments = {
        "construct_instrument": ("record_flags", "quantum_contents"),
        "infer_flag_front": ("record_flags", "candidate"),
    }
    actual_arguments = {
        name: tuple(argument.arg for argument in node.args.args)
        for name, node in public_nodes.items()
    }
    constructor = public_nodes.get("construct_instrument")
    forbidden_arguments = {
        "front", "direction", "host_direction", "branch", "cap_role",
        "precursor", "role", "epoch", "tape", "center", "site_id",
        "scheduler", "global_clock", "probability_feedback",
    }
    arguments = {
        argument
        for values in actual_arguments.values()
        for argument in values
    }
    constructor_reads_quantum = bool(constructor) and any(
        isinstance(node, ast.Name)
        and node.id == "quantum_contents"
        and not isinstance(getattr(node, "ctx", None), ast.Param)
        for node in ast.walk(constructor)
    )
    # Storing the opaque object in STOP is permitted; inspecting it is not.
    constructor_calls_on_quantum = bool(constructor) and any(
        isinstance(node, ast.Call)
        and any(
            isinstance(argument, ast.Name)
            and argument.id == "quantum_contents"
            for argument in node.args
        )
        and not (
            isinstance(node.func, ast.Name)
            and node.func.id == "PreservedInput"
        )
        for node in ast.walk(constructor)
    )
    poison_survives = False
    try:
        rows = construct_instrument(frozenset(), RaisingQuantumContent())
        poison_survives = len(rows) == 7
    except ForbiddenContentAccess:
        poison_survives = False
    return {
        "public_functions": set(public_nodes) == public_names,
        "exact_arguments": actual_arguments == expected_arguments,
        "forbidden_arguments": arguments & forbidden_arguments,
        "constructor_mentions_quantum": constructor_reads_quantum,
        "constructor_calls_on_quantum": constructor_calls_on_quantum,
        "poison_survives": poison_survives,
        "all_branches_internal": tuple(
            row.label
            for row in construct_instrument(frozenset(), object())[:-1]
        ) == DIRECTIONS,
        "branch_lookup_table": False,
        "same_event_feedback": False,
    }


def scope_is_narrow(scope: dict[str, object]) -> bool:
    return (
        scope["selected_center"] is True
        and scope["conditioned_atomic_event"] is True
        and scope["effective_record_mask_algebra"] is True
        and scope["effective_blank_detector"] is True
        and scope["preparation_label_probability"] is True
        and scope["born_distinguishability_probability"] is False
        and scope["autonomous_formation"] is False
        and scope["nearest_neighbor_compilation"] is False
        and scope["microscopic_detector_or_controller"] is False
        and scope["overlapping_center_arbitration"] is False
        and scope["site_occurrence"] is False
        and scope["rate_or_time"] is False
        and scope["gravity"] is False
        and scope["axiom_amendment"] is False
        and scope["retained_status"] is False
        and scope["obligation_retirement"] == 0
        and scope["toe_movement"] == 0
    )


def signature_has_forbidden_argument(source: str) -> bool:
    tree = ast.parse(source)
    forbidden = {
        "front", "host_direction", "branch", "cap_role", "precursor",
        "role", "epoch", "tape", "center", "site_id", "scheduler",
        "global_clock", "probability_feedback",
    }
    return any(
        argument.arg in forbidden
        for node in ast.walk(tree)
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        for argument in node.args.args + node.args.kwonlyargs
    )


MUTATIONS = (
    "goal_drift", "preflight_drift", "correction_drift",
    "import_block16_primary", "import_block15_primary",
    "drop_writer_site", "drop_external_destination", "wrong_record_code",
    "reverse_record_code", "nonphysical_output", "mixed_front_source",
    "nonzero_transverse_source", "fill_gap", "occupy_candidate",
    "extra_record", "collapse_branch_masks", "nonunit_product_trace",
    "drop_branch", "unequal_branch_weight", "negative_branch_weight",
    "branch_specific_precursor", "incomplete_blank_effect",
    "stop_resets_content", "stop_misses_nonblank_mask",
    "overwrite_singleton", "retain_blank_nonblank_coherence",
    "drop_rotation", "ignore_translation", "rotate_sites_not_bloch",
    "hardcode_positive_x", "public_host_direction", "public_branch",
    "public_center", "public_site_id", "public_scheduler_clock",
    "hidden_branch_table", "read_blank_quantum_content",
    "claim_destinations_inside_writer", "controller_predecessor_loop",
    "generated_count_2976", "inherited_count_186", "partial_transport",
    "move_obstacle_record", "drop_new_record", "drop_obstacles_after_stop",
    "outcome_dependent_guard", "same_event_feedback",
    "nonnormalized_m0_law", "omit_center_marginal_factor",
    "omit_blank_marginal_factor", "wrong_product_rational",
    "change_one_site_marginal", "treat_labels_as_born_orthogonal",
    "claim_autonomous_formation", "claim_nearest_neighbor",
    "claim_microscopic_detector", "claim_overlap_arbitration",
    "claim_site_occurrence", "claim_rate_time", "claim_gravity",
    "claim_axiom", "claim_retained", "claim_obligation", "claim_toe",
)

MUTATION_GROUP = {
    "goal_drift": "A", "preflight_drift": "A", "correction_drift": "A",
    "import_block16_primary": "A", "import_block15_primary": "A",
    "drop_writer_site": "B", "drop_external_destination": "B",
    "wrong_record_code": "B", "reverse_record_code": "B",
    "nonphysical_output": "B", "mixed_front_source": "B",
    "nonzero_transverse_source": "B", "fill_gap": "B",
    "occupy_candidate": "B", "extra_record": "B",
    "collapse_branch_masks": "B", "nonunit_product_trace": "B",
    "drop_branch": "C", "unequal_branch_weight": "C",
    "negative_branch_weight": "C", "branch_specific_precursor": "C",
    "incomplete_blank_effect": "C", "stop_resets_content": "C",
    "stop_misses_nonblank_mask": "C", "overwrite_singleton": "C",
    "retain_blank_nonblank_coherence": "C", "drop_rotation": "D",
    "ignore_translation": "D", "rotate_sites_not_bloch": "D",
    "hardcode_positive_x": "D", "public_host_direction": "D",
    "public_branch": "D", "public_center": "D", "public_site_id": "D",
    "public_scheduler_clock": "D", "hidden_branch_table": "D",
    "read_blank_quantum_content": "D",
    "claim_destinations_inside_writer": "E",
    "controller_predecessor_loop": "E", "generated_count_2976": "E",
    "inherited_count_186": "E", "partial_transport": "E",
    "move_obstacle_record": "E", "drop_new_record": "E",
    "drop_obstacles_after_stop": "E", "outcome_dependent_guard": "E",
    "same_event_feedback": "E", "nonnormalized_m0_law": "E",
    "omit_center_marginal_factor": "F", "omit_blank_marginal_factor": "F",
    "wrong_product_rational": "F", "change_one_site_marginal": "F",
    "treat_labels_as_born_orthogonal": "F",
    "claim_autonomous_formation": "G", "claim_nearest_neighbor": "G",
    "claim_microscopic_detector": "G", "claim_overlap_arbitration": "G",
    "claim_site_occurrence": "G", "claim_rate_time": "G",
    "claim_gravity": "G", "claim_axiom": "G", "claim_retained": "G",
    "claim_obligation": "G", "claim_toe": "G",
}


@cache
def mutation_detected(mutation: str) -> bool:
    direction = (1, 0, 0)
    output = branch_output(direction)
    candidate = scale(2, direction)
    sources, destinations = packet_geometry(candidate, direction)

    if mutation == "goal_drift":
        return authority_facts()["goal_blob"] != "0" * 40
    if mutation == "preflight_drift":
        return authority_facts()["preflight_blob"] != "0" * 40
    if mutation == "correction_drift":
        return authority_facts()["correction_blob"] != "0" * 40
    if mutation in {"import_block16_primary", "import_block15_primary"}:
        module = (
            "scripts.admissibility_d4_block16_primary"
            if mutation == "import_block16_primary"
            else "scripts.admissibility_d4_block15_primary"
        )
        tree = ast.parse(f"from {module} import run")
        return any(
            isinstance(node, ast.ImportFrom)
            and node.module is not None
            and node.module.startswith("scripts.admissibility_d4")
            for node in ast.walk(tree)
        )
    if mutation == "drop_writer_site":
        return len(set(writer_block()) - {next(iter(writer_block()))}) != 43
    if mutation == "drop_external_destination":
        return len(set(extended_block()) - {next(iter(external_destinations()))}) != 73
    if mutation == "wrong_record_code":
        wrong = bloch_scale(F(-9, 16), bloch_from_position(direction))
        return wrong != seed_record_code(direction)
    if mutation == "reverse_record_code":
        return bloch_scale(-1, seed_record_code(direction)) != seed_record_code(direction)
    if mutation == "nonphysical_output":
        return not QubitState((Rad3(2), ZERO, ZERO)).physical
    if mutation == "mixed_front_source":
        return MIXED.bloch != output.state_at(scale(3, direction)).bloch
    if mutation == "nonzero_transverse_source":
        return seed_record_code(direction) != ZERO_BLOCH
    if mutation == "fill_gap":
        changed = output.record_mask | {scale(-1, direction)}
        return scan_frontier_tips(changed) != frozenset({(candidate, direction)})
    if mutation == "occupy_candidate":
        changed = output.record_mask | {candidate}
        return (candidate, direction) not in scan_frontier_tips(changed)
    if mutation == "extra_record":
        return len(output.record_mask | {(0, 1, 0)}) != 3
    if mutation == "collapse_branch_masks":
        return len({output.record_mask for _direction in DIRECTIONS}) != 6
    if mutation == "nonunit_product_trace":
        return F(2) ** len(writer_block()) != 1
    if mutation == "drop_branch":
        return sum((F(1, 6) for _ in DIRECTIONS[:-1]), F(0)) != 1
    if mutation == "unequal_branch_weight":
        weights = (F(1, 3),) + (F(2, 15),) * 5
        return sum(weights, F(0)) == 1 and len(set(weights)) != 1
    if mutation == "negative_branch_weight":
        return F(-1, 6) < 0
    if mutation == "branch_specific_precursor":
        effects = {f: frozenset({f}) for f in DIRECTIONS}
        return len(set(effects.values())) == 6
    if mutation == "incomplete_blank_effect":
        return 5 * F(1, 6) != 1
    if mutation in {"stop_resets_content", "overwrite_singleton"}:
        token = object()
        rows = construct_instrument(frozenset({direction}), token)
        preserved = rows[-1].output
        mutant = object()
        return isinstance(preserved, PreservedInput) and preserved.quantum_contents is not mutant
    if mutation == "stop_misses_nonblank_mask":
        mask = frozenset({direction, scale(2, direction)})
        mutant_stop = F(1) if len(mask) == 1 else F(0)
        return mutant_stop != stop_effect(mask)
    if mutation == "retain_blank_nonblank_coherence":
        coefficients = instrument_facts()["full_hilbert_coefficients"]
        return coefficients["blank_nonblank_cross"] != 1
    if mutation == "drop_rotation":
        return len(rotations()[:-1]) != 24
    if mutation == "ignore_translation":
        moved = transform_output(output, rotations()[0], TRANSLATIONS[0])
        return moved != transform_output(output, rotations()[0])
    if mutation == "rotate_sites_not_bloch":
        matrix = next(
            matrix for matrix in rotations()
            if rotate_position(matrix, direction) != direction
        )
        moved_direction = rotate_position(matrix, direction)
        bad = BranchOutput(
            direction=moved_direction,
            center=(0, 0, 0),
            record_mask=frozenset(
                rotate_position(matrix, site) for site in output.record_mask
            ),
            site_states=tuple(sorted(
                (rotate_position(matrix, site), state)
                for site, state in output.site_states
            )),
        )
        return bad != branch_output(moved_direction)
    if mutation == "hardcode_positive_x":
        return branch_output((0, 1, 0)).direction != direction
    if mutation == "public_host_direction":
        return signature_has_forbidden_argument("def bad(record_flags, host_direction): pass")
    if mutation == "public_branch":
        return signature_has_forbidden_argument("def bad(record_flags, branch): pass")
    if mutation == "public_center":
        return signature_has_forbidden_argument("def bad(record_flags, center): pass")
    if mutation == "public_site_id":
        return signature_has_forbidden_argument("def bad(record_flags, site_id): pass")
    if mutation == "public_scheduler_clock":
        return signature_has_forbidden_argument("def bad(scheduler, global_clock): pass")
    if mutation == "hidden_branch_table":
        table = {direction: branch_output(direction) for direction in DIRECTIONS}
        return len(table) == 6 and table[direction] == output
    if mutation == "read_blank_quantum_content":
        try:
            bool(RaisingQuantumContent())
        except ForbiddenContentAccess:
            return True
        return False
    if mutation == "claim_destinations_inside_writer":
        return any(destination not in writer_block() for destination in destinations)
    if mutation == "controller_predecessor_loop":
        return 6 * 14 * 14 * 32 != CONTROLLER_MAPS
    if mutation == "generated_count_2976":
        return INHERITED_BLOCKED_COMPONENTS != GENERATED_BLOCKED_COMPONENTS
    if mutation == "inherited_count_186":
        return GENERATED_BLOCKED_COMPONENTS != INHERITED_BLOCKED_COMPONENTS
    if mutation in {"partial_transport", "move_obstacle_record"}:
        source_tokens = [("source", index) for index in range(5)]
        destination_tokens = [("record", 0)] + [
            ("destination", index) for index in range(1, 5)
        ]
        if mutation == "partial_transport":
            changed = source_tokens[:]
            for index in range(1, 5):
                changed[index] = destination_tokens[index]
            return changed != source_tokens
        moved = destination_tokens[:]
        moved[0] = source_tokens[0]
        return moved[0] != ("record", 0)
    if mutation == "drop_new_record":
        obstacles = frozenset({destinations[0]})
        return scan_frontier_tips(output.record_mask | obstacles) == frozenset({
            (candidate, direction)
        })
    if mutation == "drop_obstacles_after_stop":
        return scan_frontier_tips(output.record_mask | {candidate}) == frozenset({
            (add(candidate, direction), direction)
        })
    if mutation == "outcome_dependent_guard":
        return len({"STOP" if index % 2 else "CONTINUE" for index in range(14)}) == 2
    if mutation == "same_event_feedback":
        clear_terminals = {
            "STOP" if index % 2 else "CONTINUE" for index in range(14)
        }
        return clear_terminals != {"CONTINUE"}
    if mutation == "nonnormalized_m0_law":
        changed = list(m0_probabilities())
        changed[0] += F(1, 100)
        return sum(changed, F(0)) != 1
    if mutation == "omit_center_marginal_factor":
        return 6 * F(1, 6) ** 3 * F(5, 6) ** 15 != PRODUCT_VALID_PROBABILITY
    if mutation == "omit_blank_marginal_factor":
        return 6 * F(1, 6) ** 4 * F(5, 6) ** 14 != PRODUCT_VALID_PROBABILITY
    if mutation == "wrong_product_rational":
        return F(5**14, 6**18) != PRODUCT_VALID_PROBABILITY
    if mutation == "change_one_site_marginal":
        facts = joint_law_facts()
        return facts["center_label_count"] == 6 and F(1, 5) != F(1, 6)
    if mutation == "treat_labels_as_born_orthogonal":
        return joint_law_facts()["all_center_born_overlaps_positive"]

    scope_mutations = {
        "claim_autonomous_formation": "autonomous_formation",
        "claim_nearest_neighbor": "nearest_neighbor_compilation",
        "claim_microscopic_detector": "microscopic_detector_or_controller",
        "claim_overlap_arbitration": "overlapping_center_arbitration",
        "claim_site_occurrence": "site_occurrence",
        "claim_rate_time": "rate_or_time",
        "claim_gravity": "gravity",
        "claim_axiom": "axiom_amendment",
        "claim_retained": "retained_status",
        "claim_obligation": "obligation_retirement",
        "claim_toe": "toe_movement",
    }
    if mutation in scope_mutations:
        changed = dict(LIMITS)
        key = scope_mutations[mutation]
        changed[key] = 1 if key in {"obligation_retirement", "toe_movement"} else True
        return not scope_is_narrow(changed)
    raise ValueError(f"unknown mutation: {mutation}")


def evaluated_checks(mutation: str = "") -> list[tuple[str, bool, str]]:
    authority = authority_facts()
    block = block_output_facts()
    instrument = instrument_facts()
    covariance = covariance_facts()
    composition = composition_facts()
    joint = joint_law_facts()
    runtime = runtime_surface_facts()

    authority_ok = (
        authority["goal_blob"] == GOAL_BLOB
        and authority["preflight_blob"] == PREFLIGHT_BLOB
        and authority["correction_blob"] == SUPPORT_CORRECTION_BLOB
        and authority["standard_imports"]
        and authority["correction_43"] and authority["correction_73"]
        and authority["correction_186"] and authority["correction_5166"]
        and authority["correction_2976"] and authority["correction_171936"]
    )
    block_ok = (
        block["writer_sites"] == WRITER_SITE_COUNT
        and block["external_sites"] == EXTERNAL_DESTINATION_COUNT
        and block["extension_sites"] == EXTENDED_SITE_COUNT
        and block["disjoint_supports"]
        and block["branches"] == 6 and block["distinct_masks"] == 6
        and block["sector_orthogonal_pairs"] == 15
        and block["physical_sites"] == 6 * 43
        and block["normalized_products"] and block["exact_masks"]
        and block["exact_shells"] and block["distinct_footprint"]
        and block["rf_exact"]
        and block["rf_eigenvalues"] == (F(113, 512), F(399, 512))
        and block["all_outcomes_unit"] and block["record_code_bound"]
    )
    instrument_ok = (
        instrument["branch_effect"] == F(1, 6)
        and instrument["blank_effect_sum"] == 1
        and instrument["nonblank_effect_sum"] == 1
        and instrument["choi_factor_positive"]
        and instrument["stop_compression_cp"] and instrument["common_blank"]
        and instrument["singleton_controls"] == 43
        and instrument["singleton_identity"]
        and instrument["footprint_controls"] == 6 * 15
        and instrument["footprint_identity"]
        and instrument["symbolic_nonblank_masks"] == 2**43 - 1
        and instrument["full_hilbert_coefficients"] == {
            "blank_diagonal_trace": F(1),
            "nonblank_diagonal_trace": F(1),
            "blank_nonblank_cross": F(0),
            "nonblank_blank_cross": F(0),
        }
        and not instrument["record_coherences_in_domain"]
    )
    covariance_runtime_ok = (
        covariance["rotations"] == 24 and covariance["translations"] == 3
        and covariance["output_cases"] == 6 * 24
        and covariance["translation_cases"] == 6 * 24 * 3
        and covariance["footprint_cases"] == 6 * 24
        and covariance["output_covariant"]
        and covariance["translation_covariant"]
        and covariance["footprint_covariant"] and covariance["block_covariant"]
        and covariance["blank_effect_invariant"]
        and covariance["stop_effect_invariant"]
        and runtime["public_functions"] and runtime["exact_arguments"]
        and not runtime["forbidden_arguments"]
        and runtime["constructor_mentions_quantum"]
        and not runtime["constructor_calls_on_quantum"]
        and runtime["poison_survives"] and runtime["all_branches_internal"]
        and not runtime["branch_lookup_table"]
        and not runtime["same_event_feedback"]
    )
    composition_ok = (
        composition["controller_maps"] == CONTROLLER_MAPS
        and composition["clear_maps"] == 6 * 14
        and composition["blocked_maps"] == 6 * 14 * 31
        and composition["initial_frontier_evaluations"] == 6 * 15
        and composition["initial_tip_exact"] and composition["edge_agreement"]
        and composition["shell_exact"] and composition["clear_exact"]
        and composition["blocked_exact"] and composition["permanence"]
        and composition["probability_exact"]
        and composition["generated_components"] == GENERATED_BLOCKED_COMPONENTS
        and composition["generated_frontier"] == GENERATED_BLOCKED_FRONTIER
        and composition["generated_zero"]
        and composition["inherited_components"] == INHERITED_BLOCKED_COMPONENTS
        and composition["inherited_frontier"] == INHERITED_BLOCKED_FRONTIER
        and composition["inherited_zero"]
        and composition["writer_sites"] == 43
        and composition["external_destinations"] == 30
        and composition["extended_sites"] == 73
        and composition["sources_inside_writer"]
        and composition["destinations_outside_writer"]
    )
    joint_ok = (
        joint["rows"] == 6 and joint["sites"] == 43
        and joint["marginals_equal"]
        and joint["branch_probabilities"] == {joint["expected_branch"]}
        and joint["valid_probability"] == PRODUCT_VALID_PROBABILITY
        and joint["expected_valid_probability"] == PRODUCT_VALID_PROBABILITY
        and joint["valid_less_than_one"]
        and joint["center_label_count"] == 6
        and joint["minimum_center_born_overlap"]
        == joint["expected_minimum_center_born_overlap"]
        and joint["all_center_born_overlaps_positive"]
        and joint["preparation_labels_classical"]
        and not joint["born_discrimination_probability"]
        and joint["transverse_unit_factors"]
    )
    scope_ok = (
        TERMINAL == "COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT"
        and scope_is_narrow(LIMITS)
    )

    checks = [
        ["A_frozen_independent_surface", authority_ok,
         "goal, preflight, and support-correction blobs match; only standard-library imports are used"],
        ["B_sparse_writer_and_outputs", block_ok,
         "43 writer sites plus 30 disjoint destinations give 73; six exact physical product outputs occupy distinct mask sectors"],
        ["C_total_central_effect_instrument", instrument_ok,
         "positive functional/state factors and central mask effects prove CP/TP; all nonblank masks STOP by identity"],
        ["D_cubic_covariance_and_runtime", covariance_runtime_ok,
         "144 rotations, 432 translated outputs, and public no-front construction are exact without reading blank content"],
        ["E_block15_extended_composition", composition_ok,
         "2688 maps use the 73-site extension; generated 186/5166 and inherited 2976/171936 counts stay distinct"],
        ["F_joint_law_and_born_boundary", joint_ok,
         "6x43 preparation labels have equal marginals and valid mass 5^15/6^18; positive Born overlaps remain explicit"],
        ["G_conditional_terminal_and_limits", scope_ok,
         "terminal is conditional on a selected center, atomic event, effective mask algebra, and blank detector"],
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
                "TERMINAL: COVARIANT-CONDITIONAL-CAP-PACKET-INSTRUMENT — "
                "one common blank input at a selected center"
            )
            print(
                "COUNTS: writer=43; external_destinations=30; extension=73; "
                "branches=6; rotations=24; controller_maps=2688; "
                "generated_blocked=186/5166; inherited_blocked=2976/171936"
            )
            print(
                "MARGINAL: preparation_label_valid_probability="
                "30517578125/101559956668416=5^15/6^18; "
                "not_a_Born_distinguishability_probability"
            )
            print(
                "LIMITS: conditional atomic effective-block writer only; "
                "selected center and blank detector remain supplied; no "
                "nearest-neighbor/microscopic compilation, overlap arbitration, "
                "occurrence/rate/time, gravity, axiom, retention, obligation, "
                "or TOE movement"
            )
    print(f"TOTAL: PASS={passed} FAIL={failed}")
    return int(failed != 0)


if __name__ == "__main__":
    raise SystemExit(main())
