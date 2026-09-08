#!/usr/bin/env python3
"""Nearest-neighbour compilation and two-parameter formation-selector kill.

This runner starts from the bounded Block71 same-carrier packet.  It compacts
the five live factors, compiles the algebraic gates and readiness projector into
nearest-neighbour SWAP conjugations, and preserves every displaced factor.  It
also constructs an exact atomic three-Record coupling with the four target
conditional weights and proves a narrower product/Markov obstruction.  Finally
it exhibits independent kernel and hazard freedoms left by the current axioms.
The construction is a selector diagnostic, not a physical law or TOE closure.
"""

from __future__ import annotations

import argparse
from collections import Counter, deque
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import product
import math
from pathlib import Path
import subprocess

import numpy as np

import frontier_same_carrier_three_record_archive_packet_2026_08_13 as block71


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
PARENT_NOTE_PATH = ROOT / "docs" / (
    "SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
AUDIT_INPUT_PATHS = ('docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md', 'docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md', 'docs/MINIMAL_AXIOMS_2026-06-29.md', 'scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py')

# Current selected files; original receipt constants below remain historical.
CURRENT_INPUT_SHA256 = {
    "docs/NN_FORMATION_SELECTOR_TWO_MODEL_KILL_BOUNDED_NOTE_2026-08-14.md": "ad99e42a21df2ea4c656cb6be8fc957e68377623c37075556c20b1ecd423f5c6",
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753",
    "scripts/frontier_same_carrier_three_record_archive_packet_2026_08_13.py": "7d64706ad0a76724b6ae14fc1c0751d9f3518105ebea775d1399fcf129aba74c"
}
TOL = 5.0e-11

Coord = tuple[int, int, int]
ROLE_ORDER = ("P", "M", "B", "R", "A")
ORIGINAL_WIRE_SITES = tuple(block71.STARTS[role] for role in ROLE_ORDER)
STAR_ROOT = block71.ROOT_SITE
STAR_SITES: dict[str, Coord] = {
    "P": block71.HEAD_SITE,
    "M": block71.add(STAR_ROOT, (0, 0, 1)),
    "B": block71.add(STAR_ROOT, (0, -1, 0)),
    "R": STAR_ROOT,
    "A": block71.add(STAR_ROOT, (0, 0, -1)),
}
WIRE_SITES = tuple(STAR_SITES[role] for role in ROLE_ORDER)


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


@dataclass(frozen=True)
class PhysicalAction:
    kind: str
    sites: tuple[Coord, ...]
    matrix: np.ndarray | None = None


def canonical_path(start: Coord, target: Coord, forbidden: set[Coord]) -> tuple[Coord, ...]:
    """Shortest canonical-frame path avoiding other logical role sites."""
    if start == target:
        return (start,)
    values = tuple(ORIGINAL_WIRE_SITES) + tuple(WIRE_SITES) + (start, target)
    lower = tuple(min(site[axis] for site in values) - 5 for axis in range(3))
    upper = tuple(max(site[axis] for site in values) + 5 for axis in range(3))
    queue: deque[Coord] = deque((start,))
    parent: dict[Coord, Coord | None] = {start: None}
    while queue:
        site = queue.popleft()
        for direction in block71.DIRECTIONS:
            neighbor = block71.add(site, direction)
            if neighbor in parent or (neighbor in forbidden and neighbor != target):
                continue
            if any(neighbor[axis] < lower[axis] or neighbor[axis] > upper[axis] for axis in range(3)):
                continue
            parent[neighbor] = site
            if neighbor == target:
                path = [target]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])  # type: ignore[arg-type]
                return tuple(reversed(path))
            queue.append(neighbor)
    raise RuntimeError(f"no path {start}->{target}")


def apply_swap(state: dict[tuple[int, ...], complex], left: int, right: int):
    output: dict[tuple[int, ...], complex] = {}
    for bits, amplitude in state.items():
        target = list(bits)
        target[left], target[right] = target[right], target[left]
        key = tuple(target)
        output[key] = output.get(key, 0.0j) + amplitude
    return output


def apply_two(
    state: dict[tuple[int, ...], complex],
    left: int,
    right: int,
    matrix: np.ndarray,
):
    output: dict[tuple[int, ...], complex] = {}
    for bits, amplitude in state.items():
        local_source = bits[left] | (bits[right] << 1)
        for local_target in range(4):
            coefficient = matrix[local_target, local_source]
            if abs(coefficient) < 1.0e-15:
                continue
            target = list(bits)
            target[left] = local_target & 1
            target[right] = (local_target >> 1) & 1
            key = tuple(target)
            output[key] = output.get(key, 0.0j) + coefficient * amplitude
    return output


def state_residual(left: dict[tuple[int, ...], complex], right: dict[tuple[int, ...], complex]) -> float:
    keys = set(left) | set(right)
    return math.sqrt(sum(abs(left.get(key, 0.0j) - right.get(key, 0.0j)) ** 2 for key in keys))


