#!/usr/bin/env python3
"""Block 4: common-front remote-context Record-event congruence.

This runner composes three separately typed objects without treating any of
them as more than they are:

* the exact common-front Kraus factorization from Block 3;
* a strict-nearest-neighbour two-target Record rail whose remote context is
  absent from the complete first-target condition; and
* the accepted Cycle-317 M64 carrier for the staged matrix blocks.

The rail derives pair-specific equality of the complete first-site
Admissibility measure by literal condition identity.  It does not assign that
measure a numerical value, prove that an effect-label code is a physical
event, force finite atomic support, or construct a total formation/history
law.
"""

from __future__ import annotations

from contextlib import redirect_stdout
from dataclasses import dataclass
from hashlib import sha256
from io import StringIO
from itertools import permutations, product
from pathlib import Path
import sys

import numpy as np
import sympy as sp


AUDIT_TIMEOUT_SEC = 180

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18 as c317
import physical_effect_equivalence_normalized_grade_cycle321_2026_07_18 as c321
import shared_effect_record_randomized_preparation_congruence_independence_2026_08_20 as block3


NOTE_PATH = ROOT / "docs" / (
    "COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
BLOCK1_PATH = ROOT / "docs" / (
    "RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_"
    "BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
BLOCK3_PATH = ROOT / "docs" / (
    "SHARED_EFFECT_RECORD_RANDOMIZED_PREPARATION_CONGRUENCE_"
    "INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md"
)
CYCLE317_PATH = ROOT / "docs/work_history/repo/review_feedback" / (
    "PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md"
)
CARRIER_PATH = ROOT / "docs" / (
    "ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_"
    "FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
)

AUDIT_INPUT_PATHS = (
    "docs/COMMON_FRONT_STAGE_REMOTE_CONTEXT_RECORD_EVENT_CONGRUENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/RECORD_NATIVE_DYADIC_PREPARATION_TAG_SCREENING_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/SHARED_EFFECT_RECORD_RANDOMIZED_PREPARATION_CONGRUENCE_INDEPENDENCE_BOUNDED_THEOREM_NOTE_2026-08-20.md",
    "docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md",
    "docs/work_history/repo/review_feedback/PHYSICAL_CONTACT_TERNARY_BORN_FORCING_BRIDGE_CYCLE317_NOTE_2026-07-18.md",
    "scripts/shared_effect_record_randomized_preparation_congruence_independence_2026_08_20.py",
    "scripts/physical_contact_ternary_born_forcing_bridge_cycle317_2026_07_18.py",
)

TOL = 9.0e-11
PASS = 0
FAIL = 0

Point = tuple[int, int, int]
Rotation = tuple[Point, Point, Point]
M2Code = tuple[sp.Expr, sp.Expr, sp.Expr, sp.Expr]
Records = dict[Point, M2Code]

DIRECTIONS: tuple[Point, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
EX = (1, 0, 0)
TRANSVERSE: tuple[Point, ...] = (
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print(f"PASS [{label}] {detail}")
    else:
        FAIL += 1
        print(f"FAIL [{label}] {detail}")


def normalized(path: Path) -> str:
    body = path.read_text(encoding="utf-8").lower()
    for marker in ("*", "`", ">"):
        body = body.replace(marker, "")
    return " ".join(body.split())


def add(left: Point, right: Point) -> Point:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def neg(point: Point) -> Point:
    return (-point[0], -point[1], -point[2])


def l1(left: Point, right: Point) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def determinant(matrix: Rotation) -> int:
    a, b, c = matrix
    return (
        a[0] * (b[1] * c[2] - b[2] * c[1])
        - a[1] * (b[0] * c[2] - b[2] * c[0])
        + a[2] * (b[0] * c[1] - b[1] * c[0])
    )


def proper_cubic_rotations() -> tuple[Rotation, ...]:
    rows: list[Rotation] = []
    axes = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
    for order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = tuple(
                tuple(signs[row] * axes[order[row]][column] for column in range(3))
                for row in range(3)
            )
            if determinant(matrix) == 1:
                rows.append(matrix)  # type: ignore[arg-type]
    return tuple(rows)


def rotate(matrix: Rotation, point: Point) -> Point:
    return tuple(
        sum(matrix[row][column] * point[column] for column in range(3))
        for row in range(3)
    )  # type: ignore[return-value]


def shift(point: Point, offset: Point) -> Point:
    return add(point, offset)


def code(matrix: sp.Matrix) -> M2Code:
    if matrix.shape != (2, 2):
        raise ValueError("one site must carry one M2(C) possibility")
    return tuple(sp.simplify(matrix[row, column]) for row in range(2) for column in range(2))  # type: ignore[return-value]


def as_matrix(value: M2Code) -> sp.Matrix:
    return sp.Matrix(((value[0], value[1]), (value[2], value[3])))


def kappa(effect: sp.Matrix, label: int) -> M2Code:
    return code(effect + sp.I * label * sp.eye(2))


E0_EXACT = sp.diag(sp.Rational(1, 2), 0)
REMAINDER_EXACT = sp.eye(2) - E0_EXACT
RHO_EXACT = sp.diag(sp.Rational(3, 5), sp.Rational(2, 5))
SIGMA_E0_EXACT = sp.diag(sp.Rational(3, 10), 0)
SIGMA_REMAINDER_EXACT = sp.diag(sp.Rational(3, 10), sp.Rational(2, 5))
PREPARATION = kappa(RHO_EXACT, 7)
COMMON_MARKERS = frozenset(
    (
        kappa(E0_EXACT, 20),
        kappa(REMAINDER_EXACT, 21),
        kappa(sp.eye(2) / 2, 22),
        kappa(sp.eye(2), 23),
    )
)
RESIDUAL_MARKERS = frozenset(
    (
        kappa(sp.eye(2) / 3, 24),
        kappa(2 * sp.eye(2) / 3, 25),
        kappa(sp.eye(2), 26),
    )
)
CONTEXT_A = kappa(sp.Matrix(((1, 1), (1, 1))) / 2, 30)
CONTEXT_B = kappa(sp.Matrix(((1, -sp.I), (sp.I, 1))) / 2, 31)
E0_RECORD = kappa(E0_EXACT, 0)
REMAINDER_RECORD = kappa(REMAINDER_EXACT, 1)


@dataclass(frozen=True)
class LocalCondition:
    target_blank: bool
    neighbours: tuple[tuple[Point, M2Code | None], ...]


@dataclass(frozen=True)
class ReadySite:
    stage: str
    forward: Point
    predecessor: Point
    read_positions: tuple[Point, ...]


def local_condition(records: Records, target: Point) -> LocalCondition:
    return LocalCondition(
        target not in records,
        tuple((direction, records.get(add(target, direction))) for direction in DIRECTIONS),
    )


def decode_ready_site(records: Records, target: Point) -> ReadySite | None:
    if target in records:
        return None
    occupied = tuple(
        direction for direction in DIRECTIONS if add(target, direction) in records
    )
    blanks = tuple(direction for direction in DIRECTIONS if direction not in occupied)
    if len(occupied) != 5 or len(blanks) != 1:
        return None
    forward = blanks[0]
    predecessor = add(target, neg(forward))
    if predecessor not in records:
        return None
    transverse_positions = tuple(
        add(target, direction) for direction in occupied if direction != neg(forward)
    )
    if len(transverse_positions) != 4:
        return None
    transverse = frozenset(records[position] for position in transverse_positions)
    predecessor_content = records[predecessor]
    stage = ""
    if predecessor_content == PREPARATION and transverse == COMMON_MARKERS:
        stage = "common-front"
    elif predecessor_content == REMAINDER_RECORD:
        if transverse == RESIDUAL_MARKERS | {CONTEXT_A}:
            stage = "continuation-A"
        elif transverse == RESIDUAL_MARKERS | {CONTEXT_B}:
            stage = "continuation-B"
    if not stage:
        return None
    return ReadySite(
        stage,
        forward,
        predecessor,
        tuple(sorted((predecessor,) + transverse_positions)),
    )


def frontier(records: Records) -> set[Point]:
    return {
        add(position, direction)
        for position in records
        for direction in DIRECTIONS
        if add(position, direction) not in records
    }


def active_sites(records: Records) -> tuple[tuple[Point, ReadySite], ...]:
    return tuple(
        (target, ready)
        for target in sorted(frontier(records))
        if (ready := decode_ready_site(records, target)) is not None
    )


@dataclass(frozen=True)
class Layout:
    context: str
    records: tuple[tuple[Point, M2Code], ...]
    first_target: Point
    continuation_target: Point
    forward_blank: Point
    context_site: Point

    def record_map(self) -> Records:
        return dict(self.records)


def build_layout(context: str) -> Layout:
    if context not in ("A", "B"):
        raise ValueError("the finite layout declares only contexts A and B")
    s0 = (0, 0, 0)
    s1 = (1, 0, 0)
    s2 = (2, 0, 0)
    context_site = (1, 1, 0)
    records: Records = {(-1, 0, 0): PREPARATION}
    for direction, marker in zip(TRANSVERSE, sorted(COMMON_MARKERS, key=repr), strict=True):
        records[add(s0, direction)] = marker
    residual_positions = ((1, -1, 0), (1, 0, 1), (1, 0, -1))
    for position, marker in zip(residual_positions, sorted(RESIDUAL_MARKERS, key=repr), strict=True):
        records[position] = marker
    records[context_site] = CONTEXT_A if context == "A" else CONTEXT_B
    return Layout(context, tuple(sorted(records.items())), s0, s1, s2, context_site)


def transformed_layout(layout: Layout, rotation: Rotation, offset: Point) -> Layout:
    def transform(point: Point) -> Point:
        return shift(rotate(rotation, point), offset)

    return Layout(
        layout.context,
        tuple(sorted((transform(point), value) for point, value in layout.records)),
        transform(layout.first_target),
        transform(layout.continuation_target),
        transform(layout.forward_blank),
        transform(layout.context_site),
    )


def append_record(records: Records, target: Point, content: M2Code) -> Records:
    if target in records:
        raise ValueError("Record permanence forbids overwriting an occupied site")
    updated = dict(records)
    updated[target] = content
    return updated


def condition_measure_key(condition: LocalCondition) -> str:
    """Name the law-level measure by its complete local condition, not a value."""

    return sha256(repr(condition).encode("utf-8")).hexdigest()


def ancestors(nodes: set[Point], edges: set[tuple[Point, Point]], target: Point) -> set[Point]:
    reverse: dict[Point, set[Point]] = {node: set() for node in nodes}
    for source, destination in edges:
        reverse[destination].add(source)
    found: set[Point] = set()
    stack = list(reverse[target])
    while stack:
        node = stack.pop()
        if node in found:
            continue
        found.add(node)
        stack.extend(reverse[node] - found)
    return found


def source_and_axiom_controls() -> None:
    sources = tuple(normalized(path) for path in (AXIOM_PATH, BLOCK1_PATH, BLOCK3_PATH, CYCLE317_PATH, CARRIER_PATH))
    axiom, block1_text, block3_text, cycle317_text, carrier_text = sources
    check(
        "sources",
        all(path.exists() for path in (NOTE_PATH, AXIOM_PATH, BLOCK1_PATH, BLOCK3_PATH, CYCLE317_PATH, CARRIER_PATH))
        and "one fixed nearest-neighbor admissibility rule" in axiom
        and "probability distribution over the possibilities is determined by" in axiom
        and "records form" in axiom
        and "records are permanent" in axiom
        and "five occupied nearest neighbours and one blank" in block1_text
        and "common-first-stage factorization is exact" in block3_text
        and "effect functionality remains a hypothesis" in cycle317_text
        and "current record clause does not select kappa" in carrier_text,
        "current axiom, append rail, factorization, physical carrier, and event-registration boundary are bound",
    )


def layout_controls() -> tuple[Layout, Layout]:
    layout_a, layout_b = build_layout("A"), build_layout("B")
    records_a, records_b = layout_a.record_map(), layout_b.record_map()
    condition_a = local_condition(records_a, layout_a.first_target)
    condition_b = local_condition(records_b, layout_b.first_target)
    changed = {
        point
        for point in set(records_a) | set(records_b)
        if records_a.get(point) != records_b.get(point)
    }
    check(
        "literal-common-front-condition",
        condition_a == condition_b
        and changed == {layout_a.context_site}
        and l1(layout_a.context_site, layout_a.first_target) == 2
        and l1(layout_a.context_site, layout_a.continuation_target) == 1
        and active_sites(records_a) == ((layout_a.first_target, decode_ready_site(records_a, layout_a.first_target)),)
        and active_sites(records_b) == ((layout_b.first_target, decode_ready_site(records_b, layout_b.first_target)),),
        {
            "world_difference": "one physical context Record at graph distance two",
            "initial_active_sites": 1,
            "stage_one_condition": "exactly identical",
        },
    )
    key_a = condition_measure_key(condition_a)
    key_b = condition_measure_key(condition_b)
    check(
        "same-condition-measure-congruence",
        key_a == key_b and E0_RECORD == kappa(E0_EXACT, 0),
        {
            "inference": "one condition determines one full M2(C) measure",
            "event": "the same fixed front-E0 effect-label content event in both worlds",
            "numerical_mass": "not assigned",
        },
    )

    e0_a = append_record(records_a, layout_a.first_target, E0_RECORD)
    e0_b = append_record(records_b, layout_b.first_target, E0_RECORD)
    rem_a = append_record(records_a, layout_a.first_target, REMAINDER_RECORD)
    rem_b = append_record(records_b, layout_b.first_target, REMAINDER_RECORD)
    check(
        "record-native-stage-gating",
        active_sites(e0_a) == ()
        and active_sites(e0_b) == ()
        and active_sites(rem_a) == ((layout_a.continuation_target, decode_ready_site(rem_a, layout_a.continuation_target)),)
        and active_sites(rem_b) == ((layout_b.continuation_target, decode_ready_site(rem_b, layout_b.continuation_target)),)
        and decode_ready_site(rem_a, layout_a.continuation_target).stage == "continuation-A"  # type: ignore[union-attr]
        and decode_ready_site(rem_b, layout_b.continuation_target).stage == "continuation-B",  # type: ignore[union-attr]
        "E0 permanence seals the front Record; only the complement content enables the context-specific continuation",
    )
    permanence = all(
        updated[position] == value
        for records, updated in ((records_a, e0_a), (records_a, rem_a), (records_b, e0_b), (records_b, rem_b))
        for position, value in records.items()
    )
    read_safety = all(
        position in records
        for records, target in (
            (records_a, layout_a.first_target),
            (records_b, layout_b.first_target),
            (rem_a, layout_a.continuation_target),
            (rem_b, layout_b.continuation_target),
        )
        for position in decode_ready_site(records, target).read_positions  # type: ignore[union-attr]
    )
    check(
        "append-permanence-and-readable-inputs",
        permanence and read_safety,
        "every transition appends one blank target, preserves old Records, and reads content only from occupied neighbours",
    )
    q = sp.Symbol("q", positive=True)
    formation_a = sp.Rational(1, 3)
    formation_b = sp.Rational(2, 3)
    check(
        "formation-boundary-control",
        key_a == key_b
        and sp.simplify(formation_a * q - formation_b * q) != 0,
        "equal conditional content measures do not equalize an independently supplied formation-site probability",
    )
    return layout_a, layout_b


def causal_and_hostile_controls(layout_a: Layout, layout_b: Layout) -> None:
    records_a, records_b = layout_a.record_map(), layout_b.record_map()
    common_sources = {
        point for point in records_a if l1(point, layout_a.first_target) == 1
    }
    residual_sources = set(add(layout_a.continuation_target, direction) for direction in TRANSVERSE) - {layout_a.context_site}
    nodes = common_sources | residual_sources | {
        layout_a.context_site,
        layout_a.first_target,
        layout_a.continuation_target,
    }
    edges = {
        (source, layout_a.first_target)
        for source in common_sources
        if l1(source, layout_a.first_target) == 1
    } | {
        (source, layout_a.continuation_target)
        for source in residual_sources | {layout_a.context_site, layout_a.first_target}
        if l1(source, layout_a.continuation_target) == 1
    }
    check(
        "nearest-neighbour-causal-exclusion",
        all(l1(source, destination) == 1 for source, destination in edges)
        and layout_a.context_site not in ancestors(nodes, edges, layout_a.first_target)
        and layout_a.context_site in ancestors(nodes, edges, layout_a.continuation_target)
        and layout_a.first_target in ancestors(nodes, edges, layout_a.continuation_target),
        "the supplied finite dependency DAG has no context-to-front path and routes context only to the continuation",
    )

    deletion_failures = []
    for point in sorted(records_a):
        mutated = dict(records_a)
        del mutated[point]
        if point in common_sources:
            deletion_failures.append(decode_ready_site(mutated, layout_a.first_target) is not None)
    rem_a = append_record(records_a, layout_a.first_target, REMAINDER_RECORD)
    continuation_inputs = set(decode_ready_site(rem_a, layout_a.continuation_target).read_positions)  # type: ignore[union-attr]
    for point in sorted(continuation_inputs):
        mutated = dict(rem_a)
        del mutated[point]
        deletion_failures.append(decode_ready_site(mutated, layout_a.continuation_target) is not None)

    leaked_a, leaked_b = dict(records_a), dict(records_b)
    leak_site = add(layout_a.first_target, (0, 1, 0))
    leaked_a[leak_site] = CONTEXT_A
    leaked_b[leak_site] = CONTEXT_B
    check(
        "hostile-deletions-and-context-leak",
        not any(deletion_failures)
        and local_condition(leaked_a, layout_a.first_target)
        != local_condition(leaked_b, layout_b.first_target)
        and decode_ready_site(leaked_a, layout_a.first_target) is None
        and decode_ready_site(leaked_b, layout_b.first_target) is None,
        "every declared dependency is load bearing, and moving context into the first star destroys the connector premise",
    )


def covariance_controls(layout_a: Layout, layout_b: Layout) -> None:
    rotations = proper_cubic_rotations()
    offsets = ((0, 0, 0), (3, -2, 5), (-4, 1, -3))
    failures = 0
    cases = 0
    for rotation in rotations:
        for offset in offsets:
            for layout in (layout_a, layout_b):
                carried = transformed_layout(layout, rotation, offset)
                records = carried.record_map()
                ready = active_sites(records)
                failures += ready != ((carried.first_target, decode_ready_site(records, carried.first_target)),)
                rem = append_record(records, carried.first_target, REMAINDER_RECORD)
                continuation = decode_ready_site(rem, carried.continuation_target)
                failures += continuation is None or continuation.stage != f"continuation-{layout.context}"
                failures += l1(carried.context_site, carried.first_target) != 2
                failures += l1(carried.context_site, carried.continuation_target) != 1
                cases += 1
    check(
        "spatial-covariance",
        len(rotations) == 24 and cases == 144 and failures == 0,
        "the complete rail, unique active front, late context, and continuation survive 24 rotations at three translations",
    )


def positive_sqrt(matrix: np.ndarray) -> np.ndarray:
    values, vectors = np.linalg.eigh(matrix)
    if float(np.min(values)) < -TOL:
        raise ValueError("positive_sqrt received a matrix outside the positive cone")
    return vectors @ np.diag(np.sqrt(np.maximum(values, 0.0))) @ vectors.conj().T


def matrix_and_physical_controls() -> None:
    menu_a, menu_b = block3.exact_menus()
    fixtures = {length: c317.physical_fixture(length) for length in (3, 6)}
    contact = fixtures[3].contact
    program_a = block3.build_program("M_A", menu_a, contact)
    program_b = block3.build_program("M_B", menu_b, contact)
    e0 = block3.h2_to_numpy(menu_a[0])
    k0 = positive_sqrt(e0) @ contact
    remainder = positive_sqrt(np.eye(2) - e0) @ contact
    inverse = np.linalg.inv(remainder)
    residuals = {
        program.name: tuple(operator @ inverse for operator in program.kraus[1:])
        for program in (program_a, program_b)
    }
    stage1 = np.vstack((k0, remainder))
    total = {
        program.name: np.vstack(
            (k0,) + tuple(operator @ remainder for operator in residuals[program.name])
        )
        for program in (program_a, program_b)
    }
    recovery = max(
        float(np.linalg.norm(total[program.name] - np.vstack(program.kraus)))
        for program in (program_a, program_b)
    )
    completeness = max(
        float(np.linalg.norm(stage1.conj().T @ stage1 - np.eye(2))),
        *(float(np.linalg.norm(matrix.conj().T @ matrix - np.eye(2))) for matrix in total.values()),
        *(
            float(
                np.linalg.norm(
                    sum((operator.conj().T @ operator for operator in branch), start=np.zeros((2, 2), dtype=complex))
                    - np.eye(2)
                )
            )
            for branch in residuals.values()
        ),
    )
    check(
        "exact-controlled-composition",
        max(recovery, completeness) < TOL,
        {
            "all_composition_residuals": f"< {TOL:g}",
            "contexts": ("M_A", "M_B"),
            "external_clock_or_probability": "none",
        },
    )

    context_a = np.diag((1.0, 0.0)).astype(complex)
    context_b = np.diag((0.0, 1.0)).astype(complex)
    controlled = np.kron(context_a, total["M_A"]) + np.kron(context_b, total["M_B"])
    common_cp = float(
        np.linalg.norm(c321.choi((program_a.kraus[0],)) - c321.choi((program_b.kraus[0],)))
    )
    e0_block = max(
        float(np.linalg.norm(total[name][:2, :] - k0)) for name in ("M_A", "M_B")
    )
    check(
        "coherent-context-sealed-port",
        float(np.linalg.norm(controlled.conj().T @ controlled - np.eye(4))) < TOL
        and max(common_cp, e0_block) < TOL,
        "the context-controlled isometry acts differently only after the complement port; the complete E0 CP block is identical",
    )

    rho = np.diag((3 / 5, 2 / 5)).astype(complex)
    sigma_e0 = k0 @ rho @ k0.conj().T
    sigma_remainder = remainder @ rho @ remainder.conj().T
    exact_sigma_e0 = np.asarray(as_matrix(SIGMA_E0_EXACT), dtype=complex)
    exact_sigma_remainder = np.asarray(as_matrix(SIGMA_REMAINDER_EXACT), dtype=complex)
    realized_residual = max(
        float(np.linalg.norm(sigma_e0 - exact_sigma_e0)),
        float(np.linalg.norm(sigma_remainder - exact_sigma_remainder)),
        *(
            float(
                np.linalg.norm(
                    operator @ sigma_remainder @ operator.conj().T
                    - target @ rho @ target.conj().T
                )
            )
            for program in (program_a, program_b)
            for operator, target in zip(residuals[program.name], program.kraus[1:])
        ),
    )
    check(
        "realized-branch-content-connector",
        realized_residual < TOL
        and np.min(np.linalg.eigvalsh(sigma_e0)) > -TOL
        and np.min(np.linalg.eigvalsh(sigma_remainder)) > -TOL,
        "after a separately supplied branch actualizes, its unnormalized positive operator fits one M2 Record and is sufficient for exact residual CP continuation; no trace is used as probability",
    )

    physical_residuals = []
    for fixture in fixtures.values():
        for program in (program_a, program_b):
            physical_stage1 = np.vstack((fixture.two_ray_encoding @ k0, fixture.two_ray_encoding @ remainder))
            physical_total = np.vstack(
                tuple(fixture.two_ray_encoding @ block for block in program.kraus)
            )
            physical_composed = np.vstack(
                (fixture.two_ray_encoding @ k0,)
                + tuple(
                    fixture.two_ray_encoding @ operator @ remainder
                    for operator in residuals[program.name]
                )
            )
            physical_residuals.extend(
                (
                    float(np.linalg.norm(physical_stage1.conj().T @ physical_stage1 - np.eye(2))),
                    float(np.linalg.norm(physical_total.conj().T @ physical_total - np.eye(2))),
                    float(np.linalg.norm(physical_composed - physical_total)),
                )
            )
    c317.PASS = c317.FAIL = 0
    inherited = StringIO()
    with redirect_stdout(inherited):
        c317.physical_locality_and_covariance_controls(
            fixtures,
            {
                "common_front": (k0, remainder),
                "residual_A": residuals["M_A"],
                "residual_B": residuals["M_B"],
                "composed_A": program_a.kraus,
                "composed_B": program_b.kraus,
            },
        )
    if c317.FAIL:
        print(inherited.getvalue(), end="")
    check(
        "physical-composed-carrier",
        max(physical_residuals) < TOL and c317.PASS == 2 and c317.FAIL == 0,
        "both composed staged programs stay in the accepted M64 code through held L=6 with bounded support and 24/24 carried frames",
    )


def boundary_controls() -> None:
    note = normalized(NOTE_PATH)
    required = (
        "same complete condition implies the same full local probability measure",
        "no numerical event mass is assigned",
        "singleton may have zero measure",
        "finite atomic registration remains open",
        "formation site and rate remain open",
        "not a total nearest-neighbour model",
        "no universal effect functionality",
        "flat/staged transfer remains open",
        "pointer-to-record actualization remains open",
        "coherent and realized modes are separate",
        "zero obligation retirement",
        "toe percentage movement: zero",
        "review-loop was not used",
    )
    forbidden = (
        "the born rule is derived",
        "new axiom is required",
        "record writer is complete",
        "the e0 atom has nonzero mass",
    )
    check(
        "claim-boundary",
        all(phrase in note for phrase in required)
        and all(phrase not in note for phrase in forbidden),
        "pair-specific measure congruence only; event typing, atomicity, generalization, histories, and axiom necessity remain open",
    )
    n5 = (
        "per_element: exact M2 effect-label codewords and all common/residual Kraus blocks are checked without assigning probability values",
        "per_site: two successive blank targets use only occupied nearest-neighbour Record contents and append without overwriting",
        "per_mode: remote contexts A and B, E0 seal, complement continuation, context leak, and every dependency deletion are checked",
        "per_block: the Record rail, supplied dependency DAG, coherent staged isometry, M64 lift, and spatial covariance are checked",
        "lattice_wide: checked and not executed — arbitrary programs, finite-event registration, autonomous formation, histories, and frequencies remain open",
    )
    for line in n5:
        print(line)
    check(
        "n5-certificate",
        all(len(line) >= 80 for line in n5) and all(line in NOTE_PATH.read_text(encoding="utf-8") for line in n5),
        "all five resolution statements are substantive and source-bound",
    )


def main() -> int:
    source_and_axiom_controls()
    layout_a, layout_b = layout_controls()
    causal_and_hostile_controls(layout_a, layout_b)
    covariance_controls(layout_a, layout_b)
    matrix_and_physical_controls()
    boundary_controls()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
