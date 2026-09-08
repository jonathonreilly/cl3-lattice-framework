#!/usr/bin/env python3
"""Block 91: normalized joint order-environment semantic collision instrument.

The Block90 semantic-overlap witness cannot execute two isolated event words:
their ideal orders differ by sqrt(2).  This runner instead makes order a
physical environment label.  It applies both coherent dilations before either
archive, projects the two event outcomes jointly, and then archives both
events.  Refusal, no-event, and two orders times sixteen joint event branches
form a 34-outcome normalized instrument on the exact fifteen-site witness.

The finite Block89 census is also sharpened.  Both dilation orders normalize
on all 921 ready write-disjoint semantic-overlap placements.  Of these, 447
have disjoint six-site archive supports; 445 additionally admit every required
cross-semantic swap-back path in the present compiler, while two are trapped
by the semantic obstacle set.  The exact witness compiles in either order to
374 nearest-neighbor primitives on one guarded 52-site corridor.

This is supplied formation/update content.  It is not selected by current
authority and does not provide corridor genesis, a global atlas, outcome
actuality, renewal, cadence, source/action typing, gravity, audit retention,
obligation retirement, or TOE percentage movement.
"""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from dataclasses import dataclass
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import subprocess

import numpy as np

import frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14 as block90


block89 = block90.block89
block86 = block90.block86
block72 = block90.block72
block71 = block90.block71

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_REPO_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_RECEIPT = "161a6ed1f9"
PARENT_RUNNER = ROOT / "scripts" / (
    "frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14.py"
)
PARENT_NOTE = ROOT / "docs" / (
    "LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
)
HISTORICAL_PARENT_SHA256 = ('7207915e40339d1cc1cf0848acc9359e0cefbd10b15c49cc643f35508d76a534', '2b1acd0de5f63e60248fdfcd2abda67d1bb15787a081343397f54bcbbf99ba7f')
PARENT_SHA256 = ('e649a807fb02c80974ffff827f03ac6a28c568ad9c1517e7c259d82d8ee06395', 'ec3d6653b00f6d06b4eb95ac6bb24c6024e3fbe63d5a8ce5a6b78fca9a175968')
HISTORICAL_PARENT_FILES = (('161a6ed1f9', 'scripts/frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14.py'), ('161a6ed1f9', 'docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md'))
AUDIT_INPUT_PATHS = (
    "docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14.py",
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py",
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py",
)

# Current selected files; original receipt constants below remain historical.
CURRENT_INPUT_SHA256 = {
    "docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "7a75e900c7507eef7369f4b22196eb7b20997a427d798c5d0f6fe84c1f5c236a",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md": "ec3d6653b00f6d06b4eb95ac6bb24c6024e3fbe63d5a8ce5a6b78fca9a175968",
    "scripts/frontier_live_m2_pair_aware_swapback_collision_repair_2026_08_14.py": "e649a807fb02c80974ffff827f03ac6a28c568ad9c1517e7c259d82d8ee06395",
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "2d4fd67f35917906d6f2fd481a27a35ac49b54814644540f9f3c884263961038",
    "scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py": "81e5b4845c64cc149ab1984e0884975e8ec279a7ea6fbaeb5ac88ff4ac83504a",
    "docs/LIVE_M2_CONSERVATIVE_ARCHIVE_LOCK_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "6e22bb1618341229793e9301e1ab7804b34203b55bbcae050c9fb8082cdeff2a",
    "scripts/frontier_live_m2_conservative_archive_lock_instrument_2026_08_14.py": "544a27161eacae82fb6d792eafb3e3a93f567d64a23565769a05d7a9f3270d89",
    "docs/RECORD_VISIBLE_INTEGRATED_FORMATION_INSTRUMENT_BOUNDED_NOTE_2026-08-14.md": "29b0177eaca7e86542c1a15d9a64751895ea5798d695f6305f23891ec974ff58",
    "scripts/frontier_record_visible_integrated_formation_instrument_2026_08_14.py": "9586e59e5d30d7020dc3d5b03a461fe85a3e659790eacfb0fa1e489dc504cde1",
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md": "ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6",
    "scripts/frontier_nn_formation_selector_two_model_kill_2026_08_14.py": "cff4964b3dc6acebb8ad4d0c501371197898b207f8cc77468e7c76749a6d9664",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py": "7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c"
}
AUDIT_TIMEOUT_SEC = 240
TOL = 5.0e-11
HAZARD = float(block86.HAZARD)
BRANCHES = tuple(product((0, 1), repeat=2))
JOINT_BRANCHES = tuple(product(BRANCHES, repeat=2))
ROLES = block90.ROLES


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
    axiom = git_text("origin/main", AXIOM_REPO_PATH)
    registry_text = git_text("origin/main", REGISTRY_REPO_PATH)
    registry = json.loads(registry_text)
    paths = tuple(
        registry["nodes"][claim_id]["current_path"]
        for claim_id in registry["canonical_ids"]
    )
    source_texts = tuple(git_text("origin/main", path) for path in paths)
    forbidden = (
        "joint order-environment collision instrument",
        "34-outcome semantic collision law",
        "pair-aware semantic-overlap formation law",
        "clean order-coin renewal law",
    )
    flat_axiom = " ".join(axiom.split())
    return {
        "axiom_sha256": sha256(axiom.encode()).hexdigest(),
        "local_axiom_matches": (ROOT / AXIOM_REPO_PATH).read_text() == axiom,
        "local_registry_matches": (ROOT / REGISTRY_REPO_PATH).read_text()
        == registry_text,
        "canonical_ids": tuple(registry["canonical_ids"]),
        "sources_match": all(
            (ROOT / path).is_file() and (ROOT / path).read_text() == text
            for path, text in zip(paths, source_texts)
        ),
        "forbidden_phrase_hits": sum(
            phrase in text for phrase in forbidden for text in source_texts
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


def witness_events() -> tuple[block89.EventSpec, block89.EventSpec]:
    return (
        block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0)),
        block89.EventSpec(
            "right",
            block90.SEMANTIC_OVERLAP_ROTATION,
            block90.SEMANTIC_OVERLAP_TRANSLATION,
        ),
    )


def event_site(
    event: block89.EventSpec, site: block71.Coord
) -> block71.Coord:
    return block90.event_site(event, site)


def semantic_support(event: block89.EventSpec) -> frozenset[block71.Coord]:
    return block90.semantic_support(event)


def start_sites(event: block89.EventSpec) -> frozenset[block71.Coord]:
    return frozenset(event_site(event, block71.STARTS[role]) for role in ROLES)


def archive_support(event: block89.EventSpec) -> frozenset[block71.Coord]:
    return frozenset(
        event_site(event, block71.STARTS[role]) for role in ("P", "M", "B")
    ) | frozenset(
        event_site(event, site)
        for site in (block71.HEAD_SITE, block71.ROOT_SITE, block71.META_SITE)
    )


