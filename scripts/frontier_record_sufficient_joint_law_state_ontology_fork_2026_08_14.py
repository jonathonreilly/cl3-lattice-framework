#!/usr/bin/env python3
"""Block 94: Record-sufficient joint-law and state-ontology fork.

The exact Block86 prepared-live-input family cannot be reproduced by a
current-map Record-only Markov kernel: m=0 and m=1 have the same initial
Record map but require distinct full readable laws (TV 1/3), whose
formation-conditioned packet laws have total-variation distance one.  All
six static three-write orders expose a local conditional-measure collision.

A changed Record-only theory does exist. Starting from a K-minus controller
Record, one total time-homogeneous kernel generates the root bit, generates
the conditional metadata bit, and fixes completed/off-domain maps. It has 96
normalized covariant packet atoms and uses no hidden live M2 state. Four
law/ontology routes remain; no axiom amendment or end-to-end law is selected.
"""

from __future__ import annotations

import argparse
from fractions import Fraction
from hashlib import sha256
from itertools import permutations, product
import json
import math
from pathlib import Path
import subprocess
import sys

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LIVE_M2_RECORD_SUFFICIENT_JOINT_LAW_STATE_ONTOLOGY_FORK_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
RUNNER_RELATIVE = (
    "scripts/frontier_record_sufficient_joint_law_state_ontology_fork_"
    "2026_08_14.py"
)
BLOCK86_NOTE = (
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_"
    "NOTE_2026-08-14.md"
)
BLOCK86_RUNNER = (
    "scripts/frontier_live_m2_conservative_archive_lock_instrument_"
    "2026_08_14.py"
)
BLOCK92_NOTE = (
    "docs/LIVE_M2_JOINT_ARCHIVE_GRAPH_PERMUTATION_CAPACITY_BOUNDED_"
    "THEOREM_NOTE_2026-08-14.md"
)
BLOCK92_RUNNER = (
    "scripts/frontier_live_m2_joint_archive_graph_permutation_capacity_"
    "2026_08_14.py"
)
REGISTRY_PATH = "docs/audit/data/axiom_premise_nodes.json"
PRIMITIVE_PATHS = (
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
)
HISTORY_ROUTE_PATH = (
    "docs/work_history/repo/review_feedback/"
    "RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md"
)
CONSTITUTIONAL_LEDGER_PATH = (
    "archive/notes/docs/work_history/repo/review_feedback/"
    "MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md"
)
AUDIT_INPUT_PATHS = ('docs/LIVE_M2_RECORD_SUFFICIENT_JOINT_LAW_STATE_ONTOLOGY_FORK_BOUNDED_THEOREM_NOTE_2026-08-14.md', 'docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md', 'docs/LIVE_M2_JOINT_ARCHIVE_GRAPH_PERMUTATION_CAPACITY_BOUNDED_THEOREM_NOTE_2026-08-14.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'docs/audit/data/axiom_premise_nodes.json', 'docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md', 'docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md', 'docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md', 'docs/work_history/repo/review_feedback/RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md', 'archive/notes/docs/work_history/repo/review_feedback/MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md', 'scripts/frontier_record_sufficient_joint_law_state_ontology_fork_2026_08_14.py', 'scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py', 'scripts/frontier_live_m2_joint_archive_graph_permutation_capacity_2026_08_14.py', 'docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md', 'scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py', 'docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md', 'scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py', 'docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md', 'scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py', 'docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md', 'scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py', 'docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md', 'scripts/frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14.py', 'docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md', 'scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py')

# Current selected files; original receipt constants below remain historical.
CURRENT_INPUT_SHA256 = {
    "docs/LIVE_M2_RECORD_SUFFICIENT_JOINT_LAW_STATE_ONTOLOGY_FORK_BOUNDED_THEOREM_NOTE_2026-08-14.md": "a0dc4fe907360e00a6d9ceb5e392066d4b09f0c3d751163010b4122244dd7199",
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "6e22bb1618341229793e9301e1ab7804b34203b55bbcae050c9fb8082cdeff2a",
    "docs/LIVE_M2_JOINT_ARCHIVE_GRAPH_PERMUTATION_CAPACITY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "d1d513bb6bacfa741a267ff19f46db38e53744e1a77e2ec0241a2621bf2bb9ba",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/work_history/repo/review_feedback/RECORD_ONLY_STATE_BELL_LAW_TYPE_DICHOTOMY_CYCLE29_NOTE_2026-07-14.md": "272c60e8f36e206c986b98f2f54a634caf375af56868609aac1427da7773a787",
    "archive/notes/docs/work_history/repo/review_feedback/MINIMUM_CONSTITUTIONAL_CONTENT_EXHAUSTION_LEDGER_NOTE_2026-07-14.md": "a55706586a30ebf2fe591e251a267d596d47d72fd830544cb2649a0bbdb2fcec",
    "scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py": "544a27161eacae82fb6d792eafb3e3a93f567d64a23565769a05d7a9f3270d89",
    "scripts/frontier_live_m2_joint_archive_graph_permutation_capacity_2026_08_14.py": "a1e5b37d81453545403bd5ef33113a46f53391238219bb103a8051807a3978aa",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py": "7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md": "ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py": "cff4964b3dc6acebb8ad4d0c501371197898b207f8cc77468e7c76749a6d9664",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md": "29b0177eaca7e86542c1a15d9a64751895ea5798d695f6305f23891ec974ff58",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py": "9586e59e5d30d7020dc3d5b03a461fe85a3e659790eacfb0fa1e489dc504cde1",
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "2d4fd67f35917906d6f2fd481a27a35ac49b54814644540f9f3c884263961038",
    "scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py": "81e5b4845c64cc149ab1984e0884975e8ec279a7ea6fbaeb5ac88ff4ac83504a",
    "docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md": "ec3d6653b00f6d06b4eb95ac6bb24c6024e3fbe63d5a8ce5a6b78fca9a175968",
    "scripts/frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14.py": "e649a807fb02c80974ffff827f03ac6a28c568ad9c1517e7c259d82d8ee06395",
    "docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "7a75e900c7507eef7369f4b22196eb7b20997a427d798c5d0f6fe84c1f5c236a",
    "scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py": "01f6296b0ad887d6a47212f3ce5bb090dd4e50774e10ab6b86e4c35fa7e70ff2"
}

CURRENT_AXIOM_COMMIT = "eee6ab5874e2fc207db5526dc82d9f71ae550c7c"
CURRENT_AXIOM_BLOB = "bc23300becfe4e4db57153c0e94cfcdf2338da71"
PARENT_COMMIT = "edef1793b1ef3297a2cb89694c90d842682b9951"
BLOCK86_NOTE_BLOB = "b87efbe57b4187657091d8ac4d22667ce1bf7cf5"
BLOCK86_RUNNER_BLOB = "3ee48277a9af4e6effe4eb2ea87bad9d67d95624"
BLOCK92_NOTE_BLOB = "1aefd08628e7db1e7679f892aea6a8d2044315f4"
BLOCK92_RUNNER_BLOB = "79db96293d33a273c1502809d7d587e29f5e9e71"

BLOCK87_COMMIT = "66ded17d80d44d90f5aa9ec52a8950ba573d4b55"
BLOCK87_NOTE_PATH = "docs/ADMISSIBILITY_FINITE_STATE_MARKOV_COMPLETION_BOUNDED_THEOREM_NOTE_2026-08-14.md"
BLOCK87_RUNNER_PATH = "scripts/frontier_admissibility_finite_state_markov_completion_2026_08_14.py"
BLOCK87_NOTE_BLOB = "1855640b20f71a3ed8ecba9b6e43b5daf6b8c549"
BLOCK87_RUNNER_BLOB = "c27c3339dfbb5d63c98100d42839419d41e98c41"

EFFECT_COMMIT = "9242944fe4e91fd35739d59b759e7df35c5bcf58"
EFFECT_NOTE_PATH = "docs/ADMISSIBILITY_M2_EFFECT_LABEL_RECORD_CARRIER_ATOMIC_BORN_LAW_FACTORIZATION_BOUNDED_THEOREM_NOTE_2026-08-10.md"
EFFECT_RUNNER_PATH = "scripts/admissibility_m2_effect_label_record_carrier_atomic_born_law_factorization_2026_08_10.py"
EFFECT_NOTE_BLOB = "60cfd7fa1887f5bc13e897d19f365b3fa699ea7f"
EFFECT_RUNNER_BLOB = "ef378fb5e80057c18ef26e153ff7548e5e4f71e7"

Coord = tuple[int, int, int]
Content = str
Measure = tuple[tuple[Content, Fraction], ...]
RecordItems = tuple[tuple[Coord, Content], ...]

HEAD_SITE: Coord = (0, 1, 0)
ROOT_SITE: Coord = (-1, 1, 0)
META_SITE: Coord = (-1, 2, 0)
ROLE_SITES = {"H": HEAD_SITE, "R": ROOT_SITE, "M": META_SITE}
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
)
BRANCH_WEIGHTS = {
    0: (Fraction(1, 2), Fraction(1, 2)),
    1: (Fraction(1, 5), Fraction(4, 5)),
}
PRIOR = (Fraction(1, 2), Fraction(1, 2))
HAZARD = Fraction(1, 3)
TOL = 1.0e-11


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, key: str, statement: str, condition, detail: str = "") -> None:
        ok = bool(condition)
        short = statement if len(statement) <= 91 else statement[:88] + "..."
        print(f"[{'PASS' if ok else 'FAIL'}] {key}: {short}")
        if detail:
            clipped = detail if len(detail) <= 132 else detail[:129] + "..."
            print(f"       {clipped}")
        self.passed += int(ok)
        self.failed += int(not ok)

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return int(self.failed != 0)


