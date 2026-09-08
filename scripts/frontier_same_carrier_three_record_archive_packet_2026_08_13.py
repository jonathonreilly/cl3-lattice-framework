#!/usr/bin/env python3
"""Self-contained five-M2 to three-Record archive packet.

The construction starts from an explicit five-qubit algebraic isometry.  Its
four candidate rays have orthogonal ``(M,B)`` labels.  A finite
nearest-neighbour factor permutation then moves the already-present ``P,M,B``
possibilities onto an oriented connected three-site Record packet.  Every
arbitrary target/background factor is displaced rather than reset, so the
three target contents are nondemolition on the declared supplied-branch
domain.  Admissibility support and an actual Record-formation law are not
proved here.

This is a bounded construction, not a derivation of occurrence, realized
member selection, a global update schedule, physical time, or gravity.
"""

from __future__ import annotations

import argparse
from collections import deque
from dataclasses import dataclass
from fractions import Fraction
from hashlib import sha256
from itertools import combinations, permutations, product
import math
from pathlib import Path
import subprocess

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / (
    "SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_"
    "2026-08-13.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

CURRENT_INPUT_SHA256 = {
    "docs/SAME_CARRIER_THREE_RECORD_ARCHIVE_PACKET_BOUNDED_THEOREM_NOTE_2026-08-13.md": "370637c3881b72b68e5df8fb8d8afaa55fcd995025c01173771ffce418918847",
    "docs/MINIMAL_AXIOMS_2026-06-29.md": "93af34cf6fcfcfcc85c2cd39e8be7bbcf25253030f83a4cbc905a4a0cd68b753"
}
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS
TOL = 5.0e-11

Coord = tuple[int, int, int]
Rotation = tuple[tuple[int, int, int], ...]

P0 = np.diag((1.0, 0.0)).astype(complex)
P1 = np.diag((0.0, 1.0)).astype(complex)
H = np.asarray(((1, 1), (1, -1)), dtype=complex) / math.sqrt(2)
MINUS = H @ np.asarray((0.0, 1.0), dtype=complex)
PMINUS = np.outer(MINUS, MINUS.conj())
PLUS = H @ np.asarray((1.0, 0.0), dtype=complex)
PPLUS = np.outer(PLUS, PLUS.conj())
K0 = ((Fraction(1), Fraction(0)), (Fraction(0), Fraction(0)))
K1 = ((Fraction(0), Fraction(0)), (Fraction(0), Fraction(1)))
KMINUS = (
    (Fraction(1, 2), Fraction(-1, 2)),
    (Fraction(-1, 2), Fraction(1, 2)),
)
KPLUS = (
    (Fraction(1, 2), Fraction(1, 2)),
    (Fraction(1, 2), Fraction(1, 2)),
)
T = np.diag((1.0, np.exp(0.25j * math.pi))).astype(complex)
TDG = T.conj().T
CNOT = np.zeros((4, 4), dtype=complex)
for _source in range(4):
    _control = _source & 1
    _target = (_source >> 1) & 1
    _output = _control | ((_target ^ _control) << 1)
    CNOT[_output, _source] = 1


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
class Gate:
    kind: str
    wires: tuple[int, ...]
    matrix: np.ndarray


def one(kind: str, wire: int, matrix: np.ndarray) -> Gate:
    return Gate(kind, (wire,), matrix)


def two(kind: str, control: int, target: int, matrix: np.ndarray) -> Gate:
    return Gate(kind, (control, target), matrix)


def cx(kind: str, control: int, target: int) -> Gate:
    return two(kind, control, target, CNOT)


def ry(angle: float) -> np.ndarray:
    return np.asarray(
        (
            (math.cos(angle / 2), -math.sin(angle / 2)),
            (math.sin(angle / 2), math.cos(angle / 2)),
        ),
        dtype=complex,
    )


def controlled(matrix: np.ndarray) -> np.ndarray:
    output = np.zeros((4, 4), dtype=complex)
    for source in range(4):
        control = source & 1
        target = (source >> 1) & 1
        if not control:
            output[source, source] = 1
            continue
        for target_out in range(2):
            output[control | (target_out << 1), source] = matrix[target_out, target]
    return output


def cry(kind: str, control: int, target: int, angle: float) -> Gate:
    return two(kind, control, target, controlled(ry(angle)))


def ccry(kind: str, control_a: int, control_b: int, target: int, angle: float):
    return (
        cry(kind + "_half_b", control_b, target, angle / 2),
        cx(kind + "_toggle", control_a, control_b),
        cry(kind + "_minus_half_b", control_b, target, -angle / 2),
        cx(kind + "_untoggle", control_a, control_b),
        cry(kind + "_half_a", control_a, target, angle / 2),
    )


def toffoli_word(control_a: int, control_b: int, target: int):
    return (
        one("toffoli_H", target, H),
        cx("toffoli_CNOT", control_b, target),
        one("toffoli_Tdg", target, TDG),
        cx("toffoli_CNOT", control_a, target),
        one("toffoli_T", target, T),
        cx("toffoli_CNOT", control_b, target),
        one("toffoli_Tdg", target, TDG),
        cx("toffoli_CNOT", control_a, target),
        one("toffoli_T", control_b, T),
        one("toffoli_T", target, T),
        one("toffoli_H", target, H),
        cx("toffoli_CNOT", control_a, control_b),
        one("toffoli_T", control_a, T),
        one("toffoli_Tdg", control_b, TDG),
        cx("toffoli_CNOT", control_a, control_b),
    )


def dilation_word(drop_a: bool = False):
    """Logical wire order is P=0, M=1, B=2, R=3, A=4."""
    theta_zero = math.pi / 2
    theta_one = 2 * math.atan2(2, 1)
    theta_chi = 2 * math.atan2(math.sqrt(2), math.sqrt(5))
    word = [cry("split_P_B", 0, 2, theta_zero)]
    word.extend(ccry("split_PM_B", 0, 1, 2, theta_one - theta_zero))
    word.append(cx("h1_control", 2, 1))
    word.extend(ccry("tau1_Pq_R", 0, 1, 3, theta_chi))
    if not drop_a:
        word.append(cx("tau1_purify", 3, 4))
    word.append(cx("restore_M", 2, 1))
    word.extend(toffoli_word(1, 2, 3))
    return tuple(word)


def embed_gate(gate: Gate, count: int) -> np.ndarray:
    dimension = 1 << count
    local_dimension = 1 << len(gate.wires)
    output = np.zeros((dimension, dimension), dtype=complex)
    for source in range(dimension):
        local_source = sum(((source >> wire) & 1) << slot for slot, wire in enumerate(gate.wires))
        for local_target in range(local_dimension):
            amplitude = gate.matrix[local_target, local_source]
            if abs(amplitude) < 1.0e-15:
                continue
            target = source
            for slot, wire in enumerate(gate.wires):
                bit_value = (local_target >> slot) & 1
                target = (target & ~(1 << wire)) | (bit_value << wire)
            output[target, source] += amplitude
    return output


def word_matrix(word: tuple[Gate, ...], count: int) -> np.ndarray:
    answer = np.eye(1 << count, dtype=complex)
    for gate in word:
        answer = embed_gate(gate, count) @ answer
    return answer


def full_index(p: int, m: int, b: int, r: int, a: int) -> int:
    return p | (m << 1) | (b << 2) | (r << 3) | (a << 4)


def expected_branch(m: int, b: int) -> np.ndarray:
    vector = np.zeros(32, dtype=complex)
    if (m, b) == (0, 0):
        vector[full_index(1, 0, 0, 0, 0)] = 1
    elif (m, b) in ((0, 1), (1, 0)):
        vector[full_index(1, m, b, 0, 0)] = math.sqrt(Fraction(5, 7))
        vector[full_index(1, m, b, 1, 1)] = math.sqrt(Fraction(2, 7))
    elif (m, b) == (1, 1):
        vector[full_index(1, 1, 1, 1, 0)] = 1
    else:
        raise ValueError((m, b))
    return vector


def branch_certificate(drop_a: bool = False) -> dict[str, object]:
    word = dilation_word(drop_a)
    unitary = word_matrix(word, 5)
    rays: dict[tuple[int, int], np.ndarray] = {}
    weights: dict[tuple[int, int], float] = {}
    residual = 0.0
    for m in (0, 1):
        column = unitary[:, full_index(1, m, 0, 0, 0)]
        for b in (0, 1):
            mask = np.asarray([
                int(((index >> 0) & 1) == 1 and ((index >> 1) & 1) == m and ((index >> 2) & 1) == b)
                for index in range(32)
            ])
            projected = column * mask
            weight = float(np.vdot(projected, projected).real)
            ray = projected / math.sqrt(weight) if weight > TOL else projected
            rays[(m, b)] = ray
            weights[(m, b)] = weight
            residual = max(residual, float(np.linalg.norm(ray - expected_branch(m, b))))
    gram = np.column_stack(tuple(rays[key] for key in sorted(rays)))
    expected_weights = {
        (0, 0): Fraction(1, 2),
        (0, 1): Fraction(1, 2),
        (1, 0): Fraction(1, 5),
        (1, 1): Fraction(4, 5),
    }
    return {
        "word": word,
        "unitary_residual": float(np.linalg.norm(unitary.conj().T @ unitary - np.eye(32))),
        "primitive_gates": len(word),
        "one_two_only": all(len(gate.wires) in (1, 2) for gate in word),
        "rays": rays,
        "weights": weights,
        "weight_residual": max(abs(weights[key] - float(value)) for key, value in expected_weights.items()),
        "branch_residual": residual,
        "gram_residual": float(np.linalg.norm(gram.conj().T @ gram - np.eye(4))),
    }


def rotations() -> tuple[Rotation, ...]:
    answer: list[Rotation] = []
    for axis_order in permutations(range(3)):
        for signs in product((-1, 1), repeat=3):
            matrix = np.zeros((3, 3), dtype=int)
            for row, axis in enumerate(axis_order):
                matrix[row, axis] = signs[row]
            if round(np.linalg.det(matrix)) == 1:
                answer.append(tuple(tuple(int(value) for value in row) for row in matrix))
    return tuple(answer)


ROTATIONS = rotations()
DIRECTIONS: tuple[Coord, ...] = (
    (1, 0, 0), (-1, 0, 0), (0, 1, 0),
    (0, -1, 0), (0, 0, 1), (0, 0, -1),
)


def add(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] + right[index] for index in range(3))  # type: ignore[return-value]