def dilation_actions(
    event: block89.EventSpec,
) -> tuple[block72.PhysicalAction, ...]:
    return tuple(
        block72.PhysicalAction(
            gate.kind,
            tuple(
                event_site(event, block71.STARTS[ROLES[wire]])
                for wire in gate.wires
            ),
            gate.matrix,
        )
        for gate in block71.dilation_word()
    )


def archive_actions(
    event: block89.EventSpec,
) -> tuple[block72.PhysicalAction, ...]:
    actions = block90.ideal_event_actions(event)
    return actions[len(block71.dilation_word()) :]


def ordered_events(
    events: tuple[block89.EventSpec, block89.EventSpec], order: int
) -> tuple[block89.EventSpec, block89.EventSpec]:
    return events if order == 0 else tuple(reversed(events))


def joint_dilation_actions(
    events: tuple[block89.EventSpec, block89.EventSpec], order: int
) -> tuple[block72.PhysicalAction, ...]:
    return tuple(
        action
        for event in ordered_events(events, order)
        for action in dilation_actions(event)
    )


def joint_archive_actions(
    events: tuple[block89.EventSpec, block89.EventSpec]
) -> tuple[block72.PhysicalAction, ...]:
    return archive_actions(events[0]) + archive_actions(events[1])


def branch_matches(
    bits: tuple[int, ...],
    site_index: dict[block71.Coord, int],
    events: tuple[block89.EventSpec, block89.EventSpec],
    branch: tuple[tuple[int, int], tuple[int, int]],
) -> bool:
    for event, (matter, bit) in zip(events, branch):
        required = (
            (event_site(event, block71.STARTS["P"]), 1),
            (event_site(event, block71.STARTS["M"]), matter),
            (event_site(event, block71.STARTS["B"]), bit),
        )
        if any(bits[site_index[site]] != value for site, value in required):
            return False
    return True


def project_branch(
    state: dict[tuple[int, ...], complex],
    site_index: dict[block71.Coord, int],
    events: tuple[block89.EventSpec, block89.EventSpec],
    branch: tuple[tuple[int, int], tuple[int, int]],
) -> dict[tuple[int, ...], complex]:
    return {
        bits: amplitude
        for bits, amplitude in state.items()
        if branch_matches(bits, site_index, events, branch)
    }


def state_probability(state: dict[tuple[int, ...], complex]) -> float:
    return float(sum(abs(amplitude) ** 2 for amplitude in state.values()))


def joint_ready_requirements(
    events: tuple[block89.EventSpec, block89.EventSpec]
) -> dict[block71.Coord, int]:
    requirements = block89.fixed_requirements(events[0])
    requirements.update(block89.fixed_requirements(events[1]))
    return requirements


def dilation_order_leakage(
    events: tuple[block89.EventSpec, block89.EventSpec], order: int
) -> tuple[float, int]:
    sites = tuple(sorted(start_sites(events[0]) | start_sites(events[1])))
    site_index = {site: index for index, site in enumerate(sites)}
    requirements = joint_ready_requirements(events)
    free = tuple(
        sorted(
            {
                event_site(event, block71.STARTS["M"])
                for event in events
            }
            - set(requirements)
        )
    )
    maximum = 0.0
    cases = 0
    for values in product((0, 1), repeat=len(free)):
        bits = [0] * len(sites)
        for site, value in requirements.items():
            bits[site_index[site]] = value
        for site, value in zip(free, values):
            bits[site_index[site]] = value
        output = block86.apply_physical_actions(
            {tuple(bits): 1.0 + 0.0j},
            joint_dilation_actions(events, order),
            site_index,
        )
        bad = sum(
            abs(amplitude) ** 2
            for target, amplitude in output.items()
            if any(
                target[
                    site_index[event_site(event, block71.STARTS["P"])]
                ]
                != 1
                for event in events
            )
        )
        maximum = max(maximum, float(bad))
        cases += 1
    return maximum, cases


@lru_cache(maxsize=None)
def census_certificate(miss_one: bool = False) -> dict[str, object]:
    base = block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0))
    core = block89.base_core_support()
    semantic_overlap = archive_disjoint = archive_overlap = 0
    dilation_order_checks = dilation_failures = dilation_basis_cases = 0
    route_checks = route_failures = fully_routable = 0
    archive_overlap_histogram: Counter[int] = Counter()
    route_failure_geometries: list[tuple[object, ...]] = []
    for rotation in block71.ROTATIONS:
        rotated = {block71.rotate(rotation, site) for site in core}
        translations = {
            block89.subtraction(left, right)
            for left in core
            for right in rotated
        }
        for translation in translations:
            if rotation == block89.IDENTITY_ROTATION and translation == (0, 0, 0):
                continue
            other = block89.EventSpec("right", rotation, translation)
            if not (block89.event_support(base) & block89.event_support(other)):
                continue
            if not block89.simultaneously_ready(base, other):
                continue
            if block89.event_support(base, "write") & block89.event_support(
                other, "write"
            ):
                continue
            if not (semantic_support(base) & semantic_support(other)):
                continue
            semantic_overlap += 1
            events = (base, other)
            for order in (0, 1):
                leakage, cases = dilation_order_leakage(events, order)
                dilation_order_checks += 1
                dilation_basis_cases += cases
                dilation_failures += leakage >= TOL
            overlap = len(archive_support(base) & archive_support(other))
            archive_overlap_histogram[overlap] += 1
            if overlap:
                archive_overlap += 1
                continue
            archive_disjoint += 1
            all_semantic = semantic_support(base) | semantic_support(other)
            pair_failures = 0
            for event in events:
                for start, target in block90.event_endpoint_pairs(event):
                    route_checks += 1
                    try:
                        block90.pair_path(start, target, all_semantic)
                    except RuntimeError:
                        route_failures += 1
                        pair_failures += 1
                        route_failure_geometries.append(
                            (rotation, translation, event.label, start, target)
                        )
            fully_routable += pair_failures == 0
    if miss_one:
        dilation_failures += 1
    return {
        "semantic_overlap": semantic_overlap,
        "archive_disjoint": archive_disjoint,
        "archive_overlap": archive_overlap,
        "archive_overlap_histogram": tuple(sorted(archive_overlap_histogram.items())),
        "dilation_order_checks": dilation_order_checks,
        "dilation_basis_cases": dilation_basis_cases,
        "dilation_failures": dilation_failures,
        "route_checks": route_checks,
        "route_failures": route_failures,
        "fully_routable": fully_routable,
        "route_failure_geometries": tuple(route_failure_geometries),
        "forced_miss": miss_one,
    }


