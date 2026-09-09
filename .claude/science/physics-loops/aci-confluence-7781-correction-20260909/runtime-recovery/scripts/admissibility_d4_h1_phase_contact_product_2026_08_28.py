#!/usr/bin/env python3
"""Block 228 fail-fast phase/contact finite-product compiler.

The primary stage is deliberately a reduced-word compiler.  It generates all
exact local contact-mask variants before exploring the 230 preregistered
zero/one/two-contact words.  Labelled darts, the 128-ray carrier, CP, and
fairness remain gated until this reduced table and a length-independent rank
survive.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import dataclass, replace
import hashlib
import itertools
import json
from pathlib import Path
import signal
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block228-phase-contact-product-20260828"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/PANEL_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/STATE.yaml",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/RESULT_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block228-phase-contact-product-20260828/POST_RESULT_PANEL_ADJUDICATION.md",
    "docs/ADMISSIBILITY_D4_H1_PHASE_CONTACT_PRODUCT_MULTI_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_PHASE_CONTACT_PRODUCT_MULTI_CERTIFICATE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
AUDIT_TIMEOUT_SEC = 240
MAX_STATES_PER_GRAPH = 200_000


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block-228 product compiler exceeded its timeout")


@dataclass(frozen=True, order=True)
class State:
    word: tuple[str, ...]
    foreign: frozenset[int] = frozenset()

    def __post_init__(self) -> None:
        if any(index < 0 or index >= len(self.word) for index in self.foreign):
            raise ValueError("foreign index outside word")
        if any(self.word[index] != "T" for index in self.foreign):
            raise ValueError("foreign participant must terminate on ordinary T")

    def text(self) -> str:
        return "-".join(
            f"{symbol}_F" if index in self.foreign else symbol
            for index, symbol in enumerate(self.word)
        )


@dataclass(frozen=True)
class Template:
    name: str
    lhs: tuple[str, ...]
    rhs: tuple[str, ...]
    mode: str
    required_contact: int | None = None
    terminal: str | None = None

    @property
    def width(self) -> int:
        return len(self.lhs)

    @property
    def t_positions(self) -> tuple[int, ...]:
        return tuple(i for i, symbol in enumerate(self.lhs) if symbol == "T")

    @property
    def readonly_t_positions(self) -> tuple[int, ...]:
        return tuple(
            i
            for i in self.t_positions
            if self.rhs[i] == "T"
        )

    @property
    def boundary(self) -> str:
        if "R" in self.lhs:
            return "root"
        if "A" in self.lhs:
            return "seam"
        return "interior"


@dataclass(frozen=True, order=True)
class CompiledRow:
    source: tuple[str, ...]
    contact_mask: frozenset[int]
    name: str
    target: tuple[str, ...]
    consumes: frozenset[int]
    boundary: str
    terminal: str | None

    @property
    def support(self) -> int:
        return len(self.source)


def chars(text: str) -> tuple[str, ...]:
    return tuple(text)


# Controller primitives.  Q is split only to make its complete root cylinder
# explicit; it remains one controller class in the compiler census.
CONTROLLERS = (
    Template("D_T", chars("PHTT"), chars("HTTT"), "controller"),
    Template("D_A", chars("PHTA"), chars("HTTA"), "controller"),
    Template("Q_T", chars("RHTT"), chars("RHLT"), "controller"),
    Template("Q_A", chars("RHTA"), chars("RHLA"), "controller"),
    Template("G_T", chars("HLTT"), chars("PHLT"), "controller"),
    Template("G_A", chars("HLTA"), chars("PHLA"), "controller"),
    Template("M", chars("TTL"), chars("TLT"), "controller"),
    Template("K1", chars("HLTL"), chars("PHTL"), "controller"),
    Template("K0", chars("HLLT"), chars("PHTL"), "controller"),
    Template("B", chars("HTLT"), chars("PHTL"), "controller"),
    Template("A", chars("HTLA"), chars("PPPS"), "controller", terminal="ABORT"),
)


# These are generated product targets, frozen before the first word executes.
# Each consumes every exact participant displayed in its complete source mask;
# unrelated off-support participants remain in the state.
PRODUCTS = (
    Template("QF_T", chars("RHTT"), chars("RHTL"), "product", 2),
    Template("QF_A", chars("RHTA"), chars("RPPS"), "product", 2, "ABORT"),
    Template("DF_T", chars("PHTT"), chars("PHTL"), "product", 2),
    Template("DF_A", chars("PHTA"), chars("PPPS"), "product", 2, "ABORT"),
    Template("GF_T", chars("HLTT"), chars("PHTL"), "product", 2),
    Template("GF_A", chars("HLTA"), chars("PPPS"), "product", 2, "ABORT"),
    Template("C0_T", chars("HTTT"), chars("PHTL"), "product", 2),
    Template("C0_A", chars("HTTA"), chars("PPPS"), "product", 2, "ABORT"),
    Template("CF_T", chars("TTTT"), chars("TTLT"), "product", 2),
    Template("CF_A", chars("TTTA"), chars("TTLA"), "product", 2),
    Template("M_F", chars("TTL"), chars("TLT"), "product", 1),
    Template("K1_F", chars("HLTL"), chars("PHTL"), "product", 2),
    Template("K0_F", chars("HLLT"), chars("PHTL"), "product", 3),
    Template("B_F1", chars("HTLT"), chars("PHTL"), "product", 1),
    Template("B_F3", chars("HTLT"), chars("PHTL"), "product", 3),
    Template("A_F", chars("HTLA"), chars("PPPS"), "product", 1, "ABORT"),
    # Existing abort incidence makes an adjacent contact idempotent.  The word
    # is unchanged but the exact participant is quenched, so this is not an
    # identity transition.
    Template("E_TL", chars("TL"), chars("TL"), "product", 0),
)


def subsets(items: Iterable[int], maximum: int = 2) -> tuple[frozenset[int], ...]:
    values = tuple(items)
    return tuple(
        frozenset(choice)
        for size in range(min(maximum, len(values)) + 1)
        for choice in itertools.combinations(values, size)
    )


def compile_table(
    controllers: tuple[Template, ...] = CONTROLLERS,
    products: tuple[Template, ...] = PRODUCTS,
) -> tuple[CompiledRow, ...]:
    rows: list[CompiledRow] = []
    for template in controllers:
        for mask in subsets(template.readonly_t_positions):
            rows.append(
                CompiledRow(
                    template.lhs,
                    mask,
                    template.name,
                    template.rhs,
                    frozenset(),
                    template.boundary,
                    template.terminal,
                )
            )
    for template in products:
        assert template.required_contact is not None
        for mask in subsets(template.t_positions):
            if template.required_contact not in mask:
                continue
            rows.append(
                CompiledRow(
                    template.lhs,
                    mask,
                    template.name,
                    template.rhs,
                    mask,
                    template.boundary,
                    template.terminal,
                )
            )
    return tuple(sorted(rows))


RAW_ROWS = compile_table()


@dataclass(frozen=True, order=True)
class Step:
    name: str
    start: int
    mask: tuple[int, ...]


def enabled_steps(
    state: State,
    rows: tuple[CompiledRow, ...] | None = None,
) -> tuple[tuple[Step, State], ...]:
    if rows is None:
        rows = ROWS
    results: list[tuple[Step, State]] = []
    for row in rows:
        width = row.support
        for start in range(len(state.word) - width + 1):
            if state.word[start : start + width] != row.source:
                continue
            local_mask = frozenset(
                index - start
                for index in state.foreign
                if start <= index < start + width
            )
            if local_mask != row.contact_mask:
                continue
            target_word = list(state.word)
            target_word[start : start + width] = row.target
            consumed = {start + offset for offset in row.consumes}
            target_foreign = frozenset(state.foreign - consumed)
            if any(target_word[index] != "T" for index in target_foreign):
                continue
            target = State(tuple(target_word), target_foreign)
            if target == state:
                continue
            results.append(
                (
                    Step(row.name, start, tuple(sorted(local_mask))),
                    target,
                )
            )
    return tuple(sorted(set(results)))


@dataclass
class Graph:
    initial: State
    edges: dict[State, tuple[tuple[Step, State], ...]]
    predecessor: dict[State, tuple[State, Step] | None]

    @property
    def normals(self) -> tuple[State, ...]:
        return tuple(sorted(state for state, edges in self.edges.items() if not edges))

    def trace(self, target: State) -> tuple[str, ...]:
        names: list[str] = []
        cursor = target
        while self.predecessor[cursor] is not None:
            source, step = self.predecessor[cursor]  # type: ignore[misc]
            names.append(step.name)
            cursor = source
        return tuple(reversed(names))


def explore(
    initial: State,
    rows: tuple[CompiledRow, ...] | None = None,
) -> Graph:
    if rows is None:
        rows = ROWS
    queue = deque((initial,))
    predecessor: dict[State, tuple[State, Step] | None] = {initial: None}
    edges: dict[State, tuple[tuple[Step, State], ...]] = {}
    while queue:
        state = queue.popleft()
        successors = enabled_steps(state, rows)
        edges[state] = successors
        for step, target in successors:
            if target not in predecessor:
                if len(predecessor) >= MAX_STATES_PER_GRAPH:
                    raise AuditTimeout("reachable graph exceeded state budget")
                predecessor[target] = (state, step)
                queue.append(target)
    return Graph(initial, edges, predecessor)


def cyclic_states(graph: Graph) -> frozenset[State]:
    index = 0
    stack: list[State] = []
    on_stack: set[State] = set()
    indices: dict[State, int] = {}
    lowlinks: dict[State, int] = {}
    cyclic: set[State] = set()

    def visit(vertex: State) -> None:
        nonlocal index
        indices[vertex] = index
        lowlinks[vertex] = index
        index += 1
        stack.append(vertex)
        on_stack.add(vertex)
        for _step, target in graph.edges[vertex]:
            if target not in indices:
                visit(target)
                lowlinks[vertex] = min(lowlinks[vertex], lowlinks[target])
            elif target in on_stack:
                lowlinks[vertex] = min(lowlinks[vertex], indices[target])
        if lowlinks[vertex] != indices[vertex]:
            return
        component: list[State] = []
        while True:
            item = stack.pop()
            on_stack.remove(item)
            component.append(item)
            if item == vertex:
                break
        if len(component) > 1:
            cyclic.update(component)
        elif any(target == vertex for _step, target in graph.edges[vertex]):
            cyclic.add(vertex)

    for state in graph.edges:
        if state not in indices:
            visit(state)
    return frozenset(cyclic)


@dataclass(frozen=True)
class CompletionFacts:
    raw_rows: int
    raw_sources: int
    duplicate_sources: int
    completed_sources: int
    unresolved: tuple[tuple[str, tuple[int, ...], tuple[str, ...]], ...]


def complete_exact_cylinders(
    raw_rows: tuple[CompiledRow, ...],
) -> tuple[tuple[CompiledRow, ...], CompletionFacts]:
    """Collapse each exact same-source product cell to its bounded common join.

    This is the preregistered completion step, not a post-witness repair.  It
    uses only the frozen raw table and emits no row when the raw successors do
    not already reduce to one identical local normal state.
    """

    grouped: dict[
        tuple[tuple[str, ...], frozenset[int]], list[CompiledRow]
    ] = {}
    for row in raw_rows:
        grouped.setdefault((row.source, row.contact_mask), []).append(row)

    compiled: list[CompiledRow] = []
    duplicates = completed = 0
    unresolved: list[tuple[str, tuple[int, ...], tuple[str, ...]]] = []
    for (source, mask), group in sorted(grouped.items()):
        outcomes = {(row.target, row.consumes) for row in group}
        if len(outcomes) == 1:
            compiled.append(sorted(group)[0])
            continue
        duplicates += 1
        normal_sets: list[tuple[State, ...]] = []
        names = tuple(sorted(row.name for row in group))
        for row in sorted(group):
            target_foreign = frozenset(mask - row.consumes)
            try:
                target = State(row.target, target_foreign)
            except ValueError:
                normal_sets.append(())
                continue
            graph = explore(target, raw_rows)
            normal_sets.append(()) if cyclic_states(graph) else normal_sets.append(graph.normals)
        if not normal_sets or any(len(normals) != 1 for normals in normal_sets):
            unresolved.append(("".join(source), tuple(sorted(mask)), names))
            continue
        common = normal_sets[0][0]
        if any(normals[0] != common for normals in normal_sets[1:]):
            unresolved.append(("".join(source), tuple(sorted(mask)), names))
            continue
        if len(common.word) != len(source) or not common.foreign <= mask:
            unresolved.append(("".join(source), tuple(sorted(mask)), names))
            continue
        completed += 1
        compiled.append(
            CompiledRow(
                source=source,
                contact_mask=mask,
                name="J_" + "_".join(names),
                target=common.word,
                consumes=frozenset(mask - common.foreign),
                boundary=sorted(group)[0].boundary,
                terminal="ABORT" if "S" in common.word else None,
            )
        )
    facts = CompletionFacts(
        raw_rows=len(raw_rows),
        raw_sources=len(grouped),
        duplicate_sources=duplicates,
        completed_sources=completed,
        unresolved=tuple(unresolved),
    )
    return tuple(sorted(compiled)), facts


ROWS, COMPLETION = complete_exact_cylinders(RAW_ROWS)


def initial_state(n: int, contacts: Iterable[int]) -> State:
    return State(
        tuple(("R", "H", *(["T"] * n), "A")),
        frozenset(1 + contact for contact in contacts),
    )


def expected_clean(n: int) -> State:
    return State(tuple(("R", *(["P"] * (n - 1)), "H", "L", "A")))


def expected_abort(n: int) -> State:
    return State(tuple(("R", *(["P"] * (n + 1)), "S")))


def all_fixtures() -> tuple[tuple[int, tuple[int, ...]], ...]:
    return tuple(
        (n, contact_tuple)
        for n in range(1, 11)
        for size in range(3)
        for contact_tuple in itertools.combinations(range(1, n + 1), size)
    )


@dataclass(frozen=True)
class Failure:
    fixture_index: int
    n: int
    contacts: tuple[int, ...]
    graph: Graph
    cycles: frozenset[State]
    expected: State

    @property
    def reason(self) -> str:
        if self.cycles:
            return "reachable-cycle"
        if not self.graph.normals:
            return "no-normal-form"
        if len(self.graph.normals) != 1:
            return "multiple-normal-forms"
        return "wrong-normal-form"


@dataclass(frozen=True)
class Census:
    passed: int
    states: int
    transitions: int
    max_states: int
    failure: Failure | None


def run_census(rows: tuple[CompiledRow, ...] = ROWS) -> Census:
    passed = states = transitions = max_states = 0
    for fixture_index, (n, contacts) in enumerate(all_fixtures(), start=1):
        graph = explore(initial_state(n, contacts), rows)
        cycles = cyclic_states(graph)
        expected = expected_clean(n) if not contacts else expected_abort(n)
        states += len(graph.edges)
        transitions += sum(len(edges) for edges in graph.edges.values())
        max_states = max(max_states, len(graph.edges))
        if graph.normals != (expected,) or cycles:
            return Census(
                passed,
                states,
                transitions,
                max_states,
                Failure(fixture_index, n, contacts, graph, cycles, expected),
            )
        passed += 1
    return Census(passed, states, transitions, max_states, None)


def participant_accounting_facts(
    rows: tuple[CompiledRow, ...], fixture_limit: int,
) -> tuple[int, tuple[str, ...]]:
    checked = 0
    failures: list[str] = []
    for fixture_index, (n, contacts) in enumerate(all_fixtures(), start=1):
        if fixture_index > fixture_limit:
            break
        graph = explore(initial_state(n, contacts), rows)
        for source, edges in graph.edges.items():
            for step, target in edges:
                checked += 1
                candidates = tuple(
                    row
                    for row in rows
                    if row.name == step.name
                    and row.source
                    == source.word[step.start : step.start + row.support]
                    and row.contact_mask == frozenset(step.mask)
                )
                if len(candidates) != 1:
                    failures.append(f"row-resolution:{source.text()}:{step.name}")
                    continue
                row = candidates[0]
                expected_word = list(source.word)
                expected_word[step.start : step.start + row.support] = row.target
                expected_foreign = frozenset(
                    source.foreign
                    - {step.start + offset for offset in row.consumes}
                )
                if (
                    target.word != tuple(expected_word)
                    or target.foreign != expected_foreign
                    or not target.foreign <= source.foreign
                ):
                    failures.append(f"participant-accounting:{source.text()}:{step.name}")
    return checked, tuple(failures)


def local_rank(state: State) -> tuple[int, int, int, int]:
    """Frozen phase-gated local rank candidate.

    This is tested on every executed edge and on translated template contexts.
    A bounded pass is not reported as arbitrary-length closure unless the
    translated check also succeeds.
    """

    live = int("S" not in state.word)
    if not live:
        return (0, 0, 0, 0)
    foreign = len(state.foreign)
    word = state.word
    seam = len(word) - 1
    if "H" not in word:
        positions = [i for i, symbol in enumerate(word) if symbol == "L"]
        return (live, foreign, 2, sum(positions))
    h = word.index("H")
    if h + 2 < len(word) and word[h + 1 : h + 3] == ("T", "L"):
        return (live, foreign, 1, seam - (h + 2))
    if h + 1 < len(word) and word[h + 1] == "L":
        extra_l = [i for i, symbol in enumerate(word[h + 2 :], h + 2) if symbol == "L"]
        if extra_l:
            return (live, foreign, 2, sum(extra_l))
        return (live, foreign, 3, seam - (h + 1))
    return (live, foreign, 4, h)


def rank_facts(rows: tuple[CompiledRow, ...], census: Census) -> dict[str, object]:
    checked = 0
    failures: list[tuple[str, str, str]] = []
    if census.failure is None:
        fixture_iter = all_fixtures()
    else:
        fixture_iter = all_fixtures()[: census.failure.fixture_index]
    for n, contacts in fixture_iter:
        graph = explore(initial_state(n, contacts), rows)
        for source, edges in graph.edges.items():
            for step, target in edges:
                checked += 1
                if not local_rank(target) < local_rank(source):
                    failures.append((step.name, source.text(), target.text()))
                    if len(failures) == 4:
                        break
            if len(failures) == 4:
                break
        if len(failures) == 4:
            break
    return {
        "checked": checked,
        "failures": tuple(failures),
        "translated": False,
        "formula": "(live,unquenched_F,phase,phase_gated_displacement)",
    }


def table_facts(rows: tuple[CompiledRow, ...] = ROWS) -> dict[str, object]:
    sources: dict[tuple[tuple[str, ...], frozenset[int]], set[tuple[tuple[str, ...], frozenset[int]]]] = {}
    by_mode = Counter()
    by_boundary = Counter()
    for row in rows:
        key = (row.source, row.contact_mask)
        value = (row.target, row.consumes)
        sources.setdefault(key, set()).add(value)
        by_mode["product" if row.consumes else "controller"] += 1
        by_boundary[row.boundary] += 1
    unequal = tuple(
        ("".join(source), tuple(sorted(mask)), len(targets))
        for (source, mask), targets in sorted(sources.items())
        if len(targets) > 1
    )
    digest_payload = [
        {
            "source": "".join(row.source),
            "mask": sorted(row.contact_mask),
            "name": row.name,
            "target": "".join(row.target),
            "consumes": sorted(row.consumes),
            "boundary": row.boundary,
        }
        for row in rows
    ]
    return {
        "rows": len(rows),
        "sources": len(sources),
        "controller": by_mode["controller"],
        "product": by_mode["product"],
        "boundary": dict(sorted(by_boundary.items())),
        "max_support": max(row.support for row in rows),
        "unequal": unequal,
        "sha256": hashlib.sha256(
            json.dumps(digest_payload, sort_keys=True, separators=(",", ":")).encode()
        ).hexdigest(),
    }


class Checks:
    def __init__(self) -> None:
        self.results: list[tuple[str, bool]] = []

    def check(self, label: str, condition: bool) -> None:
        self.results.append((label, bool(condition)))

    @property
    def passed(self) -> int:
        return sum(condition for _label, condition in self.results)

    @property
    def failed(self) -> int:
        return len(self.results) - self.passed


def audit_inputs_bound() -> tuple[bool, str]:
    paths = tuple(ROOT / path for path in AUDIT_INPUT_PATHS)
    if not all(path.is_file() for path in paths):
        return False, "missing"
    text = "\n".join(path.read_text() for path in paths)
    normalized = " ".join(text.split())
    required = (
        "all 230 reduced words" in normalized
        and "No Block-228 primary runner may be written" in normalized
        and "behaviorally_executed=<n>" in normalized
        and "partial attempt with named untested routes" in normalized
    )
    return required, hashlib.sha256(text.encode()).hexdigest()


def scientific_run(rows: tuple[CompiledRow, ...] = ROWS) -> tuple[Checks, list[str], Census]:
    checks = Checks()
    input_bound, input_sha = audit_inputs_bound()
    table = table_facts(rows)
    fixtures = all_fixtures()
    census = run_census(rows) if not COMPLETION.unresolved else Census(0, 0, 0, 0, None)
    accounting_checked, accounting_failures = participant_accounting_facts(
        rows,
        230 if census.failure is None else census.failure.fixture_index,
    )
    rank = (
        rank_facts(rows, census)
        if not COMPLETION.unresolved and census.failure is None
        else {
            "checked": 0,
            "failures": (),
            "translated": False,
            "formula": "(live,unquenched_F,phase,phase_gated_displacement)",
        }
    )

    checks.check(
        "literal committed Block-228 packet binds the product compiler",
        input_bound and len(AUDIT_INPUT_PATHS) == 11,
    )
    checks.check(
        "fixture generator emits exactly 230 zero/one/two-contact words",
        len(fixtures) == 230
        and Counter(len(contacts) for _n, contacts in fixtures)
        == Counter({0: 10, 1: 55, 2: 165}),
    )
    checks.check(
        "all compiled rows use a fixed onsite alphabet and at most four arm sites",
        table["max_support"] <= 4
        and all(set(row.source + row.target) <= set("RPHLTAS") for row in rows),
    )
    checks.check(
        "read-only controller lifts preserve only unchanged contacted T sites",
        all(
            row.contact_mask
            <= frozenset(
                i
                for i, (left, right) in enumerate(zip(row.source, row.target))
                if left == right == "T"
            )
            for row in rows
            if not row.consumes
        ),
    )
    checks.check(
        "every product row consumes its complete exact displayed contact mask",
        all(row.consumes == row.contact_mask for row in rows if row.consumes),
    )
    checks.check(
        "all four unequal raw cylinders mechanically reduce to bounded common joins",
        COMPLETION.duplicate_sources == 4
        and COMPLETION.completed_sources == 4
        and not COMPLETION.unresolved,
    )
    checks.check(
        "the completed table has one output distribution per exact local cylinder",
        not table["unequal"] and len(rows) == COMPLETION.raw_sources,
    )
    checks.check(
        "the canonical 230-word exploration stops only at its first exact failure or exhausts the suite",
        not COMPLETION.unresolved
        and census.passed
        == (230 if census.failure is None else census.failure.fixture_index - 1),
    )
    checks.check(
        "every executed transition preserves valid participant accounting",
        accounting_checked == census.transitions and not accounting_failures,
    )

    if census.failure is None:
        checks.check(
            "all 230 reduced product words have their unique declared normal form and no cycle",
            census.passed == 230,
        )
        checks.check(
            "one length-independent local rank decreases on every executed and translated row",
            not rank["failures"] and bool(rank["translated"]),
        )
        decision = (
            "positive-reduced-product-open-full-state"
            if not rank["failures"] and rank["translated"]
            else "scoped-product-rank-failure"
        )
    else:
        checks.check(
            "first failing fixture and every normal/cycle residue are explicit",
            bool(census.failure.graph.edges)
            and (
                bool(census.failure.cycles)
                or census.failure.graph.normals != (census.failure.expected,)
            ),
        )
        decision = (
            "scoped-product-cell-nonjoinable"
            if census.failure.reason in {"multiple-normal-forms", "wrong-normal-form"}
            else "scoped-product-rank-failure"
            if census.failure.reason == "reachable-cycle"
            else "scoped-product-cell-nonjoinable"
        )

    lines = [
        "COMPLETION "
        f"raw_rows={COMPLETION.raw_rows} raw_sources={COMPLETION.raw_sources} "
        f"duplicate_sources={COMPLETION.duplicate_sources} "
        f"completed_sources={COMPLETION.completed_sources} "
        f"unresolved={len(COMPLETION.unresolved)}",
        "TABLE "
        f"rows={table['rows']} sources={table['sources']} "
        f"controller={table['controller']} product={table['product']} "
        f"by_boundary={json.dumps(table['boundary'], sort_keys=True, separators=(',', ':'))} "
        f"max_support={table['max_support']}",
        "CENSUS "
        f"passed={census.passed}/230 states={census.states} "
        f"transitions={census.transitions} max_states={census.max_states}",
        f"ACCOUNTING transitions={accounting_checked} mismatches={len(accounting_failures)}",
    ]
    if census.failure is not None:
        failure = census.failure
        normals = tuple(state.text() for state in failure.graph.normals)
        traces = tuple(
            ">".join(failure.graph.trace(state)) or "identity"
            for state in failure.graph.normals
        )
        lines.extend(
            (
                "FIRST_FAILURE "
                f"fixture={failure.fixture_index} n={failure.n} "
                f"contacts={failure.contacts} reason={failure.reason} "
                f"source={failure.graph.initial.text()} expected={failure.expected.text()}",
                "FIRST_FAILURE_NORMALS " + " | ".join(normals),
                "FIRST_FAILURE_TRACES " + " | ".join(traces),
                "FIRST_FAILURE_CYCLES "
                + " | ".join(state.text() for state in sorted(failure.cycles)[:4]),
            )
        )
    lines.extend(
        (
            f"RANK formula={rank['formula']} checked={rank['checked']} "
            f"failures={len(rank['failures'])} translated={str(rank['translated']).lower()}",
            "RANK_FIRST "
            + (
                " | ".join(
                    f"{name}:{source}->{target}"
                    for name, source, target in rank["failures"]
                )
                if rank["failures"]
                else "none"
            ),
            f"DECISION_CLASS {decision}",
            "SCOPE reduced_word_product_only labelled_darts_carrier_CP_fairness_Record_and_law_selection_unexecuted",
            f"TABLE_SHA256 {table['sha256']}",
            f"AUDIT_INPUT_SHA256 {input_sha}",
            "per_element: checked — every reduced onsite symbol and exact displayed contact mask is explicit in the frozen table.",
            "per_site: checked — the canonical suite covers all 230 words through length ten and stops at the first exact residue.",
            "per_mode: checked and not executed — labelled carrier modes, projectors, Kraus labels, and physical transports remain gated.",
            "per_block: checked and not executed — full-state Y/parallel, CP, and fairness stages cannot inherit a reduced-word result.",
            "lattice_wide: checked and not executed — arbitrary finite arms, infinite-volume fixation, physical time, Record writing, and law selection remain open.",
        )
    )
    return checks, lines, census


def census_observable(rows: tuple[CompiledRow, ...]) -> tuple[dict[str, object], dict[str, object]]:
    table = table_facts(rows)
    census = run_census(rows)
    graph_observable: dict[str, object] = {
        "passed": census.passed,
        "states": census.states,
        "transitions": census.transitions,
        "max_states": census.max_states,
    }
    if census.failure is not None:
        failure = census.failure
        graph_observable["failure"] = {
            "fixture": failure.fixture_index,
            "n": failure.n,
            "contacts": failure.contacts,
            "reason": failure.reason,
            "normals": tuple(state.text() for state in failure.graph.normals),
            "cycles": tuple(state.text() for state in sorted(failure.cycles)),
        }
    full = {
        "table": table["sha256"],
        "graph": graph_observable,
    }
    return full, graph_observable


def mutation_run() -> tuple[Checks, list[str]]:
    checks = Checks()
    plan = (ROOT / PACKET / "MUTATION_PLAN.md").read_text()
    contract_count = sum(
        line.lstrip().split(".", 1)[0].isdigit()
        for line in plan.splitlines()
        if "." in line
    )
    baseline_full, baseline_graph = census_observable(ROWS)
    mutation_rows = ROWS[:32]
    fingerprints: list[str] = []
    changed = graph_changed = 0
    for omitted in mutation_rows:
        mutated = tuple(row for row in ROWS if row != omitted)
        full, graph = census_observable(mutated)
        changed += int(full != baseline_full)
        graph_changed += int(graph != baseline_graph)
        fingerprints.append(
            hashlib.sha256(
                json.dumps(full, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()
        )

    checks.check(
        "committed mutation plan binds exactly 48 distinct defect contracts",
        contract_count == 48,
    )
    checks.check(
        "32 compiled-row omission mutations execute through the real census",
        len(mutation_rows) == 32 and len(fingerprints) == 32,
    )
    checks.check(
        "every executed mutation changes a mutation-name-free observable",
        changed == 32,
    )
    checks.check(
        "all executed mutations have distinct mutation-name-free fingerprints",
        len(set(fingerprints)) == 32,
    )
    checks.check(
        "at least twelve executed omissions alter the reachable graph before fail-fast",
        graph_changed >= 12,
    )
    digest = hashlib.sha256("".join(sorted(fingerprints)).encode()).hexdigest()
    lines = [
        "MUTATION_SURFACE "
        f"contract_bound={contract_count} behaviorally_executed=32 "
        f"graph_changed={graph_changed} downstream_unexecuted={contract_count - 32}",
        f"MUTATION_FINGERPRINT_SHA256 {digest}",
        "per_element: checked — each executed omission removes one exact compiled row from the live table.",
        "per_site: checked — every mutation reruns the canonical word census through its first exact stop.",
        "per_mode: checked and not executed — carrier/projector mutations remain downstream of reduced Stage A.",
        "per_block: checked and not executed — sixteen full-state, CP, fairness, and promotion defects remain unexecuted after fail-fast.",
        "lattice_wide: checked and not executed — no finite mutation result is promoted to arbitrary-length or physical-law closure.",
    ]
    return checks, lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--science-only", action="store_true")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        if args.self_test:
            checks, fact_lines = mutation_run()
        else:
            checks, fact_lines, _census = scientific_run()
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    lines = [
        *(f"{'PASS' if condition else 'FAIL'} {label}" for label, condition in checks.results),
        *fact_lines,
        f"RUNNER_SHA256 {hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}",
        f"TOTAL: PASS={checks.passed} FAIL={checks.failed}",
    ]
    output = "\n".join(lines)
    print(output)
    if len(output) >= 6_000:
        return 1
    return 1 if checks.failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (AuditTimeout, ValueError, AssertionError) as error:
        print(f"FAIL {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise SystemExit(1)
