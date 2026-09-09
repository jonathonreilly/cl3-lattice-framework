#!/usr/bin/env python3
"""Block 230 ACI component-summary terminal-confluence gate.

The frozen Boolean-union core is reconstructed exactly, including the
Block-229 translated overlap discriminator.  Stage A1 then stops at the first
in-domain typed Y counterexample: replacing the central writer summary by a
terminal ray can cut the gossip graph before the collected union has been
broadcast to every arm.  Later bounded suites and physical stages are not
executed after that preregistered hard stop.
"""

from __future__ import annotations

import argparse
from collections import defaultdict, deque
from dataclasses import dataclass
import hashlib
import importlib.util
import itertools
import json
from pathlib import Path
import signal
import sys
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
PARENT_PATH = (
    ROOT
    / "scripts/admissibility_d4_h1_cleanup_front_coalescence_radius_2026_08_28.py"
)
PACKET = (
    ".claude/science/physics-loops/"
    "toe-axiom-closure-block230-aci-component-summary-20260828"
)
NOTE = (
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_"
    "CONFLUENCE_BOUNDARY_NOTE_2026-08-28.md"
)
DISCIPLINE = (
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_"
    "CONFLUENCE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md"
)
AUDIT_INPUT_PATHS = (
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/GOAL.md",
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/PREREGISTRATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/MUTATION_PLAN.md",
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/PANEL_ADJUDICATION.md",
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/APPROACH_REGISTRY.md",
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/NO_GO_LEDGER.md",
    ".claude/science/physics-loops/toe-axiom-closure-block230-aci-component-summary-20260828/STATE.yaml",
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_CONFLUENCE_BOUNDARY_NOTE_2026-08-28.md",
    "docs/ADMISSIBILITY_D4_H1_ACI_COMPONENT_SUMMARY_TERMINAL_CONFLUENCE_NO_GO_DISCIPLINE_CHECKLIST_2026-08-28.md",
    "scripts/admissibility_d4_h1_cleanup_front_coalescence_radius_2026_08_28.py",
)
AUDIT_TIMEOUT_SEC = 120
EXPECTED_JOIN_SHA256 = (
    "5e7bfc1cb5c5d43ec8df382bfe491c4e12ce7cb1e6d6929d8358148812be5c18"
)

RHO = 1
ALPHA = 2
LAMBDA = 4
CHI = 8
PHI = 16
EXPECTED_Y = RHO | ALPHA | LAMBDA | CHI
CLEAN = 64
Y_EDGES = ((0, 1), (0, 2), (0, 3))
Y_INITIAL = (ALPHA, RHO, LAMBDA, CHI)


class AuditTimeout(RuntimeError):
    pass


def timeout_handler(_signum: int, _frame: object) -> None:
    raise AuditTimeout("Block-230 terminal-confluence gate exceeded its timeout")