def witness_basis_data() -> tuple[
    tuple[block71.Coord, ...],
    dict[block71.Coord, int],
    tuple[block71.Coord, block71.Coord],
    tuple[block71.Coord, ...],
]:
    events = witness_events()
    sites = tuple(sorted(semantic_support(events[0]) | semantic_support(events[1])))
    requirements = joint_ready_requirements(events)
    matter_sites = tuple(
        event_site(event, block71.STARTS["M"]) for event in events
    )
    target_sites = tuple(
        sorted(
            {
                event_site(event, site)
                for event in events
                for site in (block71.HEAD_SITE, block71.ROOT_SITE, block71.META_SITE)
            }
        )
    )
    return sites, requirements, matter_sites, target_sites


def witness_input(
    matter: tuple[int, int], target_index: int
) -> tuple[tuple[int, ...], dict[block71.Coord, int]]:
    sites, requirements, matter_sites, target_sites = witness_basis_data()
    site_index = {site: index for index, site in enumerate(sites)}
    values = dict(requirements)
    values[matter_sites[0]] = matter[0]
    values[matter_sites[1]] = matter[1]
    bits = [0] * len(sites)
    for site, value in values.items():
        bits[site_index[site]] = value
    for wire, site in enumerate(target_sites):
        bits[site_index[site]] = (target_index >> wire) & 1
    return tuple(bits), site_index


@lru_cache(maxsize=None)
def completeness_certificate(break_completeness: bool = False) -> dict[str, object]:
    events = witness_events()
    sites, requirements, _, target_sites = witness_basis_data()
    maximum_order_residual = 0.0
    maximum_total_residual = 0.0
    order_basis_cases = 0
    for matter in product((0, 1), repeat=2):
        for target_index in range(1 << len(target_sites)):
            bits, site_index = witness_input(matter, target_index)
            order_sums: list[float] = []
            for order in (0, 1):
                dilated = block86.apply_physical_actions(
                    {bits: 1.0 + 0.0j},
                    joint_dilation_actions(events, order),
                    site_index,
                )
                total = 0.0
                for branch_index, branch in enumerate(JOINT_BRANCHES):
                    probability = state_probability(
                        project_branch(dilated, site_index, events, branch)
                    )
                    if break_completeness and order == 0 and branch_index == 0:
                        probability *= 2
                    total += probability
                order_sums.append(total)
                maximum_order_residual = max(
                    maximum_order_residual, abs(total - 1.0)
                )
                order_basis_cases += 1
            normalized = (1 - HAZARD) + HAZARD * 0.5 * sum(order_sums)
            maximum_total_residual = max(
                maximum_total_residual, abs(normalized - 1.0)
            )
    nonready_cases = 0
    refusal_failures = 0
    base_bits, site_index = witness_input((0, 0), 0)
    for site, required in requirements.items():
        hostile = list(base_bits)
        hostile[site_index[site]] = 1 - required
        refusal_failures += all(
            hostile[site_index[fixed]] == value
            for fixed, value in requirements.items()
        )
        nonready_cases += 1
    full_dimension = 1 << len(sites)
    ready_rank = 4 * (1 << len(target_sites))
    return {
        "outcomes": 34,
        "order_labels": 2,
        "joint_event_labels_per_order": 16,
        "semantic_sites": len(sites),
        "full_dimension": full_dimension,
        "ready_rank": ready_rank,
        "refusal_rank": full_dimension - ready_rank,
        "no_event_weight": 1 - HAZARD,
        "joint_event_weight": HAZARD,
        "order_basis_cases": order_basis_cases,
        "maximum_order_completeness_residual": maximum_order_residual,
        "maximum_full_completeness_residual": maximum_total_residual,
        "nonready_refusal_cases": nonready_cases,
        "refusal_failures": refusal_failures,
        "naimark_input_dimension": full_dimension,
        "naimark_output_dimension": 34 * full_dimension,
        "binary_environment_qubits": math.ceil(math.log2(34)),
        "break_completeness": break_completeness,
    }


def erase_wire(
    state: dict[tuple[int, ...], complex], wire: int
) -> dict[tuple[int, ...], complex]:
    output: dict[tuple[int, ...], complex] = {}
    for bits, amplitude in state.items():
        target = list(bits)
        target[wire] = 0
        key = tuple(target)
        output[key] = output.get(key, 0.0j) + amplitude
    return output


def normalized_state(
    state: dict[tuple[int, ...], complex]
) -> dict[tuple[int, ...], complex]:
    norm = math.sqrt(state_probability(state))
    return {bits: amplitude / norm for bits, amplitude in state.items()}


def sparse_inner(
    left: dict[tuple[int, ...], complex],
    right: dict[tuple[int, ...], complex],
) -> complex:
    if len(left) > len(right):
        left, right = right, left
        return np.conjugate(sparse_inner(left, right))
    return sum(np.conjugate(amplitude) * right.get(bits, 0.0j) for bits, amplitude in left.items())


def one_site_density(
    state: dict[tuple[int, ...], complex], wire: int
) -> np.ndarray:
    grouped: dict[tuple[int, ...], list[complex]] = {}
    for bits, amplitude in state.items():
        rest = bits[:wire] + bits[wire + 1 :]
        grouped.setdefault(rest, [0.0j, 0.0j])[bits[wire]] += amplitude
    density = np.zeros((2, 2), dtype=complex)
    for vector in grouped.values():
        column = np.asarray(vector, dtype=complex)
        density += np.outer(column, column.conj())
    return density