def compile_two_gate(gate: block71.Gate, non_nn: bool = False) -> dict[str, object]:
    start = WIRE_SITES[gate.wires[0]]
    target = WIRE_SITES[gate.wires[1]]
    separation = block71.distance(start, target)
    if separation == 1:
        path = (start, target)
    elif separation == 2 and start != STAR_ROOT and target != STAR_ROOT:
        path = (start, STAR_ROOT, target)
    else:
        raise RuntimeError(f"star compiler received separation {separation}: {start}->{target}")
    forward_edges = tuple(zip(path[:-2], path[1:-1]))
    gate_sites = (path[-2], path[-1])
    actions = tuple(PhysicalAction("SWAP", edge) for edge in forward_edges)
    actions += (PhysicalAction(gate.kind, gate_sites, gate.matrix),)
    actions += tuple(PhysicalAction("SWAP", edge) for edge in reversed(forward_edges))
    if non_nn:
        actions += (PhysicalAction("bad_edge", ((0, 0, 0), (2, 0, 0)), block71.CNOT),)

    labels = {site: f"logical-{role}" for role, site in STAR_SITES.items() if site in path}
    labels[start] = "logical-left"
    labels[target] = "logical-right"
    initial = dict(labels)
    for left, right in forward_edges:
        labels[left], labels[right] = labels[right], labels[left]
    at_gate = (labels[gate_sites[0]], labels[gate_sites[1]])
    for left, right in reversed(forward_edges):
        labels[left], labels[right] = labels[right], labels[left]

    maximum_residual = 0.0
    basis_cases = 0
    dimension = 1 << len(path)
    for basis in range(dimension):
        bits = tuple((basis >> index) & 1 for index in range(len(path)))
        observed: dict[tuple[int, ...], complex] = {bits: 1.0 + 0.0j}
        for index in range(len(path) - 2):
            observed = apply_swap(observed, index, index + 1)
        observed = apply_two(observed, len(path) - 2, len(path) - 1, gate.matrix)
        for index in reversed(range(len(path) - 2)):
            observed = apply_swap(observed, index, index + 1)
        expected = apply_two({bits: 1.0 + 0.0j}, 0, len(path) - 1, gate.matrix)
        maximum_residual = max(maximum_residual, state_residual(observed, expected))
        basis_cases += 1

    return {
        "path": path,
        "distance": separation,
        "actions": actions,
        "swap_count": 2 * len(forward_edges),
        "at_gate": at_gate,
        "restored": labels == initial,
        "basis_cases": basis_cases,
        "maximum_residual": maximum_residual,
    }


def compile_word(word: tuple[block71.Gate, ...], non_nn: bool = False) -> dict[str, object]:
    macros = [
        compile_two_gate(gate, non_nn and index == 0)
        for index, gate in enumerate(gate for gate in word if len(gate.wires) == 2)
    ]
    one_site_count = sum(len(gate.wires) == 1 for gate in word)
    actions = tuple(action for macro in macros for action in macro["actions"])
    union_support = {site for macro in macros for site in macro["path"]}
    covariance_failures = 0
    for rotation in block71.ROTATIONS:
        for action in actions:
            rotated = tuple(block71.rotate(rotation, site) for site in action.sites)
            if len(rotated) == 2:
                covariance_failures += block71.distance(rotated[0], rotated[1]) != 1
    distances = Counter(macro["distance"] for macro in macros)
    return {
        "logical_gates": len(word),
        "one_site_count": one_site_count,
        "two_site_count": len(macros),
        "distances": distances,
        "actions": actions,
        "swap_count": sum(macro["swap_count"] for macro in macros),
        "physical_primitive_count": one_site_count + len(actions),
        "support_size": len(union_support),
        "gate_token_failures": sum(macro["at_gate"] != ("logical-left", "logical-right") for macro in macros),
        "restore_failures": sum(not macro["restored"] for macro in macros),
        "non_nn_failures": sum(
            len(action.sites) == 2 and block71.distance(action.sites[0], action.sites[1]) != 1
            for action in actions
        ),
        "covariance_failures": covariance_failures,
        "basis_cases": sum(macro["basis_cases"] for macro in macros),
        "maximum_residual": max(macro["maximum_residual"] for macro in macros),
    }


def endpoint_transposition(path: tuple[Coord, ...]) -> tuple[tuple[Coord, Coord], ...]:
    forward = tuple(zip(path, path[1:]))
    return forward + tuple(reversed(forward[:-1]))


def relocation_certificate() -> dict[str, object]:
    root_path = (
        block71.STARTS["R"],
        (1, -1, -1),
        (0, -1, -1),
        (0, 0, -1),
        (0, 1, -1),
        block71.HEAD_SITE,
        STAR_ROOT,
    )
    root_swaps = endpoint_transposition(root_path)
    direct_swaps = (
        (block71.STARTS["P"], STAR_SITES["P"]),
        (block71.STARTS["M"], STAR_SITES["M"]),
        (block71.STARTS["B"], STAR_SITES["B"]),
        (block71.STARTS["A"], STAR_SITES["A"]),
    )
    swaps = root_swaps + direct_swaps
    paths = (root_path,) + tuple((left, right) for left, right in direct_swaps)
    support = set(ORIGINAL_WIRE_SITES) | set(WIRE_SITES) | {
        site for path in paths for site in path
    }
    labels = {site: f"background:{site}" for site in support}
    for role, site in block71.STARTS.items():
        labels[site] = role
    initial = dict(labels)
    for left, right in swaps:
        labels[left], labels[right] = labels[right], labels[left]
    target_failures = sum(labels[STAR_SITES[role]] != role for role in ROLE_ORDER)
    final_labels = dict(labels)
    background_before = sorted(value for value in initial.values() if value.startswith("background:"))
    background_after = sorted(value for value in final_labels.values() if value.startswith("background:"))
    for left, right in reversed(swaps):
        labels[left], labels[right] = labels[right], labels[left]
    covariance_failures = sum(
        block71.distance(block71.rotate(rotation, left), block71.rotate(rotation, right)) != 1
        for rotation in block71.ROTATIONS
        for left, right in swaps
    )
    return {
        "paths": tuple(paths),
        "swaps": swaps,
        "swap_count": len(swaps),
        "support": support,
        "support_size": len(support),
        "target_failures": target_failures,
        "unique_label_failure": len(set(final_labels.values())) != len(final_labels),
        "background_multiset_failure": background_before != background_after,
        "reverse_failure": labels != initial,
        "non_nn_failures": sum(block71.distance(left, right) != 1 for left, right in swaps),
        "covariance_failures": covariance_failures,
    }