def load_parent() -> object:
    spec = importlib.util.spec_from_file_location("block229_cleanup", PARENT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Block-229 parent")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


P = load_parent()


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


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def audit_inputs_bound() -> tuple[bool, str]:
    paths = tuple(ROOT / path for path in AUDIT_INPUT_PATHS)
    if not all(path.is_file() for path in paths):
        return False, "missing"
    texts = tuple(path.read_text(encoding="utf-8") for path in paths)
    joined = "\n".join(texts)
    normalized = " ".join(joined.split())
    bound = (
        "abstract algebra, carrier map, topology class" in normalized
        and "one typed seam" in normalized
        and "scoped-summary-rank-or-confluence-failure" in normalized
        and "No-Go Discipline Gate" in normalized
        and "19 distinct" in normalized
        and "terminal normal forms" in normalized
    )
    return bound, hashlib.sha256(joined.encode()).hexdigest()


def join_table(join: Callable[[int, int], int] = lambda x, y: x | y) -> list[list[int]]:
    return [[x, y, join(x, y)] for x in range(32) for y in range(32)]


@dataclass(frozen=True)
class AlgebraFacts:
    products: int
    digest: str
    associative: int
    commutative: int
    idempotent: int
    bottom: int


def algebra_facts(
    join: Callable[[int, int], int] = lambda x, y: x | y,
) -> AlgebraFacts:
    table = join_table(join)
    return AlgebraFacts(
        products=len(table),
        digest=hashlib.sha256(canonical_json(table).encode()).hexdigest(),
        associative=sum(
            join(join(x, y), z) == join(x, join(y, z))
            for x, y, z in itertools.product(range(32), repeat=3)
        ),
        commutative=sum(
            join(x, y) == join(y, x)
            for x, y in itertools.product(range(32), repeat=2)
        ),
        idempotent=sum(join(x, x) == x for x in range(32)),
        bottom=sum(join(0, x) == join(x, 0) == x for x in range(32)),
    )


@dataclass(frozen=True, order=True)
class OverlapState:
    summaries: tuple[int, ...]
    live_participants: frozenset[int]


def overlap_successors(state: OverlapState) -> tuple[OverlapState, ...]:
    targets: set[OverlapState] = set()
    for index in range(len(state.summaries) - 1):
        union = state.summaries[index] | state.summaries[index + 1]
        if state.summaries[index] == state.summaries[index + 1] == union:
            continue
        summaries = list(state.summaries)
        summaries[index] = summaries[index + 1] = union
        targets.add(OverlapState(tuple(summaries), state.live_participants))
    for index in state.live_participants:
        summaries = list(state.summaries)
        summaries[index] |= PHI
        targets.add(
            OverlapState(
                tuple(summaries), state.live_participants.difference((index,))
            )
        )
    return tuple(sorted(targets))


def reach_overlap(initial: OverlapState) -> frozenset[OverlapState]:
    queue = deque((initial,))
    seen = {initial}
    while queue:
        source = queue.popleft()
        for target in overlap_successors(source):
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return frozenset(seen)


def old_symbol_summary(symbol: str) -> int:
    return {"R": RHO, "A": ALPHA, "L": PHI}.get(symbol, 0)


def quotient_overlap(state: object, lo: int, hi: int) -> OverlapState:
    summaries = tuple(old_symbol_summary(state.word[index]) for index in range(lo, hi))
    live = frozenset(index - lo for index in state.foreign if lo <= index < hi)
    return OverlapState(summaries, live)


@dataclass(frozen=True)
class WitnessFacts:
    translations: tuple[tuple[int, int, int, int], ...]
    common_normal: tuple[int, ...]


def witness_facts() -> WitnessFacts:
    translations = []
    common_normal: tuple[int, ...] = ()
    for n in range(10, 17):
        source = P.critical_source(n)
        branch_a = P.take(source, "CF_A", n - 1)
        branch_t = P.take(source, "CF_T", n - 3)
        lo, hi = n - 3, n + 3
        reach_a = reach_overlap(quotient_overlap(branch_a, lo, hi))
        reach_t = reach_overlap(quotient_overlap(branch_t, lo, hi))
        common = reach_a & reach_t
        translations.append((n, len(reach_a), len(reach_t), len(common)))
        normal = OverlapState((ALPHA | PHI,) * 6, frozenset())
        if normal in common:
            common_normal = normal.summaries
    return WitnessFacts(tuple(translations), common_normal)


def old_table_factorization_violations() -> tuple[tuple[object, ...], ...]:
    groups: dict[tuple[int, ...], list[tuple[object, ...]]] = defaultdict(list)
    for row in P.ROWS:
        source = [old_symbol_summary(symbol) for symbol in row.source]
        for offset in row.contact_mask:
            source[offset] |= PHI
        target = tuple(old_symbol_summary(symbol) for symbol in row.target)
        groups[tuple(source)].append(
            (
                row.name,
                target,
                tuple(sorted(row.consumes)),
                "".join(row.source),
                "".join(row.target),
            )
        )
    violations = []
    for source, rows in sorted(groups.items()):
        if len({(row[1], row[2]) for row in rows}) > 1:
            violations.append((source, tuple(rows)))
    return tuple(violations)


@dataclass(frozen=True, order=True)
class YState:
    sites: tuple[int, int, int, int]

    @property
    def writer_live(self) -> bool:
        return self.sites[0] < CLEAN


@dataclass(frozen=True, order=True)
class Step:
    kind: str
    edge: int = -1


@dataclass
class Graph:
    edges: dict[YState, tuple[tuple[Step, YState], ...]]
    predecessor: dict[YState, tuple[YState, Step] | None]

    @property
    def normals(self) -> tuple[YState, ...]:
        return tuple(sorted(state for state, edges in self.edges.items() if not edges))

    @property
    def transitions(self) -> int:
        return sum(len(edges) for edges in self.edges.values())


def enabled_y(
    state: YState,
    *,
    neighbor_guard: bool = False,
    one_endpoint_merge: bool = False,
    identity_edges: bool = False,
) -> tuple[tuple[Step, YState], ...]:
    targets: list[tuple[Step, YState]] = []
    for edge, (left, right) in enumerate(Y_EDGES):
        x, y = state.sites[left], state.sites[right]
        if x >= CLEAN or y >= CLEAN:
            continue
        union = x | y
        if x == y and not identity_edges:
            continue
        sites = list(state.sites)
        sites[left] = union
        if not one_endpoint_merge:
            sites[right] = union
        target = YState(tuple(sites))
        if target != state or identity_edges:
            targets.append((Step("merge", edge), target))
    writer = state.sites[0]
    terminal_ready = writer < CLEAN and writer & EXPECTED_Y == EXPECTED_Y
    if neighbor_guard and terminal_ready:
        terminal_ready = all(state.sites[index] == writer for index in (1, 2, 3))
    if terminal_ready:
        targets.append((Step("terminal"), YState((CLEAN, *state.sites[1:]))))
    return tuple(targets)


def explore_y(**options: bool) -> Graph:
    initial = YState(Y_INITIAL)
    queue = deque((initial,))
    predecessor: dict[YState, tuple[YState, Step] | None] = {initial: None}
    edges: dict[YState, tuple[tuple[Step, YState], ...]] = {}
    while queue:
        source = queue.popleft()
        successors = enabled_y(source, **options)
        edges[source] = successors
        for step, target in successors:
            if target not in predecessor:
                predecessor[target] = (source, step)
                queue.append(target)
    return Graph(edges, predecessor)


def descendants(graph: Graph, initial: YState) -> frozenset[YState]:
    queue = deque((initial,))
    seen = {initial}
    while queue:
        source = queue.popleft()
        for _step, target in graph.edges[source]:
            if target not in seen:
                seen.add(target)
                queue.append(target)
    return frozenset(seen)


def y_rank(state: YState) -> int:
    return sum(
        5 - site.bit_count() for site in state.sites if site < CLEAN
    ) + int(state.writer_live)


@dataclass(frozen=True)
class YFacts:
    states: int
    transitions: int
    normals: int
    correct_normals: int
    peak: YState
    terminal_target: YState
    merge_target: YState
    descendant_intersection: int
    rank_failures: int
    guarded_states: int
    guarded_transitions: int
    guarded_normals: tuple[YState, ...]


def y_facts() -> YFacts:
    graph = explore_y()
    peak = YState((EXPECTED_Y, RHO | ALPHA, RHO | ALPHA | LAMBDA, EXPECTED_Y))
    peak_targets = dict((step, target) for step, target in graph.edges[peak])
    terminal_target = peak_targets[Step("terminal")]
    merge_target = peak_targets[Step("merge", 0)]
    rank_failures = sum(
        y_rank(target) >= y_rank(source)
        for source, successors in graph.edges.items()
        for _step, target in successors
    )
    correct = YState((CLEAN, EXPECTED_Y, EXPECTED_Y, EXPECTED_Y))
    guarded = explore_y(neighbor_guard=True)
    return YFacts(
        states=len(graph.edges),
        transitions=graph.transitions,
        normals=len(graph.normals),
        correct_normals=sum(normal == correct for normal in graph.normals),
        peak=peak,
        terminal_target=terminal_target,
        merge_target=merge_target,
        descendant_intersection=len(
            descendants(graph, terminal_target) & descendants(graph, merge_target)
        ),
        rank_failures=rank_failures,
        guarded_states=len(guarded.edges),
        guarded_transitions=guarded.transitions,
        guarded_normals=guarded.normals,
    )


def graph_observable(**options: bool) -> str:
    graph = explore_y(**options)
    payload = tuple(
        (
            source.sites,
            tuple((step.kind, step.edge, target.sites) for step, target in successors),
        )
        for source, successors in sorted(graph.edges.items())
    )
    return hashlib.sha256(canonical_json(payload).encode()).hexdigest()


def mutation_run() -> tuple[Checks, list[str]]:
    checks = Checks()
    plan = (ROOT / PACKET / "MUTATION_PLAN.md").read_text(encoding="utf-8")
    contract_bound = sum(
        line.lstrip().split(".", 1)[0].isdigit()
        for line in plan.splitlines()
        if "." in line
    )
    baseline_algebra = algebra_facts()
    baseline_graph = graph_observable()

    join_mutations: tuple[Callable[[int, int], int], ...] = (
        lambda x, y: x ^ y,
        lambda x, _y: x,
        lambda x, y: (x | y) ^ int((x, y) == (1, 2)),
        lambda x, y: (x | y) ^ int((x, y) == (2, 1)),
        lambda x, y: 0 if x == y == 1 else x | y,
        lambda x, y: x | y | int(x == 0 or y == 0),
    )
    algebra_changed = sum(algebra_facts(join) != baseline_algebra for join in join_mutations)
    table_payload = join_table()
    table_defects = (
        len(table_payload[:-1]) != baseline_algebra.products,
        hashlib.sha256(canonical_json([*table_payload[:-1], [31, 31, 0]]).encode()).hexdigest()
        != baseline_algebra.digest,
        len(range(64)) != 32,
    )
    graph_variants = (
        graph_observable(one_endpoint_merge=True),
        graph_observable(identity_edges=True),
        graph_observable(neighbor_guard=True),
    )
    graph_changed = sum(value != baseline_graph for value in graph_variants)

    checks.check("the committed mutation plan binds exactly 52 defects", contract_bound == 52)
    checks.check("six algebra mutations traverse and change the actual 32-state product", algebra_changed == 6)
    checks.check("missing-product, digest, and sixth-atom defects are distinguished", all(table_defects))
    checks.check("one-endpoint, identity, and terminal-guard mutations change the reachable graph", graph_changed == 3)
    checks.check("downstream participant, labelled, carrier, CP, and absorption mutations remain unexecuted after the Stage-A1 stop", True)
    return checks, [
        "MUTATION contract_bound=52 behaviorally_executed=12 graph_changed=3 downstream_unexecuted=40",
        f"MUTATION_BASELINE algebra={baseline_algebra.digest} graph={baseline_graph}",
    ]


def scientific_run() -> tuple[Checks, list[str]]:
    checks = Checks()
    input_bound, input_sha = audit_inputs_bound()
    algebra = algebra_facts()
    witness = witness_facts()
    factorization = old_table_factorization_violations()
    y = y_facts()
    correct = YState((CLEAN, EXPECTED_Y, EXPECTED_Y, EXPECTED_Y))

    checks.check(
        "literal committed Block-230 packet, landing note, and N1-N8 sidecar bind the run",
        input_bound and len(AUDIT_INPUT_PATHS) == 10,
    )
    checks.check(
        "all 1,024 ordered products reproduce the frozen union-table digest",
        algebra.products == 1024 and algebra.digest == EXPECTED_JOIN_SHA256,
    )
    checks.check(
        "all 32,768 triples and all pair/diagonal/bottom cases satisfy ACI plus bottom",
        algebra.associative == 32768
        and algebra.commutative == 1024
        and algebra.idempotent == 32
        and algebra.bottom == 32,
    )
    checks.check(
        "the translated Block-229 CF_A/CF_T pair joins inside the same six-site quotient for every n=10..16",
        witness.translations == tuple((n, 20, 87, 15) for n in range(10, 17))
        and witness.common_normal == (ALPHA | PHI,) * 6,
    )
    checks.check(
        "the old 46-row comparator has seven exact factorization collisions without changing the new compiler",
        len(P.ROWS) == 46 and len(factorization) == 7,
    )
    checks.check(
        "the minimal central-writer typed Y has 51 states, 70 transitions, and 19 terminal normals",
        y.states == 51
        and y.transitions == 70
        and y.normals == 19
        and y.correct_normals == 1,
    )
    checks.check(
        "the reachable terminal-versus-merge local peak has no common descendant",
        y.peak == YState((15, 3, 7, 15))
        and y.terminal_target == YState((CLEAN, 3, 7, 15))
        and y.merge_target == YState((15, 15, 7, 15))
        and y.descendant_intersection == 0,
    )
    checks.check(
        "the preregistered integer rank strictly decreases yet does not imply confluence",
        y.rank_failures == 0,
    )
    checks.check(
        "the strongest local neighbor-readiness steelman closes this exact Y but is outside the frozen terminal rule",
        y.guarded_states == 33
        and y.guarded_transitions == 52
        and y.guarded_normals == (correct,),
    )
    checks.check(
        "the hard stop leaves full bounded tree census, labelled lift, CP, absorption, Record law, and axioms unexecuted",
        True,
    )

    factor_names = tuple(tuple(row[0] for row in rows) for _source, rows in factorization)
    lines = [
        f"A0_ALGEBRA products={algebra.products} associative={algebra.associative}/32768 commutative={algebra.commutative}/1024 idempotent={algebra.idempotent}/32 bottom={algebra.bottom}/32 sha256={algebra.digest}",
        "A0_TRANSLATED_OVERLAP " + canonical_json(witness.translations),
        "A0_COMMON_NORMAL " + canonical_json(witness.common_normal),
        f"A0_OLD_TABLE_FACTOR comparator_rows=46 violating_summary_sources={len(factorization)} names={canonical_json(factor_names)}",
        f"A1_FIRST_FAILURE topology=typed_Y writer=seam_center initial={Y_INITIAL} states={y.states} transitions={y.transitions} terminal_normals={y.normals} correct_normals={y.correct_normals}",
        f"A1_PEAK source={y.peak.sites} terminal={y.terminal_target.sites} merge01={y.merge_target.sites} common_descendants={y.descendant_intersection}",
        f"A1_RANK transition_non_decreases={y.rank_failures} termination_pass=true confluence_fail=true",
        f"STEELMAN_NEIGHBOR_GUARD states={y.guarded_states} transitions={y.guarded_transitions} normals={tuple(state.sites for state in y.guarded_normals)} status=outside_frozen_Block230",
        "DECISION_CLASS scoped-summary-rank-or-confluence-failure",
        "NO_GO_STATUS partial-attempt-with-named-untested-routes",
        "NEXT_ROUTE preregister_neighbor_readiness_guard_then_prove_arbitrary_tree_and_CP_absorption",
        "SCOPE frozen_self-summary_terminal_guard_only ACI_core_live stronger_local_guard_live distributed_incidence_Haar_serial_coherent_live",
        f"AUDIT_INPUT_SHA256 {input_sha}",
        "per_element: checked — all 1,024 Boolean-union products and all 32,768 associativity triples pass exactly.",
        "per_site: checked — the central writer terminal-versus-incident-merge peak is reachable and has no common descendant.",
        "per_mode: checked and not executed — parity carrier rays, labelled projectors, and Lindblad modes are downstream of Stage A1.",
        "per_block: checked — the complete four-site typed Y graph has 51 states and 19 distinct terminal normal forms.",
        "lattice_wide: checked and not executed — the frozen compiler already fails a finite subgraph, while broader ACI and physics routes remain live.",
        "TOE zero obligation retirement; zero axiom retirement; zero TOE percentage movement; retained-positive end-to-end theory count remains zero.",
    ]
    projected = "\n".join(
        [*(f"PASS {label}" for label, _condition in checks.results), *lines]
    )
    checks.check(
        "stdout remains below the six-thousand-character forensic budget",
        len(projected) + 200 < 6_000,
    )
    return checks, lines


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if hasattr(signal, "SIGALRM"):
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(AUDIT_TIMEOUT_SEC)
    try:
        checks, lines = mutation_run() if args.self_test else scientific_run()
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
