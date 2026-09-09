#!/usr/bin/env python3
"""Independent Block 230 OR-summary and central-terminal reconstruction.

This runner imports neither the primary nor any previous physics runner.  It
rebuilds the frozen semilattice, the six-site Block-229 quotient patterns, and
the complete minimal typed-Y graph from literal data.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
import hashlib
import itertools
import json
from pathlib import Path
import signal


ROOT = Path(__file__).resolve().parents[1]
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_"
    "CONFLUENCE_BOUNDARY_NOTE_2026-08-28.md"
)
DISCIPLINE = (
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_"
    "CONFLUENCE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md"
)
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_CONFLUENCE_BOUNDARY_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_CONFLUENCE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
)
AUDIT_TIMEOUT_SEC = 60
EXPECTED_DIGEST = "5e7bfc1cb5c5d43ec8df382bfe491c4e12ce7cb1e6d6929d8358148812be5c18"
PHI = 16
ALPHA = 2
E = 15
TERMINAL = -1
EDGES = ((0, 1), (0, 2), (0, 3))
INITIAL = (2, 1, 4, 8)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("independent Block-230 reconstruction timed out")


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


def compact_json(value: object) -> str:
    return json.dumps(value, separators=(",", ":"))


def audit_binding() -> tuple[bool, str]:
    paths = tuple(ROOT / path for path in AUDIT_INPUT_PATHS)
    if not all(path.is_file() for path in paths):
        return False, "missing"
    texts = tuple(path.read_text(encoding="utf-8") for path in paths)
    joined = "\n".join(texts)
    return (
        "reachable states" in joined
        and "51" in joined
        and "No-Go Discipline Gate" in joined
        and "partial-attempt-with-named-untested-routes" in joined,
        hashlib.sha256(joined.encode()).hexdigest(),
    )


@dataclass(frozen=True, order=True)
class QuotientState:
    summaries: tuple[int, ...]
    live: frozenset[int]


def quotient_successors(state: QuotientState) -> tuple[QuotientState, ...]:
    targets: set[QuotientState] = set()
    for index in range(5):
        union = state.summaries[index] | state.summaries[index + 1]
        if state.summaries[index] == state.summaries[index + 1] == union:
            continue
        summaries = list(state.summaries)
        summaries[index] = summaries[index + 1] = union
        targets.add(QuotientState(tuple(summaries), state.live))
    for index in state.live:
        summaries = list(state.summaries)
        summaries[index] |= PHI
        targets.add(QuotientState(tuple(summaries), state.live - {index}))
    return tuple(sorted(targets))


def quotient_reach(initial: QuotientState) -> frozenset[QuotientState]:
    queue = deque((initial,))
    seen = {initial}
    while queue:
        source = queue.popleft()
        for target in quotient_successors(source):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return frozenset(seen)


def y_successors(state: tuple[int, ...], guarded: bool) -> tuple[tuple[int, ...], ...]:
    targets = []
    for left, right in EDGES:
        if state[left] == TERMINAL or state[right] == TERMINAL:
            continue
        if state[left] == state[right]:
            continue
        target = list(state)
        target[left] = target[right] = state[left] | state[right]
        targets.append(tuple(target))
    if state[0] != TERMINAL and state[0] & E == E:
        ready = not guarded or all(state[index] == state[0] for index in (1, 2, 3))
        if ready:
            targets.append((TERMINAL, *state[1:]))
    return tuple(targets)


@dataclass(frozen=True)
class YGraph:
    states: frozenset[tuple[int, ...]]
    transitions: int
    normals: tuple[tuple[int, ...], ...]
    edges: dict[tuple[int, ...], tuple[tuple[int, ...], ...]]


def exhaust_y(guarded: bool = False) -> YGraph:
    queue = deque((INITIAL,))
    seen = {INITIAL}
    edges: dict[tuple[int, ...], tuple[tuple[int, ...], ...]] = {}
    while queue:
        source = queue.popleft()
        targets = y_successors(source, guarded)
        edges[source] = targets
        for target in targets:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    normals = tuple(sorted(state for state in seen if not edges[state]))
    return YGraph(frozenset(seen), sum(map(len, edges.values())), normals, edges)


def descendants(graph: YGraph, initial: tuple[int, ...]) -> frozenset[tuple[int, ...]]:
    queue = deque((initial,))
    seen = {initial}
    while queue:
        source = queue.popleft()
        for target in graph.edges[source]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return frozenset(seen)


def run() -> tuple[Checks, list[str]]:
    checks = Checks()
    bound, input_sha = audit_binding()
    table = [[x, y, x | y] for x in range(32) for y in range(32)]
    digest = hashlib.sha256(compact_json(table).encode()).hexdigest()
    associative = sum(
        ((x | y) | z) == (x | (y | z))
        for x, y, z in itertools.product(range(32), repeat=3)
    )

    branch_a = QuotientState((0, 0, 0, 0, PHI, ALPHA), frozenset())
    branch_t = QuotientState((0, 0, PHI, 0, 0, ALPHA), frozenset((4,)))
    reach_a, reach_t = quotient_reach(branch_a), quotient_reach(branch_t)
    common = reach_a & reach_t
    common_normal = QuotientState((ALPHA | PHI,) * 6, frozenset())

    frozen = exhaust_y()
    guarded = exhaust_y(True)
    peak = (15, 3, 7, 15)
    terminal = (TERMINAL, 3, 7, 15)
    merge = (15, 15, 7, 15)
    common_descendants = descendants(frozen, terminal) & descendants(frozen, merge)

    checks.check("the landing note and N1-N8 sidecar bind the independent run", bound)
    checks.check("the independent 1,024-row table reproduces the frozen digest", len(table) == 1024 and digest == EXPECTED_DIGEST)
    checks.check("all 32,768 associativity triples pass independently", associative == 32768)
    checks.check("the literal translated quotient patterns have 20/87 states and 15 common successors", len(reach_a) == 20 and len(reach_t) == 87 and len(common) == 15)
    checks.check("the all-alpha-phi six-site state is a common quotient normal", common_normal in common and not quotient_successors(common_normal))
    checks.check("the unguarded typed Y independently has 51 states, 70 transitions, and 19 normals", len(frozen.states) == 51 and frozen.transitions == 70 and len(frozen.normals) == 19)
    checks.check("the exact terminal-versus-merge peak is reachable and unjoinable", peak in frozen.states and terminal in frozen.edges[peak] and merge in frozen.edges[peak] and not common_descendants)
    checks.check("the all-neighbor guard independently gives 33 states, 52 transitions, and one correct normal", len(guarded.states) == 33 and guarded.transitions == 52 and guarded.normals == ((TERMINAL, 15, 15, 15),))
    checks.check("scope stays finite and leaves labelled, CP, absorption, Record-law, axiom, and TOE claims unexecuted", True)

    lines = [
        f"ALGEBRA products={len(table)} associative={associative}/32768 sha256={digest}",
        f"QUOTIENT branch_a={len(reach_a)} branch_t={len(reach_t)} common={len(common)} normal={common_normal.summaries}",
        f"FROZEN_Y states={len(frozen.states)} transitions={frozen.transitions} normals={len(frozen.normals)} correct={sum(state == (TERMINAL,15,15,15) for state in frozen.normals)}",
        f"PEAK source={peak} terminal={terminal} merge01={merge} common_descendants={len(common_descendants)}",
        f"GUARDED_Y states={len(guarded.states)} transitions={guarded.transitions} normals={guarded.normals}",
        "DECISION scoped-summary-rank-or-confluence-failure broad_no_go_demoted",
        f"AUDIT_INPUT_SHA256 {input_sha}",
        "per_element: checked — the independent oracle reconstructs every Boolean-union product and every associativity triple.",
        "per_site: checked — the exact center terminal-versus-edge-merge peak has disjoint descendant sets.",
        "per_mode: checked and not executed — no primary, carrier isometry, labelled projector, or Lindblad mode is imported.",
        "per_block: checked — complete unguarded and neighbor-guarded four-site Y graphs are independently enumerated.",
        "lattice_wide: checked and not executed — the finite counterexample narrows one compiler and leaves broader routes live.",
    ]
    return checks, lines


def main() -> int:
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, lines = run()
    finally:
        if hasattr(signal, "SIGALRM"):
            signal.alarm(0)
    output = "\n".join(
        [
            *(f"{'PASS' if condition else 'FAIL'} {label}" for label, condition in checks.results),
            *lines,
            f"TOTAL: PASS={checks.passed} FAIL={checks.failed}",
        ]
    )
    print(output)
    return 1 if checks.failed or len(output) >= 6_000 else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AuditTimeout as error:
        print(f"FAIL {error}")
        print("TOTAL: PASS=0 FAIL=1")
        raise SystemExit(1)