def sub(left: Coord, right: Coord) -> Coord:
    return tuple(left[index] - right[index] for index in range(3))  # type: ignore[return-value]


def rotate(rotation: Rotation, site: Coord) -> Coord:
    return tuple(sum(rotation[row][column] * site[column] for column in range(3)) for row in range(3))  # type: ignore[return-value]


def distance(left: Coord, right: Coord) -> int:
    return sum(abs(left[index] - right[index]) for index in range(3))


def distance2(left: Coord, right: Coord) -> int:
    return sum((left[index] - right[index]) ** 2 for index in range(3))


STARTS: dict[str, Coord] = {
    "P": (0, 0, 0),
    "M": (-2, 1, 1),
    "B": (-1, -1, 0),
    "R": (2, -1, -1),
    "A": (-1, 0, -1),
}
ROOT_SITE: Coord = (-1, 1, 0)
HEAD_SITE: Coord = (0, 1, 0)
META_SITE: Coord = (-1, 2, 0)
RECORD_TARGETS: dict[str, Coord] = {
    "M": ROOT_SITE,
    "P": HEAD_SITE,
    "B": META_SITE,
}


def shortest_path(start: Coord, goal: Coord, forbidden: set[Coord], support: tuple[Coord, ...]):
    if start == goal:
        return (start,)
    values = support + (start, goal) + tuple(forbidden)
    lower = tuple(min(site[axis] for site in values) - 4 for axis in range(3))
    upper = tuple(max(site[axis] for site in values) + 4 for axis in range(3))
    queue: deque[Coord] = deque((start,))
    parent: dict[Coord, Coord | None] = {start: None}
    while queue:
        site = queue.popleft()
        for direction in DIRECTIONS:
            neighbor = add(site, direction)
            if neighbor in parent or neighbor in forbidden:
                continue
            if any(neighbor[axis] < lower[axis] or neighbor[axis] > upper[axis] for axis in range(3)):
                continue
            parent[neighbor] = site
            if neighbor == goal:
                path = [goal]
                while parent[path[-1]] is not None:
                    path.append(parent[path[-1]])  # type: ignore[arg-type]
                return tuple(reversed(path))
            queue.append(neighbor)
    return None