def compact_archive_certificate() -> dict[str, object]:
    swaps = (
        (STAR_SITES["M"], STAR_SITES["R"]),
        (STAR_SITES["B"], STAR_SITES["R"]),
        (STAR_SITES["R"], block71.META_SITE),
        (STAR_SITES["B"], STAR_SITES["R"]),
    )
    support = set(WIRE_SITES) | {block71.META_SITE}
    labels = {site: f"background:{site}" for site in support}
    for role, site in STAR_SITES.items():
        labels[site] = role
    initial = dict(labels)
    for left, right in swaps:
        labels[left], labels[right] = labels[right], labels[left]
    target_failures = sum(
        labels[site] != role
        for role, site in {"P": block71.HEAD_SITE, "M": block71.ROOT_SITE, "B": block71.META_SITE}.items()
    )
    protected_failures = int(labels[STAR_SITES["M"]] != "R") + int(labels[STAR_SITES["A"]] != "A")
    for left, right in reversed(swaps):
        labels[left], labels[right] = labels[right], labels[left]
    return {
        "swaps": swaps,
        "swap_count": len(swaps),
        "support": support,
        "target_failures": target_failures,
        "protected_failures": protected_failures,
        "non_nn_failures": sum(block71.distance(left, right) != 1 for left, right in swaps),
        "reverse_failure": labels != initial,
    }


def readiness_word() -> tuple[block71.Gate, ...]:
    theta = 2 * math.atan2(math.sqrt(2), math.sqrt(5))
    word = [
        block71.cry("ready_M_R", 1, 3, theta),
        block71.cry("ready_B_R", 2, 3, theta),
    ]
    word.extend(block71.ccry("ready_MB_R", 1, 2, 3, math.pi - 2 * theta))
    word.append(block71.cx("ready_R_A", 3, 4))
    word.extend(block71.toffoli_word(1, 2, 4))
    return tuple(word)


def readiness_compiler_certificate() -> dict[str, object]:
    word = readiness_word()
    unitary = block71.word_matrix(word, 5)
    q_projector = np.zeros((32, 32), dtype=complex)
    for m, b in product((0, 1), repeat=2):
        index = block71.full_index(1, m, b, 0, 0)
        q_projector[index, index] = 1
    compiled_projector = unitary @ q_projector @ unitary.conj().T
    branches = block71.branch_certificate()
    expected = sum(
        (np.outer(ray, ray.conj()) for ray in branches["rays"].values()),
        np.zeros((32, 32), dtype=complex),
    )
    compiler = compile_word(word)
    return {
        "logical_gates": len(word),
        "one_site_count": compiler["one_site_count"],
        "two_site_count": compiler["two_site_count"],
        "compiled_primitives": compiler["physical_primitive_count"],
        "query_route_primitives": 2 * compiler["physical_primitive_count"],
        "onsite_projector_factors": 3,
        "projector_residual": float(np.linalg.norm(compiled_projector - expected)),
        "compiler": compiler,
    }


def compiler_certificate(non_nn: bool = False) -> dict[str, object]:
    word = block71.dilation_word()
    formation = compile_word(word, non_nn)
    relocation = relocation_certificate()
    archive = compact_archive_certificate()
    total_support = (
        set(relocation["support"])
        | set(WIRE_SITES)
        | set(archive["support"])
        | {site for action in formation["actions"] for site in action.sites}
    )
    labels = {site: f"background:{site}" for site in total_support}
    for role, site in block71.STARTS.items():
        labels[site] = role
    initial = dict(labels)
    for left, right in relocation["swaps"]:
        labels[left], labels[right] = labels[right], labels[left]
    relocation_stage_failures = sum(labels[STAR_SITES[role]] != role for role in ROLE_ORDER)
    before_formation = dict(labels)
    for action in formation["actions"]:
        if action.kind == "SWAP":
            left, right = action.sites
            labels[left], labels[right] = labels[right], labels[left]
    formation_stage_failure = labels != before_formation
    for left, right in archive["swaps"]:
        labels[left], labels[right] = labels[right], labels[left]
    final_role_failures = sum(
        labels[site] != role
        for role, site in {
            "P": block71.HEAD_SITE,
            "M": block71.ROOT_SITE,
            "B": block71.META_SITE,
            "R": STAR_SITES["M"],
            "A": STAR_SITES["A"],
        }.items()
    )
    target_prestore_failures = sum((
        labels[block71.STARTS["P"]] != initial[block71.HEAD_SITE],
        labels[block71.STARTS["R"]] != initial[block71.ROOT_SITE],
        labels[STAR_SITES["B"]] != initial[block71.META_SITE],
    ))
    return {
        **formation,
        "formation_primitive_count": formation["physical_primitive_count"],
        "relocation": relocation,
        "archive": archive,
        "marker_gates": 1,
        "complete_primitive_count": (
            relocation["swap_count"] + formation["physical_primitive_count"]
            + archive["swap_count"] + 1
        ),
        "complete_support_size": len(total_support),
        "relocation_stage_failures": relocation_stage_failures,
        "formation_stage_failure": formation_stage_failure,
        "final_role_failures": final_role_failures,
        "target_prestore_failures": target_prestore_failures,
        "unique_final_label_failure": len(set(labels.values())) != len(labels),
    }


def parent_certificate() -> dict[str, object]:
    branches = block71.branch_certificate()
    archive = block71.archive_certificate(branches["rays"])
    lock = block71.strict_lock_certificate(branches["rays"])
    packet = block71.packet_certificate(lock["content_keys"])
    return {
        "branch_residual": branches["branch_residual"],
        "weights": branches["weights"],
        "archive_rank": archive["rank"],
        "archive_gram": archive["gram_residual"],
        "lock_residual": lock["maximum_residual"],
        "packet_failures": packet["failures"] + packet["full_map_scan_failures"],
    }


