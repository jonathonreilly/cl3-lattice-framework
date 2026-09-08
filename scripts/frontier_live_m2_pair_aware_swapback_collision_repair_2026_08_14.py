#!/usr/bin/env python3
"""Block 90: pair-aware swap-back repair of the Block89 collision witness.

The exact Block86 coherent event unitary is compiled directly on its eight
semantic factors.  Every nonlocal two-factor gate is routed by adjacent SWAPs
and the route is reversed immediately; archive endpoint transpositions also
restore every path-interior factor.  For the Block89 symmetric pair the paths
avoid both events' semantic supports except at intended endpoints.  On a
supplied Record-free route corridor, the resulting finite NN words have
overlapping transient unrecorded backgrounds but implement disjoint semantic
operators and therefore commute.  A permanent Record on a route-only site is
an exact obstruction: the selected 32-site support must be guarded and the
joint corridor reserved before execution.  This conditionally repairs the
exact hostile pair without a deterministic selector.  Semantic-overlap
collisions, a global obstacle-aware route atlas, outcome-pointer compilation,
resource renewal, cadence, source/action typing, and gravity remain open.  The
construction is a bounded compiler theorem, not an adopted formation law or
TOE obligation retirement.
"""

from __future__ import annotations

import argparse
from functools import lru_cache
from hashlib import sha256
from itertools import product
import json
import math
from pathlib import Path
import subprocess

import numpy as np

import frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14 as block89


block86 = block89.block86
block72 = block89.block72
block71 = block89.block71

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_"
    "2026-08-14.md"
)
AXIOM_REPO_PATH = "docs/MINIMAL_AXIOMS_2026-06-29.md"
REGISTRY_REPO_PATH = "docs/audit/data/axiom_premise_nodes.json"
PARENT_RUNNER = ROOT / "scripts" / (
    "frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py"
)
PARENT_NOTE = ROOT / "docs" / (
    "LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_"
    "BOUNDED_THEOREM_NOTE_2026-08-14.md"
)
PARENT_RECEIPT = "00d3a2ca79619e474ebcc1d34c468d76b0eb57b1"
HISTORICAL_PARENT_SHA256 = ('ff2741790f7bba4c974a9f69101602120d2233c1078e41e7520a82195b03fed3', 'eb04913f21353364b648ca50f783ca5f2ec833e24c464c4eecaf084708932342')
PARENT_SHA256 = ('81e5b4845c64cc149ab1984e0884975e8ec279a7ea6fbaeb5ac88ff4ac83504a', '2d4fd67f35917906d6f2fd481a27a35ac49b54814644540f9f3c884263961038')
HISTORICAL_PARENT_FILES = (('00d3a2ca79619e474ebcc1d34c468d76b0eb57b1', 'scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py'), ('00d3a2ca79619e474ebcc1d34c468d76b0eb57b1', 'docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md'))
AUDIT_INPUT_PATHS = (
    "docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/audit/data/axiom_premise_nodes.json",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md",
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py",
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
    "docs/LIVE_M2_PAIR_AWARE_SWAPBACK_COLLISION_REPAIR_BOUNDED_THEOREM_NOTE_2026-08-14.md": "ec3d6653b00f6d06b4eb95ac6bb24c6024e3fbe63d5a8ce5a6b78fca9a175968",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "docs/audit/data/axiom_premise_nodes.json": "615f13aaa70e82d50cdf1a8aa479eb40d6ce70a3bb7b152ac63fd88bee341f37",
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
    "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md": "5516fb0bb8f50286b3c34d3f2668b1a2e347b9f7e257a8b5745f84f1093dd96b",
    "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md": "755cfd44924439468708124a8aaafce1b2bcaf6260d3bc08263dc6e7a4327563",
    "docs/LIVE_M2_TYPED_EVENT_CRITICAL_PAIR_CONFLUENCE_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-08-14.md": "2d4fd67f35917906d6f2fd481a27a35ac49b54814644540f9f3c884263961038",
    "scripts/frontier_live_m2_typed_event_critical_pair_confluence_2026_08_14.py": "81e5b4845c64cc149ab1984e0884975e8ec279a7ea6fbaeb5ac88ff4ac83504a",
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
ROLES = ("P", "M", "B", "R", "A")
SEMANTIC_OVERLAP_ROTATION: block71.Rotation = (
    (-1, 0, 0),
    (0, -1, 0),
    (0, 0, 1),
)
SEMANTIC_OVERLAP_TRANSLATION: block71.Coord = (1, -2, 1)


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
        "pair-aware swap-back compiler",
        "semantic-support collision atlas",
        "live-M2 formation instrument",
        "clean-input renewal law",
    )
    flat_axiom = " ".join(axiom.split())
    return {
        "axiom_sha256": sha256(axiom.encode()).hexdigest(),
        "local_axiom_matches": (ROOT / AXIOM_REPO_PATH).read_text() == axiom,
        "local_registry_matches": (ROOT / REGISTRY_REPO_PATH).read_text() == registry_text,
        "canonical_ids": tuple(registry["canonical_ids"]),
        "sources_match": all(
            (ROOT / path).is_file() and (ROOT / path).read_text() == text
            for path, text in zip(paths, source_texts)
        ),
        "compiler_phrase_hits": sum(
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


def symmetric_pair() -> tuple[block89.EventSpec, block89.EventSpec]:
    return (
        block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0)),
        block89.EventSpec("right", block89.SWAP_ROTATION, block89.SWAP_TRANSLATION),
    )


def semantic_support(event: block89.EventSpec) -> frozenset[block71.Coord]:
    return block89.event_support(event, "abstract")


def event_site(event: block89.EventSpec, site: block71.Coord) -> block71.Coord:
    return block89.transform_site(event, site)


def transform_action(
    rotation: block71.Rotation,
    translation: block71.Coord,
    action: block72.PhysicalAction,
) -> block72.PhysicalAction:
    geometry = block89.EventSpec("geometry", rotation, translation)
    return block72.PhysicalAction(
        action.kind,
        tuple(event_site(geometry, site) for site in action.sites),
        action.matrix,
    )


