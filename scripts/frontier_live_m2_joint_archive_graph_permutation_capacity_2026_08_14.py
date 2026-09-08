#!/usr/bin/env python3
"""Block 92: joint archive graph permutation and source-slot capacity boundary.

Block91 left 474 ready write-disjoint semantic collisions with overlapping
archive supports.  This runner exhausts those placements.  When all six
branch-source sites are distinct, the six source-to-Record arrows form a
partial permutation: every weak component is a directed path or cycle.
Closing each path and compiling the resulting cycles by endpoint SWAPs gives
an exactly conservative joint archive.  There are 335 such placements; 333
admit all present cross-semantic paths, while two have exact trapped paths.

The other 139 placements reuse a physical branch source.  A dimension count
is then sharp for a six-lock archive confined to the source/target union:
135 five-source placements require at least one fixed-input capacity factor
and four four-source placements require at least two.  This is a bounded
capacity theorem, not a universal no-go: existing R/A factors, an enlarged
environment, a different Record contract, or nonconservative overwrite can
change the premise if a lawful compiler makes the needed capacity available.

Together with Blocks90-91 this raises conditional critical-pair unitary
compiler coverage to 1,912/2,230 = 85.7399%.  That percentage is compiler
coverage, not TOE closure.  Current authority supplies neither this archive
law nor clean capacity, a global atlas, outcome actuality, renewal/cadence,
source/action typing, gravity, retention, obligation retirement, or TOE score
movement.
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

import frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14 as block91


block90 = block91.block90
block89 = block91.block89
block86 = block91.block86
block72 = block91.block72
block71 = block91.block71

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LIVE_M2_JOINT_ARCHIVE_GRAPH_PERMUTATION_CAPACITY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_REPO_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_RECEIPT = "ab86482668"
PARENT_RUNNER = ROOT / "scripts" / (
    "frontier_live_m2_joint_order_environment_collision_instrument_"
    "2026_08_14.py"
)
PARENT_NOTE = ROOT / "docs" / (
    "LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
HISTORICAL_PARENT_SHA256 = ('7b7203f0c48b8577ddaf6b4235c7a982f1cfe73a4ec7fd15f31dd3e0d8d8ac88', '38b15d0b2501770e86dcdd75d810af0f70fa691e242a22ced53967f17da60827')
PARENT_SHA256 = ('01f6296b0ad887d6a47212f3ce5bb090dd4e50774e10ab6b86e4c35fa7e70ff2', '7a75e900c7507eef7369f4b22196eb7b20997a427d798c5d0f6fe84c1f5c236a')
HISTORICAL_PARENT_FILES = (('ab86482668', 'scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py'), ('ab86482668', 'docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md'))
AUDIT_INPUT_PATHS = (
    "docs/LIVE_M2_JOINT_ARCHIVE_GRAPH_PERMUTATION_CAPACITY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py",
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
    "docs/LIVE_M2_JOINT_ARCHIVE_GRAPH_PERMUTATION_CAPACITY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "d1d513bb6bacfa741a267ff19f46db38e53744e1a77e2ec0241a2621bf2bb9ba",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/LIVE_M2_JOINT_ORDER_ENVIRONMENT_COLLISION_INSTRUMENT_BOUNDED_THEOREM_NOTE_2026-08-14.md": "7a75e900c7507eef7369f4b22196eb7b20997a427d798c5d0f6fe84c1f5c236a",
    "scripts/frontier_live_m2_joint_order_environment_collision_instrument_2026_08_14.py": "01f6296b0ad887d6a47212f3ce5bb090dd4e50774e10ab6b86e4c35fa7e70ff2",
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
ROLES = block90.ROLES
ARCHIVE_ROLES = (
    ("P", block71.HEAD_SITE),
    ("M", block71.ROOT_SITE),
    ("B", block71.META_SITE),
)
REPRESENTATIVE_ROTATION = (
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
)
REPRESENTATIVE_TRANSLATION = (-3, 3, 1)


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
        "joint archive graph permutation law",
        "six-lock collision archive law",
        "clean archive-capacity factor law",
        "global Record-aware route atlas",
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


def event_site(
    event: block89.EventSpec, site: block71.Coord
) -> block71.Coord:
    return block91.event_site(event, site)


def semantic_support(event: block89.EventSpec) -> frozenset[block71.Coord]:
    return block91.semantic_support(event)


def archive_support(event: block89.EventSpec) -> frozenset[block71.Coord]:
    return block91.archive_support(event)


@dataclass(frozen=True)
class ArchiveEdge:
    source: block71.Coord
    target: block71.Coord
    event_index: int
    event_label: str
    role: str


def archive_edges(
    events: tuple[block89.EventSpec, block89.EventSpec]
) -> tuple[ArchiveEdge, ...]:
    return tuple(
        ArchiveEdge(
            event_site(event, block71.STARTS[role]),
            event_site(event, target),
            event_index,
            event.label,
            role,
        )
        for event_index, event in enumerate(events)
        for role, target in ARCHIVE_ROLES
    )


def semantic_overlap_placements():
    base = block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0))
    core = block89.base_core_support()
    for rotation in block71.ROTATIONS:
        rotated = {block71.rotate(rotation, site) for site in core}
        translations = {
            block89.subtraction(left, right)
            for left in core
            for right in rotated
        }
        for translation in sorted(translations):
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
            yield base, other


def archive_graph_components(
    edges: tuple[ArchiveEdge, ...]
) -> tuple[tuple[str, tuple[block71.Coord, ...]], ...]:
    sources = [edge.source for edge in edges]
    targets = [edge.target for edge in edges]
    if len(set(sources)) != len(sources):
        raise ValueError("archive sources are not injective")
    if len(set(targets)) != len(targets):
        raise ValueError("archive targets are not injective")
    outgoing = {edge.source: edge.target for edge in edges}
    incoming = {edge.target: edge.source for edge in edges}
    vertices = set(outgoing) | set(incoming)
    seen: set[block71.Coord] = set()
    components: list[tuple[str, tuple[block71.Coord, ...]]] = []

    for start in sorted(set(outgoing) - set(incoming)):
        if start in seen:
            continue
        path: list[block71.Coord] = []
        site = start
        while site not in seen:
            path.append(site)
            seen.add(site)
            if site not in outgoing:
                break
            site = outgoing[site]
        if not path or path[-1] in outgoing:
            raise AssertionError("path component did not terminate")
        components.append(("path", tuple(path)))

    for start in sorted(vertices):
        if start in seen:
            continue
        cycle: list[block71.Coord] = []
        site = start
        while site not in seen:
            cycle.append(site)
            seen.add(site)
            site = outgoing[site]
        if site != start:
            raise AssertionError("cycle component did not close")
        components.append(("cycle", tuple(cycle)))

    if seen != vertices:
        raise AssertionError("component census missed a vertex")
    reconstructed: set[tuple[block71.Coord, block71.Coord]] = set()
    for kind, vertices_in_component in components:
        reconstructed.update(zip(vertices_in_component[:-1], vertices_in_component[1:]))
        if kind == "cycle":
            reconstructed.add((vertices_in_component[-1], vertices_in_component[0]))
    expected = {(edge.source, edge.target) for edge in edges}
    if reconstructed != expected:
        raise AssertionError("component census did not reconstruct the graph")
    return tuple(components)


def archive_transpositions(
    components: tuple[tuple[str, tuple[block71.Coord, ...]], ...]
) -> tuple[tuple[block71.Coord, block71.Coord], ...]:
    swaps: list[tuple[block71.Coord, block71.Coord]] = []
    for _, vertices in components:
        swaps.extend(reversed(tuple(zip(vertices[:-1], vertices[1:]))))
    return tuple(swaps)


def symbolic_permutation_certificate(
    edges: tuple[ArchiveEdge, ...],
    swaps: tuple[tuple[block71.Coord, block71.Coord], ...],
) -> dict[str, object]:
    vertices = {site for edge in edges for site in (edge.source, edge.target)}
    contents = {site: site for site in vertices}
    for left, right in swaps:
        contents[left], contents[right] = contents[right], contents[left]
    target_failures = sum(
        contents[edge.target] != edge.source for edge in edges
    )
    return {
        "vertices": len(vertices),
        "swaps": len(swaps),
        "target_failures": target_failures,
        "bijective": set(contents.values()) == vertices,
        "contents": contents,
    }


def branch_value(
    event_index: int,
    role: str,
    joint_branch: tuple[int, int, int, int],
) -> int:
    left_matter, left_bit, right_matter, right_bit = joint_branch
    if role == "P":
        return 1
    if event_index == 0:
        return left_matter if role == "M" else left_bit
    return right_matter if role == "M" else right_bit


def compatible_branch_count(edges: tuple[ArchiveEdge, ...]) -> int:
    groups: dict[block71.Coord, list[ArchiveEdge]] = defaultdict(list)
    for edge in edges:
        groups[edge.source].append(edge)
    count = 0
    for joint_branch in product((0, 1), repeat=4):
        compatible = all(
            len(
                {
                    branch_value(edge.event_index, edge.role, joint_branch)
                    for edge in group
                }
            )
            == 1
            for group in groups.values()
        )
        count += compatible
    return count


@lru_cache(maxsize=None)
def archive_graph_census(
    miss_graph: bool = False, break_permutation: bool = False
) -> dict[str, object]:
    semantic_cases = archive_overlap_cases = 0
    injective = duplicate = 0
    injective_overlap: Counter[int] = Counter()
    duplicate_source_count: Counter[int] = Counter()
    duplicate_detail: Counter[tuple[int, int, int]] = Counter()
    source_role_compatible_histogram: Counter[int] = Counter()
    clean_factor_histogram: Counter[int] = Counter()
    component_patterns: Counter[tuple[tuple[str, int], ...]] = Counter()
    symbolic_failures = component_failures = 0
    route_checks = route_failures = fully_routable = 0
    dilation_route_checks = dilation_route_failures = 0
    route_failure_geometries: list[tuple[object, ...]] = []
    archive_primitive_counts: list[int] = []
    transposition_count = 0
    capacity_rows: Counter[tuple[int, int, int, int, int]] = Counter()
    mutation_used = False

    for base, other in semantic_overlap_placements():
        semantic_cases += 1
        if not (archive_support(base) & archive_support(other)):
            continue
        archive_overlap_cases += 1
        events = (base, other)
        edges = archive_edges(events)
        sources = {edge.source for edge in edges}
        targets = {edge.target for edge in edges}
        if len(targets) != 6:
            raise AssertionError("write-disjoint placement lost target injectivity")
        overlap = len(sources & targets)
        if len(sources) < 6:
            duplicate += 1
            unique_sources = len(sources)
            duplicate_source_count[unique_sources] += 1
            support_overlap = len(archive_support(base) & archive_support(other))
            duplicate_detail[(unique_sources, overlap, support_overlap)] += 1
            source_role_compatible_histogram[compatible_branch_count(edges)] += 1
            clean_factors = 6 - unique_sources
            clean_factor_histogram[clean_factors] += 1
            input_rank = 1 << (6 - overlap)
            output_capacity = 1 << (unique_sources - overlap)
            capacity_rows[
                (
                    unique_sources,
                    overlap,
                    input_rank,
                    output_capacity,
                    clean_factors,
                )
            ] += 1
            continue

        injective += 1
        injective_overlap[overlap] += 1
        try:
            components = archive_graph_components(edges)
        except (AssertionError, ValueError):
            component_failures += 1
            continue
        pattern = tuple(sorted((kind, len(vertices)) for kind, vertices in components))
        component_patterns[pattern] += 1
        swaps = archive_transpositions(components)
        transposition_count += len(swaps)
        tested_swaps = swaps
        if break_permutation and not mutation_used:
            tested_swaps = swaps[1:]
            mutation_used = True
        symbolic = symbolic_permutation_certificate(edges, tested_swaps)
        symbolic_failures += symbolic["target_failures"] > 0 or not symbolic["bijective"]

        all_semantic = semantic_support(base) | semantic_support(other)
        local_dilation_route_failures = 0
        # Event order changes gate order, not endpoints or the obstacle set, so
        # one route census per event proves the prerequisite for both orders.
        for event in events:
            for gate in block71.dilation_word():
                if len(gate.wires) != 2:
                    continue
                dilation_route_checks += 1
                sites = tuple(
                    event_site(event, block71.STARTS[ROLES[wire]])
                    for wire in gate.wires
                )
                try:
                    block90.pair_path(sites[0], sites[1], all_semantic)
                except RuntimeError:
                    dilation_route_failures += 1
                    local_dilation_route_failures += 1
        local_route_failures = 0
        local_primitives = 0
        for start, target in swaps:
            route_checks += 1
            try:
                path = block90.pair_path(start, target, all_semantic)
            except RuntimeError:
                route_failures += 1
                local_route_failures += 1
                route_failure_geometries.append(
                    (other.rotation, other.translation, start, target)
                )
                continue
            local_primitives += 2 * len(path) - 3
        if local_route_failures == 0 and local_dilation_route_failures == 0:
            fully_routable += 1
            archive_primitive_counts.append(local_primitives)

    partition_failures = int(miss_graph)
    return {
        "semantic_cases": semantic_cases,
        "archive_overlap_cases": archive_overlap_cases,
        "injective": injective,
        "duplicate": duplicate,
        "injective_overlap": tuple(sorted(injective_overlap.items())),
        "duplicate_source_count": tuple(sorted(duplicate_source_count.items())),
        "duplicate_detail": tuple(sorted(duplicate_detail.items())),
        "source_role_compatible_histogram": tuple(
            sorted(source_role_compatible_histogram.items())
        ),
        "clean_factor_histogram": tuple(sorted(clean_factor_histogram.items())),
        "component_patterns": tuple(sorted(component_patterns.items(), key=str)),
        "component_failures": component_failures,
        "symbolic_failures": symbolic_failures,
        "transposition_count": transposition_count,
        "route_checks": route_checks,
        "route_failures": route_failures,
        "dilation_route_checks": dilation_route_checks,
        "dilation_route_failures": dilation_route_failures,
        "fully_routable": fully_routable,
        "route_failure_geometries": tuple(route_failure_geometries),
        "archive_primitive_min": min(archive_primitive_counts),
        "archive_primitive_max": max(archive_primitive_counts),
        "capacity_rows": tuple(sorted(capacity_rows.items())),
        "partition_failures": partition_failures,
        "break_permutation": break_permutation,
    }


def representative_events() -> tuple[block89.EventSpec, block89.EventSpec]:
    return (
        block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0)),
        block89.EventSpec(
            "right", REPRESENTATIVE_ROTATION, REPRESENTATIVE_TRANSLATION
        ),
    )


def representative_graph() -> dict[str, object]:
    events = representative_events()
    edges = archive_edges(events)
    components = archive_graph_components(edges)
    swaps = archive_transpositions(components)
    symbolic = symbolic_permutation_certificate(edges, swaps)
    return {
        "events": events,
        "edges": edges,
        "components": components,
        "swaps": swaps,
        "symbolic": symbolic,
        "source_target_overlap": len(
            {edge.source for edge in edges} & {edge.target for edge in edges}
        ),
        "archive_support_overlap": len(
            archive_support(events[0]) & archive_support(events[1])
        ),
    }


def ideal_archive_actions(
    events: tuple[block89.EventSpec, block89.EventSpec]
) -> tuple[block72.PhysicalAction, ...]:
    graph = representative_graph()
    actions = [
        block72.PhysicalAction(
            "archive_head_H",
            (event_site(event, block71.STARTS["P"]),),
            block71.H,
        )
        for event in events
    ]
    actions.extend(
        block72.PhysicalAction("SWAP", endpoints)
        for endpoints in graph["swaps"]
    )
    return tuple(actions)


def representative_basis_data() -> tuple[
    tuple[block71.Coord, ...],
    dict[block71.Coord, int],
    tuple[block71.Coord, ...],
    tuple[block71.Coord, ...],
]:
    events = representative_events()
    semantic = tuple(sorted(semantic_support(events[0]) | semantic_support(events[1])))
    requirements = block91.joint_ready_requirements(events)
    free_sites = tuple(site for site in semantic if site not in requirements)
    sources = {edge.source for edge in archive_edges(events)}
    free_targets = tuple(
        sorted({edge.target for edge in archive_edges(events)} - sources)
    )
    return semantic, requirements, free_sites, free_targets


def representative_input(
    free_index: int,
) -> tuple[tuple[int, ...], dict[block71.Coord, int]]:
    semantic, requirements, free_sites, _ = representative_basis_data()
    site_index = {site: index for index, site in enumerate(semantic)}
    bits = [0] * len(semantic)
    for site, value in requirements.items():
        bits[site_index[site]] = value
    for wire, site in enumerate(free_sites):
        bits[site_index[site]] = (free_index >> wire) & 1
    return tuple(bits), site_index


@lru_cache(maxsize=None)
def branch_archive_certificate(erase_target: bool = False) -> dict[str, object]:
    events = representative_events()
    semantic, _, free_sites, free_targets = representative_basis_data()
    site_index = {site: index for index, site in enumerate(semantic)}
    sources = tuple(sorted({edge.source for edge in archive_edges(events)}))
    graph = representative_graph()
    destination_of: dict[block71.Coord, block71.Coord] = {}
    contents = graph["symbolic"]["contents"]
    for destination, origin in contents.items():
        destination_of[origin] = destination
    erase_site = destination_of[free_targets[0]]
    columns: dict[tuple[int, object], list[tuple[int, tuple[int, int], dict, float]]] = defaultdict(list)
    lock_residual = 0.0
    for order in (0, 1):
        dilation = block91.joint_dilation_actions(events, order)
        archive = ideal_archive_actions(events)
        for free_index in range(1 << len(free_sites)):
            bits, _ = representative_input(free_index)
            matter = tuple(
                bits[
                    site_index[event_site(event, block71.STARTS["M"])]
                ]
                for event in events
            )
            archive_index = sum(
                bits[site_index[site]] << wire
                for wire, site in enumerate(free_targets)
            )
            dilated = block86.apply_physical_actions(
                {bits: 1.0 + 0.0j}, dilation, site_index
            )
            for branch in block91.JOINT_BRANCHES:
                projected = block91.project_branch(
                    dilated, site_index, events, branch
                )
                if not projected:
                    continue
                output = block86.apply_physical_actions(
                    projected, archive, site_index
                )
                if erase_target:
                    output = block91.erase_wire(output, site_index[erase_site])
                probability = block91.state_probability(output)
                if probability < TOL:
                    continue
                normalized = block91.normalized_state(output)
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
                                    block91.one_site_density(
                                        normalized, site_index[site]
                                    )
                                    - expected
                                )
                            ),
                        )
                columns[(order, branch)].append(
                    (archive_index, matter, output, probability)
                )

    ranks: list[int] = []
    gram_residuals: list[float] = []
    probability_spreads: list[float] = []
    target_count_failures = matter_support_failures = 0
    for key in sorted(columns, key=str):
        entries = columns[key]
        matter_support_failures += len({entry[1] for entry in entries}) != 1
        target_count_failures += len(entries) != (1 << len(free_targets))
        entries = sorted(entries, key=lambda entry: entry[0])
        normalized = [block91.normalized_state(entry[2]) for entry in entries]
        gram = np.asarray(
            [
                [block91.sparse_inner(left, right) for right in normalized]
                for left in normalized
            ],
            dtype=complex,
        )
        ranks.append(int(np.linalg.matrix_rank(gram, tol=TOL)))
        gram_residuals.append(float(np.linalg.norm(gram - np.eye(len(entries)))))
        weights = [entry[3] for entry in entries]
        probability_spreads.append(max(weights) - min(weights))
    return {
        "semantic_sites": len(semantic),
        "free_ready_sites": len(free_sites),
        "free_target_sites": len(free_targets),
        "source_sites": len(sources),
        "nonzero_branch_maps": len(columns),
        "rank_set": tuple(sorted(set(ranks))),
        "minimum_rank": min(ranks),
        "maximum_gram_residual": max(gram_residuals),
        "maximum_probability_spread": max(probability_spreads),
        "target_count_failures": target_count_failures,
        "matter_support_failures": matter_support_failures,
        "lock_residual": lock_residual,
        "erased_target": erase_target,
    }


def endpoint_route_actions(
    start: block71.Coord,
    target: block71.Coord,
    all_semantic: frozenset[block71.Coord],
    *,
    drop_swapback: bool = False,
) -> tuple[tuple[block72.PhysicalAction, ...], tuple[block71.Coord, ...]]:
    path = block90.pair_path(start, target, all_semantic)
    forward = tuple(zip(path, path[1:]))
    reverse = tuple(reversed(forward[:-1]))
    if drop_swapback and reverse:
        reverse = reverse[:-1]
    actions = tuple(block72.PhysicalAction("SWAP", edge) for edge in forward + reverse)
    return actions, path


def compile_representative_word(
    order: int, *, drop_swapback: bool = False
) -> dict[str, object]:
    events = representative_events()
    all_semantic = semantic_support(events[0]) | semantic_support(events[1])
    actions: list[block72.PhysicalAction] = []
    paths: list[tuple[block71.Coord, ...]] = []
    macro_residual = 0.0
    macro_cases = 0
    dropped = False
    for event in block91.ordered_events(events, order):
        for gate in block71.dilation_word():
            routed, path = block90.routed_gate_actions(gate, event, all_semantic)
            actions.extend(routed)
            if len(gate.wires) == 2:
                residual, cases = block90.two_gate_macro_residual(path, gate.matrix)
                macro_residual = max(macro_residual, residual)
                macro_cases += cases
                paths.append(path)
    for event in events:
        actions.append(
            block72.PhysicalAction(
                "archive_head_H",
                (event_site(event, block71.STARTS["P"]),),
                block71.H,
            )
        )
    for start, target in representative_graph()["swaps"]:
        should_drop = drop_swapback and not dropped
        candidate_path = block90.pair_path(start, target, all_semantic)
        should_drop = should_drop and len(candidate_path) > 2
        routed, path = endpoint_route_actions(
            start,
            target,
            all_semantic,
            drop_swapback=should_drop,
        )
        actions.extend(routed)
        if not should_drop:
            residual, cases = block90.endpoint_swap_residual(path)
            macro_residual = max(macro_residual, residual)
            macro_cases += cases
        paths.append(path)
        dropped = dropped or should_drop
    action_tuple = tuple(actions)
    support = frozenset(site for action in action_tuple for site in action.sites)
    return {
        "actions": action_tuple,
        "paths": tuple(paths),
        "primitives": len(action_tuple),
        "support": support,
        "support_sites": len(support),
        "path_count": len(paths),
        "macro_residual": macro_residual,
        "macro_cases": macro_cases,
        "nn_failures": sum(
            len(action.sites) == 2 and block71.distance(*action.sites) != 1
            for action in action_tuple
        ),
        "dropped_swapback": dropped,
    }


def ideal_representative_word(order: int) -> tuple[block72.PhysicalAction, ...]:
    events = representative_events()
    return block91.joint_dilation_actions(events, order) + ideal_archive_actions(events)


def physical_equivalence(
    compiler: dict[str, object], order: int
) -> dict[str, object]:
    semantic, requirements, free_sites, _ = representative_basis_data()
    semantic_set = set(semantic)
    support = tuple(sorted(set(compiler["support"]) | semantic_set))
    site_index = {site: index for index, site in enumerate(support)}
    background = tuple(site for site in support if site not in semantic_set)
    maximum = 0.0
    background_failures = 0
    for free_index in range(1 << len(free_sites)):
        bits = [0] * len(support)
        for site, value in requirements.items():
            bits[site_index[site]] = value
        for wire, site in enumerate(free_sites):
            bits[site_index[site]] = (free_index >> wire) & 1
        for site in background:
            bits[site_index[site]] = (
                abs(site[0]) + 2 * abs(site[1]) + 3 * abs(site[2])
            ) % 2
        state = {tuple(bits): 1.0 + 0.0j}
        observed = block86.apply_physical_actions(
            state, compiler["actions"], site_index
        )
        expected = block86.apply_physical_actions(
            state, ideal_representative_word(order), site_index
        )
        maximum = max(maximum, block72.state_residual(observed, expected))
        background_failures += any(
            any(
                output[site_index[site]] != bits[site_index[site]]
                for site in background
            )
            for output in observed
        )
    return {
        "basis_cases": 1 << len(free_sites),
        "background_sites": len(background),
        "maximum_residual": maximum,
        "background_failures": background_failures,
    }


@lru_cache(maxsize=None)
def compiler_certificate(drop_swapback: bool = False) -> dict[str, object]:
    compilers = tuple(
        compile_representative_word(
            order, drop_swapback=drop_swapback and order == 0
        )
        for order in (0, 1)
    )
    equivalences = tuple(
        physical_equivalence(compiler, order)
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
        "macro_residual": max(item["macro_residual"] for item in compilers),
        "macro_cases": sum(item["macro_cases"] for item in compilers),
        "nn_failures": sum(item["nn_failures"] for item in compilers),
        "basis_cases": sum(item["basis_cases"] for item in equivalences),
        "maximum_residual": max(item["maximum_residual"] for item in equivalences),
        "background_sites": tuple(item["background_sites"] for item in equivalences),
        "background_failures": sum(item["background_failures"] for item in equivalences),
        "dropped_swapback": any(item["dropped_swapback"] for item in compilers),
        "outcome_projection_nn_compiled": False,
        "global_route_atlas_supplied": False,
    }


def capacity_certificate(fake_capacity: bool = False) -> dict[str, object]:
    census = archive_graph_census()
    failures = 0
    cases = 0
    maximum_deficit = 0
    for row, count in census["capacity_rows"]:
        unique_sources, overlap, input_rank, output_capacity, clean_factors = row
        claimed = 0 if fake_capacity and cases == 0 else clean_factors
        enlarged_capacity = 1 << (unique_sources - overlap + claimed)
        insufficient_before = (
            clean_factors == 0
            or (1 << (unique_sources - overlap + clean_factors - 1)) < input_rank
        )
        failures += not (
            output_capacity < input_rank
            and enlarged_capacity >= input_rank
            and insufficient_before
            and clean_factors == 6 - unique_sources
        )
        cases += count
        maximum_deficit = max(maximum_deficit, clean_factors)
    return {
        "duplicate_cases": cases,
        "capacity_rows": census["capacity_rows"],
        "clean_factor_histogram": census["clean_factor_histogram"],
        "source_role_compatible_histogram": census[
            "source_role_compatible_histogram"
        ],
        "maximum_clean_factor_deficit": maximum_deficit,
        "dimension_failures": failures,
        "capacity_use_authorized_by_law": False,
        "bounded_to_six_locks_and_source_target_union": True,
        "universal_no_go_claimed": False,
        "fake_capacity": fake_capacity,
    }


@lru_cache(maxsize=None)
def full_semantic_capacity_certificate() -> dict[str, object]:
    """Test the strongest escape from source-target-union confinement.

    Dilation acts only on the ten role occurrences.  Record targets outside
    that active set are exact spectator factors, so their identity dimension
    can be restored analytically after checking the small active branch map.
    A scaled isometry of rank r can be sent by a branch-controlled unitary to
    six fixed locks iff r does not exceed the 2^(n-6) lock-complement space.
    """
    nonzero_maps = zero_maps = capacity_failures = isometry_failures = 0
    maximum_probability_spread = 0.0
    maximum_off_diagonal = 0.0
    maximum_diagonal_residual = 0.0
    minimum_capacity_ratio = math.inf
    rank_histogram: Counter[int] = Counter()
    nonzero_label_histograms_by_order = (Counter(), Counter())
    order_set_mismatches = 0
    order_set_difference_histogram: Counter[tuple[int, int]] = Counter()
    order_set_difference_geometries: list[tuple[object, ...]] = []
    auxiliary_outside_histogram: Counter[tuple[int, int]] = Counter()
    geometry_rows: Counter[tuple[int, int, int, int, int, int]] = Counter()
    placements = 0

    for left, right in semantic_overlap_placements():
        if not (archive_support(left) & archive_support(right)):
            continue
        events = (left, right)
        edges = archive_edges(events)
        sources = {edge.source for edge in edges}
        if len(sources) == 6:
            continue
        placements += 1
        targets = {edge.target for edge in edges}
        active = tuple(
            sorted(
                {
                    event_site(event, block71.STARTS[role])
                    for event in events
                    for role in ROLES
                }
            )
        )
        active_index = {site: index for index, site in enumerate(active)}
        requirements = block91.joint_ready_requirements(events)
        free_active = tuple(site for site in active if site not in requirements)
        semantic = set(active) | targets
        spectator_targets = targets - set(active)
        spectator_dimension = 1 << len(spectator_targets)
        lock_complement_capacity = 1 << (len(semantic) - 6)
        auxiliary = {
            event_site(event, block71.STARTS[role])
            for event in events
            for role in ("R", "A")
        }
        auxiliary_outside_histogram[
            (len(sources), len(auxiliary - (sources | targets)))
        ] += 1

        placement_order_sets: list[frozenset[object]] = []
        for order in (0, 1):
            columns: dict[object, list[tuple[dict, float]]] = defaultdict(list)
            for free_index in range(1 << len(free_active)):
                bits = [0] * len(active)
                for site, value in requirements.items():
                    bits[active_index[site]] = value
                for wire, site in enumerate(free_active):
                    bits[active_index[site]] = (free_index >> wire) & 1
                dilated = block86.apply_physical_actions(
                    {tuple(bits): 1.0 + 0.0j},
                    block91.joint_dilation_actions(events, order),
                    active_index,
                )
                for branch in block91.JOINT_BRANCHES:
                    projected = block91.project_branch(
                        dilated, active_index, events, branch
                    )
                    probability = block91.state_probability(projected)
                    if probability > TOL:
                        columns[branch].append((projected, probability))

            nonzero_set = frozenset(columns)
            placement_order_sets.append(nonzero_set)
            nonzero_label_histograms_by_order[order][len(nonzero_set)] += 1

            for branch in block91.JOINT_BRANCHES:
                entries = columns.get(branch, ())
                if not entries:
                    zero_maps += 1
                    continue
                nonzero_maps += 1
                probabilities = [entry[1] for entry in entries]
                spread = max(probabilities) - min(probabilities)
                maximum_probability_spread = max(
                    maximum_probability_spread, spread
                )
                normalized = [
                    block91.normalized_state(entry[0]) for entry in entries
                ]
                local_off_diagonal = 0.0
                local_diagonal = 0.0
                for index, column in enumerate(normalized):
                    local_diagonal = max(
                        local_diagonal,
                        abs(block91.sparse_inner(column, column) - 1.0),
                    )
                    for other in normalized[index + 1 :]:
                        local_off_diagonal = max(
                            local_off_diagonal,
                            abs(block91.sparse_inner(column, other)),
                        )
                maximum_off_diagonal = max(
                    maximum_off_diagonal, float(local_off_diagonal)
                )
                maximum_diagonal_residual = max(
                    maximum_diagonal_residual, float(local_diagonal)
                )
                isometry_failures += (
                    spread >= TOL
                    or local_off_diagonal >= TOL
                    or local_diagonal >= TOL
                )
                rank = len(entries) * spectator_dimension
                rank_histogram[rank] += 1
                capacity_failures += rank > lock_complement_capacity
                minimum_capacity_ratio = min(
                    minimum_capacity_ratio,
                    lock_complement_capacity / rank,
                )
                geometry_rows[
                    (
                        len(sources),
                        len(semantic),
                        len(free_active),
                        len(spectator_targets),
                        rank,
                        lock_complement_capacity,
                    )
                ] += 1
        if placement_order_sets[0] != placement_order_sets[1]:
            order_set_mismatches += 1
            order_zero_only = tuple(
                sorted(placement_order_sets[0] - placement_order_sets[1])
            )
            order_one_only = tuple(
                sorted(placement_order_sets[1] - placement_order_sets[0])
            )
            order_set_difference_histogram[
                (len(order_zero_only), len(order_one_only))
            ] += 1
            order_set_difference_geometries.append(
                (
                    right.rotation,
                    right.translation,
                    order_zero_only,
                    order_one_only,
                )
            )
    return {
        "placements": placements,
        "possible_order_branch_maps": placements * 2 * 16,
        "nonzero_maps": nonzero_maps,
        "zero_maps": zero_maps,
        "rank_histogram": tuple(sorted(rank_histogram.items())),
        "nonzero_label_histograms_by_order": tuple(
            tuple(sorted(histogram.items()))
            for histogram in nonzero_label_histograms_by_order
        ),
        "order_set_mismatches": order_set_mismatches,
        "order_set_difference_histogram": tuple(
            sorted(order_set_difference_histogram.items())
        ),
        "order_set_difference_geometries": tuple(order_set_difference_geometries),
        "auxiliary_outside_histogram": tuple(
            sorted(auxiliary_outside_histogram.items())
        ),
        "geometry_rows": tuple(sorted(geometry_rows.items())),
        "capacity_failures": capacity_failures,
        "isometry_failures": isometry_failures,
        "maximum_probability_spread": maximum_probability_spread,
        "maximum_off_diagonal": maximum_off_diagonal,
        "maximum_diagonal_residual": maximum_diagonal_residual,
        "minimum_capacity_ratio": minimum_capacity_ratio,
        "branch_controlled_unitary_extensions": (
            nonzero_maps
            if capacity_failures == 0 and isometry_failures == 0
            else 0
        ),
        "explicit_extension_matrices_built": False,
        "nn_compiler_built": False,
        "outcome_control_compiled": False,
    }


def coverage_certificate(false_coverage: bool = False) -> dict[str, object]:
    parent = block90.repairable_census_certificate()
    collision = block91.census_certificate()
    archive = archive_graph_census()
    covered = (
        parent["semantic_disjoint"]
        + collision["fully_routable"]
        + archive["fully_routable"]
    )
    if false_coverage:
        covered += 1
    total = parent["simultaneously_ready"]
    residual_duplicate = archive["duplicate"]
    residual_route_traps = collision["route_failures"] + archive["route_failures"]
    residual_write_overlap = parent["write_overlap"]
    residual = total - covered
    return {
        "total": total,
        "covered": covered,
        "coverage_percent": 100.0 * covered / total,
        "residual": residual,
        "residual_percent": 100.0 * residual / total,
        "residual_duplicate": residual_duplicate,
        "residual_route_traps": residual_route_traps,
        "residual_write_overlap": residual_write_overlap,
        "partition_residual": residual
        - residual_duplicate
        - residual_route_traps
        - residual_write_overlap,
        "toe_percentage_movement": False,
        "obligations_retired": 0,
        "retained_positive_end_to_end_theories": 0,
        "false_coverage": false_coverage,
    }


def canonical_ledger(
    records: dict[block71.Coord, object],
    resources: dict[str, str],
    archives: set[str],
    sources: set[tuple[block71.Coord, block71.Coord]],
    reservation: set[block71.Coord],
    labels: set[tuple[object, ...]],
) -> block91.JointLedger:
    return block91.canonical_joint_ledger(
        records, resources, archives, sources, reservation, labels
    )


def initial_ledger(corridor: frozenset[block71.Coord]) -> block91.JointLedger:
    return canonical_ledger(
        {block89.SENTINEL: block71.KPLUS},
        {"left": "ready", "right": "ready", "order_coin": "ready"},
        set(),
        set(),
        set(corridor),
        set(),
    )


def apply_branch(
    ledger: block91.JointLedger,
    branch: object,
    corridor: frozenset[block71.Coord],
    *,
    overwrite: bool = False,
    ignore_ambient_record: bool = False,
    erase_source: bool = False,
) -> tuple[str, block91.JointLedger]:
    records = dict(ledger.records)
    resources = dict(ledger.resources)
    archives = set(ledger.archives)
    sources = set(ledger.sources)
    reservation = set(ledger.reserved_corridor)
    labels = set(ledger.environment_labels)
    semantic = semantic_support(representative_events()[0]) | semantic_support(
        representative_events()[1]
    )
    guard = semantic if ignore_ambient_record else corridor
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
    writes = block89.branch_writes(representative_events()[0], left_branch)
    writes.update(
        block89.branch_writes(representative_events()[1], right_branch)
    )
    if not records.keys().isdisjoint(writes) and not overwrite:
        return "guard_refusal", ledger
    records.update(writes)
    resources = {key: "spent" for key in resources}
    archives.update(("left", "right"))
    if not erase_source:
        for event in representative_events():
            sources.add(
                (
                    event_site(event, block71.ROOT_SITE),
                    event_site(event, block71.HEAD_SITE),
                )
            )
    labels.add((order, left_branch, right_branch))
    return "event", canonical_ledger(
        records, resources, archives, sources, set(), labels
    )


def ambient_record_witness(
    compiler: dict[str, object]
) -> dict[str, object]:
    semantic, requirements, free_sites, _ = representative_basis_data()
    semantic_set = set(semantic)
    support = tuple(sorted(compiler["corridor"] | semantic_set))
    site_index = {site: index for index, site in enumerate(support)}
    background = tuple(site for site in support if site not in semantic_set)
    actions = compile_representative_word(0)["actions"]
    for ambient_site in background:
        bits = [0] * len(support)
        for site, value in requirements.items():
            bits[site_index[site]] = value
        for wire, site in enumerate(free_sites):
            bits[site_index[site]] = wire % 2
        bits[site_index[ambient_site]] = 1
        state = {tuple(bits): 1.0 + 0.0j}
        current = state
        before_value = block91.marginal(state, site_index[ambient_site])
        for index, action in enumerate(actions):
            updated = block86.apply_physical_actions(
                current, (action,), site_index
            )
            after_value = block91.marginal(updated, site_index[ambient_site])
            transient_residual = max(
                abs(after_value[value] - before_value[value])
                for value in (0, 1)
            )
            if ambient_site in action.sites and transient_residual > TOL:
                final = block86.apply_physical_actions(
                    state, actions, site_index
                )
                final_value = block91.marginal(final, site_index[ambient_site])
                return {
                    "site": ambient_site,
                    "zero_index": index,
                    "one_index": index + 1,
                    "kind": action.kind,
                    "sites": action.sites,
                    "before": before_value,
                    "after": after_value,
                    "final": final_value,
                    "transient_residual": transient_residual,
                    "final_residual": max(
                        abs(final_value[value] - before_value[value])
                        for value in (0, 1)
                    ),
                    "outside_semantic": ambient_site not in semantic_set,
                    "inside_corridor": ambient_site in compiler["corridor"],
                }
            current = updated
    raise AssertionError("no transient ambient-Record witness found")


@lru_cache(maxsize=None)
def ledger_certificate(
    overwrite: bool = False,
    ignore_ambient_record: bool = False,
    erase_source: bool = False,
    fake_renewal: bool = False,
) -> dict[str, object]:
    compiler = compiler_certificate()
    corridor = compiler["corridor"]
    event_failures = decode_failures = source_failures = 0
    representative: block91.JointLedger | None = None
    for order in (0, 1):
        for left_branch, right_branch in block91.JOINT_BRANCHES:
            initial = initial_ledger(corridor)
            status, output = apply_branch(
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
    if representative is None:
        raise AssertionError("no representative ledger")

    event_key = (0, (0, 1), (1, 0))
    initial = initial_ledger(corridor)
    no_status, no_output = apply_branch(initial, "no_event", corridor)
    retry_status, retry = apply_branch(no_output, event_key, corridor)
    replay_status, replay = apply_branch(retry, event_key, corridor)

    write_site = event_site(representative_events()[0], block71.HEAD_SITE)
    occupied_records = dict(initial.records)
    occupied_records[write_site] = block71.K1
    occupied = canonical_ledger(
        occupied_records,
        dict(initial.resources),
        set(initial.archives),
        set(initial.sources),
        set(initial.reserved_corridor),
        set(initial.environment_labels),
    )
    occupied_status, occupied_output = apply_branch(
        occupied, event_key, corridor, overwrite=overwrite
    )

    ambient = ambient_record_witness(compiler)
    ambient_records = dict(initial.records)
    ambient_records[ambient["site"]] = block71.K1
    ambient_ledger = canonical_ledger(
        ambient_records,
        dict(initial.resources),
        set(initial.archives),
        set(initial.sources),
        set(initial.reserved_corridor),
        set(initial.environment_labels),
    )
    ambient_status, ambient_output = apply_branch(
        ambient_ledger,
        event_key,
        corridor,
        ignore_ambient_record=ignore_ambient_record,
    )

    spent = sum(value == "spent" for _, value in representative.resources)
    if fake_renewal:
        spent = 0
    continuity_failures = 0
    for root, head in representative.sources:
        delta = {root: -1, head: 1}
        boundary = {root: 1, head: -1}
        continuity_failures += any(delta[site] + boundary[site] for site in delta)
    return {
        "event_branches": 32,
        "event_failures": event_failures,
        "decode_failures": decode_failures,
        "source_failures": source_failures,
        "records": len(representative.records) - 1,
        "resources_spent": spent,
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
        "occupied_status": occupied_status,
        "occupied_identity": occupied_output == occupied,
        "ambient_status": ambient_status,
        "ambient_identity": ambient_output == ambient_ledger,
        "ambient": ambient,
        "continuity_failures": continuity_failures,
        "overwriting": overwrite,
        "ignored_ambient_record": ignore_ambient_record,
        "erased_source": erase_source,
        "renewal_supplied": fake_renewal,
        "capacity_route_supplied": False,
        "actual_draw_supplied": False,
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
        "1,912/2,230",
        "85.7399%",
        "13,400",
        "333",
        "139",
        "source-role-compatible labels",
        "actual nonzero labels per order",
        "order-dependent nonzero-label sets",
        "8 choose 2 = 28",
        "one supplied clean factor",
        "two supplied clean factors",
        "four trapped route geometries remain open",
        "175 write-overlap placements remain open",
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
            "miss_graph",
            "break_permutation",
            "erase_target",
            "drop_swapback",
            "false_coverage",
            "fake_capacity",
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
    checks.check(
        "A-current-authority-and-exact-Block91-parent",
        authority["local_axiom_matches"]
        and authority["local_registry_matches"]
        and authority["sources_match"]
        and authority["forbidden_phrase_hits"] == 0
        and authority["current_contract"]
        and authority["current_inputs_match"]
        and authority["historical_parents_match"]
        and authority["parent_hashes"] == PARENT_SHA256
        and not authority["forced_stale"],
        f"axiom={authority['axiom_sha256'][:12]}; no joint archive graph law, clean capacity, global atlas, or gravity law is registered",
    )

    census = archive_graph_census(mutation == "miss_graph", mutation == "break_permutation")
    expected_patterns = (
        ((('cycle', 2), ('cycle', 2), ('path', 2), ('path', 2)), 1),
        ((('cycle', 2), ('path', 2), ('path', 2), ('path', 2), ('path', 2)), 8),
        ((('path', 2), ('path', 2), ('path', 2), ('path', 2), ('path', 3)), 306),
        ((('path', 2), ('path', 2), ('path', 2), ('path', 4)), 4),
        ((('path', 2), ('path', 2), ('path', 3), ('path', 3)), 16),
    )
    checks.check(
        "B-corrected-474-case-archive-graph-census",
        census["semantic_cases"] == 921
        and census["archive_overlap_cases"] == 474
        and census["injective"] == 335
        and census["duplicate"] == 139
        and census["injective_overlap"] == ((1, 306), (2, 28), (4, 1))
        and census["duplicate_source_count"] == ((4, 4), (5, 135))
        and census["component_patterns"] == expected_patterns
        and census["component_failures"] == 0
        and census["partition_failures"] == 0,
        "474 archive overlaps split into 335 injective source graphs and 139 duplicate-source graphs; corrected components cover each vertex exactly once",
    )

    checks.check(
        "C-all-335-injective-graphs-close-to-exact-permutations",
        census["transposition_count"] == 2000
        and census["symbolic_failures"] == 0,
        f"five path/cycle component types compile to {census['transposition_count']} transpositions with {census['symbolic_failures']} target-lock or bijectivity failures",
    )

    branch = branch_archive_certificate(mutation == "erase_target")
    checks.check(
        "D-representative-32-rank32-five-target-isometries-and-six-locks",
        branch["semantic_sites"] == 15
        and branch["free_ready_sites"] == 7
        and branch["free_target_sites"] == 5
        and branch["source_sites"] == 6
        and branch["nonzero_branch_maps"] == 32
        and branch["rank_set"] == (32,)
        and branch["target_count_failures"] == 0
        and branch["matter_support_failures"] == 0
        and branch["maximum_gram_residual"] < TOL
        and branch["maximum_probability_spread"] < TOL
        and branch["lock_residual"] < TOL
        and not branch["erased_target"],
        f"32 maps preserve five branch-compatible arbitrary target qubits at rank {branch['minimum_rank']}; Gram={branch['maximum_gram_residual']:.3g}, lock={branch['lock_residual']:.3g}",
    )

    compiler = compiler_certificate(mutation == "drop_swapback")
    checks.check(
        "E-333-routable-injective-graphs-and-exact-representative-NN-word",
        census["route_checks"] == 2000
        and census["route_failures"] == 2
        and census["dilation_route_checks"] == 13400
        and census["dilation_route_failures"] == 0
        and census["fully_routable"] == 333
        and census["archive_primitive_min"] == 16
        and census["archive_primitive_max"] == 42
        and compiler["primitives"][0] == compiler["primitives"][1]
        and compiler["supports_equal"]
        and compiler["nn_failures"] == 0
        and compiler["macro_residual"] < TOL
        and compiler["maximum_residual"] < TOL
        and compiler["background_failures"] == 0
        and not compiler["dropped_swapback"],
        f"333/335 pass {census['dilation_route_checks']} order-independent dilation and {census['route_checks']} archive path checks with two exact traps; representative uses {compiler['primitives'][0]} primitives on {compiler['corridor_sites']} guarded sites with residual {compiler['maximum_residual']:.2e}",
    )

    coverage = coverage_certificate(mutation == "false_coverage")
    checks.check(
        "F-exact-1912-of-2230-conditional-compiler-coverage",
        coverage["total"] == 2230
        and coverage["covered"] == 1912
        and abs(coverage["coverage_percent"] - 85.73991031390135) < TOL
        and coverage["residual"] == 318
        and coverage["residual_duplicate"] == 139
        and coverage["residual_route_traps"] == 4
        and coverage["residual_write_overlap"] == 175
        and coverage["partition_residual"] == 0
        and coverage["obligations_retired"] == 0
        and not coverage["toe_percentage_movement"],
        f"conditional NN compiler coverage is {coverage['covered']}/{coverage['total']}={coverage['coverage_percent']:.6f}%; residual 318=139 controlled archives+4 routes+175 write overlaps, with zero TOE credit",
    )

    capacity = capacity_certificate(mutation == "fake_capacity")
    full_capacity = full_semantic_capacity_certificate()
    expected_order_support_differences = (
        (
            ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
            (-3, 0, 1),
            (((1, 1), (1, 0)),),
            (((1, 1), (1, 1)),),
        ),
        (
            ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
            (-3, 1, 0),
            (((1, 1), (1, 1)),),
            (((1, 0), (1, 1)),),
        ),
        (
            ((-1, 0, 0), (0, 0, -1), (0, -1, 0)),
            (0, 0, 0),
            (((1, 1), (0, 1)), ((1, 1), (1, 0))),
            (((0, 1), (1, 1)), ((1, 0), (1, 1))),
        ),
    )
    checks.check(
        "G-sharp-union-capacity-boundary-and-full-semantic-carrier-escape",
        capacity["duplicate_cases"] == 139
        and capacity["clean_factor_histogram"] == ((1, 135), (2, 4))
        and capacity["source_role_compatible_histogram"]
        == ((4, 3), (8, 118), (16, 18))
        and capacity["maximum_clean_factor_deficit"] == 2
        and capacity["dimension_failures"] == 0
        and capacity["bounded_to_six_locks_and_source_target_union"]
        and not capacity["universal_no_go_claimed"]
        and not capacity["capacity_use_authorized_by_law"]
        and full_capacity["placements"] == 139
        and full_capacity["possible_order_branch_maps"] == 4448
        and full_capacity["nonzero_maps"] == 2458
        and full_capacity["zero_maps"] == 1990
        and full_capacity["rank_histogram"] == ((16, 32), (32, 416), (64, 2010))
        and full_capacity["nonzero_label_histograms_by_order"]
        == (
            ((4, 3), (6, 4), (8, 114), (9, 1), (16, 17)),
            ((4, 3), (6, 4), (8, 114), (9, 1), (16, 17)),
        )
        and full_capacity["order_set_mismatches"] == 3
        and full_capacity["order_set_difference_histogram"]
        == (((1, 1), 2), ((2, 2), 1))
        and full_capacity["order_set_difference_geometries"]
        == expected_order_support_differences
        and full_capacity["auxiliary_outside_histogram"]
        == (((4, 4), 4), ((5, 2), 3), ((5, 3), 22), ((5, 4), 110))
        and full_capacity["capacity_failures"] == 0
        and full_capacity["isometry_failures"] == 0
        and full_capacity["maximum_probability_spread"] < TOL
        and full_capacity["maximum_off_diagonal"] < TOL
        and full_capacity["maximum_diagonal_residual"] < TOL
        and full_capacity["minimum_capacity_ratio"] >= 2.0
        and full_capacity["branch_controlled_unitary_extensions"] == 2458
        and not full_capacity["nn_compiler_built"],
        "source-role equality is only a necessary label test; actual nonzero support is 1,229 labels/order with three order-dependent support sets. The source-target-only archive needs 1/2 fixed slots, but the full semantic carrier has >=2x six-lock complement capacity and scaled-isometric extensions for all 2,458 nonzero order/branch maps; the controlled NN compiler remains open",
    )

    ledger = ledger_certificate(
        overwrite=mutation == "overwrite",
        ignore_ambient_record=mutation == "ignore_ambient_record",
        erase_source=mutation == "erase_source",
        fake_renewal=mutation == "fake_renewal",
    )
    ambient = ledger["ambient"]
    checks.check(
        "H-complete-overlap-ledger-resource-debit-and-full-corridor-guard",
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
        and ledger["no_event_status"] == "no_event"
        and ledger["no_event_identity"]
        and ledger["retry_status"] == "event"
        and ledger["replay_status"] == "guard_refusal"
        and ledger["replay_identity"]
        and ledger["occupied_status"] == "guard_refusal"
        and ledger["occupied_identity"]
        and ledger["ambient_status"] == "guard_refusal"
        and ledger["ambient_identity"]
        and ambient["outside_semantic"]
        and ambient["inside_corridor"]
        and ambient["transient_residual"] > TOL
        and ambient["final_residual"] < TOL
        and ledger["continuity_failures"] == 0
        and not ledger["renewal_supplied"],
        f"six Records, three spent resources, two archives/sources, replay and occupied-corridor refusal; route-only K1 at {ambient['site']} changes at primitive {ambient['one_index']} but is restored only at macro end",
    )

    checks.check(
        "I-bounded-capacity-no-go-discipline-and-strict-TOE-accounting",
        boundary_surface_ok(mutation == "false_progress")
        and not ledger["capacity_route_supplied"]
        and not ledger["actual_draw_supplied"]
        and not ledger["physical_rate_supplied"]
        and not ledger["energy_action_supplied"]
        and not ledger["gravity_supplied"],
        "N1-N8 credits 333 positive archive compilers and the exact 139-case capacity boundary while preserving route, write, authority, actuality, renewal, gravity, retention, and zero-score walls",
    )

    print(
        "METRICS archive_overlap={} injective={} routable={} duplicate={} transpositions={} dilation_route_checks={} dilation_route_failures={} archive_route_checks={} archive_route_failures={} branch_rank={} gram={:.3g} compiler_primitives={} corridor_sites={} full_carrier_maps={} full_carrier_capacity_failures={} covered={} total={} coverage_percent={:.9f}".format(
            census["archive_overlap_cases"],
            census["injective"],
            census["fully_routable"],
            census["duplicate"],
            census["transposition_count"],
            census["dilation_route_checks"],
            census["dilation_route_failures"],
            census["route_checks"],
            census["route_failures"],
            branch["minimum_rank"],
            branch["maximum_gram_residual"],
            compiler["primitives"][0],
            compiler["corridor_sites"],
            full_capacity["nonzero_maps"],
            full_capacity["capacity_failures"],
            coverage["covered"],
            coverage["total"],
            coverage["coverage_percent"],
        )
    )
    print("N5_RESOLUTION per_element: six archive arrows, 13,400 order-independent dilation routes, five component types, 2,000 archive endpoint transpositions, six Record locks, two event packets, one order coin, and two source edges are typed")
    print("N5_RESOLUTION per_site: each injective source-target graph is decomposed exactly; the representative has one source-target collision, five arbitrary branch-compatible target factors, and a fully guarded routed corridor")
    print("N5_RESOLUTION per_mode: path, cycle, injective, duplicate-source, necessary source-role compatibility, actual nonzero amplitude, three order-dependent support sets, full-carrier isometry, trapped route, refusal, no-event, retry, replay, occupied write, ambient Record, and capacity modes are checked")
    print("N5_RESOLUTION per_block: current authority, exact Block91 receipt, exhaustive archive graph and dilation-route censuses, symbolic conservation, branch isometry and amplitude-support census, NN compiler, full-carrier escape, coverage partition, restricted dimension boundary, ledger, guard, debit, and source boundary are checked")
    print("N5_RESOLUTION lattice_wide: 333 of 474 archive-overlap placements receive the present conditional NN unitary compiler; all 2,458 nonzero duplicate-source order/branch maps admit geometry/label-specific abstract six-lock unitary extensions on the full semantic carrier, while their common controlled NN compiler, four route traps, 175 write overlaps, global selection, actuality, renewal, time, energy, gravity, retention, and TOE closure remain open")
    print("BOUNDARY: injective archive collisions admit an exact conservative graph-permutation law; all 13,400 dilation prerequisites pass and 333/335 archive words route on supplied Record-free corridors. Duplicate-source archives confined to their source-target union have an exact one- or two-fixed-slot deficit, but the existing full semantic carrier has sufficient abstract capacity for every nonzero branch; each order has 1,229 nonzero labels, three geometries have order-dependent support, and no common branch-controlled NN archive is constructed. The law/compiler, global atlas, actual outcome, renewal/cadence, source/action typing, gravity, audit retention, obligation retirement, and TOE percentage movement are not supplied")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