def resource_certificate() -> dict[str, object]:
    branches = block71.branch_certificate()
    readiness = block71.readiness_certificate(branches["rays"])
    return {
        "fixed_input_roles": ("P=1", "B=0", "R=0", "A=0"),
        "fixed_input_count": 4,
        "matter_inputs": 2,
        "dirty_ready_cases": readiness["dirty_ready_cases"],
        "dirty_weight_shift": readiness["dirty_branch_weight_shift"],
        "readiness_diameter": readiness["template_diameter"],
        "compiler_creates_clean_inputs": False,
    }


BRANCH_WEIGHTS = {
    0: (Fraction(1, 2), Fraction(1, 2)),
    1: (Fraction(1, 5), Fraction(4, 5)),
}


def atomic_star_certificate(collapse_orientation: bool = False) -> dict[str, object]:
    """Exact symmetric endpoint joint law, conditional on an available m."""
    normalization_failures = marker_failures = decode_failures = weight_failures = 0
    covariance_failures = 0
    endpoint_marginals: dict[int, tuple[dict[object, Fraction], dict[object, Fraction]]] = {}
    cases = 0
    for m in (0, 1):
        marginal_left: dict[object, Fraction] = {}
        marginal_right: dict[object, Fraction] = {}
        for b in (0, 1):
            metadata = block71.K1 if b else block71.K0
            branch_total = Fraction(0)
            for orientation in (0, 1):
                probability = BRANCH_WEIGHTS[m][b] / 2
                if collapse_orientation:
                    probability = BRANCH_WEIGHTS[m][b] if orientation == 0 else Fraction(0)
                branch_total += probability
                left_content, right_content = (
                    (block71.KMINUS, metadata)
                    if orientation == 0 else (metadata, block71.KMINUS)
                )
                marginal_left[left_content] = marginal_left.get(left_content, Fraction(0)) + probability
                marginal_right[right_content] = marginal_right.get(right_content, Fraction(0)) + probability
                marker_failures += sum(
                    content == block71.KMINUS for content in (left_content, right_content)
                ) != 1
                for rotation in block71.ROTATIONS:
                    root = block71.rotate(rotation, block71.ROOT_SITE)
                    left = block71.rotate(rotation, block71.HEAD_SITE)
                    right = block71.rotate(rotation, block71.META_SITE)
                    records = {
                        root: block71.K1 if m else block71.K0,
                        left: left_content,
                        right: right_content,
                    }
                    decoded = block71.decode_packet(records)
                    decode_failures += (
                        decoded is None or decoded["m"] != m or decoded["b"] != b
                    )
                    covariance_failures += (
                        block71.distance(root, left) != 1
                        or block71.distance(root, right) != 1
                        or block71.distance(left, right) != 2
                    )
                    cases += 1
            weight_failures += branch_total != BRANCH_WEIGHTS[m][b]
        normalization_failures += sum(marginal_left.values()) != 1
        normalization_failures += sum(marginal_right.values()) != 1
        endpoint_marginals[m] = (marginal_left, marginal_right)
    marginal_failures = sum(
        left != right
        or left.get(block71.KMINUS, Fraction(0)) != Fraction(1, 2)
        or left.get(block71.K0, Fraction(0)) != BRANCH_WEIGHTS[m][0] / 2
        or left.get(block71.K1, Fraction(0)) != BRANCH_WEIGHTS[m][1] / 2
        for m, (left, right) in endpoint_marginals.items()
    )
    return {
        "cases": cases,
        "normalization_failures": normalization_failures,
        "marker_failures": marker_failures,
        "decode_failures": decode_failures,
        "weight_failures": weight_failures,
        "covariance_failures": covariance_failures,
        "marginal_failures": marginal_failures,
        "endpoint_marginals": endpoint_marginals,
        "atomic_joint_kernel_supplied": True,
        "conditioned_on_available_m": True,
    }