def actions_equal(
    left: tuple[block72.PhysicalAction, ...],
    right: tuple[block72.PhysicalAction, ...],
) -> bool:
    if len(left) != len(right):
        return False
    for first, second in zip(left, right):
        if first.kind != second.kind or first.sites != second.sites:
            return False
        if first.matrix is None or second.matrix is None:
            if first.matrix is not None or second.matrix is not None:
                return False
        elif not np.allclose(first.matrix, second.matrix, atol=TOL):
            return False
    return True


def event_endpoint_pairs(
    event: block89.EventSpec,
) -> tuple[tuple[block71.Coord, block71.Coord], ...]:
    pairs: list[tuple[block71.Coord, block71.Coord]] = []
    for gate in block71.dilation_word():
        if len(gate.wires) != 2:
            continue
        pairs.append(
            (
                event_site(event, block71.STARTS[ROLES[gate.wires[0]]]),
                event_site(event, block71.STARTS[ROLES[gate.wires[1]]]),
            )
        )
    for role, target in (
        ("P", block71.HEAD_SITE),
        ("M", block71.ROOT_SITE),
        ("B", block71.META_SITE),
    ):
        pairs.append(
            (event_site(event, block71.STARTS[role]), event_site(event, target))
        )
    return tuple(dict.fromkeys(pairs))


def pair_path(
    start: block71.Coord,
    target: block71.Coord,
    all_semantic: frozenset[block71.Coord],
) -> tuple[block71.Coord, ...]:
    path = block71.shortest_path(
        start,
        target,
        set(all_semantic) - {start, target},
        tuple(all_semantic),
    )
    if path is None:
        raise RuntimeError(f"no pair-aware path {start}->{target}")
    return path


def routed_gate_actions(
    gate: block71.Gate,
    event: block89.EventSpec,
    all_semantic: frozenset[block71.Coord],
    *,
    drop_swapback: bool = False,
) -> tuple[tuple[block72.PhysicalAction, ...], tuple[block71.Coord, ...]]:
    sites = tuple(
        event_site(event, block71.STARTS[ROLES[wire]]) for wire in gate.wires
    )
    if len(sites) == 1:
        return (block72.PhysicalAction(gate.kind, sites, gate.matrix),), sites
    path = pair_path(sites[0], sites[1], all_semantic)
    forward = tuple(zip(path[:-2], path[1:-1]))
    reverse = tuple(reversed(forward))
    if drop_swapback and reverse:
        reverse = reverse[:-1]
    actions = tuple(block72.PhysicalAction("SWAP", edge) for edge in forward)
    actions += (block72.PhysicalAction(gate.kind, (path[-2], path[-1]), gate.matrix),)
    actions += tuple(block72.PhysicalAction("SWAP", edge) for edge in reverse)
    return actions, path


def endpoint_swap_actions(
    start: block71.Coord,
    target: block71.Coord,
    all_semantic: frozenset[block71.Coord],
) -> tuple[tuple[block72.PhysicalAction, ...], tuple[block71.Coord, ...]]:
    path = pair_path(start, target, all_semantic)
    forward = tuple(zip(path, path[1:]))
    swaps = forward + tuple(reversed(forward[:-1]))
    return tuple(block72.PhysicalAction("SWAP", edge) for edge in swaps), path


def two_gate_macro_residual(
    path: tuple[block71.Coord, ...],
    matrix: np.ndarray,
    *,
    drop_swapback: bool = False,
) -> tuple[float, int]:
    maximum = 0.0
    count = 0
    width = len(path)
    for basis in range(1 << width):
        bits = tuple((basis >> index) & 1 for index in range(width))
        observed: dict[tuple[int, ...], complex] = {bits: 1.0 + 0.0j}
        for index in range(width - 2):
            observed = block72.apply_swap(observed, index, index + 1)
        observed = block72.apply_two(observed, width - 2, width - 1, matrix)
        reverse = list(reversed(range(width - 2)))
        if drop_swapback and reverse:
            reverse = reverse[:-1]
        for index in reverse:
            observed = block72.apply_swap(observed, index, index + 1)
        expected = block72.apply_two(
            {bits: 1.0 + 0.0j}, 0, width - 1, matrix
        )
        maximum = max(maximum, block72.state_residual(observed, expected))
        count += 1
    return maximum, count


def endpoint_swap_residual(path: tuple[block71.Coord, ...]) -> tuple[float, int]:
    maximum = 0.0
    count = 0
    width = len(path)
    for basis in range(1 << width):
        bits = tuple((basis >> index) & 1 for index in range(width))
        observed: dict[tuple[int, ...], complex] = {bits: 1.0 + 0.0j}
        for index in range(width - 1):
            observed = block72.apply_swap(observed, index, index + 1)
        for index in reversed(range(width - 2)):
            observed = block72.apply_swap(observed, index, index + 1)
        expected = block72.apply_swap(
            {bits: 1.0 + 0.0j}, 0, width - 1
        )
        maximum = max(maximum, block72.state_residual(observed, expected))
        count += 1
    return maximum, count


def ideal_semantic_unitary() -> np.ndarray:
    dilation = block71.word_matrix(block71.dilation_word(), 5)
    return block86.archive_unitary() @ block86.extended_low(dilation)


def full_semantic_equivalence(
    actions: tuple[block72.PhysicalAction, ...],
    event: block89.EventSpec,
) -> dict[str, object]:
    semantic = tuple(
        event_site(event, block71.STARTS[role]) for role in ROLES
    ) + tuple(
        event_site(event, site)
        for site in (block71.HEAD_SITE, block71.ROOT_SITE, block71.META_SITE)
    )
    semantic_set = set(semantic)
    support = tuple(sorted({site for action in actions for site in action.sites}))
    site_index = {site: index for index, site in enumerate(support)}
    background = tuple(site for site in support if site not in semantic_set)
    background_values = {
        site: (abs(site[0]) + 2 * abs(site[1]) + 3 * abs(site[2])) % 2
        for site in background
    }
    ideal = ideal_semantic_unitary()
    maximum = 0.0
    background_failures = 0
    for source in range(256):
        bits = [0] * len(support)
        for wire, site in enumerate(semantic):
            bits[site_index[site]] = (source >> wire) & 1
        for site, value in background_values.items():
            bits[site_index[site]] = value
        observed = block86.apply_physical_actions(
            {tuple(bits): 1.0 + 0.0j}, actions, site_index
        )
        expected: dict[tuple[int, ...], complex] = {}
        for target, amplitude in enumerate(ideal[:, source]):
            if abs(amplitude) < 1.0e-15:
                continue
            result = list(bits)
            for wire, site in enumerate(semantic):
                result[site_index[site]] = (target >> wire) & 1
            expected[tuple(result)] = amplitude
        maximum = max(maximum, block72.state_residual(observed, expected))
        background_failures += any(
            any(key[site_index[site]] != value for site, value in background_values.items())
            for key in observed
        )
    return {
        "basis_cases": 256,
        "maximum_residual": maximum,
        "background_sites": len(background),
        "background_failures": background_failures,
    }