@lru_cache(maxsize=None)
def branch_archive_certificate(erase_target: bool = False) -> dict[str, object]:
    events = witness_events()
    sites, _, _, target_sites = witness_basis_data()
    site_index = {site: index for index, site in enumerate(sites)}
    columns: dict[tuple[int, object], list[tuple[tuple[int, int], int, dict, float]]] = defaultdict(list)
    lock_residual = 0.0
    for order in (0, 1):
        dilation = joint_dilation_actions(events, order)
        archive = joint_archive_actions(events)
        for matter in product((0, 1), repeat=2):
            for target_index in range(1 << len(target_sites)):
                bits, _ = witness_input(matter, target_index)
                dilated = block86.apply_physical_actions(
                    {bits: 1.0 + 0.0j}, dilation, site_index
                )
                for branch in JOINT_BRANCHES:
                    projected = project_branch(
                        dilated, site_index, events, branch
                    )
                    if not projected:
                        continue
                    output = block86.apply_physical_actions(
                        projected, archive, site_index
                    )
                    if erase_target:
                        erase_site = event_site(events[0], block71.STARTS["P"])
                        output = erase_wire(output, site_index[erase_site])
                    probability = state_probability(output)
                    if probability < TOL:
                        continue
                    normalized = normalized_state(output)
                    for event, (matter_out, bit_out) in zip(events, branch):
                        locks = (
                            (event_site(event, block71.HEAD_SITE), block71.PMINUS),
                            (
                                event_site(event, block71.ROOT_SITE),
                                block71.P1 if matter_out else block71.P0,
                            ),
                            (
                                event_site(event, block71.META_SITE),
                                block71.P1 if bit_out else block71.P0,
                            ),
                        )
                        for site, expected in locks:
                            lock_residual = max(
                                lock_residual,
                                float(
                                    np.linalg.norm(
                                        one_site_density(normalized, site_index[site])
                                        - expected
                                    )
                                ),
                            )
                    columns[(order, branch)].append(
                        (matter, target_index, output, probability)
                    )
    ranks: list[int] = []
    gram_residuals: list[float] = []
    probability_spreads: list[float] = []
    probabilities: list[float] = []
    matter_support_failures = target_count_failures = 0
    for key in sorted(columns, key=str):
        entries = columns[key]
        matters = {entry[0] for entry in entries}
        matter_support_failures += len(matters) != 1
        target_count_failures += len(entries) != 64
        entries = sorted(entries, key=lambda entry: entry[1])
        normalized = [normalized_state(entry[2]) for entry in entries]
        gram = np.asarray(
            [
                [sparse_inner(left, right) for right in normalized]
                for left in normalized
            ],
            dtype=complex,
        )
        gram_residuals.append(float(np.linalg.norm(gram - np.eye(len(entries)))))
        ranks.append(int(np.linalg.matrix_rank(gram, tol=TOL)))
        weights = [entry[3] for entry in entries]
        probabilities.extend(weights)
        probability_spreads.append(max(weights) - min(weights))
    return {
        "nonzero_branch_maps": len(columns),
        "rank_set": tuple(sorted(set(ranks))),
        "minimum_rank": min(ranks),
        "maximum_gram_residual": max(gram_residuals),
        "maximum_probability_spread_across_targets": max(probability_spreads),
        "minimum_conditional_branch_weight": min(probabilities),
        "maximum_conditional_branch_weight": max(probabilities),
        "minimum_actual_event_probability": HAZARD * 0.5 * min(probabilities),
        "maximum_actual_event_probability": HAZARD * 0.5 * max(probabilities),
        "matter_support_failures": matter_support_failures,
        "target_count_failures": target_count_failures,
        "target_qubits": len(target_sites),
        "archive_support_overlap": len(
            archive_support(events[0]) & archive_support(events[1])
        ),
        "lock_residual": lock_residual,
        "external_reference_preserved_by_branch_isometries": not erase_target,
        "erased_target": erase_target,
    }


@lru_cache(maxsize=None)
def order_environment_certificate(collapse_order: bool = False) -> dict[str, object]:
    events = witness_events()
    sites, _, _, _ = witness_basis_data()
    site_index = {site: index for index, site in enumerate(sites)}
    distributions: dict[tuple[int, tuple[int, int]], dict[object, float]] = {}
    normalization_residual = 0.0
    for order in (0, 1):
        for matter in product((0, 1), repeat=2):
            bits, _ = witness_input(matter, 0)
            dilated = block86.apply_physical_actions(
                {bits: 1.0 + 0.0j},
                joint_dilation_actions(events, order),
                site_index,
            )
            distribution = {
                branch: state_probability(
                    project_branch(dilated, site_index, events, branch)
                )
                for branch in JOINT_BRANCHES
            }
            distributions[(order, matter)] = distribution
            normalization_residual = max(
                normalization_residual, abs(sum(distribution.values()) - 1.0)
            )
    televisions: dict[tuple[int, int], float] = {}
    for matter in product((0, 1), repeat=2):
        left = distributions[(0, matter)]
        right = distributions[(1, matter)]
        televisions[matter] = 0.5 * sum(
            abs(left[branch] - right[branch]) for branch in JOINT_BRANCHES
        )

    relabel_cases = relabel_failures = 0
    swapped = (events[1], events[0])
    for order in (0, 1):
        for matter in product((0, 1), repeat=2):
            bits, _ = witness_input(matter, 0)
            original_dilated = block86.apply_physical_actions(
                {bits: 1.0 + 0.0j},
                joint_dilation_actions(events, order),
                site_index,
            )
            swapped_dilated = block86.apply_physical_actions(
                {bits: 1.0 + 0.0j},
                joint_dilation_actions(swapped, 1 - order),
                site_index,
            )
            for branch in JOINT_BRANCHES:
                original = project_branch(
                    original_dilated, site_index, events, branch
                )
                transformed = project_branch(
                    swapped_dilated,
                    site_index,
                    swapped,
                    (branch[1], branch[0]),
                )
                relabel_failures += block72.state_residual(original, transformed) >= TOL
                relabel_cases += 1
    if collapse_order:
        relabel_failures += 1
    return {
        "order_labels": 1 if collapse_order else 2,
        "television_distances": tuple(sorted(televisions.items())),
        "maximum_normalization_residual": normalization_residual,
        "positive_order_dependence_cases": sum(
            value > TOL for value in televisions.values()
        ),
        "order_independent_cases": sum(
            value <= TOL for value in televisions.values()
        ),
        "maximum_television": max(televisions.values()),
        "relabel_cases": relabel_cases,
        "relabel_failures": relabel_failures,
        "equal_order_coin": True,
        "order_label_load_bearing": max(televisions.values()) > TOL,
        "collapsed_order": collapse_order,
    }


def compile_joint_word(
    order: int, *, drop_swapback: bool = False
) -> dict[str, object]:
    events = witness_events()
    all_semantic = semantic_support(events[0]) | semantic_support(events[1])
    actions: list[block72.PhysicalAction] = []
    paths: list[tuple[block71.Coord, ...]] = []
    macro_residual = 0.0
    macro_cases = 0
    dropped = False
    for event in ordered_events(events, order):
        for gate in block71.dilation_word():
            should_drop = False
            if drop_swapback and len(gate.wires) == 2 and not dropped:
                endpoints = tuple(
                    event_site(event, block71.STARTS[ROLES[wire]])
                    for wire in gate.wires
                )
                candidate_path = block90.pair_path(
                    endpoints[0], endpoints[1], all_semantic
                )
                should_drop = len(candidate_path) > 2
            routed, path = block90.routed_gate_actions(
                gate,
                event,
                all_semantic,
                drop_swapback=should_drop,
            )
            actions.extend(routed)
            if len(gate.wires) == 2:
                residual, cases = block90.two_gate_macro_residual(
                    path, gate.matrix, drop_swapback=should_drop
                )
                macro_residual = max(macro_residual, residual)
                macro_cases += cases
                paths.append(path)
                dropped = dropped or should_drop
    for event in events:
        actions.append(
            block72.PhysicalAction(
                "archive_head_H",
                (event_site(event, block71.STARTS["P"]),),
                block71.H,
            )
        )
        for role, target in (
            ("P", block71.HEAD_SITE),
            ("M", block71.ROOT_SITE),
            ("B", block71.META_SITE),
        ):
            routed, path = block90.endpoint_swap_actions(
                event_site(event, block71.STARTS[role]),
                event_site(event, target),
                all_semantic,
            )
            actions.extend(routed)
            residual, cases = block90.endpoint_swap_residual(path)
            macro_residual = max(macro_residual, residual)
            macro_cases += cases
            paths.append(path)
    action_tuple = tuple(actions)
    support = frozenset(
        site for action in action_tuple for site in action.sites
    )
    return {
        "actions": action_tuple,
        "paths": tuple(paths),
        "path_count": len(paths),
        "maximum_path_vertices": max(map(len, paths)),
        "primitives": len(action_tuple),
        "support": support,
        "support_sites": len(support),
        "macro_residual": macro_residual,
        "macro_cases": macro_cases,
        "nn_failures": sum(
            len(action.sites) == 2 and block71.distance(*action.sites) != 1
            for action in action_tuple
        ),
        "dropped_swapback": dropped,
    }


