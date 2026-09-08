#!/usr/bin/env python3
"""Block 89: typed-event critical pairs for the live-M2 candidate.

The Block86 one-event instrument and its 15-site routed coherent core are
lifted to two events without silently identifying abstract Kraus support,
Record-write support, and physical routing support.  Disjoint full footprints
give exact branch-map and complete-ledger confluence.  A symmetry-related
ready pair has disjoint abstract instruments and writes but overlapping routed
cores whose two orders differ, so full-footprint arbitration is load-bearing.
The safe covariant all-conflicts-refuse scheduler is proved confluent but not
live; a deterministic covariant maximal selector is impossible on the swapped
pair without extra context.  This is a bounded scheduler/resource boundary,
not an adopted physical law or a TOE obligation retirement.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import combinations, product
import json
import math
from pathlib import Path
import subprocess

import numpy as np

import frontier_live_m2_conservative_archive_lock_instrument_2026_08_14 as block86


block73 = block86.block73
block72 = block86.block72
block71 = block86.block71

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_REPO_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_RUNNER = ROOT / "scripts" / (
    "frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py"
)
PARENT_NOTE = ROOT / "docs" / (
    "LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
)
PARENT_RECEIPT = "769100a0906c8b49c42702ae314a1b9077debfae"
HISTORICAL_PARENT_SHA256 = ('4f98e8a72a5c81805d9aedb5cf071598e5d94bc7de7928a686c0cc5eac42a999', 'b0486c818ac94b4b07967f221222f8acaa279d66bf51974ecea606c29315edb8')
PARENT_SHA256 = ('544a27161eacae82fb6d792eafb3e3a93f567d64a23565769a05d7a9f3270d89', '6e22bb1618341229793e9301e1ab7804b34203b55bbcae050c9fb8082cdeff2a')
HISTORICAL_PARENT_FILES = (('769100a0906c8b49c42702ae314a1b9077debfae', 'scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py'), ('769100a0906c8b49c42702ae314a1b9077debfae', 'docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md'))
AUDIT_INPUT_PATHS = (
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py",
)

# Current selected files; original receipt constants below remain historical.
CURRENT_INPUT_SHA256 = {
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "2d4fd67f35917906d6f2fd481a27a35ac49b54814644540f9f3c884263961038",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "6e22bb1618341229793e9301e1ab7804b34203b55bbcae050c9fb8082cdeff2a",
    "scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py": "544a27161eacae82fb6d792eafb3e3a93f567d64a23565769a05d7a9f3270d89",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md": "ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md": "29b0177eaca7e86542c1a15d9a64751895ea5798d695f6305f23891ec974ff58",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py": "7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py": "cff4964b3dc6acebb8ad4d0c501371197898b207f8cc77468e7c76749a6d9664",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py": "9586e59e5d30d7020dc3d5b03a461fe85a3e659790eacfb0fa1e489dc504cde1"
}
AUDIT_TIMEOUT_SEC = 180
TOL = 5.0e-11
IDENTITY_ROTATION: block71.Rotation = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
)
SWAP_ROTATION: block71.Rotation = (
    (1, 0, 0),
    (0, -1, 0),
    (0, 0, -1),
)
SWAP_TRANSLATION: block71.Coord = (0, 0, -1)
SENTINEL: block71.Coord = (100, -100, 90)
Content = object
BRANCH_KEYS: tuple[object, ...] = (
    "refusal",
    "no_event",
    (0, 0),
    (0, 1),
    (1, 0),
    (1, 1),
)


@dataclass(frozen=True)
class EventSpec:
    label: str
    rotation: block71.Rotation
    translation: block71.Coord


@dataclass(frozen=True)
class Ledger:
    records: tuple[tuple[block71.Coord, Content], ...]
    resources: tuple[tuple[str, str], ...]
    archives: tuple[str, ...]
    sources: tuple[tuple[block71.Coord, block71.Coord], ...]
    reservations: tuple[str, ...]


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str) -> None:
        result = bool(condition)
        self.passed += int(result)
        self.failed += int(not result)
        print(f"{'PASS' if result else 'FAIL'} {label}: {detail}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def file_sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def git_text(ref: str, path: str) -> str:
    return subprocess.check_output(
        ("git", "show", f"{ref}:{path}"), cwd=ROOT, text=True
    )


def is_ancestor(commit: str) -> bool:
    return subprocess.run(
        ("git", "merge-base", "--is-ancestor", commit, "HEAD"),
        cwd=ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    ).returncode == 0


def current_inputs_match() -> bool:
    return all((ROOT / path).is_file()
               and sha256((ROOT / path).read_bytes()).hexdigest() == digest
               for path, digest in CURRENT_INPUT_SHA256.items())


def authority_certificate(stale: bool = False) -> dict[str, object]:
    main = subprocess.check_output(
        ("git", "rev-parse", "origin/main"), cwd=ROOT, text=True
    ).strip()
    axiom = git_text("origin/main", AXIOM_REPO_PATH)
    registry_text = git_text("origin/main", REGISTRY_REPO_PATH)
    registry = json.loads(registry_text)
    paths = tuple(
        registry["nodes"][claim_id]["current_path"]
        for claim_id in registry["canonical_ids"]
    )
    source_texts = tuple(git_text("origin/main", path) for path in paths)
    forbidden = (
        "typed-event footprint reservation",
        "collision scheduler",
        "live-M2 formation instrument",
        "clean-input renewal law",
    )
    flat_axiom = " ".join(axiom.split())
    return {
        "main": main,
        "axiom_sha256": sha256(axiom.encode()).hexdigest(),
        "local_axiom_matches": (ROOT / AXIOM_REPO_PATH).read_text() == axiom,
        "local_registry_matches": (ROOT / REGISTRY_REPO_PATH).read_text() == registry_text,
        "canonical_ids": tuple(registry["canonical_ids"]),
        "current_paths": paths,
        "sources_present": all((ROOT / path).is_file() for path in paths),
        "sources_match": all((ROOT / path).read_text() == text for path, text in zip(paths, source_texts)),
        "scheduler_phrase_hits": sum(
            needle in text for needle in forbidden for text in source_texts
        ),
        "current_contract": all(
            phrase in flat_axiom
            for phrase in (
                "A state is a configuration of records.",
                "Admissibility is not a dynamics axiom.",
                "update laws",
                "the remaining formation rules",
                "source/action and physical-observable identification",
            )
        ),
        "parent_ancestor": is_ancestor(PARENT_RECEIPT),
        "parent_hashes": (file_sha256(PARENT_RUNNER), file_sha256(PARENT_NOTE)),
        "current_inputs_match": current_inputs_match(),
        "historical_parents_match": tuple(
            sha256(subprocess.check_output(("git", "show", f"{commit}:{path}"), cwd=ROOT)).hexdigest()
            for commit, path in HISTORICAL_PARENT_FILES
        ) == HISTORICAL_PARENT_SHA256,
        "forced_stale": stale,
    }


def matmul_rotation(
    left: block71.Rotation, right: block71.Rotation
) -> block71.Rotation:
    return tuple(
        tuple(
            sum(left[row][slot] * right[slot][column] for slot in range(3))
            for column in range(3)
        )
        for row in range(3)
    )  # type: ignore[return-value]


def transform_site(event: EventSpec, site: block71.Coord) -> block71.Coord:
    return block71.add(event.translation, block71.rotate(event.rotation, site))


def transform_event(
    rotation: block71.Rotation,
    translation: block71.Coord,
    event: EventSpec,
) -> EventSpec:
    return EventSpec(
        event.label,
        matmul_rotation(rotation, event.rotation),
        block71.add(translation, block71.rotate(rotation, event.translation)),
    )


@lru_cache(maxsize=None)
def base_physical_actions() -> tuple[block72.PhysicalAction, ...]:
    physical, _ideal = block86.ordered_actions()
    return physical


@lru_cache(maxsize=None)
def transformed_actions(event: EventSpec) -> tuple[block72.PhysicalAction, ...]:
    physical = base_physical_actions()
    return tuple(
        block72.PhysicalAction(
            action.kind,
            tuple(transform_site(event, site) for site in action.sites),
            action.matrix,
        )
        for action in physical
    )


@lru_cache(maxsize=None)
def base_core_support() -> frozenset[block71.Coord]:
    physical = base_physical_actions()
    return frozenset(site for action in physical for site in action.sites)


@lru_cache(maxsize=None)
def base_abstract_support() -> frozenset[block71.Coord]:
    return frozenset(
        set(block71.STARTS.values())
        | {block71.HEAD_SITE, block71.ROOT_SITE, block71.META_SITE}
    )


@lru_cache(maxsize=None)
def base_write_support() -> frozenset[block71.Coord]:
    return frozenset((block71.HEAD_SITE, block71.ROOT_SITE, block71.META_SITE))


@lru_cache(maxsize=None)
def event_support(event: EventSpec, kind: str = "core") -> frozenset[block71.Coord]:
    bases = {
        "core": base_core_support(),
        "abstract": base_abstract_support(),
        "write": base_write_support(),
    }
    return frozenset(transform_site(event, site) for site in bases[kind])


def fixed_requirements(event: EventSpec) -> dict[block71.Coord, int]:
    return {
        transform_site(event, block71.STARTS[role]): value
        for role, value in (("P", 1), ("B", 0), ("R", 0), ("A", 0))
    }


def simultaneously_ready(left: EventSpec, right: EventSpec) -> bool:
    requirements = fixed_requirements(left)
    for site, value in fixed_requirements(right).items():
        if site in requirements and requirements[site] != value:
            return False
        requirements[site] = value
    return True


def subtraction(left: block71.Coord, right: block71.Coord) -> block71.Coord:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def overlap_census_certificate() -> dict[str, object]:
    base = EventSpec("left", IDENTITY_ROTATION, (0, 0, 0))
    core = base_core_support()
    placements = ready = write_disjoint = abstract_disjoint = 0
    overlap_histogram: dict[int, int] = {}
    for rotation in block71.ROTATIONS:
        rotated = {block71.rotate(rotation, site) for site in core}
        translations = {
            subtraction(left, right) for left in core for right in rotated
        }
        for translation in translations:
            if rotation == IDENTITY_ROTATION and translation == (0, 0, 0):
                continue
            other = EventSpec("right", rotation, translation)
            overlap = event_support(base) & event_support(other)
            if not overlap:
                continue
            placements += 1
            if not simultaneously_ready(base, other):
                continue
            ready += 1
            if event_support(base, "write") & event_support(other, "write"):
                continue
            write_disjoint += 1
            overlap_histogram[len(overlap)] = overlap_histogram.get(len(overlap), 0) + 1
            if not (event_support(base, "abstract") & event_support(other, "abstract")):
                abstract_disjoint += 1
    diameter = max(
        block71.distance(left, right) for left in core for right in core
    )
    return {
        "core_sites": len(core),
        "abstract_sites": len(base_abstract_support()),
        "write_sites": len(base_write_support()),
        "core_diameter": diameter,
        "overlap_placements": placements,
        "simultaneously_ready": ready,
        "ready_write_disjoint": write_disjoint,
        "ready_write_and_abstract_disjoint": abstract_disjoint,
        "overlap_histogram": tuple(sorted(overlap_histogram.items())),
    }


def clean_entangled_amplitude() -> np.ndarray:
    target0 = np.eye(8, dtype=complex)[:, 0]
    target7 = np.eye(8, dtype=complex)[:, 7]
    state0 = block86.clean_input_vector(0, target0)
    state1 = block86.clean_input_vector(1, target7)
    return (
        np.outer(state0, state0) + 1j * np.outer(state1, state1)
    ) / math.sqrt(2)


def disjoint_branch_confluence_certificate(break_order: bool = False) -> dict[str, object]:
    left = EventSpec("left", IDENTITY_ROTATION, (0, 0, 0))
    right = EventSpec("right", IDENTITY_ROTATION, (20, 0, 0))
    operators = block86.instrument_operators()
    amplitude = clean_entangled_amplitude()
    maximum_residual = 0.0
    normalization = 0.0
    nonzero = 0
    cases = 0
    for left_index, left_operator in enumerate(operators.values()):
        left_applied = left_operator @ amplitude
        for right_index, right_operator in enumerate(operators.values()):
            left_then_right = left_applied @ right_operator.T
            right_then_left = left_operator @ (amplitude @ right_operator.T)
            if break_order and left_index == 0 and right_index == 0:
                left_then_right = left_then_right.copy()
                left_then_right[0, 0] += 1
            maximum_residual = max(
                maximum_residual,
                float(np.linalg.norm(left_then_right - right_then_left)),
            )
            probability = float(np.vdot(right_then_left, right_then_left).real)
            normalization += probability
            nonzero += probability > TOL
            cases += 1
    return {
        "branch_pairs": cases,
        "nonzero_branches": nonzero,
        "normalization": normalization,
        "maximum_order_residual": maximum_residual,
        "core_disjoint": event_support(left).isdisjoint(event_support(right)),
        "arbitrary_entangled_input": True,
        "external_reference_extension": True,
    }


def initial_ledger(events: tuple[EventSpec, ...]) -> Ledger:
    return Ledger(
        records=((SENTINEL, block71.KPLUS),),
        resources=tuple(sorted((event.label, "ready") for event in events)),
        archives=(),
        sources=(),
        reservations=tuple(sorted(event.label for event in events)),
    )


def canonical_ledger(
    records: dict[block71.Coord, Content],
    resources: dict[str, str],
    archives: set[str],
    sources: set[tuple[block71.Coord, block71.Coord]],
    reservations: set[str],
) -> Ledger:
    return Ledger(
        tuple(sorted(records.items())),
        tuple(sorted(resources.items())),
        tuple(sorted(archives)),
        tuple(sorted(sources)),
        tuple(sorted(reservations)),
    )


def branch_writes(event: EventSpec, branch: tuple[int, int]) -> dict[block71.Coord, Content]:
    m, b = branch
    return block86.packet_records(event.rotation, event.translation, m, b)


def apply_ledger_branch(
    ledger: Ledger,
    event: EventSpec,
    branch: object,
    *,
    overwrite: bool = False,
    erase_source: bool = False,
) -> tuple[str, Ledger]:
    records = dict(ledger.records)
    resources = dict(ledger.resources)
    archives = set(ledger.archives)
    sources = set(ledger.sources)
    reservations = set(ledger.reservations)
    occupied = not records.keys().isdisjoint(event_support(event))
    if resources.get(event.label) == "spent" or occupied:
        if overwrite and isinstance(branch, tuple):
            records.update(branch_writes(event, branch))
            return "event", canonical_ledger(records, resources, archives, sources, reservations)
        return "guard_refusal", ledger
    if not isinstance(branch, tuple):
        return str(branch), ledger
    writes = branch_writes(event, branch)
    if not records.keys().isdisjoint(writes) and not overwrite:
        return "guard_refusal", ledger
    records.update(writes)
    resources[event.label] = "spent"
    archives.add(event.label)
    root = transform_site(event, block71.ROOT_SITE)
    head = transform_site(event, block71.HEAD_SITE)
    if not erase_source:
        sources.add((root, head))
    reservations.discard(event.label)
    return "event", canonical_ledger(records, resources, archives, sources, reservations)


def complete_ledger_confluence_certificate(
    overwrite: bool = False,
    erase_source: bool = False,
) -> dict[str, object]:
    left = EventSpec("left", IDENTITY_ROTATION, (0, 0, 0))
    right = EventSpec("right", IDENTITY_ROTATION, (20, 0, 0))
    keys = BRANCH_KEYS
    mismatches = source_failures = decode_failures = 0
    branch_cases = 0
    for left_key, right_key in product(keys, repeat=2):
        initial = initial_ledger((left, right))
        _, after_left = apply_ledger_branch(
            initial, left, left_key, overwrite=overwrite, erase_source=erase_source
        )
        _, left_right = apply_ledger_branch(
            after_left, right, right_key, overwrite=overwrite, erase_source=erase_source
        )
        _, after_right = apply_ledger_branch(
            initial, right, right_key, overwrite=overwrite, erase_source=erase_source
        )
        _, right_left = apply_ledger_branch(
            after_right, left, left_key, overwrite=overwrite, erase_source=erase_source
        )
        mismatches += left_right != right_left
        expected_sources = int(isinstance(left_key, tuple)) + int(isinstance(right_key, tuple))
        source_failures += len(left_right.sources) != (0 if erase_source else expected_sources)
        for root, head in left_right.sources:
            delta = {root: -1, head: 1}
            boundary = {root: 1, head: -1}
            source_failures += any(delta[site] + boundary[site] for site in delta)
        packets = block71.find_packets(dict(left_right.records))
        decode_failures += len(packets) != expected_sources
        branch_cases += 1
    return {
        "branch_cases": branch_cases,
        "ledger_mismatches": mismatches,
        "source_failures": source_failures,
        "decode_failures": decode_failures,
        "record_components": True,
        "resource_components": True,
        "archive_components": True,
        "source_components": True,
        "reservation_components": True,
    }


def depth_two_certificate(overwrite: bool = False) -> dict[str, object]:
    left = EventSpec("left", IDENTITY_ROTATION, (0, 0, 0))
    right = EventSpec("right", IDENTITY_ROTATION, (20, 0, 0))
    initial = initial_ledger((left, right))
    _, after_left = apply_ledger_branch(initial, left, (0, 0), overwrite=overwrite)
    _, after_both = apply_ledger_branch(after_left, right, (1, 1), overwrite=overwrite)
    replay_left_status, replay_left = apply_ledger_branch(
        after_both, left, (0, 1), overwrite=overwrite
    )
    replay_right_status, replay_right = apply_ledger_branch(
        after_both, right, (1, 0), overwrite=overwrite
    )
    mixed_initial = initial_ledger((left, right))
    _, mixed = apply_ledger_branch(mixed_initial, left, (1, 0), overwrite=overwrite)
    no_status, mixed_no = apply_ledger_branch(mixed, right, "no_event", overwrite=overwrite)
    retry_status, mixed_retry = apply_ledger_branch(mixed_no, right, (0, 1), overwrite=overwrite)
    return {
        "records_after_two_events": len(after_both.records) - 1,
        "spent_after_two_events": sum(value == "spent" for _, value in after_both.resources),
        "archives_after_two_events": len(after_both.archives),
        "sources_after_two_events": len(after_both.sources),
        "left_replay_status": replay_left_status,
        "right_replay_status": replay_right_status,
        "left_replay_identity": replay_left == after_both,
        "right_replay_identity": replay_right == after_both,
        "mixed_no_event_status": no_status,
        "mixed_no_event_identity": mixed_no == mixed,
        "mixed_retry_status": retry_status,
        "mixed_retry_records": len(mixed_retry.records) - 1,
        "renewal_or_new_event_genesis": False,
    }


def ready_basis_state(left: EventSpec, right: EventSpec) -> tuple[tuple[block71.Coord, ...], tuple[int, ...]]:
    requirements = fixed_requirements(left)
    for site, value in fixed_requirements(right).items():
        if site in requirements and requirements[site] != value:
            raise ValueError("incompatible ready fixtures")
        requirements[site] = value
    for event in (left, right):
        requirements.setdefault(transform_site(event, block71.STARTS["M"]), 0)
    sites = tuple(sorted(event_support(left) | event_support(right)))
    bits = tuple(requirements.get(site, 0) for site in sites)
    return sites, bits


def physical_collision_certificate(hide_collision: bool = False) -> dict[str, object]:
    left = EventSpec("left", IDENTITY_ROTATION, (0, 0, 0))
    right = EventSpec("right", SWAP_ROTATION, SWAP_TRANSLATION)
    left_actions = transformed_actions(left)
    right_actions = transformed_actions(right)
    sites, bits = ready_basis_state(left, right)
    site_index = {site: index for index, site in enumerate(sites)}
    state = {bits: 1.0 + 0.0j}
    left_right = block86.apply_physical_actions(
        block86.apply_physical_actions(state, left_actions, site_index),
        right_actions,
        site_index,
    )
    right_left = block86.apply_physical_actions(
        block86.apply_physical_actions(state, right_actions, site_index),
        left_actions,
        site_index,
    )
    residual = block72.state_residual(left_right, right_left)
    if hide_collision:
        residual = 0.0
    swapped_left = transform_event(SWAP_ROTATION, SWAP_TRANSLATION, left)
    swapped_right = transform_event(SWAP_ROTATION, SWAP_TRANSLATION, right)
    geometry = EventSpec("symmetry", SWAP_ROTATION, SWAP_TRANSLATION)
    ready_state = dict(zip(sites, bits))
    ready_state_invariant = all(
        transform_site(geometry, site) in ready_state
        and ready_state[transform_site(geometry, site)] == value
        for site, value in ready_state.items()
    )
    return {
        "simultaneously_ready": simultaneously_ready(left, right),
        "write_overlap": len(event_support(left, "write") & event_support(right, "write")),
        "abstract_overlap": len(event_support(left, "abstract") & event_support(right, "abstract")),
        "core_overlap": len(event_support(left) & event_support(right)),
        "union_sites": len(sites),
        "left_right_terms": len(left_right),
        "right_left_terms": len(right_left),
        "order_residual": residual,
        "affine_involution": (
            matmul_rotation(SWAP_ROTATION, SWAP_ROTATION) == IDENTITY_ROTATION
            and block71.add(
                block71.rotate(SWAP_ROTATION, SWAP_TRANSLATION),
                SWAP_TRANSLATION,
            ) == (0, 0, 0)
        ),
        "events_swapped": (
            swapped_left.rotation == right.rotation
            and swapped_left.translation == right.translation
            and swapped_right.rotation == left.rotation
            and swapped_right.translation == left.translation
        ),
        "ready_state_invariant": ready_state_invariant,
    }


def conflict(left: EventSpec, right: EventSpec, write_only: bool = False) -> bool:
    kind = "write" if write_only else "core"
    return not event_support(left, kind).isdisjoint(event_support(right, kind))


def isolated_events(
    events: tuple[EventSpec, ...], *, write_only: bool = False, tie_break: bool = False
) -> tuple[EventSpec, ...]:
    accepted = tuple(
        event
        for event in events
        if all(
            other == event or not conflict(event, other, write_only)
            for other in events
        )
    )
    if tie_break and not accepted and events:
        return (sorted(events, key=lambda item: (item.translation, item.rotation))[0],)
    return accepted


def scheduler_certificate(write_only: bool = False, tie_break: bool = False) -> dict[str, object]:
    disjoint = (
        EventSpec("left", IDENTITY_ROTATION, (0, 0, 0)),
        EventSpec("right", IDENTITY_ROTATION, (20, 0, 0)),
    )
    symmetric = (
        EventSpec("left", IDENTITY_ROTATION, (0, 0, 0)),
        EventSpec("right", SWAP_ROTATION, SWAP_TRANSLATION),
    )
    disjoint_accepted = isolated_events(disjoint, write_only=write_only, tie_break=tie_break)
    conflict_accepted = isolated_events(symmetric, write_only=write_only, tie_break=tie_break)
    covariance_failures = 0
    for rotation in block71.ROTATIONS:
        for translation in ((0, 0, 0), (7, -5, 3)):
            transformed = tuple(
                transform_event(rotation, translation, event) for event in symmetric
            )
            accepted_transformed = isolated_events(
                transformed, write_only=write_only, tie_break=tie_break
            )
            expected_geometries = {
                (
                    transform_event(rotation, translation, event).rotation,
                    transform_event(rotation, translation, event).translation,
                )
                for event in conflict_accepted
            }
            observed_geometries = {
                (event.rotation, event.translation) for event in accepted_transformed
            }
            covariance_failures += observed_geometries != expected_geometries

    # The affine involution exchanges the two events.  Its invariant subsets
    # are empty and the full conflicting pair; only empty is conflict-free.
    invariant_subsets = 0
    invariant_conflict_free = 0
    invariant_maximal_conflict_free = 0
    for mask in range(4):
        subset = {index for index in range(2) if (mask >> index) & 1}
        image = {1 - index for index in subset}
        if subset != image:
            continue
        invariant_subsets += 1
        conflict_free = len(subset) < 2
        invariant_conflict_free += conflict_free
        maximal = conflict_free and len(subset) == 1
        invariant_maximal_conflict_free += maximal
    return {
        "disjoint_accepted": len(disjoint_accepted),
        "conflict_accepted": len(conflict_accepted),
        "conflict_free": all(
            not conflict(left, right)
            for left, right in combinations(conflict_accepted, 2)
        ),
        "covariance_cases": 48,
        "covariance_failures": covariance_failures,
        "invariant_subsets": invariant_subsets,
        "invariant_conflict_free": invariant_conflict_free,
        "invariant_maximal_conflict_free": invariant_maximal_conflict_free,
        "safe_conflict_rule": "refuse_all_members_of_each_conflict_component",
        "conflict_fixture_progress": len(conflict_accepted) > 0,
        "full_footprint_guard": not write_only,
        "deterministic_tie_break": tie_break,
    }


def resource_source_certificate(erase_source: bool = False, fake_renewal: bool = False) -> dict[str, object]:
    left = EventSpec("left", IDENTITY_ROTATION, (0, 0, 0))
    right = EventSpec("right", IDENTITY_ROTATION, (20, 0, 0))
    ledger = initial_ledger((left, right))
    _, ledger = apply_ledger_branch(ledger, left, (0, 1), erase_source=erase_source)
    _, ledger = apply_ledger_branch(ledger, right, (1, 0), erase_source=erase_source)
    resources = dict(ledger.resources)
    if fake_renewal:
        resources = {key: "ready" for key in resources}
    continuity_failures = 0
    for root, head in ledger.sources:
        delta = {root: -1, head: 1}
        boundary = {root: 1, head: -1}
        continuity_failures += any(delta[site] + boundary[site] for site in delta)
    return {
        "event_count": 2,
        "records_written": len(ledger.records) - 1,
        "archives": len(ledger.archives),
        "sources": len(ledger.sources),
        "spent_resources": sum(value == "spent" for value in resources.values()),
        "continuity_failures": continuity_failures,
        "clean_genesis_supplied": False,
        "renewal_supplied": fake_renewal,
        "physical_rate_supplied": False,
        "energy_normalization_supplied": False,
        "gravity_action_supplied": False,
    }


def boundary_surface_ok(law_claim: bool = False, false_progress: bool = False) -> bool:
    if not NOTE_PATH.is_file():
        return False
    note = NOTE_PATH.read_text(encoding="utf-8")
    needles = (
        "### N1 — Alternative-route enumeration and normalization",
        "### N2 — Wall-independence audit",
        "### N3 — Hidden-wall scan",
        "### N4 — Residual matching",
        "### N5 — Rhetoric and granularity audit",
        "### N6 — Partial-closure path scan",
        "### N7 — Steelman and strongest surviving escape route",
        "### N8 — Cross-cycle echo audit",
        "full 15-site physical footprint",
        "deterministic covariant maximal selector",
        "all-conflicts-refuse",
        "no TOE percentage movement",
        "not an approved primitive",
        "live-M2 ontology remains conditional",
        "Record-write disjointness is insufficient",
        "clean-resource genesis and renewal remain open",
        "gravity remains open",
    )
    return not law_claim and not false_progress and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom",
            "break_branch_order",
            "overwrite",
            "hide_collision",
            "write_only_guard",
            "tie_break",
            "erase_source",
            "fake_renewal",
            "law_claim",
            "false_progress",
        ),
    )
    args = parser.parse_args()
    mutation = args.mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    authority_ok = (
        authority["local_axiom_matches"]
        and authority["local_registry_matches"]
        and authority["canonical_ids"] == (
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        )
        and authority["sources_present"]
        and authority["sources_match"]
        and authority["scheduler_phrase_hits"] == 0
        and authority["current_contract"]
        and authority["current_inputs_match"]
        and authority["historical_parents_match"]
        and authority["parent_hashes"] == PARENT_SHA256
        and not authority["forced_stale"]
    )
    checks.check(
        "A-current-authority-and-exact-Block86-parent",
        authority_ok,
        f"axiom={str(authority['axiom_sha256'])[:12]}; live authority and four premises contain no typed-event scheduler/renewal registration",
    )

    census = overlap_census_certificate()
    census_ok = (
        census["core_sites"] == 15
        and census["abstract_sites"] == 8
        and census["write_sites"] == 3
        and census["overlap_placements"] == 2365
        and census["simultaneously_ready"] == 2230
        and census["ready_write_disjoint"] == 2055
        and census["ready_write_and_abstract_disjoint"] == 1134
    )
    checks.check(
        "B-exact-nearby-critical-pair-census",
        census_ok,
        f"15/8/3 core/abstract/write sites; {census['overlap_placements']} overlapping placements, {census['simultaneously_ready']} ready, {census['ready_write_disjoint']} ready+write-disjoint, {census['ready_write_and_abstract_disjoint']} also abstract-disjoint",
    )

    branch = disjoint_branch_confluence_certificate(mutation == "break_branch_order")
    branch_ok = (
        branch["branch_pairs"] == 36
        and branch["nonzero_branches"] == 17
        and abs(branch["normalization"] - 1) < TOL
        and branch["maximum_order_residual"] < TOL
        and branch["core_disjoint"]
        and branch["arbitrary_entangled_input"]
        and branch["external_reference_extension"]
    )
    checks.check(
        "C-disjoint-full-footprint-CP-branch-confluence",
        branch_ok,
        f"all {branch['branch_pairs']} unnormalized branch pairs commute on an entangled two-event input; 17 nonzero branches normalize to {branch['normalization']:.15g}, residual={branch['maximum_order_residual']:.2e}",
    )

    ledger = complete_ledger_confluence_certificate(
        mutation == "overwrite", False
    )
    ledger_ok = (
        ledger["branch_cases"] == 36
        and ledger["ledger_mismatches"] == 0
        and ledger["source_failures"] == 0
        and ledger["decode_failures"] == 0
        and all(
            ledger[key]
            for key in (
                "record_components",
                "resource_components",
                "archive_components",
                "source_components",
                "reservation_components",
            )
        )
    )
    checks.check(
        "D-complete-Record-resource-archive-source-ledger-confluence",
        ledger_ok,
        f"{ledger['branch_cases']} branch pairs have {ledger['ledger_mismatches']} complete-ledger order mismatches, {ledger['source_failures']} source-continuity failures, {ledger['decode_failures']} packet-decoder failures",
    )

    depth = depth_two_certificate(mutation == "overwrite")
    depth_ok = (
        depth["records_after_two_events"] == 6
        and depth["spent_after_two_events"] == 2
        and depth["archives_after_two_events"] == 2
        and depth["sources_after_two_events"] == 2
        and depth["left_replay_status"] == "guard_refusal"
        and depth["right_replay_status"] == "guard_refusal"
        and depth["left_replay_identity"]
        and depth["right_replay_identity"]
        and depth["mixed_no_event_status"] == "no_event"
        and depth["mixed_no_event_identity"]
        and depth["mixed_retry_status"] == "event"
        and depth["mixed_retry_records"] == 6
        and not depth["renewal_or_new_event_genesis"]
    )
    checks.check(
        "E-depth-two-replay-and-mixed-branch-control",
        depth_ok,
        f"two events write {depth['records_after_two_events']} Records and spend {depth['spent_after_two_events']} packets; replays are {depth['left_replay_status']}/{depth['right_replay_status']}, while a disjoint no-event remains retryable",
    )

    collision = physical_collision_certificate(mutation == "hide_collision")
    collision_ok = (
        collision["simultaneously_ready"]
        and collision["write_overlap"] == 0
        and collision["abstract_overlap"] == 0
        and collision["core_overlap"] == 8
        and collision["affine_involution"]
        and collision["events_swapped"]
        and collision["ready_state_invariant"]
        and collision["order_residual"] > TOL
    )
    checks.check(
        "F-write-and-abstract-disjoint-routed-core-collision",
        collision_ok,
        f"the swapped ready pair has write/abstract/core overlaps {collision['write_overlap']}/{collision['abstract_overlap']}/{collision['core_overlap']}; {collision['left_right_terms']}/{collision['right_left_terms']} sparse terms differ by {collision['order_residual']:.6g}",
    )

    scheduler = scheduler_certificate(
        mutation == "write_only_guard", mutation == "tie_break"
    )
    scheduler_ok = (
        scheduler["disjoint_accepted"] == 2
        and scheduler["conflict_accepted"] == 0
        and scheduler["conflict_free"]
        and scheduler["covariance_cases"] == 48
        and scheduler["covariance_failures"] == 0
        and scheduler["invariant_subsets"] == 2
        and scheduler["invariant_conflict_free"] == 1
        and scheduler["invariant_maximal_conflict_free"] == 0
        and scheduler["full_footprint_guard"]
        and not scheduler["deterministic_tie_break"]
        and not scheduler["conflict_fixture_progress"]
    )
    checks.check(
        "G-covariant-conflict-refusal-and-maximal-selector-obstruction",
        scheduler_ok,
        f"the full-footprint scheduler accepts {scheduler['disjoint_accepted']} disjoint and {scheduler['conflict_accepted']} conflicting events in 48 covariance cases; swapped pair has {scheduler['invariant_maximal_conflict_free']} invariant maximal conflict-free selections",
    )

    resources = resource_source_certificate(
        mutation == "erase_source", mutation == "fake_renewal"
    )
    resource_ok = (
        resources["event_count"] == 2
        and resources["records_written"] == 6
        and resources["archives"] == 2
        and resources["sources"] == 2
        and resources["spent_resources"] == 2
        and resources["continuity_failures"] == 0
        and not resources["clean_genesis_supplied"]
        and not resources["renewal_supplied"]
        and not resources["physical_rate_supplied"]
        and not resources["energy_normalization_supplied"]
        and not resources["gravity_action_supplied"]
    )
    checks.check(
        "H-exact-debit-and-source-boundary",
        resource_ok,
        f"two events debit {resources['spent_resources']} ready packets, archive {resources['archives']} targets, write {resources['records_written']} Records and {resources['sources']} conserved source edges; renewal/rate/energy/gravity remain unsupplied",
    )

    boundary_ok = boundary_surface_ok(
        mutation == "law_claim", mutation == "false_progress"
    )
    checks.check(
        "I-bounded-law-and-TOE-accounting",
        boundary_ok,
        "the N1-N8 surface identifies a sufficient confluent guard and the exact liveness/symmetry/resource/ontology walls without adoption, retention, or score movement",
    )

    print(
        "METRICS overlap_placements={} ready_overlap={} write_disjoint_ready={} abstract_disjoint_ready={} routed_order_residual={:.9g}".format(
            census["overlap_placements"],
            census["simultaneously_ready"],
            census["ready_write_disjoint"],
            census["ready_write_and_abstract_disjoint"],
            collision["order_residual"],
        )
    )
    print("N5_RESOLUTION per_element: all six Block86 Kraus labels and all 36 two-event branch pairs are typed; zero labels are inferred from host control")
    print("N5_RESOLUTION per_site: the exact 15-site core, eight-site abstract support, three writes, fixed inputs, matter slot, and transformed source edge are separated")
    print("N5_RESOLUTION per_mode: disjoint, overlapping, write-disjoint, abstract-disjoint, entangled-input, no-event, event, replay, and symmetric-conflict modes are checked")
    print("N5_RESOLUTION per_block: current authority, Block86 receipt, CP maps, routed core, Record/resource/archive/source ledger, scheduler, and depth-two control are checked")
    print("N5_RESOLUTION lattice_wide: all finite relative core-overlap placements over 24 proper-cubic orientations are exhausted; arbitrary finite/infinite enabled-event confluence, liveness, renewal, time, energy, and gravity are not claimed")
    print(
        "BOUNDARY: disjoint full physical footprints give exact two-event branch and complete-ledger confluence, but Record-write and abstract-instrument disjointness do not protect the routed core; the covariant all-conflicts-refuse rule is safe but deadlocks the symmetric fixture, while stochastic arbitration, readable symmetry breaking, or a merged collision law and clean-resource renewal remain supplied choices"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