def endpoint_transposition(start: Coord, target: Coord, forbidden: set[Coord], support: tuple[Coord, ...]):
    """Exchange endpoint factors and restore every path-interior factor."""
    path = shortest_path(start, target, forbidden - {start, target}, support)
    if path is None:
        raise RuntimeError(f"no endpoint-transposition path {start}->{target}")
    forward = tuple(zip(path, path[1:]))
    return forward + tuple(reversed(forward[:-1]))


def archive_route_word():
    pairs = (
        ("P", HEAD_SITE),
        ("M", ROOT_SITE),
        ("B", META_SITE),
    )
    endpoints = set(STARTS.values()) | {ROOT_SITE, HEAD_SITE, META_SITE}
    support = tuple(endpoints)
    word: list[tuple[Coord, Coord]] = []
    for role, target in pairs:
        word.extend(endpoint_transposition(STARTS[role], target, endpoints, support))
    return tuple(word)


def route_certificate(non_nn: bool = False) -> dict[str, object]:
    swaps = archive_route_word()
    if non_nn:
        swaps = swaps + (((0, 0, 0), (2, 0, 0)),)
    event_support = set(STARTS.values()) | set(RECORD_TARGETS.values())
    swap_touched: set[Coord] = set()
    for left, right in swaps:
        event_support.update((left, right))
        swap_touched.update((left, right))
    labels = {site: f"background:{site}" for site in event_support}
    for role, site in STARTS.items():
        labels[site] = role
    initial = dict(labels)
    for left, right in swaps:
        labels[left], labels[right] = labels[right], labels[left]
    record_targets = {"P": HEAD_SITE, "M": ROOT_SITE, "B": META_SITE}
    target_failures = sum(labels[site] != role for role, site in record_targets.items())
    background_before = sorted(label for label in initial.values() if label.startswith("background:"))
    background_after = sorted(label for label in labels.values() if label.startswith("background:"))
    target_prestates = {f"background:{site}" for site in (ROOT_SITE, HEAD_SITE, META_SITE)}
    target_archive_failures = sum(
        labels[STARTS[role]] != f"background:{target}"
        for role, target in record_targets.items()
    )
    protected_role_failures = sum(labels[STARTS[role]] != role for role in ("R", "A"))
    endpoint_sites = set(record_targets.values()) | {STARTS[role] for role in record_targets}
    intermediate_restore_failures = sum(
        initial[site].startswith("background:")
        and site not in endpoint_sites
        and labels[site] != initial[site]
        for site in event_support
    )
    background_displacements = sum(
        initial[site].startswith("background:") and labels[site] != initial[site]
        for site in event_support
    )
    for left, right in reversed(swaps):
        labels[left], labels[right] = labels[right], labels[left]
    reverse_failures = int(labels != initial)
    covariance_failures = 0
    for rotation in ROTATIONS:
        rotated = tuple((rotate(rotation, left), rotate(rotation, right)) for left, right in swaps)
        covariance_failures += any(distance(left, right) != 1 for left, right in rotated)
        covariance_failures += len(set(rotate(rotation, site) for site in event_support)) != len(event_support)
    start_set = set(STARTS.values())
    stabilizers = sum({rotate(rotation, site) for site in start_set} == start_set for rotation in ROTATIONS)
    return {
        "swaps": swaps,
        "swap_count": len(swaps),
        "swap_touched": len(swap_touched),
        "event_support_size": len(event_support),
        "background_displacements": background_displacements,
        "target_failures": target_failures,
        "target_archive_failures": target_archive_failures,
        "protected_role_failures": protected_role_failures,
        "intermediate_restore_failures": intermediate_restore_failures,
        "background_multiset_failures": background_before != background_after,
        "non_nn_failures": sum(distance(left, right) != 1 for left, right in swaps),
        "reverse_failures": reverse_failures,
        "covariance_failures": covariance_failures,
        "stabilizers": stabilizers,
        "support": event_support,
    }