def ideal_joint_word(order: int) -> tuple[block72.PhysicalAction, ...]:
    events = witness_events()
    return joint_dilation_actions(events, order) + joint_archive_actions(events)


def physical_semantic_equivalence(
    compiler: dict[str, object], order: int
) -> dict[str, object]:
    actions = compiler["actions"]
    semantic = semantic_support(witness_events()[0]) | semantic_support(
        witness_events()[1]
    )
    support = tuple(sorted(set(compiler["support"]) | set(semantic)))
    site_index = {site: index for index, site in enumerate(support)}
    background = tuple(site for site in support if site not in semantic)
    maximum = 0.0
    background_failures = 0
    cases = 0
    _, requirements, matter_sites, target_sites = witness_basis_data()
    for matter in product((0, 1), repeat=2):
        for target_index in range(1 << len(target_sites)):
            bits = [0] * len(support)
            values = dict(requirements)
            values[matter_sites[0]] = matter[0]
            values[matter_sites[1]] = matter[1]
            for site, value in values.items():
                bits[site_index[site]] = value
            for wire, site in enumerate(target_sites):
                bits[site_index[site]] = (target_index >> wire) & 1
            for site in background:
                bits[site_index[site]] = (
                    abs(site[0]) + 2 * abs(site[1]) + 3 * abs(site[2])
                ) % 2
            state = {tuple(bits): 1.0 + 0.0j}
            observed = block86.apply_physical_actions(
                state, actions, site_index
            )
            expected = block86.apply_physical_actions(
                state, ideal_joint_word(order), site_index
            )
            maximum = max(
                maximum, block72.state_residual(observed, expected)
            )
            background_failures += any(
                any(
                    output[site_index[site]] != bits[site_index[site]]
                    for site in background
                )
                for output in observed
            )
            cases += 1
    return {
        "basis_cases": cases,
        "background_sites": len(background),
        "maximum_residual": maximum,
        "background_failures": background_failures,
    }


@lru_cache(maxsize=None)
def compiler_certificate(drop_swapback: bool = False) -> dict[str, object]:
    compilers = tuple(
        compile_joint_word(order, drop_swapback=drop_swapback and order == 0)
        for order in (0, 1)
    )
    equivalences = tuple(
        physical_semantic_equivalence(compiler, order)
        for order, compiler in enumerate(compilers)
    )
    return {
        "orders": 2,
        "primitives": tuple(item["primitives"] for item in compilers),
        "support_sites": tuple(item["support_sites"] for item in compilers),
        "supports_equal": compilers[0]["support"] == compilers[1]["support"],
        "corridor": compilers[0]["support"] | compilers[1]["support"],
        "corridor_sites": len(compilers[0]["support"] | compilers[1]["support"]),
        "path_counts": tuple(item["path_count"] for item in compilers),
        "maximum_path_vertices": max(
            item["maximum_path_vertices"] for item in compilers
        ),
        "macro_cases": sum(item["macro_cases"] for item in compilers),
        "macro_residual": max(item["macro_residual"] for item in compilers),
        "nn_failures": sum(item["nn_failures"] for item in compilers),
        "basis_cases": sum(item["basis_cases"] for item in equivalences),
        "maximum_semantic_residual": max(
            item["maximum_residual"] for item in equivalences
        ),
        "background_sites": tuple(
            item["background_sites"] for item in equivalences
        ),
        "background_failures": sum(
            item["background_failures"] for item in equivalences
        ),
        "dropped_swapback": any(
            item["dropped_swapback"] for item in compilers
        ),
        "outcome_projection_nn_compiled": False,
        "global_route_atlas_supplied": False,
    }


@dataclass(frozen=True)
class JointLedger:
    records: tuple[tuple[block71.Coord, object], ...]
    resources: tuple[tuple[str, str], ...]
    archives: tuple[str, ...]
    sources: tuple[tuple[block71.Coord, block71.Coord], ...]
    reserved_corridor: tuple[block71.Coord, ...]
    environment_labels: tuple[tuple[object, ...], ...]


def canonical_joint_ledger(
    records: dict[block71.Coord, object],
    resources: dict[str, str],
    archives: set[str],
    sources: set[tuple[block71.Coord, block71.Coord]],
    reserved_corridor: set[block71.Coord],
    environment_labels: set[tuple[object, ...]],
) -> JointLedger:
    return JointLedger(
        tuple(sorted(records.items())),
        tuple(sorted(resources.items())),
        tuple(sorted(archives)),
        tuple(sorted(sources)),
        tuple(sorted(reserved_corridor)),
        tuple(sorted(environment_labels, key=str)),
    )


def initial_joint_ledger(corridor: frozenset[block71.Coord]) -> JointLedger:
    return canonical_joint_ledger(
        {block89.SENTINEL: block71.KPLUS},
        {"left": "ready", "right": "ready", "order_coin": "ready"},
        set(),
        set(),
        set(corridor),
        set(),
    )


def apply_joint_branch(
    ledger: JointLedger,
    branch: object,
    corridor: frozenset[block71.Coord],
    *,
    overwrite: bool = False,
    ignore_ambient_record: bool = False,
    erase_source: bool = False,
) -> tuple[str, JointLedger]:
    records = dict(ledger.records)
    resources = dict(ledger.resources)
    archives = set(ledger.archives)
    sources = set(ledger.sources)
    reservation = set(ledger.reserved_corridor)
    labels = set(ledger.environment_labels)
    guard = (
        semantic_support(witness_events()[0])
        | semantic_support(witness_events()[1])
        if ignore_ambient_record
        else corridor
    )
    unavailable = any(
        resources.get(key) != "ready"
        for key in ("left", "right", "order_coin")
    )
    occupied = not records.keys().isdisjoint(guard)
    unreserved = reservation != set(corridor)
    if unavailable or occupied or unreserved:
        if not (overwrite and isinstance(branch, tuple)):
            return "guard_refusal", ledger
    if not isinstance(branch, tuple):
        return str(branch), ledger
    order, left_branch, right_branch = branch
    writes = block89.branch_writes(witness_events()[0], left_branch)
    writes.update(block89.branch_writes(witness_events()[1], right_branch))
    if not records.keys().isdisjoint(writes) and not overwrite:
        return "guard_refusal", ledger
    records.update(writes)
    resources = {key: "spent" for key in resources}
    archives.update(("left", "right"))
    if not erase_source:
        for event in witness_events():
            sources.add(
                (
                    event_site(event, block71.ROOT_SITE),
                    event_site(event, block71.HEAD_SITE),
                )
            )
    labels.add((order, left_branch, right_branch))
    return "event", canonical_joint_ledger(
        records, resources, archives, sources, set(), labels
    )