def compile_pair_event(
    left: block89.EventSpec,
    right: block89.EventSpec,
    event: block89.EventSpec,
    *,
    drop_swapback: bool = False,
) -> dict[str, object]:
    all_semantic = semantic_support(left) | semantic_support(right)
    actions: list[block72.PhysicalAction] = []
    paths: list[tuple[block71.Coord, ...]] = []
    macro_residual = 0.0
    macro_cases = 0
    dropped = False
    for gate in block71.dilation_word():
        should_drop = drop_swapback and len(gate.wires) == 2 and not dropped
        routed, path = routed_gate_actions(
            gate, event, all_semantic, drop_swapback=should_drop
        )
        actions.extend(routed)
        if len(gate.wires) == 2:
            residual, cases = two_gate_macro_residual(
                path, gate.matrix, drop_swapback=should_drop
            )
            macro_residual = max(macro_residual, residual)
            macro_cases += cases
            paths.append(path)
            dropped = dropped or should_drop
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
        routed, path = endpoint_swap_actions(
            event_site(event, block71.STARTS[role]),
            event_site(event, target),
            all_semantic,
        )
        actions.extend(routed)
        residual, cases = endpoint_swap_residual(path)
        macro_residual = max(macro_residual, residual)
        macro_cases += cases
        paths.append(path)
    action_tuple = tuple(actions)
    support = {site for action in action_tuple for site in action.sites}
    interiors = {site for path in paths for site in path[1:-1]}
    other = right if event == left else left
    equivalence = full_semantic_equivalence(action_tuple, event)
    return {
        "actions": action_tuple,
        "paths": tuple(paths),
        "path_count": len(paths),
        "path_histogram": tuple(
            sorted((length, sum(len(path) == length for path in paths)) for length in set(map(len, paths)))
        ),
        "maximum_path_vertices": max(map(len, paths)),
        "physical_primitives": len(action_tuple),
        "support": frozenset(support),
        "support_sites": len(support),
        "route_macro_cases": macro_cases,
        "route_macro_residual": macro_residual,
        "non_nn_failures": sum(
            len(action.sites) == 2 and block71.distance(*action.sites) != 1
            for action in action_tuple
        ),
        "semantic_interior_hits": len(interiors & set(all_semantic)),
        "other_write_hits": len(support & set(block89.event_support(other, "write"))),
        "equivalence": equivalence,
        "dropped_swapback": dropped,
    }


@lru_cache(maxsize=None)
def repairable_census_certificate(miss_one: bool = False) -> dict[str, object]:
    base = block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0))
    core = block89.base_core_support()
    placements = ready = write_overlap = semantic_overlap = semantic_disjoint = 0
    path_checks = path_failures = 0
    maximum_path = 0
    for rotation in block71.ROTATIONS:
        rotated = {block71.rotate(rotation, site) for site in core}
        translations = {
            block89.subtraction(left, right) for left in core for right in rotated
        }
        for translation in translations:
            if rotation == block89.IDENTITY_ROTATION and translation == (0, 0, 0):
                continue
            other = block89.EventSpec("right", rotation, translation)
            if not (block89.event_support(base) & block89.event_support(other)):
                continue
            placements += 1
            if not block89.simultaneously_ready(base, other):
                continue
            ready += 1
            if block89.event_support(base, "write") & block89.event_support(other, "write"):
                write_overlap += 1
                continue
            if semantic_support(base) & semantic_support(other):
                semantic_overlap += 1
                continue
            semantic_disjoint += 1
            all_semantic = semantic_support(base) | semantic_support(other)
            for event in (base, other):
                for start, target in event_endpoint_pairs(event):
                    path_checks += 1
                    try:
                        path = pair_path(start, target, all_semantic)
                    except RuntimeError:
                        path_failures += 1
                    else:
                        maximum_path = max(maximum_path, len(path))
    if miss_one:
        path_failures += 1
    return {
        "overlap_placements": placements,
        "simultaneously_ready": ready,
        "write_overlap": write_overlap,
        "write_disjoint_semantic_overlap": semantic_overlap,
        "semantic_disjoint": semantic_disjoint,
        "unique_endpoint_pairs_per_event": len(event_endpoint_pairs(base)),
        "path_checks": path_checks,
        "path_failures": path_failures,
        "maximum_path_vertices": maximum_path,
    }


@lru_cache(maxsize=None)
def symmetric_compiler_certificate(drop_swapback: bool = False) -> dict[str, object]:
    left, right = symmetric_pair()
    left_compiler = compile_pair_event(
        left, right, left, drop_swapback=drop_swapback
    )
    right_actions = tuple(
        transform_action(block89.SWAP_ROTATION, block89.SWAP_TRANSLATION, action)
        for action in left_compiler["actions"]
    )
    right_support = frozenset(
        site for action in right_actions for site in action.sites
    )
    left_support = left_compiler["support"]
    back_to_left = tuple(
        transform_action(block89.SWAP_ROTATION, block89.SWAP_TRANSLATION, action)
        for action in right_actions
    )
    return {
        "left": left_compiler,
        "right_actions": right_actions,
        "right_support": right_support,
        "route_overlap": len(left_support & right_support),
        "union_support": len(left_support | right_support),
        "left_hits_right_writes": len(left_support & block89.event_support(right, "write")),
        "right_hits_left_writes": len(right_support & block89.event_support(left, "write")),
        "words_swap_under_involution": actions_equal(
            back_to_left, left_compiler["actions"]
        ),
        "semantic_overlap": len(semantic_support(left) & semantic_support(right)),
        "write_overlap": len(
            block89.event_support(left, "write")
            & block89.event_support(right, "write")
        ),
    }