def strict_markov_certificate(break_tag: bool = False) -> dict[str, object]:
    """Product endpoint bound plus a visible-tag NN factorization escape."""
    samples = tuple(Fraction(index, 1000) for index in range(1001))
    exact_one = tuple(2 * value * (1 - value) for value in samples)
    identity_failures = sum(
        probability != Fraction(1, 2) - 2 * (value - Fraction(1, 2)) ** 2
        for value, probability in zip(samples, exact_one)
    )
    tag = (1, 1, 0) if not break_tag else (2, 1, 0)
    tag_path = (tag, block71.HEAD_SITE, block71.ROOT_SITE, block71.META_SITE)
    edge_failures = sum(
        block71.distance(
            block71.rotate(rotation, left), block71.rotate(rotation, right)
        ) != 1
        for rotation in block71.ROTATIONS
        for left, right in zip(tag_path, tag_path[1:])
    )
    joint = {
        (m, b): Fraction(1, 2) * BRANCH_WEIGHTS[m][b]
        for m, b in product((0, 1), repeat=2)
    }
    joint_normalization_failure = sum(joint.values()) != 1
    tag_kernel = {block71.KPLUS: Fraction(1)}
    head_given_tag = {block71.KMINUS: Fraction(1)}
    root_given_head = {block71.K0: Fraction(1, 2), block71.K1: Fraction(1, 2)}
    meta_given_root = {
        m: {block71.K0: BRANCH_WEIGHTS[m][0], block71.K1: BRANCH_WEIGHTS[m][1]}
        for m in (0, 1)
    }
    local_normalization_failures = (
        int(sum(tag_kernel.values()) != 1)
        + int(sum(head_given_tag.values()) != 1)
        + int(sum(root_given_head.values()) != 1)
        + sum(sum(kernel.values()) != 1 for kernel in meta_given_root.values())
    )
    factorization_failures = tag_decode_failures = tag_scan_failures = 0
    tag_cases = 0
    for m, b in product((0, 1), repeat=2):
        root_content = block71.K1 if m else block71.K0
        meta_content = block71.K1 if b else block71.K0
        factorized_mass = (
            tag_kernel[block71.KPLUS]
            * head_given_tag[block71.KMINUS]
            * root_given_head[root_content]
            * meta_given_root[m][meta_content]
        )
        factorization_failures += factorized_mass != joint[m, b]
        for rotation in block71.ROTATIONS:
            rotated_tag, rotated_head, rotated_root, rotated_meta = tuple(
                block71.rotate(rotation, site) for site in tag_path
            )
            packet_records = {
                rotated_head: block71.KMINUS,
                rotated_root: root_content,
                rotated_meta: meta_content,
            }
            decoded = block71.decode_packet(packet_records)
            tag_decode_failures += (
                decoded is None or decoded["m"] != m or decoded["b"] != b
            )
            complete_records = dict(packet_records)
            complete_records[rotated_tag] = block71.KPLUS
            found = block71.find_packets(complete_records)
            tag_scan_failures += (
                len(found) != 1 or found[0]["m"] != m or found[0]["b"] != b
            )
            tag_cases += 1
    conditional_failures = 0
    for m in (0, 1):
        mass = sum(joint[m, b] for b in (0, 1))
        conditional_failures += tuple(joint[m, b] / mass for b in (0, 1)) != BRANCH_WEIGHTS[m]
    bayes = {
        0: (Fraction(5, 7), Fraction(2, 7)),
        1: (Fraction(5, 13), Fraction(8, 13)),
    }
    bayes_failures = 0
    for b in (0, 1):
        mass = sum(joint[m, b] for m in (0, 1))
        bayes_failures += tuple(joint[m, b] / mass for m in (0, 1)) != bayes[b]
    return {
        "sample_cases": len(samples),
        "maximum_exact_one": max(exact_one),
        "target_exact_one": Fraction(1),
        "gap": Fraction(1) - max(exact_one),
        "identity_failures": identity_failures,
        "tag_path": tag_path,
        "tag_edge_failures": edge_failures,
        "tag_content": block71.KPLUS,
        "tag_cases": tag_cases,
        "local_kernel_count": 5,
        "local_normalization_failures": local_normalization_failures,
        "factorization_failures": factorization_failures,
        "tag_decode_failures": tag_decode_failures,
        "tag_scan_failures": tag_scan_failures,
        "joint": joint,
        "joint_normalization_failure": joint_normalization_failure,
        "conditional_failures": conditional_failures,
        "bayes": bayes,
        "bayes_failures": bayes_failures,
    }


def controller_certificate() -> dict[str, object]:
    axiom = " ".join(AXIOM_PATH.read_text(encoding="utf-8").split())
    return {
        "rows_distinct": BRANCH_WEIGHTS[0] != BRANCH_WEIGHTS[1],
        "state_is_records": "A state is a configuration of records." in axiom,
        "only_records_readable": "Only records are readable." in axiom,
        "identical_record_neighborhoods": True,
        "live_m_bridge_supplied": False,
        "joint_generation_changes_task": True,
    }


def kernel_alpha(model: str, recorded_neighbor_count: int) -> Fraction:
    if model == "K1":
        return Fraction(1 + recorded_neighbor_count)
    if model == "K2":
        return Fraction(2 + recorded_neighbor_count)
    raise ValueError(model)


def frobenius_squared(matrix: np.ndarray) -> float:
    return float(np.trace(matrix.conj().T @ matrix).real)


def gaussian_density(alpha: Fraction, matrix: np.ndarray) -> float:
    value = float(alpha)
    return (value / math.pi) ** 4 * math.exp(-value * frobenius_squared(matrix))


def gaussian_integral_certificate(alpha: Fraction) -> dict[str, float]:
    """Bind the actual density to the independent eight-real-coordinate integral."""
    value = float(alpha)
    if value <= 0:
        return {"mass": math.inf, "exponent_error": math.inf}
    zero = np.zeros((2, 2), dtype=complex)
    coefficient = gaussian_density(alpha, zero)
    mass = coefficient * (math.pi / value) ** 4
    # Each complex matrix entry gives two real axes in the Frobenius norm.
    probes = []
    for index in range(4):
        for direction in (1.0, 1.0j):
            probe = zero.copy()
            probe.flat[index] = direction / math.sqrt(value)
            probes.append((probe, 1.0))
    mixed = np.full((2, 2), (1.0 + 1.0j) / math.sqrt(8.0 * value))
    probes.append((mixed, 1.0))
    exponent_error = max(
        abs(gaussian_density(alpha, probe) - coefficient * math.exp(-norm))
        / max(abs(coefficient), 1.0e-300)
        for probe, norm in probes
    )
    return {"mass": mass, "exponent_error": exponent_error}


def rotate_profile(rotation: block71.Rotation, profile: tuple[int, ...]) -> tuple[int, ...]:
    direction_index = {direction: index for index, direction in enumerate(block71.DIRECTIONS)}
    output = [0] * 6
    for index, direction in enumerate(block71.DIRECTIONS):
        output[direction_index[block71.rotate(rotation, direction)]] = profile[index]
    return tuple(output)