def marginal(
    state: dict[tuple[int, ...], complex], wire: int
) -> tuple[float, float]:
    return tuple(
        float(
            sum(
                abs(amplitude) ** 2
                for bits, amplitude in state.items()
                if bits[wire] == value
            )
        )
        for value in (0, 1)
    )


@lru_cache(maxsize=None)
def ledger_corridor_certificate(
    overwrite: bool = False,
    ignore_ambient_record: bool = False,
    erase_source: bool = False,
) -> dict[str, object]:
    compiler = compiler_certificate(False)
    corridor = compiler["corridor"]
    event_failures = decode_failures = source_failures = 0
    representative: JointLedger | None = None
    for order in (0, 1):
        for left_branch, right_branch in JOINT_BRANCHES:
            initial = initial_joint_ledger(corridor)
            status, output = apply_joint_branch(
                initial,
                (order, left_branch, right_branch),
                corridor,
                overwrite=overwrite,
                erase_source=erase_source,
            )
            event_failures += status != "event"
            decode_failures += len(block71.find_packets(dict(output.records))) != 2
            source_failures += len(output.sources) != (0 if erase_source else 2)
            representative = output
    assert representative is not None

    event_key = (0, (0, 1), (1, 0))
    initial = initial_joint_ledger(corridor)
    no_status, no_output = apply_joint_branch(initial, "no_event", corridor)
    retry_status, retry = apply_joint_branch(no_output, event_key, corridor)
    replay_status, replay = apply_joint_branch(retry, event_key, corridor)

    write_site = event_site(witness_events()[0], block71.HEAD_SITE)
    occupied_records = dict(initial.records)
    occupied_records[write_site] = block71.K1
    occupied = canonical_joint_ledger(
        occupied_records,
        dict(initial.resources),
        set(initial.archives),
        set(initial.sources),
        set(initial.reserved_corridor),
        set(initial.environment_labels),
    )
    occupied_status, occupied_output = apply_joint_branch(
        occupied,
        event_key,
        corridor,
        overwrite=overwrite,
    )

    ambient_site = (-2, -1, 0)
    ambient_records = dict(initial.records)
    ambient_records[ambient_site] = block71.K1
    ambient = canonical_joint_ledger(
        ambient_records,
        dict(initial.resources),
        set(initial.archives),
        set(initial.sources),
        set(initial.reserved_corridor),
        set(initial.environment_labels),
    )
    ambient_status, ambient_output = apply_joint_branch(
        ambient,
        event_key,
        corridor,
        ignore_ambient_record=ignore_ambient_record,
    )

    physical = compile_joint_word(0)["actions"]
    support = tuple(sorted(corridor))
    site_index = {site: index for index, site in enumerate(support)}
    requirements = joint_ready_requirements(witness_events())
    bits = [requirements.get(site, 0) for site in support]
    bits[site_index[ambient_site]] = 1
    state = {tuple(bits): 1.0 + 0.0j}
    touches = tuple(
        (index, action)
        for index, action in enumerate(physical)
        if ambient_site in action.sites
    )
    first_index, first_action = touches[0]
    before = block86.apply_physical_actions(
        state, physical[:first_index], site_index
    )
    after = block86.apply_physical_actions(
        before, (first_action,), site_index
    )
    final = block86.apply_physical_actions(state, physical, site_index)
    ambient_wire = site_index[ambient_site]

    continuity_failures = 0
    for root, head in representative.sources:
        delta = {root: -1, head: 1}
        boundary = {root: 1, head: -1}
        continuity_failures += any(
            delta[site] + boundary[site] for site in delta
        )
    return {
        "event_branches": 32,
        "event_failures": event_failures,
        "decode_failures": decode_failures,
        "source_failures": source_failures,
        "records": len(representative.records) - 1,
        "resources_spent": sum(
            value == "spent" for _, value in representative.resources
        ),
        "archives": len(representative.archives),
        "sources": len(representative.sources),
        "environment_labels": len(representative.environment_labels),
        "reservation_released": len(representative.reserved_corridor) == 0,
        "corridor_sites": len(corridor),
        "no_event_status": no_status,
        "no_event_identity": no_output == initial,
        "retry_status": retry_status,
        "replay_status": replay_status,
        "replay_identity": replay == retry,
        "occupied_write_status": occupied_status,
        "occupied_write_identity": occupied_output == occupied,
        "ambient_site": ambient_site,
        "ambient_outside_semantic": ambient_site
        not in (
            semantic_support(witness_events()[0])
            | semantic_support(witness_events()[1])
        ),
        "ambient_inside_corridor": ambient_site in corridor,
        "ambient_status": ambient_status,
        "ambient_identity": ambient_output == ambient,
        "first_touch_zero_index": first_index,
        "first_touch_one_index": first_index + 1,
        "first_touch_kind": first_action.kind,
        "first_touch_sites": first_action.sites,
        "ambient_before": marginal(before, ambient_wire),
        "ambient_after": marginal(after, ambient_wire),
        "ambient_final": marginal(final, ambient_wire),
        "continuity_failures": continuity_failures,
        "overwriting": overwrite,
        "ignored_ambient_record": ignore_ambient_record,
        "erased_source": erase_source,
    }


def resource_boundary_certificate(
    erase_source: bool = False, fake_renewal: bool = False
) -> dict[str, object]:
    ledger = ledger_corridor_certificate(False, False, erase_source)
    spent = ledger["resources_spent"]
    if fake_renewal:
        spent = 0
    return {
        "records": ledger["records"],
        "archives": ledger["archives"],
        "sources": ledger["sources"],
        "continuity_failures": ledger["continuity_failures"],
        "spent_resources": spent,
        "event_packets_spent": 2 if spent else 0,
        "order_coin_spent": 1 if spent else 0,
        "joint_environment_outcomes": 34,
        "binary_environment_qubits": 6,
        "clean_genesis_supplied": False,
        "renewal_supplied": fake_renewal,
        "outcome_pointer_nn_compiled": False,
        "actual_draw_supplied": False,
        "hazard_derived": False,
        "global_corridor_protocol_supplied": False,
        "global_route_atlas_supplied": False,
        "physical_rate_supplied": False,
        "energy_action_supplied": False,
        "gravity_supplied": False,
    }