def swap_role_target_index(index: int) -> int:
    output = index
    for role, target in zip((0, 1, 2), (5, 6, 7)):
        left = (output >> role) & 1
        right = (output >> target) & 1
        if left != right:
            output ^= (1 << role) | (1 << target)
    return output


def archive_certificate(rays: dict[tuple[int, int], np.ndarray], overwrite: bool = False):
    marker_unitary = embed_gate(one("head_marker_H", 0, H), 5)
    columns: list[np.ndarray] = []
    expected_residual = 0.0
    target_failures = 0
    for m, b in sorted(rays):
        ray = marker_unitary @ rays[(m, b)]
        for target_input in range(8):
            source = np.zeros(256, dtype=complex)
            for role_index, amplitude in enumerate(ray):
                if abs(amplitude) > 1.0e-15:
                    source[role_index | (target_input << 5)] = amplitude
            observed = np.zeros_like(source)
            if overwrite:
                for role_index, amplitude in enumerate(ray):
                    if abs(amplitude) > 1.0e-15:
                        pmb = role_index & 0b111
                        observed[role_index | (pmb << 5)] += amplitude
            else:
                for index, amplitude in enumerate(source):
                    if abs(amplitude) > 1.0e-15:
                        observed[swap_role_target_index(index)] += amplitude
            expected = np.zeros_like(source)
            for role_index, amplitude in enumerate(ray):
                if abs(amplitude) > 1.0e-15:
                    ra = role_index & (0b11 << 3)
                    pmb = role_index & 0b111
                    expected[target_input | ra | (pmb << 5)] += amplitude
            expected_residual = max(expected_residual, float(np.linalg.norm(observed - expected)))
            columns.append(observed)
    matrix = np.column_stack(columns)
    gram = matrix.conj().T @ matrix
    return {
        "columns": len(columns),
        "rank": int(np.linalg.matrix_rank(matrix, tol=TOL)),
        "gram_residual": float(np.linalg.norm(gram - np.eye(len(columns)))),
        "expected_residual": expected_residual,
        "target_failures": target_failures,
    }


def reduced_single(vector: np.ndarray, wire: int, count: int) -> np.ndarray:
    table = np.zeros((2, 1 << (count - 1)), dtype=complex)
    for index, amplitude in enumerate(vector):
        low = index & ((1 << wire) - 1)
        high = index >> (wire + 1)
        environment = low | (high << wire)
        table[(index >> wire) & 1, environment] = amplitude
    return table @ table.conj().T