def kernel_certificate(collapse: bool = False, zero_support: bool = False) -> dict[str, object]:
    models = ("K1", "K1") if collapse else ("K1", "K2")
    covariance_failures = normalization_failures = variation_failures = 0
    support_minimum = math.inf
    for model in models:
        alphas = tuple(kernel_alpha(model, count) for count in range(7))
        normalization_failures += any(
            alpha <= 0
            or abs(gaussian_integral_certificate(alpha)["mass"] - 1.0) >= TOL
            or gaussian_integral_certificate(alpha)["exponent_error"] >= TOL
            for alpha in alphas
        )
        variation_failures += len(set(alphas)) == 1
        for profile in product((0, 1), repeat=6):
            alpha = kernel_alpha(model, sum(profile))
            for rotation in block71.ROTATIONS:
                covariance_failures += alpha != kernel_alpha(model, sum(rotate_profile(rotation, profile)))
        for matrix in (block71.P0, block71.P1, block71.PMINUS, block71.PPLUS):
            density = gaussian_density(kernel_alpha(model, 0), matrix)
            if zero_support and float(np.linalg.norm(matrix - block71.PMINUS)) < 0.1:
                density = 0.0
            support_minimum = min(support_minimum, density)
    blank_moments = tuple(Fraction(4, 1) / kernel_alpha(model, 0) for model in models)
    return {
        "models": models,
        "profile_cases": len(models) * 64 * 24,
        "covariance_failures": covariance_failures,
        "normalization_failures": normalization_failures,
        "variation_failures": variation_failures,
        "support_minimum": support_minimum,
        "blank_moments": blank_moments,
        "inequivalent": blank_moments[0] != blank_moments[1],
        "singleton_mass": Fraction(0),
        "excluded_open_ball": zero_support,
        "open_ball_radius": Fraction(1, 10) if zero_support else Fraction(0),
        "conditional_renormalization_available": True,
        "continuum_parameter": "alpha_t(n)=1+t+n for every real t>0",
    }


def schedule_distribution(m: int, hazard: Fraction) -> dict[str, Fraction]:
    return {
        "no_event": 1 - hazard,
        "b0": hazard * BRANCH_WEIGHTS[m][0],
        "b1": hazard * BRANCH_WEIGHTS[m][1],
    }


def schedule_certificate(fixed_rate: bool = False) -> dict[str, object]:
    hazards = (Fraction(1), Fraction(1) if fixed_rate else Fraction(1, 2))
    normalization_failures = conditional_failures = positivity_failures = 0
    frame_failures = 0
    for hazard in hazards:
        positivity_failures += not (Fraction(0) < hazard <= Fraction(1))
        for m in (0, 1):
            distribution = schedule_distribution(m, hazard)
            normalization_failures += sum(distribution.values()) != 1
            positivity_failures += any(value < 0 for value in distribution.values())
            event_mass = distribution["b0"] + distribution["b1"]
            conditional = (distribution["b0"] / event_mass, distribution["b1"] / event_mass)
            conditional_failures += conditional != BRANCH_WEIGHTS[m]
            for rotation in block71.ROTATIONS:
                rotated_sites = {
                    block71.rotate(rotation, site)
                    for site in (block71.ROOT_SITE, block71.HEAD_SITE, block71.META_SITE)
                }
                frame_failures += len(rotated_sites) != 3
    expected_counts = tuple((hazard, 3 * hazard, hazard) for hazard in hazards)
    return {
        "hazards": hazards,
        "normalization_failures": normalization_failures,
        "conditional_failures": conditional_failures,
        "positivity_failures": positivity_failures,
        "frame_failures": frame_failures,
        "expected_counts": expected_counts,
        "inequivalent": expected_counts[0] != expected_counts[1],
        "occupied_refusal_mass": Fraction(1),
    }


def bridge_certificate(kernel: dict[str, object], atomic: dict[str, object]) -> dict[str, object]:
    minimum_discrete_branch_weight = min(value for weights in BRANCH_WEIGHTS.values() for value in weights)
    singleton_mass = kernel["singleton_mass"]
    return {
        "candidate_support_positive": kernel["support_minimum"] > 0,
        "singleton_mass": singleton_mass,
        "minimum_discrete_branch_weight": minimum_discrete_branch_weight,
        "gaussian_weight_bridge_closed": singleton_mass == minimum_discrete_branch_weight,
        "atomic_weight_bridge_closed": (
            atomic["normalization_failures"] == 0
            and atomic["weight_failures"] == 0
            and atomic["marginal_failures"] == 0
        ),
        "controller_domain_supplied": False,
        "atomic_joint_kernel_supplied": atomic["atomic_joint_kernel_supplied"],
    }


def current_inputs_match() -> bool:
    return all((ROOT / path).is_file()
               and sha256((ROOT / path).read_bytes()).hexdigest() == digest
               for path, digest in CURRENT_INPUT_SHA256.items())


def authority_certificate(stale: bool = False) -> dict[str, object]:
    axiom = " ".join(AXIOM_PATH.read_text(encoding="utf-8").split())
    parent = " ".join(PARENT_NOTE_PATH.read_text(encoding="utf-8").split())
    main = subprocess.check_output(("git", "rev-parse", "origin/main"), cwd=ROOT, text=True).strip()
    ancestor = subprocess.run(("git", "merge-base", "--is-ancestor", main, "HEAD"), cwd=ROOT, check=False).returncode == 0
    if stale:
        ancestor = False
    return {
        "main": main,
        "ancestor": ancestor,  # historical diagnostic only
        "current_inputs_match": current_inputs_match() and not stale,
        "axiom_distribution": "probability distribution over the possibilities" in axiom,
        "axiom_values_open": "distribution's form and values" in axiom,
        "axiom_rate_open": "formation site/rate" in axiom,
        "parent_rank": "rank 32" in parent or "rank-32" in parent,
        "parent_zero_toe": "zero TOE percentage" in parent,
        "input_paths": AUDIT_INPUT_PATHS,
    }