def repaired_collision_certificate(compact_collision: bool = False) -> dict[str, object]:
    left, right = symmetric_pair()
    compiler = symmetric_compiler_certificate(False)
    left_actions = compiler["left"]["actions"]
    right_actions = compiler["right_actions"]
    sites = tuple(sorted(compiler["left"]["support"] | compiler["right_support"]))
    requirements = block89.fixed_requirements(left)
    requirements.update(block89.fixed_requirements(right))
    requirements.setdefault(event_site(left, block71.STARTS["M"]), 0)
    requirements.setdefault(event_site(right, block71.STARTS["M"]), 0)
    bits = tuple(requirements.get(site, 0) for site in sites)
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
    old = block89.physical_collision_certificate()
    if compact_collision:
        residual = float(old["order_residual"])
    geometry = block89.EventSpec(
        "symmetry", block89.SWAP_ROTATION, block89.SWAP_TRANSLATION
    )
    ready_state = dict(zip(sites, bits))
    state_invariant = all(
        event_site(geometry, site) in ready_state
        and ready_state[event_site(geometry, site)] == value
        for site, value in ready_state.items()
    )
    return {
        "old_compact_residual": old["order_residual"],
        "new_residual": residual,
        "left_right_terms": len(left_right),
        "right_left_terms": len(right_left),
        "physical_primitives_each": compiler["left"]["physical_primitives"],
        "support_each": compiler["left"]["support_sites"],
        "route_overlap": compiler["route_overlap"],
        "union_support": compiler["union_support"],
        "cross_write_hits": (
            compiler["left_hits_right_writes"] + compiler["right_hits_left_writes"]
        ),
        "state_invariant": state_invariant,
        "words_swap_under_involution": compiler["words_swap_under_involution"],
        "abstract_operator_supports_disjoint": compiler["semantic_overlap"] == 0,
        "compact_collision_forced": compact_collision,
    }


def apply_semantic_branch(
    ledger: block89.Ledger,
    event: block89.EventSpec,
    branch: object,
    *,
    execution_support: frozenset[block71.Coord] | None = None,
    overwrite: bool = False,
    erase_source: bool = False,
) -> tuple[str, block89.Ledger]:
    records = dict(ledger.records)
    resources = dict(ledger.resources)
    archives = set(ledger.archives)
    sources = set(ledger.sources)
    reservations = set(ledger.reservations)
    guard_support = semantic_support(event) if execution_support is None else execution_support
    occupied = not records.keys().isdisjoint(guard_support)
    if resources.get(event.label) == "spent" or occupied:
        if overwrite and isinstance(branch, tuple):
            records.update(block89.branch_writes(event, branch))
            return "event", block89.canonical_ledger(
                records, resources, archives, sources, reservations
            )
        return "guard_refusal", ledger
    if not isinstance(branch, tuple):
        return str(branch), ledger
    writes = block89.branch_writes(event, branch)
    if not records.keys().isdisjoint(writes) and not overwrite:
        return "guard_refusal", ledger
    records.update(writes)
    resources[event.label] = "spent"
    archives.add(event.label)
    if not erase_source:
        sources.add(
            (
                event_site(event, block71.ROOT_SITE),
                event_site(event, block71.HEAD_SITE),
            )
        )
    reservations.discard(event.label)
    return "event", block89.canonical_ledger(
        records, resources, archives, sources, reservations
    )


def repaired_ledger_certificate(overwrite: bool = False) -> dict[str, object]:
    left, right = symmetric_pair()
    compiler = symmetric_compiler_certificate(False)
    execution_support = {
        left.label: compiler["left"]["support"],
        right.label: compiler["right_support"],
    }
    mismatches = source_failures = decode_failures = 0
    for left_key, right_key in product(block89.BRANCH_KEYS, repeat=2):
        initial = block89.initial_ledger((left, right))
        _, after_left = apply_semantic_branch(
            initial,
            left,
            left_key,
            execution_support=execution_support[left.label],
            overwrite=overwrite,
        )
        _, left_right = apply_semantic_branch(
            after_left,
            right,
            right_key,
            execution_support=execution_support[right.label],
            overwrite=overwrite,
        )
        _, after_right = apply_semantic_branch(
            initial,
            right,
            right_key,
            execution_support=execution_support[right.label],
            overwrite=overwrite,
        )
        _, right_left = apply_semantic_branch(
            after_right,
            left,
            left_key,
            execution_support=execution_support[left.label],
            overwrite=overwrite,
        )
        mismatches += left_right != right_left
        expected = int(isinstance(left_key, tuple)) + int(isinstance(right_key, tuple))
        source_failures += len(left_right.sources) != expected
        for root, head in left_right.sources:
            delta = {root: -1, head: 1}
            boundary = {root: 1, head: -1}
            source_failures += any(
                delta[site] + boundary[site] for site in delta
            )
        decode_failures += len(block71.find_packets(dict(left_right.records))) != expected

    initial = block89.initial_ledger((left, right))
    _, after_left = apply_semantic_branch(
        initial,
        left,
        (0, 0),
        execution_support=execution_support[left.label],
        overwrite=overwrite,
    )
    _, after_both = apply_semantic_branch(
        after_left,
        right,
        (1, 1),
        execution_support=execution_support[right.label],
        overwrite=overwrite,
    )
    replay_left_status, replay_left = apply_semantic_branch(
        after_both,
        left,
        (1, 0),
        execution_support=execution_support[left.label],
        overwrite=overwrite,
    )
    replay_right_status, replay_right = apply_semantic_branch(
        after_both,
        right,
        (0, 1),
        execution_support=execution_support[right.label],
        overwrite=overwrite,
    )
    mixed_initial = block89.initial_ledger((left, right))
    _, mixed = apply_semantic_branch(
        mixed_initial,
        left,
        (1, 0),
        execution_support=execution_support[left.label],
        overwrite=overwrite,
    )
    no_status, mixed_no = apply_semantic_branch(
        mixed,
        right,
        "no_event",
        execution_support=execution_support[right.label],
        overwrite=overwrite,
    )
    retry_status, mixed_retry = apply_semantic_branch(
        mixed_no,
        right,
        (0, 1),
        execution_support=execution_support[right.label],
        overwrite=overwrite,
    )
    branch = block89.disjoint_branch_confluence_certificate()
    joint_corridor = execution_support[left.label] | execution_support[right.label]
    initial_record_sites = set(dict(initial.records))
    return {
        "branch_pairs": branch["branch_pairs"],
        "branch_residual": branch["maximum_order_residual"],
        "branch_normalization": branch["normalization"],
        "ledger_cases": len(block89.BRANCH_KEYS) ** 2,
        "ledger_mismatches": mismatches,
        "source_failures": source_failures,
        "decode_failures": decode_failures,
        "records_after_two": len(after_both.records) - 1,
        "spent_after_two": sum(value == "spent" for _, value in after_both.resources),
        "archives_after_two": len(after_both.archives),
        "sources_after_two": len(after_both.sources),
        "left_replay_status": replay_left_status,
        "right_replay_status": replay_right_status,
        "left_replay_identity": replay_left == after_both,
        "right_replay_identity": replay_right == after_both,
        "mixed_no_status": no_status,
        "mixed_no_identity": mixed_no == mixed,
        "mixed_retry_status": retry_status,
        "mixed_retry_records": len(mixed_retry.records) - 1,
        "route_cross_write_hits": (
            compiler["left_hits_right_writes"] + compiler["right_hits_left_writes"]
        ),
        "left_guard_sites": len(execution_support[left.label]),
        "right_guard_sites": len(execution_support[right.label]),
        "joint_reserved_sites": len(joint_corridor),
        "joint_route_overlap": len(
            execution_support[left.label] & execution_support[right.label]
        ),
        "initial_corridor_record_hits": len(initial_record_sites & joint_corridor),
        "overwriting": overwrite,
    }