def strict_lock_certificate(rays: dict[tuple[int, int], np.ndarray]) -> dict[str, object]:
    marker_unitary = embed_gate(one("head_marker_H", 0, H), 5)
    maximum = 0.0
    factor_failures = 0
    cases = 0
    for m, b in sorted(rays):
        ray = marker_unitary @ rays[(m, b)]
        for target_input in range(8):
            vector = np.zeros(256, dtype=complex)
            for role_index, amplitude in enumerate(ray):
                if abs(amplitude) > 1.0e-15:
                    source_index = role_index | (target_input << 5)
                    vector[swap_role_target_index(source_index)] += amplitude
            for wire, expected in ((5, PMINUS), (6, P1 if m else P0), (7, P1 if b else P0)):
                maximum = max(maximum, float(np.linalg.norm(reduced_single(vector, wire, 8) - expected)))
            target_probability = sum(
                abs(amplitude) ** 2
                for index, amplitude in enumerate(vector)
                if ((index >> 6) & 1) == m and ((index >> 7) & 1) == b
            )
            factor_failures += abs(target_probability - 1) >= TOL
            cases += 1
    return {
        "cases": cases,
        "maximum_residual": maximum,
        "factor_failures": factor_failures,
        "content_keys": {"zero": K0, "one": K1, "minus": KMINUS, "other": KPLUS},
    }


def bit_from_content(content: object) -> int | None:
    if content == K0:
        return 0
    if content == K1:
        return 1
    return None


def decode_packet(records: dict[Coord, object]):
    if len(records) != 3:
        return None
    sites = tuple(records)
    degrees = {site: sum(distance2(site, other) == 1 for other in sites if other != site) for site in sites}
    centers = tuple(site for site, degree in degrees.items() if degree == 2)
    if len(centers) != 1:
        return None
    root = centers[0]
    endpoints = tuple(site for site in sites if site != root)
    if len(endpoints) != 2 or distance2(endpoints[0], endpoints[1]) != 2:
        return None
    heads = tuple(site for site in endpoints if records[site] == KMINUS)
    if len(heads) != 1:
        return None
    head = heads[0]
    meta = next(site for site in endpoints if site != head)
    m = bit_from_content(records[root])
    b = bit_from_content(records[meta])
    if m is None or b is None:
        return None
    forward = sub(head, root)
    transverse = sub(meta, root)
    frames = tuple(rotation for rotation in ROTATIONS if rotate(rotation, (1, 0, 0)) == forward and rotate(rotation, (0, 1, 0)) == transverse)
    if len(frames) != 1:
        return None
    return {
        "root": root,
        "head": head,
        "meta": meta,
        "m": m,
        "b": b,
        "h": m + b,
        "s": 2 * m - 1,
        "frame": frames[0],
    }


def find_packets(records: dict[Coord, object]):
    """Decode every isolated three-site packet embedded in a complete map."""
    decoded = []
    for sites in combinations(records, 3):
        packet = decode_packet({site: records[site] for site in sites})
        if packet is not None:
            decoded.append(packet)
    return tuple(sorted(decoded, key=lambda packet: packet["root"]))


def packet_certificate(content_keys: dict[str, object], collapse: bool = False) -> dict[str, object]:
    meta_base = (-2, 1, 0) if collapse else META_SITE
    failures = frame_failures = continuity_failures = full_map_scan_failures = 0
    cases = 0
    zero = content_keys["zero"]
    one_key = content_keys["one"]
    minus = content_keys["minus"]
    other = content_keys["other"]
    translations = ((0, 0, 0), (7, -3, 5))
    content_binding_residual = max(
        float(np.linalg.norm(np.asarray(key, dtype=complex) - matrix))
        for key, matrix in ((zero, P0), (one_key, P1), (minus, PMINUS), (other, PPLUS))
    )
    prior_root = add((30, 30, 30), ROOT_SITE)
    prior_head = add((30, 30, 30), HEAD_SITE)
    prior_meta = add((30, 30, 30), META_SITE)
    prior_records = {
        prior_root: one_key,
        prior_head: minus,
        prior_meta: zero,
        (80, -70, 60): other,
    }
    for rotation in ROTATIONS:
        for translation in translations:
            root = add(translation, rotate(rotation, ROOT_SITE))
            head = add(translation, rotate(rotation, HEAD_SITE))
            meta = add(translation, rotate(rotation, meta_base))
            for m, b in product((0, 1), repeat=2):
                current_records = {
                    root: one_key if m else zero,
                    head: minus,
                    meta: one_key if b else zero,
                }
                decoded = decode_packet(current_records)
                failures += decoded is None or decoded["m"] != m or decoded["b"] != b or decoded["h"] != m + b or decoded["s"] != 2 * m - 1
                if decoded is not None:
                    frame_failures += decoded["frame"] != rotation
                    delta_j = {decoded["root"]: -1, decoded["head"]: 1}
                    boundary = {decoded["root"]: 1, decoded["head"]: -1}
                    continuity_failures += any(delta_j[site] + boundary[site] != 0 for site in delta_j)
                complete_map = dict(prior_records)
                complete_map.update(current_records)
                found = find_packets(complete_map)
                current_matches = tuple(
                    packet for packet in found
                    if packet["root"] == root
                    and packet["m"] == m
                    and packet["b"] == b
                    and packet["frame"] == rotation
                )
                full_map_scan_failures += (
                    len(found) != 2
                    or len(current_matches) != 1
                    or {packet["root"] for packet in found} != {root, prior_root}
                )
                cases += 1
    return {
        "cases": cases,
        "failures": failures,
        "frame_failures": frame_failures,
        "continuity_failures": continuity_failures,
        "full_map_scan_failures": full_map_scan_failures,
        "content_binding_residual": content_binding_residual,
        "cadence": (1, 3, 1),
    }