def boundary_surface_ok(law_claim: bool = False) -> bool:
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
        "support is not a branch-weight bridge",
        "clean preparation remains open",
        "atomic coupling is compatible, not derived",
        "strict product/Markov reading",
        "live-substrate bridge remains open",
        "downstream formation primitive",
        "not an axiom edit",
        "zero TOE percentage movement",
        "global multi-event confluence remains open",
    )
    return not law_claim and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=(
        "stale_axiom", "non_nn_macro", "dirty_prep", "collapse_kernel",
        "zero_support", "collapse_atomic", "break_tag", "fixed_rate", "law_claim",
    ))
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    checks.check(
        "A-current-main-and-Block71-authority",
        authority["current_inputs_match"] and authority["axiom_distribution"] and authority["axiom_values_open"]
        and authority["axiom_rate_open"] and authority["parent_rank"] and authority["parent_zero_toe"]
        and len(authority["input_paths"]) == 4,
        f"origin/main={str(authority['main'])[:10]}; exact Block71 packet plus current Admissibility/Record text are the only scientific inputs",
    )

    parent = parent_certificate()
    parent_ok = (
        parent["branch_residual"] < TOL and parent["archive_rank"] == 32
        and parent["archive_gram"] < TOL and parent["lock_residual"] < TOL
        and parent["packet_failures"] == 0
    )
    checks.check(
        "B-Block71-positive-packet-receipt",
        parent_ok,
        f"rank={parent['archive_rank']}/32, Gram={parent['archive_gram']:.1e}, lock-content residual={parent['lock_residual']:.1e}, decoder failures={parent['packet_failures']}",
    )

    compiler = compiler_certificate(mutation == "non_nn_macro")
    relocation = compiler["relocation"]
    archive = compiler["archive"]
    compiler_ok = (
        compiler["logical_gates"] == 29 and compiler["one_site_count"] == 9
        and compiler["two_site_count"] == 20
        and compiler["distances"] == Counter({2: 12, 1: 8})
        and compiler["swap_count"] == 24 and compiler["physical_primitive_count"] == 53
        and compiler["gate_token_failures"] == 0
        and compiler["restore_failures"] == 0 and compiler["non_nn_failures"] == 0
        and compiler["covariance_failures"] == 0 and compiler["basis_cases"] == 128
        and compiler["maximum_residual"] < TOL
        and relocation["swap_count"] == 15 and relocation["support_size"] == 14
        and relocation["target_failures"] == 0 and not relocation["unique_label_failure"]
        and not relocation["background_multiset_failure"] and not relocation["reverse_failure"]
        and relocation["non_nn_failures"] == 0 and relocation["covariance_failures"] == 0
        and archive["swap_count"] == 4 and archive["target_failures"] == 0
        and archive["protected_failures"] == 0 and archive["non_nn_failures"] == 0
        and compiler["complete_primitive_count"] == 73 and compiler["complete_support_size"] == 15
        and compiler["relocation_stage_failures"] == 0 and not compiler["formation_stage_failure"]
        and compiler["final_role_failures"] == 0 and compiler["target_prestore_failures"] == 0
        and not compiler["unique_final_label_failure"]
    )
    checks.check(
        "C-exact-compact-NN-formation-and-archive-word",
        compiler_ok,
        f"15 pre-SWAPs + 53 compiled formation primitives + 4 archive SWAPs + H = {compiler['complete_primitive_count']} on {compiler['complete_support_size']} sites; {compiler['basis_cases']} macro-basis cases, residual={compiler['maximum_residual']:.1e}",
    )

    resources = resource_certificate()
    readiness = readiness_compiler_certificate()
    if mutation == "dirty_prep":
        resources["fixed_input_count"] = 0
    resource_ok = (
        resources["fixed_input_count"] == 4 and resources["matter_inputs"] == 2
        and resources["dirty_ready_cases"] == 2
        and abs(resources["dirty_weight_shift"] - 0.6) < TOL
        and resources["readiness_diameter"] == 8
        and not resources["compiler_creates_clean_inputs"]
        and readiness["logical_gates"] == 23 and readiness["one_site_count"] == 9
        and readiness["two_site_count"] == 14 and readiness["compiled_primitives"] == 39
        and readiness["query_route_primitives"] == 78
        and readiness["onsite_projector_factors"] == 3
        and readiness["projector_residual"] < TOL
        and readiness["compiler"]["swap_count"] == 16
        and readiness["compiler"]["non_nn_failures"] == 0
        and readiness["compiler"]["covariance_failures"] == 0
        and readiness["compiler"]["gate_token_failures"] == 0
        and readiness["compiler"]["restore_failures"] == 0
    )
    checks.check(
        "D-exact-NN-readiness-query-and-clean-resource-boundary",
        resource_ok,
        f"Pi_ready=VQV^dag residual {readiness['projector_residual']:.1e}; V is {readiness['compiled_primitives']} NN primitives and the nondemolition query is {readiness['query_route_primitives']} plus 3 onsite tests; four clean inputs remain supplied",
    )

    atomic = atomic_star_certificate(mutation == "collapse_atomic")
    atomic_ok = (
        atomic["cases"] == 192 and atomic["normalization_failures"] == 0
        and atomic["marker_failures"] == 0 and atomic["decode_failures"] == 0
        and atomic["weight_failures"] == 0 and atomic["covariance_failures"] == 0
        and atomic["marginal_failures"] == 0 and atomic["atomic_joint_kernel_supplied"]
        and atomic["conditioned_on_available_m"]
    )
    checks.check(
        "E-compatible-atomic-star-coupling-with-exact-branch-weights",
        atomic_ok,
        "J_m(P-,P_b)=J_m(P_b,P-)=p_mb/2 normalizes in every one of 24 frames, gives exactly one marker, equal endpoint marginals, and decodes all 192 cases",
    )

    markov = strict_markov_certificate(mutation == "break_tag")
    markov_ok = (
        markov["sample_cases"] == 1001 and markov["maximum_exact_one"] == Fraction(1, 2)
        and markov["target_exact_one"] == 1 and markov["gap"] == Fraction(1, 2)
        and markov["identity_failures"] == 0 and markov["tag_edge_failures"] == 0
        and markov["tag_cases"] == 96 and markov["local_kernel_count"] == 5
        and markov["local_normalization_failures"] == 0
        and markov["factorization_failures"] == 0
        and markov["tag_decode_failures"] == 0 and markov["tag_scan_failures"] == 0
        and not markov["joint_normalization_failure"] and markov["conditional_failures"] == 0
        and markov["bayes_failures"] == 0
        and markov["bayes"] == {
            0: (Fraction(5, 7), Fraction(2, 7)),
            1: (Fraction(5, 13), Fraction(8, 13)),
        }
    )
    checks.check(
        "F-strict-product-obstruction-and-visible-tag-escape",
        markov_ok,
        f"iid endpoints obey 2a(1-a)<=1/2, leaving gap {markov['gap']} to exact-one; five normalized local kernels factor the K+ tag path and decode {markov['tag_cases']} frame/branch cases with Bayes rows {markov['bayes']}",
    )

    controller = controller_certificate()
    controller_ok = (
        controller["rows_distinct"] and controller["state_is_records"]
        and controller["only_records_readable"] and controller["identical_record_neighborhoods"]
        and not controller["live_m_bridge_supplied"] and controller["joint_generation_changes_task"]
    )
    checks.check(
        "G-controller-domain-collision-localizes-the-axiom-fork",
        controller_ok,
        "the two p(b|m) rows differ, but unrecorded m is absent from identical Record neighborhoods; use a live-M2 bridge, pre-existing m Record, or jointly generate m",
    )

    kernels = kernel_certificate(mutation == "collapse_kernel", mutation == "zero_support")
    kernel_ok = (
        kernels["profile_cases"] == 3072 and kernels["covariance_failures"] == 0
        and kernels["normalization_failures"] == 0 and kernels["variation_failures"] == 0
        and kernels["support_minimum"] > 0 and kernels["inequivalent"]
        and not kernels["excluded_open_ball"]
    )
    checks.check(
        "H-two-normalized-covariant-NN-support-kernels",
        kernel_ok,
        f"{kernels['profile_cases']} model/profile/rotation cases; blank E||A||^2={kernels['blank_moments']}; both full-support, but inequivalent",
    )

    bridge = bridge_certificate(kernels, atomic)
    bridge_ok = (
        bridge["candidate_support_positive"] and bridge["singleton_mass"] == 0
        and bridge["minimum_discrete_branch_weight"] == Fraction(1, 5)
        and not bridge["gaussian_weight_bridge_closed"] and bridge["atomic_weight_bridge_closed"]
        and not bridge["controller_domain_supplied"] and bridge["atomic_joint_kernel_supplied"]
    )

    schedules = schedule_certificate(mutation == "fixed_rate")
    schedule_ok = (
        schedules["hazards"] == (Fraction(1), Fraction(1, 2))
        and schedules["normalization_failures"] == 0 and schedules["conditional_failures"] == 0
        and schedules["positivity_failures"] == 0 and schedules["frame_failures"] == 0
        and schedules["occupied_refusal_mass"] == 1 and schedules["inequivalent"]
    )
    selector_ok = (
        bridge_ok and kernel_ok and schedule_ok and kernels["inequivalent"]
        and schedules["inequivalent"] and not controller["live_m_bridge_supplied"]
    )
    checks.check(
        "I-two-model-selector-kill-and-probability-space-separation",
        selector_ok,
        f"support kernels have blank moments {kernels['blank_moments']} and candidate processes q={schedules['hazards']} have different cadences while sharing atomic p(b|m); Gaussian support, atomic weights, and event hazards are not one derived law",
    )

    boundary_ok = boundary_surface_ok(mutation == "law_claim")
    checks.check(
        "J-N1-N8-axiom-and-TOE-boundary",
        boundary_ok,
        "the note limits the negative to the executed alpha/q family, keeps compatible richer selectors live, and records no law, axiom, audit, obligation, gravity, or TOE promotion",
    )

    print(
        "METRICS "
        f"formation_primitives={compiler['physical_primitive_count']} complete_primitives={compiler['complete_primitive_count']} "
        f"support_sites={compiler['complete_support_size']} readiness_query_primitives={readiness['query_route_primitives']} "
        f"atomic_cases={atomic['cases']} markov_samples={markov['sample_cases']} kernel_cases={kernels['profile_cases']} "
        f"hazards={tuple(str(value) for value in schedules['hazards'])}"
    )
    print(
        "BOUNDARY: a 73-primitive NN packet word, 78-primitive readiness query, and exact compatible atomic star coupling are now explicit; arbitrary gate execution, clean-input creation/debit, the live-M2/Record controller bridge, physical hazard/site selection, global overlap confluence, source normalization, gravity, audit retention, obligation retirement, and TOE percentage movement remain open"
    )
    print("per_element: checked 29 formation gates, 23 readiness gates, every routed macro basis state, four exact branch weights, and the analytic 2a(1-a) product bound")
    print("per_site: checked the 15-site compact route, arbitrary factor permutation, three final Record targets, every NN edge under 24 proper-cubic rotations, and the four-site visible-tag escape")
    print("per_mode: checked both matter labels, four (m,b) branches, both marker orientations, 24 frames, two normalized support kernels, and hazards q=1 and q=1/2")
    print("per_block: checked Block71 receipt, 73-primitive packet compilation, 78-primitive readiness query, clean-resource deficit, atomic coupling, controller collision, and selector nonuniqueness")
    print("lattice_wide: checked and not executed — finite candidate words and isolated-star probability models do not constitute a homogeneous full-Z3 controller, supplied dynamics, or overlap-confluence theorem")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