def covariance_acceptance_certificate(tie_break: bool = False) -> dict[str, object]:
    left, right = symmetric_pair()
    compiler = symmetric_compiler_certificate(False)
    accepted = (left,) if tie_break else (left, right)
    failures = 0
    cases = 0
    for rotation in block71.ROTATIONS:
        for translation in ((0, 0, 0), (7, -5, 3)):
            transformed_events = tuple(
                block89.transform_event(rotation, translation, event)
                for event in (left, right)
            )
            transformed_left_actions = tuple(
                transform_action(rotation, translation, action)
                for action in compiler["left"]["actions"]
            )
            transformed_right_actions = tuple(
                transform_action(rotation, translation, action)
                for action in compiler["right_actions"]
            )
            left_support = {
                site for action in transformed_left_actions for site in action.sites
            }
            right_support = {
                site for action in transformed_right_actions for site in action.sites
            }
            failures += any(
                len(action.sites) == 2 and block71.distance(*action.sites) != 1
                for action in transformed_left_actions + transformed_right_actions
            )
            failures += not semantic_support(transformed_events[0]).isdisjoint(
                semantic_support(transformed_events[1])
            )
            failures += bool(
                left_support & block89.event_support(transformed_events[1], "write")
            )
            failures += bool(
                right_support & block89.event_support(transformed_events[0], "write")
            )
            cases += 1
    return {
        "accepted": len(accepted),
        "covariance_cases": cases,
        "covariance_failures": failures,
        "words_swap_under_involution": compiler["words_swap_under_involution"],
        "full_pair_invariant": not tie_break,
        "deterministic_selector_used": tie_break,
        "route_overlap_allowed": compiler["route_overlap"],
    }


def ideal_event_actions(
    event: block89.EventSpec,
) -> tuple[block72.PhysicalAction, ...]:
    actions = [
        block72.PhysicalAction(
            gate.kind,
            tuple(
                event_site(event, block71.STARTS[ROLES[wire]])
                for wire in gate.wires
            ),
            gate.matrix,
        )
        for gate in block71.dilation_word()
    ]
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
        actions.append(
            block72.PhysicalAction(
                "SWAP",
                (
                    event_site(event, block71.STARTS[role]),
                    event_site(event, target),
                ),
            )
        )
    return tuple(actions)


def semantic_overlap_witness(hide_collision: bool = False) -> dict[str, object]:
    left = block89.EventSpec("left", block89.IDENTITY_ROTATION, (0, 0, 0))
    right = block89.EventSpec(
        "right", SEMANTIC_OVERLAP_ROTATION, SEMANTIC_OVERLAP_TRANSLATION
    )
    sites = tuple(sorted(semantic_support(left) | semantic_support(right)))
    requirements = block89.fixed_requirements(left)
    requirements.update(block89.fixed_requirements(right))
    requirements.setdefault(event_site(left, block71.STARTS["M"]), 0)
    requirements.setdefault(event_site(right, block71.STARTS["M"]), 0)
    bits = tuple(requirements.get(site, 1) for site in sites)
    site_index = {site: index for index, site in enumerate(sites)}
    state = {bits: 1.0 + 0.0j}
    left_actions = ideal_event_actions(left)
    right_actions = ideal_event_actions(right)
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
    shared = semantic_support(left) & semantic_support(right)
    return {
        "simultaneously_ready": block89.simultaneously_ready(left, right),
        "write_overlap": len(
            block89.event_support(left, "write")
            & block89.event_support(right, "write")
        ),
        "semantic_overlap": len(shared),
        "core_overlap": len(block89.event_support(left) & block89.event_support(right)),
        "shared_site": tuple(shared),
        "shared_roles": ("left:B", "right:R"),
        "union_sites": len(sites),
        "left_right_terms": len(left_right),
        "right_left_terms": len(right_left),
        "order_residual": residual,
    }