def boundary_surface_ok(false_progress: bool = False) -> bool:
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
        "34-outcome",
        "445",
        "474",
        "two trapped route geometries remain open",
        "global Record-aware corridor protocol remains open",
        "clean-resource genesis and renewal remain open",
        "source/action typing and gravity remain open",
        "no TOE percentage movement",
        "not an approved primitive",
    )
    return not false_progress and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom",
            "miss_one_pair",
            "break_completeness",
            "erase_target",
            "collapse_order",
            "drop_swapback",
            "overwrite",
            "ignore_ambient_record",
            "erase_source",
            "fake_renewal",
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
        and authority["canonical_ids"]
        == (
            "minimal_axioms",
            "scale_reference_primitive",
            "kinetic_isotropy_primitive",
            "realized_state_primitive",
        )
        and authority["sources_match"]
        and authority["forbidden_phrase_hits"] == 0
        and authority["current_contract"]
        and authority["current_inputs_match"]
        and authority["historical_parents_match"]
        and authority["parent_hashes"] == PARENT_SHA256
        and not authority["forced_stale"]
    )
    checks.check(
        "A-current-authority-and-exact-Block90-parent",
        authority_ok,
        f"axiom={str(authority['axiom_sha256'])[:12]}; no joint collision instrument, order coin, corridor protocol, or renewal is registered",
    )

    census = census_certificate(mutation == "miss_one_pair")
    census_ok = (
        census["semantic_overlap"] == 921
        and census["archive_disjoint"] == 447
        and census["archive_overlap"] == 474
        and census["archive_overlap_histogram"]
        == ((0, 447), (1, 432), (2, 40), (3, 1), (4, 1))
        and census["dilation_order_checks"] == 1842
        and census["dilation_failures"] == 0
        and census["route_checks"] == 9834
        and census["route_failures"] == 2
        and census["fully_routable"] == 445
        and len(census["route_failure_geometries"]) == 2
        and not census["forced_miss"]
    )
    checks.check(
        "B-full-semantic-overlap-census-and-joint-dilation-normalization",
        census_ok,
        f"both dilation orders normalize on {census['semantic_overlap']} placements/{census['dilation_order_checks']} order checks; 447 archive-disjoint split into {census['fully_routable']} routed and {census['route_failures']} trapped, while 474 archive-overlap placements remain",
    )

    completeness = completeness_certificate(mutation == "break_completeness")
    completeness_ok = (
        completeness["outcomes"] == 34
        and completeness["order_labels"] == 2
        and completeness["joint_event_labels_per_order"] == 16
        and completeness["semantic_sites"] == 15
        and completeness["full_dimension"] == 32768
        and completeness["ready_rank"] == 256
        and completeness["refusal_rank"] == 32512
        and abs(completeness["no_event_weight"] - 2 / 3) < TOL
        and abs(completeness["joint_event_weight"] - 1 / 3) < TOL
        and completeness["order_basis_cases"] == 512
        and completeness["maximum_order_completeness_residual"] < TOL
        and completeness["maximum_full_completeness_residual"] < TOL
        and completeness["refusal_failures"] == 0
        and completeness["binary_environment_qubits"] == 6
        and not completeness["break_completeness"]
    )
    checks.check(
        "C-normalized-34-outcome-joint-order-environment-instrument",
        completeness_ok,
        f"refusal rank {completeness['refusal_rank']} plus no-event weight 2/3 and 2x16 joint branches at event weight 1/3 close {completeness['order_basis_cases']} ready-order rows to residual {completeness['maximum_full_completeness_residual']:.2e}",
    )

    archive = branch_archive_certificate(mutation == "erase_target")
    archive_ok = (
        archive["nonzero_branch_maps"] == 32
        and archive["rank_set"] == (64,)
        and archive["minimum_rank"] == 64
        and archive["maximum_gram_residual"] < TOL
        and archive["maximum_probability_spread_across_targets"] < TOL
        and archive["minimum_conditional_branch_weight"] > 0
        and archive["maximum_conditional_branch_weight"] < 1
        and archive["matter_support_failures"] == 0
        and archive["target_count_failures"] == 0
        and archive["target_qubits"] == 6
        and archive["archive_support_overlap"] == 0
        and archive["lock_residual"] < TOL
        and archive["external_reference_preserved_by_branch_isometries"]
        and not archive["erased_target"]
    )
    checks.check(
        "D-all-32-event-maps-preserve-six-target-reference-and-locks",
        archive_ok,
        f"32/32 nonzero maps have rank {archive['minimum_rank']}, six-target Gram residual {archive['maximum_gram_residual']:.2e}, six-lock residual {archive['lock_residual']:.2e}, and conditional weights [{archive['minimum_conditional_branch_weight']:.9f},{archive['maximum_conditional_branch_weight']:.9f}]",
    )

    order = order_environment_certificate(mutation == "collapse_order")
    television = dict(order["television_distances"])
    order_ok = (
        order["order_labels"] == 2
        and order["maximum_normalization_residual"] < TOL
        and order["positive_order_dependence_cases"] == 2
        and order["order_independent_cases"] == 2
        and abs(television[(0, 0)] - 0.19090088708030317) < TOL
        and abs(television[(0, 1)] - 0.07636035483212167) < TOL
        and television[(1, 0)] < TOL
        and television[(1, 1)] < TOL
        and order["relabel_cases"] == 128
        and order["relabel_failures"] == 0
        and order["equal_order_coin"]
        and order["order_label_load_bearing"]
        and not order["collapsed_order"]
    )
    checks.check(
        "E-load-bearing-equal-order-coin-and-event-relabel-covariance",
        order_ok,
        f"matter TVs are {television[(0, 0)]:.9f}, {television[(0, 1)]:.9f}, {television[(1, 0)]:.2e}, {television[(1, 1)]:.2e}; {order['relabel_cases']} order/branch relabel checks have {order['relabel_failures']} failures",
    )

    compiler = compiler_certificate(mutation == "drop_swapback")
    compiler_ok = (
        compiler["orders"] == 2
        and compiler["primitives"] == (374, 374)
        and compiler["support_sites"] == (52, 52)
        and compiler["supports_equal"]
        and compiler["corridor_sites"] == 52
        and compiler["path_counts"] == (46, 46)
        and compiler["maximum_path_vertices"] == 9
        and compiler["macro_residual"] < TOL
        and compiler["nn_failures"] == 0
        and compiler["basis_cases"] == 512
        and compiler["maximum_semantic_residual"] < TOL
        and compiler["background_sites"] == (37, 37)
        and compiler["background_failures"] == 0
        and not compiler["dropped_swapback"]
        and not compiler["outcome_projection_nn_compiled"]
        and not compiler["global_route_atlas_supplied"]
    )
    checks.check(
        "F-two-exact-374-primitive-NN-words-on-one-guarded-corridor",
        compiler_ok,
        f"both orders use 374 primitives/46 paths on the same 52-site corridor and match all {compiler['basis_cases']} order/basis rows at residual {compiler['maximum_semantic_residual']:.2e}; outcome projection and the global atlas remain open",
    )

    ledger = ledger_corridor_certificate(
        mutation == "overwrite",
        mutation == "ignore_ambient_record",
        False,
    )
    ledger_ok = (
        ledger["event_branches"] == 32
        and ledger["event_failures"] == 0
        and ledger["decode_failures"] == 0
        and ledger["source_failures"] == 0
        and ledger["records"] == 6
        and ledger["resources_spent"] == 3
        and ledger["archives"] == 2
        and ledger["sources"] == 2
        and ledger["environment_labels"] == 1
        and ledger["reservation_released"]
        and ledger["corridor_sites"] == 52
        and ledger["no_event_status"] == "no_event"
        and ledger["no_event_identity"]
        and ledger["retry_status"] == "event"
        and ledger["replay_status"] == "guard_refusal"
        and ledger["replay_identity"]
        and ledger["occupied_write_status"] == "guard_refusal"
        and ledger["occupied_write_identity"]
        and ledger["ambient_site"] == (-2, -1, 0)
        and ledger["ambient_outside_semantic"]
        and ledger["ambient_inside_corridor"]
        and ledger["ambient_status"] == "guard_refusal"
        and ledger["ambient_identity"]
        and ledger["first_touch_zero_index"] == 34
        and ledger["first_touch_one_index"] == 35
        and ledger["first_touch_kind"] == "SWAP"
        and ledger["first_touch_sites"]
        == ((-1, -1, 0), (-2, -1, 0))
        and abs(ledger["ambient_before"][0]) < TOL
        and abs(ledger["ambient_before"][1] - 1) < TOL
        and abs(ledger["ambient_after"][0] - 0.5) < TOL
        and abs(ledger["ambient_after"][1] - 0.5) < TOL
        and abs(ledger["ambient_final"][0]) < TOL
        and abs(ledger["ambient_final"][1] - 1) < TOL
        and ledger["continuity_failures"] == 0
        and not ledger["overwriting"]
        and not ledger["ignored_ambient_record"]
    )
    checks.check(
        "G-complete-joint-ledger-depth-two-and-52-site-corridor-guard",
        ledger_ok,
        f"all 32 event branches write {ledger['records']} Records, spend three resources, archive two events, add two sources, and release the 52-site reservation; ambient K1 primitive 34 disturbance is blocked by exact identity refusal",
    )

    resources = resource_boundary_certificate(
        mutation == "erase_source", mutation == "fake_renewal"
    )
    resource_ok = (
        resources["records"] == 6
        and resources["archives"] == 2
        and resources["sources"] == 2
        and resources["continuity_failures"] == 0
        and resources["spent_resources"] == 3
        and resources["event_packets_spent"] == 2
        and resources["order_coin_spent"] == 1
        and resources["joint_environment_outcomes"] == 34
        and resources["binary_environment_qubits"] == 6
        and not resources["clean_genesis_supplied"]
        and not resources["renewal_supplied"]
        and not resources["outcome_pointer_nn_compiled"]
        and not resources["actual_draw_supplied"]
        and not resources["hazard_derived"]
        and not resources["global_corridor_protocol_supplied"]
        and not resources["global_route_atlas_supplied"]
        and not resources["physical_rate_supplied"]
        and not resources["energy_action_supplied"]
        and not resources["gravity_supplied"]
    )
    checks.check(
        "H-order-coin-source-and-physical-law-boundary",
        resource_ok,
        "two event packets plus one load-bearing order coin are spent and two source edges conserve exactly; coin genesis/renewal, actual outcome, hazard derivation, global corridor/atlas, cadence, energy/action, and gravity remain unsupplied",
    )

    boundary_ok = boundary_surface_ok(mutation == "false_progress")
    checks.check(
        "I-bounded-joint-law-no-go-discipline-and-strict-TOE-accounting",
        boundary_ok,
        "the N1-N8 surface credits the 34-outcome witness and 445-case unitary-compiler reach while preserving the two trapped routes, 474 archive overlaps, 175 write overlaps, authority, actuality, renewal, gravity, retention, and no-score boundaries",
    )

    print(
        "METRICS semantic_overlap={} archive_disjoint={} fully_routable={} archive_overlap={} outcomes={} nonzero_maps={} branch_rank={} max_gram={:.3g} tv00={:.9g} tv01={:.9g} compiler_primitives={} corridor_sites={}".format(
            census["semantic_overlap"],
            census["archive_disjoint"],
            census["fully_routable"],
            census["archive_overlap"],
            completeness["outcomes"],
            archive["nonzero_branch_maps"],
            archive["minimum_rank"],
            archive["maximum_gram_residual"],
            television[(0, 0)],
            television[(0, 1)],
            compiler["primitives"][0],
            compiler["corridor_sites"],
        )
    )
    print("N5_RESOLUTION per_element: 34 environment outcomes, two order labels, 32 nonzero joint event maps, 58 logical dilation gates, 46 physical routes, two event packets, one order coin, and two source edges are typed")
    print("N5_RESOLUTION per_site: the exact witness has 15 semantic sites, six disjoint Record targets, six arbitrary archive qubits, 52 guarded physical sites, and 37 arbitrary unrecorded route-background factors")
    print("N5_RESOLUTION per_mode: refusal, no-event, both joint dilation orders, all 16 branch pairs per order, replay, retry, occupied write, ambient Record, archive-overlap, and trapped-route modes are checked")
    print("N5_RESOLUTION per_block: current authority, exact Block90 receipt, full semantic-overlap census, joint completeness, branch isometries, order covariance, NN compiler, complete ledger, corridor guard, resource debit, and source boundary are checked")
    print("N5_RESOLUTION lattice_wide: both dilation orders normalize on all 921 finite ready write-disjoint semantic-overlap placements; only 445 archive-disjoint placements receive the present cross-semantic unitary compiler skeleton, while outcome projection, global event sets, 474 archive overlaps, two trapped routes, 175 write overlaps, actuality, renewal, time, energy, and gravity are not claimed")
    print("BOUNDARY: a supplied equal order coin converts the exact sqrt(2) semantic noncommutation into one normalized 34-outcome transaction, and the present construction reaches 445 of 921 semantic-overlap placements on supplied Record-free corridors; two trapped route geometries, 474 archive-overlap placements, 175 write-overlap placements, the selected global law/atlas, outcome actuality, clean renewal, cadence, source/action typing, gravity, audit retention, obligation retirement, and TOE percentage movement remain open")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