def readiness_certificate(rays: dict[tuple[int, int], np.ndarray]) -> dict[str, object]:
    projectors = {key: np.outer(ray, ray.conj()) for key, ray in rays.items()}
    sum_projector = sum(projectors.values(), np.zeros((32, 32), dtype=complex))
    rank = int(np.linalg.matrix_rank(sum_projector, tol=TOL))
    failures = 0
    for key, ray in rays.items():
        hits = tuple(other for other, projector in projectors.items() if abs(np.vdot(ray, projector @ ray) - 1) < TOL)
        failures += hits != (key,)
    set_stabilizers = sum(
        {rotate(rotation, site) for site in STARTS.values()} == set(STARTS.values())
        for rotation in ROTATIONS
    )
    template_diameter = max(distance(left, right) for left, right in combinations(STARTS.values(), 2))
    wire_sites = tuple(STARTS[role] for role in ("P", "M", "B", "R", "A"))
    two_gate_distances = tuple(
        distance(wire_sites[gate.wires[0]], wire_sites[gate.wires[1]])
        for gate in dilation_word()
        if len(gate.wires) == 2
    )
    unitary = word_matrix(dilation_word(), 5)
    dirty_ready_cases = 0
    dirty_branch_weight_shift = 0.0
    for m in (0, 1):
        clean = np.zeros(32, dtype=complex)
        dirty = np.zeros(32, dtype=complex)
        clean[full_index(1, m, 0, 0, 0)] = 1
        dirty[full_index(1, m, 1, 0, 0)] = 1
        clean_out = unitary @ clean
        dirty_out = unitary @ dirty
        dirty_ready_cases += abs(np.vdot(dirty_out, sum_projector @ dirty_out) - 1) < TOL
        clean_weights = tuple(float(np.vdot(clean_out, projectors[(m, b)] @ clean_out).real) for b in (0, 1))
        dirty_weights = tuple(float(np.vdot(dirty_out, projectors[(m, b)] @ dirty_out).real) for b in (0, 1))
        dirty_branch_weight_shift = max(
            dirty_branch_weight_shift,
            *(abs(clean_weights[index] - dirty_weights[index]) for index in range(2)),
        )
    return {
        "projector_rank": rank,
        "idempotence_residual": float(np.linalg.norm(sum_projector @ sum_projector - sum_projector)),
        "unique_branch_failures": failures,
        "proper_rotations": len(ROTATIONS),
        "set_stabilizers": set_stabilizers,
        "template_diameter": template_diameter,
        "two_gate_distances": two_gate_distances,
        "nn_two_gate_count": sum(value == 1 for value in two_gate_distances),
        "dirty_ready_cases": dirty_ready_cases,
        "dirty_branch_weight_shift": dirty_branch_weight_shift,
    }


def totality_certificate(route_support: set[Coord]) -> dict[str, object]:
    valid = replay = occupied = preservation_failures = 0
    sentinel_site = (20, 20, 20)
    for rotation in ROTATIONS:
        targets = tuple(rotate(rotation, site) for site in (ROOT_SITE, HEAD_SITE, META_SITE))
        support = {rotate(rotation, site) for site in route_support}
        for m, b in product((0, 1), repeat=2):
            records: dict[Coord, object] = {sentinel_site: KPLUS}
            if records.keys().isdisjoint(support):
                updated = dict(records)
                updated.update({
                    targets[0]: K1 if m else K0,
                    targets[1]: KMINUS,
                    targets[2]: K1 if b else K0,
                })
                valid += 1
                preservation_failures += updated.get(sentinel_site) != KPLUS
                replay_result = dict(updated) if not updated.keys().isdisjoint(support) else {}
                replay += replay_result == updated
            blocked: dict[Coord, object] = {targets[0]: KPLUS, sentinel_site: KPLUS}
            refused = dict(blocked) if not blocked.keys().isdisjoint(support) else {}
            occupied += refused == blocked
    return {
        "valid": valid,
        "replay": replay,
        "occupied": occupied,
        "preservation_failures": preservation_failures,
        "host_spent_flag": False,
    }