@lru_cache(maxsize=None)
def ambient_route_record_obstruction_certificate(
    ignore_corridor_guard: bool = False,
) -> dict[str, object]:
    """Expose why swap-back needs a Record-free, jointly reserved corridor."""

    left, right = symmetric_pair()
    compiler = symmetric_compiler_certificate(False)
    left_support = compiler["left"]["support"]
    right_support = compiler["right_support"]
    joint_corridor = left_support | right_support
    ambient_site = (-2, -1, 0)
    pair_semantic = semantic_support(left) | semantic_support(right)
    pair_compact = block89.event_support(left) | block89.event_support(right)

    touches = tuple(
        (index, action)
        for index, action in enumerate(compiler["left"]["actions"])
        if ambient_site in action.sites
    )
    first_index, first_action = touches[0]
    sites = tuple(sorted(left_support))
    site_index = {site: index for index, site in enumerate(sites)}
    requirements = block89.fixed_requirements(left)
    requirements.update(block89.fixed_requirements(right))
    requirements.setdefault(event_site(left, block71.STARTS["M"]), 0)
    requirements.setdefault(event_site(right, block71.STARTS["M"]), 0)
    bits = [requirements.get(site, 0) for site in sites]
    bits[site_index[ambient_site]] = 1
    initial_state = {tuple(bits): 1.0 + 0.0j}
    prefix_state = block86.apply_physical_actions(
        initial_state,
        compiler["left"]["actions"][:first_index],
        site_index,
    )
    after_touch = block86.apply_physical_actions(
        prefix_state,
        (first_action,),
        site_index,
    )
    final_state = block86.apply_physical_actions(
        initial_state,
        compiler["left"]["actions"],
        site_index,
    )

    def marginal(state: dict[tuple[int, ...], complex]) -> tuple[float, float]:
        wire = site_index[ambient_site]
        return tuple(
            float(
                sum(abs(amplitude) ** 2 for key, amplitude in state.items() if key[wire] == value)
            )
            for value in (0, 1)
        )

    before_marginal = marginal(prefix_state)
    after_marginal = marginal(after_touch)
    final_marginal = marginal(final_state)

    initial_ledger = block89.initial_ledger((left, right))
    records = dict(initial_ledger.records)
    records[ambient_site] = block71.K1
    ambient_ledger = block89.canonical_ledger(
        records,
        dict(initial_ledger.resources),
        set(initial_ledger.archives),
        set(initial_ledger.sources),
        set(initial_ledger.reservations),
    )
    guarded_support = None if ignore_corridor_guard else left_support
    status, guarded_output = apply_semantic_branch(
        ambient_ledger,
        left,
        (0, 1),
        execution_support=guarded_support,
    )
    ready_neighbor = event_site(left, block71.STARTS["B"])
    return {
        "ambient_site": ambient_site,
        "ambient_content_is_K1": records[ambient_site] == block71.K1,
        "outside_pair_semantic": ambient_site not in pair_semantic,
        "outside_pair_compact_cores": ambient_site not in pair_compact,
        "inside_left_route_support": ambient_site in left_support,
        "left_guard_sites": len(left_support),
        "right_guard_sites": len(right_support),
        "joint_reserved_sites": len(joint_corridor),
        "joint_route_overlap": len(left_support & right_support),
        "first_touch_zero_index": first_index,
        "first_touch_one_index": first_index + 1,
        "first_touch_kind": first_action.kind,
        "first_touch_sites": first_action.sites,
        "ready_neighbor": ready_neighbor,
        "ready_neighbor_is_left_B": ready_neighbor == first_action.sites[0],
        "ready_neighbor_initial_value": requirements[ready_neighbor],
        "before_marginal": before_marginal,
        "after_marginal": after_marginal,
        "final_marginal": final_marginal,
        "primitive_permanence_violated": (
            abs(before_marginal[0] - after_marginal[0]) > TOL
            or abs(before_marginal[1] - after_marginal[1]) > TOL
        ),
        "macro_restores_record_factor": (
            abs(final_marginal[0]) < TOL and abs(final_marginal[1] - 1.0) < TOL
        ),
        "guarded_status": status,
        "guarded_state_identity": guarded_output == ambient_ledger,
        "complete_route_support_guarded": not ignore_corridor_guard,
    }


