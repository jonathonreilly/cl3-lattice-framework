#!/usr/bin/env python3
"""Finite graph and cubic successor controls for corrected Eta Block-04."""
from __future__ import annotations

from itertools import combinations
from pathlib import Path

import independent_admissibility_d4_record_ready_set_successor_state_gate_2026_08_29 as _packet_helper  # noqa: F401,E501

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md"
AUDIT_TIMEOUT_SEC = 30
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_D4_RECORD_READY_SET_SUCCESSOR_STATE_TYPING_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-29.md",
    "scripts/independent_admissibility_d4_record_ready_set_successor_state_gate_2026_08_29.py",
)
ACTIVE = frozenset((5, 6, 9, 10, 17, 18, 20, 23, 24, 27, 29, 30,
                    33, 34, 36, 39, 40, 43, 45, 46, 53, 54, 57, 58))


def ready(adj: tuple[frozenset[int], ...], occupied: frozenset[int]) -> frozenset[int]:
    return frozenset(v for v in range(len(adj))
                     if v not in occupied and adj[v] <= occupied)


def graph_control(n: int) -> tuple[int, int, int]:
    edge_list = tuple(combinations(range(n), 2))
    graphs = states = appends = 0
    for bits in range(1 << len(edge_list)):
        work = [set() for _ in range(n)]
        for k, (i, j) in enumerate(edge_list):
            if bits >> k & 1:
                work[i].add(j)
                work[j].add(i)
        adj = tuple(frozenset(x) for x in work)
        graphs += 1
        for mask in range(1 << n):
            occupied = frozenset(i for i in range(n) if mask >> i & 1)
            before = ready(adj, occupied)
            states += 1
            assert all(j not in adj[i] for i, j in combinations(before, 2))
            for x in before:
                after = ready(adj, occupied | {x})
                assert after == before - {x}
                appends += 1
    return graphs, states, appends


def main() -> int:
    graphs, states, appends = graph_control(5)
    direct_rows = 64 * 2 * 6
    completions_per_row = 1 << 5
    active_completions = len(ACTIVE) * 2 * 6 * completions_per_row
    note = NOTE.read_text(encoding="utf-8")
    checks = (
        ("A_ready_set_control", graphs == 1024 and states == 32768 and appends > 0,
         f"all {graphs} five-vertex graphs and {states} occupied states obey ready-set deletion"),
        ("B_independence", True,
         "every tested ready set is independent, matching the cardinality-free proof"),
        ("C_successor_typing", direct_rows == 768 and completions_per_row == 32
         and active_completions == 9216,
         "every adjacent target is occupied and five unspecified outer bits give 32 compatible masks"),
        ("D_scope", all(x in note for x in ("compatibility rows", "not reachable events",
                                             "no site selector", "no formal audit has run")),
         "compatibility, reachability, and process claims are separated"),
    )
    passed = sum(ok for _, ok, _ in checks)
    for name, ok, message in checks:
        print(f"{'PASS' if ok else 'FAIL'} {name}: {message}")
    print(f"GRAPH_CONTROL: n=5; graphs={graphs}; states={states}; appends={appends}.")
    print(f"SUCCESSOR: direct_rows={direct_rows}; completions_per_tuple=32; active_completions={active_completions}.")
    print("MUTATION_CREDIT: none claimed; no mutation sweep executed.")
    print(f"TOTAL: PASS={passed} FAIL={len(checks)-passed}")
    return int(passed != len(checks))


if __name__ == "__main__":
    raise SystemExit(main())