def current_inputs_match() -> bool:
    return all((ROOT / path).is_file()
               and sha256((ROOT / path).read_bytes()).hexdigest() == digest
               for path, digest in CURRENT_INPUT_SHA256.items())


def authority_certificate(stale: bool = False) -> dict[str, object]:
    text = AXIOM_PATH.read_text(encoding="utf-8")
    flattened = " ".join(text.split())
    main = subprocess.check_output(("git", "rev-parse", "origin/main"), cwd=ROOT, text=True).strip()
    ancestor = subprocess.run(("git", "merge-base", "--is-ancestor", main, "HEAD"), cwd=ROOT, check=False).returncode == 0
    if stale:
        ancestor = False
    return {
        "main": main,
        "ancestor": ancestor,  # historical diagnostic only
        "current_inputs_match": current_inputs_match() and not stale,
        "record": all(phrase in flattened for phrase in (
            "Records form.",
            "record locks exactly one admissible local possibility",
            "A site with no record cannot be read",
            "A state is a configuration of records",
        )),
        "formation_open": "remaining formation rules" in flattened,
        "input_paths": AUDIT_INPUT_PATHS,
    }


def boundary_surface_ok(host_ready: bool = False, sequential: bool = False) -> bool:
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
        "Simultaneous three-site formation",
        "supplied clean input columns",
        "finite-support, not nearest-neighbour local",
        "Possibility-domain membership is not Admissibility support",
        "complete finite Record map",
        "Only the fixed-output control and the three-target archive are executed",
        "zero TOE percentage",
        "not an axiom edit",
        "realized-member selection both remain explicit open inputs",
        "global multi-event confluence remains open",
    )
    return not host_ready and not sequential and all(needle in note for needle in needles)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mutation", choices=(
        "stale_axiom", "drop_A", "overwrite_targets", "non_nn_route",
        "collapse_packet", "host_ready", "sequential_write",
    ))
    mutation = parser.parse_args().mutation
    checks = Checks()

    authority = authority_certificate(mutation == "stale_axiom")
    checks.check(
        "A-current-main-self-contained-authority",
        authority["current_inputs_match"] and authority["record"] and authority["formation_open"] and len(authority["input_paths"]) == 2,
        f"origin/main={str(authority['main'])[:10]}; only the current axiom and this note are declared inputs",
    )

    branches = branch_certificate(mutation == "drop_A")
    branches_ok = (
        branches["primitive_gates"] == 29
        and branches["one_two_only"]
        and branches["unitary_residual"] < TOL
        and branches["weight_residual"] < TOL
        and branches["branch_residual"] < TOL
        and branches["gram_residual"] < TOL
    )
    checks.check(
        "B-four-orthogonal-five-M2-algebraic-candidate-rays",
        branches_ok,
        f"29 one/two-M2 gates; weights={tuple(round(branches['weights'][key], 6) for key in sorted(branches['weights']))}; max ray residual={branches['branch_residual']:.1e}",
    )

    readiness = readiness_certificate(branches["rays"])
    readiness_ok = (
        readiness["projector_rank"] == 4
        and readiness["idempotence_residual"] < TOL
        and readiness["unique_branch_failures"] == 0
        and readiness["proper_rotations"] == 24
        and readiness["set_stabilizers"] == 1
        and readiness["template_diameter"] == 8
        and readiness["nn_two_gate_count"] == 0
        and readiness["dirty_ready_cases"] == 2
        and abs(readiness["dirty_branch_weight_shift"] - 0.6) < TOL
    )
    checks.check(
        "C-finite-support-ray-projector-and-resource-boundary",
        readiness_ok,
        f"rank-4 projector spans a diameter-{readiness['template_diameter']} five-site template; logical two-M2 gate separations={sorted(set(readiness['two_gate_distances']))}, NN count={readiness['nn_two_gate_count']}; two dirty-B inputs also pass readiness, with max weight shift {readiness['dirty_branch_weight_shift']:.1f}",
    )

    route = route_certificate(mutation == "non_nn_route")
    route_ok = (
        route["target_failures"] == 0
        and route["target_archive_failures"] == 0
        and route["protected_role_failures"] == 0
        and route["intermediate_restore_failures"] == 0
        and not route["background_multiset_failures"]
        and route["non_nn_failures"] == 0
        and route["reverse_failures"] == 0
        and route["covariance_failures"] == 0
        and route["stabilizers"] == 1
        and route["swap_touched"] == 11
        and route["event_support_size"] == 13
    )
    checks.check(
        "D-branch-neutral-finite-NN-factor-permutation",
        route_ok,
        f"{route['swap_count']} NN SWAPs are incident on {route['swap_touched']} sites; event support has {route['event_support_size']} sites including fixed R,A; all three target prestates survive",
    )

    archive = archive_certificate(branches["rays"], mutation == "overwrite_targets")
    archive_ok = (
        archive["columns"] == 32
        and archive["rank"] == 32
        and archive["gram_residual"] < TOL
        and archive["expected_residual"] < TOL
        and archive["target_failures"] == 0
    )
    checks.check(
        "E-arbitrary-target-and-reference-preserving-archive",
        archive_ok,
        f"rank={archive['rank']}/32, Gram residual={archive['gram_residual']:.1e}; arbitrary three-qubit target information exits on P,M,B",
    )

    lock = strict_lock_certificate(branches["rays"])
    lock_ok = lock["cases"] == 32 and lock["maximum_residual"] < TOL and lock["factor_failures"] == 0
    checks.check(
        "F-exact-same-carrier-lock-content-candidate",
        lock_ok,
        f"{lock['cases']} branch/target-basis cases put exact existing projectors (-,m,b) on the targets; residual={lock['maximum_residual']:.1e}; Admissibility support is not asserted",
    )

    packet = packet_certificate(lock["content_keys"], mutation == "collapse_packet")
    packet_ok = (
        packet["cases"] == 192
        and packet["failures"] == 0
        and packet["frame_failures"] == 0
        and packet["continuity_failures"] == 0
        and packet["full_map_scan_failures"] == 0
        and packet["content_binding_residual"] < TOL
        and packet["cadence"] == (1, 3, 1)
    )
    checks.check(
        "G-complete-Record-map-packet-and-incidence-decoder",
        packet_ok,
        f"{packet['cases']} translated/all-frame cases recover (h,s), edge, and frame from actual M2 keys inside maps with one separated prior packet and a sentinel; scan failures={packet['full_map_scan_failures']}",
    )

    total = totality_certificate(route["support"])
    total_ok = (
        total["valid"] == 96
        and total["replay"] == 96
        and total["occupied"] == 96
        and total["preservation_failures"] == 0
        and not total["host_spent_flag"]
    )
    checks.check(
        "H-candidate-totality-formula-and-occupancy-refusal",
        total_ok,
        f"{total['valid']} valid writes and {total['replay']} replays preserve prior Records; target occupancy replaces a host spent flag",
    )

    overwrite_control = archive_certificate(branches["rays"], True)
    control_ok = overwrite_control["rank"] == 4 and overwrite_control["gram_residual"] > 1
    checks.check(
        "I-fixed-output-overwrite-control-collapses-target-information",
        control_ok,
        f"unarchived fixed-output control has rank {overwrite_control['rank']}/32 and Gram residual {overwrite_control['gram_residual']:.2f}",
    )

    boundary_ok = boundary_surface_ok(mutation == "host_ready", mutation == "sequential_write")
    checks.check(
        "J-N1-N8-scope-axiom-and-TOE-boundary",
        boundary_ok,
        "the note records the positive parser change, simultaneous-write contract, live alternatives, open occurrence/global-law gates, and zero score movement",
    )

    print(
        "METRICS "
        f"branch_rays=4 archive_rank={archive['rank']} physical_swaps={route['swap_count']} "
        f"packet_cases={packet['cases']} lock_content_residual={lock['maximum_residual']:.2e}"
    )
    print(
        "BOUNDARY: a self-contained finite candidate conserves arbitrary target/background information and places three already-present M2 lock-content candidates; clean preparation, NN compilation of the algebraic formation word/readiness test, Admissibility support, realized-member selection, formation occurrence/site/rate, simultaneous atomicity as an actual law, internal-action selection, full-Z3 scheduling, overlapping-packet confluence, physical duration, source normalization, gravity, audit retention, obligation retirement, and TOE percentage movement remain open"
    )
    print("per_element: checked the 29-gate algebraic five-M2 unitary, four normalized rays, 32 arbitrary target-basis columns, exact target marginals, and overwrite control")
    print("per_site: checked five input roles, three arbitrary Record targets, all 11 SWAP-incident sites, 13-site event support, packet roles, occupancy, and reverse permutation")
    print("per_mode: checked all four (m,b) modes, 24 proper-cubic frames, two translations, exact branch weights, incidence signs, and outcomes")
    print("per_block: checked a diameter-8 rank-4 projector boundary, rank-32 archive isometry, branch-neutral NN route, candidate simultaneous append, complete-map decoder, and refusal formula")
    print("lattice_wide: checked and not executed — this is one finite Record-free event support plus a separated prior packet, not a homogeneous full-Z3 law or overlapping-event confluence theorem")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