def resource_boundary_certificate(
    erase_source: bool = False,
    fake_renewal: bool = False,
    ignore_ambient_record: bool = False,
) -> dict[str, object]:
    left, right = symmetric_pair()
    compiler = symmetric_compiler_certificate(False)
    ledger = block89.initial_ledger((left, right))
    _, ledger = apply_semantic_branch(
        ledger,
        left,
        (0, 1),
        execution_support=compiler["left"]["support"],
        erase_source=erase_source,
    )
    _, ledger = apply_semantic_branch(
        ledger,
        right,
        (1, 0),
        execution_support=compiler["right_support"],
        erase_source=erase_source,
    )
    resources = dict(ledger.resources)
    if fake_renewal:
        resources = {key: "ready" for key in resources}
    continuity_failures = 0
    for root, head in ledger.sources:
        delta = {root: -1, head: 1}
        boundary = {root: 1, head: -1}
        continuity_failures += any(
            delta[site] + boundary[site] for site in delta
        )
    ambient = ambient_route_record_obstruction_certificate(ignore_ambient_record)
    return {
        "records": len(ledger.records) - 1,
        "archives": len(ledger.archives),
        "sources": len(ledger.sources),
        "spent": sum(value == "spent" for value in resources.values()),
        "continuity_failures": continuity_failures,
        "clean_genesis_supplied": False,
        "renewal_supplied": fake_renewal,
        "outcome_pointer_compiled": False,
        "physical_rate_supplied": False,
        "energy_action_supplied": False,
        "gravity_supplied": False,
        "global_covariant_route_atlas_supplied": False,
        "ambient_record_free_route_domain_supplied": False,
        "obstacle_aware_route_atlas_supplied": False,
        "fixture_corridor_guard_sites": ambient["left_guard_sites"],
        "fixture_joint_reserved_sites": ambient["joint_reserved_sites"],
        "fixture_joint_route_overlap": ambient["joint_route_overlap"],
        "ambient_record_site": ambient["ambient_site"],
        "ambient_record_outside_semantic": ambient["outside_pair_semantic"],
        "ambient_record_outside_compact_cores": ambient["outside_pair_compact_cores"],
        "ambient_record_inside_route": ambient["inside_left_route_support"],
        "ambient_first_touch_zero_index": ambient["first_touch_zero_index"],
        "ambient_first_touch_one_index": ambient["first_touch_one_index"],
        "ambient_first_touch_kind": ambient["first_touch_kind"],
        "ambient_first_touch_sites": ambient["first_touch_sites"],
        "ambient_ready_neighbor_is_left_B": ambient["ready_neighbor_is_left_B"],
        "ambient_ready_neighbor_initial_value": ambient["ready_neighbor_initial_value"],
        "ambient_before_marginal": ambient["before_marginal"],
        "ambient_after_marginal": ambient["after_marginal"],
        "ambient_final_marginal": ambient["final_marginal"],
        "ambient_primitive_permanence_violated": ambient[
            "primitive_permanence_violated"
        ],
        "ambient_macro_restores_record_factor": ambient[
            "macro_restores_record_factor"
        ],
        "ambient_guarded_status": ambient["guarded_status"],
        "ambient_guarded_state_identity": ambient["guarded_state_identity"],
        "complete_route_support_guarded": ambient["complete_route_support_guarded"],
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
        "1,134",
        "pair-aware swap-back",
        "semantic-overlap witness",
        "no TOE percentage movement",
        "not an approved primitive",
        "global covariant route atlas remains open",
        "ambient Record-free route domain remains open",
        "clean-resource genesis and renewal remain open",
        "source/action typing and gravity remain open",
    )
    return not false_progress and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--mutation",
        choices=(
            "stale_axiom",
            "miss_one_pair",
            "drop_swapback",
            "compact_collision",
            "overwrite",
            "tie_break",
            "hide_semantic_collision",
            "erase_source",
            "fake_renewal",
            "ignore_ambient_record",
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
        and authority["compiler_phrase_hits"] == 0
        and authority["current_contract"]
        and authority["current_inputs_match"]
        and authority["historical_parents_match"]
        and authority["parent_hashes"] == PARENT_SHA256
        and not authority["forced_stale"]
    )
    checks.check(
        "A-current-authority-and-exact-Block89-parent",
        authority_ok,
        f"axiom={str(authority['axiom_sha256'])[:12]}; no pair-aware compiler, route atlas, live-M2 law, or renewal is registered",
    )

    census = repairable_census_certificate(mutation == "miss_one_pair")
    census_ok = (
        census["overlap_placements"] == 2365
        and census["simultaneously_ready"] == 2230
        and census["write_overlap"] == 175
        and census["write_disjoint_semantic_overlap"] == 921
        and census["semantic_disjoint"] == 1134
        and census["unique_endpoint_pairs_per_event"] == 11
        and census["path_checks"] == 24948
        and census["path_failures"] == 0
    )
    checks.check(
        "B-all-semantic-disjoint-critical-pairs-have-cross-semantic-avoiding-NN-routes",
        census_ok,
        f"{census['semantic_disjoint']} pairs x 2 events x 11 endpoint pairs give {census['path_checks']} routes avoiding both event-semantic supports with {census['path_failures']} failures; ambient Record obstacles are outside this census",
    )

    compiler = symmetric_compiler_certificate(mutation == "drop_swapback")
    left_compiler = compiler["left"]
    equivalence = left_compiler["equivalence"]
    compiler_ok = (
        left_compiler["path_count"] == 23
        and left_compiler["physical_primitives"] == 191
        and left_compiler["support_sites"] == 32
        and left_compiler["route_macro_residual"] < TOL
        and left_compiler["non_nn_failures"] == 0
        and left_compiler["semantic_interior_hits"] == 0
        and left_compiler["other_write_hits"] == 0
        and equivalence["basis_cases"] == 256
        and equivalence["maximum_residual"] < TOL
        and equivalence["background_failures"] == 0
        and not left_compiler["dropped_swapback"]
    )
    checks.check(
        "C-exact-pair-aware-swapback-NN-semantic-compiler",
        compiler_ok,
        f"191 primitives/32 sites and 23 restored routes give 256/256 semantic-basis agreement at {equivalence['maximum_residual']:.2e}; semantic-interior/cross-write hits={left_compiler['semantic_interior_hits']}/{left_compiler['other_write_hits']}",
    )

    collision = repaired_collision_certificate(mutation == "compact_collision")
    collision_ok = (
        collision["old_compact_residual"] > TOL
        and collision["new_residual"] < TOL
        and collision["left_right_terms"] == 256
        and collision["right_left_terms"] == 256
        and collision["physical_primitives_each"] == 191
        and collision["support_each"] == 32
        and collision["route_overlap"] == 6
        and collision["cross_write_hits"] == 0
        and collision["state_invariant"]
        and collision["words_swap_under_involution"]
        and collision["abstract_operator_supports_disjoint"]
        and not collision["compact_collision_forced"]
    )
    checks.check(
        "D-hostile-symmetric-pair-physical-collision-repaired",
        collision_ok,
        f"compact residual {collision['old_compact_residual']:.6f} falls to {collision['new_residual']:.2e}; two 191-primitive words overlap on {collision['route_overlap']} transient sites but hit 0 cross-event writes",
    )

    ledger = repaired_ledger_certificate(mutation == "overwrite")
    ledger_ok = (
        ledger["branch_pairs"] == 36
        and ledger["branch_residual"] < TOL
        and abs(ledger["branch_normalization"] - 1) < TOL
        and ledger["ledger_cases"] == 36
        and ledger["ledger_mismatches"] == 0
        and ledger["source_failures"] == 0
        and ledger["decode_failures"] == 0
        and ledger["records_after_two"] == 6
        and ledger["spent_after_two"] == 2
        and ledger["archives_after_two"] == 2
        and ledger["sources_after_two"] == 2
        and ledger["left_replay_status"] == "guard_refusal"
        and ledger["right_replay_status"] == "guard_refusal"
        and ledger["left_replay_identity"]
        and ledger["right_replay_identity"]
        and ledger["mixed_no_status"] == "no_event"
        and ledger["mixed_no_identity"]
        and ledger["mixed_retry_status"] == "event"
        and ledger["mixed_retry_records"] == 6
        and ledger["route_cross_write_hits"] == 0
        and ledger["left_guard_sites"] == 32
        and ledger["right_guard_sites"] == 32
        and ledger["joint_reserved_sites"] == 58
        and ledger["joint_route_overlap"] == 6
        and ledger["initial_corridor_record_hits"] == 0
        and not ledger["overwriting"]
    )
    checks.check(
        "E-all-36-branches-complete-ledger-and-depth-two-liveness",
        ledger_ok,
        f"36 branch pairs have {ledger['ledger_mismatches']} ledger mismatches; both events write {ledger['records_after_two']} Records, spend {ledger['spent_after_two']} packets, and replay as {ledger['left_replay_status']}/{ledger['right_replay_status']}",
    )

    covariance = covariance_acceptance_certificate(mutation == "tie_break")
    covariance_ok = (
        covariance["accepted"] == 2
        and covariance["covariance_cases"] == 48
        and covariance["covariance_failures"] == 0
        and covariance["words_swap_under_involution"]
        and covariance["full_pair_invariant"]
        and not covariance["deterministic_selector_used"]
        and covariance["route_overlap_allowed"] == 6
    )
    checks.check(
        "F-covariant-full-pair-acceptance-without-deterministic-selector",
        covariance_ok,
        f"the involution swaps the two compiled words, both events are accepted, and {covariance['covariance_cases']} transformed fixtures have {covariance['covariance_failures']} geometry failures",
    )

    semantic = semantic_overlap_witness(mutation == "hide_semantic_collision")
    semantic_ok = (
        semantic["simultaneously_ready"]
        and semantic["write_overlap"] == 0
        and semantic["semantic_overlap"] == 1
        and semantic["core_overlap"] == 1
        and semantic["shared_roles"] == ("left:B", "right:R")
        and semantic["union_sites"] == 15
        and semantic["left_right_terms"] == 256
        and semantic["right_left_terms"] == 128
        and semantic["order_residual"] > TOL
    )
    checks.check(
        "G-exact-semantic-overlap-residual-needs-genuine-joint-collision",
        semantic_ok,
        f"a ready write-disjoint pair shares left:B=right:R at {semantic['shared_site']} and its 256/128 ideal orders differ by {semantic['order_residual']:.9g}",
    )

    resources = resource_boundary_certificate(
        mutation == "erase_source",
        mutation == "fake_renewal",
        mutation == "ignore_ambient_record",
    )
    resource_ok = (
        resources["records"] == 6
        and resources["archives"] == 2
        and resources["sources"] == 2
        and resources["spent"] == 2
        and resources["continuity_failures"] == 0
        and not resources["clean_genesis_supplied"]
        and not resources["renewal_supplied"]
        and not resources["outcome_pointer_compiled"]
        and not resources["physical_rate_supplied"]
        and not resources["energy_action_supplied"]
        and not resources["gravity_supplied"]
        and not resources["global_covariant_route_atlas_supplied"]
        and not resources["ambient_record_free_route_domain_supplied"]
        and not resources["obstacle_aware_route_atlas_supplied"]
        and resources["fixture_corridor_guard_sites"] == 32
        and resources["fixture_joint_reserved_sites"] == 58
        and resources["fixture_joint_route_overlap"] == 6
        and resources["ambient_record_site"] == (-2, -1, 0)
        and resources["ambient_record_outside_semantic"]
        and resources["ambient_record_outside_compact_cores"]
        and resources["ambient_record_inside_route"]
        and resources["ambient_first_touch_zero_index"] == 34
        and resources["ambient_first_touch_one_index"] == 35
        and resources["ambient_first_touch_kind"] == "SWAP"
        and resources["ambient_first_touch_sites"]
        == ((-1, -1, 0), (-2, -1, 0))
        and resources["ambient_ready_neighbor_is_left_B"]
        and resources["ambient_ready_neighbor_initial_value"] == 0
        and abs(resources["ambient_before_marginal"][0]) < TOL
        and abs(resources["ambient_before_marginal"][1] - 1.0) < TOL
        and abs(resources["ambient_after_marginal"][0] - 0.5) < TOL
        and abs(resources["ambient_after_marginal"][1] - 0.5) < TOL
        and abs(resources["ambient_final_marginal"][0]) < TOL
        and abs(resources["ambient_final_marginal"][1] - 1.0) < TOL
        and resources["ambient_primitive_permanence_violated"]
        and resources["ambient_macro_restores_record_factor"]
        and resources["ambient_guarded_status"] == "guard_refusal"
        and resources["ambient_guarded_state_identity"]
        and resources["complete_route_support_guarded"]
    )
    checks.check(
        "H-exact-resource-source-and-physical-law-boundary",
        resource_ok,
        f"a K1 Record at {resources['ambient_record_site']} is changed 1->(1/2,1/2) by zero-based primitive 34 unless the full 32-site support is guarded; the repaired transaction refuses it unchanged, while corridor supply/atlas, renewal, pointer, cadence, energy/action, and gravity remain open",
    )

    boundary_ok = boundary_surface_ok(mutation == "false_progress")
    checks.check(
        "I-bounded-repair-no-go-discipline-and-TOE-accounting",
        boundary_ok,
        "the N1-N8 surface credits the exact symmetric collision repair and 1,134-route existence result while preserving the semantic-collision, law-selection, renewal, source/action, gravity, retention, and no-score boundaries",
    )

    print(
        "METRICS repairable_semantic_disjoint={} route_checks={} compiler_primitives={} compiler_support={} repaired_residual={:.9g} residual_semantic_overlap={} residual_write_overlap={} semantic_witness_residual={:.9g}".format(
            census["semantic_disjoint"],
            census["path_checks"],
            collision["physical_primitives_each"],
            collision["support_each"],
            collision["new_residual"],
            census["write_disjoint_semantic_overlap"],
            census["write_overlap"],
            semantic["order_residual"],
        )
    )
    print("N5_RESOLUTION per_element: all 29 logical gates, 23 physical routes, six branch labels, 36 branch pairs, two packets, and two source edges are typed")
    print("N5_RESOLUTION per_site: each event has eight semantic sites, 32 guarded route sites, zero cross-event semantic/write hits, six transient pair-route overlaps, and one exact ambient-Record obstruction on the hostile fixture")
    print("N5_RESOLUTION per_mode: compact-collision, swap-back repair, both macro orders, event, no-event, refusal, replay, semantic-overlap, and transformed-pair modes are checked")
    print("N5_RESOLUTION per_block: current authority, Block89 receipt, route macros, full semantic unitary, branch maps, complete ledger, compiler symmetry, and resource boundary are checked")
    print("N5_RESOLUTION lattice_wide: all 1,134 finite ready semantic-disjoint routed collisions have cross-semantic path-existence checks only; a supplied Record-free route domain, obstacle-aware global atlas, arbitrary event sets, renewal, time, energy, and gravity are not claimed")
    print("BOUNDARY: on a supplied Record-free jointly reserved corridor, pair-aware swap-back routing repairs the exact Block89 symmetric physical collision and permits both events without a selector; an ambient permanent Record on a route-only site forces identity refusal, 921 write-disjoint semantic-overlap pairs include an exact noncommuting witness, 175 ready pairs overlap in writes, and current authority supplies neither the corridor domain/compiler atlas nor live-M2 formation, outcome compilation, renewal, cadence, source/action typing, or gravity")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