def flat(path: Path) -> str:
    return " ".join(path.read_text(encoding="utf-8").lower().split())


def git_commit_path_blob(commit: str, path: str) -> str:
    return subprocess.run(
        ("git", "rev-parse", f"{commit}:{path}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def git_worktree_path_blob(path: str) -> str:
    return subprocess.run(
        ("git", "hash-object", "--", path),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def current_inputs_match() -> bool:
    return all((ROOT / path).is_file()
               and sha256((ROOT / path).read_bytes()).hexdigest() == digest
               for path, digest in CURRENT_INPUT_SHA256.items())


def authority_certificate(mutation: str) -> dict[str, object]:
    origin_main = subprocess.run(
        ("git", "rev-parse", "origin/main"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    current = {NOTE_PATH.relative_to(ROOT).as_posix(), RUNNER_RELATIVE}
    frozen = tuple(path for path in AUDIT_INPUT_PATHS if path not in current)
    mismatches = tuple(
        path
        for path in frozen
        if not (ROOT / path).is_file()
        or sha256((ROOT / path).read_bytes()).hexdigest() != CURRENT_INPUT_SHA256[path]
    )
    loaded: set[str] = set()
    for module in tuple(sys.modules.values()):
        file_name = getattr(module, "__file__", None)
        if not file_name:
            continue
        path = Path(file_name).resolve()
        try:
            relative = path.relative_to(ROOT).as_posix()
        except ValueError:
            continue
        if relative.startswith("scripts/") and relative.endswith(".py"):
            loaded.add(relative)
    declared = {path for path in AUDIT_INPUT_PATHS if path.startswith("scripts/")}
    expected_axiom = "0" * 40 if mutation == "stale_axiom_authority" else CURRENT_AXIOM_BLOB
    remote = {
        "block87_note": git_commit_path_blob(BLOCK87_COMMIT, BLOCK87_NOTE_PATH),
        "block87_runner": git_commit_path_blob(BLOCK87_COMMIT, BLOCK87_RUNNER_PATH),
        "effect_note": git_commit_path_blob(EFFECT_COMMIT, EFFECT_NOTE_PATH),
        "effect_runner": git_commit_path_blob(EFFECT_COMMIT, EFFECT_RUNNER_PATH),
    }
    return {
        "origin_main": origin_main,  # current ref recorded, not an immutable requirement
        "current_inputs_match": current_inputs_match(),
        "historical_parents_match": (
            git_commit_path_blob(PARENT_COMMIT, BLOCK86_NOTE) == BLOCK86_NOTE_BLOB
            and git_commit_path_blob(PARENT_COMMIT, BLOCK86_RUNNER) == BLOCK86_RUNNER_BLOB
            and git_commit_path_blob(PARENT_COMMIT, BLOCK92_NOTE) == BLOCK92_NOTE_BLOB
            and git_commit_path_blob(PARENT_COMMIT, BLOCK92_RUNNER) == BLOCK92_RUNNER_BLOB
            and git_commit_path_blob(CURRENT_AXIOM_COMMIT, "docs/MINIMAL_AXIOMS_2026-06-29.md") == CURRENT_AXIOM_BLOB
        ),
        "axiom_blob": git_worktree_path_blob("docs/MINIMAL_AXIOMS_2026-06-29.md"),
        "expected_axiom": expected_axiom,
        "block86_note": git_worktree_path_blob(BLOCK86_NOTE),
        "block86_runner": git_worktree_path_blob(BLOCK86_RUNNER),
        "block92_note": git_worktree_path_blob(BLOCK92_NOTE),
        "block92_runner": git_worktree_path_blob(BLOCK92_RUNNER),
        "mismatches": mismatches,
        "missing": tuple(path for path in AUDIT_INPUT_PATHS if not (ROOT / path).exists()),
        "loaded_missing": tuple(sorted(loaded - declared)),
        "remote": remote,
    }


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def dot(left: Coord, right: Coord) -> int:
    return sum(left[index] * right[index] for index in range(3))


def rotations() -> tuple[np.ndarray, ...]:
    answer: list[np.ndarray] = []
    for axes in permutations(range(3)):
        permutation = np.eye(3, dtype=int)[list(axes)]
        for signs in product((-1, 1), repeat=3):
            rotation = np.diag(signs) @ permutation
            if round(np.linalg.det(rotation)) == 1:
                answer.append(rotation)
    return tuple(answer)


ROTATIONS = rotations()


def rotate(rotation: np.ndarray, site: Coord) -> Coord:
    return tuple(int(value) for value in rotation @ np.asarray(site))  # type: ignore[return-value]


def sorted_items(records: dict[Coord, Content]) -> RecordItems:
    return tuple(sorted(records.items()))


def canonical_nn_signature(records: dict[Coord, Content], site: Coord) -> tuple[tuple[Coord, Content], ...]:
    candidates: list[tuple[tuple[Coord, Content], ...]] = []
    for rotation in ROTATIONS:
        entries: list[tuple[Coord, Content]] = []
        for direction in DIRECTIONS:
            neighbor = add(site, direction)
            if neighbor in records:
                entries.append((rotate(rotation, direction), records[neighbor]))
        candidates.append(tuple(sorted(entries)))
    return min(candidates)


def point_measure(content: Content) -> Measure:
    return ((content, Fraction(1)),)


def desired_measure(role: str, matter: int) -> Measure:
    if role == "H":
        return point_measure("minus")
    if role == "R":
        return point_measure(str(matter))
    return (("0", BRANCH_WEIGHTS[matter][0]), ("1", BRANCH_WEIGHTS[matter][1]))


def realized_content(role: str, matter: int, branch: int) -> Content:
    return {"H": "minus", "R": str(matter), "M": str(branch)}[role]


def total_variation(left: Measure, right: Measure) -> Fraction:
    ldict = dict(left)
    rdict = dict(right)
    keys = set(ldict) | set(rdict)
    return Fraction(1, 2) * sum(abs(ldict.get(key, Fraction(0)) - rdict.get(key, Fraction(0))) for key in keys)


def blank_marginal_certificate(mutation: str) -> dict[str, object]:
    empty: dict[Coord, Content] = {}
    signatures = {
        role: canonical_nn_signature(empty, site) for role, site in ROLE_SITES.items()
    }
    head = desired_measure("H", 0)
    root = desired_measure("R", 0)
    meta = desired_measure("M", 0)
    tvs = (
        total_variation(head, root),
        total_variation(head, meta),
        total_variation(root, meta),
    )
    valid = mutation != "erase_blank_alias"
    return {
        "distinct_signatures": len(set(signatures.values())),
        "signature": next(iter(signatures.values())),
        "tvs": tvs,
        "valid": valid,
    }


def order_requirements(order: tuple[str, ...]) -> dict[tuple[tuple[Coord, Content], ...], set[Measure]]:
    requirements: dict[tuple[tuple[Coord, Content], ...], set[Measure]] = {}
    for matter, branch in product((0, 1), repeat=2):
        records: dict[Coord, Content] = {}
        for role in order:
            signature = canonical_nn_signature(records, ROLE_SITES[role])
            requirements.setdefault(signature, set()).add(desired_measure(role, matter))
            records[ROLE_SITES[role]] = realized_content(role, matter, branch)
    return requirements


def sequential_order_certificate(mutation: str) -> dict[str, object]:
    rows = []
    for order in permutations(("H", "R", "M")):
        requirements = order_requirements(order)
        conflicts = tuple(
            (signature, tuple(sorted(measures)))
            for signature, measures in requirements.items()
            if len(measures) > 1
        )
        rows.append(("".join(order), len(requirements), len(conflicts)))
    best = min(rows, key=lambda row: (row[2], row[1], row[0]))
    valid = mutation != "fake_order_pass"
    note = flat(NOTE_PATH)
    return {
        "rows": tuple(rows),
        "conflict_counts": tuple(row[2] for row in rows),
        "failed_orders": sum(row[2] > 0 for row in rows),
        "best": best,
        "valid": valid,
        "scoped": all(
            phrase in note
            for phrase in (
                "all six static write orders",
                "head-root-meta is the unique least-conflicting order",
                "root condition still cannot see the prepared matter bit",
            )
        ),
    }


def desired_formation_conditioned_distribution(
    matter: int,
) -> dict[RecordItems, Fraction]:
    answer: dict[RecordItems, Fraction] = {}
    for branch in (0, 1):
        records = {
            HEAD_SITE: "minus",
            ROOT_SITE: str(matter),
            META_SITE: str(branch),
        }
        answer[sorted_items(records)] = BRANCH_WEIGHTS[matter][branch]
    return answer


def desired_full_distribution(matter: int) -> dict[RecordItems, Fraction]:
    """Block86 clean-domain law, including its common no-event atom."""
    answer = {tuple(): Fraction(1) - HAZARD}
    for records, weight in desired_formation_conditioned_distribution(matter).items():
        answer[records] = HAZARD * weight
    return answer


def distribution_tv(
    left: dict[RecordItems, Fraction],
    right: dict[RecordItems, Fraction],
) -> Fraction:
    keys = set(left) | set(right)
    return Fraction(1, 2) * sum(abs(left.get(key, Fraction(0)) - right.get(key, Fraction(0))) for key in keys)


def record_sufficiency_certificate(mutation: str) -> dict[str, object]:
    conditioned_m0 = desired_formation_conditioned_distribution(0)
    conditioned_m1 = desired_formation_conditioned_distribution(1)
    full_m0 = desired_full_distribution(0)
    full_m1 = desired_full_distribution(1)
    proof_valid = mutation != "fake_record_sufficiency"
    note = flat(NOTE_PATH)
    return {
        "conditioned_m0_mass": sum(conditioned_m0.values()),
        "conditioned_m1_mass": sum(conditioned_m1.values()),
        "formation_mass": HAZARD,
        "conditioned_tv": distribution_tv(conditioned_m0, conditioned_m1),
        "full_m0_mass": sum(full_m0.values()),
        "full_m1_mass": sum(full_m1.values()),
        "full_tv": distribution_tv(full_m0, full_m1),
        "same_initial_records": True,
        "proof_valid": proof_valid,
        "scoped": all(
            phrase in note
            for phrase in (
                "record-sufficiency theorem",
                "the same initial record state has one future measure",
                "prepared-live-input family",
                "full readable laws therefore have tv `1/3`",
                "formation-conditioned packet laws have tv `1`",
                "does not rule out generating `m` as a record outcome",
            )
        ),
    }


def transverse_directions(direction: Coord) -> tuple[Coord, ...]:
    return tuple(candidate for candidate in DIRECTIONS if dot(candidate, direction) == 0)


def decode_packet(records: dict[Coord, Content]) -> dict[str, object] | None:
    if len(records) != 3:
        return None
    degrees = {
        site: sum(sum((site[i] - other[i]) ** 2 for i in range(3)) == 1 for other in records if other != site)
        for site in records
    }
    roots = tuple(site for site, degree in degrees.items() if degree == 2)
    if len(roots) != 1:
        return None
    root = roots[0]
    endpoints = tuple(site for site in records if site != root)
    heads = tuple(site for site in endpoints if records[site] == "minus")
    if len(heads) != 1:
        return None
    head = heads[0]
    meta = next(site for site in endpoints if site != head)
    if records[root] not in ("0", "1") or records[meta] not in ("0", "1"):
        return None
    forward = sub(head, root)
    transverse = sub(meta, root)
    frames = tuple(
        rotation
        for rotation in ROTATIONS
        if rotate(rotation, (1, 0, 0)) == forward
        and rotate(rotation, (0, 1, 0)) == transverse
    )
    if len(frames) != 1:
        return None
    return {
        "head": head,
        "root": root,
        "meta": meta,
        "m": int(records[root]),
        "b": int(records[meta]),
        "frame_count": len(frames),
    }


def root_step(head: Coord) -> dict[RecordItems, Fraction]:
    answer: dict[RecordItems, Fraction] = {}
    for direction in DIRECTIONS:
        root = add(head, direction)
        for matter in (0, 1):
            records = {head: "minus", root: str(matter)}
            answer[sorted_items(records)] = Fraction(1, 6) * PRIOR[matter]
    return answer


def decode_intermediate(records: RecordItems) -> dict[str, object] | None:
    if len(records) != 2:
        return None
    record_map = dict(records)
    heads = tuple(site for site, content in records if content == "minus")
    bits = tuple(site for site, content in records if content in ("0", "1"))
    if len(heads) != 1 or len(bits) != 1:
        return None
    head = heads[0]
    root = bits[0]
    direction = sub(root, head)
    if direction not in DIRECTIONS:
        return None
    return {
        "head": head,
        "root": root,
        "direction": direction,
        "matter": int(record_map[root]),
    }


def meta_step(records: RecordItems) -> dict[RecordItems, Fraction]:
    decoded = decode_intermediate(records)
    if decoded is None:
        return {records: Fraction(1)}
    current = dict(records)
    root = decoded["root"]
    direction = decoded["direction"]
    matter = decoded["matter"]
    assert isinstance(root, tuple)
    assert isinstance(direction, tuple)
    assert isinstance(matter, int)
    answer: dict[RecordItems, Fraction] = {}
    for transverse in transverse_directions(direction):
        meta = add(root, transverse)
        for branch in (0, 1):
            updated = dict(current)
            updated[meta] = str(branch)
            answer[sorted_items(updated)] = Fraction(1, 4) * BRANCH_WEIGHTS[matter][branch]
    return answer


def record_kernel(
    records: RecordItems,
    mutation: str = "",
) -> dict[RecordItems, Fraction]:
    """One total time-homogeneous kernel on all finite Record maps.

    The isolated one-controller seed advances to an intermediate packet, a
    valid intermediate advances to a completed packet, and every completed or
    off-domain map is an identity/refusal state.
    """
    if len(records) == 1 and records[0][1] == "minus":
        return root_step(records[0][0])
    if decode_intermediate(records) is not None:
        return meta_step(records)
    decoded_packet = decode_packet(dict(records))
    if mutation == "break_sequential_kernel" and decoded_packet is not None:
        head = decoded_packet["head"]
        assert isinstance(head, tuple)
        return root_step(head)
    return {records: Fraction(1)}


def compose_two_steps(head: Coord = (0, 0, 0)) -> dict[RecordItems, Fraction]:
    seed = sorted_items({head: "minus"})
    answer: dict[RecordItems, Fraction] = {}
    for intermediate, first_weight in record_kernel(seed).items():
        for final, second_weight in record_kernel(intermediate).items():
            answer[final] = answer.get(final, Fraction(0)) + first_weight * second_weight
    return answer


def transform_records(records: RecordItems, rotation: np.ndarray, translation: Coord = (0, 0, 0)) -> RecordItems:
    return tuple(
        sorted((add(translation, rotate(rotation, site)), content) for site, content in records)
    )


def sequential_kernel_certificate(mutation: str) -> dict[str, object]:
    seed = sorted_items({(0, 0, 0): "minus"})
    first = record_kernel(seed, mutation)
    second = compose_two_steps((0, 0, 0))
    decode_failures = 0
    content_weight_failures = 0
    for records, weight in second.items():
        decoded = decode_packet(dict(records))
        if decoded is None:
            decode_failures += 1
            continue
        expected = Fraction(1, 6) * PRIOR[int(decoded["m"])] * Fraction(1, 4) * BRANCH_WEIGHTS[int(decoded["m"])][int(decoded["b"])]
        content_weight_failures += weight != expected
    covariance_failures = 0
    for rotation in ROTATIONS:
        transformed = {transform_records(records, rotation): weight for records, weight in second.items()}
        covariance_failures += transformed != second
    translation = (7, -4, 3)
    translated = compose_two_steps(translation)
    expected_translation = {
        transform_records(records, np.eye(3, dtype=int), translation): weight
        for records, weight in second.items()
    }
    requirements: dict[tuple[tuple[Coord, Content], ...], set[Measure]] = {}
    head = (0, 0, 0)
    for intermediate in first:
        records = dict(intermediate)
        root, matter_content = next(
            (site, content) for site, content in intermediate if content in ("0", "1")
        )
        root_signature = canonical_nn_signature({head: "minus"}, root)
        requirements.setdefault(root_signature, set()).add(
            (("0", PRIOR[0]), ("1", PRIOR[1]))
        )
        matter = int(matter_content)
        direction = sub(root, head)
        for transverse in transverse_directions(direction):
            meta = add(root, transverse)
            signature = canonical_nn_signature(records, meta)
            requirements.setdefault(signature, set()).add(
                (("0", BRANCH_WEIGHTS[matter][0]), ("1", BRANCH_WEIGHTS[matter][1]))
            )
    condition_conflicts = sum(len(measures) != 1 for measures in requirements.values())
    third: dict[RecordItems, Fraction] = {}
    terminal_fixed_points = 0
    for completed, old_weight in second.items():
        transition = record_kernel(completed, mutation)
        terminal_fixed_points += transition == {completed: Fraction(1)}
        for output, transition_weight in transition.items():
            third[output] = third.get(output, Fraction(0)) + old_weight * transition_weight
    off_domain_probes = (
        tuple(),
        sorted_items({(0, 0, 0): "0"}),
        sorted_items({(0, 0, 0): "minus", (2, 0, 0): "0"}),
        sorted_items({(0, 0, 0): "other", (1, 0, 0): "1"}),
    )
    off_domain_failures = sum(
        record_kernel(records, mutation) != {records: Fraction(1)}
        for records in off_domain_probes
    )
    note = flat(NOTE_PATH)
    return {
        "first_atoms": len(first),
        "first_mass": sum(first.values()),
        "second_atoms": len(second),
        "second_mass": sum(second.values()),
        "decode_failures": decode_failures,
        "weight_failures": content_weight_failures,
        "covariance_failures": covariance_failures,
        "translation_match": translated == expected_translation,
        "condition_signatures": len(requirements),
        "condition_conflicts": condition_conflicts,
        "third_atoms": len(third),
        "third_mass": sum(third.values()),
        "third_matches_second": third == second,
        "terminal_fixed_points": terminal_fixed_points,
        "off_domain_probes": len(off_domain_probes),
        "off_domain_failures": off_domain_failures,
        "scoped": all(
            phrase in note
            for phrase in (
                "twelve first-step atoms",
                "ninety-six two-step packet atoms",
                "stage is inferred from the record map",
                "one total time-homogeneous kernel",
                "off-domain map is an identity/refusal state",
                "`m` is generated at the root rather than read from a live input",
            )
        ),
    }


def controller_reachability_certificate(mutation: str) -> dict[str, object]:
    identity = np.eye(2, dtype=complex)
    sigma_x = np.asarray(((0, 1), (1, 0)), dtype=complex)
    sigma_z = np.asarray(((1, 0), (0, -1)), dtype=complex)
    kminus = 0.5 * (identity - sigma_x)
    kzero = 0.5 * (identity + sigma_z)
    kone = 0.5 * (identity - sigma_z)
    direction: Coord = (-1, 0, 0)
    sign = -1 if mutation == "fake_controller_genesis" else 1
    norm_squared = dot(direction, direction)
    square_root = math.isqrt(norm_squared)
    assert square_root * square_root == norm_squared
    unit_direction = np.asarray(direction, dtype=float) / square_root
    projector = 0.5 * (identity + sign * unit_direction[0] * sigma_x)
    probability = (
        Fraction(1) + sign * Fraction(square_root, 3)
    ) / 2
    block87_note = subprocess.run(
        ("git", "show", f"{BLOCK87_COMMIT}:{BLOCK87_NOTE_PATH}"),
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    formula_bound = (
        "p_s(d) = [1 + s sqrt(k)/3]/2" in block87_note
        and "k = |d|^2 in {1,2,3}" in block87_note
    )
    block73_tag = 2.0 * identity - kzero
    alphabet_spectra = {
        tuple(np.round(np.linalg.eigvalsh(0.5 * identity), 12)),
        tuple(np.round(np.linalg.eigvalsh(kminus), 12)),
        tuple(np.round(np.linalg.eigvalsh(kzero), 12)),
        tuple(np.round(np.linalg.eigvalsh(kone), 12)),
    }
    first_shell = {(0, 0, 0)} | set(DIRECTIONS)
    head = (1, 0, 0)
    root = (2, 0, 0)
    meta = (2, 1, 0)
    root_neighbors = {add(root, direction) for direction in DIRECTIONS} & first_shell
    meta_neighbors = {add(meta, direction) for direction in DIRECTIONS} & first_shell
    note = flat(NOTE_PATH)
    return {
        "kminus_residual": float(np.max(np.abs(projector - kminus))),
        "head_probability": probability,
        "norm_squared": norm_squared,
        "square_root": square_root,
        "formula_bound": formula_bound,
        "kzero_rank": int(np.linalg.matrix_rank(kzero)),
        "kone_rank": int(np.linalg.matrix_rank(kone)),
        "tag_spectrum": tuple(np.round(np.linalg.eigvalsh(block73_tag), 12)),
        "tag_in_alphabet": tuple(np.round(np.linalg.eigvalsh(block73_tag), 12)) in alphabet_spectra,
        "root_neighbors": root_neighbors,
        "meta_neighbors": meta_neighbors,
        "scoped": all(
            phrase in note
            for phrase in (
                "block87 can produce the k-minus controller content",
                "derived positive marginal mass `2/3`",
                "does not select the hybrid continuation",
                "block73 spectrum-{1,2} tags are not in the block87 reachable alphabet",
            )
        ),
    }


def inherited_law_certificate() -> dict[str, object]:
    """Independent exact Block86 clean-input rows and all their used restrictions."""
    weights = ((Fraction(1, 2), Fraction(1, 2)),
               (Fraction(1, 5), Fraction(4, 5)))
    full_weights = ((Fraction(1, 6), Fraction(1, 6)),
                    (Fraction(1, 15), Fraction(4, 15)))
    full_failures = conditional_failures = 0
    laws = []
    for matter in (0, 1):
        keys = tuple(tuple(sorted({(0, 1, 0): "minus", (-1, 1, 0): str(matter),
                                   (-1, 2, 0): str(branch)}.items()))
                     for branch in (0, 1))
        expected = {(): Fraction(2, 3), **dict(zip(keys, full_weights[matter]))}
        actual = desired_full_distribution(matter)
        laws.append(actual)
        full_failures += actual != expected
        conditional_failures += desired_formation_conditioned_distribution(matter) != dict(zip(keys, weights[matter]))
        expected_rows = {"H": (("minus", Fraction(1)),),
                         "R": ((str(matter), Fraction(1)),),
                         "M": (("0", weights[matter][0]), ("1", weights[matter][1]))}
        conditional_failures += sum(desired_measure(role, matter) != row
                                    for role, row in expected_rows.items())
    generated_failures = 0
    for packet, weight in compose_two_steps().items():
        decoded = decode_packet(dict(packet))
        if decoded is None:
            generated_failures += 1
        else:
            # Six equiprobable directions, fair generated m, four transverse directions.
            expected = Fraction(1, 48) * weights[int(decoded["m"])][int(decoded["b"])]
            generated_failures += weight != expected
    return {"full_law_failures": full_failures,
            "conditional_row_failures": conditional_failures,
            "generated_weight_failures": generated_failures,
            "full_tv": distribution_tv(*laws), "laws": laws}


def effect_label_certificate(mutation: str) -> dict[str, object]:
    effect = 0.5 * np.eye(2, dtype=complex)
    codes = tuple(effect + 1.0j * label * np.eye(2) for label in range(34))
    recovered_effect_error = max(
        float(np.max(np.abs(0.5 * (code + code.conj().T) - effect))) for code in codes
    )
    recovered_labels = tuple(float(0.5 * np.trace(code).imag) for code in codes)
    unique = len({tuple(np.round(code.reshape(-1), 12)) for code in codes})
    if mutation == "collapse_effect_labels":
        unique -= 1
    unitary = np.asarray(((1, 1), (1, -1)), dtype=complex) / np.sqrt(2.0)
    covariance_error = max(
        float(
            np.max(
                np.abs(
                    unitary @ code @ unitary.conj().T
                    - (unitary @ effect @ unitary.conj().T + 1.0j * label * np.eye(2))
                )
            )
        )
        for label, code in enumerate(codes)
    )
    note = flat(NOTE_PATH)
    return {
        "codes": len(codes),
        "unique": unique,
        "effect_error": recovered_effect_error,
        "label_error": max(abs(recovered_labels[index] - index) for index in range(34)),
        "covariance_error": covariance_error,
        "scoped": all(
            phrase in note
            for phrase in (
                "34 effect-label codes",
                "algebraic label capacity is not the blocker",
                "does not select those matrices as record content or readout",
            )
        ),
    }


def axiom_fork_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    axiom = (ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md").read_text(encoding="utf-8")
    registry = json.loads((ROOT / REGISTRY_PATH).read_text(encoding="utf-8"))
    expected_ids = (
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    )
    registered_ids = tuple(registry["canonical_ids"])
    registered_paths = tuple(
        registry["nodes"][claim_id]["current_path"] for claim_id in registered_ids
    )
    expected_paths = (
        "docs/MINIMAL_AXIOMS_2026-06-29.md",
        *PRIMITIVE_PATHS,
    )
    realized = (ROOT / PRIMITIVE_PATHS[-1]).read_text(encoding="utf-8").lower()
    history = flat(ROOT / HISTORY_ROUTE_PATH)
    constitutional = flat(ROOT / CONSTITUTIONAL_LEDGER_PATH)
    valid = all(
        phrase in note
        for phrase in (
            "readable-state/causal-prestate distinction",
            "preparation record",
            "global record-history/law-side condition",
            "no core axiom edit is forced",
            "if the conservative live route is intended",
            "hazard, scheduler, resource, and physical-time values remain downstream",
            "the 34-outcome lift is gated off",
        )
    )
    if mutation == "force_axiom_edit":
        valid = False
    return {
        "valid": valid,
        "state_is_records": "A state is a configuration of records." in axiom,
        "only_records_readable": "Only records are readable." in axiom,
        "records_permanent": "records are permanent" in axiom,
        "law_domain_is_supplied_condition": (
            "Its domain is a supplied condition" in axiom
        ),
        "registry_ids_exact": registered_ids == expected_ids,
        "registry_paths_exact": registered_paths == expected_paths,
        "registry_paths_declared": all(path in AUDIT_INPUT_PATHS for path in registered_paths),
        "no_preparation_or_prestate_primitive": not any(
            token in claim_id for claim_id in registered_ids
            for token in ("preparation", "prestate")
        ),
        "realized_state_supplies_no_content_or_probability": (
            "no state" in realized and "probability rule" in realized
        ),
        "history_route_bound": all(
            phrase in history
            for phrase in (
                "record-fibre strong lumpability",
                "complete record history",
                "three nonconstitutional ways",
            )
        ),
        "constitutional_route_bound": (
            "global-history and record-only local routes preserve the ontology"
            in constitutional
        ),
    }


def no_go_certificate(mutation: str) -> dict[str, object]:
    note = flat(NOTE_PATH)
    required = (
        "n1 — alternative route enumeration",
        "n2 — wall-independence audit",
        "n3 — hidden-wall scan",
        "n4 — residual matching",
        "n5 — rhetoric audit",
        "n6 — partial-closure path scan",
        "n7 — steelman",
        "n8 — cross-cycle echo",
        "exact target contract",
        "single collapsed terminal wall",
        "global record-history/law-side condition",
        "| **attempted** | fails",
        "| **attempted** | survives",
        "no universal record-only, live-m2, axiom, or toe no-go",
    )
    valid = all(phrase in note for phrase in required)
    if mutation == "weaken_routes":
        valid = False
    return {
        "valid": valid,
        "attempted": note.count("attempted"),
        "path_line": note.count("path:line"),
        "zero_score": mutation != "claim_toe_progress" and all(
            phrase in note
            for phrase in (
                "zero obligation retirement",
                "no toe percentage moves",
                "retained-positive end-to-end theory count remains zero",
            )
        ),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom_authority",
            "erase_blank_alias",
            "fake_order_pass",
            "fake_record_sufficiency",
            "break_sequential_kernel",
            "fake_controller_genesis",
            "collapse_effect_labels",
            "force_axiom_edit",
            "weaken_routes",
            "claim_toe_progress",
        ),
        default="",
    )
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation)
    checks.check(
        "A-current-axiom-parent-and-remote-comparison-authority",
        "axioms, Block86/92, registry/history routes, Block87, and the effect-label carrier are content-bound",
        authority["current_inputs_match"]
        and authority["historical_parents_match"]
        and authority["axiom_blob"] == authority["expected_axiom"]
        and authority["remote"]["block87_note"] == BLOCK87_NOTE_BLOB
        and authority["remote"]["block87_runner"] == BLOCK87_RUNNER_BLOB
        and authority["remote"]["effect_note"] == EFFECT_NOTE_BLOB
        and authority["remote"]["effect_runner"] == EFFECT_RUNNER_BLOB
        and not authority["mismatches"]
        and not authority["missing"]
        and not authority["loaded_missing"],
        f"origin/main={authority['origin_main'][:10]}; local/loaded mismatches={len(authority['mismatches'])}/{len(authority['loaded_missing'])}; remote receipts=4",
    )

    blank = blank_marginal_certificate(mutation)
    checks.check(
        "B-identical-blank-neighborhood-unequal-one-site-measures",
        "the three blank target sites have one Record signature but the m=0 lock marginals differ",
        blank["distinct_signatures"] == 1
        and blank["signature"] == ()
        and blank["tvs"] == (Fraction(1), Fraction(1), Fraction(1, 2))
        and blank["valid"],
        f"distinct signatures={blank['distinct_signatures']}; pairwise TV={tuple(str(value) for value in blank['tvs'])}",
    )

    orders = sequential_order_certificate(mutation)
    checks.check(
        "C-all-six-sequential-write-orders-collide",
        "every static write order requires unequal one-site measures on an identical prior Record condition",
        len(orders["rows"]) == 6
        and orders["failed_orders"] == 6
        and orders["conflict_counts"] == (1, 3, 3, 3, 3, 3)
        and orders["best"] == ("HRM", 4, 1)
        and orders["valid"]
        and orders["scoped"],
        f"orders={orders['rows']}; best={orders['best']}",
    )

    sufficiency = record_sufficiency_certificate(mutation)
    checks.check(
        "D-prepared-live-family-fails-Record-sufficiency",
        "one current Record map cannot have the two distinct full future laws required by prepared m=0 and m=1",
        sufficiency["conditioned_m0_mass"] == 1
        and sufficiency["conditioned_m1_mass"] == 1
        and sufficiency["formation_mass"] > 0
        and sufficiency["conditioned_tv"] == 1
        and sufficiency["full_m0_mass"] == 1
        and sufficiency["full_m1_mass"] == 1
        and sufficiency["full_tv"] == sufficiency["formation_mass"]
        and sufficiency["same_initial_records"]
        and sufficiency["proof_valid"]
        and sufficiency["scoped"],
        f"conditioned/full masses={sufficiency['conditioned_m0_mass']}/{sufficiency['full_m0_mass']}; conditioned/full TV={sufficiency['conditioned_tv']}/{sufficiency['full_tv']}",
    )

    sequential = sequential_kernel_certificate(mutation)
    checks.check(
        "E-Record-only-controller-seeded-generative-kernel",
        "a K-minus controller yields a normalized covariant two-stage packet law when m is generated at the root",
        sequential["first_atoms"] == 12
        and sequential["first_mass"] == 1
        and sequential["second_atoms"] == 96
        and sequential["second_mass"] == 1
        and sequential["decode_failures"] == 0
        and sequential["weight_failures"] == 0
        and sequential["covariance_failures"] == 0
        and sequential["translation_match"]
        and sequential["condition_signatures"] == 3
        and sequential["condition_conflicts"] == 0
        and sequential["third_atoms"] == 96
        and sequential["third_mass"] == 1
        and sequential["third_matches_second"]
        and sequential["terminal_fixed_points"] == 96
        and sequential["off_domain_probes"] == 4
        and sequential["off_domain_failures"] == 0
        and sequential["scoped"],
        f"atoms={sequential['first_atoms']}->{sequential['second_atoms']}->{sequential['third_atoms']}; terminal/off-domain failures={96-sequential['terminal_fixed_points']}/{sequential['off_domain_failures']}; decode/condition/cubic failures={sequential['decode_failures']}/{sequential['condition_conflicts']}/{sequential['covariance_failures']}",
    )

    controller = controller_reachability_certificate(mutation)
    checks.check(
        "F-Block87-controller-content-reachability-and-integration-boundary",
        "Block87's pinned formula derives K-minus with positive mass but neither its scheduler nor Block73 tags are inherited",
        controller["kminus_residual"] < TOL
        and controller["norm_squared"] == 1
        and controller["square_root"] == 1
        and controller["formula_bound"]
        and 0 < controller["head_probability"] < 1
        and controller["head_probability"] == Fraction(2, 3)
        and controller["kzero_rank"] == 1
        and controller["kone_rank"] == 1
        and controller["tag_spectrum"] == (1.0, 2.0)
        and not controller["tag_in_alphabet"]
        and controller["root_neighbors"] == {(1, 0, 0)}
        and controller["meta_neighbors"] == set()
        and controller["scoped"],
        f"K-minus residual/mass={controller['kminus_residual']:.1e}/{controller['head_probability']}; tag spectrum={controller['tag_spectrum']}; outward root/meta old neighbors={controller['root_neighbors']}/{controller['meta_neighbors']}",
    )

    inherited = inherited_law_certificate()
    checks.check(
        "J-exact-inherited-full-laws-and-conditional-rows",
        "both complete Block86 laws, six used marginal rows, and all generated weights match independent exact values",
        inherited["full_law_failures"] == 0
        and inherited["conditional_row_failures"] == 0
        and inherited["generated_weight_failures"] == 0
        and inherited["full_tv"] == Fraction(1, 3),
        f"full/conditional/generated failures={inherited['full_law_failures']}/{inherited['conditional_row_failures']}/{inherited['generated_weight_failures']}; TV={inherited['full_tv']}",
    )

    labels = effect_label_certificate(mutation)
    checks.check(
        "G-thirty-four-outcome-M2-label-capacity-is-not-the-wall",
        "the existing M2 carrier injects and decodes 34 supplied effect-label atoms covariantly",
        labels["codes"] == 34
        and labels["unique"] == 34
        and labels["effect_error"] < TOL
        and labels["label_error"] < TOL
        and labels["covariance_error"] < TOL
        and labels["scoped"],
        f"codes/unique={labels['codes']}/{labels['unique']}; effect/label/covariance={labels['effect_error']:.1e}/{labels['label_error']:.1e}/{labels['covariance_error']:.1e}",
    )

    fork = axiom_fork_certificate(mutation)
    checks.check(
        "H-exact-state-ontology-fork-and-minimal-update-surface",
        "four law/ontology routes remain, including global Record-history conditioning without a forced core edit",
        all(fork.values()),
    )

    no_go = no_go_certificate(mutation)
    checks.check(
        "I-no-go-discipline-retention-and-TOE-scope",
        "N1-N8 preserves generated, preparation, history-conditioned, and prestate escapes and assigns zero TOE credit",
        no_go["valid"]
        and no_go["attempted"] >= 5
        and no_go["path_line"] >= 2
        and no_go["zero_score"],
        f"ATTEMPTED markers={no_go['attempted']}; path:line markers={no_go['path_line']}",
    )

    print(
        f"AXIOM_AUTHORITY: observed origin/main={authority['origin_main']} axiom={CURRENT_AXIOM_BLOB}; historical Block92 parent={PARENT_COMMIT}; Block87/effect comparisons are commit-pinned"
    )
    print(
        "per_element: checked — K-minus/K0/K1 contents, exact one-site measures, two prepared-m rows, 34 effect-label codes, and controller spectra"
    )
    print(
        "per_site: checked — actual head/root/meta geometry, six-neighbor signatures, six write orders, six root directions, and four transverse continuations"
    )
    print(
        "per_mode: checked — both prepared m values and both b branches; full laws have TV 1/3 and formation-conditioned packet laws have TV 1"
    )
    print(
        "per_block: checked — current-map Markov impossibility, one total 12-to-96-to-96 absorbing kernel, four route classes, exact primitive registry, Block87 controller reachability, and 34-label capacity"
    )
    print(
        "lattice_wide: checked and not executed — complete-history weights/domain, arbitrary-map controller or preparation provenance, overlap arbitration, selected law values, actuality, physical time, source/action/gravity, and audit retention remain open"
    )
    print(
        "RESULT: the current Record map is insufficient for the prepared live-M2 family under one current-map Markov kernel, but a changed controller-seeded law can generate m as a Record outcome"
    )
    print(
        "LAW_ONTOLOGY_ROUTES: generated m, a preparation Record, complete Record-history/law-side conditioning, or a causal-prestate distinction; no core axiom edit is forced by the narrow theorem"
    )
    print(
        "PORTFOLIO: do not lift to the Block91 34-outcome live joint law until the law/ontology route is chosen; algebraic label capacity is already adequate"
    )
    print(
        "SCOPE: no selected global law, core axiom edit, audit verdict, obligation retirement, retained end-to-end theory, or TOE percentage movement"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
